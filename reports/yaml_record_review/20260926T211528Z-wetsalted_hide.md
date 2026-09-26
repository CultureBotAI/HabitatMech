# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/wetsalted_hide.yaml
- Started UTC: 2026-09-26T21:05:00Z
- Finished UTC: 2026-09-26T21:15:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/engineered/wetsalted_hide.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.ccd148a035` |
| Label | `Wetsalted hide` |
| Category | `ENGINEERED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated or maintained | Generated from `data/raw/` plus `curation/decisions.tsv`; do not hand-edit |

The filename is pinned by `data/habitats/PATHS.tsv`, whose exact target row is:

```text
habitatmech:GOLD.ccd148a035	wetsalted_hide
```

The single source concept is maintained in `curation/decisions.tsv` as a
class-level sweep row:

| Field | Value |
|---|---|
| source ID | `habitatmech:GOLD.ccd148a035` |
| decision | `CONFIRM_UNGROUNDED` |
| curator/date | `claude-opus-5` / `2026-08-12` |
| review depth | `CLASS` |
| target ID, target label, predicate, relation | empty |
| note | Class-level sweep; no term in the vendored slice matched this label by any search route, but whether the concept is a habitat at all was not assessed. |

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/wetsalted_hide.yaml` | PASS; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/wetsalted_hide.yaml` | PASS; one file scanned, zero files with errors, zero total error rows. |
| `just validate-causal-all` | PASS; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | PASS; the term-request table is current at 109 terms. |
| `just validate-history` | PASS; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | PASS; 3,206 expected records, zero missing, zero extra, zero differing. |
| `git diff --check` | PASS; no whitespace errors before this report edit. |

No validator was skipped.

## Identity and Grounding

The generated record matches the GOLD source mechanically:

- `data/raw/gold_ecosystem_paths.tsv` row 701 has the exact canonical path
  `Engineered > Industrial production > Engineered product > Wetsalted hide`,
  leaf label `Wetsalted hide`, depth 4, two GOLD nodes,
  `gold.ecosystem:7646|gold.ecosystem:7647`, three GOLD organism assertions,
  and three total counted source assertions.
- The generated `source_attestations[0]` keeps that full GOLD path, records the
  first collapsed node as `source_id: gold.ecosystem:7646`, and reports
  `assertion_count: 3` with `assertion_unit: ORGANISM`.
- The locked slug maps the generated HabitatMech identifier to
  `wetsalted_hide`, which matches the checked-in path.

The GOLD source concept is a real engineered-product habitat. GOLD places the
leaf under `Engineered > Industrial production > Engineered product`; a
wet-salted hide is an animal hide preserved for leather production, not the
living host integument. The current generated parent,
`habitatmech:GOLD.74bb2a619a` `Engineered product`, is the exact GOLD
source-hierarchy parent and is therefore appropriate as a generated broader
record even though that parent record is itself still at class-level
`CONFIRM_UNGROUNDED`.

The current `UNGROUNDED` identity is also correct because the vendored slice has
no exact `wetsalted hide` or `wet-salted hide` term. It does, however, contain a
valid broader term: `ENVO:02000053` `hide`, defined as "A skin obtained from
animals for human use typically from deer or cattle sources used to produce
leather, shoes, fashion accessories, musical instruments." A wet-salted hide is
narrower than that term by the preservation process applied before tanning, so
`ENVO:02000053` should be a parent rather than the identity.

## Evidence

| Claim | Evidence | Status |
|---|---|---|
| The record denotes the GOLD path `Engineered > Industrial production > Engineered product > Wetsalted hide`. | `data/raw/gold_ecosystem_paths.tsv:701` lists that canonical path, leaf label, two node IDs and three organism assertions; the generated YAML repeats the first node ID, exact source path, assertion count and assertion unit. | Supported exactly. |
| `habitatmech:GOLD.74bb2a619a` is the source-hierarchy parent. | `data/raw/gold_ecosystem_paths.tsv:221` is the depth-3 `Engineered > Industrial production > Engineered product` row, and the target row 701 is its depth-4 child. | Supported for generated GOLD hierarchy. |
| `ENVO:02000053` `hide` is a valid broader parent, not an exact identity. | The vendored ontology defines `hide` as an animal skin obtained for leather or other human uses; the GOLD label composes that class with a wet-salting preservation state. | Supported as a broader term. |

No unsupported record-level evidence items, causal-graph edges,
environmental-parameter rows, characteristic-taxon rows, discussions, or dataset
entries need correction because the generated record does not contain any.

## Completeness

The generated YAML is complete for its current input state: it has the exact
GOLD source path, the inherited GOLD engineered-product parent, and generated
curation-history events for the class-level `CONFIRM_UNGROUNDED` row and the
source seed. Its empty definition, synonyms, xrefs, environmental parameters,
characteristic taxa, causal graphs, discussions, and datasets are expected for
a class-swept generated record that lacks an item-level term request or causal
overlay.

Ignored/hidden-inclusive exact searches for
`habitatmech:GOLD.ccd148a035`, `GOLD.ccd148a035`, `Wetsalted hide`,
`wetsalted_hide`, `wetsalted`, `gold.ecosystem:7646`,
`gold.ecosystem:7647`, and `ENVO:02000053` covered `data/raw/`,
`data/habitats/`, `curation/`, `history/`, `research/`,
`reports/habitat_research_manifest.tsv`, and `reports/yaml_record_review/`.
They found the generated target, its locked slug, its raw GOLD row, its
class-level decision row, the broader `hide` ontology term, contextual
non-target research mentions, and no prior target-specific YAML review, no
target-specific term request or term-request exclusion, no history record, no
causal overlay, and no GOLD biosample, study, or MIxS triad side-table rows for
this exact path or its two GOLD node IDs.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Wetsalted hide` remains at class-level `CONFIRM_UNGROUNDED` even though item-level review can confirm a real engineered-product habitat narrower than `ENVO:02000053` `hide` and request an exact ENVO term. | `curation/decisions.tsv:1131` has `review_depth` `CLASS`; the full GOLD path supports a wet-salted-hide interpretation under engineered products; `ENVO:02000053` is a broader hide term and not the exact wet-salted subtype. | `curation/decisions.tsv`; `curation/term_requests.tsv`; `history/` |

No blockers or minor findings.

## Recommended Edits

1. Item-review `habitatmech:GOLD.ccd148a035` in
   `curation/decisions.tsv`. Replace the class-level row with an item-level
   `GROUND_AS_PARENT` decision that attaches `ENVO:02000053` `hide` as a true
   broader parent and leaves the minted Wetsalted hide identity distinct from
   generic hide.
2. Add a `curation/term_requests.tsv` row for this identifier, with
   `ENVO:02000053` `hide` as the parent and a genus-differentia definition for
   the wet-salted processing state, such as "A hide which has been preserved by
   wet salting before tanning." Normalize the requested label to ENVO style,
   such as `wet-salted hide`, and preserve the GOLD spelling `Wetsalted hide`
   as an exact synonym.
3. Add an append-only history record for the curation session under `history/`.
4. Regenerate this record from maintained inputs:

```bash
just seed
just seed-canary habitatmech:GOLD.ccd148a035
just seed-apply --force
```

## Follow-up Checks

After the future curation edit:

1. Re-read `data/habitats/engineered/wetsalted_hide.yaml` and confirm it has
   `grounding_status: NARROW`, `mapping_status: REVIEWED`, the curated
   wet-salted-hide definition and exact synonym from the term-request row, and a
   generated item-level `GROUND_AS_PARENT` curation event for
   `habitatmech:GOLD.ccd148a035`.
2. Confirm `parent_habitats` contains both the source-derived
   `habitatmech:GOLD.74bb2a619a` parent and `ENVO:02000053`, because both
   `Engineered product` and `hide` are true broader classes.
3. Confirm `source_attestations[0]` still points at
   `Engineered > Industrial production > Engineered product > Wetsalted hide`
   with three GOLD organism assertions.
4. Run the narrow validators:

```bash
just validate data/habitats/engineered/wetsalted_hide.yaml
just validate-strict data/habitats/engineered/wetsalted_hide.yaml
just term-requests-check
just validate-history
just verify-corpus --max-diffs 1
git diff --check
```

5. Run the full corpus gate before PR:

```bash
just qc
```

## Additional Notes

- The committed `Material` research report mentions `Wetsalted hide` only as a
  sibling under GOLD `Engineered product`; it is context for the GOLD subtree
  and does not maintain this target's grounding, definition, or term request.
- This was a read-only review. It did not edit generated YAML, generated pages,
  source inventories, decision rows, term requests, causal overlays, or history
  records.
