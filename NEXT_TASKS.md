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

- **#50 — the id-label validator never runs.** Vendored, sha-pinned,
  contract-tested, and inert: no `conf/id_label_targets.yaml`, no `run_qc.py`
  step. HabitatMech's config is the closest template. Expect findings on the
  first run — the seeder's name rules were tuned against ChEBI names, not
  ontology labels.
- **#51 — governed artifacts have no drift guard before M4.** The identity
  check stops `vendored-sync` before it compares bytes, and only two of the
  thirteen fleet-wide artifacts are hash-pinned in `tests/test_schema.py`. A
  committed manifest snapshot at the pinned ref would close this offline.
- **#55 — `uv.lock` is not committed and CI syncs unlocked.** `verify-corpus`
  proves reproduction under whatever environment is installed today. Commit
  the lockfile; run CI with `--locked`.
- **#57 — `just new-history` does not exist.** The vendored curation-history
  contract names it; TraitMech and HabitatMech have it. Port the fleet's
  recipe rather than invent one. Nothing to scaffold until M6 starts.

## Fleet

- **M4 — admission to claw.** Three PRs in claw's order (`PLAN.md` §7).
  Until then `just vendored-sync` fails on identity, by design. No issue yet.
- **Claw pin.** `scripts/.vendored_canon_ref` follows what the other eight
  members pin (`eeccfebe23`, #47), not claw `main`. Re-pin when the fleet does;
  a re-pin re-vendors any governed artifact whose hash moved (#49 did one).

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
