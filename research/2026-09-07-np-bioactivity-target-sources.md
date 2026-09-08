# Bioactivity, molecular target, pharmacology and ethnopharmacology resources for a structure-keyed natural products KB

Research date: **2026-09-07**. All "verified live" claims were fetched from the primary page on that date; URLs given inline.

Licence classes used: `CC0_OK` (public domain / CC0), `ATTRIBUTION` (CC BY, seedable into a CC BY 4.0 corpus), `SHARE_ALIKE` (CC BY-SA / ODbL — **not seedable**), `NON_COMMERCIAL` (**not seedable**), `RESTRICTED` (bespoke or all-rights-reserved terms — **not seedable**), `UNVERIFIED` (no licence statement found — **not seedable**, and "no statement" is not "free").

---

## Summary

**The headline finding for this cluster is that almost every large curated bioactivity resource is share-alike, non-commercial, or unlicensed.** ChEMBL, the Guide to PHARMACOLOGY and DrugCentral are all copyleft; DrugBank, IMPPAT, FooDB and Phenol-Explorer are non-commercial; NPASS, TTD, SymMap and HERB state no licence at all; CO-ADD, despite branding itself "open-access", carries an all-rights-reserved UQ copyright notice that explicitly forbids systematic download.

Only four sources in this cluster can actually seed measured bioactivity or targets into a CC BY 4.0 corpus:

| Source | Class | What it seeds | Scale of the usable slice |
|---|---|---|---|
| **BindingDB (own-curated subset)** | ATTRIBUTION (CC BY 3.0) | Ki/IC50/Kd/EC50 with pH, temperature, target organism, UniProt, PMID | 93,712 rows / 46,304 distinct InChIKeys in the curated-articles file |
| **PubChem BioAssay** | CC0_OK (with depositor caveat) | Assay results, dose-response, assay descriptions | 300,270,330 bioactivity rows over 1,980,801 assays |
| **Open Targets Platform** | CC0_OK (platform output) | Target-disease associations, drug mechanism of action, clinical phase | Release 26.06 (2026-06-25) |
| **Dr. Duke's (USDA)** | CC0_OK | Plant-chemical-activity triples, ethnobotanical uses | Frozen; developed 1992-2016 |

NCI DTP / NCI-60 is very likely usable (US federal, NCI states its text is "free of copyright") but has no explicit data licence, so it is a policy-inference rather than a licence grant.

**The single most important practical result**: BindingDB separates its own CC BY 3.0 curation into a dedicated download (`BindingDB_BindingDB_Articles_*_tsv.zip`), and that file carries Standard InChIKey in column 4 and UniProt accessions per target chain. It is the only large, cleanly-licensed, structure-keyed, measured-affinity dataset in this cluster. I downloaded and profiled it (canary verified, see §2).

Two further findings worth escalating: the **ChEMBL `natural_product` flag is unreliable** — prazosin, a fully synthetic quinazoline, is flagged `natural_product=1` in ChEMBL 37 (verified by API call) — and **NAPRALERT is currently offline**, with its own site saying "Currently Unavailable".

---

## Per-source findings

### 1. ChEMBL

**1. What it is.** Manually curated bioactivity database of drug-like molecules, maintained by EMBL-EBI (Hinxton, UK).

- Current release: **ChEMBL 37, database prepared 01/05/2026**, files posted 2026-05-29. Verified live 2026-09-07 at `https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_37_release_notes.txt`. Confidence: high.
- Size, verbatim from the release notes:
  ```
  2,921,148 compounds (of which 2,897,819 have mol files)
  3,824,604 compound records (non-unique compounds)
  24,527,044 activities
  1,970,438 assays
  18,552 targets
  101,100 documents
  ```
- **Natural products flagged**: I queried the ChEMBL API live on 2026-09-07:
  - `natural_product=1` → **98,989** molecules
  - `natural_product=0` → 2,822,159 molecules

  (`https://www.ebi.ac.uk/chembl/api/data/molecule.json?natural_product=1&limit=1`, reading `page_meta.total_count`). Confidence: high.
- The NP flag was reimplemented at release 33 based on mappings to COCONUT; ~64,000 molecules were flagged at ChEMBL 33, so the flag has grown by roughly half again since. Confidence: medium — the release-33 figure comes from the ChEMBL 2023 NAR paper via search, not from a page I fetched directly.
- `np_likeness_score` lives on `COMPOUND_PROPERTIES`, not `MOLECULE_DICTIONARY`. It is the Ertl/Roggo/Schuffenhauer 2008 score as implemented in RDKit, trained on ~50,000 natural products from open databases and ~1 million ZINC drug-like molecules. Range in ChEMBL 32 was -4.1 to 4.1, median -1.0. Verified live 2026-09-07 at `http://chembl.blogspot.com/2023/03/natural-product-likeness-in-chembl.html`. Confidence: high for the method, medium for the exact range (that was ChEMBL 32, not 37).

**2. What it would contribute.** Measured activities with full assay context: assay description, assay organism, target, standard type/relation/value/units, and the source document. Curated from the primary literature plus deposited datasets. This is the richest assay-context resource in the cluster. Fields are curated, not predicted, though `standard_value` normalisation is automated.

Notably, ChEMBL 37 already ingests several screening sets directly relevant to NP work, with counts verbatim from the release notes:

| Deposited source | Assays | Compound records | Activities |
|---|---|---|---|
| CO-ADD Antimicrobial Screening | 35 | 24,315 | 99,793 |
| PubChem BioAssays | 2,999 | 531,694 | 7,434,992 |
| BindingDB Patent Bioactivity Data | 13,835 | 641,469 | 2,682,137 |
| Drugs for Neglected Diseases Initiative | 233 | 7,070 | 14,452 |
| MMV Malaria Box | 138 | 8,438 | 45,158 |
| MMV Pathogen Box | 88 | 1,574 | 6,256 |

**3. Identifiers carried.** ChEMBL ID, Standard InChI and Standard InChIKey, canonical SMILES, UniProt (via `chembl_uniprot_mapping.txt`), PubChem CID via UniChem, NCBI Taxonomy for assay and target organisms. Joinability to a structure-keyed corpus is excellent.

**4. Bulk access.** FTP at `https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/`. Formats: SQLite (5.4 GB), MySQL (2.0 GB), PostgreSQL (1.9 GB), SDF (888 MB), FASTA, `chembl_37_chemreps.txt.gz` (279 MB, structures only), RDF/turtle in a parallel tree. Versioned by integer release number with dated release notes. Verified live 2026-09-07.

**5. LICENCE: `SHARE_ALIKE` — NOT SEEDABLE.**

The FTP tree ships a `LICENSE` file whose first lines read, verbatim:

> ```
> Creative Commons
>
> Attribution-ShareAlike 3.0 Unported
> ```

and a `REQUIRED.ATTRIBUTION` file which reads, verbatim:

> "The data in ChEMBL is covered by the licence in the file LICENSE.
>
> Under the -BY clause, we request attribution for subsequent use of ChEMBL.
> [...]
> If ChEMBL is incorporated into other works, we ask that the ChEMBL IDs are preserved, and that the release number of ChEMBL is clearly displayed."

The interface documentation states the same: "Creative Commons Attribution-Share Alike 3.0 Unported License". Verified live 2026-09-07 at `https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/LICENSE`, `.../REQUIRED.ATTRIBUTION`, and `https://chembl.gitbook.io/chembl-interface-documentation/about`. Confidence: high.

CC BY-SA 3.0 is copyleft. Records derived from ChEMBL cannot be redistributed under CC BY 4.0. **Curate-only at best** — ChEMBL is usable as a lookup to guide manual curation from the underlying primary literature, but its records cannot be copied into the corpus.

**6. Data-quality traps.**

- **The `natural_product` flag has false positives.** Verified live 2026-09-07: `CHEMBL2` is **PRAZOSIN** (InChIKey `IENZQIKPVFGBNW-UHFFFAOYSA-N`, SMILES `COc1cc2nc(N3CCN(C(=O)c4ccco4)CC3)nc(N)c2cc1OC`), a wholly synthetic quinazoline α1-adrenoceptor antagonist, and it carries `natural_product=1` with `np_likeness_score=-1.29`. The flag and the likeness score actively disagree on this record. Any pipeline that trusts `natural_product=1` as an NP definition will import synthetic drugs. Confidence: high, verified by direct API call.
- Salt and parent forms are separate ChEMBL IDs linked by `molecule_hierarchy`; activities attach to whichever form the paper reported. Failing to resolve to `parent_chembl_id` double-counts and splits structures.
- `standard_value` is normalised but `activity_comment` free text ("inactive", "not determined") carries meaning that the numeric columns do not.
- Assays on whole organisms and cell lines sit alongside molecular-target assays; `assay_type` and `confidence_score` must be read before treating a row as a molecular-target measurement.

---

### 2. BindingDB

**1. What it is.** "The first public molecular recognition database" — measured binding affinities of small molecules to proteins. Run as a nonprofit project (UC San Diego / Skaggs, Gilson group).

- Live counts, verbatim from the site header on 2026-09-07: "BindingDB contains 3.2M data for 1.4M Compounds and 11.5K Targets. Of those, 1.6M data for 772K Compounds and 4.8K Targets were curated by BindingDB curators." The Info page gives the precise figures: **3,241,782 binding data for 11,509 proteins and over 1,440,011 drug-like molecules**.
- Current data snapshot: **202609**, files updated 2026-08-30; latest release note dated 2026-08-22. Verified live 2026-09-07 at `https://www.bindingdb.org/rwd/bind/info.jsp` and `https://www.bindingdb.org/rwd/bind/chemsearch/marvin/Download.jsp`. Confidence: high.

**2. What it would contribute.** Measured affinities with unusually good measurement context: Ki, IC50, Kd, EC50, kon, koff, plus **pH and temperature** columns — which almost no other resource in this cluster carries. Target source organism is recorded per measurement. All curated, none predicted.

**3. Identifiers carried.** I downloaded the curated-articles TSV and read the header live on 2026-09-07. The file has **640 columns**; the first 51 include:

```
0  BindingDB Reactant_set_id
1  Ligand SMILES
2  Ligand InChI
3  Ligand InChI Key
6  Target Name
7  Target Source Organism According to Curator or DataSource
8  Ki (nM)      9  IC50 (nM)     10 Kd (nM)     11 EC50 (nM)
12 kon (M-1-s-1) 13 koff (s-1)   14 pH          15 Temp (C)
16 Curation/DataSource
17 Article DOI  18 BindingDB Entry DOI  19 PMID  20 PubChem AID  21 Patent Number
31 PubChem CID  32 PubChem SID  33 ChEBI ID of Ligand  34 ChEMBL ID of Ligand
35 DrugBank ID of Ligand  36 IUPHAR_GRAC ID of Ligand  37 KEGG ID  38 ZINC ID
40 BindingDB Target Chain Sequence 1
44 UniProt (SwissProt) Primary ID of Target Chain 1
49 UniProt (TrEMBL) Primary ID of Target Chain 1
```

Standard InChIKey is a first-class column. Joinability to a structure-keyed corpus is the best in this cluster.

**4. Bulk access.** `https://www.bindingdb.org/rwd/bind/chemsearch/marvin/Download.jsp`. TSV, 2D SDF, 3D SDF, and MySQL dump. Updated roughly monthly, versioned `YYYYMM`. Long-term DOI-bearing archives are deposited quarterly at UC San Diego Library digital collections (`https://library.ucsd.edu/dc/collection/bb03870458`) — the site explicitly recommends citing the archive for reproducible use.

Crucially, **the downloads are split by provenance**, which is what makes the licence separable:

- `BindingDB_BindingDB_Articles_202609_tsv.zip` (17.43 MB) — "Only data curated from articles by BindingDB"
- `BindingDB_ChEMBL_202609_tsv.zip` (329.14 MB) — ChEMBL-derived
- `BindingDB_Patents_202609_tsv.zip` (163.71 MB)
- `BindingDB_PubChem_202609_tsv.zip` (22.03 MB)
- `BindingDB_PDSPKi_202609_tsv.zip`, `BindingDB_CSAR_*`, `BindingDB_ITC_*`, `BindingDB_Covid-19_*`
- Assay text lives separately: `BindingDB_Assays_202609_tsv.zip` joined via `BindingDB_rsid_eaids_202609_tsv.zip`

**5. LICENCE: split — the own-curated subset is `ATTRIBUTION` (CC BY 3.0) and IS SEEDABLE.**

Verbatim from `https://www.bindingdb.org/rwd/bind/info.jsp`, verified live 2026-09-07:

> "Data imported from ChEMBL are provided under their Creative Commons Attribution-Share Alike 3.0 Unported License. All data curated by BindingDB staff are provided under the Creative Commons Attribution 3.0 License."

Confidence: high. CC BY 3.0 is one-way compatible into a CC BY 4.0 release with attribution preserved.

**Canary result (performed 2026-09-07).** I downloaded `BindingDB_BindingDB_Articles_202609_tsv.zip` (18,272,073 bytes) and profiled it end to end:

| Metric | Value |
|---|---|
| Rows | 93,712 |
| Distinct Ligand InChIKeys | 46,304 |
| Rows with IC50 | 63,525 |
| Rows with Ki | 25,790 |
| Rows with EC50 | 4,230 |
| Rows with Kd | 2,650 |

`Curation/DataSource` values present in that file: `Curated from the literature by BindingDB` (93,023), `ChEMBL` (429), `Taylor Research Group, UCSD` (260). Top target source organisms: *Homo sapiens* 58,540; SARS-CoV-2 5,579; HIV-1 5,528; *Rattus norvegicus* 3,187; *Bos taurus* 2,235; *Mus musculus* 1,500.

**Two operational warnings from that canary.**

- The "BindingDB Articles" file is **not 100% BindingDB-curated**: 429 of its rows are labelled `ChEMBL` and are therefore CC BY-SA. A licence-clean extraction must filter on `Curation/DataSource == "Curated from the literature by BindingDB"`, not merely on the filename.
- 93,712 rows is far short of the 1.6M "curated by BindingDB curators" the front page advertises. The larger figure evidently includes BindingDB's patent curation (the patents file is 163 MB) and other streams that are not in the articles download. **Do not assume the whole 1.6M is available as CC BY 3.0 in one file** — only the articles subset is packaged that way, and the licensing of the patent-curated stream is not separately stated on the page I read. Confidence: high that the articles file is 93,712 rows; medium-low on how the remaining ~1.5M curated points are licensed, which is an open question below.

**6. Data-quality traps.** Multi-chain targets spread UniProt IDs across ~600 columns (chains 1..N), so naive single-column parsing loses complexes. Affinities are reported with relational operators embedded as leading `>` or `<` characters inside the numeric cell (e.g. `> 10000`), so the columns are not clean floats. The same publication may appear via both the articles and the ChEMBL routes, producing near-duplicate measurements under different licences.

---

### 3. PubChem BioAssay

**1. What it is.** NCBI/NLM's public repository of chemical substances and bioactivity screening results, populated by depositors.

- Live counts, queried 2026-09-07 via the PubChem SDQ endpoint:
  - Compounds (CIDs): **124,663,070**
  - BioAssays: **1,980,801**
  - Bioactivity rows: **300,270,330**
  - (`https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi` with `collection` = `compound`, `bioassay`, `bioactivity`.) Confidence: high.
- FTP bioassay tree last modified 2026-07-15; `assay.ftpdump.history` updated 2026-08-25. Verified live at `https://ftp.ncbi.nlm.nih.gov/pubchem/Bioassay/`.

**2. What it would contribute.** Raw and normalised screening results with assay descriptions, activity outcome calls, dose-response where deposited, and depositor provenance. It is the largest volume of measured bioactivity available anywhere without a copyleft encumbrance. Everything is deposited, not predicted — but deposited quality varies enormously by depositor.

**How to identify NP-relevant assays.** PubChem itself has **no natural-product flag** on compounds or assays. There is no single filter. The practical routes are:

- **Structure-first (recommended).** Take an NP structure set keyed by Standard InChIKey — LOTUS, COCONUT, NPAtlas, NPASS — resolve it to CIDs, then pull bioactivities for those CIDs. LOTUS is present in PubChem as a substance source (`https://pubchem.ncbi.nlm.nih.gov/source/25132`, "LOTUS - the natural products occurrence database"), which makes the CID resolution a lookup rather than a structure-matching exercise. Confidence: medium-high — I confirmed the source page exists but did not enumerate its substance count.
- **Depositor-first.** Filter assays by depositor for NP-heavy screening programmes: NCI DTP (the NCI-60 and prescreen data are mirrored into PubChem), NIAID, Scripps, Broad. This catches extract and fraction screens as well as pure compounds, which is a mixed blessing.
- Both routes should be used together; neither alone is complete.

**3. Identifiers carried.** CID, SID, Standard InChIKey, canonical and isomeric SMILES, AID, and depositor-supplied target annotations (often a UniProt accession or a GI, inconsistently). Structure-keyed joins are straightforward via InChIKey.

**4. Bulk access.** FTP at `https://ftp.ncbi.nlm.nih.gov/pubchem/Bioassay/` in ASN.1, JSON, and XML (the CSV and Concise trees have not been refreshed since 2021-03-08 — use JSON or ASN.1). Also PUG-REST and the SDQ agent for programmatic queries. No release numbering; the tree is continuously updated with dated directories.

**5. LICENCE: `CC0_OK`, with a real depositor caveat.**

NCBI's policy page states, verbatim (verified live 2026-09-07 at `https://www.ncbi.nlm.nih.gov/home/about/policies/`):

> "Information that is created by or for the US government on this site is within the public domain."

and, for molecular databases:

> NCBI places "no restrictions on the use or distribution of the data contained therein."

But the same page names PubChem specifically in its third-party caveat:

> some NCBI resources incorporate "material contributed or licensed by individuals, companies, or organizations that may be protected by U.S. and foreign copyright laws"

Confidence: high for the quotes; medium for the practical conclusion. PubChem is a **deposition** archive, so the operative licence is the depositor's, not NCBI's. In practice the bulk of BioAssay content is government or academic screening output that is freely redistributable, but a KB that seeds from PubChem should record the depositor per assay so that any later challenge can be traced. Treat PubChem as CC0-compatible **at the level of the individual depositor**, and avoid re-exporting assays whose depositor is a commercial vendor.

**6. Data-quality traps.**

- Assay results deposited on **substances** (SIDs), some of which are mixtures, extracts, or salts; the SID-to-CID standardisation can attach an extract's activity to a single parsed constituent.
- Primary single-concentration screens sit alongside confirmatory dose-response with no consistent flag; "Active" in a primary screen is a hit call, not a measured potency.
- Many AIDs carry no units and no method beyond a free-text description.
- Depositor target annotations are frequently absent, and where present are sometimes the intended target rather than the assayed one.

---

### 4. NPASS

**1. What it is.** Natural Product Activity and Species Source database — links natural products to biological targets via experimental quantitative activity data. Maintained by the BIDD group (Prof. Chen Yu Zong; maintainer Hanbo Lin; PI A/Prof. Zeng Xian), hosted at Fudan University, Shanghai; servers in China.

- Version **3.0**, site states released 2025-06-15; the accompanying NAR paper ("NPASS database update 2026") published 2025-11-17 in *Nucleic Acids Research* 54(D1):D1519. The site brands the current data as "NPASS-2026". Verified live 2026-09-07 at `https://bidd.group/NPASS/index.php`. Confidence: high.
- Headline counts from the site: 204,023 natural products; 1,048,756 activity records; 8,764 biological targets; 48,940 source organisms; 208,415 composition records. The paper adds 9,713 ADME records for 744 NPs and 34,975 toxicity records for 3,662 NPs, drawn from 1,822 manually reviewed publications.

**2. What it would contribute.** This is, on paper, the closest fit to the KB's shape: natural products keyed by structure, connected to targets, with quantitative activity and a species source. **I downloaded and profiled the actual files on 2026-09-07** rather than trusting the counts.

`NPASS3.0_activities.txt` (105,252,592 bytes, 1,048,755 data rows) columns:

```
np_id  target_id  activity_type_grouped  activity_relation  activity_type
activity_value  activity_units  assay_organism  assay_tax_id  assay_strain
assay_tissue  assay_cell_type  ref_id  ref_id_type
```

Example row: `NPC46644  NPT918  Kd  =  Kd  26  nM  Homo sapiens  9606  n.a.  n.a.  n.a.  23362862  PMID`.

This is genuinely good assay context — organism with NCBI tax ID, strain, tissue, cell type, and a PMID per record.

Measured distributions from my profiling:

| Activity type | Records |
|---|---|
| Others | 547,786 |
| IC50 | 181,506 |
| MIC | 123,914 |
| GI50 | 68,120 |
| Potency | 58,529 |
| EC50 | 20,548 |
| ED50 | 16,326 |
| Ki | 15,365 |
| Kd | 14,547 |
| AC50 | 2,115 |

| Units | Records |
|---|---|
| nM | 448,509 |
| ug.mL-1 | 211,385 |
| % | 181,314 |
| n.a. (missing) | 80,426 |
| ug ml-1 | 18,540 |
| cells.uL-1 | 13,813 |
| mm | 12,010 |
| uM | 8,674 |

Assay organisms: *Homo sapiens* 330,439; missing 188,114; *Rattus norvegicus* 142,871; *Mus musculus* 49,087; *Staphylococcus aureus* 35,577; *Escherichia coli* 25,744; *Pseudomonas aeruginosa* 14,056; *Candida albicans* 11,410. The bacterial and fungal counts make NPASS the best single source of MIC data for natural products that I found.

`NPASS3.0_target.txt` (8,763 targets) columns: `target_id, target_type, target_name, target_organism_tax_id, target_organism, uniprot_id`. **Only 5,056 of 8,764 targets (58%) carry a UniProt accession.** Target types:

| Target type | Count |
|---|---|
| Individual protein | 2,927 |
| Organism | 1,879 |
| Cell line | 1,639 |
| Single protein | 1,377 |
| Protein complex | 343 |
| Protein family | 246 |
| Tissue | 129 |
| Protein-protein interaction | 71 |
| Others | 40 |
| Selectivity group | 27 |

**3. Identifiers carried.** `NPASS3.0_naturalproducts_structure.txt` (64,734,351 bytes, 203,390 rows) has exactly four columns: `np_id, InChI, InChIKey, SMILES`. Zero rows are missing an InChIKey; there are **203,290 distinct InChIKeys across 203,390 rows**, so 100 rows share a key with another. The general-info file carries cross-references to other resources. Targets carry UniProt where available; organisms carry NCBI Taxonomy IDs. The NAR paper states "InChIKeys were used as unique identifiers", ChEMBL target entries for proteins, and "NCBI Taxonomy IDs were employed for consistent mapping".

Joinability is excellent — this is a natively InChIKey-keyed resource.

**4. Bulk access.** Plain HTTP file downloads from `https://bidd.group/NPASS/downloadnpass.html`, under `./downloadFiles/`. Eleven files: general info, physicochemical properties, structure (TXT and SDF in rar/zip), activity records, species source, target info, species taxonomy, toxicity, and four specialised sets (symbiont, elicitation, coculture, engineered organisms). TSV/TXT. Versioned only by the "3.0" in the filenames; no DOI, no dated snapshots, no changelog. Previous versions (1.0, 2.0) remain downloadable.

The download page has a visible defect: entries 7 through 11 all point at "Species Taxonomic Information (~3.13 MB)" with identical descriptions, so the listing does not match the eleven distinct datasets the page claims. Verified live 2026-09-07. Confidence: high.

**5. LICENCE: `UNVERIFIED` — NOT SEEDABLE.**

I checked the front page, the download page, and the privacy policy. **No licence, terms-of-use, or copyright statement exists anywhere on the NPASS site.** The privacy policy (`https://bidd.group/NPASS/privacy_policy.php`) governs only personal data of contributors — it covers GDPR-style rights over submitter names and emails and says "Our primary mission is to serve as an open-access resource for biomedical research", but it grants no rights over the database contents. `https://bidd.group/NPASS/about.html` returns 404.

Verified live 2026-09-07. Confidence: high that no licence is stated.

Calling itself "open-access" in prose is not a licence. **NPASS is the single biggest missed opportunity in this cluster** — it is InChIKey-keyed, has a million measured activities with assay organism and PMID, and covers MICs against ESKAPE-relevant pathogens that nothing else covers as well. It is worth writing to the maintainers (Hanbo Lin, hanbolin@u.nus.edu; Prof. Zeng Xian, zengxian@fudan.edu.cn) to ask them to apply CC BY 4.0. Until then it is curate-only.

**6. Data-quality traps.**

- **`Others` is the largest activity type at 547,786 records (52%)** — over half the database is not a recognised potency measurement.
- **80,426 records (7.7%) have no units at all** (`n.a.`), and a further 181,314 are dimensionless percentages that are meaningless without the tested concentration.
- **188,114 records (18%) have no assay organism.**
- Unit strings are not normalised: `ug.mL-1` and `ug ml-1` are the same unit spelled two ways, splitting 229,925 records across two tokens. `mm` (12,010 records) is presumably zone-of-inhibition diameter, which is not a potency at all.
- **Target vocabulary is internally inconsistent**: "Individual protein" (2,927) and "Single protein" (1,377) are evidently the same concept under two labels, which will fragment any target-type filter.
- 42% of targets have no UniProt accession, and 3,647 "targets" are whole organisms, cell lines, or tissues rather than molecular targets. A KB field named "molecular target" must not be populated from these rows unindexed.
- 100 InChIKey collisions across rows mean np_id is not 1:1 with structure.

---

### 5. CO-ADD (Community for Open Antimicrobial Drug Discovery)

**1. What it is.** Not-for-profit open screening initiative led by academics at the Institute for Molecular Bioscience, The University of Queensland, funded in part by Wellcome. Offers free primary screening of submitted compounds against five ESKAPE bacteria and two fungi, and publishes the results after a confidentiality period.

- Verified live 2026-09-07 at `https://www.co-add.org/` and `https://db.co-add.org/`.
- The site does not publish a compound count on any page I could reach. Confidence: high that the count is not stated; the database front page is a JavaScript application whose statistics I could not extract without executing scripts.
- Indirect scale, from ChEMBL 37's release notes: the "CO-ADD Antimicrobial Screening" deposition into ChEMBL comprises **35 assays, 24,315 compound records, 99,793 activities**. Confidence: high for the ChEMBL-deposited slice, which is a lower bound on CO-ADD's total.

**2. What it would contribute.** Primary antimicrobial screening (growth inhibition) and dose-response MICs against a defined ESKAPE panel plus *Candida albicans* and *Cryptococcus neoformans*, with cytotoxicity and haemolysis counter-screens. Uniform protocol across all compounds, which is rare and valuable. All measured, none predicted. No molecular targets — this is phenotypic whole-cell data.

**3. Identifiers carried.** Chemical structure as SMILES in the CSV and as connection tables in the SDF. Whether Standard InChIKey is a column I could not confirm without downloading, and the download links are JavaScript-driven form posts rather than static URLs. Confidence: low on the exact identifier set.

**4. Bulk access.** `https://db.co-add.org/downloads`, which states verbatim (verified live 2026-09-07):

> "The complete knowledge base is available in two different formats, as structure definition file (SDF) and comma separated value (CSV) file containing the chemical structure as SMILES string."

Three offerings: "Complete Data Sets", "Single Concentration Data", "Dose Response Data". No version number, no release date, no DOI on the page.

**5. LICENCE: `RESTRICTED` — NOT SEEDABLE.**

This is the sharpest gap between branding and terms in the whole cluster. The database front page headline reads "Open-access Antimicrobial Screening Database". The only actual terms on the site are at `https://www.co-add.org/?q=content/privacy-copyright`, which state verbatim (verified live 2026-09-07):

> "Copyright (c) 2016 The University of Queensland
>
> (a) unless otherwise indicated, we, together with our licensors, own and control all the copyright and other intellectual property rights in our website and the material on our website under Australian copyright law; and (b) all the copyright and other intellectual property rights in our website and the material on our website are reserved.
>
> For personal, non-commercial purposes, you may view or make copies of the material contained on the site. **Content may not be systematically downloaded, retrieved or stored. Content may not be reproduced or transmitted without our prior written permission.**"

(Emphasis mine.) Confidence: high — I extracted this from the rendered page body, not a summary.

"Content may not be systematically downloaded" is a direct prohibition on the bulk download the same organisation offers, and "may not be reproduced or transmitted without our prior written permission" forecloses redistribution entirely. No Creative Commons licence is named anywhere on the site.

**The one usable route**: CO-ADD's data is *also* deposited into ChEMBL (35 assays / 99,793 activities), where it inherits ChEMBL's CC BY-SA 3.0. That is share-alike, so it is still not seedable into CC BY 4.0 — but it is at least an explicit licence rather than an outright reservation.

**Recommended action**: CO-ADD is a Wellcome-funded open-science project whose terms page appears to be an unmodified university boilerplate from 2016 that contradicts its own mission. A direct request for a CC BY 4.0 grant over the screening data has a good chance of succeeding (`info@co-add.org`). This is probably the highest-value licence request in the cluster after NPASS.

**6. Data-quality traps.** Single-concentration primary screening hits are inhibition percentages, not potencies, and must not be recorded as MICs. Compounds are submitted by third-party chemists whose structure assignments CO-ADD does not independently verify. Purity is submitter-declared.

---

### 6. NCI DTP Natural Products Repository and NCI-60

**1. What it is.** The NCI Developmental Therapeutics Program's Natural Products Branch maintains the Natural Products Repository; the NCI-60 human tumour cell line screen is DTP's long-running cytotoxicity platform.

- Repository holdings, verbatim from `https://dctd.cancer.gov/programs/dtp/organization/npb/npnpd` (verified live 2026-09-07): over **230,000 unique extracts** — 80,000 plant samples from 5,000 unique genera, 25,000 marine invertebrates and algae from 4,000 genera, 25,000 microbial samples from 1,000 genera, collected globally since 1986.
- The NCI Program for Natural Products Discovery (NPNPD) prefractionated library produces subfractions in "assay-ready format" with NMR, LC-MS and FTIR analytical results.
- **NCI-60 data: July 2026 release.** Verified live 2026-09-07 at `https://wiki.nci.nih.gov/spaces/NCIDTPdata/pages/147193864/NCI-60+Growth+Inhibition+Data` (page last updated 2026-07-08).

**2. What it would contribute.** Cell-line cytotoxicity endpoints for a very large, NP-rich compound set. Files and sizes, verbatim from the wiki:

| Dataset | Uncompressed | Download |
|---|---|---|
| Concentration/response data | 2.37 Gb | DOSERESP.zip (332 Mb) |
| GI50 | 401 Mb | GI50.zip (37 Mb) |
| TGI | 396 Mb | TGI.zip (33 Mb) |
| LC50 | 391 Mb | LC50.zip (29 Mb) |
| IC50 | 401 Mb | IC50.zip (35 Mb) |
| One-concentration prescreen | 470 Mb | ONECONC.zip (52 Mb) |

Endpoints are GI50, TGI, LC50 and IC50 per cell line per experiment, with 60 current cell lines plus 11 historical ones. Data is now reported per individual experiment (EXPID) to 4 decimal places rather than aggregated. Measured, not predicted. No molecular targets — the COMPARE algorithm *infers* mechanism from activity-pattern correlation, which is a prediction and must be labelled as one.

**3. Identifiers carried.** **NSC numbers only.** There is no InChIKey, SMILES, or CID in the activity files. Structures for public NSCs are available separately from DTP, and NSC-to-CID mappings exist via PubChem (DTP deposits into PubChem). Joining NCI-60 to a structure-keyed corpus is therefore a two-hop operation with real attrition. Confidence: high.

**4. Bulk access.** `https://dctd.cancer.gov/data-tools-biospecimens/data/bulk-data-downloads` links to the NCI Wiki pages; the July 2026 release files are linked from the growth-inhibition page. Previous releases are archived at a separate wiki page. Public COMPARE at `https://dtp.cancer.gov/public_compare`. ZIP of flat files. Versioned by release month; no DOI.

**5. LICENCE: `CC0_OK` by inference — but no explicit data licence. Treat as medium confidence.**

The bulk-data page carries only a pointer, verbatim:

> "If you would like to reproduce some or all of this content, see Reuse of NCI Information for guidance about copyright and permissions."

The linked NCI policy states, verbatim (verified live 2026-09-07 at `https://www.cancer.gov/policies/copyright-reuse`):

> "Unless otherwise indicated, all text within National Cancer Institute (NCI) products is free of copyright and may be reused without our permission."

with a requirement to credit NCI and, for digital use, link to the original.

Confidence: medium. The policy is written about *text and graphics in NCI products*, not about database records, and NCI never uses the words "public domain" or names a Creative Commons licence. As US federal government work product, the screening data is almost certainly not copyrightable in the US, but that is a legal inference about the absence of copyright rather than a licence grant. **Seedable with an explicit provenance note**, and worth a confirmatory email to DTP if the KB wants a firm footing.

**6. Data-quality traps.** These are unusually well documented by DTP itself, quoting verbatim from the wiki:

- **"NSC numbers are not intended to identify unique chemical structures in the NSC series, though most of them do."** The primary key is not a structure key.
- **"Most NSC numbers represent single, defined small molecules (as either a free base or as a simple salt). Some NSC numbers have been assigned to more complex biological agents, but they have also been assigned to mixtures, extracts, crude fractions, etc."** This is precisely the extract-attributed-to-a-constituent trap, present at the identifier level.
- Units disambiguate this partially: `CONCENTRATION_UNIT` is `M` for small molecules, `u` (µg/mL) for complex biologicals, and `V` for volume-based — and the wiki admits **"There is no further definition regarding what a volume-based concentration means."** Any row with unit `u` or `V` should be excluded from single-compound potency claims.
- **"Additional quality control or consistency checks have not been performed"** beyond lab-level QC at run time.
- Endpoints outside the tested dilution range are reported as the highest or lowest concentration in the series, i.e. **censored values reported as point estimates**. These are not true GI50s and will bias any downstream aggregate.
- Salt versus free base is conflated inside a single NSC.

---

### 7. DrugBank

**1. What it is.** Drug and drug-target database, originating at the University of Alberta (Wishart group), now commercialised through OMx Personal Health Analytics.

- Latest version **5.1.22, released 2026-06-27**. Verified live 2026-09-07 at `https://go.drugbank.com/releases/latest`. Confidence: high.

**2. What it would contribute.** Curated mechanism of action in prose, drug targets with UniProt, pharmacology, clinical/approval status, ATC codes, and drug categories. Strong on mechanism narrative, which few other sources give. Curated, not text-mined.

**3. Identifiers carried.** DrugBank ID, InChIKey, SMILES, UniProt for targets, PubChem CID, ChEBI, KEGG. Good joinability.

**4. Bulk access.** XML and CSV via the releases page, gated behind account registration and a licence agreement. **The page currently states that "All Academic DrugBank dataset downloads are temporarily paused" while the distribution programme is updated** — verified live 2026-09-07. Confidence: high.

**5. LICENCE: `NON_COMMERCIAL` for the main dataset — NOT SEEDABLE. A small CC0 subset exists.**

Two tiers, verbatim from the releases page:

> Most datasets: "Creative Common's Attribution-NonCommercial 4.0 International License"
>
> Open Data datasets: "Creative Common's CC0 International License"

Academic access requires affiliation with an academic institution, research not primarily benefiting commercial entities, and tools built solely for academic purposes. Commercial use requires contacting sales.

Confidence: high.

CC BY-NC 4.0 is incompatible with a CC BY 4.0 release. **The main DrugBank dataset is not seedable.** The separately-published "Open Data" subset (drug names, categories, and a limited identifier vocabulary) is CC0 and *is* seedable, but it carries no bioactivity, no targets, and no mechanism, so it contributes almost nothing to this KB's core content. Note the general trap flagged in my brief: DrugBank's papers are open access, which is not the database licence.

**6. Data-quality traps.** Target lists mix primary pharmacological targets with enzymes, transporters and carriers involved in disposition; treating all four tables as "targets" badly overstates mechanism. Many target assignments have no affinity value attached. Mechanism text is narrative and not machine-parseable into an assertion without curation.

---

### 8. DrugCentral

**1. What it is.** Online drug compendium of approved drugs, from the Oprea group (originally University of New Mexico), the drug layer under the Illuminating the Druggable Genome / Target Central Resource Database.

**2. What it would contribute.** Approved-drug mechanism of action with target UniProt and action type (agonist/antagonist/inhibitor), regulatory approval status across FDA/EMA/PMDA, pharmacologic class, and bioactivity summaries. Curated.

**3. Identifiers carried.** DrugCentral ID, SMILES and InChI, CAS registry, INN names, UniProt for targets. The download page notes the SMILES/InChI file "contains structures in SMILES and InChI formats along with INN names, DrugCentral ids, and CAS registry numbers" — InChIKey is derivable from the InChI. Verified live 2026-09-07.

**4. Bulk access.** `https://drugcentral.org/download`. PostgreSQL dump, TSV of drug-target interactions, SDF in MOL V2000 and V3000, SMILES/InChI file, approved-drug CSVs for FDA/EMA/PMDA, TCRD import files. A public read-only Postgres instance is offered at `drugcentral:unmtid-dbs.net:5433` with credentials published on the page.

**Staleness warning**: the current database dump on the page is dated **11/01/2023 (Postgres v14.5)**, and the site header still reads "DrugCentral 2023". The page also carries a stray note "Drug central in active developement, finalizing frameworks June 29." The footer reads "© 2026". So the site is maintained but **the bulk download is nearly three years old as of today**. Verified live 2026-09-07. Confidence: high.

**5. LICENCE: `SHARE_ALIKE` — NOT SEEDABLE.**

Verbatim from `https://drugcentral.org/privacy` (verified live 2026-09-07):

> "DrugCentral is available under Creative Commons license, download and use of this resource evidences your agreement to all the terms and conditions of license."

The licence linked is **Creative Commons Attribution-ShareAlike 4.0 International**. Confidence: high.

CC BY-SA 4.0 is copyleft and cannot be seeded into a CC BY 4.0 corpus. Curate-only.

**6. Data-quality traps.** Coverage is approved drugs, so natural products appear only where they reached market — a heavily biased slice of NP space. Target action types are curated from labels and literature with variable evidence depth. The 2023 vintage means recent approvals and withdrawals are missing.

---

### 9. IUPHAR/BPS Guide to PHARMACOLOGY (GtoPdb)

**1. What it is.** Expert-curated database of ligand-activity-target relationships, developed at the Centre for Discovery Brain Sciences, University of Edinburgh, led by Prof. Jamie Davies, with Dr Simon Harding as senior developer and curators Dr Jane Armstrong, Dr Elena Faccenda and Dr Christopher Southan. Backed by IUPHAR and the British Pharmacological Society.

- The current companion publication is the Concise Guide to PHARMACOLOGY 2025/26 in the *British Journal of Pharmacology*. Verified live 2026-09-07 at `https://www.guidetopharmacology.org/about.jsp`.
- **I could not obtain current ligand, target, or interaction counts.** Both `statistics.jsp` and `download.jsp` now redirect to a login wall. Confidence: high that the statistics are login-gated; no count reported.

**2. What it would contribute.** The highest-quality expert-curated ligand-target pharmacology available: quantitative affinities with the measurement type named, receptor nomenclature that is the field's reference standard, selectivity annotations, and clinical status. Curated by expert subcommittees, not text-mined. For a KB that needs authoritative target assignments, this is the gold standard.

**3. Identifiers carried.** GtoPdb ligand and target IDs, InChIKey, SMILES, UniProt, PubChem CID, ChEMBL ID, Ensembl, HGNC. Excellent joinability in principle.

**4. Bulk access.** CSV downloads and a REST API at `https://www.guidetopharmacology.org/services/` returning JSON, covering targets, ligands, interactions, diseases and references. A `pyGtoP` Python wrapper exists but is described on the site as "not actively maintained".

**Access change**: the download page now states, verbatim (verified live 2026-09-07 at `https://www.guidetopharmacology.org/download.jsp`):

> "The IUPHAR/BPS Guide to Pharmacology now requires all users to register and login in order to access the database. This change is necessary so that we can collect accurate user access data, which helps us maintain GtoPdb as an open-access, freely available resource. Commercial users, please read our sustainability statement for more information on commercial access fees."

A time-limited guest login is offered "for a limited time as we move to the new registration system, after which all users will be have to be registered". Confidence: high.

**5. LICENCE: `SHARE_ALIKE` — NOT SEEDABLE.**

Two statements, both verified live 2026-09-07:

From `https://www.guidetopharmacology.org/about.jsp`:

> "The Guide to PHARMACOLOGY database is licensed under the Open Data Commons Open Database License (ODbL)."

and its contents are

> "licensed under a Creative Commons Attribution-ShareAlike 4.0 International License."

The footer of every page, including the login page, repeats:

> "This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License"

Confidence: high.

ODbL and CC BY-SA 4.0 are both share-alike. Compounded by registration gating and commercial access fees, GtoPdb is firmly curate-only. Note the tension worth recording: the site describes itself as "open-access, freely available" while charging commercial access fees and applying copyleft.

**6. Data-quality traps.** Affinity values are often summary or representative values selected by curators from several publications rather than raw per-experiment measurements — good for authority, but they are not independent replicates and should not be pooled with per-experiment data from BindingDB or ChEMBL as if they were.

---

### 10. Therapeutic Target Database (TTD)

**1. What it is.** Database of known and explored therapeutic protein and nucleic acid targets with the drugs directed at them. Maintained by the Innovative Drug Research and Bioinformatics Group (IDRB), Zhejiang University College of Pharmaceutical Sciences.

- **TTD 2026** update published in *Nucleic Acids Research* (`https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkaf1154/8324952`). Reported content: 3,798 targets and 40,398 drugs; 306,247 target-disease associations covering 2,912 targets; 10,506 perturbation profiles on 2,368 targets; activity landscapes for 17,806 drugs; clinical profiles for 2,234 approved drugs. Confidence: medium — these figures come from the article abstract via search, not from a database page I could render.

**2. What it would contribute.** Target-disease associations, target development/clinical status, and drug-target pairs with therapeutic context. Useful for the "is this a validated therapeutic target" question rather than for raw measured affinity.

**3. Identifiers carried.** TTD target and drug IDs, with cross-references to UniProt, PubChem and ChEBI in the classic flat files. Confidence: medium — I could not open the current download listing to confirm the column set.

**4. Bulk access.** Historically a set of numbered flat files (`P1-01-TTD_target_download.txt` and siblings). The current site at `https://ttd.idrblab.cn/full-data-download` and the mirror at `https://db.idrblab.net/ttd/full-data-download` are **single-page JavaScript applications that render nothing without script execution**. I fetched and searched the compiled bundle (`/assets/index-B1MIElFm.js`, 1,299,857 bytes) for download filenames and found none — the file list is fetched at runtime from an API I could not locate. Legacy file paths under `sites/default/files/` return the SPA shell rather than the files. `https://idrblab.org/ttd/` renders only "Therapeutic Target Database (TTD) Is Loading...".

**Conclusion: TTD bulk downloads are effectively web-only for an automated client.** Verified live 2026-09-07. Confidence: high.

**5. LICENCE: `UNVERIFIED` — NOT SEEDABLE.**

I searched the rendered pages and the full JavaScript bundle for licence, copyright, Creative Commons and terms-of-use strings. The only licence strings in the bundle belong to bundled libraries (Font Awesome, MIT-licensed code) — **there is no data licence or terms-of-use statement for TTD's contents**. Secondary sources describe TTD as "freely accessible without login", which is an access statement, not a licence.

Confidence: high that no licence is stated on the site. Absence of a statement is UNVERIFIED, not permission.

**6. Data-quality traps.** Target-disease associations are aggregated from heterogeneous evidence without a uniform evidence code. "Explored" targets sit alongside clinically validated ones. Drug-target pairs frequently carry no affinity value.

---

### 11. Open Targets Platform

**1. What it is.** Target-disease association platform, a public-private partnership including EMBL-EBI, Wellcome Sanger, GSK and others.

- Latest release: **26.06, posted 2026-06-25** (FTP directory `26.06/` and `latest/` both dated 2026-06-25). Verified live 2026-09-07 at `https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/`. Confidence: high.
- Release cadence is quarterly (25.03, 25.06, 25.09, 25.12, 26.03, 26.06).

**2. What it would contribute.** Drug mechanism of action, drug clinical phase, target-disease associations with evidence scores and per-datasource provenance, and target annotations. The molecule/mechanism-of-action datasets are the relevant part for this KB. Evidence is aggregated from named sources with explicit scoring, so the curated-versus-inferred distinction is machine-readable — a genuine advantage.

**3. Identifiers carried.** Ensembl gene IDs and UniProt for targets, EFO/MONDO for diseases, ChEMBL IDs for drugs, InChIKey via the ChEMBL molecule records. Structure-keyed joining works through the ChEMBL molecule layer.

**4. Bulk access.** FTP at `https://ftp.ebi.ac.uk/pub/databases/opentargets/platform/latest/`, plus Google Cloud and a GraphQL API. Parquet and JSON. Versioned `YY.MM` with a stable `latest/` symlink. Releases back to 16.04 are retained.

**5. LICENCE: `CC0_OK` for the platform output — SEEDABLE, with an important per-source caveat.**

Verbatim from `https://platform-docs.opentargets.org/licence` (verified live 2026-09-07):

> "Open Targets Platform is marked with CC0 1.0. This dedicates the data to the public domain, allowing downstream users to consume the data without restriction."

and for code:

> "The codebases that power the Platform - including our pipelines, GraphQL API, and React UI - are all open source and licensed under the APACHE LICENSE, VERSION 2.0."

Confidence: high.

**The caveat is material.** The same page enumerates per-datasource licences across 50+ integrated sources. Most are CC BY 4.0 or CC0 1.0, but the exceptions include:

- **ChEMBL and Human Protein Atlas: CC BY-SA 3.0**
- EFO, Gene Signature, PROGENy, UKB-PPP: Apache 2.0
- SLAPenrich: MIT terms of use
- Cancer Gene Census, Genomics England PanelApp, Project Score: "Commercial use for Open Targets"
- EMBL-EBI sources (ClinVar, Gene2Phenotype, IntAct, Signor, GWAS Catalog): EMBL-EBI terms of use

So Open Targets asserts CC0 over its platform as a whole while acknowledging that some upstream inputs are share-alike or restricted. **A KB seeding from Open Targets should take the CC0 dedication at face value for Open Targets' own derived output, but should not use Open Targets as a laundering route for ChEMBL content** — the drug and mechanism-of-action datasets are substantially ChEMBL-derived, and copying ChEMBL bioactivity records via Open Targets does not escape CC BY-SA 3.0. Use Open Targets for its own association scores and evidence aggregation; go to the primary literature for ChEMBL-origin measurements. Confidence: high on the licence text, medium on the legal analysis of the derivation question, which merits a second opinion.

**6. Data-quality traps.** Association scores are computed, not measured, and must never be presented as bioactivity. Text-mined evidence (Europe PMC-derived) sits alongside experimental evidence in the same association object and is distinguished only by the datasource field. Target-disease associations are gene-level, not compound-level.

---

### 12. IMPPAT 2.0

**1. What it is.** Indian Medicinal Plants, Phytochemistry And Therapeutics — a manually curated database built by digitalising more than 100 books on traditional Indian medicine plus 7,000+ research articles. Developed at The Institute of Mathematical Sciences (IMSc), Chennai, in Areejit Samal's group.

- Version **2.0, released 2022-06-17**; version 1.0 was 2018-01-25. Content: **4,010 Indian medicinal plants, 17,967 phytochemicals, 1,095 therapeutic uses**. Verified live 2026-09-07 at `https://cb.imsc.res.in/imppat/home`. Confidence: high.

**2. What it would contribute.** Three association types, all at the level of plant *part*: plant-part-phytochemical, plant-part-therapeutic use, and plant-part-traditional formulation. This is ethnopharmacology and phytochemical occurrence, **not measured bioactivity** — there are no IC50s, no molecular targets, no assay context.

**3. Identifiers carried.** IMPPAT phytochemical identifiers with 2D and 3D structures; the site states structures are provided for all 17,967 phytochemicals. InChIKey and SMILES are provided per compound on the compound pages. Confidence: medium — I confirmed structures exist but could not download the bulk file to verify column names, because the download page is broken (below).

**4. Bulk access. Broken as of today.** The site's own navigation links to `/imppat/download`, and I also tried `/imppat/downloads` and `/imppat/download-home`. **All return HTTP 404** with the site's error page. Verified live 2026-09-07. Confidence: high. The associated code repository is at `https://github.com/asamallab/IMPPAT2`, but that hosts analysis code, not the database.

**5. LICENCE: `NON_COMMERCIAL` — NOT SEEDABLE.**

The footer of every IMPPAT page, including the 404 page, states verbatim (verified live 2026-09-07):

> "This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License."

The same footer carries a disclaimer:

> "The main goal of this database is to compile information from scientific literature on Indian medicinal plants to aid ongoing research efforts. The compiled data should be used only for research purposes and should not be used for any self diagnosis or medical treatment."

Confidence: high.

CC BY-NC 4.0 is incompatible with CC BY 4.0. Some secondary descriptions additionally claim the licence "does not permit creation of adaptations or other derivative works", which would be more restrictive than standard CC BY-NC; I did not find that restriction on the site itself and do not rely on it. Either way: not seedable.

**6. Data-quality traps.** Therapeutic uses are traditional indications attributed to a plant part, not to a compound. Any pipeline that propagates a plant's traditional indication onto each of its constituent phytochemicals manufactures false compound-level claims at scale — this is the canonical herb-level-indication trap, and IMPPAT's plant-part granularity makes it tempting precisely because it looks more specific than it is.

---

### 13. TCM databases: TCMSP, HERB, SymMap

These three share a pattern: substantial curated content, no usable licence, and infrastructure that is partly broken.

#### 13a. TCMSP

**1. What it is.** Traditional Chinese Medicine Systems Pharmacology Database and Analysis Platform, from the Lab of Systems Pharmacology (Northwest A&F University). Captures herb-compound-target-disease relationships with computed ADME properties (oral bioavailability, drug-likeness, Caco-2 permeability, blood-brain barrier, aqueous solubility).

- **Version 2.3.** Verified live 2026-09-07 at `https://www.tcmsp-e.com/tcmsp.php`. Confidence: high.

**2. What it would contribute.** Herb-ingredient-target-disease links plus predicted pharmacokinetic parameters. **The ADME values are computed, not measured** — this is the resource's defining characteristic and its defining risk.

**3. Identifiers carried.** The search interface accepts InChIKey and CAS alongside herb, chemical, target and disease names, so InChIKey is present in the underlying data. Confidence: medium.

**4. Bulk access. Degraded.** A "Download" item appears in the menu markup but is commented out in the HTML I retrieved. `https://tcmsp-e.com/tcmspsearch.php` returns **"Error querying database.."** — the search backend is failing as of today. The legacy host `old.tcmsp-e.com` does not resolve to a reachable server (connection refused on port 443). Verified live 2026-09-07. Confidence: high.

**5. LICENCE: `RESTRICTED` — NOT SEEDABLE.**

Site footer, verbatim (verified live 2026-09-07):

> "Copyright © 2012 - 2023 Lab of Systems Pharmacology. All Rights Reserved."

No Creative Commons licence anywhere. "All Rights Reserved" is an express reservation. Confidence: high.

The site additionally promotes paid training courses, a commercial storefront ("TCMSP大健康商城"), paid technical support, and recruitment of commercial promotion partners — the operation is monetised, which makes an open re-licence unlikely.

**6. Data-quality traps.** The computed oral-bioavailability and drug-likeness thresholds (OB ≥ 30%, DL ≥ 0.18) that the TCM network-pharmacology literature applies almost universally are prediction cutoffs, not measurements, and compounds are routinely filtered in or out of published analyses on that basis. Targets are largely inferred by similarity-based prediction. Presenting any TCMSP target as measured would be a serious error.

#### 13b. HERB

**1. What it is.** High-throughput experiment- and reference-guided database of traditional Chinese medicine. **HERB 2.0** was published in *Nucleic Acids Research* 53(D1):D1404-D1414 on 2025-01-06 (doi:10.1093/nar/gkae1037), by Gao, Liu, Lei and colleagues.

- HERB 2.0 content per the paper: 8,558 clinical trials and 8,032 meta-analyses curated, with clear clinical conclusions extracted for 1,941 trials and 593 meta-analyses; 2,231 high-throughput experiments with 6,644 curated references; 376 new diseases. Confidence: medium — from the article, not from a database page.

**2. What it would contribute.** Clinical-trial and meta-analysis evidence for TCM, plus experiment-derived herb-gene relationships. The clinical-evidence layer is genuinely distinctive; nothing else in this cluster carries curated meta-analysis conclusions.

**3. Identifiers carried.** Not verified.

**4. Bulk access. Not determinable.** `http://herb.ac.cn/` and `http://herb.ac.cn/v2/` return HTTP 200 but the rendered text is literally just "HERB" / "HERB 2.0" — the site is an Umi/React single-page application (`/static/umi.js`) that renders nothing without JavaScript. `http://herb.ac.cn/Download` behaves identically. An earlier HTTPS attempt to `herb.ac.cn` was refused at the connection level (ECONNREFUSED on 47.92.70.12:443); only plain HTTP responds. Verified live 2026-09-07. Confidence: high.

**5. LICENCE: `UNVERIFIED` — NOT SEEDABLE.** No terms page was reachable. Confidence: high that I could not verify; no claim either way about what the terms are.

**6. Data-quality traps.** Clinical conclusions are extracted from trials of *herbs and formulations*, not of single compounds. Attributing a formulation's clinical result to a constituent structure is unsupportable.

#### 13c. SymMap

**1. What it is.** Integrative TCM database linking herbs to symptoms and to modern medicine through both molecular mechanism and symptom mapping. From Beijing University of Chinese Medicine, the Institute of Computing Technology (Chinese Academy of Sciences), and Beijing Jiaotong University.

- **Version 2.0.** Verified live 2026-09-07 at `http://www.symmap.org/`. Confidence: high.
- Component counts, verbatim from the download page:

| Component | Count | Stated source |
|---|---|---|
| Herb | 698 | Chinese Pharmacopoeia (2015, 2020), Chinese Materia Medica Dictionary (2006), Chinese Materia Medica (1999), National Compilation of Chinese Herbal Medicine (1996) |
| TCM symptom | 2,285 | Chinese Pharmacopoeia (2015, 2020) |
| MM symptom | 1,148 | Manual curation to UMLS, MeSH, CSSO, Symptom Ontology |
| Ingredient | 26,035 | Integration of TCMID, TCMSP, TCM-ID, HIT, HERB, DCABM-TCM |
| Target | 20,965 | Integration of HIT, TCMSP, HPO, DrugBank, NCBI, HERB |
| Disease | 14,086 | Integration of OMIM, MeSH, Orphanet, MalaCards, UMLS |
| Syndrome | 233 | Chinese Pharmacopoeia (2015, 2020) |

**2. What it would contribute.** Herb-symptom-ingredient-target-disease mappings, with medical experts having manually extracted and proofread herbs, symptoms and syndromes against the Chinese Pharmacopoeia. Ingredients are annotated into four categories (QC ingredients, blood ingredients, metabolic ingredients, other) using mass-spectrometry data from the 2020 Pharmacopoeia — that MS-grounded categorisation is a real contribution.

**3. Identifiers carried.** SymMap IDs (SMHB/SMTS/SMMS/SMIT/SMTT/SMDE/SMSY prefixes) as the primary keys. Cross-references exist to the integrated sources. Structure identifiers not verified.

**4. Bulk access.** Working, unlike its siblings. Per-component description files and search-key files downloadable from `http://www.symmap.org/download/`, sizes 31 KB to 3.6 MB. Version 1.0 datasets remain available alongside 2.0. Verified live 2026-09-07.

**5. LICENCE: `UNVERIFIED` — NOT SEEDABLE.**

The only ownership statement on the site is a bare copyright line, verbatim:

> "Copyright © 2022, Beijing University of Chinese Medicine; Institute of Computing Technology, Chinese Academy of Sciences; Beijing Jiaotong University, China"

No licence, no terms of use, no Creative Commons mark. Confidence: high.

**6. Data-quality traps.** The ingredient and target layers are **integrated from TCMSP, HIT, HERB, TCMID and DrugBank** — so SymMap inherits TCMSP's predicted targets and DrugBank's NC licence encumbrance simultaneously. Its targets are an aggregation of other databases' assertions, largely without independent measurement. Symptom-to-ingredient relationships are herb-mediated inferences, which is exactly the herb-level-indication trap in a new shape.

---

### 14. NAPRALERT

**1. What it is.** NAtural PRoducts ALERT — the historically most comprehensive natural-products literature database, covering ethnomedical, pharmacological and biochemical information on extracts and on metabolites from natural sources, spanning in vitro, in situ, in vivo, human case reports and clinical studies. Created at the University of Illinois Chicago in 1975 by the late Prof. Norman R. Farnsworth; maintained by the UIC Pharmacognosy Institute.

- Scale, verbatim from `https://pharmacognosy.pharmacy.uic.edu/napralert/` (verified live 2026-09-07):

  > "Data from more than 200,000 sceintific papers and reviews are included in NAPRALERT with about 25% of the database derived from abstracts and 75% from original articles. Organisms from all countries of the world are represented, including marine and microorganisms. [...] The earliest papers date to the late 1800's."

  and, on ethnomedicine:

  > "Ethnomedical information on more than 20,000 species of plants"

**2. Currency — a serious limitation stated by the maintainers themselves**, verbatim:

> "We believe that our coverage of the literature is comprehensive from at least 1975 through 2004. Due to budgetary constraints, we estimate the database to currently include only about 20% of the global natural-products literature from 2005 to the present"

**3. Availability. Currently offline.** The page carries the heading, verbatim:

> "NAPRALERT ONLINE [Status Update: Currently Unavailable]"

Verified live 2026-09-07. Confidence: high.

**4. Bulk access.** None. Historically a query service, plus availability through STN (CAS). No bulk download has ever been offered.

**5. LICENCE: `RESTRICTED` — NOT SEEDABLE.**

NAPRALERT® is a registered trademark. The site describes, verbatim:

> "NAPRALERT thrives to offer limited free searches of the database, as well as advancing several levels of fee-based services to the natural product community"

Access is fee-based by citation count, with free service to scientists in developing countries under a WHO arrangement. Distribution through STN is governed by CAS Information Use Policies. There is no open licence and no redistribution grant. Confidence: high.

**6. Data-quality traps.** This is the archetypal source of the extract-attribution problem: NAPRALERT records pharmacology of *extracts of organisms* alongside pharmacology of *metabolites from natural sources*, in the same database. The site's own caution notes that pharmacological activity categories are inconsistently granular ("there are many closely-related targets that might relate to a single endpoint"). Combined with the 2005-onward coverage gap, any figure derived from NAPRALERT is a lower bound of unknown tightness.

---

### 15. FooDB

**1. What it is.** Food constituent database from the Wishart group (University of Alberta) / The Metabolomics Innovation Centre, describing itself as "the world's largest and most comprehensive resource on food constituents, chemistry, and biology".

- Version **1.0, still labelled "Pre-release 1.0"**. Verified live 2026-09-07 at `https://foodb.ca/downloads` and `https://foodb.ca/about`. Confidence: high.

**2. What it would contribute.** Food-compound occurrence, concentrations in foods, chemical classes, and narrative "presumptive health effects (from published studies)". Each chemical entry has more than 100 data fields. It is an occurrence and composition resource with descriptive biology, **not a measured-bioactivity resource** — there are no potencies, targets, or assay records.

**3. Identifiers carried.** The about page states FooDB links "food compound data to other relevant databases such as HMDB, PubChem, CHEBI, KEGG, and NCBI_Taxonomy". InChIKey and SMILES are present on compound records per the Wishart-suite convention. Confidence: medium.

**4. Bulk access. Stale.** From `https://foodb.ca/downloads`:

| File | Date added | Size |
|---|---|---|
| FooDB CSV | 2020-04-07 | 952.52 MB |
| FooDB XML | 2020-04-07 | 6438.08 MB |
| FooDB JSON | 2020-04-07 | 86.66 MB |
| FooDB MySQL dump | 2020-04-07 | 172.73 MB |

Spectra and peak-list downloads are dated 2022-10-13. **The core data has not been refreshed since April 2020.** Verified live 2026-09-07.

Host stability is poor: `https://foodb.ca/` returned **HTTP 525** (Cloudflare SSL handshake failure) on my first attempt and HTTP 200 minutes later. Intermittent.

**5. LICENCE: `NON_COMMERCIAL` — NOT SEEDABLE.**

Footer of every page, verbatim (verified live 2026-09-07):

> "This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License."

The downloads page adds:

> "Please read our terms surrounding use and distribution of the FooDB database."

and the about page notes that commercial use requires explicit permission and that users downloading significant portions must cite the FooDB paper. Confidence: high.

**6. Data-quality traps.** "Presumptive health effects" is explicitly presumptive and must never be recorded as a bioactivity claim. Concentration values are food-matrix composition, not dose. Many compound entries are predicted constituents rather than experimentally detected ones.

---

### 16. Phenol-Explorer

**1. What it is.** Database of polyphenol content in foods — reported as the first comprehensive such resource, with more than 35,000 content values for 500 polyphenols in over 400 foods. Hosted on Wishart-lab infrastructure.

- **Version 3.6.** Verified live 2026-09-07 at `http://phenol-explorer.eu/downloads`. Confidence: high.
- Release 3.0 added data on the effects of food processing and cooking.

**2. Hosting is currently misconfigured.** `https://phenol-explorer.eu/` and `http://phenol-explorer.eu/` serve **the Livestock Metabolome Database (LMDB)** rather than Phenol-Explorer. The TLS certificate presented for `phenol-explorer.eu` has altnames `*.lmdb.ca, *.wishartlab.com, lmdb.ca, wishartlab.com` — it does not cover the Phenol-Explorer domain at all, so HTTPS fails certificate validation outright. Deeper paths such as `/downloads` and `/contents` *do* serve Phenol-Explorer correctly. This is a virtual-host misconfiguration on a shared Wishart server, not a shutdown. Verified live 2026-09-07. Confidence: high.

**3. What it would contribute.** Polyphenol composition of foods with analytical method. Composition data, **not bioactivity** — no targets, no potencies.

**4. Bulk access. Substantially broken for v3.6.** The downloads page lists the v3.6 table with "Not Available" in the Released-on and Download columns for nearly every dataset: complete composition data, polyphenol metabolites, polyphenol classification, food classification, source publications, and both structure files (`/compounds/structures.csv`, `/metabolites/structures.csv`) all show "Not Available". Only "Polyphenols having composition data" and "Foods having composition data", both dated 2009-01-10, offer a CSV. The v2.0 table (dated 2012-05-10) has working Excel and CSV links. Verified live 2026-09-07. Confidence: high.

**5. LICENCE: `NON_COMMERCIAL` — NOT SEEDABLE.**

Verbatim from `http://phenol-explorer.eu/downloads` (verified live 2026-09-07):

> "Phenol-Explorer is offered to the public as a freely available resource. Use and re-distribution of the data, in whole or in part, for commercial purposes requires explicit permission of the authors and explicit acknowledgment of the source material (Phenol-Explorer) and the original publications (see how to cite us)."

> "Important: We ask that users who download significant portions of the database cite the Phenol-Explorer paper in any resulting publications."

Confidence: high.

This is a bespoke non-commercial restriction rather than a named Creative Commons licence. "Freely available" in the first clause is qualified by the commercial-permission requirement in the second. A CC BY 4.0 release permits commercial use, so Phenol-Explorer content cannot be seeded.

**6. Data-quality traps.** Content values are food-matrix concentrations aggregated across analytical methods with different recoveries; the Folin method for "total polyphenols" is a non-specific colorimetric assay that is not comparable with chromatographic per-compound values. Retention factors for processing are derived, not measured per food.

---

### 17. Dr. Duke's Phytochemical and Ethnobotanical Databases

**1. What it is.** The USDA's ethnobotanical and phytochemical database, developed by James A. Duke, maintained by the U.S. Department of Agriculture, Agricultural Research Service. Reports species, phytochemicals, biological activities, and ethnobotanical uses.

- Development period **1992-2016**; the primary reference is Duke's 1992 *Handbook of phytochemical constituents of GRAS herbs and other economic plants*. Verified live 2026-09-07 at `https://phytochem.nal.usda.gov/about`. Confidence: high. The resource is effectively frozen — no new curation since 2016.

**2. What it would contribute.** Plant-chemical occurrence, chemical-biological activity assertions, and ethnobotanical uses. The activity assertions are literature-derived qualitative activity labels (e.g. "antibacterial", "antioxidant") attached to compounds, sometimes with a quantitative value and a reference. **This is not assay-context bioactivity** — there is generally no cell line, no measurement type, and no unit discipline.

Its real value to a CC BY 4.0 KB is that it is the only ethnobotanical resource in this cluster that is actually seedable.

**3. Identifiers carried.** Chemical names and plant taxa as the primary keys. Structure identifiers are weak — the historic tables are name-based, so resolving Dr. Duke's chemicals to Standard InChIKeys requires an external name-to-structure resolution step with real error rates. Confidence: medium-high. This is the main obstacle to using it in a structure-keyed corpus.

**4. Bulk access.** Interactive web version at `https://phytochem.nal.usda.gov/`. Raw database tables are archived for download through USDA Ag Data Commons (`https://agdatacommons.nal.usda.gov/articles/dataset/Dr_Duke_s_Phytochemical_and_Ethnobotanical_Databases/24660351`) and listed on data.gov, distributed as `Duke-Source-CSV.zip`. The Ag Data Commons deposit is versioned and DOI-bearing. Per-query exports to PDF or spreadsheet are available from the web interface.

**5. LICENCE: `CC0_OK` — SEEDABLE.**

Verbatim from `https://phytochem.nal.usda.gov/about` (verified live 2026-09-07):

> "Contents of this database are made available under a Creative Commons CC0 public domain dedication."

Confidence: high. This is an explicit CC0 dedication on the database's own about page — not a policy inference, not an article licence. It is the cleanest licence in the entire cluster.

**6. Data-quality traps.** This resource carries the heaviest concentration of the traps named in my brief:

- Activity labels are frequently **attributed to a plant** and then associated with its constituent chemicals, which is the herb-level-indication trap by construction.
- Many activity entries have **no units, no assay, and no dose**; where a quantitative value exists its basis is often unstated.
- Values are aggregated from heterogeneous 20th-century literature of highly variable rigour, including secondary compilations.
- Chemical naming is historic and non-standard; synonym collisions are common, and name-to-structure resolution will silently mis-assign some records.
- Content is frozen at 2016 and reflects the state of knowledge and nomenclature of that era.

**Recommendation**: seed Dr. Duke's only as *ethnobotanical and occurrence* assertions with explicit low-evidence provenance, never as measured bioactivity, and gate every record on successful, checked name-to-InChIKey resolution.

---

## Refuted or unverifiable claims

1. **"ChEMBL is CC BY."** Refuted. ChEMBL is **CC BY-SA 3.0 Unported**, confirmed from the licence file shipped in the FTP release tree itself. This is the single most consequential finding for the KB's seeding plan, because ChEMBL is the default assumption for bioactivity data.

2. **"ChEMBL's `natural_product` flag identifies natural products."** Refuted by counterexample. `CHEMBL2` is prazosin — a synthetic quinazoline α1-antagonist first approved in 1976 — and carries `natural_product=1` in ChEMBL 37 while its own `np_likeness_score` is -1.29. The flag cannot be used as an NP definition without independent structural verification. Verified by direct API call 2026-09-07.

3. **"CO-ADD is open access, so its data is reusable."** Refuted. The database is branded "Open-access Antimicrobial Screening Database", but the only terms on the site reserve all rights, permit copying for "personal, non-commercial purposes" only, and state that "Content may not be systematically downloaded, retrieved or stored" and "may not be reproduced or transmitted without our prior written permission."

4. **"NPASS is open."** Unverifiable. The NPASS privacy policy calls the project "an open-access resource for biomedical research", but no licence, terms-of-use, or copyright grant exists on the front page, the download page, or the privacy policy. `about.html` returns 404. Prose describing a project as open-access is not a licence grant.

5. **"TTD is freely accessible, therefore reusable."** Unverifiable as a licence claim. Free access without login is documented; a redistribution licence is not. I searched both the rendered pages and the full 1.3 MB JavaScript bundle and found no data licence — the only licence strings present belong to bundled front-end libraries.

6. **"BindingDB's 1.6 million curated data points are available under CC BY 3.0 in one download."** Not established, and probably false as stated. The CC BY 3.0 statement covers "all data curated by BindingDB staff", but the packaged articles download contains only **93,712 rows**. The remainder of the curated corpus is distributed across the patents and other files, whose licence status the Info page does not separately address. Only the articles subset is confirmed as a cleanly packaged CC BY 3.0 extract, and even it contains 429 ChEMBL-sourced rows that must be filtered out by `Curation/DataSource`.

7. **"Phenol-Explorer is offline."** Refuted, with a correction. The apex domain serves the wrong application (the Livestock Metabolome Database) and its TLS certificate does not cover the Phenol-Explorer hostname, so a naive HTTPS fetch fails. But deeper paths under plain HTTP serve Phenol-Explorer v3.6 correctly. The resource exists; its hosting is misconfigured and its v3.6 downloads are mostly marked "Not Available".

8. **"NAPRALERT is available."** Refuted for the present moment. Its own page states "NAPRALERT ONLINE [Status Update: Currently Unavailable]". Separately, the maintainers state coverage since 2005 is only about 20% of the natural-products literature.

9. **"DrugCentral and FooDB are current."** Refuted. DrugCentral's downloadable database dump is dated 2023-11-01 and the site still styles itself "DrugCentral 2023". FooDB's core data files are dated 2020-04-07 and it remains labelled "Pre-release 1.0".

10. **"GtoPdb is freely downloadable."** Refuted as of today. Downloads and statistics now sit behind mandatory registration, with a guest login offered only "for a limited time", and commercial users are directed to access fees. The data licence is separately copyleft (ODbL and CC BY-SA 4.0).

11. **Claims I could not verify at all**: HERB's licence and download contents (JavaScript-only site, HTTPS refused); TTD's current download file list and column set (JavaScript-only site); GtoPdb's current ligand/target/interaction counts (login-gated); CO-ADD's total compound count (not published on any reachable page); IMPPAT's bulk file structure (download page returns 404 at all three URLs the site itself advertises).

---

## Open questions

1. **Can BindingDB's non-article curated data be licensed as CC BY 3.0?** The gap between 93,712 packaged rows and the advertised 1.6M curated data points is the largest single lever available. BindingDB curates patents directly, and if that curation carries the same CC BY 3.0 grant it would multiply the seedable measured-affinity corpus by more than an order of magnitude. This needs a direct question to the BindingDB team, and it is the highest-value clarification in this cluster.

2. **Will NPASS apply an explicit licence?** NPASS is InChIKey-keyed, has a million activity records with assay organism, tissue, cell type and PMID, and covers antimicrobial MICs better than any other resource here. It is the best structural fit to this KB and is blocked solely by the absence of a licence statement. A request to Hanbo Lin (hanbolin@u.nus.edu) and Prof. Zeng Xian (zengxian@fudan.edu.cn) asking for CC BY 4.0 is worth making early, since a positive answer would reshape the seeding plan.

3. **Will CO-ADD grant CC BY 4.0 over its screening data?** A Wellcome-funded open-science initiative whose terms page is 2016 university boilerplate contradicting its own stated mission is a strong candidate for a successful re-licence request (`info@co-add.org`). Even a grant limited to the dose-response MIC data would be valuable.

4. **How far does the Open Targets CC0 dedication actually reach over ChEMBL-derived content?** Open Targets marks its platform output CC0 while acknowledging ChEMBL inputs are CC BY-SA 3.0. Whether copying Open Targets' drug and mechanism-of-action records into a CC BY 4.0 corpus is legitimate, or whether it constitutes redistribution of ChEMBL under a licence ChEMBL did not grant, is a question I can frame but not settle. It should get a legal read before any ChEMBL-derived Open Targets field is seeded.

5. **Is NCI DTP data formally public domain?** The federal-work inference is strong but NCI never says "public domain" about database records, and its stated policy addresses text and graphics in NCI products. A confirmatory email to DTP asking for an explicit statement (or a CC0 mark) would convert a medium-confidence inference into a high-confidence one, and would unlock the July 2026 NCI-60 release.

6. **What fraction of Dr. Duke's chemical names resolve cleanly to Standard InChIKeys?** It is the cluster's only CC0 ethnobotanical source, so its value depends entirely on name-to-structure resolution yield and error rate. This needs an empirical test against the Ag Data Commons CSV before any seeding decision, not an assumption.

7. **Are HERB and TTD reachable with a JavaScript-capable client, and do they state terms there?** Both are single-page applications that revealed nothing to an HTTP client. A browser-based check would settle whether a licence exists behind the render, and would recover TTD's download manifest. Worth one short session.

8. **How should extract-derived and mixture-derived activity be represented at all?** Every ethnopharmacology source in this cluster (NAPRALERT, IMPPAT, Dr. Duke's, HERB, SymMap, TCMSP) and two of the screening sources (NCI DTP explicitly, PubChem implicitly) carry activity measured on extracts, fractions, formulations or plant parts. The KB is one-record-per-structure. A deliberate schema decision is needed — most likely an evidence class that records extract-level observations as *context for* a structure without asserting they are *properties of* it. Deferring this decision guarantees the trap gets encoded in the data.

9. **Which ChEMBL-deposited screening sets have independently open upstream licences?** ChEMBL's CC BY-SA 3.0 blankets its whole distribution, but several depositions (MMV Malaria Box and Pathogen Box, DNDi, Open Source Malaria, Gates Foundation Compound Collection) originate from organisations with open-data commitments of their own. Obtaining those datasets from the depositor rather than from ChEMBL could bypass the share-alike encumbrance entirely. Worth checking depositor by depositor for the NP-relevant sets.
