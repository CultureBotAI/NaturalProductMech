# NaturalProductMech

Knowledge base of **individual natural product structures** — one record per
chemical structure made by a living organism, carrying who makes it, from which
gene cluster, what it does, and the evidence for all three.

NaturalProductMech is the biosynthetic-origin counterpart of
[AntibioticMech](https://github.com/CultureBotAI/AntibioticMech) (antimicrobial
compounds and their mechanisms),
[TraitMech](https://github.com/CultureBotAI/TraitMech) (traits),
[CultureMech](https://github.com/CultureBotAI/CultureMech) (growth media),
[MediaIngredientMech](https://github.com/CultureBotAI/MediaIngredientMech)
(ingredients), [HabitatMech](https://github.com/CultureBotAI/HabitatMech)
(habitats), [CellStructureMech](https://github.com/CultureBotAI/CellStructureMech)
(cell structures), [ProteinTraitsMech](https://github.com/CultureBotAI/proteintraitsmech)
(proteins) and [CommunityMech](https://github.com/CultureBotAI/CommunityMech)
(communities), and follows the curation pattern established by
[dismech](https://github.com/monarch-initiative/dismech): one YAML per entity,
ontology-grounded, evidence-backed, schema-validated, curated incrementally.

## Status: planning

**2026-09-07.** This repository currently holds the plan, the data-source
research, the seeded source queue and the curation skills. There is no schema,
seeder or corpus yet.

| Document | What it is |
|---|---|
| [PLAN.md](PLAN.md) | Scope, schema design, the AntibioticMech join, milestones M0–M6 |
| [CLAUDE.md](CLAUDE.md) | Operational guidance for editing agents, written ahead of the code |
| [research/2026-09-07-natural-product-data-sources.md](research/2026-09-07-natural-product-data-sources.md) | The verified source landscape, with the three cluster reports beside it |
| [curation/source_queue.tsv](curation/source_queue.tsv) | 29 candidate sources, ranked, with licence status and the gap each closes |
| [.claude/skills/](.claude/skills) | Four curation workflows adapted from AntibioticMech |

## The gap it fills

AntibioticMech answers what a compound does to a microbe and how the microbe
resists it. It has nowhere to say who *makes* erythromycin, from which gene
cluster, by which pathway. TraitMech says an organism produces antibiotics;
ProteinTraitsMech says what a polyketide synthase domain is. None of them says
which structure a given *Streptomyces* strain makes, from which locus, with
what evidence.

| Section of a record | Question it answers |
|---|---|
| `producer_organisms` | Which taxon biosynthesizes it, and how do we know? |
| `occurrences` | Where has it been found, and in whose paper? |
| `biosynthetic_gene_clusters` | Which cluster, in which genome, at which coordinates? |
| `biosynthetic_pathway` | Which enzymes, in which order? |
| `bioactivities` / `molecular_targets` | What does it do, measured how? |
| `causal_graphs` | How is it made, and how does it act? Every edge cited. |

## The two distinctions the corpus is built on

**One record is one chemical structure**, keyed on a Standard InChIKey. A
compound class is not a record. Neither is an extract, a fraction, an essential
oil or a herbal preparation — activity measured on a mixture is not evidence
about any constituent of it.

**Occurrence is not production.** A compound isolated from a sponge may be made
by its bacterial symbiont; one "found in" a plant extract may come from a
fungal endophyte. So `producer_organisms` requires biosynthesis-grade evidence
— a gene cluster with experimental support, heterologous expression, isotope
feeding, or production by an axenic culture — while `occurrences` requires a
cited isolation or detection report. The seeder never promotes one to the
other. That distinction is why LOTUS's 674,454 structure–organism–reference
triples are occurrences, and why MIBiG's per-locus evidence vocabulary is what
grades a producer claim.

## Sources

The first release seeds from six sources whose licences were verified against
their own terms pages on 2026-09-07:

| Source | Licence | Contributes |
|---|---|---|
| [MIBiG 4.0](https://mibig.secondarymetabolites.org/) | CC BY 4.0 | producers with NCBI taxid, gene clusters, cluster class, references |
| [ChEBI](https://www.ebi.ac.uk/chebi/) | CC BY 4.0 | identity, structures, specialized-metabolite roles |
| [LOTUS](https://lotus.nprod.net/) via Wikidata | CC0 | referenced occurrences |
| [NPClassifier](https://github.com/mwang87/NP-Classifier) | CC0 | the filing classification, computed from structure |
| [PubChem](https://pubchem.ncbi.nlm.nih.gov/) | public domain | structures the others lack |
| [CyanoMetDB](https://www.eawag.ch/en/department/uchem/projects/cyanometdb/) | CC BY 4.0 | curated cyanobacterial metabolites |

Excellent resources that **cannot** be seeded into a CC BY 4.0 corpus, and why:
NPAtlas (CC BY-NC from release 2024_09), Norine (CC BY-NC-SA), NP-MRD
(CC BY-NC), CMNPD (CC BY-NC-SA), NPBS Atlas (CC BY-NC), KNApSAcK
(redistribution prohibited), ChEMBL (share-alike), ClassyFire/ChemOnt (bespoke
terms), MetaCyc (subscription), KEGG (not a public database). NPASS and
StreptomeDB state no licence at all, which is not the same as permission.
COCONUT advertises CC0 over a collection that demonstrably contains rows from
all four of the restricted sources above.

The full reasoning, with licence text quoted from each primary page, is in the
[research report](research/2026-09-07-natural-product-data-sources.md).

## Licence

Two licences, because the repository will hold two different things.

**Code, schema, tests, configuration, documentation and curation decisions:
[CC0 1.0](LICENSE).** This repository's own work, dedicated to the public
domain.

**Record content, once it exists: [CC BY 4.0](LICENSE-DATA).** It will derive
from CC BY sources whose attribution cannot be stripped, so the corpus is
redistributable — freely, commercially, modified — provided the attribution
rides along. Attribution will be per-record and machine-readable through each
record's `source_concepts` block.
