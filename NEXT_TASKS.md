# Next tasks

Owed work, by issue. This is the ledger `PLAN.md` §6 and the skills point at:
what the repository has committed to and not yet delivered. An item leaves this
file when its issue closes, not before. The issue carries the evidence and the
discussion; this file carries the order.

Milestones are in `PLAN.md` §7. M0–M5 have landed (M4, fleet admission, in
culturebotai-claw#395); M6 has not.

## Requested next chemistry work — 2026-11-08 intake

This is the proposed execution order for the user's five chemistry blocker
groups, after current authorized work and a verified workflow boundary. While the backlog PR
is open, it is a proposed order; after merge it must reach the session through
NPM's own workflow. This file is not an automatic runtime queue, and a saved
backlog or a transport result is not proof that the native session accepted work.

| Order | Issue | Implementation plan | First bounded outcome |
| --- | --- | --- | --- |
| 1 | [#1237: Resolve metallophore identifiers and source eligibility](https://github.com/CultureBotAI/NaturalProductMech/issues/1237) | [Plan](https://github.com/CultureBotAI/NaturalProductMech/issues/1237#issuecomment-6731359732) | Reject the three wrong supplied ChEBI mappings; account for existing staphylopine and the bacillopaline near-match before source refresh. |
| 2 | [#1238: Repair the pinned pre-pseudomonine representation](https://github.com/CultureBotAI/NaturalProductMech/issues/1238) | [Plan](https://github.com/CultureBotAI/NaturalProductMech/issues/1238#issuecomment-6731415274) | Use a source-pinned, identity-preserving representation canary; repeat at the locked RDKit version. |
| 3 | [#1240: Adjudicate pre-putrebactin form ambiguity](https://github.com/CultureBotAI/NaturalProductMech/issues/1240) | [Plan](https://github.com/CultureBotAI/NaturalProductMech/issues/1240#issuecomment-6731416669) | Keep the collision guard; preserve both source concepts until exact-form or unresolved admission is reviewed. |
| 4 | [#1239: Hold and adjudicate the tenuazonic-acid candidate](https://github.com/CultureBotAI/NaturalProductMech/issues/1239) | [Plan](https://github.com/CultureBotAI/NaturalProductMech/issues/1239#issuecomment-6731415891) | Preserve the existing BGC0002158 owner; no automatic tautomer-key merge or second record. |
| 5 | [#1241: Distinguish ferric complexes from free ligands](https://github.com/CultureBotAI/NaturalProductMech/issues/1241) | [Plan](https://github.com/CultureBotAI/NaturalProductMech/issues/1241#issuecomment-6731417235) | Retain metal/protonation/source identity and inspect workup and producer evidence for each exact entity. |

The order resolves identifier mistakes first, then uses the narrow representation
repair as the implementation canary before broader identity decisions. Work
touching shared admission/identity code should be serialized and re-reviewed
after earlier changes; an unresolved scientific decision stays deferred rather
than weakening a guard. Each issue's source pins, evidence requirements,
negative controls and PR boundaries govern its implementation. Follow normal
branch/PR, repository checks and independent adversarial review; merges remain
a separate user decision. This request does not authorize data changes merely
because a name appears in the list.

**Dispatch hold at intake verification:** the supervisor's adopted C4S3
protein-example goal and the separately completed user-directed chelator goal
do not match. PR #1054 and its still-open findings #1055/#1056 remain attributed
to C4S3; the completed chelator work does not close them. Preserve active work,
drafts, receipts and repair budgets. This backlog supplies neither closure
evidence nor authority to reconcile that boundary. Do not replay either goal
or send around the supervisor gate. Once separately approved reconciliation
and ordinary closure checks establish a safe boundary, recheck the process,
screen, native state and supported task-dispatch path. Require exact native
acceptance of any scoped request; otherwise retain this order and report the
hold.

## Claims the code does not yet deliver

Documentation was ported from AntibioticMech ahead of the code. These are the
pieces named as available that were never built.


## Gates that do not yet guard

- **#64 — NCBITaxon labels are skipped by the id-label gate.** The corpus's
  largest (id, label) surface, about 13,700 pairs; OAK's adapter is 13.5 GB
  and cannot be cached in CI. Derive a corpus-scoped adapter from `names.dmp`
  in `extract_ncbi_taxonomy.py` and point the config at it. A local run
  already found 123 distinct mismatching pairs and 58 unknown ids (#62, #63).

## Fleet

- **Claw pin.** `scripts/.vendored_canon_ref` holds the claw commit every fleet
  member pins, not claw `main`; claw's fleet audit requires them to agree.
  Re-pin when the fleet does.
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
