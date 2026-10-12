# Scientific record review: sediment__e3709872

- Review: 20261012T125039Z-sediment__e3709872
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-12T12:38:20.147953Z
- Finished UTC: 2026-10-12T12:50:39.660095Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Coastal sediment is not coastal sea water ENVO:00002150. The modal source marine-benthic annotations do not make water a material genus and include an obsolete local term not emitted here. Keep ontology/source refresh separate from the exact incoming-edge correction.

## Scope And Provenance

Complete resolved record and its sole source concept, with bounded authority checks.

Selection: Next forty records lacking a completed individual scientific review in stable repository-relative path order. Each target is assessed separately; this does not establish category-wide scientific correctness. Starting coverage: 848/3208 distinct individually reviewed records.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b02596a4dc6a9ce2c28ff3780762a39aef943820.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.9df2041479 | data/habitats/aquatic/sediment__e3709872.yaml | generated | Sediment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validation gate | passed | True | habitatmech:GOLD.9df2041479 | Actual success 2026-10-12T12:40:23.607950Z to 2026-10-12T12:40:25.373225Z. Native command scope retained. |
| Native validation gate | passed | True | habitatmech:GOLD.9df2041479 | Actual success 2026-10-12T12:40:29.018560Z to 2026-10-12T12:40:35.990580Z. Native command scope retained. |
| Native validation gate | passed | True | habitatmech:GOLD.9df2041479 | Actual success 2026-10-12T12:40:35.991426Z to 2026-10-12T12:40:50.457488Z. Native command scope retained. |
| Native validation gate | passed | True | habitatmech:GOLD.9df2041479 | Actual success 2026-10-12T12:40:50.458224Z to 2026-10-12T12:41:52.821380Z. Native command scope retained. |
| Native validation gate | passed | True | habitatmech:GOLD.9df2041479 | Actual success 2026-10-12T12:41:52.822147Z to 2026-10-12T12:41:59.333576Z. Native command scope retained. |
| Native validation gate | passed | True | habitatmech:GOLD.9df2041479 | Actual success 2026-10-12T12:41:59.334281Z to 2026-10-12T12:42:03.081279Z. Native command scope retained. |
| Native validation gate | passed | True | habitatmech:GOLD.9df2041479 | Actual success 2026-10-12T12:42:03.082126Z to 2026-10-12T12:42:17.438355Z. Native command scope retained. |
| Native validation gate | passed | True | habitatmech:GOLD.9df2041479 | Actual success 2026-10-12T12:42:17.439209Z to 2026-10-12T12:42:17.918358Z. Native command scope retained. |
| Exact-base CI QC evidence | passed | True | habitatmech:GOLD.9df2041479 | Actual success 2026-10-12T12:38:42.872938Z to 2026-10-12T12:38:45.642655Z. All three required merge-group workflows passed at the exact captured base; authoritative QC passed 1052 tests with 3 skipped. Newly saved review bundles require their own integrity check. Earlier CI does not validate these new bundles. |
| Original occurrence-input recovery | unavailable | False | habitatmech:GOLD.9df2041479 | Original checkout cannot be traversed due to Operation not permitted; temporary source search is bounded and does not prove global absence. |
| Claim-specific expression-module query | not_applicable | False | habitatmech:GOLD.9df2041479 | No exact organism/dataset/gene claim requiring this adapter. |

## Scientific And Domain Assessments

### Qualified sediment identity and source scope

identity: supported. Targets: habitatmech:GOLD.9df2041479.

The complete record retains the exact GOLD path and source mint as an AQUATIC sediment habitat. It is not asserted as water, a containing feature or an exact candidate ontology identity. Coastal sediment is not coastal sea water ENVO:00002150. The modal source marine-benthic annotations do not make water a material genus and include an obsolete local term not emitted here. Keep ontology/source refresh separate from the exact incoming-edge correction.

### Independent genus and context contributions

grounding: concern. Targets: habitatmech:GOLD.9df2041479.

Coastal sediment is not coastal sea water ENVO:00002150. The modal source marine-benthic annotations do not make water a material genus and include an obsolete local term not emitted here. Keep ontology/source refresh separate from the exact incoming-edge correction.

### Attestation comparison endpoint

grounding: concern. Targets: habitatmech:GOLD.9df2041479.

All NARROW routes retain a source identity while using a broader ontology comparison; the emitted contract does not distinguish these endpoints.

### Frozen source accounting and lifecycle

provenance: supported. Targets: habitatmech:GOLD.9df2041479.

The full target reproduces with 1 source concept and 0 ITEM-reviewed contributors. Counts and units match frozen inputs; omitted counts are not biological zero. Later sample/organism counts do not reconstruct those historical assertions. REVIEWED is a decision-coverage gate, not scientific approval.

### Original occurrence membership versus later examples

evidence: unknown. Targets: habitatmech:GOLD.9df2041479.

Later BioSample examples include amended sediments; laboratory manipulations are not natural class-wide properties. Original source occurrence inputs are inaccessible; no source-count correction is inferred.

### Optional data and structured adapter applicability

completeness: supported. Targets: habitatmech:GOLD.9df2041479.

No authored definition, taxa, parameter, graph, gene or expression claim is emitted. Optional missing slots are not automatic defects. No iModulonDB query applies; no negative biological inference is made.

## Findings

### F1: NARROW attestation does not expose its actual broader comparison endpoint

major / open / confirmed; issue key: habitatmech-gold.9df2041479-mapping-endpoint-contract.

The schema defines mapping_predicate from source_id to this record identifier, while the executed narrow route retains the source mint and compares it to a broader ontology parent. The target ID is therefore ambiguous under the advertised contract. This is a representation mismatch, not a claim that every reflexive SKOS statement is formally inconsistent; changing only the predicate is not a complete repair.

### F2: GOLD context is not an established strictly broader material class

major / open / confirmed; issue key: habitatmech-gold.9df2041479-gold-context-parent.

Coastal sediment is not coastal sea water ENVO:00002150. The modal source marine-benthic annotations do not make water a material genus and include an obsolete local term not emitted here. Keep ontology/source refresh separate from the exact incoming-edge correction.

## Recommended Actions And Acceptance Checks

### A1

Resolve shared issue #1398 with explicit source-to-record versus source-to-ontology comparison semantics and downstream export regression tests. Do not infer SSSOM/KGX readiness from this record review.

- Reassess the exact source and contribution; preserve independent true genera, qualified identity, source counts/units and omitted counts.
- Change maintained inputs with append-only curation history, never generated YAML or existing review bundles.
- Add focused regression tests, inspect an exact seed canary, regenerate guarded products, and pass schema, strict, label, history, provenance, corpus reproduction and QC gates.
- Save a linked successor observation for any disposition. No proposed repair was executed during this assessment.

### A2

Assess and exclude only the unsupported context contribution using its exact source path and expected resolved parent; retain source provenance and independently supported material genera.

- Reassess the exact source and contribution; preserve independent true genera, qualified identity, source counts/units and omitted counts.
- Change maintained inputs with append-only curation history, never generated YAML or existing review bundles.
- Add focused regression tests, inspect an exact seed canary, regenerate guarded products, and pass schema, strict, label, history, provenance, corpus reproduction and QC gates.
- Save a linked successor observation for any disposition. No proposed repair was executed during this assessment.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/aquatic/sediment__e3709872.yaml; Entire captured YAML, including attestations and generated history | supports | Coastal sediment is not coastal sea water ENVO:00002150. The modal source marine-benthic annotations do not make water a material genus and include an obsolete local term not emitted here. Keep ontology/source refresh separate from the exact incoming-edge correction. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied strict-parent, source comparison endpoint, MIxS-role, source-count/unit, evidence and ITEM lifecycle rules. |
| RAW | data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; Exact logical TSV rows, header=row1 | supports | {"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Environmental &gt; Aquatic &gt; Marine &gt; Coastal &gt; Sediment", "depth": "5", "ecosystem": "Environmental", "ecosystem_category": "Aquatic", "ecosystem_subtype": "Coastal", "ecosystem_type": "Marine", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:4045", "leaf_label": "Sediment", "organism_count": "295", "specific_ecosystem": "Sediment", "study_count": "0", "total_assertions": "295"}, "logical_row": 95}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "572", "canonical_path": "Environmental &gt; Aquatic &gt; Marine &gt; Coastal &gt; Sediment", "ecosystem_path_id": "4045"}, "logical_row": 58}], "data/raw/gold_path_triads.tsv": [{"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Marine &gt; Coastal &gt; Sediment", "distinct_terms": "4", "samples": "377", "slot": "broad", "studies": "33", "studies_agreeing": "23", "top_label": "marine benthic biome", "top_share": "0.86", "top_term": "ENVO:01000024"}, "logical_row": 455}, {"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Marine &gt; Coastal &gt; Sediment", "distinct_terms": "7", "samples": "377", "slot": "local", "studies": "33", "studies_agreeing": "22", "top_label": "marine benthic feature", "top_share": "0.82", "top_term": "ENVO:01000105"}, "logical_row": 456}, {"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Marine &gt; Coastal &gt; Sediment", "distinct_terms": "6", "samples": "377", "slot": "medium", "studies": "33", "studies_agreeing": "28", "top_label": "marine sediment", "top_share": "0.94", "top_term": "ENVO:03000033"}, "logical_row": 457}]} |
| CODE | src/habitatmech/seed.py; Full parsed target reconstruction and executed resolver routes; not recovery of original source membership | supports | {"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:00002007"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.9df2041479", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:00002007"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.9df2041479", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "minted": "habitatmech:GOLD.9df2041479", "source": "GOLD", "source_id": "gold.ecosystem:4045"}], "source_concepts": 1} |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Current official OWL labels, definitions, typed synonyms, named parents and separate restrictions; candidates are not exact matches by implication | supports | {"ENVO:00002006": {"definitions": ["An environmental material primarily composed of dihydrogen oxide in its liquid form."], "deprecated": [], "equivalents": [], "labels": ["liquid water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000815", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_15377"]}], "replacements": [], "synonyms": {"hasBroadSynonym": ["water"], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002007": {"definitions": ["Particulate environmental material which is formed as a result of the transport and deposition of particles by flowing liquid."], "deprecated": [], "equivalents": [], "labels": ["sediment"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000060", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000086"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PATO_0000984"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002010": {"definitions": ["Water which contains a significant concentration of dissolved salts."], "deprecated": [], "equivalents": [], "labels": ["saline water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/ENVO_02000200"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_26710"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000086"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PATO_0001657"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["salt water"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002149": {"definitions": ["Water which has physicochemical properties that have been determined by the processes occuring in a sea or ocean."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002010"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#unionOf": [{"nested": true}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["sea water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002010", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#unionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00000015"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00000016"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["ocean water", "seawater"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002150": {"definitions": ["Coastal sea water is sea water that is adjacent to a coast."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002149"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002220"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00000303"]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["coastal sea water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002149", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002220"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00000303"]}], "replacements": [], "synonyms": {"hasBroadSynonym": ["coastal water"], "hasExactSynonym": ["coastal ocean water", "coastal oceanic water", "coastal seawater"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:03000033": {"definitions": ["Sediment which has been transported through the marine water column, settling on the seafloor."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#unionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002007"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"nested": true}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002007"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"nested": true}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["marine sediment"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002007", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002220"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00001999"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002353"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_03000036"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["marine sediments"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}} |
| PARENT | data/habitats/aquatic/coastal_sea_water.yaml; data/habitats/aquatic/sea_water.yaml; data/habitats/aquatic/saline_water.yaml; data/habitats/aquatic/liquid_water.yaml; data/habitats/terrestrial/sediment.yaml; Ancestor context only, not additional complete scientific review coverage | supports | {"ENVO:00002006": {"curation_history": [{"action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Co-attestor review (#12): 'water' resolves to ENVO:00002006 'liquid water'. The term adds 'liquid', which the key does not say, but every parameter band on the row is a property of liquid water and the table has separate rows for ice. Correct as seeded. (source concept habitatmech:ENVIRONMENTS_TABLE.97e0db4016)", "curator": "claude-opus-5", "timestamp": "2026-08-15T00:00:00Z"}, {"action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Co-attestor review (#12): this source names the ontology CURIE itself, so its grounding is definitional rather than a lexical guess \u2014 the record IS the term the source pointed at. Recorded so the record it co-attests can reach REVIEWED, which needs every source concept decided. (source concept habitatmech:MADIN.ee80f974c2)", "curator": "claude-opus-5", "timestamp": "2026-08-15T00:00:00Z"}, {"action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Co-attestor review (#12): this source names the ontology CURIE itself, so its grounding is definitional rather than a lexical guess \u2014 the record IS the term the source pointed at. Recorded so the record it co-attests can reach REVIEWED, which needs every source concept decided. (source concept habitatmech:PREGO.9c5507e85a)", "curator": "claude-opus-5", "timestamp": "2026-08-15T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE, MADIN, PREGO. Grounding: EXACT.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "ADD_CAUSAL_GRAPH", "changes": "Added a liquid-water planktonic solute-foraging graph backed by PMID:15306380, PMID:25500507, PMID:21663439, PMID:21329211, PMID:23118182, PMID:23204367, and DOI:10.3354/meps010257.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-04T00:00:00Z"}, {"action": "REVISE_CAUSAL_GRAPH", "changes": "Bounded the graph to a conditional marine water-column model under issue 1263. Distinguished liquid phase from water activity and suspended from sinking particles; represented connected habitat, bacterial community and biomass-production process without physical STATE nodes; retargeted the growth edge to biomass production and separated uptake from carbon incorporation. Preserved graph, node and edge IDs and existing citations; added claim-level support from inspected Stocker and Seymour full text.", "curator": "codex-gpt-5", "llm_assisted": true, "timestamp": "2026-10-12T00:00:00Z"}], "definition": "An environmental material primarily composed of dihydrogen oxide in its liquid form.", "grounding_status": "EXACT", "label": "liquid water", "parent_habitats": ["ENVO:01000815"]}, "ENVO:00002007": {"curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE, MADIN, PREGO. Grounding: EXACT.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "ADD_CAUSAL_GRAPH", "changes": "Added a sediment porewater redox-ladder graph backed by PMID:31388058, PMID:15618510, and PMID:35308366.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-04T00:00:00Z"}], "definition": "Particulate environmental material which is formed as a result of the transport and deposition of particles by flowing liquid.", "grounding_status": "EXACT", "label": "sediment", "parent_habitats": ["ENVO:01000060"]}, "ENVO:00002010": {"curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE, PREGO. Grounding: EXACT.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}], "definition": "Water which contains a significant concentration of dissolved salts.", "grounding_status": "EXACT", "label": "saline water", "parent_habitats": ["ENVO:00002006"]}, "ENVO:00002149": {"curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE, MADIN, PREGO. Grounding: EXACT.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "ADD_CAUSAL_GRAPH", "changes": "Added a seawater dissolved-organic-matter and oligotrophic-uptake graph backed by PMID:26951682, PMID:19805210, PMID:34010286, and PMID:16109880.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-04T00:00:00Z"}, {"action": "REVISE_CAUSAL_GRAPH", "changes": "Corrected node scope and genome trait typing for issue #2025. Preserved graph/node/edge IDs and all four publication references; separated the Pelagibacter example, comparative strategy evidence, modeled transport and inferred community-level linkage. No taxonomic grounding was invented.", "curator": "codex-gpt-5", "llm_assisted": true, "timestamp": "2026-10-12T00:00:00Z"}], "definition": "Water which has physicochemical properties that have been determined by the processes occuring in a sea or ocean.", "grounding_status": "EXACT", "label": "sea water", "parent_habitats": ["ENVO:00002010"]}, "ENVO:00002150": {"curation_history": [{"action": "GROUND", "changes": "Grounded to ENVO:00002150 'coastal sea water' (CLOSE). GOLD's Marine &gt; Coastal zone. ENVO:00002150 names the water body specifically while GOLD's node is the zone, so CLOSE rather than EXACT. (source concept habitatmech:GOLD.1a3d0aff0c)", "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "GROUND", "changes": "Grounded to ENVO:00002150 'coastal sea water' (CLOSE). The neritic zone is the region; ENVO names the water body, so CLOSE. Path: Environmental &gt; Aquatic &gt; Marine &gt; Neritic zone/Coastal water (source concept habitatmech:GOLD.89754b31f3)", "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "GROUND", "changes": "Grounded to ENVO:00002150 'coastal sea water' (CLOSE). The neritic zone is the region; ENVO names the water body, so CLOSE. Path: Environmental &gt; Aquatic &gt; Marine &gt; Littoral zone &gt; Neritic zone/Coasta (source concept habitatmech:GOLD.ad324e6267)", "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. PREGO asserts ENVO:00002150 coastal sea water directly; the self-grounding is correct. Endorsed to complete the coastal record. (source concept habitatmech:PREGO.0da0bcd805)", "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD, PREGO. Grounding: EXACT.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained GOLD label 'Coastal' as RELATED_SYNONYM: a CLOSE source mapping does not establish exact lexical equivalence. Independent ontology synonyms and verbatim attestations are preserved (#1459).", "curator": "seed_from_sources", "timestamp": "2026-10-07T00:00:00Z"}, {"action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained GOLD label 'Neritic zone/Coastal water' as RELATED_SYNONYM: a CLOSE source mapping does not establish exact lexical equivalence. Independent ontology synonyms and verbatim attestations are preserved (#1459).", "curator": "seed_from_sources", "timestamp": "2026-10-07T00:00:00Z"}, {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution ENVO:00001999 for habitatmech:GOLD.1a3d0aff0c (Environmental &gt; Aquatic &gt; Marine &gt; Coastal). ITEM hierarchy assessment: https://github.com/CultureBotAI/HabitatMech/issues/1987 (20261012T001621Z-coastal_sea_water). ENVO denotes sea-water material near a coast. GOLD Coastal and Coastal zone are place-based bins, including sediment examples in the later export, not coextensive water-material classes. CLOSE does not establish identity. The marine-water-body and littoral-zone parents are context, while sea water is a defensible genus. Official coastal water is a broad synonym, not exact. Exclude only this guarded GOLD source-parent contribution. Preserve independent parents, frozen source identity/counts/units or omissions and native lifecycle. Later examples do not reconstruct frozen membership; shared synonym and endpoint issues remain separate.", "curator": "codex-gpt-5", "timestamp": "2026-10-12T00:00:00Z"}, {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution ENVO:00001999 for habitatmech:GOLD.89754b31f3 (Environmental &gt; Aquatic &gt; Marine &gt; Neritic zone/Coastal water). ITEM hierarchy assessment: https://github.com/CultureBotAI/HabitatMech/issues/1987 (20261012T001621Z-coastal_sea_water). ENVO denotes sea-water material near a coast. GOLD Coastal and Coastal zone are place-based bins, including sediment examples in the later export, not coextensive water-material classes. CLOSE does not establish identity. The marine-water-body and littoral-zone parents are context, while sea water is a defensible genus. Official coastal water is a broad synonym, not exact. Exclude only this guarded GOLD source-parent contribution. Preserve independent parents, frozen source identity/counts/units or omissions and native lifecycle. Later examples do not reconstruct frozen membership; shared synonym and endpoint issues remain separate.", "curator": "codex-gpt-5", "timestamp": "2026-10-12T00:00:00Z"}, {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution ENVO:01000125 for habitatmech:GOLD.ad324e6267 (Environmental &gt; Aquatic &gt; Marine &gt; Littoral zone &gt; Neritic zone/Coastal water). ITEM hierarchy assessment: https://github.com/CultureBotAI/HabitatMech/issues/1987 (20261012T001621Z-coastal_sea_water). ENVO denotes sea-water material near a coast. GOLD Coastal and Coastal zone are place-based bins, including sediment examples in the later export, not coextensive water-material classes. CLOSE does not establish identity. The marine-water-body and littoral-zone parents are context, while sea water is a defensible genus. Official coastal water is a broad synonym, not exact. Exclude only this guarded GOLD source-parent contribution. Preserve independent parents, frozen source identity/counts/units or omissions and native lifecycle. Later examples do not reconstruct frozen membership; shared synonym and endpoint issues remain separate.", "curator": "codex-gpt-5", "timestamp": "2026-10-12T00:00:00Z"}], "definition": "Coastal sea water is sea water that is adjacent to a coast.", "grounding_status": "EXACT", "label": "coastal sea water", "parent_habitats": ["ENVO:00002149"]}} |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; Official export retrieved 11-Oct, advertised generated 10-Oct; not original August membership; contacts excluded | supports | Exact positional-path census={"Biosample": 666, "Organism": 241, "SequencingProject": 1025}; inspected first up-to-three BioSample/Organism metadata examples={"Biosample": [{"data": {"BIOSAMPLE GOLD ID": "Gb0053374", "BIOSAMPLE NAME": "Marine sediment microbial community from Cabo Rojo, Puerto Rico - PR CR 10% Liquid 1", "BIOSAMPLE NCBI TAX NAME": "marine metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Cabo Rojo, Puerto Rico"}, "row": 2024}, {"data": {"BIOSAMPLE GOLD ID": "Gb0112468", "BIOSAMPLE NAME": "Marine sediment microbial communities from the Atlantic coast under amendment with organic carbon and nitrate - tdAd00.1", "BIOSAMPLE NCBI TAX NAME": "marine sediment metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Marine sediment"}, "row": 7373}, {"data": {"BIOSAMPLE GOLD ID": "Gb0112469", "BIOSAMPLE NAME": "Marine sediment microbial communities from the Atlantic coast under amendment with organic carbon and nitrate - tdAd00.2", "BIOSAMPLE NCBI TAX NAME": "marine sediment metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Marine sediment"}, "row": 7374}], "Organism": [{"data": {"ORGANISM GOLD ID": "Go0001511", "ORGANISM HABITAT": "Aquatic&#124;Mud&#124;Soil&#124;Host&#124;Fresh water", "ORGANISM NAME": "Acetoanaerobium sticklandii DSM 519", "ORGANISM SAMPLE COLLECTION SITE": "Mud water"}, "row": 1370}, {"data": {"ORGANISM GOLD ID": "Go0011444", "ORGANISM HABITAT": "Marine", "ORGANISM NAME": "candidate division WS3 bacterium SCGC AAA257-D15", "ORGANISM SAMPLE COLLECTION SITE": "Aarhus Bay"}, "row": 10057}, {"data": {"ORGANISM GOLD ID": "Go0013808", "ORGANISM HABITAT": "Marine&#124;Sediment&#124;Aquatic", "ORGANISM NAME": "Desulfatibacillum aliphaticivorans DSM 15576", "ORGANISM SAMPLE COLLECTION SITE": "Marine sediment"}, "row": 12192}]}. Later BioSample examples include amended sediments; laboratory manipulations are not natural class-wide properties. Remaining members and joined studies were indexed, not individually assessed. |
| CLASS | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Exact five-position ecosystem tuples; not organism membership or certification of all historical node IDs | supports | [{"row": 684, "slug": "sediment__e3709872", "path": "Environmental &gt; Aquatic &gt; Marine &gt; Coastal &gt; Sediment", "values": ["4045", "Environmental", "Aquatic", "Marine", "Coastal", "Sediment"]}] |
| MIXS | https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS; ENVO environmental-triad guidance | supports | Broad ecosystem, local feature and sampled material describe different environmental roles; association is not automatically class identity or strict ancestry. |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf; Search receipts retained in temporary assessment workspace | supports | Ignored/hidden-inclusive identifier, label, slug and source-path searches across these roots found no prior structured review for this exact target. Legacy Findings sections were read; full bibliographies were not revalidated. Original Documents checkout is inaccessible, not demonstrated absent. The temporary checkout lacks original GOLD dump files in the bounded filename search. |
| ISSUES | https://github.com/CultureBotAI/HabitatMech/issues | context_only | Fetched 989 all-state issue titles/bodies; inspected relevant exact-source issue bodies as leads. No exhaustive comment crawl. Issue state is not scientific disposition. |

## Limits And Additional Notes

- Clean GitHub origin/main snapshot. The original Documents checkout remains inaccessible; local uncommitted and ignored-only content there cannot be assessed.
- Completed individual assessment is self-review, not independent approval or whole-corpus certification.
- Only first up-to-three matching BioSample/Organism metadata descriptions per sheet were interpreted; remaining members, projects and joined studies were indexed only.
- Later GOLD export/classification does not reconstruct frozen August membership or certify every historical node live.
- Label correspondence passed with 1178 canonical pairs, one synonym, five accepted exceptions and 2057 no-adapter skips; skips are not scientific approval.
- SSSOM/KGX conformance to current kg-microbe modeling was not audited; shared issue #1398 remains open.
- Legacy reports are leads; their complete bibliographies were not revalidated and old findings are not retired.
- No habitat, curation input, scientific status/history, generated product or GitHub issue was changed during this assessment.
- No prior structured observation for this exact target was found in the ignored-inclusive temporary-checkout search; no predecessor is silently superseded.
- Assessment phase was read-only. Later authorized publication or curation must preserve this historical observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T125039Z-sediment__e3709872
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: sediment__e3709872'
started_at: '2026-10-12T12:38:20.147953Z'
finished_at: '2026-10-12T12:50:39.660095Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Agent participated in repository curation; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Coastal sediment is not coastal sea water ENVO:00002150. The modal source
  marine-benthic annotations do not make water a material genus and include an obsolete
  local term not emitted here. Keep ontology/source refresh separate from the exact
  incoming-edge correction.
source:
  git_revision: b02596a4dc6a9ce2c28ff3780762a39aef943820
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
    sha256: aafa11dd6f511bbab3d8ce7c5281a5e2b9391c27c8e0a92b6dd846d8c9b6dceb
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 166b69bc3190175dbc49a749ccc5bc5bfbadf464b66db46873e392e8184ddf60
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
  - path: data/habitats/aquatic/coastal_sea_water.yaml
    sha256: d61837f21dfc72e618854ff2a346900e21ca4a928fc763a6c87973559544dafc
    role: context
  - path: data/habitats/aquatic/liquid_water.yaml
    sha256: b91ec338644558b9184fbbb52ace39758ffacaf10f76eb8c52bd854a389c9fd2
    role: context
  - path: data/habitats/aquatic/saline_water.yaml
    sha256: 0114f8f1def88f8f8ce2b675bdd8b96e44ca92248424969288ebaa803fa8c248
    role: context
  - path: data/habitats/aquatic/sea_water.yaml
    sha256: 7bbf23f757f65b7e0597904571054832f16b405bf5183afb06c60fc7d3724ecc
    role: context
  - path: data/habitats/aquatic/sediment__e3709872.yaml
    sha256: cddcea912825338018d5985c28f327df993c2ec0e321167d4e008e2b59e88b13
    role: target
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
  - path: reports/yaml_record_review/20261005T214517Z-sediment__e3709872.md
    sha256: 99e665047ca684e4aa538398afa1499f49973c8635a6db7f35508a7e1af2102f
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
- target_id: habitatmech:GOLD.9df2041479
  path: data/habitats/aquatic/sediment__e3709872.yaml
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
    role: Generated construction
scope:
  description: Complete resolved record and its sole source concept, with bounded
    authority checks.
  selection: 'Next forty records lacking a completed individual scientific review
    in stable repository-relative path order. Each target is assessed separately;
    this does not establish category-wide scientific correctness. Starting coverage:
    848/3208 distinct individually reviewed records.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.9df2041479
  exclusions:
  - target: Other 3207 current records
    reason: Ancestor/context inspection is not complete target review.
checks:
- check_id: C0
  name: Native validation gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.9df2041479
  command: env RECORD_REVIEW_BASE=b02596a4dc6a9ce2c28ff3780762a39aef943820 just validate
    data/habitats/aquatic/sediment__e3709872.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T12:40:23.607950Z to 2026-10-12T12:40:25.373225Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C1
  name: Native validation gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.9df2041479
  command: env RECORD_REVIEW_BASE=b02596a4dc6a9ce2c28ff3780762a39aef943820 just validate-strict
    data/habitats/aquatic/sediment__41657647.yaml data/habitats/aquatic/sediment__46eca6b1.yaml
    data/habitats/aquatic/sediment__4985d562.yaml data/habitats/aquatic/sediment__4afb1aae.yaml
    data/habitats/aquatic/sediment__4d63a226.yaml data/habitats/aquatic/sediment__4dfcbb19.yaml
    data/habitats/aquatic/sediment__4ec76487.yaml data/habitats/aquatic/sediment__51ff1590.yaml
    data/habitats/aquatic/sediment__5561a5d1.yaml data/habitats/aquatic/sediment__58c2d02d.yaml
    data/habitats/aquatic/sediment__5ef6feae.yaml data/habitats/aquatic/sediment__69d4893f.yaml
    data/habitats/aquatic/sediment__6e0c4228.yaml data/habitats/aquatic/sediment__6e93a95d.yaml
    data/habitats/aquatic/sediment__7288ec0e.yaml data/habitats/aquatic/sediment__745f8d63.yaml
    data/habitats/aquatic/sediment__74d34b20.yaml data/habitats/aquatic/sediment__7b762d48.yaml
    data/habitats/aquatic/sediment__7b8eb154.yaml data/habitats/aquatic/sediment__7e21c5d8.yaml
    data/habitats/aquatic/sediment__8cbae4cd.yaml data/habitats/aquatic/sediment__8e884524.yaml
    data/habitats/aquatic/sediment__8f9b6931.yaml data/habitats/aquatic/sediment__94b343a0.yaml
    data/habitats/aquatic/sediment__978ea781.yaml data/habitats/aquatic/sediment__a24ea793.yaml
    data/habitats/aquatic/sediment__a36658ce.yaml data/habitats/aquatic/sediment__a4ddb224.yaml
    data/habitats/aquatic/sediment__a8039b03.yaml data/habitats/aquatic/sediment__b9940958.yaml
    data/habitats/aquatic/sediment__bbedc720.yaml data/habitats/aquatic/sediment__bf1216c6.yaml
    data/habitats/aquatic/sediment__cd41307f.yaml data/habitats/aquatic/sediment__ce4efe59.yaml
    data/habitats/aquatic/sediment__d5068bb8.yaml data/habitats/aquatic/sediment__d851e63e.yaml
    data/habitats/aquatic/sediment__dc3822ec.yaml data/habitats/aquatic/sediment__e3709872.yaml
    data/habitats/aquatic/sediment__e51105ff.yaml data/habitats/aquatic/sediment__e63c4954.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T12:40:29.018560Z to 2026-10-12T12:40:35.990580Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C2
  name: Native validation gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.9df2041479
  command: env RECORD_REVIEW_BASE=b02596a4dc6a9ce2c28ff3780762a39aef943820 just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T12:40:35.991426Z to 2026-10-12T12:40:50.457488Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C3
  name: Native validation gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.9df2041479
  command: env RECORD_REVIEW_BASE=b02596a4dc6a9ce2c28ff3780762a39aef943820 just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T12:40:50.458224Z to 2026-10-12T12:41:52.821380Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C4
  name: Native validation gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.9df2041479
  command: env RECORD_REVIEW_BASE=b02596a4dc6a9ce2c28ff3780762a39aef943820 just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T12:41:52.822147Z to 2026-10-12T12:41:59.333576Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C5
  name: Native validation gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.9df2041479
  command: env RECORD_REVIEW_BASE=b02596a4dc6a9ce2c28ff3780762a39aef943820 just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T12:41:59.334281Z to 2026-10-12T12:42:03.081279Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C6
  name: Native validation gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.9df2041479
  command: env RECORD_REVIEW_BASE=b02596a4dc6a9ce2c28ff3780762a39aef943820 just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T12:42:03.082126Z to 2026-10-12T12:42:17.438355Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C7
  name: Native validation gate
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.9df2041479
  command: env RECORD_REVIEW_BASE=b02596a4dc6a9ce2c28ff3780762a39aef943820 just provenance-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T12:42:17.439209Z to 2026-10-12T12:42:17.918358Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C8
  name: Exact-base CI QC evidence
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.9df2041479
  command: gh run view 38247399033 --repo CultureBotAI/HabitatMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T12:38:42.872938Z to 2026-10-12T12:38:45.642655Z.
    All three required merge-group workflows passed at the exact captured base; authoritative
    QC passed 1052 tests with 3 skipped. Newly saved review bundles require their
    own integrity check. Earlier CI does not validate these new bundles.
  evidence_ids:
  - R
  - RULES
- check_id: ORIGINAL
  name: Original occurrence-input recovery
  required: false
  status: unavailable
  target_ids:
  - habitatmech:GOLD.9df2041479
  summary: Original checkout cannot be traversed due to Operation not permitted; temporary
    source search is bounded and does not prove global absence.
  evidence_ids:
  - SEARCH
- check_id: IMODULON
  name: Claim-specific expression-module query
  required: false
  status: not_applicable
  target_ids:
  - habitatmech:GOLD.9df2041479
  summary: No exact organism/dataset/gene claim requiring this adapter.
  evidence_ids:
  - R
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/aquatic/sediment__e3709872.yaml
  summary: Coastal sediment is not coastal sea water ENVO:00002150. The modal source
    marine-benthic annotations do not make water a material genus and include an obsolete
    local term not emitted here. Keep ontology/source refresh separate from the exact
    incoming-edge correction.
  accessed_at: '2026-10-12T12:50:39.660095Z'
  support: supports
  locator: Entire captured YAML, including attestations and generated history
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml
  summary: Applied strict-parent, source comparison endpoint, MIxS-role, source-count/unit,
    evidence and ITEM lifecycle rules.
  accessed_at: '2026-10-12T12:50:39.660095Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0",
    "canonical_path": "Environmental > Aquatic > Marine > Coastal > Sediment", "depth":
    "5", "ecosystem": "Environmental", "ecosystem_category": "Aquatic", "ecosystem_subtype":
    "Coastal", "ecosystem_type": "Marine", "gold_node_count": "1", "gold_node_ids":
    "gold.ecosystem:4045", "leaf_label": "Sediment", "organism_count": "295", "specific_ecosystem":
    "Sediment", "study_count": "0", "total_assertions": "295"}, "logical_row": 95}],
    "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "572", "canonical_path":
    "Environmental > Aquatic > Marine > Coastal > Sediment", "ecosystem_path_id":
    "4045"}, "logical_row": 58}], "data/raw/gold_path_triads.tsv": [{"data": {"canonical_path":
    "Environmental > Aquatic > Marine > Coastal > Sediment", "distinct_terms": "4",
    "samples": "377", "slot": "broad", "studies": "33", "studies_agreeing": "23",
    "top_label": "marine benthic biome", "top_share": "0.86", "top_term": "ENVO:01000024"},
    "logical_row": 455}, {"data": {"canonical_path": "Environmental > Aquatic > Marine
    > Coastal > Sediment", "distinct_terms": "7", "samples": "377", "slot": "local",
    "studies": "33", "studies_agreeing": "22", "top_label": "marine benthic feature",
    "top_share": "0.82", "top_term": "ENVO:01000105"}, "logical_row": 456}, {"data":
    {"canonical_path": "Environmental > Aquatic > Marine > Coastal > Sediment", "distinct_terms":
    "6", "samples": "377", "slot": "medium", "studies": "33", "studies_agreeing":
    "28", "top_label": "marine sediment", "top_share": "0.94", "top_term": "ENVO:03000033"},
    "logical_row": 457}]}'
  accessed_at: '2026-10-12T12:50:39.660095Z'
  support: supports
  locator: Exact logical TSV rows, header=row1
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": ["ENVO:00002007"], "extra_xrefs": [],
    "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.9df2041479", "mapping_predicate":
    "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"},
    "automatic": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": ["ENVO:00002007"], "extra_xrefs": [], "grounding_status": "NARROW",
    "identifier": "habitatmech:GOLD.9df2041479", "mapping_predicate": "skos:narrowMatch",
    "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "minted": "habitatmech:GOLD.9df2041479",
    "source": "GOLD", "source_id": "gold.ecosystem:4045"}], "source_concepts": 1}'
  accessed_at: '2026-10-12T12:50:39.660095Z'
  support: supports
  locator: Full parsed target reconstruction and executed resolver routes; not recovery
    of original source membership
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl
  summary: '{"ENVO:00002006": {"definitions": ["An environmental material primarily
    composed of dihydrogen oxide in its liquid form."], "deprecated": [], "equivalents":
    [], "labels": ["liquid water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000815",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_15377"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": ["water"], "hasExactSynonym":
    [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002007": {"definitions":
    ["Particulate environmental material which is formed as a result of the transport
    and deposition of particles by flowing liquid."], "deprecated": [], "equivalents":
    [], "labels": ["sediment"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000060",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000086"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PATO_0000984"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [],
    "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002010": {"definitions":
    ["Water which contains a significant concentration of dissolved salts."], "deprecated":
    [], "equivalents": [], "labels": ["saline water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/ENVO_02000200"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_26710"]},
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000086"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PATO_0001657"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["salt
    water"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002149": {"definitions":
    ["Water which has physicochemical properties that have been determined by the
    processes occuring in a sea or ocean."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002010"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#unionOf":
    [{"nested": true}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}],
    "labels": ["sea water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002010",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#unionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00000015"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    ["http://purl.obolibrary.org/obo/ENVO_00000016"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest":
    ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}]}], "replacements": [],
    "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["ocean water", "seawater"],
    "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002150": {"definitions":
    ["Coastal sea water is sea water that is adjacent to a coast."], "deprecated":
    [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"],
    "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    ["http://purl.obolibrary.org/obo/ENVO_00002149"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0002220"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_00000303"]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest":
    ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["coastal
    sea water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002149", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0002220"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_00000303"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": ["coastal water"], "hasExactSynonym": ["coastal ocean water",
    "coastal oceanic water", "coastal seawater"], "hasNarrowSynonym": [], "hasRelatedSynonym":
    []}}, "ENVO:03000033": {"definitions": ["Sediment which has been transported through
    the marine water column, settling on the seafloor."], "deprecated": [], "equivalents":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"],
    "http://www.w3.org/2002/07/owl#unionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"],
    "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    ["http://purl.obolibrary.org/obo/ENVO_00002007"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"nested": true}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest":
    ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002007"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"nested": true}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest":
    ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["marine sediment"],
    "parents": ["http://purl.obolibrary.org/obo/ENVO_00002007", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0002220"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_00001999"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0002353"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_03000036"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": [], "hasExactSynonym": ["marine sediments"], "hasNarrowSynonym":
    [], "hasRelatedSynonym": []}}}'
  accessed_at: '2026-10-12T12:37:33.062486Z'
  support: supports
  locator: Current official OWL labels, definitions, typed synonyms, named parents
    and separate restrictions; candidates are not exact matches by implication
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats/aquatic/coastal_sea_water.yaml; data/habitats/aquatic/sea_water.yaml;
    data/habitats/aquatic/saline_water.yaml; data/habitats/aquatic/liquid_water.yaml;
    data/habitats/terrestrial/sediment.yaml
  summary: '{"ENVO:00002006": {"curation_history": [{"action": "REVIEW", "changes":
    "Reviewed and endorsed the seeder''s own resolution. Co-attestor review (#12):
    ''water'' resolves to ENVO:00002006 ''liquid water''. The term adds ''liquid'',
    which the key does not say, but every parameter band on the row is a property
    of liquid water and the table has separate rows for ice. Correct as seeded. (source
    concept habitatmech:ENVIRONMENTS_TABLE.97e0db4016)", "curator": "claude-opus-5",
    "timestamp": "2026-08-15T00:00:00Z"}, {"action": "REVIEW", "changes": "Reviewed
    and endorsed the seeder''s own resolution. Co-attestor review (#12): this source
    names the ontology CURIE itself, so its grounding is definitional rather than
    a lexical guess \u2014 the record IS the term the source pointed at. Recorded
    so the record it co-attests can reach REVIEWED, which needs every source concept
    decided. (source concept habitatmech:MADIN.ee80f974c2)", "curator": "claude-opus-5",
    "timestamp": "2026-08-15T00:00:00Z"}, {"action": "REVIEW", "changes": "Reviewed
    and endorsed the seeder''s own resolution. Co-attestor review (#12): this source
    names the ontology CURIE itself, so its grounding is definitional rather than
    a lexical guess \u2014 the record IS the term the source pointed at. Recorded
    so the record it co-attests can reach REVIEWED, which needs every source concept
    decided. (source concept habitatmech:PREGO.9c5507e85a)", "curator": "claude-opus-5",
    "timestamp": "2026-08-15T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES", "changes":
    "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE, MADIN, PREGO.
    Grounding: EXACT.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"},
    {"action": "ADD_CAUSAL_GRAPH", "changes": "Added a liquid-water planktonic solute-foraging
    graph backed by PMID:15306380, PMID:25500507, PMID:21663439, PMID:21329211, PMID:23118182,
    PMID:23204367, and DOI:10.3354/meps010257.", "curator": "codex", "llm_assisted":
    true, "timestamp": "2026-09-04T00:00:00Z"}, {"action": "REVISE_CAUSAL_GRAPH",
    "changes": "Bounded the graph to a conditional marine water-column model under
    issue 1263. Distinguished liquid phase from water activity and suspended from
    sinking particles; represented connected habitat, bacterial community and biomass-production
    process without physical STATE nodes; retargeted the growth edge to biomass production
    and separated uptake from carbon incorporation. Preserved graph, node and edge
    IDs and existing citations; added claim-level support from inspected Stocker and
    Seymour full text.", "curator": "codex-gpt-5", "llm_assisted": true, "timestamp":
    "2026-10-12T00:00:00Z"}], "definition": "An environmental material primarily composed
    of dihydrogen oxide in its liquid form.", "grounding_status": "EXACT", "label":
    "liquid water", "parent_habitats": ["ENVO:01000815"]}, "ENVO:00002007": {"curation_history":
    [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by ENVIRONMENTS_TABLE, MADIN, PREGO. Grounding: EXACT.", "curator": "seed_from_sources",
    "timestamp": "2026-08-16T05:58:02Z"}, {"action": "ADD_CAUSAL_GRAPH", "changes":
    "Added a sediment porewater redox-ladder graph backed by PMID:31388058, PMID:15618510,
    and PMID:35308366.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-04T00:00:00Z"}],
    "definition": "Particulate environmental material which is formed as a result
    of the transport and deposition of particles by flowing liquid.", "grounding_status":
    "EXACT", "label": "sediment", "parent_habitats": ["ENVO:01000060"]}, "ENVO:00002010":
    {"curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from
    data/raw/ inventories; attested by ENVIRONMENTS_TABLE, PREGO. Grounding: EXACT.",
    "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}], "definition":
    "Water which contains a significant concentration of dissolved salts.", "grounding_status":
    "EXACT", "label": "saline water", "parent_habitats": ["ENVO:00002006"]}, "ENVO:00002149":
    {"curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from
    data/raw/ inventories; attested by ENVIRONMENTS_TABLE, MADIN, PREGO. Grounding:
    EXACT.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"},
    {"action": "ADD_CAUSAL_GRAPH", "changes": "Added a seawater dissolved-organic-matter
    and oligotrophic-uptake graph backed by PMID:26951682, PMID:19805210, PMID:34010286,
    and PMID:16109880.", "curator": "codex", "llm_assisted": true, "timestamp": "2026-09-04T00:00:00Z"},
    {"action": "REVISE_CAUSAL_GRAPH", "changes": "Corrected node scope and genome
    trait typing for issue #2025. Preserved graph/node/edge IDs and all four publication
    references; separated the Pelagibacter example, comparative strategy evidence,
    modeled transport and inferred community-level linkage. No taxonomic grounding
    was invented.", "curator": "codex-gpt-5", "llm_assisted": true, "timestamp": "2026-10-12T00:00:00Z"}],
    "definition": "Water which has physicochemical properties that have been determined
    by the processes occuring in a sea or ocean.", "grounding_status": "EXACT", "label":
    "sea water", "parent_habitats": ["ENVO:00002010"]}, "ENVO:00002150": {"curation_history":
    [{"action": "GROUND", "changes": "Grounded to ENVO:00002150 ''coastal sea water''
    (CLOSE). GOLD''s Marine > Coastal zone. ENVO:00002150 names the water body specifically
    while GOLD''s node is the zone, so CLOSE rather than EXACT. (source concept habitatmech:GOLD.1a3d0aff0c)",
    "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "GROUND",
    "changes": "Grounded to ENVO:00002150 ''coastal sea water'' (CLOSE). The neritic
    zone is the region; ENVO names the water body, so CLOSE. Path: Environmental >
    Aquatic > Marine > Neritic zone/Coastal water (source concept habitatmech:GOLD.89754b31f3)",
    "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "GROUND",
    "changes": "Grounded to ENVO:00002150 ''coastal sea water'' (CLOSE). The neritic
    zone is the region; ENVO names the water body, so CLOSE. Path: Environmental >
    Aquatic > Marine > Littoral zone > Neritic zone/Coasta (source concept habitatmech:GOLD.ad324e6267)",
    "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "REVIEW",
    "changes": "Reviewed and endorsed the seeder''s own resolution. PREGO asserts
    ENVO:00002150 coastal sea water directly; the self-grounding is correct. Endorsed
    to complete the coastal record. (source concept habitatmech:PREGO.0da0bcd805)",
    "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD, PREGO. Grounding:
    EXACT.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"},
    {"action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained GOLD label ''Coastal''
    as RELATED_SYNONYM: a CLOSE source mapping does not establish exact lexical equivalence.
    Independent ontology synonyms and verbatim attestations are preserved (#1459).",
    "curator": "seed_from_sources", "timestamp": "2026-10-07T00:00:00Z"}, {"action":
    "SOURCE_SYNONYM_SCOPED", "changes": "Retained GOLD label ''Neritic zone/Coastal
    water'' as RELATED_SYNONYM: a CLOSE source mapping does not establish exact lexical
    equivalence. Independent ontology synonyms and verbatim attestations are preserved
    (#1459).", "curator": "seed_from_sources", "timestamp": "2026-10-07T00:00:00Z"},
    {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent
    contribution ENVO:00001999 for habitatmech:GOLD.1a3d0aff0c (Environmental > Aquatic
    > Marine > Coastal). ITEM hierarchy assessment: https://github.com/CultureBotAI/HabitatMech/issues/1987
    (20261012T001621Z-coastal_sea_water). ENVO denotes sea-water material near a coast.
    GOLD Coastal and Coastal zone are place-based bins, including sediment examples
    in the later export, not coextensive water-material classes. CLOSE does not establish
    identity. The marine-water-body and littoral-zone parents are context, while sea
    water is a defensible genus. Official coastal water is a broad synonym, not exact.
    Exclude only this guarded GOLD source-parent contribution. Preserve independent
    parents, frozen source identity/counts/units or omissions and native lifecycle.
    Later examples do not reconstruct frozen membership; shared synonym and endpoint
    issues remain separate.", "curator": "codex-gpt-5", "timestamp": "2026-10-12T00:00:00Z"},
    {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent
    contribution ENVO:00001999 for habitatmech:GOLD.89754b31f3 (Environmental > Aquatic
    > Marine > Neritic zone/Coastal water). ITEM hierarchy assessment: https://github.com/CultureBotAI/HabitatMech/issues/1987
    (20261012T001621Z-coastal_sea_water). ENVO denotes sea-water material near a coast.
    GOLD Coastal and Coastal zone are place-based bins, including sediment examples
    in the later export, not coextensive water-material classes. CLOSE does not establish
    identity. The marine-water-body and littoral-zone parents are context, while sea
    water is a defensible genus. Official coastal water is a broad synonym, not exact.
    Exclude only this guarded GOLD source-parent contribution. Preserve independent
    parents, frozen source identity/counts/units or omissions and native lifecycle.
    Later examples do not reconstruct frozen membership; shared synonym and endpoint
    issues remain separate.", "curator": "codex-gpt-5", "timestamp": "2026-10-12T00:00:00Z"},
    {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent
    contribution ENVO:01000125 for habitatmech:GOLD.ad324e6267 (Environmental > Aquatic
    > Marine > Littoral zone > Neritic zone/Coastal water). ITEM hierarchy assessment:
    https://github.com/CultureBotAI/HabitatMech/issues/1987 (20261012T001621Z-coastal_sea_water).
    ENVO denotes sea-water material near a coast. GOLD Coastal and Coastal zone are
    place-based bins, including sediment examples in the later export, not coextensive
    water-material classes. CLOSE does not establish identity. The marine-water-body
    and littoral-zone parents are context, while sea water is a defensible genus.
    Official coastal water is a broad synonym, not exact. Exclude only this guarded
    GOLD source-parent contribution. Preserve independent parents, frozen source identity/counts/units
    or omissions and native lifecycle. Later examples do not reconstruct frozen membership;
    shared synonym and endpoint issues remain separate.", "curator": "codex-gpt-5",
    "timestamp": "2026-10-12T00:00:00Z"}], "definition": "Coastal sea water is sea
    water that is adjacent to a coast.", "grounding_status": "EXACT", "label": "coastal
    sea water", "parent_habitats": ["ENVO:00002149"]}}'
  accessed_at: '2026-10-12T12:50:39.660095Z'
  support: supports
  locator: Ancestor context only, not additional complete scientific review coverage
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  summary: 'Exact positional-path census={"Biosample": 666, "Organism": 241, "SequencingProject":
    1025}; inspected first up-to-three BioSample/Organism metadata examples={"Biosample":
    [{"data": {"BIOSAMPLE GOLD ID": "Gb0053374", "BIOSAMPLE NAME": "Marine sediment
    microbial community from Cabo Rojo, Puerto Rico - PR CR 10% Liquid 1", "BIOSAMPLE
    NCBI TAX NAME": "marine metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Cabo
    Rojo, Puerto Rico"}, "row": 2024}, {"data": {"BIOSAMPLE GOLD ID": "Gb0112468",
    "BIOSAMPLE NAME": "Marine sediment microbial communities from the Atlantic coast
    under amendment with organic carbon and nitrate - tdAd00.1", "BIOSAMPLE NCBI TAX
    NAME": "marine sediment metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Marine
    sediment"}, "row": 7373}, {"data": {"BIOSAMPLE GOLD ID": "Gb0112469", "BIOSAMPLE
    NAME": "Marine sediment microbial communities from the Atlantic coast under amendment
    with organic carbon and nitrate - tdAd00.2", "BIOSAMPLE NCBI TAX NAME": "marine
    sediment metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Marine sediment"},
    "row": 7374}], "Organism": [{"data": {"ORGANISM GOLD ID": "Go0001511", "ORGANISM
    HABITAT": "Aquatic|Mud|Soil|Host|Fresh water", "ORGANISM NAME": "Acetoanaerobium
    sticklandii DSM 519", "ORGANISM SAMPLE COLLECTION SITE": "Mud water"}, "row":
    1370}, {"data": {"ORGANISM GOLD ID": "Go0011444", "ORGANISM HABITAT": "Marine",
    "ORGANISM NAME": "candidate division WS3 bacterium SCGC AAA257-D15", "ORGANISM
    SAMPLE COLLECTION SITE": "Aarhus Bay"}, "row": 10057}, {"data": {"ORGANISM GOLD
    ID": "Go0013808", "ORGANISM HABITAT": "Marine|Sediment|Aquatic", "ORGANISM NAME":
    "Desulfatibacillum aliphaticivorans DSM 15576", "ORGANISM SAMPLE COLLECTION SITE":
    "Marine sediment"}, "row": 12192}]}. Later BioSample examples include amended
    sediments; laboratory manipulations are not natural class-wide properties. Remaining
    members and joined studies were indexed, not individually assessed.'
  accessed_at: '2026-10-11T13:21:51.155056Z'
  support: supports
  locator: Official export retrieved 11-Oct, advertised generated 10-Oct; not original
    August membership; contacts excluded
  snapshot_sha256: b222fa9df89ffbd1a30897a1e7302da363c57b463d9948ecc9bfcb9304b4a96f
- evidence_id: CLASS
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  summary: '[{"row": 684, "slug": "sediment__e3709872", "path": "Environmental > Aquatic
    > Marine > Coastal > Sediment", "values": ["4045", "Environmental", "Aquatic",
    "Marine", "Coastal", "Sediment"]}]'
  accessed_at: '2026-10-12T12:37:34.562371Z'
  support: supports
  locator: Exact five-position ecosystem tuples; not organism membership or certification
    of all historical node IDs
  snapshot_sha256: 3937335bc3919f62d2596a8ea8a77ccc97402c951239ee5ac2869539861733b3
- evidence_id: MIXS
  kind: authority
  reference: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
  summary: Broad ecosystem, local feature and sampled material describe different
    environmental roles; association is not automatically class identity or strict
    ancestry.
  accessed_at: '2026-10-12T12:37:34.720812Z'
  support: supports
  locator: ENVO environmental-triad guidance
  snapshot_sha256: ac4026149c78705b7b40e67ddefd24df39e7e2e7290fba91a3d68309d7ba1a42
- evidence_id: SEARCH
  kind: search
  reference: curation; history; research; reports; reviews; data/raw; data/habitats;
    conf
  summary: Ignored/hidden-inclusive identifier, label, slug and source-path searches
    across these roots found no prior structured review for this exact target. Legacy
    Findings sections were read; full bibliographies were not revalidated. Original
    Documents checkout is inaccessible, not demonstrated absent. The temporary checkout
    lacks original GOLD dump files in the bounded filename search.
  accessed_at: '2026-10-12T12:50:39.660095Z'
  support: supports
  locator: Search receipts retained in temporary assessment workspace
  search_scope: Ignored/hidden-inclusive identifier, label, slug and source-path searches
    across these roots found no prior structured review for this exact target. Legacy
    Findings sections were read; full bibliographies were not revalidated. Original
    Documents checkout is inaccessible, not demonstrated absent. The temporary checkout
    lacks original GOLD dump files in the bounded filename search.
- evidence_id: ISSUES
  kind: database
  reference: https://github.com/CultureBotAI/HabitatMech/issues
  summary: Fetched 989 all-state issue titles/bodies; inspected relevant exact-source
    issue bodies as leads. No exhaustive comment crawl. Issue state is not scientific
    disposition.
  accessed_at: '2026-10-12T12:50:39.660095Z'
  support: context_only
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Qualified sediment identity and source scope
  outcome: supported
  summary: The complete record retains the exact GOLD path and source mint as an AQUATIC
    sediment habitat. It is not asserted as water, a containing feature or an exact
    candidate ontology identity. Coastal sediment is not coastal sea water ENVO:00002150.
    The modal source marine-benthic annotations do not make water a material genus
    and include an obsolete local term not emitted here. Keep ontology/source refresh
    separate from the exact incoming-edge correction.
  target_ids:
  - habitatmech:GOLD.9df2041479
  evidence_ids:
  - R
  - RAW
  - CLASS
- assessment_id: HIERARCHY
  area: grounding
  topic: Independent genus and context contributions
  outcome: concern
  summary: Coastal sediment is not coastal sea water ENVO:00002150. The modal source
    marine-benthic annotations do not make water a material genus and include an obsolete
    local term not emitted here. Keep ontology/source refresh separate from the exact
    incoming-edge correction.
  target_ids:
  - habitatmech:GOLD.9df2041479
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
  - CODE
- assessment_id: ENDPOINT
  area: grounding
  topic: Attestation comparison endpoint
  outcome: concern
  summary: All NARROW routes retain a source identity while using a broader ontology
    comparison; the emitted contract does not distinguish these endpoints.
  target_ids:
  - habitatmech:GOLD.9df2041479
  evidence_ids:
  - R
  - RULES
  - CODE
- assessment_id: PROVENANCE
  area: provenance
  topic: Frozen source accounting and lifecycle
  outcome: supported
  summary: The full target reproduces with 1 source concept and 0 ITEM-reviewed contributors.
    Counts and units match frozen inputs; omitted counts are not biological zero.
    Later sample/organism counts do not reconstruct those historical assertions. REVIEWED
    is a decision-coverage gate, not scientific approval.
  target_ids:
  - habitatmech:GOLD.9df2041479
  evidence_ids:
  - R
  - RAW
  - CODE
  - BULK
- assessment_id: SOURCE_SCOPE
  area: evidence
  topic: Original occurrence membership versus later examples
  outcome: unknown
  summary: Later BioSample examples include amended sediments; laboratory manipulations
    are not natural class-wide properties. Original source occurrence inputs are inaccessible;
    no source-count correction is inferred.
  target_ids:
  - habitatmech:GOLD.9df2041479
  evidence_ids:
  - RAW
  - BULK
  - CLASS
  - SEARCH
- assessment_id: COMPLETENESS
  area: completeness
  topic: Optional data and structured adapter applicability
  outcome: supported
  summary: No authored definition, taxa, parameter, graph, gene or expression claim
    is emitted. Optional missing slots are not automatic defects. No iModulonDB query
    applies; no negative biological inference is made.
  target_ids:
  - habitatmech:GOLD.9df2041479
  evidence_ids:
  - R
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: habitatmech-gold.9df2041479-mapping-endpoint-contract
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: NARROW attestation does not expose its actual broader comparison endpoint
  description: The schema defines mapping_predicate from source_id to this record
    identifier, while the executed narrow route retains the source mint and compares
    it to a broader ontology parent. The target ID is therefore ambiguous under the
    advertised contract. This is a representation mismatch, not a claim that every
    reflexive SKOS statement is formally inconsistent; changing only the predicate
    is not a complete repair.
  target_ids:
  - habitatmech:GOLD.9df2041479
  field_paths:
  - source_attestations.mapping_predicate
  - grounding_status
  evidence_ids:
  - R
  - RULES
  - RAW
  - CODE
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Attestation comparison endpoint contract
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: NARROW route and emitted mapping endpoint
  rule_id: docs/CURATION.md; SourceAttestation.mapping_predicate
  native_severity: major
  normalization_reason: Materially unsupported genus or comparison-endpoint contract.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
- finding_id: F2
  issue_key: habitatmech-gold.9df2041479-gold-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: GOLD context is not an established strictly broader material class
  description: Coastal sediment is not coastal sea water ENVO:00002150. The modal
    source marine-benthic annotations do not make water a material genus and include
    an obsolete local term not emitted here. Keep ontology/source refresh separate
    from the exact incoming-edge correction.
  target_ids:
  - habitatmech:GOLD.9df2041479
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
    role: Exact source-path parent contribution
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Independent GOLD hierarchy pass
  rule_id: docs/CURATION.md; SourceAttestation.mapping_predicate
  native_severity: major
  normalization_reason: Materially unsupported genus or comparison-endpoint contract.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1523
actions:
- action_id: A1
  description: 'Resolve shared issue #1398 with explicit source-to-record versus source-to-ontology
    comparison semantics and downstream export regression tests. Do not infer SSSOM/KGX
    readiness from this record review.'
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.9df2041479
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Attestation comparison endpoint contract
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: NARROW route and emitted mapping endpoint
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Reassess the exact source and contribution; preserve independent true genera,
    qualified identity, source counts/units and omitted counts.
  - Change maintained inputs with append-only curation history, never generated YAML
    or existing review bundles.
  - Add focused regression tests, inspect an exact seed canary, regenerate guarded
    products, and pass schema, strict, label, history, provenance, corpus reproduction
    and QC gates.
  - Save a linked successor observation for any disposition. No proposed repair was
    executed during this assessment.
- action_id: A2
  description: Assess and exclude only the unsupported context contribution using
    its exact source path and expected resolved parent; retain source provenance and
    independently supported material genera.
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.9df2041479
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact source-path parent contribution
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Independent GOLD hierarchy pass
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Reassess the exact source and contribution; preserve independent true genera,
    qualified identity, source counts/units and omitted counts.
  - Change maintained inputs with append-only curation history, never generated YAML
    or existing review bundles.
  - Add focused regression tests, inspect an exact seed canary, regenerate guarded
    products, and pass schema, strict, label, history, provenance, corpus reproduction
    and QC gates.
  - Save a linked successor observation for any disposition. No proposed repair was
    executed during this assessment.
limitations:
- Clean GitHub origin/main snapshot. The original Documents checkout remains inaccessible;
  local uncommitted and ignored-only content there cannot be assessed.
- Completed individual assessment is self-review, not independent approval or whole-corpus
  certification.
- Only first up-to-three matching BioSample/Organism metadata descriptions per sheet
  were interpreted; remaining members, projects and joined studies were indexed only.
- Later GOLD export/classification does not reconstruct frozen August membership or
  certify every historical node live.
- Label correspondence passed with 1178 canonical pairs, one synonym, five accepted
  exceptions and 2057 no-adapter skips; skips are not scientific approval.
- 'SSSOM/KGX conformance to current kg-microbe modeling was not audited; shared issue
  #1398 remains open.'
- Legacy reports are leads; their complete bibliographies were not revalidated and
  old findings are not retired.
- No habitat, curation input, scientific status/history, generated product or GitHub
  issue was changed during this assessment.
notes:
- No prior structured observation for this exact target was found in the ignored-inclusive
  temporary-checkout search; no predecessor is silently superseded.
- Assessment phase was read-only. Later authorized publication or curation must preserve
  this historical observation.
tags:
- habitatmech
- aquatic
- record-review
- scientific-review
```
