# Record review: cecum mucosa (BTO:0000213)

- Review: 20261015T235743Z-cecum_mucosa-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T23:39:44Z
- Finished UTC: 2026-10-15T23:57:43Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

BTO cecum mucosa has a supported intestinal-mucosa superclass; current BTO separately relates it part_of to cecum. The target preserves that distinction and the 53-taxon pool with 25 ranked associations. NCBITaxon:541000 is an alias of current Oscillospiraceae 216572, not a dangling taxon. Absent optional definition and label do not establish a scientific defect.

## Scope And Provenance

Full field-by-field scientific assessment of this exact generated target at 0eb609a7ddb34925067116af806e26c165e10678.

Selection: Stale cecum individual observation plus the next 23 identifiers lacking completed individual-kind reviews in the ignored-inclusive 3209-record census. This bundle assesses one resolved record; previous batch reviews remain valid history.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 0eb609a7ddb34925067116af806e26c165e10678.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000213 | data/habitats/host_associated/cecum_mucosa.yaml | generated | cecum mucosa |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000213 | Finished 2026-10-15T23:44:42Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cecum_mucosa.yaml |
| validate-strict | passed | True | BTO:0000213 | Finished 2026-10-15T23:45:51Z. uv run python scripts/validate_strict.py data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000213 | Finished 2026-10-15T23:46:04Z. No issues found<br>829 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000213 | Finished 2026-10-15T23:46:05Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000213 | Finished 2026-10-15T23:46:28Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000213 | Finished 2026-10-15T23:46:34Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000213 | Finished 2026-10-15T23:46:59Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000213 | Finished 2026-10-15T23:48:03Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline native QC | passed | True | BTO:0000213 | Verified 2026-10-15T23:55:08Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38822113212 |
| Standalone evidence-reference validator applicability | not_applicable | False | BTO:0000213 | No standalone citation/reference validator is documented for these evidence-free generated records. Target EvidenceItems and causal edges are absent. Stable source and ontology/taxon references were checked manually and with documented native gates; current-decision primary citations were separately verified where present. |

## Scientific And Domain Assessments

### Identity, definition, category, aliases and hierarchy

identity: supported. Targets: BTO:0000213.

BTO cecum mucosa has a supported intestinal-mucosa superclass; current BTO separately relates it part_of to cecum. The target preserves that distinction and the 53-taxon pool with 25 ranked associations. NCBITaxon:541000 is an alias of current Oscillospiraceae 216572, not a dangling taxon. Absent optional definition and label do not establish a scientific defect.

### Source assertions, pools, ranks and supplementary context

quantity: supported. Targets: BTO:0000213.

All emitted counts/units, labels, ranks, scores and candidate pools match exact frozen rows. [{"source": "PREGO", "count": 53, "unit": "TAXON"}]. Zero tree counts are omitted; later biosamples and study memberships are not added. Current taxonomy resolves displayed identifiers including explicit aliases.

### Biological support and bounded source uncertainty

evidence: supported. Targets: BTO:0000213.

BTO cecum mucosa has a supported intestinal-mucosa superclass; current BTO separately relates it part_of to cecum. The target preserves that distinction and the 53-taxon pool with 25 ranked associations. NCBITaxon:541000 is an alias of current Oscillospiraceae 216572, not a dangling taxon. Absent optional definition and label do not establish a scientific defect.

### Native status, optional parameters and causal mechanisms

completeness: supported. Targets: BTO:0000213.

Executed native resolution reproduces EXACT/SEEDED. No environmental parameters, causal graphs, discussions, datasets or is_characteristic=true claims are present. Missing optional fields and SEEDED status alone are not defects; parent mechanisms are not inherited.

### Native validation and reproduction

schema: supported. Targets: BTO:0000213.

Target schema/strict checks, 829 histories, source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured label checks passed. Exact-base remote full QC passed. Deterministic validity is separate from scientific support; reference-check applicability is stated explicitly.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/cecum_mucosa.yaml; Entire target YAML | supports | All fields, attestations, taxa and generated history read. |
| ERULE | docs/CURATION.md; Identity, strict broader hierarchy and evidence rules | supports | Organism, disease, material and habitat identities remain distinct. Parents must be strictly broader, not merely containing sites. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation and TaxonAssociation | supports | Mapping predicate endpoint is source-to-record; source association is weaker than characteristic presence. Optional fields and native review status have distinct contracts. |
| ESEED | src/habitatmech/seed.py; Executed native source routes and complete document reproduction | supports | [{"mint": "habitatmech:PREGO.1b01d8cfa1", "automatic": {"identifier": "BTO:0000213", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000213", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source counts, channels and taxon ranking | supports | Exact frozen rows reproduce counts/units and ranked taxon scores. The committed projection does not retain original PREGO pair citation links. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313 | supports | [{"row": 289, "data": {"prego_id": "BTO:0000213", "rank": "1", "taxon_id": "NCBITaxon:119852", "taxon_label": "Oscillospira", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 290, "data": {"prego_id": "BTO:0000213", "rank": "2", "taxon_id": "NCBITaxon:1263", "taxon_label": "Ruminococcus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 291, "data": {"prego_id": "BTO:0000213", "rank": "3", "taxon_id": "NCBITaxon:128827", "taxon_label": "Erysipelotrichaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 292, "data": {"prego_id": "BTO:0000213", "rank": "4", "taxon_id": "NCBITaxon:135569", "taxon_label": "Helicobacter apodemus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 293, "data": {"prego_id": "BTO:0000213", "rank": "5", "taxon_id": "NCBITaxon:1578", "taxon_label": "Lactobacillus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 294, "data": {"prego_id": "BTO:0000213", "rank": "6", "taxon_id": "NCBITaxon:1598", "taxon_label": "Limosilactobacillus reuteri", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 295, "data": {"prego_id": "BTO:0000213", "rank": "7", "taxon_id": "NCBITaxon:171549", "taxon_label": "Bacteroidales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 296, "data": {"prego_id": "BTO:0000213", "rank": "8", "taxon_id": "NCBITaxon:171550", "taxon_label": "Rikenellaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 297, "data": {"prego_id": "BTO:0000213", "rank": "9", "taxon_id": "NCBITaxon:186802", "taxon_label": "Eubacteriales", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 298, "data": {"prego_id": "BTO:0000213", "rank": "10", "taxon_id": "NCBITaxon:186803", "taxon_label": "Lachnospiraceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 299, "data": {"prego_id": "BTO:0000213", "rank": "11", "taxon_id": "NCBITaxon:189330", "taxon_label": "Dorea", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 300, "data": {"prego_id": "BTO:0000213", "rank": "12", "taxon_id": "NCBITaxon:194924", "taxon_label": "Desulfovibrionaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 301, "data": {"prego_id": "BTO:0000213", "rank": "13", "taxon_id": "NCBITaxon:209", "taxon_label": "Helicobacter", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 302, "data": {"prego_id": "BTO:0000213", "rank": "14", "taxon_id": "NCBITaxon:2353", "taxon_label": "Flexispira", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 303, "data": {"prego_id": "BTO:0000213", "rank": "15", "taxon_id": "NCBITaxon:248039", "taxon_label": "Mucispirillum schaedleri", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 304, "data": {"prego_id": "BTO:0000213", "rank": "16", "taxon_id": "NCBITaxon:283168", "taxon_label": "Odoribacter", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 305, "data": {"prego_id": "BTO:0000213", "rank": "17", "taxon_id": "NCBITaxon:31979", "taxon_label": "Clostridiaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 306, "data": {"prego_id": "BTO:0000213", "rank": "18", "taxon_id": "NCBITaxon:33038", "taxon_label": "Mediterraneibacter gnavus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 307, "data": {"prego_id": "BTO:0000213", "rank": "19", "taxon_id": "NCBITaxon:33042", "taxon_label": "Coprococcus", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 308, "data": {"prego_id": "BTO:0000213", "rank": "20", "taxon_id": "NCBITaxon:375288", "taxon_label": "Parabacteroides", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 309, "data": {"prego_id": "BTO:0000213", "rank": "21", "taxon_id": "NCBITaxon:40544", "taxon_label": "Sutterella", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 310, "data": {"prego_id": "BTO:0000213", "rank": "22", "taxon_id": "NCBITaxon:447020", "taxon_label": "Adlercreutzia", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 311, "data": {"prego_id": "BTO:0000213", "rank": "23", "taxon_id": "NCBITaxon:51514", "taxon_label": "Dehalobacterium", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 312, "data": {"prego_id": "BTO:0000213", "rank": "24", "taxon_id": "NCBITaxon:541000", "taxon_label": "", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 313, "data": {"prego_id": "BTO:0000213", "rank": "25", "taxon_id": "NCBITaxon:543", "taxon_label": "Enterobacteriaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 219 | supports | [{"row": 219, "data": {"prego_id": "BTO:0000213", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "53", "direct_assertion_count": "53", "max_prego_score": "4", "channels": "environmental_samples", "prego_synonyms": "cecum mucosa&#124;cecum mucosal&#124;cecum mucosas"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 151,409 | supports | [{"row": 151, "data": {"subject": "BTO:0000213", "predicate": "rdfs:subClassOf", "object": "BTO:0000642"}}, {"row": 409, "data": {"subject": "BTO:0000642", "predicate": "rdfs:subClassOf", "object": "BTO:0000886"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 215,643 | supports | [{"row": 215, "data": {"term_id": "BTO:0000213", "ontology": "BTO", "label": "cecum mucosa", "definition": "", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 643, "data": {"term_id": "BTO:0000642", "ontology": "BTO", "label": "intestinal mucosa", "definition": "The surface lining of the intestines where the cells absorb nutrients.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EP9 | data/habitats/host_associated/intestinal_mucosa.yaml; Full immediate-parent record; context only | supports | {"identifier": "BTO:0000642", "label": "intestinal mucosa", "definition": "The surface lining of the intestines where the cells absorb nutrients.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "intestinal mucosal", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinal mucosas", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats": ["BTO:0000886"], "source_attestations": [{"source": "PREGO", "source_id": "BTO:0000642", "source_label": "intestinal mucosa", "assertion_count": 1, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:272621", "source": "PREGO", "taxon_label": "Lactobacillus acidophilus NCFM", "score": 3.0, "rank": 1, "candidate_pool": 1}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: EXACT."}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000213/graph; BTO_0000213-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000213", "target": "http://purl.obolibrary.org/obo/BTO_0000642", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000213", "target": "http://purl.obolibrary.org/obo/BTO_0000166", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000213; BTO_0000213.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0000213", "label": "cecum mucosa", "is_obsolete": false, "description": []} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000642/graph; BTO_0000642-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000642", "target": "http://purl.obolibrary.org/obo/BTO_0000886", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000642", "target": "http://purl.obolibrary.org/obo/BTO_0000648", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000642; BTO_0000642.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0000642", "label": "intestinal mucosa", "is_obsolete": false, "description": ["The surface lining of the intestines where the cells absorb nutrients."]} |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000886/graph; BTO_0000886-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000886", "target": "http://purl.obolibrary.org/obo/BTO_0000634", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000886; BTO_0000886.json | context_only | Current term identity, active status and definition: {"obo_id": "BTO:0000886", "label": "mucosa", "is_obsolete": false, "description": ["A membrane lining all body passages that communicate with the air, such as the respiratory and alimentary tracts, and having cells and associated glands that secrete mucus."]} |
| EX7 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PMID:35208748, DOI:10.3390/microorganisms10020293. PREGO methods distinguish literature, genomic/isolate and environmental channels. BioProject-associated abstract mining can yield score-three associations. Source score/channel alone is not direct localization, prevalence or characteristic presence; this does not establish the extraction route of a particular pair. |
| EX8 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=100176,100883,102106,102234,1032526,1091138,109326,1095955,1096995,1096996,1096997,1117,1121103,1126011,113286,117563,118747,119852,1213463,122587,1233262,1236904,1238993,1249,1253,1263,1263756,1263757,1263758,1263760,1263761,1263762,1263763,1263835,1265,1266,1268,1269,1279,1280,1280940,1282,128827,1292046,1296,1300,1313,1315977,1329902,135569,1408179,1472682,1578,1598,1639,1643450,171549,171550,1747766,1773,186802,186803,189330,194924,209,2353,243161,248039,272563,280871,283168,314724,31979,33038,33042,375288,40544,447020,51514,539221,541000,543,553198,647227,83262&amp;retmode=xml; taxonomy.xml | context_only | Current NCBI identities and source-label comparisons: [{"id": "NCBITaxon:119852", "source": "PREGO", "label": "Oscillospira", "current_id": "119852", "current_name": "Oscillospira", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1263", "source": "PREGO", "label": "Ruminococcus", "current_id": "1263", "current_name": "Ruminococcus", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:128827", "source": "PREGO", "label": "Erysipelotrichaceae", "current_id": "128827", "current_name": "Erysipelotrichaceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:135569", "source": "PREGO", "label": "Helicobacter apodemus", "current_id": "135569", "current_name": "Helicobacter apodemus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1578", "source": "PREGO", "label": "Lactobacillus", "current_id": "1578", "current_name": "Lactobacillus", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1598", "source": "PREGO", "label": "Limosilactobacillus reuteri", "current_id": "1598", "current_name": "Limosilactobacillus reuteri", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:171549", "source": "PREGO", "label": "Bacteroidales", "current_id": "171549", "current_name": "Bacteroidales", "rank": "order", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:171550", "source": "PREGO", "label": "Rikenellaceae", "current_id": "171550", "current_name": "Rikenellaceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:186802", "source": "PREGO", "label": "Eubacteriales", "current_id": "186802", "current_name": "Eubacteriales", "rank": "order", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:186803", "source": "PREGO", "label": "Lachnospiraceae", "current_id": "186803", "current_name": "Lachnospiraceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:189330", "source": "PREGO", "label": "Dorea", "current_id": "189330", "current_name": "Dorea", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:194924", "source": "PREGO", "label": "Desulfovibrionaceae", "current_id": "194924", "current_name": "Desulfovibrionaceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:209", "source": "PREGO", "label": "Helicobacter", "current_id": "209", "current_name": "Helicobacter", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2353", "source": "PREGO", "label": "Flexispira", "current_id": "2353", "current_name": "Flexispira", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:248039", "source": "PREGO", "label": "Mucispirillum schaedleri", "current_id": "248039", "current_name": "Mucispirillum schaedleri", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:283168", "source": "PREGO", "label": "Odoribacter", "current_id": "283168", "current_name": "Odoribacter", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:31979", "source": "PREGO", "label": "Clostridiaceae", "current_id": "31979", "current_name": "Clostridiaceae", "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:33038", "source": "PREGO", "label": "Mediterraneibacter gnavus", "current_id": "33038", "current_name": "Mediterraneibacter gnavus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:33042", "source": "PREGO", "label": "Coprococcus", "current_id": "33042", "current_name": "Coprococcus", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:375288", "source": "PREGO", "label": "Parabacteroides", "current_id": "375288", "current_name": "Parabacteroides", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:40544", "source": "PREGO", "label": "Sutterella", "current_id": "40544", "current_name": "Sutterella", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:447020", "source": "PREGO", "label": "Adlercreutzia", "current_id": "447020", "current_name": "Adlercreutzia", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:51514", "source": "PREGO", "label": "Dehalobacterium", "current_id": "51514", "current_name": "Dehalobacterium", "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:541000", "source": "PREGO", "label": null, "current_id": "216572", "current_name": "Oscillospiraceae", "rank": "family", "direct_match": false, "recognized_alias": false}, {"id": "NCBITaxon:543", "source": "PREGO", "label": "Enterobacteriaceae", "current_id": "543", "current_name": "Enterobacteriaceae", "rank": "family", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local maintained inputs and review archive; rg --no-ignore --hidden -l -F -e BTO:0000213 -e 'cecum mucosa' -e cecum_mucosa -e habitatmech:PREGO.1b01d8cfa1 curation history research reports data/raw build reviews | context_only | Identifier/label/slug search and full structured-YAML traversal; exact TSV rows were parsed separately. Broad search matches are leads, not all independently reviewed. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -ipath '*prego*' | context_only | No PREGO-named files were found in the configured checkout. Original pair exports remain unavailable there, not proven absent globally. |

## Limits And Additional Notes

- Source counts, ranks and scores do not establish prevalence, viability or characteristic presence. Original specimen-level evidence for every source member has not been reconstructed.
- Configured label validation skipped 2063 no-adapter pairs; displayed TaxIds were separately resolved against current NCBI including aliases.
- Exact-base full QC was verified remotely, not newly executed locally. New saved bundles require a separate archive check.
- iModulonDB is not applicable: target assertions contain no gene, regulator or expression-module claim. No paid research or native status promotion was performed.
- Original PREGO pair-level exports were not found in the configured checkout. Positive primary witnesses do not reconstruct every pair or its extraction route.
- Captured input hashes match both working bytes and exact committed base blobs.
- This observation proposes curation but does not itself mutate inputs. The separately authorized PR workflow may address supported findings in later commits.
- Ignored-inclusive archive traversal found no earlier structured target observation. Historical prose does not count as a formal predecessor.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T235743Z-cecum_mucosa-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: cecum mucosa (BTO:0000213)'
started_at: '2026-10-15T23:39:44Z'
finished_at: '2026-10-15T23:57:43Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected record and sources; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: BTO cecum mucosa has a supported intestinal-mucosa superclass; current BTO
  separately relates it part_of to cecum. The target preserves that distinction and
  the 53-taxon pool with 25 ranked associations. NCBITaxon:541000 is an alias of current
  Oscillospiraceae 216572, not a dangling taxon. Absent optional definition and label
  do not establish a scientific defect.
source:
  git_revision: 0eb609a7ddb34925067116af806e26c165e10678
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
    sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 7158cb696b7e2ac84a8d594a03015711424ff56e21c07a4648ffc6fb2e84a107
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
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: 747e6a5612dc0b7ed881b9fb323fd57ab3c75794d9ee5ebb9d59b2be57dbf8cd
    role: context
  - path: data/habitats/host_associated/cecum_mucosa.yaml
    sha256: aa1ac4b448fed7393cb22b522eddbb86ca9d9d65bccbdbbaf2bd68a94ad5f686
    role: target
  - path: data/habitats/host_associated/intestinal_mucosa.yaml
    sha256: 41d4be2a27877bae0556ae889867dd08a1604b4e036ede7c0a81ccb501730ff9
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
- target_id: BTO:0000213
  path: data/habitats/host_associated/cecum_mucosa.yaml
  label: cecum mucosa
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
  description: Full field-by-field scientific assessment of this exact generated target
    at 0eb609a7ddb34925067116af806e26c165e10678.
  selection: Stale cecum individual observation plus the next 23 identifiers lacking
    completed individual-kind reviews in the ignored-inclusive 3209-record census.
    This bundle assesses one resolved record; previous batch reviews remain valid
    history.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000213
  exclusions:
  - target: Other records, original source specimens and SSSOM/KGX products
    reason: Parent and source context do not add reviewed targets; exports and every
      original source specimen are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/cecum_mucosa.yaml
  exit_code: 0
  target_ids:
  - BTO:0000213
  summary: "Finished 2026-10-15T23:44:42Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cecum_mucosa.yaml"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml
    data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml
    data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml
    data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml
    data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml
    data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml
    data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml
    data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml
    data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml
    data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml
    data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml
    data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml
  exit_code: 0
  target_ids:
  - BTO:0000213
  summary: "Finished 2026-10-15T23:45:51Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml\
    \ data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml\
    \ data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml\
    \ data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml\
    \ data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml\
    \ data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml\
    \ data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml\
    \ data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml\
    \ data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml\
    \ data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml\
    \ data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml\
    \ data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0000213
  summary: 'Finished 2026-10-15T23:46:04Z. No issues found

    829 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0000213
  summary: "Finished 2026-10-15T23:46:05Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0000213
  summary: "Finished 2026-10-15T23:46:28Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0000213
  summary: "Finished 2026-10-15T23:46:34Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0000213
  summary: "Finished 2026-10-15T23:46:59Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0000213
  summary: "Finished 2026-10-15T23:48:03Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict check covers all 24 named targets; other native
    checks have full-corpus scope.
- check_id: CCI
  name: Exact-baseline native QC
  status: passed
  required: true
  command: gh run view 38822113212 --repo CultureBotAI/HabitatMech --json headSha,conclusion,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0000213
  summary: Verified 2026-10-15T23:55:08Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38822113212
  scope_note: Unchanged committed scientific-input baseline; new output bundles are
    outside this run.
- check_id: CREF
  name: Standalone evidence-reference validator applicability
  status: not_applicable
  required: false
  target_ids:
  - BTO:0000213
  summary: No standalone citation/reference validator is documented for these evidence-free
    generated records. Target EvidenceItems and causal edges are absent. Stable source
    and ontology/taxon references were checked manually and with documented native
    gates; current-decision primary citations were separately verified where present.
  scope_note: No command or exit code is invented for an unavailable/nonapplicable
    checker. Full-corpus causal validation ran separately.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/cecum_mucosa.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T23:57:43Z'
  support: supports
  summary: All fields, attestations, taxa and generated history read.
  snapshot_sha256: aa1ac4b448fed7393cb22b522eddbb86ca9d9d65bccbdbbaf2bd68a94ad5f686
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strict broader hierarchy and evidence rules
  accessed_at: '2026-10-15T23:57:43Z'
  support: supports
  summary: Organism, disease, material and habitat identities remain distinct. Parents
    must be strictly broader, not merely containing sites.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation and TaxonAssociation
  accessed_at: '2026-10-15T23:57:43Z'
  support: supports
  summary: Mapping predicate endpoint is source-to-record; source association is weaker
    than characteristic presence. Optional fields and native review status have distinct
    contracts.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native source routes and complete document reproduction
  accessed_at: '2026-10-15T23:57:43Z'
  support: supports
  summary: '[{"mint": "habitatmech:PREGO.1b01d8cfa1", "automatic": {"identifier":
    "BTO:0000213", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0000213", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source counts, channels and taxon ranking
  accessed_at: '2026-10-15T23:57:43Z'
  support: supports
  summary: Exact frozen rows reproduce counts/units and ranked taxon scores. The committed
    projection does not retain original PREGO pair citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313
  accessed_at: '2026-10-15T23:57:43Z'
  support: supports
  summary: '[{"row": 289, "data": {"prego_id": "BTO:0000213", "rank": "1", "taxon_id":
    "NCBITaxon:119852", "taxon_label": "Oscillospira", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    290, "data": {"prego_id": "BTO:0000213", "rank": "2", "taxon_id": "NCBITaxon:1263",
    "taxon_label": "Ruminococcus", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 291, "data": {"prego_id":
    "BTO:0000213", "rank": "3", "taxon_id": "NCBITaxon:128827", "taxon_label": "Erysipelotrichaceae",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 292, "data": {"prego_id": "BTO:0000213", "rank":
    "4", "taxon_id": "NCBITaxon:135569", "taxon_label": "Helicobacter apodemus", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 293, "data": {"prego_id": "BTO:0000213", "rank": "5", "taxon_id":
    "NCBITaxon:1578", "taxon_label": "Lactobacillus", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    294, "data": {"prego_id": "BTO:0000213", "rank": "6", "taxon_id": "NCBITaxon:1598",
    "taxon_label": "Limosilactobacillus reuteri", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    295, "data": {"prego_id": "BTO:0000213", "rank": "7", "taxon_id": "NCBITaxon:171549",
    "taxon_label": "Bacteroidales", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 296, "data": {"prego_id":
    "BTO:0000213", "rank": "8", "taxon_id": "NCBITaxon:171550", "taxon_label": "Rikenellaceae",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 297, "data": {"prego_id": "BTO:0000213", "rank":
    "9", "taxon_id": "NCBITaxon:186802", "taxon_label": "Eubacteriales", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 298, "data": {"prego_id": "BTO:0000213", "rank": "10", "taxon_id":
    "NCBITaxon:186803", "taxon_label": "Lachnospiraceae", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    299, "data": {"prego_id": "BTO:0000213", "rank": "11", "taxon_id": "NCBITaxon:189330",
    "taxon_label": "Dorea", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 300, "data": {"prego_id":
    "BTO:0000213", "rank": "12", "taxon_id": "NCBITaxon:194924", "taxon_label": "Desulfovibrionaceae",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 301, "data": {"prego_id": "BTO:0000213", "rank":
    "13", "taxon_id": "NCBITaxon:209", "taxon_label": "Helicobacter", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 302, "data": {"prego_id": "BTO:0000213", "rank": "14", "taxon_id":
    "NCBITaxon:2353", "taxon_label": "Flexispira", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    303, "data": {"prego_id": "BTO:0000213", "rank": "15", "taxon_id": "NCBITaxon:248039",
    "taxon_label": "Mucispirillum schaedleri", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    304, "data": {"prego_id": "BTO:0000213", "rank": "16", "taxon_id": "NCBITaxon:283168",
    "taxon_label": "Odoribacter", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 305, "data": {"prego_id":
    "BTO:0000213", "rank": "17", "taxon_id": "NCBITaxon:31979", "taxon_label": "Clostridiaceae",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 306, "data": {"prego_id": "BTO:0000213", "rank":
    "18", "taxon_id": "NCBITaxon:33038", "taxon_label": "Mediterraneibacter gnavus",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 307, "data": {"prego_id": "BTO:0000213", "rank":
    "19", "taxon_id": "NCBITaxon:33042", "taxon_label": "Coprococcus", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 308, "data": {"prego_id": "BTO:0000213", "rank": "20", "taxon_id":
    "NCBITaxon:375288", "taxon_label": "Parabacteroides", "prego_score": "4", "direct_flag":
    "TRUE", "channels": "environmental_samples", "corroborated_by": ""}}, {"row":
    309, "data": {"prego_id": "BTO:0000213", "rank": "21", "taxon_id": "NCBITaxon:40544",
    "taxon_label": "Sutterella", "prego_score": "4", "direct_flag": "TRUE", "channels":
    "environmental_samples", "corroborated_by": ""}}, {"row": 310, "data": {"prego_id":
    "BTO:0000213", "rank": "22", "taxon_id": "NCBITaxon:447020", "taxon_label": "Adlercreutzia",
    "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}, {"row": 311, "data": {"prego_id": "BTO:0000213", "rank":
    "23", "taxon_id": "NCBITaxon:51514", "taxon_label": "Dehalobacterium", "prego_score":
    "4", "direct_flag": "TRUE", "channels": "environmental_samples", "corroborated_by":
    ""}}, {"row": 312, "data": {"prego_id": "BTO:0000213", "rank": "24", "taxon_id":
    "NCBITaxon:541000", "taxon_label": "", "prego_score": "4", "direct_flag": "TRUE",
    "channels": "environmental_samples", "corroborated_by": ""}}, {"row": 313, "data":
    {"prego_id": "BTO:0000213", "rank": "25", "taxon_id": "NCBITaxon:543", "taxon_label":
    "Enterobacteriaceae", "prego_score": "4", "direct_flag": "TRUE", "channels": "environmental_samples",
    "corroborated_by": ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 219
  accessed_at: '2026-10-15T23:57:43Z'
  support: supports
  summary: '[{"row": 219, "data": {"prego_id": "BTO:0000213", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "53", "direct_assertion_count":
    "53", "max_prego_score": "4", "channels": "environmental_samples", "prego_synonyms":
    "cecum mucosa|cecum mucosal|cecum mucosas"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 151,409
  accessed_at: '2026-10-15T23:57:43Z'
  support: supports
  summary: '[{"row": 151, "data": {"subject": "BTO:0000213", "predicate": "rdfs:subClassOf",
    "object": "BTO:0000642"}}, {"row": 409, "data": {"subject": "BTO:0000642", "predicate":
    "rdfs:subClassOf", "object": "BTO:0000886"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 215,643
  accessed_at: '2026-10-15T23:57:43Z'
  support: supports
  summary: '[{"row": 215, "data": {"term_id": "BTO:0000213", "ontology": "BTO", "label":
    "cecum mucosa", "definition": "", "synonyms": "", "deprecated": "", "directly_referenced":
    "TRUE", "label_only": "FALSE"}}, {"row": 643, "data": {"term_id": "BTO:0000642",
    "ontology": "BTO", "label": "intestinal mucosa", "definition": "The surface lining
    of the intestines where the cells absorb nutrients.", "synonyms": "", "deprecated":
    "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/intestinal_mucosa.yaml
  locator: Full immediate-parent record; context only
  accessed_at: '2026-10-15T23:57:43Z'
  support: supports
  summary: '{"identifier": "BTO:0000642", "label": "intestinal mucosa", "definition":
    "The surface lining of the intestines where the cells absorb nutrients.", "definition_source":
    "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status":
    "SEEDED", "synonyms": [{"synonym_text": "intestinal mucosal", "synonym_type":
    "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinal mucosas",
    "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats": ["BTO:0000886"],
    "source_attestations": [{"source": "PREGO", "source_id": "BTO:0000642", "source_label":
    "intestinal mucosa", "assertion_count": 1, "assertion_unit": "TAXON", "score":
    3.0, "evidence_channels": "annotated_genomes_isolates"}], "characteristic_taxa":
    [{"taxon_id": "NCBITaxon:272621", "source": "PREGO", "taxon_label": "Lactobacillus
    acidophilus NCFM", "score": 3.0, "rank": 1, "candidate_pool": 1}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by PREGO. Grounding: EXACT."}]}'
  snapshot_sha256: 41d4be2a27877bae0556ae889867dd08a1604b4e036ede7c0a81ccb501730ff9
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000213/graph
  locator: BTO_0000213-graph.json
  accessed_at: '2026-10-15T23:42:01Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000213",
    "target": "http://purl.obolibrary.org/obo/BTO_0000642", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000213",
    "target": "http://purl.obolibrary.org/obo/BTO_0000166", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: f4a0f9884a58d6812c320713ec41d2cd69188adc1c5550ac8374d5da46f50581
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000213
  locator: BTO_0000213.json
  accessed_at: '2026-10-15T23:42:01Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0000213",
    "label": "cecum mucosa", "is_obsolete": false, "description": []}'
  snapshot_sha256: 7df3669b308626228dc8c3b5debb819cff57e44a51c7fa0497271ff63dccde06
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000642/graph
  locator: BTO_0000642-graph.json
  accessed_at: '2026-10-15T23:42:11Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000642",
    "target": "http://purl.obolibrary.org/obo/BTO_0000886", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000642",
    "target": "http://purl.obolibrary.org/obo/BTO_0000648", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: f0e735b83c894c9ae95b392e276ae68a49cdba3e6a6b2dc98f0150d6e7a336f1
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000642
  locator: BTO_0000642.json
  accessed_at: '2026-10-15T23:42:10Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0000642",
    "label": "intestinal mucosa", "is_obsolete": false, "description": ["The surface
    lining of the intestines where the cells absorb nutrients."]}'
  snapshot_sha256: c4b607af8b62dbd62461a58292966ccd427c1f211be4b4dddf9b3fe42a4bf34d
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000886/graph
  locator: BTO_0000886-graph.json
  accessed_at: '2026-10-15T23:42:13Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000886",
    "target": "http://purl.obolibrary.org/obo/BTO_0000634", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 81eea8edab96805ddfa4005f8b213b56f1b0113d2546196c51fbe3f437509e61
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000886
  locator: BTO_0000886.json
  accessed_at: '2026-10-15T23:42:12Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "BTO:0000886",
    "label": "mucosa", "is_obsolete": false, "description": ["A membrane lining all
    body passages that communicate with the air, such as the respiratory and alimentary
    tracts, and having cells and associated glands that secrete mucus."]}'
  snapshot_sha256: f2702c25b61d00fc5ce81a3573dc72d1548eb4d46fdf433408c5c51831ccf40a
- evidence_id: EX7
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-15T23:55:06Z'
  support: context_only
  summary: PMID:35208748, DOI:10.3390/microorganisms10020293. PREGO methods distinguish
    literature, genomic/isolate and environmental channels. BioProject-associated
    abstract mining can yield score-three associations. Source score/channel alone
    is not direct localization, prevalence or characteristic presence; this does not
    establish the extraction route of a particular pair.
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX8
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=100176,100883,102106,102234,1032526,1091138,109326,1095955,1096995,1096996,1096997,1117,1121103,1126011,113286,117563,118747,119852,1213463,122587,1233262,1236904,1238993,1249,1253,1263,1263756,1263757,1263758,1263760,1263761,1263762,1263763,1263835,1265,1266,1268,1269,1279,1280,1280940,1282,128827,1292046,1296,1300,1313,1315977,1329902,135569,1408179,1472682,1578,1598,1639,1643450,171549,171550,1747766,1773,186802,186803,189330,194924,209,2353,243161,248039,272563,280871,283168,314724,31979,33038,33042,375288,40544,447020,51514,539221,541000,543,553198,647227,83262&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T23:42:53Z'
  support: context_only
  summary: 'Current NCBI identities and source-label comparisons: [{"id": "NCBITaxon:119852",
    "source": "PREGO", "label": "Oscillospira", "current_id": "119852", "current_name":
    "Oscillospira", "rank": "genus", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:1263", "source": "PREGO", "label": "Ruminococcus", "current_id":
    "1263", "current_name": "Ruminococcus", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:128827", "source": "PREGO", "label":
    "Erysipelotrichaceae", "current_id": "128827", "current_name": "Erysipelotrichaceae",
    "rank": "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:135569",
    "source": "PREGO", "label": "Helicobacter apodemus", "current_id": "135569", "current_name":
    "Helicobacter apodemus", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1578", "source": "PREGO", "label": "Lactobacillus", "current_id":
    "1578", "current_name": "Lactobacillus", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:1598", "source": "PREGO", "label":
    "Limosilactobacillus reuteri", "current_id": "1598", "current_name": "Limosilactobacillus
    reuteri", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:171549", "source": "PREGO", "label": "Bacteroidales", "current_id":
    "171549", "current_name": "Bacteroidales", "rank": "order", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:171550", "source": "PREGO", "label":
    "Rikenellaceae", "current_id": "171550", "current_name": "Rikenellaceae", "rank":
    "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:186802",
    "source": "PREGO", "label": "Eubacteriales", "current_id": "186802", "current_name":
    "Eubacteriales", "rank": "order", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:186803", "source": "PREGO", "label": "Lachnospiraceae", "current_id":
    "186803", "current_name": "Lachnospiraceae", "rank": "family", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:189330", "source": "PREGO",
    "label": "Dorea", "current_id": "189330", "current_name": "Dorea", "rank": "genus",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:194924", "source":
    "PREGO", "label": "Desulfovibrionaceae", "current_id": "194924", "current_name":
    "Desulfovibrionaceae", "rank": "family", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:209", "source": "PREGO", "label": "Helicobacter", "current_id":
    "209", "current_name": "Helicobacter", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:2353", "source": "PREGO", "label":
    "Flexispira", "current_id": "2353", "current_name": "Flexispira", "rank": "genus",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:248039", "source":
    "PREGO", "label": "Mucispirillum schaedleri", "current_id": "248039", "current_name":
    "Mucispirillum schaedleri", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:283168", "source": "PREGO", "label": "Odoribacter", "current_id":
    "283168", "current_name": "Odoribacter", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:31979", "source": "PREGO", "label":
    "Clostridiaceae", "current_id": "31979", "current_name": "Clostridiaceae", "rank":
    "family", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:33038",
    "source": "PREGO", "label": "Mediterraneibacter gnavus", "current_id": "33038",
    "current_name": "Mediterraneibacter gnavus", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:33042", "source": "PREGO",
    "label": "Coprococcus", "current_id": "33042", "current_name": "Coprococcus",
    "rank": "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:375288",
    "source": "PREGO", "label": "Parabacteroides", "current_id": "375288", "current_name":
    "Parabacteroides", "rank": "genus", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:40544", "source": "PREGO", "label": "Sutterella", "current_id":
    "40544", "current_name": "Sutterella", "rank": "genus", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:447020", "source": "PREGO", "label":
    "Adlercreutzia", "current_id": "447020", "current_name": "Adlercreutzia", "rank":
    "genus", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:51514",
    "source": "PREGO", "label": "Dehalobacterium", "current_id": "51514", "current_name":
    "Dehalobacterium", "rank": "genus", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:541000", "source": "PREGO", "label": null, "current_id":
    "216572", "current_name": "Oscillospiraceae", "rank": "family", "direct_match":
    false, "recognized_alias": false}, {"id": "NCBITaxon:543", "source": "PREGO",
    "label": "Enterobacteriaceae", "current_id": "543", "current_name": "Enterobacteriaceae",
    "rank": "family", "direct_match": true, "recognized_alias": true}]'
  snapshot_sha256: 22118a4a92efa67e2814d38b58438e380bea8eb227b6b5ca7ea1d8af85f80a68
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and review archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0000213 -e 'cecum mucosa' -e cecum_mucosa
    -e habitatmech:PREGO.1b01d8cfa1 curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-15T23:41:33Z'
  support: context_only
  summary: Identifier/label/slug search and full structured-YAML traversal; exact
    TSV rows were parsed separately. Broad search matches are leads, not all independently
    reviewed.
  search_scope: curation, history, research, reports, data/raw, build and reviews,
    including hidden/ignored content; structured traversal independent of gitignore.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -ipath '*prego*'
  accessed_at: '2026-10-15T23:55:07Z'
  support: context_only
  summary: No PREGO-named files were found in the configured checkout. Original pair
    exports remain unavailable there, not proven absent globally.
  search_scope: find over configured kg-microbe checkout including hidden and ignored
    files.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, category, aliases and hierarchy
  outcome: supported
  summary: BTO cecum mucosa has a supported intestinal-mucosa superclass; current
    BTO separately relates it part_of to cecum. The target preserves that distinction
    and the 53-taxon pool with 25 ranked associations. NCBITaxon:541000 is an alias
    of current Oscillospiraceae 216572, not a dangling taxon. Absent optional definition
    and label do not establish a scientific defect.
  target_ids:
  - BTO:0000213
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
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
- assessment_id: A2
  area: quantity
  topic: Source assertions, pools, ranks and supplementary context
  outcome: supported
  summary: 'All emitted counts/units, labels, ranks, scores and candidate pools match
    exact frozen rows. [{"source": "PREGO", "count": 53, "unit": "TAXON"}]. Zero tree
    counts are omitted; later biosamples and study memberships are not added. Current
    taxonomy resolves displayed identifiers including explicit aliases.'
  target_ids:
  - BTO:0000213
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
- assessment_id: A3
  area: evidence
  topic: Biological support and bounded source uncertainty
  outcome: supported
  summary: BTO cecum mucosa has a supported intestinal-mucosa superclass; current
    BTO separately relates it part_of to cecum. The target preserves that distinction
    and the 53-taxon pool with 25 ranked associations. NCBITaxon:541000 is an alias
    of current Oscillospiraceae 216572, not a dangling taxon. Absent optional definition
    and label do not establish a scientific defect.
  target_ids:
  - BTO:0000213
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
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
- assessment_id: A4
  area: completeness
  topic: Native status, optional parameters and causal mechanisms
  outcome: supported
  summary: Executed native resolution reproduces EXACT/SEEDED. No environmental parameters,
    causal graphs, discussions, datasets or is_characteristic=true claims are present.
    Missing optional fields and SEEDED status alone are not defects; parent mechanisms
    are not inherited.
  target_ids:
  - BTO:0000213
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native validation and reproduction
  outcome: supported
  summary: Target schema/strict checks, 829 histories, source provenance, exact 3209-record
    reproduction, 32 causal overlays, 110 term requests and configured label checks
    passed. Exact-base remote full QC passed. Deterministic validity is separate from
    scientific support; reference-check applicability is stated explicitly.
  target_ids:
  - BTO:0000213
  evidence_ids:
  - E1
  - ERULE
findings: []
actions: []
limitations:
- Source counts, ranks and scores do not establish prevalence, viability or characteristic
  presence. Original specimen-level evidence for every source member has not been
  reconstructed.
- Configured label validation skipped 2063 no-adapter pairs; displayed TaxIds were
  separately resolved against current NCBI including aliases.
- Exact-base full QC was verified remotely, not newly executed locally. New saved
  bundles require a separate archive check.
- 'iModulonDB is not applicable: target assertions contain no gene, regulator or expression-module
  claim. No paid research or native status promotion was performed.'
- Original PREGO pair-level exports were not found in the configured checkout. Positive
  primary witnesses do not reconstruct every pair or its extraction route.
notes:
- Captured input hashes match both working bytes and exact committed base blobs.
- This observation proposes curation but does not itself mutate inputs. The separately
  authorized PR workflow may address supported findings in later commits.
- Ignored-inclusive archive traversal found no earlier structured target observation.
  Historical prose does not count as a formal predecessor.
tags:
- individual-scientific-review
- host-associated
```
