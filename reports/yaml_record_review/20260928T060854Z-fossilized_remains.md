# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/fossilized_remains.yaml`
- Started UTC: 2026-09-28T06:08:54Z
- Finished UTC: 2026-09-28T06:08:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4af8939c1f` |
| Label | `Fossilized remains` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated path | `data/habitats/host_associated/fossilized_remains.yaml` |
| GOLD path | `Host-associated > Birds > Remains > Fossilized remains` |
| Locked slug | `data/habitats/PATHS.tsv:1846` maps `habitatmech:GOLD.4af8939c1f` to `fossilized_remains` |

The target is a generated GOLD-only record for the Birds branch of the GOLD
`Fossilized remains` paths. It has one GOLD source attestation, one generated
source-path parent, no definition, no synonyms, no xrefs, no environmental
parameters, no characteristic taxa, no record-local evidence, no causal graphs,
no discussions, and no datasets.

The generated YAML is byte-reproducible from committed inputs. Future fixes
belong in maintained curation inputs, not in
`data/habitats/host_associated/fossilized_remains.yaml` or `pages/`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/fossilized_remains.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/fossilized_remains.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows; wrote `reports/instance_validation_failures.tsv`. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-fossilized-remains-worklist.tsv` | Passed; wrote 953 ungrounded rows and listed `habitatmech:GOLD.4af8939c1f` at row 557. |
| `just report --out /tmp/habitatmech-fossilized-remains-report.tsv` | Passed; wrote the 3206-record corpus TSV and listed `habitatmech:GOLD.4af8939c1f` at row 1846 with no definition, one parent, no parameters, no taxa, and no causal graphs. |
| `git diff --cached --check` | Passed; no staged whitespace or patch errors. |

No validator was skipped.

## Identity and Grounding

The minted identity and GOLD source attestation match the raw path inventory:

- `data/raw/gold_ecosystem_paths.tsv:1896` is the exact raw row for `Host-associated > Birds > Remains > Fossilized remains`. It records leaf label `Fossilized remains`, depth `4`, two collapsed GOLD ecosystem node ids, zero organism assertions, zero study assertions, zero biosample assertions, zero total assertions, and node ids `gold.ecosystem:7504|gold.ecosystem:7505`.
- `data/habitats/PATHS.tsv:1846` pins the generated identifier `habitatmech:GOLD.4af8939c1f` to slug `fossilized_remains`, matching the reviewed YAML path.
- `curation/decisions.tsv:491` has a `CONFIRM_UNGROUNDED` row for this exact minted identifier, but its `review_depth` is only `CLASS`.

The generated parent follows the immediate GOLD source path, not an item-level
curator assertion. `data/raw/gold_ecosystem_paths.tsv:282` has the broader path
`Host-associated > Birds > Remains`, and `data/habitats/PATHS.tsv:1326` maps
that parent concept to `habitatmech:GOLD.07c6babcdb` / `remains`. That parent
also has only a class-level `CONFIRM_UNGROUNDED` row at
`curation/decisions.tsv:140`.

The existing `UNGROUNDED` status is not item-level signoff. The class-level
sweep only established that the label did not match the vendored slice through
the automated lexical routes documented in
`docs/HARMONIZATION.md#class-level-sweep`; it explicitly did not decide whether
the GOLD source concept is a habitat, a term-request candidate, or narrower than
a vendored term.

One plausible broader ontology term remains unresolved at item depth:
`data/raw/ontology_terms.tsv:7256` vendors `ENVO:00002164` with canonical label
`fossil material`, and `data/raw/ontology_subclass_edges.tsv:5367` places it
under `ENVO:01000814` solid environmental material. GOLD also used the older
label `fossil` for `ENVO:00002164` in committed MIxS-triad rows for mammalian
fossilized-remains descendants such as `Coprolite` and `Paleofeces`, while
`just report` now treats that as the known upstream/slice label mismatch
`fossil` versus `fossil material`. None of those rows item-review the Birds
`Fossilized remains` grouping node.

## Evidence

| Claim | Nearest source | Review |
|---|---|---|
| The record denotes the GOLD path `Host-associated > Birds > Remains > Fossilized remains`. | `data/raw/gold_ecosystem_paths.tsv:1896` lists the same canonical path and leaf label; the generated YAML repeats both. | Supported exactly. |
| The source attestation uses `gold.ecosystem:7504` and notes that two GOLD ecosystem node ids share the path. | The raw aggregate row lists `gold.ecosystem:7504|gold.ecosystem:7505`; the seeder records the first id and a collapsed-node note. | Supported exactly. |
| The source attestation omits `assertion_count` and `assertion_unit`. | The raw aggregate row records `organism_count`, `study_count`, `biosample_count`, and `total_assertions` as `0`. | Supported exactly. |
| `Fossilized remains` is narrower than the Birds `Remains` node. | `data/raw/gold_ecosystem_paths.tsv:282` and `:1896` show the exact parent and child paths, and `data/habitats/PATHS.tsv:1326` pins the Birds `Remains` identifier emitted in `parent_habitats`. | Supported as a generated source-path edge. |
| No vendored ontology term fits the Birds `Fossilized remains` concept. | The current decision is a class-level lexical no-match row. It did not inspect the GOLD path or candidate broader material terms such as `ENVO:00002164`. | Unresolved until item review. |

The target has no causal graph overlay. Ignored/hidden-inclusive exact searches
of `curation/causal_graphs`, `curation/term_requests.tsv`,
`curation/term_requests_excluded.tsv`, `curation/external_xrefs.tsv`,
`history`, `research`, and `reports/habitat_research_manifest.tsv` for
`habitatmech:GOLD.4af8939c1f`, `gold.ecosystem:7504`,
`gold.ecosystem:7505`, `Fossilized remains`, `fossilized_remains`, and the
exact Birds GOLD path found no maintained overlay, authored definition, term
request, exclusion, external xref, history file, or research report for this
target.

## Completeness

The generated YAML is structurally complete for its current input state: it
records the exact GOLD path, the first collapsed node id, the collapsed-node
note, the immediate GOLD parent, and generated curation-history entries for the
class-level `CONFIRM_UNGROUNDED` row and the source seed.

Its empty definition and definition source are not enough for a reviewed,
minted habitat record. If item-level curation keeps the source concept minted
and `CONFIRM_UNGROUNDED`, `curation/term_requests.tsv` should define a
bird-fossilized-remains associated environment or another label that matches
the exact source meaning. If item review instead finds `ENVO:00002164` is a
true broader term, `curation/decisions.tsv` should use `GROUND_AS_PARENT` and
the generated record should move to `NARROW`.

The empty environmental-parameter, characteristic-taxon, evidence, causal-graph,
discussion, and dataset slots are acceptable today. The exact Birds
`Fossilized remains` path has no direct rows in `data/raw/gold_studies.tsv`,
`data/raw/gold_path_biosamples.tsv`, or `data/raw/gold_path_triads.tsv`; an
ignored/hidden-inclusive fixed-string search for
`Host-associated > Birds > Remains` across the committed raw GOLD side tables
found only the GOLD ecosystem-path rows for the parent and depth-4 sibling
grouping nodes.

Ignored/hidden-inclusive exact searches covered `data/habitats`, `data/raw`,
`curation`, `history`, `research`, `reports`, `conf`, `src`, `tests`, `docs`,
`.claude`, `README.md`, and `justfile`. They found the target YAML, the path
lock, the raw GOLD row, the class-level decision, the Birds parent record, and
the Fish, Mammals, and Mammals: Human sibling `Fossilized remains` records, but
no item-level decision, term request, history record, causal overlay,
target-specific research report, or prior exact YAML review report for
`habitatmech:GOLD.4af8939c1f`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The Birds `Fossilized remains` source concept is still backed only by a class-level `CONFIRM_UNGROUNDED` row, so the generated `UNGROUNDED` state has not been item-reviewed against a plausible fossil-material parent. | `curation/decisions.tsv:491` has `review_depth` `CLASS`; `data/raw/gold_ecosystem_paths.tsv:1896` shows a real GOLD path with two upstream ecosystem node ids; `data/raw/ontology_terms.tsv:7256` vendors `ENVO:00002164` `fossil material` as a candidate broader term that the class sweep did not inspect. | `curation/decisions.tsv`; if the record stays minted, `curation/term_requests.tsv`. |

No blockers or minor findings.

## Recommended Edits

1. Item-review `habitatmech:GOLD.4af8939c1f` in `curation/decisions.tsv`.
   Inspect GOLD ecosystem nodes `7504` and `7505` and decide whether
   `Host-associated > Birds > Remains > Fossilized remains` denotes
   fossilized bird remains as a microbial habitat or is only an empty GOLD
   grouping node.
2. Compare `ENVO:00002164` `fossil material` against the exact Birds
   `Fossilized remains` concept. If it is strictly broader, use
   `GROUND_AS_PARENT`; do not ground the Birds concept exactly to `fossil
   material` unless item review establishes they are equivalent.
3. If no existing term is broader enough and precise enough, keep
   `CONFIRM_UNGROUNDED` at `ITEM` depth and add a
   `curation/term_requests.tsv` definition for the minted record. Use `ADD`
   parent mode to preserve the source-derived Birds `Remains` parent unless
   item-level review proves that parent false.

## Follow-up Checks

After item-level curation, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.4af8939c1f`
- `just validate data/habitats/host_associated/fossilized_remains.yaml`
- `just validate-strict data/habitats/host_associated/fossilized_remains.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just report --out /tmp/habitatmech-fossilized-remains-report.tsv`
- `git diff --check`

If the item-level edit adds a term request or causal overlay, also inspect the
regenerated target to confirm the definition, parents, status, and history
entries follow from maintained inputs.

## Additional Notes

This report covers only `habitatmech:GOLD.4af8939c1f`, the Birds
`Fossilized remains` record. Three same-label siblings exist at
`Host-associated > Fish > Remains > Fossilized remains`,
`Host-associated > Mammals > Remains > Fossilized remains`, and
`Host-associated > Mammals: Human > Remains > Fossilized remains`; they have
distinct generated identifiers and should be reviewed separately.
