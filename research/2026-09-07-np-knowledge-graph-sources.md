# Knowledge-graph natural-product resources — research report

Cluster: NP-KG (Taneja/Boyce, NaPDI Center), NaPDI Center repository and ontology work,
PheKnowLator, and other natural-product / biomedical knowledge graphs.

Research date: **2026-09-07**. All "verified live" claims were checked on that date at the
URL given.

---

## Summary

**NP-KG cannot seed a structure-keyed natural-product corpus.** It is a pharmacokinetic
drug-interaction knowledge graph, not a natural-product structure resource. Its entire
natural-product content is a 651-class OWL extension in which:

- **613 phytoconstituents** are named entities. **460** are mapped to a ChEBI class; **153**
  carry a minted `http://napdi.org/napdi_srs_imports:<normalized_name>` URI whose only
  superclass is `CHEBI_24431` ("chemical entity"), i.e. a name with no structure and no
  chemical parent of any information content.
- **68 plant / plant-part entities** are minted under `PO_0025131`, linked to **34 NCBI
  Taxonomy identifiers** via `RO_0002162` (in taxon).
- **716 `RO_0002180` (has component) edges** connect plant entities to constituents.
- There is **no InChI, no InChIKey, no SMILES, no PubChem CID, no UNII, no CAS** anywhere in
  the ontology extension. Verified by grep over the extension OWL file.

Joinability to a structure-keyed corpus therefore runs entirely through ChEBI, and only for
the 460 constituents that got a ChEBI ID. Those you could already get from ChEBI directly.
The 153 name-only constituents are exactly the compounds ChEBI lacks, and NP-KG adds nothing
about them beyond a lowercased name string and a plant association.

What NP-KG genuinely offers a curator: a **plant → constituent → CYP/transporter →
interacting drug** evidence trail for 31 heavily studied botanicals, with PubMed IDs for the
machine-read literature layer, plus ~1,270 hand-curated chemical–enzyme/transporter edges
sourced from DIKB, FDA drug-interaction tables and DrugCentral. That is curator input, not
seed data.

**Licence position.** The NP-KG Zenodo dataset is stamped **CC BY 4.0** and the GitHub code is
**Apache-2.0**. But NP-KG is a merge of PheKnowLator, whose inputs include **CTD** (explicitly
no commercial use without written permission, redistribution constrained) and **DisGeNET**
(historically CC BY-NC-SA). The effective redistribution terms of the merged graph are the
most restrictive of its inputs, so the CC BY 4.0 stamp on the Zenodo record is **not** a
licence you can rely on for the whole graph. Treat NP-KG as **RESTRICTED** for redistribution
and **usable as curator reference**.

**Other KGs in this cluster.** PrimeKG, SPOKE and Bioteque are general biomedical KGs with no
natural-product structure layer and no producer organisms; PrimeKG's Harvard Dataverse record
is stamped CC0 despite containing DrugBank- and DisGeNET-derived content, which is a licence
laundering trap. KG-Microbe is BSD-3-Clause and ingests ChEBI, Rhea, KEGG, BacDive, GTDB and
UniProt, but **no natural-product structure source** (no NPAtlas, no MIBiG, no LOTUS) as of the
current `download.yaml`. **ENPKG** is the only genuinely NP-specific KG found here, and it is
sample-centric LC-MS/MS annotation data rather than curated compound records.

**Infrastructure warning.** All NaPDI Center web properties are **unresolvable in DNS as of
2026-09-07**: `repo.napdi.org` returns NXDOMAIN, `napdicenter.org` returns SERVFAIL, `napdi.org`
returns no A record. Internet Archive has snapshots from June 2026, so this is a recent
outage or lapse. The NaPDI repository cannot currently be used as a live source.

---

## Per-source findings

### 1. NP-KG — Knowledge Graph for Natural Product-Drug Interactions

#### 1.1 What it is, who maintains it, version, size

**What it is.** A biomedical knowledge graph built to generate mechanistic hypotheses for
**pharmacokinetic** natural product-drug interactions (NPDIs). Verbatim from the repository
README (verified live 2026-09-07 at
https://raw.githubusercontent.com/sanyabt/np-kg/main/README.md):

> NP-KG is a graph framework that creates a biomedical knowledge graph (KG) to identify and
> generate mechanistic hypotheses for pharmacokinetic natural product-drug interactions
> (NPDIs). NP-KG uses the PheKnowLator ecosystem to create an ontology-grounded KG. It then
> uses two relation extraction systems to extract triples from full texts of natural
> product-related scientific literature to create a literature-based graph, and integrates
> the nodes and edges in the ontology-grounded KG.

**Maintainers.** Sanya Bathla Taneja (ORCID 0000-0003-1707-1617) and Richard D. Boyce,
University of Pittsburgh, under the NIH NCCIH-funded NaPDI Center (grant U54 AT008909).
Paper co-authors: Taneja, Callahan, Paine, Kane-Gill, Kilicoglu, Joachimiak, Boyce.
Confidence: **high**, verified from README and paper metadata.

**Latest version.** **v3.0.0, June 2024**, DOI 10.5281/zenodo.12536780. Confidence: **high**,
verified live 2026-09-07 via the Zenodo API (`https://zenodo.org/api/records/12536780`,
`"version": "3.0.0"`, `"publication_date": "2024-06"`).

**Activity.** The GitHub repository's most recent commit is **2024-06-25** ("Update
README.md"). There are **zero GitHub releases/tags**. Verified live 2026-09-07 via the GitHub
API. The project appears dormant since mid-2024; the only later output is a 2025 AMIA
Summits paper on embeddings over the same v3.0.0 graph (see §1.8).

**Size** (verified live 2026-09-07 at
https://raw.githubusercontent.com/wiki/sanyabt/np-kg/v3.0.0.md):

| NP-KG v3.0.0 | Nodes | Edges |
|---|---:|---:|
| Merged KG | 1,089,139 | 7,836,115 |
| Ontology-grounded KG | 1,088,531 | 7,716,032 |
| Literature-based graph | 12,190 | 120,371 |

Note the published paper (JBI 2023, describing v1) reports **745,512 nodes and 7,249,576
edges**; the arXiv abstract confirms these numbers. Any citation of "745k nodes" refers to the
2023 version, not the current release. Confidence: **high**.

Natural-product coverage is **31 botanicals** (the wiki table lists 31 rows for what the text
calls "30 natural products"; two rows bundle multiple species — *Cinnamomum cassia, C. verum*
and *Glycyrrhiza glabra, G. inflata, G. uralensis*). List verified live 2026-09-07 at
https://raw.githubusercontent.com/wiki/sanyabt/np-kg/Natural-Products-in-KG.md:

Actaea racemosa, Aesculus hippocastanum, Allium sativum, Camellia sinensis, Cannabis sativa,
Cinnamomum cassia/verum, Citrus paradisi, Crataegus laevigata, Curcuma longa, Echinacea
purpurea, Ginkgo biloba, Glycine max, Glycyrrhiza spp., Hydrastis canadensis, Linum
usitatissimum, Mitragyna speciosa, Origanum vulgare, Panax ginseng, Paullinia cupana, Piper
nigrum, Rhodiola rosea, Rosmarinus officinalis, Serenoa repens, Silybum marianum, Tanacetum
parthenium, Taraxacum officinale, Trigonella foenum, Vaccinium macrocarpon, Valeriana
officinalis, Withania somnifera, Zingiber officinale.

(The `resources/pmids/` directory also contains `gojiberry_pmid.txt`, which is not on the wiki
list — a minor inconsistency.)

#### 1.2 What it would contribute to a structure-keyed NP KB

| Wanted | NP-KG provides? |
|---|---|
| Chemical structures | **No.** No InChI/InChIKey/SMILES anywhere. |
| Producer organism | **Partly.** 34 NCBI Taxonomy IDs, plant species only, linked to plant-part entities, not to individual compounds directly (compounds link to the plant part, not the taxon). |
| Biosynthetic origin / BGC | **No.** Nothing. |
| Bioactivity | **No** in the NP sense. Chemical-disease/phenotype edges come from CTD and are drug-centric. |
| Targets | **Yes, and this is the strongest part.** Human CYP450 enzymes and transporters as Protein Ontology (PR) classes, with typed relations: `is substrate of` (DIDEO_00000041), `directly negatively regulates activity of` (RO_0002449, inhibitor), `transports` (RO_0002020), `molecularly interacts with` (RO_0002436). |
| Pharmacokinetics | **Yes.** This is the resource's entire purpose. |
| Mechanism | **Yes, as hypothesis paths**, not as asserted mechanism records. The stated use is meta-path discovery over the graph. |
| Literature evidence | **Yes, but overwhelmingly machine-read.** See §1.6. |

Concretely useful curated content, all ChEBI×PRO keyed, downloaded and counted live
2026-09-07 from `https://github.com/sanyabt/np-kg/tree/main/resources/data`:

| File | Rows | Relation |
|---|---:|---|
| `CHEMICAL_SUBSTRATE.tsv` | 514 | chemical is substrate of protein |
| `CHEMICAL_MOLECULE.tsv` | 394 | chemical molecularly interacts with protein |
| `CHEMICAL_INHIBITOR.tsv` | 273 | chemical inhibits protein |
| `CHEMICAL_TRANSPORTER.tsv` | 91 | protein transports chemical |
| `staging_combined_new_202308101935.tsv` | 2,167 | the provenance-carrying source table for the above |

The staging table carries columns `chemical_id, chemical_name, protein_id, protein_name,
relation_name, relation_id, source, dikb_id, fda_id, drugcentral_id, reference, year,
measurement_type, measurement_value` — i.e. per-edge provenance to **DIKB**, **FDA drug
interaction tables** and **DrugCentral**. Sample rows are conventional drugs (busulfan →
CYP2A6 inhibits, source FDA; probenecid → BCRP, source FDA), **not** natural products. This
table is a drug-side PK reference, not an NP resource.

Also present: `dikb-evidence.zip` (5.4 MB), `fda-drug-interaction-evidence.zip` (657 KB),
`reposdb_mapped_202402191155.tsv` (1.8 MB, repoDB indications).

#### 1.3 Identifiers carried — the decisive question

**NP-KG does not identify a natural product as a structure.** Verified by direct inspection
of the ontology extension files (downloaded live 2026-09-07 from
`https://raw.githubusercontent.com/sanyabt/np-kg/main/resources/ontology-extensions/`).

`chebi-extensions-constituents-20240229.tsv` has exactly two columns:

```
constituent_name	URI
12beta-acetoxycimigenol 3-o-beta-d-xylopyranoside	http://napdi.org/napdi_srs_imports:12beta_acetoxycimigenol_3_o_beta_d_xylopyranoside
2'-o-acetylactein	http://napdi.org/napdi_srs_imports:2_o_acetylactein
23-epi-26-deoxyactein	http://purl.obolibrary.org/obo/CHEBI_70243
```

Counts I computed from the files:

| File | Data rows | ChEBI-mapped | Minted `napdi_srs_imports` |
|---|---:|---:|---:|
| `chebi-extensions-constituents-20240229.tsv` (constituents) | 613 | 460 | 153 |
| `chebi-extensions-constituents-NP-20240229.tsv` (constituents + plant entities) | 681 | 460 | 221 |

From `chebi-extensions-instance-20240229.owl` (651 `owl:Class` blocks, 221 of them minted
`napdi.org` URIs):

- 153 minted classes are `rdfs:subClassOf CHEBI_24431` ("chemical entity") — the near-root of
  ChEBI, carrying zero chemical information.
- 68 minted classes are `rdfs:subClassOf PO_0025131` (plant anatomical entity) — the plant and
  plant-part entities.
- 716 `RO_0002180` (has component) restrictions, 34 `RO_0002162` (in taxon) restrictions to
  NCBITaxon, 34 `BFO_0000050` (part of) restrictions.
- 431 distinct ChEBI IDs referenced across the file.
- `grep -oiE 'inchi|smiles|pubchem|unii|formula|CAS'` over the OWL returns **zero matches**.

A representative minted class, verbatim from the OWL:

```xml
<owl:Class rdf:about="http://napdi.org/napdi_srs_imports:acetoxyvalerenic_acid">
    <rdfs:subClassOf rdf:resource="http://purl.obolibrary.org/obo/CHEBI_24431"/>
    <rdfs:label xml:lang="en">acetoxyvalerenic acid</rdfs:label>
</owl:Class>
```

And a plant entity, showing the taxon link and the has-component pattern:

```xml
<owl:Class rdf:about="http://napdi.org/napdi_srs_imports:actaea_racemosa">
    <rdfs:subClassOf rdf:resource="http://purl.obolibrary.org/obo/PO_0025131"/>
    <rdfs:subClassOf><owl:Restriction>
        <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/BFO_0000050"/>
        <owl:someValuesFrom rdf:resource="http://napdi.org/napdi_srs_imports:actaea_racemosa_whole"/>
    </owl:Restriction></rdfs:subClassOf>
    <rdfs:subClassOf><owl:Restriction>
        <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002162"/>
        <owl:someValuesFrom rdf:resource="http://purl.obolibrary.org/obo/NCBITaxon_64040"/>
    </owl:Restriction></rdfs:subClassOf>
    <rdfs:subClassOf><owl:Restriction>
        <owl:onProperty rdf:resource="http://purl.obolibrary.org/obo/RO_0002180"/>
        <owl:someValuesFrom rdf:resource="http://napdi.org/napdi_srs_imports:actaeaepoxide_3_o_beta_d_xylopyranoside"/>
    </owl:Restriction></rdfs:subClassOf>
    ...
```

Confidence: **high** for all of the above; computed directly from the primary files.

Identifiers used elsewhere in the graph (verified live 2026-09-07 from
`resources/resource_info.txt` and the v2.0.0 wiki edge table):

| Entity class | Identifier |
|---|---|
| Chemical | ChEBI (`CHEBI_*`), MeSH for CTD input mapped through `MESH_CHEBI_MAP.txt` |
| Protein | Protein Ontology (`PR_*`, e.g. `PR_P10635` = CYP2D6), built from UniProt accessions |
| Gene | NCBI Gene (Entrez) numeric |
| RNA | Ensembl transcript (`ENST*`) |
| Pathway | Reactome (`R-HSA-*`) |
| Disease | MONDO |
| Phenotype | HPO |
| Anatomy / cell | Uberon, CLO, CL |
| Variant | dbSNP rsIDs |
| Taxon | NCBITaxon (plants only, 34 IDs) |
| Function/process | GO |

**Joinability verdict.** To join NP-KG to a structure-keyed corpus you would have to go
`napdi_srs_imports:<name>` → name normalisation → your own structure resolution, for the 153
compounds where NP-KG has nothing else, and `CHEBI_*` → InChIKey for the other 460. The
second path does not require NP-KG at all. The first path is name matching, with all the
usual failure modes and no way to verify a match against the source.

#### 1.4 Bulk access

- **Format**: merged KG as TSV (subject, edge type, object, weight), NetworkX gpickle, and
  N-Triples. Node labels and node types as separate TSVs.
- **URL**: https://doi.org/10.5281/zenodo.12536780. File list verified live 2026-09-07 via the
  Zenodo API:

| File | Size |
|---|---:|
| `NP-KG_v3.0.0.tsv` | 1,074,149,258 B |
| `NP-KG_v3.0.0.gpickle` | 936,065,236 B |
| `nodeLabels_v3.0.0.tsv` | 96,489,706 B |
| `nodeLabels_v3.0.0.pickle` | 116,100,740 B |
| `nodeTypes_v3.0.0.tsv` | 64,376,304 B |

- **Versioning**: concept DOI 10.5281/zenodo.6814507, version DOIs per release; v3.0.0 =
  10.5281/zenodo.12536780. `access_right: open`.
- **Loader**: GRAPE `Graph.from_csv(...)`, and `from grape.datasets.zenodo import NPKG` (that
  shortcut pins **v1.0.1**, not v3 — a version trap for anyone using the one-liner).
- **API**: none. Bulk download only.

Note on the earlier session-wide Zenodo problem: `WebFetch` on `zenodo.org` failed with
"unable to get issuer certificate", and the first `curl` to the Zenodo API returned a 504. A
retry of the Zenodo REST API succeeded. The DataCite API
(`https://api.datacite.org/dois/10.5281/zenodo.12536780`) is a reliable fallback and returns
the same rights metadata.

#### 1.5 Licence

Three distinct licences apply, and they must not be conflated.

**Code (GitHub repo)** — **Apache License 2.0**. Verified live 2026-09-07 at
https://raw.githubusercontent.com/sanyabt/np-kg/main/LICENSE:

> Apache License
> Version 2.0, January 2004
> http://www.apache.org/licenses/
> TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

**Dataset (Zenodo record)** — **CC BY 4.0**. Verified live 2026-09-07 two ways.
Zenodo API returns `"license": {"id": "cc-by-4.0"}`. DataCite returns:

> "rights": "Creative Commons Attribution 4.0 International",
> "rightsUri": "https://creativecommons.org/licenses/by/4.0/legalcode",
> "rightsIdentifier": "cc-by-4.0"

**Paper (arXiv preprint 2209.11950)** — **CC BY 4.0**. The JBI version of record is
paywalled (ScienceDirect returned HTTP 403). A CC BY paper is not a data licence; it is
noted only for completeness.

**Effective redistribution terms — the important part.** NP-KG is a merge, and a merged graph
inherits the most restrictive of its inputs. NP-KG = PheKnowLator v3.1.2 full instance build
+ NaPDI/GSRS/EMA ontology extensions + repoDB + ONSIDES + a literature graph. The
PheKnowLator inputs are, verbatim from
https://raw.githubusercontent.com/callahantiff/PheKnowLator/master/resources/edge_source_list.txt
and `ontology_source_list.txt` (both verified live 2026-09-07):

| Upstream source | Files used | Licence status for redistribution |
|---|---|---|
| **CTD** (Comparative Toxicogenomics Database) | `CTD_chemicals_diseases.tsv`, `CTD_chem_gene_ixns.tsv`, `CTD_chem_go_enriched.tsv`, `CTD_genes_pathways.tsv` | **RESTRICTED.** CTD legal notices state reproduction or use for commercial purpose is prohibited without prior express written permission of MDI Biological Laboratory and NC State University, plus mandatory citation and hyperlink-back requirements. **Not verified against the primary page** — https://ctdbase.org/about/legal.jsp is behind a CAPTCHA/human-verification gate and returned only the gate text to both `curl` and WebFetch on 2026-09-07. Terms above are from search-result summaries and from reusabledata.org's assessment; confidence **medium**. This is the single biggest licence blocker and should be re-verified in a browser. |
| **DisGeNET** | `curated_gene_disease_associations.tsv` | **NON_COMMERCIAL / SHARE_ALIKE (probable).** Historically CC BY-NC-SA 4.0 for the academic releases; the resource has since moved to a commercial model at disgenet.com. **Not verified** — `disgenet.org/legal` 301-redirects to `disgenet.com/Legal`, which returned only a page title to WebFetch on 2026-09-07. Confidence **low-medium**. |
| **STRING** v11.0 | `9606.protein.links.v11.0.txt` | CC BY 4.0 (not re-verified this session; confidence **medium**). |
| **Human Protein Atlas** | `HPA_GTEX_RNA_GENE_PROTEIN_EDGES.txt` | CC BY-SA 3.0 (not re-verified; confidence **medium**). **SHARE_ALIKE**. |
| **GeneMANIA** | `COMBINED.DEFAULT_NETWORKS.BP_COMBINING.txt` | Not verified; confidence **low**. |
| Reactome | `ChEBI2Reactome_All_Levels.txt`, `UniProt2Reactome_All_Levels.txt`, `gene_association.reactome` | CC BY 4.0 / CC0 depending on release. Seedable. |
| UniProt | catalyst/cofactor tables | CC BY 4.0. Seedable. |
| GO / GOA | `goa_human.gaf` | CC BY 4.0. Seedable. |
| HPO | `phenotype.hpoa` | HPO custom permissive licence. Seedable with attribution. |
| ClinVar, NCBI Gene | ClinVar edge tables | US public domain. Seedable. |
| Ensembl | transcript maps | Apache 2.0 / no restriction. Seedable. |
| ChEBI, MONDO, PRO, Uberon, CLO, SO, PW, RO, VO, HP, GO ontologies | `*_with_imports.owl` | CC BY 3.0/4.0 mostly. Seedable with attribution. |
| **GSRS** (FDA/NCATS Global Substance Registration System) | constituent lists | US government, public domain. Seedable. |
| **EMA herbal monographs** | constituent lists | EMA reuse policy, generally permissive with attribution. Confidence **low**, not verified. |
| repoDB | `reposdb_mapped_*.tsv` | CC BY 4.0 (not verified this session; confidence **low**). |
| ONSIDES | drug side effects | Tatonetti lab, GitHub. Not verified; confidence **low**. |
| DIKB, FDA DDI tables, DrugCentral | `staging_combined_*.tsv` and the four CHEMICAL_* files | DrugCentral is CC BY-SA 4.0 (**SHARE_ALIKE**); DIKB and FDA tables permissive/public. Not verified; confidence **low**. |
| SemMedDB / SemRep, INDRA/REACH outputs | literature graph | Derived from PubMed full texts including PMC subsets with heterogeneous licences. See §1.6. |

**Classification for NP-KG as a whole: RESTRICTED.** The Zenodo CC BY 4.0 stamp cannot
override CTD's no-commercial-redistribution terms or DisGeNET's NC-SA, both of which are
baked into the merged graph. NP-KG is **not seedable** into a CC BY 4.0 corpus. It is fine as
a reference a curator reads.

#### 1.6 Data-quality traps

1. **The literature layer is machine-read and is merged into the same graph as curated
   edges.** 120,371 of the 7,836,115 edges come from SemRep and INDRA/REACH relation
   extraction over full texts, then expanded by "closure operations". Relation extraction over
   biomedical full text has well-known precision problems, and the merged TSV presents these
   edges alongside GO annotations and Reactome pathways in one flat triple list. The paper's
   own evaluation reports only **38.98% congruence for green tea and 50% for kratom** against
   ground truth. Anything read out of the merged file must be filtered by edge provenance
   before it is believed.
2. **Name-only compound entities.** 153 of 613 constituents (25%) exist solely as a
   normalized lowercase name under `CHEBI_24431`. There is no way to determine what molecule
   any of them is from the graph.
3. **Class terms presented as constituents.** `sesquiterpenes`, `triterpenes` and
   `glucose 3-o-glycosides` appear in the constituent list as if they were compounds. A naive
   ingest would create "compounds" that are chemical classes.
4. **Plant-level vs constituent-level conflation.** The NP entities are plant anatomical
   entities (*Actaea racemosa*, *Actaea racemosa* whole/root), not preparations and not
   compounds. Interaction claims in the source literature are usually about an **extract or
   preparation**, and attributing them to a named constituent, or to a structure, is an
   inference NP-KG does not make and you should not make on its behalf.
5. **`RO_0002180` (has component) is occurrence, not production.** The plant→constituent edge
   says the constituent was detected in that plant part. It carries no evidence, no
   quantitation, and no biosynthetic claim. For a corpus that distinguishes producer from
   occurrence, this is occurrence data.
6. **Version drift.** The GRAPE convenience loader `from grape.datasets.zenodo import NPKG`
   returns **v1.0.1**, three versions behind. Published node/edge counts vary by version
   (745,512 / 7,249,576 in the 2023 paper; 1,090,173 / 7,934,518 in v2.0.0; 1,089,139 /
   7,836,115 in v3.0.0), so counts quoted without a version are ambiguous.
7. **Proteins are Protein Ontology classes, not UniProt accessions.** `PR_P10635` embeds a
   UniProt accession in the local ID, which happens to make mapping easy, but it is a PRO
   class and not every PR term follows that pattern.
8. **Dead source URIs.** The minted constituent and plant URIs are in the `napdi.org`
   namespace, which does not currently resolve (§2). They were never resolvable PURLs in any
   case, but this now also removes the documentation behind them.

#### 1.7 Confidence summary for NP-KG

| Claim | Confidence | Verified |
|---|---|---|
| v3.0.0, June 2024, DOI 10.5281/zenodo.12536780 | high | yes, Zenodo API + DataCite, 2026-09-07 |
| 1,089,139 nodes / 7,836,115 edges | high | yes, project wiki, 2026-09-07 |
| 613 constituents, 460 ChEBI, 153 name-only | high | computed from primary TSV, 2026-09-07 |
| No InChIKey/SMILES/CID/UNII anywhere | high | grep over primary OWL, 2026-09-07 |
| 34 NCBI Taxonomy IDs, plants only | high | computed from primary OWL, 2026-09-07 |
| Zenodo dataset CC BY 4.0 | high | yes, Zenodo API + DataCite, 2026-09-07 |
| Code Apache-2.0 | high | yes, LICENSE file, 2026-09-07 |
| CTD terms block commercial redistribution | medium | **no** — CAPTCHA gate |
| DisGeNET academic release CC BY-NC-SA | low-medium | **no** — page returned no content |
| Repository dormant since June 2024 | high | yes, GitHub API commits, 2026-09-07 |

#### 1.8 Follow-on work

**Taneja SB, Dilán-Pantojas IO, Boyce RD. "Predicting Natural Product-Drug Interactions with
Knowledge Graph Embeddings." AMIA Jt Summits Transl Sci Proc. 2025 Jun 10;2025:556-565.
PMID 40502231, PMCID PMC12150722.** Verified live 2026-09-07 via NCBI E-utilities. Abstract
verbatim in part:

> We evaluated the ability of several KG embedding methods to improve NPDI prediction on
> NP-KG, a large-scale, heterogeneous, biomedical KG. We found that the ComplEx model
> outperformed other KG embedding approaches in both intrinsic and extrinsic evaluations.

Copyright "©2025 AMIA - All rights reserved" — the paper is **RESTRICTED**, not open. This
work produces embeddings over the same v3.0.0 graph. Embeddings are not usable as corpus
seed. No new NP structure content.

Earlier related abstract: Taneja, Callahan, Brochhausen, Paine, Kane-Gill, Boyce, "Designing
potential extensions from G-SRS to ChEBI to identify natural product-drug interactions",
ISMB/ECCB 2021, https://doi.org/10.5281/zenodo.5736386. This is the design work behind the
GSRS→ChEBI constituent mapping described in §1.3, and confirms the mapping was designed as a
**name-to-ChEBI-class** exercise, not a structure registration.

---

### 2. NaPDI Center and its data repository

**What it is.** The NIH NCCIH Center of Excellence for Natural Product-Drug Interaction
Research (grant U54 AT008909), a multi-institution centre (Washington State University,
University of Pittsburgh, UNC and others) that ran chemical characterisation, in vitro and
clinical pharmacokinetic studies on botanicals and published an open repository of the
resulting data at `repo.napdi.org`, with the informational site at `napdicenter.org`.
Described in Birer-Williams C. et al. and Boyce/Paine et al., "A New Data Repository for
Pharmacokinetic Natural Product-Drug Interactions: From Chemical Characterization to
Clinical Studies", *Drug Metabolism and Disposition* 2020, PMID 32601103, PMC7543481.

**Status as of 2026-09-07: OFFLINE.** All three hosts fail DNS resolution:

```
repo.napdi.org   -> NXDOMAIN
napdi.org        -> no A record ("No answer")
napdicenter.org  -> SERVFAIL
```

Confirmed independently from the sandbox (`nslookup`, `curl` returning HTTP 000) and from the
WebFetch service (`getaddrinfo ENOTFOUND repo.napdi.org`, `getaddrinfo ENOTFOUND
napdicenter.org`). Internet Archive holds snapshots dated **2026-06-08** for `repo.napdi.org`
and **2026-06-16** for `napdicenter.org`, so the sites were live three months ago. I could not
read the archived pages: `web.archive.org` is not fetchable by this session's WebFetch tool
("Claude Code is unable to fetch from web.archive.org"). Confidence: **high** that the sites
are currently unresolvable; **not verified** what their terms of use said.

**What it would have contributed.** Per the DMD paper: chemical characterisation of natural
products, metabolomics analyses, and in vitro and clinical pharmacokinetic experimental
results, with per-study metadata. This is deep pharmacokinetic evidence on ~10 botanicals, not
a structure catalogue. Its constituent-level content is the same GSRS-derived material that
reached NP-KG as name-keyed entities.

**Licence: UNVERIFIED.** The repository was described as "open-access" and "publicly
accessible" in the DMD paper, but I could not reach any terms-of-use page. Do not assume a
licence.

**Practical conclusion.** Not usable as a live source. If the underlying content matters, the
reachable proxies are (a) the NP-KG ontology extensions on GitHub, which are the constituent
lists in derived form, and (b) the DMD paper's supplementary material.

### 2b. NaPDI ontology work — DIDEO extension

**What it is.** Rather than build a new natural-product ontology, the Boyce group extended
**DIDEO** (Drug-drug Interaction and Evidence Ontology) to cover natural-product interaction
entities. Judkins J, Tay-Sontheimer J, Boyce RD, Brochhausen M. "Extending the DIDEO ontology
to include entities from the natural product drug interaction domain of discourse." *Journal
of Biomedical Semantics* 2018;9:15. PMC5944177. Open access.

This is why `DIDEO_00000041` ("is substrate of") appears as a relation in NP-KG's
`resource_info.txt` — verified live 2026-09-07.

**Contribution to a structure-keyed KB.** Terminology and relation semantics only. DIDEO
defines the *evidence and interaction* vocabulary; it contains no compounds and no structures.
It is a useful modelling reference for how to type "X is a substrate of CYP3A4" claims, and
nothing more.

**Licence.** DIDEO is an OBO Foundry ontology; OBO requires CC BY or more permissive. Not
verified this session; confidence **medium**. Classification: **ATTRIBUTION (probable)**.

### 3. PheKnowLator — the build framework under NP-KG

**What it is.** "PheKnowLator (Phenotype Knowledge Translator) or `pkt_kg` is the first fully
customizable knowledge graph (KG) construction framework enabling users to build complex KGs
that are Semantic Web compliant and amenable to automatic Web Ontology Language (OWL)
reasoning..." Verbatim from README.rst, verified live 2026-09-07 at
https://raw.githubusercontent.com/callahantiff/PheKnowLator/master/README.rst

**Maintainer.** Tiffany J. Callahan and collaborators. Repo
https://github.com/callahantiff/PheKnowLator. Preprint https://arxiv.org/abs/2307.05727.

**Latest release: v3.1.2, 2023-11-18.** Last push to the repository **2024-05-03**. Verified
live 2026-09-07 via the GitHub API. Also effectively dormant. NP-KG v3.0.0 uses the
`PheKnowLator_v3.1.2_full_instance_inverseRelations_OWLNETS` build.

**Contribution to a structure-keyed NP KB: none directly.** It is a build framework plus a
human-centric biomedical KG. Zero natural-product content, zero producer organisms, zero
biosynthesis. Its value here is that it fixes NP-KG's identifier vocabulary (§1.3) and its
licence exposure (§1.5).

**Bulk access.** Prebuilt KGs as triple edge lists, OWL API RDF/XML, and NetworkX gpickle,
served from `https://storage.googleapis.com/pheknowlator/current_build/...`. Archived builds
listed on the wiki. A Zenodo community exists at
https://zenodo.org/communities/pheknowlator-ecosystem.

**Licence. Code: Apache-2.0**, verified live 2026-09-07 at
https://raw.githubusercontent.com/callahantiff/PheKnowLator/master/LICENSE and confirmed by
the GitHub API (`"spdx_id": "Apache-2.0"`). **Data: no separate data licence found.** The
prebuilt KGs redistribute CTD, DisGeNET, HPA, STRING and GeneMANIA content, so the same
most-restrictive-input problem applies. Classification: **RESTRICTED** for the built graphs,
**CC0_OK-equivalent (Apache-2.0)** for the code.

**Traps.** The OWL-NETS abstraction step rewrites OWL class expressions into direct edges;
what looks like a simple asserted triple in the output may be a machine-derived
simplification of a restriction. The `full_instance_inverseRelations` build also materialises
inverse edges, which double-counts if you treat the edge list as a set of independent
assertions.

### 4. Other knowledge graphs

#### 4.1 ENPKG — Experimental Natural Products Knowledge Graph

The only genuinely NP-specific knowledge graph found in this cluster.

**What it is.** A sample-centric RDF knowledge graph built from LC-MS/MS metabolomics of
plant extract collections, with molecular networking and in-silico structural annotation
(SIRIUS/CANOPUS, ISDB), taxonomically informed annotation re-weighting, and links out to
Wikidata/LOTUS. Publication: Gaudry A, Pagni M, Mehl F, Moretti S, Quiros-Guerrero L-M,
Cappelletti L, Rutz A, Kaiser M, Marcourt L, Queiroz EF, Ioset J-R, Grondin A, David B,
Wolfender J-L, Allard P-M. "A Sample-Centric and Knowledge-Driven Computational Framework for
Natural Products Drug Discovery." *ACS Central Science* 2024;10(3):494.
https://pubs.acs.org/doi/10.1021/acscentsci.3c00800 (open access).

**Maintainer.** GitHub organisation https://github.com/enpkg (9 repositories), contact
`enpkg@proton.me`. Endpoint at https://enpkg.commons-lab.org/graphdb/ (returned HTTP 406 to a
plain `curl` on 2026-09-07 — the host is up but rejects a non-browser request; a SPARQL client
is presumably required). Verified live 2026-09-07.

**Contribution.** Structures **as annotations, not as records**. ENPKG's compound nodes are
*putative* structural annotations of MS features, ranked by score, plus Wikidata/LOTUS links
for the reference library. It carries the source plant sample and its taxonomy, and bioassay
results for the extracts (antitrypanosomal etc.). For a structure-keyed corpus this is
**hypothesis-grade** chemistry: it tells you what was probably in a specific extract, not what
a given organism is known to produce.

**Identifiers.** Structures via InChIKey and Wikidata QIDs through the LOTUS linkage;
taxonomy via Wikidata and OTL/GBIF. Confidence **medium**, from the paper description; not
verified against a downloaded triple file.

**Bulk access.** Per-sample `.ttl` RDF files on Zenodo, combinable into a whole graph. Code
under GPL-3.0 (most repos) and AGPL-3.0 (`enpkg_mn_isdb_taxo`), verified live 2026-09-07 at
https://github.com/enpkg.

**Licence — data.** Mixed, and it must be checked per deposit. Verified live 2026-09-07 via
DataCite:

| Deposit | Licence |
|---|---|
| `enpkg_toy_dataset`, 10.5281/zenodo.10018590 | Creative Commons Attribution 4.0 International (`cc-by-4.0`) |
| Individual .ttl files for plate VGF159, 10.5281/zenodo.10282053 | Creative Commons Zero v1.0 Universal (`cc0-1.0`) |

Classification: **ATTRIBUTION to CC0_OK depending on deposit** for the data;
**SHARE_ALIKE / copyleft** for the code (GPL/AGPL — irrelevant if you only consume data, but
it means you cannot vendor their pipeline into a permissively licensed tool).

**Traps.** Annotations are probabilistic and reweighted by taxonomy, so a compound-organism
edge can be partly circular (the taxonomy informed the annotation). Extract-level bioassay
results are attributed to the extract, not to any constituent.

#### 4.2 KG-Microbe / KG-Hub

**What it is.** A modular reference knowledge graph for microbial traits, from the
Knowledge-Graph-Hub organisation. Repo https://github.com/Knowledge-Graph-Hub/kg-microbe,
actively maintained (last push **2026-09-07**, verified live via the GitHub API).
Paper: "KG-Microbe: Building modular and scalable knowledge graphs for microbiome and
microbial sciences", PMC13536490.

**Natural-product content: none.** From the current `download.yaml` (verified live 2026-09-07
at https://raw.githubusercontent.com/Knowledge-Graph-Hub/kg-microbe/master/download.yaml), the
declared source tags are: `tools, ontologies, stubs, mappings, bacdive, mediadive, madin,
rhea, cog, kegg, gtdb, metatraits, metatraits_gtdb, bactotraits, microbedecoder, prego, gold,
schema`. ChEBI is present as an ontology and Rhea/KEGG supply reaction chemistry, but there is
**no NPAtlas, no MIBiG, no LOTUS, no antiSMASH/BGC ingest**. So: producer organisms in
abundance (NCBI Taxonomy and GTDB), no natural-product structures.

**Bulk access.** `https://kg-hub.berkeleybop.io/kg-microbe/YYYYMMDD/kg-microbe.tar.gz` (dated
immutable builds) and `.../current/kg-microbe.tar.gz`, KGX TSV node/edge files inside.

**Licence: BSD-3-Clause**, verified live 2026-09-07 via the GitHub API
(`"spdx_id": "BSD-3-Clause"`). Note the raw `LICENSE` path on `master` returned 404, so the
licence is asserted by GitHub's detector rather than read from the file; confidence **medium**
for the exact text, **high** for the identifier. Some inputs carry their own terms — the
download file's own comments name MicrobeDecoder as CC BY 4.0 and PREGO as CC-BY, and KEGG
requires a manual cache step precisely because KEGG bulk access is licensed.

**Relevance.** Not a natural-product source, but the closest thing in this cluster to the
producer-organism half of the target schema, and its BSD/CC-BY posture is compatible.

#### 4.3 PrimeKG

**What it is.** A precision-medicine knowledge graph from the Zitnik lab (MIMS Harvard),
https://github.com/mims-harvard/PrimeKG. Published in *Scientific Data* 2023. Over 100,000
nodes and **4,050,249 relationships** across 17,080 diseases, integrating 20 resources
including CTD, DisGeNET, DrugBank, DrugCentral, Bgee, NCBI Gene, GO, HPO, MONDO, Reactome,
SIDER, UBERON and UMLS. Dataset version 2, released **2022-05-02**. Verified live 2026-09-07
via the GitHub page and the Harvard Dataverse API.

**Contribution to a structure-keyed NP KB: none.** No natural products, no producer
organisms, no biosynthesis. Drug nodes are DrugBank identifiers. Structures are not carried.

**Bulk access.** CSV via Harvard Dataverse, DOI 10.7910/DVN/IXA7BM; also through Therapeutics
Data Commons and PyKEEN loaders.

**Licence.** Code **MIT** ("PrimeKG codebase and associated tools are released under the MIT
license"). Dataverse record stamped **CC0 1.0** — verified live 2026-09-07 via the Dataverse
API, which returns `"rightsIdentifier": "CC0-1.0"`.

**Licence trap, flagged deliberately.** A CC0 stamp on a dataset that redistributes DrugBank
(CC BY-NC 4.0 for the academic release, with a commercial licence otherwise) and DisGeNET
(NC-SA) cannot be taken at face value. The depositor cannot CC0 rights they do not hold. Treat
PrimeKG as **RESTRICTED** for onward redistribution regardless of the Dataverse label.
Confidence **high** on the label, **high** on the reasoning, **medium** on the current DrugBank
and DisGeNET terms since neither was verified live this session.

#### 4.4 SPOKE

**What it is.** Scalable Precision Medicine Open Knowledge Engine, UCSF (Baranzini lab),
https://spoke.ucsf.edu/. A "database of databases" integrating 19 sources including ChEMBL,
DrugBank, SIDER, LINCS, GWAS Catalog and iRefIndex, plus de-identified UCSF clinical data.

**Access: gated.** The site offers a Neighborhood Explorer browser tool. Verbatim from the
site (verified live 2026-09-07 at https://spoke.ucsf.edu/): "SPOKE is available for both
academic and commercial use", with licensing enquiries directed to Mate Bioservices. No public
bulk download and no open licence is offered on the page.

**Classification: RESTRICTED / bespoke licence.** Not seedable. Also contains no natural
products or producer organisms.

#### 4.5 Bioteque

**What it is.** A resource of precomputed **embeddings** (descriptors) over a biomedical
knowledge graph, from the Structural Bioinformatics and Network Biology group at IRB
Barcelona, https://bioteque.irbbarcelona.org/. Downloads are HDF5 descriptor files, analytical
cards and nearest-neighbour networks per metapath. Verified live 2026-09-07.

**Contribution: none.** Embeddings are not records. No structures, no natural products, no
producer organisms, no licence stated on the download page.

**Classification: UNVERIFIED.** Not relevant to this KB.

---

## Refuted or unverifiable claims

- **Refuted: "NP-KG contains natural products."** It contains *botanical* entities and named
  constituents. It does not contain natural products as chemical structures. No InChIKey,
  InChI, SMILES, PubChem CID, UNII or CAS appears in its ontology extension, verified by grep
  over the primary OWL file on 2026-09-07.
- **Refuted: "NP-KG has 745,512 nodes."** That is the 2023 paper's figure for the original
  version. The current v3.0.0 has 1,089,139 nodes and 7,836,115 edges.
- **Refuted: "The GRAPE one-liner loads current NP-KG."** `from grape.datasets.zenodo import
  NPKG` is documented in the README as loading **v1.0.1**.
- **Refuted: "The CC BY 4.0 licence on the NP-KG paper/dataset makes NP-KG seedable."** The
  arXiv preprint is CC BY 4.0 and the Zenodo record is stamped CC BY 4.0, but the merged graph
  redistributes CTD and DisGeNET content whose own terms are more restrictive. A depositor's
  licence stamp does not clear upstream rights.
- **Unverifiable this session: CTD's exact legal text.** https://ctdbase.org/about/legal.jsp
  is behind a human-verification gate that returned only the gate message to both `curl` and
  WebFetch on 2026-09-07. The commercial-use prohibition is reported consistently by search
  summaries and by reusabledata.org, but I did not read the primary page. **Re-verify in a
  browser before relying on it.**
- **Unverifiable this session: DisGeNET's licence.** `disgenet.org/legal` 301-redirects to
  `disgenet.com/Legal`, which returned only a page title. The CC BY-NC-SA 4.0 attribution for
  the legacy academic release is from memory, not from a live page.
- **Unverifiable this session: NaPDI repository terms of use.** All NaPDI hosts fail DNS.
  `web.archive.org` is not fetchable by this session's tooling, so I could not read the June
  2026 snapshots.
- **Unverifiable: the JBI version of record.** ScienceDirect returned HTTP 403. The arXiv
  preprint (2209.11950, CC BY 4.0) was used instead, and the abstract figures match the
  published ones reported elsewhere.
- **Not claimed: PMC10120397 is not the NP-KG paper.** A WebFetch of that PMC identifier
  returned an unrelated STAR Protocols article about murine brain cultures. Do not cite it.

## Open questions

1. **Is the NaPDI outage permanent?** The domains lapsed sometime between 2026-06-16 and
   2026-09-07. If NaPDI's constituent characterisation data is wanted, someone should ask
   Richard Boyce or Sanya Taneja directly whether the repository will return or has been
   archived. (I have not contacted anyone and am not proposing to.)
2. **What exactly does CTD's current legal notice say?** This single question decides whether
   any PheKnowLator-derived graph, NP-KG and PrimeKG included, can ever be redistributed. It
   needs a browser session.
3. **How many of NP-KG's 460 ChEBI-mapped constituents are structure-complete ChEBI entries
   with an InChIKey, versus ChEBI class terms?** At least three constituent names in the list
   are plainly class terms (`sesquiterpenes`, `triterpenes`, `glucose 3-o-glycosides`). A
   resolution pass against a ChEBI dump would give the real number. I did not run one, since
   the answer only affects how large a "nothing new here" set is.
4. **Do the 153 name-only constituents resolve to structures elsewhere?** They came from GSRS,
   which is US public domain and does carry structures and UNIIs. Going back to **GSRS
   directly** would be a far better use of effort than mining NP-KG, and would produce
   structure-keyed records with a clean public-domain licence. This is the actionable lead
   from this whole cluster.
5. **Is the ENPKG whole-graph dump published under one licence?** Individual Zenodo plate
   deposits differ (one CC BY 4.0, one CC0). A combined-graph deposit, if it exists, was not
   located.
6. **Does any NP-specific KG published since 2023 carry curated structure-plus-producer
   records under a seedable licence?** I found none in this cluster. NPBS Atlas (J Cheminform
   2025) and Natural Products Atlas 3.0 (NAR 2025) are databases rather than KGs and belong to
   the structures cluster, not this one.

## Sources

- https://github.com/sanyabt/np-kg
- https://raw.githubusercontent.com/sanyabt/np-kg/main/README.md
- https://raw.githubusercontent.com/sanyabt/np-kg/main/LICENSE
- https://raw.githubusercontent.com/wiki/sanyabt/np-kg/v3.0.0.md
- https://raw.githubusercontent.com/wiki/sanyabt/np-kg/v2.0.0.md
- https://raw.githubusercontent.com/wiki/sanyabt/np-kg/Natural-Products-in-KG.md
- https://raw.githubusercontent.com/sanyabt/np-kg/main/resources/ontology-extensions/chebi-extensions-constituents-20240229.tsv
- https://raw.githubusercontent.com/sanyabt/np-kg/main/resources/ontology-extensions/chebi-extensions-constituents-NP-20240229.tsv
- https://raw.githubusercontent.com/sanyabt/np-kg/main/resources/ontology-extensions/chebi-extensions-instance-20240229.owl
- https://raw.githubusercontent.com/sanyabt/np-kg/main/resources/resource_info.txt
- https://raw.githubusercontent.com/sanyabt/np-kg/main/resources/edge_source_list.txt
- https://github.com/sanyabt/np-kg/tree/main/resources/data
- https://zenodo.org/api/records/12536780
- https://api.datacite.org/dois/10.5281/zenodo.12536780
- https://doi.org/10.5281/zenodo.12536780
- https://arxiv.org/abs/2209.11950
- https://doi.org/10.1016/j.jbi.2023.104341
- https://pubmed.ncbi.nlm.nih.gov/40502231/
- https://doi.org/10.5281/zenodo.5736386
- https://github.com/callahantiff/PheKnowLator
- https://raw.githubusercontent.com/callahantiff/PheKnowLator/master/README.rst
- https://raw.githubusercontent.com/callahantiff/PheKnowLator/master/LICENSE
- https://raw.githubusercontent.com/callahantiff/PheKnowLator/master/resources/edge_source_list.txt
- https://raw.githubusercontent.com/callahantiff/PheKnowLator/master/resources/ontology_source_list.txt
- https://arxiv.org/abs/2307.05727
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7543481/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5944177/
- https://ctdbase.org/about/legal.jsp (gated)
- https://reusabledata.org/ctd.html
- https://disgenet.com/Legal (no content returned)
- https://github.com/enpkg
- https://pubs.acs.org/doi/10.1021/acscentsci.3c00800
- https://enpkg.commons-lab.org/graphdb/
- https://api.datacite.org/dois/10.5281/zenodo.10018590
- https://api.datacite.org/dois/10.5281/zenodo.10282053
- https://github.com/Knowledge-Graph-Hub/kg-microbe
- https://raw.githubusercontent.com/Knowledge-Graph-Hub/kg-microbe/master/download.yaml
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13536490/
- https://github.com/mims-harvard/PrimeKG
- https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId=doi:10.7910/DVN/IXA7BM
- https://spoke.ucsf.edu/
- https://bioteque.irbbarcelona.org/
