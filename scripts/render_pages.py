#!/usr/bin/env python3
"""Render the browsable site under pages/ from data/habitats/.

A corpus of 3,000+ YAML files is not readable by anyone who is not already
running the tooling, which makes the curation backlog invisible to exactly the
people best placed to help with it — ontology curators. The site exists mainly
to publish two things: the records themselves, and the ENVO term-request list.

Generated, committed, and served from `main` at the repo root, matching the
sibling Mech repos. Regenerate with `just render`; CI checks the output is in
step with the corpus, the same way `verify-corpus` does for the records.

Usage:
    python3 scripts/render_pages.py
    python3 scripts/render_pages.py --out /tmp/site --check
"""

from __future__ import annotations

import argparse
import csv
import filecmp
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import quote, urlencode, urlsplit

import yaml
from jinja2 import Environment, FileSystemLoader, pass_context, select_autoescape
from markupsafe import Markup, escape

if __package__:
    from .build_term_requests import excluded as excluded_term_requests
    from .mechanism_graph import graph_svg
else:
    from build_term_requests import excluded as excluded_term_requests
    from mechanism_graph import graph_svg

from habitatmech.text_map_site import PreparedTextMap, prepare_text_map

REPO_ROOT = Path(__file__).resolve().parent.parent
HABITATS_DIR = REPO_ROOT / "data" / "habitats"
TEMPLATES_DIR = REPO_ROOT / "src" / "habitatmech" / "templates"
PAGES_DIR = REPO_ROOT / "pages"
DECISIONS_PATH = REPO_ROOT / "curation" / "decisions.tsv"
MANIFEST_PATH = REPO_ROOT / "data" / "raw" / "MANIFEST.yaml"
SCHEMA_PATH = REPO_ROOT / "src" / "habitatmech" / "schema" / "habitatmech.yaml"
GITHUB_REPO = "https://github.com/CultureBotAI/HabitatMech"

# Per-record taxon lists are capped in the extractor at 25; showing all of them
# on the page is fine, but the cap is worth naming where a reader sees it.
TAXA_SHOWN = 25

# Where the site is served from; the sitemap needs absolute URLs.
SITE_BASE = "https://culturebotai.github.io/HabitatMech/pages/"

# Rows per category page. 300 keeps the biggest category near 90 KB instead of
# 461 KB; the filter still searches the whole category via the JSON index.
CATEGORY_PAGE_SIZE = 300

CATEGORY_BLURB = {
    "TERRESTRIAL": "Soils, sediments, subsurface, rock and other land environments.",
    "AQUATIC": "Marine, freshwater and other water-column or aquatic-sediment environments.",
    "AIR": "Atmospheric and aerosol environments.",
    "HOST_ASSOCIATED": "Habitats defined by a living host, including anatomical sites.",
    "ENGINEERED": "Built or managed environments: bioreactors, wastewater, industry.",
    "FOOD": "Food and beverage matrices, including fermented products.",
    "CLINICAL": "Clinical and diagnostic sample contexts.",
    "OTHER": "Records the category heuristic could not place.",
}

GROUNDING_MEANING = {
    "EXACT": "The identifier is an exact match for the source concept.",
    "CLOSE": "Close, but not exact and not cleanly broader or narrower.",
    "NARROW": "The identifier is narrower than the source concept.",
    "BROAD": "The identifier is broader — the best available term, losing specificity.",
    "UNGROUNDED": "No defensible ontology term; a minted identifier and a term-request candidate.",
    "NOT_APPLICABLE": "Not a habitat at all — a disease, quality, process or procedure.",
}

OBO_PREFIXES = {
    "BTO",
    "CEPH",
    "CHEBI",
    "ENVO",
    "FOODON",
    "GO",
    "HAO",
    "NCBITaxon",
    "NCIT",
    "PATO",
    "PO",
    "UBERON",
}


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-") or "unnamed"


def _trim_category_prefix(path: str, category: str) -> str:
    """Drop the leading path segment only when it restates the category.

    Trimming unconditionally looked like a free saving and was not: GOLD's top
    level (Environmental / Host-associated / Engineered) is a different axis
    from habitat_category, so 707 rows lost a branch the reader needs — on a
    page that says the path is shown precisely because the label is only its
    last step (#66).
    """
    head, sep, tail = path.partition(" > ")
    if not sep or not tail:
        return path
    return tail if head.upper().replace("-", "_").replace(" ", "_") == category else path


def _slice_labels() -> list[dict]:
    """Labels for the vendored ontology slice. Empty when it is absent, so the
    site still renders from a corpus alone."""
    path = REPO_ROOT / "data" / "raw" / "ontology_terms.tsv"
    if not path.exists():
        return []
    import csv as _csv
    with path.open(newline="", encoding="utf-8") as fh:
        return list(_csv.DictReader(fh, delimiter="\t"))


def term_iri(curie: str) -> str | None:
    prefix, _, local = curie.partition(":")
    if prefix.lower() == "mesh" and re.fullmatch(r"[DC]\d+", local):
        return f"https://id.nlm.nih.gov/mesh/{local}.html"
    if prefix == "UniProtKB" and local:
        return f"https://www.uniprot.org/uniprotkb/{local}/entry"
    if prefix in OBO_PREFIXES:
        return f"http://purl.obolibrary.org/obo/{prefix}_{local}"
    return None


# A CURIE as a reader sees one: a prefix, a colon, then a local id with no
# space or markup in it.
CURIE_SHAPE = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*:[^\s<>\"'`\\]+")
# This repository's own namespace. No registry resolves it, so a habitatmech:
# identifier is linkable only through the record page it names.
LOCAL_PREFIX = "habitatmech"


def curie_url(curie: str) -> str | None:
    """Where a displayed identifier is looked up, when no record page names it.

    Known prefixes use term_iri(). Any other well-formed CURIE falls back to
    bioregistry.io, which resolves or explains every registered prefix, so a
    displayed identifier is never a dead end; a habitatmech: identifier with no
    record page has nowhere to go and stays unlinked.
    """
    value = (curie or "").strip()
    if not CURIE_SHAPE.fullmatch(value):
        return None
    known = term_iri(value)
    if known:
        return known
    if value.partition(":")[0] == LOCAL_PREFIX:
        return None
    return "https://bioregistry.io/" + quote(value, safe=":/")


# The sibling Mech routes this site links, from the fleet's route table, which
# was loaded live in headless Chrome on 2026-10-25: each search route restored
# ?q= into its search box with a filtered count. A per-taxon link uses
# TaxonMech's record route, which opens that taxon (or says it is outside
# TaxonMech's published scope) rather than a label search.
SIBLING_SEARCH = {
    "TaxonMech": "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=",
    "CommunityMech": "https://culturebotai.github.io/CommunityMech/browser.html?q=",
    "CultureMech": "https://culturebotai.github.io/CultureMech/app/browser.html?q=",
    "TraitMech": "https://culturebotai.github.io/TraitMech/pages/browse.html?q=",
}
TAXONMECH_RECORD = "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id="


def sibling_search(mech: str, query: str) -> str:
    return SIBLING_SEARCH[mech] + quote(query, safe="")


def taxonmech_url(taxon_id: str) -> str | None:
    if not re.fullmatch(r"NCBITaxon:\d+", taxon_id or ""):
        return None
    return TAXONMECH_RECORD + quote(taxon_id, safe="")


# Citation tokens inside record prose. URLs come first so that a DOI inside a
# URL stays part of that URL, and a known-prefix CURIE comes last so that
# "DOI:10.1/x" and "PMID:1" are read as citations. Matching runs on the raw
# text and every piece is escaped on the way out, so record text never becomes
# markup. A URL or DOI never contains whitespace, angle brackets, quotes,
# backticks or square brackets, so Markdown written around one --
# `[10.1/x](https://...)`, `10.1/x` in backticks -- ends the token instead of
# joining it. Only prefixes this site already resolves are recognised as CURIEs
# in prose, where "word:word" is otherwise just punctuation.
_TOKEN_CHARS = r"[^\s<>\"'`\\\[\]]"
_PROSE_PREFIXES = sorted(OBO_PREFIXES | {"UniProtKB", "mesh", "MESH", "MeSH", LOCAL_PREFIX})
CITATION_TOKEN = re.compile(
    rf"(?P<url>\b(?i:https?)://{_TOKEN_CHARS}+)"
    rf"|(?P<doi>(?:\b(?i:doi)(?::\s?|=|\s))?(?<![\w./])10\.[0-9]{{4,9}}/{_TOKEN_CHARS}+)"
    r"|(?P<pmid>\b(?i:pmid)(?::\s?|\s)(?P<pmid_number>[0-9]{1,9})\b)"
    r"|(?P<pmcid>\bPMC[0-9]{4,9}\b)"
    rf"|(?P<curie>\b(?:{'|'.join(_PROSE_PREFIXES)}):[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*)"
)
_CLOSERS = {")": "(", "]": "[", "}": "{"}
# Sentence punctuation, plus the Markdown emphasis and code marks that close a
# token written as **10.x/y** or `10.x/y`.
_TRAILING = ".,;:!?'\"*`"


def _trim_token(token: str) -> str:
    """Cut a token at a closing parenthesis it never opened, then drop the
    punctuation, Markdown marks and unbalanced closers that end it.

    "(10.1016/0005-2744(70)90044-4)" keeps the DOI's own parentheses, while in
    "(https://a.org/x)-(https://b.org/y)" the first ")" closes the sentence's
    parenthesis, so the token ends there and the second URL is its own.
    Without this a note's "(https://.../issues/1948);" linked the issue with
    ");" on the end, which GitHub answers with an empty search (#2046).
    """
    depth = 0
    for index, char in enumerate(token):
        depth += {"(": 1, ")": -1}.get(char, 0)
        if depth < 0:
            token = token[:index]
            break
    while token:
        last = token[-1]
        if last in _TRAILING or (last in _CLOSERS
                                 and token.count(last) > token.count(_CLOSERS[last])):
            token = token[:-1]
            continue
        break
    return token


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


def _record_href(root: str, slug_of: dict[str, str], curie: str) -> str | None:
    slug = slug_of.get(curie)
    return f"{root}habitats/{slug}.html" if slug else None


def _token_url(kind: str, token: str, match: re.Match[str], root: str,
               slug_of: dict[str, str], own: str) -> str | None:
    if kind == "url":
        return _web_url(token)
    if kind == "doi":
        doi = token[token.index("10."):]
        return "https://doi.org/" + quote(doi, safe="/") if "/" in doi else None
    if kind == "pmid":
        return f"https://pubmed.ncbi.nlm.nih.gov/{match.group('pmid_number')}/"
    if kind == "pmcid":
        return f"https://pmc.ncbi.nlm.nih.gov/articles/{token}/"
    if token == own:
        return None  # the page the reader is already on
    return _record_href(root, slug_of, token) or term_iri(token)


def autolink_text(value: object, *, root: str = "", slug_of: dict[str, str] | None = None,
                  own: str = "") -> Markup:
    """Escape record prose and link the citations and identifiers in it.

    PMID -> PubMed, DOI -> doi.org, PMCID -> PMC, http(s) URLs -> themselves,
    and a known-prefix CURIE -> the record page that has it as its identifier,
    else its resolver (`own`, the current record's identifier, stays unlinked).
    Only the token becomes the anchor and its visible text is unchanged, so a
    citation inside an evidence note, an edge description or a curation change
    can be followed without the sentence being reworded. For record content
    only: schema and documentation prose carries format examples such as
    PMID:12345678 that must stay plain text.
    """
    if value is None:
        return Markup("")
    if isinstance(value, Markup):
        return value
    text = str(value)
    slug_of = slug_of or {}
    out: list[str] = []
    position = scan = 0
    while match := CITATION_TOKEN.search(text, scan):
        kind = match.lastgroup if match.lastgroup != "pmid_number" else "pmid"
        token = match.group(0)
        if kind in {"url", "doi"}:
            token = _trim_token(token)
        url = _token_url(kind, token, match, root, slug_of, own) if token else None
        if not url:
            scan = match.end()
            continue
        out.append(escape(text[position:match.start()]))
        if url.startswith(("http://", "https://")):
            out.append(Markup('<a href="{}" rel="noopener noreferrer">{}</a>').format(url, token))
        else:
            out.append(Markup('<a href="{}">{}</a>').format(url, token))
        # Resume after the token, not the match: what trimming cut off may hold
        # the next citation, as in "(https://a.org/x)-(https://b.org/y)".
        position = scan = match.start() + len(token)
    out.append(escape(text[position:]))
    return Markup("").join(out)


def _own_identifier(context) -> str:
    record = context.get("r")
    return str(record.get("identifier") or "") if isinstance(record, dict) else ""


@pass_context
def autolink(context, value: object) -> Markup:
    return autolink_text(value, root=context.get("root") or "",
                         slug_of=context.get("slug_of") or {}, own=_own_identifier(context))


@pass_context
def term_link(context, curie: object) -> Markup:
    """A displayed identifier as code, linked to where a reader can look it up.

    A CURIE that names one of this corpus's records links to that record's
    page; anything else goes through curie_url(). Never a link to "#".
    """
    value = str(curie or "").strip()
    if not value:
        return Markup("")
    code = Markup('<code class="curie">{}</code>').format(value)
    url = (_record_href(context.get("root") or "", context.get("slug_of") or {}, value)
           or curie_url(value))
    return Markup('<a href="{}">{}</a>').format(url, code) if url else code


@pass_context
def reference_link(context, reference: object) -> Markup:
    """An evidence reference: its citations linked, else a term link."""
    value = str(reference or "").strip()
    linked = autolink(context, value)
    if "<a " in linked:
        return Markup('<code class="curie">{}</code>').format(linked)
    return term_link(context, value)


def latest_timestamp(events: list[dict]) -> datetime | None:
    """The latest recorded event, read from the events and never from the clock,
    so rendering unchanged records twice gives the same bytes."""
    moments = []
    for event in events or []:
        raw = event.get("timestamp")
        try:
            moment = (raw if isinstance(raw, datetime)
                      else datetime.fromisoformat(str(raw).strip().replace("Z", "+00:00")))
        except ValueError:
            continue
        if moment.tzinfo is not None:
            moments.append(moment.astimezone(UTC))
    return max(moments) if moments else None


def as_of(events: list[dict]) -> str:
    moment = latest_timestamp(events)
    return moment.strftime("%Y-%m-%d") if moment else ""


def issue_url(identifier: str, page_url: str) -> str:
    """A new GitHub issue prefilled with the record it is about."""
    query = urlencode({"title": f"Problem with {identifier}", "body": page_url},
                      quote_via=quote)
    return f"{GITHUB_REPO}/issues/new?{query}"


def schema_reference(schema_path: Path = SCHEMA_PATH) -> dict:
    """Readable documentation of the record schema, read from the schema itself.

    Every class with the slots LinkML resolves for it (imports and slot_usage
    applied) and every enumeration with its values, in the schema's own order
    and with no clock, so an unchanged schema renders the same bytes and the
    pages/ check covers it. Descriptions are the schema's own wording.
    """
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(schema_path))
    module_file = {}
    for name, schema in view.schema_map.items():
        source = schema_path.parent / f"{name}.yaml"
        if source.is_file():
            module_file[schema.id] = source.relative_to(REPO_ROOT).as_posix()
    classes = view.all_classes()
    enums = view.all_enums()
    local = list(view.all_classes(imports=False))
    ordered = local + [name for name in classes if name not in local]
    local_enums = list(view.all_enums(imports=False))
    ordered_enums = local_enums + [name for name in enums if name not in local_enums]

    def range_kind(name: str) -> str:
        return "class" if name in classes else "enum" if name in enums else "type"

    def slot_row(slot) -> dict:
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
        "version": str(view.schema.version or ""),
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
            "description": enums[name].description or "",
            "source": module_file.get(enums[name].from_schema, ""),
            "permissible": [{"text": text, "description": value.description or "",
                        "meaning": value.meaning or ""}
                       for text, value in (enums[name].permissible_values or {}).items()],
        } for name in ordered_enums],
    }


def load_records() -> list[tuple[Path, dict]]:
    out = []
    for path in sorted(HABITATS_DIR.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        if isinstance(doc, dict):
            out.append((path, doc))
    return out


def load_decisions() -> dict[str, dict[str, str]]:
    if not DECISIONS_PATH.exists():
        return {}
    with DECISIONS_PATH.open(newline="", encoding="utf-8") as fh:
        return {r["identifier"]: r for r in csv.DictReader(fh, delimiter="\t")}


def render_graphs(graphs: list[dict]) -> list[dict]:
    out = []
    for graph in graphs:
        labels = {node["node_id"]: node["label"] for node in graph.get("nodes") or []}
        protein_examples = []
        for node in graph.get("nodes") or []:
            for ex in node.get("protein_examples") or []:
                accession = ex.get("accession", "")
                protein_examples.append(
                    {
                        "node_id": node.get("node_id", ""),
                        "node_label": node.get("label", ""),
                        "accession": accession,
                        "uniprot_url": term_iri(accession) or "",
                        "entry_name": ex.get("entry_name", ""),
                        "recommended_name": ex.get("recommended_name", ""),
                        "gene_symbol": ex.get("gene_symbol", ""),
                        "locus_tag": ex.get("locus_tag", ""),
                        "taxon_id": ex.get("taxon_id", ""),
                        "taxon_name": ex.get("taxon_name", ""),
                        "role_in_node": ex.get("role_in_node", ""),
                        "sequence_length": ex.get("sequence_length", ""),
                        "crc64": ex.get("crc64", ""),
                        "evidence": ex.get("evidence") or [],
                    }
                )
        out.append(
            {
                "source_graph": graph,
                "graph_id": graph.get("graph_id", ""),
                "title": graph.get("title") or graph.get("graph_id", ""),
                "description": graph.get("description", ""),
                "edges": [
                    {
                        "edge_id": edge.get("edge_id", ""),
                        "subject": labels.get(edge.get("subject"), edge.get("subject", "")),
                        "predicate": edge.get("predicate", ""),
                        "object": labels.get(edge.get("object"), edge.get("object", "")),
                        "description": edge.get("description", ""),
                        "evidence": edge.get("evidence") or [],
                    }
                    for edge in graph.get("edges") or []
                ],
                "protein_examples": protein_examples,
            }
        )
    return out


def extracted_at() -> str:
    if MANIFEST_PATH.exists():
        for line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines():
            if line.startswith("extracted_at:"):
                return line.split(":", 1)[1].strip().strip("'\"")[:10]
    return "an unrecorded date"


def template_environment() -> Environment:
    """The Jinja environment every page is rendered with, filters included."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["graph_svg"] = graph_svg
    env.filters["autolink"] = autolink
    env.filters["term_link"] = term_link
    env.filters["reference_link"] = reference_link
    env.filters["taxonmech_url"] = taxonmech_url
    env.globals["sibling_search"] = sibling_search
    env.globals["github_repo"] = GITHUB_REPO
    return env


def build(out_dir: Path) -> None:
    # Validate enablement, current checksums and fresh full inputs before
    # an ordinary site build can remove or replace existing pages.
    with prepare_text_map(REPO_ROOT) as text_map:
        _build(out_dir, text_map)


def _build(out_dir: Path, text_map: PreparedTextMap | None) -> None:
    if text_map is not None:
        text_map.stage(out_dir, directory="text-map-source")
    records = load_records()
    if not records:
        raise SystemExit(f"no records under {HABITATS_DIR}; run `just seed-apply` first")
    decisions = load_decisions()
    excluded_requests = excluded_term_requests()

    env = template_environment()
    env.globals["text_map_enabled"] = text_map is not None

    slug_of = {doc["identifier"]: slugify(f"{doc['label']}-{doc['identifier']}") for _, doc in records}
    label_of = {doc["identifier"]: doc["label"] for _, doc in records}
    # A cross-referenced term is usually NOT a record — that is what makes it a
    # cross-reference — so the corpus cannot name it. Falling back to the
    # vendored slice is the difference between "ENVO:00002204" and
    # "anthropogenic contamination feature" on the page.
    for _row in _slice_labels():
        label_of.setdefault(_row["term_id"], _row["label"])

    by_category: dict[str, list[dict]] = defaultdict(list)
    grounding_counts: Counter = Counter()
    status_counts: Counter = Counter()
    multi_source = 0
    term_requests: list[dict] = []
    swept = 0

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "habitats").mkdir(exist_ok=True)
    (out_dir / "category").mkdir(exist_ok=True)

    # First pass: corpus-wide counts. Record pages are rendered in the second
    # pass and previously read `stats` before it was filled, so their footer
    # printed " of 3192 records are machine-generated" with the count missing —
    # on exactly the pages where a reader is looking at one such record (#31).
    stats = {
        "total": len(records),
        "extracted_at": extracted_at(),
        "reviewed": sum(1 for _, d in records if d.get("mapping_status") == "REVIEWED"),
        "seeded": sum(1 for _, d in records if d.get("mapping_status") == "SEEDED"),
        # The dated version of the corpus: its latest recorded curation event.
        # Aggregate pages state it; a record page states its own record's date
        # instead, so one record's curation does not rewrite every page (#31).
        "corpus_as_of": as_of([e for _, d in records for e in d.get("curation_history") or []]),
    }

    for path, doc in records:
        identifier = doc["identifier"]
        attestations = doc.get("source_attestations") or []
        sources = sorted({a["source"] for a in attestations})
        assertions = sum(a.get("assertion_count") or 0 for a in attestations)
        grounding_counts[doc.get("grounding_status", "?")] += 1
        status_counts[doc.get("mapping_status", "?")] += 1
        if len(sources) > 1:
            multi_source += 1

        taxa = doc.get("characteristic_taxa") or []
        record = {
            "identifier": identifier,
            "label": doc["label"],
            "iri": term_iri(identifier),
            "definition": doc.get("definition"),
            "definition_source": doc.get("definition_source"),
            "category": doc.get("habitat_category", "OTHER"),
            "category_slug": slugify(doc.get("habitat_category", "OTHER")),
            "grounding": doc.get("grounding_status", "?"),
            "status": doc.get("mapping_status", "?"),
            "sources": sources,
            "attestations": attestations,
            "parameters": doc.get("environmental_parameters") or [],
            "causal_graphs": render_graphs(doc.get("causal_graphs") or []),
            "synonyms": [
                {"text": s["synonym_text"], "source": s.get("source", "")}
                for s in (doc.get("synonyms") or [])
            ],
            "parents": [
                {
                    "id": p,
                    "label": label_of.get(p, p),
                    "href": f"../habitats/{slug_of[p]}.html" if p in slug_of else curie_url(p),
                }
                for p in (doc.get("parent_habitats") or [])
            ],
            # Terms upstream linked to this concept without this repo asserting
            # they are the same thing or that one is broader (#99). 48 records
            # carry one and none of them reached the page before.
            "xrefs": [
                {
                    "id": x,
                    "label": label_of.get(x, ""),
                    "href": f"../habitats/{slug_of[x]}.html" if x in slug_of else curie_url(x),
                }
                for x in (doc.get("xrefs") or [])
            ],
            "taxa": [
                {
                    "id": t["taxon_id"],
                    "label": t.get("taxon_label"),
                    "source": t.get("source", ""),
                    "rank": t.get("rank"),
                    "pool": t.get("candidate_pool"),
                    "corroborated": t.get("corroborated_by") or [],
                }
                for t in taxa[:TAXA_SHOWN]
            ],
            "taxa_total": len(taxa),
            "taxa_truncated": len(taxa) > TAXA_SHOWN,
            # Every recorded event, the seeding first. The curator decisions
            # are the part a reader cannot get anywhere else -- decisions.tsv
            # is a seeder input, not something the site serves, so before #94
            # a curated grounding was indistinguishable from a machine-generated
            # one -- but leaving the seed event out hid the only dated,
            # attributed event of the 1,322 records nobody has curated since.
            "events": [
                {
                    "action": e.get("action", ""),
                    "curator": e.get("curator", ""),
                    "date": (e.get("timestamp") or "")[:10],
                    "changes": e.get("changes", "").replace("[CLASS-level] ", ""),
                    "class_level": "[CLASS-level]" in (e.get("changes") or ""),
                    "seeded": e.get("action") == "SEEDED_FROM_SOURCES",
                }
                for e in (doc.get("curation_history") or [])
            ],
            "as_of": as_of(doc.get("curation_history") or []),
            "repo_path": str(path.relative_to(REPO_ROOT)),
            "issue_url": issue_url(identifier, f"{SITE_BASE}habitats/{slug_of[identifier]}.html"),
        }

        (out_dir / "habitats" / f"{slug_of[identifier]}.html").write_text(
            env.get_template("habitat.html").render(r=record, root="../", stats=stats,
                                                    slug_of=slug_of),
            encoding="utf-8",
        )

        by_category[record["category"]].append(
            {
                "label": doc["label"],
                "identifier": identifier,
                "slug": slug_of[identifier],
                "grounding": record["grounding"],
                "path": (
                    attestations[0].get("source_path")
                    or attestations[0].get("source_label", "")
                    if attestations else ""
                ),
                # Same path with the category prefix trimmed. Every row on a
                # category page repeats it — "Host-associated > " 1643 times —
                # and the page it is on already says which category this is
                # (#34). The untrimmed `path` still feeds the search key.
                "short_path": _trim_category_prefix(
                    (
                        attestations[0].get("source_path")
                        or attestations[0].get("source_label", "")
                        if attestations else ""
                    ),
                    record["category"],
                ),
                "assertions": assertions,
                "sources": sources,
            }
        )

        # The term-request list is the individually-examined ungrounded records
        # only. The bulk-swept ones are candidates for it, not members, and
        # conflating them would send curators a list mostly nobody has read.
        if doc.get("grounding_status") == "UNGROUNDED":
            decision = decisions.get(identifier, {})
            depth = (decision.get("review_depth") or "ITEM").upper()
            if doc.get("mapping_status") == "REVIEWED" and depth == "ITEM":
                # Deliberately excluded item reviews are neither requests nor sweeps.
                if identifier in excluded_requests:
                    continue
                term_requests.append(
                    {
                        "label": doc["label"],
                        "slug": slug_of[identifier],
                        "assertions": assertions,
                        "sources": sources,
                        "note": decision.get("notes", ""),
                    }
                )
            else:
                swept += 1

    stats.update(
        {
            "grounded": sum(
                v for k, v in grounding_counts.items()
                if k in ("EXACT", "CLOSE", "NARROW", "BROAD")
            ),
            "multi_source": multi_source,
            "term_requests": len(term_requests),
        }
    )
    # What HabitatMech contributes over the ontologies it grounds to. Computed
    # by the report so the site and `just report` cannot disagree about the
    # project's headline claim.
    coverage_rows = []
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from habitatmech.report import COVERAGE_KINDS, _coverage_over_ontologies

        kinds, kind_assertions = _coverage_over_ontologies(records)
        coverage_rows = [
            {"count": kinds[key], "assertions": kind_assertions[key], "why": why}
            for key, why in COVERAGE_KINDS
        ]
        stats["new_over_envo"] = sum(kinds.values()) - kinds["named_by_envo"]
        stats["novel"] = kinds["unnamed"] + kinds["refines_envo"] + kinds["refines_other"]
    except ImportError:
        stats["new_over_envo"] = 0
        stats["novel"] = 0
    assert stats["seeded"] == status_counts.get("SEEDED", 0)

    groundings = [
        {"name": name, "count": count, "meaning": GROUNDING_MEANING.get(name, "")}
        for name, count in grounding_counts.most_common()
    ]

    categories = [
        {
            "label": name,
            "slug": slugify(name),
            "count": len(items),
            "pct": round(100 * len(items) / len(records)),
            "grounded": sum(1 for i in items if i["grounding"] not in ("UNGROUNDED", "NOT_APPLICABLE")),
            "description": CATEGORY_BLURB.get(name, ""),
        }
        for name, items in sorted(by_category.items(), key=lambda kv: -len(kv[1]))
    ]
    category_pages: list[str] = []
    for name, items in sorted(by_category.items(), key=lambda kv: -len(kv[1])):
        ordered = sorted(items, key=lambda r: (-r["assertions"], r["label"]))
        slug = slugify(name)
        # Paginated because 99% of a category page is its table body, and the
        # biggest was 1641 rows in 461 KB — the likeliest first click from
        # Browse, and by far the heaviest page on the site (#34).
        chunks = [ordered[i:i + CATEGORY_PAGE_SIZE]
                  for i in range(0, len(ordered), CATEGORY_PAGE_SIZE)] or [[]]
        pager = [
            {"n": n, "href": f"{slug}.html" if n == 1 else f"{slug}-{n}.html"}
            for n in range(1, len(chunks) + 1)
        ]
        for n, chunk in enumerate(chunks, start=1):
            target = out_dir / "category" / (f"{slug}.html" if n == 1 else f"{slug}-{n}.html")
            target.write_text(
                env.get_template("category.html").render(
                    category=name,
                    description=CATEGORY_BLURB.get(name, ""),
                    records=chunk,
                    total=len(ordered),
                    page=n,
                    pager=pager if len(pager) > 1 else [],
                    index_url=f"{slug}.json",
                    root="../",
                    stats=stats,
                    categories=categories,
                    groundings=groundings,
                ),
                encoding="utf-8",
            )
            category_pages.append(f"category/{target.name}")
        # A compact index so the filter can still search the WHOLE category
        # rather than only the page in front of you. Fetched on the first
        # keystroke, not on load, so it costs nothing to a reader who browses.
        (out_dir / "category" / f"{slug}.json").write_text(
            json.dumps(
                [[r["label"], r["slug"], r["short_path"], r["grounding"],
                  r["assertions"], ", ".join(r["sources"])] for r in ordered],
                separators=(",", ":"), ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    (out_dir / "index.html").write_text(
        env.get_template("index.html").render(
            stats=stats, categories=categories, groundings=groundings,
            coverage=coverage_rows, root=""
        ),
        encoding="utf-8",
    )
    (out_dir / "browse.html").write_text(
        env.get_template("browse.html").render(
            stats=stats, categories=categories, groundings=groundings, root=""
        ),
        encoding="utf-8",
    )
    (out_dir / "term-requests.html").write_text(
        env.get_template("term_requests.html").render(
            requests=sorted(term_requests, key=lambda r: -r["assertions"]),
            swept=swept,
            stats=stats,
            root="",
            slug_of=slug_of,
        ),
        encoding="utf-8",
    )
    # Readable documentation of the record schema, generated from the schema
    # so it cannot fall behind it the way a hand-written page would.
    (out_dir / "schema.html").write_text(
        env.get_template("schema.html").render(schema=schema_reference(), stats=stats, root=""),
        encoding="utf-8",
    )
    shutil.copyfile(TEMPLATES_DIR / "style.css", out_dir / "style.css")
    shutil.copyfile(TEMPLATES_DIR / "theme-toggle.js", out_dir / "theme-toggle.js")
    # Without this, Pages runs Jekyll over the site and silently drops any path
    # beginning with an underscore — a 404 rather than a visible error. Slugs
    # come from habitat labels, so that is not guaranteed to stay impossible
    # (#32). Written by the renderer so it is reproducible like everything else.
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")

    # A sitemap matters more here than for a typical project site: the point of
    # publishing is that ontology curators find the term requests and the record
    # pages, and every record page is otherwise reachable only by following a
    # category link — three clicks from the root, with no machine-readable index
    # of the deepest and most numerous content (#36).
    listed = ["index.html", "browse.html", "term-requests.html", "schema.html"]
    listed += category_pages
    listed += [f"habitats/{slug}.html" for slug in sorted(slug_of.values())]
    urls = "\n".join(f"  <url><loc>{SITE_BASE}{page}</loc></url>" for page in listed)
    (out_dir / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n",
        encoding="utf-8",
    )
    (out_dir / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_BASE}sitemap.xml\n", encoding="utf-8"
    )

    # Redirect stubs for records curation retired. A record page is named
    # slugify(label + identifier), so improving either moves the URL — which is
    # most of what curation does. Without these, every improvement 404s a
    # published address and a content-hashed identifier stops being citable
    # (#54). data/habitats/RETIRED.tsv is rebuilt by `just redirects`.
    retired_written: set[Path] = set()
    retired_path = REPO_ROOT / "data" / "habitats" / "RETIRED.tsv"
    if retired_path.exists():
        with retired_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                targets = [
                    {"identifier": t, "label": label_of.get(t, t), "slug": slug_of[t]}
                    for t in row["current_identifiers"].split("|")
                    if t in slug_of
                ]
                if not targets:
                    continue
                if row["retired_slug"] in slug_of.values():
                    # A retired slug that a live record now uses. Overwriting it
                    # would replace a real habitat with a redirect away from
                    # itself; the live record wins and the stub is dropped.
                    continue
                stub = out_dir / "habitats" / f"{row['retired_slug']}.html"
                stub.write_text(
                    env.get_template("redirect.html").render(
                        r={
                            "retired_identifier": row["retired_identifier"],
                            "retired_label": row.get("retired_label") or row["retired_identifier"],
                            "resolved_by": row["resolved_by"],
                            "targets": targets,
                        },
                        root="../", site_base=SITE_BASE, stats=stats,
                    ),
                    encoding="utf-8",
                )
                retired_written.add(stub)

    (out_dir / "404.html").write_text(
        env.get_template("not_found.html").render(root=SITE_BASE, stats=stats),
        encoding="utf-8",
    )

    if text_map is not None:
        # The map says how many of the site's records it plots, from the
        # coverage its own manifest records, so a sampled map is never silent.
        manifest = json.loads(
            (out_dir / "text-map-source" / "manifest.json").read_text(encoding="utf-8"))
        (out_dir / "text-map").mkdir(exist_ok=True)
        (out_dir / "text-map" / "index.html").write_text(
            env.get_template("text_map.html").render(
                root="../", stats=stats, categories=categories, groundings=groundings,
                map_coverage=manifest.get("coverage") or {},
            ),
            encoding="utf-8")

    # Remove pages for records that no longer exist. Curation splits records as
    # well as merging them, so the set shrinks too; without this the site keeps
    # serving a page for a habitat the corpus has dropped, and --check reports it
    # as orphaned forever. Same reason the seeder has --prune.
    written = {
        out_dir / "index.html", out_dir / "browse.html", out_dir / "term-requests.html",
        out_dir / "schema.html",
        out_dir / "style.css", out_dir / "theme-toggle.js", out_dir / ".nojekyll",
        out_dir / "sitemap.xml", out_dir / "robots.txt", out_dir / "404.html",
    }
    written |= retired_written
    if text_map is not None:
        written |= {out_dir / "text-map-source" / name
                    for name in ("index.html", "points.json", "manifest.json")}
        written.add(out_dir / "text-map" / "index.html")
    written |= {out_dir / "habitats" / f"{slug}.html" for slug in slug_of.values()}
    written |= {out_dir / name for name in category_pages}
    written |= {out_dir / "category" / f"{c['slug']}.json" for c in categories}
    pruned = 0
    for existing in sorted(out_dir.rglob("*")):
        if existing.is_file() and existing not in written:
            existing.unlink()
            pruned += 1

    print(f"rendered {len(records)} habitat pages, {len(retired_written)} redirect stubs, "
          f"{len(categories)} categories, {len(term_requests)} term requests"
          + (f", pruned {pruned} stale" if pruned else "")
          + f" -> {out_dir}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Render to a temp dir and fail if pages/ differs — the site is "
        "committed, so it can go stale against the corpus exactly as records "
        "could go stale against data/raw/.",
    )
    args = parser.parse_args(argv)

    if not args.check:
        build(args.out)
        if args.out.resolve() == PAGES_DIR.resolve():
            shutil.copyfile(args.out / "404.html", REPO_ROOT / "404.html")
        return 0

    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "site"
        build(target)
        stale = []
        for rendered in sorted(target.rglob("*")):
            if rendered.is_dir():
                continue
            committed = PAGES_DIR / rendered.relative_to(target)
            if not committed.exists() or not filecmp.cmp(rendered, committed, shallow=False):
                stale.append(str(rendered.relative_to(target)))
        root_404 = REPO_ROOT / "404.html"
        if not root_404.exists() or root_404.read_bytes() != (target / "404.html").read_bytes():
            stale.append("../404.html")
        extra = [
            str(p.relative_to(PAGES_DIR))
            for p in sorted(PAGES_DIR.rglob("*"))
            if p.is_file() and not (target / p.relative_to(PAGES_DIR)).exists()
        ]
        if stale or extra:
            print(f"pages/ is stale: {len(stale)} differing, {len(extra)} orphaned", file=sys.stderr)
            for name in (stale + extra)[:10]:
                print(f"  {name}", file=sys.stderr)
            print("\nRegenerate with `just render`.", file=sys.stderr)
            return 1
        print("pages/ is in step with the corpus")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
