# YAML Record Review: Skeletonized remains

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/skeletonized_remains__68ea2ec4.yaml`
- Started UTC: `2026-09-30T20:00:00Z`
- Finished UTC: `2026-09-30T20:10:05Z`
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.a843dbe12a` |
| Label | `Skeletonized remains` |
| Stable slug | `skeletonized_remains__68ea2ec4` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Source concept | `habitatmech:GOLD.a843dbe12a` |
| Source attestation | `GOLD`, `gold.ecosystem:7588`, `Host-associated > Fish > Remains > Skeletonized remains` |

The target is the generated GOLD record for the Fish-specific
`Skeletonized remains` path under `Host-associated > Fish > Remains`. It has
one GOLD source attestation, one generated GOLD source-path parent, no authored
definition, no synonyms, no environmental parameters, no characteristic taxa,
no record-level evidence block, no datasets, no discussions, and no causal
graphs.

The record is structurally reproducible from maintained inputs. Its current
`UNGROUNDED` state comes from a class-level `CONFIRM_UNGROUNDED` row that
checked only automated lexical routes into the vendored ontology slice; it did
not item-review the Fish `Skeletonized remains` source path.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/skeletonized_remains__68ea2ec4.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/skeletonized_remains__68ea2ec4.yaml` | Passed; 1 file scanned, 0 files with errors, 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206 on disk, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitat_worklist_fish_skeletonized.tsv` | Not completed; the helper produced no output after repeated polls and was stopped with exit code 143, so the report uses the exact `curation/decisions.tsv` row for the decision-depth check instead of a backlog rank. |

## Identity and Grounding

The minted GOLD identity is sound. `data/raw/gold_ecosystem_paths.tsv` has the
exact source row `Host-associated > Fish > Remains > Skeletonized remains`
with leaf label `Skeletonized remains`, depth 4, two collapsed GOLD ecosystem
node IDs, zero organism, study, BioSample, MIxS triad, and GOLD triad counts,
zero total assertions, and source IDs `gold.ecosystem:7588|gold.ecosystem:7589`.

`data/habitats/PATHS.tsv` pins `habitatmech:GOLD.a843dbe12a` to
`skeletonized_remains__68ea2ec4`, and the generated target YAML uses that
identifier and stem for exactly this Fish source path.

The target is distinct from the same-label Birds and Mammals: Human records.
The Bird path `Host-associated > Birds > Remains > Skeletonized remains` is
generated as `habitatmech:GOLD.ab6354f42c` in
`data/habitats/host_associated/skeletonized_remains__25008b61.yaml`, and the
Mammals: Human path
`Host-associated > Mammals: Human > Remains > Skeletonized remains` is
generated as `habitatmech:GOLD.2f62ba7993` in
`data/habitats/host_associated/skeletonized_remains.yaml`. The Fish source
path therefore needs its own item review even though the leaf label is shared.

The generated `UNGROUNDED` status is traceable, but only to a class-level
decision. `curation/decisions.tsv` lists `habitatmech:GOLD.a843dbe12a` as
`CONFIRM_UNGROUNDED` with `review_depth` `CLASS`; the embedded YAML history
and rendered page both carry that class-level note.

The vendored ontology slice exposes terms that were not adjudicated by the
class-level lexical no-match. `data/raw/ontology_terms.tsv` includes
`ENVO:00002033` `carcass` for the dead body of an animal, `BTO:0001965`
`carcass` for a dead body, `BTO:0000140` `bone` for most vertebrate skeleton
connective tissue, and skeletal-system or exoskeleton terms. Those are not
exact identity matches for a whole Fish `Skeletonized remains` habitat, but
they are plausible broader or related candidates that an item-level curator
should explicitly accept or reject before leaving this record `UNGROUNDED`.

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
`Host-associated > Fish > Remains > Skeletonized remains` path plus
`gold.ecosystem:7588` and `gold.ecosystem:7589` found no rows in
`data/raw/gold_path_biosamples.tsv`, `data/raw/gold_path_triads.tsv`, or
`data/raw/gold_studies.tsv`.

No causal graph is attached to this record. Exact ignored/hidden-inclusive
searches found no causal overlay, history record, research report,
configuration entry, or prior exact review keyed by
`habitatmech:GOLD.a843dbe12a` or the `skeletonized_remains__68ea2ec4` stem
under `curation/causal_graphs/`, `history/`, `research/`, `conf/`, or
`reports/yaml_record_review/`.

## Completeness

The rendered page
`pages/habitats/skeletonized-remains-habitatmech-gold-a843dbe12a.html`
reflects the same minted identifier, label, category, `UNGROUNDED` grounding,
`SEEDED` mapping status, GOLD source path, collapsed-node note, single broader
habitat, and class-level curation event as the YAML.

Exact ignored/hidden-inclusive searches covered `data/raw/`, `data/habitats/`,
`curation/`, `pages/habitats/`, `history/`, `research/`, `conf/`, and prior
YAML review reports for the Fish `Skeletonized remains` identifier, exact
GOLD source IDs, exact source path, and record stem. They found no prior exact
review report, no item-level decision, and no maintained evidence-bearing
overlay for this target.

The empty optional arrays are expected for the current generated state. The
Fish GOLD path has zero assertions, the three GOLD side tables have no rows
for this path, and no maintained causal graph overlay supplies any graph to
merge into the record.

The current corpus exposes plausible broader dead-body and skeletal terms.
Until an item-level curator compares those terms against the exact Fish
source path, the record is incomplete as a reviewed `UNGROUNDED` minted
concept.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The Fish `Skeletonized remains` source concept is still backed only by a class-level `CONFIRM_UNGROUNDED` row, so the generated `UNGROUNDED` state has not been item-reviewed against plausible carcass, skeletal, or bone parents. | `curation/decisions.tsv` lists `habitatmech:GOLD.a843dbe12a` with `review_depth` `CLASS`; `data/raw/gold_ecosystem_paths.tsv` shows a real Fish source path with two upstream ecosystem node IDs; `data/raw/ontology_terms.tsv` vendors `ENVO:00002033` and `BTO:0001965` `carcass`, `BTO:0000140` `bone`, and skeletal-system terms that the lexical no-match row did not inspect for this path. | `curation/decisions.tsv`; if the record stays minted, `curation/term_requests.tsv`. |

No blocker or minor findings were found.

## Recommended Edits

1. Item-review `habitatmech:GOLD.a843dbe12a` in
   `curation/decisions.tsv`. Compare the exact
   `Host-associated > Fish > Remains > Skeletonized remains` source concept
   against existing carcass and skeletal or bone terms, decide whether any
   term is a true parent, and replace the class-level row with an `ITEM`-depth
   row.
2. If no existing term fits exactly or broadly enough, keep the GOLD record
   minted, add a `curation/term_requests.tsv` definition for the Fish
   `Skeletonized remains` concept, and use `ADD` parent mode unless item
   review proves the generated Fish `Remains` parent false.

## Follow-up Checks

After the maintained inputs change, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.a843dbe12a`
- `just validate data/habitats/host_associated/skeletonized_remains__68ea2ec4.yaml`
- `just validate-strict data/habitats/host_associated/skeletonized_remains__68ea2ec4.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `git diff --check`

If the item-level edit changes the definition, broader parents, curation
status, or graph overlays, also inspect the regenerated target YAML and
rendered page to confirm that the generated fields follow from maintained
inputs.

## Additional Notes

- iModulonDB structured source checks were not applicable: the record names a
  GOLD habitat path and no genes, locus tags, regulators, pathways,
  stress-response terms, or transcriptomic datasets.
- The prior Bird `Skeletonized remains` report reviews
  `habitatmech:GOLD.ab6354f42c`, not this Fish target. Same-label same-depth
  GOLD leaves remain distinct whenever the source path scopes them to
  different host branches.
