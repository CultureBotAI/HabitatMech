# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/ags_aerobic_granular_sludge.yaml
- Started UTC: 2026-09-23T19:46:57Z
- Finished UTC: 2026-09-23T19:49:48Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | habitatmech:GOLD.099b899fb9 |
| Label | AGS (Aerobic granular sludge) |
| Class | HabitatRecord |
| Category | ENGINEERED |
| Grounding status | UNGROUNDED |
| Mapping status | SEEDED |
| Maintained owner | generated from `data/raw/gold_ecosystem_paths.tsv`, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; item-level follow-up belongs in `curation/decisions.tsv` and, if no exact existing term fits, `curation/term_requests.tsv` |

[data/habitats/engineered/ags_aerobic_granular_sludge.yaml](../../data/habitats/engineered/ags_aerobic_granular_sludge.yaml) is the generated record for GOLD `Engineered > Bioreactor > Aerobic > AGS (Aerobic granular sludge)`.

The target was resolved with ignored-file-inclusive searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-ags_aerobic_granular_sludge.md' -print` found no prior exact review report.
- `find curation/causal_graphs -maxdepth 1 -type f -name 'ags_aerobic_granular_sludge.yaml' -print` found no causal-graph overlay for this record.
- Exact `rg --no-ignore --hidden` searches for `habitatmech:GOLD.099b899fb9`, `GOLD.099b899fb9`, `gold.ecosystem:8143`, `gold.ecosystem:8144`, `Engineered > Bioreactor > Aerobic > AGS (Aerobic granular sludge)`, `AGS (Aerobic granular sludge)`, and `ags_aerobic_granular_sludge` across `curation`, `data/habitats`, `data/raw`, `history`, `research`, and `reports`, excluding generated `data/text_map`, `pages`, `build`, prior YAML-review reports, and `.venv`, found the GOLD path inventory, the class-level `CONFIRM_UNGROUNDED` row, the slug lock, and this generated record; they found no maintained term request, causal overlay, history record, or target-specific research report.
- Exact ignored-file-inclusive searches for `aerobic granular sludge` and `granular sludge` found neighboring GOLD granular-sludge leaves and vendored near misses, but no exact existing HabitatMech term request for aerobic granular sludge.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/ags_aerobic_granular_sludge.yaml` | pass; no LinkML issues found |
| `just validate-strict data/habitats/engineered/ags_aerobic_granular_sludge.yaml` | pass; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| `just validate-causal curation/causal_graphs/ags_aerobic_granular_sludge.yaml` | not applicable; exact `find curation/causal_graphs -maxdepth 1 -type f -name 'ags_aerobic_granular_sludge.yaml' -print` found no overlay |
| `just validate-causal-all` | pass; 32 causal-graph curation files with 32 graphs validated |
| Reference validator | not applicable; this generated GOLD-only record has no causal graph and no DOI, PMID, or URL evidence slots to inspect |
| `just term-requests-check` | pass; term-request table is current with 109 terms |
| `just validate-history` | pass; no issues found; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | pass; 3206 expected, 3206 found, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | pass; 0 ungrounded records still undecided; 1810 decisions on file |
| `just report` | pass; 3206 records; 0 stale class-level sweeps and 0 swept paths whose parent-plus-leaf compound names a habitat term |
| `git diff --check` | pass |

## Identity and Grounding

The minted identifier, label, category, and source path agree with the GOLD inventory. `data/raw/gold_ecosystem_paths.tsv` has `Engineered > Bioreactor > Aerobic > AGS (Aerobic granular sludge)` with leaf label `AGS (Aerobic granular sludge)`, collapsed GOLD node IDs `gold.ecosystem:8143|gold.ecosystem:8144`, and no organism, study, biosample, or total assertions. `data/habitats/PATHS.tsv` locks `habitatmech:GOLD.099b899fb9` to the `ags_aerobic_granular_sludge` slug.

The `UNGROUNDED` status is generated from the class-level sweep, not from an item-level review. `curation/decisions.tsv` marks `habitatmech:GOLD.099b899fb9` `CONFIRM_UNGROUNDED` at `CLASS` depth because no term in the vendored slice matched the label by the sweep's lexical routes; `docs/HARMONIZATION.md` says that sweep did not establish whether the concept is a habitat at all and therefore does not promote a record to `REVIEWED`.

`ENVO:00002126` `aerobic bioreactor` is inherited from the immediate GOLD parent path. The parent source concept `Engineered > Bioreactor > Aerobic` has already been reviewed as an exact match for `aerobic bioreactor`.

The vendored slice has granular-sludge near misses, but not an exact AGS term. `ENVO:00002212` names `thermophilic granular sludge`, `ENVO:00002129` names `anaerobic sludge`, `ENVO:00003965` names `anaerobic digester sludge`, and `ENVO:00002213` names an `anaerobic sludge blanket reactor`; all over-specify a temperature, oxygen state, or reactor geometry that the GOLD AGS source path does not assert.

## Evidence

This record has one GOLD source attestation:

- The `GOLD` attestation mirrors `data/raw/gold_ecosystem_paths.tsv`: source id `gold.ecosystem:8143`, source label `AGS (Aerobic granular sludge)`, source path `Engineered > Bioreactor > Aerobic > AGS (Aerobic granular sludge)`, two collapsed GOLD node IDs, and zero direct organism assertions.

No PREGO or BacDive source concept is merged into this record, and no PREGO or BacDive taxon list is present. No evidence-backed causal mechanism evidence is present.

Unsupported or over-scoped claims:

- None in the generated fields themselves; the generated fields are internally consistent with the current class-level decision and raw GOLD path.

## Completeness

The record carries the generated source-owned content for this single GOLD path: the minted source identifier, GOLD label, engineered category, inherited `aerobic bioreactor` parent from the GOLD parent path, source attestation, class-level curation event, seed event, and slug lock.

The curation state is materially incomplete. The source path is a specific aerobic granular sludge leaf, the vendored ontology slice has no exact aerobic-granular-sludge term, exact ignored-file-inclusive searches found no item-level decision, term request, target-specific research report, or causal overlay, and the only maintained decision explicitly says source-concept habitat status was not assessed.

Optional characteristic-taxon, environmental-parameter, DOI/PMID/URL evidence, dataset, discussion, and causal-graph slots are correctly absent; the GOLD inventory provides only source occurrence evidence for this path, not characteristic taxa, mechanism edges, or environmental parameter rows.

## Findings

- **major**: `habitatmech:GOLD.099b899fb9` is still only class-swept, so a candidate aerobic-granular-sludge habitat has no item-level habitat decision or term request.

  **Evidence**: The GOLD path is `Engineered > Bioreactor > Aerobic > AGS (Aerobic granular sludge)` and its immediate parent is the item-reviewed `ENVO:00002126` `aerobic bioreactor` source path. The only `curation/decisions.tsv` row for `habitatmech:GOLD.099b899fb9` is a `CLASS`-depth `CONFIRM_UNGROUNDED` row whose note explicitly says habitat status was not assessed. Exact ignored-file-inclusive searches found no maintained `curation/term_requests.tsv` row, target-specific history entry, or research report for this source concept. `docs/HARMONIZATION.md` states that `CLASS` decisions do not promote a record to `REVIEWED`; `docs/CURATION.md` says `CONFIRM_UNGROUNDED` means the source concept is a real habitat for which no fitting identity term is available.

  **Maintained owner**: item-level habitat and grounding review belongs in `curation/decisions.tsv`; an authored definition and requested parent for a novel aerobic-granular-sludge habitat belong in `curation/term_requests.tsv` if item-level review still finds no exact existing term.

## Recommended Edits

- Reopen `habitatmech:GOLD.099b899fb9` as an item-level curation task in `curation/decisions.tsv`, because the class-level sweep only established a negative lexical result against the vendored slice.
- Inspect the existing external candidate space for an exact aerobic-granular-sludge term. Do not ground to the vendored `thermophilic granular sludge`, `anaerobic sludge`, `anaerobic digester sludge`, or `anaerobic sludge blanket reactor` terms unless the intended identity narrows beyond GOLD's aerobic AGS path.
- If no exact external term fits, keep `habitatmech:GOLD.099b899fb9` minted with an `ITEM`-depth `CONFIRM_UNGROUNDED` row and add a focused `curation/term_requests.tsv` row under a strict aerobic-bioprocess or sludge parent chosen during item-level review.
- Regenerate `habitatmech:GOLD.099b899fb9` and inspect [data/habitats/engineered/ags_aerobic_granular_sludge.yaml](../../data/habitats/engineered/ags_aerobic_granular_sludge.yaml) to confirm the record remains under a strictly broader parent and moves from a class-swept seed to the expected reviewed or term-requested state.

## Follow-up Checks

The narrow proof path for a future fix is:

- exact ignored-file-inclusive searches for `habitatmech:GOLD.099b899fb9`, `gold.ecosystem:8143`, `gold.ecosystem:8144`, `AGS (Aerobic granular sludge)`, and any selected external ontology candidate
- `just seed`
- `just seed-canary habitatmech:GOLD.099b899fb9`
- inspect [data/habitats/engineered/ags_aerobic_granular_sludge.yaml](../../data/habitats/engineered/ags_aerobic_granular_sludge.yaml) for the expected `grounding_status`, `mapping_status`, `parent_habitats`, and curation history
- `just validate-strict data/habitats/engineered/ags_aerobic_granular_sludge.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

The AGS GOLD row has `gold_node_count` 2 but no direct upstream organism, study, biosample, or total assertions. That makes this lower volume than neighboring `Engineered > Bioreactor > UASB (Upflow anaerobic sludge blanket) > Sludge > Granular sludge`, but it does not by itself prove the source concept is not a habitat; it only means the current GOLD inventory contributes taxonomy no further than the source path.
