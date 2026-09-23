# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/activated_sludge__a422e33f.yaml`
- Started UTC: 2026-09-23T08:43:00Z
- Finished UTC: 2026-09-23T08:47:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.dab267c443` |
| Label | `Activated sludge` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source concept | `Engineered > Wastewater > Nutrient removal > Dissolved organics (aerobic) > Activated sludge` |
| Maintained owner | Generated from the GOLD path inventory and `data/habitats/PATHS.tsv`; generated YAML remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:2911` maps `habitatmech:GOLD.dab267c443` to `activated_sludge__a422e33f` |

This is the generated GOLD record for one path-qualified `Activated sludge`
leaf below `Engineered > Wastewater > Nutrient removal > Dissolved organics
(aerobic)`. Its source key is deterministic:
`sha1("GOLD:Engineered > Wastewater > Nutrient removal > Dissolved organics
(aerobic) > Activated sludge")[:10]` is `dab267c443`, matching the generated
`habitatmech:GOLD.dab267c443` identifier.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__a422e33f.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/engineered/activated_sludge__a422e33f.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| Reference validator | Not checked: this record has no DOI/PMID/URL `EvidenceItem` or target causal-edge evidence, and ignored/hidden-inclusive exact target searches found no target-specific `research/habitats/` report requiring `scripts/check_report_citations.py` |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Pass; 0 ungrounded records are still undecided and 1810 decisions are on file |
| `just report` | Pass; the report completed and kept the corpus at 3206 records |
| `git diff --check` | Pass; no whitespace errors |

## Identity and Grounding

The record's generated identity and direct source trace are internally
consistent:

- `data/raw/gold_ecosystem_paths.tsv:1412` directly attests the canonical path
  `Engineered > Wastewater > Nutrient removal > Dissolved organics (aerobic) >
  Activated sludge`, with leaf label `Activated sludge`, `depth: 5`, one GOLD
  ecosystem node, zero organism-level assertions, zero aggregate source-table
  assertions, and node id `gold.ecosystem:4257`.
- `data/habitats/PATHS.tsv:2911` pins `habitatmech:GOLD.dab267c443` to
  `activated_sludge__a422e33f`.
- The generated `source_id: gold.ecosystem:4257`, `source_label`, and
  `source_path` match the raw GOLD row exactly.
- `data/raw/ontology_terms.tsv:7191` gives `ENVO:00002046` the canonical label
  `activated sludge`, `data/raw/ontology_terms.tsv:7189` gives
  `ENVO:00002044` the canonical label `sludge`, and
  `data/raw/ontology_subclass_edges.tsv:5293` places activated sludge under
  sludge, supporting the generic ontology parent retained by the
  ambiguous-leaf rule.

`grounding_status: NARROW` is appropriate for a path-qualified GOLD leaf. GOLD
has many `Activated sludge` leaves under engineered subpaths, while
`ENVO:00002046` names generic activated sludge; keeping this source concept
minted and using `ENVO:00002046` as a broader parent avoids merging all GOLD
activated-sludge contexts into one ontology identity.

`mapping_status: SEEDED` is expected for the target itself. Ignored/hidden-
inclusive exact searches for `habitatmech:GOLD.dab267c443`,
`activated_sludge__a422e33f`, `gold.ecosystem:4257`, and the full GOLD source
path under `curation/`, `history/`, `research/`, `reports/`, `data/raw`,
`data/habitats/PATHS.tsv`, and generated habitat records found the raw GOLD
rows, the generated target, the slug lock, and no item-level decision, term
request, causal overlay, or history entry for `habitatmech:GOLD.dab267c443`.

The record inherits one unsupported source-path parent edge. The raw GOLD
parent row at `data/raw/gold_ecosystem_paths.tsv:1411` is the intermediate path
`Engineered > Wastewater > Nutrient removal > Dissolved organics (aerobic)`,
which carries leaf label `Dissolved organics (aerobic)` and no aggregate
source-table assertions. The generated parent record
`data/habitats/engineered/dissolved_organics_aerobic.yaml` has only a
class-level `CONFIRM_UNGROUNDED` decision at `curation/decisions.tsv:225`; that
decision explicitly says the sweep did not assess whether the concept is a
habitat. Nothing target-specific has established `Dissolved organics (aerobic)`
as a strict broader habitat for activated-sludge material.

## Evidence

| Claim | Nearest source | Review |
|---|---|---|
| GOLD contains the child path `Engineered > Wastewater > Nutrient removal > Dissolved organics (aerobic) > Activated sludge`. | `data/raw/gold_ecosystem_paths.tsv:1412` | Supported exactly |
| The generated source node is `gold.ecosystem:4257`. | `data/raw/gold_ecosystem_paths.tsv:1412` | Supported exactly |
| The source concept has zero aggregate source-table assertions. | `data/raw/gold_ecosystem_paths.tsv:1412` | Supported exactly; the generated source attestation correspondingly omits count and unit fields |
| The source concept is narrower than generic ENVO activated sludge. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_terms.tsv:7189`; `data/raw/ontology_subclass_edges.tsv:5293`; sibling GOLD `Activated sludge` paths in `data/raw/gold_ecosystem_paths.tsv` | Supported exactly |
| The source concept is narrower than `habitatmech:GOLD.17461837d0` `Dissolved organics (aerobic)`. | GOLD source hierarchy plus `curation/decisions.tsv:225` | Not supported after review; the GOLD path puts the leaf below this intermediate path segment, but the maintained curation for the parent has not established `Dissolved organics (aerobic)` as a habitat or as a strict broader material parent |

The record has no definition, synonyms, xrefs, environmental parameters,
characteristic taxa, record-level evidence, causal graphs, discussion links,
datasets, or quality flags. No target-specific maintained input currently
supplies those fields.

Unsupported or over-scoped claims:

- `parent_habitats` includes `habitatmech:GOLD.17461837d0`, even though the only
  curated decision for that parent leaves its item-level habitat identity
  unreviewed.

## Completeness

The direct GOLD source attestation is complete for
`data/raw/gold_ecosystem_paths.tsv:1412`: the generated record carries the only
GOLD ecosystem node, the source label, the full GOLD source path, and the
`skos:narrowMatch` predicate. The source row has zero organism and total
assertions, so the generated attestation correctly has no assertion count,
assertion unit, or merged-node note. The supplemental
`data/raw/gold_path_biosamples.tsv:555` row and
`data/raw/gold_studies.tsv:54`, `:249`, `:272`, `:326`, `:375`, `:433`, `:615`,
and `:642` show GOLD API biosamples and GOLD studies for this path, but those
supplements are not the organism-assertion column used for GOLD
source-attestation counts.

The target is not complete enough for review signoff because its maintained
inputs do not yet resolve the inherited process-condition parent. The target
needs an item-level decision so the seeder can either merge it into generic
activated sludge or keep it minted while replacing the source-path parent with
the supported `ENVO:00002046` parent.

No causal graph is expected until the target identity and hierarchy are fixed.
Upstream GOLD occurrence is not mechanism evidence.

Ignored/hidden-inclusive exact searches covered the target minted id, the
record stem, the full GOLD source path, `gold.ecosystem:4257`, the generated
parent id `habitatmech:GOLD.17461837d0`, the parent GOLD source path,
`ENVO:00002046`, and `ENVO:00002044`, excluding generated `build`,
`data/text_map`, and `pages` trees for broad content searches. They found the
cited raw, path-lock, maintained parent curation, generated-record, side-table,
prior review, and parent-focused research rows, and no maintained
target-specific curation row.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-A422E33F-001 | major | `parent_habitats` still asserts `Activated sludge` is a kind of `Dissolved organics (aerobic)`, but `ENVO:00002046` confirms the child is activated-sludge material and the only maintained decision for `habitatmech:GOLD.17461837d0` explicitly did not assess whether the parent is a habitat. The generated hierarchy currently preserves a source-path process-condition parent as though it were a reviewed broader habitat. | Add an item-level target decision in `curation/decisions.tsv`; if the concept stays minted, add `curation/term_requests.tsv` with `parent_mode=REPLACE` so the child keeps `ENVO:00002046` and drops the unreviewed GOLD parent. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add an item-level row for `habitatmech:GOLD.dab267c443` in
   `curation/decisions.tsv`.

2. Decide the source identity explicitly:
   - If `Engineered > Wastewater > Nutrient removal > Dissolved organics
     (aerobic) > Activated sludge` is just a generic activated-sludge
     placement, ground the source concept to `ENVO:00002046` `activated sludge`
     so its GOLD attestation merges into the exact ontology-backed record.
   - If the dissolved-organics/aerobic path should remain a separate engineered
     treatment-context child, keep it minted with `GROUND_AS_PARENT` to
     `ENVO:00002046` and add a `curation/term_requests.tsv` definition with
     `parent_mode=REPLACE` to remove the inherited
     `habitatmech:GOLD.17461837d0` parent.

3. Rerun `just seed`, then a canary for `habitatmech:GOLD.dab267c443`, and
   inspect the regenerated
   `data/habitats/engineered/activated_sludge__a422e33f.yaml`.

## Follow-up Checks

For the hierarchy fix, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.dab267c443`
- `just validate data/habitats/engineered/activated_sludge__a422e33f.yaml`
- `just validate-strict data/habitats/engineered/activated_sludge__a422e33f.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

Manually confirm the regenerated record no longer lists
`habitatmech:GOLD.17461837d0` under `parent_habitats` unless future item-level
curation substantively establishes `Dissolved organics (aerobic)` as a broader
habitat rather than a GOLD source-path process condition.

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-activated_sludge__a422e33f.md' -print` found no pre-existing exact review report for this record before this file was written, and `find` included ignored files under the searched directory.
- Exact ignored/hidden-inclusive content searches for `habitatmech:GOLD.dab267c443`, `activated_sludge__a422e33f`, `gold.ecosystem:4257`, `Engineered > Wastewater > Nutrient removal > Dissolved organics (aerobic) > Activated sludge`, `habitatmech:GOLD.17461837d0`, `Engineered > Wastewater > Nutrient removal > Dissolved organics (aerobic)`, `ENVO:00002046`, and `ENVO:00002044` found the cited raw, path-lock, maintained parent curation, parent-focused research, prior review, and generated-record rows, and no target-specific curated input rows.
