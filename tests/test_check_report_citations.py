"""Tests for scripts/check_report_citations.py."""

from __future__ import annotations

from scripts import check_report_citations


def test_user_agent_does_not_disclose_email_address():
    """External API User-Agent strings must not disclose personal/lab emails."""
    assert "mailto:" not in check_report_citations.USER_AGENT.lower()
    assert "@" not in check_report_citations.USER_AGENT
    assert check_report_citations.USER_AGENT == "HabitatMech-citation-check/1.0"


def test_normalise_strips_trailing_punctuation_and_publisher_suffixes():
    assert (
        check_report_citations.normalise("10.1038/s41564-024-01641-6/full).")
        == "10.1038/s41564-024-01641-6"
    )
    assert (
        check_report_citations.normalise("10.1128/AEM.01234-20(see")
        == "10.1128/AEM.01234-20"
    )
