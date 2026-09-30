# YAML Record Review: Multiple organs

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/multiple_organs.yaml`
- Started UTC: 2026-09-30T14:53:30Z
- Finished UTC: 2026-09-30T14:58:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Record | `data/habitats/host_associated/multiple_organs.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.11ea780433` |
| Label | `Multiple organs` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Maintained/generated | generated from committed source inventories and `curation/decisions.tsv` by `scripts/seed_from_sources.py` |
| Path lock | `data/habitats/PATHS.tsv:1408` pins `habitatmech:GOLD.11ea780433` to `multiple_organs` |

This is the generated GOLD record for the Fish `Multiple organs` source path.
The source row is an internal GOLD bucket under `Host-associated > Fish >
Multiple systems` and above `Whole body`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/host_associated/multiple_organs.yaml` | Passed; `linkml-validate` reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/multiple_organs.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records expected, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report --out /tmp/habitatmech_multiple_organs_fish_report.tsv` | Passed; the TSV reports this target as `HOST_ASSOCIATED`, `UNGROUNDED`, `SEEDED`, GOLD-attested, definition-free, with 1 parent, 0 parameters, 0 taxa, and 0 causal graphs. |
| `just worklist --status all --out /tmp/habitat_worklist_multiple_organs_fish.tsv` | Passed; wrote 953 ungrounded rows. This target is still listed at row 688 because its only maintained decision is a `CLASS`-depth sweep, not an item-level judgement. |

## Identity and Grounding

The source identity is internally consistent. `data/raw/gold_ecosystem_paths.tsv`
contains the canonical GOLD row `Host-associated > Fish > Multiple systems >
Multiple organs` with leaf label `Multiple organs`, depth 4, two GOLD node IDs,
and zero organism assertions. The generated source attestation uses the first
node ID, `gold.ecosystem:6958`, and records that two GOLD ecosystem node IDs
share this path.

The `UNGROUNDED` status is supported by the maintained class-level decision at
`curation/decisions.tsv:193`, which records that no vendored term matched this
label by the sweep's lexical search routes. That row deliberately uses
`review_depth: CLASS`, so the record remains `SEEDED` and still appears in
`just worklist` for future item-level curation; it should not be treated as an
ENVO term-request candidate until that review happens.

The worklist's lexical candidate, `UBERON:0001630` `muscle organ`, is
over-specific for a generic GOLD `Multiple organs` bucket. The Mammals record
for `Host-associated > Mammals > Multiple systems > Multiple organs` has the
same source label and was previously kept ungrounded for the same reason.

The single parent is supported:

| Parent | Support | Review |
|---|---|---|
| `habitatmech:GOLD.864a5fdcb7` | `data/raw/gold_ecosystem_paths.tsv:1942` contains the immediate GOLD parent path `Host-associated > Fish > Multiple systems`, whose generated record is `data/habitats/host_associated/multiple_systems__74c7f0de.yaml`. | Supported as the source-path parent. |

The GOLD hierarchy below this row is also preserved:
`data/raw/gold_ecosystem_paths.tsv:1944` contains the immediate child
`Host-associated > Fish > Multiple systems > Multiple organs > Whole body`, and
the generated `data/habitats/host_associated/whole_body__4c96bb01.yaml` uses
`habitatmech:GOLD.11ea780433` as one of its source-path parents.

## Evidence

The record has no curator-authored causal graphs, characteristic taxa,
environmental parameters, authored definition, assertion-bearing GOLD organism
path, or record-level literature evidence, so there are no claim-level
citations to audit.

| Claim | Nearest maintained support | Review |
|---|---|---|
| GOLD has a Fish `Multiple organs` source path with two upstream node IDs. | `data/raw/gold_ecosystem_paths.tsv:1943` | Supported exactly by source IDs `gold.ecosystem:6958` and `gold.ecosystem:6959`. |
| The generated source attestation uses the first node ID for a path shared by two GOLD IDs. | Target YAML `source_attestations` and `data/raw/gold_ecosystem_paths.tsv:1943` | Supported exactly. |
| The path has no GOLD organism assertions to serialize as `characteristic_taxa`. | Target YAML, `/tmp/habitatmech_multiple_organs_fish_report.tsv`, and `/tmp/habitat_worklist_multiple_organs_fish.tsv` | Supported; the target has no `characteristic_taxa`, the aggregate report shows 0 taxa, and the worklist ranks the row with 0 assertions. |
| The source path still has auxiliary GOLD evidence in side tables. | `data/raw/gold_path_biosamples.tsv:918`; `data/raw/gold_studies.tsv:3045` | Supported; node `6959` has 2 BioSamples and study `Gs0150218` includes this path among 12 GOLD paths. These side tables do not require an `assertion_count` because GOLD assertion counts are organism counts in generated HabitatRecords. |
| The record reflects a class-level ungrounded sweep, not an item-level review. | `curation/decisions.tsv:193`; generated `curation_history` in the target YAML | Supported exactly. |

The rendered page
`pages/habitats/multiple-organs-habitatmech-gold-11ea780433.html` reflects the
same identifier, `HOST_ASSOCIATED` category, `UNGROUNDED` grounding, `SEEDED`
mapping status, single GOLD source attestation, Fish `Multiple systems` parent,
and class-level curation note as the generated YAML.

Unsupported or over-scoped claims: None found.

## Completeness

The generated record is complete for the maintained inputs currently available:

- The minted identifier, GOLD label, representative source ID, multi-node note,
  and source path are present.
- The source-path parent to Fish `Multiple systems` is present.
- The class-level sweep is reflected as `UNGROUNDED` without promoting
  `mapping_status` to `REVIEWED`.
- The record correctly has no serialized `assertion_count`, definition,
  characteristic taxa, environmental parameters, causal graphs, datasets,
  discussion links, or record-level literature evidence.
- iModulonDB was not applicable because this source bucket names no gene, locus,
  regulator, transcriptomic dataset, or strain-level expression claim.

Exact ignored/hidden-inclusive searches for the Fish source path, both GOLD node
IDs, and `habitatmech:GOLD.11ea780433` covered `data/raw`, `data/habitats`,
`data/habitats/PATHS.tsv`, `pages/habitats`, `curation`, `history`, `research`,
and `reports/yaml_record_review`. They found the cited raw row, side-table
BioSample and study evidence, class-level decision, path lock, generated record,
rendered page, generated Whole body child, and a prior Mammals review that
mentions this Fish child; they found no maintained term request, causal-graph
overlay, history record, target-specific research report, or prior exact Fish
`multiple_organs` review report.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If a future curator wants to promote this seeded record to reviewed status,
replace the existing `CLASS`-depth decision for `habitatmech:GOLD.11ea780433`
with an item-level `CONFIRM_UNGROUNDED` or `NOT_APPLICABLE` decision, rerun
`just seed`, and canary `habitatmech:GOLD.11ea780433`. Keep the Fish
source-path parent unchanged unless the committed GOLD inventory changes.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future item-level review row, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.11ea780433`
- `just validate data/habitats/host_associated/multiple_organs.yaml`
- `just validate-strict data/habitats/host_associated/multiple_organs.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -name '*multiple_organs.md' -print` found no pre-existing exact Fish target report, and `find` included ignored files under the searched directory.
- `just report --out /tmp/habitatmech_multiple_organs_fish_report.tsv` reported this record at TSV row 1408 as `habitatmech:GOLD.11ea780433	Multiple organs	HOST_ASSOCIATED	UNGROUNDED	SEEDED	GOLD	1	0	False	1	0	0	0	data/habitats/host_associated/multiple_organs.yaml`.
- `just worklist --status all --out /tmp/habitat_worklist_multiple_organs_fish.tsv` reported this record at TSV row 688 as `habitatmech:GOLD.11ea780433	Multiple organs	HOST_ASSOCIATED	0	GOLD	Host-associated > Fish > Multiple systems > Multiple organs	TRUE	UBERON:0001630=muscle organ`.
