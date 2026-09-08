# Harmonization: how sources become records

Read this before changing `scripts/seed_from_sources.py` or any extractor.

## The unit of the corpus is a structure

One `NaturalProductRecord` is one chemical structure. Not one name, not one
preparation, not one class. The operational test is a Standard InChIKey: a
concept without one is not written.

That excludes things upstream sources legitimately model but this corpus cannot
key on:

| Upstream concept | Why it is not a record |
|---|---|
| A MIBiG compound named "a polyketide" | A class, and one of 1,042 MIBiG compound records with no structure |
| "Streptomyces culture extract" | A mixture; activity on it says nothing about a constituent |
| ChEBI's `bacterial metabolite` role | Admits glucose and ATP — see `conf/np_roles.tsv` |
| A LOTUS row whose reference does not resolve | An occurrence with no evidence is not an occurrence |

Those concepts are not lost. They land on the curation worklist, each needing a
structure or an explicit `EXCLUDE` decision in `curation/decisions.tsv`.

## What admits a compound

Membership is **asserted by a source**, never inferred from a structure. One of:

1. an experimentally supported biosynthetic origin — a MIBiG entry linking the
   structure to a gene cluster in a named organism;
2. a cited occurrence in a taxon — a LOTUS structure–organism–reference triple;
3. an allow-listed ChEBI specialized-metabolite role.

NP-likeness scores and computed natural-product flags admit nothing. ChEMBL's
own `natural_product` flag marks prazosin, a wholly synthetic quinazoline,
while its NP-likeness score disagrees — which is the concrete reason this rule
is a rule.

## Identity resolution

For each source concept, in order:

1. **A ChEBI concept grounds to its own CURIE** when ChEBI supplies a default
   structure. ChEBI is the identity authority here.
2. **Otherwise the concept keeps a minted identifier**,
   `naturalproductmech:<source>-<10-hex>`, hashed from `(source, source_id)`.

The hash covers the source identifier, never the label. A minted CURIE is the
key `curation/decisions.tsv` rows are written against, so an upstream label
correction must not move it.

MIBiG stores SMILES and **never an InChIKey** — there is no InChI field
anywhere in its JSON — so keys are generated locally with the pinned RDKit.

## The merge, and its limits

Concepts resolving to the same Standard InChIKey merge into one record carrying
every source concept. That merge is the product.

**A caution on the InChIKey as identity.** It does not recognise some 1,5
keto-enol tautomer pairs as the same compound, cannot express cis/trans in
organometallics, and does not support relative stereochemistry. So a collision
is not proof of sameness, and an absence of collision is not proof of
difference. Macrocyclic peptides, glycopeptides and glycosides — most of this
corpus — are where that bites. `stereo_complete` records when a structure has
undefined stereocentres rather than hiding it.

**A minted record must never duplicate a ChEBI-grounded structure.** That is a
failure of resolution, and `tests/test_corpus_integrity.py` fails on it.

## Producer versus occurrence

Two fields, two evidence bars, and the seeder never promotes one to the other.

`producer_organisms` requires evidence of biosynthesis. From MIBiG, that grade
is machine-readable: each locus carries `evidence[].method` from a controlled
vocabulary, and `conf/producer_evidence.tsv` maps it.

| `evidence_basis` | MIBiG methods |
|---|---|
| `BGC_CHARACTERIZED` | Heterologous expression; Knock-out studies; Enzymatic assays; In vitro expression |
| `BGC_CORRELATED` | Gene expression correlated with compound production; Correlation of genomic and metabolomic data |
| not producer-grade | Homology-based prediction |

Both first tiers are producer claims. `BGC_CORRELATED` is the weaker one and
stays marked as such: correlation is equally consistent with co-regulation, a
neighbouring cluster, or a shared precursor. A method absent from the map fails
closed rather than being admitted by default.

`occurrences` requires a citation and nothing more, because it claims less.
A LOTUS row lands here whatever taxon it names.

**Three MIBiG fields that do not mean what they look like**, all verified
against the 4.0 release:

- `quality` reads `questionable` for 2,710 of 3,013 entries and marks
  legacy-format entries awaiting re-curation, not doubtful science.
- The changelog reviewer id is the `AAAA…` placeholder in 2,988 of 3,013
  entries, so a reviewer gate admits 25 entries.
- `completeness` is `unknown` for 2,132 entries.

None of the three is a truth signal. The locus evidence vocabulary is.

## Filing

`np_pathway` decides one thing: which directory the record lives in and which
row of the report it lands on. It is NPClassifier's pathway, which is
**computed**, so three rules keep it from moving records under a reader:

1. The classifier runs at **extraction** time into a committed,
   manifest-pinned inventory. A seed-time API call would break the offline
   pipeline and make `verify-corpus` meaningless.
2. The pathway is **pinned per record** in `PATHS.tsv` at first seed.
3. A later inventory that disagrees produces a `pathway-drift` worklist entry
   for a curator, never an automatic move. `RETIRED.tsv` reserves the old slug
   when a move is accepted, because slugs are published URLs.

A multi-label or empty classifier result files `UNCLASSIFIED` and queues the
record. Picking the first array element is how AntibioticMech once asserted
that lassomycin is a rifamycin.

## Scope

`conf/sources.yaml` → `producer_scope` filters `producer_organisms` and **not**
`occurrences`. The phases are defined by producer, and dropping a cited
isolation report because its host is out of phase would discard evidence about
a compound the corpus already holds. Phase A therefore contains non-microbial
taxa in `occurrences`, which is correct.
