# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/activated_sludge__55dc7bfe.yaml`
- Started UTC: 2026-09-23T07:57:30Z
- Finished UTC: 2026-09-23T08:01:06Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.adf7e16a3a` |
| Label | `Activated sludge` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source concept | `Engineered > Bioreactor > Aerobic > Activated sludge` |
| Maintained owner | Generated from the GOLD path inventory and `data/habitats/PATHS.tsv`; generated YAML remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:2565` maps `habitatmech:GOLD.adf7e16a3a` to `activated_sludge__55dc7bfe` |

This is the generated GOLD record for one path-qualified `Activated sludge`
leaf below the reviewed `Engineered > Bioreactor > Aerobic` parent. Its source
key is deterministic: `sha1("GOLD:Engineered > Bioreactor > Aerobic >
Activated sludge")[:10]` is `adf7e16a3a`, matching the generated
`habitatmech:GOLD.adf7e16a3a` identifier.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__55dc7bfe.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/engineered/activated_sludge__55dc7bfe.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Pass; 0 ungrounded records are still undecided and 1810 decisions are on file |
| `just report` | Pass; the report completed and kept the corpus at 3206 records |
| `git diff --check` | Pass; no whitespace errors |

## Identity and Grounding

The record's generated identity and direct source trace are internally
consistent:

- `data/raw/gold_ecosystem_paths.tsv:694` directly attests the canonical path
  `Engineered > Bioreactor > Aerobic > Activated sludge`, with leaf label
  `Activated sludge`, `depth: 4`, two GOLD ecosystem nodes, three
  organism-level assertions, and node ids `gold.ecosystem:5470` and
  `gold.ecosystem:5471`.
- `data/habitats/PATHS.tsv:2565` pins `habitatmech:GOLD.adf7e16a3a` to
  `activated_sludge__55dc7bfe`.
- The generated `source_id: gold.ecosystem:5470`, `source_label`,
  `source_path`, `assertion_count: 3`, and `assertion_unit: ORGANISM` match the
  raw GOLD row exactly.
- `data/raw/ontology_terms.tsv:7191` gives `ENVO:00002046` the canonical label
  `activated sludge`, and `data/raw/ontology_subclass_edges.tsv:5293` places it
  under `ENVO:00002044` `sludge`, supporting the generic ontology parent
  retained by the ambiguous-leaf rule.

`grounding_status: NARROW` is appropriate for a path-qualified GOLD leaf. GOLD
has many `Activated sludge` leaves under engineered subpaths, while
`ENVO:00002046` names generic activated sludge; keeping this source concept
minted and using `ENVO:00002046` as a broader parent avoids merging all GOLD
activated-sludge contexts into one ontology identity.

`mapping_status: SEEDED` is expected for the target itself. Ignored/hidden-
inclusive exact searches for `habitatmech:GOLD.adf7e16a3a`,
`activated_sludge__55dc7bfe`, `gold.ecosystem:5470`, `gold.ecosystem:5471`,
and the full GOLD source path under `curation/`, `history/`, `research/`,
`reports/`, `data/raw`, `data/habitats/PATHS.tsv`, and generated habitat
records found the raw GOLD rows, the generated target, the slug lock, and no
item-level decision, term request, causal overlay, or history entry for
`habitatmech:GOLD.adf7e16a3a`.

The record inherits one false parent edge. The GOLD source path is a child of
`Engineered > Bioreactor > Aerobic`, and that parent was reviewed at
`curation/decisions.tsv:838` as an exact match to `ENVO:00002126`
`aerobic bioreactor`. The target child, however, is labelled `Activated sludge`;
`ENVO:00002126` denotes a bioreactor, while the vendored ENVO slice places
`activated sludge` under `ENVO:00002044` `sludge`.

## Evidence

| Claim | Nearest source | Review |
|---|---|---|
| GOLD contains the child path `Engineered > Bioreactor > Aerobic > Activated sludge`. | `data/raw/gold_ecosystem_paths.tsv:694` | Supported exactly |
| The generated source node `gold.ecosystem:5470` is the first of two GOLD ecosystem nodes collapsed into this canonical path. | `data/raw/gold_ecosystem_paths.tsv:694` | Supported exactly |
| The source concept has three GOLD organism-level assertions in the seeder's source table. | `data/raw/gold_ecosystem_paths.tsv:694` | Supported exactly; `src/habitatmech/seed.py` serializes GOLD `assertion_count` from `organism_count`, so the generated `assertion_count: 3` is faithful |
| The source concept is narrower than generic ENVO activated sludge. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_subclass_edges.tsv:5293`; sibling GOLD `Activated sludge` paths in `data/raw/gold_ecosystem_paths.tsv` | Supported exactly |
| The source concept is narrower than `ENVO:00002126` `aerobic bioreactor`. | GOLD source hierarchy plus `curation/decisions.tsv:838` | Not supported after review; the source hierarchy places the leaf below the exact-grounded parent, but the child denotes an activated-sludge material rather than the aerobic bioreactor that contains it |

The record has no definition, synonyms, xrefs, environmental parameters,
characteristic taxa, record-level evidence, causal graphs, discussion links,
datasets, or quality flags. No target-specific maintained input currently
supplies those fields.

Unsupported or over-scoped claims:

- `parent_habitats` includes `ENVO:00002126`, which denotes the aerobic
  bioreactor rather than its activated-sludge contents.

## Completeness

The direct GOLD source attestation is complete for
`data/raw/gold_ecosystem_paths.tsv:694`: the generated record carries the
representative source node, source label, full GOLD source path,
`skos:narrowMatch` predicate, organism assertion count, organism assertion
unit, and note that two GOLD ecosystem node ids share the canonical path. The
supplemental `data/raw/gold_path_biosamples.tsv:419` row reports 32 GOLD API
biosamples for `gold.ecosystem:5471`, but that supplement is not the
organism-assertion column used for GOLD source-attestation counts.

The target is not complete enough for review signoff because its maintained
inputs do not yet suppress the false device-as-material parent. The target
needs its own item-level decision so the seeder can stop regenerating
`ENVO:00002126` as a parent of an activated-sludge material.

No causal graph is expected until the target identity and hierarchy are fixed.
Upstream GOLD occurrence is not mechanism evidence.

Ignored/hidden-inclusive exact searches covered the target minted id, the
record stem, the full GOLD source path, `gold.ecosystem:5470`,
`gold.ecosystem:5471`, the reviewed parent source id
`habitatmech:GOLD.904dea8017`, parent node ids `gold.ecosystem:4534`,
`gold.ecosystem:4535`, and `gold.ecosystem:4536`, `ENVO:00002046`,
`ENVO:00002044`, `ENVO:00002123`, and `ENVO:00002126`, excluding generated
`build`, `data/text_map`, and `pages` trees for broad content searches. They
found the cited raw, path-lock, maintained parent curation, generated-record,
and prior generic activated-sludge review rows, and no maintained
target-specific curation row.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-55DC7BFE-001 | major | `parent_habitats` still asserts `habitatmech:GOLD.adf7e16a3a` is a kind of `ENVO:00002126` `aerobic bioreactor`, but the child is labelled `Activated sludge` and kept under `ENVO:00002046`. The generated hierarchy now conflates a sludge material with the bioreactor that may contain sludge. | Add an item-level target decision in `curation/decisions.tsv`; if the concept stays minted, add `curation/term_requests.tsv` with `parent_mode=REPLACE` so the child keeps `ENVO:00002046` and drops the false GOLD parent. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add an item-level row for `habitatmech:GOLD.adf7e16a3a` in
   `curation/decisions.tsv`.

2. Decide the source identity explicitly:
   - If `Engineered > Bioreactor > Aerobic > Activated sludge` is just a
     generic activated-sludge placement, ground the source concept to
     `ENVO:00002046` `activated sludge` so its GOLD attestation merges into the
     exact ontology-backed record.
   - If the path should remain a separate aerobic-bioreactor-specific child,
     keep it minted with `GROUND_AS_PARENT` to `ENVO:00002046` and add a
     `curation/term_requests.tsv` definition with `parent_mode=REPLACE` to
     remove the inherited `ENVO:00002126` parent.

3. Rerun `just seed`, then a canary for `habitatmech:GOLD.adf7e16a3a`, and
   inspect the regenerated `data/habitats/engineered/activated_sludge__55dc7bfe.yaml`.

## Follow-up Checks

For the hierarchy fix, run:

- `just seed`
- `just seed-canary habitatmech:GOLD.adf7e16a3a`
- `just validate data/habitats/engineered/activated_sludge__55dc7bfe.yaml`
- `just validate-strict data/habitats/engineered/activated_sludge__55dc7bfe.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

Manually confirm the regenerated record no longer lists `ENVO:00002126` under
`parent_habitats` unless future curation substantively changes the target from
activated-sludge material to an aerobic bioreactor.

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-activated_sludge__55dc7bfe.md' -print` found no pre-existing exact review report for this record before this file was written, and `find` included ignored files under the searched directory.
- Exact ignored/hidden-inclusive content searches for `habitatmech:GOLD.adf7e16a3a`, `activated_sludge__55dc7bfe`, `gold.ecosystem:5470`, `gold.ecosystem:5471`, `Engineered > Bioreactor > Aerobic > Activated sludge`, `habitatmech:GOLD.904dea8017`, `gold.ecosystem:4534`, `gold.ecosystem:4535`, `gold.ecosystem:4536`, `ENVO:00002046`, `ENVO:00002044`, `ENVO:00002123`, and `ENVO:00002126` found the cited raw, path-lock, maintained parent curation, prior review, and generated-record rows, and no target-specific curated input rows.
