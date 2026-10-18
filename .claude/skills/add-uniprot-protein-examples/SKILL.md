---
name: add-uniprot-protein-examples
description: >-
  Review NaturalProductMech records and causal graphs to add verified
  UniProtKB protein examples and groundings for GENE, PROTEIN, ENZYME and
  PROTEIN_COMPLEX elements across inline causal_graphs, causal_graph_refs
  components, biosynthetic_pathway steps and molecular_targets.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Review records and add UniProtKB protein examples to causal graphs

Systematically audit `NaturalProductRecord` files (`data/natural_products/<np_pathway>/<slug>.yaml`)
and their exact-owner causal-graph components (`data/causal_graphs/<standard_inchi_key>/<graph_id>.yaml`)
to add verified, active `UniProtKB:<accession>` groundings and protein example
nodes for `GENE`, `PROTEIN`, `ENZYME`, and `PROTEIN_COMPLEX` elements, as well
as `biosynthetic_pathway` steps and curator-owned `molecular_targets.protein_examples`.

## Core principles and boundaries

- **Every `UniProtKB:<accession>` must be active and verified.** Confirm against
  `https://rest.uniprot.org/uniprotkb/<accession>.json` that `entryType` is
  active (not `"Inactive"` / obsolete), and verify organism, gene/locus tag,
  cross-references (EMBL/GenBank/RefSeq/PDB/ComplexPortal), and sequence length.
- **Preserve provenance boundaries.** Never collapse an engineered mutant,
  affinity-tagged fusion preparation, chimeric construct, or strain-specific
  `NCBIProtein:` reference into a canonical `UniProtKB:` identifier when the
  graph explicitly distinguishes them. Instead, add a distinct grounded
  `UniProtKB:` reference or example node and connect it with an explicit edge.
- **Never hand-edit YAML files.** Mutate owner records exclusively through
  `naturalproductmech.curate.curation_event.record_curation_event` and
  `naturalproductmech.io.validated_write.write_validated_natural_product`, and
  component graphs through `write_validated_graph_bundle`.
- **Keep both owners and components under the 64-KiB review limit** (65,536 bytes).
- **Do not mutate seeder-owned fields** (`occurrences`, `producer_organisms`,
  `biosynthetic_gene_clusters`, `bioactivities`, or `molecular_targets` with
  `source: PUBCHEM` / `BINDINGDB`) in ways that fail `just verify-reproduction`.
- **Never perform unauthorized outbound actions** (no GitHub issues, PRs,
  comments, emails, or external posts).

## Step 1: Inventory candidate records and causal graphs

Scan both inline `causal_graphs` and external `causal_graph_refs` components
(via `read_natural_product(path)` for inspection, raw YAML for edits) to find:

1. Causal graphs containing `GENE`, `PROTEIN`, `ENZYME`, or `PROTEIN_COMPLEX`
   nodes with zero `UniProtKB:` nodes in the graph.
2. Individual `GENE`, `PROTEIN`, `ENZYME`, or `PROTEIN_COMPLEX` nodes that are
   `UNGROUNDED`, grounded to `NCBIProtein:<accession>`, or grounded to
   `ComplexPortal:<id>` without a linked `UniProtKB:<accession>` node.
3. `biosynthetic_pathway` steps lacking `UniProtKB:` in `enzyme_id` where a
   verified enzyme sequence is known.

Before modifying any record, check `tests/` for record-specific regression tests
(e.g., `tests/test_lomaiviticin_curation.py`) and read existing graph
`description`, node `notes`, and `discussions` to respect documented negative
verifications or unresolved sequence identities.

## Step 2: Resolve candidate proteins against UniProtKB and UniParc

For each candidate gene, protein, enzyme, or complex:

1. **Exact INSDC / RefSeq protein lookup**:
   Query `https://rest.uniprot.org/uniprotkb/search?query=xref:embl-<GenPept_without_version>`
   or `query=<GenPept_or_RefSeq_accession>` to check if an active UniProtKB
   entry directly indexes the deposited protein.
2. **UniParc exact-sequence lookup (when the native strain entry is unindexed or obsolete)**:
   Query `https://rest.uniprot.org/uniparc/search?query=<GenPept_or_RefSeq_accession>`
   and inspect `uniParcCrossReferences` for active `UniProtKB/Swiss-Prot` or
   `UniProtKB/TrEMBL` cross-references (`active: true`) sharing 100% sequence
   identity (`upi`).
3. **Gene / locus / BGC / organism lookup**:
   Query `https://rest.uniprot.org/uniprotkb/search?query=gene:<gene>+AND+<organism_or_accession>`
   or search the corpus (`data/`, `data/raw/`, `curation/`) for sibling graphs on
   the same record that already ground the native parent protein to `UniProtKB:`.
4. **ComplexPortal subunit lookup**:
   For `ComplexPortal:CPX-...` nodes, fetch `https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-...`
   or query UniProtKB `xref:complexportal-CPX-...` to identify the exact
   constituent `UniProtKB:<accession>` subunit proteins.

## Step 3: Apply the appropriate causal-graph grounding pattern

Choose one of four patterns depending on what the existing node represents:

### Pattern A: Direct `UniProtKB:` grounding on the node
Use when an `UNGROUNDED` or `NCBIProtein:` node represents the canonical native
protein in that exact organism/strain, an active `UniProtKB:<accession>` entry
directly indexes that exact sequence/deposit, and no provenance note requires
keeping `NCBIProtein:` as the primary `identifier`:
- Set `identifier: UniProtKB:<accession>` and `grounding_status: GROUNDED`.
- Preserve the GenPept/RefSeq accession, nucleotide accession, and locus tag in
  `notes`.

### Pattern B: Sequence-identical or orthologous UniProtKB protein example node
Use when a node is a `GENE` locus or a native `NCBIProtein:<accession>` whose
exact strain deposit is unindexed or obsolete in UniProtKB, OR when keeping the
versioned `NCBIProtein:<accession>` node is required for INSDC provenance, and an
active `UniProtKB:<accession>` entry exists with an identical sequence (via
UniParc) or as a verified orthologous reference protein example:
- Keep the existing `GENE` or `NCBIProtein:` node intact.
- Add a companion `PROTEIN` or `ENZYME` node with `identifier: UniProtKB:<accession>`
  and `grounding_status: GROUNDED` (e.g., `node_id: <stem>_uniprot_example`,
  `label: <Name> (<Strain/Organism> UniProtKB example)`).
- Connect them with a `CausalEdge`:
  - `predicate: has a sequence-identical UniProtKB example` (when sharing the
    same UniParc UPI / 100% sequence identity), or
  - `predicate: has a UniProtKB protein example` (when linking a `GENE` locus or
    a verified reference strain ortholog with stated sequence identity in `notes`).
- Attach `DATABASE_ASSERTION` (or `CURATOR_INFERENCE` when sequence comparison is
  involved) evidence citing `https://rest.uniprot.org/uniprotkb/<accession>.json`
  and stating the UniParc UPI or alignment identity in `notes`.

### Pattern C: Native `UniProtKB:` reference node for engineered/mutant/assay preparations
Use when a graph (often a `causal_graph_refs` component) models recombinant
tagged preparations (`His6`, `MBP`, `GST`, `TrxA`), point mutants, chimeric
fusions, or cell-lysate preparations as `UNGROUNDED` / `REVIEW_NEEDED` nodes:
- Keep the preparation/mutant nodes `UNGROUNDED` (or `REVIEW_NEEDED`) so recombinant
  constructs are not conflated with wild-type native proteins.
- Add the canonical wild-type `ENZYME` or `PROTEIN` node grounded to
  `UniProtKB:<accession>` (`grounding_status: GROUNDED`, e.g.,
  `node_id: <protein>_native_reference`, `label: Native <Protein> reference (<UniProtKB>)`).
- Add a `CausalEdge` from the native reference node to the wild-type comparator
  or representative construct node (`predicate: is the native protein reference for`),
  citing `https://rest.uniprot.org/uniprotkb/<accession>.json` (`DATABASE_ASSERTION`).

### Pattern D: Constituent `UniProtKB:` subunit nodes for `PROTEIN_COMPLEX` nodes
Use when a `PROTEIN_COMPLEX` node (`ComplexPortal:<id>` or an ungrounded complex
whose subunits have active `UniProtKB:` entries) appears without subunit nodes:
- Add `PROTEIN` or `ENZYME` nodes for each verified subunit with
  `identifier: UniProtKB:<accession>` and `grounding_status: GROUNDED`.
- Connect each subunit node to the `PROTEIN_COMPLEX` node with a `CausalEdge`
  (`predicate: is a subunit of`), citing the ComplexPortal and/or UniProtKB record.

## Step 4: Write through the guarded path and validate

1. Load raw owner YAML (`data/natural_products/...`) or component YAML
   (`data/causal_graphs/...`), append a `CurationEvent` via `record_curation_event`,
   and write via `write_validated_natural_product` or `write_validated_graph_bundle`.
2. Ensure top-level key order places `curation_history` last on owner records.
3. Run the full verification suite:
   ```bash
   uv run python scripts/validate_strict.py --all --out /tmp/validate-strict.tsv
   uv run python scripts/verify_corpus.py --summary
   uv run python scripts/check_reproduction.py --summary
   uv run python scripts/render_pages.py
   uv run python scripts/check_docs.py --write
   uv run python scripts/run_qc.py
   uv run pytest
   ```
