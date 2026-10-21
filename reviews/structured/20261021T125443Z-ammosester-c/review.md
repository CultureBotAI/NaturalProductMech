# Ammosester C: product-specific methods and representation

- Review: 20261021T125443Z-ammosester-c
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-21T12:40:26.558982Z
- Finished UTC: 2026-10-21T12:54:43.311577Z
- Reviewer: Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The primary lactam and stored hydroxyl/imino form have the same heavy-atom constitution but different Standard InChIKeys, requiring an explicit representation decision and exact-key join safeguards. Native-organism deletion supports C production in the tested engineered background; replace the inherited enzyme method, which directly forms B, and qualify the production strain.

## Scope And Provenance

One complete generated owner and any referenced components, assessed claim by claim for exact identity, provenance, origin, producer and occurrence scope, biosynthesis, classification, optional content and audit history.

Selection: Campaign record 66, batch 007, selected in path order from the fresh-main authoritative validated catalogue and the separately validated pending-PR targets. At selection, 114 of 3116 current records had campaign coverage and 3002 remained. The population search included ignored files. Exactly one target is assessed here.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1c2402097718c138b081e00943de8f04de0541cd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-695cae6453 | data/natural_products/alkaloids/ammosester-c.yaml | generated | ammosester C |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Closed-schema target validation | passed | True | naturalproductmech:mibig-695cae6453 | The documented target strict validator completed; scientific support is assessed separately. |
| Corpus path and filing integrity | passed | True | naturalproductmech:mibig-695cae6453 | All 3,116 current record files agree with PATHS.tsv and their pinned filing pathways. |
| Corpus reproduction | passed | True | naturalproductmech:mibig-695cae6453 | All 3,116 current records passed the documented byte-reproduction gate against committed inventories and maintained curation inputs. |
| Native deterministic review queue | passed | True | naturalproductmech:mibig-695cae6453 | The exhaustive review queue produced 8,928 diagnostic rows across 12 queues; this deterministic output does not establish scientific review. |
| Configured ontology identifier-label correspondence | passed | True | naturalproductmech:mibig-695cae6453 | The configured identifier-label gate passed using the existing ontology caches: 13,449 canonical matches, 646 synonym matches, 35 documented exceptions, 499 warning-only mismatches and 4,744 pairs skipped because their prefixes have no adapter. |
| Full repository quality gate on the current main baseline | passed | True | naturalproductmech:mibig-695cae6453 | The full documented just qc recipe passed on the unchanged main baseline during batch004. Test summary: 999 passed, 4 skipped, 2 warnings in 441.24s (0:07:21). All configured lint, governance, documentation, provenance, source-queue, schema, rendering, reproduction, filing-integrity and reporting stages completed successfully. |
| Complete owner and component scope | passed | True | naturalproductmech:mibig-695cae6453 | The complete owner and all present fields were read. The parsed component-reference set is empty, so no referenced component was omitted. All existing inspection input hashes still match. |
| Required primary body and original supplementary experiment access | passed | True | naturalproductmech:mibig-695cae6453 | The full cited main body and official SI are available and inspected for exact identity, culture, deletion and enzyme endpoints. No required primary-access gap remains in this science scope; raw NMR spectra were not independently re-elucidated. |
| Exact-product producer/locus method and strain representation | failed | True | naturalproductmech:mibig-695cae6453 | The inherited Enzymatic assays label is not the demonstrated method for exact C: purified Ame24 produces B (22). Exact C (23) is lost in the native-organism SB18003 Δame24 derivative relative to SB18002. The appropriate product-specific method is Knock-out studies, which also resolves the undergraded producer claim under the repository policy, provided the engineered native strain context is retained. |
| Molecular graph and current xref reconstruction | passed | True | naturalproductmech:mibig-695cae6453 | Owner and current NPAtlas agree exactly; the independent primary-to-owner atom map establishes the microstate difference without a constitutional mismatch. |
| Documented source-to-owner chemical representation | failed | True | naturalproductmech:mibig-695cae6453 | The owner does not qualify the established primary versus stored microstate distinction. A cited representation policy/discussion is required; any key-changing repair needs guarded implementation. |

## Scientific And Domain Assessments

### Native status and retained seed history

provenance: supported. Targets: naturalproductmech:mibig-695cae6453.

The 3 dated seed events and SEEDED status describe generated provenance. This review does not relabel the owner REVIEWED or treat seed history as scientific approval. The latest 2026-10-13 event is another source-and-table seed event, not scientific sign-off.

### Optional mechanism and application content

completeness: not_applicable. Targets: naturalproductmech:mibig-695cae6453.

The owner has no structured pathway steps, causal edges, organism-specific proteins, molecular-target items, bioactivity rows or synthetic-biology applications. Their absence alone is not a defect in this source-generated record. No enzyme, target, activity or engineering claim is inferred from the name or chemical class.

### Structured transcriptomic context

completeness: not_applicable. Targets: naturalproductmech:mibig-695cae6453.

No exact named native producer and strain is covered by the inspected iModulonDB dataset catalogue. E. coli used as a recombinant expression host in source experiments does not supply native-producer expression context; genus-only occurrences cannot identify a covered species or strain. No applicable module query follows from these records. This bounded coverage limit is not negative evidence about production or function.

### Published exact compound and representation boundary

identity: supported. Targets: naturalproductmech:mibig-695cae6453.

Compound 23 is the N-desmethyl analog of B: neutral C12H9ClN4O3, with an N-1 H and C-2 lactam in the primary Figure 2C/SI S16. Main Table 1 and the reported HMBC correlations from 1-NH corroborate that depiction. The current owner has the same heavy-atom connectivity and charge but a different lactim/imino microstate with a different Standard InChIKey; this is a tautomeric representation issue, not a constitutional-isomer substitution. No tetrahedral stereocentre is present. Chemical authority and any representation repair are independently handled in the identifier packet.

### Exact species occurrence and natural-origin scope

evidence: supported. Targets: naturalproductmech:mibig-695cae6453.

The sole LOTUS DOI and producer/locus PMID are aliases for the same 2021 study. Positive culture isolation of compound 23 from the native-organism derivative supports the S. uncialis occurrence. Preserve the proposed downstream oxidation and engineered culture context without treating them as proof of synthetic origin or unmodified wild-type production.

### Product-specific genetic and biochemical support

evidence: concern. Targets: naturalproductmech:mibig-695cae6453.

The inherited Enzymatic assays label is not the demonstrated method for exact C: purified Ame24 produces B (22). Exact C (23) is lost in the native-organism SB18003 Δame24 derivative relative to SB18002. The appropriate product-specific method is Knock-out studies, which also resolves the undergraded producer claim under the repository policy, provided the engineered native strain context is retained.

### Upstream model, nonenzymatic proposal and optional enrichments

completeness: supported. Targets: naturalproductmech:mibig-695cae6453.

No missing optional pathway or protein finding is warranted. Any enrichment must preserve direct product endpoints, tagged construct scope, absence of rescue in the inspected experiment, and the proposed upstream scaffold-peptide chemistry. OTHER/RIBOSOMAL source classification and the NPClassifier labels are not independent precursor or catalytic experiments.

### Consumed guarded method and strain decisions

ownership: supported. Targets: naturalproductmech:mibig-695cae6453.

Use exact compound-specific maintained method, citation-guard and strain inputs. These recommendations were checked against the current consumers, but no corpus regeneration or correction fixture was run in this science review. If a chemical correction is composed with these inputs, first resolve and test the loader rejection rather than removing drift guards.

### Versioned source concepts, exact joins and eligible grounding

provenance: supported. Targets: naturalproductmech:mibig-695cae6453.

Source-concept identifiers are reproducibly minted from MIBIG plus accession:compound_index, not a chemical graph. Complete raw-row digests and versioned current source entries are retained. The exact-key committed eligible ChEBI projection is empty, and current matching ChEBI entries are two-star; no three-star replacement or asserted ontology class is inferred.

### Predicted classification and source BGC class

provenance: supported. Targets: naturalproductmech:mibig-695cae6453.

The owner filing and NPClassifier superclass/class output preserve the exact-key model version and source values. BGC classes are separate MIBiG assertions. Their presence does not prove a mechanism, and two-star authority classes/roles are not silently admitted.

### Chemical entity and source-organism namespaces

scope: supported. Targets: naturalproductmech:mibig-695cae6453.

The current LOTUS chemical Wikidata entity retains the owner full key, while organism Q103811340 maps to NCBI1048205 Streptomyces uncialis. The deposited DCA2648 genome context does not establish that the engineered experimental genotype is wild type; that scientific boundary is assessed separately.

### Primary depicted microstate versus stored authority form

representation: concern. Targets: naturalproductmech:mibig-695cae6453.

C uses VMGBZXKKNNEJRM while the primary depicted lactam is JVRCXQRBYCAUKV. Explicit atom mapping shows identical heavy-atom constitution; the key discrepancy is a hydrogen/bond-order representation difference, not a different carbon/nitrogen skeleton.

## Findings

### S066-F-METHODS: Replace the inherited enzyme label with exact ammosester C deletion evidence

major / open / confirmed; issue key: mibig-bgc0002343-compound3-method-scope.

The inherited Enzymatic assays label is not the demonstrated method for exact C: purified Ame24 produces B (22). Exact C (23) is lost in the native-organism SB18003 Δame24 derivative relative to SB18002. The appropriate product-specific method is Knock-out studies, which also resolves the undergraded producer claim under the repository policy, provided the engineered native strain context is retained. The species-level label also omits the experimental SB18002 strain context; include that context in the same repair. This finding does not change chemical identity or transfer other congener experiments.

### C066-F-MICROSTATE: The primary and stored microstates need explicit qualification

major / open / confirmed; issue key: ammosester-c-microstate.

The primary lactam drawing and stored hydroxyl/imino representation have different Standard keys, JVRCXQRBYCAUKV-UHFFFAOYSA-N and VMGBZXKKNNEJRM-UHFFFAOYSA-N, despite the same element-labelled heavy-atom connectivity, neutral formula and charge. The undocumented distinction materially affects exact-key occurrence/authority joins.

## Recommended Actions And Acceptance Checks

### S066-ACTION-METHODS

Add an attributed REPLACE in curation/mibig_locus_evidence_overrides.tsv for naturalproductmech:mibig-695cae6453, source MIBIG, source_id BGC0002343 and exact source_label ammosester C. Set exactly Knock-out studies. REPLACE does not enforce its expected_* columns, so they are not sufficient drift protection. Pair it with the consumed claim-reference row for BGC0002343:3, expected_source_row_sha256 796a5df9fbca18ef80d0b5322e744eda5d056cf3a53aaa9ad1c4ec760296aa7a, producer_reference and locus_reference PMID:33982054, source_reference DOI:10.1093/jimb/kuab027, and curator/date/rationale. Add the separately consumed producer-strain row with the same source ID/SHA and strain SB18002 (DCA2648 ΔclaO-D::scar). The method decision changes grades; the citation/strain decisions only supply guards and attributed context. Exact proposed field dictionaries are retained in science-proposed-inputs.json. If a structure correction is also adopted, extend and test the composition contract before attempting the paired citation correction, which currently rejects structure-corrected rows; the strain qualification path also rejects them.

- Match the untouched full BGC0002343:3 source row SHA 796a5df9fbca18ef80d0b5322e744eda5d056cf3a53aaa9ad1c4ec760296aa7a; reject stale, duplicate, missing and unconsumed decisions before output. Exercise complete raw-row drift rejection through the paired consumed guard, or implement and test equivalent REPLACE context guards before using that alternative.
- Emit exactly Knock-out studies with BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED, qualified to the tested SB18002/SB18003 background. Do not add whole-cluster heterologous production or a rescue experiment.
- Retain taxon 1048205, raw source version 3, LFBV01000006.1:293360..323959, stable owner/path and the valid species occurrence. Preserve current chemistry unless the separately adjudicated identifier action explicitly changes its microstate; do not let a method change silently migrate structures.
- Keep DCA2648 deposited-source metadata separate from SB18002 production and SB18003 deletion context. E. coli BL21(DE3) is the recombinant protein host, not an asserted natural producer.
- If combined with a structure decision, add focused tests for guarded composition and source drift; do not bypass correct_claim_reference rejection or drop the complete raw-row digest.
- Inspect the regenerated canary diff, run focused contract tests and required strict/reproduction/repository gates. Proposed input dictionaries and static consumer inspection are not evidence that these gates have run.

### C066-A-MICROSTATE

First add a cited curator-owned representation discussion, preserving both original primary and source graphs, explicit atom mapping, Standard/fixed-H keys and the limits of tautomer normalization; use the validated writer and a truthful curation event. Pin original BGC0002343:3 version3 and full-row SHA 796a5df9fbca18ef80d0b5322e744eda5d056cf3a53aaa9ad1c4ec760296aa7a. Do not declare a constitutional isomer or silently choose a source by majority. If policy adjudication requires a changed stored graph, extend the maintained correction schema/loader with a specifically supported primary-graph representation action: pin source row, primary snapshot, explicit valid target graph and calculated full/fixed-H fields; current REPLACE_WITH_CHEBI cannot use a two-star target. Recheck complete corpus target-key collisions and regenerate joins from the chosen exact representation; retain original source provenance and do not transfer old-key LOTUS, Cyano, NPClassifier or sibling links automatically. Compose this decision with the independent method, strain and citation repairs in one tested transform: existing claim-reference and strain applications reject structure_correction_note, so current tables cannot simply be stacked. The separately recommended method REPLACE must retain its full original source-row guard and the producer/locus assertions.

- The discussion states equal heavy-atom constitution and preserves different hydrogen/bond-order placement, formula, charge, Standard and fixed-H keys.
- No two-star ChEBI entry is promoted to eligible grounding and no current invalid default SMILES is copied.
- Any representation change rejects stale source/target pins, checks collisions and proves reproducible exact-key joins; it composes safely with method/strain/reference actions.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R066-OWNER | data/natural_products/alkaloids/ammosester-c.yaml; Complete owner YAML, including every history entry, source claim and discussion | supports | Root read the complete ammosester C owner after its individual intake. It has 1 MIBiG source concepts, 1 occurrence entries, 1 producers and 1 loci. There are no inline or referenced mechanism graphs, pathway steps, molecular targets, bioactivity rows or synthetic-biology applications in this owner. The complete parsed owner was inspected; ignored-file filters were not used to infer field absence. |
| R066-LOCAL-SOURCES | /private/tmp/npm-review-work/066/local-sources.json; Complete target-specific MIBiG, LOTUS, CyanoMetDB, ChEBI and NPClassifier slices | context_only | Root read every matching local source row and compared it with the complete emitted owner. The separate scientific and identifier assessments decide claim support; deterministic reproduction does not establish primary evidence. |
| R066-IMODULON-DATASETS | /private/tmp/npm-review-work/010/imodulon-datasets.txt; Complete 28-row dataset catalogue; actual command receipt in 010/imodulon-context-receipts.json | context_only | The successful structured-adapter catalogue retrieved at 07:21:15 UTC was fully re-read. Its 28 datasets contain no Fischerella, Azotobacter, Kamptonema/Oscillatoria, Vibrio anguillarum or V. campbellii, Streptomyces uncialis, S. hygrospinosus or S. venezuelae dataset. The Streptomyces entries are S. albidoflavus and S. coelicolor; the Vibrio entries are V. natriegens. A genus-level occurrence does not justify substituting a different species. This same-session catalogue retains its original retrieval time; a fresh request is not claimed. |
| S066-OWNER | data/natural_products/alkaloids/ammosester-c.yaml; Entire owner YAML, resolved owner and complete local source rows | supports | The exact owner imports BGC0002343:3 version 3, S. uncialis taxon 1048205, LFBV01000006.1:293360..323959 and PMID:33982054. It has no strain qualifier, carries Enzymatic assays, SOURCE_ASSERTION and CLUSTER_DEMONSTRATED, and one LOTUS occurrence citing DOI:10.1093/JIMB/KUAB027. The DOI and PMID identify the same study. No optional pathway, enzyme, reaction, molecular-target or activity claim is asserted. |
| S066-RAW | data/raw/mibig_compounds.tsv; Complete BGC0002343:3 raw compound row; publication compound number 23 differs from source compound index | supports | The complete source-row SHA256 is 796a5df9fbca18ef80d0b5322e744eda5d056cf3a53aaa9ad1c4ec760296aa7a. The source method is exactly Enzymatic assays; version, taxon, accession, bounds and full key VMGBZXKKNNEJRM-UHFFFAOYSA-N are retained as old-context guards. This is a faithful import of entry-level evidence, requiring exact-product adjudication. |
| S066-IDENTITY | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/fullTextXML; Complete original main; structural-elucidation Results for compound 23; Table 1; Figure 2C | supports | Compound 23 is the N-desmethyl analog of B: neutral C12H9ClN4O3, with an N-1 H and C-2 lactam in the primary Figure 2C/SI S16. Main Table 1 and the reported HMBC correlations from 1-NH corroborate that depiction. The current owner has the same heavy-atom connectivity and charge but a different lactim/imino microstate with a different Standard InChIKey; this is a tautomeric representation issue, not a constitutional-isomer substitution. No tetrahedral stereocentre is present. |
| S066-SI-IDENTITY | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/supplementaryFiles; Official SI: original Figure S5 on S16; compound 23 NMR/MS section located; Table S1 on S2 | supports | The original numbered drawing and HMBC summary for compound 23 were inspected. All SI text was read; its raw spectral panels were located rather than independently reassigned. The original main reports isolation of 3 mg from the 10-L SB18002 fermentation. This is positive product-specific isolation evidence, not a generic ammosamide-family citation. |
| S066-CULTURE | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/fullTextXML; Methods: strains, fermentation and compound isolation; first Results subsection | supports | The wild-type source strain is S. uncialis DCA2648, but isolation of exact compound 23 was from SB18002, engineered by deleting the cladoniamide cluster to reveal the minor metabolites. The paper calls the isolated compounds natural products. This is a derivative of the native organism, not whole-cluster heterologous synthesis and not direct evidence that unmodified DCA2648 was chemically assayed for every congener. |
| S066-GENETICS | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/supplementaryFiles; Table S1 on S2; original Figure S7A–C on S18, Southern blot and HPLC traces | supports | SB18002 is ΔclaO-D::scar. SB18003 is its Δame24::aac(3)IV derivative, made by double-crossover replacement. The original Southern image shows the stated 6.5-kb parental and 1.4-kb mutant bands. HPLC at 540 nm shows 21–23 absent while 24 remains. Thus exact compound 23 is lost in the tested mutant, supporting a native-organism knockout endpoint in this engineered background. No rescue experiment or heterologous full-cluster production is reported in this inspected experiment. |
| S066-ASSAY | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/fullTextXML; Complete in-vitro assay Methods and Ame24 Results; Figure 2B | supports | N-terminal His6-Ame24 was produced in E. coli BL21(DE3), purified and assayed with 200 µM acid 24, 500 µM SAM and 200 µM enzyme in 50 mM Tris, pH 7.5, at 30 °C. The new product is exact B (22), identified by HPLC–MS against an authentic standard; boiled Ame24 is the negative control. This proves 24 consumption and 22 formation. It does not directly demonstrate formation of 21, 23 or 24, nor a complete pathway in E. coli. |
| S066-SI-ASSAY | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/supplementaryFiles; Original Figure S8A–C on S19; Table S3 on S3 | supports | The original S19 drawing labels acid 24 as substrate and B (22) as product. The gel caption describes the retained N-His6 construct as 309 amino acids; Table S3 tabulates native Ame24/AB852_RS23910 as 286 amino acids. The SI reports 5.7% conversion at 2 h and 20.1% at 18 h, while the main says about 6% and 12%. The exact-product endpoint is clear, but the 18-hour quantitative discrepancy must not be silently resolved. |
| S066-PATHWAY | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/fullTextXML; Unified-pathway Results; original Figure 3; final fermentation-time-course paragraph | context_only | The proposed scaffold-peptide route, Ame22 chemistry and methylation order are hypotheses in this source. The time course has B (22) dominant at day 4, A (21) dominant at day 6, then declining A with increasing B and appearance of 23/24. The authors propose A as the final enzymatic product and 22–24 as C-2-oxidized products, potentially nonenzymatic. They could not obtain proposed free-acid substrates 17/26 to establish the preferred Ame24 substrate or reaction order. Culture isolation remains positive; this proposal does not itself justify a SYNTHETIC label or prove every nonenzymatic conversion. |
| S066-ACTIVITY | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/fullTextXML; Exact compound-specific Table 2 and cytotoxicity Methods | context_only | Exact C (23) has EC50 &gt;200 µM in all five tested human cancer cell lines; do not transfer A/B activity. These are optional enrichment candidates, not defects in an owner without an activity claim. |
| S066-LOCUS | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=LFBV01000006.1&amp;seq_start=293360&amp;seq_stop=323959&amp;rettype=gbwithparts&amp;retmode=text; Bounded LFBV01000006.1 source/header and feature window 293360..323959 | supports | The 30,600-bp window identifies S. uncialis DCA2648, taxon 1048205. It is a source-genome bridge, not a deposited SB18002 engineered genome. Automated legacy CDS annotations do not by themselves establish exact assay-construct sequences or experimental cluster endpoints. No complete protein translation comparison is claimed. |
| S066-MICROSTATE | /private/tmp/npm-review-work/shared-next-batch007/authorities/ammosester-microstates/comparison.json; Explicit numbered primary-to-authority 20-heavy-atom adjacency/bond-order/hydrogen comparison | supports | Primary lactam JVRCXQRBYCAUKV-UHFFFAOYSA-N and current source VMGBZXKKNNEJRM-UHFFFAOYSA-N share all 20 heavy atoms and 22 heavy-atom adjacencies. Differences are hydrogen locations and pi-bond orders; both are neutral. This is tautomeric representation, not changed heavy-atom connectivity or a salt/cation mismatch. The identifier packet owns any exact structure or authority correction. |
| S066-METHOD-CONSUMER | scripts/seed_from_sources.py; load/apply_mibig_locus_evidence_overrides; build_records composition and emitted producer/locus grades | supports | WITHDRAW enforces seven old-context fields against the raw source and allows empty replacement methods. REPLACE requires nonempty recognized methods but does not enforce expected_* context fields; pair it with a consumed complete-raw-row-SHA decision or first implement equivalent tested guards. Knock-out studies yields BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED; Enzymatic assays alone yields SOURCE_ASSERTION/CLUSTER_DEMONSTRATED. |
| S066-REFERENCE-GUARD | src/naturalproductmech/curate/claim_references.py; Complete loader and correct_claim_reference implementation | supports | The consumed claim-reference table requires the exact BGC accession:compound index and full raw-row digest; it rejects stale, duplicate or ambiguous matches and records separate CURATOR_INFERENCE attribution. Same PMID values can be retained while the adjudication rationale identifies the distinct method decision. It rejects rows with structure_correction_note, so a combined structure/claim-reference correction requires an explicit tested composition change rather than assuming existing compatibility. |
| S066-STRAIN-CONSUMER | src/naturalproductmech/curate/producer_strains.py; Complete producer strain/isolate qualification contract | supports | A curation/mibig_producer_strains.tsv row selects the exact accession:compound index, guards the full untouched raw-row SHA and emits an attributed strain qualifier. It changes neither taxon nor grade by itself. The seeder also rejects strain qualification on a row with structure_correction_note. This is the effective route for SB18002 (DCA2648 ΔclaO-D::scar) production context; raw genome metadata remains DCA2648. |
| C066-OWNER | data/natural_products/alkaloids/ammosester-c.yaml; Complete owner and resolved source projection | supports | The owner identifies ammosester C with full key VMGBZXKKNNEJRM-UHFFFAOYSA-N; exact source rows, xrefs, source concepts and classification were read. |
| C066-RAW | data/raw/mibig_compounds.tsv; Complete relevant raw rows and local exact-key inventories | supports | Exact source row SHA-256 values: BGC0002343:3 = 796a5df9fbca18ef80d0b5322e744eda5d056cf3a53aaa9ad1c4ec760296aa7a. Digests cover every column using canonical sorted JSON. Complete exact-key eligible ChEBI projection has 0 row(s). |
| C066-CLASS | data/raw/npclassifier.tsv; Exact-key classification row and owner attribution | context_only | The filing and NPClassifier superclass/class outputs are attributed to the pinned model version. MIBiG biosynthetic classes remain a separate source axis; current authority ontology relations are not silently promoted into asserted corpus classes. |
| C066-SEARCH | /private/tmp/npm-review-work/066/chemistry-local-search.txt; Complete matching path list | supports | Ignored-inclusive search checks the exact full key, current slug and target ID across current owners, curation, configuration and source code. Exact raw inventory rows were separately parsed. This bounded search does not claim universal absence. |
| C066-NPA | https://www.npatlas.org/api/v1/compound/NPA033060; Complete exact identity, identifier, provenance and relevant source fields | supports | NPA033060 resolves in the NPAtlas compound namespace. Its complete identity, structure history and origin-reference fields were read; current formula C12H9ClN4O3 and full key VMGBZXKKNNEJRM-UHFFFAOYSA-N. Exact graph results are retained in the independent comparison. |
| C066-PC | https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/VMGBZXKKNNEJRM-UHFFFAOYSA-N/JSON; Complete exact identity, identifier, provenance and relevant source fields | supports | PubChem Compound CID 135878873 resolves for the exact-key query. Identity properties and the complete atom/bond/stereo representation are retained; CID is not a Substance SID. |
| C066-CHEBI-SEARCH | https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=VMGBZXKKNNEJRM-UHFFFAOYSA-N&amp;size=100; Complete exact identity, identifier, provenance and relevant source fields | supports | Bounded exact full-key ChEBI query and returned candidate list inspected. The returned two-star entry is not a three-star eligible grounding; no global absence claim is made. |
| C066-CHEBI | https://www.ebi.ac.uk/chebi/backend/api/public/compound/221166/; Complete exact identity, identifier, provenance and relevant source fields | supports | Current CHEBI:221166 is 2-star and therefore is outside this repository's three-star eligibility rule. Complete identity, default structure, origins and ontology relations were inspected. Its public entry is not an eligible replacement solely because its key matches. |
| C066-CHEBI-MOL | https://www.ebi.ac.uk/chebi/backend/api/public/molfile/221166/; Complete exact identity, identifier, provenance and relevant source fields | supports | The official MOL was parsed independently, without editing. It supplies the representation comparison; agreement of a MOL does not validate a contradictory default SMILES. |
| C066-CALC | /private/tmp/npm-review-work/066/chemistry-authority-comparison.json; Fresh full Standard and fixed-H graph comparison, charge, formula and every tetrahedral centre | supports | Owner, NPAtlas, PubChem and official ChEBI MOL reconstruct to VMGBZXKKNNEJRM-UHFFFAOYSA-N. Full Standard and fixed-H InChI, formula, charge and assigned/undefined centres are retained per representation. Default ChEBI SMILES is separately tested and is not silently repaired. |
| C066-WD-Q103811340 | https://www.wikidata.org/wiki/Special:EntityData/Q103811340.json; Complete exact identity, identifier, provenance and relevant source fields | supports | Current LOTUS-linked Wikidata entity: {"qid": "Q103811340", "label": "Streptomyces uncialis", "P235": [], "P234": [], "P2017": [], "P685": ["1048205"], "P225": ["Streptomyces uncialis"]}. Chemical and organism namespaces are kept distinct; this resolution is not primary occurrence evidence. |
| C066-WD-Q113959004 | https://www.wikidata.org/wiki/Special:EntityData/Q113959004.json; Complete exact identity, identifier, provenance and relevant source fields | supports | Current LOTUS-linked Wikidata entity: {"qid": "Q113959004", "label": "Methyl 11-amino-10-chloro-3-hydroxy-9-imino-2,7-diazatricyclo[6.3.1.04,12]dodeca-1,3,5,8(12),10-pentaene-6-carboxylate", "P235": ["VMGBZXKKNNEJRM-UHFFFAOYSA-N"], "P234": ["InChI=1S/C12H9ClN4O3/c1-20-12(19)4-2-3-5-9(16-4)7(14)6(13)8(15)10(5)17-11(3)18/h2,14,16,18H,15H2,1H3"], "P2017": [], "P685": [], "P225": []}. Chemical and organism namespaces are kept distinct; this resolution is not primary occurrence evidence. |
| C066-MIBIG-BGC0002343 | https://mibig.secondarymetabolites.org/repository/BGC0002343.3/annotations.json; Complete exact identity, identifier, provenance and relevant source fields | supports | BGC0002343 version 3 resolves as active, with quality questionable and completeness unknown. Complete compounds, source taxonomy, loci and methods were inspected. The selected exact row matches the raw representation; source metadata is not independent experimental verification. |
| C066-TAX | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1930928,1283330,1048205,56108,354,230521&amp;retmode=xml; Relevant complete taxon records with rank, names, aliases and lineage | supports | NCBI1048205 resolves to Streptomyces uncialis at species rank. The deposited LFBV01000006.1 source is DCA2648. This is not itself an accession for the tested engineered SB18002 ΔclaO-D::scar genotype; source-locus and tested-culture scopes remain separate. |
| C066-GENBANK0 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=LFBV01000006.1&amp;seq_start=293360&amp;seq_stop=323959&amp;rettype=gbwithparts&amp;retmode=text; Header, source qualifiers and interval metadata; no protein translation assertion | supports | The exact accession version and requested bounded interval resolve. Header, reference and source-feature metadata support the deposited organism/strain bridge only. The entire chromosome was not downloaded, and no historical stock, protein-sequence or experimentally delimited endpoint equivalence is inferred. |
| C066-PRIMARY | DOI:10.1093/jimb/kuab027; Official SI S16 Figure S5, exact compound 23 | supports | Original primary drawing 23 gives C12H9ClN4O3, charge 0, Standard key JVRCXQRBYCAUKV-UHFFFAOYSA-N and fixed-H key JVRCXQRBYCAUKV-HCKMINDGNA-N. Original pixels and numbered graph transcription were compared; no inferred solution population or new experimental structure determination is claimed. |
| C066-PRIMARY-CALC | /private/tmp/npm-review-work/066/chemistry-primary-comparison.json; Fresh parsing of source-labelled molecular graph versus owner | supports | Complete formula/charge/Standard/fixed-H comparison is retained with the literal primary graph input. It is interpreted with the actual source pixels, not merely compound labels. |
| C066-MICROSTATE | /private/tmp/npm-review-work/shared-next-batch007/authorities/ammosester-microstates/comparison.json; Unique element-labelled heavy-atom mapping and explicit hydrogen/bond-order differences | supports | Both forms have the same unique heavy-atom adjacency mapping, formula and charge. For A, N5 gains H and the C6 amino group loses H in the authority representation; Standard keys match but fixed-H keys differ, and default RDKit tautomer canonicalization does not converge. For C, the source lactam versus authority hydroxyl/imino form shifts N1 to O2 H and C6 amino to N5 H with pi-bond changes; Standard keys differ despite equal heavy-atom connectivity, while RDKit canonical tautomers converge. These are representational observations, not measured microstate populations. |

## Limits And Additional Notes

- This review audits the present assertions and the concrete source questions they raise; it does not claim exhaustive discovery of every later activity or biosynthetic study. Optional enrichment remains distinct from correcting an unsupported current assertion.
- The cited main and official SI are available; the review does not independently reassign every raw NMR peak or reconstruct complete tagged-protein sequences. Original main and SI disagree on the 18-hour Ame24 conversion yield (about 12% versus 20.1%), so only the supported direction and exact endpoint are relied upon.
- The paper proposes nonenzymatic C-2 oxidation and parallel methylation routes. It directly establishes culture occurrence and the specified deletion/assay endpoints, not every upstream step or preferred native reaction order. No automatic synthetic-origin reassignment follows from the proposal.
- GenBank source metadata bridge the DCA2648 genome window; legacy annotation alone does not prove experimental cluster endpoints, exact current RS-tag equivalence or identity of the 309-aa tagged assay construct. These unasserted protein claims are outside this bounded owner review.
- Maintained actions are recommendations only. A method/strain/citation composition can conflict with a separately proposed structure correction; the existing rejection must be addressed with a tested contract, not bypassed.
- The authority snapshots and depicted graphs establish representation, not pH-dependent microstate populations or equilibrium. Experimental genotype, deletion phenotypes and enzyme-substrate/product scope are assessed separately.
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
review_id: 20261021T125443Z-ammosester-c
title: 'Ammosester C: product-specific methods and representation'
started_at: '2026-10-21T12:40:26.558982Z'
finished_at: '2026-10-21T12:54:43.311577Z'
completion: completed
verdict: needs_curation
scientific_review: true
summary: The primary lactam and stored hydroxyl/imino form have the same heavy-atom
  constitution but different Standard InChIKeys, requiring an explicit representation
  decision and exact-key join safeguards. Native-organism deletion supports C production
  in the tested engineered background; replace the inherited enzyme method, which
  directly forms B, and qualify the production strain.
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
  - path: data/natural_products/alkaloids/ammosester-c.yaml
    sha256: 4df748e42b978453f42e5f820fa00f9cffbc301b141d1d3326560633a94ead04
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
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
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
  selection: Campaign record 66, batch 007, selected in path order from the fresh-main
    authoritative validated catalogue and the separately validated pending-PR targets.
    At selection, 114 of 3116 current records had campaign coverage and 3002 remained.
    The population search included ignored files. Exactly one target is assessed here.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - naturalproductmech:mibig-695cae6453
targets:
- target_id: naturalproductmech:mibig-695cae6453
  path: data/natural_products/alkaloids/ammosester-c.yaml
  label: ammosester C
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
  - naturalproductmech:mibig-695cae6453
  command: just validate-strict data/natural_products/alkaloids/ammosester-c.yaml
    --out /private/tmp/npm-review-work/066/strict.tsv
  exit_code: 0
  scope_note: Actual command finished 2026-10-21T12:40:29.043960Z
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
    for batch007 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch007. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-695cae6453
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
    Reused for batch007 only after a fresh fetch/clean branch, equal commit/tree and
    two reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch007. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-695cae6453
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
    for batch007 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch007. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-695cae6453
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
    for batch007 only after a fresh fetch/clean branch, equal commit/tree and two
    reads of all 9,182 tracked byte streams and modes (208,070,649 bytes), including
    a recheck after the fresh authoritative catalogue. This gate was not rerun for
    batch007. Original execution times, scope, warnings, exceptions and skips are
    retained.'
  target_ids:
  - naturalproductmech:mibig-695cae6453
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
    transcript: /private/tmp/npm-native-checks/batch-004/qc.log. Reused for batch007
    only after a fresh fetch/clean branch, equal commit/tree and two reads of all
    9,182 tracked byte streams and modes (208,070,649 bytes), including a recheck
    after the fresh authoritative catalogue. This gate was not rerun for batch007.
    Original execution times, scope, warnings, exceptions and skips are retained.'
  target_ids:
  - naturalproductmech:mibig-695cae6453
- check_id: R066-FULL-OWNER
  name: Complete owner and component scope
  status: passed
  required: true
  summary: The complete owner and all present fields were read. The parsed component-reference
    set is empty, so no referenced component was omitted. All existing inspection
    input hashes still match.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - R066-OWNER
  - R066-LOCAL-SOURCES
- check_id: S066-C-PRIMARY
  name: Required primary body and original supplementary experiment access
  status: passed
  required: true
  summary: The full cited main body and official SI are available and inspected for
    exact identity, culture, deletion and enzyme endpoints. No required primary-access
    gap remains in this science scope; raw NMR spectra were not independently re-elucidated.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - S066-IDENTITY
  - S066-SI-IDENTITY
  - S066-CULTURE
  - S066-GENETICS
  - S066-ASSAY
  - S066-SI-ASSAY
- check_id: S066-C-METHODS
  name: Exact-product producer/locus method and strain representation
  status: failed
  required: true
  summary: 'The inherited Enzymatic assays label is not the demonstrated method for
    exact C: purified Ame24 produces B (22). Exact C (23) is lost in the native-organism
    SB18003 Δame24 derivative relative to SB18002. The appropriate product-specific
    method is Knock-out studies, which also resolves the undergraded producer claim
    under the repository policy, provided the engineered native strain context is
    retained.'
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - S066-OWNER
  - S066-RAW
  - S066-CULTURE
  - S066-GENETICS
  - S066-ASSAY
  - S066-SI-ASSAY
  - S066-METHOD-CONSUMER
- check_id: C066-CHEM-CHECK
  name: Molecular graph and current xref reconstruction
  status: passed
  required: true
  summary: Owner and current NPAtlas agree exactly; the independent primary-to-owner
    atom map establishes the microstate difference without a constitutional mismatch.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - C066-CALC
  - C066-NPA
  - C066-PRIMARY-CALC
  - C066-MICROSTATE
- check_id: C066-REPRESENTATION-CHECK
  name: Documented source-to-owner chemical representation
  status: failed
  required: true
  summary: The owner does not qualify the established primary versus stored microstate
    distinction. A cited representation policy/discussion is required; any key-changing
    repair needs guarded implementation.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - C066-OWNER
  - C066-PRIMARY-CALC
  - C066-MICROSTATE
evidence:
- evidence_id: R066-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/ammosester-c.yaml
  locator: Complete owner YAML, including every history entry, source claim and discussion
  accessed_at: '2026-10-21T12:44:40.142802Z'
  support: supports
  summary: Root read the complete ammosester C owner after its individual intake.
    It has 1 MIBiG source concepts, 1 occurrence entries, 1 producers and 1 loci.
    There are no inline or referenced mechanism graphs, pathway steps, molecular targets,
    bioactivity rows or synthetic-biology applications in this owner. The complete
    parsed owner was inspected; ignored-file filters were not used to infer field
    absence.
  snapshot_sha256: 4df748e42b978453f42e5f820fa00f9cffbc301b141d1d3326560633a94ead04
- evidence_id: R066-LOCAL-SOURCES
  kind: record_content
  reference: /private/tmp/npm-review-work/066/local-sources.json
  locator: Complete target-specific MIBiG, LOTUS, CyanoMetDB, ChEBI and NPClassifier
    slices
  accessed_at: '2026-10-21T12:44:40.142802Z'
  support: context_only
  summary: Root read every matching local source row and compared it with the complete
    emitted owner. The separate scientific and identifier assessments decide claim
    support; deterministic reproduction does not establish primary evidence.
  snapshot_sha256: 7d12631c4a6a8a5e131d8c0846263f633660a047491a45eaeae8c43f3df57547
- evidence_id: R066-IMODULON-DATASETS
  kind: database
  reference: /private/tmp/npm-review-work/010/imodulon-datasets.txt
  locator: Complete 28-row dataset catalogue; actual command receipt in 010/imodulon-context-receipts.json
  accessed_at: '2026-10-21T07:21:15.957321Z'
  support: context_only
  summary: The successful structured-adapter catalogue retrieved at 07:21:15 UTC was
    fully re-read. Its 28 datasets contain no Fischerella, Azotobacter, Kamptonema/Oscillatoria,
    Vibrio anguillarum or V. campbellii, Streptomyces uncialis, S. hygrospinosus or
    S. venezuelae dataset. The Streptomyces entries are S. albidoflavus and S. coelicolor;
    the Vibrio entries are V. natriegens. A genus-level occurrence does not justify
    substituting a different species. This same-session catalogue retains its original
    retrieval time; a fresh request is not claimed.
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
- evidence_id: S066-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/ammosester-c.yaml
  locator: Entire owner YAML, resolved owner and complete local source rows
  accessed_at: '2026-10-21T12:49:48.328076Z'
  support: supports
  summary: The exact owner imports BGC0002343:3 version 3, S. uncialis taxon 1048205,
    LFBV01000006.1:293360..323959 and PMID:33982054. It has no strain qualifier, carries
    Enzymatic assays, SOURCE_ASSERTION and CLUSTER_DEMONSTRATED, and one LOTUS occurrence
    citing DOI:10.1093/JIMB/KUAB027. The DOI and PMID identify the same study. No
    optional pathway, enzyme, reaction, molecular-target or activity claim is asserted.
  snapshot_sha256: 4df748e42b978453f42e5f820fa00f9cffbc301b141d1d3326560633a94ead04
- evidence_id: S066-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: Complete BGC0002343:3 raw compound row; publication compound number 23
    differs from source compound index
  accessed_at: '2026-10-21T12:49:48.328076Z'
  support: supports
  summary: The complete source-row SHA256 is 796a5df9fbca18ef80d0b5322e744eda5d056cf3a53aaa9ad1c4ec760296aa7a.
    The source method is exactly Enzymatic assays; version, taxon, accession, bounds
    and full key VMGBZXKKNNEJRM-UHFFFAOYSA-N are retained as old-context guards. This
    is a faithful import of entry-level evidence, requiring exact-product adjudication.
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: S066-IDENTITY
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/fullTextXML
  locator: Complete original main; structural-elucidation Results for compound 23;
    Table 1; Figure 2C
  accessed_at: '2026-10-21T12:07:16.520644Z'
  support: supports
  summary: 'Compound 23 is the N-desmethyl analog of B: neutral C12H9ClN4O3, with
    an N-1 H and C-2 lactam in the primary Figure 2C/SI S16. Main Table 1 and the
    reported HMBC correlations from 1-NH corroborate that depiction. The current owner
    has the same heavy-atom connectivity and charge but a different lactim/imino microstate
    with a different Standard InChIKey; this is a tautomeric representation issue,
    not a constitutional-isomer substitution. No tetrahedral stereocentre is present.'
  snapshot_sha256: ba8441b2ae4e375eeaebff2ca4bab03f4d59a93508738827d11c678e14e47432
- evidence_id: S066-SI-IDENTITY
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/supplementaryFiles
  locator: 'Official SI: original Figure S5 on S16; compound 23 NMR/MS section located;
    Table S1 on S2'
  accessed_at: '2026-10-21T12:07:17.239548Z'
  support: supports
  summary: The original numbered drawing and HMBC summary for compound 23 were inspected.
    All SI text was read; its raw spectral panels were located rather than independently
    reassigned. The original main reports isolation of 3 mg from the 10-L SB18002
    fermentation. This is positive product-specific isolation evidence, not a generic
    ammosamide-family citation.
  snapshot_sha256: 35863d9c6b8802b18361dc1b6f9f535192da02712d5f345905ff168ad06050f1
- evidence_id: S066-CULTURE
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/fullTextXML
  locator: 'Methods: strains, fermentation and compound isolation; first Results subsection'
  accessed_at: '2026-10-21T12:07:16.520644Z'
  support: supports
  summary: The wild-type source strain is S. uncialis DCA2648, but isolation of exact
    compound 23 was from SB18002, engineered by deleting the cladoniamide cluster
    to reveal the minor metabolites. The paper calls the isolated compounds natural
    products. This is a derivative of the native organism, not whole-cluster heterologous
    synthesis and not direct evidence that unmodified DCA2648 was chemically assayed
    for every congener.
  snapshot_sha256: ba8441b2ae4e375eeaebff2ca4bab03f4d59a93508738827d11c678e14e47432
- evidence_id: S066-GENETICS
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/supplementaryFiles
  locator: Table S1 on S2; original Figure S7A–C on S18, Southern blot and HPLC traces
  accessed_at: '2026-10-21T12:07:17.239548Z'
  support: supports
  summary: SB18002 is ΔclaO-D::scar. SB18003 is its Δame24::aac(3)IV derivative, made
    by double-crossover replacement. The original Southern image shows the stated
    6.5-kb parental and 1.4-kb mutant bands. HPLC at 540 nm shows 21–23 absent while
    24 remains. Thus exact compound 23 is lost in the tested mutant, supporting a
    native-organism knockout endpoint in this engineered background. No rescue experiment
    or heterologous full-cluster production is reported in this inspected experiment.
  snapshot_sha256: 35863d9c6b8802b18361dc1b6f9f535192da02712d5f345905ff168ad06050f1
- evidence_id: S066-ASSAY
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/fullTextXML
  locator: Complete in-vitro assay Methods and Ame24 Results; Figure 2B
  accessed_at: '2026-10-21T12:07:16.520644Z'
  support: supports
  summary: N-terminal His6-Ame24 was produced in E. coli BL21(DE3), purified and assayed
    with 200 µM acid 24, 500 µM SAM and 200 µM enzyme in 50 mM Tris, pH 7.5, at 30
    °C. The new product is exact B (22), identified by HPLC–MS against an authentic
    standard; boiled Ame24 is the negative control. This proves 24 consumption and
    22 formation. It does not directly demonstrate formation of 21, 23 or 24, nor
    a complete pathway in E. coli.
  snapshot_sha256: ba8441b2ae4e375eeaebff2ca4bab03f4d59a93508738827d11c678e14e47432
- evidence_id: S066-SI-ASSAY
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/supplementaryFiles
  locator: Original Figure S8A–C on S19; Table S3 on S3
  accessed_at: '2026-10-21T12:07:17.239548Z'
  support: supports
  summary: The original S19 drawing labels acid 24 as substrate and B (22) as product.
    The gel caption describes the retained N-His6 construct as 309 amino acids; Table
    S3 tabulates native Ame24/AB852_RS23910 as 286 amino acids. The SI reports 5.7%
    conversion at 2 h and 20.1% at 18 h, while the main says about 6% and 12%. The
    exact-product endpoint is clear, but the 18-hour quantitative discrepancy must
    not be silently resolved.
  snapshot_sha256: 35863d9c6b8802b18361dc1b6f9f535192da02712d5f345905ff168ad06050f1
- evidence_id: S066-PATHWAY
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/fullTextXML
  locator: Unified-pathway Results; original Figure 3; final fermentation-time-course
    paragraph
  accessed_at: '2026-10-21T12:07:16.520644Z'
  support: context_only
  summary: The proposed scaffold-peptide route, Ame22 chemistry and methylation order
    are hypotheses in this source. The time course has B (22) dominant at day 4, A
    (21) dominant at day 6, then declining A with increasing B and appearance of 23/24.
    The authors propose A as the final enzymatic product and 22–24 as C-2-oxidized
    products, potentially nonenzymatic. They could not obtain proposed free-acid substrates
    17/26 to establish the preferred Ame24 substrate or reaction order. Culture isolation
    remains positive; this proposal does not itself justify a SYNTHETIC label or prove
    every nonenzymatic conversion.
  snapshot_sha256: ba8441b2ae4e375eeaebff2ca4bab03f4d59a93508738827d11c678e14e47432
- evidence_id: S066-ACTIVITY
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8210675/fullTextXML
  locator: Exact compound-specific Table 2 and cytotoxicity Methods
  accessed_at: '2026-10-21T12:07:16.520644Z'
  support: context_only
  summary: Exact C (23) has EC50 >200 µM in all five tested human cancer cell lines;
    do not transfer A/B activity. These are optional enrichment candidates, not defects
    in an owner without an activity claim.
  snapshot_sha256: ba8441b2ae4e375eeaebff2ca4bab03f4d59a93508738827d11c678e14e47432
- evidence_id: S066-LOCUS
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=LFBV01000006.1&seq_start=293360&seq_stop=323959&rettype=gbwithparts&retmode=text
  locator: Bounded LFBV01000006.1 source/header and feature window 293360..323959
  accessed_at: '2026-10-21T12:25:21.288718Z'
  support: supports
  summary: The 30,600-bp window identifies S. uncialis DCA2648, taxon 1048205. It
    is a source-genome bridge, not a deposited SB18002 engineered genome. Automated
    legacy CDS annotations do not by themselves establish exact assay-construct sequences
    or experimental cluster endpoints. No complete protein translation comparison
    is claimed.
  snapshot_sha256: c857a8f56a107b9a04ea43b5563b5a8425a79abee9342bbfa942bb0f8bfb93d4
- evidence_id: S066-MICROSTATE
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch007/authorities/ammosester-microstates/comparison.json
  locator: Explicit numbered primary-to-authority 20-heavy-atom adjacency/bond-order/hydrogen
    comparison
  accessed_at: '2026-10-21T12:32:12.259351Z'
  support: supports
  summary: Primary lactam JVRCXQRBYCAUKV-UHFFFAOYSA-N and current source VMGBZXKKNNEJRM-UHFFFAOYSA-N
    share all 20 heavy atoms and 22 heavy-atom adjacencies. Differences are hydrogen
    locations and pi-bond orders; both are neutral. This is tautomeric representation,
    not changed heavy-atom connectivity or a salt/cation mismatch. The identifier
    packet owns any exact structure or authority correction.
  snapshot_sha256: 4217c58db1f1bc7966a1a84c9467dca8cbfdd81b09fcb335ea2c5147f6016d5f
- evidence_id: S066-METHOD-CONSUMER
  kind: record_content
  reference: scripts/seed_from_sources.py
  locator: load/apply_mibig_locus_evidence_overrides; build_records composition and
    emitted producer/locus grades
  accessed_at: '2026-10-21T12:49:48.328076Z'
  support: supports
  summary: WITHDRAW enforces seven old-context fields against the raw source and allows
    empty replacement methods. REPLACE requires nonempty recognized methods but does
    not enforce expected_* context fields; pair it with a consumed complete-raw-row-SHA
    decision or first implement equivalent tested guards. Knock-out studies yields
    BGC_CHARACTERIZED/CLUSTER_DEMONSTRATED; Enzymatic assays alone yields SOURCE_ASSERTION/CLUSTER_DEMONSTRATED.
  snapshot_sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
- evidence_id: S066-REFERENCE-GUARD
  kind: record_content
  reference: src/naturalproductmech/curate/claim_references.py
  locator: Complete loader and correct_claim_reference implementation
  accessed_at: '2026-10-21T12:49:48.328076Z'
  support: supports
  summary: The consumed claim-reference table requires the exact BGC accession:compound
    index and full raw-row digest; it rejects stale, duplicate or ambiguous matches
    and records separate CURATOR_INFERENCE attribution. Same PMID values can be retained
    while the adjudication rationale identifies the distinct method decision. It rejects
    rows with structure_correction_note, so a combined structure/claim-reference correction
    requires an explicit tested composition change rather than assuming existing compatibility.
  snapshot_sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
- evidence_id: S066-STRAIN-CONSUMER
  kind: record_content
  reference: src/naturalproductmech/curate/producer_strains.py
  locator: Complete producer strain/isolate qualification contract
  accessed_at: '2026-10-21T12:49:48.328076Z'
  support: supports
  summary: A curation/mibig_producer_strains.tsv row selects the exact accession:compound
    index, guards the full untouched raw-row SHA and emits an attributed strain qualifier.
    It changes neither taxon nor grade by itself. The seeder also rejects strain qualification
    on a row with structure_correction_note. This is the effective route for SB18002
    (DCA2648 ΔclaO-D::scar) production context; raw genome metadata remains DCA2648.
  snapshot_sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
- evidence_id: C066-OWNER
  kind: record_content
  reference: data/natural_products/alkaloids/ammosester-c.yaml
  locator: Complete owner and resolved source projection
  accessed_at: '2026-10-21T12:52:23.739276Z'
  support: supports
  summary: The owner identifies ammosester C with full key VMGBZXKKNNEJRM-UHFFFAOYSA-N;
    exact source rows, xrefs, source concepts and classification were read.
  snapshot_sha256: 4df748e42b978453f42e5f820fa00f9cffbc301b141d1d3326560633a94ead04
- evidence_id: C066-RAW
  kind: record_content
  reference: data/raw/mibig_compounds.tsv
  locator: Complete relevant raw rows and local exact-key inventories
  accessed_at: '2026-10-21T12:52:23.739276Z'
  support: supports
  summary: 'Exact source row SHA-256 values: BGC0002343:3 = 796a5df9fbca18ef80d0b5322e744eda5d056cf3a53aaa9ad1c4ec760296aa7a.
    Digests cover every column using canonical sorted JSON. Complete exact-key eligible
    ChEBI projection has 0 row(s).'
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
- evidence_id: C066-CLASS
  kind: record_content
  reference: data/raw/npclassifier.tsv
  locator: Exact-key classification row and owner attribution
  accessed_at: '2026-10-21T12:52:23.739276Z'
  support: context_only
  summary: The filing and NPClassifier superclass/class outputs are attributed to
    the pinned model version. MIBiG biosynthetic classes remain a separate source
    axis; current authority ontology relations are not silently promoted into asserted
    corpus classes.
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
- evidence_id: C066-SEARCH
  kind: search
  reference: /private/tmp/npm-review-work/066/chemistry-local-search.txt
  locator: Complete matching path list
  accessed_at: '2026-10-21T12:52:23.859042Z'
  support: supports
  summary: Ignored-inclusive search checks the exact full key, current slug and target
    ID across current owners, curation, configuration and source code. Exact raw inventory
    rows were separately parsed. This bounded search does not claim universal absence.
  snapshot_sha256: 23b957c186a70db60f1c7545cf208099d5f8c8b9f903b3d2657edd3bdd8faa81
  search_scope: rg --no-ignore --hidden -l -F -e VMGBZXKKNNEJRM-UHFFFAOYSA-N -e ammosester-c
    -e naturalproductmech:mibig-695cae6453 data/natural_products curation conf src
    scripts
- evidence_id: C066-NPA
  kind: database
  reference: https://www.npatlas.org/api/v1/compound/NPA033060
  locator: Complete exact identity, identifier, provenance and relevant source fields
  accessed_at: '2026-10-21T12:21:56.797637Z'
  support: supports
  summary: NPA033060 resolves in the NPAtlas compound namespace. Its complete identity,
    structure history and origin-reference fields were read; current formula C12H9ClN4O3
    and full key VMGBZXKKNNEJRM-UHFFFAOYSA-N. Exact graph results are retained in
    the independent comparison.
  snapshot_sha256: c7d97f6fb9d957090d62017560414e8b7657b5d742229f73f4bf4ddb98af2593
- evidence_id: C066-PC
  kind: database
  reference: https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/VMGBZXKKNNEJRM-UHFFFAOYSA-N/JSON
  locator: Complete exact identity, identifier, provenance and relevant source fields
  accessed_at: '2026-10-21T12:21:56.541127Z'
  support: supports
  summary: PubChem Compound CID 135878873 resolves for the exact-key query. Identity
    properties and the complete atom/bond/stereo representation are retained; CID
    is not a Substance SID.
  snapshot_sha256: 19cf1099fe7d4d8f44c7c4d0017c8e5a297aa53d25e7ac0e39150ad34b96a2c2
- evidence_id: C066-CHEBI-SEARCH
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/es_search/?term=VMGBZXKKNNEJRM-UHFFFAOYSA-N&size=100
  locator: Complete exact identity, identifier, provenance and relevant source fields
  accessed_at: '2026-10-21T12:21:56.436108Z'
  support: supports
  summary: Bounded exact full-key ChEBI query and returned candidate list inspected.
    The returned two-star entry is not a three-star eligible grounding; no global
    absence claim is made.
  snapshot_sha256: 65b74a3c49f16a80e252e3a0a5c0f87420c47919a786925da7fab19594be52e8
- evidence_id: C066-CHEBI
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/221166/
  locator: Complete exact identity, identifier, provenance and relevant source fields
  accessed_at: '2026-10-21T12:22:17.604902Z'
  support: supports
  summary: Current CHEBI:221166 is 2-star and therefore is outside this repository's
    three-star eligibility rule. Complete identity, default structure, origins and
    ontology relations were inspected. Its public entry is not an eligible replacement
    solely because its key matches.
  snapshot_sha256: a998d7b97196c4bdc3f6725c9c79985f425991d7c42754fc27defb9043d13dfa
- evidence_id: C066-CHEBI-MOL
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/molfile/221166/
  locator: Complete exact identity, identifier, provenance and relevant source fields
  accessed_at: '2026-10-21T12:22:17.622505Z'
  support: supports
  summary: The official MOL was parsed independently, without editing. It supplies
    the representation comparison; agreement of a MOL does not validate a contradictory
    default SMILES.
  snapshot_sha256: 0e0bd054f60f57cc529031a2185cd52f1b8ef17dde24643d3e6dd1b88f4be478
- evidence_id: C066-CALC
  kind: validation
  reference: /private/tmp/npm-review-work/066/chemistry-authority-comparison.json
  locator: Fresh full Standard and fixed-H graph comparison, charge, formula and every
    tetrahedral centre
  accessed_at: '2026-10-21T12:52:23.862142Z'
  support: supports
  summary: Owner, NPAtlas, PubChem and official ChEBI MOL reconstruct to VMGBZXKKNNEJRM-UHFFFAOYSA-N.
    Full Standard and fixed-H InChI, formula, charge and assigned/undefined centres
    are retained per representation. Default ChEBI SMILES is separately tested and
    is not silently repaired.
  snapshot_sha256: e3a4c2d956b543c45a429b9124a6d7d695dd6ea008e8bfcc2c645d4328ee6a7e
- evidence_id: C066-WD-Q103811340
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q103811340.json
  locator: Complete exact identity, identifier, provenance and relevant source fields
  accessed_at: '2026-10-21T12:44:55.704386Z'
  support: supports
  summary: 'Current LOTUS-linked Wikidata entity: {"qid": "Q103811340", "label": "Streptomyces
    uncialis", "P235": [], "P234": [], "P2017": [], "P685": ["1048205"], "P225": ["Streptomyces
    uncialis"]}. Chemical and organism namespaces are kept distinct; this resolution
    is not primary occurrence evidence.'
  snapshot_sha256: 18505c78a03c65a3e44a812f31c6c49001514f92aa39418c368a5128d232f5b5
- evidence_id: C066-WD-Q113959004
  kind: database
  reference: https://www.wikidata.org/wiki/Special:EntityData/Q113959004.json
  locator: Complete exact identity, identifier, provenance and relevant source fields
  accessed_at: '2026-10-21T12:44:55.949890Z'
  support: supports
  summary: 'Current LOTUS-linked Wikidata entity: {"qid": "Q113959004", "label": "Methyl
    11-amino-10-chloro-3-hydroxy-9-imino-2,7-diazatricyclo[6.3.1.04,12]dodeca-1,3,5,8(12),10-pentaene-6-carboxylate",
    "P235": ["VMGBZXKKNNEJRM-UHFFFAOYSA-N"], "P234": ["InChI=1S/C12H9ClN4O3/c1-20-12(19)4-2-3-5-9(16-4)7(14)6(13)8(15)10(5)17-11(3)18/h2,14,16,18H,15H2,1H3"],
    "P2017": [], "P685": [], "P225": []}. Chemical and organism namespaces are kept
    distinct; this resolution is not primary occurrence evidence.'
  snapshot_sha256: 8d49207785791b6353f360d59a136b1b8d5db20b267f9cc0fba3bafb468acbf4
- evidence_id: C066-MIBIG-BGC0002343
  kind: database
  reference: https://mibig.secondarymetabolites.org/repository/BGC0002343.3/annotations.json
  locator: Complete exact identity, identifier, provenance and relevant source fields
  accessed_at: '2026-10-21T12:21:54.832495Z'
  support: supports
  summary: BGC0002343 version 3 resolves as active, with quality questionable and
    completeness unknown. Complete compounds, source taxonomy, loci and methods were
    inspected. The selected exact row matches the raw representation; source metadata
    is not independent experimental verification.
  snapshot_sha256: 5a839d367076e714423daf91484b1dc5f1ccaec38eda0cc182d387d796a89c47
- evidence_id: C066-TAX
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1930928,1283330,1048205,56108,354,230521&retmode=xml
  locator: Relevant complete taxon records with rank, names, aliases and lineage
  accessed_at: '2026-10-21T12:25:18.454076Z'
  support: supports
  summary: NCBI1048205 resolves to Streptomyces uncialis at species rank. The deposited
    LFBV01000006.1 source is DCA2648. This is not itself an accession for the tested
    engineered SB18002 ΔclaO-D::scar genotype; source-locus and tested-culture scopes
    remain separate.
  snapshot_sha256: 59a73aa6f2724bd0982590842fa1708abe0260289499b5cc047354af2a2fa26f
- evidence_id: C066-GENBANK0
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=LFBV01000006.1&seq_start=293360&seq_stop=323959&rettype=gbwithparts&retmode=text
  locator: Header, source qualifiers and interval metadata; no protein translation
    assertion
  accessed_at: '2026-10-21T12:25:21.288718Z'
  support: supports
  summary: The exact accession version and requested bounded interval resolve. Header,
    reference and source-feature metadata support the deposited organism/strain bridge
    only. The entire chromosome was not downloaded, and no historical stock, protein-sequence
    or experimentally delimited endpoint equivalence is inferred.
  snapshot_sha256: c857a8f56a107b9a04ea43b5563b5a8425a79abee9342bbfa942bb0f8bfb93d4
- evidence_id: C066-PRIMARY
  kind: primary_source
  reference: DOI:10.1093/jimb/kuab027
  locator: Official SI S16 Figure S5, exact compound 23
  accessed_at: '2026-10-21T12:07:17.239548Z'
  support: supports
  summary: Original primary drawing 23 gives C12H9ClN4O3, charge 0, Standard key JVRCXQRBYCAUKV-UHFFFAOYSA-N
    and fixed-H key JVRCXQRBYCAUKV-HCKMINDGNA-N. Original pixels and numbered graph
    transcription were compared; no inferred solution population or new experimental
    structure determination is claimed.
  snapshot_sha256: 35863d9c6b8802b18361dc1b6f9f535192da02712d5f345905ff168ad06050f1
- evidence_id: C066-PRIMARY-CALC
  kind: validation
  reference: /private/tmp/npm-review-work/066/chemistry-primary-comparison.json
  locator: Fresh parsing of source-labelled molecular graph versus owner
  accessed_at: '2026-10-21T12:52:26.825935Z'
  support: supports
  summary: Complete formula/charge/Standard/fixed-H comparison is retained with the
    literal primary graph input. It is interpreted with the actual source pixels,
    not merely compound labels.
  snapshot_sha256: 307e613b1f852a5abb899a0f493257119ff76551c38d8091372d714508f40ddb
- evidence_id: C066-MICROSTATE
  kind: validation
  reference: /private/tmp/npm-review-work/shared-next-batch007/authorities/ammosester-microstates/comparison.json
  locator: Unique element-labelled heavy-atom mapping and explicit hydrogen/bond-order
    differences
  accessed_at: '2026-10-21T12:32:12.258080Z'
  support: supports
  summary: Both forms have the same unique heavy-atom adjacency mapping, formula and
    charge. For A, N5 gains H and the C6 amino group loses H in the authority representation;
    Standard keys match but fixed-H keys differ, and default RDKit tautomer canonicalization
    does not converge. For C, the source lactam versus authority hydroxyl/imino form
    shifts N1 to O2 H and C6 amino to N5 H with pi-bond changes; Standard keys differ
    despite equal heavy-atom connectivity, while RDKit canonical tautomers converge.
    These are representational observations, not measured microstate populations.
  snapshot_sha256: 4217c58db1f1bc7966a1a84c9467dca8cbfdd81b09fcb335ea2c5147f6016d5f
assessments:
- assessment_id: R066-HISTORY
  area: provenance
  topic: Native status and retained seed history
  outcome: supported
  summary: The 3 dated seed events and SEEDED status describe generated provenance.
    This review does not relabel the owner REVIEWED or treat seed history as scientific
    approval. The latest 2026-10-13 event is another source-and-table seed event,
    not scientific sign-off.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - R066-OWNER
- assessment_id: R066-OPTIONAL
  area: completeness
  topic: Optional mechanism and application content
  outcome: not_applicable
  summary: The owner has no structured pathway steps, causal edges, organism-specific
    proteins, molecular-target items, bioactivity rows or synthetic-biology applications.
    Their absence alone is not a defect in this source-generated record. No enzyme,
    target, activity or engineering claim is inferred from the name or chemical class.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - R066-OWNER
  - R066-LOCAL-SOURCES
- assessment_id: R066-IMODULON
  area: completeness
  topic: Structured transcriptomic context
  outcome: not_applicable
  summary: No exact named native producer and strain is covered by the inspected iModulonDB
    dataset catalogue. E. coli used as a recombinant expression host in source experiments
    does not supply native-producer expression context; genus-only occurrences cannot
    identify a covered species or strain. No applicable module query follows from
    these records. This bounded coverage limit is not negative evidence about production
    or function.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - R066-OWNER
  - R066-IMODULON-DATASETS
- assessment_id: S066-A-IDENTITY
  area: identity
  topic: Published exact compound and representation boundary
  outcome: supported
  summary: 'Compound 23 is the N-desmethyl analog of B: neutral C12H9ClN4O3, with
    an N-1 H and C-2 lactam in the primary Figure 2C/SI S16. Main Table 1 and the
    reported HMBC correlations from 1-NH corroborate that depiction. The current owner
    has the same heavy-atom connectivity and charge but a different lactim/imino microstate
    with a different Standard InChIKey; this is a tautomeric representation issue,
    not a constitutional-isomer substitution. No tetrahedral stereocentre is present.
    Chemical authority and any representation repair are independently handled in
    the identifier packet.'
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - S066-OWNER
  - S066-IDENTITY
  - S066-SI-IDENTITY
  - S066-MICROSTATE
- assessment_id: S066-A-OCCURRENCE
  area: evidence
  topic: Exact species occurrence and natural-origin scope
  outcome: supported
  summary: The sole LOTUS DOI and producer/locus PMID are aliases for the same 2021
    study. Positive culture isolation of compound 23 from the native-organism derivative
    supports the S. uncialis occurrence. Preserve the proposed downstream oxidation
    and engineered culture context without treating them as proof of synthetic origin
    or unmodified wild-type production.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - S066-CULTURE
  - S066-GENETICS
  - S066-PATHWAY
- assessment_id: S066-A-METHODS
  area: evidence
  topic: Product-specific genetic and biochemical support
  outcome: concern
  summary: 'The inherited Enzymatic assays label is not the demonstrated method for
    exact C: purified Ame24 produces B (22). Exact C (23) is lost in the native-organism
    SB18003 Δame24 derivative relative to SB18002. The appropriate product-specific
    method is Knock-out studies, which also resolves the undergraded producer claim
    under the repository policy, provided the engineered native strain context is
    retained.'
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - S066-RAW
  - S066-CULTURE
  - S066-GENETICS
  - S066-ASSAY
  - S066-SI-ASSAY
  dimensions:
  - name: deposited_source_genome
    value: S. uncialis DCA2648; LFBV01000006.1
    definition: Genome-mining source and current accession source metadata; not a
      separately deposited engineered mutant genome.
    evidence_ids:
    - S066-LOCUS
    - S066-CULTURE
  - name: tested_native_organism_background
    value: SB18002 ΔclaO-D::scar; SB18003 further Δame24::aac(3)IV
    definition: Compound isolation and loss/retention were compared in this native-organism
      derivative, not a species-wide or heterologous-cluster experiment.
    evidence_ids:
    - S066-CULTURE
    - S066-GENETICS
  - name: exact_assay_direction
    value: acid 24 + SAM → ammosester B (22)
    definition: Purified retained N-His6-Ame24 directly forms 22; it consumes 24 and
      does not assay formation of 21 or 23.
    evidence_ids:
    - S066-ASSAY
    - S066-SI-ASSAY
  - name: recommended_evidence_tier
    value: BGC_CHARACTERIZED / CLUSTER_DEMONSTRATED
    definition: Product-specific native deletion supports the producer grade, while
      the locus grade remains demonstrated. The purified enzyme method applies additionally
      only to B.
    evidence_ids:
    - S066-GENETICS
    - S066-ASSAY
    - S066-METHOD-CONSUMER
- assessment_id: S066-A-PROPOSALS
  area: completeness
  topic: Upstream model, nonenzymatic proposal and optional enrichments
  outcome: supported
  summary: No missing optional pathway or protein finding is warranted. Any enrichment
    must preserve direct product endpoints, tagged construct scope, absence of rescue
    in the inspected experiment, and the proposed upstream scaffold-peptide chemistry.
    OTHER/RIBOSOMAL source classification and the NPClassifier labels are not independent
    precursor or catalytic experiments.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - S066-OWNER
  - S066-PATHWAY
  - S066-ASSAY
  - S066-ACTIVITY
- assessment_id: S066-A-REPAIR
  area: ownership
  topic: Consumed guarded method and strain decisions
  outcome: supported
  summary: Use exact compound-specific maintained method, citation-guard and strain
    inputs. These recommendations were checked against the current consumers, but
    no corpus regeneration or correction fixture was run in this science review. If
    a chemical correction is composed with these inputs, first resolve and test the
    loader rejection rather than removing drift guards.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - S066-METHOD-CONSUMER
  - S066-REFERENCE-GUARD
  - S066-STRAIN-CONSUMER
- assessment_id: C066-SOURCE
  area: provenance
  topic: Versioned source concepts, exact joins and eligible grounding
  outcome: supported
  summary: Source-concept identifiers are reproducibly minted from MIBIG plus accession:compound_index,
    not a chemical graph. Complete raw-row digests and versioned current source entries
    are retained. The exact-key committed eligible ChEBI projection is empty, and
    current matching ChEBI entries are two-star; no three-star replacement or asserted
    ontology class is inferred.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - C066-RAW
  - C066-CHEBI
  - C066-CHEBI-SEARCH
  - C066-SEARCH
  - C066-MIBIG-BGC0002343
- assessment_id: C066-CLASSIFICATION
  area: provenance
  topic: Predicted classification and source BGC class
  outcome: supported
  summary: The owner filing and NPClassifier superclass/class output preserve the
    exact-key model version and source values. BGC classes are separate MIBiG assertions.
    Their presence does not prove a mechanism, and two-star authority classes/roles
    are not silently admitted.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - C066-CLASS
  - C066-RAW
  - C066-OWNER
  - C066-CHEBI
- assessment_id: C066-TAXON
  area: scope
  topic: Chemical entity and source-organism namespaces
  outcome: supported
  summary: The current LOTUS chemical Wikidata entity retains the owner full key,
    while organism Q103811340 maps to NCBI1048205 Streptomyces uncialis. The deposited
    DCA2648 genome context does not establish that the engineered experimental genotype
    is wild type; that scientific boundary is assessed separately.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - C066-WD-Q113959004
  - C066-WD-Q103811340
  - C066-TAX
  - C066-GENBANK0
- assessment_id: C066-IDENTITY
  area: representation
  topic: Primary depicted microstate versus stored authority form
  outcome: concern
  summary: C uses VMGBZXKKNNEJRM while the primary depicted lactam is JVRCXQRBYCAUKV.
    Explicit atom mapping shows identical heavy-atom constitution; the key discrepancy
    is a hydrogen/bond-order representation difference, not a different carbon/nitrogen
    skeleton.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  evidence_ids:
  - C066-CALC
  - C066-PRIMARY
  - C066-PRIMARY-CALC
  - C066-MICROSTATE
  - C066-OWNER
findings:
- finding_id: S066-F-METHODS
  issue_key: mibig-bgc0002343-compound3-method-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Replace the inherited enzyme label with exact ammosester C deletion evidence
  description: 'The inherited Enzymatic assays label is not the demonstrated method
    for exact C: purified Ame24 produces B (22). Exact C (23) is lost in the native-organism
    SB18003 Δame24 derivative relative to SB18002. The appropriate product-specific
    method is Knock-out studies, which also resolves the undergraded producer claim
    under the repository policy, provided the engineered native strain context is
    retained. The species-level label also omits the experimental SB18002 strain context;
    include that context in the same repair. This finding does not change chemical
    identity or transfer other congener experiments.'
  target_ids:
  - naturalproductmech:mibig-695cae6453
  field_paths:
  - producer_organisms[0].evidence_basis
  - producer_organisms[0].strain
  - producer_organisms[0].notes
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  - biosynthetic_gene_clusters[0].link_evidence_basis
  evidence_ids:
  - S066-RAW
  - S066-CULTURE
  - S066-GENETICS
  - S066-ASSAY
  - S066-SI-ASSAY
  - S066-METHOD-CONSUMER
  - S066-REFERENCE-GUARD
  - S066-STRAIN-CONSUMER
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Consumed exact-compound method correction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Paired full-raw-row SHA guard and attributed adjudication
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Guarded exact experimental production background
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Compose maintained decisions and regenerate the owner
  rule_id: 'review-checklist: exact product, strain and native versus biochemical
    evidence'
- finding_id: C066-F-MICROSTATE
  issue_key: ammosester-c-microstate
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: The primary and stored microstates need explicit qualification
  description: The primary lactam drawing and stored hydroxyl/imino representation
    have different Standard keys, JVRCXQRBYCAUKV-UHFFFAOYSA-N and VMGBZXKKNNEJRM-UHFFFAOYSA-N,
    despite the same element-labelled heavy-atom connectivity, neutral formula and
    charge. The undocumented distinction materially affects exact-key occurrence/authority
    joins.
  target_ids:
  - naturalproductmech:mibig-695cae6453
  field_paths:
  - chemical_structure
  - discussions
  - xrefs
  evidence_ids:
  - C066-OWNER
  - C066-RAW
  - C066-CALC
  - C066-PRIMARY
  - C066-PRIMARY-CALC
  - C066-MICROSTATE
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/ammosester-c.yaml
    role: Curator-owned cited representation discussion through the validated writer
      and curation event helper
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Any later representation-changing decision requires an explicit supported
      consumed action and safe graph checks
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Current actions are limited to eligible ChEBI changes; not directly usable
      for these two-star same-compound microstates
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Current claim-reference overlay rejects a structure-corrected row; composition
      must be explicit if identity representation changes
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Corrected-key join provenance and source-concept retention if a key change
      is selected
  rule_id: review-yaml-record:exact-identity-and-representation
  native_severity: major
  normalization_reason: The defect concerns representation or nomenclature; it does
    not establish a different heavy-atom constitution.
actions:
- action_id: S066-ACTION-METHODS
  finding_ids:
  - S066-F-METHODS
  target_ids:
  - naturalproductmech:mibig-695cae6453
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_locus_evidence_overrides.tsv
    role: Consumed exact-compound method correction
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Paired full-raw-row SHA guard and attributed adjudication
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Guarded exact experimental production background
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Compose maintained decisions and regenerate the owner
  generator: scripts/seed_from_sources.py
  description: Add an attributed REPLACE in curation/mibig_locus_evidence_overrides.tsv
    for naturalproductmech:mibig-695cae6453, source MIBIG, source_id BGC0002343 and
    exact source_label ammosester C. Set exactly Knock-out studies. REPLACE does not
    enforce its expected_* columns, so they are not sufficient drift protection. Pair
    it with the consumed claim-reference row for BGC0002343:3, expected_source_row_sha256
    796a5df9fbca18ef80d0b5322e744eda5d056cf3a53aaa9ad1c4ec760296aa7a, producer_reference
    and locus_reference PMID:33982054, source_reference DOI:10.1093/jimb/kuab027,
    and curator/date/rationale. Add the separately consumed producer-strain row with
    the same source ID/SHA and strain SB18002 (DCA2648 ΔclaO-D::scar). The method
    decision changes grades; the citation/strain decisions only supply guards and
    attributed context. Exact proposed field dictionaries are retained in science-proposed-inputs.json.
    If a structure correction is also adopted, extend and test the composition contract
    before attempting the paired citation correction, which currently rejects structure-corrected
    rows; the strain qualification path also rejects them.
  acceptance_checks:
  - Match the untouched full BGC0002343:3 source row SHA 796a5df9fbca18ef80d0b5322e744eda5d056cf3a53aaa9ad1c4ec760296aa7a;
    reject stale, duplicate, missing and unconsumed decisions before output. Exercise
    complete raw-row drift rejection through the paired consumed guard, or implement
    and test equivalent REPLACE context guards before using that alternative.
  - Emit exactly Knock-out studies with BGC_CHARACTERIZED and CLUSTER_DEMONSTRATED,
    qualified to the tested SB18002/SB18003 background. Do not add whole-cluster heterologous
    production or a rescue experiment.
  - Retain taxon 1048205, raw source version 3, LFBV01000006.1:293360..323959, stable
    owner/path and the valid species occurrence. Preserve current chemistry unless
    the separately adjudicated identifier action explicitly changes its microstate;
    do not let a method change silently migrate structures.
  - Keep DCA2648 deposited-source metadata separate from SB18002 production and SB18003
    deletion context. E. coli BL21(DE3) is the recombinant protein host, not an asserted
    natural producer.
  - If combined with a structure decision, add focused tests for guarded composition
    and source drift; do not bypass correct_claim_reference rejection or drop the
    complete raw-row digest.
  - Inspect the regenerated canary diff, run focused contract tests and required strict/reproduction/repository
    gates. Proposed input dictionaries and static consumer inspection are not evidence
    that these gates have run.
- action_id: C066-A-MICROSTATE
  finding_ids:
  - C066-F-MICROSTATE
  target_ids:
  - naturalproductmech:mibig-695cae6453
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/alkaloids/ammosester-c.yaml
    role: Curator-owned cited representation discussion through the validated writer
      and curation event helper
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/structure_corrections.py
    role: Any later representation-changing decision requires an explicit supported
      consumed action and safe graph checks
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Current actions are limited to eligible ChEBI changes; not directly usable
      for these two-star same-compound microstates
  - repository: CultureBotAI/NaturalProductMech
    path: src/naturalproductmech/curate/claim_references.py
    role: Current claim-reference overlay rejects a structure-corrected row; composition
      must be explicit if identity representation changes
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Corrected-key join provenance and source-concept retention if a key change
      is selected
  description: 'First add a cited curator-owned representation discussion, preserving
    both original primary and source graphs, explicit atom mapping, Standard/fixed-H
    keys and the limits of tautomer normalization; use the validated writer and a
    truthful curation event. Pin original BGC0002343:3 version3 and full-row SHA 796a5df9fbca18ef80d0b5322e744eda5d056cf3a53aaa9ad1c4ec760296aa7a.
    Do not declare a constitutional isomer or silently choose a source by majority.
    If policy adjudication requires a changed stored graph, extend the maintained
    correction schema/loader with a specifically supported primary-graph representation
    action: pin source row, primary snapshot, explicit valid target graph and calculated
    full/fixed-H fields; current REPLACE_WITH_CHEBI cannot use a two-star target.
    Recheck complete corpus target-key collisions and regenerate joins from the chosen
    exact representation; retain original source provenance and do not transfer old-key
    LOTUS, Cyano, NPClassifier or sibling links automatically. Compose this decision
    with the independent method, strain and citation repairs in one tested transform:
    existing claim-reference and strain applications reject structure_correction_note,
    so current tables cannot simply be stacked. The separately recommended method
    REPLACE must retain its full original source-row guard and the producer/locus
    assertions.'
  generator: Implement the maintained source decision and regenerate with the documented
    seeder workflow; do not patch a generated YAML or raw source snapshot.
  acceptance_checks:
  - The discussion states equal heavy-atom constitution and preserves different hydrogen/bond-order
    placement, formula, charge, Standard and fixed-H keys.
  - No two-star ChEBI entry is promoted to eligible grounding and no current invalid
    default SMILES is copied.
  - Any representation change rejects stale source/target pins, checks collisions
    and proves reproducible exact-key joins; it composes safely with method/strain/reference
    actions.
limitations:
- This review audits the present assertions and the concrete source questions they
  raise; it does not claim exhaustive discovery of every later activity or biosynthetic
  study. Optional enrichment remains distinct from correcting an unsupported current
  assertion.
- The cited main and official SI are available; the review does not independently
  reassign every raw NMR peak or reconstruct complete tagged-protein sequences. Original
  main and SI disagree on the 18-hour Ame24 conversion yield (about 12% versus 20.1%),
  so only the supported direction and exact endpoint are relied upon.
- The paper proposes nonenzymatic C-2 oxidation and parallel methylation routes. It
  directly establishes culture occurrence and the specified deletion/assay endpoints,
  not every upstream step or preferred native reaction order. No automatic synthetic-origin
  reassignment follows from the proposal.
- GenBank source metadata bridge the DCA2648 genome window; legacy annotation alone
  does not prove experimental cluster endpoints, exact current RS-tag equivalence
  or identity of the 309-aa tagged assay construct. These unasserted protein claims
  are outside this bounded owner review.
- Maintained actions are recommendations only. A method/strain/citation composition
  can conflict with a separately proposed structure correction; the existing rejection
  must be addressed with a tested contract, not bypassed.
- The authority snapshots and depicted graphs establish representation, not pH-dependent
  microstate populations or equilibrium. Experimental genotype, deletion phenotypes
  and enzyme-substrate/product scope are assessed separately.
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
- batch-007
```
