# Record review: colonic epithelium (BTO:0001709)

- Review: 20261016T035442Z-colonic_epithelium-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T03:35:49Z
- Finished UTC: 2026-10-16T03:54:42Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

BTO colonic epithelium has a valid intestinal-epithelium superclass and is distinct from whole colon. The single species-level L. plantarum association has score three, not a prevalence estimate. Primary abstracts show strain-specific colonic mucosal co-culture and epithelial-binding experiments, supporting a bounded interaction context without establishing natural localization for all strains or identifying the original PREGO evidence. The absent optional definition and SEEDED status are not themselves defects.

## Scope And Provenance

Full field-by-field assessment of this one resolved generated record.

Selection: One of the next 24 unreviewed records selected in deterministic path order from the ignored-inclusive 3209-record census. This bundle assesses exactly one target, not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 67cde35918d7361de3a1164fb22756cba5d20e30.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0001709 | data/habitats/host_associated/colonic_epithelium.yaml | generated | colonic epithelium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0001709 | Finished 2026-10-16T03:36:18Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/colonic_epithelium.yaml |
| validate-strict | passed | True | BTO:0001709 | Finished 2026-10-16T03:36:32Z. uv run python scripts/validate_strict.py data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0001709 | Finished 2026-10-16T03:36:40Z. No issues found<br>831 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0001709 | Finished 2026-10-16T03:36:40Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0001709 | Finished 2026-10-16T03:37:54Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0001709 | Finished 2026-10-16T03:38:04Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0001709 | Finished 2026-10-16T03:38:23Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0001709 | Finished 2026-10-16T03:39:05Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted native QC | passed | True | BTO:0001709 | Verified 2026-10-16T03:43:47Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38843593114 |
| Displayed candidate-pool correspondence | passed | False | BTO:0001709 | Finished 2026-10-16T03:54:30Z. All 60 displayed candidate pools equal exact source taxon totals. |
| Standalone citation validation applicability | not_applicable | False | BTO:0001709 | No standalone citation checker is documented for these evidence-free generated targets. Stable references were checked with native gates and current authorities; causal validation ran globally. |

## Scientific And Domain Assessments

### Identity, grounding, aliases and strictly broader hierarchy

identity: supported. Targets: BTO:0001709.

BTO colonic epithelium has a valid intestinal-epithelium superclass and is distinct from whole colon. The single species-level L. plantarum association has score three, not a prevalence estimate. Primary abstracts show strain-specific colonic mucosal co-culture and epithelial-binding experiments, supporting a bounded interaction context without establishing natural localization for all strains or identifying the original PREGO evidence. The absent optional definition and SEEDED status are not themselves defects.

### Native source units, ranks, scores and candidate pools

quantity: supported. Targets: BTO:0001709.

Exact source rows reproduce every emitted count/unit and displayed taxon rank/score/pool. Zero tree counts are omitted; supplemental biosamples, study memberships and triads are nonadditive. {"assertions": [{"source": "PREGO", "count": 1, "unit": "TAXON", "row": {"row": 610, "data": {"prego_id": "BTO:0001709", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "colon epithelia&#124;colon epithelial&#124;colon epithelium&#124;colon epitheliums&#124;colonic epithelia&#124;colonic epithelial&#124;colonic epithelium&#124;colonic epitheliums"}}}], "taxa": [{"id": "NCBITaxon:1590", "source": "PREGO", "label": "Lactiplantibacillus plantarum", "current_id": "1590", "current_name": "Lactiplantibacillus plantarum", "rank": "species", "direct_match": true, "recognized_alias": true, "other_names": ["Lactobacillus arabinosus", "Lactobacillus arizonensis", "Lactobacillus plantarum (Orla-Jensen 1919) Bergey et al. 1923 (Approved Lists 1980)", "Lactobacterium plantarum", "Streptobacterium plantarum", "Lactobacillus sp. DMR09", "Lactobacillus sp. HC-2", "Lactobacillus sp. Lact08", "Lactobacillus sp. Lact09", "Lactobacillus sp. Lact14", "Lactobacillus sp. M6DWS", "Lactobacillus sp. S2", "Lactobacillus sp. S8", "Lactobacillus sp. XJ25", "Lactobacillus sp. Z12", "Weissella sp. Lact07", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            ", "\n            "], "source_row": {"row": 2443, "data": {"prego_id": "BTO:0001709", "rank": "1", "taxon_id": "NCBITaxon:1590", "taxon_label": "Lactiplantibacillus plantarum", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}]}

### Association evidence and claim scope

evidence: supported. Targets: BTO:0001709.

Current ontology/TaxId identities and source attestations were verified. BTO colonic epithelium has a valid intestinal-epithelium superclass and is distinct from whole colon. The single species-level L. plantarum association has score three, not a prevalence estimate. Primary abstracts show strain-specific colonic mucosal co-culture and epithelial-binding experiments, supporting a bounded interaction context without establishing natural localization for all strains or identifying the original PREGO evidence. The absent optional definition and SEEDED status are not themselves defects. Individual papers support only the stated scope; original source pairs were not exhaustively reconstructed.

### Native lifecycle, optional content and mechanism limits

completeness: supported. Targets: BTO:0001709.

Executed native routes reproduce EXACT/SEEDED. Required content is present. No optional environmental parameters, causal graph, discussion, dataset or characteristic-presence claim is fabricated. Missing ITEM status alone is not a defect; no status or history promotion is performed.

### Native validation and reproducibility

schema: supported. Targets: BTO:0001709.

31 baseline commands passed: target schema, cohort strict, 831 histories, source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured labels. Exact-base hosted QC passed. Deterministic validity is not scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/colonic_epithelium.yaml; Entire generated target YAML | supports | All fields, source attestations, displayed taxa, aliases and complete generated history read. |
| ERULE | docs/CURATION.md; Identity, evidence and strictly broader parents | supports | All parent contributions must be strictly broader; source context, anatomy, host and diagnosis are distinct. Optional absence is not a required-field defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and GroundingStatusEnum | supports | The mapping contract compares source concept to record identifier; source-is-record omits the predicate. Native status and association rules are preserved. |
| ESEED | src/habitatmech/seed.py; Executed source routes and entire document reproduction | supports | [{"mint": "habitatmech:PREGO.68c4307863", "automatic": {"identifier": "BTO:0001709", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0001709", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source counts, source-strain-taxon join and PREGO scoring/ranking | supports | Inspected native projections. Original BacDive source-strain join and PREGO pair citation evidence are not retained in the compact per-habitat taxon tables. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 2443 | supports | [{"row": 2443, "data": {"prego_id": "BTO:0001709", "rank": "1", "taxon_id": "NCBITaxon:1590", "taxon_label": "Lactiplantibacillus plantarum", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 610 | supports | [{"row": 610, "data": {"prego_id": "BTO:0001709", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "colon epithelia&#124;colon epithelial&#124;colon epithelium&#124;colon epitheliums&#124;colonic epithelia&#124;colonic epithelial&#124;colonic epithelium&#124;colonic epitheliums"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 515,1160 | supports | [{"row": 515, "data": {"subject": "BTO:0000781", "predicate": "rdfs:subClassOf", "object": "BTO:0000416"}}, {"row": 1160, "data": {"subject": "BTO:0001709", "predicate": "rdfs:subClassOf", "object": "BTO:0000781"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 782,1709 | supports | [{"row": 782, "data": {"term_id": "BTO:0000781", "ontology": "BTO", "label": "intestinal epithelium", "definition": "The endodermally-derived epithelium of the intestine varies considerably, but the absorptive epithelium of small intestine is usually implied.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 1709, "data": {"term_id": "BTO:0001709", "ontology": "BTO", "label": "colonic epithelium", "definition": "", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| EP9 | data/habitats/host_associated/intestinal_epithelium.yaml; Immediate parent record, context only | supports | {"identifier": "BTO:0000781", "label": "intestinal epithelium", "definition": "The endodermally-derived epithelium of the intestine varies considerably, but the absorptive epithelium of small intestine is usually implied.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "intestinal epithelia", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinal epithelial", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinal epitheliums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats": ["BTO:0000416"], "source_attestations": [{"source": "PREGO", "source_id": "BTO:0000781", "source_label": "intestinal epithelium", "assertion_count": 34, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "annotated_genomes_isolates&#124;environmental_samples"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:1263", "source": "PREGO", "taxon_label": "Ruminococcus", "score": 4.0, "rank": 1, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:1485", "source": "PREGO", "taxon_label": "Clostridium", "score": 4.0, "rank": 2, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:1578", "source": "PREGO", "taxon_label": "Lactobacillus", "score": 4.0, "rank": 3, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:171549", "source": "PREGO", "taxon_label": "Bacteroidales", "score": 4.0, "rank": 4, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:186802", "source": "PREGO", "taxon_label": "Eubacteriales", "score": 4.0, "rank": 5, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:191303", "source": "PREGO", "taxon_label": "Turicibacter", "score": 4.0, "rank": 6, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:248039", "source": "PREGO", "taxon_label": "Mucispirillum schaedleri", "score": 4.0, "rank": 7, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:31979", "source": "PREGO", "taxon_label": "Clostridiaceae", "score": 4.0, "rank": 8, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:541000", "source": "PREGO", "score": 4.0, "rank": 9, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:543", "source": "PREGO", "taxon_label": "Enterobacteriaceae", "score": 4.0, "rank": 10, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:1205679", "source": "PREGO", "taxon_label": "Bifidobacterium longum subsp. longum CECT 7347", "score": 3.0, "rank": 11, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:1224749", "source": "PREGO", "taxon_label": "Exiguobacterium sp. ZWU0009", "score": 3.0, "rank": 12, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:340186", "source": "PREGO", "taxon_label": "Escherichia coli E110019", "score": 3.0, "rank": 13, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:555970", "source": "PREGO", "taxon_label": "Bifidobacterium animalis subsp. lactis DSM 10140", "score": 3.0, "rank": 14, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:580050", "source": "PREGO", "taxon_label": "Bifidobacterium animalis subsp. lactis Bl-04", "score": 3.0, "rank": 15, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:186803", "source": "PREGO", "taxon_label": "Lachnospiraceae", "score": 1.78273, "rank": 16, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:1598", "source": "PREGO", "taxon_label": "Limosilactobacillus reuteri", "score": 1.69324, "rank": 17, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:33042", "source": "PREGO", "taxon_label": "Coprococcus", "score": 1.69324, "rank": 18, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:119852", "source": "PREGO", "taxon_label": "Oscillospira", "score": 1.6655, "rank": 19, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:35493", "source": "PREGO", "score": 1.65121, "rank": 20, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:838", "source": "PREGO", "taxon_label": "Prevotella", "score": 1.62176, "rank": 21, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:158851", "source": "PREGO", "taxon_label": "Trabulsiella", "score": 1.57521, "rank": 22, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:33038", "source": "PREGO", "taxon_label": "Mediterraneibacter gnavus", "score": 1.57521, "rank": 23, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:171550", "source": "PREGO", "taxon_label": "Rikenellaceae", "score": 1.50806, "rank": 24, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:186804", "source": "PREGO", "taxon_label": "Peptostreptococcaceae", "score": 1.49025, "rank": 25, "candidate_pool": 34}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: EXACT."}]} |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000416/graph; BTO_0000416-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000416", "target": "http://purl.obolibrary.org/obo/BTO_0000634", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000416; BTO_0000416.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "BTO:0000416", "label": "epithelium", "is_obsolete": false, "description": ["A membranous cellular tissue that covers a free surface or lines a tube or cavity of an animal body and serves especially to enclose and protect the other parts of the body, to produce secretions and excretions, and to function in assimilation."], "obo_synonym": null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"], "id": ["BTO:0000416"]}} |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000781/graph; BTO_0000781-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000781", "target": "http://purl.obolibrary.org/obo/BTO_0000416", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000781", "target": "http://purl.obolibrary.org/obo/BTO_0000648", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000781; BTO_0000781.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "BTO:0000781", "label": "intestinal epithelium", "is_obsolete": false, "description": ["The endodermally-derived epithelium of the intestine varies considerably, but the absorptive epithelium of small intestine is usually implied."], "obo_synonym": null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"], "id": ["BTO:0000781"]}} |
| EX14 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001709/graph; BTO_0001709-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001709", "target": "http://purl.obolibrary.org/obo/BTO_0000781", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0001709", "target": "http://purl.obolibrary.org/obo/BTO_0000269", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX15 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001709; BTO_0001709.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "BTO:0001709", "label": "colonic epithelium", "is_obsolete": false, "description": [], "obo_synonym": null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"], "id": ["BTO:0001709"]}} |
| EX16 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PMID:35208748; DOI:10.3390/microorganisms10020293. Methods and scoring appendix inspected: channels have different evidence and scoring; score-three BioProject associations can derive from abstract mining. This does not identify the extraction route of any particular retained pair. |
| EX17 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Lactobacillus%20plantarum%22%20AND%20%28TITLE%3Aadhesion%20OR%20TITLE%3Amucosa%20OR%20TITLE%3Aepithelial%29%20AND%20FIRST_PDATE%3A%5B1990-01-01%20TO%202020-12-31%5D&amp;format=json&amp;resultType=core&amp;pageSize=50; paper-plantarum-adhesion.json | context_only | Primary abstracts PMID:22669626 (DOI:10.1007/s12263-012-0301-y) and PMID:23395591 (DOI:10.1016/j.micres.2013.01.003) inspected. Colonic mucosal co-culture uses 299v and an adhesion mutant; a separate study assays binding of surface enzymes to Caco-2 cells. Bounded experimental context only. The first full text was unavailable (EPMC HTTP500; PMC browser challenge). |
| EX18 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=102234,1027273,1048357,1069963,1074311,1110509,1117,1120968,1120983,1121027,1150864,1173995,119852,1216969,1224163,1234143,1234144,1245026,1263,1280004,1292046,1297579,1342794,1342818,1348114,1385512,1401264,141693,1449351,1452538,1453497,1479025,1481923,1485,1578,1590,171549,171550,171552,186802,186803,189330,248039,31979,33038,33042,375288,384676,411459,411460,444103,51514,541000,560080,572511,816,830,838,85831,872&amp;retmode=xml; taxonomy.xml | context_only | Current exact TaxId resolutions, including merged IDs and labels: [{"id": "NCBITaxon:1590", "source": "PREGO", "label": "Lactiplantibacillus plantarum", "current_id": "1590", "current_name": "Lactiplantibacillus plantarum", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local source/curation/review corpus; rg --no-ignore --hidden -l -F -e BTO:0001709 -e 'colonic epithelium' -e colonic_epithelium -e habitatmech:PREGO.68c4307863 curation history research reports data/raw build reviews | context_only | Source rows were parsed by exact keys; broad name hits were leads, not all inspected. No formal structured target predecessor. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f '(' -ipath '*prego*' -o -ipath '*bacdive*' ')' | context_only | Search found BacDive notebooks and Git metadata, but no manifest-matching BacDive/PREGO transformed node/edge exports. No claim of global absence. |

## Limits And Additional Notes

- Original specimen-level evidence and every pair-level citation were not exhaustively reconstructed. Source associations, counts, ranks and scores are not prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs; target TaxIds were separately resolved with current NCBI.
- Exact-base hosted QC covers unchanged scientific inputs, not a new local full-QC execution or these new review files. Each new bundle requires native validation/save and the subsequent archive check.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. Cited experiments are used only for identity and context, not imported causal mechanisms.
- Original source-strain or PREGO pair exports were unavailable in the configured checkout; no uncertain association is removed or source count rewritten.
- Selected primary full text was unavailable (EPMC HTTP500; PMC browser challenge); inspected abstracts and available authorities are explicitly distinguished from full methods.
- Captured working_tree provenance is retained. All local input hashes were additionally checked against exact base 67cde35918d7361de3a1164fb22756cba5d20e30.
- Read-only review: no source, curation, generated record, status or history edit; no GitHub mutation or paid research.
- Ignored-inclusive structured archive traversal found no previous structured target review. Legacy prose is contextual evidence, not formal predecessor lineage or issue closure.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T035442Z-colonic_epithelium-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: colonic epithelium (BTO:0001709)'
started_at: '2026-10-16T03:35:49Z'
finished_at: '2026-10-16T03:54:42Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assessed all evidence and target; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: BTO colonic epithelium has a valid intestinal-epithelium superclass and is
  distinct from whole colon. The single species-level L. plantarum association has
  score three, not a prevalence estimate. Primary abstracts show strain-specific colonic
  mucosal co-culture and epithelial-binding experiments, supporting a bounded interaction
  context without establishing natural localization for all strains or identifying
  the original PREGO evidence. The absent optional definition and SEEDED status are
  not themselves defects.
source:
  git_revision: 67cde35918d7361de3a1164fb22756cba5d20e30
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
    sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 04ba048af6f93b69c127bc3d47e2403dbe153452c75f9e26939188fc5daa52d7
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
  - path: data/habitats/host_associated/colonic_epithelium.yaml
    sha256: d8cb4e9542a2a519633b1dce24e14ab85dee49a0ee39f6c58a6493786217c09e
    role: target
  - path: data/habitats/host_associated/intestinal_epithelium.yaml
    sha256: 2bbbf509cc5639d693e335c3dcda9aa871c8beacd327b3f188e514010f1ab3e4
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
- target_id: BTO:0001709
  path: data/habitats/host_associated/colonic_epithelium.yaml
  label: colonic epithelium
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
  description: Full field-by-field assessment of this one resolved generated record.
  selection: One of the next 24 unreviewed records selected in deterministic path
    order from the ignored-inclusive 3209-record census. This bundle assesses exactly
    one target, not a proxy sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0001709
  exclusions:
  - target: Other records, individual source specimens and SSSOM/KGX products
    reason: Parent context is not additional review coverage; original specimens and
      exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/colonic_epithelium.yaml
  exit_code: 0
  target_ids:
  - BTO:0001709
  summary: "Finished 2026-10-16T03:36:18Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/colonic_epithelium.yaml"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml
    data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml
    data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml
    data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml
    data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml
    data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml
    data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml
    data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml
    data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml
    data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml
    data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml
    data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml
  exit_code: 0
  target_ids:
  - BTO:0001709
  summary: "Finished 2026-10-16T03:36:32Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml\
    \ data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml\
    \ data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml\
    \ data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml\
    \ data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml\
    \ data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml\
    \ data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml\
    \ data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml\
    \ data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml\
    \ data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml\
    \ data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml\
    \ data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0001709
  summary: 'Finished 2026-10-16T03:36:40Z. No issues found

    831 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0001709
  summary: "Finished 2026-10-16T03:36:40Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0001709
  summary: "Finished 2026-10-16T03:37:54Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0001709
  summary: "Finished 2026-10-16T03:38:04Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0001709
  summary: "Finished 2026-10-16T03:38:23Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0001709
  summary: "Finished 2026-10-16T03:39:05Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: CCI
  name: Exact-base hosted native QC
  status: passed
  required: true
  command: gh run view 38843593114 --repo CultureBotAI/HabitatMech --json headSha,conclusion,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0001709
  summary: Verified 2026-10-16T03:43:47Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38843593114
  scope_note: Unchanged scientific-input base only. Not a claim that the new output
    bundles were part of the earlier run.
- check_id: CPOOL
  name: Displayed candidate-pool correspondence
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/habitatmech-review-cq-author.py pool_check
  exit_code: 0
  target_ids:
  - BTO:0001709
  summary: Finished 2026-10-16T03:54:30Z. All 60 displayed candidate pools equal exact
    source taxon totals.
  scope_note: Supplemental mechanical cross-check of all 60 displayed taxon entries;
    not a replacement for native validators or scientific evidence.
- check_id: CREF
  name: Standalone citation validation applicability
  status: not_applicable
  required: false
  target_ids:
  - BTO:0001709
  summary: No standalone citation checker is documented for these evidence-free generated
    targets. Stable references were checked with native gates and current authorities;
    causal validation ran globally.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/colonic_epithelium.yaml
  locator: Entire generated target YAML
  accessed_at: '2026-10-16T03:54:41Z'
  support: supports
  summary: All fields, source attestations, displayed taxa, aliases and complete generated
    history read.
  snapshot_sha256: d8cb4e9542a2a519633b1dce24e14ab85dee49a0ee39f6c58a6493786217c09e
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, evidence and strictly broader parents
  accessed_at: '2026-10-16T03:54:41Z'
  support: supports
  summary: All parent contributions must be strictly broader; source context, anatomy,
    host and diagnosis are distinct. Optional absence is not a required-field defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and GroundingStatusEnum
  accessed_at: '2026-10-16T03:54:41Z'
  support: supports
  summary: The mapping contract compares source concept to record identifier; source-is-record
    omits the predicate. Native status and association rules are preserved.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source routes and entire document reproduction
  accessed_at: '2026-10-16T03:54:41Z'
  support: supports
  summary: '[{"mint": "habitatmech:PREGO.68c4307863", "automatic": {"identifier":
    "BTO:0001709", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0001709", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source counts, source-strain-taxon join and PREGO scoring/ranking
  accessed_at: '2026-10-16T03:54:41Z'
  support: supports
  summary: Inspected native projections. Original BacDive source-strain join and PREGO
    pair citation evidence are not retained in the compact per-habitat taxon tables.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 2443
  accessed_at: '2026-10-16T03:54:41Z'
  support: supports
  summary: '[{"row": 2443, "data": {"prego_id": "BTO:0001709", "rank": "1", "taxon_id":
    "NCBITaxon:1590", "taxon_label": "Lactiplantibacillus plantarum", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 610
  accessed_at: '2026-10-16T03:54:41Z'
  support: supports
  summary: '[{"row": 610, "data": {"prego_id": "BTO:0001709", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count":
    "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "colon epithelia|colon epithelial|colon epithelium|colon epitheliums|colonic epithelia|colonic
    epithelial|colonic epithelium|colonic epitheliums"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 515,1160
  accessed_at: '2026-10-16T03:54:41Z'
  support: supports
  summary: '[{"row": 515, "data": {"subject": "BTO:0000781", "predicate": "rdfs:subClassOf",
    "object": "BTO:0000416"}}, {"row": 1160, "data": {"subject": "BTO:0001709", "predicate":
    "rdfs:subClassOf", "object": "BTO:0000781"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 782,1709
  accessed_at: '2026-10-16T03:54:41Z'
  support: supports
  summary: '[{"row": 782, "data": {"term_id": "BTO:0000781", "ontology": "BTO", "label":
    "intestinal epithelium", "definition": "The endodermally-derived epithelium of
    the intestine varies considerably, but the absorptive epithelium of small intestine
    is usually implied.", "synonyms": "", "deprecated": "", "directly_referenced":
    "TRUE", "label_only": "FALSE"}}, {"row": 1709, "data": {"term_id": "BTO:0001709",
    "ontology": "BTO", "label": "colonic epithelium", "definition": "", "synonyms":
    "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/intestinal_epithelium.yaml
  locator: Immediate parent record, context only
  accessed_at: '2026-10-16T03:54:41Z'
  support: supports
  summary: '{"identifier": "BTO:0000781", "label": "intestinal epithelium", "definition":
    "The endodermally-derived epithelium of the intestine varies considerably, but
    the absorptive epithelium of small intestine is usually implied.", "definition_source":
    "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status":
    "SEEDED", "synonyms": [{"synonym_text": "intestinal epithelia", "synonym_type":
    "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinal epithelial",
    "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "intestinal
    epitheliums", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "parent_habitats":
    ["BTO:0000416"], "source_attestations": [{"source": "PREGO", "source_id": "BTO:0000781",
    "source_label": "intestinal epithelium", "assertion_count": 34, "assertion_unit":
    "TAXON", "score": 4.0, "evidence_channels": "annotated_genomes_isolates|environmental_samples"}],
    "characteristic_taxa": [{"taxon_id": "NCBITaxon:1263", "source": "PREGO", "taxon_label":
    "Ruminococcus", "score": 4.0, "rank": 1, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:1485",
    "source": "PREGO", "taxon_label": "Clostridium", "score": 4.0, "rank": 2, "candidate_pool":
    34}, {"taxon_id": "NCBITaxon:1578", "source": "PREGO", "taxon_label": "Lactobacillus",
    "score": 4.0, "rank": 3, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:171549",
    "source": "PREGO", "taxon_label": "Bacteroidales", "score": 4.0, "rank": 4, "candidate_pool":
    34}, {"taxon_id": "NCBITaxon:186802", "source": "PREGO", "taxon_label": "Eubacteriales",
    "score": 4.0, "rank": 5, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:191303",
    "source": "PREGO", "taxon_label": "Turicibacter", "score": 4.0, "rank": 6, "candidate_pool":
    34}, {"taxon_id": "NCBITaxon:248039", "source": "PREGO", "taxon_label": "Mucispirillum
    schaedleri", "score": 4.0, "rank": 7, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:31979",
    "source": "PREGO", "taxon_label": "Clostridiaceae", "score": 4.0, "rank": 8, "candidate_pool":
    34}, {"taxon_id": "NCBITaxon:541000", "source": "PREGO", "score": 4.0, "rank":
    9, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:543", "source": "PREGO", "taxon_label":
    "Enterobacteriaceae", "score": 4.0, "rank": 10, "candidate_pool": 34}, {"taxon_id":
    "NCBITaxon:1205679", "source": "PREGO", "taxon_label": "Bifidobacterium longum
    subsp. longum CECT 7347", "score": 3.0, "rank": 11, "candidate_pool": 34}, {"taxon_id":
    "NCBITaxon:1224749", "source": "PREGO", "taxon_label": "Exiguobacterium sp. ZWU0009",
    "score": 3.0, "rank": 12, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:340186",
    "source": "PREGO", "taxon_label": "Escherichia coli E110019", "score": 3.0, "rank":
    13, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:555970", "source": "PREGO",
    "taxon_label": "Bifidobacterium animalis subsp. lactis DSM 10140", "score": 3.0,
    "rank": 14, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:580050", "source":
    "PREGO", "taxon_label": "Bifidobacterium animalis subsp. lactis Bl-04", "score":
    3.0, "rank": 15, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:186803", "source":
    "PREGO", "taxon_label": "Lachnospiraceae", "score": 1.78273, "rank": 16, "candidate_pool":
    34}, {"taxon_id": "NCBITaxon:1598", "source": "PREGO", "taxon_label": "Limosilactobacillus
    reuteri", "score": 1.69324, "rank": 17, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:33042",
    "source": "PREGO", "taxon_label": "Coprococcus", "score": 1.69324, "rank": 18,
    "candidate_pool": 34}, {"taxon_id": "NCBITaxon:119852", "source": "PREGO", "taxon_label":
    "Oscillospira", "score": 1.6655, "rank": 19, "candidate_pool": 34}, {"taxon_id":
    "NCBITaxon:35493", "source": "PREGO", "score": 1.65121, "rank": 20, "candidate_pool":
    34}, {"taxon_id": "NCBITaxon:838", "source": "PREGO", "taxon_label": "Prevotella",
    "score": 1.62176, "rank": 21, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:158851",
    "source": "PREGO", "taxon_label": "Trabulsiella", "score": 1.57521, "rank": 22,
    "candidate_pool": 34}, {"taxon_id": "NCBITaxon:33038", "source": "PREGO", "taxon_label":
    "Mediterraneibacter gnavus", "score": 1.57521, "rank": 23, "candidate_pool": 34},
    {"taxon_id": "NCBITaxon:171550", "source": "PREGO", "taxon_label": "Rikenellaceae",
    "score": 1.50806, "rank": 24, "candidate_pool": 34}, {"taxon_id": "NCBITaxon:186804",
    "source": "PREGO", "taxon_label": "Peptostreptococcaceae", "score": 1.49025, "rank":
    25, "candidate_pool": 34}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by PREGO. Grounding: EXACT."}]}'
  snapshot_sha256: 2bbbf509cc5639d693e335c3dcda9aa871c8beacd327b3f188e514010f1ab3e4
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000416/graph
  locator: BTO_0000416-graph.json
  accessed_at: '2026-10-16T03:36:41Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000416",
    "target": "http://purl.obolibrary.org/obo/BTO_0000634", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: e50888bed6bfcd90ce1b785f823effc7c973c728796ab6381c9a4f5e0d6040cc
- evidence_id: EX11
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000416
  locator: BTO_0000416.json
  accessed_at: '2026-10-16T03:36:40Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "BTO:0000416", "label": "epithelium", "is_obsolete": false, "description": ["A
    membranous cellular tissue that covers a free surface or lines a tube or cavity
    of an animal body and serves especially to enclose and protect the other parts
    of the body, to produce secretions and excretions, and to function in assimilation."],
    "obo_synonym": null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"],
    "id": ["BTO:0000416"]}}'
  snapshot_sha256: 094a4c6c194f28a9c1f5319bbc931433bd6f01da8bdc3a42c015c0a54574c535
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000781/graph
  locator: BTO_0000781-graph.json
  accessed_at: '2026-10-16T03:36:46Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000781",
    "target": "http://purl.obolibrary.org/obo/BTO_0000416", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000781",
    "target": "http://purl.obolibrary.org/obo/BTO_0000648", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 89f79f359253a30a37e7de50b0f18fe9ee4a347c3d53bc29ced0ec0d6683420c
- evidence_id: EX13
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000781
  locator: BTO_0000781.json
  accessed_at: '2026-10-16T03:36:46Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "BTO:0000781", "label": "intestinal epithelium", "is_obsolete": false, "description":
    ["The endodermally-derived epithelium of the intestine varies considerably, but
    the absorptive epithelium of small intestine is usually implied."], "obo_synonym":
    null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"], "id": ["BTO:0000781"]}}'
  snapshot_sha256: 0b47d6f81b0bf4a3985945a4fb817fb13037328abc3ccf534f57685b48772988
- evidence_id: EX14
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001709/graph
  locator: BTO_0001709-graph.json
  accessed_at: '2026-10-16T03:36:59Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001709",
    "target": "http://purl.obolibrary.org/obo/BTO_0000781", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0001709",
    "target": "http://purl.obolibrary.org/obo/BTO_0000269", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: aef60426b0c69cfb57b900f1f80d76997680f065e8fd4be7f7c9e1e93e578fe3
- evidence_id: EX15
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001709
  locator: BTO_0001709.json
  accessed_at: '2026-10-16T03:36:58Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "BTO:0001709", "label": "colonic epithelium", "is_obsolete": false, "description":
    [], "obo_synonym": null, "annotation": {"has_obo_namespace": ["BrendaTissueOBO"],
    "id": ["BTO:0001709"]}}'
  snapshot_sha256: 151c3731d37d6180f9d3b5ac8c09ef8d1f4f45427f797f400cf5230c8f6272d4
- evidence_id: EX16
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-16T03:52:56Z'
  support: context_only
  summary: 'PMID:35208748; DOI:10.3390/microorganisms10020293. Methods and scoring
    appendix inspected: channels have different evidence and scoring; score-three
    BioProject associations can derive from abstract mining. This does not identify
    the extraction route of any particular retained pair.'
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX17
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Lactobacillus%20plantarum%22%20AND%20%28TITLE%3Aadhesion%20OR%20TITLE%3Amucosa%20OR%20TITLE%3Aepithelial%29%20AND%20FIRST_PDATE%3A%5B1990-01-01%20TO%202020-12-31%5D&format=json&resultType=core&pageSize=50
  locator: paper-plantarum-adhesion.json
  accessed_at: '2026-10-16T03:46:35Z'
  support: context_only
  summary: Primary abstracts PMID:22669626 (DOI:10.1007/s12263-012-0301-y) and PMID:23395591
    (DOI:10.1016/j.micres.2013.01.003) inspected. Colonic mucosal co-culture uses
    299v and an adhesion mutant; a separate study assays binding of surface enzymes
    to Caco-2 cells. Bounded experimental context only. The first full text was unavailable
    (EPMC HTTP500; PMC browser challenge).
  snapshot_sha256: fee88c7465d982d1310b20c99d7ec872cf2ea2566d5ac8562a280d50b1d9e5bb
- evidence_id: EX18
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=102234,1027273,1048357,1069963,1074311,1110509,1117,1120968,1120983,1121027,1150864,1173995,119852,1216969,1224163,1234143,1234144,1245026,1263,1280004,1292046,1297579,1342794,1342818,1348114,1385512,1401264,141693,1449351,1452538,1453497,1479025,1481923,1485,1578,1590,171549,171550,171552,186802,186803,189330,248039,31979,33038,33042,375288,384676,411459,411460,444103,51514,541000,560080,572511,816,830,838,85831,872&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-16T03:37:40Z'
  support: context_only
  summary: 'Current exact TaxId resolutions, including merged IDs and labels: [{"id":
    "NCBITaxon:1590", "source": "PREGO", "label": "Lactiplantibacillus plantarum",
    "current_id": "1590", "current_name": "Lactiplantibacillus plantarum", "rank":
    "species", "direct_match": true, "recognized_alias": true}]'
  snapshot_sha256: 8cc30a816c5940897a93cd10094f921f070f1378c3dab63db865fd736db4f15b
- evidence_id: ESEARCH
  kind: search
  reference: Local source/curation/review corpus
  locator: rg --no-ignore --hidden -l -F -e BTO:0001709 -e 'colonic epithelium' -e
    colonic_epithelium -e habitatmech:PREGO.68c4307863 curation history research reports
    data/raw build reviews
  accessed_at: '2026-10-16T03:36:40Z'
  support: context_only
  summary: Source rows were parsed by exact keys; broad name hits were leads, not
    all inspected. No formal structured target predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews
    including hidden/ignored files; structured YAML archive parsed independently of
    gitignore.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f '(' -ipath '*prego*' -o -ipath '*bacdive*' ')'
  accessed_at: '2026-10-16T03:46:37Z'
  support: context_only
  summary: Search found BacDive notebooks and Git metadata, but no manifest-matching
    BacDive/PREGO transformed node/edge exports. No claim of global absence.
  search_scope: find across the configured checkout, including hidden and ignored
    files.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, grounding, aliases and strictly broader hierarchy
  outcome: supported
  summary: BTO colonic epithelium has a valid intestinal-epithelium superclass and
    is distinct from whole colon. The single species-level L. plantarum association
    has score three, not a prevalence estimate. Primary abstracts show strain-specific
    colonic mucosal co-culture and epithelial-binding experiments, supporting a bounded
    interaction context without establishing natural localization for all strains
    or identifying the original PREGO evidence. The absent optional definition and
    SEEDED status are not themselves defects.
  target_ids:
  - BTO:0001709
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
  - EP9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
- assessment_id: A2
  area: quantity
  topic: Native source units, ranks, scores and candidate pools
  outcome: supported
  summary: 'Exact source rows reproduce every emitted count/unit and displayed taxon
    rank/score/pool. Zero tree counts are omitted; supplemental biosamples, study
    memberships and triads are nonadditive. {"assertions": [{"source": "PREGO", "count":
    1, "unit": "TAXON", "row": {"row": 610, "data": {"prego_id": "BTO:0001709", "ontology":
    "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count":
    "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates",
    "prego_synonyms": "colon epithelia|colon epithelial|colon epithelium|colon epitheliums|colonic
    epithelia|colonic epithelial|colonic epithelium|colonic epitheliums"}}}], "taxa":
    [{"id": "NCBITaxon:1590", "source": "PREGO", "label": "Lactiplantibacillus plantarum",
    "current_id": "1590", "current_name": "Lactiplantibacillus plantarum", "rank":
    "species", "direct_match": true, "recognized_alias": true, "other_names": ["Lactobacillus
    arabinosus", "Lactobacillus arizonensis", "Lactobacillus plantarum (Orla-Jensen
    1919) Bergey et al. 1923 (Approved Lists 1980)", "Lactobacterium plantarum", "Streptobacterium
    plantarum", "Lactobacillus sp. DMR09", "Lactobacillus sp. HC-2", "Lactobacillus
    sp. Lact08", "Lactobacillus sp. Lact09", "Lactobacillus sp. Lact14", "Lactobacillus
    sp. M6DWS", "Lactobacillus sp. S2", "Lactobacillus sp. S8", "Lactobacillus sp.
    XJ25", "Lactobacillus sp. Z12", "Weissella sp. Lact07", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            ",
    "\n            ", "\n            ", "\n            ", "\n            ", "\n            "],
    "source_row": {"row": 2443, "data": {"prego_id": "BTO:0001709", "rank": "1", "taxon_id":
    "NCBITaxon:1590", "taxon_label": "Lactiplantibacillus plantarum", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}}]}'
  target_ids:
  - BTO:0001709
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
  - EP9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
- assessment_id: A3
  area: evidence
  topic: Association evidence and claim scope
  outcome: supported
  summary: Current ontology/TaxId identities and source attestations were verified.
    BTO colonic epithelium has a valid intestinal-epithelium superclass and is distinct
    from whole colon. The single species-level L. plantarum association has score
    three, not a prevalence estimate. Primary abstracts show strain-specific colonic
    mucosal co-culture and epithelial-binding experiments, supporting a bounded interaction
    context without establishing natural localization for all strains or identifying
    the original PREGO evidence. The absent optional definition and SEEDED status
    are not themselves defects. Individual papers support only the stated scope; original
    source pairs were not exhaustively reconstructed.
  target_ids:
  - BTO:0001709
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
  - EP9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
- assessment_id: A4
  area: completeness
  topic: Native lifecycle, optional content and mechanism limits
  outcome: supported
  summary: Executed native routes reproduce EXACT/SEEDED. Required content is present.
    No optional environmental parameters, causal graph, discussion, dataset or characteristic-presence
    claim is fabricated. Missing ITEM status alone is not a defect; no status or history
    promotion is performed.
  target_ids:
  - BTO:0001709
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native validation and reproducibility
  outcome: supported
  summary: '31 baseline commands passed: target schema, cohort strict, 831 histories,
    source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term
    requests and configured labels. Exact-base hosted QC passed. Deterministic validity
    is not scientific approval.'
  target_ids:
  - BTO:0001709
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
findings: []
actions: []
limitations:
- Original specimen-level evidence and every pair-level citation were not exhaustively
  reconstructed. Source associations, counts, ranks and scores are not prevalence,
  viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs; target TaxIds were separately
  resolved with current NCBI.
- Exact-base hosted QC covers unchanged scientific inputs, not a new local full-QC
  execution or these new review files. Each new bundle requires native validation/save
  and the subsequent archive check.
- 'iModulonDB is not applicable: no gene, regulator or expression-module claim is
  asserted. Cited experiments are used only for identity and context, not imported
  causal mechanisms.'
- Original source-strain or PREGO pair exports were unavailable in the configured
  checkout; no uncertain association is removed or source count rewritten.
- Selected primary full text was unavailable (EPMC HTTP500; PMC browser challenge);
  inspected abstracts and available authorities are explicitly distinguished from
  full methods.
notes:
- Captured working_tree provenance is retained. All local input hashes were additionally
  checked against exact base 67cde35918d7361de3a1164fb22756cba5d20e30.
- 'Read-only review: no source, curation, generated record, status or history edit;
  no GitHub mutation or paid research.'
- Ignored-inclusive structured archive traversal found no previous structured target
  review. Legacy prose is contextual evidence, not formal predecessor lineage or issue
  closure.
tags:
- individual-scientific-review
- host-associated
```
