#!/usr/bin/env python3
"""Validate curated causal-graph overlays and their target HabitatRecords."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from habitatmech.curate.causal_graphs import (  # noqa: E402
    CURATED_CAUSAL_GRAPHS_DIR,
    load_causal_graph_curations,
)
from habitatmech.seed import build_corpus  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=CURATED_CAUSAL_GRAPHS_DIR,
        help="Directory containing HabitatCausalGraphCuration YAML files.",
    )
    args = parser.parse_args(argv)

    curations = load_causal_graph_curations(args.root)
    build_corpus(causal_graphs_root=args.root)
    graph_count = sum(len(curation.causal_graphs) for curation in curations.values())
    print(
        f"validated {len(curations)} causal-graph curation file(s) "
        f"with {graph_count} graph(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
