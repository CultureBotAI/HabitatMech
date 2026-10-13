"""Bound the material-parent fixes and the paper-note rationale correction."""

from dataclasses import replace

from habitatmech import seed
from habitatmech.text_map_inputs import build_context, semantic_text

MATERIALS = {
    "habitatmech:GOLD.808ed1c989": (
        "ENVO:03600078",
        "Engineered > Built environment > Oil refinery > Crude oil sludge",
        ["gold.ecosystem:4867"],
    ),
    "habitatmech:GOLD.083ab65161": (
        "habitatmech:GOLD.583dbbd71a",
        "Engineered > Built environment > Mushroom farm > Cultivation substrate",
        ["gold.ecosystem:7851", "gold.ecosystem:7852"],
    ),
}


def test_material_exclusions_change_only_context_edges_and_audit(monkeypatch):
    exclusions = seed.load_gold_parent_exclusions(seed.GOLD_PARENT_EXCLUSIONS_PATH)
    assert MATERIALS.keys() <= exclusions.keys()
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    monkeypatch.setattr(seed, "load_gold_parent_exclusions", lambda _: {
        key: row for key, row in exclusions.items() if key not in MATERIALS
    })
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == MATERIALS.keys()
    context = build_context(seed.REPO_ROOT)
    assert {key for key in before
            if semantic_text(before[key], context) != semantic_text(after[key], context)} == (
        MATERIALS.keys()
    )
    rows = {row["canonical_path"]: row for row in seed.read_tsv("gold_ecosystem_paths.tsv")}
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    for identifier, (parent, path, nodes) in MATERIALS.items():
        old, new = before[identifier], after[identifier]
        assert seed.mint("GOLD", path) == identifier
        assert exclusions[identifier].source_path == path
        assert exclusions[identifier].parent_id == parent
        assert old["parent_habitats"] == [parent]
        assert "parent_habitats" not in new
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["action"] == "SOURCE_PARENT_EXCLUDED"
        assert event["timestamp"] == "2026-10-08T00:00:00Z"
        assert event["curator"] == "codex-gpt-5"
        assert identifier in event["changes"] and parent in event["changes"]
        for field in (old.keys() | new.keys()) - {"parent_habitats", "curation_history"}:
            assert new.get(field) == old.get(field), (identifier, field)
        assert decisions[identifier].review_depth == "CLASS"
        assert new["grounding_status"] == "UNGROUNDED"
        assert new["mapping_status"] == "SEEDED"
        assert new["habitat_category"] == "ENGINEERED"
        assert rows[path]["gold_node_ids"].split("|") == nodes
        attestation, = new["source_attestations"]
        assert attestation["source_path"] == path
        assert attestation["source_id"] == nodes[0]
        assert "assertion_count" not in attestation
        assert "assertion_unit" not in attestation
        assert "mapping_predicate" not in attestation
        assert ("notes" in attestation) == (len(nodes) > 1)
        if len(nodes) > 1:
            assert "2 GOLD ecosystem node ids" in attestation["notes"]


def test_currency_rationale_preserves_all_scientific_fields(monkeypatch):
    identifier = "ENVO:00003896"
    source = "habitatmech:GOLD.54bc9674a9"
    path = "Engineered > Paper > Currency notes"
    old_note = "Leaf label equals the ENVO label exactly and no other source concept claims it."
    new_note = (
        "The plural source label is curator-recognized as equivalent to the singular ENVO "
        "label in this paper-note context; normalized labels are not equal and the automatic "
        "route is gold_unmatched."
    )
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decision = decisions[source]
    assert decision.notes == f"{new_note} Path: {path}"
    assert decision.review_depth == "ITEM"
    assert seed.norm_label("Currency notes") != seed.norm_label("currency note")
    assert seed.mint("GOLD", path) == source
    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    decisions[source] = replace(decision, notes=f"{old_note} Path: {path}")
    monkeypatch.setattr(seed, "load_decisions", lambda _: decisions)
    before = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    assert before.keys() == after.keys()
    assert {key for key in before if before[key] != after[key]} == {identifier}
    old, new = before[identifier], after[identifier]
    for field in (old.keys() | new.keys()) - {"curation_history"}:
        assert new.get(field) == old.get(field), field
    assert len(old["curation_history"]) == len(new["curation_history"]) == 2
    assert new["curation_history"][0] == {
        **old["curation_history"][0],
        "changes": old["curation_history"][0]["changes"].replace(old_note, new_note),
    }
    assert new["curation_history"][0]["curator"] == "claude-opus-5"
    assert new["curation_history"][0]["timestamp"] == "2026-08-12T00:00:00Z"
    assert new["curation_history"][1] == old["curation_history"][1]
    assert new["grounding_status"] == "EXACT" and new["mapping_status"] == "REVIEWED"
    assert new["parent_habitats"] == ["ENVO:00003895", "ENVO:03501256"]
    assert new["synonyms"] == [
        {"synonym_text": "Currency notes", "synonym_type": "EXACT_SYNONYM", "source": "GOLD"},
        {"synonym_text": "bank note", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"},
    ]
    attestation, = new["source_attestations"]
    assert attestation["source_id"] == "gold.ecosystem:4388"
    assert attestation["source_path"] == path
    assert attestation["mapping_predicate"] == "skos:exactMatch"
    assert "3 GOLD ecosystem node ids" in attestation["notes"]
    assert "assertion_count" not in attestation and "assertion_unit" not in attestation
    ontology = seed.OntologyIndex(
        seed.read_tsv("ontology_terms.tsv"), seed.read_tsv("ontology_subclass_edges.tsv"),
    )
    mapping = {}
    for row in seed.read_tsv("isolation_source_groundings.tsv"):
        for field in ("subject_label", "subject_label_normalized"):
            key = seed.norm_label(row[field])
            if key:
                mapping.setdefault(key, row)
    rows = seed.read_tsv("gold_ecosystem_paths.tsv")
    row = next(row for row in rows if row["canonical_path"] == path)
    assert row["gold_node_ids"].split("|") == [
        "gold.ecosystem:4388", "gold.ecosystem:4389", "gold.ecosystem:4390",
    ]
    default = seed.resolve_gold(
        row, ontology, mapping, seed.leaf_claimants(rows), seed.composed_claimants(rows),
    )
    assert default.route == "gold_unmatched"
    assert default.identifier == source and default.grounding_status == "UNGROUNDED"
