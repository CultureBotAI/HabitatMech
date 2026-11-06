# Stage 6 Infrastructure Implementation Plan — Cycle 5 (`mech-goal-sequence-20261019`)

## Scope Freeze

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `5`
- **Stage:** `6` (`infrastructure`)
- **Source revision (`main` HEAD at freeze):** `d42e47bbbc5ac99158bd0e7bde6f9a9e50fc777a`
- **Supervisor-frozen `infra_scope` cutoff (`scope_frozen_at`):** `2026-11-05T21:30:38Z`
- **Frozen ledger:** `INFRA_TASKS.md` (`sha256: 54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`)
- **Snapshot copy:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/infra_snapshot.md` (`sha256: 54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`)

## Frozen Intake Inventory

| Task ID | Issue | Status at Freeze | Priority | Dependencies | Cycle 5 Stage 6 Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `habitatmech-infra-0001` | [CultureBotAI/HabitatMech#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250) | `resolved` (implemented in Cycle 1 Stage 6, PR #2258) | `high` | `none` | None — already `resolved` and closed in Cycle 1 Stage 6; retained in `INFRA_TASKS.md` for audit provenance |

### Cycle 5 Stages 1–5 Intake Audit

Across Cycle 5 Stages 1–5 (`d42e47bbbc5ac99158bd0e7bde6f9a9e50fc777a`), zero new infrastructure tasks (`note`, `open`, or `deferred`) were appended to `INFRA_TASKS.md`:

1. **Stage 1 (`add_records`, PR #2289, merge commit `402e744a03b6216b6af6b9a4f334b472a2f447c0`):** Audited the bounded habitat frontier (`3,209` total habitat records, `671` curated definitions in `curation/term_requests.tsv`) and synchronized `reviews/workflow/latest.yaml` through Cycle 4 Stage 6; no new habitat records or infrastructure requirements were identified.
2. **Stage 2 (`causal_graphs`, PR #2292, merge commit `4730e9f500c904e36a1d08f5551fa5d1fd07157b`):** Added 10 new evidence-backed causal mechanism overlays (`dairy_processing_facility.yaml`, `diffuse_flow.yaml`, `fruiting_body.yaml`, `leaf_surface.yaml`, `oil_contaminated_soil.yaml`, `rock_dwelling_subaerial_biofilms.yaml`, `solar_salterns.yaml`, `subpolar_coniferous_forest_biome.yaml`, `surface_soil.yaml`, `tundra_biome.yaml`, bringing the corpus from 63 to 73 overlays across 160 eligible defined `REVIEWED` records) using existing causal-graph overlay infrastructure.
3. **Stage 3 (`protein_examples`, PR #2293, merge commit `215b23c90244e634e64f88fa2c1a2a3bb011880a`):** Audited all 10 new `GENE_OR_PROTEIN` causal mechanism nodes introduced in Cycle 5 Stage 2 (`dairy_biofilm_matrix_exopolysaccharides_and_amyloids` in `dairy_processing_facility.yaml`, `sox_sulfur_oxidation_multienzyme_system` in `diffuse_flow.yaml`, `trehalose_6_phosphate_synthase_phosphatase` in `fruiting_body.yaml`, `syringafactin_lipopeptide_synthetase` in `leaf_surface.yaml`, `alkB_alkane_1_monooxygenase_system` in `oil_contaminated_soil.yaml`, `scytonemin_biosynthetic_enzymes` in `rock_dwelling_subaerial_biofilms.yaml`, `bacteriorhodopsin_and_xanthorhodopsin_proton_pumps` in `solar_salterns.yaml`, `manganese_peroxidase_and_laccase` in `subpolar_coniferous_forest_biome.yaml`, `photolyase_and_trehalose_synthase` in `surface_soil.yaml`, `particulate_methane_monooxygenase_pmoCAB` in `tundra_biome.yaml`), populated 20 verified UniProtKB protein exemplars (`54 -> 74` corpus total across `23 -> 29` `GENE_OR_PROTEIN` nodes) on 6 overlays, and documented source-limited community-guild notes on 4 overlays (`diffuse_flow.yaml`, `fruiting_body.yaml`, `oil_contaminated_soil.yaml`, `tundra_biome.yaml`) directly through the `ProteinExample` schema/validator/renderer shipped in Cycle 1 Stage 6 (`habitatmech-infra-0001`).
4. **Stage 4 (`record_review`, PR #2294, merge commit `f0c857592f79534eeb3701824a58eb7b5fcefef3`):** Audited the frozen 24-record lexical slice `data/habitats/host_associated/epicuticular_wax.yaml` through `data/habitats/host_associated/excretory_system.yaml` (`24` `kind: record` bundles and `1` `kind: category` cohort bundle in `reviews/structured/`), carried forward 30 deferred `#1398` findings from Cycle 4 Stage 5, and recorded 23 new open findings (`13` GOLD context-parent defects, `2` synonym/scope defects, and `8` new `#1398` mapping-endpoint contract defects = `53` total open/deferred findings in `carry_forward_ids`); no new repository infrastructure tasks were opened in `INFRA_TASKS.md`.
5. **Stage 5 (`resolve_review_findings`, PR #2297, merge commit `d42e47bbbc5ac99158bd0e7bde6f9a9e50fc777a`):** Partitioned all 53 Stage 4 findings into 3 issue groups (`G-epicuticular-wax-to-excretory-system-parent-grounding-repairs` on [#2295](https://github.com/CultureBotAI/HabitatMech/issues/2295) with 13 resolved findings, `G-epicuticular-wax-to-excretory-system-synonym-scope-repairs` on [#2296](https://github.com/CultureBotAI/HabitatMech/issues/2296) with 2 resolved findings, and `G-source-attestation-mapping-endpoint-contract` on [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) with 38 deferred findings carried forward — 30 from Cycles 1–4 plus 8 from Cycle 5 Stage 4), resolved all 15 actionable curation findings across 14 records via `curation/gold_parent_exclusions.tsv`, `curation/term_requests.tsv`, `curation/definition_source_label_exclusions.tsv`, `curation/decisions.tsv`, and 14 post-remediation structured review bundles in `reviews/structured/`. Note: [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) is tracked as a Stage 4/5 record-review finding group (`G-source-attestation-mapping-endpoint-contract` in `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml`) rather than an `INFRA_TASKS.md` task item.

## Explicit Empty Dependency-Aware Implementation Plan

Per `workflow/parent/mech-cycle.yaml` (`infrastructure_policy.explicit_empty_plan: true`, inherited by `workflow/mech-workflow.yaml`), when `INFRA_TASKS.md` has zero pending (`note`, `open`, or `deferred`) tasks at the Stage 6 freeze cutoff:

1. **Selected Tasks for Implementation (`0`):** None. The sole task in `INFRA_TASKS.md` (`habitatmech-infra-0001`, [#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250)) was implemented, validated, and marked `resolved` in Cycle 1 Stage 6 (PR #2258).
2. **Deferred / Carried-Forward Infrastructure Tasks (`0`):** None in `INFRA_TASKS.md`.
3. **Tracked Review Index Synchronization:** Update `reviews/workflow/latest.yaml` from the supervisor-maintained `verified-evidence-index.json` so that the verified Cycle 5 Stage 5 closure entry (PR #2297, merge commit `d42e47bbbc5ac99158bd0e7bde6f9a9e50fc777a`) is recorded in the repository's tracked index.
4. **Stage 6 Evidence Package & Validation:**
   - Freeze `INFRA_TASKS.md` to `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/infra_snapshot.md` with exact matching SHA-256 (`54631ad2605e30fc085f06b51f7e8b1a8015f55b754a2d0fedd978d2e14b32a8`).
   - Run `kg_microbe_workflows validate --profile workflow/mech-workflow.yaml`, `.venv/bin/python scripts/run_qc.py`, and `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`.
   - Record all validation outputs in `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/validation.md` and `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/evidence.yaml` (`outcome: no_findings`).
