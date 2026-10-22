# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 1, Stage 6)

- **Run ID:** `mech-goal-sequence-20261019`
- **Repository:** `CultureBotAI/HabitatMech`
- **Cycle / Stage:** Cycle `1`, Stage `6` (`infrastructure`)
- **Source Revision:** `40309c4c50113f19c66dcf385025e40304cc004f`
- **Scope Cutoff (`scope_frozen_at`):** `2026-10-22T10:20:24Z`
- **Frozen Snapshot Artifact:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md` (`sha256: fd06c4fb4c51aeea1a85ebe400d80a5c106b1c9a93555f9d5c25370ec1a9de0c`)

## 1. Frozen Intake Summary

At the supervisor cutoff (`2026-10-22T10:20:24Z`), `INFRA_TASKS.md` contained 1 non-resolved task:

| Task ID | Status at Cutoff | GitHub Issue | Priority | Dependencies | Selected Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `habitatmech-infra-0001` | `open` | [#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250) | `high` | `none` | Implement in Cycle 1 Stage 6 (`status -> resolved`) |

No tasks are blocked or deferred.

## 2. Dependency-Aware Implementation Plan for `habitatmech-infra-0001` (#2250)

### Problem Statement

In HabitatMech's 33 causal-graph overlays, `GENE_OR_PROTEIN` nodes represent multisubunit protein complexes (`nitrogenase_complex` in `root_nodule.yaml`), multi-family channel classes (`mechanosensitive_channels` in `fresh_water.yaml`), host-plant hemoprotein isoprotein families (`leghemoglobin` in `root_nodule.yaml`), multi-transporter functional classes (`compatible_solute_transporter` in `sea_water.yaml`), strain-represented family classes (`proteorhodopsin` in `sea_water.yaml`), or community-level secreted enzyme pools (`extracellular_enzymes` in `biofilm.yaml`, `grassland_soil.yaml`, and `marine_water_body.yaml`). Placing a single subunit or organism ortholog CURIE in `grounding` or untyped `xrefs` would conflate an exemplar with 1:1 node equivalence and violate `conf/id_label_targets.yaml`.

### Implementation Steps (Ordered by Dependency)

1. **LinkML Schema Extension (`src/habitatmech/schema/habitatmech.yaml`):**
   - Declare `UniProtKB: https://www.uniprot.org/uniprotkb/` in `prefixes`.
   - Add `ProteinExampleRoleEnum` with permissible values `subunit`, `family_member`, `strain_exemplar`, and `isoprotein`.
   - Add `ProteinExample` class with required `accession` (`^UniProtKB:([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})$`), `entry_name` (`^[A-Z0-9]{1,10}_[A-Z0-9]{1,5}$`), `recommended_name`, optional `gene_symbol`, optional `locus_tag`, required `taxon_id` (`^NCBITaxon:[0-9]+$`), `taxon_name`, `role_in_node` (`ProteinExampleRoleEnum`), `sequence_length` (`integer >= 1`), `crc64` (`^[0-9A-F]{16}$`), and `evidence` (`EvidenceItem` list).
   - Add multivalued `protein_examples` (`range: ProteinExample`) on `CausalNode`.
2. **Causal-Graph Overlay Integrity Validation (`src/habitatmech/curate/causal_graphs.py`):**
   - Enforce in `_validate_graph_integrity` that `protein_examples` may only appear on nodes with `node_type == "GENE_OR_PROTEIN"`.
   - Enforce that `protein_examples` accessions are unique within a node, have non-blank `accession`, `entry_name`, `recommended_name`, `taxon_id`, `taxon_name`, `role_in_node`, and `crc64`, positive integer `sequence_length`, and non-empty `evidence` items with non-blank `reference`.
3. **HTML Page Projection and Template Rendering (`scripts/render_pages.py`, `src/habitatmech/templates/habitat.html`):**
   - Project `protein_examples` across each causal graph in `render_graphs()`, resolving `accession_iri` (`https://www.uniprot.org/uniprotkb/...`), `taxon_iri` (`http://purl.obolibrary.org/obo/NCBITaxon_...`), and `evidence` links.
   - Render a dedicated `Protein examples` table under each causal graph that contains `protein_examples`.
4. **Overlay Backfill & Corpus Regeneration (`curation/causal_graphs/*.yaml`, `data/habitats/**/*.yaml`, `pages/habitats/*.html`):**
   - Backfill all 15 live-API-verified active UniProtKB protein exemplars from Stage 3 into `curation/causal_graphs/fresh_water.yaml` (`UniProtKB:P0C0S1`, `UniProtKB:P0A742`), `curation/causal_graphs/root_nodule.yaml` (`UniProtKB:P02233`, `UniProtKB:O48668`, `UniProtKB:O80405`, `UniProtKB:Q1M7Z2`, `UniProtKB:Q1M7Z3`, `UniProtKB:Q1M7Z4`, `UniProtKB:Q0RAV4`, `UniProtKB:Q0RAV5`, `UniProtKB:Q0RAV6`), and `curation/causal_graphs/sea_water.yaml` (`UniProtKB:Q4FMH4`, `UniProtKB:Q4FKZ8`, `UniProtKB:Q4FM26`, `UniProtKB:Q4FMK2`).
   - Record curation history in `history/other/causal_graphs/2026-10-22T103500Z-antigravity-225001.yaml`.
   - Regenerate `data/habitats/aquatic/fresh_water.yaml`, `data/habitats/host_associated/root_nodule__0f1c7944.yaml`, and `data/habitats/aquatic/sea_water.yaml` via `scripts/seed_from_sources.py` and re-render `pages/` via `scripts/render_pages.py`.
5. **Skill & Ledger Alignment (`.claude/skills/`, `INFRA_TASKS.md`):**
   - Update `.claude/skills/add-uniprot-protein-examples/SKILL.md` and `.claude/skills/habitatmech-evolve-workflow/SKILL.md` to document `CausalNode.protein_examples` (`ProteinExample`).
   - Update `INFRA_TASKS.md` to mark `habitatmech-infra-0001` as `resolved` with its disposition linked to `#2250`.

## 3. Acceptance Criteria

- `scripts/validate_causal_graph_curations.py` passes across all 33 causal-graph overlays.
- `scripts/seed_from_sources.py --verify` passes with 0 drifted records across all 3,209 habitats.
- `scripts/render_pages.py --check` passes with 0 drifted HTML pages.
- `scripts/validate_id_label_correspondence.py` and `scripts/check_curation_history.py` pass cleanly.
- Unit tests in `tests/test_causal_graph_curations.py`, `tests/test_schema.py`, and `tests/test_render_pages.py` cover positive and negative `protein_examples` validation and HTML rendering.
