# NPASS and CO-ADD: what they would add, measured before the licence is resolved

Evaluation date: 2026-09-08. Written under the owner's decision of 2026-09-07 to
proceed with both sources while their licence questions are resolved later as a
batch.

**Nothing from either source entered the repository.** No inventory in
`data/raw/`, no records, no redistributable content. What follows is counts
about the data, produced by `scripts/evaluate_npass.py`, so that when the
licence answer arrives it arrives to a decision already made on evidence.

## NPASS: the largest single gain available to this corpus

Measured against the committed corpus of 3,115 structures:

| | |
|---|---:|
| NPASS structures in release 3.0 | 203,390 |
| **Joined to the corpus by exact Standard InChIKey** | **1,895 (61%)** |
| Activity rows for corpus structures | 70,102 |
| Distinct corpus structures with an activity | 588 |
| Species-pair rows for corpus structures | 9,083 |
| Distinct corpus structures with a species pair | 1,888 |

Every one of the 70,102 activity rows carries **units, a target identifier and
an assay organism**, and every one of the 9,083 species-pair rows carries a
reference. That matters because the corpus refuses a measurement without units
and a method, and refuses an occurrence without a citation — the usual reason a
bioactivity source cannot be seeded is that most of its rows would fail those
gates. NPASS's would not.

Most common activity types among the joined rows:

| Type | Rows |
|---|---:|
| MIC | 17,090 |
| IC50 | 15,263 |
| Activity | 5,222 |
| GI50 | 3,003 |
| Potency | 2,436 |
| AC50 | 2,144 |
| Inhibition | 1,960 |
| Kd | 1,685 |

For scale: `bioactivities` is currently empty on all 3,115 records, and
`molecular_targets` is populated on 14. NPASS would take the first to roughly
588 records and the second far beyond 14.

**Why it is joinable at all.** NPASS is natively InChIKey-keyed. Most of the
bioactivity landscape is name-keyed, which the `source-queue` skill classes as
a curation project rather than an extraction. A 61% structure-level join with
no name matching is what makes this source different in kind from its
neighbours.

**The blocker is unchanged and is not technical.** Re-checked 2026-09-08: the
NPASS download page carries no licence, copyright or terms-of-use statement,
consistent with the homepage and about page checked on 2026-09-07. A
third-party registry records CC-BY-NC; that is not the maintainers' word, and
no statement is not permission. `scripts/check_source_queue.py` refuses an
ADOPTED row under unverified terms, and that gate is what the corpus's CC BY
4.0 promise rests on.

**Caveats that survive a grant**, from the source research: NPASS inherits from
COCONUT, UNPD and TCM resources, so upstream errors propagate and one
occurrence can arrive by several routes; species sources are genus-level for a
large fraction, which this corpus's required `taxon_id` would reject as it
already rejects 1,146 ChEBI origins and 804 LOTUS rows; and a 2023 tranche of
roughly 66,600 compounds carries only *estimated* activity profiles, which must
never be read as measurements. The activity rows would need a filter
distinguishing measured from estimated before any of them were seeded.

## CO-ADD: the evaluation is bounded by its own terms

CO-ADD's terms state that content "may not be systematically downloaded,
retrieved or stored". An evaluation that downloaded its files to count them
would breach exactly the terms under discussion, so **no CO-ADD data was
fetched**.

The two indirect routes both dead-end:

- **Through ChEMBL**, where CO-ADD's screening is deposited as 35 assays and
  99,793 activities. ChEMBL is CC BY-SA 3.0, so that slice cannot be seeded
  into a CC BY 4.0 corpus either — the route changes the licence, not the
  answer.
- **Through published summaries**, which give totals rather than the
  structure-level join this corpus needs. Nothing there answers "how many of
  our 3,115 records would gain a measurement".

So CO-ADD's evaluation is complete in the sense that matters: **it cannot be
measured without either breaching its terms or inheriting share-alike ones**,
and that is the finding. Its value is unchanged and unverified.

The ask remains worth making. CO-ADD is a Wellcome-funded open-science project
whose front page reads "Open-access Antimicrobial Screening Database" while its
only terms page reserves all rights — which reads like unmodified 2016
university boilerplate rather than an intended restriction.

## Recommendation

Both licence requests are worth making, and NPASS is worth making first. It is
the single largest gain available to this corpus from any source, blocked by a
missing sentence rather than by a restrictive one, and the measurement above is
the argument to send with the request.
