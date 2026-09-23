# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/activated_sludge__f91e662c.yaml`
- Started UTC: 2026-09-23T11:59:00Z
- Finished UTC: 2026-09-23T12:02:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.0d353772af` |
| Label | `Activated Sludge` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:3506` |
| Source path | `Engineered > Wastewater > Activated Sludge` |
| Record status | Generated from `data/raw/` plus maintained curation inputs; generated YAML remains read-only |

This is the generated GOLD record for activated sludge directly under `Engineered > Wastewater`. `data/habitats/PATHS.tsv:1375` locks `habitatmech:GOLD.0d353772af` to the `activated_sludge__f91e662c` slug, and the identifier matches `sha1("GOLD:Engineered > Wastewater > Activated Sludge")[:10]`.

The target has no direct item-level row in `curation/decisions.tsv`, no authored definition in `curation/term_requests.tsv`, and no causal-graph overlay under `curation/causal_graphs`. Its maintained direct source row is `data/raw/gold_ecosystem_paths.tsv:47`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__f91e662c.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/activated_sludge__f91e662c.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the committed term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; the generated corpus still has 3206 records, 2520 `SEEDED` mappings, 686 `REVIEWED` mappings, 0 risky unreviewed groundings, and 0 swept concepts whose label or path currently names a non-habitat. |
| Reference validator | Not applicable; this record has no record-level `evidence`, no `causal_graphs`, and therefore no literature references for a reference-specific validator to resolve. |
| `git diff --check` | Passed before writing this report; no whitespace or patch errors were present. |

## Identity and Grounding

The direct GOLD identity is supported by `data/raw/gold_ecosystem_paths.tsv:47`:

| Raw field | Value |
|---|---|
| `canonical_path` | `Engineered > Wastewater > Activated Sludge` |
| `ecosystem` | `Engineered` |
| `ecosystem_category` | `Wastewater` |
| `ecosystem_type` | `Activated Sludge` |
| `ecosystem_subtype` | empty |
| `specific_ecosystem` | empty |
| `leaf_label` | `Activated Sludge` |
| `depth` | `3` |
| `gold_node_count` | `3` |
| `organism_count` | `789` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `789` |
| `gold_node_ids` | `gold.ecosystem:3506\|gold.ecosystem:3827\|gold.ecosystem:4254` |

The generic activated-sludge ontology parent is supported. `data/raw/gold_path_triads.tsv:154` records `ENVO:00002046` `activated sludge` as the one-sample medium context for the exact GOLD path; `data/raw/ontology_terms.tsv:7191` carries `ENVO:00002046` with label `activated sludge`; and `data/raw/ontology_subclass_edges.tsv:5293` records `ENVO:00002046 rdfs:subClassOf ENVO:00002044`, whose label is `sludge` at `data/raw/ontology_terms.tsv:7189`.

The generated source-path parent is the unsupported claim. The immediate GOLD parent path `Engineered > Wastewater` resolves to `ENVO:00002001`, has a reviewed item-level decision at `curation/decisions.tsv:243`, and is backed by `data/raw/gold_ecosystem_paths.tsv:38`. That correctly makes `Engineered > Wastewater` an exact waste-water record, but it does not make the child path's activated-sludge material a narrower kind of waste water.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| The generated record represents GOLD path `Engineered > Wastewater > Activated Sludge`. | `data/raw/gold_ecosystem_paths.tsv:47` | Supported. The raw `canonical_path`, `leaf_label`, and generated `source_path` agree. |
| The generated `source_id` is `gold.ecosystem:3506`, and the duplicate-node note is warranted. | `data/raw/gold_ecosystem_paths.tsv:47`; `src/habitatmech/seed.py` | Supported. The raw row lists three GOLD ecosystem node ids with `gold.ecosystem:3506` first; the seeder emits the first id and notes the collapsed node count when a canonical GOLD path has several node ids. |
| The source row carries 789 GOLD organism assertions. | `data/raw/gold_ecosystem_paths.tsv:47` | Supported. `organism_count` and `total_assertions` are both 789, and the generated source attestation records `assertion_count: 789` with `assertion_unit: ORGANISM`. |
| GOLD has exact side-table context for the target path. | `data/raw/gold_path_biosamples.tsv:71`; `data/raw/gold_studies.tsv`; `data/raw/gold_path_triads.tsv:152-154` | Supported as contextual metadata only. The exact path has a 484-biosample side-table row, appears in 58 study rows, and carries one-sample broad, local, and medium MIxS triad rows. These side tables do not make activated sludge a subtype of waste water. |
| The source concept is narrower than generic activated sludge. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_subclass_edges.tsv:5293`; sibling `Activated sludge` GOLD paths in `data/raw/gold_ecosystem_paths.tsv` | Supported. GOLD has many engineered `Activated sludge` leaves, while `ENVO:00002046` names activated sludge generically. |
| The target path is a kind of `ENVO:00002001` `waste water`. | Generated from the GOLD `Engineered > Wastewater` parent path after the seeder resolves that parent path to `ENVO:00002001`. | Unsupported. The parent path denotes wastewater; the child denotes activated sludge in a wastewater context rather than a narrower kind of waste water itself. |

Unsupported or over-scoped claims: `parent_habitats` turns a GOLD wastewater context edge into the false statement that activated-sludge material is itself a subtype of waste water.

## Completeness

No direct source fields are missing for the maintained GOLD row. The generated record carries the source name, first GOLD node id, leaf label, canonical path, duplicate-node note, `skos:narrowMatch` mapping predicate, 789-organism assertion count, the activated-sludge ontology parent, and the immediate GOLD path parent.

The record has no synonyms, xrefs, authored definition, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussions, datasets, or quality flags. Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.0d353772af`, `0d353772af`, `activated_sludge__f91e662c`, `gold.ecosystem:3506`, `gold.ecosystem:3827`, `gold.ecosystem:4254`, and the exact source path covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and generated records while excluding broad generated `build`, `data/text_map`, and `pages` outputs; they found the expected raw rows, generated target, and path lock, and no target-specific maintained curation input.

The same ignored/hidden-inclusive search found one aggregate path row, one 484-biosample row, 58 study rows that include the path, and three one-sample MIxS triad rows for `Engineered > Wastewater > Activated Sludge`.

The consequential gap is the inherited GOLD hierarchy. `src/habitatmech/seed.py` stores every resolved GOLD path, then adds the resolved next path prefix to each child as a parent; `build_document()` serializes that set as `parent_habitats`. Here that converts a wastewater context into an is-a parent for activated sludge.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-F91E662C-001 | major | `parent_habitats` asserts `habitatmech:GOLD.0d353772af` is a kind of `ENVO:00002001` `waste water`, but the child is activated sludge and the supported material parent is `ENVO:00002046` `activated sludge` under `ENVO:00002044` `sludge`. `parent_habitats` is an is-a relation, and this path edge turns GOLD's wastewater context into the false claim that activated sludge is wastewater itself. | Add an item-level decision for `habitatmech:GOLD.0d353772af` in `curation/decisions.tsv`; if the concept stays minted, add a `curation/term_requests.tsv` definition with `parent_mode=REPLACE` so the generated record keeps `ENVO:00002046` and drops the inherited `ENVO:00002001` parent. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add an item-level decision for `habitatmech:GOLD.0d353772af` in `curation/decisions.tsv`, keyed to the generated identifier and scoped to `Engineered > Wastewater > Activated Sludge`.

2. If the record denotes generic activated sludge rather than a wastewater-specific subtype, ground it directly to `ENVO:00002046` so the GOLD attestation merges into the existing activated-sludge identity.

3. If the record remains a minted wastewater-context-specific activated-sludge concept, add an authored definition under `curation/term_requests.tsv` with `ENVO:00002046` `activated sludge` as the genus and `parent_mode=REPLACE` so the next seed keeps the true activated-sludge parent and removes the false source-path parent.

4. Regenerate the corpus rather than editing `data/habitats/engineered/activated_sludge__f91e662c.yaml` directly.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.0d353772af`
- Inspect `data/habitats/engineered/activated_sludge__f91e662c.yaml`, or confirm the record intentionally merged away after an exact `GROUND`.
- `just seed-apply --force`
- `just validate data/habitats/engineered/activated_sludge__f91e662c.yaml` if the record stays minted; otherwise validate the record that absorbed its source attestation.
- `just validate-strict data/habitats/engineered/activated_sludge__f91e662c.yaml` if the record stays minted; otherwise validate the record that absorbed its source attestation.
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`
- Exact gitignore-independent searches for `habitatmech:GOLD.0d353772af`, `gold.ecosystem:3506`, `gold.ecosystem:3827`, `gold.ecosystem:4254`, and `Engineered > Wastewater > Activated Sludge` across `curation`, `data/raw`, `data/habitats`, `history`, and `research` to verify that no target-specific maintained input was missed.

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-activated_sludge__f91e662c.md' -print` included ignored files and found no pre-existing exact report for this record before this file was written.
- The direct false parent is not caused by a hand edit: `just verify-corpus --max-diffs 1` reproduced all 3206 generated records exactly from maintained inputs.
- The exact MIxS triad rows are intentionally not treated as support for `environmental_parameters`. They carry one submitted broad/local/medium context from the GOLD side table, not an authored physicochemical parameter row.
