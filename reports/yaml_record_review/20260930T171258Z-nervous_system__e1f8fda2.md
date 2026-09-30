# YAML Record Review: Nervous system

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/nervous_system__e1f8fda2.yaml`
- Started UTC: `2026-09-30T17:06:00Z`
- Finished UTC: `2026-09-30T17:12:58Z`
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.feecbcaf98` |
| Label | `Nervous system` |
| Stable slug | `nervous_system__e1f8fda2` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Maintained/generated | generated from committed source inventories by `scripts/seed_from_sources.py` |
| Path lock | `data/habitats/PATHS.tsv:3188` pins `habitatmech:GOLD.feecbcaf98` to `nervous_system__e1f8fda2` |
| Source attestation | `GOLD`, `gold.ecosystem:5286`, `Host-associated > Fish > Nervous system`, `skos:narrowMatch` |

This is the generated GOLD record for the Fish source path
`Host-associated > Fish > Nervous system`. The source row has three collapsed
GOLD ecosystem node IDs and no direct organism, study, biosample, or GOLD triad
assertions.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/nervous_system__e1f8fda2.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/nervous_system__e1f8fda2.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records expected, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just worklist --status all --out /tmp/habitat_worklist_fish_nervous_system.tsv` | Passed; wrote 953 ungrounded rows. This `NARROW` target is outside the exported worklist rows. |
| `uv run python scripts/habitat_report.py --out /tmp/habitatmech_fish_nervous_system_report.tsv` | Passed; wrote the per-record TSV. The TSV reports this target as `HOST_ASSOCIATED`, `NARROW`, `SEEDED`, GOLD-attested, definition-free, with 2 parents, 0 parameters, 0 taxa, and 0 causal graphs. |

## Identity and Grounding

The generated identity is sound. `data/raw/gold_ecosystem_paths.tsv:1949`
contains the exact source row
`Host-associated > Fish > Nervous system` with leaf label `Nervous system`,
depth 3, three collapsed GOLD ecosystem node IDs, zero aggregate assertions, and
source IDs `gold.ecosystem:5286|gold.ecosystem:7582|gold.ecosystem:7583`. The
generated source attestation uses the first of those node IDs and preserves the
complete source path with a note naming the three-ID collapse.

The `NARROW` grounding to `UBERON:0001016` is appropriate. The vendored ontology
slice labels `UBERON:0001016` as `nervous system` and defines a generic organ
system; the GOLD source path adds Fish host-clade context, so the target should
remain a minted microbial habitat narrower than the generic UBERON anatomy
class instead of adopting `UBERON:0001016` as exact identity.

The two generated parents are traceable to maintained inputs:

| Parent | Support | Review |
|---|---|---|
| `UBERON:0001016` | `data/raw/ontology_terms.tsv:12995` labels the term `nervous system`, and several GOLD host-associated records reuse the same `Nervous system` leaf under different host clades. | Supported as the generic anatomical parent, not the exact Fish-specific identity. |
| `habitatmech:GOLD.3d529a667e` | `data/raw/gold_ecosystem_paths.tsv:33` contains the immediate GOLD parent path `Host-associated > Fish`; `curation/decisions.tsv:429` and `curation/term_requests.tsv:8` curate that record as `fish-associated environment`. | Supported as the source-path parent for Fish-associated environments. |

This Fish record is distinct from the other minted host-associated `Nervous
system` source paths under `Mammals: Human`, `Mammals`, `Arthropoda: Insects`,
`Birds`, and `Reptilia`. All of those records keep separate
`habitatmech:GOLD.*` identifiers and preserve `UBERON:0001016` as a broader
parent rather than merging onto one generic anatomy record.

## Evidence

The record has no curator-authored causal graphs, characteristic taxa,
environmental parameters, authored definition, datasets, discussion links, or
record-level literature evidence, so there are no claim-level citations to
audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| The minted identifier is pinned to the reviewed slug. | `data/habitats/PATHS.tsv:3188` | Supported exactly. |
| GOLD has the Fish `Nervous system` path with three collapsed upstream node IDs. | `data/raw/gold_ecosystem_paths.tsv:1949` | Supported exactly. |
| The path has no direct GOLD assertions to serialize as `assertion_count`, `environmental_parameters`, or `characteristic_taxa`. | `data/raw/gold_ecosystem_paths.tsv:1949`, exact source-ID searches for `gold.ecosystem:5286`, `gold.ecosystem:7582`, and `gold.ecosystem:7583`, and `/tmp/habitatmech_fish_nervous_system_report.tsv` | Supported; exact ignored/hidden-inclusive source-ID searches found no matching GOLD biosample, study, or triad rows outside the collapsed raw path row and generated YAML. |
| `Brain` and `Cerebrospinal fluid` are immediate child concepts under this source path. | `data/raw/gold_ecosystem_paths.tsv:331`, `data/raw/gold_ecosystem_paths.tsv:1950`, `data/habitats/host_associated/brain__b2bb2ba8.yaml`, and `data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml` | Supported exactly. |
| No item-level curator decision, term request, causal-graph overlay, history record, research report, or prior exact review has been maintained for this target. | Exact ignored/hidden-inclusive searches for `habitatmech:GOLD.feecbcaf98`, `nervous_system__e1f8fda2`, `gold.ecosystem:5286`, `gold.ecosystem:7582`, `gold.ecosystem:7583`, and the Fish `Nervous system` path under `curation`, `history`, `research`, and `reports/yaml_record_review` | Supported; those searches found no target-specific maintained curation artifact. The prior Fish Brain review references this record only as that record's immediate GOLD parent. |

The rendered page
`pages/habitats/nervous-system-habitatmech-gold-feecbcaf98.html` reflects the
same identifier, `HOST_ASSOCIATED` category, `NARROW` grounding, `SEEDED`
mapping status, two broader habitats, and single GOLD source attestation as the
generated YAML.

Unsupported or over-scoped claims: None found.

## Completeness

The generated record is complete for the maintained inputs currently available:

- The minted identifier, GOLD label, first GOLD ecosystem node ID, full source
  path, `skos:narrowMatch` predicate, and three-node collapse note are present.
- `parent_habitats` preserves both broader meanings needed here: the generic
  UBERON `nervous system` anatomy term and the immediate Fish source-path
  parent.
- `mapping_status` remains `SEEDED`, which is correct because no item-level
  `curation/decisions.tsv` row has reviewed this Fish source path.
- The record correctly has no serialized `assertion_count`, definition,
  characteristic taxa, environmental parameters, causal graphs, datasets,
  discussion links, or record-level literature evidence.
- iModulonDB was not applicable because this source bucket names no gene,
  locus, regulator, transcriptomic dataset, or strain-level expression claim.

Exact ignored/hidden-inclusive searches for the Fish/Nervous System source
path, the target identifier, the target slug, the target's three GOLD ecosystem
node IDs, `UBERON:0001016`, and the Fish-associated parent covered `data/raw`,
`data/habitats`, `data/habitats/PATHS.tsv`, `pages/habitats`, `curation`,
`history`, `research`, and `reports/yaml_record_review`. They found the cited
raw row, path lock, generated record, rendered page, generated children,
same-label host-associated sibling records, and one parent-only mention from the
Fish Brain review; they found no target-specific maintained curation,
causal-graph, history, research, or exact review artifact.

An exact ignored/hidden-inclusive search of `data/raw/gold_path_biosamples.tsv`,
`data/raw/gold_path_triads.tsv`, and `data/raw/gold_studies.tsv` for
`^Host-associated > Fish > Nervous system\t` found no direct side-table rows for
this parent path, matching the empty optional slots in the generated YAML.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If future curation promotes this seeded record to reviewed status, preserve both
the generic `UBERON:0001016` parent and the Fish source-path parent unless the
committed GOLD hierarchy or vendored ontology slice changes. Add an `ITEM`
decision only after checking the Fish source path and repeated `Nervous system`
leaves specifically.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future item-level review row, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.feecbcaf98`
- `just validate data/habitats/host_associated/nervous_system__e1f8fda2.yaml`
- `just validate-strict data/habitats/host_associated/nervous_system__e1f8fda2.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -name '*nervous_system__e1f8fda2.md' -print` found no pre-existing exact target report, and `find` included ignored files under the searched directory.
- The worklist TSV did not contain `habitatmech:GOLD.feecbcaf98`; this target is `NARROW`, while the exported `/tmp/habitat_worklist_fish_nervous_system.tsv` contained 953 ungrounded backlog rows.
- The report TSV row at `/tmp/habitatmech_fish_nervous_system_report.tsv:3188` is `habitatmech:GOLD.feecbcaf98	Nervous system	HOST_ASSOCIATED	NARROW	SEEDED	GOLD	1	0	False	2	0	0	0	data/habitats/host_associated/nervous_system__e1f8fda2.yaml`.
