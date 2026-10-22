# Stage 5 Finding Group & GitHub Issue Map (`mech-goal-sequence-20261019`, Cycle 1)

## Consumed Stage 4 Review Artifacts

| Kind | Path | SHA-256 |
| --- | --- | --- |
| `category` | `reviews/structured/20261022T012300Z-pik-des-macrolide-deoxysugar-cohort/review.yaml` | `eb3b7444b743374124f274e797160f30e6ab901500dd26a67bb83249ad235771` |
| `record` | `reviews/structured/20261022T012305Z-desosamine-2-record-review/review.yaml` | `6e5e0713efbc7276b9e24c380fd31987e4d3a7f5878bc85b4e2ef2ab70489e7b` |
| `workflow_manifest` | `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` | `5ff5e95614064cc07c266935d62e2afab68ebb4551623a97d687c3d149b203fa` |

## Grouped Findings, Repair Ownership, and GitHub Issue Mapping

| Group ID | Finding IDs | Issue Key | Severity | Status | Repair Owner | GitHub Issue | Target IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `G-PIK-DES-001` | `F-PIK-DES-001`, `F-DES2-001` | `pik-des-atcc15439-producer-strain-missing` | `major` | `resolved` | `curation/mibig_producer_strains.tsv` (+ `scripts/seed_from_sources.py`) | [#1010](https://github.com/CultureBotAI/NaturalProductMech/issues/1010) (`created`, closes with Stage 5 PR) | `CHEBI:32540`, `CHEBI:29630`, `CHEBI:29665`, `CHEBI:29656`, `CHEBI:29649` |
| `G-PIK-DES-002` | `F-PIK-DES-002` | `bgc0000899-narbonensis-cross-species-pmid9770448-citation` | `major` | `resolved` | `curation/mibig_claim_references.tsv` (+ `curation/lotus_occurrence_exclusions.tsv`) | [#1011](https://github.com/CultureBotAI/NaturalProductMech/issues/1011) (`created`, closes with Stage 5 PR) | `naturalproductmech:mibig-bc0da8b0f6` |
| `G-PIK-DES-003` | `F-PIK-DES-003`, `F-DES2-002` | `desosamine-cyclic-open-chain-and-bgc0000898-locus-split` | `minor` | `deferred` | `curation/mibig_structure_corrections.tsv` | [#1012](https://github.com/CultureBotAI/NaturalProductMech/issues/1012) (`created`, remains `open`) | `CHEBI:32540`, `naturalproductmech:mibig-bc0da8b0f6`, `CHEBI:29630`, `CHEBI:29665`, `CHEBI:29656`, `CHEBI:29649` |

## Group Details

### `G-PIK-DES-001` — Missing `ATCC 15439` producer strain qualification on five *S. venezuelae* `pik`/`des` records
- **Cause**: MIBiG 4.0 exports species-level `NCBITaxon:54571` (*Streptomyces venezuelae*) without strain metadata for `BGC0000094:1` and `BGC0000898:1..4`, even though Xue et al., *PNAS* 1998 (`PMID:9770448`, `DOI:10.1073/pnas.95.21.12111`) and GenBank deposits `AF079138.1` and `AF079762.1` explicitly identify the producer strain as *Streptomyces venezuelae* `ATCC 15439`. In addition, `scripts/seed_from_sources.py` skipped `mibig_producer_strains.tsv` rows on structure-corrected MIBiG rows unless the rationale explicitly named `structure_source_id`.
- **Remediation**:
  1. Added five source-pinned `ATCC 15439` rows (`BGC0000094:1`, `BGC0000898:1`, `BGC0000898:2`, `BGC0000898:3`, `BGC0000898:4`) to `curation/mibig_producer_strains.tsv`.
  2. Updated `scripts/seed_from_sources.py` and `docs/CURATION.md` so a reviewed `curation/mibig_producer_strains.tsv` entry whose `rationale` explicitly names `row["structure_source_id"]` applies to a structure-corrected row while unreviewed structure-corrected rows remain blocked.
  3. Re-ran `scripts/seed_from_sources.py`, `scripts/check_docs.py`, and `scripts/render_pages.py` to regenerate `desosamine-2.yaml`, `methymycin.yaml`, `pikromycin.yaml`, `neomethymycin.yaml`, and `narbomycin.yaml`.

### `G-PIK-DES-002` — Cross-species Xue et al. 1998 citation (`PMID:9770448` / `DOI:10.1073/PNAS.95.21.12111`) attached to *S. narbonensis* `BGC0000899:1` and LOTUS occurrence in `desosamine.yaml`
- **Cause**: MIBiG `BGC0000899.4` (*Streptomyces narbonensis*, `NCBITaxon:67333`, GenBank `AF521878.1`) and LOTUS row `ZOYWWAGVGBSJDL-UHFFFAOYSA-N | NCBITaxon:67333 | 10.1073/PNAS.95.21.12111` attach `PMID:9770448` / `DOI:10.1073/PNAS.95.21.12111` (Xue et al., *PNAS* 1998), which exclusively characterizes *Streptomyces venezuelae* `ATCC 15439` (`AF079138.1` / `AF079762.1`) and never mentions *S. narbonensis* or `AF521878.1`.
- **Remediation**:
  1. Added `BGC0000899:1` to `curation/mibig_claim_references.tsv`, routing the producer assertion to `https://mibig.secondarymetabolites.org/repository/BGC0000899.4/` and the locus assertion to `https://www.ncbi.nlm.nih.gov/nuccore/AF521878.1`.
  2. Added `ZOYWWAGVGBSJDL-UHFFFAOYSA-N | NCBITaxon:67333 | 10.1073/PNAS.95.21.12111` (`expected_source_row_sha256: c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e`) to `curation/lotus_occurrence_exclusions.tsv`.
  3. Re-seeded `data/natural_products/carbohydrates/desosamine.yaml` and updated `README.md` and `pages/`.

### `G-PIK-DES-003` — Upstream tautomeric/stereochemical separation of desosamine records and `BGC0000898`/`BGC0000094` deposit split
- **Cause**: `desosamine.yaml` (`naturalproductmech:mibig-bc0da8b0f6`, `BGC0000899:1`) encodes flat cyclic hexopyranose `ZOYWWAGVGBSJDL-UHFFFAOYSA-N` (`stereo_complete: false`) whereas `desosamine-2.yaml` (`CHEBI:32540`, `BGC0000898:1`) encodes 3-star ChEBI open-chain D-desosamine aldehyde `VTJCSBJRQLZNHE-CSMHCCOUSA-N` (`stereo_complete: true`), and 3-star ChEBI lacks a stereochemically complete cyclic D-desosamine entry. Separately, MIBiG splits the *S. venezuelae* `ATCC 15439` `pik`/`des` cluster across `BGC0000094` (`AF079138.1`, `CLUSTER_DEMONSTRATED`) and `BGC0000898` (`AF079762.1`, `CLUSTER_UNSTATED` with blank coordinates).
- **Disposition**: `deferred` in open GitHub issue [#1012](https://github.com/CultureBotAI/NaturalProductMech/issues/1012). Merging distinct InChIKeys or transferring `AF079138.1` locus grades without a 3-star cyclic D-desosamine ChEBI entry and deposit-level sequence alignment would violate corpus identity and deposit-scoped locus-grading rules.
