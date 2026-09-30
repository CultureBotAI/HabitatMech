# YAML Record Review: intromittent organ

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/intromittent_organ.yaml`
- Started UTC: 2026-09-30T21:31:00Z
- Finished UTC: 2026-09-30T21:41:26Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `UBERON:0008811` |
| Label | `intromittent organ` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Stable slug | `intromittent_organ` |
| Generated path | `data/habitats/host_associated/intromittent_organ.yaml` |
| Path lock | `data/habitats/PATHS.tsv:1114` maps `UBERON:0008811` to `intromittent_organ` |
| Source attestation | `GOLD`, `gold.ecosystem:7574`, `Host-associated > Fish > Reproductive system > Intromittent organ`, `skos:exactMatch` |

The target is a generated UBERON/GOLD record for the Fish source path
`Host-associated > Fish > Reproductive system > Intromittent organ`. It carries
the UBERON definition and exact synonyms, one GOLD source attestation, one
UBERON ontology parent, one Fish source-path parent, no environmental
parameters, no characteristic taxa, no local evidence, no causal graphs, no
discussions, and no datasets.

The YAML itself is generated from `data/raw/` plus the source inventories and
does not have a maintained `curation/decisions.tsv` row. Future curation should
change maintained inputs and then regenerate instead of hand-editing
`data/habitats/host_associated/intromittent_organ.yaml` or `pages/`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/intromittent_organ.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/intromittent_organ.yaml` | Passed; scanned 1 file, found 0 files with `ERROR`, and wrote 0 error rows. |
| `just validate-causal-all` | Passed; validated 32 causal-graph curation files with 32 graphs. |
| `just validate-history` | Passed; 77 history records are valid against the vendored history schema. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --status all --out /tmp/habitatmech-fish-intromittent-organ-worklist.tsv` | Started cleanly but produced no stdout or TSV after repeated live polls; killed with exit 143 after confirming the exact `curation_worklist.py` process chain was still live. |
| `just report --out /tmp/habitatmech-fish-intromittent-organ-report.tsv` | Printed the aggregate 3206-record corpus sections but produced no requested TSV after repeated live polls; killed with exit 143 after confirming the exact `habitat_report.py` process chain was still live. |
| `git diff --check` | Passed; no unstaged whitespace or patch errors. |
| `git diff --cached --check` | Passed; no staged whitespace or patch errors. |

No schema, strict, causal-graph, history, term-request, or corpus reproduction
validator was skipped. The two TSV-producing corpus diagnostics above were
attempted but unavailable.

## Identity and Grounding

The generated identity is sound:

- `data/raw/ontology_terms.tsv:13368` vendors `UBERON:0008811` with canonical
  label `intromittent organ`, the definition copied into the generated record,
  and exact synonyms `aedeagus`, `copulatory organ`, and `penis`.
- `data/raw/gold_ecosystem_paths.tsv:1958` is the exact raw row for
  `Host-associated > Fish > Reproductive system > Intromittent organ`. It
  records leaf label `Intromittent organ`, depth `4`, two collapsed GOLD
  ecosystem node IDs, zero organism assertions, zero study assertions, zero
  biosample assertions, zero total assertions, and node IDs
  `gold.ecosystem:7574|gold.ecosystem:7575`.
- The generated YAML emits the first collapsed source ID,
  `gold.ecosystem:7574`, preserves the full Fish source path, records
  `skos:exactMatch`, and keeps the collapsed-node note that points back to
  `data/raw/gold_ecosystem_paths.tsv`.
- `data/habitats/PATHS.tsv:1114` pins `UBERON:0008811` to
  `intromittent_organ`, matching the reviewed YAML path.
- The rendered page
  `pages/habitats/intromittent-organ-uberon-0008811.html` repeats the same
  identifier, source path, UBERON definition, source-path parent, ontology
  parent, source attestation, and generated seeding event.

The `EXACT` grounding is supported by label and hierarchy. GOLD's leaf label
`Intromittent organ` differs from UBERON's canonical label only by case, and
the two direct GOLD child paths support this intended anatomy sense:
`Clasper` maps to `UBERON:0010516` `clasper`, a subclass of
`UBERON:0008811`, while `Gonopodium` remains a minted fish child that also
keeps `UBERON:0008811` as its broader anatomical parent.

The two generated parents are traceable to maintained inputs:

| Parent | Support | Review |
|---|---|---|
| `UBERON:0003135` | `data/raw/ontology_subclass_edges.tsv:11652` asserts `UBERON:0008811 rdfs:subClassOf UBERON:0003135`, and `data/raw/ontology_terms.tsv:13191` labels that parent `male reproductive organ`. | Supported as the UBERON ontology parent. |
| `habitatmech:GOLD.cad831cd73` | `data/raw/gold_ecosystem_paths.tsv:677` is the immediate GOLD parent path `Host-associated > Fish > Reproductive system`; `data/habitats/PATHS.tsv:2780` maps that source path to `reproductive_system__f30f7ffb`. | Supported as the Fish reproductive-system source-path parent. |

## Evidence

The record has no curator-authored causal graphs, characteristic taxa,
environmental parameters, authored discussions, datasets, or record-level
literature evidence, so there are no claim-level citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| The exact identifier is pinned to the reviewed slug. | `data/habitats/PATHS.tsv:1114` | Supported exactly. |
| GOLD has the Fish `Intromittent organ` path with two collapsed upstream node IDs. | `data/raw/gold_ecosystem_paths.tsv:1958` | Supported exactly. |
| The record should not serialize a GOLD `assertion_count`, `characteristic_taxa`, or `environmental_parameters`. | `data/raw/gold_ecosystem_paths.tsv:1958` and exact ignored/hidden-inclusive searches of `data/raw/gold_studies.tsv`, `data/raw/gold_path_biosamples.tsv`, and `data/raw/gold_path_triads.tsv` for this source path and source IDs | Supported; the exact Fish `Intromittent organ` path has no direct study, biosample, or MIxS triad side-table rows. |
| `Clasper` and `Gonopodium` are immediate GOLD children of this source path. | `data/raw/gold_ecosystem_paths.tsv:1959-1960`, `data/habitats/host_associated/clasper.yaml`, and `data/habitats/host_associated/gonopodium.yaml` | Supported; both generated child records use `UBERON:0008811` as a parent. |
| No item-level curator decision, term request, causal-graph overlay, history record, research report, or prior exact review has been maintained for this target. | Exact ignored/hidden-inclusive searches for `UBERON:0008811`, `intromittent_organ`, `gold.ecosystem:7574`, `gold.ecosystem:7575`, and the Fish `Intromittent organ` source path under `curation`, `history`, `research`, `conf`, `data/raw`, `data/habitats/PATHS.tsv`, `data/habitats/host_associated`, `pages/habitats`, and `reports/yaml_record_review` | Supported; the searches found the target YAML, path lock, UBERON rows, raw GOLD row, rendered page, generated child records, and no target-specific maintained curation artifact or exact prior review. |

Unsupported or over-scoped claims: None found.

## Completeness

The generated record is complete for the maintained inputs currently available:

- The ontology identifier, ontology label, UBERON definition, UBERON definition
  source, UBERON exact synonyms, GOLD label, first GOLD ecosystem node ID, full
  Fish source path, `skos:exactMatch` predicate, and two-node collapse note are
  present.
- `parent_habitats` preserves both broader meanings needed here: the UBERON
  `male reproductive organ` parent and the immediate Fish `Reproductive system`
  source-path parent.
- `mapping_status` remains `SEEDED`, which is correct because no item-level
  `curation/decisions.tsv` row has reviewed this Fish source path.
- The record correctly has no serialized `assertion_count`, characteristic
  taxa, environmental parameters, causal graphs, datasets, discussions, or
  record-level literature evidence.
- iModulonDB was not applicable because this source bucket names no gene,
  locus, regulator, transcriptomic dataset, or strain-level expression claim.

Ignored/hidden-inclusive exact searches covered `curation`, `data/raw`,
`data/habitats/PATHS.tsv`, `data/habitats/host_associated`, `history`,
`research`, `conf`, `reports/yaml_record_review`, and `pages/habitats` for
`UBERON:0008811`, `UBERON:0003135`, `intromittent_organ`,
`gold.ecosystem:7574`, `gold.ecosystem:7575`, and the exact Fish
`Intromittent organ` GOLD path. They found the cited raw row, path lock,
generated target, rendered page, immediate GOLD parent and children, UBERON
ontology rows, and no target-specific maintained curation, causal-graph,
history, research, or exact review artifact.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If future curation promotes this seeded record to reviewed status, preserve the
UBERON identity, the `UBERON:0003135` parent, and the Fish
`Reproductive system` source-path parent unless the committed GOLD hierarchy or
vendored UBERON slice changes.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future item-level review row, run:

- `just seed`
- `just seed-canary UBERON:0008811`
- `just validate data/habitats/host_associated/intromittent_organ.yaml`
- `just validate-strict data/habitats/host_associated/intromittent_organ.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`

## Additional Notes

- `find /tmp -maxdepth 1 -name 'habitatmech-fish-intromittent-organ-*.tsv' -print`
  found no worklist or report TSV after the two helper recipes were killed, and
  `find` included ignored files under the searched directory.
- Same-branch child records still need separate review: `Clasper` and
  `Gonopodium` have distinct identities from this `Intromittent organ` parent.
