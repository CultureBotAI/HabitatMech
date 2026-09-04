#!/usr/bin/env python3
"""Score and rank HabitatRecord YAML by causal-graph completeness and quality."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
HABITATS_DIR = REPO_ROOT / "data" / "habitats"

MECHANISM_NODE_TYPES = {
    "BIOLOGICAL_PROCESS",
    "CAPACITY",
    "CELLULAR_LOCALIZATION",
    "CHEMICAL",
    "COMMUNITY_PROCESS",
    "GENE_OR_PROTEIN",
    "MOLECULAR_FUNCTION",
    "PATHWAY",
    "QUALITY",
    "STATE",
    "TRAIT",
}


@dataclass(frozen=True)
class CausalGraphScore:
    identifier: str
    label: str
    habitat_category: str
    path: str
    graph_score: int
    opportunity_score: int
    graphs: int
    nodes: int
    edges: int
    edge_evidence: int
    node_grounding_pct: int
    predicate_grounding_pct: int
    findings: tuple[str, ...]

    def as_row(self) -> dict[str, object]:
        return {
            "graph_score": self.graph_score,
            "opportunity_score": self.opportunity_score,
            "identifier": self.identifier,
            "label": self.label,
            "habitat_category": self.habitat_category,
            "graphs": self.graphs,
            "nodes": self.nodes,
            "edges": self.edges,
            "edge_evidence": self.edge_evidence,
            "node_grounding_pct": self.node_grounding_pct,
            "predicate_grounding_pct": self.predicate_grounding_pct,
            "findings": "; ".join(self.findings),
            "path": self.path,
        }


def _pct(numerator: int, denominator: int) -> int:
    if not denominator:
        return 0
    return round(100 * numerator / denominator)


def _assertion_total(doc: dict[str, Any]) -> int:
    return sum(a.get("assertion_count") or 0 for a in doc.get("source_attestations") or [])


def opportunity_score(doc: dict[str, Any]) -> int:
    """Estimate how much a graph would add, independent of current graph quality."""
    source_count = len({a.get("source") for a in doc.get("source_attestations") or []})
    parameter_count = len(doc.get("environmental_parameters") or [])
    taxon_count = len(doc.get("characteristic_taxa") or [])
    assertion_credit = min(_assertion_total(doc) // 100, 40)
    parameter_credit = min(parameter_count * 4, 32)
    taxon_credit = min(taxon_count, 16)
    return min(100, source_count * 8 + assertion_credit + parameter_credit + taxon_credit)


def score_record(
    path: Path,
    doc: dict[str, Any],
    *,
    repo_root: Path = REPO_ROOT,
) -> CausalGraphScore:
    graphs = doc.get("causal_graphs") or []
    findings: list[str] = []
    graph_count = len(graphs)
    node_count = 0
    edge_count = 0
    edge_evidence = 0
    grounded_nodes = 0
    grounded_predicates = 0
    described_edges = 0
    evidence_with_snippets = 0
    dangling_edges = 0
    duplicate_nodes = 0
    duplicate_edges = 0
    missing_evidence = 0
    seen_node_types: set[str] = set()

    if not graphs:
        findings.append("missing_causal_graphs")

    for graph in graphs:
        nodes = graph.get("nodes") or []
        edges = graph.get("edges") or []
        node_count += len(nodes)
        edge_count += len(edges)

        node_ids = [node.get("node_id") for node in nodes]
        node_id_set = set(node_ids)
        duplicate_nodes += len(node_ids) - len(node_id_set)
        for node in nodes:
            if node.get("grounding"):
                grounded_nodes += 1
            node_type = node.get("node_type")
            if node_type:
                seen_node_types.add(str(node_type))

        edge_ids = [edge.get("edge_id") for edge in edges]
        duplicate_edges += len(edge_ids) - len(set(edge_ids))
        for edge in edges:
            evidence = edge.get("evidence") or []
            edge_evidence += len(evidence)
            if not evidence:
                missing_evidence += 1
            evidence_with_snippets += sum(1 for item in evidence if item.get("snippet"))
            if edge.get("predicate_id"):
                grounded_predicates += 1
            if edge.get("description"):
                described_edges += 1
            if edge.get("subject") not in node_id_set:
                dangling_edges += 1
            if edge.get("object") not in node_id_set:
                dangling_edges += 1

    if graph_count and edge_count < graph_count * 2:
        findings.append("sparse_graph")
    if duplicate_nodes:
        findings.append(f"duplicate_nodes:{duplicate_nodes}")
    if duplicate_edges:
        findings.append(f"duplicate_edges:{duplicate_edges}")
    if dangling_edges:
        findings.append(f"dangling_edges:{dangling_edges}")
    if missing_evidence:
        findings.append(f"edges_without_evidence:{missing_evidence}")
    if edge_count and described_edges < edge_count:
        findings.append(f"edges_without_description:{edge_count - described_edges}")
    if edge_count and grounded_predicates < edge_count:
        findings.append(f"edges_without_predicate_id:{edge_count - grounded_predicates}")
    if edge_evidence and evidence_with_snippets < edge_evidence:
        findings.append(f"evidence_without_snippet:{edge_evidence - evidence_with_snippets}")
    if node_count and grounded_nodes < node_count:
        findings.append(f"ungrounded_nodes:{node_count - grounded_nodes}")

    score = 0
    if graph_count:
        score += 20
    score += min(16, edge_count * 4)
    score += min(12, node_count * 2)
    score += round(16 * _pct(edge_count - missing_evidence, edge_count) / 100)
    score += round(12 * _pct(evidence_with_snippets, edge_evidence) / 100)
    score += round(10 * _pct(grounded_nodes, node_count) / 100)
    score += round(8 * _pct(grounded_predicates, edge_count) / 100)
    score += round(8 * _pct(described_edges, edge_count) / 100)
    if "HABITAT" in seen_node_types:
        score += 7
    if "ENVIRONMENTAL_PARAMETER" in seen_node_types and seen_node_types & MECHANISM_NODE_TYPES:
        score += 7
    score -= 20 * dangling_edges
    score -= 8 * duplicate_nodes
    score -= 8 * duplicate_edges

    try:
        display_path = str(path.relative_to(repo_root))
    except ValueError:
        display_path = str(path)

    return CausalGraphScore(
        identifier=doc.get("identifier", ""),
        label=doc.get("label", ""),
        habitat_category=doc.get("habitat_category", ""),
        path=display_path,
        graph_score=max(0, min(100, score)),
        opportunity_score=opportunity_score(doc),
        graphs=graph_count,
        nodes=node_count,
        edges=edge_count,
        edge_evidence=edge_evidence,
        node_grounding_pct=_pct(grounded_nodes, node_count),
        predicate_grounding_pct=_pct(grounded_predicates, edge_count),
        findings=tuple(findings),
    )


def load_scores(root: Path = HABITATS_DIR) -> list[CausalGraphScore]:
    scores: list[CausalGraphScore] = []
    for path in sorted(root.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict):
            scores.append(score_record(path, doc))
    return sorted(scores, key=lambda s: (s.graph_score, -s.opportunity_score, s.label, s.identifier))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=HABITATS_DIR)
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--out", type=Path, help="Write the complete ranked worklist as TSV.")
    args = parser.parse_args()

    scores = load_scores(args.root)
    print(f"{len(scores)} habitat record(s) ranked by causal graph quality\n")
    for score in scores[: args.limit]:
        print(
            f"{score.graph_score:3d}  opportunity={score.opportunity_score:3d}  "
            f"{score.label[:44]:44s}  {score.identifier}"
        )
        print(f"     {score.path}")
        if score.findings:
            print(f"     {', '.join(score.findings)}")
        print()

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        fields = list(CausalGraphScore("", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0, ()).as_row())
        with args.out.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(score.as_row() for score in scores)
        print(f"wrote {args.out} ({len(scores)} rows)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
