# Numbered-Product Review Evidence

Four distinct structures were inspected at durable main commit
`22ced0a503edd1d04628f7cfbdbb14ee1d03047c`. Generic compound numbers do
not establish equivalence between publications or owners.

| Owner | MIBiG member (one-based) | Observation |
| --- | --- | --- |
| shikimates_and_phenylpropanoids/compound-8 | BGC0002290.2:7 | Partial, seed-only |
| terpenoids/compound-8-2 | BGC0002162.3:6 | Partial, provisional major #983 |
| terpenoids/compound-6-2 | BGC0002162.3:3 | Partial, provisional major #982 |
| terpenoids/compound-6 | BGC0002290.2:9 | Partial, seed-only |

The two BGC0002162 encodings are C25H41+ cations. Locus-level heterologous
expression and database NMR annotations have not been traced to direct
characterization of these exact charged structures. Proposed intermediates
are not automatically isolated products. No definitive replacement, deletion,
strain mismatch, or exclusion of charged metabolites is asserted. The two
BGC0002290 numbered-material assignments remain inaccessible in primary full
text; this is an evidence gap, not a confirmed scientific contradiction.

All native records, graphs, inventories, classifications, statuses and history
remain unchanged. The full campaign denominator is 3,115 owners; each review's
denominator is one. A partial observation is not completed scientific coverage.

## Replay

With the repository's locked chemistry environment (RDKit 2026.03.5):

```bash
uv run --extra chemistry python reviews/evidence/20261014-numbered-products/replay.py \
  --output /tmp/numbered-products-replay.json
diff reviews/evidence/20261014-numbered-products/replay-result.json /tmp/numbered-products-replay.json
uv run pytest -q tests/test_numbered_products_review_archive.py
```

Use a new output filename; replay refuses overwriting. `--repo` supports running
from another directory. It verifies historical input hashes, exact InChIKeys,
one-based source membership, taxonomy/locus fields and all nine pinned inventory
joins. ChEBI origins join through exact-key ChEBI structure IDs, not a nonexistent
origin InChIKey column. Replay is deterministic chemistry/source validation,
not experimental sign-off or a current database refresh.

## Provenance And Limits

`manifest.json` pins the retained files and 15 historical Git inputs.
`sources.json` records retrieval URLs/times/hashes. Retained structured inputs
are attributed to MIBiG and NCBI; the BGC0002162 and DS027698.1 payloads are reused
from the existing compound-5 packet. JCM1740 deposit equivalence is represented
by a short factual extraction, with the catalogue URL and original response hash.
The literal SI spelling JMC1740 is interpreted as a transposition, explicitly
an inference rather than a distinct-strain claim.

Full articles, abstracts, SI PDF and catalogue HTML are reference-only and are
not redistributed. `source-analysis.json` removes only the abstract text from
the original analysis; its original hash is recorded. The original helper is
archived as text, not offered as a portable executable. Successful analysis
logs containing abstracts are likewise not copied. The replay result is the
portable encoding/inventory calculation.

2015 main-text and 2020 main-text/SI access denials were respected. Previously
retrieved public 2015 SI was inspected only at the pages named in the reviews.
The 2018 study is a separate primary publication, not an alternate copy of the
denied 2015 paper; its failed figure-page request was not retried elsewhere.
An adversarial recheck of the 2018 main page also failed at an inaccessible
identity-provider redirect; earlier inspected text was not retrieved elsewhere.
No exact stereochemical crosswalk is claimed from the SI's ent-6 depiction.

`checks-initial.json` and `checks-final.json` retain actual execution receipts,
including rejected unsaved drafts and failed environment setup attempts.
Temporary paths describe historical execution, not replay prerequisites.
`review-index.json` identifies the four immutable canonical pairs.

Publication issue [#984](https://github.com/CultureBotAI/NaturalProductMech/issues/984)
covers scope/verdict formatting and durable evidence. Scientific issues
[#982](https://github.com/CultureBotAI/NaturalProductMech/issues/982) and
[#983](https://github.com/CultureBotAI/NaturalProductMech/issues/983) remain open
pending legitimate exact-product evidence, regardless of passing CI.
