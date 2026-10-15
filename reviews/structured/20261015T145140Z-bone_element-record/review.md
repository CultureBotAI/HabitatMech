# Record review: bone element (UBERON:0001474)

- Review: 20261015T145140Z-bone_element-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T14:34:19Z
- Finished UTC: 2026-10-15T14:51:40Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The Uberon whole bone-element identity, skeletal-element genus and broad FOODON bone-or-shell genus are supported. Its additional whole avian skeletal-system superclass is false for both part/whole and host scope. BacDive contributes 125 STRAIN assertions, a 96-taxon pool and 25 displayed taxa; GOLD contributes a separate zero-count path. Both source mappings are CLOSE and ITEM-reviewed, and their source labels correctly remain RELATED rather than exact synonyms.

## Scope And Provenance

Full scientific assessment of one exact target at b558fd561286d1fe3ba133784776f7be1f9f49fb.

Selection: One of the next 21 path-ordered unreviewed records, blood through bone marrow; this bundle assesses only this identifier.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base b558fd561286d1fe3ba133784776f7be1f9f49fb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0001474 | data/habitats/host_associated/bone_element.yaml | generated | bone element |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | UBERON:0001474 | Completed 2026-10-15T14:35:45Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bone_element.yaml |
| validate-strict | passed | True | UBERON:0001474 | Completed 2026-10-15T14:36:08Z. uv run python scripts/validate_strict.py data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml data/habitats/host_associated/bone_marrow__c1fc5dec.yaml<br>Validating 21 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      21<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | UBERON:0001474 | Completed 2026-10-15T14:36:40Z. No issues found<br>813 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | UBERON:0001474 | Completed 2026-10-15T14:36:43Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | UBERON:0001474 | Completed 2026-10-15T14:37:37Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | UBERON:0001474 | Completed 2026-10-15T14:37:45Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | UBERON:0001474 | Completed 2026-10-15T14:38:11Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | UBERON:0001474 | Completed 2026-10-15T14:39:21Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | UBERON:0001474 | Verified 2026-10-15T14:33:14Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38748091185 |

## Scientific And Domain Assessments

### Identity and hierarchy

identity: concern. Targets: UBERON:0001474.

The Uberon whole bone-element identity, skeletal-element genus and broad FOODON bone-or-shell genus are supported. Its additional whole avian skeletal-system superclass is false for both part/whole and host scope. BacDive contributes 125 STRAIN assertions, a 96-taxon pool and 25 displayed taxa; GOLD contributes a separate zero-count path. Both source mappings are CLOSE and ITEM-reviewed, and their source labels correctly remain RELATED rather than exact synonyms.

### Frozen source units, ranks and parameters

quantity: supported. Targets: UBERON:0001474.

Count/unit, first GOLD node, channel, score and displayed taxon ranks/labels reproduce exact source rows. Verification: [{"source": "BACDIVE", "count": 125, "unit": "STRAIN"}, {"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero counts are omitted, never interpreted as absence. Side-table biosamples/studies and MIxS slots are not added to tree ORGANISM counts.

### Scientific support and source limits

evidence: supported. Targets: UBERON:0001474.

The Uberon whole bone-element identity, skeletal-element genus and broad FOODON bone-or-shell genus are supported. Its additional whole avian skeletal-system superclass is false for both part/whole and host scope. BacDive contributes 125 STRAIN assertions, a 96-taxon pool and 25 displayed taxa; GOLD contributes a separate zero-count path. Both source mappings are CLOSE and ITEM-reviewed, and their source labels correctly remain RELATED rather than exact synonyms.

### Native status and optional assertions

completeness: supported. Targets: UBERON:0001474.

Executed routes reproduce CLOSE/REVIEWED. No causal edge or is_characteristic=true assertion is made. Optional absent fields and SEEDED status alone are not scientific defects; this review does not promote native status.

### Deterministic native gates

schema: supported. Targets: UBERON:0001474.

Schema, strict, history, provenance, 3,208-record reproduction, causal, term-request, configured-label and exact-baseline full QC checks passed; these prove fidelity, not biological truth.

## Findings

### F1: Containing anatomy is not a broader habitat class

major / open / confirmed; issue key: bone-element-context-parent.

Exclude only the exact GOLD source-path/expected-parent contributions habitatmech:GOLD.3756d4bb39. The Uberon whole bone-element identity, skeletal-element genus and broad FOODON bone-or-shell genus are supported. Its additional whole avian skeletal-system superclass is false for both part/whole and host scope. BacDive contributes 125 STRAIN assertions, a 96-taxon pool and 25 displayed taxa; GOLD contributes a separate zero-count path. Both source mappings are CLOSE and ITEM-reviewed, and their source labels correctly remain RELATED rather than exact synonyms. Preserve independent ontology genera, source mappings, counts, units, taxa and native status.

## Recommended Actions And Acceptance Checks

### ACT1

Exclude only the exact GOLD source-path/expected-parent contributions habitatmech:GOLD.3756d4bb39. The Uberon whole bone-element identity, skeletal-element genus and broad FOODON bone-or-shell genus are supported. Its additional whole avian skeletal-system superclass is false for both part/whole and host scope. BacDive contributes 125 STRAIN assertions, a 96-taxon pool and 25 displayed taxa; GOLD contributes a separate zero-count path. Both source mappings are CLOSE and ITEM-reviewed, and their source labels correctly remain RELATED rather than exact synonyms. Preserve independent ontology genera, source mappings, counts, units, taxa and native status. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bone_element.yaml; Entire target YAML | supports | Full target read, including every source attestation, taxon, parent, parameter and history entry. |
| ERULE | docs/CURATION.md; Strict ancestry and maintained-input ownership | supports | Parent means strictly broader, not containing organ, body or system. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation, EnvironmentalParameter, CharacteristicTaxon | supports | Source-to-record mapping contract; qualified parameters and observed associations are not universal conditions or characteristic presence. |
| ESEED | src/habitatmech/seed.py; Executed build_corpus and apply_decision routes | supports | Whole generated document equality verified; source-specific resolutions: [{"mint": "habitatmech:BACDIVE.16280b13f2", "automatic": {"identifier": "UBERON:0001474", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "bacdive_mapping_table", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0001474", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_bacdive_mapping_table", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:BACDIVE.16280b13f2", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}, {"mint": "habitatmech:GOLD.6296c1e38f", "automatic": {"identifier": "UBERON:0001474", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_synonym", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0001474", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_gold_leaf_synonym", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.6296c1e38f", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Source projection | supports | PREGO projects counts, scores, channels and ranked taxa without original pair citations. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 1904 | supports | [{"row": 1904, "data": {"canonical_path": "Host-associated &gt; Birds &gt; Skeletal system &gt; Bones", "ecosystem": "Host-associated", "ecosystem_category": "Birds", "ecosystem_type": "Skeletal system", "ecosystem_subtype": "Bones", "specific_ecosystem": "", "leaf_label": "Bones", "depth": "4", "gold_node_count": "2", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7479&#124;gold.ecosystem:7480"}}] |
| ET6 | data/raw/bacdive_source_taxa.tsv; Physical TSV rows 296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320 | supports | [{"row": 296, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "1", "taxon_id": "NCBITaxon:504", "taxon_label": "Kingella kingae", "strain_count": "8", "corroborated_by": ""}}, {"row": 297, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "2", "taxon_id": "NCBITaxon:1280", "taxon_label": "Staphylococcus aureus", "strain_count": "3", "corroborated_by": ""}}, {"row": 298, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "3", "taxon_id": "NCBITaxon:1328", "taxon_label": "Streptococcus anginosus", "strain_count": "3", "corroborated_by": ""}}, {"row": 299, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "4", "taxon_id": "NCBITaxon:1659", "taxon_label": "Actinomyces israelii", "strain_count": "3", "corroborated_by": ""}}, {"row": 300, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "5", "taxon_id": "NCBITaxon:33028", "taxon_label": "Staphylococcus saccharolyticus", "strain_count": "3", "corroborated_by": ""}}, {"row": 301, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "6", "taxon_id": "NCBITaxon:46124", "taxon_label": "Granulicatella adiacens", "strain_count": "3", "corroborated_by": ""}}, {"row": 302, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "7", "taxon_id": "NCBITaxon:1402", "taxon_label": "Bacillus licheniformis", "strain_count": "2", "corroborated_by": ""}}, {"row": 303, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "8", "taxon_id": "NCBITaxon:1747", "taxon_label": "Cutibacterium acnes", "strain_count": "2", "corroborated_by": ""}}, {"row": 304, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "9", "taxon_id": "NCBITaxon:29318", "taxon_label": "Winkia neuii subsp. anitrata", "strain_count": "2", "corroborated_by": ""}}, {"row": 305, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "10", "taxon_id": "NCBITaxon:29394", "taxon_label": "Dolosigranulum pigrum", "strain_count": "2", "corroborated_by": ""}}, {"row": 306, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "11", "taxon_id": "NCBITaxon:33010", "taxon_label": "Cutibacterium avidum", "strain_count": "2", "corroborated_by": ""}}, {"row": 307, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "12", "taxon_id": "NCBITaxon:38284", "taxon_label": "Corynebacterium accolens", "strain_count": "2", "corroborated_by": ""}}, {"row": 308, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "13", "taxon_id": "NCBITaxon:43770", "taxon_label": "Corynebacterium striatum", "strain_count": "2", "corroborated_by": ""}}, {"row": 309, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "14", "taxon_id": "NCBITaxon:47920", "taxon_label": "Acidovorax delafieldii", "strain_count": "2", "corroborated_by": ""}}, {"row": 310, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "15", "taxon_id": "NCBITaxon:598660", "taxon_label": "Corynebacterium pyruviciproducens", "strain_count": "2", "corroborated_by": ""}}, {"row": 311, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "16", "taxon_id": "NCBITaxon:66228", "taxon_label": "Gleimia europaea", "strain_count": "2", "corroborated_by": ""}}, {"row": 312, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "17", "taxon_id": "NCBITaxon:717", "taxon_label": "Actinobacillus capsulatus", "strain_count": "2", "corroborated_by": ""}}, {"row": 313, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "18", "taxon_id": "NCBITaxon:732", "taxon_label": "Aggregatibacter aphrophilus", "strain_count": "2", "corroborated_by": ""}}, {"row": 314, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "19", "taxon_id": "NCBITaxon:102684", "taxon_label": "Streptococcus infantarius", "strain_count": "1", "corroborated_by": ""}}, {"row": 315, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "20", "taxon_id": "NCBITaxon:1121364", "taxon_label": "Corynebacterium massiliense DSM 45435", "strain_count": "1", "corroborated_by": ""}}, {"row": 316, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "21", "taxon_id": "NCBITaxon:1219017", "taxon_label": "Rhodococcus jostii NBRC 16295", "strain_count": "1", "corroborated_by": ""}}, {"row": 317, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "22", "taxon_id": "NCBITaxon:123899", "taxon_label": "Bordetella trematum", "strain_count": "1", "corroborated_by": ""}}, {"row": 318, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "23", "taxon_id": "NCBITaxon:1265311", "taxon_label": "Mycobacterium arosiense ATCC BAA-1401 = DSM 45069", "strain_count": "1", "corroborated_by": ""}}, {"row": 319, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "24", "taxon_id": "NCBITaxon:1283", "taxon_label": "Staphylococcus haemolyticus", "strain_count": "1", "corroborated_by": ""}}, {"row": 320, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "25", "taxon_id": "NCBITaxon:1296", "taxon_label": "Mammaliicoccus sciuri", "strain_count": "1", "corroborated_by": ""}}] |
| ET7 | data/raw/isolation_source_groundings.tsv; Physical TSV rows 46 | supports | [{"row": 46, "data": {"subject_label": "Bone", "subject_label_normalized": "bone", "object_id": "UBERON:0001474", "object_label": "bone element", "object_source": "UBERON", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification": "semapv:LexicalMatching", "curator": "ols4_auto", "source_dataset": "bacdive", "verified_date": "2026-05-01"}}] |
| ET8 | data/raw/bacdive_isolation_sources.tsv; Physical TSV rows 66 | supports | [{"row": 66, "data": {"bacdive_id": "bacdive.isolation_source:bone", "label": "Bone", "source_slug": "bone", "strain_count": "125", "taxon_count": "96"}}] |
| ET9 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 9042,11204,11205,11495 | supports | [{"row": 9042, "data": {"subject": "FOODON:03420168", "predicate": "rdfs:subClassOf", "object": "FOODON:03420122"}}, {"row": 11204, "data": {"subject": "UBERON:0001474", "predicate": "rdfs:subClassOf", "object": "FOODON:03420168"}}, {"row": 11205, "data": {"subject": "UBERON:0001474", "predicate": "rdfs:subClassOf", "object": "UBERON:0004765"}}, {"row": 11495, "data": {"subject": "UBERON:0004765", "predicate": "rdfs:subClassOf", "object": "UBERON:0000062"}}] |
| ET10 | data/raw/ontology_terms.tsv; Physical TSV rows 10714,13040,13237 | supports | [{"row": 10714, "data": {"term_id": "FOODON:03420168", "ontology": "FOODON", "label": "bone or shell", "definition": "Bone (endoskeleton) or shell (exoskeleton) of animals, or any part thereof.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row": 13040, "data": {"term_id": "UBERON:0001474", "ontology": "UBERON", "label": "bone element", "definition": "Skeletal element that is composed of bone tissue.", "synonyms": "bone&#124;bone organ&#124;bones", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 13237, "data": {"term_id": "UBERON:0004765", "ontology": "UBERON", "label": "skeletal element", "definition": "Organ consisting of skeletal tissue. Encompasses whole bones, fused bones, cartilaginious elements, teeth, dermal denticles.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| ET11 | curation/decisions.tsv; Physical TSV rows 21,609 | supports | [{"row": 21, "data": {"identifier": "habitatmech:BACDIVE.16280b13f2", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": ""}}, {"row": 609, "data": {"identifier": "habitatmech:GOLD.6296c1e38f", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP12 | data/habitats/host_associated/skeletal_system__5ac43c2f.yaml; Full parent, scope context only | supports | {"identifier": "habitatmech:GOLD.3756d4bb39", "label": "Skeletal system", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001434", "habitatmech:GOLD.47e603cf4f"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7476", "source_label": "Skeletal system", "source_path": "Host-associated &gt; Birds &gt; Skeletal system", "mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03420168/graph; FOODON_03420168-graph.json | context_only | Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/FOODON_03420168", "target": "http://purl.obolibrary.org/obo/FOODON_03420122", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03420168; FOODON_03420168.json | context_only | Inspected current ID, label, active status and definition for scope; {"obo_id": "FOODON:03420168", "label": "bone or shell", "is_obsolete": false} |
| EX3 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12408549/fullTextXML; PMC12408549.xml | context_only | Primary abstract, DOI:10.3389/fbioe.2025.1617285, PMID:40918439: human bone samples were experimentally inoculated with S. aureus or S. epidermidis and compared with uninfected controls. This is bounded experimental bone-site evidence, not natural prevalence or reidentification of 125 BacDive strains. |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434/graph; UBERON_0001434-graph.json | context_only | Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0011216", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0002204", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0004288", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434", "target": "http://purl.obolibrary.org/obo/UBERON_0004770", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}] |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434; UBERON_0001434.json | context_only | Inspected current ID, label, active status and definition for scope; {"obo_id": "UBERON:0001434", "label": "skeletal system", "is_obsolete": false} |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001474/graph; UBERON_0001474-graph.json | context_only | Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001474", "target": "http://purl.obolibrary.org/obo/UBERON_0004765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001474", "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001474", "target": "http://purl.obolibrary.org/obo/UBERON_0001434", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001474", "target": "http://purl.obolibrary.org/obo/UBERON_0002481", "uri": "http://purl.obolibrary.org/obo/RO_0002473", "label": "composed primarily of"}] |
| EX7 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001474; UBERON_0001474.json | context_only | Inspected current ID, label, active status and definition for scope; {"obo_id": "UBERON:0001474", "label": "bone element", "is_obsolete": false} |
| EX8 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0004765/graph; UBERON_0004765-graph.json | context_only | Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0004765", "target": "http://purl.obolibrary.org/obo/UBERON_0000062", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0004765", "target": "http://purl.obolibrary.org/obo/UBERON_0001434", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0004765; UBERON_0004765.json | context_only | Inspected current ID, label, active status and definition for scope; {"obo_id": "UBERON:0004765", "label": "skeletal element", "is_obsolete": false} |
| EX10 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1000935,1000936,1000937,1000938,1000939,1002339,1003201,1005704,1005705,1008452,1008453,102684,1028806,1032071,1035187,1035189,103855,1051654,106654,1069609,1069614,1069618,1069621,1069623,1069627,1073382,1094555,1120932,1121020,1121098,1121364,1122173,1122921,1122925,1122931,1122988,1123034,1219017,123899,1265311,1267000,1280,1283,1296,1304,1322345,1328,1329902,1336208,1341644,1402,1408438,1408440,1408452,1415606,1448136,147802,154288,1578,1601,1659,168808,1707330,171549,1718,1747,186802,203119,214092,220341,273075,287,29318,29394,306537,316407,32002,33010,33028,354242,38284,43770,46124,47885,47920,504,51665,525919,598660,61645,66228,717,732,76759,83655&amp;retmode=xml; taxonomy.xml | context_only | Every displayed ID was resolved, including current merged aliases; source labels are preserved, not falsely certified current preferred names. [{"id": "NCBITaxon:504", "source": "BACDIVE", "label": "Kingella kingae", "current_id": "504", "current_name": "Kingella kingae", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1280", "source": "BACDIVE", "label": "Staphylococcus aureus", "current_id": "1280", "current_name": "Staphylococcus aureus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1328", "source": "BACDIVE", "label": "Streptococcus anginosus", "current_id": "1328", "current_name": "Streptococcus anginosus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1659", "source": "BACDIVE", "label": "Actinomyces israelii", "current_id": "1659", "current_name": "Actinomyces israelii", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:33028", "source": "BACDIVE", "label": "Staphylococcus saccharolyticus", "current_id": "33028", "current_name": "Staphylococcus saccharolyticus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:46124", "source": "BACDIVE", "label": "Granulicatella adiacens", "current_id": "46124", "current_name": "Granulicatella adiacens", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1402", "source": "BACDIVE", "label": "Bacillus licheniformis", "current_id": "1402", "current_name": "Bacillus licheniformis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1747", "source": "BACDIVE", "label": "Cutibacterium acnes", "current_id": "1747", "current_name": "Cutibacterium acnes", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:29318", "source": "BACDIVE", "label": "Winkia neuii subsp. anitrata", "current_id": "29318", "current_name": "Winkia neuii subsp. anitrata", "rank": "subspecies", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:29394", "source": "BACDIVE", "label": "Dolosigranulum pigrum", "current_id": "29394", "current_name": "Dolosigranulum pigrum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:33010", "source": "BACDIVE", "label": "Cutibacterium avidum", "current_id": "33010", "current_name": "Cutibacterium avidum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:38284", "source": "BACDIVE", "label": "Corynebacterium accolens", "current_id": "38284", "current_name": "Corynebacterium accolens", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:43770", "source": "BACDIVE", "label": "Corynebacterium striatum", "current_id": "43770", "current_name": "Corynebacterium striatum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:47920", "source": "BACDIVE", "label": "Acidovorax delafieldii", "current_id": "47920", "current_name": "Acidovorax delafieldii", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:598660", "source": "BACDIVE", "label": "Corynebacterium pyruviciproducens", "current_id": "598660", "current_name": "Corynebacterium pyruviciproducens", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:66228", "source": "BACDIVE", "label": "Gleimia europaea", "current_id": "66228", "current_name": "Gleimia europaea", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:717", "source": "BACDIVE", "label": "Actinobacillus capsulatus", "current_id": "717", "current_name": "Actinobacillus capsulatus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:732", "source": "BACDIVE", "label": "Aggregatibacter aphrophilus", "current_id": "732", "current_name": "Aggregatibacter aphrophilus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:102684", "source": "BACDIVE", "label": "Streptococcus infantarius", "current_id": "102684", "current_name": "Streptococcus infantarius", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1121364", "source": "BACDIVE", "label": "Corynebacterium massiliense DSM 45435", "current_id": "1121364", "current_name": "Corynebacterium massiliense DSM 45435", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1219017", "source": "BACDIVE", "label": "Rhodococcus jostii NBRC 16295", "current_id": "1219017", "current_name": "Rhodococcus jostii NBRC 16295", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:123899", "source": "BACDIVE", "label": "Bordetella trematum", "current_id": "123899", "current_name": "Bordetella trematum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1265311", "source": "BACDIVE", "label": "Mycobacterium arosiense ATCC BAA-1401 = DSM 45069", "current_id": "1265311", "current_name": "Mycobacterium arosiense ATCC BAA-1401 = DSM 45069", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1283", "source": "BACDIVE", "label": "Staphylococcus haemolyticus", "current_id": "1283", "current_name": "Staphylococcus haemolyticus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1296", "source": "BACDIVE", "label": "Mammaliicoccus sciuri", "current_id": "1296", "current_name": "Mammaliicoccus sciuri", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local inputs and review archive; rg --no-ignore --hidden -l -F -e UBERON:0001474 -e 'bone element' -e bone_element -e habitatmech:BACDIVE.16280b13f2 -e habitatmech:GOLD.6296c1e38f curation history research reports data/raw build reviews | context_only | Exact TSV parsing and ignored-inclusive target/mint/label/slug search establish the bounded row inventory. Structured archive traversal found no predecessor; not every broad textual lead was inspected. |

## Limits And Additional Notes

- Every historical specimen and original source pair has not been independently reidentified. Source counts are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 no-adapter pairs and taxon labels; independent current NCBI lookup is recorded for displayed taxa.
- Full QC evidence is a verified remote run at the exact captured baseline, not a newly executed local QC. New review outputs require subsequent publication checks.
- iModulonDB is not applicable: no gene, regulator or expression-module assertion is made. No paid research was used.
- Captured hashes were rechecked against both working bytes and the exact Git base; no scientific inputs were silently refreshed.
- Ignored-inclusive searches and parsed structured archive found no prior structured observation of this exact target. Legacy Markdown is a lead, not structured lineage.
- This immutable observation precedes separately authorized curation and does not claim repairs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T145140Z-bone_element-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: bone element (UBERON:0001474)'
started_at: '2026-10-15T14:34:19Z'
finished_at: '2026-10-15T14:51:40Z'
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
summary: The Uberon whole bone-element identity, skeletal-element genus and broad
  FOODON bone-or-shell genus are supported. Its additional whole avian skeletal-system
  superclass is false for both part/whole and host scope. BacDive contributes 125
  STRAIN assertions, a 96-taxon pool and 25 displayed taxa; GOLD contributes a separate
  zero-count path. Both source mappings are CLOSE and ITEM-reviewed, and their source
  labels correctly remain RELATED rather than exact synonyms.
source:
  git_revision: b558fd561286d1fe3ba133784776f7be1f9f49fb
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
    sha256: 1e1c576daaee3c5055437ef42ba46363f5776210eef2e4182fe6fd3c87a7fe4d
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
  - path: data/habitats/host_associated/bone_element.yaml
    sha256: 77bec5b6160aedb9ea0247e96c76be7759fc0b054b71ac8ab9bc6187dffeb94b
    role: target
  - path: data/habitats/host_associated/skeletal_system__5ac43c2f.yaml
    sha256: c3948cbcc41d72ce4a43d816d605f12fb6002d5d5f204a8a7cdfdffa55aaf8d3
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
  - path: reports/yaml_record_review/20260922T062132Z-bone_element.md
    sha256: fdc47194fecff6574bbdf6e0df450e53aef3033ecaddd8ebb0e21efc583f4cc0
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
- target_id: UBERON:0001474
  path: data/habitats/host_associated/bone_element.yaml
  label: bone element
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
  description: Full scientific assessment of one exact target at b558fd561286d1fe3ba133784776f7be1f9f49fb.
  selection: One of the next 21 path-ordered unreviewed records, blood through bone
    marrow; this bundle assesses only this identifier.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0001474
  exclusions:
  - target: Other records and export products
    reason: Parent context is not additional coverage. SSSOM/KGX readiness is not
      certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bone_element.yaml
  exit_code: 0
  target_ids:
  - UBERON:0001474
  summary: "Completed 2026-10-15T14:35:45Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bone_element.yaml"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml
    data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml
    data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml
    data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml
    data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml
    data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml
    data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml
    data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml
    data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml
    data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml
    data/habitats/host_associated/bone_marrow__c1fc5dec.yaml
  exit_code: 0
  target_ids:
  - UBERON:0001474
  summary: "Completed 2026-10-15T14:36:08Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml\
    \ data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml\
    \ data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml\
    \ data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml\
    \ data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml\
    \ data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml\
    \ data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml\
    \ data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml\
    \ data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml\
    \ data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml\
    \ data/habitats/host_associated/bone_marrow__c1fc5dec.yaml\nValidating 21 files\
    \ with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      21\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - UBERON:0001474
  summary: 'Completed 2026-10-15T14:36:40Z. No issues found

    813 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - UBERON:0001474
  summary: "Completed 2026-10-15T14:36:43Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - UBERON:0001474
  summary: "Completed 2026-10-15T14:37:37Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - UBERON:0001474
  summary: "Completed 2026-10-15T14:37:45Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - UBERON:0001474
  summary: "Completed 2026-10-15T14:38:11Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - UBERON:0001474
  summary: "Completed 2026-10-15T14:39:21Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: CCI
  name: Exact-baseline full QC
  status: passed
  required: true
  command: gh run view 38748091185 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - UBERON:0001474
  summary: Verified 2026-10-15T14:33:14Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38748091185
  scope_note: Exact unchanged scientific input baseline; these new review outputs
    require later checks.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bone_element.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: Full target read, including every source attestation, taxon, parent, parameter
    and history entry.
  snapshot_sha256: 77bec5b6160aedb9ea0247e96c76be7759fc0b054b71ac8ab9bc6187dffeb94b
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict ancestry and maintained-input ownership
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: Parent means strictly broader, not containing organ, body or system.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation, EnvironmentalParameter, CharacteristicTaxon
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: Source-to-record mapping contract; qualified parameters and observed associations
    are not universal conditions or characteristic presence.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed build_corpus and apply_decision routes
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: 'Whole generated document equality verified; source-specific resolutions:
    [{"mint": "habitatmech:BACDIVE.16280b13f2", "automatic": {"identifier": "UBERON:0001474",
    "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "bacdive_mapping_table",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "UBERON:0001474", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch",
    "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "curated_review_of_bacdive_mapping_table", "category": null, "reviewed": true,
    "decision": {"identifier": "habitatmech:BACDIVE.16280b13f2", "decision": "REVIEW",
    "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5",
    "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested
    by more than one independent vocabulary, and this source''s label or path was
    read against the record''s ontology term to check the merge is right. It agrees.
    Source concepts in the same pass whose labels did not agree were re-decided rather
    than endorsed; see the pass''s other decisions of the same date.", "review_depth":
    "ITEM", "category": "", "relation": "parent"}}}, {"mint": "habitatmech:GOLD.6296c1e38f",
    "automatic": {"identifier": "UBERON:0001474", "grounding_status": "CLOSE", "mapping_predicate":
    "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs":
    [], "route": "gold_leaf_synonym", "category": null, "reviewed": false, "decision":
    null}, "final": {"identifier": "UBERON:0001474", "grounding_status": "CLOSE",
    "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": [], "route": "curated_review_of_gold_leaf_synonym", "category":
    null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.6296c1e38f",
    "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review
    pass: this record is attested by more than one independent vocabulary, and this
    source''s label or path was read against the record''s ontology term to check
    the merge is right. It agrees. Source concepts in the same pass whose labels did
    not agree were re-decided rather than endorsed; see the pass''s other decisions
    of the same date.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source projection
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: PREGO projects counts, scores, channels and ranked taxa without original
    pair citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 1904
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: '[{"row": 1904, "data": {"canonical_path": "Host-associated > Birds > Skeletal
    system > Bones", "ecosystem": "Host-associated", "ecosystem_category": "Birds",
    "ecosystem_type": "Skeletal system", "ecosystem_subtype": "Bones", "specific_ecosystem":
    "", "leaf_label": "Bones", "depth": "4", "gold_node_count": "2", "organism_count":
    "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids":
    "gold.ecosystem:7479|gold.ecosystem:7480"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/bacdive_source_taxa.tsv
  locator: Physical TSV rows 296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: '[{"row": 296, "data": {"bacdive_id": "bacdive.isolation_source:bone",
    "rank": "1", "taxon_id": "NCBITaxon:504", "taxon_label": "Kingella kingae", "strain_count":
    "8", "corroborated_by": ""}}, {"row": 297, "data": {"bacdive_id": "bacdive.isolation_source:bone",
    "rank": "2", "taxon_id": "NCBITaxon:1280", "taxon_label": "Staphylococcus aureus",
    "strain_count": "3", "corroborated_by": ""}}, {"row": 298, "data": {"bacdive_id":
    "bacdive.isolation_source:bone", "rank": "3", "taxon_id": "NCBITaxon:1328", "taxon_label":
    "Streptococcus anginosus", "strain_count": "3", "corroborated_by": ""}}, {"row":
    299, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "4", "taxon_id":
    "NCBITaxon:1659", "taxon_label": "Actinomyces israelii", "strain_count": "3",
    "corroborated_by": ""}}, {"row": 300, "data": {"bacdive_id": "bacdive.isolation_source:bone",
    "rank": "5", "taxon_id": "NCBITaxon:33028", "taxon_label": "Staphylococcus saccharolyticus",
    "strain_count": "3", "corroborated_by": ""}}, {"row": 301, "data": {"bacdive_id":
    "bacdive.isolation_source:bone", "rank": "6", "taxon_id": "NCBITaxon:46124", "taxon_label":
    "Granulicatella adiacens", "strain_count": "3", "corroborated_by": ""}}, {"row":
    302, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "7", "taxon_id":
    "NCBITaxon:1402", "taxon_label": "Bacillus licheniformis", "strain_count": "2",
    "corroborated_by": ""}}, {"row": 303, "data": {"bacdive_id": "bacdive.isolation_source:bone",
    "rank": "8", "taxon_id": "NCBITaxon:1747", "taxon_label": "Cutibacterium acnes",
    "strain_count": "2", "corroborated_by": ""}}, {"row": 304, "data": {"bacdive_id":
    "bacdive.isolation_source:bone", "rank": "9", "taxon_id": "NCBITaxon:29318", "taxon_label":
    "Winkia neuii subsp. anitrata", "strain_count": "2", "corroborated_by": ""}},
    {"row": 305, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "10",
    "taxon_id": "NCBITaxon:29394", "taxon_label": "Dolosigranulum pigrum", "strain_count":
    "2", "corroborated_by": ""}}, {"row": 306, "data": {"bacdive_id": "bacdive.isolation_source:bone",
    "rank": "11", "taxon_id": "NCBITaxon:33010", "taxon_label": "Cutibacterium avidum",
    "strain_count": "2", "corroborated_by": ""}}, {"row": 307, "data": {"bacdive_id":
    "bacdive.isolation_source:bone", "rank": "12", "taxon_id": "NCBITaxon:38284",
    "taxon_label": "Corynebacterium accolens", "strain_count": "2", "corroborated_by":
    ""}}, {"row": 308, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank":
    "13", "taxon_id": "NCBITaxon:43770", "taxon_label": "Corynebacterium striatum",
    "strain_count": "2", "corroborated_by": ""}}, {"row": 309, "data": {"bacdive_id":
    "bacdive.isolation_source:bone", "rank": "14", "taxon_id": "NCBITaxon:47920",
    "taxon_label": "Acidovorax delafieldii", "strain_count": "2", "corroborated_by":
    ""}}, {"row": 310, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank":
    "15", "taxon_id": "NCBITaxon:598660", "taxon_label": "Corynebacterium pyruviciproducens",
    "strain_count": "2", "corroborated_by": ""}}, {"row": 311, "data": {"bacdive_id":
    "bacdive.isolation_source:bone", "rank": "16", "taxon_id": "NCBITaxon:66228",
    "taxon_label": "Gleimia europaea", "strain_count": "2", "corroborated_by": ""}},
    {"row": 312, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "17",
    "taxon_id": "NCBITaxon:717", "taxon_label": "Actinobacillus capsulatus", "strain_count":
    "2", "corroborated_by": ""}}, {"row": 313, "data": {"bacdive_id": "bacdive.isolation_source:bone",
    "rank": "18", "taxon_id": "NCBITaxon:732", "taxon_label": "Aggregatibacter aphrophilus",
    "strain_count": "2", "corroborated_by": ""}}, {"row": 314, "data": {"bacdive_id":
    "bacdive.isolation_source:bone", "rank": "19", "taxon_id": "NCBITaxon:102684",
    "taxon_label": "Streptococcus infantarius", "strain_count": "1", "corroborated_by":
    ""}}, {"row": 315, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank":
    "20", "taxon_id": "NCBITaxon:1121364", "taxon_label": "Corynebacterium massiliense
    DSM 45435", "strain_count": "1", "corroborated_by": ""}}, {"row": 316, "data":
    {"bacdive_id": "bacdive.isolation_source:bone", "rank": "21", "taxon_id": "NCBITaxon:1219017",
    "taxon_label": "Rhodococcus jostii NBRC 16295", "strain_count": "1", "corroborated_by":
    ""}}, {"row": 317, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank":
    "22", "taxon_id": "NCBITaxon:123899", "taxon_label": "Bordetella trematum", "strain_count":
    "1", "corroborated_by": ""}}, {"row": 318, "data": {"bacdive_id": "bacdive.isolation_source:bone",
    "rank": "23", "taxon_id": "NCBITaxon:1265311", "taxon_label": "Mycobacterium arosiense
    ATCC BAA-1401 = DSM 45069", "strain_count": "1", "corroborated_by": ""}}, {"row":
    319, "data": {"bacdive_id": "bacdive.isolation_source:bone", "rank": "24", "taxon_id":
    "NCBITaxon:1283", "taxon_label": "Staphylococcus haemolyticus", "strain_count":
    "1", "corroborated_by": ""}}, {"row": 320, "data": {"bacdive_id": "bacdive.isolation_source:bone",
    "rank": "25", "taxon_id": "NCBITaxon:1296", "taxon_label": "Mammaliicoccus sciuri",
    "strain_count": "1", "corroborated_by": ""}}]'
  snapshot_sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
- evidence_id: ET7
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: Physical TSV rows 46
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: '[{"row": 46, "data": {"subject_label": "Bone", "subject_label_normalized":
    "bone", "object_id": "UBERON:0001474", "object_label": "bone element", "object_source":
    "UBERON", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification":
    "semapv:LexicalMatching", "curator": "ols4_auto", "source_dataset": "bacdive",
    "verified_date": "2026-05-01"}}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: ET8
  kind: database
  reference: data/raw/bacdive_isolation_sources.tsv
  locator: Physical TSV rows 66
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: '[{"row": 66, "data": {"bacdive_id": "bacdive.isolation_source:bone", "label":
    "Bone", "source_slug": "bone", "strain_count": "125", "taxon_count": "96"}}]'
  snapshot_sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
- evidence_id: ET9
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 9042,11204,11205,11495
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: '[{"row": 9042, "data": {"subject": "FOODON:03420168", "predicate": "rdfs:subClassOf",
    "object": "FOODON:03420122"}}, {"row": 11204, "data": {"subject": "UBERON:0001474",
    "predicate": "rdfs:subClassOf", "object": "FOODON:03420168"}}, {"row": 11205,
    "data": {"subject": "UBERON:0001474", "predicate": "rdfs:subClassOf", "object":
    "UBERON:0004765"}}, {"row": 11495, "data": {"subject": "UBERON:0004765", "predicate":
    "rdfs:subClassOf", "object": "UBERON:0000062"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET10
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 10714,13040,13237
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: '[{"row": 10714, "data": {"term_id": "FOODON:03420168", "ontology": "FOODON",
    "label": "bone or shell", "definition": "Bone (endoskeleton) or shell (exoskeleton)
    of animals, or any part thereof.", "synonyms": "", "deprecated": "", "directly_referenced":
    "FALSE", "label_only": "FALSE"}}, {"row": 13040, "data": {"term_id": "UBERON:0001474",
    "ontology": "UBERON", "label": "bone element", "definition": "Skeletal element
    that is composed of bone tissue.", "synonyms": "bone|bone organ|bones", "deprecated":
    "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 13237, "data":
    {"term_id": "UBERON:0004765", "ontology": "UBERON", "label": "skeletal element",
    "definition": "Organ consisting of skeletal tissue. Encompasses whole bones, fused
    bones, cartilaginious elements, teeth, dermal denticles.", "synonyms": "", "deprecated":
    "", "directly_referenced": "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET11
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 21,609
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: '[{"row": 21, "data": {"identifier": "habitatmech:BACDIVE.16280b13f2",
    "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review
    pass: this record is attested by more than one independent vocabulary, and this
    source''s label or path was read against the record''s ontology term to check
    the merge is right. It agrees. Source concepts in the same pass whose labels did
    not agree were re-decided rather than endorsed; see the pass''s other decisions
    of the same date.", "review_depth": "ITEM", "category": "", "relation": ""}},
    {"row": 609, "data": {"identifier": "habitatmech:GOLD.6296c1e38f", "decision":
    "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator":
    "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this
    record is attested by more than one independent vocabulary, and this source''s
    label or path was read against the record''s ontology term to check the merge
    is right. It agrees. Source concepts in the same pass whose labels did not agree
    were re-decided rather than endorsed; see the pass''s other decisions of the same
    date.", "review_depth": "ITEM", "category": "", "relation": ""}}]'
  snapshot_sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
- evidence_id: EP12
  kind: record_content
  reference: data/habitats/host_associated/skeletal_system__5ac43c2f.yaml
  locator: Full parent, scope context only
  accessed_at: '2026-10-15T14:51:40Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.3756d4bb39", "label": "Skeletal system",
    "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status":
    "SEEDED", "parent_habitats": ["UBERON:0001434", "habitatmech:GOLD.47e603cf4f"],
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7476",
    "source_label": "Skeletal system", "source_path": "Host-associated > Birds > Skeletal
    system", "mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node
    ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: NARROW."}]}'
  snapshot_sha256: c3948cbcc41d72ce4a43d816d605f12fb6002d5d5f204a8a7cdfdffa55aaf8d3
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03420168/graph
  locator: FOODON_03420168-graph.json
  accessed_at: '2026-10-15T14:36:21Z'
  support: context_only
  summary: 'Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/FOODON_03420168",
    "target": "http://purl.obolibrary.org/obo/FOODON_03420122", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: ff4c522abd126ef42154b0420c21e814c0a6de24756353b34d04474c6b39226f
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03420168
  locator: FOODON_03420168.json
  accessed_at: '2026-10-15T14:36:21Z'
  support: context_only
  summary: 'Inspected current ID, label, active status and definition for scope; {"obo_id":
    "FOODON:03420168", "label": "bone or shell", "is_obsolete": false}'
  snapshot_sha256: c9702a883f91c2d43f1590e37b20bd09f060074d8e90201f0cf41b2fae0c0f63
- evidence_id: EX3
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12408549/fullTextXML
  locator: PMC12408549.xml
  accessed_at: '2026-10-15T14:47:08Z'
  support: context_only
  summary: 'Primary abstract, DOI:10.3389/fbioe.2025.1617285, PMID:40918439: human
    bone samples were experimentally inoculated with S. aureus or S. epidermidis and
    compared with uninfected controls. This is bounded experimental bone-site evidence,
    not natural prevalence or reidentification of 125 BacDive strains.'
  snapshot_sha256: e28dc98dc6046c4bbb6e36daa22dbdba112ae47d4333d66ca41e5aaf6ac48731
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434/graph
  locator: UBERON_0001434-graph.json
  accessed_at: '2026-10-15T14:36:28Z'
  support: context_only
  summary: 'Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
    "target": "http://purl.obolibrary.org/obo/UBERON_0011216", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492",
    "label": "existence ends during"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002204", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004288", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001434",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004770", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}]'
  snapshot_sha256: ecbcf4134ad9733794246b12ecba04ef8a390ad1ec184baf4f7f0a60e5eaa71b
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001434
  locator: UBERON_0001434.json
  accessed_at: '2026-10-15T14:36:27Z'
  support: context_only
  summary: 'Inspected current ID, label, active status and definition for scope; {"obo_id":
    "UBERON:0001434", "label": "skeletal system", "is_obsolete": false}'
  snapshot_sha256: 0965f957490fb66ad6f4744d8fe4694bf133e2f156a67805e485800bc53e616e
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001474/graph
  locator: UBERON_0001474-graph.json
  accessed_at: '2026-10-15T14:36:29Z'
  support: context_only
  summary: 'Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001474",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001474",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001474",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001434", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001474",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002481", "uri": "http://purl.obolibrary.org/obo/RO_0002473",
    "label": "composed primarily of"}]'
  snapshot_sha256: f19fbbfc1186ef35ca92a8b83c0173296664c21f7b358440d07ce254b2227774
- evidence_id: EX7
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001474
  locator: UBERON_0001474.json
  accessed_at: '2026-10-15T14:36:28Z'
  support: context_only
  summary: 'Inspected current ID, label, active status and definition for scope; {"obo_id":
    "UBERON:0001474", "label": "bone element", "is_obsolete": false}'
  snapshot_sha256: c441ce63acb56b10608a7c4b073ae5514d1dbd497b72845d62bd6bbf61556416
- evidence_id: EX8
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0004765/graph
  locator: UBERON_0004765-graph.json
  accessed_at: '2026-10-15T14:36:35Z'
  support: context_only
  summary: 'Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0004765",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000062", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0004765",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001434", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 72a6e7b634f90bdccb8762694af6ab1e3ba7bf3b612169d4b7a05fcc7a8c8987
- evidence_id: EX9
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0004765
  locator: UBERON_0004765.json
  accessed_at: '2026-10-15T14:36:35Z'
  support: context_only
  summary: 'Inspected current ID, label, active status and definition for scope; {"obo_id":
    "UBERON:0004765", "label": "skeletal element", "is_obsolete": false}'
  snapshot_sha256: bf52a8a8ae22b73be890c91467dbc814862fbbc3d0f6f41633d46fb174ba0243
- evidence_id: EX10
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1000935,1000936,1000937,1000938,1000939,1002339,1003201,1005704,1005705,1008452,1008453,102684,1028806,1032071,1035187,1035189,103855,1051654,106654,1069609,1069614,1069618,1069621,1069623,1069627,1073382,1094555,1120932,1121020,1121098,1121364,1122173,1122921,1122925,1122931,1122988,1123034,1219017,123899,1265311,1267000,1280,1283,1296,1304,1322345,1328,1329902,1336208,1341644,1402,1408438,1408440,1408452,1415606,1448136,147802,154288,1578,1601,1659,168808,1707330,171549,1718,1747,186802,203119,214092,220341,273075,287,29318,29394,306537,316407,32002,33010,33028,354242,38284,43770,46124,47885,47920,504,51665,525919,598660,61645,66228,717,732,76759,83655&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T14:36:36Z'
  support: context_only
  summary: 'Every displayed ID was resolved, including current merged aliases; source
    labels are preserved, not falsely certified current preferred names. [{"id": "NCBITaxon:504",
    "source": "BACDIVE", "label": "Kingella kingae", "current_id": "504", "current_name":
    "Kingella kingae", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1280", "source": "BACDIVE", "label": "Staphylococcus
    aureus", "current_id": "1280", "current_name": "Staphylococcus aureus", "rank":
    "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1328",
    "source": "BACDIVE", "label": "Streptococcus anginosus", "current_id": "1328",
    "current_name": "Streptococcus anginosus", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1659", "source": "BACDIVE",
    "label": "Actinomyces israelii", "current_id": "1659", "current_name": "Actinomyces
    israelii", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:33028", "source": "BACDIVE", "label": "Staphylococcus saccharolyticus",
    "current_id": "33028", "current_name": "Staphylococcus saccharolyticus", "rank":
    "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:46124",
    "source": "BACDIVE", "label": "Granulicatella adiacens", "current_id": "46124",
    "current_name": "Granulicatella adiacens", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1402", "source": "BACDIVE",
    "label": "Bacillus licheniformis", "current_id": "1402", "current_name": "Bacillus
    licheniformis", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:1747", "source": "BACDIVE", "label": "Cutibacterium acnes",
    "current_id": "1747", "current_name": "Cutibacterium acnes", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:29318", "source":
    "BACDIVE", "label": "Winkia neuii subsp. anitrata", "current_id": "29318", "current_name":
    "Winkia neuii subsp. anitrata", "rank": "subspecies", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:29394", "source": "BACDIVE", "label": "Dolosigranulum
    pigrum", "current_id": "29394", "current_name": "Dolosigranulum pigrum", "rank":
    "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:33010",
    "source": "BACDIVE", "label": "Cutibacterium avidum", "current_id": "33010", "current_name":
    "Cutibacterium avidum", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:38284", "source": "BACDIVE", "label": "Corynebacterium
    accolens", "current_id": "38284", "current_name": "Corynebacterium accolens",
    "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:43770",
    "source": "BACDIVE", "label": "Corynebacterium striatum", "current_id": "43770",
    "current_name": "Corynebacterium striatum", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:47920", "source": "BACDIVE",
    "label": "Acidovorax delafieldii", "current_id": "47920", "current_name": "Acidovorax
    delafieldii", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:598660", "source": "BACDIVE", "label": "Corynebacterium pyruviciproducens",
    "current_id": "598660", "current_name": "Corynebacterium pyruviciproducens", "rank":
    "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:66228",
    "source": "BACDIVE", "label": "Gleimia europaea", "current_id": "66228", "current_name":
    "Gleimia europaea", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:717", "source": "BACDIVE", "label": "Actinobacillus capsulatus",
    "current_id": "717", "current_name": "Actinobacillus capsulatus", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:732", "source":
    "BACDIVE", "label": "Aggregatibacter aphrophilus", "current_id": "732", "current_name":
    "Aggregatibacter aphrophilus", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:102684", "source": "BACDIVE", "label": "Streptococcus
    infantarius", "current_id": "102684", "current_name": "Streptococcus infantarius",
    "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1121364",
    "source": "BACDIVE", "label": "Corynebacterium massiliense DSM 45435", "current_id":
    "1121364", "current_name": "Corynebacterium massiliense DSM 45435", "rank": "strain",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1219017", "source":
    "BACDIVE", "label": "Rhodococcus jostii NBRC 16295", "current_id": "1219017",
    "current_name": "Rhodococcus jostii NBRC 16295", "rank": "strain", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:123899", "source": "BACDIVE",
    "label": "Bordetella trematum", "current_id": "123899", "current_name": "Bordetella
    trematum", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:1265311", "source": "BACDIVE", "label": "Mycobacterium arosiense
    ATCC BAA-1401 = DSM 45069", "current_id": "1265311", "current_name": "Mycobacterium
    arosiense ATCC BAA-1401 = DSM 45069", "rank": "strain", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:1283", "source": "BACDIVE", "label":
    "Staphylococcus haemolyticus", "current_id": "1283", "current_name": "Staphylococcus
    haemolyticus", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:1296", "source": "BACDIVE", "label": "Mammaliicoccus sciuri",
    "current_id": "1296", "current_name": "Mammaliicoccus sciuri", "rank": "species",
    "direct_match": true, "recognized_alias": true}]'
  snapshot_sha256: 69f4f3dd5dd6e1a629f412ced9f307fe813a670f8088da1d3ac7471ed7b109bb
- evidence_id: ESEARCH
  kind: search
  reference: Local inputs and review archive
  locator: rg --no-ignore --hidden -l -F -e UBERON:0001474 -e 'bone element' -e bone_element
    -e habitatmech:BACDIVE.16280b13f2 -e habitatmech:GOLD.6296c1e38f curation history
    research reports data/raw build reviews
  accessed_at: '2026-10-15T14:33:45Z'
  support: context_only
  summary: Exact TSV parsing and ignored-inclusive target/mint/label/slug search establish
    the bounded row inventory. Structured archive traversal found no predecessor;
    not every broad textual lead was inspected.
  search_scope: curation, history, research, reports, data/raw, build, reviews including
    ignored/hidden files; all structured review.yaml files parsed.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity and hierarchy
  outcome: concern
  summary: The Uberon whole bone-element identity, skeletal-element genus and broad
    FOODON bone-or-shell genus are supported. Its additional whole avian skeletal-system
    superclass is false for both part/whole and host scope. BacDive contributes 125
    STRAIN assertions, a 96-taxon pool and 25 displayed taxa; GOLD contributes a separate
    zero-count path. Both source mappings are CLOSE and ITEM-reviewed, and their source
    labels correctly remain RELATED rather than exact synonyms.
  target_ids:
  - UBERON:0001474
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
- assessment_id: A2
  area: quantity
  topic: Frozen source units, ranks and parameters
  outcome: supported
  summary: 'Count/unit, first GOLD node, channel, score and displayed taxon ranks/labels
    reproduce exact source rows. Verification: [{"source": "BACDIVE", "count": 125,
    "unit": "STRAIN"}, {"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero counts
    are omitted, never interpreted as absence. Side-table biosamples/studies and MIxS
    slots are not added to tree ORGANISM counts.'
  target_ids:
  - UBERON:0001474
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
  - EX8
  - EX9
  - EX10
- assessment_id: A3
  area: evidence
  topic: Scientific support and source limits
  outcome: supported
  summary: The Uberon whole bone-element identity, skeletal-element genus and broad
    FOODON bone-or-shell genus are supported. Its additional whole avian skeletal-system
    superclass is false for both part/whole and host scope. BacDive contributes 125
    STRAIN assertions, a 96-taxon pool and 25 displayed taxa; GOLD contributes a separate
    zero-count path. Both source mappings are CLOSE and ITEM-reviewed, and their source
    labels correctly remain RELATED rather than exact synonyms.
  target_ids:
  - UBERON:0001474
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
- assessment_id: A4
  area: completeness
  topic: Native status and optional assertions
  outcome: supported
  summary: Executed routes reproduce CLOSE/REVIEWED. No causal edge or is_characteristic=true
    assertion is made. Optional absent fields and SEEDED status alone are not scientific
    defects; this review does not promote native status.
  target_ids:
  - UBERON:0001474
  evidence_ids:
  - E1
  - ERULE
  - ESEED
- assessment_id: A5
  area: schema
  topic: Deterministic native gates
  outcome: supported
  summary: Schema, strict, history, provenance, 3,208-record reproduction, causal,
    term-request, configured-label and exact-baseline full QC checks passed; these
    prove fidelity, not biological truth.
  target_ids:
  - UBERON:0001474
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: bone-element-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Containing anatomy is not a broader habitat class
  description: Exclude only the exact GOLD source-path/expected-parent contributions
    habitatmech:GOLD.3756d4bb39. The Uberon whole bone-element identity, skeletal-element
    genus and broad FOODON bone-or-shell genus are supported. Its additional whole
    avian skeletal-system superclass is false for both part/whole and host scope.
    BacDive contributes 125 STRAIN assertions, a 96-taxon pool and 25 displayed taxa;
    GOLD contributes a separate zero-count path. Both source mappings are CLOSE and
    ITEM-reviewed, and their source labels correctly remain RELATED rather than exact
    synonyms. Preserve independent ontology genera, source mappings, counts, units,
    taxa and native status.
  target_ids:
  - UBERON:0001474
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - UBERON:0001474
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Exclude only the exact GOLD source-path/expected-parent contributions
    habitatmech:GOLD.3756d4bb39. The Uberon whole bone-element identity, skeletal-element
    genus and broad FOODON bone-or-shell genus are supported. Its additional whole
    avian skeletal-system superclass is false for both part/whole and host scope.
    BacDive contributes 125 STRAIN assertions, a 96-taxon pool and 25 displayed taxa;
    GOLD contributes a separate zero-count path. Both source mappings are CLOSE and
    ITEM-reviewed, and their source labels correctly remain RELATED rather than exact
    synonyms. Preserve independent ontology genera, source mappings, counts, units,
    taxa and native status. No repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history. Do not change
    source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Every historical specimen and original source pair has not been independently reidentified.
  Source counts are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 no-adapter pairs and taxon labels; independent
  current NCBI lookup is recorded for displayed taxa.
- Full QC evidence is a verified remote run at the exact captured baseline, not a
  newly executed local QC. New review outputs require subsequent publication checks.
- 'iModulonDB is not applicable: no gene, regulator or expression-module assertion
  is made. No paid research was used.'
notes:
- Captured hashes were rechecked against both working bytes and the exact Git base;
  no scientific inputs were silently refreshed.
- Ignored-inclusive searches and parsed structured archive found no prior structured
  observation of this exact target. Legacy Markdown is a lead, not structured lineage.
- This immutable observation precedes separately authorized curation and does not
  claim repairs.
tags:
- individual-scientific-review
- host-associated
```
