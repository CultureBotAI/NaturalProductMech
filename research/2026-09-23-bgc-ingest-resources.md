# Biosynthetic-gene-cluster resources NPMech can ingest

Research date: **2026-09-23**. This is a follow-up to
`research/2026-09-07-np-biosynthesis-bgc-sources.md`, focused on BGC resources
that were missing from the first sweep or changed materially since then.

**Bottom line:** MIBiG remains the only broadly ingestible source that says
"this exact natural-product structure is produced by this characterized BGC in
this named organism." The new useful sources split into two different jobs:

1. **Pathway/protein enrichment for MIBiG-backed records**: MITE and NPdia.
2. **Computed BGC atlas context**: BGC Atlas v2 and SMC.

The first class can help fill NPMech's nearly empty pathway/causal-graph layer.
The second can say where predicted homologous BGCs occur, but should stay
reference-only unless a curator turns a similarity hit into a source-backed
compound claim.

## Current NPMech gap

`just report`, run locally on 2026-09-23:

| Field | Records |
|---|---:|
| total records | 3,115 |
| records with `biosynthetic_gene_clusters` | 3,115 |
| records with `biosynthetic_pathway` | 1 |
| records with `causal_graphs` | 27 |
| records with `molecular_targets` | 14 |

That changes the source priority. Another atlas of predicted antiSMASH regions
does not close the biggest gap because every current record already has a
MIBiG-derived locus. Sources that supply enzyme/residue/intermediate detail on
top of a BGC are more valuable now than sources that discover millions of new
predicted neighborhoods without compound identities.

## Recommended queue actions

| Source | Action | Why |
|---|---|---|
| **MITE** | Add as P2 `biosynthetic_pathway`, `CC0_OK`, `BOTH` | Expert-reviewed CC0 tailoring-enzyme reactions, with substrate/product SMILES, FASTA, reaction SMARTS, and a Zenodo-pinned `mite_data` archive. |
| **NPdia** | Add as P2 `biosynthetic_pathway`, `ATTRIBUTION`, `UNVERIFIED` access | Domain-resolved T1PKS/NRPS pathway steps keyed directly by MIBiG accession under CC BY 4.0; the live download page lists CSV/JSON/GenBank files but the buttons are disabled. |
| **BGC Atlas v2** | Add as P5 `biosynthetic_gene_clusters`, `ATTRIBUTION`, `BULK` | Modern CC BY successor to the stale BiG-FAM use case, with BGC/GCF tables and per-BGC taxonomy/environmental metadata at 16.5M-region scale. Reference-only. |
| **SMC** | Add as P5 `biosynthetic_gene_clusters`, `UNVERIFIED`, `API` | JGI's large live BGC portal has 13.16M BGC rows and compound-name search; no redistribution grant or current relational bulk dump was found. |
| **FunBGCs/FunBGCeX** | Add as P5 `biosynthetic_gene_clusters`, `UNVERIFIED`, `BULK` | Useful fungal curation lead, but its Zenodo record is `other-open` and not an explicit CC0/CC BY grant. |

No source below should be moved to `ADOPTED` from this report alone. MITE is the
only one whose licence/access profile is clean enough today for a real extractor
PR without an upstream ask.

## Per-source findings

### 1. MIBiG 4.0

**Decision:** already adopted; mine more from it before adding a second
compound-BGC source.

The September sweep settled MIBiG 4.0: it is CC BY 4.0, small, bulk,
expert-curated, and already carries the compound to BGC to producer backbone
this corpus admits. What remains locally is not source discovery but extractor
deepening:

- `mibig_gbk_4.0.tar.gz` contains the per-region GenBank files.
- `mibig_prot_seqs_4.0.fasta` contains proteins for mapped BGC genes.
- `biosynthesis.modules[]` already has domain-to-protein accessions for modular
  PKS/NRPS entries.

For M6, those three pieces are enough to populate many assembly-graph nodes with
GenBank protein accessions. UniProt grounding still needs mapping; MIBiG protein
IDs are GenPept/RefSeq-style accessions, not UniProtKB accessions.

**NPMech ingestibility:** keep `mibig` as the source of record for native
compound/BGC links; add pathway and protein extraction around the files we have
already licensed rather than looking for another anchor.

### 2. MITE

**Decision:** add to the queue as `SEED` for `biosynthetic_pathway`.

MITE, the Minimum Information about a Tailoring Enzyme database, is an
expert-curated, community-submitted repository for secondary-metabolite
tailoring enzymes. Its own About page states that entries collect
experimentally verified metadata; each entry represents a single,
non-redundant enzyme-encoding gene and one or more associated reactions. Each
reaction has SMARTS, one or more substrate/product SMILES examples, taxonomy,
cofactors, and a primary-literature basis.

**Live access checked 2026-09-23:**

- home: `https://mite.lisc.univie.ac.at/`
- current website footer: `MITE Data v1.30`
- active/retired overview: `https://mite.lisc.univie.ac.at/download/overview`
- Zenodo concept: `https://zenodo.org/records/13294303`
- latest Zenodo record resolved from the concept API:
  `mite-standard/mite_data-1.30.zip`, DOI `10.5281/zenodo.21432238`,
  2026-07-18, licence `cc-zero`
- export endpoints present:
  - `/download/overview`
  - `/download/smarts`
  - `/download/smiles`
  - `/download/fasta`

The overview CSV served 468 `MITE0000###` accessions in the 2026-09-23 live
request, through `MITE0000468`, including retired entries. The source is small
enough to vendor.

**Licence:** CC0 for `mite_data`. The footer says all displayed data is CC0, and
the Terms of Use state that displayed data is part of the public domain and
released under CC0. The Zenodo API for the current archive reports
`license.id = "cc-zero"`.

**What it can fill:** MITE can provide experimentally characterized tailoring
enzyme nodes and reactions for `biosynthetic_pathway` and `causal_graphs` after
an existing natural-product record has been selected. It is especially useful
for the add-proteins workflow because its entries carry protein sequences via
FASTA and reaction examples via SMILES.

**What it cannot fill:** MITE intentionally excludes core scaffold synthases,
gatekeeper enzymes, transporters, and resistance proteins. It is not a
compound-origin source and must not mint new natural-product records by itself.

**Join strategy:** start with MIBiG/Wikidata cross-links where present. If a
MITE enzyme has no MIBiG link, join to an existing record only through an exact
curated DOI plus pathway-name match, not through an enzyme name such as `P450`
or a fuzzy compound string.

### 3. NPdia

**Decision:** add to the queue, but leave access unverified until downloads are
actually reachable.

NPdia, the NRPS/PKS biosynthesis pathway encyclopedia, is the right conceptual
shape for NPMech M6. The live homepage describes a manually curated database of
Type I PKS and NRPS pathways from Actinomycetota with step-by-step SMILES for
every biosynthetic intermediate, and explicit gene-to-reaction/module-level
annotations. The help page documents the important join key: every entry carries
the **MIBiG BGC identifier**.

**Live size on 2026-09-23:**

| Counter | Value |
|---|---:|
| BGC entries | 448 |
| T1PKS clusters | 211 |
| NRPS clusters | 153 |
| PKS-NRPS hybrid clusters | 84 |
| biosynthetic reactions | 7,323 |
| producing organisms | 347 |
| biosynthetic genes | 11,960 |
| domain annotations | 19,006 |

**Licence:** the site footer states CC BY 4.0.

**Access problem:** `/download` lists three v1 files:

- `T1PKS_NRPS_pathways_v1.csv`
- `biosynthesis_pathways_v1.json`
- `GenBank_Files_v1.zip`

However, all three buttons were rendered as disabled spans on 2026-09-23, not
as anchors with `href` targets. The "Repository" tab was also disabled. The data
is therefore **licensable but not yet manifestable**: there is no URL to put in
`data/raw/MANIFEST.yaml`.

**NPMech ingestibility:** high once the JSON/CSV is reachable. MIBiG IDs give a
clean join to already-adopted loci; Product IDs and intermediate SMILES let us
build ordered `PathwayStep` records; blank or partial intermediates must stay
blank rather than being inferred.

### 4. BGC Atlas v2

**Decision:** add as the best open, modern broad-atlas reference; keep
BiG-FAM as stale historical context.

BGC Atlas v2 is now a much better fit for the "BiG-FAM but current" use case.
The current site exposes bulk downloads and documents a 2026-09-19 table
snapshot with:

| Table/counter | Rows |
|---|---:|
| `bgcs` | 16,491,574 |
| published non-redundant BGC corpus | 16,449,773 |
| `gcfs` | 764,320 |
| `bgc_gcf` | 19,254,436 |
| `gcf_mibig_anchor` | 2,067 |
| `bgc_taxonomy` | 16,386,489 |
| `taxonomies` | 266,571 |
| `samples` | 863,831 |
| `studies` | 53,240 |

The download page includes TSV and Parquet bundles for 42 tables:

- `bgc_atlas_v2_tables_tsv.tar.gz`
- `bgc_atlas_v2_tables_parquet.tar.gz`

and a sequence archive:

- `all_regions_gbk.tar.gz`, 163.5 GB, updated 2026-07-06
- `regions_nuc.fasta`
- `regions_prot.faa`
- `bgc_uuid_source.tsv.gz` / `.parquet`

The database uses metaSMASH 1.0.3 for metagenome-scale BGC calling and
BiG-SLiCE 2.0.2 for GCF clustering. Its About page states that BGC Atlas'
derived cluster annotations, family assignments, taxonomy, and harmonised
environmental metadata are CC BY 4.0. It also correctly scopes that grant: the
underlying assemblies and genomes remain under their source repositories' terms.

**NPMech ingestibility:** reference only. `gcf_mibig_anchor` can tell us which
predicted families have a MIBiG cluster as an anchor and which metagenome/MAG/SAG
regions look related. That is a hypothesis about homologous biosynthetic
capability, not a compound-to-producing-taxon assertion, and metagenomic
assemblies frequently lack a named isolate-level producer. Do not attach an
environmental MAG as a `producer_organism`.

**Why this supersedes BiG-FAM:** BiG-FAM was frozen on February 2020 source
snapshots and MIBiG 2.0. BGC Atlas v2 exposes 2026 downloads, antiSMASH 8-era
annotations, per-BGC GTDB taxonomy, and a MIBiG-anchor table.

### 5. Secondary Metabolism Collaboratory

**Decision:** add as a reference candidate with unverified redistribution terms.

JGI's Secondary Metabolism Collaboratory is a large live portal over predicted
BGCs. On 2026-09-23 the home page reported SMC v1.3.0; the statistics page
reported:

| Counter | Value |
|---|---:|
| genomes and other DNA sources | 1,359,747 |
| BGCs | 13,162,471 |
| BGCs with compound identified | 24,440 |
| BGC classes | 87 |
| BGC annotation tracks | 61,825,169 |
| genes and domains | 2,116,233,889 |

This is potentially a source of BGC/gene context at the same scale as BGC Atlas
with richer portal interaction: it can search by compound name, genome or
accession ID, SMC/BGC/gene ID, taxonomy, collection, BLAST, and advanced query.

**Access:** API/search, plus a stale project archive. `/projects/` has two
October 2023 FASTA downloads, `smc_blast-20231025.fasta.gz` at 67 GB and
`smc_blastp-20231025.faa.gz` at 45 GB, but no current relational snapshot. A
commented-out 2025 "Bulk SMC Download" block points to a 5.6 TB JGI Data Portal
dataset, so a current dump may exist behind JGI infrastructure rather than on
the public SMC downloads page.

**Licence:** unverified. The pages checked carried a UC/JGI copyright footer,
but not CC0, CC BY, or a database redistribution grant.

**NPMech ingestibility:** reference and curation leads only until terms are
resolved. "BGCs with compound identified" is promising, but compound-name search
is not the same thing as a structure-keyed Standard InChIKey join or an
experimentally demonstrated BGC/product link.

### 6. FunBGCs / FunBGCeX data

**Decision:** add as a fungal reference candidate under unverified terms.

FunBGCs/FunBGCeX is a fungal-BGC curation resource and benchmark dataset. Its
Zenodo data record (`10.5281/zenodo.8126803`, 2023-07-08) describes the archive
as "manually curated fungal biosynthetic gene clusters (BGCs) and custom-made
HMM profiles" and links to `ydmatsd/funbgcex-data` at tag `v0.0.0`. The archive
is bulk downloadable from Zenodo and about 16 MB, so access is tractable.

**Licence:** not ingestible yet. The Zenodo API reports `license.id =
"other-open"` rather than `cc-zero`, `cc-by-4.0`, MIT, or another concrete open
grant. The CityU website returned "You do not have permission to view this
directory or page" for the root URL on 2026-09-23.

**NPMech ingestibility:** fungal curation lead, not automatic seeding. The
resource was built to improve fungal BGC prediction, not to assert exact natural
product structures per BGC under a redistributable licence.

### 7. antiSMASH-DB, BiG-FAM and PoDP

**Decision:** leave existing rows candidate/reference.

The September decision still stands:

- **antiSMASH-DB**: large predicted-BGC reference, no compound structures and no
  data licence found.
- **BiG-FAM**: CC BY 4.0 but stale, built on 2020 snapshots and MIBiG 2.0.
- **Paired Omics Data Platform**: CC BY 4.0 and conceptually ideal because it
  links BGCs to spectra, but tiny at 117 BGC-MS/MS links in the September live
  check.

BGC Atlas v2 is the resource that changes the priority of `bigfam`, not a
reason to reanimate the stale BiG-FAM bulk download.

### 8. Tool-like or blocked resources not queued

These are useful to know about but were not worth a queue row from this pass:

| Resource family | Decision |
|---|---|
| BAGEL4 / bacteriocin and RiPP miners | Tool/server style; no verified CC0/CC BY bulk set of structure-linked BGC assertions found. |
| PRISM / RODEO / ARTS | Prediction tools and resistance/mining aids; no redistributable structure-keyed BGC assertion corpus found. |
| IMG-ABC | JGI/IMG BGC content is now better represented operationally by SMC; no separate open, versioned IMG-ABC bulk export with explicit CC BY/CC0 terms was found in this pass. |
| human, ocean, reef metagenome BGC atlases | Reference-only by construction unless they name an isolate producer and a compound. Broad metagenome atlases are now subsumed for NPMech purposes by BGC Atlas v2's public input collections and SMC. |
| KEGG / MetaCyc | Still blocked by restrictive terms from the September sweep. |

## Practical adoption order

1. **MITE canary extractor.** Read the Zenodo v1.30 archive, count exact MIBiG
   cross-links and exact NPMech record joins, then seed only one or two
   `biosynthetic_pathway`/`causal_graphs` examples that the
   `add-proteins-to-graphs` skill can audit end-to-end.
2. **NPdia availability check.** Wait for clickable CSV/JSON/GenBank downloads
   or ask KAIST for the v1 files. Do not scrape the disabled UI or reconstruct
   the data from HTML.
3. **BGC Atlas probe.** Download only the TSV table bundle, not the 163.5 GB
   GenBank archive, and measure how many current NPMech MIBiG accessions appear
   in `gcf_mibig_anchor`.
4. **SMC licence ask.** Ask whether the 13.1M BGC dataset and the 24,440
   compound-identified rows are redistributable under CC BY 4.0-compatible
   terms, and whether a current relational export exists outside the web/API.
