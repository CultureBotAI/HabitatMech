"""Bounded source-context and attestation repairs from PR #1885."""

import pytest

from habitatmech import seed
from habitatmech.curate.decisions import Decision

CONTEXT = {
    "habitatmech:GOLD.03fc563fae": ("habitatmech:GOLD.03fc563fae", "ENVO:00002043"),
    "habitatmech:GOLD.b0f6a1ef74": ("habitatmech:GOLD.b0f6a1ef74", "habitatmech:GOLD.5f3cbd7563"),
    "habitatmech:GOLD.2021aa3231": ("ENVO:01000371", "mesh:D062611"),
    "habitatmech:GOLD.099b899fb9": ("habitatmech:GOLD.099b899fb9", "ENVO:00002126"),
    "habitatmech:GOLD.94928acca0": ("habitatmech:GOLD.94928acca0", "habitatmech:GOLD.013b99db03"),
    "habitatmech:GOLD.5d882de599": ("habitatmech:GOLD.5d882de599", "habitatmech:GOLD.827b5dbbef"),
}


@pytest.fixture(scope="module")
def documents():
    return {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}


def test_context_exclusions_change_only_six_parent_contributions(documents, monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        k: v for k, v in exclusions.items() if k not in CONTEXT
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == documents.keys()
    assert {k for k in before if before[k] != documents[k]} == {v[0] for v in CONTEXT.values()}
    for source, (identifier, parent) in CONTEXT.items():
        old, new = before[identifier], documents[identifier]
        assert seed.mint("GOLD", exclusions[source].source_path) == source
        assert exclusions[source].parent_id == parent
        assert parent in old["parent_habitats"]
        assert new.get("parent_habitats", []) == [p for p in old["parent_habitats"] if p != parent]
        ignored = {"parent_habitats", "curation_history"}
        assert {k: v for k, v in old.items() if k not in ignored} == {
            k: v for k, v in new.items() if k not in ignored
        }
        added = [e for e in new["curation_history"] if e not in old["curation_history"]]
        assert len(added) == 1 and added[0]["action"] == "SOURCE_PARENT_EXCLUDED"
        assert source in added[0]["changes"] and parent in added[0]["changes"]
        assert [e for e in new["curation_history"] if e not in added] == old["curation_history"]
    assert documents["habitatmech:GOLD.94928acca0"]["parent_habitats"] == ["ENVO:00002005"]


def decision(kind, status="", target="ENVO:00000001"):
    return Decision(identifier="k", decision=kind, object_id=target, object_label="target",
                    grounding_status=status, curator="test", date="2026-10-10", notes="n" * 30)


@pytest.mark.parametrize("status,predicate", [
    ("EXACT", "skos:exactMatch"), ("BROAD", "skos:broadMatch"),
    ("CLOSE", "skos:closeMatch"), ("NARROW", "skos:narrowMatch"),
])
def test_prego_ground_preserves_source_record_mapping(status, predicate):
    source = "ENVO:00002265"
    row = {"prego_id": source, "taxon_count": "5", "max_prego_score": "4", "channels": "x"}
    taxa = [{"prego_id": source, "taxon_id": "NCBITaxon:409", "rank": "1"}]
    store = seed.ConceptStore(seed.OntologyIndex([], []))
    seed.ingest_prego(store, [row], taxa, seed.Counter(), {
        seed.mint("PREGO", source): decision("GROUND", status)
    })
    concept = store.concepts["ENVO:00000001"]
    attestation = concept.attestations[0]
    assert attestation == {"source": "PREGO", "source_id": source, "source_label": source,
                           "mapping_predicate": predicate, "assertion_count": 5,
                           "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "x"}
    assert concept.taxa["NCBITaxon:409"]["rank"] == 1
    assert len(concept.attestation_corrections) == 1


@pytest.mark.parametrize("kind,status", [(None, ""), ("REVIEW", ""),
                                         ("GROUND_AS_PARENT", "NARROW"),
                                         ("CONFIRM_UNGROUNDED", ""), ("SAME_AS", "")])
def test_prego_does_not_copy_parent_or_invent_default_predicate(kind, status):
    source = "ENVO:00002265"
    store = seed.ConceptStore(seed.OntologyIndex([], []))
    decisions = {seed.mint("PREGO", source): decision(kind, status)} if kind else {}
    seed.ingest_prego(store, [{"prego_id": source}], [], seed.Counter(), decisions)
    concept = next(iter(store.concepts.values()))
    assert "mapping_predicate" not in concept.attestations[0]
    assert not concept.attestation_corrections


@pytest.mark.parametrize("kind,status,changed", [
    (None, "", False), ("REVIEW", "", False), ("CONFIRM_UNGROUNDED", "", False),
    ("GROUND", "EXACT", True), ("GROUND_AS_PARENT", "NARROW", True),
    ("NOT_APPLICABLE", "", True), ("SAME_AS", "", True),
])
def test_declined_bacdive_note_distinguishes_override(kind, status, changed):
    source = "bacdive.isolation_source:air-conditioner"
    row = {"bacdive_id": source, "label": "Air-conditioner", "source_slug": "air-conditioner",
           "strain_count": "16"}
    store = seed.ConceptStore(seed.OntologyIndex([], []))
    decisions = {seed.mint("BACDIVE", source): decision(kind, status)} if kind else {}
    seed.ingest_bacdive(store, [row], {"air conditioner": {"object_id": ""}},
                       seed.Counter(), decisions)
    concept = next(iter(store.concepts.values()))
    attestation = concept.attestations[0]
    assert attestation["assertion_count"] == 16 and attestation["assertion_unit"] == "STRAIN"
    assert attestation["source_id"] == source
    assert bool(concept.attestation_corrections) == changed
    if changed:
        assert f"decision {kind} overrides" in attestation["notes"]
        assert f"emitted on {concept.identifier}" in attestation["notes"]
        assert "treated as ungrounded" not in attestation["notes"]
        # SAME_AS uses a transient grounding placeholder, not the survivor's status.
        assert "(UNGROUNDED)" not in attestation["notes"]
    else:
        assert "treated as ungrounded rather than re-grounded by lexical match" in attestation["notes"]


def test_real_prego_broad_and_bacdive_override_witnesses(documents):
    waste = documents["ENVO:01000371"]
    prego = next(a for a in waste["source_attestations"] if a["source"] == "PREGO")
    assert prego["source_id"] == "ENVO:00002265"
    assert prego["mapping_predicate"] == "skos:broadMatch"
    assert prego["assertion_unit"] == "TAXON"
    ac = documents["ENVO:00002874"]
    assert ac["source_attestations"][0]["mapping_predicate"] == "skos:exactMatch"
    assert "decision GROUND overrides" in ac["source_attestations"][0]["notes"]
    for doc in (waste, ac):
        corrections = [e for e in doc["curation_history"] if e["action"] == "SOURCE_ATTESTATION_CORRECTED"]
        assert len(corrections) == 1
        assert corrections[0]["timestamp"] == "2026-10-10T00:00:00Z"


def test_scrubber_definition_does_not_infer_packed_wet_design(documents):
    doc = documents["habitatmech:GOLD.ebf95a8a4a"]
    assert "scrubbing medium" in doc["definition"]
    assert not any(word in doc["definition"] for word in ("packing", "recirculating", "liquid", "biofilm"))
    assert not doc.get("synonyms")
    assert doc["parent_habitats"] == ["ENVO:00003074"]
    assert doc["grounding_status"] == "UNGROUNDED" and doc["mapping_status"] == "REVIEWED"
    assert doc["source_attestations"][0]["source_id"] == "gold.ecosystem:5805"
