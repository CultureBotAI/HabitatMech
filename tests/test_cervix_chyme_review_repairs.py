"""Preserve source evidence while removing reviewed context-only parents."""

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.c15e1115f3": "habitatmech:GOLD.f736cbfbc5",
    "habitatmech:GOLD.c7a7c79455": "habitatmech:GOLD.4a65869529",
    "habitatmech:GOLD.1c429bbeae": "habitatmech:GOLD.333c18201f",
    "habitatmech:GOLD.0989ccfb99": "habitatmech:GOLD.d3869ad37f",
    "habitatmech:GOLD.ffd1fda259": "habitatmech:GOLD.6d0c170e7a",
    "habitatmech:GOLD.5a9d059298": "habitatmech:GOLD.bd1664969c",
}
RESOLVED = {"habitatmech:GOLD.1c429bbeae": "BTO:0003446"}


def test_exact_parent_guards_and_public_issue_links():
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert PARENTS.keys() <= exclusions.keys()
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for source, parent in PARENTS.items():
        row = exclusions[source]
        assert seed.mint("GOLD", row.source_path) == source
        assert row.parent_id == parent
        urls = [word for word in row.notes.split()
                if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_six_parent_repairs_preserve_other_fields_and_records(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert PARENTS.keys() <= exclusions.keys()
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as prior:
        prior.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in exclusions.items() if key not in PARENTS
        })
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    expected = {RESOLVED.get(key, key) for key in PARENTS}
    assert len(expected) == 6
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for source, parent in PARENTS.items():
        key = RESOLVED.get(source, source)
        old, new = before[key], after[key]
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in allowed} == {
            k: v for k, v in new.items() if k not in allowed
        }
        assert parent in old["parent_habitats"]
        assert new.get("parent_habitats", []) == [
            p for p in old["parent_habitats"] if p != parent
        ]
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-16T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert source in event["changes"] and parent in event["changes"]
    for key in ("habitatmech:GOLD.c15e1115f3", "habitatmech:GOLD.c7a7c79455"):
        assert after[key]["parent_habitats"] == ["UBERON:0000002"]
    for key in ("habitatmech:GOLD.0989ccfb99", "habitatmech:GOLD.ffd1fda259"):
        assert after[key]["parent_habitats"] == ["UBERON:0000910"]
    assert after["BTO:0003446"]["grounding_status"] == "CLOSE"
    assert after["BTO:0003446"]["mapping_status"] == "REVIEWED"
    assert not after["BTO:0003446"].get("parent_habitats")
    assert not after["habitatmech:GOLD.5a9d059298"].get("parent_habitats")
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
