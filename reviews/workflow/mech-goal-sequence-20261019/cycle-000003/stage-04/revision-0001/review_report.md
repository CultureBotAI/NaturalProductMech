# Workflow Stage 4 Record & Cohort Review Report (Cycle 3, Revision 1)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: `3` / `4` (`record_review`) / `1`
- **Repository**: `CultureBotAI/NaturalProductMech` (`naturalproductmech`)
- **Frozen Source Revision (`HEAD`)**: `d14547bc76e0582aca15eeb073e203d28ea7548e`
- **Previous Review/Remediation Evidence Manifest**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml` (`8b791c06d925b39a701c2f9e0919fe64963bbf92461ac850208539f0efdcd3e5`)
- **Latest Prior Workflow Evidence Manifest (Cycle 2 Stage 6)**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/evidence.yaml` (`af17914a8d3f0028698cef2671d787204fdc4d58174b6fe2cea29c039b4b185d`)
- **Native Review Persistence Bundles**:
  1. Category/Cohort Review (`kind: category`, skill `review-yaml-category`):
     - `reviews/structured/20261025T055000Z-streptomyces-youssoufiensis-youssoufene-cohort/review.yaml` (`d818fb3426e94792c6072e382dbec97f2726afda45bac54c060ee232ad35cca9`)
     - `reviews/structured/20261025T055000Z-streptomyces-youssoufiensis-youssoufene-cohort/review.md` (`63af9a3cf0624d51ccb98acf39b9aa81f4a59de6c6e3a697cab71c78b91a7c94`)
  2. Single-Record Deep Audit (`kind: record`, skill `review-yaml-record`):
     - `reviews/structured/20261025T055005Z-youssoufene-a1-record-review/review.yaml` (`9f4b91356099846108b911750728343e7e95f960a4d54d4b3f83bcfe9e07d62f`)
     - `reviews/structured/20261025T055005Z-youssoufene-a1-record-review/review.md` (`24a4f4ec3ce42f57affef7dab4113d78bb3b348c100309cc1761b5c03908ced5`)

---

## 1. Frozen Inventory & Full-Corpus Gate Summary

At frozen post-Stage-3 commit `d14547bc76e0582aca15eeb073e203d28ea7548e`, the eligible corpus comprises **3,362 YAML records**:
- **3,116** natural product owner records indexed in `data/natural_products/PATHS.tsv` (`sha256: 7b0f3f72d5ebca52abfc04556563b81bb1303f8ef2cb7792917629ebce2e0670`), including `290` owner records with inline `causal_graphs`, `27` owner records with `causal_graph_refs`, and `11` records carrying a historical `REVIEWED` entry in `curation_history`.
- **246** standalone causal graph components under `data/causal_graphs/` (`manifest_sha256: f0db8ac7f96b28947fb53eee86c7e2b4148319cba1742a1a6a75686613972fe7`).

All 3,362 eligible YAML records were audited through deterministic full-corpus validation and worklist gates, paired with deep source-backed cohort and single-record reviews on the newly enriched Cycle 3 *Streptomyces youssoufiensis* (`NCBITaxon:654447`, `mibig:BGC0002547`) / *Streptomyces* sp. (`NCBITaxon:1931`, `mibig:BGC0002510`) youssoufene polyene-bridged benzene-ring cohort (`5` records):

| Checkpoint | Command | Digest (`sha256`) | Summary |
|---|---|---|---|
| Full-corpus verification | `.venv/bin/python scripts/verify_corpus.py --summary` | `c9bcf7add9c5022125581df2e6b486735cd23803e49b73a4a2d6a60b62eebc5e` | `3,116` owner records verified, `0` errors, lockfile integrity OK |
| Ontology ID-label correspondence | `.venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/c3_s4_id_label.tsv` | stdout `35423598d9ea0c53a374976d422665d7bfaf789855b7fd3357b97c7bc356f816`; TSV `fd6b4d6d15cac69220daf9027ac7dcb0a252f509e5bc69d831d181d0d6a6bd6b` | `OK_CANONICAL: 12619`, `OK_SYNONYM: 567`, `OK_EXCEPTION: 35`, `MISMATCH: 499` (warn-only taxon labels), `SKIPPED_NO_ADAPTER: 4898`, exit `0` |
| Standalone causal graph suite | `.venv/bin/pytest -q tests/test_graph_components.py` | `53e35ce114ca8fbf31b29cd0f5c1bac68a5dc6669944111d81e4323f8136b317` | `40 passed` across `246` standalone graph components |
| Curation worklist review queue | `.venv/bin/python scripts/curation_worklist.py --review-records --limit 5` | `2c671a47982350c5968f24b020377eb57b876914d4882d295562790da8f3d330` | `8,922` items across `12` queues (`producer-evidence: 2292`, `biosynthesis: 1184`, `structure-disagreement: 5`, `name-disagreement: 67`, `unnamed-producer: 39`, `shared-structure: 207`, `needs-a-name: 18`, `occurrence-only: 12`, `pathway-ambiguous: 620`, `unresolved-taxa: 3329`, `stereo-incomplete: 1124`, `record-review: 25`) |
| Cohort strict validation | `.venv/bin/python scripts/validate_strict.py data/natural_products/polyketides/youssoufene-a1.yaml data/natural_products/unclassified/youssoufene-b1.yaml data/natural_products/unclassified/youssoufene-b2.yaml data/natural_products/unclassified/youssoufene-b3.yaml data/natural_products/unclassified/youssoufene-b4.yaml` | `590bdeb29003f5b00c5fe407e313812c3bc83e00cd4980060ee32e333dced520` | `5` files scanned, `0` ERROR rows, `120` WARN rows, `15` INFO rows |
| Record strict validation | `.venv/bin/python scripts/validate_strict.py data/natural_products/polyketides/youssoufene-a1.yaml` | `a1421dbacfc9e16ebc794429217734cf62f8eb381d7b099d33457486fd192ef7` | `1` file scanned, `0` ERROR rows, `24` WARN rows, `3` INFO rows |

---

## 2. Deep Cohort & Record Review Targets (Cycle 3 Enriched Youssoufene Cohort)

| Record Path | Identifier | Label | Record `sha256` | MIBiG Source Rows (`sha256`) | Verdict | Highest Finding Severity |
|---|---|---|---|---|---|---|
| `data/natural_products/polyketides/youssoufene-a1.yaml` | `NPATLAS:NPA029448` | youssoufene A1 | `37079438f94fa09545861b4e162e59d2957b24c38e0449fa72d586e8969bbbd3` | `BGC0002510:1` (`2c395dc945037f9028922f784805c83c5c0c988a556fa3d485431886f8ed54bf`), `BGC0002547:1` (`5c7822f950efafabcb17c5dd3dd045bf465548f85f27ed316180eb260853eb56`) | `needs_curation` | `major` |
| `data/natural_products/unclassified/youssoufene-b1.yaml` | `NPATLAS:NPA029449` | youssoufene B1 | `be673d3142661bf64d7f7b3e82b4daaf66e1d3679e8e9472617958b94c5145a9` | `BGC0002510:2` (`a3a30df84f4098f94b63761f87141daecbd28c61c1d59326bb28044e348bf2d9`), `BGC0002547:2` (`fc4484d95a6386510ca70877a8b3453852d367cb04b5f5c52b2a4754ab2bc0f1`) | `needs_curation` | `major` |
| `data/natural_products/unclassified/youssoufene-b2.yaml` | `NPATLAS:NPA029450` | youssoufene B2 | `6ed1efda48d274e53e6372da3abccdf3f15b910d30ebde17d176ab63b81bc7fb` | `BGC0002510:3` (`ca66021e3f161f0e3929acfc653e52a080ba16106687f7c2b0a09a43d2ecdb85`), `BGC0002547:3` (`3f82114b8bd1ce4ca94132a648ebcb5e8c28d967549844ca90e2bc8ef2a9ff64`) | `needs_curation` | `major` |
| `data/natural_products/unclassified/youssoufene-b3.yaml` | `NPATLAS:NPA029451` | youssoufene B3 | `d2db6b397f7c148019450dbca660f47b27262a2ad95e5c7874b686cf92e7af37` | `BGC0002510:4` (`5be1663df3c57503f44483f712f2e0f6d083135ec73ce18e2b215ab14046d910`), `BGC0002547:4` (`ff23718d3540a5713726c8c30f3d442343892df03be1d91a03571a7ec1c8f9fa`) | `needs_curation` | `major` |
| `data/natural_products/unclassified/youssoufene-b4.yaml` | `NPATLAS:NPA029452` | youssoufene B4 | `4b0542c8abbb31b467910035bcfe060d20e75a16a9f3e78a53d09369d6336bc0` | `BGC0002510:5` (`ec2076f98bc4e76fa30e0470c7f232100a2d2f44d8f5d1527c225a198395df42`), `BGC0002547:5` (`09f341de2bd45dc8b57f375890f45646f218c6e0d2e4d3a68dd491deef45d442`) | `needs_curation` | `major` |

---

## 3. Stable Stage 4 Findings & Carried-Forward Findings

### New Open Findings from Cycle 3 Stage 4 (`F-YSF-001`, `F-YSF-002`, `F-YSF-003`)

1. **`F-YSF-001` (`completeness`, `major`, `open`) — Missing `OUC6819` producer strain qualifications on *Streptomyces youssoufiensis* (`NCBITaxon:654447`, `BGC0002547:1..5`) across all 5 youssoufene records**:
   - All five records (`youssoufene-a1.yaml`, `youssoufene-b1.yaml`, `youssoufene-b2.yaml`, `youssoufene-b3.yaml`, `youssoufene-b4.yaml`) omit `producer_organisms[0].strain` because MIBiG 4.0 `BGC0002547` (`genbank:MN844187.1`, `1..25525`) records species-level `organism_name: Streptomyces youssoufiensis` (`NCBITaxon:654447`). Both primary publications — Li et al., *Org. Lett.* 2020;22(2):704-708 (`PMID:31891272`, `DOI:10.1021/acs.orglett.9b04559`) and Liu et al., *Angew. Chem. Int. Ed.* 2021;60(1):153-158 (`PMID:33155752`, `DOI:10.1002/anie.202007777`) — as well as all 11 UniProtKB entries from `MN844187.1` explicitly identify the sequenced producer strain as *Streptomyces youssoufiensis* `OUC6819` (while `inline causal_graphs[0].organisms[0]` already sets `strain: OUC6819`).
   - **Stage 5 Remediation**: Add 5 source-pinned rows (`BGC0002547:1..5`) to `curation/mibig_producer_strains.tsv` with `strain=OUC6819` and `reference=PMID:31891272` and re-seed via `scripts/seed_from_sources.py`.

2. **`F-YSF-002` (`provenance`, `major`, `open`) — Misattributed author citation (`"Deng et al."` instead of `"Liu et al."`) in 80 `DOI:10.1002/anie.202007777` evidence notes across all 5 youssoufene records**:
   - Across all 5 youssoufene records, every `biosynthetic_pathway[0..3].evidence[0].notes` (`4` per record) and every `causal_graphs[0].edges[0..11].evidence[0].notes` (`12` per record) citing `DOI:10.1002/anie.202007777` (`16` notes per record; `80` notes total) attributes `DOI:10.1002/anie.202007777` (*Angew. Chem. Int. Ed.* 2021;60(1):153-158, `PMID:33155752`) to `"Deng et al."`. PubMed (`PMID:33155752`) and Crossref (`DOI:10.1002/anie.202007777`) confirm the authors of `DOI:10.1002/anie.202007777` are Zengzhi Liu, Jing Liu, Tingting Li, Huayue Li, Zirong Liu, Yiqian Dong, and Wenli Li (`"Liu et al."`); Zhaoxian Deng was a co-author on the 2020 *Org. Lett.* paper (`PMID:31891272`, `DOI:10.1021/acs.orglett.9b04559`), not on `DOI:10.1002/anie.202007777`.
   - **Stage 5 Remediation**: Replace `"Deng et al. (Angew. Chem. Int. Ed. 2021, DOI:10.1002/anie.202007777)"` with `"Liu et al. (Angew. Chem. Int. Ed. 2021, PMID:33155752, DOI:10.1002/anie.202007777)"` across all 80 curator-owned evidence notes on the 5 records and regenerate HTML pages.

3. **`F-YSF-003` (`representation`, `minor`, `open`) — Upstream NPClassifier split, `PROTEIN_COMPLEX` / `RHEA` grounding boundaries, and unindexed `BGC0002510` deposit metadata (`MT459140.1` / `PMID:32860295`)**:
   - (1) NPClassifier (`npclassifier.gnps2.org@2026-09-07`) classifies dimeric `youssoufene-a1.yaml` under `POLYKETIDES` (`Polyphenyl polyketides`) while returning empty `pathway_results: []` (`UNCLASSIFIED`) for monomeric `youssoufene-b1.yaml` through `youssoufene-b4.yaml`; (2) heterodimeric KS/CLF `PROTEIN_COMPLEX` nodes (`ysfbc_ks_clf`, `ysfde_ks_clf`, `ysfjk_ks_clf`) remain `UNGROUNDED` at the complex level (with subunit proteins grounded via `protein_examples`) and omit scalar `enzyme_id` on `biosynthetic_pathway` steps 1-2 due to ComplexPortal/RHEA scope boundaries; and (3) `producer_organisms[1]` (`NCBITaxon:1931`, *Streptomyces* sp., `BGC0002510:1..5`, `MT459140.1`, `PMID:32860295`) remains genus-level without strain because `MT459140.1` and `PMID:32860295` are not indexed in ENA/PubMed.
   - **Stage 5 Disposition**: Preserve as an explicit upstream representation/source boundary in Stage 5.

### Carried-Forward Deferred Findings from Cycle 2 Stage 5 (`F-PEN-003`, `F-PIK-DES-003`)

4. **`F-PEN-003` (`carried_from: F-PEN-003`, `status: deferred`, `#1015`)**:
   - Carried forward from `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml`. Note that Cycle 2 Stage 6 (`#1015`) implemented atomic multi-row `REPLACE_SHARED_WITH_CHEBI` in `src/naturalproductmech/curate/structure_corrections.py`, so `F-PEN-003` can be evaluated in Cycle 3 Stage 5 (`resolve_review_findings`) for either data migration or continued boundary disposition.
5. **`F-PIK-DES-003` (`carried_from: F-PIK-DES-003`, `status: deferred`, `#1012`)**:
   - Carried forward from `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml` under open GitHub issue `#1012` (upstream cyclic vs open-chain D-desosamine tautomer split and MIBiG `BGC0000094`/`BGC0000898` deposit partition).
