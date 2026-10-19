---
name: audit-schema-gaps
description: "Systematic gap-and-inconsistency audit for the HabitatMech LinkML schema, the YAML habitat corpus, and the scripts that generate them. Uses existing validation harnesses as diagnostics and saves assessed findings and a prioritized fix backlog as a structured review. Invoke for schema drift, data-quality issues, new bulk migrations, or records silently failing validation."
category: quality
requires_database: false
requires_internet: false
version: 1.0.0
tags: [validation, linkml, schema, data-quality, audit, qc]
---

# Audit schema gaps (schema · instances · pipeline)

## Structured Audit Output

Follow [docs/record-reviews.md](../../../docs/record-reviews.md) and
[docs/record-review-profile.md](../../../docs/record-review-profile.md). New
assessed audit findings use this registered skill and `kind: repository` (or
`batch` for an explicitly bounded record set). Save authoritative YAML plus
derived Markdown under `reviews/structured/<timestamp>-<slug>/`; link both.

Keep the schema / instances / process axes in assessment dimensions named
`audit_axis`. Preserve exact record IDs, field paths, error categories, counts,
nonzero metric denominators, sampled/full coverage and unavailable checks.
Schema probes, validator TSVs and writer heuristics are diagnostic evidence,
not completed scientific review. A schema/process-only assessment uses
`scientific_review: false`; no clean scan establishes scientific approval.
Interpret each finding against inspected inputs before saving it. Distinguish
positive supported assessments from gaps and unassessed targets.

Identify the schema declaration or writer script responsible for each proposed
repair. Hash those inputs, the exact schema and scan outputs actually used.
Preserve backlog IDs, impact, effort, fix paths and dependencies in findings,
actions and assessment details.

```bash
uv run python scripts/record_review.py inspect --targets /tmp/audit-targets.yaml
uv run python scripts/record_review.py validate /tmp/completed-audit.yaml
uv run python scripts/record_review.py save --content /tmp/completed-audit.yaml
```

Use session-unique temporary paths. Audit-only work does not edit scientific
records, schema, writers, status gates or history. Missing required harnesses
are unavailable checks; implementing or applying repairs requires separate
curation intent. Existing reports stay historical and are not rewritten.

## Why this skill exists

Open-schema LinkML validation ignores undeclared fields, allowing import or
curation scripts to emit keys that `src/habitatmech/schema/habitatmech.yaml`
does not declare. In HabitatMech, `just validate-strict`
(`scripts/validate_strict.py`) enforces closed-schema validation across all
records under `data/habitats/**/*.yaml`, and `just verify-corpus`
(`scripts/verify_corpus.py`) checks corpus-wide invariants, identifier
uniqueness, and minted-ID registry alignment (`curation/minted_identifiers.tsv`).
Always derive current record and error counts from a fresh run.

The skill is built around three orthogonal lenses:

1. **Instance-record validation** — every YAML under `data/habitats/**/*.yaml`
   is validated against `HabitatRecord` in closed mode via
   `scripts/validate_strict.py` and checked for corpus invariants via
   `scripts/verify_corpus.py`.
2. **Schema audit** — structural inspection of `src/habitatmech/schema/habitatmech.yaml`
   for identifier policy (`id` carrying `ENVO:<digits>` or minted
   `HabitatMech:NNNNNN`), untyped `string` slots, term wrapper consistency,
   `required:` rules, orphan enums, and enum casing.
3. **Pipeline / writer audit** — inspection of YAML-writing modules in
   `scripts/` and `src/habitatmech/` for `curation_history` tracking,
   `--dry-run` support, pre-write validation, and `justfile` wiring.

## When to use

| Trigger | Why |
|---|---|
| User asks to "audit the schema / records / pipeline" | Direct ask for three-axis drift detection. |
| User reports records "silently fail" or "validation passes but the data is wrong" | Signature symptom of open-schema validation. |
| A new importer, ENVO enrichment script, or bulk migration is added | Confirm it did not introduce undeclared keys or bypass history tracking. |
| Schema changes (`src/habitatmech/schema/habitatmech.yaml` modified) | Refresh instance and writer checks against the updated schema. |
| Cold-start repository health check | `just validate-strict` and `just verify-corpus` quantify current drift. |

**Don't** invoke this skill for:
- Quick three-axis error triage without saving a structured review — use `schema-gap-analysis`.
- Single-record scientific review or curation — use `review-yaml-record` or `curate-yaml-record`.
- Identifier minting or `curation/minted_identifiers.tsv` reconciliation alone — use `manage-identifiers`.

## Workflow

### Step 1 — Closed-schema instance and corpus validation

**Files:** `scripts/validate_strict.py`, `scripts/verify_corpus.py`
**Just targets:** `just validate-strict`, `just verify-corpus`

```bash
just validate-strict
just verify-corpus
```

Or write strict validation failures to a session-unique TSV:

```bash
uv run python scripts/validate_strict.py --out /tmp/habitatmech_strict.tsv
```

### Step 2 — Schema structural audit

Run `just validate-schema` and inspect `src/habitatmech/schema/habitatmech.yaml`:

```bash
just validate-schema
```

Check for:
- Classes missing `identifier: true` slots where cross-record referencing occurs.
- Slots with `range: string` that represent closed vocabularies or CURIEs.
- Term/ontology wrapper consistency across environmental descriptors, physicochemical ranges, and associated taxa.
- Orphan enums and mixed enum value casing.

### Step 3 — Pipeline / writer audit

Inspect all Python modules in `scripts/` and `src/habitatmech/` that write
YAML files and verify each corpus mutator for:
- Appending to `curation_history`
- Supporting `--dry-run`
- Validating against `src/habitatmech/schema/habitatmech.yaml` before writing
- Being wired into `justfile`

### Step 4 — Prioritized fix backlog and structured review save

Synthesize the three axes (`schema`, `instances`, `process`) and save the
prioritized backlog (`G01`, `G02`, ...) into
`reviews/structured/<timestamp>-<slug>/review.yaml` (and generated `review.md`)
via `scripts/record_review.py`.

## Anti-patterns

- **Do not rely on `just validate-data` (open-schema) alone.** Use `just validate-strict` to catch undeclared fields.
- **Do not hardcode corpus or error counts in skill prose.** Always measure from live command runs.
- **Do not edit records, schema, or writers during an audit pass.**

## Related skills

- `schema-gap-analysis` — canonical three-axis drift classification guide.
- `manage-identifiers` — `ENVO:` vs `HabitatMech:NNNNNN` identifier policy.
- `id-label-correspondence` — ontology ID and canonical label correspondence checks.
- `curate-yaml-record` — single-record evidence-backed curation workflow.
