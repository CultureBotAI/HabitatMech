#!/usr/bin/env python3
"""Run the authoritative HabitatMech quality gate locally and in CI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

COMMANDS = [
    (
        "lint",
        [sys.executable, "-m", "ruff", "check", "."],
        "Fail fast on syntax, import, and style defects before expensive corpus checks.",
    ),
    (
        "documentation",
        [sys.executable, "scripts/check_docs.py", "--check"],
        "Current narrative statistics and repository-owned public links must match generated data.",
    ),
    (
        "raw-data provenance",
        [sys.executable, "scripts/check_provenance.py"],
        "Every committed inventory must retain its source metadata and integrity checks.",
    ),
    (
        "tests",
        [sys.executable, "-m", "pytest", "-q"],
        "Tests cover grounding rules and corpus-wide invariants that per-record validation cannot see.",
    ),
    (
        "schema validation",
        [sys.executable, "scripts/validate_strict.py", "--quiet"],
        "Closed-mode validation checks every record shape; quiet mode keeps the error summary visible.",
    ),
    (
        "corpus reproduction",
        [sys.executable, "scripts/verify_corpus.py"],
        "Schema-valid hand edits are still invalid unless the corpus reproduces exactly from data/raw/.",
    ),
    (
        "generated site",
        [sys.executable, "scripts/render_pages.py", "--check"],
        "The committed, published site must not drift from the corpus that generated it.",
    ),
    (
        "retired URLs",
        [sys.executable, "scripts/build_redirects.py", "--check"],
        "Curation moves record URLs; RETIRED.tsv prevents improvements from creating published 404s.",
    ),
    (
        "term requests",
        [sys.executable, "scripts/build_term_requests.py", "--check"],
        "The committed public curation backlog must agree with reviewed ungrounded records.",
    ),
    (
        "corpus report",
        [sys.executable, "scripts/habitat_report.py"],
        "Exercise cross-corpus analyses and finish with the detailed live curation summary.",
    ),
]


def main() -> int:
    for name, command, rationale in COMMANDS:
        print(f"\n=== qc: {name} ===", flush=True)
        print(f"why: {rationale}", flush=True)
        completed = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if completed.returncode:
            print(f"qc stopped: {name} failed with exit code {completed.returncode}", file=sys.stderr)
            return completed.returncode
    print("\nAll HabitatMech quality gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
