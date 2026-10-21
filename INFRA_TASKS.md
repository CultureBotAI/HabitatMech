# HabitatMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `habitatmech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/HabitatMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
- task_id: habitatmech-infra-0001
  summary: Add typed protein_examples slot on CausalNode and UniProtKB validator/renderer support so organism- and role-scoped UniProtKB exemplars can be attached without conflating subunit/ortholog exemplars with node equivalence.
  status: open
  issue_url: https://github.com/CultureBotAI/HabitatMech/issues/2250
```
<!-- mech-infra-tasks:end -->

## Tasks

### `habitatmech-infra-0001` — Typed `protein_examples` representation on `CausalNode`

- **Originating run / cycle / stage:** `mech-goal-sequence-20261019`, cycle `1`, stage `3` (`protein_examples`)
- **Status:** `open`
- **Issue URL:** https://github.com/CultureBotAI/HabitatMech/issues/2250
- **Priority:** `high`
- **Dependencies:** `none`
- **Observation:** `CausalNode` in `src/habitatmech/schema/habitatmech.yaml` currently only provides `node_id`, `label`, `node_type`, `grounding` (single CURIE), `xrefs` (untyped flat string list), and `description`. In HabitatMech's 33 causal-graph overlays, `GENE_OR_PROTEIN` nodes represent multisubunit protein complexes (`nitrogenase` in `root_nodule.yaml`), multi-family channel classes (`mechanosensitive_channels` in `fresh_water.yaml`), host-plant hemoprotein isoprotein families (`leghemoglobin` in `root_nodule.yaml`), multi-transporter functional classes (`nutrient_transport_systems` in `sea_water.yaml`), or community-level secreted enzyme pools (`extracellular_enzymes` in `biofilm.yaml`, `grassland_soil.yaml`, and `marine_water_body.yaml`). Placing a single subunit or organism ortholog CURIE in `grounding` or untyped `xrefs` would violate `.claude/skills/add-uniprot-protein-examples/SKILL.md` ("Never insert a sibling's unsupported fields or represent a family/complex by one member... Do not use an untyped xref to smuggle in a related ortholog as equivalence") and break `conf/id_label_targets.yaml` (`grounded_causal_nodes` enforces exact `grounding` -> `label` correspondence and has no `UniProtKB:` OAK adapter).
- **Desired outcome:**
  1. Add a structured `ProteinExample` class and multivalued `protein_examples` slot on `CausalNode` in `src/habitatmech/schema/habitatmech.yaml` capturing `accession` (`UniProtKB:...`), `entry_name`, `recommended_name`, `gene_symbol`, `locus_tag`, `taxon_id` (`NCBITaxon:...`), `taxon_name`, `role_in_node` (`subunit`, `family_member`, `strain_exemplar`, `isoprotein`), `sequence_length`, `crc64`, and `evidence` (`EvidenceItem` list).
  2. Update `scripts/validate_causal_graph_curations.py`, `scripts/seed_from_sources.py`, and `scripts/render_pages.py` to validate, propagate, and render `protein_examples` on `CausalNode`.
  3. Backfill the 15 verified active UniProtKB protein exemplars audited during Stage 3 (`UniProtKB:P0C0S1`, `UniProtKB:P0A742`, `UniProtKB:Q1M7Z2`, `UniProtKB:Q1M7Z3`, `UniProtKB:Q1M7Z4`, `UniProtKB:Q0RAV4`, `UniProtKB:Q0RAV5`, `UniProtKB:Q0RAV6`, `UniProtKB:P02233`, `UniProtKB:O48668`, `UniProtKB:O80405`, `UniProtKB:Q4FMH4`, `UniProtKB:Q4FKZ8`, `UniProtKB:Q4FM26`, `UniProtKB:Q4FMK2`) into structured `protein_examples` entries on `fresh_water.yaml`, `root_nodule.yaml`, and `sea_water.yaml`.
- **Evidence paths:**
  - `src/habitatmech/schema/habitatmech.yaml`
  - `conf/id_label_targets.yaml`
  - `curation/causal_graphs/fresh_water.yaml`
  - `curation/causal_graphs/root_nodule.yaml`
  - `curation/causal_graphs/sea_water.yaml`
  - `curation/causal_graphs/biofilm.yaml`
  - `curation/causal_graphs/grassland_soil.yaml`
  - `curation/causal_graphs/marine_water_body.yaml`

