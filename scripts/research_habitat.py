#!/usr/bin/env python3
"""Run deep research for a HabitatMech novel term, via deep-research-client.

2,070 of 3,231 records name a concept no vendored ontology has a term for (#115),
and a term without a definition is not usable by anyone. Writing 92 — eventually
650-790 — genus-differentia definitions by hand, each needing citable sources, is
what this exists to make tractable (#110).

The output is an INPUT TO A CURATOR, not a record. It lands in `research/` and
nothing reads it automatically, for the same reason `data/raw/` is separate from
`data/habitats/`: a model's prose is evidence to weigh, and this repo's whole
posture is that screens and generators rank while a human decides. A definition
written straight from an unread report would be exactly the plausible-sounding
unverifiable claim that `tests/test_decisions.py` exists to catch.

Conventions are TraitMech's, deliberately — these repos share a workflow, and a
second incompatible way to call the same client helps nobody:

* Provider aliases resolve up front so the client call, the credential lookup and
  the output filename all agree on one name.
* The `--template` path is repo-relative. deep-research-client copies whatever it
  is given into each report's `template_file:` front matter, and an absolute path
  bakes one machine's home directory into every tracked report — a value that is
  wrong for every reader but one.
* No `--separate-citations`. TraitMech found all 353 of its sidecars malformed:
  broken markdown-link tails, stray trailing commas, and most listing the same
  reference two or three times.

Usage:
    python3 scripts/research_habitat.py --identifier habitatmech:GOLD.cd0b0940e5
    python3 scripts/research_habitat.py --identifier ... --dry-run
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
HABITATS_DIR = REPO_ROOT / "data" / "habitats"
RESEARCH_DIR = REPO_ROOT / "research"
TEMPLATE = REPO_ROOT / "templates" / "habitat_definition_research.md"

# Friendly names → what deep-research-client actually accepts. Mirrors
# TraitMech's map so a provider named in one repo means the same in the other.
PROVIDER_ALIASES = {"edison": "falcon"}

# Defaulting to a provider whose credential is absent turns every invocation
# into a failed call that looks like a code error, so this is the one that is
# actually reachable here rather than the one TraitMech happens to use.
#
# `cborg` was tried first, for parity with TraitMech, and its canary failed in
# 8 seconds: the cborg route asks OpenAI's /responses endpoint for
# o3-deep-research-2025-06-26, and the CBORG key exposes 1,084 models with no
# deep-research model among them. `--provider cborg` still works wherever a key
# does have one.
#
# claude_code needs no extra credential, and its defaults are the conservative
# ones: a read-only tool allowlist (WebSearch, WebFetch) so an agent-driven
# query cannot touch the filesystem, and a min_report_chars guard that raises
# rather than writing a well-formed file with no research in it.
DEFAULT_PROVIDER = "claude_code"

# deep-research-client requires Python >= 3.12 and this project supports 3.10, so
# it is not a project dependency that can simply be imported. uvx runs it in an
# isolated environment; `uv run --python 3.12` would appear to work and would
# delete and rebuild the project's own .venv on the way.
DEFAULT_CLIENT_COMMAND = (
    "uvx --python 3.12 --prerelease=allow "
    "--from deep-research-client[cyberian] deep-research-client"
)


def resolve_provider(provider: str) -> str:
    """Canonicalise on both hit and miss.

    Returning the caller's casing on a miss would send `Falcon` to a client that
    only accepts `falcon` and — because the output filename is built from this —
    would look for `-deep-research-Falcon.md`, re-running and re-paying for work
    already done on a case-sensitive filesystem.
    """
    key = provider.lower()
    return PROVIDER_ALIASES.get(key, key)


def provider_args(provider: str) -> list[str]:
    if provider == "cborg":
        return ["--use-cborg"]
    return ["--provider", provider]


def research_env(provider: str) -> dict[str, str]:
    """Alias the Edison / Falcon credentials the way TraitMech does."""
    env = os.environ.copy()
    if not env.get("EDISON_API_KEY") and env.get("EDISON_PLATFORM_API_KEY"):
        env["EDISON_API_KEY"] = env["EDISON_PLATFORM_API_KEY"]
    if provider == "falcon" and not env.get("EDISON_API_KEY") and env.get("FUTUREHOUSE_API_KEY"):
        env["EDISON_API_KEY"] = env["FUTUREHOUSE_API_KEY"]
    return env


def _repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def load_record(identifier: str) -> tuple[Path, dict]:
    for path in sorted(HABITATS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(doc, dict) and doc.get("identifier") == identifier:
            return path, doc
    raise SystemExit(f"no record with identifier {identifier!r}")


def decision_note(identifier: str, doc: dict) -> str:
    """The curator's reason this concept has no term.

    Decisions are keyed on a source concept, not on the record, so this walks
    the record's own curation history instead — which is where #94 put the
    reasoning, and is correct for a merged record with several decisions.
    """
    notes = [
        event.get("changes", "")
        for event in (doc.get("curation_history") or [])
        if event.get("action") not in (None, "SEEDED_FROM_SOURCES")
    ]
    return " ".join(notes) or "(no curator note recorded)"


def template_vars(doc: dict) -> dict[str, str]:
    attestations = doc.get("source_attestations") or []
    return {
        "habitat_label": doc.get("label", ""),
        "habitat_identifier": doc.get("identifier", ""),
        "habitat_category": doc.get("habitat_category", ""),
        "grounding_status": doc.get("grounding_status", ""),
        "attestations": "; ".join(
            f"{a.get('source')}: {a.get('source_path') or a.get('source_label')}"
            for a in attestations
        ) or "(none)",
        "assertions": str(sum(a.get("assertion_count") or 0 for a in attestations)),
        "parent_terms": ", ".join(
            p for p in (doc.get("parent_habitats") or []) if not p.startswith("habitatmech:")
        ) or "(none)",
        "xrefs": ", ".join(doc.get("xrefs") or []) or "(none)",
        "decision_note": decision_note(doc.get("identifier", ""), doc),
    }


# A report shorter than this is a failed call that happened to write something.
# Mirrors deep-research-client's own min_report_chars default, which exists for
# the same reason: "a shorter result raises rather than writing a well-formed
# file with no research in it".
MIN_REPORT_BYTES = 200


def completed_report(doc: dict, provider: str) -> Path | None:
    """The report this record can resume from, or None.

    One function, called by both the single-record script and the batch runner.
    They used to test different things — `exists()` here and `exists() and
    non-empty` in the runner — so a partial write followed by a retry was
    skipped as done and then recorded as ok, permanently (#122). Resume must
    mean the same thing to whoever asks.
    """
    out = output_path(doc, provider)
    return out if out.exists() and out.stat().st_size >= MIN_REPORT_BYTES else None


def output_path(doc: dict, provider: str) -> Path:
    slug = re.sub(r"[^a-z0-9]+", "-", (doc.get("label") or "").lower()).strip("-") or "unnamed"
    ident = re.sub(r"[^a-z0-9]+", "-", doc.get("identifier", "").lower()).strip("-")
    category = (doc.get("habitat_category") or "other").lower()
    return RESEARCH_DIR / "habitats" / category / f"{slug}-{ident}-deep-research-{provider}.md"


def build_command(*, provider: str, output_file: Path, variables: dict[str, str],
                  passthrough: list[str], client_command: str) -> list[str]:
    # Split, so the whole launcher can be passed as one string. The client needs
    # Python >= 3.12 while this project still supports 3.10, so the usual way to
    # reach it is an isolated `uvx ... deep-research-client` rather than a bare
    # executable on PATH — and `uv run --python 3.12` is NOT the way, because it
    # tears down and recreates the project's .venv as a side effect.
    command = [*shlex.split(client_command), "research",
               "--template", _repo_relative(TEMPLATE)]
    for key, value in variables.items():
        command.extend(["--var", f"{key}={value}"])
    command.extend(provider_args(provider))
    # Absolute, because the child runs at REPO_ROOT and a relative path would
    # have the parent create one directory and the child write into another.
    command.extend(["--output", str(output_file.resolve())])
    command.extend(passthrough)
    return command


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--identifier", required=True,
                        help="A record identifier, e.g. habitatmech:GOLD.cd0b0940e5")
    parser.add_argument("--provider", default=DEFAULT_PROVIDER)
    parser.add_argument(
        "--client-command",
        default=os.environ.get("DEEP_RESEARCH_CLIENT", DEFAULT_CLIENT_COMMAND),
        help="How to invoke deep-research-client. Split with shlex, so a full "
             "isolated launcher can be passed as one string. Overridable with "
             "$DEEP_RESEARCH_CLIENT.",
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the command without calling the provider. Free, and the "
                             "check to run before any batch.")
    parser.add_argument("--force", action="store_true",
                        help="Re-run even though a report already exists. Costs a paid call.")
    args, passthrough = parser.parse_known_args(argv or sys.argv[1:])

    provider = resolve_provider(args.provider)
    _path, doc = load_record(args.identifier)

    if doc.get("grounding_status") not in ("UNGROUNDED", "NOT_APPLICABLE"):
        print(f"note: {args.identifier} is {doc.get('grounding_status')}, so an ontology term "
              "already names it — research is for concepts that have none", file=sys.stderr)

    out = output_path(doc, provider)
    if completed_report(doc, provider) and not args.force:
        print(f"already researched: {_repo_relative(out)}\nPass --force to pay for it again.")
        return 0
    if out.exists() and out.stat().st_size < MIN_REPORT_BYTES:
        print(f"re-running: {_repo_relative(out)} is {out.stat().st_size} bytes, "
              f"below the {MIN_REPORT_BYTES}-byte floor", file=sys.stderr)

    variables = template_vars(doc)
    command = build_command(provider=provider, output_file=out, variables=variables,
                            passthrough=passthrough, client_command=args.client_command)

    print(f"Researching: {variables['habitat_label']} ({provider}) -> {_repo_relative(out)}")
    if args.dry_run:
        print(shlex.join(command))
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(command, check=True, env=research_env(provider), cwd=REPO_ROOT)

    # Verify the side effect, not the exit code: a run can report success, cost
    # real money, and persist nothing.
    if completed_report(doc, provider) is None:
        size = out.stat().st_size if out.exists() else 0
        raise SystemExit(
            f"provider returned success but wrote {size} bytes to {out} "
            f"(floor is {MIN_REPORT_BYTES})"
        )
    print(f"wrote {_repo_relative(out)} ({out.stat().st_size} bytes)")
    return 0


def undefined_novel_terms() -> list[tuple[int, str, str]]:
    """Records that need a definition: novel, examined, and not yet authored.

    Ranked by upstream assertion volume, because that is what a definition buys
    — the number of observations it makes interpretable.
    """
    from habitatmech.curate.definitions import load_curated_definitions

    authored = set(
        load_curated_definitions(REPO_ROOT / "curation" / "term_requests.tsv")
    )
    excluded_path = REPO_ROOT / "curation" / "term_requests_excluded.tsv"
    excluded: set[str] = set()
    if excluded_path.exists():
        with excluded_path.open(newline="", encoding="utf-8") as fh:
            excluded = {
                row["identifier"]
                for row in csv.DictReader(fh, delimiter="\t")
                if (row.get("identifier") or "").strip()
            }

    decisions: dict[str, dict] = {}
    path = REPO_ROOT / "curation" / "decisions.tsv"
    if path.exists():
        with path.open(newline="", encoding="utf-8") as fh:
            decisions = {r["identifier"]: r for r in csv.DictReader(fh, delimiter="\t")}
    out = []
    for record in sorted(HABITATS_DIR.rglob("*.yaml")):
        doc = yaml.safe_load(record.read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or doc.get("grounding_status") != "UNGROUNDED":
            continue
        if doc.get("mapping_status") != "REVIEWED":
            continue
        identifier = doc["identifier"]
        if identifier in authored or identifier in excluded:
            continue
        if (decisions.get(identifier, {}).get("review_depth") or "ITEM").upper() != "ITEM":
            continue
        volume = sum(a.get("assertion_count") or 0 for a in doc.get("source_attestations") or [])
        out.append((volume, doc.get("label", ""), identifier))
    return sorted(out, reverse=True)


if __name__ == "__main__":
    raise SystemExit(main())
