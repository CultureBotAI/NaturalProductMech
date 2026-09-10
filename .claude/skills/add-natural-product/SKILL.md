---
name: add-natural-product
description: Add a missing NaturalProductMech compound by proving it is one exact structure with an asserted biological origin and making the seeded corpus reproduce it. Use for a named compound, a MIBiG entry, or a publication lead; use curate-yaml-record for an existing YAML record and source-queue for source ranking.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Add a new NaturalProductMech compound

Produce the first reproducible `NaturalProductRecord` for one missing natural
product. Search hits and papers are leads; only an exact source concept with an
individual structure and an asserted biological origin can become committed
YAML.

Adapted from AntibioticMech's `add-antibiotic`. The identity discipline is
identical; what admits a record is different: here the compound must be
*made by something*, and the source that says so must say it in a way the
schema can carry.

## Boundaries

- Accept only one chemical structure with a Standard InChIKey **and** at least
  one of: a producer assertion with biosynthesis-grade evidence, a cited
  occurrence in a taxon, or a ChEBI role on the committed allow list
  (`conf/np_roles.tsv`). An NP-likeness score or a structural resemblance to a
  known class admits nothing.
- Reject extracts, fractions, essential oils, herbal preparations, mixtures,
  compound classes, scaffolds, structureless names, and evidence for a salt,
  fragment, glycoside, conjugate or stereoisomer that is not the exact
  structure being added.
- An occurrence is not a producer. A LOTUS-style "found in taxon X" row lands
  in `occurrences`; do not write it into `producer_organisms` unless the cited
  source shows biosynthesis (characterized BGC, heterologous expression,
  isotope feeding, or production by an axenic culture).
- If the structure already has a YAML file under `data/natural_products/`,
  switch to `curate-yaml-record`.
- If the structure has an AntibioticMech record, the antimicrobial mechanism
  stays there. Add the record here with its `related_records` link; do not
  copy targets, resistance or MIC data across.
- If the source is missing from the reproducible pipeline, add the extractor or
  stop with a source-adoption issue. Do not hand-write a one-off YAML file.

## Read first

- `CLAUDE.md` for generated-file boundaries and canary discipline.
- `PLAN.md` §2 (scope, producer versus occurrence) and §4 (the AntibioticMech
  join) until `docs/HARMONIZATION.md` exists and supersedes them.
- `docs/CURATION.md` for `PROPOSED`, evidence and review semantics.
- `src/naturalproductmech/schema/naturalproductmech.yaml` for required fields.
- `scripts/seed_from_sources.py` and `scripts/verify_corpus.py` for the fields
  the seeder owns and the committed-corpus reproduction check.
- Two or three close records from the same biosynthetic class.

## Prove the compound is missing

Use exact, narrow searches and include ignored files whenever a search result is
used to prove absence:

```bash
rg --hidden --no-ignore -n -F "<Standard InChIKey>" . -g "!/.git" -g "!/.venv"
rg --hidden --no-ignore -n -F "<CHEBI id, MIBiG accession, or Wikidata QID>" data curation .claude -g "!/.git" -g "!/.venv"
rg --hidden --no-ignore -n -F "<DOI or PMID>" . -g "!/.git" -g "!/.venv"
```

Search the proposed label, exact synonyms, CAS numbers, PubChem CIDs, ChEBI
CURIEs, MIBiG accessions, Wikidata QIDs, NPAtlas ids, DOI, PMID, and Standard
InChIKey. Also inspect `data/natural_products/PATHS.tsv`,
`data/natural_products/RETIRED.tsv` and `data/raw/antibioticmech_inchikeys.tsv`;
a live record, a retired slug, a skipped source concept or an AntibioticMech
twin changes the work from addition to grounding, source repair, linking or
curation.

Never use a broad pattern such as `CHEBI:` or `BGC` to prove absence. If an
exact label has punctuation or spaces, pass it through `rg -F` rather than a
regular expression.

## Choose the source path

New committed records must be emitted by `scripts/seed_from_sources.py` from a
versioned input. Pick the narrowest reproducible path that covers the compound:

- **Present in a newer MIBiG release.** Refresh the MIBiG inventory:
  `just extract-mibig-dry`, then `just extract-mibig`, inspect
  `data/raw/mibig_compounds.tsv` for the entry, and seed that identifier.

  Three MIBiG-specific gates, each of which exists because the obvious reading
  of a field is wrong:
  - The entry's `status` must be active. The dump ships retired and pending
    entries alongside active ones.
  - **Do not gate on `quality`.** It reads `questionable` for 2,710 of 3,013
    entries in the 4.0 release, and the MIBiG paper says that label marks
    legacy-format entries awaiting re-curation, not doubtful science. Gating on
    it would discard most of the database.
  - **Do not gate on the reviewer field.** `changelog.releases[].entries[].reviewers`
    is the placeholder `AAAA…` in essentially every entry; only 25 of 3,013
    carry a real reviewer id. AntibioticMech's reviewer gate does not transfer.
    The producer-evidence gate replaces it: map `loci[].evidence[].method`
    through `conf/producer_evidence.tsv`, which grades in three tiers.
    Heterologous expression, knockouts, enzymatic assays and in-vitro
    expression are `BGC_CHARACTERIZED`. The two correlation methods — expression
    correlated with production, and genomic–metabolomic correlation — are
    `BGC_CORRELATED`: still producer claims, but consistent with co-regulation
    or a neighbouring cluster, so they are marked rather than promoted.
    `Homology-based prediction` is not producer-grade at all and goes to the
    worklist.

  MIBiG stores SMILES and never an InChIKey, so the extractor computes the
  Standard InChIKey locally with the pinned RDKit. A compound record with no
  structure (1,042 of 5,443 in 4.0, many of them class-level names) cannot
  become a record.
- **Present in ChEBI with an allow-listed role.** Refresh with
  `just extract-chebi-dry`, `just extract-chebi`. If the role the
  compound bears is a specialized-metabolite role that is not yet in
  `conf/np_roles.tsv`, adding the role is a reviewed configuration change with
  its own rationale, not a one-compound tweak — measure what else the role
  admits before committing it.
- **Present in LOTUS / Wikidata as an occurrence.** Refresh the LOTUS inventory
  under the committed taxon filter (`conf/sources.yaml` → `producer_scope`).
  If the compound's only occurrence is outside the current producer scope, the
  answer is a scope decision, not an exception.
- **Structure missing from ChEBI.** There is no PubChem structure fetch in
  this repository — `just extract-bioassay` fetches assays for structures the
  corpus already holds. A structure no adopted source carries is a
  source-adoption question, not a fallback (`NEXT_TASKS.md`).
- **Present only in another redistributable structured source.** Add or extend
  an extractor so `conf/sources.yaml`, `SourceEnum`, `data/raw/`,
  `data/raw/MANIFEST.yaml`, `ATTRIBUTION.md`, source concepts, structures and
  provenance reproduce offline. Check `curation/source_queue.tsv` first: a
  source whose `redistribution` is `NON_COMMERCIAL`, `SHARE_ALIKE` or
  `RESTRICTED` (NPAtlas, ChEMBL, the Dictionary of Natural Products) cannot
  emit a record no matter how good its entry is.
- **Present only in a primary paper.** Add a reproducible direct-curator
  inventory for `CURATOR` source concepts before the first YAML write. If that
  lane does not exist yet, implement it or file that prerequisite.
- **Present only in a restricted or name-only source.** Do not add a record.
  File the exact source gap or use `source-queue`.

## Identity and structure

Every source concept needs a stable native `source_id`, `source_label`,
`source_version`, and `minted_identifier`. Use the same deterministic minting
style as the seeder: source plus native identifier, never the output slug or a
mutable display label.

Grounding follows the merge rules:

- use the ChEBI CURIE and `grounding_status: EXACT` when ChEBI itself supplies
  the exact default structure;
- merge a MIBiG or LOTUS concept into that ChEBI record only on an exact
  Standard InChIKey match, computed from the source's own SMILES with the
  pinned RDKit;
- keep a `naturalproductmech:` CURIE and `grounding_status: MINTED` when no
  defensible ontology identity exists;
- leave `grounding_status: REVIEW_NEEDED` only for an exact structure whose
  ontology identity needs human adjudication.

Record `stereo_complete`. Natural products are where undefined stereocentres
and InChIKey tautomer failures are most common; a structure with unassigned
stereocentres is still one record, but the flag must say so.

Parent compounds are strictly broader; salts, stereoisomers, glycosides,
conjugates and semisynthetic derivatives are different records unless the
source and structure prove exact identity. Congeners are related through
`congener_of`, never merged.

## Evidence bundle

The first emitted record keeps the `curation_status` set by its emitter:
`SEEDED` for adopted-source inventories and `PROPOSED` only for a direct
curator-entry lane. Add only fields supported by the source path:

- `label`, `identifier`, `np_pathway`, `source_concepts`,
  `chemical_structure.standard_inchi_key`, `grounding_status`, and
  `curation_status` are required for a usable first record.
- `bgc_class`, `compound_classes` and `ecological_roles` come from a source
  assertion. `np_pathway`, the filing value, is computed by NPClassifier and is
  recorded with its model version; it is never a source assertion, and it never
  admits a record. If the classifier returns more than one pathway, file the
  record `UNCLASSIFIED` and let it queue, but keep every returned label in
  `npclassifier_superclass` and `npclassifier_class` — the filing value is
  single, the classification is not.
- `producer_organisms`, `occurrences`, `biosynthetic_gene_clusters`,
  `bioactivities`, `molecular_targets`, `biosynthetic_pathway` and
  `causal_graphs` need claim-level evidence on each object. A MIBiG-seeded
  producer cites MIBiG and says so.
- `related_records` to AntibioticMech is computed by the seeder from the
  pinned inventory; do not hand-add it.
- Unresolved ambiguity — sponge versus symbiont, plant versus endophyte,
  which congener the paper actually isolated — belongs in a `Discussion`,
  not in over-specific fields.

## Write through the generator

Update the reproducible input or extractor first, then run:

```bash
just seed
just seed-canary <IDENTIFIER>
```

Inspect the canary YAML and object diff. The seeder should append a
`record_curation_event`, assign the slug with `assign_slugs()` and
`write_lockfile()`, and write the YAML through
`write_validated_natural_product()`. Fix that path if any of those steps are
missing.

After the canary is correct:

```bash
just seed-apply
just docs-stats
just qc
```

(`just chemical-map` and `just render` join this list when the site exists — #53.)

If the change is source adoption rather than record addition, also verify the
source queue and provenance:

```bash
just source-queue
just provenance-check
```

Once the site exists (#53), `pages/**` and
`data/embeddings/chemical-structure-map.json` are generated: rebuild them, do
not edit them by hand.

## Report

Report the accepted structure and its InChIKey, the source concept that emitted
it, the origin assertion that admitted it (producer, occurrence, or role) and
its evidence grade, all exact duplicate searches performed, whether an
AntibioticMech twin exists and was linked, the file path assigned in
`data/natural_products/PATHS.tsv`, the claim-level evidence added or
deliberately left empty, and every validation command run.
