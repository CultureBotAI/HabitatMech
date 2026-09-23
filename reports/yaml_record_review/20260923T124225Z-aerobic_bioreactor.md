# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/aerobic_bioreactor.yaml`
- Started UTC: 2026-09-23T12:38:00Z
- Finished UTC: 2026-09-23T12:42:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `ENVO:00002126` |
| Label | `aerobic bioreactor` |
| Category | `ENGINEERED` |
| Grounding status | `EXACT` |
| Mapping status | `REVIEWED` |
| Sources | `GOLD` |
| Record status | Generated from `data/raw/` plus maintained curation inputs; generated YAML remains read-only |

This is the generated ENVO-grounded record for `aerobic bioreactor`, attested by three reviewed GOLD source concepts:

| Source concept | GOLD node | Decision |
|---|---|---|
| `habitatmech:GOLD.904dea8017` / `Engineered > Bioreactor > Aerobic` | `gold.ecosystem:4534` | `GROUND ENVO:00002126` at `curation/decisions.tsv:838` |
| `habitatmech:GOLD.2ee55ba737` / `Engineered > Bioreactor > SSF (Solid state fermentation) > Aerobic` | `gold.ecosystem:7774` | `GROUND ENVO:00002126` at `curation/decisions.tsv:356` |
| `habitatmech:GOLD.0b917b1e6b` / `Engineered > Bioreactor > DHS reactor > Aerobic` | `gold.ecosystem:8428` | `GROUND ENVO:00002126` at `curation/decisions.tsv:162` |

`data/habitats/PATHS.tsv:646` locks `ENVO:00002126` to the `aerobic_bioreactor` slug, and `data/raw/ontology_terms.tsv:7222` supplies the ontology label and definition used in the generated record.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/aerobic_bioreactor.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/aerobic_bioreactor.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the committed term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; the generated corpus still has 3206 records, 2520 `SEEDED` mappings, 686 `REVIEWED` mappings, 0 risky unreviewed groundings, and 0 swept concepts whose label or path currently names a non-habitat. |
| Reference validator | Not applicable; this record has no record-level `evidence`, no `causal_graphs`, and therefore no literature references for a reference-specific validator to resolve. |
| `git diff --check` | Passed before writing this report; no whitespace or patch errors were present. |

## Identity and Grounding

The ENVO identity is supported for the direct GOLD `Engineered > Bioreactor > Aerobic` concept. The vendored ENVO slice defines `ENVO:00002126` `aerobic bioreactor` as "A bioreactor in which the contained material is well-oxygenated."; `data/raw/ontology_subclass_edges.tsv:5326` places it under `ENVO:00002123` `bioreactor`; and the GOLD path composes the parent `Bioreactor` with the oxygenation qualifier `Aerobic`.

The record over-merges two more specific GOLD concepts:

| Source concept | Raw row | Review |
|---|---|---|
| `Engineered > Bioreactor > SSF (Solid state fermentation) > Aerobic` | `data/raw/gold_ecosystem_paths.tsv:1211` has leaf `Aerobic` under the SSF parent and one GOLD node, `gold.ecosystem:7774`. | This denotes aerobic solid-state-fermentation context, not generic aerobic bioreactors. It is narrower than `ENVO:00002126`. |
| `Engineered > Bioreactor > DHS reactor > Aerobic` | `data/raw/gold_ecosystem_paths.tsv:1175` has leaf `Aerobic` under the DHS parent and two GOLD nodes, `gold.ecosystem:8428\|gold.ecosystem:8429`. | This denotes an aerobic DHS reactor context, not generic aerobic bioreactors. It is narrower than `ENVO:00002126`. |

The generated `mapping_status: REVIEWED` is mechanically expected because all three contributing GOLD concepts have item-level decisions, but two of those item-level decisions use `GROUND` where a narrower minted identity plus `ENVO:00002126` as parent would preserve the full GOLD meaning.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| `ENVO:00002126` is a subtype of `ENVO:00002123` `bioreactor`. | `data/raw/ontology_subclass_edges.tsv:5326`; `data/raw/ontology_terms.tsv:7221-7222` | Supported. |
| `Engineered > Bioreactor > Aerobic` is an exact source attestation for `ENVO:00002126`. | `data/raw/gold_ecosystem_paths.tsv:311`; `curation/decisions.tsv:838` | Supported. The GOLD leaf qualifies `Bioreactor`, and the item-level decision records that composed reading. |
| The generic GOLD source should carry `assertion_count: 46`. | `data/raw/gold_ecosystem_paths.tsv:311`; `src/habitatmech/seed.py` | Supported. The raw path has `organism_count=46`, and the seeder emits GOLD organism counts as source-attestation assertions. |
| The generic GOLD source should carry the duplicate-node note. | `data/raw/gold_ecosystem_paths.tsv:311`; `src/habitatmech/seed.py` | Supported. The raw row collapses three GOLD ecosystem node ids; the seeder emits the first and notes the shared path. |
| `Engineered > Bioreactor > SSF (Solid state fermentation) > Aerobic` is an exact source attestation for `ENVO:00002126`. | `curation/decisions.tsv:356` | Unsupported. The item-level note recognizes that GOLD qualifies a parent node, but the parent node is `SSF (Solid state fermentation)`, making the source narrower than generic aerobic bioreactor. |
| `Engineered > Bioreactor > DHS reactor > Aerobic` is an exact source attestation for `ENVO:00002126`. | `curation/decisions.tsv:162` | Unsupported. The item-level note recognizes that GOLD qualifies a parent node, but the parent node is `DHS reactor`, making the source narrower than generic aerobic bioreactor. |
| The generic `ENVO:00002126` record is a child of `habitatmech:GOLD.3af6ca6cc3` `SSF (Solid state fermentation)`. | Generated by merging the narrower SSF/aerobic source concept into the generic record and retaining the immediate GOLD parent. | Unsupported. Aerobic SSF bioreactors are a narrower context within aerobic bioreactors, not the other way around. |
| The generic `ENVO:00002126` record is a child of `habitatmech:GOLD.24cf427e7d` `DHS reactor`. | Generated by merging the narrower DHS/aerobic source concept into the generic record and retaining the immediate GOLD parent. | Unsupported. Aerobic DHS reactors are a narrower context within aerobic bioreactors, not the other way around. |

## Completeness

No maintained definition, causal overlay, target-specific research report, or history entry exists for `ENVO:00002126`, `aerobic_bioreactor`, `habitatmech:GOLD.904dea8017`, `habitatmech:GOLD.2ee55ba737`, or `habitatmech:GOLD.0b917b1e6b`; exact gitignore-independent searches covered `curation/term_requests.tsv`, `curation/causal_graphs`, `history`, `research`, `reports/yaml_record_review`, `data/raw`, `data/habitats/PATHS.tsv`, and generated engineered records while excluding broad generated `build`, `data/text_map`, and `pages` outputs.

The generic GOLD row at `data/raw/gold_ecosystem_paths.tsv:311` carries 46 organism assertions but has no exact `data/raw/gold_path_triads.tsv` row, so the generated record correctly has a source-attestation count and no environmental-parameter claims. The two over-merged source paths at `data/raw/gold_ecosystem_paths.tsv:1175` and `:1211` both carry zero organism, study, biosample, and total assertions, so omitting `assertion_count` and `assertion_unit` for those two attestations is supported.

The direct generated children under the over-merged parents show why the exact merges are consequential. `data/habitats/engineered/sludge__df43c436.yaml` inherits `DHS reactor` from `Engineered > Bioreactor > DHS reactor > Aerobic > Sludge`; `data/habitats/engineered/biomass__545e678f.yaml` inherits `SSF (Solid state fermentation)` from `Engineered > Bioreactor > SSF (Solid state fermentation) > Aerobic > Biomass`. Those edges can be true for the DHS- and SSF-specific child paths, but they are not broader parents of the generic ENVO aerobic-bioreactor identity.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-AEROBIC-BIOREACTOR-001 | major | Two narrower GOLD source concepts are exact-grounded into the generic `ENVO:00002126` `aerobic bioreactor` record. `Engineered > Bioreactor > SSF (Solid state fermentation) > Aerobic` denotes an aerobic SSF context, and `Engineered > Bioreactor > DHS reactor > Aerobic` denotes an aerobic DHS reactor context; neither is exact to all aerobic bioreactors. The over-merge also makes the generic ENVO record a generated child of `SSF (Solid state fermentation)` and `DHS reactor`, which reverses the true broader/narrower direction. | Update the `habitatmech:GOLD.2ee55ba737` and `habitatmech:GOLD.0b917b1e6b` rows in `curation/decisions.tsv`; if either concept stays minted, add `curation/term_requests.tsv` definitions with true genera and rerun the seed. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Replace the `GROUND ENVO:00002126` row for `habitatmech:GOLD.2ee55ba737` with a decision that preserves the SSF-specific aerobic concept, most likely `GROUND_AS_PARENT ENVO:00002126 aerobic bioreactor NARROW` plus an authored `curation/term_requests.tsv` definition under `habitatmech:GOLD.2ee55ba737`.

2. Replace the `GROUND ENVO:00002126` row for `habitatmech:GOLD.0b917b1e6b` with a decision that preserves the DHS-specific aerobic concept, most likely `GROUND_AS_PARENT ENVO:00002126 aerobic bioreactor NARROW` plus an authored `curation/term_requests.tsv` definition under `habitatmech:GOLD.0b917b1e6b`.

3. Keep the `habitatmech:GOLD.904dea8017` exact grounding to `ENVO:00002126` unless a future curator finds evidence that GOLD's top-level `Engineered > Bioreactor > Aerobic` bucket is itself narrower than the ENVO term.

4. Regenerate the corpus rather than editing `data/habitats/engineered/aerobic_bioreactor.yaml` directly.

## Follow-up Checks

- `just seed`
- `just seed-canary ENVO:00002126`
- `just seed-canary habitatmech:GOLD.2ee55ba737`
- `just seed-canary habitatmech:GOLD.0b917b1e6b`
- Inspect `data/habitats/engineered/aerobic_bioreactor.yaml` and confirm it keeps `ENVO:00002123` but no longer lists `habitatmech:GOLD.24cf427e7d` or `habitatmech:GOLD.3af6ca6cc3` under `parent_habitats`.
- Inspect the regenerated SSF- and DHS-specific aerobic records and confirm `ENVO:00002126` is retained as their broader parent, not their exact identity.
- `just seed-apply --force`
- `just validate data/habitats/engineered/aerobic_bioreactor.yaml`
- `just validate-strict data/habitats/engineered/aerobic_bioreactor.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-aerobic_bioreactor.md' -print` included ignored files and found no pre-existing exact report for this record before this file was written.
- The unsupported parents are not caused by a hand edit: `just verify-corpus --max-diffs 1` reproduced all 3206 generated records exactly from maintained inputs.
- Exact hidden/ignored-inclusive searches for `ENVO:00002126`, `aerobic_bioreactor`, `habitatmech:GOLD.904dea8017`, `habitatmech:GOLD.2ee55ba737`, `habitatmech:GOLD.0b917b1e6b`, `Engineered > Bioreactor > Aerobic`, `Engineered > Bioreactor > SSF (Solid state fermentation) > Aerobic`, and `Engineered > Bioreactor > DHS reactor > Aerobic` found the cited ontology, raw GOLD, path-lock, decision, and generated rows, and no maintained input that repairs the over-merge.
