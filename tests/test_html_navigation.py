"""Published table and bypass navigation contracts."""
from html.parser import HTMLParser
from pathlib import Path


class Structure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.tables = []
        self.mains = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "main":
            self.mains.append(attrs)
        if tag == "a":
            self.links.append(attrs)
        if tag == "table":
            self.tables.append(self.stack[-1])
        if tag not in {"meta", "link", "input", "br", "hr", "img"}:
            self.stack.append((tag, attrs))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break


def test_published_tables_have_keyboard_scroll_regions_and_main_landmark():
    root = Path(__file__).resolve().parents[1] / "pages"
    paths = [root / "index.html", root / "browse.html", root / "term-requests.html",
             *sorted((root / "category").glob("*.html")),
             *sorted((root / "habitats").glob("*.html"))[:10]]
    for path in paths:
        page = Structure()
        page.feed(path.read_text())
        assert page.mains == [{"id": "main-content", "tabindex": "-1"}], path
        assert any(a.get("href") == "#main-content" for a in page.links), path
        assert any(a.get("href") == "https://culturebotai.github.io/mechs/" for a in page.links), path
        for tag, attrs in page.tables:
            assert tag == "div" and attrs.get("class") == "table-scroll", path
            assert attrs.get("role") == "region" and attrs.get("tabindex") == "0", path
            assert attrs.get("aria-label"), path
