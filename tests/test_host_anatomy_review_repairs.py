"""Constrain the reviewed host-name and anatomical-parent corrections."""

from dataclasses import replace

from habitatmech import seed

HOSTS = {
    "habitatmech:GOLD.0cd585a031": ("Amphibia", "NCBITaxon:8292", 41),
    "habitatmech:GOLD.6e10201167": ("Annelida", "NCBITaxon:6340", 150),
}
PARENTS = {
    "habitatmech:GOLD.9e917ffe11": "habitatmech:GOLD.2173317f9c",
    "habitatmech:GOLD.a2d2eb3d96": "habitatmech:GOLD.5b0aa7456c",
    "habitatmech:GOLD.a613af1611": "habitatmech:GOLD.6bda0871e2",
    "habitatmech:GOLD.1d3e238d30": "habitatmech:GOLD.6bda0871e2",
    "habitatmech:GOLD.e45d906034": "habitatmech:GOLD.5b0aa7456c",
    "habitatmech:GOLD.aaf13396b6": "habitatmech:GOLD.5b0aa7456c",
    "habitatmech:GOLD.cb3fda7227": "habitatmech:GOLD.d0a97e09fe",
    "habitatmech:GOLD.9d219f6fdc": "habitatmech:GOLD.50722c7871",
    "habitatmech:GOLD.53e4290463": "habitatmech:GOLD.19840c718e",
    "habitatmech:GOLD.c3e9d3ce0b": "habitatmech:GOLD.1daee83236",
}
CHAMBER = "habitatmech:GOLD.53e4290463"
FORNIX = "UBERON:0016487"
CORRECTION = "anterior-fornix-ontology-synonym-scope"
RESOLVED = {
    "habitatmech:GOLD.cb3fda7227": "UBERON:0009963",
    "habitatmech:GOLD.c3e9d3ce0b": FORNIX,
}


def test_host_anatomy_repairs_preserve_corpus_scope(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    definitions = seed.load_curated_definitions(seed.CURATED_DEFINITIONS_PATH)
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    corrections = seed.load_record_annotation_corrections(seed.RECORD_ANNOTATION_CORRECTIONS_PATH)
    assert PARENTS.keys() <= exclusions.keys()
    assert all(not definitions[key].exact_synonyms for key in HOSTS)
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    with monkeypatch.context() as old:
        old.setattr(seed, "load_gold_parent_exclusions", lambda _: {
            key: row for key, row in exclusions.items() if key not in PARENTS
        })
        old.setattr(seed, "load_curated_definitions", lambda _: {
            **definitions, **{key: replace(definitions[key], exact_synonyms=(value[0],))
                              for key, value in HOSTS.items()}
        })
        old.setattr(seed, "load_decisions", lambda _: {
            **decisions, CHAMBER: replace(decisions[CHAMBER], decision="GROUND_AS_PARENT",
                                         object_id="BTO:0000510", object_label="hindgut",
                                         grounding_status="NARROW")
        })
        old.setattr(seed, "load_record_annotation_corrections", lambda _: [
            row for row in corrections if row.correction_id != CORRECTION
        ])
        before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}

    expected = {RESOLVED.get(key, key) for key in PARENTS} | HOSTS.keys()
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == expected
    for key in expected:
        allowed = {"parent_habitats", "curation_history"}
        if key in HOSTS or key == FORNIX:
            allowed.add("synonyms")
        if key == CHAMBER:
            allowed |= {"grounding_status", "source_attestations"}
        assert {k: v for k, v in before[key].items() if k not in allowed} == {
            k: v for k, v in after[key].items() if k not in allowed
        }

    for source, parent in PARENTS.items():
        key = RESOLVED.get(source, source)
        assert parent in before[key]["parent_habitats"]
        assert parent not in after[key].get("parent_habitats", [])
        if key != CHAMBER:
            assert after[key].get("parent_habitats", []) == [
                p for p in before[key]["parent_habitats"] if p != parent
            ]
            assert before[key]["source_attestations"] == after[key]["source_attestations"]
            old_history = before[key]["curation_history"]
            assert after[key]["curation_history"][:len(old_history)] == old_history

    for key, (label, taxon, count) in HOSTS.items():
        assert not after[key].get("synonyms")
        assert after[key]["xrefs"] == [taxon]
        assert after[key]["parent_habitats"] == ["ENVO:01001000", "ENVO:01001002"]
        assert after[key]["curation_history"] == before[key]["curation_history"]
        attestation = after[key]["source_attestations"][0]
        assert attestation["source_label"] == label
        assert attestation["assertion_count"] == count
        assert attestation["assertion_unit"] == "ORGANISM"

    chamber = after[CHAMBER]
    assert chamber["grounding_status"] == "UNGROUNDED"
    assert chamber["mapping_status"] == "REVIEWED"
    assert not chamber.get("parent_habitats")
    assert not chamber.get("xrefs")
    old_attestation = dict(before[CHAMBER]["source_attestations"][0])
    assert old_attestation.pop("mapping_predicate") == "skos:narrowMatch"
    assert chamber["source_attestations"] == [old_attestation]
    assert old_attestation["source_id"] == "gold.ecosystem:7325"

    synonyms = {(s["source"], s["synonym_text"]): s["synonym_type"]
                for s in after[FORNIX]["synonyms"]}
    assert synonyms == {
        ("GOLD", "Anterior fornix"): "RELATED_SYNONYM",
        ("UBERON", "anterior fornix"): "BROAD_SYNONYM",
        ("UBERON", "anterior part of fornix of vagina"): "EXACT_SYNONYM",
        ("UBERON", "pars anterior fornicis vaginae"): "EXACT_SYNONYM",
    }
    assert after[FORNIX]["grounding_status"] == "CLOSE"
    assert after[FORNIX]["mapping_status"] == "REVIEWED"
    assert {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts} == after
