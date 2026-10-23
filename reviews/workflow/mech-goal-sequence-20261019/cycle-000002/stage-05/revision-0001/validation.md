# Stage 5 Validation & Fresh Review Summary (`mech-goal-sequence-20261019`, Cycle 2)

## Validation Gates Executed

| Check ID | Command | Exit Code | Result |
| --- | --- | --- | --- |
| `strict-cohort-post-remediation` | `.venv/bin/python scripts/validate_strict.py --workers 1 --out /tmp/stage5_c2_strict.tsv data/natural_products/amino_acids_and_peptides/n-5s-5-ammonio-5-carboxylatopentanoyl-l-cysteinyl-d-valinate.yaml data/natural_products/amino_acids_and_peptides/isopenicillin-n.yaml data/natural_products/amino_acids_and_peptides/benzylpenicillin-sodium.yaml` | `0` | 3 cohort YAML files validated with 0 `ERROR` rows. |
| `verify-corpus-post-remediation` | `.venv/bin/python scripts/verify_corpus.py --summary` | `0` | `lockfile integrity OK: 3116 records` against `data/natural_products/PATHS.tsv`. |
| `validate-id-labels-post-remediation` | `.venv/bin/python scripts/validate_id_label_correspondence.py --report /tmp/stage5_c2_id_label.tsv` | `0` | `OK_CANONICAL: 13465`, `OK_SYNONYM: 655`, `OK_EXCEPTION: 35`, `MISMATCH: 499`, `ID_NOT_FOUND: 0` (`0` flagged pairs on cohort records). |
| `unit-tests-post-remediation` | `.venv/bin/python -B -m pytest -o cache_dir=/tmp/pytest_cache -q tests/test_producer_strains.py tests/test_claim_references.py tests/test_lotus_exclusions.py tests/test_structure_corrections.py tests/test_seed_skeleton.py` | `0` | `330 passed in 27.07s`. |
| `check-docs-post-remediation` | `.venv/bin/python scripts/check_docs.py` | `0` | `README statistics block is current`. |
| `check-reproduction-post-remediation` | `.venv/bin/python scripts/check_reproduction.py --summary` | `0` | `corpus reproduction OK: 3116 records match data/raw/`. |
| `render-pages-post-remediation` | `.venv/bin/python scripts/render_pages.py --check` | `0` | `pages/ is in step with the corpus` (`3116` record pages across `8` pathways). |
| `record-review-check-post-remediation` | `.venv/bin/python scripts/record_review.py check --require-reviews --base main` | `0` | `99` valid structured review bundles verified; append-only immutability preserved. |

## Fresh Post-Remediation Structured Review

- **Bundle**: `reviews/structured/20261023T144300Z-penicillium-chrysogenum-stage5-remediation-review/review.yaml`
- **Verdict**: `pass_with_limitations` (`completion: completed`, `scientific_review: true`)
- **Dispositions**:
  - `F-PEN-001` (`G-PEN-001`, `#1022`): `resolved`
  - `F-PEN-002` (`G-PEN-002`, `#1023`): `resolved`
  - `F-PEN-003` (`G-PEN-003`, `#1015`): `deferred`
  - `F-PIK-DES-003` (`G-PIK-DES-003`, `#1012`): `deferred` (carried forward from Cycle 1 Stage 5)
