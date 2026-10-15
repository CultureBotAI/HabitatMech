"""Keep source context and host names distinct from habitat ancestry/identity."""

from dataclasses import replace

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.acd58e051d": "habitatmech:GOLD.9bb307824f",
    "habitatmech:GOLD.752ac1c5aa": "habitatmech:GOLD.11bece2c6f",
    "habitatmech:GOLD.6bdd76cda3": "habitatmech:GOLD.ca321f1251",
    "habitatmech:GOLD.a220aa6bb0": "habitatmech:GOLD.feecbcaf98",
    "habitatmech:GOLD.e1c2f5f7d4": "habitatmech:GOLD.0f64d697b2",
    "habitatmech:GOLD.2e584195fd": "habitatmech:GOLD.bbbdbf55b3",
    "habitatmech:GOLD.0e7950bba4": "habitatmech:GOLD.89cf14e129",
    "habitatmech:GOLD.f21263a95e": "habitatmech:GOLD.9bb307824f",
    "habitatmech:GOLD.1064d1667e": "habitatmech:GOLD.9bb307824f",
    "habitatmech:GOLD.cd608e3ced": "habitatmech:GOLD.9bb307824f",
    "habitatmech:GOLD.7862616c64": "habitatmech:GOLD.89cf14e129",
    "habitatmech:GOLD.4885b989e7": "habitatmech:GOLD.fac4f63f3b",
    "habitatmech:GOLD.67ad6b3f36": "habitatmech:GOLD.e36ba981d1",
    "habitatmech:GOLD.f7cc0ef1b4": "habitatmech:GOLD.0c74807e42",
    "habitatmech:GOLD.62f0ba9899": "habitatmech:GOLD.67ad6b3f36",
    "habitatmech:GOLD.1cfb2fdc59": "habitatmech:GOLD.5bbc13545b",
}
RESOLVED = {
    "habitatmech:GOLD.62f0ba9899": "BTO:0002922",
    "habitatmech:GOLD.1cfb2fdc59": "BTO:0002375",
}
HOST = "habitatmech:BACDIVE.a4a67c4a7f"
ALIAS = "Bovinae-Cow,-Cattle"


def test_exact_review_exclusions_and_public_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    aliases = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    assert PARENTS.keys() <= parents.keys()
    assert HOST in aliases
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for key, parent in PARENTS.items():
        row = parents[key]
        assert row.parent_id == parent
        assert seed.mint("GOLD", row.source_path) == key
    for row in [*[parents[key] for key in PARENTS], aliases[HOST]]:
        urls = [word for word in row.notes.split()
                if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")]
        assert len(urls) == 1
        assert urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_review_repairs_preserve_the_full_corpus(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    aliases = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    assert PARENTS.keys() <= parents.keys()
    assert HOST in aliases
    assert ALIAS not in definitions[HOST].exact_synonyms
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in parents.items() if key not in PARENTS
        })
        old.setattr(seed, "load_definition_source_label_exclusions", lambda _: {
            key: row for key, row in aliases.items() if key != HOST
        })
        old.setattr(seed, "load_curated_definitions", lambda _: {
            key: replace(row, exact_synonyms=(ALIAS, *row.exact_synonyms))
            if key == HOST else row for key, row in definitions.items()
        })
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    affected = {RESOLVED.get(key, key) for key in PARENTS}
    expected = affected | {HOST}
    assert len(expected) == 17
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key in expected:
        allowed = {"curation_history", "synonyms" if key == HOST else "parent_habitats"}
        assert {k: v for k, v in before[key].items() if k not in allowed} == {
            k: v for k, v in after[key].items() if k not in allowed
        }
        prior = before[key]["curation_history"]
        assert after[key]["curation_history"][:len(prior)] == prior
        added = after[key]["curation_history"][len(prior):]
        assert len(added) == 1
        assert added[0]["action"] == (
            "SOURCE_SYNONYM_EXCLUDED" if key == HOST else "SOURCE_PARENT_EXCLUDED"
        )
    for source, parent in PARENTS.items():
        key = RESOLVED.get(source, source)
        assert parent in before[key]["parent_habitats"]
        assert after[key].get("parent_habitats", []) == [
            p for p in before[key]["parent_habitats"] if p != parent
        ]
    assert after[HOST].get("synonyms", []) == [
        s for s in before[HOST]["synonyms"] if s["synonym_text"] != ALIAS
    ]
    assert after[HOST]["source_attestations"][0]["source_label"] == ALIAS
    for key in ("habitatmech:GOLD.752ac1c5aa", "habitatmech:GOLD.4885b989e7"):
        assert after[key]["source_attestations"][0]["mapping_predicate"] == "skos:narrowMatch"
    assert after["habitatmech:GOLD.752ac1c5aa"]["parent_habitats"] == ["UBERON:0000955"]
    assert after["habitatmech:GOLD.4885b989e7"]["parent_habitats"] == ["UBERON:0002185"]
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
