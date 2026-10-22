# Pikromycin/methymycin/desosamine (pik/des) macrolide-deoxysugar cohort review

- Review: 20261022T012300Z-pik-des-macrolide-deoxysugar-cohort
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-22T01:12:00.000000Z
- Finished UTC: 2026-10-22T01:23:00.000000Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full 6-record category review of the Streptomyces venezuelae ATCC 15439 pik/des macrolide-deoxysugar cohort (BGC0000094, BGC0000898) and the homologous Streptomyces narbonensis desosamine cluster (BGC0000899), anchored to a full-corpus deterministic checkpoint of all 3,116 natural product owners and 246 standalone causal graph components (3,362 total YAML records). Confirms clean SPLIT_SHARED_WITH_CHEBI separation of D-desosamine (CHEBI:32540, desosamine-2.yaml) from methymycin (CHEBI:29630, methymycin.yaml), while identifying three open findings for Stage 5 grouped remediation: (1) missing ATCC 15439 strain qualification across the five S. venezuelae compound rows BGC0000094:1 and BGC0000898:1..4 (F-PIK-DES-001), (2) cross-species Xue et al. 1998 (PMID:9770448 / DOI:10.1073/PNAS.95.21.12111) citation transfer onto S. narbonensis BGC0000899:1 and LOTUS occurrences[0] in desosamine.yaml (F-PIK-DES-002), and (3) upstream tautomeric/stereochemical and GenBank deposit-split boundaries between BGC0000899, BGC0000898, and BGC0000094 across all 6 cohort records (F-PIK-DES-003).

## Scope And Provenance

Coherent 6-record biosynthetic and chemical-identity cohort covering all NaturalProductMech records seeded from MIBiG BGC0000094, BGC0000898, and BGC0000899, evaluated alongside frozen full-corpus inventory checks (3,116 owner YAML records and 246 standalone causal graph components; 3,362 total YAML records).

Selection: All records derived from the S. venezuelae pik/des gene clusters (BGC0000094:1, BGC0000898:1..4) and the homologous S. narbonensis des cluster (BGC0000899:1), selected to audit the Cycle 1 Stage 1 SPLIT_SHARED_WITH_CHEBI structure split and its cohort-wide producer, locus, and citation consistency.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: git_commit at Git base f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CHEBI:32540 | data/natural_products/carbohydrates/desosamine-2.yaml | generated | desosamine |
| naturalproductmech:mibig-bc0da8b0f6 | data/natural_products/carbohydrates/desosamine.yaml | generated | desosamine |
| CHEBI:29630 | data/natural_products/polyketides/methymycin.yaml | generated | methymycin |
| CHEBI:29665 | data/natural_products/polyketides/pikromycin.yaml | generated | pikromycin |
| CHEBI:29656 | data/natural_products/polyketides/neomethymycin.yaml | generated | neomethymycin |
| CHEBI:29649 | data/natural_products/polyketides/narbomycin.yaml | generated | narbomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native source inspection (cohort) | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | Captured exact Git base f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf and verified SHA256 digests for all 6 cohort target YAML files. |
| Strict schema and semantic validation (cohort) | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | All 6 cohort YAML files passed strict LinkML validation with 0 ERROR rows. |
| Full-corpus lockfile and filing verification | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | Verified lockfile integrity across all 3,116 natural product owner records against data/natural_products/PATHS.tsv. |
| Full-corpus ontology ID-label correspondence | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | Full-corpus ID-label check passed (13,449 canonical, 646 synonym, 35 exception, 0 ID_NOT_FOUND); all ChEBI and NCBITaxon terms on the 6 cohort records resolve canonically. |
| Exhaustive corpus review-queue checkpoint | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | Computed exhaustive review-records queue across all 3,116 corpus owners (8,905 worklist items across 11 queues, 8,928 output lines with --limit 5: producer-evidence 2,292; biosynthesis 1,192; structure-disagreement 5; name-disagreement 67; unnamed-producer 39; shared-structure 207; needs-a-name 18; occurrence-only 12; pathway-ambiguous 620; unresolved-taxa 3,329; stereo-incomplete 1,124); all 6 cohort records appear in producer-evidence (1 SOURCE_ASSERTION producer each) and desosamine.yaml additionally appears in stereo-incomplete. |
| Repository-wide identifier and BGC cross-reference search | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | Verified all repository references to BGC0000094, BGC0000898, BGC0000899, and cohort identifiers across raw inventories, curation tables, records, and tests. |
| Full-corpus standalone causal graph component validation | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | Validated all 246 standalone causal graph component YAML files under data/causal_graphs/ (40 passed, 0 failed). |

## Scientific And Domain Assessments

### Chemical structure identity and SPLIT_SHARED_WITH_CHEBI separation across the 6-record cohort

identity: supported. Targets: CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649.

Each of the four macrolide antibiotics (methymycin CHEBI:29630, pikromycin CHEBI:29665, neomethymycin CHEBI:29656, narbomycin CHEBI:29649) and the two desosamine records (open-chain D-desosamine CHEBI:32540 and cyclic flat-ring desosamine naturalproductmech:mibig-bc0da8b0f6) carries a distinct Standard InChIKey verified against ChEBI 3-star structures and MIBiG 4.0 rows. BGC0000898:1 is cleanly separated from methymycin.yaml onto desosamine-2.yaml with upstream methymycin xrefs stripped.

### Missing ATCC 15439 producer strain qualification on S. venezuelae BGC0000094 and BGC0000898 records

completeness: concern. Targets: CHEBI:32540, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649.

All five Streptomyces venezuelae records (desosamine-2.yaml, methymycin.yaml, pikromycin.yaml, neomethymycin.yaml, narbomycin.yaml) cite PMID:9770448 (DOI:10.1073/pnas.95.21.12111) and GenBank AF079138.1 / AF079762.1, which explicitly name strain ATCC 15439, but producer_organisms[0].strain is currently omitted because BGC0000094:1 and BGC0000898:1..4 are absent from curation/mibig_producer_strains.tsv.

### Cross-species Xue et al. 1998 citation (PMID:9770448 / DOI:10.1073/PNAS.95.21.12111) on S. narbonensis BGC0000899:1 and LOTUS occurrence (desosamine.yaml)

provenance: concern. Targets: naturalproductmech:mibig-bc0da8b0f6.

desosamine.yaml (naturalproductmech:mibig-bc0da8b0f6) asserts producer Streptomyces narbonensis (NCBITaxon:67333) and locus genbank:AF521878.1 via MIBiG BGC0000899:1 entry citation PMID:9770448, and simultaneously asserts a LOTUS occurrence for NCBITaxon:67333 citing DOI:10.1073/PNAS.95.21.12111 (the DOI of PMID:9770448). Because Xue et al. (1998) exclusively study Streptomyces venezuelae ATCC 15439, BGC0000899:1 claim references should be routed to BGC0000899.4 and GenBank AF521878.1 via curation/mibig_claim_references.tsv, and the mis-referenced LOTUS row should be excluded via curation/lotus_occurrence_exclusions.tsv.

### Tautomeric/stereochemical separation of desosamine.yaml vs desosamine-2.yaml and BGC0000898 deposit split

representation: concern. Targets: CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649.

desosamine.yaml (ZOYWWAGVGBSJDL-UHFFFAOYSA-N, flat cyclic hexopyranose, stereo_complete=false) and desosamine-2.yaml (VTJCSBJRQLZNHE-CSMHCCOUSA-N, 3-star ChEBI open-chain D-desosamine aldehyde, stereo_complete=true) remain separate records because ChEBI lacks a 3-star stereochemically complete cyclic D-desosamine entry and MIBiG BGC0000899:1 lacks stereochemical assignment. Additionally, MIBiG splits the S. venezuelae ATCC 15439 locus across BGC0000094 (AF079138.1, CLUSTER_DEMONSTRATED) and BGC0000898 (AF079762.1, CLUSTER_UNSTATED without coordinates).

### NPClassifier pathway filing, lockfile stability, and ontology label alignment

consistency: supported. Targets: CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649.

Both desosamine records file under CARBOHYDRATES and all four macrolides file under POLYKETIDES in agreement with data/raw/npclassifier.tsv and data/natural_products/PATHS.tsv; all ontology labels pass validate_id_label_correspondence.py.

## Findings

### F-PIK-DES-001: Missing ATCC 15439 producer strain qualification on five S. venezuelae pik/des records

major / open / confirmed; issue key: pik-des-atcc15439-producer-strain-missing.

The five Streptomyces venezuelae (NCBITaxon:54571) records seeded from MIBiG compound rows BGC0000094:1 (methymycin.yaml, sha256 4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5), BGC0000898:1 (desosamine-2.yaml, sha256 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae), BGC0000898:2 (pikromycin.yaml, sha256 224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923), BGC0000898:3 (neomethymycin.yaml, sha256 002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead), and BGC0000898:4 (narbomycin.yaml, sha256 1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578) omit producer_organisms[0].strain even though their primary reference Xue et al., PNAS 1998 (PMID:9770448, DOI:10.1073/pnas.95.21.12111) and GenBank deposits AF079138.1 and AF079762.1 explicitly identify the producer strain as Streptomyces venezuelae ATCC 15439. Add source-pinned ATCC 15439 qualifications for source_id keys BGC0000094:1, BGC0000898:1, BGC0000898:2, BGC0000898:3, and BGC0000898:4 in curation/mibig_producer_strains.tsv.

### F-PIK-DES-002: Cross-species Xue et al. 1998 citation (PMID:9770448 / DOI:10.1073/PNAS.95.21.12111) attached to S. narbonensis BGC0000899:1 and LOTUS occurrence in desosamine.yaml

major / open / confirmed; issue key: bgc0000899-narbonensis-cross-species-pmid9770448-citation.

data/natural_products/carbohydrates/desosamine.yaml (naturalproductmech:mibig-bc0da8b0f6) carries cross-species citations to Xue et al., PNAS 1998 (PMID:9770448 / DOI:10.1073/PNAS.95.21.12111) on three claims for Streptomyces narbonensis (NCBITaxon:67333): (1) producer_organisms[0].evidence[0].reference and (2) biosynthetic_gene_clusters[0].evidence[0].reference (seeded from MIBiG BGC0000899:1, sha256 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922, with notes "MIBiG BGC0000899 entry version 4; citation taken from the entry level" on genome_accession genbank:AF521878.1), and (3) occurrences[0].evidence[0].reference (seeded from LOTUS row ZOYWWAGVGBSJDL-UHFFFAOYSA-N &#124; NCBITaxon:67333 &#124; 10.1073/PNAS.95.21.12111, expected_source_row_sha256 c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e). Because Xue et al. (1998) exclusively characterize Streptomyces venezuelae ATCC 15439 (AF079138.1 / AF079762.1) and never report S. narbonensis or AF521878.1 (deposited in 2002), Stage 5 must both route BGC0000899:1 in curation/mibig_claim_references.tsv and exclude the mis-referenced LOTUS row in curation/lotus_occurrence_exclusions.tsv.

### F-PIK-DES-003: Upstream tautomeric/stereochemical separation of desosamine records and BGC0000898/BGC0000094 deposit split

minor / open / confirmed; issue key: desosamine-cyclic-open-chain-and-bgc0000898-locus-split.

Two upstream source-representation boundaries affect this cohort: (1) desosamine.yaml (naturalproductmech:mibig-bc0da8b0f6, BGC0000899:1) encodes flat cyclic hexopyranose ZOYWWAGVGBSJDL-UHFFFAOYSA-N (stereo_complete=false) whereas desosamine-2.yaml (CHEBI:32540, BGC0000898:1) encodes 3-star ChEBI open-chain D-desosamine aldehyde VTJCSBJRQLZNHE-CSMHCCOUSA-N (stereo_complete=true), and ChEBI lacks a 3-star stereochemically complete cyclic D-desosamine entry; (2) MIBiG 4.0 splits the S. venezuelae ATCC 15439 pik/des cluster across BGC0000094 (AF079138.1, CLUSTER_DEMONSTRATED) and BGC0000898 (AF079762.1, CLUSTER_UNSTATED with blank locus coordinates and methods). Merging the two desosamine records or upgrading BGC0000898 locus grades without deposit-level sequence alignment and a curated cyclic D-desosamine ChEBI target would violate exact-structure and deposit-scoped grading rules.

## Recommended Actions And Acceptance Checks

### qualify-atcc15439-producer-strain

Add source-pinned ATCC 15439 strain qualification rows for compound-row keys BGC0000094:1 (4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5), BGC0000898:1 (1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae), BGC0000898:2 (224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923), BGC0000898:3 (002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead), and BGC0000898:4 (1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578) citing DOI:10.1073/pnas.95.21.12111 to curation/mibig_producer_strains.tsv and re-seed the five S. venezuelae records via scripts/seed_from_sources.py.

- Verify exact_source_row_sha256 pins for BGC0000094:1 and BGC0000898:1..4 in curation/mibig_producer_strains.tsv.
- Run scripts/seed_from_sources.py and confirm producer_organisms[0].strain == ATCC 15439 on methymycin.yaml, desosamine-2.yaml, pikromycin.yaml, neomethymycin.yaml, and narbomycin.yaml.
- Verify zero regressions across scripts/validate_strict.py and scripts/verify_corpus.py.

### route-bgc0000899-claim-references

Add a source-pinned claim-reference override for source_id BGC0000899:1 (expected_source_row_sha256 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922) in curation/mibig_claim_references.tsv routing producer_reference to https://mibig.secondarymetabolites.org/repository/BGC0000899.4/ and locus_reference/source_reference to https://www.ncbi.nlm.nih.gov/nuccore/AF521878.1, add a source-pinned LOTUS occurrence exclusion row (ZOYWWAGVGBSJDL-UHFFFAOYSA-N, NCBITaxon:67333, 10.1073/PNAS.95.21.12111, expected_source_row_sha256 c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e) in curation/lotus_occurrence_exclusions.tsv, and re-seed desosamine.yaml.

- Verify expected_source_row_sha256 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922 for BGC0000899:1 in curation/mibig_claim_references.tsv.
- Verify expected_source_row_sha256 c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e for (ZOYWWAGVGBSJDL-UHFFFAOYSA-N, NCBITaxon:67333, 10.1073/PNAS.95.21.12111) in curation/lotus_occurrence_exclusions.tsv.
- Re-seed desosamine.yaml via scripts/seed_from_sources.py and confirm producer and locus claims cite BGC0000899.4 and AF521878.1 with CURATOR_INFERENCE routing provenance and that the cross-species LOTUS occurrence is excluded.
- Verify scripts/validate_strict.py and scripts/verify_corpus.py pass with zero errors.

### preserve-desosamine-tautomer-and-deposit-separation

Retain separate records for CHEBI:32540 (desosamine-2.yaml, open-chain D-desosamine aldehyde) and naturalproductmech:mibig-bc0da8b0f6 (desosamine.yaml, stereo-incomplete cyclic desosamine) and retain deposit-scoped BGC0000898 grading until upstream ChEBI cyclic D-desosamine grounding and AF079762.1/AF079138.1 coordinate alignment are available.

- Do not merge different InChIKeys (VTJCSBJRQLZNHE-CSMHCCOUSA-N vs ZOYWWAGVGBSJDL-UHFFFAOYSA-N) without a 3-star stereochemically complete ChEBI target.
- Do not transfer AF079138.1 locus_evidence_methods onto AF079762.1 without verified sequence-coordinate equivalence.

## Category Boundaries

- retain: CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649. All six cohort records represent distinct committed Standard InChIKeys: four macrolide antibiotics (CHEBI:29630 methymycin, CHEBI:29665 pikromycin, CHEBI:29656 neomethymycin, CHEBI:29649 narbomycin) and two desosamine representations (CHEBI:32540 stereochemically complete open-chain D-desosamine aldehyde from S. venezuelae BGC0000898:1 vs naturalproductmech:mibig-bc0da8b0f6 stereo-incomplete flat cyclic hexopyranose from S. narbonensis BGC0000899:1). BGC0000898:1 is already properly split from methymycin.yaml via SPLIT_SHARED_WITH_CHEBI.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cohort-owners | data/natural_products/PATHS.tsv; desosamine-2.yaml, desosamine.yaml, methymycin.yaml, pikromycin.yaml, neomethymycin.yaml, narbomycin.yaml at f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf | supports | All 6 cohort YAML files are present at their locked PATHS.tsv locations with distinct Standard InChIKeys, valid LinkML structure, and SEEDED curation status. |
| mibig-inventory | data/raw/mibig_compounds.tsv; BGC0000094:1 (sha256 4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5), BGC0000898:1..4 (sha256s 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae, 224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923, 002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead, 1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578), BGC0000899:1 (sha256 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922) | partial | MIBiG 4.0 exports species-level NCBITaxon:54571 (S. venezuelae) on BGC0000094:1 (AF079138.1) and BGC0000898:1..4 (AF079762.1) and NCBITaxon:67333 (S. narbonensis) on BGC0000899:1 (AF521878.1), all citing entry-level PMID:9770448. |
| chebi-structures | data/raw/chebi_structures.tsv; CHEBI:32540 (VTJCSBJRQLZNHE-CSMHCCOUSA-N), CHEBI:29630 (HUKYPYXOBINMND-HYUJHOPRSA-N), CHEBI:29665 (UZQBOFAUUTZOQE-VSLWXVDYSA-N), CHEBI:29656 (UEIVQYHYALXCBD-OTUJEKPESA-N), CHEBI:29649 (OXFYAOOMMKGGAI-JLTOUBQASA-N) | supports | All five S. venezuelae cohort members ground to 3-star stereochemically complete ChEBI structures; CHEBI:32540 encodes open-chain D-desosamine aldehyde while BGC0000899:1 encodes flat cyclic hexopyranose ZOYWWAGVGBSJDL-UHFFFAOYSA-N absent from 3-star ChEBI. |
| structure-corrections | curation/mibig_structure_corrections.tsv; BGC0000898:1 -&gt; CHEBI:32540 (SPLIT_SHARED_WITH_CHEBI) | supports | SPLIT_SHARED_WITH_CHEBI cleanly routes BGC0000898:1 (desosamine) away from the erroneous methymycin SMILES onto CHEBI:32540 and strips the upstream methymycin xrefs pubchem:5282034&#124;npatlas:NPA01238. |
| pnas-1998 | DOI:10.1073/pnas.95.21.12111; Xue et al., Proc. Natl. Acad. Sci. U.S.A. 1998;95(21):12111-12116 (PMID:9770448); title, abstract, and GenBank AF079138.1 / AF079762.1 strain attribution | supports | Xue et al. (1998) explicitly characterize the pikromycin/methymycin/narbomycin/neomethymycin PKS (pikAI-pikAV), desosamine biosynthesis (desI-desVIII), and P450 hydroxylase (pikC) gene cluster in Streptomyces venezuelae ATCC 15439, and do not study Streptomyces narbonensis AF521878.1. |
| genbank-af521878 | https://www.ncbi.nlm.nih.gov/nuccore/AF521878.1; GenBank AF521878.1 and MIBiG BGC0000899.4 entry metadata for Streptomyces narbonensis desosamine biosynthetic gene cluster | partial | AF521878.1 is a partial desosamine BGC sequence deposit from Streptomyces narbonensis (NCBITaxon:67333); MIBiG BGC0000899.4 attaches PMID:9770448 (which studies S. venezuelae ATCC 15439) at the entry level. |
| corpus-worklist | scripts/curation_worklist.py; Full-corpus checkpoint: 3,116 natural product owners (273 with inline causal_graphs, 27 with causal_graph_refs) and 246 standalone causal graph components (3,362 total YAML records) at f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf | supports | Deterministic worklist, lockfile, and graph-component checks confirm 3,116 valid owner records and 246 standalone causal graph components (8,905 worklist items across 11 queues), with all 6 pik/des cohort members in SEEDED status and queued under producer-evidence. |
| lotus-inventory | data/raw/lotus_occurrences.tsv; ZOYWWAGVGBSJDL-UHFFFAOYSA-N &#124; NCBITaxon:67333 &#124; 10.1073/PNAS.95.21.12111 (expected_source_row_sha256 c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e) | partial | LOTUS exports an occurrence row linking ZOYWWAGVGBSJDL-UHFFFAOYSA-N to NCBITaxon:67333 (Streptomyces narbonensis) via DOI 10.1073/PNAS.95.21.12111 (Xue et al., 1998, PMID:9770448), propagating the same cross-species S. venezuelae ATCC 15439 reference onto occurrences[0] in desosamine.yaml. |

## Limits And Additional Notes

- Stage 4 is strictly read-only with respect to scientific YAML records and curation TSVs; all proposed curation edits are preserved as open findings for Stage 5 grouped remediation.
- Full-corpus deterministic checks (verify_corpus.py, validate_id_label_correspondence.py, curation_worklist.py --review-records, pytest tests/test_graph_components.py) audited all 3,116 owners and 246 standalone causal graph components (3,362 total YAML records), while claim-by-claim primary literature verification in this bundle was scoped to the 6-record pik/des cohort.
- GenBank AF521878.1 (BGC0000899) is a direct sequence submission without a dedicated primary experimental publication in the committed inventory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T012300Z-pik-des-macrolide-deoxysugar-cohort
kind: category
repository: CultureBotAI/NaturalProductMech
title: Pikromycin/methymycin/desosamine (pik/des) macrolide-deoxysugar cohort review
started_at: '2026-10-22T01:12:00.000000Z'
finished_at: '2026-10-22T01:23:00.000000Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Same cycle campaign agent auditing the frozen post-Stage-3 corpus
    inventory; not an external human review.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: SEEDED retained across all 6 cohort records; producer strain ATCC
  15439, BGC0000899:1 claim-reference routing, and LOTUS cross-species occurrence
  exclusion queued for Stage 5
scientific_review: true
summary: 'Full 6-record category review of the Streptomyces venezuelae ATCC 15439
  pik/des macrolide-deoxysugar cohort (BGC0000094, BGC0000898) and the homologous
  Streptomyces narbonensis desosamine cluster (BGC0000899), anchored to a full-corpus
  deterministic checkpoint of all 3,116 natural product owners and 246 standalone
  causal graph components (3,362 total YAML records). Confirms clean SPLIT_SHARED_WITH_CHEBI
  separation of D-desosamine (CHEBI:32540, desosamine-2.yaml) from methymycin (CHEBI:29630,
  methymycin.yaml), while identifying three open findings for Stage 5 grouped remediation:
  (1) missing ATCC 15439 strain qualification across the five S. venezuelae compound
  rows BGC0000094:1 and BGC0000898:1..4 (F-PIK-DES-001), (2) cross-species Xue et
  al. 1998 (PMID:9770448 / DOI:10.1073/PNAS.95.21.12111) citation transfer onto S.
  narbonensis BGC0000899:1 and LOTUS occurrences[0] in desosamine.yaml (F-PIK-DES-002),
  and (3) upstream tautomeric/stereochemical and GenBank deposit-split boundaries
  between BGC0000899, BGC0000898, and BGC0000094 across all 6 cohort records (F-PIK-DES-003).'
source:
  git_revision: f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
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
  - path: curation/pubchem_bioassay_exclusions.tsv
    sha256: 76f9cbb17e62a270afed637b5058a553cfe85c754c6c9ec406635f12dae572fa
    role: context
  - path: data/natural_products/PATHS.tsv
    sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
    role: context
  - path: data/natural_products/carbohydrates/desosamine-2.yaml
    sha256: e9aa2c5f8c764bac920477fda25577f8352012d088382090ec452c9d747c2f26
    role: target
  - path: data/natural_products/carbohydrates/desosamine.yaml
    sha256: 054f874a6fb55098958357acfab7ecc78bcb597cfb04cf5437e9d74d29702c4d
    role: target
  - path: data/natural_products/polyketides/methymycin.yaml
    sha256: 7c19ea9d7cedee074008cf7bed76bdf2f76abf41d8a659507778b26948b416ee
    role: target
  - path: data/natural_products/polyketides/narbomycin.yaml
    sha256: b112dcc3d151dca470cae5bf9f4528892052edae5707ccc2e3c5a88d224f84de
    role: target
  - path: data/natural_products/polyketides/neomethymycin.yaml
    sha256: fc676329e89ea3bbd693300d380a8c11a231e476c51628f50bd9bb8b382ea1ef
    role: target
  - path: data/natural_products/polyketides/pikromycin.yaml
    sha256: f64b4aaadd9a388a8dc4066f2fe15f052ad6a82bf4fc84884907db82d6d940b1
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
    sha256: 58573bcc19cc469884cafd52be38122daa5ebbcb5dedaa684b9022eecd103753
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
    sha256: 8c3e23bb9e16bea0bc839f6c0b3b91ba2f0dbc264d103b00b4887586e708834f
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
- target_id: CHEBI:32540
  path: data/natural_products/carbohydrates/desosamine-2.yaml
  label: desosamine
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/carbohydrates/desosamine-2.yaml
    role: Generated natural product owner record
- target_id: naturalproductmech:mibig-bc0da8b0f6
  path: data/natural_products/carbohydrates/desosamine.yaml
  label: desosamine
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/carbohydrates/desosamine.yaml
    role: Generated natural product owner record
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Pinned LOTUS taxon-structure-reference occurrence assertions
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Source-pinned LOTUS occurrence exclusion table
- target_id: CHEBI:29630
  path: data/natural_products/polyketides/methymycin.yaml
  label: methymycin
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/methymycin.yaml
    role: Generated natural product owner record
- target_id: CHEBI:29665
  path: data/natural_products/polyketides/pikromycin.yaml
  label: pikromycin
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/pikromycin.yaml
    role: Generated natural product owner record
- target_id: CHEBI:29656
  path: data/natural_products/polyketides/neomethymycin.yaml
  label: neomethymycin
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/neomethymycin.yaml
    role: Generated natural product owner record
- target_id: CHEBI:29649
  path: data/natural_products/polyketides/narbomycin.yaml
  label: narbomycin
  kind: generated
  record_class: NaturalProductRecord
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/polyketides/narbomycin.yaml
    role: Generated natural product owner record
scope:
  description: Coherent 6-record biosynthetic and chemical-identity cohort covering
    all NaturalProductMech records seeded from MIBiG BGC0000094, BGC0000898, and BGC0000899,
    evaluated alongside frozen full-corpus inventory checks (3,116 owner YAML records
    and 246 standalone causal graph components; 3,362 total YAML records).
  selection: All records derived from the S. venezuelae pik/des gene clusters (BGC0000094:1,
    BGC0000898:1..4) and the homologous S. narbonensis des cluster (BGC0000899:1),
    selected to audit the Cycle 1 Stage 1 SPLIT_SHARED_WITH_CHEBI structure split
    and its cohort-wide producer, locus, and citation consistency.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  exclusions:
  - target: Remaining 3,110 natural product owner records and 246 standalone causal
      graph components in the frozen 3,362-file corpus inventory
    reason: Audited at the corpus-checkpoint level via verify_corpus.py, validate_id_label_correspondence.py,
      curation_worklist.py --review-records, and pytest tests/test_graph_components.py;
      excluded from this 6-record pik/des category cohort denominator to preserve
      per-target scientific review depth.
checks:
- check_id: inspect-cohort
  name: Native source inspection (cohort)
  status: passed
  required: true
  command: .venv/bin/python scripts/record_review.py inspect --targets /tmp/stage4_targets_cohort.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - cohort-owners
  summary: Captured exact Git base f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf and verified
    SHA256 digests for all 6 cohort target YAML files.
  scope_note: 2026-10-22T01:22:04.371418Z..2026-10-22T01:22:07.276393Z; output SHA256
    adcde9689f2c52f4c91445d1407ac6886ecb14dbc170e46ee2f7a0d43fb7e9fd
- check_id: strict-cohort
  name: Strict schema and semantic validation (cohort)
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --workers 1 --out /tmp/strict_cohort.tsv
    data/natural_products/carbohydrates/desosamine-2.yaml data/natural_products/carbohydrates/desosamine.yaml
    data/natural_products/polyketides/methymycin.yaml data/natural_products/polyketides/pikromycin.yaml
    data/natural_products/polyketides/neomethymycin.yaml data/natural_products/polyketides/narbomycin.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - cohort-owners
  summary: All 6 cohort YAML files passed strict LinkML validation with 0 ERROR rows.
  scope_note: 2026-10-22T01:17:46.004235Z..2026-10-22T01:17:50.285016Z; output SHA256
    dfc2c19d17b3a607f326a6094a754bd80c103487f7676f8acb78d3edccf66785
- check_id: verify-corpus
  name: Full-corpus lockfile and filing verification
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py --summary
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - corpus-worklist
  summary: Verified lockfile integrity across all 3,116 natural product owner records
    against data/natural_products/PATHS.tsv.
  scope_note: 2026-10-22T01:12:31.470813Z..2026-10-22T01:14:13.653446Z; output SHA256
    c9bcf7add9c5022125581df2e6b486735cd23803e49b73a4a2d6a60b62eebc5e
- check_id: validate-id-labels
  name: Full-corpus ontology ID-label correspondence
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/id_label_correspondence.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - chebi-structures
  - mibig-inventory
  summary: Full-corpus ID-label check passed (13,449 canonical, 646 synonym, 35 exception,
    0 ID_NOT_FOUND); all ChEBI and NCBITaxon terms on the 6 cohort records resolve
    canonically.
  scope_note: 2026-10-22T01:18:32.625871Z..2026-10-22T01:20:33.968758Z; output SHA256
    c859dad0c7a6023dd517b77fdcb98bb923c85cef6d72bd3ccf600babbb9bc41e
- check_id: review-queue
  name: Exhaustive corpus review-queue checkpoint
  status: passed
  required: true
  command: .venv/bin/python scripts/curation_worklist.py --review-records --limit
    5
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - corpus-worklist
  summary: 'Computed exhaustive review-records queue across all 3,116 corpus owners
    (8,905 worklist items across 11 queues, 8,928 output lines with --limit 5: producer-evidence
    2,292; biosynthesis 1,192; structure-disagreement 5; name-disagreement 67; unnamed-producer
    39; shared-structure 207; needs-a-name 18; occurrence-only 12; pathway-ambiguous
    620; unresolved-taxa 3,329; stereo-incomplete 1,124); all 6 cohort records appear
    in producer-evidence (1 SOURCE_ASSERTION producer each) and desosamine.yaml additionally
    appears in stereo-incomplete.'
  scope_note: 2026-10-22T01:15:57.039000Z..2026-10-22T01:16:45.056753Z; output SHA256
    21ceb24b744ee53c05d07dc655d00221db28f301469a9ded2cf9c3947a13da95
- check_id: local-search
  name: Repository-wide identifier and BGC cross-reference search
  status: passed
  required: true
  command: git grep -l -E BGC0000094|BGC0000898|BGC0000899|CHEBI:32540|CHEBI:29630|CHEBI:29665|CHEBI:29656|CHEBI:29649|naturalproductmech:mibig-bc0da8b0f6
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - cohort-owners
  - structure-corrections
  summary: Verified all repository references to BGC0000094, BGC0000898, BGC0000899,
    and cohort identifiers across raw inventories, curation tables, records, and tests.
  scope_note: 2026-10-22T01:21:20.376870Z..2026-10-22T01:21:24.691383Z; output SHA256
    18f7171fac0c9a66d492f459da59ed6abab6ea14eedfca2faaad1d7832d77cb4
- check_id: test-graph-components
  name: Full-corpus standalone causal graph component validation
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_graph_components.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - corpus-worklist
  summary: Validated all 246 standalone causal graph component YAML files under data/causal_graphs/
    (40 passed, 0 failed).
  scope_note: 2026-10-22T01:58:42.242233Z..2026-10-22T01:59:44.949915Z; output SHA256
    1addc70b9c898aa0b26f903283dd652e3403a6e0f111121e094a1d46a7c31656
evidence:
- evidence_id: cohort-owners
  kind: record_content
  reference: data/natural_products/PATHS.tsv
  locator: desosamine-2.yaml, desosamine.yaml, methymycin.yaml, pikromycin.yaml, neomethymycin.yaml,
    narbomycin.yaml at f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf
  accessed_at: '2026-10-22T01:22:07.276393Z'
  support: supports
  snapshot_sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
  summary: All 6 cohort YAML files are present at their locked PATHS.tsv locations
    with distinct Standard InChIKeys, valid LinkML structure, and SEEDED curation
    status.
- evidence_id: mibig-inventory
  kind: database
  reference: data/raw/mibig_compounds.tsv
  locator: BGC0000094:1 (sha256 4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5),
    BGC0000898:1..4 (sha256s 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae,
    224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923, 002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead,
    1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578), BGC0000899:1
    (sha256 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922)
  accessed_at: '2026-10-22T01:13:23.000000Z'
  support: partial
  snapshot_sha256: e26edc58f14ca9391f830d8027f562e6100b06413402da9014223560cb95dba6
  summary: MIBiG 4.0 exports species-level NCBITaxon:54571 (S. venezuelae) on BGC0000094:1
    (AF079138.1) and BGC0000898:1..4 (AF079762.1) and NCBITaxon:67333 (S. narbonensis)
    on BGC0000899:1 (AF521878.1), all citing entry-level PMID:9770448.
- evidence_id: chebi-structures
  kind: database
  reference: data/raw/chebi_structures.tsv
  locator: CHEBI:32540 (VTJCSBJRQLZNHE-CSMHCCOUSA-N), CHEBI:29630 (HUKYPYXOBINMND-HYUJHOPRSA-N),
    CHEBI:29665 (UZQBOFAUUTZOQE-VSLWXVDYSA-N), CHEBI:29656 (UEIVQYHYALXCBD-OTUJEKPESA-N),
    CHEBI:29649 (OXFYAOOMMKGGAI-JLTOUBQASA-N)
  accessed_at: '2026-10-22T01:13:23.000000Z'
  support: supports
  snapshot_sha256: 62b457dbdde9332087cc9c2262772f4246ae74ee66afab96761ba926208120a2
  summary: All five S. venezuelae cohort members ground to 3-star stereochemically
    complete ChEBI structures; CHEBI:32540 encodes open-chain D-desosamine aldehyde
    while BGC0000899:1 encodes flat cyclic hexopyranose ZOYWWAGVGBSJDL-UHFFFAOYSA-N
    absent from 3-star ChEBI.
- evidence_id: structure-corrections
  kind: record_content
  reference: curation/mibig_structure_corrections.tsv
  locator: BGC0000898:1 -> CHEBI:32540 (SPLIT_SHARED_WITH_CHEBI)
  accessed_at: '2026-10-22T01:21:24.691383Z'
  support: supports
  snapshot_sha256: c48f7467343ec2679f404d2fbd8b178e5f62afc7545b785ecb75f99d8617f4f0
  summary: SPLIT_SHARED_WITH_CHEBI cleanly routes BGC0000898:1 (desosamine) away from
    the erroneous methymycin SMILES onto CHEBI:32540 and strips the upstream methymycin
    xrefs pubchem:5282034|npatlas:NPA01238.
- evidence_id: pnas-1998
  kind: primary_source
  reference: DOI:10.1073/pnas.95.21.12111
  locator: Xue et al., Proc. Natl. Acad. Sci. U.S.A. 1998;95(21):12111-12116 (PMID:9770448);
    title, abstract, and GenBank AF079138.1 / AF079762.1 strain attribution
  accessed_at: '2026-10-22T01:12:00.000000Z'
  support: supports
  summary: Xue et al. (1998) explicitly characterize the pikromycin/methymycin/narbomycin/neomethymycin
    PKS (pikAI-pikAV), desosamine biosynthesis (desI-desVIII), and P450 hydroxylase
    (pikC) gene cluster in Streptomyces venezuelae ATCC 15439, and do not study Streptomyces
    narbonensis AF521878.1.
- evidence_id: genbank-af521878
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/nuccore/AF521878.1
  locator: GenBank AF521878.1 and MIBiG BGC0000899.4 entry metadata for Streptomyces
    narbonensis desosamine biosynthetic gene cluster
  accessed_at: '2026-10-22T01:12:00.000000Z'
  support: partial
  summary: AF521878.1 is a partial desosamine BGC sequence deposit from Streptomyces
    narbonensis (NCBITaxon:67333); MIBiG BGC0000899.4 attaches PMID:9770448 (which
    studies S. venezuelae ATCC 15439) at the entry level.
- evidence_id: corpus-worklist
  kind: validation
  reference: scripts/curation_worklist.py
  locator: 'Full-corpus checkpoint: 3,116 natural product owners (273 with inline
    causal_graphs, 27 with causal_graph_refs) and 246 standalone causal graph components
    (3,362 total YAML records) at f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf'
  accessed_at: '2026-10-22T01:16:45.056753Z'
  support: supports
  snapshot_sha256: 913508ca8df2eb5c037cd9e4769b14b027869ab78c7306f33b59e1c7e383a1c3
  summary: Deterministic worklist, lockfile, and graph-component checks confirm 3,116
    valid owner records and 246 standalone causal graph components (8,905 worklist
    items across 11 queues), with all 6 pik/des cohort members in SEEDED status and
    queued under producer-evidence.
- evidence_id: lotus-inventory
  kind: database
  reference: data/raw/lotus_occurrences.tsv
  locator: ZOYWWAGVGBSJDL-UHFFFAOYSA-N | NCBITaxon:67333 | 10.1073/PNAS.95.21.12111
    (expected_source_row_sha256 c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e)
  accessed_at: '2026-10-22T01:13:23.000000Z'
  support: partial
  snapshot_sha256: ee636011f7ed59c5c90afe6a039c32d049e5bc1c4421390bf47d941f19709e94
  summary: LOTUS exports an occurrence row linking ZOYWWAGVGBSJDL-UHFFFAOYSA-N to
    NCBITaxon:67333 (Streptomyces narbonensis) via DOI 10.1073/PNAS.95.21.12111 (Xue
    et al., 1998, PMID:9770448), propagating the same cross-species S. venezuelae
    ATCC 15439 reference onto occurrences[0] in desosamine.yaml.
assessments:
- assessment_id: cohort-identity
  area: identity
  topic: Chemical structure identity and SPLIT_SHARED_WITH_CHEBI separation across
    the 6-record cohort
  outcome: supported
  summary: Each of the four macrolide antibiotics (methymycin CHEBI:29630, pikromycin
    CHEBI:29665, neomethymycin CHEBI:29656, narbomycin CHEBI:29649) and the two desosamine
    records (open-chain D-desosamine CHEBI:32540 and cyclic flat-ring desosamine naturalproductmech:mibig-bc0da8b0f6)
    carries a distinct Standard InChIKey verified against ChEBI 3-star structures
    and MIBiG 4.0 rows. BGC0000898:1 is cleanly separated from methymycin.yaml onto
    desosamine-2.yaml with upstream methymycin xrefs stripped.
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - chebi-structures
  - structure-corrections
- assessment_id: venezuelae-producer-strain
  area: completeness
  topic: Missing ATCC 15439 producer strain qualification on S. venezuelae BGC0000094
    and BGC0000898 records
  outcome: concern
  summary: All five Streptomyces venezuelae records (desosamine-2.yaml, methymycin.yaml,
    pikromycin.yaml, neomethymycin.yaml, narbomycin.yaml) cite PMID:9770448 (DOI:10.1073/pnas.95.21.12111)
    and GenBank AF079138.1 / AF079762.1, which explicitly name strain ATCC 15439,
    but producer_organisms[0].strain is currently omitted because BGC0000094:1 and
    BGC0000898:1..4 are absent from curation/mibig_producer_strains.tsv.
  target_ids:
  - CHEBI:32540
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - pnas-1998
- assessment_id: narbonensis-citation-routing
  area: provenance
  topic: Cross-species Xue et al. 1998 citation (PMID:9770448 / DOI:10.1073/PNAS.95.21.12111)
    on S. narbonensis BGC0000899:1 and LOTUS occurrence (desosamine.yaml)
  outcome: concern
  summary: desosamine.yaml (naturalproductmech:mibig-bc0da8b0f6) asserts producer
    Streptomyces narbonensis (NCBITaxon:67333) and locus genbank:AF521878.1 via MIBiG
    BGC0000899:1 entry citation PMID:9770448, and simultaneously asserts a LOTUS occurrence
    for NCBITaxon:67333 citing DOI:10.1073/PNAS.95.21.12111 (the DOI of PMID:9770448).
    Because Xue et al. (1998) exclusively study Streptomyces venezuelae ATCC 15439,
    BGC0000899:1 claim references should be routed to BGC0000899.4 and GenBank AF521878.1
    via curation/mibig_claim_references.tsv, and the mis-referenced LOTUS row should
    be excluded via curation/lotus_occurrence_exclusions.tsv.
  target_ids:
  - naturalproductmech:mibig-bc0da8b0f6
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - pnas-1998
  - genbank-af521878
  - lotus-inventory
- assessment_id: desosamine-tautomer-stereo-split
  area: representation
  topic: Tautomeric/stereochemical separation of desosamine.yaml vs desosamine-2.yaml
    and BGC0000898 deposit split
  outcome: concern
  summary: desosamine.yaml (ZOYWWAGVGBSJDL-UHFFFAOYSA-N, flat cyclic hexopyranose,
    stereo_complete=false) and desosamine-2.yaml (VTJCSBJRQLZNHE-CSMHCCOUSA-N, 3-star
    ChEBI open-chain D-desosamine aldehyde, stereo_complete=true) remain separate
    records because ChEBI lacks a 3-star stereochemically complete cyclic D-desosamine
    entry and MIBiG BGC0000899:1 lacks stereochemical assignment. Additionally, MIBiG
    splits the S. venezuelae ATCC 15439 locus across BGC0000094 (AF079138.1, CLUSTER_DEMONSTRATED)
    and BGC0000898 (AF079762.1, CLUSTER_UNSTATED without coordinates).
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - mibig-inventory
  - chebi-structures
  - pnas-1998
  - genbank-af521878
- assessment_id: classification-and-filing
  area: consistency
  topic: NPClassifier pathway filing, lockfile stability, and ontology label alignment
  outcome: supported
  summary: Both desosamine records file under CARBOHYDRATES and all four macrolides
    file under POLYKETIDES in agreement with data/raw/npclassifier.tsv and data/natural_products/PATHS.tsv;
    all ontology labels pass validate_id_label_correspondence.py.
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - cohort-owners
  - chebi-structures
  - corpus-worklist
findings:
- finding_id: F-PIK-DES-001
  issue_key: pik-des-atcc15439-producer-strain-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Missing ATCC 15439 producer strain qualification on five S. venezuelae pik/des
    records
  description: The five Streptomyces venezuelae (NCBITaxon:54571) records seeded from
    MIBiG compound rows BGC0000094:1 (methymycin.yaml, sha256 4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5),
    BGC0000898:1 (desosamine-2.yaml, sha256 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae),
    BGC0000898:2 (pikromycin.yaml, sha256 224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923),
    BGC0000898:3 (neomethymycin.yaml, sha256 002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead),
    and BGC0000898:4 (narbomycin.yaml, sha256 1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578)
    omit producer_organisms[0].strain even though their primary reference Xue et al.,
    PNAS 1998 (PMID:9770448, DOI:10.1073/pnas.95.21.12111) and GenBank deposits AF079138.1
    and AF079762.1 explicitly identify the producer strain as Streptomyces venezuelae
    ATCC 15439. Add source-pinned ATCC 15439 qualifications for source_id keys BGC0000094:1,
    BGC0000898:1, BGC0000898:2, BGC0000898:3, and BGC0000898:4 in curation/mibig_producer_strains.tsv.
  target_ids:
  - CHEBI:32540
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  field_paths:
  - producer_organisms[0].strain
  - producer_organisms[0].evidence
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - pnas-1998
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  rule_id: review-checklist:producer-strain-qualification
  native_severity: major
  normalization_reason: Omission of an explicitly published producer strain across
    five linked BGC records is a material completeness gap resolvable via curation/mibig_producer_strains.tsv.
- finding_id: F-PIK-DES-002
  issue_key: bgc0000899-narbonensis-cross-species-pmid9770448-citation
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Cross-species Xue et al. 1998 citation (PMID:9770448 / DOI:10.1073/PNAS.95.21.12111)
    attached to S. narbonensis BGC0000899:1 and LOTUS occurrence in desosamine.yaml
  description: 'data/natural_products/carbohydrates/desosamine.yaml (naturalproductmech:mibig-bc0da8b0f6)
    carries cross-species citations to Xue et al., PNAS 1998 (PMID:9770448 / DOI:10.1073/PNAS.95.21.12111)
    on three claims for Streptomyces narbonensis (NCBITaxon:67333): (1) producer_organisms[0].evidence[0].reference
    and (2) biosynthetic_gene_clusters[0].evidence[0].reference (seeded from MIBiG
    BGC0000899:1, sha256 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922,
    with notes "MIBiG BGC0000899 entry version 4; citation taken from the entry level"
    on genome_accession genbank:AF521878.1), and (3) occurrences[0].evidence[0].reference
    (seeded from LOTUS row ZOYWWAGVGBSJDL-UHFFFAOYSA-N | NCBITaxon:67333 | 10.1073/PNAS.95.21.12111,
    expected_source_row_sha256 c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e).
    Because Xue et al. (1998) exclusively characterize Streptomyces venezuelae ATCC
    15439 (AF079138.1 / AF079762.1) and never report S. narbonensis or AF521878.1
    (deposited in 2002), Stage 5 must both route BGC0000899:1 in curation/mibig_claim_references.tsv
    and exclude the mis-referenced LOTUS row in curation/lotus_occurrence_exclusions.tsv.'
  target_ids:
  - naturalproductmech:mibig-bc0da8b0f6
  field_paths:
  - producer_organisms[0].evidence[0].reference
  - biosynthetic_gene_clusters[0].evidence[0].reference
  - occurrences[0].evidence[0].reference
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - pnas-1998
  - genbank-af521878
  - lotus-inventory
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Pinned LOTUS taxon-structure-reference occurrence assertions
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Source-pinned LOTUS occurrence exclusion table
  rule_id: review-checklist:claim-specific-citation-routing
  native_severity: major
  normalization_reason: Cross-species primary reference misattribution between S.
    venezuelae and S. narbonensis misstates claim provenance and is directly correctable
    via curation/mibig_claim_references.tsv.
- finding_id: F-PIK-DES-003
  issue_key: desosamine-cyclic-open-chain-and-bgc0000898-locus-split
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Upstream tautomeric/stereochemical separation of desosamine records and BGC0000898/BGC0000094
    deposit split
  description: 'Two upstream source-representation boundaries affect this cohort:
    (1) desosamine.yaml (naturalproductmech:mibig-bc0da8b0f6, BGC0000899:1) encodes
    flat cyclic hexopyranose ZOYWWAGVGBSJDL-UHFFFAOYSA-N (stereo_complete=false) whereas
    desosamine-2.yaml (CHEBI:32540, BGC0000898:1) encodes 3-star ChEBI open-chain
    D-desosamine aldehyde VTJCSBJRQLZNHE-CSMHCCOUSA-N (stereo_complete=true), and
    ChEBI lacks a 3-star stereochemically complete cyclic D-desosamine entry; (2)
    MIBiG 4.0 splits the S. venezuelae ATCC 15439 pik/des cluster across BGC0000094
    (AF079138.1, CLUSTER_DEMONSTRATED) and BGC0000898 (AF079762.1, CLUSTER_UNSTATED
    with blank locus coordinates and methods). Merging the two desosamine records
    or upgrading BGC0000898 locus grades without deposit-level sequence alignment
    and a curated cyclic D-desosamine ChEBI target would violate exact-structure and
    deposit-scoped grading rules.'
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  field_paths:
  - chemical_structure.standard_inchi_key
  - chemical_structure.smiles
  - biosynthetic_gene_clusters[0].link_evidence_basis
  - biosynthetic_gene_clusters[0].locus_evidence_methods
  evidence_ids:
  - mibig-inventory
  - chebi-structures
  - pnas-1998
  - genbank-af521878
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  rule_id: review-checklist:exact-structure-and-deposit-boundary
  native_severity: minor
  normalization_reason: Faithful reflection of upstream ChEBI open-chain vs MIBiG
    flat-ring representation and separate GenBank deposits AF079138.1/AF079762.1;
    documented as a source-limited boundary rather than an immediate data error.
actions:
- action_id: qualify-atcc15439-producer-strain
  description: Add source-pinned ATCC 15439 strain qualification rows for compound-row
    keys BGC0000094:1 (4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5),
    BGC0000898:1 (1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae),
    BGC0000898:2 (224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923),
    BGC0000898:3 (002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead),
    and BGC0000898:4 (1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578)
    citing DOI:10.1073/pnas.95.21.12111 to curation/mibig_producer_strains.tsv and
    re-seed the five S. venezuelae records via scripts/seed_from_sources.py.
  finding_ids:
  - F-PIK-DES-001
  target_ids:
  - CHEBI:32540
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Verify exact_source_row_sha256 pins for BGC0000094:1 and BGC0000898:1..4 in curation/mibig_producer_strains.tsv.
  - Run scripts/seed_from_sources.py and confirm producer_organisms[0].strain == ATCC
    15439 on methymycin.yaml, desosamine-2.yaml, pikromycin.yaml, neomethymycin.yaml,
    and narbomycin.yaml.
  - Verify zero regressions across scripts/validate_strict.py and scripts/verify_corpus.py.
- action_id: route-bgc0000899-claim-references
  description: Add a source-pinned claim-reference override for source_id BGC0000899:1
    (expected_source_row_sha256 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922)
    in curation/mibig_claim_references.tsv routing producer_reference to https://mibig.secondarymetabolites.org/repository/BGC0000899.4/
    and locus_reference/source_reference to https://www.ncbi.nlm.nih.gov/nuccore/AF521878.1,
    add a source-pinned LOTUS occurrence exclusion row (ZOYWWAGVGBSJDL-UHFFFAOYSA-N,
    NCBITaxon:67333, 10.1073/PNAS.95.21.12111, expected_source_row_sha256 c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e)
    in curation/lotus_occurrence_exclusions.tsv, and re-seed desosamine.yaml.
  finding_ids:
  - F-PIK-DES-002
  target_ids:
  - naturalproductmech:mibig-bc0da8b0f6
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/lotus_occurrences.tsv
    role: Pinned LOTUS taxon-structure-reference occurrence assertions
  - repository: CultureBotAI/NaturalProductMech
    path: curation/lotus_occurrence_exclusions.tsv
    role: Source-pinned LOTUS occurrence exclusion table
  generator: scripts/seed_from_sources.py
  acceptance_checks:
  - Verify expected_source_row_sha256 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922
    for BGC0000899:1 in curation/mibig_claim_references.tsv.
  - Verify expected_source_row_sha256 c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e
    for (ZOYWWAGVGBSJDL-UHFFFAOYSA-N, NCBITaxon:67333, 10.1073/PNAS.95.21.12111) in
    curation/lotus_occurrence_exclusions.tsv.
  - Re-seed desosamine.yaml via scripts/seed_from_sources.py and confirm producer
    and locus claims cite BGC0000899.4 and AF521878.1 with CURATOR_INFERENCE routing
    provenance and that the cross-species LOTUS occurrence is excluded.
  - Verify scripts/validate_strict.py and scripts/verify_corpus.py pass with zero
    errors.
- action_id: preserve-desosamine-tautomer-and-deposit-separation
  description: Retain separate records for CHEBI:32540 (desosamine-2.yaml, open-chain
    D-desosamine aldehyde) and naturalproductmech:mibig-bc0da8b0f6 (desosamine.yaml,
    stereo-incomplete cyclic desosamine) and retain deposit-scoped BGC0000898 grading
    until upstream ChEBI cyclic D-desosamine grounding and AF079762.1/AF079138.1 coordinate
    alignment are available.
  finding_ids:
  - F-PIK-DES-003
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  owner_paths:
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/mibig_compounds.tsv
    role: Pinned MIBiG 4.0 compound, producer, and locus assertions
  - repository: CultureBotAI/NaturalProductMech
    path: data/raw/chebi_structures.tsv
    role: Pinned 3-star ChEBI chemical structure and CURIE grounding
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_structure_corrections.tsv
    role: Source-pinned MIBiG structure correction and SPLIT_SHARED_WITH_CHEBI routing
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_producer_strains.tsv
    role: Source-pinned producer strain qualification table
  - repository: CultureBotAI/NaturalProductMech
    path: curation/mibig_claim_references.tsv
    role: Source-pinned producer and locus claim reference routing table
  - repository: CultureBotAI/NaturalProductMech
    path: scripts/seed_from_sources.py
    role: Deterministic corpus seeder and harmonization writer
  - repository: CultureBotAI/NaturalProductMech
    path: data/natural_products/PATHS.tsv
    role: Locked identifier-to-path filing table
  acceptance_checks:
  - Do not merge different InChIKeys (VTJCSBJRQLZNHE-CSMHCCOUSA-N vs ZOYWWAGVGBSJDL-UHFFFAOYSA-N)
    without a 3-star stereochemically complete ChEBI target.
  - Do not transfer AF079138.1 locus_evidence_methods onto AF079762.1 without verified
    sequence-coordinate equivalence.
boundary_decisions:
- action: retain
  target_ids:
  - CHEBI:32540
  - naturalproductmech:mibig-bc0da8b0f6
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  rationale: 'All six cohort records represent distinct committed Standard InChIKeys:
    four macrolide antibiotics (CHEBI:29630 methymycin, CHEBI:29665 pikromycin, CHEBI:29656
    neomethymycin, CHEBI:29649 narbomycin) and two desosamine representations (CHEBI:32540
    stereochemically complete open-chain D-desosamine aldehyde from S. venezuelae
    BGC0000898:1 vs naturalproductmech:mibig-bc0da8b0f6 stereo-incomplete flat cyclic
    hexopyranose from S. narbonensis BGC0000899:1). BGC0000898:1 is already properly
    split from methymycin.yaml via SPLIT_SHARED_WITH_CHEBI.'
  evidence_ids:
  - cohort-owners
  - mibig-inventory
  - chebi-structures
  - structure-corrections
limitations:
- Stage 4 is strictly read-only with respect to scientific YAML records and curation
  TSVs; all proposed curation edits are preserved as open findings for Stage 5 grouped
  remediation.
- Full-corpus deterministic checks (verify_corpus.py, validate_id_label_correspondence.py,
  curation_worklist.py --review-records, pytest tests/test_graph_components.py) audited
  all 3,116 owners and 246 standalone causal graph components (3,362 total YAML records),
  while claim-by-claim primary literature verification in this bundle was scoped to
  the 6-record pik/des cohort.
- GenBank AF521878.1 (BGC0000899) is a direct sequence submission without a dedicated
  primary experimental publication in the committed inventory.
```
