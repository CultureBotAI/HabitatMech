# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/host_associated/endosymbionts.yaml
- Started UTC: 2026-09-26T13:52:01Z
- Finished UTC: 2026-09-26T13:52:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.895a2372e5` |
| Label | `Endosymbionts` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Generated path | `data/habitats/host_associated/endosymbionts.yaml` |
| Maintained path lock | `data/habitats/PATHS.tsv:2312` maps `habitatmech:GOLD.895a2372e5` to `endosymbionts` |
| Source concept | GOLD `gold.ecosystem:3371` and three duplicate node IDs |
| Source label | `Endosymbionts` |
| Source path | `Host-associated > Endosymbionts` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |

The reviewed file is generated from the GOLD source inventory and one
class-level curation decision. It should not be patched directly.

## Validation

| Command | Result |
|---|---|
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Passed; wrote 953 rows. The target appeared as row 238 with three GOLD organism assertions and no lexical candidate. |
| `just validate data/habitats/host_associated/endosymbionts.yaml` | Passed with `No issues found`. |
| `just validate-strict data/habitats/host_associated/endosymbionts.yaml` | Passed; one file scanned, zero files with `ERROR`, zero total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Passed. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identifier, GOLD source identity, duplicate-node note, path, and
assertion count agree with the raw GOLD aggregate:

| Claim | Evidence | Assessment |
|---|---|---|
| The target is the top-level `Endosymbionts` child under `Host-associated`. | `data/raw/gold_ecosystem_paths.tsv:739` records `Host-associated > Endosymbionts`, leaf label `Endosymbionts`, depth 2, four GOLD node IDs, three organism assertions, zero study assertions, zero biosample assertions, and total assertion count 3. | Supported exactly. |
| The stable generated filename is pinned for this identifier. | `data/habitats/PATHS.tsv:2312` maps `habitatmech:GOLD.895a2372e5` to `endosymbionts`. | Supported exactly. |
| The `source_attestations` block preserves the first raw GOLD source ID, source label, path, assertion count, assertion unit, and duplicate-node note. | The generated YAML has `source: GOLD`, `source_id: gold.ecosystem:3371`, `source_label: Endosymbionts`, `source_path: Host-associated > Endosymbionts`, `assertion_count: 3`, `assertion_unit: ORGANISM`, and notes that four GOLD ecosystem node IDs share this path. | Supported exactly. |
| The broad parent `ENVO:01001000` is the vendored `environmental system determined by an organism` term. | `data/raw/ontology_terms.tsv:8495` labels `ENVO:01001000` as `environmental system determined by an organism` and records `host-associated environment` as a synonym. | Supported as a broad host-associated parent. It is not an exact grounding or an authored definition for the `Endosymbionts` leaf. |
| The source concept is still owned only by a class-level sweep decision. | `curation/decisions.tsv:809` has `CONFIRM_UNGROUNDED` for `habitatmech:GOLD.895a2372e5` with `review_depth` `CLASS`. Its note says habitat status was not assessed. | Reproducible but incomplete. |

The same source-path branch already has two children with item-level curation:

| Identifier | GOLD path | Assertions | Current review status |
|---|---:|---:|---|
| `habitatmech:GOLD.a89688e0ba` | `Host-associated > Endosymbionts > Bacteria` | 1 organism | Defined as `endosymbiotic bacterium-associated environment`; `mapping_status: REVIEWED`. |
| `habitatmech:GOLD.1ab59245f7` | `Host-associated > Endosymbionts > Fungi` | 0 assertions | `ENVO:01001041` `fungi-associated environment` attached as a broad parent by an item-level `GROUND_AS_PARENT` decision. |

Both generated children still carry `habitatmech:GOLD.895a2372e5` as a parent.
The Bacteria term-request note scopes that child to the Endosymbionts branch and
says `ENVO:01001000` is only the tightest vendored genus until bacterium- and
endosymbiont-associated intermediate terms exist; the Fungi item-level decision
keeps the Fungi leaf minted under this source-derived parent. That makes the
parent's class-depth status the unresolved part of an otherwise item-reviewed
branch, not an isolated low-volume leaf.

## Evidence

| Record claim | Nearest source | Assessment |
|---|---|---|
| `source: GOLD`, `source_id: gold.ecosystem:3371`, `source_label: Endosymbionts`, and `source_path: Host-associated > Endosymbionts` | `data/raw/gold_ecosystem_paths.tsv:739` | Supported exactly. |
| `assertion_count: 3`, `assertion_unit: ORGANISM`, and four duplicate GOLD node IDs | `data/raw/gold_ecosystem_paths.tsv:739` | Supported exactly. The count is a GOLD organism count and should not be summed with child, BacDive strain, or PREGO taxon counts. |
| Parent `ENVO:01001000` | `data/raw/gold_ecosystem_paths.tsv:18` is the top-level `Host-associated` GOLD aggregate; `data/raw/ontology_terms.tsv:8495` records `ENVO:01001000` as the vendored host-associated environment term. | Supported as a broad source-path parent. |
| Child use as a source-derived parent | `data/habitats/host_associated/bacteria__7bc807fd.yaml` and `data/habitats/host_associated/fungi.yaml` both list `habitatmech:GOLD.895a2372e5` in `parent_habitats`. `data/raw/gold_ecosystem_paths.tsv:1032` and `:1915` show both records are exact GOLD children of `Host-associated > Endosymbionts`. | Supported exactly. |
| Absence of a curated definition, environmental parameters, evidence objects, causal graph, item-level history event, target-specific research report, term request, and prior exact YAML review | Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.895a2372e5`, `Host-associated > Endosymbionts`, and `gold.ecosystem:3371`, `gold.ecosystem:4749`, `gold.ecosystem:4750`, `gold.ecosystem:4751` across `data/raw/`, `curation/`, `history/`, `research/habitats/`, `reports/yaml_record_review/`, `data/habitats/`, and `pages/habitats/` found the expected raw rows, path lock, class-level decision, generated record and page, generated child parent edges, and contextual mentions in Bacteria, Fungi, and Microbial research reports. A hidden/ignored-inclusive `find` for `*endosymbionts*` under `reports/yaml_record_review/` and `research/habitats/` found no prior exact YAML review and no deep-research report targeting this parent record. | Supported. The current parent is a generated GOLD node with no committed item-level curation of its own. |

## Completeness

The generated record completely preserves the current GOLD source aggregate and
the class-level `CONFIRM_UNGROUNDED` decision. It correctly leaves
definition-bearing, causal, parameter, characteristic-taxon, and evidence slots
empty because no maintained input owns those target-specific claims yet.

The record is incomplete as a branch-level grounding and definition decision.
The `Host-associated > Endosymbionts > Bacteria` child is already an authored
term request scoped to the Endosymbionts branch, and its committed research
report identifies this parent as a missing intermediate class shared with
`Host-associated > Endosymbionts > Fungi`. The sibling Fungi item review also
keeps its GOLD source concept under this parent. Those curated child rows are
consistent with an item-level reading in which `Endosymbionts` means host cells
that are themselves endosymbiotic inside another organism, as opposed to the
ordinary organism-role reading where the endosymbiont is the occupant rather
than the habitat. The current parent has not recorded that judgment, definition,
or ENVO term request.

The GOLD shape still needs item review rather than blind promotion. The parent
path has four duplicate node IDs and three organism assertions but no study or
biosample assertions, and prior deep-research for the zero-assertion `Fungi`
child noted that `Host-associated > Endosymbionts > Fungi` is ambiguous between
fungi as endosymbiont hosts and a placeholder for fungal isolates. The parent
needs the same full-path decision so the branch does not encode a role/host
axis without an explicit curator statement.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ENDOSYMBIONTS-001 | Major | `Host-associated > Endosymbionts` is still `SEEDED` and `UNGROUNDED` from a `CLASS`-depth `CONFIRM_UNGROUNDED` decision even though its Bacteria and Fungi children are item-reviewed and retain it as their source-derived parent. No item-level decision records whether the parent denotes an endosymbiont-associated host-cell habitat that needs a HabitatMech definition and ENVO term request, a non-habitat organism-role bin, or an ambiguous GOLD scaffold to keep minted with only a broad parent. | `curation/decisions.tsv`; if the parent is a novel habitat after item review, `curation/term_requests.tsv` |

## Recommended Edits

1. Item-review `gold.ecosystem:3371`, `gold.ecosystem:4749`,
   `gold.ecosystem:4750`, and `gold.ecosystem:4751` together as the duplicate
   GOLD nodes for `Host-associated > Endosymbionts`.
2. Resolve the branch reading against the existing
   `Host-associated > Endosymbionts > Bacteria` and `> Fungi` item reviews:
   either define the parent as an endosymbiotic-organism-associated environment
   broad enough for both children, or record why the parent should remain
   minted without a definition or be marked `NOT_APPLICABLE`.
3. If the host-cell reading holds, replace the class-level sweep row with an
   item-level decision and add a parent term request under `ENVO:01001000`
   `environmental system determined by an organism`.

## Follow-up Checks

1. After item review, rerun
   `just validate data/habitats/host_associated/endosymbionts.yaml` on the
   regenerated Endosymbionts `HabitatRecord`.
2. Rerun `just term-requests-check` if the item review adds or changes an ENVO
   term request for this parent record.
3. Rerun `just verify-corpus --max-diffs 1` to verify the maintained decision,
   definition, and source inputs regenerate
   `data/habitats/host_associated/endosymbionts.yaml` exactly.
4. Repeat a hidden/ignored-inclusive exact search for
   `habitatmech:GOLD.895a2372e5`, all four raw `gold.ecosystem` IDs, and
   `Host-associated > Endosymbionts` before declaring the class-level decision
   fully superseded.

## Additional Notes

None found.
