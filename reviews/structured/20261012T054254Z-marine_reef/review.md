# Scientific record review: marine_reef

- Review: 20261012T054254Z-marine_reef
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-12T05:18:45.183669Z
- Finished UTC: 2026-10-12T05:42:54.839387Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The physical marine reef retains reef ancestry and location within marine water, rather than being a biome. Its PREGO pool of 112 and selected 25 associations match the reef-biome record, but shared observations do not prove identity or authorize merging. Taxon 158080 is a resolvable historical alias of 141390, not a broken reference.

## Scope And Provenance

Entire exact generated record, all contributors and individual asserted causal edges, with bounded source-context assessment.

Selection: Next forty records without a completed individual scientific review in stable repository-relative path order: marine anoxic zone through microbial_mats__200e1828. Full individual observations, not a category-wide pass. Prior coverage counts distinct observations, not a clean current-input corpus. Starting distinct-review coverage 688/3208 is not clean current-input coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ed9e0d0f382e4502a64f4de10102c4512bddca38.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:01000143 | data/habitats/aquatic/marine_reef.yaml | generated | marine reef |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native gate on captured inputs | passed | True | ENVO:01000143 | Actual success 2026-10-12T05:21:57.392635Z to 2026-10-12T05:22:01.423608Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:01000143 | Actual success 2026-10-12T05:23:16.222412Z to 2026-10-12T05:23:26.347203Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:01000143 | Actual success 2026-10-12T05:23:26.348469Z to 2026-10-12T05:23:51.098950Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:01000143 | Actual success 2026-10-12T05:23:51.100146Z to 2026-10-12T05:25:01.530644Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:01000143 | Actual success 2026-10-12T05:25:01.532072Z to 2026-10-12T05:25:11.808379Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:01000143 | Actual success 2026-10-12T05:25:11.809657Z to 2026-10-12T05:25:19.058687Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:01000143 | Actual success 2026-10-12T05:25:19.059693Z to 2026-10-12T05:25:46.351294Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:01000143 | Actual success 2026-10-12T05:25:46.352569Z to 2026-10-12T05:25:47.389752Z. Native command scope retained. |
| Exact-base CI authoritative QC | passed | True | ENVO:01000143 | Actual success 2026-10-12T05:21:53.294030Z to 2026-10-12T05:21:55.368917Z. All three required merge-group workflows passed at the exact captured base; authoritative QC passed 913 tests with 3 skipped. Newly saved review bundles require their own integrity check. These newly saved review bundles were not part of that earlier exact-base CI run. |
| Complete target reconstruction | passed | False | ENVO:01000143 | All 40 complete documents matched; captured hashes rechecked before authoring. |
| Original assertion membership | unavailable | False | ENVO:01000143 | Bounded ignored-inclusive searches did not recover complete original assertion inputs; later exports are contextual evidence only. |
| Expression-adapter applicability | not_applicable | False | ENVO:01000143 | The successful 28-dataset inventory was read for graph scope. No matching claim-specific organism/strain/gene or expression-module assertion requires a search or summarize call. Absence is not negative ecological evidence. |

## Scientific And Domain Assessments

### Exact identity, definition and source intent

identity: supported. Targets: ENVO:01000143.

The physical marine reef retains reef ancestry and location within marine water, rather than being a biome. Its PREGO pool of 112 and selected 25 associations match the reef-biome record, but shared observations do not prove identity or authorize merging. Taxon 158080 is a resolvable historical alias of 141390, not a broken reference.

### Parent contributors and mapping endpoints

grounding: supported. Targets: ENVO:01000143.

The physical marine reef retains reef ancestry and location within marine water, rather than being a biome. Its PREGO pool of 112 and selected 25 associations match the reef-biome record, but shared observations do not prove identity or authorize merging. Taxon 158080 is a resolvable historical alias of 141390, not a broken reference. Ontology, GOLD path, ambiguous-leaf and authored-genus routes were distinguished.

### Source units and native lifecycle

provenance: supported. Targets: ENVO:01000143.

Complete reconstruction preserves 1 contributing concepts and 0 ITEM-reviewed contributors. Attestations=[{"source": "PREGO", "source_id": "ENVO:01000143", "source_label": "marine reef", "assertion_count": 112, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "environmental_samples"}]. Counts with different units are not summed. Reproduction validates derivation, not the scientific truth of the mapping.

### Taxonomy and association scope

evidence: concern. Targets: ENVO:01000143.

All emitted identifiers resolve, including historical aliases. Source rows, ranks, scores and corroboration reproduce; these are selected associations, not proven characteristic taxa. Original occurrence evidence was not fully recovered, so no claim of exhaustive ecological validation is made. 158080 resolves to 141390 Chromohalobacter israelensis

### Optional slots and bounded evidence

completeness: supported. Targets: ENVO:01000143.

Optional empty fields alone are not defects. No causal graph is asserted in the exact captured record; ignored-inclusive support search and the full causal gate were checked. No record-level gene/regulator or transcriptomics claim warrants a component query.

## Findings

### F1: Historical taxonomy identifiers or names need versioned maintenance

minor / open / confirmed; issue key: envo-01000143-taxonomy-alias-maintenance.

158080 resolves to 141390 Chromohalobacter israelensis. The original IDs remain resolvable; this is not proof of a false habitat association.

## Recommended Actions And Acceptance Checks

### A1

Use versioned taxonomy normalization, preserving original IDs/names, ranks, scores, source pools and corroboration. Test alias deduplication rather than guessing a replacement organism.

- Change only maintained owners after source-level assessment; retain independent true parents, source identity/count/unit provenance and lifecycle unless a separately justified change requires otherwise.
- Append required current history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, label, provenance, corpus reproduction, causal/history and full QC gates; save a linked successor for any finding disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/aquatic/marine_reef.yaml; Entire captured YAML read, including all taxa, parameters, graphs and generated history | supports | The physical marine reef retains reef ancestry and location within marine water, rather than being a biome. Its PREGO pool of 112 and selected 25 associations match the reef-biome record, but shared observations do not prove identity or authorize merging. Taxon 158080 is a resolvable historical alias of 141390, not a broken reference. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied exact identity, strict-genus, MIxS roles, source-unit/score and ITEM lifecycle contracts; graph node types retain their biological definitions. |
| RAW | data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; Exact logical TSV rows, header=row1; filtered by current source IDs and exact paths, not legacy issue line numbers | supports | {"data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:01001899", "predicate": "rdfs:subClassOf", "subject": "ENVO:01000143"}, "logical_row": 5794}], "data/raw/ontology_terms.tsv": [{"data": {"definition": "A reef which is located in a marine water body.", "deprecated": "", "directly_referenced": "TRUE", "label": "marine reef", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id": "ENVO:01000143"}, "logical_row": 7643}], "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "1", "taxon_id": "NCBITaxon:102", "taxon_label": "Polaribacter glomeratus"}, "logical_row": 7747}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "2", "taxon_id": "NCBITaxon:1026", "taxon_label": "Marinoscillum furvescens"}, "logical_row": 7748}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "3", "taxon_id": "NCBITaxon:103810", "taxon_label": "Riemerella columbina"}, "logical_row": 7749}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "4", "taxon_id": "NCBITaxon:104268", "taxon_label": "Tenacibaculum mesophilum"}, "logical_row": 7750}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "5", "taxon_id": "NCBITaxon:104270", "taxon_label": "Tenacibaculum ovolyticum"}, "logical_row": 7751}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "6", "taxon_id": "NCBITaxon:1044", "taxon_label": "Erythrobacter longus"}, "logical_row": 7752}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "7", "taxon_id": "NCBITaxon:107401", "taxon_label": "Tenacibaculum maritimum"}, "logical_row": 7753}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "8", "taxon_id": "NCBITaxon:1080", "taxon_label": "Afifella marina"}, "logical_row": 7754}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "9", "taxon_id": "NCBITaxon:111770", "taxon_label": "Thiothrix fructosivorans"}, "logical_row": 7755}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "10", "taxon_id": "NCBITaxon:114404", "taxon_label": "Edaphosphingomonas fennica"}, "logical_row": 7756}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "11", "taxon_id": "NCBITaxon:119542", "taxon_label": "Roseinatronobacter bogoriensis"}, "logical_row": 7757}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "12", "taxon_id": "NCBITaxon:1217908", "taxon_label": "Octadecabacter antarcticus"}, "logical_row": 7758}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "13", "taxon_id": "NCBITaxon:133924", "taxon_label": "Leisingera methylohalidivorans"}, "logical_row": 7759}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "14", "taxon_id": "NCBITaxon:143224", "taxon_label": "Zobellia uliginosa"}, "logical_row": 7760}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "15", "taxon_id": "NCBITaxon:150120", "taxon_label": "Shewanella livingstonensis"}, "logical_row": 7761}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "16", "taxon_id": "NCBITaxon:158080", "taxon_label": ""}, "logical_row": 7762}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "17", "taxon_id": "NCBITaxon:161528", "taxon_label": "Erythrobacter sp. SD-21"}, "logical_row": 7763}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "18", "taxon_id": "NCBITaxon:168275", "taxon_label": "Psychromonas arctica"}, "logical_row": 7764}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "19", "taxon_id": "NCBITaxon:172371", "taxon_label": "Alloalcanivorax venustensis"}, "logical_row": 7765}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "20", "taxon_id": "NCBITaxon:173737", "taxon_label": "Cytophaga sp. MBIC04693"}, "logical_row": 7766}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "21", "taxon_id": "NCBITaxon:184914", "taxon_label": "Corallococcus coralloides"}, "logical_row": 7767}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "22", "taxon_id": "NCBITaxon:188906", "taxon_label": "Jannaschia helgolandensis"}, "logical_row": 7768}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "23", "taxon_id": "NCBITaxon:188908", "taxon_label": "Oleispira antarctica"}, "logical_row": 7769}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "24", "taxon_id": "NCBITaxon:197222", "taxon_label": "Paraglaciecola mesophila"}, "logical_row": 7770}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "25", "taxon_id": "NCBITaxon:200617", "taxon_label": "Rhodopseudomonas julia"}, "logical_row": 7771}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category": "biolink:OntologyClass", "channels": "environmental_samples", "direct_assertion_count": "112", "max_prego_score": "4", "ontology": "ENVO", "prego_id": "ENVO:01000143", "prego_synonyms": "marine reef&#124;marine reefs", "taxon_count": "112"}, "logical_row": 181}]} |
| CODE | src/habitatmech/seed.py; Executed complete-document reconstruction; all 40 matched; routes distinguish source mints and generated identity | supports | {"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:01000143", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:01000143", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.b465e3c8a7", "source": "PREGO", "source_id": "ENVO:01000143"}], "source_concepts": 1} |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Official OWL retrieved 12-Oct; labels, definitions, typed synonyms, named parents and restrictions; no snapshot refresh | supports | {"ENVO:01000143": {"definitions": ["A reef which is located in a marine water body."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_01001899"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0001025"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00001999"]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["marine reef"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01001899", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0001025"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00001999"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:01001899": {"definitions": [], "deprecated": [], "equivalents": [], "labels": ["reef"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000012"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}} |
| PARENT | data/raw/ontology_terms.tsv; Ancestor context adds no full-record coverage | supports | {} |
| TAX0 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1000566%2C1003110%2C1005925%2C1005926%2C1005928%2C1006%2C1007105%2C1007109%2C1007110%2C1007111%2C1007112%2C1007113%2C1007114%2C1007115%2C1007116%2C1007117%2C1007118%2C1007119%2C1007120%2C1007122%2C1007124%2C1009412%2C1009413%2C1009414%2C1009415%2C1009416%2C1009418%2C1009419%2C1009420%2C1009421%2C1017277%2C102%2C1026%2C1027373%2C1027374%2C1028566%2C1028742%2C1028743%2C1028745%2C1028746%2C1028749%2C1028752%2C1031273%2C1031541%2C103810%2C1038845%2C1038928%2C1038929%2C1042%2C104268%2C104270%2C1042877%2C1044%2C104421%2C1045558%2C1048%2C1048221%2C1057%2C106299%2C1074%2C107401%2C1080%2C1089550%2C109263%2C1094980%2C110163%2C1104565%2C1104566%2C110662%2C110663%2C111770%2C1121404%2C1121937%2C1121948%2C1122607%2C1123059%2C1123242%2C1123275%2C114404%2C1150474%2C119394%2C119542%2C1208324%2C1211807%2C121224%2C1217908%2C1219067%2C1242148%2C1246444%2C1246460%2C1265%2C126741%2C1267768%2C1267769%2C1276246%2C1282%2C129958%2C132144%2C133924%2C134561%2C1358%2C13616%2C13686%2C1371%2C1387275%2C139239%2C1394%2C1411902%2C143223%2C143224%2C147%2C1486246%2C150120%2C1543721%2C156%2C156128%2C156133%2C1570%2C158080%2C158192%2C158500%2C1609977%2C161528%2C163248%2C163503%2C168275%2C168759%2C1703256%2C1716143%2C172371%2C173%2C173365%2C173737%2C173764%2C174%2C174302%2C174315%2C1774373%2C179326%2C180542%2C1808508%2C1808945%2C1817405%2C1836499%2C184592%2C184914%2C1855%2C186022%2C1869227%2C1871328&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The three chunks jointly resolve all 346 requested cohort IDs. Target results=[{"current_id": "102", "current_name": "Polaribacter glomeratus", "frozen_label": "Polaribacter glomeratus", "id": "102", "rank": "species"}, {"current_id": "1026", "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum furvescens", "id": "1026", "rank": "species"}, {"current_id": "103810", "current_name": "Riemerella columbina", "frozen_label": "Riemerella columbina", "id": "103810", "rank": "species"}, {"current_id": "104268", "current_name": "Tenacibaculum mesophilum", "frozen_label": "Tenacibaculum mesophilum", "id": "104268", "rank": "species"}, {"current_id": "104270", "current_name": "Tenacibaculum ovolyticum", "frozen_label": "Tenacibaculum ovolyticum", "id": "104270", "rank": "species"}, {"current_id": "1044", "current_name": "Erythrobacter longus", "frozen_label": "Erythrobacter longus", "id": "1044", "rank": "species"}, {"current_id": "107401", "current_name": "Tenacibaculum maritimum", "frozen_label": "Tenacibaculum maritimum", "id": "107401", "rank": "species"}, {"current_id": "1080", "current_name": "Afifella marina", "frozen_label": "Afifella marina", "id": "1080", "rank": "species"}, {"current_id": "111770", "current_name": "Thiothrix fructosivorans", "frozen_label": "Thiothrix fructosivorans", "id": "111770", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank": "species"}, {"current_id": "119542", "current_name": "Roseinatronobacter bogoriensis", "frozen_label": "Roseinatronobacter bogoriensis", "id": "119542", "rank": "species"}, {"current_id": "1217908", "current_name": "Octadecabacter antarcticus", "frozen_label": "Octadecabacter antarcticus", "id": "1217908", "rank": "species"}, {"current_id": "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label": "Leisingera methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id": "143224", "current_name": "Zobellia uliginosa", "frozen_label": "Zobellia uliginosa", "id": "143224", "rank": "species"}, {"current_id": "150120", "current_name": "Shewanella livingstonensis", "frozen_label": "Shewanella livingstonensis", "id": "150120", "rank": "species"}, {"current_id": "141390", "current_name": "Chromohalobacter israelensis", "frozen_label": null, "id": "158080", "rank": "species"}, {"current_id": "161528", "current_name": "Erythrobacter sp. SD-21", "frozen_label": "Erythrobacter sp. SD-21", "id": "161528", "rank": "species"}, {"current_id": "168275", "current_name": "Psychromonas arctica", "frozen_label": "Psychromonas arctica", "id": "168275", "rank": "species"}, {"current_id": "172371", "current_name": "Alloalcanivorax venustensis", "frozen_label": "Alloalcanivorax venustensis", "id": "172371", "rank": "species"}, {"current_id": "173737", "current_name": "Cytophaga sp. MBIC04693", "frozen_label": "Cytophaga sp. MBIC04693", "id": "173737", "rank": "species"}, {"current_id": "184914", "current_name": "Corallococcus coralloides", "frozen_label": "Corallococcus coralloides", "id": "184914", "rank": "species"}, {"current_id": "188906", "current_name": "Jannaschia helgolandensis", "frozen_label": "Jannaschia helgolandensis", "id": "188906", "rank": "species"}, {"current_id": "188908", "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica", "id": "188908", "rank": "species"}, {"current_id": "197222", "current_name": "Paraglaciecola mesophila", "frozen_label": "Paraglaciecola mesophila", "id": "197222", "rank": "species"}, {"current_id": "200617", "current_name": "Rhodopseudomonas julia", "frozen_label": "Rhodopseudomonas julia", "id": "200617", "rank": "species"}]. Alias/name resolution does not establish habitat occurrence. |
| TAX1 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1872627%2C1876%2C188906%2C188908%2C1903071%2C190308%2C191302%2C1926630%2C1931%2C195064%2C1961642%2C197222%2C198804%2C2%2C200617%2C2022602%2C2024855%2C203122%2C203907%2C205920%2C2099376%2C212050%2C214688%2C214988%2C216432%2C216773%2C2183988%2C2213%2C223788%2C224915%2C225345%2C225937%2C226126%2C2264%2C234267%2C240016%2C2423%2C243090%2C247026%2C257363%2C264%2C264462%2C264951%2C265606%2C266940%2C2738566%2C28108%2C28122%2C28181%2C28223%2C28251%2C28258%2C28262%2C29158%2C29159%2C2926447%2C29292%2C293614%2C29805%2C302409%2C3055%2C3068%2C31330%2C313595%2C313603%2C313606%2C314230%2C314275%2C316279%2C319225%2C320388%2C332415%2C337701%2C339861%2C340047%2C34085%2C344747%2C357244%2C35743%2C35845%2C358766%2C361576%2C36870%2C36987%2C372461%2C378806%2C379066%2C39152%2C391625%2C39947%2C402880%2C40464%2C406538%2C406540%2C411477%2C411485%2C419481%2C425006%2C428125%2C435805%2C43928%2C442956%2C443152%2C445336%2C44751%2C45351%2C457427%2C463619%2C46539%2C466153%2C46687%2C46704%2C46745%2C472759%2C483407%2C483417%2C48499%2C48729%2C491952%2C49447%2C498761%2C502025%2C504472%2C50741%2C515618%2C51671%2C518766%2C523849%2C530564%2C53249%2C537937%2C53953%2C55518%2C555512%2C55567%2C562%2C563043%2C56780%2C56811%2C57043%2C575540%2C583355%2C585501%2C595452%2C595453%2C59919%2C59920%2C6047%2C60480%2C6087&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The three chunks jointly resolve all 346 requested cohort IDs. Target results=[{"current_id": "102", "current_name": "Polaribacter glomeratus", "frozen_label": "Polaribacter glomeratus", "id": "102", "rank": "species"}, {"current_id": "1026", "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum furvescens", "id": "1026", "rank": "species"}, {"current_id": "103810", "current_name": "Riemerella columbina", "frozen_label": "Riemerella columbina", "id": "103810", "rank": "species"}, {"current_id": "104268", "current_name": "Tenacibaculum mesophilum", "frozen_label": "Tenacibaculum mesophilum", "id": "104268", "rank": "species"}, {"current_id": "104270", "current_name": "Tenacibaculum ovolyticum", "frozen_label": "Tenacibaculum ovolyticum", "id": "104270", "rank": "species"}, {"current_id": "1044", "current_name": "Erythrobacter longus", "frozen_label": "Erythrobacter longus", "id": "1044", "rank": "species"}, {"current_id": "107401", "current_name": "Tenacibaculum maritimum", "frozen_label": "Tenacibaculum maritimum", "id": "107401", "rank": "species"}, {"current_id": "1080", "current_name": "Afifella marina", "frozen_label": "Afifella marina", "id": "1080", "rank": "species"}, {"current_id": "111770", "current_name": "Thiothrix fructosivorans", "frozen_label": "Thiothrix fructosivorans", "id": "111770", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank": "species"}, {"current_id": "119542", "current_name": "Roseinatronobacter bogoriensis", "frozen_label": "Roseinatronobacter bogoriensis", "id": "119542", "rank": "species"}, {"current_id": "1217908", "current_name": "Octadecabacter antarcticus", "frozen_label": "Octadecabacter antarcticus", "id": "1217908", "rank": "species"}, {"current_id": "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label": "Leisingera methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id": "143224", "current_name": "Zobellia uliginosa", "frozen_label": "Zobellia uliginosa", "id": "143224", "rank": "species"}, {"current_id": "150120", "current_name": "Shewanella livingstonensis", "frozen_label": "Shewanella livingstonensis", "id": "150120", "rank": "species"}, {"current_id": "141390", "current_name": "Chromohalobacter israelensis", "frozen_label": null, "id": "158080", "rank": "species"}, {"current_id": "161528", "current_name": "Erythrobacter sp. SD-21", "frozen_label": "Erythrobacter sp. SD-21", "id": "161528", "rank": "species"}, {"current_id": "168275", "current_name": "Psychromonas arctica", "frozen_label": "Psychromonas arctica", "id": "168275", "rank": "species"}, {"current_id": "172371", "current_name": "Alloalcanivorax venustensis", "frozen_label": "Alloalcanivorax venustensis", "id": "172371", "rank": "species"}, {"current_id": "173737", "current_name": "Cytophaga sp. MBIC04693", "frozen_label": "Cytophaga sp. MBIC04693", "id": "173737", "rank": "species"}, {"current_id": "184914", "current_name": "Corallococcus coralloides", "frozen_label": "Corallococcus coralloides", "id": "184914", "rank": "species"}, {"current_id": "188906", "current_name": "Jannaschia helgolandensis", "frozen_label": "Jannaschia helgolandensis", "id": "188906", "rank": "species"}, {"current_id": "188908", "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica", "id": "188908", "rank": "species"}, {"current_id": "197222", "current_name": "Paraglaciecola mesophila", "frozen_label": "Paraglaciecola mesophila", "id": "197222", "rank": "species"}, {"current_id": "200617", "current_name": "Rhodopseudomonas julia", "frozen_label": "Rhodopseudomonas julia", "id": "200617", "rank": "species"}]. Alias/name resolution does not establish habitat occurrence. |
| TAX2 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=610380%2C6182%2C6238%2C6334%2C639602%2C641112%2C6613%2C6669%2C688066%2C69293%2C6945%2C69773%2C7029%2C703612%2C7070%2C7159%2C7209%2C7425%2C74546%2C74547%2C748449%2C756272%2C758583%2C75883%2C760154%2C765912%2C7668%2C76775%2C7719%2C777%2C7955%2C80836%2C8090%2C83428%2C86104%2C880%2C880447%2C885%2C89184%2C9031%2C91360%2C9258%2C939306%2C939316%2C939324%2C939346&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The three chunks jointly resolve all 346 requested cohort IDs. Target results=[{"current_id": "102", "current_name": "Polaribacter glomeratus", "frozen_label": "Polaribacter glomeratus", "id": "102", "rank": "species"}, {"current_id": "1026", "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum furvescens", "id": "1026", "rank": "species"}, {"current_id": "103810", "current_name": "Riemerella columbina", "frozen_label": "Riemerella columbina", "id": "103810", "rank": "species"}, {"current_id": "104268", "current_name": "Tenacibaculum mesophilum", "frozen_label": "Tenacibaculum mesophilum", "id": "104268", "rank": "species"}, {"current_id": "104270", "current_name": "Tenacibaculum ovolyticum", "frozen_label": "Tenacibaculum ovolyticum", "id": "104270", "rank": "species"}, {"current_id": "1044", "current_name": "Erythrobacter longus", "frozen_label": "Erythrobacter longus", "id": "1044", "rank": "species"}, {"current_id": "107401", "current_name": "Tenacibaculum maritimum", "frozen_label": "Tenacibaculum maritimum", "id": "107401", "rank": "species"}, {"current_id": "1080", "current_name": "Afifella marina", "frozen_label": "Afifella marina", "id": "1080", "rank": "species"}, {"current_id": "111770", "current_name": "Thiothrix fructosivorans", "frozen_label": "Thiothrix fructosivorans", "id": "111770", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank": "species"}, {"current_id": "119542", "current_name": "Roseinatronobacter bogoriensis", "frozen_label": "Roseinatronobacter bogoriensis", "id": "119542", "rank": "species"}, {"current_id": "1217908", "current_name": "Octadecabacter antarcticus", "frozen_label": "Octadecabacter antarcticus", "id": "1217908", "rank": "species"}, {"current_id": "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label": "Leisingera methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id": "143224", "current_name": "Zobellia uliginosa", "frozen_label": "Zobellia uliginosa", "id": "143224", "rank": "species"}, {"current_id": "150120", "current_name": "Shewanella livingstonensis", "frozen_label": "Shewanella livingstonensis", "id": "150120", "rank": "species"}, {"current_id": "141390", "current_name": "Chromohalobacter israelensis", "frozen_label": null, "id": "158080", "rank": "species"}, {"current_id": "161528", "current_name": "Erythrobacter sp. SD-21", "frozen_label": "Erythrobacter sp. SD-21", "id": "161528", "rank": "species"}, {"current_id": "168275", "current_name": "Psychromonas arctica", "frozen_label": "Psychromonas arctica", "id": "168275", "rank": "species"}, {"current_id": "172371", "current_name": "Alloalcanivorax venustensis", "frozen_label": "Alloalcanivorax venustensis", "id": "172371", "rank": "species"}, {"current_id": "173737", "current_name": "Cytophaga sp. MBIC04693", "frozen_label": "Cytophaga sp. MBIC04693", "id": "173737", "rank": "species"}, {"current_id": "184914", "current_name": "Corallococcus coralloides", "frozen_label": "Corallococcus coralloides", "id": "184914", "rank": "species"}, {"current_id": "188906", "current_name": "Jannaschia helgolandensis", "frozen_label": "Jannaschia helgolandensis", "id": "188906", "rank": "species"}, {"current_id": "188908", "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica", "id": "188908", "rank": "species"}, {"current_id": "197222", "current_name": "Paraglaciecola mesophila", "frozen_label": "Paraglaciecola mesophila", "id": "197222", "rank": "species"}, {"current_id": "200617", "current_name": "Rhodopseudomonas julia", "frozen_label": "Rhodopseudomonas julia", "id": "200617", "rank": "species"}]. Alias/name resolution does not establish habitat occurrence. |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf; Search boundaries are explicit; no global absence claim | supports | Identifier, label, slug and exact-path searches included hidden/ignored files in these roots. No earlier structured target observation was found. Legacy reports exist and are not silently retired. Bounded original-source search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv", "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv", "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv", "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv", "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv", "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv", "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv", "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv", "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv", "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv", "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}], "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "exit_code": 0, "matches": [], "stderr": ""}]} |
| ISSUES | https://github.com/CultureBotAI/HabitatMech/issues; GitHub CLI inventory retrieved 12-Oct | supports | Read-only all-state 967-issue title/body inventory and relevant bodies inspected. Issues are historical leads, not primary support; current owner rows and scientific evidence were checked independently. Comments were not exhaustively crawled. Closed issue #1301 is reflected in the current graph and is not reopened by preserving old history. |

## Limits And Additional Notes

- Completed assessment is not a clean-record verdict or proof of every original source occurrence.
- Only the first three exact-path BioSample and Organism descriptions per target/sheet were individually interpreted; remaining members and study joins were indexed, not scientifically reviewed.
- Later GOLD export/classification does not reconstruct original August membership. No ontology, taxonomy or source snapshot was refreshed.
- Same-agent review, not independent approval. Native status and curation/history inputs are unchanged.
- SSSOM/KGX conformance to current kg-microbe modeling was not audited; shared endpoint issue #1398 remains open.
- Whole-corpus scientific review remains incomplete. Ancestor/context reads add no record coverage. Product-label checking retains 2057 no-adapter skips and five accepted exceptions.
- Review-only observation: no curation, status promotion, GitHub mutation or paid research.
- No earlier structured target observation found; legacy reports are historical and are not automatically superseded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T054254Z-marine_reef
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: marine_reef'
started_at: '2026-10-12T05:18:45.183669Z'
finished_at: '2026-10-12T05:42:54.839387Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Agent has participated in repository curation; this is not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The physical marine reef retains reef ancestry and location within marine
  water, rather than being a biome. Its PREGO pool of 112 and selected 25 associations
  match the reef-biome record, but shared observations do not prove identity or authorize
  merging. Taxon 158080 is a resolvable historical alias of 141390, not a broken reference.
source:
  git_revision: ed9e0d0f382e4502a64f4de10102c4512bddca38
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
    sha256: 2fd5aec7ac1710ede2405849e78dd0423c253d72b43676230f72b9905bae99dd
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 1934ff1b8a27ba93174a6b656dc489506c47c3aae8204db89b7516ae2cc0886f
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 3f2ce04805defe5ff65dc20988cc72bc94d4636b3140eb1311017866bdc0ea0a
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/aquatic/marine_reef.yaml
    sha256: bbdd76b8996558a201f5d7c26955b6a5787090001571341361db64150f966acf
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
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260927T073130Z-coral_reef.md
    sha256: 3b608b9c3fd7558216f7c92449dcfb34349f0a32503e01284208af9b181de52b
    role: context
  - path: reports/yaml_record_review/20260928T155715Z-marine_debries.md
    sha256: e53a8d1b9100924541b9d5373087ddb4e5dbe2fbad90b986ccb928dfa7e9734c
    role: context
  - path: reports/yaml_record_review/20261003T194635Z-marine_reef.md
    sha256: 3b1ba981e340828133965bcdd9730327d49850222bc1115e893ddab90277cb9d
    role: context
  - path: reports/yaml_record_review/20261003T194832Z-marine_reef_biome.md
    sha256: 247164d1d630d272151161ce6c71e6b17fb2e266bfae85eeea17652e5a6f857a
    role: context
  - path: reports/yaml_record_review/20261003T201840Z-marine_sponge_reef.md
    sha256: f07aae926d6d8600cfd59def99fa051db7c37660ad767d8eb1df92ba3468d97f
    role: context
  - path: reports/yaml_record_review/20261005T004149Z-reef_zone.md
    sha256: e7977c8172971df3bc5402e5776d7ca7f33ca4e91f09ec01afc1878cc6fae483
    role: context
  - path: research/habitats/host_associated/cnidaria-habitatmech-gold-e3fede2aea-deep-research-claude_code.md
    sha256: 940129ed92b38e855908f71f2e399441137ad15fab83adc1cd433cfaa68716cb
    role: context
  - path: research/habitats/host_associated/oyster-habitatmech-gold-fd2443a2c3-deep-research-claude_code.md
    sha256: bec20f814923184f5b87a1a3613e6df40c47e13e265065fe473960e1e9ab4691
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: 4bf5391d25ff48a2d81eb3821af6582de063fd0391440973d309dfd93016490c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
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
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
targets:
- target_id: ENVO:01000143
  path: data/habitats/aquatic/marine_reef.yaml
  label: marine reef
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source-specific identity and lifecycle decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definitions and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded source context-parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology labels, definitions and synonyms
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Harmonization and generated record construction
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Frozen PREGO source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Frozen PREGO source inventory
scope:
  description: Entire exact generated record, all contributors and individual asserted
    causal edges, with bounded source-context assessment.
  selection: 'Next forty records without a completed individual scientific review
    in stable repository-relative path order: marine anoxic zone through microbial_mats__200e1828.
    Full individual observations, not a category-wide pass. Prior coverage counts
    distinct observations, not a clean current-input corpus. Starting distinct-review
    coverage 688/3208 is not clean current-input coverage.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:01000143
  exclusions:
  - target: Other 3207 current records
    reason: Context reads are not their full scientific review.
checks:
- check_id: C0
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:01000143
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=ed9e0d0f382e4502a64f4de10102c4512bddca38
    just validate data/habitats/aquatic/marine_reef.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:21:57.392635Z to 2026-10-12T05:22:01.423608Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C1
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:01000143
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=ed9e0d0f382e4502a64f4de10102c4512bddca38
    just validate-strict data/habitats/aquatic/marine_anoxic_zone.yaml data/habitats/aquatic/marine_aphotic_zone.yaml
    data/habitats/aquatic/marine_basin_floor.yaml data/habitats/aquatic/marine_bathyal_zone_biome.yaml
    data/habitats/aquatic/marine_bathypelagic_zone.yaml data/habitats/aquatic/marine_benthic_biome.yaml
    data/habitats/aquatic/marine_biome.yaml data/habitats/aquatic/marine_cold_seep_biome.yaml
    data/habitats/aquatic/marine_coral_reef_biome.yaml data/habitats/aquatic/marine_lake.yaml
    data/habitats/aquatic/marine_littoral_zone.yaml data/habitats/aquatic/marine_mesopelagic_zone.yaml
    data/habitats/aquatic/marine_mud.yaml data/habitats/aquatic/marine_oligotrophic_desert.yaml
    data/habitats/aquatic/marine_pelagic_zone.yaml data/habitats/aquatic/marine_photic_zone.yaml
    data/habitats/aquatic/marine_reef.yaml data/habitats/aquatic/marine_reef_biome.yaml
    data/habitats/aquatic/marine_salt_marsh_biome.yaml data/habitats/aquatic/marine_sediment.yaml
    data/habitats/aquatic/marine_sponge_reef.yaml data/habitats/aquatic/marine_supra_littoral_zone.yaml
    data/habitats/aquatic/marine_water_body.yaml data/habitats/aquatic/marsh.yaml
    data/habitats/aquatic/mediterranean_sea_biome.yaml data/habitats/aquatic/melt_pond.yaml
    data/habitats/aquatic/meltwater.yaml data/habitats/aquatic/meromictic_lake.yaml
    data/habitats/aquatic/mesopelagic_twilight_zone.yaml data/habitats/aquatic/metalimnion.yaml
    data/habitats/aquatic/microbial_mat__2020a793.yaml data/habitats/aquatic/microbial_mat__23532df8.yaml
    data/habitats/aquatic/microbial_mat__5129baa2.yaml data/habitats/aquatic/microbial_mat__54ad7767.yaml
    data/habitats/aquatic/microbial_mat__8a9e02e4.yaml data/habitats/aquatic/microbial_mat__b6425172.yaml
    data/habitats/aquatic/microbial_mat__eb27cff0.yaml data/habitats/aquatic/microbial_mat__fc2dbb7f.yaml
    data/habitats/aquatic/microbial_mats.yaml data/habitats/aquatic/microbial_mats__200e1828.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:23:16.222412Z to 2026-10-12T05:23:26.347203Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C2
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:01000143
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=ed9e0d0f382e4502a64f4de10102c4512bddca38
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:23:26.348469Z to 2026-10-12T05:23:51.098950Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C3
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:01000143
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=ed9e0d0f382e4502a64f4de10102c4512bddca38
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:23:51.100146Z to 2026-10-12T05:25:01.530644Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C4
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:01000143
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=ed9e0d0f382e4502a64f4de10102c4512bddca38
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:25:01.532072Z to 2026-10-12T05:25:11.808379Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C5
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:01000143
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=ed9e0d0f382e4502a64f4de10102c4512bddca38
    just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:25:11.809657Z to 2026-10-12T05:25:19.058687Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C6
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:01000143
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=ed9e0d0f382e4502a64f4de10102c4512bddca38
    just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:25:19.059693Z to 2026-10-12T05:25:46.351294Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C7
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:01000143
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=ed9e0d0f382e4502a64f4de10102c4512bddca38
    just provenance-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:25:46.352569Z to 2026-10-12T05:25:47.389752Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C8
  name: Exact-base CI authoritative QC
  required: true
  status: passed
  target_ids:
  - ENVO:01000143
  command: gh run view 38205892664 --repo CultureBotAI/HabitatMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:21:53.294030Z to 2026-10-12T05:21:55.368917Z.
    All three required merge-group workflows passed at the exact captured base; authoritative
    QC passed 913 tests with 3 skipped. Newly saved review bundles require their own
    integrity check. These newly saved review bundles were not part of that earlier
    exact-base CI run.
  evidence_ids:
  - R
  - RULES
- check_id: REPRO
  name: Complete target reconstruction
  required: false
  status: passed
  target_ids:
  - ENVO:01000143
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache uv run python
    /private/tmp/habitatmech-review-bc-evidence.py
  exit_code: 0
  summary: All 40 complete documents matched; captured hashes rechecked before authoring.
  evidence_ids:
  - RAW
  - CODE
- check_id: ORIGINAL
  name: Original assertion membership
  required: false
  status: unavailable
  target_ids:
  - ENVO:01000143
  summary: Bounded ignored-inclusive searches did not recover complete original assertion
    inputs; later exports are contextual evidence only.
  evidence_ids:
  - SEARCH
- check_id: IMODULON
  name: Expression-adapter applicability
  required: false
  status: not_applicable
  target_ids:
  - ENVO:01000143
  summary: The successful 28-dataset inventory was read for graph scope. No matching
    claim-specific organism/strain/gene or expression-module assertion requires a
    search or summarize call. Absence is not negative ecological evidence.
  evidence_ids:
  - R
  - RULES
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/aquatic/marine_reef.yaml
  summary: The physical marine reef retains reef ancestry and location within marine
    water, rather than being a biome. Its PREGO pool of 112 and selected 25 associations
    match the reef-biome record, but shared observations do not prove identity or
    authorize merging. Taxon 158080 is a resolvable historical alias of 141390, not
    a broken reference.
  accessed_at: '2026-10-12T05:40:43.431606Z'
  support: supports
  locator: Entire captured YAML read, including all taxa, parameters, graphs and generated
    history
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml
  summary: Applied exact identity, strict-genus, MIxS roles, source-unit/score and
    ITEM lifecycle contracts; graph node types retain their biological definitions.
  accessed_at: '2026-10-12T05:40:43.431606Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:01001899",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:01000143"}, "logical_row": 5794}],
    "data/raw/ontology_terms.tsv": [{"data": {"definition": "A reef which is located
    in a marine water body.", "deprecated": "", "directly_referenced": "TRUE", "label":
    "marine reef", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id":
    "ENVO:01000143"}, "logical_row": 7643}], "data/raw/prego_habitat_taxa.tsv": [{"data":
    {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE",
    "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "1", "taxon_id": "NCBITaxon:102",
    "taxon_label": "Polaribacter glomeratus"}, "logical_row": 7747}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "2", "taxon_id": "NCBITaxon:1026",
    "taxon_label": "Marinoscillum furvescens"}, "logical_row": 7748}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "3", "taxon_id": "NCBITaxon:103810",
    "taxon_label": "Riemerella columbina"}, "logical_row": 7749}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "4", "taxon_id": "NCBITaxon:104268",
    "taxon_label": "Tenacibaculum mesophilum"}, "logical_row": 7750}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "5", "taxon_id": "NCBITaxon:104270",
    "taxon_label": "Tenacibaculum ovolyticum"}, "logical_row": 7751}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "6", "taxon_id": "NCBITaxon:1044",
    "taxon_label": "Erythrobacter longus"}, "logical_row": 7752}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "7", "taxon_id": "NCBITaxon:107401",
    "taxon_label": "Tenacibaculum maritimum"}, "logical_row": 7753}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "8", "taxon_id": "NCBITaxon:1080",
    "taxon_label": "Afifella marina"}, "logical_row": 7754}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "9", "taxon_id": "NCBITaxon:111770",
    "taxon_label": "Thiothrix fructosivorans"}, "logical_row": 7755}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "10", "taxon_id": "NCBITaxon:114404",
    "taxon_label": "Edaphosphingomonas fennica"}, "logical_row": 7756}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "11", "taxon_id": "NCBITaxon:119542",
    "taxon_label": "Roseinatronobacter bogoriensis"}, "logical_row": 7757}, {"data":
    {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE",
    "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "12", "taxon_id": "NCBITaxon:1217908",
    "taxon_label": "Octadecabacter antarcticus"}, "logical_row": 7758}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "13", "taxon_id": "NCBITaxon:133924",
    "taxon_label": "Leisingera methylohalidivorans"}, "logical_row": 7759}, {"data":
    {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE",
    "prego_id": "ENVO:01000143", "prego_score": "4", "rank": "14", "taxon_id": "NCBITaxon:143224",
    "taxon_label": "Zobellia uliginosa"}, "logical_row": 7760}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "15", "taxon_id": "NCBITaxon:150120",
    "taxon_label": "Shewanella livingstonensis"}, "logical_row": 7761}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:01000143", "prego_score": "4", "rank": "16", "taxon_id": "NCBITaxon:158080",
    "taxon_label": ""}, "logical_row": 7762}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score":
    "4", "rank": "17", "taxon_id": "NCBITaxon:161528", "taxon_label": "Erythrobacter
    sp. SD-21"}, "logical_row": 7763}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score":
    "4", "rank": "18", "taxon_id": "NCBITaxon:168275", "taxon_label": "Psychromonas
    arctica"}, "logical_row": 7764}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score":
    "4", "rank": "19", "taxon_id": "NCBITaxon:172371", "taxon_label": "Alloalcanivorax
    venustensis"}, "logical_row": 7765}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score":
    "4", "rank": "20", "taxon_id": "NCBITaxon:173737", "taxon_label": "Cytophaga sp.
    MBIC04693"}, "logical_row": 7766}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score":
    "4", "rank": "21", "taxon_id": "NCBITaxon:184914", "taxon_label": "Corallococcus
    coralloides"}, "logical_row": 7767}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score":
    "4", "rank": "22", "taxon_id": "NCBITaxon:188906", "taxon_label": "Jannaschia
    helgolandensis"}, "logical_row": 7768}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score":
    "4", "rank": "23", "taxon_id": "NCBITaxon:188908", "taxon_label": "Oleispira antarctica"},
    "logical_row": 7769}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank":
    "24", "taxon_id": "NCBITaxon:197222", "taxon_label": "Paraglaciecola mesophila"},
    "logical_row": 7770}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:01000143", "prego_score": "4", "rank":
    "25", "taxon_id": "NCBITaxon:200617", "taxon_label": "Rhodopseudomonas julia"},
    "logical_row": 7771}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category":
    "biolink:OntologyClass", "channels": "environmental_samples", "direct_assertion_count":
    "112", "max_prego_score": "4", "ontology": "ENVO", "prego_id": "ENVO:01000143",
    "prego_synonyms": "marine reef|marine reefs", "taxon_count": "112"}, "logical_row":
    181}]}'
  accessed_at: '2026-10-12T05:40:43.431606Z'
  support: supports
  locator: Exact logical TSV rows, header=row1; filtered by current source IDs and
    exact paths, not legacy issue line numbers
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:01000143", "mapping_predicate": null, "reviewed":
    false, "route": "prego_self_grounded"}, "automatic": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:01000143", "mapping_predicate": null, "reviewed":
    false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.b465e3c8a7",
    "source": "PREGO", "source_id": "ENVO:01000143"}], "source_concepts": 1}'
  accessed_at: '2026-10-12T05:40:43.431606Z'
  support: supports
  locator: Executed complete-document reconstruction; all 40 matched; routes distinguish
    source mints and generated identity
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl
  summary: '{"ENVO:01000143": {"definitions": ["A reef which is located in a marine
    water body."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_01001899"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0001025"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00001999"]}],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}],
    "labels": ["marine reef"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01001899",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0001025"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00001999"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [],
    "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:01001899": {"definitions":
    [], "deprecated": [], "equivalents": [], "labels": ["reef"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000012"],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [],
    "hasNarrowSynonym": [], "hasRelatedSynonym": []}}}'
  accessed_at: '2026-10-12T05:20:26.560054Z'
  support: supports
  locator: Official OWL retrieved 12-Oct; labels, definitions, typed synonyms, named
    parents and restrictions; no snapshot refresh
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/raw/ontology_terms.tsv
  summary: '{}'
  accessed_at: '2026-10-12T05:40:43.431606Z'
  support: supports
  locator: Ancestor context adds no full-record coverage
- evidence_id: TAX0
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1000566%2C1003110%2C1005925%2C1005926%2C1005928%2C1006%2C1007105%2C1007109%2C1007110%2C1007111%2C1007112%2C1007113%2C1007114%2C1007115%2C1007116%2C1007117%2C1007118%2C1007119%2C1007120%2C1007122%2C1007124%2C1009412%2C1009413%2C1009414%2C1009415%2C1009416%2C1009418%2C1009419%2C1009420%2C1009421%2C1017277%2C102%2C1026%2C1027373%2C1027374%2C1028566%2C1028742%2C1028743%2C1028745%2C1028746%2C1028749%2C1028752%2C1031273%2C1031541%2C103810%2C1038845%2C1038928%2C1038929%2C1042%2C104268%2C104270%2C1042877%2C1044%2C104421%2C1045558%2C1048%2C1048221%2C1057%2C106299%2C1074%2C107401%2C1080%2C1089550%2C109263%2C1094980%2C110163%2C1104565%2C1104566%2C110662%2C110663%2C111770%2C1121404%2C1121937%2C1121948%2C1122607%2C1123059%2C1123242%2C1123275%2C114404%2C1150474%2C119394%2C119542%2C1208324%2C1211807%2C121224%2C1217908%2C1219067%2C1242148%2C1246444%2C1246460%2C1265%2C126741%2C1267768%2C1267769%2C1276246%2C1282%2C129958%2C132144%2C133924%2C134561%2C1358%2C13616%2C13686%2C1371%2C1387275%2C139239%2C1394%2C1411902%2C143223%2C143224%2C147%2C1486246%2C150120%2C1543721%2C156%2C156128%2C156133%2C1570%2C158080%2C158192%2C158500%2C1609977%2C161528%2C163248%2C163503%2C168275%2C168759%2C1703256%2C1716143%2C172371%2C173%2C173365%2C173737%2C173764%2C174%2C174302%2C174315%2C1774373%2C179326%2C180542%2C1808508%2C1808945%2C1817405%2C1836499%2C184592%2C184914%2C1855%2C186022%2C1869227%2C1871328&retmode=xml
  summary: 'The three chunks jointly resolve all 346 requested cohort IDs. Target
    results=[{"current_id": "102", "current_name": "Polaribacter glomeratus", "frozen_label":
    "Polaribacter glomeratus", "id": "102", "rank": "species"}, {"current_id": "1026",
    "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum furvescens",
    "id": "1026", "rank": "species"}, {"current_id": "103810", "current_name": "Riemerella
    columbina", "frozen_label": "Riemerella columbina", "id": "103810", "rank": "species"},
    {"current_id": "104268", "current_name": "Tenacibaculum mesophilum", "frozen_label":
    "Tenacibaculum mesophilum", "id": "104268", "rank": "species"}, {"current_id":
    "104270", "current_name": "Tenacibaculum ovolyticum", "frozen_label": "Tenacibaculum
    ovolyticum", "id": "104270", "rank": "species"}, {"current_id": "1044", "current_name":
    "Erythrobacter longus", "frozen_label": "Erythrobacter longus", "id": "1044",
    "rank": "species"}, {"current_id": "107401", "current_name": "Tenacibaculum maritimum",
    "frozen_label": "Tenacibaculum maritimum", "id": "107401", "rank": "species"},
    {"current_id": "1080", "current_name": "Afifella marina", "frozen_label": "Afifella
    marina", "id": "1080", "rank": "species"}, {"current_id": "111770", "current_name":
    "Thiothrix fructosivorans", "frozen_label": "Thiothrix fructosivorans", "id":
    "111770", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas
    fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank":
    "species"}, {"current_id": "119542", "current_name": "Roseinatronobacter bogoriensis",
    "frozen_label": "Roseinatronobacter bogoriensis", "id": "119542", "rank": "species"},
    {"current_id": "1217908", "current_name": "Octadecabacter antarcticus", "frozen_label":
    "Octadecabacter antarcticus", "id": "1217908", "rank": "species"}, {"current_id":
    "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label": "Leisingera
    methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id": "143224",
    "current_name": "Zobellia uliginosa", "frozen_label": "Zobellia uliginosa", "id":
    "143224", "rank": "species"}, {"current_id": "150120", "current_name": "Shewanella
    livingstonensis", "frozen_label": "Shewanella livingstonensis", "id": "150120",
    "rank": "species"}, {"current_id": "141390", "current_name": "Chromohalobacter
    israelensis", "frozen_label": null, "id": "158080", "rank": "species"}, {"current_id":
    "161528", "current_name": "Erythrobacter sp. SD-21", "frozen_label": "Erythrobacter
    sp. SD-21", "id": "161528", "rank": "species"}, {"current_id": "168275", "current_name":
    "Psychromonas arctica", "frozen_label": "Psychromonas arctica", "id": "168275",
    "rank": "species"}, {"current_id": "172371", "current_name": "Alloalcanivorax
    venustensis", "frozen_label": "Alloalcanivorax venustensis", "id": "172371", "rank":
    "species"}, {"current_id": "173737", "current_name": "Cytophaga sp. MBIC04693",
    "frozen_label": "Cytophaga sp. MBIC04693", "id": "173737", "rank": "species"},
    {"current_id": "184914", "current_name": "Corallococcus coralloides", "frozen_label":
    "Corallococcus coralloides", "id": "184914", "rank": "species"}, {"current_id":
    "188906", "current_name": "Jannaschia helgolandensis", "frozen_label": "Jannaschia
    helgolandensis", "id": "188906", "rank": "species"}, {"current_id": "188908",
    "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica",
    "id": "188908", "rank": "species"}, {"current_id": "197222", "current_name": "Paraglaciecola
    mesophila", "frozen_label": "Paraglaciecola mesophila", "id": "197222", "rank":
    "species"}, {"current_id": "200617", "current_name": "Rhodopseudomonas julia",
    "frozen_label": "Rhodopseudomonas julia", "id": "200617", "rank": "species"}].
    Alias/name resolution does not establish habitat occurrence.'
  accessed_at: '2026-10-12T05:21:31.882540Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: 47eba2c6c7ff47d6263796c3afdcff6e39319e77b443b6200d469773ef5ff403
- evidence_id: TAX1
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1872627%2C1876%2C188906%2C188908%2C1903071%2C190308%2C191302%2C1926630%2C1931%2C195064%2C1961642%2C197222%2C198804%2C2%2C200617%2C2022602%2C2024855%2C203122%2C203907%2C205920%2C2099376%2C212050%2C214688%2C214988%2C216432%2C216773%2C2183988%2C2213%2C223788%2C224915%2C225345%2C225937%2C226126%2C2264%2C234267%2C240016%2C2423%2C243090%2C247026%2C257363%2C264%2C264462%2C264951%2C265606%2C266940%2C2738566%2C28108%2C28122%2C28181%2C28223%2C28251%2C28258%2C28262%2C29158%2C29159%2C2926447%2C29292%2C293614%2C29805%2C302409%2C3055%2C3068%2C31330%2C313595%2C313603%2C313606%2C314230%2C314275%2C316279%2C319225%2C320388%2C332415%2C337701%2C339861%2C340047%2C34085%2C344747%2C357244%2C35743%2C35845%2C358766%2C361576%2C36870%2C36987%2C372461%2C378806%2C379066%2C39152%2C391625%2C39947%2C402880%2C40464%2C406538%2C406540%2C411477%2C411485%2C419481%2C425006%2C428125%2C435805%2C43928%2C442956%2C443152%2C445336%2C44751%2C45351%2C457427%2C463619%2C46539%2C466153%2C46687%2C46704%2C46745%2C472759%2C483407%2C483417%2C48499%2C48729%2C491952%2C49447%2C498761%2C502025%2C504472%2C50741%2C515618%2C51671%2C518766%2C523849%2C530564%2C53249%2C537937%2C53953%2C55518%2C555512%2C55567%2C562%2C563043%2C56780%2C56811%2C57043%2C575540%2C583355%2C585501%2C595452%2C595453%2C59919%2C59920%2C6047%2C60480%2C6087&retmode=xml
  summary: 'The three chunks jointly resolve all 346 requested cohort IDs. Target
    results=[{"current_id": "102", "current_name": "Polaribacter glomeratus", "frozen_label":
    "Polaribacter glomeratus", "id": "102", "rank": "species"}, {"current_id": "1026",
    "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum furvescens",
    "id": "1026", "rank": "species"}, {"current_id": "103810", "current_name": "Riemerella
    columbina", "frozen_label": "Riemerella columbina", "id": "103810", "rank": "species"},
    {"current_id": "104268", "current_name": "Tenacibaculum mesophilum", "frozen_label":
    "Tenacibaculum mesophilum", "id": "104268", "rank": "species"}, {"current_id":
    "104270", "current_name": "Tenacibaculum ovolyticum", "frozen_label": "Tenacibaculum
    ovolyticum", "id": "104270", "rank": "species"}, {"current_id": "1044", "current_name":
    "Erythrobacter longus", "frozen_label": "Erythrobacter longus", "id": "1044",
    "rank": "species"}, {"current_id": "107401", "current_name": "Tenacibaculum maritimum",
    "frozen_label": "Tenacibaculum maritimum", "id": "107401", "rank": "species"},
    {"current_id": "1080", "current_name": "Afifella marina", "frozen_label": "Afifella
    marina", "id": "1080", "rank": "species"}, {"current_id": "111770", "current_name":
    "Thiothrix fructosivorans", "frozen_label": "Thiothrix fructosivorans", "id":
    "111770", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas
    fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank":
    "species"}, {"current_id": "119542", "current_name": "Roseinatronobacter bogoriensis",
    "frozen_label": "Roseinatronobacter bogoriensis", "id": "119542", "rank": "species"},
    {"current_id": "1217908", "current_name": "Octadecabacter antarcticus", "frozen_label":
    "Octadecabacter antarcticus", "id": "1217908", "rank": "species"}, {"current_id":
    "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label": "Leisingera
    methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id": "143224",
    "current_name": "Zobellia uliginosa", "frozen_label": "Zobellia uliginosa", "id":
    "143224", "rank": "species"}, {"current_id": "150120", "current_name": "Shewanella
    livingstonensis", "frozen_label": "Shewanella livingstonensis", "id": "150120",
    "rank": "species"}, {"current_id": "141390", "current_name": "Chromohalobacter
    israelensis", "frozen_label": null, "id": "158080", "rank": "species"}, {"current_id":
    "161528", "current_name": "Erythrobacter sp. SD-21", "frozen_label": "Erythrobacter
    sp. SD-21", "id": "161528", "rank": "species"}, {"current_id": "168275", "current_name":
    "Psychromonas arctica", "frozen_label": "Psychromonas arctica", "id": "168275",
    "rank": "species"}, {"current_id": "172371", "current_name": "Alloalcanivorax
    venustensis", "frozen_label": "Alloalcanivorax venustensis", "id": "172371", "rank":
    "species"}, {"current_id": "173737", "current_name": "Cytophaga sp. MBIC04693",
    "frozen_label": "Cytophaga sp. MBIC04693", "id": "173737", "rank": "species"},
    {"current_id": "184914", "current_name": "Corallococcus coralloides", "frozen_label":
    "Corallococcus coralloides", "id": "184914", "rank": "species"}, {"current_id":
    "188906", "current_name": "Jannaschia helgolandensis", "frozen_label": "Jannaschia
    helgolandensis", "id": "188906", "rank": "species"}, {"current_id": "188908",
    "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica",
    "id": "188908", "rank": "species"}, {"current_id": "197222", "current_name": "Paraglaciecola
    mesophila", "frozen_label": "Paraglaciecola mesophila", "id": "197222", "rank":
    "species"}, {"current_id": "200617", "current_name": "Rhodopseudomonas julia",
    "frozen_label": "Rhodopseudomonas julia", "id": "200617", "rank": "species"}].
    Alias/name resolution does not establish habitat occurrence.'
  accessed_at: '2026-10-12T05:21:33.762356Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: 211e97ebc927aae4966a064aa1db888cc9672558b906b2333d2088bb0c5b87fb
- evidence_id: TAX2
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=610380%2C6182%2C6238%2C6334%2C639602%2C641112%2C6613%2C6669%2C688066%2C69293%2C6945%2C69773%2C7029%2C703612%2C7070%2C7159%2C7209%2C7425%2C74546%2C74547%2C748449%2C756272%2C758583%2C75883%2C760154%2C765912%2C7668%2C76775%2C7719%2C777%2C7955%2C80836%2C8090%2C83428%2C86104%2C880%2C880447%2C885%2C89184%2C9031%2C91360%2C9258%2C939306%2C939316%2C939324%2C939346&retmode=xml
  summary: 'The three chunks jointly resolve all 346 requested cohort IDs. Target
    results=[{"current_id": "102", "current_name": "Polaribacter glomeratus", "frozen_label":
    "Polaribacter glomeratus", "id": "102", "rank": "species"}, {"current_id": "1026",
    "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum furvescens",
    "id": "1026", "rank": "species"}, {"current_id": "103810", "current_name": "Riemerella
    columbina", "frozen_label": "Riemerella columbina", "id": "103810", "rank": "species"},
    {"current_id": "104268", "current_name": "Tenacibaculum mesophilum", "frozen_label":
    "Tenacibaculum mesophilum", "id": "104268", "rank": "species"}, {"current_id":
    "104270", "current_name": "Tenacibaculum ovolyticum", "frozen_label": "Tenacibaculum
    ovolyticum", "id": "104270", "rank": "species"}, {"current_id": "1044", "current_name":
    "Erythrobacter longus", "frozen_label": "Erythrobacter longus", "id": "1044",
    "rank": "species"}, {"current_id": "107401", "current_name": "Tenacibaculum maritimum",
    "frozen_label": "Tenacibaculum maritimum", "id": "107401", "rank": "species"},
    {"current_id": "1080", "current_name": "Afifella marina", "frozen_label": "Afifella
    marina", "id": "1080", "rank": "species"}, {"current_id": "111770", "current_name":
    "Thiothrix fructosivorans", "frozen_label": "Thiothrix fructosivorans", "id":
    "111770", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas
    fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank":
    "species"}, {"current_id": "119542", "current_name": "Roseinatronobacter bogoriensis",
    "frozen_label": "Roseinatronobacter bogoriensis", "id": "119542", "rank": "species"},
    {"current_id": "1217908", "current_name": "Octadecabacter antarcticus", "frozen_label":
    "Octadecabacter antarcticus", "id": "1217908", "rank": "species"}, {"current_id":
    "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label": "Leisingera
    methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id": "143224",
    "current_name": "Zobellia uliginosa", "frozen_label": "Zobellia uliginosa", "id":
    "143224", "rank": "species"}, {"current_id": "150120", "current_name": "Shewanella
    livingstonensis", "frozen_label": "Shewanella livingstonensis", "id": "150120",
    "rank": "species"}, {"current_id": "141390", "current_name": "Chromohalobacter
    israelensis", "frozen_label": null, "id": "158080", "rank": "species"}, {"current_id":
    "161528", "current_name": "Erythrobacter sp. SD-21", "frozen_label": "Erythrobacter
    sp. SD-21", "id": "161528", "rank": "species"}, {"current_id": "168275", "current_name":
    "Psychromonas arctica", "frozen_label": "Psychromonas arctica", "id": "168275",
    "rank": "species"}, {"current_id": "172371", "current_name": "Alloalcanivorax
    venustensis", "frozen_label": "Alloalcanivorax venustensis", "id": "172371", "rank":
    "species"}, {"current_id": "173737", "current_name": "Cytophaga sp. MBIC04693",
    "frozen_label": "Cytophaga sp. MBIC04693", "id": "173737", "rank": "species"},
    {"current_id": "184914", "current_name": "Corallococcus coralloides", "frozen_label":
    "Corallococcus coralloides", "id": "184914", "rank": "species"}, {"current_id":
    "188906", "current_name": "Jannaschia helgolandensis", "frozen_label": "Jannaschia
    helgolandensis", "id": "188906", "rank": "species"}, {"current_id": "188908",
    "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica",
    "id": "188908", "rank": "species"}, {"current_id": "197222", "current_name": "Paraglaciecola
    mesophila", "frozen_label": "Paraglaciecola mesophila", "id": "197222", "rank":
    "species"}, {"current_id": "200617", "current_name": "Rhodopseudomonas julia",
    "frozen_label": "Rhodopseudomonas julia", "id": "200617", "rank": "species"}].
    Alias/name resolution does not establish habitat occurrence.'
  accessed_at: '2026-10-12T05:21:35.121229Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: 7dccc4bfc1eff3c32cab8b06f150ad44aa14c05a522cd0b648b04709382f5821
- evidence_id: SEARCH
  kind: search
  reference: curation; history; research; reports; reviews; data/raw; data/habitats;
    conf
  summary: 'Identifier, label, slug and exact-path searches included hidden/ignored
    files in these roots. No earlier structured target observation was found. Legacy
    reports exist and are not silently retired. Bounded original-source search={"configured_root":
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists":
    true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv",
    "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv",
    "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv",
    "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv",
    "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv",
    "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv",
    "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv",
    "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv",
    "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv",
    "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv",
    "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}],
    "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"],
    "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command":
    ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "exit_code": 0, "matches": [], "stderr": ""}]}'
  accessed_at: '2026-10-12T05:40:43.431606Z'
  support: supports
  locator: Search boundaries are explicit; no global absence claim
  search_scope: 'Identifier, label, slug and exact-path searches included hidden/ignored
    files in these roots. No earlier structured target observation was found. Legacy
    reports exist and are not silently retired. Bounded original-source search={"configured_root":
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists":
    true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv",
    "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv",
    "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv",
    "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv",
    "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv",
    "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv",
    "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv",
    "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv",
    "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv",
    "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv",
    "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}],
    "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"],
    "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command":
    ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "exit_code": 0, "matches": [], "stderr": ""}]}'
- evidence_id: ISSUES
  kind: database
  reference: https://github.com/CultureBotAI/HabitatMech/issues
  summary: 'Read-only all-state 967-issue title/body inventory and relevant bodies
    inspected. Issues are historical leads, not primary support; current owner rows
    and scientific evidence were checked independently. Comments were not exhaustively
    crawled. Closed issue #1301 is reflected in the current graph and is not reopened
    by preserving old history.'
  accessed_at: '2026-10-12T05:40:43.431606Z'
  support: supports
  locator: GitHub CLI inventory retrieved 12-Oct
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Exact identity, definition and source intent
  outcome: supported
  summary: The physical marine reef retains reef ancestry and location within marine
    water, rather than being a biome. Its PREGO pool of 112 and selected 25 associations
    match the reef-biome record, but shared observations do not prove identity or
    authorize merging. Taxon 158080 is a resolvable historical alias of 141390, not
    a broken reference.
  target_ids:
  - ENVO:01000143
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
- assessment_id: HIERARCHY
  area: grounding
  topic: Parent contributors and mapping endpoints
  outcome: supported
  summary: The physical marine reef retains reef ancestry and location within marine
    water, rather than being a biome. Its PREGO pool of 112 and selected 25 associations
    match the reef-biome record, but shared observations do not prove identity or
    authorize merging. Taxon 158080 is a resolvable historical alias of 141390, not
    a broken reference. Ontology, GOLD path, ambiguous-leaf and authored-genus routes
    were distinguished.
  target_ids:
  - ENVO:01000143
  evidence_ids:
  - R
  - RAW
  - CODE
  - ONT
  - PARENT
- assessment_id: PROVENANCE
  area: provenance
  topic: Source units and native lifecycle
  outcome: supported
  summary: 'Complete reconstruction preserves 1 contributing concepts and 0 ITEM-reviewed
    contributors. Attestations=[{"source": "PREGO", "source_id": "ENVO:01000143",
    "source_label": "marine reef", "assertion_count": 112, "assertion_unit": "TAXON",
    "score": 4.0, "evidence_channels": "environmental_samples"}]. Counts with different
    units are not summed. Reproduction validates derivation, not the scientific truth
    of the mapping.'
  target_ids:
  - ENVO:01000143
  evidence_ids:
  - R
  - RAW
  - CODE
  - RULES
- assessment_id: TAXA
  area: evidence
  topic: Taxonomy and association scope
  outcome: concern
  summary: All emitted identifiers resolve, including historical aliases. Source rows,
    ranks, scores and corroboration reproduce; these are selected associations, not
    proven characteristic taxa. Original occurrence evidence was not fully recovered,
    so no claim of exhaustive ecological validation is made. 158080 resolves to 141390
    Chromohalobacter israelensis
  target_ids:
  - ENVO:01000143
  evidence_ids:
  - R
  - RAW
  - TAX0
  - TAX1
  - TAX2
  - RULES
- assessment_id: COMPLETENESS
  area: completeness
  topic: Optional slots and bounded evidence
  outcome: supported
  summary: Optional empty fields alone are not defects. No causal graph is asserted
    in the exact captured record; ignored-inclusive support search and the full causal
    gate were checked. No record-level gene/regulator or transcriptomics claim warrants
    a component query.
  target_ids:
  - ENVO:01000143
  evidence_ids:
  - R
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: envo-01000143-taxonomy-alias-maintenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical taxonomy identifiers or names need versioned maintenance
  description: 158080 resolves to 141390 Chromohalobacter israelensis. The original
    IDs remain resolvable; this is not proof of a false habitat association.
  target_ids:
  - ENVO:01000143
  field_paths:
  - characteristic_taxa
  evidence_ids:
  - R
  - RAW
  - TAX0
  - TAX1
  - TAX2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Actual source taxon-row owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Versioned taxon normalization
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Bounded lexical, candidate-assessment or versioned taxonomy
    maintenance concern.
actions:
- action_id: A1
  description: Use versioned taxonomy normalization, preserving original IDs/names,
    ranks, scores, source pools and corroboration. Test alias deduplication rather
    than guessing a replacement organism.
  finding_ids:
  - F1
  target_ids:
  - ENVO:01000143
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Actual source taxon-row owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Versioned taxon normalization
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained owners after source-level assessment; retain independent
    true parents, source identity/count/unit provenance and lifecycle unless a separately
    justified change requires otherwise.
  - Append required current history, add focused regressions, inspect a seed canary
    and regenerate affected products without hand-editing records or pages.
  - Pass schema, strict, label, provenance, corpus reproduction, causal/history and
    full QC gates; save a linked successor for any finding disposition.
limitations:
- Completed assessment is not a clean-record verdict or proof of every original source
  occurrence.
- Only the first three exact-path BioSample and Organism descriptions per target/sheet
  were individually interpreted; remaining members and study joins were indexed, not
  scientifically reviewed.
- Later GOLD export/classification does not reconstruct original August membership.
  No ontology, taxonomy or source snapshot was refreshed.
- Same-agent review, not independent approval. Native status and curation/history
  inputs are unchanged.
- 'SSSOM/KGX conformance to current kg-microbe modeling was not audited; shared endpoint
  issue #1398 remains open.'
- Whole-corpus scientific review remains incomplete. Ancestor/context reads add no
  record coverage. Product-label checking retains 2057 no-adapter skips and five accepted
  exceptions.
notes:
- 'Review-only observation: no curation, status promotion, GitHub mutation or paid
  research.'
- No earlier structured target observation found; legacy reports are historical and
  are not automatically superseded.
tags:
- habitatmech
- aquatic
- record-review
- scientific-review
```
