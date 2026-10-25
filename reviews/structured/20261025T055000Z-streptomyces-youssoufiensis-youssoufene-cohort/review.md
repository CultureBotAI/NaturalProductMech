# Streptomyces youssoufiensis OUC6819 and Streptomyces sp. youssoufene polyketide cohort review (BGC0002547 and BGC0002510)

- Review: 20261025T055000Z-streptomyces-youssoufiensis-youssoufene-cohort
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-25T05:32:00.000000Z
- Finished UTC: 2026-10-25T05:50:00.000000Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full 5-record category review of the Streptomyces youssoufiensis (NCBITaxon:654447, BGC0002547, MN844187.1) and Streptomyces sp. (NCBITaxon:1931, BGC0002510, MT459140.1) cinnamoyl lipid polyketide youssoufene cohort: dimeric youssoufene A1 (naturalproductmech:mibig-78ea4c55fb, data/natural_products/polyketides/youssoufene-a1.yaml) and monomeric congeners youssoufene B1 (naturalproductmech:mibig-ccb60942af, data/natural_products/unclassified/youssoufene-b1.yaml), youssoufene B2 (naturalproductmech:mibig-cf5248036e, data/natural_products/unclassified/youssoufene-b2.yaml), youssoufene B3 (naturalproductmech:mibig-f827d9f550, data/natural_products/unclassified/youssoufene-b3.yaml), and youssoufene B4 (naturalproductmech:mibig-18ba3c758c, data/natural_products/unclassified/youssoufene-b4.yaml), anchored to a full-corpus deterministic checkpoint of all 3,116 natural product owner records (290 with inline causal_graphs and 27 with causal_graph_refs) and 246 standalone causal graph components (3,362 total YAML records). Confirms Cycle 3 Stage 2 and Stage 3 curation of the 4-step YsfB/YsfC, YsfD/YsfE, YsfG, and YsfJ/YsfK biosynthetic pathways and 13-node / 12-edge BIOSYNTHESIS causal graphs (grounding 7 ENZYME nodes to NCBIProtein:QHB92589.1..QHB92592.1, QHB92594.1, QHB92597.1, QHB92598.1 and UniParc:UPI00131FE52F..UPI0013202848) across all 5 cohort records, while identifying three open findings for Stage 5 grouped remediation: (1) missing OUC6819 producer strain qualifications on producer_organisms[0] (NCBITaxon:654447, BGC0002547:1..5, MN844187.1, PMID:31891272 / DOI:10.1021/acs.orglett.9b04559) across all 5 records (F-YSF-001), (2) misattributed author citation ('Deng et al.' instead of 'Liu et al.') in biosynthetic_pathway[0..3].evidence[0].notes and causal_graphs[0].edges[0..11].evidence[0].notes citing DOI:10.1002/anie.202007777 (Angew. Chem. Int. Ed. 2021;60(1):153-158, PMID:33155752, authored by Zengzhi Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li) across all 5 records (F-YSF-002), and (3) upstream representation and source boundaries comprising NPClassifier POLYKETIDES vs UNCLASSIFIED split between dimeric youssoufene A1 and monomeric youssoufenes B1-B4, UNGROUNDED ComplexPortal/RHEA status on heterodimeric type II PKS KS/CLF complexes YsfB-YsfC, YsfD-YsfE, and YsfJ-YsfK, and genus-level NCBITaxon:1931 (Streptomyces sp., BGC0002510, MT459140.1, PMID:32860295) without a verifiable cultured strain designation (F-YSF-003).

## Scope And Provenance

Coherent 5-record biosynthetic and chemical-identity cohort covering all NaturalProductMech records seeded from the youssoufene cinnamoyl lipid polyketide biosynthetic gene clusters MIBiG BGC0002547 (MN844187.1, Streptomyces youssoufiensis) and BGC0002510 (MT459140.1, Streptomyces sp.), evaluated alongside frozen full-corpus inventory checks (3,116 owner YAML records and 246 standalone causal graph components; 3,362 total YAML records).

Selection: All 5 records derived from BGC0002547:1..5 and BGC0002510:1..5 (youssoufene A1 and youssoufenes B1-B4), selected to audit the Cycle 3 Stage 2 and Stage 3 curation of the 4-step YsfB/YsfC, YsfD/YsfE, YsfG, and YsfJ/YsfK type II PKS biosynthetic pathways and 13-node / 12-edge BIOSYNTHESIS causal graphs, producer strain completeness, claim-level citation accuracy, and chemical classification / grounding boundaries.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: git_commit at Git base d14547bc76e0582aca15eeb073e203d28ea7548e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| naturalproductmech:mibig-78ea4c55fb | data/natural_products/polyketides/youssoufene-a1.yaml | generated | youssoufene A1 |
| naturalproductmech:mibig-ccb60942af | data/natural_products/unclassified/youssoufene-b1.yaml | generated | youssoufene B1 |
| naturalproductmech:mibig-cf5248036e | data/natural_products/unclassified/youssoufene-b2.yaml | generated | youssoufene B2 |
| naturalproductmech:mibig-f827d9f550 | data/natural_products/unclassified/youssoufene-b3.yaml | generated | youssoufene B3 |
| naturalproductmech:mibig-18ba3c758c | data/natural_products/unclassified/youssoufene-b4.yaml | generated | youssoufene B4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict schema and semantic validation (cohort) | passed | True | naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c | All 5 cohort YAML files passed strict LinkML and semantic validation with 0 ERROR rows. |
| Full-corpus lockfile and filing verification | passed | True | naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c | Verified lockfile integrity across all 3,116 natural product owner records against data/natural_products/PATHS.tsv. |
| Full-corpus ontology ID-label correspondence | passed | True | naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c | Full-corpus ID-label check passed with 0 ERROR rows (12,619 OK_CANONICAL, 567 OK_SYNONYM, 35 OK_EXCEPTION, 0 ID_NOT_FOUND, 499 warn-only taxon_labels mismatches, 4,898 SKIPPED_NO_ADAPTER); all NCBITaxon (NCBITaxon:654447, NCBITaxon:1931) and BFO/RO ontology terms on the 5 cohort records resolve canonically. |
| Exhaustive corpus review-queue checkpoint | passed | True | naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c | Computed exhaustive review-records queue across all 3,116 corpus owners (8,922 rows across 12 queues: producer-evidence 2,292; biosynthesis 1,177; structure-disagreement 5; name-disagreement 67; unnamed-producer 39; shared-structure 207; needs-a-name 18; occurrence-only 12; pathway-ambiguous 620; unresolved-taxa 3,329; stereo-incomplete 1,124; record-review 32). All 5 cohort records appear in producer-evidence and unresolved-taxa (due to genus-level NCBITaxon:1931 on BGC0002510:1..5). |
| Repository-wide identifier and BGC cross-reference search | passed | True | naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c | Verified all 28 repository file references at d14547bc76e0582aca15eeb073e203d28ea7548e to BGC0002547, BGC0002510, MN844187.1, MT459140.1, and cohort identifiers across raw inventories, curation tables, records, pages, and structured reviews. |
| Full-corpus standalone causal graph component validation | passed | True | naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c | Validated all 246 standalone causal graph component YAML files under data/causal_graphs/ (40 passed, 0 failed). |

## Scientific And Domain Assessments

### Chemical structure grounding and 4-step YsfB/YsfC, YsfD/YsfE, YsfG, and YsfJ/YsfK biosynthetic pathway and 13-node / 12-edge causal graph verification

identity: supported. Targets: naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c.

All five cohort records carry distinct, stereochemically complete Standard InChIKeys and ground to committed project-minted naturalproductmech:mibig-* identifiers with grounding_status: MINTED (youssoufene A1 PBGNPVWDTRYFBH-GSOXOQHNSA-N, youssoufene B1 ODPDWQHBVRLWMV-JTWCGSJHSA-N, youssoufene B2 ODPDWQHBVRLWMV-WEQBXWHASA-N, youssoufene B3 WDDIDKVGAUZJRA-SLWKRUQWSA-N, and youssoufene B4 WDDIDKVGAUZJRA-CGAUJLMDSA-N) with zero ChEBI/PubChem false merges. All 5 records carry verified 4-step biosynthetic_pathway entries (step 1: YsfB/YsfC KS/CLF complex; step 2: YsfD/YsfE KS/CLF complex; step 3: YsfG isomerase [NCBIProtein:QHB92594.1]; step 4: YsfJ/YsfK KS/CLF complex; with exact A1 dimerization and release left unexpanded on youssoufene-a1.yaml) and 13-node / 12-edge BIOSYNTHESIS causal_graphs grounding 7 ENZYME nodes (nodes[0..6]) from Streptomyces youssoufiensis OUC6819 (MN844187.1) to exact GenBank protein and UniParc accessions (YsfB NCBIProtein:QHB92589.1 / UniParc:UPI00131FE52F, YsfC NCBIProtein:QHB92590.1 / UniParc:UPI00131FCA94, YsfD NCBIProtein:QHB92591.1 / UniParc:UPI00131FC4C1, YsfE NCBIProtein:QHB92592.1 / UniParc:UPI00131FAF34, YsfG NCBIProtein:QHB92594.1 / UniParc:UPI001320438E, YsfJ NCBIProtein:QHB92597.1 / UniParc:UPI00131F724F, YsfK NCBIProtein:QHB92598.1 / UniParc:UPI0013202848), 3 UNGROUNDED PROTEIN_COMPLEX nodes (nodes[7..9]: ysfbc_ks_clf, ysfde_ks_clf, ysfjk_ks_clf linked from their subunit ENZYME nodes via 'is subunit of' edges[0..5]), 2 UNGROUNDED PROCESS nodes (nodes[10..11]: acp_tethered_chain_elongation, benzene_ring_closure), and 1 GROUNDED COMPOUND node (nodes[12]), passing strict LinkML and ontology ID-label validation.

### Missing OUC6819 producer strain qualification on Streptomyces youssoufiensis (NCBITaxon:654447, BGC0002547:1..5)

completeness: concern. Targets: naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c.

Across all 5 cohort records, producer_organisms[0] (NCBITaxon:654447, Streptomyces youssoufiensis, mibig:BGC0002547, genbank:MN844187.1, PMID:31891272) omits producer_organisms[0].strain because MIBiG 4.0 exports species-level organism_name='Streptomyces youssoufiensis'. GenBank MN844187.1, Li et al. (2020, PMID:31891272, DOI:10.1021/acs.orglett.9b04559), Liu et al. (2021, PMID:33155752, DOI:10.1002/anie.202007777), and the records' own biosynthetic_pathway and causal_graphs notes and protein_examples[0].strain explicitly identify the sequenced producer strain as Streptomyces youssoufiensis OUC6819.

### Misattributed author citation ('Deng et al.' instead of 'Liu et al.') on DOI:10.1002/anie.202007777 evidence notes

provenance: concern. Targets: naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c.

Across all 5 cohort records, every evidence item in biosynthetic_pathway[0..3].evidence[0].notes (4 per record) and causal_graphs[0].edges[0..11].evidence[0].notes (12 per record) that cites DOI:10.1002/anie.202007777 (Angew. Chem. Int. Ed. 2021;60(1):153-158, PMID:33155752) refers to the authors as 'Deng et al.' (16 evidence notes on youssoufene-a1.yaml and 16 evidence notes on each of youssoufene-b1.yaml through youssoufene-b4.yaml; 80 total). However, DOI:10.1002/anie.202007777 is authored by Zengzhi Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li (Liu et al., with no author named Deng; Zhaoxian Deng was a co-author on the earlier Org. Lett. 2020 discovery paper DOI:10.1021/acs.orglett.9b04559, not on DOI:10.1002/anie.202007777).

### NPClassifier dimeric/monomeric pathway split, UNGROUNDED KS/CLF heterodimers, and genus-level BGC0002510 taxon boundary

representation: concern. Targets: naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c.

Three upstream representation and source boundaries affect the 5-record cohort: (1) NPClassifier (npclassifier.gnps2.org@2026-09-07) classifies dimeric youssoufene A1 under POLYKETIDES (np_classification.superclass_results: [Linear polyketides]) while returning empty pathway_results: [] for monomeric youssoufenes B1-B4 (which file under data/natural_products/unclassified/ with np_pathway: UNCLASSIFIED despite bgc_class: [PKS]); (2) the three heterodimeric type II PKS KS/CLF PROTEIN_COMPLEX nodes (nodes[7..9]: ysfbc_ks_clf, ysfde_ks_clf, ysfjk_ks_clf) remain UNGROUNDED at the complex level (while their constituent subunit ENZYME nodes nodes[0..3, 5..6] YsfB/YsfC, YsfD/YsfE, and YsfJ/YsfK carry grounding.id and protein_examples and connect via 'is subunit of' edges[0..5]), and biosynthetic_pathway steps[0..1, 3] omit scalar enzyme_id and steps[0..3] omit reaction_id because ComplexPortal and RHEA lack entries for these bacterial type II PKS heterodimers and polyene-forming steps; and (3) producer_organisms[1] (NCBITaxon:1931, Streptomyces sp., mibig:BGC0002510, genbank:MT459140.1:71..11851, PMID:32860295) remains genus-level without strain qualification because MIBiG 4.0 exports NCBITaxon:1931 and PMID:32860295 / MT459140.1 are not indexed in PubMed/ENA to verify a cultured strain designation.

## Findings

### F-YSF-001: Missing OUC6819 producer strain qualifications on Streptomyces youssoufiensis (NCBITaxon:654447, BGC0002547:1..5) across all 5 youssoufene records

major / open / confirmed; issue key: streptomyces-youssoufiensis-bgc0002547-ouc6819-producer-strain-missing.

All five Streptomyces youssoufiensis (NCBITaxon:654447) producer_organisms[0] claims seeded from BGC0002547:1..5 (MN844187.1:1..20186, PMID:31891272; row sha256s 1d48b2327fd1ff6df8dacc84f722e6dcef3c298cafc6442b51a0d2190b11547f on youssoufene-a1.yaml, acd26c9ce0f501c27e8a2d0097dce5d2fbee8400976c822752702b3b9c486417 on youssoufene-b1.yaml, ea799308511137361955d15f115be158a232e46e13f06711cf9e271ad1fe89ed on youssoufene-b2.yaml, e9c6f5c63380450c1cd78dee862c1662fb8c78e013db12318271be20b551eeae on youssoufene-b3.yaml, and deba7c35303ec40e78d46bdb947fd45ba3e178c5547f16c8540e2ec60909e553 on youssoufene-b4.yaml) omit producer_organisms[0].strain. GenBank MN844187.1, Li et al. (2020, PMID:31891272, DOI:10.1021/acs.orglett.9b04559), Liu et al. (2021, PMID:33155752, DOI:10.1002/anie.202007777), and the records' own biosynthetic_pathway and causal_graphs notes and protein_examples[0].strain explicitly identify the sequenced producer strain as Streptomyces youssoufiensis OUC6819.

### F-YSF-002: Misattributed author citation ('Deng et al.' instead of 'Liu et al.') on DOI:10.1002/anie.202007777 evidence notes across all 5 youssoufene records

major / open / confirmed; issue key: youssoufene-cohort-anie-202007777-author-attribution-mismatch.

Across all five youssoufene YAML records (youssoufene-a1.yaml and youssoufene-b1.yaml through youssoufene-b4.yaml), all 16 evidence items per record (80 total across the cohort) in biosynthetic_pathway[0..3].evidence[0].notes (4 per record) and causal_graphs[0].edges[0..11].evidence[0].notes (12 per record) that cite DOI:10.1002/anie.202007777 (Angew. Chem. Int. Ed. 2021;60(1):153-158, PMID:33155752) attribute the study to 'Deng et al.' in their prose notes. In fact, DOI:10.1002/anie.202007777 is authored by Zengzhi Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li (Liu et al.), with no author named Deng (Zhaoxian Deng was a co-author on the earlier 2020 Org. Lett. discovery paper DOI:10.1021/acs.orglett.9b04559, PMID:31891272).

### F-YSF-003: Upstream NPClassifier dimeric/monomeric split, UNGROUNDED KS/CLF heterodimer complexes, and genus-level BGC0002510 taxon boundary

minor / open / confirmed; issue key: youssoufene-cohort-npclassifier-ks-clf-and-bgc0002510-boundaries.

1) NPClassifier (npclassifier.gnps2.org@2026-09-07) classifies dimeric youssoufene A1 (PBGNPVWDTRYFBH-GSOXOQHNSA-N) under POLYKETIDES (Linear polyketides), while returning empty pathway_results: [] for monomeric congeners youssoufenes B1-B4 (which therefore file under data/natural_products/unclassified/ with np_pathway: UNCLASSIFIED despite bgc_class: [PKS]). 2) The three heterodimeric type II PKS KS/CLF PROTEIN_COMPLEX nodes (nodes[7..9]: ysfbc_ks_clf, ysfde_ks_clf, ysfjk_ks_clf) remain UNGROUNDED at the complex level (while their constituent subunit ENZYME nodes nodes[0..3, 5..6] carry grounding.id and protein_examples and connect via 'is subunit of' edges[0..5]), biosynthetic_pathway[0..1, 3] omit scalar enzyme_id, and biosynthetic_pathway[0..3] omit reaction_id because ComplexPortal and RHEA lack entries for these bacterial type II PKS heterodimers and polyene-forming steps. 3) producer_organisms[1] (NCBITaxon:1931, Streptomyces sp., mibig:BGC0002510, genbank:MT459140.1:71..11851, PMID:32860295) remains at genus level without strain qualification because MIBiG 4.0 exports NCBITaxon:1931 and PMID:32860295 / MT459140.1 are not indexed in PubMed/ENA to verify a cultured strain designation.

## Recommended Actions And Acceptance Checks

### qualify-youssoufiensis-ouc6819-producer-strains

Add five source-pinned producer strain rows to curation/mibig_producer_strains.tsv (columns source_id, expected_source_row_sha256, strain, reference, curator, date, rationale) for source_id=BGC0002547:1..5 (expected_source_row_sha256s 1d48b2327fd1ff6df8dacc84f722e6dcef3c298cafc6442b51a0d2190b11547f, acd26c9ce0f501c27e8a2d0097dce5d2fbee8400976c822752702b3b9c486417, ea799308511137361955d15f115be158a232e46e13f06711cf9e271ad1fe89ed, e9c6f5c63380450c1cd78dee862c1662fb8c78e013db12318271be20b551eeae, and deba7c35303ec40e78d46bdb947fd45ba3e178c5547f16c8540e2ec60909e553, strain='OUC6819', reference=PMID:31891272), then re-seed via scripts/seed_from_sources.py.

- Verify expected_source_row_sha256 pins for BGC0002547:1..5 in curation/mibig_producer_strains.tsv.
- Run scripts/seed_from_sources.py and confirm producer_organisms[0] (NCBITaxon:654447, mibig:BGC0002547) carries strain: OUC6819 across all 5 youssoufene YAML records.
- Verify zero regressions across scripts/validate_strict.py and scripts/verify_corpus.py.

### fix-anie-202007777-liu-et-al-attribution

Update the 16 evidence notes per record (80 total) citing DOI:10.1002/anie.202007777 in biosynthetic_pathway[0..3].evidence[0].notes and causal_graphs[0].edges[0..11].evidence[0].notes across youssoufene-a1.yaml and youssoufene-b1.yaml through youssoufene-b4.yaml to replace 'Deng et al.' with 'Liu et al. (2021)' (matching Zengzhi Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li, Angew. Chem. Int. Ed. 2021;60(1):153-158, PMID:33155752), append a CURATION_REVIEW_FIX history entry, and regenerate HTML pages.

- Confirm zero occurrences of 'Deng et al.' on evidence items citing DOI:10.1002/anie.202007777 across all 5 youssoufene YAML records.
- Confirm scripts/validate_strict.py, scripts/verify_corpus.py, and pytest tests/test_graph_components.py pass with zero errors.

### preserve-youssoufene-representation-boundaries

Retain locked PATHS.tsv filing (POLYKETIDES for youssoufene-a1.yaml and UNCLASSIFIED for youssoufene-b1.yaml through youssoufene-b4.yaml), retain UNGROUNDED PROTEIN_COMPLEX status on nodes[7..9] (ysfbc_ks_clf, ysfde_ks_clf, ysfjk_ks_clf) with subunit ENZYME nodes[0..3, 5..6] connected via 'is subunit of' edges[0..5], and retain genus-level NCBITaxon:1931 without strain on BGC0002510:1..5.

- Do not alter locked PATHS.tsv paths or invent ComplexPortal/RHEA identifiers or unverified BGC0002510 strain names.

## Category Boundaries

- retain: naturalproductmech:mibig-78ea4c55fb, naturalproductmech:mibig-ccb60942af, naturalproductmech:mibig-cf5248036e, naturalproductmech:mibig-f827d9f550, naturalproductmech:mibig-18ba3c758c. All five cohort records represent distinct, stereochemically defined natural products isolated from Streptomyces youssoufiensis OUC6819 with distinct Standard InChIKeys: dimeric youssoufene A1 (PBGNPVWDTRYFBH-GSOXOQHNSA-N) and monomeric E/Z geometric isomers youssoufene B1 (ODPDWQHBVRLWMV-JTWCGSJHSA-N), youssoufene B2 (ODPDWQHBVRLWMV-WEQBXWHASA-N), youssoufene B3 (WDDIDKVGAUZJRA-SLWKRUQWSA-N), and youssoufene B4 (WDDIDKVGAUZJRA-CGAUJLMDSA-N).

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cohort-owners | data/natural_products/PATHS.tsv; youssoufene-a1.yaml (sha256 7bb8f5d4d4bd5e30083973a8a2e41adefe24b1a77f0ad34480e9ba0b15f368a6), youssoufene-b1.yaml (sha256 ea395342b0f7b1b4b8038e7a731c274e1c1ceb2645f2ea8e94ac5ba8613b7746), youssoufene-b2.yaml (sha256 00ec251535ea020620a618880c862ff19eed67e5468f87a65bc227637cdede23), youssoufene-b3.yaml (sha256 65059808b4f28c4fc23f5fbf9b2e4390443c0f59477e4428c998cfee3c0020bc), youssoufene-b4.yaml (sha256 f6bf3a389fd5b5f5f60b7d08e922a450cf1409327db785f727b117d4165ff5a7) at d14547bc76e0582aca15eeb073e203d28ea7548e | supports | All 5 cohort YAML files are present at their locked PATHS.tsv locations (youssoufene-a1.yaml under POLYKETIDES and youssoufene-b1.yaml through youssoufene-b4.yaml under UNCLASSIFIED) with distinct Standard InChIKeys, valid LinkML structure, MINTED grounding_status, SEEDED curation_status, and verified 4-step YsfB/YsfC, YsfD/YsfE, YsfG, and YsfJ/YsfK biosynthetic_pathway and 13-node / 12-edge BIOSYNTHESIS causal_graphs. |
| mibig-inventory | data/raw/mibig_compounds.tsv; BGC0002547:1 (sha256 1d48b2327fd1ff6df8dacc84f722e6dcef3c298cafc6442b51a0d2190b11547f), BGC0002547:2 (sha256 acd26c9ce0f501c27e8a2d0097dce5d2fbee8400976c822752702b3b9c486417), BGC0002547:3 (sha256 ea799308511137361955d15f115be158a232e46e13f06711cf9e271ad1fe89ed), BGC0002547:4 (sha256 e9c6f5c63380450c1cd78dee862c1662fb8c78e013db12318271be20b551eeae), BGC0002547:5 (sha256 deba7c35303ec40e78d46bdb947fd45ba3e178c5547f16c8540e2ec60909e553), BGC0002510:1 (sha256 c3e0435917bbd397fd24aea07e7c3b9d3ab5e82f9c78ef6da21bb8ea14af03a5), BGC0002510:2 (sha256 21a73e5aa35fa5662f80788006a9257f1c9e68dc05f7bde528eeb59e1299ae32), BGC0002510:3 (sha256 c641bc135402bc0f73b1b4d3b15aad09f0623693626d416a3bb8287887656a4f), BGC0002510:4 (sha256 3ee732411d55c6c81ada94e96ccd5ffa512f45c0f9814c8e16799ae118465741), BGC0002510:5 (sha256 440036d24978d7e86647f1e21328444c39d2ff1caf96715ffa10e15679c6b67f) | partial | MIBiG 4.0 exports species-level NCBITaxon:654447 (Streptomyces youssoufiensis) across BGC0002547:1..5 (MN844187.1:1..20186, entry citation pubmed:31891272, Knock-out studies / BGC_CHARACTERIZED) without strain OUC6819, and genus-level NCBITaxon:1931 (Streptomyces sp.) across BGC0002510:1..5 (MT459140.1:71..11851, entry citation pubmed:32860295, Heterologous expression / SOURCE_ASSERTION). |
| npclassifier-table | data/raw/npclassifier.tsv; PBGNPVWDTRYFBH-GSOXOQHNSA-N row (line 1837, sha256 d367b73e14e4bf3ab0e3db221b079888b881594d06d0ecfff1872d8c92eca27b); monomeric congeners ODPDWQHBVRLWMV-JTWCGSJHSA-N (line 1712, sha256 5be79c76cc3448dd9ec5b41b74ee3a25613244efe620d128c6df5dc85344d620), ODPDWQHBVRLWMV-WEQBXWHASA-N (line 1713, sha256 7c7191d2be603781ab260932448c6b2738c12df52b17d67e2e8661fa6d60b408), WDDIDKVGAUZJRA-SLWKRUQWSA-N (line 2612, sha256 bdc5e21c9037b39645c0ca372bbf1231ebd429462821d8ea06acbbd4fec9c6a1), and WDDIDKVGAUZJRA-CGAUJLMDSA-N (line 2611, sha256 c0d3affa7c23f82eb842cf37e363d161587cf62ced1ba997eeace3bbd06d1f4d) present with empty classification columns (pathway_results: []) | supports | NPClassifier (npclassifier.gnps2.org@2026-09-07) classifies dimeric youssoufene A1 (PBGNPVWDTRYFBH-GSOXOQHNSA-N) as Polyketides / Linear polyketides, while returning empty pathway_results: [] for the four monomeric congeners youssoufenes B1-B4 (ODPDWQHBVRLWMV-JTWCGSJHSA-N, ODPDWQHBVRLWMV-WEQBXWHASA-N, WDDIDKVGAUZJRA-SLWKRUQWSA-N, WDDIDKVGAUZJRA-CGAUJLMDSA-N). |
| li-2020-orglett-pmid31891272 | DOI:10.1021/acs.orglett.9b04559; Li et al., Org. Lett. 2020;22(2):704-708 (PMID:31891272) and INSDC MN844187.1 (1..20186) | supports | Li et al. (2020, PMID:31891272, DOI:10.1021/acs.orglett.9b04559; authors Yaojie Li, Meilin Wang, Huayue Li, Yingang Zhang, Zhaoxian Deng, and Wenli Li) and GenBank MN844187.1 report the discovery of the ysf biosynthetic gene cluster (BGC0002547, 1..20186) and the isolation/characterization of youssoufenes A1 and B1-B4 in Streptomyces youssoufiensis strain OUC6819 (via ΔdtpC removal of competing dioxatetrahydropyrimidine biosynthesis and ΔysfA / ΔysfE / ΔysfG gene inactivation). |
| liu-2021-anie-pmid33155752 | DOI:10.1002/anie.202007777; Liu et al., Angew. Chem. Int. Ed. 2021;60(1):153-158 (PMID:33155752, 'An Unusual Type II Polyketide Synthase System Involved in Cinnamoyl Lipid Biosynthesis') | supports | Liu et al. (2021, PMID:33155752, DOI:10.1002/anie.202007777; authors Zengzhi Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li — no author named Deng) establish the enzymatic mechanism of the YsfA..YsfL type II PKS system in Streptomyces youssoufiensis OUC6819 through in vivo gene inactivation (ΔysfB, ΔysfC, ΔysfD, ΔysfE, ΔysfF, ΔysfH, ΔysfI, ΔysfJ, ΔysfK, ΔysfL) and in vitro reconstitution of purified YsfA, YsfB/YsfC, YsfD/YsfE, YsfJ/YsfK, YsfF, YsfH, and YsfI. |
| corpus-worklist | scripts/curation_worklist.py; Full-corpus checkpoint: 3,116 natural product owners (290 with inline causal_graphs, 27 with causal_graph_refs) and 246 standalone causal graph components (3,362 total YAML records) at d14547bc76e0582aca15eeb073e203d28ea7548e | supports | Deterministic worklist, lockfile, and graph-component checks confirm 3,116 valid owner records and 246 standalone causal graph components (8,922 worklist items across 12 queues), with all 5 youssoufene cohort members in SEEDED status. |

## Limits And Additional Notes

- Stage 4 is strictly read-only with respect to scientific YAML records and curation TSVs; all proposed curation edits are preserved as open findings for Stage 5 grouped remediation.
- Full-corpus deterministic checks (verify_corpus.py, validate_id_label_correspondence.py, curation_worklist.py --review-records, pytest tests/test_graph_components.py) audited all 3,116 owners and 246 standalone causal graph components (3,362 total YAML records), while claim-by-claim primary literature verification in this bundle was scoped to the 5-record Streptomyces youssoufiensis / Streptomyces sp. youssoufene cohort.
- INSDC accession MT459140.1 and PMID:32860295 (BGC0002510) are not indexed in ENA or PubMed, preventing independent verification of a cultured strain designation for producer_organisms[1] (NCBITaxon:1931).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T055000Z-streptomyces-youssoufiensis-youssoufene-cohort
kind: category
repository: CultureBotAI/NaturalProductMech
title: Streptomyces youssoufiensis OUC6819 and Streptomyces sp. youssoufene polyketide
  cohort review (BGC0002547 and BGC0002510)
started_at: '2026-10-25T05:32:00.000000Z'
finished_at: '2026-10-25T05:50:00.000000Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Same cycle campaign agent auditing the frozen post-Stage-3 corpus
    inventory; not an external human review.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: SEEDED retained across all 5 cohort records; OUC6819 producer strain
  qualifications (BGC0002547:1..5) and Liu et al. 2021 author attribution fixes on
  DOI:10.1002/anie.202007777 evidence notes queued for Stage 5
scientific_review: true
summary: 'Full 5-record category review of the Streptomyces youssoufiensis (NCBITaxon:654447,
  BGC0002547, MN844187.1) and Streptomyces sp. (NCBITaxon:1931, BGC0002510, MT459140.1)
  cinnamoyl lipid polyketide youssoufene cohort: dimeric youssoufene A1 (naturalproductmech:mibig-78ea4c55fb,
  data/natural_products/polyketides/youssoufene-a1.yaml) and monomeric congeners youssoufene
  B1 (naturalproductmech:mibig-ccb60942af, data/natural_products/unclassified/youssoufene-b1.yaml),
  youssoufene B2 (naturalproductmech:mibig-cf5248036e, data/natural_products/unclassified/youssoufene-b2.yaml),
  youssoufene B3 (naturalproductmech:mibig-f827d9f550, data/natural_products/unclassified/youssoufene-b3.yaml),
  and youssoufene B4 (naturalproductmech:mibig-18ba3c758c, data/natural_products/unclassified/youssoufene-b4.yaml),
  anchored to a full-corpus deterministic checkpoint of all 3,116 natural product
  owner records (290 with inline causal_graphs and 27 with causal_graph_refs) and
  246 standalone causal graph components (3,362 total YAML records). Confirms Cycle
  3 Stage 2 and Stage 3 curation of the 4-step YsfB/YsfC, YsfD/YsfE, YsfG, and YsfJ/YsfK
  biosynthetic pathways and 13-node / 12-edge BIOSYNTHESIS causal graphs (grounding
  7 ENZYME nodes to NCBIProtein:QHB92589.1..QHB92592.1, QHB92594.1, QHB92597.1, QHB92598.1
  and UniParc:UPI00131FE52F..UPI0013202848) across all 5 cohort records, while identifying
  three open findings for Stage 5 grouped remediation: (1) missing OUC6819 producer
  strain qualifications on producer_organisms[0] (NCBITaxon:654447, BGC0002547:1..5,
  MN844187.1, PMID:31891272 / DOI:10.1021/acs.orglett.9b04559) across all 5 records
  (F-YSF-001), (2) misattributed author citation (''Deng et al.'' instead of ''Liu
  et al.'') in biosynthetic_pathway[0..3].evidence[0].notes and causal_graphs[0].edges[0..11].evidence[0].notes
  citing DOI:10.1002/anie.202007777 (Angew. Chem. Int. Ed. 2021;60(1):153-158, PMID:33155752,
  authored by Zengzhi Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong,
  and Wenli Li) across all 5 records (F-YSF-002), and (3) upstream representation
  and source boundaries comprising NPClassifier POLYKETIDES vs UNCLASSIFIED split
  between dimeric youssoufene A1 and monomeric youssoufenes B1-B4, UNGROUNDED ComplexPortal/RHEA
  status on heterodimeric type II PKS KS/CLF complexes YsfB-YsfC, YsfD-YsfE, and YsfJ-YsfK,
  and genus-level NCBITaxon:1931 (Streptomyces sp., BGC0002510, MT459140.1, PMID:32860295)
  without a verifiable cultured strain designation (F-YSF-003).'
source:
  git_revision: d14547bc76e0582aca15eeb073e203d28ea7548e
  state: git_commit
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 13895fe1bda5f07ba46909db8778d1426ddf83ba3e55569e0cb52cd4d51590a9
    role: context
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 645746a86769610457ad445361746d6d5ccccdd29ddf29fc1ff256d419ff70de
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
  - path: curation/decisions.tsv
    sha256: 7214a74975fb2cb65521da18dd14ea1c65665f50060106976dc0db9caf887805
    role: context
  - path: curation/lotus_occurrence_exclusions.tsv
    sha256: d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d
    role: context
  - path: curation/mibig_claim_references.tsv
    sha256: bee1d64051b9b934be99ed1320ef33ecef7644c94bbdd11e7c1a040accd02029
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: bab55d1e354d6196096511d7fdb25f25e4c98cfbe041e02a91d707419987f7ae
    role: context
  - path: curation/mibig_structure_corrections.tsv
    sha256: c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0
    role: context
  - path: curation/mibig_xref_exclusions.tsv
    sha256: cc27be3b8e741164b50f154f8fc82df884066006b5343c295541ee671868bc9c
    role: context
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/polyketides/youssoufene-a1.yaml
    sha256: 7bb8f5d4d4bd5e30083973a8a2e41adefe24b1a77f0ad34480e9ba0b15f368a6
    role: target
  - path: data/natural_products/unclassified/youssoufene-b1.yaml
    sha256: ea395342b0f7b1b4b8038e7a731c274e1c1ceb2645f2ea8e94ac5ba8613b7746
    role: target
  - path: data/natural_products/unclassified/youssoufene-b2.yaml
    sha256: 00ec251535ea020620a618880c862ff19eed67e5468f87a65bc227637cdede23
    role: target
  - path: data/natural_products/unclassified/youssoufene-b3.yaml
    sha256: 65059808b4f28c4fc23f5fbf9b2e4390443c0f59477e4428c998cfee3c0020bc
    role: target
  - path: data/natural_products/unclassified/youssoufene-b4.yaml
    sha256: f6bf3a389fd5b5f5f60b7d08e922a450cf1409327db785f727b117d4165ff5a7
    role: target
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
    sha256: c3ebdac3952c23894df0d58843322b1082357098642762b834eca137358d1eaa
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
  - path: pyproject.toml
    sha256: 02505a46585e870eac7333f31a6773df51465ef13969d4d490fbc0247931d85c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/curation_worklist.py
    sha256: 913508ca8df2eb5c037cd9e4769b14b027869ab78c7306f33b59e1c7e383a1c3
    role: context
  - path: scripts/extract_mibig.py
    sha256: e1168a2a7839e3f3d0517e43180831cbc306b5e31cc519e9a78bde4d43c7290c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/seed_from_sources.py
    sha256: 5a16b71b2dd3172f3ac6bc5aa4a2a7bbcec072413e8e093197bc5459e0331da5
    role: context
  - path: scripts/validate_id_label_correspondence.py
    sha256: b5ff41bb52d24f5d7819fb12769e216440f75ec3fb3df3e3cb2c5082fffb40e0
    role: context
  - path: scripts/validate_strict.py
    sha256: e9b844d10fb7d2889521677716098da5883c7fd7d3c887a5cb600b87bbca0c21
    role: context
  - path: scripts/verify_corpus.py
    sha256: 3e79d6e18e43010a84e2ef7857625655185796d447ee12979a94cd836d756b60
    role: context
  - path: src/naturalproductmech/curate/claim_references.py
    sha256: 0ed8df41410e4762b93e2706a48d7be5b8e6d9718f87ac1a7408f2bf15f4a1b3
    role: context
  - path: src/naturalproductmech/curate/producer_strains.py
    sha256: c3b7a7ad66e5c6bc8d37b25b012a12fdde04fa886a2aa612d636ac210af3df68
    role: context
  - path: src/naturalproductmech/curate/structure_corrections.py
    sha256: 11808e60990b3520dbe8f9c50f6574f54cd32165185577a699f988c77f3d27ec
    role: context
  - path: src/naturalproductmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/naturalproductmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/naturalproductmech/schema/naturalproductmech.yaml
    sha256: 9410055c2ff37a012666b2f5e06260b02abe1183ee1caace6791461a4894841d
    role: context
targets:
- target_id: naturalproductmech:mibig-78ea4c55fb
  path: data/natural_products/polyketides/youssoufene-a1.yaml
  label: youssoufene A1
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/youssoufene-a1.yaml
    role: Generated and curator-enriched natural product owner record
- target_id: naturalproductmech:mibig-ccb60942af
  path: data/natural_products/unclassified/youssoufene-b1.yaml
  label: youssoufene B1
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b1.yaml
    role: Generated and curator-enriched natural product owner record
- target_id: naturalproductmech:mibig-cf5248036e
  path: data/natural_products/unclassified/youssoufene-b2.yaml
  label: youssoufene B2
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b2.yaml
    role: Generated and curator-enriched natural product owner record
- target_id: naturalproductmech:mibig-f827d9f550
  path: data/natural_products/unclassified/youssoufene-b3.yaml
  label: youssoufene B3
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b3.yaml
    role: Generated and curator-enriched natural product owner record
- target_id: naturalproductmech:mibig-18ba3c758c
  path: data/natural_products/unclassified/youssoufene-b4.yaml
  label: youssoufene B4
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b4.yaml
    role: Generated and curator-enriched natural product owner record
scope:
  description: Coherent 5-record biosynthetic and chemical-identity cohort covering
    all NaturalProductMech records seeded from the youssoufene cinnamoyl lipid polyketide
    biosynthetic gene clusters MIBiG BGC0002547 (MN844187.1, Streptomyces youssoufiensis)
    and BGC0002510 (MT459140.1, Streptomyces sp.), evaluated alongside frozen full-corpus
    inventory checks (3,116 owner YAML records and 246 standalone causal graph components;
    3,362 total YAML records).
  selection: All 5 records derived from BGC0002547:1..5 and BGC0002510:1..5 (youssoufene
    A1 and youssoufenes B1-B4), selected to audit the Cycle 3 Stage 2 and Stage 3
    curation of the 4-step YsfB/YsfC, YsfD/YsfE, YsfG, and YsfJ/YsfK type II PKS biosynthetic
    pathways and 13-node / 12-edge BIOSYNTHESIS causal graphs, producer strain completeness,
    claim-level citation accuracy, and chemical classification / grounding boundaries.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  exclusions:
  - target: Remaining 3,111 natural product owner records and 246 standalone causal
      graph components in the frozen 3,362-file corpus inventory
    reason: Audited at the corpus-checkpoint level via verify_corpus.py, validate_id_label_correspondence.py,
      curation_worklist.py --review-records, and pytest tests/test_graph_components.py;
      excluded from this 5-record youssoufene cohort denominator to preserve per-target
      scientific review depth.
checks:
- check_id: strict-cohort
  name: Strict schema and semantic validation (cohort)
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/c3_s4_strict_failures.tsv
    data/natural_products/polyketides/youssoufene-a1.yaml data/natural_products/unclassified/youssoufene-b1.yaml
    data/natural_products/unclassified/youssoufene-b2.yaml data/natural_products/unclassified/youssoufene-b3.yaml
    data/natural_products/unclassified/youssoufene-b4.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  evidence_ids:
  - cohort-owners
  summary: All 5 cohort YAML files passed strict LinkML and semantic validation with
    0 ERROR rows.
  scope_note: 2026-10-25T05:32:58Z..2026-10-25T05:33:10Z; output SHA256 590bdeb29003f5b00c5fe407e313812c3bc83e00cd4980060ee32e333dced520
- check_id: verify-corpus
  name: Full-corpus lockfile and filing verification
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py --summary
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  evidence_ids:
  - corpus-worklist
  summary: Verified lockfile integrity across all 3,116 natural product owner records
    against data/natural_products/PATHS.tsv.
  scope_note: 2026-10-25T05:32:58Z..2026-10-25T05:34:49Z; output SHA256 c9bcf7add9c5022125581df2e6b486735cd23803e49b73a4a2d6a60b62eebc5e
- check_id: validate-id-labels
  name: Full-corpus ontology ID-label correspondence
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/c3_s4_id_label.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  summary: Full-corpus ID-label check passed with 0 ERROR rows (12,619 OK_CANONICAL,
    567 OK_SYNONYM, 35 OK_EXCEPTION, 0 ID_NOT_FOUND, 499 warn-only taxon_labels mismatches,
    4,898 SKIPPED_NO_ADAPTER); all NCBITaxon (NCBITaxon:654447, NCBITaxon:1931) and
    BFO/RO ontology terms on the 5 cohort records resolve canonically.
  scope_note: 2026-10-25T05:34:49Z..2026-10-25T05:36:50Z; output SHA256 35423598d9ea0c53a374976d422665d7bfaf789855b7fd3357b97c7bc356f816;
    report TSV SHA256 fd6b4d6d15cac69220daf9027ac7dcb0a252f509e5bc69d831d181d0d6a6bd6b
- check_id: review-queue
  name: Exhaustive corpus review-queue checkpoint
  status: passed
  required: true
  command: .venv/bin/python scripts/curation_worklist.py --review-records --limit
    5
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  evidence_ids:
  - corpus-worklist
  summary: 'Computed exhaustive review-records queue across all 3,116 corpus owners
    (8,922 rows across 12 queues: producer-evidence 2,292; biosynthesis 1,177; structure-disagreement
    5; name-disagreement 67; unnamed-producer 39; shared-structure 207; needs-a-name
    18; occurrence-only 12; pathway-ambiguous 620; unresolved-taxa 3,329; stereo-incomplete
    1,124; record-review 32). All 5 cohort records appear in producer-evidence and
    unresolved-taxa (due to genus-level NCBITaxon:1931 on BGC0002510:1..5).'
  scope_note: 2026-10-25T05:37:30Z..2026-10-25T05:38:08Z; output SHA256 2c671a47982350c5968f24b020377eb57b876914d4882d295562790da8f3d330
- check_id: local-search
  name: Repository-wide identifier and BGC cross-reference search
  status: passed
  required: true
  command: git grep -l -E 'BGC0002547|BGC0002510|MN844187|MT459140|youssoufene-a1|youssoufene-b1|youssoufene-b2|youssoufene-b3|youssoufene-b4|mibig-78ea4c55fb|mibig-ccb60942af|mibig-cf5248036e|mibig-f827d9f550|mibig-18ba3c758c'
    d14547bc76e0582aca15eeb073e203d28ea7548e
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  summary: Verified all 28 repository file references at d14547bc76e0582aca15eeb073e203d28ea7548e
    to BGC0002547, BGC0002510, MN844187.1, MT459140.1, and cohort identifiers across
    raw inventories, curation tables, records, pages, and structured reviews.
  scope_note: 2026-10-25T05:49:15Z..2026-10-25T05:50:38Z; output SHA256 692f4bb22b6e94c26f581dca2e1df08797a7d021d48576cbb61f52075392979e
- check_id: test-graph-components
  name: Full-corpus standalone causal graph component validation
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_graph_components.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  evidence_ids:
  - corpus-worklist
  summary: Validated all 246 standalone causal graph component YAML files under data/causal_graphs/
    (40 passed, 0 failed).
  scope_note: 2026-10-25T05:36:50Z..2026-10-25T05:37:30Z; output SHA256 53e35ce114ca8fbf31b29cd0f5c1bac68a5dc6669944111d81e4323f8136b317
evidence:
- evidence_id: cohort-owners
  kind: record_content
  reference: data/natural_products/PATHS.tsv
  locator: youssoufene-a1.yaml (sha256 7bb8f5d4d4bd5e30083973a8a2e41adefe24b1a77f0ad34480e9ba0b15f368a6),
    youssoufene-b1.yaml (sha256 ea395342b0f7b1b4b8038e7a731c274e1c1ceb2645f2ea8e94ac5ba8613b7746),
    youssoufene-b2.yaml (sha256 00ec251535ea020620a618880c862ff19eed67e5468f87a65bc227637cdede23),
    youssoufene-b3.yaml (sha256 65059808b4f28c4fc23f5fbf9b2e4390443c0f59477e4428c998cfee3c0020bc),
    youssoufene-b4.yaml (sha256 f6bf3a389fd5b5f5f60b7d08e922a450cf1409327db785f727b117d4165ff5a7)
    at d14547bc76e0582aca15eeb073e203d28ea7548e
  accessed_at: '2026-10-25T05:40:00.000000Z'
  support: supports
  snapshot_sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
  summary: All 5 cohort YAML files are present at their locked PATHS.tsv locations
    (youssoufene-a1.yaml under POLYKETIDES and youssoufene-b1.yaml through youssoufene-b4.yaml
    under UNCLASSIFIED) with distinct Standard InChIKeys, valid LinkML structure,
    MINTED grounding_status, SEEDED curation_status, and verified 4-step YsfB/YsfC,
    YsfD/YsfE, YsfG, and YsfJ/YsfK biosynthetic_pathway and 13-node / 12-edge BIOSYNTHESIS
    causal_graphs.
- evidence_id: mibig-inventory
  kind: database
  reference: data/raw/mibig_compounds.tsv
  locator: BGC0002547:1 (sha256 1d48b2327fd1ff6df8dacc84f722e6dcef3c298cafc6442b51a0d2190b11547f),
    BGC0002547:2 (sha256 acd26c9ce0f501c27e8a2d0097dce5d2fbee8400976c822752702b3b9c486417),
    BGC0002547:3 (sha256 ea799308511137361955d15f115be158a232e46e13f06711cf9e271ad1fe89ed),
    BGC0002547:4 (sha256 e9c6f5c63380450c1cd78dee862c1662fb8c78e013db12318271be20b551eeae),
    BGC0002547:5 (sha256 deba7c35303ec40e78d46bdb947fd45ba3e178c5547f16c8540e2ec60909e553),
    BGC0002510:1 (sha256 c3e0435917bbd397fd24aea07e7c3b9d3ab5e82f9c78ef6da21bb8ea14af03a5),
    BGC0002510:2 (sha256 21a73e5aa35fa5662f80788006a9257f1c9e68dc05f7bde528eeb59e1299ae32),
    BGC0002510:3 (sha256 c641bc135402bc0f73b1b4d3b15aad09f0623693626d416a3bb8287887656a4f),
    BGC0002510:4 (sha256 3ee732411d55c6c81ada94e96ccd5ffa512f45c0f9814c8e16799ae118465741),
    BGC0002510:5 (sha256 440036d24978d7e86647f1e21328444c39d2ff1caf96715ffa10e15679c6b67f)
  accessed_at: '2026-10-25T05:40:00.000000Z'
  support: partial
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
  summary: MIBiG 4.0 exports species-level NCBITaxon:654447 (Streptomyces youssoufiensis)
    across BGC0002547:1..5 (MN844187.1:1..20186, entry citation pubmed:31891272, Knock-out
    studies / BGC_CHARACTERIZED) without strain OUC6819, and genus-level NCBITaxon:1931
    (Streptomyces sp.) across BGC0002510:1..5 (MT459140.1:71..11851, entry citation
    pubmed:32860295, Heterologous expression / SOURCE_ASSERTION).
- evidence_id: npclassifier-table
  kind: database
  reference: data/raw/npclassifier.tsv
  locator: 'PBGNPVWDTRYFBH-GSOXOQHNSA-N row (line 1837, sha256 d367b73e14e4bf3ab0e3db221b079888b881594d06d0ecfff1872d8c92eca27b);
    monomeric congeners ODPDWQHBVRLWMV-JTWCGSJHSA-N (line 1712, sha256 5be79c76cc3448dd9ec5b41b74ee3a25613244efe620d128c6df5dc85344d620),
    ODPDWQHBVRLWMV-WEQBXWHASA-N (line 1713, sha256 7c7191d2be603781ab260932448c6b2738c12df52b17d67e2e8661fa6d60b408),
    WDDIDKVGAUZJRA-SLWKRUQWSA-N (line 2612, sha256 bdc5e21c9037b39645c0ca372bbf1231ebd429462821d8ea06acbbd4fec9c6a1),
    and WDDIDKVGAUZJRA-CGAUJLMDSA-N (line 2611, sha256 c0d3affa7c23f82eb842cf37e363d161587cf62ced1ba997eeace3bbd06d1f4d)
    present with empty classification columns (pathway_results: [])'
  accessed_at: '2026-10-25T05:40:00.000000Z'
  support: supports
  snapshot_sha256: acb377573d2680b9dfacc9025a44dbbee03dca12e667485230d30ff7e3baecb3
  summary: 'NPClassifier (npclassifier.gnps2.org@2026-09-07) classifies dimeric youssoufene
    A1 (PBGNPVWDTRYFBH-GSOXOQHNSA-N) as Polyketides / Linear polyketides, while returning
    empty pathway_results: [] for the four monomeric congeners youssoufenes B1-B4
    (ODPDWQHBVRLWMV-JTWCGSJHSA-N, ODPDWQHBVRLWMV-WEQBXWHASA-N, WDDIDKVGAUZJRA-SLWKRUQWSA-N,
    WDDIDKVGAUZJRA-CGAUJLMDSA-N).'
- evidence_id: li-2020-orglett-pmid31891272
  kind: primary_source
  reference: DOI:10.1021/acs.orglett.9b04559
  locator: Li et al., Org. Lett. 2020;22(2):704-708 (PMID:31891272) and INSDC MN844187.1
    (1..20186)
  accessed_at: '2026-10-25T05:41:00.000000Z'
  support: supports
  summary: Li et al. (2020, PMID:31891272, DOI:10.1021/acs.orglett.9b04559; authors
    Yaojie Li, Meilin Wang, Huayue Li, Yingang Zhang, Zhaoxian Deng, and Wenli Li)
    and GenBank MN844187.1 report the discovery of the ysf biosynthetic gene cluster
    (BGC0002547, 1..20186) and the isolation/characterization of youssoufenes A1 and
    B1-B4 in Streptomyces youssoufiensis strain OUC6819 (via ΔdtpC removal of competing
    dioxatetrahydropyrimidine biosynthesis and ΔysfA / ΔysfE / ΔysfG gene inactivation).
- evidence_id: liu-2021-anie-pmid33155752
  kind: primary_source
  reference: DOI:10.1002/anie.202007777
  locator: Liu et al., Angew. Chem. Int. Ed. 2021;60(1):153-158 (PMID:33155752, 'An
    Unusual Type II Polyketide Synthase System Involved in Cinnamoyl Lipid Biosynthesis')
  accessed_at: '2026-10-25T05:41:00.000000Z'
  support: supports
  summary: Liu et al. (2021, PMID:33155752, DOI:10.1002/anie.202007777; authors Zengzhi
    Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li —
    no author named Deng) establish the enzymatic mechanism of the YsfA..YsfL type
    II PKS system in Streptomyces youssoufiensis OUC6819 through in vivo gene inactivation
    (ΔysfB, ΔysfC, ΔysfD, ΔysfE, ΔysfF, ΔysfH, ΔysfI, ΔysfJ, ΔysfK, ΔysfL) and in
    vitro reconstitution of purified YsfA, YsfB/YsfC, YsfD/YsfE, YsfJ/YsfK, YsfF,
    YsfH, and YsfI.
- evidence_id: corpus-worklist
  kind: validation
  reference: scripts/curation_worklist.py
  locator: 'Full-corpus checkpoint: 3,116 natural product owners (290 with inline
    causal_graphs, 27 with causal_graph_refs) and 246 standalone causal graph components
    (3,362 total YAML records) at d14547bc76e0582aca15eeb073e203d28ea7548e'
  accessed_at: '2026-10-25T05:38:08.000000Z'
  support: supports
  snapshot_sha256: 913508ca8df2eb5c037cd9e4769b14b027869ab78c7306f33b59e1c7e383a1c3
  summary: Deterministic worklist, lockfile, and graph-component checks confirm 3,116
    valid owner records and 246 standalone causal graph components (8,922 worklist
    items across 12 queues), with all 5 youssoufene cohort members in SEEDED status.
assessments:
- assessment_id: cohort-identity-and-ysf-biosynthesis
  area: identity
  topic: Chemical structure grounding and 4-step YsfB/YsfC, YsfD/YsfE, YsfG, and YsfJ/YsfK
    biosynthetic pathway and 13-node / 12-edge causal graph verification
  outcome: supported
  summary: 'All five cohort records carry distinct, stereochemically complete Standard
    InChIKeys and ground to committed project-minted naturalproductmech:mibig-* identifiers
    with grounding_status: MINTED (youssoufene A1 PBGNPVWDTRYFBH-GSOXOQHNSA-N, youssoufene
    B1 ODPDWQHBVRLWMV-JTWCGSJHSA-N, youssoufene B2 ODPDWQHBVRLWMV-WEQBXWHASA-N, youssoufene
    B3 WDDIDKVGAUZJRA-SLWKRUQWSA-N, and youssoufene B4 WDDIDKVGAUZJRA-CGAUJLMDSA-N)
    with zero ChEBI/PubChem false merges. All 5 records carry verified 4-step biosynthetic_pathway
    entries (step 1: YsfB/YsfC KS/CLF complex; step 2: YsfD/YsfE KS/CLF complex; step
    3: YsfG isomerase [NCBIProtein:QHB92594.1]; step 4: YsfJ/YsfK KS/CLF complex;
    with exact A1 dimerization and release left unexpanded on youssoufene-a1.yaml)
    and 13-node / 12-edge BIOSYNTHESIS causal_graphs grounding 7 ENZYME nodes (nodes[0..6])
    from Streptomyces youssoufiensis OUC6819 (MN844187.1) to exact GenBank protein
    and UniParc accessions (YsfB NCBIProtein:QHB92589.1 / UniParc:UPI00131FE52F, YsfC
    NCBIProtein:QHB92590.1 / UniParc:UPI00131FCA94, YsfD NCBIProtein:QHB92591.1 /
    UniParc:UPI00131FC4C1, YsfE NCBIProtein:QHB92592.1 / UniParc:UPI00131FAF34, YsfG
    NCBIProtein:QHB92594.1 / UniParc:UPI001320438E, YsfJ NCBIProtein:QHB92597.1 /
    UniParc:UPI00131F724F, YsfK NCBIProtein:QHB92598.1 / UniParc:UPI0013202848), 3
    UNGROUNDED PROTEIN_COMPLEX nodes (nodes[7..9]: ysfbc_ks_clf, ysfde_ks_clf, ysfjk_ks_clf
    linked from their subunit ENZYME nodes via ''is subunit of'' edges[0..5]), 2 UNGROUNDED
    PROCESS nodes (nodes[10..11]: acp_tethered_chain_elongation, benzene_ring_closure),
    and 1 GROUNDED COMPOUND node (nodes[12]), passing strict LinkML and ontology ID-label
    validation.'
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - li-2020-orglett-pmid31891272
  - liu-2021-anie-pmid33155752
  - corpus-worklist
- assessment_id: ouc6819-producer-strain-completeness
  area: completeness
  topic: Missing OUC6819 producer strain qualification on Streptomyces youssoufiensis
    (NCBITaxon:654447, BGC0002547:1..5)
  outcome: concern
  summary: Across all 5 cohort records, producer_organisms[0] (NCBITaxon:654447, Streptomyces
    youssoufiensis, mibig:BGC0002547, genbank:MN844187.1, PMID:31891272) omits producer_organisms[0].strain
    because MIBiG 4.0 exports species-level organism_name='Streptomyces youssoufiensis'.
    GenBank MN844187.1, Li et al. (2020, PMID:31891272, DOI:10.1021/acs.orglett.9b04559),
    Liu et al. (2021, PMID:33155752, DOI:10.1002/anie.202007777), and the records'
    own biosynthetic_pathway and causal_graphs notes and protein_examples[0].strain
    explicitly identify the sequenced producer strain as Streptomyces youssoufiensis
    OUC6819.
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - li-2020-orglett-pmid31891272
  - liu-2021-anie-pmid33155752
- assessment_id: anie-202007777-author-attribution
  area: provenance
  topic: Misattributed author citation ('Deng et al.' instead of 'Liu et al.') on
    DOI:10.1002/anie.202007777 evidence notes
  outcome: concern
  summary: Across all 5 cohort records, every evidence item in biosynthetic_pathway[0..3].evidence[0].notes
    (4 per record) and causal_graphs[0].edges[0..11].evidence[0].notes (12 per record)
    that cites DOI:10.1002/anie.202007777 (Angew. Chem. Int. Ed. 2021;60(1):153-158,
    PMID:33155752) refers to the authors as 'Deng et al.' (16 evidence notes on youssoufene-a1.yaml
    and 16 evidence notes on each of youssoufene-b1.yaml through youssoufene-b4.yaml;
    80 total). However, DOI:10.1002/anie.202007777 is authored by Zengzhi Liu, Jing
    Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li (Liu et al.,
    with no author named Deng; Zhaoxian Deng was a co-author on the earlier Org. Lett.
    2020 discovery paper DOI:10.1021/acs.orglett.9b04559, not on DOI:10.1002/anie.202007777).
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  evidence_ids:
  - cohort-owners
  - li-2020-orglett-pmid31891272
  - liu-2021-anie-pmid33155752
- assessment_id: npclassifier-ks-clf-and-bgc0002510-boundaries
  area: representation
  topic: NPClassifier dimeric/monomeric pathway split, UNGROUNDED KS/CLF heterodimers,
    and genus-level BGC0002510 taxon boundary
  outcome: concern
  summary: 'Three upstream representation and source boundaries affect the 5-record
    cohort: (1) NPClassifier (npclassifier.gnps2.org@2026-09-07) classifies dimeric
    youssoufene A1 under POLYKETIDES (np_classification.superclass_results: [Linear
    polyketides]) while returning empty pathway_results: [] for monomeric youssoufenes
    B1-B4 (which file under data/natural_products/unclassified/ with np_pathway: UNCLASSIFIED
    despite bgc_class: [PKS]); (2) the three heterodimeric type II PKS KS/CLF PROTEIN_COMPLEX
    nodes (nodes[7..9]: ysfbc_ks_clf, ysfde_ks_clf, ysfjk_ks_clf) remain UNGROUNDED
    at the complex level (while their constituent subunit ENZYME nodes nodes[0..3,
    5..6] YsfB/YsfC, YsfD/YsfE, and YsfJ/YsfK carry grounding.id and protein_examples
    and connect via ''is subunit of'' edges[0..5]), and biosynthetic_pathway steps[0..1,
    3] omit scalar enzyme_id and steps[0..3] omit reaction_id because ComplexPortal
    and RHEA lack entries for these bacterial type II PKS heterodimers and polyene-forming
    steps; and (3) producer_organisms[1] (NCBITaxon:1931, Streptomyces sp., mibig:BGC0002510,
    genbank:MT459140.1:71..11851, PMID:32860295) remains genus-level without strain
    qualification because MIBiG 4.0 exports NCBITaxon:1931 and PMID:32860295 / MT459140.1
    are not indexed in PubMed/ENA to verify a cultured strain designation.'
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - npclassifier-table
  - liu-2021-anie-pmid33155752
findings:
- finding_id: F-YSF-001
  issue_key: streptomyces-youssoufiensis-bgc0002547-ouc6819-producer-strain-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Missing OUC6819 producer strain qualifications on Streptomyces youssoufiensis
    (NCBITaxon:654447, BGC0002547:1..5) across all 5 youssoufene records
  description: All five Streptomyces youssoufiensis (NCBITaxon:654447) producer_organisms[0]
    claims seeded from BGC0002547:1..5 (MN844187.1:1..20186, PMID:31891272; row sha256s
    1d48b2327fd1ff6df8dacc84f722e6dcef3c298cafc6442b51a0d2190b11547f on youssoufene-a1.yaml,
    acd26c9ce0f501c27e8a2d0097dce5d2fbee8400976c822752702b3b9c486417 on youssoufene-b1.yaml,
    ea799308511137361955d15f115be158a232e46e13f06711cf9e271ad1fe89ed on youssoufene-b2.yaml,
    e9c6f5c63380450c1cd78dee862c1662fb8c78e013db12318271be20b551eeae on youssoufene-b3.yaml,
    and deba7c35303ec40e78d46bdb947fd45ba3e178c5547f16c8540e2ec60909e553 on youssoufene-b4.yaml)
    omit producer_organisms[0].strain. GenBank MN844187.1, Li et al. (2020, PMID:31891272,
    DOI:10.1021/acs.orglett.9b04559), Liu et al. (2021, PMID:33155752, DOI:10.1002/anie.202007777),
    and the records' own biosynthetic_pathway and causal_graphs notes and protein_examples[0].strain
    explicitly identify the sequenced producer strain as Streptomyces youssoufiensis
    OUC6819.
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  field_paths:
  - producer_organisms[0].strain
  - producer_organisms[0].evidence
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - li-2020-orglett-pmid31891272
  - liu-2021-anie-pmid33155752
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/youssoufene-a1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      A1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b2.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B2)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b3.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B3)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b4.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B4)
  rule_id: review-checklist:producer-strain-qualification
  native_severity: major
  normalization_reason: Omission of explicitly published sequenced producer strain
    OUC6819 across five BGC0002547 compound rows is a material completeness gap directly
    resolvable via curation/mibig_producer_strains.tsv.
- finding_id: F-YSF-002
  issue_key: youssoufene-cohort-anie-202007777-author-attribution-mismatch
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Misattributed author citation ('Deng et al.' instead of 'Liu et al.') on
    DOI:10.1002/anie.202007777 evidence notes across all 5 youssoufene records
  description: Across all five youssoufene YAML records (youssoufene-a1.yaml and youssoufene-b1.yaml
    through youssoufene-b4.yaml), all 16 evidence items per record (80 total across
    the cohort) in biosynthetic_pathway[0..3].evidence[0].notes (4 per record) and
    causal_graphs[0].edges[0..11].evidence[0].notes (12 per record) that cite DOI:10.1002/anie.202007777
    (Angew. Chem. Int. Ed. 2021;60(1):153-158, PMID:33155752) attribute the study
    to 'Deng et al.' in their prose notes. In fact, DOI:10.1002/anie.202007777 is
    authored by Zengzhi Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian
    Dong, and Wenli Li (Liu et al.), with no author named Deng (Zhaoxian Deng was
    a co-author on the earlier 2020 Org. Lett. discovery paper DOI:10.1021/acs.orglett.9b04559,
    PMID:31891272).
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  field_paths:
  - biosynthetic_pathway[*].evidence[0].notes
  - causal_graphs[0].edges[*].evidence[0].notes
  evidence_ids:
  - cohort-owners
  - li-2020-orglett-pmid31891272
  - liu-2021-anie-pmid33155752
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/youssoufene-a1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      A1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b2.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B2)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b3.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B3)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b4.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B4)
  rule_id: review-checklist:claim-specific-citation-routing
  native_severity: major
  normalization_reason: Citing DOI:10.1002/anie.202007777 (Liu et al. 2021) as 'Deng
    et al.' across 80 curator-owned biosynthetic_pathway and causal_graphs evidence
    notes misstates primary-source authorship and is directly remediable in Stage
    5.
- finding_id: F-YSF-003
  issue_key: youssoufene-cohort-npclassifier-ks-clf-and-bgc0002510-boundaries
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Upstream NPClassifier dimeric/monomeric split, UNGROUNDED KS/CLF heterodimer
    complexes, and genus-level BGC0002510 taxon boundary
  description: '1) NPClassifier (npclassifier.gnps2.org@2026-09-07) classifies dimeric
    youssoufene A1 (PBGNPVWDTRYFBH-GSOXOQHNSA-N) under POLYKETIDES (Linear polyketides),
    while returning empty pathway_results: [] for monomeric congeners youssoufenes
    B1-B4 (which therefore file under data/natural_products/unclassified/ with np_pathway:
    UNCLASSIFIED despite bgc_class: [PKS]). 2) The three heterodimeric type II PKS
    KS/CLF PROTEIN_COMPLEX nodes (nodes[7..9]: ysfbc_ks_clf, ysfde_ks_clf, ysfjk_ks_clf)
    remain UNGROUNDED at the complex level (while their constituent subunit ENZYME
    nodes nodes[0..3, 5..6] carry grounding.id and protein_examples and connect via
    ''is subunit of'' edges[0..5]), biosynthetic_pathway[0..1, 3] omit scalar enzyme_id,
    and biosynthetic_pathway[0..3] omit reaction_id because ComplexPortal and RHEA
    lack entries for these bacterial type II PKS heterodimers and polyene-forming
    steps. 3) producer_organisms[1] (NCBITaxon:1931, Streptomyces sp., mibig:BGC0002510,
    genbank:MT459140.1:71..11851, PMID:32860295) remains at genus level without strain
    qualification because MIBiG 4.0 exports NCBITaxon:1931 and PMID:32860295 / MT459140.1
    are not indexed in PubMed/ENA to verify a cultured strain designation.'
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  field_paths:
  - np_pathway
  - np_classification.pathway_results
  - np_classification.superclass_results
  - producer_organisms[1].taxon_id
  - producer_organisms[1].strain
  - biosynthetic_pathway[0].enzyme_id
  - biosynthetic_pathway[0].reaction_id
  - biosynthetic_pathway[1].enzyme_id
  - biosynthetic_pathway[1].reaction_id
  - biosynthetic_pathway[2].reaction_id
  - biosynthetic_pathway[3].enzyme_id
  - biosynthetic_pathway[3].reaction_id
  - causal_graphs[0].nodes[7].grounding_status
  - causal_graphs[0].nodes[8].grounding_status
  - causal_graphs[0].nodes[9].grounding_status
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - npclassifier-table
  - liu-2021-anie-pmid33155752
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/youssoufene-a1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      A1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b2.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B2)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b3.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B3)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b4.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B4)
  rule_id: review-checklist:exact-structure-and-deposit-boundary
  native_severity: minor
  normalization_reason: Faithful reflection of pinned NPClassifier output, ComplexPortal/RHEA
    coverage limits on heterodimeric type II PKS enzymes, and unindexed MT459140.1
    / PMID:32860295 metadata; documented as a source/representation boundary.
actions:
- action_id: qualify-youssoufiensis-ouc6819-producer-strains
  description: Add five source-pinned producer strain rows to curation/mibig_producer_strains.tsv
    (columns source_id, expected_source_row_sha256, strain, reference, curator, date,
    rationale) for source_id=BGC0002547:1..5 (expected_source_row_sha256s 1d48b2327fd1ff6df8dacc84f722e6dcef3c298cafc6442b51a0d2190b11547f,
    acd26c9ce0f501c27e8a2d0097dce5d2fbee8400976c822752702b3b9c486417, ea799308511137361955d15f115be158a232e46e13f06711cf9e271ad1fe89ed,
    e9c6f5c63380450c1cd78dee862c1662fb8c78e013db12318271be20b551eeae, and deba7c35303ec40e78d46bdb947fd45ba3e178c5547f16c8540e2ec60909e553,
    strain='OUC6819', reference=PMID:31891272), then re-seed via scripts/seed_from_sources.py.
  finding_ids:
  - F-YSF-001
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/youssoufene-a1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      A1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b2.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B2)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b3.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B3)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b4.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B4)
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Verify expected_source_row_sha256 pins for BGC0002547:1..5 in curation/mibig_producer_strains.tsv.
  - 'Run scripts/seed_from_sources.py and confirm producer_organisms[0] (NCBITaxon:654447,
    mibig:BGC0002547) carries strain: OUC6819 across all 5 youssoufene YAML records.'
  - Verify zero regressions across scripts/validate_strict.py and scripts/verify_corpus.py.
- action_id: fix-anie-202007777-liu-et-al-attribution
  description: Update the 16 evidence notes per record (80 total) citing DOI:10.1002/anie.202007777
    in biosynthetic_pathway[0..3].evidence[0].notes and causal_graphs[0].edges[0..11].evidence[0].notes
    across youssoufene-a1.yaml and youssoufene-b1.yaml through youssoufene-b4.yaml
    to replace 'Deng et al.' with 'Liu et al. (2021)' (matching Zengzhi Liu, Jing
    Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li, Angew. Chem.
    Int. Ed. 2021;60(1):153-158, PMID:33155752), append a CURATION_REVIEW_FIX history
    entry, and regenerate HTML pages.
  finding_ids:
  - F-YSF-002
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/youssoufene-a1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      A1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b2.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B2)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b3.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B3)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b4.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B4)
  acceptance_checks:
  - Confirm zero occurrences of 'Deng et al.' on evidence items citing DOI:10.1002/anie.202007777
    across all 5 youssoufene YAML records.
  - Confirm scripts/validate_strict.py, scripts/verify_corpus.py, and pytest tests/test_graph_components.py
    pass with zero errors.
- action_id: preserve-youssoufene-representation-boundaries
  description: Retain locked PATHS.tsv filing (POLYKETIDES for youssoufene-a1.yaml
    and UNCLASSIFIED for youssoufene-b1.yaml through youssoufene-b4.yaml), retain
    UNGROUNDED PROTEIN_COMPLEX status on nodes[7..9] (ysfbc_ks_clf, ysfde_ks_clf,
    ysfjk_ks_clf) with subunit ENZYME nodes[0..3, 5..6] connected via 'is subunit
    of' edges[0..5], and retain genus-level NCBITaxon:1931 without strain on BGC0002510:1..5.
  finding_ids:
  - F-YSF-003
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/npclassifier.tsv
    role: Pinned NPClassifier chemical classification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/youssoufene-a1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      A1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b1.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B1)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b2.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B2)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b3.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B3)
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/unclassified/youssoufene-b4.yaml
    role: Generated and curator-enriched natural product owner record (youssoufene
      B4)
  acceptance_checks:
  - Do not alter locked PATHS.tsv paths or invent ComplexPortal/RHEA identifiers or
    unverified BGC0002510 strain names.
boundary_decisions:
- action: retain
  target_ids:
  - naturalproductmech:mibig-78ea4c55fb
  - naturalproductmech:mibig-ccb60942af
  - naturalproductmech:mibig-cf5248036e
  - naturalproductmech:mibig-f827d9f550
  - naturalproductmech:mibig-18ba3c758c
  rationale: 'All five cohort records represent distinct, stereochemically defined
    natural products isolated from Streptomyces youssoufiensis OUC6819 with distinct
    Standard InChIKeys: dimeric youssoufene A1 (PBGNPVWDTRYFBH-GSOXOQHNSA-N) and monomeric
    E/Z geometric isomers youssoufene B1 (ODPDWQHBVRLWMV-JTWCGSJHSA-N), youssoufene
    B2 (ODPDWQHBVRLWMV-WEQBXWHASA-N), youssoufene B3 (WDDIDKVGAUZJRA-SLWKRUQWSA-N),
    and youssoufene B4 (WDDIDKVGAUZJRA-CGAUJLMDSA-N).'
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - li-2020-orglett-pmid31891272
  - liu-2021-anie-pmid33155752
limitations:
- Stage 4 is strictly read-only with respect to scientific YAML records and curation
  TSVs; all proposed curation edits are preserved as open findings for Stage 5 grouped
  remediation.
- Full-corpus deterministic checks (verify_corpus.py, validate_id_label_correspondence.py,
  curation_worklist.py --review-records, pytest tests/test_graph_components.py) audited
  all 3,116 owners and 246 standalone causal graph components (3,362 total YAML records),
  while claim-by-claim primary literature verification in this bundle was scoped to
  the 5-record Streptomyces youssoufiensis / Streptomyces sp. youssoufene cohort.
- INSDC accession MT459140.1 and PMID:32860295 (BGC0002510) are not indexed in ENA
  or PubMed, preventing independent verification of a cultured strain designation
  for producer_organisms[1] (NCBITaxon:1931).
```
