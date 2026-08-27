#!/usr/bin/env python3
"""Rebuild data/habitats/RETIRED.tsv — the map from dead record URLs to live ones.

A record page is named ``slugify(f"{label}-{identifier}")``, so the URL moves
whenever a curator improves either. That is most of what curation *does*:
re-grounding a concept changes its identifier, and adopting the ontology's own
label changes its label. 43 published URLs had already 404'd across five merges
before this existed, and the rate rises with the curation backlog (#54).

That undercuts the point of a content-hashed identifier. A record advertised as
stable and citable, whose URL dies the first time someone improves its
grounding, is not citable.

This walks git history to recover them:

* every ``pages/habitats/*.html`` that has ever existed on the branch and does
  not exist now is a dead URL;
* its identifier comes from the page's own meta description;
* the target is that identifier's current record if it still has one — the
  common case, a pure label change — and otherwise the record that inherited
  its *source concepts*, which is what a merge actually does. Source ids
  (``gold.ecosystem:5826``, ``bacdive.isolation_source:nectar``) are stable
  upstream keys, so they survive the merge that the identifier did not.

Re-run after a merge that retires records. `just redirects`.

Usage:
    python3 scripts/build_redirects.py            # rewrite RETIRED.tsv
    python3 scripts/build_redirects.py --check    # fail if it is out of date
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from render_pages import slugify  # noqa: E402

HABITATS_DIR = REPO_ROOT / "data" / "habitats"
RETIRED_PATH = HABITATS_DIR / "RETIRED.tsv"
COLUMNS = ["retired_slug", "retired_identifier", "retired_label",
           "current_identifiers", "resolved_by"]

# Retraction is a curation decision, so it lives with the other ones rather
# than in the generated map it edits. Same shape as
# curation/term_requests_excluded.tsv: the key, who decided, and why.
RETRACTED_PATH = REPO_ROOT / "curation" / "redirects_retracted.tsv"
RETRACTED_COLUMNS = ["retired_slug", "curator", "date", "why_retracted"]
_OVERFLOW = "_extra_fields"

# The page's meta description reads "{label} ({identifier}): a microbial
# habitat ...". Anchoring on the "): " is what makes this unambiguous when the
# label has parentheses of its own — 37 records do, and a leading [^"(]* would
# capture "MNF" out of "Mixotrophic (MNF)" instead of the identifier (#60).
_META_DESC = re.compile(r'<meta name="description" content="([^"]*)"')
_DESC_ID = re.compile(r"\(([^()]+)\):\s")
_CURIE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$")


def git(*args: str, allow_failure: bool = False) -> str:
    """Run git, and fail loudly rather than returning nothing.

    This used to return `""` on any non-zero exit, which every caller here reads
    as "there is nothing at this path" — so a broken git call and a legitimately
    absent file were the same answer. Simulating a failing `git show` while
    leaving the rest working built **34 rows instead of 138**, silently: the two
    blob reads feed 104 of the map's redirects, `just redirects` would have
    written the short list, and `just render` would then have pruned 104
    published record URLs into 404s (#176).

    Absence is a real answer for exactly one question — "did this path exist at
    this commit" — and `blob_at` asks it, with `allow_failure`. Everything else,
    and every blob read, is an error.
    """
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        capture_output=True, text=True, check=False,
    )
    if result.returncode != 0 and not allow_failure:
        raise SystemExit(
            f"git {' '.join(args)} failed with exit {result.returncode}: "
            f"{result.stderr.strip() or '(no stderr)'}"
        )
    return result.stdout if result.returncode == 0 else ""


def blob_at(commit: str, path: str) -> str | None:
    """A file's content at `commit`, or None if it did not exist there.

    Two legitimate absences, both of which used to be indistinguishable from a
    broken git call: `git log -- path` lists the commit that *deleted* a path as
    well as the ones that wrote it, and `<commit>^` does not resolve when
    `<commit>` is the root.

    `ls-tree` covers both — it exits 0 with no output for a path absent from a
    real tree, and non-zero for a revision that does not resolve — so it is the
    one probe allowed to fail quietly. The `show` that follows is not: by then
    the blob is known to be there, so a failure is a failure (#176).
    """
    if not git("ls-tree", "--name-only", commit, "--", path,
               allow_failure=True).strip():
        return None
    return git("show", f"{commit}:{path}")


def ever_published_slugs() -> set[str]:
    """Every page name `pages/habitats/` has ever contained.

    Listed per commit rather than inferred from deletions: a retired page is
    replaced in place by its own stub, so a deletion-based walk goes blind as
    soon as the stub lands. Used only to answer "was this URL ever real" — a
    redirect for an address nobody could have linked to is noise.
    """
    found: set[str] = set()
    for commit in git("log", "--format=%H", "--", "pages/habitats").splitlines():
        commit = commit.strip()
        if not commit:
            continue
        for path in git("ls-tree", "-r", "--name-only", commit,
                        "--", "pages/habitats").splitlines():
            if path.endswith(".html"):
                found.add(Path(path).stem)
    return found


def retired_map_history() -> dict[str, dict[str, str]]:
    """Newest committed row for every slug ever recorded in RETIRED.tsv.

    A redirect is itself published state. Once a label change records an old
    URL, a later merge must carry that URL forward even though the deleted
    record now contains only the newer label. Reading all committed map
    versions makes the history append-only without making the working file an
    input to its own generation.
    """
    found: dict[str, dict[str, str]] = {}
    relative = str(RETIRED_PATH.relative_to(REPO_ROOT))
    for commit in git("log", "--format=%H", "--", relative).splitlines():
        blob = blob_at(commit, relative)
        if not blob:
            continue
        for row in csv.DictReader(io.StringIO(blob), delimiter="\t"):
            slug = (row.get("retired_slug") or "").strip()
            if slug:
                found.setdefault(slug, row)
    return found


def _shown(path: Path) -> str:
    """A path for an error message, relative to the repo when it is inside it.

    `relative_to` RAISES for a path that is not, so composing a message with it
    is a way for the error path itself to die before it can say anything — which
    is how three of the retraction tests first failed, on the diagnostic rather
    than on the thing being diagnosed.
    """
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def load_retractions() -> dict[str, dict[str, str]]:
    """Redirects a curator has withdrawn, keyed by slug.

    A redirect is published state, and the generator had no way to unpublish
    one. Deleting a row from RETIRED.tsv does not retract it: the rebuild reads
    HEAD, HEAD still has the row, and the row comes straight back — `--check`
    then reports the hand-edited file as stale and regenerating restores it.
    The only way through was to commit the deletion first, while `--check` was
    failing, and regenerate afterwards: a two-step nobody would guess and
    nothing documented (#178).

    So retraction is stated where every other curation decision is, with a
    curator and a reason, and subtracted from the map at the end of `build`.
    Unpublishing a citable URL should leave a record of who did it and why.
    """
    if not RETRACTED_PATH.exists():
        return {}
    with RETRACTED_PATH.open(newline="", encoding="utf-8") as fh:
        # restkey, so a row with more fields than the header is visible. A tab
        # anywhere in why_retracted otherwise sent the tail of the reason to
        # DictReader's unnamed overflow key and truncated the audit record
        # silently — the URL unpublished, the stated justification a fragment
        # (#195). A tab in prose is what a spreadsheet paste produces.
        reader = csv.DictReader(fh, delimiter="\t", restkey=_OVERFLOW)
        missing = set(RETRACTED_COLUMNS) - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(
                f"{_shown(RETRACTED_PATH)} is missing "
                f"column(s): {', '.join(sorted(missing))}"
            )
        found: dict[str, dict[str, str]] = {}
        for line, row in enumerate(reader, start=2):
            # First, before anything reads row.values(): the overflow key holds
            # a LIST, not a string, so every later check would have to guard
            # against it.
            if row.pop(_OVERFLOW, None):
                raise SystemExit(
                    f"{_shown(RETRACTED_PATH)} line {line}: more fields than "
                    f"columns, so a value contains a tab and has been "
                    f"truncated at it; check why_retracted"
                )
            slug = (row.get("retired_slug") or "").strip()
            if not slug and not any((v or "").strip() for v in row.values()):
                continue  # a blank separator line, not a retraction
            if not slug:
                raise SystemExit(
                    f"{_shown(RETRACTED_PATH)} line {line}: a retraction with "
                    "no retired_slug names no URL; it would be skipped silently"
                )
            for column in ("curator", "date", "why_retracted"):
                if not (row.get(column) or "").strip():
                    raise SystemExit(
                        f"{_shown(RETRACTED_PATH)} line {line}: "
                        f"retracting {slug!r} needs a {column}"
                    )
            if slug in found:
                raise SystemExit(
                    f"{_shown(RETRACTED_PATH)} line {line}: "
                    f"{slug!r} is retracted twice"
                )
            found[slug] = row
    return found


def committed_redirect_slugs() -> set[str]:
    """Redirect stubs published by the branch's current committed site.

    A redirect that is still live in HEAD is active state the next generation
    must carry forward. Absence from HEAD is *not* a retraction the working
    tree can express: HEAD is committed history, so deleting a row from the
    working file changes nothing here and the row returns on the next rebuild.
    Withdrawing a published redirect goes through `load_retractions` (#178).

    Read from HEAD's copy of the map rather than by recognising a rendered stub.
    Recognising one meant grepping the committed pages for the literal
    "has moved — HabitatMech", which is a second copy of `redirect.html`'s title
    block — and rewording that title dropped the carry-forward silently: 138 rows
    became 137, losing the one URL #159 exists to save, with `just redirects`
    writing the smaller file and `just render` then pruning the stub (#162).

    The map is the same answer without the coupling. `render_pages` generates
    one stub per row and its --check gate keeps the two in step, so HEAD's rows
    *are* HEAD's stubs — verified equal at 138/138 when this replaced the grep.
    HEAD's copy, not the working file, so the map still cannot be an input to
    its own generation.
    """
    blob = blob_at("HEAD", str(RETIRED_PATH.relative_to(REPO_ROOT)))
    if blob is None:
        # No committed map yet: a first run, or a fresh branch that has never
        # retired a URL. Nothing to carry forward, which is not an error — and
        # `blob_at` distinguishes that from a `git show` that failed (#176).
        return set()
    reader = csv.DictReader(io.StringIO(blob), delimiter="\t")
    if "retired_slug" not in (reader.fieldnames or []):
        raise SystemExit(
            f"HEAD:{RETIRED_PATH.relative_to(REPO_ROOT)} has no retired_slug "
            "column; refusing to rebuild the map from an unreadable predecessor"
        )
    return {
        slug for row in reader if (slug := (row.get("retired_slug") or "").strip())
    }


def retired_record_details() -> tuple[dict[str, set[str]], dict[str, str]]:
    """Every retired record's identifier -> the source ids it carried.

    Source ids are upstream keys (``gold.ecosystem:5826``), so they survive the
    merge that the record identifier did not — they are what links a dead record
    to the live one that absorbed it.

    Built in a single pass over the deletions rather than by searching history
    per identifier: the corpus is 3200 records over dozens of commits, and the
    naive form is thousands of `git show` calls.
    """
    found: dict[str, set[str]] = {}
    labels: dict[str, str] = {}
    commit = ""
    for line in git("log", "--diff-filter=DR", "--name-status", "--format=%H",
                    "--", "data/habitats").splitlines():
        if line and "\t" not in line:
            commit = line.strip()
            continue
        parts = line.split("\t")
        if len(parts) < 2 or not commit or not parts[1].endswith(".yaml"):
            continue
        blob = blob_at(f"{commit}^", parts[1])
        if not blob:
            continue
        try:
            doc = yaml.safe_load(blob)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict) or "identifier" not in doc:
            continue
        source_ids = {
            a.get("source_id") for a in (doc.get("source_attestations") or [])
            if a.get("source_id")
        }
        # Latest wins: `git log` is newest-first, so the first sighting of an
        # identifier is the state it was in when it was retired.
        found.setdefault(doc["identifier"], source_ids)
        if doc.get("label"):
            labels.setdefault(doc["identifier"], doc["label"])
    return found, labels


def slug_for(doc: dict) -> str:
    """The page name the renderer gives this record. Must stay in step with
    render_pages, which is why it imports that module's slugify rather than
    reimplementing it."""
    return slugify(f"{doc['label']}-{doc['identifier']}")


def load_corpus() -> tuple[dict[str, dict], dict[str, str]]:
    """(identifier -> doc, source_id -> identifier) over the live corpus."""
    by_id: dict[str, dict] = {}
    by_source: dict[str, str] = {}
    for path in sorted(HABITATS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or "identifier" not in doc:
            continue
        by_id[doc["identifier"]] = doc
        for attestation in doc.get("source_attestations") or []:
            source_id = attestation.get("source_id")
            if source_id:
                by_source.setdefault(source_id, doc["identifier"])
    return by_id, by_source


def build() -> list[dict[str, str]]:
    by_id, by_source = load_corpus()
    retired_sources, retired_labels = retired_record_details()
    live_slugs = {slug_for(doc) for doc in by_id.values()}
    published = ever_published_slugs()
    retracted = load_retractions()
    # A slug that was never a real page cannot have been redirected, so it is a
    # typo rather than a retraction. Checked against every page the branch has
    # ever held, not against this run's rows: once a retraction takes effect the
    # slug stops being generated, and a tombstone that failed the moment it
    # started working would be worse than no tombstone at all.
    unknown = sorted(slug for slug in retracted if slug not in published)
    if unknown:
        raise SystemExit(
            f"{_shown(RETRACTED_PATH)} retracts slug(s) that "
            f"pages/habitats has never contained: {', '.join(unknown)}"
        )
    # A live record's own page passes the check above — `published` includes
    # pages that still exist — but `build` only ever emits slugs that are NOT
    # live, so no row can match one. That is a curator naming the new URL
    # instead of the old one, presenting as a successful retraction (#188).
    alive = sorted(slug for slug in retracted if slug in live_slugs)
    if alive:
        raise SystemExit(
            f"{_shown(RETRACTED_PATH)} retracts slug(s) that are a live "
            f"record's own page, so no redirect exists to withdraw: "
            f"{', '.join(alive)}"
        )
    rows: list[dict[str, str]] = []
    # Derived from RECORD history, not page history. A retired page is replaced
    # in place by its own redirect stub, so git logs a modification rather than
    # a deletion and any page-based detection stops seeing it the moment the
    # stub is committed — the map erased itself one release after being built.
    # Records are never replaced that way, and they carry both halves of the
    # page name.
    # Label changes need their own signal. PATHS.tsv deliberately pins a
    # record's FILENAME so it survives re-labelling, so a label change is an
    # in-place edit that record history cannot see — but the page name embeds
    # the label, so the URL moves anyway. Any published slug that ends in a live
    # record's identifier but is not its current slug is one of those.
    for identifier, doc in sorted(by_id.items()):
        suffix = "-" + slugify(identifier)
        current = slug_for(doc)
        for slug in sorted(published):
            if slug != current and slug.endswith(suffix) and slug not in live_slugs:
                rows.append({
                    "retired_slug": slug, "retired_identifier": identifier,
                    "retired_label": doc["label"],
                    "current_identifiers": identifier, "resolved_by": "label_changed",
                })

    for identifier, label in sorted(retired_labels.items()):
        slug = slugify(f"{label}-{identifier}")
        if slug in live_slugs or slug not in published:
            continue
        if identifier in by_id:
            # The record is alive; only its label moved. Nothing to look up.
            rows.append({
                "retired_slug": slug, "retired_identifier": identifier,
                "retired_label": retired_labels.get(identifier, by_id[identifier]["label"]),
                "current_identifiers": identifier, "resolved_by": "label_changed",
            })
            continue
        # The identifier is gone, so the concept merged or was re-grounded.
        # Follow its source concepts to whatever absorbed them.
        landed = sorted({
            by_source[s] for s in retired_sources.get(identifier, ()) if s in by_source
        })
        if not landed:
            continue
        # A retired record can have SPLIT rather than merged: NCIT:C17649 "Other"
        # held both Invertebrates-Other and Rodentia-Other, and curating it sent
        # them to different records. There is no single right target then, and
        # picking the most common one silently sends half the readers to the
        # wrong habitat — so all of them are kept and the stub offers a choice.
        rows.append({
            "retired_slug": slug, "retired_identifier": identifier,
            "retired_label": retired_labels.get(identifier, ""),
            "current_identifiers": "|".join(landed),
            "resolved_by": "source_concepts_split" if len(landed) > 1 else "source_concepts_merged",
        })

    # Carry forward every redirect previously published. Its former target may
    # itself have been merged since the row was written, so resolve dead target
    # identifiers through their stable upstream source ids to the live corpus.
    current_by_slug = {
        row["retired_slug"]: row for row in rows
        if row["retired_slug"] not in retracted
    }
    active_historical = committed_redirect_slugs()
    for slug, historical in sorted(retired_map_history().items()):
        if slug not in active_historical or slug in retracted:
            # Retracted before the target resolution below, deliberately: a
            # redirect whose targets have all died is exactly the kind a
            # curator needs to withdraw, and that path raises rather than
            # returns.
            continue
        if slug in live_slugs or slug in current_by_slug:
            continue
        landed: set[str] = set()
        unresolved: list[str] = []
        for target in (historical.get("current_identifiers") or "").split("|"):
            target = target.strip()
            if not target:
                continue
            if target in by_id:
                landed.add(target)
                continue
            inherited = {
                by_source[source_id]
                for source_id in retired_sources.get(target, ())
                if source_id in by_source
            }
            if inherited:
                landed.update(inherited)
            else:
                unresolved.append(target)
        if unresolved or not landed:
            raise SystemExit(
                f"cannot carry forward retired slug {slug!r}: no live target for "
                f"{', '.join(unresolved) or historical.get('current_identifiers', '')}"
            )
        current_by_slug[slug] = {
            "retired_slug": slug,
            "retired_identifier": historical.get("retired_identifier", ""),
            "retired_label": historical.get("retired_label", ""),
            "current_identifiers": "|".join(sorted(landed)),
            "resolved_by": (
                "source_concepts_split" if len(landed) > 1
                else "source_concepts_merged"
            ),
        }
    return list(current_by_slug.values())


def write(rows: list[dict[str, str]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: r["retired_slug"]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Fail if RETIRED.tsv is not what this would write.")
    args = parser.parse_args(argv)

    # A shallow clone has no history to reconstruct from, and would silently
    # produce an empty map that --check then reports as "out of date" for the
    # wrong reason. Fail with the actual cause instead (#45's lesson).
    if git("rev-parse", "--is-shallow-repository").strip() == "true":
        print("this is a shallow clone; build_redirects needs full history "
              "(actions/checkout with fetch-depth: 0)", file=sys.stderr)
        return 2

    rows = build()
    if args.check:
        existing = RETIRED_PATH.read_text(encoding="utf-8") if RETIRED_PATH.exists() else ""
        import io
        buffer = io.StringIO()
        writer = csv.DictWriter(buffer, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: r["retired_slug"]))
        if buffer.getvalue() != existing:
            print("RETIRED.tsv is out of date; run `just redirects`", file=sys.stderr)
            return 1
        print(f"RETIRED.tsv is current ({len(rows)} redirects)")
        return 0

    write(rows, RETIRED_PATH)
    by_reason = Counter(r["resolved_by"] for r in rows)
    print(f"wrote {RETIRED_PATH.relative_to(REPO_ROOT)}: {len(rows)} redirect(s)")
    for reason, count in sorted(by_reason.items()):
        print(f"  {reason:26s} {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
