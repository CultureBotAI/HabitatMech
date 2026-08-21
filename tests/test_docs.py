"""Documentation that claims to be current is generated from the corpus."""

from __future__ import annotations

import re

import pytest

from scripts import check_docs


def test_readme_corpus_statistics_are_current():
    current = check_docs.README.read_text(encoding="utf-8")
    expected = check_docs.update_readme(
        current, check_docs.statistics_block(check_docs.load_records())
    )
    assert current == expected, "README corpus statistics are stale; run `just docs-stats`"


def test_statistics_markers_must_be_unique():
    block = f"{check_docs.START}\nold\n{check_docs.END}"
    duplicated = f"{block}\n{block}"
    try:
        check_docs.update_readme(duplicated, block)
    except ValueError as exc:
        assert "exactly once" in str(exc)
    else:
        raise AssertionError("duplicate generated-statistics markers were accepted")


def test_repository_owned_github_pages_links_resolve():
    """Prominent README links must name files that are actually published."""
    readme = check_docs.README.read_text(encoding="utf-8")
    prefix = "https://culturebotai.github.io/HabitatMech/"
    urls = re.findall(rf"{re.escape(prefix)}[^\s)>]+", readme)
    assert urls, "README has no repository-owned GitHub Pages links to check"
    missing = [url for url in urls if not (check_docs.REPO_ROOT / url.removeprefix(prefix)).is_file()]
    assert not missing, f"README links to unpublished GitHub Pages files: {missing}"


def test_statistics_include_unfamiliar_category_and_grounding_values():
    records = [
        {
            "habitat_category": "NEW_CATEGORY",
            "grounding_status": "NEW_GROUNDING",
            "mapping_status": "SEEDED",
            "source_attestations": [],
        }
    ]
    block = check_docs.statistics_block(records)
    assert "| NEW_CATEGORY | 1 |" in block
    assert "| NEW_GROUNDING | 1 |" in block


def test_statistics_reject_an_unaccounted_mapping_status():
    records = [
        {
            "habitat_category": "OTHER",
            "grounding_status": "UNGROUNDED",
            "mapping_status": "PENDING",
            "source_attestations": [],
        }
    ]
    with pytest.raises(ValueError, match="do not partition"):
        check_docs.statistics_block(records)
