"""The ENVO term-request batch: a public ask of volunteer editors.

Everything here exists because the request leaves the repo. A wrong parent, a
404 citation or a term we could have found ourselves costs someone else's time,
and unlike a record it cannot be quietly re-seeded afterwards.
"""

from __future__ import annotations

import csv
import sys

import pytest


@pytest.fixture(scope="module")
def requests_module(repo_root):
    sys.path.insert(0, str(repo_root / "scripts"))
    import build_term_requests

    return build_term_requests


def test_the_committed_table_is_what_the_generator_emits(requests_module, repo_root):
    """Same gate as pages/ and RETIRED.tsv: a generated artifact that is
    committed goes stale exactly as records can."""
    assert requests_module.main(["--check"]) == 0


def test_every_request_names_a_real_ungrounded_record_and_a_real_parent(
    requests_module, repo_root
):
    """`validate` raises on a malformed request. Running it over the committed
    file is what makes that gate real rather than available."""
    with (repo_root / "data" / "raw" / "ontology_terms.tsv").open(
        newline="", encoding="utf-8"
    ) as fh:
        labels = {r["term_id"]: r["label"] for r in csv.DictReader(fh, delimiter="\t")}
    corpus = requests_module.load_corpus()
    rows = requests_module.load_requests()
    assert rows, "no term requests on file"
    requests_module.validate(rows, corpus, labels)


def test_no_requested_term_already_exists_in_the_ontologies(requests_module, repo_root):
    """The failure this is here to prevent actually happened: two records were
    filed as "ENVO has no shared parent for plant- and animal-associated
    environment" when ENVO:01001000 had been in the vendored slice all along,
    and 28,888 upstream assertions sat ungrounded behind a false premise.

    Asking for a term that exists is the one mistake that makes an editor
    distrust the whole batch.
    """
    sys.path.insert(0, str(repo_root / "scripts"))
    from seed_from_sources import norm_label

    with (repo_root / "data" / "raw" / "ontology_terms.tsv").open(
        newline="", encoding="utf-8"
    ) as fh:
        known = {}
        for row in csv.DictReader(fh, delimiter="\t"):
            for name in [row["label"], *(row.get("synonyms") or "").split("|")]:
                key = norm_label(name)
                if key:
                    known.setdefault(key, (row["term_id"], row["label"]))

    clashes = [
        (r["requested_label"], known[norm_label(r["requested_label"])])
        for r in requests_module.load_requests()
        if norm_label(r["requested_label"]) in known
    ]
    assert not clashes, f"requesting terms that already exist: {clashes}"


def test_every_citation_url_resolves_to_a_rendered_page(requests_module, repo_root):
    """ENVO requires citable definition sources and they go in the issue, so a
    broken one is visible to everyone. The first version of this generator built
    the slug itself instead of using the renderer's and emitted 404s."""
    table = repo_root / "curation" / "term_requests" / "envo_robot_template.tsv"
    with table.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    assert rows, "the term-request table is empty"

    checked, missing = 0, []
    for row in rows:
        for url in row["definition cross reference"].split("|"):
            checked += 1
            page = repo_root / "pages" / "habitats" / url.rsplit("/", 1)[-1]
            if not page.exists():
                missing.append(url)
    assert checked, "no citation URLs to check"
    assert not missing, f"citation URLs with no page behind them: {missing[:5]}"


def test_created_by_is_left_empty_rather_than_guessed(requests_module, repo_root):
    """ENVO wants full ORCID IRIs. The generator cannot know them, and a guessed
    attribution on a public submission is worse than a blank one — so the column
    stays empty until a human fills it, and this records that as intent rather
    than an oversight."""
    table = repo_root / "curation" / "term_requests" / "envo_robot_template.tsv"
    with table.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    invented = [r["label"] for r in rows if (r.get("created by") or "").strip()]
    assert not invented, (
        f"created by is filled for {invented[:3]} — if a human set it, delete this "
        "test; if the generator did, it invented an attribution"
    )
