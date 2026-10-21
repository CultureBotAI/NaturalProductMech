# Diazaquinomycin E: original methyl group missing from the retained structure

- Review: 20261021T215706Z-diazaquinomycin-e
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T21:49:55.297806Z
- Finished UTC: 2026-10-21T21:57:06.369767Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The original 2014 article identifies native F001 diazaquinomycin E as C23H28N2O4 with one alpha methyl group and two pentyl chains. The retained C22H26N2O4 structure omits that methyl, creating a confirmed constitutional error also present in its PubChem cross-reference. The completed review requires a guarded structure correction and separate adjudication of affected source joins, while preserving the positive named-E isolation evidence.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 180, batch 018, selected in path order from the fresh-main authoritative validated catalogue and the separately validated targets in earlier batch commits (publication tracked separately). At selection, 224 of 3116 current records had campaign coverage and 2892 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-c12262ec06 | data/natural_products/alkaloids/diazaquinomycin-e.yaml | generated | diazaquinomycin E |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-c12262ec06 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-c12262ec06 | All 3116 corpus records are filed exactly where PATHS.tsv pins them. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-c12262ec06 | All 3116 records reproduce byte-for-byte from data/raw/. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-c12262ec06 | The canonical review-queue command completed with actual exit0 on the fresh main base; exact output, warnings and skips remain in the pinned transcript. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-c12262ec06 | Configured identifier-label validation exited zero: 13449 canonical matches, 646 synonym matches and 35 configured exceptions; 499 non-blocking warnings and 4750 no-adapter skips remain. |
| Full repository quality gate on the fresh main baseline | passed | True | naturalproductmech:mibig-c12262ec06 | Full fresh-base quality command completed successfully:999 tests passed,4 skipped,2 warnings;3116 records passed closed schema validation and corpus reproduction, and generated pages were current. |
| Complete owner and captured-source scope | passed | True | naturalproductmech:mibig-c12262ec06 | Successful official intake and a fresh root full-owner/read receipt precede this authoring. All six officially captured sets and the separately mechanically parsed seventh PubChem set match. All matching raw rows and 12 written diazaquinomycin A observations were read by root; primary assay interpretation remains separately scoped. No BindingDB or graph assertion is present. The external component set is empty. |
| Named native isolation and assay context | passed | True | naturalproductmech:mibig-c12262ec06 | Original main and official SI support the exact named compound and experimental endpoint; F/G cocrystal evidence is not transferred to A/E. |
| Stored chemical representation and complete source row | passed | True | naturalproductmech:mibig-c12262ec06 | Fresh intake derivation agrees with the stored graph; the source selector, full row and prepared snapshot were independently rechecked. |
| Literal identifier resolution and parsed representation | passed | True | naturalproductmech:mibig-c12262ec06 | Every present literal was resolved; differing Standard/fixed-H, charge or precision is assessed separately. For invalid default ChEBI JSON SMILES, the independently fetched official MOL supplies the parsed comparison. |
| Exact primary E constitution | failed | True | naturalproductmech:mibig-c12262ec06 | The original compound1 contains an additional methyl absent from the current MIBiG/PubChem graph. This is direct primary constitutional disagreement. |

## Scientific And Domain Assessments

### Native status and complete audit history

provenance: supported. Targets: naturalproductmech:mibig-c12262ec06.

All 2 retained events are SEEDED_FROM_SOURCES. Native status remains SEEDED; provenance events are not structured-review passes.

### Complete optional-assertion inventory

completeness: not_applicable. Targets: naturalproductmech:mibig-c12262ec06.

No optional definition, pathway, graph, target, assay, application, summary, relation, discussion or clinical-status assertion is present. Optional enrichment is separate from checking existing source claims.

### Exact-key computed classification provenance

representation: supported. Targets: naturalproductmech:mibig-c12262ec06.

The exact-key NPClassifier projection and version npclassifier.gnps2.org@2026-09-07 reproduce the owner filing, superclass/class labels and glycoside value false. Computed labels are not independent precursor, mechanism or natural-origin evidence. Any accepted new identity requires reclassification for its effective key.

### Literal organism identifier routing

grounding: supported. Targets: naturalproductmech:mibig-c12262ec06.

All literal organism-QID routes agree at the inspected P225/P685 scope. Occurrence and experimental-unit support remain separate.

### Taxonomic names versus experimental stocks

provenance: supported. Targets: naturalproductmech:mibig-c12262ec06.

NCBI 1510026 Streptomyces sp. F001 is species rank under unclassified Streptomyces, despite its stock-like label. NCBI 1883 is genus Streptomyces. Neither identifier alone validates a specific genomic locus or equates historical producing cultures.

### Producer transcriptomic applicability

completeness: not_applicable. Targets: naturalproductmech:mibig-c12262ec06.

No exact native producer species/strain dataset is represented in the inspected catalogue. Related species and possible experimental hosts do not establish a construct/condition match; no gene/module or compound-production inference is made.

### Exact native strain, isolation and locus evidence

evidence: supported. Targets: naturalproductmech:mibig-c12262ec06.

The 2014 study isolates named E (1) from Streptomyces sp. F001. Its marine sediment source and current exact accession agree at source-metadata scope. No genetic manipulation of this locus is reported in the complete isolation paper, so the empty methods and source-tier biological assertion are not upgraded from annotation.

### Named E biological evidence versus retained graph

identity: concern. Targets: naturalproductmech:mibig-c12262ec06.

Original E1 has C23H28N2O4 with one alpha methyl and two pentyl chains; the retained C22 graph lacks that methyl. Native isolation and LC50 9.0 µM are positive for the original drawn E, not automatically for the current graph. Independent chemistry owns this identity finding and its guarded repair; no duplicate chemical action is created in this science packet.

### Single 2014 genus-level occurrence

scope: supported. Targets: naturalproductmech:mibig-c12262ec06.

The cited publication positively isolates named E from F001. Its coarse Streptomyces assertion is supported for that source concept, subject to resolving the exact graph; it is not a separate producer-grade or sequence experiment.

### Conditional biological joins after identity repair

ownership: not_applicable. Targets: naturalproductmech:mibig-c12262ec06.

Preserve the exact original source BGC0001850:2 and full SHA 84e71f90e7c50894f10046bfb1b87a62a0f490dc9cb3635bc70e5ba29346d6e4. Any new primary-graph consumer must explicitly decide old-key occurrence/xref/classification admission and preserve raw provenance. Current strain/reference consumers reject structure_correction_note; merely updating their hashes is insufficient if those overlays are added. No BGC method enrichment is warranted from this isolation source.

### Stored representation and source-concept provenance

identity: supported. Targets: naturalproductmech:mibig-c12262ec06.

The complete source row BGC0001850:2 and source-concept hash reproduce this stored representation; this does not establish that the upstream compound label is correct. Formula, charge, Standard and fixed-H distinctions are independently recorded. Primary support and any conflicting exact xref are assessed separately.

### Exact authority eligibility and source representation

provenance: supported. Targets: naturalproductmech:mibig-c12262ec06.

No exact eligible row exists in the committed ChEBI projection for this owner. Current bounded name/key searches do not justify a different congener or a two-star grounding.

### Literal identifiers, namespaces and exact microstates

representation: supported. Targets: naturalproductmech:mibig-c12262ec06.

Stored literals were requested exactly and compared in their returned namespaces: [{"formula": "C22H26N2O4", "literal": "pubchem:134814868", "returned_key": "JTXSSZYKSHIXRS-UHFFFAOYSA-N", "same_fixed_h": true, "same_standard": true}]. Standard equality does not imply literal fixed-H equality. Current authority agreement is not independent primary proof. Canonical Wikidata P233 is not an assertion of the isomeric hand.

### Exact three-star projection and source concept

grounding: supported. Targets: naturalproductmech:mibig-c12262ec06.

No eligible exact committed ChEBI row matches this owner. Current two-star entries remain ineligible for asserted grounding/classification and the implemented structure-replacement target contract.

### Primary chemical support and retained precision

scope: concern. Targets: naturalproductmech:mibig-c12262ec06.

The original 2014 main and Figure 1 compound 1 explicitly give asymmetric diazaquinomycin E with one C3–C11 methyl and two pentyl chains, C23H28N2O4. Independent numbered transcription gives XRVKCURQKFTZGG-UHFFFAOYSA-N. The retained C22H26N2O4 graph lacks that methyl and is a different constitution. This is direct primary constitution evidence, not an authority vote. The original F/G co-crystal does not determine E. The source reports its mass values as published; no forced agreement is imposed. No complete record replacement or old-key biological/occurrence migration is authorized by this source packet.

## Findings

### C180-F-METHYL: The retained E graph omits the original product’s methyl group

blocker / open / confirmed; issue key: mibig-bgc0001850-compound2-diazaquinomycin-e-missing-methyl.

The independently transcribed original E1 is asymmetric C23H28N2O4 with one C3–C11 methyl and two pentyl groups; the retained symmetric C22 graph omits that methyl. Its current PubChem literal shares the same defect relative to the source product.

## Recommended Actions And Acceptance Checks

### C180-ACTION-METHYL

Exact original guards: [{"entry_version": "4", "expected_source_row_sha256": "84e71f90e7c50894f10046bfb1b87a62a0f490dc9cb3635bc70e5ba29346d6e4", "old_compound_name": "diazaquinomycin E", "old_database_ids": "pubchem:134814868", "old_key": "JTXSSZYKSHIXRS-UHFFFAOYSA-N", "old_smiles": "CCCCCC1=CC(=O)NC2=C1C(=O)C3=C(C2=O)NC(=O)C=C3CCCCC", "old_standard_inchi": "InChI=1S/C22H26N2O4/c1-3-5-7-9-13-11-15(25)23-19-17(13)21(27)18-14(10-8-6-4-2)12-16(26)24-20(18)22(19)28/h11-12H,3-10H2,1-2H3,(H,23,25)(H,24,26)", "old_stereo_complete": "true", "source_id": "BGC0001850:2"}]. Adjudicate the complete primary achiral E graph XRVKCURQKFTZGG-UHFFFAOYSA-N and all exact source joins. CHEBI222154 MOL agrees but is only 2-star, and its default JSON SMILES is invalid; it is not an eligible current REPLACE_WITH_CHEBI target. A reviewed primary-graph consumer with exact original/candidate hashes, formula/valence/Standard/fixed-H checks and collision guards is required if adopted. Do not simply substitute the invalid JSON or keep PubChem134814868 as an exact corrected xref. Preserve native F001 isolation at the actual named-E graph resolution and adjudicate its old-key occurrence independently. Preserve the complete raw source row and original source mint. Any graph correction must independently adjudicate old-key LOTUS triples, assays, external identifiers, eligible ChEBI joins and filing/classification; no old-key data is automatically transferred. Any required strain/reference overlay composition must be implemented and tested because current consumers reject structure_correction_note. Preserve positive biological source claims at their demonstrated congener/resolution.

- Missing, duplicate or changed original rows and stale full-row hashes fail closed.
- Candidate chemistry and any introduced target row are parsed and compared in Standard and fixed-H form, including all defined/undefined centres and alkene geometry; invalid default SMILES is not copied.
- No source occurrence, assay, identifier or biological claim is migrated by name or authority majority.
- Every adopted overlay and any required new composition path has focused consumed-route/regeneration tests and the normal strict/reference/history checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R180-OWNER | data/natural_products/alkaloids/diazaquinomycin-e.yaml; Complete post-intake owner, optional assertions and all history events | supports | Root read the complete owner after successful official intake: 1 occurrence, 1 producer and 1 locus assertions. No referenced external component is present. Optional fields: none. |
| R180-LOCAL | /private/tmp/npm-review-work/180/local-sources.json; Complete resolved owner and all six officially captured raw row sets | context_only | All six captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB and NPClassifier sets match the frozen preparation, including empty sets. The separate seventh PubChem inventory comparison is distinguished below. Source fidelity does not itself establish experimental support. |
| R180-PUBCHEM-PREP | data/raw/pubchem_bioassay.tsv; Exact-key rows compared with the separate provisional seventh source set | context_only | The separate committed PubChem raw set contains 0 matching rows and reproduces the frozen preparation. This is not part of the official six-set intake. All matching rows were read by root; the 12 diazaquinomycin A observations are the only emitted assays. The separately prepared assay packet owns exact endpoint/call interpretation. Empty/no-assay-data rows elsewhere are not tested outcomes. |
| R180-Q1144013 | https://www.wikidata.org/wiki/Q1144013; P225 and P685 in the retained complete nine-entity response | context_only | Literal scientific name and NCBI taxon identifier agree with the matched source rows. Identifier routing does not establish occurrence chemistry, producing stock or experiment. |
| R180-TAXON-CONTEXT | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;retmode=xml&amp;id=112125,1163,1175,1220761,1427518,1510026,176275,1873482,1883,1956,28073,2926,344612,373637,38033,385555,39447,398006,467598,500485,54296,571,7461,77021,77022; Exact relevant TaxId, ScientificName, Rank, ParentTaxId and OtherNames fields | context_only | NCBI 1510026 Streptomyces sp. F001 is species rank under unclassified Streptomyces, despite its stock-like label. NCBI 1883 is genus Streptomyces. Neither identifier alone validates a specific genomic locus or equates historical producing cultures. |
| R180-IMODULON | https://imodulondb.org/api/datasets; Complete 20-organism, 28-dataset official catalogue | context_only | The full retained catalogue establishes membership only. None of these exact native producer labels occurs in it. Listed S. albidoflavus, S. coelicolor or E. coli datasets do not establish an exact native producer/strain, introduced construct or relevant experimental condition for these owners. |
| S180-E-LOCAL | /private/tmp/npm-review-work/180/local-sources.json; Whole owner, all assertions and components; seven exact source sets | context_only | The entire actual owner and six captured source sets match the frozen inventory; the seventh PubChem set was independently reconciled against the full raw TSV. |
| S180-E-RAW | data/raw/mibig_compounds.tsv; {"bgc_classes": "other", "bgc_subclasses": "shikimate-derived", "cluster_link_evidence_basis": "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "2", "compound_name": "diazaquinomycin E", "database_ids": "pubchem:134814868", "entry_completeness": "complete", "entry_quality": "questionable", "entry_status": "active", "entry_version": "4", "genome_accession": "QZWF01000007.1", "locus_evidence_methods": "", "locus_from": "257859", "locus_to": "281361", "mibig_accession": "BGC0001850", "primary_reference": "DOI:10.3390/md12063574", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis": "ENTRY", "smiles": "CCCCCC1=CC(=O)NC2=C1C(=O)C3=C(C2=O)NC(=O)C=C3CCCCC", "standard_inchi": "InChI=1S/C22H26N2O4/c1-3-5-7-9-13-11-15(25)23-19-17(13)21(27)18-14(10-8-6-4-2)12-16(26)24-20(18)22(19)28/h11-12H,3-10H2,1-2H3,(H,23,25)(H,24,26)", "standard_inchi_key": "JTXSSZYKSHIXRS-UHFFFAOYSA-N", "stereo_complete": "true", "taxon_id": "NCBITaxon:1510026", "taxon_label": "Streptomyces sp. F001"} | context_only | Exact immutable source selector BGC0001850:2; expected_source_row_sha256=84e71f90e7c50894f10046bfb1b87a62a0f490dc9cb3635bc70e5ba29346d6e4. |
| S180-E-PLAN | /private/tmp/npm-review-work/shared-next-batch018/review-support/source-notes-v2.json; Source notes, exact compound scope and consumer feasibility | context_only | Frozen source-only reading scopes, actual retrieval times and full raw-row selectors. Formal authoring does not imply a new retrieval or a broader source read. |
| S180-E-CONSUMERS | /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py; Method overrides; original source_row; producer/cluster emission; strain/reference composition | context_only | REPLACE changes method grades but has no independent full-row SHA check. WITHDRAW clears all methods and checks its old context. Real full-row-pinned strain/citation overlays can guard compatible paired changes; their current consumers reject a structure-correction marker. |
| S180-E-GRADING | conf/producer_evidence.tsv; Complete two-claim evidence vocabulary | context_only | Knock-out studies is defined as native-organism necessity. Heterologous expression supports the cloned locus, without upgrading the native taxon assertion. |
| S180-E-ACCESS | /private/tmp/npm-review-work/shared-next-batch018/review-support/input-manifest-v2.json; Flattened source packet and exact per-response receipts | context_only | All successful and failed source responses, derived texts, inspected figure files and raw selectors are byte-pinned. Main-body access gaps are scoped to the attempted sources, not a claim of biological absence. |
| S180-E-DAQ14 | DOI:10.3390/md12063574; PMC4071591, complete scientific main, Methods, Tables and Figure 1; retained /private/tmp/npm-review-work/shared-next-batch018/review-support/attempt-003/primary-two-pmc.xml | supports | Native F001 cultures yield diazaquinomycin E (1) and A (4). E has one alpha methyl and two pentyl groups, C23H28N2O4; A has two alpha methyls and two propyl groups. The F/G cocrystal is not an E assignment experiment. Pure E/A OVCAR5 LC50 values are 9.0/8.8 µM after 96 h SRB. Cellular p21/PARP/H2AX experiments concern A. This isolation paper does not report a BGC perturbation experiment. Read scope: Complete scientific main text, Methods, tables and captions read. Original Figure 1 pixels inspected and independently compared with the numbered transcription. No crystal intensity refinement. |
| S180-E-DAQ14-SI | DOI:10.3390/md12063574; Official PDF supplement, dose-response Figure S1 and spectral data; retained /private/tmp/npm-review-work/shared-next-batch018/review-support/attempt-004/diazaquinomycin2014-supplements.zip | supports | The dose-response legend explicitly identifies DAQE and DAQA. Its heading uses inconsistent compound numbers (1 and 3), which must not silently override the legend and main identification as E1/A4. Read scope: Complete extracted supplement text/tables/captions read; original physical page 2 dose-response pixels inspected. No raw spectral reassignment. |
| S180-E-DAQ-LOCUS | genbank:QZWF01000007.1; Exact versioned source header and all feature qualifiers except translations; retained /private/tmp/npm-review-work/shared-next-batch018/review-support/attempt-009/QZWF01000007.1.gb | supports | F001 Indonesian sediment source, exact requested 23,503 bp interval, automated homology annotations and a partial first CDS. Annotation is not an experimental demonstration of A/E biosynthesis. Read scope: Complete header and metadata/feature qualifiers read. DNA and translation bytes retained but not manually retranslated or compared to every experimental construct. |
| C180-OWNER | data/natural_products/alkaloids/diazaquinomycin-e.yaml; Complete owner and all seven matching source-row sets; no referenced components | supports | The complete owner denotes diazaquinomycin E under naturalproductmech:mibig-c12262ec06. All source selectors, versions and complete row digests are retained in COMPARISON: [{"row_sha256": "84e71f90e7c50894f10046bfb1b87a62a0f490dc9cb3635bc70e5ba29346d6e4", "selector": "BGC0001850:2", "version": "4"}]. The official intake and prepared owner bytes agree. |
| C180-GRAPH | /private/tmp/npm-review-work/180/chemistry.json; Fresh intake RDKit result and frozen Standard/fixed-H comparison | supports | The stored SMILES recomputes to JTXSSZYKSHIXRS-UHFFFAOYSA-N, formula C22H26N2O4, formal charge 0; stored InChI/key agree. These are representation checks, not experimental identity proof. |
| C180-COMPARISON | /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/chemical-comparison.json; Record 180; exact source rows and each graph comparison | supports | Exact Standard, fixed-H, formula, charge and stereo comparisons of the retained owner, complete raw rows and current authority responses; primary experimental proof is assessed separately. |
| C180-LOCAL-SEARCH | /private/tmp/npm-review-work/180/chemistry-search-receipt.json; Exact full key, label, slug and source selector in raw/owner/curation trees | supports | Ignored-inclusive bounded search preserves all matching paths; an absent curation decision does not imply a missing scientific source. |
| C180-CHEBI-SEARCH-1 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=JTXSSZYKSHIXRS-UHFFFAOYSA-N&amp;size=100; Literal key search; chebi-key-180.json | supports | No compound matches the provided term: 'JTXSSZYKSHIXRS-UHFFFAOYSA-N' |
| C180-CHEBI-SEARCH-2 | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=diazaquinomycin+E&amp;size=100; Literal name search; chebi-name-180.json | supports | 1 returned name/key results; evaluate exact key and stars, not name similarity. |
| C180-AUTH-1 | https://mibig.secondarymetabolites.org/repository/BGC0001850.4/annotations.json; compounds[1].structure; BGC0001850.4.json | supports | current MIBiG BGC0001850:2: representation parses=True; parsed key JTXSSZYKSHIXRS-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C180-AUTH-2 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/134814868/property/IsomericSMILES,InChI,InChIKey,MolecularFormula/JSON; PropertyTable.Properties[].SMILES; pubchem-134814868.json | supports | PubChem literal 134814868: representation parses=True; parsed key JTXSSZYKSHIXRS-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C180-AUTH-3 | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/134814868/SDF?record_type=2d; first complete SDF; pubchem-134814868.sdf | supports | PubChem SDF literal 134814868: representation parses=True; parsed key JTXSSZYKSHIXRS-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. |
| C180-AUTH-4 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/222154/; default_structure.smiles; CHEBI222154.json | context_only | ChEBI JSON 222154: representation parses=False; parsed key None; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C180-AUTH-5 | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/222154/; official MOL endpoint; CHEBI222154-official.mol | context_only | ChEBI MOL 222154: representation parses=True; parsed key XRVKCURQKFTZGG-UHFFFAOYSA-N; exact stored Standard key match=False, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C180-AUTH-6 | https://www.wikidata.org/wiki/Special:EntityData/Q125617960.json; P233; Q125617960.json | supports | Wikidata Q125617960: representation parses=True; parsed key JTXSSZYKSHIXRS-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True. This current database representation is not independent primary experimental proof. Canonical P233 is not an isomeric stereo assertion; compare P2017 when present. |
| C180-AUTH-7 | https://www.wikidata.org/wiki/Special:EntityData/Q125617960.json; P234 Standard InChI (normalized reconstruction; not a literal fixed-H assertion); Q125617960.json | supports | Wikidata Q125617960: representation parses=True; parsed key JTXSSZYKSHIXRS-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=False. This current database representation is not independent primary experimental proof. |
| C180-CONSUMERS | src/naturalproductmech/curate/structure_corrections.py; Complete correction consumer and separately pinned selector/collision comparison | supports | Only REPLACE_WITH_CHEBI and SPLIT_SHARED_WITH_CHEBI are implemented. They require a unique structured three-star committed target and complete original/target row hashes; arbitrary primary SMILES and label overrides are not accepted. The loader copies target SMILES, so valid MOL versus invalid JSON text must be distinguished. It clears old xrefs and rebuilds exact-key joins. Existing claim-reference and strain consumers reject structure_correction_note; composition needs explicit implementation and tests. |
| C180-XREF-CONSUMER | src/naturalproductmech/curate/xref_exclusions.py; Complete literal-xref exclusion consumer; pubchem/npatlas namespace and full-row guard | supports | A specific existing literal pubchem or npatlas assertion can be excluded under the exact original BGC:compound_index selector and complete row hash. This neither installs a positive xref nor migrates biological observations. It rejects a structure-corrected row; compatible stacking is not assumed. |
| C180-ROUTING | /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/grounding-source-selector-routing.json; Exact scoped calculation; original inputs, version and limitations retained | supports | Complete source selectors and mints reproduce, each full original row is unique, and exact diagnostic alternate keys for171/180 have no committed eligible CheBI or MIBiG target in the inspected inventory. Existing-decision absence is limited to the two complete maintained TSVs searched ignored-inclusively. |
| C180-PRIMARY-2014 | DOI:10.3390/md12063574; Full scientific Results/Methods and original Figure 1; E1 versus A4; retained /private/tmp/npm-review-work/shared-next-batch018/review-support/attempt-003/primary-two-pmc.xml | supports | Original A4 has two alpha methyls and two propyl groups; E1 has one alpha methyl and two pentyl groups. F/G co-crystal evidence does not assign E. The chemistry pass read the complete scientific body but did not independently reassign all SI spectra. |
| C180-PRIMARY-FIGURE | DOI:10.3390/md12063574; Verified original ZIP member marinedrugs-12-03574-g001.jpg; original Figure 1; retained /private/tmp/npm-review-work/shared-next-batch018/review-support/attempt-004/diazaquinomycin2014-supplements.zip | supports | The exact extracted original image bytes match the retained download archive. Numbered independent graph transcription distinguishes A4 and E1 without choosing by database majority. |
| C180-PRIMARY-MAP | /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/diazaquinomycin2014-figure1-comparison.json; Exact scoped calculation; original inputs, version and limitations retained | supports | Independent numbered graphs reproduce A as WZZGVUSWZMBPPL with Standard/fixed-H agreement and E as XRVKCURQKFTZGG, C23H28N2O4. The retained E graph is C22H26N2O4 and lacks the primary C3–C11 methyl. |

## Limits And Additional Notes

- The root section inventories present claims and source routing; chemical identities, source-specific experiments, definition claims and optional-content assertions require their separately scoped scientific assessments.
- Original E assignment does not borrow the F/G cocrystal.
- Any future graph change requires explicit preservation and re-adjudication of old-key LOTUS, xrefs, classification and source joins.
- The frozen source packet preserves actual access times and explicit full-text/pixel scope; formal authoring does not imply new retrieval.
- No optional missing pathway, protein or activity entry is treated as a mandatory defect. Taxonomic namespace, computed classification and independent chemical authority checks are retained in their separate sections.
- Only the proposed maintained route and acceptance criteria are reported; no scientific record, source inventory, campaign or repository state was changed.
- Authority matches establish the representations actually returned at their retained access times; they are not independent experimental structure or absolute-hand determinations. Root and science sections separately assess organism, locus, classification and history claims.
- This is direct primary constitution evidence, not an authority vote. The original F/G co-crystal does not determine E. The source reports its mass values as published; no forced agreement is imposed. No complete record replacement or old-key biological/occurrence migration is authorized by this source packet.
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
review_id: 20261021T215706Z-diazaquinomycin-e
title: 'Diazaquinomycin E: original methyl group missing from the retained structure'
started_at: '2026-10-21T21:49:55.297806Z'
finished_at: '2026-10-21T21:57:06.369767Z'
completion: completed
verdict: needs_curation
scientific_review: true
summary: The original 2014 article identifies native F001 diazaquinomycin E as C23H28N2O4
  with one alpha methyl group and two pentyl chains. The retained C22H26N2O4 structure
  omits that methyl, creating a confirmed constitutional error also present in its
  PubChem cross-reference. The completed review requires a guarded structure correction
  and separate adjudication of affected source joins, while preserving the positive
  named-E isolation evidence.
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
    role: context
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
  - path: tests/test_claim_references.py
    sha256: 11b2fc60dbe32154df63fb2e8c784c7c8ba6585581c09bba2eebe2c5192d4c06
    role: context
  - path: tests/test_mibig_locus_evidence_overrides.py
    sha256: 9177b5bd24f6e47cc4743857179217d9e0d4add9560b2ce3faefaebe53ba09a0
    role: context
  - path: tests/test_producer_strains.py
    sha256: 17002ef1640464777f1925d12d842ed83c9098aad6de724ae0ea236ecccc4ff3
    role: context
scope:
  description: One complete generated owner and any referenced components, assessed
    claim by claim for exact identity, provenance, origin, producer and occurrence
    scope, biosynthesis, classification, optional content and audit history.
  selection: Campaign record 180, batch 018, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated targets in earlier
    batch commits (publication tracked separately). At selection, 224 of 3116 current
    records had campaign coverage and 2892 remained. The population search included
    ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-c12262ec06
targets:
- target_id: naturalproductmech:mibig-c12262ec06
  path: data/natural_products/alkaloids/diazaquinomycin-e.yaml
  label: diazaquinomycin E
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
  - naturalproductmech:mibig-c12262ec06
  command: just validate-strict data/natural_products/alkaloids/diazaquinomycin-e.yaml
    --out /private/tmp/npm-review-work/180/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T21:49:56.999350Z
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
  - naturalproductmech:mibig-c12262ec06
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
  - naturalproductmech:mibig-c12262ec06
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
  - naturalproductmech:mibig-c12262ec06
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
  - naturalproductmech:mibig-c12262ec06
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
  - naturalproductmech:mibig-c12262ec06
- check_id: R180-FULL-OWNER
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
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - R180-OWNER
  - R180-LOCAL
  - R180-PUBCHEM-PREP
- check_id: S180-C-NAMED-ISOLATION
  name: Named native isolation and assay context
  status: passed
  required: true
  summary: Original main and official SI support the exact named compound and experimental
    endpoint; F/G cocrystal evidence is not transferred to A/E.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - S180-E-DAQ14
  - S180-E-DAQ14-SI
- check_id: C180-C-REPRESENTATION
  name: Stored chemical representation and complete source row
  status: passed
  required: true
  summary: Fresh intake derivation agrees with the stored graph; the source selector,
    full row and prepared snapshot were independently rechecked.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - C180-OWNER
  - C180-GRAPH
  - C180-COMPARISON
- check_id: C180-C-XREF
  name: Literal identifier resolution and parsed representation
  status: passed
  required: true
  summary: Every present literal was resolved; differing Standard/fixed-H, charge
    or precision is assessed separately. For invalid default ChEBI JSON SMILES, the
    independently fetched official MOL supplies the parsed comparison.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - C180-COMPARISON
  - C180-AUTH-1
  - C180-AUTH-2
  - C180-AUTH-3
  - C180-AUTH-4
  - C180-AUTH-5
  - C180-AUTH-6
  - C180-AUTH-7
- check_id: C180-C-CONSTITUTION
  name: Exact primary E constitution
  status: failed
  required: true
  summary: The original compound1 contains an additional methyl absent from the current
    MIBiG/PubChem graph. This is direct primary constitutional disagreement.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - C180-PRIMARY-2014
  - C180-PRIMARY-FIGURE
  - C180-PRIMARY-MAP
  - C180-COMPARISON
evidence:
- evidence_id: R180-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/diazaquinomycin-e.yaml
  locator: Complete post-intake owner, optional assertions and all history events
  accessed_at: '2026-10-21T21:50:20.710767Z'
  support: supports
  summary: 'Root read the complete owner after successful official intake: 1 occurrence,
    1 producer and 1 locus assertions. No referenced external component is present.
    Optional fields: none.'
  snapshot_sha256: 3438673a011d56c1e6b842b82f90e5d9642d0afd1a0169d385812f22251082a6
- evidence_id: R180-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/180/local-sources.json
  locator: Complete resolved owner and all six officially captured raw row sets
  accessed_at: '2026-10-21T21:50:20.710767Z'
  support: context_only
  summary: All six captured MIBiG, LOTUS, ChEBI structures/origins, CyanoMetDB and
    NPClassifier sets match the frozen preparation, including empty sets. The separate
    seventh PubChem inventory comparison is distinguished below. Source fidelity does
    not itself establish experimental support.
  snapshot_sha256: 9d16d87e03ccbba6277b133d87cc5edc0b2f1f9987b8519cb7c9d311b28fe999
- evidence_id: R180-PUBCHEM-PREP
  kind: record_content
  reference: data/raw/pubchem_bioassay.tsv
  locator: Exact-key rows compared with the separate provisional seventh source set
  accessed_at: '2026-10-21T21:50:26.475384Z'
  support: context_only
  summary: The separate committed PubChem raw set contains 0 matching rows and reproduces
    the frozen preparation. This is not part of the official six-set intake. All matching
    rows were read by root; the 12 diazaquinomycin A observations are the only emitted
    assays. The separately prepared assay packet owns exact endpoint/call interpretation.
    Empty/no-assay-data rows elsewhere are not tested outcomes.
  snapshot_sha256: 6c6184b880a20eea1df8a7cd440886063f59f8e2e663bcc36c296fdc4f52ff1b
- evidence_id: R180-Q1144013
  kind: database
  reference: https://www.wikidata.org/wiki/Q1144013
  locator: P225 and P685 in the retained complete nine-entity response
  accessed_at: '2026-10-21T20:16:18.792344Z'
  support: context_only
  summary: Literal scientific name and NCBI taxon identifier agree with the matched
    source rows. Identifier routing does not establish occurrence chemistry, producing
    stock or experiment.
  snapshot_sha256: 618d1ed87da35071c378273e14a8b5030f73f9485418b509039d6437d0372f92
- evidence_id: R180-TAXON-CONTEXT
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&retmode=xml&id=112125,1163,1175,1220761,1427518,1510026,176275,1873482,1883,1956,28073,2926,344612,373637,38033,385555,39447,398006,467598,500485,54296,571,7461,77021,77022
  locator: Exact relevant TaxId, ScientificName, Rank, ParentTaxId and OtherNames
    fields
  accessed_at: '2026-10-21T20:16:19.157506Z'
  support: context_only
  summary: NCBI 1510026 Streptomyces sp. F001 is species rank under unclassified Streptomyces,
    despite its stock-like label. NCBI 1883 is genus Streptomyces. Neither identifier
    alone validates a specific genomic locus or equates historical producing cultures.
  snapshot_sha256: 10cf506b9c7a3918100ff016e4681733f450deced1f583bd9100ae2a1a6fe4cb
- evidence_id: R180-IMODULON
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
- evidence_id: S180-E-LOCAL
  kind: record_content
  reference: /private/tmp/npm-review-work/180/local-sources.json
  locator: Whole owner, all assertions and components; seven exact source sets
  accessed_at: '2026-10-21T21:50:20.710767Z'
  support: context_only
  summary: The entire actual owner and six captured source sets match the frozen inventory;
    the seventh PubChem set was independently reconciled against the full raw TSV.
  snapshot_sha256: 9d16d87e03ccbba6277b133d87cc5edc0b2f1f9987b8519cb7c9d311b28fe999
- evidence_id: S180-E-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: '{"bgc_classes": "other", "bgc_subclasses": "shikimate-derived", "cluster_link_evidence_basis":
    "CLUSTER_UNSTATED", "compound_classes": "", "compound_index": "2", "compound_name":
    "diazaquinomycin E", "database_ids": "pubchem:134814868", "entry_completeness":
    "complete", "entry_quality": "questionable", "entry_status": "active", "entry_version":
    "4", "genome_accession": "QZWF01000007.1", "locus_evidence_methods": "", "locus_from":
    "257859", "locus_to": "281361", "mibig_accession": "BGC0001850", "primary_reference":
    "DOI:10.3390/md12063574", "producer_evidence_basis": "SOURCE_ASSERTION", "reference_basis":
    "ENTRY", "smiles": "CCCCCC1=CC(=O)NC2=C1C(=O)C3=C(C2=O)NC(=O)C=C3CCCCC", "standard_inchi":
    "InChI=1S/C22H26N2O4/c1-3-5-7-9-13-11-15(25)23-19-17(13)21(27)18-14(10-8-6-4-2)12-16(26)24-20(18)22(19)28/h11-12H,3-10H2,1-2H3,(H,23,25)(H,24,26)",
    "standard_inchi_key": "JTXSSZYKSHIXRS-UHFFFAOYSA-N", "stereo_complete": "true",
    "taxon_id": "NCBITaxon:1510026", "taxon_label": "Streptomyces sp. F001"}'
  accessed_at: '2026-10-21T21:50:20.710767Z'
  support: context_only
  summary: Exact immutable source selector BGC0001850:2; expected_source_row_sha256=84e71f90e7c50894f10046bfb1b87a62a0f490dc9cb3635bc70e5ba29346d6e4.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: S180-E-PLAN
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch018/review-support/source-notes-v2.json
  locator: Source notes, exact compound scope and consumer feasibility
  accessed_at: '2026-10-21T20:31:56.793720Z'
  support: context_only
  summary: Frozen source-only reading scopes, actual retrieval times and full raw-row
    selectors. Formal authoring does not imply a new retrieval or a broader source
    read.
  snapshot_sha256: 619ff34112de12e198759ee8efc02e72393197b66da5b011ba7a4ec30b0aa178
- evidence_id: S180-E-CONSUMERS
  kind: record_content
  reference: /private/tmp/npm-record-reviews-20261021/scripts/seed_from_sources.py
  locator: Method overrides; original source_row; producer/cluster emission; strain/reference
    composition
  accessed_at: '2026-10-21T21:50:20.710767Z'
  support: context_only
  summary: REPLACE changes method grades but has no independent full-row SHA check.
    WITHDRAW clears all methods and checks its old context. Real full-row-pinned strain/citation
    overlays can guard compatible paired changes; their current consumers reject a
    structure-correction marker.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: S180-E-GRADING
  kind: record_content
  reference: conf/producer_evidence.tsv
  locator: Complete two-claim evidence vocabulary
  accessed_at: '2026-10-21T21:50:20.710767Z'
  support: context_only
  summary: Knock-out studies is defined as native-organism necessity. Heterologous
    expression supports the cloned locus, without upgrading the native taxon assertion.
  snapshot_sha256: 67d8209149c2e86f4605381e4a667fc2aff53b71e8351ef337a443642c74f131
- evidence_id: S180-E-ACCESS
  kind: record_content
  reference: /private/tmp/npm-review-work/shared-next-batch018/review-support/input-manifest-v2.json
  locator: Flattened source packet and exact per-response receipts
  accessed_at: '2026-10-21T20:31:56.838236Z'
  support: context_only
  summary: All successful and failed source responses, derived texts, inspected figure
    files and raw selectors are byte-pinned. Main-body access gaps are scoped to the
    attempted sources, not a claim of biological absence.
  snapshot_sha256: 70fc5abd3587a9cd4dd236554037c61c39d4de628b84b963440441eb7ea58957
- evidence_id: S180-E-DAQ14
  kind: primary_source
  reference: DOI:10.3390/md12063574
  locator: PMC4071591, complete scientific main, Methods, Tables and Figure 1; retained
    /private/tmp/npm-review-work/shared-next-batch018/review-support/attempt-003/primary-two-pmc.xml
  accessed_at: '2026-10-21T20:10:00.864157Z'
  support: supports
  summary: 'Native F001 cultures yield diazaquinomycin E (1) and A (4). E has one
    alpha methyl and two pentyl groups, C23H28N2O4; A has two alpha methyls and two
    propyl groups. The F/G cocrystal is not an E assignment experiment. Pure E/A OVCAR5
    LC50 values are 9.0/8.8 µM after 96 h SRB. Cellular p21/PARP/H2AX experiments
    concern A. This isolation paper does not report a BGC perturbation experiment.
    Read scope: Complete scientific main text, Methods, tables and captions read.
    Original Figure 1 pixels inspected and independently compared with the numbered
    transcription. No crystal intensity refinement.'
  snapshot_sha256: f56a0d3a72908d48898a1a5385106b9825eea72a8c0641390d7de481213d2f28
- evidence_id: S180-E-DAQ14-SI
  kind: primary_source
  reference: DOI:10.3390/md12063574
  locator: Official PDF supplement, dose-response Figure S1 and spectral data; retained
    /private/tmp/npm-review-work/shared-next-batch018/review-support/attempt-004/diazaquinomycin2014-supplements.zip
  accessed_at: '2026-10-21T20:10:34.941573Z'
  support: supports
  summary: 'The dose-response legend explicitly identifies DAQE and DAQA. Its heading
    uses inconsistent compound numbers (1 and 3), which must not silently override
    the legend and main identification as E1/A4. Read scope: Complete extracted supplement
    text/tables/captions read; original physical page 2 dose-response pixels inspected.
    No raw spectral reassignment.'
  snapshot_sha256: 231f87aefca3ffa68781bbb5fe367dbcd55e78078cd53c2ca1b9fceaffe2be24
- evidence_id: S180-E-DAQ-LOCUS
  kind: database
  reference: genbank:QZWF01000007.1
  locator: Exact versioned source header and all feature qualifiers except translations;
    retained /private/tmp/npm-review-work/shared-next-batch018/review-support/attempt-009/QZWF01000007.1.gb
  accessed_at: '2026-10-21T20:16:17.945262Z'
  support: supports
  summary: 'F001 Indonesian sediment source, exact requested 23,503 bp interval, automated
    homology annotations and a partial first CDS. Annotation is not an experimental
    demonstration of A/E biosynthesis. Read scope: Complete header and metadata/feature
    qualifiers read. DNA and translation bytes retained but not manually retranslated
    or compared to every experimental construct.'
  snapshot_sha256: 91bdfaf33a05cbd7430ed329c558ab2dc48140e2585a2de5129952b262545d0e
- evidence_id: C180-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/diazaquinomycin-e.yaml
  locator: Complete owner and all seven matching source-row sets; no referenced components
  accessed_at: '2026-10-21T21:50:37.680169Z'
  support: supports
  summary: 'The complete owner denotes diazaquinomycin E under naturalproductmech:mibig-c12262ec06.
    All source selectors, versions and complete row digests are retained in COMPARISON:
    [{"row_sha256": "84e71f90e7c50894f10046bfb1b87a62a0f490dc9cb3635bc70e5ba29346d6e4",
    "selector": "BGC0001850:2", "version": "4"}]. The official intake and prepared
    owner bytes agree.'
  snapshot_sha256: 3438673a011d56c1e6b842b82f90e5d9642d0afd1a0169d385812f22251082a6
- evidence_id: C180-GRAPH
  kind: validation
  reference: /private/tmp/npm-review-work/180/chemistry.json
  locator: Fresh intake RDKit result and frozen Standard/fixed-H comparison
  accessed_at: '2026-10-21T21:49:56.013420Z'
  support: supports
  summary: The stored SMILES recomputes to JTXSSZYKSHIXRS-UHFFFAOYSA-N, formula C22H26N2O4,
    formal charge 0; stored InChI/key agree. These are representation checks, not
    experimental identity proof.
  snapshot_sha256: 433a98e33a528e461f27d75220df1ac8ccb7b3a66f5147f16d28704962a73365
- evidence_id: C180-COMPARISON
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/chemical-comparison.json
  locator: Record 180; exact source rows and each graph comparison
  accessed_at: '2026-10-21T20:15:53.614413Z'
  support: supports
  summary: Exact Standard, fixed-H, formula, charge and stereo comparisons of the
    retained owner, complete raw rows and current authority responses; primary experimental
    proof is assessed separately.
  snapshot_sha256: 941268dc4402c97bfbd9f113317e60aa89a5ecd89e45a4d8f14709827989c49c
- evidence_id: C180-LOCAL-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/180/chemistry-search-receipt.json
  locator: Exact full key, label, slug and source selector in raw/owner/curation trees
  accessed_at: '2026-10-21T21:50:37.886826Z'
  support: supports
  summary: Ignored-inclusive bounded search preserves all matching paths; an absent
    curation decision does not imply a missing scientific source.
  snapshot_sha256: cd560c48170098415562b6d08926fa888ab12b91ab6927663d351fe39beddbc0
  search_scope: rg --no-ignore --hidden; data/natural_products, data/raw and curation;
    exact full key, current label, slug and BGC:compound_index. No claim beyond these
    trees.
- evidence_id: C180-CHEBI-SEARCH-1
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=JTXSSZYKSHIXRS-UHFFFAOYSA-N&size=100
  locator: Literal key search; chebi-key-180.json
  accessed_at: '2026-10-21T20:14:44.183984Z'
  support: supports
  summary: 'No compound matches the provided term: ''JTXSSZYKSHIXRS-UHFFFAOYSA-N'''
  snapshot_sha256: 6051412888782da5f387b16796b24d35b54dc205e1c9ec5dd44574fcab412ffe
  search_scope: Official ChEBI es_search bounded key request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C180-CHEBI-SEARCH-2
  kind: search
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=diazaquinomycin+E&size=100
  locator: Literal name search; chebi-name-180.json
  accessed_at: '2026-10-21T20:14:43.145055Z'
  support: supports
  summary: 1 returned name/key results; evaluate exact key and stars, not name similarity.
  snapshot_sha256: bc008a961621e8b9ddefafd59063cd22f065015f60f90e2b415702263480f112
  search_scope: Official ChEBI es_search bounded name request, size=100, exact URL
    retained. This is not a universal absence claim.
- evidence_id: C180-AUTH-1
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0001850.4/annotations.json
  locator: compounds[1].structure; BGC0001850.4.json
  accessed_at: '2026-10-21T20:14:42.280903Z'
  support: supports
  summary: 'current MIBiG BGC0001850:2: representation parses=True; parsed key JTXSSZYKSHIXRS-UHFFFAOYSA-N;
    exact stored Standard key match=True, fixed-H match=True. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: aee73ec5cc2c0a5e77154cc26569024528a3a721e9b58bb92283e08ae0e0fdfe
- evidence_id: C180-AUTH-2
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/134814868/property/IsomericSMILES,InChI,InChIKey,MolecularFormula/JSON
  locator: PropertyTable.Properties[].SMILES; pubchem-134814868.json
  accessed_at: '2026-10-21T20:14:42.624724Z'
  support: supports
  summary: 'PubChem literal 134814868: representation parses=True; parsed key JTXSSZYKSHIXRS-UHFFFAOYSA-N;
    exact stored Standard key match=True, fixed-H match=True. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: a845eab743ce35d8dee664783ceb473a62da828b6c8ce3ac1a2f524f6bb05a91
- evidence_id: C180-AUTH-3
  kind: authority
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/134814868/SDF?record_type=2d
  locator: first complete SDF; pubchem-134814868.sdf
  accessed_at: '2026-10-21T20:14:42.612851Z'
  support: supports
  summary: 'PubChem SDF literal 134814868: representation parses=True; parsed key
    JTXSSZYKSHIXRS-UHFFFAOYSA-N; exact stored Standard key match=True, fixed-H match=True.
    This current database representation is not independent primary experimental proof.'
  snapshot_sha256: 30b31a1fe04b9c33e38ec94e6a46bb91e47e9d277bbc67b5e655b1740c64e857
- evidence_id: C180-AUTH-4
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/222154/
  locator: default_structure.smiles; CHEBI222154.json
  accessed_at: '2026-10-21T20:15:27.588665Z'
  support: context_only
  summary: 'ChEBI JSON 222154: representation parses=False; parsed key None; exact
    stored Standard key match=False, fixed-H match=False. This current database representation
    is not independent primary experimental proof.'
  snapshot_sha256: 5577c73844d085b49eb5a947e1d227fe7b8e61402a034419861540a9a5b8d5a7
- evidence_id: C180-AUTH-5
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/222154/
  locator: official MOL endpoint; CHEBI222154-official.mol
  accessed_at: '2026-10-21T20:15:27.699107Z'
  support: context_only
  summary: 'ChEBI MOL 222154: representation parses=True; parsed key XRVKCURQKFTZGG-UHFFFAOYSA-N;
    exact stored Standard key match=False, fixed-H match=False. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: f1ce8372f3affa3d038bbb16fc855a0768fca1dfe4daeeb6ac35d0cc362707c1
- evidence_id: C180-AUTH-6
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q125617960.json
  locator: P233; Q125617960.json
  accessed_at: '2026-10-21T20:14:42.826499Z'
  support: supports
  summary: 'Wikidata Q125617960: representation parses=True; parsed key JTXSSZYKSHIXRS-UHFFFAOYSA-N;
    exact stored Standard key match=True, fixed-H match=True. This current database
    representation is not independent primary experimental proof. Canonical P233 is
    not an isomeric stereo assertion; compare P2017 when present.'
  snapshot_sha256: a353be1b443555f7a1b87937e913d4308ae47480f5e7248dd6808aab9c68ae30
- evidence_id: C180-AUTH-7
  kind: authority
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q125617960.json
  locator: P234 Standard InChI (normalized reconstruction; not a literal fixed-H assertion);
    Q125617960.json
  accessed_at: '2026-10-21T20:14:42.826499Z'
  support: supports
  summary: 'Wikidata Q125617960: representation parses=True; parsed key JTXSSZYKSHIXRS-UHFFFAOYSA-N;
    exact stored Standard key match=True, fixed-H match=False. This current database
    representation is not independent primary experimental proof.'
  snapshot_sha256: a353be1b443555f7a1b87937e913d4308ae47480f5e7248dd6808aab9c68ae30
- evidence_id: C180-CONSUMERS
  kind: record_content
  reference: src/naturalproductmech/curate/structure_corrections.py
  locator: Complete correction consumer and separately pinned selector/collision comparison
  accessed_at: '2026-10-21T21:50:37.680169Z'
  support: supports
  summary: Only REPLACE_WITH_CHEBI and SPLIT_SHARED_WITH_CHEBI are implemented. They
    require a unique structured three-star committed target and complete original/target
    row hashes; arbitrary primary SMILES and label overrides are not accepted. The
    loader copies target SMILES, so valid MOL versus invalid JSON text must be distinguished.
    It clears old xrefs and rebuilds exact-key joins. Existing claim-reference and
    strain consumers reject structure_correction_note; composition needs explicit
    implementation and tests.
  snapshot_sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
- evidence_id: C180-XREF-CONSUMER
  kind: record_content
  reference: src/naturalproductmech/curate/xref_exclusions.py
  locator: Complete literal-xref exclusion consumer; pubchem/npatlas namespace and
    full-row guard
  accessed_at: '2026-10-21T21:50:37.680169Z'
  support: supports
  summary: A specific existing literal pubchem or npatlas assertion can be excluded
    under the exact original BGC:compound_index selector and complete row hash. This
    neither installs a positive xref nor migrates biological observations. It rejects
    a structure-corrected row; compatible stacking is not assumed.
  snapshot_sha256: 17c3d9e7794bae596b22cf19a2dd5bc2169475d6fea81ea4e6f1781a53af9157
- evidence_id: C180-ROUTING
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
- evidence_id: C180-PRIMARY-2014
  kind: primary_source
  reference: DOI:10.3390/md12063574
  locator: Full scientific Results/Methods and original Figure 1; E1 versus A4; retained
    /private/tmp/npm-review-work/shared-next-batch018/review-support/attempt-003/primary-two-pmc.xml
  accessed_at: '2026-10-21T20:10:00.864157Z'
  support: supports
  summary: Original A4 has two alpha methyls and two propyl groups; E1 has one alpha
    methyl and two pentyl groups. F/G co-crystal evidence does not assign E. The chemistry
    pass read the complete scientific body but did not independently reassign all
    SI spectra.
  snapshot_sha256: f56a0d3a72908d48898a1a5385106b9825eea72a8c0641390d7de481213d2f28
- evidence_id: C180-PRIMARY-FIGURE
  kind: primary_source
  reference: DOI:10.3390/md12063574
  locator: Verified original ZIP member marinedrugs-12-03574-g001.jpg; original Figure
    1; retained /private/tmp/npm-review-work/shared-next-batch018/review-support/attempt-004/diazaquinomycin2014-supplements.zip
  accessed_at: '2026-10-21T20:10:34.941573Z'
  support: supports
  summary: The exact extracted original image bytes match the retained download archive.
    Numbered independent graph transcription distinguishes A4 and E1 without choosing
    by database majority.
  snapshot_sha256: 231f87aefca3ffa68781bbb5fe367dbcd55e78078cd53c2ca1b9fceaffe2be24
- evidence_id: C180-PRIMARY-MAP
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch018/chemistry-prep/diazaquinomycin2014-figure1-comparison.json
  locator: Exact scoped calculation; original inputs, version and limitations retained
  accessed_at: '2026-10-21T20:16:51.688735Z'
  support: supports
  summary: Independent numbered graphs reproduce A as WZZGVUSWZMBPPL with Standard/fixed-H
    agreement and E as XRVKCURQKFTZGG, C23H28N2O4. The retained E graph is C22H26N2O4
    and lacks the primary C3–C11 methyl.
  snapshot_sha256: fb0be01ee050ff0ed5335241094b62ff7bd26c074f97036a680cfd85210c9145
assessments:
- assessment_id: R180-HISTORY
  area: provenance
  topic: Native status and complete audit history
  outcome: supported
  summary: All 2 retained events are SEEDED_FROM_SOURCES. Native status remains SEEDED;
    provenance events are not structured-review passes.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - R180-OWNER
- assessment_id: R180-OPTIONAL
  area: completeness
  topic: Complete optional-assertion inventory
  outcome: not_applicable
  summary: No optional definition, pathway, graph, target, assay, application, summary,
    relation, discussion or clinical-status assertion is present. Optional enrichment
    is separate from checking existing source claims.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - R180-OWNER
  - R180-LOCAL
  - R180-PUBCHEM-PREP
- assessment_id: R180-FILING
  area: representation
  topic: Exact-key computed classification provenance
  outcome: supported
  summary: The exact-key NPClassifier projection and version npclassifier.gnps2.org@2026-09-07
    reproduce the owner filing, superclass/class labels and glycoside value false.
    Computed labels are not independent precursor, mechanism or natural-origin evidence.
    Any accepted new identity requires reclassification for its effective key.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - R180-OWNER
  - R180-LOCAL
- assessment_id: R180-ORGANISM-IDS
  area: grounding
  topic: Literal organism identifier routing
  outcome: supported
  summary: All literal organism-QID routes agree at the inspected P225/P685 scope.
    Occurrence and experimental-unit support remain separate.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - R180-Q1144013
- assessment_id: R180-TAXON-SCOPE
  area: provenance
  topic: Taxonomic names versus experimental stocks
  outcome: supported
  summary: NCBI 1510026 Streptomyces sp. F001 is species rank under unclassified Streptomyces,
    despite its stock-like label. NCBI 1883 is genus Streptomyces. Neither identifier
    alone validates a specific genomic locus or equates historical producing cultures.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - R180-TAXON-CONTEXT
  - R180-OWNER
- assessment_id: R180-IMODULON-SCOPE
  area: completeness
  topic: Producer transcriptomic applicability
  outcome: not_applicable
  summary: No exact native producer species/strain dataset is represented in the inspected
    catalogue. Related species and possible experimental hosts do not establish a
    construct/condition match; no gene/module or compound-production inference is
    made.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - R180-OWNER
  - R180-IMODULON
- assessment_id: S180-A-NATIVE
  area: evidence
  topic: Exact native strain, isolation and locus evidence
  outcome: supported
  summary: The 2014 study isolates named E (1) from Streptomyces sp. F001. Its marine
    sediment source and current exact accession agree at source-metadata scope. No
    genetic manipulation of this locus is reported in the complete isolation paper,
    so the empty methods and source-tier biological assertion are not upgraded from
    annotation.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - S180-E-LOCAL
  - S180-E-DAQ14
  - S180-E-DAQ14-SI
  - S180-E-DAQ-LOCUS
  dimensions:
  - name: native_strain
    value: Streptomyces sp. F001
    definition: Native marine-isolate culture, separate from historical OM-704.
    evidence_ids:
    - S180-E-DAQ14
    - S180-E-DAQ-LOCUS
  - name: producer_locus_evidence
    value: SOURCE_ASSERTION / CLUSTER_UNSTATED
    definition: Imported empty methods remain source-faithful; genomic annotation
      is not a new experiment.
    evidence_ids:
    - S180-E-LOCAL
    - S180-E-GRADING
    - S180-E-DAQ-LOCUS
  - name: pure_compound_endpoint
    value: OVCAR5, 96 h SRB LC50
    definition: E and A are measured separately; no direct molecular target is inferred.
    evidence_ids:
    - S180-E-DAQ14
    - S180-E-DAQ14-SI
- assessment_id: S180-A-EXACT-APPLICABILITY
  area: identity
  topic: Named E biological evidence versus retained graph
  outcome: concern
  summary: Original E1 has C23H28N2O4 with one alpha methyl and two pentyl chains;
    the retained C22 graph lacks that methyl. Native isolation and LC50 9.0 µM are
    positive for the original drawn E, not automatically for the current graph. Independent
    chemistry owns this identity finding and its guarded repair; no duplicate chemical
    action is created in this science packet.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - S180-E-LOCAL
  - S180-E-DAQ14
  - S180-E-DAQ14-SI
- assessment_id: S180-A-OCCURRENCE
  area: scope
  topic: Single 2014 genus-level occurrence
  outcome: supported
  summary: The cited publication positively isolates named E from F001. Its coarse
    Streptomyces assertion is supported for that source concept, subject to resolving
    the exact graph; it is not a separate producer-grade or sequence experiment.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - S180-E-LOCAL
  - S180-E-DAQ14
- assessment_id: S180-A-COMPOSITION
  area: ownership
  topic: Conditional biological joins after identity repair
  outcome: not_applicable
  summary: Preserve the exact original source BGC0001850:2 and full SHA 84e71f90e7c50894f10046bfb1b87a62a0f490dc9cb3635bc70e5ba29346d6e4.
    Any new primary-graph consumer must explicitly decide old-key occurrence/xref/classification
    admission and preserve raw provenance. Current strain/reference consumers reject
    structure_correction_note; merely updating their hashes is insufficient if those
    overlays are added. No BGC method enrichment is warranted from this isolation
    source.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - S180-E-RAW
  - S180-E-CONSUMERS
  - S180-E-DAQ14
  - S180-E-DAQ-LOCUS
- assessment_id: C180-A-IDENTITY
  area: identity
  topic: Stored representation and source-concept provenance
  outcome: supported
  summary: The complete source row BGC0001850:2 and source-concept hash reproduce
    this stored representation; this does not establish that the upstream compound
    label is correct. Formula, charge, Standard and fixed-H distinctions are independently
    recorded. Primary support and any conflicting exact xref are assessed separately.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - C180-OWNER
  - C180-GRAPH
  - C180-COMPARISON
  dimensions:
  - name: mibig_source_selector
    value: BGC0001850:2
    definition: Accession plus compound_index, distinct from the entry-level accession.
    evidence_ids:
    - C180-OWNER
  - name: complete_raw_row_sha256
    value: 84e71f90e7c50894f10046bfb1b87a62a0f490dc9cb3635bc70e5ba29346d6e4
    definition: Sorted compact ASCII JSON of every parsed TSV field, including empty
      values.
    evidence_ids:
    - C180-OWNER
- assessment_id: C180-A-GROUNDING
  area: provenance
  topic: Exact authority eligibility and source representation
  outcome: supported
  summary: No exact eligible row exists in the committed ChEBI projection for this
    owner. Current bounded name/key searches do not justify a different congener or
    a two-star grounding.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - C180-OWNER
  - C180-COMPARISON
  - C180-LOCAL-SEARCH
  - C180-CHEBI-SEARCH-1
  - C180-CHEBI-SEARCH-2
- assessment_id: C180-A-XREF
  area: representation
  topic: Literal identifiers, namespaces and exact microstates
  outcome: supported
  summary: 'Stored literals were requested exactly and compared in their returned
    namespaces: [{"formula": "C22H26N2O4", "literal": "pubchem:134814868", "returned_key":
    "JTXSSZYKSHIXRS-UHFFFAOYSA-N", "same_fixed_h": true, "same_standard": true}].
    Standard equality does not imply literal fixed-H equality. Current authority agreement
    is not independent primary proof. Canonical Wikidata P233 is not an assertion
    of the isomeric hand.'
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - C180-COMPARISON
  - C180-AUTH-1
  - C180-AUTH-2
  - C180-AUTH-3
  - C180-AUTH-4
  - C180-AUTH-5
  - C180-AUTH-6
  - C180-AUTH-7
- assessment_id: C180-A-CHEBI-ELIGIBILITY
  area: grounding
  topic: Exact three-star projection and source concept
  outcome: supported
  summary: No eligible exact committed ChEBI row matches this owner. Current two-star
    entries remain ineligible for asserted grounding/classification and the implemented
    structure-replacement target contract.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - C180-OWNER
  - C180-COMPARISON
  - C180-ROUTING
  - C180-AUTH-1
  - C180-AUTH-2
  - C180-AUTH-3
  - C180-AUTH-4
  - C180-AUTH-5
  - C180-AUTH-6
  - C180-AUTH-7
- assessment_id: C180-A-PRIMARY-SCOPE
  area: scope
  topic: Primary chemical support and retained precision
  outcome: concern
  summary: The original 2014 main and Figure 1 compound 1 explicitly give asymmetric
    diazaquinomycin E with one C3–C11 methyl and two pentyl chains, C23H28N2O4. Independent
    numbered transcription gives XRVKCURQKFTZGG-UHFFFAOYSA-N. The retained C22H26N2O4
    graph lacks that methyl and is a different constitution. This is direct primary
    constitution evidence, not an authority vote. The original F/G co-crystal does
    not determine E. The source reports its mass values as published; no forced agreement
    is imposed. No complete record replacement or old-key biological/occurrence migration
    is authorized by this source packet.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  evidence_ids:
  - C180-PRIMARY-2014
  - C180-PRIMARY-FIGURE
  - C180-PRIMARY-MAP
  - C180-OWNER
  - C180-COMPARISON
findings:
- finding_id: C180-F-METHYL
  issue_key: mibig-bgc0001850-compound2-diazaquinomycin-e-missing-methyl
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: The retained E graph omits the original product’s methyl group
  description: The independently transcribed original E1 is asymmetric C23H28N2O4
    with one C3–C11 methyl and two pentyl groups; the retained symmetric C22 graph
    omits that methyl. Its current PubChem literal shares the same defect relative
    to the source product.
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  field_paths:
  - chemical_structure
  - xrefs
  - source_concepts
  - grounding_status
  - grounding_notes
  - occurrences
  evidence_ids:
  - C180-OWNER
  - C180-GRAPH
  - C180-COMPARISON
  - C180-CONSUMERS
  - C180-XREF-CONSUMER
  - C180-ROUTING
  - C180-PRIMARY-2014
  - C180-PRIMARY-FIGURE
  - C180-PRIMARY-MAP
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Exact source-pinned identity decision
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Current three-star target contract or explicitly reviewed missing primary-graph
      route
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Exact literal exclusion and full original-row pin
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Enforce literal namespace/uniqueness and compatible composition
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Rebuild exact-key assertions and source-qualified context
  rule_id: review-yaml-record:exact-identity-and-representation
  native_severity: blocker
  normalization_reason: The positive primary/source identity conflict blocks publication
    as one exact named product pending adjudication. This does not select an unverified
    replacement or claim a new absolute experiment.
actions:
- action_id: C180-ACTION-METHYL
  finding_ids:
  - C180-F-METHYL
  target_ids:
  - naturalproductmech:mibig-c12262ec06
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Exact source-pinned identity decision
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Current three-star target contract or explicitly reviewed missing primary-graph
      route
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_xref_exclusions.tsv
    role: Exact literal exclusion and full original-row pin
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/xref_exclusions.py
    role: Enforce literal namespace/uniqueness and compatible composition
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Rebuild exact-key assertions and source-qualified context
  description: 'Exact original guards: [{"entry_version": "4", "expected_source_row_sha256":
    "84e71f90e7c50894f10046bfb1b87a62a0f490dc9cb3635bc70e5ba29346d6e4", "old_compound_name":
    "diazaquinomycin E", "old_database_ids": "pubchem:134814868", "old_key": "JTXSSZYKSHIXRS-UHFFFAOYSA-N",
    "old_smiles": "CCCCCC1=CC(=O)NC2=C1C(=O)C3=C(C2=O)NC(=O)C=C3CCCCC", "old_standard_inchi":
    "InChI=1S/C22H26N2O4/c1-3-5-7-9-13-11-15(25)23-19-17(13)21(27)18-14(10-8-6-4-2)12-16(26)24-20(18)22(19)28/h11-12H,3-10H2,1-2H3,(H,23,25)(H,24,26)",
    "old_stereo_complete": "true", "source_id": "BGC0001850:2"}]. Adjudicate the complete
    primary achiral E graph XRVKCURQKFTZGG-UHFFFAOYSA-N and all exact source joins.
    CHEBI222154 MOL agrees but is only 2-star, and its default JSON SMILES is invalid;
    it is not an eligible current REPLACE_WITH_CHEBI target. A reviewed primary-graph
    consumer with exact original/candidate hashes, formula/valence/Standard/fixed-H
    checks and collision guards is required if adopted. Do not simply substitute the
    invalid JSON or keep PubChem134814868 as an exact corrected xref. Preserve native
    F001 isolation at the actual named-E graph resolution and adjudicate its old-key
    occurrence independently. Preserve the complete raw source row and original source
    mint. Any graph correction must independently adjudicate old-key LOTUS triples,
    assays, external identifiers, eligible ChEBI joins and filing/classification;
    no old-key data is automatically transferred. Any required strain/reference overlay
    composition must be implemented and tested because current consumers reject structure_correction_note.
    Preserve positive biological source claims at their demonstrated congener/resolution.'
  generator: Maintained decision/consumer work followed by documented regeneration;
    no generated owner or raw-source edit.
  acceptance_checks:
  - Missing, duplicate or changed original rows and stale full-row hashes fail closed.
  - Candidate chemistry and any introduced target row are parsed and compared in Standard
    and fixed-H form, including all defined/undefined centres and alkene geometry;
    invalid default SMILES is not copied.
  - No source occurrence, assay, identifier or biological claim is migrated by name
    or authority majority.
  - Every adopted overlay and any required new composition path has focused consumed-route/regeneration
    tests and the normal strict/reference/history checks.
limitations:
- The root section inventories present claims and source routing; chemical identities,
  source-specific experiments, definition claims and optional-content assertions require
  their separately scoped scientific assessments.
- Original E assignment does not borrow the F/G cocrystal.
- Any future graph change requires explicit preservation and re-adjudication of old-key
  LOTUS, xrefs, classification and source joins.
- The frozen source packet preserves actual access times and explicit full-text/pixel
  scope; formal authoring does not imply new retrieval.
- No optional missing pathway, protein or activity entry is treated as a mandatory
  defect. Taxonomic namespace, computed classification and independent chemical authority
  checks are retained in their separate sections.
- Only the proposed maintained route and acceptance criteria are reported; no scientific
  record, source inventory, campaign or repository state was changed.
- Authority matches establish the representations actually returned at their retained
  access times; they are not independent experimental structure or absolute-hand determinations.
  Root and science sections separately assess organism, locus, classification and
  history claims.
- This is direct primary constitution evidence, not an authority vote. The original
  F/G co-crystal does not determine E. The source reports its mass values as published;
  no forced agreement is imposed. No complete record replacement or old-key biological/occurrence
  migration is authorized by this source packet.
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
