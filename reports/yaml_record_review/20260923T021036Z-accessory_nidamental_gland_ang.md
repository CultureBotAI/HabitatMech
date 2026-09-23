# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/accessory_nidamental_gland_ang.yaml`
- Started UTC: 2026-09-23T02:06:00Z
- Finished UTC: 2026-09-23T02:10:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Path | `data/habitats/host_associated/accessory_nidamental_gland_ang.yaml` |
| Class | `HabitatRecord` |
| Identifier | `habitatmech:GOLD.453b1756ab` |
| Label | `accessory nidamental gland` |
| Habitat category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `REVIEWED` |
| Record status | Generated from one GOLD source concept, one item-level `CONFIRM_UNGROUNDED` decision, and one term-request row |
| GOLD source ids | `gold.ecosystem:7869`, `gold.ecosystem:7870` |
| GOLD source path | `Host-associated > Mollusca > Reproductive system > Accessory nidamental gland (ANG)` |
| Decision row | `curation/decisions.tsv:1664` |
| Term request row | `curation/term_requests.tsv:80` |
| External xref row | `curation/external_xrefs.tsv:3` |
| Locked slug | `data/habitats/PATHS.tsv:1809` maps `habitatmech:GOLD.453b1756ab` to `accessory_nidamental_gland_ang` |

This is the generated record for the GOLD cephalopod accessory nidamental gland path. The GOLD source-concept key is `habitatmech:GOLD.453b1756ab`, reproducibly computed as `sha1("GOLD:Host-associated > Mollusca > Reproductive system > Accessory nidamental gland (ANG)")[:10]`. The record has the intended shape for an exact real habitat whose exact anatomy term is unavailable for grounding: it remains minted and `UNGROUNDED`, keeps the inactive and unvendored exact `CEPH:0000001` term only as an xref, uses vendored `UBERON:0003937` as a broader anatomy parent, and carries an authored term request for ontology submission.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/habitats/host_associated/accessory_nidamental_gland_ang.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/host_associated/accessory_nidamental_gland_ang.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Passed; the term-request table is current at 109 generated terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just verify-corpus --max-diffs 1` | Passed; all 3,206 expected records reproduced exactly from `data/raw/`, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; reported 0 undecided ungrounded records and 1,810 decisions on file. |
| `just report` | Passed; the corpus summary still reports 0 risky groundings not yet reviewed, 0 contradicted sweeps, and 0 current records claiming a non-habitat organism/process term as a habitat. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identity is reproducible. `data/raw/gold_ecosystem_paths.tsv:2492` is exactly the GOLD path `Host-associated > Mollusca > Reproductive system > Accessory nidamental gland (ANG)`, and the source-concept path hashes to `453b1756ab`. `data/habitats/host_associated/accessory_nidamental_gland_ang.yaml:1-29` preserves the minted identifier, term-request label, curated synonyms, `CEPH:0000001` xref, first GOLD source id, source label, full source path, and the note that the collapsed GOLD path covers two node ids.

The locked slug is correct: `data/habitats/PATHS.tsv:1809` maps `habitatmech:GOLD.453b1756ab` to `accessory_nidamental_gland_ang`, and a pre-report ignored-file-inclusive `find data/habitats -name 'accessory_nidamental_gland_ang.yaml' -print` found exactly one generated target.

The raw source row has two GOLD ecosystem node ids and 0 organism, study, biosample, and total assertions. The generated source attestation therefore correctly omits `assertion_count`, `assertion_unit`, and `mapping_predicate`: the record is the minted source concept itself, not an ontology-grounded record that would need a `skos:*Match` predicate.

The source-path parent is traceable. `data/raw/gold_ecosystem_paths.tsv:866` records `Host-associated > Mollusca > Reproductive system`; that path hashes to `habitatmech:GOLD.fcc934bd13`; `data/habitats/PATHS.tsv:3168` locks it to `reproductive_system__54f3b564`; and `data/habitats/host_associated/reproductive_system__54f3b564.yaml:1-15` is the generated parent with the expected two GOLD organism assertions from three GOLD node ids.

`mapping_status: REVIEWED` follows the maintained item-level decision. `curation/decisions.tsv:1664` records `CONFIRM_UNGROUNDED` with `review_depth: ITEM`, `object_id: CEPH:0000001`, `object_label: accessory nidamental gland`, and `relation: xref` for `habitatmech:GOLD.453b1756ab`; the generated `CONFIRM_UNGROUNDED` event mirrors that row in `data/habitats/host_associated/accessory_nidamental_gland_ang.yaml:35-45`.

The `CEPH:0000001` xref is explicitly allowed. `curation/external_xrefs.tsv:3` verifies the `CEPH:0000001` label and records why the exact Cephalopod Ontology anatomy term is retained only as an `xref` from an inactive, unvendored ontology, not as a HabitatMech identity or broader parent.

The curated definition, synonyms, and `UBERON:0003937` parent all come from `curation/term_requests.tsv:80`. The requested parent exists in the vendored slice as `reproductive gland`, with definition "Any of the organized aggregations of cells that function as secretory or excretory organs and are associated with reproduction." `UBERON:0003937` is therefore a true broader anatomy genus for the accessory nidamental gland rather than a near-miss identity.

The definition's boundaries are supported. The committed deep-research report scoped the GOLD path to the dissected cephalopod symbiotic reproductive organ and explicitly excluded the main nidamental gland, egg jelly coat or capsule, light organ, oviducal gland, mantle cavity, and whole host clade. The inspected primary literature also supports the core defining claims: Bloodgood 1977 reported epithelium-lined tubules filled with dense bacteria; Collins et al. 2012 found ANG bacterial populations partitioned in host tubules and likely deposited into egg jelly; Kamp et al. 2025 resolved individual non-intersecting tubules that converge where bacteria can mix with squid jelly; and the horizontal/environmental acquisition claim is already traced in the research report to Kaufman et al. 1998 and follow-up bobtail-squid studies.

## Evidence

| Claim | Source | Assessment |
| --- | --- | --- |
| The record represents the GOLD path `Host-associated > Mollusca > Reproductive system > Accessory nidamental gland (ANG)`. | `data/raw/gold_ecosystem_paths.tsv:2492`; `data/habitats/host_associated/accessory_nidamental_gland_ang.yaml:24-29` | Supported exactly. |
| Two GOLD node ids share this collapsed path, and the path has no upstream organism/study/biosample assertions. | `data/raw/gold_ecosystem_paths.tsv:2492`; generated source note at `data/habitats/host_associated/accessory_nidamental_gland_ang.yaml:29` | Supported exactly. |
| `habitatmech:GOLD.fcc934bd13` is the immediate GOLD source-path parent. | `data/raw/gold_ecosystem_paths.tsv:866`; `data/habitats/PATHS.tsv:3168`; `data/habitats/host_associated/reproductive_system__54f3b564.yaml:1-15` | Supported as the generated parent from the GOLD path hierarchy. |
| `CEPH:0000001` exactly names the accessory nidamental gland but is xref-only for this record. | `curation/decisions.tsv:1664`; `curation/external_xrefs.tsv:3`; `data/habitats/host_associated/accessory_nidamental_gland_ang.yaml:21-22` | Supported. The maintained decision uses `relation: xref`, and the external-xref row records `inactive_unvendored`. |
| `UBERON:0003937` `reproductive gland` is a valid broader parent. | `data/raw/ontology_terms.tsv:13224`; `curation/term_requests.tsv:80`; `data/habitats/host_associated/accessory_nidamental_gland_ang.yaml:18-20` | Supported. The term is present in the vendored slice and is broader than this cephalopod female accessory gland. |
| The authored definition is narrower than the generic source label and distinguishes the real habitat from neighboring organs and downstream egg jelly. | `curation/term_requests.tsv:80`; `research/habitats/host_associated/accessory-nidamental-gland-ang-habitatmech-gold-453b1756ab-deep-research-claude_code.md:147-268`; primary ANG literature inspected by DOI/PMID from the report | Supported. The term request did not import uncertain report claims about pigmentation chemistry, oxygen tension, or fixed dominant taxa. |
| `Accessory nidamental gland (ANG)` and `accessory nidamental glands` are exact synonyms. | `curation/term_requests.tsv:80`; `research/habitats/host_associated/accessory-nidamental-gland-ang-habitatmech-gold-453b1756ab-deep-research-claude_code.md:244-253` | Supported. The source label is preserved and the plural names the paired organ without changing identity. |

Unsupported or over-scoped claims: none found. No environmental parameters, characteristic taxa, causal graphs, discussions, or datasets are asserted by the generated record, so this review did not need to assess parameter ranges, taxon typicality, causal edge evidence, or dataset relevance.

## Completeness

The record has the maintained inputs expected for this source concept: a reviewed item-level decision, a curated definition and broader parent in `curation/term_requests.tsv`, an exact inactive/unvendored xref in `curation/external_xrefs.tsv`, two history records for the 2026-09-10 curation work, and a successful committed deep-research report recorded in `reports/habitat_research_manifest.tsv`.

Exact ignored/hidden-inclusive content searches for `habitatmech:GOLD.453b1756ab`, `gold.ecosystem:7869`, `gold.ecosystem:7870`, `accessory_nidamental_gland_ang`, and `Accessory nidamental gland (ANG)` covered `curation`, `history`, `research/habitats`, `reports`, `data/raw`, and `data/habitats/PATHS.tsv`, excluding only generated `data/text_map/**`, `pages/**`, and `build/**`. They found the expected maintained TSV rows, the raw GOLD row, the locked `PATHS.tsv` row, the successful research manifest row plus two failed pre-success attempts, the committed target research report, two target history records, and a broader Mollusca research report that mentions this GOLD path.

Filename searches found no target-specific causal overlay and no previous exact review report. `find curation/causal_graphs -maxdepth 1 \( -name '*accessory*' -o -name '*nidamental*' -o -name '*453b1756ab*' \) -print` returned no rows, and `find reports/yaml_record_review -maxdepth 1 -type f -name '*-accessory_nidamental_gland_ang.md' -print` returned no previous exact report. Those `find` checks include ignored files beneath the checked directories.

The missing causal overlay is not a correctness gap. Accessory-nidamental-gland literature describes bacterial community partitioning, horizontal acquisition, and egg-defense effects that could support a future graph, but the schema does not require a causal graph for every well-studied record, and the current generated YAML makes no unsupported causal claims.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

A future curation pass could add an evidence-backed causal graph for ANG tubule partitioning, environmental colonization, and egg-defense biology using the same committed report as a literature index, but that would be additive curation rather than a correction to this reviewed record.

## Follow-up Checks

No corrective follow-up is required.

If this record later gains a causal-graph overlay or changes its term request, rerun:

- `just seed`
- `just seed-canary habitatmech:GOLD.453b1756ab`
- `just validate data/habitats/host_associated/accessory_nidamental_gland_ang.yaml`
- `just validate-strict data/habitats/host_associated/accessory_nidamental_gland_ang.yaml`
- `just validate-causal curation/causal_graphs/<overlay>.yaml`, if an overlay is added
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- The pre-report exact record check `find data/habitats -name 'accessory_nidamental_gland_ang.yaml' -print` found exactly one generated target; `find` includes ignored files.
- The pre-report exact report check `find reports/yaml_record_review -maxdepth 1 -type f -name '*-accessory_nidamental_gland_ang.md' -print` returned no previous exact report; `find` includes ignored files.
- `reports/habitat_research_manifest.tsv` records two failed provider attempts for `habitatmech:GOLD.453b1756ab` before the successful 504-second, 26,558-byte report. The maintained term request cites the successful committed report rather than either failed attempt.
- `UBERON:0002788` `anterior nuclear group` is present in the vendored slice as a thalamic region with synonym `ANG`, but it is deliberately absent from this record. The maintained decision already records that the abbreviation match is a false lexical hit for a molluscan reproductive gland.
- The source parent `habitatmech:GOLD.fcc934bd13` is still `mapping_status: SEEDED`; that does not block this record's `REVIEWED` status because mapping status is derived from item-level decisions for contributing source concepts, not from the status of every source-derived parent.
