# Natural-product STRUCTURE and OCCURRENCE aggregators — source assessment

Research date: **2026-09-07**. All "verified live" claims were fetched on that date by the URL given.
Target KB: one record per individual chemical structure keyed by Standard InChIKey, carrying producer
organism, biosynthetic origin, bioactivity, target, mechanism, with evidence. Record content to be
released **CC BY 4.0**, so only **CC0** and **CC BY** upstream sources are seedable.

## Summary

**Seedable now (CC0 / CC BY, verified):**

| Source | Licence (verified) | What it gives |
|---|---|---|
| LOTUS via Wikidata | CC0 (Wikidata main-namespace structured data) | 674,454 structure–organism–reference triples, InChIKey + organism QID + reference DOI |
| COCONUT 2.0 bulk downloads | CC0 stated on download page | 738,827 structures with computed properties, NPClassifier + ClassyFire |
| ChEBI | CC BY 4.0 | 218,768 terms, curated metabolite-role subtree (16,362 entities with a metabolite role) |
| CyanoMetDB v3 (Zenodo) | CC BY 4.0 on the Zenodo record | ~3,085 cyanobacterial metabolites, manually curated from primary literature |

**Not seedable (NonCommercial, ShareAlike, restricted, or unverified):**

- **NPAtlas** — CC BY-NC 4.0 **from release 2024_09 onward** (was CC BY 4.0 through 2024_03). This is the
  single most painful exclusion: NPAtlas is the best-curated microbial NP occurrence resource, with NCBI
  taxids and DOI+PMID on every compound. Only the ≤2024_03 CC BY releases are seedable.
- **CMNPD** — CC BY-NC-SA 4.0 (both NC and SA). Curate-only.
- **NPBS Atlas** — CC BY-NC 4.0 stated on its own licence page.
- **NPASS** — **no data licence anywhere on the site**; UNVERIFIED. Third-party registries say CC-BY-NC.
- **KNApSAcK** — explicit no-redistribution, no-commercial-use notice. RESTRICTED.
- **StreptomeDB 4** — no licence statement on site or download page. UNVERIFIED.
- **SuperNatural 3.0** — host no longer resolves (checked against 8.8.8.8). Effectively gone.
- **UNPD** — defunct since ~2017; survives only as a COCONUT sub-collection.
- **NuBBE** — site unreachable today (TCP timeout); licence unverified.
- **DNP, MarinLit, AntiBase (Wiley Identifier of Natural Products)** — commercial, subscription,
  redistribution prohibited. Not usable as a seed under any reading.

**Practical recommendation.** Seed the occurrence layer from **LOTUS-via-Wikidata (CC0)**. It is the only
large corpus that is simultaneously CC0, InChIKey-keyed, per-pair reference-attached, and taxonomy-resolved
to NCBI/GBIF/OTT ids: 674,454 (structure, organism, reference) triples over 227,319 unique InChIKeys.
Seed the structure layer and chemical classification from **COCONUT**, but two caveats decide how:
its CC0 banner is contradicted by its own README and by its contents (it demonstrably contains NPAtlas,
CMNPD, KNApSAcK and NPASS records), so filter on the `collections` column; and its organism and DOI lists
are unpaired, so it supplies structures and classifications, not referenced occurrence edges.
Add **ChEBI (CC BY)** for curated class/role scaffolding and **CyanoMetDB (CC BY)** for cyanobacteria.
Treat NPAtlas, CMNPD, NPASS and NPBS Atlas as curation targets, not seeds.

---

## Per-source findings

### 1. COCONUT 2.0 — COlleCtion of Open Natural prodUcTs

**1. What / who / version / size.** Aggregator of open NP datasets, developed and maintained by the
Steinbeck group at Friedrich Schiller University Jena. Current release **September 2026** (files named
`…-09-2026`), verified live 2026-09-07 at <https://coconut.naturalproducts.net/download>. Statistics page
(<https://coconut.naturalproducts.net/stats>, verified live) reports:

| Metric | Value |
|---|---|
| Unique molecules | 738,829 |
| Revoked molecules | 38,828 (~5%) |
| Unique organisms | 73,137 (63,924 with an IRI) |
| Molecules with organisms | 315,147 (42.7%) |
| Citations mapped | 124,776 |
| Molecules with citations | 286,478 (38.8%) |
| Collections | 71 (70 distinct tags appear in the CSV export) |
| Geo locations | 2,847 |

I independently downloaded `coconut_csv_lite-09-2026.zip` (190 MB) and counted **738,827 data rows**,
consistent with the stated 738,829. Confidence: high (verified by download).

The 2.0 paper (Chandrasekhar et al., *NAR* 53:D634, 2025, <https://doi.org/10.1093/nar/gkae1063>) reports
695,133 molecules from 63 collections at publication, so the live database has grown since.

**2. Contribution.** Structures at scale, plus computed physicochemical properties, sugar-moiety flags,
NP-likeness, Murcko framework, ClassyFire (`chemical_class`, `chemical_sub_class`, `chemical_super_class`,
`direct_parent_classification`) and **NPClassifier** (`np_classifier_pathway`, `_superclass`, `_class`,
`_is_glycoside`). Organism and citation links exist in the full dump, not in the lite CSV. Organism strings
are mapped to ontology terms via EMBL-EBI OLS4 or the Global Names Finder API, i.e. **name resolution, not
hand curation**. Classification fields are all **computed**. Names/synonyms and references are inherited
from source collections, so their quality is the quality of the worst upstream collection.

**3. Identifiers.** I downloaded and inspected **both** CSV exports. The lite CSV has 40 columns:
`identifier` (CNP…), `canonical_smiles`, `standard_inchi`, `standard_inchi_key`, `name`, `iupac_name`,
`annotation_level`, descriptors, then ClassyFire and NPClassifier fields. The **full** CSV
(`coconut_csv-09-2026.csv`, 236 MB zipped) has 44 columns — the same 39 plus **`organisms`, `collections`,
`dois`, `synonyms`, `cas`**.

**Standard InChIKey is present and is the natural join key.** But note what is *absent*: there is **no
PubChem CID, no ChEBI ID, no Wikidata QID, and no NCBI taxid column in either CSV export.** `organisms` is a
pipe-delimited list of bare organism *name strings* (e.g. `Lyngbya|Lyngbya sp.`) and `dois` is a separate
pipe-delimited list. The two lists are **not paired**, so a COCONUT row tells you "this compound has been
associated with these organisms" and "these DOIs are associated with this compound" — it does **not** give
you a (structure, organism, reference) triple. For referenced occurrence edges you need LOTUS or NPAtlas.
Cross-references may exist in the 31.91 GB SQL dump; they are not in the CSVs. Confidence: high (measured).

Coverage measured over all 738,827 rows of the full CSV:

| Metric | Value |
|---|---|
| Rows | 738,827 |
| Unique Standard InChIKeys | 728,421 (≈10,400 rows share a key with another row) |
| Rows with ≥1 organism | 273,553 (37.0%) |
| Rows with ≥1 DOI | 241,767 (32.7%) |
| Rows with both | 240,870 (32.6%) |
| Distinct collections | 70 |

**4. Bulk access.** Open HTTP downloads from `https://coconut.s3.uni-jena.de/prod/downloads/2026-09/…`:
2D SDF lite 287.6 MB, 2D SDF full 691.7 MB, 3D SDF 305.3 MB, CSV lite 191 MB, CSV full 207.9 MB, and a
full SQL dump `coconut-dump-09-2026.sql` at 31.91 GB (includes inactive records). Versioning is by
month-year in the filename; older releases are archived on Zenodo under concept
<https://zenodo.org/search?q=parent.id%3A13382750>. There is a REST API but it is **not anonymous**:
`GET https://coconut.naturalproducts.net/api/molecules?limit=1` returned `{"message":"Unauthenticated."}`
(verified live 2026-09-07). Bulk files need no account.

**5. LICENCE — read this carefully.** The download page states, verbatim (verified live 2026-09-07 at
<https://coconut.naturalproducts.net/download>):

> "COCONUT data is released under the Creative Commons CC0 license, allowing for free use, modification,
> and distribution without any restrictions. No attribution is required when utilizing this data."

The About page states: "Complete curated dataset is available for download under CC0 License" and
"COCONUT infrastucture code is licensed under the MIT license".

**But** the project's own README contradicts the blanket claim, verbatim (verified live 2026-09-07 at
<https://raw.githubusercontent.com/Steinbeck-Lab/coconut/main/README.md>):

> "COCONUT infrastructure code is licensed under the MIT license - see the LICENSE. Every source on
> COCONUT comes with its own specific license. It is essential to review the license details for each
> dataset before using it."

The same README also carries the odd line "The code for this web application is released under the MIT
license. Copyright © CC-BY-SA 2024."

**Classification: CC0_OK for the aggregate as published, with a serious documented upstream-licence
caveat.** I tallied the `collections` column across all 738,827 rows. The 70 distinct collections
demonstrably include sources that are **not** CC0 and in several cases forbid redistribution outright:

| Collection inside COCONUT | Rows | Its own licence (this report) |
|---|---|---|
| Super Natural II | 311,887 | unverified / host gone |
| Wikidata Natural Products | 196,593 | CC0 |
| Supernatural3 | 124,944 | unverified / host gone |
| NPASS | 81,801 | **no licence stated** |
| KNApSaCK | 47,475 | **redistribution explicitly prohibited** |
| NPAtlas | 34,748 | **CC BY-NC (current releases)** |
| UNPD | 31,207 | unverified, defunct |
| CMNPD | 30,700 | **CC BY-NC-SA** |
| ChEBI NPs | 14,547 | CC BY |
| StreptomeDB | 6,324 | unverified |

So the download page's unqualified "CC0 … without any restrictions" cannot be literally true for every
record: roughly 200,000 rows carry a tag from a collection whose upstream licence is NC, SA, restricted, or
unstated. The README's per-source caveat is the accurate statement. Practical mitigation: **filter on the
`collections` column** and seed only from rows whose collections are all CC0/CC BY (Wikidata NP, ChEBI NPs,
and other verified-open collections), rather than relying on the CC0 banner. Confidence: high that both
licence texts exist as quoted; high that the aggregate contains non-CC0 upstream content (measured).

**6. Quality traps.** Stereochemistry is preserved from sources in 2.0 (1.0 used parent structures), so
stereoisomers are separate entries and duplicate-looking InChIKey first-blocks are common. Multi-component
entries were removed and ChEMBL-pipeline standardization applied, so salts are largely handled. Roughly 5%
of molecules are **revoked** and must be filtered. `annotation_level` runs 0–5; in the first 200,000 lite
rows I measured 20,980 at level 0 and 64,919 at level 1, i.e. a large low-annotation tail. **101,817 of
those 200,000 rows (51%) have an empty `name` field** — name-less records are a real hazard.

Measured over the full export: only **37.0%** of rows carry any organism and **32.7%** any DOI, so two
thirds of COCONUT cannot support a referenced occurrence claim. **728,421 unique InChIKeys across 738,827
rows** means ~10,400 rows duplicate another row's Standard InChIKey — deduplicate on ingest. And, as noted
above, organism and DOI lists are **unpaired**, so COCONUT cannot by itself attribute a specific occurrence
to a specific reference. Confidence: high (measured directly).

### 2. LOTUS — the LOTUS Initiative

**1. What / who / version / size.** Referenced structure–organism pair resource, Rutz, Bisson, Allard et
al., *eLife* 11:e70780 (2022), <https://elifesciences.org/articles/70780>. The paper reports 750,000+
referenced pairs, 290,000+ structures, 40,000+ organisms, 75,000+ references at publication.

The living resource is **Wikidata**, with periodic frozen exports on Zenodo. Latest frozen export verified
live 2026-09-07 via the Zenodo API: record **19360665**, published **2026-04-13**, concept DOI
`10.5281/zenodo.5794106`, version DOI `10.5281/zenodo.19360665`. Its own change report says the triplet
table went from 658,502 to 674,151 entries (+39,530 added, −23,881 removed).

I downloaded `260413_frozen.csv.gz` (20.6 MB) and measured directly:

| Metric | Measured value |
|---|---|
| Rows (triples) | 674,454 |
| Unique Standard InChIKeys | 227,319 |
| Unique organism Wikidata QIDs | 37,486 |
| Unique reference DOIs | 91,382 |
| Rows with an empty DOI | 175 |
| Rows flagged `manual_validation` | 0 |

Confidence: high (measured from the file).

**2. Contribution.** This is the occurrence backbone: every row is a (structure, organism, reference)
triple, not a bare compound–organism assertion. The metadata table adds structural descriptors, NPClassifier
and ClassyFire classifications, Open Tree of Life taxonomy, PubChem properties, and PMID/PMCID. Curation is
**rule-based automated validation with manual spot-checking** — the paper reports ~30% of 2.5M harvested
entries survived validation, and a 100-entry manual test gave 97% true positives. Not hand-curated
record-by-record.

**3. Identifiers — best in class for joinability.** Core table columns (verified from the file header):
`structure_inchikey, organism_name, reference_doi, manual_validation, organism_wikidata, structure_wikidata,
reference_wikidata`. Metadata table columns include `structure_inchi, structure_smiles, structure_cid`
(PubChem), `structure_taxonomy_npclassifier_*`, `structure_taxonomy_classyfire_*`, and crucially
`organism_taxonomy_gbifid, organism_taxonomy_ncbiid, organism_taxonomy_ottid` plus a full
domain→varietas rank ladder. So: **Standard InChIKey, SMILES, InChI, PubChem CID, Wikidata QIDs for all
three entities, NCBI taxid, GBIF ID, OTT ID, and DOI** all in one table.

**4. Bulk access.** Zenodo, versioned with per-version DOIs and a concept DOI; four files including a
`lotus_exporter.py` marimo notebook that regenerates the export from live Wikidata. Also queryable live via
the Wikidata SPARQL endpoint. The web mirror <https://lotus.naturalproducts.net> exists but see below.

**5. LICENCE — verify the route you actually use.** Two different answers:

- The initiative's own homepage says, verbatim (verified live 2026-09-07 at <https://lotus.nprod.net/>):
  > "The LOTUS data is available under CC0 licence. It is hosted in parallel at https://www.wikidata.org/ ,
  > https://search.nprod.net/ and at https://lotus.naturalproducts.net/ ."
- Wikidata's own licensing page states, verbatim (verified live 2026-09-07 at
  <https://www.wikidata.org/wiki/Wikidata:Licensing>):
  > "All structured data in the main, property and lexeme namespaces is made available under the Creative
  > Commons CC0 License"
  with text in other namespaces under CC BY-SA 4.0.
- **However**, the Zenodo frozen export record 19360665 is tagged **`cc-by-4.0`**, not CC0 (verified live
  2026-09-07 via `https://zenodo.org/api/records/19360665`).

**Classification: CC0_OK via the Wikidata route** (SPARQL query or Wikidata dumps → main-namespace
structured data is CC0). **ATTRIBUTION (CC BY 4.0) if you take the Zenodo CSVs**, per the Zenodo record's
own licence field. Both are compatible with a CC BY 4.0 release; take the Wikidata route if you want CC0
cleanliness, cite Rutz et al. either way. Confidence: high.

**6. Quality traps.** The web mirror is explicitly dying — the homepage says lotus.naturalproducts.net "is
unmaintained and will be slowly phased out", so do not build against it. The `manual_validation` column is
**present but empty in every one of the 674,454 rows** of the current export, so you cannot use it to
select a curated subset; treat all pairs as automatically validated. 175 rows carry no DOI. Organism names
are Wikidata items, which can be genus-level, ambiguous, or synonymized; the metadata table's NCBI/GBIF/OTT
ids are the reliable handles. Because LOTUS derives from literature-mined upstreams (including the old
UNPD), extract-versus-constituent confusion and misattributed producers persist at some rate.

### 3. NPAtlas — The Natural Products Atlas

**1. What / who / version / size.** Curated database of **microbial** (bacterial and fungal) natural
products, Linington group at Simon Fraser University with an international curation team. Website version
3.0.2, **database version 2024_09**, verified live 2026-09-07 at <https://www.npatlas.org/> and
<https://www.npatlas.org/download>. The 3.0 paper (*NAR* 53:D691, 2024,
<https://doi.org/10.1093/nar/gkae1093>) reports **36,545 compounds**, 1,347 papers curated in that cycle
and 590 structure corrections incorporated. Note the database has not had a new release since 2024_09 as of
today — that is 24 months.

**2. Contribution.** The highest-quality microbial occurrence data available. Curation is human review on
top of an SVM-based literature triage, and the group explicitly states manual review remains essential. I
pulled a full record live (verified 2026-09-07, `https://www.npatlas.org/api/v1/compound/NPA000001`) — it
carries `origin_reference` with **both DOI and PMID** plus full citation, and `origin_organism` with genus,
species, and a `taxon` object containing **`ncbi_id`** and a complete ancestor ladder each with its own
`ncbi_id`, plus MycoBank external ids. Also `mol_structures` with per-version reference DOIs and
reassignment flags, `syntheses`, `reassignments`, `exclusions`, and `external_ids` (e.g. NP-MRD).

**3. Identifiers.** `npaid`, `inchikey` (Standard), `inchi`, `smiles`, `mol_formula`, exact mass, plus NCBI
taxid, MycoBank id, and cross-links to MIBiG, GNPS, NP-MRD and PubChem. Excellent joinability.

**4. Bulk access.** JSON, TSV, SDF, XLSX and graphML from <https://www.npatlas.org/download>; archived on
Zenodo, concept DOI `10.5281/zenodo.3530792`, version record 13756408 = `v2024_09` dated 2024-09-13, with
`np_atlas_2024_09.json` (478 MB), `.tsv` (33 MB), `.sdf` (181 MB), `.xlsx` (12.8 MB) and an
`np_atlas_excluded_2024_09.json`. Open REST API, no authentication needed (I called it anonymously).

**5. LICENCE — the blocker.** Verbatim from <https://www.npatlas.org/terms> (verified live 2026-09-07):

> "Data downloaded from the Natural Products Atlas is licensed under a Creative Commons
> Attribution-Noncommercial 4.0 International License."

The download page repeats it. The Zenodo record 13756408 carries licence id `cc-by-nc-4.0` (verified via
API). The 3.0 paper states the change verbatim: "future releases of the Natural Products Atlas (starting
with 2024_09) will be covered by a Creative Commons CC BY-NC 4.0 … license that precludes commercial use",
with commercial users directed to support@npatlas.org.

**Classification: NON_COMMERCIAL for 2024_09 and later. Releases through 2024_03 were CC BY 4.0** and are
therefore seedable if you can obtain them from the Zenodo concept series; verify the licence field on the
specific older version record before using it, since Zenodo licence tags are per-version. Confidence: high
for the current licence, medium for the exact older-version tagging (I did not enumerate every prior Zenodo
version record).

**6. Quality traps.** Comparatively few. The database explicitly models structure **reassignments** and
maintains an `excluded` file — if you ingest naively you will import retracted or superseded structures, so
honour `has_exclusions`, `reassignments` and the excluded JSON. Organism attribution is to the producing
strain as reported, which for endophyte and symbiont chemistry may be the isolation host rather than the
true biosynthetic producer.

### 4. NPASS — Natural Product Activity and Species Source

**1. What / who / version / size.** Maintained by the BIDD group (Chen Yu Zong, Tsinghua Shenzhen; Zeng
Xian, Fudan; contact Hanbo Lin). **Version 3.0, released 2025-06-15**, verified live 2026-09-07 at
<https://bidd.group/NPASS/>. Homepage counters: **204,023 natural products, 48,940 source organisms, 8,764
targets, 1,048,756 activity records, 208,415 composition records**.

**2. Contribution.** Uniquely combines species source with **quantitative bioactivity** against named
targets, plus composition/concentration values, symbiont/co-culture/engineered-organism source categories,
and predicted ADMET. Species-source and activity data are manually extracted from PubMed plus imported from
ChEMBL (v35 per the about page) and other databases including COCONUT, UNPD, StreptomeDB, TCM resources.
Chemical Checker bioactivity profiles and ADMETlab properties are **predicted**, and the 2023 update added
~66,600 compounds that have *only* estimated activity profiles — those must not be treated as measurements.

**3. Identifiers.** The about page (verified live) lists Standard InChI, InChIKey, canonical SMILES, MOL
files, **NCBI Taxonomy IDs for ~93% of species at genus level**, plus ChEMBL, UniProt and IUPHAR/BPS target
cross-references. Compound ids are `NPC…`.

**4. Bulk access.** Eleven flat files at <https://bidd.group/NPASS/downloadnpass.html>, labelled
**NPASS-2026**, verified live 2026-09-07: general information (~48 MB), structure with InChI/InChIKey/SMILES
(~65 MB), activity records with targets and references (~105 MB), **species source with NP–species pairs
and references (~110 MB)**, target information, species taxonomy (~7.2 MB), toxicity, and small files for
symbiont, elicitation, co-culture and engineered sources. No DOI, no dated archive, no versioned mirror —
the files are simply replaced.

**5. LICENCE — UNVERIFIED.** I fetched the homepage, the about page and the download page. **None of them
carries any licence, copyright, or terms-of-use statement**; the only legal link is a privacy policy. The
NAR papers are CC BY-NC (article licence, which governs the paper, not the database). The Bioregistry entry
<https://bioregistry.io/api/registry/npass> records `"license":"CC-BY-NC"`, but that is a third-party
assertion, not the maintainers'.

**Classification: UNVERIFIED, most likely NON_COMMERCIAL.** Not seedable. If NPASS matters to the project,
write to the maintainers for an explicit licence grant. Confidence: high that no licence is stated on site
(three pages checked); high that a third-party registry says CC-BY-NC.

**6. Quality traps.** Heavy database-of-databases inheritance (COCONUT, UNPD, TCM sources), so upstream
errors propagate and the same occurrence can appear from several routes. Species sources are genus-level
for a large fraction. The predicted-activity records outnumber measured ones in some slices and are not
always visually distinguished. TCM-derived "source" records frequently describe a multi-herb preparation or
a crude extract rather than a verified single-organism isolation.

### 5. SuperNatural 3.0

**1. What / who / version / size.** Preissner group, Charité Berlin. Published *NAR* 51:D654 (2023),
<https://doi.org/10.1093/nar/gkac1008>; **449,058 natural compounds and NP-based derivatives**.

**Status today: the site is gone.** The published URL host `bioinf-applied.charite.de` **fails to resolve**,
both from the local resolver and from Google Public DNS (`dig +short @8.8.8.8 bioinf-applied.charite.de`
returned nothing, verified 2026-09-07). `supernatural.charite.de` also does not resolve. I could not reach
the database, its FAQ, or its download link.

**2–4. Contribution / identifiers / bulk access.** From the paper (verified via PMC
<https://pmc.ncbi.nlm.nih.gov/articles/PMC9825600/>): SuperNatural ids, supplier ids, PubChem names, SMILES,
ChEMBL ids, UniProt ids, source organisms with a taxonomy link, and a whole-dataset CSV offered via the FAQ.
Mechanism of action, pathways, disease indications, taste properties and COVID-19 protease inhibition are
all **predicted**, as is toxicity class (ProTox-II). Much of the content is "NP-based derivatives", i.e.
semi-synthetic and vendor catalogue compounds, not natural products *sensu stricto*.

**5. LICENCE — UNVERIFIED.** No licence page could be fetched because the host is down. The only licence
text available is the *article* licence, verbatim from the paper: "This is an Open Access article distributed
under the terms of the Creative Commons Attribution-NonCommercial License … which permits non-commercial
re-use". That governs the paper, not the data. **Classification: UNVERIFIED / effectively unavailable.**
Not seedable. Confidence: high on unavailability today, high that no data licence was verifiable.

**6. Quality traps.** Vendor-catalogue derivatives mixed with genuine NPs; predicted mechanism and pathway
fields that look like assertions; no per-record occurrence references.

### 6. CMNPD — Comprehensive Marine Natural Products Database

**1. What / who / version / size.** Manually curated marine NP knowledge base from the State Key Laboratory
of Natural and Biomimetic Drugs, School of Pharmaceutical Sciences, Peking University. Live counters
verified 2026-09-07 at <https://docs.cmnpd.org/about>: **31,561 compounds, 3,354 source organisms at species
level, 2,652 targets, 72,349 bioactivity records, 128,488 documents**. Paper: Lyu et al., *NAR* 49:D509
(2021), <https://doi.org/10.1093/nar/gkaa763>. The docs site says "Last updated 6 years ago" — this
resource looks static.

**2. Contribution.** Marine chemistry with systematic organism taxonomy (kingdom→species), **sampling
location with geographic coordinates**, standardized bioactivity with binding constants, spectral
information, and literature/patent citations. Curation is manual from literature plus authoritative
databases.

**3. Identifiers.** SMILES, InChI, **InChIKey**, ClassyFire classification, and external links to ChEMBL and
PubChem (verified on the about page). NCBI taxids are not advertised as a stored field; taxonomy is
name-and-rank based.

**4. Bulk access.** Five files at <https://docs.cmnpd.org/downloads> (verified live 2026-09-07):
`CMNPD_1.0_2d.sdf.gz` (~11 MB), `CMNPD_1.0_3d.sdf.gz` (~39 MB), `CMNPD_1.0_calc_prop.tsv` (~14 MB),
`CMNPD_1.0_act_br.tsv` (~1 MB), `CMNPD_1.0_act_std.tsv` (~10 MB). Version 1.0 only; no DOI.

**5. LICENCE.** Verbatim from <https://docs.cmnpd.org/terms-and-conditions> (verified live 2026-09-07):

> "The CMNPD data is made available under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
> International license. Except as otherwise provided in any additional terms for a service, you may print
> or download content from the services for your own personal, non-commercial, informational or scholarly
> use."

**Classification: NON_COMMERCIAL and SHARE_ALIKE.** Doubly incompatible with a CC BY 4.0 release. Not
seedable. Confidence: high.

**6. Quality traps.** Marine invertebrate "producers" are frequently the collected holobiont, not the
biosynthetic organism (a well-known problem for sponge and tunicate metabolites, many of which are actually
microbial). Sampling location is per-collection, not per-occurrence. The dataset appears frozen at v1.0.

### 7. KNApSAcK

**1. What / who / version / size.** Species–metabolite relationship database, Nakamura, Asahi, Altaf-Ul-Amin,
Kurokawa and Kanaya, NAIST Comparative Genomics Laboratory. Verified live 2026-09-07 at
<http://www.knapsackfamily.com/knapsack_core/top.php>: **last update 2026/07/03, 63,735 metabolites,
159,606 metabolite–species pairs, 24,766 species.** Still actively updated, which is notable.

**2. Contribution.** Broad species–metabolite occurrence pairs, especially strong on plants and on
Japanese/Asian phytochemistry that is under-represented elsewhere. Curation is literature-based.

**3. Identifiers.** The search interface offers lookup by INCHI-KEY, INCHI-CODE, SMILES, CAS_ID, molecular
formula and internal C_ID (verified on the core page), so InChIKey is carried. No NCBI taxid; organisms are
names only.

**4. Bulk access — effectively none.** The only download offered on <http://www.knapsackfamily.com/KNApSAcK/>
is **Version 1.200.03, dated 2008/12/19** (zip/lzh/tar.gz). The 2026 data is web/CGI only, one record per
page. Any bulk use of current data means scraping, which the terms forbid.

**5. LICENCE — RESTRICTED.** Verbatim from the core system page (verified live 2026-09-07):

> "CAUTION: (C) Any content included in KNApSAcK database cannot be re-distributed or used for commercial
> purposes by any user without contacting with KNApSAcK DB group (skanaya[at]gtc.naist.jp)."

The page footer reads "All rights reserved. © 2007 NARA INSTITUTE of SCIENCE and TECHNOLOGY".

**Classification: RESTRICTED.** Explicitly prohibits redistribution. Not seedable. A negotiated grant is
conceivable — the notice invites contact — but that is a conversation, not a licence. Confidence: high.

**6. Quality traps.** Name-based organism records with no taxid; heavy plant bias; a large fraction of pairs
trace to older compendia rather than primary isolation reports.

### 8. NuBBE / NuBBEDB

**1. What / who / version / size.** Brazilian biodiversity NP database from the Nuclei of Bioassays,
Ecophysiology and Biosynthesis of Natural Products, UNESP. The 2017 update paper (*Sci Rep* 7:7215,
<https://doi.org/10.1038/s41598-017-07451-x>) reports **2,147 compounds**: 1,688 from plants, 325
semi-synthetic, 109 from microorganisms, 34 biotransformation products, 8 marine.

**Status today: unreachable.** `nubbe.iq.unesp.br` resolves (200.145.86.33) but every HTTP and HTTPS request
timed out after 30–45 s, on both `/portal/nubbe-search.html` and `/portal/nubbedb.html`, verified
2026-09-07. Secondary reporting suggests service disruption since late 2025.

**2–4.** Per the paper: compounds with chemical descriptors, species sources, geographic location, NMR
spectroscopic data and pharmacological properties; small enough to be a curation input rather than a bulk
seed. Identifiers and bulk-download mechanics could not be verified today. A knowledge-graph rendering
exists at <https://nubbekg.aksw.org/> (not fetched).

**5. LICENCE — UNVERIFIED.** No licence page could be reached. Classification: UNVERIFIED. Not seedable
without a live check. Confidence: high on unreachability, low on everything requiring the live site.

**6. Quality traps.** 15% of records are semi-synthetic derivatives, not natural products; small scale.

### 9. StreptomeDB 4.0

**1. What / who / version / size.** Streptomycete NP database from the Pharmaceutical Bioinformatics group
(PhaBiFr), University of Freiburg. **Version 4.0, 2025**; paper *NAR* 53:D724 (2025),
<https://doi.org/10.1093/nar/gkae1178>, verified via the OUP article page. Contents: **8,552 natural
products, 7,793 unique scaffolds, 3,888 producer strains, 7,630 curated PubMed articles**. Site verified
live 2026-09-07 at <https://streptomedb.vm.uni-freiburg.de/streptomedb/> (the old
`pharmbioinf.uni-freiburg.de/streptomedb` URL 301-redirects there).

**2. Contribution.** The deepest coverage of *Streptomyces* chemistry with **manually curated
compound–organism–reference links**, plus biosynthesis routes and activities. Everything protein-related is
**not** curated: 336,228 NP–protein relations are literature-mined by PubTator/BioBERT sentence
co-occurrence, and 398,717 NP–protein interactions are pharmacophore **predictions** (ePharmaLib). Predicted
NMR/MS spectra (8,551 / 8,520) and ADMET (8,287) are likewise computed.

**3. Identifiers.** Compounds are searchable by name and SMILES; the SDF download carries structures and
metadata. Whether Standard InChIKey and NCBI taxid are stored fields could not be confirmed from the site
or the paper text I retrieved — an SDF inspection would settle it.

**4. Bulk access.** One file: "All Compounds" SDF, 33.1 MB, at
<https://streptomedb.vm.uni-freiburg.de/streptomedb/download/> (verified live 2026-09-07). No DOI, no dated
versioning, no API advertised.

**5. LICENCE — UNVERIFIED.** Neither the home page nor the download page carries a licence or terms
statement; the download page footer says only "© Copyright PhaBiFr. All Rights Reserved 2024". The *NAR*
paper is CC BY 4.0, but that is the article licence: verbatim, "This is an Open Access article distributed
under the terms of the Creative Commons Attribution License … which permits unrestricted reuse, distribution,
and reproduction in any medium." **Classification: UNVERIFIED** ("All Rights Reserved" in the footer argues
against assuming openness). Not seedable without asking. The group is responsive and the underlying data is
academic-curated, so an explicit CC BY grant is a plausible ask. Confidence: high.

**6. Quality traps.** If you ingest the whole SDF you will mix ~8.5k curated compounds with hundreds of
thousands of mined and predicted protein relations — keep the provenance flags. Producer strains are strain-
level names that need resolution to NCBI taxids. Streptomycete literature has many synonym/renamed-species
issues.

### 10. CyanoMetDB

**1. What / who / version / size.** Manually curated database of cyanobacterial secondary metabolites, led
by Elisabeth Janssen at Eawag (Swiss Federal Institute of Aquatic Science and Technology) with an
international consortium. Original paper: Jones et al., *Water Research* 196:117017 (2021),
<https://doi.org/10.1016/j.watres.2021.117017>. **Version 03, released September 2024**, reported at
**3,085 metabolites** (medium confidence — see below).

Note: `cyanometdb.org` does **not** resolve (checked 2026-09-07); the project home is
<https://www.eawag.ch/en/department/uchem/projects/cyanometdb/>, which describes "2010 cyanobacterial
metabolites and 99 structurally related compounds" — that text appears to describe an earlier version.

**2. Contribution.** Manually curated from primary references, which is exactly the evidence model the KB
wants: metabolite, producer genus/organism, primary literature reference, SMILES, InChIKey, sample type,
and whether NMR was used. Small but high-quality; the reference resource for cyanobacterial toxins and
peptides.

**3. Identifiers.** SMILES and InChIKey (a dedicated InChIKeys file is distributed), producer organism names,
primary reference metadata. No NCBI taxid advertised.

**4. Bulk access.** Zenodo, concept DOI `10.5281/zenodo.4551528`; current version record **13854577**, tagged
`NORMAN-SLE-S75.0.3.0`, published **2024-09-28** (verified via the Zenodo API 2026-09-07). Files:
`CyanoMetDB_Version03.xlsx` (2.2 MB), `CyanoMetDB_V03_2024.csv` (3.7 MB), a MetFrag CSV, and
`CyanoMetDB_V03_2024_InChIKeys.txt`. Also distributed via the NORMAN Suspect List Exchange (S75), MetFrag,
NPAtlas and PubChem.

**5. LICENCE.** The Zenodo record carries licence id **`cc-by-4.0`** (verified live 2026-09-07 via
`https://zenodo.org/api/records/13854577`). The Eawag project page states no licence of its own.
**Classification: ATTRIBUTION (CC BY 4.0) — seedable.** Cite both Jones et al. 2021 and the Zenodo record,
as the record explicitly asks. Confidence: high on the licence tag.

**6. Quality traps.** Small scope by design (cyanobacteria only). Producer attribution is often to a
genus or a bloom sample rather than an axenic strain. Many congeners differ only in stereochemistry or a
single residue, so InChIKey-level deduplication against other sources will surface near-duplicates that are
genuinely distinct compounds.

### 11. NPBS Atlas (formerly NPBS database)

**1. What / who / version / size.** Natural Products and Biological Sources Atlas, BioChemAI Chemical Data
Center, **Shanghai Institute of Organic Chemistry, Chinese Academy of Sciences**. Paper: Xu et al.,
*J Cheminform* 17:172 (2025), <https://doi.org/10.1186/s13321-025-01116-y>. Live counters verified
2026-09-07 at <https://biochemai.cstspace.cn/npbs/>:

| Metric | Value |
|---|---|
| Known natural products | 218,941 |
| Botanical | 152,841 |
| Zoological | 20,267 |
| Fungal | 32,737 |
| Bacterial | 21,220 |
| Marine | 31,118 |

The predecessor NPBS (Zhang et al., *Database* 2020, <https://doi.org/10.1093/database/baaa102>) had
122,776 molecules, 33,377 biological sources and 898,294 relational records.

**2. Contribution.** Explicitly built for the compound→biological-source question, which is precisely this
KB's axis. Fields: identifiers, structures, names, bioactivities, biosynthetic pathways, chemical
classifications, calculated properties, references, and organism sources annotated with scientific
nomenclature, taxonomic classification, marine flag, **source part**, and traditional-Chinese-medicine
source. Built by "systematic text mining and expert manual curation" — the 2020 paper is candid that
text-mining (NPBSsys, NER-based) does the bulk and manual work supplements it.

**3. Identifiers.** InChIKey is the stated molecular key (2020 paper); structures as MDL molfiles; RDKit
properties. NCBI taxid support is not advertised; organism handling is nomenclatural.

**4. Bulk access.** Three downloads at <https://biochemai.cstspace.cn/npbs/downloads/> (verified live
2026-09-07): structures with biological-source annotations as tab-separated CSV, detailed biological-source
annotations as JSON, and bioactivity annotations as JSON. No DOI or dated versioning.

**5. LICENCE.** Verbatim from <https://biochemai.cstspace.cn/npbs/license/> (verified live 2026-09-07):

> "Access and use of this database are freely available under Open Source license of Creative Commons
> Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)."

and, in section 7, "All rights reserved by Chemical Data Center, Shanghai Institute of Organic Chemistry,
Chinese Academy of Sciences". The about page repeats: "Access and use of this database are limited to
non-commercial purposes". Note the *article* in *J Cheminform* is CC BY — a classic trap; the database is
not.

**Classification: NON_COMMERCIAL.** Not seedable. Confidence: high.

**6. Quality traps.** Text-mining provenance means occurrence pairs may lack a verifiable primary reference
and may reflect a review's summary rather than an isolation report. TCM source annotations often name a
drug/herb preparation, not a taxon. The terms explicitly forbid crawlers, so bulk use is limited to the
three published files.

### 12. UNPD — Universal Natural Products Database

**Status: defunct.** 229,358 molecules in its last published version. The host `pkuxxj.pku.edu.cn` still
resolves (222.29.45.252) but HTTP to `http://pkuxxj.pku.edu.cn/UNPD/` failed to connect (verified
2026-09-07). It has been reported unreachable since roughly 2017.

**Where the data survives.** As a COCONUT sub-collection, <https://coconut.naturalproducts.net/collections/CNPC0050>,
and as structures in the ISDB in-silico MS/MS resource (<https://github.com/oolonek/ISDB>, ~170,602 UNPD
structures with predicted spectra). LOTUS and NPASS also inherit UNPD-derived records.

**LICENCE: UNVERIFIED** — no licence page exists to fetch. Do not treat UNPD-derived records as open on the
strength of their host aggregator's licence; this is one of the specific reasons the COCONUT blanket-CC0
claim deserves scepticism. Quality traps: no stereochemistry discipline, name-only records, and occurrence
assertions without references — UNPD is a major source of the "text-mined pair with no citation" problem
downstream. Confidence: high on defunct status, high on survival routes.

### 13. Dictionary of Natural Products (CRC / Taylor & Francis)

**1. What / who / size.** The reference NP compendium, published by CRC Press / Taylor & Francis on the
CHEMnetBASE platform, <https://dnp.chemnetbase.com/>. Marketing pages state **over 340,000 natural
compounds**, twice-yearly updates, roughly 10,000 new entries a year (medium confidence: the authoritative
About page returned HTTP 403 to my fetches; the figure comes from Taylor & Francis librarian-resources and
Routledge pages, which are the publisher's own but are marketing copy).

**2–3. Contribution / identifiers.** I reached the search interface itself (verified live 2026-09-07 at
<https://dnp.chemnetbase.com/>, accessed via an institutional entitlement banner reading "Access Provided
by: University of California - Berkeley (CDL)"). Its searchable property list includes **Biological Source**,
Biological Use/Importance, CAS Registry Nos., Chemical Name, molecular formula, accurate mass, melting and
boiling point, and a CRC Number. So DNP does carry curated biological-source strings — but as text in a
proprietary record, not as taxids.

**4. Bulk access.** Two commercial routes only: a 12-month online subscription, or "ASCII/Oracle Files (Raw
data)" licensed separately, priced by user count.

**5. LICENCE: RESTRICTED.** No open licence exists. I could not fetch the platform's terms page (403), so I
am not quoting terms verbatim; the access model itself (per-seat subscription, separately licensed raw-data
product) settles the classification regardless. **Not seedable, and not usable as a curation crib either
without a data licence** — copying facts out of a subscription database into a CC BY release is exactly what
the raw-data licence is sold to control. Confidence: high on the classification, medium on the record count,
low on any specific contract wording.

**6. Quality traps.** Not applicable for our purposes; the blocker is legal, not technical.

### 14. MarinLit (Royal Society of Chemistry)

**1. What / who.** The marine natural products literature database, published by the RSC since 2014,
<https://marinlit.rsc.org/>. The landing page is a JavaScript shell and its FAQ blog gave no size figures,
so **I could not verify a compound or article count** — do not quote one.

**2–4.** Subscription-only, with dereplication-oriented search over the marine NP literature. No bulk export
is advertised; access is per-institution via subscriber login (<https://marinlit.rsc.org/marinlit/subscriberlogin>).

**5. LICENCE: RESTRICTED.** From the MarinLit FAQ, verbatim: "Your MarinLit licence terms are guaranteed for
the duration of the licence period that you've purchased." RSC's general terms state, verbatim (verified
live 2026-09-07 at <https://www.rsc.org/help-legal/legal/terms-conditions/>):

> "You may browse, download or print out one copy of the material displayed on Our Websites for your
> personal, non-commercial, non-public use, but you must retain all copyright and other proprietary notices
> contained on these materials."

and prohibit "to further copy, distribute or otherwise use any of the materials from Our Websites without
our written consent". **Not seedable.** Confidence: high on the terms, low on size figures (unverified).

### 15. AntiBase — now "Wiley Identifier of Natural Products" (Wiley)

**1. What / who / version / size.** The former AntiBase (Laatsch) natural-compound identifier, now sold by
Wiley as the **Wiley Identifier of Natural Products** (AntiBase Library + ChemWindow). The **2025 release**
was announced in March 2025 with **more than 105,000 compounds** (+9,500 over the 2024 edition's >95,000).
Product page: <https://sciencesolutions.wiley.com/solutions/technique/screening/wiley-identifier-of-natural-products/>.
Confidence: medium — these figures come from Wiley press releases and trade coverage, not a fetched product
datasheet.

**2–3.** Covers algae, animals, bacteria, dinoflagellates, fungi, lichens and plants; carries chemical
properties, bioactivity data, literature DOIs, cross-references to HMDB, ZINC, KEGG and ChEMBL, and
computed/measured spectra (IR, HRMS, MS, UV, ¹H NMR). Genuinely rich on the dereplication axis.

**4. Bulk access.** Commercial licence, delivered with Wiley's ChemWindow desktop software. No open dump.

**5. LICENCE: RESTRICTED.** Proprietary commercial product. Not seedable. Confidence: high.

### 16. ChEBI — Chemical Entities of Biological Interest

**1. What / who / version / size.** EMBL-EBI's manually curated ontology and database of small molecules.
**Release 255**, data-version date **2026-09-01**, loaded into OLS on 2026-09-07 (verified via
`https://www.ebi.ac.uk/ols4/api/ontologies/chebi` and the `chebi.obo` header). I downloaded
`chebi.obo.gz` (47 MB) from <https://ftp.ebi.ac.uk/pub/databases/chebi/ontology/> and counted **218,768
terms**; the About page says ">195,000 entries" (that number is stale). Confidence: high (measured).

**2. Contribution — classification scaffolding, not occurrence data.** ChEBI's value here is the curated
**role** hierarchy. Measured directly from release 255 (`relationship: RO:0000087` = has role):

| Role | Direct has-role assertions | Entities incl. species-specific sub-roles |
|---|---|---|
| metabolite (CHEBI:25212) | 5,333 | 16,362 (whole metabolite-role subtree, 60 role terms) |
| plant metabolite (CHEBI:76924) | 3,379 | 3,588 |
| bacterial metabolite (CHEBI:76969) | 1,016 | 1,964 |
| fungal metabolite (CHEBI:76946) | 495 | 1,794 |
| marine metabolite (CHEBI:76507) | 336 | 505 |
| algal metabolite (CHEBI:84735) | 143 | 143 |

Total `has role` assertions of all kinds in release 255: **59,112**. There are 47 role terms whose name ends
in "metabolite", including species-specific ones such as *Saccharomyces cerevisiae metabolite*, *Mycoplasma
genitalium metabolite* and *Jacobaea metabolite*.

**Does ChEBI carry producer-organism assertions?** Only obliquely, and this matters. There is **no
organism field and no taxid cross-reference**. Producer information is encoded (a) inside role term *names*
at whatever granularity a curator chose — kingdom-level ("plant metabolite"), genus-level ("Jacobaea
metabolite"), or species-level ("Saccharomyces cerevisiae metabolite") — and (b) as free text inside
definitions ("It is a bacterial metabolite found in *Streptomyces*…"). Extracting a structured
compound→taxon edge from ChEBI therefore requires parsing role labels against a taxonomy and mining
definition text. It is a *classification* source, not an occurrence source.

Note also `natural product fundamental parent` (CHEBI:35507) — a structural-parent class, not a
natural-product flag. There is no single clean "is a natural product" class to filter on.

**3. Identifiers.** ChEBI IDs are a first-class cross-reference target and ChEBI carries InChI, InChIKey,
SMILES and formula per structured entity — but **not in `chebi.obo`**: I found zero InChIKey property values
in the OBO, so take structures from the SDF, the flat files, or the PostgreSQL dump instead.

**4. Bulk access.** <https://ftp.ebi.ac.uk/pub/databases/chebi/> (verified live 2026-09-07): `SDF/`,
`flat_files/` (TSV mirroring the PostgreSQL schema), `generic_dumps/` (PostgreSQL), `ontology/` (FULL, CORE,
LITE OBO/OWL), `archive/` for past releases, `sss/`. Monthly numbered releases; the OBO carries
`data-version: 255`. Note `chebi_lite.obo` **omits relationships** — I confirmed it contains zero `has_role`
edges, so use the full OBO/OWL for role work.

**5. LICENCE.** Verbatim from <https://www.ebi.ac.uk/chebi/about> (verified live 2026-09-07):

> "All data in the ChEBI database is non-proprietary or is derived from a non-proprietary source. It is thus
> freely accessible and available to anyone. Each data item is fully traceable and explicitly referenced to
> the original source. The data on this website is available under the Creative Commons License (CC BY 4.0),
> and governed by EMBL-EBI's terms of use and Long-term data preservation policy."

**Classification: ATTRIBUTION (CC BY 4.0) — seedable.** Confidence: high.

**6. Quality traps.** The big one for this KB: **ChEBI is full of class terms, not just compounds.** Of
218,768 terms, a large fraction are structural or role classes with no structure at all, so an
InChIKey-keyed import must filter to entities that actually have a structure or you will create "records"
for abstract classes such as "azaphilone". Role assertions are curator-selected and non-exhaustive, so
absence of "plant metabolite" is not evidence of absence. Species-specific role labels encode taxon
granularity inconsistently. Definitions contain organism claims that look structured but are prose.

---

## Refuted or unverifiable claims

- **"COCONUT data is CC0."** Refuted as an unqualified claim. The download and About pages say CC0 without
  qualification, but the project's own README says every source carries its own licence and must be checked
  individually — and the data proves the README right. I counted the `collections` column across all
  738,827 rows: it contains 34,748 NPAtlas rows (CC BY-NC), 30,700 CMNPD rows (CC BY-NC-SA), 47,475
  KNApSAcK rows (redistribution prohibited) and 81,801 NPASS rows (no licence stated). Treat CC0 as the
  aggregator's intent, and filter by source collection.
- **"COCONUT gives you referenced compound–organism pairs."** Refuted. The `organisms` and `dois` columns
  are independent pipe-delimited lists on the compound row; they are not paired to each other. COCONUT
  cannot attribute a given occurrence to a given reference.
- **"NPAtlas is CC BY."** Refuted for current data. It was CC BY 4.0 through release 2024_03 and is
  **CC BY-NC 4.0 from 2024_09 onward**, stated on the site, in the Zenodo record metadata, and in the 3.0
  paper.
- **"LOTUS is CC0."** True via the Wikidata route. **Not** how the Zenodo frozen exports are tagged — record
  19360665 carries `cc-by-4.0`. Both work for a CC BY 4.0 release; the distinction matters if CC0
  cleanliness is a requirement.
- **"NPASS is CC-BY-NC."** Unverifiable from the source. Three NPASS pages carry no licence statement at
  all. The CC-BY-NC label comes from Bioregistry, a third party. NPASS is UNVERIFIED, not licensed.
- **"StreptomeDB is CC BY because the paper is CC BY."** Refuted as reasoning. The *NAR* article licence
  governs the article. The download page footer says "All Rights Reserved". Same error would apply to NPBS
  Atlas (CC BY article, CC BY-NC database) and SuperNatural (CC BY-NC article, no data licence).
- **"SuperNatural 3.0 is freely available at bioinf-applied.charite.de."** The published URL's host does not
  resolve in public DNS as of 2026-09-07. The resource is effectively unavailable.
- **"CyanoMetDB is at cyanometdb.org."** That domain does not resolve. Use the Eawag project page and the
  Zenodo concept DOI `10.5281/zenodo.4551528`.
- **LOTUS `manual_validation` flag.** The column exists in the current frozen export and is **empty in all
  674,454 rows**. Do not filter on it expecting a curated subset.

**URLs that failed to fetch, and why:**

| URL | Failure |
|---|---|
| `https://zenodo.org/records/5794106`, `.../13854577` (WebFetch) | TLS "unable to get issuer certificate"; worked via curl and the Zenodo REST API |
| `https://www.ebi.ac.uk/chebi/downloadsForward.do`, `aboutChebiForward.do`, `userManualForward.do` | TLS error / legacy endpoints; superseded by `/chebi/about` and the FTP site |
| `http://www.knapsackfamily.com/KNApSAcK/`, `https://nubbe.iq.unesp.br/...` (WebFetch) | TLS error; KNApSAcK worked via curl, NuBBE timed out on every route |
| `https://bioinf-applied.charite.de/supernatural_3/` | DNS does not resolve (local and 8.8.8.8) |
| `https://cyanometdb.org/` | DNS does not resolve |
| `http://pkuxxj.pku.edu.cn/UNPD/` | Host resolves, connection fails |
| `https://dnp.chemnetbase.com/help/About.xhtml`, Taylor & Francis librarian pages/PDF | HTTP 403 |
| `https://link.springer.com/article/10.1186/s13321-025-01116-y` | 303 to an IdP; used the live NPBS site instead |
| `https://pmc.ncbi.nlm.nih.gov/articles/PMC12625013/` | reCAPTCHA wall |
| `https://zenodo.org/records/13854577/files/CyanoMetDB_V03_2024.csv` | repeated HTTP 504 from Zenodo; metadata retrieved via API |
| `https://bidd.group/NPASS/download.php` | 404; correct path is `downloadnpass.html` |
| `https://coconut.naturalproducts.net/api/molecules` | `{"message":"Unauthenticated."}` — API needs a token |

## Open questions

1. **COCONUT SQL dump cross-references.** Resolved for the CSVs: the full CSV adds `organisms`,
   `collections`, `dois`, `synonyms`, `cas` and nothing else — no PubChem CID, ChEBI ID, Wikidata QID or
   NCBI taxid, and organism/DOI lists are unpaired. Whether the 31.91 GB SQL dump carries per-pair links and
   external cross-reference tables is still unknown and is the only reason to touch that dump.
2. **Per-collection licences inside COCONUT.** Partially answered: I have row counts for all 70 collections
   and licence findings for the ten largest, and at least ~200k rows come from NC/restricted/unstated
   sources. A full 70-collection licence audit is still needed before any COCONUT slice is called
   CC0-clean.
3. **NPAtlas pre-2024_09 Zenodo versions.** Confirm that specific older version records (e.g. 2024_03) are
   tagged `cc-by-4.0` on Zenodo before relying on them as a CC BY seed.
4. **StreptomeDB and NPASS licence grants.** Both are academically curated and neither states a data
   licence. A direct request for an explicit CC BY grant is cheap and would unlock the two best
   actinomycete and bioactivity-occurrence resources respectively.
5. **StreptomeDB SDF contents.** Does the 33 MB SDF carry Standard InChIKey and organism NCBI taxids per
   record? Requires downloading and parsing it.
6. **CyanoMetDB v3 exact entry count.** Zenodo file downloads returned 504 repeatedly; 3,085 metabolites is
   from secondary reporting, and the Eawag page quotes an older 2,010 + 99 figure. Verify by downloading
   `CyanoMetDB_Version03.xlsx` when Zenodo is healthy.
7. **NuBBE status.** Site unreachable today. Recheck, or use the NuBBE knowledge graph at
   <https://nubbekg.aksw.org/>, and find a licence statement either way.
8. **MarinLit size.** No verified compound/article count was obtainable; the site is a JS shell and the FAQ
   gives none.
9. **ChEBI organism mining.** Is it worth parsing species-specific role labels and definition prose into
   structured compound→taxon edges? 16,362 entities carry a metabolite role, but the taxon granularity is
   inconsistent and the yield of clean species-level edges is unknown.
