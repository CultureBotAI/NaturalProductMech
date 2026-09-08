# NaturalProductMech — plan

Written 2026-09-07. This is the plan for a new Mech knowledge base of
**natural products**: individual chemical structures made by living organisms,
each record carrying who makes it, how it is made, what it does, and the
evidence for all three. It follows the pattern of
[AntibioticMech](../AntibioticMech) (one YAML per structure, harmonized from
committed inventories, closed-schema validated, reproducible, curated
incrementally) and joins the CultureBotAI Mech fleet governed by
[culturebotai-claw](https://github.com/CultureBotAI/culturebotai-claw).

Companion documents written the same day:

- `research/2026-09-07-natural-product-data-sources.md` — the verified
  data-source landscape, including NP-KG (Taneja et al.). Evidence for a
  curator, never automatic input.
- `curation/source_queue.tsv` — the ranked source queue seeded from that
  report. Nothing is `ADOPTED` yet; adoption is a pull request per source.
- `.claude/skills/` — the four AntibioticMech skills adapted to this corpus.
- `CLAUDE.md` — operational guidance for editing agents, written ahead of the
  code so the scaffold is built to it rather than documented after.

## 1. Why a separate repository

AntibioticMech answers "what does this compound do to a microbe and how does
the microbe resist it". It has nowhere to say who *makes* erythromycin, from
which gene cluster, by which pathway, and what else the compound does when it
is not killing bacteria.

Measured against its committed corpus on 2026-09-07, not assumed:

| AntibioticMech, 2,909 records | Count |
|---|---:|
| Unique Standard InChIKeys | 2,893 |
| Records carrying `biosynthesis_origin` | 3 |
| Records carrying `producer_organisms` | 6 |

So the origin question is not merely under-answered there, it is unasked: the
field exists and is empty on 99.9% of the corpus. MIBiG was adopted in August
2026 and its committed inventory holds 43 rows from 24 entries, because the
extractor gates on a non-placeholder reviewer id — a gate this research showed
matches 25 of MIBiG's 3,013 entries. The join is real and the corpus was not
built for it.

TraitMech says an organism *produces antibiotics*; ProteinTraitsMech says what
a polyketide synthase domain is; CellStructureMech says what a flagellum is
made of. None says which structure a given *Streptomyces* strain makes, from
which locus, with what evidence. That compound-centred origin layer is the gap.

The fleet's rule is one repository per entity type with a stable identity
model. A natural product record is keyed on the same thing as an antibiotic
record — a Standard InChIKey — so the two corpora will overlap on identity and
must **join, not duplicate**. Section 4 says how.

## 2. Scope

### 2.1 The unit of the corpus

One `NaturalProductRecord` is one chemical structure with a Standard InChIKey.
Inherited unchanged from AntibioticMech, including its consequences:

- A compound class ("macrolide", "indole alkaloid") is never a record. It is a
  `structural_class` / `bgc_class` on the records it covers.
- An extract, fraction, essential oil, herbal preparation or "crude
  supernatant" is never a record. Activity measured on a mixture is not
  evidence about any single constituent.
- Salts, stereoisomers, glycosylated congeners and semisynthetic derivatives
  are different records. Congener families (erythromycin A/B/C) are related
  through `parent_compounds` and `congener_of`, not merged.
- No InChIKey, no record. A name-only source concept goes to the worklist.

### 2.2 What makes something a natural product here

Membership is **asserted by an adopted source, never inferred from a
structure**. A compound enters the corpus when at least one seedable source
asserts one of:

1. an **experimentally supported biosynthetic origin** — a MIBiG entry links
   the structure to a characterized gene cluster in a named organism;
2. an **occurrence in a taxon with a citation** — a LOTUS
   structure–organism–reference triple, or an equivalent curated pair;
3. a **ChEBI specialized-metabolite role** from an explicit, committed allow
   list (`conf/np_roles.tsv`): mycotoxin, phytotoxin, siderophore, quorum
   sensing signal, bacterial/fungal/plant pigment, antibiotic-of-natural-origin
   and so on. ChEBI's bare `metabolite` roles are **not** in that list: glucose
   and ATP are bacterial metabolites and are not what this corpus is for.

NP-likeness scores, natural-product flags computed from structure, and
"looks like a polyketide" are classification signals, recorded as computed and
marked as such. They never admit a record.

### 2.3 Producer versus occurrence — the distinction this corpus exists to keep

The fleet already bit on this in AntibioticMech's source queue: an occurrence
in a taxon is not proof of biosynthesis. A compound isolated from a sponge may
be made by its bacterial symbiont; a compound "found in" a plant extract may be
a contaminant, a degradation product or a fungal endophyte's. So the schema has
two fields with two evidence standards:

| Field | Claim | Minimum evidence |
|---|---|---|
| `producer_organisms` | This taxon biosynthesizes the compound | A gene cluster with experimental support, heterologous expression, isotope feeding, or a primary paper stating production by an axenic culture |
| `occurrences` | This compound was detected in / isolated from this taxon | A cited isolation or detection report (LOTUS supplies these) |

A LOTUS row lands in `occurrences`. It moves to `producer_organisms` only when
a curator or a producer-grade source supports it. The seeder never promotes.

MIBiG makes the producer grade machine-readable, which is why it anchors the
corpus: each locus carries `evidence[].method` from a controlled vocabulary.
The 4.0 release's distribution across entries is knockout studies 542,
heterologous expression 638, enzymatic assays 284, expression correlated with
production 219, genomic–metabolomic correlation 82, in-vitro expression 25, and
homology-based prediction 31. Everything but the last is producer-grade;
`Homology-based prediction` is not, and lands in the worklist. That mapping
lives in `conf/producer_evidence.tsv` so it can be argued with rather than
buried in the extractor.

### 2.4 Phased scope, by producer kingdom

The full natural-product universe is far beyond what a one-YAML-per-record
corpus with a rendered site can carry, and beyond what KG-Microbe needs. The
research report measured the candidates rather than quoting them: COCONUT's
September 2026 release holds 738,827 rows over 728,421 unique InChIKeys, and
the current LOTUS export holds 674,454 structure–organism–reference triples
over 227,319 unique InChIKeys. Scope is therefore phased by producer, in the
order that serves the fleet:

| Phase | Producers | Seed sources | Expected size |
|---|---|---|---|
| **A** | Bacteria, archaea, fungi, microalgae and cyanobacteria — the KG-Microbe organisms | MIBiG 4.0, LOTUS microbial-taxon subset, ChEBI role allow-list, CyanoMetDB | thousands, not hundreds of thousands |
| **B** | Marine invertebrates and their symbionts (where the microbial origin is asserted) | LOTUS subset, MIBiG | to be measured after A |
| **C** | Plants and other eukaryotes | LOTUS | decision deferred; may stay a separate corpus |

MIBiG 4.0 sets the floor for Phase A: 3,013 entries in the release dump, every
one carrying an NCBI taxid, holding 5,443 compound records of which 4,401 have
a structure. That is the anchor. LOTUS then adds occurrences to those records
and admits others through its microbial-taxon subset.

Phase A is the repository's first release. Phases B and C are decisions, not
promises, and will be made against `just report` numbers after A ships. The
taxon filter is a committed configuration (`conf/sources.yaml` → `producer_scope`)
so widening it is a diff, not a rewrite.

### 2.5 Explicitly out of scope

- Synthetic compounds and semisynthetic derivatives without a natural parent
  in the corpus (they may appear as `xrefs` or `derivatives` on the parent).
- Primary metabolites admitted only by a `metabolite` role.
- Antimicrobial *mechanism* content — molecular targets of antibacterial action,
  resistance determinants, MIC spectra. That lives in AntibioticMech, and a
  NaturalProductMech record points at it (section 4).
- Pharmacokinetic natural product–drug interactions (NP-KG's subject). See
  the research report for what NP-KG can lend this corpus instead.

## 3. Schema

`src/naturalproductmech/schema/naturalproductmech.yaml`, LinkML, closed
validation, with `mech_shared.yaml` and `history.yaml` vendored byte-identical
from claw. The design copies AntibioticMech's shape and changes what the domain
requires.

### 3.1 `NaturalProductRecord` (root, one per file)

Carried over unchanged from `AntibioticRecord`: `identifier`, `label`,
`definition`, `definition_source`, `synonyms`, `parent_compounds`, `xrefs`,
`chemical_structure`, `source_concepts`, `grounding_status`, `grounding_notes`,
`evidence`, `causal_graphs`, `curation_status`, `curation_history`,
`discussions`, `datasets`, `molecular_targets`, `structural_observations`,
`clinical_status`, `clinical_status_assertions`.

Replaced:

| AntibioticMech | NaturalProductMech | Why |
|---|---|---|
| `antimicrobial_class` (filing) | `np_pathway` (filing) — NPClassifier's seven pathways: `ALKALOIDS`, `AMINO_ACIDS_AND_PEPTIDES`, `CARBOHYDRATES`, `FATTY_ACIDS`, `POLYKETIDES`, `SHIKIMATES_AND_PHENYLPROPANOIDS`, `TERPENOIDS`, plus `UNCLASSIFIED` | Directory and report row. Chosen because it is computable from the structure alone, so **every** record can be filed — most records have no gene cluster. NPClassifier's ontology, models and data are CC0. Computed, and the record says so with model version. |
| — | `bgc_class` (multivalued) — MIBiG 4.0's cluster vocabulary: `PKS`, `NRPS`, `RIBOSOMAL`, `TERPENE`, `SACCHARIDE`, `OTHER`, with `bgc_subclass` free text | The class of the *gene cluster* is a different claim from the class of the *molecule*, and MIBiG 4.0 separated them deliberately — it removed `alkaloid` as a biosynthetic class for exactly this reason. Asserted, only where a BGC exists. |
| `activity_roles` | `ecological_roles` (ChEBI roles: siderophore, toxin, pigment, signal…) + `compound_classes` (every asserted molecule-level class, e.g. MIBiG's Dewick-based ontology, unreduced) | Filing is one decision; the evidence stays |
| `structural_class` | `structural_class` (kept) + `npclassifier_superclass` / `npclassifier_class` (computed, versioned) | Structure and biosynthesis are different axes. ChemOnt/ClassyFire terms are **not** carried: ClassyFire's terms restrict commercial redistribution, so a ChemOnt string arriving inside an otherwise-CC BY record is dropped. |
| `mode_of_action` (antimicrobial enum) | `bioactivity_summary` (multivalued `BioactivityClassEnum`: ANTIBACTERIAL, ANTIFUNGAL, CYTOTOXIC, ANTIVIRAL, ANTIPARASITIC, ENZYME_INHIBITOR, SIGNALLING, TOXIN, IMMUNOMODULATOR, …) | A natural product's activities are plural; each summary value must be backed by at least one `bioactivities` item or a source assertion |
| `activity_spectrum` (MIC observations) | `bioactivities` (`BioactivityObservation`: target organism / cell line / enzyme, assay, value, units, qualifier, evidence) | Generalised beyond MIC; the "an MIC without units is not a measurement" rule generalises to every value |
| `resistance_mechanisms` | dropped (AntibioticMech owns it) | Section 4 |
| `producer_organisms` (MIBiG slice) | `producer_organisms` (first-class, with `evidence_basis`: BGC_CHARACTERIZED / HETEROLOGOUS_EXPRESSION / ISOTOPE_FEEDING / AXENIC_CULTURE / SOURCE_ASSERTION) + `occurrences` | Section 2.3 |
| — | `biosynthetic_gene_clusters` (`BiosyntheticGeneCluster`: MIBiG accession + version, organism, genome accession, locus coordinates, biosynthetic class, `reviewed`, evidence) | The origin layer this corpus exists for |
| — | `biosynthetic_pathway` (`PathwayStep` list: enzyme (UniProt / EC / Rhea), substrate, product, evidence) — optional, curated | Feeds biosynthesis causal graphs |
| — | `congener_of` / `derivatives` | Family relations without merging |
| — | `related_records` (`CrossCorpusLink`: corpus, identifier, relation, basis=InChIKey) | Section 4 |
| `biosynthesis_origin` | kept, but a record here is `NATURAL_PRODUCT` by construction; the field exists for `SEMISYNTHETIC` parents that are admitted as derivatives | |

### 3.2 Evidence rules

Same as AntibioticMech and stated in `docs/CURATION.md`:

- Identity, structure and classification inherit provenance from the source
  concept; record-level `evidence` is optional.
- Every `ProducerOrganism`, `Occurrence`, `BiosyntheticGeneCluster`,
  `BioactivityObservation`, `MolecularTarget`, `PathwayStep` and `CausalEdge`
  requires its own `EvidenceItem`.
- A database assertion is cited as a database assertion (`source: MIBIG`,
  `reference: MIBIG:BGC0000055`), never dressed as a paper.
- A value without units and method is not an observation.
- Computed classification carries the tool name and version in its provenance
  and is never presented as asserted.

### 3.3 Causal graphs

`CausalGraph` from the shared shape, with two `scope` values this corpus adds:
`BIOSYNTHESIS` (precursor → enzyme steps → product, with BGC genes as nodes)
and `BIOACTIVITY` (compound → target engagement → cellular effect). AntibioticMech's
antimicrobial mode-of-action graphs are not duplicated; a `related_records`
link points at them.

## 4. Joining AntibioticMech and the rest of the fleet

The join key is the Standard InChIKey, the same key both corpora already
refuse to write a record without. Rules:

1. **No mechanism duplication.** If a structure has an AntibioticMech record,
   this corpus does not seed `molecular_targets`, `mode_of_action` or MIC data
   for its antimicrobial activity. It records `related_records:
   [{corpus: AntibioticMech, identifier: CHEBI:42355, relation: SAME_STRUCTURE}]`
   and a `bioactivity_summary` value of `ANTIBACTERIAL` backed by that link.
2. **Producer content flows one way.** NaturalProductMech is the authority on
   `producer_organisms` and BGCs. AntibioticMech's MIBiG slice stays as it is
   today; once this corpus is stable, AntibioticMech may read this corpus's
   inventory instead of MIBiG directly — a decision for that repository.
3. **The cross-link is computed, not curated.** A committed inventory
   `data/raw/antibioticmech_inchikeys.tsv` (InChIKey → identifier → slug,
   pinned to an AntibioticMech commit) drives the link; `just verify-corpus`
   reproduces it. Drift means one corpus moved and the pin needs advancing,
   which is a visible PR, not a silent divergence.
4. **Other siblings**, later and by the same mechanism: TraitMech traits
   (`produces <class>`), HabitatMech (producer isolation environment via
   BacDive strain data), CultureMech (media in which production was observed),
   ProteinTraitsMech (PKS/NRPS domain records for pathway enzymes). Each is a
   `CrossCorpusLink` with a pinned inventory, none is in the first release.
5. **KG-Microbe** ingests no natural-product structure source today — no
   MIBiG, no NPAtlas, no LOTUS in its current `download.yaml`, measured
   2026-09-07. It consumes the corpus through a KGX export (`kgx_export`
   capability in claw's fleet manifest) — `Chemical → produced_by → Taxon`,
   `Chemical → has_bgc → Gene cluster`, with Biolink predicates chosen when the
   export is designed. Not in the first release, but the schema keeps the taxon
   ids as NCBITaxon CURIEs so the export is a projection, not a mapping.

## 5. Sources — the first release and the queue

The full landscape, licence verification and quality traps are in the research
report; the ranked queue is `curation/source_queue.tsv`. The licence gate is
the same as AntibioticMech's and for the same reason: record content is CC BY
4.0, so CC0 and CC BY sources seed, CC BY-SA and NonCommercial and bespoke
terms are curate-only or reference, and an unverified licence blocks adoption.

**First release (Phase A) seeds from:**

| Source | Contributes | Licence (verified 2026-09-07) | Gate before adoption |
|---|---|---|---|
| MIBiG 4.0 | structures (SMILES), producers with NCBI taxid, BGCs with GenBank loci and an evidence vocabulary, cluster class, references | CC BY 4.0, stated in the paper's data-availability section and the site footer | filter `status` to active; generate InChIKeys locally; map `loci[].evidence[].method` to producer grade |
| ChEBI (3-star) | identity, structures, definitions, synonyms, specialized-metabolite roles | CC BY 4.0 | role allow-list committed and reviewed |
| LOTUS (via Wikidata) | occurrences with reference DOI, structures, Wikidata QIDs, NCBI/GBIF/OTT taxon ids, PubChem CIDs | CC0 on the Wikidata route (main-namespace structured data); the Zenodo frozen export is tagged CC BY 4.0 instead | microbial-taxon filter; occurrences only, never producers |
| PubChem | structures for concepts ChEBI does not cover | public domain, per-source conditions respected | same canary discipline as AntibioticMech |
| NPClassifier | computed pathway/superclass/class, and the filing decision | CC0 for ontology, models and data (code MIT) | run locally with a pinned model version; stored as computed |
| CyanoMetDB v3 | manually curated cyanobacterial metabolites with producer and primary reference | CC BY 4.0 on the Zenodo record | small, high quality; cite the record as it asks |
| AntibioticMech (pinned) | cross-corpus links | CC BY 4.0 (fleet) | pin a commit |

NP-KG, the resource this plan was asked to evaluate, is **not** among them,
and the reason is not licence but content: it carries no chemical structures at
all. Its natural-product layer is 613 named phytoconstituents, 153 of which
have no chemical parent beyond "chemical entity", and no InChIKey, SMILES or
PubChem identifier appears anywhere in it. It is a curator reference for
plant–constituent–enzyme pharmacokinetic mechanism, filtered by edge
provenance, and its merged upstreams make it restricted for redistribution
regardless. See the research report §6.

**Bioactivity and targets (M5), settled by the same research.** Measured
activity is the worst-licensed layer in this domain: ChEMBL, DrugCentral and
the Guide to PHARMACOLOGY are share-alike; DrugBank, IMPPAT, FooDB and
Phenol-Explorer are non-commercial; NPASS, the Therapeutic Target Database,
SymMap and HERB state no licence; CO-ADD reserves all rights while branding
itself open-access. Two sources can seed:

- **BindingDB's own-curated subset**, CC BY 3.0 and separable from its
  ChEMBL-derived rows by the `Curation/DataSource` column — 93,712 rows over
  46,304 InChIKeys, with UniProt per target chain and pH and temperature per
  measurement. Filter on the column, not the filename: 429 of those rows are
  ChEMBL's and are share-alike.
- **PubChem BioAssay**, public domain but a deposition archive, so the seeded
  row records its depositor and primary single-concentration hits are never
  written as potencies.

One result from that cluster is direct evidence for §2.2's rule. ChEMBL's
`natural_product` flag marks prazosin — a wholly synthetic quinazoline — as a
natural product, while its own NP-likeness score disagrees. The flag was
rebuilt at release 33 from COCONUT mappings. A computed or flag-based
natural-product signal never admits a record.

**Queued behind licence or identity gates:** COCONUT (its download page claims
CC0 "without any restrictions" while its own README says every source keeps its
licence — and the collections column proves the README right, so adoption means
filtering to verified-open collections, not trusting the banner), NPAtlas
(CC BY-NC from release 2024_09; only releases through 2024_03 were CC BY),
NPASS (no licence stated anywhere), ChEMBL (share-alike), BindingDB curated
subset, PubChem BioAssay, GNPS libraries (native contributions CC0), MoNA and
MassBank (CC BY, per-record), Paired Omics Data Platform (CC BY, but only 117
BGC-to-spectrum links), BiG-FAM (CC BY, frozen on 2020 data), antiSMASH-DB (no
data licence published, and no compound assignment anyway), Rhea (CC BY, for
pathway steps), NP-KG.

**Refused for seeding, kept as reference:** Norine (CC BY-NC-SA), NP-MRD
(CC BY-NC), CMNPD (CC BY-NC-SA), NPBS Atlas (CC BY-NC), KNApSAcK (redistribution
explicitly prohibited), ClassyFire/ChemOnt (bespoke terms), MetaCyc/BioCyc
(subscription), KEGG (not a public database), Dictionary of Natural Products,
MarinLit, AntiBase, NAPRALERT.

**A rule the report earned the hard way:** an open-access *article* licence is
not a database licence. StreptomeDB, NPBS Atlas and SuperNatural all publish
CC BY or CC BY-NC papers over data that is differently licensed or unlicensed.
`verified_on` in the queue means the database's own terms page was read.

## 6. Repository layout

Identical to AntibioticMech's, renamed. The point of copying the layout is
that the fleet's tools (claw governance, skills, site contract, source queue
checker) already know it.

```
NaturalProductMech/
  CLAUDE.md  README.md  PLAN.md → NEXT_TASKS.md once scaffolded
  ATTRIBUTION.md  CITATION.cff  LICENSE (CC0)  LICENSE-DATA (CC BY 4.0)
  justfile  pyproject.toml  uv.lock
  conf/sources.yaml            # sources, producer_scope taxon filter, class priority
  conf/np_roles.tsv            # ChEBI roles that admit a compound (allow list)
  curation/decisions.tsv       # GROUND / EXCLUDE / KEEP_MINTED per source concept
  curation/source_queue.tsv    # ranked candidate sources
  data/raw/                    # committed inventories + MANIFEST.yaml (sha256, versions)
  data/natural_products/<np_pathway>/<slug>.yaml
  data/natural_products/PATHS.tsv  RETIRED.tsv
  src/naturalproductmech/{schema,curate,validation,templates}/
  scripts/  tests/  pages/  research/  docs/{HARMONIZATION,CURATION}.md
  .claude/skills/{add-natural-product,curate-yaml-record,source-queue,review-open-issues}
  .github/workflows/{main,vendored-sync}.yaml
```

Identity minting: `naturalproductmech:<source>-<10-hex>` hashed from
`(source, source_id)`, never from a label. ChEBI grounds to its own CURIE.
Merge on InChIKey with AntibioticMech's two exceptions (ChEBI-internal
collisions stay separate; two minted concepts sharing a structure are flagged,
not merged).

## 7. Milestones

Each milestone is one or more PRs on a branch, reviewed adversarially, with
findings filed as issues, per the standing git workflow. Nothing merges without
the owner's go-ahead.

**M0 — Plan, research, skills (this PR).** `PLAN.md`, the research report,
the seeded source queue, the four skills, `CLAUDE.md`. No code.

**M1 — Scaffold.** Copy AntibioticMech at its current commit, rename package
and prefixes, strip antimicrobial-specific code paths (ARO extractor,
resistance, target roles, FDA, BindingDB, PHI-base, CRyPTIC evaluators) and
their tests, keep the ChEBI extractor, PubChem enrichment, MIBiG extractor,
seeder skeleton, validation, curation event, site renderer, QC runner,
provenance and source-queue checkers, chemical-map. Write the schema per
section 3. `just qc` green on an empty corpus. Vendor claw's governed files
at the current pin *without* a consumer entry yet (the checker will fail on
identity until M4 — record that as the expected red gate, or run it in
`--offline` mode until admission).

**M2 — ChEBI + MIBiG seed (Phase A core).** `conf/np_roles.tsv` reviewed;
ChEBI inventory limited to 3-star compounds bearing an allow-listed role or
matched by MIBiG; MIBiG extractor emitting compounds, producers, BGCs, class.
Canary one record (`just seed-canary CHEBI:42355` — erythromycin A, so the
AntibioticMech join is exercised on day one), then `just seed-apply`. Site
rendered. README statistics block generated. First adversarial review pass.

**M3 — LOTUS occurrences.** Wikidata SPARQL or the LOTUS bulk dump, filtered
to microbial taxa, exact InChIKey join, `occurrences` populated with the
LOTUS reference. Measure incremental coverage against M2 before deciding
whether to widen the taxon filter.

**M4 — Fleet admission.** Three PRs in the order claw requires: (1) claw
declares `naturalproductmech` in `fleet.yaml` and the vendored-consumer
registry, with every capability's status and reason; (2) this repository pins
that ref and passes `vendored-sync`; (3) claw removes the incomplete-consumer
ledger entry. The AntibioticMech admission (claw #309) and HabitatMech
admission (claw #360) are the templates.

**M5 — Bioactivity and targets.** BindingDB curated subset and PubChem
BioAssay for measured activities and targets on records that have them;
`bioactivity_summary` derived only from backed items. ChEMBL stays curate-only.

**M6 — Curation.** Biosynthesis causal graphs for the best-evidenced MIBiG
records first (`just worklist --queue biosynthesis` ranks by BGC evidence
waiting), then bioactivity graphs. This is the work; everything above is the
scaffold for it.

## 8. Risks and decisions already taken

- **Corpus size.** Phase A stays in the low thousands by construction. A
  size budget goes in `conf/sources.yaml` and `just seed` refuses to exceed it
  without an explicit flag, so widening scope is a recorded decision.
- **The InChIKey's known failures** (tautomers, organometallic cis/trans,
  relative stereochemistry) bite hardest on exactly this chemistry —
  macrocycles, glycosides, peptides. Same policy as AntibioticMech: a collision
  is not proof of sameness, a non-collision is not proof of difference, and
  `stereo_complete` is recorded so undefined stereocentres are visible.
- **Occurrence ≠ production.** Two fields, two evidence bars, seeder never
  promotes. Non-negotiable.
- **Computed ≠ asserted.** NPClassifier and NP-likeness are recorded with tool
  and version, never as source assertions, and never admit a record.
- **Licence aggregation.** COCONUT and NP-KG both relabel upstream content; a
  dataset-level licence claim does not override the upstream terms of the rows
  in it. Per-source provenance is kept so restricted rows can be excluded.
- **Overlap with AntibioticMech** is a join, not a fork. The pinned InChIKey
  inventory makes the overlap reproducible and drift visible.
- **Name.** `NaturalProductMech`, package `naturalproductmech`, prefix
  `naturalproductmech:`. No collision in the CultureBotAI organisation as of
  today (checked `NaturalProductMech`, `NaturalProductsMech`, `NPMech`).
