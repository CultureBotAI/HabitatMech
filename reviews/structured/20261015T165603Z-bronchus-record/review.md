# Record review: bronchus (UBERON:0002185)

- Review: 20261015T165603Z-bronchus-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T16:30:55Z
- Finished UTC: 2026-10-15T16:56:03Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Uberon bronchus and its respiratory-tube superclass are supported. BacDive Bronchial-wash is intentionally a CLOSE sampled-site proxy with a RELATED source synonym, not exact lexical equivalence. The type-strain description of Legionella lansingensis ATCC49751 documents bronchoscopy washings. Eighteen STRAIN assertions and all eighteen displayed taxa remain source associations, not evidence that every isolate resided in bronchial tissue or was characteristic.

## Scope And Provenance

Full field-by-field scientific review of this one exact target at 50dbf8b388bf32ca58708f7993e83120310f7cea.

Selection: One of the next 24 path-ordered unreviewed targets in an ignored-inclusive 3208-record census. This bundle assesses only this identifier, not a cohort sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 50dbf8b388bf32ca58708f7993e83120310f7cea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0002185 | data/habitats/host_associated/bronchus.yaml | generated | bronchus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | UBERON:0002185 | Completed 2026-10-15T16:35:18Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bronchus.yaml |
| validate-strict | passed | True | UBERON:0002185 | Completed 2026-10-15T16:35:27Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | UBERON:0002185 | Completed 2026-10-15T16:35:39Z. No issues found<br>814 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | UBERON:0002185 | Completed 2026-10-15T16:35:39Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | UBERON:0002185 | Completed 2026-10-15T16:36:01Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | UBERON:0002185 | Completed 2026-10-15T16:36:06Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | UBERON:0002185 | Completed 2026-10-15T16:36:35Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | UBERON:0002185 | Completed 2026-10-15T16:37:38Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | UBERON:0002185 | Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320 |

## Scientific And Domain Assessments

### Identity, definition, hierarchy and aliases

identity: supported. Targets: UBERON:0002185.

Uberon bronchus and its respiratory-tube superclass are supported. BacDive Bronchial-wash is intentionally a CLOSE sampled-site proxy with a RELATED source synonym, not exact lexical equivalence. The type-strain description of Legionella lansingensis ATCC49751 documents bronchoscopy washings. Eighteen STRAIN assertions and all eighteen displayed taxa remain source associations, not evidence that every isolate resided in bronchial tissue or was characteristic.

### Frozen counts, units, ranks, channels and scores

quantity: supported. Targets: UBERON:0002185.

Every source assertion and displayed taxon was checked against its exact raw row. [{"source": "BACDIVE", "count": 18, "unit": "STRAIN"}]. Side-table biosample/study counts are not added to tree ORGANISM counts. Zero-count omission is not biological absence.

### Scientific support and scope limits

evidence: supported. Targets: UBERON:0002185.

Uberon bronchus and its respiratory-tube superclass are supported. BacDive Bronchial-wash is intentionally a CLOSE sampled-site proxy with a RELATED source synonym, not exact lexical equivalence. The type-strain description of Legionella lansingensis ATCC49751 documents bronchoscopy washings. Eighteen STRAIN assertions and all eighteen displayed taxa remain source associations, not evidence that every isolate resided in bronchial tissue or was characteristic.

### Status, optional content, triads and mechanisms

completeness: supported. Targets: UBERON:0002185.

Actual routes reproduce CLOSE/REVIEWED. No environmental-parameter, causal-edge, discussion/dataset or is_characteristic=true assertion is present in this target. Optional absence and SEEDED status alone are not defects. Scientific review does not promote native status.

### Native deterministic validation

schema: supported. Targets: UBERON:0002185.

Ordinary and strict schemas, 814 history records, provenance, 3208-record reproduction, 32 causal overlays, term-request checks, configured labels and exact-base full QC passed. These establish fidelity, not biological truth.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bronchus.yaml; Entire target YAML | supports | Entire record read: identity, definition, parents, source attestations, every displayed taxon and complete history. |
| ERULE | docs/CURATION.md; Host, anatomy, hierarchy, disposition and evidence rules | supports | Parent_habitats means strictly broader; source occurrence does not establish characteristic presence. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord and SourceAttestation slots | supports | Typed identity, broader habitat and source-to-record mapping semantics; optional fields are not mandatory. |
| ESEED | src/habitatmech/seed.py; Executed build_corpus/apply_decision routes and parent accumulation | supports | Full target equality was verified against actual generated document. Exact source routes: [{"mint": "habitatmech:BACDIVE.d37a7e5c01", "automatic": {"identifier": "UBERON:0002185", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "bacdive_mapping_table", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0002185", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_bacdive_mapping_table", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:BACDIVE.d37a7e5c01", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-14", "notes": "Cohort review: no words shared, but a bronchial wash samples the bronchus, and the bronchus is where the strain lived. Grounding a lavage specimen to its anatomical site is the right habitat reading.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Frozen inventory projection | supports | Source counts and taxon ranks/scores preserve source units; PREGO projections do not retain original pair-level citations. |
| ET5 | data/raw/bacdive_source_taxa.tsv; Physical TSV rows 396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413 | supports | [{"row": 396, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "1", "taxon_id": "NCBITaxon:1122164", "taxon_label": "Legionella lansingensis DSM 19556 = ATCC 49751", "strain_count": "1", "corroborated_by": ""}}, {"row": 397, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "2", "taxon_id": "NCBITaxon:1141647", "taxon_label": "Nocardia arizonensis", "strain_count": "1", "corroborated_by": ""}}, {"row": 398, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "3", "taxon_id": "NCBITaxon:1206729", "taxon_label": "Nocardia exalbida NBRC 100660", "strain_count": "1", "corroborated_by": ""}}, {"row": 399, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "4", "taxon_id": "NCBITaxon:1226751", "taxon_label": "Mycolicibacterium monacense DSM 44395", "strain_count": "1", "corroborated_by": ""}}, {"row": 400, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "5", "taxon_id": "NCBITaxon:1817", "taxon_label": "Nocardia", "strain_count": "1", "corroborated_by": ""}}, {"row": 401, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "6", "taxon_id": "NCBITaxon:1962118", "taxon_label": "Mycobacteroides abscessus subsp. massiliense", "strain_count": "1", "corroborated_by": ""}}, {"row": 402, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "7", "taxon_id": "NCBITaxon:2074", "taxon_label": "Pseudonocardia autotrophica", "strain_count": "1", "corroborated_by": ""}}, {"row": 403, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "8", "taxon_id": "NCBITaxon:222805", "taxon_label": "Mycobacterium intracellulare subsp. chimaera", "strain_count": "1", "corroborated_by": ""}}, {"row": 404, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "9", "taxon_id": "NCBITaxon:238", "taxon_label": "Elizabethkingia meningoseptica", "strain_count": "1", "corroborated_by": ""}}, {"row": 405, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "10", "taxon_id": "NCBITaxon:28087", "taxon_label": "Legionella sainthelensi", "strain_count": "1", "corroborated_by": ""}}, {"row": 406, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "11", "taxon_id": "NCBITaxon:286804", "taxon_label": "Segniliparus rugosus", "strain_count": "1", "corroborated_by": ""}}, {"row": 407, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "12", "taxon_id": "NCBITaxon:341199", "taxon_label": "Nocardia kroppenstedtii", "strain_count": "1", "corroborated_by": ""}}, {"row": 408, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "13", "taxon_id": "NCBITaxon:480035", "taxon_label": "Nocardia wallacei", "strain_count": "1", "corroborated_by": ""}}, {"row": 409, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "14", "taxon_id": "NCBITaxon:524884", "taxon_label": "Saccharopolyspora rosea", "strain_count": "1", "corroborated_by": ""}}, {"row": 410, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "15", "taxon_id": "NCBITaxon:72407", "taxon_label": "Klebsiella pneumoniae subsp. pneumoniae", "strain_count": "1", "corroborated_by": ""}}, {"row": 411, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "16", "taxon_id": "NCBITaxon:747", "taxon_label": "Pasteurella multocida", "strain_count": "1", "corroborated_by": ""}}, {"row": 412, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "17", "taxon_id": "NCBITaxon:756689", "taxon_label": "Nocardia amikacinitolerans", "strain_count": "1", "corroborated_by": ""}}, {"row": 413, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "18", "taxon_id": "NCBITaxon:912594", "taxon_label": "Mycolicibacterium iranicum", "strain_count": "1", "corroborated_by": ""}}] |
| ET6 | data/raw/isolation_source_groundings.tsv; Physical TSV rows 52 | supports | [{"row": 52, "data": {"subject_label": "Bronchial-wash", "subject_label_normalized": "bronchial wash", "object_id": "UBERON:0002185", "object_label": "bronchus", "object_source": "UBERON", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification": "semapv:ManualMappingCuration", "curator": "manual_review", "source_dataset": "bacdive", "verified_date": "2026-05-02"}}] |
| ET7 | data/raw/bacdive_isolation_sources.tsv; Physical TSV rows 119 | supports | [{"row": 119, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "label": "Bronchial-wash", "source_slug": "bronchial-wash", "strain_count": "18", "taxon_count": "18"}}] |
| ET8 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 11020,11345 | supports | [{"row": 11020, "data": {"subject": "UBERON:0000117", "predicate": "rdfs:subClassOf", "object": "UBERON:0000025"}}, {"row": 11345, "data": {"subject": "UBERON:0002185", "predicate": "rdfs:subClassOf", "object": "UBERON:0000117"}}] |
| ET9 | data/raw/ontology_terms.tsv; Physical TSV rows 12902,13125 | supports | [{"row": 12902, "data": {"term_id": "UBERON:0000117", "ontology": "UBERON", "label": "respiratory tube", "definition": "A tube in the respiratory system. Examples: bronchus, bronchiole, trachea.", "synonyms": "airway&#124;respiratory conducting tube&#124;segment of tracheobronchial tree&#124;tracheobronchial tree segment", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row": 13125, "data": {"term_id": "UBERON:0002185", "ontology": "UBERON", "label": "bronchus", "definition": "The upper conducting airways of the lung; these airways arise from the terminus of the trachea.", "synonyms": "bronchi&#124;bronchial tissue&#124;bronchial trunk", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET10 | curation/decisions.tsv; Physical TSV rows 1553 | supports | [{"row": 1553, "data": {"identifier": "habitatmech:BACDIVE.d37a7e5c01", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-14", "notes": "Cohort review: no words shared, but a bronchial wash samples the bronchus, and the bronchus is where the strain lived. Grounding a lavage specimen to its anatomical site is the right habitat reading.", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| ELEGACY | reports/yaml_record_review/20260922T142857Z-bronchus.md; Findings and recommended edits; historical lead | supports | Legacy conclusions were compared with current target and primary evidence. No formal predecessor or automatic native-status requirement is inferred. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000117/graph; UBERON_0000117-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000117", "target": "http://purl.obolibrary.org/obo/UBERON_0000025", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000117", "target": "http://purl.obolibrary.org/obo/UBERON_0000065", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000117", "target": "http://purl.obolibrary.org/obo/UBERON_0000483", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000117; UBERON_0000117.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0000117", "label": "respiratory tube", "is_obsolete": false, "description": ["A tube in the respiratory system. Examples: bronchus, bronchiole, trachea."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002185/graph; UBERON_0002185-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/UBERON_0002185", "target": "http://purl.obolibrary.org/obo/UBERON_0000117", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002185", "target": "http://purl.obolibrary.org/obo/UBERON_0002224", "uri": "http://purl.obolibrary.org/obo/RO_0001025", "label": "located in"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002185", "target": "http://purl.obolibrary.org/obo/UBERON_0007196", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002185; UBERON_0002185.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0002185", "label": "bronchus", "is_obsolete": false, "description": ["The upper conducting airways of the lung; these airways arise from the terminus of the trachea."]} |
| EX5 | https://bacdive.dsmz.de/isolation-sources; bacdive-isolation.html | context_only | Current BacDive isolation-source browser contains Bovinae (Cow, Cattle) and Bronchial wash categories. It is a vocabulary witness, not a census of the frozen strain membership or proof of cattle-only scope. |
| EX6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Legionella%20lansingensis%22%20AND%20%22species%22&amp;format=json&amp;resultType=core&amp;pageSize=20; paper-lansingensis.json | context_only | Primary species-description abstract PMID:1401005, DOI:10.1128/JCM.30.9.2398-2401.1992: strain1677-MI-H (ATCC49751) was isolated from bronchoscopy washings. Supports the sampled-site proxy, not histological residency or all eighteen BacDive observations. |
| EX7 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1117644,1122164,1131452,1131453,1131454,1131455,1133849,1141647,1157946,1162284,1162288,1177117,1189613,1193128,1199187,1206729,1214102,1220554,1226751,12455,1271862,1328,1329,1329902,1334,1348,1392869,147802,153721,1578,1590,1601,161879,1639,1658,1661,1679,1680,1682,1683,168808,169963,1718,1724,1796,1802,1817,184914,1886,1962118,197,198,2,205913,206,2074,2081794,222805,238,2701,28026,28087,286804,287,32002,32020,33,341199,36808,391904,439842,476,47885,480035,484020,51665,524884,653940,678,720,72407,731,747,756689,76759,82135,82348,83655,838,84107,912594,985762&amp;retmode=xml; taxonomy.xml | context_only | All displayed IDs resolve in current NCBI Taxonomy. Preferred names and source labels were compared, without treating recognized historical aliases as wrong identities: [{"id": "NCBITaxon:1122164", "source": "BACDIVE", "label": "Legionella lansingensis DSM 19556 = ATCC 49751", "current_id": "1122164", "current_name": "Legionella lansingensis DSM 19556 = ATCC 49751", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1141647", "source": "BACDIVE", "label": "Nocardia arizonensis", "current_id": "1141647", "current_name": "Nocardia arizonensis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1206729", "source": "BACDIVE", "label": "Nocardia exalbida NBRC 100660", "current_id": "1206729", "current_name": "Nocardia exalbida NBRC 100660", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1226751", "source": "BACDIVE", "label": "Mycolicibacterium monacense DSM 44395", "current_id": "1226751", "current_name": "Mycolicibacterium monacense DSM 44395", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1817", "source": "BACDIVE", "label": "Nocardia", "current_id": "1817", "current_name": "Nocardia", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1962118", "source": "BACDIVE", "label": "Mycobacteroides abscessus subsp. massiliense", "current_id": "1962118", "current_name": "Mycobacteroides abscessus subsp. massiliense", "rank": "subspecies", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2074", "source": "BACDIVE", "label": "Pseudonocardia autotrophica", "current_id": "2074", "current_name": "Pseudonocardia autotrophica", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:222805", "source": "BACDIVE", "label": "Mycobacterium intracellulare subsp. chimaera", "current_id": "222805", "current_name": "Mycobacterium intracellulare subsp. chimaera", "rank": "subspecies", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:238", "source": "BACDIVE", "label": "Elizabethkingia meningoseptica", "current_id": "238", "current_name": "Elizabethkingia meningoseptica", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28087", "source": "BACDIVE", "label": "Legionella sainthelensi", "current_id": "28087", "current_name": "Legionella sainthelensi", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:286804", "source": "BACDIVE", "label": "Segniliparus rugosus", "current_id": "286804", "current_name": "Segniliparus rugosus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:341199", "source": "BACDIVE", "label": "Nocardia kroppenstedtii", "current_id": "341199", "current_name": "Nocardia kroppenstedtii", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:480035", "source": "BACDIVE", "label": "Nocardia wallacei", "current_id": "480035", "current_name": "Nocardia wallacei", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:524884", "source": "BACDIVE", "label": "Saccharopolyspora rosea", "current_id": "524884", "current_name": "Saccharopolyspora rosea", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:72407", "source": "BACDIVE", "label": "Klebsiella pneumoniae subsp. pneumoniae", "current_id": "72407", "current_name": "Klebsiella pneumoniae subsp. pneumoniae", "rank": "subspecies", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:747", "source": "BACDIVE", "label": "Pasteurella multocida", "current_id": "747", "current_name": "Pasteurella multocida", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:756689", "source": "BACDIVE", "label": "Nocardia amikacinitolerans", "current_id": "756689", "current_name": "Nocardia amikacinitolerans", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:912594", "source": "BACDIVE", "label": "Mycolicibacterium iranicum", "current_id": "912594", "current_name": "Mycolicibacterium iranicum", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e UBERON:0002185 -e bronchus -e bronchus -e habitatmech:BACDIVE.d37a7e5c01 curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately from broad textual matches. No previous structured target observation was found; not every broad label match was inspected. |

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
review_id: 20261015T165603Z-bronchus-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: bronchus (UBERON:0002185)'
started_at: '2026-10-15T16:30:55Z'
finished_at: '2026-10-15T16:56:03Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the target and evidence; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Uberon bronchus and its respiratory-tube superclass are supported. BacDive
  Bronchial-wash is intentionally a CLOSE sampled-site proxy with a RELATED source
  synonym, not exact lexical equivalence. The type-strain description of Legionella
  lansingensis ATCC49751 documents bronchoscopy washings. Eighteen STRAIN assertions
  and all eighteen displayed taxa remain source associations, not evidence that every
  isolate resided in bronchial tissue or was characteristic.
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
  - path: data/habitats/host_associated/bronchus.yaml
    sha256: a508a8a4dbd42a1a1204559e6f8c430f3b269f69a923100ae7fd30e547214cdc
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
  - path: reports/yaml_record_review/20260922T142857Z-bronchus.md
    sha256: 16a35fa1f4fc60aa41fa23696d9240d66d3d33a18cf2c98643a1e12065f766e4
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
- target_id: UBERON:0002185
  path: data/habitats/host_associated/bronchus.yaml
  label: bronchus
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
  - UBERON:0002185
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context is not additional coverage. Export compatibility and original
      individual source specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bronchus.yaml
  exit_code: 0
  target_ids:
  - UBERON:0002185
  summary: "Completed 2026-10-15T16:35:18Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bronchus.yaml"
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
  - UBERON:0002185
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
  - UBERON:0002185
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
  - UBERON:0002185
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
  - UBERON:0002185
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
  - UBERON:0002185
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
  - UBERON:0002185
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
  - UBERON:0002185
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
  - UBERON:0002185
  summary: Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320
  scope_note: Exact unchanged scientific input baseline; new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bronchus.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: 'Entire record read: identity, definition, parents, source attestations,
    every displayed taxon and complete history.'
  snapshot_sha256: a508a8a4dbd42a1a1204559e6f8c430f3b269f69a923100ae7fd30e547214cdc
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host, anatomy, hierarchy, disposition and evidence rules
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: Parent_habitats means strictly broader; source occurrence does not establish
    characteristic presence.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord and SourceAttestation slots
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: Typed identity, broader habitat and source-to-record mapping semantics;
    optional fields are not mandatory.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed build_corpus/apply_decision routes and parent accumulation
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: 'Full target equality was verified against actual generated document. Exact
    source routes: [{"mint": "habitatmech:BACDIVE.d37a7e5c01", "automatic": {"identifier":
    "UBERON:0002185", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch",
    "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "bacdive_mapping_table", "category": null, "reviewed": false, "decision": null},
    "final": {"identifier": "UBERON:0002185", "grounding_status": "CLOSE", "mapping_predicate":
    "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs":
    [], "route": "curated_review_of_bacdive_mapping_table", "category": null, "reviewed":
    true, "decision": {"identifier": "habitatmech:BACDIVE.d37a7e5c01", "decision":
    "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator":
    "claude-opus-5", "date": "2026-08-14", "notes": "Cohort review: no words shared,
    but a bronchial wash samples the bronchus, and the bronchus is where the strain
    lived. Grounding a lavage specimen to its anatomical site is the right habitat
    reading.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Frozen inventory projection
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: Source counts and taxon ranks/scores preserve source units; PREGO projections
    do not retain original pair-level citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/bacdive_source_taxa.tsv
  locator: Physical TSV rows 396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: '[{"row": 396, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash",
    "rank": "1", "taxon_id": "NCBITaxon:1122164", "taxon_label": "Legionella lansingensis
    DSM 19556 = ATCC 49751", "strain_count": "1", "corroborated_by": ""}}, {"row":
    397, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank":
    "2", "taxon_id": "NCBITaxon:1141647", "taxon_label": "Nocardia arizonensis", "strain_count":
    "1", "corroborated_by": ""}}, {"row": 398, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash",
    "rank": "3", "taxon_id": "NCBITaxon:1206729", "taxon_label": "Nocardia exalbida
    NBRC 100660", "strain_count": "1", "corroborated_by": ""}}, {"row": 399, "data":
    {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "4", "taxon_id":
    "NCBITaxon:1226751", "taxon_label": "Mycolicibacterium monacense DSM 44395", "strain_count":
    "1", "corroborated_by": ""}}, {"row": 400, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash",
    "rank": "5", "taxon_id": "NCBITaxon:1817", "taxon_label": "Nocardia", "strain_count":
    "1", "corroborated_by": ""}}, {"row": 401, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash",
    "rank": "6", "taxon_id": "NCBITaxon:1962118", "taxon_label": "Mycobacteroides
    abscessus subsp. massiliense", "strain_count": "1", "corroborated_by": ""}}, {"row":
    402, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank":
    "7", "taxon_id": "NCBITaxon:2074", "taxon_label": "Pseudonocardia autotrophica",
    "strain_count": "1", "corroborated_by": ""}}, {"row": 403, "data": {"bacdive_id":
    "bacdive.isolation_source:bronchial-wash", "rank": "8", "taxon_id": "NCBITaxon:222805",
    "taxon_label": "Mycobacterium intracellulare subsp. chimaera", "strain_count":
    "1", "corroborated_by": ""}}, {"row": 404, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash",
    "rank": "9", "taxon_id": "NCBITaxon:238", "taxon_label": "Elizabethkingia meningoseptica",
    "strain_count": "1", "corroborated_by": ""}}, {"row": 405, "data": {"bacdive_id":
    "bacdive.isolation_source:bronchial-wash", "rank": "10", "taxon_id": "NCBITaxon:28087",
    "taxon_label": "Legionella sainthelensi", "strain_count": "1", "corroborated_by":
    ""}}, {"row": 406, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash",
    "rank": "11", "taxon_id": "NCBITaxon:286804", "taxon_label": "Segniliparus rugosus",
    "strain_count": "1", "corroborated_by": ""}}, {"row": 407, "data": {"bacdive_id":
    "bacdive.isolation_source:bronchial-wash", "rank": "12", "taxon_id": "NCBITaxon:341199",
    "taxon_label": "Nocardia kroppenstedtii", "strain_count": "1", "corroborated_by":
    ""}}, {"row": 408, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash",
    "rank": "13", "taxon_id": "NCBITaxon:480035", "taxon_label": "Nocardia wallacei",
    "strain_count": "1", "corroborated_by": ""}}, {"row": 409, "data": {"bacdive_id":
    "bacdive.isolation_source:bronchial-wash", "rank": "14", "taxon_id": "NCBITaxon:524884",
    "taxon_label": "Saccharopolyspora rosea", "strain_count": "1", "corroborated_by":
    ""}}, {"row": 410, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash",
    "rank": "15", "taxon_id": "NCBITaxon:72407", "taxon_label": "Klebsiella pneumoniae
    subsp. pneumoniae", "strain_count": "1", "corroborated_by": ""}}, {"row": 411,
    "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash", "rank": "16",
    "taxon_id": "NCBITaxon:747", "taxon_label": "Pasteurella multocida", "strain_count":
    "1", "corroborated_by": ""}}, {"row": 412, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash",
    "rank": "17", "taxon_id": "NCBITaxon:756689", "taxon_label": "Nocardia amikacinitolerans",
    "strain_count": "1", "corroborated_by": ""}}, {"row": 413, "data": {"bacdive_id":
    "bacdive.isolation_source:bronchial-wash", "rank": "18", "taxon_id": "NCBITaxon:912594",
    "taxon_label": "Mycolicibacterium iranicum", "strain_count": "1", "corroborated_by":
    ""}}]'
  snapshot_sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
- evidence_id: ET6
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: Physical TSV rows 52
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: '[{"row": 52, "data": {"subject_label": "Bronchial-wash", "subject_label_normalized":
    "bronchial wash", "object_id": "UBERON:0002185", "object_label": "bronchus", "object_source":
    "UBERON", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification":
    "semapv:ManualMappingCuration", "curator": "manual_review", "source_dataset":
    "bacdive", "verified_date": "2026-05-02"}}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: ET7
  kind: database
  reference: data/raw/bacdive_isolation_sources.tsv
  locator: Physical TSV rows 119
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: '[{"row": 119, "data": {"bacdive_id": "bacdive.isolation_source:bronchial-wash",
    "label": "Bronchial-wash", "source_slug": "bronchial-wash", "strain_count": "18",
    "taxon_count": "18"}}]'
  snapshot_sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 11020,11345
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: '[{"row": 11020, "data": {"subject": "UBERON:0000117", "predicate": "rdfs:subClassOf",
    "object": "UBERON:0000025"}}, {"row": 11345, "data": {"subject": "UBERON:0002185",
    "predicate": "rdfs:subClassOf", "object": "UBERON:0000117"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET9
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 12902,13125
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: '[{"row": 12902, "data": {"term_id": "UBERON:0000117", "ontology": "UBERON",
    "label": "respiratory tube", "definition": "A tube in the respiratory system.
    Examples: bronchus, bronchiole, trachea.", "synonyms": "airway|respiratory conducting
    tube|segment of tracheobronchial tree|tracheobronchial tree segment", "deprecated":
    "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row": 13125, "data":
    {"term_id": "UBERON:0002185", "ontology": "UBERON", "label": "bronchus", "definition":
    "The upper conducting airways of the lung; these airways arise from the terminus
    of the trachea.", "synonyms": "bronchi|bronchial tissue|bronchial trunk", "deprecated":
    "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET10
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 1553
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: '[{"row": 1553, "data": {"identifier": "habitatmech:BACDIVE.d37a7e5c01",
    "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-14", "notes": "Cohort review:
    no words shared, but a bronchial wash samples the bronchus, and the bronchus is
    where the strain lived. Grounding a lavage specimen to its anatomical site is
    the right habitat reading.", "review_depth": "ITEM", "category": "", "relation":
    ""}}]'
  snapshot_sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20260922T142857Z-bronchus.md
  locator: Findings and recommended edits; historical lead
  accessed_at: '2026-10-15T16:56:03Z'
  support: supports
  summary: Legacy conclusions were compared with current target and primary evidence.
    No formal predecessor or automatic native-status requirement is inferred.
  snapshot_sha256: 16a35fa1f4fc60aa41fa23696d9240d66d3d33a18cf2c98643a1e12065f766e4
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
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002185
  locator: UBERON_0002185.json
  accessed_at: '2026-10-15T16:34:30Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0002185",
    "label": "bronchus", "is_obsolete": false, "description": ["The upper conducting
    airways of the lung; these airways arise from the terminus of the trachea."]}'
  snapshot_sha256: 2c4ed6adb27738ca7592f153e9364906adfef2431835e9aa966afb0b54eb09db
- evidence_id: EX5
  kind: database
  reference: https://bacdive.dsmz.de/isolation-sources
  locator: bacdive-isolation.html
  accessed_at: '2026-10-15T16:44:15Z'
  support: context_only
  summary: Current BacDive isolation-source browser contains Bovinae (Cow, Cattle)
    and Bronchial wash categories. It is a vocabulary witness, not a census of the
    frozen strain membership or proof of cattle-only scope.
  snapshot_sha256: 60f9932f434230027051edf3e35a6e3af4d52d2812eda2e7088ea9228ffef9de
- evidence_id: EX6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Legionella%20lansingensis%22%20AND%20%22species%22&format=json&resultType=core&pageSize=20
  locator: paper-lansingensis.json
  accessed_at: '2026-10-15T16:44:09Z'
  support: context_only
  summary: 'Primary species-description abstract PMID:1401005, DOI:10.1128/JCM.30.9.2398-2401.1992:
    strain1677-MI-H (ATCC49751) was isolated from bronchoscopy washings. Supports
    the sampled-site proxy, not histological residency or all eighteen BacDive observations.'
  snapshot_sha256: b4a3fcec9797534c2985de595306dc00d3625b628d6406a03b8b57329673010f
- evidence_id: EX7
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1117644,1122164,1131452,1131453,1131454,1131455,1133849,1141647,1157946,1162284,1162288,1177117,1189613,1193128,1199187,1206729,1214102,1220554,1226751,12455,1271862,1328,1329,1329902,1334,1348,1392869,147802,153721,1578,1590,1601,161879,1639,1658,1661,1679,1680,1682,1683,168808,169963,1718,1724,1796,1802,1817,184914,1886,1962118,197,198,2,205913,206,2074,2081794,222805,238,2701,28026,28087,286804,287,32002,32020,33,341199,36808,391904,439842,476,47885,480035,484020,51665,524884,653940,678,720,72407,731,747,756689,76759,82135,82348,83655,838,84107,912594,985762&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T16:34:33Z'
  support: context_only
  summary: 'All displayed IDs resolve in current NCBI Taxonomy. Preferred names and
    source labels were compared, without treating recognized historical aliases as
    wrong identities: [{"id": "NCBITaxon:1122164", "source": "BACDIVE", "label": "Legionella
    lansingensis DSM 19556 = ATCC 49751", "current_id": "1122164", "current_name":
    "Legionella lansingensis DSM 19556 = ATCC 49751", "rank": "strain", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1141647", "source": "BACDIVE",
    "label": "Nocardia arizonensis", "current_id": "1141647", "current_name": "Nocardia
    arizonensis", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:1206729", "source": "BACDIVE", "label": "Nocardia exalbida NBRC
    100660", "current_id": "1206729", "current_name": "Nocardia exalbida NBRC 100660",
    "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1226751",
    "source": "BACDIVE", "label": "Mycolicibacterium monacense DSM 44395", "current_id":
    "1226751", "current_name": "Mycolicibacterium monacense DSM 44395", "rank": "strain",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1817", "source":
    "BACDIVE", "label": "Nocardia", "current_id": "1817", "current_name": "Nocardia",
    "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1962118",
    "source": "BACDIVE", "label": "Mycobacteroides abscessus subsp. massiliense",
    "current_id": "1962118", "current_name": "Mycobacteroides abscessus subsp. massiliense",
    "rank": "subspecies", "direct_match": true, "recognized_alias": true}, {"id":
    "NCBITaxon:2074", "source": "BACDIVE", "label": "Pseudonocardia autotrophica",
    "current_id": "2074", "current_name": "Pseudonocardia autotrophica", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:222805", "source":
    "BACDIVE", "label": "Mycobacterium intracellulare subsp. chimaera", "current_id":
    "222805", "current_name": "Mycobacterium intracellulare subsp. chimaera", "rank":
    "subspecies", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:238",
    "source": "BACDIVE", "label": "Elizabethkingia meningoseptica", "current_id":
    "238", "current_name": "Elizabethkingia meningoseptica", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:28087", "source": "BACDIVE",
    "label": "Legionella sainthelensi", "current_id": "28087", "current_name": "Legionella
    sainthelensi", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:286804", "source": "BACDIVE", "label": "Segniliparus rugosus",
    "current_id": "286804", "current_name": "Segniliparus rugosus", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:341199", "source":
    "BACDIVE", "label": "Nocardia kroppenstedtii", "current_id": "341199", "current_name":
    "Nocardia kroppenstedtii", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:480035", "source": "BACDIVE", "label": "Nocardia wallacei",
    "current_id": "480035", "current_name": "Nocardia wallacei", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:524884", "source":
    "BACDIVE", "label": "Saccharopolyspora rosea", "current_id": "524884", "current_name":
    "Saccharopolyspora rosea", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:72407", "source": "BACDIVE", "label": "Klebsiella pneumoniae
    subsp. pneumoniae", "current_id": "72407", "current_name": "Klebsiella pneumoniae
    subsp. pneumoniae", "rank": "subspecies", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:747", "source": "BACDIVE", "label": "Pasteurella multocida",
    "current_id": "747", "current_name": "Pasteurella multocida", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:756689", "source":
    "BACDIVE", "label": "Nocardia amikacinitolerans", "current_id": "756689", "current_name":
    "Nocardia amikacinitolerans", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:912594", "source": "BACDIVE", "label": "Mycolicibacterium
    iranicum", "current_id": "912594", "current_name": "Mycolicibacterium iranicum",
    "rank": "species", "direct_match": true, "recognized_alias": true}]'
  snapshot_sha256: 249c661a92762c2362c9b3b8c3a0606ef71a9369fb2600df89f8ed7f06ace644
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e UBERON:0002185 -e bronchus -e bronchus
    -e habitatmech:BACDIVE.d37a7e5c01 curation history research reports data/raw build
    reviews
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
  outcome: supported
  summary: Uberon bronchus and its respiratory-tube superclass are supported. BacDive
    Bronchial-wash is intentionally a CLOSE sampled-site proxy with a RELATED source
    synonym, not exact lexical equivalence. The type-strain description of Legionella
    lansingensis ATCC49751 documents bronchoscopy washings. Eighteen STRAIN assertions
    and all eighteen displayed taxa remain source associations, not evidence that
    every isolate resided in bronchial tissue or was characteristic.
  target_ids:
  - UBERON:0002185
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
- assessment_id: A2
  area: quantity
  topic: Frozen counts, units, ranks, channels and scores
  outcome: supported
  summary: 'Every source assertion and displayed taxon was checked against its exact
    raw row. [{"source": "BACDIVE", "count": 18, "unit": "STRAIN"}]. Side-table biosample/study
    counts are not added to tree ORGANISM counts. Zero-count omission is not biological
    absence.'
  target_ids:
  - UBERON:0002185
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
  - EX7
- assessment_id: A3
  area: evidence
  topic: Scientific support and scope limits
  outcome: supported
  summary: Uberon bronchus and its respiratory-tube superclass are supported. BacDive
    Bronchial-wash is intentionally a CLOSE sampled-site proxy with a RELATED source
    synonym, not exact lexical equivalence. The type-strain description of Legionella
    lansingensis ATCC49751 documents bronchoscopy washings. Eighteen STRAIN assertions
    and all eighteen displayed taxa remain source associations, not evidence that
    every isolate resided in bronchial tissue or was characteristic.
  target_ids:
  - UBERON:0002185
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
- assessment_id: A4
  area: completeness
  topic: Status, optional content, triads and mechanisms
  outcome: supported
  summary: Actual routes reproduce CLOSE/REVIEWED. No environmental-parameter, causal-edge,
    discussion/dataset or is_characteristic=true assertion is present in this target.
    Optional absence and SEEDED status alone are not defects. Scientific review does
    not promote native status.
  target_ids:
  - UBERON:0002185
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
  - UBERON:0002185
  evidence_ids:
  - E1
  - ERULE
findings: []
actions: []
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
