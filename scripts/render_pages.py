#!/usr/bin/env python3
"""Render the browsable site under pages/ from data/habitats/.

A corpus of 3,000+ YAML files is not readable by anyone who is not already
running the tooling, which makes the curation backlog invisible to exactly the
people best placed to help with it — ontology curators. The site exists mainly
to publish two things: the records themselves, and the ENVO term-request list.

Generated, committed, and served from `main` at the repo root, matching the
sibling Mech repos. Regenerate with `just render`; CI checks the output is in
step with the corpus, the same way `verify-corpus` does for the records.

Usage:
    python3 scripts/render_pages.py
    python3 scripts/render_pages.py --out /tmp/site --check
"""

from __future__ import annotations

import argparse
import csv
import filecmp
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

REPO_ROOT = Path(__file__).resolve().parent.parent
HABITATS_DIR = REPO_ROOT / "data" / "habitats"
TEMPLATES_DIR = REPO_ROOT / "src" / "habitatmech" / "templates"
PAGES_DIR = REPO_ROOT / "pages"
DECISIONS_PATH = REPO_ROOT / "curation" / "decisions.tsv"
MANIFEST_PATH = REPO_ROOT / "data" / "raw" / "MANIFEST.yaml"

# Per-record taxon lists are capped in the extractor at 25; showing all of them
# on the page is fine, but the cap is worth naming where a reader sees it.
TAXA_SHOWN = 25

# Where the site is served from; the sitemap needs absolute URLs.
SITE_BASE = "https://culturebotai.github.io/HabitatMech/pages/"

# Rows per category page. 300 keeps the biggest category near 90 KB instead of
# 461 KB; the filter still searches the whole category via the JSON index.
CATEGORY_PAGE_SIZE = 300

# Where the site is served from, for absolute URLs in the sitemap.
SITE_BASE = "https://culturebotai.github.io/HabitatMech/pages/"

# Rows per category page. 300 keeps the biggest category near 90 KB instead of
# 461 KB; the filter still searches the whole category via the JSON index.
CATEGORY_PAGE_SIZE = 300

CATEGORY_BLURB = {
    "TERRESTRIAL": "Soils, sediments, subsurface, rock and other land environments.",
    "AQUATIC": "Marine, freshwater and other water-column or aquatic-sediment environments.",
    "AIR": "Atmospheric and aerosol environments.",
    "HOST_ASSOCIATED": "Habitats defined by a living host, including anatomical sites.",
    "ENGINEERED": "Built or managed environments: bioreactors, wastewater, industry.",
    "FOOD": "Food and beverage matrices, including fermented products.",
    "CLINICAL": "Clinical and diagnostic sample contexts.",
    "OTHER": "Records the category heuristic could not place.",
}

GROUNDING_MEANING = {
    "EXACT": "The identifier is an exact match for the source concept.",
    "CLOSE": "Close, but not exact and not cleanly broader or narrower.",
    "NARROW": "The identifier is narrower than the source concept.",
    "BROAD": "The identifier is broader — the best available term, losing specificity.",
    "UNGROUNDED": "No defensible ontology term; a minted identifier and a term-request candidate.",
    "NOT_APPLICABLE": "Not a habitat at all — a host taxon, a disease process, a quality.",
}

OBO_PREFIXES = {"ENVO", "UBERON", "FOODON", "BTO", "PO", "PATO", "CHEBI", "GO", "NCIT", "NCBITaxon"}


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-") or "unnamed"


def _trim_category_prefix(path: str, category: str) -> str:
    """Drop the leading path segment only when it restates the category.

    Trimming unconditionally looked like a free saving and was not: GOLD's top
    level (Environmental / Host-associated / Engineered) is a different axis
    from habitat_category, so 707 rows lost a branch the reader needs — on a
    page that says the path is shown precisely because the label is only its
    last step (#66).
    """
    head, sep, tail = path.partition(" > ")
    if not sep or not tail:
        return path
    return tail if head.upper().replace("-", "_").replace(" ", "_") == category else path


def _slice_labels() -> list[dict]:
    """Labels for the vendored ontology slice. Empty when it is absent, so the
    site still renders from a corpus alone."""
    path = REPO_ROOT / "data" / "raw" / "ontology_terms.tsv"
    if not path.exists():
        return []
    import csv as _csv
    with path.open(newline="", encoding="utf-8") as fh:
        return list(_csv.DictReader(fh, delimiter="\t"))


def term_iri(curie: str) -> str | None:
    prefix, _, local = curie.partition(":")
    if prefix in OBO_PREFIXES:
        return f"http://purl.obolibrary.org/obo/{prefix}_{local}"
    return None


def load_records() -> list[tuple[Path, dict]]:
    out = []
    for path in sorted(HABITATS_DIR.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        if isinstance(doc, dict):
            out.append((path, doc))
    return out


def load_decisions() -> dict[str, dict[str, str]]:
    if not DECISIONS_PATH.exists():
        return {}
    with DECISIONS_PATH.open(newline="", encoding="utf-8") as fh:
        return {r["identifier"]: r for r in csv.DictReader(fh, delimiter="\t")}


def extracted_at() -> str:
    if MANIFEST_PATH.exists():
        for line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines():
            if line.startswith("extracted_at:"):
                return line.split(":", 1)[1].strip().strip("'\"")[:10]
    return "an unrecorded date"


def build(out_dir: Path) -> None:
    records = load_records()
    if not records:
        raise SystemExit(f"no records under {HABITATS_DIR}; run `just seed-apply` first")
    decisions = load_decisions()

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    slug_of = {doc["identifier"]: slugify(f"{doc['label']}-{doc['identifier']}") for _, doc in records}
    label_of = {doc["identifier"]: doc["label"] for _, doc in records}
    # A cross-referenced term is usually NOT a record — that is what makes it a
    # cross-reference — so the corpus cannot name it. Falling back to the
    # vendored slice is the difference between "ENVO:00002204" and
    # "anthropogenic contamination feature" on the page.
    for _row in _slice_labels():
        label_of.setdefault(_row["term_id"], _row["label"])

    by_category: dict[str, list[dict]] = defaultdict(list)
    grounding_counts: Counter = Counter()
    status_counts: Counter = Counter()
    multi_source = 0
    term_requests: list[dict] = []
    swept = 0

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "habitats").mkdir(exist_ok=True)
    (out_dir / "category").mkdir(exist_ok=True)

    # First pass: corpus-wide counts. Record pages are rendered in the second
    # pass and previously read `stats` before it was filled, so their footer
    # printed " of 3192 records are machine-generated" with the count missing —
    # on exactly the pages where a reader is looking at one such record (#31).
    stats = {
        "total": len(records),
        "extracted_at": extracted_at(),
        "reviewed": sum(1 for _, d in records if d.get("mapping_status") == "REVIEWED"),
        "seeded": sum(1 for _, d in records if d.get("mapping_status") == "SEEDED"),
    }

    for path, doc in records:
        identifier = doc["identifier"]
        attestations = doc.get("source_attestations") or []
        sources = sorted({a["source"] for a in attestations})
        assertions = sum(a.get("assertion_count") or 0 for a in attestations)
        grounding_counts[doc.get("grounding_status", "?")] += 1
        status_counts[doc.get("mapping_status", "?")] += 1
        if len(sources) > 1:
            multi_source += 1

        taxa = doc.get("characteristic_taxa") or []
        record = {
            "identifier": identifier,
            "label": doc["label"],
            "iri": term_iri(identifier),
            "definition": doc.get("definition"),
            "definition_source": doc.get("definition_source"),
            "category": doc.get("habitat_category", "OTHER"),
            "category_slug": slugify(doc.get("habitat_category", "OTHER")),
            "grounding": doc.get("grounding_status", "?"),
            "status": doc.get("mapping_status", "?"),
            "sources": sources,
            "attestations": attestations,
            "parameters": doc.get("environmental_parameters") or [],
            "synonyms": [
                {"text": s["synonym_text"], "source": s.get("source", "")}
                for s in (doc.get("synonyms") or [])
            ],
            "parents": [
                {
                    "id": p,
                    "label": label_of.get(p, p),
                    "href": f"../habitats/{slug_of[p]}.html" if p in slug_of else term_iri(p),
                }
                for p in (doc.get("parent_habitats") or [])
            ],
            # Terms upstream linked to this concept without this repo asserting
            # they are the same thing or that one is broader (#99). 48 records
            # carry one and none of them reached the page before.
            "xrefs": [
                {
                    "id": x,
                    "label": label_of.get(x, ""),
                    "href": f"../habitats/{slug_of[x]}.html" if x in slug_of else term_iri(x),
                }
                for x in (doc.get("xrefs") or [])
            ],
            "taxa": [
                {
                    "id": t["taxon_id"],
                    "label": t.get("taxon_label"),
                    "source": t.get("source", ""),
                    "rank": t.get("rank"),
                    "pool": t.get("candidate_pool"),
                    "corroborated": t.get("corroborated_by") or [],
                }
                for t in taxa[:TAXA_SHOWN]
            ],
            "taxa_total": len(taxa),
            "taxa_truncated": len(taxa) > TAXA_SHOWN,
            # Everything except the seed event: a curator's decisions, which
            # are the part of the history a reader cannot get anywhere else.
            # decisions.tsv is a seeder input, not something the site serves,
            # so before #94 a curated grounding was indistinguishable from a
            # machine-generated one on the page.
            "decisions": [
                {
                    "action": e.get("action", ""),
                    "curator": e.get("curator", ""),
                    "date": (e.get("timestamp") or "")[:10],
                    "changes": e.get("changes", "").replace("[CLASS-level] ", ""),
                    "class_level": "[CLASS-level]" in (e.get("changes") or ""),
                }
                for e in (doc.get("curation_history") or [])
                if e.get("action") != "SEEDED_FROM_SOURCES"
            ],
            "repo_path": str(path.relative_to(REPO_ROOT)),
        }

        (out_dir / "habitats" / f"{slug_of[identifier]}.html").write_text(
            env.get_template("habitat.html").render(r=record, root="../", stats=stats),
            encoding="utf-8",
        )

        by_category[record["category"]].append(
            {
                "label": doc["label"],
                "identifier": identifier,
                "slug": slug_of[identifier],
                "grounding": record["grounding"],
                "path": (
                    attestations[0].get("source_path")
                    or attestations[0].get("source_label", "")
                    if attestations else ""
                ),
                # Same path with the category prefix trimmed. Every row on a
                # category page repeats it — "Host-associated > " 1643 times —
                # and the page it is on already says which category this is
                # (#34). The untrimmed `path` still feeds the search key.
                "short_path": _trim_category_prefix(
                    (
                        attestations[0].get("source_path")
                        or attestations[0].get("source_label", "")
                        if attestations else ""
                    ),
                    record["category"],
                ),
                "assertions": assertions,
                "sources": sources,
            }
        )

        # The term-request list is the individually-examined ungrounded records
        # only. The bulk-swept ones are candidates for it, not members, and
        # conflating them would send curators a list mostly nobody has read.
        if doc.get("grounding_status") == "UNGROUNDED":
            decision = decisions.get(identifier, {})
            depth = (decision.get("review_depth") or "ITEM").upper()
            if doc.get("mapping_status") == "REVIEWED" and depth == "ITEM":
                term_requests.append(
                    {
                        "label": doc["label"],
                        "slug": slug_of[identifier],
                        "assertions": assertions,
                        "sources": sources,
                        "note": decision.get("notes", "")[:220],
                    }
                )
            else:
                swept += 1

    stats.update(
        {
            "grounded": sum(
                v for k, v in grounding_counts.items()
                if k in ("EXACT", "CLOSE", "NARROW", "BROAD")
            ),
            "multi_source": multi_source,
            "term_requests": len(term_requests),
        }
    )
    assert stats["seeded"] == status_counts.get("SEEDED", 0)

    categories = []
    category_pages: list[str] = []
    for name, items in sorted(by_category.items(), key=lambda kv: -len(kv[1])):
        categories.append(
            {
                "label": name,
                "slug": slugify(name),
                "count": len(items),
                "pct": round(100 * len(items) / len(records)),
                "grounded": sum(1 for i in items if i["grounding"] not in ("UNGROUNDED", "NOT_APPLICABLE")),
                "description": CATEGORY_BLURB.get(name, ""),
            }
        )
        ordered = sorted(items, key=lambda r: (-r["assertions"], r["label"]))
        slug = slugify(name)
        # Paginated because 99% of a category page is its table body, and the
        # biggest was 1641 rows in 461 KB — the likeliest first click from
        # Browse, and by far the heaviest page on the site (#34).
        chunks = [ordered[i:i + CATEGORY_PAGE_SIZE]
                  for i in range(0, len(ordered), CATEGORY_PAGE_SIZE)] or [[]]
        pager = [
            {"n": n, "href": f"{slug}.html" if n == 1 else f"{slug}-{n}.html"}
            for n in range(1, len(chunks) + 1)
        ]
        for n, chunk in enumerate(chunks, start=1):
            target = out_dir / "category" / (f"{slug}.html" if n == 1 else f"{slug}-{n}.html")
            target.write_text(
                env.get_template("category.html").render(
                    category=name,
                    description=CATEGORY_BLURB.get(name, ""),
                    records=chunk,
                    total=len(ordered),
                    page=n,
                    pager=pager if len(pager) > 1 else [],
                    index_url=f"{slug}.json",
                    root="../",
                    stats=stats,
                ),
                encoding="utf-8",
            )
            category_pages.append(f"category/{target.name}")
        # A compact index so the filter can still search the WHOLE category
        # rather than only the page in front of you. Fetched on the first
        # keystroke, not on load, so it costs nothing to a reader who browses.
        (out_dir / "category" / f"{slug}.json").write_text(
            json.dumps(
                [[r["label"], r["slug"], r["short_path"], r["grounding"],
                  r["assertions"], ", ".join(r["sources"])] for r in ordered],
                separators=(",", ":"), ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    groundings = [
        {"name": name, "count": count, "meaning": GROUNDING_MEANING.get(name, "")}
        for name, count in grounding_counts.most_common()
    ]

    (out_dir / "index.html").write_text(
        env.get_template("index.html").render(
            stats=stats, categories=categories, groundings=groundings, root=""
        ),
        encoding="utf-8",
    )
    (out_dir / "browse.html").write_text(
        env.get_template("browse.html").render(stats=stats, categories=categories, root=""),
        encoding="utf-8",
    )
    (out_dir / "term-requests.html").write_text(
        env.get_template("term_requests.html").render(
            requests=sorted(term_requests, key=lambda r: -r["assertions"]),
            swept=swept,
            stats=stats,
            root="",
        ),
        encoding="utf-8",
    )
    shutil.copyfile(TEMPLATES_DIR / "style.css", out_dir / "style.css")
    # Without this, Pages runs Jekyll over the site and silently drops any path
    # beginning with an underscore — a 404 rather than a visible error. Slugs
    # come from habitat labels, so that is not guaranteed to stay impossible
    # (#32). Written by the renderer so it is reproducible like everything else.
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")

    # A sitemap matters more here than for a typical project site: the point of
    # publishing is that ontology curators find the term requests and the record
    # pages, and every record page is otherwise reachable only by following a
    # category link — three clicks from the root, with no machine-readable index
    # of the deepest and most numerous content (#36).
    listed = ["index.html", "browse.html", "term-requests.html"]
    listed += category_pages
    listed += [f"habitats/{slug}.html" for slug in sorted(slug_of.values())]
    urls = "\n".join(f"  <url><loc>{SITE_BASE}{page}</loc></url>" for page in listed)
    (out_dir / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n",
        encoding="utf-8",
    )
    (out_dir / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_BASE}sitemap.xml\n", encoding="utf-8"
    )

    # Redirect stubs for records curation retired. A record page is named
    # slugify(label + identifier), so improving either moves the URL — which is
    # most of what curation does. Without these, every improvement 404s a
    # published address and a content-hashed identifier stops being citable
    # (#54). data/habitats/RETIRED.tsv is rebuilt by `just redirects`.
    retired_written: set[Path] = set()
    retired_path = REPO_ROOT / "data" / "habitats" / "RETIRED.tsv"
    if retired_path.exists():
        with retired_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                targets = [
                    {"identifier": t, "label": label_of.get(t, t), "slug": slug_of[t]}
                    for t in row["current_identifiers"].split("|")
                    if t in slug_of
                ]
                if not targets:
                    continue
                if row["retired_slug"] in slug_of.values():
                    # A retired slug that a live record now uses. Overwriting it
                    # would replace a real habitat with a redirect away from
                    # itself; the live record wins and the stub is dropped.
                    continue
                stub = out_dir / "habitats" / f"{row['retired_slug']}.html"
                stub.write_text(
                    env.get_template("redirect.html").render(
                        r={
                            "retired_identifier": row["retired_identifier"],
                            "retired_label": row.get("retired_label") or row["retired_identifier"],
                            "resolved_by": row["resolved_by"],
                            "targets": targets,
                        },
                        root="../", site_base=SITE_BASE, stats=stats,
                    ),
                    encoding="utf-8",
                )
                retired_written.add(stub)

    (out_dir / "404.html").write_text(
        env.get_template("not_found.html").render(root="", stats=stats),
        encoding="utf-8",
    )

    # Remove pages for records that no longer exist. Curation splits records as
    # well as merging them, so the set shrinks too; without this the site keeps
    # serving a page for a habitat the corpus has dropped, and --check reports it
    # as orphaned forever. Same reason the seeder has --prune.
    written = {
        out_dir / "index.html", out_dir / "browse.html", out_dir / "term-requests.html",
        out_dir / "style.css", out_dir / ".nojekyll", out_dir / "sitemap.xml",
        out_dir / "robots.txt", out_dir / "404.html",
    }
    written |= retired_written
    written |= {out_dir / "habitats" / f"{slug}.html" for slug in slug_of.values()}
    written |= {out_dir / name for name in category_pages}
    written |= {out_dir / "category" / f"{c['slug']}.json" for c in categories}
    pruned = 0
    for existing in sorted(out_dir.rglob("*")):
        if existing.is_file() and existing not in written:
            existing.unlink()
            pruned += 1

    print(f"rendered {len(records)} habitat pages, {len(retired_written)} redirect stubs, "
          f"{len(categories)} categories, {len(term_requests)} term requests"
          + (f", pruned {pruned} stale" if pruned else "")
          + f" -> {out_dir}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Render to a temp dir and fail if pages/ differs — the site is "
        "committed, so it can go stale against the corpus exactly as records "
        "could go stale against data/raw/.",
    )
    args = parser.parse_args(argv)

    if not args.check:
        build(args.out)
        return 0

    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "site"
        build(target)
        stale = []
        for rendered in sorted(target.rglob("*")):
            if rendered.is_dir():
                continue
            committed = PAGES_DIR / rendered.relative_to(target)
            if not committed.exists() or not filecmp.cmp(rendered, committed, shallow=False):
                stale.append(str(rendered.relative_to(target)))
        extra = [
            str(p.relative_to(PAGES_DIR))
            for p in sorted(PAGES_DIR.rglob("*"))
            if p.is_file() and not (target / p.relative_to(PAGES_DIR)).exists()
        ]
        if stale or extra:
            print(f"pages/ is stale: {len(stale)} differing, {len(extra)} orphaned", file=sys.stderr)
            for name in (stale + extra)[:10]:
                print(f"  {name}", file=sys.stderr)
            print("\nRegenerate with `just render`.", file=sys.stderr)
            return 1
        print("pages/ is in step with the corpus")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
