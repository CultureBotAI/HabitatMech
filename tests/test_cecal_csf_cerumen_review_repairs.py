"""Keep source context distinct from a strict broader habitat class."""

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.cb4d8fc60e": "habitatmech:GOLD.5b0aa7456c",
    "habitatmech:GOLD.66d6a3a57a": "habitatmech:GOLD.cd0b0940e5",
    "habitatmech:GOLD.6a1f882bb7": "habitatmech:GOLD.4b37ab4b76",
    "habitatmech:GOLD.60a0f24d46": "habitatmech:GOLD.bd9662fadb",
    "habitatmech:GOLD.21f701f425": "habitatmech:GOLD.ce83e63059",
    "habitatmech:GOLD.cf49d42b99": "habitatmech:GOLD.feecbcaf98",
    "habitatmech:GOLD.2777b651ed": "habitatmech:GOLD.54eda01cf1",
    "habitatmech:GOLD.fe4f95287e": "habitatmech:GOLD.066547cb98",
    "habitatmech:GOLD.98bf2e4e7d": "habitatmech:GOLD.56e0776270",
    "habitatmech:GOLD.aea4a5fe91": "UBERON:0013211",
    "habitatmech:GOLD.77cb05c27a": "habitatmech:GOLD.dc86c8917c",
    "habitatmech:GOLD.e30a9eb98c": "BTO:0006350",
}
RESOLVED = {
    "habitatmech:GOLD.66d6a3a57a": "ENVO:02000008",
    "habitatmech:GOLD.60a0f24d46": "BTO:0001906",
    "habitatmech:GOLD.cf49d42b99": "UBERON:0001359",
    "habitatmech:GOLD.aea4a5fe91": "UBERON:0002297",
    "habitatmech:GOLD.77cb05c27a": "UBERON:0013211",
}


def test_exact_review_parent_guards_and_public_links():
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert PARENTS.keys() <= exclusions.keys()
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for key, parent in PARENTS.items():
        row = exclusions[key]
        assert row.parent_id == parent
        assert seed.mint("GOLD", row.source_path) == key
        urls = [word for word in row.notes.split()
                if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")]
        assert len(urls) == 1
        assert urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_context_parent_repairs_preserve_the_complete_corpus(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert PARENTS.keys() <= exclusions.keys()
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in exclusions.items() if key not in PARENTS
        })
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    expected = {RESOLVED.get(key, key) for key in PARENTS}
    assert len(expected) == 12
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key in expected:
        allowed = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in before[key].items() if k not in allowed} == {
            k: v for k, v in after[key].items() if k not in allowed
        }
        prior = before[key]["curation_history"]
        assert after[key]["curation_history"][:len(prior)] == prior
        added = after[key]["curation_history"][len(prior):]
        assert len(added) == 1 and added[0]["action"] == "SOURCE_PARENT_EXCLUDED"
    for source, parent in PARENTS.items():
        key = RESOLVED.get(source, source)
        assert parent in before[key]["parent_habitats"]
        assert after[key].get("parent_habitats", []) == [
            p for p in before[key]["parent_habitats"] if p != parent
        ]

    valid_genera = {
        "habitatmech:GOLD.cb4d8fc60e": ["BTO:0000166"],
        "ENVO:02000008": ["ENVO:01000155"],
        "BTO:0001906": ["BTO:0000282", "BTO:0001368"],
        "UBERON:0001359": ["UBERON:0007779"],
        "UBERON:0002297": ["UBERON:0001089"],
        "UBERON:0013211": ["UBERON:0000382"],
    }
    for key, genera in valid_genera.items():
        assert after[key]["parent_habitats"] == genera
    for key in ("habitatmech:GOLD.21f701f425", "habitatmech:GOLD.2777b651ed",
                "habitatmech:GOLD.fe4f95287e"):
        assert after[key]["parent_habitats"] == ["UBERON:0001359"]
        assert after[key]["source_attestations"][0]["mapping_predicate"] == "skos:narrowMatch"
    assert after["habitatmech:GOLD.6a1f882bb7"]["grounding_status"] == "NOT_APPLICABLE"
    assert after["habitatmech:GOLD.98bf2e4e7d"]["xrefs"] == ["UBERON:0006967"]
    assert after["habitatmech:GOLD.e30a9eb98c"]["grounding_status"] == "UNGROUNDED"
    assert after["BTO:0006350"] == before["BTO:0006350"]
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
