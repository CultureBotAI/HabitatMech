# Scientific record review: marine_water_body

- Review: 20261012T054256Z-marine_water_body
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-12T05:19:15.702311Z
- Finished UTC: 2026-10-12T05:42:56.014225Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The physical lentic marine water body is not an aquatic biome. Preserve BacDive 2040 STRAIN, GOLD 6420 ORGANISM and PREGO 171 TAXON assertions, the two CLOSE source mappings and 50 selected associations. The revised 15-edge carbon-pump graph is explicitly conditional and its earlier unrelated citation is no longer active. Current node types still confuse ecological assemblages, habitats and enzyme products with taxa, exposures and a trait.

## Scope And Provenance

Entire exact generated record, all contributors and individual asserted causal edges, with bounded source-context assessment.

Selection: Next forty records without a completed individual scientific review in stable repository-relative path order: marine anoxic zone through microbial_mats__200e1828. Full individual observations, not a category-wide pass. Prior coverage counts distinct observations, not a clean current-input corpus. Starting distinct-review coverage 688/3208 is not clean current-input coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ed9e0d0f382e4502a64f4de10102c4512bddca38.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00001999 | data/habitats/aquatic/marine_water_body.yaml | generated | marine water body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native gate on captured inputs | passed | True | ENVO:00001999 | Actual success 2026-10-12T05:22:17.396509Z to 2026-10-12T05:22:20.564796Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:00001999 | Actual success 2026-10-12T05:23:16.222412Z to 2026-10-12T05:23:26.347203Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:00001999 | Actual success 2026-10-12T05:23:26.348469Z to 2026-10-12T05:23:51.098950Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:00001999 | Actual success 2026-10-12T05:23:51.100146Z to 2026-10-12T05:25:01.530644Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:00001999 | Actual success 2026-10-12T05:25:01.532072Z to 2026-10-12T05:25:11.808379Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:00001999 | Actual success 2026-10-12T05:25:11.809657Z to 2026-10-12T05:25:19.058687Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:00001999 | Actual success 2026-10-12T05:25:19.059693Z to 2026-10-12T05:25:46.351294Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:00001999 | Actual success 2026-10-12T05:25:46.352569Z to 2026-10-12T05:25:47.389752Z. Native command scope retained. |
| Exact-base CI authoritative QC | passed | True | ENVO:00001999 | Actual success 2026-10-12T05:21:53.294030Z to 2026-10-12T05:21:55.368917Z. All three required merge-group workflows passed at the exact captured base; authoritative QC passed 913 tests with 3 skipped. Newly saved review bundles require their own integrity check. These newly saved review bundles were not part of that earlier exact-base CI run. |
| Complete target reconstruction | passed | False | ENVO:00001999 | All 40 complete documents matched; captured hashes rechecked before authoring. |
| Original assertion membership | unavailable | False | ENVO:00001999 | Bounded ignored-inclusive searches did not recover complete original assertion inputs; later exports are contextual evidence only. |
| Expression-adapter applicability | not_applicable | False | ENVO:00001999 | The successful 28-dataset inventory was read for graph scope. No matching claim-specific organism/strain/gene or expression-module assertion requires a search or summarize call. Absence is not negative ecological evidence. |

## Scientific And Domain Assessments

### marine_body_contains_euphotic_zone

evidence: supported. Targets: ENVO:00001999.

Herndl Fig1 supports the explicitly oceanic illuminated-water setting, not all marine water bodies.

### euphotic_zone_supports_marine_phytoplankton

evidence: supported. Targets: ENVO:00001999.

Arrigo pp350-351 supports light/resource dependence and co-limitation.

### phytoplankton_perform_oxygenic_photosynthesis

evidence: supported. Targets: ENVO:00001999.

NOAA Primary Production supports oxygenic carbon fixation by photosynthetic phytoplankton.

### photosynthesis_generates_particulate_carbon

evidence: supported. Targets: ENVO:00001999.

NOAA Primary Production supports biomass formation; the edge does not make all fixed carbon particulate.

### particulate_carbon_forms_sinking_particles

evidence: supported. Targets: ENVO:00001999.

Herndl introduction supports aggregation and detrital sinking, with nonsinking particles distinguished.

### sinking_particles_enter_dark_ocean

evidence: supported. Targets: ENVO:00001999.

Herndl introduction/Fig1 supports export below the euphotic zone.

### sinking_particles_select_particle_bacteria

evidence: supported. Targets: ENVO:00001999.

Herndl Microbial activity in the dark supports particle-associated activity, not selection sufficiency.

### particle_bacteria_express_extracellular_enzymes

evidence: supported. Targets: ENVO:00001999.

Herndl Microbial activity in the dark describes extracellular-enzyme release by particle-associated microbes.

### enzymes_release_dissolved_organic_matter

evidence: supported. Targets: ENVO:00001999.

Arnosti complete abstract supports hydrolysis to uptake-sized substrates, not a measured leakage flux.

### dissolved_organic_matter_supports_free_living_heterotrophs

evidence: supported. Targets: ENVO:00001999.

Herndl contrasts bioavailable substrates with refractory deep dissolved carbon.

### heterotrophs_drive_microbial_remineralization

evidence: supported. Targets: ENVO:00001999.

Arnosti abstract supports heterotrophic organic-matter processing without a measured free-living share.

### dark_ocean_hosts_remineralization

evidence: supported. Targets: ENVO:00001999.

Herndl introduction/Fig1 supports remineralization beneath the euphotic zone.

### remineralization_consumes_oxygen

evidence: supported. Targets: ENVO:00001999.

Arrigo Fig2 p351 supports oxygen use; the current edge is explicitly aerobic.

### remineralization_releases_dic

evidence: supported. Targets: ENVO:00001999.

Herndl introduction/Fig1 supports respiratory conversion to inorganic carbon.

### remineralization_regenerates_nutrients

evidence: supported. Targets: ENVO:00001999.

Arrigo p349 and Fig2 p351 support nitrogen/phosphorus regeneration without a universal ratio.

### Exact identity, definition and source intent

identity: supported. Targets: ENVO:00001999.

The physical lentic marine water body is not an aquatic biome. Preserve BacDive 2040 STRAIN, GOLD 6420 ORGANISM and PREGO 171 TAXON assertions, the two CLOSE source mappings and 50 selected associations. The revised 15-edge carbon-pump graph is explicitly conditional and its earlier unrelated citation is no longer active. Current node types still confuse ecological assemblages, habitats and enzyme products with taxa, exposures and a trait.

### Parent contributors and mapping endpoints

grounding: concern. Targets: ENVO:00001999.

The physical lentic marine water body is not an aquatic biome. Preserve BacDive 2040 STRAIN, GOLD 6420 ORGANISM and PREGO 171 TAXON assertions, the two CLOSE source mappings and 50 selected associations. The revised 15-edge carbon-pump graph is explicitly conditional and its earlier unrelated citation is no longer active. Current node types still confuse ecological assemblages, habitats and enzyme products with taxa, exposures and a trait. Ontology, GOLD path, ambiguous-leaf and authored-genus routes were distinguished.

### Source units and native lifecycle

provenance: supported. Targets: ENVO:00001999.

Complete reconstruction preserves 3 contributing concepts and 3 ITEM-reviewed contributors. Attestations=[{"source": "BACDIVE", "source_id": "bacdive.isolation_source:marine", "source_label": "Marine", "mapping_predicate": "skos:closeMatch", "assertion_count": 2040, "assertion_unit": "STRAIN"}, {"source": "GOLD", "source_id": "gold.ecosystem:3487", "source_label": "Marine", "source_path": "Environmental &gt; Aquatic &gt; Marine", "mapping_predicate": "skos:closeMatch", "assertion_count": 6420, "assertion_unit": "ORGANISM", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "PREGO", "source_id": "ENVO:00001999", "source_label": "marine water body", "assertion_count": 171, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "environmental_samples"}]. Counts with different units are not summed. Reproduction validates derivation, not the scientific truth of the mapping.

### Taxonomy and association scope

evidence: concern. Targets: ENVO:00001999.

All emitted identifiers resolve, including historical aliases. Source rows, ranks, scores and corroboration reproduce; these are selected associations, not proven characteristic taxa. Original occurrence evidence was not fully recovered, so no claim of exhaustive ecological validation is made. 158080 resolves to 141390 Chromohalobacter israelensis

### Optional slots and bounded evidence

completeness: supported. Targets: ENVO:00001999.

Optional empty fields alone are not defects. Every current graph edge has an individual assessment; node typing is assessed separately. Expression-module membership is not direct causal proof.

## Findings

### F1: Source context is emitted as a strict superclass

major / open / confirmed; issue key: envo-00001999-context-parent.

The physical lentic marine water body is not an aquatic biome. Preserve BacDive 2040 STRAIN, GOLD 6420 ORGANISM and PREGO 171 TAXON assertions, the two CLOSE source mappings and 50 selected associations. The revised 15-edge carbon-pump graph is explicitly conditional and its earlier unrelated citation is no longer active. Current node types still confuse ecological assemblages, habitats and enzyme products with taxa, exposures and a trait. Unsupported GOLD contributions: ENVO:00002030.

### F2: Historical taxonomy identifiers or names need versioned maintenance

minor / open / confirmed; issue key: envo-00001999-taxonomy-alias-maintenance.

158080 resolves to 141390 Chromohalobacter israelensis. The original IDs remain resolvable; this is not proof of a false habitat association.

### F3: Graph node types misrepresent habitats and functional assemblages

major / open / confirmed; issue key: envo-00001999-graph-node-type-scope.

Euphotic zone and dark ocean denote habitats rather than exposures/stressors. Phytoplankton, particle-associated bacteria and free-living heterotrophs are ecological assemblages, not single taxa. Extracellular enzymes are gene products or catalytic activities, not themselves a microbial trait. The previously fixed unrelated PMID remains only in preserved history.

## Recommended Actions And Acceptance Checks

### A1

Exclude only the specified GOLD contributions, retaining independent ontology/curator genera and source provenance. Where source specificity is unresolved, assess the source decision separately instead of treating an exclusion as proof of exact equivalence.

- Change only maintained owners after source-level assessment; retain independent true parents, source identity/count/unit provenance and lifecycle unless a separately justified change requires otherwise.
- Append required current history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, label, provenance, corpus reproduction, causal/history and full QC gates; save a linked successor for any finding disposition.

### A2

Use versioned taxonomy normalization, preserving original IDs/names, ranks, scores, source pools and corroboration. Test alias deduplication rather than guessing a replacement organism.

- Change only maintained owners after source-level assessment; retain independent true parents, source identity/count/unit provenance and lifecycle unless a separately justified change requires otherwise.
- Append required current history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, label, provenance, corpus reproduction, causal/history and full QC gates; save a linked successor for any finding disposition.

### A3

Use supported HABITAT/COMMUNITY/gene-product or process representations as appropriate; do not relabel ecological guilds as clades. Preserve supported causal meaning and recheck every affected edge.

- Change only maintained owners after source-level assessment; retain independent true parents, source identity/count/unit provenance and lifecycle unless a separately justified change requires otherwise.
- Append required current history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, label, provenance, corpus reproduction, causal/history and full QC gates; save a linked successor for any finding disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/aquatic/marine_water_body.yaml; Entire captured YAML read, including all taxa, parameters, graphs and generated history | supports | The physical lentic marine water body is not an aquatic biome. Preserve BacDive 2040 STRAIN, GOLD 6420 ORGANISM and PREGO 171 TAXON assertions, the two CLOSE source mappings and 50 selected associations. The revised 15-edge carbon-pump graph is explicitly conditional and its earlier unrelated citation is no longer active. Current node types still confuse ecological assemblages, habitats and enzyme products with taxa, exposures and a trait. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied exact identity, strict-genus, MIxS roles, source-unit/score and ITEM lifecycle contracts; graph node types retain their biological definitions. |
| RAW | data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; Exact logical TSV rows, header=row1; filtered by current source IDs and exact paths, not legacy issue line numbers | supports | {"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:BACDIVE.407144fe70", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row": 28}, {"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:GOLD.5856c699e4", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row": 552}, {"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:PREGO.a653eb2a85", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row": 1490}], "data/raw/bacdive_isolation_sources.tsv": [{"data": {"bacdive_id": "bacdive.isolation_source:marine", "label": "Marine", "source_slug": "marine", "strain_count": "2040", "taxon_count": "1805"}, "logical_row": 16}], "data/raw/bacdive_source_taxa.tsv": [{"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "1", "strain_count": "24", "taxon_id": "NCBITaxon:1876", "taxon_label": "Micromonospora sp."}, "logical_row": 1723}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "2", "strain_count": "14", "taxon_id": "NCBITaxon:83428", "taxon_label": "uncultured Bacillus sp."}, "logical_row": 1724}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "3", "strain_count": "11", "taxon_id": "NCBITaxon:1869227", "taxon_label": "bacterium"}, "logical_row": 1725}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "4", "strain_count": "11", "taxon_id": "NCBITaxon:562", "taxon_label": "Escherichia coli"}, "logical_row": 1726}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "5", "strain_count": "7", "taxon_id": "NCBITaxon:314275", "taxon_label": "Alteromonas mediterranea"}, "logical_row": 1727}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "6", "strain_count": "6", "taxon_id": "NCBITaxon:2", "taxon_label": "Bacteria"}, "logical_row": 1728}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "PREGO", "rank": "7", "strain_count": "6", "taxon_id": "NCBITaxon:28108", "taxon_label": "Alteromonas macleodii"}, "logical_row": 1729}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "8", "strain_count": "6", "taxon_id": "NCBITaxon:53249", "taxon_label": "Pseudoalteromonas sp."}, "logical_row": 1730}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "9", "strain_count": "5", "taxon_id": "NCBITaxon:50741", "taxon_label": "Marinobacter sp."}, "logical_row": 1731}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "10", "strain_count": "5", "taxon_id": "NCBITaxon:56811", "taxon_label": "Psychrobacter sp."}, "logical_row": 1732}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "11", "strain_count": "4", "taxon_id": "NCBITaxon:1211807", "taxon_label": "Stutzerimonas kunmingensis"}, "logical_row": 1733}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "12", "strain_count": "4", "taxon_id": "NCBITaxon:1871328", "taxon_label": "Kocuria sp."}, "logical_row": 1734}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "13", "strain_count": "4", "taxon_id": "NCBITaxon:1931", "taxon_label": "Streptomyces sp."}, "logical_row": 1735}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "14", "strain_count": "4", "taxon_id": "NCBITaxon:2024855", "taxon_label": "Rhodopirellula sp."}, "logical_row": 1736}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "15", "strain_count": "4", "taxon_id": "NCBITaxon:2099376", "taxon_label": "Desulforhopalus sp."}, "logical_row": 1737}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "16", "strain_count": "4", "taxon_id": "NCBITaxon:2213", "taxon_label": "Methanosarcina sp."}, "logical_row": 1738}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "17", "strain_count": "4", "taxon_id": "NCBITaxon:265606", "taxon_label": "Rhodopirellula baltica"}, "logical_row": 1739}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "PREGO", "rank": "18", "strain_count": "4", "taxon_id": "NCBITaxon:28258", "taxon_label": "Cobetia marina"}, "logical_row": 1740}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "19", "strain_count": "4", "taxon_id": "NCBITaxon:2926447", "taxon_label": "Marinispora"}, "logical_row": 1741}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "20", "strain_count": "4", "taxon_id": "NCBITaxon:44751", "taxon_label": "Exiguobacterium sp."}, "logical_row": 1742}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "21", "strain_count": "4", "taxon_id": "NCBITaxon:51671", "taxon_label": "Microbacterium sp."}, "logical_row": 1743}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "22", "strain_count": "4", "taxon_id": "NCBITaxon:885", "taxon_label": "Desulfovibrio sp."}, "logical_row": 1744}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "23", "strain_count": "3", "taxon_id": "NCBITaxon:1042", "taxon_label": "Erythrobacter sp."}, "logical_row": 1745}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "24", "strain_count": "3", "taxon_id": "NCBITaxon:1486246", "taxon_label": "Halomonas sp."}, "logical_row": 1746}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "25", "strain_count": "3", "taxon_id": "NCBITaxon:1703256", "taxon_label": "Pseudoalteromonas gelatinilytica"}, "logical_row": 1747}], "data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Environmental &gt; Aquatic &gt; Marine", "depth": "3", "ecosystem": "Environmental", "ecosystem_category": "Aquatic", "ecosystem_subtype": "", "ecosystem_type": "Marine", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:3487&#124;gold.ecosystem:3768&#124;gold.ecosystem:4003", "leaf_label": "Marine", "organism_count": "6420", "specific_ecosystem": "", "study_count": "0", "total_assertions": "6420"}, "logical_row": 8}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "5248", "canonical_path": "Environmental &gt; Aquatic &gt; Marine", "ecosystem_path_id": "4003"}, "logical_row": 8}], "data/raw/gold_path_triads.tsv": [{"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Marine", "distinct_terms": "11", "samples": "3749", "slot": "broad", "studies": "141", "studies_agreeing": "128", "top_label": "marine biome", "top_share": "0.96", "top_term": "ENVO:00000447"}, "logical_row": 434}, {"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Marine", "distinct_terms": "31", "samples": "3749", "slot": "local", "studies": "141", "studies_agreeing": "113", "top_label": "marine water body", "top_share": "0.79", "top_term": "ENVO:00001999"}, "logical_row": 435}, {"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Marine", "distinct_terms": "22", "samples": "3749", "slot": "medium", "studies": "141", "studies_agreeing": "109", "top_label": "sea water", "top_share": "0.87", "top_term": "ENVO:00002149"}, "logical_row": 436}], "data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:01000617", "predicate": "rdfs:subClassOf", "subject": "ENVO:00001999"}, "logical_row": 5261}], "data/raw/ontology_terms.tsv": [{"data": {"definition": "A lentic water body which is composed primarily of marine water.", "deprecated": "", "directly_referenced": "TRUE", "label": "marine water body", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "body of marine water&#124;marine waterbody", "term_id": "ENVO:00001999"}, "logical_row": 7158}], "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "1", "taxon_id": "NCBITaxon:102", "taxon_label": "Polaribacter glomeratus"}, "logical_row": 5366}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "2", "taxon_id": "NCBITaxon:1026", "taxon_label": "Marinoscillum furvescens"}, "logical_row": 5367}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "3", "taxon_id": "NCBITaxon:104268", "taxon_label": "Tenacibaculum mesophilum"}, "logical_row": 5368}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "4", "taxon_id": "NCBITaxon:107401", "taxon_label": "Tenacibaculum maritimum"}, "logical_row": 5369}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "5", "taxon_id": "NCBITaxon:111770", "taxon_label": "Thiothrix fructosivorans"}, "logical_row": 5370}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "6", "taxon_id": "NCBITaxon:114404", "taxon_label": "Edaphosphingomonas fennica"}, "logical_row": 5371}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "7", "taxon_id": "NCBITaxon:1282", "taxon_label": "Staphylococcus epidermidis"}, "logical_row": 5372}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "8", "taxon_id": "NCBITaxon:132144", "taxon_label": "Candidatus Glomeribacter gigasporarum"}, "logical_row": 5373}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "9", "taxon_id": "NCBITaxon:133924", "taxon_label": "Leisingera methylohalidivorans"}, "logical_row": 5374}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "10", "taxon_id": "NCBITaxon:13616", "taxon_label": ""}, "logical_row": 5375}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "11", "taxon_id": "NCBITaxon:1371", "taxon_label": "Marinococcus halophilus"}, "logical_row": 5376}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "12", "taxon_id": "NCBITaxon:143223", "taxon_label": "Salegentibacter salegens"}, "logical_row": 5377}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "13", "taxon_id": "NCBITaxon:156128", "taxon_label": ""}, "logical_row": 5378}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "14", "taxon_id": "NCBITaxon:156133", "taxon_label": ""}, "logical_row": 5379}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "15", "taxon_id": "NCBITaxon:158080", "taxon_label": ""}, "logical_row": 5380}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "16", "taxon_id": "NCBITaxon:158500", "taxon_label": "Novosphingobium resinovorum"}, "logical_row": 5381}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "17", "taxon_id": "NCBITaxon:168275", "taxon_label": "Psychromonas arctica"}, "logical_row": 5382}, {"data": {"channels": "environmental_samples", "corroborated_by": "BACDIVE", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "18", "taxon_id": "NCBITaxon:172371", "taxon_label": "Alloalcanivorax venustensis"}, "logical_row": 5383}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "19", "taxon_id": "NCBITaxon:173365", "taxon_label": "Methylobacter tundripaludum"}, "logical_row": 5384}, {"data": {"channels": "environmental_samples", "corroborated_by": "BACDIVE", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "20", "taxon_id": "NCBITaxon:180542", "taxon_label": "Salinisphaera shabanensis"}, "logical_row": 5385}, {"data": {"channels": "environmental_samples", "corroborated_by": "BACDIVE", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "21", "taxon_id": "NCBITaxon:184914", "taxon_label": "Corallococcus coralloides"}, "logical_row": 5386}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "22", "taxon_id": "NCBITaxon:186022", "taxon_label": "Thalassionema frauenfeldii"}, "logical_row": 5387}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "23", "taxon_id": "NCBITaxon:188908", "taxon_label": "Oleispira antarctica"}, "logical_row": 5388}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "24", "taxon_id": "NCBITaxon:190308", "taxon_label": "Shewanella schlegeliana"}, "logical_row": 5389}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "25", "taxon_id": "NCBITaxon:191302", "taxon_label": "Devosia neptuniae"}, "logical_row": 5390}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category": "biolink:OntologyClass", "channels": "environmental_samples", "direct_assertion_count": "171", "max_prego_score": "4", "ontology": "ENVO", "prego_id": "ENVO:00001999", "prego_synonyms": "marine water bodies&#124;marine water body", "taxon_count": "171"}, "logical_row": 158}]} |
| CODE | src/habitatmech/seed.py; Executed complete-document reconstruction; all 40 matched; routes distinguish source mints and generated identity | supports | {"reviewed_sources": 3, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:BACDIVE.407144fe70", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status": "CLOSE", "identifier": "ENVO:00001999", "mapping_predicate": "skos:closeMatch", "reviewed": true, "route": "curated_review_of_bacdive_mapping_table"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "CLOSE", "identifier": "ENVO:00001999", "mapping_predicate": "skos:closeMatch", "reviewed": false, "route": "bacdive_mapping_table"}, "minted": "habitatmech:BACDIVE.407144fe70", "source": "BACDIVE", "source_id": "bacdive.isolation_source:marine"}, {"actual": {"category": null, "contributes_grounding": true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:GOLD.5856c699e4", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status": "CLOSE", "identifier": "ENVO:00001999", "mapping_predicate": "skos:closeMatch", "reviewed": true, "route": "curated_review_of_gold_mapping_table"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "CLOSE", "identifier": "ENVO:00001999", "mapping_predicate": "skos:closeMatch", "reviewed": false, "route": "gold_mapping_table"}, "minted": "habitatmech:GOLD.5856c699e4", "source": "GOLD", "source_id": "gold.ecosystem:3487"}, {"actual": {"category": null, "contributes_grounding": true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:PREGO.a653eb2a85", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00001999", "mapping_predicate": null, "reviewed": true, "route": "curated_review_of_prego_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00001999", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.a653eb2a85", "source": "PREGO", "source_id": "ENVO:00001999"}], "source_concepts": 3} |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Official OWL retrieved 12-Oct; labels, definitions, typed synonyms, named parents and restrictions; no snapshot refresh | supports | {"ENVO:00000063": {"definitions": ["An accumulation of water of varying size."], "deprecated": [], "equivalents": [], "labels": ["water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000685", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000819"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002354"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01001220"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_15377"]}], "replacements": [], "synonyms": {"hasBroadSynonym": ["hydrographic feature"], "hasExactSynonym": ["aquatic feature", "bodies of water", "body of water", "waterbody"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00000428": {"definitions": ["A biome is an ecosystem which is undergoing climactic ecological succession."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_01001110"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000056"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01001827"]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["biome"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000813", "http://purl.obolibrary.org/obo/ENVO_01001110", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000817"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PCO_0000002"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000056"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01001827"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002507"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PCO_0000002"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["major habitat type"], "hasNarrowSynonym": [], "hasRelatedSynonym": ["EcosytemType"]}}, "ENVO:00001999": {"definitions": ["A lentic water body which is composed primarily of marine water."], "deprecated": [], "equivalents": [], "labels": ["marine water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000617"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["body of marine water", "marine waterbody"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002030": {"definitions": ["A biome which is determined by a water body and which has ecological climax communities adapted to life in or on water."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00000428"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002507"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00000063"]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["aquatic biome"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000428", "http://purl.obolibrary.org/obo/ENVO_01001787"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:01000254": {"definitions": ["A system which has the disposition to environ one or more material entities."], "deprecated": [], "equivalents": [], "labels": ["environmental system"], "parents": ["http://purl.obolibrary.org/obo/RO_0002577"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["environment"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:01000617": {"definitions": ["A lentic water body is a water body in which the accumulated water, in its totality, has very little to no directed flow."], "deprecated": [], "equivalents": [], "labels": ["lentic water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000063"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}} |
| PARENT | data/habitats/aquatic/lentic_water_body.yaml; data/habitats/aquatic/water_body.yaml; data/habitats/aquatic/aquatic_biome.yaml; data/habitats/other/environmental.yaml; data/habitats/other/environmental_system.yaml; data/habitats/other/biome.yaml; Ancestor context adds no full-record coverage | supports | {"ENVO:00000063": {"definition": "An accumulation of water of varying size.", "grounding_status": "EXACT", "label": "water body", "parent_habitats": ["ENVO:01000685"]}, "ENVO:00000428": {"definition": "A biome is an ecosystem which is undergoing climactic ecological succession.", "grounding_status": "EXACT", "label": "biome", "parent_habitats": ["ENVO:01000813", "ENVO:01001110"]}, "ENVO:00002030": {"definition": "A biome which is determined by a water body and which has ecological climax communities adapted to life in or on water.", "grounding_status": "EXACT", "label": "aquatic biome", "parent_habitats": ["ENVO:00000428", "ENVO:01001787", "habitatmech:BACDIVE.0f1e92a02c"]}, "ENVO:01000254": {"definition": "A system which has the disposition to environ one or more material entities.", "grounding_status": "EXACT", "label": "environmental system", "parent_habitats": null}, "ENVO:01000617": {"definition": "A lentic water body is a water body in which the accumulated water, in its totality, has very little to no directed flow.", "grounding_status": "EXACT", "label": "lentic water body", "parent_habitats": ["ENVO:00000063"]}, "habitatmech:BACDIVE.0f1e92a02c": {"definition": "An environmental system which is a portion of the air, water, or land surface or subsurface of an astronomical body sampled in place, and which is neither bounded by a host organism nor constituted by a constructed or operated artefact.", "grounding_status": "UNGROUNDED", "label": "free-living environment", "parent_habitats": ["ENVO:01000254"]}} |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; Five-position ecosystem paths preserved; contacts excluded; first 3 BioSample and Organism descriptions per target | supports | Exact positional census counts={"Biosample": 5389, "Organism": 5364, "SequencingProject": 10866}; individually inspected descriptions={"Biosample": [{"data": {"BIOSAMPLE GOLD ID": "Gb0051204", "BIOSAMPLE NAME": "Marine ecosystem from Palmer Station, Antarctica ", "BIOSAMPLE NCBI TAX NAME": "marine metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Palmer Station, Antarctica"}, "row": 200}, {"data": {"BIOSAMPLE GOLD ID": "Gb0051208", "BIOSAMPLE NAME": "Marine ecosystem from Technion - Israel Institute of Technology, Israel", "BIOSAMPLE NCBI TAX NAME": "marine metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Marine Roseobacter"}, "row": 201}, {"data": {"BIOSAMPLE GOLD ID": "Gb0051293", "BIOSAMPLE NAME": "Marine ecosystem from Monterey Bay, USA", "BIOSAMPLE NCBI TAX NAME": "marine metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Monterey Bay, Pacific Ocean"}, "row": 248}], "Organism": [{"data": {"ORGANISM GOLD ID": "Go0000012", "ORGANISM NAME": "Altermonas sp. SCGC AC-669 C16", "ORGANISM SAMPLE COLLECTION SITE": "Eastern Tropical South Pacific Ocean, Chile"}, "row": 11}, {"data": {"ORGANISM GOLD ID": "Go0000017", "ORGANISM HABITAT": "Marine&#124;Aquatic", "ORGANISM NAME": "Shewanella baltica OS195", "ORGANISM SAMPLE COLLECTION SITE": "Sea-water; anoxic zone; 240 m depth from the Baltic Sea"}, "row": 16}, {"data": {"ORGANISM GOLD ID": "Go0000018", "ORGANISM HABITAT": "Marine&#124;Aquatic", "ORGANISM NAME": "Hemiselmis andersenii CCMP 644 (nucleomorph)", "ORGANISM SAMPLE COLLECTION SITE": "Gulf of Mexico, North Atlantic Sea"}, "row": 17}]}. These later examples may include mixed sample/host/enrichment contexts; they do not reconstruct original assertion membership. Remaining members and study joins were indexed, not individually assessed. |
| CLASS | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Later official classification; 29 of 31 cohort paths matched; missing tuples do not establish nonexistence | supports | [{"row": 802, "slug": "marine_water_body", "path": "Environmental &gt; Aquatic &gt; Marine", "values": ["4003", "Environmental", "Aquatic", "Marine", "Unclassified", "Unclassified"]}] |
| TAX0 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1000566%2C1003110%2C1005925%2C1005926%2C1005928%2C1006%2C1007105%2C1007109%2C1007110%2C1007111%2C1007112%2C1007113%2C1007114%2C1007115%2C1007116%2C1007117%2C1007118%2C1007119%2C1007120%2C1007122%2C1007124%2C1009412%2C1009413%2C1009414%2C1009415%2C1009416%2C1009418%2C1009419%2C1009420%2C1009421%2C1017277%2C102%2C1026%2C1027373%2C1027374%2C1028566%2C1028742%2C1028743%2C1028745%2C1028746%2C1028749%2C1028752%2C1031273%2C1031541%2C103810%2C1038845%2C1038928%2C1038929%2C1042%2C104268%2C104270%2C1042877%2C1044%2C104421%2C1045558%2C1048%2C1048221%2C1057%2C106299%2C1074%2C107401%2C1080%2C1089550%2C109263%2C1094980%2C110163%2C1104565%2C1104566%2C110662%2C110663%2C111770%2C1121404%2C1121937%2C1121948%2C1122607%2C1123059%2C1123242%2C1123275%2C114404%2C1150474%2C119394%2C119542%2C1208324%2C1211807%2C121224%2C1217908%2C1219067%2C1242148%2C1246444%2C1246460%2C1265%2C126741%2C1267768%2C1267769%2C1276246%2C1282%2C129958%2C132144%2C133924%2C134561%2C1358%2C13616%2C13686%2C1371%2C1387275%2C139239%2C1394%2C1411902%2C143223%2C143224%2C147%2C1486246%2C150120%2C1543721%2C156%2C156128%2C156133%2C1570%2C158080%2C158192%2C158500%2C1609977%2C161528%2C163248%2C163503%2C168275%2C168759%2C1703256%2C1716143%2C172371%2C173%2C173365%2C173737%2C173764%2C174%2C174302%2C174315%2C1774373%2C179326%2C180542%2C1808508%2C1808945%2C1817405%2C1836499%2C184592%2C184914%2C1855%2C186022%2C1869227%2C1871328&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The three chunks jointly resolve all 346 requested cohort IDs. Target results=[{"current_id": "28108", "current_name": "Alteromonas macleodii", "frozen_label": "Alteromonas macleodii", "id": "28108", "rank": "species"}, {"current_id": "172371", "current_name": "Alloalcanivorax venustensis", "frozen_label": "Alloalcanivorax venustensis", "id": "172371", "rank": "species"}, {"current_id": "28258", "current_name": "Cobetia marina", "frozen_label": "Cobetia marina", "id": "28258", "rank": "species"}, {"current_id": "180542", "current_name": "Salinisphaera shabanensis", "frozen_label": "Salinisphaera shabanensis", "id": "180542", "rank": "species"}, {"current_id": "184914", "current_name": "Corallococcus coralloides", "frozen_label": "Corallococcus coralloides", "id": "184914", "rank": "species"}, {"current_id": "102", "current_name": "Polaribacter glomeratus", "frozen_label": "Polaribacter glomeratus", "id": "102", "rank": "species"}, {"current_id": "1876", "current_name": "Micromonospora sp.", "frozen_label": "Micromonospora sp.", "id": "1876", "rank": "species"}, {"current_id": "1026", "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum furvescens", "id": "1026", "rank": "species"}, {"current_id": "83428", "current_name": "uncultured Bacillus sp.", "frozen_label": "uncultured Bacillus sp.", "id": "83428", "rank": "species"}, {"current_id": "104268", "current_name": "Tenacibaculum mesophilum", "frozen_label": "Tenacibaculum mesophilum", "id": "104268", "rank": "species"}, {"current_id": "1869227", "current_name": "bacterium", "frozen_label": "bacterium", "id": "1869227", "rank": "species"}, {"current_id": "107401", "current_name": "Tenacibaculum maritimum", "frozen_label": "Tenacibaculum maritimum", "id": "107401", "rank": "species"}, {"current_id": "562", "current_name": "Escherichia coli", "frozen_label": "Escherichia coli", "id": "562", "rank": "species"}, {"current_id": "111770", "current_name": "Thiothrix fructosivorans", "frozen_label": "Thiothrix fructosivorans", "id": "111770", "rank": "species"}, {"current_id": "314275", "current_name": "Alteromonas mediterranea", "frozen_label": "Alteromonas mediterranea", "id": "314275", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank": "species"}, {"current_id": "2", "current_name": "Bacteria", "frozen_label": "Bacteria", "id": "2", "rank": "domain"}, {"current_id": "1282", "current_name": "Staphylococcus epidermidis", "frozen_label": "Staphylococcus epidermidis", "id": "1282", "rank": "species"}, {"current_id": "132144", "current_name": "Candidatus Glomeribacter gigasporarum", "frozen_label": "Candidatus Glomeribacter gigasporarum", "id": "132144", "rank": "species"}, {"current_id": "53249", "current_name": "Pseudoalteromonas sp.", "frozen_label": "Pseudoalteromonas sp.", "id": "53249", "rank": "species"}, {"current_id": "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label": "Leisingera methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id": "50741", "current_name": "Marinobacter sp.", "frozen_label": "Marinobacter sp.", "id": "50741", "rank": "species"}, {"current_id": "13616", "current_name": "Monodelphis domestica", "frozen_label": null, "id": "13616", "rank": "species"}, {"current_id": "56811", "current_name": "Psychrobacter sp.", "frozen_label": "Psychrobacter sp.", "id": "56811", "rank": "species"}, {"current_id": "1371", "current_name": "Marinococcus halophilus", "frozen_label": "Marinococcus halophilus", "id": "1371", "rank": "species"}, {"current_id": "1211807", "current_name": "Stutzerimonas kunmingensis", "frozen_label": "Stutzerimonas kunmingensis", "id": "1211807", "rank": "species"}, {"current_id": "143223", "current_name": "Salegentibacter salegens", "frozen_label": "Salegentibacter salegens", "id": "143223", "rank": "species"}, {"current_id": "1871328", "current_name": "Kocuria sp.", "frozen_label": "Kocuria sp.", "id": "1871328", "rank": "species"}, {"current_id": "156128", "current_name": "Nephroselmis pyriformis", "frozen_label": null, "id": "156128", "rank": "species"}, {"current_id": "1931", "current_name": "Streptomyces sp.", "frozen_label": "Streptomyces sp.", "id": "1931", "rank": "species"}, {"current_id": "156133", "current_name": "Prasinoderma coloniale", "frozen_label": null, "id": "156133", "rank": "species"}, {"current_id": "2024855", "current_name": "Rhodopirellula sp.", "frozen_label": "Rhodopirellula sp.", "id": "2024855", "rank": "species"}, {"current_id": "141390", "current_name": "Chromohalobacter israelensis", "frozen_label": null, "id": "158080", "rank": "species"}, {"current_id": "2099376", "current_name": "Desulforhopalus sp.", "frozen_label": "Desulforhopalus sp.", "id": "2099376", "rank": "species"}, {"current_id": "158500", "current_name": "Novosphingobium resinovorum", "frozen_label": "Novosphingobium resinovorum", "id": "158500", "rank": "species"}, {"current_id": "2213", "current_name": "Methanosarcina sp.", "frozen_label": "Methanosarcina sp.", "id": "2213", "rank": "species"}, {"current_id": "168275", "current_name": "Psychromonas arctica", "frozen_label": "Psychromonas arctica", "id": "168275", "rank": "species"}, {"current_id": "265606", "current_name": "Rhodopirellula baltica", "frozen_label": "Rhodopirellula baltica", "id": "265606", "rank": "species"}, {"current_id": "173365", "current_name": "Methylobacter tundripaludum", "frozen_label": "Methylobacter tundripaludum", "id": "173365", "rank": "species"}, {"current_id": "2926447", "current_name": "Marinispora", "frozen_label": "Marinispora", "id": "2926447", "rank": "genus"}, {"current_id": "44751", "current_name": "Exiguobacterium sp.", "frozen_label": "Exiguobacterium sp.", "id": "44751", "rank": "species"}, {"current_id": "51671", "current_name": "Microbacterium sp.", "frozen_label": "Microbacterium sp.", "id": "51671", "rank": "species"}, {"current_id": "186022", "current_name": "Thalassionema frauenfeldii", "frozen_label": "Thalassionema frauenfeldii", "id": "186022", "rank": "species"}, {"current_id": "885", "current_name": "Desulfovibrio sp.", "frozen_label": "Desulfovibrio sp.", "id": "885", "rank": "species"}, {"current_id": "188908", "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica", "id": "188908", "rank": "species"}, {"current_id": "1042", "current_name": "Erythrobacter sp.", "frozen_label": "Erythrobacter sp.", "id": "1042", "rank": "species"}, {"current_id": "190308", "current_name": "Shewanella schlegeliana", "frozen_label": "Shewanella schlegeliana", "id": "190308", "rank": "species"}, {"current_id": "1486246", "current_name": "Halomonas sp.", "frozen_label": "Halomonas sp.", "id": "1486246", "rank": "species"}, {"current_id": "191302", "current_name": "Devosia neptuniae", "frozen_label": "Devosia neptuniae", "id": "191302", "rank": "species"}, {"current_id": "1703256", "current_name": "Pseudoalteromonas gelatinilytica", "frozen_label": "Pseudoalteromonas gelatinilytica", "id": "1703256", "rank": "species"}]. Alias/name resolution does not establish habitat occurrence. |
| TAX1 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1872627%2C1876%2C188906%2C188908%2C1903071%2C190308%2C191302%2C1926630%2C1931%2C195064%2C1961642%2C197222%2C198804%2C2%2C200617%2C2022602%2C2024855%2C203122%2C203907%2C205920%2C2099376%2C212050%2C214688%2C214988%2C216432%2C216773%2C2183988%2C2213%2C223788%2C224915%2C225345%2C225937%2C226126%2C2264%2C234267%2C240016%2C2423%2C243090%2C247026%2C257363%2C264%2C264462%2C264951%2C265606%2C266940%2C2738566%2C28108%2C28122%2C28181%2C28223%2C28251%2C28258%2C28262%2C29158%2C29159%2C2926447%2C29292%2C293614%2C29805%2C302409%2C3055%2C3068%2C31330%2C313595%2C313603%2C313606%2C314230%2C314275%2C316279%2C319225%2C320388%2C332415%2C337701%2C339861%2C340047%2C34085%2C344747%2C357244%2C35743%2C35845%2C358766%2C361576%2C36870%2C36987%2C372461%2C378806%2C379066%2C39152%2C391625%2C39947%2C402880%2C40464%2C406538%2C406540%2C411477%2C411485%2C419481%2C425006%2C428125%2C435805%2C43928%2C442956%2C443152%2C445336%2C44751%2C45351%2C457427%2C463619%2C46539%2C466153%2C46687%2C46704%2C46745%2C472759%2C483407%2C483417%2C48499%2C48729%2C491952%2C49447%2C498761%2C502025%2C504472%2C50741%2C515618%2C51671%2C518766%2C523849%2C530564%2C53249%2C537937%2C53953%2C55518%2C555512%2C55567%2C562%2C563043%2C56780%2C56811%2C57043%2C575540%2C583355%2C585501%2C595452%2C595453%2C59919%2C59920%2C6047%2C60480%2C6087&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The three chunks jointly resolve all 346 requested cohort IDs. Target results=[{"current_id": "28108", "current_name": "Alteromonas macleodii", "frozen_label": "Alteromonas macleodii", "id": "28108", "rank": "species"}, {"current_id": "172371", "current_name": "Alloalcanivorax venustensis", "frozen_label": "Alloalcanivorax venustensis", "id": "172371", "rank": "species"}, {"current_id": "28258", "current_name": "Cobetia marina", "frozen_label": "Cobetia marina", "id": "28258", "rank": "species"}, {"current_id": "180542", "current_name": "Salinisphaera shabanensis", "frozen_label": "Salinisphaera shabanensis", "id": "180542", "rank": "species"}, {"current_id": "184914", "current_name": "Corallococcus coralloides", "frozen_label": "Corallococcus coralloides", "id": "184914", "rank": "species"}, {"current_id": "102", "current_name": "Polaribacter glomeratus", "frozen_label": "Polaribacter glomeratus", "id": "102", "rank": "species"}, {"current_id": "1876", "current_name": "Micromonospora sp.", "frozen_label": "Micromonospora sp.", "id": "1876", "rank": "species"}, {"current_id": "1026", "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum furvescens", "id": "1026", "rank": "species"}, {"current_id": "83428", "current_name": "uncultured Bacillus sp.", "frozen_label": "uncultured Bacillus sp.", "id": "83428", "rank": "species"}, {"current_id": "104268", "current_name": "Tenacibaculum mesophilum", "frozen_label": "Tenacibaculum mesophilum", "id": "104268", "rank": "species"}, {"current_id": "1869227", "current_name": "bacterium", "frozen_label": "bacterium", "id": "1869227", "rank": "species"}, {"current_id": "107401", "current_name": "Tenacibaculum maritimum", "frozen_label": "Tenacibaculum maritimum", "id": "107401", "rank": "species"}, {"current_id": "562", "current_name": "Escherichia coli", "frozen_label": "Escherichia coli", "id": "562", "rank": "species"}, {"current_id": "111770", "current_name": "Thiothrix fructosivorans", "frozen_label": "Thiothrix fructosivorans", "id": "111770", "rank": "species"}, {"current_id": "314275", "current_name": "Alteromonas mediterranea", "frozen_label": "Alteromonas mediterranea", "id": "314275", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank": "species"}, {"current_id": "2", "current_name": "Bacteria", "frozen_label": "Bacteria", "id": "2", "rank": "domain"}, {"current_id": "1282", "current_name": "Staphylococcus epidermidis", "frozen_label": "Staphylococcus epidermidis", "id": "1282", "rank": "species"}, {"current_id": "132144", "current_name": "Candidatus Glomeribacter gigasporarum", "frozen_label": "Candidatus Glomeribacter gigasporarum", "id": "132144", "rank": "species"}, {"current_id": "53249", "current_name": "Pseudoalteromonas sp.", "frozen_label": "Pseudoalteromonas sp.", "id": "53249", "rank": "species"}, {"current_id": "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label": "Leisingera methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id": "50741", "current_name": "Marinobacter sp.", "frozen_label": "Marinobacter sp.", "id": "50741", "rank": "species"}, {"current_id": "13616", "current_name": "Monodelphis domestica", "frozen_label": null, "id": "13616", "rank": "species"}, {"current_id": "56811", "current_name": "Psychrobacter sp.", "frozen_label": "Psychrobacter sp.", "id": "56811", "rank": "species"}, {"current_id": "1371", "current_name": "Marinococcus halophilus", "frozen_label": "Marinococcus halophilus", "id": "1371", "rank": "species"}, {"current_id": "1211807", "current_name": "Stutzerimonas kunmingensis", "frozen_label": "Stutzerimonas kunmingensis", "id": "1211807", "rank": "species"}, {"current_id": "143223", "current_name": "Salegentibacter salegens", "frozen_label": "Salegentibacter salegens", "id": "143223", "rank": "species"}, {"current_id": "1871328", "current_name": "Kocuria sp.", "frozen_label": "Kocuria sp.", "id": "1871328", "rank": "species"}, {"current_id": "156128", "current_name": "Nephroselmis pyriformis", "frozen_label": null, "id": "156128", "rank": "species"}, {"current_id": "1931", "current_name": "Streptomyces sp.", "frozen_label": "Streptomyces sp.", "id": "1931", "rank": "species"}, {"current_id": "156133", "current_name": "Prasinoderma coloniale", "frozen_label": null, "id": "156133", "rank": "species"}, {"current_id": "2024855", "current_name": "Rhodopirellula sp.", "frozen_label": "Rhodopirellula sp.", "id": "2024855", "rank": "species"}, {"current_id": "141390", "current_name": "Chromohalobacter israelensis", "frozen_label": null, "id": "158080", "rank": "species"}, {"current_id": "2099376", "current_name": "Desulforhopalus sp.", "frozen_label": "Desulforhopalus sp.", "id": "2099376", "rank": "species"}, {"current_id": "158500", "current_name": "Novosphingobium resinovorum", "frozen_label": "Novosphingobium resinovorum", "id": "158500", "rank": "species"}, {"current_id": "2213", "current_name": "Methanosarcina sp.", "frozen_label": "Methanosarcina sp.", "id": "2213", "rank": "species"}, {"current_id": "168275", "current_name": "Psychromonas arctica", "frozen_label": "Psychromonas arctica", "id": "168275", "rank": "species"}, {"current_id": "265606", "current_name": "Rhodopirellula baltica", "frozen_label": "Rhodopirellula baltica", "id": "265606", "rank": "species"}, {"current_id": "173365", "current_name": "Methylobacter tundripaludum", "frozen_label": "Methylobacter tundripaludum", "id": "173365", "rank": "species"}, {"current_id": "2926447", "current_name": "Marinispora", "frozen_label": "Marinispora", "id": "2926447", "rank": "genus"}, {"current_id": "44751", "current_name": "Exiguobacterium sp.", "frozen_label": "Exiguobacterium sp.", "id": "44751", "rank": "species"}, {"current_id": "51671", "current_name": "Microbacterium sp.", "frozen_label": "Microbacterium sp.", "id": "51671", "rank": "species"}, {"current_id": "186022", "current_name": "Thalassionema frauenfeldii", "frozen_label": "Thalassionema frauenfeldii", "id": "186022", "rank": "species"}, {"current_id": "885", "current_name": "Desulfovibrio sp.", "frozen_label": "Desulfovibrio sp.", "id": "885", "rank": "species"}, {"current_id": "188908", "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica", "id": "188908", "rank": "species"}, {"current_id": "1042", "current_name": "Erythrobacter sp.", "frozen_label": "Erythrobacter sp.", "id": "1042", "rank": "species"}, {"current_id": "190308", "current_name": "Shewanella schlegeliana", "frozen_label": "Shewanella schlegeliana", "id": "190308", "rank": "species"}, {"current_id": "1486246", "current_name": "Halomonas sp.", "frozen_label": "Halomonas sp.", "id": "1486246", "rank": "species"}, {"current_id": "191302", "current_name": "Devosia neptuniae", "frozen_label": "Devosia neptuniae", "id": "191302", "rank": "species"}, {"current_id": "1703256", "current_name": "Pseudoalteromonas gelatinilytica", "frozen_label": "Pseudoalteromonas gelatinilytica", "id": "1703256", "rank": "species"}]. Alias/name resolution does not establish habitat occurrence. |
| TAX2 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=610380%2C6182%2C6238%2C6334%2C639602%2C641112%2C6613%2C6669%2C688066%2C69293%2C6945%2C69773%2C7029%2C703612%2C7070%2C7159%2C7209%2C7425%2C74546%2C74547%2C748449%2C756272%2C758583%2C75883%2C760154%2C765912%2C7668%2C76775%2C7719%2C777%2C7955%2C80836%2C8090%2C83428%2C86104%2C880%2C880447%2C885%2C89184%2C9031%2C91360%2C9258%2C939306%2C939316%2C939324%2C939346&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The three chunks jointly resolve all 346 requested cohort IDs. Target results=[{"current_id": "28108", "current_name": "Alteromonas macleodii", "frozen_label": "Alteromonas macleodii", "id": "28108", "rank": "species"}, {"current_id": "172371", "current_name": "Alloalcanivorax venustensis", "frozen_label": "Alloalcanivorax venustensis", "id": "172371", "rank": "species"}, {"current_id": "28258", "current_name": "Cobetia marina", "frozen_label": "Cobetia marina", "id": "28258", "rank": "species"}, {"current_id": "180542", "current_name": "Salinisphaera shabanensis", "frozen_label": "Salinisphaera shabanensis", "id": "180542", "rank": "species"}, {"current_id": "184914", "current_name": "Corallococcus coralloides", "frozen_label": "Corallococcus coralloides", "id": "184914", "rank": "species"}, {"current_id": "102", "current_name": "Polaribacter glomeratus", "frozen_label": "Polaribacter glomeratus", "id": "102", "rank": "species"}, {"current_id": "1876", "current_name": "Micromonospora sp.", "frozen_label": "Micromonospora sp.", "id": "1876", "rank": "species"}, {"current_id": "1026", "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum furvescens", "id": "1026", "rank": "species"}, {"current_id": "83428", "current_name": "uncultured Bacillus sp.", "frozen_label": "uncultured Bacillus sp.", "id": "83428", "rank": "species"}, {"current_id": "104268", "current_name": "Tenacibaculum mesophilum", "frozen_label": "Tenacibaculum mesophilum", "id": "104268", "rank": "species"}, {"current_id": "1869227", "current_name": "bacterium", "frozen_label": "bacterium", "id": "1869227", "rank": "species"}, {"current_id": "107401", "current_name": "Tenacibaculum maritimum", "frozen_label": "Tenacibaculum maritimum", "id": "107401", "rank": "species"}, {"current_id": "562", "current_name": "Escherichia coli", "frozen_label": "Escherichia coli", "id": "562", "rank": "species"}, {"current_id": "111770", "current_name": "Thiothrix fructosivorans", "frozen_label": "Thiothrix fructosivorans", "id": "111770", "rank": "species"}, {"current_id": "314275", "current_name": "Alteromonas mediterranea", "frozen_label": "Alteromonas mediterranea", "id": "314275", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank": "species"}, {"current_id": "2", "current_name": "Bacteria", "frozen_label": "Bacteria", "id": "2", "rank": "domain"}, {"current_id": "1282", "current_name": "Staphylococcus epidermidis", "frozen_label": "Staphylococcus epidermidis", "id": "1282", "rank": "species"}, {"current_id": "132144", "current_name": "Candidatus Glomeribacter gigasporarum", "frozen_label": "Candidatus Glomeribacter gigasporarum", "id": "132144", "rank": "species"}, {"current_id": "53249", "current_name": "Pseudoalteromonas sp.", "frozen_label": "Pseudoalteromonas sp.", "id": "53249", "rank": "species"}, {"current_id": "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label": "Leisingera methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id": "50741", "current_name": "Marinobacter sp.", "frozen_label": "Marinobacter sp.", "id": "50741", "rank": "species"}, {"current_id": "13616", "current_name": "Monodelphis domestica", "frozen_label": null, "id": "13616", "rank": "species"}, {"current_id": "56811", "current_name": "Psychrobacter sp.", "frozen_label": "Psychrobacter sp.", "id": "56811", "rank": "species"}, {"current_id": "1371", "current_name": "Marinococcus halophilus", "frozen_label": "Marinococcus halophilus", "id": "1371", "rank": "species"}, {"current_id": "1211807", "current_name": "Stutzerimonas kunmingensis", "frozen_label": "Stutzerimonas kunmingensis", "id": "1211807", "rank": "species"}, {"current_id": "143223", "current_name": "Salegentibacter salegens", "frozen_label": "Salegentibacter salegens", "id": "143223", "rank": "species"}, {"current_id": "1871328", "current_name": "Kocuria sp.", "frozen_label": "Kocuria sp.", "id": "1871328", "rank": "species"}, {"current_id": "156128", "current_name": "Nephroselmis pyriformis", "frozen_label": null, "id": "156128", "rank": "species"}, {"current_id": "1931", "current_name": "Streptomyces sp.", "frozen_label": "Streptomyces sp.", "id": "1931", "rank": "species"}, {"current_id": "156133", "current_name": "Prasinoderma coloniale", "frozen_label": null, "id": "156133", "rank": "species"}, {"current_id": "2024855", "current_name": "Rhodopirellula sp.", "frozen_label": "Rhodopirellula sp.", "id": "2024855", "rank": "species"}, {"current_id": "141390", "current_name": "Chromohalobacter israelensis", "frozen_label": null, "id": "158080", "rank": "species"}, {"current_id": "2099376", "current_name": "Desulforhopalus sp.", "frozen_label": "Desulforhopalus sp.", "id": "2099376", "rank": "species"}, {"current_id": "158500", "current_name": "Novosphingobium resinovorum", "frozen_label": "Novosphingobium resinovorum", "id": "158500", "rank": "species"}, {"current_id": "2213", "current_name": "Methanosarcina sp.", "frozen_label": "Methanosarcina sp.", "id": "2213", "rank": "species"}, {"current_id": "168275", "current_name": "Psychromonas arctica", "frozen_label": "Psychromonas arctica", "id": "168275", "rank": "species"}, {"current_id": "265606", "current_name": "Rhodopirellula baltica", "frozen_label": "Rhodopirellula baltica", "id": "265606", "rank": "species"}, {"current_id": "173365", "current_name": "Methylobacter tundripaludum", "frozen_label": "Methylobacter tundripaludum", "id": "173365", "rank": "species"}, {"current_id": "2926447", "current_name": "Marinispora", "frozen_label": "Marinispora", "id": "2926447", "rank": "genus"}, {"current_id": "44751", "current_name": "Exiguobacterium sp.", "frozen_label": "Exiguobacterium sp.", "id": "44751", "rank": "species"}, {"current_id": "51671", "current_name": "Microbacterium sp.", "frozen_label": "Microbacterium sp.", "id": "51671", "rank": "species"}, {"current_id": "186022", "current_name": "Thalassionema frauenfeldii", "frozen_label": "Thalassionema frauenfeldii", "id": "186022", "rank": "species"}, {"current_id": "885", "current_name": "Desulfovibrio sp.", "frozen_label": "Desulfovibrio sp.", "id": "885", "rank": "species"}, {"current_id": "188908", "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica", "id": "188908", "rank": "species"}, {"current_id": "1042", "current_name": "Erythrobacter sp.", "frozen_label": "Erythrobacter sp.", "id": "1042", "rank": "species"}, {"current_id": "190308", "current_name": "Shewanella schlegeliana", "frozen_label": "Shewanella schlegeliana", "id": "190308", "rank": "species"}, {"current_id": "1486246", "current_name": "Halomonas sp.", "frozen_label": "Halomonas sp.", "id": "1486246", "rank": "species"}, {"current_id": "191302", "current_name": "Devosia neptuniae", "frozen_label": "Devosia neptuniae", "id": "191302", "rank": "species"}, {"current_id": "1703256", "current_name": "Pseudoalteromonas gelatinilytica", "frozen_label": "Pseudoalteromonas gelatinilytica", "id": "1703256", "rank": "species"}]. Alias/name resolution does not establish habitat occurrence. |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf; Search boundaries are explicit; no global absence claim | supports | Identifier, label, slug and exact-path searches included hidden/ignored files in these roots. No earlier structured target observation was found. Legacy reports exist and are not silently retired. Bounded original-source search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv", "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv", "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv", "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv", "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv", "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv", "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv", "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv", "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv", "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv", "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}], "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "exit_code": 0, "matches": [], "stderr": ""}]} |
| ISSUES | https://github.com/CultureBotAI/HabitatMech/issues; GitHub CLI inventory retrieved 12-Oct | supports | Read-only all-state 967-issue title/body inventory and relevant bodies inspected. Issues are historical leads, not primary support; current owner rows and scientific evidence were checked independently. Comments were not exhaustively crawled. Closed issue #1301 is reflected in the current graph and is not reopened by preserving old history. |
| GRAPH | curation/causal_graphs/marine_water_body.yaml; Current full overlay | supports | Entire overlay and generated graph read, including all node types, edge descriptions, evidence and preserved historical events. |
| PUMP | https://pmc.ncbi.nlm.nih.gov/articles/PMC3972885/; DOI:10.1038/ngeo1921; Introduction/Fig1, Sinking versus buoyant particles, Microbial activity in the dark | supports | Conditional export and remineralization, with nonsinking and dark-fixation alternatives. |
| ARRIGO | https://pangea.stanford.edu/research/Oceans/GES205/Arrigo_Nature_Global%20Ocean%20Nutrients.pdf; PMID:16163345; printed pp349-351, Fig2. Author PDF header says nature04158; publication metadata identifies this title/author as nature04159. No citation was swapped. | supports | Light/resource co-limitation, aerobic breakdown and nonuniform nutrient regeneration. |
| NOAA | https://www.fisheries.noaa.gov/west-coast/science-data/phytoplankton-northwest-us-shelf-ecosystem; What Are Phytoplankton; What Is Primary Production | supports | Photosynthesis and biomass account with diverse phytoplankton groups. |
| ARNOSTI | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21329211+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID:21329211; core bibliographic metadata and complete abstract, not full text | supports | Complete abstract supports hydrolysis to uptake-sized substrates and heterotrophic carbon processing. |
| IMODULONDB | iModulonDB via kg-microbe-sources; Actual 28-dataset inventory inspected; no covered claim-specific strain/gene or expression module in this generic guild graph warrants a search/component query | supports | {"command": ["../../culturebotai-claw/.venv/bin/kg-microbe-sources", "imodulondb", "datasets"], "started_at": "2026-10-12T05:22:18.796436+00:00", "finished_at": "2026-10-12T05:22:19.723730+00:00", "exit_code": 0, "path": "/private/tmp/habitatmech-review-bc-imodulondb-datasets.source", "sha256": "1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549", "stderr": ""} |

## Limits And Additional Notes

- Completed assessment is not a clean-record verdict or proof of every original source occurrence.
- Only the first three exact-path BioSample and Organism descriptions per target/sheet were individually interpreted; remaining members and study joins were indexed, not scientifically reviewed.
- Later GOLD export/classification does not reconstruct original August membership. No ontology, taxonomy or source snapshot was refreshed.
- Same-agent review, not independent approval. Native status and curation/history inputs are unchanged.
- SSSOM/KGX conformance to current kg-microbe modeling was not audited; shared endpoint issue #1398 remains open.
- Whole-corpus scientific review remains incomplete. Ancestor/context reads add no record coverage. Product-label checking retains 2057 no-adapter skips and five accepted exceptions.
- Full text was read for the explicitly identified full-text items; Arnosti support is bounded to the complete abstract. Europe PMC pump XML failed, but PMC HTML full text was inspected. PDF text required an isolated reader dependency; repository dependencies were not changed.
- Review-only observation: no curation, status promotion, GitHub mutation or paid research.
- No earlier structured target observation found; legacy reports are historical and are not automatically superseded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T054256Z-marine_water_body
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: marine_water_body'
started_at: '2026-10-12T05:19:15.702311Z'
finished_at: '2026-10-12T05:42:56.014225Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Agent has participated in repository curation; this is not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The physical lentic marine water body is not an aquatic biome. Preserve BacDive
  2040 STRAIN, GOLD 6420 ORGANISM and PREGO 171 TAXON assertions, the two CLOSE source
  mappings and 50 selected associations. The revised 15-edge carbon-pump graph is
  explicitly conditional and its earlier unrelated citation is no longer active. Current
  node types still confuse ecological assemblages, habitats and enzyme products with
  taxa, exposures and a trait.
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
  - path: curation/causal_graphs/aquatic_biome.yaml
    sha256: 03ba09d10f9a9d8d32060fc0208b511ef0d59e731fd7c63ca6c02296e70da5f5
    role: context
  - path: curation/causal_graphs/marine_water_body.yaml
    sha256: b2f81102970e9541bf61978fabdd68b7db8f9459f1ef11b467fecfc2956f238b
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
  - path: data/habitats/aquatic/aquatic_biome.yaml
    sha256: 27466c1abb6814aa790ecec6987d803850d0237c697c565e6fc21d1baaebfa27
    role: context
  - path: data/habitats/aquatic/lentic_water_body.yaml
    sha256: 571e0538d45626dcb9d8f5b3338e6ce31cff66f5ff693e36c04ae81d9e9920c0
    role: context
  - path: data/habitats/aquatic/marine_water_body.yaml
    sha256: 2f4bbc8c5e548c015eed7c3ff7e59df17ba70da940f7877f0d4097deebea8046
    role: target
  - path: data/habitats/aquatic/water_body.yaml
    sha256: 589b017dac949a9705a816afad5094c2ee9ac1655feb1c771358a07472848239
    role: context
  - path: data/habitats/other/biome.yaml
    sha256: 43080ce9bd411ee97a20d97c17bd923405c040feaf9454d44ca22a2955ce1854
    role: context
  - path: data/habitats/other/environmental.yaml
    sha256: b23a64a2d7594f05716dfc8f525d184fe8bb5d885dbb9e755ba8cc844f433659
    role: context
  - path: data/habitats/other/environmental_system.yaml
    sha256: 2c227791ce7b92c16ae9b76ad8295be95efee73cb65ec7050d1de2b00c8eecbc
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
  - path: history/mappings/gulf/2026-09-11T063533Z-codex-gpt-5-cfe960.yaml
    sha256: a6e47bc32e1270bf054fd6cb436b66bfc58ec148054f2677c209bf2a8d7b29d0
    role: context
  - path: history/mappings/intertidal_zone/2026-10-06T183132Z-codex-gpt-5-6d1f29.yaml
    sha256: cadcd14a51a3621fa4d993bf027706e0e5e6d06a5b26d0ddecbcc24da6e26171
    role: context
  - path: history/mappings/subtidal_zone__792000f9/2026-10-06T155005Z-codex-gpt-5-16648e.yaml
    sha256: 79954c37f8cb9d252e0974a16d9794f0e51146894e18b13c023665d483163517
    role: context
  - path: history/other/marine_water_body/2026-10-03T211358Z-claude-code-9bd806.yaml
    sha256: 593edc2be58b8c7f5082d82f2f8e6de6f3a93d5919f72b4420b0abc65a2c2c51
    role: context
  - path: history/other/marine_water_body/2026-10-03T211516Z-codex-d2f76b.yaml
    sha256: 57c12996f2c2f8ade72b763d7b5b6cba182fadc5abf317b4142087370403ab04
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/pr_review/20261006T205343Z-volcanic-water-publication.md
    sha256: 75eded0a0b2f8962312d9efe8e6520b67871c23dbb0b1e83f1ea505bd3c07768
    role: context
  - path: reports/pr_review/20261007T000816Z-wetland-area-publication.md
    sha256: 7e0960675b13a09db3e96b53417dfdda3d633e884ffc7c0f7202b27f2df2be7e
    role: context
  - path: reports/yaml_record_review/20260921T164930Z-aquifer__33e3996b.md
    sha256: 7e32db9e0ca1fafce660a216b83d27ae47be6e6519e9125d488e1f4c94ff0979
    role: context
  - path: reports/yaml_record_review/20260921T173138Z-archipelago.md
    sha256: 6a80cf09fd2ccee07b70e66514aec05bf2556fd96d6e96c342891d4f80793f73
    role: context
  - path: reports/yaml_record_review/20260921T183205Z-atoll_lagoon.md
    sha256: 369070348a70b536fc9d90249347101927f579a8eeff256d5b5f1f1b5108064b
    role: context
  - path: reports/yaml_record_review/20260921T201614Z-benthic_zone.md
    sha256: 7a314c7269e584f26a32ed5cef6dc96ecb385a108c7095c786af9abdd14743f8
    role: context
  - path: reports/yaml_record_review/20260921T224523Z-biofouling__fa010eab.md
    sha256: f274e9df67c6a9d095c875ba58422388e8729f658ab32ad6885ccf401328ac7e
    role: context
  - path: reports/yaml_record_review/20260926T082617Z-waste__ae37fc5e.md
    sha256: f924cb5fc215d62146f5d4a333ea1613809b77a4a245b5e60f0e659c2692d013
    role: context
  - path: reports/yaml_record_review/20260926T173701Z-mine_water__20810f85.md
    sha256: 27d5a4bd2403e9d7780d97a382d93441af29afa94d6e27d7c2566aafd648e9b6
    role: context
  - path: reports/yaml_record_review/20260927T031816Z-coastal_lagoon.md
    sha256: 1c1d03cdfbc2ac45c14a36a6ed259efefa815ba56faac9c52639a01d7a2daeac
    role: context
  - path: reports/yaml_record_review/20260927T034749Z-coastal_sea_water.md
    sha256: f6274c9b7b2f525cbc24349707070f7d5a1345e5c60f4c26318e3c33377b4f6c
    role: context
  - path: reports/yaml_record_review/20260927T042003Z-coastal_water_body.md
    sha256: 211ebbbf56dc1910274ee18d18f394d051797926ef584b257613bb02e0bfad81
    role: context
  - path: reports/yaml_record_review/20260927T052345Z-cold_seep.md
    sha256: 0df47f7d6f888d495d5f0982ae6f50975ec08de28718ba8179779d8170b47790
    role: context
  - path: reports/yaml_record_review/20260927T070044Z-continental_margin.md
    sha256: 19b399914525093f25c7e2b723a1160fc918921694bb78fb9c45caf59d704ce1
    role: context
  - path: reports/yaml_record_review/20260927T123621Z-deep_subsurface__f51dcfb9.md
    sha256: 39bacc94378e6a7879ea32cebee5afe9bfc032539ba819c3cbe19a224e69f29a
    role: context
  - path: reports/yaml_record_review/20260927T130739Z-deepwater_brine_lake.md
    sha256: f46b02db6565338e8f45bbb85cb9efbf32b409ec777a31a2c7bf17ba18f61d4f
    role: context
  - path: reports/yaml_record_review/20260927T134057Z-demersal_zone.md
    sha256: de9562eec474e99fd7c50e4d416717af1cc5432a421bb180269f47a13bd997ea
    role: context
  - path: reports/yaml_record_review/20261002T014625Z-epipelagic.md
    sha256: f2683ef6750b0a73b79307eeee3e8f80f9b740caac75ec668e8357297cf24a47
    role: context
  - path: reports/yaml_record_review/20261002T074751Z-fjord.md
    sha256: e1a7c3184ac3d502b27e96da28380c8df732a443127797a8d4349faa43162aff
    role: context
  - path: reports/yaml_record_review/20261003T080641Z-fossil.md
    sha256: 1189e6262e0ae4473bf6e3f8d4982a2670db64d698c83316e486a453a3a5145b
    role: context
  - path: reports/yaml_record_review/20261003T105031Z-gulf.md
    sha256: dabc2844c37e5859277baea55d30a244958e50edca1b2155d2845d5ba386c4bc
    role: context
  - path: reports/yaml_record_review/20261003T105248Z-hadalpelagic.md
    sha256: a46bd118223d4261f147e092bf21285038b52c177d6c042e6c6db54a1a09d6e2
    role: context
  - path: reports/yaml_record_review/20261003T105513Z-harbor.md
    sha256: c375bbc66f1680372f1c7008dc03d5e92c1e2e7dd43f3fe6a077a705747223ac
    role: context
  - path: reports/yaml_record_review/20261003T122253Z-hydrothermal_vent.md
    sha256: e5ed7a7ef77e714c127ab080ab58cf95c846b6bed915eb1ceb1c1eab235383d2
    role: context
  - path: reports/yaml_record_review/20261003T140149Z-hypoxic_zone.md
    sha256: e90ef6ffc8d0860ca2dc63e0fb934934380ae670c0b9c4f885f8b60213aa959f
    role: context
  - path: reports/yaml_record_review/20261003T143338Z-ice_shelf.md
    sha256: a85824734275b133c04ebf928a1bfeac37f6bdec1813b73eba6c182c4be9dbc8
    role: context
  - path: reports/yaml_record_review/20261003T143846Z-inlet.md
    sha256: d4a245a43dae88035594855de3011332a80cd4c3dafd9b5cf76c705c4bf081ea
    role: context
  - path: reports/yaml_record_review/20261003T151340Z-intertidal_zone__2f295854.md
    sha256: 8deb917e036da4baa06b6c53e9cd5f62a3ed2840653cc9f71999700e0061697a
    role: context
  - path: reports/yaml_record_review/20261003T160438Z-lentic_water_body.md
    sha256: 448b220e3a8a5fe001286965d18caceb934884f01ea3ec1d4d9146dd9d5e6ea0
    role: context
  - path: reports/yaml_record_review/20261003T180537Z-marine_basin_floor.md
    sha256: a7749e298e514c8cc8708c0ba8b8ae544744f719a3301ad1687ec1a915e06160
    role: context
  - path: reports/yaml_record_review/20261003T181016Z-marine_bathypelagic_zone.md
    sha256: a5f9b0f2f5e844b67b0584d65671b15f1f7f50a2b9b27aa63da88af7adc66df6
    role: context
  - path: reports/yaml_record_review/20261003T183900Z-marine_benthic_biome.md
    sha256: 322888a864fcf4ebda315f7b4f482b350955686518f8b17c5b1bd95bc798529d
    role: context
  - path: reports/yaml_record_review/20261003T190816Z-marine_lake.md
    sha256: 5b2c24401d3e534c3b85cbc016896750eb8cc311f05029f06ad9f81c5326374a
    role: context
  - path: reports/yaml_record_review/20261003T191057Z-marine_littoral_zone.md
    sha256: 1224f670aacf199aba96b6e77a0a182ae0ee75354956763da79702161e8738a3
    role: context
  - path: reports/yaml_record_review/20261003T191323Z-marine_mesopelagic_zone.md
    sha256: b5fce3b82d069e0a02552001d2ee6b03dfcdab62164cf85538809a58ddb86213
    role: context
  - path: reports/yaml_record_review/20261003T193646Z-marine_mud.md
    sha256: 862d9bc67320f482e97655fc63f84cebba0901385aea344e0f1c7572ebaaff04
    role: context
  - path: reports/yaml_record_review/20261003T194112Z-marine_pelagic_zone.md
    sha256: 11a111c73be28b588a4d3cbb6a8ce3a46b9c57d28f27611a6d5ff4674830c6f3
    role: context
  - path: reports/yaml_record_review/20261003T201434Z-marine_sediment.md
    sha256: 934f32cad95162955f3d45f3dbaf811bef9e72a622e96e978c78f6e922bd6e10
    role: context
  - path: reports/yaml_record_review/20261003T202104Z-marine_supra_littoral_zone.md
    sha256: fd36e62c946a80c0a0ff442f9cfadee5d48a2efea8ebf19b595d04c4d8b1f3a2
    role: context
  - path: reports/yaml_record_review/20261003T205749Z-marine_water_body.md
    sha256: 3ff02dce6f202ddc7367e0a35e6182ca67862e854aa5a0281c1b54739edf40b0
    role: context
  - path: reports/yaml_record_review/20261004T194729Z-mud_volcano__980e0b1f.md
    sha256: 1e32d50eeb6654cc5710c5609c194ff3c950ff3ca4a1fd6db92d26b7e4436e39
    role: context
  - path: reports/yaml_record_review/20261004T204024Z-ocean.md
    sha256: d74ef8bb32d0a18c7397b9614c7f8632b56432bf85d6b9517315e7f35c5275c5
    role: context
  - path: reports/yaml_record_review/20261004T211318Z-ocean_trench.md
    sha256: 05e67714a13fbe3823f3ac6d61fbcf16ef69164150de37c89ffebf42876062ba
    role: context
  - path: reports/yaml_record_review/20261004T211801Z-oceanic_abyssopelagic_zone_biome.md
    sha256: ebddfd1916c01593685971c319c6713be6b2f302eca20ed89e6a1d90966b30b9
    role: context
  - path: reports/yaml_record_review/20261004T213438Z-oceanic_zone.md
    sha256: b2fc13da6c9521db8bde443cbc508ea0b4c072c270aa04a5afef4066e30c2e32
    role: context
  - path: reports/yaml_record_review/20261004T224406Z-oil_seep.md
    sha256: 0b26acf7ac5ee58e4cb6ab31d7db1bbe2ae3cf9a8c80b9956e08422e75c74a72
    role: context
  - path: reports/yaml_record_review/20261005T012524Z-river_plume.md
    sha256: 03480061acdb6f29377ca8ef77a8475d85ea0bc310cc6f0c8b19516d40a5f4dd
    role: context
  - path: reports/yaml_record_review/20261005T072944Z-sea.md
    sha256: fb8cda2994b98bdaf390488f4a322fcdc447c64b0793574a6b11872793262cc9
    role: context
  - path: reports/yaml_record_review/20261005T074020Z-sea_grass_bed.md
    sha256: 9fb4444c754ce1e1723ebf070091b4bf00d64b4ec644c03043940b8ac80bfbf0
    role: context
  - path: reports/yaml_record_review/20261005T081127Z-sea_ice.md
    sha256: bf1763d4557cdbf621fa03372f0c4b3f544b097d72390e585f617083bceb78b1
    role: context
  - path: reports/yaml_record_review/20261005T090236Z-seaweed.md
    sha256: f5f126cbbdc1bd108779d71930da632e14586c69f7b7fcf0bb4ddc828cc04fb9
    role: context
  - path: reports/yaml_record_review/20261005T174924Z-sediment__978ea781.md
    sha256: 15354ff2c17226c1495c2590585e389170b386175952fec2f334034130196c1e
    role: context
  - path: reports/yaml_record_review/20261005T175903Z-sediment__a24ea793.md
    sha256: 1dba7e9463e1125bf4cc2fdafde1bdc7245d48462d224e7b0322b39d2cb1b465
    role: context
  - path: reports/yaml_record_review/20261005T184701Z-sediment__a8039b03.md
    sha256: 18a768150425920c3866d6e835a1578db9f426ea9c53317fc22c69b0784dee7e
    role: context
  - path: reports/yaml_record_review/20261005T192420Z-sediment__b9940958.md
    sha256: cca02be9f3c681fb382d2e7324edbd7527d11f10decd479c0a5cfaa24f6c1c9f
    role: context
  - path: reports/yaml_record_review/20261005T201439Z-sediment__ce4efe59.md
    sha256: 18e8764e8799b2ca03b95c260a286c189559eebaef8bd10bcef9c42458cd5915
    role: context
  - path: reports/yaml_record_review/20261006T005847Z-shipwreck.md
    sha256: c241ce621d4ae1fe601d8e0fafb633eabfa81d0c7bd9db07f4e71863bf3b39fd
    role: context
  - path: reports/yaml_record_review/20261006T101729Z-strait.md
    sha256: 6e5c4d5a8100a6d35ebf4ddf822150bb4f6a143049ba879eee8156c8fa63e6a4
    role: context
  - path: reports/yaml_record_review/20261006T114536Z-subterranean_estuary.md
    sha256: 4b431e0ab82eb1e3cd57f5e89fb5d8b6d1d326a64866f5fedc0707ed4ced98c7
    role: context
  - path: reports/yaml_record_review/20261006T151610Z-subtidal_zone__792000f9.md
    sha256: 3dd8f70b4c3773d4a1f7a0a68cb985b4a3b51d59bf2e0e0677fe345a250b9b8f
    role: context
  - path: reports/yaml_record_review/20261006T180914Z-tidal_mudflat.md
    sha256: 89c10e84d8d94337662699f0baa0870101dc0d70f0b091b0882499eea0d0e1a6
    role: context
  - path: reports/yaml_record_review/20261006T203103Z-volcanic.md
    sha256: 34a0a3918a8600afb53ce1d386c4f8984a86eabde4f1cd1aa4a5a24c7dabc878
    role: context
  - path: reports/yaml_record_review/20261006T235209Z-wetland_area.md
    sha256: ef4f2e2a8bbc04f80e4e2fd1bf5cc9b107f06c65f9527ea58da5a1fde61b9ef7
    role: context
  - path: research/habitats/aquatic/non-marine-saline-and-alkaline-habitatmech-gold-ce244e62cd-deep-research-claude_code.md
    sha256: 21ae034cb3b0945799a66cbf6d689755bd21940a7583e9978657be0998119cb7
    role: context
  - path: research/habitats/aquatic/seaweed-habitatmech-gold-0e7a5162bb-deep-research-claude_code.md
    sha256: 30ea8adaa34fc4b27f349ece7ed868408a66683052aa12205976a982c09968ad
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
- target_id: ENVO:00001999
  path: data/habitats/aquatic/marine_water_body.yaml
  label: marine water body
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
    path: data/raw/bacdive_isolation_sources.tsv
    role: Frozen BACDIVE source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/isolation_source_groundings.tsv
    role: Frozen BACDIVE source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Frozen BACDIVE source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Frozen PREGO source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Frozen PREGO source inventory
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/marine_water_body.yaml
    role: Curated mechanism nodes, edges and evidence
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
  - ENVO:00001999
  exclusions:
  - target: Other 3207 current records
    reason: Context reads are not their full scientific review.
checks:
- check_id: C0
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00001999
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=ed9e0d0f382e4502a64f4de10102c4512bddca38
    just validate data/habitats/aquatic/marine_water_body.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:22:17.396509Z to 2026-10-12T05:22:20.564796Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C1
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00001999
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
  - ENVO:00001999
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
  - ENVO:00001999
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
  - ENVO:00001999
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
  - ENVO:00001999
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
  - ENVO:00001999
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
  - ENVO:00001999
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
  - ENVO:00001999
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
  - ENVO:00001999
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
  - ENVO:00001999
  summary: Bounded ignored-inclusive searches did not recover complete original assertion
    inputs; later exports are contextual evidence only.
  evidence_ids:
  - SEARCH
- check_id: IMODULON
  name: Expression-adapter applicability
  required: false
  status: not_applicable
  target_ids:
  - ENVO:00001999
  summary: The successful 28-dataset inventory was read for graph scope. No matching
    claim-specific organism/strain/gene or expression-module assertion requires a
    search or summarize call. Absence is not negative ecological evidence.
  evidence_ids:
  - IMODULONDB
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/aquatic/marine_water_body.yaml
  summary: The physical lentic marine water body is not an aquatic biome. Preserve
    BacDive 2040 STRAIN, GOLD 6420 ORGANISM and PREGO 171 TAXON assertions, the two
    CLOSE source mappings and 50 selected associations. The revised 15-edge carbon-pump
    graph is explicitly conditional and its earlier unrelated citation is no longer
    active. Current node types still confuse ecological assemblages, habitats and
    enzyme products with taxa, exposures and a trait.
  accessed_at: '2026-10-12T05:41:00.550099Z'
  support: supports
  locator: Entire captured YAML read, including all taxa, parameters, graphs and generated
    history
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml
  summary: Applied exact identity, strict-genus, MIxS roles, source-unit/score and
    ITEM lifecycle contracts; graph node types retain their biological definitions.
  accessed_at: '2026-10-12T05:41:00.550099Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5",
    "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier":
    "habitatmech:BACDIVE.407144fe70", "notes": "Multi-source review pass: this record
    is attested by more than one independent vocabulary, and this source''s label
    or path was read against the record''s ontology term to check the merge is right.
    It agrees. Source concepts in the same pass whose labels did not agree were re-decided
    rather than endorsed; see the pass''s other decisions of the same date.", "object_id":
    "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row":
    28}, {"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13",
    "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:GOLD.5856c699e4",
    "notes": "Multi-source review pass: this record is attested by more than one independent
    vocabulary, and this source''s label or path was read against the record''s ontology
    term to check the merge is right. It agrees. Source concepts in the same pass
    whose labels did not agree were re-decided rather than endorsed; see the pass''s
    other decisions of the same date.", "object_id": "", "object_label": "", "relation":
    "", "review_depth": "ITEM"}, "logical_row": 552}, {"data": {"category": "", "curator":
    "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status":
    "", "identifier": "habitatmech:PREGO.a653eb2a85", "notes": "Multi-source review
    pass: this record is attested by more than one independent vocabulary, and this
    source''s label or path was read against the record''s ontology term to check
    the merge is right. It agrees. Source concepts in the same pass whose labels did
    not agree were re-decided rather than endorsed; see the pass''s other decisions
    of the same date.", "object_id": "", "object_label": "", "relation": "", "review_depth":
    "ITEM"}, "logical_row": 1490}], "data/raw/bacdive_isolation_sources.tsv": [{"data":
    {"bacdive_id": "bacdive.isolation_source:marine", "label": "Marine", "source_slug":
    "marine", "strain_count": "2040", "taxon_count": "1805"}, "logical_row": 16}],
    "data/raw/bacdive_source_taxa.tsv": [{"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "", "rank": "1", "strain_count": "24", "taxon_id": "NCBITaxon:1876",
    "taxon_label": "Micromonospora sp."}, "logical_row": 1723}, {"data": {"bacdive_id":
    "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "2", "strain_count":
    "14", "taxon_id": "NCBITaxon:83428", "taxon_label": "uncultured Bacillus sp."},
    "logical_row": 1724}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "", "rank": "3", "strain_count": "11", "taxon_id": "NCBITaxon:1869227",
    "taxon_label": "bacterium"}, "logical_row": 1725}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "", "rank": "4", "strain_count": "11", "taxon_id": "NCBITaxon:562",
    "taxon_label": "Escherichia coli"}, "logical_row": 1726}, {"data": {"bacdive_id":
    "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "5", "strain_count":
    "7", "taxon_id": "NCBITaxon:314275", "taxon_label": "Alteromonas mediterranea"},
    "logical_row": 1727}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "", "rank": "6", "strain_count": "6", "taxon_id": "NCBITaxon:2",
    "taxon_label": "Bacteria"}, "logical_row": 1728}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "PREGO", "rank": "7", "strain_count": "6", "taxon_id": "NCBITaxon:28108",
    "taxon_label": "Alteromonas macleodii"}, "logical_row": 1729}, {"data": {"bacdive_id":
    "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "8", "strain_count":
    "6", "taxon_id": "NCBITaxon:53249", "taxon_label": "Pseudoalteromonas sp."}, "logical_row":
    1730}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by":
    "", "rank": "9", "strain_count": "5", "taxon_id": "NCBITaxon:50741", "taxon_label":
    "Marinobacter sp."}, "logical_row": 1731}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "", "rank": "10", "strain_count": "5", "taxon_id": "NCBITaxon:56811",
    "taxon_label": "Psychrobacter sp."}, "logical_row": 1732}, {"data": {"bacdive_id":
    "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "11", "strain_count":
    "4", "taxon_id": "NCBITaxon:1211807", "taxon_label": "Stutzerimonas kunmingensis"},
    "logical_row": 1733}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "", "rank": "12", "strain_count": "4", "taxon_id": "NCBITaxon:1871328",
    "taxon_label": "Kocuria sp."}, "logical_row": 1734}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "", "rank": "13", "strain_count": "4", "taxon_id": "NCBITaxon:1931",
    "taxon_label": "Streptomyces sp."}, "logical_row": 1735}, {"data": {"bacdive_id":
    "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "14", "strain_count":
    "4", "taxon_id": "NCBITaxon:2024855", "taxon_label": "Rhodopirellula sp."}, "logical_row":
    1736}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by":
    "", "rank": "15", "strain_count": "4", "taxon_id": "NCBITaxon:2099376", "taxon_label":
    "Desulforhopalus sp."}, "logical_row": 1737}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "", "rank": "16", "strain_count": "4", "taxon_id": "NCBITaxon:2213",
    "taxon_label": "Methanosarcina sp."}, "logical_row": 1738}, {"data": {"bacdive_id":
    "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "17", "strain_count":
    "4", "taxon_id": "NCBITaxon:265606", "taxon_label": "Rhodopirellula baltica"},
    "logical_row": 1739}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "PREGO", "rank": "18", "strain_count": "4", "taxon_id": "NCBITaxon:28258",
    "taxon_label": "Cobetia marina"}, "logical_row": 1740}, {"data": {"bacdive_id":
    "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "19", "strain_count":
    "4", "taxon_id": "NCBITaxon:2926447", "taxon_label": "Marinispora"}, "logical_row":
    1741}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by":
    "", "rank": "20", "strain_count": "4", "taxon_id": "NCBITaxon:44751", "taxon_label":
    "Exiguobacterium sp."}, "logical_row": 1742}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "", "rank": "21", "strain_count": "4", "taxon_id": "NCBITaxon:51671",
    "taxon_label": "Microbacterium sp."}, "logical_row": 1743}, {"data": {"bacdive_id":
    "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "22", "strain_count":
    "4", "taxon_id": "NCBITaxon:885", "taxon_label": "Desulfovibrio sp."}, "logical_row":
    1744}, {"data": {"bacdive_id": "bacdive.isolation_source:marine", "corroborated_by":
    "", "rank": "23", "strain_count": "3", "taxon_id": "NCBITaxon:1042", "taxon_label":
    "Erythrobacter sp."}, "logical_row": 1745}, {"data": {"bacdive_id": "bacdive.isolation_source:marine",
    "corroborated_by": "", "rank": "24", "strain_count": "3", "taxon_id": "NCBITaxon:1486246",
    "taxon_label": "Halomonas sp."}, "logical_row": 1746}, {"data": {"bacdive_id":
    "bacdive.isolation_source:marine", "corroborated_by": "", "rank": "25", "strain_count":
    "3", "taxon_id": "NCBITaxon:1703256", "taxon_label": "Pseudoalteromonas gelatinilytica"},
    "logical_row": 1747}], "data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count":
    "0", "canonical_path": "Environmental > Aquatic > Marine", "depth": "3", "ecosystem":
    "Environmental", "ecosystem_category": "Aquatic", "ecosystem_subtype": "", "ecosystem_type":
    "Marine", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:3487|gold.ecosystem:3768|gold.ecosystem:4003",
    "leaf_label": "Marine", "organism_count": "6420", "specific_ecosystem": "", "study_count":
    "0", "total_assertions": "6420"}, "logical_row": 8}], "data/raw/gold_path_biosamples.tsv":
    [{"data": {"biosample_count": "5248", "canonical_path": "Environmental > Aquatic
    > Marine", "ecosystem_path_id": "4003"}, "logical_row": 8}], "data/raw/gold_path_triads.tsv":
    [{"data": {"canonical_path": "Environmental > Aquatic > Marine", "distinct_terms":
    "11", "samples": "3749", "slot": "broad", "studies": "141", "studies_agreeing":
    "128", "top_label": "marine biome", "top_share": "0.96", "top_term": "ENVO:00000447"},
    "logical_row": 434}, {"data": {"canonical_path": "Environmental > Aquatic > Marine",
    "distinct_terms": "31", "samples": "3749", "slot": "local", "studies": "141",
    "studies_agreeing": "113", "top_label": "marine water body", "top_share": "0.79",
    "top_term": "ENVO:00001999"}, "logical_row": 435}, {"data": {"canonical_path":
    "Environmental > Aquatic > Marine", "distinct_terms": "22", "samples": "3749",
    "slot": "medium", "studies": "141", "studies_agreeing": "109", "top_label": "sea
    water", "top_share": "0.87", "top_term": "ENVO:00002149"}, "logical_row": 436}],
    "data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:01000617",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:00001999"}, "logical_row": 5261}],
    "data/raw/ontology_terms.tsv": [{"data": {"definition": "A lentic water body which
    is composed primarily of marine water.", "deprecated": "", "directly_referenced":
    "TRUE", "label": "marine water body", "label_only": "FALSE", "ontology": "ENVO",
    "synonyms": "body of marine water|marine waterbody", "term_id": "ENVO:00001999"},
    "logical_row": 7158}], "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "1", "taxon_id": "NCBITaxon:102",
    "taxon_label": "Polaribacter glomeratus"}, "logical_row": 5366}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "2", "taxon_id": "NCBITaxon:1026",
    "taxon_label": "Marinoscillum furvescens"}, "logical_row": 5367}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "3", "taxon_id": "NCBITaxon:104268",
    "taxon_label": "Tenacibaculum mesophilum"}, "logical_row": 5368}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "4", "taxon_id": "NCBITaxon:107401",
    "taxon_label": "Tenacibaculum maritimum"}, "logical_row": 5369}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "5", "taxon_id": "NCBITaxon:111770",
    "taxon_label": "Thiothrix fructosivorans"}, "logical_row": 5370}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "6", "taxon_id": "NCBITaxon:114404",
    "taxon_label": "Edaphosphingomonas fennica"}, "logical_row": 5371}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "7", "taxon_id": "NCBITaxon:1282",
    "taxon_label": "Staphylococcus epidermidis"}, "logical_row": 5372}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "8", "taxon_id": "NCBITaxon:132144",
    "taxon_label": "Candidatus Glomeribacter gigasporarum"}, "logical_row": 5373},
    {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "9", "taxon_id":
    "NCBITaxon:133924", "taxon_label": "Leisingera methylohalidivorans"}, "logical_row":
    5374}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "10", "taxon_id":
    "NCBITaxon:13616", "taxon_label": ""}, "logical_row": 5375}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "11", "taxon_id": "NCBITaxon:1371",
    "taxon_label": "Marinococcus halophilus"}, "logical_row": 5376}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "12", "taxon_id": "NCBITaxon:143223",
    "taxon_label": "Salegentibacter salegens"}, "logical_row": 5377}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "13", "taxon_id": "NCBITaxon:156128",
    "taxon_label": ""}, "logical_row": 5378}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score":
    "4", "rank": "14", "taxon_id": "NCBITaxon:156133", "taxon_label": ""}, "logical_row":
    5379}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "15", "taxon_id":
    "NCBITaxon:158080", "taxon_label": ""}, "logical_row": 5380}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00001999", "prego_score": "4", "rank": "16", "taxon_id": "NCBITaxon:158500",
    "taxon_label": "Novosphingobium resinovorum"}, "logical_row": 5381}, {"data":
    {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE",
    "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "17", "taxon_id": "NCBITaxon:168275",
    "taxon_label": "Psychromonas arctica"}, "logical_row": 5382}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "BACDIVE", "direct_flag": "TRUE",
    "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "18", "taxon_id": "NCBITaxon:172371",
    "taxon_label": "Alloalcanivorax venustensis"}, "logical_row": 5383}, {"data":
    {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE",
    "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "19", "taxon_id": "NCBITaxon:173365",
    "taxon_label": "Methylobacter tundripaludum"}, "logical_row": 5384}, {"data":
    {"channels": "environmental_samples", "corroborated_by": "BACDIVE", "direct_flag":
    "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank": "20", "taxon_id":
    "NCBITaxon:180542", "taxon_label": "Salinisphaera shabanensis"}, "logical_row":
    5385}, {"data": {"channels": "environmental_samples", "corroborated_by": "BACDIVE",
    "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank":
    "21", "taxon_id": "NCBITaxon:184914", "taxon_label": "Corallococcus coralloides"},
    "logical_row": 5386}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank":
    "22", "taxon_id": "NCBITaxon:186022", "taxon_label": "Thalassionema frauenfeldii"},
    "logical_row": 5387}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank":
    "23", "taxon_id": "NCBITaxon:188908", "taxon_label": "Oleispira antarctica"},
    "logical_row": 5388}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank":
    "24", "taxon_id": "NCBITaxon:190308", "taxon_label": "Shewanella schlegeliana"},
    "logical_row": 5389}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00001999", "prego_score": "4", "rank":
    "25", "taxon_id": "NCBITaxon:191302", "taxon_label": "Devosia neptuniae"}, "logical_row":
    5390}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category": "biolink:OntologyClass",
    "channels": "environmental_samples", "direct_assertion_count": "171", "max_prego_score":
    "4", "ontology": "ENVO", "prego_id": "ENVO:00001999", "prego_synonyms": "marine
    water bodies|marine water body", "taxon_count": "171"}, "logical_row": 158}]}'
  accessed_at: '2026-10-12T05:41:00.550099Z'
  support: supports
  locator: Exact logical TSV rows, header=row1; filtered by current source IDs and
    exact paths, not legacy issue line numbers
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 3, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13",
    "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:BACDIVE.407144fe70",
    "notes": "Multi-source review pass: this record is attested by more than one independent
    vocabulary, and this source''s label or path was read against the record''s ontology
    term to check the merge is right. It agrees. Source concepts in the same pass
    whose labels did not agree were re-decided rather than endorsed; see the pass''s
    other decisions of the same date.", "object_id": "", "object_label": "", "relation":
    "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "CLOSE", "identifier": "ENVO:00001999", "mapping_predicate": "skos:closeMatch",
    "reviewed": true, "route": "curated_review_of_bacdive_mapping_table"}, "automatic":
    {"category": null, "contributes_grounding": true, "decision": null, "extra_parents":
    [], "extra_xrefs": [], "grounding_status": "CLOSE", "identifier": "ENVO:00001999",
    "mapping_predicate": "skos:closeMatch", "reviewed": false, "route": "bacdive_mapping_table"},
    "minted": "habitatmech:BACDIVE.407144fe70", "source": "BACDIVE", "source_id":
    "bacdive.isolation_source:marine"}, {"actual": {"category": null, "contributes_grounding":
    true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13",
    "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:GOLD.5856c699e4",
    "notes": "Multi-source review pass: this record is attested by more than one independent
    vocabulary, and this source''s label or path was read against the record''s ontology
    term to check the merge is right. It agrees. Source concepts in the same pass
    whose labels did not agree were re-decided rather than endorsed; see the pass''s
    other decisions of the same date.", "object_id": "", "object_label": "", "relation":
    "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "CLOSE", "identifier": "ENVO:00001999", "mapping_predicate": "skos:closeMatch",
    "reviewed": true, "route": "curated_review_of_gold_mapping_table"}, "automatic":
    {"category": null, "contributes_grounding": true, "decision": null, "extra_parents":
    [], "extra_xrefs": [], "grounding_status": "CLOSE", "identifier": "ENVO:00001999",
    "mapping_predicate": "skos:closeMatch", "reviewed": false, "route": "gold_mapping_table"},
    "minted": "habitatmech:GOLD.5856c699e4", "source": "GOLD", "source_id": "gold.ecosystem:3487"},
    {"actual": {"category": null, "contributes_grounding": true, "decision": {"category":
    "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status":
    "", "identifier": "habitatmech:PREGO.a653eb2a85", "notes": "Multi-source review
    pass: this record is attested by more than one independent vocabulary, and this
    source''s label or path was read against the record''s ontology term to check
    the merge is right. It agrees. Source concepts in the same pass whose labels did
    not agree were re-decided rather than endorsed; see the pass''s other decisions
    of the same date.", "object_id": "", "object_label": "", "relation": "parent",
    "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00001999", "mapping_predicate": null, "reviewed":
    true, "route": "curated_review_of_prego_self_grounded"}, "automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "EXACT", "identifier": "ENVO:00001999", "mapping_predicate":
    null, "reviewed": false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.a653eb2a85",
    "source": "PREGO", "source_id": "ENVO:00001999"}], "source_concepts": 3}'
  accessed_at: '2026-10-12T05:41:00.550099Z'
  support: supports
  locator: Executed complete-document reconstruction; all 40 matched; routes distinguish
    source mints and generated identity
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
    []}}, "ENVO:00000428": {"definitions": ["A biome is an ecosystem which is undergoing
    climactic ecological succession."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_01001110"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000056"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01001827"]}],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}],
    "labels": ["biome"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000813",
    "http://purl.obolibrary.org/obo/ENVO_01001110", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_01000817"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/PCO_0000002"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0000056"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_01001827"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0002507"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/PCO_0000002"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": [], "hasExactSynonym": ["major habitat type"], "hasNarrowSynonym":
    [], "hasRelatedSynonym": ["EcosytemType"]}}, "ENVO:00001999": {"definitions":
    ["A lentic water body which is composed primarily of marine water."], "deprecated":
    [], "equivalents": [], "labels": ["marine water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000617"],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["body
    of marine water", "marine waterbody"], "hasNarrowSynonym": [], "hasRelatedSynonym":
    []}}, "ENVO:00002030": {"definitions": ["A biome which is determined by a water
    body and which has ecological climax communities adapted to life in or on water."],
    "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00000428"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002507"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00000063"]}],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}],
    "labels": ["aquatic biome"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000428",
    "http://purl.obolibrary.org/obo/ENVO_01001787"], "replacements": [], "synonyms":
    {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym":
    []}}, "ENVO:01000254": {"definitions": ["A system which has the disposition to
    environ one or more material entities."], "deprecated": [], "equivalents": [],
    "labels": ["environmental system"], "parents": ["http://purl.obolibrary.org/obo/RO_0002577"],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["environment"],
    "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:01000617": {"definitions":
    ["A lentic water body is a water body in which the accumulated water, in its totality,
    has very little to no directed flow."], "deprecated": [], "equivalents": [], "labels":
    ["lentic water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000063"],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [],
    "hasNarrowSynonym": [], "hasRelatedSynonym": []}}}'
  accessed_at: '2026-10-12T05:20:26.560054Z'
  support: supports
  locator: Official OWL retrieved 12-Oct; labels, definitions, typed synonyms, named
    parents and restrictions; no snapshot refresh
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats/aquatic/lentic_water_body.yaml; data/habitats/aquatic/water_body.yaml;
    data/habitats/aquatic/aquatic_biome.yaml; data/habitats/other/environmental.yaml;
    data/habitats/other/environmental_system.yaml; data/habitats/other/biome.yaml
  summary: '{"ENVO:00000063": {"definition": "An accumulation of water of varying
    size.", "grounding_status": "EXACT", "label": "water body", "parent_habitats":
    ["ENVO:01000685"]}, "ENVO:00000428": {"definition": "A biome is an ecosystem which
    is undergoing climactic ecological succession.", "grounding_status": "EXACT",
    "label": "biome", "parent_habitats": ["ENVO:01000813", "ENVO:01001110"]}, "ENVO:00002030":
    {"definition": "A biome which is determined by a water body and which has ecological
    climax communities adapted to life in or on water.", "grounding_status": "EXACT",
    "label": "aquatic biome", "parent_habitats": ["ENVO:00000428", "ENVO:01001787",
    "habitatmech:BACDIVE.0f1e92a02c"]}, "ENVO:01000254": {"definition": "A system
    which has the disposition to environ one or more material entities.", "grounding_status":
    "EXACT", "label": "environmental system", "parent_habitats": null}, "ENVO:01000617":
    {"definition": "A lentic water body is a water body in which the accumulated water,
    in its totality, has very little to no directed flow.", "grounding_status": "EXACT",
    "label": "lentic water body", "parent_habitats": ["ENVO:00000063"]}, "habitatmech:BACDIVE.0f1e92a02c":
    {"definition": "An environmental system which is a portion of the air, water,
    or land surface or subsurface of an astronomical body sampled in place, and which
    is neither bounded by a host organism nor constituted by a constructed or operated
    artefact.", "grounding_status": "UNGROUNDED", "label": "free-living environment",
    "parent_habitats": ["ENVO:01000254"]}}'
  accessed_at: '2026-10-12T05:41:00.550099Z'
  support: supports
  locator: Ancestor context adds no full-record coverage
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  summary: 'Exact positional census counts={"Biosample": 5389, "Organism": 5364, "SequencingProject":
    10866}; individually inspected descriptions={"Biosample": [{"data": {"BIOSAMPLE
    GOLD ID": "Gb0051204", "BIOSAMPLE NAME": "Marine ecosystem from Palmer Station,
    Antarctica ", "BIOSAMPLE NCBI TAX NAME": "marine metagenome", "BIOSAMPLE SAMPLE
    COLLECTION SITE": "Palmer Station, Antarctica"}, "row": 200}, {"data": {"BIOSAMPLE
    GOLD ID": "Gb0051208", "BIOSAMPLE NAME": "Marine ecosystem from Technion - Israel
    Institute of Technology, Israel", "BIOSAMPLE NCBI TAX NAME": "marine metagenome",
    "BIOSAMPLE SAMPLE COLLECTION SITE": "Marine Roseobacter"}, "row": 201}, {"data":
    {"BIOSAMPLE GOLD ID": "Gb0051293", "BIOSAMPLE NAME": "Marine ecosystem from Monterey
    Bay, USA", "BIOSAMPLE NCBI TAX NAME": "marine metagenome", "BIOSAMPLE SAMPLE COLLECTION
    SITE": "Monterey Bay, Pacific Ocean"}, "row": 248}], "Organism": [{"data": {"ORGANISM
    GOLD ID": "Go0000012", "ORGANISM NAME": "Altermonas sp. SCGC AC-669 C16", "ORGANISM
    SAMPLE COLLECTION SITE": "Eastern Tropical South Pacific Ocean, Chile"}, "row":
    11}, {"data": {"ORGANISM GOLD ID": "Go0000017", "ORGANISM HABITAT": "Marine|Aquatic",
    "ORGANISM NAME": "Shewanella baltica OS195", "ORGANISM SAMPLE COLLECTION SITE":
    "Sea-water; anoxic zone; 240 m depth from the Baltic Sea"}, "row": 16}, {"data":
    {"ORGANISM GOLD ID": "Go0000018", "ORGANISM HABITAT": "Marine|Aquatic", "ORGANISM
    NAME": "Hemiselmis andersenii CCMP 644 (nucleomorph)", "ORGANISM SAMPLE COLLECTION
    SITE": "Gulf of Mexico, North Atlantic Sea"}, "row": 17}]}. These later examples
    may include mixed sample/host/enrichment contexts; they do not reconstruct original
    assertion membership. Remaining members and study joins were indexed, not individually
    assessed.'
  accessed_at: '2026-10-11T13:21:51.155056Z'
  support: supports
  locator: Five-position ecosystem paths preserved; contacts excluded; first 3 BioSample
    and Organism descriptions per target
  snapshot_sha256: b222fa9df89ffbd1a30897a1e7302da363c57b463d9948ecc9bfcb9304b4a96f
- evidence_id: CLASS
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  summary: '[{"row": 802, "slug": "marine_water_body", "path": "Environmental > Aquatic
    > Marine", "values": ["4003", "Environmental", "Aquatic", "Marine", "Unclassified",
    "Unclassified"]}]'
  accessed_at: '2026-10-12T05:20:29.451803Z'
  support: supports
  locator: Later official classification; 29 of 31 cohort paths matched; missing tuples
    do not establish nonexistence
  snapshot_sha256: 78ed6ce1c3799a2d6ef2d17e4a9eeee5da48eef78df0b71079c0f942555e5e7d
- evidence_id: TAX0
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1000566%2C1003110%2C1005925%2C1005926%2C1005928%2C1006%2C1007105%2C1007109%2C1007110%2C1007111%2C1007112%2C1007113%2C1007114%2C1007115%2C1007116%2C1007117%2C1007118%2C1007119%2C1007120%2C1007122%2C1007124%2C1009412%2C1009413%2C1009414%2C1009415%2C1009416%2C1009418%2C1009419%2C1009420%2C1009421%2C1017277%2C102%2C1026%2C1027373%2C1027374%2C1028566%2C1028742%2C1028743%2C1028745%2C1028746%2C1028749%2C1028752%2C1031273%2C1031541%2C103810%2C1038845%2C1038928%2C1038929%2C1042%2C104268%2C104270%2C1042877%2C1044%2C104421%2C1045558%2C1048%2C1048221%2C1057%2C106299%2C1074%2C107401%2C1080%2C1089550%2C109263%2C1094980%2C110163%2C1104565%2C1104566%2C110662%2C110663%2C111770%2C1121404%2C1121937%2C1121948%2C1122607%2C1123059%2C1123242%2C1123275%2C114404%2C1150474%2C119394%2C119542%2C1208324%2C1211807%2C121224%2C1217908%2C1219067%2C1242148%2C1246444%2C1246460%2C1265%2C126741%2C1267768%2C1267769%2C1276246%2C1282%2C129958%2C132144%2C133924%2C134561%2C1358%2C13616%2C13686%2C1371%2C1387275%2C139239%2C1394%2C1411902%2C143223%2C143224%2C147%2C1486246%2C150120%2C1543721%2C156%2C156128%2C156133%2C1570%2C158080%2C158192%2C158500%2C1609977%2C161528%2C163248%2C163503%2C168275%2C168759%2C1703256%2C1716143%2C172371%2C173%2C173365%2C173737%2C173764%2C174%2C174302%2C174315%2C1774373%2C179326%2C180542%2C1808508%2C1808945%2C1817405%2C1836499%2C184592%2C184914%2C1855%2C186022%2C1869227%2C1871328&retmode=xml
  summary: 'The three chunks jointly resolve all 346 requested cohort IDs. Target
    results=[{"current_id": "28108", "current_name": "Alteromonas macleodii", "frozen_label":
    "Alteromonas macleodii", "id": "28108", "rank": "species"}, {"current_id": "172371",
    "current_name": "Alloalcanivorax venustensis", "frozen_label": "Alloalcanivorax
    venustensis", "id": "172371", "rank": "species"}, {"current_id": "28258", "current_name":
    "Cobetia marina", "frozen_label": "Cobetia marina", "id": "28258", "rank": "species"},
    {"current_id": "180542", "current_name": "Salinisphaera shabanensis", "frozen_label":
    "Salinisphaera shabanensis", "id": "180542", "rank": "species"}, {"current_id":
    "184914", "current_name": "Corallococcus coralloides", "frozen_label": "Corallococcus
    coralloides", "id": "184914", "rank": "species"}, {"current_id": "102", "current_name":
    "Polaribacter glomeratus", "frozen_label": "Polaribacter glomeratus", "id": "102",
    "rank": "species"}, {"current_id": "1876", "current_name": "Micromonospora sp.",
    "frozen_label": "Micromonospora sp.", "id": "1876", "rank": "species"}, {"current_id":
    "1026", "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum
    furvescens", "id": "1026", "rank": "species"}, {"current_id": "83428", "current_name":
    "uncultured Bacillus sp.", "frozen_label": "uncultured Bacillus sp.", "id": "83428",
    "rank": "species"}, {"current_id": "104268", "current_name": "Tenacibaculum mesophilum",
    "frozen_label": "Tenacibaculum mesophilum", "id": "104268", "rank": "species"},
    {"current_id": "1869227", "current_name": "bacterium", "frozen_label": "bacterium",
    "id": "1869227", "rank": "species"}, {"current_id": "107401", "current_name":
    "Tenacibaculum maritimum", "frozen_label": "Tenacibaculum maritimum", "id": "107401",
    "rank": "species"}, {"current_id": "562", "current_name": "Escherichia coli",
    "frozen_label": "Escherichia coli", "id": "562", "rank": "species"}, {"current_id":
    "111770", "current_name": "Thiothrix fructosivorans", "frozen_label": "Thiothrix
    fructosivorans", "id": "111770", "rank": "species"}, {"current_id": "314275",
    "current_name": "Alteromonas mediterranea", "frozen_label": "Alteromonas mediterranea",
    "id": "314275", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas
    fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank":
    "species"}, {"current_id": "2", "current_name": "Bacteria", "frozen_label": "Bacteria",
    "id": "2", "rank": "domain"}, {"current_id": "1282", "current_name": "Staphylococcus
    epidermidis", "frozen_label": "Staphylococcus epidermidis", "id": "1282", "rank":
    "species"}, {"current_id": "132144", "current_name": "Candidatus Glomeribacter
    gigasporarum", "frozen_label": "Candidatus Glomeribacter gigasporarum", "id":
    "132144", "rank": "species"}, {"current_id": "53249", "current_name": "Pseudoalteromonas
    sp.", "frozen_label": "Pseudoalteromonas sp.", "id": "53249", "rank": "species"},
    {"current_id": "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label":
    "Leisingera methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id":
    "50741", "current_name": "Marinobacter sp.", "frozen_label": "Marinobacter sp.",
    "id": "50741", "rank": "species"}, {"current_id": "13616", "current_name": "Monodelphis
    domestica", "frozen_label": null, "id": "13616", "rank": "species"}, {"current_id":
    "56811", "current_name": "Psychrobacter sp.", "frozen_label": "Psychrobacter sp.",
    "id": "56811", "rank": "species"}, {"current_id": "1371", "current_name": "Marinococcus
    halophilus", "frozen_label": "Marinococcus halophilus", "id": "1371", "rank":
    "species"}, {"current_id": "1211807", "current_name": "Stutzerimonas kunmingensis",
    "frozen_label": "Stutzerimonas kunmingensis", "id": "1211807", "rank": "species"},
    {"current_id": "143223", "current_name": "Salegentibacter salegens", "frozen_label":
    "Salegentibacter salegens", "id": "143223", "rank": "species"}, {"current_id":
    "1871328", "current_name": "Kocuria sp.", "frozen_label": "Kocuria sp.", "id":
    "1871328", "rank": "species"}, {"current_id": "156128", "current_name": "Nephroselmis
    pyriformis", "frozen_label": null, "id": "156128", "rank": "species"}, {"current_id":
    "1931", "current_name": "Streptomyces sp.", "frozen_label": "Streptomyces sp.",
    "id": "1931", "rank": "species"}, {"current_id": "156133", "current_name": "Prasinoderma
    coloniale", "frozen_label": null, "id": "156133", "rank": "species"}, {"current_id":
    "2024855", "current_name": "Rhodopirellula sp.", "frozen_label": "Rhodopirellula
    sp.", "id": "2024855", "rank": "species"}, {"current_id": "141390", "current_name":
    "Chromohalobacter israelensis", "frozen_label": null, "id": "158080", "rank":
    "species"}, {"current_id": "2099376", "current_name": "Desulforhopalus sp.", "frozen_label":
    "Desulforhopalus sp.", "id": "2099376", "rank": "species"}, {"current_id": "158500",
    "current_name": "Novosphingobium resinovorum", "frozen_label": "Novosphingobium
    resinovorum", "id": "158500", "rank": "species"}, {"current_id": "2213", "current_name":
    "Methanosarcina sp.", "frozen_label": "Methanosarcina sp.", "id": "2213", "rank":
    "species"}, {"current_id": "168275", "current_name": "Psychromonas arctica", "frozen_label":
    "Psychromonas arctica", "id": "168275", "rank": "species"}, {"current_id": "265606",
    "current_name": "Rhodopirellula baltica", "frozen_label": "Rhodopirellula baltica",
    "id": "265606", "rank": "species"}, {"current_id": "173365", "current_name": "Methylobacter
    tundripaludum", "frozen_label": "Methylobacter tundripaludum", "id": "173365",
    "rank": "species"}, {"current_id": "2926447", "current_name": "Marinispora", "frozen_label":
    "Marinispora", "id": "2926447", "rank": "genus"}, {"current_id": "44751", "current_name":
    "Exiguobacterium sp.", "frozen_label": "Exiguobacterium sp.", "id": "44751", "rank":
    "species"}, {"current_id": "51671", "current_name": "Microbacterium sp.", "frozen_label":
    "Microbacterium sp.", "id": "51671", "rank": "species"}, {"current_id": "186022",
    "current_name": "Thalassionema frauenfeldii", "frozen_label": "Thalassionema frauenfeldii",
    "id": "186022", "rank": "species"}, {"current_id": "885", "current_name": "Desulfovibrio
    sp.", "frozen_label": "Desulfovibrio sp.", "id": "885", "rank": "species"}, {"current_id":
    "188908", "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica",
    "id": "188908", "rank": "species"}, {"current_id": "1042", "current_name": "Erythrobacter
    sp.", "frozen_label": "Erythrobacter sp.", "id": "1042", "rank": "species"}, {"current_id":
    "190308", "current_name": "Shewanella schlegeliana", "frozen_label": "Shewanella
    schlegeliana", "id": "190308", "rank": "species"}, {"current_id": "1486246", "current_name":
    "Halomonas sp.", "frozen_label": "Halomonas sp.", "id": "1486246", "rank": "species"},
    {"current_id": "191302", "current_name": "Devosia neptuniae", "frozen_label":
    "Devosia neptuniae", "id": "191302", "rank": "species"}, {"current_id": "1703256",
    "current_name": "Pseudoalteromonas gelatinilytica", "frozen_label": "Pseudoalteromonas
    gelatinilytica", "id": "1703256", "rank": "species"}]. Alias/name resolution does
    not establish habitat occurrence.'
  accessed_at: '2026-10-12T05:21:31.882540Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: 47eba2c6c7ff47d6263796c3afdcff6e39319e77b443b6200d469773ef5ff403
- evidence_id: TAX1
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1872627%2C1876%2C188906%2C188908%2C1903071%2C190308%2C191302%2C1926630%2C1931%2C195064%2C1961642%2C197222%2C198804%2C2%2C200617%2C2022602%2C2024855%2C203122%2C203907%2C205920%2C2099376%2C212050%2C214688%2C214988%2C216432%2C216773%2C2183988%2C2213%2C223788%2C224915%2C225345%2C225937%2C226126%2C2264%2C234267%2C240016%2C2423%2C243090%2C247026%2C257363%2C264%2C264462%2C264951%2C265606%2C266940%2C2738566%2C28108%2C28122%2C28181%2C28223%2C28251%2C28258%2C28262%2C29158%2C29159%2C2926447%2C29292%2C293614%2C29805%2C302409%2C3055%2C3068%2C31330%2C313595%2C313603%2C313606%2C314230%2C314275%2C316279%2C319225%2C320388%2C332415%2C337701%2C339861%2C340047%2C34085%2C344747%2C357244%2C35743%2C35845%2C358766%2C361576%2C36870%2C36987%2C372461%2C378806%2C379066%2C39152%2C391625%2C39947%2C402880%2C40464%2C406538%2C406540%2C411477%2C411485%2C419481%2C425006%2C428125%2C435805%2C43928%2C442956%2C443152%2C445336%2C44751%2C45351%2C457427%2C463619%2C46539%2C466153%2C46687%2C46704%2C46745%2C472759%2C483407%2C483417%2C48499%2C48729%2C491952%2C49447%2C498761%2C502025%2C504472%2C50741%2C515618%2C51671%2C518766%2C523849%2C530564%2C53249%2C537937%2C53953%2C55518%2C555512%2C55567%2C562%2C563043%2C56780%2C56811%2C57043%2C575540%2C583355%2C585501%2C595452%2C595453%2C59919%2C59920%2C6047%2C60480%2C6087&retmode=xml
  summary: 'The three chunks jointly resolve all 346 requested cohort IDs. Target
    results=[{"current_id": "28108", "current_name": "Alteromonas macleodii", "frozen_label":
    "Alteromonas macleodii", "id": "28108", "rank": "species"}, {"current_id": "172371",
    "current_name": "Alloalcanivorax venustensis", "frozen_label": "Alloalcanivorax
    venustensis", "id": "172371", "rank": "species"}, {"current_id": "28258", "current_name":
    "Cobetia marina", "frozen_label": "Cobetia marina", "id": "28258", "rank": "species"},
    {"current_id": "180542", "current_name": "Salinisphaera shabanensis", "frozen_label":
    "Salinisphaera shabanensis", "id": "180542", "rank": "species"}, {"current_id":
    "184914", "current_name": "Corallococcus coralloides", "frozen_label": "Corallococcus
    coralloides", "id": "184914", "rank": "species"}, {"current_id": "102", "current_name":
    "Polaribacter glomeratus", "frozen_label": "Polaribacter glomeratus", "id": "102",
    "rank": "species"}, {"current_id": "1876", "current_name": "Micromonospora sp.",
    "frozen_label": "Micromonospora sp.", "id": "1876", "rank": "species"}, {"current_id":
    "1026", "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum
    furvescens", "id": "1026", "rank": "species"}, {"current_id": "83428", "current_name":
    "uncultured Bacillus sp.", "frozen_label": "uncultured Bacillus sp.", "id": "83428",
    "rank": "species"}, {"current_id": "104268", "current_name": "Tenacibaculum mesophilum",
    "frozen_label": "Tenacibaculum mesophilum", "id": "104268", "rank": "species"},
    {"current_id": "1869227", "current_name": "bacterium", "frozen_label": "bacterium",
    "id": "1869227", "rank": "species"}, {"current_id": "107401", "current_name":
    "Tenacibaculum maritimum", "frozen_label": "Tenacibaculum maritimum", "id": "107401",
    "rank": "species"}, {"current_id": "562", "current_name": "Escherichia coli",
    "frozen_label": "Escherichia coli", "id": "562", "rank": "species"}, {"current_id":
    "111770", "current_name": "Thiothrix fructosivorans", "frozen_label": "Thiothrix
    fructosivorans", "id": "111770", "rank": "species"}, {"current_id": "314275",
    "current_name": "Alteromonas mediterranea", "frozen_label": "Alteromonas mediterranea",
    "id": "314275", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas
    fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank":
    "species"}, {"current_id": "2", "current_name": "Bacteria", "frozen_label": "Bacteria",
    "id": "2", "rank": "domain"}, {"current_id": "1282", "current_name": "Staphylococcus
    epidermidis", "frozen_label": "Staphylococcus epidermidis", "id": "1282", "rank":
    "species"}, {"current_id": "132144", "current_name": "Candidatus Glomeribacter
    gigasporarum", "frozen_label": "Candidatus Glomeribacter gigasporarum", "id":
    "132144", "rank": "species"}, {"current_id": "53249", "current_name": "Pseudoalteromonas
    sp.", "frozen_label": "Pseudoalteromonas sp.", "id": "53249", "rank": "species"},
    {"current_id": "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label":
    "Leisingera methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id":
    "50741", "current_name": "Marinobacter sp.", "frozen_label": "Marinobacter sp.",
    "id": "50741", "rank": "species"}, {"current_id": "13616", "current_name": "Monodelphis
    domestica", "frozen_label": null, "id": "13616", "rank": "species"}, {"current_id":
    "56811", "current_name": "Psychrobacter sp.", "frozen_label": "Psychrobacter sp.",
    "id": "56811", "rank": "species"}, {"current_id": "1371", "current_name": "Marinococcus
    halophilus", "frozen_label": "Marinococcus halophilus", "id": "1371", "rank":
    "species"}, {"current_id": "1211807", "current_name": "Stutzerimonas kunmingensis",
    "frozen_label": "Stutzerimonas kunmingensis", "id": "1211807", "rank": "species"},
    {"current_id": "143223", "current_name": "Salegentibacter salegens", "frozen_label":
    "Salegentibacter salegens", "id": "143223", "rank": "species"}, {"current_id":
    "1871328", "current_name": "Kocuria sp.", "frozen_label": "Kocuria sp.", "id":
    "1871328", "rank": "species"}, {"current_id": "156128", "current_name": "Nephroselmis
    pyriformis", "frozen_label": null, "id": "156128", "rank": "species"}, {"current_id":
    "1931", "current_name": "Streptomyces sp.", "frozen_label": "Streptomyces sp.",
    "id": "1931", "rank": "species"}, {"current_id": "156133", "current_name": "Prasinoderma
    coloniale", "frozen_label": null, "id": "156133", "rank": "species"}, {"current_id":
    "2024855", "current_name": "Rhodopirellula sp.", "frozen_label": "Rhodopirellula
    sp.", "id": "2024855", "rank": "species"}, {"current_id": "141390", "current_name":
    "Chromohalobacter israelensis", "frozen_label": null, "id": "158080", "rank":
    "species"}, {"current_id": "2099376", "current_name": "Desulforhopalus sp.", "frozen_label":
    "Desulforhopalus sp.", "id": "2099376", "rank": "species"}, {"current_id": "158500",
    "current_name": "Novosphingobium resinovorum", "frozen_label": "Novosphingobium
    resinovorum", "id": "158500", "rank": "species"}, {"current_id": "2213", "current_name":
    "Methanosarcina sp.", "frozen_label": "Methanosarcina sp.", "id": "2213", "rank":
    "species"}, {"current_id": "168275", "current_name": "Psychromonas arctica", "frozen_label":
    "Psychromonas arctica", "id": "168275", "rank": "species"}, {"current_id": "265606",
    "current_name": "Rhodopirellula baltica", "frozen_label": "Rhodopirellula baltica",
    "id": "265606", "rank": "species"}, {"current_id": "173365", "current_name": "Methylobacter
    tundripaludum", "frozen_label": "Methylobacter tundripaludum", "id": "173365",
    "rank": "species"}, {"current_id": "2926447", "current_name": "Marinispora", "frozen_label":
    "Marinispora", "id": "2926447", "rank": "genus"}, {"current_id": "44751", "current_name":
    "Exiguobacterium sp.", "frozen_label": "Exiguobacterium sp.", "id": "44751", "rank":
    "species"}, {"current_id": "51671", "current_name": "Microbacterium sp.", "frozen_label":
    "Microbacterium sp.", "id": "51671", "rank": "species"}, {"current_id": "186022",
    "current_name": "Thalassionema frauenfeldii", "frozen_label": "Thalassionema frauenfeldii",
    "id": "186022", "rank": "species"}, {"current_id": "885", "current_name": "Desulfovibrio
    sp.", "frozen_label": "Desulfovibrio sp.", "id": "885", "rank": "species"}, {"current_id":
    "188908", "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica",
    "id": "188908", "rank": "species"}, {"current_id": "1042", "current_name": "Erythrobacter
    sp.", "frozen_label": "Erythrobacter sp.", "id": "1042", "rank": "species"}, {"current_id":
    "190308", "current_name": "Shewanella schlegeliana", "frozen_label": "Shewanella
    schlegeliana", "id": "190308", "rank": "species"}, {"current_id": "1486246", "current_name":
    "Halomonas sp.", "frozen_label": "Halomonas sp.", "id": "1486246", "rank": "species"},
    {"current_id": "191302", "current_name": "Devosia neptuniae", "frozen_label":
    "Devosia neptuniae", "id": "191302", "rank": "species"}, {"current_id": "1703256",
    "current_name": "Pseudoalteromonas gelatinilytica", "frozen_label": "Pseudoalteromonas
    gelatinilytica", "id": "1703256", "rank": "species"}]. Alias/name resolution does
    not establish habitat occurrence.'
  accessed_at: '2026-10-12T05:21:33.762356Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: 211e97ebc927aae4966a064aa1db888cc9672558b906b2333d2088bb0c5b87fb
- evidence_id: TAX2
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=610380%2C6182%2C6238%2C6334%2C639602%2C641112%2C6613%2C6669%2C688066%2C69293%2C6945%2C69773%2C7029%2C703612%2C7070%2C7159%2C7209%2C7425%2C74546%2C74547%2C748449%2C756272%2C758583%2C75883%2C760154%2C765912%2C7668%2C76775%2C7719%2C777%2C7955%2C80836%2C8090%2C83428%2C86104%2C880%2C880447%2C885%2C89184%2C9031%2C91360%2C9258%2C939306%2C939316%2C939324%2C939346&retmode=xml
  summary: 'The three chunks jointly resolve all 346 requested cohort IDs. Target
    results=[{"current_id": "28108", "current_name": "Alteromonas macleodii", "frozen_label":
    "Alteromonas macleodii", "id": "28108", "rank": "species"}, {"current_id": "172371",
    "current_name": "Alloalcanivorax venustensis", "frozen_label": "Alloalcanivorax
    venustensis", "id": "172371", "rank": "species"}, {"current_id": "28258", "current_name":
    "Cobetia marina", "frozen_label": "Cobetia marina", "id": "28258", "rank": "species"},
    {"current_id": "180542", "current_name": "Salinisphaera shabanensis", "frozen_label":
    "Salinisphaera shabanensis", "id": "180542", "rank": "species"}, {"current_id":
    "184914", "current_name": "Corallococcus coralloides", "frozen_label": "Corallococcus
    coralloides", "id": "184914", "rank": "species"}, {"current_id": "102", "current_name":
    "Polaribacter glomeratus", "frozen_label": "Polaribacter glomeratus", "id": "102",
    "rank": "species"}, {"current_id": "1876", "current_name": "Micromonospora sp.",
    "frozen_label": "Micromonospora sp.", "id": "1876", "rank": "species"}, {"current_id":
    "1026", "current_name": "Marinoscillum furvescens", "frozen_label": "Marinoscillum
    furvescens", "id": "1026", "rank": "species"}, {"current_id": "83428", "current_name":
    "uncultured Bacillus sp.", "frozen_label": "uncultured Bacillus sp.", "id": "83428",
    "rank": "species"}, {"current_id": "104268", "current_name": "Tenacibaculum mesophilum",
    "frozen_label": "Tenacibaculum mesophilum", "id": "104268", "rank": "species"},
    {"current_id": "1869227", "current_name": "bacterium", "frozen_label": "bacterium",
    "id": "1869227", "rank": "species"}, {"current_id": "107401", "current_name":
    "Tenacibaculum maritimum", "frozen_label": "Tenacibaculum maritimum", "id": "107401",
    "rank": "species"}, {"current_id": "562", "current_name": "Escherichia coli",
    "frozen_label": "Escherichia coli", "id": "562", "rank": "species"}, {"current_id":
    "111770", "current_name": "Thiothrix fructosivorans", "frozen_label": "Thiothrix
    fructosivorans", "id": "111770", "rank": "species"}, {"current_id": "314275",
    "current_name": "Alteromonas mediterranea", "frozen_label": "Alteromonas mediterranea",
    "id": "314275", "rank": "species"}, {"current_id": "114404", "current_name": "Edaphosphingomonas
    fennica", "frozen_label": "Edaphosphingomonas fennica", "id": "114404", "rank":
    "species"}, {"current_id": "2", "current_name": "Bacteria", "frozen_label": "Bacteria",
    "id": "2", "rank": "domain"}, {"current_id": "1282", "current_name": "Staphylococcus
    epidermidis", "frozen_label": "Staphylococcus epidermidis", "id": "1282", "rank":
    "species"}, {"current_id": "132144", "current_name": "Candidatus Glomeribacter
    gigasporarum", "frozen_label": "Candidatus Glomeribacter gigasporarum", "id":
    "132144", "rank": "species"}, {"current_id": "53249", "current_name": "Pseudoalteromonas
    sp.", "frozen_label": "Pseudoalteromonas sp.", "id": "53249", "rank": "species"},
    {"current_id": "133924", "current_name": "Leisingera methylohalidivorans", "frozen_label":
    "Leisingera methylohalidivorans", "id": "133924", "rank": "species"}, {"current_id":
    "50741", "current_name": "Marinobacter sp.", "frozen_label": "Marinobacter sp.",
    "id": "50741", "rank": "species"}, {"current_id": "13616", "current_name": "Monodelphis
    domestica", "frozen_label": null, "id": "13616", "rank": "species"}, {"current_id":
    "56811", "current_name": "Psychrobacter sp.", "frozen_label": "Psychrobacter sp.",
    "id": "56811", "rank": "species"}, {"current_id": "1371", "current_name": "Marinococcus
    halophilus", "frozen_label": "Marinococcus halophilus", "id": "1371", "rank":
    "species"}, {"current_id": "1211807", "current_name": "Stutzerimonas kunmingensis",
    "frozen_label": "Stutzerimonas kunmingensis", "id": "1211807", "rank": "species"},
    {"current_id": "143223", "current_name": "Salegentibacter salegens", "frozen_label":
    "Salegentibacter salegens", "id": "143223", "rank": "species"}, {"current_id":
    "1871328", "current_name": "Kocuria sp.", "frozen_label": "Kocuria sp.", "id":
    "1871328", "rank": "species"}, {"current_id": "156128", "current_name": "Nephroselmis
    pyriformis", "frozen_label": null, "id": "156128", "rank": "species"}, {"current_id":
    "1931", "current_name": "Streptomyces sp.", "frozen_label": "Streptomyces sp.",
    "id": "1931", "rank": "species"}, {"current_id": "156133", "current_name": "Prasinoderma
    coloniale", "frozen_label": null, "id": "156133", "rank": "species"}, {"current_id":
    "2024855", "current_name": "Rhodopirellula sp.", "frozen_label": "Rhodopirellula
    sp.", "id": "2024855", "rank": "species"}, {"current_id": "141390", "current_name":
    "Chromohalobacter israelensis", "frozen_label": null, "id": "158080", "rank":
    "species"}, {"current_id": "2099376", "current_name": "Desulforhopalus sp.", "frozen_label":
    "Desulforhopalus sp.", "id": "2099376", "rank": "species"}, {"current_id": "158500",
    "current_name": "Novosphingobium resinovorum", "frozen_label": "Novosphingobium
    resinovorum", "id": "158500", "rank": "species"}, {"current_id": "2213", "current_name":
    "Methanosarcina sp.", "frozen_label": "Methanosarcina sp.", "id": "2213", "rank":
    "species"}, {"current_id": "168275", "current_name": "Psychromonas arctica", "frozen_label":
    "Psychromonas arctica", "id": "168275", "rank": "species"}, {"current_id": "265606",
    "current_name": "Rhodopirellula baltica", "frozen_label": "Rhodopirellula baltica",
    "id": "265606", "rank": "species"}, {"current_id": "173365", "current_name": "Methylobacter
    tundripaludum", "frozen_label": "Methylobacter tundripaludum", "id": "173365",
    "rank": "species"}, {"current_id": "2926447", "current_name": "Marinispora", "frozen_label":
    "Marinispora", "id": "2926447", "rank": "genus"}, {"current_id": "44751", "current_name":
    "Exiguobacterium sp.", "frozen_label": "Exiguobacterium sp.", "id": "44751", "rank":
    "species"}, {"current_id": "51671", "current_name": "Microbacterium sp.", "frozen_label":
    "Microbacterium sp.", "id": "51671", "rank": "species"}, {"current_id": "186022",
    "current_name": "Thalassionema frauenfeldii", "frozen_label": "Thalassionema frauenfeldii",
    "id": "186022", "rank": "species"}, {"current_id": "885", "current_name": "Desulfovibrio
    sp.", "frozen_label": "Desulfovibrio sp.", "id": "885", "rank": "species"}, {"current_id":
    "188908", "current_name": "Oleispira antarctica", "frozen_label": "Oleispira antarctica",
    "id": "188908", "rank": "species"}, {"current_id": "1042", "current_name": "Erythrobacter
    sp.", "frozen_label": "Erythrobacter sp.", "id": "1042", "rank": "species"}, {"current_id":
    "190308", "current_name": "Shewanella schlegeliana", "frozen_label": "Shewanella
    schlegeliana", "id": "190308", "rank": "species"}, {"current_id": "1486246", "current_name":
    "Halomonas sp.", "frozen_label": "Halomonas sp.", "id": "1486246", "rank": "species"},
    {"current_id": "191302", "current_name": "Devosia neptuniae", "frozen_label":
    "Devosia neptuniae", "id": "191302", "rank": "species"}, {"current_id": "1703256",
    "current_name": "Pseudoalteromonas gelatinilytica", "frozen_label": "Pseudoalteromonas
    gelatinilytica", "id": "1703256", "rank": "species"}]. Alias/name resolution does
    not establish habitat occurrence.'
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
  accessed_at: '2026-10-12T05:41:00.550099Z'
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
  accessed_at: '2026-10-12T05:41:00.550099Z'
  support: supports
  locator: GitHub CLI inventory retrieved 12-Oct
- evidence_id: GRAPH
  kind: record_content
  reference: curation/causal_graphs/marine_water_body.yaml
  summary: Entire overlay and generated graph read, including all node types, edge
    descriptions, evidence and preserved historical events.
  accessed_at: '2026-10-12T05:41:00.550099Z'
  support: supports
  locator: Current full overlay
- evidence_id: PUMP
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3972885/
  summary: Conditional export and remineralization, with nonsinking and dark-fixation
    alternatives.
  accessed_at: '2026-10-12T05:31:26.144017Z'
  support: supports
  locator: DOI:10.1038/ngeo1921; Introduction/Fig1, Sinking versus buoyant particles,
    Microbial activity in the dark
  snapshot_sha256: 0852441bab8d1ffc77c366781f5efb20257c0ff09fb180dd6d60a4fa1ebfe7da
- evidence_id: ARRIGO
  kind: primary_source
  reference: https://pangea.stanford.edu/research/Oceans/GES205/Arrigo_Nature_Global%20Ocean%20Nutrients.pdf
  summary: Light/resource co-limitation, aerobic breakdown and nonuniform nutrient
    regeneration.
  accessed_at: '2026-10-12T05:30:19.020556Z'
  support: supports
  locator: PMID:16163345; printed pp349-351, Fig2. Author PDF header says nature04158;
    publication metadata identifies this title/author as nature04159. No citation
    was swapped.
  snapshot_sha256: f6fc9293e324af92cb0d3700abd7853740a7f6cde6f131cc6f26368e0129dec7
- evidence_id: NOAA
  kind: primary_source
  reference: https://www.fisheries.noaa.gov/west-coast/science-data/phytoplankton-northwest-us-shelf-ecosystem
  summary: Photosynthesis and biomass account with diverse phytoplankton groups.
  accessed_at: '2026-10-12T05:21:50.480690Z'
  support: supports
  locator: What Are Phytoplankton; What Is Primary Production
  snapshot_sha256: 9e866f51188be43eac8bae92d9795da93c627a608493ff7a28b599acc0b6181e
- evidence_id: ARNOSTI
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21329211+AND+SRC%3AMED&format=json&resultType=core
  summary: Complete abstract supports hydrolysis to uptake-sized substrates and heterotrophic
    carbon processing.
  accessed_at: '2026-10-12T05:21:44.201518Z'
  support: supports
  locator: PMID:21329211; core bibliographic metadata and complete abstract, not full
    text
  snapshot_sha256: b3a177202554a3c4f032bcdb4f7d6604274c40ed65721bff95e7b63e0de58b52
- evidence_id: IMODULONDB
  kind: database
  reference: iModulonDB via kg-microbe-sources
  summary: '{"command": ["../../culturebotai-claw/.venv/bin/kg-microbe-sources", "imodulondb",
    "datasets"], "started_at": "2026-10-12T05:22:18.796436+00:00", "finished_at":
    "2026-10-12T05:22:19.723730+00:00", "exit_code": 0, "path": "/private/tmp/habitatmech-review-bc-imodulondb-datasets.source",
    "sha256": "1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549",
    "stderr": ""}'
  accessed_at: '2026-10-12T05:41:00.550099Z'
  support: supports
  locator: Actual 28-dataset inventory inspected; no covered claim-specific strain/gene
    or expression module in this generic guild graph warrants a search/component query
assessments:
- assessment_id: EDGE-marine_body_contains_euphotic_zone
  area: evidence
  topic: marine_body_contains_euphotic_zone
  outcome: supported
  summary: Herndl Fig1 supports the explicitly oceanic illuminated-water setting,
    not all marine water bodies.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-euphotic_zone_supports_marine_phytoplankton
  area: evidence
  topic: euphotic_zone_supports_marine_phytoplankton
  outcome: supported
  summary: Arrigo pp350-351 supports light/resource dependence and co-limitation.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-phytoplankton_perform_oxygenic_photosynthesis
  area: evidence
  topic: phytoplankton_perform_oxygenic_photosynthesis
  outcome: supported
  summary: NOAA Primary Production supports oxygenic carbon fixation by photosynthetic
    phytoplankton.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-photosynthesis_generates_particulate_carbon
  area: evidence
  topic: photosynthesis_generates_particulate_carbon
  outcome: supported
  summary: NOAA Primary Production supports biomass formation; the edge does not make
    all fixed carbon particulate.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-particulate_carbon_forms_sinking_particles
  area: evidence
  topic: particulate_carbon_forms_sinking_particles
  outcome: supported
  summary: Herndl introduction supports aggregation and detrital sinking, with nonsinking
    particles distinguished.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-sinking_particles_enter_dark_ocean
  area: evidence
  topic: sinking_particles_enter_dark_ocean
  outcome: supported
  summary: Herndl introduction/Fig1 supports export below the euphotic zone.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-sinking_particles_select_particle_bacteria
  area: evidence
  topic: sinking_particles_select_particle_bacteria
  outcome: supported
  summary: Herndl Microbial activity in the dark supports particle-associated activity,
    not selection sufficiency.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-particle_bacteria_express_extracellular_enzymes
  area: evidence
  topic: particle_bacteria_express_extracellular_enzymes
  outcome: supported
  summary: Herndl Microbial activity in the dark describes extracellular-enzyme release
    by particle-associated microbes.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-enzymes_release_dissolved_organic_matter
  area: evidence
  topic: enzymes_release_dissolved_organic_matter
  outcome: supported
  summary: Arnosti complete abstract supports hydrolysis to uptake-sized substrates,
    not a measured leakage flux.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-dissolved_organic_matter_supports_free_living_heterotrophs
  area: evidence
  topic: dissolved_organic_matter_supports_free_living_heterotrophs
  outcome: supported
  summary: Herndl contrasts bioavailable substrates with refractory deep dissolved
    carbon.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-heterotrophs_drive_microbial_remineralization
  area: evidence
  topic: heterotrophs_drive_microbial_remineralization
  outcome: supported
  summary: Arnosti abstract supports heterotrophic organic-matter processing without
    a measured free-living share.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-dark_ocean_hosts_remineralization
  area: evidence
  topic: dark_ocean_hosts_remineralization
  outcome: supported
  summary: Herndl introduction/Fig1 supports remineralization beneath the euphotic
    zone.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-remineralization_consumes_oxygen
  area: evidence
  topic: remineralization_consumes_oxygen
  outcome: supported
  summary: Arrigo Fig2 p351 supports oxygen use; the current edge is explicitly aerobic.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-remineralization_releases_dic
  area: evidence
  topic: remineralization_releases_dic
  outcome: supported
  summary: Herndl introduction/Fig1 supports respiratory conversion to inorganic carbon.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: EDGE-remineralization_regenerates_nutrients
  area: evidence
  topic: remineralization_regenerates_nutrients
  outcome: supported
  summary: Arrigo p349 and Fig2 p351 support nitrogen/phosphorus regeneration without
    a universal ratio.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
- assessment_id: IDENTITY
  area: identity
  topic: Exact identity, definition and source intent
  outcome: supported
  summary: The physical lentic marine water body is not an aquatic biome. Preserve
    BacDive 2040 STRAIN, GOLD 6420 ORGANISM and PREGO 171 TAXON assertions, the two
    CLOSE source mappings and 50 selected associations. The revised 15-edge carbon-pump
    graph is explicitly conditional and its earlier unrelated citation is no longer
    active. Current node types still confuse ecological assemblages, habitats and
    enzyme products with taxa, exposures and a trait.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
- assessment_id: HIERARCHY
  area: grounding
  topic: Parent contributors and mapping endpoints
  outcome: concern
  summary: The physical lentic marine water body is not an aquatic biome. Preserve
    BacDive 2040 STRAIN, GOLD 6420 ORGANISM and PREGO 171 TAXON assertions, the two
    CLOSE source mappings and 50 selected associations. The revised 15-edge carbon-pump
    graph is explicitly conditional and its earlier unrelated citation is no longer
    active. Current node types still confuse ecological assemblages, habitats and
    enzyme products with taxa, exposures and a trait. Ontology, GOLD path, ambiguous-leaf
    and authored-genus routes were distinguished.
  target_ids:
  - ENVO:00001999
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
  summary: 'Complete reconstruction preserves 3 contributing concepts and 3 ITEM-reviewed
    contributors. Attestations=[{"source": "BACDIVE", "source_id": "bacdive.isolation_source:marine",
    "source_label": "Marine", "mapping_predicate": "skos:closeMatch", "assertion_count":
    2040, "assertion_unit": "STRAIN"}, {"source": "GOLD", "source_id": "gold.ecosystem:3487",
    "source_label": "Marine", "source_path": "Environmental > Aquatic > Marine", "mapping_predicate":
    "skos:closeMatch", "assertion_count": 6420, "assertion_unit": "ORGANISM", "notes":
    "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."},
    {"source": "PREGO", "source_id": "ENVO:00001999", "source_label": "marine water
    body", "assertion_count": 171, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels":
    "environmental_samples"}]. Counts with different units are not summed. Reproduction
    validates derivation, not the scientific truth of the mapping.'
  target_ids:
  - ENVO:00001999
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
  - ENVO:00001999
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
  summary: Optional empty fields alone are not defects. Every current graph edge has
    an individual assessment; node typing is assessed separately. Expression-module
    membership is not direct causal proof.
  target_ids:
  - ENVO:00001999
  evidence_ids:
  - R
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: envo-00001999-context-parent
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Source context is emitted as a strict superclass
  description: 'The physical lentic marine water body is not an aquatic biome. Preserve
    BacDive 2040 STRAIN, GOLD 6420 ORGANISM and PREGO 171 TAXON assertions, the two
    CLOSE source mappings and 50 selected associations. The revised 15-edge carbon-pump
    graph is explicitly conditional and its earlier unrelated citation is no longer
    active. Current node types still confuse ecological assemblages, habitats and
    enzyme products with taxa, exposures and a trait. Unsupported GOLD contributions:
    ENVO:00002030.'
  target_ids:
  - ENVO:00001999
  field_paths:
  - parent_habitats
  evidence_ids:
  - R
  - RAW
  - CODE
  - ONT
  - PARENT
  - BULK
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact source-path and expected-parent guards
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material identity, strict-hierarchy, evidence or representation
    defect.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1300
- finding_id: F2
  issue_key: envo-00001999-taxonomy-alias-maintenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical taxonomy identifiers or names need versioned maintenance
  description: 158080 resolves to 141390 Chromohalobacter israelensis. The original
    IDs remain resolvable; this is not proof of a false habitat association.
  target_ids:
  - ENVO:00001999
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
- finding_id: F3
  issue_key: envo-00001999-graph-node-type-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Graph node types misrepresent habitats and functional assemblages
  description: Euphotic zone and dark ocean denote habitats rather than exposures/stressors.
    Phytoplankton, particle-associated bacteria and free-living heterotrophs are ecological
    assemblages, not single taxa. Extracellular enzymes are gene products or catalytic
    activities, not themselves a microbial trait. The previously fixed unrelated PMID
    remains only in preserved history.
  target_ids:
  - ENVO:00001999
  field_paths:
  - causal_graphs[0].nodes
  evidence_ids:
  - GRAPH
  - RULES
  - PUMP
  - ARRIGO
  - NOAA
  - ARNOSTI
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/marine_water_body.yaml
    role: Node type and endpoint definitions
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material identity, strict-hierarchy, evidence or representation
    defect.
actions:
- action_id: A1
  description: Exclude only the specified GOLD contributions, retaining independent
    ontology/curator genera and source provenance. Where source specificity is unresolved,
    assess the source decision separately instead of treating an exclusion as proof
    of exact equivalence.
  finding_ids:
  - F1
  target_ids:
  - ENVO:00001999
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact source-path and expected-parent guards
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained owners after source-level assessment; retain independent
    true parents, source identity/count/unit provenance and lifecycle unless a separately
    justified change requires otherwise.
  - Append required current history, add focused regressions, inspect a seed canary
    and regenerate affected products without hand-editing records or pages.
  - Pass schema, strict, label, provenance, corpus reproduction, causal/history and
    full QC gates; save a linked successor for any finding disposition.
- action_id: A2
  description: Use versioned taxonomy normalization, preserving original IDs/names,
    ranks, scores, source pools and corroboration. Test alias deduplication rather
    than guessing a replacement organism.
  finding_ids:
  - F2
  target_ids:
  - ENVO:00001999
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
- action_id: A3
  description: Use supported HABITAT/COMMUNITY/gene-product or process representations
    as appropriate; do not relabel ecological guilds as clades. Preserve supported
    causal meaning and recheck every affected edge.
  finding_ids:
  - F3
  target_ids:
  - ENVO:00001999
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/marine_water_body.yaml
    role: Node type and endpoint definitions
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
- Full text was read for the explicitly identified full-text items; Arnosti support
  is bounded to the complete abstract. Europe PMC pump XML failed, but PMC HTML full
  text was inspected. PDF text required an isolated reader dependency; repository
  dependencies were not changed.
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
