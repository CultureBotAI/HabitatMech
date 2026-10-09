"""Keep pollutant aliases and refinery location out of habitat equivalence."""

import pytest

from habitatmech import seed
from habitatmech.text_map_inputs import build_context, semantic_text


@pytest.mark.parametrize(
    "identifier,loader,path_constant,changed_field,event_action",
    [
        (
            "habitatmech:GOLD.1a78606807",
            "load_definition_source_label_exclusions",
            "DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH",
            "synonyms",
            "SOURCE_SYNONYM_EXCLUDED",
        ),
        (
            "habitatmech:GOLD.c98a35c438",
            "load_gold_parent_exclusions",
            "GOLD_PARENT_EXCLUSIONS_PATH",
            "parent_habitats",
            "SOURCE_PARENT_EXCLUDED",
        ),
    ],
)
def test_guarded_fix_preserves_other_claims_and_entire_corpus(
    monkeypatch, identifier, loader, path_constant, changed_field, event_action,
):
    exclusions = getattr(seed, loader)(getattr(seed, path_constant))
    exclusion = exclusions[identifier]
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    monkeypatch.setattr(
        seed, loader,
        lambda _: {key: row for key, row in exclusions.items() if key != identifier},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    context = build_context(seed.REPO_ROOT)
    assert {key for key in before
            if semantic_text(before[key], context) != semantic_text(after[key], context)} == {
        identifier,
    }
    old, new = before[identifier], after[identifier]
    assert not new.get(changed_field)
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["action"] == event_action
    assert event["timestamp"] == "2026-10-09T00:00:00Z"
    assert event["curator"] == "codex-gpt-5"
    assert exclusion.notes in event["changes"]
    for field in (old.keys() | new.keys()) - {changed_field, "curation_history"}:
        assert new.get(field) == old.get(field), field
    assert new["grounding_status"] == "UNGROUNDED"
    assert new["habitat_category"] == "ENGINEERED"
    source, = new["source_attestations"]
    assert source["source"] == "GOLD"
    assert source["assertion_unit"] == "ORGANISM"
    assert "mapping_predicate" not in source
    assert seed.mint("GOLD", source["source_path"]) == identifier
    row = next(row for row in seed.read_tsv("gold_ecosystem_paths.tsv")
               if row["canonical_path"] == source["source_path"])
    decision = seed.load_decisions(seed.DECISIONS_PATH)[identifier]

    if changed_field == "synonyms":
        assert exclusion.source_label == "Persistent organic pollutants (POP)"
        assert exclusion.requested_label == new["label"]
        assert old["synonyms"] == [{
            "synonym_text": exclusion.source_label,
            "synonym_type": "EXACT_SYNONYM",
            "source": "HabitatMech curation",
        }]
        assert new["label"] == "persistent organic pollutant bioremediation material"
        assert new["parent_habitats"] == ["ENVO:00010483", "habitatmech:GOLD.5f0e9e816a"]
        assert new["definition_source"] == "HabitatMech"
        assert new["mapping_status"] == "REVIEWED"
        assert decision.review_depth == "ITEM"
        assert source["source_label"] == exclusion.source_label
        assert source["source_path"] == (
            "Engineered > Bioremediation > Persistent organic pollutants (POP)"
        )
        assert source["source_id"] == "gold.ecosystem:3528"
        assert source["assertion_count"] == 9
        assert row["gold_node_ids"].split("|") == [
            "gold.ecosystem:3528", "gold.ecosystem:4723", "gold.ecosystem:4724",
        ]
    else:
        assert old["parent_habitats"] == ["ENVO:03600078"]
        assert exclusion.parent_id == "ENVO:03600078"
        assert exclusion.source_path == source["source_path"] == (
            "Engineered > Built environment > Oil refinery > Petroleum sludge"
        )
        assert new["label"] == source["source_label"] == "Petroleum sludge"
        assert new["mapping_status"] == "SEEDED"
        assert decision.review_depth == "CLASS"
        assert source["source_id"] == "gold.ecosystem:4518"
        assert source["assertion_count"] == 1
        assert row["gold_node_ids"].split("|") == [
            "gold.ecosystem:4518", "gold.ecosystem:4519",
        ]
        assert new.get("definition") is None
        sibling = after["habitatmech:GOLD.2bc7edd546"]
        assert sibling["parent_habitats"] == ["habitatmech:GOLD.808ed1c989"]
        assert sibling["source_attestations"][0]["assertion_count"] == 2
