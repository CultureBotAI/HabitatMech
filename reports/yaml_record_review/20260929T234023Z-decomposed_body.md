# YAML Record Review: Decomposed body

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/decomposed_body.yaml`
- Started UTC: `2026-09-29T23:34:05Z`
- Finished UTC: `2026-09-29T23:40:23Z`
- Verdict: needs item curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.098a328598` |
| Label | `Decomposed body` |
| Stable slug | `decomposed_body` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | `habitatmech:GOLD.098a328598` |
| Source attestation | `GOLD`, `gold.ecosystem:7502`, `Host-associated > Birds > Remains > Decomposed body` |

The record is the generated GOLD concept for the Bird-specific
`Decomposed body` path under `Host-associated > Birds > Remains`. It has one
GOLD source attestation, no assertion count, one generated source-path parent,
no authored definition, no synonyms, no environmental parameters, no
characteristic taxa, no record-level evidence block, and no causal graphs.

The generated record is structurally reproducible from maintained inputs. Its
current `UNGROUNDED` state comes from a class-level `CONFIRM_UNGROUNDED` row
that checked only the automated lexical routes into the vendored ontology
slice; it did not item-review the Bird `Decomposed body` source path.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/decomposed_body.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/decomposed_body.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206 on disk, with 0 missing, 0 extra, and 0 differing. |
| `just report --ungrounded-top 0 --out /private/tmp/habitatmech-report-bird-decomposed-body.tsv` | Passed; wrote the TSV snapshot and reported `habitatmech:GOLD.098a328598` as `UNGROUNDED`, `SEEDED`, 1 source, 0 assertions, no definition, 1 parent, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --limit 40 --status all --out /private/tmp/habitatmech-worklist-bird-decomposed-body.tsv` | Passed; wrote 953 ungrounded backlog rows and listed `habitatmech:GOLD.098a328598` at row 491 with 0 assertions from the Bird `Decomposed body` GOLD path. |

## Identity and Grounding

The minted GOLD identity is sound. `data/raw/gold_ecosystem_paths.tsv` has the
exact source row `Host-associated > Birds > Remains > Decomposed body` with
leaf label `Decomposed body`, depth 4, two collapsed GOLD ecosystem node IDs,
zero aggregate assertions, and source IDs
`gold.ecosystem:7502|gold.ecosystem:7503`.

`data/habitats/PATHS.tsv` pins `habitatmech:GOLD.098a328598` to the stable
`decomposed_body` slug, and the generated target YAML uses that identifier and
slug for exactly this Bird source path.

The generated `UNGROUNDED` status is traceable, but only to a class-level
decision. `curation/decisions.tsv` has a `CONFIRM_UNGROUNDED` row for
`habitatmech:GOLD.098a328598` with `review_depth` `CLASS`. The embedded YAML
history and rendered page both carry that class-level curation note. An
ignored/hidden-inclusive exact search found no `decomposed body` label in
`data/raw/ontology_terms.tsv`, which is consistent with the class-level
lexical no-match.

The generated parent `habitatmech:GOLD.07c6babcdb` is traceable to the
immediate GOLD source path `Host-associated > Birds > Remains`.
`data/habitats/PATHS.tsv` pins that parent identifier to `remains`, and the
parent record has the same class-level `CONFIRM_UNGROUNDED` provenance.

The target is distinct from the other generated Decomposed body records for
Fish and Mammals: Human. Those source paths preserve their own host-branch
context in separate `habitatmech:GOLD.*` identifiers.

## Evidence

The record carries no curator-authored evidence block. Its identity is backed
by the GOLD path inventory and the maintained class-level grounding decision,
not by an item-level curation decision.

The zero assertion total is supported by the raw GOLD inventory. The exact raw
row reports `organism_count = 0`, `study_count = 0`, `biosample_count = 0`,
`mixs_triad_count = 0`, `gold_triad_count = 0`, and `total_assertions = 0` for
this path, and ignored/hidden-inclusive searches for `gold.ecosystem:7502`
and `gold.ecosystem:7503` found no rows in
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or
`data/raw/gold_studies.tsv`.

No causal graph is attached to this record. Ignored/hidden-inclusive searches
found no causal overlay keyed by `habitatmech:GOLD.098a328598`,
`gold.ecosystem:7502`, `gold.ecosystem:7503`, or the exact source GOLD path
under `curation/causal_graphs`.

## Completeness

- The rendered page
  `pages/habitats/decomposed-body-habitatmech-gold-098a328598.html` reflects
  the same minted identifier, label, category, `UNGROUNDED` grounding,
  `SEEDED` mapping status, GOLD source path, collapsed-node note, single
  broader habitat, and class-level curation event as the YAML.
- The exact ignored/hidden-inclusive search for
  `habitatmech:GOLD.098a328598`, `gold.ecosystem:7502`,
  `gold.ecosystem:7503`, and the full source path covered `curation`,
  `history`, `research`, `conf/`, and prior YAML review reports. It found the
  maintained class-level curation decision, but no item-level curation
  decision, maintained overlay, research report, history record, causal graph,
  or prior exact review for this target.
- The other generated children under `Host-associated > Birds > Remains` are
  `Fossilized remains`, `Frozen remains`, `Mummified remains`, and
  `Skeletonized remains`; each remains a separate source-path child of
  `habitatmech:GOLD.07c6babcdb`.
- Empty optional slots are appropriate for the current zero-assertion source
  row. No raw side-table rows support generated environmental parameters or
  taxa, and no maintained overlay supplies causal graphs.

## Findings

| Severity | Finding | Evidence |
|---|---|---|
| Major | The record's `UNGROUNDED` status is still a class-level lexical no-match, not item-level signoff on the Bird `Decomposed body` source concept. | `curation/decisions.tsv` lists `habitatmech:GOLD.098a328598` as `CONFIRM_UNGROUNDED` with `review_depth` `CLASS`, and `just worklist --status all` still ranks the record in the 953-row ungrounded backlog. |

No structural or reproducibility defects were found in the generated YAML.

## Recommended Edits

1. Item-review `habitatmech:GOLD.098a328598` in `curation/decisions.tsv`.
   Inspect GOLD ecosystem nodes `7502` and `7503` and decide whether
   `Host-associated > Birds > Remains > Decomposed body` is a habitat concept,
   a term-request candidate, or narrower than any existing vendored term.
2. If no existing term fits, keep `CONFIRM_UNGROUNDED` at `ITEM` depth and add
   a `curation/term_requests.tsv` definition for the minted record. Use `ADD`
   parent mode to preserve the generated Birds `Remains` parent unless
   item-level review proves that parent false.

## Follow-up Checks

After item-level curation, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.098a328598`
- `just validate data/habitats/host_associated/decomposed_body.yaml`
- `just validate-strict data/habitats/host_associated/decomposed_body.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just report --ungrounded-top 0 --out /tmp/habitatmech-report-bird-decomposed-body.tsv`
- `git diff --check`

If the item-level edit adds a term request or causal overlay, also inspect the
regenerated target to confirm the definition, parents, status, and history
entries follow from maintained inputs.

## Additional Notes

- The existing review of
  `reports/yaml_record_review/20260928T060854Z-fossilized_remains.md` covers
  the sibling `Fossilized remains` child, not this Decomposed body record.
- iModulonDB structured source checks were not applicable: the record names a
  GOLD habitat path and no genes, locus tags, regulators, pathways,
  stress-response terms, or transcriptomic datasets.
