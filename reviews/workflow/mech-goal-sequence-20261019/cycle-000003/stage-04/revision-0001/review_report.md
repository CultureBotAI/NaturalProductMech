# Workflow Stage 4 Record & Cohort Review Report (Cycle 3, Revision 1)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: `3` / `4` (`record_review`) / `1`
- **Repository**: `CultureBotAI/NaturalProductMech` (`naturalproductmech`)
- **Frozen Source Revision (`HEAD`)**: `d14547bc76e0582aca15eeb073e203d28ea7548e`
- **Previous Review/Remediation Evidence Manifest**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml` (`8b791c06d925b39a701c2f9e0919fe64963bbf92461ac850208539f0efdcd3e5`)
- **Latest Prior Workflow Evidence Manifest (Cycle 2 Stage 6)**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/evidence.yaml` (`af17914a8d3f0028698cef2671d787204fdc4d58174b6fe2cea29c039b4b185d`)
- **Native Review Persistence Bundles**:
  1. Category/Cohort Review (`kind: category`, skill `review-yaml-category`):
     - `reviews/structured/20261025T055000Z-streptomyces-youssoufiensis-youssoufene-cohort/review.yaml` (`f55bc505b5e614cc3732c6abbabb9216a33a3a8fe2310dfc1adfe5846681c120`)
     - `reviews/structured/20261025T055000Z-streptomyces-youssoufiensis-youssoufene-cohort/review.md` (`2b336c1b8dbb49abb7993f789abda2de10f8bb803b9e8446cb6b88e63cd5b9c0`)
  2. Single-Record Deep Audit (`kind: record`, skill `review-yaml-record`):
     - `reviews/structured/20261025T055005Z-youssoufene-a1-record-review/review.yaml` (`cd4bed0269fe80314aee0757ab8369985115cedc5607a1520babb6301a2a3cb7`)
     - `reviews/structured/20261025T055005Z-youssoufene-a1-record-review/review.md` (`3f122881a3f3a11eeb2db6a90f74ae76f26e71cfa64923a0528b88c281fff5e5`)

---

## 1. Frozen Inventory & Full-Corpus Gate Summary

At frozen post-Stage-3 commit `d14547bc76e0582aca15eeb073e203d28ea7548e`, the eligible corpus comprises **3,362 YAML records**:
- **3,116** natural product owner records indexed in `data/natural_products/PATHS.tsv` (`sha256: 2c9c281744ec13b23711a42b9901ffd88a0d8f1e4fdf0a6102b1c677ff0389f3`), including `290` owner records with inline `causal_graphs`, `27` owner records with `causal_graph_refs`, and `11` records carrying a historical `REVIEWED` entry in `curation_history`.
- **246** standalone causal graph components under `data/causal_graphs/` (`manifest_sha256: f0db8ac7f96b28947fb53eee86c7e2b4148319cba1742a1a6a75686613972fe7`).

All 3,362 eligible YAML records were audited through deterministic full-corpus validation and worklist gates, paired with deep source-backed cohort and single-record reviews on the newly enriched Cycle 3 *Streptomyces youssoufiensis* (`NCBITaxon:654447`, `mibig:BGC0002547`) / *Streptomyces* sp. (`NCBITaxon:1931`, `mibig:BGC0002510`) youssoufene polyene-bridged benzene-ring cohort (`5` records):

| Checkpoint | Command | Digest (`sha256`) | Summary |
|---|---|---|---|
| Full-corpus verification | `.venv/bin/python scripts/verify_corpus.py --summary` | `c9bcf7add9c5022125581df2e6b486735cd23803e49b73a4a2d6a60b62eebc5e` | `3,116` owner records verified, `0` errors, lockfile integrity OK |
| Ontology ID-label correspondence | `.venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/c3_s4_id_label.tsv` | stdout `35423598d9ea0c53a374976d422665d7bfaf789855b7fd3357b97c7bc356f816`; TSV `fd6b4d6d15cac69220daf9027ac7dcb0a252f509e5bc69d831d181d0d6a6bd6b` | `OK_CANONICAL: 12619`, `OK_SYNONYM: 567`, `OK_EXCEPTION: 35`, `MISMATCH: 499` (warn-only taxon labels), `SKIPPED_NO_ADAPTER: 4898`, exit `0` |
| Standalone causal graph suite | `.venv/bin/pytest -q tests/test_graph_components.py` | `53e35ce114ca8fbf31b29cd0f5c1bac68a5dc6669944111d81e4323f8136b317` | `40 passed` across `246` standalone graph components |
| Curation worklist review queue | `.venv/bin/python scripts/curation_worklist.py --review-records --limit 5` | `2c671a47982350c5968f24b020377eb57b876914d4882d295562790da8f3d330` | `8,922` items across `12` queues (`producer-evidence: 2292`, `biosynthesis: 1177`, `structure-disagreement: 5`, `name-disagreement: 67`, `unnamed-producer: 39`, `shared-structure: 207`, `needs-a-name: 18`, `occurrence-only: 12`, `pathway-ambiguous: 620`, `unresolved-taxa: 3329`, `stereo-incomplete: 1124`, `record-review: 32`) |
| Cohort strict validation | `.venv/bin/python scripts/validate_strict.py data/natural_products/polyketides/youssoufene-a1.yaml data/natural_products/unclassified/youssoufene-b1.yaml data/natural_products/unclassified/youssoufene-b2.yaml data/natural_products/unclassified/youssoufene-b3.yaml data/natural_products/unclassified/youssoufene-b4.yaml` | `590bdeb29003f5b00c5fe407e313812c3bc83e00cd4980060ee32e333dced520` | `5` files scanned, `0` ERROR rows, `120` WARN rows, `15` INFO rows |
| Record strict validation | `.venv/bin/python scripts/validate_strict.py data/natural_products/polyketides/youssoufene-a1.yaml` | `a1421dbacfc9e16ebc794429217734cf62f8eb381d7b099d33457486fd192ef7` | `1` file scanned, `0` ERROR rows, `24` WARN rows, `3` INFO rows |

---

## 2. Deep Cohort & Record Review Targets (Cycle 3 Enriched Youssoufene Cohort)

| Record Path | Identifier | Label | Record `sha256` | MIBiG Source Rows (`sha256`) | Verdict | Highest Finding Severity |
|---|---|---|---|---|---|---|
| `data/natural_products/polyketides/youssoufene-a1.yaml` | `naturalproductmech:mibig-78ea4c55fb` | youssoufene A1 | `7bb8f5d4d4bd5e30083973a8a2e41adefe24b1a77f0ad34480e9ba0b15f368a6` | `BGC0002510:1` (`c3e0435917bbd397fd24aea07e7c3b9d3ab5e82f9c78ef6da21bb8ea14af03a5`), `BGC0002547:1` (`1d48b2327fd1ff6df8dacc84f722e6dcef3c298cafc6442b51a0d2190b11547f`) | `needs_curation` | `major` |
| `data/natural_products/unclassified/youssoufene-b1.yaml` | `naturalproductmech:mibig-ccb60942af` | youssoufene B1 | `ea395342b0f7b1b4b8038e7a731c274e1c1ceb2645f2ea8e94ac5ba8613b7746` | `BGC0002510:2` (`21a73e5ac9b76d1786526d9777da8ba9b88dc0aa1a420232f6e13936cf13b838`), `BGC0002547:2` (`acd26c9cf5030b8b06c4534bb1919c878ff432bb8bfdf1d87f7c0476926c81d4`) | `needs_curation` | `major` |
| `data/natural_products/unclassified/youssoufene-b2.yaml` | `naturalproductmech:mibig-cf5248036e` | youssoufene B2 | `00ec251535ea020620a618880c862ff19eed67e5468f87a65bc227637cdede23` | `BGC0002510:3` (`c641bc134e699b6a5725a08aa96bc5245ba988918655e55306d11033a1a3552d`), `BGC0002547:3` (`ea799308305a5d8e5c0a42a0895dc7ee080379a727a26269e01829e6530ffdb7`) | `needs_curation` | `major` |
| `data/natural_products/unclassified/youssoufene-b3.yaml` | `naturalproductmech:mibig-f827d9f550` | youssoufene B3 | `65059808b4f28c4fc23f5fbf9b2e4390443c0f59477e4428c998cfee3c0020bc` | `BGC0002510:4` (`3ee732419ebcefc2eb1947c0a3726c2957b24dc9b5c6fa9fb4f16060246049cb`), `BGC0002547:4` (`e9c6f5c63e79b21bdba197184998ff4583f3d324777d335c5047311056715007`) | `needs_curation` | `major` |
| `data/natural_products/unclassified/youssoufene-b4.yaml` | `naturalproductmech:mibig-18ba3c758c` | youssoufene B4 | `f6bf3a389fd5b5f5f60b7d08e922a450cf1409327db785f727b117d4165ff5a7` | `BGC0002510:5` (`440036d2d8e8c6821c0e40687d768d801b49d888565b9f72765c290bc7eb1c5a`), `BGC0002547:5` (`deba7c3574dc3b75f9d6045232b4f21275bf1a38eddc988bc837e8490db9da00`) | `needs_curation` | `major` |

---

## 3. Stable Stage 4 Findings & Carried-Forward Findings

### New Open Findings from Cycle 3 Stage 4 (`F-YSF-001`, `F-YSF-002`, `F-YSF-003`)

1. **`F-YSF-001` (`completeness`, `major`, `open`) — Missing `OUC6819` producer strain qualifications on *Streptomyces youssoufiensis* (`NCBITaxon:654447`, `BGC0002547:1..5`) across all 5 youssoufene records**:
   - All five records (`youssoufene-a1.yaml`, `youssoufene-b1.yaml`, `youssoufene-b2.yaml`, `youssoufene-b3.yaml`, `youssoufene-b4.yaml`) omit `producer_organisms[0].strain` because MIBiG 4.0 `BGC0002547` (`genbank:MN844187.1`, `1..20186`) records species-level `organism_name: Streptomyces youssoufiensis` (`NCBITaxon:654447`). Both primary publications — Li et al., *Org. Lett.* 2020;22(2):704-708 (`PMID:31891272`, `DOI:10.1021/acs.orglett.9b04559`) and Liu et al., *Angew. Chem. Int. Ed.* 2021;60(1):153-158 (`PMID:33155752`, `DOI:10.1002/anie.202007777`) — as well as GenBank `MN844187.1` (`/strain="OUC6819"`) and each record's own `causal_graphs[0].nodes[0..6].protein_examples[0].strain` (`OUC6819`) explicitly identify the sequenced producer strain as *Streptomyces youssoufiensis* `OUC6819`.
   - **Stage 5 Remediation**: Add 5 source-pinned rows (`BGC0002547:1..5`) to `curation/mibig_producer_strains.tsv` with `strain=OUC6819` and `reference=PMID:31891272` and re-seed via `scripts/seed_from_sources.py`.

2. **`F-YSF-002` (`provenance`, `major`, `open`) — Misattributed author citation (`"Deng et al."` instead of `"Liu et al."`) in 80 `DOI:10.1002/anie.202007777` evidence notes across all 5 youssoufene records**:
   - Across all 5 youssoufene records, every `biosynthetic_pathway[0..3].evidence[0].notes` (`4` per record) and every `causal_graphs[0].edges[0..11].evidence[0].notes` (`12` per record) citing `DOI:10.1002/anie.202007777` (`16` notes per record; `80` notes total) attributes `DOI:10.1002/anie.202007777` (*Angew. Chem. Int. Ed.* 2021;60(1):153-158, `PMID:33155752`) to `"Deng et al."`. PubMed (`PMID:33155752`) and Crossref (`DOI:10.1002/anie.202007777`) confirm the authors of `DOI:10.1002/anie.202007777` are Zengzhi Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li (`"Liu et al."`); Zhaoxian Deng was a co-author on the 2020 *Org. Lett.* paper (`PMID:31891272`, `DOI:10.1021/acs.orglett.9b04559`), not on `DOI:10.1002/anie.202007777`.
   - **Stage 5 Remediation**: Replace `"Deng et al. (Angew. Chem. Int. Ed. 2021, DOI:10.1002/anie.202007777)"` with `"Liu et al. (Angew. Chem. Int. Ed. 2021, PMID:33155752, DOI:10.1002/anie.202007777)"` across all 80 curator-owned evidence notes on the 5 records and regenerate HTML pages.

3. **`F-YSF-003` (`representation`, `minor`, `open`) — Upstream NPClassifier split, `PROTEIN_COMPLEX` / `RHEA` grounding boundaries, and unindexed `BGC0002510` deposit metadata (`MT459140.1` / `PMID:32860295`)**:
   - (1) NPClassifier (`npclassifier.gnps2.org@2026-04-06`) classifies dimeric `youssoufene-a1.yaml` under `POLYKETIDES` (`Linear polyketides`) while returning empty `pathway_results: []` (`UNCLASSIFIED`) for monomeric `youssoufene-b1.yaml` through `youssoufene-b4.yaml`; (2) heterodimeric KS/CLF `PROTEIN_COMPLEX` nodes (`ysfbc_ks_clf` [`nodes[7]`], `ysfde_ks_clf` [`nodes[8]`], `ysfjk_ks_clf` [`nodes[9]`]) remain `UNGROUNDED` at the complex level (while subunit `ENZYME` nodes `nodes[0..3, 5..6]` carry `grounding.id` and `protein_examples` and connect via `is subunit of` edges `edges[0..5]`), steps 1, 2, and 4 omit scalar complex `enzyme_id`, and steps 1-4 omit RHEA `reaction_id` due to ComplexPortal/RHEA scope boundaries; and (3) `producer_organisms[1]` (`NCBITaxon:1931`, *Streptomyces* sp., `BGC0002510:1..5`, `MT459140.1:71..11851`, `PMID:32860295`) remains genus-level without strain because `MT459140.1` and `PMID:32860295` are not indexed in ENA/PubMed.
   - **Stage 5 Disposition**: Preserve as an explicit upstream representation/source boundary in Stage 5.

### Carried-Forward Deferred Findings from Cycle 2 Stage 5 (`F-PEN-003`, `F-PIK-DES-003`)

4. **`F-PEN-003` (`carried_from: F-PEN-003`, `status: deferred`, `#1015`)**:
   - Carried forward from `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml`. Note that Cycle 2 Stage 6 (`#1015`) implemented atomic multi-row `REPLACE_SHARED_WITH_CHEBI` in `src/naturalproductmech/curate/structure_corrections.py`, so `F-PEN-003` can be evaluated in Cycle 3 Stage 5 (`resolve_review_findings`) for either data migration or continued boundary disposition.
5. **`F-PIK-DES-003` (`carried_from: F-PIK-DES-003`, `status: deferred`, `#1012`)**:
   - Carried forward from `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml` under open GitHub issue `#1012` (upstream cyclic vs open-chain D-desosamine tautomer split and MIBiG `BGC0000094`/`BGC0000898` deposit partition).
