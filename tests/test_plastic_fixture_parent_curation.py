"""Keep sampled surfaces and installed fixtures separate from their locations."""

from habitatmech import seed
from habitatmech.text_map_inputs import build_context, semantic_text

FIXTURE = "ENVO:01000989"
SURFACE = "habitatmech:GOLD.8ef066825a"
FIXTURE_SOURCE = "habitatmech:GOLD.e4509f5b53"
SOURCES = {FIXTURE_SOURCE, SURFACE}


def test_context_exclusions_preserve_all_other_claims_and_records(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    monkeypatch.setattr(
        seed, "load_gold_parent_exclusions",
        lambda _: {key: row for key, row in exclusions.items() if key not in SOURCES},
    )
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {FIXTURE, SURFACE}
    context = build_context(seed.REPO_ROOT)
    assert {key for key in before
            if semantic_text(before[key], context) != semantic_text(after[key], context)} == {
        FIXTURE, SURFACE,
    }

    for identifier, source, removed, retained in (
        (FIXTURE, FIXTURE_SOURCE, "ENVO:00000073", ["ENVO:00003074"]),
        (SURFACE, SURFACE, "habitatmech:GOLD.961229841c", []),
    ):
        old, new = before[identifier], after[identifier]
        exclusion = exclusions[source]
        assert exclusion.parent_id == removed
        assert old["parent_habitats"] == sorted([removed, *retained])
        assert new.get("parent_habitats", []) == retained
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-10T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert exclusion.notes in event["changes"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        attestation = new["source_attestations"][0]
        assert attestation["source_path"] == exclusion.source_path
        assert seed.mint("GOLD", attestation["source_path"]) == source

    fixture = after[FIXTURE]
    assert (fixture["grounding_status"], fixture["mapping_status"]) == ("BROAD", "REVIEWED")
    assert fixture["synonyms"] == [{
        "synonym_text": "Sink", "synonym_type": "RELATED_SYNONYM", "source": "GOLD",
    }]
    attestation = fixture["source_attestations"][0]
    assert attestation["mapping_predicate"] == "skos:broadMatch"
    assert (attestation["assertion_count"], attestation["assertion_unit"]) == (1, "ORGANISM")
    assert attestation["source_id"] == "gold.ecosystem:8365"
    assert attestation["source_path"] == "Engineered > Built environment > Building > Sink"
    assert "2 GOLD ecosystem node ids" in attestation["notes"]
    rows = {r["canonical_path"]: r for r in seed.read_tsv("gold_ecosystem_paths.tsv")}
    assert rows[attestation["source_path"]]["gold_node_ids"].split("|") == [
        "gold.ecosystem:8365", "gold.ecosystem:8366",
    ]

    surface = after[SURFACE]
    assert (surface["grounding_status"], surface["mapping_status"]) == ("UNGROUNDED", "SEEDED")
    assert surface["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:5466", "source_label": "Plastic surface",
        "source_path": "Engineered > Built environment > City > Subway > Plastic surface",
    }]
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    assert decisions[SURFACE].review_depth == "CLASS"
    assert decisions[FIXTURE_SOURCE].review_depth == "ITEM"
