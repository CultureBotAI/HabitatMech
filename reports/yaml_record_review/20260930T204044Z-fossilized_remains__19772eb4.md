# YAML Record Review: Fossilized remains

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/fossilized_remains__19772eb4.yaml`
- Started UTC: `2026-09-30T20:33:00Z`
- Finished UTC: `2026-09-30T20:40:44Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.76df031f74` |
| Label | `Fossilized remains` |
| Stable slug | `fossilized_remains__19772eb4` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | `habitatmech:GOLD.76df031f74` |
| Source attestation | `GOLD`, `gold.ecosystem:7586`, `Host-associated > Fish > Remains > Fossilized remains` |

The target is the generated GOLD record for the Fish-specific
`Fossilized remains` path under `Host-associated > Fish > Remains`. It has one
GOLD source attestation, one generated GOLD source-path parent, no authored
definition, no synonyms, no xrefs, no environmental parameters, no
characteristic taxa, no record-level evidence block, no datasets, no
discussions, and no causal graphs.

The record is structurally reproducible from maintained inputs. Its current
`UNGROUNDED` state comes from a class-level `CONFIRM_UNGROUNDED` row that
checked only automated lexical routes into the vendored ontology slice; it did
not item-review the Fish `Fossilized remains` source path.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/fossilized_remains__19772eb4.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/fossilized_remains__19772eb4.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206 on disk, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-fish-fossilized-remains-worklist.tsv` | Not completed; the helper produced no output and no TSV after repeated polls, then was stopped with exit code 143. The report uses the exact `curation/decisions.tsv` row for the decision-depth check instead. |
| `just report --out /tmp/habitatmech-fish-fossilized-remains-report.tsv` | Not completed; the helper emitted aggregate console sections but no TSV after repeated polls, then was stopped with exit code 143. The exact YAML and maintained source rows were inspected directly instead. |

## Identity and Grounding

The minted GOLD identity is sound. `data/raw/gold_ecosystem_paths.tsv` has the
exact source row `Host-associated > Fish > Remains > Fossilized remains` with
leaf label `Fossilized remains`, depth 4, two collapsed GOLD ecosystem node
IDs, zero organism, study, BioSample, MIxS triad, and GOLD triad counts, zero
total assertions, and source IDs `gold.ecosystem:7586|gold.ecosystem:7587`.

`data/habitats/PATHS.tsv` pins `habitatmech:GOLD.76df031f74` to
`fossilized_remains__19772eb4`, and the generated target YAML uses that
identifier and stem for exactly this Fish source path.

The target is distinct from three same-label GOLD sibling records. The Bird
path `Host-associated > Birds > Remains > Fossilized remains` is generated as
`habitatmech:GOLD.4af8939c1f` in
`data/habitats/host_associated/fossilized_remains.yaml`; the Mammals path
`Host-associated > Mammals > Remains > Fossilized remains` is generated as
`habitatmech:GOLD.c5640eadf7` in
`data/habitats/host_associated/fossilized_remains__eec3c6e8.yaml`; and the
Mammals: Human path
`Host-associated > Mammals: Human > Remains > Fossilized remains` is generated
as `habitatmech:GOLD.f1a2eca320` in
`data/habitats/host_associated/fossilized_remains__8b01c49f.yaml`. The Fish
path therefore needs its own item review even though the leaf label is shared.

The generated `UNGROUNDED` status is traceable, but only to a class-level
decision. `curation/decisions.tsv` lists `habitatmech:GOLD.76df031f74` as
`CONFIRM_UNGROUNDED` with `review_depth` `CLASS`; the embedded YAML history
and rendered page both carry that class-level note.

One plausible broader ontology term remains unresolved at item depth.
`data/raw/ontology_terms.tsv` vendors `ENVO:00002164` `fossil material`, a
solid environmental material formed by mineral replacement of organic
substances, and `data/raw/ontology_subclass_edges.tsv` places it under
`ENVO:01000814` `solid environmental material`. GOLD also used the older label
`fossil` for `ENVO:00002164` in committed MIxS triad rows for mammalian
fossilized-remains descendants such as `Coprolite` and `Paleofeces`. None of
those rows item-review the Fish `Fossilized remains` grouping node.

The single generated parent, `habitatmech:GOLD.d1de3c94cf`, is traceable to
the immediate broader GOLD source path `Host-associated > Fish > Remains`.
`data/habitats/PATHS.tsv` pins that parent identifier to
`remains__784e165d`, and the Fish `Remains` parent carries the same kind of
class-level `CONFIRM_UNGROUNDED` provenance.

## Evidence

No curator-authored evidence block is attached. This record's identity is
backed by the GOLD path inventory plus the maintained class-level grounding
decision, not by an item-level curation decision or cited habitat evidence.

The zero assertion total is supported by the raw GOLD inventory. The exact raw
row reports zero counts for all source-side assertion columns, and exact
ignored/hidden-inclusive searches for the Fish
`Host-associated > Fish > Remains > Fossilized remains` path plus
`gold.ecosystem:7586` and `gold.ecosystem:7587` found no rows in
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or
`data/raw/gold_studies.tsv`.

No causal graph is attached to this record. Exact ignored/hidden-inclusive
searches found no causal overlay, history record, research report,
configuration entry, or prior exact review keyed by
`habitatmech:GOLD.76df031f74` or the `fossilized_remains__19772eb4` stem under
`curation/causal_graphs/`, `history/`, `research/`, `conf/`, or
`reports/yaml_record_review/`.

## Completeness

The rendered page
`pages/habitats/fossilized-remains-habitatmech-gold-76df031f74.html` reflects
the same minted identifier, label, category, `UNGROUNDED` grounding,
`SEEDED` mapping status, GOLD source path, collapsed-node note, single broader
habitat, and class-level curation event as the YAML.

Exact ignored/hidden-inclusive searches covered `data/raw/`, `data/habitats/`,
`curation/`, `pages/habitats/`, `history/`, `research/`, `conf/`, and prior
YAML review reports for the Fish `Fossilized remains` identifier, exact GOLD
source IDs, exact source path, and record stem. They found no prior review
keyed by the Fish identifier or slug, no item-level decision, and no maintained
evidence-bearing overlay for this target. The only prior same-label review was
for the Birds `Fossilized remains` record and only mentioned the Fish path as a
sibling that still needed separate review.

The empty optional arrays are expected for the current generated state. The
Fish GOLD path has zero assertions, the three GOLD side tables have no rows
for this path, and no maintained causal graph overlay supplies any graph to
merge into the record.

The current corpus exposes a plausible broader fossil-material term. Until an
item-level curator compares that term against the exact Fish source path, the
record is incomplete as a reviewed `UNGROUNDED` minted concept.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The Fish `Fossilized remains` source concept is still backed only by a class-level `CONFIRM_UNGROUNDED` row, so the generated `UNGROUNDED` state has not been item-reviewed against a plausible broader fossil-material candidate. | `curation/decisions.tsv` lists `habitatmech:GOLD.76df031f74` with `review_depth` `CLASS`; `data/raw/gold_ecosystem_paths.tsv` shows a real Fish source path with two upstream ecosystem node IDs; `data/raw/ontology_terms.tsv` vendors `ENVO:00002164` `fossil material`, which the lexical no-match row did not inspect for this path. | `curation/decisions.tsv`; if the record stays minted, `curation/term_requests.tsv`. |

No blockers or minor findings were found.

## Recommended Edits

1. Item-review `habitatmech:GOLD.76df031f74` in
   `curation/decisions.tsv`. Inspect GOLD ecosystem nodes `7586` and `7587`
   and decide whether `Host-associated > Fish > Remains > Fossilized remains`
   denotes fossilized fish remains as a microbial habitat or is only an empty
   GOLD grouping node.
2. Compare `ENVO:00002164` `fossil material` against the exact Fish
   `Fossilized remains` concept. If it is strictly broader, use
   `GROUND_AS_PARENT`; do not ground the Fish concept exactly to `fossil
   material` unless item review establishes they are equivalent.
3. If no existing term fits exactly or broadly enough, keep the GOLD record
   minted, add a `curation/term_requests.tsv` definition for the Fish
   `Fossilized remains` concept, and use `ADD` parent mode unless item review
   proves the generated Fish `Remains` parent false.

## Follow-up Checks

After item-level curation, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.76df031f74`
- `just validate data/habitats/host_associated/fossilized_remains__19772eb4.yaml`
- `just validate-strict data/habitats/host_associated/fossilized_remains__19772eb4.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `git diff --check`

If the item-level edit adds a term request or causal overlay, also inspect the
regenerated target YAML and rendered page to confirm that generated fields
follow from maintained inputs.

## Additional Notes

- iModulonDB structured source checks were not applicable: the record names a
  GOLD habitat path and no genes, locus tags, regulators, pathways,
  stress-response terms, or transcriptomic datasets.
- The prior Bird `Fossilized remains` report reviews
  `habitatmech:GOLD.4af8939c1f`, not this Fish target. Same-label same-depth
  GOLD leaves remain distinct whenever the source path scopes them to
  different host branches.
