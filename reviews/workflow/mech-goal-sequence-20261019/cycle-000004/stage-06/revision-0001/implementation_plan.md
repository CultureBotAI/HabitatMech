# Stage 6 Infrastructure Implementation Plan — Cycle 4 (`mech-goal-sequence-20261019`)

## Scope Freeze

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `4`
- **Stage:** `6` (`infrastructure`)
- **Source revision (`main` HEAD at freeze):** `13ae9f8a89e7b002257470e911453a6c7d38c0f5`
- **Supervisor-frozen `infra_scope` cutoff (`scope_frozen_at`):** `2026-11-04T08:11:21Z`
- **Frozen ledger:** `INFRA_TASKS.md` (`sha256: 54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`)
- **Snapshot copy:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md` (`sha256: 54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`)

## Frozen Intake Inventory

| Task ID | Issue | Status at Freeze | Priority | Dependencies | Cycle 4 Stage 6 Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `habitatmech-infra-0001` | [CultureBotAI/HabitatMech#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250) | `resolved` (implemented in Cycle 1 Stage 6, PR #2258) | `high` | `none` | None — already `resolved` and closed in Cycle 1 Stage 6; retained in `INFRA_TASKS.md` for audit provenance |

### Cycle 4 Stages 1–5 Intake Audit

Across Cycle 4 Stages 1–5 (`13ae9f8a89e7b002257470e911453a6c7d38c0f5`), zero new infrastructure tasks (`note`, `open`, or `deferred`) were appended to `INFRA_TASKS.md`:

1. **Stage 1 (`add_records`, PR #2280, merge commit `a0cd2c701d7b326836a82644eace24f70973861c`):** Grounded and defined 10 unreviewed microbial habitats (`ENVO:00002016` sedimentary rock, `ENVO:00002221` clay soil, `ENVO:01000016` abyssalpelagic zone, `ENVO:01000324` planetary boundary layer, `UBERON:0000029` lymph node, `UBERON:0001911` mammary gland, `UBERON:0001988` feces, `UBERON:0002048` lung, `UBERON:0002107` liver, `UBERON:0002371` bone marrow) using existing curation tables (`curation/decisions.tsv`, `curation/term_requests.tsv`); no schema, validator, or generator changes were needed.
2. **Stage 2 (`causal_graphs`, PR #2281, merge commit `903a9788a1d13e9e381ff8884bf0ed71ba708efe`):** Added 10 new evidence-backed causal mechanism overlays (`abyssalpelagic_zone.yaml`, `bone_marrow.yaml`, `clay_soil.yaml`, `feces.yaml`, `liver.yaml`, `lung.yaml`, `lymph_node.yaml`, `mammary_gland.yaml`, `planetary_boundary_layer.yaml`, `sedimentary_rock.yaml`, bringing the corpus to 63 overlays) using existing causal-graph overlay infrastructure.
3. **Stage 3 (`protein_examples`, PR #2282, merge commit `ad20de05c38d4fadf667b5c579eef50496b31b02`):** Audited all 10 new `GENE_OR_PROTEIN` causal mechanism nodes introduced in Cycle 4 Stage 2 (`piezophilic_respiratory_complexes` in `abyssalpelagic_zone.yaml`, `granulysin_and_perforin` in `bone_marrow.yaml`, `Fe_III_reductase_MtrCAB` in `clay_soil.yaml`, `mucin_sulfatases_and_glycoside_hydrolases` in `feces.yaml`, `type_III_secretion_system_effectors` in `liver.yaml`, `esx_1_secretion_system` in `lung.yaml`, `f1_capsular_antigen_caf1` in `lymph_node.yaml`, `fibronectin_binding_proteins_fnbpa_fnbpb` in `mammary_gland.yaml`, `ice_nucleation_protein_inaZ` in `planetary_boundary_layer.yaml`, `dsrAB_dissimilatory_sulfite_reductase` in `sedimentary_rock.yaml`) and populated 18 verified UniProtKB protein exemplars (`36 -> 54` corpus total across `13 -> 23` `GENE_OR_PROTEIN` nodes) directly through the `ProteinExample` schema/validator/renderer shipped in Cycle 1 Stage 6 (`habitatmech-infra-0001`).
4. **Stage 4 (`record_review`, PR #2283, merge commit `95a1eb1b6a5b18b8a5c3b135222b1118f7506ef0`):** Executed bounded 10-record and 5-category reviews across Cycle 4 newly curated records and cohorts. Identified 5 curation findings (`F-C04-001` through `F-C04-005`) and carried forward 30 upstream-blocked `#1398` findings (`F-C01-001` through `F-C01-011`, `F-C02-001` through `F-C02-009`, `F-C03-001` through `F-C03-010`); no new repository infrastructure tasks were opened in `INFRA_TASKS.md`.
5. **Stage 5 (`resolve_review_findings`, PR #2287, merge commit `13ae9f8a89e7b002257470e911453a6c7d38c0f5`):** Resolved all 5 Cycle 4 curation findings (`F-C04-001` through `F-C04-005`) across GitHub issues [#2285](https://github.com/CultureBotAI/HabitatMech/issues/2285) and [#2286](https://github.com/CultureBotAI/HabitatMech/issues/2286) via `curation/gold_parent_exclusions.tsv`, `curation/decisions.tsv`, and `curation/term_requests.tsv`, and explicitly carried forward the 30 deferred `#1398` findings (`F-C01-001` through `F-C01-011`, `F-C02-001` through `F-C02-009`, `F-C03-001` through `F-C03-010`) in the Stage 5 evidence manifest. Note: [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) is tracked as a Stage 4/5 record-review finding group (`G-C04-003` in `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-05/revision-0001/evidence.yaml`) rather than an `INFRA_TASKS.md` task item.

## Explicit Empty Dependency-Aware Implementation Plan

Per `workflow/mech-workflow.yaml` (`stage_overrides.6.parameters.explicit_empty_plan: true`), when `INFRA_TASKS.md` has zero pending (`note`, `open`, or `deferred`) tasks at the Stage 6 freeze cutoff:

1. **Selected Tasks for Implementation (`0`):** None. The sole task in `INFRA_TASKS.md` (`habitatmech-infra-0001`, [#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250)) was implemented, validated, and marked `resolved` in Cycle 1 Stage 6 (PR #2258).
2. **Deferred / Carried-Forward Infrastructure Tasks (`0`):** None in `INFRA_TASKS.md`.
3. **Tracked Review Index Synchronization:** Update `reviews/workflow/latest.yaml` from the supervisor-maintained `verified-evidence-index.json` so that the verified Cycle 4 Stage 5 closure entry (PR #2287, merge commit `13ae9f8a89e7b002257470e911453a6c7d38c0f5`) is recorded in the repository's tracked index.
4. **Stage 6 Evidence Package & Validation:**
   - Freeze `INFRA_TASKS.md` to `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md` with exact matching SHA-256 (`54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`).
   - Run `kg_microbe_workflows validate --profile workflow/mech-workflow.yaml`, `just qc`, and `just validate-products`.
   - Record all validation outputs in `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/validation.md` and `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/evidence.yaml` (`outcome: no_findings`).
