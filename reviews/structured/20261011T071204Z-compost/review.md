# Scientific record review: compost

- Review: 20261011T071204Z-compost
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T07:00:29.668504Z
- Finished UTC: 2026-10-11T07:12:04.137068Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

ENVO compost and its broad manure genus are supported; manure here includes plant-derived organic fertilizer, not only animal excrement. All five contributors have ITEM decisions. GOLD Composting and Oil palm remain CLOSE with RELATED synonyms, not exact aliases. The corrected active-phase graph is supported within its stated scope. Two source taxon names and a conflicting strain-origin association need bounded provenance follow-up.

## Scope And Provenance

Entire exact HabitatRecord, all contributor provenance, direct-parent meaning and applicable biological evidence.

Selection: Next 23 alphabetically ordered engineered paths lacking a completed scientific structured review, through the full composting-variant family; separate exact-target assessments, not a sample or a category verdict. Starting current coverage232/3208.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 853fa61c16adea01016cebc064f5d12f32074712.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00002170 | data/habitats/engineered/compost.yaml | generated | compost |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | ENVO:00002170 | Exit0; actual start 2026-10-11T07:01:34.250710Z and finish 2026-10-11T07:01:36.630921Z. Full command scope is retained; deterministic validation is not scientific approval. |
| Native validate-strict | passed | True | ENVO:00002170 | Exit0; actual start 2026-10-11T07:02:29.087455Z and finish 2026-10-11T07:02:39.251682Z. Full command scope is retained; deterministic validation is not scientific approval. |
| Native verify-corpus | passed | True | ENVO:00002170 | Exit0; actual start 2026-10-11T07:02:39.253690Z and finish 2026-10-11T07:02:58.440891Z. Full command scope is retained; deterministic validation is not scientific approval. |
| Native validate-products | passed | True | ENVO:00002170 | Exit0; actual start 2026-10-11T07:02:58.442215Z and finish 2026-10-11T07:03:52.174368Z. Full command scope is retained; deterministic validation is not scientific approval. |
| Native validate-history | passed | True | ENVO:00002170 | Exit0; actual start 2026-10-11T07:03:52.176353Z and finish 2026-10-11T07:03:58.888428Z. Full command scope is retained; deterministic validation is not scientific approval. |
| Native validate-causal-all | passed | True | ENVO:00002170 | Exit0; actual start 2026-10-11T07:03:58.889136Z and finish 2026-10-11T07:04:03.188656Z. Full command scope is retained; deterministic validation is not scientific approval. |
| Native term-requests-check | passed | True | ENVO:00002170 | Exit0; actual start 2026-10-11T07:04:03.189461Z and finish 2026-10-11T07:04:20.926153Z. Full command scope is retained; deterministic validation is not scientific approval. |
| Full-field reproduction | passed | False | ENVO:00002170 | All23 exact build_document results equal current YAML, including all biology and history fields. |
| Original source assertion reconstruction | unavailable | False | ENVO:00002170 | Configured original GOLD, PREGO, Madin and environment paths returned ENOENT in ignored-inclusive searches. Frozen inventories and later exports remain distinct evidence. |
| Focused compost overlay validation | passed | True | ENVO:00002170 | Native LinkML validator exited0 with no issues. |
| Full publication QC | skipped | False | ENVO:00002170 | Not yet run at this pre-curation observation; publication validation is separate. No future result is asserted. |

## Scientific And Domain Assessments

### Ontology identity and direct genus

identity: supported. Targets: ENVO:00002170.

ENVO compost and its broad manure genus are supported; manure here includes plant-derived organic fertilizer, not only animal excrement. All five contributors have ITEM decisions. GOLD Composting and Oil palm remain CLOSE with RELATED synonyms, not exact aliases. The corrected active-phase graph is supported within its stated scope. Two source taxon names and a conflicting strain-origin association need bounded provenance follow-up.

### Reported associations, taxonomy and source caps

evidence: concern. Targets: ENVO:00002170.

All displayed pairs trace to the frozen source rows; IDs resolve. 33 displayed entries are the union of two top25 lists with17 shared IDs; source pools112 and1913 are distinct, not summed. Qualitative parameters are source bands, not measurements or universal bounds.

### Five scoped causal edges

evidence: supported. Targets: ENVO:00002170.

Corrected node types distinguish substrate habitat, temperature parameter and community succession. Direction and evidence support the five active-phase edges; the Finore edges are synthesis-level evidence and do not imply universal optimum conditions.

### Eleven qualitative source axes

scope: supported. Targets: ENVO:00002170.

Each parameter comes from the single-term compost row. The low pH band is source qualitative classification, not an invariant numeric pH; phase/feedstock variability and absent numerical thresholds limit interpretation. No multi-term component row was attached.

### Counts, predicates, source and status

provenance: supported. Targets: ENVO:00002170.

Frozen source IDs, paths, node collapse, organism counts and zero omissions match. All fields reproduce. 5/5 source concepts have ITEM decisions; this review does not promote native status. Unlike counts and later snapshots are not additive.

### Claim-proportionate fields and missing evidence

completeness: supported. Targets: ENVO:00002170.

No required field gap is established by optional absent taxa, parameters, definitions or graphs. Missing original assertion evidence is a stated limit, not permission to invent biological facts. Relevant source intent and hierarchy defects remain explicit findings.

## Findings

### F1: Two MADIN display labels are source-normalized tokens

minor / open / confirmed; issue key: envo-00002170-taxon-display-labels.

NCBITaxon1714 and36773 resolve as Cellulomonas uda and Burkholderia sp.; the record displays cellulomonas_uda and burkholderia_sp. The associations and stable IDs are not thereby invalid.

### F2: Strain-origin conflict needs assertion-level provenance

minor / open / provisional; issue key: envo-00002170-strain-origin-context.

Rhodovibrio salinarum DSM9154 (NCBITaxon1089552) is PREGO rank3 and MADIN-corroborated. DSMZ reports saltern origin, whereas later GOLD Go0014368 says compost feedstock. Repeated vocabulary agreement is not necessarily independent biological evidence. The schema only claims association, so this is a provenance question, not demonstrated false occurrence.

## Recommended Actions And Acceptance Checks

### A1

Refresh through a pinned governed taxonomy input, retaining original source labels and IDs. Do not hand-edit generated records or silently relabel unrelated taxon pools.

- Inspect exact source identity and supporting primary metadata; do not infer absence or invent a replacement class.
- Preserve mint/path, counts and units, source status and every immutable review. Append native history for authorized changes.
- Exercise an exact regression, dry seed and inspect a target canary, regenerate affected products, then run schema, strict, history, label, corpus and full QC gates.

### A2

Recover original PREGO and Madin support for the exact strain. Distinguish isolation origin from subsequent detection/enrichment; preserve conflicting metadata and change an association only with direct evidence.

- Inspect exact source identity and supporting primary metadata; do not infer absence or invent a replacement class.
- Preserve mint/path, counts and units, source status and every immutable review. Append native history for authorized changes.
- Exercise an exact regression, dry seed and inspect a target canary, regenerate affected products, then run schema, strict, history, label, corpus and full QC gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/engineered/compost.yaml; Entire generated YAML, including all history, taxa, parameters and graph fields | supports | ENVO compost and its broad manure genus are supported; manure here includes plant-derived organic fertilizer, not only animal excrement. All five contributors have ITEM decisions. GOLD Composting and Oil palm remain CLOSE with RELATED synonyms, not exact aliases. The corrected active-phase graph is supported within its stated scope. Two source taxon names and a conflicting strain-origin association need bounded provenance follow-up. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md; src/habitatmech/schema/habitatmech.yaml; Native source, identity, hierarchy, quantity, taxon, graph and status rules | supports | Strict parents require is-a; process, product, feedstock and sampled medium differ. Counts and source scores are not abundance. All contributors need ITEM decisions for REVIEWED. Optional fields may remain empty. iModulonDB is not applicable because no gene, regulator, module or strain-expression claim is made. |
| RAW | data/raw; curation/decisions.tsv; curation/gold_parent_exclusions.tsv; Exact source-mint, canonical-path or target-ID rows in maintained root TSVs | supports | {"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "GROUND", "grounding_status": "CLOSE", "identifier": "habitatmech:GOLD.4741a9f8bb", "notes": "GOLD names the composting process, ENVO the resulting material; close but not exact. Path: Engineered &gt; Solid waste &gt; Composting", "object_id": "ENVO:00002170", "object_label": "compost", "relation": "", "review_depth": "ITEM"}, "logical_row": 478}, {"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "GROUND", "grounding_status": "CLOSE", "identifier": "habitatmech:GOLD.981cf7502c", "notes": "GOLD names the composting process, ENVO the resulting material; close but not exact. Path: Engineered &gt; Solid waste &gt; Composting &gt; Oil palm", "object_id": "ENVO:00002170", "object_label": "compost", "relation": "", "review_depth": "ITEM"}, "logical_row": 886}, {"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:PREGO.e2f1a69477", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row": 1515}, {"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-15", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:ENVIRONMENTS_TABLE.392f1cbccf", "notes": "Co-attestor review (#12): 'compost' resolves to ENVO:00002170 'compost'. Correct as seeded.", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row": 1632}, {"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-15", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:MADIN.87d709b6aa", "notes": "Co-attestor review (#12): this source names the ontology CURIE itself, so its grounding is definitional rather than a lexical guess \u2014 the record IS the term the source pointed at. Recorded so the record it co-attests can reach REVIEWED, which needs every source concept decided.", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row": 1638}], "curation/gold_parent_exclusions.tsv": [{"data": {"curator": "codex-gpt-5", "date": "2026-10-07", "identifier": "habitatmech:GOLD.4741a9f8bb", "notes": "ITEM hierarchy assessment (#1664): generic ENVO:00002170 compost material is not universally discarded Solid Waste. EPA (https://www.epa.gov/sustainable-management-food/composting) distinguishes organic waste inputs from stable soil-amendment product; NLM mesh:D062611 denotes discarded materials. Suppress only this GOLD context contribution, preserving independent ENVO:03501300 manure, all source paths, heterogeneous counts and existing identity decisions. This does not settle the process/material scope of qualified GOLD Composting sources or assert a legal waste classification. Evidence: reports/yaml_record_review/20261007T222058Z-compost.md.", "parent_id": "mesh:D062611", "source_path": "Engineered &gt; Solid waste &gt; Composting"}, "logical_row": 74}], "data/raw/environment_parameters.tsv": [{"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "Gradients", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "high"}, "logical_row": 525}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "Nutrients", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "high"}, "logical_row": 526}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "Organic", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "high"}, "logical_row": 527}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "Pressure", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "low"}, "logical_row": 528}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "Salinity", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "low"}, "logical_row": 529}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "Structural", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "medium"}, "logical_row": 530}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "Water", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "medium"}, "logical_row": 531}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "pH", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "low"}, "logical_row": 532}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "salinity variability", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "small"}, "logical_row": 533}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "temp variability", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "medium"}, "logical_row": 534}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other", "parameter": "water variability", "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "occasionally dry"}, "logical_row": 535}], "data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Engineered &gt; Solid waste &gt; Composting", "depth": "3", "ecosystem": "Engineered", "ecosystem_category": "Solid waste", "ecosystem_subtype": "", "ecosystem_type": "Composting", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:3511&#124;gold.ecosystem:3842&#124;gold.ecosystem:4273", "leaf_label": "Composting", "organism_count": "270", "specific_ecosystem": "", "study_count": "0", "total_assertions": "270"}, "logical_row": 100}, {"data": {"biosample_count": "0", "canonical_path": "Engineered &gt; Solid waste &gt; Composting &gt; Oil palm", "depth": "4", "ecosystem": "Engineered", "ecosystem_category": "Solid waste", "ecosystem_subtype": "Oil palm", "ecosystem_type": "Composting", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:5755&#124;gold.ecosystem:5756", "leaf_label": "Oil palm", "organism_count": "1", "specific_ecosystem": "", "study_count": "0", "total_assertions": "1"}, "logical_row": 907}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "11", "canonical_path": "Engineered &gt; Solid waste &gt; Composting", "ecosystem_path_id": "4273"}, "logical_row": 609}], "data/raw/gold_studies.tsv": [{"data": {"path_count": "1", "paths": "Engineered &gt; Solid waste &gt; Composting", "study_gold_id": "Gs0145093"}, "logical_row": 2832}, {"data": {"path_count": "3", "paths": "Engineered &gt; Solid waste &gt; Composting&#124;Host-associated &gt; Arthropoda: Insects &gt; Whole body&#124;Host-associated &gt; Fungi &gt; Mycelium", "study_gold_id": "Gs0150459"}, "logical_row": 3276}, {"data": {"path_count": "8", "paths": "Engineered &gt; Industrial production &gt; Chemical products &gt; Lab-grade water&#124;Engineered &gt; Solid waste &gt; Composting&#124;Environmental &gt; Air &gt; Outdoor Air&#124;Environmental &gt; Aquatic &gt; Deep subsurface &gt; Groundwater &gt; Contaminated&#124;Environmental &gt; Aquatic &gt; Freshwater &gt; Creek&#124;Environmental &gt; Terrestrial &gt; Soil&#124;Host-associated &gt; Arthropoda: Chelicerates &gt; Whole body&#124;Host-associated &gt; Arthropoda: Insects &gt; Whole body", "study_gold_id": "Gs0156806"}, "logical_row": 4124}], "data/raw/madin_habitat_taxa.tsv": [{"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1089552", "taxon_label": "Rhodovibrio salinarum DSM 9154"}, "logical_row": 505}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1111737", "taxon_label": "Thermocrispum municipale DSM 44069"}, "logical_row": 506}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1111738", "taxon_label": "Thermocrispum agreste DSM 44070"}, "logical_row": 507}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121013", "taxon_label": "Arenimonas composti TR7-09, DSM 18010"}, "logical_row": 508}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121349", "taxon_label": "Comamonas composti DSM 21721"}, "logical_row": 509}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121385", "taxon_label": "Demetria terragena DSM 11295"}, "logical_row": 510}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121395", "taxon_label": "Desulfitobacterium chlororespirans DSM 11544"}, "logical_row": 511}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121927", "taxon_label": "Gordonia hirsuta K718a, DSM 44140"}, "logical_row": 512}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121952", "taxon_label": "Humibacter albus DSM 18994"}, "logical_row": 513}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1122239", "taxon_label": "Microbacterium luticocti DSM 19459"}, "logical_row": 514}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1122958", "taxon_label": "Phenylobacterium composti DSM 19425"}, "logical_row": 515}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1123405", "taxon_label": "Tuberibacillus calidus DSM 17572"}, "logical_row": 516}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1292027", "taxon_label": "Pseudomonas azotifigens DSM 17556"}, "logical_row": 517}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1408", "taxon_label": "Bacillus pumilus"}, "logical_row": 518}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1714", "taxon_label": "cellulomonas_uda"}, "logical_row": 519}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:269800", "taxon_label": "Thermobifida fusca YX"}, "logical_row": 520}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:287", "taxon_label": "Pseudomonas aeruginosa"}, "logical_row": 521}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:292459", "taxon_label": "Symbiobacterium thermophilum IAM 14863"}, "logical_row": 522}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:36773", "taxon_label": "burkholderia_sp"}, "logical_row": 523}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:394503", "taxon_label": "Ruminiclostridium cellulolyticum H10"}, "logical_row": 524}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:407022", "taxon_label": "pseudosphingobacterium_domesticum"}, "logical_row": 525}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:471852", "taxon_label": "Thermomonospora curvata DSM 43183"}, "logical_row": 526}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:644383", "taxon_label": "thermosporothrix_hazakensis"}, "logical_row": 527}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:649349", "taxon_label": "Leadbetterella byssophila DSM 17132"}, "logical_row": 528}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:743721", "taxon_label": "Pseudoxanthomonas suwonensis 11-1"}, "logical_row": 529}], "data/raw/madin_habitats.tsv": [{"data": {"label": "compost", "madin_id": "ENVO:00002170", "taxon_count": "112", "vocabulary": "ENVO"}, "logical_row": 36}], "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "1", "taxon_id": "NCBITaxon:1045004", "taxon_label": "Oenococcus kitaharae DSM 17330"}, "logical_row": 6183}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "2", "taxon_id": "NCBITaxon:1045012", "taxon_label": "Acetivibrio clariflavus 4-2a"}, "logical_row": 6184}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "3", "taxon_id": "NCBITaxon:1089552", "taxon_label": "Rhodovibrio salinarum DSM 9154"}, "logical_row": 6185}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "4", "taxon_id": "NCBITaxon:1111737", "taxon_label": "Thermocrispum municipale DSM 44069"}, "logical_row": 6186}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "5", "taxon_id": "NCBITaxon:1111738", "taxon_label": "Thermocrispum agreste DSM 44070"}, "logical_row": 6187}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "6", "taxon_id": "NCBITaxon:1121013", "taxon_label": "Arenimonas composti TR7-09 = DSM 18010"}, "logical_row": 6188}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "7", "taxon_id": "NCBITaxon:1121349", "taxon_label": "Comamonas composti DSM 21721"}, "logical_row": 6189}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "8", "taxon_id": "NCBITaxon:1121385", "taxon_label": "Demetria terragena DSM 11295"}, "logical_row": 6190}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "9", "taxon_id": "NCBITaxon:1121395", "taxon_label": "Desulfitobacterium chlororespirans DSM 11544"}, "logical_row": 6191}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "10", "taxon_id": "NCBITaxon:1121431", "taxon_label": "Desulfallas thermosapovorans DSM 6562"}, "logical_row": 6192}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "11", "taxon_id": "NCBITaxon:1121927", "taxon_label": "Gordonia hirsuta DSM 44140 = NBRC 16056"}, "logical_row": 6193}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "12", "taxon_id": "NCBITaxon:1121952", "taxon_label": "Humibacter albus DSM 18994"}, "logical_row": 6194}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "13", "taxon_id": "NCBITaxon:1122239", "taxon_label": "Microbacterium luticocti DSM 19459"}, "logical_row": 6195}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "14", "taxon_id": "NCBITaxon:1122958", "taxon_label": "Phenylobacterium composti DSM 19425"}, "logical_row": 6196}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "15", "taxon_id": "NCBITaxon:1123024", "taxon_label": "Pseudonocardia asaccharolytica DSM 44247 = NBRC 16224"}, "logical_row": 6197}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "16", "taxon_id": "NCBITaxon:1123405", "taxon_label": "Tuberibacillus calidus DSM 17572"}, "logical_row": 6198}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "17", "taxon_id": "NCBITaxon:1292027", "taxon_label": "Stutzerimonas azotifigens DSM 17556"}, "logical_row": 6199}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "18", "taxon_id": "NCBITaxon:1868734", "taxon_label": "Aeribacillus composti"}, "logical_row": 6200}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "19", "taxon_id": "NCBITaxon:1970199", "taxon_label": "Sorangiineae bacterium NIC37A_2"}, "logical_row": 6201}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "20", "taxon_id": "NCBITaxon:407022", "taxon_label": "Olivibacter domesticus"}, "logical_row": 6202}, {"data": {"channels": "annotated_genomes_isolates&#124;environmental_samples", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "21", "taxon_id": "NCBITaxon:471852", "taxon_label": "Thermomonospora curvata DSM 43183"}, "logical_row": 6203}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "22", "taxon_id": "NCBITaxon:644383", "taxon_label": "Thermosporothrix hazakensis"}, "logical_row": 6204}, {"data": {"channels": "annotated_genomes_isolates&#124;environmental_samples", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "23", "taxon_id": "NCBITaxon:649349", "taxon_label": "Leadbetterella byssophila DSM 17132"}, "logical_row": 6205}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "2.82248", "rank": "24", "taxon_id": "NCBITaxon:39650", "taxon_label": "Cellvibrio mixtus"}, "logical_row": 6206}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "2.77144", "rank": "25", "taxon_id": "NCBITaxon:155077", "taxon_label": "Cellvibrio japonicus"}, "logical_row": 6207}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category": "biolink:OntologyClass", "channels": "annotated_genomes_isolates&#124;environmental_samples", "direct_assertion_count": "1915", "max_prego_score": "3", "ontology": "ENVO", "prego_id": "ENVO:00002170", "prego_synonyms": "compost&#124;composts", "taxon_count": "1913"}, "logical_row": 40}]}. Logical TSV row ordinals include the header; not physical lines when cells contain newlines. Parent-owned rows are excluded from this target attestation audit. |
| CODE | src/habitatmech/seed.py; resolve_gold mapping route, ingest_gold hierarchy, complete read-only reproduction | supports | {"reviewed_sources": 5, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "GROUND", "grounding_status": "CLOSE", "identifier": "habitatmech:GOLD.4741a9f8bb", "notes": "GOLD names the composting process, ENVO the resulting material; close but not exact. Path: Engineered &gt; Solid waste &gt; Composting", "object_id": "ENVO:00002170", "object_label": "compost", "relation": "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status": "CLOSE", "identifier": "ENVO:00002170", "mapping_predicate": "skos:closeMatch", "reviewed": true, "route": "curated_ground_from_gold_mapping_table"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002170", "mapping_predicate": "skos:exactMatch", "reviewed": false, "route": "gold_mapping_table"}, "path": "Engineered &gt; Solid waste &gt; Composting"}, {"actual": {"category": null, "contributes_grounding": true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "GROUND", "grounding_status": "CLOSE", "identifier": "habitatmech:GOLD.981cf7502c", "notes": "GOLD names the composting process, ENVO the resulting material; close but not exact. Path: Engineered &gt; Solid waste &gt; Composting &gt; Oil palm", "object_id": "ENVO:00002170", "object_label": "compost", "relation": "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status": "CLOSE", "identifier": "ENVO:00002170", "mapping_predicate": "skos:closeMatch", "reviewed": true, "route": "curated_ground_from_gold_unmatched"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "UNGROUNDED", "identifier": "habitatmech:GOLD.981cf7502c", "mapping_predicate": null, "reviewed": false, "route": "gold_unmatched"}, "path": "Engineered &gt; Solid waste &gt; Composting &gt; Oil palm"}], "source_concepts": 5}. Complete build_document equality was checked. The ambiguous GOLD mapping route emits a mint with NARROW and an extra ontology parent; immediate source-path parents are contributed independently. Native status follows source decisions, not this review. |
| ONT | https://www.ebi.ac.uk/ols4/api/ontologies; https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.obo; Exact target and direct ontology parent JSON labels, definitions and active state | supports | [{"definition": ["Manure which has been derived from the aerobically decomposed remnants of organic materials."], "id": "ENVO:00002170", "label": "compost", "obsolete": false}, {"definition": ["Most manure consists of animal feces; other sources include compost and green manure.", "An environmental material consisting of organic matter from plants and/or animals that is used in agriculture as fertilizer."], "id": "ENVO:03501300", "label": "manure", "obsolete": false}]. Ontology meaning verifies a term, not every GOLD source crosswalk. |
| PARENT | data/habitats; data/raw/ontology_subclass_edges.tsv; Captured direct-parent identity and provenance fields | supports | {"ENVO:03501300": {"definition": "An environmental material consisting of organic matter from plants and/or animals that is used in agriculture as fertilizer.", "identifier": "ENVO:03501300", "label": "manure", "parent_habitats": ["ENVO:00010483", "habitatmech:GOLD.18ee4196a9"], "source_attestations": [{"mapping_predicate": "skos:closeMatch", "source": "GOLD", "source_id": "gold.ecosystem:8076", "source_label": "Liquid manure", "source_path": "Engineered &gt; Solid waste &gt; Animal waste &gt; Manure slurry &gt; Liquid manure"}]}}. Direct-parent context only, not scientific review of their biological claims. Coal has no generated sedimentary-rock record in this capture; its ontology genus is checked directly. |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; Exact five-position tuples; first-three member descriptions except all16 latrine BioSamples and all8 vegetable organisms | supports | Retained later export, not a fresh download or original frozen-member reconstruction. Complete streamed census counts including headers={"Biosample": 244951, "Organism": 532019, "SequencingProject": 636914, "Study": 63806}; exact target matches={"Biosample": 12, "Organism": 259, "SequencingProject": 81}; inspected bounded source descriptions={"Biosample": [{"data": {"BIOSAMPLE GOLD ID": "Gb0247172", "BIOSAMPLE NAME": "Wheat straw compost microbial community from United Kingdom - WSC_Wk1_1", "BIOSAMPLE NCBI TAX NAME": "", "BIOSAMPLE SAMPLE COLLECTION SITE": "Wheat straw compost"}, "paths": ["Engineered &gt; Solid waste &gt; Composting"], "row": 93613}, {"data": {"BIOSAMPLE GOLD ID": "Gb0247173", "BIOSAMPLE NAME": "Wheat straw compost microbial community from United Kingdom - WSC_Wk1_2", "BIOSAMPLE NCBI TAX NAME": "", "BIOSAMPLE SAMPLE COLLECTION SITE": "Wheat straw compost"}, "paths": ["Engineered &gt; Solid waste &gt; Composting"], "row": 93614}, {"data": {"BIOSAMPLE GOLD ID": "Gb0247174", "BIOSAMPLE NAME": "Wheat straw compost microbial community from United Kingdom - WSC_Wk1_3", "BIOSAMPLE NCBI TAX NAME": "", "BIOSAMPLE SAMPLE COLLECTION SITE": "Wheat straw compost"}, "paths": ["Engineered &gt; Solid waste &gt; Composting"], "row": 93615}], "Organism": [{"data": {"ORGANISM GOLD ID": "Go0075327", "ORGANISM HABITAT": "", "ORGANISM ISOLATION HOST NAME": "", "ORGANISM NAME": "Streptomyces exfoliatus DSM 41693", "ORGANISM SAMPLE COLLECTION SITE": "Compost"}, "paths": ["Engineered &gt; Solid waste &gt; Composting"], "row": 46758}, {"data": {"ORGANISM GOLD ID": "Go0086731", "ORGANISM HABITAT": "", "ORGANISM ISOLATION HOST NAME": "", "ORGANISM NAME": "Acetivibrio straminisolvens JCM 21531", "ORGANISM SAMPLE COLLECTION SITE": "a bacterial community constructed from composting processes"}, "paths": ["Engineered &gt; Solid waste &gt; Composting"], "row": 51944}, {"data": {"ORGANISM GOLD ID": "Go0089984", "ORGANISM HABITAT": "Compost", "ORGANISM ISOLATION HOST NAME": "", "ORGANISM NAME": "Agrilactobacillus composti JCM 14202", "ORGANISM SAMPLE COLLECTION SITE": "composting material of distilled shochu residue"}, "paths": ["Engineered &gt; Solid waste &gt; Composting"], "row": 53386}]}. Other matched descriptions and joined studies are inventoried, not all independently reviewed. Empty and Unclassified normalize to empty without dropping tuple positions. Projects retain both matched source paths; study counts are not habitat assertion counts. |
| CLASS | https://gold.jgi.doe.gov/; Classification site-data sheet exact five-position tuple | supports | Later retained classification snapshot SHA256 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396; exact rows=[{"row": 387, "slug": "compost", "path": "Engineered &gt; Solid waste &gt; Composting &gt; Oil palm", "values": ["5756", "Engineered", "Solid waste", "Composting", "Oil palm", "Unclassified"]}, {"row": 388, "slug": "compost", "path": "Engineered &gt; Solid waste &gt; Composting", "values": ["4273", "Engineered", "Solid waste", "Composting", "Unclassified", "Unclassified"]}]. Original endpoint was not retained. A miss is bounded to this snapshot. |
| PROCESS | https://www.epa.gov/sustainable-management-food/composting; Definitions and Composting Basics and Approaches | supports | Composting is an aerobic decomposition process; compost is its stabilized product. Feedstock, active material and facility are distinct. This terminology does not define a GOLD source category. |
| SEARCH | curation; data/raw; history; research; reports; reviews; conf; Saved support-search and exact-row audits | supports | Ignored/hidden-inclusive rg and Path.rglob searches covered identifiers, paths, labels and slugs, all root raw/curation TSVs and all32 overlay identifiers. No previous completed scientific structured review targeted this exact ID at capture. Only compost has a target overlay in this selection. Configured original-source paths were checked including ignored files: [{"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold"], "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold: IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold: No such file or directory (os error 2)\n"}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego"], "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego: IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego: No such file or directory (os error 2)\n"}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal"], "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal: IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal: No such file or directory (os error 2)\n"}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv"], "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv: IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv: No such file or directory (os error 2)\n"}]. These are bounded path failures, not global source absence. |
| SOURCE-CONTEXT | data/habitats/engineered/compost.yaml; Field-by-field interpretation of the exact record against inspected evidence | supports | ENVO compost and its broad manure genus are supported; manure here includes plant-derived organic fertilizer, not only animal excrement. All five contributors have ITEM decisions. GOLD Composting and Oil palm remain CLOSE with RELATED synonyms, not exact aliases. The corrected active-phase graph is supported within its stated scope. Two source taxon names and a conflicting strain-origin association need bounded provenance follow-up. |
| TAXA | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1045004%2C1045012%2C1089552%2C1111737%2C1111738%2C1121013%2C1121349%2C1121385%2C1121395%2C1121431%2C1121927%2C1121952%2C1122239%2C1122958%2C1123024%2C1123405%2C1292027%2C1408%2C155077%2C1714%2C1868734%2C1970199%2C269800%2C287%2C292459%2C36773%2C394503%2C39650%2C407022%2C420662%2C471852%2C644383%2C649349%2C743721&amp;retmode=xml; NCBI efetch Taxon ID, ScientificName, Rank and AkaTaxIds for all displayed associations | supports | [{"canonical_name": "Rhodovibrio salinarum DSM 9154", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 3, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1089552", "taxon_label": "Rhodovibrio salinarum DSM 9154"}}, {"canonical_name": "Thermocrispum municipale DSM 44069", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 4, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1111737", "taxon_label": "Thermocrispum municipale DSM 44069"}}, {"canonical_name": "Thermocrispum agreste DSM 44070", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 5, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1111738", "taxon_label": "Thermocrispum agreste DSM 44070"}}, {"canonical_name": "Arenimonas composti TR7-09 = DSM 18010", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 6, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1121013", "taxon_label": "Arenimonas composti TR7-09 = DSM 18010"}}, {"canonical_name": "Comamonas composti DSM 21721", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 7, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1121349", "taxon_label": "Comamonas composti DSM 21721"}}, {"canonical_name": "Demetria terragena DSM 11295", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 8, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1121385", "taxon_label": "Demetria terragena DSM 11295"}}, {"canonical_name": "Desulfitobacterium chlororespirans DSM 11544", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 9, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1121395", "taxon_label": "Desulfitobacterium chlororespirans DSM 11544"}}, {"canonical_name": "Gordonia hirsuta DSM 44140 = NBRC 16056", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 11, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1121927", "taxon_label": "Gordonia hirsuta DSM 44140 = NBRC 16056"}}, {"canonical_name": "Humibacter albus DSM 18994", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 12, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1121952", "taxon_label": "Humibacter albus DSM 18994"}}, {"canonical_name": "Microbacterium luticocti DSM 19459", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 13, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1122239", "taxon_label": "Microbacterium luticocti DSM 19459"}}, {"canonical_name": "Phenylobacterium composti DSM 19425", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 14, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1122958", "taxon_label": "Phenylobacterium composti DSM 19425"}}, {"canonical_name": "Tuberibacillus calidus DSM 17572", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 16, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1123405", "taxon_label": "Tuberibacillus calidus DSM 17572"}}, {"canonical_name": "Stutzerimonas azotifigens DSM 17556", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 17, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1292027", "taxon_label": "Stutzerimonas azotifigens DSM 17556"}}, {"canonical_name": "Olivibacter domesticus", "rank": "species", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 20, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:407022", "taxon_label": "Olivibacter domesticus"}}, {"canonical_name": "Thermomonospora curvata DSM 43183", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 21, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:471852", "taxon_label": "Thermomonospora curvata DSM 43183"}}, {"canonical_name": "Thermosporothrix hazakensis", "rank": "species", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 22, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:644383", "taxon_label": "Thermosporothrix hazakensis"}}, {"canonical_name": "Leadbetterella byssophila DSM 17132", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 23, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:649349", "taxon_label": "Leadbetterella byssophila DSM 17132"}}, {"canonical_name": "Bacillus pumilus", "rank": "species", "source": {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:1408", "taxon_label": "Bacillus pumilus"}}, {"canonical_name": "Cellulomonas uda", "rank": "species", "source": {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:1714", "taxon_label": "cellulomonas_uda"}}, {"canonical_name": "Thermobifida fusca YX", "rank": "strain", "source": {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:269800", "taxon_label": "Thermobifida fusca YX"}}, {"canonical_name": "Pseudomonas aeruginosa", "rank": "species", "source": {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:287", "taxon_label": "Pseudomonas aeruginosa"}}, {"canonical_name": "Symbiobacterium thermophilum IAM 14863", "rank": "strain", "source": {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:292459", "taxon_label": "Symbiobacterium thermophilum IAM 14863"}}, {"canonical_name": "Burkholderia sp.", "rank": "species", "source": {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:36773", "taxon_label": "burkholderia_sp"}}, {"canonical_name": "Ruminiclostridium cellulolyticum H10", "rank": "strain", "source": {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:394503", "taxon_label": "Ruminiclostridium cellulolyticum H10"}}, {"canonical_name": "Pseudoxanthomonas suwonensis 11-1", "rank": "strain", "source": {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:743721", "taxon_label": "Pseudoxanthomonas suwonensis 11-1"}}, {"canonical_name": "Oenococcus kitaharae DSM 17330", "rank": "strain", "source": {"candidate_pool": 1913, "rank": 1, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1045004", "taxon_label": "Oenococcus kitaharae DSM 17330"}}, {"canonical_name": "Acetivibrio clariflavus 4-2a", "rank": "strain", "source": {"candidate_pool": 1913, "rank": 2, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1045012", "taxon_label": "Acetivibrio clariflavus 4-2a"}}, {"canonical_name": "Desulfallas thermosapovorans DSM 6562", "rank": "strain", "source": {"candidate_pool": 1913, "rank": 10, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1121431", "taxon_label": "Desulfallas thermosapovorans DSM 6562"}}, {"canonical_name": "Pseudonocardia asaccharolytica DSM 44247 = NBRC 16224", "rank": "strain", "source": {"candidate_pool": 1913, "rank": 15, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1123024", "taxon_label": "Pseudonocardia asaccharolytica DSM 44247 = NBRC 16224"}}, {"canonical_name": "Aeribacillus composti", "rank": "species", "source": {"candidate_pool": 1913, "rank": 18, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1868734", "taxon_label": "Aeribacillus composti"}}, {"canonical_name": "Sorangiineae bacterium NIC37A_2", "rank": "species", "source": {"candidate_pool": 1913, "rank": 19, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1970199", "taxon_label": "Sorangiineae bacterium NIC37A_2"}}, {"canonical_name": "Cellvibrio mixtus", "rank": "species", "source": {"candidate_pool": 1913, "rank": 24, "score": 2.82248, "source": "PREGO", "taxon_id": "NCBITaxon:39650", "taxon_label": "Cellvibrio mixtus"}}, {"canonical_name": "Cellvibrio japonicus", "rank": "species", "source": {"candidate_pool": 1913, "rank": 25, "score": 2.77144, "source": "PREGO", "taxon_id": "NCBITaxon:155077", "taxon_label": "Cellvibrio japonicus"}}]. Every displayed ID resolves directly without a merged alias. Ranks are mixed species/strain and source ranking is not abundance. No is_characteristic flag is asserted. Source agreement is not proof of independent experiments. |
| GRAPH | PMID:16454493; DOI:10.1021/bp050171d; DOI:10.1186/s40538-023-00381-z; Richard PubMed XML title/authors/DOI/abstract; Finore publisher named sections and five edge snippets | supports | Richard2006 abstract verifies oxygen-dependent biodegradation across tested substrate, temperature and moisture conditions, including a reversal at65C; not universal monotonic stimulation. Finore2023 is explicitly a review. Inspected introduction, thermodynamics, thermophilic succession and enzyme passages support substrate use, heat generation with heat loss, temperature-dependent succession and enzyme activities in active plant-rich composting. All five short snippets match normalized source text. The graph history explicitly limits active thermophilic scope; it does not describe every mature compost or a single experiment. |
| STRAIN-ORIGIN | https://www.dsmz.de/collection/catalogue/details/culture/DSM-9154; DSMZ name, collection-number and origin fields; exact later GOLD row Go0014368 | context_only | DSM9154 is the Rhodovibrio salinarum type strain, also ATCC35394, with Portugal saltern collection provenance. Later GOLD Go0014368 instead labels its collection site compost feedstock. This conflict requires original assertion tracing; it is not proof the organism cannot occur in compost. |

## Limits And Additional Notes

- One exact record is assessed; parent context and later member inventories do not add reviewed records.
- Original frozen assertion-level support is not reconstructed; later GOLD exports are contextual and do not replace original counts.
- Only explicitly described member fields and paper passages were inspected, not every study or full paper, and no figure-dependent inference is made.
- Current NLM JSON requests for Solid Waste reset; no target depends on adopting a new MeSH identity. Stable direct target/ontology parent IDs were separately checked.
- iModulonDB is not applicable to the claims in these records; no expression-module inference is made.
- This pre-curation observation does not certify SSSOM/KGX readiness, authorize native status promotion, or close prior issues. Original bundles remain immutable.
- The all-record review goal remains active.
- Legacy reviews are leads, not copied verdicts or normalized predecessor observations. Existing open issues are not silently closed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T071204Z-compost
kind: record
repository: culturebotai/HabitatMech
title: 'Scientific record review: compost'
started_at: '2026-10-11T07:00:29.668504Z'
finished_at: '2026-10-11T07:12:04.137068Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Continuing agent participated in earlier curation/review; this
    is adversarial self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: ENVO compost and its broad manure genus are supported; manure here includes
  plant-derived organic fertilizer, not only animal excrement. All five contributors
  have ITEM decisions. GOLD Composting and Oil palm remain CLOSE with RELATED synonyms,
  not exact aliases. The corrected active-phase graph is supported within its stated
  scope. Two source taxon names and a conflicting strain-origin association need bounded
  provenance follow-up.
source:
  git_revision: 853fa61c16adea01016cebc064f5d12f32074712
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
    sha256: 4a8150d842452267f80310ea3974346c0a01a9c432273d409cc68499a51b30e8
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
  - path: data/habitats/engineered/compost.yaml
    sha256: ac7f1e3a3e8ca2e751b14d0cabcbefa461bf4ff72183e74650dacc79c62531b9
    role: target
  - path: data/habitats/engineered/manure.yaml
    sha256: 5abbcdffe09572cb4ef5ecfc784c2fc173c8b631525c881dad66dccd80f925a1
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
  - path: reports/pr_review/20261007T224637Z-compost-publication.md
    sha256: 90f25b097f5caafcbfe82013cc03e98904af3b991c65f5d11e0e9000e42a75e0
    role: context
  - path: reports/pr_review/20261008T002302Z-composting-variants-publication.md
    sha256: b112dbcfcac33e5950882db1daeff98b82a432dc1a6a064f640509160f538c21
    role: context
  - path: reports/yaml_record_review/20260921T052348Z-composting_facility.md
    sha256: 0328b2efe3618e91b5a3c9fb3cf7120e662dc06b4b45306a4525846562fb4290
    role: context
  - path: reports/yaml_record_review/20260928T103041Z-composting__ccb9142d.md
    sha256: 1ede66f6c5f424ab29df814af375e95abcc00f5392391525cf51dae2cfde42ef
    role: context
  - path: reports/yaml_record_review/20261007T214652Z-commercial_compost.md
    sha256: 88029b8570ac8a93e335714c44056d9de1a2c7b14a9ce3d51cbbae4f5f2b0634
    role: context
  - path: reports/yaml_record_review/20261007T222058Z-compost.md
    sha256: 07aa1a5e3fe12e8ee833a4356cfa45c34ea059b62c4f986d8bb1542b79257043
    role: context
  - path: reports/yaml_record_review/20261007T222445Z-compost_biofilter.md
    sha256: c5b0fde60b736a6e8500827ebc9360e16a245ada5616d03cee6b95ce0c5f325b
    role: context
  - path: reports/yaml_record_review/20261007T225643Z-composting.md
    sha256: 0cb4529d723a44711903b3cc60357d8737a58f56b744158ec88559a87b72d9a5
    role: context
  - path: reports/yaml_record_review/20261007T230734Z-composting.md
    sha256: 293928405214f16d158b7c348f96d22c2eb235f807fdc82e37a22519eec051b8
    role: context
  - path: reports/yaml_record_review/20261008T000835Z-composting__0995fad8.md
    sha256: be3b8ce600e37561fa8246180189c6e2e95be7b5ec0c966addcb3dbd5e26129a
    role: context
  - path: reports/yaml_record_review/20261008T001124Z-composting__17c06daf.md
    sha256: 4db905438125fa330ddc645035f9a3006b69aea55828797775c2043c70f20c77
    role: context
  - path: reports/yaml_record_review/20261008T010150Z-composting__17c89528.md
    sha256: c8a60de11cd63150a05889ae45b037e09a37749395ad343a0baf7f6943321ac9
    role: context
  - path: reports/yaml_record_review/20261008T010437Z-composting__1f48c1e1.md
    sha256: 2ce3bd174df67835868477dab8458ab1af0fa36a47a85fa55ac2a4fb5dde9f73
    role: context
  - path: reports/yaml_record_review/20261008T010755Z-composting__3d1c60e3.md
    sha256: 669569629a4559f4956ee0abf5e5a276d16f2289d180bd3bfe4b5afb584575eb
    role: context
  - path: reports/yaml_record_review/20261008T011217Z-composting__59a6ebe1.md
    sha256: a6ceaa973e265a4a43fbfd10789998fcbe47f400e74c750cb5bd68d10f76811d
    role: context
  - path: reports/yaml_record_review/20261008T014409Z-composting__614642ae.md
    sha256: 579e27703b15d6e28c7b371c217e6389b484a426791d964cab5b03722008706a
    role: context
  - path: reports/yaml_record_review/20261008T014734Z-composting__64a719cb.md
    sha256: ee253a49a6339f5c04d6a3c02ee692d949d9a2304b7e85c83ab3e2ada3317aa5
    role: context
  - path: reports/yaml_record_review/20261008T014913Z-composting__66a8d404.md
    sha256: f2344764018e2fab61781f8bd122b04795ab0dd27315e698eefdb2f31ddd63dd
    role: context
  - path: reports/yaml_record_review/20261008T023744Z-composting__7007242d.md
    sha256: f1dec5d4931cc1175dc6b9343796959cdba12f680eb367a9a430db448ca5d0b8
    role: context
  - path: reports/yaml_record_review/20261008T024112Z-composting__73149eb7.md
    sha256: bf5d554a09087a009b7718da7a35c748d72f8691cd98f7219fc1cbb4ea982a07
    role: context
  - path: reports/yaml_record_review/20261008T024322Z-composting__884e79de.md
    sha256: 27ff85e386b6933e179d1d049bc2eb8db07c9fd45b5f6acd1c5bf60597d5c2a8
    role: context
  - path: reports/yaml_record_review/20261008T024539Z-composting__97f67f01.md
    sha256: f373dcd4edb2d9d024f466f7c5349ab151e8c836d881b5edec5e959561fb30ea
    role: context
  - path: reports/yaml_record_review/20261008T024819Z-composting__a2009224.md
    sha256: 7000e9aee93d34f8c3ce4e9472ac2dd39e0bc1dab6f94fe2689f3bd982bfc37a
    role: context
  - path: reports/yaml_record_review/20261008T025128Z-composting__b5981ec2.md
    sha256: fb630b7bee0627b203102c7e9d8c184fb8e9e8ae97e453166243ec15b79c466c
    role: context
  - path: reports/yaml_record_review/20261008T031215Z-composting__f25ec0d0.md
    sha256: e5b3b9217fa63abecfbe2bc710fcfc2fe02f8cdc291ec8a65c3a8619c345aa5f
    role: context
  - path: reports/yaml_record_review/20261008T031459Z-composting__fe5ff5cf.md
    sha256: 696fc5882760d97a11879db7842ed0d108659e60f42afa634652da07f2872773
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
  description: Entire exact HabitatRecord, all contributor provenance, direct-parent
    meaning and applicable biological evidence.
  selection: Next 23 alphabetically ordered engineered paths lacking a completed scientific
    structured review, through the full composting-variant family; separate exact-target
    assessments, not a sample or a category verdict. Starting current coverage232/3208.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00002170
  exclusions:
  - target: Other3207 current HabitatRecords
    reason: Context does not constitute additional scientific verdicts.
targets:
- target_id: ENVO:00002170
  path: data/habitats/engineered/compost.yaml
  label: compost
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Exact source-concept identity and grounding decisions
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded immediate GOLD context-parent exclusions
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: Authored habitat definitions and genus
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained harmonization and generation
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD concepts and ORGANISM counts
  - repository: culturebotai/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: PREGO vocabulary and association pool
  - repository: culturebotai/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: PREGO ranked source associations
  - repository: culturebotai/HabitatMech
    path: data/raw/madin_habitats.tsv
    role: Madin habitat vocabulary and source counts
  - repository: culturebotai/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Madin taxon observations
  - repository: culturebotai/HabitatMech
    path: data/raw/environment_parameters.tsv
    role: Attributed qualitative parameter bands
  - repository: culturebotai/HabitatMech
    path: curation/causal_graphs/compost.yaml
    role: Maintained causal graph and edge evidence
checks:
- check_id: C2
  name: Native validate
  status: passed
  required: true
  summary: Exit0; actual start 2026-10-11T07:01:34.250710Z and finish 2026-10-11T07:01:36.630921Z.
    Full command scope is retained; deterministic validation is not scientific approval.
  target_ids:
  - ENVO:00002170
  command: just validate data/habitats/engineered/compost.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C23
  name: Native validate-strict
  status: passed
  required: true
  summary: Exit0; actual start 2026-10-11T07:02:29.087455Z and finish 2026-10-11T07:02:39.251682Z.
    Full command scope is retained; deterministic validation is not scientific approval.
  target_ids:
  - ENVO:00002170
  command: just validate-strict data/habitats/engineered/coal.yaml data/habitats/engineered/commercial_compost.yaml
    data/habitats/engineered/compost.yaml data/habitats/engineered/compost_biofilter.yaml
    data/habitats/engineered/composting.yaml data/habitats/engineered/composting__0995fad8.yaml
    data/habitats/engineered/composting__17c06daf.yaml data/habitats/engineered/composting__17c89528.yaml
    data/habitats/engineered/composting__1f48c1e1.yaml data/habitats/engineered/composting__3d1c60e3.yaml
    data/habitats/engineered/composting__59a6ebe1.yaml data/habitats/engineered/composting__614642ae.yaml
    data/habitats/engineered/composting__64a719cb.yaml data/habitats/engineered/composting__66a8d404.yaml
    data/habitats/engineered/composting__7007242d.yaml data/habitats/engineered/composting__73149eb7.yaml
    data/habitats/engineered/composting__884e79de.yaml data/habitats/engineered/composting__97f67f01.yaml
    data/habitats/engineered/composting__a2009224.yaml data/habitats/engineered/composting__b5981ec2.yaml
    data/habitats/engineered/composting__ccb9142d.yaml data/habitats/engineered/composting__f25ec0d0.yaml
    data/habitats/engineered/composting__fe5ff5cf.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C24
  name: Native verify-corpus
  status: passed
  required: true
  summary: Exit0; actual start 2026-10-11T07:02:39.253690Z and finish 2026-10-11T07:02:58.440891Z.
    Full command scope is retained; deterministic validation is not scientific approval.
  target_ids:
  - ENVO:00002170
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C25
  name: Native validate-products
  status: passed
  required: true
  summary: Exit0; actual start 2026-10-11T07:02:58.442215Z and finish 2026-10-11T07:03:52.174368Z.
    Full command scope is retained; deterministic validation is not scientific approval.
  target_ids:
  - ENVO:00002170
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C26
  name: Native validate-history
  status: passed
  required: true
  summary: Exit0; actual start 2026-10-11T07:03:52.176353Z and finish 2026-10-11T07:03:58.888428Z.
    Full command scope is retained; deterministic validation is not scientific approval.
  target_ids:
  - ENVO:00002170
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C27
  name: Native validate-causal-all
  status: passed
  required: true
  summary: Exit0; actual start 2026-10-11T07:03:58.889136Z and finish 2026-10-11T07:04:03.188656Z.
    Full command scope is retained; deterministic validation is not scientific approval.
  target_ids:
  - ENVO:00002170
  command: just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C28
  name: Native term-requests-check
  status: passed
  required: true
  summary: Exit0; actual start 2026-10-11T07:04:03.189461Z and finish 2026-10-11T07:04:20.926153Z.
    Full command scope is retained; deterministic validation is not scientific approval.
  target_ids:
  - ENVO:00002170
  command: just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: REPRO
  name: Full-field reproduction
  status: passed
  required: false
  summary: All23 exact build_document results equal current YAML, including all biology
    and history fields.
  target_ids:
  - ENVO:00002170
  command: .venv/bin/python /private/tmp/habitatmech-review-am-reproduce.py
  exit_code: 0
  evidence_ids:
  - CODE
- check_id: ORIGINAL
  name: Original source assertion reconstruction
  status: unavailable
  required: false
  summary: Configured original GOLD, PREGO, Madin and environment paths returned ENOENT
    in ignored-inclusive searches. Frozen inventories and later exports remain distinct
    evidence.
  target_ids:
  - ENVO:00002170
  evidence_ids:
  - SEARCH
- check_id: FOCUSED-GRAPH
  name: Focused compost overlay validation
  status: passed
  required: true
  summary: Native LinkML validator exited0 with no issues.
  target_ids:
  - ENVO:00002170
  command: just validate-causal curation/causal_graphs/compost.yaml
  exit_code: 0
  evidence_ids:
  - GRAPH
- check_id: PUBLICATION
  name: Full publication QC
  status: skipped
  required: false
  summary: Not yet run at this pre-curation observation; publication validation is
    separate. No future result is asserted.
  target_ids:
  - ENVO:00002170
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/engineered/compost.yaml
  summary: ENVO compost and its broad manure genus are supported; manure here includes
    plant-derived organic fertilizer, not only animal excrement. All five contributors
    have ITEM decisions. GOLD Composting and Oil palm remain CLOSE with RELATED synonyms,
    not exact aliases. The corrected active-phase graph is supported within its stated
    scope. Two source taxon names and a conflicting strain-origin association need
    bounded provenance follow-up.
  locator: Entire generated YAML, including all history, taxa, parameters and graph
    fields
  accessed_at: '2026-10-11T07:12:04.137068Z'
  support: supports
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md;
    src/habitatmech/schema/habitatmech.yaml
  summary: Strict parents require is-a; process, product, feedstock and sampled medium
    differ. Counts and source scores are not abundance. All contributors need ITEM
    decisions for REVIEWED. Optional fields may remain empty. iModulonDB is not applicable
    because no gene, regulator, module or strain-expression claim is made.
  locator: Native source, identity, hierarchy, quantity, taxon, graph and status rules
  accessed_at: '2026-10-11T07:12:04.137068Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5",
    "date": "2026-08-13", "decision": "GROUND", "grounding_status": "CLOSE", "identifier":
    "habitatmech:GOLD.4741a9f8bb", "notes": "GOLD names the composting process, ENVO
    the resulting material; close but not exact. Path: Engineered > Solid waste >
    Composting", "object_id": "ENVO:00002170", "object_label": "compost", "relation":
    "", "review_depth": "ITEM"}, "logical_row": 478}, {"data": {"category": "", "curator":
    "claude-opus-5", "date": "2026-08-13", "decision": "GROUND", "grounding_status":
    "CLOSE", "identifier": "habitatmech:GOLD.981cf7502c", "notes": "GOLD names the
    composting process, ENVO the resulting material; close but not exact. Path: Engineered
    > Solid waste > Composting > Oil palm", "object_id": "ENVO:00002170", "object_label":
    "compost", "relation": "", "review_depth": "ITEM"}, "logical_row": 886}, {"data":
    {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision":
    "REVIEW", "grounding_status": "", "identifier": "habitatmech:PREGO.e2f1a69477",
    "notes": "Multi-source review pass: this record is attested by more than one independent
    vocabulary, and this source''s label or path was read against the record''s ontology
    term to check the merge is right. It agrees. Source concepts in the same pass
    whose labels did not agree were re-decided rather than endorsed; see the pass''s
    other decisions of the same date.", "object_id": "", "object_label": "", "relation":
    "", "review_depth": "ITEM"}, "logical_row": 1515}, {"data": {"category": "", "curator":
    "claude-opus-5", "date": "2026-08-15", "decision": "REVIEW", "grounding_status":
    "", "identifier": "habitatmech:ENVIRONMENTS_TABLE.392f1cbccf", "notes": "Co-attestor
    review (#12): ''compost'' resolves to ENVO:00002170 ''compost''. Correct as seeded.",
    "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"},
    "logical_row": 1632}, {"data": {"category": "", "curator": "claude-opus-5", "date":
    "2026-08-15", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:MADIN.87d709b6aa",
    "notes": "Co-attestor review (#12): this source names the ontology CURIE itself,
    so its grounding is definitional rather than a lexical guess \u2014 the record
    IS the term the source pointed at. Recorded so the record it co-attests can reach
    REVIEWED, which needs every source concept decided.", "object_id": "", "object_label":
    "", "relation": "", "review_depth": "ITEM"}, "logical_row": 1638}], "curation/gold_parent_exclusions.tsv":
    [{"data": {"curator": "codex-gpt-5", "date": "2026-10-07", "identifier": "habitatmech:GOLD.4741a9f8bb",
    "notes": "ITEM hierarchy assessment (#1664): generic ENVO:00002170 compost material
    is not universally discarded Solid Waste. EPA (https://www.epa.gov/sustainable-management-food/composting)
    distinguishes organic waste inputs from stable soil-amendment product; NLM mesh:D062611
    denotes discarded materials. Suppress only this GOLD context contribution, preserving
    independent ENVO:03501300 manure, all source paths, heterogeneous counts and existing
    identity decisions. This does not settle the process/material scope of qualified
    GOLD Composting sources or assert a legal waste classification. Evidence: reports/yaml_record_review/20261007T222058Z-compost.md.",
    "parent_id": "mesh:D062611", "source_path": "Engineered > Solid waste > Composting"},
    "logical_row": 74}], "data/raw/environment_parameters.tsv": [{"data": {"cobo_simon_habitat":
    "NA", "env_type": "compost", "main_group": "Other", "parameter": "Gradients",
    "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "high"}, "logical_row":
    525}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group":
    "Other", "parameter": "Nutrients", "term_ids": "ENVO:00002170", "term_labels":
    "compost", "value": "high"}, "logical_row": 526}, {"data": {"cobo_simon_habitat":
    "NA", "env_type": "compost", "main_group": "Other", "parameter": "Organic", "term_ids":
    "ENVO:00002170", "term_labels": "compost", "value": "high"}, "logical_row": 527},
    {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group": "Other",
    "parameter": "Pressure", "term_ids": "ENVO:00002170", "term_labels": "compost",
    "value": "low"}, "logical_row": 528}, {"data": {"cobo_simon_habitat": "NA", "env_type":
    "compost", "main_group": "Other", "parameter": "Salinity", "term_ids": "ENVO:00002170",
    "term_labels": "compost", "value": "low"}, "logical_row": 529}, {"data": {"cobo_simon_habitat":
    "NA", "env_type": "compost", "main_group": "Other", "parameter": "Structural",
    "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "medium"}, "logical_row":
    530}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group":
    "Other", "parameter": "Water", "term_ids": "ENVO:00002170", "term_labels": "compost",
    "value": "medium"}, "logical_row": 531}, {"data": {"cobo_simon_habitat": "NA",
    "env_type": "compost", "main_group": "Other", "parameter": "pH", "term_ids": "ENVO:00002170",
    "term_labels": "compost", "value": "low"}, "logical_row": 532}, {"data": {"cobo_simon_habitat":
    "NA", "env_type": "compost", "main_group": "Other", "parameter": "salinity variability",
    "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "small"}, "logical_row":
    533}, {"data": {"cobo_simon_habitat": "NA", "env_type": "compost", "main_group":
    "Other", "parameter": "temp variability", "term_ids": "ENVO:00002170", "term_labels":
    "compost", "value": "medium"}, "logical_row": 534}, {"data": {"cobo_simon_habitat":
    "NA", "env_type": "compost", "main_group": "Other", "parameter": "water variability",
    "term_ids": "ENVO:00002170", "term_labels": "compost", "value": "occasionally
    dry"}, "logical_row": 535}], "data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count":
    "0", "canonical_path": "Engineered > Solid waste > Composting", "depth": "3",
    "ecosystem": "Engineered", "ecosystem_category": "Solid waste", "ecosystem_subtype":
    "", "ecosystem_type": "Composting", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:3511|gold.ecosystem:3842|gold.ecosystem:4273",
    "leaf_label": "Composting", "organism_count": "270", "specific_ecosystem": "",
    "study_count": "0", "total_assertions": "270"}, "logical_row": 100}, {"data":
    {"biosample_count": "0", "canonical_path": "Engineered > Solid waste > Composting
    > Oil palm", "depth": "4", "ecosystem": "Engineered", "ecosystem_category": "Solid
    waste", "ecosystem_subtype": "Oil palm", "ecosystem_type": "Composting", "gold_node_count":
    "2", "gold_node_ids": "gold.ecosystem:5755|gold.ecosystem:5756", "leaf_label":
    "Oil palm", "organism_count": "1", "specific_ecosystem": "", "study_count": "0",
    "total_assertions": "1"}, "logical_row": 907}], "data/raw/gold_path_biosamples.tsv":
    [{"data": {"biosample_count": "11", "canonical_path": "Engineered > Solid waste
    > Composting", "ecosystem_path_id": "4273"}, "logical_row": 609}], "data/raw/gold_studies.tsv":
    [{"data": {"path_count": "1", "paths": "Engineered > Solid waste > Composting",
    "study_gold_id": "Gs0145093"}, "logical_row": 2832}, {"data": {"path_count": "3",
    "paths": "Engineered > Solid waste > Composting|Host-associated > Arthropoda:
    Insects > Whole body|Host-associated > Fungi > Mycelium", "study_gold_id": "Gs0150459"},
    "logical_row": 3276}, {"data": {"path_count": "8", "paths": "Engineered > Industrial
    production > Chemical products > Lab-grade water|Engineered > Solid waste > Composting|Environmental
    > Air > Outdoor Air|Environmental > Aquatic > Deep subsurface > Groundwater >
    Contaminated|Environmental > Aquatic > Freshwater > Creek|Environmental > Terrestrial
    > Soil|Host-associated > Arthropoda: Chelicerates > Whole body|Host-associated
    > Arthropoda: Insects > Whole body", "study_gold_id": "Gs0156806"}, "logical_row":
    4124}], "data/raw/madin_habitat_taxa.tsv": [{"data": {"corroborated_by": "PREGO",
    "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1089552", "taxon_label": "Rhodovibrio
    salinarum DSM 9154"}, "logical_row": 505}, {"data": {"corroborated_by": "PREGO",
    "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1111737", "taxon_label": "Thermocrispum
    municipale DSM 44069"}, "logical_row": 506}, {"data": {"corroborated_by": "PREGO",
    "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1111738", "taxon_label": "Thermocrispum
    agreste DSM 44070"}, "logical_row": 507}, {"data": {"corroborated_by": "PREGO",
    "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121013", "taxon_label": "Arenimonas
    composti TR7-09, DSM 18010"}, "logical_row": 508}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121349", "taxon_label":
    "Comamonas composti DSM 21721"}, "logical_row": 509}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121385", "taxon_label":
    "Demetria terragena DSM 11295"}, "logical_row": 510}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121395", "taxon_label":
    "Desulfitobacterium chlororespirans DSM 11544"}, "logical_row": 511}, {"data":
    {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121927",
    "taxon_label": "Gordonia hirsuta K718a, DSM 44140"}, "logical_row": 512}, {"data":
    {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1121952",
    "taxon_label": "Humibacter albus DSM 18994"}, "logical_row": 513}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1122239", "taxon_label":
    "Microbacterium luticocti DSM 19459"}, "logical_row": 514}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1122958", "taxon_label":
    "Phenylobacterium composti DSM 19425"}, "logical_row": 515}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1123405", "taxon_label":
    "Tuberibacillus calidus DSM 17572"}, "logical_row": 516}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1292027", "taxon_label":
    "Pseudomonas azotifigens DSM 17556"}, "logical_row": 517}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1408", "taxon_label":
    "Bacillus pumilus"}, "logical_row": 518}, {"data": {"corroborated_by": "PREGO",
    "madin_id": "ENVO:00002170", "taxon_id": "NCBITaxon:1714", "taxon_label": "cellulomonas_uda"},
    "logical_row": 519}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170",
    "taxon_id": "NCBITaxon:269800", "taxon_label": "Thermobifida fusca YX"}, "logical_row":
    520}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id":
    "NCBITaxon:287", "taxon_label": "Pseudomonas aeruginosa"}, "logical_row": 521},
    {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id":
    "NCBITaxon:292459", "taxon_label": "Symbiobacterium thermophilum IAM 14863"},
    "logical_row": 522}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170",
    "taxon_id": "NCBITaxon:36773", "taxon_label": "burkholderia_sp"}, "logical_row":
    523}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id":
    "NCBITaxon:394503", "taxon_label": "Ruminiclostridium cellulolyticum H10"}, "logical_row":
    524}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id":
    "NCBITaxon:407022", "taxon_label": "pseudosphingobacterium_domesticum"}, "logical_row":
    525}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id":
    "NCBITaxon:471852", "taxon_label": "Thermomonospora curvata DSM 43183"}, "logical_row":
    526}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id":
    "NCBITaxon:644383", "taxon_label": "thermosporothrix_hazakensis"}, "logical_row":
    527}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id":
    "NCBITaxon:649349", "taxon_label": "Leadbetterella byssophila DSM 17132"}, "logical_row":
    528}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002170", "taxon_id":
    "NCBITaxon:743721", "taxon_label": "Pseudoxanthomonas suwonensis 11-1"}, "logical_row":
    529}], "data/raw/madin_habitats.tsv": [{"data": {"label": "compost", "madin_id":
    "ENVO:00002170", "taxon_count": "112", "vocabulary": "ENVO"}, "logical_row": 36}],
    "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score":
    "3", "rank": "1", "taxon_id": "NCBITaxon:1045004", "taxon_label": "Oenococcus
    kitaharae DSM 17330"}, "logical_row": 6183}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score":
    "3", "rank": "2", "taxon_id": "NCBITaxon:1045012", "taxon_label": "Acetivibrio
    clariflavus 4-2a"}, "logical_row": 6184}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170",
    "prego_score": "3", "rank": "3", "taxon_id": "NCBITaxon:1089552", "taxon_label":
    "Rhodovibrio salinarum DSM 9154"}, "logical_row": 6185}, {"data": {"channels":
    "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE",
    "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "4", "taxon_id": "NCBITaxon:1111737",
    "taxon_label": "Thermocrispum municipale DSM 44069"}, "logical_row": 6186}, {"data":
    {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag":
    "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "5", "taxon_id":
    "NCBITaxon:1111738", "taxon_label": "Thermocrispum agreste DSM 44070"}, "logical_row":
    6187}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3",
    "rank": "6", "taxon_id": "NCBITaxon:1121013", "taxon_label": "Arenimonas composti
    TR7-09 = DSM 18010"}, "logical_row": 6188}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170",
    "prego_score": "3", "rank": "7", "taxon_id": "NCBITaxon:1121349", "taxon_label":
    "Comamonas composti DSM 21721"}, "logical_row": 6189}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170",
    "prego_score": "3", "rank": "8", "taxon_id": "NCBITaxon:1121385", "taxon_label":
    "Demetria terragena DSM 11295"}, "logical_row": 6190}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170",
    "prego_score": "3", "rank": "9", "taxon_id": "NCBITaxon:1121395", "taxon_label":
    "Desulfitobacterium chlororespirans DSM 11544"}, "logical_row": 6191}, {"data":
    {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "10", "taxon_id":
    "NCBITaxon:1121431", "taxon_label": "Desulfallas thermosapovorans DSM 6562"},
    "logical_row": 6192}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3",
    "rank": "11", "taxon_id": "NCBITaxon:1121927", "taxon_label": "Gordonia hirsuta
    DSM 44140 = NBRC 16056"}, "logical_row": 6193}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170",
    "prego_score": "3", "rank": "12", "taxon_id": "NCBITaxon:1121952", "taxon_label":
    "Humibacter albus DSM 18994"}, "logical_row": 6194}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170",
    "prego_score": "3", "rank": "13", "taxon_id": "NCBITaxon:1122239", "taxon_label":
    "Microbacterium luticocti DSM 19459"}, "logical_row": 6195}, {"data": {"channels":
    "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE",
    "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "14", "taxon_id": "NCBITaxon:1122958",
    "taxon_label": "Phenylobacterium composti DSM 19425"}, "logical_row": 6196}, {"data":
    {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "15", "taxon_id":
    "NCBITaxon:1123024", "taxon_label": "Pseudonocardia asaccharolytica DSM 44247
    = NBRC 16224"}, "logical_row": 6197}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170",
    "prego_score": "3", "rank": "16", "taxon_id": "NCBITaxon:1123405", "taxon_label":
    "Tuberibacillus calidus DSM 17572"}, "logical_row": 6198}, {"data": {"channels":
    "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE",
    "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "17", "taxon_id": "NCBITaxon:1292027",
    "taxon_label": "Stutzerimonas azotifigens DSM 17556"}, "logical_row": 6199}, {"data":
    {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "18", "taxon_id":
    "NCBITaxon:1868734", "taxon_label": "Aeribacillus composti"}, "logical_row": 6200},
    {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "19", "taxon_id":
    "NCBITaxon:1970199", "taxon_label": "Sorangiineae bacterium NIC37A_2"}, "logical_row":
    6201}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3",
    "rank": "20", "taxon_id": "NCBITaxon:407022", "taxon_label": "Olivibacter domesticus"},
    "logical_row": 6202}, {"data": {"channels": "annotated_genomes_isolates|environmental_samples",
    "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170",
    "prego_score": "3", "rank": "21", "taxon_id": "NCBITaxon:471852", "taxon_label":
    "Thermomonospora curvata DSM 43183"}, "logical_row": 6203}, {"data": {"channels":
    "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE",
    "prego_id": "ENVO:00002170", "prego_score": "3", "rank": "22", "taxon_id": "NCBITaxon:644383",
    "taxon_label": "Thermosporothrix hazakensis"}, "logical_row": 6204}, {"data":
    {"channels": "annotated_genomes_isolates|environmental_samples", "corroborated_by":
    "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score": "3",
    "rank": "23", "taxon_id": "NCBITaxon:649349", "taxon_label": "Leadbetterella byssophila
    DSM 17132"}, "logical_row": 6205}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score":
    "2.82248", "rank": "24", "taxon_id": "NCBITaxon:39650", "taxon_label": "Cellvibrio
    mixtus"}, "logical_row": 6206}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002170", "prego_score":
    "2.77144", "rank": "25", "taxon_id": "NCBITaxon:155077", "taxon_label": "Cellvibrio
    japonicus"}, "logical_row": 6207}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category":
    "biolink:OntologyClass", "channels": "annotated_genomes_isolates|environmental_samples",
    "direct_assertion_count": "1915", "max_prego_score": "3", "ontology": "ENVO",
    "prego_id": "ENVO:00002170", "prego_synonyms": "compost|composts", "taxon_count":
    "1913"}, "logical_row": 40}]}. Logical TSV row ordinals include the header; not
    physical lines when cells contain newlines. Parent-owned rows are excluded from
    this target attestation audit.'
  locator: Exact source-mint, canonical-path or target-ID rows in maintained root
    TSVs
  accessed_at: '2026-10-11T07:12:04.137068Z'
  support: supports
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 5, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13",
    "decision": "GROUND", "grounding_status": "CLOSE", "identifier": "habitatmech:GOLD.4741a9f8bb",
    "notes": "GOLD names the composting process, ENVO the resulting material; close
    but not exact. Path: Engineered > Solid waste > Composting", "object_id": "ENVO:00002170",
    "object_label": "compost", "relation": "parent", "review_depth": "ITEM"}, "extra_parents":
    [], "extra_xrefs": [], "grounding_status": "CLOSE", "identifier": "ENVO:00002170",
    "mapping_predicate": "skos:closeMatch", "reviewed": true, "route": "curated_ground_from_gold_mapping_table"},
    "automatic": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier":
    "ENVO:00002170", "mapping_predicate": "skos:exactMatch", "reviewed": false, "route":
    "gold_mapping_table"}, "path": "Engineered > Solid waste > Composting"}, {"actual":
    {"category": null, "contributes_grounding": true, "decision": {"category": "",
    "curator": "claude-opus-5", "date": "2026-08-13", "decision": "GROUND", "grounding_status":
    "CLOSE", "identifier": "habitatmech:GOLD.981cf7502c", "notes": "GOLD names the
    composting process, ENVO the resulting material; close but not exact. Path: Engineered
    > Solid waste > Composting > Oil palm", "object_id": "ENVO:00002170", "object_label":
    "compost", "relation": "parent", "review_depth": "ITEM"}, "extra_parents": [],
    "extra_xrefs": [], "grounding_status": "CLOSE", "identifier": "ENVO:00002170",
    "mapping_predicate": "skos:closeMatch", "reviewed": true, "route": "curated_ground_from_gold_unmatched"},
    "automatic": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": [], "extra_xrefs": [], "grounding_status": "UNGROUNDED", "identifier":
    "habitatmech:GOLD.981cf7502c", "mapping_predicate": null, "reviewed": false, "route":
    "gold_unmatched"}, "path": "Engineered > Solid waste > Composting > Oil palm"}],
    "source_concepts": 5}. Complete build_document equality was checked. The ambiguous
    GOLD mapping route emits a mint with NARROW and an extra ontology parent; immediate
    source-path parents are contributed independently. Native status follows source
    decisions, not this review.'
  locator: resolve_gold mapping route, ingest_gold hierarchy, complete read-only reproduction
  accessed_at: '2026-10-11T07:12:04.137068Z'
  support: supports
- evidence_id: ONT
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies; https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.obo
  summary: '[{"definition": ["Manure which has been derived from the aerobically decomposed
    remnants of organic materials."], "id": "ENVO:00002170", "label": "compost", "obsolete":
    false}, {"definition": ["Most manure consists of animal feces; other sources include
    compost and green manure.", "An environmental material consisting of organic matter
    from plants and/or animals that is used in agriculture as fertilizer."], "id":
    "ENVO:03501300", "label": "manure", "obsolete": false}]. Ontology meaning verifies
    a term, not every GOLD source crosswalk.'
  locator: Exact target and direct ontology parent JSON labels, definitions and active
    state
  accessed_at: '2026-10-11T07:03:08.343635Z'
  support: supports
  snapshot_sha256: 2f0b693f1234bc7e0b47ee12ea8e9e29d8536f56f8e0e0479eb15e6065715b93
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats; data/raw/ontology_subclass_edges.tsv
  summary: '{"ENVO:03501300": {"definition": "An environmental material consisting
    of organic matter from plants and/or animals that is used in agriculture as fertilizer.",
    "identifier": "ENVO:03501300", "label": "manure", "parent_habitats": ["ENVO:00010483",
    "habitatmech:GOLD.18ee4196a9"], "source_attestations": [{"mapping_predicate":
    "skos:closeMatch", "source": "GOLD", "source_id": "gold.ecosystem:8076", "source_label":
    "Liquid manure", "source_path": "Engineered > Solid waste > Animal waste > Manure
    slurry > Liquid manure"}]}}. Direct-parent context only, not scientific review
    of their biological claims. Coal has no generated sedimentary-rock record in this
    capture; its ontology genus is checked directly.'
  locator: Captured direct-parent identity and provenance fields
  accessed_at: '2026-10-11T07:12:04.137068Z'
  support: supports
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  summary: 'Retained later export, not a fresh download or original frozen-member
    reconstruction. Complete streamed census counts including headers={"Biosample":
    244951, "Organism": 532019, "SequencingProject": 636914, "Study": 63806}; exact
    target matches={"Biosample": 12, "Organism": 259, "SequencingProject": 81}; inspected
    bounded source descriptions={"Biosample": [{"data": {"BIOSAMPLE GOLD ID": "Gb0247172",
    "BIOSAMPLE NAME": "Wheat straw compost microbial community from United Kingdom
    - WSC_Wk1_1", "BIOSAMPLE NCBI TAX NAME": "", "BIOSAMPLE SAMPLE COLLECTION SITE":
    "Wheat straw compost"}, "paths": ["Engineered > Solid waste > Composting"], "row":
    93613}, {"data": {"BIOSAMPLE GOLD ID": "Gb0247173", "BIOSAMPLE NAME": "Wheat straw
    compost microbial community from United Kingdom - WSC_Wk1_2", "BIOSAMPLE NCBI
    TAX NAME": "", "BIOSAMPLE SAMPLE COLLECTION SITE": "Wheat straw compost"}, "paths":
    ["Engineered > Solid waste > Composting"], "row": 93614}, {"data": {"BIOSAMPLE
    GOLD ID": "Gb0247174", "BIOSAMPLE NAME": "Wheat straw compost microbial community
    from United Kingdom - WSC_Wk1_3", "BIOSAMPLE NCBI TAX NAME": "", "BIOSAMPLE SAMPLE
    COLLECTION SITE": "Wheat straw compost"}, "paths": ["Engineered > Solid waste
    > Composting"], "row": 93615}], "Organism": [{"data": {"ORGANISM GOLD ID": "Go0075327",
    "ORGANISM HABITAT": "", "ORGANISM ISOLATION HOST NAME": "", "ORGANISM NAME": "Streptomyces
    exfoliatus DSM 41693", "ORGANISM SAMPLE COLLECTION SITE": "Compost"}, "paths":
    ["Engineered > Solid waste > Composting"], "row": 46758}, {"data": {"ORGANISM
    GOLD ID": "Go0086731", "ORGANISM HABITAT": "", "ORGANISM ISOLATION HOST NAME":
    "", "ORGANISM NAME": "Acetivibrio straminisolvens JCM 21531", "ORGANISM SAMPLE
    COLLECTION SITE": "a bacterial community constructed from composting processes"},
    "paths": ["Engineered > Solid waste > Composting"], "row": 51944}, {"data": {"ORGANISM
    GOLD ID": "Go0089984", "ORGANISM HABITAT": "Compost", "ORGANISM ISOLATION HOST
    NAME": "", "ORGANISM NAME": "Agrilactobacillus composti JCM 14202", "ORGANISM
    SAMPLE COLLECTION SITE": "composting material of distilled shochu residue"}, "paths":
    ["Engineered > Solid waste > Composting"], "row": 53386}]}. Other matched descriptions
    and joined studies are inventoried, not all independently reviewed. Empty and
    Unclassified normalize to empty without dropping tuple positions. Projects retain
    both matched source paths; study counts are not habitat assertion counts.'
  locator: Exact five-position tuples; first-three member descriptions except all16
    latrine BioSamples and all8 vegetable organisms
  accessed_at: '2026-10-11T07:12:04.137068Z'
  support: supports
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: CLASS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'Later retained classification snapshot SHA256 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396;
    exact rows=[{"row": 387, "slug": "compost", "path": "Engineered > Solid waste
    > Composting > Oil palm", "values": ["5756", "Engineered", "Solid waste", "Composting",
    "Oil palm", "Unclassified"]}, {"row": 388, "slug": "compost", "path": "Engineered
    > Solid waste > Composting", "values": ["4273", "Engineered", "Solid waste", "Composting",
    "Unclassified", "Unclassified"]}]. Original endpoint was not retained. A miss
    is bounded to this snapshot.'
  locator: Classification site-data sheet exact five-position tuple
  accessed_at: '2026-10-11T07:12:04.137068Z'
  support: supports
  snapshot_sha256: 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
- evidence_id: PROCESS
  kind: authority
  reference: https://www.epa.gov/sustainable-management-food/composting
  summary: Composting is an aerobic decomposition process; compost is its stabilized
    product. Feedstock, active material and facility are distinct. This terminology
    does not define a GOLD source category.
  locator: Definitions and Composting Basics and Approaches
  accessed_at: '2026-10-11T07:03:17.872451Z'
  support: supports
  snapshot_sha256: e6cd64095d42cde62481c328089810f616ead29abe94aa249e3c6da6c897c471
- evidence_id: SEARCH
  kind: search
  reference: curation; data/raw; history; research; reports; reviews; conf
  summary: 'Ignored/hidden-inclusive rg and Path.rglob searches covered identifiers,
    paths, labels and slugs, all root raw/curation TSVs and all32 overlay identifiers.
    No previous completed scientific structured review targeted this exact ID at capture.
    Only compost has a target overlay in this selection. Configured original-source
    paths were checked including ignored files: [{"command": ["rg", "--files", "--no-ignore",
    "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold"],
    "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold:
    No such file or directory (os error 2)\n"}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego"],
    "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego:
    No such file or directory (os error 2)\n"}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal"],
    "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal:
    No such file or directory (os error 2)\n"}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv"],
    "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv:
    No such file or directory (os error 2)\n"}]. These are bounded path failures,
    not global source absence.'
  locator: Saved support-search and exact-row audits
  accessed_at: '2026-10-11T07:12:04.137068Z'
  support: supports
  search_scope: 'Ignored/hidden-inclusive rg and Path.rglob searches covered identifiers,
    paths, labels and slugs, all root raw/curation TSVs and all32 overlay identifiers.
    No previous completed scientific structured review targeted this exact ID at capture.
    Only compost has a target overlay in this selection. Configured original-source
    paths were checked including ignored files: [{"command": ["rg", "--files", "--no-ignore",
    "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold"],
    "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold:
    No such file or directory (os error 2)\n"}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego"],
    "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego:
    No such file or directory (os error 2)\n"}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal"],
    "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal:
    No such file or directory (os error 2)\n"}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv"],
    "exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv:
    No such file or directory (os error 2)\n"}]. These are bounded path failures,
    not global source absence.'
- evidence_id: SOURCE-CONTEXT
  kind: record_content
  reference: data/habitats/engineered/compost.yaml
  summary: ENVO compost and its broad manure genus are supported; manure here includes
    plant-derived organic fertilizer, not only animal excrement. All five contributors
    have ITEM decisions. GOLD Composting and Oil palm remain CLOSE with RELATED synonyms,
    not exact aliases. The corrected active-phase graph is supported within its stated
    scope. Two source taxon names and a conflicting strain-origin association need
    bounded provenance follow-up.
  locator: Field-by-field interpretation of the exact record against inspected evidence
  accessed_at: '2026-10-11T07:12:04.137068Z'
  support: supports
- evidence_id: TAXA
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1045004%2C1045012%2C1089552%2C1111737%2C1111738%2C1121013%2C1121349%2C1121385%2C1121395%2C1121431%2C1121927%2C1121952%2C1122239%2C1122958%2C1123024%2C1123405%2C1292027%2C1408%2C155077%2C1714%2C1868734%2C1970199%2C269800%2C287%2C292459%2C36773%2C394503%2C39650%2C407022%2C420662%2C471852%2C644383%2C649349%2C743721&retmode=xml
  summary: '[{"canonical_name": "Rhodovibrio salinarum DSM 9154", "rank": "strain",
    "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 3, "score":
    3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1089552", "taxon_label": "Rhodovibrio
    salinarum DSM 9154"}}, {"canonical_name": "Thermocrispum municipale DSM 44069",
    "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"],
    "rank": 4, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1111737", "taxon_label":
    "Thermocrispum municipale DSM 44069"}}, {"canonical_name": "Thermocrispum agreste
    DSM 44070", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by":
    ["MADIN"], "rank": 5, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1111738",
    "taxon_label": "Thermocrispum agreste DSM 44070"}}, {"canonical_name": "Arenimonas
    composti TR7-09 = DSM 18010", "rank": "strain", "source": {"candidate_pool": 1913,
    "corroborated_by": ["MADIN"], "rank": 6, "score": 3.0, "source": "PREGO", "taxon_id":
    "NCBITaxon:1121013", "taxon_label": "Arenimonas composti TR7-09 = DSM 18010"}},
    {"canonical_name": "Comamonas composti DSM 21721", "rank": "strain", "source":
    {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 7, "score": 3.0,
    "source": "PREGO", "taxon_id": "NCBITaxon:1121349", "taxon_label": "Comamonas
    composti DSM 21721"}}, {"canonical_name": "Demetria terragena DSM 11295", "rank":
    "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank":
    8, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1121385", "taxon_label":
    "Demetria terragena DSM 11295"}}, {"canonical_name": "Desulfitobacterium chlororespirans
    DSM 11544", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by":
    ["MADIN"], "rank": 9, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1121395",
    "taxon_label": "Desulfitobacterium chlororespirans DSM 11544"}}, {"canonical_name":
    "Gordonia hirsuta DSM 44140 = NBRC 16056", "rank": "strain", "source": {"candidate_pool":
    1913, "corroborated_by": ["MADIN"], "rank": 11, "score": 3.0, "source": "PREGO",
    "taxon_id": "NCBITaxon:1121927", "taxon_label": "Gordonia hirsuta DSM 44140 =
    NBRC 16056"}}, {"canonical_name": "Humibacter albus DSM 18994", "rank": "strain",
    "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank": 12, "score":
    3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1121952", "taxon_label": "Humibacter
    albus DSM 18994"}}, {"canonical_name": "Microbacterium luticocti DSM 19459", "rank":
    "strain", "source": {"candidate_pool": 1913, "corroborated_by": ["MADIN"], "rank":
    13, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1122239", "taxon_label":
    "Microbacterium luticocti DSM 19459"}}, {"canonical_name": "Phenylobacterium composti
    DSM 19425", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by":
    ["MADIN"], "rank": 14, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1122958",
    "taxon_label": "Phenylobacterium composti DSM 19425"}}, {"canonical_name": "Tuberibacillus
    calidus DSM 17572", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by":
    ["MADIN"], "rank": 16, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1123405",
    "taxon_label": "Tuberibacillus calidus DSM 17572"}}, {"canonical_name": "Stutzerimonas
    azotifigens DSM 17556", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by":
    ["MADIN"], "rank": 17, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1292027",
    "taxon_label": "Stutzerimonas azotifigens DSM 17556"}}, {"canonical_name": "Olivibacter
    domesticus", "rank": "species", "source": {"candidate_pool": 1913, "corroborated_by":
    ["MADIN"], "rank": 20, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:407022",
    "taxon_label": "Olivibacter domesticus"}}, {"canonical_name": "Thermomonospora
    curvata DSM 43183", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by":
    ["MADIN"], "rank": 21, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:471852",
    "taxon_label": "Thermomonospora curvata DSM 43183"}}, {"canonical_name": "Thermosporothrix
    hazakensis", "rank": "species", "source": {"candidate_pool": 1913, "corroborated_by":
    ["MADIN"], "rank": 22, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:644383",
    "taxon_label": "Thermosporothrix hazakensis"}}, {"canonical_name": "Leadbetterella
    byssophila DSM 17132", "rank": "strain", "source": {"candidate_pool": 1913, "corroborated_by":
    ["MADIN"], "rank": 23, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:649349",
    "taxon_label": "Leadbetterella byssophila DSM 17132"}}, {"canonical_name": "Bacillus
    pumilus", "rank": "species", "source": {"candidate_pool": 112, "corroborated_by":
    ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:1408", "taxon_label": "Bacillus
    pumilus"}}, {"canonical_name": "Cellulomonas uda", "rank": "species", "source":
    {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id":
    "NCBITaxon:1714", "taxon_label": "cellulomonas_uda"}}, {"canonical_name": "Thermobifida
    fusca YX", "rank": "strain", "source": {"candidate_pool": 112, "corroborated_by":
    ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:269800", "taxon_label": "Thermobifida
    fusca YX"}}, {"canonical_name": "Pseudomonas aeruginosa", "rank": "species", "source":
    {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id":
    "NCBITaxon:287", "taxon_label": "Pseudomonas aeruginosa"}}, {"canonical_name":
    "Symbiobacterium thermophilum IAM 14863", "rank": "strain", "source": {"candidate_pool":
    112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:292459",
    "taxon_label": "Symbiobacterium thermophilum IAM 14863"}}, {"canonical_name":
    "Burkholderia sp.", "rank": "species", "source": {"candidate_pool": 112, "corroborated_by":
    ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:36773", "taxon_label": "burkholderia_sp"}},
    {"canonical_name": "Ruminiclostridium cellulolyticum H10", "rank": "strain", "source":
    {"candidate_pool": 112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id":
    "NCBITaxon:394503", "taxon_label": "Ruminiclostridium cellulolyticum H10"}}, {"canonical_name":
    "Pseudoxanthomonas suwonensis 11-1", "rank": "strain", "source": {"candidate_pool":
    112, "corroborated_by": ["PREGO"], "source": "MADIN", "taxon_id": "NCBITaxon:743721",
    "taxon_label": "Pseudoxanthomonas suwonensis 11-1"}}, {"canonical_name": "Oenococcus
    kitaharae DSM 17330", "rank": "strain", "source": {"candidate_pool": 1913, "rank":
    1, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1045004", "taxon_label":
    "Oenococcus kitaharae DSM 17330"}}, {"canonical_name": "Acetivibrio clariflavus
    4-2a", "rank": "strain", "source": {"candidate_pool": 1913, "rank": 2, "score":
    3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1045012", "taxon_label": "Acetivibrio
    clariflavus 4-2a"}}, {"canonical_name": "Desulfallas thermosapovorans DSM 6562",
    "rank": "strain", "source": {"candidate_pool": 1913, "rank": 10, "score": 3.0,
    "source": "PREGO", "taxon_id": "NCBITaxon:1121431", "taxon_label": "Desulfallas
    thermosapovorans DSM 6562"}}, {"canonical_name": "Pseudonocardia asaccharolytica
    DSM 44247 = NBRC 16224", "rank": "strain", "source": {"candidate_pool": 1913,
    "rank": 15, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1123024",
    "taxon_label": "Pseudonocardia asaccharolytica DSM 44247 = NBRC 16224"}}, {"canonical_name":
    "Aeribacillus composti", "rank": "species", "source": {"candidate_pool": 1913,
    "rank": 18, "score": 3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1868734",
    "taxon_label": "Aeribacillus composti"}}, {"canonical_name": "Sorangiineae bacterium
    NIC37A_2", "rank": "species", "source": {"candidate_pool": 1913, "rank": 19, "score":
    3.0, "source": "PREGO", "taxon_id": "NCBITaxon:1970199", "taxon_label": "Sorangiineae
    bacterium NIC37A_2"}}, {"canonical_name": "Cellvibrio mixtus", "rank": "species",
    "source": {"candidate_pool": 1913, "rank": 24, "score": 2.82248, "source": "PREGO",
    "taxon_id": "NCBITaxon:39650", "taxon_label": "Cellvibrio mixtus"}}, {"canonical_name":
    "Cellvibrio japonicus", "rank": "species", "source": {"candidate_pool": 1913,
    "rank": 25, "score": 2.77144, "source": "PREGO", "taxon_id": "NCBITaxon:155077",
    "taxon_label": "Cellvibrio japonicus"}}]. Every displayed ID resolves directly
    without a merged alias. Ranks are mixed species/strain and source ranking is not
    abundance. No is_characteristic flag is asserted. Source agreement is not proof
    of independent experiments.'
  locator: NCBI efetch Taxon ID, ScientificName, Rank and AkaTaxIds for all displayed
    associations
  accessed_at: '2026-10-11T07:03:20.333907Z'
  support: supports
  snapshot_sha256: d56b2a4a53788acbad1ee5806560688b7889e6350e2bbf6c2cd27c2990a58d64
- evidence_id: GRAPH
  kind: primary_source
  reference: PMID:16454493; DOI:10.1021/bp050171d; DOI:10.1186/s40538-023-00381-z
  summary: Richard2006 abstract verifies oxygen-dependent biodegradation across tested
    substrate, temperature and moisture conditions, including a reversal at65C; not
    universal monotonic stimulation. Finore2023 is explicitly a review. Inspected
    introduction, thermodynamics, thermophilic succession and enzyme passages support
    substrate use, heat generation with heat loss, temperature-dependent succession
    and enzyme activities in active plant-rich composting. All five short snippets
    match normalized source text. The graph history explicitly limits active thermophilic
    scope; it does not describe every mature compost or a single experiment.
  locator: Richard PubMed XML title/authors/DOI/abstract; Finore publisher named sections
    and five edge snippets
  accessed_at: '2026-10-11T07:03:18.235889Z'
  support: supports
  snapshot_sha256: adc8ac97ceec0dbf80935e34b6617504b5e9dfdabe71b727b9356e6df926694c
- evidence_id: STRAIN-ORIGIN
  kind: authority
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-9154
  summary: DSM9154 is the Rhodovibrio salinarum type strain, also ATCC35394, with
    Portugal saltern collection provenance. Later GOLD Go0014368 instead labels its
    collection site compost feedstock. This conflict requires original assertion tracing;
    it is not proof the organism cannot occur in compost.
  locator: DSMZ name, collection-number and origin fields; exact later GOLD row Go0014368
  accessed_at: '2026-10-11T07:12:04.137068Z'
  support: context_only
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Ontology identity and direct genus
  outcome: supported
  summary: ENVO compost and its broad manure genus are supported; manure here includes
    plant-derived organic fertilizer, not only animal excrement. All five contributors
    have ITEM decisions. GOLD Composting and Oil palm remain CLOSE with RELATED synonyms,
    not exact aliases. The corrected active-phase graph is supported within its stated
    scope. Two source taxon names and a conflicting strain-origin association need
    bounded provenance follow-up.
  target_ids:
  - ENVO:00002170
  evidence_ids:
  - R
  - ONT
  - RAW
  - PARENT
- assessment_id: TAXON
  area: evidence
  topic: Reported associations, taxonomy and source caps
  outcome: concern
  summary: All displayed pairs trace to the frozen source rows; IDs resolve. 33 displayed
    entries are the union of two top25 lists with17 shared IDs; source pools112 and1913
    are distinct, not summed. Qualitative parameters are source bands, not measurements
    or universal bounds.
  target_ids:
  - ENVO:00002170
  evidence_ids:
  - R
  - RAW
  - TAXA
- assessment_id: GRAPH
  area: evidence
  topic: Five scoped causal edges
  outcome: supported
  summary: Corrected node types distinguish substrate habitat, temperature parameter
    and community succession. Direction and evidence support the five active-phase
    edges; the Finore edges are synthesis-level evidence and do not imply universal
    optimum conditions.
  target_ids:
  - ENVO:00002170
  evidence_ids:
  - R
  - GRAPH
  - RULES
- assessment_id: PARAMETERS
  area: scope
  topic: Eleven qualitative source axes
  outcome: supported
  summary: Each parameter comes from the single-term compost row. The low pH band
    is source qualitative classification, not an invariant numeric pH; phase/feedstock
    variability and absent numerical thresholds limit interpretation. No multi-term
    component row was attached.
  target_ids:
  - ENVO:00002170
  evidence_ids:
  - R
  - RAW
  - RULES
  - GRAPH
- assessment_id: PROVENANCE
  area: provenance
  topic: Counts, predicates, source and status
  outcome: supported
  summary: Frozen source IDs, paths, node collapse, organism counts and zero omissions
    match. All fields reproduce. 5/5 source concepts have ITEM decisions; this review
    does not promote native status. Unlike counts and later snapshots are not additive.
  target_ids:
  - ENVO:00002170
  evidence_ids:
  - R
  - RAW
  - CODE
  - RULES
- assessment_id: COMPLETENESS
  area: completeness
  topic: Claim-proportionate fields and missing evidence
  outcome: supported
  summary: No required field gap is established by optional absent taxa, parameters,
    definitions or graphs. Missing original assertion evidence is a stated limit,
    not permission to invent biological facts. Relevant source intent and hierarchy
    defects remain explicit findings.
  target_ids:
  - ENVO:00002170
  evidence_ids:
  - R
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: envo-00002170-taxon-display-labels
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Two MADIN display labels are source-normalized tokens
  description: NCBITaxon1714 and36773 resolve as Cellulomonas uda and Burkholderia
    sp.; the record displays cellulomonas_uda and burkholderia_sp. The associations
    and stable IDs are not thereby invalid.
  target_ids:
  - ENVO:00002170
  field_paths:
  - characteristic_taxa[18].taxon_label
  - characteristic_taxa[22].taxon_label
  evidence_ids:
  - R
  - RAW
  - TAXA
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Bounded source-display or conflicting provenance problem,
    not demonstrated wrong habitat identity or ecological absence.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/extract.py
    role: Governed taxonomy display normalization
  - repository: culturebotai/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Source-derived display inventory
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1666
- finding_id: F2
  issue_key: envo-00002170-strain-origin-context
  category: provenance
  severity: minor
  status: open
  certainty: provisional
  title: Strain-origin conflict needs assertion-level provenance
  description: Rhodovibrio salinarum DSM9154 (NCBITaxon1089552) is PREGO rank3 and
    MADIN-corroborated. DSMZ reports saltern origin, whereas later GOLD Go0014368
    says compost feedstock. Repeated vocabulary agreement is not necessarily independent
    biological evidence. The schema only claims association, so this is a provenance
    question, not demonstrated false occurrence.
  target_ids:
  - ENVO:00002170
  field_paths:
  - characteristic_taxa[0]
  evidence_ids:
  - R
  - RAW
  - TAXA
  - STRAIN-ORIGIN
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: minor
  normalization_reason: Bounded source-display or conflicting provenance problem,
    not demonstrated wrong habitat identity or ecological absence.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/extract.py
    role: Assertion-level source context
  - repository: culturebotai/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Governed association provenance
  - repository: culturebotai/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Governed corroboration provenance
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1912
actions:
- action_id: A1
  description: Refresh through a pinned governed taxonomy input, retaining original
    source labels and IDs. Do not hand-edit generated records or silently relabel
    unrelated taxon pools.
  finding_ids:
  - F1
  target_ids:
  - ENVO:00002170
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/extract.py
    role: Governed taxonomy display normalization
  - repository: culturebotai/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Source-derived display inventory
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Inspect exact source identity and supporting primary metadata; do not infer absence
    or invent a replacement class.
  - Preserve mint/path, counts and units, source status and every immutable review.
    Append native history for authorized changes.
  - Exercise an exact regression, dry seed and inspect a target canary, regenerate
    affected products, then run schema, strict, history, label, corpus and full QC
    gates.
- action_id: A2
  description: Recover original PREGO and Madin support for the exact strain. Distinguish
    isolation origin from subsequent detection/enrichment; preserve conflicting metadata
    and change an association only with direct evidence.
  finding_ids:
  - F2
  target_ids:
  - ENVO:00002170
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/extract.py
    role: Assertion-level source context
  - repository: culturebotai/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Governed association provenance
  - repository: culturebotai/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Governed corroboration provenance
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Inspect exact source identity and supporting primary metadata; do not infer absence
    or invent a replacement class.
  - Preserve mint/path, counts and units, source status and every immutable review.
    Append native history for authorized changes.
  - Exercise an exact regression, dry seed and inspect a target canary, regenerate
    affected products, then run schema, strict, history, label, corpus and full QC
    gates.
limitations:
- One exact record is assessed; parent context and later member inventories do not
  add reviewed records.
- Original frozen assertion-level support is not reconstructed; later GOLD exports
  are contextual and do not replace original counts.
- Only explicitly described member fields and paper passages were inspected, not every
  study or full paper, and no figure-dependent inference is made.
- Current NLM JSON requests for Solid Waste reset; no target depends on adopting a
  new MeSH identity. Stable direct target/ontology parent IDs were separately checked.
- iModulonDB is not applicable to the claims in these records; no expression-module
  inference is made.
- This pre-curation observation does not certify SSSOM/KGX readiness, authorize native
  status promotion, or close prior issues. Original bundles remain immutable.
notes:
- The all-record review goal remains active.
- Legacy reviews are leads, not copied verdicts or normalized predecessor observations.
  Existing open issues are not silently closed.
tags:
- habitatmech
- engineered
- record-review
- scientific-review
```
