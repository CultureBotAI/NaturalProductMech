# Post-remediation verification review of the pik/des macrolide-deoxysugar cohort (Stage 5)

- Review: 20261022T034800Z-pik-des-stage5-remediation-review
- Repository: CultureBotAI/NaturalProductMech
- Started UTC: 2026-10-22T03:35:00.000000Z
- Finished UTC: 2026-10-22T03:48:00.000000Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Fresh post-remediation category review of the 6-record pikromycin/methymycin/desosamine (pik/des) cohort (CHEBI:32540 desosamine-2.yaml, naturalproductmech:mibig-bc0da8b0f6 desosamine.yaml, CHEBI:29630 methymycin.yaml, CHEBI:29665 pikromycin.yaml, CHEBI:29656 neomethymycin.yaml, CHEBI:29649 narbomycin.yaml). Confirms that (1) F-PIK-DES-001 / F-DES2-001 (#1010) is resolved: all five Streptomyces venezuelae compound rows (BGC0000094:1, BGC0000898:1..4) now carry producer_organisms[0].strain == ATCC 15439 with source-pinned CURATOR_INFERENCE provenance from curation/mibig_producer_strains.tsv while preserving SOURCE_ASSERTION and SEEDED status; (2) F-PIK-DES-002 (#1011) is resolved: Streptomyces narbonensis BGC0000899:1 producer and locus citations in desosamine.yaml are routed to BGC0000899.4 and GenBank AF521878.1 via curation/mibig_claim_references.tsv, and the cross-species LOTUS occurrence citing DOI:10.1073/PNAS.95.21.12111 is excluded via curation/lotus_occurrence_exclusions.tsv with a RESOLVED source-lotus-exclusion discussion; and (3) F-PIK-DES-003 / F-DES2-002 (#1012) remains documented and deferred until a 3-star stereochemically complete cyclic D-desosamine ChEBI entry and deposit-level AF079762.1/AF079138.1 sequence alignment are available.

## Scope And Provenance

Coherent 6-record biosynthetic and chemical-identity cohort covering all NaturalProductMech records seeded from MIBiG BGC0000094, BGC0000898, and BGC0000899, evaluated alongside frozen full-corpus inventory checks (3,116 owner YAML records and 246 standalone causal graph components; 3,362 total YAML records).

Selection: All records derived from the S. venezuelae pik/des gene clusters (BGC0000094:1, BGC0000898:1..4) and the homologous S. narbonensis des cluster (BGC0000899:1), selected to audit the Cycle 1 Stage 1 SPLIT_SHARED_WITH_CHEBI structure split and its cohort-wide producer, locus, and citation consistency.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base 71a28cf520dc96a7107b00d87703ba1e59acc02c.
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
| Strict schema and semantic validation (remediated cohort) | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | All 6 remediated cohort YAML files passed strict LinkML validation with 0 ERROR rows. |
| Full-corpus lockfile and filing verification | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | Verified lockfile integrity across all 3,116 natural product owner records against data/natural_products/PATHS.tsv. |
| Full-corpus ontology ID-label correspondence | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | Full-corpus ID-label check passed (13,448 canonical, 646 synonym, 35 exception, 0 ID_NOT_FOUND). |
| Curation table and deterministic seeding unit test suite | passed | True | CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649 | 322 passed in 26.37s covering producer strain qualification on structure-corrected rows, BGC0000899 claim-reference routing, and LOTUS exact-triple occurrence exclusion. |

## Scientific And Domain Assessments

### Chemical structure identity and SPLIT_SHARED_WITH_CHEBI separation across the 6-record cohort

identity: supported. Targets: CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649.

Each of the four macrolide antibiotics (methymycin CHEBI:29630, pikromycin CHEBI:29665, neomethymycin CHEBI:29656, narbomycin CHEBI:29649) and the two desosamine records (open-chain D-desosamine CHEBI:32540 and cyclic flat-ring desosamine naturalproductmech:mibig-bc0da8b0f6) carries a distinct Standard InChIKey verified against ChEBI 3-star structures and MIBiG 4.0 rows. BGC0000898:1 is cleanly separated from methymycin.yaml onto desosamine-2.yaml with upstream methymycin xrefs stripped.

### ATCC 15439 producer strain qualification on S. venezuelae BGC0000094 and BGC0000898 records

completeness: supported. Targets: CHEBI:32540, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649.

Resolved (#1010): all five Streptomyces venezuelae cohort records (desosamine-2.yaml, methymycin.yaml, pikromycin.yaml, neomethymycin.yaml, narbomycin.yaml) now carry producer_organisms[0].strain == ATCC 15439 with source-pinned CURATOR_INFERENCE provenance from curation/mibig_producer_strains.tsv.

### Remediation of cross-species Xue et al. 1998 citation on S. narbonensis BGC0000899:1 and LOTUS occurrence (desosamine.yaml)

provenance: supported. Targets: naturalproductmech:mibig-bc0da8b0f6.

Resolved (#1011): desosamine.yaml (naturalproductmech:mibig-bc0da8b0f6) now routes producer_organisms[0] to https://mibig.secondarymetabolites.org/repository/BGC0000899.4/ and biosynthetic_gene_clusters[0] to https://www.ncbi.nlm.nih.gov/nuccore/AF521878.1 via curation/mibig_claim_references.tsv, and excludes the mis-referenced LOTUS occurrence via curation/lotus_occurrence_exclusions.tsv.

### Tautomeric/stereochemical separation of desosamine.yaml vs desosamine-2.yaml and BGC0000898 deposit split

representation: not_applicable. Targets: CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649.

Deferred (#1012): upstream tautomeric/stereochemical boundary between flat cyclic hexopyranose ZOYWWAGVGBSJDL-UHFFFAOYSA-N (desosamine.yaml) and 3-star ChEBI open-chain D-desosamine aldehyde VTJCSBJRQLZNHE-CSMHCCOUSA-N (desosamine-2.yaml), plus MIBiG BGC0000094/BGC0000898 deposit partitioning, are preserved without unverified cross-InChIKey merge or locus-grade transfer.

### NPClassifier pathway filing, lockfile stability, and ontology label alignment

consistency: supported. Targets: CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649.

Both desosamine records file under CARBOHYDRATES and all four macrolides file under POLYKETIDES in agreement with data/raw/npclassifier.tsv and data/natural_products/PATHS.tsv; all ontology labels pass validate_id_label_correspondence.py.

## Findings

### F-PIK-DES-001: Missing ATCC 15439 producer strain qualification on five S. venezuelae pik/des records

major / resolved / confirmed; issue key: pik-des-atcc15439-producer-strain-missing.

The five Streptomyces venezuelae (NCBITaxon:54571) records seeded from MIBiG compound rows BGC0000094:1 (methymycin.yaml, sha256 4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5), BGC0000898:1 (desosamine-2.yaml, sha256 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae), BGC0000898:2 (pikromycin.yaml, sha256 224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923), BGC0000898:3 (neomethymycin.yaml, sha256 002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead), and BGC0000898:4 (narbomycin.yaml, sha256 1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578) omit producer_organisms[0].strain even though their primary reference Xue et al., PNAS 1998 (PMID:9770448, DOI:10.1073/pnas.95.21.12111) and GenBank deposits AF079138.1 and AF079762.1 explicitly identify the producer strain as Streptomyces venezuelae ATCC 15439. Add source-pinned ATCC 15439 qualifications for source_id keys BGC0000094:1, BGC0000898:1, BGC0000898:2, BGC0000898:3, and BGC0000898:4 in curation/mibig_producer_strains.tsv.

Disposition: Resolved in Stage 5 (#1010) by adding source-pinned ATCC 15439 strain qualifications for BGC0000094:1 and BGC0000898:1..4 to curation/mibig_producer_strains.tsv, updating scripts/seed_from_sources.py to allow reviewed structure-corrected rows naming structure_source_id in rationale, and re-seeding desosamine-2.yaml, methymycin.yaml, pikromycin.yaml, neomethymycin.yaml, and narbomycin.yaml.

### F-PIK-DES-002: Cross-species Xue et al. 1998 citation (PMID:9770448 / DOI:10.1073/PNAS.95.21.12111) attached to S. narbonensis BGC0000899:1 and LOTUS occurrence in desosamine.yaml

major / resolved / confirmed; issue key: bgc0000899-narbonensis-cross-species-pmid9770448-citation.

data/natural_products/carbohydrates/desosamine.yaml (naturalproductmech:mibig-bc0da8b0f6) carries cross-species citations to Xue et al., PNAS 1998 (PMID:9770448 / DOI:10.1073/PNAS.95.21.12111) on three claims for Streptomyces narbonensis (NCBITaxon:67333): (1) producer_organisms[0].evidence[0].reference and (2) biosynthetic_gene_clusters[0].evidence[0].reference (seeded from MIBiG BGC0000899:1, sha256 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922, with notes "MIBiG BGC0000899 entry version 4; citation taken from the entry level" on genome_accession genbank:AF521878.1), and (3) occurrences[0].evidence[0].reference (seeded from LOTUS row ZOYWWAGVGBSJDL-UHFFFAOYSA-N &#124; NCBITaxon:67333 &#124; 10.1073/PNAS.95.21.12111, expected_source_row_sha256 c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e). Because Xue et al. (1998) exclusively characterize Streptomyces venezuelae ATCC 15439 (AF079138.1 / AF079762.1) and never report S. narbonensis or AF521878.1 (deposited in 2002), Stage 5 must both route BGC0000899:1 in curation/mibig_claim_references.tsv and exclude the mis-referenced LOTUS row in curation/lotus_occurrence_exclusions.tsv.

Disposition: Resolved in Stage 5 (#1011) by routing BGC0000899:1 producer and locus claims in curation/mibig_claim_references.tsv to BGC0000899.4 and GenBank AF521878.1, excluding the mis-referenced LOTUS occurrence (ZOYWWAGVGBSJDL-UHFFFAOYSA-N &#124; NCBITaxon:67333 &#124; 10.1073/PNAS.95.21.12111) in curation/lotus_occurrence_exclusions.tsv, and re-seeding desosamine.yaml.

### F-PIK-DES-003: Upstream tautomeric/stereochemical separation of desosamine records and BGC0000898/BGC0000094 deposit split

minor / deferred / confirmed; issue key: desosamine-cyclic-open-chain-and-bgc0000898-locus-split.

Two upstream source-representation boundaries affect this cohort: (1) desosamine.yaml (naturalproductmech:mibig-bc0da8b0f6, BGC0000899:1) encodes flat cyclic hexopyranose ZOYWWAGVGBSJDL-UHFFFAOYSA-N (stereo_complete=false) whereas desosamine-2.yaml (CHEBI:32540, BGC0000898:1) encodes 3-star ChEBI open-chain D-desosamine aldehyde VTJCSBJRQLZNHE-CSMHCCOUSA-N (stereo_complete=true), and ChEBI lacks a 3-star stereochemically complete cyclic D-desosamine entry; (2) MIBiG 4.0 splits the S. venezuelae ATCC 15439 pik/des cluster across BGC0000094 (AF079138.1, CLUSTER_DEMONSTRATED) and BGC0000898 (AF079762.1, CLUSTER_UNSTATED with blank locus coordinates and methods). Merging the two desosamine records or upgrading BGC0000898 locus grades without deposit-level sequence alignment and a curated cyclic D-desosamine ChEBI target would violate exact-structure and deposit-scoped grading rules.

Disposition: Deferred in Stage 5 (#1012) because 3-star ChEBI lacks a stereochemically complete cyclic D-desosamine entry and MIBiG BGC0000898 (AF079762.1) exports blank locus coordinates; merging distinct InChIKeys or transferring AF079138.1 locus grades without sequence-coordinate equivalence would violate corpus curation rules.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: CHEBI:32540, naturalproductmech:mibig-bc0da8b0f6, CHEBI:29630, CHEBI:29665, CHEBI:29656, CHEBI:29649. All six cohort records represent distinct committed Standard InChIKeys: four macrolide antibiotics (CHEBI:29630 methymycin, CHEBI:29665 pikromycin, CHEBI:29656 neomethymycin, CHEBI:29649 narbomycin) and two desosamine representations (CHEBI:32540 stereochemically complete open-chain D-desosamine aldehyde from S. venezuelae BGC0000898:1 vs naturalproductmech:mibig-bc0da8b0f6 stereo-incomplete flat cyclic hexopyranose from S. narbonensis BGC0000899:1). BGC0000898:1 is already properly split from methymycin.yaml via SPLIT_SHARED_WITH_CHEBI.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| cohort-owners | data/natural_products/PATHS.tsv; desosamine-2.yaml, desosamine.yaml, methymycin.yaml, pikromycin.yaml, neomethymycin.yaml, narbomycin.yaml (Stage 5 working tree) | supports | All 6 remediated cohort YAML files reproduce deterministically from scripts/seed_from_sources.py and pass strict validation. |
| producer-strains-table | curation/mibig_producer_strains.tsv; BGC0000094:1 and BGC0000898:1..4 -&gt; ATCC 15439 (DOI:10.1073/pnas.95.21.12111) | supports | Source-pinned ATCC 15439 strain qualifications for BGC0000094:1 and BGC0000898:1..4 populate producer_organisms[0].strain across all five S. venezuelae cohort records. |
| claim-references-table | curation/mibig_claim_references.tsv; BGC0000899:1 -&gt; BGC0000899.4 (producer) and GenBank AF521878.1 (locus) | supports | Routes BGC0000899:1 producer and locus claims away from cross-species S. venezuelae reference PMID:9770448 to BGC0000899.4 and GenBank AF521878.1. |
| lotus-exclusions-table | curation/lotus_occurrence_exclusions.tsv; ZOYWWAGVGBSJDL-UHFFFAOYSA-N &#124; NCBITaxon:67333 &#124; 10.1073/PNAS.95.21.12111 | supports | Excludes the mis-referenced LOTUS occurrence on desosamine.yaml and records a RESOLVED source-lotus-exclusion discussion. |
| mibig-inventory | data/raw/mibig_compounds.tsv; BGC0000094:1 (sha256 4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5), BGC0000898:1..4 (sha256s 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae, 224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923, 002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead, 1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578), BGC0000899:1 (sha256 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922) | partial | MIBiG 4.0 exports species-level NCBITaxon:54571 (S. venezuelae) on BGC0000094:1 (AF079138.1) and BGC0000898:1..4 (AF079762.1) and NCBITaxon:67333 (S. narbonensis) on BGC0000899:1 (AF521878.1), all citing entry-level PMID:9770448. |
| chebi-structures | data/raw/chebi_structures.tsv; CHEBI:32540 (VTJCSBJRQLZNHE-CSMHCCOUSA-N), CHEBI:29630 (HUKYPYXOBINMND-HYUJHOPRSA-N), CHEBI:29665 (UZQBOFAUUTZOQE-VSLWXVDYSA-N), CHEBI:29656 (UEIVQYHYALXCBD-OTUJEKPESA-N), CHEBI:29649 (OXFYAOOMMKGGAI-JLTOUBQASA-N) | supports | All five S. venezuelae cohort members ground to 3-star stereochemically complete ChEBI structures; CHEBI:32540 encodes open-chain D-desosamine aldehyde while BGC0000899:1 encodes flat cyclic hexopyranose ZOYWWAGVGBSJDL-UHFFFAOYSA-N absent from 3-star ChEBI. |
| structure-corrections | curation/mibig_structure_corrections.tsv; BGC0000898:1 -&gt; CHEBI:32540 (SPLIT_SHARED_WITH_CHEBI) | supports | SPLIT_SHARED_WITH_CHEBI cleanly routes BGC0000898:1 (desosamine) away from the erroneous methymycin SMILES onto CHEBI:32540 and strips the upstream methymycin xrefs pubchem:5282034&#124;npatlas:NPA01238. |
| pnas-1998 | DOI:10.1073/pnas.95.21.12111; Xue et al., Proc. Natl. Acad. Sci. U.S.A. 1998;95(21):12111-12116 (PMID:9770448); title, abstract, and GenBank AF079138.1 / AF079762.1 strain attribution | supports | Xue et al. (1998) explicitly characterize the pikromycin/methymycin/narbomycin/neomethymycin PKS (pikAI-pikAV), desosamine biosynthesis (desI-desVIII), and P450 hydroxylase (pikC) gene cluster in Streptomyces venezuelae ATCC 15439, and do not study Streptomyces narbonensis AF521878.1. |
| genbank-af521878 | https://www.ncbi.nlm.nih.gov/nuccore/AF521878.1; GenBank AF521878.1 and MIBiG BGC0000899.4 entry metadata for Streptomyces narbonensis desosamine biosynthetic gene cluster | partial | AF521878.1 is a partial desosamine BGC sequence deposit from Streptomyces narbonensis (NCBITaxon:67333); MIBiG BGC0000899.4 attaches PMID:9770448 (which studies S. venezuelae ATCC 15439) at the entry level. |
| corpus-worklist | scripts/curation_worklist.py; Full-corpus checkpoint: 3,116 natural product owners (273 with inline causal_graphs, 27 with causal_graph_refs) and 246 standalone causal graph components (3,362 total YAML records) at f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf | supports | Deterministic worklist, lockfile, and graph-component checks confirm 3,116 valid owner records and 246 standalone causal graph components (8,905 worklist items across 11 queues), with all 6 pik/des cohort members in SEEDED status and queued under producer-evidence. |

## Limits And Additional Notes

- F-PIK-DES-003 / F-DES2-002 (tracked in open GitHub issue #1012) remains deferred because 3-star ChEBI currently lacks a stereochemically complete cyclic D-desosamine entry and MIBiG BGC0000898 (AF079762.1) exports blank locus coordinates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T034800Z-pik-des-stage5-remediation-review
kind: category
repository: CultureBotAI/NaturalProductMech
title: Post-remediation verification review of the pik/des macrolide-deoxysugar cohort
  (Stage 5)
started_at: '2026-10-22T03:35:00.000000Z'
finished_at: '2026-10-22T03:48:00.000000Z'
reviewer:
  identity: Antigravity
  kind: agent
  independence: self_review
  independence_basis: Post-remediation Stage 5 verification review of the 6-record
    pik/des cohort after applying source-pinned producer strain, claim-reference routing,
    and LOTUS occurrence exclusion decisions.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: SEEDED retained across all 6 cohort records; F-PIK-DES-001 (#1010)
  and F-PIK-DES-002 (#1011) resolved via source-pinned curation tables; F-PIK-DES-003
  (#1012) deferred as upstream source-representation boundary
scientific_review: true
summary: 'Fresh post-remediation category review of the 6-record pikromycin/methymycin/desosamine
  (pik/des) cohort (CHEBI:32540 desosamine-2.yaml, naturalproductmech:mibig-bc0da8b0f6
  desosamine.yaml, CHEBI:29630 methymycin.yaml, CHEBI:29665 pikromycin.yaml, CHEBI:29656
  neomethymycin.yaml, CHEBI:29649 narbomycin.yaml). Confirms that (1) F-PIK-DES-001
  / F-DES2-001 (#1010) is resolved: all five Streptomyces venezuelae compound rows
  (BGC0000094:1, BGC0000898:1..4) now carry producer_organisms[0].strain == ATCC 15439
  with source-pinned CURATOR_INFERENCE provenance from curation/mibig_producer_strains.tsv
  while preserving SOURCE_ASSERTION and SEEDED status; (2) F-PIK-DES-002 (#1011) is
  resolved: Streptomyces narbonensis BGC0000899:1 producer and locus citations in
  desosamine.yaml are routed to BGC0000899.4 and GenBank AF521878.1 via curation/mibig_claim_references.tsv,
  and the cross-species LOTUS occurrence citing DOI:10.1073/PNAS.95.21.12111 is excluded
  via curation/lotus_occurrence_exclusions.tsv with a RESOLVED source-lotus-exclusion
  discussion; and (3) F-PIK-DES-003 / F-DES2-002 (#1012) remains documented and deferred
  until a 3-star stereochemically complete cyclic D-desosamine ChEBI entry and deposit-level
  AF079762.1/AF079138.1 sequence alignment are available.'
source:
  git_revision: 71a28cf520dc96a7107b00d87703ba1e59acc02c
  state: working_tree
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
    sha256: 6a9594c1159fc8038b59f8d421efd15dfb3d748e8e6d508b8f7fb84c43abe09b
    role: context
  - path: curation/mibig_locus_evidence_overrides.tsv
    sha256: 7f943dc205f3ae2d03570863f5d9a169bf1e7a0dce53b33f82d8ebff63b5930e
    role: context
  - path: curation/mibig_producer_isolates.tsv
    sha256: 8067b946129f61013351e4c0f99a76c1ec4f8b2fce572b984ab905c55c7a3cc8
    role: context
  - path: curation/mibig_producer_strains.tsv
    sha256: 8879da121435bf96833919d8300031745197ee78a527d602b233dcd1dde23268
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
    sha256: 9cd2d384e1cc47a944b746149784dac9ecc023fe8e3346228e95b8d02279a310
    role: target
  - path: data/natural_products/carbohydrates/desosamine.yaml
    sha256: 5a1738b564e635f7260a01956b3bbba354fdd2af96fa95b1c9245ee849689db3
    role: target
  - path: data/natural_products/polyketides/methymycin.yaml
    sha256: 279e24ae3369266a3326b168a2a96f76c8c2b211e5ad0fbe0614e87b8adf6ca4
    role: target
  - path: data/natural_products/polyketides/narbomycin.yaml
    sha256: 790f623f6404b18ab99d6381236d928f85408d28bc63ac1de21dae7e26735355
    role: target
  - path: data/natural_products/polyketides/neomethymycin.yaml
    sha256: 72460fdd53c0c0ee0bcfd0d9f5f212d1dc7198ef9b6eb0666e82d53af571b499
    role: target
  - path: data/natural_products/polyketides/pikromycin.yaml
    sha256: a5a6410fc09604ae039dc5f2c2fbc6e8fe47d1eef1c2eb5da237592bd0b9d804
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
    sha256: 8131041cc030009e847fe3730b4a8dbcc4a0b7d2b7bd19b82e19cd4e49b5434e
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
    sha256: b992853ea5e476fa27937bd6641ebe9b266f178215572e45d16ba597115e250d
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
- check_id: strict-cohort-post-remediation
  name: Strict schema and semantic validation (remediated cohort)
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py --workers 1 --out /tmp/stage5_strict.tsv
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
  - producer-strains-table
  - claim-references-table
  - lotus-exclusions-table
  summary: All 6 remediated cohort YAML files passed strict LinkML validation with
    0 ERROR rows.
  scope_note: 2026-10-22T03:42:32Z..2026-10-22T03:42:36Z; 6 files scanned, 0 errors
- check_id: verify-corpus-post-remediation
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
  - cohort-owners
  - corpus-worklist
  summary: Verified lockfile integrity across all 3,116 natural product owner records
    against data/natural_products/PATHS.tsv.
  scope_note: 2026-10-22T03:42:40Z..2026-10-22T03:44:15Z; 3,116 lockfile rows, 3,116
    files on disk
- check_id: validate-id-labels-post-remediation
  name: Full-corpus ontology ID-label correspondence
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/stage5_id_label.tsv
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
  summary: Full-corpus ID-label check passed (13,448 canonical, 646 synonym, 35 exception,
    0 ID_NOT_FOUND).
  scope_note: 2026-10-22T03:45:22Z..2026-10-22T03:47:23Z; 0 ID_NOT_FOUND across all
    3,116 records
- check_id: unit-tests-post-remediation
  name: Curation table and deterministic seeding unit test suite
  status: passed
  required: true
  command: .venv/bin/python -B -m pytest -o cache_dir=/tmp/pytest_cache -q tests/test_producer_strains.py
    tests/test_claim_references.py tests/test_lotus_exclusions.py tests/test_structure_corrections.py
    tests/test_seed_skeleton.py
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
  - producer-strains-table
  - claim-references-table
  - lotus-exclusions-table
  - structure-corrections
  summary: 322 passed in 26.37s covering producer strain qualification on structure-corrected
    rows, BGC0000899 claim-reference routing, and LOTUS exact-triple occurrence exclusion.
  scope_note: 2026-10-22T03:41:51Z..2026-10-22T03:42:25Z; 322 passed, 0 failed
evidence:
- evidence_id: cohort-owners
  kind: record_content
  reference: data/natural_products/PATHS.tsv
  locator: desosamine-2.yaml, desosamine.yaml, methymycin.yaml, pikromycin.yaml, neomethymycin.yaml,
    narbomycin.yaml (Stage 5 working tree)
  accessed_at: '2026-10-22T03:42:36.000000Z'
  support: supports
  snapshot_sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3
  summary: All 6 remediated cohort YAML files reproduce deterministically from scripts/seed_from_sources.py
    and pass strict validation.
- evidence_id: producer-strains-table
  kind: record_content
  reference: curation/mibig_producer_strains.tsv
  locator: BGC0000094:1 and BGC0000898:1..4 -> ATCC 15439 (DOI:10.1073/pnas.95.21.12111)
  accessed_at: '2026-10-22T03:42:36.000000Z'
  support: supports
  snapshot_sha256: 8879da121435bf96833919d8300031745197ee78a527d602b233dcd1dde23268
  summary: Source-pinned ATCC 15439 strain qualifications for BGC0000094:1 and BGC0000898:1..4
    populate producer_organisms[0].strain across all five S. venezuelae cohort records.
- evidence_id: claim-references-table
  kind: record_content
  reference: curation/mibig_claim_references.tsv
  locator: BGC0000899:1 -> BGC0000899.4 (producer) and GenBank AF521878.1 (locus)
  accessed_at: '2026-10-22T03:42:36.000000Z'
  support: supports
  snapshot_sha256: 6a9594c1159fc8038b59f8d421efd15dfb3d748e8e6d508b8f7fb84c43abe09b
  summary: Routes BGC0000899:1 producer and locus claims away from cross-species S.
    venezuelae reference PMID:9770448 to BGC0000899.4 and GenBank AF521878.1.
- evidence_id: lotus-exclusions-table
  kind: record_content
  reference: curation/lotus_occurrence_exclusions.tsv
  locator: ZOYWWAGVGBSJDL-UHFFFAOYSA-N | NCBITaxon:67333 | 10.1073/PNAS.95.21.12111
  accessed_at: '2026-10-22T03:42:36.000000Z'
  support: supports
  snapshot_sha256: d1778f304b83256e756a3aec99f4fd67b5a5d2aee3ca32f88dd0418592f8a30d
  summary: Excludes the mis-referenced LOTUS occurrence on desosamine.yaml and records
    a RESOLVED source-lotus-exclusion discussion.
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
  topic: ATCC 15439 producer strain qualification on S. venezuelae BGC0000094 and
    BGC0000898 records
  outcome: supported
  summary: 'Resolved (#1010): all five Streptomyces venezuelae cohort records (desosamine-2.yaml,
    methymycin.yaml, pikromycin.yaml, neomethymycin.yaml, narbomycin.yaml) now carry
    producer_organisms[0].strain == ATCC 15439 with source-pinned CURATOR_INFERENCE
    provenance from curation/mibig_producer_strains.tsv.'
  target_ids:
  - CHEBI:32540
  - CHEBI:29630
  - CHEBI:29665
  - CHEBI:29656
  - CHEBI:29649
  evidence_ids:
  - cohort-owners
  - producer-strains-table
  - mibig-inventory
  - pnas-1998
- assessment_id: narbonensis-citation-routing
  area: provenance
  topic: Remediation of cross-species Xue et al. 1998 citation on S. narbonensis BGC0000899:1
    and LOTUS occurrence (desosamine.yaml)
  outcome: supported
  summary: 'Resolved (#1011): desosamine.yaml (naturalproductmech:mibig-bc0da8b0f6)
    now routes producer_organisms[0] to https://mibig.secondarymetabolites.org/repository/BGC0000899.4/
    and biosynthetic_gene_clusters[0] to https://www.ncbi.nlm.nih.gov/nuccore/AF521878.1
    via curation/mibig_claim_references.tsv, and excludes the mis-referenced LOTUS
    occurrence via curation/lotus_occurrence_exclusions.tsv.'
  target_ids:
  - naturalproductmech:mibig-bc0da8b0f6
  evidence_ids:
  - cohort-owners
  - claim-references-table
  - lotus-exclusions-table
  - mibig-inventory
  - pnas-1998
  - genbank-af521878
- assessment_id: desosamine-tautomer-stereo-split
  area: representation
  topic: Tautomeric/stereochemical separation of desosamine.yaml vs desosamine-2.yaml
    and BGC0000898 deposit split
  outcome: not_applicable
  summary: 'Deferred (#1012): upstream tautomeric/stereochemical boundary between
    flat cyclic hexopyranose ZOYWWAGVGBSJDL-UHFFFAOYSA-N (desosamine.yaml) and 3-star
    ChEBI open-chain D-desosamine aldehyde VTJCSBJRQLZNHE-CSMHCCOUSA-N (desosamine-2.yaml),
    plus MIBiG BGC0000094/BGC0000898 deposit partitioning, are preserved without unverified
    cross-InChIKey merge or locus-grade transfer.'
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
  status: resolved
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
  - producer-strains-table
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
  disposition_reason: Resolved in Stage 5 (#1010) by adding source-pinned ATCC 15439
    strain qualifications for BGC0000094:1 and BGC0000898:1..4 to curation/mibig_producer_strains.tsv,
    updating scripts/seed_from_sources.py to allow reviewed structure-corrected rows
    naming structure_source_id in rationale, and re-seeding desosamine-2.yaml, methymycin.yaml,
    pikromycin.yaml, neomethymycin.yaml, and narbomycin.yaml.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261022T012300Z-pik-des-macrolide-deoxysugar-cohort
    finding_id: F-PIK-DES-001
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261022T012305Z-desosamine-2-record-review
    finding_id: F-DES2-001
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/1010
- finding_id: F-PIK-DES-002
  issue_key: bgc0000899-narbonensis-cross-species-pmid9770448-citation
  category: provenance
  severity: major
  status: resolved
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
  - claim-references-table
  - lotus-exclusions-table
  - mibig-inventory
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
  disposition_reason: Resolved in Stage 5 (#1011) by routing BGC0000899:1 producer
    and locus claims in curation/mibig_claim_references.tsv to BGC0000899.4 and GenBank
    AF521878.1, excluding the mis-referenced LOTUS occurrence (ZOYWWAGVGBSJDL-UHFFFAOYSA-N
    | NCBITaxon:67333 | 10.1073/PNAS.95.21.12111) in curation/lotus_occurrence_exclusions.tsv,
    and re-seeding desosamine.yaml.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261022T012300Z-pik-des-macrolide-deoxysugar-cohort
    finding_id: F-PIK-DES-002
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/1011
- finding_id: F-PIK-DES-003
  issue_key: desosamine-cyclic-open-chain-and-bgc0000898-locus-split
  category: representation
  severity: minor
  status: deferred
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
  disposition_reason: Deferred in Stage 5 (#1012) because 3-star ChEBI lacks a stereochemically
    complete cyclic D-desosamine entry and MIBiG BGC0000898 (AF079762.1) exports blank
    locus coordinates; merging distinct InChIKeys or transferring AF079138.1 locus
    grades without sequence-coordinate equivalence would violate corpus curation rules.
  previous_occurrences:
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261022T012300Z-pik-des-macrolide-deoxysugar-cohort
    finding_id: F-PIK-DES-003
  - repository: CultureBotAI/NaturalProductMech
    review_id: 20261022T012305Z-desosamine-2-record-review
    finding_id: F-DES2-002
  external_issues:
  - https://github.com/CultureBotAI/NaturalProductMech/issues/1012
actions: []
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
- 'F-PIK-DES-003 / F-DES2-002 (tracked in open GitHub issue #1012) remains deferred
  because 3-star ChEBI currently lacks a stereochemically complete cyclic D-desosamine
  entry and MIBiG BGC0000898 (AF079762.1) exports blank locus coordinates.'
related_reviews:
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261022T012300Z-pik-des-macrolide-deoxysugar-cohort
  relationship: supersedes_open_findings
- repository: CultureBotAI/NaturalProductMech
  review_id: 20261022T012305Z-desosamine-2-record-review
  relationship: supersedes_open_findings
```
