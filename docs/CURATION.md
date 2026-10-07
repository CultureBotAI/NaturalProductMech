# Curation

## The decision file

`curation/decisions.tsv` is the curator's half of seeding. One row per source
concept, keyed by that concept's **minted identifier** — the stable
`naturalproductmech:<source>-<hash>` CURIE that appears in every record's
`source_concepts` block.

| Column | Meaning |
|---|---|
| `minted_identifier` | The key. Copy it from the record's `source_concepts` block, or from `just worklist`. |
| `source` / `source_id` / `source_label` | Context for a human reading the file. |
| `decision` | `GROUND` (use `identifier`), `EXCLUDE` (drop the concept), or `KEEP_MINTED`. |
| `identifier` | The CURIE to ground to. Required for `GROUND`. |
| `curator` / `date` / `rationale` | Who decided, when, and why. |

This is a reserved decision format, not an implemented seeder input. The current
seeder does **not** read `decisions.tsv`; adding a row does not change a record.
Use an implemented, tested harmonization path below, or add the appropriate
consumer before recording a new decision here.

## MIBiG structure corrections

`curation/mibig_structure_corrections.tsv` supports the narrow action
`REPLACE_WITH_CHEBI`. It replaces one uniquely owned MIBiG compound structure
with one unambiguous 3-star ChEBI default structure. It does not modify raw
inventories, merge existing owners, or declare the old and new structures equal.

The `source_id` is `BGC accession:compound_index`. The two
`expected_*_row_sha256` values pin the **complete parsed source and target rows**,
including version, locus, names, xrefs, chemistry and empty fields. Compute these
with `naturalproductmech.curate.structure_corrections.row_digest`, not a hash of
the TSV line. Missing/duplicate rows, changed row content, ambiguous ChEBI keys,
or an already occupied destination key stop seeding. Every correction requires
a stable reference, curator, ISO date and rationale. `standard_inchi` and
`stereo_complete` are curator-supplied chemistry derived from the target SMILES
using the project's pinned RDKit and must be verified before adoption.

All original MIBiG xrefs are withheld and recorded in the correction note;
re-adopting any of them needs separate identity evidence. Occurrences, assays,
classification and sibling links join only on the corrected key. No old-key
claims are transferred. The correction appears separately as `CURATOR_INFERENCE`
on producer and BGC evidence and in a resolved source-conflict discussion.
The chemical structure names ChEBI as its source; the MIBiG source concept stays.
NPClassifier's extractor also consumes these corrections, so run its dry run
and one-call canary on the corrected structure before seeding.

Seeding refuses to overwrite an existing file with a different structure.
Correcting a curated owner requires an explicit, separately audited migration
through `write_validated_natural_product` (or the component bundle workflow):
re-audit each old claim, retain applicable graphs and history, append an event,
and update `PATHS.tsv` for the new identifier/path. Never relax the ordinary
same-key carry-forward rule. Canary, reproduction and full corpus gates still
apply. Corrections that would merge owners or relocate components need a
dedicated migration and are outside this narrow path.

## MIBiG locus-evidence overrides

`curation/mibig_locus_evidence_overrides.tsv` is for a narrower correction:
MIBiG sometimes cites a paper at entry level without migrating its experiment
into `loci[].evidence[].method`. A row in this table supplies those MIBiG
method names before the seeder grades both claims: enzymatic or heterologous
evidence upgrades only the locus link written to `biosynthetic_gene_clusters`,
while native knock-out or correlation evidence can also upgrade the
`producer_organisms` grade.

| Column | Meaning |
|---|---|
| `minted_identifier` | The exact MIBiG compound row key from `source_concepts`. Use this rather than `source_id`, because a BGC can list several compounds. |
| `source` / `source_id` / `source_label` | Context for a human reading the file. |
| `locus_evidence_methods` | Pipe-separated MIBiG method names from `conf/producer_evidence.tsv`. |
| `curator` / `date` / `rationale` | Who decided, when, and why. |

The explicit `action` is `REPLACE` for these method corrections. Legacy callers
without an `action` key retain that behavior; an explicitly blank or unknown
action is rejected.

Use `WITHDRAW` only when source evidence is inapplicable to the named
taxon/locus, not merely because a method is missing. Replacement methods must
be empty. The row must carry a stable DOI, PMID or HTTPS `reference`, a
`rationale`, `curator`, `date`, `source: MIBIG` and `source_id`. It also pins
`expected_entry_version`, `expected_taxon_id`, `expected_genome_accession`,
`expected_locus_from`, `expected_locus_to`, `expected_standard_inchi_key` and
`expected_locus_evidence_methods` to the exact raw values. Missing/duplicate
targets or any source-context drift fail for inspection, including method
order changes. An upstream refresh must not silently inherit a stale exclusion.

Withdrawal is applied before lead-record selection. An empty applicable method
set grades the producer as `SOURCE_ASSERTION` and the cluster link as
`CLUSTER_UNSTATED`, not `CLUSTER_PREDICTED`. The original inventory remains
untouched; the original method names, qualification and curator attribution
travel in separate claim-level `CURATOR_INFERENCE` evidence for both producer
and cluster. The database's original citation stays `DATABASE_ASSERTION`.
This corrects BGC0000892 version 4: its experiments concern DSM50341, not the
BSR3 genome it lists. It does not relabel either strain or prove a native
protein mapping.

## What a re-seed keeps, and what it overwrites

The corpus is generated, so a re-seed rebuilds every record. What it does *not*
do is discard the work a curator did on one. Four things are carried forward
from the file, matched on the record's Standard InChIKey so a reused slug
cannot inherit another compound's curation:

| carried | why |
|---|---|
| `biosynthetic_pathway`, `causal_graphs`, `causal_graph_refs` | M6 curation; the seeder does not produce them at all |
| `curation_history` | the trail, and re-stamped only when seeder-owned content changed |
| `curation_status` when it is not `SEEDED` | only a curator moves a record off `SEEDED`, so only a curator can move it back |
| curator-owned fields on a `discussion` | the seeder raises the question, you answer it |

On a discussion the seeder owns `discussion_id`, `kind` and `prompt` — it
re-raises the question each run — and everything else is yours: `status`,
`resolution_note`, `resolved_date`, `posed_by`, `rationale`, `evidence`,
`proposed_experiments`, `notes`. Matching is on `discussion_id`. A discussion
the seeder stops raising is dropped along with its answer, which is right: the
condition that prompted it is gone.

**Everything else on a record is the seeder's**, and editing it by hand will be
reverted on the next `just seed-apply` — and, since #85, reported by
`just verify-reproduction` before then. A label, a producer claim or a
classification that is wrong is a bug in an extractor, the seeder, or
`curation/decisions.tsv`; fixing it in the record fixes one row and leaves the
cause in place.

## Evidence rules

- Evidence sits on the **narrowest object it supports**. Every
  `ProducerOrganism`, `Occurrence`, `BiosyntheticGeneCluster`, `PathwayStep`,
  `BioactivityObservation`, `MolecularTarget`, `ClinicalStatusAssertion` and
  `CausalEdge` requires its own. Record-level `evidence` never satisfies that.
- A **database assertion is cited as one**. A MIBiG producer is
  `source: MIBIG` with the accession and `evidence_type: DATABASE_ASSERTION`;
  it does not become the isolation paper because MIBiG cites one.
- A `snippet` is a short verbatim passage, never a paraphrase.
- **A value without units and method is not a measurement.** A
  single-concentration screening hit is a percentage inhibition, not an MIC.
- **An assay run on an extract is not an observation about a constituent.**
- Preserve disagreement. Two candidate producers, a revised structure, a
  stereochemical reassignment: narrow the claim or open a `Discussion`.

## What may back a `bioactivity_summary` value

`bioactivity_summary` is derived and carries no evidence of its own, so it must
never float. Exactly one rule, and it is the same one everywhere:

1. a `bioactivities` item — a measurement, with units and method;
2. a `molecular_targets` item whose target implies that activity class;
3. a `related_records` link to a sibling corpus that carries the mechanism —
   this is how an antibacterial value is backed without duplicating
   AntibioticMech's target and resistance content;
4. a cited source assertion, such as MIBiG's own bioactivity labels.

No value without one of the four, and the record says which.

## What a REVIEWED record means

A record moves from `SEEDED` to `REVIEWED` when a curator has checked all of:

1. **Identity** — the structure is the compound the label names, and the ChEBI
   grounding, or the reason for a minted identity, is right.
2. **Structure** — SMILES, InChI, InChIKey and formula agree, at the
   stereochemical resolution the source actually determined. `stereo_complete`
   is honest.
3. **Filing and classification** — `np_pathway` matches its committed
   classification, and every asserted class and role is retained.
4. **Origin** — every producer claim carries evidence that shows biosynthesis
   by that taxon, at the `evidence_basis` it declares; every occurrence is
   cited; every gene cluster is active and names this compound.

A curated `causal_graph` is the goal state, not the entry requirement.

## The two errors this corpus is most likely to make

**Occurrence written as production.** A taxon that a paper only isolated the
compound *from* does not belong in `producer_organisms`. Watch for the
host–symbiont trap: sponge, tunicate, lichen and endophyte metabolites whose
real producer is a microorganism. When it is unresolved, that is a
`Discussion`, not a producer claim.

**A cluster grade read as a producer grade.** `BGC_CHARACTERIZED` on a
producer means evidence addressed *this organism*; `CLUSTER_DEMONSTRATED` on a
gene cluster means evidence addressed *this locus*. A record can carry the
second without the first, and 485 producer claims once carried the first on the
strength of the second. When curating, check which question the cited
experiment answered.

**Computed presented as asserted.** `np_pathway` and `np_classification` are
NPClassifier's output and say so, with the model version. Upgrading a
`BGC_CORRELATED` producer to `BGC_CHARACTERIZED` is the same error one level
down.

Neither is visible to any gate. That is what review is for.

## Writing a record

### Complete mechanism reads

Graphs can be inline in `causal_graphs` or referenced by ordered local IDs in
`causal_graph_refs`. Each reference resolves to
`data/causal_graphs/<StandardInChIKey>/<graph_id>.yaml`, a closed-schema
`CausalGraphDocument` with `record_id`, `standard_inchi_key`, `graph`, and its
own `curation_history`. Both owner identifiers must match the record exactly.
References are graph IDs, never arbitrary paths. Inline graphs precede referenced
graphs; IDs must be unique across both. Nodes and edges remain graph-local.

Read the owner AND every referenced component when reviewing a mechanism. Use
`naturalproductmech.graph_components.read_natural_product(path)` for reports,
rendering, or analysis. It resolves all graphs and fails on missing/invalid
components. Its expanded dictionary retains refs and is **read-only**: writing
it would duplicate graph IDs. Mutators and the seeder must load raw owner YAML.
The structure-only embedding and PubChem identity extractor deliberately read
raw owners because they do not consume mechanisms. The vendored label checker
reads components through its explicit `graph_component_nodes` config target.

### Graph component writes

Use components when complete evidence would exceed the 64-KiB owner limit.
Every component has the same 64-KiB limit; do not weaken qualifiers or drop
biology to fit. Split at coherent, independently reviewable graph boundaries,
not arbitrary line counts. Do not claim an inter-graph edge with a local node ID.

For a migration, preserve every graph object and the owner's existing history,
add refs before `curation_history`, and append a migration event to the owner.
Each component gets an event naming the original record and source commit so
the preserved parent history can be followed. Compare the resolved graphs to
the original objects, including evidence and snippets, and compare rendered
output. A storage migration alone must not change biology.

For a new or changed component, append `record_curation_event` to that component.
Append an owner event whenever the owner changes (including a new ref). Submit
raw owner and changed components to
`write_validated_graph_bundle(owner, record_path, components)` from
`naturalproductmech.graph_components`. It preflights the bundle's schema,
ownership, topology, sizes and append-only events before writes; ordinary write
failures roll back. It does not provide a multi-file filesystem transaction:
after interruption or power loss, inspect the worktree and run the complete
audit before retrying. Do not delete or detach components implicitly.
Preflight also rejects reassignment of an existing component to another owner,
even with an appended event. Distinct records sharing an InChIKey must use
distinct component graph IDs; an ownership transfer needs an explicit migration.

`just validate-strict <owner-path>` checks the owner and all its components.
Full `just validate-all`, `just verify-corpus`, and `just verify-reproduction`
also reject orphaned components. Reproduction carries refs and audits components;
it does not regenerate curator evidence from source inventories. Reseeding an
unchanged record must preserve owner AND component bytes.

### Inline record writes

Never hand-edit a record and never serialize one directly. Load the YAML, apply
only the reviewed changes, then finish with both repository helpers:

```python
from pathlib import Path

import yaml

from naturalproductmech.curate.curation_event import record_curation_event
from naturalproductmech.validation.write_validated import write_validated_natural_product

path = Path("data/natural_products/<np_pathway>/<slug>.yaml")
doc = yaml.safe_load(path.read_text(encoding="utf-8"))
assert doc["identifier"] == "<expected CURIE>"

# Apply only the source-checked curator-owned changes here.

record_curation_event(
    doc,
    curator="<actual agent identifier>",
    action="RECORD_CURATED",
    changes="Describe the exact evidence-backed changes and unresolved gaps.",
    llm_assisted=True,
)
write_validated_natural_product(doc, path)
```

If no substantive field changed, do not write and do not append an event.

## Opening a Discussion

`Discussion` and `Dataset` come from the vendored `mech_shared.yaml`, and their
field names are not guessable from prose — it is `discussion_id`, not
`local_id`, and `prompt` is required beside it. `tests/conftest.py` carries
schema-valid fixtures for both; copy those shapes rather than inventing one.

```yaml
discussions:
- discussion_id: producer-attribution
  kind: CURATION_TODO          # OPEN_QUESTION | KNOWLEDGE_GAP | CONTROVERSY | ...
  status: OPEN                 # OPEN | UNDER_DISCUSSION | RESOLVED | ARCHIVED
  prompt: >-
    Is the sponge the producer, or its bacterial symbiont? The isolation report
    describes a whole-animal extract and does not distinguish them.
  rationale: >-
    Recorded as an occurrence rather than a producer claim until an axenic
    culture, a characterized cluster, or a feeding study separates them.
```

A discussion is for a concrete unresolved question whose answer would change
the record. It is not a placeholder for every empty optional field.
