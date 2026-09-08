# Biosynthesis, BGC, classification and spectral resources for a structure-keyed Natural Products KB

Research date: **2026-09-07**. All "verified live" claims were checked against the primary site,
API, FTP file or PMC full text on that date. Where a site is a JavaScript single-page app, the
raw HTML returned only a title; in those cases the underlying JSON API or the compiled JS bundle
was fetched instead, and this is stated explicitly.

Licence classes used: **CC0_OK** (public domain / CC0), **ATTRIBUTION** (CC BY, seedable),
**SHARE_ALIKE**, **NON_COMMERCIAL**, **RESTRICTED** (subscription / bespoke terms),
**UNVERIFIED** (no licence statement found on the primary pages).

---

## Summary

**Seedable into a CC BY 4.0 KB (licence verified verbatim):**

| Resource | Licence | Verified at |
|---|---|---|
| MIBiG 4.0 | CC BY 4.0 | site footer + paper Data availability |
| BiG-FAM | CC BY 4.0 | `rel="license"` on bigfam.bioinformatics.nl |
| Paired Omics Data Platform | CC BY 4.0 | app bundle + submission terms |
| GNPS libraries (native contributions) | CC0 | GNPS documentation |
| MoNA | CC BY 4.0 by default | MoNA app bundle licence page |
| MassBank EU | CC BY (per-record `LICENSE` tag) | live API record + record-format spec |
| NPClassifier ontology/models/data | CC0 (code MIT) | repo README + LICENSE |
| Rhea | CC BY 4.0 | `ftp.expasy.org/databases/rhea/LICENSE.txt` |

**Not seedable:**

| Resource | Licence | Why |
|---|---|---|
| Norine | CC BY-NC-SA 4.0 | NonCommercial + ShareAlike |
| NP-MRD | CC BY-NC 4.0 | NonCommercial |
| ClassyFire / ChemOnt | bespoke, commercial re-distribution needs permission | RESTRICTED |
| MetaCyc / BioCyc | paid subscription "at least $5,000" | RESTRICTED |
| KEGG | "KEGG is not a public database"; commercial licence required | RESTRICTED |
| antiSMASH database dumps | no data licence found on primary pages | UNVERIFIED (code is AGPL-3.0) |

**The single highest-value source for this KB is MIBiG 4.0**: it is the only resource that carries
an expert-curated compound→BGC→producer-organism triple with an explicit experimental-evidence
qualifier, under CC BY 4.0, in a small bulk JSON download. Its main gap for a structure-keyed KB is
that **it stores SMILES, never InChIKey** — standard InChIKeys must be generated locally — and
**1042 of 5443 compound records have no structure at all**.

**The main quantitative traps** are: MIBiG's `quality` field is `questionable` for 2710 of 3013
entries (legacy-format entries, not a claim of falsity); antiSMASH-DB's ~479k regions are
*algorithmic predictions with no compound assignment*; and BiG-FAM is frozen on 2020 data and
MIBiG 2.0.

---

## Per-source findings

### 1. MIBiG 4.0 — Minimum Information about a Biosynthetic Gene cluster

**1. What it is.** Curated repository and data standard for biosynthetic gene clusters, maintained
by the Medema group (Wageningen), Weber group (DTU Biosustain) and a large community of
contributors. Latest release **4.0**, published **2024-11-15** (dump timestamp), paper published
2025-01-06 (Zdouc, Blin et al., *Nucleic Acids Res* 53:D678–D690, doi:10.1093/nar/gkae1115).

Size, from the live API (`https://mibig.secondarymetabolites.org/api/v1/stats`, verified live
2026-09-07):

| Counter | Value |
|---|---|
| total entries | 3015 |
| active | 2439 |
| retired | 377 |
| pending | 199 |
| complete | 810 |
| partial | 72 |

Class counts, same endpoint: PKS 1239, NRPS 1020, Ribosomal 447, Other 421, Terpene 241,
Saccharide 216. Top phyla: Actinomycetota 1226, Ascomycota 576, Pseudomonadota 507.

The paper states 3059 entries: "267 contributors performed 8304 edits, creating 557 new entries and
modifying 590 existing entries, resulting in a new total of 3059 curated entries in MIBiG"
(verified live 2026-09-07 at https://pmc.ncbi.nlm.nih.gov/articles/PMC11701617/). The 4.0 JSON
tarball I downloaded and unpacked contains **3013 files**. The three numbers (3059 paper / 3015 live
API / 3013 in the 4.0 dump) differ; the site is now running a `4.0alpha1` build
(`/api/v1/version` → `{"api":"4.0alpha1","build_time":"Mon, 13 Apr 2026 ..."}`), so the live
database has drifted past the 4.0 release. Confidence: **high** (all three counts read directly).

**2. Contribution to a structure-keyed NP KB.** This is the anchor resource for
compound→BGC→producer. From my own parse of all 3013 files in `mibig_json_4.0.tar.gz`
(verified live 2026-09-07):

- **compound→producer organism with NCBI taxid**: `taxonomy` is present in **3013/3013** entries
  and **every one carries `ncbiTaxId`** (e.g. `{"name":"Verrucosispora maris AB-18-032","ncbiTaxId":263358}`).
- **compound→BGC locus**: `loci[].accession` is a GenBank/RefSeq accession (e.g. `JF752342.1`) with
  `location.from/to`, plus an `evidence[].method` controlled vocabulary. Observed evidence counts
  across all entries: Heterologous expression 638, Knock-out studies 542, Enzymatic assays 284,
  Gene expression correlated with compound production 219, Correlation of genomic and metabolomic
  data 82, **Homology-based prediction 31**, In vitro expression 25, syn-BNP 1.
- **biosynthetic class**: `biosynthesis.classes[].class` + `.subclass`. Most common
  class/subclass pairs: NRPS/Type I 995, PKS/Unknown 818, ribosomal/RiPP 412, other/other 377,
  PKS/Type I 226, terpene/Unknown 168, saccharide/(none) 164.
- **enzyme-level steps**: `biosynthesis.modules[]` gives per-module domains (KS, AT, carrier, KR,
  DH…) each attributed to a **protein accession** (e.g. `AEK75502.1`). There is no UniProt, EC or
  Rhea identifier in the record — joining to UniProt requires mapping the GenBank protein accession.
- **evidence of structure**: `compounds[].evidence[].method` — NMR 1234, Mass spectrometry 550,
  MS/MS 237, Chemical derivatisation 79, X-ray crystallography 39, Total synthesis 34.
- **bioactivity**: `compounds[].bioactivities[]` — antibacterial (772 + 353 legacy), cytotoxic
  (505 + 251), antifungal (303 + 152), inhibitor (136 + 79), siderophore (70 + 71), antiviral 62.
  There is **no molecular target field** and no mechanism field.

Expert-reviewed vs auto-generated: all content is human-curated; nothing is machine-predicted.
The paper describes a new peer-review layer: "for MIBiG data where a high confidence level is
required (e.g. machine learning applications), we recommend the use of reviewed entries only (the
website facilitates filtering/sorting on this)".

**3. Identifiers carried.** `accession` (BGC number), `loci[].accession` (GenBank/RefSeq),
gene/protein accessions, `taxonomy.ncbiTaxId`, and per compound `structure` (SMILES) plus
`databaseIds`. Cross-reference prefix counts over all compounds (my parse):

| Prefix | Count |
|---|---|
| npatlas | 2167 |
| pubchem | 1614 |
| chemspider | 184 |
| chebi | 87 |
| cyanometdb | 68 |
| chembl | 56 |
| lotus | 11 |

**No InChI or InChIKey field exists anywhere in the MIBiG 4.0 JSON.** Joinability to a
structure-keyed corpus therefore runs through (a) locally generating a standard InChIKey from the
SMILES, or (b) the NP Atlas / PubChem cross-references. Coverage: 5443 compound records total,
**4401 with a SMILES**, of which 3218 also have at least one database ID; 1183 have a structure but
no database ID; **1042 have neither** (name only, often a class-level or ill-defined name).
Confidence: **high**, counted directly.

**4. Bulk access.** Index: https://dl.secondarymetabolites.org/mibig/ (verified live 2026-09-07).

| File | Size | Date |
|---|---|---|
| `mibig_json_4.0.tar.gz` | 931.9 KiB | 2024-11-15 |
| `mibig_json_4.0_all_jsons.tar.xz` | 690.0 KiB | 2026-03-24 |
| `mibig_gbk_4.0.tar.gz` | 79.8 MiB | 2024-11-15 |
| `mibig_prot_seqs_4.0.fasta` | 30.4 MiB | 2024-11-15 |
| `mibig_antismash_4.0_gbk_as8b1.tar.bz2` | 63.0 MiB | 2025-01-27 |

Versioning is by release number in the filename, plus a per-entry `changelog.releases[]` with dates
and a per-entry `version` integer. Git history at https://github.com/mibig-secmet/mibig-json.
Zenodo community DOI given in the paper: https://doi.org/10.5281/zenodo.13367755 (I could **not**
fetch Zenodo — see Refuted/unverifiable).

**5. LICENCE — ATTRIBUTION (CC BY 4.0).** Two independent verifications.

Site footer, extracted from the compiled SPA bundle
`https://mibig.secondarymetabolites.org/assets/index.019ca147.js` (verified live 2026-09-07),
verbatim: `This work is licensed under a ... Creative Commons Attribution 4.0 International
License.` with `rel="license" href="http://creativecommons.org/licenses/by/4.0/"`.

Paper Data availability (verified live 2026-09-07 at
https://pmc.ncbi.nlm.nih.gov/articles/PMC11701617/), verbatim:

> "The MIBiG repository is available at https://mibig.secondarymetabolites.org/. Files in JSON
> format following the MIBiG data standard (https://github.com/mibig-secmet/mibig-json) can be
> found on the MIBiG webpage (https://mibig.secondarymetabolites.org/download) and on the MIBiG
> Zenodo Community page (https://doi.org/10.5281/zenodo.13367755). Further materials are available
> on GitHub (https://github.com/mibig-secmet). All data are freely available with no restrictions
> for academic and commercial reuse under the OSI-approved CC BY 4.0 Open Source license
> (https://creativecommons.org/licenses/by/4.0/)."

Note: the `mibig-json` GitHub repository has **no LICENSE file** (verified: raw LICENSE → 404,
GitHub licence API → 404). The licence claim rests on the website footer and the paper, which is
adequate but worth recording.

**6. Data-quality traps.**

- **`quality` is not what it looks like.** Distribution over the 3013 files: `questionable` 2710,
  `high` 233, `low` 42, `medium` 28. The paper explains: "To summarize the data quality of an entry
  concisely, we also introduced a 'Quality' identifier, and it is possible to filter entries based
  on high, medium or questionable quality of data. Note that this label only reflects the presumed
  data quality of an MIBiG entry and does not address the quality of the underlying literature."
  Combined with "entries added in previous versions of MIBiG still follow the legacy format, and
  will be updated gradually over time", `questionable` overwhelmingly marks **legacy-format entries
  not yet re-curated**, not entries believed to be wrong. Treating it as a truth flag would discard
  90% of the database. Confidence: **high** on the counts, **medium** on the interpretation.
- **`completeness` is mostly unknown**: complete 809, partial 72, `unknown` 2132.
- **377 retired entries** are present in the dump and must be filtered on `status`.
- **Putative BGC–compound links exist**: 31 loci are supported only by `Homology-based prediction`.
  Filter on `loci[].evidence[].method` if experimental support is required.
- **Class-level / structureless compounds**: 1042 compound records have no SMILES.
- **Schema drift inside one release**: `bioactivities[].name` appears both as a bare string
  (`"antibacterial"`, 353 records) and as an object (`{"activity":"antibacterial"}`, 772 records).
  Any parser must handle both.
- **`alkaloid` is no longer a biosynthetic class** — see the vocabulary section below.
- **Reviewer identity is not exposed in the dump**: `changelog.releases[].entries[].reviewers` is
  the placeholder `AAAAAAAAAAAAAAAAAAAAAAAA` for essentially every entry; only 25 of 3013 entries
  carry any non-placeholder reviewer ID. I could not find a machine-readable "reviewed" boolean in
  the 4.0 JSON, although the paper says the website supports filtering on it. Confidence:
  **medium** — counted directly, but the website's reviewed filter may be backed by a field added
  after the 4.0 dump.

**7. Confidence.** Counts, fields and licence: high, all verified live 2026-09-07 by downloading and
parsing the actual release file. Paper figures: high. The "reviewed" flag question: open.

---

### 2. antiSMASH database (version 5, and version 4)

**1. What it is.** Precomputed antiSMASH results over dereplicated public microbial genomes,
maintained by Kai Blin, Simon Shaw and Tilmann Weber (DTU Biosustain) with Marnix Medema (WUR).

Live statistics from `https://antismash-db.secondarymetabolites.org/api/stats` (verified live
2026-09-07):

| Counter | Value |
|---|---|
| BGC regions (`num_clusters`) | 479,420 |
| genomes (`num_genomes`) | 56,054 |
| sequences (`num_sequences`) | 236,080 |
| distinct cluster types | 99 |

Version 5 paper (*Nucleic Acids Res* 54:D522, published 2025-11-18, verified live 2026-09-07 at
https://academic.oup.com/nar/article/54/D1/D522/8326462): 497,429 BGC regions from 833 archaeal,
54,800 bacterial and 421 fungal genomes, computed with **antiSMASH 8.1**, 105 supported pathway
types. Version 4 paper (*Nucleic Acids Res* 52:D586, 2024-01-05,
https://pmc.ncbi.nlm.nih.gov/articles/PMC10767862/): 231,534 regions from 592 archaeal, 35,726
bacterial and 236 fungal genomes, antiSMASH 7.1, genomes from NCBI RefSeq downloaded 4–5 April 2023.
The live counters sit slightly below the v5 paper's numbers, consistent with the paper counting a
pre-release snapshot. Confidence: **high** for the live numbers, **high** for both papers.

**2. Contribution to a structure-keyed NP KB.** Essentially **none directly** — and this is the
important point. antiSMASH-DB gives genome→BGC region→predicted BGC *type*; it does **not** give a
compound identity, a structure or an InChIKey. Its value to this KB is indirect:

- expanding a known compound's producer set, by finding regions whose KnownClusterBlast hit is the
  MIBiG entry for that compound (a similarity claim, not an identity claim);
- supplying genome accession, contig and coordinates for a producer organism;
- taxonomy (`asdb5_taxa.json.gz` in the download directory).

Everything in it is **auto-generated**; nothing is expert-reviewed.

**3. Identifiers carried.** NCBI assembly accessions (`GCF_*`), RefSeq/GenBank nucleotide
accessions, NCBI taxids, MIBiG accessions via KnownClusterBlast, and (new in v5) DSMZ and DTU
Biosustain NBC strain-collection identifiers. No InChIKey, SMILES, PubChem CID or ChEBI.
Confidence: high.

**4. Bulk access.** https://dl.secondarymetabolites.org/database/ (verified live 2026-09-07):

| Release | Files |
|---|---|
| 5.0/ (2026-01-20) | `asdb5_gbks.tar` 172.4 GiB, `asdb5_jsons.tar` 181.2 GiB, `asdb5_taxa.json.gz` 945.8 KiB, `MD5SUMS`; beta2 copies from 2025-09-16 |
| 4.0/ (2025-06-30) | `antismash_4.0b2_full.sql.xz` 29.6 GiB, `asdb-beta2-jsons.tar` 105.6 GiB |

There is also a REST API (`/api/stats`, `/api/v2.0/stats`, `/api/v1.0/version`). Versioning is by
release directory number; no DOI found.

**5. LICENCE — UNVERIFIED for the data.** I could not find any licence statement for the database
content on the site, the download index or the API. What is verified:

- Code: `https://raw.githubusercontent.com/antismash/db-schema/master/LICENSE` is the **GNU Affero
  General Public License version 3** (verified live 2026-09-07); `antismash/db-api` carries the same
  AGPL text.
- The v4 and v5 papers state, verbatim: *"There are no access restrictions for academic or
  commercial use of the web server"* and *"The source code components and SQL schema for the
  antiSMASH database are available on GitHub under an OSI-approved Open Source license."*

"No access restrictions on the web server" is a statement about *access*, not about
*redistribution*, and the AGPL covers the code, not the data. The underlying genomes are NCBI
RefSeq (US-government-produced, effectively unrestricted), and the annotations are machine-generated
derivatives. **Classify UNVERIFIED**; do not treat as CC BY without asking the authors.
Confidence: **high** that no data licence is stated; the conclusion is a licence-absence finding,
not a licence.

**6. Data-quality traps.** Every region is a **prediction**. Region "products" are rule-based type
labels (`t1pks`, `nrps`, `ripp-like`, `terpene-precursor`), not compounds; `ripp-like` alone covers
53,736 regions and is described in the API as a "Fallback rule containing known RiPP-related
profiles". A KnownClusterBlast similarity to a MIBiG BGC is not evidence the genome makes that
compound. Region boundaries are heuristic and change between antiSMASH versions, so region IDs are
not stable across releases (4.0 used antiSMASH 7.1, 5.0 uses 8.1).

**7. Confidence.** High for all figures and for the licence-absence finding.

---

### 3. BiG-FAM and BiG-SLiCE

**1. What it is.** BiG-FAM is a database of gene cluster families (GCFs) built by running BiG-SLiCE
over public BGCs; developed and maintained by Satria Kautsar with Marnix Medema (Wageningen), per
the About page (verified live 2026-09-07 at https://bigfam.bioinformatics.nl/about). Citation:
Kautsar, Blin, Shaw, Weber, Medema, *Nucleic Acids Res* 2021, doi:10.1093/nar/gkaa812.

Size (verified live 2026-09-07 at https://bigfam.bioinformatics.nl/stats): **1,225,071 BGCs** in
**29,955 GCF models**, clustered with BiG-SLiCE 1.0.0 at threshold T=900.0. Per-dataset breakdown
from `https://bigfam.bioinformatics.nl/api/stats/get_dataset_table`:

| Dataset | Genomes | BGCs |
|---|---|---|
| mibig (MIBiG 2.0 reference BGCs) | 0 | 1,910 |
| isolate_bacterial_draft | 153,564 | 959,407 |
| isolate_fungal | 5,588 | 123,939 |
| isolate_bacterial_complete | 17,021 | 101,531 |
| mag_uba | 5,799 | 16,585 |
| mag_bovine | 3,727 | 8,969 |
| mag_ocean | 2,003 | 5,347 |
| mag_humangut | 2,525 | 4,791 |
| isolate_archaeal | 913 | 2,111 |
| mag_chicken | 351 | 481 |

The dataset descriptions themselves state the source snapshots were taken in **February 2020**.

**2. Contribution.** Grouping only: it can tell you that a MIBiG BGC for compound X belongs to GCF
*n* and that *m* other genomes carry members of that family. It supplies **no compound, structure or
InChIKey**. Useful as a "how widely is this biosynthetic capability distributed" annotation, and to
propagate producer-organism hypotheses (explicitly hypotheses). Everything is auto-generated.

**3. Identifiers carried.** GCF IDs, internal BGC IDs, genome accessions, links out to antiSMASH-DB
and MIBiG accessions. No chemical identifiers.

**4. Bulk access.** No download button on the site. The Help page FAQ answer to "How do I (bulk)
download GCF data from BiG-FAM?" points to `https://bioinformatics.nl/~kauts001/ltr/bigslice/paper_data/`
— **this URL failed to fetch for me** (curl returned HTTP status 000 with 0 bytes, i.e. no response;
verified 2026-09-07). Treat bulk access as effectively unavailable pending confirmation; the
alternative is to rebuild locally from the code at https://github.com/medema-group/bigfamdb.
An API exists (`/api/stats/...`) but is not a documented bulk interface.

**5. LICENCE — ATTRIBUTION (CC BY 4.0) for the database.** Verified live 2026-09-07: the BiG-FAM
home page carries `<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">` with the
standard CC BY 4.0 badge image. The Help page states, verbatim: *"All code is freely available under
a GNU Affero General Public License v3.0."* and, for the bulk paper data, *"(data is licensed under
a Creative Commons CC-BY license)"*. BiG-SLiCE itself is AGPL-3.0 (`medema-group/bigslice`
`LICENSE.txt`, verified via the GitHub licence API). So: **data CC BY, code AGPL** — a clean split.

**6. Data-quality traps.** The whole database is frozen on **2020** genome snapshots and **MIBiG
2.0** (1,910 reference BGCs versus 3,015 today), so MIBiG accessions resolved through BiG-FAM will
be stale and some will be retired entries. GCF membership at T=900 is a single arbitrary threshold —
the Help page's own worked example shows a query BGC matching a GCF at d=1,609 whose anchor gene is
only 52.63% similar by BLASTp, i.e. GCF co-membership does not imply the same product.

**7. Confidence.** High for counts and licence (read directly from the live site and API). The bulk
download URL failure is verified; whether the host is permanently gone is **unknown**.

---

### 4. Norine — nonribosomal peptides

**1. What it is.** Database and analysis platform for nonribosomal peptides, University of Lille /
CRIStAL (Pupin, Leclère, Flissi et al.). Home page states, verbatim: *"Norine currently contains
1744 peptides."* (verified live 2026-09-07 at https://bioinfo.lifl.fr/norine/). No release version
or dated dump is published; the resource is continuously updated with a crowdsourcing route
("MyNorine"). Latest reference paper: *Nucleic Acids Res* 2019, doi:10.1093/nar/gkz1000.

**2. Contribution.** Compound→producer organism, activity, and monomeric structure for NRPs —
exactly the class where structures are hardest. The download form (`/norine/download.jsp`, verified
live) offers: Norine ID, name, general name, synonyms, **activities**, peptide category, molecular
formula, molecular weight, status; structure type, number of monomers, PDB SEQRES, linear
representation, graph representation; **organism name, taxonomy, Gram, synonyms, taxid**; and
bibliographic references with **PMIDs**. So it does carry NCBI taxids and literature evidence.
Curation is manual/expert plus crowdsourced submissions.

**3. Identifiers carried.** Norine IDs (`NOR#####`), per-peptide **DataCite DOIs** (example given on
the terms page: "Orfamide A, 2015, Norine database, DOI: 10.26097/nor01255"), NCBI taxid, PMIDs, and
links to external databases (PDB, PubChem) via the REST link service. Structures are stored as
**monomeric graphs**, not as atom-level SMILES for the whole peptide; the REST documentation does
list "Get all peptides with smiles", so some SMILES exist. **No InChIKey.** For a structure-keyed KB
this is a real obstacle: monomer graphs do not convert to a standard InChIKey without work.
Confidence: **medium** on SMILES coverage (documented endpoint seen, not exercised).

**4. Bulk access.** No single dump file. Data comes out through (a) the web download form, which
exports the selected fields for a search result set, and (b) a REST API documented at
`https://bioinfo.lifl.fr/norine/service.jsp` with base path `/norine/rest/` (peptide by Norine ID,
peptide by name, all peptides with SMILES, all monomers, monomer cluster tree, external-database
links, organism by name, plus Smiles2Monomers and activity-prediction services). My guessed endpoint
paths (`/norine/rest/peptides/all` etc.) returned 404, so the exact routes must be read off the
service page. No DOI-versioned release, no dated dumps.

**5. LICENCE — SHARE_ALIKE + NON_COMMERCIAL (CC BY-NC-SA 4.0). Not seedable.** Verified live
2026-09-07 at https://bioinfo.lifl.fr/norine/terms.jsp, verbatim:

> "We have chosen to apply the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
> International (CC BY-NC-SA 4.0) to our database, under the following terms: Attribution — You must
> give appropriate credit… NonCommercial — You may not use the material for commercial purposes.
> ShareAlike — If you remix, transform, or build upon the material, you must distribute your
> contributions under the same license as the original."

And the disclaimer, verbatim: *"We cannot provide unrestricted permission regarding the use of the
data, as some data may be covered by patents or other rights."* The home page's phrase "Norine is
freely available to everybody" is immediately qualified by the CC BY-NC-SA statement — do not read
it as permissive.

**Consequence for this KB:** Norine content cannot be redistributed under CC BY 4.0. Curate-only:
use it to check facts, cite the underlying PMIDs, and re-derive from the primary literature.

**6. Data-quality traps.** Peptide "status" field exists (some entries are hypothetical/predicted).
Producer organisms are given as names plus taxid but strains are inconsistently resolved. Monomer
graph representations require Norine's own monomer vocabulary to interpret.

**7. Confidence.** High for the count and the licence (both read verbatim off the live pages).
Medium for the REST specifics.

---

### 5. Paired Omics Data Platform (PoDP)

**1. What it is.** Community platform standardising links between genome/metagenome data and
metabolomics datasets, from the iOMEGA project (Wageningen Bioinformatics, Netherlands eScience
Center); reference paper: van der Hooft et al., *Nat Chem Biol* 2021,
"A community resource for paired genomic and metabolomic data mining"
(doi:10.1038/s41589-020-00724-z, linked from the site's structured metadata).

Live statistics from `https://pairedomicsdata.bioinformatics.nl/api/stats` (verified live
2026-09-07):

| Counter | Value |
|---|---|
| projects | 81 |
| principal investigators | 53 |
| metabolome samples | 4,974 |
| **BGC↔MS2 links (`bgc_ms2`)** | **117** |
| genome records (summed over projects) | 2,639 |
| genome↔metabolomics links (summed) | 5,008 |

Genome types: metagenome 1,306; genome 1,291; MAG 42.

**2. Contribution.** The unique contribution is **spectrum-level evidence that a specific BGC
produces a specific detected mass feature**, i.e. exactly the "evidence of detection" link. But note
the scale: **117** BGC↔MS2 links in total. This is a precision resource, not a bulk one. It also
gives growth medium, extraction solvent, instrument and ionisation mode per sample, which is real
provenance for a detection claim. All records are **submitter-provided and admin-reviewed** ("After
the project is reviewed by the platform administrators (usually within two weeks), the project is
listed on the site").

**3. Identifiers carried.** GenBank/RefSeq genome accessions, MassIVE dataset accessions
(`MSV#######`), MetaboLights accessions (`MTBLS####`), MIBiG accessions where BGCs are named, NCBI
species names fetched from GenBank. **No chemical structure identifiers at all** — the metabolite
side is a spectrum/dataset reference, not a compound. Joining to a structure-keyed KB therefore
requires going through GNPS/MassIVE annotation of the referenced spectra.

**4. Bulk access.** Site: *"The projects in the platform are archived to the Zenodo repository each
month"* (from the compiled app bundle, verified live 2026-09-07). Concept DOI:
**10.5281/zenodo.3736430**. There is also a JSON REST API: `/api/projects` (project list) and
`/api/projects/{id}` (full project record), plus an OpenAPI 3.0.3 spec. Per-project JSON is
advertised in the site's schema.org metadata as
`https://pairedomicsdata.bioinformatics.nl/api/projects/{id}`, `encodingFormat: application/json`.

**5. LICENCE — ATTRIBUTION (CC BY 4.0).** Verified live 2026-09-07 from the compiled app bundle
`/static/js/main.1fc88a5c.js`. Download page, verbatim: *"This work is licensed under a Creative
Commons Attribution 4.0 International License"* with `rel="license"` pointing at
`https://creativecommons.org/licenses/by/4.0/`. Submission page, verbatim: *"By submitting your
project to the platform, you agree that the project is licensed under Creative Commons Attribution
4.0 International and can be distributed as part of the platforms dataset."* The site's schema.org
DataCatalog and per-project Dataset blocks both carry
`license: "https://creativecommons.org/licenses/by/4.0/legalcode"`. Code (`iomega/paired-data-form`)
is **Apache-2.0** (verified via the GitHub licence API). Seedable.

**6. Data-quality traps.** Only 117 of the 5,008 genome–metabolomics links are resolved down to a
BGC↔MS2 pairing; the rest are dataset-level co-occurrence, which is far weaker evidence.
Ionisation-mode skew is severe (positive 80 projects, negative 5), and 546 of the genome records are
"feces metagenome" — a metagenome is not a producer organism. Submissions are self-reported.

**7. Confidence.** High for all counts (read from the live API) and for the licence (read from the
live app bundle). The Zenodo record itself could not be fetched — see below.

---

### 6. GNPS / MassIVE and the GNPS spectral libraries

**1. What it is.** The Global Natural Products Social Molecular Networking platform (Dorrestein and
Wang labs, UCSD, now also GNPS2) hosts community MS/MS reference libraries plus MassIVE, the
underlying raw-data repository.

Size, verified live 2026-09-07 at https://external.gnps2.org/gnpslibrary: *"Total number of MS/MS
Spectra - 2,907,573"*, *"Date Last Libraries Fully Exported - 2026-03-29 01:42:23.206000"*, site
version 2025.06.13. Libraries are typed as `GNPS` (community-deposited), `GNPS_PROPOGATED`
(computationally propagated from reference spectra), `IMPORT` (imported from other resources, e.g.
MassBank) and `AGGREGATED`.

**2. Contribution.** Spectral evidence that a named structure was **detected in a real sample**, and
via MassIVE the dataset/sample it was detected in. For an NP KB this is the natural backing for
"observed in organism X" claims. Library annotation quality is tiered (bronze/silver/gold), with
higher tiers gated: *"approval is required to contribute to silver and gold libraries."*

**3. Identifiers carried.** Library spectra carry compound name, SMILES/InChI where the depositor
supplied them, adduct, instrument, and a GNPS library accession (`CCMSLIB########`); MassIVE
accessions (`MSV#######`) identify datasets. InChIKey is often derivable from the deposited
SMILES/InChI but is not guaranteed present, and **many library entries have no structure at all** —
see traps.

**4. Bulk access.** Per-library **MGF, MSP and JSON** downloads from
https://external.gnps2.org/gnpslibrary (each library links to `/gnpslibrary/<NAME>.mgf|.msp|.json`).
Preprocessed/cleaned versions (matchms and ML pipelines) are published as *"Versioned, citable
archives … available for download at Zenodo"*. Note the JSON exports are very large (I aborted a
single-library JSON fetch after it exceeded 256 MB).

**5. LICENCE — CC0_OK for native GNPS contributions, MIXED overall.** Verified live 2026-09-07 at
https://ccms-ucsd.github.io/GNPSDocumentation/downloadlibraries/ and
https://ccms-ucsd.github.io/GNPSDocumentation/spectrumcuration/, verbatim:

> "All GNPS Reference spectra contributed directly to GNPS by default will have the CC0 license."

and, on the same download page:

> "Third party libraries imported may not conform to the CC BY license and should be verified by
> users."

So: spectra in the `GNPS` type libraries are CC0 and freely seedable; spectra in `IMPORT` libraries
inherit their source licence and must be filtered per library. `GNPS_PROPOGATED` entries are
computational derivatives of reference spectra — CC0 by inheritance from GNPS-native parents, but
verify per library. The library-list page (`gnpslibrary`) itself carries no licence statement; the
CC0 statement lives only in the documentation. Confidence: **high** for the quoted text, **medium**
for its per-library application, since no machine-readable licence field is exposed in the library
table.

**6. Data-quality traps.** (a) Library entries **without structures** are common — annotation is
free-text name plus optional SMILES, and propagated/analogue libraries deliberately contain entries
whose exact structure is unknown. (b) `GNPS_PROPOGATED` entries are *inferred*, not measured for
that compound. (c) The bronze tier is unvetted community annotation; treating a bronze library match
as an identification is a well-known failure mode. (d) The same compound appears many times across
libraries with inconsistent names, so deduplication must be by InChIKey (first block) not by name.

**7. Confidence.** High for the spectrum total and export date (read from the live page). High for
the licence text. I did **not** verify MassIVE's own dataset terms — see Open questions.

---

### 7. NP-MRD — Natural Products Magnetic Resonance Database

**1. What it is.** Cloud NMR database for natural products, Wishart lab (University of Alberta) with
The Metabolomics Innovation Centre; "a freely available cloud-based, user-friendly, FAIR electronic
database" that accepts raw FIDs, processed spectra, assignments and metadata (verified live
2026-09-07 at https://np-mrd.org/about).

Size, verified live 2026-09-07 at https://np-mrd.org/statistics:

| Counter | Value |
|---|---|
| total compounds | 281,859 |
| compounds with **experimental** spectra | 3,672 |
| compounds with experimental NMR assignments | 22,491 |
| compounds with **predicted** spectra | 251,536 |
| experimental NMR spectra | 19,045 |
| total spectra incl. simulated + predicted | 5,479,144 |
| from NP Atlas | 20,468 |
| from JEOL CH-NMR-NP | 19,025 |
| from HMDB / BMRB | 879 / 284 |

**2. Contribution.** Structure-keyed compound records with **species of origin** (the site has a
"By Species of Origin" browse) and NMR evidence of characterisation. It is the best NMR-side
evidence source for NPs. But see the licence — this is curate-only.

**3. Identifiers carried.** NP-MRD accessions (`NP#######`), structures as SDF and SMILES, and
metadata XML/JSON that includes taxonomy and provenance. InChIKey is expected in the metadata
(HMDB-family schema) but I did **not** verify the field list by opening a download file.

**4. Bulk access.** https://np-mrd.org/downloads (verified live 2026-09-07): metadata in **XML** and
**JSON**, structures in **SDF** and **SMILES CSV**, each split into seven ID ranges
(NP0000001–NP0350000), all dated **2025-08-01**; NMR FID files dated 2024-09-11 (the first shard
alone is 8.8 GB). Versioning is by release date on the download page, no DOI.

**5. LICENCE — NON_COMMERCIAL (CC BY-NC 4.0). Not seedable.** Verified live 2026-09-07 on
https://np-mrd.org/about (Licensing Details section), verbatim:

> "This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International
> License. This means that our data can be used in derivative works as long as proper attribution is
> given to the source of the data, but these derivative works may not be used for commercial
> purposes."

and in the FAIR compliance section, verbatim:

> "All data and metadata in the NP-MRD are released under the Creative Commons (CC) 4.0 License
> Suite according to the Attribution (BY) and Non-commercial (NC) licensing conditions."

Note the dedicated `/licensing` path is a 404; the licensing text is a section of `/about`.

**6. Data-quality traps.** The headline "281,859 compounds" is dominated by **predicted** spectra:
only **3,672 compounds (1.3%) have experimental spectra**. A large fraction of records are
back-filled from NP Atlas and JEOL rather than deposited. The site also currently displays the
banner *"This repository is under review for potential modification in compliance with
administration directives."*, which is a continuity risk worth noting.

**7. Confidence.** High for counts, download dates and licence (all read live). Medium for the exact
identifier fields inside the metadata files (not opened).

---

### 8. MoNA — MassBank of North America

**1. What it is.** Metadata-centric auto-curating mass spectral repository, Fiehn lab, UC Davis
(https://mona.fiehnlab.ucdavis.edu/ and https://massbank.us/).

Size, verified live 2026-09-07 at `https://mona.fiehnlab.ucdavis.edu/rest/statistics/global`:

| Counter | Value |
|---|---|
| spectra | 3,596,790 |
| compounds | 892,257 |
| metadata fields | 84,091 |
| submitters | 146 |

**2. Contribution.** Very large spectral corpus keyed on chemical structures, including in-silico
libraries. Useful as detection evidence and as an InChIKey-anchored name/structure source. Curation
is **automatic** ("auto-curating"), not expert review.

**3. Identifiers carried.** MoNA spectrum IDs, InChI, **InChIKey**, SMILES, molecular formula, plus
whatever cross-references submitters attached. A dedicated bulk file exists specifically for this:
`MoNA-export-All_Spectra-identifier-table-ids.zip`, described in the REST download listing as
*"Table of spectral and chemical identifiers for all MoNA records"* — this is the cheapest way to
join MoNA to a structure-keyed corpus.

**4. Bulk access.** REST API (`/rest/...`, with a Swagger spec linked from the site) plus static
exports listed at `/rest/downloads/static`. The human downloads page is a JavaScript app and
returned no content to a plain fetch.

**5. LICENCE — ATTRIBUTION (CC BY 4.0 by default).** The licence page is client-rendered; I
extracted the text from the compiled Angular bundle `main.229f9e98534bdfed69f0.js` (verified live
2026-09-07), verbatim:

> "The content of the MoNA database is licensed under CC BY 4.0 by default. If you would like to
> publish your data under a different license, please contact us before submitting your data. Once
> your data are submitted our default license will apply."

and for code, verbatim: *"The MoNA source code, REST API, and web client are currently licensed under
the GLPL License v3"* (sic — GPL v3 is meant). Seedable, with the caveat that "by default" implies
individual submissions may carry other terms.

**6. Data-quality traps.** A large share of the 3.6M spectra are **in-silico predicted**, not
measured; the split is not visible from the global statistics endpoint. Auto-curation means metadata
normalisation errors propagate. Compound count (892,257) far exceeds any curated NP corpus, so most
entries are not natural products.

**7. Confidence.** High for the counts (live REST) and the licence text (read from the shipped
application). Medium on the in-silico proportion — not quantified.

---

### 9. MassBank (EU / consortium)

**1. What it is.** The original open mass spectral library, MassBank consortium, website hosted and
distributed by Helmholtz-Zentrum für Umweltforschung (UFZ), Leipzig (stated verbatim in the site's
bootstrap data: *"This website is hosted and distributed by the Helmholtz-Zentrum für
Umweltforschung GmbH - UFZ, Leipzig, Germany."*).

Versions and size (verified live 2026-09-07):

| Source | Value |
|---|---|
| Deployed instance `massbank.eu/MassBank-api/metadata` | version **2025.10** (2025-10-24), spectra 134,756, compounds 20,549 |
| `massbank.eu/MassBank-api/records/count` | **139,006** |
| GitHub latest release | **2026.03**, published 2026-04-15 |
| NAR 2026 paper (release 2025.05.1) | 119,845 spectra, 18,529 compounds, 53 contributors |
| Front-end version string | v2025.12.1 |

The three numbers differ because the data repository, the deployed instance and the paper are on
different release trains. Confidence: high (each read from its own primary source).

**2. Contribution.** Structure-keyed, curated MS/MS reference spectra with full acquisition
metadata — the highest-provenance spectral evidence of the spectral resources here. Records are
validated by CI against a formal record-format specification before merge, which is closer to expert
review than MoNA's auto-curation. Contributor-provided, reviewed by pull request.

**3. Identifiers carried.** Excellent. A live record fetch (`/MassBank-api/records?pageSize=1`,
verified 2026-09-07) shows per record: accession (`MSBNK-<contributor>-<id>`), authors, `license`,
`copyright`, compound names, formula, exact mass, **SMILES**, **InChI**, and a `link` array
containing **INCHIKEY**, **PUBCHEM** CID, **CHEBI**, **KEGG**, CAS, ChemSpider, CompTox DTXSID and
**ChemOnt** (ClassyFire) IDs. Directly joinable on standard InChIKey.

**4. Bulk access.** GitHub repository https://github.com/MassBank/MassBank-data (one text file per
record, organised by contributor directory — 68 contributor directories seen), with **tagged
releases** (`2026.03`) whose assets are `MassBank.json` (534 MB), `MassBank_NISTformat.msp`
(137 MB) and `MassBank_RIKENformat.msp` (168 MB), and a **Zenodo DOI** per release (badge
`zenodo.org/badge/125496536`). Also a REST API at `massbank.eu/MassBank-api/`. This is the
best-versioned spectral source in this cluster.

**5. LICENCE — ATTRIBUTION (CC BY), per record.** Verified live 2026-09-07 two ways. The record
format specification (https://raw.githubusercontent.com/MassBank/MassBank-web/main/Documentation/MassBankRecordFormat.md)
states, verbatim: *"The default Creative Commons license of MassBank record is defined as CC BY."*,
and lists `LICENSE` as a **mandatory** record tag whose value is *"Creative Commons License or its
compatible terms"*. A live API record returned `"license":"CC BY"` alongside
`"copyright":"Copyright (C) 2016 Department of Chemistry, University of Athens"`.

**Important:** because `LICENSE` is per record and only *defaults* to CC BY, a bulk ingest must read
the per-record `LICENSE` value and drop or quarantine anything that is not CC BY / CC0 (some records
historically carry CC BY-NC or CC BY-SA). Do not apply a blanket CC BY assumption.

**6. Data-quality traps.** Per-record licence heterogeneity (above) is the main one. There is also a
`legacy.blacklist` file and a `deprecated` field in the API, so deprecated records must be filtered.
Contributor prefixes overlap conceptually with MoNA and GNPS imports, so the same spectrum can be
ingested three times from three resources — deduplicate on SPLASH or InChIKey + acquisition params.

**7. Confidence.** High throughout; every figure was read from a live API or the GitHub release API.

---

### 10. NPClassifier

**1. What it is.** Deep-neural-network structural classifier for natural products, from Kim, Wang,
Leber, Nothias, Reher, Kang, van der Hooft, Dorrestein, Gerwick and Cottrell, *J Nat Prod* 2021,
84(11):2795–2807, doi:10.1021/acs.jnatprod.1c00399. Code at https://github.com/mwang87/NP-Classifier.

Ontology size, counted directly from `Classifier/dict/index_v1.json` in the repository (verified live
2026-09-07):

| Level | Terms |
|---|---|
| Pathway | **7** |
| Superclass | **77** |
| Class | **687** |

The seven pathways are: Alkaloids; Amino acids and Peptides; Carbohydrates; Fatty acids;
Polyketides; Shikimates and Phenylpropanoids; Terpenoids.

**2. Contribution.** A **biosynthesis-oriented** chemical classification keyed purely on structure —
it takes a SMILES and returns pathway/superclass/class. That makes it directly applicable to every
record in a structure-keyed KB, computed locally, with no join required. It complements MIBiG's
biosynthetic class (which describes the *gene cluster*) by describing the *molecule*.

**3. Identifiers carried.** None — it consumes SMILES and emits ontology terms. Its output must be
stored as your own annotation, with the model version recorded.

**4. Bulk access.** No precomputed annotation dump is published by the project itself. Two routes:
(a) run the classifier locally (Docker compose, models fetched by `get_models.sh`); (b) call the
public API. I verified the API live 2026-09-07:
`https://npclassifier.gnps2.org/classify?smiles=<SMILES>` returned, for the MIBiG SMILES of
abyssomicin C, `{"class_results":["Spirotetronate macrolides"],"superclass_results":["Macrolides"],
"pathway_results":["Polyketides"],"isglycoside":false}`. The older host
`https://npclassifier.ucsd.edu/` returned an empty body. NP Atlas and GNPS also carry precomputed
NPClassifier terms for their own compounds.

**5. LICENCE — CC0_OK for the ontology and models; MIT for the code.** Verified live 2026-09-07 in
the repository README, verbatim:

> "The license as included for the software is MIT. Additionally, all data, models, and ontology are
> licensed as [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/)."

The `LICENSE` file is the MIT text (Copyright (c) 2020 Ming Wang). This is the most permissive
classification vocabulary available and is the obvious default for an NP KB.

**6. Data-quality traps.** It is a classifier: outputs are **predictions**, and must be stored as
such with the model version. It returns multiple labels per level (note the plural `*_results`
arrays) and an `isglycoside` flag. It was trained on natural products, so it is unreliable on
synthetic or non-NP structures. Disagreements with ClassyFire are expected by design — see below.

**7. Confidence.** High: ontology counts from the repository file, licence from the README, API
behaviour tested live.

---

### 11. ClassyFire and ChemOnt

**1. What it is.** Rule-based structural taxonomy (Feunang et al. 2016) over the ChemOnt ontology,
Wishart lab / The Metabolomics Innovation Centre.

Size and version, verified live 2026-09-07 at http://classyfire.wishartlab.com/downloads:
**ChemOnt v2.1**, OBO format, **4825 categories**, **9012 synonyms**, released **2016-08-27**.
Precomputed annotation sets are offered for HMDB 3.6, T3DB, ChEBI 126 and DrugBank 5, all released
**2016-08-29/31**.

**2. Contribution.** A second, independent chemical taxonomy; widely used and already embedded in
other resources (MassBank records carry `ChemOnt` links, e.g.
`CHEMONTID:0000079; Organic compounds; Organoheterocyclic compounds; Azolines; Imidazolines`, seen
live in a MassBank API record). Good for cross-checking, and for joining to resources that already
store ChemOnt IDs.

**3. Identifiers carried.** `CHEMONTID:#######` terms; annotation CSVs are keyed to the source
database's IDs (HMDB, ChEBI, DrugBank, T3DB), and ClassyFire's API is addressed by InChIKey.

**4. Bulk access.** `ChemOnt_2_1.obo.zip` plus the four annotation CSV/zip files from the downloads
page. A REST API exists (`/entities/<InChIKey>.json`); my test key returned 404, meaning that
structure simply is not in their cache, not that the API is gone.

**5. LICENCE — RESTRICTED / effectively NON_COMMERCIAL.** Verified live 2026-09-07 at
http://classyfire.wishartlab.com/downloads, verbatim:

> "ClassyFire is offered to the public as a freely available resource. Use and re-distribution of
> the data, in whole or in part, for commercial purposes requires explicit permission of the authors
> and explicit acknowledgment of the source material (ClassyFire) and the original publication (see
> below). We ask that users who download significant portions of the database cite the ClassyFire
> paper in any resulting publications."

This is a bespoke licence, not a Creative Commons one, and it is incompatible with releasing derived
records under CC BY 4.0 (which permits commercial reuse). **Not seedable.** Use NPClassifier instead
for the KB's own classification, and treat ChemOnt IDs that arrive embedded in third-party CC BY
records (e.g. MassBank) as a separate question to raise with the licence owner.

**6. Data-quality traps.** The ontology and all published annotation sets are **from 2016** and have
not been re-released; source databases have moved on by many versions. ClassyFire is
structure-rule-based and deliberately not biosynthesis-aware, so it will disagree with NPClassifier
on exactly the cases an NP KB cares about — e.g. a molecule ClassyFire files by ring system that
NPClassifier files by biosynthetic origin. Neither is "right"; store both with provenance and never
merge them into one class field.

**7. Confidence.** High for version, counts, dates and licence text (read live). Medium for the API
state (one 404 test).

---

### 12. MetaCyc / BioCyc

**1. What it is.** Curated metabolic pathway and enzyme database, SRI International (Karp group);
MetaCyc is the reference pathway database within the BioCyc collection. Footer states
"©2026 SRI International" (verified live 2026-09-07).

Size and release version could **not** be established from the pages I could fetch (the site is
heavily scripted and the statistics live behind the organism selector). Not verified.

**2. Contribution.** MetaCyc contains secondary-metabolite biosynthesis pathways with per-step
reactions, enzymes and EC numbers — in principle exactly the "pathway/enzyme steps" layer. It also
indexes compounds by InChIKey (the site's own search help says a query may be *"A full or partial
compound InChI-key. Examples: CKLJMWTZIZZHCS-REOHCLBHSA-M"*), so it is structurally joinable.

**3. Identifiers carried.** MetaCyc compound/reaction/pathway IDs, InChIKey, EC numbers, UniProt
cross-references. Confidence: medium (inferred from the search help text and general knowledge of
the schema; I did not open a data file, because the data files are paywalled).

**4. Bulk access.** Download formats listed on https://biocyc.org/download.shtml: BioPAX, Pathway
Tools attribute-value, Pathway Tools tabular, SBML, and GO annotations (EcoCyc only). Access is
gated (below).

**5. LICENCE — RESTRICTED. Not seedable.** Verified live 2026-09-07 at
https://biocyc.org/download.shtml, verbatim:

> "Access to BioCyc data files requires (1) a license (see bottom of page), and (2) a paid BioCyc
> subscription costing at least $5,000 (exceptions: access to data files for EcoCyc and for
> Faecalibacterium prausnitzii A2-165 are free, although a license is required)."

and:

> "Access to the Pathway Tools software by academic users requires a free license… For access by
> commercial users, a fee is required."

Even the free-file exceptions (EcoCyc, *F. prausnitzii*) require accepting a licence, and neither is
a natural-product organism of interest. Do not ingest MetaCyc content. If pathway steps are needed
under an open licence, **Rhea plus UniProt is the substitute**.

**6. Data-quality traps.** Not assessed — no access.

**7. Confidence.** High for the licence (quoted verbatim from the live download page). Version and
size: **not verified**.

---

### 13. KEGG

**1. What it is.** Kyoto Encyclopedia of Genes and Genomes, Kanehisa Laboratories. Relevant content
for this KB: the secondary-metabolite biosynthesis maps (map01050s, biosynthesis of terpenoids,
polyketides, alkaloids etc.), the COMPOUND database and the reaction/orthology links.

Version/size: not verified (KEGG's release statistics were not fetched).

**2. Contribution.** In principle, pathway-level context and compound–enzyme–organism links. In
practice, irrelevant to a CC BY KB because of the licence.

**3. Identifiers carried.** KEGG COMPOUND `C#####`, DRUG `D#####`, reaction `R#####`, pathway
`map#####`, KO, plus cross-references. MassBank records already carry KEGG IDs as links.

**4. Bulk access.** KEGG FTP, subscription only. REST API for limited academic web use.

**5. LICENCE — RESTRICTED. Not seedable.** Verified live 2026-09-07 at
https://www.kegg.jp/kegg/legal.html (last updated on that page: October 1, 2024), verbatim:

> "KEGG is an original database product, copyright Kanehisa Laboratories."

> "Academic users may freely use the KEGG website at https://www.kegg.jp/ or its mirror site at
> GenomeNet https://www.genome.jp/kegg/. Academic users who utilize KEGG for providing services are
> requested to obtain an academic service provider license, which is included in the KEGG FTP
> academic subscription."

> "Non-academic users must understand that KEGG is not a public database, nor is it a publicly
> funded database. Non-academic use of KEGG requires a commercial license."

A KB released CC BY 4.0 is by definition available for commercial reuse, so it cannot embed KEGG
content. Note the sharper trap: "academic users who utilize KEGG for **providing services**" already
need a paid academic service-provider licence — publishing a KEGG-derived KB is providing a service.
Cite KEGG identifiers as external pointers only, do not copy KEGG content.

**6. Data-quality traps.** Not assessed.

**7. Confidence.** High for the licence (verbatim from the live page). Version/size not verified.

---

### 14. Rhea

**1. What it is.** Expert-curated database of biochemical reactions, SIB Swiss Institute of
Bioinformatics; an ELIXIR Core Data Resource and Global Core Biodata Resource (both badges present
on the live site).

Release, verified live 2026-09-07 at `https://ftp.expasy.org/databases/rhea/rhea-release.properties`:

```
rhea.release.number=142
rhea.release.date=2026-09-02
```

Reaction count not verified.

**2. Contribution.** The open-licence route to **enzyme-level pathway steps**: Rhea reactions are
written over **ChEBI** structures and are the reaction vocabulary used by UniProt catalytic-activity
annotations, so a chain of `compound (ChEBI) → Rhea reaction → UniProt enzyme → organism` is
constructible entirely under open licences. Rhea also cross-references EC numbers. Curation is
expert.

**3. Identifiers carried.** `RHEA:#####` reaction IDs, **ChEBI** IDs for every participant, EC
numbers, and UniProt links from the UniProt side. The site's own search box accepts
`inchikey:XLYOFNOQVPJJNP-UHFFFAOYSA-N`, confirming InChIKey-based lookup into ChEBI structures
(verified live from the search placeholder text). Joinability to a structure-keyed corpus is
therefore good, via ChEBI.

**4. Bulk access.** FTP at https://ftp.expasy.org/databases/rhea/ with subdirectories `rdf/`,
`tsv/`, `txt/`, `biopax/`, `ctfiles/`, `old_releases/`, plus a SPARQL endpoint and a REST API.
Versioned by numbered releases with a machine-readable release properties file and an
`old_releases/` archive (verified live 2026-09-07).

**5. LICENCE — ATTRIBUTION (CC BY 4.0).** The `/help/license` web page is script-rendered and would
not yield text; the FTP LICENSE file did. Verified live 2026-09-07 at
https://ftp.expasy.org/databases/rhea/LICENSE.txt, verbatim:

> "We have chosen to apply the Creative Commons Attribution 4.0 International (CC BY 4.0) License
> (https://creativecommons.org/licenses/by/4.0/) to all copyrightable parts of the Rhea database.
> All files in the Rhea FTP directory may be copied and redistributed freely, without advance
> permission, provided that this copyright statement is reproduced with each copy."

> "DISCLAIMER: We make no warranties regarding the correctness of the data, and disclaim liability
> for damages resulting from its use. All data is provided for research, educational and
> informational purposes only. It is not in intended to be used for medical purposes such as
> diagnosis, treatment or care."

Seedable.

**6. Data-quality traps.** Rhea covers **enzymatic reactions**, not multi-step natural-product
assembly lines; a PKS module is not one Rhea reaction. Coverage of secondary metabolism is far
thinner than of central metabolism. Participants are ChEBI entities, so a compound absent from ChEBI
cannot be expressed.

**7. Confidence.** High for release number/date and licence (both read from the live FTP files).
Reaction count and NP coverage: not verified.

---

### 15. Biosynthetic class vocabularies used by MIBiG

The brief listed "Polyketide, NRP, RiPP, Terpene, Saccharide, Alkaloid, Other". **That is the MIBiG
3.x vocabulary and it is out of date for 4.0.**

Observed values of `biosynthesis.classes[].class` across all 3013 MIBiG 4.0 JSON files (my parse,
verified 2026-09-07) — exactly six values, no others:

| Class | Entries |
|---|---|
| PKS | 1238 |
| NRPS | 1020 |
| ribosomal | 447 |
| other | 421 |
| terpene | 241 |
| saccharide | 216 |

(The live API reports the same six with display labels PKS / NRPS / Ribosomal / Other / Terpene /
Saccharide, and counts within one or two of these.)

**`alkaloid` no longer exists as a biosynthetic class.** The MIBiG 4.0 paper states it explicitly
(verified live 2026-09-07 at https://pmc.ncbi.nlm.nih.gov/articles/PMC11701617/), verbatim:

> "Additionally, we have separated biosynthetic classification from compound classification (e.g. we
> removed 'alkaloid' as a biosynthetic class) and introduced a custom biosynthesis-inspired chemical
> ontology for SMs (Supplementary Data 1, section 3.4) based on the work by Dewick."

Two consequences for the KB:

1. Model **class of the gene cluster** and **class of the molecule** as separate fields. MIBiG 4.0
   now does exactly this: `biosynthesis.classes[].class` for the cluster, and a per-compound
   `classes[]` using MIBiG's own Dewick-based ontology (observed values include `Macrocyclic`,
   `Cyclic polyketide`, `Polycyclic polyketide`, `Linear`, `Alkylresorcinol/phloroglucinol
   polyketide`, `Macrocyclic polyketide`; present on 1036 compound records).
2. There are now **at least three competing molecule-level ontologies** in play — MIBiG's Dewick
   ontology, NPClassifier (CC0), and ChemOnt (restricted). Only NPClassifier is both open and
   computable from structure alone; make it the KB's primary and keep the others as
   provenance-tagged alternates.

Subclass vocabulary is also richer than the class list suggests: observed class/subclass pairs
include NRPS/Type I (995), PKS/Unknown (818), ribosomal/RiPP (412), other/other (377), PKS/Type I
(226), terpene/Unknown (168), saccharide/(null) (164), PKS/Iterative type I (65),
saccharide/hybrid-tailoring (41), PKS/Type II (39). Note the heavy use of `Unknown` — subclass is
frequently unfilled, and the paper records a newly defined "non-ribosomal peptide synthetase Type VI
(modular, non-condensation-domain peptide-bond-forming)".

---

## Refuted or unverifiable claims

**Refuted / corrected:**

1. **"MIBiG biosynthetic classes include Alkaloid."** False for MIBiG 4.0 — removed as a
   biosynthetic class, stated in the paper and confirmed by the absence of the value across all 3013
   release files.
2. **"MIBiG entries carry InChIKeys."** False. There is no InChI or InChIKey field in the MIBiG 4.0
   JSON; only SMILES plus external database IDs.
3. **"MIBiG's `questionable` quality flag means the entry is doubtful."** Misleading. It
   predominantly marks legacy-format entries pending re-curation, per the paper's own wording.
4. **"antiSMASH-DB is CC BY because the paper is CC BY."** Conflation. The CC BY statement in the
   NAR article applies to the *article*. No data licence is published for the database dumps.
5. **"MoNA data is CC BY 4.0 because a search summary said so."** The claim happens to be right, but
   the search snippet quoted the *journal article's* open-access boilerplate. The actual MoNA
   licence text ("licensed under CC BY 4.0 by default") was obtained from the MoNA application
   itself, and it carries a per-submission caveat the snippet omitted.
6. **"Norine is freely available to everybody"** (Norine's own home-page phrasing) must not be read
   as an open licence — the same sentence continues into CC BY-NC-SA 4.0.
7. **MassBank record counts vary by source** (119,845 in the 2026 paper; 134,756 in the deployed
   instance's metadata; 139,006 from the record-count endpoint). None is wrong; they are different
   release trains. Do not quote a single figure without naming its source.

**Could not be verified (URL failures, all attempted 2026-09-07):**

| URL | Failure |
|---|---|
| `https://zenodo.org/api/records/3736430`, `/records/4575489`, `/records/7497442` | HTTP 403 via curl ("Access to this resource has been restricted due to unusual traffic"); "unable to get issuer certificate" via WebFetch. **No Zenodo record was directly verified in this work** — PoDP, MIBiG and MassBank Zenodo DOIs are reported as cited by their own primary sites/papers, not as independently confirmed. |
| `https://bioinformatics.nl/~kauts001/ltr/bigslice/paper_data/` | HTTP status 000, 0 bytes. BiG-FAM's documented bulk-download location appears unreachable. |
| `https://bioportal.bioontology.org/ontologies/CHEMONT` | Cloudflare interstitial ("Just a moment…"); ChemOnt facts taken from the ClassyFire downloads page instead. |
| `https://www.rhea-db.org/help/license` | HTTP 403 via WebFetch; script-only shell via curl. Licence obtained from the FTP LICENSE.txt instead. |
| `https://antismash-db.secondarymetabolites.org/api/v1.0/stats` | `{"error":"Internal server error"}`. `/api/stats` and `/api/v2.0/stats` work. |
| `https://bioinfo.lifl.fr/norine/rest/{peptides,monomers}/...` | 404 on my guessed paths; the documented service page confirms the API exists but the exact routes were not extracted. |
| `https://npclassifier.ucsd.edu/` | Empty response body. The working host is `https://npclassifier.gnps2.org/`. |
| `https://classyfire.wishartlab.com/` (home), `https://mibig.secondarymetabolites.org/` (home), `https://antismash-db.secondarymetabolites.org/` (home), `https://pairedomicsdata.bioinformatics.nl/` (home), `https://mona.fiehnlab.ucdavis.edu/downloads` | All returned only a page title to both WebFetch and curl — single-page apps. Facts were recovered from their JSON APIs or compiled JS bundles, as noted per source. |
| `https://external.gnps2.org/gnpslibrary/GNPS-NIH-NATURALPRODUCTSLIBRARY.json` | Aborted: response exceeded 256 MB. |

**Not verified (not attempted or inconclusive):**

- MetaCyc/BioCyc release version, pathway and compound counts.
- KEGG release version and secondary-metabolite map counts.
- Rhea total reaction count.
- MassIVE's own dataset terms of use (distinct from the GNPS library CC0 statement).
- NP-MRD's per-record identifier field list (download files not opened).
- The proportion of MoNA spectra that are in-silico rather than measured.

---

## Open questions

1. **Is there a machine-readable "reviewed" flag in MIBiG?** The paper recommends filtering to
   reviewed entries for machine-learning use and says the website supports it, but the 4.0 JSON dump
   exposes reviewers only as a pseudonymous ID that is the `AAAA…` placeholder in 2988 of 3013
   entries. Either the flag was added after the 4.0 release (the live site runs `4.0alpha1` of a
   newer build) or it is derived server-side. Resolve by fetching
   `mibig_json_4.0_all_jsons.tar.xz` (2026-03-24) and diffing the schema, or by asking the MIBiG
   team. This matters: "reviewed only" is the natural high-confidence subset for the KB.

2. **What licence covers antiSMASH-DB's bulk dumps?** No statement exists. Since the KB would only
   use antiSMASH-DB for genome→BGC context rather than compound records, one option is to skip it
   entirely; the other is to email the maintainers (mail address is on the antiSMASH site) and get a
   one-line CC BY or CC0 confirmation. Recommend asking, because the same team maintains MIBiG under
   CC BY and is likely to agree.

3. **Which GNPS libraries are CC0 and which are imports?** The library table types each library
   (`GNPS`, `GNPS_PROPOGATED`, `IMPORT`, `AGGREGATED`) but publishes no per-library licence field.
   A seeding pipeline needs an explicit allow-list of library names to ingest. Build it from the
   `type` column and verify the handful of large `IMPORT` libraries individually.

4. **Per-record licence distribution in MassBank.** `LICENSE` is mandatory and defaults to CC BY, but
   the actual distribution of values across the 139,006 records is unknown. Compute it from the
   `MassBank.json` release asset before ingesting, and quarantine any non-CC BY/CC0 value.

5. **Can ChemOnt IDs that arrive inside CC BY records (MassBank) be redistributed?** MassBank
   records are CC BY and contain `ChemOnt` classification strings; ClassyFire's own terms restrict
   commercial redistribution of its data. This is a genuine conflict that should be flagged to
   whoever owns licence policy for the KB, rather than resolved by an agent. Safe default: drop the
   ChemOnt strings, keep NPClassifier.

6. **How to reach Norine's content legitimately.** Norine is the best NRP-specific resource and it is
   CC BY-NC-SA. The compliant route is to use it as a *pointer* to the primary literature (it exposes
   PMIDs per peptide) and re-curate, or to ask the Lille team for a CC BY exception for structure +
   producer + taxid fields only. Same pattern applies to NP-MRD (CC BY-NC).

7. **Are the Zenodo archives actually reachable from a normal client?** Every Zenodo fetch in this
   session was blocked, so the PoDP monthly archive, the MIBiG Zenodo community and the MassBank
   release DOIs are unconfirmed as working download routes. Retry from a different network before
   designing a pipeline around them; the non-Zenodo alternatives
   (`dl.secondarymetabolites.org`, GitHub release assets, PoDP's `/api/projects`) all worked and are
   the safer primary route.
