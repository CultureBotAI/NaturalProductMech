"""Replay the retained pre-curation chemistry audit against its exact Git base."""

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

PACK = Path(__file__).resolve().parent


def verify_owner_snapshots(repo, pack, base):
    for slug in ("geldanamycin-2", "geldanamycin"):
        path = f"data/natural_products/polyketides/{slug}.yaml"
        data = subprocess.check_output(["git", "-C", str(repo), "show", f"{base}:{path}"])
        owner = yaml.safe_load(data)
        snapshot = json.loads((pack / (slug + "-resolved.json")).read_text())
        if owner.get("causal_graph_refs") or owner != snapshot:
            raise ValueError(f"Snapshot does not match exact historical inline owner: {slug}")


def replay(repo, output):
    manifest = json.loads((PACK / "manifest.json").read_text())
    expected = json.loads((PACK / "source-inspection.json").read_text())
    verify_owner_snapshots(repo, PACK, manifest["base"])
    with tempfile.TemporaryDirectory(prefix="geldanamycin-replay-") as work:
        work = Path(work)
        for name, digest in manifest["retained"].items():
            # Preserve the originally executed script, including its unused import.
            source = PACK / ("inspect_sources.original.py.txt" if name == "inspect_sources.py" else name)
            data = source.read_bytes()
            if hashlib.sha256(data).hexdigest() != digest:
                raise ValueError(f"Evidence drift: {name}")
            if name != "source-inspection.json":
                shutil.copyfile(source, work / name)
        raw = work / "data/raw"
        raw.mkdir(parents=True)
        for name in expected["inventories"]:
            path = f"data/raw/{name}.tsv"
            data = subprocess.check_output(["git", "-C", str(repo), "show", f"{manifest['base']}:{path}"])
            (raw / (name + ".tsv")).write_bytes(data)
        subprocess.run([sys.executable, str(work / "inspect_sources.py")], cwd=work,
                       stdout=subprocess.DEVNULL, check=True)
        actual = json.loads((work / "source-inspection.json").read_text())
        if actual != expected:
            raise ValueError("Replay differs from retained source inspection")
        with output.open("x") as handle:
            json.dump(actual, handle, indent=2)
            handle.write("\n")
    print("Reproduced both pre-curation chemistry and inventory audits.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=PACK.parents[2])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    replay(args.repo, args.output)
