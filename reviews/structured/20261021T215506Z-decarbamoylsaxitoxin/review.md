# Decarbamoylsaxitoxin: occurrence citations and identification scope

- Review: 20261021T215506Z-decarbamoylsaxitoxin
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T21:49:34.902039Z
- Finished UTC: 2026-10-21T21:55:06.976731Z
- Reviewer: Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The chemical identity and the native T3 culture evidence are supported, while four genus-specific occurrence assertions cite a 1983 study of a different sampled organism. Bee brain annotations and acid-extraction products need explicit identification and origin qualifications. Several remaining occurrence sources could only be inspected as abstracts, so the review remains partial. The alternative guanidine representations are tautomers with matching Standard InChI, not an enantiomer conflict.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 173, batch 018, selected in path order from the fresh-main authoritative validated catalogue and the separately validated targets in earlier batch commits (publication tracked separately). At selection, 224 of 3116 current records had campaign coverage and 2892 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:133919 | data/natural_products/alkaloids/decarbamoylsaxitoxin.yaml | generated | decarbamoylsaxitoxin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | CHEBI:133919 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | CHEBI:133919 | All 3116 corpus records are filed exactly where PATHS.tsv pins them. |
| Corpus reproduction | passed | True | CHEBI:133919 | All 3116 records reproduce byte-for-byte from data/raw/. |
| Native deterministic review queue | passed | True | CHEBI:133919 | The canonical review-queue command completed with actual exit0 on the fresh main base; exact output, warnings and skips remain in the pinned transcript. |
| Configured ontology identifier-label correspondence | passed | True | CHEBI:133919 | Configured identifier-label validation exited zero: 13449 canonical matches, 646 synonym matches and 35 configured exceptions; 499 non-blocking warnings and 4750 no-adapter skips remain. |
| Full repository quality gate on the fresh main baseline | passed | True | CHEBI:133919 | Full fresh-base quality command completed successfully:999 tests passed,4 skipped,2 warnings;3116 records passed closed schema validation and corpus reproduction, and generated pages were current. |
| Complete owner and captured-source scope | passed | True | CHEBI:133919 | Successful official intake and a fresh root full-owner/read receipt precede this authoring. All six officially captured sets and the separately mechanically parsed seventh PubChem set match. All matching raw rows and 12 written diazaquinomycin A observations were read by root; primary assay interpretation remains separately scoped. No BindingDB or graph assertion is present. The external component set is empty. |
| Exact taxon applicability of the four 1983 LOTUS triples | failed | True | CHEBI:133919 | The complete three-page 1983 study isolates PBT=dcSTX from Spondylus butleri associated with a Pyrodinium bloom. It does not report Anabaena, Aphanizomenon, Lyngbya or Cylindrospermopsis as the sampled or detected organisms. |
| Required source-specific occurrence and congener checks | unavailable | True | CHEBI:133919 | The 2001 body and several cited occurrence studies remain abstract-only after bounded public routes. Standards, derivative signals, human metabolites, extraction products and exact source-organism results cannot all be resolved from those abstracts. Known positive cultures and deposited putative bee annotations are retained explicitly. |
| Stored chemical representation and complete source row | passed | True | CHEBI:133919 | Fresh intake derivation agrees with the stored graph; the source selector, full row and prepared snapshot were independently rechecked. |
| Literal identifier resolution and parsed representation | passed | True | CHEBI:133919 | Every present literal was resolved; differing Standard/fixed-H, charge or precision is assessed separately. For invalid default ChEBI JSON SMILES, the independently fetched official MOL supplies the parsed comparison. |
| Exact Standard identity and tautomer boundary | passed | True | CHEBI:133919 | Unique 3-star CHEBI133919 and literal PubChem24941628 match the full Standard identity. The definition describes the CheBI diimino tautomer; the retained depiction uses the amino/endo-imino form. This is not constitutional or stereochemical disagreement. |

## Scientific And Domain Assessments

### Native status and complete audit history

provenance: supported. Targets: CHEBI:133919.

All 2 retained events are SEEDED_FROM_SOURCES. Native status remains SEEDED; provenance events are not structured-review passes.

### Complete optional-assertion inventory

completeness: supported. Targets: CHEBI:133919.

This owner has one imported ChEBI definition; its constitutional and biological clauses are present assertions requiring separate chemistry/science support. The no-assay-data raw row is not a measured assay, and no pathway, graph, molecular target, application, activity summary, relation, discussion or clinical-status assertion is present.

### Exact-key computed classification provenance

representation: supported. Targets: CHEBI:133919.

The exact-key NPClassifier projection and version npclassifier.gnps2.org@2026-09-07 reproduce the owner filing, superclass/class labels and glycoside value false. Computed labels are not independent precursor, mechanism or natural-origin evidence. Any accepted new identity requires reclassification for its effective key.

### Literal organism identifier routing

grounding: supported. Targets: CHEBI:133919.

All literal organism-QID routes agree at the inspected P225/P685 scope. Occurrence and experimental-unit support remain separate.

### Taxonomic names versus experimental stocks

provenance: supported. Targets: CHEBI:133919.

NCBI 398006 is Cylindrospermopsis raciborskii T3 at strain rank under 77022. The species response includes Raphidiopsis raciborskii as a synonym while retaining Cylindrospermopsis as its primary name. NCBI 467598 Microseira wollei includes Lyngbya wollei; 373637 Aulacomya atra lists Aulacomya ater as a misspelling. The four cyanobacterial genera, algal species, mollusks, fish and bee identities verify only routing; their exact compound/source resolution remains separately assessed.

### Producer transcriptomic applicability

completeness: not_applicable. Targets: CHEBI:133919.

No exact native producer species/strain dataset is represented in the inspected catalogue. Related species and possible experimental hosts do not establish a construct/condition match; no gene/module or compound-production inference is made.

### biosynthesis_origin and producer_organisms[0]

evidence: supported. Targets: CHEBI:133919.

The full 2008 primary explicitly reports dcSTX in C. raciborskii T3 along with other paralytic shellfish toxins. DQ787200.1 independently identifies T3. This is a positive culture-level source assertion; the early-intermediate MS experiment is not a direct final-dcSTX enzymatic trace.

### biosynthetic_gene_clusters[0] and bgc_class

provenance: supported. Targets: CHEBI:133919.

The original 2008 work links the sxt region through genomic annotation and measured early intermediates, without a transformation system, exact dcSTX knockout or purified final-product reconstitution. Its final paragraph reports constitutive sxt RT-PCR expression with data not shown; transcriptional regulation remained under study, so this is not expression-linked dcSTX production. SxtL-mediated decarbamoylation and a route bypassing SxtI are alternatives, not resolved enzyme claims. DQ787200.1 is 37,606 bp, but empty imported locus bounds are not silently replaced by the whole submission. OTHER is source class context.

### definition and definition_source

representation: supported. Targets: CHEBI:133919.

The imported broad toxin, marine-dinoflagellate/cyanobacterial and paralytic-shellfish-poisoning context is compatible with the inspected 1983, 2008 and 2010 primary studies. The definition does not establish all emitted organism triples, direct biosynthesis by seafood consumers or one uniquely resolved dcSTX enzyme route. Exact structural nomenclature is separately assessed by chemistry.

### occurrences[0] Anabaena

evidence: unknown. Targets: CHEBI:133919.

Original2001abstract reports Anabaena circinalis extracts and radioreceptor-versus-HPLC comparisons, with general introductory mention of Anabaena/Aphanizomenon. Exact dcSTX/congener-by-strain table and applicability to this particular genus remain uninspected because full body was unavailable.

### occurrences[1] Anabaena

evidence: concern. Targets: CHEBI:133919.

Complete1983primary isolates PBT=dcSTX from Spondylus butleri in a Pyrodinium-associated outbreak. None of the four cited cyanobacterial genera is its reported sample or detected organism; this particular taxon-reference triple is not supported by the inspected full study.

### occurrences[2] Aphanizomenon

evidence: unknown. Targets: CHEBI:133919.

Original2001abstract reports Anabaena circinalis extracts and radioreceptor-versus-HPLC comparisons, with general introductory mention of Anabaena/Aphanizomenon. Exact dcSTX/congener-by-strain table and applicability to this particular genus remain uninspected because full body was unavailable.

### occurrences[3] Aphanizomenon

evidence: concern. Targets: CHEBI:133919.

Complete1983primary isolates PBT=dcSTX from Spondylus butleri in a Pyrodinium-associated outbreak. None of the four cited cyanobacterial genera is its reported sample or detected organism; this particular taxon-reference triple is not supported by the inspected full study.

### occurrences[4] Pao turgidus

evidence: supported. Targets: CHEBI:133919.

Originalabstract positively reports wild Tetraodon turgidus STX/dcSTX and separate experimentally injected cultured-fish accumulation. It explicitly argues exogenous origin; occurrence is not autonomous fish biosynthesis.

### occurrences[5] Lyngbya

evidence: unknown. Targets: CHEBI:133919.

Original2001abstract reports Anabaena circinalis extracts and radioreceptor-versus-HPLC comparisons, with general introductory mention of Anabaena/Aphanizomenon. Exact dcSTX/congener-by-strain table and applicability to this particular genus remain uninspected because full body was unavailable.

### occurrences[6] Lyngbya

evidence: concern. Targets: CHEBI:133919.

Complete1983primary isolates PBT=dcSTX from Spondylus butleri in a Pyrodinium-associated outbreak. None of the four cited cyanobacterial genera is its reported sample or detected organism; this particular taxon-reference triple is not supported by the inspected full study.

### occurrences[7] Alexandrium tamarense

evidence: unknown. Targets: CHEBI:133919.

Originalabstract distinguishes seven analytical toxins including dcSTX from the tested algae: HK9301 has GTX2/GTX3, CI01 no detected PST. It does not establish exact dcSTX in either tested extract. Full body remains unavailable, so do not claim an exhaustive study-wide absence beyond this explicit abstract result.

### occurrences[8] Aulacomya ater

evidence: unknown. Targets: CHEBI:133919.

Originalabstract detects dcSTX as a human liver/kidney/lung metabolic product after an Aulacomya meal. Whether the consumed mussel itself contained dcSTX needs the uninspected source table. Public institutional PDF lead returned a challenge page, not the paper.

### occurrences[9] Acanthocardia tuberculata

evidence: unknown. Targets: CHEBI:133919.

Originalabstract concerns PST quantification in mussels/cockles and an interfering peak near dcSTX. It does not establish an exact dcSTX-positive Acanthocardia sample; detailed source table remains unavailable.

### occurrences[10] Gymnodinium catenatum

evidence: unknown. Targets: CHEBI:133919.

Originalabstract isolates GC1/2/3; GC3 is a4-hydroxybenzoate ester derivative of dcSTX. Ester identification does not by itself prove free dcSTX occurrence. Full experimental body remains unavailable.

### occurrences[11] Microseira wollei

evidence: concern. Targets: CHEBI:133919.

Originalabstract explicitly shows hydrochloric-acid extraction converts L.wollei toxins into dcSTX/dcGTX2/3, whereas0.1M acetic acid preserves the original profile. Preserve extraction-product scope, not an unsupported claim that every native mat contains free dcSTX.

### occurrences[12] Aphanizomenon gracile

evidence: supported. Targets: CHEBI:133919.

Full2010primary confirms exact dcSTX by LC-MS against standards in all14 A.gracile strains; it constitutes0.7–14.3% of quantified PSP toxin profile, with strain-specific proportions. Toxin-gene presence in additional nontoxic strains is separately described.

### occurrences[13] Apis cerana

evidence: concern. Targets: CHEBI:133919.

Official current MAF has three exact dcSTX-labelled feature rows1379/1658/5760, allMSI:2, with nonzero values in20brain samples. Two structure representations omit stereo; the third has exact isomeric InChI. These support an explicit putative annotation, not authentic-standard identification or bee biosynthesis.

### occurrences[14] Cylindrospermopsis

evidence: unknown. Targets: CHEBI:133919.

Original2001abstract reports Anabaena circinalis extracts and radioreceptor-versus-HPLC comparisons, with general introductory mention of Anabaena/Aphanizomenon. Exact dcSTX/congener-by-strain table and applicability to this particular genus remain uninspected because full body was unavailable.

### occurrences[15] Cylindrospermopsis

evidence: concern. Targets: CHEBI:133919.

Complete1983primary isolates PBT=dcSTX from Spondylus butleri in a Pyrodinium-associated outbreak. None of the four cited cyanobacterial genera is its reported sample or detected organism; this particular taxon-reference triple is not supported by the inspected full study.

### occurrences[16] Cylindrospermopsis raciborskii

evidence: supported. Targets: CHEBI:133919.

Originalabstract explicitly reports dcSTX by LC-fluorescence in the Brazilian C.raciborskii strain. French/Australian and other strain phenotypes are separate; full strain designation/experimental conditions are not inspected.

### Absent pathways, graph and bioactivity observations

evidence: not_applicable. Targets: CHEBI:133919.

No mechanism or assay is emitted, and the sole matching PubChem inventory row says no assay data. Proposed sxt chemistry and physiological toxin effects do not create an obligation to add an unverified exact-enzyme mechanism.

### Stored representation and source-concept provenance

identity: supported. Targets: CHEBI:133919.

The complete source row BGC0000188:3 and source-concept hash reproduce this stored representation; this does not establish that the upstream compound label is correct. Formula, charge, Standard and fixed-H distinctions are independently recorded. Primary support and any conflicting exact xref are assessed separately.

### Exact authority eligibility and source representation

provenance: supported. Targets: CHEBI:133919.

Exactly one committed three-star default ChEBI row matches; its current graph is checked separately.

### Literal identifiers, namespaces and exact microstates

representation: supported. Targets: CHEBI:133919.

Stored literals were requested exactly and compared in their returned namespaces: [{"formula": "C9H16N6O3", "literal": "pubchem:24941628", "returned_key": "VRRIYZJUSNMZMP-PJPYAQQDSA-N", "same_fixed_h": true, "same_standard": true}]. Standard equality does not imply literal fixed-H equality. Current authority agreement is not independent primary proof. Canonical Wikidata P233 is not an assertion of the isomeric hand.

### Exact three-star projection and source concept

grounding: supported. Targets: CHEBI:133919.

CHEBI:133919 is the unique committed eligible three-star Standard-key match; its tautomeric fixed-H distinction is retained.

### Unemitted raw ChemSpider assertion

provenance: supported. Targets: CHEBI:133919.

The exact raw ChemSpider mismatch is retained for source audit, without inventing an owner xref or proposing removal of an already excluded namespace.

### Primary chemical support and retained precision

scope: supported. Targets: CHEBI:133919.

The original 1983 three-page paper identifies paralytic shellfish toxin from Spondylus butleri by NMR, chromatography/electrophoresis comparison to decarbamoylsaxitoxin prepared from saxitoxin, and carbamoylation back to saxitoxin. The source provides a chemical identity bridge, not evidence for every later organism occurrence. The present comparison does not independently redetermine all absolute stereocentres. The retained amino/endo-imino form and ChEBI diimino form have identical full Standard InChI, formula, charge and stereochemistry, with a positive guanidine proton/bond-placement tautomer relationship but different fixed-H InChI. Do not call this constitutional or enantiomeric disagreement. The legacy-CIP diagnostic error is corrected explicitly in v3.

## Findings

### S173-F-LOTUS1983: Four organism occurrences cite an original study of a different sample

major / open / confirmed; issue key: lotus-dcstx-1983-four-cyanobacterial-misattributions.

The inspected 1983 study characterizes dcSTX in Spondylus butleri from a Pyrodinium-associated outbreak, whereas four emitted LOTUS triples attach that paper to cyanobacterial genera absent from the study. This is a source-specific citation error, not evidence that those genera can never contain dcSTX.

### S173-F-CONTEXT: Two occurrence assertions omit decisive analytical context

minor / open / confirmed; issue key: chebi-133919-source-specific-detection-context.

MTBLS379 reports putatively annotated MSI:2 bee-brain features, while PMID22960450 explicitly reports dcSTX formation during hydrochloric-acid extraction of Lyngbya/Microseira material. The current generic database occurrence wording preserves positive source associations but hides these limitations; neither source should be promoted to authentic-standard native free-toxin proof.

## Recommended Actions And Acceptance Checks

### S173-ACT-LOTUS1983

Use the existing curation/lotus_occurrence_exclusions.tsv contract for exactly these four unique triples: complete raw row {"organism_name": "Anabaena", "organism_wikidata": "http://www.wikidata.org/entity/Q133353", "reference_doi": "10.1080/00021369.1983.10865612", "standard_inchi_key": "VRRIYZJUSNMZMP-PJPYAQQDSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27277104", "taxon_id": "NCBITaxon:1163"}; expected_source_row_sha256=ca1511af57f882aa25f14fe389e8166df034f86b673980dac2688f2cda13a3c5 &#124; complete raw row {"organism_name": "Aphanizomenon", "organism_wikidata": "http://www.wikidata.org/entity/Q309515", "reference_doi": "10.1080/00021369.1983.10865612", "standard_inchi_key": "VRRIYZJUSNMZMP-PJPYAQQDSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27277104", "taxon_id": "NCBITaxon:1175"}; expected_source_row_sha256=d524cf16947a87716e598b74d04afb02ca78d35bb9f9c197ca4e195a9f4a3686 &#124; complete raw row {"organism_name": "Lyngbya", "organism_wikidata": "http://www.wikidata.org/entity/Q310362", "reference_doi": "10.1080/00021369.1983.10865612", "standard_inchi_key": "VRRIYZJUSNMZMP-PJPYAQQDSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27277104", "taxon_id": "NCBITaxon:28073"}; expected_source_row_sha256=4011e192dec93f155d04d1622d5e83e9f7e8d600ff35ad8e395951e14d2e8904 &#124; complete raw row {"organism_name": "Cylindrospermopsis", "organism_wikidata": "http://www.wikidata.org/entity/Q5199328", "reference_doi": "10.1080/00021369.1983.10865612", "standard_inchi_key": "VRRIYZJUSNMZMP-PJPYAQQDSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27277104", "taxon_id": "NCBITaxon:77021"}; expected_source_row_sha256=355d90374204f4af5c8196fc602f9a98cf08b36ab9d024905d82842531914ccd. Set reference=DOI:10.1080/00021369.1983.10865612 with curator/date and the sample-specific rationale. The consumer keeps raw inventories unchanged and emits exclusion provenance. Do not alter the four separate 2001 triples or other ChEBI occurrences, and do not automatically replace the taxa with Spondylus/Pyrodinium without independently keyed source rows and structural adjudication.

- Exactly four literal key/taxon/DOI selectors and complete row hashes match uniquely; any source drift or duplicate fails.
- All other occurrence references and the positive T3 producer/locus remain unchanged.
- Regenerated occurrence list omits only the unsupported triples and retains the consumed exclusion discussion; normal strict/reference/history checks pass.

### S173-ACT-CONTEXT

Implement a tested typed origin-context consumer, keyed to each complete ChEBI origin row with SHA256, because the inspected seeder has no consumed exact-row origin qualification table. Guard complete raw row {"chebi_id": "CHEBI:133919", "comments": "", "component_text": "", "source_accession": "MTBLS379", "species_accession": "7461", "species_text": "Apis cerana", "strain_text": ""}; expected_source_row_sha256=a88667777bb5dfce1ce7482c567a6cd29ccab03fb0c4b66a99a09b7c477bf8a4 &#124; complete raw row {"chebi_id": "CHEBI:133919", "comments": "", "component_text": "", "source_accession": "22960450", "species_accession": "467598", "species_text": "Microseira wollei", "strain_text": ""}; expected_source_row_sha256=2d30a2b950246d1b074b0044186d1f77ca6a6283ecb171510bed744437367e5c. Preserve the occurrence source assertion, original reference and raw bytes. Add MSI:2 putative brain-feature annotation for MTBLS379, and source-reported hydrochloric-acid conversion for PMID22960450, with explicit reference and curator attribution. Do not infer a concentration, an adduct, bee biosynthesis, universal natural absence, or automatic taxon replacement. The latter study body remains a required gap; its directly stated abstract conversion is the bounded qualifier.

- Complete raw-row digest and origin identifiers reject drift, ambiguity and conflicting qualifications.
- Qualification is attached only to the two source observations, without changing exact chemical identity or treating feature intensities as concentrations.
- The new consumer is explicitly tested; no raw-field or generated-YAML hand edit substitutes for a maintained route.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R173-OWNER | data/natural_products/alkaloids/decarbamoylsaxitoxin.yaml; Complete post-intake owner, optional assertions and all history events | supports | Root read the complete owner after successful official intake: 17 occurrence, 1 producer and 1 locus assertions. No referenced external component is present. Optional fields: definition. |
| R173-LOCAL | /private/tmp/npm-review-work/173/local-sources.json; Complete resolved owner and all six officially captured raw row sets | context_only | All six captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB and NPClassifier sets match the frozen preparation, including empty sets. The separate seventh PubChem inventory comparison is distinguished below. Source fidelity does not itself establish experimental support. |
| R173-PUBCHEM-PREP | data/raw/pubchem_bioassay.tsv; Exact-key rows compared with the separate provisional seventh source set | context_only | The separate committed PubChem raw set contains 1 matching rows and reproduces the frozen preparation. This is not part of the official six-set intake. All matching rows were read by root; the 12 diazaquinomycin A observations are the only emitted assays. The separately prepared assay packet owns exact endpoint/call interpretation. Empty/no-assay-data rows elsewhere are not tested outcomes. |
| R173-Q133353 | https://www.wikidata.org/wiki/Q133353; P225 and P685 in the retained complete nine-entity response | context_only | Literal scientific name and NCBI taxon identifier agree with the matched source rows. Identifier routing does not establish occurrence chemistry, producing stock or experiment. |
| R173-Q309515 | https://www.wikidata.org/wiki/Q309515; P225 and P685 in the retained complete nine-entity response | context_only | Literal scientific name and NCBI taxon identifier agree with the matched source rows. Identifier routing does not establish occurrence chemistry, producing stock or experiment. |
| R173-Q310362 | https://www.wikidata.org/wiki/Q310362; P225 and P685 in the retained complete nine-entity response | context_only | Literal scientific name and NCBI taxon identifier agree with the matched source rows. Identifier routing does not establish occurrence chemistry, producing stock or experiment. |
| R173-Q5199328 | https://www.wikidata.org/wiki/Q5199328; P225 and P685 in the retained complete nine-entity response | context_only | Literal scientific name and NCBI taxon identifier agree with the matched source rows. Identifier routing does not establish occurrence chemistry, producing stock or experiment. |
| R173-TAXON-CONTEXT | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=112125,1163,1175,1220761,1427518,1510026,176275,1873482,1883,1956,28073,2926,344612,373637,38033,385555,39447,398006,467598,500485,54296,571,7461,77021,77022; Exact relevant TaxId, ScientificName, Rank, ParentTaxId and OtherNames fields | context_only | NCBI 398006 is Cylindrospermopsis raciborskii T3 at strain rank under 77022. The species response includes Raphidiopsis raciborskii as a synonym while retaining Cylindrospermopsis as its primary name. NCBI 467598 Microseira wollei includes Lyngbya wollei; 373637 Aulacomya atra lists Aulacomya ater as a misspelling. The four cyanobacterial genera, algal species, mollusks, fish and bee identities verify only routing; their exact compound/source resolution remains separately assessed. |
| R173-IMODULON | https://imodulondb.org/api/datasets; Complete 20-organism, 28-dataset official catalogue | context_only | The full retained catalogue establishes membership only. None of these exact native producer labels occurs in it. Listed S. albidoflavus, S. coelicolor or E. coli datasets do not establish an exact native producer/strain, introduced construct or relevant experimental condition for these owners. |
| S173-E-LOCAL | /private/tmp/npm-review-work/173/local-sources.json; Complete resolved owner, components and six captured source sets; seventh PubChem verified from raw TSV | context_only | The complete actual owner and six captured source sets match the prepared complete read; the seventh PubChem set was separately reread and compared field for field. Current methods and producer/locus tiers remain distinct from primary experimental conclusions. |
| S173-E-CONSUMERS | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Method loader/application 467–594; producer/locus emission 1070–1152; occurrence origin/exclusion rendering 1161–1264; exact citation, strain and LOTUS consumers statically read | context_only | Method-only overrides cannot change coordinates or producer host. WITHDRAW pins seven literal source-context fields and needs nonempty original methods; REPLACE lacks a direct complete-row digest guard. Claim references and producer-strain qualifications pin complete rows but do not suppress associations and reject structure-correction composition. LOTUS exclusions uniquely pin exact triples and complete rows; the inspected ChEBI-origin emission has no equivalent qualification hook. |
| S173-E-SCHEMA | /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml; ProducerEvidenceBasisEnum and ClusterLinkEvidenceEnum858–920 | context_only | ProducerEvidenceBasisEnum is expressly evidence in the named organism; heterologous cloned-locus evidence is a different question. The source list jointly drives producer and locus grades. |
| S173-E-SEARCH | /private/tmp/npm-review-work/173/science-search.json; Prepared exact source scope | context_only | Current exact-key/name/accession qualification search retained. This bounded decision-tree search does not establish absence of primary scientific evidence or generic consumers. |
| S173-E-LIMITS | /private/tmp/npm-review-work/shared-next-batch018/bgc-science/source-notes.json; Exact source read scopes, failed routes, required full-body gaps and source-specific records 171–175 | context_only | The frozen source preparation distinguishes complete original bodies, author-uploaded text, original abstracts and failed challenge/429 responses. No failed response is treated as a primary experimental body. |
| S173-E-MIBIG-173 | https://mibig.secondarymetabolites.org/repository/BGC0000188.5/annotations.json; Exact version, compound index 3, target compound evidence, taxonomy, loci, classes and legacy references; other compound chemistry is not certified. | context_only | Current official source keeps this target annotation and imported experimental labels. Database metadata identifies what the source asserts; it does not independently prove experimental applicability to the exact product. |
| S173-E-DC1983 | DOI:10.1080/00021369.1983.10865612; Complete three-page primary text read, exact PBT isolation/NMR/carbamoylation and organism context. | supports | Complete three-page primary text read, exact PBT isolation/NMR/carbamoylation and organism context. |
| S173-E-DC2008 | PMID:18487408; Complete scientific main/Methods/Results/Discussion and all tables/captions in original PMC2446512. Distinguishes congener reports, hypothetical enzymatic steps and measured early intermediates. | supports | Complete scientific main/Methods/Results/Discussion and all tables/captions in original PMC2446512. Distinguishes congener reports, hypothetical enzymatic steps and measured early intermediates. |
| S173-E-DC2010 | PMID:20048055; Complete scientific main/Methods/Results/Discussion and all tables/captions in original PMC2820976, including fourteen A. gracile strains and direct dcSTX LC-MS confirmation against standards. | supports | Complete scientific main/Methods/Results/Discussion and all tables/captions in original PMC2820976, including fourteen A. gracile strains and direct dcSTX LC-MS confirmation against standards. |
| S173-E-DC2001-ABSTRACT | PMID:11348083; Exact original abstract/title/article identifiers; full 2001 experimental body unavailable after bounded publisher request. | partial | Exact original abstract/title/article identifiers; full 2001 experimental body unavailable after bounded publisher request. |
| S173-E-PUBMED | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=31897521,18487408,25157164,12740803,12924931,15019474,16192070,16544882,17996918,20048055,22960450&amp;retmode=xml; All eleven own article titles, abstracts and PubmedData/ArticleIdList entries, including the eight distinct cited dcSTX occurrence papers. This is abstract-level evidence, not full experimental bodies. | partial | All eleven own article titles, abstracts and PubmedData/ArticleIdList entries, including the eight distinct cited dcSTX occurrence papers. This is abstract-level evidence, not full experimental bodies. |
| S173-E-BEE2017 | DOI:10.1371/journal.pone.0175573; Scientific main read through Methods/Discussion; Table1 completely scanned for dcSTX, but unrelated numerical Table1 rows not all manually transcribed. Main calls differential identifications putative; no dcSTX-specific standard result. | supports | Scientific main read through Methods/Discussion; Table1 completely scanned for dcSTX, but unrelated numerical Table1 rows not all manually transcribed. Main calls differential identifications putative; no dcSTX-specific standard result. |
| S173-E-BEE-STUDY | MTBLS379; Official study title, publication, all experimental protocol descriptions, assay filenames and public-study metadata; unrelated account/contact fields are not used. | supports | Official study title, publication, all experimental protocol descriptions, assay filenames and public-study metadata; unrelated account/contact fields are not used. |
| S173-E-BEE-MAF | MTBLS379; All7916 rows scanned for exact CHEBI133919/name; three dcSTX rows fully inspected including chemical representations, MSI:2, retention times, mass/charge and20 abundance fields. No re-identification from raw spectra. | supports | All7916 rows scanned for exact CHEBI133919/name; three dcSTX rows fully inspected including chemical representations, MSI:2, retention times, mass/charge and20 abundance fields. No re-identification from raw spectra. |
| S173-E-BEE-SAMPLES | MTBLS379; All20 sample rows inspected: brain, Apis cerana, ten mite-infested and ten control sample labels. | supports | All20 sample rows inspected: brain, Apis cerana, ten mite-infested and ten control sample labels. |
| S173-E-GB-DC | GenBank:DQ787200.1; Complete header and all source/gene/CDS annotation fields excluding full residue-by-residue translation/base verification. | supports | Complete header and all source/gene/CDS annotation fields excluding full residue-by-residue translation/base verification. |
| C173-OWNER | data/natural_products/alkaloids/decarbamoylsaxitoxin.yaml; Complete owner and all seven matching source-row sets; no referenced components | supports | The complete owner denotes decarbamoylsaxitoxin under CHEBI:133919. All source selectors, versions and complete row digests are retained in COMPARISON: [{"row_sha256": "f706af2abfa361e9921be0a4d962fe97fad33bc7f816df7bf429732965ff6807", "selector": "BGC0000188:3", "version": "5"}]. The official intake and prepared owner bytes agree. |
| C173-GRAPH | /private/tmp/npm-review-work/173/chemistry.json; Fresh intake RDKit result and frozen Standard/fixed-H comparison | supports | The stored SMILES recomputes to VRRIYZJUSNMZMP-PJPYAQQDSA-N, formula C9H16N6O3, formal charge 0; stored InChI/key agree. These are representation checks, not experimental identity proof. |
| C173-COMPARISON | /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/chemical-comparison.json; Record 173; exact source rows and each graph comparison | supports | Exact Standard, fixed-H, formula, charge and stereo comparisons of the retained owner, complete raw rows and current authority responses; primary experimental proof is assessed separately. |
| C173-LOCAL-SEARCH | /private/tmp/npm-review-work/173/chemistry-search-receipt.json; Exact full key, label, slug and source selector in raw/owner/curation trees | supports | Ignored-inclusive bounded search preserves all matching paths; an absent curation decision does not imply a missing scientific source. |
| C173-CHEBI-SEARCH-1 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=VRRIYZJUSNMZMP-PJPYAQQDSA-N&amp;size=100; Literal key search; chebi-key-173.json | supports | 1 returned name/key results; evaluate exact key and stars, not name similarity. |
| C173-CHEBI-SEARCH-2 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=decarbamoylsaxitoxin&amp;size=100; Literal name search; chebi-name-173.json | supports | 2 returned name/key results; evaluate exact key and stars, not name similarity. |
| C173-AUTH-1 | https://mibig.secondarymetabolites.org/repository/BGC0000188.5/annotations.json; compounds[2].structure; BGC0000188.5.json | supports | current MIBiG BGC0000188:3: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C173-AUTH-2 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/24941628/property/IsomericSMILES,InChI,InChIKey,MolecularFormula/JSON; PropertyTable.Properties[].SMILES; pubchem-24941628.json | supports | PubChem literal 24941628: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C173-AUTH-3 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/24941628/SDF?record_type=2d; first complete SDF; pubchem-24941628.sdf | supports | PubChem SDF literal 24941628: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C173-AUTH-4 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/133919/; default_structure.smiles; CHEBI133919.json | supports | ChEBI JSON 133919: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N; exact stored Standard key match=True, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C173-AUTH-5 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/133919/; official MOL endpoint; CHEBI133919-official.mol | supports | ChEBI MOL 133919: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N; exact stored Standard key match=True, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C173-AUTH-6 | https://www.wikidata.org/wiki/Special:EntityData/Q27277104.json; P2017; Q27277104.json | supports | Wikidata Q27277104: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C173-AUTH-7 | https://www.wikidata.org/wiki/Special:EntityData/Q27277104.json; P233; Q27277104.json | context_only | Wikidata Q27277104: representation parses=True; parsed key VRRIYZJUSNMZMP-UHFFFAOYSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. Canonical P233 is not an isomeric stereo assertion; compare P2017 when present. |
| C173-AUTH-8 | https://www.wikidata.org/wiki/Special:EntityData/Q27277104.json; P234 Standard InChI (normalized reconstruction; not a literal fixed-H assertion); Q27277104.json | supports | Wikidata Q27277104: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N; exact stored Standard key match=True, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C173-CONSUMERS | src/naturalproductmech/curate/structure_corrections.py; Complete correction consumer and separately pinned selector/collision comparison | supports | Only REPLACE_WITH_CHEBI and SPLIT_SHARED_WITH_CHEBI are implemented. They require a unique structured three-star committed target and complete original/target row hashes; arbitrary primary SMILES and label overrides are not accepted. The loader copies target SMILES, so valid MOL versus invalid JSON text must be distinguished. It clears old xrefs and rebuilds exact-key joins. Existing claim-reference and strain consumers reject structure_correction_note; composition needs explicit implementation and tests. |
| C173-XREF-CONSUMER | src/naturalproductmech/curate/xref_exclusions.py; Complete literal-xref exclusion consumer; pubchem/npatlas namespace and full-row guard | supports | A specific existing literal pubchem or npatlas assertion can be excluded under the exact original BGC:compound_index selector and complete row hash. This neither installs a positive xref nor migrates biological observations. It rejects a structure-corrected row; compatible stacking is not assumed. |
| C173-ROUTING | /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/grounding-source-selector-routing.json; Exact scoped calculation; original inputs, version and limitations retained | supports | Complete source selectors and mints reproduce, each full original row is unique, and exact diagnostic alternate keys for171/180 have no committed eligible CheBI or MIBiG target in the inspected inventory. Existing-decision absence is limited to the two complete maintained TSVs searched ignored-inclusively. |
| C173-PRIMARY-1983 | DOI:10.1080/00021369.1983.10865612; Complete original three-page extracted text; NMR/chromatography and carbamoylation comparison; retained /private/tmp/npm-review-work/shared-next-batch018/bgc-science/attempt-004/dcstx1983-primary.pdf | supports | Shellfish toxin was compared with decarbamoylsaxitoxin prepared from saxitoxin and chemically converted back to saxitoxin. This supports exact chemical identity at the reported comparison scope, not every later taxon occurrence or a new absolute re-refinement. |
| C173-MICROSTATE | /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/microstate-comparison-v3.json; Exact scoped calculation; original inputs, version and limitations retained | supports | Retained amino/endo-imino and ChEBI diimino forms have the same full Standard InChI and stereochemistry, with positive guanidine hydrogen/bond-placement tautomerism and different fixed-H forms. The earlier cached legacy CIP discrepancy is explicitly superseded; there is no atom 7 enantiomer conflict. |
| C173-RAW-CHEMSPIDER | /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/chemspider94709-raw-source-comparison.json; Exact scoped calculation; original inputs, version and limitations retained | supports | Raw-only ChemSpider94709 resolves to IOGRODCJ with one undefined centre, not the full PJPYAQQD key. The current seeder excludes the ChemSpider namespace, so no emitted xref is affected. |

## Limits And Additional Notes

- The root section inventories present claims and source routing; chemical identities, source-specific experiments, definition claims and optional-content assertions require their separately scoped scientific assessments.
- Original retrieval times and immutable source snapshots are reused; authoring time is not represented as new source access.
- Exact chemical identity/authority repairs and general taxonomic/classification/history checks are independently assessed. Any combined biological and chemical correction must explicitly adjudicate old-key associations and consumer composition.
- Authority matches establish the representations actually returned at their retained access times; they are not independent experimental structure or absolute-hand determinations. Root and science sections separately assess organism, locus, classification and history claims.
- The retained amino/endo-imino form and ChEBI diimino form have identical full Standard InChI, formula, charge and stereochemistry, with a positive guanidine proton/bond-placement tautomer relationship but different fixed-H InChI. Do not call this constitutional or enantiomeric disagreement. The legacy-CIP diagnostic error is corrected explicitly in v3.
- The reproduction report retains 42 withheld ambiguous producer claims, 161 merged-taxon rewrites and five unresolved assay-organism targets.
- 499 identifier-label plausibility warnings are non-blocking; 4750 pairs have no configured adapter and were skipped.
- Four tests were skipped and two dependency deprecation warnings remain. Passing configured QC is not independent scientific verification.
- Native baseline gates establish configured consistency, not independent biological production, exact stereochemistry or primary-source adequacy.
- The full configured gate logs retain warnings, skipped tests, identifier exceptions and no-adapter pairs; a successful command does not convert these into verified scientific claims.
- Ontology caches may be reused by the canonical identifier-label gate. Fresh command execution is not proof every remote authority was refreshed.
- Every tracked byte stream/mode and ignored-inclusive corpus/review YAML population was checked; external caches and generated bytecode are not asserted to be independently byte-pinned.
- No scientific owner, inventory, curation table, native status or history was edited. Actions are proposed work.
- Shared baseline gates and target strict validation retain their actual fresh command receipts for this base. Scientific failed or unavailable checks are distinct from bundle validation.

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
review_id: 20261021T215506Z-decarbamoylsaxitoxin
title: 'Decarbamoylsaxitoxin: occurrence citations and identification scope'
started_at: '2026-10-21T21:49:34.902039Z'
finished_at: '2026-10-21T21:55:06.976731Z'
completion: partial
verdict: needs_curation
scientific_review: true
summary: The chemical identity and the native T3 culture evidence are supported, while
  four genus-specific occurrence assertions cite a 1983 study of a different sampled
  organism. Bee brain annotations and acid-extraction products need explicit identification
  and origin qualifications. Several remaining occurrence sources could only be inspected
  as abstracts, so the review remains partial. The alternative guanidine representations
  are tautomers with matching Standard InChI, not an enantiomer conflict.
source:
  git_revision: f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
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
  - path: data/natural_products/alkaloids/cytochalasin-k.yaml
    sha256: 5215ed06eb842344613ad7d7ca93ce83da3169506610abc5b87ed1a533e8840d
    role: context
  - path: data/natural_products/alkaloids/cytoglobosin-x.yaml
    sha256: bab71c2aff04171fbd153a3088980b77ddfad1c87dfd438bb5b304105ed203b4
    role: context
  - path: data/natural_products/alkaloids/decarbamoylsaxitoxin.yaml
    sha256: d9b4ca68866bf479dab3a048ea216f85c309c957742cbd8a213cb6f2d5965ba0
    role: target
  - path: data/natural_products/alkaloids/dehydro-tilivalline.yaml
    sha256: ba126a1e86577027443bab9c9c2a320de3584855d052e49476e56c3c55b70652
    role: context
  - path: data/natural_products/alkaloids/dehydrohistidyltryptophanyldiketopiperazine.yaml
    sha256: 2c289074bbcca634022e442b51bd80bf9aff59948d35d1f37fd051a3aca3a37a
    role: context
  - path: data/natural_products/alkaloids/demethoxygriseoluteic-acid.yaml
    sha256: 4eb28c9719232dfe0d91a29df6b842af19c108422ad766336ac8a88326763081
    role: context
  - path: data/natural_products/alkaloids/desmethylbassianin.yaml
    sha256: 8c4fedf5f7829666b122fb1e0177da850d578cad7265d9cf00867008c48d9bb5
    role: context
  - path: data/natural_products/alkaloids/diastaphenazine.yaml
    sha256: e80c885728a4aabc6e6e1aa417cf7afa7b2ddf792334728610afc27efe9a69f8
    role: context
  - path: data/natural_products/alkaloids/diazaquinomycin-a.yaml
    sha256: 64b4c698e7a31939bb5e12f97220bfba746475487a6ae89ec03963bbf0568261
    role: context
  - path: data/natural_products/alkaloids/diazaquinomycin-e.yaml
    sha256: 3438673a011d56c1e6b842b82f90e5d9642d0afd1a0169d385812f22251082a6
    role: context
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
  - path: src/naturalproductmech/curate/bioassay_exclusions.py
    sha256: 4a4176e072ac9759aa8a9e88300d7e2de5aaf4ebf30b5c42fcf4c9c0b6cebbb4
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
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
  - path: tests/test_bioassay_exclusions.py
    sha256: 099a0b8f6f51ce93406344440b63d99db7203486ed92797d90990005bdb6bbd0
    role: context
  - path: tests/test_capsular_curation.py
    sha256: 33fc880aa197ac90693ae75a59e79a93bbf22e65d544b1762616fdc54fa85001
    role: context
  - path: tests/test_claim_references.py
    sha256: 11b2fc60dbe32154df63fb2e8c784c7c8ba6585581c09bba2eebe2c5192d4c06
    role: context
  - path: tests/test_compound3_curation.py
    sha256: 0455a48e25ec56f5d5fa141c3318fee860e47a7885ee75cab36f6c42f7acd785
    role: context
  - path: tests/test_ferrichrome_curation.py
    sha256: 70fefc22ec85b952617e7370aee395c948e2d6477e3431507e8c5451c32b94ad
    role: context
  - path: tests/test_fogacin_locus_scope.py
    sha256: 7562d539700576ad848b548699f6d4c7d7dfe4ad7a1c04d3b4db1bc8457ef129
    role: context
  - path: tests/test_gentamicin_curation.py
    sha256: 7330dacb16aace87281368b0801eed5988ad90970a22152072368effe81976ff
    role: context
  - path: tests/test_lomaiviticin_curation.py
    sha256: 52267ca7a3932711d3cc54bd57e29320261a126727a0a40fadc04fda8e26f700
    role: context
  - path: tests/test_lotus_exclusions.py
    sha256: 3e3aa443714202e1bc41f0fb236e6bf69caabd68a16af23b972323f5f846386c
    role: context
  - path: tests/test_mibig_locus_evidence_overrides.py
    sha256: 9177b5bd24f6e47cc4743857179217d9e0d4add9560b2ce3faefaebe53ba09a0
    role: context
  - path: tests/test_myxochromide_curation.py
    sha256: 67630f73544870e90e374ea6634fa6b70f1fc126684181a0207a115904a2046a
    role: context
  - path: tests/test_producer_strains.py
    sha256: 17002ef1640464777f1925d12d842ed83c9098aad6de724ae0ea236ecccc4ff3
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 173, batch 018, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated targets in earlier
    batch commits (publication tracked separately). At selection, 224 of 3116 current
    records had campaign coverage and 2892 remained. The population search included
    ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CHEBI:133919
targets:
- target_id: CHEBI:133919
  path: data/natural_products/alkaloids/decarbamoylsaxitoxin.yaml
  label: decarbamoylsaxitoxin
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
  - CHEBI:133919
  command: just validate-strict data/natural_products/alkaloids/decarbamoylsaxitoxin.yaml
    --out /private/tmp/npm-review-work/173/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T21:49:36.523498Z
- check_id: shared-verify-corpus
  name: Corpus path and filing integrity
  status: passed
  required: true
  summary: All 3116 corpus records are filed exactly where PATHS.tsv pins them.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-018-baseline-verify-corpus-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just verify-corpus --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh batch018 execution on f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T21:43:11.095314Z;
    finished 2026-10-21T21:43:43.016017Z; root observed terminal0 at 2026-10-21T21:46:19.304730Z.
    Actual receipt: /private/tmp/npm-native-checks/batch-018/verify-corpus.json; exact
    transcript: /private/tmp/npm-native-checks/batch-018/verify-corpus.log; input
    proof: /private/tmp/npm-native-checks/batch-018/verify-corpus-fresh-inputs.json.
    Dedicated pytest basetemp isolates fixture retention; no cleanup was performed.
    Warnings, skips and configured exceptions remain part of this gate scope.'
  target_ids:
  - CHEBI:133919
- check_id: shared-verify-reproduction
  name: Corpus reproduction
  status: passed
  required: true
  summary: All 3116 records reproduce byte-for-byte from data/raw/.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-018-baseline-verify-reproduction-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just verify-reproduction --summary
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh batch018 execution on f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T21:43:11.049802Z;
    finished 2026-10-21T21:44:10.266611Z; root observed terminal0 at 2026-10-21T21:46:19.305204Z.
    Actual receipt: /private/tmp/npm-native-checks/batch-018/verify-reproduction.json;
    exact transcript: /private/tmp/npm-native-checks/batch-018/verify-reproduction.log;
    input proof: /private/tmp/npm-native-checks/batch-018/verify-reproduction-fresh-inputs.json.
    Dedicated pytest basetemp isolates fixture retention; no cleanup was performed.
    Warnings, skips and configured exceptions remain part of this gate scope.'
  target_ids:
  - CHEBI:133919
- check_id: shared-review-queue
  name: Native deterministic review queue
  status: passed
  required: true
  summary: The canonical review-queue command completed with actual exit0 on the fresh
    main base; exact output, warnings and skips remain in the pinned transcript.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-018-baseline-review-queue-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just review-queue --tsv /private/tmp/npm-review-queue-batch-018.tsv
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh batch018 execution on f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T21:43:11.094986Z;
    finished 2026-10-21T21:43:27.046585Z; root observed terminal0 at 2026-10-21T21:43:37.247816Z.
    Actual receipt: /private/tmp/npm-native-checks/batch-018/review-queue.json; exact
    transcript: /private/tmp/npm-native-checks/batch-018/review-queue.log; input proof:
    /private/tmp/npm-native-checks/batch-018/review-queue-fresh-inputs.json. Dedicated
    pytest basetemp isolates fixture retention; no cleanup was performed. Warnings,
    skips and configured exceptions remain part of this gate scope.'
  target_ids:
  - CHEBI:133919
- check_id: shared-validate-products
  name: Configured ontology identifier-label correspondence
  status: passed
  required: true
  summary: 'Configured identifier-label validation exited zero: 13449 canonical matches,
    646 synonym matches and 35 configured exceptions; 499 non-blocking warnings and
    4750 no-adapter skips remain.'
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-018-baseline-validate-products-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just validate-products
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh batch018 execution on f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T21:43:11.095805Z;
    finished 2026-10-21T21:44:09.649497Z; root observed terminal0 at 2026-10-21T21:46:19.305601Z.
    Actual receipt: /private/tmp/npm-native-checks/batch-018/validate-products.json;
    exact transcript: /private/tmp/npm-native-checks/batch-018/validate-products.log;
    input proof: /private/tmp/npm-native-checks/batch-018/validate-products-fresh-inputs.json.
    Dedicated pytest basetemp isolates fixture retention; no cleanup was performed.
    Warnings, skips and configured exceptions remain part of this gate scope.'
  target_ids:
  - CHEBI:133919
- check_id: shared-qc
  name: Full repository quality gate on the fresh main baseline
  status: passed
  required: true
  summary: Full fresh-base quality command completed successfully:999 tests passed,4
    skipped,2 warnings;3116 records passed closed schema validation and corpus reproduction,
    and generated pages were current.
  command: UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/npm-review-uv-cache RECORD_REVIEW_BASE=f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
    PYTEST_ADDOPTS=--basetemp=/private/tmp/npm-review-pytest/batch-018-baseline-qc-attempt-001
    PYTHONDONTWRITEBYTECODE=1 just qc
  exit_code: 0
  expected_exit_code: 0
  scope_note: 'Fresh batch018 execution on f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
    in /private/tmp/npm-record-reviews-20261021. Started 2026-10-21T21:43:11.050051Z;
    finished 2026-10-21T21:48:43.599885Z; root observed terminal0 at 2026-10-21T21:48:54.733149Z.
    Actual receipt: /private/tmp/npm-native-checks/batch-018/qc.json; exact transcript:
    /private/tmp/npm-native-checks/batch-018/qc.log; input proof: /private/tmp/npm-native-checks/batch-018/qc-fresh-inputs.json.
    Dedicated pytest basetemp isolates fixture retention; no cleanup was performed.
    Warnings, skips and configured exceptions remain part of this gate scope.'
  target_ids:
  - CHEBI:133919
- check_id: R173-FULL-OWNER
  name: Complete owner and captured-source scope
  status: passed
  required: true
  summary: Successful official intake and a fresh root full-owner/read receipt precede
    this authoring. All six officially captured sets and the separately mechanically
    parsed seventh PubChem set match. All matching raw rows and 12 written diazaquinomycin
    A observations were read by root; primary assay interpretation remains separately
    scoped. No BindingDB or graph assertion is present. The external component set
    is empty.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - R173-OWNER
  - R173-LOCAL
  - R173-PUBCHEM-PREP
- check_id: S173-C-LOTUS1983
  name: Exact taxon applicability of the four 1983 LOTUS triples
  status: failed
  required: true
  summary: The complete three-page 1983 study isolates PBT=dcSTX from Spondylus butleri
    associated with a Pyrodinium bloom. It does not report Anabaena, Aphanizomenon,
    Lyngbya or Cylindrospermopsis as the sampled or detected organisms.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC1983
- check_id: S173-C-OCCURRENCE-DETAILS
  name: Required source-specific occurrence and congener checks
  status: unavailable
  required: true
  summary: The 2001 body and several cited occurrence studies remain abstract-only
    after bounded public routes. Standards, derivative signals, human metabolites,
    extraction products and exact source-organism results cannot all be resolved from
    those abstracts. Known positive cultures and deposited putative bee annotations
    are retained explicitly.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC2001-ABSTRACT
  - S173-E-PUBMED
  - S173-E-LIMITS
  - S173-E-DC2010
  - S173-E-BEE-MAF
- check_id: C173-C-REPRESENTATION
  name: Stored chemical representation and complete source row
  status: passed
  required: true
  summary: Fresh intake derivation agrees with the stored graph; the source selector,
    full row and prepared snapshot were independently rechecked.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - C173-OWNER
  - C173-GRAPH
  - C173-COMPARISON
- check_id: C173-C-XREF
  name: Literal identifier resolution and parsed representation
  status: passed
  required: true
  summary: Every present literal was resolved; differing Standard/fixed-H, charge
    or precision is assessed separately. For invalid default ChEBI JSON SMILES, the
    independently fetched official MOL supplies the parsed comparison.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - C173-COMPARISON
  - C173-AUTH-1
  - C173-AUTH-2
  - C173-AUTH-3
  - C173-AUTH-4
  - C173-AUTH-5
  - C173-AUTH-6
  - C173-AUTH-7
  - C173-AUTH-8
- check_id: C173-C-STANDARD-IDENTITY
  name: Exact Standard identity and tautomer boundary
  status: passed
  required: true
  summary: Unique 3-star CHEBI133919 and literal PubChem24941628 match the full Standard
    identity. The definition describes the CheBI diimino tautomer; the retained depiction
    uses the amino/endo-imino form. This is not constitutional or stereochemical disagreement.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - C173-PRIMARY-1983
  - C173-MICROSTATE
  - C173-RAW-CHEMSPIDER
  - C173-COMPARISON
evidence:
- evidence_id: R173-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/decarbamoylsaxitoxin.yaml
  locator: Complete post-intake owner, optional assertions and all history events
  accessed_at: '2026-10-21T21:50:20.704182Z'
  support: supports
  summary: 'Root read the complete owner after successful official intake: 17 occurrence,
    1 producer and 1 locus assertions. No referenced external component is present.
    Optional fields: definition.'
  snapshot_sha256: d9b4ca68866bf479dab3a048ea216f85c309c957742cbd8a213cb6f2d5965ba0
- evidence_id: R173-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/173/local-sources.json
  locator: Complete resolved owner and all six officially captured raw row sets
  accessed_at: '2026-10-21T21:50:20.704182Z'
  support: context_only
  summary: All six captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB and
    NPClassifier sets match the frozen preparation, including empty sets. The separate
    seventh PubChem inventory comparison is distinguished below. Source fidelity does
    not itself establish experimental support.
  snapshot_sha256: 3296b2b780066c9c9fff528a43a83b2d6e0dd326445bc73c2752c94e959016b6
- evidence_id: R173-PUBCHEM-PREP
  kind: record_content
  reference: data/raw/pubchem_bioassay.tsv
  locator: Exact-key rows compared with the separate provisional seventh source set
  accessed_at: '2026-10-21T21:50:26.370500Z'
  support: context_only
  summary: The separate committed PubChem raw set contains 1 matching rows and reproduces
    the frozen preparation. This is not part of the official six-set intake. All matching
    rows were read by root; the 12 diazaquinomycin A observations are the only emitted
    assays. The separately prepared assay packet owns exact endpoint/call interpretation.
    Empty/no-assay-data rows elsewhere are not tested outcomes.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: R173-Q133353
  kind: database
  reference: https://www.wikidata.org/wiki/Q133353
  locator: P225 and P685 in the retained complete nine-entity response
  accessed_at: '2026-10-21T20:16:18.792344Z'
  support: context_only
  summary: Literal scientific name and NCBI taxon identifier agree with the matched
    source rows. Identifier routing does not establish occurrence chemistry, producing
    stock or experiment.
  snapshot_sha256: 618d1ed87da35071c378273e14a8b5030f73f9485418b509039d6437d0372f92
- evidence_id: R173-Q309515
  kind: database
  reference: https://www.wikidata.org/wiki/Q309515
  locator: P225 and P685 in the retained complete nine-entity response
  accessed_at: '2026-10-21T20:16:18.792344Z'
  support: context_only
  summary: Literal scientific name and NCBI taxon identifier agree with the matched
    source rows. Identifier routing does not establish occurrence chemistry, producing
    stock or experiment.
  snapshot_sha256: 618d1ed87da35071c378273e14a8b5030f73f9485418b509039d6437d0372f92
- evidence_id: R173-Q310362
  kind: database
  reference: https://www.wikidata.org/wiki/Q310362
  locator: P225 and P685 in the retained complete nine-entity response
  accessed_at: '2026-10-21T20:16:18.792344Z'
  support: context_only
  summary: Literal scientific name and NCBI taxon identifier agree with the matched
    source rows. Identifier routing does not establish occurrence chemistry, producing
    stock or experiment.
  snapshot_sha256: 618d1ed87da35071c378273e14a8b5030f73f9485418b509039d6437d0372f92
- evidence_id: R173-Q5199328
  kind: database
  reference: https://www.wikidata.org/wiki/Q5199328
  locator: P225 and P685 in the retained complete nine-entity response
  accessed_at: '2026-10-21T20:16:18.792344Z'
  support: context_only
  summary: Literal scientific name and NCBI taxon identifier agree with the matched
    source rows. Identifier routing does not establish occurrence chemistry, producing
    stock or experiment.
  snapshot_sha256: 618d1ed87da35071c378273e14a8b5030f73f9485418b509039d6437d0372f92
- evidence_id: R173-TAXON-CONTEXT
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=112125,1163,1175,1220761,1427518,1510026,176275,1873482,1883,1956,28073,2926,344612,373637,38033,385555,39447,398006,467598,500485,54296,571,7461,77021,77022
  locator: Exact relevant TaxId, ScientificName, Rank, ParentTaxId and OtherNames
    fields
  accessed_at: '2026-10-21T20:16:19.157506Z'
  support: context_only
  summary: NCBI 398006 is Cylindrospermopsis raciborskii T3 at strain rank under 77022.
    The species response includes Raphidiopsis raciborskii as a synonym while retaining
    Cylindrospermopsis as its primary name. NCBI 467598 Microseira wollei includes
    Lyngbya wollei; 373637 Aulacomya atra lists Aulacomya ater as a misspelling. The
    four cyanobacterial genera, algal species, mollusks, fish and bee identities verify
    only routing; their exact compound/source resolution remains separately assessed.
  snapshot_sha256: 10cf506b9c7a3918100ff016e4681733f450deced1f583bd9100ae2a1a6fe4cb
- evidence_id: R173-IMODULON
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete 20-organism, 28-dataset official catalogue
  accessed_at: '2026-10-21T20:16:18.346411Z'
  support: context_only
  summary: The full retained catalogue establishes membership only. None of these
    exact native producer labels occurs in it. Listed S. albidoflavus, S. coelicolor
    or E. coli datasets do not establish an exact native producer/strain, introduced
    construct or relevant experimental condition for these owners.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: S173-E-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/173/local-sources.json
  locator: Complete resolved owner, components and six captured source sets; seventh
    PubChem verified from raw TSV
  accessed_at: '2026-10-21T21:50:50.396526Z'
  support: context_only
  summary: The complete actual owner and six captured source sets match the prepared
    complete read; the seventh PubChem set was separately reread and compared field
    for field. Current methods and producer/locus tiers remain distinct from primary
    experimental conclusions.
  snapshot_sha256: 3296b2b780066c9c9fff528a43a83b2d6e0dd326445bc73c2752c94e959016b6
- evidence_id: S173-E-CONSUMERS
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Method loader/application 467–594; producer/locus emission 1070–1152; occurrence
    origin/exclusion rendering 1161–1264; exact citation, strain and LOTUS consumers
    statically read
  accessed_at: '2026-10-21T21:50:50.396526Z'
  support: context_only
  summary: Method-only overrides cannot change coordinates or producer host. WITHDRAW
    pins seven literal source-context fields and needs nonempty original methods;
    REPLACE lacks a direct complete-row digest guard. Claim references and producer-strain
    qualifications pin complete rows but do not suppress associations and reject structure-correction
    composition. LOTUS exclusions uniquely pin exact triples and complete rows; the
    inspected ChEBI-origin emission has no equivalent qualification hook.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: S173-E-SCHEMA
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/src/naturalproductmech/schema/naturalproductmech.yaml
  locator: ProducerEvidenceBasisEnum and ClusterLinkEvidenceEnum858–920
  accessed_at: '2026-10-21T21:50:50.396526Z'
  support: context_only
  summary: ProducerEvidenceBasisEnum is expressly evidence in the named organism;
    heterologous cloned-locus evidence is a different question. The source list jointly
    drives producer and locus grades.
  snapshot_sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
- evidence_id: S173-E-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/173/science-search.json
  locator: Prepared exact source scope
  accessed_at: '2026-10-21T21:50:50.403744Z'
  support: context_only
  summary: Current exact-key/name/accession qualification search retained. This bounded
    decision-tree search does not establish absence of primary scientific evidence
    or generic consumers.
  snapshot_sha256: 8b6d2298b9f2b8ca3e55264686e8f7d3e4eb88ed10b5597a965a766143fe464d
  search_scope: rg --no-ignore --hidden -n -F over curation, using exact identifier,
    label, Standard InChIKey and every relevant BGC accession.
- evidence_id: S173-E-LIMITS
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch018/bgc-science/source-notes.json
  locator: Exact source read scopes, failed routes, required full-body gaps and source-specific
    records 171–175
  accessed_at: '2026-10-21T20:18:55.674166Z'
  support: context_only
  summary: The frozen source preparation distinguishes complete original bodies, author-uploaded
    text, original abstracts and failed challenge/429 responses. No failed response
    is treated as a primary experimental body.
  snapshot_sha256: 33c9703c2904e5399faa77331c2f68256d2a1f58927ef5e2cab47754f87e04d3
- evidence_id: S173-E-MIBIG-173
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000188.5/annotations.json
  locator: Exact version, compound index 3, target compound evidence, taxonomy, loci,
    classes and legacy references; other compound chemistry is not certified.
  accessed_at: '2026-10-21T20:14:38.613216Z'
  support: context_only
  summary: Current official source keeps this target annotation and imported experimental
    labels. Database metadata identifies what the source asserts; it does not independently
    prove experimental applicability to the exact product.
  snapshot_sha256: f34f78a039888d795b18aa7e044c0e8504afe7a5008685f0d6651ece0e18f805
- evidence_id: S173-E-DC1983
  kind: primary_source
  reference: DOI:10.1080/00021369.1983.10865612
  locator: Complete three-page primary text read, exact PBT isolation/NMR/carbamoylation
    and organism context.
  accessed_at: '2026-10-21T20:10:14.512206Z'
  support: supports
  summary: Complete three-page primary text read, exact PBT isolation/NMR/carbamoylation
    and organism context.
  snapshot_sha256: 8d5f2164091fc1113013e8962e6e76aceaf5d5f5d7f2f21c35122fe439202b7f
- evidence_id: S173-E-DC2008
  kind: primary_source
  reference: PMID:18487408
  locator: Complete scientific main/Methods/Results/Discussion and all tables/captions
    in original PMC2446512. Distinguishes congener reports, hypothetical enzymatic
    steps and measured early intermediates.
  accessed_at: '2026-10-21T20:10:13.737332Z'
  support: supports
  summary: Complete scientific main/Methods/Results/Discussion and all tables/captions
    in original PMC2446512. Distinguishes congener reports, hypothetical enzymatic
    steps and measured early intermediates.
  snapshot_sha256: ff6ff7b48eca3a2bd8196bbbc08b3c4085ce5eb099dccf3e3d1f6f9099932c8c
- evidence_id: S173-E-DC2010
  kind: primary_source
  reference: PMID:20048055
  locator: Complete scientific main/Methods/Results/Discussion and all tables/captions
    in original PMC2820976, including fourteen A. gracile strains and direct dcSTX
    LC-MS confirmation against standards.
  accessed_at: '2026-10-21T20:10:14.045252Z'
  support: supports
  summary: Complete scientific main/Methods/Results/Discussion and all tables/captions
    in original PMC2820976, including fourteen A. gracile strains and direct dcSTX
    LC-MS confirmation against standards.
  snapshot_sha256: 4e55e763f813cad803bc790e1d6065586b5df24c669aaba4c457b2f260250ac8
- evidence_id: S173-E-DC2001-ABSTRACT
  kind: primary_source
  reference: PMID:11348083
  locator: Exact original abstract/title/article identifiers; full 2001 experimental
    body unavailable after bounded publisher request.
  accessed_at: '2026-10-21T20:11:33.179183Z'
  support: partial
  summary: Exact original abstract/title/article identifiers; full 2001 experimental
    body unavailable after bounded publisher request.
  snapshot_sha256: df9fc99de9453be8d1771171bff9072384fd021a99f4f88e01a6f1ea8a5d1173
- evidence_id: S173-E-PUBMED
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=31897521,18487408,25157164,12740803,12924931,15019474,16192070,16544882,17996918,20048055,22960450&retmode=xml
  locator: All eleven own article titles, abstracts and PubmedData/ArticleIdList entries,
    including the eight distinct cited dcSTX occurrence papers. This is abstract-level
    evidence, not full experimental bodies.
  accessed_at: '2026-10-21T20:05:09.356964Z'
  support: partial
  summary: All eleven own article titles, abstracts and PubmedData/ArticleIdList entries,
    including the eight distinct cited dcSTX occurrence papers. This is abstract-level
    evidence, not full experimental bodies.
  snapshot_sha256: 58de0028aa2e09deffccd00426dc6f6acfa53ae88fab88089ba6c1aec9c51ea9
- evidence_id: S173-E-BEE2017
  kind: primary_source
  reference: DOI:10.1371/journal.pone.0175573
  locator: Scientific main read through Methods/Discussion; Table1 completely scanned
    for dcSTX, but unrelated numerical Table1 rows not all manually transcribed. Main
    calls differential identifications putative; no dcSTX-specific standard result.
  accessed_at: '2026-10-21T20:14:28.235648Z'
  support: supports
  summary: Scientific main read through Methods/Discussion; Table1 completely scanned
    for dcSTX, but unrelated numerical Table1 rows not all manually transcribed. Main
    calls differential identifications putative; no dcSTX-specific standard result.
  snapshot_sha256: b372eaa6cb2c58db5c0d44099c0c021e0cdf952a8cb3b84fb4af00d767711752
- evidence_id: S173-E-BEE-STUDY
  kind: primary_source
  reference: MTBLS379
  locator: Official study title, publication, all experimental protocol descriptions,
    assay filenames and public-study metadata; unrelated account/contact fields are
    not used.
  accessed_at: '2026-10-21T20:11:34.294348Z'
  support: supports
  summary: Official study title, publication, all experimental protocol descriptions,
    assay filenames and public-study metadata; unrelated account/contact fields are
    not used.
  snapshot_sha256: 023e3505af2c2e8522498d82135cd4c1a9823981aeaecac5821501f613c073ef
- evidence_id: S173-E-BEE-MAF
  kind: primary_source
  reference: MTBLS379
  locator: All7916 rows scanned for exact CHEBI133919/name; three dcSTX rows fully
    inspected including chemical representations, MSI:2, retention times, mass/charge
    and20 abundance fields. No re-identification from raw spectra.
  accessed_at: '2026-10-21T20:14:56.963023Z'
  support: supports
  summary: All7916 rows scanned for exact CHEBI133919/name; three dcSTX rows fully
    inspected including chemical representations, MSI:2, retention times, mass/charge
    and20 abundance fields. No re-identification from raw spectra.
  snapshot_sha256: 1aa1e332658f645f21819e9bcec79e91010c7e9273144f5997069265600d103e
- evidence_id: S173-E-BEE-SAMPLES
  kind: primary_source
  reference: MTBLS379
  locator: 'All20 sample rows inspected: brain, Apis cerana, ten mite-infested and
    ten control sample labels.'
  accessed_at: '2026-10-21T20:14:55.001880Z'
  support: supports
  summary: 'All20 sample rows inspected: brain, Apis cerana, ten mite-infested and
    ten control sample labels.'
  snapshot_sha256: be15efba89ba564951c5dfffaaecd9890c8fb45fe38885ab089a5c76566a9ab1
- evidence_id: S173-E-GB-DC
  kind: database
  reference: GenBank:DQ787200.1
  locator: Complete header and all source/gene/CDS annotation fields excluding full
    residue-by-residue translation/base verification.
  accessed_at: '2026-10-21T20:11:33.551861Z'
  support: supports
  summary: Complete header and all source/gene/CDS annotation fields excluding full
    residue-by-residue translation/base verification.
  snapshot_sha256: 69593b08d8951d94764f2884d270f940c30860a9d0e698c77174436b9f67fa05
- evidence_id: C173-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/decarbamoylsaxitoxin.yaml
  locator: Complete owner and all seven matching source-row sets; no referenced components
  accessed_at: '2026-10-21T21:50:32.492703Z'
  support: supports
  summary: 'The complete owner denotes decarbamoylsaxitoxin under CHEBI:133919. All
    source selectors, versions and complete row digests are retained in COMPARISON:
    [{"row_sha256": "f706af2abfa361e9921be0a4d962fe97fad33bc7f816df7bf429732965ff6807",
    "selector": "BGC0000188:3", "version": "5"}]. The official intake and prepared
    owner bytes agree.'
  snapshot_sha256: d9b4ca68866bf479dab3a048ea216f85c309c957742cbd8a213cb6f2d5965ba0
- evidence_id: C173-GRAPH
  kind: validation
  reference: /private/tmp/npm-review-work/173/chemistry.json
  locator: Fresh intake RDKit result and frozen Standard/fixed-H comparison
  accessed_at: '2026-10-21T21:49:35.563093Z'
  support: supports
  summary: The stored SMILES recomputes to VRRIYZJUSNMZMP-PJPYAQQDSA-N, formula C9H16N6O3,
    formal charge 0; stored InChI/key agree. These are representation checks, not
    experimental identity proof.
  snapshot_sha256: 31699f08b84552e0d0b14c9b0500e6332f8619f4a6183f26106f60ae3e541ae9
- evidence_id: C173-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/chemical-comparison.json
  locator: Record 173; exact source rows and each graph comparison
  accessed_at: '2026-10-21T20:15:53.614413Z'
  support: supports
  summary: Exact Standard, fixed-H, formula, charge and stereo comparisons of the
    retained owner, complete raw rows and current authority responses; primary experimental
    proof is assessed separately.
  snapshot_sha256: 941268dc4402c97bfbd9f113317e60aa89a5ecd89e45a4d8f14709827989c49c
- evidence_id: C173-LOCAL-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/173/chemistry-search-receipt.json
  locator: Exact full key, label, slug and source selector in raw/owner/curation trees
  accessed_at: '2026-10-21T21:50:32.707549Z'
  support: supports
  summary: Ignored-inclusive bounded search preserves all matching paths; an absent
    curation decision does not imply a missing scientific source.
  snapshot_sha256: f53d4776baf2a817f0a0b22998bd131cee3f9c2ac4b63670c9af14977281ad98
  search_scope: rg --no-ignore --hidden; data/natural_products, data/raw and curation;
    exact full key, current label, slug and BGC:compound_index. No claim beyond these
    trees.
- evidence_id: C173-CHEBI-SEARCH-1
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=VRRIYZJUSNMZMP-PJPYAQQDSA-N&size=100
  locator: Literal key search; chebi-key-173.json
  accessed_at: '2026-10-21T20:14:39.162533Z'
  support: supports
  summary: 1 returned name/key results; evaluate exact key and stars, not name similarity.
  snapshot_sha256: b79fa079e9972d9ad4019d46b7eccc64e7fb2fffe2716661f3efe1ce42dc9a3f
  search_scope: Official ChEBI es_search bounded key request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C173-CHEBI-SEARCH-2
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=decarbamoylsaxitoxin&size=100
  locator: Literal name search; chebi-name-173.json
  accessed_at: '2026-10-21T20:14:39.159878Z'
  support: supports
  summary: 2 returned name/key results; evaluate exact key and stars, not name similarity.
  snapshot_sha256: 0c9e8553d4ce2fe7d2e2e9e41b6cc60d5d92331139621327014fcc25cf7f4318
  search_scope: Official ChEBI es_search bounded name request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C173-AUTH-1
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0000188.5/annotations.json
  locator: compounds[2].structure; BGC0000188.5.json
  accessed_at: '2026-10-21T20:14:38.613216Z'
  support: supports
  summary: 'current MIBiG BGC0000188:3: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N;
    exact stored Standard key match=True, fixed-H match=True. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: f34f78a039888d795b18aa7e044c0e8504afe7a5008685f0d6651ece0e18f805
- evidence_id: C173-AUTH-2
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/24941628/property/IsomericSMILES,InChI,InChIKey,MolecularFormula/JSON
  locator: PropertyTable.Properties[].SMILES; pubchem-24941628.json
  accessed_at: '2026-10-21T20:14:38.537148Z'
  support: supports
  summary: 'PubChem literal 24941628: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N;
    exact stored Standard key match=True, fixed-H match=True. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: 6c3f3abc87a98a79ded5abbaadd10b59ed6410a56d56782bee23dcf43cebd406
- evidence_id: C173-AUTH-3
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/24941628/SDF?record_type=2d
  locator: first complete SDF; pubchem-24941628.sdf
  accessed_at: '2026-10-21T20:14:38.613733Z'
  support: supports
  summary: 'PubChem SDF literal 24941628: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N;
    exact stored Standard key match=True, fixed-H match=True. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: e13d2f17d1a1117ab03bfb49c91d62b92018635901e5828f01b6e357807a615a
- evidence_id: C173-AUTH-4
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/133919/
  locator: default_structure.smiles; CHEBI133919.json
  accessed_at: '2026-10-21T20:15:26.325280Z'
  support: supports
  summary: 'ChEBI JSON 133919: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N;
    exact stored Standard key match=True, fixed-H match=False. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: 14063521aa687b31270494bfd69c9348297d2d69ae1aa98a3bbdd3e50690c611
- evidence_id: C173-AUTH-5
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/133919/
  locator: official MOL endpoint; CHEBI133919-official.mol
  accessed_at: '2026-10-21T20:15:26.324890Z'
  support: supports
  summary: 'ChEBI MOL 133919: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N;
    exact stored Standard key match=True, fixed-H match=False. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: eb196d75a46c5e9eb0525265af2c316a1b89bcd4751f590358cf1b8158e8f15a
- evidence_id: C173-AUTH-6
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q27277104.json
  locator: P2017; Q27277104.json
  accessed_at: '2026-10-21T20:14:38.799751Z'
  support: supports
  summary: 'Wikidata Q27277104: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N;
    exact stored Standard key match=True, fixed-H match=True. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: 356413e7b4697997e63246f99574ba702de83d82997b05a6d74ad34166cb7fe2
- evidence_id: C173-AUTH-7
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q27277104.json
  locator: P233; Q27277104.json
  accessed_at: '2026-10-21T20:14:38.799751Z'
  support: context_only
  summary: 'Wikidata Q27277104: representation parses=True; parsed key VRRIYZJUSNMZMP-UHFFFAOYSA-N;
    exact stored Standard key match=False, fixed-H match=False. This current database
    representation is not independent primary experimental proof. Canonical P233 is
    not an isomeric stereo assertion; compare P2017 when present.'
  snapshot_sha256: 356413e7b4697997e63246f99574ba702de83d82997b05a6d74ad34166cb7fe2
- evidence_id: C173-AUTH-8
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q27277104.json
  locator: P234 Standard InChI (normalized reconstruction; not a literal fixed-H assertion);
    Q27277104.json
  accessed_at: '2026-10-21T20:14:38.799751Z'
  support: supports
  summary: 'Wikidata Q27277104: representation parses=True; parsed key VRRIYZJUSNMZMP-PJPYAQQDSA-N;
    exact stored Standard key match=True, fixed-H match=False. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: 356413e7b4697997e63246f99574ba702de83d82997b05a6d74ad34166cb7fe2
- evidence_id: C173-CONSUMERS
  kind: record_content
  reference: src/naturalproductmech/curate/structure_corrections.py
  locator: Complete correction consumer and separately pinned selector/collision comparison
  accessed_at: '2026-10-21T21:50:32.492703Z'
  support: supports
  summary: Only REPLACE_WITH_CHEBI and SPLIT_SHARED_WITH_CHEBI are implemented. They
    require a unique structured three-star committed target and complete original/target
    row hashes; arbitrary primary SMILES and label overrides are not accepted. The
    loader copies target SMILES, so valid MOL versus invalid JSON text must be distinguished.
    It clears old xrefs and rebuilds exact-key joins. Existing claim-reference and
    strain consumers reject structure_correction_note; composition needs explicit
    implementation and tests.
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
- evidence_id: C173-XREF-CONSUMER
  kind: record_content
  reference: src/naturalproductmech/curate/xref_exclusions.py
  locator: Complete literal-xref exclusion consumer; pubchem/npatlas namespace and
    full-row guard
  accessed_at: '2026-10-21T21:50:32.492703Z'
  support: supports
  summary: A specific existing literal pubchem or npatlas assertion can be excluded
    under the exact original BGC:compound_index selector and complete row hash. This
    neither installs a positive xref nor migrates biological observations. It rejects
    a structure-corrected row; compatible stacking is not assumed.
  snapshot_sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
- evidence_id: C173-ROUTING
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/grounding-source-selector-routing.json
  locator: Exact scoped calculation; original inputs, version and limitations retained
  accessed_at: '2026-10-21T20:28:14.342897Z'
  support: supports
  summary: Complete source selectors and mints reproduce, each full original row is
    unique, and exact diagnostic alternate keys for171/180 have no committed eligible
    CheBI or MIBiG target in the inspected inventory. Existing-decision absence is
    limited to the two complete maintained TSVs searched ignored-inclusively.
  snapshot_sha256: 1556828e2a4093a2d3efa271b09c9099fb514110ccb29621cffaf855499c072e
- evidence_id: C173-PRIMARY-1983
  kind: primary_source
  reference: DOI:10.1080/00021369.1983.10865612
  locator: Complete original three-page extracted text; NMR/chromatography and carbamoylation
    comparison; retained /private/tmp/npm-review-work/shared-next-batch018/bgc-science/attempt-004/dcstx1983-primary.pdf
  accessed_at: '2026-10-21T20:10:14.512206Z'
  support: supports
  summary: Shellfish toxin was compared with decarbamoylsaxitoxin prepared from saxitoxin
    and chemically converted back to saxitoxin. This supports exact chemical identity
    at the reported comparison scope, not every later taxon occurrence or a new absolute
    re-refinement.
  snapshot_sha256: 8d5f2164091fc1113013e8962e6e76aceaf5d5f5d7f2f21c35122fe439202b7f
- evidence_id: C173-MICROSTATE
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/microstate-comparison-v3.json
  locator: Exact scoped calculation; original inputs, version and limitations retained
  accessed_at: '2026-10-21T20:18:06.746217Z'
  support: supports
  summary: Retained amino/endo-imino and ChEBI diimino forms have the same full Standard
    InChI and stereochemistry, with positive guanidine hydrogen/bond-placement tautomerism
    and different fixed-H forms. The earlier cached legacy CIP discrepancy is explicitly
    superseded; there is no atom 7 enantiomer conflict.
  snapshot_sha256: 93e2be2ab8a1e068caa6ccd48f393630d38a5d9747843c55b2fbe4f2f33ca2e3
- evidence_id: C173-RAW-CHEMSPIDER
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/chemspider94709-raw-source-comparison.json
  locator: Exact scoped calculation; original inputs, version and limitations retained
  accessed_at: '2026-10-21T20:28:14.205359Z'
  support: supports
  summary: Raw-only ChemSpider94709 resolves to IOGRODCJ with one undefined centre,
    not the full PJPYAQQD key. The current seeder excludes the ChemSpider namespace,
    so no emitted xref is affected.
  snapshot_sha256: 17f29f6292966dcb75a8b0ddde7d0379a45982aa5fe79a7b46936adc943cba16
assessments:
- assessment_id: R173-HISTORY
  area: provenance
  topic: Native status and complete audit history
  outcome: supported
  summary: All 2 retained events are SEEDED_FROM_SOURCES. Native status remains SEEDED;
    provenance events are not structured-review passes.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - R173-OWNER
- assessment_id: R173-OPTIONAL
  area: completeness
  topic: Complete optional-assertion inventory
  outcome: supported
  summary: This owner has one imported ChEBI definition; its constitutional and biological
    clauses are present assertions requiring separate chemistry/science support. The
    no-assay-data raw row is not a measured assay, and no pathway, graph, molecular
    target, application, activity summary, relation, discussion or clinical-status
    assertion is present.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - R173-OWNER
  - R173-LOCAL
  - R173-PUBCHEM-PREP
- assessment_id: R173-FILING
  area: representation
  topic: Exact-key computed classification provenance
  outcome: supported
  summary: The exact-key NPClassifier projection and version npclassifier.gnps2.org@2026-09-07
    reproduce the owner filing, superclass/class labels and glycoside value false.
    Computed labels are not independent precursor, mechanism or natural-origin evidence.
    Any accepted new identity requires reclassification for its effective key.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - R173-OWNER
  - R173-LOCAL
- assessment_id: R173-ORGANISM-IDS
  area: grounding
  topic: Literal organism identifier routing
  outcome: supported
  summary: All literal organism-QID routes agree at the inspected P225/P685 scope.
    Occurrence and experimental-unit support remain separate.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - R173-Q133353
  - R173-Q309515
  - R173-Q310362
  - R173-Q5199328
- assessment_id: R173-TAXON-SCOPE
  area: provenance
  topic: Taxonomic names versus experimental stocks
  outcome: supported
  summary: NCBI 398006 is Cylindrospermopsis raciborskii T3 at strain rank under 77022.
    The species response includes Raphidiopsis raciborskii as a synonym while retaining
    Cylindrospermopsis as its primary name. NCBI 467598 Microseira wollei includes
    Lyngbya wollei; 373637 Aulacomya atra lists Aulacomya ater as a misspelling. The
    four cyanobacterial genera, algal species, mollusks, fish and bee identities verify
    only routing; their exact compound/source resolution remains separately assessed.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - R173-TAXON-CONTEXT
  - R173-OWNER
- assessment_id: R173-IMODULON-SCOPE
  area: completeness
  topic: Producer transcriptomic applicability
  outcome: not_applicable
  summary: No exact native producer species/strain dataset is represented in the inspected
    catalogue. Related species and possible experimental hosts do not establish a
    construct/condition match; no gene/module or compound-production inference is
    made.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - R173-OWNER
  - R173-IMODULON
- assessment_id: S173-A-NATIVE
  area: evidence
  topic: biosynthesis_origin and producer_organisms[0]
  outcome: supported
  summary: The full 2008 primary explicitly reports dcSTX in C. raciborskii T3 along
    with other paralytic shellfish toxins. DQ787200.1 independently identifies T3.
    This is a positive culture-level source assertion; the early-intermediate MS experiment
    is not a direct final-dcSTX enzymatic trace.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC2008
  - S173-E-GB-DC
  dimensions:
  - name: native_strain
    value: Cylindrospermopsis raciborskii T3
    definition: Exact reported producer and submitted locus source, distinct from
      other species-level occurrence studies.
    evidence_ids:
    - S173-E-DC2008
    - S173-E-GB-DC
  - name: evidence_tier
    value: SOURCE_ASSERTION / CLUSTER_UNSTATED
    definition: Imported empty methods remain conservative; sequencing/homology does
      not imply knockout.
    evidence_ids:
    - S173-E-LOCAL
    - S173-E-DC2008
- assessment_id: S173-A-LOCUS
  area: provenance
  topic: biosynthetic_gene_clusters[0] and bgc_class
  outcome: supported
  summary: The original 2008 work links the sxt region through genomic annotation
    and measured early intermediates, without a transformation system, exact dcSTX
    knockout or purified final-product reconstitution. Its final paragraph reports
    constitutive sxt RT-PCR expression with data not shown; transcriptional regulation
    remained under study, so this is not expression-linked dcSTX production. SxtL-mediated
    decarbamoylation and a route bypassing SxtI are alternatives, not resolved enzyme
    claims. DQ787200.1 is 37,606 bp, but empty imported locus bounds are not silently
    replaced by the whole submission. OTHER is source class context.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC2008
  - S173-E-GB-DC
  - S173-E-MIBIG-173
- assessment_id: S173-A-DEFINITION
  area: representation
  topic: definition and definition_source
  outcome: supported
  summary: The imported broad toxin, marine-dinoflagellate/cyanobacterial and paralytic-shellfish-poisoning
    context is compatible with the inspected 1983, 2008 and 2010 primary studies.
    The definition does not establish all emitted organism triples, direct biosynthesis
    by seafood consumers or one uniquely resolved dcSTX enzyme route. Exact structural
    nomenclature is separately assessed by chemistry.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC1983
  - S173-E-DC2008
  - S173-E-DC2010
- assessment_id: S173-A-OCC-0
  area: evidence
  topic: occurrences[0] Anabaena
  outcome: unknown
  summary: Original2001abstract reports Anabaena circinalis extracts and radioreceptor-versus-HPLC
    comparisons, with general introductory mention of Anabaena/Aphanizomenon. Exact
    dcSTX/congener-by-strain table and applicability to this particular genus remain
    uninspected because full body was unavailable.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC2001-ABSTRACT
  dimensions:
  - name: occurrence_reference
    value: DOI:10.1021/ES001575Z
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-DC2001-ABSTRACT
- assessment_id: S173-A-OCC-1
  area: evidence
  topic: occurrences[1] Anabaena
  outcome: concern
  summary: Complete1983primary isolates PBT=dcSTX from Spondylus butleri in a Pyrodinium-associated
    outbreak. None of the four cited cyanobacterial genera is its reported sample
    or detected organism; this particular taxon-reference triple is not supported
    by the inspected full study.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC1983
  dimensions:
  - name: occurrence_reference
    value: DOI:10.1080/00021369.1983.10865612
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-DC1983
- assessment_id: S173-A-OCC-2
  area: evidence
  topic: occurrences[2] Aphanizomenon
  outcome: unknown
  summary: Original2001abstract reports Anabaena circinalis extracts and radioreceptor-versus-HPLC
    comparisons, with general introductory mention of Anabaena/Aphanizomenon. Exact
    dcSTX/congener-by-strain table and applicability to this particular genus remain
    uninspected because full body was unavailable.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC2001-ABSTRACT
  dimensions:
  - name: occurrence_reference
    value: DOI:10.1021/ES001575Z
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-DC2001-ABSTRACT
- assessment_id: S173-A-OCC-3
  area: evidence
  topic: occurrences[3] Aphanizomenon
  outcome: concern
  summary: Complete1983primary isolates PBT=dcSTX from Spondylus butleri in a Pyrodinium-associated
    outbreak. None of the four cited cyanobacterial genera is its reported sample
    or detected organism; this particular taxon-reference triple is not supported
    by the inspected full study.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC1983
  dimensions:
  - name: occurrence_reference
    value: DOI:10.1080/00021369.1983.10865612
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-DC1983
- assessment_id: S173-A-OCC-4
  area: evidence
  topic: occurrences[4] Pao turgidus
  outcome: supported
  summary: Originalabstract positively reports wild Tetraodon turgidus STX/dcSTX and
    separate experimentally injected cultured-fish accumulation. It explicitly argues
    exogenous origin; occurrence is not autonomous fish biosynthesis.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-PUBMED
  dimensions:
  - name: occurrence_reference
    value: PMID:17996918
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-PUBMED
- assessment_id: S173-A-OCC-5
  area: evidence
  topic: occurrences[5] Lyngbya
  outcome: unknown
  summary: Original2001abstract reports Anabaena circinalis extracts and radioreceptor-versus-HPLC
    comparisons, with general introductory mention of Anabaena/Aphanizomenon. Exact
    dcSTX/congener-by-strain table and applicability to this particular genus remain
    uninspected because full body was unavailable.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC2001-ABSTRACT
  dimensions:
  - name: occurrence_reference
    value: DOI:10.1021/ES001575Z
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-DC2001-ABSTRACT
- assessment_id: S173-A-OCC-6
  area: evidence
  topic: occurrences[6] Lyngbya
  outcome: concern
  summary: Complete1983primary isolates PBT=dcSTX from Spondylus butleri in a Pyrodinium-associated
    outbreak. None of the four cited cyanobacterial genera is its reported sample
    or detected organism; this particular taxon-reference triple is not supported
    by the inspected full study.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC1983
  dimensions:
  - name: occurrence_reference
    value: DOI:10.1080/00021369.1983.10865612
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-DC1983
- assessment_id: S173-A-OCC-7
  area: evidence
  topic: occurrences[7] Alexandrium tamarense
  outcome: unknown
  summary: 'Originalabstract distinguishes seven analytical toxins including dcSTX
    from the tested algae: HK9301 has GTX2/GTX3, CI01 no detected PST. It does not
    establish exact dcSTX in either tested extract. Full body remains unavailable,
    so do not claim an exhaustive study-wide absence beyond this explicit abstract
    result.'
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-PUBMED
  dimensions:
  - name: occurrence_reference
    value: PMID:16544882
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-PUBMED
- assessment_id: S173-A-OCC-8
  area: evidence
  topic: occurrences[8] Aulacomya ater
  outcome: unknown
  summary: Originalabstract detects dcSTX as a human liver/kidney/lung metabolic product
    after an Aulacomya meal. Whether the consumed mussel itself contained dcSTX needs
    the uninspected source table. Public institutional PDF lead returned a challenge
    page, not the paper.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-PUBMED
  dimensions:
  - name: occurrence_reference
    value: PMID:15019474
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-PUBMED
- assessment_id: S173-A-OCC-9
  area: evidence
  topic: occurrences[9] Acanthocardia tuberculata
  outcome: unknown
  summary: Originalabstract concerns PST quantification in mussels/cockles and an
    interfering peak near dcSTX. It does not establish an exact dcSTX-positive Acanthocardia
    sample; detailed source table remains unavailable.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-PUBMED
  dimensions:
  - name: occurrence_reference
    value: PMID:16192070
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-PUBMED
- assessment_id: S173-A-OCC-10
  area: evidence
  topic: occurrences[10] Gymnodinium catenatum
  outcome: unknown
  summary: Originalabstract isolates GC1/2/3; GC3 is a4-hydroxybenzoate ester derivative
    of dcSTX. Ester identification does not by itself prove free dcSTX occurrence.
    Full experimental body remains unavailable.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-PUBMED
  dimensions:
  - name: occurrence_reference
    value: PMID:12924931
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-PUBMED
- assessment_id: S173-A-OCC-11
  area: evidence
  topic: occurrences[11] Microseira wollei
  outcome: concern
  summary: Originalabstract explicitly shows hydrochloric-acid extraction converts
    L.wollei toxins into dcSTX/dcGTX2/3, whereas0.1M acetic acid preserves the original
    profile. Preserve extraction-product scope, not an unsupported claim that every
    native mat contains free dcSTX.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-PUBMED
  dimensions:
  - name: occurrence_reference
    value: PMID:22960450
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-PUBMED
- assessment_id: S173-A-OCC-12
  area: evidence
  topic: occurrences[12] Aphanizomenon gracile
  outcome: supported
  summary: Full2010primary confirms exact dcSTX by LC-MS against standards in all14
    A.gracile strains; it constitutes0.7–14.3% of quantified PSP toxin profile, with
    strain-specific proportions. Toxin-gene presence in additional nontoxic strains
    is separately described.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC2010
  dimensions:
  - name: occurrence_reference
    value: PMID:20048055
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-DC2010
- assessment_id: S173-A-OCC-13
  area: evidence
  topic: occurrences[13] Apis cerana
  outcome: concern
  summary: Official current MAF has three exact dcSTX-labelled feature rows1379/1658/5760,
    allMSI:2, with nonzero values in20brain samples. Two structure representations
    omit stereo; the third has exact isomeric InChI. These support an explicit putative
    annotation, not authentic-standard identification or bee biosynthesis.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-BEE-MAF
  - S173-E-BEE-SAMPLES
  - S173-E-BEE-STUDY
  - S173-E-BEE2017
  dimensions:
  - name: occurrence_reference
    value: MTBLS379
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-BEE-MAF
    - S173-E-BEE-SAMPLES
    - S173-E-BEE-STUDY
    - S173-E-BEE2017
- assessment_id: S173-A-OCC-14
  area: evidence
  topic: occurrences[14] Cylindrospermopsis
  outcome: unknown
  summary: Original2001abstract reports Anabaena circinalis extracts and radioreceptor-versus-HPLC
    comparisons, with general introductory mention of Anabaena/Aphanizomenon. Exact
    dcSTX/congener-by-strain table and applicability to this particular genus remain
    uninspected because full body was unavailable.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC2001-ABSTRACT
  dimensions:
  - name: occurrence_reference
    value: DOI:10.1021/ES001575Z
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-DC2001-ABSTRACT
- assessment_id: S173-A-OCC-15
  area: evidence
  topic: occurrences[15] Cylindrospermopsis
  outcome: concern
  summary: Complete1983primary isolates PBT=dcSTX from Spondylus butleri in a Pyrodinium-associated
    outbreak. None of the four cited cyanobacterial genera is its reported sample
    or detected organism; this particular taxon-reference triple is not supported
    by the inspected full study.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC1983
  dimensions:
  - name: occurrence_reference
    value: DOI:10.1080/00021369.1983.10865612
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-DC1983
- assessment_id: S173-A-OCC-16
  area: evidence
  topic: occurrences[16] Cylindrospermopsis raciborskii
  outcome: supported
  summary: Originalabstract explicitly reports dcSTX by LC-fluorescence in the Brazilian
    C.raciborskii strain. French/Australian and other strain phenotypes are separate;
    full strain designation/experimental conditions are not inspected.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-PUBMED
  dimensions:
  - name: occurrence_reference
    value: PMID:12740803
    definition: Literal source assertion; organism occurrence is not a biosynthetic
      claim.
    evidence_ids:
    - S173-E-PUBMED
- assessment_id: S173-A-OPTIONAL
  area: evidence
  topic: Absent pathways, graph and bioactivity observations
  outcome: not_applicable
  summary: No mechanism or assay is emitted, and the sole matching PubChem inventory
    row says no assay data. Proposed sxt chemistry and physiological toxin effects
    do not create an obligation to add an unverified exact-enzyme mechanism.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC2008
- assessment_id: C173-A-IDENTITY
  area: identity
  topic: Stored representation and source-concept provenance
  outcome: supported
  summary: The complete source row BGC0000188:3 and source-concept hash reproduce
    this stored representation; this does not establish that the upstream compound
    label is correct. Formula, charge, Standard and fixed-H distinctions are independently
    recorded. Primary support and any conflicting exact xref are assessed separately.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - C173-OWNER
  - C173-GRAPH
  - C173-COMPARISON
  dimensions:
  - name: mibig_source_selector
    value: BGC0000188:3
    definition: Accession plus compound_index, distinct from the entry-level accession.
    evidence_ids:
    - C173-OWNER
  - name: complete_raw_row_sha256
    value: f706af2abfa361e9921be0a4d962fe97fad33bc7f816df7bf429732965ff6807
    definition: Sorted compact ASCII JSON of every parsed TSV field, including empty
      values.
    evidence_ids:
    - C173-OWNER
- assessment_id: C173-A-GROUNDING
  area: provenance
  topic: Exact authority eligibility and source representation
  outcome: supported
  summary: Exactly one committed three-star default ChEBI row matches; its current
    graph is checked separately.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - C173-OWNER
  - C173-COMPARISON
  - C173-LOCAL-SEARCH
  - C173-CHEBI-SEARCH-1
  - C173-CHEBI-SEARCH-2
- assessment_id: C173-A-XREF
  area: representation
  topic: Literal identifiers, namespaces and exact microstates
  outcome: supported
  summary: 'Stored literals were requested exactly and compared in their returned
    namespaces: [{"formula": "C9H16N6O3", "literal": "pubchem:24941628", "returned_key":
    "VRRIYZJUSNMZMP-PJPYAQQDSA-N", "same_fixed_h": true, "same_standard": true}].
    Standard equality does not imply literal fixed-H equality. Current authority agreement
    is not independent primary proof. Canonical Wikidata P233 is not an assertion
    of the isomeric hand.'
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - C173-COMPARISON
  - C173-AUTH-1
  - C173-AUTH-2
  - C173-AUTH-3
  - C173-AUTH-4
  - C173-AUTH-5
  - C173-AUTH-6
  - C173-AUTH-7
  - C173-AUTH-8
- assessment_id: C173-A-CHEBI-ELIGIBILITY
  area: grounding
  topic: Exact three-star projection and source concept
  outcome: supported
  summary: CHEBI:133919 is the unique committed eligible three-star Standard-key match;
    its tautomeric fixed-H distinction is retained.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - C173-OWNER
  - C173-COMPARISON
  - C173-ROUTING
  - C173-AUTH-1
  - C173-AUTH-2
  - C173-AUTH-3
  - C173-AUTH-4
  - C173-AUTH-5
  - C173-AUTH-6
  - C173-AUTH-7
  - C173-AUTH-8
- assessment_id: C173-A-RAW-NAMESPACE
  area: provenance
  topic: Unemitted raw ChemSpider assertion
  outcome: supported
  summary: The exact raw ChemSpider mismatch is retained for source audit, without
    inventing an owner xref or proposing removal of an already excluded namespace.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - C173-PRIMARY-1983
  - C173-MICROSTATE
  - C173-RAW-CHEMSPIDER
  - C173-OWNER
- assessment_id: C173-A-PRIMARY-SCOPE
  area: scope
  topic: Primary chemical support and retained precision
  outcome: supported
  summary: The original 1983 three-page paper identifies paralytic shellfish toxin
    from Spondylus butleri by NMR, chromatography/electrophoresis comparison to decarbamoylsaxitoxin
    prepared from saxitoxin, and carbamoylation back to saxitoxin. The source provides
    a chemical identity bridge, not evidence for every later organism occurrence.
    The present comparison does not independently redetermine all absolute stereocentres.
    The retained amino/endo-imino form and ChEBI diimino form have identical full
    Standard InChI, formula, charge and stereochemistry, with a positive guanidine
    proton/bond-placement tautomer relationship but different fixed-H InChI. Do not
    call this constitutional or enantiomeric disagreement. The legacy-CIP diagnostic
    error is corrected explicitly in v3.
  target_ids:
  - CHEBI:133919
  evidence_ids:
  - C173-PRIMARY-1983
  - C173-MICROSTATE
  - C173-RAW-CHEMSPIDER
  - C173-OWNER
  - C173-COMPARISON
findings:
- finding_id: S173-F-LOTUS1983
  issue_key: lotus-dcstx-1983-four-cyanobacterial-misattributions
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Four organism occurrences cite an original study of a different sample
  description: The inspected 1983 study characterizes dcSTX in Spondylus butleri from
    a Pyrodinium-associated outbreak, whereas four emitted LOTUS triples attach that
    paper to cyanobacterial genera absent from the study. This is a source-specific
    citation error, not evidence that those genera can never contain dcSTX.
  target_ids:
  - CHEBI:133919
  field_paths:
  - occurrences[1]
  - occurrences[3]
  - occurrences[6]
  - occurrences[15]
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-DC1983
  - S173-E-CONSUMERS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Immutable exact source triples
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Existing full-row-guarded exclusion table
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/lotus_exclusions.py
    role: Unique triple and digest consumer
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Exclusion before occurrence rendering and discussion provenance
- finding_id: S173-F-CONTEXT
  issue_key: chebi-133919-source-specific-detection-context
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Two occurrence assertions omit decisive analytical context
  description: MTBLS379 reports putatively annotated MSI:2 bee-brain features, while
    PMID22960450 explicitly reports dcSTX formation during hydrochloric-acid extraction
    of Lyngbya/Microseira material. The current generic database occurrence wording
    preserves positive source associations but hides these limitations; neither source
    should be promoted to authentic-standard native free-toxin proof.
  target_ids:
  - CHEBI:133919
  field_paths:
  - occurrences[11].evidence
  - occurrences[11].detection_context
  - occurrences[13].evidence
  - occurrences[13].detection_context
  evidence_ids:
  - S173-E-LOCAL
  - S173-E-BEE-MAF
  - S173-E-BEE-SAMPLES
  - S173-E-BEE-STUDY
  - S173-E-BEE2017
  - S173-E-PUBMED
  - S173-E-CONSUMERS
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Immutable origin rows and original bibliography
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Current unconditional ChEBI-origin rendering; new typed qualification hook
      required
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/schema/naturalproductmech.yaml
    role: Existing occurrence evidence/notes and detection_context representation
actions:
- action_id: S173-ACT-LOTUS1983
  finding_ids:
  - S173-F-LOTUS1983
  target_ids:
  - CHEBI:133919
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Immutable exact source triples
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Existing full-row-guarded exclusion table
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/lotus_exclusions.py
    role: Unique triple and digest consumer
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Exclusion before occurrence rendering and discussion provenance
  description: 'Use the existing curation/lotus_occurrence_exclusions.tsv contract
    for exactly these four unique triples: complete raw row {"organism_name": "Anabaena",
    "organism_wikidata": "http://www.wikidata.org/entity/Q133353", "reference_doi":
    "10.1080/00021369.1983.10865612", "standard_inchi_key": "VRRIYZJUSNMZMP-PJPYAQQDSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27277104", "taxon_id":
    "NCBITaxon:1163"}; expected_source_row_sha256=ca1511af57f882aa25f14fe389e8166df034f86b673980dac2688f2cda13a3c5
    | complete raw row {"organism_name": "Aphanizomenon", "organism_wikidata": "http://www.wikidata.org/entity/Q309515",
    "reference_doi": "10.1080/00021369.1983.10865612", "standard_inchi_key": "VRRIYZJUSNMZMP-PJPYAQQDSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27277104", "taxon_id":
    "NCBITaxon:1175"}; expected_source_row_sha256=d524cf16947a87716e598b74d04afb02ca78d35bb9f9c197ca4e195a9f4a3686
    | complete raw row {"organism_name": "Lyngbya", "organism_wikidata": "http://www.wikidata.org/entity/Q310362",
    "reference_doi": "10.1080/00021369.1983.10865612", "standard_inchi_key": "VRRIYZJUSNMZMP-PJPYAQQDSA-N",
    "structure_wikidata": "http://www.wikidata.org/entity/Q27277104", "taxon_id":
    "NCBITaxon:28073"}; expected_source_row_sha256=4011e192dec93f155d04d1622d5e83e9f7e8d600ff35ad8e395951e14d2e8904
    | complete raw row {"organism_name": "Cylindrospermopsis", "organism_wikidata":
    "http://www.wikidata.org/entity/Q5199328", "reference_doi": "10.1080/00021369.1983.10865612",
    "standard_inchi_key": "VRRIYZJUSNMZMP-PJPYAQQDSA-N", "structure_wikidata": "http://www.wikidata.org/entity/Q27277104",
    "taxon_id": "NCBITaxon:77021"}; expected_source_row_sha256=355d90374204f4af5c8196fc602f9a98cf08b36ab9d024905d82842531914ccd.
    Set reference=DOI:10.1080/00021369.1983.10865612 with curator/date and the sample-specific
    rationale. The consumer keeps raw inventories unchanged and emits exclusion provenance.
    Do not alter the four separate 2001 triples or other ChEBI occurrences, and do
    not automatically replace the taxa with Spondylus/Pyrodinium without independently
    keyed source rows and structural adjudication.'
  acceptance_checks:
  - Exactly four literal key/taxon/DOI selectors and complete row hashes match uniquely;
    any source drift or duplicate fails.
  - All other occurrence references and the positive T3 producer/locus remain unchanged.
  - Regenerated occurrence list omits only the unsupported triples and retains the
    consumed exclusion discussion; normal strict/reference/history checks pass.
- action_id: S173-ACT-CONTEXT
  finding_ids:
  - S173-F-CONTEXT
  target_ids:
  - CHEBI:133919
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_origins.tsv
    role: Immutable origin rows and original bibliography
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Current unconditional ChEBI-origin rendering; new typed qualification hook
      required
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/schema/naturalproductmech.yaml
    role: Existing occurrence evidence/notes and detection_context representation
  description: 'Implement a tested typed origin-context consumer, keyed to each complete
    ChEBI origin row with SHA256, because the inspected seeder has no consumed exact-row
    origin qualification table. Guard complete raw row {"chebi_id": "CHEBI:133919",
    "comments": "", "component_text": "", "source_accession": "MTBLS379", "species_accession":
    "7461", "species_text": "Apis cerana", "strain_text": ""}; expected_source_row_sha256=a88667777bb5dfce1ce7482c567a6cd29ccab03fb0c4b66a99a09b7c477bf8a4
    | complete raw row {"chebi_id": "CHEBI:133919", "comments": "", "component_text":
    "", "source_accession": "22960450", "species_accession": "467598", "species_text":
    "Microseira wollei", "strain_text": ""}; expected_source_row_sha256=2d30a2b950246d1b074b0044186d1f77ca6a6283ecb171510bed744437367e5c.
    Preserve the occurrence source assertion, original reference and raw bytes. Add
    MSI:2 putative brain-feature annotation for MTBLS379, and source-reported hydrochloric-acid
    conversion for PMID22960450, with explicit reference and curator attribution.
    Do not infer a concentration, an adduct, bee biosynthesis, universal natural absence,
    or automatic taxon replacement. The latter study body remains a required gap;
    its directly stated abstract conversion is the bounded qualifier.'
  acceptance_checks:
  - Complete raw-row digest and origin identifiers reject drift, ambiguity and conflicting
    qualifications.
  - Qualification is attached only to the two source observations, without changing
    exact chemical identity or treating feature intensities as concentrations.
  - The new consumer is explicitly tested; no raw-field or generated-YAML hand edit
    substitutes for a maintained route.
limitations:
- The root section inventories present claims and source routing; chemical identities,
  source-specific experiments, definition claims and optional-content assertions require
  their separately scoped scientific assessments.
- Original retrieval times and immutable source snapshots are reused; authoring time
  is not represented as new source access.
- Exact chemical identity/authority repairs and general taxonomic/classification/history
  checks are independently assessed. Any combined biological and chemical correction
  must explicitly adjudicate old-key associations and consumer composition.
- Authority matches establish the representations actually returned at their retained
  access times; they are not independent experimental structure or absolute-hand determinations.
  Root and science sections separately assess organism, locus, classification and
  history claims.
- The retained amino/endo-imino form and ChEBI diimino form have identical full Standard
  InChI, formula, charge and stereochemistry, with a positive guanidine proton/bond-placement
  tautomer relationship but different fixed-H InChI. Do not call this constitutional
  or enantiomeric disagreement. The legacy-CIP diagnostic error is corrected explicitly
  in v3.
- The reproduction report retains 42 withheld ambiguous producer claims, 161 merged-taxon
  rewrites and five unresolved assay-organism targets.
- 499 identifier-label plausibility warnings are non-blocking; 4750 pairs have no
  configured adapter and were skipped.
- Four tests were skipped and two dependency deprecation warnings remain. Passing
  configured QC is not independent scientific verification.
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
tags:
- path-order-campaign
- batch-018
```
