# Natural-product data sources: licence and quality landscape

Consolidated deep-research report, 2026-09-07. Four research agents covered
four clusters of the source landscape, each fetching the primary pages —
licence pages, download indexes, APIs, release files and papers — rather than
summaries, and in several cases downloading and parsing the actual release
data. The cluster reports are kept verbatim beside this one and are the
authority for detail:

- [np-structure-occurrence-sources](2026-09-07-np-structure-occurrence-sources.md)
  — COCONUT, LOTUS, NPAtlas, NPASS, CMNPD, KNApSAcK, StreptomeDB, CyanoMetDB,
  NPBS, UNPD, SuperNatural, NuBBE, ChEBI, and the proprietary compendia.
- [np-biosynthesis-bgc-sources](2026-09-07-np-biosynthesis-bgc-sources.md)
  — MIBiG, antiSMASH-DB, BiG-FAM, Norine, Paired Omics Data Platform, GNPS,
  NP-MRD, MoNA, MassBank, NPClassifier, ClassyFire, MetaCyc, KEGG, Rhea.
- [np-knowledge-graph-sources](2026-09-07-np-knowledge-graph-sources.md)
  — NP-KG (Taneja et al.), the NaPDI Center, PheKnowLator, ENPKG, and the
  general biomedical knowledge graphs.
- [np-bioactivity-target-sources](2026-09-07-np-bioactivity-target-sources.md)
  — ChEMBL, BindingDB, PubChem BioAssay, NPASS activities, DrugBank,
  DrugCentral, IUPHAR, Open Targets, and the ethnopharmacology resources.

This report is evidence for a curator, never automatic input. It exists to be
folded into `curation/source_queue.tsv` by the `source-queue` skill — one row
at a time, with the licence column moved off `UNVERIFIED` only where a report
quotes the licence page itself.

## Summary

For a CC BY 4.0, one-structure-per-record natural-product knowledge base, the
landscape splits on licensing far more sharply than on content, and the best
content is disproportionately on the wrong side of the line.

**Six sources can seed Phase A**, each with its licence text quoted from the
primary page and verified live on 2026-09-07:

| Source | Licence | What it closes |
|---|---|---|
| MIBiG 4.0 | CC BY 4.0 | producers with NCBI taxid, gene clusters with GenBank loci and an experimental-evidence vocabulary, cluster class, references |
| ChEBI release 255 | CC BY 4.0 | identity, structures, specialized-metabolite roles |
| LOTUS via Wikidata | CC0 | 674,454 structure–organism–reference occurrence triples |
| NPClassifier | CC0 (models, ontology and data; MIT code) | the filing classification, computable from structure alone |
| PubChem | public domain, per-source conditions respected | structures for concepts the others name without one |
| CyanoMetDB v3 | CC BY 4.0 | ~3,085 manually curated cyanobacterial metabolites with producer and primary reference |

**The exclusions hurt more than usual in this domain.** NPAtlas is the
best-curated microbial occurrence resource in existence, its API returns an
NCBI taxid with both a DOI and a PMID for every compound, and it moved to
CC BY-NC at release 2024_09. Norine is the definitive nonribosomal-peptide
resource and is CC BY-NC-SA. NP-MRD, CMNPD and NPBS Atlas are all
NonCommercial. KNApSAcK forbids redistribution outright. ChEMBL, the strongest
normalized bioactivity resource, is share-alike. MetaCyc costs at least five
thousand dollars and KEGG states plainly that it is not a public database.

**Two findings change the design**, and both were only visible because an agent
parsed the actual release rather than reading about it.

First, **MIBiG's obvious quality signals are not quality signals.** Its
`quality` field reads `questionable` for 2,710 of 3,013 entries, and the MIBiG
4.0 paper says that label marks legacy-format entries awaiting re-curation, not
doubtful science. Its changelog reviewer id is the placeholder `AAAA…` in 2,988
of 3,013 entries. AntibioticMech's MIBiG extractor gates on a non-placeholder
reviewer, which is defensible there because it wanted a tiny high-confidence
slice; carried over here unchanged it would admit 25 entries out of 3,013. The
gate that does work is per-locus: `loci[].evidence[].method` is a controlled
vocabulary, and its distribution across the release is knockout studies 542,
heterologous expression 638, enzymatic assays 284, expression correlated with
production 219, genomic–metabolomic correlation 82, in-vitro expression 25, and
homology-based prediction 31. Everything but the last is producer-grade
evidence. That is the mapping `conf/producer_evidence.tsv` should carry.

Second, **COCONUT's CC0 banner does not survive contact with its own
collections column.** Its download page states the data is released under CC0
"without any restrictions"; its README states that every source comes with its
own licence and must be reviewed individually. Tallying the collections column
across all 738,827 rows shows the README is right: 47,475 rows tagged KNApSAcK,
whose terms forbid redistribution; 81,801 tagged NPASS, which states no licence
anywhere; 34,748 tagged NPAtlas under CC BY-NC; 30,700 tagged CMNPD under
CC BY-NC-SA. A dataset-level licence claim does not relicense the rows inside
it. COCONUT can only be adopted by filtering to verified-open collections, and
even then it cannot supply referenced occurrences, because its organism and DOI
columns are unpaired lists on the compound row.

**The recurring trap across all four clusters** is the same one, and it caught
several resources: *an open-access article licence is not a database licence.*
StreptomeDB, NPBS Atlas and SuperNatural all publish CC BY or CC BY-NC papers
over data that is differently licensed or unlicensed. antiSMASH-DB's CC BY
article says nothing about its dumps, which carry no data licence at all. The
queue's `verified_on` column therefore means one specific thing: the database's
own terms page was read on that date.

## Verified findings

### 1. MIBiG 4.0 is the anchor, and it is the only source with a machine-readable producer-evidence grade

**Confidence: high.** Verified by downloading and parsing all 3,013 files in
`mibig_json_4.0.tar.gz`, plus the live API and the paper.

MIBiG is the only resource carrying an expert-curated compound → gene cluster →
producer organism triple with an explicit experimental-evidence qualifier.
Every one of the 3,013 entries carries a `taxonomy.ncbiTaxId`. Loci carry
GenBank or RefSeq accessions with coordinates. Compounds carry SMILES, evidence
of structure determination (NMR 1,234, mass spectrometry 550, MS/MS 237, X-ray
39, total synthesis 34) and bioactivity labels. Nothing in it is machine
predicted; all content is human curated.

Licence, quoted verbatim from the paper's data-availability section
(<https://pmc.ncbi.nlm.nih.gov/articles/PMC11701617/>):

> "All data are freely available with no restrictions for academic and
> commercial reuse under the OSI-approved CC BY 4.0 Open Source license"

The site footer carries the same, with `rel="license"` pointing at CC BY 4.0.
Worth recording: the `mibig-json` GitHub repository has no LICENSE file, so the
claim rests on the website and the paper. That is adequate but it is not a
third confirmation.

What the extractor must handle:

- **No InChI or InChIKey field exists anywhere in the JSON.** Standard
  InChIKeys are generated locally from SMILES with the pinned RDKit. Of 5,443
  compound records, 4,401 have a SMILES; 1,042 have neither structure nor
  database id and are often class-level names.
- **377 retired entries ship in the dump** and must be filtered on `status`.
- **`completeness` is `unknown` for 2,132 entries.**
- **Schema drift inside one release**: `bioactivities[].name` appears both as a
  bare string and as an object. A parser must handle both.
- **`alkaloid` is no longer a biosynthetic class.** MIBiG 4.0 separated
  biosynthetic classification from compound classification and removed it. The
  cluster vocabulary is exactly six values: PKS 1,238, NRPS 1,020, ribosomal
  447, other 421, terpene 241, saccharide 216.
- **Three counts disagree** — 3,059 in the paper, 3,015 from the live API,
  3,013 in the 4.0 dump — because the live site now runs a `4.0alpha1` build.
  Pin the dump and record which.

Cross-references, counted across all compounds: NPAtlas 2,167, PubChem 1,614,
ChemSpider 184, ChEBI 87, CyanoMetDB 68, ChEMBL 56, LOTUS 11. The ChEBI overlap
is small, which means most MIBiG compounds will need minted identifiers.

### 2. LOTUS is the occurrence backbone, and the route decides the licence

**Confidence: high.** Verified by downloading and measuring the current frozen
export.

The 2026-04-13 export holds **674,454 structure–organism–reference triples**
over **227,319 unique Standard InChIKeys**, **37,486 organism Wikidata QIDs**
and **91,382 reference DOIs**; 175 rows carry no DOI. The metadata table adds
InChI, SMILES, PubChem CID, NCBI taxid, GBIF id, OTT id, a full rank ladder,
and NPClassifier terms. For joinability to a structure-keyed corpus this is the
best in the entire landscape.

Two licence routes with two different answers. Wikidata's licensing page states
verbatim that "All structured data in the main, property and lexeme namespaces
is made available under the Creative Commons CC0 License", and LOTUS's homepage
states "The LOTUS data is available under CC0 licence". But the Zenodo frozen
export record is tagged `cc-by-4.0`. Both are compatible with a CC BY 4.0
release; take the Wikidata route for CC0 cleanliness and cite Rutz et al.
either way.

Two cautions. The `manual_validation` column is present but **empty in all
674,454 rows**, so no hand-curated subset can be selected — treat every pair as
automatically validated, which the paper describes as rule-based validation
with manual spot-checking (~97% true positives on a 100-entry test). And the
`lotus.naturalproducts.net` mirror is documented as unmaintained and being
phased out; do not build against it.

Because LOTUS inherits from literature-mined upstreams including the defunct
UNPD, extract-versus-constituent confusion and misattributed producers persist
at some rate. This is precisely why LOTUS rows land in `occurrences` and never
in `producer_organisms`.

### 3. NPClassifier is the right filing vocabulary, and it is CC0

**Confidence: high.** Ontology counted from the repository; licence quoted from
the README; API tested live.

NPClassifier takes a SMILES and returns pathway, superclass and class:
**7 pathways, 77 superclasses, 687 classes**. The seven pathways are Alkaloids;
Amino acids and Peptides; Carbohydrates; Fatty acids; Polyketides; Shikimates
and Phenylpropanoids; Terpenoids. The README states verbatim:

> "The license as included for the software is MIT. Additionally, all data,
> models, and ontology are licensed as CC0."

That makes it the only open, biosynthesis-oriented, structure-computable
classification available, which is why the plan files records by NPClassifier
pathway rather than by MIBiG's cluster class: every record has a structure, but
most records will never have a gene cluster. Its outputs are predictions and
must be stored with the model version; it returns arrays, so a record can carry
several labels per level.

The alternative, ChemOnt via ClassyFire, is refused: its terms require
permission for commercial redistribution. That has a downstream consequence
worth stating — MassBank records are CC BY and contain ChemOnt strings, so the
safe default is to drop those strings and keep NPClassifier.

### 4. ChEBI supplies identity and the role allow-list, but not producers

**Confidence: high.** Counted directly from `chebi.obo`.

Release 255 holds 218,768 terms. In the metabolite role subtree, 16,362
entities carry a role, of which 3,588 plant, 1,964 bacterial, 1,794 fungal and
505 marine. Licence CC BY 4.0, quoted from the about page.

The limitation is structural: ChEBI has **no organism field and no taxid**.
Producer information is encoded in role labels and definition prose. So ChEBI
admits a compound to the corpus and grounds its identity, but rarely supplies a
producer claim. The role allow-list in `conf/np_roles.tsv` is therefore the
scope decision, and it must exclude the bare `metabolite` roles — those would
admit glucose and ATP.

### 5. The best occurrence resource is licence-blocked, and the second best has no licence at all

**Confidence: high** for both licences; quoted from their own terms pages.

NPAtlas terms page, verbatim: "Data downloaded from the Natural Products Atlas
is licensed under a Creative Commons Attribution-Noncommercial 4.0
International License." The 3.0 paper confirms the change began with release
2024_09 and directs commercial users to email for permission. Releases through
2024_03 were CC BY 4.0 and would be seedable if the specific older Zenodo
version's licence field is verified — a real option worth pricing, because
NPAtlas is 36,545 curated microbial compounds with NCBI taxids, DOIs and PMIDs,
and because it models structure reassignments and maintains an excluded-records
file that a naive ingest would miss.

NPASS is version 3.0 (2025-06-15) with 204,023 natural products, 48,940 source
organisms and 1,048,756 activity records. Its homepage, about page and download
page were all checked and **none carries any licence, copyright or terms
statement**. A third-party registry records CC-BY-NC; that is not the
maintainers' word. Unverified is not permission.

StreptomeDB 4.0 is the same shape: 8,552 natural products, 3,888 producer
strains, 7,630 curated articles, manually curated compound–organism–reference
links — and no licence on the site, with an "All Rights Reserved" footer over a
CC BY paper. Both StreptomeDB and antiSMASH-DB are worth an explicit ask; the
antiSMASH team also maintains MIBiG under CC BY.

### 6. NP-KG carries no chemical structures, and its licence is the most restrictive of its inputs

**Confidence: high** on the structure finding, computed directly from the
primary OWL and TSV files; **medium** on one licence link, noted below.

NP-KG was the specific resource this research was asked to assess, so the
finding matters: **it cannot seed a structure-keyed corpus, because it does not
identify natural products as structures at all.**

Version 3.0.0, June 2024, 1,089,139 nodes and 7,836,115 edges. (The widely
cited 745,512-node figure is the 2023 paper's earlier build.) Its entire
natural-product layer is a 651-class OWL extension:

- **613 phytoconstituents**, of which 460 map to a ChEBI class and **153 carry
  only a minted `napdi.org` name URI whose sole superclass is `CHEBI:24431`,
  "chemical entity"** — a lowercased name with no chemical parent of any
  information content.
- 68 plant or plant-part entities under `PO:0025131`, linked to 34 NCBI
  Taxonomy identifiers.
- 716 plant-has-component-constituent edges.
- **No InChI, InChIKey, SMILES, PubChem CID, UNII, CAS or formula anywhere**,
  confirmed by grep over the extension file.

So every join from NP-KG to a structure runs through ChEBI, and only for the
460 constituents that received a ChEBI id — which this corpus can obtain from
ChEBI directly. The 153 name-only constituents are precisely the compounds
ChEBI lacks, and NP-KG adds nothing about them beyond a name string and a plant
association.

The licence position is the second reason. The Zenodo dataset is stamped
CC BY 4.0 and the code is Apache-2.0, but NP-KG is a merge built on
PheKnowLator, whose declared inputs include **CTD**, whose terms prohibit
commercial reproduction without written permission, and **DisGeNET**, which was
CC BY-NC-SA and has since moved to a commercial model. A merged graph's
effective terms are the most restrictive of its inputs, so the CC BY 4.0 stamp
does not describe the whole graph. Classification: RESTRICTED. The CTD terms
could not be read from the primary page — `ctdbase.org/about/legal.jsp` sits
behind a human-verification gate that returned only the gate text — so that
specific link is medium confidence and deserves a browser check before anyone
relies on the conclusion in either direction.

What NP-KG genuinely offers is curator reference: a plant → constituent →
CYP/transporter → interacting drug evidence trail for 31 heavily studied
botanicals, with PubMed identifiers, plus roughly 1,270 hand-curated
chemical–enzyme edges. Note that its literature layer is machine-read by
relation extraction and merged into the same flat triple list as curated edges,
and the paper's own evaluation reports 38.98% congruence for green tea and 50%
for kratom against ground truth. Anything read out of it must be filtered by
edge provenance.

Three adjacent findings from the same cluster:

- **All NaPDI Center domains fail DNS as of 2026-09-07.** `repo.napdi.org`
  returns NXDOMAIN, `napdicenter.org` SERVFAIL, `napdi.org` no A record.
  Internet Archive has June 2026 snapshots, so this is recent. The NaPDI
  repository cannot currently be used as a live source.
- **PrimeKG's Harvard Dataverse record is stamped CC0** while carrying DrugBank-
  and DisGeNET-derived content. The same licence-laundering pattern as COCONUT,
  in a different community.
- **KG-Microbe ingests no natural-product structure source** — no MIBiG, no
  NPAtlas, no LOTUS in its current `download.yaml`. That is the consumer-side
  case for this corpus existing, stated as a measurement rather than an
  assumption.

The one genuinely natural-product-specific knowledge graph found is **ENPKG**,
which is sample-centric LC-MS/MS annotation: its compound nodes are *putative*
structural annotations of mass features, ranked by score. That is
hypothesis-grade chemistry — what was probably in one extract, not what an
organism is known to produce — so it is a curation lead, not a seed. Its
deposits are individually licensed, CC BY on some and CC0 on others, so a
per-deposit check would be required even for reference use.

The useful lead out of this cluster is not a knowledge graph at all. It is
**GSRS**, the FDA/NCATS Global Substance Registration System, which supplied
NP-KG's constituent names, is US government public domain, and does carry
structures and UNIIs. AntibioticMech already reads it.

### 7. Predicted gene clusters cannot ground a compound record

**Confidence: high.** Verified from the live statistics API and both papers.

antiSMASH-DB holds **479,420 predicted BGC regions over 56,054 genomes** and
assigns **no compound identity to any of them**. There is no InChIKey, SMILES,
PubChem CID or ChEBI id in it. Its only use here would be indirect: expanding a
known compound's producer set through KnownClusterBlast hits back to a MIBiG
entry, which is a similarity claim and not an identity claim. Everything in it
is auto-generated. It also publishes no data licence.

BiG-FAM is CC BY 4.0 and would let a producer claim generalize across a gene
cluster family, but it is frozen on 2020 data and MIBiG 2.0, and its documented
bulk-download URL is unreachable. The Paired Omics Data Platform is CC BY 4.0
and conceptually ideal — it links gene clusters to mass spectra — but holds
**117 BGC-to-MS2 links in total**.

## Consequences for the plan

1. **Do not port AntibioticMech's MIBiG reviewer gate.** Replace it with the
   per-locus evidence-method mapping. `PLAN.md` §2.3 and the
   `add-natural-product` skill were corrected on 2026-09-07 to say so.
2. **File by NPClassifier pathway, not by gene-cluster class.** Most records
   will never have a cluster. Carry the cluster class separately, and only
   where MIBiG asserts one.
3. **Generate InChIKeys locally** from MIBiG and COCONUT SMILES; neither ships
   one, and MIBiG ships no InChI either.
4. **Keep `occurrences` and `producer_organisms` separate from day one.** LOTUS
   is 674,454 occurrence triples and zero producer claims. Merging the two
   fields would make the corpus's largest input silently overstate itself.
5. **Never trust an aggregate licence.** COCONUT is the worked example and the
   `source-queue` skill now carries the rule.
6. **Record which route a licence came from.** LOTUS is CC0 through Wikidata
   and CC BY through Zenodo. `data/raw/MANIFEST.yaml` should say which was
   fetched.

## Refuted or corrected claims

Recorded so a future pass does not re-derive them.

1. **"MIBiG biosynthetic classes include Alkaloid."** False for 4.0 — removed
   as a biosynthetic class, stated in the paper and confirmed by its absence
   across all 3,013 release files.
2. **"MIBiG entries carry InChIKeys."** False. No InChI or InChIKey field
   exists in the 4.0 JSON.
3. **"MIBiG's `questionable` quality flag means the entry is doubtful."**
   Misleading. It predominantly marks legacy-format entries pending
   re-curation.
4. **"COCONUT is CC0."** True of the aggregate as published and false of a
   large fraction of the rows inside it. Roughly 200,000 rows carry a
   collection tag whose upstream terms are NC, SA, restricted, or unstated.
5. **"antiSMASH-DB is CC BY because the paper is CC BY."** Conflation of an
   article licence with a data licence. The same error is available for
   StreptomeDB, NPBS Atlas and SuperNatural.
6. **"NPAtlas is CC BY."** True only through release 2024_03.
7. **"Norine is freely available to everybody."** Norine's own phrasing, which
   continues into CC BY-NC-SA 4.0.
8. **MassBank record counts** vary by release train — 119,845 in the 2026
   paper, 134,756 in the deployed instance, 139,006 from the count endpoint.
   None is wrong; never quote one without naming its source.

## Could not be verified

- **Every Zenodo fetch failed** in the biosynthesis cluster, with HTTP 403
  ("unusual traffic") or a certificate error. No Zenodo record was
  independently confirmed there, so the MIBiG, PoDP and MassBank Zenodo DOIs
  are reported as their own sites cite them. The structures cluster did reach
  the Zenodo API for the LOTUS, NPAtlas and CyanoMetDB records. Non-Zenodo
  routes — `dl.secondarymetabolites.org`, GitHub release assets — all worked
  and are the safer primary route for a pipeline.
- **Is there a machine-readable "reviewed" flag in MIBiG?** The paper
  recommends filtering to reviewed entries and says the website supports it,
  but the 4.0 dump exposes only the placeholder reviewer id. Either the flag
  postdates the 4.0 release or it is derived server-side. Resolve by diffing
  the 2026-03-24 `all_jsons` tarball's schema, or by asking the MIBiG team.
- **Which GNPS libraries are CC0 and which are imports.** The library table
  types libraries but publishes no per-library licence field. Seeding needs an
  explicit allow-list.
- **The per-record licence distribution in MassBank.** `LICENSE` is mandatory
  and defaults to CC BY; the actual distribution across ~139,000 records is
  unknown and must be computed before ingest.
- **Whether NPAtlas releases ≤2024_03 are individually tagged CC BY on Zenodo.**
  Licence tags are per-version and were not enumerated.
- Several hosts were down or unreachable on the day: SuperNatural 3.0 does not
  resolve in public DNS, UNPD is defunct and survives only inside aggregators,
  NuBBE times out, and `cyanometdb.org` does not resolve (the Eawag project
  page is the live home).

## Open questions for the owner

1. **Is buying into the NPAtlas ≤2024_03 CC BY releases worth it?** It is the
   best microbial occurrence data available and the older releases are
   seedable, but they are two years stale and the corpus would carry a source
   frozen in the past. Alternative: ask the Linington group for a scoped CC BY
   grant covering structure, producer and taxid fields only.
2. **Should StreptomeDB and antiSMASH-DB be asked for an explicit licence?**
   Both are academic groups with no licence statement rather than a restrictive
   one, and the antiSMASH team already publishes MIBiG under CC BY. Contacting
   maintainers is an outbound action and needs authorization.
3. **How far does Phase A's taxon filter reach?** Cyanobacteria and microalgae
   are in; the sponge and tunicate metabolites whose real producers are
   uncultured symbionts are the hard boundary, and they are a large fraction of
   marine natural-product chemistry.
