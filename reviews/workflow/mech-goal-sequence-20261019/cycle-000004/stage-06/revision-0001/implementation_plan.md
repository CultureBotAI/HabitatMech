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

1. **Stage 1 (`add_records`, PR #2280, merge commit `a0cd2c701d7b326836a82644eace24f70973861c`):** Curated bounded frontier `engineered` habitat definitions (`8` new definitions in `curation/term_requests.tsv` lines 665–672: `habitatmech:GOLD.013b99db03`, `habitatmech:GOLD.0d77d00b06`, `habitatmech:GOLD.3af6ca6cc3`, `habitatmech:GOLD.4a2450370b`, `habitatmech:GOLD.5f3cbd7563`, `habitatmech:GOLD.c07aaa941d`, `habitatmech:GOLD.e474187df8`, `habitatmech:GOLD.f07ee97491`) and ITEM curation decisions in `curation/decisions.tsv` (`3,209` total habitat records); no schema, validator, or generator changes were needed.
2. **Stage 2 (`causal_graphs`, PR #2281, merge commit `903a9788a1d13e9e381ff8884bf0ed71ba708efe`):** Added 10 new evidence-backed causal mechanism overlays (`abyssalpelagic_zone.yaml`, `bone_marrow.yaml`, `clay_soil.yaml`, `feces.yaml`, `liver.yaml`, `lung.yaml`, `lymph_node.yaml`, `mammary_gland.yaml`, `planetary_boundary_layer.yaml`, `sedimentary_rock.yaml`, bringing the corpus to 63 overlays) using existing causal-graph overlay infrastructure.
3. **Stage 3 (`protein_examples`, PR #2282, merge commit `ad20de05c38d4fadf667b5c579eef50496b31b02`):** Audited all 10 new `GENE_OR_PROTEIN` causal mechanism nodes introduced in Cycle 4 Stage 2 (`piezophilic_respiratory_complexes` in `abyssalpelagic_zone.yaml`, `granulysin_and_perforin` in `bone_marrow.yaml`, `Fe_III_reductase_MtrCAB` in `clay_soil.yaml`, `mucin_sulfatases_and_glycoside_hydrolases` in `feces.yaml`, `type_III_secretion_system_effectors` in `liver.yaml`, `esx_1_secretion_system` in `lung.yaml`, `f1_capsular_antigen_caf1` in `lymph_node.yaml`, `fibronectin_binding_proteins_fnbpa_fnbpb` in `mammary_gland.yaml`, `ice_nucleation_protein_inaZ` in `planetary_boundary_layer.yaml`, `dsrAB_dissimilatory_sulfite_reductase` in `sedimentary_rock.yaml`) and populated 18 verified UniProtKB protein exemplars (`36 -> 54` corpus total across `13 -> 23` `GENE_OR_PROTEIN` nodes) directly through the `ProteinExample` schema/validator/renderer shipped in Cycle 1 Stage 6 (`habitatmech-infra-0001`).
4. **Stage 4 (`record_review`, PR #2283, merge commit `95a1eb1b6a5b18b8a5c3b135222b1118f7506ef0`):** Audited the frozen 24-record lexical slice `data/habitats/host_associated/empyema_drain.yaml` through `data/habitats/host_associated/epibionts.yaml` (`24` `kind: record` bundles and `1` `kind: category` cohort bundle in `reviews/structured/`), carried forward 24 deferred `#1398` findings from Cycle 3 Stage 5, and recorded 16 new open findings (`6` parent/grounding defects, `4` exact-synonym provenance defects, and `6` new `#1398` mapping-endpoint contract defects = `40` total open findings in `carry_forward_ids`); no new repository infrastructure tasks were opened in `INFRA_TASKS.md`.
5. **Stage 5 (`resolve_review_findings`, PR #2287, merge commit `13ae9f8a89e7b002257470e911453a6c7d38c0f5`):** Partitioned all 40 Stage 4 findings into 3 issue groups (`G-empyema-drain-to-epibionts-parent-grounding-repairs` on [#2285](https://github.com/CultureBotAI/HabitatMech/issues/2285) with 6 resolved findings, `G-empyema-drain-to-epibionts-exact-synonym-repairs` on [#2286](https://github.com/CultureBotAI/HabitatMech/issues/2286) with 4 resolved findings, and `G-source-attestation-mapping-endpoint-contract` on [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) with 30 deferred findings carried forward — 24 from Cycles 1–3 plus 6 from Cycle 4 Stage 4), resolved all 10 actionable curation findings across 9 records via `curation/decisions.tsv`, `curation/gold_parent_exclusions.tsv`, `curation/definition_source_label_exclusions.tsv`, `curation/term_requests.tsv`, `data/habitats/PATHS.tsv`, and 9 post-remediation structured review bundles in `reviews/structured/`. Note: [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) is tracked as a Stage 4/5 record-review finding group (`G-source-attestation-mapping-endpoint-contract` in `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-05/revision-0001/evidence.yaml`) rather than an `INFRA_TASKS.md` task item.

## Explicit Empty Dependency-Aware Implementation Plan

Per `workflow/parent/mech-cycle.yaml` (`infrastructure_policy.explicit_empty_plan: true`, inherited by `workflow/mech-workflow.yaml`), when `INFRA_TASKS.md` has zero pending (`note`, `open`, or `deferred`) tasks at the Stage 6 freeze cutoff:

1. **Selected Tasks for Implementation (`0`):** None. The sole task in `INFRA_TASKS.md` (`habitatmech-infra-0001`, [#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250)) was implemented, validated, and marked `resolved` in Cycle 1 Stage 6 (PR #2258).
2. **Deferred / Carried-Forward Infrastructure Tasks (`0`):** None in `INFRA_TASKS.md`.
3. **Tracked Review Index Synchronization:** Update `reviews/workflow/latest.yaml` from the supervisor-maintained `verified-evidence-index.json` so that the verified Cycle 4 Stage 5 closure entry (PR #2287, merge commit `13ae9f8a89e7b002257470e911453a6c7d38c0f5`) is recorded in the repository's tracked index.
4. **Stage 6 Evidence Package & Validation:**
   - Freeze `INFRA_TASKS.md` to `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md` with exact matching SHA-256 (`54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`).
   - Run `kg_microbe_workflows validate --profile workflow/mech-workflow.yaml`, `just qc`, and `just validate-products`.
   - Record all validation outputs in `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/validation.md` and `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/evidence.yaml` (`outcome: no_findings`).
