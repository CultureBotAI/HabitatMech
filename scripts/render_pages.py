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

# Where the site is served from, for absolute URLs in the sitemap.
SITE_BASE = "https://culturebotai.github.io/HabitatMech/pages/"

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
        (out_dir / "category" / f"{slugify(name)}.html").write_text(
            env.get_template("category.html").render(
                category=name,
                description=CATEGORY_BLURB.get(name, ""),
                records=sorted(items, key=lambda r: (-r["assertions"], r["label"])),
                root="../",
                stats=stats,
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
    listed += [f"category/{c['slug']}.html" for c in categories]
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

    # Remove pages for records that no longer exist. Curation splits records as
    # well as merging them, so the set shrinks too; without this the site keeps
    # serving a page for a habitat the corpus has dropped, and --check reports it
    # as orphaned forever. Same reason the seeder has --prune.
    written = {
        out_dir / "index.html", out_dir / "browse.html", out_dir / "term-requests.html",
        out_dir / "style.css", out_dir / ".nojekyll", out_dir / "sitemap.xml",
        out_dir / "robots.txt",
    }
    written |= {out_dir / "habitats" / f"{slug}.html" for slug in slug_of.values()}
    written |= {out_dir / "category" / f"{c['slug']}.html" for c in categories}
    pruned = 0
    for existing in sorted(out_dir.rglob("*")):
        if existing.is_file() and existing not in written:
            existing.unlink()
            pruned += 1

    print(f"rendered {len(records)} habitat pages, {len(categories)} categories, "
          f"{len(term_requests)} term requests"
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
