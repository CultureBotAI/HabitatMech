#!/usr/bin/env python3
"""Run the authoritative HabitatMech quality gate locally and in CI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

COMMANDS = [
    ("lint", [sys.executable, "-m", "ruff", "check", "."]),
    ("documentation", [sys.executable, "scripts/check_docs.py", "--check"]),
    ("raw-data provenance", [sys.executable, "scripts/check_provenance.py"]),
    ("tests", [sys.executable, "-m", "pytest"]),
    ("schema validation", [sys.executable, "scripts/validate_strict.py"]),
    ("corpus reproduction", [sys.executable, "scripts/verify_corpus.py"]),
    ("generated site", [sys.executable, "scripts/render_pages.py", "--check"]),
    ("retired URLs", [sys.executable, "scripts/build_redirects.py", "--check"]),
    ("term requests", [sys.executable, "scripts/build_term_requests.py", "--check"]),
    ("corpus report", [sys.executable, "scripts/habitat_report.py"]),
]


def main() -> int:
    for name, command in COMMANDS:
        print(f"\n=== qc: {name} ===", flush=True)
        completed = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if completed.returncode:
            print(f"qc stopped: {name} failed with exit code {completed.returncode}", file=sys.stderr)
            return completed.returncode
    print("\nAll HabitatMech quality gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
