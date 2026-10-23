# Stage 4 (`record_review`) Report — Run `mech-goal-sequence-20261019` (Cycle 2, Revision 1)

## 1. Executive Summary

This report records the Stage 4 (`record_review`) audit for run `mech-goal-sequence-20261019`, cycle `2`, pinned to the frozen post-Stage-3 repository baseline `508e90d99e8e8cb7627eb8c885d535be25873c7f`.

- **Frozen Eligible Inventory**: `3,362` total YAML records (`3,116` natural product owner records in `data/natural_products/PATHS.tsv` [`2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3`], including `282` with inline `causal_graphs`, `27` with `causal_graph_refs`, `3,116` with `curation_status: SEEDED`, and `11` carrying historical `action: REVIEWED` in `curation_history`, plus `246` standalone causal graph component YAML files in `data/causal_graphs/` [combined path+sha256 manifest digest `f0db8ac7f96b28947fb53eee86c7e2b4148319cba1742a1a6a75686613972fe7`]).
- **Corpus-Wide Deterministic Verification**: All `3,116` owner records and `246` standalone causal graph components were audited via:
  - `.venv/bin/python scripts/verify_corpus.py --summary` (`3,116` owner records verified, `0` errors; output SHA256 `c9bcf7add9c5022125581df2e6b486735cd23803e49b73a4a2d6a60b62eebc5e`),
  - `.venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/c2_s4_id_label.tsv` (`13,465` canonical matches, `655` synonym matches, `35` documented exceptions, `499` warn-level `taxon_labels` mismatches, `0` ID_NOT_FOUND, `4,790` skipped-no-adapter; output SHA256 `c8bb404d2189463dd173a7ddea6b48893bdba5af63321842dac90984211f41c3`, report TSV SHA256 `fe66438001b7bdb1b56a18c44a7aa432b5913b9e9c372662bf976cd91c864b0c`),
  - `.venv/bin/python -m pytest -q tests/test_graph_components.py` (`246` standalone causal graph component YAML files validated, `40` passed, `0` failed; output SHA256 `b5a96643be6dd236e181473fa1bbb15fbe22452a95447e99ddc4b6b0a949d7a2`), and
  - `.venv/bin/python scripts/curation_worklist.py --review-records --limit 5` (`8,924` worklist items across `12` queues; output SHA256 `7edbdc274466a876b3ef923cd3fa7c5a711f1f6aa3119d96c43ef85c7c768c31`: `producer-evidence=2,292`, `biosynthesis=1,184`, `structure-disagreement=5`, `name-disagreement=67`, `unnamed-producer=39`, `shared-structure=207`, `needs-a-name=18`, `occurrence-only=12`, `pathway-ambiguous=620`, `unresolved-taxa=3,329`, `stereo-incomplete=1,124`, `record-review=27`).
- **Native Persistence Bundles Saved**:
  1. **Cohort Review (`review-yaml-category`)**: `reviews/structured/20261023T115930Z-penicillium-chrysogenum-penicillin-cohort/review.yaml` (`e71e4a476abae109905bc88f6f0cba6e88fdef9eef157d8008ac66a31a457906`) and `review.md` (`b01b1982d5c0bc8fef5d4eedad49ff26f6f8124e682228baf776cd42c4cb5cd3`) — covers the 3-record *Penicillium chrysogenum* (`NCBITaxon:5076`) penicillin biosynthetic cohort (`BGC0000404`, `BGC0000405`) whose pathway steps (`PcbAB` / `PcbC`) and causal graphs were curated and UniProt-grounded in Cycle 2 Stages 2 and 3.
  2. **Single-Record Review (`review-yaml-record`)**: `reviews/structured/20261023T115935Z-benzylpenicillin-sodium-record-review/review.yaml` (`ff55de36d206b4a1ef9ac412439a3c910705373b240e803631635fbe361ee8fa`) and `review.md` (`d0242044cc837ee8c9622a582b24b861e367322a309faccd73820a88076fdd0f`) — deep single-record audit of `data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml` (`CHEBI:51765`).
- **Open & Carried-Forward Scientific Findings Preserved for Stage 5 (`resolve_review_findings`)**: `3` new open findings (`F-PEN-001`, `F-PEN-002`, `F-PEN-003`) plus `1` carried-forward deferred finding (`F-PIK-DES-003` from Cycle 1 Stage 5 `#1012`) are preserved with exact remediation or boundary dispositions for Stage 5. No scientific record (`data/natural_products/`, `data/causal_graphs/`, `curation/*.tsv`) was mutated in Stage 4.

## 2. Frozen Inventory & Cohort Membership

| Record Path | Record ID | Name | Review Status | MIBiG Rows | Record SHA256 | MIBiG Row SHA256 (`row_digest`) | Verdict (`ReviewVerdictEnum`) | Highest Finding Severity |
|---|---|---|---|---|---|---|---|---|
| `data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml` | `CHEBI:58572` | N-[(5S)-5-ammonio-5-carboxylatopentanoyl]-L-cysteinyl-D-valinate | `SEEDED` | `BGC0000405:1` | `369d888b75ac4cbe1c1c95a8fb6a7e15c27cb97d27d69875a1e1b83599e3bbd5` | `50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1` | `needs_curation` | `major` |
| `data/natural_products/amino_acids_and_peptides/isopenicillin-n.yaml` | `CHEBI:18165` | isopenicillin N | `SEEDED` | `BGC0000405:2` | `02dfa271ed3ca87f0cdcaea0b0e701ec1fab935d3a5f559d6955565193bbdf75` | `ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860` | `needs_curation` | `major` |
| `data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml` | `CHEBI:51765` | benzylpenicillin sodium | `SEEDED` | `BGC0000404:1`, `BGC0000405:3` | `201779de13d90f23e3ec700c3bd7dbaa46cacd9a0f74d87638b35eb5e51a5bf2` | `9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19`, `847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42` | `needs_curation` | `major` |

## 3. Open & Carried-Forward Findings Preserved for Stage 5 (`resolve_review_findings`)

### `F-PEN-001` — Missing `AS-P-78` (`BGC0000404:1`) and `Wisconsin 54-1255` (`BGC0000405:1..3`) producer strain qualifications on *Penicillium chrysogenum* (`NCBITaxon:5076`) records
- **Severity**: `high` (workflow) / `major` (native `record_review.yaml`)
- **Category**: `completeness` (`PRODUCER_OR_OCCURRENCE`)
- **Status**: `open`
- **Field Paths**: `producer_organisms[0].strain`, `producer_organisms[0].evidence`
- **Affected Records & Source Rows**:
  - `data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml` (`BGC0000405:1`, `expected_source_row_sha256: 50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1`)
  - `data/natural_products/amino_acids_and_peptides/isopenicillin-n.yaml` (`BGC0000405:2`, `expected_source_row_sha256: ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860`)
  - `data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml` (`BGC0000404:1` [`9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19`] and `BGC0000405:3` [`847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42`])
- **Evidence**: Fierro et al., *Fungal Genet. Biol.* 43(9):618-629 (2006), `PMID:16713314`, `DOI:10.1016/j.fgb.2006.03.001` (GenBank `DQ192518.1`, strain `AS-P-78`); van den Berg et al., *Fungal Genet. Biol.* 44(9):830-843 (2007), `PMID:17499530`, `DOI:10.1016/j.fgb.2007.03.008` (GenBank `EF601124.1`, strain `Wisconsin 54-1255`).
- **Stage 5 Remediation**: Add four source-pinned rows (`BGC0000404:1`, `BGC0000405:1`, `BGC0000405:2`, `BGC0000405:3`) to `curation/mibig_producer_strains.tsv` and re-run `.venv/bin/python scripts/seed_from_sources.py`.

### `F-PEN-002` — Anachronistic entry-level citations on `BGC0000404:1` (`DOI:10.1016/s0140-6736(00)87452-8`, Chain et al. 1940 on `DQ192518.1`) and `BGC0000405:1..3` (`PMID:1368505`, Smith et al. 1990 on `EF601124.1`)
- **Severity**: `medium` (workflow) / `major` (native `record_review.yaml`)
- **Category**: `provenance` (`EVIDENCE_MISMATCH`)
- **Status**: `open`
- **Field Paths**: `producer_organisms[0].evidence`, `biosynthetic_gene_clusters[0].evidence`, `biosynthetic_gene_clusters[1].evidence`
- **Affected Records & Source Rows**:
  - `data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml` (`BGC0000405:1`, `50cbd967cf8076f7cbfa5a77bbb9b2910e1e37593d10edea50ad6c3a83316de1`)
  - `data/natural_products/amino_acids_and_peptides/isopenicillin-n.yaml` (`BGC0000405:2`, `ae975df0e01f81b73c2e119b776207ca3e0f061375585a06ceef3f099dbbe860`)
  - `data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml` (`BGC0000404:1`, `9460d29fcad2b7ecb913298bc80838656966e219ec0654094d28b71942eaeb19`; `BGC0000405:3`, `847cf368dc26e162604ac12681781efc5814bcc31c4e19e94b09578562a1dd42`)
- **Evidence**: `DOI:10.1016/s0140-6736(00)87452-8` (Chain et al., *Lancet* 1940) predates GenBank `DQ192518.1` (`BGC0000404:1`) by 65 years; `PMID:1368505` (Smith et al., *EMBO J.* 1990) predates GenBank `EF601124.1` (`BGC0000405:1..3`) by 17 years.
- **Stage 5 Remediation**: Add `BGC0000404:1` (`DOI:10.1016/j.fgb.2006.03.001`) and `BGC0000405:1..3` (`DOI:10.1016/j.fgb.2007.03.008`) to `curation/mibig_claim_references.tsv` and re-run `.venv/bin/python scripts/seed_from_sources.py`.

### `F-PEN-003` — Upstream MIBiG salt and protonation-state encoding on `CHEBI:51765` (`benzylpenicillin sodium` vs biological `CHEBI:51354`) and `CHEBI:58572` (monoanion vs neutral ACV `CHEBI:28496`)
- **Severity**: `low` (workflow) / `minor` (native `record_review.yaml`)
- **Category**: `representation` (`LUMP_AND_SPLIT`)
- **Status**: `open`
- **Field Paths**: `id`, `name`, `chemical_structure.standard_inchi_key`, `chemical_structure.smiles`, `biosynthetic_pathway`
- **Affected Records**: `data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml` (`CHEBI:51765`) and `data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml` (`CHEBI:58572`).
- **Stage 5 Disposition**: Source-limited representation boundary (`DEFER` in Stage 5 linked to `#1015`) unless a pharmaceutical counterion-stripping policy is adopted in `curation/structure_corrections.tsv`.

### `F-PIK-DES-003` (Carried Forward from Cycle 1 Stage 5 `#1012`) — Upstream stereo-incomplete cyclic tautomer on `BGC0000899:1` (`desosamine.yaml`) and unmerged `BGC0000094`/`BGC0000898` cluster split
- **Status**: `deferred` (`carried_from: F-PIK-DES-003`, `issue_url: https://github.com/CultureBotAI/NaturalProductMech/issues/1012`)
- **Disposition**: Carried forward from Cycle 1 Stage 5 (`reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml`) as a deferred upstream representation boundary tracked in `#1012`.
