# Stage 4 (`record_review`) Report — Run `mech-goal-sequence-20261019` (Cycle 1, Revision 1)

## 1. Executive Summary

This report records the Stage 4 (`record_review`) audit for run `mech-goal-sequence-20261019`, cycle `1`, pinned to the frozen post-Stage-3 repository baseline `f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf`.

- **Frozen Eligible Inventory**: `3,202` total records (`3,116` natural product owner records in `data/natural_products/PATHS.tsv` [`2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3`] plus `86` linked causal graph components in `data/causal_graphs/`).
- **Corpus-Wide Deterministic Verification**: All `3,116` owner records and `86` causal graph components were audited via `.venv/bin/python scripts/verify_corpus.py --summary` (`0` errors, `0` warnings), `.venv/bin/python scripts/validate_id_label_correspondence.py` (`13,449` canonical matches, `646` synonym matches, `35` documented exceptions, `0` ID_NOT_FOUND, `0` label mismatches), and `.venv/bin/python scripts/curation_worklist.py --review-records --limit 5` (`8,928` worklist items across `11` queues).
- **Native Persistence Bundles Saved**:
  1. **Cohort Review (`review-yaml-category`)**: `reviews/structured/20261022T012300Z-pik-des-macrolide-deoxysugar-cohort/review.yaml` (`be7836c96dd7ab8591a677e23758c96e417e0b3576e69f087a4a670414a44036`) and `review.md` (`b9a1911537ce4b63715b2406cf1c0051ae821eb513d76f8b1231ed5607dbb135`) — covers the 6-record `pik`/`des` macrolide-deoxysugar cohort (`BGC0000094`, `BGC0000898`, `BGC0000899`).
  2. **Single-Record Review (`review-yaml-record`)**: `reviews/structured/20261022T012305Z-desosamine-2-record-review/review.yaml` (`86943df0f80cd043fefeb5a861d2932c14cefe00c5bca8e33dfd3326ead2c8b3`) and `review.md` (`101d42e0bb280bce645393c0643899d41cf8fd4f20b4c285cf273bfdddbc97fe`) — deep single-record audit of the newly split D-desosamine record (`data/natural_products/carbohydrates/desosamine-2.yaml`, `CHEBI:32540`).
- **Open Scientific Findings Preserved for Stage 5 (`resolve_review_findings`)**: `3` stable findings (`F-PIK-DES-001`, `F-PIK-DES-002`, `F-PIK-DES-003`) are preserved with `status: open` and exact remediation or boundary dispositions for Stage 5. No scientific record (`data/natural_products/`, `data/causal_graphs/`, `curation/*.tsv`) was mutated in Stage 4.

## 2. Frozen Inventory & Cohort Membership

| Record Path | Record ID | Name | Review Status | MIBiG Row | Record SHA256 | MIBiG Row SHA256 | Verdict |
|---|---|---|---|---|---|---|---|
| `data/natural_products/carbohydrates/desosamine.yaml` | `naturalproductmech:mibig-bc0da8b0f6` | Desosamine | `SEEDED` | `BGC0000899:1` | `054f874a6fb55098958357acfab7ecc78bcb597cfb04cf5437e9d74d29702c4d` | `82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922` | `FAIL` |
| `data/natural_products/carbohydrates/desosamine-2.yaml` | `CHEBI:32540` | D-desosamine | `SEEDED` | `BGC0000898:1` | `e9aa2c5f8c764bac920477fda25577f8352012d088382090ec452c9d747c2f26` | `1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae` | `NEEDS_CURATION` |
| `data/natural_products/polyketides/methymycin.yaml` | `CHEBI:29630` | methymycin | `SEEDED` | `BGC0000094:1` | `7c19ea9d7cedee074008cf7bed76bdf2f76abf41d8a659507778b26948b416ee` | `4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5` | `NEEDS_CURATION` |
| `data/natural_products/polyketides/pikromycin.yaml` | `CHEBI:29665` | pikromycin | `SEEDED` | `BGC0000898:2` | `f64b4aaadd9a388a8dc4066f2fe15f052ad6a82bf4fc84884907db82d6d940b1` | `224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923` | `NEEDS_CURATION` |
| `data/natural_products/polyketides/neomethymycin.yaml` | `CHEBI:29656` | neomethymycin | `SEEDED` | `BGC0000898:3` | `fc676329e89ea3bbd693300d380a8c11a231e476c51628f50bd9bb8b382ea1ef` | `002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead` | `NEEDS_CURATION` |
| `data/natural_products/polyketides/narbomycin.yaml` | `CHEBI:29649` | narbomycin | `SEEDED` | `BGC0000898:4` | `b112dcc3d151dca470cae5bf9f4528892052edae5707ccc2e3c5a88d224f84de` | `1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578` | `NEEDS_CURATION` |

## 3. Open Findings Preserved for Stage 5 (`resolve_review_findings`)

### `F-PIK-DES-001` — Missing `ATCC 15439` producer strain qualification on five *Streptomyces venezuelae* `pik`/`des` records (`BGC0000094` and `BGC0000898`)
- **Severity**: `high` (workflow) / `major` (native `record_review.yaml`)
- **Category**: `completeness` (`PRODUCER_OR_OCCURRENCE`)
- **Status**: `open`
- **Affected Records**:
  - `data/natural_products/carbohydrates/desosamine-2.yaml` (`BGC0000898:1`)
  - `data/natural_products/polyketides/methymycin.yaml` (`BGC0000094:1`)
  - `data/natural_products/polyketides/pikromycin.yaml` (`BGC0000898:2`)
  - `data/natural_products/polyketides/neomethymycin.yaml` (`BGC0000898:3`)
  - `data/natural_products/polyketides/narbomycin.yaml` (`BGC0000898:4`)
- **Evidence**: Xue et al., *Proc. Natl. Acad. Sci. U.S.A.* 95(21):12111-12116 (1998), `PMID:9770448`, `DOI:10.1073/pnas.95.21.12111`; GenBank `AF079138.1` and `AF079762.1`.
- **Stage 5 Remediation**: Add `BGC0000094` and `BGC0000898` rows to `curation/mibig_producer_strains.tsv` (`NCBITaxon:54571`, `Streptomyces venezuelae`, `ATCC 15439`, `PMID:9770448`) and re-run `.venv/bin/python scripts/seed_from_sources.py`.

### `F-PIK-DES-002` — Cross-species `PMID:9770448` citation attached to *Streptomyces narbonensis* and `AF521878.1` on `BGC0000899` (`desosamine.yaml`)
- **Severity**: `medium` (workflow) / `major` (native `record_review.yaml`)
- **Category**: `provenance` (`EVIDENCE_MISMATCH`)
- **Status**: `open`
- **Affected Record**: `data/natural_products/carbohydrates/desosamine.yaml` (`BGC0000899:1`)
- **Evidence**: `PMID:9770448` characterizes only *S. venezuelae* ATCC 15439 (`AF079138.1` / `AF079762.1`) and never sequences *Streptomyces narbonensis* (`NCBITaxon:67333`) or GenBank `AF521878.1` (deposited 4 years later in 2002).
- **Stage 5 Remediation**: Add `BGC0000899` to `curation/mibig_claim_references.tsv` routing `producer_reference` to `https://mibig.secondarymetabolites.org/repository/BGC0000899.4/` and `locus_reference` to `https://www.ncbi.nlm.nih.gov/nuccore/AF521878.1`, then re-run `.venv/bin/python scripts/seed_from_sources.py`.

### `F-PIK-DES-003` — Upstream stereo-incomplete cyclic tautomer on `BGC0000899:1` (`desosamine.yaml`) and unmerged `BGC0000094`/`BGC0000898` cluster split
- **Severity**: `low` (workflow) / `minor` (native `record_review.yaml`)
- **Category**: `representation` (`LUMP_AND_SPLIT`)
- **Status**: `open`
- **Affected Records**: All 6 cohort records (`desosamine.yaml`, `desosamine-2.yaml`, `methymycin.yaml`, `pikromycin.yaml`, `neomethymycin.yaml`, `narbomycin.yaml`).
- **Stage 5 Disposition**: Source-limited boundary (`DEFER` with documented rationale in Stage 5) until ChEBI or MIBiG supplies a 3-star stereochemically defined cyclic D-desosaminopyranose entry or unifies tautomer identity and cluster deposits (`AF079138.1` vs `AF079762.1`).
