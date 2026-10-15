"""Reviewed blood and bone classes must not inherit their anatomical containers."""

from collections import defaultdict

from jinja2 import Environment

from habitatmech import seed

# Each entry identifies a source concept, resolved record and excluded parent.
EXCLUSIONS = {
    "habitatmech:GOLD.f46a5017f9": ("habitatmech:GOLD.f46a5017f9", "habitatmech:GOLD.0552e4fd8a"),
    "habitatmech:GOLD.476e09babd": ("habitatmech:GOLD.476e09babd", "habitatmech:GOLD.5b9148ecc0"),
    "habitatmech:GOLD.d25ff4a586": ("habitatmech:GOLD.d25ff4a586", "habitatmech:GOLD.0635cc88f0"),
    "habitatmech:GOLD.6c6aab19d3": ("habitatmech:GOLD.6c6aab19d3", "habitatmech:GOLD.7a7f8b9aa3"),
    "habitatmech:GOLD.941ff9f450": ("UBERON:0001969", "habitatmech:GOLD.d25ff4a586"),
    "habitatmech:GOLD.b81daaf43c": ("UBERON:0001969", "habitatmech:GOLD.6c6aab19d3"),
    "habitatmech:GOLD.9bed5e7377": ("UBERON:0001977", "habitatmech:GOLD.d25ff4a586"),
    "habitatmech:GOLD.1a5b0996a6": ("UBERON:0001977", "habitatmech:GOLD.6c6aab19d3"),
    "habitatmech:GOLD.643da6e69e": ("UBERON:0001977", "habitatmech:GOLD.f46a5017f9"),
    "habitatmech:GOLD.774bc38294": ("habitatmech:GOLD.774bc38294", "habitatmech:GOLD.867abac275"),
    "habitatmech:GOLD.67f49f8b15": ("habitatmech:GOLD.67f49f8b15", "habitatmech:GOLD.ea67ca30cb"),
    "habitatmech:GOLD.28cfbd7dee": ("habitatmech:GOLD.28cfbd7dee", "habitatmech:GOLD.092eae5cd7"),
    "habitatmech:GOLD.d9b3a1e82d": ("habitatmech:GOLD.d9b3a1e82d", "habitatmech:GOLD.b1f5d69111"),
    "habitatmech:GOLD.6296c1e38f": ("UBERON:0001474", "habitatmech:GOLD.3756d4bb39"),
    "habitatmech:GOLD.cb1c796cde": ("habitatmech:GOLD.cb1c796cde", "habitatmech:GOLD.28cfbd7dee"),
    "habitatmech:GOLD.ef3ff31a67": ("habitatmech:GOLD.ef3ff31a67", "habitatmech:GOLD.67f49f8b15"),
}


def test_exact_blood_bone_exclusions_and_issue_links():
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert EXCLUSIONS.keys() <= exclusions.keys()
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for source, (_, parent) in EXCLUSIONS.items():
        row = exclusions[source]
        assert row.parent_id == parent
        assert seed.mint("GOLD", row.source_path) == source
        urls = [word.rstrip(".") for word in row.notes.split()
                if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")]
        assert len(urls) == 1
        assert urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_blood_bone_repairs_preserve_full_corpus_and_source_claims(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert EXCLUSIONS.keys() <= exclusions.keys()
    removed = defaultdict(set)
    for target, parent in EXCLUSIONS.values():
        removed[target].add(parent)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in exclusions.items() if key not in EXCLUSIONS
        })
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == set(removed)
    assert len(removed) == 13
    for target, parents in removed.items():
        assert parents <= set(before[target]["parent_habitats"])
        assert set(after[target]["parent_habitats"]) == set(before[target]["parent_habitats"]) - parents
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in before[target].items() if k not in allowed} == {
            k: v for k, v in after[target].items() if k not in allowed
        }
        old_history = before[target]["curation_history"]
        assert after[target]["curation_history"][:len(old_history)] == old_history
        new_events = after[target]["curation_history"][len(old_history):]
        assert len(new_events) == sum(t == target for t, _ in EXCLUSIONS.values())
        assert all(event["action"] == "SOURCE_PARENT_EXCLUDED" for event in new_events)

    assert after["UBERON:0001969"]["parent_habitats"] == ["UBERON:0000179"]
    assert after["UBERON:0001977"]["parent_habitats"] == ["UBERON:0000179"]
    assert after["UBERON:0001474"]["parent_habitats"] == ["FOODON:03420168", "UBERON:0004765"]
    assert after["UBERON:0001474"]["mapping_status"] == "REVIEWED"
    for source in ("habitatmech:GOLD.cb1c796cde", "habitatmech:GOLD.ef3ff31a67"):
        assert after[source]["parent_habitats"] == ["UBERON:0002371"]
        assert after[source]["source_attestations"][0]["mapping_predicate"] == "skos:narrowMatch"
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
