# Scientific record review: marine_sediment

- Review: 20261012T054255Z-marine_sediment
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-12T05:18:55.657116Z
- Finished UTC: 2026-10-12T05:42:55.442542Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Marine sediment is deposited particulate material, not a whole marine water body. Preserve sediment ancestry, 1035 GOLD ORGANISM assertions, the 837-member Madin taxon pool, 25 displayed associations and seven source-attributed qualitative parameter bands. The 14-edge sulfur graph needs conditional redox scope, claim-specific evidence, correct carbon/sulfur wording and truthful node types; taxonomic aliases also need versioned maintenance.

## Scope And Provenance

Entire exact generated record, all contributors and individual asserted causal edges, with bounded source-context assessment.

Selection: Next forty records without a completed individual scientific review in stable repository-relative path order: marine anoxic zone through microbial_mats__200e1828. Full individual observations, not a category-wide pass. Prior coverage counts distinct observations, not a clean current-input corpus. Starting distinct-review coverage 688/3208 is not clean current-input coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ed9e0d0f382e4502a64f4de10102c4512bddca38.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:03000033 | data/habitats/aquatic/marine_sediment.yaml | generated | marine sediment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native gate on captured inputs | passed | True | ENVO:03000033 | Actual success 2026-10-12T05:22:08.341299Z to 2026-10-12T05:22:11.391220Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:03000033 | Actual success 2026-10-12T05:23:16.222412Z to 2026-10-12T05:23:26.347203Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:03000033 | Actual success 2026-10-12T05:23:26.348469Z to 2026-10-12T05:23:51.098950Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:03000033 | Actual success 2026-10-12T05:23:51.100146Z to 2026-10-12T05:25:01.530644Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:03000033 | Actual success 2026-10-12T05:25:01.532072Z to 2026-10-12T05:25:11.808379Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:03000033 | Actual success 2026-10-12T05:25:11.809657Z to 2026-10-12T05:25:19.058687Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:03000033 | Actual success 2026-10-12T05:25:19.059693Z to 2026-10-12T05:25:46.351294Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | ENVO:03000033 | Actual success 2026-10-12T05:25:46.352569Z to 2026-10-12T05:25:47.389752Z. Native command scope retained. |
| Exact-base CI authoritative QC | passed | True | ENVO:03000033 | Actual success 2026-10-12T05:21:53.294030Z to 2026-10-12T05:21:55.368917Z. All three required merge-group workflows passed at the exact captured base; authoritative QC passed 913 tests with 3 skipped. Newly saved review bundles require their own integrity check. These newly saved review bundles were not part of that earlier exact-base CI run. |
| Complete target reconstruction | passed | False | ENVO:03000033 | All 40 complete documents matched; captured hashes rechecked before authoring. |
| Original assertion membership | unavailable | False | ENVO:03000033 | Bounded ignored-inclusive searches did not recover complete original assertion inputs; later exports are contextual evidence only. |
| Expression-adapter applicability | not_applicable | False | ENVO:03000033 | The successful 28-dataset inventory was read for graph scope. No matching claim-specific organism/strain/gene or expression-module assertion requires a search or summarize call. Absence is not negative ecological evidence. |

## Scientific And Domain Assessments

### marine_sediment_receives_particles

evidence: supported. Targets: ENVO:03000033.

Deposition and burial context are supported by D'Hondt introduction and Box1; no universal anoxia follows.

### particles_bury_marine_organic_matter

evidence: supported. Targets: ENVO:03000033.

D'Hondt introduction and Box1 support organic-particle burial; this is not the fate of every particle.

### buried_organic_matter_depletes_oxygen

evidence: supported. Targets: ENVO:03000033.

Jorgensen introduction supports aerobic carbon oxidation as an oxygen sink; depletion depends on supply.

### oxygen_depletion_creates_anoxic_porewater

evidence: concern. Targets: ENVO:03000033.

D'Hondt introduction/Fig1 expressly includes fully oxic sediment columns; rapid universal depletion is contradicted.

### seawater_supplies_sulfate

evidence: supported. Targets: ENVO:03000033.

Jorgensen Organic Matter Degradation describes sulfate transport from overlying seawater.

### sulfate_selects_sulfate_reducers

evidence: supported. Targets: ENVO:03000033.

Wasmund introduction/Sulfate-Reducing Microorganisms supports sulfate-respiring guilds, with donor and temperature dependence.

### anoxic_porewater_enables_sulfate_reduction

evidence: concern. Targets: ENVO:03000033.

Nagakura concerns Guaymas sediments; D'Hondt Box1 and Jorgensen zonation discussion contradict strict mutual exclusion.

### sulfate_reducers_perform_sulfate_reduction

evidence: supported. Targets: ENVO:03000033.

Wasmund Sulfate-Reducing Microorganisms supports coupled substrate oxidation and sulfate respiration; hydrogen is another donor.

### sulfate_reduction_mineralizes_carbon

evidence: supported. Targets: ENVO:03000033.

Jorgensen introduction describes coupled organic-carbon oxidation and sulfate reduction; carbon becomes inorganic carbon, not sulfide.

### sulfate_reduction_produces_sulfide

evidence: concern. Targets: ENVO:03000033.

Wasmund introduction supports sulfate-to-sulfide conversion, but the supplied snippet is absent from whitespace-normalized complete XML.

### sulfide_selects_sulfur_oxidizers

evidence: supported. Targets: ENVO:03000033.

Jorgensen introduction/Fig1 supports conditional sulfide oxidation with oxidants; it is not a quantified selection experiment.

### sulfur_oxidizers_perform_sulfide_oxidation

evidence: supported. Targets: ENVO:03000033.

Wasmund introduction and sulfur-oxidizer account support biological sulfur oxidation without assigning all flux to microbes.

### reactive_iron_traps_sulfide

evidence: concern. Targets: ENVO:03000033.

Lin Results3.2/Discussion concern mineral surfaces and sulfate-reduction rates, not this trapping reaction; Jorgensen introduction supports the chemistry.

### sulfide_reaction_forms_iron_sulfides

evidence: supported. Targets: ENVO:03000033.

Jorgensen introduction/Fig1 supports precipitation of reduced sulfur with iron; other sulfide fates remain possible.

### Exact identity, definition and source intent

identity: supported. Targets: ENVO:03000033.

Marine sediment is deposited particulate material, not a whole marine water body. Preserve sediment ancestry, 1035 GOLD ORGANISM assertions, the 837-member Madin taxon pool, 25 displayed associations and seven source-attributed qualitative parameter bands. The 14-edge sulfur graph needs conditional redox scope, claim-specific evidence, correct carbon/sulfur wording and truthful node types; taxonomic aliases also need versioned maintenance.

### Parent contributors and mapping endpoints

grounding: concern. Targets: ENVO:03000033.

Marine sediment is deposited particulate material, not a whole marine water body. Preserve sediment ancestry, 1035 GOLD ORGANISM assertions, the 837-member Madin taxon pool, 25 displayed associations and seven source-attributed qualitative parameter bands. The 14-edge sulfur graph needs conditional redox scope, claim-specific evidence, correct carbon/sulfur wording and truthful node types; taxonomic aliases also need versioned maintenance. Ontology, GOLD path, ambiguous-leaf and authored-genus routes were distinguished.

### Source units and native lifecycle

provenance: supported. Targets: ENVO:03000033.

Complete reconstruction preserves 3 contributing concepts and 0 ITEM-reviewed contributors. Attestations=[{"source": "ENVIRONMENTS_TABLE", "source_id": "sediment_marine", "source_label": "sediment_marine", "notes": "Physicochemical parameter bands from kg-microbe's environment table."}, {"source": "GOLD", "source_id": "gold.ecosystem:4563", "source_label": "Sediment", "source_path": "Environmental &gt; Aquatic &gt; Marine &gt; Sediment", "mapping_predicate": "skos:exactMatch", "assertion_count": 1035, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "MADIN", "source_id": "ENVO:03000033", "source_label": "marine sediment", "assertion_count": 837, "assertion_unit": "TAXON"}]. Counts with different units are not summed. Reproduction validates derivation, not the scientific truth of the mapping.

### Taxonomy and association scope

evidence: concern. Targets: ENVO:03000033.

All emitted identifiers resolve, including historical aliases. Source rows, ranks, scores and corroboration reproduce; these are selected associations, not proven characteristic taxa. Original occurrence evidence was not fully recovered, so no claim of exhaustive ecological validation is made. 1017277 resolves to 296995 Exiguobacterium indicum; six historical name combinations have current synonyms and five further labels differ only in formatting

### Qualitative bands and triad roles

evidence: supported. Targets: ENVO:03000033.

All 7 source-attributed single-term parameter bands reproduce. These qualitative descriptors are not universal measurements; multi-term rows are not applied to only one component. MIxS broad/local/medium context is not automatically identity.

### Optional slots and bounded evidence

completeness: supported. Targets: ENVO:03000033.

Optional empty fields alone are not defects. Every current graph edge has an individual assessment; node typing is assessed separately. Expression-module membership is not direct causal proof.

## Findings

### F1: Source context is emitted as a strict superclass

major / open / confirmed; issue key: envo-03000033-context-parent.

Marine sediment is deposited particulate material, not a whole marine water body. Preserve sediment ancestry, 1035 GOLD ORGANISM assertions, the 837-member Madin taxon pool, 25 displayed associations and seven source-attributed qualitative parameter bands. The 14-edge sulfur graph needs conditional redox scope, claim-specific evidence, correct carbon/sulfur wording and truthful node types; taxonomic aliases also need versioned maintenance. Unsupported GOLD contributions: ENVO:00001999.

### F2: Historical taxonomy identifiers or names need versioned maintenance

minor / open / confirmed; issue key: envo-03000033-taxonomy-alias-maintenance.

1017277 resolves to 296995 Exiguobacterium indicum; six historical name combinations have current synonyms and five further labels differ only in formatting. The original IDs remain resolvable; this is not proof of a false habitat association.

### F3: The sulfur graph overgeneralizes redox scope and misplaces evidence

major / open / confirmed; issue key: envo-03000033-sulfur-graph-scope-evidence.

Rapid anoxia and exhaustion of all higher-energy acceptors are overgeneralized. The graph summary confuses carbon oxidation with sulfate reduction to sulfide. Lin supports clay-linked rate effects, not iron-mineral trapping. One Wasmund snippet is absent from complete normalized XML; other title/topic fragments do not identify claim-bearing passages.

### F4: Graph node types misrepresent habitats and functional assemblages

major / open / confirmed; issue key: envo-03000033-graph-node-type-scope.

Anoxic porewater is external habitat context, not a cellular STATE. Sulfate-reducing and sulfur-oxidizing assemblages are polyphyletic functional guilds, not one organism or clade as TAXON requires.

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

Qualify the anoxic pathway, distinguish carbon and sulfur fates, replace unsupported trapping evidence with an inspected relevant source, and use exact short excerpts or precise locators. Preserve supported conditional mechanisms and stable IDs where possible.

- Change only maintained owners after source-level assessment; retain independent true parents, source identity/count/unit provenance and lifecycle unless a separately justified change requires otherwise.
- Append required current history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, label, provenance, corpus reproduction, causal/history and full QC gates; save a linked successor for any finding disposition.

### A4

Use supported HABITAT/COMMUNITY/gene-product or process representations as appropriate; do not relabel ecological guilds as clades. Preserve supported causal meaning and recheck every affected edge.

- Change only maintained owners after source-level assessment; retain independent true parents, source identity/count/unit provenance and lifecycle unless a separately justified change requires otherwise.
- Append required current history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, label, provenance, corpus reproduction, causal/history and full QC gates; save a linked successor for any finding disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/aquatic/marine_sediment.yaml; Entire captured YAML read, including all taxa, parameters, graphs and generated history | supports | Marine sediment is deposited particulate material, not a whole marine water body. Preserve sediment ancestry, 1035 GOLD ORGANISM assertions, the 837-member Madin taxon pool, 25 displayed associations and seven source-attributed qualitative parameter bands. The 14-edge sulfur graph needs conditional redox scope, claim-specific evidence, correct carbon/sulfur wording and truthful node types; taxonomic aliases also need versioned maintenance. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied exact identity, strict-genus, MIxS roles, source-unit/score and ITEM lifecycle contracts; graph node types retain their biological definitions. |
| RAW | data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; Exact logical TSV rows, header=row1; filtered by current source IDs and exact paths, not legacy issue line numbers | supports | {"data/raw/environment_parameters.tsv": [{"data": {"cobo_simon_habitat": "marine", "env_type": "sediment_marine", "main_group": "Aquatic", "parameter": "Salinity", "term_ids": "ENVO:03000033", "term_labels": "marine sediment", "value": "high"}, "logical_row": 95}, {"data": {"cobo_simon_habitat": "marine", "env_type": "sediment_marine", "main_group": "Aquatic", "parameter": "Structural", "term_ids": "ENVO:03000033", "term_labels": "marine sediment", "value": "medium"}, "logical_row": 96}, {"data": {"cobo_simon_habitat": "marine", "env_type": "sediment_marine", "main_group": "Aquatic", "parameter": "Water", "term_ids": "ENVO:03000033", "term_labels": "marine sediment", "value": "high"}, "logical_row": 97}, {"data": {"cobo_simon_habitat": "marine", "env_type": "sediment_marine", "main_group": "Aquatic", "parameter": "pH", "term_ids": "ENVO:03000033", "term_labels": "marine sediment", "value": "high"}, "logical_row": 98}, {"data": {"cobo_simon_habitat": "marine", "env_type": "sediment_marine", "main_group": "Aquatic", "parameter": "salinity variability", "term_ids": "ENVO:03000033", "term_labels": "marine sediment", "value": "small"}, "logical_row": 99}, {"data": {"cobo_simon_habitat": "marine", "env_type": "sediment_marine", "main_group": "Aquatic", "parameter": "temp variability", "term_ids": "ENVO:03000033", "term_labels": "marine sediment", "value": "low"}, "logical_row": 100}, {"data": {"cobo_simon_habitat": "marine", "env_type": "sediment_marine", "main_group": "Aquatic", "parameter": "water variability", "term_ids": "ENVO:03000033", "term_labels": "marine sediment", "value": "permanently wet"}, "logical_row": 101}], "data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Environmental &gt; Aquatic &gt; Marine &gt; Sediment", "depth": "4", "ecosystem": "Environmental", "ecosystem_category": "Aquatic", "ecosystem_subtype": "Sediment", "ecosystem_type": "Marine", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:4563&#124;gold.ecosystem:4564", "leaf_label": "Sediment", "organism_count": "1035", "specific_ecosystem": "", "study_count": "0", "total_assertions": "1035"}, "logical_row": 39}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "533", "canonical_path": "Environmental &gt; Aquatic &gt; Marine &gt; Sediment", "ecosystem_path_id": "4564"}, "logical_row": 66}], "data/raw/gold_path_triads.tsv": [{"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Marine &gt; Sediment", "distinct_terms": "3", "samples": "286", "slot": "broad", "studies": "40", "studies_agreeing": "38", "top_label": "marine benthic biome", "top_share": "0.92", "top_term": "ENVO:01000024"}, "logical_row": 665}, {"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Marine &gt; Sediment", "distinct_terms": "3", "samples": "286", "slot": "local", "studies": "40", "studies_agreeing": "37", "top_label": "marine benthic feature", "top_share": "0.92", "top_term": "ENVO:01000105"}, "logical_row": 666}, {"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Marine &gt; Sediment", "distinct_terms": "2", "samples": "286", "slot": "medium", "studies": "40", "studies_agreeing": "39", "top_label": "marine sediment", "top_share": "0.93", "top_term": "ENVO:03000033"}, "logical_row": 667}], "data/raw/madin_habitat_taxa.tsv": [{"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1003110", "taxon_label": "verrucosispora_maris"}, "logical_row": 997}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1005925", "taxon_label": "Kordiimonas aestuarii"}, "logical_row": 998}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1005926", "taxon_label": "Muricauda taeanensis"}, "logical_row": 999}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1005928", "taxon_label": "roseovarius_lutimaris"}, "logical_row": 1000}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1006", "taxon_label": "flexibacter_tractuosus"}, "logical_row": 1001}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1007105", "taxon_label": "Pusillimonas sp. T7-7"}, "logical_row": 1002}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1017277", "taxon_label": "exiguobacterium_enclense"}, "logical_row": 1003}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1027373", "taxon_label": "Nitrosopumilus sp. AR"}, "logical_row": 1004}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1027374", "taxon_label": "Nitrosopumilus sp. SJ"}, "logical_row": 1005}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028566", "taxon_label": "Sulfolobus acidocaldarius N8"}, "logical_row": 1006}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028742", "taxon_label": "Altererythrobacter gangjinensis"}, "logical_row": 1007}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028743", "taxon_label": "Arenibacter hampyeongensis"}, "logical_row": 1008}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028745", "taxon_label": "Aestuariibaculum suncheonense"}, "logical_row": 1009}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028746", "taxon_label": "Gramella aestuarii"}, "logical_row": 1010}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028749", "taxon_label": "Microbulbifer gwangyangensis"}, "logical_row": 1011}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028752", "taxon_label": "Shewanella aestuarii"}, "logical_row": 1012}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1031273", "taxon_label": "Gaetbulibacter lutimaris"}, "logical_row": 1013}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1031541", "taxon_label": "tropicimonas_sediminicola"}, "logical_row": 1014}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1038845", "taxon_label": "flavobacterium_rakeshii"}, "logical_row": 1015}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1038928", "taxon_label": "streptomyces_xinghaiensis"}, "logical_row": 1016}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1038929", "taxon_label": "Streptomyces xinghaiensis S187"}, "logical_row": 1017}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1042877", "taxon_label": "Thermococcus sp. 4557"}, "logical_row": 1018}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1045558", "taxon_label": "Neptunomonas qingdaonensis"}, "logical_row": 1019}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1048", "taxon_label": "marichromatium_gracile"}, "logical_row": 1020}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1048221", "taxon_label": "Mucilaginibacter litoreus"}, "logical_row": 1021}], "data/raw/madin_habitats.tsv": [{"data": {"label": "marine sediment", "madin_id": "ENVO:03000033", "taxon_count": "837", "vocabulary": "ENVO"}, "logical_row": 10}], "data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:00002007", "predicate": "rdfs:subClassOf", "subject": "ENVO:03000033"}, "logical_row": 7974}], "data/raw/ontology_terms.tsv": [{"data": {"definition": "Sediment which has been transported through the marine water column, settling on the seafloor.", "deprecated": "", "directly_referenced": "TRUE", "label": "marine sediment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "marine sediments", "term_id": "ENVO:03000033"}, "logical_row": 9583}]} |
| CODE | src/habitatmech/seed.py; Executed complete-document reconstruction; all 40 matched; routes distinguish source mints and generated identity | supports | {"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:03000033", "mapping_predicate": null, "reviewed": false, "route": "environments_table_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:03000033", "mapping_predicate": null, "reviewed": false, "route": "environments_table_self_grounded"}, "minted": "habitatmech:ENVIRONMENTS_TABLE.712afe5b2b", "source": "ENVIRONMENTS_TABLE", "source_id": "sediment_marine"}, {"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:03000033", "mapping_predicate": "skos:exactMatch", "reviewed": false, "route": "gold_composed_label"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:03000033", "mapping_predicate": "skos:exactMatch", "reviewed": false, "route": "gold_composed_label"}, "minted": "habitatmech:GOLD.da51ff29f9", "source": "GOLD", "source_id": "gold.ecosystem:4563"}, {"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:03000033", "mapping_predicate": null, "reviewed": false, "route": "madin_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:03000033", "mapping_predicate": null, "reviewed": false, "route": "madin_self_grounded"}, "minted": "habitatmech:MADIN.b94291a1ab", "source": "MADIN", "source_id": "ENVO:03000033"}], "source_concepts": 3} |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Official OWL retrieved 12-Oct; labels, definitions, typed synonyms, named parents and restrictions; no snapshot refresh | supports | {"ENVO:00000063": {"definitions": ["An accumulation of water of varying size."], "deprecated": [], "equivalents": [], "labels": ["water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000685", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000819"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002354"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01001220"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_15377"]}], "replacements": [], "synonyms": {"hasBroadSynonym": ["hydrographic feature"], "hasExactSynonym": ["aquatic feature", "bodies of water", "body of water", "waterbody"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00000428": {"definitions": ["A biome is an ecosystem which is undergoing climactic ecological succession."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_01001110"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000056"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01001827"]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["biome"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000813", "http://purl.obolibrary.org/obo/ENVO_01001110", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000817"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PCO_0000002"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000056"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01001827"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002507"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PCO_0000002"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["major habitat type"], "hasNarrowSynonym": [], "hasRelatedSynonym": ["EcosytemType"]}}, "ENVO:00001999": {"definitions": ["A lentic water body which is composed primarily of marine water."], "deprecated": [], "equivalents": [], "labels": ["marine water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000617"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["body of marine water", "marine waterbody"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002007": {"definitions": ["Particulate environmental material which is formed as a result of the transport and deposition of particles by flowing liquid."], "deprecated": [], "equivalents": [], "labels": ["sediment"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000060", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000086"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PATO_0000984"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002030": {"definitions": ["A biome which is determined by a water body and which has ecological climax communities adapted to life in or on water."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00000428"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002507"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00000063"]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["aquatic biome"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000428", "http://purl.obolibrary.org/obo/ENVO_01001787"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:01000254": {"definitions": ["A system which has the disposition to environ one or more material entities."], "deprecated": [], "equivalents": [], "labels": ["environmental system"], "parents": ["http://purl.obolibrary.org/obo/RO_0002577"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["environment"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:01000617": {"definitions": ["A lentic water body is a water body in which the accumulated water, in its totality, has very little to no directed flow."], "deprecated": [], "equivalents": [], "labels": ["lentic water body"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000063"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:03000033": {"definitions": ["Sediment which has been transported through the marine water column, settling on the seafloor."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#unionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002007"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"nested": true}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002007"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"nested": true}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["marine sediment"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002007", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002220"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00001999"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002353"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_03000036"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["marine sediments"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}} |
| PARENT | data/habitats/terrestrial/sediment.yaml; data/habitats/aquatic/marine_water_body.yaml; data/habitats/aquatic/lentic_water_body.yaml; data/habitats/aquatic/water_body.yaml; data/habitats/aquatic/aquatic_biome.yaml; data/habitats/other/environmental.yaml; data/habitats/other/environmental_system.yaml; data/habitats/other/biome.yaml; Ancestor context adds no full-record coverage | supports | {"ENVO:00000063": {"definition": "An accumulation of water of varying size.", "grounding_status": "EXACT", "label": "water body", "parent_habitats": ["ENVO:01000685"]}, "ENVO:00000428": {"definition": "A biome is an ecosystem which is undergoing climactic ecological succession.", "grounding_status": "EXACT", "label": "biome", "parent_habitats": ["ENVO:01000813", "ENVO:01001110"]}, "ENVO:00001999": {"definition": "A lentic water body which is composed primarily of marine water.", "grounding_status": "EXACT", "label": "marine water body", "parent_habitats": ["ENVO:00002030", "ENVO:01000617"]}, "ENVO:00002007": {"definition": "Particulate environmental material which is formed as a result of the transport and deposition of particles by flowing liquid.", "grounding_status": "EXACT", "label": "sediment", "parent_habitats": ["ENVO:01000060"]}, "ENVO:00002030": {"definition": "A biome which is determined by a water body and which has ecological climax communities adapted to life in or on water.", "grounding_status": "EXACT", "label": "aquatic biome", "parent_habitats": ["ENVO:00000428", "ENVO:01001787", "habitatmech:BACDIVE.0f1e92a02c"]}, "ENVO:01000254": {"definition": "A system which has the disposition to environ one or more material entities.", "grounding_status": "EXACT", "label": "environmental system", "parent_habitats": null}, "ENVO:01000617": {"definition": "A lentic water body is a water body in which the accumulated water, in its totality, has very little to no directed flow.", "grounding_status": "EXACT", "label": "lentic water body", "parent_habitats": ["ENVO:00000063"]}, "habitatmech:BACDIVE.0f1e92a02c": {"definition": "An environmental system which is a portion of the air, water, or land surface or subsurface of an astronomical body sampled in place, and which is neither bounded by a host organism nor constituted by a constructed or operated artefact.", "grounding_status": "UNGROUNDED", "label": "free-living environment", "parent_habitats": ["ENVO:01000254"]}} |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; Five-position ecosystem paths preserved; contacts excluded; first 3 BioSample and Organism descriptions per target | supports | Exact positional census counts={"Biosample": 1192, "Organism": 958, "SequencingProject": 1667}; individually inspected descriptions={"Biosample": [{"data": {"BIOSAMPLE GOLD ID": "Gb0055052", "BIOSAMPLE NAME": "Enriched marine sediment ecosystem from Crete, Greece ", "BIOSAMPLE NCBI TAX NAME": "marine sediment metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Crete, Greece"}, "row": 3138}, {"data": {"BIOSAMPLE GOLD ID": "Gb0112951", "BIOSAMPLE NAME": "Trench sediment microbial communities from the deep Pacific Ocean", "BIOSAMPLE NCBI TAX NAME": "marine sediment metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Deep-Sea Trench"}, "row": 7504}, {"data": {"BIOSAMPLE GOLD ID": "Gb0136900", "BIOSAMPLE NAME": "Deep sea sediment microbial communities from the Gulf of Mexico - control with no oil added", "BIOSAMPLE NCBI TAX NAME": "sediment metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Deepsea sediment of the Gulf of Mexico"}, "row": 12727}], "Organism": [{"data": {"ORGANISM GOLD ID": "Go0000056", "ORGANISM HABITAT": "Marine&#124;Sediment", "ORGANISM NAME": "Shewanella sediminis HAW-EB3", "ORGANISM SAMPLE COLLECTION SITE": "Sediment at depth of 215m from an unexploded-ordinance-dumping site at Halifax"}, "row": 51}, {"data": {"ORGANISM GOLD ID": "Go0000182", "ORGANISM HABITAT": "Sediment&#124;Fresh water", "ORGANISM NAME": "Desulforamulus reducens MI-1", "ORGANISM SAMPLE COLLECTION SITE": "Heavy metal-contaminated sediment collected at the Mare Island Naval Shipyard on the San Francisco Bay"}, "row": 173}, {"data": {"ORGANISM GOLD ID": "Go0003229", "ORGANISM HABITAT": "Marine&#124;Sediment&#124;Surface water", "ORGANISM NAME": "Luminiphilus syltensis NOR5-1B", "ORGANISM SAMPLE COLLECTION SITE": "top oxic layer of a muddy sediment core, List, Sylt (55002'N, 8024'E) Germany, 19.10.2005"}, "row": 2843}]}. These later examples may include mixed sample/host/enrichment contexts; they do not reconstruct original assertion membership. Remaining members and study joins were indexed, not individually assessed. |
| CLASS | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Later official classification; 29 of 31 cohort paths matched; missing tuples do not establish nonexistence | supports | [{"row": 794, "slug": "marine_sediment", "path": "Environmental &gt; Aquatic &gt; Marine &gt; Sediment", "values": ["4564", "Environmental", "Aquatic", "Marine", "Sediment", "Unclassified"]}] |
| TAX0 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1000566%2C1003110%2C1005925%2C1005926%2C1005928%2C1006%2C1007105%2C1007109%2C1007110%2C1007111%2C1007112%2C1007113%2C1007114%2C1007115%2C1007116%2C1007117%2C1007118%2C1007119%2C1007120%2C1007122%2C1007124%2C1009412%2C1009413%2C1009414%2C1009415%2C1009416%2C1009418%2C1009419%2C1009420%2C1009421%2C1017277%2C102%2C1026%2C1027373%2C1027374%2C1028566%2C1028742%2C1028743%2C1028745%2C1028746%2C1028749%2C1028752%2C1031273%2C1031541%2C103810%2C1038845%2C1038928%2C1038929%2C1042%2C104268%2C104270%2C1042877%2C1044%2C104421%2C1045558%2C1048%2C1048221%2C1057%2C106299%2C1074%2C107401%2C1080%2C1089550%2C109263%2C1094980%2C110163%2C1104565%2C1104566%2C110662%2C110663%2C111770%2C1121404%2C1121937%2C1121948%2C1122607%2C1123059%2C1123242%2C1123275%2C114404%2C1150474%2C119394%2C119542%2C1208324%2C1211807%2C121224%2C1217908%2C1219067%2C1242148%2C1246444%2C1246460%2C1265%2C126741%2C1267768%2C1267769%2C1276246%2C1282%2C129958%2C132144%2C133924%2C134561%2C1358%2C13616%2C13686%2C1371%2C1387275%2C139239%2C1394%2C1411902%2C143223%2C143224%2C147%2C1486246%2C150120%2C1543721%2C156%2C156128%2C156133%2C1570%2C158080%2C158192%2C158500%2C1609977%2C161528%2C163248%2C163503%2C168275%2C168759%2C1703256%2C1716143%2C172371%2C173%2C173365%2C173737%2C173764%2C174%2C174302%2C174315%2C1774373%2C179326%2C180542%2C1808508%2C1808945%2C1817405%2C1836499%2C184592%2C184914%2C1855%2C186022%2C1869227%2C1871328&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The three chunks jointly resolve all 346 requested cohort IDs. Target results=[{"current_id": "1003110", "current_name": "Micromonospora maris", "frozen_label": "verrucosispora_maris", "id": "1003110", "rank": "species"}, {"current_id": "1005925", "current_name": "Kordiimonas aestuarii", "frozen_label": "Kordiimonas aestuarii", "id": "1005925", "rank": "species"}, {"current_id": "1005926", "current_name": "Flagellimonas taeanensis", "frozen_label": "Muricauda taeanensis", "id": "1005926", "rank": "species"}, {"current_id": "1005928", "current_name": "Roseovarius lutimaris", "frozen_label": "roseovarius_lutimaris", "id": "1005928", "rank": "species"}, {"current_id": "1006", "current_name": "Marivirga tractuosa", "frozen_label": "flexibacter_tractuosus", "id": "1006", "rank": "species"}, {"current_id": "1007105", "current_name": "Pusillimonas sp. T7-7", "frozen_label": "Pusillimonas sp. T7-7", "id": "1007105", "rank": "species"}, {"current_id": "296995", "current_name": "Exiguobacterium indicum", "frozen_label": "exiguobacterium_enclense", "id": "1017277", "rank": "species"}, {"current_id": "1027373", "current_name": "Nitrosopumilus sp. AR", "frozen_label": "Nitrosopumilus sp. AR", "id": "1027373", "rank": "species"}, {"current_id": "1027374", "current_name": "Nitrosopumilus sp. SJ", "frozen_label": "Nitrosopumilus sp. SJ", "id": "1027374", "rank": "species"}, {"current_id": "1028566", "current_name": "Sulfolobus acidocaldarius N8", "frozen_label": "Sulfolobus acidocaldarius N8", "id": "1028566", "rank": "strain"}, {"current_id": "1028742", "current_name": "Pontixanthobacter gangjinensis", "frozen_label": "Altererythrobacter gangjinensis", "id": "1028742", "rank": "species"}, {"current_id": "1028743", "current_name": "Arenibacter hampyeongensis", "frozen_label": "Arenibacter hampyeongensis", "id": "1028743", "rank": "species"}, {"current_id": "1028745", "current_name": "Aestuariibaculum suncheonense", "frozen_label": "Aestuariibaculum suncheonense", "id": "1028745", "rank": "species"}, {"current_id": "1028746", "current_name": "Christiangramia aestuarii", "frozen_label": "Gramella aestuarii", "id": "1028746", "rank": "species"}, {"current_id": "1028749", "current_name": "Microbulbifer gwangyangensis", "frozen_label": "Microbulbifer gwangyangensis", "id": "1028749", "rank": "species"}, {"current_id": "1028752", "current_name": "Shewanella aestuarii", "frozen_label": "Shewanella aestuarii", "id": "1028752", "rank": "species"}, {"current_id": "1031273", "current_name": "Gaetbulibacter lutimaris", "frozen_label": "Gaetbulibacter lutimaris", "id": "1031273", "rank": "species"}, {"current_id": "1031541", "current_name": "Tropicimonas sediminicola", "frozen_label": "tropicimonas_sediminicola", "id": "1031541", "rank": "species"}, {"current_id": "1038845", "current_name": "Flavobacterium rakeshii", "frozen_label": "flavobacterium_rakeshii", "id": "1038845", "rank": "species"}, {"current_id": "1038928", "current_name": "Streptomyces xinghaiensis", "frozen_label": "streptomyces_xinghaiensis", "id": "1038928", "rank": "species"}, {"current_id": "1038929", "current_name": "Streptomyces xinghaiensis S187", "frozen_label": "Streptomyces xinghaiensis S187", "id": "1038929", "rank": "strain"}, {"current_id": "1042877", "current_name": "Thermococcus sp. 4557", "frozen_label": "Thermococcus sp. 4557", "id": "1042877", "rank": "species"}, {"current_id": "1045558", "current_name": "Neptunomonas qingdaonensis", "frozen_label": "Neptunomonas qingdaonensis", "id": "1045558", "rank": "species"}, {"current_id": "1048", "current_name": "Marichromatium gracile", "frozen_label": "marichromatium_gracile", "id": "1048", "rank": "species"}, {"current_id": "1048221", "current_name": "Mucilaginibacter litoreus", "frozen_label": "Mucilaginibacter litoreus", "id": "1048221", "rank": "species"}]. Alias/name resolution does not establish habitat occurrence. |
| TAX1 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1872627%2C1876%2C188906%2C188908%2C1903071%2C190308%2C191302%2C1926630%2C1931%2C195064%2C1961642%2C197222%2C198804%2C2%2C200617%2C2022602%2C2024855%2C203122%2C203907%2C205920%2C2099376%2C212050%2C214688%2C214988%2C216432%2C216773%2C2183988%2C2213%2C223788%2C224915%2C225345%2C225937%2C226126%2C2264%2C234267%2C240016%2C2423%2C243090%2C247026%2C257363%2C264%2C264462%2C264951%2C265606%2C266940%2C2738566%2C28108%2C28122%2C28181%2C28223%2C28251%2C28258%2C28262%2C29158%2C29159%2C2926447%2C29292%2C293614%2C29805%2C302409%2C3055%2C3068%2C31330%2C313595%2C313603%2C313606%2C314230%2C314275%2C316279%2C319225%2C320388%2C332415%2C337701%2C339861%2C340047%2C34085%2C344747%2C357244%2C35743%2C35845%2C358766%2C361576%2C36870%2C36987%2C372461%2C378806%2C379066%2C39152%2C391625%2C39947%2C402880%2C40464%2C406538%2C406540%2C411477%2C411485%2C419481%2C425006%2C428125%2C435805%2C43928%2C442956%2C443152%2C445336%2C44751%2C45351%2C457427%2C463619%2C46539%2C466153%2C46687%2C46704%2C46745%2C472759%2C483407%2C483417%2C48499%2C48729%2C491952%2C49447%2C498761%2C502025%2C504472%2C50741%2C515618%2C51671%2C518766%2C523849%2C530564%2C53249%2C537937%2C53953%2C55518%2C555512%2C55567%2C562%2C563043%2C56780%2C56811%2C57043%2C575540%2C583355%2C585501%2C595452%2C595453%2C59919%2C59920%2C6047%2C60480%2C6087&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The three chunks jointly resolve all 346 requested cohort IDs. Target results=[{"current_id": "1003110", "current_name": "Micromonospora maris", "frozen_label": "verrucosispora_maris", "id": "1003110", "rank": "species"}, {"current_id": "1005925", "current_name": "Kordiimonas aestuarii", "frozen_label": "Kordiimonas aestuarii", "id": "1005925", "rank": "species"}, {"current_id": "1005926", "current_name": "Flagellimonas taeanensis", "frozen_label": "Muricauda taeanensis", "id": "1005926", "rank": "species"}, {"current_id": "1005928", "current_name": "Roseovarius lutimaris", "frozen_label": "roseovarius_lutimaris", "id": "1005928", "rank": "species"}, {"current_id": "1006", "current_name": "Marivirga tractuosa", "frozen_label": "flexibacter_tractuosus", "id": "1006", "rank": "species"}, {"current_id": "1007105", "current_name": "Pusillimonas sp. T7-7", "frozen_label": "Pusillimonas sp. T7-7", "id": "1007105", "rank": "species"}, {"current_id": "296995", "current_name": "Exiguobacterium indicum", "frozen_label": "exiguobacterium_enclense", "id": "1017277", "rank": "species"}, {"current_id": "1027373", "current_name": "Nitrosopumilus sp. AR", "frozen_label": "Nitrosopumilus sp. AR", "id": "1027373", "rank": "species"}, {"current_id": "1027374", "current_name": "Nitrosopumilus sp. SJ", "frozen_label": "Nitrosopumilus sp. SJ", "id": "1027374", "rank": "species"}, {"current_id": "1028566", "current_name": "Sulfolobus acidocaldarius N8", "frozen_label": "Sulfolobus acidocaldarius N8", "id": "1028566", "rank": "strain"}, {"current_id": "1028742", "current_name": "Pontixanthobacter gangjinensis", "frozen_label": "Altererythrobacter gangjinensis", "id": "1028742", "rank": "species"}, {"current_id": "1028743", "current_name": "Arenibacter hampyeongensis", "frozen_label": "Arenibacter hampyeongensis", "id": "1028743", "rank": "species"}, {"current_id": "1028745", "current_name": "Aestuariibaculum suncheonense", "frozen_label": "Aestuariibaculum suncheonense", "id": "1028745", "rank": "species"}, {"current_id": "1028746", "current_name": "Christiangramia aestuarii", "frozen_label": "Gramella aestuarii", "id": "1028746", "rank": "species"}, {"current_id": "1028749", "current_name": "Microbulbifer gwangyangensis", "frozen_label": "Microbulbifer gwangyangensis", "id": "1028749", "rank": "species"}, {"current_id": "1028752", "current_name": "Shewanella aestuarii", "frozen_label": "Shewanella aestuarii", "id": "1028752", "rank": "species"}, {"current_id": "1031273", "current_name": "Gaetbulibacter lutimaris", "frozen_label": "Gaetbulibacter lutimaris", "id": "1031273", "rank": "species"}, {"current_id": "1031541", "current_name": "Tropicimonas sediminicola", "frozen_label": "tropicimonas_sediminicola", "id": "1031541", "rank": "species"}, {"current_id": "1038845", "current_name": "Flavobacterium rakeshii", "frozen_label": "flavobacterium_rakeshii", "id": "1038845", "rank": "species"}, {"current_id": "1038928", "current_name": "Streptomyces xinghaiensis", "frozen_label": "streptomyces_xinghaiensis", "id": "1038928", "rank": "species"}, {"current_id": "1038929", "current_name": "Streptomyces xinghaiensis S187", "frozen_label": "Streptomyces xinghaiensis S187", "id": "1038929", "rank": "strain"}, {"current_id": "1042877", "current_name": "Thermococcus sp. 4557", "frozen_label": "Thermococcus sp. 4557", "id": "1042877", "rank": "species"}, {"current_id": "1045558", "current_name": "Neptunomonas qingdaonensis", "frozen_label": "Neptunomonas qingdaonensis", "id": "1045558", "rank": "species"}, {"current_id": "1048", "current_name": "Marichromatium gracile", "frozen_label": "marichromatium_gracile", "id": "1048", "rank": "species"}, {"current_id": "1048221", "current_name": "Mucilaginibacter litoreus", "frozen_label": "Mucilaginibacter litoreus", "id": "1048221", "rank": "species"}]. Alias/name resolution does not establish habitat occurrence. |
| TAX2 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=610380%2C6182%2C6238%2C6334%2C639602%2C641112%2C6613%2C6669%2C688066%2C69293%2C6945%2C69773%2C7029%2C703612%2C7070%2C7159%2C7209%2C7425%2C74546%2C74547%2C748449%2C756272%2C758583%2C75883%2C760154%2C765912%2C7668%2C76775%2C7719%2C777%2C7955%2C80836%2C8090%2C83428%2C86104%2C880%2C880447%2C885%2C89184%2C9031%2C91360%2C9258%2C939306%2C939316%2C939324%2C939346&amp;retmode=xml; NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames | supports | The three chunks jointly resolve all 346 requested cohort IDs. Target results=[{"current_id": "1003110", "current_name": "Micromonospora maris", "frozen_label": "verrucosispora_maris", "id": "1003110", "rank": "species"}, {"current_id": "1005925", "current_name": "Kordiimonas aestuarii", "frozen_label": "Kordiimonas aestuarii", "id": "1005925", "rank": "species"}, {"current_id": "1005926", "current_name": "Flagellimonas taeanensis", "frozen_label": "Muricauda taeanensis", "id": "1005926", "rank": "species"}, {"current_id": "1005928", "current_name": "Roseovarius lutimaris", "frozen_label": "roseovarius_lutimaris", "id": "1005928", "rank": "species"}, {"current_id": "1006", "current_name": "Marivirga tractuosa", "frozen_label": "flexibacter_tractuosus", "id": "1006", "rank": "species"}, {"current_id": "1007105", "current_name": "Pusillimonas sp. T7-7", "frozen_label": "Pusillimonas sp. T7-7", "id": "1007105", "rank": "species"}, {"current_id": "296995", "current_name": "Exiguobacterium indicum", "frozen_label": "exiguobacterium_enclense", "id": "1017277", "rank": "species"}, {"current_id": "1027373", "current_name": "Nitrosopumilus sp. AR", "frozen_label": "Nitrosopumilus sp. AR", "id": "1027373", "rank": "species"}, {"current_id": "1027374", "current_name": "Nitrosopumilus sp. SJ", "frozen_label": "Nitrosopumilus sp. SJ", "id": "1027374", "rank": "species"}, {"current_id": "1028566", "current_name": "Sulfolobus acidocaldarius N8", "frozen_label": "Sulfolobus acidocaldarius N8", "id": "1028566", "rank": "strain"}, {"current_id": "1028742", "current_name": "Pontixanthobacter gangjinensis", "frozen_label": "Altererythrobacter gangjinensis", "id": "1028742", "rank": "species"}, {"current_id": "1028743", "current_name": "Arenibacter hampyeongensis", "frozen_label": "Arenibacter hampyeongensis", "id": "1028743", "rank": "species"}, {"current_id": "1028745", "current_name": "Aestuariibaculum suncheonense", "frozen_label": "Aestuariibaculum suncheonense", "id": "1028745", "rank": "species"}, {"current_id": "1028746", "current_name": "Christiangramia aestuarii", "frozen_label": "Gramella aestuarii", "id": "1028746", "rank": "species"}, {"current_id": "1028749", "current_name": "Microbulbifer gwangyangensis", "frozen_label": "Microbulbifer gwangyangensis", "id": "1028749", "rank": "species"}, {"current_id": "1028752", "current_name": "Shewanella aestuarii", "frozen_label": "Shewanella aestuarii", "id": "1028752", "rank": "species"}, {"current_id": "1031273", "current_name": "Gaetbulibacter lutimaris", "frozen_label": "Gaetbulibacter lutimaris", "id": "1031273", "rank": "species"}, {"current_id": "1031541", "current_name": "Tropicimonas sediminicola", "frozen_label": "tropicimonas_sediminicola", "id": "1031541", "rank": "species"}, {"current_id": "1038845", "current_name": "Flavobacterium rakeshii", "frozen_label": "flavobacterium_rakeshii", "id": "1038845", "rank": "species"}, {"current_id": "1038928", "current_name": "Streptomyces xinghaiensis", "frozen_label": "streptomyces_xinghaiensis", "id": "1038928", "rank": "species"}, {"current_id": "1038929", "current_name": "Streptomyces xinghaiensis S187", "frozen_label": "Streptomyces xinghaiensis S187", "id": "1038929", "rank": "strain"}, {"current_id": "1042877", "current_name": "Thermococcus sp. 4557", "frozen_label": "Thermococcus sp. 4557", "id": "1042877", "rank": "species"}, {"current_id": "1045558", "current_name": "Neptunomonas qingdaonensis", "frozen_label": "Neptunomonas qingdaonensis", "id": "1045558", "rank": "species"}, {"current_id": "1048", "current_name": "Marichromatium gracile", "frozen_label": "marichromatium_gracile", "id": "1048", "rank": "species"}, {"current_id": "1048221", "current_name": "Mucilaginibacter litoreus", "frozen_label": "Mucilaginibacter litoreus", "id": "1048221", "rank": "species"}]. Alias/name resolution does not establish habitat occurrence. |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf; Search boundaries are explicit; no global absence claim | supports | Identifier, label, slug and exact-path searches included hidden/ignored files in these roots. No earlier structured target observation was found. Legacy reports exist and are not silently retired. Bounded original-source search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv", "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv", "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv", "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv", "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv", "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv", "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv", "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv", "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv", "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv", "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}], "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "exit_code": 0, "matches": [], "stderr": ""}]} |
| ISSUES | https://github.com/CultureBotAI/HabitatMech/issues; GitHub CLI inventory retrieved 12-Oct | supports | Read-only all-state 967-issue title/body inventory and relevant bodies inspected. Issues are historical leads, not primary support; current owner rows and scientific evidence were checked independently. Comments were not exhaustively crawled. Closed issue #1301 is reflected in the current graph and is not reopened by preserving old history. |
| GRAPH | curation/causal_graphs/marine_sediment.yaml; Current full overlay | supports | Entire overlay and generated graph read, including all node types, edge descriptions, evidence and preserved historical events. |
| DHONDT | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6684631/fullTextXML; PMID:31388058; Introduction/Fig1 and Box1 | supports | Oxic exceptions, burial and overlapping respiratory processes. |
| JORGENSEN | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6492693/fullTextXML; PMID:31105660; Introduction/Fig1 and Organic Matter Degradation | supports | Conditional sulfate supply, carbon oxidation, sulfide oxidation and iron-sulfide sinks. |
| WASMUND | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5573963/fullTextXML; PMID:28419734; Introduction and Sulfate-Reducing Microorganisms | supports | Polyphyletic sulfur guilds and coupled redox transformations. The exact snippet marine sediment sulfur cycling was searched across all XML text with whitespace normalized and was not found; the Introduction still supports sulfate-to-sulfide conversion. |
| NAGAKURA | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8927301/fullTextXML; PMID:35308366; Introduction | supports | Guaymas sediment context and sulfate-reduction pathways, not universal exclusion of other respiration. |
| LIN | https://api.repository.cam.ac.uk/server/api/core/bitstreams/da5d036c-2344-4ffc-8494-216f2fee4429/content; DOI:10.1016/j.epsl.2022.117841; Abstract, Results3.2 and Discussion pp6-9 | supports | Clay-surface experiments support altered sulfate-reduction rates, not the asserted iron trapping mechanism. |
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
review_id: 20261012T054255Z-marine_sediment
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: marine_sediment'
started_at: '2026-10-12T05:18:55.657116Z'
finished_at: '2026-10-12T05:42:55.442542Z'
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
summary: Marine sediment is deposited particulate material, not a whole marine water
  body. Preserve sediment ancestry, 1035 GOLD ORGANISM assertions, the 837-member
  Madin taxon pool, 25 displayed associations and seven source-attributed qualitative
  parameter bands. The 14-edge sulfur graph needs conditional redox scope, claim-specific
  evidence, correct carbon/sulfur wording and truthful node types; taxonomic aliases
  also need versioned maintenance.
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
  - path: curation/causal_graphs/marine_sediment.yaml
    sha256: 8b230eb079171ab8134b648caa29878dc5015fb36362559a6a8c67fb2b433741
    role: context
  - path: curation/causal_graphs/marine_water_body.yaml
    sha256: b2f81102970e9541bf61978fabdd68b7db8f9459f1ef11b467fecfc2956f238b
    role: context
  - path: curation/causal_graphs/sediment.yaml
    sha256: 62b97afba9466dc64f8b5b1b3fd5d92f8b4b6bf96fe1c761af579ff7deca0e47
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
  - path: data/habitats/aquatic/marine_sediment.yaml
    sha256: 3ec90a8a523183bb7807e01ab1aa7d2ab5d6d2e72b0b49dbb09e447d22bd50a4
    role: target
  - path: data/habitats/aquatic/marine_water_body.yaml
    sha256: 2f4bbc8c5e548c015eed7c3ff7e59df17ba70da940f7877f0d4097deebea8046
    role: context
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
    sha256: f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/mappings/subtidal_zone_sediment/2026-10-06T155005Z-codex-gpt-5-1d40a6.yaml
    sha256: 4b39092f3177df08d06b44660036442e394b3a622ab9cc62057116d792194dca
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260927T070044Z-continental_margin.md
    sha256: 19b399914525093f25c7e2b723a1160fc918921694bb78fb9c45caf59d704ce1
    role: context
  - path: reports/yaml_record_review/20260927T113801Z-deep_marine_sediment.md
    sha256: 20d56ca4e54205031b580fc35da2feeb5f8d037c92d79ea15fd90940d83ae2f2
    role: context
  - path: reports/yaml_record_review/20261002T031939Z-estuarine_sediment.md
    sha256: 841e3e589ce8d20aa5039906c0ff61dc483e5f6b0a5e0d04e6c6c11fca759d5c
    role: context
  - path: reports/yaml_record_review/20261003T172452Z-mangrove_sediment.md
    sha256: e292a7643c4b448b3632987e0a0a553141369409c03485458fd88a9d4c240f81
    role: context
  - path: reports/yaml_record_review/20261003T201434Z-marine_sediment.md
    sha256: 934f32cad95162955f3d45f3dbaf811bef9e72a622e96e978c78f6e922bd6e10
    role: context
  - path: reports/yaml_record_review/20261004T194729Z-mud_volcano__980e0b1f.md
    sha256: 1e32d50eeb6654cc5710c5609c194ff3c950ff3ca4a1fd6db92d26b7e4436e39
    role: context
  - path: reports/yaml_record_review/20261004T220733Z-oil_contaminated_sediment__3c338598.md
    sha256: f5fa244cb6d458a30b40da3a84c215fe9f30319a45e9e85c5eae78a03494bfbe
    role: context
  - path: reports/yaml_record_review/20261004T221058Z-oil_contaminated_sediment__6a7b1764.md
    sha256: 1d75607b82d33477d6421f9d148b645356c63cded96b846310927b7e7f86ffd2
    role: context
  - path: reports/yaml_record_review/20261004T221603Z-oil_contaminated_sediment__b1bb8113.md
    sha256: a0d108b2ae0d45369c8fe098567c3cc7bd37a472345b4b749afbd7641add9f2f
    role: context
  - path: reports/yaml_record_review/20261005T030436Z-sabkha_sediment.md
    sha256: b0b70eae0be91964ae6a551a003547f6926082bf3b667cd572cf7391385f07d5
    role: context
  - path: reports/yaml_record_review/20261005T063632Z-salt_marsh_sediment.md
    sha256: fd20cff2809b310ab37c39375fe6cbb3ce9f25b4f255721ce7dfa67b81505fdf
    role: context
  - path: reports/yaml_record_review/20261005T064509Z-salt_pond_sediment.md
    sha256: df8d37cfbcd3cc9711e3f1dcee48df4620e26d44fb2d736b042af9da47da3fe0
    role: context
  - path: reports/yaml_record_review/20261005T085456Z-seagrass_bed_sediment.md
    sha256: 8850312900721ef09c463e31ecf7e13f5d4ddee5a9598e65f4a3684d3095b637
    role: context
  - path: reports/yaml_record_review/20261005T102204Z-sediment__0ef8e416.md
    sha256: 269ebd5e18fd050947e5c61ce89a2174a5806a86145556ba61720ce2f6be5520
    role: context
  - path: reports/yaml_record_review/20261005T102756Z-sediment__11488300.md
    sha256: dc90148490b7d987335adfd7528aeca8d520cfcb55b196d20a5620c8ee174682
    role: context
  - path: reports/yaml_record_review/20261005T111306Z-sediment__2a63f0bb.md
    sha256: cf2cbbb8deb2d553142a4c33bec289760df9bba3f37900f69ecc7106d237460f
    role: context
  - path: reports/yaml_record_review/20261005T111751Z-sediment__2b3ec834.md
    sha256: e6ca42f5ff00b317c307e491da24aa1d9114ed72e5f33e9b1a27ee4190773471
    role: context
  - path: reports/yaml_record_review/20261005T112645Z-sediment__301877e9.md
    sha256: 4f4e08398dd8adee45aaf0170a34880752d19049cd42c74aed86c54f33563ad7
    role: context
  - path: reports/yaml_record_review/20261005T120103Z-sediment__347a23a3.md
    sha256: bb25e912efb70b77f719eb0bc1436f81219a771b3735e9788b0bbff5885d4ec7
    role: context
  - path: reports/yaml_record_review/20261005T121510Z-sediment__3f324bf4.md
    sha256: 0adc86f9392b482537ccf9ba1296cc60ab02bdb2e82bf362094e130b258e33c1
    role: context
  - path: reports/yaml_record_review/20261005T151749Z-sediment__69d4893f.md
    sha256: 2c2e186fe5b68412281b1b2f5da224d52d0696c6105c214c6e92c8d139a4439c
    role: context
  - path: reports/yaml_record_review/20261005T160547Z-sediment__745f8d63.md
    sha256: d54892bccfa0067e25db4935356ba442bf89a7b094c499d148790f6e62261f46
    role: context
  - path: reports/yaml_record_review/20261005T165619Z-sediment__8cbae4cd.md
    sha256: 92c5f925a4b94a90dee5e72cad901284ae8664d6fa51e2bcabd77f5ff90558b5
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
  - path: reports/yaml_record_review/20261005T214517Z-sediment__e3709872.md
    sha256: 99e665047ca684e4aa538398afa1499f49973c8635a6db7f35508a7e1af2102f
    role: context
  - path: reports/yaml_record_review/20261005T222657Z-sediment__e63c4954.md
    sha256: 33b512efb9d34438b8923e675c14ef8669d93cd10798c5bb6cd03db6d367e3d1
    role: context
  - path: reports/yaml_record_review/20261005T231034Z-sediment__e8fdcd7d.md
    sha256: c1759e496a673e8570f4161c65c5ce9d32f2d2d6e3a5eb5a3010a30ebf678dd3
    role: context
  - path: reports/yaml_record_review/20261005T231535Z-sediment__e910a9d2.md
    sha256: ab63d4d6b197b39e2bcfc9a0bf3ccfb04200dfc2be49d4680e341a4cf76568b7
    role: context
  - path: reports/yaml_record_review/20261008T083813Z-defined_media__b53817a1.md
    sha256: 394ad9be6d875469384aa6a15053f6af702e3ca325dbd6b449a322a09c2d4bfb
    role: context
  - path: research/habitats/other/core-sample-habitatmech-bacdive-3bf519722c-deep-research-claude_code.md
    sha256: 818ad0e118be0bd31e5e59e385c1ed2ce30a498936d04fb9793d1584953b7630
    role: context
  - path: research/habitats/terrestrial/rock-core-sediment-habitatmech-gold-3b04872853-deep-research-claude_code.md
    sha256: d4233582ddf5bf3f1111cfd94c1d482c354da7924f672b7905f010feba5dc992
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
- target_id: ENVO:03000033
  path: data/habitats/aquatic/marine_sediment.yaml
  label: marine sediment
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
    path: data/raw/environment_parameters.tsv
    role: Frozen ENVIRONMENTS_TABLE source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitats.tsv
    role: Frozen MADIN source inventory
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Frozen MADIN source inventory
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/marine_sediment.yaml
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
  - ENVO:03000033
  exclusions:
  - target: Other 3207 current records
    reason: Context reads are not their full scientific review.
checks:
- check_id: C0
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:03000033
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=ed9e0d0f382e4502a64f4de10102c4512bddca38
    just validate data/habitats/aquatic/marine_sediment.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T05:22:08.341299Z to 2026-10-12T05:22:11.391220Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C1
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - ENVO:03000033
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
  - ENVO:03000033
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
  - ENVO:03000033
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
  - ENVO:03000033
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
  - ENVO:03000033
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
  - ENVO:03000033
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
  - ENVO:03000033
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
  - ENVO:03000033
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
  - ENVO:03000033
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
  - ENVO:03000033
  summary: Bounded ignored-inclusive searches did not recover complete original assertion
    inputs; later exports are contextual evidence only.
  evidence_ids:
  - SEARCH
- check_id: IMODULON
  name: Expression-adapter applicability
  required: false
  status: not_applicable
  target_ids:
  - ENVO:03000033
  summary: The successful 28-dataset inventory was read for graph scope. No matching
    claim-specific organism/strain/gene or expression-module assertion requires a
    search or summarize call. Absence is not negative ecological evidence.
  evidence_ids:
  - IMODULONDB
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/aquatic/marine_sediment.yaml
  summary: Marine sediment is deposited particulate material, not a whole marine water
    body. Preserve sediment ancestry, 1035 GOLD ORGANISM assertions, the 837-member
    Madin taxon pool, 25 displayed associations and seven source-attributed qualitative
    parameter bands. The 14-edge sulfur graph needs conditional redox scope, claim-specific
    evidence, correct carbon/sulfur wording and truthful node types; taxonomic aliases
    also need versioned maintenance.
  accessed_at: '2026-10-12T05:40:53.189655Z'
  support: supports
  locator: Entire captured YAML read, including all taxa, parameters, graphs and generated
    history
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml
  summary: Applied exact identity, strict-genus, MIxS roles, source-unit/score and
    ITEM lifecycle contracts; graph node types retain their biological definitions.
  accessed_at: '2026-10-12T05:40:53.189655Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"data/raw/environment_parameters.tsv": [{"data": {"cobo_simon_habitat":
    "marine", "env_type": "sediment_marine", "main_group": "Aquatic", "parameter":
    "Salinity", "term_ids": "ENVO:03000033", "term_labels": "marine sediment", "value":
    "high"}, "logical_row": 95}, {"data": {"cobo_simon_habitat": "marine", "env_type":
    "sediment_marine", "main_group": "Aquatic", "parameter": "Structural", "term_ids":
    "ENVO:03000033", "term_labels": "marine sediment", "value": "medium"}, "logical_row":
    96}, {"data": {"cobo_simon_habitat": "marine", "env_type": "sediment_marine",
    "main_group": "Aquatic", "parameter": "Water", "term_ids": "ENVO:03000033", "term_labels":
    "marine sediment", "value": "high"}, "logical_row": 97}, {"data": {"cobo_simon_habitat":
    "marine", "env_type": "sediment_marine", "main_group": "Aquatic", "parameter":
    "pH", "term_ids": "ENVO:03000033", "term_labels": "marine sediment", "value":
    "high"}, "logical_row": 98}, {"data": {"cobo_simon_habitat": "marine", "env_type":
    "sediment_marine", "main_group": "Aquatic", "parameter": "salinity variability",
    "term_ids": "ENVO:03000033", "term_labels": "marine sediment", "value": "small"},
    "logical_row": 99}, {"data": {"cobo_simon_habitat": "marine", "env_type": "sediment_marine",
    "main_group": "Aquatic", "parameter": "temp variability", "term_ids": "ENVO:03000033",
    "term_labels": "marine sediment", "value": "low"}, "logical_row": 100}, {"data":
    {"cobo_simon_habitat": "marine", "env_type": "sediment_marine", "main_group":
    "Aquatic", "parameter": "water variability", "term_ids": "ENVO:03000033", "term_labels":
    "marine sediment", "value": "permanently wet"}, "logical_row": 101}], "data/raw/gold_ecosystem_paths.tsv":
    [{"data": {"biosample_count": "0", "canonical_path": "Environmental > Aquatic
    > Marine > Sediment", "depth": "4", "ecosystem": "Environmental", "ecosystem_category":
    "Aquatic", "ecosystem_subtype": "Sediment", "ecosystem_type": "Marine", "gold_node_count":
    "2", "gold_node_ids": "gold.ecosystem:4563|gold.ecosystem:4564", "leaf_label":
    "Sediment", "organism_count": "1035", "specific_ecosystem": "", "study_count":
    "0", "total_assertions": "1035"}, "logical_row": 39}], "data/raw/gold_path_biosamples.tsv":
    [{"data": {"biosample_count": "533", "canonical_path": "Environmental > Aquatic
    > Marine > Sediment", "ecosystem_path_id": "4564"}, "logical_row": 66}], "data/raw/gold_path_triads.tsv":
    [{"data": {"canonical_path": "Environmental > Aquatic > Marine > Sediment", "distinct_terms":
    "3", "samples": "286", "slot": "broad", "studies": "40", "studies_agreeing": "38",
    "top_label": "marine benthic biome", "top_share": "0.92", "top_term": "ENVO:01000024"},
    "logical_row": 665}, {"data": {"canonical_path": "Environmental > Aquatic > Marine
    > Sediment", "distinct_terms": "3", "samples": "286", "slot": "local", "studies":
    "40", "studies_agreeing": "37", "top_label": "marine benthic feature", "top_share":
    "0.92", "top_term": "ENVO:01000105"}, "logical_row": 666}, {"data": {"canonical_path":
    "Environmental > Aquatic > Marine > Sediment", "distinct_terms": "2", "samples":
    "286", "slot": "medium", "studies": "40", "studies_agreeing": "39", "top_label":
    "marine sediment", "top_share": "0.93", "top_term": "ENVO:03000033"}, "logical_row":
    667}], "data/raw/madin_habitat_taxa.tsv": [{"data": {"corroborated_by": "", "madin_id":
    "ENVO:03000033", "taxon_id": "NCBITaxon:1003110", "taxon_label": "verrucosispora_maris"},
    "logical_row": 997}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033",
    "taxon_id": "NCBITaxon:1005925", "taxon_label": "Kordiimonas aestuarii"}, "logical_row":
    998}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id":
    "NCBITaxon:1005926", "taxon_label": "Muricauda taeanensis"}, "logical_row": 999},
    {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1005928",
    "taxon_label": "roseovarius_lutimaris"}, "logical_row": 1000}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1006", "taxon_label":
    "flexibacter_tractuosus"}, "logical_row": 1001}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1007105", "taxon_label":
    "Pusillimonas sp. T7-7"}, "logical_row": 1002}, {"data": {"corroborated_by": "",
    "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1017277", "taxon_label": "exiguobacterium_enclense"},
    "logical_row": 1003}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033",
    "taxon_id": "NCBITaxon:1027373", "taxon_label": "Nitrosopumilus sp. AR"}, "logical_row":
    1004}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id":
    "NCBITaxon:1027374", "taxon_label": "Nitrosopumilus sp. SJ"}, "logical_row": 1005},
    {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028566",
    "taxon_label": "Sulfolobus acidocaldarius N8"}, "logical_row": 1006}, {"data":
    {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028742",
    "taxon_label": "Altererythrobacter gangjinensis"}, "logical_row": 1007}, {"data":
    {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028743",
    "taxon_label": "Arenibacter hampyeongensis"}, "logical_row": 1008}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028745", "taxon_label":
    "Aestuariibaculum suncheonense"}, "logical_row": 1009}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028746", "taxon_label":
    "Gramella aestuarii"}, "logical_row": 1010}, {"data": {"corroborated_by": "",
    "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1028749", "taxon_label": "Microbulbifer
    gwangyangensis"}, "logical_row": 1011}, {"data": {"corroborated_by": "", "madin_id":
    "ENVO:03000033", "taxon_id": "NCBITaxon:1028752", "taxon_label": "Shewanella aestuarii"},
    "logical_row": 1012}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033",
    "taxon_id": "NCBITaxon:1031273", "taxon_label": "Gaetbulibacter lutimaris"}, "logical_row":
    1013}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id":
    "NCBITaxon:1031541", "taxon_label": "tropicimonas_sediminicola"}, "logical_row":
    1014}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id":
    "NCBITaxon:1038845", "taxon_label": "flavobacterium_rakeshii"}, "logical_row":
    1015}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id":
    "NCBITaxon:1038928", "taxon_label": "streptomyces_xinghaiensis"}, "logical_row":
    1016}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id":
    "NCBITaxon:1038929", "taxon_label": "Streptomyces xinghaiensis S187"}, "logical_row":
    1017}, {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id":
    "NCBITaxon:1042877", "taxon_label": "Thermococcus sp. 4557"}, "logical_row": 1018},
    {"data": {"corroborated_by": "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1045558",
    "taxon_label": "Neptunomonas qingdaonensis"}, "logical_row": 1019}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1048", "taxon_label":
    "marichromatium_gracile"}, "logical_row": 1020}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:03000033", "taxon_id": "NCBITaxon:1048221", "taxon_label":
    "Mucilaginibacter litoreus"}, "logical_row": 1021}], "data/raw/madin_habitats.tsv":
    [{"data": {"label": "marine sediment", "madin_id": "ENVO:03000033", "taxon_count":
    "837", "vocabulary": "ENVO"}, "logical_row": 10}], "data/raw/ontology_subclass_edges.tsv":
    [{"data": {"object": "ENVO:00002007", "predicate": "rdfs:subClassOf", "subject":
    "ENVO:03000033"}, "logical_row": 7974}], "data/raw/ontology_terms.tsv": [{"data":
    {"definition": "Sediment which has been transported through the marine water column,
    settling on the seafloor.", "deprecated": "", "directly_referenced": "TRUE", "label":
    "marine sediment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "marine
    sediments", "term_id": "ENVO:03000033"}, "logical_row": 9583}]}'
  accessed_at: '2026-10-12T05:40:53.189655Z'
  support: supports
  locator: Exact logical TSV rows, header=row1; filtered by current source IDs and
    exact paths, not legacy issue line numbers
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:03000033", "mapping_predicate": null, "reviewed":
    false, "route": "environments_table_self_grounded"}, "automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "EXACT", "identifier": "ENVO:03000033", "mapping_predicate":
    null, "reviewed": false, "route": "environments_table_self_grounded"}, "minted":
    "habitatmech:ENVIRONMENTS_TABLE.712afe5b2b", "source": "ENVIRONMENTS_TABLE", "source_id":
    "sediment_marine"}, {"actual": {"category": null, "contributes_grounding": true,
    "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:03000033", "mapping_predicate": "skos:exactMatch",
    "reviewed": false, "route": "gold_composed_label"}, "automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "EXACT", "identifier": "ENVO:03000033", "mapping_predicate":
    "skos:exactMatch", "reviewed": false, "route": "gold_composed_label"}, "minted":
    "habitatmech:GOLD.da51ff29f9", "source": "GOLD", "source_id": "gold.ecosystem:4563"},
    {"actual": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier":
    "ENVO:03000033", "mapping_predicate": null, "reviewed": false, "route": "madin_self_grounded"},
    "automatic": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier":
    "ENVO:03000033", "mapping_predicate": null, "reviewed": false, "route": "madin_self_grounded"},
    "minted": "habitatmech:MADIN.b94291a1ab", "source": "MADIN", "source_id": "ENVO:03000033"}],
    "source_concepts": 3}'
  accessed_at: '2026-10-12T05:40:53.189655Z'
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
    []}}, "ENVO:00002007": {"definitions": ["Particulate environmental material which
    is formed as a result of the transport and deposition of particles by flowing
    liquid."], "deprecated": [], "equivalents": [], "labels": ["sediment"], "parents":
    ["http://purl.obolibrary.org/obo/ENVO_01000060", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0000086"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/PATO_0000984"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym":
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
    "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:03000033": {"definitions":
    ["Sediment which has been transported through the marine water column, settling
    on the seafloor."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#unionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002007"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"nested": true}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"],
    "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    ["http://purl.obolibrary.org/obo/ENVO_00002007"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest":
    [{"nested": true}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}],
    "labels": ["marine sediment"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002007",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002220"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00001999"]},
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002353"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_03000036"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["marine
    sediments"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}}'
  accessed_at: '2026-10-12T05:20:26.560054Z'
  support: supports
  locator: Official OWL retrieved 12-Oct; labels, definitions, typed synonyms, named
    parents and restrictions; no snapshot refresh
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats/terrestrial/sediment.yaml; data/habitats/aquatic/marine_water_body.yaml;
    data/habitats/aquatic/lentic_water_body.yaml; data/habitats/aquatic/water_body.yaml;
    data/habitats/aquatic/aquatic_biome.yaml; data/habitats/other/environmental.yaml;
    data/habitats/other/environmental_system.yaml; data/habitats/other/biome.yaml
  summary: '{"ENVO:00000063": {"definition": "An accumulation of water of varying
    size.", "grounding_status": "EXACT", "label": "water body", "parent_habitats":
    ["ENVO:01000685"]}, "ENVO:00000428": {"definition": "A biome is an ecosystem which
    is undergoing climactic ecological succession.", "grounding_status": "EXACT",
    "label": "biome", "parent_habitats": ["ENVO:01000813", "ENVO:01001110"]}, "ENVO:00001999":
    {"definition": "A lentic water body which is composed primarily of marine water.",
    "grounding_status": "EXACT", "label": "marine water body", "parent_habitats":
    ["ENVO:00002030", "ENVO:01000617"]}, "ENVO:00002007": {"definition": "Particulate
    environmental material which is formed as a result of the transport and deposition
    of particles by flowing liquid.", "grounding_status": "EXACT", "label": "sediment",
    "parent_habitats": ["ENVO:01000060"]}, "ENVO:00002030": {"definition": "A biome
    which is determined by a water body and which has ecological climax communities
    adapted to life in or on water.", "grounding_status": "EXACT", "label": "aquatic
    biome", "parent_habitats": ["ENVO:00000428", "ENVO:01001787", "habitatmech:BACDIVE.0f1e92a02c"]},
    "ENVO:01000254": {"definition": "A system which has the disposition to environ
    one or more material entities.", "grounding_status": "EXACT", "label": "environmental
    system", "parent_habitats": null}, "ENVO:01000617": {"definition": "A lentic water
    body is a water body in which the accumulated water, in its totality, has very
    little to no directed flow.", "grounding_status": "EXACT", "label": "lentic water
    body", "parent_habitats": ["ENVO:00000063"]}, "habitatmech:BACDIVE.0f1e92a02c":
    {"definition": "An environmental system which is a portion of the air, water,
    or land surface or subsurface of an astronomical body sampled in place, and which
    is neither bounded by a host organism nor constituted by a constructed or operated
    artefact.", "grounding_status": "UNGROUNDED", "label": "free-living environment",
    "parent_habitats": ["ENVO:01000254"]}}'
  accessed_at: '2026-10-12T05:40:53.189655Z'
  support: supports
  locator: Ancestor context adds no full-record coverage
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  summary: 'Exact positional census counts={"Biosample": 1192, "Organism": 958, "SequencingProject":
    1667}; individually inspected descriptions={"Biosample": [{"data": {"BIOSAMPLE
    GOLD ID": "Gb0055052", "BIOSAMPLE NAME": "Enriched marine sediment ecosystem from
    Crete, Greece ", "BIOSAMPLE NCBI TAX NAME": "marine sediment metagenome", "BIOSAMPLE
    SAMPLE COLLECTION SITE": "Crete, Greece"}, "row": 3138}, {"data": {"BIOSAMPLE
    GOLD ID": "Gb0112951", "BIOSAMPLE NAME": "Trench sediment microbial communities
    from the deep Pacific Ocean", "BIOSAMPLE NCBI TAX NAME": "marine sediment metagenome",
    "BIOSAMPLE SAMPLE COLLECTION SITE": "Deep-Sea Trench"}, "row": 7504}, {"data":
    {"BIOSAMPLE GOLD ID": "Gb0136900", "BIOSAMPLE NAME": "Deep sea sediment microbial
    communities from the Gulf of Mexico - control with no oil added", "BIOSAMPLE NCBI
    TAX NAME": "sediment metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Deepsea
    sediment of the Gulf of Mexico"}, "row": 12727}], "Organism": [{"data": {"ORGANISM
    GOLD ID": "Go0000056", "ORGANISM HABITAT": "Marine|Sediment", "ORGANISM NAME":
    "Shewanella sediminis HAW-EB3", "ORGANISM SAMPLE COLLECTION SITE": "Sediment at
    depth of 215m from an unexploded-ordinance-dumping site at Halifax"}, "row": 51},
    {"data": {"ORGANISM GOLD ID": "Go0000182", "ORGANISM HABITAT": "Sediment|Fresh
    water", "ORGANISM NAME": "Desulforamulus reducens MI-1", "ORGANISM SAMPLE COLLECTION
    SITE": "Heavy metal-contaminated sediment collected at the Mare Island Naval Shipyard
    on the San Francisco Bay"}, "row": 173}, {"data": {"ORGANISM GOLD ID": "Go0003229",
    "ORGANISM HABITAT": "Marine|Sediment|Surface water", "ORGANISM NAME": "Luminiphilus
    syltensis NOR5-1B", "ORGANISM SAMPLE COLLECTION SITE": "top oxic layer of a muddy
    sediment core, List, Sylt (55002''N, 8024''E) Germany, 19.10.2005"}, "row": 2843}]}.
    These later examples may include mixed sample/host/enrichment contexts; they do
    not reconstruct original assertion membership. Remaining members and study joins
    were indexed, not individually assessed.'
  accessed_at: '2026-10-11T13:21:51.155056Z'
  support: supports
  locator: Five-position ecosystem paths preserved; contacts excluded; first 3 BioSample
    and Organism descriptions per target
  snapshot_sha256: b222fa9df89ffbd1a30897a1e7302da363c57b463d9948ecc9bfcb9304b4a96f
- evidence_id: CLASS
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  summary: '[{"row": 794, "slug": "marine_sediment", "path": "Environmental > Aquatic
    > Marine > Sediment", "values": ["4564", "Environmental", "Aquatic", "Marine",
    "Sediment", "Unclassified"]}]'
  accessed_at: '2026-10-12T05:20:29.451803Z'
  support: supports
  locator: Later official classification; 29 of 31 cohort paths matched; missing tuples
    do not establish nonexistence
  snapshot_sha256: 78ed6ce1c3799a2d6ef2d17e4a9eeee5da48eef78df0b71079c0f942555e5e7d
- evidence_id: TAX0
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1000566%2C1003110%2C1005925%2C1005926%2C1005928%2C1006%2C1007105%2C1007109%2C1007110%2C1007111%2C1007112%2C1007113%2C1007114%2C1007115%2C1007116%2C1007117%2C1007118%2C1007119%2C1007120%2C1007122%2C1007124%2C1009412%2C1009413%2C1009414%2C1009415%2C1009416%2C1009418%2C1009419%2C1009420%2C1009421%2C1017277%2C102%2C1026%2C1027373%2C1027374%2C1028566%2C1028742%2C1028743%2C1028745%2C1028746%2C1028749%2C1028752%2C1031273%2C1031541%2C103810%2C1038845%2C1038928%2C1038929%2C1042%2C104268%2C104270%2C1042877%2C1044%2C104421%2C1045558%2C1048%2C1048221%2C1057%2C106299%2C1074%2C107401%2C1080%2C1089550%2C109263%2C1094980%2C110163%2C1104565%2C1104566%2C110662%2C110663%2C111770%2C1121404%2C1121937%2C1121948%2C1122607%2C1123059%2C1123242%2C1123275%2C114404%2C1150474%2C119394%2C119542%2C1208324%2C1211807%2C121224%2C1217908%2C1219067%2C1242148%2C1246444%2C1246460%2C1265%2C126741%2C1267768%2C1267769%2C1276246%2C1282%2C129958%2C132144%2C133924%2C134561%2C1358%2C13616%2C13686%2C1371%2C1387275%2C139239%2C1394%2C1411902%2C143223%2C143224%2C147%2C1486246%2C150120%2C1543721%2C156%2C156128%2C156133%2C1570%2C158080%2C158192%2C158500%2C1609977%2C161528%2C163248%2C163503%2C168275%2C168759%2C1703256%2C1716143%2C172371%2C173%2C173365%2C173737%2C173764%2C174%2C174302%2C174315%2C1774373%2C179326%2C180542%2C1808508%2C1808945%2C1817405%2C1836499%2C184592%2C184914%2C1855%2C186022%2C1869227%2C1871328&retmode=xml
  summary: 'The three chunks jointly resolve all 346 requested cohort IDs. Target
    results=[{"current_id": "1003110", "current_name": "Micromonospora maris", "frozen_label":
    "verrucosispora_maris", "id": "1003110", "rank": "species"}, {"current_id": "1005925",
    "current_name": "Kordiimonas aestuarii", "frozen_label": "Kordiimonas aestuarii",
    "id": "1005925", "rank": "species"}, {"current_id": "1005926", "current_name":
    "Flagellimonas taeanensis", "frozen_label": "Muricauda taeanensis", "id": "1005926",
    "rank": "species"}, {"current_id": "1005928", "current_name": "Roseovarius lutimaris",
    "frozen_label": "roseovarius_lutimaris", "id": "1005928", "rank": "species"},
    {"current_id": "1006", "current_name": "Marivirga tractuosa", "frozen_label":
    "flexibacter_tractuosus", "id": "1006", "rank": "species"}, {"current_id": "1007105",
    "current_name": "Pusillimonas sp. T7-7", "frozen_label": "Pusillimonas sp. T7-7",
    "id": "1007105", "rank": "species"}, {"current_id": "296995", "current_name":
    "Exiguobacterium indicum", "frozen_label": "exiguobacterium_enclense", "id": "1017277",
    "rank": "species"}, {"current_id": "1027373", "current_name": "Nitrosopumilus
    sp. AR", "frozen_label": "Nitrosopumilus sp. AR", "id": "1027373", "rank": "species"},
    {"current_id": "1027374", "current_name": "Nitrosopumilus sp. SJ", "frozen_label":
    "Nitrosopumilus sp. SJ", "id": "1027374", "rank": "species"}, {"current_id": "1028566",
    "current_name": "Sulfolobus acidocaldarius N8", "frozen_label": "Sulfolobus acidocaldarius
    N8", "id": "1028566", "rank": "strain"}, {"current_id": "1028742", "current_name":
    "Pontixanthobacter gangjinensis", "frozen_label": "Altererythrobacter gangjinensis",
    "id": "1028742", "rank": "species"}, {"current_id": "1028743", "current_name":
    "Arenibacter hampyeongensis", "frozen_label": "Arenibacter hampyeongensis", "id":
    "1028743", "rank": "species"}, {"current_id": "1028745", "current_name": "Aestuariibaculum
    suncheonense", "frozen_label": "Aestuariibaculum suncheonense", "id": "1028745",
    "rank": "species"}, {"current_id": "1028746", "current_name": "Christiangramia
    aestuarii", "frozen_label": "Gramella aestuarii", "id": "1028746", "rank": "species"},
    {"current_id": "1028749", "current_name": "Microbulbifer gwangyangensis", "frozen_label":
    "Microbulbifer gwangyangensis", "id": "1028749", "rank": "species"}, {"current_id":
    "1028752", "current_name": "Shewanella aestuarii", "frozen_label": "Shewanella
    aestuarii", "id": "1028752", "rank": "species"}, {"current_id": "1031273", "current_name":
    "Gaetbulibacter lutimaris", "frozen_label": "Gaetbulibacter lutimaris", "id":
    "1031273", "rank": "species"}, {"current_id": "1031541", "current_name": "Tropicimonas
    sediminicola", "frozen_label": "tropicimonas_sediminicola", "id": "1031541", "rank":
    "species"}, {"current_id": "1038845", "current_name": "Flavobacterium rakeshii",
    "frozen_label": "flavobacterium_rakeshii", "id": "1038845", "rank": "species"},
    {"current_id": "1038928", "current_name": "Streptomyces xinghaiensis", "frozen_label":
    "streptomyces_xinghaiensis", "id": "1038928", "rank": "species"}, {"current_id":
    "1038929", "current_name": "Streptomyces xinghaiensis S187", "frozen_label": "Streptomyces
    xinghaiensis S187", "id": "1038929", "rank": "strain"}, {"current_id": "1042877",
    "current_name": "Thermococcus sp. 4557", "frozen_label": "Thermococcus sp. 4557",
    "id": "1042877", "rank": "species"}, {"current_id": "1045558", "current_name":
    "Neptunomonas qingdaonensis", "frozen_label": "Neptunomonas qingdaonensis", "id":
    "1045558", "rank": "species"}, {"current_id": "1048", "current_name": "Marichromatium
    gracile", "frozen_label": "marichromatium_gracile", "id": "1048", "rank": "species"},
    {"current_id": "1048221", "current_name": "Mucilaginibacter litoreus", "frozen_label":
    "Mucilaginibacter litoreus", "id": "1048221", "rank": "species"}]. Alias/name
    resolution does not establish habitat occurrence.'
  accessed_at: '2026-10-12T05:21:31.882540Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: 47eba2c6c7ff47d6263796c3afdcff6e39319e77b443b6200d469773ef5ff403
- evidence_id: TAX1
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1872627%2C1876%2C188906%2C188908%2C1903071%2C190308%2C191302%2C1926630%2C1931%2C195064%2C1961642%2C197222%2C198804%2C2%2C200617%2C2022602%2C2024855%2C203122%2C203907%2C205920%2C2099376%2C212050%2C214688%2C214988%2C216432%2C216773%2C2183988%2C2213%2C223788%2C224915%2C225345%2C225937%2C226126%2C2264%2C234267%2C240016%2C2423%2C243090%2C247026%2C257363%2C264%2C264462%2C264951%2C265606%2C266940%2C2738566%2C28108%2C28122%2C28181%2C28223%2C28251%2C28258%2C28262%2C29158%2C29159%2C2926447%2C29292%2C293614%2C29805%2C302409%2C3055%2C3068%2C31330%2C313595%2C313603%2C313606%2C314230%2C314275%2C316279%2C319225%2C320388%2C332415%2C337701%2C339861%2C340047%2C34085%2C344747%2C357244%2C35743%2C35845%2C358766%2C361576%2C36870%2C36987%2C372461%2C378806%2C379066%2C39152%2C391625%2C39947%2C402880%2C40464%2C406538%2C406540%2C411477%2C411485%2C419481%2C425006%2C428125%2C435805%2C43928%2C442956%2C443152%2C445336%2C44751%2C45351%2C457427%2C463619%2C46539%2C466153%2C46687%2C46704%2C46745%2C472759%2C483407%2C483417%2C48499%2C48729%2C491952%2C49447%2C498761%2C502025%2C504472%2C50741%2C515618%2C51671%2C518766%2C523849%2C530564%2C53249%2C537937%2C53953%2C55518%2C555512%2C55567%2C562%2C563043%2C56780%2C56811%2C57043%2C575540%2C583355%2C585501%2C595452%2C595453%2C59919%2C59920%2C6047%2C60480%2C6087&retmode=xml
  summary: 'The three chunks jointly resolve all 346 requested cohort IDs. Target
    results=[{"current_id": "1003110", "current_name": "Micromonospora maris", "frozen_label":
    "verrucosispora_maris", "id": "1003110", "rank": "species"}, {"current_id": "1005925",
    "current_name": "Kordiimonas aestuarii", "frozen_label": "Kordiimonas aestuarii",
    "id": "1005925", "rank": "species"}, {"current_id": "1005926", "current_name":
    "Flagellimonas taeanensis", "frozen_label": "Muricauda taeanensis", "id": "1005926",
    "rank": "species"}, {"current_id": "1005928", "current_name": "Roseovarius lutimaris",
    "frozen_label": "roseovarius_lutimaris", "id": "1005928", "rank": "species"},
    {"current_id": "1006", "current_name": "Marivirga tractuosa", "frozen_label":
    "flexibacter_tractuosus", "id": "1006", "rank": "species"}, {"current_id": "1007105",
    "current_name": "Pusillimonas sp. T7-7", "frozen_label": "Pusillimonas sp. T7-7",
    "id": "1007105", "rank": "species"}, {"current_id": "296995", "current_name":
    "Exiguobacterium indicum", "frozen_label": "exiguobacterium_enclense", "id": "1017277",
    "rank": "species"}, {"current_id": "1027373", "current_name": "Nitrosopumilus
    sp. AR", "frozen_label": "Nitrosopumilus sp. AR", "id": "1027373", "rank": "species"},
    {"current_id": "1027374", "current_name": "Nitrosopumilus sp. SJ", "frozen_label":
    "Nitrosopumilus sp. SJ", "id": "1027374", "rank": "species"}, {"current_id": "1028566",
    "current_name": "Sulfolobus acidocaldarius N8", "frozen_label": "Sulfolobus acidocaldarius
    N8", "id": "1028566", "rank": "strain"}, {"current_id": "1028742", "current_name":
    "Pontixanthobacter gangjinensis", "frozen_label": "Altererythrobacter gangjinensis",
    "id": "1028742", "rank": "species"}, {"current_id": "1028743", "current_name":
    "Arenibacter hampyeongensis", "frozen_label": "Arenibacter hampyeongensis", "id":
    "1028743", "rank": "species"}, {"current_id": "1028745", "current_name": "Aestuariibaculum
    suncheonense", "frozen_label": "Aestuariibaculum suncheonense", "id": "1028745",
    "rank": "species"}, {"current_id": "1028746", "current_name": "Christiangramia
    aestuarii", "frozen_label": "Gramella aestuarii", "id": "1028746", "rank": "species"},
    {"current_id": "1028749", "current_name": "Microbulbifer gwangyangensis", "frozen_label":
    "Microbulbifer gwangyangensis", "id": "1028749", "rank": "species"}, {"current_id":
    "1028752", "current_name": "Shewanella aestuarii", "frozen_label": "Shewanella
    aestuarii", "id": "1028752", "rank": "species"}, {"current_id": "1031273", "current_name":
    "Gaetbulibacter lutimaris", "frozen_label": "Gaetbulibacter lutimaris", "id":
    "1031273", "rank": "species"}, {"current_id": "1031541", "current_name": "Tropicimonas
    sediminicola", "frozen_label": "tropicimonas_sediminicola", "id": "1031541", "rank":
    "species"}, {"current_id": "1038845", "current_name": "Flavobacterium rakeshii",
    "frozen_label": "flavobacterium_rakeshii", "id": "1038845", "rank": "species"},
    {"current_id": "1038928", "current_name": "Streptomyces xinghaiensis", "frozen_label":
    "streptomyces_xinghaiensis", "id": "1038928", "rank": "species"}, {"current_id":
    "1038929", "current_name": "Streptomyces xinghaiensis S187", "frozen_label": "Streptomyces
    xinghaiensis S187", "id": "1038929", "rank": "strain"}, {"current_id": "1042877",
    "current_name": "Thermococcus sp. 4557", "frozen_label": "Thermococcus sp. 4557",
    "id": "1042877", "rank": "species"}, {"current_id": "1045558", "current_name":
    "Neptunomonas qingdaonensis", "frozen_label": "Neptunomonas qingdaonensis", "id":
    "1045558", "rank": "species"}, {"current_id": "1048", "current_name": "Marichromatium
    gracile", "frozen_label": "marichromatium_gracile", "id": "1048", "rank": "species"},
    {"current_id": "1048221", "current_name": "Mucilaginibacter litoreus", "frozen_label":
    "Mucilaginibacter litoreus", "id": "1048221", "rank": "species"}]. Alias/name
    resolution does not establish habitat occurrence.'
  accessed_at: '2026-10-12T05:21:33.762356Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank, AkaTaxIds and OtherNames
  snapshot_sha256: 211e97ebc927aae4966a064aa1db888cc9672558b906b2333d2088bb0c5b87fb
- evidence_id: TAX2
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=610380%2C6182%2C6238%2C6334%2C639602%2C641112%2C6613%2C6669%2C688066%2C69293%2C6945%2C69773%2C7029%2C703612%2C7070%2C7159%2C7209%2C7425%2C74546%2C74547%2C748449%2C756272%2C758583%2C75883%2C760154%2C765912%2C7668%2C76775%2C7719%2C777%2C7955%2C80836%2C8090%2C83428%2C86104%2C880%2C880447%2C885%2C89184%2C9031%2C91360%2C9258%2C939306%2C939316%2C939324%2C939346&retmode=xml
  summary: 'The three chunks jointly resolve all 346 requested cohort IDs. Target
    results=[{"current_id": "1003110", "current_name": "Micromonospora maris", "frozen_label":
    "verrucosispora_maris", "id": "1003110", "rank": "species"}, {"current_id": "1005925",
    "current_name": "Kordiimonas aestuarii", "frozen_label": "Kordiimonas aestuarii",
    "id": "1005925", "rank": "species"}, {"current_id": "1005926", "current_name":
    "Flagellimonas taeanensis", "frozen_label": "Muricauda taeanensis", "id": "1005926",
    "rank": "species"}, {"current_id": "1005928", "current_name": "Roseovarius lutimaris",
    "frozen_label": "roseovarius_lutimaris", "id": "1005928", "rank": "species"},
    {"current_id": "1006", "current_name": "Marivirga tractuosa", "frozen_label":
    "flexibacter_tractuosus", "id": "1006", "rank": "species"}, {"current_id": "1007105",
    "current_name": "Pusillimonas sp. T7-7", "frozen_label": "Pusillimonas sp. T7-7",
    "id": "1007105", "rank": "species"}, {"current_id": "296995", "current_name":
    "Exiguobacterium indicum", "frozen_label": "exiguobacterium_enclense", "id": "1017277",
    "rank": "species"}, {"current_id": "1027373", "current_name": "Nitrosopumilus
    sp. AR", "frozen_label": "Nitrosopumilus sp. AR", "id": "1027373", "rank": "species"},
    {"current_id": "1027374", "current_name": "Nitrosopumilus sp. SJ", "frozen_label":
    "Nitrosopumilus sp. SJ", "id": "1027374", "rank": "species"}, {"current_id": "1028566",
    "current_name": "Sulfolobus acidocaldarius N8", "frozen_label": "Sulfolobus acidocaldarius
    N8", "id": "1028566", "rank": "strain"}, {"current_id": "1028742", "current_name":
    "Pontixanthobacter gangjinensis", "frozen_label": "Altererythrobacter gangjinensis",
    "id": "1028742", "rank": "species"}, {"current_id": "1028743", "current_name":
    "Arenibacter hampyeongensis", "frozen_label": "Arenibacter hampyeongensis", "id":
    "1028743", "rank": "species"}, {"current_id": "1028745", "current_name": "Aestuariibaculum
    suncheonense", "frozen_label": "Aestuariibaculum suncheonense", "id": "1028745",
    "rank": "species"}, {"current_id": "1028746", "current_name": "Christiangramia
    aestuarii", "frozen_label": "Gramella aestuarii", "id": "1028746", "rank": "species"},
    {"current_id": "1028749", "current_name": "Microbulbifer gwangyangensis", "frozen_label":
    "Microbulbifer gwangyangensis", "id": "1028749", "rank": "species"}, {"current_id":
    "1028752", "current_name": "Shewanella aestuarii", "frozen_label": "Shewanella
    aestuarii", "id": "1028752", "rank": "species"}, {"current_id": "1031273", "current_name":
    "Gaetbulibacter lutimaris", "frozen_label": "Gaetbulibacter lutimaris", "id":
    "1031273", "rank": "species"}, {"current_id": "1031541", "current_name": "Tropicimonas
    sediminicola", "frozen_label": "tropicimonas_sediminicola", "id": "1031541", "rank":
    "species"}, {"current_id": "1038845", "current_name": "Flavobacterium rakeshii",
    "frozen_label": "flavobacterium_rakeshii", "id": "1038845", "rank": "species"},
    {"current_id": "1038928", "current_name": "Streptomyces xinghaiensis", "frozen_label":
    "streptomyces_xinghaiensis", "id": "1038928", "rank": "species"}, {"current_id":
    "1038929", "current_name": "Streptomyces xinghaiensis S187", "frozen_label": "Streptomyces
    xinghaiensis S187", "id": "1038929", "rank": "strain"}, {"current_id": "1042877",
    "current_name": "Thermococcus sp. 4557", "frozen_label": "Thermococcus sp. 4557",
    "id": "1042877", "rank": "species"}, {"current_id": "1045558", "current_name":
    "Neptunomonas qingdaonensis", "frozen_label": "Neptunomonas qingdaonensis", "id":
    "1045558", "rank": "species"}, {"current_id": "1048", "current_name": "Marichromatium
    gracile", "frozen_label": "marichromatium_gracile", "id": "1048", "rank": "species"},
    {"current_id": "1048221", "current_name": "Mucilaginibacter litoreus", "frozen_label":
    "Mucilaginibacter litoreus", "id": "1048221", "rank": "species"}]. Alias/name
    resolution does not establish habitat occurrence.'
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
  accessed_at: '2026-10-12T05:40:53.189655Z'
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
  accessed_at: '2026-10-12T05:40:53.189655Z'
  support: supports
  locator: GitHub CLI inventory retrieved 12-Oct
- evidence_id: GRAPH
  kind: record_content
  reference: curation/causal_graphs/marine_sediment.yaml
  summary: Entire overlay and generated graph read, including all node types, edge
    descriptions, evidence and preserved historical events.
  accessed_at: '2026-10-12T05:40:53.189655Z'
  support: supports
  locator: Current full overlay
- evidence_id: DHONDT
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6684631/fullTextXML
  summary: Oxic exceptions, burial and overlapping respiratory processes.
  accessed_at: '2026-10-12T05:29:53.833765Z'
  support: supports
  locator: PMID:31388058; Introduction/Fig1 and Box1
  snapshot_sha256: 9150a3527672b3c313985a20e204276f65a20149844662ef5283d5deb25dd42c
- evidence_id: JORGENSEN
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6492693/fullTextXML
  summary: Conditional sulfate supply, carbon oxidation, sulfide oxidation and iron-sulfide
    sinks.
  accessed_at: '2026-10-12T05:30:01.872870Z'
  support: supports
  locator: PMID:31105660; Introduction/Fig1 and Organic Matter Degradation
  snapshot_sha256: 8d83308c4d20591add11a0e7f3f5b29a9bf325a9e2fed8dfc171e41908c2ebf8
- evidence_id: WASMUND
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5573963/fullTextXML
  summary: Polyphyletic sulfur guilds and coupled redox transformations. The exact
    snippet marine sediment sulfur cycling was searched across all XML text with whitespace
    normalized and was not found; the Introduction still supports sulfate-to-sulfide
    conversion.
  accessed_at: '2026-10-12T05:30:09.037919Z'
  support: supports
  locator: PMID:28419734; Introduction and Sulfate-Reducing Microorganisms
  snapshot_sha256: f5468cad4ff1844cb35a31e966b2e7e941fbf25759bc563cf3e0c348d3259e67
- evidence_id: NAGAKURA
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8927301/fullTextXML
  summary: Guaymas sediment context and sulfate-reduction pathways, not universal
    exclusion of other respiration.
  accessed_at: '2026-10-12T05:30:11.318785Z'
  support: supports
  locator: PMID:35308366; Introduction
  snapshot_sha256: 8c455e1eeeed0fc30eaea5c2664604daf04b1ee9b7b21e422a1db610acc6b042
- evidence_id: LIN
  kind: primary_source
  reference: https://api.repository.cam.ac.uk/server/api/core/bitstreams/da5d036c-2344-4ffc-8494-216f2fee4429/content
  summary: Clay-surface experiments support altered sulfate-reduction rates, not the
    asserted iron trapping mechanism.
  accessed_at: '2026-10-12T05:30:19.430876Z'
  support: supports
  locator: DOI:10.1016/j.epsl.2022.117841; Abstract, Results3.2 and Discussion pp6-9
  snapshot_sha256: 50606a86547fbaac3b984c4725515e5de5267626d826f4d02f594e5c410d97ca
- evidence_id: IMODULONDB
  kind: database
  reference: iModulonDB via kg-microbe-sources
  summary: '{"command": ["../../culturebotai-claw/.venv/bin/kg-microbe-sources", "imodulondb",
    "datasets"], "started_at": "2026-10-12T05:22:18.796436+00:00", "finished_at":
    "2026-10-12T05:22:19.723730+00:00", "exit_code": 0, "path": "/private/tmp/habitatmech-review-bc-imodulondb-datasets.source",
    "sha256": "1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549",
    "stderr": ""}'
  accessed_at: '2026-10-12T05:40:53.189655Z'
  support: supports
  locator: Actual 28-dataset inventory inspected; no covered claim-specific strain/gene
    or expression module in this generic guild graph warrants a search/component query
assessments:
- assessment_id: EDGE-marine_sediment_receives_particles
  area: evidence
  topic: marine_sediment_receives_particles
  outcome: supported
  summary: Deposition and burial context are supported by D'Hondt introduction and
    Box1; no universal anoxia follows.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-particles_bury_marine_organic_matter
  area: evidence
  topic: particles_bury_marine_organic_matter
  outcome: supported
  summary: D'Hondt introduction and Box1 support organic-particle burial; this is
    not the fate of every particle.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-buried_organic_matter_depletes_oxygen
  area: evidence
  topic: buried_organic_matter_depletes_oxygen
  outcome: supported
  summary: Jorgensen introduction supports aerobic carbon oxidation as an oxygen sink;
    depletion depends on supply.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-oxygen_depletion_creates_anoxic_porewater
  area: evidence
  topic: oxygen_depletion_creates_anoxic_porewater
  outcome: concern
  summary: D'Hondt introduction/Fig1 expressly includes fully oxic sediment columns;
    rapid universal depletion is contradicted.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-seawater_supplies_sulfate
  area: evidence
  topic: seawater_supplies_sulfate
  outcome: supported
  summary: Jorgensen Organic Matter Degradation describes sulfate transport from overlying
    seawater.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-sulfate_selects_sulfate_reducers
  area: evidence
  topic: sulfate_selects_sulfate_reducers
  outcome: supported
  summary: Wasmund introduction/Sulfate-Reducing Microorganisms supports sulfate-respiring
    guilds, with donor and temperature dependence.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-anoxic_porewater_enables_sulfate_reduction
  area: evidence
  topic: anoxic_porewater_enables_sulfate_reduction
  outcome: concern
  summary: Nagakura concerns Guaymas sediments; D'Hondt Box1 and Jorgensen zonation
    discussion contradict strict mutual exclusion.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-sulfate_reducers_perform_sulfate_reduction
  area: evidence
  topic: sulfate_reducers_perform_sulfate_reduction
  outcome: supported
  summary: Wasmund Sulfate-Reducing Microorganisms supports coupled substrate oxidation
    and sulfate respiration; hydrogen is another donor.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-sulfate_reduction_mineralizes_carbon
  area: evidence
  topic: sulfate_reduction_mineralizes_carbon
  outcome: supported
  summary: Jorgensen introduction describes coupled organic-carbon oxidation and sulfate
    reduction; carbon becomes inorganic carbon, not sulfide.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-sulfate_reduction_produces_sulfide
  area: evidence
  topic: sulfate_reduction_produces_sulfide
  outcome: concern
  summary: Wasmund introduction supports sulfate-to-sulfide conversion, but the supplied
    snippet is absent from whitespace-normalized complete XML.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-sulfide_selects_sulfur_oxidizers
  area: evidence
  topic: sulfide_selects_sulfur_oxidizers
  outcome: supported
  summary: Jorgensen introduction/Fig1 supports conditional sulfide oxidation with
    oxidants; it is not a quantified selection experiment.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-sulfur_oxidizers_perform_sulfide_oxidation
  area: evidence
  topic: sulfur_oxidizers_perform_sulfide_oxidation
  outcome: supported
  summary: Wasmund introduction and sulfur-oxidizer account support biological sulfur
    oxidation without assigning all flux to microbes.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-reactive_iron_traps_sulfide
  area: evidence
  topic: reactive_iron_traps_sulfide
  outcome: concern
  summary: Lin Results3.2/Discussion concern mineral surfaces and sulfate-reduction
    rates, not this trapping reaction; Jorgensen introduction supports the chemistry.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: EDGE-sulfide_reaction_forms_iron_sulfides
  area: evidence
  topic: sulfide_reaction_forms_iron_sulfides
  outcome: supported
  summary: Jorgensen introduction/Fig1 supports precipitation of reduced sulfur with
    iron; other sulfide fates remain possible.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
- assessment_id: IDENTITY
  area: identity
  topic: Exact identity, definition and source intent
  outcome: supported
  summary: Marine sediment is deposited particulate material, not a whole marine water
    body. Preserve sediment ancestry, 1035 GOLD ORGANISM assertions, the 837-member
    Madin taxon pool, 25 displayed associations and seven source-attributed qualitative
    parameter bands. The 14-edge sulfur graph needs conditional redox scope, claim-specific
    evidence, correct carbon/sulfur wording and truthful node types; taxonomic aliases
    also need versioned maintenance.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
- assessment_id: HIERARCHY
  area: grounding
  topic: Parent contributors and mapping endpoints
  outcome: concern
  summary: Marine sediment is deposited particulate material, not a whole marine water
    body. Preserve sediment ancestry, 1035 GOLD ORGANISM assertions, the 837-member
    Madin taxon pool, 25 displayed associations and seven source-attributed qualitative
    parameter bands. The 14-edge sulfur graph needs conditional redox scope, claim-specific
    evidence, correct carbon/sulfur wording and truthful node types; taxonomic aliases
    also need versioned maintenance. Ontology, GOLD path, ambiguous-leaf and authored-genus
    routes were distinguished.
  target_ids:
  - ENVO:03000033
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
  summary: 'Complete reconstruction preserves 3 contributing concepts and 0 ITEM-reviewed
    contributors. Attestations=[{"source": "ENVIRONMENTS_TABLE", "source_id": "sediment_marine",
    "source_label": "sediment_marine", "notes": "Physicochemical parameter bands from
    kg-microbe''s environment table."}, {"source": "GOLD", "source_id": "gold.ecosystem:4563",
    "source_label": "Sediment", "source_path": "Environmental > Aquatic > Marine >
    Sediment", "mapping_predicate": "skos:exactMatch", "assertion_count": 1035, "assertion_unit":
    "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown.
    See data/raw/gold_ecosystem_paths.tsv."}, {"source": "MADIN", "source_id": "ENVO:03000033",
    "source_label": "marine sediment", "assertion_count": 837, "assertion_unit": "TAXON"}].
    Counts with different units are not summed. Reproduction validates derivation,
    not the scientific truth of the mapping.'
  target_ids:
  - ENVO:03000033
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
    so no claim of exhaustive ecological validation is made. 1017277 resolves to 296995
    Exiguobacterium indicum; six historical name combinations have current synonyms
    and five further labels differ only in formatting
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - R
  - RAW
  - TAX0
  - TAX1
  - TAX2
  - RULES
- assessment_id: PARAMETERS
  area: evidence
  topic: Qualitative bands and triad roles
  outcome: supported
  summary: All 7 source-attributed single-term parameter bands reproduce. These qualitative
    descriptors are not universal measurements; multi-term rows are not applied to
    only one component. MIxS broad/local/medium context is not automatically identity.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - R
  - RAW
  - CODE
  - RULES
- assessment_id: COMPLETENESS
  area: completeness
  topic: Optional slots and bounded evidence
  outcome: supported
  summary: Optional empty fields alone are not defects. Every current graph edge has
    an individual assessment; node typing is assessed separately. Expression-module
    membership is not direct causal proof.
  target_ids:
  - ENVO:03000033
  evidence_ids:
  - R
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: envo-03000033-context-parent
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Source context is emitted as a strict superclass
  description: 'Marine sediment is deposited particulate material, not a whole marine
    water body. Preserve sediment ancestry, 1035 GOLD ORGANISM assertions, the 837-member
    Madin taxon pool, 25 displayed associations and seven source-attributed qualitative
    parameter bands. The 14-edge sulfur graph needs conditional redox scope, claim-specific
    evidence, correct carbon/sulfur wording and truthful node types; taxonomic aliases
    also need versioned maintenance. Unsupported GOLD contributions: ENVO:00001999.'
  target_ids:
  - ENVO:03000033
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
  - https://github.com/CultureBotAI/HabitatMech/issues/1293
- finding_id: F2
  issue_key: envo-03000033-taxonomy-alias-maintenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical taxonomy identifiers or names need versioned maintenance
  description: 1017277 resolves to 296995 Exiguobacterium indicum; six historical
    name combinations have current synonyms and five further labels differ only in
    formatting. The original IDs remain resolvable; this is not proof of a false habitat
    association.
  target_ids:
  - ENVO:03000033
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
    path: data/raw/madin_habitat_taxa.tsv
    role: Actual source taxon-row owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Versioned taxon normalization
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Bounded lexical, candidate-assessment or versioned taxonomy
    maintenance concern.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1295
- finding_id: F3
  issue_key: envo-03000033-sulfur-graph-scope-evidence
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The sulfur graph overgeneralizes redox scope and misplaces evidence
  description: Rapid anoxia and exhaustion of all higher-energy acceptors are overgeneralized.
    The graph summary confuses carbon oxidation with sulfate reduction to sulfide.
    Lin supports clay-linked rate effects, not iron-mineral trapping. One Wasmund
    snippet is absent from complete normalized XML; other title/topic fragments do
    not identify claim-bearing passages.
  target_ids:
  - ENVO:03000033
  field_paths:
  - causal_graphs[0].description
  - causal_graphs[0].edges
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/marine_sediment.yaml
    role: Graph scope and claim-level evidence
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material identity, strict-hierarchy, evidence or representation
    defect.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1294
- finding_id: F4
  issue_key: envo-03000033-graph-node-type-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Graph node types misrepresent habitats and functional assemblages
  description: Anoxic porewater is external habitat context, not a cellular STATE.
    Sulfate-reducing and sulfur-oxidizing assemblages are polyphyletic functional
    guilds, not one organism or clade as TAXON requires.
  target_ids:
  - ENVO:03000033
  field_paths:
  - causal_graphs[0].nodes
  evidence_ids:
  - GRAPH
  - RULES
  - DHONDT
  - JORGENSEN
  - WASMUND
  - NAGAKURA
  - LIN
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/marine_sediment.yaml
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
  - ENVO:03000033
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
  - ENVO:03000033
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
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
  description: Qualify the anoxic pathway, distinguish carbon and sulfur fates, replace
    unsupported trapping evidence with an inspected relevant source, and use exact
    short excerpts or precise locators. Preserve supported conditional mechanisms
    and stable IDs where possible.
  finding_ids:
  - F3
  target_ids:
  - ENVO:03000033
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/marine_sediment.yaml
    role: Graph scope and claim-level evidence
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained owners after source-level assessment; retain independent
    true parents, source identity/count/unit provenance and lifecycle unless a separately
    justified change requires otherwise.
  - Append required current history, add focused regressions, inspect a seed canary
    and regenerate affected products without hand-editing records or pages.
  - Pass schema, strict, label, provenance, corpus reproduction, causal/history and
    full QC gates; save a linked successor for any finding disposition.
- action_id: A4
  description: Use supported HABITAT/COMMUNITY/gene-product or process representations
    as appropriate; do not relabel ecological guilds as clades. Preserve supported
    causal meaning and recheck every affected edge.
  finding_ids:
  - F4
  target_ids:
  - ENVO:03000033
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/marine_sediment.yaml
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
