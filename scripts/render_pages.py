#!/usr/bin/env python3
"""Render the browsable site under pages/ from the committed corpus.

    just render
    just render-check

The site is committed, like the corpus and the inventories, so a reader gets
what CI rendered rather than what their toolchain happens to produce. That also
means it can go stale against the corpus exactly as a record could go stale
against `data/raw/`, which is what `--check` is for: it renders to a temporary
directory and fails if `pages/` differs.

What the pages are FOR
----------------------
The corpus exists to keep a producer claim and an occurrence apart, so every
page that can show the distinction shows it. A record page gives producers
their evidence basis and occurrences their citation, in separate sections, and
says on each what the claim does and does not assert. A pathway page counts
causal against asserted producer claims per record, because that ratio is the
honest summary of how much of this corpus is demonstrated.

The filing pathway is NPClassifier's and therefore computed, so the record page
says which model version decided it rather than presenting it as an assertion.
"""

from __future__ import annotations

import argparse
import csv
import filecmp
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode, urlsplit

import yaml
from jinja2 import Environment, FileSystemLoader, pass_context, select_autoescape
from markupsafe import Markup, escape

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = REPO_ROOT / "src" / "naturalproductmech" / "templates"
CORPUS_DIR = REPO_ROOT / "data" / "natural_products"
PAGES_DIR = REPO_ROOT / "pages"
SCHEMA_PATH = REPO_ROOT / "src" / "naturalproductmech" / "schema" / "naturalproductmech.yaml"
SITE_BASE = "https://culturebotai.github.io/NaturalProductMech/pages/"
REPO_URL = "https://github.com/CultureBotAI/NaturalProductMech"
CHEMICAL_MAP_ARTIFACT = REPO_ROOT / "data" / "embeddings" / "chemical-structure-map.json"

PATHWAY_TITLES = {
    "ALKALOIDS": "Alkaloids",
    "AMINO_ACIDS_AND_PEPTIDES": "Amino acids and peptides",
    "CARBOHYDRATES": "Carbohydrates",
    "FATTY_ACIDS": "Fatty acids",
    "POLYKETIDES": "Polyketides",
    "SHIKIMATES_AND_PHENYLPROPANOIDS": "Shikimates and phenylpropanoids",
    "TERPENOIDS": "Terpenoids",
    "UNCLASSIFIED": "Unclassified",
}
PATHWAY_BLURBS = {
    "UNCLASSIFIED": "The classifier returned several pathways or none, so the "
                    "filing decision was left open rather than resolved by array order.",
}

#: Fields the index reports coverage for, in the order `just report` uses.
COVERAGE_FIELDS = [
    "biosynthesis_origin", "producer_taxon_groups", "occurrence_taxon_groups",
    "producer_organisms", "occurrences", "biosynthetic_gene_clusters",
    "biosynthetic_pathway", "bioactivities", "bioactivity_summary", "molecular_targets",
    "causal_graphs", "related_records", "discussions",
]

sys.path.insert(0, str(REPO_ROOT / "src"))
from naturalproductmech.grading import CAUSAL_BASES  # noqa: E402
from naturalproductmech.graph_components import read_natural_product  # noqa: E402

# --- where a displayed identifier leads ---------------------------------------
#: The public page for each namespace a record page shows, keyed by the prefix
#: exactly as the corpus spells it, with the local-id shape that page exists
#: for. Every route was opened in a browser on 2026-10-25; RHEA answers a bot
#: check before its page. An identifier whose shape does not match is shown as
#: text rather than sent to a page that does not exist.
_MIBIG = (r"BGC[0-9]{7}(?:\.[0-9]+)?", "https://mibig.secondarymetabolites.org/go/{}")
# GenBank accessions (CP011254.1, AUSV01000133.1, AKJ75108.1) and RefSeq-style
# ones (NZ_CP011254.1, NC_003888.3, WP_011030045.1, GPC_000003970.1). MIBiG
# writes its own placeholder, MIBIG.BGC0001325.1, for a sequence it holds
# itself; GenBank has no such record, so that value stays text.
_NUCCORE = (r"(?:[A-Z]{2,3}_)?[A-Z]{0,6}[0-9]+(?:\.[0-9]+)?", "https://www.ncbi.nlm.nih.gov/nuccore/{}")
_PROTEIN = (r"(?:[A-Z]{2,3}_)?[A-Z]{0,3}[0-9]+(?:\.[0-9]+)?", "https://www.ncbi.nlm.nih.gov/protein/{}")
_PUBCHEM_CID = (r"[0-9]+", "https://pubchem.ncbi.nlm.nih.gov/compound/{}")
RESOLVERS: dict[str, tuple[str, str]] = {
    "CHEBI": (r"[0-9]+", "http://purl.obolibrary.org/obo/CHEBI_{}"),
    "chembl": (r"CHEMBL[0-9]+", "https://www.ebi.ac.uk/chembl/explore/compound/{}"),
    "ComplexPortal": (r"CPX-[0-9]+", "https://www.ebi.ac.uk/complexportal/complex/{}"),
    "DOI": (r"10\.[0-9]{4,9}/\S+", "https://doi.org/{}"),
    "EC": (r"[0-9]+(?:\.(?:[0-9]+|n[0-9]+|-)){0,3}", "https://enzyme.expasy.org/EC/{}"),
    "genbank": _NUCCORE,
    "GO": (r"[0-9]{7}", "https://www.ebi.ac.uk/QuickGO/term/GO:{}"),
    # LOTUS identifies a structure by its Wikidata item.
    "lotus": (r"Q[0-9]+", "https://www.wikidata.org/wiki/{}"),
    "MIBiG": _MIBIG, "MIBIG": _MIBIG, "mibig": _MIBIG,
    "NCBI_Nuccore": _NUCCORE,
    "NCBI_Protein": _PROTEIN, "NCBIProtein": _PROTEIN,
    "NCBITaxon": (r"[0-9]+", "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id={}"),
    "npatlas": (r"NPA[0-9]+", "https://www.npatlas.org/explore/compounds/{}"),
    "PDB": (r"[0-9][A-Za-z0-9]{3}", "https://www.rcsb.org/structure/{}"),
    "PMID": (r"[0-9]+", "https://pubmed.ncbi.nlm.nih.gov/{}/"),
    # MIBiG's cross-references name PubChem compounds by CID.
    "pubchem": _PUBCHEM_CID, "pubchem.compound": _PUBCHEM_CID,
    "pubchem.aid": (r"[0-9]+", "https://pubchem.ncbi.nlm.nih.gov/bioassay/{}"),
    "RHEA": (r"[0-9]+", "https://www.rhea-db.org/rhea/{}"),
    "UniProtKB": (r"[A-Z0-9]{6,10}(?:-[0-9]+)?", "https://www.uniprot.org/uniprotkb/{}/entry"),
}
#: Namespaces the corpus uses that no page resolves, so they are shown as text:
#: CyanoMetDB is a downloadable table with no per-compound page, and bioregistry
#: knows neither it nor this corpus's or AntibioticMech's minted identifiers.
#: A minted identifier of this corpus links its own record page instead.
UNRESOLVABLE = frozenset({"antibioticmech", "cyanometdb", "naturalproductmech"})
LOCAL_PREFIX = "naturalproductmech"
CURIE = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*:[^\s<>\"'`\\]+")
_WEB = re.compile(r"(?i)https?://")


def _web_url(value: str) -> str | None:
    """An http(s) URL with a host and no credentials, else None."""
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        return None
    try:
        parts = urlsplit(value)
        _ = parts.port  # rejects a malformed port
    except ValueError:
        return None
    if (parts.scheme.lower() in {"http", "https"} and parts.hostname
            and parts.username is None and parts.password is None):
        return value
    return None


def curie_url(value: object) -> str | None:
    """Where a reader can look up a displayed identifier, or None if nowhere.

    Known namespaces use RESOLVERS, and only for the local-id shape their page
    exists for. A well-formed identifier of any other prefix falls back to
    bioregistry.io, which resolves or explains every registered prefix; the
    namespaces in UNRESOLVABLE stay text. A URL, or an identifier whose local
    part is one (`url:https://...`, as some references are written), is its
    own address.
    """
    if not isinstance(value, str):
        return None
    text = value.strip()
    if _WEB.match(text):
        return _web_url(text)
    if not CURIE.fullmatch(text):
        return None
    prefix, local = text.split(":", 1)
    if _WEB.match(local):
        return _web_url(local)
    route = RESOLVERS.get(prefix)
    if route:
        shape, template = route
        if not re.fullmatch(shape, local):
            return None
        return template.format(quote(local, safe="/" if prefix == "DOI" else ""))
    if prefix in UNRESOLVABLE:
        return None
    return "https://bioregistry.io/" + quote(text, safe=":/")


@pass_context
def term_link(context: Any, value: object) -> Markup:
    """A displayed identifier, linked to where a reader can look it up.

    An identifier naming one of this corpus's records opens that record's page,
    before any external resolver is consulted. On the record's own page its
    identifier opens what the page is built from instead of reloading it: the
    ChEBI entry for an exact identity, the source YAML for a minted one.
    Everything else goes through curie_url(); a value no route accepts is
    shown as text, never as a link to nowhere.
    """
    if value is None or value == "":
        return Markup("")
    text = str(value).strip()
    record = context.get("r")
    own = record.get("identifier") if isinstance(record, dict) else None
    pages = context.get("own_pages") or {}
    if text != own and text in pages:
        url: str | None = f"{context.get('root') or ''}{pages[text]}"
    elif text == own and text.startswith(LOCAL_PREFIX + ":") and record.get("record_path"):
        url = f"{REPO_URL}/blob/main/{quote(record['record_path'])}"
    else:
        url = curie_url(text)
    if url:
        return Markup('<a href="{}">{}</a>').format(url, text)
    return escape(text)


# Citation tokens inside record prose. URLs come first so that a DOI inside a
# URL stays part of that URL. Matching runs on the raw text and every piece is
# escaped on the way out, so record text never becomes markup. A URL or DOI
# never contains whitespace, angle brackets, quotes, backticks or square
# brackets, so markup written around one -- `[10.1/x](https://...)`, a DOI in
# backticks or bold -- ends the token instead of joining it (CultureBotAI/TraitMech#2022).
_TOKEN_CHARS = r"[^\s<>\"'`\\\[\]]"
_CITATION = re.compile(
    rf"(?P<url>\b(?i:https?)://{_TOKEN_CHARS}+)"
    rf"|(?P<doi>(?:\b(?i:doi)(?::\s?|=|\s))?(?<![\w./])10\.[0-9]{{4,9}}/{_TOKEN_CHARS}+)"
    r"|(?P<pmid>\b(?i:pmid)(?::\s?|\s)(?P<pmid_number>[0-9]{1,9})\b)"
    r"|(?P<pmcid>\bPMC[0-9]{4,9}\b)"
)
_CLOSERS = {")": "(", "}": "{"}


def _trim_token(token: str) -> str:
    """Cut a token at a closing parenthesis it never opened, then drop the
    sentence punctuation, emphasis marks and unbalanced closers that end it.

    `(see 10.1016/0005-2744(70)90044-4)` keeps the DOI's own parentheses, and
    `(https://doi.org/10.1/x)` loses the one that closes the sentence's.
    """
    depth = 0
    for index, char in enumerate(token):
        depth += {"(": 1, ")": -1}.get(char, 0)
        if depth < 0:
            token = token[:index]
            break
    while token:
        last = token[-1]
        if last in ".,;:!?*" or (last in _CLOSERS
                                 and token.count(last) > token.count(_CLOSERS[last])):
            token = token[:-1]
            continue
        break
    return token


def _token_url(kind: str, token: str, match: re.Match[str]) -> str | None:
    if kind == "url":
        return _web_url(token)
    if kind == "doi":
        doi = token[token.index("10."):]
        return "https://doi.org/" + quote(doi, safe="/") if "/" in doi else None
    if kind == "pmid":
        return f"https://pubmed.ncbi.nlm.nih.gov/{match.group('pmid_number')}/"
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{token}/"


def autolink(value: object) -> Markup:
    """Escape record prose and link the PMID, PMCID, DOI and http(s) URL tokens in it.

    Only the token becomes the anchor and its visible text is unchanged, so a
    citation in a note, a snippet or a curation event can be followed without
    the sentence around it being reworded. Applied to record content only:
    the schema's own descriptions hold identifiers as format examples.
    """
    if value is None:
        return Markup("")
    if isinstance(value, Markup):
        return value
    text = str(value)
    out: list[str] = []
    position = scan = 0
    while match := _CITATION.search(text, scan):
        kind = match.lastgroup if match.lastgroup != "pmid_number" else "pmid"
        token = match.group(0)
        if kind in {"url", "doi"}:
            token = _trim_token(token)
        url = _token_url(kind, token, match) if token else None
        if not url:
            scan = match.end()
            continue
        out.append(escape(text[position:match.start()]))
        out.append(Markup('<a href="{}">{}</a>').format(url, token))
        # Resume after the token, not the match: what trimming cut off may hold
        # the next citation, as in "(https://a.org/x)-(https://b.org/y)".
        position = scan = match.start() + len(token)
    out.append(escape(text[position:]))
    return Markup("").join(out)


def reference_link(value: object) -> Markup:
    """A cited reference or source value, followable.

    A whole identifier or URL (`PMID:…`, `DOI:…`, `pubchem.aid:…`, a link)
    opens its source; any other text keeps the PMIDs, DOIs and URLs inside it
    followable and is otherwise shown as written.
    """
    if value is None:
        return Markup("")
    text = str(value)
    url = curie_url(text)
    if url:
        return Markup('<a href="{}">{}</a>').format(url, text)
    return autolink(text)


def code_spans(value: str) -> Markup:
    """Markdown-style `code` spans as <code>, everything else escaped."""
    parts = str(value).split("`")
    return Markup("").join(Markup("<code>{}</code>").format(part) if index % 2 else escape(part)
                           for index, part in enumerate(parts))


def template_environment() -> Environment:
    """The renderer's Jinja environment, with the link filters the pages use.

    Tests render templates through this, so a page under test is rendered
    exactly as `just render` renders it.
    """
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)),
                      autoescape=select_autoescape(["html"]),
                      trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)
    env.filters.update(term_link=term_link, reference_link=reference_link,
                       autolink=autolink, code_spans=code_spans)
    return env


def corpus_commit() -> str:
    """The commit the corpus was rendered from, or a marker when unknown.

    Not embedded in a page: a commit id would make every page differ on every
    commit, and `--check` would then be a test of the git history rather than
    of the site. It is printed, for whoever runs the render.
    """
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO_ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def load_records() -> list[tuple[Path, dict[str, Any]]]:
    out = []
    for path in sorted(CORPUS_DIR.rglob("*.yaml")):
        doc = read_natural_product(path)
        if isinstance(doc, dict) and doc.get("identifier"):
            out.append((path, doc))
    return out


def slug_of(path: Path) -> str:
    return path.stem


def measurement(item: dict[str, Any]) -> str:
    value, units = item.get("measurement_value"), item.get("measurement_units")
    kind = item.get("measurement_type") or ""
    if value is None:
        return kind
    return f"{kind} {value:g} {units or ''}".strip()


def first_reference(item: dict[str, Any]) -> str:
    for evidence in item.get("evidence") or []:
        if evidence.get("reference"):
            return evidence["reference"]
    return ""


def references(item: dict[str, Any]) -> list[str]:
    return [
        evidence["reference"]
        for evidence in item.get("evidence") or []
        if evidence.get("reference")
    ]


def pathway_endpoints(item: dict[str, Any], singular: str, plural: str) -> list[str]:
    values = item.get(plural) or []
    if isinstance(values, str):
        values = [values]
    if values:
        return list(values)
    return [item[singular]] if item.get(singular) else []


def pathway_endpoint(item: dict[str, Any], singular: str, plural: str) -> str:
    return " + ".join(pathway_endpoints(item, singular, plural)) or "ungrounded"


def _as_utc(value: object) -> datetime | None:
    """A timezone-aware timestamp in UTC; None for anything else."""
    if isinstance(value, datetime):
        moment = value
    else:
        try:
            moment = datetime.fromisoformat(str(value).strip().replace("Z", "+00:00"))
        except ValueError:
            return None
    return moment.astimezone(timezone.utc) if moment.tzinfo else None


def _stamp(value: object) -> str:
    """An event timestamp as the record writes it: ISO-8601 UTC, Z-suffixed."""
    moment = _as_utc(value)
    return moment.strftime("%Y-%m-%dT%H:%M:%SZ") if moment else str(value or "")


def curation_history(doc: dict[str, Any]) -> list[dict[str, Any]]:
    """The record's curation events, newest first, as the record states them.

    A re-seed that changed nothing is recorded each time it ran, so a run of
    consecutive SEEDED_FROM_SOURCES events with the same curator and the same
    change note is shown once, with how many there were and when the run began.
    Nothing else is merged, and nothing is reworded.
    """
    runs: list[dict[str, Any]] = []
    for event in doc.get("curation_history") or []:
        if not isinstance(event, dict):
            continue
        stamp = _stamp(event.get("timestamp"))
        last = runs[-1] if runs else None
        if (last and event.get("action") == "SEEDED_FROM_SOURCES"
                and all(last["event"].get(key) == event.get(key)
                        for key in ("action", "curator", "changes"))):
            last["count"] += 1
            last["timestamp"] = stamp
            continue
        runs.append({"event": event, "count": 1, "first": stamp, "timestamp": stamp})
    return [{**run["event"], "timestamp": run["timestamp"], "first": run["first"],
             "count": run["count"]} for run in reversed(runs)]


def record_href(doc: dict[str, Any], path: Path) -> str:
    """The record page's path below pages/, as build() writes it."""
    return f"{str(doc.get('np_pathway') or 'UNCLASSIFIED').lower()}/{slug_of(path)}.html"


def source_concept_url(concept: dict[str, Any]) -> str | None:
    """A source concept's page. MIBiG writes its accessions without a prefix."""
    source_id = str(concept.get("source_id") or "")
    if ":" not in source_id and concept.get("source") == "MIBIG":
        source_id = f"mibig:{source_id}"
    return curie_url(source_id)


def search_identifiers(doc: dict[str, Any]) -> list[str]:
    """Presentation aliases from the record; no identity or map changes."""
    return list(dict.fromkeys(filter(None, [doc["identifier"],
        (doc.get("chemical_structure") or {}).get("standard_inchi_key"),
        *(doc.get("xrefs") or []),
        *(s.get("source_id") for s in doc.get("source_concepts") or [])])))


# --- sibling Mechs -------------------------------------------------------------
#: The sibling routes a page may use, each verified live on 2026-10-25 (HTTP 200,
#: and the query restored into the sibling's search with a filtered count).
#: A guessed route is how every Explore-across-X-Mech tag came to 404; the
#: tests hold every emitted sibling URL to these prefixes.
SIBLING_SEARCH = {
    "AntibioticMech": "https://culturebotai.github.io/AntibioticMech/pages/browse.html?q=",
    "MediaIngredientMech": "https://culturebotai.github.io/MediaIngredientMech/browser.html?q=",
    "PathwayMech": "https://culturebotai.github.io/PathwayMech/pages/browse.html?q=",
}
#: Specific-record routes: TaxonMech opens one taxon (and says so when the taxon
#: is outside its published scope); PathwayMech names a record page after its
#: identifier; AntibioticMech files a record under its class directory.
TAXONMECH_TAXON = "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id="
PATHWAYMECH_RECORDS = "https://culturebotai.github.io/PathwayMech/pages/records/"
ANTIBIOTICMECH_PAGES = "https://culturebotai.github.io/AntibioticMech/pages/"
#: AntibioticMech's class -> directory map, as its scripts/seed_from_sources.py
#: CLASS_DIRS states it at the pinned corpus commit (conf/sibling_pins.yaml).
#: Not the lowercased class name: ANTIMICROBIAL_UNSPECIFIED is filed under
#: unspecified/, and lowercasing sent all 50 of those links to a 404 (#986).
ANTIBIOTICMECH_CLASS_DIRS = {
    "ANTIBACTERIAL": "antibacterial",
    "ANTIMYCOBACTERIAL": "antimycobacterial",
    "ANTIFUNGAL": "antifungal",
    "ANTIPROTOZOAL": "antiprotozoal",
    "ANTIVIRAL": "antiviral",
    "BIOCIDE": "biocide",
    "ANTIMICROBIAL_UNSPECIFIED": "unspecified",
    "OTHER": "other",
}
_NCBI_TAXON = re.compile(r"NCBITaxon:[0-9]+")


def _pinned_rows(name: str) -> dict[str, list[dict[str, str]]]:
    result: dict[str, list[dict[str, str]]] = {}
    source = REPO_ROOT / "data" / "raw" / name
    if source.exists():
        with source.open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream, delimiter="\t"):
                result.setdefault(row["identifier"], []).append(row)
    return result


@lru_cache(maxsize=1)
def antibiotic_routes() -> dict[str, list[dict[str, str]]]:
    """Use the target's routes in the already pinned structure-join inventory."""
    return _pinned_rows("antibioticmech_inchikeys.tsv")


@lru_cache(maxsize=1)
def pathway_routes() -> dict[str, list[dict[str, str]]]:
    """The PathwayMech records the pinned product inventory names."""
    return _pinned_rows("pathwaymech_products.tsv")


def _pinned(rows: list[dict[str, str]], link: dict[str, Any], structure: dict[str, Any]) -> list:
    """Rows for this exact structure at the link's pinned sibling commit."""
    return [r for r in rows
            if r["standard_inchi_key"] == structure.get("standard_inchi_key")
            and r["corpus_commit"].startswith(link.get("source_version") or "")]


def related_link(link: dict[str, Any], structure: dict[str, Any]) -> dict[str, Any]:
    """A sibling record link, given a URL only where the pinned inventory proves it.

    The URL comes from the sibling's own route for the exact structure at the
    pinned commit, never from the identifier alone; without that proof the
    entry stays text.
    """
    result = dict(link)
    if link.get("corpus") == "AntibioticMech":
        rows = _pinned(antibiotic_routes().get(link.get("identifier"), []), link, structure)
        routes = {(ANTIBIOTICMECH_CLASS_DIRS.get(r["antimicrobial_class"]), r["slug"]) for r in rows}
        if len(routes) == 1:
            category, slug = next(iter(routes))
            if category:
                result["url"] = (f"{ANTIBIOTICMECH_PAGES}"
                                 f"{quote(category, safe='')}/{quote(slug, safe='')}.html")
    elif link.get("corpus") == "PathwayMech":
        if _pinned(pathway_routes().get(link.get("identifier"), []), link, structure):
            # PathwayMech names a record page after its identifier, with ':'
            # and '/' replaced by '_' (#987).
            page = str(link["identifier"]).replace(":", "_").replace("/", "_")
            result["url"] = f"{PATHWAYMECH_RECORDS}{quote(page, safe='')}.html"
    return result


def sibling_links(doc: dict[str, Any], producers: list[dict[str, Any]],
                  clusters: list[dict[str, Any]]) -> list[dict[str, str]]:
    """The record's hand-offs to sibling Mechs, each on a verified route.

    AntibioticMech is searched by the Standard InChIKey, which its browse
    indexes. MediaIngredientMech is searched only for a ChEBI identity, the
    identifier its browser matches; no sibling can answer this corpus's minted
    identifiers, so those records get no MediaIngredientMech search. A producer
    taxon opens TaxonMech's taxon route, and a gene cluster is searched in
    PathwayMech by its MIBiG accession, which PathwayMech's browse indexes.
    """
    label = doc.get("label", "")
    identifier = doc["identifier"]
    links = []
    inchi_key = (doc.get("chemical_structure") or {}).get("standard_inchi_key")
    if inchi_key:
        links.append({"text": f"AntibioticMech ({label})",
                      "url": SIBLING_SEARCH["AntibioticMech"] + quote(inchi_key, safe="")})
    if identifier.startswith("CHEBI:"):
        links.append({"text": f"MediaIngredientMech ({identifier})",
                      "url": SIBLING_SEARCH["MediaIngredientMech"] + quote(identifier, safe="")})
    taxa: dict[str, str] = {}
    for producer in producers:
        taxon = producer.get("taxon_id") or ""
        if _NCBI_TAXON.fullmatch(taxon):
            taxa.setdefault(taxon, producer.get("taxon_label") or taxon)
    for taxon, taxon_label in list(taxa.items())[:4]:
        links.append({"text": f"TaxonMech: {taxon_label} ({taxon})",
                      "url": TAXONMECH_TAXON + quote(taxon, safe="")})
    accessions = dict.fromkeys(c["accession"] for c in clusters if c.get("accession"))
    for accession in list(accessions)[:3]:
        local = str(accession).split(":", 1)[-1]
        links.append({"text": f"PathwayMech ({accession})",
                      "url": SIBLING_SEARCH["PathwayMech"] + quote(local, safe="")})
    return links


def build_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    producers = []
    for p in doc.get("producer_organisms") or []:
        producers.append({**p, "causal": p.get("evidence_basis") in CAUSAL_BASES,
                          "evidence": p.get("evidence") or [],
                          "references": list(dict.fromkeys(references(p)))})
    occurrences = []
    for o in doc.get("occurrences") or []:
        occurrences.append({**o, "reference": first_reference(o)})
    clusters = []
    for c in doc.get("biosynthetic_gene_clusters") or []:
        clusters.append({**c, "demonstrated": c.get("link_evidence_basis") == "CLUSTER_DEMONSTRATED"})
    targets = []
    for t in doc.get("molecular_targets") or []:
        targets.append({**t, "measurement": measurement(t), "reference": first_reference(t)})
    bioactivities = []
    seen_bioactivities: set[str] = set()
    duplicate_bioactivities = 0
    for b in doc.get("bioactivities") or []:
        # Full source equality only: a missing target, changed condition, or
        # different evidence makes a distinct entry even if its value matches.
        key = json.dumps(b, sort_keys=True, ensure_ascii=False)
        if key in seen_bioactivities:
            duplicate_bioactivities += 1
            continue
        seen_bioactivities.add(key)
        measured = measurement({
            "measurement_type": b.get("measurement_type"),
            "measurement_value": b.get("value"),
            "measurement_units": b.get("units"),
        })
        result = "; ".join(part for part in (measured, b.get("call")) if part)
        bioactivities.append({"assay": b.get("assay", ""), "result": result,
                              "reference": first_reference(b), "source": b,
                              "target": b.get("target_enzyme") or "Not recorded"})
    steps = []
    for s in doc.get("biosynthetic_pathway") or []:
        steps.append({
            **s,
            "reference": first_reference(s),
            "substrate_display": pathway_endpoint(s, "substrate", "substrates"),
            "product_display": pathway_endpoint(s, "product", "products"),
            "substrate_ids": pathway_endpoints(s, "substrate", "substrates"),
            "product_ids": pathway_endpoints(s, "product", "products"),
        })
    graphs = []
    for g in doc.get("causal_graphs") or []:
        labels = {n.get("node_id"): n.get("label", n.get("node_id", ""))
                  for n in g.get("nodes") or []}
        edges = [{**e,
                  "subject_label": labels.get(e.get("subject"), e.get("subject", "")),
                  "object_label": labels.get(e.get("object"), e.get("object", "")),
                  "references": references(e)}
                 for e in g.get("edges") or []]
        graphs.append({**g, "edges": edges})

    href = record_href(doc, path)
    # A prefilled issue names the record and the page it was reported from.
    report = urlencode({"title": f"Problem with {doc['identifier']}", "body": SITE_BASE + href},
                       quote_via=quote)
    return {
        "label": doc.get("label", ""),
        "identifier": doc["identifier"],
        "slug": slug_of(path),
        "href": href,
        "issue_url": f"{REPO_URL}/issues/new?{report}",
        "synonyms": [s["value"] for s in doc.get("synonyms") or []],
        "definition": doc.get("definition"),
        "grounding_status": doc.get("grounding_status", ""),
        "grounding_note": doc.get("grounding_notes"),
        "search_identifiers": search_identifiers(doc),
        "curation_status": doc.get("curation_status", ""),
        "bioactivity_summary": doc.get("bioactivity_summary") or [],
        "structure": doc.get("chemical_structure") or {},
        "xrefs": doc.get("xrefs") or [],
        "pathway_title": PATHWAY_TITLES.get(doc.get("np_pathway", ""), doc.get("np_pathway", "")),
        "classification": doc.get("np_classification"),
        "bgc_class": doc.get("bgc_class") or [],
        "producers": producers,
        "occurrences": occurrences,
        # The record caps what it carries; say so rather than implying the
        # inventories hold no more (#28).
        "occurrences_capped": None,
        "clusters": clusters,
        "targets": targets,
        "bioactivities": bioactivities,
        "bioactivity_duplicates": duplicate_bioactivities,
        "bioactivity_total": len(bioactivities),
        "related": [related_link(link, doc.get("chemical_structure") or {})
                    for link in doc.get("related_records") or []],
        "sibling_links": sibling_links(doc, producers, clusters),
        "discussions": [{**d, "status": d.get("status") or "OPEN"}
                        for d in doc.get("discussions") or []
                        if (d.get("status") or "OPEN") == "OPEN"],
        "pathway_steps": steps,
        "graphs": graphs,
        "source_concepts": [{**s, "url": source_concept_url(s)}
                            for s in doc.get("source_concepts") or []],
        "history": curation_history(doc),
        # The record page's own date: when this record last changed, never
        # the corpus's, so curating one record leaves every other page alone.
        "updated": latest_event(doc.get("curation_history") or []),
        "record_path": str(path.relative_to(REPO_ROOT)),
        "causal": sum(1 for p in producers if p["causal"]),
        "weak": sum(1 for p in producers if not p["causal"]),
        "n_occurrences": len(occurrences),
        "n_clusters": len(clusters),
    }


def join_text_map(artifact: dict[str, Any], hrefs: dict[str, str]) -> dict[str, Any]:
    """Only show extant owners; never retag an old identity's text embedding."""
    points = [point for point in artifact["points"] if point[3] in hrefs]
    return {
        **artifact,
        "points": points,
        "n": len(points),
        "hrefs": {point[3]: hrefs[point[3]] for point in points},
    }


def load_chemical_map(record_ids: set[str]) -> dict[str, Any] | None:
    """The committed structure-map artifact, or None when it has not been built.

    Checked against the live corpus rather than trusted: an artifact naming a
    different record set would draw a map of a corpus that no longer exists,
    and the page gives no hint that anything is stale. Absent is fine and the
    map page is skipped — `just chemical-map` is a separate, heavier step than
    `just render`.
    """
    if not CHEMICAL_MAP_ARTIFACT.exists():
        return None
    artifact = json.loads(CHEMICAL_MAP_ARTIFACT.read_text(encoding="utf-8"))
    rows = artifact.get("records")
    if not isinstance(rows, list):
        raise SystemExit(f"{CHEMICAL_MAP_ARTIFACT}: records must be a list")
    map_ids = {row.get("identifier") for row in rows if isinstance(row, dict)}
    if map_ids != record_ids or len(rows) != len(record_ids):
        raise SystemExit(
            f"{CHEMICAL_MAP_ARTIFACT.relative_to(REPO_ROOT)} names a different record "
            f"set than the corpus ({len(rows)} vs {len(record_ids)}); "
            f"regenerate with `just chemical-map`"
        )
    return artifact


def corpus_digest(records: list[tuple[Path, dict[str, Any]]]) -> str:
    """SHA-256 over every record as the site reads it, graph components included.

    It is the footer's version of the corpus, so it moves whenever a record's
    content does. It used to hash file name, identifier and InChIKey only, and
    stayed the same through every curation that changed what a page says.
    Canonical JSON, so the digest follows content rather than YAML layout.
    """
    h = hashlib.sha256()
    for path, doc in records:
        h.update(f"{path.name}\0".encode())
        h.update(json.dumps(doc, sort_keys=True, ensure_ascii=False, default=str).encode())
        h.update(b"\n")
    return h.hexdigest()[:12]


def latest_event(events: list[Any]) -> str:
    """The latest of some curation events, as "YYYY-MM-DD HH:MM UTC".

    Read from the records, never from the clock, so rendering an unchanged
    corpus twice gives the same bytes and `--check` stays a test of the site.
    Empty when no event carries a usable timestamp: there is then no date to
    claim.
    """
    moments = [_as_utc(event.get("timestamp")) for event in events if isinstance(event, dict)]
    known = [moment for moment in moments if moment is not None]
    return max(known).strftime("%Y-%m-%d %H:%M UTC") if known else ""


def corpus_as_of(records: list[tuple[Path, dict[str, Any]]]) -> str:
    """The latest curation event across the corpus: the aggregate pages' date."""
    return latest_event([event for _, doc in records
                         for event in doc.get("curation_history") or []])


#: How the corpus is produced, quoted from README.md's status section rather
#: than paraphrased, so the site never claims more about curation than the
#: repository does. A test holds the quote to the README.
PRODUCTION_QUOTE = (
    "The corpus reproduces offline from committed inventories: MIBiG (structures, "
    "producers, gene clusters), ChEBI (grounding, origins), LOTUS and CyanoMetDB "
    "(cited occurrences), NCBI Taxonomy (name resolution), NPClassifier (the filing "
    "pathway), PubChem BioAssay and BindingDB (measured activities and targets), and "
    "AntibioticMech (antimicrobial classification and cross-corpus links). Every "
    "record remains `SEEDED` until a curator signs off identity, structure, filing "
    "class, and producer claims; partial `biosynthetic_pathway` and `causal_graphs` "
    "curation is now underway."
)


def curation_summary(records: list[tuple[Path, dict[str, Any]]],
                     statuses: list[dict[str, str]]) -> dict[str, Any]:
    """What the records themselves say about how they were produced.

    Every status the schema defines, with its definition and how many records
    carry it, and every curator named in a curation event with its event count.
    Curators are listed as the records name them, never classified here.
    """
    by_status = Counter(doc.get("curation_status") for _, doc in records)
    curators: Counter[str] = Counter()
    llm_assisted = 0
    for _, doc in records:
        for event in doc.get("curation_history") or []:
            if isinstance(event, dict):
                curators[str(event.get("curator") or "unrecorded")] += 1
                llm_assisted += 1 if event.get("llm_assisted") else 0
    return {
        "statuses": [{**status, "count": by_status.get(status["text"], 0)} for status in statuses],
        "curators": sorted(curators.items(), key=lambda item: (-item[1], item[0])),
        "events": sum(curators.values()),
        "llm_assisted": llm_assisted,
    }


def schema_reference(schema_path: Path = SCHEMA_PATH) -> dict[str, Any]:
    """Readable documentation of the record schema, read from the schema itself.

    The site linked only the raw YAML. This is what LinkML resolves instead:
    every class with its induced slots (imports and slot usage applied) and
    every enum with its permissible values, in the schema's own declaration
    order and with no clock, so an unchanged schema renders byte-identically
    under `--check`.
    """
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(schema_path))
    view.imports_closure()
    module_file = {}
    for name, schema in view.schema_map.items():
        source = schema_path.parent / f"{name}.yaml"
        if source.exists():
            module_file[schema.id] = source.relative_to(REPO_ROOT).as_posix()
    classes = view.all_classes()
    enums = view.all_enums()
    local = list(view.all_classes(imports=False))
    ordered = local + [name for name in classes if name not in local]

    def range_kind(name: str | None) -> str:
        if name in classes:
            return "class"
        if name in enums:
            return "enum"
        return "type"

    def slot_row(slot: Any) -> dict[str, Any]:
        names = [alt.range for alt in (slot.any_of or slot.exactly_one_of or []) if alt.range]
        ranges = names or [slot.range or view.schema.default_range or "string"]
        return {
            "name": slot.name,
            "ranges": [{"name": name, "kind": range_kind(name)} for name in ranges],
            "required": bool(slot.required or slot.identifier),
            "multivalued": bool(slot.multivalued),
            "identifier": bool(slot.identifier),
            "pattern": slot.pattern or "",
            "description": slot.description or "",
        }

    return {
        "title": view.schema.title or view.schema.name,
        "description": view.schema.description or "",
        "license": view.schema.license or "",
        "source": schema_path.relative_to(REPO_ROOT).as_posix(),
        "modules": sorted(set(module_file.values())),
        "classes": [{
            "name": name,
            "description": classes[name].description or "",
            "is_a": classes[name].is_a or "",
            "source": module_file.get(classes[name].from_schema, ""),
            "slots": [slot_row(slot) for slot in view.class_induced_slots(name)],
        } for name in ordered],
        "enums": [{
            "name": name,
            "description": enum.description or "",
            "source": module_file.get(enum.from_schema, ""),
            "permissible": [{"text": text, "description": value.description or "",
                             "meaning": value.meaning or ""}
                            for text, value in (enum.permissible_values or {}).items()],
        } for name, enum in enums.items()],
    }


def enum_values(schema: dict[str, Any], name: str) -> list[dict[str, str]]:
    """An enum's permissible values with their descriptions, as the schema states them."""
    return next((enum["permissible"] for enum in schema["enums"] if enum["name"] == name), [])


def build(out_dir: Path) -> tuple[int, int]:
    env = template_environment()
    records = load_records()
    digest = corpus_digest(records)
    gen_on = retrieved_on()
    provenance = f"{len(records)} records · {gen_on} · corpus SHA-256 {digest}"
    # The aggregate pages' footer: the dated version of the corpus they list.
    # Record pages and the not-found page never carry it. A corpus-wide date,
    # count or digest on every record page would rewrite all of them on each
    # curation commit, and every concurrent record PR would conflict on them;
    # a record page states when its own record last changed instead.
    common = {"build_provenance": provenance, "corpus_as_of": corpus_as_of(records)}
    schema = schema_reference()
    statuses = enum_values(schema, "CurationStatusEnum")
    status_meanings = {value["text"]: value["description"] for value in statuses}
    by_pathway: dict[str, list[dict[str, Any]]] = {}
    coverage: Counter[str] = Counter()
    producer_claims = causal_claims = occurrence_records = 0

    for path, doc in records:
        built = build_record(path, doc)
        by_pathway.setdefault(doc.get("np_pathway", "UNCLASSIFIED"), []).append(built)
        for field in COVERAGE_FIELDS:
            if doc.get(field):
                coverage[field] += 1
        producer_claims += len(built["producers"])
        causal_claims += built["causal"]
        occurrence_records += 1 if built["occurrences"] else 0

    label_counts = Counter(doc.get("label", "").casefold() for _, doc in records)
    for items in by_pathway.values():
        for item in items:
            item["duplicate_label"] = label_counts[item["label"].casefold()] > 1

    pathways = []
    for key in PATHWAY_TITLES:
        items = sorted(by_pathway.get(key, []), key=lambda r: (r["label"].lower(), r["identifier"]))
        if not items:
            continue
        pathways.append({
            "key": key, "slug": key.lower(), "title": PATHWAY_TITLES[key],
            "blurb": PATHWAY_BLURBS.get(key, ""), "count": len(items), "records": items,
        })
    # Every published record's page, below pages/: what an identifier naming
    # one of this corpus's records links to.
    href_by_identifier = {
        record["identifier"]: f"{pathway['slug']}/{record['slug']}.html"
        for pathway in pathways for record in pathway["records"]
    }

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    shutil.copyfile(TEMPLATES_DIR / "style.css", out_dir / "style.css")
    if (TEMPLATES_DIR / "theme-toggle.js").exists():
        shutil.copyfile(TEMPLATES_DIR / "theme-toggle.js", out_dir / "theme-toggle.js")

    # conf/sources.yaml is a mapping of source key -> config at the top level,
    # alongside a couple of non-source settings. Counting its keys blindly
    # would report `producer_scope` as a data source.
    sources_path = REPO_ROOT / "conf" / "sources.yaml"
    source_count = 0
    if sources_path.exists():
        conf = yaml.safe_load(sources_path.read_text(encoding="utf-8")) or {}
        source_count = sum(1 for value in conf.values()
                           if isinstance(value, dict) and "license" in value)

    (out_dir / "index.html").write_text(env.get_template("index.html").render(
        root="", total=len(records), source_count=source_count, pathways=pathways,
        coverage=[(f, coverage.get(f, 0)) for f in COVERAGE_FIELDS],
        generated_on=gen_on,
        stats={"producer_claims": producer_claims, "causal": causal_claims,
               "occurrence_records": occurrence_records},
        production_quote=PRODUCTION_QUOTE,
        curation=curation_summary(records, statuses),
        **common,
    ), encoding="utf-8")
    (out_dir / "browse.html").write_text(env.get_template("browse.html").render(
        root="", total=len(records), pathways=pathways, **common), encoding="utf-8")
    (out_dir / "schema.html").write_text(env.get_template("schema.html").render(
        root="", schema=schema, repo_url=REPO_URL, **common), encoding="utf-8")
    (out_dir / "404.html").write_text(env.get_template("not_found.html").render(
        root=SITE_BASE), encoding="utf-8")

    # The corpus map, when its JSON has been built. Committed and small, so the
    # site renders it whenever it is there and skips it otherwise — a checkout
    # where `just embed-map` has never run gets no half-drawn page.
    corpus_map_path = REPO_ROOT / "data" / "embeddings" / "corpus_map.json"
    if corpus_map_path.exists():
        artifact = json.loads(corpus_map_path.read_text(encoding="utf-8"))
        corpus_map = join_text_map(artifact, href_by_identifier)
        # The map is computed apart from the pages, so it can lag the corpus.
        # The page names what it leaves out instead of drawing fewer points
        # than the site counts without a word.
        plotted = set(corpus_map["hrefs"])
        unplotted = [{"label": record["label"], "identifier": record["identifier"],
                      "href": href_by_identifier[record["identifier"]]}
                     for pathway in pathways for record in pathway["records"]
                     if record["identifier"] not in plotted]
        (out_dir / "map.html").write_text(
            env.get_template("map.html").render(
                root="", map=corpus_map, total=len(href_by_identifier),
                unplotted=sorted(unplotted, key=lambda item: item["identifier"]),
                dropped=len(artifact["points"]) - len(corpus_map["points"]),
                # Embedded as JSON in a <script> tag, so the two characters
                # that would end it early are escaped.
                map_json=json.dumps(corpus_map, separators=(",", ":"))
                .replace("<", "\\u003c").replace("\u2028", "\\u2028")
                .replace("\u2029", "\\u2029"),
                **common),
            encoding="utf-8")

    # The structure map, when its artifact has been built. Skipped rather than
    # half-drawn: `just chemical-map` needs RDKit and UMAP, which `just render`
    # does not, so a checkout that has never run it still renders a whole site.
    chemical_map = load_chemical_map({doc["identifier"] for _, doc in records})
    if chemical_map is not None:
        (out_dir / "chemical-map.html").write_text(
            env.get_template("chemical_map.html").render(
                root="", quality=chemical_map["quality"],
                model_version=chemical_map["model_version"],
                total=len(records), **common),
            encoding="utf-8")
        shutil.copyfile(TEMPLATES_DIR / "chemical_map.js", out_dir / "chemical-map.js")
        (out_dir / "data").mkdir(exist_ok=True)
        (out_dir / "data" / "chemical-search.json").write_text(
            json.dumps({doc["identifier"]: search_identifiers(doc) for _, doc in records},
                       ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8")
        shutil.copyfile(CHEMICAL_MAP_ARTIFACT,
                        out_dir / "data" / "chemical-structure-map.json")

    sequence_map_path = REPO_ROOT / "data" / "embeddings" / "sequence_map.json"
    if sequence_map_path.exists():
        seq_map = json.loads(sequence_map_path.read_text(encoding="utf-8"))
        (out_dir / "sequence-map.html").write_text(
            env.get_template("sequence_map.html").render(
                root="", seq_map=seq_map, **common
            ),
            encoding="utf-8",
        )
        (out_dir / "data").mkdir(exist_ok=True)
        shutil.copyfile(sequence_map_path, out_dir / "data" / "sequence_map.json")

    record_template = env.get_template("record.html")
    pathway_template = env.get_template("pathway.html")
    written = 0
    for pathway in pathways:
        directory = out_dir / pathway["slug"]
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "index.html").write_text(
            pathway_template.render(
                root="../", pathway=pathway, **common
            ),
            encoding="utf-8",
        )
        for record in pathway["records"]:
            (directory / f"{record['slug']}.html").write_text(
                record_template.render(root="../", r=record, own_pages=href_by_identifier,
                                       status_meanings=status_meanings),
                encoding="utf-8")
            written += 1
    return written, len(pathways)


def retrieved_on() -> str:
    """The manifest's retrieval date — the corpus's own notion of 'when'.

    Deliberately not today's date: a page that says when it was rendered
    differs on every render and would make `--check` fail for no reason.
    """
    manifest = REPO_ROOT / "data" / "raw" / "MANIFEST.yaml"
    if manifest.exists():
        value = (yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}).get("retrieved_on")
        if value:
            return f"from sources retrieved {value}"
    return "from the committed inventories"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument("--check", action="store_true",
                        help="render to a temporary directory and fail if pages/ differs")
    args = parser.parse_args(argv)

    if not args.check:
        written, pathways = build(args.out)
        if args.out.resolve() == PAGES_DIR.resolve():
            shutil.copyfile(args.out / "404.html", REPO_ROOT / "404.html")
        print(f"rendered {written} record pages across {pathways} pathways "
              f"-> {args.out.relative_to(REPO_ROOT)} (corpus at {corpus_commit()})")
        return 0

    with tempfile.TemporaryDirectory() as tmp:
        expected = Path(tmp) / "pages"
        build(expected)
        if not args.out.exists():
            print("pages/ is not rendered; run `just render`", file=sys.stderr)
            return 1
        differences = _diff(expected, args.out)
        if args.out.resolve() == PAGES_DIR.resolve():
            root_404 = REPO_ROOT / "404.html"
            if not root_404.exists() or root_404.read_bytes() != (expected / "404.html").read_bytes():
                differences.append("../404.html: missing or stale publication-root recovery page")
        if differences:
            print("pages/ is out of step with the corpus:", file=sys.stderr)
            for line in differences[:20]:
                print(f"  {line}", file=sys.stderr)
            if len(differences) > 20:
                print(f"  … and {len(differences) - 20} more", file=sys.stderr)
            print("\nRun `just render` and commit the result.", file=sys.stderr)
            return 1
    print("pages/ is in step with the corpus")
    return 0


def _diff(expected: Path, actual: Path) -> list[str]:
    want = {p.relative_to(expected) for p in expected.rglob("*") if p.is_file()}
    have = {p.relative_to(actual) for p in actual.rglob("*") if p.is_file()}
    out = [f"{p}: expected but not committed" for p in sorted(want - have)]
    out += [f"{p}: committed but not rendered" for p in sorted(have - want)]
    for rel in sorted(want & have):
        if not filecmp.cmp(expected / rel, actual / rel, shallow=False):
            out.append(f"{rel}: differs")
    return out


if __name__ == "__main__":
    raise SystemExit(main())
