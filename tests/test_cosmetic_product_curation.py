"""A rationale correction must not change cosmetic-product scientific claims."""

from dataclasses import replace

from habitatmech import seed


def test_cosmetic_product_rationale_correction_has_exact_scope(monkeypatch):
    identifier = "ENVO:00003893"
    source = "habitatmech:GOLD.0792bc5bfe"
    path = "Engineered > Industrial production > Chemical products > Cosmetic products"
    old_note = "Leaf label equals the ENVO label exactly and no other source concept claims it."
    new_note = (
        "The plural source label is curator-recognized as equivalent to the singular ENVO "
        "label in this product context; normalized labels are not equal and the automatic "
        "route is gold_unmatched."
    )
    decisions = seed.load_decisions(seed.DECISIONS_PATH)
    decision = decisions[source]
    assert decision.notes == f"{new_note} Path: {path}"
    assert decision.review_depth == "ITEM"
    assert seed.norm_label("Cosmetic products") != seed.norm_label("cosmetic product")
    assert seed.mint("GOLD", path) == source

    after = {c.identifier: seed.build_document(c) for c in seed.build_corpus().concepts}
    decisions[source] = replace(decision, notes=f"{old_note} Path: {path}")
    monkeypatch.setattr(seed, "load_decisions", lambda path: decisions)
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
    assert new["parent_habitats"] == ["ENVO:00003074", "ENVO:2000000"]
    assert new["synonyms"] == [{
        "synonym_text": "Cosmetic products", "synonym_type": "EXACT_SYNONYM", "source": "GOLD",
    }]
    assert new["source_attestations"] == [{
        "source": "GOLD", "source_id": "gold.ecosystem:8328", "source_label": "Cosmetic products",
        "source_path": path, "mapping_predicate": "skos:exactMatch",
        "notes": "2 GOLD ecosystem node ids share this path; first shown. "
                 "See data/raw/gold_ecosystem_paths.tsv.",
    }]
    row = next(row for row in seed.read_tsv(seed.RAW_DIR / "gold_ecosystem_paths.tsv")
               if row["canonical_path"] == path)
    assert set(row["gold_node_ids"].split("|")) == {
        "gold.ecosystem:8328", "gold.ecosystem:8329",
    }
    ontology = seed.OntologyIndex(
        seed.read_tsv("ontology_terms.tsv"), seed.read_tsv("ontology_subclass_edges.tsv"),
    )
    mapping = {}
    for mapping_row in seed.read_tsv("isolation_source_groundings.tsv"):
        for field in ("subject_label", "subject_label_normalized"):
            key = seed.norm_label(mapping_row[field])
            if key:
                mapping.setdefault(key, mapping_row)
    gold_rows = seed.read_tsv("gold_ecosystem_paths.tsv")
    default = seed.resolve_gold(
        row, ontology, mapping, seed.leaf_claimants(gold_rows), seed.composed_claimants(gold_rows),
    )
    assert default.route == "gold_unmatched"
    assert default.identifier == source
    assert default.grounding_status == "UNGROUNDED"
