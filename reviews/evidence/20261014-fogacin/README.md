# Fogacin Review Evidence

This pack assesses the two exact fogacin owners at
`12e9c505e12ba17920a7c95964fd1c35e3e057d3`. Similar labels do not make their
different hydrogenation states interchangeable. The native records remain
SEEDED; deterministic chemistry checks do not establish primary identity.

`replay-inputs.json` pins nine historical Git inputs and eight captured database
responses. `sources.json` retains HTTP metadata, including unsuccessful article
access. Primary articles and abstract bodies are not redistributed. Their
inspected scope and access limitations are recorded in the structured reviews.

Run with the repository dependencies and pinned RDKit 2026.03.5 installed:

```sh
python reviews/evidence/20261014-fogacin/inspect_sources.py --output /tmp/fogacin-replay.json
```

The helper can run outside the repository working directory. It resolves its
pack relative to its own file and accepts `--repo` for another checkout with the
historical base available. Output is exclusive: choose a new output path.
`source-inspection.json` is the retained baseline output, not a claim that all
deposited protein annotations have experimental validation. ChEBI origins join
through matched ChEBI structure identifiers, not an absent InChIKey column.
