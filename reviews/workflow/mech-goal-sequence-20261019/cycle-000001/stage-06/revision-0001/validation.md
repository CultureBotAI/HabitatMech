# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019`, Cycle 1, Stage 6)

- **Run ID:** `mech-goal-sequence-20261019`
- **Repository:** `CultureBotAI/HabitatMech`
- **Cycle / Stage:** Cycle `1`, Stage `6` (`infrastructure`)
- **Task Resolved:** `habitatmech-infra-0001` ([#2250](https://github.com/CultureBotAI/HabitatMech/issues/2250))

## 1. Schema and Causal-Graph Overlay Validation

- `python scripts/validate_causal_graph_curations.py`:
  - Validated all `33` causal-graph curation files (`33` graphs) against `HabitatCausalGraphCuration` in `src/habitatmech/schema/habitatmech.yaml` and `_validate_graph_integrity` in `src/habitatmech/curate/causal_graphs.py`.
  - Confirmed all `15` verified UniProtKB exemplars across `curation/causal_graphs/fresh_water.yaml` (`UniProtKB:P0C0S1`, `UniProtKB:P0A742`), `curation/causal_graphs/root_nodule.yaml` (`UniProtKB:P02233`, `UniProtKB:O48668`, `UniProtKB:O80405`, `UniProtKB:Q1M7Z2`, `UniProtKB:Q1M7Z3`, `UniProtKB:Q1M7Z4`, `UniProtKB:Q0RAV4`, `UniProtKB:Q0RAV5`, `UniProtKB:Q0RAV6`), and `curation/causal_graphs/sea_water.yaml` (`UniProtKB:Q4FMH4`, `UniProtKB:Q4FKZ8`, `UniProtKB:Q4FM26`, `UniProtKB:Q4FMK2`) pass closed-mode LinkML validation and node-level integrity checks.

## 2. Corpus Regeneration, Site Rendering, and History Checks

- `python scripts/verify_corpus.py`:
  - `expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0` (`corpus reproduces exactly from data/raw/`).
- `python scripts/render_pages.py`:
  - `rendered 3209 habitat pages, 720 redirect stubs, 8 categories, 650 term requests -> pages`.
- `python scripts/validate_history.py history`:
  - `No issues found; 846 history record(s) valid against src/habitatmech/schema/history.yaml`.
- `bash scripts/check_vendored_sync.sh`:
  - `OK: 22 governed artifacts match the pinned claw revision`.
- `python scripts/check_docs.py --check`:
  - `README corpus statistics are current`.
- `python scripts/check_curation_floor.py`:
  - `curation floor: no identifier lost since origin/main, HEAD`.

## 3. Unit Tests and Workflow Contract Validation

- `pytest tests/test_causal_graph_curations.py tests/test_schema.py tests/test_render_pages.py`:
  - Verified positive loading of `protein_examples` on `GENE_OR_PROTEIN` nodes, rejection of `protein_examples` on non-`GENE_OR_PROTEIN` nodes, rejection of duplicate `protein_examples` accessions on the same node, rejection of `protein_examples` lacking evidence, schema coverage of `ProteinExampleRoleEnum` and `UniProtKB`/`NCBITaxon` prefixes, and rendered HTML links on `fresh-water-envo-00002011.html`, `root-nodule-envo-01000164.html`, and `sea-water-envo-00002149.html`.
- `python -m kg_microbe_workflows check-repo --root .`:
  - Confirmed `workflow/mech-workflow.yaml` and `INFRA_TASKS.md` validate cleanly against the pinned workflow contract.
