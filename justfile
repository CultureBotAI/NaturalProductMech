# NaturalProductMech — individual natural product chemical structures

set positional-arguments := true

schema := "src/naturalproductmech/schema/naturalproductmech.yaml"
corpus := "data/natural_products"

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
# byte-identical at the pinned ref. It is deliberately not part of `just qc`
# for that reason, and joins it at admission.
vendored-sync:
    bash scripts/check_vendored_sync.sh
