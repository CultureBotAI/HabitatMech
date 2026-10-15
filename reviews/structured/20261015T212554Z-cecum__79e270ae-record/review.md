# Record review: Cecum (habitatmech:GOLD.a8f8c792c1)

- Review: 20261015T212554Z-cecum__79e270ae-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T21:15:03Z
- Finished UTC: 2026-10-15T21:25:54Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The mammalian source can retain generic BTO cecum as its anatomical genus, but not whole mammalian large intestine as an is-a parent. Its 164 ORGANISM assertions reproduce the raw source. The BTO parent record has a separately identified molluscan merger defect; that does not make the mammalian-to-BTO class relation itself false. The narrow-mapping endpoint is independently inconsistent.

## Scope And Provenance

Full field-by-field scientific assessment of this exact target at 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b.

Selection: One of the next 24 path-ordered unreviewed identifiers in the ignored-inclusive 3208-record census. This bundle assesses one exact identifier, not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.a8f8c792c1 | data/habitats/host_associated/cecum__79e270ae.yaml | generated | Cecum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.a8f8c792c1 | Finished 2026-10-15T21:15:05Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cecum__79e270ae.yaml |
| validate-strict | passed | True | habitatmech:GOLD.a8f8c792c1 | Finished 2026-10-15T21:15:16Z. uv run python scripts/validate_strict.py data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.a8f8c792c1 | Finished 2026-10-15T21:15:30Z. No issues found<br>824 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.a8f8c792c1 | Finished 2026-10-15T21:15:32Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.a8f8c792c1 | Finished 2026-10-15T21:16:11Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.a8f8c792c1 | Finished 2026-10-15T21:16:19Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.a8f8c792c1 | Finished 2026-10-15T21:16:50Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.a8f8c792c1 | Finished 2026-10-15T21:17:56Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline native QC | passed | True | habitatmech:GOLD.a8f8c792c1 | Verified 2026-10-15T21:13:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38805081742 |

## Scientific And Domain Assessments

### Identity, definition, category and ancestry

identity: concern. Targets: habitatmech:GOLD.a8f8c792c1.

The mammalian source can retain generic BTO cecum as its anatomical genus, but not whole mammalian large intestine as an is-a parent. Its 164 ORGANISM assertions reproduce the raw source. The BTO parent record has a separately identified molluscan merger defect; that does not make the mammalian-to-BTO class relation itself false. The narrow-mapping endpoint is independently inconsistent.

### Frozen source counts, units, ranks, channels and pool

quantity: supported. Targets: habitatmech:GOLD.a8f8c792c1.

Exact source rows reproduce all emitted counts and displayed taxon rows. [{"source": "GOLD", "count": 164, "unit": "ORGANISM"}]. Zero GOLD counts are omitted; supplemental biosamples and study memberships are not added to tree ORGANISM counts.

### Biological support and bounded uncertainty

evidence: supported. Targets: habitatmech:GOLD.a8f8c792c1.

The mammalian source can retain generic BTO cecum as its anatomical genus, but not whole mammalian large intestine as an is-a parent. Its 164 ORGANISM assertions reproduce the raw source. The BTO parent record has a separately identified molluscan merger defect; that does not make the mammalian-to-BTO class relation itself false. The narrow-mapping endpoint is independently inconsistent.

### Native status, optional fields and mechanisms

completeness: supported. Targets: habitatmech:GOLD.a8f8c792c1.

Executed resolution reproduces NARROW/SEEDED. No target environmental parameters, causal graphs, discussions, datasets or is_characteristic=true claims are present. Optional absence and SEEDED status alone do not warrant findings; parent mechanisms are not inherited.

### Deterministic validity and source fidelity

schema: supported. Targets: habitatmech:GOLD.a8f8c792c1.

Ordinary/strict target validation, 824 histories, source provenance, exact 3208-record reproduction, 32 causal overlays, 110 term requests, configured labels and exact-base remote QC passed. These are not substitutes for scientific identity assessment.

## Findings

### F1: Containing anatomy is emitted as a broader habitat class

major / open / confirmed; issue key: cecum--79e270ae-context-parent.

Exclude only the exact GOLD source-path/expected-parent contribution habitatmech:GOLD.6bda0871e2. The mammalian source can retain generic BTO cecum as its anatomical genus, but not whole mammalian large intestine as an is-a parent. Its 164 ORGANISM assertions reproduce the raw source. The BTO parent record has a separately identified molluscan merger defect; that does not make the mammalian-to-BTO class relation itself false. The narrow-mapping endpoint is independently inconsistent. Preserve independent valid ontology genera and raw source paths.

### F2: Narrow predicate uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: cecum--79e270ae-mapping-endpoint-contract.

Resolution retains the GOLD source mint but emits narrowMatch relative to its ontology parent. SourceAttestation declares a source-to-record relation. Reconcile producer, schema and downstream consumers under #1398 without merging host-specific concepts or blindly reversing predicates. This is not a claim that SKOS prohibits self-links and does not certify SSSOM/KGX conformance.

## Recommended Actions And Acceptance Checks

### ACT1

Exclude only the exact GOLD source-path/expected-parent contribution habitatmech:GOLD.6bda0871e2. The mammalian source can retain generic BTO cecum as its anatomical genus, but not whole mammalian large intestine as an is-a parent. Its 164 ORGANISM assertions reproduce the raw source. The BTO parent record has a separately identified molluscan merger defect; that does not make the mammalian-to-BTO class relation itself false. The narrow-mapping endpoint is independently inconsistent. Preserve independent valid ontology genera and raw source paths. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Resolution retains the GOLD source mint but emits narrowMatch relative to its ontology parent. SourceAttestation declares a source-to-record relation. Reconcile producer, schema and downstream consumers under #1398 without merging host-specific concepts or blindly reversing predicates. This is not a claim that SKOS prohibits self-links and does not certify SSSOM/KGX conformance. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/cecum__79e270ae.yaml; Entire target YAML | supports | All fields, displayed taxa, source attestations and complete generated history read. |
| ERULE | docs/CURATION.md; Identity, strictly broader hierarchy and source evidence rules | supports | All parent contributions must be strictly broader. Disease, organism, sampled material and habitat meanings are distinct. Optional absence is not automatically a defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation and category semantics | supports | Source mapping endpoints are source-to-record. Reported associations do not imply characteristic presence. Native category and optional-field contracts retained. |
| ESEED | src/habitatmech/seed.py; Executed source resolution and full generated-document reproduction | supports | [{"mint": "habitatmech:GOLD.a8f8c792c1", "automatic": {"identifier": "habitatmech:GOLD.a8f8c792c1", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["BTO:0000166"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.a8f8c792c1", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["BTO:0000166"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source projections, taxon ranking and counts | supports | Frozen counts/units, maximum scores, channels, candidate pools and top taxon rows were traced to exact source rows. Original PREGO pair citation links are not retained in this projection. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 138 | supports | [{"row": 138, "data": {"canonical_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum", "ecosystem": "Host-associated", "ecosystem_category": "Mammals", "ecosystem_type": "Digestive system", "ecosystem_subtype": "Large intestine", "specific_ecosystem": "Cecum", "leaf_label": "Cecum", "depth": "5", "gold_node_count": "1", "organism_count": "164", "study_count": "0", "biosample_count": "0", "total_assertions": "164", "gold_node_ids": "gold.ecosystem:4105"}}] |
| ET6 | data/raw/gold_path_biosamples.tsv; Physical TSV rows 81 | supports | [{"row": 81, "data": {"canonical_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum", "ecosystem_path_id": "4105", "biosample_count": "405"}}] |
| ET7 | data/raw/gold_studies.tsv; Physical TSV rows 16,133,134,135,136,257,298,352,832,865,1333,1448,1461,2360,2620,2633,2643,2654,2696,2704,2788,2834,2912,2916,2923,3047,3108,3111,3203,3477,3770,3844,3951 | supports | [{"row": 16, "data": {"study_gold_id": "Gs0045062", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 133, "data": {"study_gold_id": "Gs0047139", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 134, "data": {"study_gold_id": "Gs0047140", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 135, "data": {"study_gold_id": "Gs0047141", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 136, "data": {"study_gold_id": "Gs0047142", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 257, "data": {"study_gold_id": "Gs0056639", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 298, "data": {"study_gold_id": "Gs0060783", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 352, "data": {"study_gold_id": "Gs0063335", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 832, "data": {"study_gold_id": "Gs0114534", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 865, "data": {"study_gold_id": "Gs0114692", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 1333, "data": {"study_gold_id": "Gs0121394", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 1448, "data": {"study_gold_id": "Gs0127566", "path_count": "20", "paths": "Engineered &gt; Artificial ecosystem &gt; Sand microcosm&#124;Engineered &gt; Industrial production &gt; Chemical products &gt; Reagent blank&#124;Engineered &gt; WWTP &gt; Wastewater&#124;Environmental &gt; Aquatic &gt; Deep subsurface &gt; Shale gas/oil reservoir &gt; Produced water/Flow back&#124;Environmental &gt; Aquatic &gt; Freshwater &gt; Lake&#124;Environmental &gt; Aquatic &gt; Freshwater &gt; Lake &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Marine&#124;Environmental &gt; Aquatic &gt; Marine &gt; Gulf&#124;Environmental &gt; Aquatic &gt; Marine &gt; Inlet&#124;Environmental &gt; Aquatic &gt; Marine &gt; Mud volcano &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Marine &gt; Strait&#124;Environmental &gt; Terrestrial &gt; Asphalt lakes &gt; Tar&#124;Environmental &gt; Terrestrial &gt; Deep subsurface &gt; Oil well&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Proximal colon&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Rectum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Small intestine&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; Rumen fluid"}}, {"row": 1461, "data": {"study_gold_id": "Gs0128738", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 2360, "data": {"study_gold_id": "Gs0142264", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 2620, "data": {"study_gold_id": "Gs0144759", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 2633, "data": {"study_gold_id": "Gs0144772", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 2643, "data": {"study_gold_id": "Gs0144782", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 2654, "data": {"study_gold_id": "Gs0144793", "path_count": "2", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Fecal"}}, {"row": 2696, "data": {"study_gold_id": "Gs0144911", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 2704, "data": {"study_gold_id": "Gs0144920", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 2788, "data": {"study_gold_id": "Gs0145049", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 2834, "data": {"study_gold_id": "Gs0145095", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 2912, "data": {"study_gold_id": "Gs0145229", "path_count": "3", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Small intestine &gt; Ileum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Small intestine &gt; Jejunum"}}, {"row": 2916, "data": {"study_gold_id": "Gs0145233", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 2923, "data": {"study_gold_id": "Gs0145240", "path_count": "2", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Fecal"}}, {"row": 3047, "data": {"study_gold_id": "Gs0150220", "path_count": "4", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Fecal&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Small intestine &gt; Ileum"}}, {"row": 3108, "data": {"study_gold_id": "Gs0150285", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 3111, "data": {"study_gold_id": "Gs0150288", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 3203, "data": {"study_gold_id": "Gs0150382", "path_count": "2", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Fecal"}}, {"row": 3477, "data": {"study_gold_id": "Gs0150665", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 3770, "data": {"study_gold_id": "Gs0153857", "path_count": "3", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Fecal"}}, {"row": 3844, "data": {"study_gold_id": "Gs0153961", "path_count": "1", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum"}}, {"row": 3951, "data": {"study_gold_id": "Gs0154267", "path_count": "11", "paths": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Cecum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Rectum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Small intestine &gt; Duodenum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Small intestine &gt; Ileum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Small intestine &gt; Jejunum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; Abomasum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; Omasum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; Reticulum&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; Rumen&#124;Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; Rumen mucosa"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 168 | supports | [{"row": 168, "data": {"term_id": "BTO:0000166", "ontology": "BTO", "label": "cecum", "definition": "The first part of the large intestine, forming a dilated pouch into which open the ileum, colon, and appendix vermiformis.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EP9 | data/habitats/host_associated/cecum.yaml; Entire immediate parent record; context only | supports | {"identifier": "BTO:0000166", "label": "cecum", "definition": "The first part of the large intestine, forming a dilated pouch into which open the ileum, colon, and appendix vermiformis.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Cecum/Intestinal cecum", "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "blind intestine", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "blind intestines", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "blind intestinous", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "blindgut", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "blindguts", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "caeca", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "caecal", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "caecum", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "caecums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "ceca", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "cecal", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "cecums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum caeca", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum caecal", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum caecum", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum caecums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum crassum caeca", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum crassum caecal", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum crassum caecum", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum crassum caecums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum crassum ceca", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum crassum cecal", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum crassum cecum", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum crassum cecums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats": ["habitatmech:GOLD.c336fb0bb7"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7832", "source_label": "Cecum/Intestinal cecum", "source_path": "Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Cecum/Intestinal cecum", "mapping_predicate": "skos:exactMatch"}, {"source": "PREGO", "source_id": "BTO:0000166", "source_label": "cecum", "assertion_count": 549, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "annotated_genomes_isolates&#124;environmental_samples"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:100176", "source": "PREGO", "taxon_label": "Papillibacter cinnamivorans", "score": 4.0, "rank": 1, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:100883", "source": "PREGO", "taxon_label": "Coprobacillus", "score": 4.0, "rank": 2, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:102106", "source": "PREGO", "taxon_label": "Collinsella", "score": 4.0, "rank": 3, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:102234", "source": "PREGO", "taxon_label": "Cyanobacterium", "score": 4.0, "rank": 4, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1032526", "source": "PREGO", "taxon_label": "Pedosphaera", "score": 4.0, "rank": 5, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1091138", "source": "PREGO", "score": 4.0, "rank": 6, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:109326", "source": "PREGO", "taxon_label": "Anaerovorax", "score": 4.0, "rank": 7, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1117", "source": "PREGO", "taxon_label": "Cyanobacteriota", "score": 4.0, "rank": 8, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:113286", "source": "PREGO", "taxon_label": "Pseudoramibacter", "score": 4.0, "rank": 9, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:117563", "source": "PREGO", "taxon_label": "Granulicatella", "score": 4.0, "rank": 10, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:118747", "source": "PREGO", "taxon_label": "Bulleidia", "score": 4.0, "rank": 11, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:119852", "source": "PREGO", "taxon_label": "Oscillospira", "score": 4.0, "rank": 12, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1249", "source": "PREGO", "taxon_label": "Weissella paramesenteroides", "score": 4.0, "rank": 13, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1253", "source": "PREGO", "taxon_label": "Pediococcus", "score": 4.0, "rank": 14, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1263", "source": "PREGO", "taxon_label": "Ruminococcus", "score": 4.0, "rank": 15, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1265", "source": "PREGO", "taxon_label": "Ruminococcus flavefaciens", "score": 4.0, "rank": 16, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1266", "source": "PREGO", "taxon_label": "Sarcina", "score": 4.0, "rank": 17, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1268", "source": "PREGO", "taxon_label": "Micrococcaceae", "score": 4.0, "rank": 18, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1269", "source": "PREGO", "taxon_label": "Micrococcus", "score": 4.0, "rank": 19, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1279", "source": "PREGO", "taxon_label": "Staphylococcus", "score": 4.0, "rank": 20, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1280", "source": "PREGO", "taxon_label": "Staphylococcus aureus", "score": 4.0, "rank": 21, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1282", "source": "PREGO", "taxon_label": "Staphylococcus epidermidis", "score": 4.0, "rank": 22, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:128827", "source": "PREGO", "taxon_label": "Erysipelotrichaceae", "score": 4.0, "rank": 23, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1296", "source": "PREGO", "taxon_label": "Mammaliicoccus sciuri", "score": 4.0, "rank": 24, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1300", "source": "PREGO", "taxon_label": "Streptococcaceae", "score": 4.0, "rank": 25, "candidate_pool": 549}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to BTO:0000166 'cecum' (EXACT). Slash alternative naming one structure. Path: Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Cecum/Intest (source concept habitatmech:GOLD.37d9cdc188)"}, {"timestamp": "2026-08-13T00:00:00Z", "curator": "claude-opus-5", "action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date. (source concept habitatmech:PREGO.35b3d0b858)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD, PREGO. Grounding: EXACT."}]} |
| EP10 | data/habitats/host_associated/large_intestine__834e53c8.yaml; Entire immediate parent record; context only | supports | {"identifier": "habitatmech:GOLD.6bda0871e2", "label": "Large intestine", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000059", "habitatmech:GOLD.c8e85f3c84"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:3660", "source_label": "Large intestine", "source_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine", "mapping_predicate": "skos:narrowMatch", "assertion_count": 37, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000166/graph; BTO_0000166-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000166", "target": "http://purl.obolibrary.org/obo/BTO_0000706", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000166", "target": "http://purl.obolibrary.org/obo/BTO_0002273", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000166; BTO_0000166.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0000166", "label": "cecum", "is_obsolete": false, "description": ["The first part of the large intestine, forming a dilated pouch into which open the ileum, colon, and appendix vermiformis."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059/graph; UBERON_0000059-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000059", "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059", "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059", "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059", "target": "http://purl.obolibrary.org/obo/UBERON_0000160", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059", "target": "http://purl.obolibrary.org/obo/UBERON_0004907", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059; UBERON_0000059.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0000059", "label": "large intestine", "is_obsolete": false, "description": ["A subdivision of the digestive tract that connects the small intestine to the cloaca or anus. Lacks or has few villi[Kardong]."]} |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.a8f8c792c1 -e Cecum -e cecum__79e270ae -e habitatmech:GOLD.a8f8c792c1 curation history research reports data/raw build reviews | context_only | Exact source rows were parsed separately; no formal structured target predecessor was found. Broad label matches were treated as leads, not all read. |

## Limits And Additional Notes

- Individual source specimens and all original pair-level citations have not been independently reconstructed. Counts, ranks and source scores are not prevalence or characteristic presence.
- Configured label validation skips 2061 no-adapter pairs. Displayed TaxIds were separately checked against current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged scientific input base, not a new local full-QC execution. These new bundles require their own post-save archive check.
- iModulonDB is not applicable to target claims: no gene, regulator, expression module or causal mechanism is asserted. Papers mentioning genes are used only for source context. No paid research was used.
- All captured local inputs were compared with both current bytes and exact Git-base blobs. The review explicitly assesses that committed revision.
- Ignored-inclusive archive search found no previous structured observation targeting this identifier. Legacy prose is a lead, not formal predecessor lineage or automatic closure.
- Read-only review: no curation, generation, native status/history promotion or GitHub mutation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T212554Z-cecum__79e270ae-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Cecum (habitatmech:GOLD.a8f8c792c1)'
started_at: '2026-10-15T21:15:03Z'
finished_at: '2026-10-15T21:25:54Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses target and evidence; not independent reviewer
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The mammalian source can retain generic BTO cecum as its anatomical genus,
  but not whole mammalian large intestine as an is-a parent. Its 164 ORGANISM assertions
  reproduce the raw source. The BTO parent record has a separately identified molluscan
  merger defect; that does not make the mammalian-to-BTO class relation itself false.
  The narrow-mapping endpoint is independently inconsistent.
source:
  git_revision: 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b
  state: git_commit
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 4544b5d2c11fbbb3a46cd8a65f7e664363df78c1000c590aab533219f9eec59b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce
    role: context
  - path: CLAUDE.md
    sha256: 98d95f910ff5160bc5b2ff572766785519dacdba487700bebaa6dbf96d071fd9
    role: context
  - path: conf/id_label_targets.yaml
    sha256: e100d84aabccaeb00c1a60246142b3cafcec009dbfba58f5cc319c35adddb633
    role: context
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: 490d3478aadc1dc3c4f04770d06db02fead4964d2e40ff339bfa389d46a5918a
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 12be4a7eccfcc6a9b9ef89fc1cb009e8f5e9ab87005bd6eb7ba93c910abf8f6d
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: bc7a13d922c179cd9bcd4d37b348bc90a39b08a4dafba7af4ed0039ad99621c3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: a2a0496837ea75e487d7fc5d35317a890262a941d8fffe9babcd39f2f332c6db
    role: context
  - path: data/habitats/host_associated/cecum.yaml
    sha256: 623da28718fc205e72e52b35719ed08693a1d8b5850f49df7b38ebff5438815c
    role: context
  - path: data/habitats/host_associated/cecum__79e270ae.yaml
    sha256: e2f9e69138fed3775e5c7cf0d20b39d3394dc7081d7b8a647ee20d55306cc76e
    role: target
  - path: data/habitats/host_associated/large_intestine__834e53c8.yaml
    sha256: 2c086c4115cc2a0b04df48cb9b989c051c96d6625a64dbe26cef1ac90e6d4d15
    role: context
  - path: data/raw/GOLD_MANIFEST.yaml
    sha256: 99ec487ae02d512cfb75440685f927abe907effe52cb755feb095631e8841489
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 4657672d429be35e551ceef4a1204ab0a8120558ce63e2a2b74188eee94b8480
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/bacdive_source_taxa.tsv
    sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
    role: context
  - path: data/raw/environment_parameters.tsv
    sha256: a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/gold_path_biosamples.tsv
    sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
    role: context
  - path: data/raw/gold_path_triads.tsv
    sha256: b1717bd8fc4fdcd6a1a132f4eb32df3638b01ddf7d78f9a5797f110ee2b1e8d6
    role: context
  - path: data/raw/gold_studies.tsv
    sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
    role: context
  - path: data/raw/isolation_source_groundings.tsv
    sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
    role: context
  - path: data/raw/madin_habitat_taxa.tsv
    sha256: d30854cfcffca0405914d04071ac47053938d354d5df250125843131b7c91fd7
    role: context
  - path: data/raw/madin_habitats.tsv
    sha256: 2ae1756f40242600365c49bfbdada4bce5fc8b86630426bb34892f055e5a5c93
    role: context
  - path: data/raw/ontology_subclass_edges.tsv
    sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
    role: context
  - path: data/raw/ontology_terms.tsv
    sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
    role: context
  - path: data/raw/prego_habitat_taxa.tsv
    sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
    role: context
  - path: data/raw/prego_habitats.tsv
    sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
    role: context
  - path: docs/CURATION.md
    sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/curate/__init__.py
    sha256: d9837c29dc61d8c9245fdb471a68a109cea31b131cdbc0c4d51d23a8d013ce12
    role: context
  - path: src/habitatmech/curate/causal_graphs.py
    sha256: d1884374263ed7926292c52a58742c614e75628d78ff50fe688e6abc0ddf9c1c
    role: context
  - path: src/habitatmech/curate/curation_event.py
    sha256: 08c774d309fe988c468097518d346f07a653b283cb9b9b51c7fe79fa0af785a9
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
    role: context
  - path: src/habitatmech/curate/definition_source_label_exclusions.py
    sha256: 0c13e83fe17613e8b9f5b346d1259104172f8c1de42f911625579b903707625d
    role: context
  - path: src/habitatmech/curate/definitions.py
    sha256: decd02eea029e884ab1a8bbb51dd870edb5544906b3ddd39598147b27ce572c9
    role: context
  - path: src/habitatmech/curate/external_xrefs.py
    sha256: 8b90ec049887d3aa67e31cce7f7a04d7300421c6fedb833cc66e5d5f5f181694
    role: context
  - path: src/habitatmech/curate/gold_parent_exclusions.py
    sha256: 044d8277509a9b1f6e4f2d7ea1fb82319b41e09ffef7788738a0f4ed0d0b63af
    role: context
  - path: src/habitatmech/curate/record_annotation_corrections.py
    sha256: 15bad3d40fd95e2acc72d3ff3c74289c15fb8a1775adc523b3575c3ea8487033
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/labels.py
    sha256: eb6986c3a9c7d5a3e4651b639351f1f2d3e12d74c4bfaa92899205a1f9df0977
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: habitatmech:GOLD.a8f8c792c1
  path: data/habitats/host_associated/cecum__79e270ae.yaml
  label: Cecum
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
scope:
  description: Full field-by-field scientific assessment of this exact target at 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b.
  selection: One of the next 24 path-ordered unreviewed identifiers in the ignored-inclusive
    3208-record census. This bundle assesses one exact identifier, not a proxy sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.a8f8c792c1
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context and source witnesses do not add reviewed identifiers. Export
      conformance and individual source specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/cecum__79e270ae.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  summary: "Finished 2026-10-15T21:15:05Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cecum__79e270ae.yaml"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml
    data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml
    data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml
    data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml
    data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml
    data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml
    data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml
    data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml
    data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml
    data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml
    data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml
    data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  summary: "Finished 2026-10-15T21:15:16Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml\
    \ data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml\
    \ data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml\
    \ data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml\
    \ data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml\
    \ data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml\
    \ data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml\
    \ data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml\
    \ data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml\
    \ data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml\
    \ data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml\
    \ data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  summary: 'Finished 2026-10-15T21:15:30Z. No issues found

    824 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  summary: "Finished 2026-10-15T21:15:32Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  summary: "Finished 2026-10-15T21:16:11Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  summary: "Finished 2026-10-15T21:16:19Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  summary: "Finished 2026-10-15T21:16:50Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  summary: "Finished 2026-10-15T21:17:56Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for this target; strict check covers all 24 named targets;
    other documented checks have full-corpus scope.
- check_id: CCI
  name: Exact-baseline native QC
  status: passed
  required: true
  command: gh run view 38805081742 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  summary: Verified 2026-10-15T21:13:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38805081742
  scope_note: Unchanged committed scientific-input baseline. New output bundles are
    outside this remote execution.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/cecum__79e270ae.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: All fields, displayed taxa, source attestations and complete generated
    history read.
  snapshot_sha256: e2f9e69138fed3775e5c7cf0d20b39d3394dc7081d7b8a647ee20d55306cc76e
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strictly broader hierarchy and source evidence rules
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: All parent contributions must be strictly broader. Disease, organism, sampled
    material and habitat meanings are distinct. Optional absence is not automatically
    a defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation and category semantics
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: Source mapping endpoints are source-to-record. Reported associations do
    not imply characteristic presence. Native category and optional-field contracts
    retained.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source resolution and full generated-document reproduction
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.a8f8c792c1", "automatic": {"identifier": "habitatmech:GOLD.a8f8c792c1",
    "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding":
    true, "extra_parents": ["BTO:0000166"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "habitatmech:GOLD.a8f8c792c1", "grounding_status": "NARROW", "mapping_predicate":
    "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["BTO:0000166"],
    "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null,
    "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source projections, taxon ranking and counts
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: Frozen counts/units, maximum scores, channels, candidate pools and top
    taxon rows were traced to exact source rows. Original PREGO pair citation links
    are not retained in this projection.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 138
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"row": 138, "data": {"canonical_path": "Host-associated > Mammals >
    Digestive system > Large intestine > Cecum", "ecosystem": "Host-associated", "ecosystem_category":
    "Mammals", "ecosystem_type": "Digestive system", "ecosystem_subtype": "Large intestine",
    "specific_ecosystem": "Cecum", "leaf_label": "Cecum", "depth": "5", "gold_node_count":
    "1", "organism_count": "164", "study_count": "0", "biosample_count": "0", "total_assertions":
    "164", "gold_node_ids": "gold.ecosystem:4105"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/gold_path_biosamples.tsv
  locator: Physical TSV rows 81
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"row": 81, "data": {"canonical_path": "Host-associated > Mammals > Digestive
    system > Large intestine > Cecum", "ecosystem_path_id": "4105", "biosample_count":
    "405"}}]'
  snapshot_sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
- evidence_id: ET7
  kind: database
  reference: data/raw/gold_studies.tsv
  locator: Physical TSV rows 16,133,134,135,136,257,298,352,832,865,1333,1448,1461,2360,2620,2633,2643,2654,2696,2704,2788,2834,2912,2916,2923,3047,3108,3111,3203,3477,3770,3844,3951
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"row": 16, "data": {"study_gold_id": "Gs0045062", "path_count": "1",
    "paths": "Host-associated > Mammals > Digestive system > Large intestine > Cecum"}},
    {"row": 133, "data": {"study_gold_id": "Gs0047139", "path_count": "1", "paths":
    "Host-associated > Mammals > Digestive system > Large intestine > Cecum"}}, {"row":
    134, "data": {"study_gold_id": "Gs0047140", "path_count": "1", "paths": "Host-associated
    > Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 135, "data":
    {"study_gold_id": "Gs0047141", "path_count": "1", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 136, "data":
    {"study_gold_id": "Gs0047142", "path_count": "1", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 257, "data":
    {"study_gold_id": "Gs0056639", "path_count": "1", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 298, "data":
    {"study_gold_id": "Gs0060783", "path_count": "1", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 352, "data":
    {"study_gold_id": "Gs0063335", "path_count": "1", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 832, "data":
    {"study_gold_id": "Gs0114534", "path_count": "1", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 865, "data":
    {"study_gold_id": "Gs0114692", "path_count": "1", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 1333, "data":
    {"study_gold_id": "Gs0121394", "path_count": "1", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 1448, "data":
    {"study_gold_id": "Gs0127566", "path_count": "20", "paths": "Engineered > Artificial
    ecosystem > Sand microcosm|Engineered > Industrial production > Chemical products
    > Reagent blank|Engineered > WWTP > Wastewater|Environmental > Aquatic > Deep
    subsurface > Shale gas/oil reservoir > Produced water/Flow back|Environmental
    > Aquatic > Freshwater > Lake|Environmental > Aquatic > Freshwater > Lake > Sediment|Environmental
    > Aquatic > Marine|Environmental > Aquatic > Marine > Gulf|Environmental > Aquatic
    > Marine > Inlet|Environmental > Aquatic > Marine > Mud volcano > Sediment|Environmental
    > Aquatic > Marine > Strait|Environmental > Terrestrial > Asphalt lakes > Tar|Environmental
    > Terrestrial > Deep subsurface > Oil well|Host-associated > Mammals > Digestive
    system > Large intestine|Host-associated > Mammals > Digestive system > Large
    intestine > Cecum|Host-associated > Mammals > Digestive system > Large intestine
    > Proximal colon|Host-associated > Mammals > Digestive system > Large intestine
    > Rectum|Host-associated > Mammals > Digestive system > Small intestine|Host-associated
    > Mammals > Digestive system > Stomach|Host-associated > Mammals > Digestive system
    > Stomach > Rumen fluid"}}, {"row": 1461, "data": {"study_gold_id": "Gs0128738",
    "path_count": "1", "paths": "Host-associated > Mammals > Digestive system > Large
    intestine > Cecum"}}, {"row": 2360, "data": {"study_gold_id": "Gs0142264", "path_count":
    "1", "paths": "Host-associated > Mammals > Digestive system > Large intestine
    > Cecum"}}, {"row": 2620, "data": {"study_gold_id": "Gs0144759", "path_count":
    "1", "paths": "Host-associated > Mammals > Digestive system > Large intestine
    > Cecum"}}, {"row": 2633, "data": {"study_gold_id": "Gs0144772", "path_count":
    "1", "paths": "Host-associated > Mammals > Digestive system > Large intestine
    > Cecum"}}, {"row": 2643, "data": {"study_gold_id": "Gs0144782", "path_count":
    "1", "paths": "Host-associated > Mammals > Digestive system > Large intestine
    > Cecum"}}, {"row": 2654, "data": {"study_gold_id": "Gs0144793", "path_count":
    "2", "paths": "Host-associated > Mammals > Digestive system > Large intestine
    > Cecum|Host-associated > Mammals > Digestive system > Large intestine > Fecal"}},
    {"row": 2696, "data": {"study_gold_id": "Gs0144911", "path_count": "1", "paths":
    "Host-associated > Mammals > Digestive system > Large intestine > Cecum"}}, {"row":
    2704, "data": {"study_gold_id": "Gs0144920", "path_count": "1", "paths": "Host-associated
    > Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 2788, "data":
    {"study_gold_id": "Gs0145049", "path_count": "1", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 2834, "data":
    {"study_gold_id": "Gs0145095", "path_count": "1", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum"}}, {"row": 2912, "data":
    {"study_gold_id": "Gs0145229", "path_count": "3", "paths": "Host-associated >
    Mammals > Digestive system > Large intestine > Cecum|Host-associated > Mammals
    > Digestive system > Small intestine > Ileum|Host-associated > Mammals > Digestive
    system > Small intestine > Jejunum"}}, {"row": 2916, "data": {"study_gold_id":
    "Gs0145233", "path_count": "1", "paths": "Host-associated > Mammals > Digestive
    system > Large intestine > Cecum"}}, {"row": 2923, "data": {"study_gold_id": "Gs0145240",
    "path_count": "2", "paths": "Host-associated > Mammals > Digestive system > Large
    intestine > Cecum|Host-associated > Mammals > Digestive system > Large intestine
    > Fecal"}}, {"row": 3047, "data": {"study_gold_id": "Gs0150220", "path_count":
    "4", "paths": "Host-associated > Mammals > Digestive system > Large intestine|Host-associated
    > Mammals > Digestive system > Large intestine > Cecum|Host-associated > Mammals
    > Digestive system > Large intestine > Fecal|Host-associated > Mammals > Digestive
    system > Small intestine > Ileum"}}, {"row": 3108, "data": {"study_gold_id": "Gs0150285",
    "path_count": "1", "paths": "Host-associated > Mammals > Digestive system > Large
    intestine > Cecum"}}, {"row": 3111, "data": {"study_gold_id": "Gs0150288", "path_count":
    "1", "paths": "Host-associated > Mammals > Digestive system > Large intestine
    > Cecum"}}, {"row": 3203, "data": {"study_gold_id": "Gs0150382", "path_count":
    "2", "paths": "Host-associated > Mammals > Digestive system > Large intestine
    > Cecum|Host-associated > Mammals > Digestive system > Large intestine > Fecal"}},
    {"row": 3477, "data": {"study_gold_id": "Gs0150665", "path_count": "1", "paths":
    "Host-associated > Mammals > Digestive system > Large intestine > Cecum"}}, {"row":
    3770, "data": {"study_gold_id": "Gs0153857", "path_count": "3", "paths": "Host-associated
    > Mammals > Digestive system > Large intestine|Host-associated > Mammals > Digestive
    system > Large intestine > Cecum|Host-associated > Mammals > Digestive system
    > Large intestine > Fecal"}}, {"row": 3844, "data": {"study_gold_id": "Gs0153961",
    "path_count": "1", "paths": "Host-associated > Mammals > Digestive system > Large
    intestine > Cecum"}}, {"row": 3951, "data": {"study_gold_id": "Gs0154267", "path_count":
    "11", "paths": "Host-associated > Mammals > Digestive system > Large intestine|Host-associated
    > Mammals > Digestive system > Large intestine > Cecum|Host-associated > Mammals
    > Digestive system > Large intestine > Rectum|Host-associated > Mammals > Digestive
    system > Small intestine > Duodenum|Host-associated > Mammals > Digestive system
    > Small intestine > Ileum|Host-associated > Mammals > Digestive system > Small
    intestine > Jejunum|Host-associated > Mammals > Digestive system > Stomach > Abomasum|Host-associated
    > Mammals > Digestive system > Stomach > Omasum|Host-associated > Mammals > Digestive
    system > Stomach > Reticulum|Host-associated > Mammals > Digestive system > Stomach
    > Rumen|Host-associated > Mammals > Digestive system > Stomach > Rumen mucosa"}}]'
  snapshot_sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 168
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '[{"row": 168, "data": {"term_id": "BTO:0000166", "ontology": "BTO", "label":
    "cecum", "definition": "The first part of the large intestine, forming a dilated
    pouch into which open the ileum, colon, and appendix vermiformis.", "synonyms":
    "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/cecum.yaml
  locator: Entire immediate parent record; context only
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '{"identifier": "BTO:0000166", "label": "cecum", "definition": "The first
    part of the large intestine, forming a dilated pouch into which open the ileum,
    colon, and appendix vermiformis.", "definition_source": "BTO", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "REVIEWED",
    "synonyms": [{"synonym_text": "Cecum/Intestinal cecum", "synonym_type": "EXACT_SYNONYM",
    "source": "GOLD"}, {"synonym_text": "blind intestine", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "blind intestines", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "blind intestinous", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "blindgut", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "blindguts", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "caeca", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "caecal", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "caecum", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "caecums", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "ceca", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "cecal", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "cecums", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "intestinum caeca", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "intestinum caecal", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "intestinum caecum", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "intestinum caecums", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "intestinum crassum caeca", "synonym_type":
    "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum crassum caecal",
    "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum
    crassum caecum", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text":
    "intestinum crassum caecums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"},
    {"synonym_text": "intestinum crassum ceca", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "intestinum crassum cecal", "synonym_type":
    "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum crassum cecum",
    "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinum
    crassum cecums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats":
    ["habitatmech:GOLD.c336fb0bb7"], "source_attestations": [{"source": "GOLD", "source_id":
    "gold.ecosystem:7832", "source_label": "Cecum/Intestinal cecum", "source_path":
    "Host-associated > Mollusca > Digestive system > Hindgut > Cecum/Intestinal cecum",
    "mapping_predicate": "skos:exactMatch"}, {"source": "PREGO", "source_id": "BTO:0000166",
    "source_label": "cecum", "assertion_count": 549, "assertion_unit": "TAXON", "score":
    4.0, "evidence_channels": "annotated_genomes_isolates|environmental_samples"}],
    "characteristic_taxa": [{"taxon_id": "NCBITaxon:100176", "source": "PREGO", "taxon_label":
    "Papillibacter cinnamivorans", "score": 4.0, "rank": 1, "candidate_pool": 549},
    {"taxon_id": "NCBITaxon:100883", "source": "PREGO", "taxon_label": "Coprobacillus",
    "score": 4.0, "rank": 2, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:102106",
    "source": "PREGO", "taxon_label": "Collinsella", "score": 4.0, "rank": 3, "candidate_pool":
    549}, {"taxon_id": "NCBITaxon:102234", "source": "PREGO", "taxon_label": "Cyanobacterium",
    "score": 4.0, "rank": 4, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1032526",
    "source": "PREGO", "taxon_label": "Pedosphaera", "score": 4.0, "rank": 5, "candidate_pool":
    549}, {"taxon_id": "NCBITaxon:1091138", "source": "PREGO", "score": 4.0, "rank":
    6, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:109326", "source": "PREGO",
    "taxon_label": "Anaerovorax", "score": 4.0, "rank": 7, "candidate_pool": 549},
    {"taxon_id": "NCBITaxon:1117", "source": "PREGO", "taxon_label": "Cyanobacteriota",
    "score": 4.0, "rank": 8, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:113286",
    "source": "PREGO", "taxon_label": "Pseudoramibacter", "score": 4.0, "rank": 9,
    "candidate_pool": 549}, {"taxon_id": "NCBITaxon:117563", "source": "PREGO", "taxon_label":
    "Granulicatella", "score": 4.0, "rank": 10, "candidate_pool": 549}, {"taxon_id":
    "NCBITaxon:118747", "source": "PREGO", "taxon_label": "Bulleidia", "score": 4.0,
    "rank": 11, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:119852", "source":
    "PREGO", "taxon_label": "Oscillospira", "score": 4.0, "rank": 12, "candidate_pool":
    549}, {"taxon_id": "NCBITaxon:1249", "source": "PREGO", "taxon_label": "Weissella
    paramesenteroides", "score": 4.0, "rank": 13, "candidate_pool": 549}, {"taxon_id":
    "NCBITaxon:1253", "source": "PREGO", "taxon_label": "Pediococcus", "score": 4.0,
    "rank": 14, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1263", "source": "PREGO",
    "taxon_label": "Ruminococcus", "score": 4.0, "rank": 15, "candidate_pool": 549},
    {"taxon_id": "NCBITaxon:1265", "source": "PREGO", "taxon_label": "Ruminococcus
    flavefaciens", "score": 4.0, "rank": 16, "candidate_pool": 549}, {"taxon_id":
    "NCBITaxon:1266", "source": "PREGO", "taxon_label": "Sarcina", "score": 4.0, "rank":
    17, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1268", "source": "PREGO",
    "taxon_label": "Micrococcaceae", "score": 4.0, "rank": 18, "candidate_pool": 549},
    {"taxon_id": "NCBITaxon:1269", "source": "PREGO", "taxon_label": "Micrococcus",
    "score": 4.0, "rank": 19, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1279",
    "source": "PREGO", "taxon_label": "Staphylococcus", "score": 4.0, "rank": 20,
    "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1280", "source": "PREGO", "taxon_label":
    "Staphylococcus aureus", "score": 4.0, "rank": 21, "candidate_pool": 549}, {"taxon_id":
    "NCBITaxon:1282", "source": "PREGO", "taxon_label": "Staphylococcus epidermidis",
    "score": 4.0, "rank": 22, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:128827",
    "source": "PREGO", "taxon_label": "Erysipelotrichaceae", "score": 4.0, "rank":
    23, "candidate_pool": 549}, {"taxon_id": "NCBITaxon:1296", "source": "PREGO",
    "taxon_label": "Mammaliicoccus sciuri", "score": 4.0, "rank": 24, "candidate_pool":
    549}, {"taxon_id": "NCBITaxon:1300", "source": "PREGO", "taxon_label": "Streptococcaceae",
    "score": 4.0, "rank": 25, "candidate_pool": 549}], "curation_history": [{"timestamp":
    "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes":
    "Grounded to BTO:0000166 ''cecum'' (EXACT). Slash alternative naming one structure.
    Path: Host-associated > Mollusca > Digestive system > Hindgut > Cecum/Intest (source
    concept habitatmech:GOLD.37d9cdc188)"}, {"timestamp": "2026-08-13T00:00:00Z",
    "curator": "claude-opus-5", "action": "REVIEW", "changes": "Reviewed and endorsed
    the seeder''s own resolution. Multi-source review pass: this record is attested
    by more than one independent vocabulary, and this source''s label or path was
    read against the record''s ontology term to check the merge is right. It agrees.
    Source concepts in the same pass whose labels did not agree were re-decided rather
    than endorsed; see the pass''s other decisions of the same date. (source concept
    habitatmech:PREGO.35b3d0b858)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator":
    "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from
    data/raw/ inventories; attested by GOLD, PREGO. Grounding: EXACT."}]}'
  snapshot_sha256: 623da28718fc205e72e52b35719ed08693a1d8b5850f49df7b38ebff5438815c
- evidence_id: EP10
  kind: record_content
  reference: data/habitats/host_associated/large_intestine__834e53c8.yaml
  locator: Entire immediate parent record; context only
  accessed_at: '2026-10-15T21:25:54Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.6bda0871e2", "label": "Large intestine",
    "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status":
    "SEEDED", "parent_habitats": ["UBERON:0000059", "habitatmech:GOLD.c8e85f3c84"],
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:3660",
    "source_label": "Large intestine", "source_path": "Host-associated > Mammals >
    Digestive system > Large intestine", "mapping_predicate": "skos:narrowMatch",
    "assertion_count": 37, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem
    node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by GOLD. Grounding: NARROW."}]}'
  snapshot_sha256: 2c086c4115cc2a0b04df48cb9b989c051c96d6625a64dbe26cef1ac90e6d4d15
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000166/graph
  locator: BTO_0000166-graph.json
  accessed_at: '2026-10-15T21:13:52Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000166",
    "target": "http://purl.obolibrary.org/obo/BTO_0000706", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000166",
    "target": "http://purl.obolibrary.org/obo/BTO_0002273", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 5a3b1f1eca1553a995153a1970d6cdf6e439879e0efa6f51d18c3d534a131cd9
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000166
  locator: BTO_0000166.json
  accessed_at: '2026-10-15T21:13:51Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0000166",
    "label": "cecum", "is_obsolete": false, "description": ["The first part of the
    large intestine, forming a dilated pouch into which open the ileum, colon, and
    appendix vermiformis."]}'
  snapshot_sha256: a1996ad92a59beb60230672c36476edd1ef43af133fc7a65b57dc75b2eb965b8
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059/graph
  locator: UBERON_0000059-graph.json
  accessed_at: '2026-10-15T21:14:03Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000059",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059",
    "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000160", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004907", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 8e11a36702591e8fdbb38beb59c7ca21416d18f4a524ccdd7fb246e8d82d799c
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059
  locator: UBERON_0000059.json
  accessed_at: '2026-10-15T21:14:02Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0000059",
    "label": "large intestine", "is_obsolete": false, "description": ["A subdivision
    of the digestive tract that connects the small intestine to the cloaca or anus.
    Lacks or has few villi[Kardong]."]}'
  snapshot_sha256: d43e203ec23dc43e60bf4f3eeef91235a695dc997d4784a65919688f223aaba8
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.a8f8c792c1 -e Cecum -e
    cecum__79e270ae -e habitatmech:GOLD.a8f8c792c1 curation history research reports
    data/raw build reviews
  accessed_at: '2026-10-15T21:13:37Z'
  support: context_only
  summary: Exact source rows were parsed separately; no formal structured target predecessor
    was found. Broad label matches were treated as leads, not all read.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    hidden/ignored content included, with structured review.yaml parsing independent
    of gitignore.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, category and ancestry
  outcome: concern
  summary: The mammalian source can retain generic BTO cecum as its anatomical genus,
    but not whole mammalian large intestine as an is-a parent. Its 164 ORGANISM assertions
    reproduce the raw source. The BTO parent record has a separately identified molluscan
    merger defect; that does not make the mammalian-to-BTO class relation itself false.
    The narrow-mapping endpoint is independently inconsistent.
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EP9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  dimensions:
  - name: native_status
    value: NARROW/SEEDED
    definition: Generated grounding and curation status, distinct from scientific
      review verdict.
    evidence_ids:
    - E1
    - ESEED
- assessment_id: A2
  area: quantity
  topic: Frozen source counts, units, ranks, channels and pool
  outcome: supported
  summary: 'Exact source rows reproduce all emitted counts and displayed taxon rows.
    [{"source": "GOLD", "count": 164, "unit": "ORGANISM"}]. Zero GOLD counts are omitted;
    supplemental biosamples and study memberships are not added to tree ORGANISM counts.'
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  dimensions:
  - name: source_assertion_units
    value: '[{"source": "GOLD", "count": 164, "unit": "ORGANISM"}]'
    definition: Frozen counts with noninterchangeable source units; zero GOLD counts
      are verified in raw rows.
    evidence_ids:
    - E1
    - EEXTRACT
- assessment_id: A3
  area: evidence
  topic: Biological support and bounded uncertainty
  outcome: supported
  summary: The mammalian source can retain generic BTO cecum as its anatomical genus,
    but not whole mammalian large intestine as an is-a parent. Its 164 ORGANISM assertions
    reproduce the raw source. The BTO parent record has a separately identified molluscan
    merger defect; that does not make the mammalian-to-BTO class relation itself false.
    The narrow-mapping endpoint is independently inconsistent.
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EP9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
- assessment_id: A4
  area: completeness
  topic: Native status, optional fields and mechanisms
  outcome: supported
  summary: Executed resolution reproduces NARROW/SEEDED. No target environmental parameters,
    causal graphs, discussions, datasets or is_characteristic=true claims are present.
    Optional absence and SEEDED status alone do not warrant findings; parent mechanisms
    are not inherited.
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Deterministic validity and source fidelity
  outcome: supported
  summary: Ordinary/strict target validation, 824 histories, source provenance, exact
    3208-record reproduction, 32 causal overlays, 110 term requests, configured labels
    and exact-base remote QC passed. These are not substitutes for scientific identity
    assessment.
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: cecum--79e270ae-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Containing anatomy is emitted as a broader habitat class
  description: Exclude only the exact GOLD source-path/expected-parent contribution
    habitatmech:GOLD.6bda0871e2. The mammalian source can retain generic BTO cecum
    as its anatomical genus, but not whole mammalian large intestine as an is-a parent.
    Its 164 ORGANISM assertions reproduce the raw source. The BTO parent record has
    a separately identified molluscan merger defect; that does not make the mammalian-to-BTO
    class relation itself false. The narrow-mapping endpoint is independently inconsistent.
    Preserve independent valid ontology genera and raw source paths.
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EP9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: cecum--79e270ae-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow predicate uses an undeclared ontology-parent endpoint
  description: 'Resolution retains the GOLD source mint but emits narrowMatch relative
    to its ontology parent. SourceAttestation declares a source-to-record relation.
    Reconcile producer, schema and downstream consumers under #1398 without merging
    host-specific concepts or blindly reversing predicates. This is not a claim that
    SKOS prohibits self-links and does not certify SSSOM/KGX conformance.'
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EP9
  - EP10
  - EX1
  - EX2
  - EX3
  - EX4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Exclude only the exact GOLD source-path/expected-parent contribution
    habitatmech:GOLD.6bda0871e2. The mammalian source can retain generic BTO cecum
    as its anatomical genus, but not whole mammalian large intestine as an is-a parent.
    Its 164 ORGANISM assertions reproduce the raw source. The BTO parent record has
    a separately identified molluscan merger defect; that does not make the mammalian-to-BTO
    class relation itself false. The narrow-mapping endpoint is independently inconsistent.
    Preserve independent valid ontology genera and raw source paths. No repair is
    performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact claim, preserving independent valid genera, raw provenance and
    source counts/units. Change native status or mappings only when supported by the
    authorized ITEM assessment; never decrement source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.a8f8c792c1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Resolution retains the GOLD source mint but emits narrowMatch relative
    to its ontology parent. SourceAttestation declares a source-to-record relation.
    Reconcile producer, schema and downstream consumers under #1398 without merging
    host-specific concepts or blindly reversing predicates. This is not a claim that
    SKOS prohibits self-links and does not certify SSSOM/KGX conformance. No repair
    is performed by this review.'
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact claim, preserving independent valid genera, raw provenance and
    source counts/units. Change native status or mappings only when supported by the
    authorized ITEM assessment; never decrement source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Individual source specimens and all original pair-level citations have not been
  independently reconstructed. Counts, ranks and source scores are not prevalence
  or characteristic presence.
- Configured label validation skips 2061 no-adapter pairs. Displayed TaxIds were separately
  checked against current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged scientific input
  base, not a new local full-QC execution. These new bundles require their own post-save
  archive check.
- 'iModulonDB is not applicable to target claims: no gene, regulator, expression module
  or causal mechanism is asserted. Papers mentioning genes are used only for source
  context. No paid research was used.'
notes:
- All captured local inputs were compared with both current bytes and exact Git-base
  blobs. The review explicitly assesses that committed revision.
- Ignored-inclusive archive search found no previous structured observation targeting
  this identifier. Legacy prose is a lead, not formal predecessor lineage or automatic
  closure.
- 'Read-only review: no curation, generation, native status/history promotion or GitHub
  mutation.'
tags:
- individual-scientific-review
- host-associated
```
