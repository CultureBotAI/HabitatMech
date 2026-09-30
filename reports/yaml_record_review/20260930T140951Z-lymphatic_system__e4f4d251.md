# YAML Record Review: Lymphatic system

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/lymphatic_system__e4f4d251.yaml`
- Started UTC: 2026-09-30T14:05:10Z
- Finished UTC: 2026-09-30T14:09:51Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Record | `data/habitats/host_associated/lymphatic_system__e4f4d251.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.a8a343cf61` |
| Label | `Lymphatic system` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Maintained/generated | generated from committed source inventories by `scripts/seed_from_sources.py` |
| Path lock | `data/habitats/PATHS.tsv:2533` pins `habitatmech:GOLD.a8a343cf61` to `lymphatic_system__e4f4d251` |

This is the generated GOLD record for the host-scoped Fish `Lymphatic system`
source path. It is intentionally distinct from the Birds, mammal, and human
records with the same display label because the generic UBERON anatomy term
does not encode the host context that GOLD puts in the path.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/lymphatic_system__e4f4d251.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/lymphatic_system__e4f4d251.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records expected, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report --out /tmp/habitatmech_lymphatic_system_fish_report.tsv` | Passed; the TSV reports this target as `HOST_ASSOCIATED`, `NARROW`, `SEEDED`, GOLD-attested, definition-free, with 2 parents, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --status all --out /tmp/habitat_worklist_lymphatic_system_fish.tsv` | Passed; wrote 953 ungrounded rows. `habitatmech:GOLD.a8a343cf61` is not listed because the worklist ranks ungrounded records, not narrow ontology groundings. |

## Identity and Grounding

The source identity is internally consistent. `data/raw/gold_ecosystem_paths.tsv`
contains the canonical GOLD row `Host-associated > Fish > Lymphatic system`
with leaf label `Lymphatic system`, depth 3, three GOLD node IDs, zero direct
assertions, and source IDs `gold.ecosystem:7557`, `gold.ecosystem:7558`, and
`gold.ecosystem:7559`. The generated source attestation uses the first node ID
and records that three GOLD ecosystem node IDs share this path.

The `NARROW` grounding is appropriate for an unreviewed source path whose
closest ontology term is the generic vertebrate `UBERON:0002465` `lymphoid
system`. `data/raw/ontology_terms.tsv` defines `UBERON:0002465` and lists
`lymphatic system` as an exact synonym, but the GOLD source concept adds the
fish host context and is therefore narrower than the host-generic anatomy
class. The prior Birds `Lymphatic system` review at
`reports/yaml_record_review/20260929T212735Z-lymphatic_system__b7b64dca.md`
accepted the same NARROW pattern for the bird-specific sibling.

Both parents are justified:

| Parent | Support | Review |
|---|---|---|
| `UBERON:0002465` | `data/raw/ontology_terms.tsv:13164` defines `UBERON:0002465` `lymphoid system` and lists `lymphatic system` as an exact synonym. | Supported as the nearest broader generic anatomy term. |
| `habitatmech:GOLD.3d529a667e` | `data/raw/gold_ecosystem_paths.tsv:33` contains the immediate GOLD parent path `Host-associated > Fish`, whose generated, reviewed record is `data/habitats/host_associated/fish.yaml`. | Supported as the source-path parent for fish-associated environments. |

## Evidence

The record has no curator-authored causal graphs, characteristic taxa,
environmental parameters, authored definition, assertion-bearing source path, or
record-level evidence, so there are no claim-level citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| GOLD has a Fish `Lymphatic system` path with three upstream node IDs. | `data/raw/gold_ecosystem_paths.tsv:1941` | Supported exactly. |
| The GOLD path has zero organism, study, biosample, and total assertions. | `data/raw/gold_ecosystem_paths.tsv:1941` | Supported exactly; the generated attestation correctly omits `assertion_count` instead of serializing zero. |
| The Fish `Spleen` record is a child of this Fish `Lymphatic system` source path. | `data/raw/gold_ecosystem_paths.tsv:593`; `data/habitats/host_associated/spleen__733ab9e0.yaml` | Supported exactly by the raw child path and generated child record. |
| The Fish `Lymphatic system` path is sibling-shaped with other host-specific Lymphatic system records. | `data/habitats/host_associated/lymphatic_system__b7b64dca.yaml`; `data/habitats/host_associated/lymphatic_system.yaml`; `data/habitats/host_associated/lymphatic_system__5f8baf7d.yaml` | Supported; all keep `UBERON:0002465` as a parent and use a host-specific source-path parent. |

The rendered page
`pages/habitats/lymphatic-system-habitatmech-gold-a8a343cf61.html` reflects the
same identifier, `HOST_ASSOCIATED` category, `NARROW` grounding, `SEEDED`
mapping status, single GOLD source attestation, two broader parents, and no
optional evidence sections as the generated YAML.

Unsupported or over-scoped claims: None found.

## Completeness

The generated record is complete for the maintained inputs currently available:

- The minted identifier, GOLD label, representative source ID, multi-node note,
  and source path are present.
- The broad UBERON lymphoid-system parent is present.
- The source-path parent to `fish-associated environment` is present.
- The Fish Spleen child is generated separately and correctly points back to
  this record as its source-path parent.
- The record correctly has no serialized `assertion_count`, definition,
  characteristic taxa, environmental parameters, causal graphs, datasets,
  discussion links, or record-level literature evidence.
- iModulonDB was not applicable because this anatomical habitat record names no
  gene, locus, regulator, transcriptomic dataset, or strain-level expression
  claim.

Exact ignored/hidden-inclusive searches for the Fish source path, all three
GOLD node IDs, `habitatmech:GOLD.a8a343cf61`, `UBERON:0002465`, and
`lymphatic_system__e4f4d251` covered `data/raw`, `data/habitats/PATHS.tsv`, the
target YAML, `pages/habitats`, `curation`, `history`, `research`, and
`reports/yaml_record_review`. They found the cited raw, path-lock,
generated-record, rendered-page, prior Birds Lymphatic review, Fish Spleen
child, and shared UBERON-parent mentions; they found no maintained decision row,
term request, causal-graph overlay, history record, target-specific research
report, or prior exact `lymphatic_system__e4f4d251` review report. Exact
ignored/hidden-inclusive searches of `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_path_triads.tsv`, and `data/raw/gold_studies.tsv` found no Fish
Lymphatic rows, matching the empty optional slots in the generated YAML.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If a future curator wants to promote this seeded record to reviewed status, add
an item-level `REVIEW` decision in `curation/decisions.tsv` for
`habitatmech:GOLD.a8a343cf61`, rerun `just seed`, canary
`habitatmech:GOLD.a8a343cf61`, and keep the UBERON and Fish source-path parents
unchanged unless the committed GOLD or ontology inventories change.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future status-only review row, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.a8a343cf61`
- `just validate data/habitats/host_associated/lymphatic_system__e4f4d251.yaml`
- `just validate-strict data/habitats/host_associated/lymphatic_system__e4f4d251.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -name '*lymphatic_system__e4f4d251.md' -print` found no pre-existing exact target report, and `find` included ignored files under the searched directory.
- `just report --out /tmp/habitatmech_lymphatic_system_fish_report.tsv` reported this record at TSV row 2533 as `habitatmech:GOLD.a8a343cf61	Lymphatic system	HOST_ASSOCIATED	NARROW	SEEDED	GOLD	1	0	False	2	0	0	0	data/habitats/host_associated/lymphatic_system__e4f4d251.yaml`.
- `just worklist --status all --out /tmp/habitat_worklist_lymphatic_system_fish.tsv` wrote 953 ungrounded rows; exact search found no `habitatmech:GOLD.a8a343cf61` row in that TSV because this target is `NARROW`, not `UNGROUNDED`.
