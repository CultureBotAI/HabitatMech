"""Source cultivation and conversion contexts are not material superclasses."""

from habitatmech import seed

CASES = (
    (
        "habitatmech:GOLD.c7e1dbc6bb", "habitatmech:GOLD.c7e1dbc6bb",
        "habitatmech:GOLD.55a9660503",
        "Engineered > Lab culture > Culture media > Fungi > Co-culture",
        {"gold.ecosystem:7777"}, [], "UNGROUNDED",
    ),
    (
        "habitatmech:GOLD.6a8d0ed24a", "habitatmech:GOLD.6a8d0ed24a",
        "habitatmech:GOLD.5871068dfe",
        "Engineered > Lab culture > Culture media > Bacteria > Co-culture",
        {"gold.ecosystem:6000"}, [], "UNGROUNDED",
    ),
    (
        "ENVO:02000091", "habitatmech:GOLD.d30d9c1ae1",
        "habitatmech:GOLD.7df92c13b7",
        "Engineered > Biotransformation > Coal",
        {"gold.ecosystem:5393", "gold.ecosystem:5394", "gold.ecosystem:5395"},
        ["ENVO:00002016"], "EXACT",
    ),
)


def test_coculture_coal_exclusions_change_only_parents_and_audit(monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    sources = {case[1] for case in CASES}
    exclusions = {
        key: row for key, row in seed.load_gold_parent_exclusions(
            seed.GOLD_PARENT_EXCLUSIONS_PATH
        ).items() if key not in sources
    }
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda path: exclusions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {
        case[0] for case in CASES
    }
    rows = seed.read_tsv(seed.RAW_DIR / "gold_ecosystem_paths.tsv")
    by_path = {row["canonical_path"]: row for row in rows}
    for identifier, source, parent, path, nodes, retained, grounding in CASES:
        old, new = before[identifier], after[identifier]
        assert set(old["parent_habitats"]) == {parent, *retained}
        assert new.get("parent_habitats", []) == retained
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-07T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert source in event["changes"]
        assert parent in event["changes"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        assert new["habitat_category"] == "ENGINEERED"
        assert new["grounding_status"] == grounding
        assert new["mapping_status"] == "SEEDED"
        assert len(new["source_attestations"]) == 1
        attestation = new["source_attestations"][0]
        assert attestation["source"] == "GOLD"
        assert attestation["source_path"] == path
        assert attestation["source_id"] in nodes
        assert "assertion_count" not in attestation
        assert "assertion_unit" not in attestation
        assert attestation.get("mapping_predicate") == (
            "skos:exactMatch" if grounding == "EXACT" else None
        )
        assert ("3 GOLD ecosystem node ids" in attestation.get("notes", "")) == (
            len(nodes) == 3
        )
        assert seed.mint("GOLD", path) == source
        assert set(by_path[path]["gold_node_ids"].split("|")) == nodes
        assert after[parent] == before[parent]
    assert after["habitatmech:BACDIVE.ff945d8a69"] == before[
        "habitatmech:BACDIVE.ff945d8a69"
    ]
