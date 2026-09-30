# YAML Record Review: olfactory system

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/olfactory_system.yaml`
- Started UTC: `2026-09-30T18:11:44Z`
- Finished UTC: `2026-09-30T18:11:56Z`
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `UBERON:0005725` |
| Label | `olfactory system` |
| Stable slug | `olfactory_system` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained/generated | generated from committed source inventories by `scripts/seed_from_sources.py` |
| Path lock | `data/habitats/PATHS.tsv:1091` pins `UBERON:0005725` to `olfactory_system` |
| Source attestation | `GOLD`, `gold.ecosystem:7813`, `Host-associated > Fish > Olfactory system`, `skos:exactMatch` |

This is the generated GOLD record for the Fish source path
`Host-associated > Fish > Olfactory system`. The source row has three collapsed
GOLD ecosystem node IDs and no direct organism, biosample, study, or GOLD triad
evidence rows that should be serialized onto this record.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/olfactory_system.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/olfactory_system.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records expected, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just worklist --status all --out /tmp/habitat_worklist_fish_olfactory_system.tsv` | Passed; wrote 953 ungrounded rows. This `EXACT` target is outside the exported worklist rows. |
| `uv run python scripts/habitat_report.py --out /tmp/habitatmech_fish_olfactory_system_report.tsv` | Passed; wrote the per-record TSV. The TSV reports this target as `HOST_ASSOCIATED`, `EXACT`, `SEEDED`, GOLD-attested, with a definition, 2 parents, 0 parameters, 0 taxa, and 0 causal graphs. |

## Identity and Grounding

The generated identity is sound. `data/raw/gold_ecosystem_paths.tsv:1951`
contains the exact source row `Host-associated > Fish > Olfactory system`, with
leaf label `Olfactory system`, depth 3, three collapsed GOLD ecosystem node IDs,
zero aggregate assertions, and source IDs
`gold.ecosystem:7813|gold.ecosystem:7814|gold.ecosystem:7815`. The generated
source attestation uses the first of those node IDs, preserves the full source
path with `skos:exactMatch`, and notes the three-ID collapse.

`UBERON:0005725` is the appropriate exact identity. The vendored ontology slice
labels it `olfactory system` and defines it as a sensory system capable of
olfaction, which matches the GOLD source-path leaf. The record copies that
definition and attributes it to UBERON.

The two generated parents are traceable to maintained inputs:

| Parent | Support | Review |
|---|---|---|
| `UBERON:0005726` | `data/raw/ontology_subclass_edges.tsv:11545` asserts `UBERON:0005725 rdfs:subClassOf UBERON:0005726`, and `data/raw/ontology_terms.tsv:13285` labels `UBERON:0005726` `chemosensory system`. | Supported as the ontology parent for olfactory system. |
| `habitatmech:GOLD.3d529a667e` | `data/raw/gold_ecosystem_paths.tsv:33` contains the immediate GOLD parent path `Host-associated > Fish`; `curation/decisions.tsv:429`, `curation/term_requests.tsv:8`, and `data/habitats/host_associated/fish.yaml` curate that record as `fish-associated environment`. | Supported as the source-path parent for fish-associated environments. |

The exact `Olfactory system` label is not a local host-associated collision.
Exact ignored/hidden-inclusive searches of `data/habitats/host_associated`
found no other record whose label or source label is `Olfactory system` or
`olfactory system`.

## Evidence

The record has no curator-authored causal graphs, characteristic taxa,
environmental parameters, authored discussions, datasets, or record-level
literature evidence, so there are no claim-level citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| The exact identifier is pinned to the reviewed slug. | `data/habitats/PATHS.tsv:1091` | Supported exactly. |
| GOLD has the Fish `Olfactory system` path with three collapsed upstream node IDs. | `data/raw/gold_ecosystem_paths.tsv:1951` | Supported exactly. |
| The first collapsed GOLD node ID is the only node ID serialized in the generated YAML. | Exact ignored/hidden-inclusive searches for `gold.ecosystem:7813`, `gold.ecosystem:7814`, and `gold.ecosystem:7815` under `data/raw`, `data/habitats`, `curation`, `history`, `research`, `reports/yaml_record_review`, and `pages/habitats` | Supported; `gold.ecosystem:7813` appears in the raw path row and target YAML, while `gold.ecosystem:7814` and `gold.ecosystem:7815` appear only in the raw path row. |
| The record should not serialize a GOLD `assertion_count`, `characteristic_taxa`, or `environmental_parameters` from the committed GOLD side tables. | `src/habitatmech/seed.py`, `data/raw/gold_ecosystem_paths.tsv:1951`, and exact ignored/hidden-inclusive searches of `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_studies.tsv`, and `data/raw/gold_path_triads.tsv` for the Fish olfactory-system path | Supported; `seed.py` serializes GOLD `assertion_count` only from `gold_ecosystem_paths.tsv` `organism_count`, which is zero for this path, and the GOLD side tables have no rows for the target path. |
| `Olfactory pit` is the immediate GOLD child concept under this source path. | `data/raw/gold_ecosystem_paths.tsv:1952` and `data/habitats/host_associated/olfactory_pit.yaml` | Supported; the child record points to `UBERON:0005725` as a parent. |
| The target page renders the same identity and provenance as the YAML. | `pages/habitats/olfactory-system-uberon-0005725.html` | Supported; the page shows `UBERON:0005725`, `HOST_ASSOCIATED`, `EXACT`, `SEEDED`, the UBERON definition, both broader habitats, and the single GOLD source attestation with no assertion count. |
| No item-level curator decision, term request, causal-graph overlay, history record, research report, or prior exact review has been maintained for this target. | Exact ignored/hidden-inclusive searches for `UBERON:0005725`, `olfactory_system`, `gold.ecosystem:7813`, `gold.ecosystem:7814`, `gold.ecosystem:7815`, and the Fish `Olfactory system` source path under `curation`, `history`, `research`, `reports/yaml_record_review`, and `data/habitats` | Supported; those searches found the path lock, generated target, rendered page, generated child records, ontology rows, and the curated Fish parent, but no target-specific maintained curation or review artifact. |

Unsupported or over-scoped claims: None found.

## Completeness

The generated record is complete for the maintained inputs currently available:

- The ontology identifier, ontology label, UBERON definition, UBERON definition
  source, GOLD label, first GOLD ecosystem node ID, full Fish source path,
  `skos:exactMatch` predicate, and three-node collapse note are present.
- `parent_habitats` preserves both broader meanings needed here: the UBERON
  `chemosensory system` parent and the immediate Fish source-path parent.
- `mapping_status` remains `SEEDED`, which is correct because no item-level
  `curation/decisions.tsv` row has reviewed this Fish source path.
- The record correctly has no serialized `assertion_count`, synonyms,
  characteristic taxa, environmental parameters, causal graphs, datasets,
  discussions, or record-level literature evidence.
- iModulonDB was not applicable because this source bucket names no gene, locus,
  regulator, transcriptomic dataset, or strain-level expression claim.

Exact ignored/hidden-inclusive searches covered the Fish source path, the target
identifier, the target slug, the three GOLD ecosystem node IDs,
`UBERON:0005725`, `UBERON:0005726`, the local same-label space, and the GOLD
biosample, study, and triad side tables. They found the cited raw row, path
lock, generated record, rendered page, immediate GOLD parent and children,
UBERON ontology rows, and no target-specific maintained curation, causal-graph,
history, research, or exact review artifact.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If future curation promotes this seeded record to reviewed status, preserve the
UBERON identity, the `UBERON:0005726` parent, and the Fish source-path parent
unless the committed GOLD hierarchy or vendored UBERON slice changes.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future item-level review row, run:

- `just seed`
- `just seed-canary UBERON:0005725`
- `just validate data/habitats/host_associated/olfactory_system.yaml`
- `just validate-strict data/habitats/host_associated/olfactory_system.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -name '*olfactory_system*.md' -print` found no pre-existing exact target report, and `find` included ignored files under the searched directory.
- The worklist TSV did not contain `UBERON:0005725`; this target is `EXACT`, while the exported `/tmp/habitat_worklist_fish_olfactory_system.tsv` contained 953 ungrounded backlog rows.
- The report TSV row at `/tmp/habitatmech_fish_olfactory_system_report.tsv:1091` is `UBERON:0005725	olfactory system	HOST_ASSOCIATED	EXACT	SEEDED	GOLD	1	0	True	2	0	0	0	data/habitats/host_associated/olfactory_system.yaml`.
