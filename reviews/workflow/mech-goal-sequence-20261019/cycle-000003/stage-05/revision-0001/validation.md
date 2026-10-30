# Stage 5 Validation & Fresh Review Summary (`mech-goal-sequence-20261019`, Cycle 3)

## Validation Gates Executed

| Check ID | Command | Exit Code | Result |
| --- | --- | --- | --- |
| `strict-cohort-post-remediation` | `.venv/bin/python scripts/validate_strict.py --workers 1 --out /tmp/stage5_c3_strict.tsv data/natural_products/polyketides/youssoufene-a1.yaml data/natural_products/unclassified/youssoufene-b1.yaml data/natural_products/unclassified/youssoufene-b2.yaml data/natural_products/unclassified/youssoufene-b3.yaml data/natural_products/unclassified/youssoufene-b4.yaml` | `0` | 5 cohort YAML files validated with 0 `ERROR` rows. |
| `verify-corpus-post-remediation` | `.venv/bin/python scripts/verify_corpus.py --summary` | `0` | `lockfile integrity OK: 3116 records, each filed where PATHS.tsv pins it`. |
| `validate-id-labels-post-remediation` | `.venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/stage5_c3_id_label.tsv` | `0` | `OK_CANONICAL: 13472`, `OK_SYNONYM: 657`, `OK_EXCEPTION: 35`, `MISMATCH: 499`, `ID_NOT_FOUND: 0`, `SKIPPED_NO_ADAPTER: 4898` (`0` flagged pairs on cohort records). |
| `unit-tests-post-remediation` | `.venv/bin/python -B -m pytest -o cache_dir=/tmp/pytest_cache -q tests/test_producer_strains.py tests/test_claim_references.py tests/test_lotus_exclusions.py tests/test_structure_corrections.py tests/test_seed_skeleton.py tests/test_graph_components.py` | `0` | `380 passed in 137.66s`. |
| `check-docs-post-remediation` | `.venv/bin/python scripts/check_docs.py` | `0` | `README statistics block is current`. |
| `check-reproduction-post-remediation` | `.venv/bin/python scripts/check_reproduction.py` | `0` | `corpus reproduction OK: 3116 records are byte-identical to what the seeder builds from data/raw/`. |
| `render-pages-post-remediation` | `.venv/bin/python scripts/render_pages.py --check` | `0` | `pages/ is in step with the corpus` (`3116` record pages across `8` pathways). |
| `record-review-check-post-remediation` | `.venv/bin/python scripts/record_review.py check --require-reviews --base main` | `0` | `102` valid structured review bundles verified; append-only immutability preserved. |

## Fresh Post-Remediation Structured Review

- **Bundle**: `reviews/structured/20261030T045500Z-streptomyces-youssoufiensis-stage5-remediation-review/review.yaml`
- **Verdict**: `pass_with_limitations` (`completion: completed`, `scientific_review: true`)
- **Dispositions**:
  - `F-YSF-001` (`G-YSF-001`, `#1044`): `resolved`
  - `F-YSF-002` (`G-YSF-002`, `#1045`): `resolved`
  - `F-YSF-003` (`G-YSF-003`, `#1046`): `deferred`
  - `F-PEN-003` (`G-PEN-003`, `#1047` / `naturalproductmech-infra-0003`): `deferred` (carried forward from Cycle 2 Stage 5)
  - `F-PIK-DES-003` (`G-PIK-DES-003`, `#1012`): `deferred` (carried forward from Cycle 1 Stage 5)
