# Record review: bladder (BTO:0000123)

- Review: 20261015T125452Z-bladder-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T12:40:42Z
- Finished UTC: 2026-10-15T12:54:52Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The generic BTO bladder identity and viscus superclass are supported, without narrowing all animal liquid/gas sacs to urinary bladder. PREGO preserves 32 taxa and 25 displayed rows. A TOP379 sequence record identifies human urine, and the linked study examines both intestinal and urinary isolates; this supports bounded urinary context, not all 32 bladder-localization claims.

## Scope And Provenance

Scientific review of one exact target at 68ceabb7039a537f65be44ac6aaa913116a154f5.

Selection: First seven records in the prepared next-twenty path-ordered cohort; this bundle assesses exactly one resolved identifier.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 68ceabb7039a537f65be44ac6aaa913116a154f5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000123 | data/habitats/host_associated/bladder.yaml | generated | bladder |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000123 | Completed 2026-10-15T12:40:45Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bladder.yaml |
| validate-strict | passed | True | BTO:0000123 | Completed 2026-10-15T12:41:35Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml data/habitats/host_associated/blast_cell.yaml data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000123 | Completed 2026-10-15T12:41:43Z. No issues found<br>808 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000123 | Completed 2026-10-15T12:41:44Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000123 | Completed 2026-10-15T12:41:58Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000123 | Completed 2026-10-15T12:42:02Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000123 | Completed 2026-10-15T12:42:18Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000123 | Completed 2026-10-15T12:42:59Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-revision baseline full QC | passed | True | BTO:0000123 | Verified 2026-10-15T12:40:46Z: https://github.com/CultureBotAI/HabitatMech/actions/runs/38733485444 |

## Scientific And Domain Assessments

### Native validation and reproduction

schema: supported. Targets: BTO:0000123.

Schema, strict, history, provenance, 3,208-record reproduction, causal overlays, term requests and configured labels passed. These establish deterministic fidelity, not scientific support.

### Identity, hierarchy and nomenclature

identity: supported. Targets: BTO:0000123.

The generic BTO bladder identity and viscus superclass are supported, without narrowing all animal liquid/gas sacs to urinary bladder. PREGO preserves 32 taxa and 25 displayed rows. A TOP379 sequence record identifies human urine, and the linked study examines both intestinal and urinary isolates; this supports bounded urinary context, not all 32 bladder-localization claims.

### Source count, unit and ranking

quantity: supported. Targets: BTO:0000123.

Exact source projections retain [{"source": "PREGO", "source_id": "BTO:0000123", "source_label": "bladder", "assertion_count": 32, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}]. All 25 displayed taxa were resolved against current NCBI IDs/labels. Ranks and candidate pools are source-specific; unlike units are never summed.

### Native status and optional fields

completeness: supported. Targets: BTO:0000123.

Executed source decisions reproduce EXACT/SEEDED. No causal mechanism or is_characteristic assertion is present. Missing optional fields or SEEDED status are not automatic scientific defects.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bladder.yaml; Entire target YAML | supports | Read the full target including source paths, taxa, hierarchy and history. |
| ERULE | docs/CURATION.md; Identity, broader-parent and ownership rules | supports | Context, containment and whole-host identity differ from strictly broader habitat ancestry. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and CharacteristicTaxon | supports | Mapping endpoints, assertion units and association versus characteristic-presence semantics. |
| ESEED | src/habitatmech/seed.py; Executed native source resolution | supports | Exact routes: [{"source": "PREGO", "mint": "habitatmech:PREGO.309b2fc00e", "automatic": {"identifier": "BTO:0000123", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000123", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; extract_prego | supports | Projection preserves distinct-taxon totals and score/channel ranking but not original pair citations. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112 | supports | [{"row": 88, "data": {"prego_id": "BTO:0000123", "rank": "1", "taxon_id": "NCBITaxon:1206108", "taxon_label": "Escherichia coli J96", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 89, "data": {"prego_id": "BTO:0000123", "rank": "2", "taxon_id": "NCBITaxon:1286329", "taxon_label": "Escherichia coli TOP379", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 90, "data": {"prego_id": "BTO:0000123", "rank": "3", "taxon_id": "NCBITaxon:1286330", "taxon_label": "Escherichia coli TOP382-1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 91, "data": {"prego_id": "BTO:0000123", "rank": "4", "taxon_id": "NCBITaxon:1286331", "taxon_label": "Escherichia coli TOP382-2", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 92, "data": {"prego_id": "BTO:0000123", "rank": "5", "taxon_id": "NCBITaxon:1286332", "taxon_label": "Escherichia coli TOP382-3", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 93, "data": {"prego_id": "BTO:0000123", "rank": "6", "taxon_id": "NCBITaxon:1286333", "taxon_label": "Escherichia coli TOP291", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 94, "data": {"prego_id": "BTO:0000123", "rank": "7", "taxon_id": "NCBITaxon:1286334", "taxon_label": "Escherichia coli TOP293-1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 95, "data": {"prego_id": "BTO:0000123", "rank": "8", "taxon_id": "NCBITaxon:1286335", "taxon_label": "Escherichia coli TOP293-2", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 96, "data": {"prego_id": "BTO:0000123", "rank": "9", "taxon_id": "NCBITaxon:1286336", "taxon_label": "Escherichia coli TOP293-3", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 97, "data": {"prego_id": "BTO:0000123", "rank": "10", "taxon_id": "NCBITaxon:1286337", "taxon_label": "Escherichia coli TOP293-4", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 98, "data": {"prego_id": "BTO:0000123", "rank": "11", "taxon_id": "NCBITaxon:1286338", "taxon_label": "Escherichia coli TOP498", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 99, "data": {"prego_id": "BTO:0000123", "rank": "12", "taxon_id": "NCBITaxon:1286339", "taxon_label": "Escherichia coli TOP550-1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 100, "data": {"prego_id": "BTO:0000123", "rank": "13", "taxon_id": "NCBITaxon:1286340", "taxon_label": "Escherichia coli TOP550-2", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 101, "data": {"prego_id": "BTO:0000123", "rank": "14", "taxon_id": "NCBITaxon:1286341", "taxon_label": "Escherichia coli TOP550-3", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 102, "data": {"prego_id": "BTO:0000123", "rank": "15", "taxon_id": "NCBITaxon:1286342", "taxon_label": "Escherichia coli TOP550-4", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 103, "data": {"prego_id": "BTO:0000123", "rank": "16", "taxon_id": "NCBITaxon:1286343", "taxon_label": "Escherichia coli TOP2386", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 104, "data": {"prego_id": "BTO:0000123", "rank": "17", "taxon_id": "NCBITaxon:1286344", "taxon_label": "Escherichia coli TOP2396-1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 105, "data": {"prego_id": "BTO:0000123", "rank": "18", "taxon_id": "NCBITaxon:1286345", "taxon_label": "Escherichia coli TOP2396-2", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 106, "data": {"prego_id": "BTO:0000123", "rank": "19", "taxon_id": "NCBITaxon:1286346", "taxon_label": "Escherichia coli TOP2396-3", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 107, "data": {"prego_id": "BTO:0000123", "rank": "20", "taxon_id": "NCBITaxon:1286347", "taxon_label": "Escherichia coli TOP2515", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 108, "data": {"prego_id": "BTO:0000123", "rank": "21", "taxon_id": "NCBITaxon:1286348", "taxon_label": "Escherichia coli TOP2522-1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 109, "data": {"prego_id": "BTO:0000123", "rank": "22", "taxon_id": "NCBITaxon:1286350", "taxon_label": "Escherichia coli TOP2652", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 110, "data": {"prego_id": "BTO:0000123", "rank": "23", "taxon_id": "NCBITaxon:1286351", "taxon_label": "Escherichia coli TOP2662-1", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 111, "data": {"prego_id": "BTO:0000123", "rank": "24", "taxon_id": "NCBITaxon:1286352", "taxon_label": "Escherichia coli TOP2662-2", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 112, "data": {"prego_id": "BTO:0000123", "rank": "25", "taxon_id": "NCBITaxon:1286353", "taxon_label": "Escherichia coli TOP2662-3", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 255 | supports | [{"row": 255, "data": {"prego_id": "BTO:0000123", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "32", "direct_assertion_count": "32", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "bladder&#124;bladders"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 92 | supports | [{"row": 92, "data": {"subject": "BTO:0000123", "predicate": "rdfs:subClassOf", "object": "BTO:0001491"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 125,1491 | supports | [{"row": 125, "data": {"term_id": "BTO:0000123", "ontology": "BTO", "label": "bladder", "definition": "A membranous sac in animals that serves as the receptacle of a liquid or contains gas.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 1491, "data": {"term_id": "BTO:0001491", "ontology": "BTO", "label": "viscus", "definition": "An internal organ of the body; especially: one (as the heart, liver, or intestine) located in the great cavity of the trunk proper.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| EL9 | reports/yaml_record_review/20261002T184714Z-bladder.md; Historical complete review | supports | Read as a source/issue lead. Current severity and verdict are reassessed independently; legacy prose does not close or create structured lineage. |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000123/graph; BTO_0000123-graph.json | context_only | Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000123", "target": "http://purl.obolibrary.org/obo/BTO_0001491", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000123?lang=en; BTO_0000123.json | context_only | Inspected current identifier, label, active status and full definition for the scope assessment: {"obo_id": "BTO:0000123", "label": "bladder", "is_obsolete": false} |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001491/graph; BTO_0001491-graph.json | context_only | Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0001491", "target": "http://purl.obolibrary.org/obo/BTO_0001489", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001491?lang=en; BTO_0001491.json | context_only | Inspected current identifier, label, active status and full definition for the scope assessment: {"obo_id": "BTO:0001491", "label": "viscus", "is_obsolete": false} |
| EX14 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PREGO methods section 2.3, PMID:35208748, DOI:10.3390/microorganisms10020293: genome-sequencing BioProject taxa are linked by mining associated abstracts; confidence three of five does not independently establish physical localization. |
| EX15 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:23658245%20AND%20SRC:MED&amp;format=json&amp;resultType=core; bladder-paper.json | context_only | Primary abstract PMID:23658245, DOI:10.1126/scitranslmed.3005497 describes 45 fecal/urine E. coli isolates from four women and mouse competition in gut and bladder. It supports mixed intestinal/urinary context, not a claim that every TOP isolate was directly sampled from bladder. Full-text XML returned HTTP 500 and browser retrieval a challenge; abstract only is used. |
| EX16 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1123383,1123384,1189612,1206108,1282,1286329,1286330,1286331,1286332,1286333,1286334,1286335,1286336,1286337,1286338,1286339,1286340,1286341,1286342,1286343,1286344,1286345,1286346,1286347,1286348,1286350,1286351,1286352,1286353,1322346,1408159,1408160,1497681,1552123,1585974,187452,240427,2702,375175,43771,478010,504474,508451,51663,53444,562,574375,582,588,758793,827&amp;retmode=xml; taxonomy.xml | context_only | All displayed taxon identifiers and labels resolve to current NCBI identities: [{"record_id": "1206108", "current_id": "1206108", "record_label": "Escherichia coli J96", "current_label": "Escherichia coli J96", "rank": "strain"}, {"record_id": "1286329", "current_id": "1286329", "record_label": "Escherichia coli TOP379", "current_label": "Escherichia coli TOP379", "rank": "strain"}, {"record_id": "1286330", "current_id": "1286330", "record_label": "Escherichia coli TOP382-1", "current_label": "Escherichia coli TOP382-1", "rank": "strain"}, {"record_id": "1286331", "current_id": "1286331", "record_label": "Escherichia coli TOP382-2", "current_label": "Escherichia coli TOP382-2", "rank": "strain"}, {"record_id": "1286332", "current_id": "1286332", "record_label": "Escherichia coli TOP382-3", "current_label": "Escherichia coli TOP382-3", "rank": "strain"}, {"record_id": "1286333", "current_id": "1286333", "record_label": "Escherichia coli TOP291", "current_label": "Escherichia coli TOP291", "rank": "strain"}, {"record_id": "1286334", "current_id": "1286334", "record_label": "Escherichia coli TOP293-1", "current_label": "Escherichia coli TOP293-1", "rank": "strain"}, {"record_id": "1286335", "current_id": "1286335", "record_label": "Escherichia coli TOP293-2", "current_label": "Escherichia coli TOP293-2", "rank": "strain"}, {"record_id": "1286336", "current_id": "1286336", "record_label": "Escherichia coli TOP293-3", "current_label": "Escherichia coli TOP293-3", "rank": "strain"}, {"record_id": "1286337", "current_id": "1286337", "record_label": "Escherichia coli TOP293-4", "current_label": "Escherichia coli TOP293-4", "rank": "strain"}, {"record_id": "1286338", "current_id": "1286338", "record_label": "Escherichia coli TOP498", "current_label": "Escherichia coli TOP498", "rank": "strain"}, {"record_id": "1286339", "current_id": "1286339", "record_label": "Escherichia coli TOP550-1", "current_label": "Escherichia coli TOP550-1", "rank": "strain"}, {"record_id": "1286340", "current_id": "1286340", "record_label": "Escherichia coli TOP550-2", "current_label": "Escherichia coli TOP550-2", "rank": "strain"}, {"record_id": "1286341", "current_id": "1286341", "record_label": "Escherichia coli TOP550-3", "current_label": "Escherichia coli TOP550-3", "rank": "strain"}, {"record_id": "1286342", "current_id": "1286342", "record_label": "Escherichia coli TOP550-4", "current_label": "Escherichia coli TOP550-4", "rank": "strain"}, {"record_id": "1286343", "current_id": "1286343", "record_label": "Escherichia coli TOP2386", "current_label": "Escherichia coli TOP2386", "rank": "strain"}, {"record_id": "1286344", "current_id": "1286344", "record_label": "Escherichia coli TOP2396-1", "current_label": "Escherichia coli TOP2396-1", "rank": "strain"}, {"record_id": "1286345", "current_id": "1286345", "record_label": "Escherichia coli TOP2396-2", "current_label": "Escherichia coli TOP2396-2", "rank": "strain"}, {"record_id": "1286346", "current_id": "1286346", "record_label": "Escherichia coli TOP2396-3", "current_label": "Escherichia coli TOP2396-3", "rank": "strain"}, {"record_id": "1286347", "current_id": "1286347", "record_label": "Escherichia coli TOP2515", "current_label": "Escherichia coli TOP2515", "rank": "strain"}, {"record_id": "1286348", "current_id": "1286348", "record_label": "Escherichia coli TOP2522-1", "current_label": "Escherichia coli TOP2522-1", "rank": "strain"}, {"record_id": "1286350", "current_id": "1286350", "record_label": "Escherichia coli TOP2652", "current_label": "Escherichia coli TOP2652", "rank": "strain"}, {"record_id": "1286351", "current_id": "1286351", "record_label": "Escherichia coli TOP2662-1", "current_label": "Escherichia coli TOP2662-1", "rank": "strain"}, {"record_id": "1286352", "current_id": "1286352", "record_label": "Escherichia coli TOP2662-2", "current_label": "Escherichia coli TOP2662-2", "rank": "strain"}, {"record_id": "1286353", "current_id": "1286353", "record_label": "Escherichia coli TOP2662-3", "current_label": "Escherichia coli TOP2662-3", "rank": "strain"}] |
| EX17 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=AOQB01000001&amp;rettype=gb&amp;retmode=xml; top379-genbank.xml | context_only | GenBank AOQB01000001 source qualifiers identify TOP379, taxon:1286329, Homo sapiens and urine from female. The reference links PMID:23658245 and DOI:10.1126/scitranslmed.3005497. Urine is not bladder tissue and is not proof of all displayed pair localizations. |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e BTO:0000123 -e bladder -e bladder -e habitatmech:PREGO.309b2fc00e curation history research reports data/raw build reviews | context_only | Ignored-inclusive search plus exact TSV parsing identified the stated source rows and no structured predecessor. |
| EPREGOSEARCH | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -path '*/prego/*' -name '*.tsv' | context_only | No PREGO-directory TSV payload found in this configured checkout. Committed HabitatMech projections are present; no global/upstream absence claim is made. |

## Limits And Additional Notes

- Every historical specimen and original PREGO pair has not been independently reidentified. Counts/scores/ranks are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 pairs without adapters; deterministic validity does not certify biological semantics.
- Full baseline QC is verified remote evidence at the captured revision, not a new local execution. Post-save archive and publication gates are subsequent.
- iModulonDB is not applicable: the target asserts no gene, regulator or expression module. No paid research was performed.
- Original PREGO pair evidence was not recovered. Source-specific publications support only their stated strain/site comparisons, not all retained associations or a demonstrated extraction cause.
- All captured local input hashes were rechecked against both the working tree and exact Git revision. No input bytes were silently refreshed.
- Ignored-inclusive archive traversal found no structured predecessor for this target; legacy Markdown is context, not independent approval or successor lineage.
- This observation precedes separately authorized curation/publication and does not claim a repair.
- The legacy review treats missing ITEM sign-off or an authored definition as a major gap. This review does not: the current record explicitly remains SEEDED, and its exact identifier/source path disambiguates it. This qualified verdict does not promote native status or certify every source assignment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T125452Z-bladder-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: bladder (BTO:0000123)'
started_at: '2026-10-15T12:40:42Z'
finished_at: '2026-10-15T12:54:52Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected the record and evidence; not independent
    human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The generic BTO bladder identity and viscus superclass are supported, without
  narrowing all animal liquid/gas sacs to urinary bladder. PREGO preserves 32 taxa
  and 25 displayed rows. A TOP379 sequence record identifies human urine, and the
  linked study examines both intestinal and urinary isolates; this supports bounded
  urinary context, not all 32 bladder-localization claims.
source:
  git_revision: 68ceabb7039a537f65be44ac6aaa913116a154f5
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
    sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 6d5cbfd0f5ad911fbb074ee8ec253625d1fa13d94117759b1f25a1cd2e6576bc
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: a92f9003cc5f57c397ab5118474318f216077a8e9f90564d21dfa8089477a2eb
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
  - path: data/habitats/host_associated/bladder.yaml
    sha256: 9035b57715f4f6980ee00734b52991cc3fd4ce36c034f3a967512db8e64dd802
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
  - path: reports/yaml_record_review/20261002T184714Z-bladder.md
    sha256: ef09b6407c4786583287bc81483809d71a0cbf7fcf330fdce9d8a2000a285d91
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
- target_id: BTO:0000123
  path: data/habitats/host_associated/bladder.yaml
  label: bladder
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
  description: Scientific review of one exact target at 68ceabb7039a537f65be44ac6aaa913116a154f5.
  selection: First seven records in the prepared next-twenty path-ordered cohort;
    this bundle assesses exactly one resolved identifier.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000123
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context is not additional reviewed coverage. Export readiness is
      not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bladder.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000123
  summary: "Completed 2026-10-15T12:40:45Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bladder.yaml"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml
    data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml
    data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml
    data/habitats/host_associated/blast_cell.yaml data/habitats/host_associated/blood.yaml
    data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml
    data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml
    data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml
    data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml
    data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml
    data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000123
  summary: "Completed 2026-10-15T12:41:35Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml\
    \ data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml\
    \ data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml\
    \ data/habitats/host_associated/blast_cell.yaml data/habitats/host_associated/blood.yaml\
    \ data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml\
    \ data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml\
    \ data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml\
    \ data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml\
    \ data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml\
    \ data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml\n\
    Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000123
  summary: 'Completed 2026-10-15T12:41:43Z. No issues found

    808 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000123
  summary: "Completed 2026-10-15T12:41:44Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000123
  summary: "Completed 2026-10-15T12:41:58Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000123
  summary: "Completed 2026-10-15T12:42:02Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000123
  summary: "Completed 2026-10-15T12:42:18Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000123
  summary: "Completed 2026-10-15T12:42:59Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: CCI
  name: Exact-revision baseline full QC
  status: passed
  required: true
  command: gh run view 38733485444 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0000123
  summary: 'Verified 2026-10-15T12:40:46Z: https://github.com/CultureBotAI/HabitatMech/actions/runs/38733485444'
  scope_note: Remote full-QC execution at the exact unchanged scientific baseline;
    new review outputs are not yet covered.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bladder.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: Read the full target including source paths, taxa, hierarchy and history.
  snapshot_sha256: 9035b57715f4f6980ee00734b52991cc3fd4ce36c034f3a967512db8e64dd802
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, broader-parent and ownership rules
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: Context, containment and whole-host identity differ from strictly broader
    habitat ancestry.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and CharacteristicTaxon
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: Mapping endpoints, assertion units and association versus characteristic-presence
    semantics.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native source resolution
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: 'Exact routes: [{"source": "PREGO", "mint": "habitatmech:PREGO.309b2fc00e",
    "automatic": {"identifier": "BTO:0000123", "grounding_status": "EXACT", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "prego_self_grounded", "category": null, "reviewed": false, "decision": null},
    "final": {"identifier": "BTO:0000123", "grounding_status": "EXACT", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: Projection preserves distinct-taxon totals and score/channel ranking but
    not original pair citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: '[{"row": 88, "data": {"prego_id": "BTO:0000123", "rank": "1", "taxon_id":
    "NCBITaxon:1206108", "taxon_label": "Escherichia coli J96", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 89, "data": {"prego_id": "BTO:0000123", "rank": "2", "taxon_id":
    "NCBITaxon:1286329", "taxon_label": "Escherichia coli TOP379", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 90, "data": {"prego_id": "BTO:0000123", "rank": "3", "taxon_id":
    "NCBITaxon:1286330", "taxon_label": "Escherichia coli TOP382-1", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 91, "data": {"prego_id": "BTO:0000123", "rank": "4", "taxon_id":
    "NCBITaxon:1286331", "taxon_label": "Escherichia coli TOP382-2", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 92, "data": {"prego_id": "BTO:0000123", "rank": "5", "taxon_id":
    "NCBITaxon:1286332", "taxon_label": "Escherichia coli TOP382-3", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 93, "data": {"prego_id": "BTO:0000123", "rank": "6", "taxon_id":
    "NCBITaxon:1286333", "taxon_label": "Escherichia coli TOP291", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 94, "data": {"prego_id": "BTO:0000123", "rank": "7", "taxon_id":
    "NCBITaxon:1286334", "taxon_label": "Escherichia coli TOP293-1", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 95, "data": {"prego_id": "BTO:0000123", "rank": "8", "taxon_id":
    "NCBITaxon:1286335", "taxon_label": "Escherichia coli TOP293-2", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 96, "data": {"prego_id": "BTO:0000123", "rank": "9", "taxon_id":
    "NCBITaxon:1286336", "taxon_label": "Escherichia coli TOP293-3", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 97, "data": {"prego_id": "BTO:0000123", "rank": "10", "taxon_id":
    "NCBITaxon:1286337", "taxon_label": "Escherichia coli TOP293-4", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 98, "data": {"prego_id": "BTO:0000123", "rank": "11", "taxon_id":
    "NCBITaxon:1286338", "taxon_label": "Escherichia coli TOP498", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 99, "data": {"prego_id": "BTO:0000123", "rank": "12", "taxon_id":
    "NCBITaxon:1286339", "taxon_label": "Escherichia coli TOP550-1", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 100, "data": {"prego_id": "BTO:0000123", "rank": "13", "taxon_id":
    "NCBITaxon:1286340", "taxon_label": "Escherichia coli TOP550-2", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 101, "data": {"prego_id": "BTO:0000123", "rank": "14", "taxon_id":
    "NCBITaxon:1286341", "taxon_label": "Escherichia coli TOP550-3", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 102, "data": {"prego_id": "BTO:0000123", "rank": "15", "taxon_id":
    "NCBITaxon:1286342", "taxon_label": "Escherichia coli TOP550-4", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 103, "data": {"prego_id": "BTO:0000123", "rank": "16", "taxon_id":
    "NCBITaxon:1286343", "taxon_label": "Escherichia coli TOP2386", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 104, "data": {"prego_id": "BTO:0000123", "rank": "17", "taxon_id":
    "NCBITaxon:1286344", "taxon_label": "Escherichia coli TOP2396-1", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 105, "data": {"prego_id": "BTO:0000123", "rank": "18", "taxon_id":
    "NCBITaxon:1286345", "taxon_label": "Escherichia coli TOP2396-2", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 106, "data": {"prego_id": "BTO:0000123", "rank": "19", "taxon_id":
    "NCBITaxon:1286346", "taxon_label": "Escherichia coli TOP2396-3", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 107, "data": {"prego_id": "BTO:0000123", "rank": "20", "taxon_id":
    "NCBITaxon:1286347", "taxon_label": "Escherichia coli TOP2515", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 108, "data": {"prego_id": "BTO:0000123", "rank": "21", "taxon_id":
    "NCBITaxon:1286348", "taxon_label": "Escherichia coli TOP2522-1", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 109, "data": {"prego_id": "BTO:0000123", "rank": "22", "taxon_id":
    "NCBITaxon:1286350", "taxon_label": "Escherichia coli TOP2652", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 110, "data": {"prego_id": "BTO:0000123", "rank": "23", "taxon_id":
    "NCBITaxon:1286351", "taxon_label": "Escherichia coli TOP2662-1", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 111, "data": {"prego_id": "BTO:0000123", "rank": "24", "taxon_id":
    "NCBITaxon:1286352", "taxon_label": "Escherichia coli TOP2662-2", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}, {"row": 112, "data": {"prego_id": "BTO:0000123", "rank": "25", "taxon_id":
    "NCBITaxon:1286353", "taxon_label": "Escherichia coli TOP2662-3", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 255
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: '[{"row": 255, "data": {"prego_id": "BTO:0000123", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "32", "direct_assertion_count":
    "32", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "bladder|bladders"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 92
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: '[{"row": 92, "data": {"subject": "BTO:0000123", "predicate": "rdfs:subClassOf",
    "object": "BTO:0001491"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 125,1491
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: '[{"row": 125, "data": {"term_id": "BTO:0000123", "ontology": "BTO", "label":
    "bladder", "definition": "A membranous sac in animals that serves as the receptacle
    of a liquid or contains gas.", "synonyms": "", "deprecated": "", "directly_referenced":
    "TRUE", "label_only": "FALSE"}}, {"row": 1491, "data": {"term_id": "BTO:0001491",
    "ontology": "BTO", "label": "viscus", "definition": "An internal organ of the
    body; especially: one (as the heart, liver, or intestine) located in the great
    cavity of the trunk proper.", "synonyms": "", "deprecated": "", "directly_referenced":
    "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EL9
  kind: record_content
  reference: reports/yaml_record_review/20261002T184714Z-bladder.md
  locator: Historical complete review
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: Read as a source/issue lead. Current severity and verdict are reassessed
    independently; legacy prose does not close or create structured lineage.
  snapshot_sha256: ef09b6407c4786583287bc81483809d71a0cbf7fcf330fdce9d8a2000a285d91
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000123/graph
  locator: BTO_0000123-graph.json
  accessed_at: '2026-10-15T12:46:39Z'
  support: context_only
  summary: 'Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000123",
    "target": "http://purl.obolibrary.org/obo/BTO_0001491", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: e9e42c562936bef89e676054c4e185b752bd9a2e597a45eb62c389c2fc59f561
- evidence_id: EX11
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000123?lang=en
  locator: BTO_0000123.json
  accessed_at: '2026-10-15T12:46:38Z'
  support: context_only
  summary: 'Inspected current identifier, label, active status and full definition
    for the scope assessment: {"obo_id": "BTO:0000123", "label": "bladder", "is_obsolete":
    false}'
  snapshot_sha256: 15787601180666ae39aeb60fb552cfc0877e467d88558e00074720771ac5a5fe
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001491/graph
  locator: BTO_0001491-graph.json
  accessed_at: '2026-10-15T12:46:47Z'
  support: context_only
  summary: 'Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0001491",
    "target": "http://purl.obolibrary.org/obo/BTO_0001489", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: ec79fd8d236587cc5cb962f298952edb2ae55a2c3360fe4cf6ca4ad7a3615498
- evidence_id: EX13
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001491?lang=en
  locator: BTO_0001491.json
  accessed_at: '2026-10-15T12:46:46Z'
  support: context_only
  summary: 'Inspected current identifier, label, active status and full definition
    for the scope assessment: {"obo_id": "BTO:0001491", "label": "viscus", "is_obsolete":
    false}'
  snapshot_sha256: b017023b576d2734e9fe64367b42ec83af92c4bfbde5ac1577301ac67ccc02cf
- evidence_id: EX14
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-15T12:48:05Z'
  support: context_only
  summary: 'PREGO methods section 2.3, PMID:35208748, DOI:10.3390/microorganisms10020293:
    genome-sequencing BioProject taxa are linked by mining associated abstracts; confidence
    three of five does not independently establish physical localization.'
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX15
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:23658245%20AND%20SRC:MED&format=json&resultType=core
  locator: bladder-paper.json
  accessed_at: '2026-10-15T12:49:28Z'
  support: context_only
  summary: Primary abstract PMID:23658245, DOI:10.1126/scitranslmed.3005497 describes
    45 fecal/urine E. coli isolates from four women and mouse competition in gut and
    bladder. It supports mixed intestinal/urinary context, not a claim that every
    TOP isolate was directly sampled from bladder. Full-text XML returned HTTP 500
    and browser retrieval a challenge; abstract only is used.
  snapshot_sha256: dd754340e756e2bbc94bc0a7e7e779b2a95fe69ce0d2d768ef53690a24783b80
- evidence_id: EX16
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1123383,1123384,1189612,1206108,1282,1286329,1286330,1286331,1286332,1286333,1286334,1286335,1286336,1286337,1286338,1286339,1286340,1286341,1286342,1286343,1286344,1286345,1286346,1286347,1286348,1286350,1286351,1286352,1286353,1322346,1408159,1408160,1497681,1552123,1585974,187452,240427,2702,375175,43771,478010,504474,508451,51663,53444,562,574375,582,588,758793,827&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T12:47:05Z'
  support: context_only
  summary: 'All displayed taxon identifiers and labels resolve to current NCBI identities:
    [{"record_id": "1206108", "current_id": "1206108", "record_label": "Escherichia
    coli J96", "current_label": "Escherichia coli J96", "rank": "strain"}, {"record_id":
    "1286329", "current_id": "1286329", "record_label": "Escherichia coli TOP379",
    "current_label": "Escherichia coli TOP379", "rank": "strain"}, {"record_id": "1286330",
    "current_id": "1286330", "record_label": "Escherichia coli TOP382-1", "current_label":
    "Escherichia coli TOP382-1", "rank": "strain"}, {"record_id": "1286331", "current_id":
    "1286331", "record_label": "Escherichia coli TOP382-2", "current_label": "Escherichia
    coli TOP382-2", "rank": "strain"}, {"record_id": "1286332", "current_id": "1286332",
    "record_label": "Escherichia coli TOP382-3", "current_label": "Escherichia coli
    TOP382-3", "rank": "strain"}, {"record_id": "1286333", "current_id": "1286333",
    "record_label": "Escherichia coli TOP291", "current_label": "Escherichia coli
    TOP291", "rank": "strain"}, {"record_id": "1286334", "current_id": "1286334",
    "record_label": "Escherichia coli TOP293-1", "current_label": "Escherichia coli
    TOP293-1", "rank": "strain"}, {"record_id": "1286335", "current_id": "1286335",
    "record_label": "Escherichia coli TOP293-2", "current_label": "Escherichia coli
    TOP293-2", "rank": "strain"}, {"record_id": "1286336", "current_id": "1286336",
    "record_label": "Escherichia coli TOP293-3", "current_label": "Escherichia coli
    TOP293-3", "rank": "strain"}, {"record_id": "1286337", "current_id": "1286337",
    "record_label": "Escherichia coli TOP293-4", "current_label": "Escherichia coli
    TOP293-4", "rank": "strain"}, {"record_id": "1286338", "current_id": "1286338",
    "record_label": "Escherichia coli TOP498", "current_label": "Escherichia coli
    TOP498", "rank": "strain"}, {"record_id": "1286339", "current_id": "1286339",
    "record_label": "Escherichia coli TOP550-1", "current_label": "Escherichia coli
    TOP550-1", "rank": "strain"}, {"record_id": "1286340", "current_id": "1286340",
    "record_label": "Escherichia coli TOP550-2", "current_label": "Escherichia coli
    TOP550-2", "rank": "strain"}, {"record_id": "1286341", "current_id": "1286341",
    "record_label": "Escherichia coli TOP550-3", "current_label": "Escherichia coli
    TOP550-3", "rank": "strain"}, {"record_id": "1286342", "current_id": "1286342",
    "record_label": "Escherichia coli TOP550-4", "current_label": "Escherichia coli
    TOP550-4", "rank": "strain"}, {"record_id": "1286343", "current_id": "1286343",
    "record_label": "Escherichia coli TOP2386", "current_label": "Escherichia coli
    TOP2386", "rank": "strain"}, {"record_id": "1286344", "current_id": "1286344",
    "record_label": "Escherichia coli TOP2396-1", "current_label": "Escherichia coli
    TOP2396-1", "rank": "strain"}, {"record_id": "1286345", "current_id": "1286345",
    "record_label": "Escherichia coli TOP2396-2", "current_label": "Escherichia coli
    TOP2396-2", "rank": "strain"}, {"record_id": "1286346", "current_id": "1286346",
    "record_label": "Escherichia coli TOP2396-3", "current_label": "Escherichia coli
    TOP2396-3", "rank": "strain"}, {"record_id": "1286347", "current_id": "1286347",
    "record_label": "Escherichia coli TOP2515", "current_label": "Escherichia coli
    TOP2515", "rank": "strain"}, {"record_id": "1286348", "current_id": "1286348",
    "record_label": "Escherichia coli TOP2522-1", "current_label": "Escherichia coli
    TOP2522-1", "rank": "strain"}, {"record_id": "1286350", "current_id": "1286350",
    "record_label": "Escherichia coli TOP2652", "current_label": "Escherichia coli
    TOP2652", "rank": "strain"}, {"record_id": "1286351", "current_id": "1286351",
    "record_label": "Escherichia coli TOP2662-1", "current_label": "Escherichia coli
    TOP2662-1", "rank": "strain"}, {"record_id": "1286352", "current_id": "1286352",
    "record_label": "Escherichia coli TOP2662-2", "current_label": "Escherichia coli
    TOP2662-2", "rank": "strain"}, {"record_id": "1286353", "current_id": "1286353",
    "record_label": "Escherichia coli TOP2662-3", "current_label": "Escherichia coli
    TOP2662-3", "rank": "strain"}]'
  snapshot_sha256: f8419452b360c25eb644e679b18e320a164cb1dadcd7177218469368fe9cd7dd
- evidence_id: EX17
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AOQB01000001&rettype=gb&retmode=xml
  locator: top379-genbank.xml
  accessed_at: '2026-10-15T12:48:15Z'
  support: context_only
  summary: GenBank AOQB01000001 source qualifiers identify TOP379, taxon:1286329,
    Homo sapiens and urine from female. The reference links PMID:23658245 and DOI:10.1126/scitranslmed.3005497.
    Urine is not bladder tissue and is not proof of all displayed pair localizations.
  snapshot_sha256: 3cc3472419449d125737a3781e55fce6d12c647ca7064213d23f090fc1535620
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0000123 -e bladder -e bladder -e habitatmech:PREGO.309b2fc00e
    curation history research reports data/raw build reviews
  accessed_at: '2026-10-15T12:45:44Z'
  support: context_only
  summary: Ignored-inclusive search plus exact TSV parsing identified the stated source
    rows and no structured predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews,
    including ignored and hidden files; pathlib traversal of all structured review.yaml
    files.
- evidence_id: EPREGOSEARCH
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -path '*/prego/*' -name '*.tsv'
  accessed_at: '2026-10-15T12:45:47Z'
  support: context_only
  summary: No PREGO-directory TSV payload found in this configured checkout. Committed
    HabitatMech projections are present; no global/upstream absence claim is made.
  search_scope: All matching files under the configured checkout, including ignored/hidden
    paths.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validation and reproduction
  outcome: supported
  summary: Schema, strict, history, provenance, 3,208-record reproduction, causal
    overlays, term requests and configured labels passed. These establish deterministic
    fidelity, not scientific support.
  target_ids:
  - BTO:0000123
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, hierarchy and nomenclature
  outcome: supported
  summary: The generic BTO bladder identity and viscus superclass are supported, without
    narrowing all animal liquid/gas sacs to urinary bladder. PREGO preserves 32 taxa
    and 25 displayed rows. A TOP379 sequence record identifies human urine, and the
    linked study examines both intestinal and urinary isolates; this supports bounded
    urinary context, not all 32 bladder-localization claims.
  target_ids:
  - BTO:0000123
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
- assessment_id: A3
  area: quantity
  topic: Source count, unit and ranking
  outcome: supported
  summary: 'Exact source projections retain [{"source": "PREGO", "source_id": "BTO:0000123",
    "source_label": "bladder", "assertion_count": 32, "assertion_unit": "TAXON", "score":
    3.0, "evidence_channels": "annotated_genomes_isolates"}]. All 25 displayed taxa
    were resolved against current NCBI IDs/labels. Ranks and candidate pools are source-specific;
    unlike units are never summed.'
  target_ids:
  - BTO:0000123
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
- assessment_id: A4
  area: completeness
  topic: Native status and optional fields
  outcome: supported
  summary: Executed source decisions reproduce EXACT/SEEDED. No causal mechanism or
    is_characteristic assertion is present. Missing optional fields or SEEDED status
    are not automatic scientific defects.
  target_ids:
  - BTO:0000123
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings: []
actions: []
limitations:
- Every historical specimen and original PREGO pair has not been independently reidentified.
  Counts/scores/ranks are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 pairs without adapters; deterministic validity
  does not certify biological semantics.
- Full baseline QC is verified remote evidence at the captured revision, not a new
  local execution. Post-save archive and publication gates are subsequent.
- 'iModulonDB is not applicable: the target asserts no gene, regulator or expression
  module. No paid research was performed.'
- Original PREGO pair evidence was not recovered. Source-specific publications support
  only their stated strain/site comparisons, not all retained associations or a demonstrated
  extraction cause.
notes:
- All captured local input hashes were rechecked against both the working tree and
  exact Git revision. No input bytes were silently refreshed.
- Ignored-inclusive archive traversal found no structured predecessor for this target;
  legacy Markdown is context, not independent approval or successor lineage.
- This observation precedes separately authorized curation/publication and does not
  claim a repair.
- 'The legacy review treats missing ITEM sign-off or an authored definition as a major
  gap. This review does not: the current record explicitly remains SEEDED, and its
  exact identifier/source path disambiguates it. This qualified verdict does not promote
  native status or certify every source assignment.'
tags:
- individual-scientific-review
- host-associated
```
