---
name: curate-yaml-record
description: Review and curate one HabitatMech habitat record through its authoritative decision, definition, and source-input surfaces, checking habitat identity, grounding, hierarchy, attestations, parameters, taxa, evidence, completeness, and resolvable gaps. Use for a named record audit or improvement; do not hand-edit generated habitat YAML or treat this as permission to spend credits, contact anyone, or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Curate one HabitatMech record

Produce a defensible habitat record by changing the authoritative inputs that
generate it, with an explicit account of what is supported, corrected,
unresolved, and genuinely unknown. Search results and deep-research reports are
leads; only inspected sources can support a decision.

## Boundaries

- Resolve one generated target under `data/habitats/<category>/` and every
  source concept feeding it. Stop if the label matches several habitats or the
  record is a multi-source merge whose target was not specified clearly.
- Review/audit requests are read-only. Curate, improve, complete, correct, or
  add-evidence requests authorize local edits only to the smallest maintained
  input/rule needed to regenerate the named record.
- Never hand-edit `data/habitats/` or generated `pages/`. Grounding decisions
  belong in `curation/decisions.tsv`; minted definitions and authored hierarchy
  belong in `curation/term_requests.tsv`; source assertions belong in their
  extractor/inventory.
- Never launch paid research, contact anyone, or create/edit a GitHub item or
  outbound message without explicit authorization.
- Preserve unrelated work and use a dedicated branch/worktree.
- Never fill an optional field for coverage or infer false from absence.

## Read before judging the record

Read the full generated target plus:

- `CLAUDE.md`, `docs/CURATION.md`, `docs/HARMONIZATION.md`, and
  `docs/RESEARCH.md`;
- the relevant `HabitatRecord`, source-attestation, parameter, taxon, evidence,
  graph, discussion, and history classes in
  `src/habitatmech/schema/habitatmech.yaml`;
- matching `curation/decisions.tsv`, `curation/term_requests.tsv`, path-lock,
  and source-inventory rows;
- [references/review-checklist.md](references/review-checklist.md).

Rendered pages, generated YAML, and research prose are not independent sources.

## Workflow

### 1. Establish the baseline

Read the entire YAML and trace each value to its input. Record identifier,
label, definition/source, category, parents, xrefs, all source attestations,
parameters, taxa, grounding and mapping status, evidence, graphs, discussions,
datasets, and history. Run:

```bash
just validate <record-path>
just validate-strict <record-path>
just verify-corpus
```

Use `just worklist` and `just report` to find the source concepts and decision
depths. A reproducible record can still contain a scientifically wrong input.

### 2. Verify habitat identity and grounding first

Confirm that each source concept denotes a microbial habitat rather than a
quality, chemical, disease, process, procedure, sample artifact, or whole host
taxon. Verify source path, minted ID, ontology candidate, canonical label,
grounding status, xrefs, and category.

Use `GROUND` only for exact identity; `GROUND_AS_PARENT` only for a strictly
broader term; `CONFIRM_UNGROUNDED` for a real habitat without a fitting term;
`NOT_APPLICABLE` only when the source concept is not a habitat; and `REVIEW` to
endorse the seeder's current answer. Exact grounding is always an item-level
decision.

### 3. Review every generated scientific claim

Trace parents, source attestations, MIxS triad roles, environmental parameters,
characteristic taxa, evidence, and any causal graph to their authoritative
input. Verify relationship direction, source unit/count, score semantics,
organism/context, and source version. Do not sum unlike assertion units or
treat PREGO association as characteristic presence.

A host organism may be a habitat context, but a whole-organism/taxon term is
not the habitat identity. Anatomy can ground directly when it denotes the
microbial site. Every causal edge requires real cited evidence; upstream
attestation is not mechanism evidence.

### 4. Assess completeness and resolve supported gaps

Apply the checklist and use bounded searches for consequential gaps. Prioritize:

1. non-habitat or conflated identity and wrong grounding relation;
2. invalid hierarchy, host/anatomy handling, or merged-source equivalence;
3. misleading source-attestation or environmental-parameter interpretation;
4. overclaimed characteristic taxa;
5. unsupported evidence or causal claims.

Do not create generic discussions for empty fields. If a requested curator-
owned field has no maintained input path, report that infrastructure gap rather
than bypassing corpus reproduction.

### 5. Change authoritative inputs and regenerate

For a grounding/review decision, add or update the one source-concept row in
`curation/decisions.tsv`, including `review_depth: ITEM`, curator/date, verified
ID/label, and reasoning. For a minted term definition, use
`curation/term_requests.tsv` and select `ADD` versus `REPLACE` parent mode by
the rules in `docs/CURATION.md`. Fix source-owned facts in the extractor or
inventory that owns them.

Use curator `claude` only when no identity was supplied; never attribute agent
judgement to the user. The seeder derives `mapping_status` and curation history;
never set either directly. A merged record becomes REVIEWED only when every
contributing source concept has an item-level decision.

Regenerate with a dry run and one canary before wider application:

```bash
just seed
just seed-canary <IDENTIFIER>
```

Inspect the generated file before `just seed-apply --force`. Do not prune on a
partial run.

### 6. Verify and report

```bash
just validate-strict <record-path>
just verify-corpus
just render
just qc
git diff --check
git diff -- curation data/raw src scripts data/habitats pages
```

Re-read the generated record. Confirm every decision, status, parent, source
attestation, and history event follows from the edited input and the diff is
limited to expected generated products.

Report corrections/additions and sources, retained claims checked, unresolved
gaps and bounded searches, authoritative input rows changed, why the generated
status is or is not REVIEWED, and all validation results.
