# Cycle 6 Stage 5 Grouped Remediation Validation Report (`excretory_system__22ee753c`..`fecal`)

## 1. Surgical Curation & Corpus Verification

- **Authoritative Curation Edits**:
  - `curation/gold_parent_exclusions.tsv`: 18 guarded rows prepended (`#2304`).
  - `curation/term_requests.tsv` & `curation/term_requests/envo_robot_template.tsv`: 4 rows updated (`habitatmech:GOLD.5c89d5e294`, `habitatmech:GOLD.9bfd135cfa` -> `UBERON:0004176` `REPLACE`; `habitatmech:GOLD.0a69f87c03`, `habitatmech:GOLD.28f9330745` -> `ENVO:01001055` `REPLACE`; `#2304`).
  - `curation/decisions.tsv`: 7 rows updated + 1 `REVIEW` row added (`habitatmech:GOLD.4d81fdaa51`, `habitatmech:GOLD.aceda5f881` -> `GROUND_AS_PARENT` `BTO:0000260`; `habitatmech:GOLD.5d27b319ee`, `habitatmech:GOLD.b84283af7d` -> `GROUND_AS_PARENT` `BTO:0002087`; `habitatmech:GOLD.5c89d5e294`, `habitatmech:GOLD.9bfd135cfa` -> `CONFIRM_UNGROUNDED` notes synchronized; `habitatmech:GOLD.97989ecf5e` -> `CLOSE`; `habitatmech:GOLD.2ab65bac9e` -> `REVIEW`; `#2304`, `#2305`).
  - `curation/definition_source_label_exclusions.tsv`: 1 guarded row prepended (`habitatmech:GOLD.6c8238add0`, `Extracellular` -> `molluscan gill extracellular environment`; `#2305`).
- **Exact 22-Record Corpus Diff**:
  - `data/habitats/host_associated/excretory_system__22ee753c.yaml`
  - `data/habitats/host_associated/excretory_system__37f93bb9.yaml`
  - `data/habitats/host_associated/external_genitalia.yaml`
  - `data/habitats/host_associated/external_organs.yaml`
  - `data/habitats/host_associated/external_organs__aed6edb3.yaml`
  - `data/habitats/host_associated/external_soft_tissue_zone.yaml`
  - `data/habitats/host_associated/extracellular.yaml`
  - `data/habitats/host_associated/extracellular__3f7afaf4.yaml`
  - `data/habitats/host_associated/extracellular_symbionts.yaml`
  - `data/habitats/host_associated/eye.yaml`
  - `data/habitats/host_associated/eye__59a4c665.yaml`
  - `data/habitats/host_associated/eye__810dedbb.yaml`
  - `data/habitats/host_associated/eye_ciliary_body.yaml`
  - `data/habitats/host_associated/eye_ciliary_body__832768c5.yaml`
  - `data/habitats/host_associated/eye_vitreous_chamber.yaml`
  - `data/habitats/host_associated/eye_vitreous_chamber__b4eddfc1.yaml`
  - `data/habitats/host_associated/fallopian_tubes.yaml`
  - `data/habitats/host_associated/fallopian_tubes__c41e0038.yaml`
  - `data/habitats/host_associated/fascia.yaml`
  - `data/habitats/host_associated/fascia__1f6c9c1a.yaml`
  - `data/habitats/host_associated/fat_body.yaml`
  - `data/habitats/host_associated/feather.yaml`
  - All other 3,187 habitat records remain byte-identical.

## 2. Fresh Remediation Review Bundles (`reviews/structured/`)

- Saved 22 `kind: record` remediation review bundles (`20261107T050001Z-excretory_system__22ee753c-remediation` through `20261107T050022Z-feather-remediation`) with `previous_occurrences`, `EPREV`, and `related_reviews` linking to their Stage 4 predecessor bundles (`20261106T194810Z-excretory_system__22ee753c-record` through `20261106T194832Z-feather-record`):
  - All 23 actionable findings (21 in `#2304` and 2 in `#2305`, with `external_genitalia` resolving 2 findings) are explicitly reconciled as `resolved`, while the 13 `#1398` findings on the `NARROW` records remain explicitly reconciled as `open`.
  - All Stage 4 structured review bundles (`20261106T1948*`) and Stage 4 workflow artifacts (`reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-04/revision-0001/`) remain byte-identical.

## 3. Validation Checks Executed

- `.venv/bin/python -m pytest -o cache_dir=/tmp/pytest_cache tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py`: `2 passed` (verifies counterfactual regression and 22-record surgical diff).
- `.venv/bin/python scripts/record_review.py check --require-reviews`: passed across all saved structured review bundles.
- `.venv/bin/python scripts/run_qc.py`: all quality gates passed (`3,209` records valid, `868` history records valid, corpus verification exact).
- `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`: passed (`0` unaccepted drift).
