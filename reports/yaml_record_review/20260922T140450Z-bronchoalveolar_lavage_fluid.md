# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml`
- Started UTC: 2026-09-22T14:04:50Z
- Finished UTC: 2026-09-22T14:04:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `BTO:0000155` |
| Label | `bronchoalveolar lavage fluid` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained owner | Raw PREGO row in `data/raw/prego_habitats.tsv:333`; no `habitatmech:PREGO.bdc9910582` item-level row in `curation/decisions.tsv` yet |
| Locked slug | `data/habitats/PATHS.tsv:33` maps `BTO:0000155` to `bronchoalveolar_lavage_fluid` |

This is a seeded PREGO-backed record for `BTO:0000155`. It passes structural validation and reproduces exactly, but it still needs item-level curation because the BTO slice defines `bronchoalveolar lavage fluid` as the lavage sampling technique and the raw PREGO association alone does not establish that a recovered clinical lavage material should be modeled as an in situ microbial habitat.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `git diff --check` | Pass; no whitespace or patch errors after this report was written |

## Identity and Grounding

The generated fields trace to raw PREGO and BTO inputs, but no curator has yet decided whether this source term belongs in HabitatMech:

- `data/raw/prego_habitats.tsv:333` is the raw PREGO habitat row for `BTO:0000155`. It records ontology `BTO`, `biolink:GrossAnatomicalStructure`, `taxon_count` 10, `direct_assertion_count` 10, `max_prego_score` 3, channel `annotated_genomes_isolates`, and the synonym pipe `BAL cell|BAL cells|bronchioalveolar lavage|bronchioalveolar lavage s|bronchioalveolar lavages|bronchoalveolar lavage fluid|bronchoalveolar lavage fluids`.
- `data/raw/ontology_terms.tsv:157` provides the generated label and definition for `BTO:0000155`. The definition says bronchiolar and alveolar cells and fluid are removed by wedging a bronchoscope into a bronchus, pumping in sterile saline, and withdrawing the fluid for diagnosis or treatment evaluation.
- `data/raw/prego_habitat_taxa.tsv:203` through `:212` provide the ten generated PREGO taxon associations, ranks, taxon IDs and labels, all with score `3` and channel `annotated_genomes_isolates`.
- `data/habitats/PATHS.tsv:33` pins the ontology record to `bronchoalveolar_lavage_fluid`.
- No ignored/hidden-inclusive exact search found an item-level `curation/decisions.tsv` row for the PREGO source-concept key `habitatmech:PREGO.bdc9910582` or an equivalent curated decision elsewhere.

`grounding_status: EXACT` is the seeder's direct projection of PREGO's BTO CURIE, not a curator-reviewed conclusion. The term may belong in HabitatMech if curators intentionally model lavage fluid as a host-associated sampled material, but the current BTO definition reads as a procedure for recovering lower-airway sample fluid rather than a stable microbial habitat. That uncertainty is material enough to keep the record out of `REVIEWED` status until an item-level decision records the intended semantics.

## Evidence

Every populated field is explainable from raw PREGO or the ontology slice:

| Claim | Nearest source | Review |
|---|---|---|
| Identifier `BTO:0000155`, label `bronchoalveolar lavage fluid`, and BTO definition | `data/raw/ontology_terms.tsv:157` | Supported exactly as an ontology projection; the definition itself is the semantic concern |
| `mapping_status: SEEDED` | Absence of an item-level `habitatmech:PREGO.bdc9910582` decision in `curation/decisions.tsv` | Supported exactly |
| PREGO source attestation, `assertion_count: 10`, `assertion_unit: TAXON`, `score: 3.0`, and `evidence_channels: annotated_genomes_isolates` | `data/raw/prego_habitats.tsv:333` | Supported exactly |
| Six generated `RELATED_SYNONYM` values | `data/raw/prego_habitats.tsv:333` | Supported; the seeder drops the synonym equal to the record label and keeps the remaining PREGO-provided strings |
| Ten PREGO taxa, ranks 1 through 10, score `3.0`, and `candidate_pool: 10` | `data/raw/prego_habitat_taxa.tsv:203-212`, `data/raw/prego_habitats.tsv:333` | Supported exactly; these are observational PREGO associations and none is upgraded with `is_characteristic` |
| Empty parent, xref, environmental-parameter, record-level evidence, causal-graph, discussion, and dataset slots | No maintained term request, causal overlay, or side-table row found in bounded exact searches | Supported as an accurate projection of current inputs |

The PREGO associations show that organisms or taxa were associated with the PREGO habitat term through annotated genomes and isolates. They do not by themselves prove that bronchoalveolar lavage fluid is a resident microbial habitat rather than a sampling product that proxies the lung, bronchiole, or alveolus.

## Completeness

The generated PREGO and taxon fields are complete for the current raw inputs:

- All ten `data/raw/prego_habitat_taxa.tsv` rows for `BTO:0000155` appear in the generated record with the correct ranks, IDs, labels, scores, source, and candidate pool.
- The source attestation preserves the PREGO count, max score, and evidence channel without summing it with any unlike GOLD or BacDive count.
- The generated synonyms preserve PREGO's non-label synonym strings as `RELATED_SYNONYM`, including the cell-form synonyms and the malformed `bronchioalveolar lavage s` source string.
- No curator-authored term request, causal graph, record-level evidence, discussion, or history entry is required until the item-level identity decision decides whether this is a valid habitat record.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and the generated host-associated records, excluding generated `build`, `data/text_map`, and `pages` trees. They found the raw PREGO rows, BTO ontology row, path lock, and generated YAML cited above; they found no target-specific curation decision, term request, causal overlay, history record, research report, GOLD or BacDive source row, or prior exact YAML review report.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `BTO:0000155` remains an unreviewed seeded PREGO term even though its ontology definition describes the bronchoalveolar-lavage sampling procedure. The record therefore currently exposes a sampled clinical lavage material as an `EXACT` host-associated microbial habitat without an item-level decision explaining why that sampled fluid should be retained as the habitat identity instead of being excluded, redirected to a lower-airway material, or modeled only as evidence for lung, bronchiole, or alveolar habitats. | Add an item-level `habitatmech:PREGO.bdc9910582` decision in `curation/decisions.tsv`, then regenerate `BTO:0000155`. |

## Recommended Edits

- Add an item-level `curation/decisions.tsv` row for the PREGO `BTO:0000155` source concept, keyed by `habitatmech:PREGO.bdc9910582`.
- In that row, either explicitly confirm why `bronchoalveolar lavage fluid` is a valid host-associated habitat identity, or mark the PREGO term as not applicable to prevent a lavage procedure or recovered sample from being published as an in situ habitat.
- Regenerate the target with `just seed` and preview `BTO:0000155` with `just seed-canary BTO:0000155` before applying the full generated corpus.

## Follow-up Checks

After adding the maintained decision row, re-run the same focused validation set and confirm the generated `mapping_status`, source attestation, characteristic taxa, and history event reflect the reviewed decision:

- `just validate data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml`
- `just validate-strict data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -name '*bronchoalveolar_lavage_fluid*' -print` found no pre-existing exact review report for this record before this file was written.
- Exact ignored/hidden-inclusive content searches for `habitatmech:PREGO.bdc9910582`, `BTO:0000155`, `bronchoalveolar_lavage_fluid`, `bronchoalveolar lavage fluid`, and `bronchoalveolar lavage` found no maintained curation or research artifact beyond the raw PREGO and BTO rows cited above.
