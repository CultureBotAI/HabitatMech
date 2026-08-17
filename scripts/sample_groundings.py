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
import csv
import hashlib
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
HABITATS_DIR = REPO_ROOT / "data" / "habitats"

# Fixed so the sample is a property of the corpus rather than of when it ran.
# Changing it invalidates any error rate previously reported against it.
DEFAULT_SEED = 20260814
SAMPLES_DIR = REPO_ROOT / "curation" / "samples"


def class_swept_ids() -> set[str]:
    """Concepts decided by a class-level sweep — "no term matched by any lexical
    route" — which deliberately does NOT count as reviewed. They are the largest
    group nobody has read one by one, so they are worth sampling as a group."""
    path = REPO_ROOT / "curation" / "decisions.tsv"
    if not path.exists():
        return set()
    import csv as _csv
    with path.open(newline="", encoding="utf-8") as fh:
        return {
            r["identifier"] for r in _csv.DictReader(fh, delimiter="\t")
            if (r.get("review_depth") or "ITEM").strip().upper() == "CLASS"
        }


def non_habitat_screened() -> set[str]:
    """Swept concepts the non-habitat screen already flags.

    They are excluded from the UNSCREENED population because they are not the
    unknown: the screen has said something about them, and sampling a mixture of
    "already has evidence" and "has none" answers neither question. Needs a
    kg-microbe checkout; without one this is empty and the population falls back
    to every swept concept, which the caller is told.
    """
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    try:
        import habitat_report as report
    except ImportError:
        return set()
    if report._kg_microbe_ontologies() is None:
        return set()
    records = []
    for path in sorted(HABITATS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict):
            records.append((path, doc))
    return {row[4] for row in report._non_habitat_candidates(class_swept_ids(), records)}


def population(grounding: str, reviewed: bool) -> list[dict]:
    swept = set()
    if grounding in ("CLASS_SWEPT", "CLASS_SWEPT_UNSCREENED"):
        swept = class_swept_ids()
        if grounding == "CLASS_SWEPT_UNSCREENED":
            swept -= non_habitat_screened()
    found = []
    for path in sorted(HABITATS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            continue
        if grounding in ("CLASS_SWEPT", "CLASS_SWEPT_UNSCREENED"):
            if doc.get("identifier") not in swept:
                continue
        elif doc.get("grounding_status") != grounding:
            continue
        if not reviewed and doc.get("mapping_status") == "REVIEWED":
            continue
        found.append(doc)
    return found


def select(pool: list[dict], size: int, seed: int) -> list[dict]:
    """The `size` records with the lowest hash of (seed, identifier).

    Selecting by position — which is what random.sample does — makes the draw a
    function of the whole list, so removing one record permutes the entire
    sample. The population here IS the curation backlog, so it shrinks every
    time anyone acts on it: curating two records inside one PR moved it from 856
    to 854 and silently invalidated the sample that had just been judged (#71).

    Hashing the identifier instead gives the standard consistent-sampling
    property — a record's membership depends only on that record, so the draw
    survives the corpus changing around it.
    """
    keyed = sorted(
        pool,
        key=lambda d: hashlib.sha1(f"{seed}:{d['identifier']}".encode()).hexdigest(),
    )
    return keyed[:size]


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


# A verdict is prose — "ok — homonym risk (lung vs tooth alveolus) but PREGO
# named the CURIE itself" is a real one — so only the leading token is read, and
# the rest is the judgement's reasoning. Both vocabularies in use are accepted:
# the first sample said "ok" and the second "correct", and rewriting a committed
# verdict to normalise it would edit the evidence.
VERDICT_PASS = {"ok", "correct", "right", "good"}
VERDICT_FAIL = {"wrong", "bad", "incorrect", "defect", "error"}


def verdict_of(raw: str) -> str | None:
    """`pass`, `fail`, or None when the token is not one this knows.

    None rather than a default, because a rate computed over verdicts nobody
    parsed is worse than no rate: reading "ok" as a defect silently reported
    the EXACT slice as 100% wrong.
    """
    token = (raw or "").strip().lower().split()[0].strip("—-:,.") if (raw or "").strip() else ""
    if token in VERDICT_PASS:
        return "pass"
    if token in VERDICT_FAIL:
        return "fail"
    return None


def recorded_samples() -> list[dict]:
    """Every sample drawn, judged and committed under curation/samples/.

    A sample is only an argument if the draw and the verdicts are both on
    record: "we checked 40 and found none wrong" is unfalsifiable without the
    40. These files are what makes the rate in `just report` something a reader
    can audit rather than take on trust.

    Reports the CURRENT population, not the one at draw time. Hash-based
    selection means the sample stays valid as the population shrinks (#71), but
    the extrapolation has to be to the population now.
    """
    out = []
    if not SAMPLES_DIR.exists():
        return out
    for path in sorted(SAMPLES_DIR.glob("*.tsv")):
        grounding = path.stem.split("-")[0].upper()
        with path.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
        verdicts = [(r, verdict_of(r.get("verdict", ""))) for r in rows]
        judged = [r for r, v in verdicts if v is not None]
        wrong = [r for r, v in verdicts if v == "fail"]
        unparsed = [r for r, v in verdicts
                    if v is None and (r.get("verdict") or "").strip()]
        try:
            live = len(population(grounding, reviewed=False))
        except Exception:
            live = 0
        out.append({
            "file": path.name,
            "grounding": grounding,
            "drawn": len(rows),
            "judged": len(judged),
            "wrong": len(wrong),
            "unparsed": len(unparsed),
            "population": live,
            "interval": wilson(len(wrong), len(judged)) if judged else (0.0, 0.0),
        })
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grounding", default="EXACT",
                        help="A grounding_status; CLASS_SWEPT for the concepts a class-level "
                             "sweep decided without anyone reading them; or "
                             "CLASS_SWEPT_UNSCREENED for those of them the non-habitat screen "
                             "does not already flag, which is the genuinely unassessed set.")
    parser.add_argument("--size", type=int, default=40)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--include-reviewed", action="store_true")
    parser.add_argument("--found", type=int, help="Defects found, to report a rate.")
    parser.add_argument("--record", action="store_true",
                        help="Write the drawn sample to curation/samples/ so the rate "
                             "reported against it stays auditable.")
    args = parser.parse_args(argv)

    pool = population(args.grounding, args.include_reviewed)
    if not pool:
        raise SystemExit(f"no {args.grounding} records to sample")
    size = min(args.size, len(pool))
    sample = select(pool, size, args.seed)

    print(f"population: {len(pool)} {args.grounding} records "
          f"({'incl.' if args.include_reviewed else 'excl.'} reviewed)")
    print(f"sample: {size}, seed {args.seed}\n")
    for n, doc in enumerate(sorted(sample, key=lambda d: d.get("label", "").lower()), 1):
        attestation = (doc.get("source_attestations") or [{}])[0]
        print(f"{n:3d}. {attestation.get('source_label', '')[:24]:24s} -> "
              f"{doc.get('label', '')[:30]:30s} {doc['identifier'][:20]:20s} "
              f"{(attestation.get('source_path') or '')[:44]}")

    if args.record:
        SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
        out = SAMPLES_DIR / f"{args.grounding.lower()}-{args.seed}.tsv"
        with out.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
            writer.writerow(["identifier", "label", "source_label", "source_path", "verdict"])
            for doc in sorted(sample, key=lambda d: d["identifier"]):
                a = (doc.get("source_attestations") or [{}])[0]
                writer.writerow([doc["identifier"], doc.get("label", ""),
                                 a.get("source_label", ""), a.get("source_path", ""), ""])
        print(f"\nwrote {out.relative_to(REPO_ROOT)} — fill in `verdict` per row")

    if args.found is not None:
        low, high = wilson(args.found, size)
        print(f"\n{args.found} of {size} judged wrong = {100 * args.found / size:.1f}%")
        print(f"95% Wilson interval: {100 * low:.1f}% to {100 * high:.1f}%")
        print(f"extrapolated to the population: {low * len(pool):.0f} to "
              f"{high * len(pool):.0f} of {len(pool)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
