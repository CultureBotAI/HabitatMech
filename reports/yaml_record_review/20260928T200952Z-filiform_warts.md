# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/filiform_warts.yaml`
- Started UTC: 2026-09-28T20:09:52Z
- Finished UTC: 2026-09-28T20:09:52Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| File | `data/habitats/host_associated/filiform_warts.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.06c04be03f` |
| Label | `Filiform warts` |
| Category | `HOST_ASSOCIATED` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |
| Maintained/generated | Generated from `data/raw/` plus curation inputs |

The record is the generated GOLD node for `Host-associated > Mammals: Human >
Benign tumor > Wart > Filiform warts`, a zero-assertion human
host-associated leaf under the generated Wart parent.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/filiform_warts.yaml` | Passed; LinkML reported no issues. |
| `just validate-strict data/habitats/host_associated/filiform_warts.yaml` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just verify-corpus` | Passed; expected and found 3206 records, with 0 missing, 0 extra, and 0 differing records. |
| `just worklist --status all --out /tmp/habitatmech-next5-worklist.tsv` | Passed; wrote 953 ungrounded rows. Row 545 reports this target as a decided `HOST_ASSOCIATED` GOLD concept with zero generated assertions and no lexical candidates. |
| `just report --out /tmp/habitatmech-filiform-warts-report.tsv` | Passed; row 1320 reports this target as a `HOST_ASSOCIATED` `UNGROUNDED`/`SEEDED` GOLD-only record with one source, zero generated assertions, one parent, no definition, no environmental parameters, no characteristic taxa, and no causal graph. |

## Identity and Grounding

The generated identity is reproducible from a single raw GOLD ecosystem row:

| Source | Evidence |
|---|---|
| `data/raw/gold_ecosystem_paths.tsv:2181` | Exact path `Host-associated > Mammals: Human > Benign tumor > Wart > Filiform warts`, leaf label `Filiform warts`, depth `5`, one GOLD ecosystem node, zero organisms, zero studies, zero biosamples, zero total assertions, and node id `gold.ecosystem:6668`. |
| `data/habitats/PATHS.tsv:1320` | `habitatmech:GOLD.06c04be03f` maps to slug `filiform_warts`, matching the reviewed YAML path. |
| `curation/decisions.tsv:135` | `habitatmech:GOLD.06c04be03f` has only a class-level `CONFIRM_UNGROUNDED` row. |

The generated parent is the immediate GOLD source-path parent:
`Host-associated > Mammals: Human > Benign tumor > Wart`. That parent resolves
to `data/habitats/host_associated/wart.yaml` as `BTO:0001859`, the BTO `wart`
term with the definition `A horny projection on the skin usually of the
extremities produced by proliferation of the skin papillae and caused by a
papillomavirus.`

The `BTO:0001859` parent is strictly broader than the Filiform warts source
concept. The same generated Wart parent also owns the GOLD `Common warts`,
`Flat warts`, `Genital warts`, `Plantar warts`, `Surface`, and `Tissue`
source-path children.

The current worklist reports no vendored lexical candidate for `Filiform
warts`; the target has no generated source-path children.

## Evidence

| Claim | Evidence checked | Assessment |
|---|---|---|
| This record represents GOLD's `Filiform warts` node under the human benign-tumor Wart branch. | The exact source path appears in `data/raw/gold_ecosystem_paths.tsv` on row 2181, and the generated YAML copies its GOLD node id, leaf label, and full source path. | Supported. |
| The record has no direct upstream GOLD assertion count. | The raw target row reports zero organism, study, biosample, and total assertions; an exact hidden/ignored-inclusive search for `gold.ecosystem:6668` found only the raw GOLD ecosystem path row and the generated YAML source attestation. | Supported. |
| `parent_habitats: BTO:0001859` is the generated broader Wart parent. | The target path's immediate parent is `Host-associated > Mammals: Human > Benign tumor > Wart`, which resolves to `BTO:0001859`; `data/raw/ontology_terms.tsv:1859` names `BTO:0001859` as `wart`, not a filiform-specific wart subtype. | Supported as generated source hierarchy. |
| The target already has item-level curation. | `curation/decisions.tsv:135` has `review_depth` `CLASS`; exact hidden/ignored-inclusive searches found no target-specific YAML review, append-only history record, external xref, causal overlay, habitat-research manifest row, term request, or term-request exclusion. | Unsupported. |
| A vendored ontology term names this Filiform warts subtype. | The regenerated worklist reports no candidate ontology terms for `Filiform warts`, and the class-level decision still reports that no term in the vendored slice matched this label by any search route. | Unsupported pending item-level review; no exact vendored term was found. |

Before this report was written, exact hidden/ignored-inclusive searches for
`habitatmech:GOLD.06c04be03f` covered `data`, `curation`, `history`,
`research`, `reports`, `docs`, `conf`, `src`, `tests`, `README.md`,
`justfile`, and `.claude`, with generated `pages/` and `data/text_map/`
excluded. They found only the generated record, the generated `PATHS.tsv` row,
and the class-level curation decision.

The pre-report exact hidden/ignored-inclusive search for `gold.ecosystem:6668`
covered the same maintained sources and found only the raw GOLD ecosystem path
row and the generated YAML source attestation. The pre-report exact
hidden/ignored-inclusive search for the full GOLD path found only the raw GOLD
ecosystem path row.

Before this report was written, hidden/ignored-inclusive searches for
`reports/yaml_record_review` entries with `filiform` or `wart` in the filename,
and an exact identifier search under `reports/yaml_record_review`, returned no
prior target-specific YAML review.

## Completeness

The YAML is structurally complete for its current input state. It records the
single GOLD node id, the full GOLD source path, the generated immediate Wart
parent, and curation-history entries for the class-level `CONFIRM_UNGROUNDED`
decision and source seed.

The empty definition, synonyms, xrefs, environmental parameters,
characteristic taxa, evidence, causal graphs, discussions, and datasets are
expected for a zero-assertion GOLD leaf with no target-specific research or
item-level curation. They do not prove the biological scope is finished:
`Filiform warts` still needs an item-level decision that evaluates whether a
filiform wart subtype is a valid host-associated habitat context that should
remain minted as narrower than `BTO:0001859` `wart`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | None found | The YAML validates, reproduces from committed inputs, preserves the exact `gold.ecosystem:6668` source node, and sits under the generated broader `BTO:0001859` Wart parent. | Not applicable |
| Major | The `Host-associated > Mammals: Human > Benign tumor > Wart > Filiform warts` source concept is backed only by a class-level `CONFIRM_UNGROUNDED` row, so the generated `UNGROUNDED` state has not been item-reviewed against the source path, the broader Wart parent, or the absence of any exact filiform-wart term in the vendored slice. | `curation/decisions.tsv:135` has `review_depth` `CLASS`; `data/raw/gold_ecosystem_paths.tsv:2181` shows the target carries zero direct upstream GOLD assertions; and `just worklist` reports no lexical candidates for this leaf. | `curation/decisions.tsv`; if the record stays minted and deserves a definition, `curation/term_requests.tsv` |
| Minor | None found | No non-blocking style, provenance, or schema issue was found. | Not applicable |

## Recommended Edits

1. Item-review `habitatmech:GOLD.06c04be03f` in
   `curation/decisions.tsv`. Treat `Host-associated > Mammals: Human > Benign
   tumor > Wart > Filiform warts` as the exact source concept and keep the
   decision distinct from the broader generated `BTO:0001859` Wart parent.
2. If item review confirms Filiform warts is a stable host-associated tissue
   context with no exact vendored ontology term, keep `CONFIRM_UNGROUNDED` at
   `ITEM` depth.
3. Add a `curation/term_requests.tsv` definition only if the coined
   HabitatMech term needs one after item review.

## Follow-up Checks

After item-level curation, rerun:

1. `just seed`
2. `just seed-canary habitatmech:GOLD.06c04be03f`
3. Inspect `data/habitats/host_associated/filiform_warts.yaml`
4. `just validate data/habitats/host_associated/filiform_warts.yaml`
5. `just validate-strict data/habitats/host_associated/filiform_warts.yaml`
6. `just term-requests-check`
7. `just validate-history`
8. `just verify-corpus`
9. `just report`

If curation adds a causal graph later, also run `just validate-causal-all`.

## Additional Notes

- iModulonDB was not applicable: this record names a GOLD habitat source path,
  not a gene, regulator, pathway, strain phenotype, or transcriptomics
  dataset.
