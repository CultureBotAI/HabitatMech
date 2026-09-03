"""The site is generated, committed, and served — so it can lie or go stale.

These cover the two failure modes that actually happened: the honesty notice
rendering blank on every record page, and a corpus-wide count in a per-page
footer turning any one-record curation change into a 3,192-file diff.
"""

from __future__ import annotations

import re
from pathlib import Path

from scripts import render_pages


def test_site_is_in_step_with_the_corpus():
    """pages/ is committed, so it drifts exactly as records could drift from
    data/raw/. Same gate as verify-corpus, for the site."""
    assert render_pages.main(["--check"]) == 0, "pages/ is stale; run `just render`"


def test_every_landing_stat_is_a_link_to_a_matching_view(repo_root):
    landing = (repo_root / "src/habitatmech/templates/index.html").read_text(
        encoding="utf-8"
    )

    assert '<div class="card"><div class="n">' not in landing
    assert landing.count('<a class="card" href=') == 6
    for target in (
        "browse.html",
        "index.html#grounding-status",
        "index.html#source-corroboration",
        "index.html#review-status",
        "index.html#novelty",
    ):
        assert f'href="{target}"' in landing
    assert landing.count('href="index.html#novelty"') == 2
    assert (
        '<a class="card" href="term-requests.html"><div class="n">{{ stats.novel }}'
        not in landing
    )


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


def test_label_change_stubs_do_not_claim_the_record_was_retired(repo_root):
    """A label move keeps the identifier live, so its redirect must not use
    the merge/reground copy that says the record no longer exists."""
    import csv

    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    pages = repo_root / "pages" / "habitats"
    checked = 0
    with retired.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["resolved_by"] != "label_changed":
                continue
            stub = pages / f"{row['retired_slug']}.html"
            html = stub.read_text(encoding="utf-8")
            assert "is no longer a record of its own" not in html
            assert "is still a live record" in html
            assert row["retired_identifier"] in html
            checked += 1
    assert checked, "no label-change redirect stubs were checked"


def test_merged_single_target_stubs_still_explain_identity_retirement(repo_root):
    """Reason-aware label copy must not soften redirects for records whose
    source concepts really were merged into a different identity."""
    import csv

    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    pages = repo_root / "pages" / "habitats"
    with retired.open(newline="", encoding="utf-8") as fh:
        rows = [
            row for row in csv.DictReader(fh, delimiter="\t")
            if row["resolved_by"] != "label_changed"
            and len(row["current_identifiers"].split("|")) == 1
        ]
    assert rows, "no merged single-target redirect stubs were checked"
    for row in rows:
        html = (pages / f"{row['retired_slug']}.html").read_text(encoding="utf-8")
        assert "is no longer a record of its own" in html


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


def test_carry_forward_does_not_read_the_rendered_stubs(repo_root, monkeypatch):
    """Which redirects are live is read from the map, never from page wording.

    It was read from page wording once: a `git grep` for the literal
    "has moved — HabitatMech", which duplicates `redirect.html`'s title block.
    Rewording that title made the grep match nothing, and the carry-forward then
    dropped a published URL *silently* — 138 rows to 137, losing exactly the one
    #159 exists to save, with `just redirects` writing the smaller file without
    complaint (#162).

    The sponge test above catches that, but only as a KeyError on two hardcoded
    slugs. This pins the mechanism instead: no page content may reach the
    decision, so no amount of template editing can shrink the map.
    """
    import csv
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    import build_redirects

    real_git = build_redirects.git

    def no_page_reads(*args: str, **kwargs) -> str:
        assert "grep" not in args, (
            "committed_redirect_slugs is reading rendered pages again; a "
            "template reword would silently drop published redirects (#162)"
        )
        return real_git(*args, **kwargs)

    monkeypatch.setattr(build_redirects, "git", no_page_reads)
    live = build_redirects.committed_redirect_slugs()

    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    with retired.open(newline="", encoding="utf-8") as fh:
        mapped = {r["retired_slug"] for r in csv.DictReader(fh, delimiter="\t")}
    assert live, "no committed redirects found — the carry-forward is inert"
    # Append-only, not equality. The working map GAINS a row every time a
    # curator retires a URL, and asserting equality failed on that ordinary loop
    # while printing `live - mapped` — an empty set — as the explanation (#177).
    lost = sorted(live - mapped)
    assert not lost, f"published redirects dropped by a rebuild: {lost[:5]}"


LIVE_ID = "habitatmech:GOLD.aaaaaaaaaa"
LIVE_SLUG = "live-habitat-habitatmech-gold-aaaaaaaaaa"
RELABELLED_SLUG = "old-label-habitatmech-gold-aaaaaaaaaa"
ORPHAN_SLUG = "gone-habitat-habitatmech-gold-bbbbbbbbbb"


def _miniature_world(monkeypatch, tmp_path, retractions: str = ""):
    """Stand `build()` up on a two-URL corpus instead of the real one.

    A full build walks 3300 records and the whole page history and takes ~45
    seconds, which is too slow to run once per retraction case — and the cases
    are about control flow, not about the corpus. Every collaborator is
    replaced; `load_retractions`, `slug_for` and `build` itself are the real
    ones, which is the point.

    The world holds exactly two dead URLs, one per code path that has to honour
    a retraction: `RELABELLED_SLUG`, which the derivation loop regenerates from
    the live record on every run, and `ORPHAN_SLUG`, a carried-forward row whose
    target no longer exists anywhere — the case that makes `build` raise.
    """
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
    import build_redirects

    live = {
        "identifier": LIVE_ID,
        "label": "Live habitat",
        "source_attestations": [{"source_id": "gold.ecosystem:1"}],
    }
    monkeypatch.setattr(
        build_redirects, "load_corpus",
        lambda: ({LIVE_ID: live}, {"gold.ecosystem:1": LIVE_ID}))
    monkeypatch.setattr(build_redirects, "retired_record_details", lambda: ({}, {}))
    monkeypatch.setattr(
        build_redirects, "ever_published_slugs",
        lambda: {LIVE_SLUG, RELABELLED_SLUG, ORPHAN_SLUG})
    monkeypatch.setattr(build_redirects, "retired_map_history", lambda: {
        ORPHAN_SLUG: {
            "retired_slug": ORPHAN_SLUG,
            "retired_identifier": "habitatmech:GOLD.bbbbbbbbbb",
            "retired_label": "Gone habitat",
            "current_identifiers": "habitatmech:GOLD.cccccccccc",
            "resolved_by": "source_concepts_merged",
        },
    })
    monkeypatch.setattr(
        build_redirects, "committed_redirect_slugs", lambda: {ORPHAN_SLUG})

    path = tmp_path / "redirects_retracted.tsv"
    path.write_text(
        "retired_slug\tcurator\tdate\twhy_retracted\n" + retractions,
        encoding="utf-8")
    monkeypatch.setattr(build_redirects, "RETRACTED_PATH", path)
    return build_redirects


def test_a_retraction_withdraws_a_redirect_the_rebuild_would_regenerate(
        monkeypatch, tmp_path):
    """The escape hatch #178 said did not exist.

    Deleting a row from RETIRED.tsv never retracted anything: the builder reads
    the COMMITTED map, so the row came back on the next `just redirects` and
    `--check` called the edited file stale in between. Both halves are asserted
    here from one world — the redirect is regenerated without a retraction row
    and gone with one.
    """
    # The orphan is retracted in BOTH builds; it is the other test's subject and
    # would otherwise raise here before the row under test is reached.
    baseline = f"{ORPHAN_SLUG}\tcurator\t2026-08-25\tNot this test's subject.\n"

    build_redirects = _miniature_world(monkeypatch, tmp_path, baseline)
    before = {row["retired_slug"] for row in build_redirects.build()}
    assert RELABELLED_SLUG in before, (
        "fixture is inert: the derivation loop is not producing the row a "
        "retraction is supposed to remove")

    build_redirects = _miniature_world(
        monkeypatch, tmp_path, baseline
        + f"{RELABELLED_SLUG}\tcurator\t2026-08-25\tPointed at the wrong habitat.\n")
    after = {row["retired_slug"] for row in build_redirects.build()}
    assert RELABELLED_SLUG not in after
    assert before - after == {RELABELLED_SLUG}, (
        "a retraction removed more than the row it names")


def test_a_retraction_can_withdraw_a_carried_forward_redirect_with_no_live_target(
        monkeypatch, tmp_path):
    """The carry-forward is checked BEFORE the target is resolved, deliberately.

    A redirect whose targets have all died is exactly the one a curator needs to
    withdraw, and that path raises rather than returning a row — so a retraction
    applied afterwards would never be reached.
    """
    import pytest

    build_redirects = _miniature_world(monkeypatch, tmp_path)
    with pytest.raises(SystemExit, match="cannot carry forward"):
        build_redirects.build()

    build_redirects = _miniature_world(
        monkeypatch, tmp_path,
        f"{ORPHAN_SLUG}\tcurator\t2026-08-25\tThe concept was never absorbed.\n")
    assert ORPHAN_SLUG not in {r["retired_slug"] for r in build_redirects.build()}


def test_retracting_a_slug_that_was_never_published_is_an_error(monkeypatch, tmp_path):
    """A tombstone is a claim that a URL exists; a typo silently retracts nothing.

    Checked against every page the branch has ever held rather than against this
    run's rows, because a retraction stops the slug being generated — a check
    against the current rows would start failing the moment it took effect.
    """
    import pytest

    build_redirects = _miniature_world(
        monkeypatch, tmp_path,
        "live-habitat-habitatmech-gold-typo\tcurator\t2026-08-25\tOops.\n")
    with pytest.raises(SystemExit, match="never contained"):
        build_redirects.build()


def test_a_retraction_must_say_who_and_why(monkeypatch, tmp_path):
    """Unpublishing a citable URL returns it to a 404. That needs an author and a
    reason on the record, like every other decision in curation/."""
    import pytest

    for row in (f"{RELABELLED_SLUG}\t\t2026-08-25\tNo curator.\n",
                f"{RELABELLED_SLUG}\tcurator\t2026-08-25\t\n"):
        build_redirects = _miniature_world(monkeypatch, tmp_path, row)
        with pytest.raises(SystemExit, match="needs a"):
            build_redirects.load_retractions()

    build_redirects = _miniature_world(
        monkeypatch, tmp_path,
        f"{RELABELLED_SLUG}\tcurator\t2026-08-25\tOnce.\n"
        f"{RELABELLED_SLUG}\tcurator\t2026-08-25\tTwice.\n")
    with pytest.raises(SystemExit, match="retracted twice"):
        build_redirects.load_retractions()

    build_redirects = _miniature_world(
        monkeypatch, tmp_path, "\tcurator\t2026-08-25\tSlug left blank.\n")
    with pytest.raises(SystemExit, match="names no URL"):
        build_redirects.load_retractions()


def test_a_tab_in_the_reason_fails_instead_of_truncating_it(monkeypatch, tmp_path):
    """The file exists so an unpublished URL has a stated justification. A tab
    anywhere in why_retracted sent the tail of the reason to DictReader's
    unnamed overflow key and the retraction proceeded on a fragment — the three
    required-column checks all pass, because what survives is non-empty (#195).

    A tab in prose is what a spreadsheet paste produces, so this is a curator
    typo, not an exotic input.
    """
    import pytest

    build_redirects = _miniature_world(
        monkeypatch, tmp_path,
        f"{RELABELLED_SLUG}\tcurator\t2026-08-25\tReason with a\tstray tab.\n")
    with pytest.raises(SystemExit, match="contains a tab"):
        build_redirects.load_retractions()

    # The overflow key holds a LIST, so it is rejected before anything iterates
    # row.values() — otherwise the blank-line guard raises AttributeError on it.
    build_redirects = _miniature_world(
        monkeypatch, tmp_path, "\t\t\t\tstray tab on an otherwise blank row\n")
    with pytest.raises(SystemExit, match="contains a tab"):
        build_redirects.load_retractions()


def test_retracting_a_live_records_own_url_is_an_error(monkeypatch, tmp_path):
    """`published` includes pages that still exist, so the never-published guard
    lets this through — but `build` only ever emits slugs that are NOT live, so
    no row can match one. A curator naming the new URL instead of the old one
    would otherwise get a clean run and no retraction (#188)."""
    import pytest

    build_redirects = _miniature_world(
        monkeypatch, tmp_path,
        f"{LIVE_SLUG}\tcurator\t2026-08-25\tNamed the wrong end of the move.\n")
    with pytest.raises(SystemExit, match="live record's own page"):
        build_redirects.build()


def test_a_retraction_row_is_permanent_for_a_regenerated_redirect(
        monkeypatch, tmp_path):
    """Retraction is NOT equally permanent for the two kinds of row, and this
    pins the half that is not.

    A carried-forward row stays withdrawn once committed: HEAD's map no longer
    offers it. A derived row does not — it is rebuilt every run from the live
    corpus and from every page the branch has ever held, so the tombstone is the
    only thing suppressing it. Deleting a row that looks spent republishes a
    redirect a curator withdrew because it was wrong (#189).
    """
    baseline = f"{ORPHAN_SLUG}\tcurator\t2026-08-25\tNot this test's subject.\n"
    withdrawn = (baseline
                 + f"{RELABELLED_SLUG}\tcurator\t2026-08-25\tWrong habitat.\n")

    build_redirects = _miniature_world(monkeypatch, tmp_path, withdrawn)
    assert RELABELLED_SLUG not in {r["retired_slug"] for r in build_redirects.build()}

    build_redirects = _miniature_world(monkeypatch, tmp_path, baseline)
    assert RELABELLED_SLUG in {r["retired_slug"] for r in build_redirects.build()}, (
        "dropping the tombstone no longer republishes a derived redirect; if "
        "that is now deliberate, docs/CURATION.md says otherwise (#189)")


def test_the_committed_retraction_file_parses_and_nothing_it_names_is_published(
        repo_root):
    """The real curation/redirects_retracted.tsv, without the 45-second build.

    Catches a malformed or half-applied tombstone: a row whose slug is still in
    the published map means the retraction was written but never rebuilt.
    """
    import csv
    import sys

    sys.path.insert(0, str(repo_root / "scripts"))
    import build_redirects

    retracted = build_redirects.load_retractions()
    retired = repo_root / "data" / "habitats" / "RETIRED.tsv"
    with retired.open(newline="", encoding="utf-8") as fh:
        mapped = {r["retired_slug"] for r in csv.DictReader(fh, delimiter="\t")}
    still_live = sorted(set(retracted) & mapped)
    assert not still_live, (
        f"retracted but still published: {still_live}; run `just redirects` "
        "and `just render`")


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
