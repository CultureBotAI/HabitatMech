from __future__ import annotations

from pathlib import Path

from scripts.rank_causal_graphs import score_record


def test_record_without_causal_graphs_scores_at_the_floor():
    score = score_record(
        Path("none.yaml"),
        {"identifier": "ENVO:1", "label": "no graph", "habitat_category": "OTHER"},
    )

    assert score.graph_score == 0
    assert score.findings == ("missing_causal_graphs",)


def test_evidence_backed_graph_scores_above_sparse_graph():
    strong = score_record(
        Path("strong.yaml"),
        {
            "identifier": "ENVO:1",
            "label": "strong",
            "habitat_category": "AQUATIC",
            "causal_graphs": [
                {
                    "graph_id": "g1",
                    "nodes": [
                        {
                            "node_id": "habitat",
                            "label": "habitat",
                            "node_type": "HABITAT",
                            "grounding": "ENVO:1",
                        },
                        {
                            "node_id": "salinity",
                            "label": "salinity",
                            "node_type": "ENVIRONMENTAL_PARAMETER",
                            "grounding": "PATO:1",
                        },
                        {
                            "node_id": "osmoadaptation",
                            "label": "osmoadaptation",
                            "node_type": "BIOLOGICAL_PROCESS",
                            "grounding": "GO:1",
                        },
                    ],
                    "edges": [
                        {
                            "edge_id": "e1",
                            "subject": "habitat",
                            "predicate": "has condition",
                            "predicate_id": "RO:1",
                            "object": "salinity",
                            "description": "Habitat has high salinity.",
                            "evidence": [{"reference": "PMID:1", "snippet": "salinity"}],
                        },
                        {
                            "edge_id": "e2",
                            "subject": "salinity",
                            "predicate": "selects for",
                            "predicate_id": "RO:1",
                            "object": "osmoadaptation",
                            "description": "Salinity selects for osmoadaptation.",
                            "evidence": [{"reference": "PMID:2", "snippet": "osmoadaptation"}],
                        },
                    ],
                }
            ],
        },
    )
    sparse = score_record(
        Path("sparse.yaml"),
        {
            "identifier": "ENVO:2",
            "label": "sparse",
            "habitat_category": "AQUATIC",
            "causal_graphs": [
                {
                    "graph_id": "g1",
                    "nodes": [
                        {
                            "node_id": "salinity",
                            "label": "salinity",
                            "node_type": "ENVIRONMENTAL_PARAMETER",
                        },
                        {
                            "node_id": "osmoadaptation",
                            "label": "osmoadaptation",
                            "node_type": "BIOLOGICAL_PROCESS",
                        },
                    ],
                    "edges": [
                        {
                            "edge_id": "e1",
                            "subject": "salinity",
                            "predicate": "selects for",
                            "object": "osmoadaptation",
                            "evidence": [],
                        }
                    ],
                }
            ],
        },
    )

    assert strong.graph_score > sparse.graph_score
    assert "sparse_graph" in sparse.findings
    assert "edges_without_evidence:1" in sparse.findings


def test_dangling_edges_are_penalized():
    score = score_record(
        Path("dangling.yaml"),
        {
            "identifier": "ENVO:3",
            "label": "dangling",
            "habitat_category": "AQUATIC",
            "causal_graphs": [
                {
                    "graph_id": "g1",
                    "nodes": [
                        {
                            "node_id": "salinity",
                            "label": "salinity",
                            "node_type": "ENVIRONMENTAL_PARAMETER",
                        }
                    ],
                    "edges": [
                        {
                            "edge_id": "e1",
                            "subject": "salinity",
                            "predicate": "selects for",
                            "object": "missing",
                            "evidence": [{"reference": "PMID:1"}],
                        }
                    ],
                }
            ],
        },
    )

    assert "dangling_edges:1" in score.findings
    assert score.graph_score < 40
