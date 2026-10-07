"""Regressions for the published-site audit #1504–#1511."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from scripts import render_pages as site


def environment():
    env = Environment(loader=FileSystemLoader(site.TEMPLATES_DIR),
                      autoescape=select_autoescape(['html']))
    env.filters['graph_svg'] = lambda value, *_: ''
    return env


def test_mesh_resolver_accepts_canonical_descriptors_and_keeps_unknowns_unlinked():
    assert site.term_iri('mesh:D000038') == 'https://id.nlm.nih.gov/mesh/D000038.html'
    assert site.term_iri('MESH:D013492') == 'https://id.nlm.nih.gov/mesh/D013492.html'
    assert site.term_iri('mesh:invalid') is None
    assert site.term_iri('unknown:123') is None


def test_curation_urls_are_escaped_clickable_and_preserve_punctuation():
    notes = '<script>bad()</script> Read (https://pubmed.ncbi.nlm.nih.gov/10731891/). plain text.'
    html = environment().get_template('habitat.html').render(r={
        'decisions': [{'changes': notes}], 'sources': [], 'label': 'fixture'}, stats={})
    assert 'href="https://pubmed.ncbi.nlm.nih.gov/10731891/"' in html
    assert '&lt;script&gt;bad()&lt;/script&gt;' in html
    assert '</a>). plain text.' in html
    assert 'rel="noopener noreferrer"' in html


def test_reviewed_biofilm_pages_have_exact_pubmed_links(repo_root):
    class Links(HTMLParser):
        def __init__(self):
            super().__init__()
            self.hrefs = []

        def handle_starttag(self, tag, attrs):
            if tag == "a":
                self.hrefs.extend(value for name, value in attrs if name == "href")

    for identifier, pmid in [
        ("6b1f16702e", "18615526"), ("b77f846671", "20714445"),
        ("5eaebd18a7", "20714445"),
    ]:
        page = repo_root / f"pages/habitats/biofilm-habitatmech-gold-{identifier}.html"
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        assert [href for href in parser.hrefs if "pubmed.ncbi.nlm.nih.gov" in href] == [
            f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        ]


def test_term_request_keeps_full_long_and_short_rationales():
    long = 'explanation ' * 35 + 'final words'
    html = environment().get_template('term_requests.html').render(
        requests=[{'label': 'long', 'note': long}, {'label': 'short', 'note': 'Short reason.'}], stats={})
    assert long in html and 'Short reason.' in html
    # Verify the projection feeding this template no longer slices source notes.
    source = Path(site.__file__).read_text()
    assert 'decision.get("notes", "")[:220]' not in source


def test_status_copy_does_not_infer_human_review():
    html = environment().get_template('index.html').render(stats={})
    assert 'REVIEWED status' in html
    assert 'counts do not establish human review' in html
    assert 'have had no human review' not in html


def test_map_shell_keeps_site_navigation_and_unchanged_bundle_destination():
    html = environment().get_template('text_map.html').render(root='../', stats={}, text_map_enabled=True)
    for expected in ('href="../index.html"', 'href="../browse.html"', 'All Mech projects',
                     'creativecommons.org/licenses/by/4.0/', 'LICENSE-CODE',
                     'src="../text-map-source/index.html"', "anchor.target = '_top'"):
        assert expected in html


def test_custom_404_links_recover_from_nested_missing_paths():
    html = environment().get_template('not_found.html').render(root=site.SITE_BASE, stats={})
    assert f'href="{site.SITE_BASE}browse.html"' in html
