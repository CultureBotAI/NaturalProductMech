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

1. **A structure matching exactly one 3-star ChEBI entry grounds to that
   CURIE** (`EXACT`). ChEBI is the identity authority, and the record takes its
   definition from there. Only entries ChEBI marks `default_structure` are
   eligible: an alternative depiction is not what ChEBI considers canonical.
2. **A structure matching several 3-star entries stays minted**, with
   `grounding_status: REVIEW_NEEDED` and a note naming the candidates. ChEBI
   keeps a compound and its zwitterion as separate entries sharing an
   InChIKey, on purpose; picking one would overrule the people who own the
   identifiers. Nine records are in this state.
3. **Otherwise the concept keeps a minted identifier**,
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

**ChEBI-internal collisions are not merged.** ChEBI keeps a compound and its
zwitterion as separate entries with the same Standard InChIKey, because they are
different protonation states related by `is_conjugate_acid_of`. Merging them
would overrule a curation decision made by the people who own the identifiers.
Both records stay.

**Two minted concepts sharing a structure are flagged, not merged.** At least
one upstream cross-reference is wrong and the seeder cannot tell which. Merging
would assert the two compounds are the same; dropping both would discard the one
that is right. So both are written, each carrying a `CURATION_TODO` discussion
naming its twin, and `tests/test_corpus_integrity.py` requires that flag.

**A minted record must never duplicate a ChEBI-grounded structure.** That is a
failure of resolution rather than an upstream disagreement, and
`tests/test_corpus_integrity.py` fails on it.

## Producer versus occurrence

Two fields, two evidence bars, and the seeder never promotes one to the other.

`producer_organisms` and `biosynthetic_gene_clusters` carry **two different
claims**, and MIBiG's locus evidence grades only the second one:

* **Does this TAXON make the compound?** That is the producer claim, and it
  rests on the isolation literature.
* **Does this LOCUS make it?** That is the cluster link, and it is what
  `loci[].evidence[].method` speaks to.

They come apart constantly. Heterologous expression proves a cloned locus
suffices in a host; it says nothing new about the native producer. A knock-out
is different, because the locus was removed *in the native organism* and
production stopped, so it addresses both. `conf/producer_evidence.tsv` records
which claim each method supports, in a `supports` column, and grades them
separately:

| Method | Producer | Cluster link |
|---|---|---|
| Knock-out studies | `BGC_CHARACTERIZED` | `CLUSTER_DEMONSTRATED` |
| Gene expression correlated with production | `BGC_CORRELATED` | `CLUSTER_CORRELATED` |
| Correlation of genomic and metabolomic data | `BGC_CORRELATED` | `CLUSTER_CORRELATED` |
| Heterologous expression | `SOURCE_ASSERTION` | `CLUSTER_DEMONSTRATED` |
| Enzymatic assays, in vitro expression | `SOURCE_ASSERTION` | `CLUSTER_DEMONSTRATED` |
| Homology-based prediction | `SOURCE_ASSERTION` | `CLUSTER_PREDICTED` |
| *none stated* | `SOURCE_ASSERTION` | `CLUSTER_UNSTATED` |

Folding the two together over-graded 485 producer claims as
`BGC_CHARACTERIZED` on evidence that had never addressed the organism, while
the whole locus-evidence distribution turned out to belong in the cluster
column all along.

`SOURCE_ASSERTION` is the commonest producer grade and that is honest rather
than lax: MIBiG asserts production and cites a report nobody here has read. It
sits outside `CAUSAL_BASES`, so a consumer wanting demonstrated production
filters it out.

**A taxon in both fields is corroboration, not redundancy.** 729 records name
the same organism as a producer and in an occurrence. That is two different
claims with two independent citations — MIBiG asserting production from a gene
cluster, and someone else reporting they detected the compound in that organism
— so holding both is more evidence than holding either. The occurrence says so
in its notes, and `just report` counts it, because otherwise it reads as a
failure to deduplicate.

`occurrences` requires a citation and a resolvable taxon, and nothing more,
because it claims less. ChEBI's `compound_origins` rows land here: ChEBI is
recording where a compound was *found*, not what makes it, so nothing promotes
them. A row naming a species with no numeric accession is dropped rather than
carried — a name-only organism is a name-only join, which is a curation project
rather than an extraction, and `Occurrence.taxon_id` is required so that it
cannot slip through. That rule was written down after the guarded write path
refused 1,146 such rows.

**The same rule reaches the assay organism.** A `molecular_target` records
which organism's protein was assayed, and all 123 of them carried a
`taxon_label` and no identifier — the same name-only join, in a field the
schema left optional (#67). BindingDB's organism names are now requested from
NCBI Taxonomy alongside the occurrence sources, and 107 of 122 resolve. The
remaining 15 are UniProt's proteome-strain format, `Escherichia coli (strain
K12)`, and one common name; they stay unresolved rather than being stripped to
a species, because a species id under a strain label is the defect this rule
exists to prevent (#72). They are counted at seed time and queued in
`curation/unresolved_taxa.tsv`.

`target_id` stays empty on purpose, and that is not the same gap. The schema
says a target "should be a family, complex or function; an organism-specific
accession is an example of a target, not a target identity", so BindingDB's
UniProt accessions go to `protein_examples`, where 115 of them are. Filling
`target_id` needs a family or function identifier no adopted source supplies.

**A producer needs an organism, and some NCBI nodes are not one.** A producer
claim on `NCBITaxon:12908` ("unclassified sequences") or `NCBITaxon:77133`
("uncultured bacterium") asserts a producer while naming none, and every gate
passes it — the CURIE is valid, the label is non-empty, one label per id. 42
claims did (#62, #68). So the seeder writes no producer for them.

`data/raw/taxon_non_organism.tsv` is the decision, derived from NCBI's own tree
by `just extract-taxonomy` rather than listed by hand, and restricted to taxa
the adopted sources use. Three ways a taxon lands in it:

- **structural** — the root, the rank above the domains, and NCBI's two bins,
  `unclassified sequences` and `unidentified`;
- **a non-organism subtree** — anything under `metagenomes` (a community, not
  an organism: `sponge metagenome`) or under `unclassified sequences`
  (`synthetic microbial community`);
- **a generic bin** — `uncultured bacterium` and `uncultured organism`.

The last needs its reason stated, because no lineage rule finds it. NCBI files
`uncultured bacterium` under an `environmental samples` wrapper directly beneath
the domain Bacteria — and files `uncultured bacterium AR_456` in *exactly* the
same place. The difference is not the tree, it is what a join on the id would
mean. 36 producer claims here point at `77133`, so treating it as an organism
says one bacterium makes 36 unrelated compounds. `AR_456` has its own taxid for
one clone lineage, and two records citing it agree about something. So the
generic bins are withheld and the specific uncultured clones are kept — 39
withheld, 29 kept — along with genus-level placements like `uncultured
Candidatus Entotheonella sp.`, which name a real taxon and are the state of the
art for sponge symbionts.

The claim is judged on the id the record would carry, after merged ids are
rewritten forward, so an id NCBI retired *into* a bin is caught as a bin.

What it does **not** do is drop the compound. MIBiG is the only source that
*admits* a structure — ChEBI grounds one but cannot hold a record alone — so
dropping the row would have deleted elaiophylin, a record carrying 25
occurrences, five bioactivities and an AntibioticMech link, over one unnamed
producer. A characterized cluster is an origin assertion whether or not its
host has a name; pederin's real producer is an uncultured symbiont, which is
exactly why MIBiG says 12908 for one of its three clusters and `uncultured
bacterium` for the other two. The compound, its structure and its cluster stay,
the cluster carries no organism, and an `unnamed-producer` CURATION_TODO names
each accession and why its taxon was refused. Pederin keeps all three gene
clusters — including the one graded `CLUSTER_DEMONSTRATED` — and loses all
three producer claims, which is exactly the producer/locus split this corpus
exists to keep: the locus claim survives its host being anonymous.

The inventories keep what the source said. `mibig_compounds.tsv` still records
`NCBITaxon:12908`; withholding is a decision the seeder makes at write time,
not an erasure of provenance.

**A merged taxon id is rewritten, not rejected.** MIBiG assigns taxids at
submission and LOTUS carries them from Wikidata, so both supply ids NCBI has
since retired into another taxon: 42 of them, 118 rows, found by the first
id-label run. NCBI keeps the redirect, so these still denote the organism — but
two records citing one organism under its old and new ids do not join, and a
consumer resolving against a current taxonomy gets nothing. `taxon_merged.tsv`,
built from the same taxdump as `taxon_names.tsv`, maps old to current; the
seeder rewrites every source-supplied id through it and says so on the claim.
The source's id stays in the inventory as provenance. 167 ids were rewritten,
and it raised producer-occurrence corroboration from 721 records to 732 —
claims that always described one organism and could not previously be seen to.

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
3. A later inventory that disagrees is to produce a `pathway-drift` worklist
   entry for a curator, never an automatic move. Rules 1 and 2 are enforced;
   this one is owed (#43, #52) — today a disagreement is silent. `RETIRED.tsv` reserves the old slug
   when a move is accepted, because slugs are published URLs.

A multi-label or empty classifier result files `UNCLASSIFIED` and queues the
record. Picking the first array element is how AntibioticMech once asserted
that lassomycin is a rifamycin.

## What crosses from a sibling corpus, and what does not

A structure in both this corpus and AntibioticMech is linked, never copied.
What crosses is the **classification** — the sibling's `antimicrobial_class`
becomes a `bioactivity_summary` value here, which `docs/CURATION.md` permits
because a sibling link is one of the four backings that rule accepts.

What does not cross is the **mechanism**: molecular targets, resistance
determinants and MIC spectra stay in the corpus that owns those claims. A test
asserts that nothing from the sibling's mechanism layer appears on a record
here.

The mapping is lossless in the two directions that matter. `ANTIPROTOZOAL`
becomes `ANTIPARASITIC` because that is this corpus's name for it;
`ANTIMYCOBACTERIAL` keeps its own value rather than being widened to
antibacterial; and `ANTIMICROBIAL_UNSPECIFIED` stays unspecified, because a
source that declines to name the microbes is telling you something and mapping
it to a specific class would invent the specificity it withheld. An unmapped
class is dropped rather than guessed, and the link still stands.

## Scope

`conf/sources.yaml` → `producer_scope` filters `producer_organisms` and **not**
`occurrences`. The phases are defined by producer, and dropping a cited
isolation report because its host is out of phase would discard evidence about
a compound the corpus already holds. Phase A therefore contains non-microbial
taxa in `occurrences`, which is correct.
