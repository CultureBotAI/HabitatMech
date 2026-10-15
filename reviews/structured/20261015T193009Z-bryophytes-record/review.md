# Record review: Bryophytes (habitatmech:GOLD.35beb98884)

- Review: 20261015T193009Z-bryophytes-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T19:05:01Z
- Finished UTC: 2026-10-15T19:30:09Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact Host-associated &gt; Plants &gt; Bryophytes source denotes bryophytes acting as microbial hosts, consistently under a green-plant-associated environment. Primary isolation of bacteria from two named bryophytes supports that interpretation, not a specific GOLD observation. The zero tree count, CLASS/SEEDED status and absent optional definition do not independently establish a defect. No taxon identity is substituted for the minted environment.

## Scope And Provenance

Full field-by-field scientific assessment of this exact target at a073f8e821a7c095f35501982930cc5a156835c0.

Selection: One of the next 24 path-ordered unreviewed identifiers in an ignored-inclusive 3208-record census. This bundle reviews one identifier, not a sample standing for other targets.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base a073f8e821a7c095f35501982930cc5a156835c0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.35beb98884 | data/habitats/host_associated/bryophytes.yaml | generated | Bryophytes |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.35beb98884 | Finished 2026-10-15T19:08:53Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bryophytes.yaml |
| validate-strict | passed | True | habitatmech:GOLD.35beb98884 | Finished 2026-10-15T19:10:07Z. uv run python scripts/validate_strict.py data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.35beb98884 | Finished 2026-10-15T19:10:18Z. No issues found<br>816 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.35beb98884 | Finished 2026-10-15T19:10:19Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.35beb98884 | Finished 2026-10-15T19:10:38Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.35beb98884 | Finished 2026-10-15T19:10:44Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.35beb98884 | Finished 2026-10-15T19:11:04Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.35beb98884 | Finished 2026-10-15T19:12:07Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | habitatmech:GOLD.35beb98884 | Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592 |

## Scientific And Domain Assessments

### Identity, definition, category and broader ancestry

identity: supported. Targets: habitatmech:GOLD.35beb98884.

The exact Host-associated &gt; Plants &gt; Bryophytes source denotes bryophytes acting as microbial hosts, consistently under a green-plant-associated environment. Primary isolation of bacteria from two named bryophytes supports that interpretation, not a specific GOLD observation. The zero tree count, CLASS/SEEDED status and absent optional definition do not independently establish a defect. No taxon identity is substituted for the minted environment.

### Source counts, units, ranks, pools and channels

quantity: supported. Targets: habitatmech:GOLD.35beb98884.

Every attestation and displayed taxon was compared with its exact frozen source row. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Side-table biosamples and study memberships are separate from tree ORGANISM counts; zero-count omission is not biological absence.

### Biological support and limits

evidence: supported. Targets: habitatmech:GOLD.35beb98884.

The exact Host-associated &gt; Plants &gt; Bryophytes source denotes bryophytes acting as microbial hosts, consistently under a green-plant-associated environment. Primary isolation of bacteria from two named bryophytes supports that interpretation, not a specific GOLD observation. The zero tree count, CLASS/SEEDED status and absent optional definition do not independently establish a defect. No taxon identity is substituted for the minted environment.

### Curation status, parameters, mechanisms and optional content

completeness: supported. Targets: habitatmech:GOLD.35beb98884.

Executed routes reproduce UNGROUNDED/SEEDED. No target environmental parameters, causal edges, discussions/datasets or is_characteristic=true assertions are present. Parent-record mechanisms are not inherited. Optional absence and SEEDED status alone are not defects.

### Native deterministic gates

schema: supported. Targets: habitatmech:GOLD.35beb98884.

Ordinary and strict schema, 816 curation histories, provenance, exact 3208-record reproduction, 32 causal overlays, term requests, configured labels and exact-base QC passed. Deterministic fidelity does not establish biological correctness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bryophytes.yaml; Entire target YAML | supports | All fields, displayed taxa and complete curation history read. |
| ERULE | docs/CURATION.md; Identity, hierarchy and source-evidence rules | supports | All parent contributions must be strictly broader; host identity is not environment identity. Source occurrences are not automatically characteristic. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation and category enums | supports | Source-to-record mapping endpoints; reported associations versus characteristic assertions; category scope and optional fields. |
| ESEED | src/habitatmech/seed.py; Executed resolution routes, parent accumulation, prefix category and overrides | supports | Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:GOLD.35beb98884", "automatic": {"identifier": "habitatmech:GOLD.35beb98884", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.35beb98884", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_unmatched", "category": null, "reviewed": false, "decision": {"identifier": "habitatmech:GOLD.35beb98884", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Inventory projection | supports | Counts/units and taxon ranks/scores preserve source meanings. PREGO projections omit original pair-level citation links. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 2497 | supports | [{"row": 2497, "data": {"canonical_path": "Host-associated &gt; Plants &gt; Bryophytes", "ecosystem": "Host-associated", "ecosystem_category": "Plants", "ecosystem_type": "Bryophytes", "ecosystem_subtype": "", "specific_ecosystem": "", "leaf_label": "Bryophytes", "depth": "3", "gold_node_count": "3", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:8107&#124;gold.ecosystem:8108&#124;gold.ecosystem:8109"}}] |
| ET6 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 6796 | supports | [{"row": 6796, "data": {"subject": "ENVO:01001001", "predicate": "rdfs:subClassOf", "object": "ENVO:01001000"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 8490 | supports | [{"row": 8490, "data": {"term_id": "ENVO:01001001", "ontology": "ENVO", "label": "plant-associated environment", "definition": "An environmental system determined by a green plant.", "synonyms": "Viridiplantae-associated environment&#124;plant environment", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET8 | curation/decisions.tsv; Physical TSV rows 401 | supports | [{"row": 401, "data": {"identifier": "habitatmech:GOLD.35beb98884", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS", "category": "", "relation": ""}}] |
| EP9 | data/habitats/host_associated/plant_associated_environment.yaml; Entire immediate parent record; context only | supports | {"identifier": "ENVO:01001001", "label": "plant-associated environment", "definition": "An environmental system determined by a green plant.", "definition_source": "ENVO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "Herbaceous-plants-Grass,Crops", "synonym_type": "RELATED_SYNONYM", "source": "BacDive"}, {"synonym_text": "Plants", "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "Viridiplantae-associated environment", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"}, {"synonym_text": "plant environment", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"}], "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"source": "BACDIVE", "source_id": "bacdive.isolation_source:herbaceous-plants-grass,crops", "source_label": "Herbaceous-plants-Grass,Crops", "mapping_predicate": "skos:broadMatch", "assertion_count": 2451, "assertion_unit": "STRAIN", "notes": "kg-microbe's isolation-source mapping table has no ontology target for this source; the automatic route leaves it ungrounded. The explicit curator decision GROUND overrides that route; this source is emitted on ENVO:01001001."}, {"source": "ENVIRONMENTS_TABLE", "source_id": "host_plant", "source_label": "host_plant", "notes": "Physicochemical parameter bands from kg-microbe's environment table."}, {"source": "GOLD", "source_id": "gold.ecosystem:3385", "source_label": "Plants", "source_path": "Host-associated &gt; Plants", "mapping_predicate": "skos:exactMatch", "assertion_count": 12638, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "MADIN", "source_id": "ENVO:01001001", "source_label": "plant-associated environment", "assertion_count": 1206, "assertion_unit": "TAXON"}], "environmental_parameters": [{"parameter": "GRADIENTS", "qualitative_value": "high", "source": "kg-microbe environments.csv (host_plant)"}, {"parameter": "PRESSURE", "qualitative_value": "low", "source": "kg-microbe environments.csv (host_plant)"}, {"parameter": "SALINITY_VARIABILITY", "qualitative_value": "small", "source": "kg-microbe environments.csv (host_plant)"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:28214", "source": "BACDIVE", "taxon_label": "Sphingomonas sp.", "association_count": 46, "rank": 1, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:409", "source": "BACDIVE", "taxon_label": "Methylobacterium sp.", "association_count": 43, "rank": 2, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:339", "source": "BACDIVE", "taxon_label": "Xanthomonas campestris", "association_count": 39, "rank": 3, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:56", "source": "BACDIVE", "taxon_label": "Sorangium cellulosum", "association_count": 39, "rank": 4, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:54", "source": "BACDIVE", "taxon_label": "Nannocystis exedens", "association_count": 35, "rank": 5, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:184914", "source": "BACDIVE", "taxon_label": "Corallococcus coralloides", "association_count": 33, "rank": 6, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:317", "source": "BACDIVE", "taxon_label": "Pseudomonas syringae", "association_count": 33, "rank": 7, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:391", "source": "BACDIVE", "taxon_label": "Rhizobium sp.", "association_count": 30, "rank": 8, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:554", "source": "BACDIVE", "taxon_label": "Pectobacterium carotovorum", "association_count": 30, "rank": 9, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:306", "source": "BACDIVE", "taxon_label": "Pseudomonas sp.", "association_count": 26, "rank": 10, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:305", "source": "BACDIVE", "taxon_label": "Ralstonia solanacearum", "association_count": 22, "rank": 11, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1930", "source": "BACDIVE", "taxon_label": "Streptomyces scabiei", "association_count": 20, "rank": 12, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1931", "source": "BACDIVE", "taxon_label": "Streptomyces sp.", "association_count": 20, "rank": 13, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:83428", "source": "BACDIVE", "taxon_label": "uncultured Bacillus sp.", "association_count": 19, "rank": 14, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:51671", "source": "BACDIVE", "taxon_label": "Microbacterium sp.", "association_count": 18, "rank": 15, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1405", "source": "BACDIVE", "taxon_label": "Bacillus mycoides", "association_count": 15, "rank": 16, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:2161", "source": "BACDIVE", "taxon_label": "Methanobacterium bryantii", "association_count": 15, "rank": 17, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:35761", "source": "BACDIVE", "taxon_label": "Nocardioides sp.", "association_count": 15, "rank": 18, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:58172", "source": "BACDIVE", "taxon_label": "Paenibacillus sp.", "association_count": 14, "rank": 19, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1872086", "source": "BACDIVE", "taxon_label": "Ensifer sp.", "association_count": 13, "rank": 20, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1428", "source": "BACDIVE", "taxon_label": "Bacillus thuringiensis", "association_count": 12, "rank": 21, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1872122", "source": "BACDIVE", "taxon_label": "Acidovorax sp.", "association_count": 12, "rank": 22, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:2035", "source": "BACDIVE", "taxon_label": "Curtobacterium flaccumfaciens", "association_count": 11, "rank": 23, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1411316", "source": "BACDIVE", "taxon_label": "Pedobacter sp.", "association_count": 10, "rank": 24, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1871063", "source": "BACDIVE", "taxon_label": "Aeromicrobium sp.", "association_count": 10, "rank": 25, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1002809", "source": "MADIN", "taxon_label": "Solibacillus silvestris StLB046", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1003091", "source": "MADIN", "taxon_label": "methylobacterium_thuringiense", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1003092", "source": "MADIN", "taxon_label": "Methylobacterium trifolii", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1003237", "source": "MADIN", "taxon_label": "Nitrospirillum amazonense Y2", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1004279", "source": "MADIN", "taxon_label": "mesorhizobium_muleiense", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1005048", "source": "MADIN", "taxon_label": "Collimonas fungivorans Ter331", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1005527", "source": "MADIN", "taxon_label": "Escherichia coli EC4421", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1005528", "source": "MADIN", "taxon_label": "Escherichia coli EC4422", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1005996", "source": "MADIN", "taxon_label": "Raoultella planticola ATCC 33531", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1006155", "source": "MADIN", "taxon_label": "listeria_weihenstephanensis", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1006551", "source": "MADIN", "taxon_label": "Klebsiella michiganensis KCTC 1686", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1007656", "source": "MADIN", "taxon_label": "Pseudomonas fluorescens Wayne1", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1009853", "source": "MADIN", "taxon_label": "Xanthomonas oryzae X11-5A", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1009854", "source": "MADIN", "taxon_label": "Xanthomonas oryzae X8-1A", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1010610", "source": "MADIN", "taxon_label": "methylobacterium_gnaphalii", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:101571", "source": "MADIN", "taxon_label": "burkholderia_ubonensis", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:102897", "source": "MADIN", "taxon_label": "Frankia sp. EUN1f", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1031711", "source": "MADIN", "taxon_label": "Ralstonia solanacearum Po82", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:103232", "source": "MADIN", "taxon_label": "streptomyces_ipomoeae", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1036778", "source": "MADIN", "taxon_label": "bosea_lathyri", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1036779", "source": "MADIN", "taxon_label": "bosea_lupini", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1036780", "source": "MADIN", "taxon_label": "bosea_robiniae", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1037911", "source": "MADIN", "taxon_label": "Pseudomonas fluorescens A506", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1038922", "source": "MADIN", "taxon_label": "Pseudomonas fluorescens Q2-87", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1038923", "source": "MADIN", "taxon_label": "Pseudomonas fluorescens Q8r1-96", "candidate_pool": 1206}], "causal_graphs": [{"graph_id": "plant_root_exudate_microbiome_assembly", "title": "Plant root exudate microbiome assembly", "description": "Root exudates, microbial substrate preferences, and plant immune signaling filter soil microbes into plant-associated root microbiomes that support plant-beneficial functions.", "nodes": [{"node_id": "plant_associated_environment", "label": "plant-associated environment", "node_type": "HABITAT", "grounding": "ENVO:01001001"}, {"node_id": "root_exudates", "label": "root exudates", "node_type": "CHEMICAL"}, {"node_id": "microbial_substrate_preferences", "label": "microbial substrate preferences", "node_type": "TRAIT"}, {"node_id": "salicylic_acid_signaling", "label": "salicylic acid signaling", "node_type": "BIOLOGICAL_PROCESS"}, {"node_id": "root_bacterial_colonization", "label": "root bacterial colonization", "node_type": "COMMUNITY_PROCESS"}, {"node_id": "rhizosphere_microbiome_assembly", "label": "rhizosphere microbiome assembly", "node_type": "COMMUNITY_PROCESS"}, {"node_id": "plant_beneficial_functions", "label": "plant-beneficial functions", "node_type": "BIOLOGICAL_PROCESS"}], "edges": [{"edge_id": "plant_roots_release_exudates", "subject": "plant_associated_environment", "predicate": "provides", "object": "root_exudates", "description": "Green plant roots release diverse exuded chemicals into plant-associated root environments.", "evidence": [{"reference": "DOI:10.1139/cjb-2013-0225", "snippet": "release a broad variety of chemical compounds", "notes": "Huang and colleagues summarize root exudates as plant-released chemical mixtures at the plant-root and rhizosphere interface."}]}, {"edge_id": "exudates_select_rhizosphere_microbes", "subject": "root_exudates", "predicate": "recruits", "object": "rhizosphere_microbiome_assembly", "description": "Root-exudate chemistry attracts and selects microorganisms in the rhizosphere.", "evidence": [{"reference": "DOI:10.1139/cjb-2013-0225", "snippet": "attract and select microorganisms in the rhizosphere", "notes": "Huang and colleagues review plant exudate compounds that mediate both plant-microbe and plant-microbiome interactions."}]}, {"edge_id": "substrate_traits_match_exudates", "subject": "microbial_substrate_preferences", "predicate": "responds to", "object": "root_exudates", "description": "Rhizosphere bacteria are filtered by the exuded substrates they can consume.", "evidence": [{"reference": "PMID:29556109", "snippet": "predicted and observed substrate preferences", "notes": "Zhalnina and colleagues compared rhizosphere bacterial growth responses with genome-predicted and measured substrate preferences."}]}, {"edge_id": "substrate_traits_drive_assembly", "subject": "microbial_substrate_preferences", "predicate": "drives", "object": "rhizosphere_microbiome_assembly", "description": "Microbial substrate-use traits help translate dynamic exudate chemistry into rhizosphere community-assembly patterns.", "evidence": [{"reference": "PMID:29556109", "snippet": "patterns in rhizosphere microbial community assembly", "notes": "Zhalnina and colleagues linked exudate chemistry and bacterial substrate preferences to observed rhizosphere community assembly."}]}, {"edge_id": "salicylic_acid_modulates_root_colonization", "subject": "salicylic_acid_signaling", "predicate": "modulates", "object": "root_bacterial_colonization", "description": "Plant immune signaling through salicylic acid modulates which bacterial taxa colonize roots.", "evidence": [{"reference": "PMID:26184915", "snippet": "colonization of the root microbiome", "notes": "Lebeis and colleagues measured Arabidopsis root communities and found specific bacterial-taxon responses to salicylic acid signaling."}]}, {"edge_id": "colonization_contributes_to_microbiome_assembly", "subject": "root_bacterial_colonization", "predicate": "contributes to", "object": "rhizosphere_microbiome_assembly", "description": "Host-filtered root colonization contributes to the assembled plant-associated root microbiome.", "evidence": [{"reference": "PMID:32788714", "snippet": "shape the assembly of plant-associated microbiomes", "notes": "Trivedi and colleagues review genetic, biochemical, physical, and metabolic interactions as drivers of plant microbiome assembly."}]}, {"edge_id": "assembly_modulates_plant_beneficial_functions", "subject": "rhizosphere_microbiome_assembly", "predicate": "modulates", "object": "plant_beneficial_functions", "description": "Assembled plant microbiomes modulate beneficial functions, including nutrient acquisition and plant health.", "evidence": [{"reference": "PMID:32788714", "snippet": "nutrient acquisition and plant health", "notes": "Trivedi and colleagues summarize how plant microbiome interactions influence beneficial traits."}]}]}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to ENVO:01001001 'plant-associated environment' (BROAD). Herbaceous plants, grasses and crops as hosts. ENVO:01001001 covers all plant-associated environments and so is broader than this specific host group. (source concept habitatmech:BACDIVE.d3209b6b2d)"}, {"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to ENVO:01001001 'plant-associated environment' (EXACT). GOLD's Host-associated &gt; Plants is exactly what ENVO:01001001 denotes. Unlike the animal clades there is a single matching term, so no conflation risk. (source concept habitatmech:GOLD.1b21002a97)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by BACDIVE, ENVIRONMENTS_TABLE, GOLD, MADIN. Grounding: EXACT."}, {"timestamp": "2026-09-04T00:00:00Z", "curator": "codex", "action": "ADD_CAUSAL_GRAPH", "changes": "Added a root-exudate microbiome-assembly graph backed by DOI:10.1139/cjb-2013-0225, PMID:29556109, PMID:26184915, and PMID:32788714.", "llm_assisted": true}, {"timestamp": "2026-10-09T00:00:00Z", "curator": "seed_from_sources", "action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained BacDive label 'Herbaceous-plants-Grass,Crops' as RELATED_SYNONYM: a BROAD source mapping does not establish exact lexical equivalence. Independent ontology synonyms and verbatim attestations are preserved (#1769)."}, {"timestamp": "2026-10-10T00:00:00Z", "curator": "seed_from_sources", "action": "SOURCE_ATTESTATION_CORRECTED", "changes": "Corrected bacdive.isolation_source:herbaceous-plants-grass,crops provenance wording to distinguish the declined automatic mapping from the final curator override (#1889)."}]} |
| ELEGACY | reports/yaml_record_review/20260922T151554Z-bryophytes.md; Findings and recommended edits; historical review lead | supports | The earlier major finding relied on CLASS/SEEDED status, a host label, an absent optional definition and zero counts. These are not independently a wrong habitat identity; the current source path, genus and positive primary host evidence support a qualified assessment without status promotion. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph; ENVO_01001000-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000; ENVO_01001000.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "ENVO:01001000", "label": "environmental system determined by an organism", "is_obsolete": false, "description": ["An environmental system which is determined by a living organism."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001/graph; ENVO_01001001-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001001", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001001", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33090", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001; ENVO_01001001.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "ENVO:01001001", "label": "plant-associated environment", "is_obsolete": false, "description": ["An environmental system determined by a green plant."]} |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Methylobacterium%20haplocladii%22&amp;format=json&amp;resultType=core&amp;pageSize=10; paper-bryophytes.json | context_only | Primary abstract PMID:23475343, DOI:10.1099/ijs.0.048215-0. Two named bacterial strains were isolated from Haplocladium microphyllum and Brachythecium plumosum. Supports bryophyte host plausibility without inventing a GOLD link. |
| ESEARCH | Maintained inputs and local structured archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.35beb98884 -e Bryophytes -e bryophytes -e habitatmech:GOLD.35beb98884 curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately. No formal target predecessor was found; not every broad label match was inspected. |

## Limits And Additional Notes

- Original specimens and every pair-level source citation have not been independently reidentified. Source counts and ranks are not prevalence, viability, or characteristic presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities were separately checked against current NCBI Taxonomy, not certified by that label gate.
- Full QC evidence is a successful remote run at the exact unchanged scientific input base, not a new local full-QC execution. New review files require a post-save native archive check.
- iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic module or causal mechanism is asserted. No paid research was used.
- Current input hashes were checked against both working bytes and exact tracked base blobs; source.state git_commit explicitly describes that revision.
- Ignored-inclusive searches and the parsed structured archive found no previous structured observation targeting this identifier. Broad label matches are leads, not formal lineage or automatic scientific findings.
- Read-only scientific review: no habitat curation, generation, history/status promotion or GitHub mutation is performed.
- The earlier major finding relied on CLASS/SEEDED status, a host label, an absent optional definition and zero counts. These are not independently a wrong habitat identity; the current source path, genus and positive primary host evidence support a qualified assessment without status promotion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T193009Z-bryophytes-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Bryophytes (habitatmech:GOLD.35beb98884)'
started_at: '2026-10-15T19:05:01Z'
finished_at: '2026-10-15T19:30:09Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the record and sources; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The exact Host-associated > Plants > Bryophytes source denotes bryophytes
  acting as microbial hosts, consistently under a green-plant-associated environment.
  Primary isolation of bacteria from two named bryophytes supports that interpretation,
  not a specific GOLD observation. The zero tree count, CLASS/SEEDED status and absent
  optional definition do not independently establish a defect. No taxon identity is
  substituted for the minted environment.
source:
  git_revision: a073f8e821a7c095f35501982930cc5a156835c0
  state: git_commit
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
    sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 196d393819145d33f30f7706fd9c5369ed05847d2ccbd9b977a759556ca293fd
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 9344f0bbbad1423ff0e47204ad49bc27ffaf4b5e63841e77e09cc01877b91f54
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: da5dcc7d49a3441bd9ff25d95ff204ba4e8716cf062271338ee2795ca16a5ce4
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: a2a0496837ea75e487d7fc5d35317a890262a941d8fffe9babcd39f2f332c6db
    role: context
  - path: data/habitats/host_associated/bryophytes.yaml
    sha256: 1824dccd4cb9689fcdd6cadb71ebf018d950f0ea7195ffb013ec863bdf6d3b90
    role: target
  - path: data/habitats/host_associated/plant_associated_environment.yaml
    sha256: b7b5c939eb016f76a6d8ace89e0886690459d4d800d555dcd995a011b3f3172f
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
  - path: reports/yaml_record_review/20260922T151554Z-bryophytes.md
    sha256: eeb3cf7bece3bc8ca32b9d9f580cead7753d8113e2cda65acfab08307dcb5190
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
targets:
- target_id: habitatmech:GOLD.35beb98884
  path: data/habitats/host_associated/bryophytes.yaml
  label: Bryophytes
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
  description: Full field-by-field scientific assessment of this exact target at a073f8e821a7c095f35501982930cc5a156835c0.
  selection: One of the next 24 path-ordered unreviewed identifiers in an ignored-inclusive
    3208-record census. This bundle reviews one identifier, not a sample standing
    for other targets.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.35beb98884
  exclusions:
  - target: Other habitats and SSSOM/KGX products
    reason: Parent context is not additional record coverage. Export conformance and
      original individual specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bryophytes.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.35beb98884
  summary: "Finished 2026-10-15T19:08:53Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bryophytes.yaml"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml
    data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml
    data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml
    data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml
    data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml
    data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml
    data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml
    data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml
    data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml
    data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml
    data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml
    data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.35beb98884
  summary: "Finished 2026-10-15T19:10:07Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml\
    \ data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml\
    \ data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml\
    \ data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml\
    \ data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml\
    \ data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml\
    \ data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml\
    \ data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml\
    \ data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml\
    \ data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml\
    \ data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml\
    \ data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.35beb98884
  summary: 'Finished 2026-10-15T19:10:18Z. No issues found

    816 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.35beb98884
  summary: "Finished 2026-10-15T19:10:19Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.35beb98884
  summary: "Finished 2026-10-15T19:10:38Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.35beb98884
  summary: "Finished 2026-10-15T19:10:44Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.35beb98884
  summary: "Finished 2026-10-15T19:11:04Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.35beb98884
  summary: "Finished 2026-10-15T19:12:07Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: CCI
  name: Exact-baseline full QC
  status: passed
  required: true
  command: gh run view 38786529592 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.35beb98884
  summary: Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592
  scope_note: Unchanged scientific input baseline; these new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bryophytes.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: All fields, displayed taxa and complete curation history read.
  snapshot_sha256: 1824dccd4cb9689fcdd6cadb71ebf018d950f0ea7195ffb013ec863bdf6d3b90
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, hierarchy and source-evidence rules
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: All parent contributions must be strictly broader; host identity is not
    environment identity. Source occurrences are not automatically characteristic.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation and category enums
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: Source-to-record mapping endpoints; reported associations versus characteristic
    assertions; category scope and optional fields.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed resolution routes, parent accumulation, prefix category and overrides
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: 'Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:GOLD.35beb98884",
    "automatic": {"identifier": "habitatmech:GOLD.35beb98884", "grounding_status":
    "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": [], "route": "gold_unmatched", "category": null, "reviewed":
    false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.35beb98884",
    "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_unmatched",
    "category": null, "reviewed": false, "decision": {"identifier": "habitatmech:GOLD.35beb98884",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep
    (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS",
    "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Inventory projection
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: Counts/units and taxon ranks/scores preserve source meanings. PREGO projections
    omit original pair-level citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 2497
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: '[{"row": 2497, "data": {"canonical_path": "Host-associated > Plants >
    Bryophytes", "ecosystem": "Host-associated", "ecosystem_category": "Plants", "ecosystem_type":
    "Bryophytes", "ecosystem_subtype": "", "specific_ecosystem": "", "leaf_label":
    "Bryophytes", "depth": "3", "gold_node_count": "3", "organism_count": "0", "study_count":
    "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:8107|gold.ecosystem:8108|gold.ecosystem:8109"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 6796
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: '[{"row": 6796, "data": {"subject": "ENVO:01001001", "predicate": "rdfs:subClassOf",
    "object": "ENVO:01001000"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 8490
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: '[{"row": 8490, "data": {"term_id": "ENVO:01001001", "ontology": "ENVO",
    "label": "plant-associated environment", "definition": "An environmental system
    determined by a green plant.", "synonyms": "Viridiplantae-associated environment|plant
    environment", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET8
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 401
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: '[{"row": 401, "data": {"identifier": "habitatmech:GOLD.35beb98884", "decision":
    "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep
    (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS",
    "category": "", "relation": ""}}]'
  snapshot_sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/plant_associated_environment.yaml
  locator: Entire immediate parent record; context only
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: '{"identifier": "ENVO:01001001", "label": "plant-associated environment",
    "definition": "An environmental system determined by a green plant.", "definition_source":
    "ENVO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status":
    "SEEDED", "synonyms": [{"synonym_text": "Herbaceous-plants-Grass,Crops", "synonym_type":
    "RELATED_SYNONYM", "source": "BacDive"}, {"synonym_text": "Plants", "synonym_type":
    "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "Viridiplantae-associated
    environment", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"}, {"synonym_text":
    "plant environment", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"}], "parent_habitats":
    ["ENVO:01001000"], "source_attestations": [{"source": "BACDIVE", "source_id":
    "bacdive.isolation_source:herbaceous-plants-grass,crops", "source_label": "Herbaceous-plants-Grass,Crops",
    "mapping_predicate": "skos:broadMatch", "assertion_count": 2451, "assertion_unit":
    "STRAIN", "notes": "kg-microbe''s isolation-source mapping table has no ontology
    target for this source; the automatic route leaves it ungrounded. The explicit
    curator decision GROUND overrides that route; this source is emitted on ENVO:01001001."},
    {"source": "ENVIRONMENTS_TABLE", "source_id": "host_plant", "source_label": "host_plant",
    "notes": "Physicochemical parameter bands from kg-microbe''s environment table."},
    {"source": "GOLD", "source_id": "gold.ecosystem:3385", "source_label": "Plants",
    "source_path": "Host-associated > Plants", "mapping_predicate": "skos:exactMatch",
    "assertion_count": 12638, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem
    node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."},
    {"source": "MADIN", "source_id": "ENVO:01001001", "source_label": "plant-associated
    environment", "assertion_count": 1206, "assertion_unit": "TAXON"}], "environmental_parameters":
    [{"parameter": "GRADIENTS", "qualitative_value": "high", "source": "kg-microbe
    environments.csv (host_plant)"}, {"parameter": "PRESSURE", "qualitative_value":
    "low", "source": "kg-microbe environments.csv (host_plant)"}, {"parameter": "SALINITY_VARIABILITY",
    "qualitative_value": "small", "source": "kg-microbe environments.csv (host_plant)"}],
    "characteristic_taxa": [{"taxon_id": "NCBITaxon:28214", "source": "BACDIVE", "taxon_label":
    "Sphingomonas sp.", "association_count": 46, "rank": 1, "candidate_pool": 1394},
    {"taxon_id": "NCBITaxon:409", "source": "BACDIVE", "taxon_label": "Methylobacterium
    sp.", "association_count": 43, "rank": 2, "candidate_pool": 1394}, {"taxon_id":
    "NCBITaxon:339", "source": "BACDIVE", "taxon_label": "Xanthomonas campestris",
    "association_count": 39, "rank": 3, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:56",
    "source": "BACDIVE", "taxon_label": "Sorangium cellulosum", "association_count":
    39, "rank": 4, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:54", "source":
    "BACDIVE", "taxon_label": "Nannocystis exedens", "association_count": 35, "rank":
    5, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:184914", "source": "BACDIVE",
    "taxon_label": "Corallococcus coralloides", "association_count": 33, "rank": 6,
    "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:317", "source": "BACDIVE", "taxon_label":
    "Pseudomonas syringae", "association_count": 33, "rank": 7, "candidate_pool":
    1394}, {"taxon_id": "NCBITaxon:391", "source": "BACDIVE", "taxon_label": "Rhizobium
    sp.", "association_count": 30, "rank": 8, "candidate_pool": 1394}, {"taxon_id":
    "NCBITaxon:554", "source": "BACDIVE", "taxon_label": "Pectobacterium carotovorum",
    "association_count": 30, "rank": 9, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:306",
    "source": "BACDIVE", "taxon_label": "Pseudomonas sp.", "association_count": 26,
    "rank": 10, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:305", "source": "BACDIVE",
    "taxon_label": "Ralstonia solanacearum", "association_count": 22, "rank": 11,
    "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1930", "source": "BACDIVE", "taxon_label":
    "Streptomyces scabiei", "association_count": 20, "rank": 12, "candidate_pool":
    1394}, {"taxon_id": "NCBITaxon:1931", "source": "BACDIVE", "taxon_label": "Streptomyces
    sp.", "association_count": 20, "rank": 13, "candidate_pool": 1394}, {"taxon_id":
    "NCBITaxon:83428", "source": "BACDIVE", "taxon_label": "uncultured Bacillus sp.",
    "association_count": 19, "rank": 14, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:51671",
    "source": "BACDIVE", "taxon_label": "Microbacterium sp.", "association_count":
    18, "rank": 15, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1405", "source":
    "BACDIVE", "taxon_label": "Bacillus mycoides", "association_count": 15, "rank":
    16, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:2161", "source": "BACDIVE",
    "taxon_label": "Methanobacterium bryantii", "association_count": 15, "rank": 17,
    "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:35761", "source": "BACDIVE",
    "taxon_label": "Nocardioides sp.", "association_count": 15, "rank": 18, "candidate_pool":
    1394}, {"taxon_id": "NCBITaxon:58172", "source": "BACDIVE", "taxon_label": "Paenibacillus
    sp.", "association_count": 14, "rank": 19, "candidate_pool": 1394}, {"taxon_id":
    "NCBITaxon:1872086", "source": "BACDIVE", "taxon_label": "Ensifer sp.", "association_count":
    13, "rank": 20, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1428", "source":
    "BACDIVE", "taxon_label": "Bacillus thuringiensis", "association_count": 12, "rank":
    21, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1872122", "source": "BACDIVE",
    "taxon_label": "Acidovorax sp.", "association_count": 12, "rank": 22, "candidate_pool":
    1394}, {"taxon_id": "NCBITaxon:2035", "source": "BACDIVE", "taxon_label": "Curtobacterium
    flaccumfaciens", "association_count": 11, "rank": 23, "candidate_pool": 1394},
    {"taxon_id": "NCBITaxon:1411316", "source": "BACDIVE", "taxon_label": "Pedobacter
    sp.", "association_count": 10, "rank": 24, "candidate_pool": 1394}, {"taxon_id":
    "NCBITaxon:1871063", "source": "BACDIVE", "taxon_label": "Aeromicrobium sp.",
    "association_count": 10, "rank": 25, "candidate_pool": 1394}, {"taxon_id": "NCBITaxon:1002809",
    "source": "MADIN", "taxon_label": "Solibacillus silvestris StLB046", "candidate_pool":
    1206}, {"taxon_id": "NCBITaxon:1003091", "source": "MADIN", "taxon_label": "methylobacterium_thuringiense",
    "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1003092", "source": "MADIN",
    "taxon_label": "Methylobacterium trifolii", "candidate_pool": 1206}, {"taxon_id":
    "NCBITaxon:1003237", "source": "MADIN", "taxon_label": "Nitrospirillum amazonense
    Y2", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1004279", "source": "MADIN",
    "taxon_label": "mesorhizobium_muleiense", "candidate_pool": 1206}, {"taxon_id":
    "NCBITaxon:1005048", "source": "MADIN", "taxon_label": "Collimonas fungivorans
    Ter331", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1005527", "source":
    "MADIN", "taxon_label": "Escherichia coli EC4421", "candidate_pool": 1206}, {"taxon_id":
    "NCBITaxon:1005528", "source": "MADIN", "taxon_label": "Escherichia coli EC4422",
    "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1005996", "source": "MADIN",
    "taxon_label": "Raoultella planticola ATCC 33531", "candidate_pool": 1206}, {"taxon_id":
    "NCBITaxon:1006155", "source": "MADIN", "taxon_label": "listeria_weihenstephanensis",
    "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1006551", "source": "MADIN",
    "taxon_label": "Klebsiella michiganensis KCTC 1686", "candidate_pool": 1206},
    {"taxon_id": "NCBITaxon:1007656", "source": "MADIN", "taxon_label": "Pseudomonas
    fluorescens Wayne1", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1009853",
    "source": "MADIN", "taxon_label": "Xanthomonas oryzae X11-5A", "candidate_pool":
    1206}, {"taxon_id": "NCBITaxon:1009854", "source": "MADIN", "taxon_label": "Xanthomonas
    oryzae X8-1A", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1010610", "source":
    "MADIN", "taxon_label": "methylobacterium_gnaphalii", "candidate_pool": 1206},
    {"taxon_id": "NCBITaxon:101571", "source": "MADIN", "taxon_label": "burkholderia_ubonensis",
    "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:102897", "source": "MADIN", "taxon_label":
    "Frankia sp. EUN1f", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1031711",
    "source": "MADIN", "taxon_label": "Ralstonia solanacearum Po82", "candidate_pool":
    1206}, {"taxon_id": "NCBITaxon:103232", "source": "MADIN", "taxon_label": "streptomyces_ipomoeae",
    "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1036778", "source": "MADIN",
    "taxon_label": "bosea_lathyri", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1036779",
    "source": "MADIN", "taxon_label": "bosea_lupini", "candidate_pool": 1206}, {"taxon_id":
    "NCBITaxon:1036780", "source": "MADIN", "taxon_label": "bosea_robiniae", "candidate_pool":
    1206}, {"taxon_id": "NCBITaxon:1037911", "source": "MADIN", "taxon_label": "Pseudomonas
    fluorescens A506", "candidate_pool": 1206}, {"taxon_id": "NCBITaxon:1038922",
    "source": "MADIN", "taxon_label": "Pseudomonas fluorescens Q2-87", "candidate_pool":
    1206}, {"taxon_id": "NCBITaxon:1038923", "source": "MADIN", "taxon_label": "Pseudomonas
    fluorescens Q8r1-96", "candidate_pool": 1206}], "causal_graphs": [{"graph_id":
    "plant_root_exudate_microbiome_assembly", "title": "Plant root exudate microbiome
    assembly", "description": "Root exudates, microbial substrate preferences, and
    plant immune signaling filter soil microbes into plant-associated root microbiomes
    that support plant-beneficial functions.", "nodes": [{"node_id": "plant_associated_environment",
    "label": "plant-associated environment", "node_type": "HABITAT", "grounding":
    "ENVO:01001001"}, {"node_id": "root_exudates", "label": "root exudates", "node_type":
    "CHEMICAL"}, {"node_id": "microbial_substrate_preferences", "label": "microbial
    substrate preferences", "node_type": "TRAIT"}, {"node_id": "salicylic_acid_signaling",
    "label": "salicylic acid signaling", "node_type": "BIOLOGICAL_PROCESS"}, {"node_id":
    "root_bacterial_colonization", "label": "root bacterial colonization", "node_type":
    "COMMUNITY_PROCESS"}, {"node_id": "rhizosphere_microbiome_assembly", "label":
    "rhizosphere microbiome assembly", "node_type": "COMMUNITY_PROCESS"}, {"node_id":
    "plant_beneficial_functions", "label": "plant-beneficial functions", "node_type":
    "BIOLOGICAL_PROCESS"}], "edges": [{"edge_id": "plant_roots_release_exudates",
    "subject": "plant_associated_environment", "predicate": "provides", "object":
    "root_exudates", "description": "Green plant roots release diverse exuded chemicals
    into plant-associated root environments.", "evidence": [{"reference": "DOI:10.1139/cjb-2013-0225",
    "snippet": "release a broad variety of chemical compounds", "notes": "Huang and
    colleagues summarize root exudates as plant-released chemical mixtures at the
    plant-root and rhizosphere interface."}]}, {"edge_id": "exudates_select_rhizosphere_microbes",
    "subject": "root_exudates", "predicate": "recruits", "object": "rhizosphere_microbiome_assembly",
    "description": "Root-exudate chemistry attracts and selects microorganisms in
    the rhizosphere.", "evidence": [{"reference": "DOI:10.1139/cjb-2013-0225", "snippet":
    "attract and select microorganisms in the rhizosphere", "notes": "Huang and colleagues
    review plant exudate compounds that mediate both plant-microbe and plant-microbiome
    interactions."}]}, {"edge_id": "substrate_traits_match_exudates", "subject": "microbial_substrate_preferences",
    "predicate": "responds to", "object": "root_exudates", "description": "Rhizosphere
    bacteria are filtered by the exuded substrates they can consume.", "evidence":
    [{"reference": "PMID:29556109", "snippet": "predicted and observed substrate preferences",
    "notes": "Zhalnina and colleagues compared rhizosphere bacterial growth responses
    with genome-predicted and measured substrate preferences."}]}, {"edge_id": "substrate_traits_drive_assembly",
    "subject": "microbial_substrate_preferences", "predicate": "drives", "object":
    "rhizosphere_microbiome_assembly", "description": "Microbial substrate-use traits
    help translate dynamic exudate chemistry into rhizosphere community-assembly patterns.",
    "evidence": [{"reference": "PMID:29556109", "snippet": "patterns in rhizosphere
    microbial community assembly", "notes": "Zhalnina and colleagues linked exudate
    chemistry and bacterial substrate preferences to observed rhizosphere community
    assembly."}]}, {"edge_id": "salicylic_acid_modulates_root_colonization", "subject":
    "salicylic_acid_signaling", "predicate": "modulates", "object": "root_bacterial_colonization",
    "description": "Plant immune signaling through salicylic acid modulates which
    bacterial taxa colonize roots.", "evidence": [{"reference": "PMID:26184915", "snippet":
    "colonization of the root microbiome", "notes": "Lebeis and colleagues measured
    Arabidopsis root communities and found specific bacterial-taxon responses to salicylic
    acid signaling."}]}, {"edge_id": "colonization_contributes_to_microbiome_assembly",
    "subject": "root_bacterial_colonization", "predicate": "contributes to", "object":
    "rhizosphere_microbiome_assembly", "description": "Host-filtered root colonization
    contributes to the assembled plant-associated root microbiome.", "evidence": [{"reference":
    "PMID:32788714", "snippet": "shape the assembly of plant-associated microbiomes",
    "notes": "Trivedi and colleagues review genetic, biochemical, physical, and metabolic
    interactions as drivers of plant microbiome assembly."}]}, {"edge_id": "assembly_modulates_plant_beneficial_functions",
    "subject": "rhizosphere_microbiome_assembly", "predicate": "modulates", "object":
    "plant_beneficial_functions", "description": "Assembled plant microbiomes modulate
    beneficial functions, including nutrient acquisition and plant health.", "evidence":
    [{"reference": "PMID:32788714", "snippet": "nutrient acquisition and plant health",
    "notes": "Trivedi and colleagues summarize how plant microbiome interactions influence
    beneficial traits."}]}]}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z",
    "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to ENVO:01001001
    ''plant-associated environment'' (BROAD). Herbaceous plants, grasses and crops
    as hosts. ENVO:01001001 covers all plant-associated environments and so is broader
    than this specific host group. (source concept habitatmech:BACDIVE.d3209b6b2d)"},
    {"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND",
    "changes": "Grounded to ENVO:01001001 ''plant-associated environment'' (EXACT).
    GOLD''s Host-associated > Plants is exactly what ENVO:01001001 denotes. Unlike
    the animal clades there is a single matching term, so no conflation risk. (source
    concept habitatmech:GOLD.1b21002a97)"}, {"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by BACDIVE, ENVIRONMENTS_TABLE, GOLD, MADIN.
    Grounding: EXACT."}, {"timestamp": "2026-09-04T00:00:00Z", "curator": "codex",
    "action": "ADD_CAUSAL_GRAPH", "changes": "Added a root-exudate microbiome-assembly
    graph backed by DOI:10.1139/cjb-2013-0225, PMID:29556109, PMID:26184915, and PMID:32788714.",
    "llm_assisted": true}, {"timestamp": "2026-10-09T00:00:00Z", "curator": "seed_from_sources",
    "action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained BacDive label ''Herbaceous-plants-Grass,Crops''
    as RELATED_SYNONYM: a BROAD source mapping does not establish exact lexical equivalence.
    Independent ontology synonyms and verbatim attestations are preserved (#1769)."},
    {"timestamp": "2026-10-10T00:00:00Z", "curator": "seed_from_sources", "action":
    "SOURCE_ATTESTATION_CORRECTED", "changes": "Corrected bacdive.isolation_source:herbaceous-plants-grass,crops
    provenance wording to distinguish the declined automatic mapping from the final
    curator override (#1889)."}]}'
  snapshot_sha256: b7b5c939eb016f76a6d8ace89e0886690459d4d800d555dcd995a011b3f3172f
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20260922T151554Z-bryophytes.md
  locator: Findings and recommended edits; historical review lead
  accessed_at: '2026-10-15T19:30:08Z'
  support: supports
  summary: The earlier major finding relied on CLASS/SEEDED status, a host label,
    an absent optional definition and zero counts. These are not independently a wrong
    habitat identity; the current source path, genus and positive primary host evidence
    support a qualified assessment without status promotion.
  snapshot_sha256: eeb3cf7bece3bc8ca32b9d9f580cead7753d8113e2cda65acfab08307dcb5190
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph
  locator: ENVO_01001000-graph.json
  accessed_at: '2026-10-15T19:06:11Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: e11b34dbd0a626083d5d0bbbb364469ef95831fb61cb81da5377d59715b272ca
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000
  locator: ENVO_01001000.json
  accessed_at: '2026-10-15T19:06:11Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "ENVO:01001000", "label": "environmental system determined by an organism", "is_obsolete":
    false, "description": ["An environmental system which is determined by a living
    organism."]}'
  snapshot_sha256: 8bd797929d18bf28171af7fd10f358db9b093f752d20b99f665779bb2e6b504e
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001/graph
  locator: ENVO_01001001-graph.json
  accessed_at: '2026-10-15T19:06:13Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001001",
    "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001001",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_33090", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 43b7f7cee8e27c64685cea0193012a2cc71851b91d19a2a7052fa1e6548a6a71
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001
  locator: ENVO_01001001.json
  accessed_at: '2026-10-15T19:06:12Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "ENVO:01001001", "label": "plant-associated environment", "is_obsolete": false,
    "description": ["An environmental system determined by a green plant."]}'
  snapshot_sha256: b1623e2f33257c2fadc5bf06670bcc7e95384c210301e901f7faa8059c5ed815
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22Methylobacterium%20haplocladii%22&format=json&resultType=core&pageSize=10
  locator: paper-bryophytes.json
  accessed_at: '2026-10-15T19:19:10Z'
  support: context_only
  summary: Primary abstract PMID:23475343, DOI:10.1099/ijs.0.048215-0. Two named bacterial
    strains were isolated from Haplocladium microphyllum and Brachythecium plumosum.
    Supports bryophyte host plausibility without inventing a GOLD link.
  snapshot_sha256: 7f0eab72ff537ad1c28d2af1fbb238d2d06659391296d682d89da8375abd634b
- evidence_id: ESEARCH
  kind: search
  reference: Maintained inputs and local structured archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.35beb98884 -e Bryophytes
    -e bryophytes -e habitatmech:GOLD.35beb98884 curation history research reports
    data/raw build reviews
  accessed_at: '2026-10-15T19:05:55Z'
  support: context_only
  summary: Exact source/curation rows were parsed separately. No formal target predecessor
    was found; not every broad label match was inspected.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    ignored and hidden files included; every structured review.yaml was parsed.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, category and broader ancestry
  outcome: supported
  summary: The exact Host-associated > Plants > Bryophytes source denotes bryophytes
    acting as microbial hosts, consistently under a green-plant-associated environment.
    Primary isolation of bacteria from two named bryophytes supports that interpretation,
    not a specific GOLD observation. The zero tree count, CLASS/SEEDED status and
    absent optional definition do not independently establish a defect. No taxon identity
    is substituted for the minted environment.
  target_ids:
  - habitatmech:GOLD.35beb98884
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  dimensions:
  - name: native_status
    value: UNGROUNDED/SEEDED
    definition: Generated grounding and curation status; distinct from this scientific
      review verdict.
    evidence_ids:
    - E1
    - ESEED
- assessment_id: A2
  area: quantity
  topic: Source counts, units, ranks, pools and channels
  outcome: supported
  summary: 'Every attestation and displayed taxon was compared with its exact frozen
    source row. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Side-table biosamples
    and study memberships are separate from tree ORGANISM counts; zero-count omission
    is not biological absence.'
  target_ids:
  - habitatmech:GOLD.35beb98884
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  dimensions:
  - name: source_assertion_units
    value: '[{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]'
    definition: Frozen source counts with their noninterchangeable units; omitted
      zero GOLD counts are verified in the raw row.
    evidence_ids:
    - E1
    - EEXTRACT
    - ESEED
- assessment_id: A3
  area: evidence
  topic: Biological support and limits
  outcome: supported
  summary: The exact Host-associated > Plants > Bryophytes source denotes bryophytes
    acting as microbial hosts, consistently under a green-plant-associated environment.
    Primary isolation of bacteria from two named bryophytes supports that interpretation,
    not a specific GOLD observation. The zero tree count, CLASS/SEEDED status and
    absent optional definition do not independently establish a defect. No taxon identity
    is substituted for the minted environment.
  target_ids:
  - habitatmech:GOLD.35beb98884
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
- assessment_id: A4
  area: completeness
  topic: Curation status, parameters, mechanisms and optional content
  outcome: supported
  summary: Executed routes reproduce UNGROUNDED/SEEDED. No target environmental parameters,
    causal edges, discussions/datasets or is_characteristic=true assertions are present.
    Parent-record mechanisms are not inherited. Optional absence and SEEDED status
    alone are not defects.
  target_ids:
  - habitatmech:GOLD.35beb98884
  evidence_ids:
  - E1
  - ERULE
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native deterministic gates
  outcome: supported
  summary: Ordinary and strict schema, 816 curation histories, provenance, exact 3208-record
    reproduction, 32 causal overlays, term requests, configured labels and exact-base
    QC passed. Deterministic fidelity does not establish biological correctness.
  target_ids:
  - habitatmech:GOLD.35beb98884
  evidence_ids:
  - E1
  - ERULE
findings: []
actions: []
limitations:
- Original specimens and every pair-level source citation have not been independently
  reidentified. Source counts and ranks are not prevalence, viability, or characteristic
  presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities
  were separately checked against current NCBI Taxonomy, not certified by that label
  gate.
- Full QC evidence is a successful remote run at the exact unchanged scientific input
  base, not a new local full-QC execution. New review files require a post-save native
  archive check.
- 'iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic
  module or causal mechanism is asserted. No paid research was used.'
notes:
- Current input hashes were checked against both working bytes and exact tracked base
  blobs; source.state git_commit explicitly describes that revision.
- Ignored-inclusive searches and the parsed structured archive found no previous structured
  observation targeting this identifier. Broad label matches are leads, not formal
  lineage or automatic scientific findings.
- 'Read-only scientific review: no habitat curation, generation, history/status promotion
  or GitHub mutation is performed.'
- The earlier major finding relied on CLASS/SEEDED status, a host label, an absent
  optional definition and zero counts. These are not independently a wrong habitat
  identity; the current source path, genus and positive primary host evidence support
  a qualified assessment without status promotion.
tags:
- individual-scientific-review
- host-associated
```
