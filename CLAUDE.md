# CLAUDE.md

Operational guidance for Claude Code and other editing agents in this repository.

**Status (2026-09-07): pre-scaffold.** This repository holds the plan, the
data-source research, the seeded source queue and the skills. There is no
schema, seeder, corpus or QC runner yet; `PLAN.md` §7 says in what order they
arrive. Commands below are the ones the scaffold will provide, named to match
AntibioticMech so the fleet's tooling and habits carry over. Until they exist,
a skill that calls one should say so rather than improvise.

## Repository purpose

NaturalProductMech is a LinkML knowledge base of **individual natural product
structures**: one generated YAML record per Standard InChIKey at
`data/natural_products/<biosynthetic_class>/<slug>.yaml`, harmonized from
ChEBI (3-star entries bearing an allow-listed specialized-metabolite role),
MIBiG (reviewed entries: structures, producers, gene clusters) and LOTUS
(cited occurrences, microbial taxa first), with structures for uncovered
concepts fetched from PubChem. The committed inventories in `data/raw/` are
the reproducible inputs.

Read these before changing domain behavior:

- [PLAN.md](PLAN.md) — scope, schema design, the AntibioticMech join, milestones.
- [README.md](README.md) — public model and generated statistics (once scaffolded).
- [docs/HARMONIZATION.md](docs/HARMONIZATION.md) — identity, merging, scope
  (once scaffolded; `PLAN.md` §2–§4 until then).
- [docs/CURATION.md](docs/CURATION.md) — decision semantics and evidence rules.
- [research/2026-09-07-natural-product-data-sources.md](research/2026-09-07-natural-product-data-sources.md)
  — the verified source landscape.

Sibling repositories use the same conventions: AntibioticMech (the closest
relative, and the template), TraitMech, CultureMech, MediaIngredientMech,
HabitatMech, CommunityMech, CellStructureMech, ProteinTraitsMech. The upstream
pattern is monarch-initiative/dismech. Fleet governance is
CultureBotAI/culturebotai-claw.

## Authoritative commands (scaffold target)

```bash
just qc                # every local and CI quality gate
just report            # corpus, grounding, producer and BGC coverage statistics
just test              # unit and corpus-integrity tests
just validate-all      # closed-schema validation of every record
just verify-corpus     # prove data/natural_products reproduces from its inputs
just worklist          # the curation backlog, ranked
just source-queue      # the ranked data-source queue and what is unverified in it
just render            # regenerate the committed site under pages/
just docs-stats        # refresh the generated README statistics block
```

For an upstream refresh:

```bash
just extract-inventory-dry     # ChEBI
just extract-inventory
just extract-mibig-dry
just extract-mibig
just extract-lotus-dry
just extract-lotus
just extract-pubchem-dry
just extract-pubchem-canary <ID>
just extract-pubchem
just seed
just seed-canary CHEBI:42355   # erythromycin A: exercises the AntibioticMech join
just seed-apply
just seed-apply --prune        # only when stale records should be removed
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

**Edit site templates, not `pages/`.** Change
`src/naturalproductmech/templates/`, run `just render`, commit the regenerated
pages.

**Do not edit `src/naturalproductmech/schema/mech_shared.yaml` or
`history.yaml` here.** They are vendored byte-identically across the Mech
repositories from claw and sha-pinned by the schema tests.

## Safe corpus workflow

**Canary before a bulk write, and before any paid or networked batch.** The
PubChem enrichment and the LOTUS/Wikidata fetch are the networked steps:
dry-run, then one real unit, then read the written row before the batch. Same
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
  never promotes one to the other.
- **Computed is not asserted.** NPClassifier, ClassyFire and NP-likeness carry
  tool and version and never pose as a source assertion.
- **`biosynthetic_class` is a filing decision; `biosynthetic_classes` and
  `ecological_roles` are the evidence.** Never drop a value because the class
  was assigned.
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
