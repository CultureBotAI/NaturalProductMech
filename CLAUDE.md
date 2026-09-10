# CLAUDE.md

Operational guidance for Claude Code and other editing agents in this repository.

**Status (2026-09-09): seeded, 3,115 records, curation not started.** Nine
sources are adopted and every record reproduces offline from the committed
inventories in `data/raw/` (`just verify-corpus`). `producer_organisms` and
`biosynthetic_gene_clusters` are on every record; `occurrences` on 2,342;
`bioactivities` and `molecular_targets` are sparse; `biosynthetic_pathway` and
`causal_graphs` are empty because M6 has not begun. Two things this file once
listed as commands do not exist: the curation worklist (#52) and the site
renderer (#53). They are owed in `NEXT_TASKS.md`, not named below as available.

One gate is deliberately outside `just qc`: `just vendored-sync`. Its checker
resolves this repository's identity through claw's consumer registry, and
NaturalProductMech is not admitted to the fleet manifest until M4. The governed
files ARE vendored byte-identical at the pinned ref, so the failure is on
identity, not content. Admission adds it to the gate. Until then
`tests/test_vendored_artifacts.py` is the drift guard: it compares every
fleet-wide artifact, bytes and mode, against `scripts/.vendored_manifest.json`,
claw's manifest snapshotted at the pin. A re-pin is three things in one PR:
advance `scripts/.vendored_canon_ref`, re-snapshot the manifest, re-vendor any
artifact whose hash moved.

## Repository purpose

NaturalProductMech is a LinkML knowledge base of **individual natural product
structures**: one generated YAML record per Standard InChIKey at
`data/natural_products/<np_pathway>/<slug>.yaml`, harmonized from
ChEBI (3-star entries bearing an allow-listed specialized-metabolite role),
MIBiG (active entries: structures, producers, gene clusters, graded by each
locus's experimental evidence) and LOTUS (cited occurrences, microbial taxa
first), with structures for uncovered concepts fetched from PubChem and the
filing classification computed by NPClassifier. The committed inventories in
`data/raw/` are the reproducible inputs.

Read these before changing domain behavior:

- [PLAN.md](PLAN.md) — scope, schema design, the AntibioticMech join, milestones.
- [README.md](README.md) — public model and generated statistics.
- [docs/HARMONIZATION.md](docs/HARMONIZATION.md) — identity, merging, scope,
  the producer/occurrence rule, the filing pathway.
- [docs/CURATION.md](docs/CURATION.md) — decision semantics and evidence rules.
- [NEXT_TASKS.md](NEXT_TASKS.md) — owed work, by issue.
- [research/2026-09-07-natural-product-data-sources.md](research/2026-09-07-natural-product-data-sources.md)
  — the verified source landscape.

Sibling repositories use the same conventions: AntibioticMech (the closest
relative, and the template), TraitMech, CultureMech, MediaIngredientMech,
HabitatMech, CommunityMech, CellStructureMech, ProteinTraitsMech. The upstream
pattern is monarch-initiative/dismech. Fleet governance is
CultureBotAI/culturebotai-claw.

## Authoritative commands

```bash
just qc                # every local and CI quality gate
just report            # corpus, grounding, producer and BGC coverage statistics
just test              # unit and corpus-integrity tests
just validate-all      # closed-schema validation of every record
just verify-corpus     # prove data/natural_products reproduces from its inputs
just provenance-check  # every committed inventory matches MANIFEST.yaml
just source-queue      # the ranked data-source queue and what is unverified in it
just docs-stats        # refresh the generated README statistics block
```

Not available, and not to be run expecting output: `just worklist` (#52),
`just render` / `just render-check` / `just chemical-map` (#53).

For an upstream refresh, every source has a free `-dry` run and a writing run;
the two networked batches also have a one-call `-canary`. MIBiG is the anchor
and runs first.

```bash
just extract-mibig-dry          just extract-mibig
just extract-chebi-dry          just extract-chebi
just extract-lotus-dry          just extract-lotus
just extract-cyanometdb-dry     just extract-cyanometdb
just extract-taxonomy-dry       just extract-taxonomy
just extract-npclassifier-dry   just extract-npclassifier-canary   just extract-npclassifier
just extract-bioassay-dry       just extract-bioassay-canary       just extract-bioassay
just extract-bindingdb-dry      just extract-bindingdb
just extract-antibioticmech     # refresh the pinned sibling inventory; --advance-pin to move it
just seed                       # dry run: what would be written, per pathway
just seed-canary <IDENTIFIER>   # one record — the `identifier` column of PATHS.tsv — then read it
just seed-apply
just seed-apply --prune         # only when stale records should be removed
```

## Generated-file boundaries

**Never hand-edit a record.** `data/natural_products/` is generated from the
committed inventories plus curation decisions. Put source harmonization changes
in the extractor or seeder, and curator decisions in `curation/decisions.tsv`.
`just verify-corpus` rejects drift.

**Never write a record except through `write_validated_natural_product`.** It
runs closed-schema validation before writing. Every mutation must also append a
`CurationEvent` via `naturalproductmech.curate.curation_event.record_curation_event`.

**Re-emitting an unchanged record must be byte-identical.** Preserve the YAML
emission contract enforced by `tests/test_write_validated.py`.

**There is no site yet.** `src/naturalproductmech/templates/` is empty and
`pages/` does not exist (#53). When the renderer lands the rule is
AntibioticMech's: edit templates, run `just render`, commit the regenerated
pages, never hand-edit `pages/`.

**Do not edit `src/naturalproductmech/schema/mech_shared.yaml` or
`history.yaml` here.** They are vendored byte-identically across the Mech
repositories from claw and sha-pinned by the schema tests.

## Safe corpus workflow

**Canary before a bulk write, and before any paid or networked batch.** The
NPClassifier and PubChem BioAssay batches are the networked steps, one call per
structure: dry-run, then one real unit, then read the written row before the
batch. Same
for seeding: `just seed`, `just seed-canary <IDENTIFIER>`, read the file, then
`just seed-apply`.

**The corpus has a size budget.** `conf/sources.yaml` declares
`producer_scope` (the taxon filter) and a record budget; `just seed` refuses to
exceed the budget without an explicit flag. Widening scope is a recorded
decision in a PR, not a side effect of a refresh.

**Never rename a record file directly.** Change the identifier-to-slug row in
`data/natural_products/PATHS.tsv` and re-seed.

**Do not prune on a partial run.** `--prune` with `--only` or `--limit` is
refused.

**The environment is pinned.** `uv.lock` is committed and both `just install`
and CI sync `--locked`, so a lock out of step with `pyproject.toml` fails
instead of being re-resolved. After changing a dependency, run `uv lock` and
commit the lockfile in the same PR; `verify-corpus` only proves reproduction
under the environment the lock names.

**Treat extractor drift as evidence to inspect.** `data/raw/MANIFEST.yaml`
records the sha256 of every upstream file and every emitted inventory.
`just provenance-check` after any change to `data/raw/`.

## Skills

`.claude/skills/` carries four repository-specific workflows, adapted from
AntibioticMech's:

- **`add-natural-product`** — prove a named compound, MIBiG entry or
  publication lead is one new structure with an asserted biological origin,
  then add the reproducible source path that emits its first record.
- **`review-open-issues`** — sweep and rank the whole open-issue queue against
  the committed corpus. Its P0 tier is "wrong in a way every gate passes",
  and in this corpus that means above all an occurrence written as production
  or a computed class presented as asserted.
- **`source-queue`** — triage `curation/source_queue.tsv`, the ranked list of
  data sources this corpus might adopt, with the producer-versus-occurrence
  gate added to the licence gate.
- **`curate-yaml-record`** — review and, when explicitly asked, improve one
  record by checking identity, stereochemistry, producer evidence, BGC entries
  and bioactivity claims. Writes only through the validated curation-event path.

None of the skills sends messages or mutates GitHub without explicit
authorization.

## Adopting a data source

Candidates live in `curation/source_queue.tsv`, ranked by the corpus gap they
close. The checker enforces: a source cannot be ADOPTED while its redistribution
terms are UNVERIFIED; a source with RESTRICTED, SHARE_ALIKE or NON_COMMERCIAL
terms cannot be seeded; a `compound → taxon` source must declare whether it
fills `producer_organisms` or `occurrences`. Adoption is a pull request that
adds the extractor path, the committed inventory, its manifest entry and its
`ATTRIBUTION.md` paragraph. The `source-queue` skill triages.

## Semantic invariants

- **A record is a structure.** No InChIKey, no record.
- **A record is admitted by an origin assertion**, never by a computed
  natural-product-likeness or structural resemblance.
- **A compound class, extract, fraction or preparation is never a record.**
- **Occurrence is not production.** `producer_organisms` requires
  biosynthesis-grade evidence; `occurrences` requires a citation; the seeder
  never promotes one to the other. Within `producer_organisms`,
  `BGC_CORRELATED` is not `BGC_CHARACTERIZED`: correlation between expression
  and production is a weaker claim than a knockout, and it stays marked as one.
- **The filing pathway is pinned, not recomputed.** `np_pathway` comes from a
  committed, version-pinned NPClassifier inventory and is locked per record in
  `PATHS.tsv`. A newer model that disagrees is to produce a `pathway-drift`
  worklist entry for a curator, never a silent directory move. The pin is
  enforced by `just verify-corpus`; the comparison and its queue are owed
  (#43, #52) — today a disagreement is silent.
- **Computed is not asserted.** NPClassifier, ClassyFire and NP-likeness carry
  tool and version and never pose as a source assertion.
- **`np_pathway` is a filing decision, and it is computed.** It is
  NPClassifier's pathway, so it says which model version produced it. The
  asserted classifications live beside it in `bgc_class` (the gene cluster's,
  from MIBiG), `compound_classes` (the molecule's, where a source asserts one)
  and `ecological_roles`. Never drop a value because the filing class was
  assigned, and never present the filing class as an assertion.
- **Merge on InChIKey, with two exceptions** (ChEBI-internal collisions stay
  separate; two minted concepts sharing a structure are flagged, not merged).
  `stereo_complete` is recorded because this chemistry is where the InChIKey's
  limits bite.
- **Antimicrobial mechanism lives in AntibioticMech.** The join is a
  seeder-computed `related_records` link from a pinned inventory, never a copy.
- **Mechanism, producer, occurrence, BGC and activity claims require evidence;
  classification does not.**
- **A database assertion cites the database and says so.**
- **A value without units and method is not a measurement.**
- **`parent_compounds` means strictly broader**; `congener_of` means sibling;
  an xref means the same structure.

## Git workflow

Branch before the first edit. Open a PR for every change, including docs-only
changes. Review the diff as a separate adversarial pass and file findings as
issues. Do not merge without explicit approval. Delete branches after merge.
