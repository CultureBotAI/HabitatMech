# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/invertebrates.yaml`
- Started UTC: 2026-09-28T11:17:46Z
- Finished UTC: 2026-09-28T11:17:46Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Record path | `data/habitats/host_associated/invertebrates.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4d792ac724` |
| Label | `invertebrate-associated environment` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `REVIEWED` |
| Parent habitats | `ENVO:01001000`, `ENVO:01001002` |
| Maintained owner | Generated from `data/raw/gold_ecosystem_paths.tsv`, `curation/decisions.tsv`, `curation/term_requests.tsv`, and `data/habitats/PATHS.tsv`; do not hand-edit this YAML. |

The target is the reviewed GOLD record for `Host-associated > Invertebrates`.
`data/habitats/PATHS.tsv` maps `habitatmech:GOLD.4d792ac724` to the
`invertebrates` slug; the public page moved to the current
`invertebrate-associated-environment-habitatmech-gold-4d792ac724` URL with a
retired redirect for the old source-label URL.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/invertebrates.yaml` | Pass. `linkml-validate` reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/invertebrates.yaml` | Pass. Strict closed-schema validation scanned 1 file with 0 files in error and 0 total error rows. |
| `just validate-causal curation/causal_graphs/<overlay>.yaml` | Not applicable. Ignored- and hidden-file-inclusive searches found no maintained causal-graph overlay for `habitatmech:GOLD.4d792ac724`. |
| `just validate-causal-all` | Pass. All 32 causal-graph curation files and 32 graphs validated. |
| Reference validator | Not applicable. The generated record has no `evidence`, `datasets`, or `causal_graphs` references. |
| `just term-requests-check` | Pass. The generated term-request table is current at 109 terms. |
| `just validate-history` | Pass. 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus` | Pass. 3,206 expected records were present with 0 missing, 0 extra, and 0 differing generated YAML files. |
| `just worklist --status all --out /tmp/habitatmech-invertebrates-worklist.tsv` | Pass. Wrote 953 ungrounded rows and listed this reviewed term-request record with 621 GOLD organism assertions. |
| `just report --out /tmp/habitatmech-invertebrates-report.tsv` | Pass. Wrote the 3,206-record corpus TSV and listed this record at row 1858 as `UNGROUNDED`, `REVIEWED`, GOLD-only, 621 assertions, two parents, no parameters, no taxa, and no causal graphs. |
| `git diff --check` | Pass after report creation. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes GOLD's bare `Host-associated > Invertebrates` source concept. | `data/raw/gold_ecosystem_paths.tsv` has one exact row for `Host-associated > Invertebrates` with leaf label `Invertebrates`, depth 2, `gold_node_count=4`, `organism_count=621`, `total_assertions=621`, and node IDs including `gold.ecosystem:3374`. The generated source attestation repeats the same path, first node ID, source label, and 621 `ORGANISM` assertions. | Supported exactly. |
| The minted HabitatMech identifier is correct. | GOLD host labels are source concepts whose whole-organism/taxon strings are not habitat identities. `curation/decisions.tsv` keeps `habitatmech:GOLD.4d792ac724` minted with `CONFIRM_UNGROUNDED`, attaches `ENVO:01001002` only as a broader parent, and records `review_depth=ITEM`. | Supported. |
| The authored label and definition are generated from the maintained term request. | `curation/term_requests.tsv` requests `invertebrate-associated environment` with definition `An environmental system determined by an invertebrate.`, exact synonym `Invertebrates`, parent `ENVO:01001002`, and `parent_mode=ADD`; the generated YAML carries the same label, definition, and synonym. | Supported exactly. |
| The inherited parents are strictly broader. | `ENVO:01001002` `animal-associated environment` is the requested genus for the invertebrate host environment. `ENVO:01001000` `environmental system determined by an organism` is the generated record for the source-path `Host-associated` parent and is the asserted ENVO parent of `ENVO:01001002`. | Supported. |
| `ENVO:01001176` is correctly not used as the identity or a parent. | The vendored slice defines `ENVO:01001176` as an aquatic-invertebrate-associated environment and asserts it under both `ENVO:01001002` and `ENVO:01001055` `environment associated with an animal part or small animal`; the curated term request deliberately keeps the broader `ENVO:01001002` genus because GOLD's `Invertebrates` node does not assert an aquatic host and whole adult invertebrate hosts are not necessarily animal parts or small animals. | Supported. |
| `mapping_status: REVIEWED` follows from maintained inputs. | The sole GOLD source concept has an `ITEM` decision row, and the generated history includes both the `CONFIRM_UNGROUNDED` decision from `curation/decisions.tsv` and the `DEFINED` event from `curation/term_requests.tsv`. | Supported. |

## Evidence

| Assertion | Evidence | Assessment |
|---|---|---|
| The source row has 621 organism assertions and no study or biosample assertions on the grouping row. | The exact `data/raw/gold_ecosystem_paths.tsv` row has `organism_count=621`, `study_count=0`, `biosample_count=0`, and `total_assertions=621`. | Supported exactly. |
| The source path is a broad host bucket with narrower GOLD descendants. | The GOLD raw path inventory also contains `Host-associated > Invertebrates > Cnidaria`, `Nematoda`, `Echinodermata`, `Platyhelminthes`, `Bryozoans`, `Ctenophora`, `Tunicates`, and anatomical descendants such as coral `Tissue` and `Mucus`. | Supported as source hierarchy context only; child paths keep their own records and do not alter this record's direct assertion count. |
| A committed deep-research report supports the term-requested definition and near-miss choices. | `reports/habitat_research_manifest.tsv` records a successful report for `habitatmech:GOLD.4d792ac724` at `research/habitats/host_associated/invertebrates-habitatmech-gold-4d792ac724-deep-research-claude_code.md`; the report recommends `invertebrate-associated environment`, uses `animal-associated environment` as the genus, and rejects `ENVO:01001176` as too narrow. | Supported. The maintained term-request row is the generated input; the research report is supporting curator evidence. |
| The reviewed GOLD source concept is still an ungrounded term-request record. | `just report` lists the row as `UNGROUNDED`, `REVIEWED`, `has_definition=True`, and sourced only by GOLD. `just worklist --status all` keeps it in the ENVO term-request cohort with `decided=TRUE`, not in the class-level sweep. | Supported. |

No snippet or citation mismatch was present because the generated target has no
claim-level `evidence` entries or causal graph edges.

## Completeness

The record is complete enough for its current reviewed state. The exact GOLD
source concept has an item-level decision, a maintained novel-term definition,
an exact source-label synonym, strictly broader parents, a committed
deep-research report, and generated curation history for both maintained rows.
It correctly leaves environmental parameters, characteristic taxa, datasets,
record-level evidence, and causal graphs empty: the GOLD source path supplies
host-bucket provenance, but no maintained input for this exact record asserts a
mechanism, characteristic organism, or physicochemical parameter.

Ignored- and hidden-file-inclusive searches covered `curation/causal_graphs`,
`history`, `research/habitats`, `reports/yaml_record_review`,
`reports/habitat_research_manifest.tsv`, `curation/term_requests.tsv`,
`curation/decisions.tsv`, `data/raw`, `data/habitats`, and `pages/habitats` for
`habitatmech:GOLD.4d792ac724`, `gold.ecosystem:3374`, the exact GOLD path, the
current label, and the `invertebrates` slug. They found the maintained
decision, term request, deep-research report and manifest row, generated target
and page, old page redirect, raw GOLD rows, and sibling review mentions, but no
prior exact `invertebrates` YAML review report, no causal-graph overlay, and no
append-only history item for this record.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

| Check | Purpose |
|---|---|
| None required | The existing item-level decision, term request, generated target, and validation outputs agree. |

## Additional Notes

- iModulonDB structured adapters were not applicable because this GOLD habitat
  row names no gene, locus, regulator, pathway, stress response, trait, or
  transcriptomics dataset.
- The BacDive `Invertebrates-Other` record is a related residual bucket and a
  possible future co-attestor, as described in the committed deep-research
  report. That is a merge-design question for
  `habitatmech:BACDIVE.e864a16f03`, not a defect in this GOLD record.
