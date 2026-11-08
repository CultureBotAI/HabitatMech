# Cycle 7 Stage 5 Grouped Remediation Validation Report (`fecal__0d8696a2`..`fin`)

## 1. Surgical Curation & Corpus Verification

- **Authoritative Curation Edits**:
  - `curation/gold_parent_exclusions.tsv`: 5 guarded rows prepended (`habitatmech:GOLD.53337a753d`, `habitatmech:GOLD.d11c365b20`, `habitatmech:GOLD.3671b973b2`, `habitatmech:GOLD.515763f493` on `UBERON:0001988` `feces`; `habitatmech:GOLD.8634ec53de` on `UBERON:0008897` `fin`; `#2318`).
  - `curation/term_requests.tsv` & `curation/term_requests/envo_robot_template.tsv`: 2 rows updated (`habitatmech:BACDIVE.e6b73de092` `exact_synonym` -> `cat-associated environment|feline host environment`, `#2319`; `habitatmech:GOLD.1ad500c492` `parent_mode` -> `REPLACE`, `#2318`) and 3 rows added (`habitatmech:GOLD.c8a2e380c1` `mammalian fetus-associated environment` under `ENVO:01001055` `REPLACE`; `habitatmech:GOLD.f2a6418a5c` `human fetus-associated environment` under `ENVO:2100003` `REPLACE`; `habitatmech:GOLD.fb56a964a6` `human fibroma lesion` under `NCIT:C3824` `REPLACE`, `#2318`).
  - `curation/decisions.tsv`: 1 row updated (`habitatmech:GOLD.fb56a964a6` promoted from `CLASS` to `ITEM`) and 2 `ITEM`-level `CONFIRM_UNGROUNDED` rows added (`habitatmech:GOLD.c8a2e380c1` and `habitatmech:GOLD.f2a6418a5c` with `object_id=BTO:0000449`, `relation=xref`, `#2318`).
  - `curation/definition_source_label_exclusions.tsv`: 4 guarded rows prepended (`habitatmech:BACDIVE.e6b73de092` `#2319`; `habitatmech:GOLD.c8a2e380c1`, `habitatmech:GOLD.f2a6418a5c`, `habitatmech:GOLD.fb56a964a6` `#2318`).
- **Exact 7-Record Corpus Diff**:
  - `data/habitats/host_associated/feces.yaml`
  - `data/habitats/host_associated/felidae_cat.yaml`
  - `data/habitats/host_associated/fetal_tissue.yaml`
  - `data/habitats/host_associated/fetus.yaml`
  - `data/habitats/host_associated/fetus__250e9844.yaml`
  - `data/habitats/host_associated/fibroma.yaml`
  - `data/habitats/host_associated/fin.yaml`
  - All other 3,202 habitat records remain byte-identical.

## 2. Fresh Remediation Review Bundles (`reviews/structured/`)

- Saved 7 `kind: record` remediation review bundles (`20261108T154501Z-feces-remediation` through `20261108T154507Z-fin-remediation`) with `previous_occurrences`, `EPREV`, and `related_reviews` linking to their Stage 4 predecessor bundles (`20261108T114918Z-feces-record` through `20261108T114933Z-fin-record`):
  - All 9 actionable findings (`8` in `#2318` and `1` in `#2319`, with `fetus` and `fetus__250e9844` each resolving both their `life-stage-parent` and `mapping-endpoint-contract` findings) are explicitly reconciled as `resolved` with `verdict: pass_with_limitations`.
  - All Stage 4 structured review bundles (`20261108T1149*`) and Stage 4 workflow artifacts (`reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-04/revision-0001/`) remain byte-identical.

## 3. Validation Checks Executed

- `.venv/bin/python -m pytest tests/test_fecal_0d8696a2_to_fin_review_repairs.py`: `2 passed` (verifies counterfactual regression and 7-record surgical diff).
- `.venv/bin/python scripts/record_review.py check --require-reviews`: passed across all saved structured review bundles.
- `.venv/bin/python scripts/run_qc.py`: all quality gates passed (`3,209` records valid, `870` history records valid, corpus verification exact).
- `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`: passed (`0` unaccepted drift).
