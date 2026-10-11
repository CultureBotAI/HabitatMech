# Scientific record review: laboratory_facility

- Review: 20261011T135533Z-laboratory_facility
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T13:19:57.612186Z
- Finished UTC: 2026-10-11T13:55:33.141533Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The current laboratory-facility identity, research-facility genus and exact research laboratory alias are coherent. All 25 displayed NCBI keys resolve with their emitted labels. BacDive strain6213 is classified Laboratory/Lab enrichment but was isolated from a dinoflagellate culture, demonstrating that Laboratory associations include culture provenance rather than proof of residence on facility surfaces. Preserve 363 STRAIN assertions, candidate pool310, rank/count semantics and the absence of characteristic-presence claims. The original flat category-to-facility crosswalk merits bounded reassessment.

## Scope And Provenance

Entire exact HabitatRecord, source contributors, direct-parent context and applicable biological evidence.

Selection: Next 24 alphabetically ordered unreviewed ENGINEERED records, indoor through manure. Each receives a separate full exact-target review. No category-wide scientific verdict or claim that other categories are reviewed. Starting completed-observation coverage351/3208; not a clean/currentness percentage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 05a328f935a9c9fc37571174fd7c2ac8f2e915f2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:01001406 | data/habitats/engineered/laboratory_facility.yaml | generated | laboratory facility |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native just validate | passed | True | ENVO:01001406 | Actual exit0; start 2026-10-11T13:21:14.168855Z; finish 2026-10-11T13:21:19.859041Z. Full-corpus gates do not imply additional scientific record coverage. |
| Native just validate-strict | passed | True | ENVO:01001406 | Actual exit0; start 2026-10-11T13:21:39.998009Z; finish 2026-10-11T13:21:50.571500Z. Full-corpus gates do not imply additional scientific record coverage. |
| Native just verify-corpus | passed | True | ENVO:01001406 | Actual exit0; start 2026-10-11T13:21:50.572551Z; finish 2026-10-11T13:22:22.018901Z. Full-corpus gates do not imply additional scientific record coverage. |
| Native just validate-products | passed | True | ENVO:01001406 | Actual exit0; start 2026-10-11T13:22:22.020180Z; finish 2026-10-11T13:23:56.625048Z. Full-corpus gates do not imply additional scientific record coverage. |
| Native just validate-history | passed | True | ENVO:01001406 | Actual exit0; start 2026-10-11T13:23:56.626020Z; finish 2026-10-11T13:24:06.431983Z. Full-corpus gates do not imply additional scientific record coverage. |
| Native just validate-causal-all | passed | True | ENVO:01001406 | Actual exit0; start 2026-10-11T13:24:06.433302Z; finish 2026-10-11T13:24:12.572770Z. Full-corpus gates do not imply additional scientific record coverage. |
| Native just term-requests-check | passed | True | ENVO:01001406 | Actual exit0; start 2026-10-11T13:24:12.573784Z; finish 2026-10-11T13:24:40.630469Z. Full-corpus gates do not imply additional scientific record coverage. |
| Native just qc | passed | True | ENVO:01001406 | Actual exit0; start 2026-10-11T13:24:40.631657Z; finish 2026-10-11T13:54:31.642833Z. Full-corpus gates do not imply additional scientific record coverage. |
| Complete target reproduction | passed | False | ENVO:01001406 | Fresh native build_document equals all fields of each of the 24 targets. |
| Original member/assertion reconstruction | unavailable | False | ENVO:01001406 | Original configured upstream input files were not recovered within the ignored-inclusive search bounds. Later exports are separate evidence. |

## Scientific And Domain Assessments

### Reported-from taxonomy, source units and ranks

evidence: supported. Targets: ENVO:01001406.

The current laboratory-facility identity, research-facility genus and exact research laboratory alias are coherent. All 25 displayed NCBI keys resolve with their emitted labels. BacDive strain6213 is classified Laboratory/Lab enrichment but was isolated from a dinoflagellate culture, demonstrating that Laboratory associations include culture provenance rather than proof of residence on facility surfaces. Preserve 363 STRAIN assertions, candidate pool310, rank/count semantics and the absence of characteristic-presence claims. The original flat category-to-facility crosswalk merits bounded reassessment. No is_characteristic field is present; source ranks and association scores are not prevalence.

### Identity, grounding, hierarchy, synonyms and source scope

identity: concern. Targets: ENVO:01001406.

The current laboratory-facility identity, research-facility genus and exact research laboratory alias are coherent. All 25 displayed NCBI keys resolve with their emitted labels. BacDive strain6213 is classified Laboratory/Lab enrichment but was isolated from a dinoflagellate culture, demonstrating that Laboratory associations include culture provenance rather than proof of residence on facility surfaces. Preserve 363 STRAIN assertions, candidate pool310, rank/count semantics and the absence of characteristic-presence claims. The original flat category-to-facility crosswalk merits bounded reassessment.

### Frozen source units and generated lifecycle

provenance: supported. Targets: ENVO:01001406.

All emitted fields reproduce. Exact maintained source rows preserve count units, collapsed nodes and source roles; zero-count omission does not mean no organisms. Source/reviewed-contributor counts=1/1. Actual routes are recorded in CODE. Scientific review does not promote native status or update frozen counts from later evidence.

### Claims proportional to evidence

completeness: supported. Targets: ENVO:01001406.

The full target contains no causal graph, gene/regulator or transcriptomic claim; iModulonDB is not applicable. No optional definition, parameter, mechanism, taxon or discussion is invented. Triad broad/local/medium roles remain contextual and source-specific.

## Findings

### F1: Original source entity and scope require bounded reassessment

minor / open / provisional; issue key: envo-01001406-source-entity-scope.

The current laboratory-facility identity, research-facility genus and exact research laboratory alias are coherent. All 25 displayed NCBI keys resolve with their emitted labels. BacDive strain6213 is classified Laboratory/Lab enrichment but was isolated from a dinoflagellate culture, demonstrating that Laboratory associations include culture provenance rather than proof of residence on facility surfaces. Preserve 363 STRAIN assertions, candidate pool310, rank/count semantics and the absence of characteristic-presence claims. The original flat category-to-facility crosswalk merits bounded reassessment.

## Recommended Actions And Acceptance Checks

### A1

Recover original category/member scope or an independently inspectable crosswalk; distinguish sample material, development/treatment activity and physical setting. Later members inform but do not replace frozen membership. Curate only supported changes, preserve ambiguity otherwise, and do not force optional fields or native status promotion.

- Use inspected primary evidence and the exact source path; preserve uncertainty rather than invent a replacement identity.
- Preserve count/unit semantics, source provenance and immutable histories/reviews; append native history for a supported curation change.
- Add exact-scope regressions, inspect a dry seed and canary, regenerate governed artifacts and pass labels, strict validation, provenance, reproduction, history and full QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/engineered/laboratory_facility.yaml; Entire generated YAML, including all histories, synonyms, sources and taxa | supports | The current laboratory-facility identity, research-facility genus and exact research laboratory alias are coherent. All 25 displayed NCBI keys resolve with their emitted labels. BacDive strain6213 is classified Laboratory/Lab enrichment but was isolated from a dinoflagellate culture, demonstrating that Laboratory associations include culture provenance rather than proof of residence on facility surfaces. Preserve 363 STRAIN assertions, candidate pool310, rank/count semantics and the absence of characteristic-presence claims. The original flat category-to-facility crosswalk merits bounded reassessment. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md; Complete local review checklist and maintained ownership | supports | Applied the native identity, strict-parent, source-unit, ITEM status, observational-taxon, triad-role and causal-evidence rubric. Optional absent fields are not automatically defects. |
| RAW | data/raw; curation/decisions.tsv; curation/gold_parent_exclusions.tsv; Exact source/mint/path rows, current decision and guarded exclusion contributions | supports | {"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-16", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:BACDIVE.3582899e36", "notes": "CLOSE-grounding review (#12): read against the full source path and the term's own definition. The grounding is right and CLOSE is the honest status \u2014 the term is the concept with a difference of framing or specificity that EXACT would overstate.", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row": 1746}], "data/raw/bacdive_isolation_sources.tsv": [{"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "label": "Laboratory", "source_slug": "laboratory", "strain_count": "363", "taxon_count": "310"}, "logical_row": 41}], "data/raw/bacdive_source_taxa.tsv": [{"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "1", "strain_count": "5", "taxon_id": "NCBITaxon:83428", "taxon_label": "uncultured Bacillus sp."}, "logical_row": 1599}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "2", "strain_count": "4", "taxon_id": "NCBITaxon:144185", "taxon_label": "Leifsonia aquatica"}, "logical_row": 1600}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "3", "strain_count": "4", "taxon_id": "NCBITaxon:153233", "taxon_label": "Oceanicaulis alexandrii"}, "logical_row": 1601}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "4", "strain_count": "4", "taxon_id": "NCBITaxon:286730", "taxon_label": "Alkaliflexus imshenetskii"}, "logical_row": 1602}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "5", "strain_count": "3", "taxon_id": "NCBITaxon:1211807", "taxon_label": "Stutzerimonas kunmingensis"}, "logical_row": 1603}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "6", "strain_count": "3", "taxon_id": "NCBITaxon:1270", "taxon_label": "Micrococcus luteus"}, "logical_row": 1604}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "7", "strain_count": "3", "taxon_id": "NCBITaxon:1280", "taxon_label": "Staphylococcus aureus"}, "logical_row": 1605}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "8", "strain_count": "3", "taxon_id": "NCBITaxon:1506", "taxon_label": "Clostridium sp."}, "logical_row": 1606}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "9", "strain_count": "3", "taxon_id": "NCBITaxon:28214", "taxon_label": "Sphingomonas sp."}, "logical_row": 1607}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "10", "strain_count": "3", "taxon_id": "NCBITaxon:294", "taxon_label": "Pseudomonas fluorescens"}, "logical_row": 1608}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "11", "strain_count": "3", "taxon_id": "NCBITaxon:562", "taxon_label": "Escherichia coli"}, "logical_row": 1609}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "12", "strain_count": "3", "taxon_id": "NCBITaxon:67263", "taxon_label": "Streptomyces griseus subsp. griseus"}, "logical_row": 1610}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "13", "strain_count": "2", "taxon_id": "NCBITaxon:1393", "taxon_label": "Brevibacillus brevis"}, "logical_row": 1611}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "14", "strain_count": "2", "taxon_id": "NCBITaxon:1402", "taxon_label": "Bacillus licheniformis"}, "logical_row": 1612}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "15", "strain_count": "2", "taxon_id": "NCBITaxon:1465", "taxon_label": "Brevibacillus laterosporus"}, "logical_row": 1613}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "16", "strain_count": "2", "taxon_id": "NCBITaxon:1486246", "taxon_label": "Halomonas sp."}, "logical_row": 1614}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "17", "strain_count": "2", "taxon_id": "NCBITaxon:1747", "taxon_label": "Cutibacterium acnes"}, "logical_row": 1615}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "18", "strain_count": "2", "taxon_id": "NCBITaxon:1869227", "taxon_label": "bacterium"}, "logical_row": 1616}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "19", "strain_count": "2", "taxon_id": "NCBITaxon:1906", "taxon_label": "Streptomyces fradiae"}, "logical_row": 1617}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "20", "strain_count": "2", "taxon_id": "NCBITaxon:2024826", "taxon_label": "Blastopirellula sp."}, "logical_row": 1618}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "21", "strain_count": "2", "taxon_id": "NCBITaxon:2041036", "taxon_label": "Corynebacterium gottingense"}, "logical_row": 1619}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "22", "strain_count": "2", "taxon_id": "NCBITaxon:2094151", "taxon_label": "Paramuribaculum intestinale"}, "logical_row": 1620}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "23", "strain_count": "2", "taxon_id": "NCBITaxon:2426", "taxon_label": "Teredinibacter turnerae"}, "logical_row": 1621}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "24", "strain_count": "2", "taxon_id": "NCBITaxon:28095", "taxon_label": "Burkholderia gladioli"}, "logical_row": 1622}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "25", "strain_count": "2", "taxon_id": "NCBITaxon:293", "taxon_label": "Brevundimonas diminuta"}, "logical_row": 1623}], "data/raw/isolation_source_groundings.tsv": [{"data": {"confidence": "medium", "curator": "ols4_auto", "mapping_justification": "semapv:LexicalMatching", "object_id": "ENVO:01001406", "object_label": "laboratory facility", "object_source": "ENVO", "predicate_id": "skos:closeMatch", "source_dataset": "bacdive", "subject_label": "Laboratory", "subject_label_normalized": "laboratory", "verified_date": "2026-05-01"}, "logical_row": 173}], "data/raw/ontology_terms.tsv": [{"data": {"definition": "A facility, permanent or temporary, on land, in air, space or water, where scientific research or measurements can be undertaken.", "deprecated": "", "directly_referenced": "TRUE", "label": "research facility", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id": "ENVO:00000469"}, "logical_row": 7046}, {"data": {"definition": "A research facility in which systems of manufactured products control internal conditions and in which scientific or technological research, experiments, and measurement may be performed.", "deprecated": "", "directly_referenced": "TRUE", "label": "laboratory facility", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "research laboratory", "term_id": "ENVO:01001406"}, "logical_row": 8893}]}. Logical TSV row ordinals include header. Related-record hits were filtered, not treated as target evidence. |
| CODE | src/habitatmech/seed.py; Complete target reconstruction; actual resolve_gold/apply_decision routes | supports | {"reviewed_sources": 1, "routes": [], "source_concepts": 1}. A fresh native build_document equals every target field; executed routes do not independently prove scientific equivalence. |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Exact labels, definitions, deprecation, synonym scopes and OWL parent/restriction axioms | supports | {"ENVO:00000469": {"comments": [], "definitions": ["A facility, permanent or temporary, on land, in air, space or water, where scientific research or measurements can be undertaken."], "deprecated": [], "equivalents": [], "identifier": "ENVO:00000469", "labels": ["research facility"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000070"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:01001406": {"comments": [], "definitions": ["A research facility in which systems of manufactured products control internal conditions and in which scientific or technological research, experiments, and measurement may be performed."], "deprecated": [], "equivalents": [], "identifier": "ENVO:01001406", "labels": ["laboratory facility"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000469", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000051"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01001405"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["research laboratory"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}}. Typed current ontology meaning is not itself proof of an exact GOLD crosswalk. |
| PARENT | data/habitats; data/raw/ontology_subclass_edges.tsv; Direct-parent definition and relation projection | supports | {"ENVO:00000469": {"definition": "A facility, permanent or temporary, on land, in air, space or water, where scientific research or measurements can be undertaken.", "identifier": "ENVO:00000469", "label": "research facility", "parent_habitats": ["ENVO:00000070"], "source_attestations": [{"assertion_count": 339, "assertion_unit": "TAXON", "evidence_channels": "environmental_samples", "score": 1.75033, "source": "PREGO", "source_id": "ENVO:00000469", "source_label": "research facility"}]}}. Parent identity/source context only, not extra full-record coverage. |
| SEARCH | curation; data/raw; data/habitats; history; research; reports; reviews; conf; Exact-ID review census and ignored-inclusive source/support searches | supports | Ignored/hidden-inclusive rg searched IDs, labels, slugs, source IDs and paths. Structured raw/curation rows and prior review target/finding identities were also scanned. No prior structured review assessed this exact target at capture. Original configured inputs: {"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv", "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv", "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv", "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv", "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv", "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv", "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv", "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv", "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv", "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv", "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}], "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "exit_code": 0, "matches": [], "stderr": ""}]}. Configured-path/file-name misses are bounded, not global absence. |
| TAXA | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1132443%2C1211807%2C1270%2C1280%2C1385515%2C1393%2C1402%2C144185%2C1465%2C1486246%2C1506%2C153233%2C1549639%2C1747%2C1869227%2C1906%2C2024826%2C2041036%2C2094151%2C2426%2C266265%2C28095%2C28214%2C286730%2C293%2C294%2C51173%2C562%2C67263%2C83428&amp;retmode=xml; Exact NCBI TaxId, ScientificName, rank and alias fields | supports | [{"current": {"aliases": [], "name": "uncultured Bacillus sp.", "other_names": {}, "rank": "species", "tax_id": "83428"}, "emitted": {"association_count": 5, "candidate_pool": 310, "rank": 1, "source": "BACDIVE", "taxon_id": "NCBITaxon:83428", "taxon_label": "uncultured Bacillus sp."}}, {"current": {"aliases": [], "name": "Leifsonia aquatica", "other_names": {"Synonym": "Corynebacterium aquaticum"}, "rank": "species", "tax_id": "144185"}, "emitted": {"association_count": 4, "candidate_pool": 310, "rank": 2, "source": "BACDIVE", "taxon_id": "NCBITaxon:144185", "taxon_label": "Leifsonia aquatica"}}, {"current": {"aliases": [], "name": "Oceanicaulis alexandrii", "other_names": {}, "rank": "species", "tax_id": "153233"}, "emitted": {"association_count": 4, "candidate_pool": 310, "rank": 3, "source": "BACDIVE", "taxon_id": "NCBITaxon:153233", "taxon_label": "Oceanicaulis alexandrii"}}, {"current": {"aliases": [], "name": "Alkaliflexus imshenetskii", "other_names": {}, "rank": "species", "tax_id": "286730"}, "emitted": {"association_count": 4, "candidate_pool": 310, "rank": 4, "source": "BACDIVE", "taxon_id": "NCBITaxon:286730", "taxon_label": "Alkaliflexus imshenetskii"}}, {"current": {"aliases": [], "name": "Stutzerimonas kunmingensis", "other_names": {"Includes": "Pseudomonas sp. HL22-2", "Synonym": "Pseudomonas kunmingensis"}, "rank": "species", "tax_id": "1211807"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank": 5, "source": "BACDIVE", "taxon_id": "NCBITaxon:1211807", "taxon_label": "Stutzerimonas kunmingensis"}}, {"current": {"aliases": [], "name": "Micrococcus luteus", "other_names": {"Includes": "Micrococcus sp. VTT E-072678", "Synonym": "Sarcina lutea"}, "rank": "species", "tax_id": "1270"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank": 6, "source": "BACDIVE", "taxon_id": "NCBITaxon:1270", "taxon_label": "Micrococcus luteus"}}, {"current": {"aliases": [], "name": "Staphylococcus aureus", "other_names": {"Includes": "Staphylococcus sp. Fddn_Aq4", "Synonym": "Staphylococcus pyogenes citreus"}, "rank": "species", "tax_id": "1280"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank": 7, "source": "BACDIVE", "taxon_id": "NCBITaxon:1280", "taxon_label": "Staphylococcus aureus"}}, {"current": {"aliases": [], "name": "Clostridium sp.", "other_names": {"Synonym": "Anaerobacter sp."}, "rank": "species", "tax_id": "1506"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank": 8, "source": "BACDIVE", "taxon_id": "NCBITaxon:1506", "taxon_label": "Clostridium sp."}}, {"current": {"aliases": [], "name": "Sphingomonas sp.", "other_names": {"Synonym": "Rhizomonas sp."}, "rank": "species", "tax_id": "28214"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank": 9, "source": "BACDIVE", "taxon_id": "NCBITaxon:28214", "taxon_label": "Sphingomonas sp."}}, {"current": {"aliases": [], "name": "Pseudomonas fluorescens", "other_names": {"Includes": "bacterium P1-1", "Synonym": "Liquidomonas fluorescens"}, "rank": "species", "tax_id": "294"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank": 10, "source": "BACDIVE", "taxon_id": "NCBITaxon:294", "taxon_label": "Pseudomonas fluorescens"}}, {"current": {"aliases": [], "name": "Escherichia coli", "other_names": {"CommonName": "E. coli", "EquivalentName": "Escherichia/Shigella coli", "Includes": "bacterium E3", "Synonym": "Enterococcus coli"}, "rank": "species", "tax_id": "562"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank": 11, "source": "BACDIVE", "taxon_id": "NCBITaxon:562", "taxon_label": "Escherichia coli"}}, {"current": {"aliases": [], "name": "Streptomyces griseus subsp. griseus", "other_names": {"Synonym": "Nocardia italica"}, "rank": "subspecies", "tax_id": "67263"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank": 12, "source": "BACDIVE", "taxon_id": "NCBITaxon:67263", "taxon_label": "Streptomyces griseus subsp. griseus"}}, {"current": {"aliases": [], "name": "Brevibacillus brevis", "other_names": {"Includes": "Lysinibacillus sp. SDF0063", "Synonym": "Bacillus brevis"}, "rank": "species", "tax_id": "1393"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 13, "source": "BACDIVE", "taxon_id": "NCBITaxon:1393", "taxon_label": "Brevibacillus brevis"}}, {"current": {"aliases": [], "name": "Bacillus licheniformis", "other_names": {"Includes": "Bacillus sp. WED10.6", "Synonym": "Denitrobacillus licheniformis"}, "rank": "species", "tax_id": "1402"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 14, "source": "BACDIVE", "taxon_id": "NCBITaxon:1402", "taxon_label": "Bacillus licheniformis"}}, {"current": {"aliases": [], "name": "Brevibacillus laterosporus", "other_names": {"Includes": "Brevibacillus sp. JP44SK51", "Synonym": "Bacillus laterosporus"}, "rank": "species", "tax_id": "1465"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 15, "source": "BACDIVE", "taxon_id": "NCBITaxon:1465", "taxon_label": "Brevibacillus laterosporus"}}, {"current": {"aliases": [], "name": "Halomonas sp.", "other_names": {}, "rank": "species", "tax_id": "1486246"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 16, "source": "BACDIVE", "taxon_id": "NCBITaxon:1486246", "taxon_label": "Halomonas sp."}}, {"current": {"aliases": [], "name": "Cutibacterium acnes", "other_names": {"Synonym": "Propionibacterium acnes"}, "rank": "species", "tax_id": "1747"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 17, "source": "BACDIVE", "taxon_id": "NCBITaxon:1747", "taxon_label": "Cutibacterium acnes"}}, {"current": {"aliases": [], "name": "bacterium", "other_names": {"Synonym": "unknown bacteria"}, "rank": "species", "tax_id": "1869227"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 18, "source": "BACDIVE", "taxon_id": "NCBITaxon:1869227", "taxon_label": "bacterium"}}, {"current": {"aliases": [], "name": "Streptomyces fradiae", "other_names": {"EquivalentName": "Streptomyces roseiflavus", "Includes": "Streptomyces sp. NEAE-82", "Synonym": "Streptomyces roseoflavus"}, "rank": "species", "tax_id": "1906"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 19, "source": "BACDIVE", "taxon_id": "NCBITaxon:1906", "taxon_label": "Streptomyces fradiae"}}, {"current": {"aliases": [], "name": "Blastopirellula sp.", "other_names": {}, "rank": "species", "tax_id": "2024826"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 20, "source": "BACDIVE", "taxon_id": "NCBITaxon:2024826", "taxon_label": "Blastopirellula sp."}}, {"current": {"aliases": [], "name": "Corynebacterium gottingense", "other_names": {}, "rank": "species", "tax_id": "2041036"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 21, "source": "BACDIVE", "taxon_id": "NCBITaxon:2041036", "taxon_label": "Corynebacterium gottingense"}}, {"current": {"aliases": [], "name": "Paramuribaculum intestinale", "other_names": {"Includes": "Muribaculaceae bacterium DSM 100764"}, "rank": "species", "tax_id": "2094151"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 22, "source": "BACDIVE", "taxon_id": "NCBITaxon:2094151", "taxon_label": "Paramuribaculum intestinale"}}, {"current": {"aliases": [], "name": "Teredinibacter turnerae", "other_names": {"Includes": "Teredinibacter sp. 991H.S.0a.06", "Synonym": "\"Teredinobacter turnerae\" Waterbury et al. 1989"}, "rank": "species", "tax_id": "2426"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 23, "source": "BACDIVE", "taxon_id": "NCBITaxon:2426", "taxon_label": "Teredinibacter turnerae"}}, {"current": {"aliases": [], "name": "Burkholderia gladioli", "other_names": {"Synonym": "Pseudomonas gladioli"}, "rank": "species", "tax_id": "28095"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 24, "source": "BACDIVE", "taxon_id": "NCBITaxon:28095", "taxon_label": "Burkholderia gladioli"}}, {"current": {"aliases": [], "name": "Brevundimonas diminuta", "other_names": {"Synonym": "Pseudomonas diminuta"}, "rank": "species", "tax_id": "293"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank": 25, "source": "BACDIVE", "taxon_id": "NCBITaxon:293", "taxon_label": "Brevundimonas diminuta"}}]. Current names/identifiers do not prove habitat residence or reconstruct original assertions. |
| BACDIVE | https://bacdive.dsmz.de/strain/6213; Isolation source categories and Isolation; inspected public page | context_only | BacDive6213 carries Laboratory/Lab enrichment categories and identifies culture of Alexandrium tamarense as the isolation sample, with taxon153233. It is an example of culture context, not original coverage of all363 strains. |

## Limits And Additional Notes

- Original assertion-level source inputs and original full membership were not reconstructed. Later GOLD counts neither replace frozen counts nor establish original extension.
- Only identified primary passages and first three exact BioSample/Organism descriptions per sheet were scientifically inspected; additional study summaries, if mentioned, are explicitly identified. Census and joins are not complete member-level reviews.
- Sparse qualified source representations can receive a qualified pass without an invented definition, habitat-wide ecological claim or native REVIEWED promotion.
- All required native gates, including full QC, completed successfully on the captured baseline. Optional original-member reconstruction remains unavailable.
- This review does not certify SSSOM/KGX readiness or close shared mapping-contract #1398, ontology-synonym #1249 or deprecated-anchor #1619.
- The full3208-record review goal remains incomplete.
- Historical Markdown reports were leads, not automatically converted reviews. Current user request separately authorizes publication and evidence-supported remediation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T135533Z-laboratory_facility
kind: record
repository: culturebotai/HabitatMech
title: 'Scientific record review: laboratory_facility'
started_at: '2026-10-11T13:19:57.612186Z'
finished_at: '2026-10-11T13:55:33.141533Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Continuing agent participated in prior reviews and curation.
    This is same-agent scientific/adversarial review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The current laboratory-facility identity, research-facility genus and exact
  research laboratory alias are coherent. All 25 displayed NCBI keys resolve with
  their emitted labels. BacDive strain6213 is classified Laboratory/Lab enrichment
  but was isolated from a dinoflagellate culture, demonstrating that Laboratory associations
  include culture provenance rather than proof of residence on facility surfaces.
  Preserve 363 STRAIN assertions, candidate pool310, rank/count semantics and the
  absence of characteristic-presence claims. The original flat category-to-facility
  crosswalk merits bounded reassessment.
source:
  git_revision: 05a328f935a9c9fc37571174fd7c2ac8f2e915f2
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
  - path: curation/causal_graphs/agricultural_soil.yaml
    sha256: 2f9c73b186d6b79df1d64098f929d8364a1768f732101edaf144dee7723c60f4
    role: context
  - path: curation/causal_graphs/aquatic_biome.yaml
    sha256: 03ba09d10f9a9d8d32060fc0208b511ef0d59e731fd7c63ca6c02296e70da5f5
    role: context
  - path: curation/causal_graphs/biofilm.yaml
    sha256: 37fae9d123c2edfb68376b6b4fe5441f72092d48d81dba6f60510087217c8680
    role: context
  - path: curation/causal_graphs/bioreactor.yaml
    sha256: 170d1134c3de38348844e45dbf6d87663dd4a0d1f33fd9e441a4352b6e277583
    role: context
  - path: curation/causal_graphs/brackish_water.yaml
    sha256: b9d58082a53bef1143a3868918cfed7f6d74ba7e2330648069733d9ea2c76508
    role: context
  - path: curation/causal_graphs/building.yaml
    sha256: 9e9360775fdda554b285d7ecfb9b1729bf389b8241376a410eca60bd672eb235
    role: context
  - path: curation/causal_graphs/compost.yaml
    sha256: e0fd3ae54311115939f07ba1f3f158c5c44353bd0fab1dcdc1a9292ff0ad1de5
    role: context
  - path: curation/causal_graphs/deep_marine_sediment.yaml
    sha256: eb6a68290a58ec157a4c9895e082cbba760c47b5fbe35523d3bb163af3091d0c
    role: context
  - path: curation/causal_graphs/forest_soil.yaml
    sha256: faef7b6c26c25ba33110d362dc7e4351440bc08c1106f270e1e6f2decfb1e3f4
    role: context
  - path: curation/causal_graphs/forested_area.yaml
    sha256: eb96b992e1ee8fef7df2550c765a30f0d446082ce16592b6c1da44a54b34e427
    role: context
  - path: curation/causal_graphs/fresh_water.yaml
    sha256: e95ea96aa1912066d4c98cbff91e34528668d4c453d93dc4203c67e7769c691a
    role: context
  - path: curation/causal_graphs/fungi_associated_environment.yaml
    sha256: 45736893315a37e327c25d401ff8794fee47b1056347e52f4980bc3a58e8e0d8
    role: context
  - path: curation/causal_graphs/grassland_soil.yaml
    sha256: 81b2a9ea6255dfbd4b393102b9903dd3c9e8af12f7d3a9adc7c4649650542ae8
    role: context
  - path: curation/causal_graphs/hot_spring.yaml
    sha256: ee0f6d7f7eff179b44e1e934c1c801524062a7e71f3199e16e9ef35e7bad81ed
    role: context
  - path: curation/causal_graphs/hydrothermal_vent.yaml
    sha256: b5c101a93e724531cb7e50e8031203138230c09599855fe8a03bec945469efb0
    role: context
  - path: curation/causal_graphs/hypersaline_water.yaml
    sha256: e974d5e9cc241ac9daf3542ba11156915cfb7786e683ad5ad212af5b35006158
    role: context
  - path: curation/causal_graphs/intestine_environment.yaml
    sha256: 2ef766692eff55471a3322c0cd1cf82188decf37fd5ecd3535cb0ef612e2b725
    role: context
  - path: curation/causal_graphs/leaf.yaml
    sha256: fadc8027b39884bc16cf98f774804a84fd1b1d805876310a47a095f6019435cc
    role: context
  - path: curation/causal_graphs/liquid_water.yaml
    sha256: 12aac1021b9b51c6becc4ef8509bd63557b306e42c01d9b4443d69252ce29a81
    role: context
  - path: curation/causal_graphs/marine_sediment.yaml
    sha256: 8b230eb079171ab8134b648caa29878dc5015fb36362559a6a8c67fb2b433741
    role: context
  - path: curation/causal_graphs/marine_water_body.yaml
    sha256: b2f81102970e9541bf61978fabdd68b7db8f9459f1ef11b467fecfc2956f238b
    role: context
  - path: curation/causal_graphs/milk.yaml
    sha256: 049daa5b499096c61cb625b7bb9ac0f02ea216c96d6b5f7b77126c8709b2378d
    role: context
  - path: curation/causal_graphs/peat_soil.yaml
    sha256: 0f23fa02718b08e3607478ceaa2294320b320ae841a79e144e48ed3497db09e2
    role: context
  - path: curation/causal_graphs/plant_associated_environment.yaml
    sha256: 300044040f76234e7ed3bf373137ba224e55f48e3f3d6d505086b3830877cfcb
    role: context
  - path: curation/causal_graphs/plant_litter.yaml
    sha256: 25e10d6640992be2aa506490f763d8f9642fde125f599207dae7852b6a13b369
    role: context
  - path: curation/causal_graphs/root_nodule.yaml
    sha256: b363e5d418df93d6e44c9d3f3256c8b0ede7c4518125359ffb880020fc00721c
    role: context
  - path: curation/causal_graphs/sea_water.yaml
    sha256: 240ffc8ad2c0abf6f4cce41e01018679aca726816006c90ce329b8d1910d9cd7
    role: context
  - path: curation/causal_graphs/sediment.yaml
    sha256: 62b97afba9466dc64f8b5b1b3fd5d92f8b4b6bf96fe1c761af579ff7deca0e47
    role: context
  - path: curation/causal_graphs/sludge.yaml
    sha256: 55b9c9a27fd00c7b84a8780f2cedc83eeb31ebdda9a2e1029678d96a7fa4a06c
    role: context
  - path: curation/causal_graphs/soil.yaml
    sha256: 2a2bf4b1099b3bc69015f9530cf6e926c05c33667132234b3c52f06aacc957c2
    role: context
  - path: curation/causal_graphs/terrestrial_biome.yaml
    sha256: 239e6a2b711564ed12084cddd1295547d23858dd329c33c538251d5f53c88834
    role: context
  - path: curation/causal_graphs/waste_water.yaml
    sha256: 299b5128af6cf5f7a61ce53304f1084e6eb045414b47cbcfd8832de095142aef
    role: context
  - path: curation/decisions.tsv
    sha256: c2482c7441b08f593baa8bd59546ac68c6e5c7e4e1cb36c24c12a74592b9ff3c
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: a87f36bd01c0b5bf2ba5cd995fb7b83a294a04f94512fcdf29d02c648d302731
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
  - path: data/habitats/engineered/laboratory_facility.yaml
    sha256: cc19ad4854d14143068b181d815f4d7a26ba3638bc1ed9b6fd3bc3f1ef4a0cbc
    role: target
  - path: data/habitats/engineered/research_facility.yaml
    sha256: 506dd0b31a4299e62764461725a2e69718b3a7963b7e7069aa8e1af5a2714575
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
  - path: reports/yaml_record_review/20261009T025934Z-laboratory_facility.md
    sha256: 4671a98b9b0c3a8e6bf05632c69d37fa26ab7d275e12e763003010a5527355ff
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
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
scope:
  description: Entire exact HabitatRecord, source contributors, direct-parent context
    and applicable biological evidence.
  selection: Next 24 alphabetically ordered unreviewed ENGINEERED records, indoor
    through manure. Each receives a separate full exact-target review. No category-wide
    scientific verdict or claim that other categories are reviewed. Starting completed-observation
    coverage351/3208; not a clean/currentness percentage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:01001406
  exclusions:
  - target: Other3207 current HabitatRecords
    reason: Contextual parent/source reads are not additional completed record reviews.
targets:
- target_id: ENVO:01001406
  path: data/habitats/engineered/laboratory_facility.yaml
  label: laboratory facility
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Exact source-concept identity and grounding decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded immediate GOLD source-parent contributions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definition and genus
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology identity, label, definition and synonym inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology subclass inventory
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained harmonization and deterministic generation
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_isolation_sources.tsv
    role: BacDive source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: BacDive source-taxon strain associations
checks:
- check_id: C18
  name: Native just validate
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T13:21:14.168855Z; finish 2026-10-11T13:21:19.859041Z.
    Full-corpus gates do not imply additional scientific record coverage.
  target_ids:
  - ENVO:01001406
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=05a328f935a9c9fc37571174fd7c2ac8f2e915f2
    just validate data/habitats/engineered/laboratory_facility.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C24
  name: Native just validate-strict
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T13:21:39.998009Z; finish 2026-10-11T13:21:50.571500Z.
    Full-corpus gates do not imply additional scientific record coverage.
  target_ids:
  - ENVO:01001406
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=05a328f935a9c9fc37571174fd7c2ac8f2e915f2
    just validate-strict data/habitats/engineered/indoor.yaml data/habitats/engineered/industrial_production__f961ebd0.yaml
    data/habitats/engineered/industrial_waste_material.yaml data/habitats/engineered/industrial_wastewater.yaml
    data/habitats/engineered/influent.yaml data/habitats/engineered/inoculum.yaml
    data/habitats/engineered/input_fracking_water.yaml data/habitats/engineered/insectarium.yaml
    data/habitats/engineered/intensive_care_unit_facility.yaml data/habitats/engineered/interior_wall.yaml
    data/habitats/engineered/interstitial_water.yaml data/habitats/engineered/irrigation_canal.yaml
    data/habitats/engineered/kitchen_sink.yaml data/habitats/engineered/lab_culture.yaml
    data/habitats/engineered/lab_enrichment__ef29994d.yaml data/habitats/engineered/lab_grade_water.yaml
    data/habitats/engineered/laboratory_developed.yaml data/habitats/engineered/laboratory_environment.yaml
    data/habitats/engineered/laboratory_facility.yaml data/habitats/engineered/lake_water.yaml
    data/habitats/engineered/landfill.yaml data/habitats/engineered/landfill_leachate.yaml
    data/habitats/engineered/leachate__6407848f.yaml data/habitats/engineered/manure.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C25
  name: Native just verify-corpus
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T13:21:50.572551Z; finish 2026-10-11T13:22:22.018901Z.
    Full-corpus gates do not imply additional scientific record coverage.
  target_ids:
  - ENVO:01001406
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=05a328f935a9c9fc37571174fd7c2ac8f2e915f2
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C26
  name: Native just validate-products
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T13:22:22.020180Z; finish 2026-10-11T13:23:56.625048Z.
    Full-corpus gates do not imply additional scientific record coverage.
  target_ids:
  - ENVO:01001406
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=05a328f935a9c9fc37571174fd7c2ac8f2e915f2
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C27
  name: Native just validate-history
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T13:23:56.626020Z; finish 2026-10-11T13:24:06.431983Z.
    Full-corpus gates do not imply additional scientific record coverage.
  target_ids:
  - ENVO:01001406
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=05a328f935a9c9fc37571174fd7c2ac8f2e915f2
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C28
  name: Native just validate-causal-all
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T13:24:06.433302Z; finish 2026-10-11T13:24:12.572770Z.
    Full-corpus gates do not imply additional scientific record coverage.
  target_ids:
  - ENVO:01001406
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=05a328f935a9c9fc37571174fd7c2ac8f2e915f2
    just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C29
  name: Native just term-requests-check
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T13:24:12.573784Z; finish 2026-10-11T13:24:40.630469Z.
    Full-corpus gates do not imply additional scientific record coverage.
  target_ids:
  - ENVO:01001406
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=05a328f935a9c9fc37571174fd7c2ac8f2e915f2
    just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C30
  name: Native just qc
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T13:24:40.631657Z; finish 2026-10-11T13:54:31.642833Z.
    Full-corpus gates do not imply additional scientific record coverage.
  target_ids:
  - ENVO:01001406
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=05a328f935a9c9fc37571174fd7c2ac8f2e915f2
    just qc
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: REPRO
  name: Complete target reproduction
  status: passed
  required: false
  summary: Fresh native build_document equals all fields of each of the 24 targets.
  target_ids:
  - ENVO:01001406
  command: .venv/bin/python /private/tmp/habitatmech-review-ar-local.py
  exit_code: 0
  evidence_ids:
  - CODE
- check_id: ORIGINAL
  name: Original member/assertion reconstruction
  status: unavailable
  required: false
  summary: Original configured upstream input files were not recovered within the
    ignored-inclusive search bounds. Later exports are separate evidence.
  target_ids:
  - ENVO:01001406
  evidence_ids:
  - SEARCH
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/engineered/laboratory_facility.yaml
  summary: The current laboratory-facility identity, research-facility genus and exact
    research laboratory alias are coherent. All 25 displayed NCBI keys resolve with
    their emitted labels. BacDive strain6213 is classified Laboratory/Lab enrichment
    but was isolated from a dinoflagellate culture, demonstrating that Laboratory
    associations include culture provenance rather than proof of residence on facility
    surfaces. Preserve 363 STRAIN assertions, candidate pool310, rank/count semantics
    and the absence of characteristic-presence claims. The original flat category-to-facility
    crosswalk merits bounded reassessment.
  locator: Entire generated YAML, including all histories, synonyms, sources and taxa
  accessed_at: '2026-10-11T13:55:33.141533Z'
  support: supports
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md
  summary: Applied the native identity, strict-parent, source-unit, ITEM status, observational-taxon,
    triad-role and causal-evidence rubric. Optional absent fields are not automatically
    defects.
  locator: Complete local review checklist and maintained ownership
  accessed_at: '2026-10-11T13:55:33.141533Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5",
    "date": "2026-08-16", "decision": "REVIEW", "grounding_status": "", "identifier":
    "habitatmech:BACDIVE.3582899e36", "notes": "CLOSE-grounding review (#12): read
    against the full source path and the term''s own definition. The grounding is
    right and CLOSE is the honest status \u2014 the term is the concept with a difference
    of framing or specificity that EXACT would overstate.", "object_id": "", "object_label":
    "", "relation": "", "review_depth": "ITEM"}, "logical_row": 1746}], "data/raw/bacdive_isolation_sources.tsv":
    [{"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "label": "Laboratory",
    "source_slug": "laboratory", "strain_count": "363", "taxon_count": "310"}, "logical_row":
    41}], "data/raw/bacdive_source_taxa.tsv": [{"data": {"bacdive_id": "bacdive.isolation_source:laboratory",
    "corroborated_by": "", "rank": "1", "strain_count": "5", "taxon_id": "NCBITaxon:83428",
    "taxon_label": "uncultured Bacillus sp."}, "logical_row": 1599}, {"data": {"bacdive_id":
    "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "2", "strain_count":
    "4", "taxon_id": "NCBITaxon:144185", "taxon_label": "Leifsonia aquatica"}, "logical_row":
    1600}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by":
    "", "rank": "3", "strain_count": "4", "taxon_id": "NCBITaxon:153233", "taxon_label":
    "Oceanicaulis alexandrii"}, "logical_row": 1601}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory",
    "corroborated_by": "", "rank": "4", "strain_count": "4", "taxon_id": "NCBITaxon:286730",
    "taxon_label": "Alkaliflexus imshenetskii"}, "logical_row": 1602}, {"data": {"bacdive_id":
    "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "5", "strain_count":
    "3", "taxon_id": "NCBITaxon:1211807", "taxon_label": "Stutzerimonas kunmingensis"},
    "logical_row": 1603}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory",
    "corroborated_by": "", "rank": "6", "strain_count": "3", "taxon_id": "NCBITaxon:1270",
    "taxon_label": "Micrococcus luteus"}, "logical_row": 1604}, {"data": {"bacdive_id":
    "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "7", "strain_count":
    "3", "taxon_id": "NCBITaxon:1280", "taxon_label": "Staphylococcus aureus"}, "logical_row":
    1605}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by":
    "", "rank": "8", "strain_count": "3", "taxon_id": "NCBITaxon:1506", "taxon_label":
    "Clostridium sp."}, "logical_row": 1606}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory",
    "corroborated_by": "", "rank": "9", "strain_count": "3", "taxon_id": "NCBITaxon:28214",
    "taxon_label": "Sphingomonas sp."}, "logical_row": 1607}, {"data": {"bacdive_id":
    "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "10", "strain_count":
    "3", "taxon_id": "NCBITaxon:294", "taxon_label": "Pseudomonas fluorescens"}, "logical_row":
    1608}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by":
    "", "rank": "11", "strain_count": "3", "taxon_id": "NCBITaxon:562", "taxon_label":
    "Escherichia coli"}, "logical_row": 1609}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory",
    "corroborated_by": "", "rank": "12", "strain_count": "3", "taxon_id": "NCBITaxon:67263",
    "taxon_label": "Streptomyces griseus subsp. griseus"}, "logical_row": 1610}, {"data":
    {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank":
    "13", "strain_count": "2", "taxon_id": "NCBITaxon:1393", "taxon_label": "Brevibacillus
    brevis"}, "logical_row": 1611}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory",
    "corroborated_by": "", "rank": "14", "strain_count": "2", "taxon_id": "NCBITaxon:1402",
    "taxon_label": "Bacillus licheniformis"}, "logical_row": 1612}, {"data": {"bacdive_id":
    "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "15", "strain_count":
    "2", "taxon_id": "NCBITaxon:1465", "taxon_label": "Brevibacillus laterosporus"},
    "logical_row": 1613}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory",
    "corroborated_by": "", "rank": "16", "strain_count": "2", "taxon_id": "NCBITaxon:1486246",
    "taxon_label": "Halomonas sp."}, "logical_row": 1614}, {"data": {"bacdive_id":
    "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "17", "strain_count":
    "2", "taxon_id": "NCBITaxon:1747", "taxon_label": "Cutibacterium acnes"}, "logical_row":
    1615}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by":
    "", "rank": "18", "strain_count": "2", "taxon_id": "NCBITaxon:1869227", "taxon_label":
    "bacterium"}, "logical_row": 1616}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory",
    "corroborated_by": "", "rank": "19", "strain_count": "2", "taxon_id": "NCBITaxon:1906",
    "taxon_label": "Streptomyces fradiae"}, "logical_row": 1617}, {"data": {"bacdive_id":
    "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "20", "strain_count":
    "2", "taxon_id": "NCBITaxon:2024826", "taxon_label": "Blastopirellula sp."}, "logical_row":
    1618}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by":
    "", "rank": "21", "strain_count": "2", "taxon_id": "NCBITaxon:2041036", "taxon_label":
    "Corynebacterium gottingense"}, "logical_row": 1619}, {"data": {"bacdive_id":
    "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "22", "strain_count":
    "2", "taxon_id": "NCBITaxon:2094151", "taxon_label": "Paramuribaculum intestinale"},
    "logical_row": 1620}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory",
    "corroborated_by": "", "rank": "23", "strain_count": "2", "taxon_id": "NCBITaxon:2426",
    "taxon_label": "Teredinibacter turnerae"}, "logical_row": 1621}, {"data": {"bacdive_id":
    "bacdive.isolation_source:laboratory", "corroborated_by": "", "rank": "24", "strain_count":
    "2", "taxon_id": "NCBITaxon:28095", "taxon_label": "Burkholderia gladioli"}, "logical_row":
    1622}, {"data": {"bacdive_id": "bacdive.isolation_source:laboratory", "corroborated_by":
    "", "rank": "25", "strain_count": "2", "taxon_id": "NCBITaxon:293", "taxon_label":
    "Brevundimonas diminuta"}, "logical_row": 1623}], "data/raw/isolation_source_groundings.tsv":
    [{"data": {"confidence": "medium", "curator": "ols4_auto", "mapping_justification":
    "semapv:LexicalMatching", "object_id": "ENVO:01001406", "object_label": "laboratory
    facility", "object_source": "ENVO", "predicate_id": "skos:closeMatch", "source_dataset":
    "bacdive", "subject_label": "Laboratory", "subject_label_normalized": "laboratory",
    "verified_date": "2026-05-01"}, "logical_row": 173}], "data/raw/ontology_terms.tsv":
    [{"data": {"definition": "A facility, permanent or temporary, on land, in air,
    space or water, where scientific research or measurements can be undertaken.",
    "deprecated": "", "directly_referenced": "TRUE", "label": "research facility",
    "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id": "ENVO:00000469"},
    "logical_row": 7046}, {"data": {"definition": "A research facility in which systems
    of manufactured products control internal conditions and in which scientific or
    technological research, experiments, and measurement may be performed.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "laboratory facility", "label_only":
    "FALSE", "ontology": "ENVO", "synonyms": "research laboratory", "term_id": "ENVO:01001406"},
    "logical_row": 8893}]}. Logical TSV row ordinals include header. Related-record
    hits were filtered, not treated as target evidence.'
  locator: Exact source/mint/path rows, current decision and guarded exclusion contributions
  accessed_at: '2026-10-11T13:55:33.141533Z'
  support: supports
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 1, "routes": [], "source_concepts": 1}. A fresh native
    build_document equals every target field; executed routes do not independently
    prove scientific equivalence.'
  locator: Complete target reconstruction; actual resolve_gold/apply_decision routes
  accessed_at: '2026-10-11T13:55:33.141533Z'
  support: supports
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl
  summary: '{"ENVO:00000469": {"comments": [], "definitions": ["A facility, permanent
    or temporary, on land, in air, space or water, where scientific research or measurements
    can be undertaken."], "deprecated": [], "equivalents": [], "identifier": "ENVO:00000469",
    "labels": ["research facility"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000070"],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [],
    "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:01001406": {"comments":
    [], "definitions": ["A research facility in which systems of manufactured products
    control internal conditions and in which scientific or technological research,
    experiments, and measurement may be performed."], "deprecated": [], "equivalents":
    [], "identifier": "ENVO:01001406", "labels": ["laboratory facility"], "parents":
    ["http://purl.obolibrary.org/obo/ENVO_00000469", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/BFO_0000051"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_01001405"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": [], "hasExactSynonym": ["research laboratory"], "hasNarrowSynonym":
    [], "hasRelatedSynonym": []}}}. Typed current ontology meaning is not itself proof
    of an exact GOLD crosswalk.'
  locator: Exact labels, definitions, deprecation, synonym scopes and OWL parent/restriction
    axioms
  accessed_at: '2026-10-11T13:21:47.927208Z'
  support: supports
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats; data/raw/ontology_subclass_edges.tsv
  summary: '{"ENVO:00000469": {"definition": "A facility, permanent or temporary,
    on land, in air, space or water, where scientific research or measurements can
    be undertaken.", "identifier": "ENVO:00000469", "label": "research facility",
    "parent_habitats": ["ENVO:00000070"], "source_attestations": [{"assertion_count":
    339, "assertion_unit": "TAXON", "evidence_channels": "environmental_samples",
    "score": 1.75033, "source": "PREGO", "source_id": "ENVO:00000469", "source_label":
    "research facility"}]}}. Parent identity/source context only, not extra full-record
    coverage.'
  locator: Direct-parent definition and relation projection
  accessed_at: '2026-10-11T13:55:33.141533Z'
  support: supports
- evidence_id: SEARCH
  kind: search
  reference: curation; data/raw; data/habitats; history; research; reports; reviews;
    conf
  summary: 'Ignored/hidden-inclusive rg searched IDs, labels, slugs, source IDs and
    paths. Structured raw/curation rows and prior review target/finding identities
    were also scanned. No prior structured review assessed this exact target at capture.
    Original configured inputs: {"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe",
    "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv",
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
    "exit_code": 0, "matches": [], "stderr": ""}]}. Configured-path/file-name misses
    are bounded, not global absence.'
  locator: Exact-ID review census and ignored-inclusive source/support searches
  accessed_at: '2026-10-11T13:55:33.141533Z'
  support: supports
  search_scope: 'Ignored/hidden-inclusive rg searched IDs, labels, slugs, source IDs
    and paths. Structured raw/curation rows and prior review target/finding identities
    were also scanned. No prior structured review assessed this exact target at capture.
    Original configured inputs: {"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe",
    "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv",
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
    "exit_code": 0, "matches": [], "stderr": ""}]}. Configured-path/file-name misses
    are bounded, not global absence.'
- evidence_id: TAXA
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1132443%2C1211807%2C1270%2C1280%2C1385515%2C1393%2C1402%2C144185%2C1465%2C1486246%2C1506%2C153233%2C1549639%2C1747%2C1869227%2C1906%2C2024826%2C2041036%2C2094151%2C2426%2C266265%2C28095%2C28214%2C286730%2C293%2C294%2C51173%2C562%2C67263%2C83428&retmode=xml
  summary: '[{"current": {"aliases": [], "name": "uncultured Bacillus sp.", "other_names":
    {}, "rank": "species", "tax_id": "83428"}, "emitted": {"association_count": 5,
    "candidate_pool": 310, "rank": 1, "source": "BACDIVE", "taxon_id": "NCBITaxon:83428",
    "taxon_label": "uncultured Bacillus sp."}}, {"current": {"aliases": [], "name":
    "Leifsonia aquatica", "other_names": {"Synonym": "Corynebacterium aquaticum"},
    "rank": "species", "tax_id": "144185"}, "emitted": {"association_count": 4, "candidate_pool":
    310, "rank": 2, "source": "BACDIVE", "taxon_id": "NCBITaxon:144185", "taxon_label":
    "Leifsonia aquatica"}}, {"current": {"aliases": [], "name": "Oceanicaulis alexandrii",
    "other_names": {}, "rank": "species", "tax_id": "153233"}, "emitted": {"association_count":
    4, "candidate_pool": 310, "rank": 3, "source": "BACDIVE", "taxon_id": "NCBITaxon:153233",
    "taxon_label": "Oceanicaulis alexandrii"}}, {"current": {"aliases": [], "name":
    "Alkaliflexus imshenetskii", "other_names": {}, "rank": "species", "tax_id": "286730"},
    "emitted": {"association_count": 4, "candidate_pool": 310, "rank": 4, "source":
    "BACDIVE", "taxon_id": "NCBITaxon:286730", "taxon_label": "Alkaliflexus imshenetskii"}},
    {"current": {"aliases": [], "name": "Stutzerimonas kunmingensis", "other_names":
    {"Includes": "Pseudomonas sp. HL22-2", "Synonym": "Pseudomonas kunmingensis"},
    "rank": "species", "tax_id": "1211807"}, "emitted": {"association_count": 3, "candidate_pool":
    310, "rank": 5, "source": "BACDIVE", "taxon_id": "NCBITaxon:1211807", "taxon_label":
    "Stutzerimonas kunmingensis"}}, {"current": {"aliases": [], "name": "Micrococcus
    luteus", "other_names": {"Includes": "Micrococcus sp. VTT E-072678", "Synonym":
    "Sarcina lutea"}, "rank": "species", "tax_id": "1270"}, "emitted": {"association_count":
    3, "candidate_pool": 310, "rank": 6, "source": "BACDIVE", "taxon_id": "NCBITaxon:1270",
    "taxon_label": "Micrococcus luteus"}}, {"current": {"aliases": [], "name": "Staphylococcus
    aureus", "other_names": {"Includes": "Staphylococcus sp. Fddn_Aq4", "Synonym":
    "Staphylococcus pyogenes citreus"}, "rank": "species", "tax_id": "1280"}, "emitted":
    {"association_count": 3, "candidate_pool": 310, "rank": 7, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:1280", "taxon_label": "Staphylococcus aureus"}}, {"current":
    {"aliases": [], "name": "Clostridium sp.", "other_names": {"Synonym": "Anaerobacter
    sp."}, "rank": "species", "tax_id": "1506"}, "emitted": {"association_count":
    3, "candidate_pool": 310, "rank": 8, "source": "BACDIVE", "taxon_id": "NCBITaxon:1506",
    "taxon_label": "Clostridium sp."}}, {"current": {"aliases": [], "name": "Sphingomonas
    sp.", "other_names": {"Synonym": "Rhizomonas sp."}, "rank": "species", "tax_id":
    "28214"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank": 9,
    "source": "BACDIVE", "taxon_id": "NCBITaxon:28214", "taxon_label": "Sphingomonas
    sp."}}, {"current": {"aliases": [], "name": "Pseudomonas fluorescens", "other_names":
    {"Includes": "bacterium P1-1", "Synonym": "Liquidomonas fluorescens"}, "rank":
    "species", "tax_id": "294"}, "emitted": {"association_count": 3, "candidate_pool":
    310, "rank": 10, "source": "BACDIVE", "taxon_id": "NCBITaxon:294", "taxon_label":
    "Pseudomonas fluorescens"}}, {"current": {"aliases": [], "name": "Escherichia
    coli", "other_names": {"CommonName": "E. coli", "EquivalentName": "Escherichia/Shigella
    coli", "Includes": "bacterium E3", "Synonym": "Enterococcus coli"}, "rank": "species",
    "tax_id": "562"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank":
    11, "source": "BACDIVE", "taxon_id": "NCBITaxon:562", "taxon_label": "Escherichia
    coli"}}, {"current": {"aliases": [], "name": "Streptomyces griseus subsp. griseus",
    "other_names": {"Synonym": "Nocardia italica"}, "rank": "subspecies", "tax_id":
    "67263"}, "emitted": {"association_count": 3, "candidate_pool": 310, "rank": 12,
    "source": "BACDIVE", "taxon_id": "NCBITaxon:67263", "taxon_label": "Streptomyces
    griseus subsp. griseus"}}, {"current": {"aliases": [], "name": "Brevibacillus
    brevis", "other_names": {"Includes": "Lysinibacillus sp. SDF0063", "Synonym":
    "Bacillus brevis"}, "rank": "species", "tax_id": "1393"}, "emitted": {"association_count":
    2, "candidate_pool": 310, "rank": 13, "source": "BACDIVE", "taxon_id": "NCBITaxon:1393",
    "taxon_label": "Brevibacillus brevis"}}, {"current": {"aliases": [], "name": "Bacillus
    licheniformis", "other_names": {"Includes": "Bacillus sp. WED10.6", "Synonym":
    "Denitrobacillus licheniformis"}, "rank": "species", "tax_id": "1402"}, "emitted":
    {"association_count": 2, "candidate_pool": 310, "rank": 14, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:1402", "taxon_label": "Bacillus licheniformis"}}, {"current":
    {"aliases": [], "name": "Brevibacillus laterosporus", "other_names": {"Includes":
    "Brevibacillus sp. JP44SK51", "Synonym": "Bacillus laterosporus"}, "rank": "species",
    "tax_id": "1465"}, "emitted": {"association_count": 2, "candidate_pool": 310,
    "rank": 15, "source": "BACDIVE", "taxon_id": "NCBITaxon:1465", "taxon_label":
    "Brevibacillus laterosporus"}}, {"current": {"aliases": [], "name": "Halomonas
    sp.", "other_names": {}, "rank": "species", "tax_id": "1486246"}, "emitted": {"association_count":
    2, "candidate_pool": 310, "rank": 16, "source": "BACDIVE", "taxon_id": "NCBITaxon:1486246",
    "taxon_label": "Halomonas sp."}}, {"current": {"aliases": [], "name": "Cutibacterium
    acnes", "other_names": {"Synonym": "Propionibacterium acnes"}, "rank": "species",
    "tax_id": "1747"}, "emitted": {"association_count": 2, "candidate_pool": 310,
    "rank": 17, "source": "BACDIVE", "taxon_id": "NCBITaxon:1747", "taxon_label":
    "Cutibacterium acnes"}}, {"current": {"aliases": [], "name": "bacterium", "other_names":
    {"Synonym": "unknown bacteria"}, "rank": "species", "tax_id": "1869227"}, "emitted":
    {"association_count": 2, "candidate_pool": 310, "rank": 18, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:1869227", "taxon_label": "bacterium"}}, {"current": {"aliases":
    [], "name": "Streptomyces fradiae", "other_names": {"EquivalentName": "Streptomyces
    roseiflavus", "Includes": "Streptomyces sp. NEAE-82", "Synonym": "Streptomyces
    roseoflavus"}, "rank": "species", "tax_id": "1906"}, "emitted": {"association_count":
    2, "candidate_pool": 310, "rank": 19, "source": "BACDIVE", "taxon_id": "NCBITaxon:1906",
    "taxon_label": "Streptomyces fradiae"}}, {"current": {"aliases": [], "name": "Blastopirellula
    sp.", "other_names": {}, "rank": "species", "tax_id": "2024826"}, "emitted": {"association_count":
    2, "candidate_pool": 310, "rank": 20, "source": "BACDIVE", "taxon_id": "NCBITaxon:2024826",
    "taxon_label": "Blastopirellula sp."}}, {"current": {"aliases": [], "name": "Corynebacterium
    gottingense", "other_names": {}, "rank": "species", "tax_id": "2041036"}, "emitted":
    {"association_count": 2, "candidate_pool": 310, "rank": 21, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:2041036", "taxon_label": "Corynebacterium gottingense"}},
    {"current": {"aliases": [], "name": "Paramuribaculum intestinale", "other_names":
    {"Includes": "Muribaculaceae bacterium DSM 100764"}, "rank": "species", "tax_id":
    "2094151"}, "emitted": {"association_count": 2, "candidate_pool": 310, "rank":
    22, "source": "BACDIVE", "taxon_id": "NCBITaxon:2094151", "taxon_label": "Paramuribaculum
    intestinale"}}, {"current": {"aliases": [], "name": "Teredinibacter turnerae",
    "other_names": {"Includes": "Teredinibacter sp. 991H.S.0a.06", "Synonym": "\"Teredinobacter
    turnerae\" Waterbury et al. 1989"}, "rank": "species", "tax_id": "2426"}, "emitted":
    {"association_count": 2, "candidate_pool": 310, "rank": 23, "source": "BACDIVE",
    "taxon_id": "NCBITaxon:2426", "taxon_label": "Teredinibacter turnerae"}}, {"current":
    {"aliases": [], "name": "Burkholderia gladioli", "other_names": {"Synonym": "Pseudomonas
    gladioli"}, "rank": "species", "tax_id": "28095"}, "emitted": {"association_count":
    2, "candidate_pool": 310, "rank": 24, "source": "BACDIVE", "taxon_id": "NCBITaxon:28095",
    "taxon_label": "Burkholderia gladioli"}}, {"current": {"aliases": [], "name":
    "Brevundimonas diminuta", "other_names": {"Synonym": "Pseudomonas diminuta"},
    "rank": "species", "tax_id": "293"}, "emitted": {"association_count": 2, "candidate_pool":
    310, "rank": 25, "source": "BACDIVE", "taxon_id": "NCBITaxon:293", "taxon_label":
    "Brevundimonas diminuta"}}]. Current names/identifiers do not prove habitat residence
    or reconstruct original assertions.'
  locator: Exact NCBI TaxId, ScientificName, rank and alias fields
  accessed_at: '2026-10-11T13:21:56.605933Z'
  support: supports
  snapshot_sha256: d0313e30d3a8b2cf121a6d06c8d676dd9e7214622edc9a35c04aac23e121ce7b
- evidence_id: BACDIVE
  kind: database
  reference: https://bacdive.dsmz.de/strain/6213
  summary: BacDive6213 carries Laboratory/Lab enrichment categories and identifies
    culture of Alexandrium tamarense as the isolation sample, with taxon153233. It
    is an example of culture context, not original coverage of all363 strains.
  locator: Isolation source categories and Isolation; inspected public page
  accessed_at: '2026-10-11T13:28:49.504937Z'
  support: context_only
  snapshot_sha256: 993f85b7511ed697cee48f5949350fda33ca85204a7a3acd0dee730cdebf30c9
assessments:
- assessment_id: TAXON
  area: evidence
  topic: Reported-from taxonomy, source units and ranks
  outcome: supported
  summary: The current laboratory-facility identity, research-facility genus and exact
    research laboratory alias are coherent. All 25 displayed NCBI keys resolve with
    their emitted labels. BacDive strain6213 is classified Laboratory/Lab enrichment
    but was isolated from a dinoflagellate culture, demonstrating that Laboratory
    associations include culture provenance rather than proof of residence on facility
    surfaces. Preserve 363 STRAIN assertions, candidate pool310, rank/count semantics
    and the absence of characteristic-presence claims. The original flat category-to-facility
    crosswalk merits bounded reassessment. No is_characteristic field is present;
    source ranks and association scores are not prevalence.
  target_ids:
  - ENVO:01001406
  evidence_ids:
  - R
  - RAW
  - TAXA
- assessment_id: IDENTITY
  area: identity
  topic: Identity, grounding, hierarchy, synonyms and source scope
  outcome: concern
  summary: The current laboratory-facility identity, research-facility genus and exact
    research laboratory alias are coherent. All 25 displayed NCBI keys resolve with
    their emitted labels. BacDive strain6213 is classified Laboratory/Lab enrichment
    but was isolated from a dinoflagellate culture, demonstrating that Laboratory
    associations include culture provenance rather than proof of residence on facility
    surfaces. Preserve 363 STRAIN assertions, candidate pool310, rank/count semantics
    and the absence of characteristic-presence claims. The original flat category-to-facility
    crosswalk merits bounded reassessment.
  target_ids:
  - ENVO:01001406
  evidence_ids:
  - R
  - RULES
  - RAW
  - CODE
  - ONT
  - PARENT
  - BACDIVE
- assessment_id: PROVENANCE
  area: provenance
  topic: Frozen source units and generated lifecycle
  outcome: supported
  summary: All emitted fields reproduce. Exact maintained source rows preserve count
    units, collapsed nodes and source roles; zero-count omission does not mean no
    organisms. Source/reviewed-contributor counts=1/1. Actual routes are recorded
    in CODE. Scientific review does not promote native status or update frozen counts
    from later evidence.
  target_ids:
  - ENVO:01001406
  evidence_ids:
  - R
  - RAW
  - CODE
- assessment_id: COMPLETENESS
  area: completeness
  topic: Claims proportional to evidence
  outcome: supported
  summary: The full target contains no causal graph, gene/regulator or transcriptomic
    claim; iModulonDB is not applicable. No optional definition, parameter, mechanism,
    taxon or discussion is invented. Triad broad/local/medium roles remain contextual
    and source-specific.
  target_ids:
  - ENVO:01001406
  evidence_ids:
  - R
  - RAW
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: envo-01001406-source-entity-scope
  category: provenance
  severity: minor
  status: open
  certainty: provisional
  title: Original source entity and scope require bounded reassessment
  description: The current laboratory-facility identity, research-facility genus and
    exact research laboratory alias are coherent. All 25 displayed NCBI keys resolve
    with their emitted labels. BacDive strain6213 is classified Laboratory/Lab enrichment
    but was isolated from a dinoflagellate culture, demonstrating that Laboratory
    associations include culture provenance rather than proof of residence on facility
    surfaces. Preserve 363 STRAIN assertions, candidate pool310, rank/count semantics
    and the absence of characteristic-presence claims. The original flat category-to-facility
    crosswalk merits bounded reassessment.
  target_ids:
  - ENVO:01001406
  field_paths:
  - source_attestations
  - curation_history
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
  - BACDIVE
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Bounded display or source-scope gap without demonstrated wrong
    identity.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Evidence-backed ITEM source assessment
actions:
- action_id: A1
  description: Recover original category/member scope or an independently inspectable
    crosswalk; distinguish sample material, development/treatment activity and physical
    setting. Later members inform but do not replace frozen membership. Curate only
    supported changes, preserve ambiguity otherwise, and do not force optional fields
    or native status promotion.
  finding_ids:
  - F1
  target_ids:
  - ENVO:01001406
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Evidence-backed ITEM source assessment
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Use inspected primary evidence and the exact source path; preserve uncertainty
    rather than invent a replacement identity.
  - Preserve count/unit semantics, source provenance and immutable histories/reviews;
    append native history for a supported curation change.
  - Add exact-scope regressions, inspect a dry seed and canary, regenerate governed
    artifacts and pass labels, strict validation, provenance, reproduction, history
    and full QC.
limitations:
- Original assertion-level source inputs and original full membership were not reconstructed.
  Later GOLD counts neither replace frozen counts nor establish original extension.
- Only identified primary passages and first three exact BioSample/Organism descriptions
  per sheet were scientifically inspected; additional study summaries, if mentioned,
  are explicitly identified. Census and joins are not complete member-level reviews.
- Sparse qualified source representations can receive a qualified pass without an
  invented definition, habitat-wide ecological claim or native REVIEWED promotion.
- All required native gates, including full QC, completed successfully on the captured
  baseline. Optional original-member reconstruction remains unavailable.
- 'This review does not certify SSSOM/KGX readiness or close shared mapping-contract
  #1398, ontology-synonym #1249 or deprecated-anchor #1619.'
notes:
- The full3208-record review goal remains incomplete.
- Historical Markdown reports were leads, not automatically converted reviews. Current
  user request separately authorizes publication and evidence-supported remediation.
tags:
- habitatmech
- engineered
- record-review
- scientific-review
```
