# Stage 5 Validation & Fresh Review Summary (`mech-goal-sequence-20261019`, Cycle 1)

## Validation Gates Executed

| Check ID | Command | Exit Code | Result |
| --- | --- | --- | --- |
| `strict-cohort-post-remediation` | `.venv/bin/python scripts/validate_strict.py --workers 1 --out /tmp/stage5_strict.tsv data/natural_products/carbohydrates/desosamine-2.yaml data/natural_products/carbohydrates/desosamine.yaml data/natural_products/polyketides/methymycin.yaml data/natural_products/polyketides/pikromycin.yaml data/natural_products/polyketides/neomethymycin.yaml data/natural_products/polyketides/narbomycin.yaml` | `0` | 6 cohort YAML files validated with 0 `ERROR` rows. |
| `verify-corpus-post-remediation` | `.venv/bin/python scripts/verify_corpus.py --summary` | `0` | `lockfile integrity OK: 3116 records` against `data/natural_products/PATHS.tsv`. |
| `validate-id-labels-post-remediation` | `.venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/stage5_id_label.tsv` | `0` | `OK_CANONICAL: 13448`, `OK_SYNONYM: 646`, `OK_EXCEPTION: 35`, `MISMATCH: 499`, `ID_NOT_FOUND: 0`. |
| `unit-tests-post-remediation` | `.venv/bin/python -B -m pytest -o cache_dir=/tmp/pytest_cache -q tests/test_producer_strains.py tests/test_claim_references.py tests/test_lotus_exclusions.py tests/test_structure_corrections.py tests/test_seed_skeleton.py` | `0` | `322 passed in 26.37s`. |
| `record-review-check-post-remediation` | `.venv/bin/python scripts/record_review.py check --require-reviews --base main` | `0` | All retained structured review bundles validate cleanly and preserve append-only immutability. |

## Fresh Post-Remediation Structured Review

- **Bundle**: `reviews/structured/20261022T034800Z-pik-des-stage5-remediation-review/review.yaml`
- **Verdict**: `pass_with_limitations` (`completion: completed`, `scientific_review: true`)
- **Dispositions**:
  - `F-PIK-DES-001` (`G-PIK-DES-001`, `#1010`): `resolved`
  - `F-PIK-DES-002` (`G-PIK-DES-002`, `#1011`): `resolved`
  - `F-PIK-DES-003` (`G-PIK-DES-003`, `#1012`): `deferred`
