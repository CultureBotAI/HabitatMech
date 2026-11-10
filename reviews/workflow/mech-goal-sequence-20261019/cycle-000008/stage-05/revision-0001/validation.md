# Cycle 8 Stage 5 Grouped Remediation Validation Report (`finger`..`free_living_state`)

## 1. Surgical Curation & Corpus Verification

- **Authoritative Curation Edits**:
  - `curation/decisions.tsv` & `data/habitats/PATHS.tsv`: 1 row updated (`habitatmech:GOLD.80220dc4d4` changed from `APPROVE_REMAP` `BTO:0006514` to `ITEM`-level `CONFIRM_UNGROUNDED` with `target_id=UBERON:0000029`, `relation=parent`), 1 `ITEM`-level `CONFIRM_UNGROUNDED` row added (`habitatmech:PREGO.ce9c3a92e9` with `target_id=BTO:0000464`, `relation=xref`), and 2 `ITEM`-level `NOT_APPLICABLE` rows added (`habitatmech:PREGO.267811fd7a` with `target_id=BTO:0002292` and `habitatmech:PREGO.6c4660c2ae` with `target_id=BTO:0001551`, `relation=xref`, `#2334`), with matching `PATHS.tsv` identifier updates preserving file paths.
  - `curation/term_requests.tsv` & `curation/term_requests/envo_robot_template.tsv`: 1 row updated (`habitatmech:GOLD.3d529a667e` `exact_synonym` -> `fish host environment`, `#2336`) and 2 rows added (`habitatmech:PREGO.ce9c3a92e9` `flagellate-associated environment` under `ENVO:01001000` `REPLACE`; `habitatmech:GOLD.80220dc4d4` `mammalian forelimb lymph node` under `UBERON:0000029` `REPLACE`, `#2334`).
  - `curation/definition_source_label_exclusions.tsv`: 3 guarded rows prepended (`habitatmech:GOLD.3d529a667e` `#2336`; `habitatmech:PREGO.ce9c3a92e9` and `habitatmech:GOLD.80220dc4d4` `#2334`).
  - `curation/gold_parent_exclusions.tsv`: 8 guarded rows prepended (`habitatmech:GOLD.52f22e84ee`, `habitatmech:GOLD.cd6e81f421`, `habitatmech:GOLD.bd1664969c`, `habitatmech:GOLD.8997340b18`, `habitatmech:GOLD.fe78a4c113` on `foregut__*`; `habitatmech:GOLD.9558a262cc` on `BTO:0000480` `forestomach`; `habitatmech:GOLD.319c3f351e` on `frass`; `habitatmech:GOLD.67f3cde908` on `frass__c029dd2b`, `#2335`).
- **Exact 13-Record Corpus Diff**:
  - `data/habitats/host_associated/fish.yaml`
  - `data/habitats/host_associated/flagellate.yaml`
  - `data/habitats/host_associated/flagellum.yaml`
  - `data/habitats/host_associated/foregut__6bc8c43a.yaml`
  - `data/habitats/host_associated/foregut__c14450a8.yaml`
  - `data/habitats/host_associated/foregut__ce63e8ab.yaml`
  - `data/habitats/host_associated/foregut__d14a54ae.yaml`
  - `data/habitats/host_associated/foregut__ee6a8f74.yaml`
  - `data/habitats/host_associated/foreleg.yaml`
  - `data/habitats/host_associated/forestomach.yaml`
  - `data/habitats/host_associated/frass.yaml`
  - `data/habitats/host_associated/frass__c029dd2b.yaml`
  - `data/habitats/host_associated/free_living_state.yaml`
  - All other 3,196 habitat records remain byte-identical.

## 2. Fresh Remediation Review Bundles (`reviews/structured/`)

- Saved 13 `kind: record` remediation review bundles (`20261109T215001Z-fish-remediation` through `20261109T215013Z-free_living_state-remediation`) with `previous_occurrences`, `EPREV`, and `related_reviews` linking to their Stage 4 predecessor bundles (`20261109T181011Z-fish-record` through `20261109T181033Z-free_living_state-record`):
  - All 17 actionable findings (`8` in `#2334`, `8` in `#2335`, and `1` in `#2336`) are explicitly reconciled as `resolved` (`verdict: pass_with_limitations` on the 6 records without `#1398` findings and `verdict: needs_curation` on the 7 `foregut__*` and `frass*` records that retain open `#1398` findings).
  - All Stage 4 structured review bundles (`20261109T1810*`, `20261109T181100Z*`) and Stage 4 workflow artifacts (`reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/`) remain byte-identical.

## 3. Validation Checks Executed

- `.venv/bin/python -m pytest tests/test_finger_to_free_living_state_review_repairs.py`: `2 passed` (verifies counterfactual regression and 13-record surgical diff).
- `.venv/bin/python scripts/record_review.py check --require-reviews`: passed across all saved structured review bundles.
- `.venv/bin/python scripts/run_qc.py`: all quality gates passed (`3,209` records valid, `879` history records valid, corpus verification exact).
- `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`: passed (`0` unaccepted drift).
