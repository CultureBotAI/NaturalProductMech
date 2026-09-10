---
name: add-proteins-to-graphs
description: >-
  Add evidence-backed proteins, enzymes and complexes to NaturalProductMech
  biosynthetic pathways, causal graphs and molecular targets; ground graph
  nodes and pick UniProtKB protein examples without confusing a family, complex
  or reaction with an organism-specific protein.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Add proteins to pathways and causal graphs

Add protein participants to one existing `NaturalProductRecord`: biosynthetic
enzymes in `biosynthetic_pathway`, mechanism nodes in `causal_graphs`, or
evidence-backed examples in `molecular_targets.protein_examples`. The job is to
choose the correct level of identity before choosing an identifier: a specific
protein, a family, a protein complex, an enzyme reaction class, or an
ungrounded locus are different claims.

## Boundaries

- Resolve one record and one mechanism at a time. If the evidence names several
  congeners, several clusters, a host and a symbiont, or multiple target
  families, disambiguate before adding nodes.
- NaturalProductMech has no top-level `assembly_graphs` field. Biosynthetic
  assembly is represented by `biosynthetic_pathway` plus a
  `causal_graphs` item with `scope: BIOSYNTHESIS`.
- Add a protein only when the inspected paper or adopted database identifies
  a protein, gene, domain, enzyme function or complex involved with this exact
  compound. A genome neighborhood, antiSMASH prediction, docking model, or
  label similarity is a lead unless the graph edge is explicitly marked as
  computational or inferred.
- Do not pick a convenient Swiss-Prot homolog to make a node look grounded.
  UniProtKB examples must be the assayed, crystallized or genetically tested
  protein, or a deliberately chosen ortholog that is labelled as an example.
- Do not prefix PDB chains, RefSeq `NP_` accessions, GenPept accessions or
  locus tags with `UniProtKB:`. Confirm that each `UniProtKB:<accession>`
  resolves in UniProtKB and names the organism or sequence the claim needs.
- If a source gives only a PDB chain such as `1DE9_A`, use `PDB:1DE9` as
  structural evidence or a dataset link and map the chain to UniProt before
  selecting a protein example.
- EC and Rhea identifiers ground reactions, not proteins. InterPro identifiers
  ground families or domains, not exact proteins. ComplexPortal identifiers
  ground complexes, not their subunits.
- Biosynthetic enzymes are distinct from bioactivity targets. A synthase,
  tailoring enzyme or resistance determinant from the producer cluster is not
  a drug target unless the compound also engages it.
- Antimicrobial mechanism content for structures already linked to
  AntibioticMech stays in AntibioticMech. Link to the sibling mechanism rather
  than copying its targets, resistance proteins or MIC logic.
- Never create or edit a GitHub issue, PR, comment, discussion, email, form, or
  message without explicit authorization for that outbound action.

## Read first

- `CLAUDE.md` for generated-file boundaries and the guarded write path.
- `docs/CURATION.md` for claim-level evidence and `REVIEWED` semantics.
- `src/naturalproductmech/schema/naturalproductmech.yaml`, especially
  `PathwayStep`, `MolecularTarget`, `CausalGraph`, `CausalNode`, `CausalEdge`,
  `CausalGraphScopeEnum` and `CausalNodeTypeEnum`.
- `.claude/skills/curate-yaml-record/references/review-checklist.md` for the
  per-record audit standard.
- The full target YAML, not just `causal_graphs`.
- Any MIBiG, BindingDB, PubChem or curator evidence blocks that already mention
  the protein, target, assay organism, BGC accession or source paper.

## Establish the exact claim

Start from the paper or adopted database row and write down the smallest claim
it supports:

- **Biosynthetic assembly.** Which gene or enzyme changes which substrate into
  which product? Is the step experimentally demonstrated, proposed by sequence
  similarity, or inferred from the order of products in a pathway?
- **Bioactivity.** Does the compound bind or inhibit a specific protein, a
  protein family, a protein complex, a ribosome, a nucleic-acid target, a
  membrane or a process? Was the assay direct binding, enzymatic inhibition, a
  cellular readout, a structural complex, a pull-down, genetics, or docking?
- **Causality.** Which direction did the source show? "Compound binds target",
  "gene deletion abolishes production" and "product accumulates in a mutant"
  are different edge predicates and need separate edges if all are asserted.

Search exact accessions, locus tags and identifiers in the committed corpus
before declaring a grounding absent:

```bash
rg --hidden --no-ignore -n -F "<UniProt accession>" data data/raw curation .claude -g "!/.git" -g "!/.venv"
rg --hidden --no-ignore -n -F "<locus tag or gene name>" data data/raw curation .claude -g "!/.git" -g "!/.venv"
rg --hidden --no-ignore -n -F "<PMID, DOI, MIBiG accession or PDB id>" . -g "!/.git" -g "!/.venv"
```

Use exact fixed-string searches for labels with punctuation. A broad search for
`UniProtKB:` or a pathway stem does not prove absence.

## Choose a protein identity

Represent the biology at the level the source actually supports:

- Use `CausalNode.node_type: ENZYME` with `identifier: UniProtKB:<accession>`
  when one gene product is named and the graph is about that protein's action.
- Use `PathwayStep.enzyme_id: UniProtKB:<accession>` only when the source ties
  the step to that exact sequence or accession.
- Use `PathwayStep.enzyme_id: EC:<number>` when the reaction class is known but
  the producing organism's protein is not grounded.
- Use an `InterPro:<id>` node or pathway enzyme only for a family/domain claim,
  and say in `notes` that no organism-specific accession was chosen.
- Use `ComplexPortal:<id>` and `node_type: PROTEIN_COMPLEX` for a functional
  complex when the complex, rather than a single subunit, is the causal target.
- Leave `identifier` absent and `grounding_status: UNGROUNDED` when the paper
  only gives a locus label or provisional open reading frame with no defensible
  public protein identifier.
- Use `grounding_status: REVIEW_NEEDED` for a real ambiguity: multiple
  isoforms, paralogs in the same cluster, a species mismatch, a UniProt entry
  split/merge, or a PDB chain that maps to more than one sequence.

For `molecular_targets`, keep the target identity broad when the claim is broad.
`target_id` should denote the target family, complex or function where one can
be grounded; organism-specific UniProt accessions belong in `protein_examples`
as examples of that target, mirroring the BindingDB seeder's rule.

## Pick UniProt examples

Add a `UniProtKB:` value as an example only when it survives all checks:

1. The accession resolves in UniProtKB.
2. The entry organism matches the assay organism, producing organism, or the
   explicitly selected exemplar organism.
3. The gene, locus tag, protein name, sequence length, domain architecture or
   publication cross-reference links the entry to the inspected claim.
4. Isoforms, engineered mutants and truncated constructs are either represented
   by the canonical accession with the construct details in `notes`, or left
   ungrounded when the canonical sequence would be misleading.
5. The example adds information. A random human exemplar does not help a
   bacterial mechanism whose paper only says "DNA gyrase".

When several accessions pass, prefer the experimentally measured protein over
a curated ortholog, the exact producer strain over a type strain, Swiss-Prot
over TrEMBL only after organism and gene agree, and a primary accession over a
secondary one. Record a `Discussion` rather than hiding a paralog or isoform
choice that changes the mechanism.

## Author pathways and graphs

For `biosynthetic_pathway`:

- Order `PathwayStep.step_number` by the source pathway. Do not invent an order
  from gene order in a cluster unless the paper explicitly supports it.
- Put substrates and products on the step only when the exact intermediate is
  known. A hypothesized shunt product belongs in `notes` or a `Discussion`.
- Set `proposed: true` when the enzyme assignment is inferred.
- Give each step its own `evidence`, even when several adjacent steps cite the
  same paper.

For `causal_graphs`:

- Reuse existing nodes for the same entity inside a graph; do not duplicate a
  protein under one node id per edge.
- Keep `node_id` local and stable, such as `eryf`, `hsp90`, or
  `polyketide_chain_elongation`, rather than embedding a mutable label.
- Declare every node referenced by an edge.
- Use `scope: BIOSYNTHESIS` for precursor-to-product assembly and
  `scope: BIOACTIVITY` for compound-to-target-to-effect mechanisms.
- Put the citation on the `CausalEdge`, not only on the graph or node.
- State only the direction the evidence supports. A binding edge does not prove
  downstream cell death unless the paper connected those events.

## Write through the guarded path

Curator-authored protein, pathway and graph additions are local record changes,
but they still must be written by a mutator that loads the YAML, asserts the
expected identifier, appends a `record_curation_event`, and calls
`write_validated_natural_product`.

Use a `/tmp` mutator for one-off curation. Keep only reusable graph-building
code in `scripts/` or `src/`, with tests.

After writing the record, run at least:

```bash
just validate-strict <record-path> --out /tmp/naturalproductmech-protein-graph-validation.tsv
just verify-corpus --summary
```

If generated outputs changed or a site page should expose the graph, also run:

```bash
just render
just docs-stats
just qc
```

## Report

Report the record identifier and path, the mechanism scope, each protein or
complex added, how every identifier was grounded, which UniProtKB examples were
accepted or rejected and why, every edge and pathway step added, and every
validation command run. If no defensible UniProtKB accession exists, say that
directly and list the exact ignored-file-inclusive searches that established
the local absence.
