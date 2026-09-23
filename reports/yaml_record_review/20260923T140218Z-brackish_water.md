# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/brackish_water.yaml
- Started UTC: 2026-09-23T13:57:00Z
- Finished UTC: 2026-09-23T14:02:18Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/brackish_water.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00002019` |
| Label | `brackish water` |
| Category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Maintained inputs | `data/raw/ontology_terms.tsv`, `data/raw/ontology_subclass_edges.tsv`, `data/raw/environment_parameters.tsv`, `data/raw/madin_habitats.tsv`, `data/raw/madin_habitat_taxa.tsv`, `data/raw/prego_habitats.tsv`, `data/raw/prego_habitat_taxa.tsv`, `curation/causal_graphs/brackish_water.yaml`, `data/habitats/PATHS.tsv` |
| Generated output | Yes. `data/habitats/` records are emitted from `src/habitatmech/seed.py`; future curation belongs in the maintained inputs above, `curation/decisions.tsv`, `curation/term_requests.tsv`, or the existing `curation/causal_graphs/brackish_water.yaml` overlay. |

The full 585-line record was reviewed. It is a generated ENVO-grounded habitat record fed by the kg-microbe environment table, MADIN, PREGO, and one curated causal-graph overlay. It has ten environmental parameter bands, 25 PREGO taxon associations, 25 MADIN taxon associations, one graph with 16 nodes and 17 evidenced edges, the ENVO definition, the ENVO parent `ENVO:00002010`, and generated seed/graph history.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/brackish_water.yaml` | Pass: LinkML validation reported no issues. |
| `just validate-strict data/habitats/aquatic/brackish_water.yaml` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-causal curation/causal_graphs/brackish_water.yaml` | Pass: LinkML validation of the maintained causal overlay reported no issues. |
| `just validate-causal-all` | Pass: 32 causal-graph curation files and 32 graphs validated. |
| `just term-requests-check` | Pass: committed term-request table is current at 109 terms. |
| `just validate-history` | Pass: no issues found; 77 history records validated against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass: 3206 expected records, 3206 records found, 0 missing, 0 extra, 0 differing; the corpus reproduces exactly from `data/raw/`. |
| `just worklist --limit 2000` | Pass: 0 ungrounded records still undecided; 1810 decisions on file. |
| `just report` | Pass: full corpus report completed for 3206 records. |
| `git diff --check` | Pass: no whitespace errors. |
| Reference validator | Not applicable as an automated gate: HabitatMech exposes no focused PMID/DOI reachability validator for causal overlays. The five graph references were manually resolved through PubMed or the publisher DOI landing page and matched the article scopes named in the edge notes. |

## Identity and Grounding

| Assertion | Review |
|---|---|
| `identifier: ENVO:00002019` | Supported. `data/raw/ontology_terms.tsv` carries `ENVO:00002019` as an ENVO term with canonical label `brackish water` and the same saline-range definition copied into the generated record. |
| `label: brackish water` | Supported by the vendored ENVO row, the MADIN source row, the PREGO source row, and the `water_brackish` environment-table rows. |
| Environment-table source identity | Supported. `data/raw/environment_parameters.tsv` has ten exact `water_brackish` rows mapped only to `ENVO:00002019` / `brackish water`. The generated `ENVIRONMENTS_TABLE` source attestation has the same env_type as `source_id` and `source_label`. |
| MADIN source identity | Supported. `data/raw/madin_habitats.tsv` has one row for `ENVO:00002019`, ENVO, label `brackish water`, and 64 associated taxa. |
| PREGO source identity | Supported. `data/raw/prego_habitats.tsv` has one row for `ENVO:00002019` with `taxon_count=1015`, `direct_assertion_count=1016`, `max_prego_score=3`, channels `annotated_genomes_isolates\|environmental_samples`, and synonyms `brackish water\|brackish waters`. |
| `grounding_status: EXACT` | Supported for this seeded state. Environment-table, MADIN, and PREGO concepts are already ENVO CURIEs or rows mapped exactly to the ENVO term; no sibling, broader water-body class, salinity quality, or process is being adopted as identity. |
| `mapping_status: SEEDED` | Supported. Gitignore-independent searches of `curation`, `history`, and `research` found the graph overlay but no item-level `curation/decisions.tsv` row, `curation/term_requests.tsv` row, or append-only history record for `ENVO:00002019`. |
| `habitat_category: AQUATIC` | Supported by ENVO ancestry and the seeder's category inference for an ENVO water material. |
| `parent_habitats: ENVO:00002010` | Supported. `data/raw/ontology_subclass_edges.tsv` asserts `ENVO:00002019 rdfs:subClassOf ENVO:00002010`; `ENVO:00002010` is the vendored `saline water` class. |
| Path slug | Supported. `data/habitats/PATHS.tsv` maps `ENVO:00002019` to `brackish_water`. |

The adjacent `ENVO:01001321` `brackish water body` and `ENVO:01000322` `brackish water environment` terms are broader container/environment concepts, not exact replacements for the material-class identity here. The parent is also strictly broader: `saline water` covers brackish water and hypersaline water.

## Evidence

| Record field | Nearest maintained evidence | Review |
|---|---|---|
| Definition | `data/raw/ontology_terms.tsv` row for `ENVO:00002019` | Supported. The generated `definition` exactly matches the vendored ENVO definition, and `definition_source: ENVO` is the correct provenance for that source-owned text. |
| `source_attestations[0]` | Ten `data/raw/environment_parameters.tsv` rows with `env_type=water_brackish` | Supported. The raw rows attach ten qualitative bands to only `ENVO:00002019`, and the generated source note correctly says the assertion came from kg-microbe's environment table. |
| `source_attestations[1]` | `data/raw/madin_habitats.tsv` row for `ENVO:00002019` | Supported. The source ID, source label, `assertion_count: 64`, and `assertion_unit: TAXON` match the raw MADIN habitat row. |
| `source_attestations[2]` | `data/raw/prego_habitats.tsv` row for `ENVO:00002019` | Supported. The source ID, source label, distinct-taxon count, maximum score, and evidence channels match the PREGO source row; the direct assertion count is intentionally not used as the taxon-unit `assertion_count`. |
| PREGO synonym `brackish waters` | `data/raw/prego_habitats.tsv` `prego_synonyms` for `ENVO:00002019` | Supported. The seeder suppresses the source synonym equal to the record label and retains the plural source spelling as a PREGO `RELATED_SYNONYM`. |
| Ten `environmental_parameters` entries | `data/raw/environment_parameters.tsv` rows for `water_brackish` | Supported. The generated enum labels and qualitative values match `Gradients=low`, `Nutrients=medium`, `Pressure=low`, `Salinity=medium`, `Structural=low`, `Water=high`, `pH=medium`, `salinity variability=wide`, `temp variability=medium`, and `water variability=permanently wet`. |
| 25 PREGO `characteristic_taxa` entries | `data/raw/prego_habitat_taxa.tsv` rows for `ENVO:00002019` | Supported. The generated rows match the first 25 PREGO rows for this habitat, including NCBITaxon IDs, labels, scores, ranks, and `candidate_pool: 1015`. |
| 25 MADIN `characteristic_taxa` entries | `data/raw/madin_habitat_taxa.tsv` rows for `ENVO:00002019` | Supported. The generated rows match the 25 committed MADIN taxon rows for this habitat, and each preserves `candidate_pool: 64` from the MADIN habitat row. |
| `causal_graphs[0]` | `curation/causal_graphs/brackish_water.yaml` | Supported. The generated graph, all 16 nodes, all 17 edges, and every evidence item are emitted from the maintained overlay. |
| Causal graph reference IDs | PubMed and publisher DOI records | Supported. `PMID:15006771` resolves to Crump et al. on Parker River/Plum Island Sound bacterioplankton across an estuarine salinity gradient, `PMID:22895159` to Campbell and Kirchman's Delaware Bay salinity-gradient study, `PMID:34544488` to Tee et al. on benthic and planktonic diversity and osmoregulation across a river-to-sea tidal lagoon, `PMID:21663439` to Wood's bacterial osmoregulation review, and `DOI:10.1186/s40168-024-01817-w` to Wu et al. on short-residence-time estuarine salinity-gradient metagenomes. |

The PREGO and MADIN taxon rows are not overclaimed as curated characteristic taxa. The generated `CharacteristicTaxon` rows lack `is_characteristic`, so under the schema they record reported source associations only.

The causal-graph edges are supported at the right scope for a brackish-water osmotic-stress graph: the estuarine salinity-gradient papers back mixing, tidal variability, residence time, community turnover, and freshwater/marine filtering in brackish-to-marine transitions; Wood backs the generic bacterial osmoregulatory response; Wu et al. back salt-in and compatible-solute strategies across a natural estuarine salinity gradient.

## Completeness

No consequential gaps were found for this exact ENVO-seeded merge with a maintained causal overlay:

| Area | Review |
|---|---|
| Definition | Present from ENVO and faithfully preserved. |
| Xrefs | None expected from the inspected environment-table, MADIN, PREGO, overlay, and ontology inputs. |
| Environmental parameters | Complete for this source env_type. Multi-term brackish-sediment environment-table rows also mention `ENVO:00002019`, but they correctly do not attach to this material-only record because a multi-term row is not attached for only one component. |
| Causal graphs | Present and complete for the single maintained overlay targeting `ENVO:00002019`. |
| Discussions or datasets | None expected for the inspected maintained inputs. |
| Prior reports | `find reports/yaml_record_review -maxdepth 1 -type f -name '*-brackish_water.md' -print` found no earlier exact report; the search included ignored files through `find`. |
| Existing curation | Gitignore-independent searches found no `ENVO:00002019`, `water_brackish`, or `brackish_water` owner row in `curation/decisions.tsv`, `curation/term_requests.tsv`, or `history/`; they found only the expected maintained causal overlay in `curation/causal_graphs/brackish_water.yaml`. |
| External research | Gitignore-independent searches found no `ENVO:00002019`, `water_brackish`, or `brackish_water` hit in `research/` or existing YAML review reports. |

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No corrective follow-up is required. If a future curator changes the brackish-water source mapping or graph overlay, rerun:

- `just validate data/habitats/aquatic/brackish_water.yaml`
- `just validate-strict data/habitats/aquatic/brackish_water.yaml`
- `just validate-causal curation/causal_graphs/brackish_water.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`
- `git diff --check`

## Additional Notes

- Exact searches for absence checks used `find` or `rg --no-ignore --hidden`, so ignored files were included.
- `curation/causal_graphs/liquid_water.yaml` also cites `PMID:21663439`; that is a separate, valid use of Wood's osmoregulation review for the broader liquid-water graph and does not conflict with this brackish-water graph.
