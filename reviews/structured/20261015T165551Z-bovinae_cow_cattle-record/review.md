# Record review: bovine-associated environment (habitatmech:BACDIVE.a4a67c4a7f)

- Review: 20261015T165551Z-bovinae_cow_cattle-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T16:29:23Z
- Finished UTC: 2026-10-15T16:55:51Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The minted bovine-associated environment, animal-associated genus and host category are supported. The authored exact alias Bovinae-Cow,-Cattle names the determining host rather than an environment and should not survive as exact synonymy. The source has 619 STRAIN assertions, a 336-taxon pool and 25 displayed taxa; neither the broad host definition nor the raw category establishes domestic-cattle exclusivity. The intentionally suppressed partial Bos taxon match is not a missing required xref.

## Scope And Provenance

Full field-by-field scientific review of this one exact target at 50dbf8b388bf32ca58708f7993e83120310f7cea.

Selection: One of the next 24 path-ordered unreviewed targets in an ignored-inclusive 3208-record census. This bundle assesses only this identifier, not a cohort sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 50dbf8b388bf32ca58708f7993e83120310f7cea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.a4a67c4a7f | data/habitats/host_associated/bovinae_cow_cattle.yaml | generated | bovine-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:BACDIVE.a4a67c4a7f | Completed 2026-10-15T16:33:29Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bovinae_cow_cattle.yaml |
| validate-strict | passed | True | habitatmech:BACDIVE.a4a67c4a7f | Completed 2026-10-15T16:35:27Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:BACDIVE.a4a67c4a7f | Completed 2026-10-15T16:35:39Z. No issues found<br>814 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:BACDIVE.a4a67c4a7f | Completed 2026-10-15T16:35:39Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:BACDIVE.a4a67c4a7f | Completed 2026-10-15T16:36:01Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:BACDIVE.a4a67c4a7f | Completed 2026-10-15T16:36:06Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:BACDIVE.a4a67c4a7f | Completed 2026-10-15T16:36:35Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:BACDIVE.a4a67c4a7f | Completed 2026-10-15T16:37:38Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | habitatmech:BACDIVE.a4a67c4a7f | Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320 |

## Scientific And Domain Assessments

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:BACDIVE.a4a67c4a7f.

The minted bovine-associated environment, animal-associated genus and host category are supported. The authored exact alias Bovinae-Cow,-Cattle names the determining host rather than an environment and should not survive as exact synonymy. The source has 619 STRAIN assertions, a 336-taxon pool and 25 displayed taxa; neither the broad host definition nor the raw category establishes domestic-cattle exclusivity. The intentionally suppressed partial Bos taxon match is not a missing required xref.

### Frozen counts, units, ranks, channels and scores

quantity: supported. Targets: habitatmech:BACDIVE.a4a67c4a7f.

Every source assertion and displayed taxon was checked against its exact raw row. [{"source": "BACDIVE", "count": 619, "unit": "STRAIN"}]. Side-table biosample/study counts are not added to tree ORGANISM counts. Zero-count omission is not biological absence.

### Scientific support and scope limits

evidence: supported. Targets: habitatmech:BACDIVE.a4a67c4a7f.

The minted bovine-associated environment, animal-associated genus and host category are supported. The authored exact alias Bovinae-Cow,-Cattle names the determining host rather than an environment and should not survive as exact synonymy. The source has 619 STRAIN assertions, a 336-taxon pool and 25 displayed taxa; neither the broad host definition nor the raw category establishes domestic-cattle exclusivity. The intentionally suppressed partial Bos taxon match is not a missing required xref.

### Status, optional content, triads and mechanisms

completeness: supported. Targets: habitatmech:BACDIVE.a4a67c4a7f.

Actual routes reproduce UNGROUNDED/REVIEWED. No environmental-parameter, causal-edge, discussion/dataset or is_characteristic=true assertion is present in this target. Optional absence and SEEDED status alone are not defects. Scientific review does not promote native status.

### Native deterministic validation

schema: supported. Targets: habitatmech:BACDIVE.a4a67c4a7f.

Ordinary and strict schemas, 814 history records, provenance, 3208-record reproduction, 32 causal overlays, term-request checks, configured labels and exact-base full QC passed. These establish fidelity, not biological truth.

## Findings

### F1: Whole-host name is an exact environment synonym

major / open / confirmed; issue key: bovinae-cow-cattle-host-alias.

Remove the authored exact synonym Bovinae-Cow,-Cattle from the native term request and add the guarded definition-source-label exclusion to prevent automatic reintroduction. Preserve the source attestation and bovine-associated definition; do not substitute Bos taxonomy as habitat identity or invent domestic-cattle exclusivity.

## Recommended Actions And Acceptance Checks

### ACT1

Remove the authored exact synonym Bovinae-Cow,-Cattle from the native term request and add the guarded definition-source-label exclusion to prevent automatic reintroduction. Preserve the source attestation and bovine-associated definition; do not substitute Bos taxonomy as habitat identity or invent domestic-cattle exclusivity. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identifiers, counts/units and raw provenance. Change identity, native status or mapping only when separately supported by the scoped item assessment; never change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bovinae_cow_cattle.yaml; Entire target YAML | supports | Entire record read: identity, definition, parents, source attestations, every displayed taxon and complete history. |
| ERULE | docs/CURATION.md; Host, anatomy, hierarchy, disposition and evidence rules | supports | Parent_habitats means strictly broader; source occurrence does not establish characteristic presence. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord and SourceAttestation slots | supports | Typed identity, broader habitat and source-to-record mapping semantics; optional fields are not mandatory. |
| ESEED | src/habitatmech/seed.py; Executed build_corpus/apply_decision routes and parent accumulation | supports | Full target equality was verified against actual generated document. Exact source routes: [{"mint": "habitatmech:BACDIVE.a4a67c4a7f", "automatic": {"identifier": "habitatmech:BACDIVE.a4a67c4a7f", "grounding_status": "NOT_APPLICABLE", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": ["NCBITaxon:9903"], "route": "bacdive_non_habitat_target", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:BACDIVE.a4a67c4a7f", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_bacdive_non_habitat_target", "category": "HOST_ASSOCIATED", "reviewed": true, "decision": {"identifier": "habitatmech:BACDIVE.a4a67c4a7f", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it \u2014 the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an &lt;X&gt;-associated environment. Host-associated &gt; Porifera was NOT_APPLICABLE while its own child Porifera &gt; Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. Category set to HOST_ASSOCIATED (#200): the row already claims ENVO:01001002 'animal-associated environment' as the nearest broader term, which is the claim that a living animal host defines the habitat, and every other record carrying that parent is HOST_ASSOCIATED. The category column was left blank here, so the seeder's default stood and five domestic-mammal hosts stayed in OTHER while their siblings did not. The reasoning above is unchanged.", "review_depth": "ITEM", "category": "HOST_ASSOCIATED", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Frozen inventory projection | supports | Source counts and taxon ranks/scores preserve source units; PREGO projections do not retain original pair-level citations. |
| ET5 | data/raw/bacdive_source_taxa.tsv; Physical TSV rows 346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370 | supports | [{"row": 346, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "1", "taxon_id": "NCBITaxon:731", "taxon_label": "Histophilus somni", "strain_count": "26", "corroborated_by": ""}}, {"row": 347, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "2", "taxon_id": "NCBITaxon:1802", "taxon_label": "Mycolicibacterium farcinogenes", "strain_count": "18", "corroborated_by": ""}}, {"row": 348, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "3", "taxon_id": "NCBITaxon:1661", "taxon_label": "Trueperella pyogenes", "strain_count": "14", "corroborated_by": ""}}, {"row": 349, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "4", "taxon_id": "NCBITaxon:32020", "taxon_label": "Campylobacter fetus subsp. venerealis", "strain_count": "14", "corroborated_by": ""}}, {"row": 350, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "5", "taxon_id": "NCBITaxon:1334", "taxon_label": "Streptococcus dysgalactiae", "strain_count": "11", "corroborated_by": ""}}, {"row": 351, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "6", "taxon_id": "NCBITaxon:197", "taxon_label": "Campylobacter jejuni", "strain_count": "10", "corroborated_by": ""}}, {"row": 352, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "7", "taxon_id": "NCBITaxon:1796", "taxon_label": "Mycolicibacterium senegalense", "strain_count": "9", "corroborated_by": ""}}, {"row": 353, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "8", "taxon_id": "NCBITaxon:476", "taxon_label": "Moraxella bovis", "strain_count": "8", "corroborated_by": ""}}, {"row": 354, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "9", "taxon_id": "NCBITaxon:153721", "taxon_label": "Sporocytophaga myxococcoides", "strain_count": "7", "corroborated_by": ""}}, {"row": 355, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "10", "taxon_id": "NCBITaxon:1724", "taxon_label": "Corynebacterium renale", "strain_count": "7", "corroborated_by": ""}}, {"row": 356, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "11", "taxon_id": "NCBITaxon:184914", "taxon_label": "Corallococcus coralloides", "strain_count": "7", "corroborated_by": ""}}, {"row": 357, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "12", "taxon_id": "NCBITaxon:1886", "taxon_label": "Streptomyces albidoflavus", "strain_count": "7", "corroborated_by": ""}}, {"row": 358, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "13", "taxon_id": "NCBITaxon:198", "taxon_label": "Campylobacter hyointestinalis", "strain_count": "7", "corroborated_by": ""}}, {"row": 359, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "14", "taxon_id": "NCBITaxon:33", "taxon_label": "Myxococcus fulvus", "strain_count": "7", "corroborated_by": ""}}, {"row": 360, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "15", "taxon_id": "NCBITaxon:678", "taxon_label": "Vibrio sp.", "strain_count": "7", "corroborated_by": ""}}, {"row": 361, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "16", "taxon_id": "NCBITaxon:720", "taxon_label": "Actinobacillus lignieresii", "strain_count": "7", "corroborated_by": ""}}, {"row": 362, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "17", "taxon_id": "NCBITaxon:82348", "taxon_label": "Streptococcus pluranimalium", "strain_count": "7", "corroborated_by": ""}}, {"row": 363, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "18", "taxon_id": "NCBITaxon:206", "taxon_label": "Campylobacter sputorum", "strain_count": "6", "corroborated_by": ""}}, {"row": 364, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "19", "taxon_id": "NCBITaxon:2081794", "taxon_label": "Mannheimia sp.", "strain_count": "6", "corroborated_by": ""}}, {"row": 365, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "20", "taxon_id": "NCBITaxon:653940", "taxon_label": "Basfia succiniciproducens", "strain_count": "6", "corroborated_by": ""}}, {"row": 366, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "21", "taxon_id": "NCBITaxon:1329", "taxon_label": "Streptococcus canis", "strain_count": "5", "corroborated_by": ""}}, {"row": 367, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "22", "taxon_id": "NCBITaxon:1658", "taxon_label": "Actinomyces bovis", "strain_count": "5", "corroborated_by": ""}}, {"row": 368, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "23", "taxon_id": "NCBITaxon:2", "taxon_label": "Bacteria", "strain_count": "5", "corroborated_by": ""}}, {"row": 369, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "24", "taxon_id": "NCBITaxon:36808", "taxon_label": "Corynebacterium bovis", "strain_count": "5", "corroborated_by": ""}}, {"row": 370, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "25", "taxon_id": "NCBITaxon:985762", "taxon_label": "Staphylococcus agnetis", "strain_count": "5", "corroborated_by": ""}}] |
| ET6 | data/raw/isolation_source_groundings.tsv; Physical TSV rows 49 | supports | [{"row": 49, "data": {"subject_label": "Bovinae-Cow,-Cattle", "subject_label_normalized": "bovinae cow cattle", "object_id": "NCBITaxon:9903", "object_label": "Bos", "object_source": "NCBITaxon", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification": "semapv:LexicalMatching", "curator": "ols4_search_synonym", "source_dataset": "bacdive", "verified_date": "2026-05-01"}}] |
| ET7 | data/raw/bacdive_isolation_sources.tsv; Physical TSV rows 25 | supports | [{"row": 25, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "label": "Bovinae-Cow,-Cattle", "source_slug": "bovinae-cow,-cattle", "strain_count": "619", "taxon_count": "336"}}] |
| ET8 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 6797 | supports | [{"row": 6797, "data": {"subject": "ENVO:01001002", "predicate": "rdfs:subClassOf", "object": "ENVO:01001000"}}] |
| ET9 | data/raw/ontology_terms.tsv; Physical TSV rows 8491 | supports | [{"row": 8491, "data": {"term_id": "ENVO:01001002", "ontology": "ENVO", "label": "animal-associated environment", "definition": "An environmental system determined by an animal.", "synonyms": "Metazoan-associated environment&#124;animal environment", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET10 | curation/term_requests.tsv; Physical TSV rows 19 | supports | [{"row": 19, "data": {"identifier": "habitatmech:BACDIVE.a4a67c4a7f", "requested_label": "bovine-associated environment", "parent_class": "ENVO:01001002", "parent_label": "animal-associated environment", "definition": "An animal-associated environment which is determined by a bovine.", "exact_synonym": "Bovinae-Cow,-Cattle", "curator": "claude-opus-5", "date": "2026-08-17", "notes": "Definition drafted from the record's deep-research report under research/habitats/ and read against it; the report's proposed wording, genus and near-miss table are the evidence. BacDive's cattle host category.", "parent_mode": "ADD"}}] |
| ET11 | curation/decisions.tsv; Physical TSV rows 1599 | supports | [{"row": 1599, "data": {"identifier": "habitatmech:BACDIVE.a4a67c4a7f", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it \u2014 the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an &lt;X&gt;-associated environment. Host-associated &gt; Porifera was NOT_APPLICABLE while its own child Porifera &gt; Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. Category set to HOST_ASSOCIATED (#200): the row already claims ENVO:01001002 'animal-associated environment' as the nearest broader term, which is the claim that a living animal host defines the habitat, and every other record carrying that parent is HOST_ASSOCIATED. The category column was left blank here, so the seeder's default stood and five domestic-mammal hosts stayed in OTHER while their siblings did not. The reasoning above is unchanged.", "review_depth": "ITEM", "category": "HOST_ASSOCIATED", "relation": ""}}] |
| EP12 | data/habitats/other/animal_associated_environment.yaml; Full parent record, context only | supports | {"identifier": "ENVO:01001002", "label": "animal-associated environment", "definition": "An environmental system determined by an animal.", "definition_source": "ENVO", "habitat_category": "OTHER", "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "Metazoan-associated environment", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"}, {"synonym_text": "animal environment", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"}], "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal", "notes": "Physicochemical parameter bands from kg-microbe's environment table."}, {"source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated environment", "assertion_count": 144, "assertion_unit": "TAXON"}], "environmental_parameters": [{"parameter": "PRESSURE", "qualitative_value": "low", "source": "kg-microbe environments.csv (host_animal)"}, {"parameter": "TEMPERATURE_VARIABILITY", "qualitative_value": "low", "source": "kg-microbe environments.csv (host_animal)"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:1001", "source": "MADIN", "taxon_label": "flexibacter_polymorphus", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1001732", "source": "MADIN", "taxon_label": "Mycobacterium abscessus 5S-0921", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1004165", "source": "MADIN", "taxon_label": "Photorhabdus luminescens caribbeanensis HG29", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1004166", "source": "MADIN", "taxon_label": "Photorhabdus luminescens hainanensis C8404", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:102862", "source": "MADIN", "taxon_label": "proteus_penneri", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1028805", "source": "MADIN", "taxon_label": "Haemophilus haemolyticus M21621", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1049564", "source": "MADIN", "taxon_label": "endosymbiont of Tevnia jerichonana (vent Tica)", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1084229", "source": "MADIN", "taxon_label": "Yersinia pestis bv. Orientalis BA200901703", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:110933", "source": "MADIN", "taxon_label": "leifsonia_poae", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123042", "source": "MADIN", "taxon_label": "Photorhabdus temperata stackebrandtii GPS11", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123520", "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9686", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123521", "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9622", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123522", "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9938", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1125973", "source": "MADIN", "taxon_label": "Bosea sp. 117", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1128912", "source": "MADIN", "taxon_label": "Paraglaciecola mesophila KMM 241", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1136416", "source": "MADIN", "taxon_label": "Salinispora pacifica CNT001", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137251", "source": "MADIN", "taxon_label": "Salinispora arenicola CNH905", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137255", "source": "MADIN", "taxon_label": "Salinispora arenicola CNT005", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137257", "source": "MADIN", "taxon_label": "Salinispora arenicola CNX508", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1156842", "source": "MADIN", "taxon_label": "Streptomyces sp. LaPpAH-180", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:115862", "source": "MADIN", "taxon_label": "mycobacterium_caprae", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1159489", "source": "MADIN", "taxon_label": "Cronobacter sakazakii 2151", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187845", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZB36", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187846", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZD137", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187847", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZC157", "candidate_pool": 144}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE, MADIN. Grounding: EXACT."}]} |
| ELEGACY | reports/yaml_record_review/20260922T072807Z-bovinae_cow_cattle.md; Findings and recommended edits; historical lead | supports | Legacy conclusions were compared with current target and primary evidence. No formal predecessor or automatic native-status requirement is inferred. |
| ERESEARCH | research/habitats/other/bovinae-cow-cattle-habitatmech-bacdive-a4a67c4a7f-deep-research-claude_code.md; Whole bovine research report | supports | The report distinguishes host environment from taxon and explicitly marks cattle-only scope as inference. It is not automatic evidence for every cited claim; the short native definition does not import its rumen parameters. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph; ENVO_01001000-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000; ENVO_01001000.json | context_only | Current term identity, active status and definition: {"obo_id": "ENVO:01001000", "label": "environmental system determined by an organism", "is_obsolete": false, "description": ["An environmental system which is determined by a living organism."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph; ENVO_01001002-graph.json | context_only | Typed outgoing ontology relations, not an untyped ancestor list: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002; ENVO_01001002.json | context_only | Current term identity, active status and definition: {"obo_id": "ENVO:01001002", "label": "animal-associated environment", "is_obsolete": false, "description": ["An environmental system determined by an animal."]} |
| EX5 | https://bacdive.dsmz.de/isolation-sources; bacdive-isolation.html | context_only | Current BacDive isolation-source browser contains Bovinae (Cow, Cattle) and Bronchial wash categories. It is a vocabulary witness, not a census of the frozen strain membership or proof of cattle-only scope. |
| EX6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Histophilus%20somni%22%20AND%20%222336%22%20AND%20%22genome%22&amp;format=json&amp;resultType=core&amp;pageSize=20; paper-somni.json | context_only | Primary abstract PMID:39240084, DOI:10.1128/mra.00570-24: Histophilus somni strain 91 originated from pneumonic lung tissue of a beef calf. Supports one bovine-host example for this displayed species, not reidentification of the 26 BacDive H. somni strains. |
| EX7 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1117644,1122164,1131452,1131453,1131454,1131455,1133849,1141647,1157946,1162284,1162288,1177117,1189613,1193128,1199187,1206729,1214102,1220554,1226751,12455,1271862,1328,1329,1329902,1334,1348,1392869,147802,153721,1578,1590,1601,161879,1639,1658,1661,1679,1680,1682,1683,168808,169963,1718,1724,1796,1802,1817,184914,1886,1962118,197,198,2,205913,206,2074,2081794,222805,238,2701,28026,28087,286804,287,32002,32020,33,341199,36808,391904,439842,476,47885,480035,484020,51665,524884,653940,678,720,72407,731,747,756689,76759,82135,82348,83655,838,84107,912594,985762&amp;retmode=xml; taxonomy.xml | context_only | All displayed IDs resolve in current NCBI Taxonomy. Preferred names and source labels were compared, without treating recognized historical aliases as wrong identities: [{"id": "NCBITaxon:731", "source": "BACDIVE", "label": "Histophilus somni", "current_id": "731", "current_name": "Histophilus somni", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1802", "source": "BACDIVE", "label": "Mycolicibacterium farcinogenes", "current_id": "1802", "current_name": "Mycobacterium farcinogenes", "rank": "species", "direct_match": false, "recognized_alias": true}, {"id": "NCBITaxon:1661", "source": "BACDIVE", "label": "Trueperella pyogenes", "current_id": "1661", "current_name": "Trueperella pyogenes", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:32020", "source": "BACDIVE", "label": "Campylobacter fetus subsp. venerealis", "current_id": "32020", "current_name": "Campylobacter fetus subsp. venerealis", "rank": "subspecies", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1334", "source": "BACDIVE", "label": "Streptococcus dysgalactiae", "current_id": "1334", "current_name": "Streptococcus dysgalactiae", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:197", "source": "BACDIVE", "label": "Campylobacter jejuni", "current_id": "197", "current_name": "Campylobacter jejuni", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1796", "source": "BACDIVE", "label": "Mycolicibacterium senegalense", "current_id": "1796", "current_name": "Mycolicibacterium senegalense", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:476", "source": "BACDIVE", "label": "Moraxella bovis", "current_id": "476", "current_name": "Moraxella bovis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:153721", "source": "BACDIVE", "label": "Sporocytophaga myxococcoides", "current_id": "153721", "current_name": "Sporocytophaga myxococcoides", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1724", "source": "BACDIVE", "label": "Corynebacterium renale", "current_id": "1724", "current_name": "Corynebacterium renale", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:184914", "source": "BACDIVE", "label": "Corallococcus coralloides", "current_id": "184914", "current_name": "Corallococcus coralloides", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1886", "source": "BACDIVE", "label": "Streptomyces albidoflavus", "current_id": "1886", "current_name": "Streptomyces albidoflavus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:198", "source": "BACDIVE", "label": "Campylobacter hyointestinalis", "current_id": "198", "current_name": "Campylobacter hyointestinalis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:33", "source": "BACDIVE", "label": "Myxococcus fulvus", "current_id": "33", "current_name": "Myxococcus fulvus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:678", "source": "BACDIVE", "label": "Vibrio sp.", "current_id": "678", "current_name": "Vibrio sp.", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:720", "source": "BACDIVE", "label": "Actinobacillus lignieresii", "current_id": "720", "current_name": "Actinobacillus lignieresii", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:82348", "source": "BACDIVE", "label": "Streptococcus pluranimalium", "current_id": "82348", "current_name": "Streptococcus pluranimalium", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:206", "source": "BACDIVE", "label": "Campylobacter sputorum", "current_id": "206", "current_name": "Campylobacter sputorum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2081794", "source": "BACDIVE", "label": "Mannheimia sp.", "current_id": "2081794", "current_name": "Mannheimia sp.", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:653940", "source": "BACDIVE", "label": "Basfia succiniciproducens", "current_id": "653940", "current_name": "Basfia succiniciproducens", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1329", "source": "BACDIVE", "label": "Streptococcus canis", "current_id": "1329", "current_name": "Streptococcus canis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1658", "source": "BACDIVE", "label": "Actinomyces bovis", "current_id": "1658", "current_name": "Actinomyces bovis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2", "source": "BACDIVE", "label": "Bacteria", "current_id": "2", "current_name": "Bacteria", "rank": "domain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:36808", "source": "BACDIVE", "label": "Corynebacterium bovis", "current_id": "36808", "current_name": "Corynebacterium bovis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:985762", "source": "BACDIVE", "label": "Staphylococcus agnetis", "current_id": "985762", "current_name": "Staphylococcus agnetis", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e habitatmech:BACDIVE.a4a67c4a7f -e 'bovine-associated environment' -e bovinae_cow_cattle -e habitatmech:BACDIVE.a4a67c4a7f curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately from broad textual matches. No previous structured target observation was found; not every broad label match was inspected. |

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
review_id: 20261015T165551Z-bovinae_cow_cattle-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: bovine-associated environment (habitatmech:BACDIVE.a4a67c4a7f)'
started_at: '2026-10-15T16:29:23Z'
finished_at: '2026-10-15T16:55:51Z'
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
summary: The minted bovine-associated environment, animal-associated genus and host
  category are supported. The authored exact alias Bovinae-Cow,-Cattle names the determining
  host rather than an environment and should not survive as exact synonymy. The source
  has 619 STRAIN assertions, a 336-taxon pool and 25 displayed taxa; neither the broad
  host definition nor the raw category establishes domestic-cattle exclusivity. The
  intentionally suppressed partial Bos taxon match is not a missing required xref.
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
  - path: data/habitats/host_associated/bovinae_cow_cattle.yaml
    sha256: 344f2232b803569c07d6e1b22b461f7ee8d0308df2416eac06b5ac53ddaf11e2
    role: target
  - path: data/habitats/other/animal_associated_environment.yaml
    sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
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
  - path: reports/yaml_record_review/20260922T072807Z-bovinae_cow_cattle.md
    sha256: faa1d9a9abb159cb4a7caf3d400bd09db9250f313d4b4f77e5ec47b169a88e06
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
  - path: research/habitats/other/bovinae-cow-cattle-habitatmech-bacdive-a4a67c4a7f-deep-research-claude_code.md
    sha256: 108fc1d39bcda2abf44d808dd714d22ee0fa89df305801d23b12648f5ab74fde
    role: context
targets:
- target_id: habitatmech:BACDIVE.a4a67c4a7f
  path: data/habitats/host_associated/bovinae_cow_cattle.yaml
  label: bovine-associated environment
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
  - habitatmech:BACDIVE.a4a67c4a7f
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context is not additional coverage. Export compatibility and original
      individual source specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bovinae_cow_cattle.yaml
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.a4a67c4a7f
  summary: "Completed 2026-10-15T16:33:29Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bovinae_cow_cattle.yaml"
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
  - habitatmech:BACDIVE.a4a67c4a7f
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
  - habitatmech:BACDIVE.a4a67c4a7f
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
  - habitatmech:BACDIVE.a4a67c4a7f
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
  - habitatmech:BACDIVE.a4a67c4a7f
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
  - habitatmech:BACDIVE.a4a67c4a7f
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
  - habitatmech:BACDIVE.a4a67c4a7f
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
  - habitatmech:BACDIVE.a4a67c4a7f
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
  - habitatmech:BACDIVE.a4a67c4a7f
  summary: Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320
  scope_note: Exact unchanged scientific input baseline; new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bovinae_cow_cattle.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: 'Entire record read: identity, definition, parents, source attestations,
    every displayed taxon and complete history.'
  snapshot_sha256: 344f2232b803569c07d6e1b22b461f7ee8d0308df2416eac06b5ac53ddaf11e2
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host, anatomy, hierarchy, disposition and evidence rules
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: Parent_habitats means strictly broader; source occurrence does not establish
    characteristic presence.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord and SourceAttestation slots
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: Typed identity, broader habitat and source-to-record mapping semantics;
    optional fields are not mandatory.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed build_corpus/apply_decision routes and parent accumulation
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: 'Full target equality was verified against actual generated document. Exact
    source routes: [{"mint": "habitatmech:BACDIVE.a4a67c4a7f", "automatic": {"identifier":
    "habitatmech:BACDIVE.a4a67c4a7f", "grounding_status": "NOT_APPLICABLE", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": ["NCBITaxon:9903"],
    "route": "bacdive_non_habitat_target", "category": null, "reviewed": false, "decision":
    null}, "final": {"identifier": "habitatmech:BACDIVE.a4a67c4a7f", "grounding_status":
    "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_bacdive_non_habitat_target",
    "category": "HOST_ASSOCIATED", "reviewed": true, "decision": {"identifier": "habitatmech:BACDIVE.a4a67c4a7f",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Host-taxon reversal
    (#114): this was NOT_APPLICABLE on the reasoning that ''a host taxon is not a
    habitat''. That reasoning is wrong, and the corpus already contradicted it \u2014
    the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia,
    Mammals, Birds and Fish, which keep their own identity and a term request for
    an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while
    its own child Porifera > Sponge was a term request.An organism acting as a host
    IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated,
    animal-associated and fungi-associated environment. What is not a habitat is the
    TAXON TERM \u2014 a phylum is a class of organisms, not a place \u2014 so the
    taxon stays an xref (#99) and the concept keeps its own identity as a term-request
    candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger
    and false claim. Category set to HOST_ASSOCIATED (#200): the row already claims
    ENVO:01001002 ''animal-associated environment'' as the nearest broader term, which
    is the claim that a living animal host defines the habitat, and every other record
    carrying that parent is HOST_ASSOCIATED. The category column was left blank here,
    so the seeder''s default stood and five domestic-mammal hosts stayed in OTHER
    while their siblings did not. The reasoning above is unchanged.", "review_depth":
    "ITEM", "category": "HOST_ASSOCIATED", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Frozen inventory projection
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: Source counts and taxon ranks/scores preserve source units; PREGO projections
    do not retain original pair-level citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/bacdive_source_taxa.tsv
  locator: Physical TSV rows 346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: '[{"row": 346, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "1", "taxon_id": "NCBITaxon:731", "taxon_label": "Histophilus somni",
    "strain_count": "26", "corroborated_by": ""}}, {"row": 347, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "2", "taxon_id": "NCBITaxon:1802",
    "taxon_label": "Mycolicibacterium farcinogenes", "strain_count": "18", "corroborated_by":
    ""}}, {"row": 348, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "3", "taxon_id": "NCBITaxon:1661", "taxon_label": "Trueperella pyogenes",
    "strain_count": "14", "corroborated_by": ""}}, {"row": 349, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "4", "taxon_id": "NCBITaxon:32020",
    "taxon_label": "Campylobacter fetus subsp. venerealis", "strain_count": "14",
    "corroborated_by": ""}}, {"row": 350, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "5", "taxon_id": "NCBITaxon:1334", "taxon_label": "Streptococcus dysgalactiae",
    "strain_count": "11", "corroborated_by": ""}}, {"row": 351, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "6", "taxon_id": "NCBITaxon:197",
    "taxon_label": "Campylobacter jejuni", "strain_count": "10", "corroborated_by":
    ""}}, {"row": 352, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "7", "taxon_id": "NCBITaxon:1796", "taxon_label": "Mycolicibacterium senegalense",
    "strain_count": "9", "corroborated_by": ""}}, {"row": 353, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "8", "taxon_id": "NCBITaxon:476",
    "taxon_label": "Moraxella bovis", "strain_count": "8", "corroborated_by": ""}},
    {"row": 354, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "9", "taxon_id": "NCBITaxon:153721", "taxon_label": "Sporocytophaga myxococcoides",
    "strain_count": "7", "corroborated_by": ""}}, {"row": 355, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "10", "taxon_id": "NCBITaxon:1724",
    "taxon_label": "Corynebacterium renale", "strain_count": "7", "corroborated_by":
    ""}}, {"row": 356, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "11", "taxon_id": "NCBITaxon:184914", "taxon_label": "Corallococcus coralloides",
    "strain_count": "7", "corroborated_by": ""}}, {"row": 357, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "12", "taxon_id": "NCBITaxon:1886",
    "taxon_label": "Streptomyces albidoflavus", "strain_count": "7", "corroborated_by":
    ""}}, {"row": 358, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "13", "taxon_id": "NCBITaxon:198", "taxon_label": "Campylobacter hyointestinalis",
    "strain_count": "7", "corroborated_by": ""}}, {"row": 359, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "14", "taxon_id": "NCBITaxon:33",
    "taxon_label": "Myxococcus fulvus", "strain_count": "7", "corroborated_by": ""}},
    {"row": 360, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "15", "taxon_id": "NCBITaxon:678", "taxon_label": "Vibrio sp.", "strain_count":
    "7", "corroborated_by": ""}}, {"row": 361, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "16", "taxon_id": "NCBITaxon:720", "taxon_label": "Actinobacillus lignieresii",
    "strain_count": "7", "corroborated_by": ""}}, {"row": 362, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "17", "taxon_id": "NCBITaxon:82348",
    "taxon_label": "Streptococcus pluranimalium", "strain_count": "7", "corroborated_by":
    ""}}, {"row": 363, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "18", "taxon_id": "NCBITaxon:206", "taxon_label": "Campylobacter sputorum",
    "strain_count": "6", "corroborated_by": ""}}, {"row": 364, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "19", "taxon_id": "NCBITaxon:2081794",
    "taxon_label": "Mannheimia sp.", "strain_count": "6", "corroborated_by": ""}},
    {"row": 365, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "20", "taxon_id": "NCBITaxon:653940", "taxon_label": "Basfia succiniciproducens",
    "strain_count": "6", "corroborated_by": ""}}, {"row": 366, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "21", "taxon_id": "NCBITaxon:1329",
    "taxon_label": "Streptococcus canis", "strain_count": "5", "corroborated_by":
    ""}}, {"row": 367, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "22", "taxon_id": "NCBITaxon:1658", "taxon_label": "Actinomyces bovis",
    "strain_count": "5", "corroborated_by": ""}}, {"row": 368, "data": {"bacdive_id":
    "bacdive.isolation_source:bovinae-cow,-cattle", "rank": "23", "taxon_id": "NCBITaxon:2",
    "taxon_label": "Bacteria", "strain_count": "5", "corroborated_by": ""}}, {"row":
    369, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle", "rank":
    "24", "taxon_id": "NCBITaxon:36808", "taxon_label": "Corynebacterium bovis", "strain_count":
    "5", "corroborated_by": ""}}, {"row": 370, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "rank": "25", "taxon_id": "NCBITaxon:985762", "taxon_label": "Staphylococcus agnetis",
    "strain_count": "5", "corroborated_by": ""}}]'
  snapshot_sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
- evidence_id: ET6
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: Physical TSV rows 49
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: '[{"row": 49, "data": {"subject_label": "Bovinae-Cow,-Cattle", "subject_label_normalized":
    "bovinae cow cattle", "object_id": "NCBITaxon:9903", "object_label": "Bos", "object_source":
    "NCBITaxon", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification":
    "semapv:LexicalMatching", "curator": "ols4_search_synonym", "source_dataset":
    "bacdive", "verified_date": "2026-05-01"}}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: ET7
  kind: database
  reference: data/raw/bacdive_isolation_sources.tsv
  locator: Physical TSV rows 25
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: '[{"row": 25, "data": {"bacdive_id": "bacdive.isolation_source:bovinae-cow,-cattle",
    "label": "Bovinae-Cow,-Cattle", "source_slug": "bovinae-cow,-cattle", "strain_count":
    "619", "taxon_count": "336"}}]'
  snapshot_sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 6797
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: '[{"row": 6797, "data": {"subject": "ENVO:01001002", "predicate": "rdfs:subClassOf",
    "object": "ENVO:01001000"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET9
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 8491
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: '[{"row": 8491, "data": {"term_id": "ENVO:01001002", "ontology": "ENVO",
    "label": "animal-associated environment", "definition": "An environmental system
    determined by an animal.", "synonyms": "Metazoan-associated environment|animal
    environment", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET10
  kind: database
  reference: curation/term_requests.tsv
  locator: Physical TSV rows 19
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: '[{"row": 19, "data": {"identifier": "habitatmech:BACDIVE.a4a67c4a7f",
    "requested_label": "bovine-associated environment", "parent_class": "ENVO:01001002",
    "parent_label": "animal-associated environment", "definition": "An animal-associated
    environment which is determined by a bovine.", "exact_synonym": "Bovinae-Cow,-Cattle",
    "curator": "claude-opus-5", "date": "2026-08-17", "notes": "Definition drafted
    from the record''s deep-research report under research/habitats/ and read against
    it; the report''s proposed wording, genus and near-miss table are the evidence.
    BacDive''s cattle host category.", "parent_mode": "ADD"}}]'
  snapshot_sha256: dfde49f64273cb94b4162170a5542c94880fa36015ccaac6edfa248820492a23
- evidence_id: ET11
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 1599
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: '[{"row": 1599, "data": {"identifier": "habitatmech:BACDIVE.a4a67c4a7f",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Host-taxon reversal
    (#114): this was NOT_APPLICABLE on the reasoning that ''a host taxon is not a
    habitat''. That reasoning is wrong, and the corpus already contradicted it \u2014
    the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia,
    Mammals, Birds and Fish, which keep their own identity and a term request for
    an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while
    its own child Porifera > Sponge was a term request.An organism acting as a host
    IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated,
    animal-associated and fungi-associated environment. What is not a habitat is the
    TAXON TERM \u2014 a phylum is a class of organisms, not a place \u2014 so the
    taxon stays an xref (#99) and the concept keeps its own identity as a term-request
    candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger
    and false claim. Category set to HOST_ASSOCIATED (#200): the row already claims
    ENVO:01001002 ''animal-associated environment'' as the nearest broader term, which
    is the claim that a living animal host defines the habitat, and every other record
    carrying that parent is HOST_ASSOCIATED. The category column was left blank here,
    so the seeder''s default stood and five domestic-mammal hosts stayed in OTHER
    while their siblings did not. The reasoning above is unchanged.", "review_depth":
    "ITEM", "category": "HOST_ASSOCIATED", "relation": ""}}]'
  snapshot_sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
- evidence_id: EP12
  kind: record_content
  reference: data/habitats/other/animal_associated_environment.yaml
  locator: Full parent record, context only
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: '{"identifier": "ENVO:01001002", "label": "animal-associated environment",
    "definition": "An environmental system determined by an animal.", "definition_source":
    "ENVO", "habitat_category": "OTHER", "grounding_status": "EXACT", "mapping_status":
    "SEEDED", "synonyms": [{"synonym_text": "Metazoan-associated environment", "synonym_type":
    "EXACT_SYNONYM", "source": "ENVO"}, {"synonym_text": "animal environment", "synonym_type":
    "EXACT_SYNONYM", "source": "ENVO"}], "parent_habitats": ["ENVO:01001000"], "source_attestations":
    [{"source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label":
    "host_animal", "notes": "Physicochemical parameter bands from kg-microbe''s environment
    table."}, {"source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated
    environment", "assertion_count": 144, "assertion_unit": "TAXON"}], "environmental_parameters":
    [{"parameter": "PRESSURE", "qualitative_value": "low", "source": "kg-microbe environments.csv
    (host_animal)"}, {"parameter": "TEMPERATURE_VARIABILITY", "qualitative_value":
    "low", "source": "kg-microbe environments.csv (host_animal)"}], "characteristic_taxa":
    [{"taxon_id": "NCBITaxon:1001", "source": "MADIN", "taxon_label": "flexibacter_polymorphus",
    "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1001732", "source": "MADIN", "taxon_label":
    "Mycobacterium abscessus 5S-0921", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1004165",
    "source": "MADIN", "taxon_label": "Photorhabdus luminescens caribbeanensis HG29",
    "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1004166", "source": "MADIN", "taxon_label":
    "Photorhabdus luminescens hainanensis C8404", "candidate_pool": 144}, {"taxon_id":
    "NCBITaxon:102862", "source": "MADIN", "taxon_label": "proteus_penneri", "candidate_pool":
    144}, {"taxon_id": "NCBITaxon:1028805", "source": "MADIN", "taxon_label": "Haemophilus
    haemolyticus M21621", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1049564",
    "source": "MADIN", "taxon_label": "endosymbiont of Tevnia jerichonana (vent Tica)",
    "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1084229", "source": "MADIN", "taxon_label":
    "Yersinia pestis bv. Orientalis BA200901703", "candidate_pool": 144}, {"taxon_id":
    "NCBITaxon:110933", "source": "MADIN", "taxon_label": "leifsonia_poae", "candidate_pool":
    144}, {"taxon_id": "NCBITaxon:1123042", "source": "MADIN", "taxon_label": "Photorhabdus
    temperata stackebrandtii GPS11", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123520",
    "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9686", "candidate_pool":
    144}, {"taxon_id": "NCBITaxon:1123521", "source": "MADIN", "taxon_label": "Neisseria
    meningitidis DE9622", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123522",
    "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9938", "candidate_pool":
    144}, {"taxon_id": "NCBITaxon:1125973", "source": "MADIN", "taxon_label": "Bosea
    sp. 117", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1128912", "source":
    "MADIN", "taxon_label": "Paraglaciecola mesophila KMM 241", "candidate_pool":
    144}, {"taxon_id": "NCBITaxon:1136416", "source": "MADIN", "taxon_label": "Salinispora
    pacifica CNT001", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137251", "source":
    "MADIN", "taxon_label": "Salinispora arenicola CNH905", "candidate_pool": 144},
    {"taxon_id": "NCBITaxon:1137255", "source": "MADIN", "taxon_label": "Salinispora
    arenicola CNT005", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137257", "source":
    "MADIN", "taxon_label": "Salinispora arenicola CNX508", "candidate_pool": 144},
    {"taxon_id": "NCBITaxon:1156842", "source": "MADIN", "taxon_label": "Streptomyces
    sp. LaPpAH-180", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:115862", "source":
    "MADIN", "taxon_label": "mycobacterium_caprae", "candidate_pool": 144}, {"taxon_id":
    "NCBITaxon:1159489", "source": "MADIN", "taxon_label": "Cronobacter sakazakii
    2151", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187845", "source": "MADIN",
    "taxon_label": "Vibrio genomosp. F10 9ZB36", "candidate_pool": 144}, {"taxon_id":
    "NCBITaxon:1187846", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZD137",
    "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187847", "source": "MADIN", "taxon_label":
    "Vibrio genomosp. F10 9ZC157", "candidate_pool": 144}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE,
    MADIN. Grounding: EXACT."}]}'
  snapshot_sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20260922T072807Z-bovinae_cow_cattle.md
  locator: Findings and recommended edits; historical lead
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: Legacy conclusions were compared with current target and primary evidence.
    No formal predecessor or automatic native-status requirement is inferred.
  snapshot_sha256: faa1d9a9abb159cb4a7caf3d400bd09db9250f313d4b4f77e5ec47b169a88e06
- evidence_id: ERESEARCH
  kind: record_content
  reference: research/habitats/other/bovinae-cow-cattle-habitatmech-bacdive-a4a67c4a7f-deep-research-claude_code.md
  locator: Whole bovine research report
  accessed_at: '2026-10-15T16:55:51Z'
  support: supports
  summary: The report distinguishes host environment from taxon and explicitly marks
    cattle-only scope as inference. It is not automatic evidence for every cited claim;
    the short native definition does not import its rumen parameters.
  snapshot_sha256: 108fc1d39bcda2abf44d808dd714d22ee0fa89df305801d23b12648f5ab74fde
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph
  locator: ENVO_01001000-graph.json
  accessed_at: '2026-10-15T16:34:17Z'
  support: context_only
  summary: 'Typed outgoing ontology relations, not an untyped ancestor list: [{"source":
    "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/ENVO_01000254",
    "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"},
    {"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}]'
  snapshot_sha256: e11b34dbd0a626083d5d0bbbb364469ef95831fb61cb81da5377d59715b272ca
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000
  locator: ENVO_01001000.json
  accessed_at: '2026-10-15T16:34:16Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "ENVO:01001000",
    "label": "environmental system determined by an organism", "is_obsolete": false,
    "description": ["An environmental system which is determined by a living organism."]}'
  snapshot_sha256: 8bd797929d18bf28171af7fd10f358db9b093f752d20b99f665779bb2e6b504e
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph
  locator: ENVO_01001002-graph.json
  accessed_at: '2026-10-15T16:34:19Z'
  support: context_only
  summary: 'Typed outgoing ontology relations, not an untyped ancestor list: [{"source":
    "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"},
    {"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208",
    "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}]'
  snapshot_sha256: 882375d994d0dea7166097328c56e0e22362848e68aba0125d1b128a24ebf1b0
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002
  locator: ENVO_01001002.json
  accessed_at: '2026-10-15T16:34:18Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "ENVO:01001002",
    "label": "animal-associated environment", "is_obsolete": false, "description":
    ["An environmental system determined by an animal."]}'
  snapshot_sha256: c3c90d5e91cc85727658222c907f7747f34861ad80bf1ceac5ce209f7e170907
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
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Histophilus%20somni%22%20AND%20%222336%22%20AND%20%22genome%22&format=json&resultType=core&pageSize=20
  locator: paper-somni.json
  accessed_at: '2026-10-15T16:44:08Z'
  support: context_only
  summary: 'Primary abstract PMID:39240084, DOI:10.1128/mra.00570-24: Histophilus
    somni strain 91 originated from pneumonic lung tissue of a beef calf. Supports
    one bovine-host example for this displayed species, not reidentification of the
    26 BacDive H. somni strains.'
  snapshot_sha256: 75c465acaa3367b09320bffb0584af8dd86e84830e447ffef2d16dcc393b8096
- evidence_id: EX7
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1117644,1122164,1131452,1131453,1131454,1131455,1133849,1141647,1157946,1162284,1162288,1177117,1189613,1193128,1199187,1206729,1214102,1220554,1226751,12455,1271862,1328,1329,1329902,1334,1348,1392869,147802,153721,1578,1590,1601,161879,1639,1658,1661,1679,1680,1682,1683,168808,169963,1718,1724,1796,1802,1817,184914,1886,1962118,197,198,2,205913,206,2074,2081794,222805,238,2701,28026,28087,286804,287,32002,32020,33,341199,36808,391904,439842,476,47885,480035,484020,51665,524884,653940,678,720,72407,731,747,756689,76759,82135,82348,83655,838,84107,912594,985762&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T16:34:33Z'
  support: context_only
  summary: 'All displayed IDs resolve in current NCBI Taxonomy. Preferred names and
    source labels were compared, without treating recognized historical aliases as
    wrong identities: [{"id": "NCBITaxon:731", "source": "BACDIVE", "label": "Histophilus
    somni", "current_id": "731", "current_name": "Histophilus somni", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1802", "source":
    "BACDIVE", "label": "Mycolicibacterium farcinogenes", "current_id": "1802", "current_name":
    "Mycobacterium farcinogenes", "rank": "species", "direct_match": false, "recognized_alias":
    true}, {"id": "NCBITaxon:1661", "source": "BACDIVE", "label": "Trueperella pyogenes",
    "current_id": "1661", "current_name": "Trueperella pyogenes", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:32020", "source":
    "BACDIVE", "label": "Campylobacter fetus subsp. venerealis", "current_id": "32020",
    "current_name": "Campylobacter fetus subsp. venerealis", "rank": "subspecies",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1334", "source":
    "BACDIVE", "label": "Streptococcus dysgalactiae", "current_id": "1334", "current_name":
    "Streptococcus dysgalactiae", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:197", "source": "BACDIVE", "label": "Campylobacter jejuni",
    "current_id": "197", "current_name": "Campylobacter jejuni", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1796", "source":
    "BACDIVE", "label": "Mycolicibacterium senegalense", "current_id": "1796", "current_name":
    "Mycolicibacterium senegalense", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:476", "source": "BACDIVE", "label": "Moraxella bovis",
    "current_id": "476", "current_name": "Moraxella bovis", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:153721", "source": "BACDIVE",
    "label": "Sporocytophaga myxococcoides", "current_id": "153721", "current_name":
    "Sporocytophaga myxococcoides", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1724", "source": "BACDIVE", "label": "Corynebacterium
    renale", "current_id": "1724", "current_name": "Corynebacterium renale", "rank":
    "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:184914",
    "source": "BACDIVE", "label": "Corallococcus coralloides", "current_id": "184914",
    "current_name": "Corallococcus coralloides", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1886", "source": "BACDIVE",
    "label": "Streptomyces albidoflavus", "current_id": "1886", "current_name": "Streptomyces
    albidoflavus", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:198", "source": "BACDIVE", "label": "Campylobacter hyointestinalis",
    "current_id": "198", "current_name": "Campylobacter hyointestinalis", "rank":
    "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:33",
    "source": "BACDIVE", "label": "Myxococcus fulvus", "current_id": "33", "current_name":
    "Myxococcus fulvus", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:678", "source": "BACDIVE", "label": "Vibrio sp.", "current_id":
    "678", "current_name": "Vibrio sp.", "rank": "species", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:720", "source": "BACDIVE", "label":
    "Actinobacillus lignieresii", "current_id": "720", "current_name": "Actinobacillus
    lignieresii", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:82348", "source": "BACDIVE", "label": "Streptococcus pluranimalium",
    "current_id": "82348", "current_name": "Streptococcus pluranimalium", "rank":
    "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:206",
    "source": "BACDIVE", "label": "Campylobacter sputorum", "current_id": "206", "current_name":
    "Campylobacter sputorum", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:2081794", "source": "BACDIVE", "label": "Mannheimia sp.",
    "current_id": "2081794", "current_name": "Mannheimia sp.", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:653940", "source":
    "BACDIVE", "label": "Basfia succiniciproducens", "current_id": "653940", "current_name":
    "Basfia succiniciproducens", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1329", "source": "BACDIVE", "label": "Streptococcus canis",
    "current_id": "1329", "current_name": "Streptococcus canis", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1658", "source":
    "BACDIVE", "label": "Actinomyces bovis", "current_id": "1658", "current_name":
    "Actinomyces bovis", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:2", "source": "BACDIVE", "label": "Bacteria", "current_id":
    "2", "current_name": "Bacteria", "rank": "domain", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:36808", "source": "BACDIVE", "label": "Corynebacterium
    bovis", "current_id": "36808", "current_name": "Corynebacterium bovis", "rank":
    "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:985762",
    "source": "BACDIVE", "label": "Staphylococcus agnetis", "current_id": "985762",
    "current_name": "Staphylococcus agnetis", "rank": "species", "direct_match": true,
    "recognized_alias": true}]'
  snapshot_sha256: 249c661a92762c2362c9b3b8c3a0606ef71a9369fb2600df89f8ed7f06ace644
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:BACDIVE.a4a67c4a7f -e 'bovine-associated
    environment' -e bovinae_cow_cattle -e habitatmech:BACDIVE.a4a67c4a7f curation
    history research reports data/raw build reviews
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
  summary: The minted bovine-associated environment, animal-associated genus and host
    category are supported. The authored exact alias Bovinae-Cow,-Cattle names the
    determining host rather than an environment and should not survive as exact synonymy.
    The source has 619 STRAIN assertions, a 336-taxon pool and 25 displayed taxa;
    neither the broad host definition nor the raw category establishes domestic-cattle
    exclusivity. The intentionally suppressed partial Bos taxon match is not a missing
    required xref.
  target_ids:
  - habitatmech:BACDIVE.a4a67c4a7f
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
  - ET11
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
    raw row. [{"source": "BACDIVE", "count": 619, "unit": "STRAIN"}]. Side-table biosample/study
    counts are not added to tree ORGANISM counts. Zero-count omission is not biological
    absence.'
  target_ids:
  - habitatmech:BACDIVE.a4a67c4a7f
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
  summary: The minted bovine-associated environment, animal-associated genus and host
    category are supported. The authored exact alias Bovinae-Cow,-Cattle names the
    determining host rather than an environment and should not survive as exact synonymy.
    The source has 619 STRAIN assertions, a 336-taxon pool and 25 displayed taxa;
    neither the broad host definition nor the raw category establishes domestic-cattle
    exclusivity. The intentionally suppressed partial Bos taxon match is not a missing
    required xref.
  target_ids:
  - habitatmech:BACDIVE.a4a67c4a7f
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
  - ET11
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
  summary: Actual routes reproduce UNGROUNDED/REVIEWED. No environmental-parameter,
    causal-edge, discussion/dataset or is_characteristic=true assertion is present
    in this target. Optional absence and SEEDED status alone are not defects. Scientific
    review does not promote native status.
  target_ids:
  - habitatmech:BACDIVE.a4a67c4a7f
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
  - habitatmech:BACDIVE.a4a67c4a7f
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: bovinae-cow-cattle-host-alias
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Whole-host name is an exact environment synonym
  description: Remove the authored exact synonym Bovinae-Cow,-Cattle from the native
    term request and add the guarded definition-source-label exclusion to prevent
    automatic reintroduction. Preserve the source attestation and bovine-associated
    definition; do not substitute Bos taxonomy as habitat identity or invent domestic-cattle
    exclusivity.
  target_ids:
  - habitatmech:BACDIVE.a4a67c4a7f
  field_paths:
  - synonyms
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
  - ET11
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
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
  - habitatmech:BACDIVE.a4a67c4a7f
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Remove the authored exact synonym Bovinae-Cow,-Cattle from the native
    term request and add the guarded definition-source-label exclusion to prevent
    automatic reintroduction. Preserve the source attestation and bovine-associated
    definition; do not substitute Bos taxonomy as habitat identity or invent domestic-cattle
    exclusivity. No repair is performed by this review.
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
