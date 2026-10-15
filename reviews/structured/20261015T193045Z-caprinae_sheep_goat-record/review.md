# Record review: caprine-associated environment (habitatmech:BACDIVE.4d3086a839)

- Review: 20261015T193045Z-caprinae_sheep_goat-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T19:06:40Z
- Finished UTC: 2026-10-15T19:30:45Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The minted sheep-or-goat-associated environment and animal-associated genus are coherent; the goat-only FOODON xref does not assert identity or exclude sheep. The exact synonym Caprinae-Sheep/Goat names hosts, not an environmental system. The 412 STRAIN assertions and 25 displayed taxa from 137 candidates reproduce their sources. Primary Moraxella caprae isolation supports a goat-host witness, not all rows; a dung-baiting explanation for the myxobacterial block remains an unverified research inference.

## Scope And Provenance

Full field-by-field scientific assessment of this exact target at a073f8e821a7c095f35501982930cc5a156835c0.

Selection: One of the next 24 path-ordered unreviewed identifiers in an ignored-inclusive 3208-record census. This bundle reviews one identifier, not a sample standing for other targets.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base a073f8e821a7c095f35501982930cc5a156835c0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.4d3086a839 | data/habitats/host_associated/caprinae_sheep_goat.yaml | generated | caprine-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:BACDIVE.4d3086a839 | Finished 2026-10-15T19:09:51Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/caprinae_sheep_goat.yaml |
| validate-strict | passed | True | habitatmech:BACDIVE.4d3086a839 | Finished 2026-10-15T19:10:07Z. uv run python scripts/validate_strict.py data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:BACDIVE.4d3086a839 | Finished 2026-10-15T19:10:18Z. No issues found<br>816 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:BACDIVE.4d3086a839 | Finished 2026-10-15T19:10:19Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:BACDIVE.4d3086a839 | Finished 2026-10-15T19:10:38Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:BACDIVE.4d3086a839 | Finished 2026-10-15T19:10:44Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:BACDIVE.4d3086a839 | Finished 2026-10-15T19:11:04Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:BACDIVE.4d3086a839 | Finished 2026-10-15T19:12:07Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | habitatmech:BACDIVE.4d3086a839 | Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592 |

## Scientific And Domain Assessments

### Identity, definition, category and broader ancestry

identity: concern. Targets: habitatmech:BACDIVE.4d3086a839.

The minted sheep-or-goat-associated environment and animal-associated genus are coherent; the goat-only FOODON xref does not assert identity or exclude sheep. The exact synonym Caprinae-Sheep/Goat names hosts, not an environmental system. The 412 STRAIN assertions and 25 displayed taxa from 137 candidates reproduce their sources. Primary Moraxella caprae isolation supports a goat-host witness, not all rows; a dung-baiting explanation for the myxobacterial block remains an unverified research inference.

### Source counts, units, ranks, pools and channels

quantity: supported. Targets: habitatmech:BACDIVE.4d3086a839.

Every attestation and displayed taxon was compared with its exact frozen source row. [{"source": "BACDIVE", "count": 412, "unit": "STRAIN"}]. Side-table biosamples and study memberships are separate from tree ORGANISM counts; zero-count omission is not biological absence.

### Biological support and limits

evidence: supported. Targets: habitatmech:BACDIVE.4d3086a839.

The minted sheep-or-goat-associated environment and animal-associated genus are coherent; the goat-only FOODON xref does not assert identity or exclude sheep. The exact synonym Caprinae-Sheep/Goat names hosts, not an environmental system. The 412 STRAIN assertions and 25 displayed taxa from 137 candidates reproduce their sources. Primary Moraxella caprae isolation supports a goat-host witness, not all rows; a dung-baiting explanation for the myxobacterial block remains an unverified research inference.

### Curation status, parameters, mechanisms and optional content

completeness: supported. Targets: habitatmech:BACDIVE.4d3086a839.

Executed routes reproduce UNGROUNDED/REVIEWED. No target environmental parameters, causal edges, discussions/datasets or is_characteristic=true assertions are present. Parent-record mechanisms are not inherited. Optional absence and SEEDED status alone are not defects.

### Native deterministic gates

schema: supported. Targets: habitatmech:BACDIVE.4d3086a839.

Ordinary and strict schema, 816 curation histories, provenance, exact 3208-record reproduction, 32 causal overlays, term requests, configured labels and exact-base QC passed. Deterministic fidelity does not establish biological correctness.

## Findings

### F1: Whole-host label is an exact environment synonym

major / open / confirmed; issue key: caprinae-sheep-goat-host-alias.

Remove authored exact synonym Caprinae-Sheep/Goat and guard definition-source-label fallback from reintroducing it. Preserve the verbatim source attestation, minted habitat identity, supported definition and host xrefs.

## Recommended Actions And Acceptance Checks

### ACT1

Remove authored exact synonym Caprinae-Sheep/Goat and guard definition-source-label fallback from reintroducing it. Preserve the verbatim source attestation, minted habitat identity, supported definition and host xrefs. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identities, source totals/units and raw provenance. Change mapping or native status only when separately supported by the item assessment; never alter source counts by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/caprinae_sheep_goat.yaml; Entire target YAML | supports | All fields, displayed taxa and complete curation history read. |
| ERULE | docs/CURATION.md; Identity, hierarchy and source-evidence rules | supports | All parent contributions must be strictly broader; host identity is not environment identity. Source occurrences are not automatically characteristic. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation and category enums | supports | Source-to-record mapping endpoints; reported associations versus characteristic assertions; category scope and optional fields. |
| ESEED | src/habitatmech/seed.py; Executed resolution routes, parent accumulation, prefix category and overrides | supports | Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:BACDIVE.4d3086a839", "automatic": {"identifier": "FOODON:03411328", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "bacdive_mapping_table", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:BACDIVE.4d3086a839", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": ["FOODON:03411328"], "route": "curated_confirm_ungrounded_from_bacdive_mapping_table", "category": "HOST_ASSOCIATED", "reviewed": true, "decision": {"identifier": "habitatmech:BACDIVE.4d3086a839", "decision": "CONFIRM_UNGROUNDED", "object_id": "FOODON:03411328", "object_label": "goat", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it \u2014 the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an &lt;X&gt;-associated environment. Host-associated &gt; Porifera was NOT_APPLICABLE while its own child Porifera &gt; Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. Category set to HOST_ASSOCIATED (#200): the row already claims ENVO:01001002 'animal-associated environment' as the nearest broader term, which is the claim that a living animal host defines the habitat, and every other record carrying that parent is HOST_ASSOCIATED. The category column was left blank here, so the seeder's default stood and five domestic-mammal hosts stayed in OTHER while their siblings did not. The reasoning above is unchanged.", "review_depth": "ITEM", "category": "HOST_ASSOCIATED", "relation": "xref"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Inventory projection | supports | Counts/units and taxon ranks/scores preserve source meanings. PREGO projections omit original pair-level citation links. |
| ET5 | data/raw/bacdive_source_taxa.tsv; Physical TSV rows 440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464 | supports | [{"row": 440, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "1", "taxon_id": "NCBITaxon:184914", "taxon_label": "Corallococcus coralloides", "strain_count": "40", "corroborated_by": ""}}, {"row": 441, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "2", "taxon_id": "NCBITaxon:33", "taxon_label": "Myxococcus fulvus", "strain_count": "29", "corroborated_by": ""}}, {"row": 442, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "3", "taxon_id": "NCBITaxon:54", "taxon_label": "Nannocystis exedens", "strain_count": "27", "corroborated_by": ""}}, {"row": 443, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "4", "taxon_id": "NCBITaxon:56", "taxon_label": "Sorangium cellulosum", "strain_count": "24", "corroborated_by": ""}}, {"row": 444, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "5", "taxon_id": "NCBITaxon:34", "taxon_label": "Myxococcus xanthus", "strain_count": "18", "corroborated_by": ""}}, {"row": 445, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "6", "taxon_id": "NCBITaxon:83456", "taxon_label": "Myxococcus virescens", "strain_count": "16", "corroborated_by": ""}}, {"row": 446, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "7", "taxon_id": "NCBITaxon:206", "taxon_label": "Campylobacter sputorum", "strain_count": "15", "corroborated_by": ""}}, {"row": 447, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "8", "taxon_id": "NCBITaxon:71864", "taxon_label": "Herpetosiphon sp.", "strain_count": "11", "corroborated_by": ""}}, {"row": 448, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "9", "taxon_id": "NCBITaxon:38", "taxon_label": "Archangium disciforme", "strain_count": "10", "corroborated_by": ""}}, {"row": 449, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "10", "taxon_id": "NCBITaxon:28450", "taxon_label": "Burkholderia pseudomallei", "strain_count": "8", "corroborated_by": ""}}, {"row": 450, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "11", "taxon_id": "NCBITaxon:1872627", "taxon_label": "Archangium sp.", "strain_count": "7", "corroborated_by": ""}}, {"row": 451, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "12", "taxon_id": "NCBITaxon:90240", "taxon_label": "Moraxella caprae", "strain_count": "7", "corroborated_by": ""}}, {"row": 452, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "13", "taxon_id": "NCBITaxon:108028", "taxon_label": "Arcanobacterium pluranimalium", "strain_count": "6", "corroborated_by": ""}}, {"row": 453, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "14", "taxon_id": "NCBITaxon:75985", "taxon_label": "Mannheimia haemolytica", "strain_count": "6", "corroborated_by": ""}}, {"row": 454, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "15", "taxon_id": "NCBITaxon:83462", "taxon_label": "Corallococcus exiguus", "strain_count": "6", "corroborated_by": ""}}, {"row": 455, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "16", "taxon_id": "NCBITaxon:85401", "taxon_label": "Mannheimia glucosida", "strain_count": "6", "corroborated_by": ""}}, {"row": 456, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "17", "taxon_id": "NCBITaxon:197", "taxon_label": "Campylobacter jejuni", "strain_count": "5", "corroborated_by": ""}}, {"row": 457, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "18", "taxon_id": "NCBITaxon:28121", "taxon_label": "Butyrivibrio sp.", "strain_count": "5", "corroborated_by": ""}}, {"row": 458, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "19", "taxon_id": "NCBITaxon:1661", "taxon_label": "Trueperella pyogenes", "strain_count": "4", "corroborated_by": ""}}, {"row": 459, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "20", "taxon_id": "NCBITaxon:1719", "taxon_label": "Corynebacterium pseudotuberculosis", "strain_count": "4", "corroborated_by": ""}}, {"row": 460, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "21", "taxon_id": "NCBITaxon:1962667", "taxon_label": "Nannocystis sp.", "strain_count": "4", "corroborated_by": ""}}, {"row": 461, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "22", "taxon_id": "NCBITaxon:35", "taxon_label": "Corallococcus macrosporus", "strain_count": "4", "corroborated_by": ""}}, {"row": 462, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "23", "taxon_id": "NCBITaxon:722", "taxon_label": "Actinobacillus seminis", "strain_count": "4", "corroborated_by": ""}}, {"row": 463, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "24", "taxon_id": "NCBITaxon:731", "taxon_label": "Histophilus somni", "strain_count": "4", "corroborated_by": ""}}, {"row": 464, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "25", "taxon_id": "NCBITaxon:82806", "taxon_label": "Streptococcus ovis", "strain_count": "4", "corroborated_by": ""}}] |
| ET6 | data/raw/isolation_source_groundings.tsv; Physical TSV rows 58 | supports | [{"row": 58, "data": {"subject_label": "Caprinae-Sheep/Goat", "subject_label_normalized": "caprinae sheep/goat", "object_id": "FOODON:03411328", "object_label": "goat", "object_source": "FOODON", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification": "semapv:LexicalMatching", "curator": "ols4_search_synonym", "source_dataset": "bacdive", "verified_date": "2026-05-01"}}] |
| ET7 | data/raw/bacdive_isolation_sources.tsv; Physical TSV rows 37 | supports | [{"row": 37, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "label": "Caprinae-Sheep/Goat", "source_slug": "caprinae-sheep/goat", "strain_count": "412", "taxon_count": "137"}}] |
| ET8 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 6797,9006,9007 | supports | [{"row": 6797, "data": {"subject": "ENVO:01001002", "predicate": "rdfs:subClassOf", "object": "ENVO:01001000"}}, {"row": 9006, "data": {"subject": "FOODON:03411328", "predicate": "rdfs:subClassOf", "object": "FOODON:02021055"}}, {"row": 9007, "data": {"subject": "FOODON:03411328", "predicate": "rdfs:subClassOf", "object": "FOODON:03411134"}}] |
| ET9 | data/raw/ontology_terms.tsv; Physical TSV rows 8491,10684 | supports | [{"row": 8491, "data": {"term_id": "ENVO:01001002", "ontology": "ENVO", "label": "animal-associated environment", "definition": "An environmental system determined by an animal.", "synonyms": "Metazoan-associated environment&#124;animal environment", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 10684, "data": {"term_id": "FOODON:03411328", "ontology": "FOODON", "label": "goat", "definition": "A whole goat.", "synonyms": "Capra hircus Linnaeus, 1758&#124;caprine", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET10 | curation/term_requests.tsv; Physical TSV rows 21 | supports | [{"row": 21, "data": {"identifier": "habitatmech:BACDIVE.4d3086a839", "requested_label": "caprine-associated environment", "parent_class": "ENVO:01001002", "parent_label": "animal-associated environment", "definition": "An animal-associated environment which is determined by a sheep or a goat.", "exact_synonym": "Caprinae-Sheep/Goat", "curator": "claude-opus-5", "date": "2026-08-17", "notes": "Definition drafted from the record's deep-research report under research/habitats/ and read against it; the report's proposed wording, genus and near-miss table are the evidence. BacDive's label names both hosts and the mapping upstream dropped the sheep half, so the definition keeps both.", "parent_mode": "ADD"}}] |
| ET11 | curation/decisions.tsv; Physical TSV rows 1539 | supports | [{"row": 1539, "data": {"identifier": "habitatmech:BACDIVE.4d3086a839", "decision": "CONFIRM_UNGROUNDED", "object_id": "FOODON:03411328", "object_label": "goat", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it \u2014 the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an &lt;X&gt;-associated environment. Host-associated &gt; Porifera was NOT_APPLICABLE while its own child Porifera &gt; Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. Category set to HOST_ASSOCIATED (#200): the row already claims ENVO:01001002 'animal-associated environment' as the nearest broader term, which is the claim that a living animal host defines the habitat, and every other record carrying that parent is HOST_ASSOCIATED. The category column was left blank here, so the seeder's default stood and five domestic-mammal hosts stayed in OTHER while their siblings did not. The reasoning above is unchanged.", "review_depth": "ITEM", "category": "HOST_ASSOCIATED", "relation": "xref"}}] |
| EP12 | data/habitats/other/animal_associated_environment.yaml; Entire immediate parent record; context only | supports | {"identifier": "ENVO:01001002", "label": "animal-associated environment", "definition": "An environmental system determined by an animal.", "definition_source": "ENVO", "habitat_category": "OTHER", "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "Metazoan-associated environment", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"}, {"synonym_text": "animal environment", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"}], "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal", "notes": "Physicochemical parameter bands from kg-microbe's environment table."}, {"source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated environment", "assertion_count": 144, "assertion_unit": "TAXON"}], "environmental_parameters": [{"parameter": "PRESSURE", "qualitative_value": "low", "source": "kg-microbe environments.csv (host_animal)"}, {"parameter": "TEMPERATURE_VARIABILITY", "qualitative_value": "low", "source": "kg-microbe environments.csv (host_animal)"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:1001", "source": "MADIN", "taxon_label": "flexibacter_polymorphus", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1001732", "source": "MADIN", "taxon_label": "Mycobacterium abscessus 5S-0921", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1004165", "source": "MADIN", "taxon_label": "Photorhabdus luminescens caribbeanensis HG29", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1004166", "source": "MADIN", "taxon_label": "Photorhabdus luminescens hainanensis C8404", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:102862", "source": "MADIN", "taxon_label": "proteus_penneri", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1028805", "source": "MADIN", "taxon_label": "Haemophilus haemolyticus M21621", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1049564", "source": "MADIN", "taxon_label": "endosymbiont of Tevnia jerichonana (vent Tica)", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1084229", "source": "MADIN", "taxon_label": "Yersinia pestis bv. Orientalis BA200901703", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:110933", "source": "MADIN", "taxon_label": "leifsonia_poae", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123042", "source": "MADIN", "taxon_label": "Photorhabdus temperata stackebrandtii GPS11", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123520", "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9686", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123521", "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9622", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123522", "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9938", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1125973", "source": "MADIN", "taxon_label": "Bosea sp. 117", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1128912", "source": "MADIN", "taxon_label": "Paraglaciecola mesophila KMM 241", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1136416", "source": "MADIN", "taxon_label": "Salinispora pacifica CNT001", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137251", "source": "MADIN", "taxon_label": "Salinispora arenicola CNH905", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137255", "source": "MADIN", "taxon_label": "Salinispora arenicola CNT005", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137257", "source": "MADIN", "taxon_label": "Salinispora arenicola CNX508", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1156842", "source": "MADIN", "taxon_label": "Streptomyces sp. LaPpAH-180", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:115862", "source": "MADIN", "taxon_label": "mycobacterium_caprae", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1159489", "source": "MADIN", "taxon_label": "Cronobacter sakazakii 2151", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187845", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZB36", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187846", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZD137", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187847", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZC157", "candidate_pool": 144}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE, MADIN. Grounding: EXACT."}]} |
| ERESEARCH | research/habitats/other/caprinae-sheep-goat-habitatmech-bacdive-4d3086a839-deep-research-claude_code.md; Entire research report; leads checked against adopted claims | supports | Whole report inspected as a lead. Broad-versus-operational host scope and dung-baiting are explicitly inferences. The current short definition imports neither rumen parameters nor claims that displayed myxobacteria reside inside living hosts. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph; ENVO_01001000-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000; ENVO_01001000.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "ENVO:01001000", "label": "environmental system determined by an organism", "is_obsolete": false, "description": ["An environmental system which is determined by a living organism."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph; ENVO_01001002-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002; ENVO_01001002.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "ENVO:01001002", "label": "animal-associated environment", "is_obsolete": false, "description": ["An environmental system determined by an animal."]} |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03411328/graph; FOODON_03411328-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/FOODON_03411328", "target": "http://purl.obolibrary.org/obo/FOODON_02021055", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/FOODON_03411328", "target": "http://purl.obolibrary.org/obo/FOODON_03411134", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03411328; FOODON_03411328.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "FOODON:03411328", "label": "goat", "is_obsolete": false, "description": ["A goat which is dead or alive and has a relatively intact body.", "A whole goat."]} |
| EX7 | https://bacdive.dsmz.de/isolation-sources; bacdive-isolation.html | context_only | Current BacDive isolation-source browser contains Canidae (Dog) and Caprinae (Sheep/Goat). This verifies vocabulary context, not frozen membership, a domestic-only boundary or equivalence to an environmental-system synonym. |
| EX8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8590674%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; paper-caprine.json | context_only | Primary abstract PMID:8590674, DOI:10.1099/00207713-45-3-467. Eight Moraxella-like strains were isolated from healthy-goat nasal flora and characterized as M. caprae. Supports a scoped caprine-host witness, not all seven BacDive strain assertions for this species. |
| EX9 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=100469,1015,108028,1085628,1159213,1163745,1205679,131109,131112,1329,1330043,1334,1392869,1417985,155085,1580,1661,170187,1719,184914,1872627,1962667,197,2,206,243265,243273,28080,28091,28121,28188,283734,28450,28898,29419,317010,326522,33,34,35,38,388919,398527,52770,54,554290,557433,56,562,590061,694433,71864,722,731,753,754,759,75985,760,82806,83456,83462,85336,85401,90240,99807&amp;retmode=xml; taxonomy.xml | context_only | Current NCBI TaxIds, names and source-label comparison: [{"id": "NCBITaxon:184914", "source": "BACDIVE", "label": "Corallococcus coralloides", "current_id": "184914", "current_name": "Corallococcus coralloides", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:33", "source": "BACDIVE", "label": "Myxococcus fulvus", "current_id": "33", "current_name": "Myxococcus fulvus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:54", "source": "BACDIVE", "label": "Nannocystis exedens", "current_id": "54", "current_name": "Nannocystis exedens", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:56", "source": "BACDIVE", "label": "Sorangium cellulosum", "current_id": "56", "current_name": "Sorangium cellulosum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:34", "source": "BACDIVE", "label": "Myxococcus xanthus", "current_id": "34", "current_name": "Myxococcus xanthus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:83456", "source": "BACDIVE", "label": "Myxococcus virescens", "current_id": "83456", "current_name": "Myxococcus virescens", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:206", "source": "BACDIVE", "label": "Campylobacter sputorum", "current_id": "206", "current_name": "Campylobacter sputorum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:71864", "source": "BACDIVE", "label": "Herpetosiphon sp.", "current_id": "71864", "current_name": "Herpetosiphon sp.", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:38", "source": "BACDIVE", "label": "Archangium disciforme", "current_id": "38", "current_name": "Archangium disciforme", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28450", "source": "BACDIVE", "label": "Burkholderia pseudomallei", "current_id": "28450", "current_name": "Burkholderia pseudomallei", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1872627", "source": "BACDIVE", "label": "Archangium sp.", "current_id": "1872627", "current_name": "Archangium sp.", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:90240", "source": "BACDIVE", "label": "Moraxella caprae", "current_id": "90240", "current_name": "Moraxella caprae", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:108028", "source": "BACDIVE", "label": "Arcanobacterium pluranimalium", "current_id": "108028", "current_name": "Arcanobacterium pluranimalium", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:75985", "source": "BACDIVE", "label": "Mannheimia haemolytica", "current_id": "75985", "current_name": "Mannheimia haemolytica", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:83462", "source": "BACDIVE", "label": "Corallococcus exiguus", "current_id": "83462", "current_name": "Corallococcus exiguus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:85401", "source": "BACDIVE", "label": "Mannheimia glucosida", "current_id": "85401", "current_name": "Mannheimia glucosida", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:197", "source": "BACDIVE", "label": "Campylobacter jejuni", "current_id": "197", "current_name": "Campylobacter jejuni", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28121", "source": "BACDIVE", "label": "Butyrivibrio sp.", "current_id": "28121", "current_name": "Butyrivibrio sp.", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1661", "source": "BACDIVE", "label": "Trueperella pyogenes", "current_id": "1661", "current_name": "Trueperella pyogenes", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1719", "source": "BACDIVE", "label": "Corynebacterium pseudotuberculosis", "current_id": "1719", "current_name": "Corynebacterium pseudotuberculosis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1962667", "source": "BACDIVE", "label": "Nannocystis sp.", "current_id": "1962667", "current_name": "Nannocystis sp.", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:35", "source": "BACDIVE", "label": "Corallococcus macrosporus", "current_id": "35", "current_name": "Corallococcus macrosporus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:722", "source": "BACDIVE", "label": "Actinobacillus seminis", "current_id": "722", "current_name": "Actinobacillus seminis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:731", "source": "BACDIVE", "label": "Histophilus somni", "current_id": "731", "current_name": "Histophilus somni", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:82806", "source": "BACDIVE", "label": "Streptococcus ovis", "current_id": "82806", "current_name": "Streptococcus ovis", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Maintained inputs and local structured archive; rg --no-ignore --hidden -l -F -e habitatmech:BACDIVE.4d3086a839 -e 'caprine-associated environment' -e caprinae_sheep_goat -e habitatmech:BACDIVE.4d3086a839 curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately. No formal target predecessor was found; not every broad label match was inspected. |

## Limits And Additional Notes

- Original specimens and every pair-level source citation have not been independently reidentified. Source counts and ranks are not prevalence, viability, or characteristic presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities were separately checked against current NCBI Taxonomy, not certified by that label gate.
- Full QC evidence is a successful remote run at the exact unchanged scientific input base, not a new local full-QC execution. New review files require a post-save native archive check.
- iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic module or causal mechanism is asserted. No paid research was used.
- Current input hashes were checked against both working bytes and exact tracked base blobs; source.state git_commit explicitly describes that revision.
- Ignored-inclusive searches and the parsed structured archive found no previous structured observation targeting this identifier. Broad label matches are leads, not formal lineage or automatic scientific findings.
- Read-only scientific review: no habitat curation, generation, history/status promotion or GitHub mutation is performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T193045Z-caprinae_sheep_goat-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: caprine-associated environment (habitatmech:BACDIVE.4d3086a839)'
started_at: '2026-10-15T19:06:40Z'
finished_at: '2026-10-15T19:30:45Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the record and sources; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The minted sheep-or-goat-associated environment and animal-associated genus
  are coherent; the goat-only FOODON xref does not assert identity or exclude sheep.
  The exact synonym Caprinae-Sheep/Goat names hosts, not an environmental system.
  The 412 STRAIN assertions and 25 displayed taxa from 137 candidates reproduce their
  sources. Primary Moraxella caprae isolation supports a goat-host witness, not all
  rows; a dung-baiting explanation for the myxobacterial block remains an unverified
  research inference.
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
  - path: data/habitats/host_associated/caprinae_sheep_goat.yaml
    sha256: ca7c78132b0e35cf2b0fca9e6697e9c9b6229751e45859d3b86882434d434b54
    role: target
  - path: data/habitats/other/animal_associated_environment.yaml
    sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
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
  - path: research/habitats/other/caprinae-sheep-goat-habitatmech-bacdive-4d3086a839-deep-research-claude_code.md
    sha256: 038db349fc04bc669f0fa4aa86dcbadedddf32fc79179540c4039c6a0a7e1244
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
- target_id: habitatmech:BACDIVE.4d3086a839
  path: data/habitats/host_associated/caprinae_sheep_goat.yaml
  label: caprine-associated environment
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
  - habitatmech:BACDIVE.4d3086a839
  exclusions:
  - target: Other habitats and SSSOM/KGX products
    reason: Parent context is not additional record coverage. Export conformance and
      original individual specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/caprinae_sheep_goat.yaml
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.4d3086a839
  summary: "Finished 2026-10-15T19:09:51Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/caprinae_sheep_goat.yaml"
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
  - habitatmech:BACDIVE.4d3086a839
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
  - habitatmech:BACDIVE.4d3086a839
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
  - habitatmech:BACDIVE.4d3086a839
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
  - habitatmech:BACDIVE.4d3086a839
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
  - habitatmech:BACDIVE.4d3086a839
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
  - habitatmech:BACDIVE.4d3086a839
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
  - habitatmech:BACDIVE.4d3086a839
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
  - habitatmech:BACDIVE.4d3086a839
  summary: Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592
  scope_note: Unchanged scientific input baseline; these new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/caprinae_sheep_goat.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: All fields, displayed taxa and complete curation history read.
  snapshot_sha256: ca7c78132b0e35cf2b0fca9e6697e9c9b6229751e45859d3b86882434d434b54
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, hierarchy and source-evidence rules
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: All parent contributions must be strictly broader; host identity is not
    environment identity. Source occurrences are not automatically characteristic.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation and category enums
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: Source-to-record mapping endpoints; reported associations versus characteristic
    assertions; category scope and optional fields.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed resolution routes, parent accumulation, prefix category and overrides
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: 'Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:BACDIVE.4d3086a839",
    "automatic": {"identifier": "FOODON:03411328", "grounding_status": "CLOSE", "mapping_predicate":
    "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs":
    [], "route": "bacdive_mapping_table", "category": null, "reviewed": false, "decision":
    null}, "final": {"identifier": "habitatmech:BACDIVE.4d3086a839", "grounding_status":
    "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": ["FOODON:03411328"], "route": "curated_confirm_ungrounded_from_bacdive_mapping_table",
    "category": "HOST_ASSOCIATED", "reviewed": true, "decision": {"identifier": "habitatmech:BACDIVE.4d3086a839",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "FOODON:03411328", "object_label":
    "goat", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-16",
    "notes": "Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning
    that ''a host taxon is not a habitat''. That reasoning is wrong, and the corpus
    already contradicted it \u2014 the same kind of concept was treated as a habitat
    for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own
    identity and a term request for an <X>-associated environment. Host-associated
    > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term
    request.An organism acting as a host IS a habitat: it is where the microbe lives,
    and ENVO models exactly this at plant-associated, animal-associated and fungi-associated
    environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class
    of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept
    keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept
    is not a habitat, which is a stronger and false claim. Category set to HOST_ASSOCIATED
    (#200): the row already claims ENVO:01001002 ''animal-associated environment''
    as the nearest broader term, which is the claim that a living animal host defines
    the habitat, and every other record carrying that parent is HOST_ASSOCIATED. The
    category column was left blank here, so the seeder''s default stood and five domestic-mammal
    hosts stayed in OTHER while their siblings did not. The reasoning above is unchanged.",
    "review_depth": "ITEM", "category": "HOST_ASSOCIATED", "relation": "xref"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Inventory projection
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: Counts/units and taxon ranks/scores preserve source meanings. PREGO projections
    omit original pair-level citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/bacdive_source_taxa.tsv
  locator: Physical TSV rows 440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: '[{"row": 440, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "1", "taxon_id": "NCBITaxon:184914", "taxon_label": "Corallococcus coralloides",
    "strain_count": "40", "corroborated_by": ""}}, {"row": 441, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "2", "taxon_id": "NCBITaxon:33",
    "taxon_label": "Myxococcus fulvus", "strain_count": "29", "corroborated_by": ""}},
    {"row": 442, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "3", "taxon_id": "NCBITaxon:54", "taxon_label": "Nannocystis exedens",
    "strain_count": "27", "corroborated_by": ""}}, {"row": 443, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "4", "taxon_id": "NCBITaxon:56",
    "taxon_label": "Sorangium cellulosum", "strain_count": "24", "corroborated_by":
    ""}}, {"row": 444, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "5", "taxon_id": "NCBITaxon:34", "taxon_label": "Myxococcus xanthus",
    "strain_count": "18", "corroborated_by": ""}}, {"row": 445, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "6", "taxon_id": "NCBITaxon:83456",
    "taxon_label": "Myxococcus virescens", "strain_count": "16", "corroborated_by":
    ""}}, {"row": 446, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "7", "taxon_id": "NCBITaxon:206", "taxon_label": "Campylobacter sputorum",
    "strain_count": "15", "corroborated_by": ""}}, {"row": 447, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "8", "taxon_id": "NCBITaxon:71864",
    "taxon_label": "Herpetosiphon sp.", "strain_count": "11", "corroborated_by": ""}},
    {"row": 448, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "9", "taxon_id": "NCBITaxon:38", "taxon_label": "Archangium disciforme",
    "strain_count": "10", "corroborated_by": ""}}, {"row": 449, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "10", "taxon_id": "NCBITaxon:28450",
    "taxon_label": "Burkholderia pseudomallei", "strain_count": "8", "corroborated_by":
    ""}}, {"row": 450, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "11", "taxon_id": "NCBITaxon:1872627", "taxon_label": "Archangium sp.",
    "strain_count": "7", "corroborated_by": ""}}, {"row": 451, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "12", "taxon_id": "NCBITaxon:90240",
    "taxon_label": "Moraxella caprae", "strain_count": "7", "corroborated_by": ""}},
    {"row": 452, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "13", "taxon_id": "NCBITaxon:108028", "taxon_label": "Arcanobacterium
    pluranimalium", "strain_count": "6", "corroborated_by": ""}}, {"row": 453, "data":
    {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat", "rank": "14", "taxon_id":
    "NCBITaxon:75985", "taxon_label": "Mannheimia haemolytica", "strain_count": "6",
    "corroborated_by": ""}}, {"row": 454, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "15", "taxon_id": "NCBITaxon:83462", "taxon_label": "Corallococcus exiguus",
    "strain_count": "6", "corroborated_by": ""}}, {"row": 455, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "16", "taxon_id": "NCBITaxon:85401",
    "taxon_label": "Mannheimia glucosida", "strain_count": "6", "corroborated_by":
    ""}}, {"row": 456, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "17", "taxon_id": "NCBITaxon:197", "taxon_label": "Campylobacter jejuni",
    "strain_count": "5", "corroborated_by": ""}}, {"row": 457, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "18", "taxon_id": "NCBITaxon:28121",
    "taxon_label": "Butyrivibrio sp.", "strain_count": "5", "corroborated_by": ""}},
    {"row": 458, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "19", "taxon_id": "NCBITaxon:1661", "taxon_label": "Trueperella pyogenes",
    "strain_count": "4", "corroborated_by": ""}}, {"row": 459, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "20", "taxon_id": "NCBITaxon:1719",
    "taxon_label": "Corynebacterium pseudotuberculosis", "strain_count": "4", "corroborated_by":
    ""}}, {"row": 460, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "21", "taxon_id": "NCBITaxon:1962667", "taxon_label": "Nannocystis sp.",
    "strain_count": "4", "corroborated_by": ""}}, {"row": 461, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "22", "taxon_id": "NCBITaxon:35",
    "taxon_label": "Corallococcus macrosporus", "strain_count": "4", "corroborated_by":
    ""}}, {"row": 462, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "23", "taxon_id": "NCBITaxon:722", "taxon_label": "Actinobacillus seminis",
    "strain_count": "4", "corroborated_by": ""}}, {"row": 463, "data": {"bacdive_id":
    "bacdive.isolation_source:caprinae-sheep/goat", "rank": "24", "taxon_id": "NCBITaxon:731",
    "taxon_label": "Histophilus somni", "strain_count": "4", "corroborated_by": ""}},
    {"row": 464, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "rank": "25", "taxon_id": "NCBITaxon:82806", "taxon_label": "Streptococcus ovis",
    "strain_count": "4", "corroborated_by": ""}}]'
  snapshot_sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
- evidence_id: ET6
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: Physical TSV rows 58
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: '[{"row": 58, "data": {"subject_label": "Caprinae-Sheep/Goat", "subject_label_normalized":
    "caprinae sheep/goat", "object_id": "FOODON:03411328", "object_label": "goat",
    "object_source": "FOODON", "predicate_id": "skos:closeMatch", "confidence": "medium",
    "mapping_justification": "semapv:LexicalMatching", "curator": "ols4_search_synonym",
    "source_dataset": "bacdive", "verified_date": "2026-05-01"}}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: ET7
  kind: database
  reference: data/raw/bacdive_isolation_sources.tsv
  locator: Physical TSV rows 37
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: '[{"row": 37, "data": {"bacdive_id": "bacdive.isolation_source:caprinae-sheep/goat",
    "label": "Caprinae-Sheep/Goat", "source_slug": "caprinae-sheep/goat", "strain_count":
    "412", "taxon_count": "137"}}]'
  snapshot_sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 6797,9006,9007
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: '[{"row": 6797, "data": {"subject": "ENVO:01001002", "predicate": "rdfs:subClassOf",
    "object": "ENVO:01001000"}}, {"row": 9006, "data": {"subject": "FOODON:03411328",
    "predicate": "rdfs:subClassOf", "object": "FOODON:02021055"}}, {"row": 9007, "data":
    {"subject": "FOODON:03411328", "predicate": "rdfs:subClassOf", "object": "FOODON:03411134"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET9
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 8491,10684
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: '[{"row": 8491, "data": {"term_id": "ENVO:01001002", "ontology": "ENVO",
    "label": "animal-associated environment", "definition": "An environmental system
    determined by an animal.", "synonyms": "Metazoan-associated environment|animal
    environment", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}},
    {"row": 10684, "data": {"term_id": "FOODON:03411328", "ontology": "FOODON", "label":
    "goat", "definition": "A whole goat.", "synonyms": "Capra hircus Linnaeus, 1758|caprine",
    "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET10
  kind: database
  reference: curation/term_requests.tsv
  locator: Physical TSV rows 21
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: '[{"row": 21, "data": {"identifier": "habitatmech:BACDIVE.4d3086a839",
    "requested_label": "caprine-associated environment", "parent_class": "ENVO:01001002",
    "parent_label": "animal-associated environment", "definition": "An animal-associated
    environment which is determined by a sheep or a goat.", "exact_synonym": "Caprinae-Sheep/Goat",
    "curator": "claude-opus-5", "date": "2026-08-17", "notes": "Definition drafted
    from the record''s deep-research report under research/habitats/ and read against
    it; the report''s proposed wording, genus and near-miss table are the evidence.
    BacDive''s label names both hosts and the mapping upstream dropped the sheep half,
    so the definition keeps both.", "parent_mode": "ADD"}}]'
  snapshot_sha256: da5dcc7d49a3441bd9ff25d95ff204ba4e8716cf062271338ee2795ca16a5ce4
- evidence_id: ET11
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 1539
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: '[{"row": 1539, "data": {"identifier": "habitatmech:BACDIVE.4d3086a839",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "FOODON:03411328", "object_label":
    "goat", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-16",
    "notes": "Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning
    that ''a host taxon is not a habitat''. That reasoning is wrong, and the corpus
    already contradicted it \u2014 the same kind of concept was treated as a habitat
    for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own
    identity and a term request for an <X>-associated environment. Host-associated
    > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term
    request.An organism acting as a host IS a habitat: it is where the microbe lives,
    and ENVO models exactly this at plant-associated, animal-associated and fungi-associated
    environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class
    of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept
    keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept
    is not a habitat, which is a stronger and false claim. Category set to HOST_ASSOCIATED
    (#200): the row already claims ENVO:01001002 ''animal-associated environment''
    as the nearest broader term, which is the claim that a living animal host defines
    the habitat, and every other record carrying that parent is HOST_ASSOCIATED. The
    category column was left blank here, so the seeder''s default stood and five domestic-mammal
    hosts stayed in OTHER while their siblings did not. The reasoning above is unchanged.",
    "review_depth": "ITEM", "category": "HOST_ASSOCIATED", "relation": "xref"}}]'
  snapshot_sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
- evidence_id: EP12
  kind: record_content
  reference: data/habitats/other/animal_associated_environment.yaml
  locator: Entire immediate parent record; context only
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: '{"identifier": "ENVO:01001002", "label": "animal-associated environment",
    "definition": "An environmental system determined by an animal.", "definition_source":
    "ENVO", "habitat_category": "OTHER", "grounding_status": "EXACT", "mapping_status":
    "SEEDED", "synonyms": [{"synonym_text": "Metazoan-associated environment", "synonym_type":
    "EXACT_SYNONYM", "source": "ENVO"}, {"synonym_text": "animal environment", "synonym_type":
    "EXACT_SYNONYM", "source": "ENVO"}], "parent_habitats": ["ENVO:01001000"], "source_attestations":
    [{"source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label":
    "host_animal", "notes": "Physicochemical parameter bands from kg-microbe''s environment
    table."}, {"source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated
    environment", "assertion_count": 144, "assertion_unit": "TAXON"}], "environmental_parameters":
    [{"parameter": "PRESSURE", "qualitative_value": "low", "source": "kg-microbe environments.csv
    (host_animal)"}, {"parameter": "TEMPERATURE_VARIABILITY", "qualitative_value":
    "low", "source": "kg-microbe environments.csv (host_animal)"}], "characteristic_taxa":
    [{"taxon_id": "NCBITaxon:1001", "source": "MADIN", "taxon_label": "flexibacter_polymorphus",
    "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1001732", "source": "MADIN", "taxon_label":
    "Mycobacterium abscessus 5S-0921", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1004165",
    "source": "MADIN", "taxon_label": "Photorhabdus luminescens caribbeanensis HG29",
    "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1004166", "source": "MADIN", "taxon_label":
    "Photorhabdus luminescens hainanensis C8404", "candidate_pool": 144}, {"taxon_id":
    "NCBITaxon:102862", "source": "MADIN", "taxon_label": "proteus_penneri", "candidate_pool":
    144}, {"taxon_id": "NCBITaxon:1028805", "source": "MADIN", "taxon_label": "Haemophilus
    haemolyticus M21621", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1049564",
    "source": "MADIN", "taxon_label": "endosymbiont of Tevnia jerichonana (vent Tica)",
    "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1084229", "source": "MADIN", "taxon_label":
    "Yersinia pestis bv. Orientalis BA200901703", "candidate_pool": 144}, {"taxon_id":
    "NCBITaxon:110933", "source": "MADIN", "taxon_label": "leifsonia_poae", "candidate_pool":
    144}, {"taxon_id": "NCBITaxon:1123042", "source": "MADIN", "taxon_label": "Photorhabdus
    temperata stackebrandtii GPS11", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123520",
    "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9686", "candidate_pool":
    144}, {"taxon_id": "NCBITaxon:1123521", "source": "MADIN", "taxon_label": "Neisseria
    meningitidis DE9622", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123522",
    "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9938", "candidate_pool":
    144}, {"taxon_id": "NCBITaxon:1125973", "source": "MADIN", "taxon_label": "Bosea
    sp. 117", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1128912", "source":
    "MADIN", "taxon_label": "Paraglaciecola mesophila KMM 241", "candidate_pool":
    144}, {"taxon_id": "NCBITaxon:1136416", "source": "MADIN", "taxon_label": "Salinispora
    pacifica CNT001", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137251", "source":
    "MADIN", "taxon_label": "Salinispora arenicola CNH905", "candidate_pool": 144},
    {"taxon_id": "NCBITaxon:1137255", "source": "MADIN", "taxon_label": "Salinispora
    arenicola CNT005", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137257", "source":
    "MADIN", "taxon_label": "Salinispora arenicola CNX508", "candidate_pool": 144},
    {"taxon_id": "NCBITaxon:1156842", "source": "MADIN", "taxon_label": "Streptomyces
    sp. LaPpAH-180", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:115862", "source":
    "MADIN", "taxon_label": "mycobacterium_caprae", "candidate_pool": 144}, {"taxon_id":
    "NCBITaxon:1159489", "source": "MADIN", "taxon_label": "Cronobacter sakazakii
    2151", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187845", "source": "MADIN",
    "taxon_label": "Vibrio genomosp. F10 9ZB36", "candidate_pool": 144}, {"taxon_id":
    "NCBITaxon:1187846", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZD137",
    "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187847", "source": "MADIN", "taxon_label":
    "Vibrio genomosp. F10 9ZC157", "candidate_pool": 144}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE,
    MADIN. Grounding: EXACT."}]}'
  snapshot_sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
- evidence_id: ERESEARCH
  kind: record_content
  reference: research/habitats/other/caprinae-sheep-goat-habitatmech-bacdive-4d3086a839-deep-research-claude_code.md
  locator: Entire research report; leads checked against adopted claims
  accessed_at: '2026-10-15T19:30:45Z'
  support: supports
  summary: Whole report inspected as a lead. Broad-versus-operational host scope and
    dung-baiting are explicitly inferences. The current short definition imports neither
    rumen parameters nor claims that displayed myxobacteria reside inside living hosts.
  snapshot_sha256: 038db349fc04bc669f0fa4aa86dcbadedddf32fc79179540c4039c6a0a7e1244
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
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph
  locator: ENVO_01001002-graph.json
  accessed_at: '2026-10-15T19:06:14Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 882375d994d0dea7166097328c56e0e22362848e68aba0125d1b128a24ebf1b0
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002
  locator: ENVO_01001002.json
  accessed_at: '2026-10-15T19:06:14Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "ENVO:01001002", "label": "animal-associated environment", "is_obsolete": false,
    "description": ["An environmental system determined by an animal."]}'
  snapshot_sha256: c3c90d5e91cc85727658222c907f7747f34861ad80bf1ceac5ce209f7e170907
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03411328/graph
  locator: FOODON_03411328-graph.json
  accessed_at: '2026-10-15T19:06:17Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/FOODON_03411328",
    "target": "http://purl.obolibrary.org/obo/FOODON_02021055", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/FOODON_03411328",
    "target": "http://purl.obolibrary.org/obo/FOODON_03411134", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 64bae2bf8f90ee0ccd9e1f1e387cf5f5bb0be2e919e610c1c1113f184eafa09f
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FFOODON_03411328
  locator: FOODON_03411328.json
  accessed_at: '2026-10-15T19:06:16Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "FOODON:03411328", "label": "goat", "is_obsolete": false, "description": ["A goat
    which is dead or alive and has a relatively intact body.", "A whole goat."]}'
  snapshot_sha256: a5d00fe2dbf81570f650130aa597ce46d9b49963b16966edcb3bf6d462686421
- evidence_id: EX7
  kind: database
  reference: https://bacdive.dsmz.de/isolation-sources
  locator: bacdive-isolation.html
  accessed_at: '2026-10-15T19:19:23Z'
  support: context_only
  summary: Current BacDive isolation-source browser contains Canidae (Dog) and Caprinae
    (Sheep/Goat). This verifies vocabulary context, not frozen membership, a domestic-only
    boundary or equivalence to an environmental-system synonym.
  snapshot_sha256: 60f9932f434230027051edf3e35a6e3af4d52d2812eda2e7088ea9228ffef9de
- evidence_id: EX8
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8590674%20AND%20SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: paper-caprine.json
  accessed_at: '2026-10-15T19:19:13Z'
  support: context_only
  summary: Primary abstract PMID:8590674, DOI:10.1099/00207713-45-3-467. Eight Moraxella-like
    strains were isolated from healthy-goat nasal flora and characterized as M. caprae.
    Supports a scoped caprine-host witness, not all seven BacDive strain assertions
    for this species.
  snapshot_sha256: 092076c27d6d55fd83df40d4ee6aab53325bab04588a05dc8b8f7f4b50bfc6ab
- evidence_id: EX9
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=100469,1015,108028,1085628,1159213,1163745,1205679,131109,131112,1329,1330043,1334,1392869,1417985,155085,1580,1661,170187,1719,184914,1872627,1962667,197,2,206,243265,243273,28080,28091,28121,28188,283734,28450,28898,29419,317010,326522,33,34,35,38,388919,398527,52770,54,554290,557433,56,562,590061,694433,71864,722,731,753,754,759,75985,760,82806,83456,83462,85336,85401,90240,99807&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T19:06:42Z'
  support: context_only
  summary: 'Current NCBI TaxIds, names and source-label comparison: [{"id": "NCBITaxon:184914",
    "source": "BACDIVE", "label": "Corallococcus coralloides", "current_id": "184914",
    "current_name": "Corallococcus coralloides", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:33", "source": "BACDIVE", "label":
    "Myxococcus fulvus", "current_id": "33", "current_name": "Myxococcus fulvus",
    "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:54",
    "source": "BACDIVE", "label": "Nannocystis exedens", "current_id": "54", "current_name":
    "Nannocystis exedens", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:56", "source": "BACDIVE", "label": "Sorangium cellulosum",
    "current_id": "56", "current_name": "Sorangium cellulosum", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:34", "source":
    "BACDIVE", "label": "Myxococcus xanthus", "current_id": "34", "current_name":
    "Myxococcus xanthus", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:83456", "source": "BACDIVE", "label": "Myxococcus virescens",
    "current_id": "83456", "current_name": "Myxococcus virescens", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:206", "source":
    "BACDIVE", "label": "Campylobacter sputorum", "current_id": "206", "current_name":
    "Campylobacter sputorum", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:71864", "source": "BACDIVE", "label": "Herpetosiphon
    sp.", "current_id": "71864", "current_name": "Herpetosiphon sp.", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:38", "source":
    "BACDIVE", "label": "Archangium disciforme", "current_id": "38", "current_name":
    "Archangium disciforme", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:28450", "source": "BACDIVE", "label": "Burkholderia pseudomallei",
    "current_id": "28450", "current_name": "Burkholderia pseudomallei", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1872627", "source":
    "BACDIVE", "label": "Archangium sp.", "current_id": "1872627", "current_name":
    "Archangium sp.", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:90240", "source": "BACDIVE", "label": "Moraxella caprae",
    "current_id": "90240", "current_name": "Moraxella caprae", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:108028", "source":
    "BACDIVE", "label": "Arcanobacterium pluranimalium", "current_id": "108028", "current_name":
    "Arcanobacterium pluranimalium", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:75985", "source": "BACDIVE", "label": "Mannheimia haemolytica",
    "current_id": "75985", "current_name": "Mannheimia haemolytica", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:83462", "source":
    "BACDIVE", "label": "Corallococcus exiguus", "current_id": "83462", "current_name":
    "Corallococcus exiguus", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:85401", "source": "BACDIVE", "label": "Mannheimia glucosida",
    "current_id": "85401", "current_name": "Mannheimia glucosida", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:197", "source":
    "BACDIVE", "label": "Campylobacter jejuni", "current_id": "197", "current_name":
    "Campylobacter jejuni", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:28121", "source": "BACDIVE", "label": "Butyrivibrio sp.",
    "current_id": "28121", "current_name": "Butyrivibrio sp.", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1661", "source":
    "BACDIVE", "label": "Trueperella pyogenes", "current_id": "1661", "current_name":
    "Trueperella pyogenes", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1719", "source": "BACDIVE", "label": "Corynebacterium
    pseudotuberculosis", "current_id": "1719", "current_name": "Corynebacterium pseudotuberculosis",
    "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1962667",
    "source": "BACDIVE", "label": "Nannocystis sp.", "current_id": "1962667", "current_name":
    "Nannocystis sp.", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:35", "source": "BACDIVE", "label": "Corallococcus macrosporus",
    "current_id": "35", "current_name": "Corallococcus macrosporus", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:722", "source":
    "BACDIVE", "label": "Actinobacillus seminis", "current_id": "722", "current_name":
    "Actinobacillus seminis", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:731", "source": "BACDIVE", "label": "Histophilus somni",
    "current_id": "731", "current_name": "Histophilus somni", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:82806", "source": "BACDIVE",
    "label": "Streptococcus ovis", "current_id": "82806", "current_name": "Streptococcus
    ovis", "rank": "species", "direct_match": true, "recognized_alias": true}]'
  snapshot_sha256: ea5036b7cc5c9bf152840fae0a470b8f6cb17f89633967069648541712ecf8b2
- evidence_id: ESEARCH
  kind: search
  reference: Maintained inputs and local structured archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:BACDIVE.4d3086a839 -e 'caprine-associated
    environment' -e caprinae_sheep_goat -e habitatmech:BACDIVE.4d3086a839 curation
    history research reports data/raw build reviews
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
  outcome: concern
  summary: The minted sheep-or-goat-associated environment and animal-associated genus
    are coherent; the goat-only FOODON xref does not assert identity or exclude sheep.
    The exact synonym Caprinae-Sheep/Goat names hosts, not an environmental system.
    The 412 STRAIN assertions and 25 displayed taxa from 137 candidates reproduce
    their sources. Primary Moraxella caprae isolation supports a goat-host witness,
    not all rows; a dung-baiting explanation for the myxobacterial block remains an
    unverified research inference.
  target_ids:
  - habitatmech:BACDIVE.4d3086a839
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  dimensions:
  - name: native_status
    value: UNGROUNDED/REVIEWED
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
    source row. [{"source": "BACDIVE", "count": 412, "unit": "STRAIN"}]. Side-table
    biosamples and study memberships are separate from tree ORGANISM counts; zero-count
    omission is not biological absence.'
  target_ids:
  - habitatmech:BACDIVE.4d3086a839
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  dimensions:
  - name: source_assertion_units
    value: '[{"source": "BACDIVE", "count": 412, "unit": "STRAIN"}]'
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
  summary: The minted sheep-or-goat-associated environment and animal-associated genus
    are coherent; the goat-only FOODON xref does not assert identity or exclude sheep.
    The exact synonym Caprinae-Sheep/Goat names hosts, not an environmental system.
    The 412 STRAIN assertions and 25 displayed taxa from 137 candidates reproduce
    their sources. Primary Moraxella caprae isolation supports a goat-host witness,
    not all rows; a dung-baiting explanation for the myxobacterial block remains an
    unverified research inference.
  target_ids:
  - habitatmech:BACDIVE.4d3086a839
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - ERESEARCH
- assessment_id: A4
  area: completeness
  topic: Curation status, parameters, mechanisms and optional content
  outcome: supported
  summary: Executed routes reproduce UNGROUNDED/REVIEWED. No target environmental
    parameters, causal edges, discussions/datasets or is_characteristic=true assertions
    are present. Parent-record mechanisms are not inherited. Optional absence and
    SEEDED status alone are not defects.
  target_ids:
  - habitatmech:BACDIVE.4d3086a839
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
  - habitatmech:BACDIVE.4d3086a839
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: caprinae-sheep-goat-host-alias
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Whole-host label is an exact environment synonym
  description: Remove authored exact synonym Caprinae-Sheep/Goat and guard definition-source-label
    fallback from reintroducing it. Preserve the verbatim source attestation, minted
    habitat identity, supported definition and host xrefs.
  target_ids:
  - habitatmech:BACDIVE.4d3086a839
  field_paths:
  - synonyms
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:BACDIVE.4d3086a839
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Remove authored exact synonym Caprinae-Sheep/Goat and guard definition-source-label
    fallback from reintroducing it. Preserve the verbatim source attestation, minted
    habitat identity, supported definition and host xrefs. No repair is performed
    by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independent identities, source totals/units
    and raw provenance. Change mapping or native status only when separately supported
    by the item assessment; never alter source counts by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
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
tags:
- individual-scientific-review
- host-associated
```
