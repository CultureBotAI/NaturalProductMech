# Stage 5 Finding Group & GitHub Issue Map (`mech-goal-sequence-20261019`, Cycle 3)

## Consumed Stage 4 Review Artifacts

| Kind | Path | SHA-256 |
| --- | --- | --- |
| `category` | `reviews/structured/20261025T055000Z-streptomyces-youssoufiensis-youssoufene-cohort/review.yaml` | `f55bc505b5e614cc3732c6abbabb9216a33a3a8fe2310dfc1adfe5846681c120` |
| `record` | `reviews/structured/20261025T055005Z-youssoufene-a1-record-review/review.yaml` | `cd4bed0269fe80314aee0757ab8369985115cedc5607a1520babb6301a2a3cb7` |
| `workflow_manifest` | `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml` | `7c3fb4e21b068d6661b69dd78fb544174a9344b3c0b1ff7a8f22df0009710558` |

## Grouped Findings, Repair Ownership, and GitHub Issue Mapping

| Group ID | Finding IDs | Issue Key | Severity | Status | Repair Owner | GitHub Issue | Target IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `G-YSF-001` | `F-YSF-001`, `F-YSF-A1-001` | `streptomyces-youssoufiensis-bgc0002547-ouc6819-producer-strain-missing` | `major` | `resolved` | `curation/mibig_producer_strains.tsv` (+ `scripts/seed_from_sources.py`) | [#1044](https://github.com/CultureBotAI/NaturalProductMech/issues/1044) (`created`, closes with Stage 5 PR) | `naturalproductmech:mibig-78ea4c55fb`, `naturalproductmech:mibig-ccb60942af`, `naturalproductmech:mibig-cf5248036e`, `naturalproductmech:mibig-f827d9f550`, `naturalproductmech:mibig-18ba3c758c` |
| `G-YSF-002` | `F-YSF-002`, `F-YSF-A1-002` | `youssoufene-cohort-anie-202007777-author-attribution-mismatch` | `major` | `resolved` | `data/natural_products/polyketides/youssoufene-a1.yaml`, `data/natural_products/unclassified/youssoufene-b1.yaml`..`youssoufene-b4.yaml` (via `write_validated_natural_product` + `record_curation_event`) | [#1045](https://github.com/CultureBotAI/NaturalProductMech/issues/1045) (`created`, closes with Stage 5 PR) | `naturalproductmech:mibig-78ea4c55fb`, `naturalproductmech:mibig-ccb60942af`, `naturalproductmech:mibig-cf5248036e`, `naturalproductmech:mibig-f827d9f550`, `naturalproductmech:mibig-18ba3c758c` |
| `G-YSF-003` | `F-YSF-003`, `F-YSF-A1-003` | `youssoufene-cohort-npclassifier-ks-clf-and-bgc0002510-boundaries` | `minor` | `deferred` | `data/raw/npclassifier.tsv`, `data/natural_products/PATHS.tsv`, `data/raw/mibig_compounds.tsv` | [#1046](https://github.com/CultureBotAI/NaturalProductMech/issues/1046) (`created`, remains `open`) | `naturalproductmech:mibig-78ea4c55fb`, `naturalproductmech:mibig-ccb60942af`, `naturalproductmech:mibig-cf5248036e`, `naturalproductmech:mibig-f827d9f550`, `naturalproductmech:mibig-18ba3c758c` |
| `G-PEN-003` | `F-PEN-003` | `penicillin-cohort-salt-and-protonation-state-boundary` | `minor` | `deferred` | `curation/mibig_claim_references.tsv` (+ `src/naturalproductmech/curate/claim_references.py`, `scripts/seed_from_sources.py`; `naturalproductmech-infra-0003`) | [#1047](https://github.com/CultureBotAI/NaturalProductMech/issues/1047) (`created`, remains `open`; follows up on closed [#1015](https://github.com/CultureBotAI/NaturalProductMech/issues/1015)) | `CHEBI:58572`, `CHEBI:18165`, `CHEBI:51765` |
| `G-PIK-DES-003` | `F-PIK-DES-003` | `desosamine-cyclic-open-chain-and-bgc0000898-locus-split` | `minor` | `deferred` | `curation/mibig_structure_corrections.tsv` | [#1012](https://github.com/CultureBotAI/NaturalProductMech/issues/1012) (`reused`, remains `open`) | `CHEBI:32540`, `naturalproductmech:mibig-bc0da8b0f6`, `CHEBI:29630`, `CHEBI:29665`, `CHEBI:29656`, `CHEBI:29649` |

## Group Details

### `G-YSF-001` — Missing `OUC6819` (`BGC0002547:1..5`, `MN844187.1`) producer strain qualifications on *Streptomyces youssoufiensis* youssoufene records
- **Cause**: MIBiG 4.0 exports species-level `NCBITaxon:654447` (*Streptomyces youssoufiensis*) without strain metadata for `BGC0002547:1..5` (`MN844187.1:1..20186`), even though GenBank `MN844187.1`, Li et al., *Org. Lett.* 2020 (`PMID:31891272`, `DOI:10.1021/acs.orglett.9b04559`), Liu et al., *Angew. Chem. Int. Ed.* 2021 (`PMID:33155752`, `DOI:10.1002/anie.202007777`), and the records' own `biosynthetic_pathway` and `causal_graphs` notes and `protein_examples[0].strain` explicitly identify the sequenced producer strain as *Streptomyces youssoufiensis* `OUC6819`.
- **Remediation**:
  1. Added five source-pinned rows (`BGC0002547:1..5` -> `OUC6819`, `reference=PMID:31891272`) to `curation/mibig_producer_strains.tsv`.
  2. Added unit and regression tests in `tests/test_producer_strains.py`.
  3. Re-ran `scripts/seed_from_sources.py` to regenerate `youssoufene-a1.yaml` (`naturalproductmech:mibig-78ea4c55fb`) and `youssoufene-b1.yaml`..`youssoufene-b4.yaml` (`naturalproductmech:mibig-ccb60942af`, `naturalproductmech:mibig-cf5248036e`, `naturalproductmech:mibig-f827d9f550`, `naturalproductmech:mibig-18ba3c758c`).

### `G-YSF-002` — Misattributed author citation (`Deng et al.` instead of `Liu et al.`) on `DOI:10.1002/anie.202007777` evidence notes across all five youssoufene records
- **Cause**: Across all five youssoufene records, all 16 `PRIMARY_EXPERIMENT` evidence notes per record (80 total across `biosynthetic_pathway[0..3].evidence[0].notes` and `causal_graphs[0].edges[0..11].evidence[0].notes`) citing `DOI:10.1002/anie.202007777` (*Angew. Chem. Int. Ed.* 2021;60(1):153-158, `PMID:33155752`) attributed the study to `Deng et al.` in prose notes, conflating co-author Zhaoxian Deng from the earlier discovery paper Li et al., *Org. Lett.* 2020 (`DOI:10.1021/acs.orglett.9b04559`, `PMID:31891272`) with the 2021 enzymatic mechanism paper authored by Zengzhi Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li (`Liu et al.`).
- **Remediation**:
  1. Updated all 80 curator-owned `DOI:10.1002/anie.202007777` evidence notes across `youssoufene-a1.yaml` and `youssoufene-b1.yaml`..`youssoufene-b4.yaml` from `Deng et al.` to `Liu et al.` through `write_validated_natural_product` and `record_curation_event`.
  2. Re-seeded all five records via `scripts/seed_from_sources.py` and regenerated HTML pages via `scripts/render_pages.py`.

### `G-YSF-003` — Upstream NPClassifier dimeric/monomeric category split, `UNGROUNDED` heterodimeric KS/CLF `PROTEIN_COMPLEX` nodes, and genus-level `BGC0002510` taxon boundary
- **Cause**:
  1. Pinned `data/raw/npclassifier.tsv` (`npclassifier.gnps2.org@2026-09-07`) classifies dimeric youssoufene A1 (`PBGNPVWDTRYFBH-GSOXOQHNSA-N`) under `POLYKETIDES` (`Linear polyketides`) while returning empty `pathway_results: []` for monomeric congeners youssoufenes B1-B4 (`UNCLASSIFIED`), locked in `data/natural_products/PATHS.tsv`.
  2. ComplexPortal and RHEA lack entries for the bacterial heterodimeric type II PKS KS/CLF complexes YsfB/YsfC, YsfD/YsfE, and YsfJ/YsfK and their polyene-forming steps, so `PROTEIN_COMPLEX` nodes `nodes[7..9]` properly remain `UNGROUNDED` (with subunit `ENZYME` nodes `nodes[0..3, 5..6]` grounded and linked via `is subunit of` edges).
  3. MIBiG 4.0 exports `BGC0002510:1..5` (`genbank:MT459140.1:71..11851`, `PMID:32860295`) at genus level (`NCBITaxon:1931`, *Streptomyces* sp.) without strain metadata, and `MT459140.1` / `PMID:32860295` are not indexed in PubMed/ENA to verify a cultured strain designation.
- **Disposition**: `deferred` in open GitHub issue [#1046](https://github.com/CultureBotAI/NaturalProductMech/issues/1046).

### `G-PEN-003` — Carried-forward upstream MIBiG salt and protonation-state encoding on benzylpenicillin sodium (`CHEBI:51765`) and monoanionic ACV (`CHEBI:58572`)
- **Cause**: Although Cycle 2 Stage 6 (#1015) implemented `REPLACE_SHARED_WITH_CHEBI` in `src/naturalproductmech/curate/structure_corrections.py`, `src/naturalproductmech/curate/claim_references.py:130` (`load_claim_references`) still raises `ValueError` whenever a `source_id` appears in both `curation/mibig_claim_references.tsv` and `curation/mibig_structure_corrections.tsv`. Because `BGC0000404:1`, `BGC0000405:1`, and `BGC0000405:3` have active claim-reference routing rows from #1023 (and `scripts/seed_from_sources.py` still keys claim-reference lookup only on `row["source_id"]` rather than falling back to `row.get("structure_source_id")`), migrating those rows in `curation/mibig_structure_corrections.tsv` requires the infrastructure enhancement recorded as `naturalproductmech-infra-0003` in `INFRA_TASKS.md` (following `infrastructure_note_policy: record_only` in Stage 5).
- **Disposition**: `deferred` in open GitHub issue [#1047](https://github.com/CultureBotAI/NaturalProductMech/issues/1047) and recorded in `INFRA_TASKS.md` as `naturalproductmech-infra-0003`.

### `G-PIK-DES-003` — Carried-forward upstream tautomeric/stereochemical separation of desosamine records and `BGC0000898`/`BGC0000094` deposit split
- **Cause**: `desosamine.yaml` (`naturalproductmech:mibig-bc0da8b0f6`, `BGC0000899:1`) encodes flat cyclic hexopyranose `ZOYWWAGVGBSJDL-UHFFFAOYSA-N` (`stereo_complete: false`) whereas `desosamine-2.yaml` (`CHEBI:32540`, `BGC0000898:1`) encodes 3-star ChEBI open-chain D-desosamine aldehyde `VTJCSBJRQLZNHE-CSMHCCOUSA-N` (`stereo_complete: true`), and 3-star ChEBI lacks a stereochemically complete cyclic D-desosamine entry. Separately, MIBiG splits the *S. venezuelae* `ATCC 15439` `pik`/`des` cluster across `BGC0000094` (`AF079138.1`, `CLUSTER_DEMONSTRATED`) and `BGC0000898` (`AF079762.1`, `CLUSTER_UNSTATED` with blank coordinates).
- **Disposition**: `deferred` in open GitHub issue [#1012](https://github.com/CultureBotAI/NaturalProductMech/issues/1012).
