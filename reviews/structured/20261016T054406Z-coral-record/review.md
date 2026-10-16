# Record review: Coral (habitatmech:GOLD.a12eda25e9)

- Review: 20261016T054406Z-coral-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T05:14:08Z
- Finished UTC: 2026-10-16T05:44:06Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The full Invertebrates &gt; Cnidaria &gt; Coral source supports a coral-associated environment narrower than cnidarian-associated environment, not a coral-reef setting or fish identity. The ITEM grounding-as-parent decision is coherent. Preserve 382 ORGANISM assertions separately from 267 supplemental biosamples and study memberships; the parent record is context, not newly reviewed coverage. Only the narrow mapping endpoint defect is confirmed here.

## Scope And Provenance

Full field-by-field assessment of this one resolved generated target.

Selection: One of the next 24 unreviewed targets in deterministic path order from the ignored-inclusive 3209-record census. This bundle is not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 13cddc722250dcad4327e5f9fad0a12fe7c08268.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.a12eda25e9 | data/habitats/host_associated/coral.yaml | generated | Coral |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.a12eda25e9 | Finished 2026-10-16T05:16:36Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/coral.yaml |
| validate-strict | passed | True | habitatmech:GOLD.a12eda25e9 | Finished 2026-10-16T05:17:09Z. uv run python scripts/validate_strict.py data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.a12eda25e9 | Finished 2026-10-16T05:17:16Z. No issues found<br>834 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.a12eda25e9 | Finished 2026-10-16T05:17:16Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.a12eda25e9 | Finished 2026-10-16T05:17:32Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.a12eda25e9 | Finished 2026-10-16T05:17:36Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.a12eda25e9 | Finished 2026-10-16T05:17:53Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.a12eda25e9 | Finished 2026-10-16T05:18:37Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted native QC | passed | True | habitatmech:GOLD.a12eda25e9 | Verified 2026-10-16T05:19:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38852350960 |
| Candidate-pool correspondence | passed | False | habitatmech:GOLD.a12eda25e9 | Finished 2026-10-16T05:42:35Z. All 67 displayed candidate pools equal exact source taxon totals. |
| Standalone citation validation applicability | not_applicable | False | habitatmech:GOLD.a12eda25e9 | No standalone citation validator is documented for these generated targets without evidence objects. Current authorities verify stable references; full-corpus causal validation ran. |

## Scientific And Domain Assessments

### Identity, grounding, aliases and strict hierarchy

identity: concern. Targets: habitatmech:GOLD.a12eda25e9.

The full Invertebrates &gt; Cnidaria &gt; Coral source supports a coral-associated environment narrower than cnidarian-associated environment, not a coral-reef setting or fish identity. The ITEM grounding-as-parent decision is coherent. Preserve 382 ORGANISM assertions separately from 267 supplemental biosamples and study memberships; the parent record is context, not newly reviewed coverage. Only the narrow mapping endpoint defect is confirmed here.

### Counts, units, taxon ranks, scores and candidate pools

quantity: supported. Targets: habitatmech:GOLD.a12eda25e9.

Exact source rows reproduce emitted counts/units and displayed ranks/scores/pools. Zero tree counts are omitted; supplemental biosamples, study memberships and triads are nonadditive. {"assertions": [{"source": "GOLD", "count": 382, "unit": "ORGANISM", "row": {"row": 81, "data": {"canonical_path": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral", "ecosystem": "Host-associated", "ecosystem_category": "Invertebrates", "ecosystem_type": "Cnidaria", "ecosystem_subtype": "Coral", "specific_ecosystem": "", "leaf_label": "Coral", "depth": "4", "gold_node_count": "2", "organism_count": "382", "study_count": "0", "biosample_count": "0", "total_assertions": "382", "gold_node_ids": "gold.ecosystem:3643&#124;gold.ecosystem:4088"}}}], "taxa": []}

### Association support and source limits

evidence: supported. Targets: habitatmech:GOLD.a12eda25e9.

The full Invertebrates &gt; Cnidaria &gt; Coral source supports a coral-associated environment narrower than cnidarian-associated environment, not a coral-reef setting or fish identity. The ITEM grounding-as-parent decision is coherent. Preserve 382 ORGANISM assertions separately from 267 supplemental biosamples and study memberships; the parent record is context, not newly reviewed coverage. Only the narrow mapping endpoint defect is confirmed here. Each cited source supports only its stated scope; original source pairs were not exhaustively reconstructed.

### Native lifecycle and optional content

completeness: supported. Targets: habitatmech:GOLD.a12eda25e9.

Executed routes reproduce NARROW/REVIEWED. Required fields are present; absent optional parameters, causal graphs, discussions and datasets are not fabricated. No scientific status promotion follows from this review.

### Native gates and exact reproduction

schema: supported. Targets: habitatmech:GOLD.a12eda25e9.

31 baseline commands passed: individual schemas, 24-target strict validation, 834 histories, provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured labels. Exact-base hosted QC passed; deterministic validity is not scientific approval.

## Findings

### F1: Mapping uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: coral-mapping-endpoint-contract.

The executed narrower-than-leaf route retains the source mint but emits narrowMatch relative to an ontology parent, whereas the schema endpoint is the record identifier. Reconcile producer, schema and consumers under #1398. This is not a formal SKOS self-link prohibition or a request for a blind predicate reversal.

## Recommended Actions And Acceptance Checks

### ACT1

The executed narrower-than-leaf route retains the source mint but emits narrowMatch relative to an ontology parent, whereas the schema endpoint is the record identifier. Reconcile producer, schema and consumers under #1398. This is not a formal SKOS self-link prohibition or a request for a blind predicate reversal. Proposed work only; no repair or status promotion is performed by this review.

- Regress the exact target claim and preserve valid genera, identifiers, source counts/units and taxon associations. Recover original evidence before deleting a provisional pair; do not decrement frozen totals by hand.
- Record authorized curation history; require schema, strict, provenance, history, label, corpus, site and full QC gates.
- Save an immutable successor with the same issue key and exact predecessor finding identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/coral.yaml; Entire generated target YAML | supports | All fields, source attestations, displayed taxa, aliases and generated history read. |
| ERULE | docs/CURATION.md; Identity, strict parents and evidence scope | supports | All parent contributions must be strictly broader; source context, host, anatomy and diagnosis are distinct. Missing optional content or ITEM status alone is not a defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and native statuses | supports | Mapping contract compares source concept to record identifier; source-is-record omits the predicate. Native count units and status gates retained. |
| ESEED | src/habitatmech/seed.py; Executed source routes and target reproduction | supports | [{"mint": "habitatmech:GOLD.a12eda25e9", "automatic": {"identifier": "FOODON:03412872", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_synonym", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.a12eda25e9", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["ENVO:01001179"], "extra_xrefs": [], "route": "curated_ground_as_parent_from_gold_leaf_synonym", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.a12eda25e9", "decision": "GROUND_AS_PARENT", "object_id": "ENVO:01001179", "object_label": "cnidarian-associated environment", "grounding_status": "NARROW", "curator": "claude-opus-5", "date": "2026-08-14", "notes": "Grounding-cohort review (#62): was FOODON:03412872 'barramundi' \u2014 a FISH, matched because barramundi carries 'coral' as a synonym (its Bengali name). GOLD's path is Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral, so the habitat is a coral animal. Kept as a narrower kind of cnidarian-associated environment rather than grounded to it, because Host-associated &gt; Cnidaria is the shallower path entitled to that term.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; PREGO source projections | supports | Compact per-habitat tables preserve associations but do not retain original pair citations/dictionary provenance. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 81 | supports | [{"row": 81, "data": {"canonical_path": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral", "ecosystem": "Host-associated", "ecosystem_category": "Invertebrates", "ecosystem_type": "Cnidaria", "ecosystem_subtype": "Coral", "specific_ecosystem": "", "leaf_label": "Coral", "depth": "4", "gold_node_count": "2", "organism_count": "382", "study_count": "0", "biosample_count": "0", "total_assertions": "382", "gold_node_ids": "gold.ecosystem:3643&#124;gold.ecosystem:4088"}}] |
| ET6 | data/raw/gold_path_biosamples.tsv; Physical TSV rows 113 | supports | [{"row": 113, "data": {"canonical_path": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral", "ecosystem_path_id": "4088", "biosample_count": "267"}}] |
| ET7 | data/raw/gold_studies.tsv; Physical TSV rows 951,1096,2269,2271,2336,2363,2527,2646,2790,2812,2815,2847,2882,3001,3231,4393 | supports | [{"row": 951, "data": {"study_gold_id": "Gs0117432", "path_count": "2", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria&#124;Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 1096, "data": {"study_gold_id": "Gs0118447", "path_count": "1", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2269, "data": {"study_gold_id": "Gs0141911", "path_count": "1", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2271, "data": {"study_gold_id": "Gs0141913", "path_count": "2", "paths": "Environmental &gt; Aquatic &gt; Marine &gt; Intertidal zone &gt; Coral reef&#124;Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2336, "data": {"study_gold_id": "Gs0142151", "path_count": "3", "paths": "Environmental &gt; Aquatic &gt; Marine &gt; Oceanic&#124;Environmental &gt; Aquatic &gt; Marine &gt; Oceanic &gt; Sediment&#124;Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2363, "data": {"study_gold_id": "Gs0142267", "path_count": "2", "paths": "Environmental &gt; Aquatic &gt; Marine &gt; Oceanic&#124;Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2527, "data": {"study_gold_id": "Gs0144622", "path_count": "1", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2646, "data": {"study_gold_id": "Gs0144785", "path_count": "1", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2790, "data": {"study_gold_id": "Gs0145051", "path_count": "1", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2812, "data": {"study_gold_id": "Gs0145073", "path_count": "1", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2815, "data": {"study_gold_id": "Gs0145076", "path_count": "1", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2847, "data": {"study_gold_id": "Gs0145108", "path_count": "1", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 2882, "data": {"study_gold_id": "Gs0145193", "path_count": "1", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 3001, "data": {"study_gold_id": "Gs0149384", "path_count": "1", "paths": "Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 3231, "data": {"study_gold_id": "Gs0150411", "path_count": "2", "paths": "Environmental &gt; Aquatic &gt; Marine&#124;Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}, {"row": 4393, "data": {"study_gold_id": "Gs0160789", "path_count": "2", "paths": "Environmental &gt; Aquatic &gt; Marine &gt; Benthic zone &gt; Sediment&#124;Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral"}}] |
| ET8 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 6996 | supports | [{"row": 6996, "data": {"subject": "ENVO:01001179", "predicate": "rdfs:subClassOf", "object": "ENVO:01001002"}}] |
| ET9 | data/raw/ontology_terms.tsv; Physical TSV rows 8667 | supports | [{"row": 8667, "data": {"term_id": "ENVO:01001179", "ontology": "ENVO", "label": "cnidarian-associated environment", "definition": "An environmental system determined by a cnidarian or part of a cnidarian.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET10 | curation/decisions.tsv; Physical TSV rows 1572 | supports | [{"row": 1572, "data": {"identifier": "habitatmech:GOLD.a12eda25e9", "decision": "GROUND_AS_PARENT", "object_id": "ENVO:01001179", "object_label": "cnidarian-associated environment", "grounding_status": "NARROW", "curator": "claude-opus-5", "date": "2026-08-14", "notes": "Grounding-cohort review (#62): was FOODON:03412872 'barramundi' \u2014 a FISH, matched because barramundi carries 'coral' as a synonym (its Bengali name). GOLD's path is Host-associated &gt; Invertebrates &gt; Cnidaria &gt; Coral, so the habitat is a coral animal. Kept as a narrower kind of cnidarian-associated environment rather than grounded to it, because Host-associated &gt; Cnidaria is the shallower path entitled to that term.", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP11 | data/habitats/host_associated/cnidarian_associated_environment.yaml; Full immediate parent record, context only | supports | {"identifier": "ENVO:01001179", "label": "cnidarian-associated environment", "definition": "An environmental system determined by a cnidarian or part of a cnidarian.", "definition_source": "ENVO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Cnidaria", "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "Cnidaria-Corals", "synonym_type": "EXACT_SYNONYM", "source": "BacDive"}], "parent_habitats": ["ENVO:01001000", "ENVO:01001002", "habitatmech:GOLD.4d792ac724"], "source_attestations": [{"source": "BACDIVE", "source_id": "bacdive.isolation_source:cnidaria-corals", "source_label": "Cnidaria-Corals", "mapping_predicate": "skos:exactMatch", "assertion_count": 75, "assertion_unit": "STRAIN"}, {"source": "GOLD", "source_id": "gold.ecosystem:3383", "source_label": "Cnidaria", "source_path": "Host-associated &gt; Cnidaria", "mapping_predicate": "skos:exactMatch", "assertion_count": 95, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "GOLD", "source_id": "gold.ecosystem:3564", "source_label": "Cnidaria", "source_path": "Host-associated &gt; Invertebrates &gt; Cnidaria", "mapping_predicate": "skos:exactMatch", "assertion_count": 102, "assertion_unit": "ORGANISM", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:1449351", "source": "BACDIVE", "taxon_label": "Roseivivax isoporae LMG 25204", "association_count": 2, "rank": 1, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:560080", "source": "BACDIVE", "taxon_label": "Shewanella corallii", "association_count": 2, "rank": 2, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1027273", "source": "BACDIVE", "taxon_label": "Endozoicomonas montiporae", "association_count": 1, "rank": 3, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1048357", "source": "BACDIVE", "taxon_label": "Nocardiopsis coralliicola", "association_count": 1, "rank": 4, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1069963", "source": "BACDIVE", "taxon_label": "Janibacter alkaliphilus", "association_count": 1, "rank": 5, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1074311", "source": "BACDIVE", "taxon_label": "Vibrio alfacsensis", "association_count": 1, "rank": 6, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1120968", "source": "BACDIVE", "taxon_label": "Algoriphagus vanfongensis DSM 17529", "association_count": 1, "rank": 7, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1120983", "source": "BACDIVE", "taxon_label": "Amorphus coralli DSM 19760", "association_count": 1, "rank": 8, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1121027", "source": "BACDIVE", "taxon_label": "Aurantimonas coralicida DSM 14790", "association_count": 1, "rank": 9, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1173995", "source": "BACDIVE", "taxon_label": "Parvularcula dongshanensis", "association_count": 1, "rank": 10, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1216969", "source": "BACDIVE", "taxon_label": "Janibacter corallicola NBRC 107790", "association_count": 1, "rank": 11, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1224163", "source": "BACDIVE", "taxon_label": "Corynebacterium maris DSM 45190", "association_count": 1, "rank": 12, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1234143", "source": "BACDIVE", "taxon_label": "Endozoicomonas euniceicola", "association_count": 1, "rank": 13, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1234144", "source": "BACDIVE", "taxon_label": "Endozoicomonas gorgoniicola", "association_count": 1, "rank": 14, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1280004", "source": "BACDIVE", "taxon_label": "Vibrio owensii LMG 25430", "association_count": 1, "rank": 15, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1342794", "source": "BACDIVE", "taxon_label": "Photobacterium sanctipauli", "association_count": 1, "rank": 16, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1342818", "source": "BACDIVE", "taxon_label": "Vibrio madracius", "association_count": 1, "rank": 17, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1348114", "source": "BACDIVE", "taxon_label": "Pseudoalteromonas piratica", "association_count": 1, "rank": 18, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1385512", "source": "BACDIVE", "taxon_label": "Pontibacillus litoralis JSM 072002", "association_count": 1, "rank": 19, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1401264", "source": "BACDIVE", "taxon_label": "Prauserella coralliicola", "association_count": 1, "rank": 20, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:141693", "source": "BACDIVE", "taxon_label": "Nocardiopsis kunsanensis", "association_count": 1, "rank": 21, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1452538", "source": "BACDIVE", "taxon_label": "Microbacterium aureliae", "association_count": 1, "rank": 22, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1453497", "source": "BACDIVE", "taxon_label": "Kosmotoga arenicorallina S304", "association_count": 1, "rank": 23, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1479025", "source": "BACDIVE", "taxon_label": "Myceligenerans cantabricum", "association_count": 1, "rank": 24, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1481923", "source": "BACDIVE", "taxon_label": "Vibrio astriarenae", "association_count": 1, "rank": 25, "candidate_pool": 73}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by BACDIVE, GOLD. Grounding: EXACT."}, {"timestamp": "2026-08-17T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to ENVO:01001179 'cnidarian-associated environment' (EXACT). Adversarial review of #120 (#123): #114 correctly reversed this from NOT_APPLICABLE \u2014 a cnidarian host is a habitat \u2014 but overshot by making it a term-request candidate. The term already exists: ENVO:01001179 'cnidarian-associated environment', 'an environmental system determined by a cnidarian or part of a cnidarian', present in the vendored slice with that exact label. Requesting it would have been requesting a duplicate. Grounded EXACT. Note that GROUND does not carry an xref the way NOT_APPLICABLE and CONFIRM_UNGROUNDED do, so the taxon link (mesh:D003063 / mesh:D037421) is not retained on the record; the upstream mapping remains in data/raw/. Found by the deep research run in #120, which is the point of running it. (source concept habitatmech:BACDIVE.ef2153283d)"}, {"timestamp": "2026-08-17T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to ENVO:01001179 'cnidarian-associated environment' (EXACT). Adversarial review of #120 (#123): #114 correctly reversed this from NOT_APPLICABLE \u2014 a cnidarian host is a habitat \u2014 but overshot by making it a term-request candidate. The term already exists: ENVO:01001179 'cnidarian-associated environment', 'an environmental system determined by a cnidarian or part of a cnidarian', present in the vendored slice with that exact label. Requesting it would have been requesting a duplicate. Grounded EXACT. Note that GROUND does not carry an xref the way NOT_APPLICABLE and CONFIRM_UNGROUNDED do, so the taxon link (mesh:D003063 / mesh:D037421) is not retained on the record; the upstream mapping remains in data/raw/. Found by the deep research run in #120, which is the point of running it. (source concept habitatmech:GOLD.00086e0958)"}, {"timestamp": "2026-08-17T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to ENVO:01001179 'cnidarian-associated environment' (EXACT). Adversarial review of #120 (#123): #114 correctly reversed this from NOT_APPLICABLE \u2014 a cnidarian host is a habitat \u2014 but overshot by making it a term-request candidate. The term already exists: ENVO:01001179 'cnidarian-associated environment', 'an environmental system determined by a cnidarian or part of a cnidarian', present in the vendored slice with that exact label. Requesting it would have been requesting a duplicate. Grounded EXACT. Note that GROUND does not carry an xref the way NOT_APPLICABLE and CONFIRM_UNGROUNDED do, so the taxon link (mesh:D003063 / mesh:D037421) is not retained on the record; the upstream mapping remains in data/raw/. Found by the deep research run in #120, which is the point of running it. (source concept habitatmech:GOLD.e3fede2aea)"}]} |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph; ENVO_01001000-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000; ENVO_01001000.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "ENVO:01001000", "label": "environmental system determined by an organism", "is_obsolete": false, "description": ["An environmental system which is determined by a living organism."], "obo_synonym": null} |
| EX14 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph; ENVO_01001002-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX15 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002; ENVO_01001002.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "ENVO:01001002", "label": "animal-associated environment", "is_obsolete": false, "description": ["An environmental system determined by an animal."], "obo_synonym": null} |
| EX16 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179/graph; ENVO_01001179-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001179", "target": "http://purl.obolibrary.org/obo/ENVO_01001002", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX17 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179; ENVO_01001179.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "ENVO:01001179", "label": "cnidarian-associated environment", "is_obsolete": false, "description": ["An environmental system determined by a cnidarian or part of a cnidarian."], "obo_synonym": null} |
| ESEARCH | Local source and review corpus; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.a12eda25e9 -e Coral -e coral -e habitatmech:GOLD.a12eda25e9 curation history research reports data/raw build reviews | context_only | Exact source keys and structured archive parsed independently; broad name hits are leads, not all inspected. No formal target predecessor. |

## Limits And Additional Notes

- Original specimen-level evidence and all pair-level citations were not exhaustively reconstructed. Native association counts, taxon ranks and scores do not establish prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs. Exact target TaxIds were separately resolved; frozen taxon labels are not universally current.
- Exact-base hosted QC covers unchanged scientific inputs, not a fresh local full-QC execution or these new review outputs. Native validate/save and subsequent archive/final-head gates are separate.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. No new causal mechanism is imported.
- All captured local input hashes were independently checked against exact base 13cddc722250dcad4327e5f9fad0a12fe7c08268.
- This baseline observation changes no scientific input. Separately authorized PR remediation follows; no status promotion is conferred by review validation.
- Ignored-inclusive structured archive traversal found no formal previous target review. Legacy reports are context, not predecessor lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T054406Z-coral-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Coral (habitatmech:GOLD.a12eda25e9)'
started_at: '2026-10-16T05:14:08Z'
finished_at: '2026-10-16T05:44:06Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Parent agent integrates evidence and separate-agent source/hierarchy
    cross-checks; not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The full Invertebrates > Cnidaria > Coral source supports a coral-associated
  environment narrower than cnidarian-associated environment, not a coral-reef setting
  or fish identity. The ITEM grounding-as-parent decision is coherent. Preserve 382
  ORGANISM assertions separately from 267 supplemental biosamples and study memberships;
  the parent record is context, not newly reviewed coverage. Only the narrow mapping
  endpoint defect is confirmed here.
source:
  git_revision: 13cddc722250dcad4327e5f9fad0a12fe7c08268
  state: working_tree
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
    sha256: 5d3af0a0505a61cda5e088e2c4b7922b740b7423fbca957d49aa8261b5584b37
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 29671974bab045cad2620da3ad89d176f8a2f5ca2612ad3c8761d82fd3f1ea81
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
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
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: 747e6a5612dc0b7ed881b9fb323fd57ab3c75794d9ee5ebb9d59b2be57dbf8cd
    role: context
  - path: data/habitats/host_associated/cnidarian_associated_environment.yaml
    sha256: 89a86d0b96bbc29b7bc9b40caceaf294637cd8c380499ea41160cf4e0062524a
    role: context
  - path: data/habitats/host_associated/coral.yaml
    sha256: 0936cddd0a5b0d5689ee9dd0916ba264240da73f9e1ea75015caeed4de28e0d3
    role: target
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
- target_id: habitatmech:GOLD.a12eda25e9
  path: data/habitats/host_associated/coral.yaml
  label: Coral
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
  description: Full field-by-field assessment of this one resolved generated target.
  selection: One of the next 24 unreviewed targets in deterministic path order from
    the ignored-inclusive 3209-record census. This bundle is not a proxy sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.a12eda25e9
  exclusions:
  - target: Other records, original specimens and SSSOM/KGX products
    reason: Parents are contextual evidence, not additional review coverage; original
      specimens and exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/coral.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: "Finished 2026-10-16T05:16:36Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/coral.yaml"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml
    data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml
    data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml
    data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml
    data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml
    data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml
    data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml
    data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml
    data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml
    data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml
    data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml
    data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: "Finished 2026-10-16T05:17:09Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml\
    \ data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml\
    \ data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml\
    \ data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml\
    \ data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml\
    \ data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml\
    \ data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml\
    \ data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml\
    \ data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml\
    \ data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml\
    \ data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml\
    \ data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: 'Finished 2026-10-16T05:17:16Z. No issues found

    834 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: "Finished 2026-10-16T05:17:16Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: "Finished 2026-10-16T05:17:32Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: "Finished 2026-10-16T05:17:36Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: "Finished 2026-10-16T05:17:53Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: "Finished 2026-10-16T05:18:37Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict covers 24 targets; other native commands retain
    full-corpus scope.
- check_id: CCI
  name: Exact-base hosted native QC
  status: passed
  required: true
  command: gh run view 38852350960 --repo CultureBotAI/HabitatMech --json headSha,conclusion,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: Verified 2026-10-16T05:19:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38852350960
  scope_note: Unchanged scientific-input base; not new review-output validation.
- check_id: CPOOL
  name: Candidate-pool correspondence
  status: passed
  required: false
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python3
    /private/tmp/habitatmech-review-cr-author.py pool_check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: Finished 2026-10-16T05:42:35Z. All 67 displayed candidate pools equal exact
    source taxon totals.
  scope_note: Supplemental exact source-total check, not a replacement for native
    validators or scientific evidence.
- check_id: CREF
  name: Standalone citation validation applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  summary: No standalone citation validator is documented for these generated targets
    without evidence objects. Current authorities verify stable references; full-corpus
    causal validation ran.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/coral.yaml
  locator: Entire generated target YAML
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: All fields, source attestations, displayed taxa, aliases and generated
    history read.
  snapshot_sha256: 0936cddd0a5b0d5689ee9dd0916ba264240da73f9e1ea75015caeed4de28e0d3
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strict parents and evidence scope
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: All parent contributions must be strictly broader; source context, host,
    anatomy and diagnosis are distinct. Missing optional content or ITEM status alone
    is not a defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and native statuses
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: Mapping contract compares source concept to record identifier; source-is-record
    omits the predicate. Native count units and status gates retained.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source routes and target reproduction
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.a12eda25e9", "automatic": {"identifier": "FOODON:03412872",
    "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_synonym", "category":
    null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.a12eda25e9",
    "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding":
    true, "extra_parents": ["ENVO:01001179"], "extra_xrefs": [], "route": "curated_ground_as_parent_from_gold_leaf_synonym",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.a12eda25e9",
    "decision": "GROUND_AS_PARENT", "object_id": "ENVO:01001179", "object_label":
    "cnidarian-associated environment", "grounding_status": "NARROW", "curator": "claude-opus-5",
    "date": "2026-08-14", "notes": "Grounding-cohort review (#62): was FOODON:03412872
    ''barramundi'' \u2014 a FISH, matched because barramundi carries ''coral'' as
    a synonym (its Bengali name). GOLD''s path is Host-associated > Invertebrates
    > Cnidaria > Coral, so the habitat is a coral animal. Kept as a narrower kind
    of cnidarian-associated environment rather than grounded to it, because Host-associated
    > Cnidaria is the shallower path entitled to that term.", "review_depth": "ITEM",
    "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: PREGO source projections
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: Compact per-habitat tables preserve associations but do not retain original
    pair citations/dictionary provenance.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 81
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: '[{"row": 81, "data": {"canonical_path": "Host-associated > Invertebrates
    > Cnidaria > Coral", "ecosystem": "Host-associated", "ecosystem_category": "Invertebrates",
    "ecosystem_type": "Cnidaria", "ecosystem_subtype": "Coral", "specific_ecosystem":
    "", "leaf_label": "Coral", "depth": "4", "gold_node_count": "2", "organism_count":
    "382", "study_count": "0", "biosample_count": "0", "total_assertions": "382",
    "gold_node_ids": "gold.ecosystem:3643|gold.ecosystem:4088"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/gold_path_biosamples.tsv
  locator: Physical TSV rows 113
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: '[{"row": 113, "data": {"canonical_path": "Host-associated > Invertebrates
    > Cnidaria > Coral", "ecosystem_path_id": "4088", "biosample_count": "267"}}]'
  snapshot_sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
- evidence_id: ET7
  kind: database
  reference: data/raw/gold_studies.tsv
  locator: Physical TSV rows 951,1096,2269,2271,2336,2363,2527,2646,2790,2812,2815,2847,2882,3001,3231,4393
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: '[{"row": 951, "data": {"study_gold_id": "Gs0117432", "path_count": "2",
    "paths": "Host-associated > Invertebrates > Cnidaria|Host-associated > Invertebrates
    > Cnidaria > Coral"}}, {"row": 1096, "data": {"study_gold_id": "Gs0118447", "path_count":
    "1", "paths": "Host-associated > Invertebrates > Cnidaria > Coral"}}, {"row":
    2269, "data": {"study_gold_id": "Gs0141911", "path_count": "1", "paths": "Host-associated
    > Invertebrates > Cnidaria > Coral"}}, {"row": 2271, "data": {"study_gold_id":
    "Gs0141913", "path_count": "2", "paths": "Environmental > Aquatic > Marine > Intertidal
    zone > Coral reef|Host-associated > Invertebrates > Cnidaria > Coral"}}, {"row":
    2336, "data": {"study_gold_id": "Gs0142151", "path_count": "3", "paths": "Environmental
    > Aquatic > Marine > Oceanic|Environmental > Aquatic > Marine > Oceanic > Sediment|Host-associated
    > Invertebrates > Cnidaria > Coral"}}, {"row": 2363, "data": {"study_gold_id":
    "Gs0142267", "path_count": "2", "paths": "Environmental > Aquatic > Marine > Oceanic|Host-associated
    > Invertebrates > Cnidaria > Coral"}}, {"row": 2527, "data": {"study_gold_id":
    "Gs0144622", "path_count": "1", "paths": "Host-associated > Invertebrates > Cnidaria
    > Coral"}}, {"row": 2646, "data": {"study_gold_id": "Gs0144785", "path_count":
    "1", "paths": "Host-associated > Invertebrates > Cnidaria > Coral"}}, {"row":
    2790, "data": {"study_gold_id": "Gs0145051", "path_count": "1", "paths": "Host-associated
    > Invertebrates > Cnidaria > Coral"}}, {"row": 2812, "data": {"study_gold_id":
    "Gs0145073", "path_count": "1", "paths": "Host-associated > Invertebrates > Cnidaria
    > Coral"}}, {"row": 2815, "data": {"study_gold_id": "Gs0145076", "path_count":
    "1", "paths": "Host-associated > Invertebrates > Cnidaria > Coral"}}, {"row":
    2847, "data": {"study_gold_id": "Gs0145108", "path_count": "1", "paths": "Host-associated
    > Invertebrates > Cnidaria > Coral"}}, {"row": 2882, "data": {"study_gold_id":
    "Gs0145193", "path_count": "1", "paths": "Host-associated > Invertebrates > Cnidaria
    > Coral"}}, {"row": 3001, "data": {"study_gold_id": "Gs0149384", "path_count":
    "1", "paths": "Host-associated > Invertebrates > Cnidaria > Coral"}}, {"row":
    3231, "data": {"study_gold_id": "Gs0150411", "path_count": "2", "paths": "Environmental
    > Aquatic > Marine|Host-associated > Invertebrates > Cnidaria > Coral"}}, {"row":
    4393, "data": {"study_gold_id": "Gs0160789", "path_count": "2", "paths": "Environmental
    > Aquatic > Marine > Benthic zone > Sediment|Host-associated > Invertebrates >
    Cnidaria > Coral"}}]'
  snapshot_sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 6996
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: '[{"row": 6996, "data": {"subject": "ENVO:01001179", "predicate": "rdfs:subClassOf",
    "object": "ENVO:01001002"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET9
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 8667
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: '[{"row": 8667, "data": {"term_id": "ENVO:01001179", "ontology": "ENVO",
    "label": "cnidarian-associated environment", "definition": "An environmental system
    determined by a cnidarian or part of a cnidarian.", "synonyms": "", "deprecated":
    "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET10
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 1572
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: '[{"row": 1572, "data": {"identifier": "habitatmech:GOLD.a12eda25e9", "decision":
    "GROUND_AS_PARENT", "object_id": "ENVO:01001179", "object_label": "cnidarian-associated
    environment", "grounding_status": "NARROW", "curator": "claude-opus-5", "date":
    "2026-08-14", "notes": "Grounding-cohort review (#62): was FOODON:03412872 ''barramundi''
    \u2014 a FISH, matched because barramundi carries ''coral'' as a synonym (its
    Bengali name). GOLD''s path is Host-associated > Invertebrates > Cnidaria > Coral,
    so the habitat is a coral animal. Kept as a narrower kind of cnidarian-associated
    environment rather than grounded to it, because Host-associated > Cnidaria is
    the shallower path entitled to that term.", "review_depth": "ITEM", "category":
    "", "relation": ""}}]'
  snapshot_sha256: 5d3af0a0505a61cda5e088e2c4b7922b740b7423fbca957d49aa8261b5584b37
- evidence_id: EP11
  kind: record_content
  reference: data/habitats/host_associated/cnidarian_associated_environment.yaml
  locator: Full immediate parent record, context only
  accessed_at: '2026-10-16T05:44:06Z'
  support: supports
  summary: '{"identifier": "ENVO:01001179", "label": "cnidarian-associated environment",
    "definition": "An environmental system determined by a cnidarian or part of a
    cnidarian.", "definition_source": "ENVO", "habitat_category": "HOST_ASSOCIATED",
    "grounding_status": "EXACT", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text":
    "Cnidaria", "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text":
    "Cnidaria-Corals", "synonym_type": "EXACT_SYNONYM", "source": "BacDive"}], "parent_habitats":
    ["ENVO:01001000", "ENVO:01001002", "habitatmech:GOLD.4d792ac724"], "source_attestations":
    [{"source": "BACDIVE", "source_id": "bacdive.isolation_source:cnidaria-corals",
    "source_label": "Cnidaria-Corals", "mapping_predicate": "skos:exactMatch", "assertion_count":
    75, "assertion_unit": "STRAIN"}, {"source": "GOLD", "source_id": "gold.ecosystem:3383",
    "source_label": "Cnidaria", "source_path": "Host-associated > Cnidaria", "mapping_predicate":
    "skos:exactMatch", "assertion_count": 95, "assertion_unit": "ORGANISM", "notes":
    "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."},
    {"source": "GOLD", "source_id": "gold.ecosystem:3564", "source_label": "Cnidaria",
    "source_path": "Host-associated > Invertebrates > Cnidaria", "mapping_predicate":
    "skos:exactMatch", "assertion_count": 102, "assertion_unit": "ORGANISM", "notes":
    "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "characteristic_taxa": [{"taxon_id": "NCBITaxon:1449351", "source": "BACDIVE",
    "taxon_label": "Roseivivax isoporae LMG 25204", "association_count": 2, "rank":
    1, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:560080", "source": "BACDIVE",
    "taxon_label": "Shewanella corallii", "association_count": 2, "rank": 2, "candidate_pool":
    73}, {"taxon_id": "NCBITaxon:1027273", "source": "BACDIVE", "taxon_label": "Endozoicomonas
    montiporae", "association_count": 1, "rank": 3, "candidate_pool": 73}, {"taxon_id":
    "NCBITaxon:1048357", "source": "BACDIVE", "taxon_label": "Nocardiopsis coralliicola",
    "association_count": 1, "rank": 4, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1069963",
    "source": "BACDIVE", "taxon_label": "Janibacter alkaliphilus", "association_count":
    1, "rank": 5, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1074311", "source":
    "BACDIVE", "taxon_label": "Vibrio alfacsensis", "association_count": 1, "rank":
    6, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1120968", "source": "BACDIVE",
    "taxon_label": "Algoriphagus vanfongensis DSM 17529", "association_count": 1,
    "rank": 7, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1120983", "source":
    "BACDIVE", "taxon_label": "Amorphus coralli DSM 19760", "association_count": 1,
    "rank": 8, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1121027", "source":
    "BACDIVE", "taxon_label": "Aurantimonas coralicida DSM 14790", "association_count":
    1, "rank": 9, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1173995", "source":
    "BACDIVE", "taxon_label": "Parvularcula dongshanensis", "association_count": 1,
    "rank": 10, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1216969", "source":
    "BACDIVE", "taxon_label": "Janibacter corallicola NBRC 107790", "association_count":
    1, "rank": 11, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1224163", "source":
    "BACDIVE", "taxon_label": "Corynebacterium maris DSM 45190", "association_count":
    1, "rank": 12, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1234143", "source":
    "BACDIVE", "taxon_label": "Endozoicomonas euniceicola", "association_count": 1,
    "rank": 13, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1234144", "source":
    "BACDIVE", "taxon_label": "Endozoicomonas gorgoniicola", "association_count":
    1, "rank": 14, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1280004", "source":
    "BACDIVE", "taxon_label": "Vibrio owensii LMG 25430", "association_count": 1,
    "rank": 15, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1342794", "source":
    "BACDIVE", "taxon_label": "Photobacterium sanctipauli", "association_count": 1,
    "rank": 16, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1342818", "source":
    "BACDIVE", "taxon_label": "Vibrio madracius", "association_count": 1, "rank":
    17, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1348114", "source": "BACDIVE",
    "taxon_label": "Pseudoalteromonas piratica", "association_count": 1, "rank": 18,
    "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1385512", "source": "BACDIVE",
    "taxon_label": "Pontibacillus litoralis JSM 072002", "association_count": 1, "rank":
    19, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1401264", "source": "BACDIVE",
    "taxon_label": "Prauserella coralliicola", "association_count": 1, "rank": 20,
    "candidate_pool": 73}, {"taxon_id": "NCBITaxon:141693", "source": "BACDIVE", "taxon_label":
    "Nocardiopsis kunsanensis", "association_count": 1, "rank": 21, "candidate_pool":
    73}, {"taxon_id": "NCBITaxon:1452538", "source": "BACDIVE", "taxon_label": "Microbacterium
    aureliae", "association_count": 1, "rank": 22, "candidate_pool": 73}, {"taxon_id":
    "NCBITaxon:1453497", "source": "BACDIVE", "taxon_label": "Kosmotoga arenicorallina
    S304", "association_count": 1, "rank": 23, "candidate_pool": 73}, {"taxon_id":
    "NCBITaxon:1479025", "source": "BACDIVE", "taxon_label": "Myceligenerans cantabricum",
    "association_count": 1, "rank": 24, "candidate_pool": 73}, {"taxon_id": "NCBITaxon:1481923",
    "source": "BACDIVE", "taxon_label": "Vibrio astriarenae", "association_count":
    1, "rank": 25, "candidate_pool": 73}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by BACDIVE, GOLD. Grounding: EXACT."}, {"timestamp":
    "2026-08-17T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes":
    "Grounded to ENVO:01001179 ''cnidarian-associated environment'' (EXACT). Adversarial
    review of #120 (#123): #114 correctly reversed this from NOT_APPLICABLE \u2014
    a cnidarian host is a habitat \u2014 but overshot by making it a term-request
    candidate. The term already exists: ENVO:01001179 ''cnidarian-associated environment'',
    ''an environmental system determined by a cnidarian or part of a cnidarian'',
    present in the vendored slice with that exact label. Requesting it would have
    been requesting a duplicate. Grounded EXACT. Note that GROUND does not carry an
    xref the way NOT_APPLICABLE and CONFIRM_UNGROUNDED do, so the taxon link (mesh:D003063
    / mesh:D037421) is not retained on the record; the upstream mapping remains in
    data/raw/. Found by the deep research run in #120, which is the point of running
    it. (source concept habitatmech:BACDIVE.ef2153283d)"}, {"timestamp": "2026-08-17T00:00:00Z",
    "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to ENVO:01001179
    ''cnidarian-associated environment'' (EXACT). Adversarial review of #120 (#123):
    #114 correctly reversed this from NOT_APPLICABLE \u2014 a cnidarian host is a
    habitat \u2014 but overshot by making it a term-request candidate. The term already
    exists: ENVO:01001179 ''cnidarian-associated environment'', ''an environmental
    system determined by a cnidarian or part of a cnidarian'', present in the vendored
    slice with that exact label. Requesting it would have been requesting a duplicate.
    Grounded EXACT. Note that GROUND does not carry an xref the way NOT_APPLICABLE
    and CONFIRM_UNGROUNDED do, so the taxon link (mesh:D003063 / mesh:D037421) is
    not retained on the record; the upstream mapping remains in data/raw/. Found by
    the deep research run in #120, which is the point of running it. (source concept
    habitatmech:GOLD.00086e0958)"}, {"timestamp": "2026-08-17T00:00:00Z", "curator":
    "claude-opus-5", "action": "GROUND", "changes": "Grounded to ENVO:01001179 ''cnidarian-associated
    environment'' (EXACT). Adversarial review of #120 (#123): #114 correctly reversed
    this from NOT_APPLICABLE \u2014 a cnidarian host is a habitat \u2014 but overshot
    by making it a term-request candidate. The term already exists: ENVO:01001179
    ''cnidarian-associated environment'', ''an environmental system determined by
    a cnidarian or part of a cnidarian'', present in the vendored slice with that
    exact label. Requesting it would have been requesting a duplicate. Grounded EXACT.
    Note that GROUND does not carry an xref the way NOT_APPLICABLE and CONFIRM_UNGROUNDED
    do, so the taxon link (mesh:D003063 / mesh:D037421) is not retained on the record;
    the upstream mapping remains in data/raw/. Found by the deep research run in #120,
    which is the point of running it. (source concept habitatmech:GOLD.e3fede2aea)"}]}'
  snapshot_sha256: 89a86d0b96bbc29b7bc9b40caceaf294637cd8c380499ea41160cf4e0062524a
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph
  locator: ENVO_01001000-graph.json
  accessed_at: '2026-10-16T05:15:44Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: e11b34dbd0a626083d5d0bbbb364469ef95831fb61cb81da5377d59715b272ca
- evidence_id: EX13
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000
  locator: ENVO_01001000.json
  accessed_at: '2026-10-16T05:15:43Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "ENVO:01001000", "label": "environmental system determined by an organism", "is_obsolete":
    false, "description": ["An environmental system which is determined by a living
    organism."], "obo_synonym": null}'
  snapshot_sha256: 8bd797929d18bf28171af7fd10f358db9b093f752d20b99f665779bb2e6b504e
- evidence_id: EX14
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph
  locator: ENVO_01001002-graph.json
  accessed_at: '2026-10-16T05:15:49Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 882375d994d0dea7166097328c56e0e22362848e68aba0125d1b128a24ebf1b0
- evidence_id: EX15
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002
  locator: ENVO_01001002.json
  accessed_at: '2026-10-16T05:15:48Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "ENVO:01001002", "label": "animal-associated environment", "is_obsolete": false,
    "description": ["An environmental system determined by an animal."], "obo_synonym":
    null}'
  snapshot_sha256: c3c90d5e91cc85727658222c907f7747f34861ad80bf1ceac5ce209f7e170907
- evidence_id: EX16
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179/graph
  locator: ENVO_01001179-graph.json
  accessed_at: '2026-10-16T05:15:52Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001179",
    "target": "http://purl.obolibrary.org/obo/ENVO_01001002", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 7d620bad5f1672b07b4d54f47cadfba16d097d63a69aefb177ad5b21cc746f6a
- evidence_id: EX17
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001179
  locator: ENVO_01001179.json
  accessed_at: '2026-10-16T05:15:51Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "ENVO:01001179", "label": "cnidarian-associated environment", "is_obsolete": false,
    "description": ["An environmental system determined by a cnidarian or part of
    a cnidarian."], "obo_synonym": null}'
  snapshot_sha256: 967b0dc5b61ac3206f724734a4c631bbc02b5d025c7f4093f374cae3b7b07e12
- evidence_id: ESEARCH
  kind: search
  reference: Local source and review corpus
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.a12eda25e9 -e Coral -e
    coral -e habitatmech:GOLD.a12eda25e9 curation history research reports data/raw
    build reviews
  accessed_at: '2026-10-16T05:15:46Z'
  support: context_only
  summary: Exact source keys and structured archive parsed independently; broad name
    hits are leads, not all inspected. No formal target predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews
    including hidden/ignored files; independent structured YAML traversal.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, grounding, aliases and strict hierarchy
  outcome: concern
  summary: The full Invertebrates > Cnidaria > Coral source supports a coral-associated
    environment narrower than cnidarian-associated environment, not a coral-reef setting
    or fish identity. The ITEM grounding-as-parent decision is coherent. Preserve
    382 ORGANISM assertions separately from 267 supplemental biosamples and study
    memberships; the parent record is context, not newly reviewed coverage. Only the
    narrow mapping endpoint defect is confirmed here.
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - EP11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
- assessment_id: A2
  area: quantity
  topic: Counts, units, taxon ranks, scores and candidate pools
  outcome: supported
  summary: 'Exact source rows reproduce emitted counts/units and displayed ranks/scores/pools.
    Zero tree counts are omitted; supplemental biosamples, study memberships and triads
    are nonadditive. {"assertions": [{"source": "GOLD", "count": 382, "unit": "ORGANISM",
    "row": {"row": 81, "data": {"canonical_path": "Host-associated > Invertebrates
    > Cnidaria > Coral", "ecosystem": "Host-associated", "ecosystem_category": "Invertebrates",
    "ecosystem_type": "Cnidaria", "ecosystem_subtype": "Coral", "specific_ecosystem":
    "", "leaf_label": "Coral", "depth": "4", "gold_node_count": "2", "organism_count":
    "382", "study_count": "0", "biosample_count": "0", "total_assertions": "382",
    "gold_node_ids": "gold.ecosystem:3643|gold.ecosystem:4088"}}}], "taxa": []}'
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - EP11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
- assessment_id: A3
  area: evidence
  topic: Association support and source limits
  outcome: supported
  summary: The full Invertebrates > Cnidaria > Coral source supports a coral-associated
    environment narrower than cnidarian-associated environment, not a coral-reef setting
    or fish identity. The ITEM grounding-as-parent decision is coherent. Preserve
    382 ORGANISM assertions separately from 267 supplemental biosamples and study
    memberships; the parent record is context, not newly reviewed coverage. Only the
    narrow mapping endpoint defect is confirmed here. Each cited source supports only
    its stated scope; original source pairs were not exhaustively reconstructed.
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - EP11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
- assessment_id: A4
  area: completeness
  topic: Native lifecycle and optional content
  outcome: supported
  summary: Executed routes reproduce NARROW/REVIEWED. Required fields are present;
    absent optional parameters, causal graphs, discussions and datasets are not fabricated.
    No scientific status promotion follows from this review.
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native gates and exact reproduction
  outcome: supported
  summary: '31 baseline commands passed: individual schemas, 24-target strict validation,
    834 histories, provenance, exact 3209-record reproduction, 32 causal overlays,
    110 term requests and configured labels. Exact-base hosted QC passed; deterministic
    validity is not scientific approval.'
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  evidence_ids:
  - E1
  - ESCHEMA
  - ERULE
findings:
- finding_id: F1
  issue_key: coral-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Mapping uses an undeclared ontology-parent endpoint
  description: 'The executed narrower-than-leaf route retains the source mint but
    emits narrowMatch relative to an ontology parent, whereas the schema endpoint
    is the record identifier. Reconcile producer, schema and consumers under #1398.
    This is not a formal SKOS self-link prohibition or a request for a blind predicate
    reversal.'
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - EP11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.a12eda25e9
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  description: 'The executed narrower-than-leaf route retains the source mint but
    emits narrowMatch relative to an ontology parent, whereas the schema endpoint
    is the record identifier. Reconcile producer, schema and consumers under #1398.
    This is not a formal SKOS self-link prohibition or a request for a blind predicate
    reversal. Proposed work only; no repair or status promotion is performed by this
    review.'
  generator: Controlled source/input correction, just seed, inspected just seed-canary,
    guarded just seed-apply, and dependent term-request/map/site/redirect regeneration
    where required.
  acceptance_checks:
  - Regress the exact target claim and preserve valid genera, identifiers, source
    counts/units and taxon associations. Recover original evidence before deleting
    a provisional pair; do not decrement frozen totals by hand.
  - Record authorized curation history; require schema, strict, provenance, history,
    label, corpus, site and full QC gates.
  - Save an immutable successor with the same issue key and exact predecessor finding
    identity.
limitations:
- Original specimen-level evidence and all pair-level citations were not exhaustively
  reconstructed. Native association counts, taxon ranks and scores do not establish
  prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs. Exact target TaxIds were
  separately resolved; frozen taxon labels are not universally current.
- Exact-base hosted QC covers unchanged scientific inputs, not a fresh local full-QC
  execution or these new review outputs. Native validate/save and subsequent archive/final-head
  gates are separate.
- 'iModulonDB is not applicable: no gene, regulator or expression-module claim is
  asserted. No new causal mechanism is imported.'
notes:
- All captured local input hashes were independently checked against exact base 13cddc722250dcad4327e5f9fad0a12fe7c08268.
- This baseline observation changes no scientific input. Separately authorized PR
  remediation follows; no status promotion is conferred by review validation.
- Ignored-inclusive structured archive traversal found no formal previous target review.
  Legacy reports are context, not predecessor lineage.
tags:
- individual-scientific-review
- host-associated
```
