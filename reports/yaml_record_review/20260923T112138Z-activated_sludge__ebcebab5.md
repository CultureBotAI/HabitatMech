# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/activated_sludge__ebcebab5.yaml`
- Started UTC: 2026-09-23T11:18:00Z
- Finished UTC: 2026-09-23T11:21:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.090dc47d34` |
| Label | `Activated sludge` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Source | `GOLD` |
| Source ID | `gold.ecosystem:4301` |
| Source path | `Engineered > Bioremediation > Terephthalate > Wastewater > Activated sludge` |
| Record status | Generated from `data/raw/` plus maintained curation inputs; generated YAML remains read-only |

This is the generated GOLD record for activated sludge under `Engineered > Bioremediation > Terephthalate > Wastewater`. `data/habitats/PATHS.tsv:1335` locks `habitatmech:GOLD.090dc47d34` to the `activated_sludge__ebcebab5` slug, and the identifier matches `sha1("GOLD:Engineered > Bioremediation > Terephthalate > Wastewater > Activated sludge")[:10]`.

The target has no direct item-level row in `curation/decisions.tsv`, no authored definition in `curation/term_requests.tsv`, and no causal-graph overlay under `curation/causal_graphs`. Its maintained direct source row is `data/raw/gold_ecosystem_paths.tsv:1230`.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__ebcebab5.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/activated_sludge__ebcebab5.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the committed term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; the generated corpus still has 3206 records, 2520 `SEEDED` mappings, 686 `REVIEWED` mappings, 0 risky unreviewed groundings, and 0 swept concepts whose label or path currently names a non-habitat. |
| Reference validator | Not applicable; this record has no record-level `evidence`, no `causal_graphs`, and therefore no literature references for a reference-specific validator to resolve. |
| `git diff --check` | Passed before writing this report; no whitespace or patch errors were present. |

## Identity and Grounding

The direct GOLD identity is supported by `data/raw/gold_ecosystem_paths.tsv:1230`:

| Raw field | Value |
|---|---|
| `canonical_path` | `Engineered > Bioremediation > Terephthalate > Wastewater > Activated sludge` |
| `ecosystem` | `Engineered` |
| `ecosystem_category` | `Bioremediation` |
| `ecosystem_type` | `Terephthalate` |
| `ecosystem_subtype` | `Wastewater` |
| `specific_ecosystem` | `Activated sludge` |
| `leaf_label` | `Activated sludge` |
| `depth` | `5` |
| `gold_node_count` | `1` |
| `organism_count` | `0` |
| `study_count` | `0` |
| `biosample_count` | `0` |
| `total_assertions` | `0` |
| `gold_node_ids` | `gold.ecosystem:4301` |

The generic activated-sludge ontology parent is supported: `data/raw/ontology_terms.tsv:7191` carries `ENVO:00002046` with label `activated sludge`, and `data/raw/ontology_subclass_edges.tsv:5293` records `ENVO:00002046 rdfs:subClassOf ENVO:00002044`. `data/raw/ontology_terms.tsv:7189` labels `ENVO:00002044` as `sludge`.

The generated source-path parent is the unsupported claim. The immediate GOLD parent path `Engineered > Bioremediation > Terephthalate > Wastewater` resolves to `habitatmech:GOLD.9ab362de60`, locked to `data/habitats/engineered/wastewater__430aea49.yaml` by `data/habitats/PATHS.tsv:2435`. That parent is a `Wastewater` source concept with `ENVO:00002001` as a broader wastewater parent. Activated sludge is a sludge material in a wastewater bioremediation context, not a narrower wastewater habitat.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| The generated record represents GOLD path `Engineered > Bioremediation > Terephthalate > Wastewater > Activated sludge`. | `data/raw/gold_ecosystem_paths.tsv:1230` | Supported. The raw `canonical_path`, `leaf_label`, and generated `source_path` agree. |
| The generated `source_id` is `gold.ecosystem:4301`, with no duplicate-node note. | `data/raw/gold_ecosystem_paths.tsv:1230`; `src/habitatmech/seed.py` | Supported. The raw row lists one GOLD ecosystem node id, so the seeder emits that id and no collapsed-node note. |
| The source attestation should omit `assertion_count` and `assertion_unit`. | `data/raw/gold_ecosystem_paths.tsv:1230`; `src/habitatmech/seed.py` | Supported. The raw row has `organism_count=0`, and the seeder emits GOLD organism counts only when this value is nonzero. |
| GOLD has exact side-table context for the target path. | `data/raw/gold_path_biosamples.tsv:780`; `data/raw/gold_studies.tsv:265`; `data/raw/gold_path_triads.tsv:59-61` | Supported as contextual metadata only. Four biosamples and one study are linked to the exact path; the one-sample MIxS triads say the submitted broad, local, and medium contexts were `anthropogenic environment`, `bioreactor`, and `raw primary sludge`, not direct support for a curated activated-sludge subtype. |
| The source concept is narrower than generic activated sludge. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_subclass_edges.tsv:5293`; sibling `Activated sludge` GOLD paths in `data/raw/gold_ecosystem_paths.tsv` | Supported. GOLD has many engineered `Activated sludge` leaves, while `ENVO:00002046` names activated sludge generically. |
| The target path is a kind of `habitatmech:GOLD.9ab362de60` `Wastewater`. | Generated from the GOLD `Engineered > Bioremediation > Terephthalate > Wastewater` parent path after the seeder resolves that parent to `habitatmech:GOLD.9ab362de60`. | Unsupported. The parent path is wastewater in a terephthalate bioremediation context; the child denotes activated-sludge material under that context rather than a narrower kind of wastewater. |

Unsupported or over-scoped claims: `parent_habitats` turns a GOLD wastewater context edge into the false statement that the activated-sludge material is itself a subtype of wastewater.

## Completeness

No direct source fields are missing for the maintained GOLD row. The generated record carries the source name, one GOLD node id, leaf label, canonical path, `skos:narrowMatch` mapping predicate, the activated-sludge ontology parent, and the immediate GOLD path parent.

The record has no synonyms, xrefs, authored definition, environmental parameters, characteristic taxa, record-level evidence, causal graphs, discussions, datasets, or quality flags. Exact hidden/ignored-inclusive searches for `habitatmech:GOLD.090dc47d34`, `090dc47d34`, `activated_sludge__ebcebab5`, `gold.ecosystem:4301`, and the exact source path covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and generated records while excluding broad generated `build`, `data/text_map`, and `pages` outputs; they found the expected raw row, generated target, and path lock, and no target-specific maintained curation input.

An exact ignored/hidden-inclusive search of `data/raw/gold_path_triads.tsv`, `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_studies.tsv`, and `data/raw/gold_ecosystem_paths.tsv` found one aggregate path row, one four-biosample row, one study row that includes the path, and three one-sample MIxS triad rows for `Engineered > Bioremediation > Terephthalate > Wastewater > Activated sludge`.

The consequential gap is the inherited GOLD hierarchy. `src/habitatmech/seed.py` stores every resolved GOLD path, then adds the resolved next path prefix to each child as a parent; `build_document()` serializes that set as `parent_habitats`. Here that converts a wastewater container/context into an is-a parent for activated sludge.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-EBCEBAB5-001 | major | `parent_habitats` asserts `habitatmech:GOLD.090dc47d34` is a kind of `habitatmech:GOLD.9ab362de60` `Wastewater`, but the child is activated sludge and the supported material parent is `ENVO:00002046` `activated sludge` under `ENVO:00002044` `sludge`. `parent_habitats` is an is-a relation, and this path edge turns GOLD's terephthalate/wastewater context into the false claim that activated sludge is wastewater itself. | Add an item-level decision for `habitatmech:GOLD.090dc47d34` in `curation/decisions.tsv`; if the concept stays minted, add a `curation/term_requests.tsv` definition with `parent_mode=REPLACE` so the generated record keeps `ENVO:00002046` and drops the inherited `Wastewater` parent. |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add an item-level decision for `habitatmech:GOLD.090dc47d34` in `curation/decisions.tsv`, keyed to the generated identifier and scoped to `Engineered > Bioremediation > Terephthalate > Wastewater > Activated sludge`.

2. If the record denotes generic activated sludge rather than a terephthalate/wastewater-specific subtype, ground it directly to `ENVO:00002046` so the GOLD attestation merges into the existing activated-sludge identity.

3. If the record remains a minted terephthalate/wastewater-specific activated-sludge concept, add an authored definition under `curation/term_requests.tsv` with `ENVO:00002046` `activated sludge` as the genus and `parent_mode=REPLACE` so the next seed keeps the true activated-sludge parent and removes the false source-path parent.

4. Regenerate the corpus rather than editing `data/habitats/engineered/activated_sludge__ebcebab5.yaml` directly.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.090dc47d34`
- Inspect `data/habitats/engineered/activated_sludge__ebcebab5.yaml`, or confirm the record intentionally merged away after an exact `GROUND`.
- `just seed-apply --force`
- `just validate data/habitats/engineered/activated_sludge__ebcebab5.yaml` if the record stays minted; otherwise validate the record that absorbed its source attestation.
- `just validate-strict data/habitats/engineered/activated_sludge__ebcebab5.yaml` if the record stays minted; otherwise validate the record that absorbed its source attestation.
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`
- Exact gitignore-independent searches for `habitatmech:GOLD.090dc47d34`, `gold.ecosystem:4301`, and `Engineered > Bioremediation > Terephthalate > Wastewater > Activated sludge` across `curation`, `data/raw`, `data/habitats`, `history`, and `research` to verify that no target-specific maintained input was missed.

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-activated_sludge__ebcebab5.md' -print` included ignored files and found no pre-existing exact report for this record before this file was written.
- The direct false parent is not caused by a hand edit: `just verify-corpus --max-diffs 1` reproduced all 3206 generated records exactly from maintained inputs.
- The exact MIxS triad rows are intentionally not treated as support for `environmental_parameters`. They carry one submitted broad/local/medium context from the GOLD side table, not an authored physicochemical parameter row.
