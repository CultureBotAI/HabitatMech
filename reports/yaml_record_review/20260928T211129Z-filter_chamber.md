# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/filter_chamber.yaml`
- Started UTC: 2026-09-28T21:11:29Z
- Finished UTC: 2026-09-28T21:11:29Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| File | `data/habitats/host_associated/filter_chamber.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.6e59a6cbb1` |
| Label | `Filter chamber` |
| Category | `HOST_ASSOCIATED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Maintained/generated | Generated from `data/raw/` plus curation inputs |

The record is the generated GOLD node for `Host-associated > Arthropoda:
Insects > Digestive system > Midgut > Filter chamber`, a zero-assertion insect
host-associated source-path leaf under a GOLD-specific Midgut parent.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/filter_chamber.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/filter_chamber.yaml` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just verify-corpus` | Passed; expected and found 3206 records, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --status all --out /tmp/habitatmech-next7-worklist.tsv` | Passed; wrote 953 ungrounded rows. Row 547 reports this target as a decided `HOST_ASSOCIATED` GOLD concept with zero generated assertions and three lexical candidates: `UBERON:0004151` `heart chamber`, `UBERON:0001766` `anterior chamber`, and `UBERON:0006311` `eye chamber`. |
| `just report --out /tmp/habitatmech-filter-chamber-report.tsv` | Passed; row 2105 reports this target as a `HOST_ASSOCIATED` `UNGROUNDED`/`SEEDED` GOLD-only record with one source, zero generated assertions, one parent, no definition, no environmental parameters, no characteristic taxa, and no causal graph. |

## Identity and Grounding

The generated identity is reproducible from a single raw GOLD ecosystem row:

| Source | Evidence |
|---|---|
| `data/raw/gold_ecosystem_paths.tsv:1810` | Exact path `Host-associated > Arthropoda: Insects > Digestive system > Midgut > Filter chamber`, leaf label `Filter chamber`, depth `5`, one GOLD ecosystem node, zero organisms, zero studies, zero biosamples, zero total assertions, and node id `gold.ecosystem:7391`. |
| `data/habitats/PATHS.tsv:2105` | `habitatmech:GOLD.6e59a6cbb1` maps to slug `filter_chamber`, matching the reviewed YAML path. |
| `curation/decisions.tsv:662` | `habitatmech:GOLD.6e59a6cbb1` has only a class-level `CONFIRM_UNGROUNDED` row. |

The generated parent is the immediate GOLD source-path parent:
`Host-associated > Arthropoda: Insects > Digestive system > Midgut`. That
parent resolves to `data/habitats/host_associated/midgut__7677107b.yaml` as
`habitatmech:GOLD.67c565f695`, a generated `NARROW` record under
`UBERON:0001045` `midgut` and the GOLD digestive-system parent.

The current worklist reports three vendored lexical candidates for `Filter
chamber`:

| Term | Label | Assessment |
|---|---|---|
| `UBERON:0004151` | `cardiac chamber` | A heart anatomical space, not the insect midgut filter chamber named by the GOLD source path. |
| `UBERON:0001766` | `anterior chamber of eyeball` | An eye anatomical space, not the insect midgut filter chamber named by the GOLD source path. |
| `UBERON:0006311` | `chamber of eyeball` | An eye anatomical space, not the insect midgut filter chamber named by the GOLD source path. |

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| This record represents GOLD's `Filter chamber` node under the insect midgut branch. | The exact source path appears in `data/raw/gold_ecosystem_paths.tsv` on row 1810, and the generated YAML copies its GOLD node id, leaf label, and full source path. | Supported. |
| The record has no direct upstream GOLD assertion count. | The raw target row reports zero organism, study, biosample, and total assertions; an exact hidden/ignored-inclusive search for `gold.ecosystem:7391` found only the raw GOLD ecosystem path row and the generated YAML source attestation. | Supported. |
| `parent_habitats: habitatmech:GOLD.67c565f695` is the generated source-path parent. | The target path's immediate parent is `Host-associated > Arthropoda: Insects > Digestive system > Midgut`, which resolves to `data/habitats/host_associated/midgut__7677107b.yaml`. | Supported as generated source hierarchy. |
| The target already has item-level curation. | `curation/decisions.tsv:662` has `review_depth` `CLASS`; exact hidden/ignored-inclusive searches found no target-specific YAML review before this report, append-only history record, external xref, causal overlay, habitat-research manifest row, term request, or term-request exclusion. | Unsupported. |
| A vendored ontology term names this insect Filter chamber node. | `UBERON:0004151`, `UBERON:0001766`, and `UBERON:0006311` are heart or eye chamber terms, and the class-level decision still reports that no term in the vendored slice matched this label by any search route. | Unsupported pending item-level review; no exact vendored term was found. |

Before this report was written, exact hidden/ignored-inclusive searches for
`habitatmech:GOLD.6e59a6cbb1` covered `data`, `curation`, `history`,
`research`, `reports`, `docs`, `conf`, `src`, `tests`, `README.md`,
`justfile`, and `.claude`, with generated `pages/`, `data/text_map/`, and
`build/` excluded. They found only the generated record, the generated
`PATHS.tsv` row, and the class-level curation decision.

The pre-report exact hidden/ignored-inclusive search for `gold.ecosystem:7391`
covered the same maintained sources and found only the raw GOLD ecosystem path
row and the generated YAML source attestation. The pre-report full-path
hidden/ignored-inclusive search found only the raw GOLD ecosystem path row; the
same path appears in the YAML source attestation split across wrapped lines.

Before this report was written, hidden/ignored-inclusive searches for the exact
identifier, slug `filter_chamber`, and label `Filter chamber` under
`reports/yaml_record_review` found no prior target-specific YAML review.

## Completeness

The YAML is structurally complete for its current input state. It records the
single GOLD node id, the full GOLD source path, the generated immediate Midgut
parent, and curation-history entries for the class-level `CONFIRM_UNGROUNDED`
decision and source seed.

The empty definition, synonyms, xrefs, environmental parameters,
characteristic taxa, evidence, causal graphs, discussions, and datasets are
expected for a zero-assertion GOLD leaf with no target-specific research or
item-level curation. They do not prove the anatomical scope is finished:
`Filter chamber` still needs an item-level decision that evaluates whether the
GOLD insect midgut filter-chamber concept is a valid host-associated habitat
context distinct from the broader generated `Midgut` parent and from the heart
and eye chamber ontology candidates.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found | The YAML validates, reproduces from committed inputs, preserves the exact `gold.ecosystem:7391` source node, and sits under the generated broader `habitatmech:GOLD.67c565f695` Midgut parent. | Not applicable |
| Major | The `Host-associated > Arthropoda: Insects > Digestive system > Midgut > Filter chamber` source concept is backed only by a class-level `CONFIRM_UNGROUNDED` row, so the generated `UNGROUNDED` state has not been item-reviewed against the insect midgut source path or the heart/eye chamber lexical candidates. | `curation/decisions.tsv:662` has `review_depth` `CLASS`; `data/raw/gold_ecosystem_paths.tsv:1810` shows the target carries zero direct upstream GOLD assertions; and `data/raw/ontology_terms.tsv` shows the current lexical candidates are different anatomical chambers. | `curation/decisions.tsv`; if the record stays minted and deserves a definition, `curation/term_requests.tsv` |
| Minor | None found | No non-blocking style, provenance, or schema issue was found. | Not applicable |

## Recommended Edits

1. Item-review `habitatmech:GOLD.6e59a6cbb1` in
   `curation/decisions.tsv`. Treat `Host-associated > Arthropoda: Insects >
   Digestive system > Midgut > Filter chamber` as the exact source concept and
   keep the decision distinct from the broader generated `Midgut` parent.
2. Explicitly reject `UBERON:0004151` `cardiac chamber`, `UBERON:0001766`
   `anterior chamber of eyeball`, and `UBERON:0006311` `chamber of eyeball` as
   off-target anatomical-chamber hits.
3. If item review confirms Filter chamber is a stable insect host-associated
   habitat context, keep `CONFIRM_UNGROUNDED` at `ITEM` depth and add a
   `curation/term_requests.tsv` definition only if the coined HabitatMech term
   needs one.

## Follow-up Checks

After item-level curation, rerun:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.6e59a6cbb1`
3. Inspect `data/habitats/host_associated/filter_chamber.yaml`
4. `just validate data/habitats/host_associated/filter_chamber.yaml`
5. `just validate-strict data/habitats/host_associated/filter_chamber.yaml`
6. `just term-requests-check`
7. `just validate-history`
8. `just verify-corpus`
9. `just report`

If curation adds a causal graph later, also run `just validate-causal-all`.

## Additional Notes

- iModulonDB was not applicable: this record names a GOLD habitat source path,
  not a gene, regulator, pathway, strain phenotype, or transcriptomics
  dataset.
