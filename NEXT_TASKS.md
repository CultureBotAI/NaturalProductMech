# Next tasks

Owed work, by issue. This is the ledger `PLAN.md` §6 and the skills point at:
what the repository has committed to and not yet delivered. An item leaves this
file when its issue closes, not before. The issue carries the evidence and the
discussion; this file carries the order.

Milestones are in `PLAN.md` §7. M0–M3 and M5 have landed; M4 and M6 have not.

## Claims the code does not yet deliver

Documentation was ported from AntibioticMech ahead of the code. These are the
pieces named as available that were never built.

- **#52 — `just worklist` and `just review-queue`.** The curation backlog by
  queue. Named in `CLAUDE.md`, `PLAN.md` §3.4 and §7, `docs/CURATION.md` and two
  skills. Unblocks #43 and the `curate-yaml-record` skill's checkpoint.
- **#43 — `pathway-drift` detection.** The pin half of issue #2 is enforced by
  `just verify-corpus`; the comparison of `PATHS.tsv` against a newer
  NPClassifier inventory is not implemented, so a model upgrade disagrees
  silently. Needs #52 for somewhere to land, or a report of its own.
- **#53 — the browsable site.** Renderer, templates, `pages/`, `render-check`
  in the gate, Pages deploy. When the URL returns 200, restore the repository
  `homepage` field cleared in #46 — not before.

## Gates that do not yet guard

- **#64 — NCBITaxon labels are skipped by the id-label gate.** The corpus's
  largest (id, label) surface, about 13,700 pairs; OAK's adapter is 13.5 GB
  and cannot be cached in CI. Derive a corpus-scoped adapter from `names.dmp`
  in `extract_ncbi_taxonomy.py` and point the config at it. A local run
  already found 123 distinct mismatching pairs and 58 unknown ids (#62, #63).
- **#57 — `just new-history` does not exist.** The vendored curation-history
  contract names it; TraitMech and HabitatMech have it. Port the fleet's
  recipe rather than invent one. Nothing to scaffold until M6 starts.

## Fleet

- **M4 — admission to claw.** Three PRs in claw's order (`PLAN.md` §7).
  Until then `just vendored-sync` fails on identity, by design. No issue yet.
- **Claw pin.** `scripts/.vendored_canon_ref` follows what the other eight
  members pin (`eeccfebe23`, #47), not claw `main`. Re-pin when the fleet does.
  A re-pin advances the ref, re-snapshots `scripts/.vendored_manifest.json`,
  and re-vendors any governed artifact whose hash moved (#49 did one); the
  drift test fails until all three agree.
- **#65 — upstream: the validator's normaliser.** Eighteen of the twenty-one
  ChEBI label exceptions are Greek letters and a Unicode minus that
  `normalize()` does not fold. The fix is in claw; drop the entries when the
  re-pin lands.

## Corpus defects the gates did not see

Found by the first id-label run (#50) and by scoping it. Each is a wrong or
unjoinable value that `just qc` reproduces faithfully.

- **#68 — 68 producer claims name an uncultured bacterium or a metagenome.**
  39 of them (`uncultured bacterium`, `uncultured organism`, `sponge
  metagenome`) name no organism at all; 29 name a strain or a genus and look
  legitimate. Decide the rule in `docs/HARMONIZATION.md` before the extractor
  enforces it — it is a curation judgement, not a defect. Follows #62.
- **#61 — `xrefs` say `chebi:` where the corpus says `CHEBI:`.** MIBiG's
  spelling passed through the seeder; 54 records. Normalise at the seeder.
- **#69 — every re-seed re-stamps all 3,115 curation timestamps**, so every
  corpus PR is a 3,115-file diff and a reviewer cannot see the records that
  actually changed. `record_curation_event` already has `skip_if_recent`.

## Sources

- **Licence enquiries, as a batch — NPASS and CO-ADD.** Both measured
  (`just evaluate-npass`; CO-ADD in `research/`), neither adopted: NPASS states
  no licence anywhere checked, CO-ADD's terms are restricted. The owner deferred
  the outbound enquiries to one batch. Nothing from either enters `data/raw/`
  until the terms are resolved.
- **PubChem structure fetch — decide whether it is wanted.** `PLAN.md` M1
  named a PubChem enrichment for concepts with no structure in an adopted
  source. It was not carried over and no adopted source currently needs it;
  either adopt it as a source-queue entry with its own extractor, or strike it.
- **Unresolved organism names.** `curation/unresolved_taxa.tsv` holds the
  residue NCBI Taxonomy could not resolve exactly — superseded basionyms, in
  the main. Each resolved name is worth several occurrences.

## The work itself

- **M6 — curation.** `biosynthetic_pathway` and `causal_graphs` are empty on
  all 3,115 records. Biosynthesis graphs for the best-evidenced MIBiG records
  first (`BGC_CHARACTERIZED` producers with `CLUSTER_DEMONSTRATED` links),
  then bioactivity graphs. Everything above is scaffold for this.
