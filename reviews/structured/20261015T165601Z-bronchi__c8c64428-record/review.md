# Record review: Bronchi (habitatmech:GOLD.f7cc0ef1b4)

- Review: 20261015T165601Z-bronchi__c8c64428-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T16:30:40Z
- Finished UTC: 2026-10-15T16:56:01Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Avian Bronchi preserves a meaningful host context and generic bronchus genus despite zero tree ORGANISM assertions. It is not a subtype of the whole respiratory system. The legacy verdict-format repair in #490 did not establish scientific correctness of this edge or resolve the narrow mapping endpoint mismatch.

## Scope And Provenance

Full field-by-field scientific review of this one exact target at 50dbf8b388bf32ca58708f7993e83120310f7cea.

Selection: One of the next 24 path-ordered unreviewed targets in an ignored-inclusive 3208-record census. This bundle assesses only this identifier, not a cohort sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 50dbf8b388bf32ca58708f7993e83120310f7cea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.f7cc0ef1b4 | data/habitats/host_associated/bronchi__c8c64428.yaml | generated | Bronchi |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.f7cc0ef1b4 | Completed 2026-10-15T16:35:04Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bronchi__c8c64428.yaml |
| validate-strict | passed | True | habitatmech:GOLD.f7cc0ef1b4 | Completed 2026-10-15T16:35:27Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.f7cc0ef1b4 | Completed 2026-10-15T16:35:39Z. No issues found<br>814 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.f7cc0ef1b4 | Completed 2026-10-15T16:35:39Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.f7cc0ef1b4 | Completed 2026-10-15T16:36:01Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.f7cc0ef1b4 | Completed 2026-10-15T16:36:06Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.f7cc0ef1b4 | Completed 2026-10-15T16:36:35Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.f7cc0ef1b4 | Completed 2026-10-15T16:37:38Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | habitatmech:GOLD.f7cc0ef1b4 | Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320 |

## Scientific And Domain Assessments

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.f7cc0ef1b4.

Avian Bronchi preserves a meaningful host context and generic bronchus genus despite zero tree ORGANISM assertions. It is not a subtype of the whole respiratory system. The legacy verdict-format repair in #490 did not establish scientific correctness of this edge or resolve the narrow mapping endpoint mismatch.

### Frozen counts, units, ranks, channels and scores

quantity: supported. Targets: habitatmech:GOLD.f7cc0ef1b4.

Every source assertion and displayed taxon was checked against its exact raw row. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Side-table biosample/study counts are not added to tree ORGANISM counts. Zero-count omission is not biological absence.

### Scientific support and scope limits

evidence: supported. Targets: habitatmech:GOLD.f7cc0ef1b4.

Avian Bronchi preserves a meaningful host context and generic bronchus genus despite zero tree ORGANISM assertions. It is not a subtype of the whole respiratory system. The legacy verdict-format repair in #490 did not establish scientific correctness of this edge or resolve the narrow mapping endpoint mismatch.

### Status, optional content, triads and mechanisms

completeness: supported. Targets: habitatmech:GOLD.f7cc0ef1b4.

Actual routes reproduce NARROW/SEEDED. No environmental-parameter, causal-edge, discussion/dataset or is_characteristic=true assertion is present in this target. Optional absence and SEEDED status alone are not defects. Scientific review does not promote native status.

### Native deterministic validation

schema: supported. Targets: habitatmech:GOLD.f7cc0ef1b4.

Ordinary and strict schemas, 814 history records, provenance, 3208-record reproduction, 32 causal overlays, term-request checks, configured labels and exact-base full QC passed. These establish fidelity, not biological truth.

## Findings

### F1: Containing anatomy is not a broader habitat class

major / open / confirmed; issue key: bronchi--c8c64428-context-parent.

Exclude only the exact GOLD source-path/expected-parent contribution habitatmech:GOLD.0c74807e42. Avian Bronchi preserves a meaningful host context and generic bronchus genus despite zero tree ORGANISM assertions. It is not a subtype of the whole respiratory system. The legacy verdict-format repair in #490 did not establish scientific correctness of this edge or resolve the narrow mapping endpoint mismatch. Preserve independently valid ontology genera and source provenance.

### F2: Narrow predicate uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: bronchi--c8c64428-mapping-endpoint-contract.

Actual resolution retains the GOLD source mint but emits narrowMatch relative to the generic ontology parent. The SourceAttestation contract instead describes source-to-record identity. Reconcile producer/schema/consumers under #1398 without merging host-specific concepts or merely swapping predicates. This is not a claim that SKOS forbids self-links, and downstream SSSOM/KGX conformance has not been tested.

## Recommended Actions And Acceptance Checks

### ACT1

Exclude only the exact GOLD source-path/expected-parent contribution habitatmech:GOLD.0c74807e42. Avian Bronchi preserves a meaningful host context and generic bronchus genus despite zero tree ORGANISM assertions. It is not a subtype of the whole respiratory system. The legacy verdict-format repair in #490 did not establish scientific correctness of this edge or resolve the narrow mapping endpoint mismatch. Preserve independently valid ontology genera and source provenance. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identifiers, counts/units and raw provenance. Change identity, native status or mapping only when separately supported by the scoped item assessment; never change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Actual resolution retains the GOLD source mint but emits narrowMatch relative to the generic ontology parent. The SourceAttestation contract instead describes source-to-record identity. Reconcile producer/schema/consumers under #1398 without merging host-specific concepts or merely swapping predicates. This is not a claim that SKOS forbids self-links, and downstream SSSOM/KGX conformance has not been tested. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identifiers, counts/units and raw provenance. Change identity, native status or mapping only when separately supported by the scoped item assessment; never change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bronchi__c8c64428.yaml; Entire target YAML | supports | Entire record read: identity, definition, parents, source attestations, every displayed taxon and complete history. |
| ERULE | docs/CURATION.md; Host, anatomy, hierarchy, disposition and evidence rules | supports | Parent_habitats means strictly broader; source occurrence does not establish characteristic presence. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord and SourceAttestation slots | supports | Typed identity, broader habitat and source-to-record mapping semantics; optional fields are not mandatory. |
| ESEED | src/habitatmech/seed.py; Executed build_corpus/apply_decision routes and parent accumulation | supports | Full target equality was verified against actual generated document. Exact source routes: [{"mint": "habitatmech:GOLD.f7cc0ef1b4", "automatic": {"identifier": "habitatmech:GOLD.f7cc0ef1b4", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["UBERON:0002185"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.f7cc0ef1b4", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["UBERON:0002185"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Frozen inventory projection | supports | Source counts and taxon ranks/scores preserve source units; PREGO projections do not retain original pair-level citations. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 1901 | supports | [{"row": 1901, "data": {"canonical_path": "Host-associated &gt; Birds &gt; Respiratory system &gt; Bronchi", "ecosystem": "Host-associated", "ecosystem_category": "Birds", "ecosystem_type": "Respiratory system", "ecosystem_subtype": "Bronchi", "specific_ecosystem": "", "leaf_label": "Bronchi", "depth": "4", "gold_node_count": "2", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7440&#124;gold.ecosystem:7441"}}] |
| ET6 | data/raw/isolation_source_groundings.tsv; Physical TSV rows 52 | supports | [{"row": 52, "data": {"subject_label": "Bronchial-wash", "subject_label_normalized": "bronchial wash", "object_id": "UBERON:0002185", "object_label": "bronchus", "object_source": "UBERON", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification": "semapv:ManualMappingCuration", "curator": "manual_review", "source_dataset": "bacdive", "verified_date": "2026-05-02"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 11345 | supports | [{"row": 11345, "data": {"subject": "UBERON:0002185", "predicate": "rdfs:subClassOf", "object": "UBERON:0000117"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 13125 | supports | [{"row": 13125, "data": {"term_id": "UBERON:0002185", "ontology": "UBERON", "label": "bronchus", "definition": "The upper conducting airways of the lung; these airways arise from the terminus of the trachea.", "synonyms": "bronchi&#124;bronchial tissue&#124;bronchial trunk", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EP9 | data/habitats/host_associated/bronchus.yaml; Full parent record, context only | supports | {"identifier": "UBERON:0002185", "label": "bronchus", "definition": "The upper conducting airways of the lung; these airways arise from the terminus of the trachea.", "definition_source": "UBERON", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "CLOSE", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Bronchial-wash", "synonym_type": "RELATED_SYNONYM", "source": "BacDive"}, {"synonym_text": "bronchi", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text": "bronchial tissue", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text": "bronchial trunk", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}], "parent_habitats": ["UBERON:0000117"], "source_attestations": [{"source": "BACDIVE", "source_id": "bacdive.isolation_source:bronchial-wash", "source_label": "Bronchial-wash", "mapping_predicate": "skos:closeMatch", "assertion_count": 18, "assertion_unit": "STRAIN"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:1122164", "source": "BACDIVE", "taxon_label": "Legionella lansingensis DSM 19556 = ATCC 49751", "association_count": 1, "rank": 1, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:1141647", "source": "BACDIVE", "taxon_label": "Nocardia arizonensis", "association_count": 1, "rank": 2, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:1206729", "source": "BACDIVE", "taxon_label": "Nocardia exalbida NBRC 100660", "association_count": 1, "rank": 3, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:1226751", "source": "BACDIVE", "taxon_label": "Mycolicibacterium monacense DSM 44395", "association_count": 1, "rank": 4, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:1817", "source": "BACDIVE", "taxon_label": "Nocardia", "association_count": 1, "rank": 5, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:1962118", "source": "BACDIVE", "taxon_label": "Mycobacteroides abscessus subsp. massiliense", "association_count": 1, "rank": 6, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:2074", "source": "BACDIVE", "taxon_label": "Pseudonocardia autotrophica", "association_count": 1, "rank": 7, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:222805", "source": "BACDIVE", "taxon_label": "Mycobacterium intracellulare subsp. chimaera", "association_count": 1, "rank": 8, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:238", "source": "BACDIVE", "taxon_label": "Elizabethkingia meningoseptica", "association_count": 1, "rank": 9, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:28087", "source": "BACDIVE", "taxon_label": "Legionella sainthelensi", "association_count": 1, "rank": 10, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:286804", "source": "BACDIVE", "taxon_label": "Segniliparus rugosus", "association_count": 1, "rank": 11, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:341199", "source": "BACDIVE", "taxon_label": "Nocardia kroppenstedtii", "association_count": 1, "rank": 12, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:480035", "source": "BACDIVE", "taxon_label": "Nocardia wallacei", "association_count": 1, "rank": 13, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:524884", "source": "BACDIVE", "taxon_label": "Saccharopolyspora rosea", "association_count": 1, "rank": 14, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:72407", "source": "BACDIVE", "taxon_label": "Klebsiella pneumoniae subsp. pneumoniae", "association_count": 1, "rank": 15, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:747", "source": "BACDIVE", "taxon_label": "Pasteurella multocida", "association_count": 1, "rank": 16, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:756689", "source": "BACDIVE", "taxon_label": "Nocardia amikacinitolerans", "association_count": 1, "rank": 17, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:912594", "source": "BACDIVE", "taxon_label": "Mycolicibacterium iranicum", "association_count": 1, "rank": 18, "candidate_pool": 18}], "curation_history": [{"timestamp": "2026-08-14T00:00:00Z", "curator": "claude-opus-5", "action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Cohort review: no words shared, but a bronchial wash samples the bronchus, and the bronchus is where the strain lived. Grounding a lavage specimen to its anatomical site is the right habitat reading. (source concept habitatmech:BACDIVE.d37a7e5c01)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by BACDIVE. Grounding: CLOSE."}, {"timestamp": "2026-10-07T00:00:00Z", "curator": "seed_from_sources", "action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained BacDive label 'Bronchial-wash' as RELATED_SYNONYM: a CLOSE source mapping does not establish exact lexical equivalence. Independent ontology synonyms and verbatim attestations are preserved (#1459)."}]} |
| EP10 | data/habitats/host_associated/respiratory_system__431eac8d.yaml; Full parent record, context only | supports | {"identifier": "habitatmech:GOLD.0c74807e42", "label": "Respiratory system", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001004", "habitatmech:GOLD.47e603cf4f"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:3600", "source_label": "Respiratory system", "source_path": "Host-associated &gt; Birds &gt; Respiratory system", "mapping_predicate": "skos:narrowMatch", "assertion_count": 53, "assertion_unit": "ORGANISM", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]} |
| ELEGACY | reports/yaml_record_review/20260922T130216Z-bronchi__c8c64428.md; Findings and recommended edits; historical lead | supports | Legacy conclusions were compared with current target and primary evidence. No formal predecessor or automatic native-status requirement is inferred. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000117/graph; UBERON_0000117-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000117", "target": "http://purl.obolibrary.org/obo/UBERON_0000025", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000117", "target": "http://purl.obolibrary.org/obo/UBERON_0000065", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000117", "target": "http://purl.obolibrary.org/obo/UBERON_0000483", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000117; UBERON_0000117.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0000117", "label": "respiratory tube", "is_obsolete": false, "description": ["A tube in the respiratory system. Examples: bronchus, bronchiole, trachea."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001004/graph; UBERON_0001004-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001004", "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001004", "target": "http://purl.obolibrary.org/obo/GO_0003016", "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001004", "target": "http://purl.obolibrary.org/obo/GO_0007585", "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001004", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33213", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001004", "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001004; UBERON_0001004.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0001004", "label": "respiratory system", "is_obsolete": false, "description": ["Functional system which consists of structures involved in respiration."]} |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002185/graph; UBERON_0002185-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/UBERON_0002185", "target": "http://purl.obolibrary.org/obo/UBERON_0000117", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002185", "target": "http://purl.obolibrary.org/obo/UBERON_0002224", "uri": "http://purl.obolibrary.org/obo/RO_0001025", "label": "located in"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002185", "target": "http://purl.obolibrary.org/obo/UBERON_0007196", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002185; UBERON_0002185.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0002185", "label": "bronchus", "is_obsolete": false, "description": ["The upper conducting airways of the lung; these airways arise from the terminus of the trachea."]} |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.f7cc0ef1b4 -e Bronchi -e bronchi__c8c64428 -e habitatmech:GOLD.f7cc0ef1b4 curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately from broad textual matches. No previous structured target observation was found; not every broad label match was inspected. |

## Limits And Additional Notes

- Historical specimens and every original association have not been independently reidentified. Counts, scores and ranked rows are not prevalence, viability, characteristic presence or mechanism.
- The label gate skips 2061 no-adapter pairs and does not certify taxon labels. Every displayed taxon ID was separately resolved through current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged input baseline, not a new local full-QC execution. These new review bundles require their native post-save archive check.
- iModulonDB is not applicable: no gene, regulator, transcriptomic module or causal mechanism is asserted. No paid research was used.
- Input hashes match both current working bytes and exact tracked base blobs; source.state git_commit describes that historical revision without silently refreshing inputs.
- Ignored-inclusive searches and parsed structured archive found no previous structured observation targeting this exact identifier. Legacy findings were inspected as leads, not adopted automatically or assigned false structured lineage.
- Review-only: no habitat curation, regeneration, status promotion, history mutation or GitHub mutation is performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T165601Z-bronchi__c8c64428-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Bronchi (habitatmech:GOLD.f7cc0ef1b4)'
started_at: '2026-10-15T16:30:40Z'
finished_at: '2026-10-15T16:56:01Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the target and evidence; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Avian Bronchi preserves a meaningful host context and generic bronchus genus
  despite zero tree ORGANISM assertions. It is not a subtype of the whole respiratory
  system. The legacy verdict-format repair in #490 did not establish scientific correctness
  of this edge or resolve the narrow mapping endpoint mismatch.'
source:
  git_revision: 50dbf8b388bf32ca58708f7993e83120310f7cea
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
    sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 6d5cbfd0f5ad911fbb074ee8ec253625d1fa13d94117759b1f25a1cd2e6576bc
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 903fc125adcd84df9fa99a4fae71b30d4a3541efc48eeff3cd49b94e866a5056
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: dfde49f64273cb94b4162170a5542c94880fa36015ccaac6edfa248820492a23
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
  - path: data/habitats/host_associated/bronchi__c8c64428.yaml
    sha256: 0094773f67dcbcbe87e5f5f8acc9e867b02b6744715367590c7067d886d29fa7
    role: target
  - path: data/habitats/host_associated/bronchus.yaml
    sha256: a508a8a4dbd42a1a1204559e6f8c430f3b269f69a923100ae7fd30e547214cdc
    role: context
  - path: data/habitats/host_associated/respiratory_system__431eac8d.yaml
    sha256: 700815817315ed32613134e3b2ba05700a2600c1c0935a53173134b967d0e617
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
  - path: reports/yaml_record_review/20260922T130216Z-bronchi__c8c64428.md
    sha256: 64016b141083c4a3d8fb7f17fa9f97bd16d7bc68714422651fa0ecd9f8efcd08
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
targets:
- target_id: habitatmech:GOLD.f7cc0ef1b4
  path: data/habitats/host_associated/bronchi__c8c64428.yaml
  label: Bronchi
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
  description: Full field-by-field scientific review of this one exact target at 50dbf8b388bf32ca58708f7993e83120310f7cea.
  selection: One of the next 24 path-ordered unreviewed targets in an ignored-inclusive
    3208-record census. This bundle assesses only this identifier, not a cohort sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context is not additional coverage. Export compatibility and original
      individual source specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bronchi__c8c64428.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  summary: "Completed 2026-10-15T16:35:04Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bronchi__c8c64428.yaml"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml
    data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml
    data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml
    data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml
    data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml
    data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml
    data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml
    data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml
    data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml
    data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml
    data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml
    data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  summary: "Completed 2026-10-15T16:35:27Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml\
    \ data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml\
    \ data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml\
    \ data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml\
    \ data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml\
    \ data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml\
    \ data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml\
    \ data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml\
    \ data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml\
    \ data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml\
    \ data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml\
    \ data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  summary: 'Completed 2026-10-15T16:35:39Z. No issues found

    814 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  summary: "Completed 2026-10-15T16:35:39Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  summary: "Completed 2026-10-15T16:36:01Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  summary: "Completed 2026-10-15T16:36:06Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  summary: "Completed 2026-10-15T16:36:35Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  summary: "Completed 2026-10-15T16:37:38Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: CCI
  name: Exact-baseline full QC
  status: passed
  required: true
  command: gh run view 38764995320 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  summary: Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320
  scope_note: Exact unchanged scientific input baseline; new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bronchi__c8c64428.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: 'Entire record read: identity, definition, parents, source attestations,
    every displayed taxon and complete history.'
  snapshot_sha256: 0094773f67dcbcbe87e5f5f8acc9e867b02b6744715367590c7067d886d29fa7
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host, anatomy, hierarchy, disposition and evidence rules
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: Parent_habitats means strictly broader; source occurrence does not establish
    characteristic presence.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord and SourceAttestation slots
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: Typed identity, broader habitat and source-to-record mapping semantics;
    optional fields are not mandatory.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed build_corpus/apply_decision routes and parent accumulation
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: 'Full target equality was verified against actual generated document. Exact
    source routes: [{"mint": "habitatmech:GOLD.f7cc0ef1b4", "automatic": {"identifier":
    "habitatmech:GOLD.f7cc0ef1b4", "grounding_status": "NARROW", "mapping_predicate":
    "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["UBERON:0002185"],
    "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null,
    "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.f7cc0ef1b4",
    "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding":
    true, "extra_parents": ["UBERON:0002185"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match",
    "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Frozen inventory projection
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: Source counts and taxon ranks/scores preserve source units; PREGO projections
    do not retain original pair-level citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 1901
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: '[{"row": 1901, "data": {"canonical_path": "Host-associated > Birds > Respiratory
    system > Bronchi", "ecosystem": "Host-associated", "ecosystem_category": "Birds",
    "ecosystem_type": "Respiratory system", "ecosystem_subtype": "Bronchi", "specific_ecosystem":
    "", "leaf_label": "Bronchi", "depth": "4", "gold_node_count": "2", "organism_count":
    "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids":
    "gold.ecosystem:7440|gold.ecosystem:7441"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: Physical TSV rows 52
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: '[{"row": 52, "data": {"subject_label": "Bronchial-wash", "subject_label_normalized":
    "bronchial wash", "object_id": "UBERON:0002185", "object_label": "bronchus", "object_source":
    "UBERON", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification":
    "semapv:ManualMappingCuration", "curator": "manual_review", "source_dataset":
    "bacdive", "verified_date": "2026-05-02"}}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 11345
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: '[{"row": 11345, "data": {"subject": "UBERON:0002185", "predicate": "rdfs:subClassOf",
    "object": "UBERON:0000117"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 13125
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: '[{"row": 13125, "data": {"term_id": "UBERON:0002185", "ontology": "UBERON",
    "label": "bronchus", "definition": "The upper conducting airways of the lung;
    these airways arise from the terminus of the trachea.", "synonyms": "bronchi|bronchial
    tissue|bronchial trunk", "deprecated": "", "directly_referenced": "TRUE", "label_only":
    "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/bronchus.yaml
  locator: Full parent record, context only
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: '{"identifier": "UBERON:0002185", "label": "bronchus", "definition": "The
    upper conducting airways of the lung; these airways arise from the terminus of
    the trachea.", "definition_source": "UBERON", "habitat_category": "HOST_ASSOCIATED",
    "grounding_status": "CLOSE", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text":
    "Bronchial-wash", "synonym_type": "RELATED_SYNONYM", "source": "BacDive"}, {"synonym_text":
    "bronchi", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text":
    "bronchial tissue", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text":
    "bronchial trunk", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}], "parent_habitats":
    ["UBERON:0000117"], "source_attestations": [{"source": "BACDIVE", "source_id":
    "bacdive.isolation_source:bronchial-wash", "source_label": "Bronchial-wash", "mapping_predicate":
    "skos:closeMatch", "assertion_count": 18, "assertion_unit": "STRAIN"}], "characteristic_taxa":
    [{"taxon_id": "NCBITaxon:1122164", "source": "BACDIVE", "taxon_label": "Legionella
    lansingensis DSM 19556 = ATCC 49751", "association_count": 1, "rank": 1, "candidate_pool":
    18}, {"taxon_id": "NCBITaxon:1141647", "source": "BACDIVE", "taxon_label": "Nocardia
    arizonensis", "association_count": 1, "rank": 2, "candidate_pool": 18}, {"taxon_id":
    "NCBITaxon:1206729", "source": "BACDIVE", "taxon_label": "Nocardia exalbida NBRC
    100660", "association_count": 1, "rank": 3, "candidate_pool": 18}, {"taxon_id":
    "NCBITaxon:1226751", "source": "BACDIVE", "taxon_label": "Mycolicibacterium monacense
    DSM 44395", "association_count": 1, "rank": 4, "candidate_pool": 18}, {"taxon_id":
    "NCBITaxon:1817", "source": "BACDIVE", "taxon_label": "Nocardia", "association_count":
    1, "rank": 5, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:1962118", "source":
    "BACDIVE", "taxon_label": "Mycobacteroides abscessus subsp. massiliense", "association_count":
    1, "rank": 6, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:2074", "source":
    "BACDIVE", "taxon_label": "Pseudonocardia autotrophica", "association_count":
    1, "rank": 7, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:222805", "source":
    "BACDIVE", "taxon_label": "Mycobacterium intracellulare subsp. chimaera", "association_count":
    1, "rank": 8, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:238", "source": "BACDIVE",
    "taxon_label": "Elizabethkingia meningoseptica", "association_count": 1, "rank":
    9, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:28087", "source": "BACDIVE",
    "taxon_label": "Legionella sainthelensi", "association_count": 1, "rank": 10,
    "candidate_pool": 18}, {"taxon_id": "NCBITaxon:286804", "source": "BACDIVE", "taxon_label":
    "Segniliparus rugosus", "association_count": 1, "rank": 11, "candidate_pool":
    18}, {"taxon_id": "NCBITaxon:341199", "source": "BACDIVE", "taxon_label": "Nocardia
    kroppenstedtii", "association_count": 1, "rank": 12, "candidate_pool": 18}, {"taxon_id":
    "NCBITaxon:480035", "source": "BACDIVE", "taxon_label": "Nocardia wallacei", "association_count":
    1, "rank": 13, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:524884", "source":
    "BACDIVE", "taxon_label": "Saccharopolyspora rosea", "association_count": 1, "rank":
    14, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:72407", "source": "BACDIVE",
    "taxon_label": "Klebsiella pneumoniae subsp. pneumoniae", "association_count":
    1, "rank": 15, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:747", "source":
    "BACDIVE", "taxon_label": "Pasteurella multocida", "association_count": 1, "rank":
    16, "candidate_pool": 18}, {"taxon_id": "NCBITaxon:756689", "source": "BACDIVE",
    "taxon_label": "Nocardia amikacinitolerans", "association_count": 1, "rank": 17,
    "candidate_pool": 18}, {"taxon_id": "NCBITaxon:912594", "source": "BACDIVE", "taxon_label":
    "Mycolicibacterium iranicum", "association_count": 1, "rank": 18, "candidate_pool":
    18}], "curation_history": [{"timestamp": "2026-08-14T00:00:00Z", "curator": "claude-opus-5",
    "action": "REVIEW", "changes": "Reviewed and endorsed the seeder''s own resolution.
    Cohort review: no words shared, but a bronchial wash samples the bronchus, and
    the bronchus is where the strain lived. Grounding a lavage specimen to its anatomical
    site is the right habitat reading. (source concept habitatmech:BACDIVE.d37a7e5c01)"},
    {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by BACDIVE. Grounding: CLOSE."}, {"timestamp": "2026-10-07T00:00:00Z", "curator":
    "seed_from_sources", "action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained BacDive
    label ''Bronchial-wash'' as RELATED_SYNONYM: a CLOSE source mapping does not establish
    exact lexical equivalence. Independent ontology synonyms and verbatim attestations
    are preserved (#1459)."}]}'
  snapshot_sha256: a508a8a4dbd42a1a1204559e6f8c430f3b269f69a923100ae7fd30e547214cdc
- evidence_id: EP10
  kind: record_content
  reference: data/habitats/host_associated/respiratory_system__431eac8d.yaml
  locator: Full parent record, context only
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.0c74807e42", "label": "Respiratory system",
    "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status":
    "SEEDED", "parent_habitats": ["UBERON:0001004", "habitatmech:GOLD.47e603cf4f"],
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:3600",
    "source_label": "Respiratory system", "source_path": "Host-associated > Birds
    > Respiratory system", "mapping_predicate": "skos:narrowMatch", "assertion_count":
    53, "assertion_unit": "ORGANISM", "notes": "3 GOLD ecosystem node ids share this
    path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: NARROW."}]}'
  snapshot_sha256: 700815817315ed32613134e3b2ba05700a2600c1c0935a53173134b967d0e617
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20260922T130216Z-bronchi__c8c64428.md
  locator: Findings and recommended edits; historical lead
  accessed_at: '2026-10-15T16:56:01Z'
  support: supports
  summary: Legacy conclusions were compared with current target and primary evidence.
    No formal predecessor or automatic native-status requirement is inferred.
  snapshot_sha256: 64016b141083c4a3d8fb7f17fa9f97bd16d7bc68714422651fa0ecd9f8efcd08
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000117/graph
  locator: UBERON_0000117-graph.json
  accessed_at: '2026-10-15T16:34:21Z'
  support: context_only
  summary: 'Typed outgoing ontology relations, not an untyped ancestor list: [{"source":
    "http://purl.obolibrary.org/obo/UBERON_0000117", "target": "http://purl.obolibrary.org/obo/UBERON_0000025",
    "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"},
    {"source": "http://purl.obolibrary.org/obo/UBERON_0000117", "target": "http://purl.obolibrary.org/obo/UBERON_0000065",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source":
    "http://purl.obolibrary.org/obo/UBERON_0000117", "target": "http://purl.obolibrary.org/obo/UBERON_0000483",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}]'
  snapshot_sha256: 1a3763a3fc0d5dc843ffa2800747ea1752b5aa2320f35325eb7fc32752d6e931
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000117
  locator: UBERON_0000117.json
  accessed_at: '2026-10-15T16:34:21Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0000117",
    "label": "respiratory tube", "is_obsolete": false, "description": ["A tube in
    the respiratory system. Examples: bronchus, bronchiole, trachea."]}'
  snapshot_sha256: 37f811ab94632f77084bde57cbf6caccee1a9bc342a6ccf08d68018a51fd5bf6
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001004/graph
  locator: UBERON_0001004-graph.json
  accessed_at: '2026-10-15T16:34:25Z'
  support: context_only
  summary: 'Typed outgoing ontology relations, not an untyped ancestor list: [{"source":
    "http://purl.obolibrary.org/obo/UBERON_0001004", "target": "http://purl.obolibrary.org/obo/UBERON_0000467",
    "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"},
    {"source": "http://purl.obolibrary.org/obo/UBERON_0001004", "target": "http://purl.obolibrary.org/obo/GO_0003016",
    "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source":
    "http://purl.obolibrary.org/obo/UBERON_0001004", "target": "http://purl.obolibrary.org/obo/GO_0007585",
    "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source":
    "http://purl.obolibrary.org/obo/UBERON_0001004", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33213",
    "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source":
    "http://purl.obolibrary.org/obo/UBERON_0001004", "target": "http://purl.obolibrary.org/obo/UBERON_0000066",
    "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"}]'
  snapshot_sha256: ca0a425e8a8352ed8baa842ae4e9fe7f8f504a9a2b3c06371d3d6677c20fc2a0
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001004
  locator: UBERON_0001004.json
  accessed_at: '2026-10-15T16:34:24Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0001004",
    "label": "respiratory system", "is_obsolete": false, "description": ["Functional
    system which consists of structures involved in respiration."]}'
  snapshot_sha256: 3b389fb2d5e22e25b0c502cc7ee186efb4657f244e89168fb09ecc3608ee5446
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002185/graph
  locator: UBERON_0002185-graph.json
  accessed_at: '2026-10-15T16:34:31Z'
  support: context_only
  summary: 'Typed outgoing ontology relations, not an untyped ancestor list: [{"source":
    "http://purl.obolibrary.org/obo/UBERON_0002185", "target": "http://purl.obolibrary.org/obo/UBERON_0000117",
    "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"},
    {"source": "http://purl.obolibrary.org/obo/UBERON_0002185", "target": "http://purl.obolibrary.org/obo/UBERON_0002224",
    "uri": "http://purl.obolibrary.org/obo/RO_0001025", "label": "located in"}, {"source":
    "http://purl.obolibrary.org/obo/UBERON_0002185", "target": "http://purl.obolibrary.org/obo/UBERON_0007196",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}]'
  snapshot_sha256: 23511eda7d0d5793039125f41ca6010ba9e7a5bcedc526d31699c21a88b62c28
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002185
  locator: UBERON_0002185.json
  accessed_at: '2026-10-15T16:34:30Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0002185",
    "label": "bronchus", "is_obsolete": false, "description": ["The upper conducting
    airways of the lung; these airways arise from the terminus of the trachea."]}'
  snapshot_sha256: 2c4ed6adb27738ca7592f153e9364906adfef2431835e9aa966afb0b54eb09db
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.f7cc0ef1b4 -e Bronchi
    -e bronchi__c8c64428 -e habitatmech:GOLD.f7cc0ef1b4 curation history research
    reports data/raw build reviews
  accessed_at: '2026-10-15T16:33:57Z'
  support: context_only
  summary: Exact source/curation rows were parsed separately from broad textual matches.
    No previous structured target observation was found; not every broad label match
    was inspected.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    ignored and hidden files included, with all structured review.yaml files parsed.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: 'Avian Bronchi preserves a meaningful host context and generic bronchus
    genus despite zero tree ORGANISM assertions. It is not a subtype of the whole
    respiratory system. The legacy verdict-format repair in #490 did not establish
    scientific correctness of this edge or resolve the narrow mapping endpoint mismatch.'
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
- assessment_id: A2
  area: quantity
  topic: Frozen counts, units, ranks, channels and scores
  outcome: supported
  summary: 'Every source assertion and displayed taxon was checked against its exact
    raw row. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Side-table biosample/study
    counts are not added to tree ORGANISM counts. Zero-count omission is not biological
    absence.'
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
- assessment_id: A3
  area: evidence
  topic: Scientific support and scope limits
  outcome: supported
  summary: 'Avian Bronchi preserves a meaningful host context and generic bronchus
    genus despite zero tree ORGANISM assertions. It is not a subtype of the whole
    respiratory system. The legacy verdict-format repair in #490 did not establish
    scientific correctness of this edge or resolve the narrow mapping endpoint mismatch.'
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
- assessment_id: A4
  area: completeness
  topic: Status, optional content, triads and mechanisms
  outcome: supported
  summary: Actual routes reproduce NARROW/SEEDED. No environmental-parameter, causal-edge,
    discussion/dataset or is_characteristic=true assertion is present in this target.
    Optional absence and SEEDED status alone are not defects. Scientific review does
    not promote native status.
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  evidence_ids:
  - E1
  - ERULE
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native deterministic validation
  outcome: supported
  summary: Ordinary and strict schemas, 814 history records, provenance, 3208-record
    reproduction, 32 causal overlays, term-request checks, configured labels and exact-base
    full QC passed. These establish fidelity, not biological truth.
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: bronchi--c8c64428-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Containing anatomy is not a broader habitat class
  description: 'Exclude only the exact GOLD source-path/expected-parent contribution
    habitatmech:GOLD.0c74807e42. Avian Bronchi preserves a meaningful host context
    and generic bronchus genus despite zero tree ORGANISM assertions. It is not a
    subtype of the whole respiratory system. The legacy verdict-format repair in #490
    did not establish scientific correctness of this edge or resolve the narrow mapping
    endpoint mismatch. Preserve independently valid ontology genera and source provenance.'
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
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
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: bronchi--c8c64428-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow predicate uses an undeclared ontology-parent endpoint
  description: 'Actual resolution retains the GOLD source mint but emits narrowMatch
    relative to the generic ontology parent. The SourceAttestation contract instead
    describes source-to-record identity. Reconcile producer/schema/consumers under
    #1398 without merging host-specific concepts or merely swapping predicates. This
    is not a claim that SKOS forbids self-links, and downstream SSSOM/KGX conformance
    has not been tested.'
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
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
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Exclude only the exact GOLD source-path/expected-parent contribution
    habitatmech:GOLD.0c74807e42. Avian Bronchi preserves a meaningful host context
    and generic bronchus genus despite zero tree ORGANISM assertions. It is not a
    subtype of the whole respiratory system. The legacy verdict-format repair in #490
    did not establish scientific correctness of this edge or resolve the narrow mapping
    endpoint mismatch. Preserve independently valid ontology genera and source provenance.
    No repair is performed by this review.'
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independent identifiers, counts/units
    and raw provenance. Change identity, native status or mapping only when separately
    supported by the scoped item assessment; never change source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.f7cc0ef1b4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Actual resolution retains the GOLD source mint but emits narrowMatch
    relative to the generic ontology parent. The SourceAttestation contract instead
    describes source-to-record identity. Reconcile producer/schema/consumers under
    #1398 without merging host-specific concepts or merely swapping predicates. This
    is not a claim that SKOS forbids self-links, and downstream SSSOM/KGX conformance
    has not been tested. No repair is performed by this review.'
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independent identifiers, counts/units
    and raw provenance. Change identity, native status or mapping only when separately
    supported by the scoped item assessment; never change source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Historical specimens and every original association have not been independently
  reidentified. Counts, scores and ranked rows are not prevalence, viability, characteristic
  presence or mechanism.
- The label gate skips 2061 no-adapter pairs and does not certify taxon labels. Every
  displayed taxon ID was separately resolved through current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged input baseline,
  not a new local full-QC execution. These new review bundles require their native
  post-save archive check.
- 'iModulonDB is not applicable: no gene, regulator, transcriptomic module or causal
  mechanism is asserted. No paid research was used.'
notes:
- Input hashes match both current working bytes and exact tracked base blobs; source.state
  git_commit describes that historical revision without silently refreshing inputs.
- Ignored-inclusive searches and parsed structured archive found no previous structured
  observation targeting this exact identifier. Legacy findings were inspected as leads,
  not adopted automatically or assigned false structured lineage.
- 'Review-only: no habitat curation, regeneration, status promotion, history mutation
  or GitHub mutation is performed.'
tags:
- individual-scientific-review
- host-associated
```
