# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/agricultural_wastewater.yaml
- Started UTC: 2026-09-23T19:27:30Z
- Finished UTC: 2026-09-23T19:29:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | habitatmech:GOLD.bbf683017f |
| Label | Agricultural wastewater |
| Class | HabitatRecord |
| Category | ENGINEERED |
| Grounding status | UNGROUNDED |
| Mapping status | SEEDED |
| Maintained owner | generated from `data/raw/gold_ecosystem_paths.tsv`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; item-level follow-up belongs in `curation/decisions.tsv` and, if no exact existing term fits, `curation/term_requests.tsv` |

[data/habitats/engineered/agricultural_wastewater.yaml](../../data/habitats/engineered/agricultural_wastewater.yaml) is the generated record for GOLD `Engineered > Wastewater > Industrial wastewater > Agricultural wastewater`.

The target was resolved with ignored-file-inclusive searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-agricultural_wastewater.md' -print` found no prior exact review report.
- `find curation/causal_graphs -maxdepth 1 -type f -name 'agricultural_wastewater.yaml' -print` found no causal-graph overlay for this record.
- `rg --no-ignore --hidden -n -i -F -e 'habitatmech:GOLD.bbf683017f' -e 'gold.ecosystem:3837' -e 'gold.ecosystem:4268' -e 'Engineered > Wastewater > Industrial wastewater > Agricultural wastewater' -e 'agricultural_wastewater' -e 'Agricultural wastewater' curation data/habitats data/raw history research reports --glob '!data/text_map/**' --glob '!pages/**' --glob '!build/**' --glob '!reports/yaml_record_review/**' --glob '!.venv/**'` found the GOLD path inventories, the class-level `CONFIRM_UNGROUNDED` row, the slug lock, this generated record, and the near-miss ENVO `agricultural wastewater treatment plant` row; it found no maintained term request, causal overlay, history record, or target-specific research report.
- The same exact `rg --no-ignore --hidden` search over `curation/term_requests.tsv`, `curation/causal_graphs`, `history`, and `research` returned no target-specific rows.
- The same exact `rg --no-ignore --hidden` search over prior `reports/yaml_record_review` found only the previous `agricultural_waste_material` report's note that this sibling GOLD source is already a separate generated record; it found no earlier exact review for `habitatmech:GOLD.bbf683017f`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/agricultural_wastewater.yaml` | pass; no LinkML issues found |
| `just validate-strict data/habitats/engineered/agricultural_wastewater.yaml` | pass; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| `just validate-causal curation/causal_graphs/agricultural_wastewater.yaml` | not applicable; exact `find curation/causal_graphs -maxdepth 1 -type f -name 'agricultural_wastewater.yaml' -print` found no overlay |
| `just validate-causal-all` | pass; 32 causal-graph curation files with 32 graphs validated |
| Reference validator | not applicable; this generated GOLD-only record has no causal graph and no DOI, PMID, or URL evidence slots to inspect |
| `just term-requests-check` | pass; term-request table is current with 109 terms |
| `just validate-history` | pass; no issues found; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | pass; 3206 expected, 3206 found, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | pass; 0 ungrounded records still undecided; 1810 decisions on file |
| `just report` | pass; 3206 records; 0 stale class-level sweeps and 0 swept paths whose parent-plus-leaf compound names a habitat term |
| `git diff --check` | pass |

## Identity and Grounding

The minted identifier, label, category, and source path agree with the GOLD inventory. `data/raw/gold_ecosystem_paths.tsv` has `Engineered > Wastewater > Industrial wastewater > Agricultural wastewater` with leaf label `Agricultural wastewater`, collapsed GOLD node IDs `gold.ecosystem:3837|gold.ecosystem:4268`, and `13` organism assertions. `data/habitats/PATHS.tsv` locks the record identifier to the `agricultural_wastewater` slug.

The `UNGROUNDED` status is generated from the class-level sweep, not from an item-level review. `curation/decisions.tsv` marks `habitatmech:GOLD.bbf683017f` `CONFIRM_UNGROUNDED` at `CLASS` depth because no term in the vendored slice matched the label by the sweep's lexical routes; `docs/HARMONIZATION.md` says that sweep did not establish whether the concept is a habitat at all and therefore does not promote a record to `REVIEWED`.

`ENVO:01000964` `industrial wastewater` is a true broader parent for the GOLD source path. The parent path `Engineered > Wastewater > Industrial wastewater` grounds exactly to `ENVO:01000964`, and ENVO defines that term as wastewater produced by industrial activity with non-urine and non-fecal chemical contaminants.

The one vendored ENVO lexical near miss, `ENVO:2000003`, is not an exact identity. Its label is `agricultural wastewater treatment plant`; it denotes a plant that treats agricultural wastewater, not the wastewater material itself.

## Evidence

This record has one GOLD source attestation:

- The `GOLD` attestation mirrors `data/raw/gold_ecosystem_paths.tsv`: source id `gold.ecosystem:3837`, source label `Agricultural wastewater`, source path `Engineered > Wastewater > Industrial wastewater > Agricultural wastewater`, two collapsed GOLD node IDs, and `13` direct organism assertions.

No PREGO or BacDive source concept is merged into this record, and no PREGO or BacDive taxon list is present. No evidence-backed causal mechanism evidence is present.

Unsupported or over-scoped claims:

- None in the generated fields themselves; the generated fields are internally consistent with the current class-level decision and raw GOLD path.

## Completeness

The record carries the generated source-owned content for this single GOLD path: the minted source identifier, GOLD label, engineered category, valid `industrial wastewater` parent from the GOLD parent path, source attestation, class-level curation event, seed event, and slug lock.

The curation state is materially incomplete. The source path is a specific wastewater habitat with direct GOLD organism assertions, the vendored ontology slice has no exact agricultural-wastewater material term, and exact ignored-file-inclusive searches found no item-level decision, term request, target-specific research report, or causal overlay.

Optional characteristic-taxon, environmental-parameter, DOI/PMID/URL evidence, dataset, discussion, and causal-graph slots are correctly absent; the GOLD inventory provides source occurrence evidence, not characteristic taxa, mechanism edges, or environmental parameter rows.

## Findings

- **major**: `habitatmech:GOLD.bbf683017f` is still only class-swept, so a concrete ungrounded wastewater habitat has no item-level curation decision or term request.

  **Evidence**: The GOLD path is `Engineered > Wastewater > Industrial wastewater > Agricultural wastewater`, has `13` direct organism assertions in `data/raw/gold_ecosystem_paths.tsv`, and inherits a true `industrial wastewater` parent from the source tree. The only `curation/decisions.tsv` row is a `CLASS`-depth `CONFIRM_UNGROUNDED` row whose note explicitly says habitat status was not assessed. No exact ignored-file-inclusive search found a maintained `curation/term_requests.tsv` row, target-specific history entry, or research report for this source concept. `docs/HARMONIZATION.md` states that `CLASS` decisions do not promote a record to `REVIEWED`; `docs/CURATION.md` says `CONFIRM_UNGROUNDED` means the source concept is a real habitat for which no fitting identity term is available.

  **Maintained owner**: item-level habitat and grounding review belongs in `curation/decisions.tsv`; an authored definition and requested parent for a novel agricultural-wastewater habitat belong in `curation/term_requests.tsv` if item-level review still finds no exact existing term.

## Recommended Edits

- Reopen `habitatmech:GOLD.bbf683017f` as an item-level curation task in `curation/decisions.tsv`, because the class-level sweep only established a negative lexical result against the vendored slice.
- Inspect the existing external candidate space for an exact agricultural-wastewater material term. Do not ground to `ENVO:2000003` unless the intended identity changes to the treatment plant rather than the wastewater.
- If no exact external term fits, keep `habitatmech:GOLD.bbf683017f` minted with an `ITEM`-depth `CONFIRM_UNGROUNDED` row and add a focused `curation/term_requests.tsv` row under `ENVO:01000964` for agricultural wastewater.
- Regenerate `habitatmech:GOLD.bbf683017f` and inspect [data/habitats/engineered/agricultural_wastewater.yaml](../../data/habitats/engineered/agricultural_wastewater.yaml) to confirm the record remains under `ENVO:01000964` and moves from a class-swept seed to the expected reviewed or term-requested state.

## Follow-up Checks

The narrow proof path for a future fix is:

- exact ignored-file-inclusive searches for `habitatmech:GOLD.bbf683017f`, `gold.ecosystem:3837`, `gold.ecosystem:4268`, `Agricultural wastewater`, and any selected external ontology candidate
- `just seed`
- `just seed-canary habitatmech:GOLD.bbf683017f`
- inspect [data/habitats/engineered/agricultural_wastewater.yaml](../../data/habitats/engineered/agricultural_wastewater.yaml) for the expected `grounding_status`, `mapping_status`, `parent_habitats`, and curation history
- `just validate-strict data/habitats/engineered/agricultural_wastewater.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

[data/habitats/engineered/agricultural_waste_material.yaml](../../data/habitats/engineered/agricultural_waste_material.yaml) separately carries the ENVO `agricultural waste material` identity. The review of that record deliberately kept this `Engineered > Wastewater > Industrial wastewater > Agricultural wastewater` GOLD source separate, because the obsolete ENVO `agricultural waste` term denoted wastewater while the replacement `agricultural waste material` class is broader.

[data/habitats/engineered/industrial_wastewater.yaml](../../data/habitats/engineered/industrial_wastewater.yaml) is the generated `ENVO:01000964` parent inherited from this GOLD source path.
