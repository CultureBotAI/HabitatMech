# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/food/fermentation_cellar.yaml`
- Started UTC: 2026-09-28T18:35:32Z
- Finished UTC: 2026-09-28T18:35:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| File | `data/habitats/food/fermentation_cellar.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.0d60ee305c` |
| Label | `Fermentation cellar` |
| Category | `FOOD` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Maintained/generated | Generated from `data/raw/` plus curation inputs |

The record is the generated GOLD node for `Engineered > Food production >
Fermentation cellar`, a zero-assertion food-production source path. The source
row aggregates three GOLD ecosystem node ids for that path and sits under the
ontology-grounded `FOODON:03530206` `food production` parent.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/food/fermentation_cellar.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/food/fermentation_cellar.yaml` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just verify-corpus` | Passed; expected and found 3206 records, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --status all --out /tmp/habitatmech-next2-worklist.tsv` | Passed; wrote 953 ungrounded rows. Row 542 reports this target as a decided `FOOD` GOLD concept with zero generated assertions and lexical candidates for fermentation starters and fermentation pits. |
| `just report --out /tmp/habitatmech-fermentation-cellar-report.tsv` | Passed; row 1376 reports this target as a `FOOD` `UNGROUNDED`/`SEEDED` GOLD-only record with one source, zero generated assertions, one parent, no definition, no environmental parameters, no characteristic taxa, and no causal graph. |

## Identity and Grounding

The generated identity is reproducible from a single raw GOLD ecosystem row:

| Source | Evidence |
|---|---|
| `data/raw/gold_ecosystem_paths.tsv:1296` | Exact path `Engineered > Food production > Fermentation cellar`, leaf label `Fermentation cellar`, depth `3`, three GOLD ecosystem nodes, zero organisms, zero studies, zero biosamples, zero total assertions, and node ids `gold.ecosystem:5632`, `gold.ecosystem:8249`, and `gold.ecosystem:8250`. |
| `data/habitats/PATHS.tsv:1376` | `habitatmech:GOLD.0d60ee305c` maps to slug `fermentation_cellar`, matching the reviewed YAML path. |
| `curation/decisions.tsv:171` | `habitatmech:GOLD.0d60ee305c` has only a class-level `CONFIRM_UNGROUNDED` row. |

The generated parent is `FOODON:03530206` `food production`, which is the
grounding for the immediate GOLD source-path parent `Engineered > Food
production`. `data/habitats/food/food_production.yaml` preserves that GOLD
parent path and its `FOODON:03530206` exact match.

The only generated child is supported as a GOLD source-path child:
`data/raw/gold_ecosystem_paths.tsv:396` records `Engineered > Food production >
Fermentation cellar > Pit mud` with node ids `gold.ecosystem:5633` and
`gold.ecosystem:5634`, and `data/habitats/food/pit_mud.yaml` lists
`habitatmech:GOLD.0d60ee305c` as its generated parent. Unlike the target, that
child has 22 upstream GOLD organism assertions and one downstream GOLD study
and biosample row on the exact Pit mud path.

The current `UNGROUNDED` state is still a lexical no-match placeholder. The
vendored slice contains `ENVO:03600039` `fermentation pit` and `ENVO:03600040`
`fermentation starter`, but those maintained ontology definitions constrain
them to alcoholic-spirit fermentation pits and manufactured fermentation
starters, respectively. Neither is an exact identity for a food-production
cellar or its broader GOLD source-path site.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| This record represents GOLD's `Fermentation cellar` node under engineered food production. | The exact source path appears in `data/raw/gold_ecosystem_paths.tsv` only on row 1296, and the generated YAML copies its first GOLD node id, leaf label, and full source path. | Supported. |
| The record has no direct upstream GOLD assertion count. | The raw parent row reports zero organism, study, biosample, and total assertions. Anchored hidden/ignored-inclusive searches for the exact parent path found no `gold_studies.tsv` or `gold_path_biosamples.tsv` row for `Engineered > Food production > Fermentation cellar`. | Supported. |
| `parent_habitats: FOODON:03530206` is the generated grounding for the immediate GOLD source-path parent. | The target path's immediate parent is `Engineered > Food production`, which resolves to `data/habitats/food/food_production.yaml` and `FOODON:03530206`. | Supported as generated source hierarchy. |
| The generated `Pit mud` child belongs under this target. | The child source path is `Engineered > Food production > Fermentation cellar > Pit mud`; `data/habitats/food/pit_mud.yaml` lists the target identifier as its generated parent. | Supported as generated source hierarchy. |
| The target already has item-level curation. | `curation/decisions.tsv:171` has `review_depth` `CLASS`; exact hidden/ignored-inclusive searches found no target term request, term-request exclusion, external xref, causal overlay, habitat-research report, prior YAML review, or append-only history record. | Unsupported. |

Exact hidden/ignored-inclusive searches for
`habitatmech:GOLD.0d60ee305c` covered `curation/term_requests.tsv`,
`curation/term_requests_excluded.tsv`, `curation/external_xrefs.tsv`,
`curation/causal_graphs`, `history`, `research`,
`reports/habitat_research_manifest.tsv`, and `reports/yaml_record_review`.
They found no maintained term request, term-request exclusion, external xref,
causal overlay, append-only history record, habitat-research report, or prior
YAML review for this Fermentation cellar target.

Exact hidden/ignored-inclusive searches for `gold.ecosystem:5632`,
`gold.ecosystem:8249`, and `gold.ecosystem:8250` covered `data/raw`,
`data/habitats`, `curation`, `history`, `research`, `reports`, `docs`, `conf`,
`src`, `tests`, `README.md`, `justfile`, and `Justfile`. Matching searches for
`Engineered > Food production > Fermentation cellar` covered the same paths
plus `.claude`. They found only the raw target and Pit mud child rows, the
generated target and generated child parent pointer, the generated path lock,
and the class-level curation decision.

The vendored ontology snapshot also has no term whose label is `fermentation
cellar`: a hidden/ignored-inclusive case-insensitive fixed-string search for
`fermentation cellar` found no match in `data/raw/ontology_terms.tsv` or
`data/raw/ontology_subclass_edges.tsv`.

## Completeness

The YAML is structurally complete for its current input state. It records the
first GOLD node id, the full GOLD source path, the generated immediate parent,
and curation-history entries for the class-level `CONFIRM_UNGROUNDED` decision
and source seed.

The empty definition, synonyms, xrefs, environmental parameters,
characteristic taxa, evidence, causal graphs, discussions, and datasets are
expected for a zero-assertion GOLD parent with no target-specific research or
item-level curation. They do not prove the biological scope is finished:
`Fermentation cellar` still needs an item-level decision that evaluates the
food-production site, confirms that `Pit mud` is only a narrower child, and
compares the cellar record with the vendored fermentation-specific ENVO terms.

Before this report was written, exact hidden/ignored-inclusive searches for
`habitatmech:GOLD.0d60ee305c` and `Fermentation cellar` under
`reports/yaml_record_review` returned no prior YAML review for this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found | The YAML validates, reproduces from committed inputs, preserves the exact `gold.ecosystem:5632` source node, and sits under the generated `Engineered > Food production` source-path parent. | Not applicable |
| Major | The `Engineered > Food production > Fermentation cellar` source concept is backed only by a class-level `CONFIRM_UNGROUNDED` row, so the generated `UNGROUNDED` state has not been item-reviewed against the food-production cellar source path, its asserted `Pit mud` child, or the vendored fermentation-adjacent ENVO terms. | `curation/decisions.tsv:171` has `review_depth` `CLASS`; `data/raw/gold_ecosystem_paths.tsv:1296` shows the target carries zero direct upstream GOLD assertions; and `data/raw/ontology_terms.tsv:10081-10082` show the nearest fermentation-specific ENVO terms are narrower or adjacent rather than exact cellar identities. | `curation/decisions.tsv`; if the record stays minted and deserves a definition, `curation/term_requests.tsv` |
| Minor | None found | No non-blocking style, provenance, or schema issue was found. | Not applicable |

## Recommended Edits

1. Item-review `habitatmech:GOLD.0d60ee305c` in
   `curation/decisions.tsv`. Treat `Engineered > Food production >
   Fermentation cellar` as a site-like food-production source concept, not as
   the bare fermentation process.
2. Compare the target against `ENVO:03600039` `fermentation pit` and
   `ENVO:03600040` `fermentation starter`. The former is a narrower feature
   for producing alcoholic spirits, and the latter is a manufactured product
   used to start fermentation rather than a cellar.
3. If item review confirms this zero-assertion node should stay as a coined
   HabitatMech grouping record, keep `CONFIRM_UNGROUNDED` at `ITEM` depth and
   explain that the narrower `Pit mud` child has GOLD observations but does
   not by itself define the parent cellar scope. Add a `curation/term_requests.tsv`
   definition only if the target proves stable enough to name.

## Follow-up Checks

After item-level curation, rerun:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.0d60ee305c`
3. Inspect `data/habitats/food/fermentation_cellar.yaml`
4. `just validate data/habitats/food/fermentation_cellar.yaml`
5. `just validate-strict data/habitats/food/fermentation_cellar.yaml`
6. `just term-requests-check`
7. `just validate-history`
8. `just verify-corpus`
9. `just report`

If curation adds a causal graph later, also run `just validate-causal-all`.

## Additional Notes

- iModulonDB was not applicable: this record names a GOLD habitat source path,
  not a gene, regulator, pathway, strain phenotype, or transcriptomics dataset.
- The child `Engineered > Food production > Fermentation cellar > Pit mud`
  carries GOLD study and biosample rows. That evidence supports the child
  path, but exact hidden/ignored-inclusive searches found no comparable study
  or biosample row for the parent Fermentation cellar path.
