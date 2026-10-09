# HabitatMech review profile

New record reviews follow [the shared contract](record-reviews.md), with
authoritative YAML and derived Markdown under
`reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/`. Historical ad hoc reports remain
historical evidence and need no migration. `conf/record_review.yaml` lists the
active routes and local rubrics.

## Routes and output

- `.claude/skills/review-yaml-record/SKILL.md`: one resolved record.
- `.claude/skills/review-yaml-category/SKILL.md`: a coherent category with
  explicit lump/split/retain/defer decisions; sampled coverage keeps its method,
  denominator, inspected members and limitations. Explicit batches use `kind: batch`.
- `.claude/skills/curate-yaml-record/SKILL.md`: the audit-only route uses the
  same output contract and retains the native scientific checklist.

Run from the repository root using its own Python environment (LinkML,
linkml-runtime, jsonschema and PyYAML; pytest in the dev extra):

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
just review-validate /tmp/completed-review.yaml
just review-save /tmp/completed-review.yaml
just review-check
```

Use session-unique temporary inputs and add `--input <path>` to inspect for each
additional rubric/schema/source/overlay used. Retain the captured Git revision
and hashes. Checks record actual commands and exit codes, never invented
success. New observations are immutable; link both saved files in the final
response. Missing dependencies or required checks are an explicit blocked output
step or partial assessment, not permission to save unvalidated prose.

## Native questions and generated ownership

Review generated `data/habitats/` records together with every contributing
source concept. The native rubric is `docs/CURATION.md`,
`docs/HARMONIZATION.md`, `docs/RESEARCH.md`, and the local checklist: habitat
identity, exact grounding versus broader parents, merged-source equivalence,
host versus anatomy, MIxS triad roles, source attestations and their units,
environmental parameters, taxon association versus characteristic presence,
and causal-edge support. Preserve source unit/count and score definitions.

Set target kind to `generated`. Maintained owners include the exact rows in
`curation/decisions.tsv`, `curation/term_requests.tsv`,
`curation/gold_parent_exclusions.tsv`, and source inventories/transformations.
Mechanism changes belong to `curation/causal_graphs/<slug>.yaml` overlays.
Hash every inspected overlay and source/decision input using `inspect --input`;
record exact row locators in evidence. Findings/actions name these owners and
the necessary seeder, never a patch to generated YAML or `pages/`.

The seeder derives mapping status and history. A merged record becomes REVIEWED
only when every contributing source concept has an ITEM-level decision. Shared
review validation neither creates those decisions nor changes this gate.

## Native checks

```bash
just validate <record-path>
just validate-strict <record-path>
just validate-causal curation/causal_graphs/<slug>.yaml
just validate-causal-all
just verify-corpus
just validate-products
just qc
```

Use the causal checks when overlays are in scope and report their exact scope.
`just sample` and worklists select or diagnose inputs; `research/habitats/`
contains research leads for a curator. None is a completed scientific review.
Complete the assessment and save it with the shared helper; deterministic-only
inspection declares `scientific_review: false`. Paid research is separate.

## Validation and ownership of the contract

`schema/record_review.yaml`, `scripts/record_review.py`,
`docs/record-reviews.md`, and `tests/test_record_review_contract.py` are copied
byte-identically from CLAW. Canonical marked skill regions are rendered with
the native sections preserved. Edit the shared contract upstream and re-adopt;
the local profile, rubrics and scientific status gates remain repository-owned.
`just review-check` validates retained bundles and runs the profile/roundtrip
contract tests. The existing PR and merge-group quality workflow also runs the
contract test alongside its unchanged native checks. Zero structured reviews
means missing coverage, not a scientific pass. The new path is Git-visible
without opening ignored legacy report directories.

CI fetches full history and sets `RECORD_REVIEW_BASE` from the trusted PR base,
merge-group base, or push-before SHA. It requires that commit to exist before
running the canonical test, which rejects changes or deletions to previously
saved bundles. Local `just review-check` defaults to HEAD; set
`RECORD_REVIEW_BASE=<base-commit>` when checking a branch's committed changes.
There is no automatic CI fallback to an already modified HEAD.
