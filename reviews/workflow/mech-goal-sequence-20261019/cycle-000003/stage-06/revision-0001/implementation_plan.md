# Cycle 3 Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`)

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage:** Cycle `3`, Stage `6` (`infrastructure`)
- **Source revision:** `502235f61cb14384acf12c1d838750d54a02e5f2`
- **Scope frozen at:** `2026-10-31T10:17:03Z`
- **Frozen snapshot artifact:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md`
- **Frozen snapshot SHA-256:** `54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`

## 1. Frozen Intake Inventory (`2026-10-31T10:17:03Z`)

At the Stage 6 cutoff (`2026-10-31T10:17:03Z`), `INFRA_TASKS.md` was frozen into `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md` (`sha256: 54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`).

| Task ID | Originating Cycle / Stage | Issue | Frozen Status | Pending Work in Cycle 3 Stage 6 |
| --- | --- | --- | --- | --- |
| `habitatmech-infra-0001` | Cycle 1, Stage 3 (`protein_examples`) | [#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250) | `resolved` (Cycle 1 Stage 6, PR #2258) | None (`status: resolved`) |

- **Total entries in `INFRA_TASKS.md`:** `1` (`habitatmech-infra-0001`)
- **Entries with `status: resolved`:** `1` (`habitatmech-infra-0001`)
- **Pending entries (`status` in `note`, `open`, `deferred`):** `0`

## 2. Cycle 3 Intake Audit Across Stages 1–5

During Cycle 3 Stages 1–5, all curation and review goals operated cleanly on existing repository schemas, validators, and native writers without adding new tasks to `INFRA_TASKS.md`:

1. **Stage 1 (`open_issues`, PR #2269, commit `0324b7c75`):** Curated and defined the 3 remaining admissible microbial habitats from open issues; zero new infrastructure tasks added to `INFRA_TASKS.md`.
2. **Stage 2 (`causal_graphs`, PR #2270, commit `92efe06f2`):** Curated 10 new evidence-backed mechanism overlays (`43 -> 53` causal-graph curation files) and regenerated habitat records and HTML pages; zero new infrastructure tasks added to `INFRA_TASKS.md`.
3. **Stage 3 (`protein_examples`, PR #2272, commit `e4e1a0c35`):** Curated verified UniProtKB protein examples and source-limited scope notes across Cycle 3 causal-graph overlays using the `ProteinExample` schema and renderer delivered in Cycle 1 Stage 6 (`habitatmech-infra-0001`); zero new infrastructure tasks added to `INFRA_TASKS.md`.
4. **Stage 4 (`record_reviews`, PR #2275, commit `73f5de1ff`):** Executed record and category cohort review for the frozen 24-record lexical slice `data/habitats/host_associated/ear_discharge.yaml` through `data/habitats/host_associated/empyema.yaml` (`24` `kind: record` bundles and `1` `kind: category` bundle in `reviews/structured/`, `23` carried-forward `#1398` findings from Cycle 2 Stage 5 plus `14` new open findings = `37` total carried forward); recorded `infra_tasks: []`.
5. **Stage 5 (`review_resolution`, PR #2278, commit `502235f61`):** Grouped all 37 carried-forward Stage 4 review findings into 3 real GitHub issue groups ([#2276](https://github.com/CultureBotAI/HabitatMech/issues/2276), [#2277](https://github.com/CultureBotAI/HabitatMech/issues/2277), [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398)), resolved 13 actionable curation findings across 11 records (8 GOLD context-parent and genus/parent grounding repairs in `#2276` and 5 exact-synonym repairs in `#2277`) with 11 fresh structured remediation review bundles in `reviews/structured/`, and explicitly carried forward 24 deferred `#1398` mapping-endpoint contract findings in `carry_forward_ids` (`infra_tasks: []`).

## 3. Dependency-Aware Implementation Plan (`explicit_empty_plan: true`)

Per `workflow/mech-workflow.yaml` (`infrastructure_policy.explicit_empty_plan: true`) and the `kg_microbe_workflows` Stage 6 evidence contract (which scopes `infra_tasks` to the frozen notebook's non-resolved tasks `status != "resolved"`):

- **Selected tasks for implementation:** None (`0` pending tasks in the frozen `INFRA_TASKS.md` snapshot).
- **Dependency graph:** Empty (no pending tasks or prerequisite edges in the frozen `INFRA_TASKS.md` scope).
- **Issue-linked dispositions:**
  - `habitatmech-infra-0001` ([#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250)): Remains `resolved` from Cycle 1 Stage 6 (PR #2258); verified in active production use during Cycle 2 Stage 3 (PR #2262) and Cycle 3 Stage 3 (PR #2272).
- **Deferred / carried-forward infrastructure tasks (`carry_forward_ids`):** `[]` (none in the frozen `INFRA_TASKS.md` scope).
- **Review-resolution carry-forward boundary:** The 24 deferred `mapping-endpoint-contract` review findings under [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) (`G-source-attestation-mapping-endpoint-contract`) remain tracked in the Cycle 3 Stage 5 evidence manifest (`reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml`, now indexed in `reviews/workflow/latest.yaml`) for subsequent review lineage. Per the Stage 6 intake protocol ("never expand the frozen task-ID scope"), the frozen `INFRA_TASKS.md` scope at `2026-10-31T10:17:03Z` is preserved without retroactive scope expansion.

## 4. Acceptance Criteria

1. `reviews/workflow/latest.yaml` is synchronized with `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/habitatmech/verified-evidence-index.json`, recording all 8 verified stage closures through Cycle 3 Stage 5 (PR #2278).
2. `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md` matches the frozen `INFRA_TASKS.md` byte-for-byte (`sha256: 54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`).
3. `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/evidence.yaml` validates cleanly under `kg_microbe_workflows validate-evidence --root . --required-output infra_snapshot --required-output implementation_plan --required-output validation`.
4. All repository validation and QC gates (`verify_corpus.py`, `render_pages.py --check`, `validate_causal_graph_curations.py`, `validate_history.py history`, `check_docs.py --check`, `check_vendored_sync.sh`, `validate_id_label_correspondence.py`) pass with 0 errors.
