# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/terrestrial/uranium_contaminated.yaml
- Started UTC: 2026-09-26T20:29:00Z
- Finished UTC: 2026-09-26T20:37:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/terrestrial/uranium_contaminated.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.d722422e31` |
| Label | `Uranium contaminated` |
| Category | `TERRESTRIAL` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated or maintained | Generated from `data/raw/` plus `curation/decisions.tsv`; do not hand-edit |

The filename is pinned by `data/habitats/PATHS.tsv`, whose exact target row is:

```text
habitatmech:GOLD.d722422e31	uranium_contaminated
```

The single source concept is maintained in `curation/decisions.tsv` as a
class-level sweep row:

| Field | Value |
|---|---|
| source ID | `habitatmech:GOLD.d722422e31` |
| decision | `CONFIRM_UNGROUNDED` |
| curator/date | `claude-opus-5` / `2026-08-12` |
| review depth | `CLASS` |
| target ID, target label, predicate, relation | empty |
| note | Class-level sweep; no term in the vendored slice matched this label by any search route, but whether the concept is a habitat at all was not assessed. |

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/terrestrial/uranium_contaminated.yaml` | PASS; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/terrestrial/uranium_contaminated.yaml` | PASS; one file scanned, zero files with errors, zero total error rows. |
| `just validate-causal-all` | PASS; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | PASS; the term-request table is current at 109 terms. |
| `just validate-history` | PASS; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | PASS; 3,206 expected records, zero missing, zero extra, zero differing. |
| `git diff --check` | PASS; no whitespace errors before this report edit. |

No validator was skipped.

## Identity and Grounding

The generated record matches the GOLD source mechanically:

- `data/raw/gold_ecosystem_paths.tsv` row 724 has the exact canonical path
  `Environmental > Terrestrial > Soil > Contaminated > Uranium contaminated`,
  leaf label `Uranium contaminated`, depth 5, one GOLD node,
  `gold.ecosystem:6003`, three GOLD organism assertions, and three total
  counted source assertions.
- The generated `source_attestations[0]` keeps that full GOLD path, records
  `source_id: gold.ecosystem:6003`, and reports `assertion_count: 3` with
  `assertion_unit: ORGANISM`.
- The locked slug maps the generated HabitatMech identifier to
  `uranium_contaminated`, which matches the checked-in path.

The `Uranium contaminated` source concept is a real habitat in GOLD context:
the full path places it under `Environmental > Terrestrial > Soil >
Contaminated`, and GOLD's submitted MIxS triads reinforce that interpretation.
For this exact path, `data/raw/gold_path_triads.tsv` has two independent
studies whose top `env_medium` annotation is `ENVO:00002116` `contaminated
soil` with share `1.00`. The source is narrower than contaminated soil by
contaminant identity.

The generated `parent_habitats` value is therefore directionally correct:
`ENVO:00002116` is the vendored `contaminated soil` term, defined as "A portion
of contaminated soil is a portion of soil with elevated levels of some
contaminant." The GOLD sibling `Pesticide` is not a precedent for marking the
target `NOT_APPLICABLE`: a bare pesticide is a chemical, but `Uranium
contaminated` composes with the surrounding soil-contamination path to denote a
contaminated-soil subclass.

The lexical candidate in the worklist is a false hit. `ENVO:02000093`
`uranium mine` is asserted under `ENVO:00000076` `mine`, whose vendored
definition is "An excavation in the Earth for the purpose of extracting earth
materials." A uranium-contaminated soil sample can come from a uranium mine,
mill-tailing site or other uranium-impacted terrestrial setting; an extraction
feature is not the identity of the contaminated soil material.

## Evidence

| Claim | Evidence | Status |
| --- | --- | --- |
| The record denotes the GOLD path `Environmental > Terrestrial > Soil > Contaminated > Uranium contaminated`. | `data/raw/gold_ecosystem_paths.tsv:724` lists that canonical path, leaf label, one node and node id `gold.ecosystem:6003`; the generated YAML repeats the node and exact source path. | Supported exactly. |
| The source attestation has three GOLD organism assertions. | `data/raw/gold_ecosystem_paths.tsv:724` reports `organism_count` 3 and `total_assertions` 3; the generated YAML records `assertion_count: 3` with `assertion_unit: ORGANISM`. | Supported exactly. |
| `ENVO:00002116` `contaminated soil` is a valid broader parent. | The full GOLD path narrows the reviewed `Environmental > Terrestrial > Soil > Contaminated` parent and two independent GOLD triad studies assign `ENVO:00002116` in `env_medium` for samples on this exact path. | Supported as a broader term. |
| `ENVO:02000093` `uranium mine` is not a valid identity. | The vendored ontology files `uranium mine` under `ENVO:00000076` `mine`; mines are extraction features, while the GOLD path denotes uranium-contaminated soil. | Supported as a rejection. |

## Completeness

The generated YAML is complete for its current input state: it has the exact
GOLD source path, the inherited contaminated-soil parent, and generated
curation-history events for the class-level `CONFIRM_UNGROUNDED` row and the
source seed. Its empty definition, synonyms, xrefs, environmental parameters,
characteristic taxa, causal graphs, discussions, and datasets are expected for
a class-swept generated record that lacks an item-level term request or causal
overlay.

Ignored/hidden-inclusive exact searches for
`habitatmech:GOLD.d722422e31`, `GOLD.d722422e31`, `Uranium contaminated`,
`uranium_contaminated`, `ENVO:02000093`, `uranium mine`, and
`gold.ecosystem:6003` covered `data/raw/`, `data/habitats/`, `curation/`,
`history/`, `research/`, `reports/habitat_research_manifest.tsv`, and
`reports/yaml_record_review/`. They found the generated target, its locked
slug, its raw GOLD row, its biosample side-table row, its study and triad
side-table rows, the rejected lexical candidate in the vendored ontology, and
no prior target-specific YAML review, no target-specific term request or term
request exclusion, no history record, and no causal overlay.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | `Uranium contaminated` remains at class-level `CONFIRM_UNGROUNDED` even though item-level review can confirm a real uranium-contaminated-soil habitat narrower than `ENVO:00002116`, reject `ENVO:02000093` `uranium mine`, and request a specific ENVO term. | `curation/decisions.tsv:1188` has `review_depth` `CLASS`; the full GOLD path and two independent MIxS `env_medium` studies support a contaminated-soil interpretation; `ENVO:02000093` is a mine, not a contaminated-soil material. | `curation/decisions.tsv`; `curation/term_requests.tsv`; `history/` |

No blockers or minor findings.

## Recommended Edits

1. Item-review `habitatmech:GOLD.d722422e31` in
   `curation/decisions.tsv`. Replace the class-level row with an item-level
   `CONFIRM_UNGROUNDED` decision that explicitly rejects `ENVO:02000093`
   `uranium mine` as an extraction feature and confirms the source as a
   uranium-contaminated-soil habitat narrower than `ENVO:00002116`
   `contaminated soil`.
2. Add a `curation/term_requests.tsv` row for this identifier, with
   `ENVO:00002116` `contaminated soil` as the parent, `Uranium contaminated`
   as an exact synonym, and a definition equivalent to "A contaminated soil
   which has elevated levels of uranium." The exact requested label should be
   normalized to the ENVO style chosen by the curator, such as
   `uranium contaminated soil` or `uranium-contaminated soil`.
3. Add an append-only history record for the curation session under `history/`.
4. Regenerate this record from maintained inputs:

```bash
just seed
just seed-canary habitatmech:GOLD.d722422e31
just seed-apply --force
```

## Follow-up Checks

After the future curation edit:

1. Re-read `data/habitats/terrestrial/uranium_contaminated.yaml` and confirm
   it has `grounding_status: UNGROUNDED`, `mapping_status: REVIEWED`, the
   curated definition and synonym from the term-request row, and a generated
   item-level `CONFIRM_UNGROUNDED` curation event for
   `habitatmech:GOLD.d722422e31`.
2. Confirm `parent_habitats` still contains `ENVO:00002116` and no
   `ENVO:02000093`.
3. Confirm `source_attestations[0]` still points at
   `Environmental > Terrestrial > Soil > Contaminated > Uranium contaminated`
   with three GOLD organism assertions.
4. Run the narrow validators:

```bash
just validate data/habitats/terrestrial/uranium_contaminated.yaml
just validate-strict data/habitats/terrestrial/uranium_contaminated.yaml
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

- The reviewed `ENVO:00002116` contaminated-soil report already records
  `Uranium contaminated` as a narrower child that should keep contaminated
  soil as a broader parent; this review confirms that targeted note for the
  child record itself.
- This was a read-only review. It did not edit generated YAML, generated
  pages, source inventories, decision rows, term requests, causal overlays, or
  history records.
