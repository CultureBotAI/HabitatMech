# Stage 6 Infrastructure Validation Report — Cycle 4 (`mech-goal-sequence-20261019`)

## Validation Summary

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `4`
- **Stage:** `6` (`infrastructure`)
- **Source revision (`main` HEAD at freeze):** `13ae9f8a89e7b002257470e911453a6c7d38c0f5`
- **Supervisor-frozen `infra_scope` cutoff (`scope_frozen_at`):** `2026-11-04T08:11:21Z`
- **Outcome:** `no_findings` (zero pending `note`, `open`, or `deferred` tasks in frozen `INFRA_TASKS.md`; explicit empty implementation plan executed per `workflow/mech-workflow.yaml`).

## Executed Checks

### 1. Frozen `INFRA_TASKS.md` Snapshot Integrity

- **Command:** `shasum -a 256 INFRA_TASKS.md reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md`
- **Result:** PASS
  - `INFRA_TASKS.md`: `54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md`: `54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`
  - Matches supervisor-frozen `infra_scope.sha256` (`54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`) at `2026-11-04T08:11:21Z`.

### 2. Workflow Profile & Stage 6 Evidence Manifest Validation

- **Command:** `env PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml`
- **Result:** `Workflow profile valid` (exit code `0`)
- **Command:** `env PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --required-output infra_snapshot --required-output implementation_plan --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/evidence.yaml`
- **Result:** `Goal evidence valid` (exit code `0`)

### 3. Authoritative Quality Gates (`just qc`)

- **Command:** `just qc`
- **Result:** `All HabitatMech quality gates passed.` (exit code `0`)
  - **Lint (`ruff`):** All checks passed.
  - **Documentation:** `README corpus statistics are current`.
  - **Raw-data provenance:** `provenance current: 14 committed inventories, 2 GOLD sources`.
  - **Tests (`pytest`):** `1223 passed, 3 skipped`.
  - **Curation history:** `860 history record(s) valid against src/habitatmech/schema/history.yaml`.
  - **Closed-schema validation:** `3209` files scanned, `0` files with `ERROR`.
  - **Causal-graph curations:** `validated 63 causal-graph curation file(s) with 63 graph(s)`.
  - **Curation floor:** No identifier lost since `origin/main`, `HEAD`.
  - **Corpus reproduction:** `verified 3209 file(s) in data/habitats` (0 diffs).
  - **Redirects:** `743 redirect(s) current`.
  - **Generated site:** `verified 3965 file(s) in pages` (`3209` records, `743` redirects, `8` categories, `690` term requests).
  - **Term-request packets:** `verified 8 file(s) in curation/term_requests`.

### 4. Ontology ID-to-Label Correspondence (`just validate-products`)

- **Command:** `just validate-products`
- **Result:** `All id↔label pairs correspond.` (exit code `0`)
  - `OK_CANONICAL: 1196`
  - `OK_SYNONYM: 1`
  - `OK_EXCEPTION: 5`
  - `SKIPPED_NO_ADAPTER: 2071`
