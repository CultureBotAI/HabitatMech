"""Identity correction preserves source URLs without redirecting the generic genus."""

import csv


def test_abdominal_source_url_redirect_does_not_capture_generic_abscess_links(repo_root):
    old_slug = "abscess-mesh-d000038"
    new_slug = "abscess-habitatmech-gold-9c78e65e82"
    with (repo_root / "data/habitats/RETIRED.tsv").open(newline="") as handle:
        redirects = {r["retired_slug"]: r for r in csv.DictReader(handle, delimiter="\t")}
    assert redirects[old_slug]["current_identifiers"] == "habitatmech:GOLD.9c78e65e82"
    assert new_slug in (repo_root / "pages/habitats" / f"{old_slug}.html").read_text()
    for suffix in ["5d784b0218", "d1d916a248", "8423e76015", "9c78e65e82",
                   "f007734d4a", "6d1b8fc8fc", "9c459b5a33"]:
        page = (repo_root / "pages/habitats" / f"abscess-habitatmech-gold-{suffix}.html")
        html = page.read_text()
        assert 'href="https://id.nlm.nih.gov/mesh/D000038.html"' in html
        assert f'href="../habitats/{old_slug}.html"' not in html
