# Attribution

Record content in this repository will be licensed [CC BY 4.0](LICENSE-DATA)
and derived from the sources below. If you redistribute it, in whole or in
part, carry this attribution with it.

**No records exist yet.** This file is written ahead of the corpus so that the
attribution obligation is settled before the first row is seeded, and so that
adopting a source means adding its paragraph here in the same pull request.

## Required attribution

> NaturalProductMech (CultureBotAI), CC BY 4.0. Derived from MIBiG (CC BY 4.0),
> ChEBI (EMBL-EBI, CC BY 4.0), the LOTUS Initiative via Wikidata (CC0),
> NPClassifier (CC0), CyanoMetDB (CC BY 4.0), and chemical structures from
> PubChem (NCBI).

## Per-record provenance

Attribution is machine-readable, not only a notice. Every record carries a
`source_concepts` block naming each upstream concept that resolved to it, with
that source's own identifier and label, so a consumer taking a subset can
derive precisely which upstream resources that subset depends on.
`data/raw/MANIFEST.yaml` records what was retrieved, from which route, and when
— the route matters, because LOTUS is CC0 through Wikidata and CC BY 4.0
through its Zenodo export.

## Sources

**MIBiG** — the Minimum Information about a Biosynthetic Gene cluster
repository, maintained by the Medema and Weber groups and a community of
contributors. CC BY 4.0. Supplies producer organisms with NCBI taxonomy
identifiers, gene clusters with GenBank loci and experimental evidence,
biosynthetic classes, compound structures and primary references.
<https://mibig.secondarymetabolites.org/>

Zdouc MM, Blin K, Louwen NLL, et al. MIBiG 4.0: advancing biosynthetic gene
cluster curation through global collaboration. *Nucleic Acids Res.*
2025;53(D1):D678-D690. doi:10.1093/nar/gkae1115

**ChEBI** — Chemical Entities of Biological Interest, EMBL-EBI. CC BY 4.0.
Supplies identity, structures, definitions, synonyms, cross-references and the
specialized-metabolite role hierarchy. <https://www.ebi.ac.uk/chebi/>

Hastings J, Owen G, Dekker A, et al. ChEBI in 2016: Improved services and an
expanding collection of metabolites. *Nucleic Acids Res.* 2016;44(D1):D1214-9.
doi:10.1093/nar/gkv1031

**LOTUS** — the LOTUS Initiative. Supplies referenced structure–organism
occurrence triples with NCBI taxonomy identifiers. This corpus reads the frozen
Zenodo export (10.5281/zenodo.19360665), which is **CC BY 4.0**, rather than the
Wikidata route, whose main-namespace structured data is CC0 — a committed
inventory needs a release identity and a SPARQL query has none.
<https://lotus.nprod.net/>

Rutz A, Sorokina M, Galgonek J, et al. The LOTUS initiative for open knowledge
management in natural products research. *eLife.* 2022;11:e70780.
doi:10.7554/eLife.70780

**NPClassifier** — Kim et al. CC0 for the ontology, models and data; MIT for
the code. Supplies the biosynthesis-oriented structural classification used as
this corpus's filing decision. <https://github.com/mwang87/NP-Classifier>

Kim HW, Wang M, Leber CA, et al. NPClassifier: A deep neural network-based
structural classification tool for natural products. *J Nat Prod.*
2021;84(11):2795-2807. doi:10.1021/acs.jnatprod.1c00399

**CyanoMetDB** — Eawag and an international consortium. CC BY 4.0. Supplies
manually curated cyanobacterial metabolites with producer organisms and primary
references. <https://www.eawag.ch/en/department/uchem/projects/cyanometdb/>

Jones MR, Pinto E, Torres MA, et al. CyanoMetDB, a comprehensive public
database of secondary metabolites from cyanobacteria. *Water Res.*
2021;196:117017. doi:10.1016/j.watres.2021.117017

**PubChem** — NCBI, NLM, NIH. Public domain (US Government work), with reuse
conditions set by each contributing source, so only structures for identifiers
an adopted source already cross-references are used.
<https://pubchem.ncbi.nlm.nih.gov/>

Kim S, Chen J, Cheng T, et al. PubChem 2023 update. *Nucleic Acids Res.*
2023;51(D1):D1373-D1380. doi:10.1093/nar/gkac956

**AntibioticMech** — CultureBotAI. CC BY 4.0. Supplies the pinned InChIKey
inventory that computes cross-corpus links.
<https://github.com/CultureBotAI/AntibioticMech>

## What is CC0

Everything that is this repository's own work rather than an upstream source's:
the code, the schema, the tests, the configuration, the documentation, the
research reports, and the curation decisions. See [LICENSE](LICENSE).
