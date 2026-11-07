"""Constrain twenty-two excretory_system__22ee753c..fecal cohort parent, grounding, and synonym repairs."""

import dataclasses

from jinja2 import Environment

from habitatmech import seed
from habitatmech.curate.decisions import Decision

PARENTS = {
    "habitatmech:GOLD.d0a97e09fe": ("habitatmech:GOLD.d0a97e09fe", "habitatmech:GOLD.2959225799"),
    "habitatmech:GOLD.a37f187bfe": ("habitatmech:GOLD.a37f187bfe", "habitatmech:GOLD.6e10201167"),
    "habitatmech:GOLD.2ab65bac9e": ("UBERON:0004176", "habitatmech:GOLD.29feb6867b"),
    "habitatmech:GOLD.97989ecf5e": ("UBERON:0004176", "habitatmech:GOLD.abc827a582"),
    "habitatmech:GOLD.d5d5f596be": ("UBERON:0034929", "habitatmech:GOLD.68a62625da"),
    "habitatmech:GOLD.4b46114446": ("habitatmech:GOLD.4b46114446", "habitatmech:GOLD.4166733314"),
    "habitatmech:GOLD.7f217d034e": ("habitatmech:GOLD.7f217d034e", "habitatmech:GOLD.5a41405bc3"),
    "habitatmech:GOLD.b7f1694b87": ("habitatmech:GOLD.b7f1694b87", "habitatmech:GOLD.020f82703b"),
    "habitatmech:GOLD.4d81fdaa51": ("habitatmech:GOLD.4d81fdaa51", "habitatmech:GOLD.020f82703b"),
    "habitatmech:GOLD.aceda5f881": ("habitatmech:GOLD.aceda5f881", "habitatmech:GOLD.4166733314"),
    "habitatmech:GOLD.5d27b319ee": ("habitatmech:GOLD.5d27b319ee", "habitatmech:GOLD.4166733314"),
    "habitatmech:GOLD.b84283af7d": ("habitatmech:GOLD.b84283af7d", "habitatmech:GOLD.020f82703b"),
    "habitatmech:GOLD.a179efbe4f": ("habitatmech:GOLD.a179efbe4f", "habitatmech:GOLD.abc827a582"),
    "habitatmech:GOLD.fe591e2cb7": ("habitatmech:GOLD.fe591e2cb7", "habitatmech:GOLD.29feb6867b"),
    "habitatmech:GOLD.b64b241c4b": ("habitatmech:GOLD.b64b241c4b", "habitatmech:GOLD.06a3636aa2"),
    "habitatmech:GOLD.f74ba58314": ("habitatmech:GOLD.f74ba58314", "habitatmech:GOLD.da02e4c756"),
    "habitatmech:GOLD.e63b1e075e": ("BTO:0000442", "habitatmech:GOLD.dba2a83b95"),
    "habitatmech:GOLD.746249e4ce": ("BTO:0000447", "habitatmech:GOLD.52d3212a6a"),
}
SOURCE_PATHS = {
    "habitatmech:GOLD.d0a97e09fe": "Host-associated > Arthropoda: Crustaceans > Excretory system",
    "habitatmech:GOLD.a37f187bfe": "Host-associated > Annelida > Excretory system",
    "habitatmech:GOLD.2ab65bac9e": (
        "Host-associated > Mammals > Reproductive system > External genitalia"
    ),
    "habitatmech:GOLD.97989ecf5e": (
        "Host-associated > Mammals: Human > Reproductive system > External genitalia/Vulva"
    ),
    "habitatmech:GOLD.d5d5f596be": "Host-associated > Mammals > Multiple systems > Soft tissue",
    "habitatmech:GOLD.4b46114446": "Host-associated > Mammals > Visual system > Eye",
    "habitatmech:GOLD.7f217d034e": "Host-associated > Fish > Visual system > Eye",
    "habitatmech:GOLD.b7f1694b87": "Host-associated > Mammals: Human > Visual system > Eye",
    "habitatmech:GOLD.4d81fdaa51": (
        "Host-associated > Mammals: Human > Visual system > Eye: Ciliary body"
    ),
    "habitatmech:GOLD.aceda5f881": "Host-associated > Mammals > Visual system > Eye: Ciliary body",
    "habitatmech:GOLD.5d27b319ee": (
        "Host-associated > Mammals > Visual system > Eye: Vitreous chamber"
    ),
    "habitatmech:GOLD.b84283af7d": (
        "Host-associated > Mammals: Human > Visual system > Eye: Vitreous chamber"
    ),
    "habitatmech:GOLD.a179efbe4f": (
        "Host-associated > Mammals: Human > Reproductive system > Fallopian tubes"
    ),
    "habitatmech:GOLD.fe591e2cb7": (
        "Host-associated > Mammals > Reproductive system > Fallopian tubes"
    ),
    "habitatmech:GOLD.b64b241c4b": "Host-associated > Mammals > Connective tissue > Fascia",
    "habitatmech:GOLD.f74ba58314": "Host-associated > Mammals: Human > Connective tissue > Fascia",
    "habitatmech:GOLD.e63b1e075e": "Host-associated > Arthropoda: Insects > Fat body",
    "habitatmech:GOLD.746249e4ce": "Host-associated > Birds > Integumentary system > Skin > Feathers",
}
RETAINED_PARENTS = {
    "habitatmech:GOLD.d0a97e09fe": ["UBERON:8450002"],
    "habitatmech:GOLD.a37f187bfe": ["UBERON:8450002"],
    "UBERON:0004176": ["UBERON:0003133"],
    "habitatmech:GOLD.5c89d5e294": ["UBERON:0004176"],
    "habitatmech:GOLD.9bfd135cfa": ["UBERON:0004176"],
    "UBERON:0034929": ["UBERON:0010000", "UBERON:0010314"],
    "habitatmech:GOLD.0a69f87c03": ["ENVO:01001055"],
    "habitatmech:GOLD.28f9330745": ["ENVO:01001055"],
    "habitatmech:GOLD.4b46114446": ["UBERON:0000970"],
    "habitatmech:GOLD.7f217d034e": ["UBERON:0000970"],
    "habitatmech:GOLD.b7f1694b87": ["UBERON:0000970"],
    "habitatmech:GOLD.4d81fdaa51": ["BTO:0000260"],
    "habitatmech:GOLD.aceda5f881": ["BTO:0000260"],
    "habitatmech:GOLD.5d27b319ee": ["BTO:0002087"],
    "habitatmech:GOLD.b84283af7d": ["BTO:0002087"],
    "habitatmech:GOLD.a179efbe4f": ["UBERON:0003889"],
    "habitatmech:GOLD.fe591e2cb7": ["UBERON:0003889"],
    "habitatmech:GOLD.b64b241c4b": ["UBERON:0008982"],
    "habitatmech:GOLD.f74ba58314": ["UBERON:0008982"],
    "BTO:0000442": ["BTO:0001487"],
    "BTO:0000447": [],
}
LABEL_EXCLUSIONS = {
    "habitatmech:GOLD.6c8238add0": ("Extracellular", "molluscan gill extracellular environment"),
}


def test_reviewed_guards_and_public_evidence_links():
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
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
    assert definitions["habitatmech:GOLD.5c89d5e294"].parent_class == "UBERON:0004176"
    assert definitions["habitatmech:GOLD.5c89d5e294"].parent_mode == "REPLACE"
    assert definitions["habitatmech:GOLD.9bfd135cfa"].parent_class == "UBERON:0004176"
    assert definitions["habitatmech:GOLD.9bfd135cfa"].parent_mode == "REPLACE"
    assert definitions["habitatmech:GOLD.0a69f87c03"].parent_class == "ENVO:01001055"
    assert definitions["habitatmech:GOLD.0a69f87c03"].parent_mode == "REPLACE"
    assert definitions["habitatmech:GOLD.28f9330745"].parent_class == "ENVO:01001055"
    assert definitions["habitatmech:GOLD.28f9330745"].parent_mode == "REPLACE"
    assert decisions["habitatmech:GOLD.97989ecf5e"].grounding_status == "CLOSE"
    assert decisions["habitatmech:GOLD.2ab65bac9e"].decision == "REVIEW"
    assert decisions["habitatmech:GOLD.4d81fdaa51"].object_id == "BTO:0000260"
    assert decisions["habitatmech:GOLD.aceda5f881"].object_id == "BTO:0000260"
    assert decisions["habitatmech:GOLD.5d27b319ee"].object_id == "BTO:0002087"
    assert decisions["habitatmech:GOLD.b84283af7d"].object_id == "BTO:0002087"
    template = Environment(autoescape=True).from_string("{{ notes|urlize }}")
    for row in rows:
        urls = [
            word
            for word in row.notes.split()
            if word.startswith("https://github.com/CultureBotAI/HabitatMech/issues/")
        ]
        assert len(urls) == 1 and urls[0].rsplit("/", 1)[1].isdigit()
        assert f'href="{urls[0]}"' in template.render(notes=row.notes)


def test_twenty_two_record_delta_preserves_unrelated_claims(monkeypatch):
    parents = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    label_exclusions = seed.load_definition_source_label_exclusions(
        seed.DEFINITION_SOURCE_LABEL_EXCLUSIONS_PATH
    )
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    reverted_definitions = dict(definitions)
    reverted_definitions["habitatmech:GOLD.5c89d5e294"] = dataclasses.replace(
        definitions["habitatmech:GOLD.5c89d5e294"],
        parent_class="UBERON:0000990",
        parent_label="reproductive system",
        definition=(
            "A reproductive system anatomical surface comprising the external genitalia of a "
            "human host (such as the vulva, labia, penile shaft, glans, or coronal sulcus), "
            "colonized by cutaneous and urogenital microbiota."
        ),
        notes=(
            "Defined human external reproductive organ environment under UBERON:0000990 "
            "'reproductive system'; supported by human urogenital and external genitalia "
            "microbiome studies (PMID 22699609)."
        ),
        parent_mode="ADD",
    )
    reverted_definitions["habitatmech:GOLD.9bfd135cfa"] = dataclasses.replace(
        definitions["habitatmech:GOLD.9bfd135cfa"],
        parent_class="UBERON:0000990",
        parent_label="reproductive system",
        definition=(
            "A reproductive system anatomical surface comprising the external genitalia of a "
            "non-human or general mammalian host (including vulvar, preputial, and penile "
            "surfaces), colonized by urogenital and cutaneous microbiota."
        ),
        notes=(
            "Defined mammalian external reproductive organ environment under UBERON:0000990 "
            "'reproductive system'; supported by mammalian reproductive tract microbiome "
            "studies (PMID 28529509)."
        ),
        parent_mode="ADD",
    )
    reverted_definitions["habitatmech:GOLD.0a69f87c03"] = dataclasses.replace(
        definitions["habitatmech:GOLD.0a69f87c03"],
        parent_class="UBERON:3010636",
        parent_label="egg capsule",
        definition=(
            "An egg capsule compartment consisting of the extracellular nutritive albuminous "
            "fluid inside an annelid cocoon (such as an earthworm or leech egg capsule), "
            "where vertically transmitted bacterial symbionts proliferate before colonizing "
            "developing embryos."
        ),
        notes=(
            "ITEM curation: GOLD 'Host-associated > Annelida > Reproductive system > Egg "
            "capsule > Extracellular' denotes the extracellular fluid compartment inside an "
            "annelid egg capsule/cocoon (PMID 18480259; DOI:10.1128/AEM.00126-08). Path: "
            "Host-associated > Annelida > Reproductive system > Egg capsule > Extracellular"
        ),
        parent_mode="ADD",
    )
    reverted_definitions["habitatmech:GOLD.28f9330745"] = dataclasses.replace(
        definitions["habitatmech:GOLD.28f9330745"],
        parent_class="UBERON:0001555",
        parent_label="digestive tract",
        definition=(
            "A digestive tract lumen or mucosal surface of an annelid worm inhabited by "
            "extracellular symbiotic microorganisms."
        ),
        notes=(
            "ITEM curation: GOLD 'Host-associated > Annelida > Digestive system > Digestive "
            "tube > Extracellular symbionts' denotes the digestive tract environment of an "
            "annelid hosting extracellular symbionts (PMID 26243915; DOI:10.1038/ismej.2015.134). "
            "Path: Host-associated > Annelida > Digestive system > Digestive tube > Extracellular "
            "symbionts"
        ),
        parent_mode="ADD",
    )

    reverted_decisions = {
        k: v for k, v in decisions.items() if k != "habitatmech:GOLD.2ab65bac9e"
    }
    reverted_decisions["habitatmech:GOLD.5c89d5e294"] = dataclasses.replace(
        decisions["habitatmech:GOLD.5c89d5e294"],
        notes=(
            "Defined human external reproductive organ environment under UBERON:0000990 "
            "'reproductive system'; supported by human urogenital and external genitalia "
            "microbiome studies (PMID 22699609)."
        ),
    )
    reverted_decisions["habitatmech:GOLD.9bfd135cfa"] = dataclasses.replace(
        decisions["habitatmech:GOLD.9bfd135cfa"],
        notes=(
            "Defined mammalian external reproductive organ environment under UBERON:0000990 "
            "'reproductive system'; supported by mammalian reproductive tract microbiome "
            "studies (PMID 28529509)."
        ),
    )
    reverted_decisions["habitatmech:GOLD.97989ecf5e"] = Decision(
        identifier="habitatmech:GOLD.97989ecf5e",
        decision="GROUND",
        object_id="UBERON:0004176",
        object_label="external genitalia",
        grounding_status="EXACT",
        curator="claude-opus-5",
        date="2026-08-12",
        notes=(
            "Slash alternative; vulva is the female instance. Path: Host-associated > "
            "Mammals: Human > Reproductive system > External geni"
        ),
        review_depth="ITEM",
    )
    reverted_decisions["habitatmech:GOLD.4d81fdaa51"] = Decision(
        identifier="habitatmech:GOLD.4d81fdaa51",
        decision="GROUND_AS_PARENT",
        object_id="UBERON:0000970",
        object_label="eye",
        grounding_status="NARROW",
        curator="claude-opus-5",
        date="2026-08-12",
        notes=(
            "The ciliary body is a structure within the eye. Path: Host-associated > "
            "Mammals: Human > Visual system > Eye: Ciliary body"
        ),
        review_depth="ITEM",
    )
    reverted_decisions["habitatmech:GOLD.aceda5f881"] = Decision(
        identifier="habitatmech:GOLD.aceda5f881",
        decision="GROUND_AS_PARENT",
        object_id="UBERON:0000970",
        object_label="eye",
        grounding_status="NARROW",
        curator="claude-opus-5",
        date="2026-08-12",
        notes=(
            "The ciliary body is a structure within the eye. Path: Host-associated > "
            "Mammals > Visual system > Eye: Ciliary body"
        ),
        review_depth="ITEM",
    )
    reverted_decisions["habitatmech:GOLD.5d27b319ee"] = Decision(
        identifier="habitatmech:GOLD.5d27b319ee",
        decision="GROUND_AS_PARENT",
        object_id="UBERON:0000970",
        object_label="eye",
        grounding_status="NARROW",
        curator="claude-opus-5",
        date="2026-08-12",
        notes=(
            "The vitreous chamber is a compartment within the eye. Path: Host-associated > "
            "Mammals > Visual system > Eye: Vitreous chamber"
        ),
        review_depth="ITEM",
    )
    reverted_decisions["habitatmech:GOLD.b84283af7d"] = Decision(
        identifier="habitatmech:GOLD.b84283af7d",
        decision="GROUND_AS_PARENT",
        object_id="UBERON:0000970",
        object_label="eye",
        grounding_status="NARROW",
        curator="claude-opus-5",
        date="2026-08-12",
        notes=(
            "The vitreous chamber is a compartment within the eye. Path: Host-associated > "
            "Mammals: Human > Visual system > Eye: Vitreous chamb"
        ),
        review_depth="ITEM",
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

    expected = set(RETAINED_PARENTS.keys()) | {"habitatmech:GOLD.6c8238add0"}
    assert len(expected) == 22
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key, expected_parents in RETAINED_PARENTS.items():
        assert after[key].get("parent_habitats", []) == expected_parents
    assert after["habitatmech:GOLD.6c8238add0"].get("synonyms", []) == []
    assert after["UBERON:0004176"].get("mapping_status") == "REVIEWED"
    assert after["UBERON:0004176"].get("grounding_status") == "EXACT"
    assert [
        s
        for s in after["UBERON:0004176"].get("synonyms", [])
        if s["synonym_text"] == "External genitalia/Vulva"
    ] == [
        {
            "synonym_text": "External genitalia/Vulva",
            "synonym_type": "RELATED_SYNONYM",
            "source": "GOLD",
        }
    ]
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
