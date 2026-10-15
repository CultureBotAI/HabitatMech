"""New annotation provenance must render a usable issue link."""

from html.parser import HTMLParser


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.append(dict(attrs).get("href"))


def test_air_sac_annotation_links_exact_issue(repo_root):
    parser = Links()
    parser.feed((repo_root / "pages/habitats/air-sac-uberon-0009060.html").read_text())
    issue = "https://github.com/CultureBotAI/HabitatMech/issues/2148"
    assert issue in parser.hrefs
    assert issue + ";" not in parser.hrefs
