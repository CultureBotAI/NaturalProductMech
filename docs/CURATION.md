# Curation

## The decision file

`curation/decisions.tsv` is the curator's half of seeding. One row per source
concept, keyed by that concept's **minted identifier** — the stable
`naturalproductmech:<source>-<hash>` CURIE that appears in every record's
`source_concepts` block.

| Column | Meaning |
|---|---|
| `minted_identifier` | The key. Copy it from the record or from `just worklist`. |
| `source` / `source_id` / `source_label` | Context for a human reading the file. |
| `decision` | `GROUND` (use `identifier`), `EXCLUDE` (drop the concept), or `KEEP_MINTED`. |
| `identifier` | The CURIE to ground to. Required for `GROUND`. |
| `curator` / `date` / `rationale` | Who decided, when, and why. |

Decisions apply at seed time, so a decision changes the corpus only after
`just seed-apply` — and `just verify-corpus` then proves the corpus matches.

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

**Computed presented as asserted.** `np_pathway` and `np_classification` are
NPClassifier's output and say so, with the model version. Upgrading a
`BGC_CORRELATED` producer to `BGC_CHARACTERIZED` is the same error one level
down.

Neither is visible to any gate. That is what review is for.

## Writing a record

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
