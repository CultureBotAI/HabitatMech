# Cycle 5 Stage 5 Validation & Fresh Remediation Review Summary

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `5`
- **Stage:** `5` (`resolve_review_findings`)
- **Revision:** `1`
- **Source Revision:** `f0c857592f79534eeb3701824a58eb7b5fcefef3`

## 1. Native Writers & Derived Product Rebuild

1. **Authoritative Curation Inputs Updated:**
   - `curation/gold_parent_exclusions.tsv`: Added 13 guarded rows excluding GOLD context-only parents across `epicuticular_wax`, `epithelial_lining_fluid`, `erythrocyte`, `esophageal_ulcer`, `esophagus__25614af3`, `esophagus__2ce9b1a3`, `esophagus__d8421c5e`, `esophagus__e0ae9e65`, `esophagus__e4629951`, `ethmoid_bone`, `eustachian_tube`, `eustachian_tube__a8583033`, and `excretory_system` ([#2295](https://github.com/CultureBotAI/HabitatMech/issues/2295)).
   - `curation/term_requests.tsv` & `curation/term_requests/envo_robot_template.tsv`: Cleared bare host-organism label `'Equidae-Horse'` from `exact_synonym` on `habitatmech:BACDIVE.09c3544e85` (`equidae_horse`, `'equid-associated environment'`) ([#2296](https://github.com/CultureBotAI/HabitatMech/issues/2296)).
   - `curation/definition_source_label_exclusions.tsv`: Added guarded row for `habitatmech:BACDIVE.09c3544e85` (`Equidae-Horse`, `equid-associated environment`) suppressing automatic retention in `synonyms` (`SOURCE_SYNONYM_EXCLUDED`) while preserving verbatim `source_attestations` ([#2296](https://github.com/CultureBotAI/HabitatMech/issues/2296)).
   - `curation/decisions.tsv`: Updated `habitatmech:GOLD.55cb603eb1` (`Host-associated > Mammals: Human > Skeletal system > Bone > Scull: Ethmoid` on `ethmoid_bone`, `UBERON:0001679`) from `EXACT` to `CLOSE` ([#2296](https://github.com/CultureBotAI/HabitatMech/issues/2296)).
2. **Native Writers & Rebuild Commands Executed:**
   - `.venv/bin/python scripts/build_term_requests.py` — regenerated `curation/term_requests/envo_robot_template.tsv` (`671` ENVO terms).
   - `.venv/bin/python scripts/seed_from_sources.py --apply --force` — regenerated the 14 targeted habitat YAML records in `data/habitats/host_associated/`.
   - Rebuilt `data/text_map/` (`bundle: 1506ded0b9ba8448cdfe46ee25f1cec01313e6bf0a17e0b0b27865a3f06f8d8d`).
   - `.venv/bin/python scripts/build_redirects.py && .venv/bin/python scripts/render_pages.py` — verified `data/habitats/RETIRED.tsv` (`750` redirects, 0 new retired paths) and rendered `3209` habitat pages, `750` redirect stubs, `8` categories, and `696` term requests.
   - `.venv/bin/python scripts/check_docs.py --write` — synchronized `README.md` statistics.
   - Created provenance history logs `history/other/gold_parent_exclusions/2026-11-05T151500Z-antigravity-229501.yaml` and `history/other/definition_source_label_exclusions/2026-11-05T151510Z-antigravity-229601.yaml`.

## 2. Fresh Structured Remediation Reviews (`reviews/structured/`)

Saved 14 immutable `kind: record` remediation review bundles in `reviews/structured/` (`20261105T152501Z-epicuticular_wax-remediation` through `20261105T152514Z-excretory_system-remediation`) linked to their Stage 4 predecessor bundles (`20261105T051510Z-epicuticular_wax-record` through `20261105T051533Z-excretory_system-record`) via `EPREV`, `findings[].previous_occurrences`, and `related_reviews`:
- All 15 actionable findings (13 in `#2295` and 2 in `#2296`, with `ethmoid_bone` resolving both `ethmoid-bone-context-parent` and `ethmoid-bone-scull-ethmoid-exact-synonym`) are explicitly reconciled as `resolved`, while the 8 `#1398` findings on `esophagus__*`, `eustachian_tube*`, and `excretory_system` remain explicitly reconciled as `open`.
- All Stage 4 structured review bundles (`20261105T0515*`, `20261105T0516*`) and Stage 4 workflow artifacts (`reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/`) remain byte-identical.

## 3. Validation Checks Executed

- `.venv/bin/python -m pytest tests/test_epicuticular_wax_to_excretory_system_review_repairs.py -v -p no:cacheprovider`: `2 passed` (verifies counterfactual regression and 14-record surgical diff).
- `.venv/bin/python -m pytest tests/test_record_review_contract.py -v -p no:cacheprovider`: `4 passed` (verifies all saved structured review bundles, predecessor lineage, and input digests).
- `.venv/bin/python scripts/run_qc.py`: all quality gates passed (`3,209` records valid, `864` history records valid, corpus verification exact).
