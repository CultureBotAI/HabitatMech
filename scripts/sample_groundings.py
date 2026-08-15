#!/usr/bin/env python3
"""Draw a reproducible sample of a grounding population, for estimating its error rate.

Some slices of the curation backlog are too large to review one by one and too
uniform to screen. The 856 EXACT + SEEDED records are the case in point: the
seeder matched the source label to the ontology label exactly, so the cohort
screens in `just report` — which look for a mismatch between those two — find
nothing there by construction.

The question worth answering about such a slice is not "which ones are wrong"
but "is the rate high enough to justify reading 856 records". That is a
sampling question, and a sample only means anything if someone else can draw
the same one, so the seed is fixed and committed rather than left to the clock.

Usage:
    python3 scripts/sample_groundings.py                    # the default EXACT slice
    python3 scripts/sample_groundings.py --grounding NARROW --size 60
"""

from __future__ import annotations

import argparse
import random
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
HABITATS_DIR = REPO_ROOT / "data" / "habitats"

# Fixed so the sample is a property of the corpus rather than of when it ran.
# Changing it invalidates any error rate previously reported against it.
DEFAULT_SEED = 20260814


def population(grounding: str, reviewed: bool) -> list[dict]:
    found = []
    for path in sorted(HABITATS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or doc.get("grounding_status") != grounding:
            continue
        if not reviewed and doc.get("mapping_status") == "REVIEWED":
            continue
        found.append(doc)
    return found


def wilson(hits: int, n: int) -> tuple[float, float]:
    """95% Wilson score interval — usable at the small counts a sample gives,
    where the normal approximation puts the lower bound below zero."""
    if not n:
        return (0.0, 0.0)
    z, p = 1.96, hits / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grounding", default="EXACT")
    parser.add_argument("--size", type=int, default=40)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--include-reviewed", action="store_true")
    parser.add_argument("--found", type=int, help="Defects found, to report a rate.")
    args = parser.parse_args(argv)

    pool = population(args.grounding, args.include_reviewed)
    if not pool:
        raise SystemExit(f"no {args.grounding} records to sample")
    size = min(args.size, len(pool))
    random.seed(args.seed)
    sample = random.sample(pool, size)

    print(f"population: {len(pool)} {args.grounding} records "
          f"({'incl.' if args.include_reviewed else 'excl.'} reviewed)")
    print(f"sample: {size}, seed {args.seed}\n")
    for n, doc in enumerate(sorted(sample, key=lambda d: d.get("label", "").lower()), 1):
        attestation = (doc.get("source_attestations") or [{}])[0]
        print(f"{n:3d}. {attestation.get('source_label', '')[:24]:24s} -> "
              f"{doc.get('label', '')[:30]:30s} {doc['identifier'][:20]:20s} "
              f"{(attestation.get('source_path') or '')[:44]}")

    if args.found is not None:
        low, high = wilson(args.found, size)
        print(f"\n{args.found} of {size} judged wrong = {100 * args.found / size:.1f}%")
        print(f"95% Wilson interval: {100 * low:.1f}% to {100 * high:.1f}%")
        print(f"extrapolated to the population: {low * len(pool):.0f} to "
              f"{high * len(pool):.0f} of {len(pool)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
