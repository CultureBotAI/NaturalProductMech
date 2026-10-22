# Stage 4 (`record_review`) Report — Run `mech-goal-sequence-20261019` (Cycle 1, Revision 1)

## 1. Executive Summary

This report records the Stage 4 (`record_review`) audit for run `mech-goal-sequence-20261019`, cycle `1`, pinned to the frozen post-Stage-3 repository baseline `f7f524c4ef03b54f78f24ad4cb5ac7db2dc066bf`.

- **Frozen Eligible Inventory**: `3,362` total YAML records (`3,116` natural product owner records in `data/natural_products/PATHS.tsv` [`2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3`], including `273` with inline `causal_graphs` and `27` with `causal_graph_refs`, plus `246` standalone causal graph component YAML files in `data/causal_graphs/` [combined path+sha256 manifest digest `92ee6b2458a6b9324837fda9f6efb5ed7c968710d0858ab416e34ae745b19bfc`]).
- **Corpus-Wide Deterministic Verification**: All `3,116` owner records and `246` standalone causal graph components were audited via:
  - `.venv/bin/python scripts/verify_corpus.py --summary` (`3,116` owner records verified, `0` errors, `0` warnings; output SHA256 `c9bcf7add9c5022125581df2e6b486735cd23803e49b73a4a2d6a60b62eebc5e`),
  - `.venv/bin/python scripts/validate_id_label_correspondence.py` (`13,449` canonical matches, `646` synonym matches, `35` documented exceptions, `0` ID_NOT_FOUND, `0` label mismatches; output SHA256 `c859dad0c7a6023dd517b77fdcb98bb923c85cef6d72bd3ccf600babbb9bc41e`),
  - `.venv/bin/python -m pytest -q tests/test_graph_components.py` (`246` standalone causal graph component YAML files validated, `40` passed, `0` failed; output SHA256 `1addc70b9c898aa0b26f903283dd652e3403a6e0f111121e094a1d46a7c31656`), and
  - `.venv/bin/python scripts/curation_worklist.py --review-records --limit 5` (`8,905` worklist items across `11` queues, `8,928` output lines; output SHA256 `21ceb24b744ee53c05d07dc655d00221db28f301469a9ded2cf9c3947a13da95`: `producer-evidence=2,292`, `biosynthesis=1,192`, `structure-disagreement=5`, `name-disagreement=67`, `unnamed-producer=39`, `shared-structure=207`, `needs-a-name=18`, `occurrence-only=12`, `pathway-ambiguous=620`, `unresolved-taxa=3,329`, `stereo-incomplete=1,124`).
- **Native Persistence Bundles Saved**:
  1. **Cohort Review (`review-yaml-category`)**: `reviews/structured/20261022T012300Z-pik-des-macrolide-deoxysugar-cohort/review.yaml` (`562f6c3e0ee24be113958d0651be6efadb28340f20c01f384b58b910a7351ccf`) and `review.md` (`1aa8d7bec9cabbb8272d3fdb819cf6c33a13dd380539d83580f0d172b7e9a5a1`) — covers the 6-record `pik`/`des` macrolide-deoxysugar cohort (`BGC0000094`, `BGC0000898`, `BGC0000899`).
  2. **Single-Record Review (`review-yaml-record`)**: `reviews/structured/20261022T012305Z-desosamine-2-record-review/review.yaml` (`612c74e4718d57a0502d30c78a98d2d0e620efa533f8a956dfde62279e695a08`) and `review.md` (`9232a1773c3ce38363202e86fa3ca645cd91fea7b9886ad22edfa50dc591d386`) — deep single-record audit of the newly split D-desosamine record (`data/natural_products/carbohydrates/desosamine-2.yaml`, `CHEBI:32540`).
- **Open Scientific Findings Preserved for Stage 5 (`resolve_review_findings`)**: `3` stable findings (`F-PIK-DES-001`, `F-PIK-DES-002`, `F-PIK-DES-003`) are preserved with `status: open` and exact remediation or boundary dispositions for Stage 5. No scientific record (`data/natural_products/`, `data/causal_graphs/`, `curation/*.tsv`) was mutated in Stage 4.

## 2. Frozen Inventory & Cohort Membership

| Record Path | Record ID | Name | Review Status | MIBiG Row | Record SHA256 | MIBiG Row SHA256 | Verdict (`ReviewVerdictEnum`) | Highest Finding Severity |
|---|---|---|---|---|---|---|---|---|
| `data/natural_products/carbohydrates/desosamine.yaml` | `naturalproductmech:mibig-bc0da8b0f6` | desosamine | `SEEDED` | `BGC0000899:1` | `054f874a6fb55098958357acfab7ecc78bcb597cfb04cf5437e9d74d29702c4d` | `82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922` | `needs_curation` | `major` |
| `data/natural_products/carbohydrates/desosamine-2.yaml` | `CHEBI:32540` | desosamine | `SEEDED` | `BGC0000898:1` | `e9aa2c5f8c764bac920477fda25577f8352012d088382090ec452c9d747c2f26` | `1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae` | `needs_curation` | `major` |
| `data/natural_products/polyketides/methymycin.yaml` | `CHEBI:29630` | methymycin | `SEEDED` | `BGC0000094:1` | `7c19ea9d7cedee074008cf7bed76bdf2f76abf41d8a659507778b26948b416ee` | `4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5` | `needs_curation` | `major` |
| `data/natural_products/polyketides/pikromycin.yaml` | `CHEBI:29665` | pikromycin | `SEEDED` | `BGC0000898:2` | `f64b4aaadd9a388a8dc4066f2fe15f052ad6a82bf4fc84884907db82d6d940b1` | `224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923` | `needs_curation` | `major` |
| `data/natural_products/polyketides/neomethymycin.yaml` | `CHEBI:29656` | neomethymycin | `SEEDED` | `BGC0000898:3` | `fc676329e89ea3bbd693300d380a8c11a231e476c51628f50bd9bb8b382ea1ef` | `002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead` | `needs_curation` | `major` |
| `data/natural_products/polyketides/narbomycin.yaml` | `CHEBI:29649` | narbomycin | `SEEDED` | `BGC0000898:4` | `b112dcc3d151dca470cae5bf9f4528892052edae5707ccc2e3c5a88d224f84de` | `1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578` | `needs_curation` | `major` |

## 3. Open Findings Preserved for Stage 5 (`resolve_review_findings`)

### `F-PIK-DES-001` — Missing `ATCC 15439` producer strain qualification on five *Streptomyces venezuelae* `pik`/`des` records (`BGC0000094:1` and `BGC0000898:1..4`)
- **Severity**: `high` (workflow) / `major` (native `record_review.yaml`)
- **Category**: `completeness` (`PRODUCER_OR_OCCURRENCE`)
- **Status**: `open`
- **Field Paths**: `producer_organisms[0].strain`, `producer_organisms[0].evidence`
- **Affected Records & Source Rows**:
  - `data/natural_products/carbohydrates/desosamine-2.yaml` (`BGC0000898:1`, `expected_source_row_sha256: 1c3876fb6e15ecdbd0e4724f6af87e536ae9e4acdba5b97d7cf5381641555eae`)
  - `data/natural_products/polyketides/methymycin.yaml` (`BGC0000094:1`, `expected_source_row_sha256: 4a66615916a0118fa9dcf7c56119cd2b9791512ce06b442c397ecb0f278675c5`)
  - `data/natural_products/polyketides/pikromycin.yaml` (`BGC0000898:2`, `expected_source_row_sha256: 224e597f0ea6fd4934bbbe480086fca606e478396c63e45cc1792ae879613923`)
  - `data/natural_products/polyketides/neomethymycin.yaml` (`BGC0000898:3`, `expected_source_row_sha256: 002165ca03d959d4ac1717fb17b12a597d30e31490cf647b99a3385aa5b95ead`)
  - `data/natural_products/polyketides/narbomycin.yaml` (`BGC0000898:4`, `expected_source_row_sha256: 1817fca43f98660561bd8629c91a1248ce3ac06336dbadbec56b138cb5888578`)
- **Evidence**: Xue et al., *Proc. Natl. Acad. Sci. U.S.A.* 95(21):12111-12116 (1998), `PMID:9770448`, `DOI:10.1073/pnas.95.21.12111`; GenBank `AF079138.1` and `AF079762.1`.
- **Stage 5 Remediation**: Add the five compound-row `source_id` keys (`BGC0000094:1`, `BGC0000898:1`, `BGC0000898:2`, `BGC0000898:3`, `BGC0000898:4`) with their `expected_source_row_sha256` digests to `curation/mibig_producer_strains.tsv` (`NCBITaxon:54571`, `Streptomyces venezuelae`, `ATCC 15439`, `DOI:10.1073/pnas.95.21.12111`) and re-run `.venv/bin/python scripts/seed_from_sources.py`.

### `F-PIK-DES-002` — Cross-species Xue et al. 1998 citation (`PMID:9770448` / `DOI:10.1073/PNAS.95.21.12111`) attached to *Streptomyces narbonensis* `BGC0000899:1` and LOTUS occurrence (`desosamine.yaml`)
- **Severity**: `medium` (workflow) / `major` (native `record_review.yaml`)
- **Category**: `provenance` (`EVIDENCE_MISMATCH`)
- **Status**: `open`
- **Field Paths**: `producer_organisms[0].evidence[0].reference`, `biosynthetic_gene_clusters[0].evidence[0].reference`, `occurrences[0].evidence[0].reference`
- **Affected Record & Source Rows**:
  - `data/natural_products/carbohydrates/desosamine.yaml` (`naturalproductmech:mibig-bc0da8b0f6`)
  - MIBiG row `BGC0000899:1` (`expected_source_row_sha256: 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922`)
  - LOTUS row `ZOYWWAGVGBSJDL-UHFFFAOYSA-N | NCBITaxon:67333 | 10.1073/PNAS.95.21.12111` (`expected_source_row_sha256: c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e`)
- **Evidence**: `PMID:9770448` (`DOI:10.1073/pnas.95.21.12111`) characterizes only *S. venezuelae* ATCC 15439 (`AF079138.1` / `AF079762.1`) and never sequences *Streptomyces narbonensis* (`NCBITaxon:67333`) or GenBank `AF521878.1` (deposited 4 years later in 2002; `genome_accession: genbank:AF521878.1` on the YAML record has no coordinates while `data/raw/mibig_compounds.tsv` reports `1..12895`, and both MIBiG evidence items carry `notes: "MIBiG BGC0000899 entry version 4; citation taken from the entry level"`).
- **Stage 5 Remediation**:
  1. Add `source_id=BGC0000899:1` (`expected_source_row_sha256: 82550891ca9f5a9b94c137f6a72ae676b7e02f65eb8044803852b6dba7113922`) to `curation/mibig_claim_references.tsv` routing `producer_reference` to `https://mibig.secondarymetabolites.org/repository/BGC0000899.4/` and `locus_reference` / `source_reference` to `https://www.ncbi.nlm.nih.gov/nuccore/AF521878.1`.
  2. Add (`standard_inchi_key=ZOYWWAGVGBSJDL-UHFFFAOYSA-N`, `taxon_id=NCBITaxon:67333`, `reference_doi=10.1073/PNAS.95.21.12111`, `expected_source_row_sha256=c05b5dfc535431dcdf6070557c3cf941cc6faeed67f285376f144e1e44dd895e`) to `curation/lotus_occurrence_exclusions.tsv`, then re-run `.venv/bin/python scripts/seed_from_sources.py`.

### `F-PIK-DES-003` — Upstream stereo-incomplete cyclic tautomer on `BGC0000899:1` (`desosamine.yaml`) and unmerged `BGC0000094`/`BGC0000898` cluster split
- **Severity**: `low` (workflow) / `minor` (native `record_review.yaml`)
- **Category**: `representation` (`LUMP_AND_SPLIT`)
- **Status**: `open`
- **Field Paths**: `chemical_structure.standard_inchi_key`, `chemical_structure.smiles`, `biosynthetic_gene_clusters[0].link_evidence_basis`, `biosynthetic_gene_clusters[0].locus_evidence_methods`
- **Affected Records**: All 6 cohort records (`desosamine.yaml`, `desosamine-2.yaml`, `methymycin.yaml`, `pikromycin.yaml`, `neomethymycin.yaml`, `narbomycin.yaml`).
- **Stage 5 Disposition**: Source-limited boundary (`DEFER` with documented rationale in Stage 5) until ChEBI or MIBiG supplies a 3-star stereochemically defined cyclic D-desosaminopyranose entry or unifies tautomer identity and cluster deposits (`AF079138.1` vs `AF079762.1`).
