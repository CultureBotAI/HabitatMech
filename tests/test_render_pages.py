"""The site is generated, committed, and served — so it can lie or go stale.

These cover the two failure modes that actually happened: the honesty notice
rendering blank on every record page, and a corpus-wide count in a per-page
footer turning any one-record curation change into a 3,192-file diff.
"""

from __future__ import annotations

import re

from scripts import render_pages


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


def test_every_retired_slug_has_one_unambiguous_row(repo_root):
    """Duplicate map rows can disagree about the destination or page title."""
    import csv

    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    with retired.open(newline="", encoding="utf-8") as fh:
        slugs = [row["retired_slug"] for row in csv.DictReader(fh, delimiter="\t")]
    assert len(slugs) == len(set(slugs)), "RETIRED.tsv contains duplicate slugs"


def test_a_retired_slug_never_shadows_a_live_record(repo_root):
    """Writing a stub at a filename a live record uses would replace a real
    habitat with a redirect away from itself."""
    import csv

    import yaml

    from scripts.render_pages import slugify

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


def test_dead_page_identifier_survives_a_label_with_parentheses(repo_root):
    """A dead page's identifier is recovered from its meta description, which
    reads "{label} ({identifier}): ...". 37 records have a label containing its
    own parentheses — `Mixotrophic (MNF)`, `Rock-dwelling (endoliths)` — and a
    non-greedy leading match captures those instead. That would silently drop
    the redirect, which is the 404 this exists to prevent (#60)."""

    from scripts.build_redirects import _CURIE, _DESC_ID, _META_DESC

    def parse(desc: str) -> str:
        html = f'<meta name="description" content="{desc}">'
        match = _META_DESC.search(html)
        for m in reversed(list(_DESC_ID.finditer(match.group(1)))):
            if _CURIE.match(m.group(1).strip()):
                return m.group(1).strip()
        return ""

    assert parse("soil (ENVO:00001998): a microbial habitat.") == "ENVO:00001998"
    assert parse(
        "Rock-dwelling (endoliths) (habitatmech:GOLD.abc1234567): a habitat."
    ) == "habitatmech:GOLD.abc1234567"
    assert parse("Mixotrophic (MNF) (habitatmech:GOLD.0123456789): x.") == \
        "habitatmech:GOLD.0123456789"
    # A description with no identifier must yield nothing rather than guessing.
    assert parse("just some (prose) here.") == ""


def test_split_stubs_assert_no_canonical(repo_root):
    """A split stub deliberately declines to pick a target; asserting a
    canonical would tell search engines the opposite (#61)."""
    import csv

    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    pages = repo_root / "pages" / "habitats"
    if not retired.exists() or not pages.exists():
        return
    with retired.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            stub = pages / f"{row['retired_slug']}.html"
            if not stub.exists():
                continue
            html = stub.read_text(encoding="utf-8")
            if len(row["current_identifiers"].split("|")) > 1:
                assert "canonical" not in html, f"{stub.name} claims a canonical for a split"
                assert "http-equiv" not in html, f"{stub.name} auto-redirects a split"


def test_single_target_stubs_have_live_canonical_urls(repo_root):
    """A site base already ending in ``/pages/`` must not have ``pages/``
    appended again. The timed redirect can still work while the canonical URL
    sent to search engines points at a 404, so check both independently."""
    import csv

    import yaml

    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    pages = repo_root / "pages" / "habitats"
    if not retired.exists() or not pages.exists():
        return
    live_slugs = {}
    for path in (repo_root / "data" / "habitats").rglob("*.yaml"):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and "identifier" in doc:
            live_slugs[doc["identifier"]] = render_pages.slugify(
                f"{doc['label']}-{doc['identifier']}"
            )
    checked = 0
    with retired.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if len(row["current_identifiers"].split("|")) != 1:
                continue
            stub = pages / f"{row['retired_slug']}.html"
            if not stub.exists():
                continue
            html = stub.read_text(encoding="utf-8")
            match = re.search(r'<link rel="canonical" href="([^"]+)">', html)
            assert match, f"{stub.name} has no canonical URL"
            canonical = match.group(1)
            identifier = row["current_identifiers"]
            expected = f"{render_pages.SITE_BASE}habitats/{live_slugs[identifier]}.html"
            assert canonical == expected, (
                f"{stub.name} canonical does not match {identifier}: "
                f"expected {expected}, got {canonical}"
            )
            assert "/pages/pages/" not in canonical, (
                f"{stub.name} duplicates the site path in its canonical URL: {canonical}"
            )
            target = canonical.removeprefix(render_pages.SITE_BASE)
            assert (repo_root / "pages" / target).exists(), (
                f"{stub.name} canonical points at a missing generated page: {canonical}"
            )
            checked += 1
    assert checked, "no single-target redirect stubs were checked"


def test_not_applicable_guidance_does_not_reject_hosts(repo_root):
    guidance = render_pages.GROUNDING_MEANING["NOT_APPLICABLE"]
    assert "host taxon" not in guidance.lower()
    assert "disease" in guidance.lower() and "quality" in guidance.lower()
    homepage = (repo_root / "pages" / "index.html").read_text(encoding="utf-8")
    assert "Not a habitat at all — a host taxon" not in homepage


def test_every_stub_on_disk_has_a_row_in_the_map(repo_root):
    """A stub with no row is one the next render will prune, turning a working
    redirect back into a 404. That is how the map decayed: it was rebuilt from
    page deletions, and writing a stub replaces the page rather than deleting
    it, so the evidence disappeared one commit later (#64)."""
    import csv
    import re

    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    pages = repo_root / "pages" / "habitats"
    if not retired.exists() or not pages.exists():
        return
    with retired.open(newline="", encoding="utf-8") as fh:
        mapped = {r["retired_slug"] for r in csv.DictReader(fh, delimiter="\t")}
    stubs = {
        p.stem for p in pages.glob("*.html")
        if re.search(r"has moved — HabitatMech", p.read_text(encoding="utf-8"))
    }
    assert stubs, "no redirect stubs rendered"
    orphaned = sorted(stubs - mapped)
    assert not orphaned, f"stubs with no row in RETIRED.tsv: {orphaned[:5]}"


def test_consecutive_label_change_and_merge_preserve_both_urls(repo_root):
    """A label-change redirect remains public after its target is merged.

    The sponge concept exercised this exact two-release chain during #158:
    first its authored label moved the page, then duplicate-concept curation
    retired the identifier. Dropping the first stub would turn a URL published
    on main back into a 404.
    """
    import csv

    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    with retired.open(newline="", encoding="utf-8") as fh:
        rows = {
            row["retired_slug"]: row
            for row in csv.DictReader(fh, delimiter="\t")
        }
    expected_target = "habitatmech:GOLD.64acf9132c"
    for slug in (
        "sponge-habitatmech-gold-affd2445ea",
        "sponge-associated-environment-habitatmech-gold-affd2445ea",
    ):
        assert rows[slug]["current_identifiers"] == expected_target
        assert (repo_root / "pages" / "habitats" / f"{slug}.html").exists()


def test_category_pages_are_paginated_and_the_index_covers_the_whole_category(repo_root):
    """99% of a category page was its table body, and the biggest was 1641 rows
    in 461 KB — the likeliest first click from Browse. Paginating cuts that, but
    only helps if the filter still searches the WHOLE category: filtering the
    300 rows in front of you and calling it the answer for 1641 would be worse
    than the weight (#34)."""
    import json
    import re

    pages = repo_root / "pages" / "category"
    if not pages.exists():
        return
    biggest = max(pages.glob("*.html"), key=lambda p: p.stat().st_size)
    assert biggest.stat().st_size < 200_000, (
        f"{biggest.name} is {biggest.stat().st_size // 1024} KB; pagination has stopped working"
    )
    for index in pages.glob("*.json"):
        html = (pages / f"{index.stem}.html").read_text(encoding="utf-8")
        total = int(re.search(r'data-total="(\d+)"', html).group(1))
        entries = json.loads(index.read_text(encoding="utf-8"))
        assert len(entries) == total, (
            f"{index.name} holds {len(entries)} records but the page claims {total}; "
            "the filter would silently search a subset"
        )
        for _label, slug, *_ in entries[:50]:
            assert (repo_root / "pages" / "habitats" / f"{slug}.html").exists(), (
                f"{index.name} points at a record page that does not exist: {slug}"
            )
