# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/myocardial_abscess.yaml`
- Started UTC: 2026-09-28T10:02:23Z
- Finished UTC: 2026-09-28T10:02:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4cc5effc74` |
| Label | `Myocardial abscess` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NOT_APPLICABLE` |
| Mapping status | `REVIEWED` |
| Generated path | `data/habitats/host_associated/myocardial_abscess.yaml` |
| GOLD path | `Host-associated > Mammals: Human > Circulatory system > Heart > Myocardial abscess` |
| Locked slug | `data/habitats/PATHS.tsv:1855` maps `habitatmech:GOLD.4cc5effc74` to `myocardial_abscess` |

The target is a generated GOLD-only record for the Mammals: Human myocardial
abscess source path. It has one GOLD source attestation, one generated
source-path parent, no definition, no synonyms, no xrefs, no environmental
parameters, no characteristic taxa, no record-local evidence, no causal graphs,
no discussions, and no datasets.

The generated YAML is byte-reproducible from committed inputs. Future fixes
belong in maintained curation inputs, not in
`data/habitats/host_associated/myocardial_abscess.yaml` or `pages/`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/myocardial_abscess.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/myocardial_abscess.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows; wrote `reports/instance_validation_failures.tsv`. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just verify-corpus` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-myocardial-abscess-worklist.tsv` | Passed; wrote 953 ungrounded rows. `habitatmech:GOLD.4cc5effc74` is already `REVIEWED` / `NOT_APPLICABLE`, so it is outside the ungrounded worklist. |
| `just report --out /tmp/habitatmech-myocardial-abscess-report.tsv` | Passed; wrote the 3206-record corpus TSV and listed `habitatmech:GOLD.4cc5effc74` at row 1855 with `NOT_APPLICABLE`, `REVIEWED`, one source, one assertion, one parent, no parameters, no taxa, and no causal graphs. |

No validator was skipped.

## Identity and Grounding

The minted identity and GOLD source attestation match the raw path inventory:

- `data/raw/gold_ecosystem_paths.tsv:1066` is the exact raw row for
  `Host-associated > Mammals: Human > Circulatory system > Heart > Myocardial
  abscess`. It records leaf label `Myocardial abscess`, depth `5`, one
  collapsed GOLD ecosystem node, one organism assertion, zero study
  assertions, zero biosample assertions, one total assertion, and node id
  `gold.ecosystem:6354`.
- `data/habitats/PATHS.tsv:1855` pins the generated identifier
  `habitatmech:GOLD.4cc5effc74` to slug `myocardial_abscess`, matching the
  reviewed YAML path.
- `curation/decisions.tsv:495` has the only target-specific maintained
  decision. It marks `habitatmech:GOLD.4cc5effc74` as `NOT_APPLICABLE` at
  `ITEM` depth.

The generated `parent_habitats` edge also follows current inputs.
`data/raw/gold_ecosystem_paths.tsv:681` has the immediate broader GOLD path
`Host-associated > Mammals: Human > Circulatory system > Heart` with two
collapsed node ids, and `data/habitats/PATHS.tsv:2236` maps that path to
`habitatmech:GOLD.805ee181bd` / `heart__8efd4433`. That parent is still a
seeded `NARROW` record under `UBERON:0000948` `heart`.

The open problem is the reviewed `NOT_APPLICABLE` decision. The decision note
says the GOLD leaf names "a disease, an intervention, a sampling artefact or a
no-value filler rather than a place", but it does not choose which of those
four explanations is true for a myocardial abscess, and it does not explain
why this site-specific abscess is outside HabitatMech while several plain GOLD
`Abscess` records are accepted as habitats narrower than the generic
`mesh:D000038` `Abscess` term. That broader term is present in the vendored
slice at `data/raw/ontology_terms.tsv:13554`.

The inconsistency is bigger than this one row. The nearby
`Host-associated > Mammals: Human > Muscular system > Skeletal muscle > Muscle
abscess` GOLD path is attested by `gold.ecosystem:6353` and has the same
templated `NOT_APPLICABLE` rationale at `curation/decisions.tsv:775`. GOLD
also has plain `Abscess` leaves under skin, nasal cavity, abdominal/peritoneal
cavity, spinal cord, brain, joint capsule, and soft tissues; generated records
for most of those paths retain minted identities and carry `mesh:D000038` as a
broader parent.

## Evidence

| Claim | Nearest source | Review |
|---|---|---|
| The record denotes the GOLD path `Host-associated > Mammals: Human > Circulatory system > Heart > Myocardial abscess`. | `data/raw/gold_ecosystem_paths.tsv:1066` lists the same canonical path and leaf label; the generated YAML repeats both. | Supported exactly. |
| The source attestation uses `gold.ecosystem:6354`. | The raw aggregate row lists a single ecosystem node id, `gold.ecosystem:6354`. | Supported exactly. |
| The source attestation records one organism assertion. | The raw aggregate row records `organism_count` and `total_assertions` as `1`, while `study_count` and `biosample_count` are `0`. | Supported exactly. |
| The generated `NOT_APPLICABLE` status has item-level curation backing. | `curation/decisions.tsv:495` is keyed to the exact target identifier and has `review_depth` `ITEM`. | Supported structurally; the rationale is under-supported semantically. |
| `Myocardial abscess` is not a microbial habitat. | The maintained note gives a generic abscess-family exclusion that does not distinguish myocardial abscesses from accepted path-specific plain abscess records under `mesh:D000038`, or from other abscess rows already flagged for reopening. | Unresolved until item review. |

The target has no causal graph overlay. Ignored/hidden-inclusive exact searches
of `curation`, `history`, `research`, `reports`, and the committed raw GOLD
side tables for `habitatmech:GOLD.4cc5effc74`, `gold.ecosystem:6354`,
`myocardial_abscess`, and the exact Mammals: Human GOLD path found the raw
GOLD ecosystem row and the exact decision row, but no target-specific
biosample row, triad row, study row, causal overlay, authored definition,
term-request row, history file, research report, or prior exact YAML review.

## Completeness

The generated YAML is structurally complete for its current input state: it
records the exact GOLD path, the GOLD node id, the GOLD assertion count, the
generated source-path parent, the item-level `NOT_APPLICABLE` history event,
and the source-seeded history event.

Its empty definition, definition source, environmental-parameter,
characteristic-taxon, evidence, causal-graph, discussion, and dataset slots are
acceptable for a record currently excluded as `NOT_APPLICABLE`.

The consequential gap is the maintained curation decision. If an item-level
abscess-family pass confirms that `Myocardial abscess` denotes a physical
myocardial abscess habitat, `curation/decisions.tsv` should replace the
current row with a `GROUND_AS_PARENT` row targeting `mesh:D000038` `Abscess`.
If the concept really is a non-habitat disease name rather than an abscess
site, the `NOT_APPLICABLE` row should be kept but rewritten with a
target-specific explanation that distinguishes it from accepted site-specific
plain `Abscess` GOLD leaves.

Ignored/hidden-inclusive exact searches covered `data/habitats`, `data/raw`,
`curation`, `history`, `research`, `reports`, `pages/habitats`, and
`data/habitats/PATHS.tsv`. They found the target YAML, the path lock, the raw
GOLD row, the decision row, the Heart source-path parent, the sibling Muscle
abscess decision, generated pages, and contextual abscess-family reviews, but
no target-specific causal overlay, term request, history record, raw research
report, or prior exact YAML review report.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The `NOT_APPLICABLE` decision for `Myocardial abscess` needs reopening or a target-specific justification. The current item-level row uses the same broad "disease, intervention, sampling artefact or no-value filler" rationale as other named abscess exclusions, but it does not explain why a myocardial abscess source concept is non-habitat while path-specific plain GOLD `Abscess` leaves are retained as microbial habitats narrower than `mesh:D000038`. | `curation/decisions.tsv:495` marks `habitatmech:GOLD.4cc5effc74` `NOT_APPLICABLE`; `data/raw/gold_ecosystem_paths.tsv:1066` shows an attested GOLD myocardial abscess path with one organism assertion; `data/raw/ontology_terms.tsv:13554` vendors `mesh:D000038` `Abscess`; plain site-specific GOLD `Abscess` records under skin, nasal cavity, spinal cord, brain, joint capsule, and soft tissues already keep minted identities and `mesh:D000038` as a broader parent. | `curation/decisions.tsv` |

No blockers or minor findings.

## Recommended Edits

1. Item-review `habitatmech:GOLD.4cc5effc74` as part of the same
   abscess-family pass that rechecks the similar `Muscle abscess`, skin
   `Abscess: Furuncle/Boil`, and skin `Abscess: Pilonidal sinus` rows.
2. If `Myocardial abscess` denotes a myocardial abscess habitat rather than
   only a disease grouping, replace `curation/decisions.tsv:495` with a
   `GROUND_AS_PARENT` decision targeting `mesh:D000038` `Abscess`, with
   `grounding_status: NARROW`, `review_depth: ITEM`, and a note that quotes
   the exact GOLD path.
3. If the concept remains `NOT_APPLICABLE`, keep the decision but replace the
   templated four-way note with an explanation specific to this source path
   and its contrast with retained site-specific `Abscess` records.

## Follow-up Checks

After item-level curation, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.4cc5effc74`
- `just validate data/habitats/host_associated/myocardial_abscess.yaml`
- `just validate-strict data/habitats/host_associated/myocardial_abscess.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus`
- `just report --out /tmp/habitatmech-myocardial-abscess-report.tsv`
- `git diff --check`

If the item-level edit changes this path to `GROUND_AS_PARENT`, inspect the
regenerated record to confirm that it keeps the minted identifier, keeps the
Heart source-path parent, adds `mesh:D000038` as a broader parent, and changes
its GOLD source attestation to `skos:narrowMatch`.

## Additional Notes

This report covers only `habitatmech:GOLD.4cc5effc74`, the Mammals: Human
myocardial abscess record. `Muscle abscess` and other named abscess records
have distinct generated identifiers and should be reviewed separately.
