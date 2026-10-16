# Record review: column (BTO:0005692)

- Review: 20261016T054402Z-column-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T05:13:45Z
- Finished UTC: 2026-10-16T05:44:02Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

BTO column denotes a floral column, not a water column. Active ontology identity and frozen PREGO counts agree: 246 TAXON associations, with 25 displayed environmental-sample taxa at score four. Marine-associated names raise a homonym question but do not independently demonstrate misclassification. Original sample and dictionary provenance is unavailable here; no pair is certified as floral localization or deleted from taxonomic appearance alone.

## Scope And Provenance

Full field-by-field assessment of this one resolved generated target.

Selection: One of the next 24 unreviewed targets in deterministic path order from the ignored-inclusive 3209-record census. This bundle is not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 13cddc722250dcad4327e5f9fad0a12fe7c08268.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0005692 | data/habitats/host_associated/column.yaml | generated | column |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0005692 | Finished 2026-10-16T05:15:41Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/column.yaml |
| validate-strict | passed | True | BTO:0005692 | Finished 2026-10-16T05:17:09Z. uv run python scripts/validate_strict.py data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0005692 | Finished 2026-10-16T05:17:16Z. No issues found<br>834 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0005692 | Finished 2026-10-16T05:17:16Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0005692 | Finished 2026-10-16T05:17:32Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0005692 | Finished 2026-10-16T05:17:36Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0005692 | Finished 2026-10-16T05:17:53Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0005692 | Finished 2026-10-16T05:18:37Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted native QC | passed | True | BTO:0005692 | Verified 2026-10-16T05:19:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38852350960 |
| Candidate-pool correspondence | passed | False | BTO:0005692 | Finished 2026-10-16T05:42:35Z. All 67 displayed candidate pools equal exact source taxon totals. |
| Standalone citation validation applicability | not_applicable | False | BTO:0005692 | No standalone citation validator is documented for these generated targets without evidence objects. Current authorities verify stable references; full-corpus causal validation ran. |

## Scientific And Domain Assessments

### Identity, grounding, aliases and strict hierarchy

identity: supported. Targets: BTO:0005692.

BTO column denotes a floral column, not a water column. Active ontology identity and frozen PREGO counts agree: 246 TAXON associations, with 25 displayed environmental-sample taxa at score four. Marine-associated names raise a homonym question but do not independently demonstrate misclassification. Original sample and dictionary provenance is unavailable here; no pair is certified as floral localization or deleted from taxonomic appearance alone.

### Counts, units, taxon ranks, scores and candidate pools

quantity: supported. Targets: BTO:0005692.

Exact source rows reproduce emitted counts/units and displayed ranks/scores/pools. Zero tree counts are omitted; supplemental biosamples, study memberships and triads are nonadditive. {"assertions": [{"source": "PREGO", "count": 246, "unit": "TAXON", "row": {"row": 129, "data": {"prego_id": "BTO:0005692", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "246", "direct_assertion_count": "246", "max_prego_score": "4", "channels": "environmental_samples", "prego_synonyms": "column&#124;columns"}}}], "taxa": [{"id": "NCBITaxon:104267", "source": "PREGO", "label": "Tenacibaculum", "current_id": "104267", "current_name": "Tenacibaculum", "rank": "genus", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3011, "data": {"prego_id": "BTO:0005692", "rank": "1", "taxon_id": "NCBITaxon:104267", "taxon_label": "Tenacibaculum", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:1129", "source": "PREGO", "label": "Synechococcus", "current_id": "1129", "current_name": "Synechococcus", "rank": "genus", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3012, "data": {"prego_id": "BTO:0005692", "rank": "2", "taxon_id": "NCBITaxon:1129", "taxon_label": "Synechococcus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:118", "source": "PREGO", "label": "Planctomyces", "current_id": "118", "current_name": "Planctomyces", "rank": "genus", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3013, "data": {"prego_id": "BTO:0005692", "rank": "3", "taxon_id": "NCBITaxon:118", "taxon_label": "Planctomyces", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:1236", "source": "PREGO", "label": "Gammaproteobacteria", "current_id": "1236", "current_name": "Gammaproteobacteria", "rank": "class", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3014, "data": {"prego_id": "BTO:0005692", "rank": "4", "taxon_id": "NCBITaxon:1236", "taxon_label": "Gammaproteobacteria", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:135613", "source": "PREGO", "label": "Chromatiales", "current_id": "135613", "current_name": "Chromatiales", "rank": "order", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3015, "data": {"prego_id": "BTO:0005692", "rank": "5", "taxon_id": "NCBITaxon:135613", "taxon_label": "Chromatiales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:135619", "source": "PREGO", "label": "Oceanospirillales", "current_id": "135619", "current_name": "Oceanospirillales", "rank": "order", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3016, "data": {"prego_id": "BTO:0005692", "rank": "6", "taxon_id": "NCBITaxon:135619", "taxon_label": "Oceanospirillales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:135622", "source": "PREGO", "label": "Alteromonadales", "current_id": "135622", "current_name": "Alteromonadales", "rank": "order", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3017, "data": {"prego_id": "BTO:0005692", "rank": "7", "taxon_id": "NCBITaxon:135622", "taxon_label": "Alteromonadales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:1655514", "source": "PREGO", "label": "Candidatus Pelagibacteraceae", "current_id": "1655514", "current_name": "Candidatus Pelagibacteraceae", "rank": "family", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3018, "data": {"prego_id": "BTO:0005692", "rank": "8", "taxon_id": "NCBITaxon:1655514", "taxon_label": "Candidatus Pelagibacteraceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:1869227", "source": "PREGO", "label": "bacterium", "current_id": "1869227", "current_name": "bacterium", "rank": "species", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3019, "data": {"prego_id": "BTO:0005692", "rank": "9", "taxon_id": "NCBITaxon:1869227", "taxon_label": "bacterium", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:2", "source": "PREGO", "label": "Bacteria", "current_id": "2", "current_name": "Bacteria", "rank": "domain", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3020, "data": {"prego_id": "BTO:0005692", "rank": "10", "taxon_id": "NCBITaxon:2", "taxon_label": "Bacteria", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:200644", "source": "PREGO", "label": "Flavobacteriales", "current_id": "200644", "current_name": "Flavobacteriales", "rank": "order", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3021, "data": {"prego_id": "BTO:0005692", "rank": "11", "taxon_id": "NCBITaxon:200644", "taxon_label": "Flavobacteriales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:200666", "source": "PREGO", "label": "Sphingobacteriales", "current_id": "200666", "current_name": "Sphingobacteriales", "rank": "order", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3022, "data": {"prego_id": "BTO:0005692", "rank": "12", "taxon_id": "NCBITaxon:200666", "taxon_label": "Sphingobacteriales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:203557", "source": "PREGO", "label": "Verrucomicrobiaceae", "current_id": "203557", "current_name": "Verrucomicrobiaceae", "rank": "family", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3023, "data": {"prego_id": "BTO:0005692", "rank": "13", "taxon_id": "NCBITaxon:203557", "taxon_label": "Verrucomicrobiaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:203682", "source": "PREGO", "label": "Planctomycetota", "current_id": "203682", "current_name": "Planctomycetota", "rank": "phylum", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3024, "data": {"prego_id": "BTO:0005692", "rank": "14", "taxon_id": "NCBITaxon:203682", "taxon_label": "Planctomycetota", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:203683", "source": "PREGO", "label": "Planctomycetia", "current_id": "203683", "current_name": "Planctomycetia", "rank": "class", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3025, "data": {"prego_id": "BTO:0005692", "rank": "15", "taxon_id": "NCBITaxon:203683", "taxon_label": "Planctomycetia", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:2037", "source": "PREGO", "label": "Actinomycetales", "current_id": "2037", "current_name": "Actinomycetales", "rank": "order", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3026, "data": {"prego_id": "BTO:0005692", "rank": "16", "taxon_id": "NCBITaxon:2037", "taxon_label": "Actinomycetales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:235572", "source": "PREGO", "label": "Candidatus Portiera", "current_id": "235572", "current_name": "Candidatus Portiera", "rank": "genus", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3027, "data": {"prego_id": "BTO:0005692", "rank": "17", "taxon_id": "NCBITaxon:235572", "taxon_label": "Candidatus Portiera", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:237", "source": "PREGO", "label": "Flavobacterium", "current_id": "237", "current_name": "Flavobacterium", "rank": "genus", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3028, "data": {"prego_id": "BTO:0005692", "rank": "18", "taxon_id": "NCBITaxon:237", "taxon_label": "Flavobacterium", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:245186", "source": "PREGO", "label": "Loktanella", "current_id": "245186", "current_name": "Loktanella", "rank": "genus", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3029, "data": {"prego_id": "BTO:0005692", "rank": "19", "taxon_id": "NCBITaxon:245186", "taxon_label": "Loktanella", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:246874", "source": "PREGO", "label": "Cryomorphaceae", "current_id": "246874", "current_name": "Cryomorphaceae", "rank": "family", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3030, "data": {"prego_id": "BTO:0005692", "rank": "20", "taxon_id": "NCBITaxon:246874", "taxon_label": "Cryomorphaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:2691357", "source": "PREGO", "label": "Pirellulaceae", "current_id": "2691357", "current_name": "Pirellulaceae", "rank": "family", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3031, "data": {"prego_id": "BTO:0005692", "rank": "21", "taxon_id": "NCBITaxon:2691357", "taxon_label": "Pirellulaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:28211", "source": "PREGO", "label": "Alphaproteobacteria", "current_id": "28211", "current_name": "Alphaproteobacteria", "rank": "class", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3032, "data": {"prego_id": "BTO:0005692", "rank": "22", "taxon_id": "NCBITaxon:28211", "taxon_label": "Alphaproteobacteria", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:28216", "source": "PREGO", "label": "Betaproteobacteria", "current_id": "28216", "current_name": "Betaproteobacteria", "rank": "class", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3033, "data": {"prego_id": "BTO:0005692", "rank": "23", "taxon_id": "NCBITaxon:28216", "taxon_label": "Betaproteobacteria", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:2830", "source": "PREGO", "label": "Haptophyta", "current_id": "2830", "current_name": "Haptophyta", "rank": "phylum", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3034, "data": {"prego_id": "BTO:0005692", "rank": "24", "taxon_id": "NCBITaxon:2830", "taxon_label": "Haptophyta", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:29", "source": "PREGO", "label": "Myxococcales", "current_id": "29", "current_name": "Myxococcales", "rank": "order", "direct_match": true, "recognized_alias": true, "source_row": {"row": 3035, "data": {"prego_id": "BTO:0005692", "rank": "25", "taxon_id": "NCBITaxon:29", "taxon_label": "Myxococcales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}]}

### Association support and source limits

evidence: unknown. Targets: BTO:0005692.

BTO column denotes a floral column, not a water column. Active ontology identity and frozen PREGO counts agree: 246 TAXON associations, with 25 displayed environmental-sample taxa at score four. Marine-associated names raise a homonym question but do not independently demonstrate misclassification. Original sample and dictionary provenance is unavailable here; no pair is certified as floral localization or deleted from taxonomic appearance alone. Each cited source supports only its stated scope; original source pairs were not exhaustively reconstructed.

### Native lifecycle and optional content

completeness: supported. Targets: BTO:0005692.

Executed routes reproduce EXACT/SEEDED. Required fields are present; absent optional parameters, causal graphs, discussions and datasets are not fabricated. No scientific status promotion follows from this review.

### Native gates and exact reproduction

schema: supported. Targets: BTO:0005692.

31 baseline commands passed: individual schemas, 24-target strict validation, 834 histories, provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured labels. Exact-base hosted QC passed; deterministic validity is not scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/column.yaml; Entire generated target YAML | supports | All fields, source attestations, displayed taxa, aliases and generated history read. |
| ERULE | docs/CURATION.md; Identity, strict parents and evidence scope | supports | All parent contributions must be strictly broader; source context, host, anatomy and diagnosis are distinct. Missing optional content or ITEM status alone is not a defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and native statuses | supports | Mapping contract compares source concept to record identifier; source-is-record omits the predicate. Native count units and status gates retained. |
| ESEED | src/habitatmech/seed.py; Executed source routes and target reproduction | supports | [{"mint": "habitatmech:PREGO.a9bb4ebac2", "automatic": {"identifier": "BTO:0005692", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0005692", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; PREGO source projections | supports | Compact per-habitat tables preserve associations but do not retain original pair citations/dictionary provenance. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035 | supports | [{"row": 3011, "data": {"prego_id": "BTO:0005692", "rank": "1", "taxon_id": "NCBITaxon:104267", "taxon_label": "Tenacibaculum", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3012, "data": {"prego_id": "BTO:0005692", "rank": "2", "taxon_id": "NCBITaxon:1129", "taxon_label": "Synechococcus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3013, "data": {"prego_id": "BTO:0005692", "rank": "3", "taxon_id": "NCBITaxon:118", "taxon_label": "Planctomyces", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3014, "data": {"prego_id": "BTO:0005692", "rank": "4", "taxon_id": "NCBITaxon:1236", "taxon_label": "Gammaproteobacteria", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3015, "data": {"prego_id": "BTO:0005692", "rank": "5", "taxon_id": "NCBITaxon:135613", "taxon_label": "Chromatiales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3016, "data": {"prego_id": "BTO:0005692", "rank": "6", "taxon_id": "NCBITaxon:135619", "taxon_label": "Oceanospirillales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3017, "data": {"prego_id": "BTO:0005692", "rank": "7", "taxon_id": "NCBITaxon:135622", "taxon_label": "Alteromonadales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3018, "data": {"prego_id": "BTO:0005692", "rank": "8", "taxon_id": "NCBITaxon:1655514", "taxon_label": "Candidatus Pelagibacteraceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3019, "data": {"prego_id": "BTO:0005692", "rank": "9", "taxon_id": "NCBITaxon:1869227", "taxon_label": "bacterium", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3020, "data": {"prego_id": "BTO:0005692", "rank": "10", "taxon_id": "NCBITaxon:2", "taxon_label": "Bacteria", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3021, "data": {"prego_id": "BTO:0005692", "rank": "11", "taxon_id": "NCBITaxon:200644", "taxon_label": "Flavobacteriales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3022, "data": {"prego_id": "BTO:0005692", "rank": "12", "taxon_id": "NCBITaxon:200666", "taxon_label": "Sphingobacteriales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3023, "data": {"prego_id": "BTO:0005692", "rank": "13", "taxon_id": "NCBITaxon:203557", "taxon_label": "Verrucomicrobiaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3024, "data": {"prego_id": "BTO:0005692", "rank": "14", "taxon_id": "NCBITaxon:203682", "taxon_label": "Planctomycetota", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3025, "data": {"prego_id": "BTO:0005692", "rank": "15", "taxon_id": "NCBITaxon:203683", "taxon_label": "Planctomycetia", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3026, "data": {"prego_id": "BTO:0005692", "rank": "16", "taxon_id": "NCBITaxon:2037", "taxon_label": "Actinomycetales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3027, "data": {"prego_id": "BTO:0005692", "rank": "17", "taxon_id": "NCBITaxon:235572", "taxon_label": "Candidatus Portiera", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3028, "data": {"prego_id": "BTO:0005692", "rank": "18", "taxon_id": "NCBITaxon:237", "taxon_label": "Flavobacterium", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3029, "data": {"prego_id": "BTO:0005692", "rank": "19", "taxon_id": "NCBITaxon:245186", "taxon_label": "Loktanella", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3030, "data": {"prego_id": "BTO:0005692", "rank": "20", "taxon_id": "NCBITaxon:246874", "taxon_label": "Cryomorphaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3031, "data": {"prego_id": "BTO:0005692", "rank": "21", "taxon_id": "NCBITaxon:2691357", "taxon_label": "Pirellulaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3032, "data": {"prego_id": "BTO:0005692", "rank": "22", "taxon_id": "NCBITaxon:28211", "taxon_label": "Alphaproteobacteria", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3033, "data": {"prego_id": "BTO:0005692", "rank": "23", "taxon_id": "NCBITaxon:28216", "taxon_label": "Betaproteobacteria", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3034, "data": {"prego_id": "BTO:0005692", "rank": "24", "taxon_id": "NCBITaxon:2830", "taxon_label": "Haptophyta", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3035, "data": {"prego_id": "BTO:0005692", "rank": "25", "taxon_id": "NCBITaxon:29", "taxon_label": "Myxococcales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 129 | supports | [{"row": 129, "data": {"prego_id": "BTO:0005692", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "246", "direct_assertion_count": "246", "max_prego_score": "4", "channels": "environmental_samples", "prego_synonyms": "column&#124;columns"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 5691 | supports | [{"row": 5691, "data": {"term_id": "BTO:0005692", "ontology": "BTO", "label": "column", "definition": "A columnlike structure, especially one formed by the union of a stamen and the style in an orchid flower, or one formed by the united staminal filaments in flowers such as those of the hibiscus or mallow.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EX8 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0005692/graph; BTO_0005692-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0005692", "target": "http://purl.obolibrary.org/obo/BTO_0001559", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}] |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0005692; BTO_0005692.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "BTO:0005692", "label": "column", "is_obsolete": false, "description": ["A columnlike structure, especially one formed by the union of a stamen and the style in an orchid flower, or one formed by the united staminal filaments in flowers such as those of the hibiscus or mallow."], "obo_synonym": null} |
| EX10 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PMID:35208748; DOI:10.3390/microorganisms10020293. Inspected methods and scoring appendix: heterogeneous channels, BioProject abstract mining and capped association scores; this is not provenance for a specific retained pair. |
| EX11 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=104267,1107,1125980,1129,1154585,118,1234,1236,1268,1281779,1283,1346330,135613,135616,135619,135622,1368418,13687,1386,1400868,1405296,142182,1427368,1427369,1427370,1427371,1585697,1655514,174951,1860,186650,1869227,1883,2,20,200644,200666,200795,203557,203682,203683,203693,2037,204432,2062,213465,219685,233189,235572,237,245186,246874,2691357,28211,28216,2830,287,29,358,555793,813,86105&amp;retmode=xml; taxonomy.xml | context_only | Current exact TaxId resolutions and labels: [{"id": "NCBITaxon:104267", "source": "PREGO", "label": "Tenacibaculum", "current_id": "104267", "current_name": "Tenacibaculum", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1129", "source": "PREGO", "label": "Synechococcus", "current_id": "1129", "current_name": "Synechococcus", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:118", "source": "PREGO", "label": "Planctomyces", "current_id": "118", "current_name": "Planctomyces", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1236", "source": "PREGO", "label": "Gammaproteobacteria", "current_id": "1236", "current_name": "Gammaproteobacteria", "rank": "class", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:135613", "source": "PREGO", "label": "Chromatiales", "current_id": "135613", "current_name": "Chromatiales", "rank": "order", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:135619", "source": "PREGO", "label": "Oceanospirillales", "current_id": "135619", "current_name": "Oceanospirillales", "rank": "order", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:135622", "source": "PREGO", "label": "Alteromonadales", "current_id": "135622", "current_name": "Alteromonadales", "rank": "order", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1655514", "source": "PREGO", "label": "Candidatus Pelagibacteraceae", "current_id": "1655514", "current_name": "Candidatus Pelagibacteraceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1869227", "source": "PREGO", "label": "bacterium", "current_id": "1869227", "current_name": "bacterium", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2", "source": "PREGO", "label": "Bacteria", "current_id": "2", "current_name": "Bacteria", "rank": "domain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:200644", "source": "PREGO", "label": "Flavobacteriales", "current_id": "200644", "current_name": "Flavobacteriales", "rank": "order", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:200666", "source": "PREGO", "label": "Sphingobacteriales", "current_id": "200666", "current_name": "Sphingobacteriales", "rank": "order", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:203557", "source": "PREGO", "label": "Verrucomicrobiaceae", "current_id": "203557", "current_name": "Verrucomicrobiaceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:203682", "source": "PREGO", "label": "Planctomycetota", "current_id": "203682", "current_name": "Planctomycetota", "rank": "phylum", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:203683", "source": "PREGO", "label": "Planctomycetia", "current_id": "203683", "current_name": "Planctomycetia", "rank": "class", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2037", "source": "PREGO", "label": "Actinomycetales", "current_id": "2037", "current_name": "Actinomycetales", "rank": "order", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:235572", "source": "PREGO", "label": "Candidatus Portiera", "current_id": "235572", "current_name": "Candidatus Portiera", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:237", "source": "PREGO", "label": "Flavobacterium", "current_id": "237", "current_name": "Flavobacterium", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:245186", "source": "PREGO", "label": "Loktanella", "current_id": "245186", "current_name": "Loktanella", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:246874", "source": "PREGO", "label": "Cryomorphaceae", "current_id": "246874", "current_name": "Cryomorphaceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2691357", "source": "PREGO", "label": "Pirellulaceae", "current_id": "2691357", "current_name": "Pirellulaceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28211", "source": "PREGO", "label": "Alphaproteobacteria", "current_id": "28211", "current_name": "Alphaproteobacteria", "rank": "class", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28216", "source": "PREGO", "label": "Betaproteobacteria", "current_id": "28216", "current_name": "Betaproteobacteria", "rank": "class", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2830", "source": "PREGO", "label": "Haptophyta", "current_id": "2830", "current_name": "Haptophyta", "rank": "phylum", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:29", "source": "PREGO", "label": "Myxococcales", "current_id": "29", "current_name": "Myxococcales", "rank": "order", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local source and review corpus; rg --no-ignore --hidden -l -F -e BTO:0005692 -e column -e column -e habitatmech:PREGO.a9bb4ebac2 curation history research reports data/raw build reviews | context_only | Exact source keys and structured archive parsed independently; broad name hits are leads, not all inspected. No formal target predecessor. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -ipath '*prego*' | context_only | No PREGO-named files found in the configured checkout. This is not a claim of global source absence. |

## Limits And Additional Notes

- Original specimen-level evidence and all pair-level citations were not exhaustively reconstructed. Native association counts, taxon ranks and scores do not establish prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs. Exact target TaxIds were separately resolved; frozen taxon labels are not universally current.
- Exact-base hosted QC covers unchanged scientific inputs, not a fresh local full-QC execution or these new review outputs. Native validate/save and subsequent archive/final-head gates are separate.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. No new causal mechanism is imported.
- Original PREGO pair exports were unavailable in the configured checkout. No uncertain association or source total is changed by this review.
- Floral/water-column or anatomical/agricultural-crop polysemy remains a bounded unknown. Taxonomic appearance alone is insufficient evidence for a major misclassification finding.
- All captured local input hashes were independently checked against exact base 13cddc722250dcad4327e5f9fad0a12fe7c08268.
- This baseline observation changes no scientific input. Separately authorized PR remediation follows; no status promotion is conferred by review validation.
- Ignored-inclusive structured archive traversal found no formal previous target review. Legacy reports are context, not predecessor lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T054402Z-column-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: column (BTO:0005692)'
started_at: '2026-10-16T05:13:45Z'
finished_at: '2026-10-16T05:44:02Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Parent agent integrates evidence and separate-agent source/hierarchy
    cross-checks; not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'BTO column denotes a floral column, not a water column. Active ontology
  identity and frozen PREGO counts agree: 246 TAXON associations, with 25 displayed
  environmental-sample taxa at score four. Marine-associated names raise a homonym
  question but do not independently demonstrate misclassification. Original sample
  and dictionary provenance is unavailable here; no pair is certified as floral localization
  or deleted from taxonomic appearance alone.'
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
  - path: data/habitats/host_associated/column.yaml
    sha256: bfd6f3443276da9a958e5c550b896e03d0054676ecf700a6ae221c14a07b2240
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
- target_id: BTO:0005692
  path: data/habitats/host_associated/column.yaml
  label: column
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
  - BTO:0005692
  exclusions:
  - target: Other records, original specimens and SSSOM/KGX products
    reason: Parents are contextual evidence, not additional review coverage; original
      specimens and exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/column.yaml
  exit_code: 0
  target_ids:
  - BTO:0005692
  summary: "Finished 2026-10-16T05:15:41Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/column.yaml"
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
  - BTO:0005692
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
  - BTO:0005692
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
  - BTO:0005692
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
  - BTO:0005692
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
  - BTO:0005692
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
  - BTO:0005692
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
  - BTO:0005692
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
  - BTO:0005692
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
  - BTO:0005692
  summary: Finished 2026-10-16T05:42:35Z. All 67 displayed candidate pools equal exact
    source taxon totals.
  scope_note: Supplemental exact source-total check, not a replacement for native
    validators or scientific evidence.
- check_id: CREF
  name: Standalone citation validation applicability
  status: not_applicable
  required: false
  target_ids:
  - BTO:0005692
  summary: No standalone citation validator is documented for these generated targets
    without evidence objects. Current authorities verify stable references; full-corpus
    causal validation ran.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/column.yaml
  locator: Entire generated target YAML
  accessed_at: '2026-10-16T05:44:02Z'
  support: supports
  summary: All fields, source attestations, displayed taxa, aliases and generated
    history read.
  snapshot_sha256: bfd6f3443276da9a958e5c550b896e03d0054676ecf700a6ae221c14a07b2240
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strict parents and evidence scope
  accessed_at: '2026-10-16T05:44:02Z'
  support: supports
  summary: All parent contributions must be strictly broader; source context, host,
    anatomy and diagnosis are distinct. Missing optional content or ITEM status alone
    is not a defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and native statuses
  accessed_at: '2026-10-16T05:44:02Z'
  support: supports
  summary: Mapping contract compares source concept to record identifier; source-is-record
    omits the predicate. Native count units and status gates retained.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source routes and target reproduction
  accessed_at: '2026-10-16T05:44:02Z'
  support: supports
  summary: '[{"mint": "habitatmech:PREGO.a9bb4ebac2", "automatic": {"identifier":
    "BTO:0005692", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0005692", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: PREGO source projections
  accessed_at: '2026-10-16T05:44:02Z'
  support: supports
  summary: Compact per-habitat tables preserve associations but do not retain original
    pair citations/dictionary provenance.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035
  accessed_at: '2026-10-16T05:44:02Z'
  support: supports
  summary: '[{"row": 3011, "data": {"prego_id": "BTO:0005692", "rank": "1", "taxon_id":
    "NCBITaxon:104267", "taxon_label": "Tenacibaculum", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    3012, "data": {"prego_id": "BTO:0005692", "rank": "2", "taxon_id": "NCBITaxon:1129",
    "taxon_label": "Synechococcus", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 3013, "data": {"prego_id":
    "BTO:0005692", "rank": "3", "taxon_id": "NCBITaxon:118", "taxon_label": "Planctomyces",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 3014, "data": {"prego_id": "BTO:0005692", "rank":
    "4", "taxon_id": "NCBITaxon:1236", "taxon_label": "Gammaproteobacteria", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 3015, "data": {"prego_id": "BTO:0005692", "rank": "5", "taxon_id":
    "NCBITaxon:135613", "taxon_label": "Chromatiales", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    3016, "data": {"prego_id": "BTO:0005692", "rank": "6", "taxon_id": "NCBITaxon:135619",
    "taxon_label": "Oceanospirillales", "prego_score": "4", "direct_flag": "TRUE",
    "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3017, "data":
    {"prego_id": "BTO:0005692", "rank": "7", "taxon_id": "NCBITaxon:135622", "taxon_label":
    "Alteromonadales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 3018, "data": {"prego_id": "BTO:0005692", "rank":
    "8", "taxon_id": "NCBITaxon:1655514", "taxon_label": "Candidatus Pelagibacteraceae",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 3019, "data": {"prego_id": "BTO:0005692", "rank":
    "9", "taxon_id": "NCBITaxon:1869227", "taxon_label": "bacterium", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 3020, "data": {"prego_id": "BTO:0005692", "rank": "10", "taxon_id":
    "NCBITaxon:2", "taxon_label": "Bacteria", "prego_score": "4", "direct_flag": "TRUE",
    "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3021, "data":
    {"prego_id": "BTO:0005692", "rank": "11", "taxon_id": "NCBITaxon:200644", "taxon_label":
    "Flavobacteriales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 3022, "data": {"prego_id": "BTO:0005692", "rank":
    "12", "taxon_id": "NCBITaxon:200666", "taxon_label": "Sphingobacteriales", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 3023, "data": {"prego_id": "BTO:0005692", "rank": "13", "taxon_id":
    "NCBITaxon:203557", "taxon_label": "Verrucomicrobiaceae", "prego_score": "4",
    "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 3024, "data": {"prego_id": "BTO:0005692", "rank": "14", "taxon_id":
    "NCBITaxon:203682", "taxon_label": "Planctomycetota", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    3025, "data": {"prego_id": "BTO:0005692", "rank": "15", "taxon_id": "NCBITaxon:203683",
    "taxon_label": "Planctomycetia", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 3026, "data": {"prego_id":
    "BTO:0005692", "rank": "16", "taxon_id": "NCBITaxon:2037", "taxon_label": "Actinomycetales",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 3027, "data": {"prego_id": "BTO:0005692", "rank":
    "17", "taxon_id": "NCBITaxon:235572", "taxon_label": "Candidatus Portiera", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 3028, "data": {"prego_id": "BTO:0005692", "rank": "18", "taxon_id":
    "NCBITaxon:237", "taxon_label": "Flavobacterium", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    3029, "data": {"prego_id": "BTO:0005692", "rank": "19", "taxon_id": "NCBITaxon:245186",
    "taxon_label": "Loktanella", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 3030, "data": {"prego_id":
    "BTO:0005692", "rank": "20", "taxon_id": "NCBITaxon:246874", "taxon_label": "Cryomorphaceae",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 3031, "data": {"prego_id": "BTO:0005692", "rank":
    "21", "taxon_id": "NCBITaxon:2691357", "taxon_label": "Pirellulaceae", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 3032, "data": {"prego_id": "BTO:0005692", "rank": "22", "taxon_id":
    "NCBITaxon:28211", "taxon_label": "Alphaproteobacteria", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    3033, "data": {"prego_id": "BTO:0005692", "rank": "23", "taxon_id": "NCBITaxon:28216",
    "taxon_label": "Betaproteobacteria", "prego_score": "4", "direct_flag": "TRUE",
    "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 3034, "data":
    {"prego_id": "BTO:0005692", "rank": "24", "taxon_id": "NCBITaxon:2830", "taxon_label":
    "Haptophyta", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 3035, "data": {"prego_id": "BTO:0005692", "rank":
    "25", "taxon_id": "NCBITaxon:29", "taxon_label": "Myxococcales", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 129
  accessed_at: '2026-10-16T05:44:02Z'
  support: supports
  summary: '[{"row": 129, "data": {"prego_id": "BTO:0005692", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "246", "direct_assertion_count":
    "246", "max_prego_score": "4", "channels": "environmental_samples", "prego_synonyms":
    "column|columns"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 5691
  accessed_at: '2026-10-16T05:44:02Z'
  support: supports
  summary: '[{"row": 5691, "data": {"term_id": "BTO:0005692", "ontology": "BTO", "label":
    "column", "definition": "A columnlike structure, especially one formed by the
    union of a stamen and the style in an orchid flower, or one formed by the united
    staminal filaments in flowers such as those of the hibiscus or mallow.", "synonyms":
    "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EX8
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0005692/graph
  locator: BTO_0005692-graph.json
  accessed_at: '2026-10-16T05:15:42Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0005692",
    "target": "http://purl.obolibrary.org/obo/BTO_0001559", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}]'
  snapshot_sha256: d906210e67928de6b6f263ad2ed429b4364ea02757a5b5b1650a3f7f582713ad
- evidence_id: EX9
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0005692
  locator: BTO_0005692.json
  accessed_at: '2026-10-16T05:15:41Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "BTO:0005692", "label": "column", "is_obsolete": false, "description": ["A columnlike
    structure, especially one formed by the union of a stamen and the style in an
    orchid flower, or one formed by the united staminal filaments in flowers such
    as those of the hibiscus or mallow."], "obo_synonym": null}'
  snapshot_sha256: 23762f766b153d86d82eb80e3f12eeda39e2adb17de4ecc8a8d14fb7a9c0b491
- evidence_id: EX10
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-16T05:18:44Z'
  support: context_only
  summary: 'PMID:35208748; DOI:10.3390/microorganisms10020293. Inspected methods and
    scoring appendix: heterogeneous channels, BioProject abstract mining and capped
    association scores; this is not provenance for a specific retained pair.'
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX11
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=104267,1107,1125980,1129,1154585,118,1234,1236,1268,1281779,1283,1346330,135613,135616,135619,135622,1368418,13687,1386,1400868,1405296,142182,1427368,1427369,1427370,1427371,1585697,1655514,174951,1860,186650,1869227,1883,2,20,200644,200666,200795,203557,203682,203683,203693,2037,204432,2062,213465,219685,233189,235572,237,245186,246874,2691357,28211,28216,2830,287,29,358,555793,813,86105&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-16T05:16:21Z'
  support: context_only
  summary: 'Current exact TaxId resolutions and labels: [{"id": "NCBITaxon:104267",
    "source": "PREGO", "label": "Tenacibaculum", "current_id": "104267", "current_name":
    "Tenacibaculum", "rank": "genus", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:1129", "source": "PREGO", "label": "Synechococcus", "current_id":
    "1129", "current_name": "Synechococcus", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:118", "source": "PREGO", "label":
    "Planctomyces", "current_id": "118", "current_name": "Planctomyces", "rank": "genus",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1236", "source":
    "PREGO", "label": "Gammaproteobacteria", "current_id": "1236", "current_name":
    "Gammaproteobacteria", "rank": "class", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:135613", "source": "PREGO", "label": "Chromatiales",
    "current_id": "135613", "current_name": "Chromatiales", "rank": "order", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:135619", "source": "PREGO",
    "label": "Oceanospirillales", "current_id": "135619", "current_name": "Oceanospirillales",
    "rank": "order", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:135622",
    "source": "PREGO", "label": "Alteromonadales", "current_id": "135622", "current_name":
    "Alteromonadales", "rank": "order", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1655514", "source": "PREGO", "label": "Candidatus Pelagibacteraceae",
    "current_id": "1655514", "current_name": "Candidatus Pelagibacteraceae", "rank":
    "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1869227",
    "source": "PREGO", "label": "bacterium", "current_id": "1869227", "current_name":
    "bacterium", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:2", "source": "PREGO", "label": "Bacteria", "current_id": "2",
    "current_name": "Bacteria", "rank": "domain", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:200644", "source": "PREGO", "label": "Flavobacteriales",
    "current_id": "200644", "current_name": "Flavobacteriales", "rank": "order", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:200666", "source": "PREGO",
    "label": "Sphingobacteriales", "current_id": "200666", "current_name": "Sphingobacteriales",
    "rank": "order", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:203557",
    "source": "PREGO", "label": "Verrucomicrobiaceae", "current_id": "203557", "current_name":
    "Verrucomicrobiaceae", "rank": "family", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:203682", "source": "PREGO", "label": "Planctomycetota",
    "current_id": "203682", "current_name": "Planctomycetota", "rank": "phylum", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:203683", "source": "PREGO",
    "label": "Planctomycetia", "current_id": "203683", "current_name": "Planctomycetia",
    "rank": "class", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2037",
    "source": "PREGO", "label": "Actinomycetales", "current_id": "2037", "current_name":
    "Actinomycetales", "rank": "order", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:235572", "source": "PREGO", "label": "Candidatus Portiera",
    "current_id": "235572", "current_name": "Candidatus Portiera", "rank": "genus",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:237", "source":
    "PREGO", "label": "Flavobacterium", "current_id": "237", "current_name": "Flavobacterium",
    "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:245186",
    "source": "PREGO", "label": "Loktanella", "current_id": "245186", "current_name":
    "Loktanella", "rank": "genus", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:246874", "source": "PREGO", "label": "Cryomorphaceae", "current_id":
    "246874", "current_name": "Cryomorphaceae", "rank": "family", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:2691357", "source": "PREGO",
    "label": "Pirellulaceae", "current_id": "2691357", "current_name": "Pirellulaceae",
    "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28211",
    "source": "PREGO", "label": "Alphaproteobacteria", "current_id": "28211", "current_name":
    "Alphaproteobacteria", "rank": "class", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:28216", "source": "PREGO", "label": "Betaproteobacteria",
    "current_id": "28216", "current_name": "Betaproteobacteria", "rank": "class",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2830", "source":
    "PREGO", "label": "Haptophyta", "current_id": "2830", "current_name": "Haptophyta",
    "rank": "phylum", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:29",
    "source": "PREGO", "label": "Myxococcales", "current_id": "29", "current_name":
    "Myxococcales", "rank": "order", "direct_match": true, "recognized_alias": true}]'
  snapshot_sha256: c87693dd48667514d7e3c5fdf2b1d629f2c9c10b8749bf4e88cdc26a65349549
- evidence_id: ESEARCH
  kind: search
  reference: Local source and review corpus
  locator: rg --no-ignore --hidden -l -F -e BTO:0005692 -e column -e column -e habitatmech:PREGO.a9bb4ebac2
    curation history research reports data/raw build reviews
  accessed_at: '2026-10-16T05:15:46Z'
  support: context_only
  summary: Exact source keys and structured archive parsed independently; broad name
    hits are leads, not all inspected. No formal target predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews
    including hidden/ignored files; independent structured YAML traversal.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -ipath '*prego*'
  accessed_at: '2026-10-16T05:18:55Z'
  support: context_only
  summary: No PREGO-named files found in the configured checkout. This is not a claim
    of global source absence.
  search_scope: find includes hidden and ignored files throughout the configured checkout.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, grounding, aliases and strict hierarchy
  outcome: supported
  summary: 'BTO column denotes a floral column, not a water column. Active ontology
    identity and frozen PREGO counts agree: 246 TAXON associations, with 25 displayed
    environmental-sample taxa at score four. Marine-associated names raise a homonym
    question but do not independently demonstrate misclassification. Original sample
    and dictionary provenance is unavailable here; no pair is certified as floral
    localization or deleted from taxonomic appearance alone.'
  target_ids:
  - BTO:0005692
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EX8
  - EX9
  - EX10
  - EX11
- assessment_id: A2
  area: quantity
  topic: Counts, units, taxon ranks, scores and candidate pools
  outcome: supported
  summary: 'Exact source rows reproduce emitted counts/units and displayed ranks/scores/pools.
    Zero tree counts are omitted; supplemental biosamples, study memberships and triads
    are nonadditive. {"assertions": [{"source": "PREGO", "count": 246, "unit": "TAXON",
    "row": {"row": 129, "data": {"prego_id": "BTO:0005692", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "246", "direct_assertion_count":
    "246", "max_prego_score": "4", "channels": "environmental_samples", "prego_synonyms":
    "column|columns"}}}], "taxa": [{"id": "NCBITaxon:104267", "source": "PREGO", "label":
    "Tenacibaculum", "current_id": "104267", "current_name": "Tenacibaculum", "rank":
    "genus", "direct_match": true, "recognized_alias": true, "source_row": {"row":
    3011, "data": {"prego_id": "BTO:0005692", "rank": "1", "taxon_id": "NCBITaxon:104267",
    "taxon_label": "Tenacibaculum", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:1129", "source":
    "PREGO", "label": "Synechococcus", "current_id": "1129", "current_name": "Synechococcus",
    "rank": "genus", "direct_match": true, "recognized_alias": true, "source_row":
    {"row": 3012, "data": {"prego_id": "BTO:0005692", "rank": "2", "taxon_id": "NCBITaxon:1129",
    "taxon_label": "Synechococcus", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:118", "source":
    "PREGO", "label": "Planctomyces", "current_id": "118", "current_name": "Planctomyces",
    "rank": "genus", "direct_match": true, "recognized_alias": true, "source_row":
    {"row": 3013, "data": {"prego_id": "BTO:0005692", "rank": "3", "taxon_id": "NCBITaxon:118",
    "taxon_label": "Planctomyces", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:1236", "source":
    "PREGO", "label": "Gammaproteobacteria", "current_id": "1236", "current_name":
    "Gammaproteobacteria", "rank": "class", "direct_match": true, "recognized_alias":
    true, "source_row": {"row": 3014, "data": {"prego_id": "BTO:0005692", "rank":
    "4", "taxon_id": "NCBITaxon:1236", "taxon_label": "Gammaproteobacteria", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:135613", "source": "PREGO", "label": "Chromatiales",
    "current_id": "135613", "current_name": "Chromatiales", "rank": "order", "direct_match":
    true, "recognized_alias": true, "source_row": {"row": 3015, "data": {"prego_id":
    "BTO:0005692", "rank": "5", "taxon_id": "NCBITaxon:135613", "taxon_label": "Chromatiales",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}}, {"id": "NCBITaxon:135619", "source": "PREGO", "label":
    "Oceanospirillales", "current_id": "135619", "current_name": "Oceanospirillales",
    "rank": "order", "direct_match": true, "recognized_alias": true, "source_row":
    {"row": 3016, "data": {"prego_id": "BTO:0005692", "rank": "6", "taxon_id": "NCBITaxon:135619",
    "taxon_label": "Oceanospirillales", "prego_score": "4", "direct_flag": "TRUE",
    "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:135622",
    "source": "PREGO", "label": "Alteromonadales", "current_id": "135622", "current_name":
    "Alteromonadales", "rank": "order", "direct_match": true, "recognized_alias":
    true, "source_row": {"row": 3017, "data": {"prego_id": "BTO:0005692", "rank":
    "7", "taxon_id": "NCBITaxon:135622", "taxon_label": "Alteromonadales", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:1655514", "source": "PREGO", "label": "Candidatus Pelagibacteraceae",
    "current_id": "1655514", "current_name": "Candidatus Pelagibacteraceae", "rank":
    "family", "direct_match": true, "recognized_alias": true, "source_row": {"row":
    3018, "data": {"prego_id": "BTO:0005692", "rank": "8", "taxon_id": "NCBITaxon:1655514",
    "taxon_label": "Candidatus Pelagibacteraceae", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}}, {"id":
    "NCBITaxon:1869227", "source": "PREGO", "label": "bacterium", "current_id": "1869227",
    "current_name": "bacterium", "rank": "species", "direct_match": true, "recognized_alias":
    true, "source_row": {"row": 3019, "data": {"prego_id": "BTO:0005692", "rank":
    "9", "taxon_id": "NCBITaxon:1869227", "taxon_label": "bacterium", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:2", "source": "PREGO", "label": "Bacteria", "current_id":
    "2", "current_name": "Bacteria", "rank": "domain", "direct_match": true, "recognized_alias":
    true, "source_row": {"row": 3020, "data": {"prego_id": "BTO:0005692", "rank":
    "10", "taxon_id": "NCBITaxon:2", "taxon_label": "Bacteria", "prego_score": "4",
    "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:200644", "source": "PREGO", "label": "Flavobacteriales",
    "current_id": "200644", "current_name": "Flavobacteriales", "rank": "order", "direct_match":
    true, "recognized_alias": true, "source_row": {"row": 3021, "data": {"prego_id":
    "BTO:0005692", "rank": "11", "taxon_id": "NCBITaxon:200644", "taxon_label": "Flavobacteriales",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}}, {"id": "NCBITaxon:200666", "source": "PREGO", "label":
    "Sphingobacteriales", "current_id": "200666", "current_name": "Sphingobacteriales",
    "rank": "order", "direct_match": true, "recognized_alias": true, "source_row":
    {"row": 3022, "data": {"prego_id": "BTO:0005692", "rank": "12", "taxon_id": "NCBITaxon:200666",
    "taxon_label": "Sphingobacteriales", "prego_score": "4", "direct_flag": "TRUE",
    "channels": "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:203557",
    "source": "PREGO", "label": "Verrucomicrobiaceae", "current_id": "203557", "current_name":
    "Verrucomicrobiaceae", "rank": "family", "direct_match": true, "recognized_alias":
    true, "source_row": {"row": 3023, "data": {"prego_id": "BTO:0005692", "rank":
    "13", "taxon_id": "NCBITaxon:203557", "taxon_label": "Verrucomicrobiaceae", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:203682", "source": "PREGO", "label": "Planctomycetota",
    "current_id": "203682", "current_name": "Planctomycetota", "rank": "phylum", "direct_match":
    true, "recognized_alias": true, "source_row": {"row": 3024, "data": {"prego_id":
    "BTO:0005692", "rank": "14", "taxon_id": "NCBITaxon:203682", "taxon_label": "Planctomycetota",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}}, {"id": "NCBITaxon:203683", "source": "PREGO", "label":
    "Planctomycetia", "current_id": "203683", "current_name": "Planctomycetia", "rank":
    "class", "direct_match": true, "recognized_alias": true, "source_row": {"row":
    3025, "data": {"prego_id": "BTO:0005692", "rank": "15", "taxon_id": "NCBITaxon:203683",
    "taxon_label": "Planctomycetia", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:2037", "source":
    "PREGO", "label": "Actinomycetales", "current_id": "2037", "current_name": "Actinomycetales",
    "rank": "order", "direct_match": true, "recognized_alias": true, "source_row":
    {"row": 3026, "data": {"prego_id": "BTO:0005692", "rank": "16", "taxon_id": "NCBITaxon:2037",
    "taxon_label": "Actinomycetales", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:235572",
    "source": "PREGO", "label": "Candidatus Portiera", "current_id": "235572", "current_name":
    "Candidatus Portiera", "rank": "genus", "direct_match": true, "recognized_alias":
    true, "source_row": {"row": 3027, "data": {"prego_id": "BTO:0005692", "rank":
    "17", "taxon_id": "NCBITaxon:235572", "taxon_label": "Candidatus Portiera", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:237", "source": "PREGO", "label": "Flavobacterium", "current_id":
    "237", "current_name": "Flavobacterium", "rank": "genus", "direct_match": true,
    "recognized_alias": true, "source_row": {"row": 3028, "data": {"prego_id": "BTO:0005692",
    "rank": "18", "taxon_id": "NCBITaxon:237", "taxon_label": "Flavobacterium", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:245186", "source": "PREGO", "label": "Loktanella", "current_id":
    "245186", "current_name": "Loktanella", "rank": "genus", "direct_match": true,
    "recognized_alias": true, "source_row": {"row": 3029, "data": {"prego_id": "BTO:0005692",
    "rank": "19", "taxon_id": "NCBITaxon:245186", "taxon_label": "Loktanella", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:246874", "source": "PREGO", "label": "Cryomorphaceae",
    "current_id": "246874", "current_name": "Cryomorphaceae", "rank": "family", "direct_match":
    true, "recognized_alias": true, "source_row": {"row": 3030, "data": {"prego_id":
    "BTO:0005692", "rank": "20", "taxon_id": "NCBITaxon:246874", "taxon_label": "Cryomorphaceae",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}}, {"id": "NCBITaxon:2691357", "source": "PREGO", "label":
    "Pirellulaceae", "current_id": "2691357", "current_name": "Pirellulaceae", "rank":
    "family", "direct_match": true, "recognized_alias": true, "source_row": {"row":
    3031, "data": {"prego_id": "BTO:0005692", "rank": "21", "taxon_id": "NCBITaxon:2691357",
    "taxon_label": "Pirellulaceae", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}}, {"id": "NCBITaxon:28211", "source":
    "PREGO", "label": "Alphaproteobacteria", "current_id": "28211", "current_name":
    "Alphaproteobacteria", "rank": "class", "direct_match": true, "recognized_alias":
    true, "source_row": {"row": 3032, "data": {"prego_id": "BTO:0005692", "rank":
    "22", "taxon_id": "NCBITaxon:28211", "taxon_label": "Alphaproteobacteria", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:28216", "source": "PREGO", "label": "Betaproteobacteria",
    "current_id": "28216", "current_name": "Betaproteobacteria", "rank": "class",
    "direct_match": true, "recognized_alias": true, "source_row": {"row": 3033, "data":
    {"prego_id": "BTO:0005692", "rank": "23", "taxon_id": "NCBITaxon:28216", "taxon_label":
    "Betaproteobacteria", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}}, {"id": "NCBITaxon:2830", "source": "PREGO", "label":
    "Haptophyta", "current_id": "2830", "current_name": "Haptophyta", "rank": "phylum",
    "direct_match": true, "recognized_alias": true, "source_row": {"row": 3034, "data":
    {"prego_id": "BTO:0005692", "rank": "24", "taxon_id": "NCBITaxon:2830", "taxon_label":
    "Haptophyta", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}}, {"id": "NCBITaxon:29", "source": "PREGO", "label": "Myxococcales",
    "current_id": "29", "current_name": "Myxococcales", "rank": "order", "direct_match":
    true, "recognized_alias": true, "source_row": {"row": 3035, "data": {"prego_id":
    "BTO:0005692", "rank": "25", "taxon_id": "NCBITaxon:29", "taxon_label": "Myxococcales",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}}]}'
  target_ids:
  - BTO:0005692
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EX8
  - EX9
  - EX10
  - EX11
- assessment_id: A3
  area: evidence
  topic: Association support and source limits
  outcome: unknown
  summary: 'BTO column denotes a floral column, not a water column. Active ontology
    identity and frozen PREGO counts agree: 246 TAXON associations, with 25 displayed
    environmental-sample taxa at score four. Marine-associated names raise a homonym
    question but do not independently demonstrate misclassification. Original sample
    and dictionary provenance is unavailable here; no pair is certified as floral
    localization or deleted from taxonomic appearance alone. Each cited source supports
    only its stated scope; original source pairs were not exhaustively reconstructed.'
  target_ids:
  - BTO:0005692
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EX8
  - EX9
  - EX10
  - EX11
- assessment_id: A4
  area: completeness
  topic: Native lifecycle and optional content
  outcome: supported
  summary: Executed routes reproduce EXACT/SEEDED. Required fields are present; absent
    optional parameters, causal graphs, discussions and datasets are not fabricated.
    No scientific status promotion follows from this review.
  target_ids:
  - BTO:0005692
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
  - BTO:0005692
  evidence_ids:
  - E1
  - ESCHEMA
  - ERULE
findings: []
actions: []
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
- Original PREGO pair exports were unavailable in the configured checkout. No uncertain
  association or source total is changed by this review.
- Floral/water-column or anatomical/agricultural-crop polysemy remains a bounded unknown.
  Taxonomic appearance alone is insufficient evidence for a major misclassification
  finding.
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
