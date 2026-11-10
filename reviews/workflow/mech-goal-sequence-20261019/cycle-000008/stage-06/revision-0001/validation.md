# Stage 6 Infrastructure Validation Report — Cycle 8 (`mech-goal-sequence-20261019`)

## Validation Summary

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `8`
- **Stage:** `6` (`infrastructure`)
- **Source revision (`main` HEAD at freeze):** `6c89a863ce26add77a5b642009635af3a9580c31`
- **Supervisor-frozen `infra_scope` cutoff (`scope_frozen_at`):** `2026-11-10T06:27:40Z`
- **Outcome:** `no_findings` (zero pending `note`, `open`, or `deferred` tasks in frozen `INFRA_TASKS.md`; explicit empty implementation plan executed per `workflow/mech-workflow.yaml`).

## Executed Checks

### 1. Frozen `INFRA_TASKS.md` Snapshot Integrity

- **Command:** `shasum -a 256 INFRA_TASKS.md reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/infra_snapshot.md`
- **Result:** PASS
  - `INFRA_TASKS.md`: `54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/infra_snapshot.md`: `54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`
  - Matches supervisor-frozen `infra_scope.sha256` (`54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`) at `2026-11-10T06:27:40Z`.

### 2. Workflow Profile & Stage 6 Evidence Manifest Validation

- **Command:** `env PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --parent workflow/parent/mech-cycle.yaml --schema workflow/parent/workflow.yaml`
- **Result:** `Workflow profile valid` (exit code `0`)
- **Command:** `env PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --required-output infra_snapshot --required-output implementation_plan --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/evidence.yaml`
- **Result:** `Goal evidence valid` (exit code `0`)

### 3. Authoritative Quality Gates (`.venv/bin/python scripts/run_qc.py`)

- **Command:** `.venv/bin/python scripts/run_qc.py`
- **Result:** `All HabitatMech quality gates passed.` (exit code `0`)
  - **Lint (`ruff`):** All checks passed.
  - **Documentation:** `README corpus statistics are current`.
  - **Raw-data provenance:** `provenance current: 14 committed inventories, 2 GOLD sources`.
  - **Tests (`pytest`):** `1250 passed, 27 skipped`.
  - **Curation history:** `879 history record(s) valid against src/habitatmech/schema/history.yaml`.
  - **Closed-schema validation:** `3209` files scanned, `0` files with `ERROR`.
  - **Causal-graph curations:** `validated 103 causal-graph curation file(s) with 103 graph(s)`.
  - **Curation floor:** No identifier lost since `origin/main`, `HEAD`.
  - **Corpus reproduction:** `expected 3209 records, found 3209 on disk` (0 diffs).
  - **Redirects:** `RETIRED.tsv is current (757 redirects)`.
  - **Generated site:** `rendered 3209 habitat pages, 757 redirect stubs, 8 categories, 701 term requests` (`pages/ is in step with the corpus`).
  - **Term-request packets:** `term-request table is current (676 terms)`.

### 4. Ontology ID-to-Label Correspondence (`.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`)

- **Command:** `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- **Result:** `All id↔label pairs correspond.` (exit code `0`)
  - `OK_CANONICAL: 1209`
  - `OK_SYNONYM: 1`
  - `OK_EXCEPTION: 5`
  - `SKIPPED_NO_ADAPTER: 2098`
