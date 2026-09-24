# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/anaerobic_aerobic.yaml
- Started UTC: 2026-09-24T14:08:57Z
- Finished UTC: 2026-09-24T14:08:57Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/habitats/engineered/anaerobic_aerobic.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.4a2450370b` |
| Label | `Anaerobic-Aerobic` |
| Category | `ENGINEERED` |
| Generated or maintained | Generated from committed GOLD source inventories, `curation/decisions.tsv`, and `data/habitats/PATHS.tsv`; `data/habitats/` remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:1837` maps `habitatmech:GOLD.4a2450370b` to `anaerobic_aerobic` |
| Grounding | `UNGROUNDED` |
| Mapping status | `SEEDED` |

## Validation

| Check | Result |
| --- | --- |
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-anaerobic_aerobic.md' -print` | Passed; no prior exact `anaerobic_aerobic` review was present before this report was written. `find` included ignored files under `reports/yaml_record_review`. |
| `just validate data/habitats/engineered/anaerobic_aerobic.yaml` | Passed; no LinkML issues found. |
| `just validate-strict data/habitats/engineered/anaerobic_aerobic.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | Not applicable; the target record has no record-level `evidence`, no causal graph, and no DOI, PMID, or URL evidence items to validate. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 records were expected, 3206 were present, and there were 0 missing, extra, or differing records. |
| `just worklist --limit 2000` | Passed; 0 ungrounded records are still undecided and 1810 decisions are on file. |
| `just report` | Passed; completed the corpus report for 3206 records. |
| `git diff --check` | Passed before report creation. |

## Identity and Grounding

The minted identifier denotes the zero-assertion GOLD path `Engineered > Bioreactor > EBPR > Anaerobic-Aerobic`. `data/raw/gold_ecosystem_paths.tsv:1185` lists that exact canonical path with `leaf_label` `Anaerobic-Aerobic`, depth 4, `gold_node_count` 1, `organism_count` 0, `study_count` 0, `biosample_count` 0, `total_assertions` 0, and node id `gold.ecosystem:7761`. The generated source attestation at `data/habitats/engineered/anaerobic_aerobic.yaml:8-12` repeats the path and source node.

The current maintained decision is only a lexical class sweep. `curation/decisions.tsv:486` records `CONFIRM_UNGROUNDED` with no object term and `review_depth` `CLASS`; the row says no term matched by the class-level search routes and explicitly says the sweep did not assess whether `Engineered > Bioreactor > EBPR > Anaerobic-Aerobic` is a habitat at all.

The same leaf label occurs in two sibling engineered branches. `data/raw/gold_ecosystem_paths.tsv:1207` and `data/raw/gold_ecosystem_paths.tsv:1221` list `Engineered > Bioreactor > SBR-EBPR > Anaerobic-Aerobic` and `Engineered > Bioreactor > Thiocyanate-remediating > Anaerobic-Aerobic`. These records should not be collapsed by their shared leaf label unless item-level review finds a real source-concept equivalence.

An ignored/hidden-inclusive exact search for `Anaerobic-Aerobic`, `anaerobic-aerobic`, `anaerobic/aerobic`, `anaerobic aerobic`, `EBPR`, and `enhanced biological phosphorus` over `data/raw/ontology_terms.tsv`, `curation/term_requests.tsv`, and `curation/term_requests_excluded.tsv` found no exact ontology term, no target-specific term request, and no excluded term-request row. The target might still deserve a novel term request if item review confirms it is a reactor habitat rather than an EBPR operating-mode folder.

The current `parent_habitats` edge points at the source parent `habitatmech:GOLD.b5081d36b9` `EBPR`. That parent is also a zero-direct-assertion intermediate GOLD path with only a class-level `CONFIRM_UNGROUNDED` row at `curation/decisions.tsv:1024`, so the generated edge is traceable as source hierarchy but not yet backed by an item-level strict-broader habitat review.

## Evidence

| Claim | Evidence | Status |
| --- | --- | --- |
| The generated record denotes the GOLD path `Engineered > Bioreactor > EBPR > Anaerobic-Aerobic`. | `data/raw/gold_ecosystem_paths.tsv:1185` lists the canonical path and `gold.ecosystem:7761`; `data/habitats/engineered/anaerobic_aerobic.yaml:8-12` repeats both in the GOLD source attestation. | Supported exactly. |
| The GOLD path has no direct source assertions. | `data/raw/gold_ecosystem_paths.tsv:1185` reports 0 organisms, 0 studies, 0 biosamples, and 0 total assertions. | Supported exactly; the generated source attestation correspondingly omits count and unit fields. |
| EBPR/Anaerobic-Aerobic has child paths under GOLD. | `data/raw/gold_ecosystem_paths.tsv:1186-1187` lists `Activated sludge` and `Sludge` children below the target path. | Supported exactly. |
| The only study and biosample evidence in the EBPR/Anaerobic-Aerobic branch is on a child `Sludge` path, not the target itself. | Ignored/hidden-inclusive exact search for `Engineered > Bioreactor > EBPR > Anaerobic-Aerobic` found one `data/raw/gold_studies.tsv` row, one `data/raw/gold_path_biosamples.tsv` row, and three `data/raw/gold_path_triads.tsv` rows only for `Engineered > Bioreactor > EBPR > Anaerobic-Aerobic > Sludge`. | Supported for the committed GOLD source tables. |
| The class-level decision did not inspect the target's source path or candidate terms. | `curation/decisions.tsv:486` sets `review_depth` to `CLASS`, and `docs/CURATION.md` plus `docs/HARMONIZATION.md` define `CLASS` as a mechanically defined screen, not an item-level review. | Supported exactly. |
| No causal overlay is attached to `habitatmech:GOLD.4a2450370b`. | Ignored/hidden-inclusive exact search over `curation/causal_graphs` found no `identifier: habitatmech:GOLD.4a2450370b`, and `find curation/causal_graphs -maxdepth 1 -type f -name '*anaerobic*' -print` returned no files. | Supported exactly. |

## Completeness

The generated record is complete for the current source row but still materially incomplete as curation. It has the exact GOLD source path, the locked slug, one generated parent, one class-level decision, no definition, no synonyms, no xrefs, no direct assertion count, no environmental parameters, no characteristic taxa, no record-level evidence, and no causal graph.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `research`, `reports`, `conf/id_label_targets.yaml`, `data/habitats/PATHS.tsv`, `data/habitats/engineered`, `data/raw/gold_ecosystem_paths.tsv`, `data/raw/gold_path_biosamples.tsv`, `data/raw/gold_studies.tsv`, `data/raw/gold_path_triads.tsv`, and `data/raw/ontology_terms.tsv`. They found the target path, sibling Anaerobic-Aerobic paths, child EBPR/Anaerobic-Aerobic material paths, the target decision row, the generated target, the locked slug, the existing target-child activated-sludge YAML review, an adjacent same-label SBR-EBPR activated-sludge review, and no target-specific term request, history event, committed research report, causal overlay, direct GOLD biosample row, direct GOLD study row, or direct GOLD MIxS triad row.

The earlier `activated_sludge__6bcd092f` review already flagged `habitatmech:GOLD.4a2450370b` as an unreviewed `parent_habitats` value on a child material record. Reviewing this parent confirms the same upstream cause: GOLD provides an intermediate operating-context node, but the maintained curation has not decided whether that node is itself a habitat or merely a contextual folder for sludge and activated-sludge children.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | `Anaerobic-Aerobic` under EBPR remains at a class-level `CONFIRM_UNGROUNDED` decision whose note says habitathood was not assessed. The raw GOLD row has zero direct organisms, studies, or biosamples, and the committed sample evidence is confined to a child `Sludge` path, so the current record has not been item-reviewed as a real habitat that needs a novel label. | `curation/decisions.tsv:486`; add supporting definition and hierarchy in `curation/term_requests.tsv` if the concept stays minted. |
| Major | The generated `EBPR` parent is only source-path context. `curation/decisions.tsv:1024` leaves `habitatmech:GOLD.b5081d36b9` at `review_depth` `CLASS`, so no maintained input has established that the target is a strict subtype of an EBPR habitat rather than an operating mode within an EBPR bioreactor. | `curation/decisions.tsv:1024` for the parent; `curation/decisions.tsv:486` and possibly `curation/term_requests.tsv` for the target. |

## Recommended Edits

1. Reopen `habitatmech:GOLD.4a2450370b` in `curation/decisions.tsv` with `review_depth` `ITEM`; decide whether the GOLD node denotes a microbial habitat, an operating-mode folder that should be `NOT_APPLICABLE`, or a narrower EBPR reactor configuration that deserves a minted definition.
2. If the target stays minted, add a `curation/term_requests.tsv` row with an evidence-backed label and definition, a true ontology genus such as `ENVO:00002123` `bioreactor` if supported, and a `parent_mode` choice that preserves only strict broader parents.
3. Review the parent `habitatmech:GOLD.b5081d36b9` `EBPR` in the same curation pass so future regeneration does not keep threading child material records through an unreviewed operating-context node.
4. Rerun `just seed`, canary `habitatmech:GOLD.4a2450370b`, apply the regenerated corpus, and confirm the target, `activated_sludge__6bcd092f`, and `sludge__c3365fbe` have only strict, reviewed `parent_habitats` edges.

## Follow-up Checks

- `rg --no-ignore --hidden -n 'habitatmech:GOLD\.4a2450370b|habitatmech:GOLD\.b5081d36b9' curation/decisions.tsv curation/term_requests.tsv history research data/habitats/engineered`
- `just seed-canary habitatmech:GOLD.4a2450370b`
- `just seed-apply --force`
- `just validate data/habitats/engineered/anaerobic_aerobic.yaml`
- `just validate-strict data/habitats/engineered/anaerobic_aerobic.yaml`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

## Additional Notes

The target has no causal overlay, so no focused `just validate-causal curation/causal_graphs/<slug>.yaml` command applies.
