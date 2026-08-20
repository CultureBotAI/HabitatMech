#!/usr/bin/env python3
"""Fetch GOLD biosample ENVO triads, seeded from GOLD's own bulk export.

GOLD's API refuses an unfiltered query — every endpoint demands one of
studyGoldId, itsProposalId, organismGoldId, biosampleGoldId or apGoldId — and
the bulk Excel export at gold.jgi.doe.gov/download?mode=site_excel is broken
server-side: it declares ~239 MB and closes the connection early, at a different
point on each attempt (29 MB, 53 MB, 95 MB observed).

Enumeration was tried and abandoned: only 0.8% of proposal ids answer, and GOLD
returns 429 after roughly a dozen requests in four seconds, so a sweep would
spend a throttled budget on 404s. `--probe` still measures that, because the
number is the argument.

The route that works is `--studies`, seeded from data/raw/gold_studies.tsv:
GOLD's export says which 4,587 studies have a biosample on a path this corpus
holds, so every request hits something.

    study -> biosamples -> ENVO triad + ecosystem path

**Probe before you sweep.** GOLD has 63,802 studies and 244,653 biosamples
behind someone else's service. A full walk is tens of thousands of requests, and
running that to find out whether it was worth it is the wrong order. `--probe`
samples the id space and reports the density, the yield per hit and the
projected request count, for a few hundred requests. Read that number before
deciding, and if it is large, ask GOLD before running it rather than after.

Politeness is not optional here and is why this is deliberately slow:

* one worker by default, with a fixed delay between requests
* every response cached to disk, so a re-run costs nothing and a crash loses
  nothing
* 404 is a normal answer for a sparse id space, not an error, and is cached too
  so the same gap is never probed twice

Usage:
    python3 scripts/gold_enumerate.py --probe --sample 200
    python3 scripts/gold_enumerate.py --proposals 500000-510000
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE = REPO_ROOT / "build" / "gold_cache"
OUT = REPO_ROOT / "data" / "raw" / "gold_biosample_triads.tsv"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gold_api import API, _get, access_token  # noqa: E402

# One request every this many seconds, per worker. GOLD publishes no rate limit,
# so this is a guess made on the polite side: a public research service should
# not have to defend itself from us.
DELAY_SECONDS = 0.4

COLUMNS = [
    "biosample_gold_id", "study_gold_id", "ecosystem_path_id", "canonical_path",
    "envo_broad_scale", "envo_broad_label", "envo_local_scale", "envo_local_label",
    "envo_medium", "envo_medium_label", "habitat", "sample_collection_site",
    "host_name", "latitude", "longitude",
]


def normalise_curie(value: str | None) -> str:
    """GOLD writes ENVO_00000446; every other file in this repo writes
    ENVO:00000446. Forgetting this produces zero matches and no error."""
    return (value or "").replace("_", ":", 1) if value else ""


# Statuses that are an ANSWER and worth remembering. 404 belongs here: in a
# sparse id space it is the common reply and re-asking is pure waste. 429 and
# 5xx emphatically do not — caching a throttle would mark a study permanently
# empty, and a sweep would quietly return less data every time it was retried.
CACHEABLE = {200, 404}

# Backoff on 429. GOLD documents no rate limit; a dozen requests in four seconds
# was enough to trip one, so this waits rather than hammering through it.
THROTTLE_BACKOFF = (5, 20, 60)


def _fetch(url: str, headers: dict[str, str]) -> tuple[int, str]:
    """_get, but a network hiccup does not end a 4,587-request sweep.

    The first full run died 4,026 requests in on a single `TimeoutError` from an
    SSL read. Everything already fetched was safe in the cache, but an
    unretried transport error taking down the remaining 561 is a bug, not bad
    luck: over thousands of requests a slow response is certain, not possible.

    Returns 0 as the status when the transport never produced one, which the
    caller treats as uncacheable — an unanswered request must not be remembered
    as an answer.
    """
    for attempt in range(3):
        try:
            return _get(url, headers)
        except Exception:
            if attempt == 2:
                return 0, ""
            time.sleep(5 * (attempt + 1))
    return 0, ""


def cached_get(url: str, headers: dict[str, str], cache_key: str) -> tuple[int, str]:
    """A disk-cached GET that only caches answers, never throttles."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{hashlib.sha1(cache_key.encode()).hexdigest()}.json"
    if path.exists():
        blob = json.loads(path.read_text(encoding="utf-8"))
        return blob["status"], blob["body"]

    status, body = _fetch(url, headers)
    for wait in THROTTLE_BACKOFF:
        if status != 429:
            break
        time.sleep(wait)
        status, body = _fetch(url, headers)

    if status in CACHEABLE:
        path.write_text(json.dumps({"status": status, "body": body}), encoding="utf-8")
    time.sleep(DELAY_SECONDS)
    return status, body


def studies_for_proposal(proposal: int, headers: dict[str, str]) -> list[dict]:
    status, body = cached_get(f"{API}/studies?itsProposalId={proposal}", headers,
                              f"studies:{proposal}")
    if status != 200:
        return []
    data = json.loads(body)
    return data if isinstance(data, list) else [data]


def biosamples_for_study(study: str, headers: dict[str, str]) -> list[dict]:
    status, body = cached_get(f"{API}/biosamples?studyGoldId={study}", headers,
                              f"biosamples:{study}")
    if status != 200:
        return []
    data = json.loads(body)
    return data if isinstance(data, list) else [data]


def path_of(sample: dict) -> str:
    parts = [sample.get(k) for k in ("ecosystem", "ecosystemCategory", "ecosystemType",
                                     "ecosystemSubtype", "specificEcosystem")]
    return " > ".join(p for p in parts if p and p != "Unclassified")


def row_of(sample: dict, study: str) -> dict[str, str]:
    def term(field: str, part: str) -> str:
        value = (sample.get(field) or {}).get(part) or ""
        return normalise_curie(value) if part == "id" else value
    return {
        "biosample_gold_id": sample.get("biosampleGoldId") or "",
        "study_gold_id": study,
        "ecosystem_path_id": str(sample.get("ecosystemPathId") or ""),
        "canonical_path": path_of(sample),
        "envo_broad_scale": term("envoBroadScale", "id"),
        "envo_broad_label": term("envoBroadScale", "label"),
        "envo_local_scale": term("envoLocalScale", "id"),
        "envo_local_label": term("envoLocalScale", "label"),
        "envo_medium": term("envoMedium", "id"),
        "envo_medium_label": term("envoMedium", "label"),
        "habitat": sample.get("habitat") or "",
        "sample_collection_site": sample.get("sampleCollectionSite") or "",
        "host_name": sample.get("hostName") or "",
        "latitude": str(sample.get("latitude") or ""),
        "longitude": str(sample.get("longitude") or ""),
    }


def probe(headers: dict[str, str], sample_size: int, low: int, high: int, seed: int) -> None:
    """Sample the id space and report what a full sweep would cost.

    Reports the projection even when it is discouraging — the point is to find
    out before spending someone else's capacity, not to justify a sweep.
    """
    rng = random.Random(seed)
    ids = rng.sample(range(low, high), min(sample_size, high - low))
    hits, studies, samples, triads = 0, 0, 0, 0
    started = time.monotonic()
    for n, proposal in enumerate(ids, 1):
        found = studies_for_proposal(proposal, headers)
        if found:
            hits += 1
            studies += len(found)
            for study in found[:2]:  # cap: a probe should not become a sweep
                bs = biosamples_for_study(study.get("studyGoldId") or "", headers)
                samples += len(bs)
                triads += sum(
                    1 for b in bs
                    if all((b.get(k) or {}).get("id")
                           for k in ("envoBroadScale", "envoLocalScale", "envoMedium"))
                )
        if n % 25 == 0:
            print(f"    {n}/{len(ids)} probed, {hits} hit", flush=True)

    elapsed = time.monotonic() - started
    density = hits / len(ids) if ids else 0
    print(f"\n  probed {len(ids)} proposal ids in {low}-{high}, {elapsed:.0f}s")
    print(f"  density:            {hits}/{len(ids)} = {100 * density:.1f}% answer")
    print(f"  studies per hit:    {studies / hits:.1f}" if hits else "  studies per hit: n/a")
    print(f"  biosamples seen:    {samples}")
    print(f"  complete triads:    {triads}/{samples}" if samples else "  complete triads: n/a")
    if density:
        span = high - low
        projected = span + int(span * density * (studies / hits if hits else 0))
        print(f"\n  PROJECTED for the full {low}-{high} range:")
        print(f"    ~{projected:,} requests at {DELAY_SECONDS}s each "
              f"= ~{projected * DELAY_SECONDS / 3600:.1f} hours")
        print("    That is load on a public research service. If this number is large, "
              "ask GOLD before running it.")


def sweep_studies(headers: dict[str, str], limit: int | None) -> int:
    """Fetch triads for the studies GOLD's own export says are worth asking about.

    Enumeration was the wrong route — 0.8% of proposal ids answer, and GOLD
    returns 429 after roughly a dozen requests in four seconds. Seeding from the
    export removes both problems: every id exists, so nothing is wasted, and
    4,587 studies is small enough to be polite about.

    Resumable through the same on-disk cache as the probe, so an interrupted
    sweep costs nothing to restart and a 429 is survivable rather than fatal.
    """
    seed = REPO_ROOT / "data" / "raw" / "gold_studies.tsv"
    if not seed.exists():
        raise SystemExit(f"{seed.relative_to(REPO_ROOT)} not found — run "
                         "scripts/extract_gold_biosamples.py first")
    with seed.open(newline="", encoding="utf-8") as fh:
        studies = [r["study_gold_id"] for r in csv.DictReader(fh, delimiter="\t")]
    if limit:
        studies = studies[:limit]

    rows, seen, throttled = [], set(), 0
    for n, study in enumerate(studies, 1):
        for sample in biosamples_for_study(study, headers):
            key = sample.get("biosampleGoldId")
            if key and key not in seen:
                seen.add(key)
                rows.append(row_of(sample, study))
        if n % 25 == 0:
            triads = sum(1 for r in rows if r["envo_broad_scale"])
            print(f"    {n}/{len(studies)} studies, {len(rows)} biosamples, "
                  f"{triads} with a triad", flush=True)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: r["biosample_gold_id"]))
    triads = sum(1 for r in rows if r["envo_broad_scale"])
    print(f"\nwrote {OUT.relative_to(REPO_ROOT)}: {len(rows)} biosamples, "
          f"{triads} with a complete broad scale")
    if throttled:
        print(f"  {throttled} request(s) were throttled; re-run to fill the gaps")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", action="store_true",
                        help="sample the id space and project the cost. Do this first.")
    parser.add_argument("--sample", type=int, default=200, help="ids to probe")
    parser.add_argument("--range", default="500000-510000",
                        help="proposal id range, LOW-HIGH")
    parser.add_argument("--seed", type=int, default=20260820,
                        help="fixed, so a probe can be repeated and compared")
    parser.add_argument("--proposals", help="sweep this range instead of probing")
    parser.add_argument("--studies", action="store_true",
                        help="fetch triads for the studies in data/raw/gold_studies.tsv. "
                             "This is the real route: seeded from GOLD's own export, so "
                             "every request hits a study that exists.")
    parser.add_argument("--limit", type=int, help="stop after N studies")
    args = parser.parse_args(argv or sys.argv[1:])

    headers = {"Authorization": f"Bearer {access_token()}"}
    span = args.proposals or args.range
    low, _, high = span.partition("-")
    low, high = int(low), int(high)

    if args.studies:
        return sweep_studies(headers, args.limit)

    if args.probe or not args.proposals:
        probe(headers, args.sample, low, high, args.seed)
        return 0

    rows, seen = [], set()
    for proposal in range(low, high):
        for study in studies_for_proposal(proposal, headers):
            sid = study.get("studyGoldId") or ""
            for sample in biosamples_for_study(sid, headers):
                key = sample.get("biosampleGoldId")
                if key and key not in seen:
                    seen.add(key)
                    rows.append(row_of(sample, sid))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {OUT.relative_to(REPO_ROOT)}: {len(rows)} biosamples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
