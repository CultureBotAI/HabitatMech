# Stage 5 Validation & Fresh Remediation Review Summary

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `1`
- **Stage:** `5` (`resolve_review_findings`)
- **Revision:** `1`
- **Source Revision:** `2ec3d103f44a563f8cc4562f33e82d364039fa81`

## 1. Native Writers & Derived Product Rebuild

1. **Authoritative Curation Inputs Updated:**
   - `curation/gold_parent_exclusions.tsv`: Added 11 guarded rows excluding whole-organ, whole-system, bone-remains, and disease-to-anatomy GOLD context parents for `dental_plaque__8396e8ec`, `dentin__be69daef`, `dentition`, `dermal_papilla`, `dermatitis`, `dermatitis__d991f62d`, `dermis`, `descending_colon`, `diabetic_foot_ulcer_dfu`, `diaphragm__3c058609`, and `diaphragm__fbd202d9` ([#2255](https://github.com/CultureBotAI/HabitatMech/issues/2255)).
   - `curation/term_requests.tsv` & `curation/term_requests/envo_robot_template.tsv`: Synchronized parent ontology terms for the updated `term_requests.tsv` rows (`dental_plaque__8396e8ec`, `dentin__be69daef`, `dermatitis`, `diaphragm__3c058609`, `diaphragm__fbd202d9`) and removed bare `'Diatoms'` from `exact_synonym` on `habitatmech:GOLD.1276bea544` ([#2255](https://github.com/CultureBotAI/HabitatMech/issues/2255), [#2256](https://github.com/CultureBotAI/HabitatMech/issues/2256)).
   - `curation/definition_source_label_exclusions.tsv`: Added guarded row for `habitatmech:GOLD.1276bea544` (`Diatoms`, `GOLD`, `Host-associated > Algae > Diatoms`) ([#2256](https://github.com/CultureBotAI/HabitatMech/issues/2256)).
2. **Native Writers & Rebuild Commands Executed:**
   - `.venv/bin/python scripts/build_envo_template.py` — regenerated `curation/term_requests/envo_robot_template.tsv` cleanly (`1103` rows).
   - `.venv/bin/python scripts/generate_habitats.py` — regenerated only the 12 targeted habitat YAML files in `data/habitats/host_associated/`.
   - `.venv/bin/python scripts/build_text_map.py` — rebuilt `data/text_map/` (`source_fingerprint_sha256: 5e4158bc4b6fbdb21274399ffaee83e0fa610dc50f9a036af54ad7cc518220fa`).
   - `.venv/bin/python scripts/render_pages.py` — re-rendered the 12 affected HTML pages in `pages/habitats/` and index pages.
   - Created provenance history logs `history/other/gold_parent_exclusions/2026-10-22T063700Z-antigravity-225501.yaml` and `history/other/definition_source_label_exclusions/2026-10-22T063710Z-antigravity-225601.yaml`.

## 2. Fresh Structured Remediation Reviews (`reviews/structured/`)

Saved 12 immutable `kind: record` remediation review bundles in `reviews/structured/` (`20261022T065801Z-dental_plaque__8396e8ec-remediation` through `20261022T065812Z-diatoms-remediation`) with `supersedes` links to their Stage 4 predecessor bundles:
- 9 records (`dentition`, `dermal_papilla`, `dermatitis`, `dermatitis__d991f62d`, `dermis`, `descending_colon`, `diabetic_foot_ulcer_dfu`, `diatoms`, and the context-parent findings on `dental_plaque__8396e8ec`, `dentin__be69daef`, `diaphragm__3c058609`, `diaphragm__fbd202d9`) verified all 12 resolved findings (`resolution_state: resolved`) and preserved single open-owner invariants for the 4 records (`dental_plaque__8396e8ec`, `dentin__be69daef`, `diaphragm__3c058609`, `diaphragm__fbd202d9`) that also participate in deferred #1398.
- All Stage 4 structured review bundles (`20261022T014510Z-dental_plaque__8396e8ec-record` through `20261022T014600Z-dental_plaque_to_digestive_system-category`) and Stage 4 workflow artifacts (`reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/`) remain byte-identical.

## 3. Validation Checks Executed

- `.venv/bin/python -m pytest tests/test_dental_to_diaphragm_review_repairs.py -v --no-cov`: `2 passed` (verifies counterfactual regression and 12-record surgical diff).
- `.venv/bin/python -m pytest tests/test_record_review_contract.py tests/test_record_review_publication.py -v --no-cov`: `6 passed` (verifies all saved structured review bundles, supersession chains, single open-owner keys, input digests, and `origin/main` publication reachability).
- `.venv/bin/python scripts/validate_habitats.py`: `0 errors` across all `1,813` habitat YAML records.
- `.venv/bin/python scripts/check_history.py`: `0 errors`.
- `.venv/bin/python scripts/check_docs.py`: `0 errors`.
