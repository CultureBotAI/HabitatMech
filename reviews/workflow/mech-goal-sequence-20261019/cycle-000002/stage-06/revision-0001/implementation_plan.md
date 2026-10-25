# Cycle 2 Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`)

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage:** Cycle `2`, Stage `6` (`infrastructure`)
- **Source revision:** `e786d4f2243a2147fd554130f5869d24522a3edc`
- **Scope frozen at:** `2026-10-25T16:44:53Z`
- **Frozen snapshot artifact:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md`
- **Frozen snapshot SHA-256:** `54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`

## 1. Frozen Intake Inventory (`2026-10-25T16:44:53Z`)

At the Stage 6 cutoff (`2026-10-25T16:44:53Z`), `INFRA_TASKS.md` was frozen into `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md` (`sha256: 54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`).

| Task ID | Originating Cycle / Stage | Issue | Frozen Status | Pending Work in Cycle 2 Stage 6 |
| --- | --- | --- | --- | --- |
| `habitatmech-infra-0001` | Cycle 1, Stage 3 (`protein_examples`) | [#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250) | `resolved` (Cycle 1 Stage 6, PR #2258) | None (`status: resolved`) |

- **Total entries in `INFRA_TASKS.md`:** `1` (`habitatmech-infra-0001`)
- **Entries with `status: resolved`:** `1` (`habitatmech-infra-0001`)
- **Pending entries (`status` in `note`, `open`, `deferred`):** `0`

## 2. Cycle 2 Intake Audit Across Stages 1–5

During Cycle 2 Stages 1–5, all curation and review goals operated cleanly on existing repository schemas, validators, and native writers without adding new tasks to `INFRA_TASKS.md`:

1. **Stage 1 (`open_issues`, PR #2259, commit `07e61ccdc`):** Curated and defined 33 admissible microbial habitats from open issues; zero new infrastructure tasks added to `INFRA_TASKS.md`.
2. **Stage 2 (`causal_graphs`, PR #2260, commit `e33400fe9`):** Curated 10 evidence-backed mechanism overlays (`43` total causal-graph curation files) and regenerated habitat records and HTML pages; zero new infrastructure tasks added to `INFRA_TASKS.md`.
3. **Stage 3 (`protein_examples`, PR #2262, commit `395f4605d`):** Curated verified UniProtKB protein examples and source-limit notes using the `ProteinExample` schema and renderer delivered in Cycle 1 Stage 6 (`habitatmech-infra-0001`); zero new infrastructure tasks added to `INFRA_TASKS.md`.
4. **Stage 4 (`record_reviews`, PR #2264, commit `6a4778d4c`):** Executed record and category cohort review for the frozen 24-record lexical slice `data/habitats/host_associated/digestive_system__87922027.yaml` through `data/habitats/host_associated/ear_canal__7b012d70.yaml` (`24` `kind: record` bundles and `1` `kind: category` bundle in `reviews/structured/`, `10` carried-forward `#1398` findings from Cycle 1 Stage 5 plus `22` new open findings = `32` total carried forward); recorded `infra_tasks: []`.
5. **Stage 5 (`review_resolution`, PR #2267, commit `e786d4f22`):** Grouped all 32 carried-forward Stage 4 review findings into 3 real GitHub issue groups ([#2265](https://github.com/CultureBotAI/HabitatMech/issues/2265), [#2266](https://github.com/CultureBotAI/HabitatMech/issues/2266), [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398)), resolved 9 actionable curation findings (8 GOLD context-parent exclusions in `#2265` and 1 exact-synonym defect in `#2266`) with 9 fresh structured remediation review bundles in `reviews/structured/`, and explicitly carried forward 23 deferred `#1398` mapping-endpoint contract findings in `carry_forward_ids` (`infra_tasks: []`).

## 3. Dependency-Aware Implementation Plan (`explicit_empty_plan: true`)

Per `workflow/mech-workflow.yaml` (`infrastructure_policy.explicit_empty_plan: true`) and the `kg_microbe_workflows` Stage 6 evidence contract (which scopes `infra_tasks` to the frozen notebook's non-resolved tasks `status != "resolved"`):

- **Selected tasks for implementation:** None (`0` pending tasks in the frozen `INFRA_TASKS.md` snapshot).
- **Dependency graph:** Empty (no pending tasks or prerequisite edges in the frozen `INFRA_TASKS.md` scope).
- **Issue-linked dispositions:**
  - `habitatmech-infra-0001` ([#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250)): Remains `resolved` from Cycle 1 Stage 6 (PR #2258); verified in active production use during Cycle 2 Stage 3 (PR #2262).
- **Deferred / carried-forward infrastructure tasks (`carry_forward_ids`):** `[]` (none in the frozen `INFRA_TASKS.md` scope).
- **Review-resolution carry-forward boundary:** The 23 deferred `mapping-endpoint-contract` review findings under [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) (`G-source-attestation-mapping-endpoint-contract`) remain tracked in the Cycle 2 Stage 5 evidence manifest (`reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml`, now indexed in `reviews/workflow/latest.yaml`) for Cycle 3 Stage 4/5 review lineage. Per the Stage 6 intake protocol ("never expand the frozen task-ID scope"), the frozen `INFRA_TASKS.md` scope at `2026-10-25T16:44:53Z` is preserved without retroactive scope expansion.

## 4. Acceptance Criteria

1. `reviews/workflow/latest.yaml` is synchronized with `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/habitatmech/verified-evidence-index.json`, recording all 5 verified stage closures through Cycle 2 Stage 5 (PR #2267).
2. `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md` matches the frozen `INFRA_TASKS.md` byte-for-byte (`sha256: 54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`).
3. `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/evidence.yaml` validates cleanly under `kg_microbe_workflows validate-evidence --root . --required-output infra_snapshot --required-output implementation_plan --required-output validation`.
4. All repository validation and QC gates (`verify_corpus.py`, `render_pages.py --check`, `validate_causal_graph_curations.py`, `validate_history.py history`, `check_docs.py --check`, `check_vendored_sync.sh`, `validate_id_label_correspondence.py`) pass with 0 errors.
