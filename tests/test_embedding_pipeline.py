"""The text-map runtime enforces immutable bundle pointers."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from scripts import embedding_pipeline as pipeline


def _write_bundle(output: Path, bundle_name: str, manifest: dict) -> Path:
    bundle = output / bundle_name
    bundle.mkdir(parents=True)
    manifest_path = bundle / "manifest.json"
    manifest_path.write_bytes(pipeline.canonical(manifest) + b"\n")
    pipeline.atomic_json(
        output / "current.json",
        {
            "bundle": bundle.name,
            "manifest_sha256": pipeline.digest_file(manifest_path),
        },
    )
    return bundle


def test_current_bundle_names_the_canonical_manifest_identity(tmp_path):
    manifest = {"format_version": pipeline.FORMAT_VERSION, "representation": "semantic-text"}
    identity = hashlib.sha256(pipeline.canonical(manifest)).hexdigest()

    bundle = _write_bundle(tmp_path, identity, manifest)

    assert pipeline.current_bundle(tmp_path) == bundle


def test_current_bundle_refuses_a_renamed_generation(tmp_path):
    manifest = {"format_version": pipeline.FORMAT_VERSION, "representation": "semantic-text"}
    renamed = "0" * 64
    assert renamed != hashlib.sha256(pipeline.canonical(manifest)).hexdigest()
    _write_bundle(tmp_path, renamed, manifest)

    with pytest.raises(pipeline.ContractError, match="immutable generation"):
        pipeline.current_bundle(tmp_path)
