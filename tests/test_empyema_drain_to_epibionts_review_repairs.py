"""Constrain nine empyema_drain..epibionts cohort parent, grounding, and exact-synonym repairs."""

import dataclasses

from jinja2 import Environment

from habitatmech import seed

PARENTS = {
    "habitatmech:GOLD.2f5a0b5455": ("habitatmech:GOLD.2f5a0b5455", "habitatmech:GOLD.016d1f9e29"),
    "habitatmech:GOLD.c26b92ece6": ("habitatmech:GOLD.c26b92ece6", "habitatmech:GOLD.d63e165267"),
    "habitatmech:GOLD.1488865daa": ("habitatmech:GOLD.1488865daa", "BTO:0006350"),
    "habitatmech:GOLD.e5017de50f": ("UBERON:0001295", "habitatmech:GOLD.f736cbfbc5"),
    "habitatmech:GOLD.89d01f437a": ("habitatmech:GOLD.89d01f437a", "habitatmech:GOLD.e898437067"),
    "habitatmech:GOLD.9731c6bb13": ("habitatmech:GOLD.9731c6bb13", "ENVO:01001181"),
}
SOURCE_PATHS = {
    "habitatmech:GOLD.2f5a0b5455": (
        "Host-associated > Mammals > Endocrine system > Endocrine gland"
    ),
    "habitatmech:GOLD.c26b92ece6": (
        "Host-associated > Mammals: Human > Endocrine system > Endocrine gland"
    ),
    "habitatmech:GOLD.1488865daa": (
        "Host-associated > Mammals: Human > Benign tumor > Polyps > Endometrial/Uterine"
    ),
    "habitatmech:GOLD.e5017de50f": (
        "Host-associated > Mammals: Human > Reproductive system > Uterus > Endometrium"
    ),
    "habitatmech:GOLD.89d01f437a": (
        "Host-associated > Plants > Phyllosphere > Carposphere > Endophytes"
    ),
    "habitatmech:GOLD.9731c6bb13": (
        "Host-associated > Plants > Roots > Rhizoplane > Endophytes"
    ),
}
RETAINED_PARENTS = {
    "habitatmech:GOLD.2f5a0b5455": ["UBERON:0002368"],
    "habitatmech:GOLD.c26b92ece6": ["UBERON:0002368"],
    "habitatmech:GOLD.1488865daa": ["NCIT:C3824"],
    "UBERON:0001295": ["UBERON:0019042"],
    "habitatmech:GOLD.89d01f437a": ["ENVO:01001057"],
    "habitatmech:GOLD.9731c6bb13": ["ENVO:01001057"],
}
LABEL_EXCLUSIONS = {
    "habitatmech:GOLD.1ce5b3ff1a": ("Empyema drain", "pleural empyema drainage fluid"),
    "habitatmech:GOLD.bfe3e11951": ("Endosphere", "plant endosphere"),
}
EXPECTED_SYNONYMS = {
    "habitatmech:GOLD.1ce5b3ff1a": ["empyema chest drain fluid"],
    "habitatmech:GOLD.b8e99e08e5": ["foliar endophyte environment"],
    "habitatmech:GOLD.9731c6bb13": ["radicular endophyte environment"],
    "habitatmech:GOLD.bfe3e11951": ["internal plant tissue environment"],
}


def test_reviewed_guards_and_public_evidence_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    assert PARENTS.keys() == SOURCE_PATHS.keys()
    assert PARENTS.keys() <= parents.keys()
    assert LABEL_EXCLUSIONS.keys() <= label_exclusions.keys()
    rows = []
    for key, (_, parent) in PARENTS.items():
        row = parents[key]
        assert row.source_path == SOURCE_PATHS[key]
        assert seed.mint("GOLD", row.source_path) == key
        assert row.parent_id == parent
        rows.append(row)
    for key, (source_label, requested_label) in LABEL_EXCLUSIONS.items():
        excl = label_exclusions[key]
        assert excl.source_label == source_label
        assert excl.requested_label == requested_label
        rows.append(excl)
    for key, expected_syns in EXPECTED_SYNONYMS.items():
        assert list(definitions[key].exact_synonyms) == expected_syns
    assert definitions["habitatmech:GOLD.1488865daa"].parent_class == "NCIT:C3824"
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for row in rows:
        urls = [
            word
            for word in row.notes.split()
            if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")
        ]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_nine_record_delta_preserves_unrelated_claims(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    reverted_definitions = dict(definitions)
    reverted_definitions["habitatmech:GOLD.bfe3e11951"] = dataclasses.replace(
        definitions["habitatmech:GOLD.bfe3e11951"],
        exact_synonyms=("endosphere",),
        date="2026-10-17",
        notes=(
            "ITEM curation: GOLD 'Host-associated > Plants > Endosphere' denotes the internal "
            "tissue environment of plants inhabited by endophytes. Define under ENVO:01001001 "
            "(plant-associated environment) with parent_mode ADD (PMID 25972004; "
            "DOI:10.1128/MMBR.00050-14). Path: Host-associated > Plants > Endosphere"
        ),
    )
    reverted_definitions["habitatmech:GOLD.9731c6bb13"] = dataclasses.replace(
        definitions["habitatmech:GOLD.9731c6bb13"],
        exact_synonyms=("root endosphere",),
        date="2026-10-17",
        notes=(
            "ITEM curation: GOLD 'Host-associated > Plants > Roots > Rhizoplane > Endophytes' "
            "denotes the internal root habitat colonized by endophytes rather than the organisms "
            "themselves. Define under ENVO:01001057 and exclude bare 'Endophytes' (PMID 26213366; "
            "DOI:10.1016/j.tim.2015.07.004; PMID 22850869; DOI:10.1038/nature11336). Path: "
            "Host-associated > Plants > Roots > Rhizoplane > Endophytes"
        ),
        parent_mode="ADD",
    )
    reverted_definitions["habitatmech:GOLD.89d01f437a"] = dataclasses.replace(
        definitions["habitatmech:GOLD.89d01f437a"],
        date="2026-10-17",
        notes=(
            "ITEM curation: GOLD 'Host-associated > Plants > Phyllosphere > Carposphere > "
            "Endophytes' denotes the internal fruit tissue habitat of endophytes. Define under "
            "ENVO:01001057 and exclude bare 'Endophytes' (PMID 32346039; "
            "DOI:10.1186/s40168-020-00830-z). Path: Host-associated > Plants > Phyllosphere > "
            "Carposphere > Endophytes"
        ),
        parent_mode="ADD",
    )
    reverted_definitions["habitatmech:GOLD.1ce5b3ff1a"] = dataclasses.replace(
        definitions["habitatmech:GOLD.1ce5b3ff1a"],
        exact_synonyms=("Empyema drain", "empyema chest drain fluid"),
        date="2026-10-17",
        notes=(
            "ITEM curation: GOLD 'Host-associated > Mammals: Human > Respiratory system > "
            "Pleural space/cavity > Empyema drain' denotes purulent fluid drained from a pleural "
            "empyema rather than the pleural cavity organ (UBERON:0002402). Define under "
            "UBERON:0006314 (bodily fluid) with parent_mode REPLACE (PMID 31558513; "
            "DOI:10.1128/JCM.00856-19). Path: Host-associated > Mammals: Human > Respiratory "
            "system > Pleural space/cavity > Empyema drain"
        ),
    )
    reverted_definitions["habitatmech:GOLD.b8e99e08e5"] = dataclasses.replace(
        definitions["habitatmech:GOLD.b8e99e08e5"],
        exact_synonyms=("leaf endosphere", "foliar endophyte environment"),
        date="2026-10-17",
        notes=(
            "ITEM curation: GOLD 'Host-associated > Plants > Phyllosphere > Phylloplane/Leaf > "
            "Endophytes' denotes the internal leaf habitat of foliar endophytes rather than the "
            "leaf organ (PO:0025034). Define under ENVO:01001057 with parent_mode REPLACE and "
            "exclude bare 'Endophytes' (PMID 23154261; DOI:10.1038/nrmicro2910). Path: "
            "Host-associated > Plants > Phyllosphere > Phylloplane/Leaf > Endophytes"
        ),
    )
    reverted_definitions["habitatmech:GOLD.1488865daa"] = dataclasses.replace(
        definitions["habitatmech:GOLD.1488865daa"],
        parent_class="BTO:0006350",
        parent_label="polyp",
        definition=(
            "A polyp arising as a benign localized overgrowth of endometrial glands and stroma "
            "projecting into the human uterine cavity, colonized by uterine mucosal microbiota."
        ),
        date="2026-10-17",
        notes=(
            "Defined human endometrial polyp under BTO:0006350 'polyp'; supported by endometrial "
            "polyp reproductive tract microbiome studies (PMID 27512056)."
        ),
        parent_mode="ADD",
    )

    reverted_decisions = dict(decisions)
    reverted_decisions["habitatmech:GOLD.1488865daa"] = dataclasses.replace(
        decisions["habitatmech:GOLD.1488865daa"],
        date="2026-10-17",
        notes=(
            "Defined human endometrial polyp under BTO:0006350 'polyp'; supported by endometrial "
            "polyp reproductive tract microbiome studies (PMID 27512056)."
        ),
    )

    with monkeypatch.context() as old_ctx:
        old_ctx.setattr(
            seed,
            "load_gold_parent_exclusions",
            lambda _: {key: row for key, row in parents.items() if key not in PARENTS},
        )
        old_ctx.setattr(
            seed,
            "load_definition_source_label_exclusions",
            lambda _: {
                key: row for key, row in label_exclusions.items() if key not in LABEL_EXCLUSIONS
            },
        )
        old_ctx.setattr(
            seed,
            "load_curated_definitions",
            lambda _: reverted_definitions,
        )
        old_ctx.setattr(
            seed,
            "load_decisions",
            lambda _: reverted_decisions,
        )
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    expected = set(RETAINED_PARENTS.keys()) | set(EXPECTED_SYNONYMS.keys())
    assert len(expected) == 9
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key, expected_parents in RETAINED_PARENTS.items():
        assert after[key].get("parent_habitats", []) == expected_parents
    for key, expected_syns in EXPECTED_SYNONYMS.items():
        assert sorted(s["synonym_text"] for s in after[key].get("synonyms", [])) == sorted(
            expected_syns
        )
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
