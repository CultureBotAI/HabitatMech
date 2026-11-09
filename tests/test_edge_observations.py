"""Native association exports preserve scope, owner evidence and publication integrity."""

import csv
import importlib
import io
import json
import os
from pathlib import Path

import pytest
import yaml

from habitatmech import edge_observations as adapter


@pytest.fixture(autouse=True)
def shared_contract():
    if os.environ.get("REQUIRE_EDGE_CONTRACT") == "1":
        importlib.import_module("kg_microbe_curation.native")
    else:
        pytest.importorskip("kg_microbe_curation.native")


def native_rows(surface):
    profile = adapter.SURFACES[surface]
    row = {
        profile["key"]: "ENVO:00001998",
        "taxon_id": "NCBITaxon:562",
        "taxon_label": "Escherichia coli",
        "corroborated_by": "BACDIVE|MADIN",
    }
    if surface == "bacdive":
        row.update(bacdive_id="bacdive.isolation_source:soil", rank="01", strain_count="0002")
    elif surface == "prego":
        row.update(rank="01", prego_score="4.007270", direct_flag="TRUE", channels="a|b")
    owner = {profile["key"]: row[profile["key"]], "taxon_count": "09000", "mapping_status": "REVIEWED"}
    return row, owner


def direct(surface, row=None, owner=None):
    default_row, default_owner = native_rows(surface)
    profile = adapter.SURFACES[surface]
    paths = (
        profile["source"],
        profile["owner"],
        adapter.MANIFEST,
        adapter.SCHEMA,
        adapter.SEMANTICS,
        adapter.HARMONIZATION,
        adapter.EXTRACTOR,
    )
    return adapter.adapt_observation(
        row or default_row,
        position=1,
        owner=(1, owner or default_owner),
        retained=2,
        commit="a" * 40,
        surface=surface,
        hashes={path: "b" * 64 for path in paths},
        prefixes={},
        upstream="kg-microbe@pinned",
    )


@pytest.mark.parametrize("surface", adapter.SURFACES)
def test_native_association_is_not_reviewed_by_its_owner(surface):
    row, owner = native_rows(surface)
    result = direct(surface)
    assert result["payload"]["native_payload"] == row
    assert result["payload"]["context"]["owner_binding"]["native_payload"] == owner
    assert result["payload"]["context"]["candidate_pool"] == "09000"
    assert result["payload"]["context"]["native_inventory_is_subset"] is True
    assert result["payload"]["predicate"] == "habitatmech:characteristic_taxa"
    assert result["assurance"] == "unassessed"
    assert result["native_review"]["locator"] is None
    assert result["independent_scientific_review"] is False


def test_counts_flags_channels_and_unranked_scope_are_lossless():
    bacdive = direct("bacdive")["payload"]
    assert bacdive["native_payload"]["strain_count"] == "0002"
    assert bacdive["context"]["association_count_unit"] == "STRAIN"
    prego = direct("prego")["payload"]
    assert prego["native_payload"]["prego_score"] == "4.007270"
    assert prego["native_payload"]["direct_flag"] == "TRUE"
    assert prego["native_payload"]["channels"] == "a|b"
    madin = direct("madin")["payload"]
    assert "rank" not in madin["native_payload"]
    assert "association_count_unit" not in madin["context"]


def test_owner_context_changes_assertion_identity_without_changing_source_row():
    row, owner = native_rows("prego")
    original = direct("prego")
    changed = direct("prego", row, {**owner, "taxon_count": "10000"})
    assert original["native_locator"]["payload_sha256"] == changed["native_locator"]["payload_sha256"]
    assert original["assertion_id"] != changed["assertion_id"]


def fixture_sources(surface="prego", malformed=False):
    row, owner = native_rows(surface)
    profile = adapter.SURFACES[surface]

    def tsv(rows):
        handle = io.StringIO()
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        return handle.getvalue().encode()

    rows = [row, {**row, "taxon_id": "NCBITaxon:invalid" if malformed else "NCBITaxon:570"}]
    return {
        profile["source"]: tsv(rows),
        profile["owner"]: tsv([owner]),
        adapter.MANIFEST: yaml.safe_dump(
            {
                "kg_microbe_source": "kg-microbe@pinned",
                "outputs": [
                    {"path": Path(profile["source"]).name, "rows": 2},
                    {"path": Path(profile["owner"]).name, "rows": 1},
                ],
            }
        ).encode(),
        adapter.SCHEMA: b"prefixes: {}\n",
        adapter.SEMANTICS: b"Native scope.\n",
        adapter.HARMONIZATION: b"Selected association scope.\n",
        adapter.EXTRACTOR: b"Pinned native extraction source.\n",
    }


def install_sources(monkeypatch, sources):
    def git(command, **kwargs):
        if "get-url" in command:
            return "https://github.com/CultureBotAI/HabitatMech.git\n"
        return sources[command[-1].split(":", 1)[1]]

    monkeypatch.setattr(adapter.subprocess, "check_output", git)


def test_real_spawn_matches_serial_and_preserves_source_order(tmp_path, monkeypatch):
    install_sources(monkeypatch, fixture_sources())
    serial, parallel = tmp_path / "serial", tmp_path / "parallel"
    first = adapter.export_observations(tmp_path, "a" * 40, "prego", serial, None, workers=1)
    second = adapter.export_observations(tmp_path, "a" * 40, "prego", parallel, None, workers=4)
    assert (serial / "assertions.jsonl").read_bytes() == (parallel / "assertions.jsonl").read_bytes()
    assert first["assertion_membership_sha256"] == second["assertion_membership_sha256"]
    assert second["rows"] == 2
    assert second["native_status_counts"] == {"unassessed": 2}
    assert second["validation_workers"] == 4


def test_worker_failure_does_not_publish(tmp_path, monkeypatch):
    install_sources(monkeypatch, fixture_sources(malformed=True))
    output = tmp_path / "output"
    with pytest.raises(ValueError, match="identity differs"):
        adapter.export_observations(tmp_path, "a" * 40, "prego", output, None, workers=4)
    assert not output.exists()


@pytest.mark.parametrize("mutation", ["reverse", "duplicate"])
def test_valid_row_mutations_are_rejected_before_publication(tmp_path, monkeypatch, mutation):
    install_sources(monkeypatch, fixture_sources())
    original_open, changed = Path.open, False

    def mutate_readback(path, mode="r", *args, **kwargs):
        nonlocal changed
        if path.name == "assertions.jsonl" and mode == "rb" and not changed:
            changed = True
            with original_open(path, "rb") as handle:
                lines = handle.readlines()
            assert all(json.loads(line)["assurance"] == "unassessed" for line in lines)
            with original_open(path, "wb") as handle:
                handle.writelines(lines[::-1] if mutation == "reverse" else [lines[0], lines[0]])
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", mutate_readback)
    output = tmp_path / "output"
    with pytest.raises(ValueError, match="Persisted native bytes"):
        adapter.export_observations(tmp_path, "a" * 40, "prego", output, None)
    assert changed and not output.exists()


@pytest.mark.parametrize("failure", ["owner", "manifest", "tail"])
def test_full_inventory_preflight_rejects_invalid_unselected_input(tmp_path, monkeypatch, failure):
    sources = fixture_sources()
    profile = adapter.SURFACES["prego"]
    if failure == "owner":
        sources[profile["owner"]] = sources[profile["owner"]].replace(b"ENVO:00001998", b"ENVO:other")
    elif failure == "manifest":
        sources[adapter.MANIFEST] = sources[adapter.MANIFEST].replace(b"rows: 2", b"rows: 3")
    else:
        sources[profile["source"]] += b"malformed\n"
    install_sources(monkeypatch, sources)
    with pytest.raises(ValueError):
        adapter.export_observations(tmp_path, "a" * 40, "prego", tmp_path / "output", [1])
    assert not (tmp_path / "output").exists()
