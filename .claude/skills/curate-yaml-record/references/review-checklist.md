# NaturalProductRecord review checklist

Use this checklist to make claim-level decisions for one record. It is not a
requirement to populate every optional slot.

## Evidence standard

- Put evidence on the narrowest object it supports. `ProducerOrganism`,
  `Occurrence`, `BiosyntheticGeneCluster`, `BioactivityObservation`,
  `MolecularTarget`, `PathwayStep` and every `CausalEdge` require their own
  `evidence`; record-level evidence does not satisfy that obligation.
- An `EvidenceItem.reference` should be a stable `PMID:...`, `DOI:...`,
  `MIBIG:BGC...`, `wikidata:Q...`, database CURIE, or official URL. Confirm
  that the identifier resolves to the inspected source and that the source
  concerns the exact compound form.
- A `snippet` is a short verbatim passage, not a paraphrase. Use `notes` for
  the curator's interpretation, limitations, strain, culture conditions, or the
  fact that an assertion comes from a database rather than primary literature.
- Cite a database assertion as a database assertion. A MIBiG producer is
  `source: MIBIG` with the accession; it does not become the isolation paper
  merely because MIBiG cites one.
- Reviews are useful for vocabulary and citation discovery. Prefer the cited
  isolation, biosynthesis or assay paper for the actual claim.
- Preserve disagreement. When reliable sources conflict — two producers, two
  stereochemical assignments, a revised structure — narrow the claim or
  capture a `CONTROVERSY`; do not silently choose the convenient source.
- Negative search results mean "not found in the bounded search," not "no
  evidence exists." State the query/provider/date when that distinction
  matters.

## Field-by-field audit

| Area | Verify | Complete enough when |
|---|---|---|
| Identity | `identifier`, label, synonyms, `grounding_status`, source concepts, and exact chemical form agree; congener, glycoside and stereoisomer boundaries respected. | The record denotes one individual structure and any minted identity has an explicit rationale or queued decision. |
| Structure | SMILES, Standard InChI, InChIKey, formula, charge, masses, source, retrieval date and `stereo_complete` are mutually consistent and match the cited isolation/biosynthesis source at its stereochemical resolution. | The InChIKey is valid, the source record is the same form, and undefined stereocentres are flagged rather than invented. |
| Equivalence | Every `xref` denotes the same structure; every `parent_compounds` value is strictly broader; `congener_of` names a sibling, not a parent. | No class, conjugate, salt, stereoisomer, glycoside, patent, article, or macromolecular structure is asserted as exact chemical identity without a documented allowed exception. |
| Classification | `np_pathway` is the filing choice, computed by NPClassifier, and carries its model version; `bgc_class`, `compound_classes` and `ecological_roles` preserve every source-asserted value on their own axes. | Filing follows repository priority without erasing assertions; nothing computed is presented as asserted; no record was admitted by a computed signal. |
| Producer organisms | Each taxon has an NCBITaxon id, a strain where the source gives one, an `evidence_basis` (`BGC_CHARACTERIZED` / `BGC_CORRELATED` / `HETEROLOGOUS_EXPRESSION` / `ISOTOPE_FEEDING` / `AXENIC_CULTURE` / `SOURCE_ASSERTION`) matching what the source shows, and evidence that actually shows biosynthesis by that taxon. | No item rests on "isolated from"; a correlation-only cluster is `BGC_CORRELATED`, never `BGC_CHARACTERIZED`; host–symbiont ambiguity is a `Discussion`, not a producer claim; species-level claims are not generalized from one strain without saying so. |
| Occurrences | Each taxon has an id and a citation to an isolation or detection report; the compound in the report is this structure. | Every occurrence is cited; none has been promoted to producer without new evidence. |
| Gene clusters | MIBiG accession and entry version exist, have active status, name this compound rather than a class, and the entry's organism matches the record's producer; the locus evidence method is recorded and is not homology-only where a production claim rests on it. | Each BGC has evidence; a class-level, retired or homology-only entry is queued, not asserted. MIBiG's `quality` and reviewer fields are not used as truth signals. |
| Pathway | Each step names an enzyme (UniProt / EC / Rhea), substrate and product with evidence; the order is the source's. | Steps are cited individually; proposed or inferred steps are marked so. |
| Bioactivity | Assay run on the pure compound; organism / cell line / enzyme, outcome, method, value, qualifier and units match the experiment. | Every observation has evidence; every value has units and method; no extract-level result is attributed to the compound; nothing is generalized to a spectrum from one assay. |
| Bioactivity summary | Every `bioactivity_summary` value is backed by at least one `bioactivities` item, a `molecular_targets` item, or a `related_records` link to AntibioticMech. | No summary value floats without a backing item. |
| Molecular targets | Target identity/type/relation, taxon, experimental context, evidence status, source version/date, measurements, and protein examples are appropriately scoped; antimicrobial targets are curated in AntibioticMech when a link exists. | Each target has claim-level evidence; direct binding is asserted only from direct evidence; the target is a family, complex, or function and organism-specific UniProt records remain examples. |
| Cross-corpus links | `related_records` entries resolve in the pinned sibling inventory and denote the same InChIKey. | Links are seeder-computed from the pin; none hand-added. |
| Clinical status | Substance identity is separate from product, jurisdiction, application, and marketing state. | The official source supports the exact assertion and its retrieval/version metadata is present. |
| Causal graph | Nodes represent the right entity types (genes, enzymes, intermediates, targets, effects); edges connect declared nodes and state only source-supported direction and causality; `scope` is BIOSYNTHESIS or BIOACTIVITY. | Every edge has evidence and the graph distinguishes mechanistic biology from classification or measurement context. |
| Datasets | Dataset is public, specifically relevant (genome assembly of the producer, MS/NMR deposition, BGC sequence), and identified by accession or durable URL. | Relevance and associated publication/evidence are clear; the field is not a bibliography dump. |
| Discussions | Prompt describes a concrete unresolved question, conflict, or consequential curation task. | It has a stable local ID, kind/status, rationale, and citations when the gap itself is evidence-based. |
| Audit | Status and history match what was actually checked and changed. | The latest event is accurate, transparent about LLM assistance, and REVIEWED is used only after all sign-off criteria pass. |

## Generated versus curator-owned changes

Seeder-owned fields include identity, label/definition, synonyms,
`parent_compounds`, `xrefs`, filing class and its provenance, asserted classes
and roles, chemical structure, source concepts, grounding status,
`related_records`, and the MIBiG-marked and LOTUS-marked producer, BGC and
occurrence items. Fix these through the committed inventory, extractor, seeder,
or `curation/decisions.tsv`, then re-seed. Do not make a record-only correction
that the next seed run will undo.

Curator additions can include evidence, curator-owned producer or occurrence
items with a `CURATOR:` note, pathway steps, bioactivities, targets, mechanism
graphs, datasets, discussions, and literature-backed additions beside imported
items. Imported slices remain source-owned: add a curator-supported item or
record an `EXCLUDE` decision; do not disguise a database row as hand-curated
literature.

For any record mutation, load YAML and finish with both repository helpers:

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

Put a one-off mutator under `/tmp`, not in the repository, unless reusable
curation behavior and tests are themselves part of the requested change. Review
the object-level diff before writing. If no substantive field changed, do not
write and do not append an event.

## REVIEWED gate

`REVIEWED` means all four repository sign-off criteria have passed:

1. The label, exact structure (including stereochemical resolution), and ChEBI
   grounding or minted-identity rationale are correct.
2. SMILES, InChI, InChIKey, formula, and source describe the same structure.
3. Filing class and its provenance, and all retained classes and roles, match
   source assertions; nothing computed is presented as asserted.
4. Every producer claim carries biosynthesis-grade evidence, every occurrence
   is cited, and every BGC entry is active, reviewed and names this compound.

A complete biosynthesis causal graph is a goal, not a prerequisite. Conversely,
a long list of citations does not compensate for an unresolved identity conflict
or an occurrence sitting in the producer field. Leave the record `SEEDED` or
`PROPOSED` and report blockers whenever a gate is unmet.

For a multi-record request, regenerate `curation/record_review_queue.tsv` after
each batch. The queue must contain every record that is neither `REVIEWED` nor
`DEPRECATED`; it is a checkpoint, not evidence that any listed claim was read.
