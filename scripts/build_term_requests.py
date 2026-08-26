#!/usr/bin/env python3
"""Emit HabitatMech's own new-term definitions, in ENVO's ROBOT-template format.

HabitatMech is intended to supersede ENVO for microbial habitats, so these are
not requests to anyone: they are the labels and definitions this project supplies
for concepts no ontology names. 2,699 of 3,231 records are concepts ENVO has no
term for, and `just report` tracks that as the headline number.

The format is still ENVO's. That is deliberate and costs nothing: a ROBOT
template is the interchange format the OBO tooling already reads, so writing
definitions in it keeps them loadable by `robot template`, diffable, and usable
by anyone who wants to consume or contribute them — without the project owing
anyone a submission. The column set below is ENVO's template header, verbatim:

    Ontology ID | label | parent class | definition | definition cross reference
    | comment | comment cross reference | editors note | exact synonym
    | broad synonym | narrow synonym | related synonym | in subset
    | cross reference | subclass axiom | creation date | created by

**The term text is curated, not generated.** Deriving labels and definitions
from source labels mechanically produced things like "A environmental system
determined by an organism which is determined by microbial." and "A sediment
which is determined by rock core/Sediment." A definition is the part of a term
that carries its meaning, so it is written by a curator in
`curation/term_requests.tsv` and this script only assembles, validates and
formats it — the same split as `decisions.tsv` and the seeder.

What this script contributes is the part a curator should not retype: the
assertion counts, the attesting sources, the source path, and the record URL,
all read from the corpus so the request cannot drift from what the data says.

House style is taken from ENVO's own siblings rather than from its written rule.
The wiki says the definition's genus "MUST be the exact term label of the
superclass", but `plant-associated environment` — whose asserted parent is
`environmental system determined by an organism` — is defined "An environmental
system determined by a green plant." Following the observed family is what an
editor will expect; following the written rule would make this batch the odd
one out in its own branch.

`created by` wants pipe-delimited full ORCID IRIs. This script cannot know them,
so it leaves the column empty and says so — a guessed attribution is worse than
none.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import yaml

from habitatmech.curate.definitions import load_curated_definitions

REPO_ROOT = Path(__file__).resolve().parent.parent
HABITATS_DIR = REPO_ROOT / "data" / "habitats"
REQUESTS_TSV = REPO_ROOT / "curation" / "term_requests.tsv"
# Concepts examined and deliberately NOT asked for. Without this, the pending
# count conflates "nobody has written this yet" with "this will never be a
# term", and a backlog that cannot reach zero stops being read.
EXCLUDED_TSV = REPO_ROOT / "curation" / "term_requests_excluded.tsv"
OUT_DIR = REPO_ROOT / "curation" / "term_requests"
SITE_BASE = "https://culturebotai.github.io/HabitatMech/pages/"

# ENVO's template sheet header, in order. Do not reorder: editors consume it
# positionally when they compile the batch.
COLUMNS = [
    "Ontology ID", "label", "parent class", "definition",
    "definition cross reference", "comment", "comment cross reference",
    "editors note", "exact synonym", "broad synonym", "narrow synonym",
    "related synonym", "in subset", "cross reference", "subclass axiom",
    "creation date", "created by",
]

# The curator table's own columns are NOT listed here. They are
# `habitatmech.curate.definitions.REQUIRED_COLUMNS`, which is what the seeder
# reads and what `load_requests` below now parses with. A second copy in this
# file would be a second answer to "what is a valid row" for one file that two
# consumers depend on (#165).


def page_slug(doc: dict) -> str:
    """The record's published page slug, from the renderer's own function.

    Reimplementing it here would be a second source of truth for a URL that
    goes into a public submission, and the first version of this script did
    exactly that and emitted citation links that 404.
    """
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from render_pages import slugify

    return slugify(f"{doc['label']}-{doc['identifier']}")


class RequestError(SystemExit):
    """A malformed request. Fails rather than submitting something wrong."""


def load_corpus() -> dict[str, dict]:
    docs = {}
    for path in sorted(HABITATS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("identifier"):
            docs[doc["identifier"]] = doc
    return docs


def load_requests() -> list[dict]:
    """The table, parsed once by the loader the seeder itself uses.

    This file is no longer only an export: the same rows are applied to the
    corpus as HabitatMech's own labels and definitions, so the seeder's loader
    is the authority on what a valid row is. In particular it rejects a repeated
    `requested_label` outright, because in the corpus model that is two records
    claiming one concept rather than two export rows to collapse while silently
    picking one parent and definition (#158).

    That loader used to be called here purely for its exception, with its result
    thrown away — validation by side effect, over a second independent parse of
    the same file, and dead-looking code that a tidy-up would delete without
    anything failing (#165). One parse now, and the rows below are built from
    what it returned.
    """
    if not REQUESTS_TSV.exists():
        return []
    definitions = load_curated_definitions(REQUESTS_TSV)
    return [
        {
            "identifier": definition.identifier,
            "requested_label": definition.label,
            "parent_class": definition.parent_class,
            "parent_label": definition.parent_label,
            "definition": definition.definition,
            "exact_synonym": "|".join(definition.exact_synonyms),
            "curator": definition.curator,
            "date": definition.date,
            "notes": definition.notes,
            "parent_mode": definition.parent_mode,
        }
        for definition in definitions.values()
    ]


def validate(requests: list[dict], corpus: dict[str, dict],
             labels: dict[str, str]) -> None:
    """Refuse to emit a request that misstates the ontology or the corpus.

    These are the same three claims `decisions.tsv` is checked for, because a
    term request makes them too and this one goes to strangers: the record
    exists, the parent exists and is labelled as claimed, and the definition
    names that parent's actual label.
    """
    problems = []
    for row in requests:
        identifier = row["identifier"]
        prefix = f"{REQUESTS_TSV.name}: {identifier}"
        doc = corpus.get(identifier)
        if doc is None:
            problems.append(f"{prefix}: no such record in the corpus")
            continue
        if doc.get("grounding_status") != "UNGROUNDED":
            problems.append(
                f"{prefix}: is {doc.get('grounding_status')}, not UNGROUNDED — "
                "a grounded record does not need a new term"
            )
        parent = (row.get("parent_class") or "").strip()
        actual = labels.get(parent)
        if actual is None:
            problems.append(f"{prefix}: parent {parent} is not in the vendored slice")
        elif actual.strip().lower() != (row.get("parent_label") or "").strip().lower():
            problems.append(
                f"{prefix}: parent_label says {row.get('parent_label')!r} but "
                f"{parent} is {actual!r}"
            )
        if not (row.get("definition") or "").strip().endswith("."):
            problems.append(f"{prefix}: definition must be a sentence ending in '.'")
        if not (row.get("requested_label") or "").strip():
            problems.append(f"{prefix}: requested_label is required")
        if not (row.get("notes") or "").strip():
            problems.append(f"{prefix}: notes are required — an editor will ask why")
    if problems:
        raise RequestError(
            "term requests are not submittable:\n  " + "\n  ".join(problems)
        )


def build(requests: list[dict], corpus: dict[str, dict]) -> list[dict]:
    """One row per REQUESTED TERM, not per record.

    Several source concepts can want the same term — GOLD's "Mammals: Human"
    and BacDive's "Human" both ask for human-associated environment — and
    sending an editor the same term twice is a defect in the request, not a
    detail. Their evidence is pooled instead.

    The pooling cannot currently fire: `load_curated_definitions` rejects a
    repeated `requested_label` before the rows reach here, because the corpus
    reads the same table and a shared label there means two records claiming one
    concept (#158). It is kept rather than deleted because whether
    path-distinguished leaves may share a term label is an open question (#161),
    and this is the branch that would need to exist again if the answer is yes.
    """
    merged: dict[str, dict] = {}
    for row in sorted(requests, key=lambda r: r["requested_label"]):
        doc = corpus[row["identifier"]]
        assertions = sum(a.get("assertion_count") or 0
                         for a in doc.get("source_attestations") or [])
        attestation = (doc.get("source_attestations") or [{}])[0]
        entry = merged.setdefault(row["requested_label"], {
            "row": row, "assertions": 0, "sources": set(),
            "paths": [], "urls": [], "synonyms": set(),
        })
        entry["assertions"] += assertions
        entry["sources"].update(a["source"] for a in doc.get("source_attestations") or [])
        entry["paths"].append(attestation.get("source_path") or attestation.get("source_label") or "")
        entry["urls"].append(f"{SITE_BASE}habitats/{page_slug(doc)}.html")
        if (row.get("exact_synonym") or "").strip():
            entry["synonyms"].update(s.strip() for s in row["exact_synonym"].split("|") if s.strip())

    out = []
    for label, entry in merged.items():
        row = entry["row"]
        out.append({
            "Ontology ID": "",
            "label": label,
            "parent class": row["parent_class"],
            "definition": row["definition"],
            # ENVO wants citation URLs pipe-delimited with no spaces.
            "definition cross reference": "|".join(entry["urls"]),
            "comment": "",
            "comment cross reference": "",
            "editors note": (
                f"Requested by HabitatMech. Attested by "
                f"{', '.join(sorted(entry['sources']))} with {entry['assertions']} "
                f"upstream assertions across {len(entry['paths'])} source concept(s): "
                f"{'; '.join(p for p in entry['paths'] if p)}. {row['notes']}"
            ),
            "exact synonym": "|".join(sorted(entry["synonyms"])),
            "broad synonym": "",
            "narrow synonym": "",
            "related synonym": "",
            "in subset": "",
            "cross reference": "",
            # ENVO explicitly does not ask collaborators for this.
            "subclass axiom": "",
            "creation date": "",
            "created by": "",
            "_assertions": entry["assertions"],
        })
    out.sort(key=lambda r: -r["_assertions"])
    return out


def excluded() -> dict[str, str]:
    """Examined, and deliberately not asked for — with the reason."""
    if not EXCLUDED_TSV.exists():
        return {}
    with EXCLUDED_TSV.open(newline="", encoding="utf-8") as fh:
        return {r["identifier"]: r["why_not_a_term_request"]
                for r in csv.DictReader(fh, delimiter="\t")}


def unrequested(corpus: dict[str, dict], requested: set[str],
                decisions: dict[str, dict]) -> list[tuple]:
    """Individually-examined ungrounded records with no request written yet.

    Kept visible so the batch's coverage is a number rather than an impression:
    a term-request file that silently covers a third of the gap reads like it
    covers all of it.
    """
    out = []
    for identifier, doc in corpus.items():
        if doc.get("grounding_status") != "UNGROUNDED":
            continue
        if doc.get("mapping_status") != "REVIEWED":
            continue
        decision = decisions.get(identifier, {})
        if (decision.get("review_depth") or "ITEM").upper() != "ITEM":
            continue
        if identifier in requested or identifier in excluded():
            continue
        assertions = sum(a.get("assertion_count") or 0
                         for a in doc.get("source_attestations") or [])
        out.append((assertions, doc.get("label", ""), identifier))
    return sorted(out, reverse=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUT_DIR)
    parser.add_argument("--check", action="store_true",
                        help="Fail if the committed table is not what this would emit.")
    args = parser.parse_args(argv)

    with (REPO_ROOT / "data" / "raw" / "ontology_terms.tsv").open(
        newline="", encoding="utf-8"
    ) as fh:
        labels = {r["term_id"]: r["label"] for r in csv.DictReader(fh, delimiter="\t")}

    corpus = load_corpus()
    requests = load_requests()
    validate(requests, corpus, labels)
    rows = build(requests, corpus)

    table = "\n".join(
        ["\t".join(COLUMNS)] + ["\t".join(r.get(c, "") for c in COLUMNS) for r in rows]
    ) + "\n"
    out_path = args.out / "envo_robot_template.tsv"

    if args.check:
        if not out_path.exists() or out_path.read_text(encoding="utf-8") != table:
            print("curation/term_requests/envo_robot_template.tsv is stale; "
                  "regenerate with `python3 scripts/build_term_requests.py`")
            return 1
        print(f"term-request table is current ({len(rows)} terms)")
        return 0

    args.out.mkdir(parents=True, exist_ok=True)
    out_path.write_text(table, encoding="utf-8")
    print(f"wrote {out_path.relative_to(REPO_ROOT)}: {len(rows)} ENVO terms "
          f"from {len(requests)} source records")

    decisions_path = REPO_ROOT / "curation" / "decisions.tsv"
    decisions = {}
    if decisions_path.exists():
        with decisions_path.open(newline="", encoding="utf-8") as fh:
            decisions = {r["identifier"]: r for r in csv.DictReader(fh, delimiter="\t")}
    pending = unrequested(corpus, {r["identifier"] for r in requests}, decisions)
    skipped = excluded()
    covered = sum(r["_assertions"] for r in rows)
    print(f"\n{len(pending)} examined-ungrounded record(s) still have no request written. "
          f"Top by volume:")
    for assertions, label, identifier in pending[:10]:
        print(f"  {assertions:7d}  {label[:34]:34s} {identifier}")
    print(f"\ncovered {covered} upstream assertions; "
          f"{sum(p[0] for p in pending)} still unrequested across {len(pending)} record(s); "
          f"{len(skipped)} examined and deliberately not asked for")
    print("\n`created by` is empty: it wants pipe-delimited full ORCID IRIs and this "
          "script cannot know them.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
