"""Pinned, explicit MIBiG structure replacements; never rewrite source inventories."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import date
from urllib.parse import urlsplit

ALLOWED_ACTIONS = {
    "REPLACE_WITH_CHEBI",
    "SPLIT_SHARED_WITH_CHEBI",
    "REPLACE_SHARED_WITH_CHEBI",
}


def row_digest(row: dict[str, str]) -> str:
    """Pin the complete parsed TSV row, including empty fields and source context."""
    return hashlib.sha256(json.dumps(
        row, sort_keys=True, ensure_ascii=True, separators=(",", ":")
    ).encode("utf-8")).hexdigest()


def apply_structure_corrections(
    rows: list[dict[str, str]],
    corrections: list[dict[str, str]],
    chebi_rows: list[dict[str, str]],
) -> list[dict[str, str]]:
    """Replace a uniquely owned or shared structure group, or split onto a pinned ChEBI entry.

    No equivalence is asserted between old and new keys. All old xrefs are
    withheld, and other inventories still join only on their own exact keys.
    Collisions require a separate migration, not an implicit merge here.
    """
    result = [dict(row) for row in rows]
    source_keys = Counter(row["standard_inchi_key"] for row in rows)
    remaining_source_keys = Counter(source_keys)
    seen_sources: set[str] = set()
    seen_targets: dict[str, tuple[str, str]] = {}
    actions_by_old_key: dict[str, set[str]] = defaultdict(set)
    shared_replace_targets: dict[str, tuple[str, str, str, str]] = {}
    shared_replace_counts: Counter[str] = Counter()
    for correction in corrections:
        required = (
            "source_id", "expected_source_row_sha256", "target_chebi_id",
            "expected_target_row_sha256", "standard_inchi", "stereo_complete",
            "reference", "curator", "date", "rationale",
        )
        if any(not isinstance(correction.get(field), str) or not correction[field].strip()
               for field in required):
            raise ValueError("structure correction requires complete pins, chemistry and attribution")
        source_id = correction["source_id"]
        action = correction.get("action")
        if action not in ALLOWED_ACTIONS:
            raise ValueError(f"{source_id}: invalid structure correction action")
        if source_id in seen_sources:
            raise ValueError(f"{source_id}: duplicate structure correction")
        seen_sources.add(source_id)
        for field in ("expected_source_row_sha256", "expected_target_row_sha256"):
            if not re.fullmatch(r"[a-f0-9]{64}", correction[field]):
                raise ValueError(f"{source_id}: invalid row digest")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", correction["date"]):
            raise ValueError(f"{source_id}: invalid correction date")
        date.fromisoformat(correction["date"])
        reference = correction["reference"]
        url = urlsplit(reference)
        if not (re.fullmatch(r"(?:DOI:10\.\d{4,9}/\S+|PMID:\d+)", reference) or (
            url.scheme == "https" and url.hostname and not re.search(r"\s", reference)
        )):
            raise ValueError(f"{source_id}: correction requires a stable reference")
        if correction["stereo_complete"] not in {"true", "false"} or not re.fullmatch(
            r"InChI=1S/\S+", correction["standard_inchi"]
        ):
            raise ValueError(f"{source_id}: invalid derived chemistry")

        matches = [(i, row) for i, row in enumerate(rows)
                   if f"{row['mibig_accession']}:{row['compound_index']}" == source_id]
        targets = [row for row in chebi_rows if row["chebi_id"] == correction["target_chebi_id"]]
        if len(matches) != 1 or len(targets) != 1:
            raise ValueError(f"{source_id}: correction requires exactly one source and target row")
        index, original = matches[0]
        target = targets[0]
        if row_digest(original) != correction["expected_source_row_sha256"]:
            raise ValueError(f"{source_id}: structure correction source drift")
        if row_digest(target) != correction["expected_target_row_sha256"]:
            raise ValueError(f"{source_id}: structure correction target drift")
        old_key, new_key = original["standard_inchi_key"], target["standard_inchi_key"]
        if (target.get("stars") != "3" or not target.get("smiles")
                or not re.fullmatch(r"CHEBI:\d+", target["chebi_id"])
                or not re.fullmatch(r"[A-Z]{14}-[A-Z]{10}-[A-Z]", new_key)):
            raise ValueError(f"{source_id}: target must be a structured 3-star ChEBI entry")
        target_owner = seen_targets.get(new_key)
        if (not old_key or new_key in source_keys
                or (target_owner is not None
                    and target_owner != ("REPLACE_SHARED_WITH_CHEBI", old_key))
                or sum(row["standard_inchi_key"] == new_key for row in chebi_rows) != 1):
            raise ValueError(f"{source_id}: structure correction requires unambiguous, distinct owners")
        actions_by_old_key[old_key].add(action)
        if len(actions_by_old_key[old_key]) > 1:
            raise ValueError(f"{source_id}: cannot mix structure correction actions on {old_key}")
        if action == "REPLACE_WITH_CHEBI":
            if source_keys[old_key] != 1:
                raise ValueError(f"{source_id}: structure correction requires unambiguous, distinct owners")
        elif action == "SPLIT_SHARED_WITH_CHEBI":
            if source_keys[old_key] <= 1 or remaining_source_keys[old_key] <= 1:
                raise ValueError(
                    f"{source_id}: split structure correction requires a shared source key "
                    "with a remaining owner"
                )
        else:
            if source_keys[old_key] <= 1:
                raise ValueError(
                    f"{source_id}: shared structure replacement requires a shared source key"
                )
            target_sig = (
                correction["target_chebi_id"],
                correction["expected_target_row_sha256"],
                correction["standard_inchi"],
                correction["stereo_complete"],
            )
            if old_key in shared_replace_targets and shared_replace_targets[old_key] != target_sig:
                raise ValueError(
                    f"{source_id}: shared structure replacement for {old_key} requires an "
                    "identical ChEBI target across all rows"
                )
            shared_replace_targets[old_key] = target_sig
            shared_replace_counts[old_key] += 1
        remaining_source_keys[old_key] -= 1
        seen_targets[new_key] = (action, old_key)
        note = (
            f"Curated structure replacement for MIBiG {source_id}, version "
            f"{original['entry_version']}: {old_key} -> {target['chebi_id']} ({new_key}). "
            f"{correction['rationale']} Original database_ids withheld: "
            f"{original['database_ids'] or 'none'}. Other inventories are joined only "
            f"on the corrected key, never transferred from the old key. "
            f"Source row SHA256 {correction['expected_source_row_sha256']}; "
            f"target row SHA256 {correction['expected_target_row_sha256']}. "
            f"Curator: {correction['curator']}; date: {correction['date']}."
        )
        result[index].update({
            "smiles": target["smiles"],
            "standard_inchi": correction["standard_inchi"],
            "standard_inchi_key": new_key,
            "stereo_complete": correction["stereo_complete"],
            "database_ids": "",
            "structure_source": "CHEBI",
            "structure_source_id": target["chebi_id"],
            "structure_correction_note": note,
            "structure_correction_reference": reference,
        })
        if action in {"REPLACE_WITH_CHEBI", "REPLACE_SHARED_WITH_CHEBI"}:
            result[index]["structure_correction_old_key"] = old_key
    for old_key, count in shared_replace_counts.items():
        if count != source_keys[old_key] or remaining_source_keys[old_key] != 0:
            raise ValueError(
                f"shared structure replacement for {old_key} must cover all "
                f"{source_keys[old_key]} rows sharing that key"
            )
    return result
