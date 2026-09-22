# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/abdominal_adipose_tissue.yaml`
- Started UTC: 2026-09-22T21:18:20Z
- Finished UTC: 2026-09-22T21:23:41Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/abdominal_adipose_tissue.yaml` |
| Class | `HabitatRecord` |
| Identifier | `BTO:0004041` |
| Label | `abdominal adipose tissue` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Record status | Generated from one PREGO source concept grounded to its own BTO identifier |

This is the generated PREGO/BTO record for abdominal adipose tissue. PREGO supplies the source concept as `BTO:0004041`; `seed.py` addresses a future PREGO-specific curation row with the deterministic source key `habitatmech:PREGO.b7e2803d12`, computed from `sha1("PREGO:BTO:0004041")[:10]`, but resolves the generated record back to the BTO CURIE because PREGO's source id is already an ontology id.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/abdominal_adipose_tissue.yaml` | Passed; LinkML validation reported no issues. |
| `just validate-strict data/habitats/host_associated/abdominal_adipose_tissue.yaml` | Passed; one file scanned with 0 error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; expected 3206 generated records, found 3206, with 0 missing, 0 extra, and 0 differing. |
| `git diff --check` | Passed; no whitespace errors. |

## Identity and Grounding

The BTO identity is supported:

| Raw field | Value |
|---|---|
| `term_id` | `BTO:0004041` |
| `ontology` | `BTO` |
| `label` | `abdominal adipose tissue` |
| `definition` | `Adipose tissue located inside the peritoneal cavity, packed in between internal organs and torso. An excess of visceral fat is known as central obesity, or belly fat, the pot belly or beer belly effect, in which the abdomen protrudes excessively.` |
| `directly_referenced` | `TRUE` |
| `label_only` | `FALSE` |

`identifier`, `label`, `definition`, and `definition_source: BTO` match `data/raw/ontology_terms.tsv:4040`. `grounding_status: EXACT` is the normal PREGO self-grounding result from `src/habitatmech/seed.py`: the source concept is `BTO:0004041`, the record id is `BTO:0004041`, and there is no curation decision redirecting `habitatmech:PREGO.b7e2803d12`.

`habitat_category: HOST_ASSOCIATED` is consistent with BTO-derived anatomy. `infer_category()` maps `BTO` identifiers to `HOST_ASSOCIATED`, and the term denotes an anatomical adipose-tissue site rather than a disease, quality, process, procedure, sample artifact, or whole host taxon.

The `BTO:0001487` parent is supported. `data/raw/ontology_subclass_edges.tsv:2853` states `BTO:0004041 rdfs:subClassOf BTO:0001487`, and `data/raw/ontology_terms.tsv:1487` defines `BTO:0001487` as `adipose tissue`, which is strictly broader than abdominal adipose tissue.

`mapping_status: SEEDED` is mechanically expected. Ignored/hidden-inclusive exact searches for `habitatmech:PREGO.b7e2803d12` and `BTO:0004041` found no maintained `curation/decisions.tsv` row, so no item-level PREGO decision exists to promote this source concept to `REVIEWED`.

The vendored ontology slice also contains `UBERON:0007808` `adipose tissue of abdominal region` and `UBERON:0014454` `visceral abdominal adipose tissue`, both with overlapping abdominal/visceral fat synonyms. Those do not make this record wrong: PREGO's source id is already a BTO CURIE, and the record correctly preserves that source identity instead of remapping to a merely lexical UBERON synonym without a curator decision.

## Evidence

| Claim | Nearest support | Review |
|---|---|---|
| PREGO directly attests `BTO:0004041` as a `biolink:GrossAnatomicalStructure` habitat. | `data/raw/prego_habitats.tsv:644` | Supported exactly. |
| The PREGO row contributes one distinct associated taxon and one direct assertion. | `data/raw/prego_habitats.tsv:644` | Supported exactly: `taxon_count`, `direct_assertion_count`, and `max_prego_score` are all `1`/`3`, and the generated `source_attestations` keeps `assertion_count: 1`, `assertion_unit: TAXON`, `score: 3.0`, and `evidence_channels: annotated_genomes_isolates`. |
| The generated PREGO synonyms are source-owned alternate strings. | `data/raw/prego_habitats.tsv:644` | Supported exactly. All 15 generated `RELATED_SYNONYM` values are copied from `prego_synonyms`. |
| `NCBITaxon:1075399` is PREGO rank 1 out of 1 for this habitat. | `data/raw/prego_habitat_taxa.tsv:2818` | Supported exactly. The row names `Blattabacterium sp. (Cryptocercus punctulatus) str. Cpu`, rank `1`, score `3`, and no `corroborated_by` source; the generated taxon keeps the PREGO source, label, score, rank, and `candidate_pool: 1`. |
| `NCBITaxon:1075399` is a real NCBI taxon for `Blattabacterium sp. (Cryptocercus punctulatus) str. Cpu`. | NCBI BioProject metadata for `PRJNA71047` | Supported; the external spot-check agrees with the PREGO taxon label. |
| The generated record was seeded from PREGO with exact grounding. | `src/habitatmech/seed.py`; `data/raw/MANIFEST.yaml` | Supported. The seed event timestamp matches the August 2026 raw-inventory extraction, and no extra curated event is expected without a decision row. |

Unsupported or over-scoped claims: None found. The PREGO association with a `Blattabacterium` cockroach endosymbiont is not promoted beyond PREGO's own observation: the generated taxon omits `is_characteristic`, `reference`, and `corroborated_by`, which preserves the weaker reported-from semantics documented for PREGO-derived taxa.

## Completeness

The record carries every source-owned PREGO value that applies to this one-row input: source name, source id, BTO-derived source label, distinct-taxon assertion count, assertion unit, maximum PREGO score, channel string, every PREGO synonym, and the single top-taxon row.

No ontology definition is missing because `data/raw/ontology_terms.tsv` provides a BTO definition. No environmental parameters are missing because there is no `BTO:0004041` entry in `data/raw/environment_parameters.tsv` and PREGO anatomy rows do not provide MIxS triads. No causal graph, curated record-level evidence, discussion, or dataset is required for this generated seed record.

No maintained curation input was found for `habitatmech:PREGO.b7e2803d12`, `BTO:0004041`, `abdominal_adipose_tissue`, or `abdominal adipose tissue`; the exact ignored/hidden-inclusive searches covered `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/term_requests/envo_robot_template.tsv`, `curation/external_xrefs.tsv`, `curation/causal_graphs`, `history`, `research`, and `reports/yaml_record_review`.

No maintained causal overlay, history file, raw research report, or prior exact YAML review report was found by filename for `abdominal_adipose_tissue` or `abdominal-adipose-tissue` under `curation/causal_graphs`, `history`, `research`, or `reports/yaml_record_review`; the `find` search included ignored files beneath those checked directories.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If a future curator wants to mark the PREGO self-grounding item-reviewed, add a `REVIEW` row for `habitatmech:PREGO.b7e2803d12` in `curation/decisions.tsv` and rerun `just seed-canary BTO:0004041`. That should be a status-only change: keep the identifier at `BTO:0004041`, keep `BTO:0001487` as the only parent, and keep the PREGO taxon as observational unless a curator adds independent evidence for a stronger `is_characteristic` claim.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future status-promotion-only edit, run:

- `just seed-canary BTO:0004041`
- `just validate data/habitats/host_associated/abdominal_adipose_tissue.yaml`
- `just validate-strict data/habitats/host_associated/abdominal_adipose_tissue.yaml`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

## Additional Notes

- The pre-report exact filename check `find reports/yaml_record_review -maxdepth 1 -type f -name '*abdominal_adipose_tissue*' -print` returned no previous exact report; `find` includes ignored files.
- Exact ignored/hidden-inclusive content searches for `BTO:0004041`, `habitatmech:PREGO.b7e2803d12`, `abdominal_adipose_tissue`, `abdominal adipose tissue`, `BTO:0001487`, and `NCBITaxon:1075399` found the generated target, the PATHS row, the PREGO and BTO raw rows, two lexical UBERON alternatives, the generated broader adipose/fat-body sibling records, and no maintained curation owner that should have been applied to this record.
- `just worklist` does not list `BTO:0004041`, consistent with a PREGO self-grounded BTO record that is already generated as `EXACT`.
- `just report` completed successfully and did not flag `BTO:0004041` in any risky-grounding, GOLD-triad, novel-label, unsupported-prefix, or non-habitat section.
