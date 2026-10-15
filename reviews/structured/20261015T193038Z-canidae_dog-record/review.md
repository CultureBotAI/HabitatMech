# Record review: canid-associated environment (habitatmech:BACDIVE.33fde10528)

- Review: 20261015T193038Z-canidae_dog-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T19:05:54Z
- Finished UTC: 2026-10-15T19:30:38Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The minted canid-associated environment, animal-associated genus and Canidae taxon xref preserve host versus habitat identity. The exact synonym Canidae-Dog incorrectly equates a host category with its environment. All 344 STRAIN assertions and 25 displayed taxa from a 139-taxon pool remain source evidence, not a universal dog microbiome or proof of domestic-dog-only scope.

## Scope And Provenance

Full field-by-field scientific assessment of this exact target at a073f8e821a7c095f35501982930cc5a156835c0.

Selection: One of the next 24 path-ordered unreviewed identifiers in an ignored-inclusive 3208-record census. This bundle reviews one identifier, not a sample standing for other targets.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base a073f8e821a7c095f35501982930cc5a156835c0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.33fde10528 | data/habitats/host_associated/canidae_dog.yaml | generated | canid-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:BACDIVE.33fde10528 | Finished 2026-10-15T19:09:41Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/canidae_dog.yaml |
| validate-strict | passed | True | habitatmech:BACDIVE.33fde10528 | Finished 2026-10-15T19:10:07Z. uv run python scripts/validate_strict.py data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:BACDIVE.33fde10528 | Finished 2026-10-15T19:10:18Z. No issues found<br>816 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:BACDIVE.33fde10528 | Finished 2026-10-15T19:10:19Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:BACDIVE.33fde10528 | Finished 2026-10-15T19:10:38Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:BACDIVE.33fde10528 | Finished 2026-10-15T19:10:44Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:BACDIVE.33fde10528 | Finished 2026-10-15T19:11:04Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:BACDIVE.33fde10528 | Finished 2026-10-15T19:12:07Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | habitatmech:BACDIVE.33fde10528 | Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592 |

## Scientific And Domain Assessments

### Identity, definition, category and broader ancestry

identity: concern. Targets: habitatmech:BACDIVE.33fde10528.

The minted canid-associated environment, animal-associated genus and Canidae taxon xref preserve host versus habitat identity. The exact synonym Canidae-Dog incorrectly equates a host category with its environment. All 344 STRAIN assertions and 25 displayed taxa from a 139-taxon pool remain source evidence, not a universal dog microbiome or proof of domestic-dog-only scope.

### Source counts, units, ranks, pools and channels

quantity: supported. Targets: habitatmech:BACDIVE.33fde10528.

Every attestation and displayed taxon was compared with its exact frozen source row. [{"source": "BACDIVE", "count": 344, "unit": "STRAIN"}]. Side-table biosamples and study memberships are separate from tree ORGANISM counts; zero-count omission is not biological absence.

### Biological support and limits

evidence: supported. Targets: habitatmech:BACDIVE.33fde10528.

The minted canid-associated environment, animal-associated genus and Canidae taxon xref preserve host versus habitat identity. The exact synonym Canidae-Dog incorrectly equates a host category with its environment. All 344 STRAIN assertions and 25 displayed taxa from a 139-taxon pool remain source evidence, not a universal dog microbiome or proof of domestic-dog-only scope.

### Curation status, parameters, mechanisms and optional content

completeness: supported. Targets: habitatmech:BACDIVE.33fde10528.

Executed routes reproduce UNGROUNDED/REVIEWED. No target environmental parameters, causal edges, discussions/datasets or is_characteristic=true assertions are present. Parent-record mechanisms are not inherited. Optional absence and SEEDED status alone are not defects.

### Native deterministic gates

schema: supported. Targets: habitatmech:BACDIVE.33fde10528.

Ordinary and strict schema, 816 curation histories, provenance, exact 3208-record reproduction, 32 causal overlays, term requests, configured labels and exact-base QC passed. Deterministic fidelity does not establish biological correctness.

## Findings

### F1: Whole-host label is an exact environment synonym

major / open / confirmed; issue key: canidae-dog-host-alias.

Remove authored exact synonym Canidae-Dog and guard definition-source-label fallback from reintroducing it. Preserve the verbatim source attestation, minted habitat identity, supported definition and host xrefs.

## Recommended Actions And Acceptance Checks

### ACT1

Remove authored exact synonym Canidae-Dog and guard definition-source-label fallback from reintroducing it. Preserve the verbatim source attestation, minted habitat identity, supported definition and host xrefs. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identities, source totals/units and raw provenance. Change mapping or native status only when separately supported by the item assessment; never alter source counts by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/canidae_dog.yaml; Entire target YAML | supports | All fields, displayed taxa and complete curation history read. |
| ERULE | docs/CURATION.md; Identity, hierarchy and source-evidence rules | supports | All parent contributions must be strictly broader; host identity is not environment identity. Source occurrences are not automatically characteristic. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation and category enums | supports | Source-to-record mapping endpoints; reported associations versus characteristic assertions; category scope and optional fields. |
| ESEED | src/habitatmech/seed.py; Executed resolution routes, parent accumulation, prefix category and overrides | supports | Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:BACDIVE.33fde10528", "automatic": {"identifier": "habitatmech:BACDIVE.33fde10528", "grounding_status": "NOT_APPLICABLE", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": ["NCBITaxon:9608"], "route": "bacdive_non_habitat_target", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:BACDIVE.33fde10528", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": ["NCBITaxon:9608"], "route": "curated_confirm_ungrounded_from_bacdive_non_habitat_target", "category": "HOST_ASSOCIATED", "reviewed": true, "decision": {"identifier": "habitatmech:BACDIVE.33fde10528", "decision": "CONFIRM_UNGROUNDED", "object_id": "NCBITaxon:9608", "object_label": "Canidae", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-26", "notes": "Host-taxon reversal (#114) reaching the last members of its own family (#194): this was NOT_APPLICABLE, which asserts the source concept is not a habitat. An organism acting as a host IS a habitat, and the corpus already says so for bovine, caprine, equid, leporid and suid, all minted with ENVO:01001002 'animal-associated environment' as parent and the organism term as an xref. Never curated on the question at all: the NOT_APPLICABLE was the seeder's automatic bacdive_non_habitat_target route firing on an NCBITaxon target, and #114's sweep did not reach this row. The taxon term is not the identity - a family is a class of organisms, not a place - so it stays an xref (#99) and the concept keeps its minted identity with a term request. Category HOST_ASSOCIATED: the host is living.", "review_depth": "ITEM", "category": "HOST_ASSOCIATED", "relation": "xref"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Inventory projection | supports | Counts/units and taxon ranks/scores preserve source meanings. PREGO projections omit original pair-level citation links. |
| ET5 | data/raw/bacdive_source_taxa.tsv; Physical TSV rows 414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438 | supports | [{"row": 414, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "1", "taxon_id": "NCBITaxon:28091", "taxon_label": "Neisseria weaveri", "strain_count": "31", "corroborated_by": ""}}, {"row": 415, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "2", "taxon_id": "NCBITaxon:28080", "taxon_label": "Campylobacter upsaliensis", "strain_count": "21", "corroborated_by": ""}}, {"row": 416, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "3", "taxon_id": "NCBITaxon:754", "taxon_label": "Pasteurella dagmatis", "strain_count": "17", "corroborated_by": ""}}, {"row": 417, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "4", "taxon_id": "NCBITaxon:1015", "taxon_label": "Bergeyella zoohelcum", "strain_count": "16", "corroborated_by": ""}}, {"row": 418, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "5", "taxon_id": "NCBITaxon:2", "taxon_label": "Bacteria", "strain_count": "16", "corroborated_by": ""}}, {"row": 419, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "6", "taxon_id": "NCBITaxon:28188", "taxon_label": "Capnocytophaga canimorsus", "strain_count": "16", "corroborated_by": ""}}, {"row": 420, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "7", "taxon_id": "NCBITaxon:753", "taxon_label": "Pasteurella canis", "strain_count": "13", "corroborated_by": ""}}, {"row": 421, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "8", "taxon_id": "NCBITaxon:760", "taxon_label": "Pasteurella stomatis", "strain_count": "9", "corroborated_by": ""}}, {"row": 422, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "9", "taxon_id": "NCBITaxon:85336", "taxon_label": "Rothia nasimurium", "strain_count": "9", "corroborated_by": ""}}, {"row": 423, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "10", "taxon_id": "NCBITaxon:197", "taxon_label": "Campylobacter jejuni", "strain_count": "6", "corroborated_by": ""}}, {"row": 424, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "11", "taxon_id": "NCBITaxon:283734", "taxon_label": "Staphylococcus pseudintermedius", "strain_count": "5", "corroborated_by": ""}}, {"row": 425, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "12", "taxon_id": "NCBITaxon:326522", "taxon_label": "Neisseria animaloris", "strain_count": "5", "corroborated_by": ""}}, {"row": 426, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "13", "taxon_id": "NCBITaxon:99807", "taxon_label": "Corynebacterium auriscanis", "strain_count": "5", "corroborated_by": ""}}, {"row": 427, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "14", "taxon_id": "NCBITaxon:1329", "taxon_label": "Streptococcus canis", "strain_count": "4", "corroborated_by": ""}}, {"row": 428, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "15", "taxon_id": "NCBITaxon:28898", "taxon_label": "Campylobacter helveticus", "strain_count": "4", "corroborated_by": ""}}, {"row": 429, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "16", "taxon_id": "NCBITaxon:29419", "taxon_label": "Helicobacter canis", "strain_count": "4", "corroborated_by": ""}}, {"row": 430, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "17", "taxon_id": "NCBITaxon:317010", "taxon_label": "Enterococcus canintestini", "strain_count": "4", "corroborated_by": ""}}, {"row": 431, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "18", "taxon_id": "NCBITaxon:759", "taxon_label": "Pasteurella sp.", "strain_count": "4", "corroborated_by": ""}}, {"row": 432, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "19", "taxon_id": "NCBITaxon:1159213", "taxon_label": "Peptostreptococcus canis", "strain_count": "3", "corroborated_by": ""}}, {"row": 433, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "20", "taxon_id": "NCBITaxon:131109", "taxon_label": "Actinomyces bowdenii", "strain_count": "3", "corroborated_by": ""}}, {"row": 434, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "21", "taxon_id": "NCBITaxon:131112", "taxon_label": "Arcanobacterium phocae", "strain_count": "3", "corroborated_by": ""}}, {"row": 435, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "22", "taxon_id": "NCBITaxon:1334", "taxon_label": "Streptococcus dysgalactiae", "strain_count": "3", "corroborated_by": ""}}, {"row": 436, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "23", "taxon_id": "NCBITaxon:155085", "taxon_label": "Staphylococcus lutrae", "strain_count": "3", "corroborated_by": ""}}, {"row": 437, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "24", "taxon_id": "NCBITaxon:52770", "taxon_label": "Buchananella hordeovulneris", "strain_count": "3", "corroborated_by": ""}}, {"row": 438, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank": "25", "taxon_id": "NCBITaxon:100469", "taxon_label": "Schaalia canis", "strain_count": "2", "corroborated_by": ""}}] |
| ET6 | data/raw/isolation_source_groundings.tsv; Physical TSV rows 56 | supports | [{"row": 56, "data": {"subject_label": "Canidae-Dog", "subject_label_normalized": "canidae dog", "object_id": "NCBITaxon:9608", "object_label": "Canidae", "object_source": "NCBITaxon", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification": "semapv:LexicalMatching", "curator": "ols4_auto", "source_dataset": "bacdive", "verified_date": "2026-05-01"}}] |
| ET7 | data/raw/bacdive_isolation_sources.tsv; Physical TSV rows 42 | supports | [{"row": 42, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "label": "Canidae-Dog", "source_slug": "canidae-dog", "strain_count": "344", "taxon_count": "139"}}] |
| ET8 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 6797 | supports | [{"row": 6797, "data": {"subject": "ENVO:01001002", "predicate": "rdfs:subClassOf", "object": "ENVO:01001000"}}] |
| ET9 | data/raw/ontology_terms.tsv; Physical TSV rows 8491,10766 | supports | [{"row": 8491, "data": {"term_id": "ENVO:01001002", "ontology": "ENVO", "label": "animal-associated environment", "definition": "An environmental system determined by an animal.", "synonyms": "Metazoan-associated environment&#124;animal environment", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 10766, "data": {"term_id": "NCBITaxon:9608", "ontology": "NCBITaxon", "label": "Canidae", "definition": "", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "TRUE"}}] |
| ET10 | curation/term_requests.tsv; Physical TSV rows 45 | supports | [{"row": 45, "data": {"identifier": "habitatmech:BACDIVE.33fde10528", "requested_label": "canid-associated environment", "parent_class": "ENVO:01001002", "parent_label": "animal-associated environment", "definition": "An animal-associated environment which is determined by a dog or other canid.", "exact_synonym": "Canidae-Dog", "curator": "claude-opus-5", "date": "2026-08-26", "notes": "Definition follows the established &lt;clade&gt;-associated environment family for BacDive host buckets, whose naming rule the corpus already fixes: a -inae source label yields -ine (Bovinae-Cow,-Cattle -&gt; bovine) and a -idae source label yields -id (Equidae-Horse -&gt; equid, Leporidae-Rabbit/Hare -&gt; leporid, Suidae-Pig,Swine -&gt; suid). No deep-research run was commissioned: the genus, the wording pattern and the near-miss reasoning are already settled by those five siblings and by NCBITaxon, so a billed report would add nothing this slice turns on. Worded like the equid sibling because the source label names one vernacular host inside a wider family: NCBITaxon:9608 'Canidae' also covers foxes, wolves and jackals, so the definition must not silently narrow to the dog.", "parent_mode": "ADD"}}] |
| ET11 | curation/decisions.tsv; Physical TSV rows 1815 | supports | [{"row": 1815, "data": {"identifier": "habitatmech:BACDIVE.33fde10528", "decision": "CONFIRM_UNGROUNDED", "object_id": "NCBITaxon:9608", "object_label": "Canidae", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-26", "notes": "Host-taxon reversal (#114) reaching the last members of its own family (#194): this was NOT_APPLICABLE, which asserts the source concept is not a habitat. An organism acting as a host IS a habitat, and the corpus already says so for bovine, caprine, equid, leporid and suid, all minted with ENVO:01001002 'animal-associated environment' as parent and the organism term as an xref. Never curated on the question at all: the NOT_APPLICABLE was the seeder's automatic bacdive_non_habitat_target route firing on an NCBITaxon target, and #114's sweep did not reach this row. The taxon term is not the identity - a family is a class of organisms, not a place - so it stays an xref (#99) and the concept keeps its minted identity with a term request. Category HOST_ASSOCIATED: the host is living.", "review_depth": "ITEM", "category": "HOST_ASSOCIATED", "relation": "xref"}}] |
| EP12 | data/habitats/other/animal_associated_environment.yaml; Entire immediate parent record; context only | supports | {"identifier": "ENVO:01001002", "label": "animal-associated environment", "definition": "An environmental system determined by an animal.", "definition_source": "ENVO", "habitat_category": "OTHER", "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "Metazoan-associated environment", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"}, {"synonym_text": "animal environment", "synonym_type": "EXACT_SYNONYM", "source": "ENVO"}], "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal", "notes": "Physicochemical parameter bands from kg-microbe's environment table."}, {"source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated environment", "assertion_count": 144, "assertion_unit": "TAXON"}], "environmental_parameters": [{"parameter": "PRESSURE", "qualitative_value": "low", "source": "kg-microbe environments.csv (host_animal)"}, {"parameter": "TEMPERATURE_VARIABILITY", "qualitative_value": "low", "source": "kg-microbe environments.csv (host_animal)"}], "characteristic_taxa": [{"taxon_id": "NCBITaxon:1001", "source": "MADIN", "taxon_label": "flexibacter_polymorphus", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1001732", "source": "MADIN", "taxon_label": "Mycobacterium abscessus 5S-0921", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1004165", "source": "MADIN", "taxon_label": "Photorhabdus luminescens caribbeanensis HG29", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1004166", "source": "MADIN", "taxon_label": "Photorhabdus luminescens hainanensis C8404", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:102862", "source": "MADIN", "taxon_label": "proteus_penneri", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1028805", "source": "MADIN", "taxon_label": "Haemophilus haemolyticus M21621", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1049564", "source": "MADIN", "taxon_label": "endosymbiont of Tevnia jerichonana (vent Tica)", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1084229", "source": "MADIN", "taxon_label": "Yersinia pestis bv. Orientalis BA200901703", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:110933", "source": "MADIN", "taxon_label": "leifsonia_poae", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123042", "source": "MADIN", "taxon_label": "Photorhabdus temperata stackebrandtii GPS11", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123520", "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9686", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123521", "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9622", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1123522", "source": "MADIN", "taxon_label": "Neisseria meningitidis DE9938", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1125973", "source": "MADIN", "taxon_label": "Bosea sp. 117", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1128912", "source": "MADIN", "taxon_label": "Paraglaciecola mesophila KMM 241", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1136416", "source": "MADIN", "taxon_label": "Salinispora pacifica CNT001", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137251", "source": "MADIN", "taxon_label": "Salinispora arenicola CNH905", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137255", "source": "MADIN", "taxon_label": "Salinispora arenicola CNT005", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1137257", "source": "MADIN", "taxon_label": "Salinispora arenicola CNX508", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1156842", "source": "MADIN", "taxon_label": "Streptomyces sp. LaPpAH-180", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:115862", "source": "MADIN", "taxon_label": "mycobacterium_caprae", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1159489", "source": "MADIN", "taxon_label": "Cronobacter sakazakii 2151", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187845", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZB36", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187846", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZD137", "candidate_pool": 144}, {"taxon_id": "NCBITaxon:1187847", "source": "MADIN", "taxon_label": "Vibrio genomosp. F10 9ZC157", "candidate_pool": 144}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by ENVIRONMENTS_TABLE, MADIN. Grounding: EXACT."}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph; ENVO_01001000-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000; ENVO_01001000.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "ENVO:01001000", "label": "environmental system determined by an organism", "is_obsolete": false, "description": ["An environmental system which is determined by a living organism."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph; ENVO_01001002-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002; ENVO_01001002.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "ENVO:01001002", "label": "animal-associated environment", "is_obsolete": false, "description": ["An environmental system determined by an animal."]} |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/ncbitaxon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCBITaxon_9608/graph; NCBITaxon_9608-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/NCBITaxon_9608", "target": "http://purl.obolibrary.org/obo/NCBITaxon_379584", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/ncbitaxon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCBITaxon_9608; NCBITaxon_9608.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "NCBITaxon:9608", "label": "Canidae", "is_obsolete": false, "description": []} |
| EX7 | https://bacdive.dsmz.de/isolation-sources; bacdive-isolation.html | context_only | Current BacDive isolation-source browser contains Canidae (Dog) and Caprinae (Sheep/Goat). This verifies vocabulary context, not frozen membership, a domestic-only boundary or equivalence to an environmental-system synonym. |
| EX8 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=100469,1015,108028,1085628,1159213,1163745,1205679,131109,131112,1329,1330043,1334,1392869,1417985,155085,1580,1661,170187,1719,184914,1872627,1962667,197,2,206,243265,243273,28080,28091,28121,28188,283734,28450,28898,29419,317010,326522,33,34,35,38,388919,398527,52770,54,554290,557433,56,562,590061,694433,71864,722,731,753,754,759,75985,760,82806,83456,83462,85336,85401,90240,99807&amp;retmode=xml; taxonomy.xml | context_only | Current NCBI TaxIds, names and source-label comparison: [{"id": "NCBITaxon:28091", "source": "BACDIVE", "label": "Neisseria weaveri", "current_id": "28091", "current_name": "Neisseria weaveri", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28080", "source": "BACDIVE", "label": "Campylobacter upsaliensis", "current_id": "28080", "current_name": "Campylobacter upsaliensis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:754", "source": "BACDIVE", "label": "Pasteurella dagmatis", "current_id": "754", "current_name": "Pasteurella dagmatis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1015", "source": "BACDIVE", "label": "Bergeyella zoohelcum", "current_id": "1015", "current_name": "Bergeyella zoohelcum", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2", "source": "BACDIVE", "label": "Bacteria", "current_id": "2", "current_name": "Bacteria", "rank": "domain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28188", "source": "BACDIVE", "label": "Capnocytophaga canimorsus", "current_id": "28188", "current_name": "Capnocytophaga canimorsus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:753", "source": "BACDIVE", "label": "Pasteurella canis", "current_id": "753", "current_name": "Pasteurella canis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:760", "source": "BACDIVE", "label": "Pasteurella stomatis", "current_id": "760", "current_name": "Pasteurella stomatis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:85336", "source": "BACDIVE", "label": "Rothia nasimurium", "current_id": "85336", "current_name": "Rothia nasimurium", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:197", "source": "BACDIVE", "label": "Campylobacter jejuni", "current_id": "197", "current_name": "Campylobacter jejuni", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:283734", "source": "BACDIVE", "label": "Staphylococcus pseudintermedius", "current_id": "283734", "current_name": "Staphylococcus pseudintermedius", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:326522", "source": "BACDIVE", "label": "Neisseria animaloris", "current_id": "326522", "current_name": "Neisseria animaloris", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:99807", "source": "BACDIVE", "label": "Corynebacterium auriscanis", "current_id": "99807", "current_name": "Corynebacterium auriscanis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1329", "source": "BACDIVE", "label": "Streptococcus canis", "current_id": "1329", "current_name": "Streptococcus canis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28898", "source": "BACDIVE", "label": "Campylobacter helveticus", "current_id": "28898", "current_name": "Campylobacter helveticus", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:29419", "source": "BACDIVE", "label": "Helicobacter canis", "current_id": "29419", "current_name": "Helicobacter canis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:317010", "source": "BACDIVE", "label": "Enterococcus canintestini", "current_id": "317010", "current_name": "Enterococcus canintestini", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:759", "source": "BACDIVE", "label": "Pasteurella sp.", "current_id": "759", "current_name": "Pasteurella sp.", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1159213", "source": "BACDIVE", "label": "Peptostreptococcus canis", "current_id": "1159213", "current_name": "Peptostreptococcus canis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:131109", "source": "BACDIVE", "label": "Actinomyces bowdenii", "current_id": "131109", "current_name": "Actinomyces bowdenii", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:131112", "source": "BACDIVE", "label": "Arcanobacterium phocae", "current_id": "131112", "current_name": "Arcanobacterium phocae", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:1334", "source": "BACDIVE", "label": "Streptococcus dysgalactiae", "current_id": "1334", "current_name": "Streptococcus dysgalactiae", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:155085", "source": "BACDIVE", "label": "Staphylococcus lutrae", "current_id": "155085", "current_name": "Staphylococcus lutrae", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:52770", "source": "BACDIVE", "label": "Buchananella hordeovulneris", "current_id": "52770", "current_name": "Buchananella hordeovulneris", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:100469", "source": "BACDIVE", "label": "Schaalia canis", "current_id": "100469", "current_name": "Schaalia canis", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Maintained inputs and local structured archive; rg --no-ignore --hidden -l -F -e habitatmech:BACDIVE.33fde10528 -e 'canid-associated environment' -e canidae_dog -e habitatmech:BACDIVE.33fde10528 curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately. No formal target predecessor was found; not every broad label match was inspected. |

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
review_id: 20261015T193038Z-canidae_dog-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: canid-associated environment (habitatmech:BACDIVE.33fde10528)'
started_at: '2026-10-15T19:05:54Z'
finished_at: '2026-10-15T19:30:38Z'
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
summary: The minted canid-associated environment, animal-associated genus and Canidae
  taxon xref preserve host versus habitat identity. The exact synonym Canidae-Dog
  incorrectly equates a host category with its environment. All 344 STRAIN assertions
  and 25 displayed taxa from a 139-taxon pool remain source evidence, not a universal
  dog microbiome or proof of domestic-dog-only scope.
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
  - path: data/habitats/host_associated/canidae_dog.yaml
    sha256: 5a771d3b7370c5b9522e343c0089236d2cb716d13c573139d1947a381fbf7784
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
- target_id: habitatmech:BACDIVE.33fde10528
  path: data/habitats/host_associated/canidae_dog.yaml
  label: canid-associated environment
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
  - habitatmech:BACDIVE.33fde10528
  exclusions:
  - target: Other habitats and SSSOM/KGX products
    reason: Parent context is not additional record coverage. Export conformance and
      original individual specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/canidae_dog.yaml
  exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.33fde10528
  summary: "Finished 2026-10-15T19:09:41Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/canidae_dog.yaml"
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
  - habitatmech:BACDIVE.33fde10528
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
  - habitatmech:BACDIVE.33fde10528
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
  - habitatmech:BACDIVE.33fde10528
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
  - habitatmech:BACDIVE.33fde10528
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
  - habitatmech:BACDIVE.33fde10528
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
  - habitatmech:BACDIVE.33fde10528
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
  - habitatmech:BACDIVE.33fde10528
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
  - habitatmech:BACDIVE.33fde10528
  summary: Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592
  scope_note: Unchanged scientific input baseline; these new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/canidae_dog.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: All fields, displayed taxa and complete curation history read.
  snapshot_sha256: 5a771d3b7370c5b9522e343c0089236d2cb716d13c573139d1947a381fbf7784
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, hierarchy and source-evidence rules
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: All parent contributions must be strictly broader; host identity is not
    environment identity. Source occurrences are not automatically characteristic.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation and category enums
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: Source-to-record mapping endpoints; reported associations versus characteristic
    assertions; category scope and optional fields.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed resolution routes, parent accumulation, prefix category and overrides
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: 'Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:BACDIVE.33fde10528",
    "automatic": {"identifier": "habitatmech:BACDIVE.33fde10528", "grounding_status":
    "NOT_APPLICABLE", "mapping_predicate": null, "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": ["NCBITaxon:9608"], "route": "bacdive_non_habitat_target",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "habitatmech:BACDIVE.33fde10528", "grounding_status": "UNGROUNDED", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": ["NCBITaxon:9608"],
    "route": "curated_confirm_ungrounded_from_bacdive_non_habitat_target", "category":
    "HOST_ASSOCIATED", "reviewed": true, "decision": {"identifier": "habitatmech:BACDIVE.33fde10528",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "NCBITaxon:9608", "object_label":
    "Canidae", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-26",
    "notes": "Host-taxon reversal (#114) reaching the last members of its own family
    (#194): this was NOT_APPLICABLE, which asserts the source concept is not a habitat.
    An organism acting as a host IS a habitat, and the corpus already says so for
    bovine, caprine, equid, leporid and suid, all minted with ENVO:01001002 ''animal-associated
    environment'' as parent and the organism term as an xref. Never curated on the
    question at all: the NOT_APPLICABLE was the seeder''s automatic bacdive_non_habitat_target
    route firing on an NCBITaxon target, and #114''s sweep did not reach this row.
    The taxon term is not the identity - a family is a class of organisms, not a place
    - so it stays an xref (#99) and the concept keeps its minted identity with a term
    request. Category HOST_ASSOCIATED: the host is living.", "review_depth": "ITEM",
    "category": "HOST_ASSOCIATED", "relation": "xref"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Inventory projection
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: Counts/units and taxon ranks/scores preserve source meanings. PREGO projections
    omit original pair-level citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/bacdive_source_taxa.tsv
  locator: Physical TSV rows 414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: '[{"row": 414, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "1", "taxon_id": "NCBITaxon:28091", "taxon_label": "Neisseria weaveri",
    "strain_count": "31", "corroborated_by": ""}}, {"row": 415, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "2", "taxon_id": "NCBITaxon:28080",
    "taxon_label": "Campylobacter upsaliensis", "strain_count": "21", "corroborated_by":
    ""}}, {"row": 416, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "3", "taxon_id": "NCBITaxon:754", "taxon_label": "Pasteurella dagmatis",
    "strain_count": "17", "corroborated_by": ""}}, {"row": 417, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "4", "taxon_id": "NCBITaxon:1015",
    "taxon_label": "Bergeyella zoohelcum", "strain_count": "16", "corroborated_by":
    ""}}, {"row": 418, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "5", "taxon_id": "NCBITaxon:2", "taxon_label": "Bacteria", "strain_count":
    "16", "corroborated_by": ""}}, {"row": 419, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "6", "taxon_id": "NCBITaxon:28188", "taxon_label": "Capnocytophaga canimorsus",
    "strain_count": "16", "corroborated_by": ""}}, {"row": 420, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "7", "taxon_id": "NCBITaxon:753",
    "taxon_label": "Pasteurella canis", "strain_count": "13", "corroborated_by": ""}},
    {"row": 421, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank":
    "8", "taxon_id": "NCBITaxon:760", "taxon_label": "Pasteurella stomatis", "strain_count":
    "9", "corroborated_by": ""}}, {"row": 422, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "9", "taxon_id": "NCBITaxon:85336", "taxon_label": "Rothia nasimurium",
    "strain_count": "9", "corroborated_by": ""}}, {"row": 423, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "10", "taxon_id": "NCBITaxon:197",
    "taxon_label": "Campylobacter jejuni", "strain_count": "6", "corroborated_by":
    ""}}, {"row": 424, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "11", "taxon_id": "NCBITaxon:283734", "taxon_label": "Staphylococcus pseudintermedius",
    "strain_count": "5", "corroborated_by": ""}}, {"row": 425, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "12", "taxon_id": "NCBITaxon:326522",
    "taxon_label": "Neisseria animaloris", "strain_count": "5", "corroborated_by":
    ""}}, {"row": 426, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "13", "taxon_id": "NCBITaxon:99807", "taxon_label": "Corynebacterium auriscanis",
    "strain_count": "5", "corroborated_by": ""}}, {"row": 427, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "14", "taxon_id": "NCBITaxon:1329",
    "taxon_label": "Streptococcus canis", "strain_count": "4", "corroborated_by":
    ""}}, {"row": 428, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "15", "taxon_id": "NCBITaxon:28898", "taxon_label": "Campylobacter helveticus",
    "strain_count": "4", "corroborated_by": ""}}, {"row": 429, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "16", "taxon_id": "NCBITaxon:29419",
    "taxon_label": "Helicobacter canis", "strain_count": "4", "corroborated_by": ""}},
    {"row": 430, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank":
    "17", "taxon_id": "NCBITaxon:317010", "taxon_label": "Enterococcus canintestini",
    "strain_count": "4", "corroborated_by": ""}}, {"row": 431, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "18", "taxon_id": "NCBITaxon:759",
    "taxon_label": "Pasteurella sp.", "strain_count": "4", "corroborated_by": ""}},
    {"row": 432, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog", "rank":
    "19", "taxon_id": "NCBITaxon:1159213", "taxon_label": "Peptostreptococcus canis",
    "strain_count": "3", "corroborated_by": ""}}, {"row": 433, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "20", "taxon_id": "NCBITaxon:131109",
    "taxon_label": "Actinomyces bowdenii", "strain_count": "3", "corroborated_by":
    ""}}, {"row": 434, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "21", "taxon_id": "NCBITaxon:131112", "taxon_label": "Arcanobacterium
    phocae", "strain_count": "3", "corroborated_by": ""}}, {"row": 435, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "22", "taxon_id": "NCBITaxon:1334",
    "taxon_label": "Streptococcus dysgalactiae", "strain_count": "3", "corroborated_by":
    ""}}, {"row": 436, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "23", "taxon_id": "NCBITaxon:155085", "taxon_label": "Staphylococcus lutrae",
    "strain_count": "3", "corroborated_by": ""}}, {"row": 437, "data": {"bacdive_id":
    "bacdive.isolation_source:canidae-dog", "rank": "24", "taxon_id": "NCBITaxon:52770",
    "taxon_label": "Buchananella hordeovulneris", "strain_count": "3", "corroborated_by":
    ""}}, {"row": 438, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "rank": "25", "taxon_id": "NCBITaxon:100469", "taxon_label": "Schaalia canis",
    "strain_count": "2", "corroborated_by": ""}}]'
  snapshot_sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
- evidence_id: ET6
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: Physical TSV rows 56
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: '[{"row": 56, "data": {"subject_label": "Canidae-Dog", "subject_label_normalized":
    "canidae dog", "object_id": "NCBITaxon:9608", "object_label": "Canidae", "object_source":
    "NCBITaxon", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification":
    "semapv:LexicalMatching", "curator": "ols4_auto", "source_dataset": "bacdive",
    "verified_date": "2026-05-01"}}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: ET7
  kind: database
  reference: data/raw/bacdive_isolation_sources.tsv
  locator: Physical TSV rows 42
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: '[{"row": 42, "data": {"bacdive_id": "bacdive.isolation_source:canidae-dog",
    "label": "Canidae-Dog", "source_slug": "canidae-dog", "strain_count": "344", "taxon_count":
    "139"}}]'
  snapshot_sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 6797
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: '[{"row": 6797, "data": {"subject": "ENVO:01001002", "predicate": "rdfs:subClassOf",
    "object": "ENVO:01001000"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET9
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 8491,10766
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: '[{"row": 8491, "data": {"term_id": "ENVO:01001002", "ontology": "ENVO",
    "label": "animal-associated environment", "definition": "An environmental system
    determined by an animal.", "synonyms": "Metazoan-associated environment|animal
    environment", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}},
    {"row": 10766, "data": {"term_id": "NCBITaxon:9608", "ontology": "NCBITaxon",
    "label": "Canidae", "definition": "", "synonyms": "", "deprecated": "", "directly_referenced":
    "TRUE", "label_only": "TRUE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET10
  kind: database
  reference: curation/term_requests.tsv
  locator: Physical TSV rows 45
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: '[{"row": 45, "data": {"identifier": "habitatmech:BACDIVE.33fde10528",
    "requested_label": "canid-associated environment", "parent_class": "ENVO:01001002",
    "parent_label": "animal-associated environment", "definition": "An animal-associated
    environment which is determined by a dog or other canid.", "exact_synonym": "Canidae-Dog",
    "curator": "claude-opus-5", "date": "2026-08-26", "notes": "Definition follows
    the established <clade>-associated environment family for BacDive host buckets,
    whose naming rule the corpus already fixes: a -inae source label yields -ine (Bovinae-Cow,-Cattle
    -> bovine) and a -idae source label yields -id (Equidae-Horse -> equid, Leporidae-Rabbit/Hare
    -> leporid, Suidae-Pig,Swine -> suid). No deep-research run was commissioned:
    the genus, the wording pattern and the near-miss reasoning are already settled
    by those five siblings and by NCBITaxon, so a billed report would add nothing
    this slice turns on. Worded like the equid sibling because the source label names
    one vernacular host inside a wider family: NCBITaxon:9608 ''Canidae'' also covers
    foxes, wolves and jackals, so the definition must not silently narrow to the dog.",
    "parent_mode": "ADD"}}]'
  snapshot_sha256: da5dcc7d49a3441bd9ff25d95ff204ba4e8716cf062271338ee2795ca16a5ce4
- evidence_id: ET11
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 1815
  accessed_at: '2026-10-15T19:30:37Z'
  support: supports
  summary: '[{"row": 1815, "data": {"identifier": "habitatmech:BACDIVE.33fde10528",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "NCBITaxon:9608", "object_label":
    "Canidae", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-26",
    "notes": "Host-taxon reversal (#114) reaching the last members of its own family
    (#194): this was NOT_APPLICABLE, which asserts the source concept is not a habitat.
    An organism acting as a host IS a habitat, and the corpus already says so for
    bovine, caprine, equid, leporid and suid, all minted with ENVO:01001002 ''animal-associated
    environment'' as parent and the organism term as an xref. Never curated on the
    question at all: the NOT_APPLICABLE was the seeder''s automatic bacdive_non_habitat_target
    route firing on an NCBITaxon target, and #114''s sweep did not reach this row.
    The taxon term is not the identity - a family is a class of organisms, not a place
    - so it stays an xref (#99) and the concept keeps its minted identity with a term
    request. Category HOST_ASSOCIATED: the host is living.", "review_depth": "ITEM",
    "category": "HOST_ASSOCIATED", "relation": "xref"}}]'
  snapshot_sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
- evidence_id: EP12
  kind: record_content
  reference: data/habitats/other/animal_associated_environment.yaml
  locator: Entire immediate parent record; context only
  accessed_at: '2026-10-15T19:30:37Z'
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
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/ncbitaxon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCBITaxon_9608/graph
  locator: NCBITaxon_9608-graph.json
  accessed_at: '2026-10-15T19:06:20Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/NCBITaxon_9608",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_379584", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 0b6fe61c7f4013702ff778ca8b36d1cac9ed0b722b79945d40544fbad5d5219c
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/ncbitaxon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FNCBITaxon_9608
  locator: NCBITaxon_9608.json
  accessed_at: '2026-10-15T19:06:19Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "NCBITaxon:9608", "label": "Canidae", "is_obsolete": false, "description": []}'
  snapshot_sha256: 188f8f82f2333d8b4405ec4c0ce0e1a666d7d3bdc4124c8478d400e7002299a7
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
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=100469,1015,108028,1085628,1159213,1163745,1205679,131109,131112,1329,1330043,1334,1392869,1417985,155085,1580,1661,170187,1719,184914,1872627,1962667,197,2,206,243265,243273,28080,28091,28121,28188,283734,28450,28898,29419,317010,326522,33,34,35,38,388919,398527,52770,54,554290,557433,56,562,590061,694433,71864,722,731,753,754,759,75985,760,82806,83456,83462,85336,85401,90240,99807&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T19:06:42Z'
  support: context_only
  summary: 'Current NCBI TaxIds, names and source-label comparison: [{"id": "NCBITaxon:28091",
    "source": "BACDIVE", "label": "Neisseria weaveri", "current_id": "28091", "current_name":
    "Neisseria weaveri", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:28080", "source": "BACDIVE", "label": "Campylobacter
    upsaliensis", "current_id": "28080", "current_name": "Campylobacter upsaliensis",
    "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:754",
    "source": "BACDIVE", "label": "Pasteurella dagmatis", "current_id": "754", "current_name":
    "Pasteurella dagmatis", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1015", "source": "BACDIVE", "label": "Bergeyella zoohelcum",
    "current_id": "1015", "current_name": "Bergeyella zoohelcum", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:2", "source":
    "BACDIVE", "label": "Bacteria", "current_id": "2", "current_name": "Bacteria",
    "rank": "domain", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28188",
    "source": "BACDIVE", "label": "Capnocytophaga canimorsus", "current_id": "28188",
    "current_name": "Capnocytophaga canimorsus", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:753", "source": "BACDIVE",
    "label": "Pasteurella canis", "current_id": "753", "current_name": "Pasteurella
    canis", "rank": "species", "direct_match": true, "recognized_alias": true}, {"id":
    "NCBITaxon:760", "source": "BACDIVE", "label": "Pasteurella stomatis", "current_id":
    "760", "current_name": "Pasteurella stomatis", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:85336", "source": "BACDIVE",
    "label": "Rothia nasimurium", "current_id": "85336", "current_name": "Rothia nasimurium",
    "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:197",
    "source": "BACDIVE", "label": "Campylobacter jejuni", "current_id": "197", "current_name":
    "Campylobacter jejuni", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:283734", "source": "BACDIVE", "label": "Staphylococcus
    pseudintermedius", "current_id": "283734", "current_name": "Staphylococcus pseudintermedius",
    "rank": "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:326522",
    "source": "BACDIVE", "label": "Neisseria animaloris", "current_id": "326522",
    "current_name": "Neisseria animaloris", "rank": "species", "direct_match": true,
    "recognized_alias": true}, {"id": "NCBITaxon:99807", "source": "BACDIVE", "label":
    "Corynebacterium auriscanis", "current_id": "99807", "current_name": "Corynebacterium
    auriscanis", "rank": "species", "direct_match": true, "recognized_alias": true},
    {"id": "NCBITaxon:1329", "source": "BACDIVE", "label": "Streptococcus canis",
    "current_id": "1329", "current_name": "Streptococcus canis", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:28898", "source":
    "BACDIVE", "label": "Campylobacter helveticus", "current_id": "28898", "current_name":
    "Campylobacter helveticus", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:29419", "source": "BACDIVE", "label": "Helicobacter canis",
    "current_id": "29419", "current_name": "Helicobacter canis", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:317010", "source":
    "BACDIVE", "label": "Enterococcus canintestini", "current_id": "317010", "current_name":
    "Enterococcus canintestini", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:759", "source": "BACDIVE", "label": "Pasteurella sp.",
    "current_id": "759", "current_name": "Pasteurella sp.", "rank": "species", "direct_match":
    true, "recognized_alias": true}, {"id": "NCBITaxon:1159213", "source": "BACDIVE",
    "label": "Peptostreptococcus canis", "current_id": "1159213", "current_name":
    "Peptostreptococcus canis", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:131109", "source": "BACDIVE", "label": "Actinomyces bowdenii",
    "current_id": "131109", "current_name": "Actinomyces bowdenii", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:131112", "source":
    "BACDIVE", "label": "Arcanobacterium phocae", "current_id": "131112", "current_name":
    "Arcanobacterium phocae", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:1334", "source": "BACDIVE", "label": "Streptococcus dysgalactiae",
    "current_id": "1334", "current_name": "Streptococcus dysgalactiae", "rank": "species",
    "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:155085", "source":
    "BACDIVE", "label": "Staphylococcus lutrae", "current_id": "155085", "current_name":
    "Staphylococcus lutrae", "rank": "species", "direct_match": true, "recognized_alias":
    true}, {"id": "NCBITaxon:52770", "source": "BACDIVE", "label": "Buchananella hordeovulneris",
    "current_id": "52770", "current_name": "Buchananella hordeovulneris", "rank":
    "species", "direct_match": true, "recognized_alias": true}, {"id": "NCBITaxon:100469",
    "source": "BACDIVE", "label": "Schaalia canis", "current_id": "100469", "current_name":
    "Schaalia canis", "rank": "species", "direct_match": true, "recognized_alias":
    true}]'
  snapshot_sha256: ea5036b7cc5c9bf152840fae0a470b8f6cb17f89633967069648541712ecf8b2
- evidence_id: ESEARCH
  kind: search
  reference: Maintained inputs and local structured archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:BACDIVE.33fde10528 -e 'canid-associated
    environment' -e canidae_dog -e habitatmech:BACDIVE.33fde10528 curation history
    research reports data/raw build reviews
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
  summary: The minted canid-associated environment, animal-associated genus and Canidae
    taxon xref preserve host versus habitat identity. The exact synonym Canidae-Dog
    incorrectly equates a host category with its environment. All 344 STRAIN assertions
    and 25 displayed taxa from a 139-taxon pool remain source evidence, not a universal
    dog microbiome or proof of domestic-dog-only scope.
  target_ids:
  - habitatmech:BACDIVE.33fde10528
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
    source row. [{"source": "BACDIVE", "count": 344, "unit": "STRAIN"}]. Side-table
    biosamples and study memberships are separate from tree ORGANISM counts; zero-count
    omission is not biological absence.'
  target_ids:
  - habitatmech:BACDIVE.33fde10528
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
  dimensions:
  - name: source_assertion_units
    value: '[{"source": "BACDIVE", "count": 344, "unit": "STRAIN"}]'
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
  summary: The minted canid-associated environment, animal-associated genus and Canidae
    taxon xref preserve host versus habitat identity. The exact synonym Canidae-Dog
    incorrectly equates a host category with its environment. All 344 STRAIN assertions
    and 25 displayed taxa from a 139-taxon pool remain source evidence, not a universal
    dog microbiome or proof of domestic-dog-only scope.
  target_ids:
  - habitatmech:BACDIVE.33fde10528
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
- assessment_id: A4
  area: completeness
  topic: Curation status, parameters, mechanisms and optional content
  outcome: supported
  summary: Executed routes reproduce UNGROUNDED/REVIEWED. No target environmental
    parameters, causal edges, discussions/datasets or is_characteristic=true assertions
    are present. Parent-record mechanisms are not inherited. Optional absence and
    SEEDED status alone are not defects.
  target_ids:
  - habitatmech:BACDIVE.33fde10528
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
  - habitatmech:BACDIVE.33fde10528
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: canidae-dog-host-alias
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Whole-host label is an exact environment synonym
  description: Remove authored exact synonym Canidae-Dog and guard definition-source-label
    fallback from reintroducing it. Preserve the verbatim source attestation, minted
    habitat identity, supported definition and host xrefs.
  target_ids:
  - habitatmech:BACDIVE.33fde10528
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
  - habitatmech:BACDIVE.33fde10528
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Remove authored exact synonym Canidae-Dog and guard definition-source-label
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
