"""Food production context is not a material or tool superclass."""

from habitatmech import seed

REPAIRS = {
    "habitatmech:GOLD.62a92ea437": ("habitatmech:GOLD.62a92ea437", []),
    "FOODON:03400803": ("habitatmech:GOLD.b6cdf087cc", ["FOODON:03400801"]),
    "ENVO:01000681": ("habitatmech:GOLD.d51f0755f5", ["ENVO:01000508"]),
    "habitatmech:GOLD.3153798c1a": ("habitatmech:GOLD.3153798c1a", ["ENVO:03600040"]),
    "FOODON:03306052": ("habitatmech:GOLD.43e5763a38", ["FOODON:03303380"]),
    "FOODON:03316428": (
        "habitatmech:GOLD.0d60521505", ["FOODON:00001149", "FOODON:03303220"],
    ),
    "ENVO:03501327": ("habitatmech:GOLD.35cefb585d", ["ENVO:03501263"]),
}


def test_seven_food_exclusions_preserve_every_other_corpus_claim(monkeypatch):
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    sources = {source for source, _ in REPAIRS.values()}
    assert sources <= exclusions.keys()
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in sources
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == set(REPAIRS)
    for identifier, (source, retained) in REPAIRS.items():
        old, new = before[identifier], after[identifier]
        assert old["parent_habitats"] == sorted(["FOODON:03530206", *retained])
        assert new.get("parent_habitats", []) == retained
        assert exclusions[source].parent_id == "FOODON:03530206"
        assert seed.mint("GOLD", exclusions[source].source_path) == source
        gold = [a for a in new["source_attestations"] if a["source"] == "GOLD"]
        assert len(gold) == 1
        assert gold[0]["source_path"] == exclusions[source].source_path
        added = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(added) == 1
        event = added[0]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["curator"] == "codex-gpt-5"
        assert event["timestamp"] == "2026-10-14T00:00:00Z"
        assert source in event["changes"] and "FOODON:03530206" in event["changes"]
        assert [e for e in new["curation_history"] if e != event] == old["curation_history"]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }

    # Scope findings remain separate; these exclusions do not certify identities.
    seafood = after["FOODON:03400803"]
    assert len(seafood["source_attestations"]) == 2
    assert len(seafood["characteristic_taxa"]) == 25
    assert seafood["grounding_status"] == "CLOSE"
    assert after["ENVO:03501327"]["habitat_category"] == "FOOD"
    assert after["habitatmech:GOLD.9b7880ecd2"] == before["habitatmech:GOLD.9b7880ecd2"]
    assert after["habitatmech:GOLD.9b7880ecd2"]["parent_habitats"] == ["FOODON:03530206"]
    assert after["FOODON:03310002"] == before["FOODON:03310002"]
    assert after["FOODON:00001087"] == before["FOODON:00001087"]
    assert after["habitatmech:GOLD.da71b4e2c9"]["parent_habitats"] == ["ENVO:01000681"]
