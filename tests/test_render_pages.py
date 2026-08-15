"""The site is generated, committed, and served — so it can lie or go stale.

These cover the two failure modes that actually happened: the honesty notice
rendering blank on every record page, and a corpus-wide count in a per-page
footer turning any one-record curation change into a 3,192-file diff.
"""

from __future__ import annotations

import re

import render_pages


def test_site_is_in_step_with_the_corpus():
    """pages/ is committed, so it drifts exactly as records could drift from
    data/raw/. Same gate as verify-corpus, for the site."""
    assert render_pages.main(["--check"]) == 0, "pages/ is stale; run `just render`"


def _footer(path) -> str:
    match = re.search(r"<footer.*?</footer>", path.read_text(encoding="utf-8"), re.S)
    assert match, f"no footer in {path}"
    return re.sub(r"\s+", " ", re.sub(r"<[^>]*>", "", match.group(0)))


def test_record_pages_carry_the_unreviewed_warning(repo_root):
    """The notice exists because a clean layout makes machine-generated data look
    authoritative. It was rendering as " of 3192 records are machine-generated"
    on all 3,192 record pages, because stats were computed after they were
    written (#31) — blank in precisely the place it is most needed."""
    pages = sorted((repo_root / "pages" / "habitats").glob("*.html"))
    assert pages, "no record pages rendered"
    for path in pages[:50]:
        text = _footer(path)
        assert "machine-generated and unreviewed" in text
        assert not re.search(r"(?<![\d]) of \d+ records", text), (
            f"{path.name}: footer has an unfilled count — stats were read before "
            "they were computed"
        )


def test_record_pages_carry_no_corpus_wide_counts(repo_root):
    """A mutable corpus-wide number in a per-page footer means every curation
    change rewrites all 3,192 pages, and pages/ is committed. Keep the counts on
    the overview, where one page changes instead."""
    total = len(list((repo_root / "data" / "habitats").rglob("*.yaml")))
    for path in sorted((repo_root / "pages" / "habitats").glob("*.html"))[:50]:
        assert str(total) not in _footer(path), (
            f"{path.name}: footer embeds a corpus-wide count, which churns the "
            "whole site on any corpus change"
        )


def test_nojekyll_is_present(repo_root):
    """Without it, Pages runs Jekyll and silently drops paths beginning with an
    underscore — a 404 rather than an error anyone sees (#32)."""
    assert (repo_root / "pages" / ".nojekyll").exists()


def test_every_retired_url_resolves_to_a_live_record(repo_root):
    """A record page is named after its label and identifier, so improving
    either moves the URL — which is most of what curation does. RETIRED.tsv is
    what keeps the old address resolving; a row pointing at a record that no
    longer exists is a 404 with extra steps (#54)."""
    import csv

    import yaml

    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    if not retired.exists():
        return
    live = set()
    for path in (repo_root / "data" / "habitats").rglob("*.yaml"):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and "identifier" in doc:
            live.add(doc["identifier"])
    with retired.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    assert rows, "no retired URLs recorded"
    dangling = [
        (r["retired_slug"], t)
        for r in rows
        for t in r["current_identifiers"].split("|")
        if t not in live
    ]
    assert not dangling, f"retired URLs pointing at records that do not exist: {dangling[:5]}"


def test_a_retired_slug_never_shadows_a_live_record(repo_root):
    """Writing a stub at a filename a live record uses would replace a real
    habitat with a redirect away from itself."""
    import csv
    import sys

    import yaml

    sys.path.insert(0, str(repo_root / "scripts"))
    from render_pages import slugify

    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    if not retired.exists():
        return
    live_slugs = set()
    for path in (repo_root / "data" / "habitats").rglob("*.yaml"):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and "identifier" in doc:
            live_slugs.add(slugify(f"{doc['label']}-{doc['identifier']}"))
    with retired.open(newline="", encoding="utf-8") as fh:
        collisions = [
            r["retired_slug"] for r in csv.DictReader(fh, delimiter="\t")
            if r["retired_slug"] in live_slugs
        ]
    assert not collisions, f"retired slugs shadowing live records: {collisions[:5]}"
