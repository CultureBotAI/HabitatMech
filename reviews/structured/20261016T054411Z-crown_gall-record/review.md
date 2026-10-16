# Record review: crown gall (BTO:0000303)

- Review: 20261016T054411Z-crown_gall-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T05:14:53Z
- Finished UTC: 2026-10-16T05:44:11Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BTO crown gall is labeled for a gall but defined as a disease while inheriting plant tumor tissue, conflating condition and lesion/material. Primary evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii. Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three associations while recovering original pair provenance; neither a disease definition nor rhizosphere context establishes gall-tissue localization for every taxon.

## Scope And Provenance

Full field-by-field assessment of this one resolved generated target.

Selection: One of the next 24 unreviewed targets in deterministic path order from the ignored-inclusive 3209-record census. This bundle is not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 13cddc722250dcad4327e5f9fad0a12fe7c08268.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000303 | data/habitats/host_associated/crown_gall.yaml | generated | crown gall |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000303 | Finished 2026-10-16T05:17:02Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/crown_gall.yaml |
| validate-strict | passed | True | BTO:0000303 | Finished 2026-10-16T05:17:09Z. uv run python scripts/validate_strict.py data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000303 | Finished 2026-10-16T05:17:16Z. No issues found<br>834 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000303 | Finished 2026-10-16T05:17:16Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000303 | Finished 2026-10-16T05:17:32Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000303 | Finished 2026-10-16T05:17:36Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000303 | Finished 2026-10-16T05:17:53Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000303 | Finished 2026-10-16T05:18:37Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted native QC | passed | True | BTO:0000303 | Verified 2026-10-16T05:19:04Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38852350960 |
| Candidate-pool correspondence | passed | False | BTO:0000303 | Finished 2026-10-16T05:42:35Z. All 67 displayed candidate pools equal exact source taxon totals. |
| Standalone citation validation applicability | not_applicable | False | BTO:0000303 | No standalone citation validator is documented for these generated targets without evidence objects. Current authorities verify stable references; full-corpus causal validation ran. |

## Scientific And Domain Assessments

### Identity, grounding, aliases and strict hierarchy

identity: concern. Targets: BTO:0000303.

BTO crown gall is labeled for a gall but defined as a disease while inheriting plant tumor tissue, conflating condition and lesion/material. Primary evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii. Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three associations while recovering original pair provenance; neither a disease definition nor rhizosphere context establishes gall-tissue localization for every taxon.

### Counts, units, taxon ranks, scores and candidate pools

quantity: supported. Targets: BTO:0000303.

Exact source rows reproduce emitted counts/units and displayed ranks/scores/pools. Zero tree counts are omitted; supplemental biosamples, study memberships and triads are nonadditive. {"assertions": [{"source": "PREGO", "count": 5, "unit": "TAXON", "row": {"row": 386, "data": {"prego_id": "BTO:0000303", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "5", "direct_assertion_count": "5", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "crown gall&#124;crown gallic&#124;crown galls"}}}], "taxa": [{"id": "NCBITaxon:1281779", "source": "PREGO", "label": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "current_id": "1281779", "current_name": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "rank": "strain", "direct_match": true, "recognized_alias": true, "source_row": {"row": 459, "data": {"prego_id": "BTO:0000303", "rank": "1", "taxon_id": "NCBITaxon:1281779", "taxon_label": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}, {"id": "NCBITaxon:1368418", "source": "PREGO", "label": "Rhizobium nepotum 39/7", "current_id": "1368418", "current_name": "Rhizobium nepotum 39/7", "rank": "strain", "direct_match": true, "recognized_alias": true, "source_row": {"row": 460, "data": {"prego_id": "BTO:0000303", "rank": "2", "taxon_id": "NCBITaxon:1368418", "taxon_label": "Rhizobium nepotum 39/7", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}, {"id": "NCBITaxon:1585697", "source": "PREGO", "label": "Agrobacterium arsenijevicii", "current_id": "1585697", "current_name": "Agrobacterium arsenijevicii", "rank": "species", "direct_match": true, "recognized_alias": true, "source_row": {"row": 461, "data": {"prego_id": "BTO:0000303", "rank": "3", "taxon_id": "NCBITaxon:1585697", "taxon_label": "Agrobacterium arsenijevicii", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}, {"id": "NCBITaxon:358", "source": "PREGO", "label": "Agrobacterium tumefaciens", "current_id": "358", "current_name": "Agrobacterium tumefaciens", "rank": "species", "direct_match": true, "recognized_alias": true, "source_row": {"row": 462, "data": {"prego_id": "BTO:0000303", "rank": "4", "taxon_id": "NCBITaxon:358", "taxon_label": "Agrobacterium tumefaciens", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}, {"id": "NCBITaxon:555793", "source": "PREGO", "label": "Novosphingobium sp. Rr 2-17", "current_id": "555793", "current_name": "Novosphingobium sp. Rr 2-17", "rank": "species", "direct_match": true, "recognized_alias": true, "source_row": {"row": 463, "data": {"prego_id": "BTO:0000303", "rank": "5", "taxon_id": "NCBITaxon:555793", "taxon_label": "Novosphingobium sp. Rr 2-17", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}]}

### Association support and source limits

evidence: concern. Targets: BTO:0000303.

BTO crown gall is labeled for a gall but defined as a disease while inheriting plant tumor tissue, conflating condition and lesion/material. Primary evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii. Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three associations while recovering original pair provenance; neither a disease definition nor rhizosphere context establishes gall-tissue localization for every taxon. Each cited source supports only its stated scope; original source pairs were not exhaustively reconstructed.

### Native lifecycle and optional content

completeness: supported. Targets: BTO:0000303.

Executed routes reproduce EXACT/SEEDED. Required fields are present; absent optional parameters, causal graphs, discussions and datasets are not fabricated. No scientific status promotion follows from this review.

### Native gates and exact reproduction

schema: supported. Targets: BTO:0000303.

31 baseline commands passed: individual schemas, 24-target strict validation, 834 histories, provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured labels. Exact-base hosted QC passed; deterministic validity is not scientific approval.

## Findings

### F1: Disease definition conflicts with tissue superclass

major / open / confirmed; issue key: crown-gall-disease-tissue-definition.

BTO crown gall is labeled for a gall but defined as a disease while inheriting plant tumor tissue, conflating condition and lesion/material. Primary evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii. Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three associations while recovering original pair provenance; neither a disease definition nor rhizosphere context establishes gall-tissue localization for every taxon. Resolve lesion/material versus disease representation upstream and refresh under provenance controls, or separately design a guarded definition correction. Do not simply delete the habitat or redefine it from one clinical phrase.

### F2: Original pair provenance is needed before interpreting localization

major / open / provisional; issue key: crown-gall-prego-pair-evidence.

BTO crown gall is labeled for a gall but defined as a disease while inheriting plant tumor tissue, conflating condition and lesion/material. Primary evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii. Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three associations while recovering original pair provenance; neither a disease definition nor rhizosphere context establishes gall-tissue localization for every taxon. Recover manifest-matching original pair, channel, citation and dictionary evidence before any selective correction. Inspected origins conflict with a simple localization reading but do not prove absence or the extraction cause.

## Recommended Actions And Acceptance Checks

### ACT1

BTO crown gall is labeled for a gall but defined as a disease while inheriting plant tumor tissue, conflating condition and lesion/material. Primary evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii. Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three associations while recovering original pair provenance; neither a disease definition nor rhizosphere context establishes gall-tissue localization for every taxon. Resolve lesion/material versus disease representation upstream and refresh under provenance controls, or separately design a guarded definition correction. Do not simply delete the habitat or redefine it from one clinical phrase. Proposed work only; no repair or status promotion is performed by this review.

- Regress the exact target claim and preserve valid genera, identifiers, source counts/units and taxon associations. Recover original evidence before deleting a provisional pair; do not decrement frozen totals by hand.
- Record authorized curation history; require schema, strict, provenance, history, label, corpus, site and full QC gates.
- Save an immutable successor with the same issue key and exact predecessor finding identity.

### ACT2

BTO crown gall is labeled for a gall but defined as a disease while inheriting plant tumor tissue, conflating condition and lesion/material. Primary evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii. Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three associations while recovering original pair provenance; neither a disease definition nor rhizosphere context establishes gall-tissue localization for every taxon. Recover manifest-matching original pair, channel, citation and dictionary evidence before any selective correction. Inspected origins conflict with a simple localization reading but do not prove absence or the extraction cause. Proposed work only; no repair or status promotion is performed by this review.

- Regress the exact target claim and preserve valid genera, identifiers, source counts/units and taxon associations. Recover original evidence before deleting a provisional pair; do not decrement frozen totals by hand.
- Record authorized curation history; require schema, strict, provenance, history, label, corpus, site and full QC gates.
- Save an immutable successor with the same issue key and exact predecessor finding identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/crown_gall.yaml; Entire generated target YAML | supports | All fields, source attestations, displayed taxa, aliases and generated history read. |
| ERULE | docs/CURATION.md; Identity, strict parents and evidence scope | supports | All parent contributions must be strictly broader; source context, host, anatomy and diagnosis are distinct. Missing optional content or ITEM status alone is not a defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and native statuses | supports | Mapping contract compares source concept to record identifier; source-is-record omits the predicate. Native count units and status gates retained. |
| ESEED | src/habitatmech/seed.py; Executed source routes and target reproduction | supports | [{"mint": "habitatmech:PREGO.0f830e9ca4", "automatic": {"identifier": "BTO:0000303", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000303", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; PREGO source projections | supports | Compact per-habitat tables preserve associations but do not retain original pair citations/dictionary provenance. |
| ET5 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 459,460,461,462,463 | supports | [{"row": 459, "data": {"prego_id": "BTO:0000303", "rank": "1", "taxon_id": "NCBITaxon:1281779", "taxon_label": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 460, "data": {"prego_id": "BTO:0000303", "rank": "2", "taxon_id": "NCBITaxon:1368418", "taxon_label": "Rhizobium nepotum 39/7", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 461, "data": {"prego_id": "BTO:0000303", "rank": "3", "taxon_id": "NCBITaxon:1585697", "taxon_label": "Agrobacterium arsenijevicii", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 462, "data": {"prego_id": "BTO:0000303", "rank": "4", "taxon_id": "NCBITaxon:358", "taxon_label": "Agrobacterium tumefaciens", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}, {"row": 463, "data": {"prego_id": "BTO:0000303", "rank": "5", "taxon_id": "NCBITaxon:555793", "taxon_label": "Novosphingobium sp. Rr 2-17", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET6 | data/raw/prego_habitats.tsv; Physical TSV rows 386 | supports | [{"row": 386, "data": {"prego_id": "BTO:0000303", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "5", "direct_assertion_count": "5", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "crown gall&#124;crown gallic&#124;crown galls"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 206 | supports | [{"row": 206, "data": {"subject": "BTO:0000303", "predicate": "rdfs:subClassOf", "object": "BTO:0000677"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 305,678 | supports | [{"row": 305, "data": {"term_id": "BTO:0000303", "ontology": "BTO", "label": "crown gall", "definition": "A disease that affects many species of plants and is caused by a bacterium (Agrobacterium tumefaciens) which forms tumorous enlargements just below the ground on the stem.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 678, "data": {"term_id": "BTO:0000677", "ontology": "BTO", "label": "plant tumor tissue", "definition": "", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| EX9 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&amp;id=APCC01000001.1&amp;rettype=gb&amp;retmode=xml&amp;seq_start=1&amp;seq_stop=1; APCC01000001.xml | context_only | GenBank source feature inspected: Cherry2E-2-2, taxon1281779, rhizosphere soil of infected cherry rootstock, linked PMID23723402. The exact accession links the record strain to the published source context. |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000303/graph; BTO_0000303-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000303", "target": "http://purl.obolibrary.org/obo/BTO_0000677", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000303; BTO_0000303.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "BTO:0000303", "label": "crown gall", "is_obsolete": false, "description": ["A disease that affects many species of plants and is caused by a bacterium (Agrobacterium tumefaciens) which forms tumorous enlargements just below the ground on the stem."], "obo_synonym": null} |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000677/graph; BTO_0000677-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000677", "target": "http://purl.obolibrary.org/obo/BTO_0001461", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}] |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000677; BTO_0000677.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "BTO:0000677", "label": "plant tumor tissue", "is_obsolete": false, "description": [], "obo_synonym": null} |
| EX14 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3668010/fullTextXML; PMC3668010.xml | context_only | PMID:23723402; DOI:10.1128/genomeA.00302-13. Genome announcement and source paragraph inspected: UHFBA218 from rhizosphere soil of crown-gall-infected cherry rootstock; project APCC01000000. Not direct gall-tissue isolation. |
| EX15 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | PMID:35208748; DOI:10.3390/microorganisms10020293. Inspected methods and scoring appendix: heterogeneous channels, BioProject abstract mining and capped association scores; this is not provenance for a specific retained pair. |
| EX16 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A26117193%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=20; paper-arsenijevicii.json | context_only | Primary abstract PMID:26117193; DOI:10.1016/j.syapm.2015.06.001 describes gall-derived A. arsenijevicii strains. Species-level context does not localize every other taxon in this record. |
| EX17 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22933764%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; paper-rr217.json | context_only | Primary abstract PMID:22933764; DOI:10.1128/JB.01159-12 explicitly identifies Rr2-17 from grapevine crown-gall tumor. Full-text XML returned HTTP500; no full-text claim. |
| EX18 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=104267,1107,1125980,1129,1154585,118,1234,1236,1268,1281779,1283,1346330,135613,135616,135619,135622,1368418,13687,1386,1400868,1405296,142182,1427368,1427369,1427370,1427371,1585697,1655514,174951,1860,186650,1869227,1883,2,20,200644,200666,200795,203557,203682,203683,203693,2037,204432,2062,213465,219685,233189,235572,237,245186,246874,2691357,28211,28216,2830,287,29,358,555793,813,86105&amp;retmode=xml; taxonomy.xml | context_only | Current exact TaxId resolutions and labels: [{"id": "NCBITaxon:1281779", "source": "PREGO", "label": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "current_id": "1281779", "current_name": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1368418", "source": "PREGO", "label": "Rhizobium nepotum 39/7", "current_id": "1368418", "current_name": "Rhizobium nepotum 39/7", "rank": "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1585697", "source": "PREGO", "label": "Agrobacterium arsenijevicii", "current_id": "1585697", "current_name": "Agrobacterium arsenijevicii", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:358", "source": "PREGO", "label": "Agrobacterium tumefaciens", "current_id": "358", "current_name": "Agrobacterium tumefaciens", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:555793", "source": "PREGO", "label": "Novosphingobium sp. Rr 2-17", "current_id": "555793", "current_name": "Novosphingobium sp. Rr 2-17", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Local source and review corpus; rg --no-ignore --hidden -l -F -e BTO:0000303 -e 'crown gall' -e crown_gall -e habitatmech:PREGO.0f830e9ca4 curation history research reports data/raw build reviews | context_only | Exact source keys and structured archive parsed independently; broad name hits are leads, not all inspected. No formal target predecessor. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -ipath '*prego*' | context_only | No PREGO-named files found in the configured checkout. This is not a claim of global source absence. |

## Limits And Additional Notes

- Original specimen-level evidence and all pair-level citations were not exhaustively reconstructed. Native association counts, taxon ranks and scores do not establish prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs. Exact target TaxIds were separately resolved; frozen taxon labels are not universally current.
- Exact-base hosted QC covers unchanged scientific inputs, not a fresh local full-QC execution or these new review outputs. Native validate/save and subsequent archive/final-head gates are separate.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. No new causal mechanism is imported.
- Original PREGO pair exports were unavailable in the configured checkout. No uncertain association or source total is changed by this review.
- Selected genome full text returned EPMC HTTP500. Cited primary abstracts are distinguished from full text; the connective-tissue challenge abstracts and gall-isolate abstract do not certify every original PREGO pair.
- All captured local input hashes were independently checked against exact base 13cddc722250dcad4327e5f9fad0a12fe7c08268.
- This baseline observation changes no scientific input. Separately authorized PR remediation follows; no status promotion is conferred by review validation.
- Ignored-inclusive structured archive traversal found no formal previous target review. Legacy reports are context, not predecessor lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T054411Z-crown_gall-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: crown gall (BTO:0000303)'
started_at: '2026-10-16T05:14:53Z'
finished_at: '2026-10-16T05:44:11Z'
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
summary: BTO crown gall is labeled for a gall but defined as a disease while inheriting
  plant tumor tissue, conflating condition and lesion/material. Primary evidence supports
  Rr2-17 from a gall tumor and gall origins for A. arsenijevicii. Exact Cherry2E-2-2
  GenBank source metadata instead records rhizosphere soil of an infected rootstock
  and links the UHFBA218 genome paper. Preserve all five score-three associations
  while recovering original pair provenance; neither a disease definition nor rhizosphere
  context establishes gall-tissue localization for every taxon.
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
  - path: data/habitats/host_associated/crown_gall.yaml
    sha256: 88c59fbde3dd972d9977d8e94b081d7e459ada79980c8e35c632b46603e5b6dd
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
- target_id: BTO:0000303
  path: data/habitats/host_associated/crown_gall.yaml
  label: crown gall
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
  - BTO:0000303
  exclusions:
  - target: Other records, original specimens and SSSOM/KGX products
    reason: Parents are contextual evidence, not additional review coverage; original
      specimens and exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/crown_gall.yaml
  exit_code: 0
  target_ids:
  - BTO:0000303
  summary: "Finished 2026-10-16T05:17:02Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/crown_gall.yaml"
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
  - BTO:0000303
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
  - BTO:0000303
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
  - BTO:0000303
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
  - BTO:0000303
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
  - BTO:0000303
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
  - BTO:0000303
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
  - BTO:0000303
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
  - BTO:0000303
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
  - BTO:0000303
  summary: Finished 2026-10-16T05:42:35Z. All 67 displayed candidate pools equal exact
    source taxon totals.
  scope_note: Supplemental exact source-total check, not a replacement for native
    validators or scientific evidence.
- check_id: CREF
  name: Standalone citation validation applicability
  status: not_applicable
  required: false
  target_ids:
  - BTO:0000303
  summary: No standalone citation validator is documented for these generated targets
    without evidence objects. Current authorities verify stable references; full-corpus
    causal validation ran.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/crown_gall.yaml
  locator: Entire generated target YAML
  accessed_at: '2026-10-16T05:44:10Z'
  support: supports
  summary: All fields, source attestations, displayed taxa, aliases and generated
    history read.
  snapshot_sha256: 88c59fbde3dd972d9977d8e94b081d7e459ada79980c8e35c632b46603e5b6dd
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, strict parents and evidence scope
  accessed_at: '2026-10-16T05:44:10Z'
  support: supports
  summary: All parent contributions must be strictly broader; source context, host,
    anatomy and diagnosis are distinct. Missing optional content or ITEM status alone
    is not a defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and native statuses
  accessed_at: '2026-10-16T05:44:10Z'
  support: supports
  summary: Mapping contract compares source concept to record identifier; source-is-record
    omits the predicate. Native count units and status gates retained.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source routes and target reproduction
  accessed_at: '2026-10-16T05:44:10Z'
  support: supports
  summary: '[{"mint": "habitatmech:PREGO.0f830e9ca4", "automatic": {"identifier":
    "BTO:0000303", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "BTO:0000303", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded",
    "category": null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: PREGO source projections
  accessed_at: '2026-10-16T05:44:10Z'
  support: supports
  summary: Compact per-habitat tables preserve associations but do not retain original
    pair citations/dictionary provenance.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 459,460,461,462,463
  accessed_at: '2026-10-16T05:44:10Z'
  support: supports
  summary: '[{"row": 459, "data": {"prego_id": "BTO:0000303", "rank": "1", "taxon_id":
    "NCBITaxon:1281779", "taxon_label": "Agrobacterium tumefaciens str. Cherry 2E-2-2",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 460, "data": {"prego_id": "BTO:0000303", "rank":
    "2", "taxon_id": "NCBITaxon:1368418", "taxon_label": "Rhizobium nepotum 39/7",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 461, "data": {"prego_id": "BTO:0000303", "rank":
    "3", "taxon_id": "NCBITaxon:1585697", "taxon_label": "Agrobacterium arsenijevicii",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 462, "data": {"prego_id": "BTO:0000303", "rank":
    "4", "taxon_id": "NCBITaxon:358", "taxon_label": "Agrobacterium tumefaciens",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}, {"row": 463, "data": {"prego_id": "BTO:0000303", "rank":
    "5", "taxon_id": "NCBITaxon:555793", "taxon_label": "Novosphingobium sp. Rr 2-17",
    "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 386
  accessed_at: '2026-10-16T05:44:10Z'
  support: supports
  summary: '[{"row": 386, "data": {"prego_id": "BTO:0000303", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "5", "direct_assertion_count":
    "5", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "crown gall|crown gallic|crown galls"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 206
  accessed_at: '2026-10-16T05:44:10Z'
  support: supports
  summary: '[{"row": 206, "data": {"subject": "BTO:0000303", "predicate": "rdfs:subClassOf",
    "object": "BTO:0000677"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 305,678
  accessed_at: '2026-10-16T05:44:10Z'
  support: supports
  summary: '[{"row": 305, "data": {"term_id": "BTO:0000303", "ontology": "BTO", "label":
    "crown gall", "definition": "A disease that affects many species of plants and
    is caused by a bacterium (Agrobacterium tumefaciens) which forms tumorous enlargements
    just below the ground on the stem.", "synonyms": "", "deprecated": "", "directly_referenced":
    "TRUE", "label_only": "FALSE"}}, {"row": 678, "data": {"term_id": "BTO:0000677",
    "ontology": "BTO", "label": "plant tumor tissue", "definition": "", "synonyms":
    "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EX9
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=APCC01000001.1&rettype=gb&retmode=xml&seq_start=1&seq_stop=1
  locator: APCC01000001.xml
  accessed_at: '2026-10-16T05:22:17Z'
  support: context_only
  summary: 'GenBank source feature inspected: Cherry2E-2-2, taxon1281779, rhizosphere
    soil of infected cherry rootstock, linked PMID23723402. The exact accession links
    the record strain to the published source context.'
  snapshot_sha256: 618ae8cf3193e9b91adf54a20e948d2f955d635d4beff9b4d296182d07970ba9
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000303/graph
  locator: BTO_0000303-graph.json
  accessed_at: '2026-10-16T05:15:27Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000303",
    "target": "http://purl.obolibrary.org/obo/BTO_0000677", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: db016cf5f9b44e53291d08ace3c8196a5d48844c1582cb6744d60942b4f8064d
- evidence_id: EX11
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000303
  locator: BTO_0000303.json
  accessed_at: '2026-10-16T05:15:26Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "BTO:0000303", "label": "crown gall", "is_obsolete": false, "description": ["A
    disease that affects many species of plants and is caused by a bacterium (Agrobacterium
    tumefaciens) which forms tumorous enlargements just below the ground on the stem."],
    "obo_synonym": null}'
  snapshot_sha256: d7e2bca7c9e09fc6f47c78bd962e17b86e3fa470e4358f15b6252590cd14879d
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000677/graph
  locator: BTO_0000677-graph.json
  accessed_at: '2026-10-16T05:15:30Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000677",
    "target": "http://purl.obolibrary.org/obo/BTO_0001461", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}]'
  snapshot_sha256: bd43e07a8491b38a3670b72dcb6ad09f203ed807bfed90b06169aa61c557f12d
- evidence_id: EX13
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000677
  locator: BTO_0000677.json
  accessed_at: '2026-10-16T05:15:30Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "BTO:0000677", "label": "plant tumor tissue", "is_obsolete": false, "description":
    [], "obo_synonym": null}'
  snapshot_sha256: 81fa721773a1693532fa1d258e69555c75eb5db518bca3be936086774e3264eb
- evidence_id: EX14
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3668010/fullTextXML
  locator: PMC3668010.xml
  accessed_at: '2026-10-16T05:22:07Z'
  support: context_only
  summary: 'PMID:23723402; DOI:10.1128/genomeA.00302-13. Genome announcement and source
    paragraph inspected: UHFBA218 from rhizosphere soil of crown-gall-infected cherry
    rootstock; project APCC01000000. Not direct gall-tissue isolation.'
  snapshot_sha256: 0a3529a36e9a4c8f69b9a217032e52f55b68bf973e1fe002cbb87e1ae286b94f
- evidence_id: EX15
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-16T05:18:44Z'
  support: context_only
  summary: 'PMID:35208748; DOI:10.3390/microorganisms10020293. Inspected methods and
    scoring appendix: heterogeneous channels, BioProject abstract mining and capped
    association scores; this is not provenance for a specific retained pair.'
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX16
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A26117193%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=20
  locator: paper-arsenijevicii.json
  accessed_at: '2026-10-16T05:19:06Z'
  support: context_only
  summary: Primary abstract PMID:26117193; DOI:10.1016/j.syapm.2015.06.001 describes
    gall-derived A. arsenijevicii strains. Species-level context does not localize
    every other taxon in this record.
  snapshot_sha256: d0b46fc04c16a40a3c633cc01ae1de457f412a0707e37383fa5fa990aec3ab24
- evidence_id: EX17
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22933764%20AND%20SRC%3AMED&format=json&resultType=core
  locator: paper-rr217.json
  accessed_at: '2026-10-16T05:22:14Z'
  support: context_only
  summary: Primary abstract PMID:22933764; DOI:10.1128/JB.01159-12 explicitly identifies
    Rr2-17 from grapevine crown-gall tumor. Full-text XML returned HTTP500; no full-text
    claim.
  snapshot_sha256: 05f3584a78e01d40112dac38adbe8cff01f4b6e0089a4fd6eb6f2580863b8f2e
- evidence_id: EX18
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=104267,1107,1125980,1129,1154585,118,1234,1236,1268,1281779,1283,1346330,135613,135616,135619,135622,1368418,13687,1386,1400868,1405296,142182,1427368,1427369,1427370,1427371,1585697,1655514,174951,1860,186650,1869227,1883,2,20,200644,200666,200795,203557,203682,203683,203693,2037,204432,2062,213465,219685,233189,235572,237,245186,246874,2691357,28211,28216,2830,287,29,358,555793,813,86105&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-16T05:16:21Z'
  support: context_only
  summary: 'Current exact TaxId resolutions and labels: [{"id": "NCBITaxon:1281779",
    "source": "PREGO", "label": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "current_id":
    "1281779", "current_name": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "rank":
    "strain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1368418",
    "source": "PREGO", "label": "Rhizobium nepotum 39/7", "current_id": "1368418",
    "current_name": "Rhizobium nepotum 39/7", "rank": "strain", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:1585697", "source": "PREGO", "label":
    "Agrobacterium arsenijevicii", "current_id": "1585697", "current_name": "Agrobacterium
    arsenijevicii", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:358", "source": "PREGO", "label": "Agrobacterium tumefaciens",
    "current_id": "358", "current_name": "Agrobacterium tumefaciens", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:555793", "source":
    "PREGO", "label": "Novosphingobium sp. Rr 2-17", "current_id": "555793", "current_name":
    "Novosphingobium sp. Rr 2-17", "rank": "species", "direct_match": true, "recognized_alias":
    true}]'
  snapshot_sha256: c87693dd48667514d7e3c5fdf2b1d629f2c9c10b8749bf4e88cdc26a65349549
- evidence_id: ESEARCH
  kind: search
  reference: Local source and review corpus
  locator: rg --no-ignore --hidden -l -F -e BTO:0000303 -e 'crown gall' -e crown_gall
    -e habitatmech:PREGO.0f830e9ca4 curation history research reports data/raw build
    reviews
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
  outcome: concern
  summary: BTO crown gall is labeled for a gall but defined as a disease while inheriting
    plant tumor tissue, conflating condition and lesion/material. Primary evidence
    supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii. Exact
    Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of an infected
    rootstock and links the UHFBA218 genome paper. Preserve all five score-three associations
    while recovering original pair provenance; neither a disease definition nor rhizosphere
    context establishes gall-tissue localization for every taxon.
  target_ids:
  - BTO:0000303
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
  - EX9
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
  topic: Counts, units, taxon ranks, scores and candidate pools
  outcome: supported
  summary: 'Exact source rows reproduce emitted counts/units and displayed ranks/scores/pools.
    Zero tree counts are omitted; supplemental biosamples, study memberships and triads
    are nonadditive. {"assertions": [{"source": "PREGO", "count": 5, "unit": "TAXON",
    "row": {"row": 386, "data": {"prego_id": "BTO:0000303", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "5", "direct_assertion_count":
    "5", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "crown gall|crown gallic|crown galls"}}}], "taxa": [{"id": "NCBITaxon:1281779",
    "source": "PREGO", "label": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "current_id":
    "1281779", "current_name": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "rank":
    "strain", "direct_match": true, "recognized_alias": true, "source_row": {"row":
    459, "data": {"prego_id": "BTO:0000303", "rank": "1", "taxon_id": "NCBITaxon:1281779",
    "taxon_label": "Agrobacterium tumefaciens str. Cherry 2E-2-2", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:1368418", "source": "PREGO", "label": "Rhizobium nepotum
    39/7", "current_id": "1368418", "current_name": "Rhizobium nepotum 39/7", "rank":
    "strain", "direct_match": true, "recognized_alias": true, "source_row": {"row":
    460, "data": {"prego_id": "BTO:0000303", "rank": "2", "taxon_id": "NCBITaxon:1368418",
    "taxon_label": "Rhizobium nepotum 39/7", "prego_score": "3", "direct_flag": "TRUE",
    "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}, {"id": "NCBITaxon:1585697",
    "source": "PREGO", "label": "Agrobacterium arsenijevicii", "current_id": "1585697",
    "current_name": "Agrobacterium arsenijevicii", "rank": "species", "direct_match":
    true, "recognized_alias": true, "source_row": {"row": 461, "data": {"prego_id":
    "BTO:0000303", "rank": "3", "taxon_id": "NCBITaxon:1585697", "taxon_label": "Agrobacterium
    arsenijevicii", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates",
    "corroborated_by": ""}}}, {"id": "NCBITaxon:358", "source": "PREGO", "label":
    "Agrobacterium tumefaciens", "current_id": "358", "current_name": "Agrobacterium
    tumefaciens", "rank": "species", "direct_match": true, "recognized_alias": true,
    "source_row": {"row": 462, "data": {"prego_id": "BTO:0000303", "rank": "4", "taxon_id":
    "NCBITaxon:358", "taxon_label": "Agrobacterium tumefaciens", "prego_score": "3",
    "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}}, {"id": "NCBITaxon:555793", "source": "PREGO", "label": "Novosphingobium
    sp. Rr 2-17", "current_id": "555793", "current_name": "Novosphingobium sp. Rr
    2-17", "rank": "species", "direct_match": true, "recognized_alias": true, "source_row":
    {"row": 463, "data": {"prego_id": "BTO:0000303", "rank": "5", "taxon_id": "NCBITaxon:555793",
    "taxon_label": "Novosphingobium sp. Rr 2-17", "prego_score": "3", "direct_flag":
    "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}}]}'
  target_ids:
  - BTO:0000303
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
  - EX9
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
  topic: Association support and source limits
  outcome: concern
  summary: BTO crown gall is labeled for a gall but defined as a disease while inheriting
    plant tumor tissue, conflating condition and lesion/material. Primary evidence
    supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii. Exact
    Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of an infected
    rootstock and links the UHFBA218 genome paper. Preserve all five score-three associations
    while recovering original pair provenance; neither a disease definition nor rhizosphere
    context establishes gall-tissue localization for every taxon. Each cited source
    supports only its stated scope; original source pairs were not exhaustively reconstructed.
  target_ids:
  - BTO:0000303
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
  - EX9
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
  topic: Native lifecycle and optional content
  outcome: supported
  summary: Executed routes reproduce EXACT/SEEDED. Required fields are present; absent
    optional parameters, causal graphs, discussions and datasets are not fabricated.
    No scientific status promotion follows from this review.
  target_ids:
  - BTO:0000303
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
  - BTO:0000303
  evidence_ids:
  - E1
  - ESCHEMA
  - ERULE
findings:
- finding_id: F1
  issue_key: crown-gall-disease-tissue-definition
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Disease definition conflicts with tissue superclass
  description: BTO crown gall is labeled for a gall but defined as a disease while
    inheriting plant tumor tissue, conflating condition and lesion/material. Primary
    evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii.
    Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of
    an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three
    associations while recovering original pair provenance; neither a disease definition
    nor rhizosphere context establishes gall-tissue localization for every taxon.
    Resolve lesion/material versus disease representation upstream and refresh under
    provenance controls, or separately design a guarded definition correction. Do
    not simply delete the habitat or redefine it from one clinical phrase.
  target_ids:
  - BTO:0000303
  field_paths:
  - definition
  - parent_habitats
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
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: crown-gall-prego-pair-evidence
  category: evidence
  severity: major
  status: open
  certainty: provisional
  title: Original pair provenance is needed before interpreting localization
  description: BTO crown gall is labeled for a gall but defined as a disease while
    inheriting plant tumor tissue, conflating condition and lesion/material. Primary
    evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii.
    Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of
    an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three
    associations while recovering original pair provenance; neither a disease definition
    nor rhizosphere context establishes gall-tissue localization for every taxon.
    Recover manifest-matching original pair, channel, citation and dictionary evidence
    before any selective correction. Inspected origins conflict with a simple localization
    reading but do not prove absence or the extraction cause.
  target_ids:
  - BTO:0000303
  field_paths:
  - characteristic_taxa
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
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
  - EAVAIL
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0000303
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  description: BTO crown gall is labeled for a gall but defined as a disease while
    inheriting plant tumor tissue, conflating condition and lesion/material. Primary
    evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii.
    Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of
    an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three
    associations while recovering original pair provenance; neither a disease definition
    nor rhizosphere context establishes gall-tissue localization for every taxon.
    Resolve lesion/material versus disease representation upstream and refresh under
    provenance controls, or separately design a guarded definition correction. Do
    not simply delete the habitat or redefine it from one clinical phrase. Proposed
    work only; no repair or status promotion is performed by this review.
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
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - BTO:0000303
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/MANIFEST.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  description: BTO crown gall is labeled for a gall but defined as a disease while
    inheriting plant tumor tissue, conflating condition and lesion/material. Primary
    evidence supports Rr2-17 from a gall tumor and gall origins for A. arsenijevicii.
    Exact Cherry2E-2-2 GenBank source metadata instead records rhizosphere soil of
    an infected rootstock and links the UHFBA218 genome paper. Preserve all five score-three
    associations while recovering original pair provenance; neither a disease definition
    nor rhizosphere context establishes gall-tissue localization for every taxon.
    Recover manifest-matching original pair, channel, citation and dictionary evidence
    before any selective correction. Inspected origins conflict with a simple localization
    reading but do not prove absence or the extraction cause. Proposed work only;
    no repair or status promotion is performed by this review.
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
- Original PREGO pair exports were unavailable in the configured checkout. No uncertain
  association or source total is changed by this review.
- Selected genome full text returned EPMC HTTP500. Cited primary abstracts are distinguished
  from full text; the connective-tissue challenge abstracts and gall-isolate abstract
  do not certify every original PREGO pair.
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
