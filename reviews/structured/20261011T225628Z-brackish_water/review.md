# Scientific record review: brackish_water

- Review: 20261011T225628Z-brackish_water
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-11T22:35:45.077783Z
- Finished UTC: 2026-10-11T22:56:28.023779Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ENVO:00002019 denotes saline water material intermediate between fresh and marine water, distinct from a water body. The estuarine example graph has 17 edges; community typing and some causal extrapolations need correction, while mixing and conditional growth/residence observations are supported. Ten qualitative source bands and reported taxa remain source-specific.

## Scope And Provenance

Entire exact generated record and all contributors, with bounded claim-level scientific and source-context assessment.

Selection: Next forty unreviewed records in stable repository-relative path order: next forty AQUATIC records, atoll lagoon through coalbed methane well water. Individual full-record observations, not a category-wide pass. Starting observation coverage528/3208 is not clean current-input coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6509db458133758a41d1f39c6d41982476c3ed0d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00002019 | data/habitats/aquatic/brackish_water.yaml | generated | brackish water |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native gate on captured scientific inputs | passed | True | ENVO:00002019 | Actual success from 2026-10-11T22:38:02.546263Z to 2026-10-11T22:38:05.196951Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00002019 | Actual success from 2026-10-11T22:38:48.678016Z to 2026-10-11T22:38:56.293670Z. Native scope retained. Selected scope:40 files,0 files with ERROR,0 ERROR rows. |
| Native gate on captured scientific inputs | passed | True | ENVO:00002019 | Actual success from 2026-10-11T22:38:56.294771Z to 2026-10-11T22:39:13.326878Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00002019 | Actual success from 2026-10-11T22:39:13.327786Z to 2026-10-11T22:40:07.035407Z. Native scope retained. Recorded corpus-wide outcomes:1178 canonical,1 synonym,5 accepted exceptions,2057 SKIPPED_NO_ADAPTER. This gate does not validate minted identities or habitat occurrence. |
| Native gate on captured scientific inputs | passed | True | ENVO:00002019 | Actual success from 2026-10-11T22:40:07.036210Z to 2026-10-11T22:40:16.618000Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00002019 | Actual success from 2026-10-11T22:40:16.619117Z to 2026-10-11T22:40:22.318447Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00002019 | Actual success from 2026-10-11T22:40:22.319312Z to 2026-10-11T22:40:47.199821Z. Native scope retained. |
| Native gate on captured scientific inputs | passed | True | ENVO:00002019 | Actual success from 2026-10-11T22:38:04.444453Z to 2026-10-11T22:38:06.504418Z. All three required merge-group workflows passed at the exact captured base; authoritative QC passed 800 tests with 3 skipped. Newly saved review bundles require their own integrity check. Exact-base CI receipt; no claim that these new review files passed remote CI. |
| Complete target reconstruction | passed | False | ENVO:00002019 | All40 complete documents matched; input hashes reverified before authoring. |
| Original assertion membership | unavailable | False | ENVO:00002019 | Bounded ignored-inclusive searches did not reconstruct all original assertions. Later source exports are contextual evidence only. |
| iModulonDB applicability | not_applicable | False | ENVO:00002019 | No resolvable strain/dataset-specific expression claim in this record; expression modules would not prove habitat occurrence. |

## Scientific And Domain Assessments

### brackish_water_receives_freshwater

evidence: supported. Targets: ENVO:00002019.

Crump abstract supports freshwater advection in its estuarine example.

### brackish_water_receives_seawater

evidence: supported. Targets: ENVO:00002019.

Crump abstract supports marine advection in the same bounded setting.

### brackish_water_has_tidal_mixing

evidence: supported. Targets: ENVO:00002019.

Tee introduction supports tidal exchange in the studied lagoon.

### brackish_water_has_residence_time

evidence: supported. Targets: ENVO:00002019.

Crump abstract explicitly relates community development to residence time.

### tidal_mixing_creates_salinity_variability

evidence: supported. Targets: ENVO:00002019.

Tee introduction supports periodically changing salinity with tidal exchange.

### freshwater_seawater_mixing_sets_intermediate_salinity

evidence: supported. Targets: ENVO:00002019.

Campbell abstract supports mixing along the Delaware estuarine gradient.

### brackish_water_has_intermediate_salinity

evidence: supported. Targets: ENVO:00002019.

ENVO supplies the material definition; Campbell supplies a measured example, not a universal numerical threshold.

### intermediate_salinity_imposes_osmotic_stress

evidence: supported. Targets: ENVO:00002019.

Wood abstract supports osmotic adjustment; stress depends on change and the receiving organism, not an intrinsically harmful brackish state.

### salinity_variability_intensifies_osmotic_stress

evidence: concern. Targets: ENVO:00002019.

Tee sampled a spatial transect. A stronger temporal intensification mechanism is not directly demonstrated by those observations.

### osmotic_stress_selects_osmoregulatory_transport

evidence: concern. Targets: ENVO:00002019.

Wood supports transport activation and Wu metagenomic associations; measured evolutionary selection is not established. Transport and synthesis also differ.

### transport_enables_compatible_solutes

evidence: supported. Targets: ENVO:00002019.

Wu introduction supports uptake or biosynthesis of compatible solutes; synthesis should not be assigned to transport itself.

### transport_enables_salt_in_strategy

evidence: supported. Targets: ENVO:00002019.

Wu supports ion transport as salt-in machinery; genomic potential is not measured intracellular accumulation in every sample.

### osmotic_stress_filters_freshwater_bacteria

evidence: concern. Targets: ENVO:00002019.

Campbell reports rRNA:rDNA growth-potential proxies. The specific osmotic-filter mechanism is an interpretation, not a directly measured cause.

### osmotic_stress_filters_marine_bacteria

evidence: unknown. Targets: ENVO:00002019.

Crump abstract reports marine advection and seasonal communities but does not isolate osmotic filtering; publisher full text returned403.

### salinity_gradient_drives_community_turnover

evidence: supported. Targets: ENVO:00002019.

Crump and Campbell associate turnover with salinity and other factors, not salinity as a uniquely established cause.

### growth_and_residence_time_establish_estuarine_bacteria

evidence: concern. Targets: ENVO:00002019.

Crump supports doubling time shorter than residence time; growth faster than a duration is dimensionally incorrect wording.

### residence_time_modulates_estuarine_establishment

evidence: supported. Targets: ENVO:00002019.

Crump supports conditional establishment when growth and hydrological timescales permit retention.

### Identity, definition and source interpretation

identity: supported. Targets: ENVO:00002019.

ENVO:00002019 denotes saline water material intermediate between fresh and marine water, distinct from a water body. The estuarine example graph has 17 edges; community typing and some causal extrapolations need correction, while mixing and conditional growth/residence observations are supported. Ten qualitative source bands and reported taxa remain source-specific.

### All parent-contribution routes and mapping scope

grounding: supported. Targets: ENVO:00002019.

ENVO:00002019 denotes saline water material intermediate between fresh and marine water, distinct from a water body. The estuarine example graph has 17 edges; community typing and some causal extrapolations need correction, while mixing and conditional growth/residence observations are supported. Ten qualitative source bands and reported taxa remain source-specific. Ontology, source-path, ambiguous-leaf and authored-definition contributions were distinguished.

### Every source, count unit and native status

provenance: supported. Targets: ENVO:00002019.

Complete reconstruction preserves 3 source concepts and 0 ITEM-reviewed contributors. Actual attestations=[{"source": "ENVIRONMENTS_TABLE", "source_id": "water_brackish", "source_label": "water_brackish", "notes": "Physicochemical parameter bands from kg-microbe's environment table."}, {"source": "MADIN", "source_id": "ENVO:00002019", "source_label": "brackish water", "assertion_count": 64, "assertion_unit": "TAXON"}, {"source": "PREGO", "source_id": "ENVO:00002019", "source_label": "brackish water", "assertion_count": 1015, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates&#124;environmental_samples"}]. Unlike units are not summed. Omitted zero direct counts do not mean ecological absence; this review does not promote native status.

### Source-reported association versus characteristic presence

evidence: supported. Targets: ENVO:00002019.

All emitted taxon identifiers resolve; normalized spellings and old aliases explain supplied-label differences. Full reconstruction retains ranks, scores, pools and corroborations. No is_characteristic assertion is present; neither resolution nor a source score proves occurrence, abundance or ecological universality.

### Qualitative source bands and triad roles

evidence: supported. Targets: ENVO:00002019.

All 10 entries reproduce the exact single-term environment-table source. These qualitative descriptors are source-attributed, not measured universal thresholds. Multi-term environments are not attached for a single component. No MIxS broad/local/medium entry is silently promoted to identity.

### Optional fields and biological evidence boundaries

completeness: supported. Targets: ENVO:00002019.

Optional missing definitions, datasets or discussions are not defects solely because they are empty. Every asserted graph edge is individually assessed above. No named gene, locus, regulator, strain-specific transcriptome or expression-module claim in this record calls for an iModulonDB query; generic enzymes/osmoregulation and habitat associations do not specify an applicable organism/dataset.

## Findings

### F1: Transport is described as synthesizing solutes

minor / open / confirmed; issue key: envo-00002019-transport-synthesis-wording.

The osmoregulatory transport description conflates import/export with biosynthesis. Compatible-solute production and transport are distinct mechanisms even when both contribute to homeostasis.

### F2: Growth rate is compared directly with a residence duration

minor / open / confirmed; issue key: envo-00002019-growth-timescale-wording.

The growth-establishment edge says growth is faster than hydrologic residence time. Its source and notes instead compare doubling time with residence time; the intended conditional result is supported but the description mixes dimensions.

### F3: Mixed microbial assemblages are typed as taxa

major / open / confirmed; issue key: envo-00002019-community-node-type.

freshwater_bacterioplankton, marine_bacterioplankton and estuarine_bacterioplankton do not denote an organism or clade. Native COMMUNITY is available, so a process type or new schema enum is not an appropriate default replacement.

### F4: Some causal scope and detailed evidence remain unsupported

major / open / provisional; issue key: envo-00002019-causal-scope-support.

The estuarine example needs explicit conditional scope in its generic description. Temporal stress intensification and osmotic filtering exceed the inspected spatial, proxy or abstract evidence; metagenomic association is not directly measured physiological selection. This does not show that the mechanisms are false.

## Recommended Actions And Acceptance Checks

### A1

Separate transport from biosynthesis or widen the node to an explicitly supported osmoregulatory system; preserve the two strategy branches and evidence limitations.

- Change only maintained inputs with exact source/edge keys; preserve independent parents, identities, source counts/units and native lifecycle.
- Inspect claim-level sources; append required curation history, add focused regressions, inspect a seed canary and regenerate affected products.
- Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity and full QC; save a linked successor for each finding disposition.
- Compare actual semantic-map inputs and perform genuine regeneration when changed; do not substitute a checksum-only refresh.

### A2

Express the condition as a doubling time shorter than water residence time, or compare growth and flushing rates with consistent units; retain the seasonal study scope.

- Change only maintained inputs with exact source/edge keys; preserve independent parents, identities, source counts/units and native lifecycle.
- Inspect claim-level sources; append required curation history, add focused regressions, inspect a seed canary and regenerate affected products.
- Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity and full QC; save a linked successor for each finding disposition.
- Compare actual semantic-map inputs and perform genuine regeneration when changed; do not substitute a checksum-only refresh.

### A3

Use COMMUNITY for the assemblage nodes. For physiologically defined subpopulations, select a supported community/state representation without inventing a clade or converting the entity into a process. Preserve stable IDs where semantics are unchanged and validate rendering.

- Change only maintained inputs with exact source/edge keys; preserve independent parents, identities, source counts/units and native lifecycle.
- Inspect claim-level sources; append required curation history, add focused regressions, inspect a seed canary and regenerate affected products.
- Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity and full QC; save a linked successor for each finding disposition.
- Compare actual semantic-map inputs and perform genuine regeneration when changed; do not substitute a checksum-only refresh.

### A4

Retain supported edges, qualify context and causal strength, retrieve outstanding passages, and replace title-like snippets with short exact evidence and precise locators. Do not equate a resolving reference with claim support.

- Change only maintained inputs with exact source/edge keys; preserve independent parents, identities, source counts/units and native lifecycle.
- Inspect claim-level sources; append required curation history, add focused regressions, inspect a seed canary and regenerate affected products.
- Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity and full QC; save a linked successor for each finding disposition.
- Compare actual semantic-map inputs and perform genuine regeneration when changed; do not substitute a checksum-only refresh.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/aquatic/brackish_water.yaml; Entire captured YAML read, including provenance, parameters, taxa, graphs and history | supports | ENVO:00002019 denotes saline water material intermediate between fresh and marine water, distinct from a water body. The estuarine example graph has 17 edges; community typing and some causal extrapolations need correction, while mixing and conditional growth/residence observations are supported. Ten qualitative source bands and reported taxa remain source-specific. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied exact identity, strict-parent, MIxS-role, source unit/score, ITEM lifecycle and claim-specific evidence contracts. TAXON is an organism/clade; COMMUNITY is an interacting assemblage, not a process. |
| RAW | data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; Exact logical TSV rows; header is row1. Neighboring source/parent matches excluded. | supports | {"data/raw/environment_parameters.tsv": [{"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "Gradients", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "low"}, "logical_row": 184}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "Nutrients", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "medium"}, "logical_row": 185}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "Pressure", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "low"}, "logical_row": 186}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "Salinity", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "medium"}, "logical_row": 187}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "Structural", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "low"}, "logical_row": 188}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "Water", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "high"}, "logical_row": 189}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "pH", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "medium"}, "logical_row": 190}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "salinity variability", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "wide"}, "logical_row": 191}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "temp variability", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "medium"}, "logical_row": 192}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "water variability", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "permanently wet"}, "logical_row": 193}], "data/raw/madin_habitat_taxa.tsv": [{"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:1084519", "taxon_label": "Nibribacter koreensis"}, "logical_row": 361}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:1124597", "taxon_label": "Magnetococcus marinus"}, "logical_row": 362}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:1132696", "taxon_label": "Chryseobacterium rigui"}, "logical_row": 363}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:1165090", "taxon_label": "imtechella_halotolerans"}, "logical_row": 364}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:1194079", "taxon_label": "streptomyces_chilikensis"}, "logical_row": 365}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:152268", "taxon_label": "bacillus_litoralis"}, "logical_row": 366}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:1727163", "taxon_label": "Algoriphagus sp. M8-2"}, "logical_row": 367}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:205844", "taxon_label": "novosphingobium_pentaromativorans"}, "logical_row": 368}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:226504", "taxon_label": "algoriphagus_mannitolivorans"}, "logical_row": 369}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:226505", "taxon_label": "algoriphagus_halophilus"}, "logical_row": 370}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:226506", "taxon_label": "algoriphagus_ornithinivorans"}, "logical_row": 371}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:23", "taxon_label": "alteromonas_colwelliana"}, "logical_row": 372}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:231438", "taxon_label": "desulfoluna_butyratoxydans"}, "logical_row": 373}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:231440", "taxon_label": "desulfopila_aestuarii"}, "logical_row": 374}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:231447", "taxon_label": "desulfobulbus_japonicus"}, "logical_row": 375}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:247022", "taxon_label": "microbulbifer_maritimus"}, "logical_row": 376}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:252230", "taxon_label": "nocardioides_ganghwensis"}, "logical_row": 377}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:252231", "taxon_label": "Nocardioides aestuarii"}, "logical_row": 378}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:252597", "taxon_label": "alteromonas_litorea"}, "logical_row": 379}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:255984", "taxon_label": "erythrobacter_aquimaris"}, "logical_row": 380}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:259390", "taxon_label": "nocardia_takedensis"}, "logical_row": 381}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:285109", "taxon_label": "thioclava_pacifica"}, "logical_row": 382}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:288019", "taxon_label": "Yeosuana aromativorans"}, "logical_row": 383}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:288022", "taxon_label": "kordiimonas_gwangyangensis"}, "logical_row": 384}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:29494", "taxon_label": "vibrio_furnissii"}, "logical_row": 385}], "data/raw/madin_habitats.tsv": [{"data": {"label": "brackish water", "madin_id": "ENVO:00002019", "taxon_count": "64", "vocabulary": "ENVO"}, "logical_row": 42}], "data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:00002010", "predicate": "rdfs:subClassOf", "subject": "ENVO:00002019"}, "logical_row": 5280}], "data/raw/ontology_terms.tsv": [{"data": {"definition": "Water which has a higher salinity than fresh water but a lower salinity than marine water.", "deprecated": "", "directly_referenced": "TRUE", "label": "brackish water", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id": "ENVO:00002019"}, "logical_row": 7175}], "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "1", "taxon_id": "NCBITaxon:1046954", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-E20"}, "logical_row": 5661}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "2", "taxon_id": "NCBITaxon:1046955", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-F02"}, "logical_row": 5662}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "3", "taxon_id": "NCBITaxon:1046956", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-G07"}, "logical_row": 5663}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "4", "taxon_id": "NCBITaxon:1046957", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-G08"}, "logical_row": 5664}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "5", "taxon_id": "NCBITaxon:1046958", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-I11"}, "logical_row": 5665}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "6", "taxon_id": "NCBITaxon:1046959", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-I16"}, "logical_row": 5666}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "7", "taxon_id": "NCBITaxon:1046960", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-K16"}, "logical_row": 5667}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "8", "taxon_id": "NCBITaxon:1046961", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-L05"}, "logical_row": 5668}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "9", "taxon_id": "NCBITaxon:1046962", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-L13"}, "logical_row": 5669}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "10", "taxon_id": "NCBITaxon:1046963", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-M08"}, "logical_row": 5670}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "11", "taxon_id": "NCBITaxon:1046964", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-N05"}, "logical_row": 5671}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "12", "taxon_id": "NCBITaxon:1046965", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-N14"}, "logical_row": 5672}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "13", "taxon_id": "NCBITaxon:1046966", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-N17"}, "logical_row": 5673}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "14", "taxon_id": "NCBITaxon:1046967", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-O02"}, "logical_row": 5674}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "15", "taxon_id": "NCBITaxon:1046970", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-O17"}, "logical_row": 5675}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "16", "taxon_id": "NCBITaxon:1046971", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-P02"}, "logical_row": 5676}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "17", "taxon_id": "NCBITaxon:1046972", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-P10"}, "logical_row": 5677}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "18", "taxon_id": "NCBITaxon:1046973", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-P14"}, "logical_row": 5678}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "19", "taxon_id": "NCBITaxon:1046974", "taxon_label": "Cloacimonetes bacterium SCGC AAA255-B16"}, "logical_row": 5679}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "20", "taxon_id": "NCBITaxon:1046975", "taxon_label": "Cloacimonetes bacterium SCGC AAA255-C20"}, "logical_row": 5680}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "21", "taxon_id": "NCBITaxon:1046978", "taxon_label": "Cloacimonetes bacterium SCGC AAA255-L20"}, "logical_row": 5681}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "22", "taxon_id": "NCBITaxon:1046991", "taxon_label": "Acetothermia bacterium SCGC AAA255-C06"}, "logical_row": 5682}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "23", "taxon_id": "NCBITaxon:1047002", "taxon_label": "Microgenomates bacterium SCGC AAA255-J07"}, "logical_row": 5683}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "24", "taxon_id": "NCBITaxon:1047006", "taxon_label": "Omnitrophica bacterium SCGC AAA252-B19"}, "logical_row": 5684}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "25", "taxon_id": "NCBITaxon:1047014", "taxon_label": "Aminicenantes bacterium SCGC AAA252-B17"}, "logical_row": 5685}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category": "biolink:OntologyClass", "channels": "annotated_genomes_isolates&#124;environmental_samples", "direct_assertion_count": "1016", "max_prego_score": "3", "ontology": "ENVO", "prego_id": "ENVO:00002019", "prego_synonyms": "brackish water&#124;brackish waters", "taxon_count": "1015"}, "logical_row": 80}]} |
| CODE | src/habitatmech/seed.py; Executed complete-document reconstruction; all40 matched captured records | supports | {"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002019", "mapping_predicate": null, "reviewed": false, "route": "environments_table_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002019", "mapping_predicate": null, "reviewed": false, "route": "environments_table_self_grounded"}, "minted": "habitatmech:ENVIRONMENTS_TABLE.a814145b33", "source": "ENVIRONMENTS_TABLE", "source_id": "water_brackish"}, {"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002019", "mapping_predicate": null, "reviewed": false, "route": "madin_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002019", "mapping_predicate": null, "reviewed": false, "route": "madin_self_grounded"}, "minted": "habitatmech:MADIN.0a700a7140", "source": "MADIN", "source_id": "ENVO:00002019"}, {"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002019", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002019", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.202c26d6e8", "source": "PREGO", "source_id": "ENVO:00002019"}], "source_concepts": 3} |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Same-day official OWL: named identities, typed synonyms and direct axioms; no snapshot refresh | supports | {"ENVO:00002006": {"definitions": ["An environmental material primarily composed of dihydrogen oxide in its liquid form."], "deprecated": [], "equivalents": [], "labels": ["liquid water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000815", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_15377"]}], "replacements": [], "synonyms": {"hasBroadSynonym": ["water"], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002010": {"definitions": ["Water which contains a significant concentration of dissolved salts."], "deprecated": [], "equivalents": [], "labels": ["saline water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/ENVO_02000200"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_26710"]}, {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000086"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PATO_0001657"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["salt water"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002019": {"definitions": ["Water which has a higher salinity than fresh water but a lower salinity than marine water."], "deprecated": [], "equivalents": [], "labels": ["brackish water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002010"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}} |
| PARENT | data/habitats/aquatic/saline_water.yaml; data/habitats/aquatic/liquid_water.yaml; Ancestor context is not full-record review coverage of ancestors | supports | {"ENVO:00002006": {"definition": "An environmental material primarily composed of dihydrogen oxide in its liquid form.", "grounding_status": "EXACT", "label": "liquid water", "parent_habitats": ["ENVO:01000815"]}, "ENVO:00002010": {"definition": "Water which contains a significant concentration of dissolved salts.", "grounding_status": "EXACT", "label": "saline water", "parent_habitats": ["ENVO:00002006"]}} |
| TAX0 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1017%2C1018%2C1019%2C1029756%2C1035916%2C1040984%2C104268%2C1046954%2C1046955%2C1046956%2C1046957%2C1046958%2C1046959%2C1046960%2C1046961%2C1046962%2C1046963%2C1046964%2C1046965%2C1046966%2C1046967%2C1046970%2C1046971%2C1046972%2C1046973%2C1046974%2C1046975%2C1046978%2C1046991%2C1047002%2C1047006%2C1047014%2C1048%2C1049%2C1073250%2C1084519%2C1085%2C1087448%2C109328%2C1100%2C110539%2C110639%2C1111735%2C1120961%2C1120966%2C1120998%2C1121014%2C1121403%2C1121410%2C1121416%2C1121878%2C1121879%2C1121938%2C1122176%2C1122197%2C1123027%2C1123503%2C1123517%2C1124597%2C1132696%2C1134435%2C1156985%2C1165090%2C1175486%2C118166%2C1188229%2C1194079%2C1245526%2C1257026%2C1257027%2C1264%2C1265%2C1270%2C1282%2C129578%2C129958%2C1318%2C1397696%2C1408433%2C1409%2C1423814%2C1485%2C150172%2C1512%2C152268%2C1526%2C1527%2C154046%2C1550%2C157687%2C158847%2C1596%2C1623%2C163908%2C165179%2C165813%2C1727163%2C195907%2C195913%2C202747%2C205844%2C209897%2C216903%2C226504%2C226505%2C226506%2C23%2C231438%2C231440%2C231447%2C245187%2C245188%2C247022%2C249351%2C249352%2C252230%2C252231%2C252597%2C255984%2C259390%2C266940%2C267375%2C267990%2C28122%2C285109%2C285258%2C287844%2C288019%2C288022%2C293826%2C293890%2C29494%2C29535%2C295419%2C306540%2C306541%2C317936%2C321267%2C325473%2C326442%2C329406%2C332168%2C34085%2C343403%2C364197%2C36987%2C393131%2C395491%2C411467%2C411477&amp;retmode=xml; NCBI TaxId, ScientificName, Rank and OtherNames | supports | The two chunks jointly resolve all188 requested cohort IDs. This target=[{"current_id": "1046954", "current_name": "Cloacimonetes bacterium SCGC AAA252-E20", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-E20", "id": "1046954", "rank": "species"}, {"current_id": "1046955", "current_name": "Cloacimonetes bacterium SCGC AAA252-F02", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-F02", "id": "1046955", "rank": "species"}, {"current_id": "1046956", "current_name": "Cloacimonetes bacterium SCGC AAA252-G07", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-G07", "id": "1046956", "rank": "species"}, {"current_id": "1046957", "current_name": "Cloacimonetes bacterium SCGC AAA252-G08", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-G08", "id": "1046957", "rank": "species"}, {"current_id": "1046958", "current_name": "Cloacimonetes bacterium SCGC AAA252-I11", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-I11", "id": "1046958", "rank": "species"}, {"current_id": "1046959", "current_name": "Cloacimonetes bacterium SCGC AAA252-I16", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-I16", "id": "1046959", "rank": "species"}, {"current_id": "1046960", "current_name": "Cloacimonetes bacterium SCGC AAA252-K16", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-K16", "id": "1046960", "rank": "species"}, {"current_id": "1046961", "current_name": "Cloacimonetes bacterium SCGC AAA252-L05", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-L05", "id": "1046961", "rank": "species"}, {"current_id": "1046962", "current_name": "Cloacimonetes bacterium SCGC AAA252-L13", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-L13", "id": "1046962", "rank": "species"}, {"current_id": "1046963", "current_name": "Cloacimonetes bacterium SCGC AAA252-M08", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-M08", "id": "1046963", "rank": "species"}, {"current_id": "1046964", "current_name": "Cloacimonetes bacterium SCGC AAA252-N05", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-N05", "id": "1046964", "rank": "species"}, {"current_id": "1046965", "current_name": "Cloacimonetes bacterium SCGC AAA252-N14", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-N14", "id": "1046965", "rank": "species"}, {"current_id": "1046966", "current_name": "Cloacimonetes bacterium SCGC AAA252-N17", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-N17", "id": "1046966", "rank": "species"}, {"current_id": "1046967", "current_name": "Cloacimonetes bacterium SCGC AAA252-O02", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-O02", "id": "1046967", "rank": "species"}, {"current_id": "1046970", "current_name": "Cloacimonetes bacterium SCGC AAA252-O17", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-O17", "id": "1046970", "rank": "species"}, {"current_id": "1046971", "current_name": "Cloacimonetes bacterium SCGC AAA252-P02", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-P02", "id": "1046971", "rank": "species"}, {"current_id": "1046972", "current_name": "Cloacimonetes bacterium SCGC AAA252-P10", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-P10", "id": "1046972", "rank": "species"}, {"current_id": "1046973", "current_name": "Cloacimonetes bacterium SCGC AAA252-P14", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-P14", "id": "1046973", "rank": "species"}, {"current_id": "1046974", "current_name": "Cloacimonetes bacterium SCGC AAA255-B16", "frozen_label": "Cloacimonetes bacterium SCGC AAA255-B16", "id": "1046974", "rank": "species"}, {"current_id": "1046975", "current_name": "Cloacimonetes bacterium SCGC AAA255-C20", "frozen_label": "Cloacimonetes bacterium SCGC AAA255-C20", "id": "1046975", "rank": "species"}, {"current_id": "1046978", "current_name": "Cloacimonetes bacterium SCGC AAA255-L20", "frozen_label": "Cloacimonetes bacterium SCGC AAA255-L20", "id": "1046978", "rank": "species"}, {"current_id": "1046991", "current_name": "Acetothermia bacterium SCGC AAA255-C06", "frozen_label": "Acetothermia bacterium SCGC AAA255-C06", "id": "1046991", "rank": "species"}, {"current_id": "1047002", "current_name": "Microgenomates bacterium SCGC AAA255-J07", "frozen_label": "Microgenomates bacterium SCGC AAA255-J07", "id": "1047002", "rank": "species"}, {"current_id": "1047006", "current_name": "Omnitrophica bacterium SCGC AAA252-B19", "frozen_label": "Omnitrophica bacterium SCGC AAA252-B19", "id": "1047006", "rank": "species"}, {"current_id": "1047014", "current_name": "Aminicenantes bacterium SCGC AAA252-B17", "frozen_label": "Aminicenantes bacterium SCGC AAA252-B17", "id": "1047014", "rank": "species"}, {"current_id": "1084519", "current_name": "Nibribacter koreensis", "frozen_label": "Nibribacter koreensis", "id": "1084519", "rank": "species"}, {"current_id": "1124597", "current_name": "Magnetococcus marinus", "frozen_label": "Magnetococcus marinus", "id": "1124597", "rank": "species"}, {"current_id": "1132696", "current_name": "Chryseobacterium rigui", "frozen_label": "Chryseobacterium rigui", "id": "1132696", "rank": "species"}, {"current_id": "1165090", "current_name": "Imtechella halotolerans", "frozen_label": "imtechella_halotolerans", "id": "1165090", "rank": "species"}, {"current_id": "1194079", "current_name": "Streptomyces chilikensis", "frozen_label": "streptomyces_chilikensis", "id": "1194079", "rank": "species"}, {"current_id": "152268", "current_name": "Metabacillus litoralis", "frozen_label": "bacillus_litoralis", "id": "152268", "rank": "species"}, {"current_id": "1727163", "current_name": "Algoriphagus sanaruensis", "frozen_label": "Algoriphagus sp. M8-2", "id": "1727163", "rank": "species"}, {"current_id": "205844", "current_name": "Novosphingobium pentaromativorans", "frozen_label": "novosphingobium_pentaromativorans", "id": "205844", "rank": "species"}, {"current_id": "226504", "current_name": "Algoriphagus mannitolivorans", "frozen_label": "algoriphagus_mannitolivorans", "id": "226504", "rank": "species"}, {"current_id": "226505", "current_name": "Algoriphagus halophilus", "frozen_label": "algoriphagus_halophilus", "id": "226505", "rank": "species"}, {"current_id": "226506", "current_name": "Algoriphagus ornithinivorans", "frozen_label": "algoriphagus_ornithinivorans", "id": "226506", "rank": "species"}, {"current_id": "23", "current_name": "Shewanella colwelliana", "frozen_label": "alteromonas_colwelliana", "id": "23", "rank": "species"}, {"current_id": "231438", "current_name": "Desulfoluna butyratoxydans", "frozen_label": "desulfoluna_butyratoxydans", "id": "231438", "rank": "species"}, {"current_id": "231440", "current_name": "Desulfopila aestuarii", "frozen_label": "desulfopila_aestuarii", "id": "231440", "rank": "species"}, {"current_id": "231447", "current_name": "Desulfogranum japonicum", "frozen_label": "desulfobulbus_japonicus", "id": "231447", "rank": "species"}, {"current_id": "247022", "current_name": "Microbulbifer maritimus", "frozen_label": "microbulbifer_maritimus", "id": "247022", "rank": "species"}, {"current_id": "252230", "current_name": "Nocardioides ganghwensis", "frozen_label": "nocardioides_ganghwensis", "id": "252230", "rank": "species"}, {"current_id": "252231", "current_name": "Nocardioides aestuarii", "frozen_label": "Nocardioides aestuarii", "id": "252231", "rank": "species"}, {"current_id": "252597", "current_name": "Alteromonas litorea", "frozen_label": "alteromonas_litorea", "id": "252597", "rank": "species"}, {"current_id": "255984", "current_name": "Qipengyuania aquimaris", "frozen_label": "erythrobacter_aquimaris", "id": "255984", "rank": "species"}, {"current_id": "259390", "current_name": "Nocardia takedensis", "frozen_label": "nocardia_takedensis", "id": "259390", "rank": "species"}, {"current_id": "285109", "current_name": "Thioclava pacifica", "frozen_label": "thioclava_pacifica", "id": "285109", "rank": "species"}, {"current_id": "288019", "current_name": "Yeosuana aromativorans", "frozen_label": "Yeosuana aromativorans", "id": "288019", "rank": "species"}, {"current_id": "288022", "current_name": "Kordiimonas gwangyangensis", "frozen_label": "kordiimonas_gwangyangensis", "id": "288022", "rank": "species"}, {"current_id": "29494", "current_name": "Vibrio furnissii", "frozen_label": "vibrio_furnissii", "id": "29494", "rank": "species"}]. All noncanonical supplied names match normalized spelling or retained aliases. Resolution does not establish occurrence. |
| TAX1 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=411485%2C411901%2C418643%2C428125%2C435590%2C445336%2C449306%2C457391%2C457424%2C457427%2C477974%2C498761%2C502025%2C523845%2C52560%2C53245%2C537937%2C54121%2C551275%2C551789%2C55518%2C556258%2C562%2C56780%2C568099%2C616997%2C6376%2C643867%2C647171%2C657014%2C668820%2C693661%2C69670%2C710685%2C717231%2C889378%2C94122%2C999547&amp;retmode=xml; NCBI TaxId, ScientificName, Rank and OtherNames | supports | The two chunks jointly resolve all188 requested cohort IDs. This target=[{"current_id": "1046954", "current_name": "Cloacimonetes bacterium SCGC AAA252-E20", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-E20", "id": "1046954", "rank": "species"}, {"current_id": "1046955", "current_name": "Cloacimonetes bacterium SCGC AAA252-F02", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-F02", "id": "1046955", "rank": "species"}, {"current_id": "1046956", "current_name": "Cloacimonetes bacterium SCGC AAA252-G07", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-G07", "id": "1046956", "rank": "species"}, {"current_id": "1046957", "current_name": "Cloacimonetes bacterium SCGC AAA252-G08", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-G08", "id": "1046957", "rank": "species"}, {"current_id": "1046958", "current_name": "Cloacimonetes bacterium SCGC AAA252-I11", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-I11", "id": "1046958", "rank": "species"}, {"current_id": "1046959", "current_name": "Cloacimonetes bacterium SCGC AAA252-I16", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-I16", "id": "1046959", "rank": "species"}, {"current_id": "1046960", "current_name": "Cloacimonetes bacterium SCGC AAA252-K16", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-K16", "id": "1046960", "rank": "species"}, {"current_id": "1046961", "current_name": "Cloacimonetes bacterium SCGC AAA252-L05", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-L05", "id": "1046961", "rank": "species"}, {"current_id": "1046962", "current_name": "Cloacimonetes bacterium SCGC AAA252-L13", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-L13", "id": "1046962", "rank": "species"}, {"current_id": "1046963", "current_name": "Cloacimonetes bacterium SCGC AAA252-M08", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-M08", "id": "1046963", "rank": "species"}, {"current_id": "1046964", "current_name": "Cloacimonetes bacterium SCGC AAA252-N05", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-N05", "id": "1046964", "rank": "species"}, {"current_id": "1046965", "current_name": "Cloacimonetes bacterium SCGC AAA252-N14", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-N14", "id": "1046965", "rank": "species"}, {"current_id": "1046966", "current_name": "Cloacimonetes bacterium SCGC AAA252-N17", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-N17", "id": "1046966", "rank": "species"}, {"current_id": "1046967", "current_name": "Cloacimonetes bacterium SCGC AAA252-O02", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-O02", "id": "1046967", "rank": "species"}, {"current_id": "1046970", "current_name": "Cloacimonetes bacterium SCGC AAA252-O17", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-O17", "id": "1046970", "rank": "species"}, {"current_id": "1046971", "current_name": "Cloacimonetes bacterium SCGC AAA252-P02", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-P02", "id": "1046971", "rank": "species"}, {"current_id": "1046972", "current_name": "Cloacimonetes bacterium SCGC AAA252-P10", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-P10", "id": "1046972", "rank": "species"}, {"current_id": "1046973", "current_name": "Cloacimonetes bacterium SCGC AAA252-P14", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-P14", "id": "1046973", "rank": "species"}, {"current_id": "1046974", "current_name": "Cloacimonetes bacterium SCGC AAA255-B16", "frozen_label": "Cloacimonetes bacterium SCGC AAA255-B16", "id": "1046974", "rank": "species"}, {"current_id": "1046975", "current_name": "Cloacimonetes bacterium SCGC AAA255-C20", "frozen_label": "Cloacimonetes bacterium SCGC AAA255-C20", "id": "1046975", "rank": "species"}, {"current_id": "1046978", "current_name": "Cloacimonetes bacterium SCGC AAA255-L20", "frozen_label": "Cloacimonetes bacterium SCGC AAA255-L20", "id": "1046978", "rank": "species"}, {"current_id": "1046991", "current_name": "Acetothermia bacterium SCGC AAA255-C06", "frozen_label": "Acetothermia bacterium SCGC AAA255-C06", "id": "1046991", "rank": "species"}, {"current_id": "1047002", "current_name": "Microgenomates bacterium SCGC AAA255-J07", "frozen_label": "Microgenomates bacterium SCGC AAA255-J07", "id": "1047002", "rank": "species"}, {"current_id": "1047006", "current_name": "Omnitrophica bacterium SCGC AAA252-B19", "frozen_label": "Omnitrophica bacterium SCGC AAA252-B19", "id": "1047006", "rank": "species"}, {"current_id": "1047014", "current_name": "Aminicenantes bacterium SCGC AAA252-B17", "frozen_label": "Aminicenantes bacterium SCGC AAA252-B17", "id": "1047014", "rank": "species"}, {"current_id": "1084519", "current_name": "Nibribacter koreensis", "frozen_label": "Nibribacter koreensis", "id": "1084519", "rank": "species"}, {"current_id": "1124597", "current_name": "Magnetococcus marinus", "frozen_label": "Magnetococcus marinus", "id": "1124597", "rank": "species"}, {"current_id": "1132696", "current_name": "Chryseobacterium rigui", "frozen_label": "Chryseobacterium rigui", "id": "1132696", "rank": "species"}, {"current_id": "1165090", "current_name": "Imtechella halotolerans", "frozen_label": "imtechella_halotolerans", "id": "1165090", "rank": "species"}, {"current_id": "1194079", "current_name": "Streptomyces chilikensis", "frozen_label": "streptomyces_chilikensis", "id": "1194079", "rank": "species"}, {"current_id": "152268", "current_name": "Metabacillus litoralis", "frozen_label": "bacillus_litoralis", "id": "152268", "rank": "species"}, {"current_id": "1727163", "current_name": "Algoriphagus sanaruensis", "frozen_label": "Algoriphagus sp. M8-2", "id": "1727163", "rank": "species"}, {"current_id": "205844", "current_name": "Novosphingobium pentaromativorans", "frozen_label": "novosphingobium_pentaromativorans", "id": "205844", "rank": "species"}, {"current_id": "226504", "current_name": "Algoriphagus mannitolivorans", "frozen_label": "algoriphagus_mannitolivorans", "id": "226504", "rank": "species"}, {"current_id": "226505", "current_name": "Algoriphagus halophilus", "frozen_label": "algoriphagus_halophilus", "id": "226505", "rank": "species"}, {"current_id": "226506", "current_name": "Algoriphagus ornithinivorans", "frozen_label": "algoriphagus_ornithinivorans", "id": "226506", "rank": "species"}, {"current_id": "23", "current_name": "Shewanella colwelliana", "frozen_label": "alteromonas_colwelliana", "id": "23", "rank": "species"}, {"current_id": "231438", "current_name": "Desulfoluna butyratoxydans", "frozen_label": "desulfoluna_butyratoxydans", "id": "231438", "rank": "species"}, {"current_id": "231440", "current_name": "Desulfopila aestuarii", "frozen_label": "desulfopila_aestuarii", "id": "231440", "rank": "species"}, {"current_id": "231447", "current_name": "Desulfogranum japonicum", "frozen_label": "desulfobulbus_japonicus", "id": "231447", "rank": "species"}, {"current_id": "247022", "current_name": "Microbulbifer maritimus", "frozen_label": "microbulbifer_maritimus", "id": "247022", "rank": "species"}, {"current_id": "252230", "current_name": "Nocardioides ganghwensis", "frozen_label": "nocardioides_ganghwensis", "id": "252230", "rank": "species"}, {"current_id": "252231", "current_name": "Nocardioides aestuarii", "frozen_label": "Nocardioides aestuarii", "id": "252231", "rank": "species"}, {"current_id": "252597", "current_name": "Alteromonas litorea", "frozen_label": "alteromonas_litorea", "id": "252597", "rank": "species"}, {"current_id": "255984", "current_name": "Qipengyuania aquimaris", "frozen_label": "erythrobacter_aquimaris", "id": "255984", "rank": "species"}, {"current_id": "259390", "current_name": "Nocardia takedensis", "frozen_label": "nocardia_takedensis", "id": "259390", "rank": "species"}, {"current_id": "285109", "current_name": "Thioclava pacifica", "frozen_label": "thioclava_pacifica", "id": "285109", "rank": "species"}, {"current_id": "288019", "current_name": "Yeosuana aromativorans", "frozen_label": "Yeosuana aromativorans", "id": "288019", "rank": "species"}, {"current_id": "288022", "current_name": "Kordiimonas gwangyangensis", "frozen_label": "kordiimonas_gwangyangensis", "id": "288022", "rank": "species"}, {"current_id": "29494", "current_name": "Vibrio furnissii", "frozen_label": "vibrio_furnissii", "id": "29494", "rank": "species"}]. All noncanonical supplied names match normalized spelling or retained aliases. Resolution does not establish occurrence. |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf; Bounded searches, not global absence claims | supports | Identifier, label, slug and exact source-path searches included ignored/hidden files in these roots; coverage used Path.rglob. No earlier structured observation of this target found. Legacy reports were indexed; only specifically cited historical reports were read in full. Upstream search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv", "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv", "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv", "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv", "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv", "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv", "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv", "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv", "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv", "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv", "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}], "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "exit_code": 0, "matches": [], "stderr": ""}]} |
| ISSUES | https://github.com/CultureBotAI/HabitatMech/issues; GitHub CLI census and selected full issue bodies | supports | All-state946-issue title/body census inspected for overlap. Shared1249 and1398 apply where cited.1259 concerns a separate Lake biofilm source,1423 different records, and1638 the bioreactor graph; none is treated as this target repaired. Comments were not exhaustively crawled. |
| GRAPH | curation/causal_graphs/brackish_water.yaml; All nodes, edges, descriptions and evidence | supports | Entire overlay and generated graph read: 16 nodes and 17 edges. Exact source references and node scopes assessed. |
| PMID-15006771 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15006771+AND+SRC%3AMED&amp;format=json&amp;resultType=core; EuropePMC core metadata and abstract | supports | Bibliographic identity and full abstract inspected: Microbial biogeography along an estuarine salinity gradient: combined influences of bacterial growth and residence time.; DOI:10.1128/aem.70.3.1494-1505.2004. Abstract evidence only; causal details distinguished edge by edge. |
| PMID-21663439 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21663439+AND+SRC%3AMED&amp;format=json&amp;resultType=core; EuropePMC core metadata and abstract | supports | Bibliographic identity and full abstract inspected: Bacterial osmoregulation: a paradigm for the study of cellular homeostasis.; DOI:10.1146/annurev-micro-090110-102815. Abstract evidence only; causal details distinguished edge by edge. |
| PMID-22895159 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22895159+AND+SRC%3AMED&amp;format=json&amp;resultType=core; EuropePMC core metadata and abstract | supports | Bibliographic identity and full abstract inspected: Bacterial diversity, community structure and potential growth rates along an estuarine salinity gradient.; DOI:10.1038/ismej.2012.93. Abstract evidence only; causal details distinguished edge by edge. |
| TEE | https://link.springer.com/article/10.1186/s40168-021-01145-3; Publisher Introduction and Results through Distinct non-saline and saline osmoregulation strategies; PMID34544488 / DOI10.1186/s40168-021-01145-3 | supports | Primary spatial survey distinguishes water and sediment communities and combines genes/transcripts with geochemistry. Salinity-related strategies are supported, but it is not a temporal manipulation isolating fluctuating-salinity stress. |
| WU | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11200988/fullTextXML; Body paragraphs0-12 and35-42; DOI10.1186/s40168-024-01817-w | supports | Primary estuary metagenomic study supports salt-in and compatible-solute machinery and associations with salinity. Its genomic potential and relative abundance are not direct physiological flux or experimental selection measurements. |
| LEGACY | reports/yaml_record_review/20260923T140218Z-brackish_water.md; Historical graph assessment and findings | context_only | Historical report read in full. Its blanket graph-support conclusion is not adopted; this observation reassesses every edge. Historical unstructured findings are not automatically retired. |

## Limits And Additional Notes

- Completed assessment is not a clean scientific verdict or proof of every original assertion.
- Only first3 exact BioSample/Organism descriptions per sheet were individually interpreted, except all12 carbonate organism descriptions. Other matches and study joins were indexed, not individually assessed.
- Original frozen membership was not fully reconstructed; no ontology, taxonomy or source snapshot was refreshed.
- Same-agent review, not independent approval. No habitat data, native status, history or GitHub mutation.
- SSSOM/KGX conformance with current kg-microbe modeling was not audited; shared1398 remains open.
- Whole-corpus review remains incomplete; ancestor reads and source indexing add no target coverage.
- Crump and Wood were assessed from abstracts after publisher requests returned403; Campbell was assessed from its abstract. Selected Tee and Wu primary full-text sections were inspected. Unknown detailed edge support remains open; title fragments alone are not proof. No correction notices were present in retrieved core metadata, not proof that none exist elsewhere.
- New immutable observation only; curation and publication are separate work.
- No prior structured target observation found; historical reports are preserved and are not silently retired.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T225628Z-brackish_water
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: brackish_water'
started_at: '2026-10-11T22:35:45.077783Z'
finished_at: '2026-10-11T22:56:28.023779Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Agent has participated in repository curation; not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: ENVO:00002019 denotes saline water material intermediate between fresh and
  marine water, distinct from a water body. The estuarine example graph has 17 edges;
  community typing and some causal extrapolations need correction, while mixing and
  conditional growth/residence observations are supported. Ten qualitative source
  bands and reported taxa remain source-specific.
source:
  git_revision: 6509db458133758a41d1f39c6d41982476c3ed0d
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
  - path: curation/causal_graphs/brackish_water.yaml
    sha256: b9d58082a53bef1143a3868918cfed7f6d74ba7e2330648069733d9ea2c76508
    role: context
  - path: curation/causal_graphs/liquid_water.yaml
    sha256: 12aac1021b9b51c6becc4ef8509bd63557b306e42c01d9b4443d69252ce29a81
    role: context
  - path: curation/decisions.tsv
    sha256: 7cbec6d310b1aac248defdbe657e68c0cc1e848981230d2279e63f474c6f4c96
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 8a06bc9f5f256f4672fe553c6b754a99ddd46fd245f65553af17567123fdbd4b
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
  - path: data/habitats/aquatic/brackish_water.yaml
    sha256: a871d66322b7804156f0e1e3f1d804a729e3a079ec28bc3b4555a92bc7af905a
    role: target
  - path: data/habitats/aquatic/liquid_water.yaml
    sha256: 03eb8ba51e02bc4c8b65b67ae5d8bb740746f8eff51ed81326685fdc5067b081
    role: context
  - path: data/habitats/aquatic/saline_water.yaml
    sha256: 0114f8f1def88f8f8ce2b675bdd8b96e44ca92248424969288ebaa803fa8c248
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
  - path: reports/yaml_record_review/20260923T140218Z-brackish_water.md
    sha256: 0020d79e17fcbb4578992eb616860c9e2c22bb2af85ea751d1c6082cd3e08b33
    role: context
  - path: reports/yaml_record_review/20260923T142152Z-brackish_water_body.md
    sha256: 408a6c249cac27dba6940eacbd87a92f621a4c3b8aea068f5a671074870a5c01
    role: context
  - path: reports/yaml_record_review/20261002T025158Z-estuarine_biome.md
    sha256: fe6064e80d77aa66261fc02c56d58d48991cddb1e3d5eb002906aca712f0284a
    role: context
  - path: reports/yaml_record_review/20261003T190816Z-marine_lake.md
    sha256: 5b2c24401d3e534c3b85cbc016896750eb8cc311f05029f06ad9f81c5326374a
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
- target_id: ENVO:00002019
  path: data/habitats/aquatic/brackish_water.yaml
  label: brackish water
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Per-source grounding and native review-depth decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact GOLD context-parent contribution decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Curated definition, genus and lexical scope
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology identity, labels, synonyms and definitions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Source harmonization and generated output
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitats.tsv
    role: Frozen Madin source habitat
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Frozen Madin taxa
  - repository: CultureBotAI/HabitatMech
    path: data/raw/environment_parameters.tsv
    role: Frozen source-specific qualitative environmental parameter bands
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Frozen PREGO habitat identity and count
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Frozen top-ranked taxon associations
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Authored causal graph nodes, directed edges and claim-level evidence
scope:
  description: Entire exact generated record and all contributors, with bounded claim-level
    scientific and source-context assessment.
  selection: 'Next forty unreviewed records in stable repository-relative path order:
    next forty AQUATIC records, atoll lagoon through coalbed methane well water. Individual
    full-record observations, not a category-wide pass. Starting observation coverage528/3208
    is not clean current-input coverage.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00002019
  exclusions:
  - target: Other3207 current records
    reason: Context reads are not their full scientific review.
checks:
- check_id: C0
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=6509db458133758a41d1f39c6d41982476c3ed0d
    just validate data/habitats/aquatic/brackish_water.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-11T22:38:02.546263Z to 2026-10-11T22:38:05.196951Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C1
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=6509db458133758a41d1f39c6d41982476c3ed0d
    just validate-strict data/habitats/aquatic/atoll_lagoon.yaml data/habitats/aquatic/bar.yaml
    data/habitats/aquatic/bathypelagic_bathyal_zone.yaml data/habitats/aquatic/bay.yaml
    data/habitats/aquatic/bayou.yaml data/habitats/aquatic/beach.yaml data/habitats/aquatic/benthic_zone.yaml
    data/habitats/aquatic/biofilm__599a99de.yaml data/habitats/aquatic/biofilm__5f164a0f.yaml
    data/habitats/aquatic/biofilm__cc6fe05a.yaml data/habitats/aquatic/biofilm__e72e4f05.yaml
    data/habitats/aquatic/biofouling.yaml data/habitats/aquatic/biofouling__438bcaa2.yaml
    data/habitats/aquatic/biofouling__50243100.yaml data/habitats/aquatic/biofouling__fa010eab.yaml
    data/habitats/aquatic/black_smoker.yaml data/habitats/aquatic/bog.yaml data/habitats/aquatic/bog_lake.yaml
    data/habitats/aquatic/borax_leachate.yaml data/habitats/aquatic/borehole.yaml
    data/habitats/aquatic/brackish_estuary.yaml data/habitats/aquatic/brackish_water.yaml
    data/habitats/aquatic/brackish_water_body.yaml data/habitats/aquatic/brine.yaml
    data/habitats/aquatic/brine__2299825d.yaml data/habitats/aquatic/brine__791bb429.yaml
    data/habitats/aquatic/brine_pool.yaml data/habitats/aquatic/canal__c42831a4.yaml
    data/habitats/aquatic/carbonate.yaml data/habitats/aquatic/cave_lake.yaml data/habitats/aquatic/cave_microbial_mat.yaml
    data/habitats/aquatic/cave_pool.yaml data/habitats/aquatic/cave_pool_sediment.yaml
    data/habitats/aquatic/cave_stream.yaml data/habitats/aquatic/cave_stream_sediment.yaml
    data/habitats/aquatic/cave_water__c4d82240.yaml data/habitats/aquatic/chemocline.yaml
    data/habitats/aquatic/chloraminated.yaml data/habitats/aquatic/chlorinated.yaml
    data/habitats/aquatic/coalbed_methane_well_water.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-11T22:38:48.678016Z to 2026-10-11T22:38:56.293670Z.
    Native scope retained. Selected scope:40 files,0 files with ERROR,0 ERROR rows.
  evidence_ids:
  - R
  - RULES
- check_id: C2
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=6509db458133758a41d1f39c6d41982476c3ed0d
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-11T22:38:56.294771Z to 2026-10-11T22:39:13.326878Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C3
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=6509db458133758a41d1f39c6d41982476c3ed0d
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-11T22:39:13.327786Z to 2026-10-11T22:40:07.035407Z.
    Native scope retained. Recorded corpus-wide outcomes:1178 canonical,1 synonym,5
    accepted exceptions,2057 SKIPPED_NO_ADAPTER. This gate does not validate minted
    identities or habitat occurrence.
  evidence_ids:
  - R
  - RULES
- check_id: C4
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=6509db458133758a41d1f39c6d41982476c3ed0d
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-11T22:40:07.036210Z to 2026-10-11T22:40:16.618000Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C5
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=6509db458133758a41d1f39c6d41982476c3ed0d
    just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-11T22:40:16.619117Z to 2026-10-11T22:40:22.318447Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C6
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=6509db458133758a41d1f39c6d41982476c3ed0d
    just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-11T22:40:22.319312Z to 2026-10-11T22:40:47.199821Z.
    Native scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C7
  name: Native gate on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002019
  command: gh run view 38179820486 --repo CultureBotAI/HabitatMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success from 2026-10-11T22:38:04.444453Z to 2026-10-11T22:38:06.504418Z.
    All three required merge-group workflows passed at the exact captured base; authoritative
    QC passed 800 tests with 3 skipped. Newly saved review bundles require their own
    integrity check. Exact-base CI receipt; no claim that these new review files passed
    remote CI.
  evidence_ids:
  - R
  - RULES
- check_id: REPRO
  name: Complete target reconstruction
  required: false
  status: passed
  target_ids:
  - ENVO:00002019
  command: .venv/bin/python /private/tmp/habitatmech-review-ay-evidence.py
  exit_code: 0
  summary: All40 complete documents matched; input hashes reverified before authoring.
  evidence_ids:
  - RAW
  - CODE
- check_id: ORIGINAL
  name: Original assertion membership
  required: false
  status: unavailable
  target_ids:
  - ENVO:00002019
  summary: Bounded ignored-inclusive searches did not reconstruct all original assertions.
    Later source exports are contextual evidence only.
  evidence_ids:
  - SEARCH
- check_id: IMODULON
  name: iModulonDB applicability
  required: false
  status: not_applicable
  target_ids:
  - ENVO:00002019
  summary: No resolvable strain/dataset-specific expression claim in this record;
    expression modules would not prove habitat occurrence.
  evidence_ids:
  - R
  - RULES
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/aquatic/brackish_water.yaml
  summary: ENVO:00002019 denotes saline water material intermediate between fresh
    and marine water, distinct from a water body. The estuarine example graph has
    17 edges; community typing and some causal extrapolations need correction, while
    mixing and conditional growth/residence observations are supported. Ten qualitative
    source bands and reported taxa remain source-specific.
  accessed_at: '2026-10-11T22:52:35.425310Z'
  support: supports
  locator: Entire captured YAML read, including provenance, parameters, taxa, graphs
    and history
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml
  summary: Applied exact identity, strict-parent, MIxS-role, source unit/score, ITEM
    lifecycle and claim-specific evidence contracts. TAXON is an organism/clade; COMMUNITY
    is an interacting assemblage, not a process.
  accessed_at: '2026-10-11T22:52:35.425310Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"data/raw/environment_parameters.tsv": [{"data": {"cobo_simon_habitat":
    "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "Gradients",
    "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "low"},
    "logical_row": 184}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish",
    "main_group": "Aquatic", "parameter": "Nutrients", "term_ids": "ENVO:00002019",
    "term_labels": "brackish water", "value": "medium"}, "logical_row": 185}, {"data":
    {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic",
    "parameter": "Pressure", "term_ids": "ENVO:00002019", "term_labels": "brackish
    water", "value": "low"}, "logical_row": 186}, {"data": {"cobo_simon_habitat":
    "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "Salinity",
    "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value": "medium"},
    "logical_row": 187}, {"data": {"cobo_simon_habitat": "NA", "env_type": "water_brackish",
    "main_group": "Aquatic", "parameter": "Structural", "term_ids": "ENVO:00002019",
    "term_labels": "brackish water", "value": "low"}, "logical_row": 188}, {"data":
    {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic",
    "parameter": "Water", "term_ids": "ENVO:00002019", "term_labels": "brackish water",
    "value": "high"}, "logical_row": 189}, {"data": {"cobo_simon_habitat": "NA", "env_type":
    "water_brackish", "main_group": "Aquatic", "parameter": "pH", "term_ids": "ENVO:00002019",
    "term_labels": "brackish water", "value": "medium"}, "logical_row": 190}, {"data":
    {"cobo_simon_habitat": "NA", "env_type": "water_brackish", "main_group": "Aquatic",
    "parameter": "salinity variability", "term_ids": "ENVO:00002019", "term_labels":
    "brackish water", "value": "wide"}, "logical_row": 191}, {"data": {"cobo_simon_habitat":
    "NA", "env_type": "water_brackish", "main_group": "Aquatic", "parameter": "temp
    variability", "term_ids": "ENVO:00002019", "term_labels": "brackish water", "value":
    "medium"}, "logical_row": 192}, {"data": {"cobo_simon_habitat": "NA", "env_type":
    "water_brackish", "main_group": "Aquatic", "parameter": "water variability", "term_ids":
    "ENVO:00002019", "term_labels": "brackish water", "value": "permanently wet"},
    "logical_row": 193}], "data/raw/madin_habitat_taxa.tsv": [{"data": {"corroborated_by":
    "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:1084519", "taxon_label":
    "Nibribacter koreensis"}, "logical_row": 361}, {"data": {"corroborated_by": "",
    "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:1124597", "taxon_label": "Magnetococcus
    marinus"}, "logical_row": 362}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019",
    "taxon_id": "NCBITaxon:1132696", "taxon_label": "Chryseobacterium rigui"}, "logical_row":
    363}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id":
    "NCBITaxon:1165090", "taxon_label": "imtechella_halotolerans"}, "logical_row":
    364}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id":
    "NCBITaxon:1194079", "taxon_label": "streptomyces_chilikensis"}, "logical_row":
    365}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id":
    "NCBITaxon:152268", "taxon_label": "bacillus_litoralis"}, "logical_row": 366},
    {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:1727163",
    "taxon_label": "Algoriphagus sp. M8-2"}, "logical_row": 367}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:205844", "taxon_label":
    "novosphingobium_pentaromativorans"}, "logical_row": 368}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:226504", "taxon_label":
    "algoriphagus_mannitolivorans"}, "logical_row": 369}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:226505", "taxon_label":
    "algoriphagus_halophilus"}, "logical_row": 370}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:226506", "taxon_label":
    "algoriphagus_ornithinivorans"}, "logical_row": 371}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:23", "taxon_label": "alteromonas_colwelliana"},
    "logical_row": 372}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019",
    "taxon_id": "NCBITaxon:231438", "taxon_label": "desulfoluna_butyratoxydans"},
    "logical_row": 373}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019",
    "taxon_id": "NCBITaxon:231440", "taxon_label": "desulfopila_aestuarii"}, "logical_row":
    374}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id":
    "NCBITaxon:231447", "taxon_label": "desulfobulbus_japonicus"}, "logical_row":
    375}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id":
    "NCBITaxon:247022", "taxon_label": "microbulbifer_maritimus"}, "logical_row":
    376}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id":
    "NCBITaxon:252230", "taxon_label": "nocardioides_ganghwensis"}, "logical_row":
    377}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id":
    "NCBITaxon:252231", "taxon_label": "Nocardioides aestuarii"}, "logical_row": 378},
    {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:252597",
    "taxon_label": "alteromonas_litorea"}, "logical_row": 379}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:255984", "taxon_label":
    "erythrobacter_aquimaris"}, "logical_row": 380}, {"data": {"corroborated_by":
    "", "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:259390", "taxon_label":
    "nocardia_takedensis"}, "logical_row": 381}, {"data": {"corroborated_by": "",
    "madin_id": "ENVO:00002019", "taxon_id": "NCBITaxon:285109", "taxon_label": "thioclava_pacifica"},
    "logical_row": 382}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019",
    "taxon_id": "NCBITaxon:288019", "taxon_label": "Yeosuana aromativorans"}, "logical_row":
    383}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id":
    "NCBITaxon:288022", "taxon_label": "kordiimonas_gwangyangensis"}, "logical_row":
    384}, {"data": {"corroborated_by": "", "madin_id": "ENVO:00002019", "taxon_id":
    "NCBITaxon:29494", "taxon_label": "vibrio_furnissii"}, "logical_row": 385}], "data/raw/madin_habitats.tsv":
    [{"data": {"label": "brackish water", "madin_id": "ENVO:00002019", "taxon_count":
    "64", "vocabulary": "ENVO"}, "logical_row": 42}], "data/raw/ontology_subclass_edges.tsv":
    [{"data": {"object": "ENVO:00002010", "predicate": "rdfs:subClassOf", "subject":
    "ENVO:00002019"}, "logical_row": 5280}], "data/raw/ontology_terms.tsv": [{"data":
    {"definition": "Water which has a higher salinity than fresh water but a lower
    salinity than marine water.", "deprecated": "", "directly_referenced": "TRUE",
    "label": "brackish water", "label_only": "FALSE", "ontology": "ENVO", "synonyms":
    "", "term_id": "ENVO:00002019"}, "logical_row": 7175}], "data/raw/prego_habitat_taxa.tsv":
    [{"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank": "1", "taxon_id":
    "NCBITaxon:1046954", "taxon_label": "Cloacimonetes bacterium SCGC AAA252-E20"},
    "logical_row": 5661}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score": "3", "rank":
    "2", "taxon_id": "NCBITaxon:1046955", "taxon_label": "Cloacimonetes bacterium
    SCGC AAA252-F02"}, "logical_row": 5662}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "3", "taxon_id": "NCBITaxon:1046956", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-G07"}, "logical_row": 5663}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "4", "taxon_id": "NCBITaxon:1046957", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-G08"}, "logical_row": 5664}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "5", "taxon_id": "NCBITaxon:1046958", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-I11"}, "logical_row": 5665}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "6", "taxon_id": "NCBITaxon:1046959", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-I16"}, "logical_row": 5666}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "7", "taxon_id": "NCBITaxon:1046960", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-K16"}, "logical_row": 5667}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "8", "taxon_id": "NCBITaxon:1046961", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-L05"}, "logical_row": 5668}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "9", "taxon_id": "NCBITaxon:1046962", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-L13"}, "logical_row": 5669}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "10", "taxon_id": "NCBITaxon:1046963", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-M08"}, "logical_row": 5670}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "11", "taxon_id": "NCBITaxon:1046964", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-N05"}, "logical_row": 5671}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "12", "taxon_id": "NCBITaxon:1046965", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-N14"}, "logical_row": 5672}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "13", "taxon_id": "NCBITaxon:1046966", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-N17"}, "logical_row": 5673}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "14", "taxon_id": "NCBITaxon:1046967", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-O02"}, "logical_row": 5674}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "15", "taxon_id": "NCBITaxon:1046970", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-O17"}, "logical_row": 5675}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "16", "taxon_id": "NCBITaxon:1046971", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-P02"}, "logical_row": 5676}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "17", "taxon_id": "NCBITaxon:1046972", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-P10"}, "logical_row": 5677}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "18", "taxon_id": "NCBITaxon:1046973", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA252-P14"}, "logical_row": 5678}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "19", "taxon_id": "NCBITaxon:1046974", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA255-B16"}, "logical_row": 5679}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "20", "taxon_id": "NCBITaxon:1046975", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA255-C20"}, "logical_row": 5680}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "21", "taxon_id": "NCBITaxon:1046978", "taxon_label": "Cloacimonetes
    bacterium SCGC AAA255-L20"}, "logical_row": 5681}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "22", "taxon_id": "NCBITaxon:1046991", "taxon_label": "Acetothermia
    bacterium SCGC AAA255-C06"}, "logical_row": 5682}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "23", "taxon_id": "NCBITaxon:1047002", "taxon_label": "Microgenomates
    bacterium SCGC AAA255-J07"}, "logical_row": 5683}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "24", "taxon_id": "NCBITaxon:1047006", "taxon_label": "Omnitrophica
    bacterium SCGC AAA252-B19"}, "logical_row": 5684}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002019", "prego_score":
    "3", "rank": "25", "taxon_id": "NCBITaxon:1047014", "taxon_label": "Aminicenantes
    bacterium SCGC AAA252-B17"}, "logical_row": 5685}], "data/raw/prego_habitats.tsv":
    [{"data": {"biolink_category": "biolink:OntologyClass", "channels": "annotated_genomes_isolates|environmental_samples",
    "direct_assertion_count": "1016", "max_prego_score": "3", "ontology": "ENVO",
    "prego_id": "ENVO:00002019", "prego_synonyms": "brackish water|brackish waters",
    "taxon_count": "1015"}, "logical_row": 80}]}'
  accessed_at: '2026-10-11T22:56:28.023779Z'
  support: supports
  locator: Exact logical TSV rows; header is row1. Neighboring source/parent matches
    excluded.
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00002019", "mapping_predicate": null, "reviewed":
    false, "route": "environments_table_self_grounded"}, "automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "EXACT", "identifier": "ENVO:00002019", "mapping_predicate":
    null, "reviewed": false, "route": "environments_table_self_grounded"}, "minted":
    "habitatmech:ENVIRONMENTS_TABLE.a814145b33", "source": "ENVIRONMENTS_TABLE", "source_id":
    "water_brackish"}, {"actual": {"category": null, "contributes_grounding": true,
    "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00002019", "mapping_predicate": null, "reviewed":
    false, "route": "madin_self_grounded"}, "automatic": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00002019", "mapping_predicate": null, "reviewed":
    false, "route": "madin_self_grounded"}, "minted": "habitatmech:MADIN.0a700a7140",
    "source": "MADIN", "source_id": "ENVO:00002019"}, {"actual": {"category": null,
    "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "EXACT", "identifier": "ENVO:00002019", "mapping_predicate":
    null, "reviewed": false, "route": "prego_self_grounded"}, "automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "EXACT", "identifier": "ENVO:00002019", "mapping_predicate":
    null, "reviewed": false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.202c26d6e8",
    "source": "PREGO", "source_id": "ENVO:00002019"}], "source_concepts": 3}'
  accessed_at: '2026-10-11T22:52:35.425310Z'
  support: supports
  locator: Executed complete-document reconstruction; all40 matched captured records
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
    [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002010": {"definitions":
    ["Water which contains a significant concentration of dissolved salts."], "deprecated":
    [], "equivalents": [], "labels": ["saline water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/ENVO_02000200"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_26710"]},
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000086"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/PATO_0001657"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["salt
    water"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002019": {"definitions":
    ["Water which has a higher salinity than fresh water but a lower salinity than
    marine water."], "deprecated": [], "equivalents": [], "labels": ["brackish water"],
    "parents": ["http://purl.obolibrary.org/obo/ENVO_00002010"], "replacements": [],
    "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym":
    [], "hasRelatedSynonym": []}}}'
  accessed_at: '2026-10-11T13:21:47.927208Z'
  support: supports
  locator: 'Same-day official OWL: named identities, typed synonyms and direct axioms;
    no snapshot refresh'
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats/aquatic/saline_water.yaml; data/habitats/aquatic/liquid_water.yaml
  summary: '{"ENVO:00002006": {"definition": "An environmental material primarily
    composed of dihydrogen oxide in its liquid form.", "grounding_status": "EXACT",
    "label": "liquid water", "parent_habitats": ["ENVO:01000815"]}, "ENVO:00002010":
    {"definition": "Water which contains a significant concentration of dissolved
    salts.", "grounding_status": "EXACT", "label": "saline water", "parent_habitats":
    ["ENVO:00002006"]}}'
  accessed_at: '2026-10-11T22:52:35.425310Z'
  support: supports
  locator: Ancestor context is not full-record review coverage of ancestors
- evidence_id: TAX0
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1017%2C1018%2C1019%2C1029756%2C1035916%2C1040984%2C104268%2C1046954%2C1046955%2C1046956%2C1046957%2C1046958%2C1046959%2C1046960%2C1046961%2C1046962%2C1046963%2C1046964%2C1046965%2C1046966%2C1046967%2C1046970%2C1046971%2C1046972%2C1046973%2C1046974%2C1046975%2C1046978%2C1046991%2C1047002%2C1047006%2C1047014%2C1048%2C1049%2C1073250%2C1084519%2C1085%2C1087448%2C109328%2C1100%2C110539%2C110639%2C1111735%2C1120961%2C1120966%2C1120998%2C1121014%2C1121403%2C1121410%2C1121416%2C1121878%2C1121879%2C1121938%2C1122176%2C1122197%2C1123027%2C1123503%2C1123517%2C1124597%2C1132696%2C1134435%2C1156985%2C1165090%2C1175486%2C118166%2C1188229%2C1194079%2C1245526%2C1257026%2C1257027%2C1264%2C1265%2C1270%2C1282%2C129578%2C129958%2C1318%2C1397696%2C1408433%2C1409%2C1423814%2C1485%2C150172%2C1512%2C152268%2C1526%2C1527%2C154046%2C1550%2C157687%2C158847%2C1596%2C1623%2C163908%2C165179%2C165813%2C1727163%2C195907%2C195913%2C202747%2C205844%2C209897%2C216903%2C226504%2C226505%2C226506%2C23%2C231438%2C231440%2C231447%2C245187%2C245188%2C247022%2C249351%2C249352%2C252230%2C252231%2C252597%2C255984%2C259390%2C266940%2C267375%2C267990%2C28122%2C285109%2C285258%2C287844%2C288019%2C288022%2C293826%2C293890%2C29494%2C29535%2C295419%2C306540%2C306541%2C317936%2C321267%2C325473%2C326442%2C329406%2C332168%2C34085%2C343403%2C364197%2C36987%2C393131%2C395491%2C411467%2C411477&retmode=xml
  summary: 'The two chunks jointly resolve all188 requested cohort IDs. This target=[{"current_id":
    "1046954", "current_name": "Cloacimonetes bacterium SCGC AAA252-E20", "frozen_label":
    "Cloacimonetes bacterium SCGC AAA252-E20", "id": "1046954", "rank": "species"},
    {"current_id": "1046955", "current_name": "Cloacimonetes bacterium SCGC AAA252-F02",
    "frozen_label": "Cloacimonetes bacterium SCGC AAA252-F02", "id": "1046955", "rank":
    "species"}, {"current_id": "1046956", "current_name": "Cloacimonetes bacterium
    SCGC AAA252-G07", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-G07", "id":
    "1046956", "rank": "species"}, {"current_id": "1046957", "current_name": "Cloacimonetes
    bacterium SCGC AAA252-G08", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-G08",
    "id": "1046957", "rank": "species"}, {"current_id": "1046958", "current_name":
    "Cloacimonetes bacterium SCGC AAA252-I11", "frozen_label": "Cloacimonetes bacterium
    SCGC AAA252-I11", "id": "1046958", "rank": "species"}, {"current_id": "1046959",
    "current_name": "Cloacimonetes bacterium SCGC AAA252-I16", "frozen_label": "Cloacimonetes
    bacterium SCGC AAA252-I16", "id": "1046959", "rank": "species"}, {"current_id":
    "1046960", "current_name": "Cloacimonetes bacterium SCGC AAA252-K16", "frozen_label":
    "Cloacimonetes bacterium SCGC AAA252-K16", "id": "1046960", "rank": "species"},
    {"current_id": "1046961", "current_name": "Cloacimonetes bacterium SCGC AAA252-L05",
    "frozen_label": "Cloacimonetes bacterium SCGC AAA252-L05", "id": "1046961", "rank":
    "species"}, {"current_id": "1046962", "current_name": "Cloacimonetes bacterium
    SCGC AAA252-L13", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-L13", "id":
    "1046962", "rank": "species"}, {"current_id": "1046963", "current_name": "Cloacimonetes
    bacterium SCGC AAA252-M08", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-M08",
    "id": "1046963", "rank": "species"}, {"current_id": "1046964", "current_name":
    "Cloacimonetes bacterium SCGC AAA252-N05", "frozen_label": "Cloacimonetes bacterium
    SCGC AAA252-N05", "id": "1046964", "rank": "species"}, {"current_id": "1046965",
    "current_name": "Cloacimonetes bacterium SCGC AAA252-N14", "frozen_label": "Cloacimonetes
    bacterium SCGC AAA252-N14", "id": "1046965", "rank": "species"}, {"current_id":
    "1046966", "current_name": "Cloacimonetes bacterium SCGC AAA252-N17", "frozen_label":
    "Cloacimonetes bacterium SCGC AAA252-N17", "id": "1046966", "rank": "species"},
    {"current_id": "1046967", "current_name": "Cloacimonetes bacterium SCGC AAA252-O02",
    "frozen_label": "Cloacimonetes bacterium SCGC AAA252-O02", "id": "1046967", "rank":
    "species"}, {"current_id": "1046970", "current_name": "Cloacimonetes bacterium
    SCGC AAA252-O17", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-O17", "id":
    "1046970", "rank": "species"}, {"current_id": "1046971", "current_name": "Cloacimonetes
    bacterium SCGC AAA252-P02", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-P02",
    "id": "1046971", "rank": "species"}, {"current_id": "1046972", "current_name":
    "Cloacimonetes bacterium SCGC AAA252-P10", "frozen_label": "Cloacimonetes bacterium
    SCGC AAA252-P10", "id": "1046972", "rank": "species"}, {"current_id": "1046973",
    "current_name": "Cloacimonetes bacterium SCGC AAA252-P14", "frozen_label": "Cloacimonetes
    bacterium SCGC AAA252-P14", "id": "1046973", "rank": "species"}, {"current_id":
    "1046974", "current_name": "Cloacimonetes bacterium SCGC AAA255-B16", "frozen_label":
    "Cloacimonetes bacterium SCGC AAA255-B16", "id": "1046974", "rank": "species"},
    {"current_id": "1046975", "current_name": "Cloacimonetes bacterium SCGC AAA255-C20",
    "frozen_label": "Cloacimonetes bacterium SCGC AAA255-C20", "id": "1046975", "rank":
    "species"}, {"current_id": "1046978", "current_name": "Cloacimonetes bacterium
    SCGC AAA255-L20", "frozen_label": "Cloacimonetes bacterium SCGC AAA255-L20", "id":
    "1046978", "rank": "species"}, {"current_id": "1046991", "current_name": "Acetothermia
    bacterium SCGC AAA255-C06", "frozen_label": "Acetothermia bacterium SCGC AAA255-C06",
    "id": "1046991", "rank": "species"}, {"current_id": "1047002", "current_name":
    "Microgenomates bacterium SCGC AAA255-J07", "frozen_label": "Microgenomates bacterium
    SCGC AAA255-J07", "id": "1047002", "rank": "species"}, {"current_id": "1047006",
    "current_name": "Omnitrophica bacterium SCGC AAA252-B19", "frozen_label": "Omnitrophica
    bacterium SCGC AAA252-B19", "id": "1047006", "rank": "species"}, {"current_id":
    "1047014", "current_name": "Aminicenantes bacterium SCGC AAA252-B17", "frozen_label":
    "Aminicenantes bacterium SCGC AAA252-B17", "id": "1047014", "rank": "species"},
    {"current_id": "1084519", "current_name": "Nibribacter koreensis", "frozen_label":
    "Nibribacter koreensis", "id": "1084519", "rank": "species"}, {"current_id": "1124597",
    "current_name": "Magnetococcus marinus", "frozen_label": "Magnetococcus marinus",
    "id": "1124597", "rank": "species"}, {"current_id": "1132696", "current_name":
    "Chryseobacterium rigui", "frozen_label": "Chryseobacterium rigui", "id": "1132696",
    "rank": "species"}, {"current_id": "1165090", "current_name": "Imtechella halotolerans",
    "frozen_label": "imtechella_halotolerans", "id": "1165090", "rank": "species"},
    {"current_id": "1194079", "current_name": "Streptomyces chilikensis", "frozen_label":
    "streptomyces_chilikensis", "id": "1194079", "rank": "species"}, {"current_id":
    "152268", "current_name": "Metabacillus litoralis", "frozen_label": "bacillus_litoralis",
    "id": "152268", "rank": "species"}, {"current_id": "1727163", "current_name":
    "Algoriphagus sanaruensis", "frozen_label": "Algoriphagus sp. M8-2", "id": "1727163",
    "rank": "species"}, {"current_id": "205844", "current_name": "Novosphingobium
    pentaromativorans", "frozen_label": "novosphingobium_pentaromativorans", "id":
    "205844", "rank": "species"}, {"current_id": "226504", "current_name": "Algoriphagus
    mannitolivorans", "frozen_label": "algoriphagus_mannitolivorans", "id": "226504",
    "rank": "species"}, {"current_id": "226505", "current_name": "Algoriphagus halophilus",
    "frozen_label": "algoriphagus_halophilus", "id": "226505", "rank": "species"},
    {"current_id": "226506", "current_name": "Algoriphagus ornithinivorans", "frozen_label":
    "algoriphagus_ornithinivorans", "id": "226506", "rank": "species"}, {"current_id":
    "23", "current_name": "Shewanella colwelliana", "frozen_label": "alteromonas_colwelliana",
    "id": "23", "rank": "species"}, {"current_id": "231438", "current_name": "Desulfoluna
    butyratoxydans", "frozen_label": "desulfoluna_butyratoxydans", "id": "231438",
    "rank": "species"}, {"current_id": "231440", "current_name": "Desulfopila aestuarii",
    "frozen_label": "desulfopila_aestuarii", "id": "231440", "rank": "species"}, {"current_id":
    "231447", "current_name": "Desulfogranum japonicum", "frozen_label": "desulfobulbus_japonicus",
    "id": "231447", "rank": "species"}, {"current_id": "247022", "current_name": "Microbulbifer
    maritimus", "frozen_label": "microbulbifer_maritimus", "id": "247022", "rank":
    "species"}, {"current_id": "252230", "current_name": "Nocardioides ganghwensis",
    "frozen_label": "nocardioides_ganghwensis", "id": "252230", "rank": "species"},
    {"current_id": "252231", "current_name": "Nocardioides aestuarii", "frozen_label":
    "Nocardioides aestuarii", "id": "252231", "rank": "species"}, {"current_id": "252597",
    "current_name": "Alteromonas litorea", "frozen_label": "alteromonas_litorea",
    "id": "252597", "rank": "species"}, {"current_id": "255984", "current_name": "Qipengyuania
    aquimaris", "frozen_label": "erythrobacter_aquimaris", "id": "255984", "rank":
    "species"}, {"current_id": "259390", "current_name": "Nocardia takedensis", "frozen_label":
    "nocardia_takedensis", "id": "259390", "rank": "species"}, {"current_id": "285109",
    "current_name": "Thioclava pacifica", "frozen_label": "thioclava_pacifica", "id":
    "285109", "rank": "species"}, {"current_id": "288019", "current_name": "Yeosuana
    aromativorans", "frozen_label": "Yeosuana aromativorans", "id": "288019", "rank":
    "species"}, {"current_id": "288022", "current_name": "Kordiimonas gwangyangensis",
    "frozen_label": "kordiimonas_gwangyangensis", "id": "288022", "rank": "species"},
    {"current_id": "29494", "current_name": "Vibrio furnissii", "frozen_label": "vibrio_furnissii",
    "id": "29494", "rank": "species"}]. All noncanonical supplied names match normalized
    spelling or retained aliases. Resolution does not establish occurrence.'
  accessed_at: '2026-10-11T22:37:49.789865Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank and OtherNames
  snapshot_sha256: 0e343fd7441e46d2192a08a830ce60811f8d2d55fd5762bd925ed00e6e485bf3
- evidence_id: TAX1
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=411485%2C411901%2C418643%2C428125%2C435590%2C445336%2C449306%2C457391%2C457424%2C457427%2C477974%2C498761%2C502025%2C523845%2C52560%2C53245%2C537937%2C54121%2C551275%2C551789%2C55518%2C556258%2C562%2C56780%2C568099%2C616997%2C6376%2C643867%2C647171%2C657014%2C668820%2C693661%2C69670%2C710685%2C717231%2C889378%2C94122%2C999547&retmode=xml
  summary: 'The two chunks jointly resolve all188 requested cohort IDs. This target=[{"current_id":
    "1046954", "current_name": "Cloacimonetes bacterium SCGC AAA252-E20", "frozen_label":
    "Cloacimonetes bacterium SCGC AAA252-E20", "id": "1046954", "rank": "species"},
    {"current_id": "1046955", "current_name": "Cloacimonetes bacterium SCGC AAA252-F02",
    "frozen_label": "Cloacimonetes bacterium SCGC AAA252-F02", "id": "1046955", "rank":
    "species"}, {"current_id": "1046956", "current_name": "Cloacimonetes bacterium
    SCGC AAA252-G07", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-G07", "id":
    "1046956", "rank": "species"}, {"current_id": "1046957", "current_name": "Cloacimonetes
    bacterium SCGC AAA252-G08", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-G08",
    "id": "1046957", "rank": "species"}, {"current_id": "1046958", "current_name":
    "Cloacimonetes bacterium SCGC AAA252-I11", "frozen_label": "Cloacimonetes bacterium
    SCGC AAA252-I11", "id": "1046958", "rank": "species"}, {"current_id": "1046959",
    "current_name": "Cloacimonetes bacterium SCGC AAA252-I16", "frozen_label": "Cloacimonetes
    bacterium SCGC AAA252-I16", "id": "1046959", "rank": "species"}, {"current_id":
    "1046960", "current_name": "Cloacimonetes bacterium SCGC AAA252-K16", "frozen_label":
    "Cloacimonetes bacterium SCGC AAA252-K16", "id": "1046960", "rank": "species"},
    {"current_id": "1046961", "current_name": "Cloacimonetes bacterium SCGC AAA252-L05",
    "frozen_label": "Cloacimonetes bacterium SCGC AAA252-L05", "id": "1046961", "rank":
    "species"}, {"current_id": "1046962", "current_name": "Cloacimonetes bacterium
    SCGC AAA252-L13", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-L13", "id":
    "1046962", "rank": "species"}, {"current_id": "1046963", "current_name": "Cloacimonetes
    bacterium SCGC AAA252-M08", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-M08",
    "id": "1046963", "rank": "species"}, {"current_id": "1046964", "current_name":
    "Cloacimonetes bacterium SCGC AAA252-N05", "frozen_label": "Cloacimonetes bacterium
    SCGC AAA252-N05", "id": "1046964", "rank": "species"}, {"current_id": "1046965",
    "current_name": "Cloacimonetes bacterium SCGC AAA252-N14", "frozen_label": "Cloacimonetes
    bacterium SCGC AAA252-N14", "id": "1046965", "rank": "species"}, {"current_id":
    "1046966", "current_name": "Cloacimonetes bacterium SCGC AAA252-N17", "frozen_label":
    "Cloacimonetes bacterium SCGC AAA252-N17", "id": "1046966", "rank": "species"},
    {"current_id": "1046967", "current_name": "Cloacimonetes bacterium SCGC AAA252-O02",
    "frozen_label": "Cloacimonetes bacterium SCGC AAA252-O02", "id": "1046967", "rank":
    "species"}, {"current_id": "1046970", "current_name": "Cloacimonetes bacterium
    SCGC AAA252-O17", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-O17", "id":
    "1046970", "rank": "species"}, {"current_id": "1046971", "current_name": "Cloacimonetes
    bacterium SCGC AAA252-P02", "frozen_label": "Cloacimonetes bacterium SCGC AAA252-P02",
    "id": "1046971", "rank": "species"}, {"current_id": "1046972", "current_name":
    "Cloacimonetes bacterium SCGC AAA252-P10", "frozen_label": "Cloacimonetes bacterium
    SCGC AAA252-P10", "id": "1046972", "rank": "species"}, {"current_id": "1046973",
    "current_name": "Cloacimonetes bacterium SCGC AAA252-P14", "frozen_label": "Cloacimonetes
    bacterium SCGC AAA252-P14", "id": "1046973", "rank": "species"}, {"current_id":
    "1046974", "current_name": "Cloacimonetes bacterium SCGC AAA255-B16", "frozen_label":
    "Cloacimonetes bacterium SCGC AAA255-B16", "id": "1046974", "rank": "species"},
    {"current_id": "1046975", "current_name": "Cloacimonetes bacterium SCGC AAA255-C20",
    "frozen_label": "Cloacimonetes bacterium SCGC AAA255-C20", "id": "1046975", "rank":
    "species"}, {"current_id": "1046978", "current_name": "Cloacimonetes bacterium
    SCGC AAA255-L20", "frozen_label": "Cloacimonetes bacterium SCGC AAA255-L20", "id":
    "1046978", "rank": "species"}, {"current_id": "1046991", "current_name": "Acetothermia
    bacterium SCGC AAA255-C06", "frozen_label": "Acetothermia bacterium SCGC AAA255-C06",
    "id": "1046991", "rank": "species"}, {"current_id": "1047002", "current_name":
    "Microgenomates bacterium SCGC AAA255-J07", "frozen_label": "Microgenomates bacterium
    SCGC AAA255-J07", "id": "1047002", "rank": "species"}, {"current_id": "1047006",
    "current_name": "Omnitrophica bacterium SCGC AAA252-B19", "frozen_label": "Omnitrophica
    bacterium SCGC AAA252-B19", "id": "1047006", "rank": "species"}, {"current_id":
    "1047014", "current_name": "Aminicenantes bacterium SCGC AAA252-B17", "frozen_label":
    "Aminicenantes bacterium SCGC AAA252-B17", "id": "1047014", "rank": "species"},
    {"current_id": "1084519", "current_name": "Nibribacter koreensis", "frozen_label":
    "Nibribacter koreensis", "id": "1084519", "rank": "species"}, {"current_id": "1124597",
    "current_name": "Magnetococcus marinus", "frozen_label": "Magnetococcus marinus",
    "id": "1124597", "rank": "species"}, {"current_id": "1132696", "current_name":
    "Chryseobacterium rigui", "frozen_label": "Chryseobacterium rigui", "id": "1132696",
    "rank": "species"}, {"current_id": "1165090", "current_name": "Imtechella halotolerans",
    "frozen_label": "imtechella_halotolerans", "id": "1165090", "rank": "species"},
    {"current_id": "1194079", "current_name": "Streptomyces chilikensis", "frozen_label":
    "streptomyces_chilikensis", "id": "1194079", "rank": "species"}, {"current_id":
    "152268", "current_name": "Metabacillus litoralis", "frozen_label": "bacillus_litoralis",
    "id": "152268", "rank": "species"}, {"current_id": "1727163", "current_name":
    "Algoriphagus sanaruensis", "frozen_label": "Algoriphagus sp. M8-2", "id": "1727163",
    "rank": "species"}, {"current_id": "205844", "current_name": "Novosphingobium
    pentaromativorans", "frozen_label": "novosphingobium_pentaromativorans", "id":
    "205844", "rank": "species"}, {"current_id": "226504", "current_name": "Algoriphagus
    mannitolivorans", "frozen_label": "algoriphagus_mannitolivorans", "id": "226504",
    "rank": "species"}, {"current_id": "226505", "current_name": "Algoriphagus halophilus",
    "frozen_label": "algoriphagus_halophilus", "id": "226505", "rank": "species"},
    {"current_id": "226506", "current_name": "Algoriphagus ornithinivorans", "frozen_label":
    "algoriphagus_ornithinivorans", "id": "226506", "rank": "species"}, {"current_id":
    "23", "current_name": "Shewanella colwelliana", "frozen_label": "alteromonas_colwelliana",
    "id": "23", "rank": "species"}, {"current_id": "231438", "current_name": "Desulfoluna
    butyratoxydans", "frozen_label": "desulfoluna_butyratoxydans", "id": "231438",
    "rank": "species"}, {"current_id": "231440", "current_name": "Desulfopila aestuarii",
    "frozen_label": "desulfopila_aestuarii", "id": "231440", "rank": "species"}, {"current_id":
    "231447", "current_name": "Desulfogranum japonicum", "frozen_label": "desulfobulbus_japonicus",
    "id": "231447", "rank": "species"}, {"current_id": "247022", "current_name": "Microbulbifer
    maritimus", "frozen_label": "microbulbifer_maritimus", "id": "247022", "rank":
    "species"}, {"current_id": "252230", "current_name": "Nocardioides ganghwensis",
    "frozen_label": "nocardioides_ganghwensis", "id": "252230", "rank": "species"},
    {"current_id": "252231", "current_name": "Nocardioides aestuarii", "frozen_label":
    "Nocardioides aestuarii", "id": "252231", "rank": "species"}, {"current_id": "252597",
    "current_name": "Alteromonas litorea", "frozen_label": "alteromonas_litorea",
    "id": "252597", "rank": "species"}, {"current_id": "255984", "current_name": "Qipengyuania
    aquimaris", "frozen_label": "erythrobacter_aquimaris", "id": "255984", "rank":
    "species"}, {"current_id": "259390", "current_name": "Nocardia takedensis", "frozen_label":
    "nocardia_takedensis", "id": "259390", "rank": "species"}, {"current_id": "285109",
    "current_name": "Thioclava pacifica", "frozen_label": "thioclava_pacifica", "id":
    "285109", "rank": "species"}, {"current_id": "288019", "current_name": "Yeosuana
    aromativorans", "frozen_label": "Yeosuana aromativorans", "id": "288019", "rank":
    "species"}, {"current_id": "288022", "current_name": "Kordiimonas gwangyangensis",
    "frozen_label": "kordiimonas_gwangyangensis", "id": "288022", "rank": "species"},
    {"current_id": "29494", "current_name": "Vibrio furnissii", "frozen_label": "vibrio_furnissii",
    "id": "29494", "rank": "species"}]. All noncanonical supplied names match normalized
    spelling or retained aliases. Resolution does not establish occurrence.'
  accessed_at: '2026-10-11T22:37:51.736612Z'
  support: supports
  locator: NCBI TaxId, ScientificName, Rank and OtherNames
  snapshot_sha256: 4a2373fb2f829df8e02096f659a1031455b733542e6181aff3dc4a7746255349
- evidence_id: SEARCH
  kind: search
  reference: curation; history; research; reports; reviews; data/raw; data/habitats;
    conf
  summary: 'Identifier, label, slug and exact source-path searches included ignored/hidden
    files in these roots; coverage used Path.rglob. No earlier structured observation
    of this target found. Legacy reports were indexed; only specifically cited historical
    reports were read in full. Upstream search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe",
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
    "exit_code": 0, "matches": [], "stderr": ""}]}'
  accessed_at: '2026-10-11T22:52:35.425310Z'
  support: supports
  locator: Bounded searches, not global absence claims
  search_scope: 'Identifier, label, slug and exact source-path searches included ignored/hidden
    files in these roots; coverage used Path.rglob. No earlier structured observation
    of this target found. Legacy reports were indexed; only specifically cited historical
    reports were read in full. Upstream search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe",
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
    "exit_code": 0, "matches": [], "stderr": ""}]}'
- evidence_id: ISSUES
  kind: database
  reference: https://github.com/CultureBotAI/HabitatMech/issues
  summary: All-state946-issue title/body census inspected for overlap. Shared1249
    and1398 apply where cited.1259 concerns a separate Lake biofilm source,1423 different
    records, and1638 the bioreactor graph; none is treated as this target repaired.
    Comments were not exhaustively crawled.
  accessed_at: '2026-10-11T22:52:35.425310Z'
  support: supports
  locator: GitHub CLI census and selected full issue bodies
- evidence_id: GRAPH
  kind: record_content
  reference: curation/causal_graphs/brackish_water.yaml
  summary: 'Entire overlay and generated graph read: 16 nodes and 17 edges. Exact
    source references and node scopes assessed.'
  accessed_at: '2026-10-11T22:52:35.425310Z'
  support: supports
  locator: All nodes, edges, descriptions and evidence
- evidence_id: PMID-15006771
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15006771+AND+SRC%3AMED&format=json&resultType=core
  summary: 'Bibliographic identity and full abstract inspected: Microbial biogeography
    along an estuarine salinity gradient: combined influences of bacterial growth
    and residence time.; DOI:10.1128/aem.70.3.1494-1505.2004. Abstract evidence only;
    causal details distinguished edge by edge.'
  accessed_at: '2026-10-11T22:37:57.158738Z'
  support: supports
  locator: EuropePMC core metadata and abstract
  snapshot_sha256: 5473252a39f8c4d48f774b50dcb3b619c1ea33fe3015b4ec8771c6e3cc894229
- evidence_id: PMID-21663439
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21663439+AND+SRC%3AMED&format=json&resultType=core
  summary: 'Bibliographic identity and full abstract inspected: Bacterial osmoregulation:
    a paradigm for the study of cellular homeostasis.; DOI:10.1146/annurev-micro-090110-102815.
    Abstract evidence only; causal details distinguished edge by edge.'
  accessed_at: '2026-10-11T22:37:59.208089Z'
  support: supports
  locator: EuropePMC core metadata and abstract
  snapshot_sha256: 87a1f749053ec4d6a7eb5db6a15521d4437295b6cdbcb4078af051befaa4f5b1
- evidence_id: PMID-22895159
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22895159+AND+SRC%3AMED&format=json&resultType=core
  summary: 'Bibliographic identity and full abstract inspected: Bacterial diversity,
    community structure and potential growth rates along an estuarine salinity gradient.;
    DOI:10.1038/ismej.2012.93. Abstract evidence only; causal details distinguished
    edge by edge.'
  accessed_at: '2026-10-11T22:38:00.269215Z'
  support: supports
  locator: EuropePMC core metadata and abstract
  snapshot_sha256: bd7134735bb7d6769dd1c381c1b01a76ba7ca8ec8ab7a45308c2f6236cc3c7f3
- evidence_id: TEE
  kind: primary_source
  reference: https://link.springer.com/article/10.1186/s40168-021-01145-3
  summary: Primary spatial survey distinguishes water and sediment communities and
    combines genes/transcripts with geochemistry. Salinity-related strategies are
    supported, but it is not a temporal manipulation isolating fluctuating-salinity
    stress.
  accessed_at: '2026-10-11T22:45:04.953880Z'
  support: supports
  locator: Publisher Introduction and Results through Distinct non-saline and saline
    osmoregulation strategies; PMID34544488 / DOI10.1186/s40168-021-01145-3
  snapshot_sha256: 306eb7e86f39305e566860b50b85a165884f0d45e1e8d8667f311d6f10c93c9c
- evidence_id: WU
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11200988/fullTextXML
  summary: Primary estuary metagenomic study supports salt-in and compatible-solute
    machinery and associations with salinity. Its genomic potential and relative abundance
    are not direct physiological flux or experimental selection measurements.
  accessed_at: '2026-10-11T22:45:00.702115Z'
  support: supports
  locator: Body paragraphs0-12 and35-42; DOI10.1186/s40168-024-01817-w
  snapshot_sha256: 3110325f660ea1d154942a99b6c2d67281c4cb3d19dd9f5884d41683caae246f
- evidence_id: LEGACY
  kind: record_content
  reference: reports/yaml_record_review/20260923T140218Z-brackish_water.md
  summary: Historical report read in full. Its blanket graph-support conclusion is
    not adopted; this observation reassesses every edge. Historical unstructured findings
    are not automatically retired.
  accessed_at: '2026-10-11T22:52:35.425310Z'
  support: context_only
  locator: Historical graph assessment and findings
assessments:
- assessment_id: EDGE-brackish_water_receives_freshwater
  area: evidence
  topic: brackish_water_receives_freshwater
  outcome: supported
  summary: Crump abstract supports freshwater advection in its estuarine example.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-brackish_water_receives_seawater
  area: evidence
  topic: brackish_water_receives_seawater
  outcome: supported
  summary: Crump abstract supports marine advection in the same bounded setting.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-brackish_water_has_tidal_mixing
  area: evidence
  topic: brackish_water_has_tidal_mixing
  outcome: supported
  summary: Tee introduction supports tidal exchange in the studied lagoon.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-brackish_water_has_residence_time
  area: evidence
  topic: brackish_water_has_residence_time
  outcome: supported
  summary: Crump abstract explicitly relates community development to residence time.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-tidal_mixing_creates_salinity_variability
  area: evidence
  topic: tidal_mixing_creates_salinity_variability
  outcome: supported
  summary: Tee introduction supports periodically changing salinity with tidal exchange.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-freshwater_seawater_mixing_sets_intermediate_salinity
  area: evidence
  topic: freshwater_seawater_mixing_sets_intermediate_salinity
  outcome: supported
  summary: Campbell abstract supports mixing along the Delaware estuarine gradient.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-brackish_water_has_intermediate_salinity
  area: evidence
  topic: brackish_water_has_intermediate_salinity
  outcome: supported
  summary: ENVO supplies the material definition; Campbell supplies a measured example,
    not a universal numerical threshold.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-intermediate_salinity_imposes_osmotic_stress
  area: evidence
  topic: intermediate_salinity_imposes_osmotic_stress
  outcome: supported
  summary: Wood abstract supports osmotic adjustment; stress depends on change and
    the receiving organism, not an intrinsically harmful brackish state.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-salinity_variability_intensifies_osmotic_stress
  area: evidence
  topic: salinity_variability_intensifies_osmotic_stress
  outcome: concern
  summary: Tee sampled a spatial transect. A stronger temporal intensification mechanism
    is not directly demonstrated by those observations.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-osmotic_stress_selects_osmoregulatory_transport
  area: evidence
  topic: osmotic_stress_selects_osmoregulatory_transport
  outcome: concern
  summary: Wood supports transport activation and Wu metagenomic associations; measured
    evolutionary selection is not established. Transport and synthesis also differ.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-transport_enables_compatible_solutes
  area: evidence
  topic: transport_enables_compatible_solutes
  outcome: supported
  summary: Wu introduction supports uptake or biosynthesis of compatible solutes;
    synthesis should not be assigned to transport itself.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-transport_enables_salt_in_strategy
  area: evidence
  topic: transport_enables_salt_in_strategy
  outcome: supported
  summary: Wu supports ion transport as salt-in machinery; genomic potential is not
    measured intracellular accumulation in every sample.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-osmotic_stress_filters_freshwater_bacteria
  area: evidence
  topic: osmotic_stress_filters_freshwater_bacteria
  outcome: concern
  summary: Campbell reports rRNA:rDNA growth-potential proxies. The specific osmotic-filter
    mechanism is an interpretation, not a directly measured cause.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-osmotic_stress_filters_marine_bacteria
  area: evidence
  topic: osmotic_stress_filters_marine_bacteria
  outcome: unknown
  summary: Crump abstract reports marine advection and seasonal communities but does
    not isolate osmotic filtering; publisher full text returned403.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-salinity_gradient_drives_community_turnover
  area: evidence
  topic: salinity_gradient_drives_community_turnover
  outcome: supported
  summary: Crump and Campbell associate turnover with salinity and other factors,
    not salinity as a uniquely established cause.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-growth_and_residence_time_establish_estuarine_bacteria
  area: evidence
  topic: growth_and_residence_time_establish_estuarine_bacteria
  outcome: concern
  summary: Crump supports doubling time shorter than residence time; growth faster
    than a duration is dimensionally incorrect wording.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: EDGE-residence_time_modulates_estuarine_establishment
  area: evidence
  topic: residence_time_modulates_estuarine_establishment
  outcome: supported
  summary: Crump supports conditional establishment when growth and hydrological timescales
    permit retention.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
- assessment_id: IDENTITY
  area: identity
  topic: Identity, definition and source interpretation
  outcome: supported
  summary: ENVO:00002019 denotes saline water material intermediate between fresh
    and marine water, distinct from a water body. The estuarine example graph has
    17 edges; community typing and some causal extrapolations need correction, while
    mixing and conditional growth/residence observations are supported. Ten qualitative
    source bands and reported taxa remain source-specific.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
- assessment_id: HIERARCHY
  area: grounding
  topic: All parent-contribution routes and mapping scope
  outcome: supported
  summary: ENVO:00002019 denotes saline water material intermediate between fresh
    and marine water, distinct from a water body. The estuarine example graph has
    17 edges; community typing and some causal extrapolations need correction, while
    mixing and conditional growth/residence observations are supported. Ten qualitative
    source bands and reported taxa remain source-specific. Ontology, source-path,
    ambiguous-leaf and authored-definition contributions were distinguished.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - R
  - RAW
  - CODE
  - ONT
  - PARENT
- assessment_id: PROVENANCE
  area: provenance
  topic: Every source, count unit and native status
  outcome: supported
  summary: 'Complete reconstruction preserves 3 source concepts and 0 ITEM-reviewed
    contributors. Actual attestations=[{"source": "ENVIRONMENTS_TABLE", "source_id":
    "water_brackish", "source_label": "water_brackish", "notes": "Physicochemical
    parameter bands from kg-microbe''s environment table."}, {"source": "MADIN", "source_id":
    "ENVO:00002019", "source_label": "brackish water", "assertion_count": 64, "assertion_unit":
    "TAXON"}, {"source": "PREGO", "source_id": "ENVO:00002019", "source_label": "brackish
    water", "assertion_count": 1015, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels":
    "annotated_genomes_isolates|environmental_samples"}]. Unlike units are not summed.
    Omitted zero direct counts do not mean ecological absence; this review does not
    promote native status.'
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - R
  - RAW
  - CODE
  - RULES
- assessment_id: TAXA
  area: evidence
  topic: Source-reported association versus characteristic presence
  outcome: supported
  summary: All emitted taxon identifiers resolve; normalized spellings and old aliases
    explain supplied-label differences. Full reconstruction retains ranks, scores,
    pools and corroborations. No is_characteristic assertion is present; neither resolution
    nor a source score proves occurrence, abundance or ecological universality.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - R
  - RAW
  - TAX0
  - TAX1
  - RULES
- assessment_id: PARAMETERS
  area: evidence
  topic: Qualitative source bands and triad roles
  outcome: supported
  summary: All 10 entries reproduce the exact single-term environment-table source.
    These qualitative descriptors are source-attributed, not measured universal thresholds.
    Multi-term environments are not attached for a single component. No MIxS broad/local/medium
    entry is silently promoted to identity.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - R
  - RAW
  - CODE
  - RULES
- assessment_id: COMPLETENESS
  area: completeness
  topic: Optional fields and biological evidence boundaries
  outcome: supported
  summary: Optional missing definitions, datasets or discussions are not defects solely
    because they are empty. Every asserted graph edge is individually assessed above.
    No named gene, locus, regulator, strain-specific transcriptome or expression-module
    claim in this record calls for an iModulonDB query; generic enzymes/osmoregulation
    and habitat associations do not specify an applicable organism/dataset.
  target_ids:
  - ENVO:00002019
  evidence_ids:
  - R
  - RAW
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: envo-00002019-transport-synthesis-wording
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Transport is described as synthesizing solutes
  description: The osmoregulatory transport description conflates import/export with
    biosynthesis. Compatible-solute production and transport are distinct mechanisms
    even when both contribute to homeostasis.
  target_ids:
  - ENVO:00002019
  field_paths:
  - causal_graphs[0].edges
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Transport and synthesis descriptions
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Bounded wording or provenance limitation; identity is not
    disproved.
- finding_id: F2
  issue_key: envo-00002019-growth-timescale-wording
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Growth rate is compared directly with a residence duration
  description: The growth-establishment edge says growth is faster than hydrologic
    residence time. Its source and notes instead compare doubling time with residence
    time; the intended conditional result is supported but the description mixes dimensions.
  target_ids:
  - ENVO:00002019
  field_paths:
  - causal_graphs[0].edges
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Growth/residence description
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Bounded wording or provenance limitation; identity is not
    disproved.
- finding_id: F3
  issue_key: envo-00002019-community-node-type
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Mixed microbial assemblages are typed as taxa
  description: freshwater_bacterioplankton, marine_bacterioplankton and estuarine_bacterioplankton
    do not denote an organism or clade. Native COMMUNITY is available, so a process
    type or new schema enum is not an appropriate default replacement.
  target_ids:
  - ENVO:00002019
  field_paths:
  - causal_graphs[0].nodes
  evidence_ids:
  - GRAPH
  - RULES
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Exact node typing
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material hierarchy, scope, entity typing or comparison-contract
    defect.
- finding_id: F4
  issue_key: envo-00002019-causal-scope-support
  category: scope
  severity: major
  status: open
  certainty: provisional
  title: Some causal scope and detailed evidence remain unsupported
  description: The estuarine example needs explicit conditional scope in its generic
    description. Temporal stress intensification and osmotic filtering exceed the
    inspected spatial, proxy or abstract evidence; metagenomic association is not
    directly measured physiological selection. This does not show that the mechanisms
    are false.
  target_ids:
  - ENVO:00002019
  field_paths:
  - causal_graphs[0].description
  - causal_graphs[0].edges
  evidence_ids:
  - GRAPH
  - RULES
  - ONT
  - PMID-15006771
  - PMID-21663439
  - PMID-22895159
  - TEE
  - WU
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Conditional scope and claim-level evidence
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material hierarchy, scope, entity typing or comparison-contract
    defect.
actions:
- action_id: A1
  description: Separate transport from biosynthesis or widen the node to an explicitly
    supported osmoregulatory system; preserve the two strategy branches and evidence
    limitations.
  finding_ids:
  - F1
  target_ids:
  - ENVO:00002019
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Transport and synthesis descriptions
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained inputs with exact source/edge keys; preserve independent
    parents, identities, source counts/units and native lifecycle.
  - Inspect claim-level sources; append required curation history, add focused regressions,
    inspect a seed canary and regenerate affected products.
  - Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity
    and full QC; save a linked successor for each finding disposition.
  - Compare actual semantic-map inputs and perform genuine regeneration when changed;
    do not substitute a checksum-only refresh.
- action_id: A2
  description: Express the condition as a doubling time shorter than water residence
    time, or compare growth and flushing rates with consistent units; retain the seasonal
    study scope.
  finding_ids:
  - F2
  target_ids:
  - ENVO:00002019
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Growth/residence description
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained inputs with exact source/edge keys; preserve independent
    parents, identities, source counts/units and native lifecycle.
  - Inspect claim-level sources; append required curation history, add focused regressions,
    inspect a seed canary and regenerate affected products.
  - Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity
    and full QC; save a linked successor for each finding disposition.
  - Compare actual semantic-map inputs and perform genuine regeneration when changed;
    do not substitute a checksum-only refresh.
- action_id: A3
  description: Use COMMUNITY for the assemblage nodes. For physiologically defined
    subpopulations, select a supported community/state representation without inventing
    a clade or converting the entity into a process. Preserve stable IDs where semantics
    are unchanged and validate rendering.
  finding_ids:
  - F3
  target_ids:
  - ENVO:00002019
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Exact node typing
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained inputs with exact source/edge keys; preserve independent
    parents, identities, source counts/units and native lifecycle.
  - Inspect claim-level sources; append required curation history, add focused regressions,
    inspect a seed canary and regenerate affected products.
  - Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity
    and full QC; save a linked successor for each finding disposition.
  - Compare actual semantic-map inputs and perform genuine regeneration when changed;
    do not substitute a checksum-only refresh.
- action_id: A4
  description: Retain supported edges, qualify context and causal strength, retrieve
    outstanding passages, and replace title-like snippets with short exact evidence
    and precise locators. Do not equate a resolving reference with claim support.
  finding_ids:
  - F4
  target_ids:
  - ENVO:00002019
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/brackish_water.yaml
    role: Conditional scope and claim-level evidence
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained inputs with exact source/edge keys; preserve independent
    parents, identities, source counts/units and native lifecycle.
  - Inspect claim-level sources; append required curation history, add focused regressions,
    inspect a seed canary and regenerate affected products.
  - Pass schema, strict, product-label, corpus reproduction, causal/history, review-integrity
    and full QC; save a linked successor for each finding disposition.
  - Compare actual semantic-map inputs and perform genuine regeneration when changed;
    do not substitute a checksum-only refresh.
limitations:
- Completed assessment is not a clean scientific verdict or proof of every original
  assertion.
- Only first3 exact BioSample/Organism descriptions per sheet were individually interpreted,
  except all12 carbonate organism descriptions. Other matches and study joins were
  indexed, not individually assessed.
- Original frozen membership was not fully reconstructed; no ontology, taxonomy or
  source snapshot was refreshed.
- Same-agent review, not independent approval. No habitat data, native status, history
  or GitHub mutation.
- SSSOM/KGX conformance with current kg-microbe modeling was not audited; shared1398
  remains open.
- Whole-corpus review remains incomplete; ancestor reads and source indexing add no
  target coverage.
- Crump and Wood were assessed from abstracts after publisher requests returned403;
  Campbell was assessed from its abstract. Selected Tee and Wu primary full-text sections
  were inspected. Unknown detailed edge support remains open; title fragments alone
  are not proof. No correction notices were present in retrieved core metadata, not
  proof that none exist elsewhere.
notes:
- New immutable observation only; curation and publication are separate work.
- No prior structured target observation found; historical reports are preserved and
  are not silently retired.
tags:
- habitatmech
- aquatic
- record-review
- scientific-review
```
