---
name: curate-yaml-record
description: Review and curate one NaturalProductMech compound YAML record for scientific accuracy, claim-level evidence, producer-versus-occurrence correctness, completeness, and resolvable gaps. Use when asked to audit, improve, complete, add evidence to, or mark an individual natural product record REVIEWED; do not use for bulk source ingestion or as permission to contact anyone or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Curate one NaturalProductMech YAML record

Produce a scientifically defensible record and an explicit account of what is
supported, corrected, still missing, and genuinely unknown. Search results are
leads; only inspected sources can support a claim.

Adapted from AntibioticMech's `curate-yaml-record`. The guarded write path and
the evidence standard are identical. The scientific questions differ: here the
record's central claims are *who makes this, from what, and with what
evidence*, and the two errors this skill exists to catch are an occurrence
written as production and a computed classification written as an assertion.

## Boundaries

- Resolve one target under `data/natural_products/<np_pathway>/<slug>.yaml`. If a
  name matches multiple structures (congeners, glycosides, stereoisomers),
  stop and disambiguate before changing anything.
- A request to review or assess is read-only. A request to curate, improve,
  complete, correct, or add evidence authorizes local edits to the named record
  and the smallest necessary repository-owned provenance path.
- Never create or edit a GitHub issue, PR, comment, discussion, email, form, or
  message, and never add an `@` mention, without explicit authorization for
  that exact outbound action. Read-only literature and database requests are
  allowed when they are needed for the requested curation.
- Do not transmit a contact email as API metadata. Unset `NCBI_EMAIL` for
  publication discovery unless the user explicitly authorizes sending it.
  Billable providers only with explicit approval.
- Preserve unrelated work. Follow `CLAUDE.md`: work on a branch before editing,
  and use a separate worktree when the current checkout is dirty or occupied.
- Never infer that a missing optional field is false. Never fill a field merely
  to improve coverage.
- Antimicrobial mechanism content belongs to AntibioticMech. If the record has
  a `related_records` link there, do not add antimicrobial targets, resistance
  or MIC data here; curate them in the sibling corpus.

## Read before judging the record

Read the target record and these repository contracts:

- `CLAUDE.md`
- `docs/CURATION.md`
- `docs/HARMONIZATION.md` (until it exists, `PLAN.md` §2–§4)
- the relevant classes and enums in
  `src/naturalproductmech/schema/naturalproductmech.yaml`
- [references/review-checklist.md](references/review-checklist.md)

Check the record's `source_concepts` against the committed inventories and
`curation/decisions.tsv`; do not treat the rendered page or generated prose as
an independent source.

## Workflow

### 1. Establish a baseline

Read the entire YAML, not selected fields. Record its identifier, InChIKey,
`stereo_complete`, grounding state, source concepts, filing class and its
provenance (asserted or computed), producers with their `evidence_basis`,
occurrences, BGCs, curation status, existing citations, existing discussions,
and any `related_records`. Run closed-schema validation without dirtying the
normal report:

```bash
just validate-strict <record-path> --out /tmp/naturalproductmech-record-validation.tsv
just verify-corpus --summary
```

Inspect relevant worklist entries, especially `producer-evidence`,
`occurrence-only`, `computed-class`, `stereo-incomplete`, `bgc-unreviewed`,
`xref-unverified`, `multi-component`, and `sibling-link`. A green gate
establishes structural consistency, not scientific truth.

For a bulk request, still review records one at a time. Generate the exhaustive
checkpoint with:

```bash
just review-queue --limit 0 --tsv curation/record_review_queue.tsv
```

Remove a row only by actually moving its record to `REVIEWED` or `DEPRECATED`;
the queue is derived state.

### 2. Verify identity and structure first

Do not research a producer or an activity until the record is known to denote
the intended individual chemical structure. Check label and synonyms,
identifier grounding, congener/glycoside/salt/stereoisomer boundaries,
source-concept agreement, and consistency among SMILES, Standard InChI,
InChIKey, formula, charge, and masses.

Natural products are where identity goes wrong quietly: a paper isolates
"compound 3" and later literature names it; congener families share a name
stem; stereocentres are assigned years after isolation and revised again. Check
that the structure on the record is the one the cited producer or occurrence
source actually reports, at the stereochemical resolution it reports it.
`stereo_complete: false` is honest; a fully specified structure whose
stereochemistry the source never determined is not.

If a seeded identity, structure, classification, source concept, or xref is
wrong, correct its inventory, extractor, seeder, or the applicable row in
`curation/decisions.tsv`. Do not patch a generated field in the record.

### 3. Review every existing scientific claim

For each claim, ask whether the cited source supports this exact compound,
relationship, organism, and strength of wording. Distinguish:

- an upstream database assertion (MIBiG, LOTUS, ChEBI);
- a primary experimental publication;
- a review or other secondary summary; and
- a search-result snippet, which is discovery metadata and not evidence.

**Producer claims.** For each `producer_organisms` item, the cited evidence
must show biosynthesis by that taxon: a characterized gene cluster, heterologous
expression, isotope feeding, or production in axenic culture. "Isolated from"
is an occurrence. Check that `evidence_basis` matches what the source actually
shows — `BGC_CHARACTERIZED` needs sufficiency or necessity demonstrated, while
a cluster whose only support is that expression and production correlate is
`BGC_CORRELATED`, and quietly upgrading one to the other is the same
overstatement as writing an occurrence into the producer field. If the source only supports occurrence, move the claim to
`occurrences` (through the guarded path) and say so. Watch for the host–symbiont
trap: a compound isolated from a sponge, tunicate, lichen or plant whose actual
producer is a bacterium or fungus. Watch for strain: a species-level producer
claim from one strain is a strain-level claim.

**BGC claims.** The MIBiG accession and entry version must exist, have active
status, and name this compound rather than its class. The organism on the BGC
entry and the producer on the record must be the same taxon. Check the
locus evidence method that the producer claim rests on: a cluster supported
only by homology-based prediction does not support a production claim, and
MIBiG's `quality` and reviewer fields do not mean what their names suggest —
`questionable` marks a legacy-format entry, and the reviewer id is a
placeholder in almost every entry. Neither is a truth signal to lean on.

**Classification.** `np_pathway` is the filing decision and is computed by
NPClassifier, so its provenance must name the model version. `bgc_class` is
MIBiG's claim about the gene cluster and `compound_classes` are asserted claims
about the molecule; these are different axes and MIBiG 4.0 separated them
deliberately. A computed pathway disagreeing with an asserted compound class is
a `Discussion`, not a silent pick.

**Activities and targets.** Prefer primary experimental papers. Verify that
the assay was run on the pure compound, not an extract or a fraction, and that
the value carries units and a method. Do not upgrade docking, correlation,
class membership or "reported to have" into measured activity or direct binding.

Use the repository adapters for candidate discovery when useful:

```bash
env -u NCBI_EMAIL uv run python scripts/search_publications.py \
  --provider pubmed --provider semantic-scholar \
  --query '<compound names plus the claim being checked>' \
  --limit 20 --output /tmp/naturalproductmech-publications.jsonl
```

Search by exact label, important synonyms, identifiers, producer taxon and
targeted claim terms rather than one broad query. Follow promising citations
backward to the isolation paper and the biosynthesis paper. Do not cite the
normalized search output itself.

### 4. Assess completeness and address supported gaps

Apply the field-by-field checklist. Attempt to resolve material gaps with
bounded, targeted searches. Add information only when the exact assertion is
supported and representable without stretching the schema.

Prioritize gaps that determine whether the record can be trusted:

1. identity and structure conflicts, including stereochemistry;
2. producer claims without biosynthesis-grade evidence;
3. unsupported or overstated existing claims;
4. missing BGC or pathway evidence where a characterized cluster exists;
5. bioactivity, target, clinical and causal detail that a source specifically
   reports.

Do not add a generic `Discussion` for every empty optional field. Add one only
for a concrete unresolved conflict, evidence gap, or curation task whose
resolution would materially change the record: which organism in a
host–symbiont pair is the producer, which congener the isolation paper
describes, a stereochemical revision, a MIBiG entry naming a class.

### 5. Write through the guarded path

Never hand-edit a record and never serialize it directly. For curator-owned
fields, use a narrowly scoped temporary or checked-in Python mutator that:

1. loads the existing YAML;
2. asserts the expected record identifier and path;
3. makes only the reviewed changes;
4. calls `record_curation_event` from
   `naturalproductmech.curate.curation_event` with a specific action and change
   summary, and `llm_assisted=True` for agent-produced changes; and
5. writes with `write_validated_natural_product` from
   `naturalproductmech.validation.write_validated`.

Do not append a history event when the document is otherwise unchanged. Use the
actual agent identifier (`claude` in Claude Code, `codex` in Codex) when no
human curator identity was supplied; never attribute an agent's judgement to
the user.

Seeder-owned producer and occurrence items (MIBiG-marked, LOTUS-marked) are
compared to their inventories by `verify-corpus`. To override one, follow
`docs/CURATION.md`: add a curator-owned item with a `CURATOR:` note and real
evidence, or record an `EXCLUDE` decision against the source row. Do not edit
the seeded item in place.

Set `curation_status: REVIEWED` only when identity, structure, filing class,
and every producer claim have all been checked to the standard in
`docs/CURATION.md`. Otherwise preserve the existing status and report the
blocking gaps. A record may be materially improved without being REVIEWED.

### 6. Verify and report

After any edit, run:

```bash
just validate-strict <record-path> --out /tmp/naturalproductmech-record-validation.tsv
just verify-corpus
just qc
git diff --check
git diff -- <record-path> curation/decisions.tsv src scripts tests
```

Read the resulting YAML again. Confirm citations sit on the claims they support,
producers and occurrences are in the right field, the audit event accurately
describes the diff, and no seeded field drifted.

Report:

- corrections and additions, with the supporting PMID, DOI, MIBiG accession,
  database record, or official URL;
- every producer claim's evidence basis after review, and any moved to
  occurrence;
- claims checked and retained;
- remaining gaps, including searches that did not resolve them;
- whether the record qualifies as REVIEWED and why; and
- validation and test results.

Do not create an issue for a remaining gap unless the user separately asks for
that GitHub mutation.
