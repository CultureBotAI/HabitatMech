# Record review: axilla (UBERON:0009472)

- Review: 20261015T093737Z-axilla-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T09:23:18Z
- Finished UTC: 2026-10-15T09:37:37Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole axilla is an external soft-tissue zone, not a subtype of human Skin. The valid ontology parent should remain while source-specific skin-versus-region meaning is reassessed. Four related UBERON aliases are also incorrectly promoted to exact; axillary region has independent exact support.

## Scope And Provenance

Scientific review of one exact target at bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.

Selection: Next twenty unreviewed records in corpus path order; this bundle assesses exactly one of their resolved identifiers.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0009472 | data/habitats/host_associated/axilla.yaml | generated | axilla |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | UBERON:0009472 | Completed 2026-10-15T09:23:47Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/axilla.yaml |
| validate-strict | passed | True | UBERON:0009472 | Completed 2026-10-15T09:25:01Z. uv run python scripts/validate_strict.py data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | UBERON:0009472 | Completed 2026-10-15T09:25:13Z. No issues found<br>777 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | UBERON:0009472 | Completed 2026-10-15T09:25:14Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | UBERON:0009472 | Completed 2026-10-15T09:25:35Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | UBERON:0009472 | Completed 2026-10-15T09:25:40Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | UBERON:0009472 | Completed 2026-10-15T09:26:00Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | UBERON:0009472 | Completed 2026-10-15T09:26:58Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-revision baseline full QC | passed | True | UBERON:0009472 | Required full native QC and structured-review contract succeeded at the exact captured revision; status checked 2026-10-15T09:25:51Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38709434919 |

## Scientific And Domain Assessments

### Native validators and reproduction

schema: supported. Targets: UBERON:0009472.

Individual schema, twenty-target strict validation, 777 history records, 14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110 term requests passed. This establishes deterministic fidelity, not scientific validity.

### Identity, definition, hierarchy and synonym scope

identity: concern. Targets: UBERON:0009472.

Whole axilla is an external soft-tissue zone, not a subtype of human Skin. The valid ontology parent should remain while source-specific skin-versus-region meaning is reassessed. Four related UBERON aliases are also incorrectly promoted to exact; axillary region has independent exact support.

### Counts, units and ranking provenance

quantity: supported. Targets: UBERON:0009472.

Exact source rows reproduce [{"source": "GOLD", "count": 4, "unit": "ORGANISM"}]. Every displayed taxon ID/name resolves in NCBI; ranks and pools reproduce the exact habitat-keyed rows. Tied PREGO score/direct flags are ordered by taxon ID, not abundance. Zero tree counts do not imply microbial absence or erase different bulk counts.

### Source status and optional claims

completeness: supported. Targets: UBERON:0009472.

Full routes reproduce EXACT/REVIEWED. Optional parameter, mechanism and characteristic-presence claims are not asserted and are not required quotas. Source parent counts, triad annotations and adjacent records are not inherited observations.

## Findings

### F1: Source context is asserted as a strictly broader habitat

major / open / confirmed; issue key: axilla-source-parent.

The whole axillary region includes deeper structures and is not a kind of skin. Guard and exclude only the exact GOLD contribution habitatmech:GOLD.4b37ab4b76 in gold_parent_exclusions.tsv. Preserve the source path and independently valid parents; separately reassess source meaning before adding another genus.

### F2: Related ontology aliases are emitted as exact

major / open / confirmed; issue key: axilla-ontology-synonym-scope.

Use guarded record_annotation_corrections.tsv rows to change only the UBERON armpits, axillae, oxter and underarm annotations from EXACT_SYNONYM to RELATED_SYNONYM. Preserve independent exact aliases, canonical identity and source labels. The shared extractor/seeder scope loss remains #1249; a bounded correction does not repair every ontology synonym.

## Recommended Actions And Acceptance Checks

### ACT1

The whole axillary region includes deeper structures and is not a kind of skin. Guard and exclude only the exact GOLD contribution habitatmech:GOLD.4b37ab4b76 in gold_parent_exclusions.tsv. Preserve the source path and independently valid parents; separately reassess source meaning before adding another genus. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Use guarded record_annotation_corrections.tsv rows to change only the UBERON armpits, axillae, oxter and underarm annotations from EXACT_SYNONYM to RELATED_SYNONYM. Preserve independent exact aliases, canonical identity and source labels. The shared extractor/seeder scope loss remains #1249; a bounded correction does not repair every ontology synonym. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/axilla.yaml; Entire YAML | supports | Read the complete target including source path, fields, taxonomy and generated history. |
| ERULE | docs/CURATION.md; Host identity, broader parents and maintained ownership | supports | Whole organisms cannot identify associated environments; parent_habitats requires strictly broader habitat meaning. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon | supports | Source-to-record mapping endpoints, broader habitat relations and observed versus characteristic presence are distinct. |
| ESEED | src/habitatmech/seed.py; Native executed resolution route | supports | Executed native route and final decision: [{"source": "GOLD", "mint": "habitatmech:GOLD.383b9034af", "automatic": {"identifier": "habitatmech:GOLD.383b9034af", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0009472", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_ground_from_gold_unmatched", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.383b9034af", "decision": "GROUND", "object_id": "UBERON:0009472", "object_label": "axilla", "grounding_status": "EXACT", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Variant-match review (#12): the seeder grounds on exact labels only, so GOLD's slash and plural conventions hid a term that says exactly this. Axilla is the armpit, and the path is Human &gt; Integumentary system &gt; Skin. Path: Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Skin &gt; Axilla/Armpit", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; extract_prego | supports | Projection deduplicates pairs, preserves best score/channel, uses score/directness/taxon-ID order and retains a full distinct-taxon pool. Original pair citations are not emitted into this committed projection. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; TSV physical rows 685 | supports | [{"row": 685, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Skin &gt; Axilla/Armpit", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_type": "Integumentary system", "ecosystem_subtype": "Skin", "specific_ecosystem": "Axilla/Armpit", "leaf_label": "Axilla/Armpit", "depth": "5", "gold_node_count": "1", "organism_count": "4", "study_count": "0", "biosample_count": "0", "total_assertions": "4", "gold_node_ids": "gold.ecosystem:6117"}}] |
| ET6 | data/raw/gold_path_biosamples.tsv; TSV physical rows 274 | supports | [{"row": 274, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Skin &gt; Axilla/Armpit", "ecosystem_path_id": "6117", "biosample_count": "79"}}] |
| ET7 | data/raw/gold_studies.tsv; TSV physical rows 487,3828 | supports | Exact membership in 2 study path lists. These are not additive with tree-organism or bulk-biosample counts. |
| ET8 | data/raw/ontology_subclass_edges.tsv; TSV physical rows 11666,11826,11827 | supports | [{"row": 11666, "data": {"subject": "UBERON:0009472", "predicate": "rdfs:subClassOf", "object": "UBERON:0034929"}}, {"row": 11826, "data": {"subject": "UBERON:0034929", "predicate": "rdfs:subClassOf", "object": "UBERON:0010000"}}, {"row": 11827, "data": {"subject": "UBERON:0034929", "predicate": "rdfs:subClassOf", "object": "UBERON:0010314"}}] |
| ET9 | data/raw/ontology_terms.tsv; TSV physical rows 13375,13504 | supports | [{"row": 13375, "data": {"term_id": "UBERON:0009472", "ontology": "UBERON", "label": "axilla", "definition": "The axilla is the area directly under the joint where the forelimb connects to the shoulder.", "synonyms": "arm pit&#124;armpit&#124;armpits&#124;axilla&#124;axillae&#124;axillary region&#124;oxter&#124;regio axillaris&#124;underarm", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 13504, "data": {"term_id": "UBERON:0034929", "ontology": "UBERON", "label": "external soft tissue zone", "definition": "A region or zone on the surface of an organism that encompasses skin and any adnexa, down through muscles and bounded by underlying skeletal support structures.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET10 | curation/decisions.tsv; TSV physical rows 1656 | supports | [{"row": 1656, "data": {"identifier": "habitatmech:GOLD.383b9034af", "decision": "GROUND", "object_id": "UBERON:0009472", "object_label": "axilla", "grounding_status": "EXACT", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Variant-match review (#12): the seeder grounds on exact labels only, so GOLD's slash and plural conventions hid a term that says exactly this. Axilla is the armpit, and the path is Human &gt; Integumentary system &gt; Skin. Path: Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Skin &gt; Axilla/Armpit", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP11 | data/habitats/host_associated/external_soft_tissue_zone.yaml; Direct parent scope, not an additional target review | supports | {"identifier": "UBERON:0034929", "label": "external soft tissue zone", "definition": "A region or zone on the surface of an organism that encompasses skin and any adnexa, down through muscles and bounded by underlying skeletal support structures.", "grounding_status": "CLOSE", "parent_habitats": ["UBERON:0010000", "UBERON:0010314", "habitatmech:GOLD.68a62625da"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6880", "source_label": "Soft tissue", "source_path": "Host-associated &gt; Mammals &gt; Multiple systems &gt; Soft tissue", "mapping_predicate": "skos:closeMatch", "assertion_count": 38, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]} |
| EP12 | data/habitats/host_associated/skin__621b7871.yaml; Direct parent scope, not an additional target review | supports | {"identifier": "habitatmech:GOLD.4b37ab4b76", "label": "Skin", "grounding_status": "NARROW", "parent_habitats": ["BTO:0001253", "habitatmech:GOLD.dc86c8917c"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6114", "source_label": "Skin", "source_path": "Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Skin", "mapping_predicate": "skos:narrowMatch", "assertion_count": 754, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001253/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0001253", "target": "http://purl.obolibrary.org/obo/BTO_0000634", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001253; Canonical term identity, definition and explicit relation types | supports | BTO:0001253 skin; inspected definition and typed scope. ["The integument of an animal (as a fur-bearing mammal or a bird) separated from the body usually with its hair or feathers."] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_08000001/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_08000001", "target": "http://purl.obolibrary.org/obo/ENVO_2100003", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_08000001", "target": "http://purl.obolibrary.org/obo/UBERON_0015474", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_08000001; Canonical term identity, definition and explicit relation types | supports | ENVO:08000001 axilla skin environment; inspected definition and typed scope. ["An environment that is determined by an axilla skin."] |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10862185/fullTextXML; Materials and methods: anatomical dissection | supports | PMID:37965841; DOI:10.1111/joa.13976. The investigators removed covering skin before exposing the axillary region and neurovascular structures in 400 axillae from 200 donors. This supports the whole-region versus skin distinction; no clinical prevalence claim is adopted. |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009472/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0009472", "target": "http://purl.obolibrary.org/obo/UBERON_0034929", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0009472", "target": "http://purl.obolibrary.org/obo/UBERON_0001421", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX7 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009472; Canonical term identity, definition and explicit relation types | supports | UBERON:0009472 axilla; inspected definition and typed scope. ["The axilla is the area directly under the joint where the forelimb connects to the shoulder."] Typed synonyms: [{"name": "arm pit", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]}, {"name": "armpit", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]}, {"name": "axillary region", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "FMA", "id": "24864", "description": null, "url": "http://purl.org/sig/ont/fma/24864"}]}, {"name": "regio axillaris", "scope": "hasExactSynonym", "type": "latin term", "xrefs": [{"database": "FMA", "id": "TA", "description": null, "url": null}]}, {"name": "armpits", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]}, {"name": "axilla", "scope": "hasRelatedSynonym", "type": "latin term", "xrefs": [{"database": "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]}, {"name": "axillae", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]}, {"name": "axillary region", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]}, {"name": "oxter", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]}, {"name": "underarm", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]}] |
| EX8 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010000/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0010000", "target": "http://purl.obolibrary.org/obo/UBERON_0000061", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0010000", "target": "http://purl.obolibrary.org/obo/CL_0000000", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0010000", "target": "http://purl.obolibrary.org/obo/PATO_0001993", "uri": "http://purl.obolibrary.org/obo/RO_0000086", "label": "has quality"}] |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010000; Canonical term identity, definition and explicit relation types | supports | UBERON:0010000 multicellular anatomical structure; inspected definition and typed scope. ["An anatomical structure that has more than one cell as a part."] |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010314/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0010314", "target": "http://purl.obolibrary.org/obo/UBERON_0000061", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0010314", "target": "http://purl.obolibrary.org/obo/UBERON_0002342", "uri": "http://purl.obolibrary.org/obo/RO_0002254", "label": "has developmental contribution from"}] |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010314; Canonical term identity, definition and explicit relation types | supports | UBERON:0010314 structure with developmental contribution from neural crest; inspected definition and typed scope. ["An anatomical structure that has some part that develops from the neural crest."] |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0015474/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0015474", "target": "http://purl.obolibrary.org/obo/UBERON_8480025", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0015474", "target": "http://purl.obolibrary.org/obo/UBERON_0009472", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0015474; Canonical term identity, definition and explicit relation types | supports | UBERON:0015474 axilla skin; inspected definition and typed scope. ["A zone of skin that is part of a axilla."] |
| EX14 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0034929/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0010000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0010314", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0000014", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0000475", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0001015", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0001021", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0002049", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}] |
| EX15 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0034929; Canonical term identity, definition and explicit relation types | supports | UBERON:0034929 external soft tissue zone; inspected definition and typed scope. ["A region or zone on the surface of an organism that encompasses skin and any adnexa, down through muscles and bounded by underlying skeletal support structures."] |
| EX16 | https://purl.obolibrary.org/obo/uberon/uberon-base.owl; Direct OWL class annotations for UBERON:0009472 | supports | Official OWL types armpits, axillae, oxter and underarm as related; arm pit, armpit and regio axillaris are exact; axillary region has both exact and related assertions. Preserve the supported exact assertion. |
| ESEARCH | Local records and maintained inputs; rg --no-ignore --hidden -l -F -e UBERON:0009472 -e axilla -e axilla -e habitatmech:GOLD.383b9034af curation history research reports data/raw build reviews | context_only | Identifier, label, slug and minted-source search includes hidden and ignored files; parsed structured archive traversal found no target predecessor. Broad text hits are not treated as exact source associations. |
| ELEGACY | reports/yaml_record_review/20261004T091231Z-axilla.md; Historical target review, especially findings and evidence leads | supports | Historical assessment was consulted for source and issue leads; current findings are independently reassessed against the captured inputs and stated authorities. It is not structured predecessor lineage. |

## Limits And Additional Notes

- Source counts, PREGO scores and rank are not prevalence, viability, mechanism or characteristic presence. Every historical specimen has not been independently reidentified.
- Configured label correspondence skipped 2,061 pairs without adapters; it is not full identifier or semantic certification.
- Baseline full QC is exact-revision CI evidence, not a new local full-QC execution. The post-save archive gate is subsequent and is not claimed passed inside this observation.
- Only stated source passages were assessed. Historical reports provide leads, not independent approval; optional empty fields do not create automatic deficiencies.
- iModulonDB is not applicable because the target asserts no gene, regulator or expression module. No paid research, curation, native-status promotion or GitHub mutation was performed.
- Fresh captures were made at current main after the previous publication; earlier scratch captures were not refreshed or reused as provenance.
- All captured bytes match both current files and the exact Git revision. The extractor has a separate native supplemental capture.
- Ignored-inclusive traversal found no structured predecessor targeting this identifier. Legacy Markdown observations are contextual; no earlier structured finding is silently closed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T093737Z-axilla-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: axilla (UBERON:0009472)'
started_at: '2026-10-15T09:23:18Z'
finished_at: '2026-10-15T09:37:37Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent performed evidence inspection; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole axilla is an external soft-tissue zone, not a subtype of human Skin.
  The valid ontology parent should remain while source-specific skin-versus-region
  meaning is reassessed. Four related UBERON aliases are also incorrectly promoted
  to exact; axillary region has independent exact support.
source:
  git_revision: bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d
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
    sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: ee710783b625e34dcfa822afab0008e4bfe6b2daf3224b5f804fe569dccb26fb
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 5a794902f1338c3206cb43900e310ef7d573fcbff61da4a01d77bb43b6677c48
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 6af1d1e372e4400f3caf58808eeb508d3436c2ee1ae7a897c4a23e434093d455
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 70656ba3c46b4d72fd44cb0ef83322c2c4591edbc3501a9fb7d1497aaeab67a6
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
  - path: data/habitats/host_associated/axilla.yaml
    sha256: b5aadf31f15fed0667ca80e29f5c9badd2a722cc92f05ac360cdb08f8c76eca7
    role: target
  - path: data/habitats/host_associated/external_soft_tissue_zone.yaml
    sha256: 650a682ac2bed4df0c332ada09c4f39d4a9459ced13ef03de87d4b338174b41e
    role: context
  - path: data/habitats/host_associated/skin__621b7871.yaml
    sha256: f12724659d174beaa094e833cb08c0d39c695e0ac9be63f4f072ae4c32a62ebf
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
  - path: reports/yaml_record_review/20261004T091231Z-axilla.md
    sha256: 4ee1449f32be90e8d907c64ced9b826ed79ff74016b0b888925a031c7aca522a
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
- target_id: UBERON:0009472
  path: data/habitats/host_associated/axilla.yaml
  label: axilla
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
  description: Scientific review of one exact target at bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.
  selection: Next twenty unreviewed records in corpus path order; this bundle assesses
    exactly one of their resolved identifiers.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0009472
  exclusions:
  - target: Other records, exports and parent-record reviews
    reason: Parent context informs this review but is not counted as additional reviewed
      coverage; SSSOM/KGX readiness is not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/axilla.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0009472
  summary: "Completed 2026-10-15T09:23:47Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/axilla.yaml"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml
    data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml
    data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml
    data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml
    data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml
    data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml
    data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml
    data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml
    data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml
    data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0009472
  summary: "Completed 2026-10-15T09:25:01Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml\
    \ data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml\
    \ data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml\
    \ data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml\
    \ data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml\
    \ data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml\
    \ data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml\
    \ data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml\
    \ data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml\
    \ data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml\n\
    Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0009472
  summary: 'Completed 2026-10-15T09:25:13Z. No issues found

    777 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0009472
  summary: "Completed 2026-10-15T09:25:14Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0009472
  summary: "Completed 2026-10-15T09:25:35Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0009472
  summary: "Completed 2026-10-15T09:25:40Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0009472
  summary: "Completed 2026-10-15T09:26:00Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0009472
  summary: "Completed 2026-10-15T09:26:58Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: CCI
  name: Exact-revision baseline full QC
  status: passed
  required: true
  command: gh run view 38709434919 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0009472
  summary: Required full native QC and structured-review contract succeeded at the
    exact captured revision; status checked 2026-10-15T09:25:51Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38709434919
  scope_note: Remote baseline execution; newly saved review outputs require their
    own archive check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/axilla.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Read the complete target including source path, fields, taxonomy and generated
    history.
  snapshot_sha256: b5aadf31f15fed0667ca80e29f5c9badd2a722cc92f05ac360cdb08f8c76eca7
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, broader parents and maintained ownership
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Whole organisms cannot identify associated environments; parent_habitats
    requires strictly broader habitat meaning.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Source-to-record mapping endpoints, broader habitat relations and observed
    versus characteristic presence are distinct.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Native executed resolution route
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: 'Executed native route and final decision: [{"source": "GOLD", "mint":
    "habitatmech:GOLD.383b9034af", "automatic": {"identifier": "habitatmech:GOLD.383b9034af",
    "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category":
    null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0009472",
    "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "curated_ground_from_gold_unmatched",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.383b9034af",
    "decision": "GROUND", "object_id": "UBERON:0009472", "object_label": "axilla",
    "grounding_status": "EXACT", "curator": "claude-opus-5", "date": "2026-08-16",
    "notes": "Variant-match review (#12): the seeder grounds on exact labels only,
    so GOLD''s slash and plural conventions hid a term that says exactly this. Axilla
    is the armpit, and the path is Human > Integumentary system > Skin. Path: Host-associated
    > Mammals: Human > Integumentary system > Skin > Axilla/Armpit", "review_depth":
    "ITEM", "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Projection deduplicates pairs, preserves best score/channel, uses score/directness/taxon-ID
    order and retains a full distinct-taxon pool. Original pair citations are not
    emitted into this committed projection.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV physical rows 685
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '[{"row": 685, "data": {"canonical_path": "Host-associated > Mammals: Human
    > Integumentary system > Skin > Axilla/Armpit", "ecosystem": "Host-associated",
    "ecosystem_category": "Mammals: Human", "ecosystem_type": "Integumentary system",
    "ecosystem_subtype": "Skin", "specific_ecosystem": "Axilla/Armpit", "leaf_label":
    "Axilla/Armpit", "depth": "5", "gold_node_count": "1", "organism_count": "4",
    "study_count": "0", "biosample_count": "0", "total_assertions": "4", "gold_node_ids":
    "gold.ecosystem:6117"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/gold_path_biosamples.tsv
  locator: TSV physical rows 274
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '[{"row": 274, "data": {"canonical_path": "Host-associated > Mammals: Human
    > Integumentary system > Skin > Axilla/Armpit", "ecosystem_path_id": "6117", "biosample_count":
    "79"}}]'
  snapshot_sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
- evidence_id: ET7
  kind: database
  reference: data/raw/gold_studies.tsv
  locator: TSV physical rows 487,3828
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Exact membership in 2 study path lists. These are not additive with tree-organism
    or bulk-biosample counts.
  snapshot_sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV physical rows 11666,11826,11827
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '[{"row": 11666, "data": {"subject": "UBERON:0009472", "predicate": "rdfs:subClassOf",
    "object": "UBERON:0034929"}}, {"row": 11826, "data": {"subject": "UBERON:0034929",
    "predicate": "rdfs:subClassOf", "object": "UBERON:0010000"}}, {"row": 11827, "data":
    {"subject": "UBERON:0034929", "predicate": "rdfs:subClassOf", "object": "UBERON:0010314"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET9
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV physical rows 13375,13504
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '[{"row": 13375, "data": {"term_id": "UBERON:0009472", "ontology": "UBERON",
    "label": "axilla", "definition": "The axilla is the area directly under the joint
    where the forelimb connects to the shoulder.", "synonyms": "arm pit|armpit|armpits|axilla|axillae|axillary
    region|oxter|regio axillaris|underarm", "deprecated": "", "directly_referenced":
    "TRUE", "label_only": "FALSE"}}, {"row": 13504, "data": {"term_id": "UBERON:0034929",
    "ontology": "UBERON", "label": "external soft tissue zone", "definition": "A region
    or zone on the surface of an organism that encompasses skin and any adnexa, down
    through muscles and bounded by underlying skeletal support structures.", "synonyms":
    "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET10
  kind: database
  reference: curation/decisions.tsv
  locator: TSV physical rows 1656
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '[{"row": 1656, "data": {"identifier": "habitatmech:GOLD.383b9034af", "decision":
    "GROUND", "object_id": "UBERON:0009472", "object_label": "axilla", "grounding_status":
    "EXACT", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Variant-match
    review (#12): the seeder grounds on exact labels only, so GOLD''s slash and plural
    conventions hid a term that says exactly this. Axilla is the armpit, and the path
    is Human > Integumentary system > Skin. Path: Host-associated > Mammals: Human
    > Integumentary system > Skin > Axilla/Armpit", "review_depth": "ITEM", "category":
    "", "relation": ""}}]'
  snapshot_sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
- evidence_id: EP11
  kind: record_content
  reference: data/habitats/host_associated/external_soft_tissue_zone.yaml
  locator: Direct parent scope, not an additional target review
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '{"identifier": "UBERON:0034929", "label": "external soft tissue zone",
    "definition": "A region or zone on the surface of an organism that encompasses
    skin and any adnexa, down through muscles and bounded by underlying skeletal support
    structures.", "grounding_status": "CLOSE", "parent_habitats": ["UBERON:0010000",
    "UBERON:0010314", "habitatmech:GOLD.68a62625da"], "source_attestations": [{"source":
    "GOLD", "source_id": "gold.ecosystem:6880", "source_label": "Soft tissue", "source_path":
    "Host-associated > Mammals > Multiple systems > Soft tissue", "mapping_predicate":
    "skos:closeMatch", "assertion_count": 38, "assertion_unit": "ORGANISM", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]}'
  snapshot_sha256: 650a682ac2bed4df0c332ada09c4f39d4a9459ced13ef03de87d4b338174b41e
- evidence_id: EP12
  kind: record_content
  reference: data/habitats/host_associated/skin__621b7871.yaml
  locator: Direct parent scope, not an additional target review
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.4b37ab4b76", "label": "Skin", "grounding_status":
    "NARROW", "parent_habitats": ["BTO:0001253", "habitatmech:GOLD.dc86c8917c"], "source_attestations":
    [{"source": "GOLD", "source_id": "gold.ecosystem:6114", "source_label": "Skin",
    "source_path": "Host-associated > Mammals: Human > Integumentary system > Skin",
    "mapping_predicate": "skos:narrowMatch", "assertion_count": 754, "assertion_unit":
    "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown.
    See data/raw/gold_ecosystem_paths.tsv."}]}'
  snapshot_sha256: f12724659d174beaa094e833cb08c0d39c695e0ac9be63f4f072ae4c32a62ebf
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001253/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:26Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0001253",
    "target": "http://purl.obolibrary.org/obo/BTO_0000634", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: e21351e06776a6d6529b169ab35fcbe1459c546169c5c7f44d68388a102a9204
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001253
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:26Z'
  support: supports
  summary: BTO:0001253 skin; inspected definition and typed scope. ["The integument
    of an animal (as a fur-bearing mammal or a bird) separated from the body usually
    with its hair or feathers."]
  snapshot_sha256: 4cc1bdfc54665947a911db22bbcc8fe146c3f1d7d939f2239f978be28ba13886
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_08000001/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:28:14Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_08000001",
    "target": "http://purl.obolibrary.org/obo/ENVO_2100003", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_08000001",
    "target": "http://purl.obolibrary.org/obo/UBERON_0015474", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: bfd97d97c97a12a17f9ed74e04782ce1a8de6bc65da08fbf0a10487bf5ac1709
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_08000001
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:28:14Z'
  support: supports
  summary: ENVO:08000001 axilla skin environment; inspected definition and typed scope.
    ["An environment that is determined by an axilla skin."]
  snapshot_sha256: e25cd0b8ab4c95a2bd6702e99d13555ec2b6b86acf3327ce083c2705aba2256d
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10862185/fullTextXML
  locator: 'Materials and methods: anatomical dissection'
  accessed_at: '2026-10-15T09:28:31Z'
  support: supports
  summary: PMID:37965841; DOI:10.1111/joa.13976. The investigators removed covering
    skin before exposing the axillary region and neurovascular structures in 400 axillae
    from 200 donors. This supports the whole-region versus skin distinction; no clinical
    prevalence claim is adopted.
  snapshot_sha256: abc47ac83374c4f157af0382f5e34f2e3a6d8991ddbda4b235ca4ea09945dbaf
- evidence_id: EX6
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009472/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:51Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0009472",
    "target": "http://purl.obolibrary.org/obo/UBERON_0034929", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0009472",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001421", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: f856deaccbe72ec0ab84bf84449b687e075e355d998ac47549feb0ed3189e59e
- evidence_id: EX7
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009472
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:50Z'
  support: supports
  summary: 'UBERON:0009472 axilla; inspected definition and typed scope. ["The axilla
    is the area directly under the joint where the forelimb connects to the shoulder."]
    Typed synonyms: [{"name": "arm pit", "scope": "hasExactSynonym", "type": null,
    "xrefs": [{"database": "Wikipedia", "id": "Axilla", "description": null, "url":
    "http://en.wikipedia.org/wiki/Axilla"}]}, {"name": "armpit", "scope": "hasExactSynonym",
    "type": null, "xrefs": [{"database": "Wikipedia", "id": "Axilla", "description":
    null, "url": "http://en.wikipedia.org/wiki/Axilla"}]}, {"name": "axillary region",
    "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "FMA", "id":
    "24864", "description": null, "url": "http://purl.org/sig/ont/fma/24864"}]}, {"name":
    "regio axillaris", "scope": "hasExactSynonym", "type": "latin term", "xrefs":
    [{"database": "FMA", "id": "TA", "description": null, "url": null}]}, {"name":
    "armpits", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database":
    "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]},
    {"name": "axilla", "scope": "hasRelatedSynonym", "type": "latin term", "xrefs":
    [{"database": "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]},
    {"name": "axillae", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database":
    "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]},
    {"name": "axillary region", "scope": "hasRelatedSynonym", "type": null, "xrefs":
    [{"database": "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]},
    {"name": "oxter", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database":
    "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]},
    {"name": "underarm", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database":
    "Wikipedia", "id": "Axilla", "description": null, "url": "http://en.wikipedia.org/wiki/Axilla"}]}]'
  snapshot_sha256: 8a19d722940951882569ddb499a07c3e39ea400045a37adb6ba2a685e7f0b6f9
- evidence_id: EX8
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010000/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:52Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0010000",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000061", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0010000",
    "target": "http://purl.obolibrary.org/obo/CL_0000000", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0010000",
    "target": "http://purl.obolibrary.org/obo/PATO_0001993", "uri": "http://purl.obolibrary.org/obo/RO_0000086",
    "label": "has quality"}]'
  snapshot_sha256: 6bfb42d0c5a3f0d9a35b652d2334d40cf0e7c99db43fb6d386d9aa7d40ae684a
- evidence_id: EX9
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010000
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:51Z'
  support: supports
  summary: UBERON:0010000 multicellular anatomical structure; inspected definition
    and typed scope. ["An anatomical structure that has more than one cell as a part."]
  snapshot_sha256: a91942806b0e4042f9ddbe1c06cceed7c8b5410eda966fc9e736bc09f31ee885
- evidence_id: EX10
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010314/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:55Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0010314",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000061", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0010314",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002342", "uri": "http://purl.obolibrary.org/obo/RO_0002254",
    "label": "has developmental contribution from"}]'
  snapshot_sha256: cada528d45996c53c565cfed754f8b410e38b17dd0d269f0609ef163b94524f6
- evidence_id: EX11
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010314
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:54Z'
  support: supports
  summary: UBERON:0010314 structure with developmental contribution from neural crest;
    inspected definition and typed scope. ["An anatomical structure that has some
    part that develops from the neural crest."]
  snapshot_sha256: 7523cebc75ea8b2067920dff4881e41d1ab9f15364a0c480f9adaf34d5383fb4
- evidence_id: EX12
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0015474/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:28:13Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0015474",
    "target": "http://purl.obolibrary.org/obo/UBERON_8480025", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0015474",
    "target": "http://purl.obolibrary.org/obo/UBERON_0009472", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: c353888de8ad00af06401a088d2182acbfdff97e4f2e9322621a275e59ef012b
- evidence_id: EX13
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0015474
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:28:12Z'
  support: supports
  summary: UBERON:0015474 axilla skin; inspected definition and typed scope. ["A zone
    of skin that is part of a axilla."]
  snapshot_sha256: 94cf5c5338961a4be419d5e6a78e76216ec72d35391dadb5d838f14248429020
- evidence_id: EX14
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0034929/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:59Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0010000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0010314", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000014", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000475", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001015", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001021", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002049", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}]'
  snapshot_sha256: b29546fda916e47b82ba2cde0fc537bba943c7fa7fabacc3024d14e0398afa64
- evidence_id: EX15
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0034929
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:58Z'
  support: supports
  summary: UBERON:0034929 external soft tissue zone; inspected definition and typed
    scope. ["A region or zone on the surface of an organism that encompasses skin
    and any adnexa, down through muscles and bounded by underlying skeletal support
    structures."]
  snapshot_sha256: b14ff3638a856ff89ab4a75e976e0c396b738a6a568159f4f43beea3aac7b4f9
- evidence_id: EX16
  kind: authority
  reference: https://purl.obolibrary.org/obo/uberon/uberon-base.owl
  locator: Direct OWL class annotations for UBERON:0009472
  accessed_at: '2026-10-15T09:28:35Z'
  support: supports
  summary: Official OWL types armpits, axillae, oxter and underarm as related; arm
    pit, armpit and regio axillaris are exact; axillary region has both exact and
    related assertions. Preserve the supported exact assertion.
  snapshot_sha256: e69b77112e073da633d60b20aeec48dfc70eca98d7500707bbb3b43bcef2971c
- evidence_id: ESEARCH
  kind: search
  reference: Local records and maintained inputs
  locator: rg --no-ignore --hidden -l -F -e UBERON:0009472 -e axilla -e axilla -e
    habitatmech:GOLD.383b9034af curation history research reports data/raw build reviews
  accessed_at: '2026-10-15T09:24:07Z'
  support: context_only
  summary: Identifier, label, slug and minted-source search includes hidden and ignored
    files; parsed structured archive traversal found no target predecessor. Broad
    text hits are not treated as exact source associations.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    filesystem traversal of every structured review.yaml independent of gitignore.
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20261004T091231Z-axilla.md
  locator: Historical target review, especially findings and evidence leads
  accessed_at: '2026-10-15T09:37:37Z'
  support: supports
  summary: Historical assessment was consulted for source and issue leads; current
    findings are independently reassessed against the captured inputs and stated authorities.
    It is not structured predecessor lineage.
  snapshot_sha256: 4ee1449f32be90e8d907c64ced9b826ed79ff74016b0b888925a031c7aca522a
assessments:
- assessment_id: A1
  area: schema
  topic: Native validators and reproduction
  outcome: supported
  summary: Individual schema, twenty-target strict validation, 777 history records,
    14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110
    term requests passed. This establishes deterministic fidelity, not scientific
    validity.
  target_ids:
  - UBERON:0009472
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and synonym scope
  outcome: concern
  summary: Whole axilla is an external soft-tissue zone, not a subtype of human Skin.
    The valid ontology parent should remain while source-specific skin-versus-region
    meaning is reassessed. Four related UBERON aliases are also incorrectly promoted
    to exact; axillary region has independent exact support.
  target_ids:
  - UBERON:0009472
  evidence_ids:
  - E1
  - ERULE
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
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
- assessment_id: A3
  area: quantity
  topic: Counts, units and ranking provenance
  outcome: supported
  summary: 'Exact source rows reproduce [{"source": "GOLD", "count": 4, "unit": "ORGANISM"}].
    Every displayed taxon ID/name resolves in NCBI; ranks and pools reproduce the
    exact habitat-keyed rows. Tied PREGO score/direct flags are ordered by taxon ID,
    not abundance. Zero tree counts do not imply microbial absence or erase different
    bulk counts.'
  target_ids:
  - UBERON:0009472
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
- assessment_id: A4
  area: completeness
  topic: Source status and optional claims
  outcome: supported
  summary: Full routes reproduce EXACT/REVIEWED. Optional parameter, mechanism and
    characteristic-presence claims are not asserted and are not required quotas. Source
    parent counts, triad annotations and adjacent records are not inherited observations.
  target_ids:
  - UBERON:0009472
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: axilla-source-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Source context is asserted as a strictly broader habitat
  description: The whole axillary region includes deeper structures and is not a kind
    of skin. Guard and exclude only the exact GOLD contribution habitatmech:GOLD.4b37ab4b76
    in gold_parent_exclusions.tsv. Preserve the source path and independently valid
    parents; separately reassess source meaning before adding another genus.
  target_ids:
  - UBERON:0009472
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
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
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1366
- finding_id: F2
  issue_key: axilla-ontology-synonym-scope
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: Related ontology aliases are emitted as exact
  description: 'Use guarded record_annotation_corrections.tsv rows to change only
    the UBERON armpits, axillae, oxter and underarm annotations from EXACT_SYNONYM
    to RELATED_SYNONYM. Preserve independent exact aliases, canonical identity and
    source labels. The shared extractor/seeder scope loss remains #1249; a bounded
    correction does not repair every ontology synonym.'
  target_ids:
  - UBERON:0009472
  field_paths:
  - synonyms
  evidence_ids:
  - E1
  - ERULE
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
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1249
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - UBERON:0009472
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: The whole axillary region includes deeper structures and is not a kind
    of skin. Guard and exclude only the exact GOLD contribution habitatmech:GOLD.4b37ab4b76
    in gold_parent_exclusions.tsv. Preserve the source path and independently valid
    parents; separately reassess source meaning before adding another genus. No repair
    is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history. Do not change
    source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - UBERON:0009472
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Use guarded record_annotation_corrections.tsv rows to change only
    the UBERON armpits, axillae, oxter and underarm annotations from EXACT_SYNONYM
    to RELATED_SYNONYM. Preserve independent exact aliases, canonical identity and
    source labels. The shared extractor/seeder scope loss remains #1249; a bounded
    correction does not repair every ontology synonym. No repair is performed by this
    review.'
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history. Do not change
    source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Source counts, PREGO scores and rank are not prevalence, viability, mechanism or
  characteristic presence. Every historical specimen has not been independently reidentified.
- Configured label correspondence skipped 2,061 pairs without adapters; it is not
  full identifier or semantic certification.
- Baseline full QC is exact-revision CI evidence, not a new local full-QC execution.
  The post-save archive gate is subsequent and is not claimed passed inside this observation.
- Only stated source passages were assessed. Historical reports provide leads, not
  independent approval; optional empty fields do not create automatic deficiencies.
- iModulonDB is not applicable because the target asserts no gene, regulator or expression
  module. No paid research, curation, native-status promotion or GitHub mutation was
  performed.
notes:
- Fresh captures were made at current main after the previous publication; earlier
  scratch captures were not refreshed or reused as provenance.
- All captured bytes match both current files and the exact Git revision. The extractor
  has a separate native supplemental capture.
- Ignored-inclusive traversal found no structured predecessor targeting this identifier.
  Legacy Markdown observations are contextual; no earlier structured finding is silently
  closed.
tags:
- individual-scientific-review
- host-associated
```
