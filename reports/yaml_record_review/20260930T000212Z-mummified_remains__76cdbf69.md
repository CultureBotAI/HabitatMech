# YAML Record Review: Mummified remains

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/mummified_remains__76cdbf69.yaml`
- Started UTC: `2026-09-29T23:58:00Z`
- Finished UTC: `2026-09-30T00:02:12Z`
- Verdict: needs item curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.b933f64ea6` |
| Label | `Mummified remains` |
| Stable slug | `mummified_remains__76cdbf69` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | `habitatmech:GOLD.b933f64ea6` |
| Source attestation | `GOLD`, `gold.ecosystem:7500`, `Host-associated > Birds > Remains > Mummified remains` |

The record is the generated GOLD concept for the Bird-specific
`Mummified remains` path under `Host-associated > Birds > Remains`. It has one
GOLD source attestation, no assertion count, one generated source-path parent,
no authored definition, no synonyms, no environmental parameters, no
characteristic taxa, no record-level evidence block, and no causal graphs.

The generated record is reproducible from maintained inputs. Its current
`UNGROUNDED` state comes from a class-level `CONFIRM_UNGROUNDED` row that
checked only automated lexical routes into the vendored ontology slice; it did
not item-review the Bird `Mummified remains` source path.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/mummified_remains__76cdbf69.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/mummified_remains__76cdbf69.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206 on disk, with 0 missing, 0 extra, and 0 differing. |
| `just report --ungrounded-top 0 --out /private/tmp/habitatmech-report-bird-mummified-remains.tsv` | Passed; wrote the TSV snapshot and reported `habitatmech:GOLD.b933f64ea6` as `UNGROUNDED`, `SEEDED`, 1 source, 0 assertions, no definition, 1 parent, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --limit 40 --status all --out /private/tmp/habitatmech-worklist-bird-mummified-remains.tsv` | Passed; wrote 953 ungrounded backlog rows and listed `habitatmech:GOLD.b933f64ea6` at row 692 with 0 assertions from the Bird `Mummified remains` GOLD path. |

## Identity and Grounding

The minted GOLD identity is sound. `data/raw/gold_ecosystem_paths.tsv` has the
exact source row `Host-associated > Birds > Remains > Mummified remains` with
leaf label `Mummified remains`, depth 4, two collapsed GOLD ecosystem node
IDs, zero aggregate assertions, and source IDs
`gold.ecosystem:7500|gold.ecosystem:7501`.

`data/habitats/PATHS.tsv` pins `habitatmech:GOLD.b933f64ea6` to the stable
`mummified_remains__76cdbf69` slug, and the generated target YAML uses that
identifier and slug for exactly this Bird source path.

The generated `UNGROUNDED` status is traceable, but only to a class-level
decision. `curation/decisions.tsv` has a `CONFIRM_UNGROUNDED` row for
`habitatmech:GOLD.b933f64ea6` with `review_depth` `CLASS`. The embedded YAML
history and rendered page both carry that class-level curation note. An
ignored/hidden-inclusive exact search found no `mummified remains` label in
`data/raw/ontology_terms.tsv`, which is consistent with the class-level
lexical no-match.

The generated parent `habitatmech:GOLD.07c6babcdb` is traceable to the
immediate GOLD source path `Host-associated > Birds > Remains`.
`data/habitats/PATHS.tsv` pins that parent identifier to `remains`, and the
parent record has the same class-level `CONFIRM_UNGROUNDED` provenance.

This target is distinct from the Mammals: Human `Mummified remains` record.
Both share the same leaf label, but the Human record is minted as
`habitatmech:GOLD.7c194a46ba` from
`Host-associated > Mammals: Human > Remains > Mummified remains`, while this
record preserves the Bird host-branch context in its own minted identifier.

## Evidence

The record carries no curator-authored evidence block. Its identity is backed
by the GOLD path inventory and maintained class-level grounding decision, not
by an item-level curation decision.

The zero assertion total is supported by the raw GOLD inventory. The exact raw
row reports `organism_count = 0`, `study_count = 0`, `biosample_count = 0`,
`mixs_triad_count = 0`, `gold_triad_count = 0`, and `total_assertions = 0` for
this path, and ignored/hidden-inclusive searches for `gold.ecosystem:7500` and
`gold.ecosystem:7501` found no rows in
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or
`data/raw/gold_studies.tsv`.

No causal graph is attached to this record. Ignored/hidden-inclusive searches
found no maintained causal, history, research, or configuration overlay keyed
by `habitatmech:GOLD.b933f64ea6`, `gold.ecosystem:7500`,
`gold.ecosystem:7501`, or the exact Bird source path.

## Completeness

- The rendered page
  `pages/habitats/mummified-remains-habitatmech-gold-b933f64ea6.html`
  reflects the same minted identifier, label, category, `UNGROUNDED`
  grounding, `SEEDED` mapping status, GOLD source path, collapsed-node note,
  single broader habitat, and class-level curation event as the YAML.
- Before this report was added, an exact ignored/hidden-inclusive search for
  `Host-associated > Birds > Remains > Mummified remains` in
  `reports/yaml_record_review` found no prior exact review for this target.
- The other generated children under `Host-associated > Birds > Remains` are
  `Decomposed body`, `Fossilized remains`, `Frozen remains`, and
  `Skeletonized remains`; each remains a separate source-path child of
  `habitatmech:GOLD.07c6babcdb`.
- Empty optional slots are appropriate for the current zero-assertion source
  row. No raw side-table rows support generated environmental parameters or
  taxa, and no maintained overlay supplies causal graphs.

## Findings

| Severity | Finding | Evidence |
|---|---|---|
| Major | The record's `UNGROUNDED` status is still a class-level lexical no-match, not item-level signoff on the Bird `Mummified remains` source concept. | `curation/decisions.tsv` lists `habitatmech:GOLD.b933f64ea6` as `CONFIRM_UNGROUNDED` with `review_depth` `CLASS`, and `just worklist --status all` still ranks the record in the 953-row ungrounded backlog. |

No structural or reproducibility defects were found in the generated YAML.

## Recommended Edits

1. Item-review `habitatmech:GOLD.b933f64ea6` in `curation/decisions.tsv`.
   Inspect GOLD ecosystem nodes `7500` and `7501` and decide whether
   `Host-associated > Birds > Remains > Mummified remains` is a habitat
   concept, a term-request candidate, or narrower than any existing vendored
   term.
2. If no existing term fits, keep `CONFIRM_UNGROUNDED` at `ITEM` depth and add
   a `curation/term_requests.tsv` definition for the minted record. Use `ADD`
   parent mode to preserve the generated Birds `Remains` parent unless
   item-level review proves that parent false.

## Follow-up Checks

After item-level curation, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.b933f64ea6`
- `just validate data/habitats/host_associated/mummified_remains__76cdbf69.yaml`
- `just validate-strict data/habitats/host_associated/mummified_remains__76cdbf69.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just report --ungrounded-top 0 --out /tmp/habitatmech-report-bird-mummified-remains.tsv`
- `git diff --check`

If the item-level edit adds a term request or causal overlay, also inspect the
regenerated target to confirm the definition, parents, status, and history
entries follow from maintained inputs.

## Additional Notes

- The sibling `Skeletonized remains` record follows this target in the GOLD
  Bird `Remains` block and is still separate at
  `data/habitats/host_associated/skeletonized_remains__25008b61.yaml`.
- iModulonDB structured source checks were not applicable: the record names a
  GOLD habitat path and no genes, locus tags, regulators, pathways,
  stress-response terms, or transcriptomic datasets.
