"""Digestate source context must not turn residual material into a vessel."""

from habitatmech import seed
from habitatmech.text_map_inputs import build_context, semantic_text


DIGESTATES = {
    "habitatmech:GOLD.28f661cad5": (
        "Engineered > Bioreactor > Semi-continuous > Anaerobic > Digestate",
        "gold.ecosystem:7769",
    ),
    "habitatmech:GOLD.3b22aa41ac": (
        "Engineered > Bioreactor > SSF (Solid state fermentation) > Anaerobic > Digestate",
        "gold.ecosystem:8153",
    ),
}


def test_digestate_exclusions_change_only_two_context_edges_and_audit(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert DIGESTATES.keys() <= exclusions.keys()
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in DIGESTATES
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == DIGESTATES.keys()
    context = build_context(seed.REPO_ROOT)
    assert {key for key in before
            if semantic_text(before[key], context) != semantic_text(after[key], context)} == (
        DIGESTATES.keys()
    )
    rows = {row["canonical_path"]: row for row in seed.read_tsv("gold_ecosystem_paths.tsv")}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    for identifier, (path, node) in DIGESTATES.items():
        old, new = before[identifier], after[identifier]
        assert seed.mint("GOLD", path) == identifier
        assert exclusions[identifier].source_path == path
        assert exclusions[identifier].parent_id == "ENVO:00002124"
        assert old["parent_habitats"] == ["ENVO:00002124"]
        assert "parent_habitats" not in new
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-08T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert identifier in event["changes"] and "ENVO:00002124" in event["changes"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        assert decisions[identifier].review_depth == "CLASS"
        assert new["grounding_status"] == "UNGROUNDED"
        assert new["mapping_status"] == "SEEDED"
        assert new["habitat_category"] == "ENGINEERED"
        assert rows[path]["gold_node_ids"] == node
        attestation, = new["source_attestations"]
        assert attestation == {
            "source": "GOLD", "source_id": node,
            "source_label": "Digestate", "source_path": path,
        }
