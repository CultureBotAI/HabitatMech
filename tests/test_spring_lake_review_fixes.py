"""Exact context exclusions and independent sample/study denominators."""

import csv
from pathlib import Path

from habitatmech import seed

SPRINGS = {
    "habitatmech:GOLD.88f05b0e77": ("habitatmech:GOLD.22a80cbd14", 5, "gold.ecosystem:5961"),
    "habitatmech:GOLD.0584d2f783": ("habitatmech:GOLD.7f8e268653", 173, "gold.ecosystem:4654"),
}


def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_spring_context_exclusions_preserve_genus_and_all_other_records(monkeypatch):
    after = documents()
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda path: {key: row for key, row in exclusions.items() if key not in SPRINGS},
    )
    before = documents()
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == SPRINGS.keys()
    for identifier, (parent, count, node) in SPRINGS.items():
        old, new = before[identifier], after[identifier]
        assert old["parent_habitats"] == ["ENVO:00000027", parent]
        assert new["parent_habitats"] == ["ENVO:00000027"]
        assert new["curation_history"][:-1] == old["curation_history"]
        assert new["curation_history"][-1]["action"] == "SOURCE_PARENT_EXCLUDED"
        for field in old.keys() | new.keys():
            if field not in {"parent_habitats", "curation_history"}:
                assert old.get(field) == new.get(field), (identifier, field)
        assert new["grounding_status"] == "NARROW"
        assert new["mapping_status"] == "SEEDED"
        assert new["source_attestations"] == [{
            "source": "GOLD", "source_id": node, "source_label": "Spring",
            "source_path": exclusions[identifier].source_path,
            "mapping_predicate": "skos:narrowMatch", "assertion_count": count,
            "assertion_unit": "ORGANISM",
        }]


def test_subglacial_decision_uses_path_specific_independent_studies():
    root = Path(__file__).resolve().parents[1]
    with (root / "data/raw/gold_path_triads.tsv").open() as handle:
        triads = list(csv.DictReader(handle, delimiter="\t"))
    with (root / "data/raw/gold_studies.tsv").open() as handle:
        studies = list(csv.DictReader(handle, delimiter="\t"))
    for context, samples, expected_studies in (
        ("Deep subsurface", 3, {"Gs0112339"}),
        ("Freshwater", 7, {"Gs0114735", "Gs0128895", "Gs0154581"}),
    ):
        path = f"Environmental > Aquatic > {context} > Subglacial lake"
        rows = [r for r in triads if r["canonical_path"] == path and r["slot"] == "local"]
        assert len(rows) == 1
        assert int(rows[0]["samples"]) == samples
        assert int(rows[0]["studies"]) == len(expected_studies)
        assert rows[0]["top_term"] == "ENVO:03000120"
        assert rows[0]["top_share"] == "1.00"
        assert {r["study_gold_id"] for r in studies if path in r["paths"].split("|")} == expected_studies
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    deep = decisions["habitatmech:GOLD.7a082e8e9f"]
    assert deep.decision == "GROUND"
    assert deep.object_id == "ENVO:03000120"
    assert deep.review_depth == "ITEM"
    assert "3 API samples from 1 study, Gs0112339" in deep.notes
    assert "3 INDEPENDENT studies" not in deep.notes
    assert "3 INDEPENDENT studies" in decisions["habitatmech:GOLD.c5a94d7484"].notes


def test_corrected_decision_preserves_empty_tsv_fields_without_trailing_tabs():
    lines = seed.DECISIONS_PATH.read_text().splitlines()
    line = next(row for row in lines if row.startswith("habitatmech:GOLD.7a082e8e9f\t"))
    assert line == line.rstrip()
    row = next(csv.DictReader([lines[0], line], delimiter="\t"))
    assert len(row) == 11
    assert row["category"] == row["relation"] == ""
