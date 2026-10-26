"""The X-Mech website features this site provides, checked on rendered pages.

Each assertion is scoped to the part of a page the feature lives in: a link
that also appears in the navigation or another section would otherwise satisfy
an assertion about the section under test. Browser behaviour is checked by
running each page's shipped script against a fake DOM in Node
(tests/site_script_harness.cjs), offline and without a browser.
"""
from __future__ import annotations

import functools
import json
import re
import shutil
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest

from scripts import render_pages as site

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"
HARNESS = Path(__file__).with_name("site_script_harness.cjs")
needs_node = pytest.mark.skipif(shutil.which("node") is None,
                                reason="Node runs the shipped page scripts")


def between(text: str, start: str, end: str) -> str:
    """The first stretch of `text` from `start` up to the next `end`."""
    head = text.index(start)
    return text[head:text.index(end, head + len(start))]


def anchors(fragment: str) -> list[tuple[str, str]]:
    return re.findall(r'<a\b[^>]*?\bhref="([^"]*)"[^>]*>(.*?)</a>', fragment, re.S)


def footer(text: str) -> str:
    return between(text, '<footer class="site">', "</footer>")


@functools.cache
def corpus() -> dict[str, dict]:
    """Each record page's file name -> the record it renders."""
    return {f"{site.slugify(doc['label'] + '-' + doc['identifier'])}.html": doc
            for _, doc in site.load_records()}


@functools.cache
def record_page(name: str) -> str:
    return (PAGES / "habitats" / name).read_text(encoding="utf-8")


class Unlinked(HTMLParser):
    """Text inside <main> that is not inside a link or an SVG."""

    def __init__(self) -> None:
        super().__init__()
        self.depth = {"main": 0, "a": 0, "svg": 0}
        self.chunks: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.depth:
            self.depth[tag] += 1

    def handle_endtag(self, tag):
        if tag in self.depth:
            self.depth[tag] -= 1

    def handle_data(self, data):
        if self.depth["main"] and not self.depth["a"] and not self.depth["svg"]:
            self.chunks.append(data)


def unlinked_text(page: str) -> str:
    parser = Unlinked()
    parser.feed(page)
    return " ".join(parser.chunks)


# --------------------------------------------------------------- evidence --

def link(text: str, **kwargs) -> str:
    return str(site.autolink_text(text, **kwargs))


def test_autolink_links_pmids_dois_pmcids_and_urls():
    html = link("Backed by PMID:31388058, (PMID 25852669; DOI:10.3389/fmicb.2015.00249) and "
                "doi:10.1016/j.scitotenv.2014.07.018. See PMC12093969 or "
                "https://example.org/a?b=1&c=2.")
    assert anchors(html) == [
        ("https://pubmed.ncbi.nlm.nih.gov/31388058/", "PMID:31388058"),
        ("https://pubmed.ncbi.nlm.nih.gov/25852669/", "PMID 25852669"),
        ("https://doi.org/10.3389/fmicb.2015.00249", "DOI:10.3389/fmicb.2015.00249"),
        ("https://doi.org/10.1016/j.scitotenv.2014.07.018", "doi:10.1016/j.scitotenv.2014.07.018"),
        ("https://pmc.ncbi.nlm.nih.gov/articles/PMC12093969/", "PMC12093969"),
        ("https://example.org/a?b=1&amp;c=2", "https://example.org/a?b=1&amp;c=2"),
    ]
    assert html.endswith("</a>.")


def test_autolink_ends_a_token_at_markdown_and_punctuation():
    html = link("[10.1038/ngeo1921](https://doi.org/10.1038/ngeo1921) **10.1099/ijs.0.1** "
                "`10.1128/AEM.1` (https://a.org/p)-(https://b.org/q); "
                "https://en.wikipedia.org/wiki/Foo_(bar). (https://github.com/CultureBotAI/"
                "HabitatMech/issues/1948; 20261011T155026Z)")
    assert anchors(html) == [
        ("https://doi.org/10.1038/ngeo1921", "10.1038/ngeo1921"),
        ("https://doi.org/10.1038/ngeo1921", "https://doi.org/10.1038/ngeo1921"),
        ("https://doi.org/10.1099/ijs.0.1", "10.1099/ijs.0.1"),
        ("https://doi.org/10.1128/AEM.1", "10.1128/AEM.1"),
        ("https://a.org/p", "https://a.org/p"),
        ("https://b.org/q", "https://b.org/q"),
        ("https://en.wikipedia.org/wiki/Foo_(bar)", "https://en.wikipedia.org/wiki/Foo_(bar)"),
        # #2046: the semicolon after an issue URL used to join the link.
        ("https://github.com/CultureBotAI/HabitatMech/issues/1948",
         "https://github.com/CultureBotAI/HabitatMech/issues/1948"),
    ]


def test_autolink_keeps_record_text_as_text():
    html = link('<script>alert(1)</script> "https://x.org/a"><b>bold</b>')
    assert "<script>" not in html and "&lt;script&gt;alert(1)&lt;/script&gt;" in html
    assert "<b>" not in html
    assert anchors(html) == [("https://x.org/a", "https://x.org/a")]
    assert link("javascript:alert(1) ftp://x.org/f") == "javascript:alert(1) ftp://x.org/f"


def test_autolink_links_known_curies_to_record_pages_before_resolvers():
    slug_of = {"ENVO:00002007": "sediment-envo-00002007",
               "habitatmech:GOLD.0123456789": "x-habitatmech-gold-0123456789"}
    html = link("ENVO:00002007 is broader than ENVO:00001999; habitatmech:GOLD.0123456789. "
                "habitatmech:GOLD.ffffffffff stays, NCBITaxon:562 links, Note: word:thing "
                "ENVO:03000033 is this page.",
                root="../", slug_of=slug_of, own="ENVO:03000033")
    assert anchors(html) == [
        ("../habitats/sediment-envo-00002007.html", "ENVO:00002007"),
        ("http://purl.obolibrary.org/obo/ENVO_00001999", "ENVO:00001999"),
        ("../habitats/x-habitatmech-gold-0123456789.html", "habitatmech:GOLD.0123456789"),
        ("http://purl.obolibrary.org/obo/NCBITaxon_562", "NCBITaxon:562"),
    ]


def test_record_pages_leave_no_citation_unlinked():
    token = re.compile(r"\b(?i:pmid)(?::\s?|\s)\d{1,9}\b|(?<![\w./])10\.\d{4,9}/[^\s<>\"'`\]]+"
                       r"|\bhttps?://\S+|\bPMC\d{4,9}\b")
    unlinked = {name: token.findall(unlinked_text(record_page(name))) for name in corpus()}
    assert {name: hits for name, hits in unlinked.items() if hits} == {}
    pubmed = sum(record_page(name).count('href="https://pubmed.ncbi.nlm.nih.gov/') for name in corpus())
    assert pubmed > 1000, "not vacuous: the corpus cites PubMed on hundreds of pages"


def test_causal_graph_edge_evidence_links_pubmed():
    page = record_page("marine-sediment-envo-03000033.html")
    edges = between(page, "<caption>marine_sediment_sulfate_sulfur_cycling edges</caption>", "</table>")
    assert ('https://pubmed.ncbi.nlm.nih.gov/31388058/', 'PMID:31388058') in anchors(edges)


# ------------------------------------------------------------- term links --

def test_curie_url_resolves_known_prefixes_and_falls_back_to_bioregistry():
    assert site.curie_url("ENVO:00002007") == "http://purl.obolibrary.org/obo/ENVO_00002007"
    assert site.curie_url("NCBITaxon:562") == "http://purl.obolibrary.org/obo/NCBITaxon_562"
    assert site.curie_url("SNOMED:123456") == "https://bioregistry.io/SNOMED:123456"
    assert site.curie_url("habitatmech:GOLD.ffffffffff") is None, "no registry knows this namespace"
    assert site.curie_url("not a curie") is None


def test_every_associated_taxon_links_its_resolver_and_taxonmech_record():
    checked = 0
    for name, doc in corpus().items():
        taxa = (doc.get("characteristic_taxa") or [])[:site.TAXA_SHOWN]
        if not taxa:
            continue
        table = between(record_page(name), "<caption>Taxa reported from this habitat</caption>",
                        "</table>")
        rows = re.findall(r"<tr>\s*<td>(.*?)</td>", table, re.S)
        assert len(rows) == len(taxa), name
        for taxon, cell in zip(taxa, rows, strict=True):
            curie = taxon["taxon_id"]
            number = curie.split(":")[1]
            assert (f"http://purl.obolibrary.org/obo/NCBITaxon_{number}",
                    f'<code class="curie">{curie}</code>') in anchors(cell), (name, curie)
            assert (f"https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon%3A{number}"
                    in [href for href, _ in anchors(cell)]), (name, curie)
            checked += 1
    assert checked > 10000, "not vacuous: 12,000+ taxon rows are displayed"


def test_broader_and_related_terms_link_their_identifiers():
    page = record_page("marine-sediment-envo-03000033.html")
    broader = between(page, "<h2>Broader habitats</h2>", "</ul>")
    assert any(href == "../habitats/sediment-envo-00002007.html"
               and '<code class="curie">ENVO:00002007</code>' in text
               for href, text in anchors(broader))
    assert " ".join(unlinked_text(f"<main>{broader}</main>").split()) == "Broader habitats", \
        "each identifier sits inside the link to its term"


# ------------------------------------------------------- sibling Mech links --

# The fleet's verified sibling routes (X-Mech unified standard, loaded live in
# headless Chrome on 2026-10-25): every search route restored ?q= with a
# filtered count, and TaxonMech's record route opens one taxon. A link anywhere
# else on a sibling site is a guess that nothing here can check.
VERIFIED_SIBLING_ROUTES = (
    "https://culturebotai.github.io/CultureMech/app/browser.html?q=",
    "https://culturebotai.github.io/MediaIngredientMech/browser.html?q=",
    "https://culturebotai.github.io/CommunityMech/browser.html?q=",
    "https://culturebotai.github.io/TraitMech/pages/browse.html?q=",
    "https://culturebotai.github.io/proteintraitsmech/browse.html?q=",
    "https://culturebotai.github.io/AntibioticMech/pages/browse.html?q=",
    "https://culturebotai.github.io/CellStructureMech/pages/browse.html?q=",
    "https://culturebotai.github.io/NaturalProductMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=",
    "https://culturebotai.github.io/PathwayMech/pages/browse.html?q=",
    "https://culturebotai.github.io/DUFMech/index.html?q=",
    "https://culturebotai.github.io/CMMMech/pages/browse.html?q=",
    "https://culturebotai.github.io/AIMech/pages/browse.html?q=",
)
# Links with no query: the landing's project links and the suite directory,
# each exactly a site root (every one answered HTTP 200 on 2026-10-25).
SIBLING_SITE_ROOTS = {
    "https://culturebotai.github.io/TaxonMech/",
    "https://culturebotai.github.io/CommunityMech/",
    "https://culturebotai.github.io/CultureMech/",
    "https://culturebotai.github.io/TraitMech/",
    "https://culturebotai.github.io/mechs/",
}
FLEET_URL = re.compile(r"https?://culturebotai\.github\.io/[^\s\"'<>)]*")


def unverified_sibling_urls(text: str) -> set[str]:
    return {url for url in FLEET_URL.findall(text)
            if not url.startswith("https://culturebotai.github.io/HabitatMech/")
            and url not in SIBLING_SITE_ROOTS and not url.startswith(VERIFIED_SIBLING_ROUTES)}


def test_sibling_links_in_renderer_sources_use_verified_routes():
    sources = [*sorted(site.TEMPLATES_DIR.glob("*.html")), ROOT / "scripts" / "render_pages.py"]
    found = {path.name: unverified_sibling_urls(path.read_text(encoding="utf-8")) for path in sources}
    assert {name: urls for name, urls in found.items() if urls} == {}
    assert set(site.SIBLING_SEARCH.values()) <= set(VERIFIED_SIBLING_ROUTES)


def test_every_sibling_link_in_the_built_site_uses_a_verified_route():
    built = [*sorted(PAGES.rglob("*.html")), ROOT / "404.html"]
    built = [path for path in built if "text-map-source" not in path.parts]
    assert len(built) > 3900
    emitted: set[str] = set()
    bad: dict[str, set[str]] = {}
    for path in built:
        text = path.read_text(encoding="utf-8")
        emitted |= set(FLEET_URL.findall(text))
        if urls := unverified_sibling_urls(text):
            bad[str(path.relative_to(ROOT))] = urls
    assert bad == {}
    records = {url for url in emitted if url.startswith(site.TAXONMECH_RECORD)}
    assert len(records) > 5000, "not vacuous: taxa link TaxonMech records"
    assert all(re.fullmatch(re.escape(site.TAXONMECH_RECORD) + r"NCBITaxon%3A\d+", url)
               for url in records), "the record route opens one NCBITaxon id"


def test_record_pages_search_siblings_for_the_habitat_label():
    page = record_page("marine-sediment-envo-03000033.html")
    block = between(page, '<p class="xmech-links">', "</p>")
    hrefs = [href for href, _ in anchors(block)]
    assert hrefs == [
        "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=marine%20sediment",
        "https://culturebotai.github.io/CommunityMech/browser.html?q=marine%20sediment",
        "https://culturebotai.github.io/CultureMech/app/browser.html?q=marine%20sediment",
        "https://culturebotai.github.io/TraitMech/pages/browse.html?q=marine%20sediment",
        "https://culturebotai.github.io/mechs/",
    ]


# ------------------------------------------------------- curation history --

def test_every_record_page_lists_a_dated_attributed_event():
    seeded_only = 0
    for name, doc in corpus().items():
        section = between(record_page(name), "<h2>Curation</h2>", "</ol>")
        events = re.findall(r'<span class="meta">(\d{4}-\d{2}-\d{2}) · ([^\s<]+)', section)
        assert len(events) == len(doc["curation_history"]), name
        assert all(curator for _, curator in events), name
        if all(e["action"] == "SEEDED_FROM_SOURCES" for e in doc["curation_history"]):
            seeded_only += 1
            assert "SEEDED_FROM_SOURCES" in section, name
    assert seeded_only > 1000, "not vacuous: most records have only their seed event"


# ----------------------------------------------------------- feedback route --

def test_every_record_page_offers_a_prefilled_issue_for_that_record():
    for name, doc in corpus().items():
        actions = between(record_page(name), '<p class="record-actions">', "</p>")
        [(href, text)] = anchors(actions)
        assert text == "Report a problem with this record"
        url = urlsplit(href.replace("&amp;", "&"))
        assert f"{url.scheme}://{url.netloc}{url.path}" == \
            "https://github.com/CultureBotAI/HabitatMech/issues/new"
        query = parse_qs(url.query)
        assert query == {"title": [f"Problem with {doc['identifier']}"],
                         "body": [f"{site.SITE_BASE}habitats/{name}"]}, name


# ------------------------------------------------- licence and provenance --

def page_types() -> dict[str, Path]:
    stub = next(path for path in sorted((PAGES / "habitats").glob("*.html"))
                if path.name not in corpus())
    return {
        "landing": PAGES / "index.html", "browse": PAGES / "browse.html",
        "category": PAGES / "category" / "aquatic.html",
        "category page 2": PAGES / "category" / "host-associated-2.html",
        "record": PAGES / "habitats" / "marine-sediment-envo-03000033.html",
        "redirect stub": stub, "term requests": PAGES / "term-requests.html",
        "map": PAGES / "text-map" / "index.html", "schema": PAGES / "schema.html",
        "404": PAGES / "404.html", "root 404": ROOT / "404.html",
    }


def test_every_page_type_states_the_licences_of_the_licence_files():
    blob = "https://github.com/CultureBotAI/HabitatMech/blob/main/"
    for kind, path in page_types().items():
        text = footer(path.read_text(encoding="utf-8"))
        licence = between(text, '<p class="licence">', "</p>")
        assert anchors(licence) == [(blob + "LICENSE-DATA", "CC BY 4.0"),
                                    (blob + "LICENSE-CODE", "BSD-3-Clause"),
                                    (blob + "LICENSE", "licence scope")], kind
        assert "Third-party source material keeps its own terms" in licence, kind
    scope = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "CC-BY-4.0" in scope and "BSD-3-Clause" in scope
    assert "retain their own licenses" in scope


def test_corpus_date_is_the_latest_curation_event_whatever_its_position():
    events = [{"timestamp": "2026-10-12T05:48:36Z"}, {"timestamp": "2026-08-16T05:58:02Z"},
              {"timestamp": "not a date"}, {"timestamp": "2026-09-04T00:00:00Z"}]
    assert site.as_of(events) == "2026-10-12"
    assert site.as_of([]) == ""


def test_pages_state_a_dated_version_of_what_they_show():
    corpus_date = site.as_of([event for doc in corpus().values()
                              for event in doc["curation_history"]])
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", corpus_date)
    types = page_types()
    for kind in ("landing", "browse", "category", "term requests", "map", "schema"):
        text = footer(types[kind].read_text(encoding="utf-8"))
        assert f"Corpus as of {corpus_date}" in text, kind
    for name in ("marine-sediment-envo-03000033.html", "143-b-cell-bto-0003167.html"):
        text = footer(record_page(name))
        assert f"Record as of {site.as_of(corpus()[name]['curation_history'])}," in text
        assert "Corpus as of" not in text, "a corpus date would rewrite every record page"
    for kind in ("redirect stub", "404", "root 404"):
        text = footer(types[kind].read_text(encoding="utf-8"))
        assert "Corpus as of" not in text and "Record as of" not in text, kind


# ------------------------------------------------------------- schema docs --

def test_schema_page_documents_every_class_slot_and_enum():
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(site.SCHEMA_PATH))
    page = (PAGES / "schema.html").read_text(encoding="utf-8")
    classes = re.findall(r'<section class="schema-class" id="class-([^"]+)"', page)
    enums = re.findall(r'<section class="schema-enum" id="enum-([^"]+)"', page)
    assert sorted(classes) == sorted(view.all_classes())
    assert sorted(enums) == sorted(view.all_enums())
    record = between(page, 'id="class-HabitatRecord"', "</section>")
    slots = re.findall(r'<tr id="class-HabitatRecord-([^"]+)">', record)
    assert slots == [slot.name for slot in view.class_induced_slots("HabitatRecord")]
    identifier = between(record, 'id="class-HabitatRecord-identifier"', "</tr>")
    assert "(identifier)" in identifier and "Required" in identifier
    status = between(page, 'id="enum-MappingStatusEnum"', "</section>")
    assert "<code>REVIEWED</code>" in status
    description = between(page, '<div class="schema-description">', "</div>")
    assert "ENVO:00000316" in description and "<a " not in description, \
        "schema prose holds format examples, which stay plain text"


def test_every_page_type_links_the_schema_reference():
    for kind, path in page_types().items():
        text = path.read_text(encoding="utf-8")
        nav = between(text, '<nav aria-label="Main navigation">', "</nav>")
        targets = [href for href, label in anchors(nav) if label == "Schema"]
        assert len(targets) == 1 and targets[0].endswith("schema.html"), kind
        assert any(label == "Schema reference" for _, label in anchors(footer(text))), kind


# --------------------------------------------------------------- downloads --

def test_landing_downloads_link_files_that_exist():
    downloads = between((PAGES / "index.html").read_text(encoding="utf-8"),
                        '<h2 id="downloads">', "</ul>")
    blob = "https://github.com/CultureBotAI/HabitatMech/blob/main/"
    for href, _ in anchors(downloads):
        if href.startswith(blob):
            assert (ROOT / href[len(blob):]).is_file(), href
    assert blob + "curation/term_requests.tsv" in [href for href, _ in anchors(downloads)]
    assert "schema.html" in [href for href, _ in anchors(downloads)]


# ------------------------------------------------------ responsive, theme --

def css_rule(css: str, selector: str) -> str:
    return between(css, selector + " {", "}")


def test_link_pills_wrap_and_the_narrow_grid_cannot_grow():
    css = (PAGES / "style.css").read_text(encoding="utf-8")
    pill = css_rule(css, "a.pill")
    assert "white-space: normal" in pill and "overflow-wrap: anywhere" in pill
    narrow = between(css, "@media (max-width: 860px) {", "\n}\n")
    assert "grid-template-columns: minmax(0, 1fr);" in css_rule(narrow, ".browse-layout")


def _luminance(hex_colour: str) -> float:
    channels = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def _contrast(a: str, b: str) -> float:
    high, low = sorted((_luminance(a), _luminance(b)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def test_landing_search_button_is_legible_in_every_theme():
    css = (PAGES / "style.css").read_text(encoding="utf-8")
    button = css_rule(css, ".hero-search button")
    assert "background: var(--accent)" in button and "color: var(--bg)" in button
    assert ".hero-search button" not in css.replace(".hero-search button {", "", 1), \
        "a theme-specific override is what left OS-dark readers at 1.95:1"
    blocks = {
        "light": between(css, ':root[data-theme="light"] {', "}"),
        "dark": between(css, ':root[data-theme="dark"] {', "}"),
        "OS dark": between(css, ':root:not([data-theme="light"]) {', "}"),
    }
    for theme, block in blocks.items():
        token = dict(re.findall(r"--([a-z-]+):\s*(#[0-9a-f]{6})", block))
        assert _contrast(token["bg"], token["accent"]) >= 4.5, theme


# ----------------------------------------------- text map and no-JS states --

def test_map_page_keeps_readers_in_the_licensed_wrapper():
    page = (PAGES / "text-map" / "index.html").read_text(encoding="utf-8")
    main = between(page, "<main", "</main>")
    assert "text-map-source/index.html" not in [href.split("?")[0] for href, _ in anchors(main)], \
        "the standalone map has no navigation, theme or licence of its own"
    assert 'src="../text-map-source/index.html"' in main
    table = between(main, '<details class="map-table" id="map-table">', "</details>")
    assert "<summary>View data as table</summary>" in table
    assert 'role="region" tabindex="0"' in table
    coverage = json.loads((PAGES / "text-map-source" / "manifest.json").read_text())["coverage"]
    assert f"It plots all {coverage['displayed']} records." in main


def test_every_map_point_opens_a_committed_record_page():
    points = json.loads((PAGES / "text-map-source" / "points.json").read_text(encoding="utf-8"))
    missing = [p["page"] for p in points if not (PAGES / p["page"]).is_file()]
    assert missing == []
    assert {Path(p["page"]).name for p in points} == set(corpus())


def test_script_driven_pages_say_what_works_without_javascript():
    for path, route in ((PAGES / "browse.html", "category"),
                        (PAGES / "category" / "aquatic.html", "pages below"),
                        (PAGES / "text-map" / "index.html", "../browse.html"),
                        (PAGES / "term-requests.html", "listed in the table")):
        notice = between(path.read_text(encoding="utf-8"), "<noscript>", "</noscript>")
        assert route in notice, path.name


def inline_script(template: str, **context) -> str:
    env = site.template_environment()
    env.globals["text_map_enabled"] = True
    page = env.get_template(template).render(stats={"total": 3}, root="", **context)
    scripts = re.findall(r"<script>(.*?)</script>", page, re.S)
    assert len(scripts) == 1, template
    return scripts[0]


SCRIPT_CONTEXT = {
    "browse.html": {"categories": [{"slug": "aquatic", "label": "AQUATIC", "count": 1,
                                    "grounded": 1, "description": ""}],
                    "groundings": [{"name": "EXACT", "count": 1}]},
    "category.html": {"category": "AQUATIC", "description": "", "records": [], "total": 468,
                      "page": 1, "pager": [], "index_url": "aquatic.json"},
    "text_map.html": {"categories": [], "groundings": [],
                      "map_coverage": {"displayed": 3, "total": 3}},
}


@needs_node
@pytest.mark.parametrize("template, scenario", [
    ("browse.html", "browse_answers_the_query_typed_while_the_indexes_load"),
    ("browse.html", "browse_names_a_failed_index_and_recovers_on_retry"),
    ("browse.html", "browse_network_error_is_reported_not_counted_as_empty"),
    ("browse.html", "browse_reaches_every_match_beyond_the_first_page"),
    ("browse.html", "browse_restores_only_values_the_page_offers"),
    ("category.html", "category_failed_index_offers_retry"),
    ("text_map.html", "map_table_lists_the_plotted_records_and_follows_the_search"),
    ("text_map.html", "map_failure_is_reported_and_the_table_still_loads"),
])
def test_shipped_page_script(tmp_path, template, scenario):
    script = tmp_path / "page.js"
    script.write_text(inline_script(template, **SCRIPT_CONTEXT[template]), encoding="utf-8")
    result = subprocess.run(["node", str(HARNESS), str(script), scenario],
                            capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, result.stdout + result.stderr
    assert f"passed: {scenario}" in result.stdout


def test_committed_pages_ship_the_scripts_the_harness_checks():
    for template, page in (("browse.html", "browse.html"),
                           ("category.html", "category/aquatic.html"),
                           ("text_map.html", "text-map/index.html")):
        committed = re.findall(r"<script>(.*?)</script>",
                               (PAGES / page).read_text(encoding="utf-8"), re.S)
        assert committed == [inline_script(template, **SCRIPT_CONTEXT[template])], page
