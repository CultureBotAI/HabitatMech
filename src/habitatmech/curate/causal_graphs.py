"""Curated causal-graph overlays for generated HabitatRecords."""

from __future__ import annotations

import copy
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity

from habitatmech.validation.write_validated import DEFAULT_SCHEMA_PATH

__all__ = [
    "CURATED_CAUSAL_GRAPHS_DIR",
    "CausalGraphCuration",
    "CausalGraphCurationError",
    "apply_causal_graph_curations",
    "load_causal_graph_curation_files",
    "load_causal_graph_curations",
    "validate_causal_graph_curations",
]


REPO_ROOT = Path(__file__).resolve().parents[3]
CURATED_CAUSAL_GRAPHS_DIR = REPO_ROOT / "curation" / "causal_graphs"
TARGET_CLASS = "HabitatCausalGraphCuration"

_VALIDATOR: Validator | None = None


class CausalGraphCurationError(SystemExit):
    """A malformed or unverifiable curated causal-graph overlay."""


@dataclass(frozen=True)
class CausalGraphCuration:
    identifier: str
    path: Path
    causal_graphs: tuple[dict[str, Any], ...]
    curation_history: tuple[dict[str, Any], ...]


def _get_validator() -> Validator:
    global _VALIDATOR
    if _VALIDATOR is None:
        _VALIDATOR = Validator(
            schema=str(DEFAULT_SCHEMA_PATH),
            validation_plugins=[JsonschemaValidationPlugin(closed=True)],
        )
    return _VALIDATOR


def _curation_files(root: Path = CURATED_CAUSAL_GRAPHS_DIR) -> list[Path]:
    if root.is_file():
        return [root]
    if not root.exists():
        return []
    return sorted(root.rglob("*.yaml"))


def _validate_schema(doc: dict[str, Any], path: Path) -> None:
    report = _get_validator().validate(doc, target_class=TARGET_CLASS)
    errors = [result for result in report.results if result.severity == Severity.ERROR]
    if not errors:
        return
    details = "\n  ".join(result.message for result in errors[:10])
    more = "" if len(errors) <= 10 else f"\n  ... + {len(errors) - 10} more"
    raise CausalGraphCurationError(
        f"{path}: {len(errors)} LinkML validation error(s):\n  {details}{more}"
    )


def _require_nonempty(value: object, path: Path, where: str, problems: list[str]) -> None:
    if value is None or (isinstance(value, str) and not value.strip()):
        problems.append(f"{path}: {where} is required")


def _validate_graph_integrity(path: Path, identifier: str, graphs: Iterable[dict[str, Any]]) -> None:
    problems: list[str] = []
    graph_ids: set[str] = set()
    graphs = list(graphs)
    if not graphs:
        problems.append(f"{path}: causal_graphs must include at least one graph")

    for graph in graphs:
        graph_id = str(graph.get("graph_id") or "<missing>")
        _require_nonempty(graph.get("graph_id"), path, "graph_id", problems)
        if graph_id in graph_ids:
            problems.append(f"{path}: duplicate graph_id {graph_id!r} for {identifier}")
        graph_ids.add(graph_id)

        nodes = graph.get("nodes") or []
        edges = graph.get("edges") or []
        if not nodes:
            problems.append(f"{path}: {graph_id}: nodes must include at least one node")
        if not edges:
            problems.append(f"{path}: {graph_id}: edges must include at least one edge")

        node_ids: set[str] = set()
        for node in nodes:
            node_id = str(node.get("node_id") or "<missing>")
            _require_nonempty(node.get("node_id"), path, f"{graph_id}: node_id", problems)
            _require_nonempty(
                node.get("label"),
                path,
                f"{graph_id}: node {node_id!r} label",
                problems,
            )
            if node_id in node_ids:
                problems.append(f"{path}: {graph_id}: duplicate node_id {node_id!r}")
            node_ids.add(node_id)

        edge_ids: set[str] = set()
        referenced_node_ids: set[str] = set()
        for edge in edges:
            edge_id = str(edge.get("edge_id") or "<missing>")
            _require_nonempty(
                edge.get("edge_id"), path, f"{graph_id}: edge_id", problems
            )
            _require_nonempty(
                edge.get("predicate"),
                path,
                f"{graph_id}: edge {edge_id!r} predicate",
                problems,
            )
            if edge_id in edge_ids:
                problems.append(f"{path}: {graph_id}: duplicate edge_id {edge_id!r}")
            edge_ids.add(edge_id)
            evidence_items = edge.get("evidence") or []
            if not evidence_items:
                problems.append(
                    f"{path}: {graph_id}: edge {edge_id!r} must include evidence"
                )
            for endpoint in ("subject", "object"):
                node_id = edge.get(endpoint)
                if node_id not in node_ids:
                    problems.append(
                        f"{path}: {graph_id}: edge {edge_id!r} has undeclared "
                        f"{endpoint} {node_id!r}"
                    )
                else:
                    referenced_node_ids.add(str(node_id))
            for i, evidence in enumerate(evidence_items, start=1):
                _require_nonempty(
                    evidence.get("reference"),
                    path,
                    f"{graph_id}: edge {edge_id!r} evidence {i} reference",
                    problems,
                )

        for node_id in sorted(node_ids - referenced_node_ids):
            problems.append(
                f"{path}: {graph_id}: node {node_id!r} is not referenced by any edge"
            )

    if problems:
        raise CausalGraphCurationError(
            "curated causal graphs cannot be applied:\n  " + "\n  ".join(problems)
        )


def load_causal_graph_curation_files(
    paths: Iterable[Path],
) -> dict[str, CausalGraphCuration]:
    """Load overlay files after closed LinkML and graph-integrity validation."""
    curations: dict[str, CausalGraphCuration] = {}
    seen: dict[str, Path] = {}
    for path in sorted(paths):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise CausalGraphCurationError(f"{path}: expected a YAML mapping")

        _validate_schema(doc, path)
        identifier = doc["identifier"]
        if identifier in seen:
            raise CausalGraphCurationError(
                f"{path}: duplicate causal-graph curation for {identifier}; "
                f"already loaded {seen[identifier]}"
            )
        graphs = tuple(copy.deepcopy(doc.get("causal_graphs") or []))
        _validate_graph_integrity(path, identifier, graphs)

        curations[identifier] = CausalGraphCuration(
            identifier=identifier,
            path=path,
            causal_graphs=graphs,
            curation_history=tuple(copy.deepcopy(doc.get("curation_history") or [])),
        )
        seen[identifier] = path
    return curations


def load_causal_graph_curations(
    root: Path = CURATED_CAUSAL_GRAPHS_DIR,
) -> dict[str, CausalGraphCuration]:
    """Load every causal-graph curation overlay under ``root``."""
    return load_causal_graph_curation_files(_curation_files(root))


def validate_causal_graph_curations(
    curations: Mapping[str, CausalGraphCuration],
    concepts: Mapping[str, object],
    *,
    path: Path = CURATED_CAUSAL_GRAPHS_DIR,
) -> None:
    """Verify that every overlay extends a record emitted by the seeder."""
    missing = sorted(set(curations) - set(concepts))
    if missing:
        raise CausalGraphCurationError(
            f"{path}: causal-graph curation for missing HabitatRecord(s): "
            + ", ".join(missing)
        )


def apply_causal_graph_curations(
    concepts: Mapping[str, Any],
    curations: Mapping[str, CausalGraphCuration],
) -> None:
    """Attach curated causal graphs and their history events to concepts."""
    for identifier, curation in sorted(curations.items()):
        concept = concepts[identifier]
        concept.causal_graphs = list(copy.deepcopy(curation.causal_graphs))
        concept.causal_graph_events = list(copy.deepcopy(curation.curation_history))
