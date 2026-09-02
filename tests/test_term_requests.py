"""The ENVO term-request batch: a public ask of volunteer editors.

Everything here exists because the request leaves the repo. A wrong parent, a
404 citation or a term we could have found ourselves costs someone else's time,
and unlike a record it cannot be quietly re-seeded afterwards.
"""

from __future__ import annotations

import csv

import pytest


@pytest.fixture(scope="module")
def requests_module(repo_root):
    from scripts import build_term_requests

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
    from habitatmech.seed import norm_label

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


@pytest.mark.parametrize(
    "synonym, why",
    [
        ("indoor-air", "a URL slug"),
        ("Indoor Air", "the label with different case"),
        ("indoor.air!", "the label with punctuation added"),
        ("---", "no letters or digits at all"),
    ],
)
def test_an_exact_synonym_must_be_a_distinct_name(requests_module, synonym, why):
    """An EXACT synonym asserts that people call the thing by that name.

    Both offenders this catches were committed and shipped through `just qc`
    before anyone read them (#213): `indoor-air`, a URL slug that reached the
    column by accident, and a label coined at authoring time to mirror the
    request. The mechanical half is testable, so it is tested; a coined name
    that reads like English still needs a human.
    """
    row = {
        "identifier": "habitatmech:GOLD.0000000000",
        "requested_label": "indoor air",
        "exact_synonym": synonym,
    }
    problems = requests_module._synonym_problems("prefix", row)
    assert problems, f"{synonym!r} ({why}) was accepted as an exact synonym"


def test_a_genuine_alternative_name_is_still_accepted(requests_module):
    """The guard must not swallow the column's actual purpose: `ambient air`
    and `room air` are real alternative names and are why the column exists."""
    row = {
        "identifier": "habitatmech:GOLD.0000000000",
        "requested_label": "outdoor air",
        "exact_synonym": "ambient air|room air",
    }
    problems = requests_module._synonym_problems("prefix", row)
    assert problems == [], problems


def test_no_request_adopts_a_genus_that_drags_in_a_false_ancestor(requests_module):
    """ENVO:01001176 is true of every aquatic-invertebrate host here and is
    still the wrong genus, which is why this needs a test rather than a rule.

    ENVO asserts it under two parents: ENVO:01001002 'animal-associated
    environment' and ENVO:01001055 'environment associated with an animal part
    or small animal'. Adopting it makes every descendant inherit a
    size-and-partonomy restriction that is false of a whole adult sponge,
    ascidian, oyster, giant clam or sea urchin -- so the record would publish a
    claim its own curation note rejects.

    ENVO's own modelling is the evidence: ENVO:01001179 'cnidarian-associated
    environment', the closest analogue and a taxon-scoped class over aquatic
    invertebrates, is asserted under ENVO:01001002 alone, and ENVO:01001176 has
    no children in the vendored slice at all.

    Two independently authored reports read that same fact in opposite
    directions and the corpus ended up encoding both answers over five records
    (#210). A rule stated only in a note does not survive the next report.
    """
    rows = requests_module.load_requests()
    offenders = [
        (row["identifier"], row["requested_label"])
        for row in rows
        if (row.get("parent_class") or "").strip() == "ENVO:01001176"
    ]
    assert not offenders, (
        "ENVO:01001176 adopted as a genus; use ENVO:01001002 and record why "
        f"in the note (#210): {offenders}"
    )


def test_the_aquatic_invertebrate_hosts_share_one_genus(requests_module):
    """The defect in #210 was not a wrong genus, it was two answers.

    Sea urchin refused ENVO:01001176 on an argument that applies just as well
    to oyster, bivalve, sponge and ascidian, which adopted it. Whichever genus
    is chosen, these five have to agree, and a sixth record joining the family
    later must not quietly pick the other one.
    """
    family = {
        "habitatmech:GOLD.fd2443a2c3",  # oyster
        "habitatmech:GOLD.59e8d1205d",  # bivalve
        "habitatmech:GOLD.64acf9132c",  # sponge
        "habitatmech:GOLD.34c28836da",  # ascidian
        "habitatmech:GOLD.b19422ad27",  # sea urchin
    }
    genera = {
        row["identifier"]: (row.get("parent_class") or "").strip()
        for row in requests_module.load_requests()
        if row["identifier"] in family
    }
    assert set(genera) == family, f"family member lost its request: {family - set(genera)}"
    assert len(set(genera.values())) == 1, f"aquatic-invertebrate hosts disagree: {genera}"
