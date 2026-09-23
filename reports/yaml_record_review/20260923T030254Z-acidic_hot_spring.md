# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/terrestrial/acidic_hot_spring.yaml`
- Started UTC: 2026-09-23T02:58:00Z
- Finished UTC: 2026-09-23T03:02:54Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Path | `data/habitats/terrestrial/acidic_hot_spring.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00002120` |
| Label | `acidic hot spring` |
| Habitat category | `TERRESTRIAL` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Record status | Generated from the PREGO inventory plus the vendored ontology slice |
| PREGO source id | `ENVO:00002120` |
| Locked slug | `data/habitats/PATHS.tsv:642` maps `ENVO:00002120` to `acidic_hot_spring` |

This is the generated ENVO-grounded PREGO record for `acidic hot spring`. PREGO uses the ENVO CURIE directly, so the seeder keeps `ENVO:00002120` as the record identifier with `grounding_status: EXACT`.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/habitats/terrestrial/acidic_hot_spring.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/terrestrial/acidic_hot_spring.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal-all` | Passed; validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Passed; the term-request table is current at 109 generated terms. |
| `just validate-history` | Passed; 77 history records validated. |
| `just verify-corpus --max-diffs 1` | Passed; all 3,206 expected records reproduced exactly from `data/raw/`, with 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; reported 0 undecided ungrounded records and 1,810 decisions on file. |
| `just report` | Passed; the corpus summary still reports 0 risky groundings not yet reviewed, 0 class-level sweeps contradicted by the current slice, 0 swept concepts whose path names a term the leaf does not, and 0 current organism/process habitat claims. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identity is supported exactly. `data/raw/ontology_terms.tsv:7216` gives `ENVO:00002120` the canonical label `acidic hot spring`, the ENVO definition "An acidic spring through which groundwater, heated by geothermal energy, flows.", the exact synonym `acid hot spring`, `is_directly_referenced: TRUE`, and `label_only: FALSE`. `data/habitats/PATHS.tsv:642` pins the identifier to slug `acidic_hot_spring`, matching the reviewed YAML path.

The ontology hierarchy is also preserved exactly. `data/raw/ontology_subclass_edges.tsv:5319-5320` records both asserted broader parents, `ENVO:00000051` `hot spring` and `ENVO:01001898` `acidic spring`, and `data/habitats/terrestrial/acidic_hot_spring.yaml:22-24` emits those two CURIEs as `parent_habitats`. The vendored parent definitions show that both are true broader classes: a hot spring is a spring through which geothermally heated groundwater flows, and an acidic spring is a spring through which low-pH water flows.

The PREGO attestation is a direct self-grounding. `data/raw/prego_habitats.tsv:461` records source id `ENVO:00002120`, vocabulary `ENVO`, Biolink type `OntologyClass`, three taxon assertions, three direct assertions, maximum PREGO score `3`, evidence channel `annotated_genomes_isolates`, and the lexical variants `acid hot spring|acid hot springs|acidic hot spring|acidic hot springs`. The generated source attestation correctly carries source id `ENVO:00002120`, the ontology-derived label `acidic hot spring`, `assertion_count: 3`, `assertion_unit: TAXON`, score `3.0`, and the same evidence channel.

The deterministic PREGO source-concept key is `habitatmech:PREGO.2582fd283b`, computed from `sha1("PREGO:ENVO:00002120")[:10]`. An ignored/hidden-inclusive exact search over `curation`, `data/raw`, `data/habitats/PATHS.tsv`, `history`, `research/habitats`, and `reports/yaml_record_review`, excluding only generated `data/text_map/**`, `pages/**`, and `build/**`, found no item-level row for that key; `mapping_status: SEEDED` is therefore expected.

## Evidence

| Claim | Source | Assessment |
| --- | --- | --- |
| The record identifier, label, definition, and `definition_source: ENVO` match the vendored ontology slice. | `data/raw/ontology_terms.tsv:7216`; `data/habitats/terrestrial/acidic_hot_spring.yaml:1-8` | Supported exactly. |
| `acid hot spring` is an ENVO exact synonym, while PREGO contributes related plural variants. | `data/raw/ontology_terms.tsv:7216`; `data/raw/prego_habitats.tsv:461`; `data/habitats/terrestrial/acidic_hot_spring.yaml:9-21` | Supported exactly. The singular `acidic hot spring` PREGO spelling is the ontology primary label and is not duplicated as a generated synonym. |
| `ENVO:00000051` `hot spring` and `ENVO:01001898` `acidic spring` are the only direct vendored ontology parents of `ENVO:00002120`. | `data/raw/ontology_subclass_edges.tsv:5319-5320`; `data/raw/ontology_terms.tsv:6645`; `data/raw/ontology_terms.tsv:9388` | Supported exactly. |
| The PREGO source has three direct taxon assertions from annotated genome or isolate evidence, with a maximum score of `3`. | `data/raw/prego_habitats.tsv:461` | Supported exactly. |
| The rank-1 characteristic taxon is `NCBITaxon:1056495` `Caldisphaera lagunensis DSM 15908`. | `data/raw/prego_habitat_taxa.tsv:6006` | Supported exactly. |
| The rank-2 characteristic taxon is `NCBITaxon:380749` `Hydrogenobaculum sp. Y04AAS1`. | `data/raw/prego_habitat_taxa.tsv:6007` | Supported exactly. |
| The rank-3 characteristic taxon is `NCBITaxon:397948` `Caldivirga maquilingensis IC-167`. | `data/raw/prego_habitat_taxa.tsv:6008` | Supported exactly. |

Unsupported or over-scoped claims: none found. No environmental parameters, record-level evidence, causal graphs, discussion links, datasets, or quality flags are asserted by the generated record, so this review did not need to assess parameter ranges, causal edge evidence, or dataset relevance.

## Completeness

No consequential slot is underfilled for the maintained inputs that feed this record. The sole `source_attestations` entry captures the complete PREGO source id, source label, assertion count, `TAXON` unit, maximum score, and evidence channel; all three PREGO taxon rows for `ENVO:00002120` are emitted as `characteristic_taxa` entries; both direct ENVO parents are present; and no authored term request is expected because this record uses an existing exact ENVO term.

Exact ignored/hidden-inclusive content searches for `ENVO:00002120`, `acidic_hot_spring`, `acidic hot spring`, `acid hot spring`, `habitatmech:PREGO.2582fd283b`, `NCBITaxon:1056495`, `NCBITaxon:380749`, and `NCBITaxon:397948` covered `curation`, `data/raw`, `data/habitats/PATHS.tsv`, `history`, `research/habitats`, and `reports/yaml_record_review`, excluding only generated `data/text_map/**`, `pages/**`, and `build/**`. They found the expected path lock, raw PREGO rows, ontology rows, and generated record, plus mentions of the `ENVO:00002120` candidate in earlier `acid_lake` and `acidic_lake` review reports and unrelated acidic-hot-spring examples in host-associated research reports; they found no target-specific maintained curation row, term request, causal graph, history entry, or prior exact `acidic_hot_spring` review report.

Filename searches for `*acidic_hot_spring*`, `*acidic-hot-spring*`, `*ENVO_00002120*`, and `*00002120*` under `curation/causal_graphs`, `history`, `research/habitats`, and `reports/yaml_record_review` returned no target-specific maintained artifact. Those `find` searches include ignored files under the checked directories.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

## Follow-up Checks

No corrective follow-up is required.

Re-run the same focused validation set if future curation changes the PREGO rollup, vendored `ENVO:00002120` term, path lock, or characteristic-taxon emission:

- `just validate data/habitats/terrestrial/acidic_hot_spring.yaml`
- `just validate-strict data/habitats/terrestrial/acidic_hot_spring.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

If future review redirects `ENVO:00002120` away from this direct PREGO self-grounding, add an explicit `curation/decisions.tsv` row for `habitatmech:PREGO.2582fd283b` first, regenerate with `just seed`, and verify that the PREGO attestation and three characteristic taxa remain attached to the surviving record.

## Additional Notes

- The pre-report exact record check `find data/habitats -name 'acidic_hot_spring.yaml' -print` found exactly one generated target; `find` includes ignored files.
- The pre-report exact report check `find reports/yaml_record_review -maxdepth 1 -type f -name '*-acidic_hot_spring.md' -print` returned no previous exact report; `find` includes ignored files.
- `Caldisphaera lagunensis DSM 15908` also appears in the broader `ENVO:00000051` hot-spring PREGO and MADIN inputs. That corroborates the organism's hot-spring context on the parent record, but it is not needed to support this child record's rank-1 PREGO taxon row.
