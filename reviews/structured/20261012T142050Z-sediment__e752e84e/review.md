# Scientific record review: sediment__e752e84e

- Review: 20261012T142050Z-sediment__e752e84e
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-12T14:06:31.267477Z
- Finished UTC: 2026-10-12T14:20:50.366259Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Non-marine saline sediment is material, not the saline water body ENVO:01001319. Later examples mix lagoon sediment and halocline water and contain conflicting habitat labels; preserve these source tensions rather than silently reclassify all 37 frozen ORGANISM assertions.

## Scope And Provenance

One complete resolved record and every contributing source concept, with bounded external authority checks.

Selection: Next forty records lacking a completed individual scientific review in stable repository-relative path order. Each target is assessed separately; this does not establish category-wide scientific correctness. Initial coverage 888/3208.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base eb542f67c8c29c7277da72aae9630bd0b09eacf5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.1f5f4fee4c | data/habitats/aquatic/sediment__e752e84e.yaml | generated | Sediment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validation | passed | True | habitatmech:GOLD.1f5f4fee4c | Actual success 2026-10-12T14:08:14.986773Z to 2026-10-12T14:08:16.531247Z. Native command scope retained. |
| Native validation | passed | True | habitatmech:GOLD.1f5f4fee4c | Actual success 2026-10-12T14:09:22.255456Z to 2026-10-12T14:09:28.022961Z. Native command scope retained. |
| Native validation | passed | True | habitatmech:GOLD.1f5f4fee4c | Actual success 2026-10-12T14:09:28.023817Z to 2026-10-12T14:09:49.221540Z. Native command scope retained. |
| Native validation | passed | True | habitatmech:GOLD.1f5f4fee4c | Actual success 2026-10-12T14:09:49.224222Z to 2026-10-12T14:10:29.408992Z. Native command scope retained. |
| Native validation | passed | True | habitatmech:GOLD.1f5f4fee4c | Actual success 2026-10-12T14:10:29.409728Z to 2026-10-12T14:10:35.671227Z. Native command scope retained. |
| Native validation | passed | True | habitatmech:GOLD.1f5f4fee4c | Actual success 2026-10-12T14:10:35.672699Z to 2026-10-12T14:10:39.930189Z. Native command scope retained. |
| Native validation | passed | True | habitatmech:GOLD.1f5f4fee4c | Actual success 2026-10-12T14:10:39.931682Z to 2026-10-12T14:10:52.660726Z. Native command scope retained. |
| Native validation | passed | True | habitatmech:GOLD.1f5f4fee4c | Actual success 2026-10-12T14:10:52.661445Z to 2026-10-12T14:10:53.155068Z. Native command scope retained. |
| Exact-base CI QC evidence | passed | True | habitatmech:GOLD.1f5f4fee4c | Actual success 2026-10-12T14:08:07.095390Z to 2026-10-12T14:08:09.130913Z. All three required merge-group workflows passed at the exact captured base; authoritative QC passed 1054 tests with 3 skipped. Newly saved review bundles require their own integrity check. Does not validate new bundles. |
| Original occurrence inputs | unavailable | False | habitatmech:GOLD.1f5f4fee4c | Not recovered in bounded ignored-inclusive source-root searches; original checkout itself is accessible. |
| Claim-specific expression module | not_applicable | False | habitatmech:GOLD.1f5f4fee4c | No applicable exact expression claim. |

## Scientific And Domain Assessments

### Resolved source identity and retained scope

identity: supported. Targets: habitatmech:GOLD.1f5f4fee4c.

The complete record preserves its source identity and provenance without collapsing adjacent materials, features or organisms. Non-marine saline sediment is material, not the saline water body ENVO:01001319. Later examples mix lagoon sediment and halocline water and contain conflicting habitat labels; preserve these source tensions rather than silently reclassify all 37 frozen ORGANISM assertions.

### Typed identity, independent parents and mapping endpoints

grounding: concern. Targets: habitatmech:GOLD.1f5f4fee4c.

Non-marine saline sediment is material, not the saline water body ENVO:01001319. Later examples mix lagoon sediment and halocline water and contain conflicting habitat labels; preserve these source tensions rather than silently reclassify all 37 frozen ORGANISM assertions.

### Frozen accounting and lifecycle

provenance: supported. Targets: habitatmech:GOLD.1f5f4fee4c.

Complete reconstruction matches all fields: 1 source concepts and 0 ITEM-reviewed contributors. Frozen counts, units, scores and channels reproduce; omitted counts are not zero. REVIEWED expresses decision coverage, not scientific approval.

### Occurrence recovery and later context

evidence: unknown. Targets: habitatmech:GOLD.1f5f4fee4c.

Original full source membership is unavailable in the bounded scanned roots. Later GOLD examples and resolved NCBI identifiers are contextual cross-checks, not verification of every frozen assertion or characteristic presence. MIxS samples and studies remain separate denominators.

### Optional fields and adapters

completeness: supported. Targets: habitatmech:GOLD.1f5f4fee4c.

No unsupported new mechanism, parameter or characteristic taxon was inferred to fill optional fields. Source taxonomy associations are not expression-module claims. No exact strain/gene/dataset claim warrants iModulonDB interrogation; non-use is not negative evidence.

## Findings

### F1: NARROW comparison endpoint is ambiguous under the attestation contract

major / open / confirmed; issue key: habitatmech-gold.1f5f4fee4c-mapping-endpoint-contract.

The schema defines mapping_predicate from source_id to this record identifier, while the actual narrow route retains the source mint and compares it to a broader ontology parent. This is a representation-contract mismatch, not a claim of formal SKOS inconsistency. SSSOM/KGX readiness is not established.

### F2: GOLD context does not justify a strict habitat superclass

major / open / confirmed; issue key: habitatmech-gold.1f5f4fee4c-gold-context-parent.

Non-marine saline sediment is material, not the saline water body ENVO:01001319. Later examples mix lagoon sediment and halocline water and contain conflicting habitat labels; preserve these source tensions rather than silently reclassify all 37 frozen ORGANISM assertions.

## Recommended Actions And Acceptance Checks

### A1

Resolve source-to-record versus source-to-ontology-parent comparison semantics with seeder and downstream export regressions; a predicate-only replacement is insufficient.

- Reassess the exact source and preserve independent valid genera, source IDs, counts/units and omitted counts.
- Change maintained owners with append-only curation history; do not rewrite generated records or saved reviews.
- Add focused regressions; inspect guarded canaries and pass strict schema, labels, history, provenance, reproduction and QC.
- Use a linked successor review for any disposition; this assessment records proposed work, not an executed repair.

### A2

Assess and exclude only the unsupported exact-source contribution while retaining genuine genera and provenance; do not globally suppress a context class.

- Reassess the exact source and preserve independent valid genera, source IDs, counts/units and omitted counts.
- Change maintained owners with append-only curation history; do not rewrite generated records or saved reviews.
- Add focused regressions; inspect guarded canaries and pass strict schema, labels, history, provenance, reproduction and QC.
- Use a linked successor review for any disposition; this assessment records proposed work, not an executed repair.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/aquatic/sediment__e752e84e.yaml; Entire captured YAML, including every attestation, association and history entry | supports | Non-marine saline sediment is material, not the saline water body ENVO:01001319. Later examples mix lagoon sediment and halocline water and contain conflicting habitat labels; preserve these source tensions rather than silently reclassify all 37 frozen ORGANISM assertions. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied strict-genus, typed-identity, source comparison endpoint, MIxS-role, source-count/unit, evidence and ITEM lifecycle rules. |
| RAW | data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; Exact matching logical TSV rows; header=row1; study paths matched by membership | supports | {"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "depth": "5", "ecosystem": "Environmental", "ecosystem_category": "Aquatic", "ecosystem_subtype": "Saline", "ecosystem_type": "Non-marine Saline and Alkaline", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:3975", "leaf_label": "Sediment", "organism_count": "37", "specific_ecosystem": "Sediment", "study_count": "0", "total_assertions": "37"}, "logical_row": 329}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "41", "canonical_path": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "ecosystem_path_id": "3975"}, "logical_row": 377}], "data/raw/gold_path_triads.tsv": [{"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "distinct_terms": "1", "samples": "33", "slot": "broad", "studies": "7", "studies_agreeing": "7", "top_label": "aquatic biome", "top_share": "1.00", "top_term": "ENVO:00002030"}, "logical_row": 731}, {"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "distinct_terms": "5", "samples": "33", "slot": "local", "studies": "7", "studies_agreeing": "1", "top_label": "pond", "top_share": "0.48", "top_term": "ENVO:00000033"}, "logical_row": 732}, {"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "distinct_terms": "2", "samples": "33", "slot": "medium", "studies": "7", "studies_agreeing": "4", "top_label": "sediment", "top_share": "0.70", "top_term": "ENVO:00002007"}, "logical_row": 733}], "data/raw/gold_studies.tsv": [{"data": {"path_count": "9", "paths": "Environmental &gt; Aquatic &gt; Marine&#124;Environmental &gt; Aquatic &gt; Marine &gt; Coastal &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Marine &gt; Intertidal zone&#124;Environmental &gt; Aquatic &gt; Marine &gt; Intertidal zone &gt; Salt pond sediment&#124;Environmental &gt; Aquatic &gt; Marine &gt; Intertidal zone &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Marine &gt; Oceanic &gt; Oil-contaminated sediment&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "study_gold_id": "Gs0053056"}, "logical_row": 189}, {"data": {"path_count": "3", "paths": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Epilimnion&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "study_gold_id": "Gs0058670"}, "logical_row": 275}, {"data": {"path_count": "4", "paths": "Engineered &gt; Lab culture &gt; Culture media&#124;Engineered &gt; Lab enrichment&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Thermal springs &gt; Hot (42-90C)", "study_gold_id": "Gs0114486"}, "logical_row": 822}, {"data": {"path_count": "1", "paths": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "study_gold_id": "Gs0118593"}, "logical_row": 1146}, {"data": {"path_count": "4", "paths": "Environmental &gt; Aquatic &gt; Freshwater&#124;Environmental &gt; Aquatic &gt; Freshwater &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "study_gold_id": "Gs0133370"}, "logical_row": 1956}, {"data": {"path_count": "1", "paths": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "study_gold_id": "Gs0135943"}, "logical_row": 2169}, {"data": {"path_count": "2", "paths": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "study_gold_id": "Gs0141934"}, "logical_row": 2292}, {"data": {"path_count": "1", "paths": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "study_gold_id": "Gs0150506"}, "logical_row": 3323}, {"data": {"path_count": "3", "paths": "Environmental &gt; Aquatic &gt; Freshwater &gt; Groundwater&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "study_gold_id": "Gs0150686"}, "logical_row": 3498}, {"data": {"path_count": "13", "paths": "Environmental &gt; Aquatic &gt; Deep subsurface &gt; Groundwater&#124;Environmental &gt; Aquatic &gt; Freshwater &gt; Lake&#124;Environmental &gt; Aquatic &gt; Freshwater &gt; Lake &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline&#124;Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Thermal springs &gt; Acid lake &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Thermal springs &gt; Hot (42-90C)&#124;Environmental &gt; Aquatic &gt; Thermal springs &gt; Hot (42-90C) &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Thermal springs &gt; Tepid (25-34C)&#124;Environmental &gt; Aquatic &gt; Thermal springs &gt; Tepid (25-34C) &gt; Sediment&#124;Environmental &gt; Aquatic &gt; Thermal springs &gt; Warm (34-42C)&#124;Environmental &gt; Aquatic &gt; Thermal springs &gt; Warm (34-42C) &gt; Sediment&#124;Environmental &gt; Terrestrial &gt; Soil", "study_gold_id": "Gs0159129"}, "logical_row": 4222}]} |
| CODE | src/habitatmech/seed.py; Full parsed record reconstruction and executed resolver routes; not original occurrence recovery | supports | {"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:00002007"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.1f5f4fee4c", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:00002007"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.1f5f4fee4c", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "minted": "habitatmech:GOLD.1f5f4fee4c", "source": "GOLD", "source_id": "gold.ecosystem:3975"}], "source_concepts": 1} |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Official OWL labels, definitions, typed synonyms, named parents and restrictions kept separate | supports | {"ENVO:00000063": {"definitions": ["An accumulation of water of varying size."], "deprecated": [], "equivalents": [], "labels": ["water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000685", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000819"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002354"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01001220"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_15377"]}], "replacements": [], "synonyms": {"hasBroadSynonym": ["hydrographic feature"], "hasExactSynonym": ["aquatic feature", "bodies of water", "body of water", "waterbody"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002007": {"definitions": ["Particulate environmental material which is formed as a result of the transport and deposition of particles by flowing liquid."], "deprecated": [], "equivalents": [], "labels": ["sediment"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000060", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000086"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PATO_0000984"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:01001319": {"definitions": ["A body of water which is primarily composed of saline water."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00000063"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00002010"]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["saline water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000063", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00002010"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["saline body of water"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}} |
| PARENT | data/habitats/aquatic/saline_water_body.yaml; data/habitats/aquatic/water_body.yaml; data/habitats/terrestrial/sediment.yaml; Ancestor context only, not additional complete target review coverage | supports | {"ENVO:00000063": {"curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: EXACT.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}], "definition": "An accumulation of water of varying size.", "grounding_status": "EXACT", "label": "water body", "parent_habitats": ["ENVO:01000685"]}, "ENVO:00002007": {"curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE, MADIN, PREGO. Grounding: EXACT.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "ADD_CAUSAL_GRAPH", "changes": "Added a sediment porewater redox-ladder graph backed by PMID:31388058, PMID:15618510, and PMID:35308366.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-04T00:00:00Z"}], "definition": "Particulate environmental material which is formed as a result of the transport and deposition of particles by flowing liquid.", "grounding_status": "EXACT", "label": "sediment", "parent_habitats": ["ENVO:01000060"]}, "ENVO:01001319": {"curation_history": [{"action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date. (source concept habitatmech:BACDIVE.1f236a4c29)", "curator": "claude-opus-5", "timestamp": "2026-08-13T00:00:00Z"}, {"action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date. (source concept habitatmech:GOLD.a5eb3e9d4f)", "curator": "claude-opus-5", "timestamp": "2026-08-13T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by BACDIVE, GOLD. Grounding: CLOSE.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained BacDive label 'Saline' as RELATED_SYNONYM: a CLOSE source mapping does not establish exact lexical equivalence. Independent ontology synonyms and verbatim attestations are preserved (#1459).", "curator": "seed_from_sources", "timestamp": "2026-10-07T00:00:00Z"}, {"action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained GOLD label 'Saline' as RELATED_SYNONYM: a CLOSE source mapping does not establish exact lexical equivalence. Independent ontology synonyms and verbatim attestations are preserved (#1459).", "curator": "seed_from_sources", "timestamp": "2026-10-07T00:00:00Z"}, {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.ce244e62cd for habitatmech:GOLD.a5eb3e9d4f (Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline). Exact source-context correction https://github.com/CultureBotAI/HabitatMech/issues/1458 (20261012T111108Z-saline_water_body). The ENVO target is a saline waterbody, not saline water material. Its waterbody genus and current RELATED source-label handling are sound. Neither the ENVO class nor all inspected later source examples are inland-only, so the inland-environment source parent is unsupported on this generic target. BacDive STRAIN and GOLD ORGANISM totals remain separate. The broad Saline source labels and mixed later liquid/lake examples warrant bounded merge caution, not an automatic all-source remapping. Suppress only this immediate GOLD contribution; preserve identity, source paths/nodes/counts/units, omitted counts and independent genera. Original occurrence membership remains unavailable. No source-scope, endpoint or SSSOM/KGX certification is implied.", "curator": "codex-gpt-5", "timestamp": "2026-10-12T00:00:00Z"}], "definition": "A body of water which is primarily composed of saline water.", "grounding_status": "CLOSE", "label": "saline water body", "parent_habitats": ["ENVO:00000063"]}} |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; Official export retrieved 11-Oct, advertised generated 10-Oct; not original August membership; contacts excluded | supports | Exact positional-path census={"Biosample": 41, "Organism": 31, "SequencingProject": 65}; first up-to-three inspected BioSample/Organism examples={"Biosample": [{"data": {"BIOSAMPLE GOLD ID": "Gb0051421", "BIOSAMPLE NAME": "Sediment ecosystem from Aitoliko Lagoon, Greece ", "BIOSAMPLE NCBI TAX NAME": "salt lake metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Etoliko Lagoon, Greece"}, "row": 349}, {"data": {"BIOSAMPLE GOLD ID": "Gb0053623", "BIOSAMPLE NAME": "Saline surface water microbial communities from Etoliko Lagoon, Greece - halocline water (15 m)", "BIOSAMPLE NCBI TAX NAME": "salt lake metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Etoliko Lagoon, Greece"}, "row": 2187}, {"data": {"BIOSAMPLE GOLD ID": "Gb0053697", "BIOSAMPLE NAME": "Salt pond sediment microbial community from Union City, CA, USA - Pond 1C Sediment 2", "BIOSAMPLE NCBI TAX NAME": "salt lake metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Eden Landing Ponds, San Francisco, CA, USA"}, "row": 2230}], "Organism": [{"data": {"ORGANISM GOLD ID": "Go0007471", "ORGANISM HABITAT": "Marine&#124;Aquatic&#124;Bovine rumen", "ORGANISM NAME": "Thiocapsa marina 5811, DSM 5653", "ORGANISM SAMPLE COLLECTION SITE": "different brackish to marine sediments from Etang du Prevost in the Mediterranean Sea"}, "row": 6650}, {"data": {"ORGANISM GOLD ID": "Go0007978", "ORGANISM HABITAT": "Marine&#124;Sediment&#124;Aquatic&#124;Brackish water", "ORGANISM NAME": "Desulfobacter postgatei 2ac9", "ORGANISM SAMPLE COLLECTION SITE": "anaerobic sediment of brackish water ditch near Jadebusen, North Sea, Germany"}, "row": 7131}, {"data": {"ORGANISM GOLD ID": "Go0011448", "ORGANISM HABITAT": "Marine", "ORGANISM NAME": "Latescibacteria bacterium SCGC AAA257-K07", "ORGANISM SAMPLE COLLECTION SITE": "Sediment"}, "row": 10058}]}. Remaining members and joined studies indexed, not individually assessed. |
| CLASS | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Exact five-position ecosystem tuples, not organism membership | supports | [{"row": 847, "slug": "sediment__e752e84e", "path": "Environmental &gt; Aquatic &gt; Non-marine Saline and Alkaline &gt; Saline &gt; Sediment", "values": ["3975", "Environmental", "Aquatic", "Non-marine Saline and Alkaline", "Saline", "Sediment"]}] |
| MIXS | https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS; ENVO environmental-triad guidance | supports | Broad ecosystem, local feature and sampled material are different roles; association is not identity or genus. |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf | supports | Ignored/hidden-inclusive searches by identifier, label, slug and source path included these roots and all structured bundles. No prior structured observation matched this exact target. Original occurrence files were not found in bounded original data/build and configured kg-microbe/data searches, including ignored files; this is not global absence. Legacy Findings sections were inspected, not complete bibliographies. |
| ISSUES | https://github.com/CultureBotAI/HabitatMech/issues | context_only | Fetched 990 all-state issue titles/bodies and matched exact witnesses; issue state is not scientific disposition. Comments were not exhaustively crawled except the specifically cited spring issue. |

## Limits And Additional Notes

- Original checkout recovered and clean at origin/main before review. Ignored local supporting files are included in bounded searches; source snapshots are not assumed to be current live assertions.
- Self-review, not independent approval or whole-corpus certification.
- Original source occurrence membership was not recovered; later GOLD export does not certify frozen August assertions. Only up-to-three matching BioSample/Organism descriptions per sheet were interpreted.
- Labels: 1178 canonical, one synonym, five accepted exceptions and 2057 no-adapter skips. Skips are not scientific approval.
- Legacy reports and existing issue state are not disposition lineage. No older finding is silently closed.
- Current kg-microbe SSSOM/KGX conformance was not audited; shared mapping-contract issue #1398 remains open.
- Scientific inputs, generated products and history were unchanged during this assessment; later authorized curation must preserve this immutable observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T142050Z-sediment__e752e84e
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: sediment__e752e84e'
started_at: '2026-10-12T14:06:31.267477Z'
finished_at: '2026-10-12T14:20:50.366259Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Agent has participated in repository work; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: needs_curation
summary: Non-marine saline sediment is material, not the saline water body ENVO:01001319.
  Later examples mix lagoon sediment and halocline water and contain conflicting habitat
  labels; preserve these source tensions rather than silently reclassify all 37 frozen
  ORGANISM assertions.
source:
  git_revision: eb542f67c8c29c7277da72aae9630bd0b09eacf5
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
    sha256: 51304d515958f27ecac1a63eb76cf1887dcac32b1583d66008a1d7412208b2b0
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 9c9934f46b9ab058d34baff874cd0eeffe4e9ec5dc6a7c618824ceb65c53be03
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 331a7d9eb8a8909fc37402c0a776838979a8065644504d5c4f2a1c39bce5c24d
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/aquatic/saline_water_body.yaml
    sha256: eea526d0babe01c7d4dd64e0940bb194b6d918e0189d626c054ded9827f76289
    role: context
  - path: data/habitats/aquatic/sediment__e752e84e.yaml
    sha256: d8054bbcacf032e952b0fe961045e902d4729349fc4b800ec807cf057d116f6d
    role: target
  - path: data/habitats/aquatic/water_body.yaml
    sha256: 589b017dac949a9705a816afad5094c2ee9ac1655feb1c771358a07472848239
    role: context
  - path: data/habitats/terrestrial/sediment.yaml
    sha256: 850abac7c5b4cd5f033bd07f904cc8a6b4534ce8b38e94f6b99b7a3ac0f73147
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
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261005T224137Z-sediment__e752e84e.md
    sha256: b4f44bc68b7bd732633be85bd7efb5ed083d7abaf008a962a42665ca9d45b4b9
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
- target_id: habitatmech:GOLD.1f5f4fee4c
  path: data/habitats/aquatic/sediment__e752e84e.yaml
  label: Sediment
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source identity and lifecycle
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definitions and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Source-context parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Frozen ontology
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Exact frozen GOLD path
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated construction across all contributing source inventories
scope:
  description: One complete resolved record and every contributing source concept,
    with bounded external authority checks.
  selection: Next forty records lacking a completed individual scientific review in
    stable repository-relative path order. Each target is assessed separately; this
    does not establish category-wide scientific correctness. Initial coverage 888/3208.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  exclusions:
  - target: Other 3207 corpus records
    reason: Context inspection does not confer complete target review.
checks:
- check_id: C0
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  command: env RECORD_REVIEW_BASE=eb542f67c8c29c7277da72aae9630bd0b09eacf5 just validate
    data/habitats/aquatic/sediment__e752e84e.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T14:08:14.986773Z to 2026-10-12T14:08:16.531247Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C1
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  command: env RECORD_REVIEW_BASE=eb542f67c8c29c7277da72aae9630bd0b09eacf5 just validate-strict
    data/habitats/aquatic/sediment__e64a084a.yaml data/habitats/aquatic/sediment__e752e84e.yaml
    data/habitats/aquatic/sediment__e8fdcd7d.yaml data/habitats/aquatic/sediment__e910a9d2.yaml
    data/habitats/aquatic/sediment__ea0eadab.yaml data/habitats/aquatic/sediment__ebfa10eb.yaml
    data/habitats/aquatic/sediment__f04c7a2e.yaml data/habitats/aquatic/sediment__f7a00613.yaml
    data/habitats/aquatic/sediment__f9571146.yaml data/habitats/aquatic/sediment_water_interface.yaml
    data/habitats/aquatic/shipwreck.yaml data/habitats/aquatic/shrimp_pond.yaml data/habitats/aquatic/simulated_rainfall.yaml
    data/habitats/aquatic/sinkhole.yaml data/habitats/aquatic/small_freshwater_lake_biome.yaml
    data/habitats/aquatic/small_river_biome.yaml data/habitats/aquatic/snow.yaml data/habitats/aquatic/snow__7a83b333.yaml
    data/habitats/aquatic/soda_lake.yaml data/habitats/aquatic/soil__b5a2e0b1.yaml
    data/habitats/aquatic/solar_salterns.yaml data/habitats/aquatic/solar_salterns_sediment.yaml
    data/habitats/aquatic/solar_solterns.yaml data/habitats/aquatic/sound.yaml data/habitats/aquatic/spring__6fd75c62.yaml
    data/habitats/aquatic/spring__76db5e69.yaml data/habitats/aquatic/spring_sediment.yaml
    data/habitats/aquatic/sterile_water.yaml data/habitats/aquatic/storm_water_pond.yaml
    data/habitats/aquatic/stormwater.yaml data/habitats/aquatic/strait.yaml data/habitats/aquatic/stream.yaml
    data/habitats/aquatic/stromatolites.yaml data/habitats/aquatic/sub_saline_lake.yaml
    data/habitats/aquatic/subglacial_lake.yaml data/habitats/aquatic/subterranean_estuary.yaml
    data/habitats/aquatic/subterranean_lake.yaml data/habitats/aquatic/subterranean_lake__155f3b29.yaml
    data/habitats/aquatic/subtidal_zone.yaml data/habitats/aquatic/subtidal_zone__792000f9.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T14:09:22.255456Z to 2026-10-12T14:09:28.022961Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C2
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  command: env RECORD_REVIEW_BASE=eb542f67c8c29c7277da72aae9630bd0b09eacf5 just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T14:09:28.023817Z to 2026-10-12T14:09:49.221540Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C3
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  command: env RECORD_REVIEW_BASE=eb542f67c8c29c7277da72aae9630bd0b09eacf5 just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T14:09:49.224222Z to 2026-10-12T14:10:29.408992Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C4
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  command: env RECORD_REVIEW_BASE=eb542f67c8c29c7277da72aae9630bd0b09eacf5 just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T14:10:29.409728Z to 2026-10-12T14:10:35.671227Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C5
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  command: env RECORD_REVIEW_BASE=eb542f67c8c29c7277da72aae9630bd0b09eacf5 just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T14:10:35.672699Z to 2026-10-12T14:10:39.930189Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C6
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  command: env RECORD_REVIEW_BASE=eb542f67c8c29c7277da72aae9630bd0b09eacf5 just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T14:10:39.931682Z to 2026-10-12T14:10:52.660726Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C7
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  command: env RECORD_REVIEW_BASE=eb542f67c8c29c7277da72aae9630bd0b09eacf5 just provenance-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T14:10:52.661445Z to 2026-10-12T14:10:53.155068Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C8
  name: Exact-base CI QC evidence
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  command: gh run view 38257635522 --repo CultureBotAI/HabitatMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T14:08:07.095390Z to 2026-10-12T14:08:09.130913Z.
    All three required merge-group workflows passed at the exact captured base; authoritative
    QC passed 1054 tests with 3 skipped. Newly saved review bundles require their
    own integrity check. Does not validate new bundles.
  evidence_ids:
  - R
  - RULES
- check_id: ORIGINAL
  name: Original occurrence inputs
  required: false
  status: unavailable
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  summary: Not recovered in bounded ignored-inclusive source-root searches; original
    checkout itself is accessible.
  evidence_ids:
  - SEARCH
- check_id: IMODULON
  name: Claim-specific expression module
  required: false
  status: not_applicable
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  summary: No applicable exact expression claim.
  evidence_ids:
  - R
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/aquatic/sediment__e752e84e.yaml
  summary: Non-marine saline sediment is material, not the saline water body ENVO:01001319.
    Later examples mix lagoon sediment and halocline water and contain conflicting
    habitat labels; preserve these source tensions rather than silently reclassify
    all 37 frozen ORGANISM assertions.
  accessed_at: '2026-10-12T14:20:50.366259Z'
  support: supports
  locator: Entire captured YAML, including every attestation, association and history
    entry
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml
  summary: Applied strict-genus, typed-identity, source comparison endpoint, MIxS-role,
    source-count/unit, evidence and ITEM lifecycle rules.
  accessed_at: '2026-10-12T14:20:50.366259Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0",
    "canonical_path": "Environmental > Aquatic > Non-marine Saline and Alkaline >
    Saline > Sediment", "depth": "5", "ecosystem": "Environmental", "ecosystem_category":
    "Aquatic", "ecosystem_subtype": "Saline", "ecosystem_type": "Non-marine Saline
    and Alkaline", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:3975",
    "leaf_label": "Sediment", "organism_count": "37", "specific_ecosystem": "Sediment",
    "study_count": "0", "total_assertions": "37"}, "logical_row": 329}], "data/raw/gold_path_biosamples.tsv":
    [{"data": {"biosample_count": "41", "canonical_path": "Environmental > Aquatic
    > Non-marine Saline and Alkaline > Saline > Sediment", "ecosystem_path_id": "3975"},
    "logical_row": 377}], "data/raw/gold_path_triads.tsv": [{"data": {"canonical_path":
    "Environmental > Aquatic > Non-marine Saline and Alkaline > Saline > Sediment",
    "distinct_terms": "1", "samples": "33", "slot": "broad", "studies": "7", "studies_agreeing":
    "7", "top_label": "aquatic biome", "top_share": "1.00", "top_term": "ENVO:00002030"},
    "logical_row": 731}, {"data": {"canonical_path": "Environmental > Aquatic > Non-marine
    Saline and Alkaline > Saline > Sediment", "distinct_terms": "5", "samples": "33",
    "slot": "local", "studies": "7", "studies_agreeing": "1", "top_label": "pond",
    "top_share": "0.48", "top_term": "ENVO:00000033"}, "logical_row": 732}, {"data":
    {"canonical_path": "Environmental > Aquatic > Non-marine Saline and Alkaline >
    Saline > Sediment", "distinct_terms": "2", "samples": "33", "slot": "medium",
    "studies": "7", "studies_agreeing": "4", "top_label": "sediment", "top_share":
    "0.70", "top_term": "ENVO:00002007"}, "logical_row": 733}], "data/raw/gold_studies.tsv":
    [{"data": {"path_count": "9", "paths": "Environmental > Aquatic > Marine|Environmental
    > Aquatic > Marine > Coastal > Sediment|Environmental > Aquatic > Marine > Intertidal
    zone|Environmental > Aquatic > Marine > Intertidal zone > Salt pond sediment|Environmental
    > Aquatic > Marine > Intertidal zone > Sediment|Environmental > Aquatic > Marine
    > Oceanic > Oil-contaminated sediment|Environmental > Aquatic > Non-marine Saline
    and Alkaline|Environmental > Aquatic > Non-marine Saline and Alkaline > Saline|Environmental
    > Aquatic > Non-marine Saline and Alkaline > Saline > Sediment", "study_gold_id":
    "Gs0053056"}, "logical_row": 189}, {"data": {"path_count": "3", "paths": "Environmental
    > Aquatic > Non-marine Saline and Alkaline > Saline|Environmental > Aquatic >
    Non-marine Saline and Alkaline > Saline > Epilimnion|Environmental > Aquatic >
    Non-marine Saline and Alkaline > Saline > Sediment", "study_gold_id": "Gs0058670"},
    "logical_row": 275}, {"data": {"path_count": "4", "paths": "Engineered > Lab culture
    > Culture media|Engineered > Lab enrichment|Environmental > Aquatic > Non-marine
    Saline and Alkaline > Saline > Sediment|Environmental > Aquatic > Thermal springs
    > Hot (42-90C)", "study_gold_id": "Gs0114486"}, "logical_row": 822}, {"data":
    {"path_count": "1", "paths": "Environmental > Aquatic > Non-marine Saline and
    Alkaline > Saline > Sediment", "study_gold_id": "Gs0118593"}, "logical_row": 1146},
    {"data": {"path_count": "4", "paths": "Environmental > Aquatic > Freshwater|Environmental
    > Aquatic > Freshwater > Sediment|Environmental > Aquatic > Non-marine Saline
    and Alkaline > Saline|Environmental > Aquatic > Non-marine Saline and Alkaline
    > Saline > Sediment", "study_gold_id": "Gs0133370"}, "logical_row": 1956}, {"data":
    {"path_count": "1", "paths": "Environmental > Aquatic > Non-marine Saline and
    Alkaline > Saline > Sediment", "study_gold_id": "Gs0135943"}, "logical_row": 2169},
    {"data": {"path_count": "2", "paths": "Environmental > Aquatic > Non-marine Saline
    and Alkaline > Saline|Environmental > Aquatic > Non-marine Saline and Alkaline
    > Saline > Sediment", "study_gold_id": "Gs0141934"}, "logical_row": 2292}, {"data":
    {"path_count": "1", "paths": "Environmental > Aquatic > Non-marine Saline and
    Alkaline > Saline > Sediment", "study_gold_id": "Gs0150506"}, "logical_row": 3323},
    {"data": {"path_count": "3", "paths": "Environmental > Aquatic > Freshwater >
    Groundwater|Environmental > Aquatic > Non-marine Saline and Alkaline > Saline|Environmental
    > Aquatic > Non-marine Saline and Alkaline > Saline > Sediment", "study_gold_id":
    "Gs0150686"}, "logical_row": 3498}, {"data": {"path_count": "13", "paths": "Environmental
    > Aquatic > Deep subsurface > Groundwater|Environmental > Aquatic > Freshwater
    > Lake|Environmental > Aquatic > Freshwater > Lake > Sediment|Environmental >
    Aquatic > Non-marine Saline and Alkaline > Saline|Environmental > Aquatic > Non-marine
    Saline and Alkaline > Saline > Sediment|Environmental > Aquatic > Thermal springs
    > Acid lake > Sediment|Environmental > Aquatic > Thermal springs > Hot (42-90C)|Environmental
    > Aquatic > Thermal springs > Hot (42-90C) > Sediment|Environmental > Aquatic
    > Thermal springs > Tepid (25-34C)|Environmental > Aquatic > Thermal springs >
    Tepid (25-34C) > Sediment|Environmental > Aquatic > Thermal springs > Warm (34-42C)|Environmental
    > Aquatic > Thermal springs > Warm (34-42C) > Sediment|Environmental > Terrestrial
    > Soil", "study_gold_id": "Gs0159129"}, "logical_row": 4222}]}'
  accessed_at: '2026-10-12T14:20:50.366259Z'
  support: supports
  locator: Exact matching logical TSV rows; header=row1; study paths matched by membership
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": ["ENVO:00002007"], "extra_xrefs": [],
    "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.1f5f4fee4c", "mapping_predicate":
    "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"},
    "automatic": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": ["ENVO:00002007"], "extra_xrefs": [], "grounding_status": "NARROW",
    "identifier": "habitatmech:GOLD.1f5f4fee4c", "mapping_predicate": "skos:narrowMatch",
    "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "minted": "habitatmech:GOLD.1f5f4fee4c",
    "source": "GOLD", "source_id": "gold.ecosystem:3975"}], "source_concepts": 1}'
  accessed_at: '2026-10-12T14:20:50.366259Z'
  support: supports
  locator: Full parsed record reconstruction and executed resolver routes; not original
    occurrence recovery
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl
  summary: '{"ENVO:00000063": {"definitions": ["An accumulation of water of varying
    size."], "deprecated": [], "equivalents": [], "labels": ["water body"], "parents":
    ["http://purl.obolibrary.org/obo/ENVO_01000685", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_01000819"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0002354"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_01001220"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0002473"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/CHEBI_15377"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": ["hydrographic feature"], "hasExactSynonym": ["aquatic feature",
    "bodies of water", "body of water", "waterbody"], "hasNarrowSynonym": [], "hasRelatedSynonym":
    []}}, "ENVO:00002007": {"definitions": ["Particulate environmental material which
    is formed as a result of the transport and deposition of particles by flowing
    liquid."], "deprecated": [], "equivalents": [], "labels": ["sediment"], "parents":
    ["http://purl.obolibrary.org/obo/ENVO_01000060", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0000086"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/PATO_0000984"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym":
    []}}, "ENVO:01001319": {"definitions": ["A body of water which is primarily composed
    of saline water."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00000063"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00002010"]}],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}],
    "labels": ["saline water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000063",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00002010"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["saline
    body of water"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}}'
  accessed_at: '2026-10-12T14:06:43.102348Z'
  support: supports
  locator: Official OWL labels, definitions, typed synonyms, named parents and restrictions
    kept separate
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats/aquatic/saline_water_body.yaml; data/habitats/aquatic/water_body.yaml;
    data/habitats/terrestrial/sediment.yaml
  summary: '{"ENVO:00000063": {"curation_history": [{"action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: EXACT.",
    "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}], "definition":
    "An accumulation of water of varying size.", "grounding_status": "EXACT", "label":
    "water body", "parent_habitats": ["ENVO:01000685"]}, "ENVO:00002007": {"curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by ENVIRONMENTS_TABLE, MADIN, PREGO. Grounding: EXACT.", "curator": "seed_from_sources",
    "timestamp": "2026-08-16T05:58:02Z"}, {"action": "ADD_CAUSAL_GRAPH", "changes":
    "Added a sediment porewater redox-ladder graph backed by PMID:31388058, PMID:15618510,
    and PMID:35308366.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-04T00:00:00Z"}],
    "definition": "Particulate environmental material which is formed as a result
    of the transport and deposition of particles by flowing liquid.", "grounding_status":
    "EXACT", "label": "sediment", "parent_habitats": ["ENVO:01000060"]}, "ENVO:01001319":
    {"curation_history": [{"action": "REVIEW", "changes": "Reviewed and endorsed the
    seeder''s own resolution. Multi-source review pass: this record is attested by
    more than one independent vocabulary, and this source''s label or path was read
    against the record''s ontology term to check the merge is right. It agrees. Source
    concepts in the same pass whose labels did not agree were re-decided rather than
    endorsed; see the pass''s other decisions of the same date. (source concept habitatmech:BACDIVE.1f236a4c29)",
    "curator": "claude-opus-5", "timestamp": "2026-08-13T00:00:00Z"}, {"action": "REVIEW",
    "changes": "Reviewed and endorsed the seeder''s own resolution. Multi-source review
    pass: this record is attested by more than one independent vocabulary, and this
    source''s label or path was read against the record''s ontology term to check
    the merge is right. It agrees. Source concepts in the same pass whose labels did
    not agree were re-decided rather than endorsed; see the pass''s other decisions
    of the same date. (source concept habitatmech:GOLD.a5eb3e9d4f)", "curator": "claude-opus-5",
    "timestamp": "2026-08-13T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES", "changes":
    "Seeded from data/raw/ inventories; attested by BACDIVE, GOLD. Grounding: CLOSE.",
    "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action":
    "SOURCE_SYNONYM_SCOPED", "changes": "Retained BacDive label ''Saline'' as RELATED_SYNONYM:
    a CLOSE source mapping does not establish exact lexical equivalence. Independent
    ontology synonyms and verbatim attestations are preserved (#1459).", "curator":
    "seed_from_sources", "timestamp": "2026-10-07T00:00:00Z"}, {"action": "SOURCE_SYNONYM_SCOPED",
    "changes": "Retained GOLD label ''Saline'' as RELATED_SYNONYM: a CLOSE source
    mapping does not establish exact lexical equivalence. Independent ontology synonyms
    and verbatim attestations are preserved (#1459).", "curator": "seed_from_sources",
    "timestamp": "2026-10-07T00:00:00Z"}, {"action": "SOURCE_PARENT_EXCLUDED", "changes":
    "Excluded GOLD source-path parent contribution habitatmech:GOLD.ce244e62cd for
    habitatmech:GOLD.a5eb3e9d4f (Environmental > Aquatic > Non-marine Saline and Alkaline
    > Saline). Exact source-context correction https://github.com/CultureBotAI/HabitatMech/issues/1458
    (20261012T111108Z-saline_water_body). The ENVO target is a saline waterbody, not
    saline water material. Its waterbody genus and current RELATED source-label handling
    are sound. Neither the ENVO class nor all inspected later source examples are
    inland-only, so the inland-environment source parent is unsupported on this generic
    target. BacDive STRAIN and GOLD ORGANISM totals remain separate. The broad Saline
    source labels and mixed later liquid/lake examples warrant bounded merge caution,
    not an automatic all-source remapping. Suppress only this immediate GOLD contribution;
    preserve identity, source paths/nodes/counts/units, omitted counts and independent
    genera. Original occurrence membership remains unavailable. No source-scope, endpoint
    or SSSOM/KGX certification is implied.", "curator": "codex-gpt-5", "timestamp":
    "2026-10-12T00:00:00Z"}], "definition": "A body of water which is primarily composed
    of saline water.", "grounding_status": "CLOSE", "label": "saline water body",
    "parent_habitats": ["ENVO:00000063"]}}'
  accessed_at: '2026-10-12T14:20:50.366259Z'
  support: supports
  locator: Ancestor context only, not additional complete target review coverage
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  summary: 'Exact positional-path census={"Biosample": 41, "Organism": 31, "SequencingProject":
    65}; first up-to-three inspected BioSample/Organism examples={"Biosample": [{"data":
    {"BIOSAMPLE GOLD ID": "Gb0051421", "BIOSAMPLE NAME": "Sediment ecosystem from
    Aitoliko Lagoon, Greece ", "BIOSAMPLE NCBI TAX NAME": "salt lake metagenome",
    "BIOSAMPLE SAMPLE COLLECTION SITE": "Etoliko Lagoon, Greece"}, "row": 349}, {"data":
    {"BIOSAMPLE GOLD ID": "Gb0053623", "BIOSAMPLE NAME": "Saline surface water microbial
    communities from Etoliko Lagoon, Greece - halocline water (15 m)", "BIOSAMPLE
    NCBI TAX NAME": "salt lake metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Etoliko
    Lagoon, Greece"}, "row": 2187}, {"data": {"BIOSAMPLE GOLD ID": "Gb0053697", "BIOSAMPLE
    NAME": "Salt pond sediment microbial community from Union City, CA, USA - Pond
    1C Sediment 2", "BIOSAMPLE NCBI TAX NAME": "salt lake metagenome", "BIOSAMPLE
    SAMPLE COLLECTION SITE": "Eden Landing Ponds, San Francisco, CA, USA"}, "row":
    2230}], "Organism": [{"data": {"ORGANISM GOLD ID": "Go0007471", "ORGANISM HABITAT":
    "Marine|Aquatic|Bovine rumen", "ORGANISM NAME": "Thiocapsa marina 5811, DSM 5653",
    "ORGANISM SAMPLE COLLECTION SITE": "different brackish to marine sediments from
    Etang du Prevost in the Mediterranean Sea"}, "row": 6650}, {"data": {"ORGANISM
    GOLD ID": "Go0007978", "ORGANISM HABITAT": "Marine|Sediment|Aquatic|Brackish water",
    "ORGANISM NAME": "Desulfobacter postgatei 2ac9", "ORGANISM SAMPLE COLLECTION SITE":
    "anaerobic sediment of brackish water ditch near Jadebusen, North Sea, Germany"},
    "row": 7131}, {"data": {"ORGANISM GOLD ID": "Go0011448", "ORGANISM HABITAT": "Marine",
    "ORGANISM NAME": "Latescibacteria bacterium SCGC AAA257-K07", "ORGANISM SAMPLE
    COLLECTION SITE": "Sediment"}, "row": 10058}]}. Remaining members and joined studies
    indexed, not individually assessed.'
  accessed_at: '2026-10-11T13:21:51.155056Z'
  support: supports
  locator: Official export retrieved 11-Oct, advertised generated 10-Oct; not original
    August membership; contacts excluded
  snapshot_sha256: b222fa9df89ffbd1a30897a1e7302da363c57b463d9948ecc9bfcb9304b4a96f
- evidence_id: CLASS
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  summary: '[{"row": 847, "slug": "sediment__e752e84e", "path": "Environmental > Aquatic
    > Non-marine Saline and Alkaline > Saline > Sediment", "values": ["3975", "Environmental",
    "Aquatic", "Non-marine Saline and Alkaline", "Saline", "Sediment"]}]'
  accessed_at: '2026-10-12T14:06:45.335286Z'
  support: supports
  locator: Exact five-position ecosystem tuples, not organism membership
  snapshot_sha256: 3937335bc3919f62d2596a8ea8a77ccc97402c951239ee5ac2869539861733b3
- evidence_id: MIXS
  kind: authority
  reference: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
  summary: Broad ecosystem, local feature and sampled material are different roles;
    association is not identity or genus.
  accessed_at: '2026-10-12T14:06:45.600401Z'
  support: supports
  locator: ENVO environmental-triad guidance
  snapshot_sha256: 6fe1d8c6fd19c310c3c74d8d70072421e051fddff5b5b9a426bceeab6ba48af8
- evidence_id: SEARCH
  kind: search
  reference: curation; history; research; reports; reviews; data/raw; data/habitats;
    conf
  summary: Ignored/hidden-inclusive searches by identifier, label, slug and source
    path included these roots and all structured bundles. No prior structured observation
    matched this exact target. Original occurrence files were not found in bounded
    original data/build and configured kg-microbe/data searches, including ignored
    files; this is not global absence. Legacy Findings sections were inspected, not
    complete bibliographies.
  accessed_at: '2026-10-12T14:20:50.366259Z'
  support: supports
  search_scope: Ignored/hidden-inclusive searches by identifier, label, slug and source
    path included these roots and all structured bundles. No prior structured observation
    matched this exact target. Original occurrence files were not found in bounded
    original data/build and configured kg-microbe/data searches, including ignored
    files; this is not global absence. Legacy Findings sections were inspected, not
    complete bibliographies.
- evidence_id: ISSUES
  kind: database
  reference: https://github.com/CultureBotAI/HabitatMech/issues
  summary: Fetched 990 all-state issue titles/bodies and matched exact witnesses;
    issue state is not scientific disposition. Comments were not exhaustively crawled
    except the specifically cited spring issue.
  accessed_at: '2026-10-12T14:20:50.366259Z'
  support: context_only
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Resolved source identity and retained scope
  outcome: supported
  summary: The complete record preserves its source identity and provenance without
    collapsing adjacent materials, features or organisms. Non-marine saline sediment
    is material, not the saline water body ENVO:01001319. Later examples mix lagoon
    sediment and halocline water and contain conflicting habitat labels; preserve
    these source tensions rather than silently reclassify all 37 frozen ORGANISM assertions.
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  evidence_ids:
  - R
  - RAW
  - CODE
  - ONT
  - PARENT
- assessment_id: GROUNDING
  area: grounding
  topic: Typed identity, independent parents and mapping endpoints
  outcome: concern
  summary: Non-marine saline sediment is material, not the saline water body ENVO:01001319.
    Later examples mix lagoon sediment and halocline water and contain conflicting
    habitat labels; preserve these source tensions rather than silently reclassify
    all 37 frozen ORGANISM assertions.
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  evidence_ids:
  - R
  - RAW
  - CODE
  - ONT
  - PARENT
- assessment_id: PROVENANCE
  area: provenance
  topic: Frozen accounting and lifecycle
  outcome: supported
  summary: 'Complete reconstruction matches all fields: 1 source concepts and 0 ITEM-reviewed
    contributors. Frozen counts, units, scores and channels reproduce; omitted counts
    are not zero. REVIEWED expresses decision coverage, not scientific approval.'
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  evidence_ids:
  - R
  - RAW
  - CODE
- assessment_id: SOURCE_SCOPE
  area: evidence
  topic: Occurrence recovery and later context
  outcome: unknown
  summary: Original full source membership is unavailable in the bounded scanned roots.
    Later GOLD examples and resolved NCBI identifiers are contextual cross-checks,
    not verification of every frozen assertion or characteristic presence. MIxS samples
    and studies remain separate denominators.
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  evidence_ids:
  - R
  - RAW
  - SEARCH
  - MIXS
  - BULK
  - CLASS
- assessment_id: COMPLETENESS
  area: completeness
  topic: Optional fields and adapters
  outcome: supported
  summary: No unsupported new mechanism, parameter or characteristic taxon was inferred
    to fill optional fields. Source taxonomy associations are not expression-module
    claims. No exact strain/gene/dataset claim warrants iModulonDB interrogation;
    non-use is not negative evidence.
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  evidence_ids:
  - R
  - RULES
findings:
- finding_id: F1
  issue_key: habitatmech-gold.1f5f4fee4c-mapping-endpoint-contract
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: NARROW comparison endpoint is ambiguous under the attestation contract
  description: The schema defines mapping_predicate from source_id to this record
    identifier, while the actual narrow route retains the source mint and compares
    it to a broader ontology parent. This is a representation-contract mismatch, not
    a claim of formal SKOS inconsistency. SSSOM/KGX readiness is not established.
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  field_paths:
  - source_attestations.mapping_predicate
  evidence_ids:
  - R
  - RULES
  - RAW
  - CODE
  - ONT
  - PARENT
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained owner of the exact finding; never patch generated YAML
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material claim or representation mismatch.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
- finding_id: F2
  issue_key: habitatmech-gold.1f5f4fee4c-gold-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: GOLD context does not justify a strict habitat superclass
  description: Non-marine saline sediment is material, not the saline water body ENVO:01001319.
    Later examples mix lagoon sediment and halocline water and contain conflicting
    habitat labels; preserve these source tensions rather than silently reclassify
    all 37 frozen ORGANISM assertions.
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  field_paths:
  - parent_habitats
  evidence_ids:
  - R
  - RULES
  - RAW
  - CODE
  - ONT
  - PARENT
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner of the exact finding; never patch generated YAML
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material claim or representation mismatch.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1526
actions:
- action_id: A1
  description: Resolve source-to-record versus source-to-ontology-parent comparison
    semantics with seeder and downstream export regressions; a predicate-only replacement
    is insufficient.
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained owner of the exact finding; never patch generated YAML
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Reassess the exact source and preserve independent valid genera, source IDs, counts/units
    and omitted counts.
  - Change maintained owners with append-only curation history; do not rewrite generated
    records or saved reviews.
  - Add focused regressions; inspect guarded canaries and pass strict schema, labels,
    history, provenance, reproduction and QC.
  - Use a linked successor review for any disposition; this assessment records proposed
    work, not an executed repair.
- action_id: A2
  description: Assess and exclude only the unsupported exact-source contribution while
    retaining genuine genera and provenance; do not globally suppress a context class.
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.1f5f4fee4c
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained owner of the exact finding; never patch generated YAML
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Reassess the exact source and preserve independent valid genera, source IDs, counts/units
    and omitted counts.
  - Change maintained owners with append-only curation history; do not rewrite generated
    records or saved reviews.
  - Add focused regressions; inspect guarded canaries and pass strict schema, labels,
    history, provenance, reproduction and QC.
  - Use a linked successor review for any disposition; this assessment records proposed
    work, not an executed repair.
limitations:
- Original checkout recovered and clean at origin/main before review. Ignored local
  supporting files are included in bounded searches; source snapshots are not assumed
  to be current live assertions.
- Self-review, not independent approval or whole-corpus certification.
- Original source occurrence membership was not recovered; later GOLD export does
  not certify frozen August assertions. Only up-to-three matching BioSample/Organism
  descriptions per sheet were interpreted.
- 'Labels: 1178 canonical, one synonym, five accepted exceptions and 2057 no-adapter
  skips. Skips are not scientific approval.'
- Legacy reports and existing issue state are not disposition lineage. No older finding
  is silently closed.
- 'Current kg-microbe SSSOM/KGX conformance was not audited; shared mapping-contract
  issue #1398 remains open.'
- Scientific inputs, generated products and history were unchanged during this assessment;
  later authorized curation must preserve this immutable observation.
tags:
- habitatmech
- aquatic
- record-review
- scientific-review
```
