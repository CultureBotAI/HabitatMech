"""Schema-level checks: it loads, and the corpus only uses values it declares."""

from __future__ import annotations

import yaml
from linkml_runtime.utils.schemaview import SchemaView


def _schema(schema_path):
    return SchemaView(str(schema_path))


def test_schema_loads_with_its_imports(schema_path):
    view = _schema(schema_path)
    assert "HabitatRecord" in view.all_classes()
    # The vendored mech_shared module must resolve, or Discussion/Dataset
    # silently disappear from the record shape.
    assert "Discussion" in view.all_classes()
    assert "Dataset" in view.all_classes()


def test_habitat_record_is_the_only_tree_root(schema_path):
    view = _schema(schema_path)
    roots = [name for name, cls in view.all_classes().items() if cls.tree_root]
    assert roots == ["HabitatRecord"]


def test_mech_shared_is_vendored_byte_identical(repo_root):
    """The shared module is vendored across the Mech repos and must not be
    edited in one place. Its own docstring says so; this makes it checkable
    here by pinning the sha of the copy we shipped."""
    import hashlib

    path = repo_root / "src" / "habitatmech" / "schema" / "mech_shared.yaml"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    expected = "1a5e21eb2ee9f3584ff6af3a6906b1d442e18c41de405b1bf907c20f44eafa2a"
    assert digest == expected, (
        "mech_shared.yaml has been edited locally. It is vendored byte-identical "
        "across the Mech repos — change it once upstream and re-vendor everywhere, "
        "then update this pin."
    )


def _permissible(view, enum_name: str) -> set[str]:
    return set(view.get_enum(enum_name).permissible_values)


def test_corpus_uses_only_declared_enum_values(schema_path, records):
    """LinkML validation already enforces this per record, but only for records
    written through the gate. This catches a hand-edited value across the whole
    corpus in one place."""
    view = _schema(schema_path)
    checks = [
        ("habitat_category", "HabitatCategoryEnum", lambda d: [d.get("habitat_category")]),
        ("grounding_status", "GroundingStatusEnum", lambda d: [d.get("grounding_status")]),
        ("mapping_status", "MappingStatusEnum", lambda d: [d.get("mapping_status")]),
        ("source", "HabitatSourceEnum",
         lambda d: [a.get("source") for a in d.get("source_attestations") or []]),
        ("assertion_unit", "AssertionUnitEnum",
         lambda d: [a.get("assertion_unit") for a in d.get("source_attestations") or []]),
        ("parameter", "EnvironmentalParameterEnum",
         lambda d: [p.get("parameter") for p in d.get("environmental_parameters") or []]),
        ("synonym_type", "SynonymTypeEnum",
         lambda d: [s.get("synonym_type") for s in d.get("synonyms") or []]),
    ]
    for field, enum_name, extract in checks:
        allowed = _permissible(view, enum_name)
        bad = set()
        for _, doc in records:
            for value in extract(doc):
                if value is not None and value not in allowed:
                    bad.add(value)
        assert not bad, f"{field}: values not in {enum_name}: {sorted(bad)}"


def test_category_directories_match_the_enum(repo_root, schema_path):
    """The filesystem layout is derived from HabitatCategoryEnum. A directory
    that is not an enum value means the seeder and the schema have diverged."""
    view = _schema(schema_path)
    allowed = {v.lower() for v in _permissible(view, "HabitatCategoryEnum")}
    habitats = repo_root / "data" / "habitats"
    if not habitats.exists():
        return
    unexpected = {d.name for d in habitats.iterdir() if d.is_dir()} - allowed
    assert not unexpected, f"category directories not in the enum: {sorted(unexpected)}"


def test_schema_prefixes_cover_every_identifier_in_the_corpus(schema_path, records):
    """A CURIE whose prefix the schema does not declare cannot be expanded to a
    URI, so it is not resolvable by any downstream consumer."""
    declared = set(yaml.safe_load(schema_path.read_text(encoding="utf-8"))["prefixes"])
    used = set()
    for _, doc in records:
        used.add(doc["identifier"].split(":", 1)[0])
        for parent in doc.get("parent_habitats") or []:
            used.add(parent.split(":", 1)[0])
        for xref in doc.get("xrefs") or []:
            used.add(xref.split(":", 1)[0])
    missing = used - declared
    assert not missing, f"prefixes used in the corpus but undeclared in the schema: {sorted(missing)}"
