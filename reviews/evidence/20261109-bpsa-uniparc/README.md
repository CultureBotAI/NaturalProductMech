# Revised BpsA UniParc identity audit

Primary UniProt/UniParc JSON responses retained for issue #1244. Dates, source URLs and exact byte digests are in `manifest.json`.

UPI000444B524 matches the full 1,283-residue revised ACK77757.2 / ATZ29785.1 / A0A2K8PVS5 sequence and has Thr385. Historical UPI0001895A6C carries ACK77757.1 and Ala385. Their sole sequence difference is position 385. Previously cited UPI0001DE5E11 is an unrelated 146-residue entry, retained as a negative control.

Sequence correspondence does not establish the experimental parental allele, experimental stock identity or equivalence between historical and revised references. Existing biological caveats and historical curation events are retained.

Replay the offline evidence and current-record assertions with `uv run --extra dev pytest -q tests/test_bpsa_uniparc_identity.py`. No test contacts a source. The correction appends a current curation event using the native validated writer; it does not change either historical goal or acceptance state.
