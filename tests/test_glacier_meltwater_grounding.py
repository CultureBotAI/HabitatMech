"""The glacier-specific source remains distinct from generic meltwater."""

from dataclasses import replace

from habitatmech import seed

IDENTIFIER = "habitatmech:GOLD.f3dc60ff11"
PATH = "Environmental > Aquatic > Freshwater > Ice > Glacier meltwater"


def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_item_grounding_changes_only_glacier_meltwater(monkeypatch):
    after = documents()
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    old = replace(
        decisions[IDENTIFIER], decision="CONFIRM_UNGROUNDED", object_id="",
        object_label="", grounding_status="", review_depth="CLASS",
    )
    monkeypatch.setattr(seed, "load_decisions", lambda path: {**decisions, IDENTIFIER: old})
    before = documents()
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {IDENTIFIER}
    previous, current = before[IDENTIFIER], after[IDENTIFIER]
    assert previous["grounding_status"] == "UNGROUNDED"
    assert previous["mapping_status"] == "SEEDED"
    assert not previous.get("parent_habitats")
    assert current["parent_habitats"] == ["ENVO:01000722"]
    assert current["grounding_status"] == "NARROW"
    assert current["mapping_status"] == "REVIEWED"
    attestation = {
        "source": "GOLD", "source_id": "gold.ecosystem:7784",
        "source_label": "Glacier meltwater", "source_path": PATH,
    }
    assert previous["source_attestations"] == [attestation]
    assert current["source_attestations"] == [
        {**attestation, "mapping_predicate": "skos:narrowMatch"},
    ]
    mutable = {"parent_habitats", "grounding_status", "mapping_status",
               "source_attestations", "curation_history"}
    for field in previous.keys() | current.keys():
        if field not in mutable:
            assert previous.get(field) == current.get(field), field
    def exclusions(doc):
        return [e for e in doc["curation_history"] if e["action"] == "SOURCE_PARENT_EXCLUDED"]

    assert exclusions(previous) == exclusions(current)
    assert len(exclusions(current)) == 1
    assert after["ENVO:01000722"]["source_attestations"][0]["source_id"] == "gold.ecosystem:7297"


def test_meltwater_evidence_preserves_independent_source_units():
    rows = seed.read_tsv(seed.RAW_DIR / "gold_path_triads.tsv")
    medium = [r for r in rows if r["canonical_path"] == PATH and r["slot"] == "medium"]
    assert len(medium) == 1
    assert medium[0]["top_term"] == "ENVO:01000722"
    assert medium[0]["top_share"] == "1.00"
    assert medium[0]["samples"] == "6"
    assert medium[0]["studies"] == medium[0]["studies_agreeing"] == "1"
    studies = seed.read_tsv(seed.RAW_DIR / "gold_studies.tsv")
    assert {r["study_gold_id"] for r in studies if PATH in r["paths"].split("|")} == {"Gs0118069"}
    raw = [r for r in seed.read_tsv(seed.RAW_DIR / "gold_ecosystem_paths.tsv")
           if r["canonical_path"] == PATH]
    assert len(raw) == 1
    assert raw[0]["gold_node_ids"] == "gold.ecosystem:7784"
    assert raw[0]["organism_count"] == raw[0]["total_assertions"] == "0"
    decision = seed.load_decisions(seed.DECISIONS_PATH)[IDENTIFIER]
    assert decision.decision == "GROUND_AS_PARENT"
    assert decision.object_id == "ENVO:01000722"
    assert decision.review_depth == "ITEM"
    assert "one study Gs0118069" in decision.notes


def test_original_ten_context_exclusions_survive_branch_integration():
    expected = {
        "habitatmech:GOLD.88e2b29307": "ENVO:00001999",
        "habitatmech:GOLD.3426da4c96": "habitatmech:GOLD.ce244e62cd",
        "habitatmech:GOLD.ad12f0169a": "ENVO:00002030",
        "habitatmech:GOLD.c18afe6ef1": "ENVO:00002011",
        "habitatmech:GOLD.d14ddff103": "ENVO:00002011",
        "habitatmech:GOLD.b9a8cb85e1": "ENVO:00002011",
        "habitatmech:GOLD.a5e461ce2b": "ENVO:01001511",
        "habitatmech:GOLD.6faa98a0aa": "ENVO:00002011",
        "habitatmech:GOLD.0c89489e1b": "ENVO:01001511",
        IDENTIFIER: "ENVO:01001511",
    }
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    for source, parent in expected.items():
        assert exclusions[source].parent_id == parent
        assert seed.mint("GOLD", exclusions[source].source_path) == source
