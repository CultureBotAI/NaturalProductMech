# NaturalProductMech — individual natural product chemical structures

set positional-arguments := true

schema := "src/naturalproductmech/schema/naturalproductmech.yaml"
corpus := "data/natural_products"

# Shared tooling from a culturebotai-claw checkout. Only new-history reaches
# it; everything else here uses the vendored copies and needs no claw at all.
# Set CLAW_SRC to override the sibling-checkout default.
claw_src := env_var_or_default("CLAW_SRC", "../culturebotai-claw/src")

_require-claw module:
    #!/usr/bin/env bash
    set -euo pipefail
    if [ ! -d "{{claw_src}}/{{module}}" ]; then
      echo "error: shared module '{{module}}' not found under '{{claw_src}}'." >&2
      echo "Set CLAW_SRC to the src/ directory of a culturebotai-claw checkout." >&2
      exit 1
    fi

default:
    @just --list --unsorted

# Install package + dev tools
install:
    uv sync --locked --extra dev --extra chemistry

# Generate Pydantic classes from the LinkML schema
gen-schema:
    uv run gen-pydantic {{schema}} > src/naturalproductmech/schema/naturalproductmech_dataclasses.py

# --- extraction (networked; canary before any batch) -------------------------
# Free check: parse the cached MIBiG release and report counts, writing nothing.
extract-mibig-dry *args:
    uv run python scripts/extract_mibig.py --dry-run {{args}}

# Write data/raw/mibig_compounds.tsv from the MIBiG release.
extract-mibig *args:
    uv run python scripts/extract_mibig.py {{args}}

# Free check: how many classifier calls the batch would make. Sends nothing.
extract-npclassifier-dry:
    uv run python scripts/extract_npclassifier.py --dry-run

# ONE real classifier call, then stop. Read the written row before the batch.
extract-npclassifier-canary:
    uv run python scripts/extract_npclassifier.py --canary

# Classify every unclassified structure. Resumable: writes as it goes and skips
# keys already in the inventory, so an interruption costs one chunk.
extract-npclassifier *args:
    uv run python scripts/extract_npclassifier.py {{args}}

# Free check: parse the cached ChEBI flat files and report counts.
extract-chebi-dry *args:
    uv run python scripts/extract_chebi.py --dry-run {{args}}

# Write chebi_structures.tsv (grounding) and chebi_origins.tsv (occurrences).
extract-chebi *args:
    uv run python scripts/extract_chebi.py {{args}}

# Free check: what the sibling pin would emit, from the checkout, writing nothing.
extract-antibioticmech-dry *args:
    uv run python scripts/extract_antibioticmech.py --dry-run {{args}}

# Pin the sibling corpus's structures so cross-corpus links reproduce offline.
extract-antibioticmech *args:
    uv run python scripts/extract_antibioticmech.py {{args}}

# Free check once cached: how many LOTUS triples touch corpus structures.
extract-lotus-dry *args:
    uv run python scripts/extract_lotus.py --dry-run {{args}}

# Write lotus_occurrences.tsv from the pinned Zenodo frozen export.
extract-lotus *args:
    uv run python scripts/extract_lotus.py {{args}}

# Free check once cached: BindingDB rows touching corpus structures.
extract-bindingdb-dry *args:
    uv run python scripts/extract_bindingdb.py --dry-run {{args}}

# Write bindingdb_targets.tsv from the own-curated articles file only.
extract-bindingdb *args:
    uv run python scripts/extract_bindingdb.py {{args}}

# Free check once cached: CyanoMetDB rows touching corpus structures.
extract-cyanometdb-dry *args:
    uv run python scripts/extract_cyanometdb.py --dry-run {{args}}

# Write cyanometdb_occurrences.tsv, species-level taxon resolution only.
extract-cyanometdb *args:
    uv run python scripts/extract_cyanometdb.py {{args}}

# Measure what NPASS would add, without redistributing any of it. Writes a
# report, never an inventory: NPASS states no licence, so the gate stays shut.
evaluate-npass:
    uv run python scripts/evaluate_npass.py

# Free check once cached: how many unresolved names NCBI Taxonomy would resolve.
extract-taxonomy-dry *args:
    uv run python scripts/extract_ncbi_taxonomy.py --dry-run {{args}}

# Write taxon_names.tsv. Run BEFORE the ChEBI, LOTUS and CyanoMetDB extractors,
# which consult it to resolve organisms their own sources leave unidentified.
extract-taxonomy *args:
    uv run python scripts/extract_ncbi_taxonomy.py {{args}}

# Free check: how many PubChem CID calls the batch would make.
extract-bioassay-dry:
    uv run python scripts/extract_pubchem_bioassay.py --dry-run

# ONE real call, then stop. Read the written rows before the batch.
extract-bioassay-canary:
    uv run python scripts/extract_pubchem_bioassay.py --canary

# Query every cross-referenced CID. Resumable; excludes ChEMBL deposits.
extract-bioassay *args:
    uv run python scripts/extract_pubchem_bioassay.py {{args}}

# --- seeding -----------------------------------------------------------------
# Dry run: harmonize the committed inventories and report the records that WOULD
# be written, per pathway. No files touched. Empty until M2 adds the extractors.
seed:
    uv run python scripts/seed_from_sources.py

# Seed exactly one record end to end and validate it — the canary before any
# bulk write. `just seed-canary CHEBI:42355` (erythromycin A, which also
# exercises the AntibioticMech cross-corpus join).
seed-canary *args:
    uv run python scripts/seed_from_sources.py --apply --only "$@"

# Write every record under data/natural_products/<np_pathway>/<slug>.yaml.
# Run `just seed` and `just seed-canary` first.
seed-apply *args:
    uv run python scripts/seed_from_sources.py --apply {{args}}

# --- validation --------------------------------------------------------------
# Validate a single record against the schema
validate file:
    uv run linkml-validate -s {{schema}} --target-class NaturalProductRecord {{file}}

# Validate every record. Delegates to validate-strict (closed mode: unknown
# fields are errors, not silently accepted as in linkml-validate's open mode).
validate-all *args:
    @just validate-strict {{args}}

# Strict in-process validation in closed mode.
validate-strict *args:
    uv run python scripts/validate_strict.py {{args}}

# Verify data/natural_products/ is exactly what data/raw/ produces. Schema
# validation checks each record's shape but not its content; without this a
# hand-edited or drifted record passes every other check.
verify-corpus *args:
    uv run python scripts/verify_corpus.py {{args}}

# Verify every committed inventory is covered by MANIFEST.yaml and matches it
provenance-check:
    uv run python scripts/check_provenance.py

# Blocking id<->label gate (validator vendored from claw): every configured
# (id, label) pair under data/natural_products/ must correspond to the ontology
# through OAK. Runs in its own workflow, not in `just qc`: it needs a cached
# multi-GB ontology download. Targets, skipped prefixes and the reasons for
# each live in conf/id_label_targets.yaml.
validate-products:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

# The same check written to reports/label_drift.tsv without failing, so a red
# build still ships the list it was red about.
report-label-drift:
    mkdir -p reports
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml --report reports/label_drift.tsv

# Prove every record is byte-identical to what the seeder builds from data/raw/.
# Curator-owned fields are taken from the file, exactly as the writer takes them.
verify-reproduction *args:
    uv run python scripts/check_reproduction.py {{args}}

# The vendored contract in src/naturalproductmech/schema/history.yaml says not
# to hand-write a curation-history record: "Scaffold with `just new-history`,
# which guarantees a schema-valid skeleton and a collision-free name, then edit
# the `details` field" (#57). The scaffolder lives in claw, so this needs a
# checkout, and the guard says so rather than failing as an unknown recipe.
# "$@" not {{args}}: see `set positional-arguments`.
#
# Scaffold an append-only curation-history record (needs a claw checkout).
new-history *args: (_require-claw "kg_microbe_history")
    #!/usr/bin/env bash
    set -euo pipefail
    PYTHONPATH="{{claw_src}}" uv run python -m kg_microbe_history new "$@"

# The curation backlog by queue, ranked. Derived from the committed tree, so a
# row leaves a queue when the thing that put it there changes.
worklist *args:
    uv run python scripts/curation_worklist.py {{args}}

# The exhaustive per-record checkpoint `curate-yaml-record` works from.
review-queue *args:
    uv run python scripts/curation_worklist.py --limit 0 {{args}}

# Show the documents that WOULD be embedded, and their size distribution. Free.
embed-dry:
    python3 scripts/embed_records.py --dry-run

# Embed ONE small batch end to end — the canary before the full run.
embed-canary *args:
    python3 scripts/embed_records.py --limit 20 {{args}}

# Text-embed every record with a local model. Runs on system python so torch
# stays out of the core install; ~1 min for the corpus on Apple-Silicon MPS.
# Writes data/embeddings/ (vectors gitignored, rebuildable).
embed *args:
    python3 scripts/embed_records.py {{args}}

# Project the embeddings to 2-D -> data/embeddings/corpus_map.json (committed).
# Run `just render` afterwards to rebuild pages/map.html from it.
embed-map *args:
    python3 scripts/embed_map.py {{args}}

# Recompute the structure-only chemical embedding, then publish it. Needs the
# chemical-map extra (RDKit, UMAP); `just render` alone does not.
chemical-map:
    uv run --extra chemical-map python scripts/generate_chemical_map.py
    uv run python scripts/render_pages.py

# Deterministic staleness, coverage and scientific-quality check on the
# committed artifact. No recompute, so it is cheap enough for the gate.
chemical-map-check:
    uv run --extra chemical-map python scripts/generate_chemical_map.py --check

# The expensive audit: rerun fingerprints, distances and UMAP and compare.
chemical-map-recompute-check:
    uv run --extra chemical-map python scripts/generate_chemical_map.py --check --recompute

# Regenerate the committed site under pages/ from the corpus.
render *args:
    uv run python scripts/render_pages.py {{args}}

# Fail if pages/ is out of step with the corpus. In the gate, because a
# committed site goes stale exactly as a committed record could.
render-check:
    uv run python scripts/render_pages.py --check

# --- reporting ---------------------------------------------------------------
# Corpus report: records per pathway, grounding, and origin-evidence coverage,
# with producer claims split into causal and correlational.
report *args:
    uv run python scripts/np_report.py {{args}}

# The prioritized data-source queue: what to adopt next, and what is still
# unverified about it. `.claude/skills/source-queue` triages it.
source-queue:
    uv run python scripts/check_source_queue.py

# Refresh the generated current-corpus block in README.md
docs-stats:
    uv run python scripts/check_docs.py --write

# Fail if README.md's current-corpus block is out of step with the corpus
docs-check:
    uv run python scripts/check_docs.py --check

# --- quality -----------------------------------------------------------------
# Run the test suite
test *args:
    uv run pytest {{args}}

# Lint
lint *args:
    uv run ruff check {{args}} .

# Auto-fix lint findings
lint-fix:
    uv run ruff check --fix .

# The authoritative quality gate used both locally and in CI.
qc:
    uv run python scripts/run_qc.py

# Check the claw-governed vendored files against canon.
#
# EXPECTED TO FAIL until M4: the checker resolves this repository's identity
# through claw's consumer registry, and NaturalProductMech is not admitted to
# the fleet manifest yet (PLAN.md section 7). The files themselves ARE vendored
# byte-identical at the pinned ref. Part of `just qc` since admission
# (culturebotai-claw#395); kept as its own recipe for a quick local run.
vendored-sync:
    bash scripts/check_vendored_sync.sh
