# Agrobactin: exact-product grades exceed the native catechol assay

- Review: 20261021T111801Z-agrobactin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T11:06:01.596482Z
- Finished UTC: 2026-10-21T11:18:01.720159Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The imported native knockout measured total catechol, so its two exact-product grades require a guarded downgrade. Six native protein examples, three proposed reactions and four precursor groundings agree with current direct authorities. Full historical identity and taxon-source evidence remain unavailable or unresolved; the four occurrence triples are assessed separately.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 46, batch 005, selected in path order from the fresh-main authoritative validated catalogue and the separately validated pending-PR targets. At selection, 94 of 3116 current records had campaign coverage and 3022 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-bb581c6679 | data/natural_products/alkaloids/agrobactin.yaml | generated | agrobactin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-bb581c6679 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-bb581c6679 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-bb581c6679 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-bb581c6679 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-bb581c6679 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-bb581c6679 | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Original 2002 experiment and product specificity | failed | True | naturalproductmech:mibig-bb581c6679 | The required exact-product support check fails: the agbB knockout demonstrates total catechol and iron-limited growth, not chemically identified agrobactin from MAFF301001. This is a scientific finding, not a failed command. |
| Original historical isolation and absolute-stereochemical bridge | unavailable | True | naturalproductmech:mibig-bb581c6679 | Required full 1979/1980 identity and source-organism review remains incomplete after the retained bounded access attempts. The 1979 abstract supports named B6 isolation and relative trans substitution; the indexed crystal excerpt expressly leaves absolute configuration unproved in that study. Current database agreement does not replace this missing primary bridge. |
| All six deposited CDS and UniProt examples | passed | True | naturalproductmech:mibig-bb581c6679 | Actual local audit exit 0 at 2026-10-21T11:10:53.634894Z. All six native reference translations, lengths, stable protein IDs and UniProt complete sequences match; all six UniProt entries remain unreviewed. |
| Proposed Rhea reactions and exact precursor groundings | passed | True | naturalproductmech:mibig-bb581c6679 | All three current reaction identifiers and four exact charged precursor structures agree with the record and current UniProt predictions. The route is a substrate/product summary, not a complete stoichiometric graph; omission of water, pyruvate and nicotinamide cofactors from the diagram does not turn it into an erroneous balanced equation. |
| Exact graph and external identifier resolution | passed | True | naturalproductmech:mibig-bb581c6679 | Six independently parsed graphs agree in full standardized and fixed-H identity; eligible grounding and source concept are verified within the stated inventories. |
| Applicable native expression dataset | not_applicable | False | naturalproductmech:mibig-bb581c6679 | No matching organism/strain dataset appears in the complete retained catalogue. |

## Scientific And Domain Assessments

### Native origin and exact strain boundary

evidence: supported. Targets: naturalproductmech:mibig-bb581c6679.

The original 1979 abstract supports named agrobactin from native B6 low-iron cultures. The 2002 MAFF301001 experiment is a separate native strain/locus catechol phenotype; its E. coli strains are cloning and conjugation hosts. No heterologous agrobactin production or identity of B6 with MAFF301001 is inferred.

### Exact agrobactin producer and locus demonstration

evidence: concern. Targets: naturalproductmech:mibig-bb581c6679.

The imported Knock-out studies method is real but its measured chemical endpoint is too broad for this exact product. BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED therefore overstate exact agrobactin support. Preserve the native catechol phenotype and the source association separately.

### Six proposed steps and the partial 11-node, 10-edge graph

graph: supported. Targets: naturalproductmech:mibig-bb581c6679.

All six pathway steps are explicitly proposed. AgbC/B/A reaction notes distinguish UniProt prediction from direct assays, the graph retains prediction language, and it has no terminal agrobactin product edge. The 2002 paper supports cloned genes, homology hypotheses and the native agbB phenotype, not six purified-enzyme experiments. Those already-qualified hypotheses are not counted as additional confirmed errors.

### 2002 LOTUS occurrence at taxon 358

evidence: supported. Targets: naturalproductmech:mibig-bb581c6679.

The 2002 introduction explicitly reports the earlier B6 agrobactin isolation and cites Ong 1979, so it supplies secondary/background support at the historical A. tumefaciens label. It is not a new MAFF301001 isolation, an independent replicate or an exact-stereochemical determination. A blanket claim that this citation contains no agrobactin occurrence support would be inaccurate. The original 1979 abstract supplies the direct native-isolation lead.

### 2002 LOTUS occurrence at taxon 362

evidence: unknown. Targets: naturalproductmech:mibig-bb581c6679.

The full paper concerns historical A. tumefaciens B6 background and MAFF301001 experimental material; it does not supply a separately traced taxon 362 stock or exact-product isolate. Retain uncertainty about the LOTUS taxonomic attribution pending the authority and strain bridge; do not silently equate identifiers 358 and 362 or infer universal absence.

### Both 1980 LOTUS occurrence triples and absolute identity

evidence: unknown. Targets: naturalproductmech:mibig-bb581c6679.

The original crystallography article was not available in full. Its indexed paragraph establishes a trans relative assignment and a study-specific absolute-configuration limit, but does not settle the complete source-organism, stock or modern taxon mapping for either LOTUS triple. Lack of access alone does not justify excluding either occurrence.

### Biological-function evidence and unresolved terminal biosynthesis

completeness: supported. Targets: naturalproductmech:mibig-bb581c6679.

The owner explicitly leaves terminal agrobactin assembly unresolved. The historical original abstract also provides native iron-acquisition function, but does not justify a molecular target or unqualified cross-species assay claim. Optional quantitative bioactivity and a fully resolved biosynthetic route are not required additions without claim-specific primary detail.

### Native reference proteins and gene identity

grounding: supported. Targets: naturalproductmech:mibig-bb581c6679.

AgbC Q8GRA0/BAC16757.2 (342 aa), AgbB Q8GR98/BAC16759.1 (289 aa), AgbA Q8GR97/BAC16760.1 (251 aa), AgbD Q83VM4/BAC57934.1 (241 aa), AgbE Q8GR99/BAC16758.1 (541 aa) and AgbF Q83VM5/BAC57933.1 (548 aa) are exact current AB083344.2 sequence matches. None is promoted to a reviewed, purified or stock-specific protein.

### Protein function and reaction support

evidence: supported. Targets: naturalproductmech:mibig-bb581c6679.

AgbC/B/A Rhea reactions are ARBA predictions. AgbD has automatic EntD-family/enterobactin annotations; only the phosphopantetheinyl-transferase candidate role is transferred, not proof of enterobactin production, an Agb complex or exact agrobactin assembly. AgbE and AgbF carry probable submitted functions. The owner already preserves these distinctions.

### Four charged precursor nodes and three reaction references

grounding: supported. Targets: naturalproductmech:mibig-bb581c6679.

The two dianions and two monoanions match current 3-star structures, including (2S,3S)-dihydroxy-dihydrobenzoate. The full Rhea equations include the expected small participants and NAD pair. Exact reaction grounding does not supply an experimental enzyme assay.

### 2002 sequence report versus current version 2

provenance: supported. Targets: naturalproductmech:mibig-bb581c6679.

The 2002 paper describes four ORFs and reports agbC as 1,176 bp. Current AB083344.2 has six complete CDSs and a 1,029 bp agbC (342 aa); it replaced version 1 in March 2003. The owner correctly specifies current version-2 sequences and cites direct databases for AgbD/F. Do not infer that the historical paper assayed these six exact current sequences, or that its 1,176 bp AgbC was the current 342 aa reference.

### Historical gene-annotation locator

provenance: unknown. Targets: naturalproductmech:mibig-bb581c6679.

The retrieved current MIBiG annotations JSON does not reproduce the historical gene-annotation statements in the owner. The historical September page was not archived in this packet, so no confirmed contradiction with that earlier snapshot is asserted. All six sequence crosswalks are independently supported by the current direct sequence authorities.

### Current graph and exact external xrefs

identity: supported. Targets: naturalproductmech:mibig-bb581c6679.

Six current representations agree on complete identity and fixed-H form. NPA018820 resolves exactly, while the unavailable original absolute-configuration derivation remains a separate scientific limit.

### Minted identity and active source concept

provenance: supported. Targets: naturalproductmech:mibig-bb581c6679.

Current exact ChEBI211827 has two stars and no eligible exact row is present in the complete pinned three-star inventory. MIBiG version2 resolves; its correct source provenance does not establish the overclaimed exact-product phenotype.

### Historical organism names versus distinct current species

scope: unknown. Targets: naturalproductmech:mibig-bb581c6679.

Both taxon IDs resolve, and the historical Rhizobium label is a recognized synonym for362. However358 and362 are separate current species, so two names do not establish duplicate observations or the same experimental stock. The primary historical strain-to-modern-species applicability remains qualified where not directly established.

### Existing proposed mechanism and audit trail

provenance: supported. Targets: naturalproductmech:mibig-bb581c6679.

All five native history events remain intact, including the prior correction that removed an unsupported terminal product edge and retained proposed reaction scope. Current SEEDED status is unchanged. These resolved details are not repeated as new findings.

### Computational classification attribution

provenance: supported. Targets: naturalproductmech:mibig-bb581c6679.

Classification is retained as a versioned computational output, not a newly demonstrated biosynthetic reaction.

## Findings

### S046-F-EXACT-PRODUCT-GRADE: The native knockout endpoint does not establish exact agrobactin production

major / open / confirmed; issue key: agrobactin-bgc0002474-catechol-knockout-not-exact-product.

Sonoda 2002 demonstrates that the MAFF301001 agb region is necessary for iron-limited growth and catechol output, measured by a colorimetric total-catechol assay. Agrobactin from B6 is cited as historical background and gives the genes their name; the study does not identify the MAFF301001 product as that exact molecular structure. Importing Knock-out studies into BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED on this compound therefore exceeds the product specificity of the experiment. This does not refute agrobactin production by B6, the observed catechol phenotype, the deposited locus, or the explicitly proposed pathway.

## Recommended Actions And Acceptance Checks

### S046-ACTION-WITHDRAW

Add a consumed WITHDRAW decision for naturalproductmech:mibig-bb581c6679, source MIBIG, source_id BGC0002474 (compound selector BGC0002474:1), expected_entry_version 2, expected_taxon_id NCBITaxon:358, expected_genome_accession AB083344.2, expected_locus_from and expected_locus_to both explicitly empty, expected_standard_inchi_key BWPMKVHHFNGYEN-CJAUYULYSA-N, and expected_locus_evidence_methods Knock-out studies. Set replacement locus_evidence_methods empty and attribute the decision to DOI:10.1266/ggs.77.137 with curator, actual decision date and the Arnow endpoint rationale. The complete raw-row audit digest is fbca66b5711f7b1e2120450b8acc1fd545cfe65272f2818a4fb04960a66095dd; the current WITHDRAW consumer enforces the named context fields, not an arbitrary expected_source_row_sha256 column. Preserve the untouched raw inventory and regenerate normally. This downgrades the imported producer to SOURCE_ASSERTION and locus to CLUSTER_UNSTATED while retaining both rows and emitting the experimental qualification. Retain B6 native isolation, the MAFF301001 catechol phenotype and all explicitly proposed protein/reaction hypotheses with their separate scopes. Do not repair this by replacing the method with an unsupported stronger experiment, deleting the locus, attaching B6 as the MAFF301001 strain, or editing the generated owner directly.

- Reject a changed version, taxon, accession, bound, full key or original method, and reject zero or multiple matching source rows. Both empty bounds must be supplied explicitly. Recompute the complete raw-row digest during implementation and re-review any additional-field drift rather than pretending the current override validates all fields.
- The regenerated exact-product imported grades are SOURCE_ASSERTION and CLUSTER_UNSTATED; producer and BGC associations remain, raw Knock-out studies remains available in provenance and the qualification explains the total-catechol endpoint.
- Keep the separate native B6 isolation and the MAFF301001 experiment distinct. Preserve all six proposed steps and the partial graph unless a new, separately supported reaction finding requires change; never recreate a demonstrated terminal agrobactin edge.
- Assess each LOTUS row separately: the 2002 taxon-358 triple has historical B6 background support, while its taxon-362 bridge and the full 1980 source mapping remain unresolved. Do not automatically withdraw all four triples or treat two species identifiers as synonyms. Any later justified exclusion must use its exact key/taxon/DOI and full row hash retained in the audit.
- Add attribution and the required curation event through the documented authorized workflow, then run strict target validation, provenance, corpus integrity, byte reproduction and required QC. Do not promote scientific status while historical primary identity or taxon-source questions remain unresolved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| S046-OWNER | data/natural_products/alkaloids/agrobactin.yaml; Complete generated owner, all six proposed steps and all 11 nodes / 10 edges | supports | The imported exact agrobactin source has BGC_CHARACTERIZED producer and CLUSTER_DEMONSTRATED locus grades from Knock-out studies. Its pathway already labels the enzyme steps proposed and leaves the terminal route unresolved. Four LOTUS occurrence triples use two publications across two taxon identifiers. |
| S046-RAW | data/raw/mibig_compounds.tsv; data/raw/lotus_occurrences.tsv; /private/tmp/npm-review-work/046/local-sources.json | supports | Exact BGC0002474:1 version 2 row and four LOTUS rows were inspected, including all fields. Complete raw MIBiG row SHA256 fbca66b5711f7b1e2120450b8acc1fd545cfe65272f2818a4fb04960a66095dd. Each LOTUS selector and complete row hash is retained in protein-reaction-audit.json. |
| S046-2002 | DOI:10.1266/ggs.77.137; /private/tmp/npm-review-work/shared-next-batch005/agrobactin/2002-primary.pdf | supports | Entire original article, printed pp. 137–146, was read. MAFF301001 rif and its agbB::Gm mutant MIUB were compared in LB with or without 200 micromolar 2,2-prime-dipyridyl. The native phenotype is growth and total catechol in the Arnow assay with a catechol standard (Methods p. 140; Figs. 5–6 pp. 144–145). Four agb genes were assigned functions by homology. The introduction and naming discussion attribute earlier agrobactin isolation to B6 and cite Ong 1979; no target-resolved chemical identification of the MAFF301001 catechol product is reported. |
| S046-1979 | DOI:10.1016/S0021-9258(17)37736-0; /private/tmp/npm-review-work/shared-next-batch005/agrobactin/1979-pubmed.xml | supports | Complete official original abstract read, not the full article. It reports isolation of agrobactin from iron-limited A. tumefaciens B6 cultures, a spermidine/threonyl/tricatechol scaffold with trans oxazoline substituents and native iron-starvation rescue. Acid-opened agrobactin A is a distinct species; its heterologous iron-feeding behavior must not be transferred to intact agrobactin. The abstract does not independently establish the complete modern absolute-stereochemical graph. |
| S046-1980-EXCERPT | DOI:10.1021/ja00546a014; /private/tmp/npm-review-work/shared-next-batch005/agrobactin/1980-indexed-stereo-excerpt.json | supports | Only a search-indexed excerpt of original printed p. 7723 was available. The authors describe the trans relative configuration but explicitly do not prove absolute configuration in this crystal study; one L configuration is assumed in the figures. This is a source-specific limitation, not proof that the current assignment is wrong or that later work did not resolve it. |
| S046-HISTORICAL-ACCESS | DOI:10.1021/ja00546a014; DOI:10.1016/S0021-9258(17)37736-0; /private/tmp/npm-review-work/shared-next-batch005/agrobactin/source-notes.json | context_only | The retained primary-source preparation records failed original 1979 full-text routes and failed 1980 full-PDF routes. The successful 1979 PubMed abstract and indexed 1980 paragraph are explicitly distinguished from full articles. No absence of a paper or of later absolute-configuration proof is inferred. |
| S046-REPAIR-OWNERS | scripts/seed_from_sources.py; src/naturalproductmech/grading.py; conf/producer_evidence.tsv; src/naturalproductmech/curate/lotus_exclusions.py; src/naturalproductmech/curate/claim_references.py; Seeder lines 467–567 and 790–835; complete grading and LOTUS/claim-reference consumers | supports | WITHDRAW requires exact source/version/taxon/accession/bounds/key/original-method guards and empty replacement methods; it downgrades both grades while retaining producer and locus assertions. LOTUS exclusion instead requires an exact structure/taxon/DOI selector and complete raw-row SHA. A normal REPLACE override does not provide those WITHDRAW guards. Neither action should be confused with deletion of the compound, producer or locus. |
| P046-GENBANK | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=AB083344.2&amp;rettype=gb&amp;retmode=text; /private/tmp/npm-review-work/046/identity/genbank.gb | supports | Current AB083344.2 is a 7,390 bp linear-chromosome MAFF301001 reference, with six complete CDSs and a comment that it replaced version 1 on 2003-03-03. Coordinates, codon tables, start/stop codons and complete translated sequences were inspected; these are deposited references, not assay-stock sequences. |
| P046-Q83VM5 | https://rest.uniprot.org/uniprotkb/Q83VM5.json; /private/tmp/npm-review-work/046/identity/uniprot-Q83VM5.json | supports | Current unreviewed Q83VM5, agbF, 548 aa, maps through EMBL AB083344 to BAC57933.1 at complement(104..1750); full sequence independently matches the current CDS translation. Protein existence: 4: Predicted. Sequence identity does not establish the proposed function or exact experimental stock. |
| P046-Q8GRA0 | https://rest.uniprot.org/uniprotkb/Q8GRA0.json; /private/tmp/npm-review-work/046/identity/uniprot-Q8GRA0.json | supports | Current unreviewed Q8GRA0, agbC, 342 aa, maps through EMBL AB083344 to BAC16757.2 at 1949..2977; full sequence independently matches the current CDS translation. Protein existence: 3: Inferred from homology. Sequence identity does not establish the proposed function or exact experimental stock. |
| P046-Q8GR99 | https://rest.uniprot.org/uniprotkb/Q8GR99.json; /private/tmp/npm-review-work/046/identity/uniprot-Q8GR99.json | supports | Current unreviewed Q8GR99, agbE, 541 aa, maps through EMBL AB083344 to BAC16758.1 at 3142..4767; full sequence independently matches the current CDS translation. Protein existence: 4: Predicted. Sequence identity does not establish the proposed function or exact experimental stock. |
| P046-Q8GR98 | https://rest.uniprot.org/uniprotkb/Q8GR98.json; /private/tmp/npm-review-work/046/identity/uniprot-Q8GR98.json | supports | Current unreviewed Q8GR98, agbB, 289 aa, maps through EMBL AB083344 to BAC16759.1 at 4860..5729; full sequence independently matches the current CDS translation. Protein existence: 4: Predicted. Sequence identity does not establish the proposed function or exact experimental stock. |
| P046-Q8GR97 | https://rest.uniprot.org/uniprotkb/Q8GR97.json; /private/tmp/npm-review-work/046/identity/uniprot-Q8GR97.json | supports | Current unreviewed Q8GR97, agbA, 251 aa, maps through EMBL AB083344 to BAC16760.1 at 5743..6498; full sequence independently matches the current CDS translation. Protein existence: 3: Inferred from homology. Sequence identity does not establish the proposed function or exact experimental stock. |
| P046-Q83VM4 | https://rest.uniprot.org/uniprotkb/Q83VM4.json; /private/tmp/npm-review-work/046/identity/uniprot-Q83VM4.json | supports | Current unreviewed Q83VM4, agbD, 241 aa, maps through EMBL AB083344 to BAC57934.1 at 6529..7254; full sequence independently matches the current CDS translation. Protein existence: 3: Inferred from homology. Sequence identity does not establish the proposed function or exact experimental stock. |
| P046-CHEBI29748 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/29748/; /private/tmp/npm-review-work/046/identity/chebi29748.json | supports | Current 3-star CHEBI:29748 is chorismate(2-), charge -2, full key WTFXTQVDAKGDEY-HTQZYQBOSA-L. RDKit independently reproduced the deposited key and charge from the authority SMILES. This confirms the graph node's exact ionic/stereochemical referent, not its detection in the 2002 experiment. |
| P046-CHEBI29780 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/29780/; /private/tmp/npm-review-work/046/identity/chebi29780.json | supports | Current 3-star CHEBI:29780 is isochorismate(2-), charge -2, full key NTGWPRCCOQCMGE-YUMQZZPRSA-L. RDKit independently reproduced the deposited key and charge from the authority SMILES. This confirms the graph node's exact ionic/stereochemical referent, not its detection in the 2002 experiment. |
| P046-CHEBI58764 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/58764/; /private/tmp/npm-review-work/046/identity/chebi58764.json | supports | Current 3-star CHEBI:58764 is (2S,3S)-2,3-dihydroxy-2,3-dihydrobenzoate, charge -1, full key INCSWYKICIYAHB-WDSKDSINSA-M. RDKit independently reproduced the deposited key and charge from the authority SMILES. This confirms the graph node's exact ionic/stereochemical referent, not its detection in the 2002 experiment. |
| P046-CHEBI36654 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/36654/; /private/tmp/npm-review-work/046/identity/chebi36654.json | supports | Current 3-star CHEBI:36654 is 2,3-dihydroxybenzoate, charge -1, full key GLDQAMYCGOIJDV-UHFFFAOYSA-M. RDKit independently reproduced the deposited key and charge from the authority SMILES. This confirms the graph node's exact ionic/stereochemical referent, not its detection in the 2002 experiment. |
| P046-RHEA18985 | https://www.rhea-db.org/rhea?query=rhea%3A18985&amp;columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&amp;format=tsv; /private/tmp/npm-review-work/046/identity/rhea18985.tsv | supports | RHEA:18985 returns chorismate = isochorismate. The complete listed ChEBI participants agree with the current Q8GRA0 catalytic annotation. That annotation uses ECO:0000256/ARBA. Requested citation metadata was not returned by this TSV endpoint. |
| P046-RHEA11112 | https://www.rhea-db.org/rhea?query=rhea%3A11112&amp;columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&amp;format=tsv; /private/tmp/npm-review-work/046/identity/rhea11112.tsv | supports | RHEA:11112 returns isochorismate + H2O = (2S,3S)-2,3-dihydroxy-2,3-dihydrobenzoate + pyruvate. The complete listed ChEBI participants agree with the current Q8GR98 catalytic annotation. That annotation uses ECO:0000256/ARBA. Requested citation metadata was not returned by this TSV endpoint. |
| P046-RHEA23824 | https://www.rhea-db.org/rhea?query=rhea%3A23824&amp;columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&amp;format=tsv; /private/tmp/npm-review-work/046/identity/rhea23824.tsv | supports | RHEA:23824 returns (2S,3S)-2,3-dihydroxy-2,3-dihydrobenzoate + NAD(+) = 2,3-dihydroxybenzoate + NADH + H(+). The complete listed ChEBI participants agree with the current Q8GR97 catalytic annotation. That annotation uses ECO:0000256/ARBA. Requested citation metadata was not returned by this TSV endpoint. |
| P046-AUDIT | /private/tmp/npm-review-work/046/protein-reaction-audit.py; /private/tmp/npm-review-work/046/protein-reaction-audit.json | supports | Actual local sequence/graph check finished with exit code 0: all 35 original pins unchanged; six complete bacterial CDSs translated exactly, including reverse-complement AgbF and its GTG initiation methionine; all six UniProt sequences and EMBL protein IDs matched. Four precursor keys/charges and all three Rhea participant sets matched. Detailed coordinates, sequence hashes and source hashes are retained. |
| P046-MIBIG-SCOPE | https://mibig.secondarymetabolites.org/repository/BGC0002474.2/annotations.json; /private/tmp/npm-review-work/046/identity/mibig.json | supports | The current compact version-2 annotations JSON retains the agrobactin association but contains no individual gene annotation array. It therefore does not independently verify the owner notes that the MIBiG page annotated each Agb protein in September 2026. Current GenBank and UniProt supply the direct six-protein crosswalk; no claim about unchanged historical page content is made. |
| R046-OWNER | data/natural_products/alkaloids/agrobactin.yaml; Entire671-line owner, six proposed steps,11nodes/10edges and allfive native history events | supports | The owner denotes neutral agrobactin with two assigned centres, four LOTUS triples and one MIBiG producer/locus. Six proposed enzyme steps and a deliberately partial graph end in an NRPS assembly process rather than an asserted final-product reaction. No molecular-target or activity claims are present. |
| R046-CHEM | /private/tmp/npm-review-work/046/identity/chemical-comparison.json; Six independently parsed owner/MIBiG/NPAtlas/ChEBI-JSON/MOL/Wikidata-P2017 graphs | supports | All six graphs agree on full key BWPMKVHHFNGYEN-CJAUYULYSA-N, fixed-H form, neutral C32H36N4O10 and the encoded R/S pair. The ChEBI systematic name labels the oxazoline centres4S,5R. This is current database representation agreement; it does not independently establish historical absolute configuration. |
| R046-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/211827/; Retained complete response; stated relevant authority fields | supports | CHEBI211827 is a released two-star exact agrobactin entry, neutral C32H36N4O10 and matching full key, with A. tumefaciens358/1980DOI origin. It is not an eligible three-star replacement for the minted identifier. |
| R046-CHEBI-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/211827/; Complete parsed MOL graph | supports | The actual official MOL independently retains the exact two-centre graph, charge and fixed-H form. |
| R046-NPA | https://www.npatlas.org/api/v1/compound/NPA018820; Retained complete response; stated relevant authority fields | supports | NPA018820 resolves to exact agrobactin, the same1980 crystal-structure reference and A. tumefaciens origin; its nested taxon is genus-level and is not a strain or modern species authentication. No exclusion or reassignment is reported. |
| R046-MIBIG | https://mibig.secondarymetabolites.org/repository/BGC0002474.2/annotations.json; Retained complete response; stated relevant authority fields | supports | Active BGC0002474 version2 reproduces the exact owner graph, NPA018820, taxon358, AB083344.2, native Knock-out studies method and PMID12207035. Quality questionable/completeness unknown remain source metadata. Bounds0/0 do not justify using the full accession as a measured cluster interval. The current JSON has no genes object; deposited proteins are checked directly against GenBank/UniProt, not invented from this response. |
| R046-TAXON | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=358,362&amp;retmode=xml; Both top-level names, ranks, parent links, all synonym/equivalent-name lists and selected B6 type-material context; no independent taxonomic revision | supports | NCBI358 is species Agrobacterium tumefaciens, genomic groupG1; NCBI362 is species Agrobacterium radiobacter, genomic groupG4, with Rhizobium radiobacter explicitly listed as a synonym. They are separate children of the A. tumefaciens complex1183400, not current synonym IDs. The358 type-material list includes B6; this does not establish the historical identity of every strain formerly called A. tumefaciens or bridge MAFF301001 to362. |
| R046-WIKI | https://www.wikidata.org/w/api.php?action=wbgetentities&amp;ids=Q104947509%7CQ131472%7CQ20645236&amp;props=labels%7Cclaims&amp;languages=en&amp;format=json; Three returned entities, labels and chemical identity/taxon claims; complete P685 property inspection | supports | Chemical Q104947509 P2017/P234/P235 preserve exact owner stereochemistry; P233 is stereounspecified and is not used as an exact structure substitute. Q131472 explicitly maps to NCBI358. Q20645236 is labelled Rhizobium radiobacter but has no P685 statement in the returned claims; its mapping uses NCBI362’s explicit synonym, not an invented Wikidata taxon assertion. |
| R046-RAW | data/raw/mibig_compounds.tsv; Complete exact BGC0002474:1 row and complete parsed exact-key inventories | supports | The owner reproduces the source graph, methods, selected citation and blank locus bounds. No exact eligible three-star ChEBI row occurs in the complete pinned inventory. Four LOTUS triples represent two references repeated over two distinct current taxon IDs; they cannot be deduplicated as equivalent taxa without source-specific historical strain evidence. |
| R046-CLASS | data/raw/npclassifier.tsv; Complete exact-key classifier row | supports | The owner reproduces the explicitly versioned NPClassifier2026-09-07 pathway/superclass/class assignments. This computational attribution is distinct from source biosynthetic class and experimentally verified mechanism. |
| R046-IMODULON | https://imodulondb.org/; Previously retained complete28-dataset catalogue | context_only | No matching native organism/strain dataset occurs in the complete retained catalogue. No regulatory module is added from a different organism or from unasserted optional expression context. |

## Limits And Additional Notes

- The full 1979 isolation article and full 1980 crystallographic article were not recovered through the retained bounded routes. The original 1979 abstract and indexed 1980 paragraph were read at their explicitly limited scope.
- No independent original absolute-configuration proof or later synthesis comparison was inspected. This does not establish that the current stereochemical assignment is wrong or that such proof does not exist.
- The 2002 product-specific limitation is a conclusion from the full article, not an inference from missing access. Historical B6 isolation, MAFF301001 total-catechol phenotype and current taxonomic mapping must remain separate.
- No historical AB083344.1 nucleotide sequence or experimental-stock resequencing was fetched. Current CDS identity does not prove identity of the 2002 laboratory stock or an insertion-mutant allele.
- Rhea TSV responses supplied equations and participant IDs, not the requested citation column; these are authority definitions, not recovered primary assays.
- Current unreviewed UniProt functional annotations are predictions. The AgbD enterobactin boilerplate must not be treated as evidence of a different siderophore product or a demonstrated Agb protein complex.
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
review_id: 20261021T111801Z-agrobactin
title: 'Agrobactin: exact-product grades exceed the native catechol assay'
started_at: '2026-10-21T11:06:01.596482Z'
finished_at: '2026-10-21T11:18:01.720159Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The imported native knockout measured total catechol, so its two exact-product
  grades require a guarded downgrade. Six native protein examples, three proposed
  reactions and four precursor groundings agree with current direct authorities. Full
  historical identity and taxon-source evidence remain unavailable or unresolved;
  the four occurrence triples are assessed separately.
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
  - path: data/natural_products/alkaloids/agrobactin.yaml
    sha256: 24358e4e0043aab16bb67a162bc0d95ee540ea57661bed7034ec98d07c8dd39c
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
  selection: Campaign record 46, batch 005, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated pending-PR targets.
    At selection, 94 of 3116 current records had campaign coverage and 3022 remained.
    The population search included ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-bb581c6679
targets:
- target_id: naturalproductmech:mibig-bb581c6679
  path: data/natural_products/alkaloids/agrobactin.yaml
  label: agrobactin
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
    path: data/natural_products/alkaloids/agrobactin.yaml
    role: Curator-owned assertions, inline mechanisms, discussions and audit history
checks:
- check_id: C-STRICT
  name: Closed-schema target validation
  status: passed
  required: true
  summary: The documented target strict validator completed; scientific support is
    assessed separately.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  command: just validate-strict data/natural_products/alkaloids/agrobactin.yaml --out
    /private/tmp/npm-review-work/046/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T11:06:04.750309Z
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
  - naturalproductmech:mibig-bb581c6679
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
  - naturalproductmech:mibig-bb581c6679
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
  - naturalproductmech:mibig-bb581c6679
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
  - naturalproductmech:mibig-bb581c6679
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
  - naturalproductmech:mibig-bb581c6679
- check_id: S046-C-PRIMARY
  name: Original 2002 experiment and product specificity
  status: failed
  required: true
  summary: 'The required exact-product support check fails: the agbB knockout demonstrates
    total catechol and iron-limited growth, not chemically identified agrobactin from
    MAFF301001. This is a scientific finding, not a failed command.'
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - S046-OWNER
  - S046-RAW
  - S046-2002
- check_id: S046-C-HISTORICAL
  name: Original historical isolation and absolute-stereochemical bridge
  status: unavailable
  required: true
  summary: Required full 1979/1980 identity and source-organism review remains incomplete
    after the retained bounded access attempts. The 1979 abstract supports named B6
    isolation and relative trans substitution; the indexed crystal excerpt expressly
    leaves absolute configuration unproved in that study. Current database agreement
    does not replace this missing primary bridge.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - S046-1979
  - S046-1980-EXCERPT
  - S046-HISTORICAL-ACCESS
- check_id: P046-C-SEQUENCES
  name: All six deposited CDS and UniProt examples
  status: passed
  required: true
  summary: Actual local audit exit 0 at 2026-10-21T11:10:53.634894Z. All six native
    reference translations, lengths, stable protein IDs and UniProt complete sequences
    match; all six UniProt entries remain unreviewed.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - P046-GENBANK
  - P046-AUDIT
  - P046-Q83VM5
  - P046-Q8GRA0
  - P046-Q8GR99
  - P046-Q8GR98
  - P046-Q8GR97
  - P046-Q83VM4
  command: .venv/bin/python /private/tmp/npm-review-work/046/protein-reaction-audit.py
  exit_code: 0
  scope_note: Executed in /private/tmp/npm-record-reviews-20261021 from 2026-10-21T11:10:52.613572Z
    to 2026-10-21T11:10:53.634894Z; output /private/tmp/npm-review-work/046/protein-reaction-audit.log;
    current deposited references only.
- check_id: P046-C-REACTIONS
  name: Proposed Rhea reactions and exact precursor groundings
  status: passed
  required: true
  summary: All three current reaction identifiers and four exact charged precursor
    structures agree with the record and current UniProt predictions. The route is
    a substrate/product summary, not a complete stoichiometric graph; omission of
    water, pyruvate and nicotinamide cofactors from the diagram does not turn it into
    an erroneous balanced equation.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - P046-AUDIT
  - P046-RHEA18985
  - P046-RHEA11112
  - P046-RHEA23824
  - P046-CHEBI29748
  - P046-CHEBI29780
  - P046-CHEBI58764
  - P046-CHEBI36654
- check_id: R046-C-CHEM
  name: Exact graph and external identifier resolution
  status: passed
  required: true
  summary: Six independently parsed graphs agree in full standardized and fixed-H
    identity; eligible grounding and source concept are verified within the stated
    inventories.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - R046-CHEM
  - R046-NPA
  - R046-CHEBI
  - R046-RAW
- check_id: R046-C-IMODULON
  name: Applicable native expression dataset
  status: not_applicable
  required: false
  summary: No matching organism/strain dataset appears in the complete retained catalogue.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - R046-IMODULON
evidence:
- evidence_id: S046-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/agrobactin.yaml
  locator: Complete generated owner, all six proposed steps and all 11 nodes / 10
    edges
  accessed_at: '2026-10-21T11:13:27.219295Z'
  support: supports
  summary: The imported exact agrobactin source has BGC_CHARACTERIZED producer and
    CLUSTER_DEMONSTRATED locus grades from Knock-out studies. Its pathway already
    labels the enzyme steps proposed and leaves the terminal route unresolved. Four
    LOTUS occurrence triples use two publications across two taxon identifiers.
  snapshot_sha256: 24358e4e0043aab16bb67a162bc0d95ee540ea57661bed7034ec98d07c8dd39c
- evidence_id: S046-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv; data/raw/lotus_occurrences.tsv
  locator: /private/tmp/npm-review-work/046/local-sources.json
  accessed_at: '2026-10-21T11:13:27.219295Z'
  support: supports
  summary: Exact BGC0002474:1 version 2 row and four LOTUS rows were inspected, including
    all fields. Complete raw MIBiG row SHA256 fbca66b5711f7b1e2120450b8acc1fd545cfe65272f2818a4fb04960a66095dd.
    Each LOTUS selector and complete row hash is retained in protein-reaction-audit.json.
  snapshot_sha256: dffdfb3be0260eacfc6f7ac4059596bf36b182ee4c7ecb0d0bd7ed72b142fda1
- evidence_id: S046-2002
  kind: primary_source
  reference: DOI:10.1266/ggs.77.137
  locator: /private/tmp/npm-review-work/shared-next-batch005/agrobactin/2002-primary.pdf
  accessed_at: '2026-10-21T10:41:42.491154Z'
  support: supports
  summary: Entire original article, printed pp. 137–146, was read. MAFF301001 rif
    and its agbB::Gm mutant MIUB were compared in LB with or without 200 micromolar
    2,2-prime-dipyridyl. The native phenotype is growth and total catechol in the
    Arnow assay with a catechol standard (Methods p. 140; Figs. 5–6 pp. 144–145).
    Four agb genes were assigned functions by homology. The introduction and naming
    discussion attribute earlier agrobactin isolation to B6 and cite Ong 1979; no
    target-resolved chemical identification of the MAFF301001 catechol product is
    reported.
  snapshot_sha256: 400e540de238333ffd6d100f4258bae8b3d98ebfa8a5cee8f113e3a5f3a0f877
- evidence_id: S046-1979
  kind: primary_source
  reference: DOI:10.1016/S0021-9258(17)37736-0
  locator: /private/tmp/npm-review-work/shared-next-batch005/agrobactin/1979-pubmed.xml
  accessed_at: '2026-10-21T10:47:04.792056Z'
  support: supports
  summary: Complete official original abstract read, not the full article. It reports
    isolation of agrobactin from iron-limited A. tumefaciens B6 cultures, a spermidine/threonyl/tricatechol
    scaffold with trans oxazoline substituents and native iron-starvation rescue.
    Acid-opened agrobactin A is a distinct species; its heterologous iron-feeding
    behavior must not be transferred to intact agrobactin. The abstract does not independently
    establish the complete modern absolute-stereochemical graph.
  snapshot_sha256: e148073ab9755de1212a34cf8afa686195487a28fff70e90facd4cbbafa2dd7e
- evidence_id: S046-1980-EXCERPT
  kind: primary_source
  reference: DOI:10.1021/ja00546a014
  locator: /private/tmp/npm-review-work/shared-next-batch005/agrobactin/1980-indexed-stereo-excerpt.json
  accessed_at: '2026-10-21T10:46:56Z'
  support: supports
  summary: Only a search-indexed excerpt of original printed p. 7723 was available.
    The authors describe the trans relative configuration but explicitly do not prove
    absolute configuration in this crystal study; one L configuration is assumed in
    the figures. This is a source-specific limitation, not proof that the current
    assignment is wrong or that later work did not resolve it.
  snapshot_sha256: d4c4951dd87ee7bfa6152bab52b48f6893c24e50667899c517660bc7ccbd0ef4
- evidence_id: S046-HISTORICAL-ACCESS
  kind: search
  reference: DOI:10.1021/ja00546a014; DOI:10.1016/S0021-9258(17)37736-0
  locator: /private/tmp/npm-review-work/shared-next-batch005/agrobactin/source-notes.json
  accessed_at: '2026-10-21T10:48:46.682709Z'
  support: context_only
  summary: The retained primary-source preparation records failed original 1979 full-text
    routes and failed 1980 full-PDF routes. The successful 1979 PubMed abstract and
    indexed 1980 paragraph are explicitly distinguished from full articles. No absence
    of a paper or of later absolute-configuration proof is inferred.
  snapshot_sha256: ce7620f9c7a9d3c93ce19bcee79e968fb64e8af023cc86ce02125dad8bd3284d
  search_scope: Bounded original 1979 JBC PDF, author-upload and publisher API routes;
    1980 original crystallography PDF mirror and indexed primary excerpt. This is
    an access-scope record, not an exhaustive literature search.
- evidence_id: S046-REPAIR-OWNERS
  kind: record_content
  reference: scripts/seed_from_sources.py; src/naturalproductmech/grading.py; conf/producer_evidence.tsv;
    src/naturalproductmech/curate/lotus_exclusions.py; src/naturalproductmech/curate/claim_references.py
  locator: Seeder lines 467–567 and 790–835; complete grading and LOTUS/claim-reference
    consumers
  accessed_at: '2026-10-21T11:13:27.219295Z'
  support: supports
  summary: WITHDRAW requires exact source/version/taxon/accession/bounds/key/original-method
    guards and empty replacement methods; it downgrades both grades while retaining
    producer and locus assertions. LOTUS exclusion instead requires an exact structure/taxon/DOI
    selector and complete raw-row SHA. A normal REPLACE override does not provide
    those WITHDRAW guards. Neither action should be confused with deletion of the
    compound, producer or locus.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: P046-GENBANK
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AB083344.2&rettype=gb&retmode=text
  locator: /private/tmp/npm-review-work/046/identity/genbank.gb
  accessed_at: '2026-10-21T11:07:16.190953Z'
  support: supports
  summary: Current AB083344.2 is a 7,390 bp linear-chromosome MAFF301001 reference,
    with six complete CDSs and a comment that it replaced version 1 on 2003-03-03.
    Coordinates, codon tables, start/stop codons and complete translated sequences
    were inspected; these are deposited references, not assay-stock sequences.
  snapshot_sha256: 2a9f483ede8cfb5b2eebba182113a5e996bf1862159c90b51dccfe227c01efa5
- evidence_id: P046-Q83VM5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q83VM5.json
  locator: /private/tmp/npm-review-work/046/identity/uniprot-Q83VM5.json
  accessed_at: '2026-10-21T11:07:17.472739Z'
  support: supports
  summary: 'Current unreviewed Q83VM5, agbF, 548 aa, maps through EMBL AB083344 to
    BAC57933.1 at complement(104..1750); full sequence independently matches the current
    CDS translation. Protein existence: 4: Predicted. Sequence identity does not establish
    the proposed function or exact experimental stock.'
  snapshot_sha256: d1a05aac546bb8c117d487910d019e7c0b94ed388f31f4bfd03518ecfdd6f1d3
- evidence_id: P046-Q8GRA0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8GRA0.json
  locator: /private/tmp/npm-review-work/046/identity/uniprot-Q8GRA0.json
  accessed_at: '2026-10-21T11:07:18.097651Z'
  support: supports
  summary: 'Current unreviewed Q8GRA0, agbC, 342 aa, maps through EMBL AB083344 to
    BAC16757.2 at 1949..2977; full sequence independently matches the current CDS
    translation. Protein existence: 3: Inferred from homology. Sequence identity does
    not establish the proposed function or exact experimental stock.'
  snapshot_sha256: 5f4f81ee61ed1d68dec5064b29b6990a835aef6709f27db597292fe67dd10abb
- evidence_id: P046-Q8GR99
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8GR99.json
  locator: /private/tmp/npm-review-work/046/identity/uniprot-Q8GR99.json
  accessed_at: '2026-10-21T11:07:17.919569Z'
  support: supports
  summary: 'Current unreviewed Q8GR99, agbE, 541 aa, maps through EMBL AB083344 to
    BAC16758.1 at 3142..4767; full sequence independently matches the current CDS
    translation. Protein existence: 4: Predicted. Sequence identity does not establish
    the proposed function or exact experimental stock.'
  snapshot_sha256: 0a68297e69f01d155608447cec2dea112b240402dd0d9b9a54a79e967067d9d1
- evidence_id: P046-Q8GR98
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8GR98.json
  locator: /private/tmp/npm-review-work/046/identity/uniprot-Q8GR98.json
  accessed_at: '2026-10-21T11:07:17.497143Z'
  support: supports
  summary: 'Current unreviewed Q8GR98, agbB, 289 aa, maps through EMBL AB083344 to
    BAC16759.1 at 4860..5729; full sequence independently matches the current CDS
    translation. Protein existence: 4: Predicted. Sequence identity does not establish
    the proposed function or exact experimental stock.'
  snapshot_sha256: c380620cf048993055d7c89edb653e3bd5188b36e4fe9fe47017ef9bdc74387d
- evidence_id: P046-Q8GR97
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8GR97.json
  locator: /private/tmp/npm-review-work/046/identity/uniprot-Q8GR97.json
  accessed_at: '2026-10-21T11:07:17.472980Z'
  support: supports
  summary: 'Current unreviewed Q8GR97, agbA, 251 aa, maps through EMBL AB083344 to
    BAC16760.1 at 5743..6498; full sequence independently matches the current CDS
    translation. Protein existence: 3: Inferred from homology. Sequence identity does
    not establish the proposed function or exact experimental stock.'
  snapshot_sha256: d21f527830e54586f19cc8946e24acf0858ad28c5ebf70b25350bca4c3e485f1
- evidence_id: P046-Q83VM4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q83VM4.json
  locator: /private/tmp/npm-review-work/046/identity/uniprot-Q83VM4.json
  accessed_at: '2026-10-21T11:07:17.230097Z'
  support: supports
  summary: 'Current unreviewed Q83VM4, agbD, 241 aa, maps through EMBL AB083344 to
    BAC57934.1 at 6529..7254; full sequence independently matches the current CDS
    translation. Protein existence: 3: Inferred from homology. Sequence identity does
    not establish the proposed function or exact experimental stock.'
  snapshot_sha256: f43db40b4b773a411df3e77ee0244a58d8143aa3da7e1d716235381670f2e10b
- evidence_id: P046-CHEBI29748
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/29748/
  locator: /private/tmp/npm-review-work/046/identity/chebi29748.json
  accessed_at: '2026-10-21T11:07:16.548457Z'
  support: supports
  summary: Current 3-star CHEBI:29748 is chorismate(2-), charge -2, full key WTFXTQVDAKGDEY-HTQZYQBOSA-L.
    RDKit independently reproduced the deposited key and charge from the authority
    SMILES. This confirms the graph node's exact ionic/stereochemical referent, not
    its detection in the 2002 experiment.
  snapshot_sha256: ef8fb7231c90d0c74071faf93756f1c7307d310c83d754dec70bfbfd029148a7
- evidence_id: P046-CHEBI29780
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/29780/
  locator: /private/tmp/npm-review-work/046/identity/chebi29780.json
  accessed_at: '2026-10-21T11:07:16.807677Z'
  support: supports
  summary: Current 3-star CHEBI:29780 is isochorismate(2-), charge -2, full key NTGWPRCCOQCMGE-YUMQZZPRSA-L.
    RDKit independently reproduced the deposited key and charge from the authority
    SMILES. This confirms the graph node's exact ionic/stereochemical referent, not
    its detection in the 2002 experiment.
  snapshot_sha256: 37b23e97f02d7513cb779271e48d5897a712f76a4ffa8e3c0a18a7d70f0dca3f
- evidence_id: P046-CHEBI58764
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/58764/
  locator: /private/tmp/npm-review-work/046/identity/chebi58764.json
  accessed_at: '2026-10-21T11:07:16.817932Z'
  support: supports
  summary: Current 3-star CHEBI:58764 is (2S,3S)-2,3-dihydroxy-2,3-dihydrobenzoate,
    charge -1, full key INCSWYKICIYAHB-WDSKDSINSA-M. RDKit independently reproduced
    the deposited key and charge from the authority SMILES. This confirms the graph
    node's exact ionic/stereochemical referent, not its detection in the 2002 experiment.
  snapshot_sha256: d25b6e2761ca7b306771d38b381b31cc8e075000908b706d6708aebe89904c10
- evidence_id: P046-CHEBI36654
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/36654/
  locator: /private/tmp/npm-review-work/046/identity/chebi36654.json
  accessed_at: '2026-10-21T11:07:16.817817Z'
  support: supports
  summary: Current 3-star CHEBI:36654 is 2,3-dihydroxybenzoate, charge -1, full key
    GLDQAMYCGOIJDV-UHFFFAOYSA-M. RDKit independently reproduced the deposited key
    and charge from the authority SMILES. This confirms the graph node's exact ionic/stereochemical
    referent, not its detection in the 2002 experiment.
  snapshot_sha256: 3fa7e0b4764b733986551512f6bdc43275f380df96b8ba14c85ac85d18382f76
- evidence_id: P046-RHEA18985
  kind: authority
  reference: https://www.rhea-db.org/rhea?query=rhea%3A18985&columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&format=tsv
  locator: /private/tmp/npm-review-work/046/identity/rhea18985.tsv
  accessed_at: '2026-10-21T11:07:18.157024Z'
  support: supports
  summary: RHEA:18985 returns chorismate = isochorismate. The complete listed ChEBI
    participants agree with the current Q8GRA0 catalytic annotation. That annotation
    uses ECO:0000256/ARBA. Requested citation metadata was not returned by this TSV
    endpoint.
  snapshot_sha256: 16bf7bb436982173985ea8da787ee8a018914554e47f9c64f5946b3fe9dfa59d
- evidence_id: P046-RHEA11112
  kind: authority
  reference: https://www.rhea-db.org/rhea?query=rhea%3A11112&columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&format=tsv
  locator: /private/tmp/npm-review-work/046/identity/rhea11112.tsv
  accessed_at: '2026-10-21T11:07:18.114498Z'
  support: supports
  summary: RHEA:11112 returns isochorismate + H2O = (2S,3S)-2,3-dihydroxy-2,3-dihydrobenzoate
    + pyruvate. The complete listed ChEBI participants agree with the current Q8GR98
    catalytic annotation. That annotation uses ECO:0000256/ARBA. Requested citation
    metadata was not returned by this TSV endpoint.
  snapshot_sha256: f56e515501fb701e5ca7b1f23188edd903163fa221e21587dc6bc78553f98281
- evidence_id: P046-RHEA23824
  kind: authority
  reference: https://www.rhea-db.org/rhea?query=rhea%3A23824&columns=rhea-id%2Cequation%2Cchebi-id%2Ccitation&format=tsv
  locator: /private/tmp/npm-review-work/046/identity/rhea23824.tsv
  accessed_at: '2026-10-21T11:07:18.321094Z'
  support: supports
  summary: RHEA:23824 returns (2S,3S)-2,3-dihydroxy-2,3-dihydrobenzoate + NAD(+) =
    2,3-dihydroxybenzoate + NADH + H(+). The complete listed ChEBI participants agree
    with the current Q8GR97 catalytic annotation. That annotation uses ECO:0000256/ARBA.
    Requested citation metadata was not returned by this TSV endpoint.
  snapshot_sha256: e2c530ec8c8a681b4524cc98762d2e05735fc7d55f158318a33c401be0f56683
- evidence_id: P046-AUDIT
  kind: validation
  reference: /private/tmp/npm-review-work/046/protein-reaction-audit.py
  locator: /private/tmp/npm-review-work/046/protein-reaction-audit.json
  accessed_at: '2026-10-21T11:10:53.634894Z'
  support: supports
  summary: 'Actual local sequence/graph check finished with exit code 0: all 35 original
    pins unchanged; six complete bacterial CDSs translated exactly, including reverse-complement
    AgbF and its GTG initiation methionine; all six UniProt sequences and EMBL protein
    IDs matched. Four precursor keys/charges and all three Rhea participant sets matched.
    Detailed coordinates, sequence hashes and source hashes are retained.'
  snapshot_sha256: d30fc582504945c7c9860e09c9dcab374a1c77209b4d00d17ebd6c3fbad741f2
- evidence_id: P046-MIBIG-SCOPE
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002474.2/annotations.json
  locator: /private/tmp/npm-review-work/046/identity/mibig.json
  accessed_at: '2026-10-21T11:07:16.045109Z'
  support: supports
  summary: The current compact version-2 annotations JSON retains the agrobactin association
    but contains no individual gene annotation array. It therefore does not independently
    verify the owner notes that the MIBiG page annotated each Agb protein in September
    2026. Current GenBank and UniProt supply the direct six-protein crosswalk; no
    claim about unchanged historical page content is made.
  snapshot_sha256: 5fe9c1b4001ae143c052dd9d613689acaf3c59527164ddbbceab0fe372400e1c
- evidence_id: R046-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/agrobactin.yaml
  locator: Entire671-line owner, six proposed steps,11nodes/10edges and allfive native
    history events
  accessed_at: '2026-10-21T11:12:43.767281Z'
  support: supports
  summary: The owner denotes neutral agrobactin with two assigned centres, four LOTUS
    triples and one MIBiG producer/locus. Six proposed enzyme steps and a deliberately
    partial graph end in an NRPS assembly process rather than an asserted final-product
    reaction. No molecular-target or activity claims are present.
  snapshot_sha256: 24358e4e0043aab16bb67a162bc0d95ee540ea57661bed7034ec98d07c8dd39c
- evidence_id: R046-CHEM
  kind: validation
  reference: /private/tmp/npm-review-work/046/identity/chemical-comparison.json
  locator: Six independently parsed owner/MIBiG/NPAtlas/ChEBI-JSON/MOL/Wikidata-P2017
    graphs
  accessed_at: '2026-10-21T11:11:41.535160Z'
  support: supports
  summary: All six graphs agree on full key BWPMKVHHFNGYEN-CJAUYULYSA-N, fixed-H form,
    neutral C32H36N4O10 and the encoded R/S pair. The ChEBI systematic name labels
    the oxazoline centres4S,5R. This is current database representation agreement;
    it does not independently establish historical absolute configuration.
  snapshot_sha256: b6907a62d9d015959ee111771ba04e06833d0c7d92423dad7ed1dc27416a2a77
- evidence_id: R046-CHEBI
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/211827/
  locator: Retained complete response; stated relevant authority fields
  accessed_at: '2026-10-21T11:10:13.282065Z'
  support: supports
  summary: CHEBI211827 is a released two-star exact agrobactin entry, neutral C32H36N4O10
    and matching full key, with A. tumefaciens358/1980DOI origin. It is not an eligible
    three-star replacement for the minted identifier.
  snapshot_sha256: e8841a609bbed9cda76d73b665b98fc2679daed419ae453d8df0d429e7667bd0
- evidence_id: R046-CHEBI-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/211827/
  locator: Complete parsed MOL graph
  accessed_at: '2026-10-21T11:10:13.280758Z'
  support: supports
  summary: The actual official MOL independently retains the exact two-centre graph,
    charge and fixed-H form.
  snapshot_sha256: e4e99719f242708e766347c2edc3433123483e7eefa8ffbea76a13d4004275fc
- evidence_id: R046-NPA
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA018820
  locator: Retained complete response; stated relevant authority fields
  accessed_at: '2026-10-21T11:07:18.571865Z'
  support: supports
  summary: NPA018820 resolves to exact agrobactin, the same1980 crystal-structure
    reference and A. tumefaciens origin; its nested taxon is genus-level and is not
    a strain or modern species authentication. No exclusion or reassignment is reported.
  snapshot_sha256: ab64f56b146eb160eb0e41cefa134f754769cd2b783c59db7e7e16c88fd66e45
- evidence_id: R046-MIBIG
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002474.2/annotations.json
  locator: Retained complete response; stated relevant authority fields
  accessed_at: '2026-10-21T11:07:16.548298Z'
  support: supports
  summary: Active BGC0002474 version2 reproduces the exact owner graph, NPA018820,
    taxon358, AB083344.2, native Knock-out studies method and PMID12207035. Quality
    questionable/completeness unknown remain source metadata. Bounds0/0 do not justify
    using the full accession as a measured cluster interval. The current JSON has
    no genes object; deposited proteins are checked directly against GenBank/UniProt,
    not invented from this response.
  snapshot_sha256: 5fe9c1b4001ae143c052dd9d613689acaf3c59527164ddbbceab0fe372400e1c
- evidence_id: R046-TAXON
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=358,362&retmode=xml
  locator: Both top-level names, ranks, parent links, all synonym/equivalent-name
    lists and selected B6 type-material context; no independent taxonomic revision
  accessed_at: '2026-10-21T11:07:16.817656Z'
  support: supports
  summary: NCBI358 is species Agrobacterium tumefaciens, genomic groupG1; NCBI362
    is species Agrobacterium radiobacter, genomic groupG4, with Rhizobium radiobacter
    explicitly listed as a synonym. They are separate children of the A. tumefaciens
    complex1183400, not current synonym IDs. The358 type-material list includes B6;
    this does not establish the historical identity of every strain formerly called
    A. tumefaciens or bridge MAFF301001 to362.
  snapshot_sha256: 7dc898412b2bff52dd031f122533d1ffdbd632b8640ac4a45e6fa62c338bc380
- evidence_id: R046-WIKI
  kind: database
  reference: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q104947509%7CQ131472%7CQ20645236&props=labels%7Cclaims&languages=en&format=json
  locator: Three returned entities, labels and chemical identity/taxon claims; complete
    P685 property inspection
  accessed_at: '2026-10-21T11:07:16.807554Z'
  support: supports
  summary: Chemical Q104947509 P2017/P234/P235 preserve exact owner stereochemistry;
    P233 is stereounspecified and is not used as an exact structure substitute. Q131472
    explicitly maps to NCBI358. Q20645236 is labelled Rhizobium radiobacter but has
    no P685 statement in the returned claims; its mapping uses NCBI362’s explicit
    synonym, not an invented Wikidata taxon assertion.
  snapshot_sha256: 48993fa8fd5fde643bc66f5626f6183c2ba65ae42b18fc82dfe67093f5861405
- evidence_id: R046-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: Complete exact BGC0002474:1 row and complete parsed exact-key inventories
  accessed_at: '2026-10-21T11:12:43.767281Z'
  support: supports
  summary: The owner reproduces the source graph, methods, selected citation and blank
    locus bounds. No exact eligible three-star ChEBI row occurs in the complete pinned
    inventory. Four LOTUS triples represent two references repeated over two distinct
    current taxon IDs; they cannot be deduplicated as equivalent taxa without source-specific
    historical strain evidence.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: R046-CLASS
  kind: record_content
  reference: data/raw/npclassifier.tsv
  locator: Complete exact-key classifier row
  accessed_at: '2026-10-21T11:12:43.767281Z'
  support: supports
  summary: The owner reproduces the explicitly versioned NPClassifier2026-09-07 pathway/superclass/class
    assignments. This computational attribution is distinct from source biosynthetic
    class and experimentally verified mechanism.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: R046-IMODULON
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
- assessment_id: S046-A-NATIVE
  area: evidence
  topic: Native origin and exact strain boundary
  outcome: supported
  summary: The original 1979 abstract supports named agrobactin from native B6 low-iron
    cultures. The 2002 MAFF301001 experiment is a separate native strain/locus catechol
    phenotype; its E. coli strains are cloning and conjugation hosts. No heterologous
    agrobactin production or identity of B6 with MAFF301001 is inferred.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - S046-1979
  - S046-2002
- assessment_id: S046-A-PRODUCT
  area: evidence
  topic: Exact agrobactin producer and locus demonstration
  outcome: concern
  summary: The imported Knock-out studies method is real but its measured chemical
    endpoint is too broad for this exact product. BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED
    therefore overstate exact agrobactin support. Preserve the native catechol phenotype
    and the source association separately.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - S046-OWNER
  - S046-RAW
  - S046-2002
  dimensions:
  - name: analytical_specificity
    value: total catechol
    definition: The experiment measures a chemical class, not chromatographically
      or spectroscopically identified agrobactin.
    evidence_ids:
    - S046-2002
  - name: producer_locus_boundary
    value: native MAFF301001 catechol phenotype
    definition: The native knockout supports the locus phenotype without resolving
      the exact molecular product or proving the B6 strain locus.
    evidence_ids:
    - S046-2002
    - S046-1979
- assessment_id: S046-A-GRAPH
  area: graph
  topic: Six proposed steps and the partial 11-node, 10-edge graph
  outcome: supported
  summary: All six pathway steps are explicitly proposed. AgbC/B/A reaction notes
    distinguish UniProt prediction from direct assays, the graph retains prediction
    language, and it has no terminal agrobactin product edge. The 2002 paper supports
    cloned genes, homology hypotheses and the native agbB phenotype, not six purified-enzyme
    experiments. Those already-qualified hypotheses are not counted as additional
    confirmed errors.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - S046-OWNER
  - S046-2002
- assessment_id: S046-A-LOTUS-2002-358
  area: evidence
  topic: 2002 LOTUS occurrence at taxon 358
  outcome: supported
  summary: The 2002 introduction explicitly reports the earlier B6 agrobactin isolation
    and cites Ong 1979, so it supplies secondary/background support at the historical
    A. tumefaciens label. It is not a new MAFF301001 isolation, an independent replicate
    or an exact-stereochemical determination. A blanket claim that this citation contains
    no agrobactin occurrence support would be inaccurate. The original 1979 abstract
    supplies the direct native-isolation lead.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - S046-RAW
  - S046-2002
  - S046-1979
- assessment_id: S046-A-LOTUS-2002-362
  area: evidence
  topic: 2002 LOTUS occurrence at taxon 362
  outcome: unknown
  summary: The full paper concerns historical A. tumefaciens B6 background and MAFF301001
    experimental material; it does not supply a separately traced taxon 362 stock
    or exact-product isolate. Retain uncertainty about the LOTUS taxonomic attribution
    pending the authority and strain bridge; do not silently equate identifiers 358
    and 362 or infer universal absence.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - S046-RAW
  - S046-2002
  - S046-1979
- assessment_id: S046-A-LOTUS-1980
  area: evidence
  topic: Both 1980 LOTUS occurrence triples and absolute identity
  outcome: unknown
  summary: The original crystallography article was not available in full. Its indexed
    paragraph establishes a trans relative assignment and a study-specific absolute-configuration
    limit, but does not settle the complete source-organism, stock or modern taxon
    mapping for either LOTUS triple. Lack of access alone does not justify excluding
    either occurrence.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - S046-RAW
  - S046-1980-EXCERPT
  - S046-HISTORICAL-ACCESS
- assessment_id: S046-A-COMPLETENESS
  area: completeness
  topic: Biological-function evidence and unresolved terminal biosynthesis
  outcome: supported
  summary: The owner explicitly leaves terminal agrobactin assembly unresolved. The
    historical original abstract also provides native iron-acquisition function, but
    does not justify a molecular target or unqualified cross-species assay claim.
    Optional quantitative bioactivity and a fully resolved biosynthetic route are
    not required additions without claim-specific primary detail.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - S046-OWNER
  - S046-1979
  - S046-2002
- assessment_id: P046-A-PROTEINS
  area: grounding
  topic: Native reference proteins and gene identity
  outcome: supported
  summary: AgbC Q8GRA0/BAC16757.2 (342 aa), AgbB Q8GR98/BAC16759.1 (289 aa), AgbA
    Q8GR97/BAC16760.1 (251 aa), AgbD Q83VM4/BAC57934.1 (241 aa), AgbE Q8GR99/BAC16758.1
    (541 aa) and AgbF Q83VM5/BAC57933.1 (548 aa) are exact current AB083344.2 sequence
    matches. None is promoted to a reviewed, purified or stock-specific protein.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - P046-AUDIT
  - P046-GENBANK
- assessment_id: P046-A-PREDICTION
  area: evidence
  topic: Protein function and reaction support
  outcome: supported
  summary: AgbC/B/A Rhea reactions are ARBA predictions. AgbD has automatic EntD-family/enterobactin
    annotations; only the phosphopantetheinyl-transferase candidate role is transferred,
    not proof of enterobactin production, an Agb complex or exact agrobactin assembly.
    AgbE and AgbF carry probable submitted functions. The owner already preserves
    these distinctions.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - P046-Q8GRA0
  - P046-Q8GR98
  - P046-Q8GR97
  - P046-Q83VM4
  - P046-Q8GR99
  - P046-Q83VM5
- assessment_id: P046-A-CHEM
  area: grounding
  topic: Four charged precursor nodes and three reaction references
  outcome: supported
  summary: The two dianions and two monoanions match current 3-star structures, including
    (2S,3S)-dihydroxy-dihydrobenzoate. The full Rhea equations include the expected
    small participants and NAD pair. Exact reaction grounding does not supply an experimental
    enzyme assay.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - P046-AUDIT
  - P046-RHEA18985
  - P046-RHEA11112
  - P046-RHEA23824
- assessment_id: P046-A-VERSION
  area: provenance
  topic: 2002 sequence report versus current version 2
  outcome: supported
  summary: The 2002 paper describes four ORFs and reports agbC as 1,176 bp. Current
    AB083344.2 has six complete CDSs and a 1,029 bp agbC (342 aa); it replaced version
    1 in March 2003. The owner correctly specifies current version-2 sequences and
    cites direct databases for AgbD/F. Do not infer that the historical paper assayed
    these six exact current sequences, or that its 1,176 bp AgbC was the current 342
    aa reference.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - P046-GENBANK
  - P046-AUDIT
- assessment_id: P046-A-MIBIG-HISTORY
  area: provenance
  topic: Historical gene-annotation locator
  outcome: unknown
  summary: The retrieved current MIBiG annotations JSON does not reproduce the historical
    gene-annotation statements in the owner. The historical September page was not
    archived in this packet, so no confirmed contradiction with that earlier snapshot
    is asserted. All six sequence crosswalks are independently supported by the current
    direct sequence authorities.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - P046-MIBIG-SCOPE
  - P046-GENBANK
  - P046-AUDIT
- assessment_id: R046-IDENTITY
  area: identity
  topic: Current graph and exact external xrefs
  outcome: supported
  summary: Six current representations agree on complete identity and fixed-H form.
    NPA018820 resolves exactly, while the unavailable original absolute-configuration
    derivation remains a separate scientific limit.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - R046-CHEM
  - R046-CHEBI
  - R046-CHEBI-MOL
  - R046-NPA
  - R046-WIKI
- assessment_id: R046-GROUNDING
  area: provenance
  topic: Minted identity and active source concept
  outcome: supported
  summary: Current exact ChEBI211827 has two stars and no eligible exact row is present
    in the complete pinned three-star inventory. MIBiG version2 resolves; its correct
    source provenance does not establish the overclaimed exact-product phenotype.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - R046-RAW
  - R046-CHEBI
  - R046-MIBIG
- assessment_id: R046-TAXON
  area: scope
  topic: Historical organism names versus distinct current species
  outcome: unknown
  summary: Both taxon IDs resolve, and the historical Rhizobium label is a recognized
    synonym for362. However358 and362 are separate current species, so two names do
    not establish duplicate observations or the same experimental stock. The primary
    historical strain-to-modern-species applicability remains qualified where not
    directly established.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - R046-TAXON
  - R046-WIKI
  - R046-RAW
- assessment_id: R046-HISTORY
  area: provenance
  topic: Existing proposed mechanism and audit trail
  outcome: supported
  summary: All five native history events remain intact, including the prior correction
    that removed an unsupported terminal product edge and retained proposed reaction
    scope. Current SEEDED status is unchanged. These resolved details are not repeated
    as new findings.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - R046-OWNER
- assessment_id: R046-CLASS
  area: provenance
  topic: Computational classification attribution
  outcome: supported
  summary: Classification is retained as a versioned computational output, not a newly
    demonstrated biosynthetic reaction.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  evidence_ids:
  - R046-CLASS
  - R046-OWNER
findings:
- finding_id: S046-F-EXACT-PRODUCT-GRADE
  issue_key: agrobactin-bgc0002474-catechol-knockout-not-exact-product
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The native knockout endpoint does not establish exact agrobactin production
  description: Sonoda 2002 demonstrates that the MAFF301001 agb region is necessary
    for iron-limited growth and catechol output, measured by a colorimetric total-catechol
    assay. Agrobactin from B6 is cited as historical background and gives the genes
    their name; the study does not identify the MAFF301001 product as that exact molecular
    structure. Importing Knock-out studies into BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED
    on this compound therefore exceeds the product specificity of the experiment.
    This does not refute agrobactin production by B6, the observed catechol phenotype,
    the deposited locus, or the explicitly proposed pathway.
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  field_paths:
  - producer_organisms[0].evidence_basis
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - biosynthetic_gene_clusters[0].link_evidence_basis
  evidence_ids:
  - S046-OWNER
  - S046-RAW
  - S046-2002
  - S046-1979
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Consumed maintained table for a narrowly pinned WITHDRAW of exact-product
      experiment grades
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Guarded override consumer and normal regeneration
  - repository: CultureBotAI/NaturalProductMech
    path: conf/producer_evidence.tsv
    role: Existing two-claim grading vocabulary; no global mapping change needed
  rule_id: 'review-checklist: exact-product evidence and producer versus locus scope'
  native_severity: 'major: broad analytical endpoint promoted to exact-product causal
    grades'
  normalization_reason: One analytical-specificity error affects the two imported
    grades; it is reported once, without re-reporting already qualified proposed pathway
    reactions.
actions:
- action_id: S046-ACTION-WITHDRAW
  finding_ids:
  - S046-F-EXACT-PRODUCT-GRADE
  target_ids:
  - naturalproductmech:mibig-bb581c6679
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Consumed maintained table for a narrowly pinned WITHDRAW of exact-product
      experiment grades
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Guarded override consumer and normal regeneration
  - repository: CultureBotAI/NaturalProductMech
    path: conf/producer_evidence.tsv
    role: Existing two-claim grading vocabulary; no global mapping change needed
  description: Add a consumed WITHDRAW decision for naturalproductmech:mibig-bb581c6679,
    source MIBIG, source_id BGC0002474 (compound selector BGC0002474:1), expected_entry_version
    2, expected_taxon_id NCBITaxon:358, expected_genome_accession AB083344.2, expected_locus_from
    and expected_locus_to both explicitly empty, expected_standard_inchi_key BWPMKVHHFNGYEN-CJAUYULYSA-N,
    and expected_locus_evidence_methods Knock-out studies. Set replacement locus_evidence_methods
    empty and attribute the decision to DOI:10.1266/ggs.77.137 with curator, actual
    decision date and the Arnow endpoint rationale. The complete raw-row audit digest
    is fbca66b5711f7b1e2120450b8acc1fd545cfe65272f2818a4fb04960a66095dd; the current
    WITHDRAW consumer enforces the named context fields, not an arbitrary expected_source_row_sha256
    column. Preserve the untouched raw inventory and regenerate normally. This downgrades
    the imported producer to SOURCE_ASSERTION and locus to CLUSTER_UNSTATED while
    retaining both rows and emitting the experimental qualification. Retain B6 native
    isolation, the MAFF301001 catechol phenotype and all explicitly proposed protein/reaction
    hypotheses with their separate scopes. Do not repair this by replacing the method
    with an unsupported stronger experiment, deleting the locus, attaching B6 as the
    MAFF301001 strain, or editing the generated owner directly.
  generator: scripts/seed_from_sources.py consuming curation/mibig_locus_evidence_overrides.tsv
    through load_mibig_locus_evidence_overrides and apply_mibig_locus_evidence_override
  acceptance_checks:
  - Reject a changed version, taxon, accession, bound, full key or original method,
    and reject zero or multiple matching source rows. Both empty bounds must be supplied
    explicitly. Recompute the complete raw-row digest during implementation and re-review
    any additional-field drift rather than pretending the current override validates
    all fields.
  - The regenerated exact-product imported grades are SOURCE_ASSERTION and CLUSTER_UNSTATED;
    producer and BGC associations remain, raw Knock-out studies remains available
    in provenance and the qualification explains the total-catechol endpoint.
  - Keep the separate native B6 isolation and the MAFF301001 experiment distinct.
    Preserve all six proposed steps and the partial graph unless a new, separately
    supported reaction finding requires change; never recreate a demonstrated terminal
    agrobactin edge.
  - 'Assess each LOTUS row separately: the 2002 taxon-358 triple has historical B6
    background support, while its taxon-362 bridge and the full 1980 source mapping
    remain unresolved. Do not automatically withdraw all four triples or treat two
    species identifiers as synonyms. Any later justified exclusion must use its exact
    key/taxon/DOI and full row hash retained in the audit.'
  - Add attribution and the required curation event through the documented authorized
    workflow, then run strict target validation, provenance, corpus integrity, byte
    reproduction and required QC. Do not promote scientific status while historical
    primary identity or taxon-source questions remain unresolved.
limitations:
- The full 1979 isolation article and full 1980 crystallographic article were not
  recovered through the retained bounded routes. The original 1979 abstract and indexed
  1980 paragraph were read at their explicitly limited scope.
- No independent original absolute-configuration proof or later synthesis comparison
  was inspected. This does not establish that the current stereochemical assignment
  is wrong or that such proof does not exist.
- The 2002 product-specific limitation is a conclusion from the full article, not
  an inference from missing access. Historical B6 isolation, MAFF301001 total-catechol
  phenotype and current taxonomic mapping must remain separate.
- No historical AB083344.1 nucleotide sequence or experimental-stock resequencing
  was fetched. Current CDS identity does not prove identity of the 2002 laboratory
  stock or an insertion-mutant allele.
- Rhea TSV responses supplied equations and participant IDs, not the requested citation
  column; these are authority definitions, not recovered primary assays.
- Current unreviewed UniProt functional annotations are predictions. The AgbD enterobactin
  boilerplate must not be treated as evidence of a different siderophore product or
  a demonstrated Agb protein complex.
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
