# Remediation review: cortex

- Review: 20261016T062913Z-cortex-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T05:59:21Z
- Finished UTC: 2026-10-16T06:29:13Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed the guarded GOLD context-parent contribution. Identity and native status are unchanged. Source observations and independent genera are preserved. Remaining predecessor findings are explicitly open.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding after bounded repair.

Selection: One of ten repaired targets from the column-through-crown-gall cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ee3b5b9ecb9031a9a59dd7ed87da7c97c55a181f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0001851 | data/habitats/host_associated/cortex.yaml | generated | cortex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/cortex.yaml | passed | True | UBERON:0001851 | Finished 2026-10-16T05:47:41Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cortex.yaml |
| just validate-strict data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml | passed | True | UBERON:0001851 | Finished 2026-10-16T05:47:56Z. uv run python scripts/validate_strict.py data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | UBERON:0001851 | Finished 2026-10-16T05:48:04Z. No issues found<br>836 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | UBERON:0001851 | Finished 2026-10-16T05:48:04Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | UBERON:0001851 | Finished 2026-10-16T05:48:17Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | UBERON:0001851 | Finished 2026-10-16T05:48:21Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | UBERON:0001851 | Finished 2026-10-16T05:48:36Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | UBERON:0001851 | Finished 2026-10-16T05:49:16Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| uv run pytest -q tests/test_conjunctiva_crop_review_repairs.py --no-cov | passed | True | UBERON:0001851 | Finished 2026-10-16T05:49:22Z. ..                                                                       [100%]<br>2 passed in 4.92s |
| uv run ruff check . | passed | True | UBERON:0001851 | Finished 2026-10-16T05:49:22Z. All checks passed! |
| git diff --check | passed | True | UBERON:0001851 | Finished 2026-10-16T05:49:22Z.  |
| just term-requests | passed | True | UBERON:0001851 | Finished 2026-10-16T05:55:54Z. wrote curation/term_requests/envo_robot_template.tsv: 110 ENVO terms from 110 source records<br><br>22 examined-ungrounded record(s) still have no request written. Top by volume:<br>      438  Medical-environment                habitatmech:BACDIVE.5e52ea1bba<br>      228  Fruit-Seed                         habitatmech:BACDIVE.ba016fe448<br>       35  Egg                                habitatmech:BACDIVE.d48ce9485d<br>        5  Caeca: Bacteriome                  habitatmech:GOLD.2d506b9526<br>        3  Abdomen                            habitatmech:GOLD.c6b0b54290<br>        2  Crop                               habitatmech:GOLD.5446ce4c6d<br>        1  Thalassic                          habitatmech:GOLD.3fece6dbf7<br>        1  Crop                               habitatmech:GOLD.57011086ca<br>        0  Subtidal zone sediment             habitatmech:GOLD.785879d721<br>        0  Subterranean lake                  habitatmech:GOLD.937bf682c4<br><br>covered 105842 upstream assertions; 713 still unrequested across 22 record(s); 15 examined and deliberately not asked for<br><br>&#96;created by&#96; is empty: it wants pipe-delimited full ORCID IRIs and this script cannot know them.<br> uv run python scripts/build_term_requests.py |
| just docs-stats | passed | True | UBERON:0001851 | Finished 2026-10-16T05:56:12Z. updated README corpus statistics<br> uv run python scripts/check_docs.py --write |
| just render | passed | True | UBERON:0001851 | Finished 2026-10-16T05:56:38Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 132 term requests -&gt; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages<br> uv run python scripts/render_pages.py |
| just render-check | passed | True | UBERON:0001851 | Finished 2026-10-16T05:57:05Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 132 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpiryd8m6g/site<br>pages/ is in step with the corpus<br> uv run python scripts/render_pages.py --check |
| just redirects-check | passed | True | UBERON:0001851 | Finished 2026-10-16T05:58:39Z. RETIRED.tsv is current (259 redirects)<br> uv run python scripts/build_redirects.py --check |
| uv run ruff check . | passed | True | UBERON:0001851 | Finished 2026-10-16T05:58:39Z. All checks passed! |
| git diff --check | passed | True | UBERON:0001851 | Finished 2026-10-16T05:58:40Z.  |
| Exact-revision hosted authoritative QC and archive contract | passed | True | UBERON:0001851 | Verified 2026-10-16T06:28:52Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38858656719 |

## Scientific And Domain Assessments

### Bounded correction and exact preservation

consistency: supported. Targets: UBERON:0001851.

Removed the guarded GOLD context-parent contribution. Identity and native status are unchanged. Source observations and independent genera are preserved. Remaining predecessor findings are explicitly open.

### Current anatomical identity and hierarchy

identity: concern. Targets: UBERON:0001851.

UBERON:0001851: cortex; EXACT/SEEDED; parents ["UBERON:0000064"]. No replacement anatomical identity or definition is fabricated. Remaining exact-identity findings are not concealed.

### Units, counts and observations

quantity: supported. Targets: UBERON:0001851.

[{"source": "GOLD", "source_id": "gold.ecosystem:8244", "source_label": "Cortex", "source_path": "Host-associated &gt; Plants &gt; Roots &gt; Cortex", "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]. Original source counts/units, taxa, scores and parameters remain unchanged; these are not prevalence measurements.

### Predecessor reconciliation

representation: concern. Targets: UBERON:0001851.

Every previous finding keeps its stable issue key and exact lineage. Removing invalid non-avian matches does not solve global mapping contract #1398.

### Evidence and lifecycle boundaries

completeness: supported. Targets: UBERON:0001851.

Only the two explicit non-avian ITEM decisions change native status. Optional definitions, causal mechanisms and biological absence claims are not invented.

## Findings

### F1: GOLD context is not a strictly broader habitat class

major / resolved / confirmed; issue key: cortex-context-parent.

Removed only the guarded GOLD source-context contribution PO:0009005. Independent parents and every source observation are retained.

Disposition: Removed only the guarded GOLD source-context contribution PO:0009005. Independent parents and every source observation are retained.

### F2: Root-cortex source is not exact generic organ cortex

major / open / confirmed; issue key: cortex-generic-identity.

The whole-root edge is removed, but exact generic cortex identity for the root-cortex source remains unresolved. An explicit identity migration and downstream redirect accounting remain required.

Disposition: The whole-root edge is removed, but exact generic cortex identity for the root-cortex source remains unresolved. An explicit identity migration and downstream redirect accounting remain required.

## Recommended Actions And Acceptance Checks

### ACT2

The sole source is Plants &gt; Roots &gt; Cortex, yet the record claims exact generic UBERON cortex identity and makes that generic organ layer a subtype of the whole plant root. Both the exact identity scope and whole-root parent need correction. Current PO root cortex is a verified candidate, not automatically adopted by this review. Preserve zero-count semantics and the independent organ-part genus pending explicit source-specific identity migration. Assess PO:0000258 against pinned sources and migrate identity through native path/redirect controls, not hand-edited YAML. Proposed work only; no repair or status promotion is performed by this review.

- Regress the exact target claim and preserve valid genera, identifiers, source counts/units and taxon associations. Recover original evidence before deleting a provisional pair; do not decrement frozen totals by hand.
- Record authorized curation history; require schema, strict, provenance, history, label, corpus, site and full QC gates.
- Save an immutable successor with the same issue key and exact predecessor finding identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001/graph; ENVO_01001001-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001001", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001001", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33090", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001; ENVO_01001001.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "ENVO:01001001", "label": "plant-associated environment", "is_obsolete": false, "description": ["An environmental system determined by a green plant."], "obo_synonym": null} |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0000258/graph; PO_0000258-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/PO_0000258", "target": "http://purl.obolibrary.org/obo/PO_0005708", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/PO_0000258", "target": "http://purl.obolibrary.org/obo/PO_0009005", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0000258; PO_0000258.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "PO:0000258", "label": "root cortex", "is_obsolete": false, "description": ["In dicots and gymnosperms, the cortex consists of mainly parenchyma cells. In monocots sclerenchyma develops in addition to parenchyma.", "A portion of cortex (PO:0005708) that is part of a root (PO:0009005)."], "obo_synonym": [{"name": "cortex de la ra&amp;#237z (Spanish, exact)", "scope": "hasExactSynonym", "type": "Spanish synonym (exact)", "xrefs": [{"database": "POC", "id": "Maria_Alejandra_Gandolfo", "description": null, "url": null}]}, {"name": "\u6839\u76ae\u5c64 (Japanese, exact)", "scope": "hasExactSynonym", "type": "Japanese synonym (exact)", "xrefs": [{"database": "NIG", "id": "Yukiko_Yamazaki", "description": null, "url": null}]}]} |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0005708/graph; PO_0005708-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/PO_0005708", "target": "http://purl.obolibrary.org/obo/PO_0025059", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX14 | https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0005708; PO_0005708.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "PO:0005708", "label": "cortex", "is_obsolete": false, "description": ["A maximal portion of ground tissue (PO:0025059) between the vascular system (PO:0000034) and the epidermis (PO:0005679) in a plant."], "obo_synonym": [{"name": "cortex (corteza) (Spanish, exact)", "scope": "hasExactSynonym", "type": "Spanish synonym (exact)", "xrefs": [{"database": "POC", "id": "Maria_Alejandra_Gandolfo", "description": null, "url": null}]}, {"name": "\u76ae\u5c64 (Japanese, exact)", "scope": "hasExactSynonym", "type": "Japanese synonym (exact)", "xrefs": [{"database": "NIG", "id": "Yukiko_Yamazaki", "description": null, "url": null}]}]} |
| EX15 | https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0009005/graph; PO_0009005-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/PO_0009005", "target": "http://purl.obolibrary.org/obo/PO_0025004", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/PO_0009005", "target": "http://purl.obolibrary.org/obo/UBERON_0001062", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/PO_0009005", "target": "http://purl.obolibrary.org/obo/PO_0005029", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/PO_0009005", "target": "http://purl.obolibrary.org/obo/PO_0025025", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX16 | https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0009005; PO_0009005.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "PO:0009005", "label": "root", "is_obsolete": false, "description": ["Roots function in the absorption of water and inorganic nutrients, anchoring the plant body to the substrate and supporting it, storage of food and nutrients, and vegetative reproduction. The roots of most vascular plant species enter into symbiosis with soil-borne microorganisms. Roots are usually positively geotropic and found underground, although there are many exceptions such as the aerial roots of orchids. Roots often form secondary thickening from the root lateral meristem (PO:0006308). Commonly thought of as one of the three basic parts of the plant body, along with the shoot axis (PO:0025029) and leaves (PO:0025034).", "A plant axis (PO:0025004) that lacks shoot axis nodes (PO:0005004) and usually grows indeterminately."], "obo_synonym": [{"name": "ra&amp;#237z (Spanish, exact)", "scope": "hasExactSynonym", "type": "Spanish synonym (exact)", "xrefs": [{"database": "POC", "id": "Maria_Alejandra_Gandolfo", "description": null, "url": null}]}, {"name": "radices (exact, plural)", "scope": "hasExactSynonym", "type": "plural form", "xrefs": [{"database": "FNA", "id": "3c46e84c-23e4-416b-91cd-2f7c42e4b13d", "description": null, "url": null}]}, {"name": "radix (exact)", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "FNA", "id": "e6315684-fc99-4976-b39d-b356c4b7e7fd", "description": null, "url": null}]}, {"name": "\u6839 (Japanese, exact)", "scope": "hasExactSynonym", "type": "Japanese synonym (exact)", "xrefs": [{"database": "NIG", "id": "Yukiko_Yamazaki", "description": null, "url": null}]}, {"name": "climbing root (narrow)", "scope": "hasNarrowSynonym", "type": null, "xrefs": [{"database": "FNA", "id": "bf0ce902-e91c-401a-92a8-26b20142ce5f", "description": null, "url": null}]}]} |
| EX17 | https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0025004/graph; PO_0025004-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/PO_0025004", "target": "http://purl.obolibrary.org/obo/PO_0009008", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX18 | https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0025004; PO_0025004.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "PO:0025004", "label": "plant axis", "is_obsolete": false, "description": ["Includes roots and shoots.", "An axial plant organ (PO:0009008)."], "obo_synonym": [{"name": "eje de la planta (Spanish, exact)", "scope": "hasExactSynonym", "type": "Spanish synonym (exact)", "xrefs": [{"database": "POC", "id": "Maria_Alejandra_Gandolfo", "description": null, "url": null}]}, {"name": "plant axes (exact, plural)", "scope": "hasExactSynonym", "type": "plural form", "xrefs": [{"database": "FNA", "id": "2355281f-ab10-4ae2-a3d8-672cace068a8", "description": null, "url": null}]}, {"name": "\u690d\u7269\u8ef8\uff08\u8ef8\u67f1\uff09 (Japanese, exact)", "scope": "hasExactSynonym", "type": "Japanese synonym (exact)", "xrefs": [{"database": "NIG", "id": "Yukiko_Yamazaki", "description": null, "url": null}]}]} |
| EX19 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000064/graph; UBERON_0000064-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000064", "target": "http://purl.obolibrary.org/obo/UBERON_0010000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX20 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000064; UBERON_0000064.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "UBERON:0000064", "label": "organ part", "is_obsolete": false, "description": ["A multicellular structure that is a part of an organ."], "obo_synonym": [{"name": "cardinal organ part", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "FMA", "id": "82472", "description": null, "url": "http://purl.org/sig/ont/fma/82472"}]}, {"name": "regional part of organ", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "BIRNLEX", "id": "16", "description": null, "url": "http://uri.neuinfo.org/nif/nifstd/birnlex_16"}]}]} |
| EX21 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001062/graph; UBERON_0001062-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001062", "target": "http://purl.obolibrary.org/obo/BFO_0000004", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX22 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001062; UBERON_0001062.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "UBERON:0001062", "label": "anatomical entity", "is_obsolete": false, "description": ["Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species."], "obo_synonym": null} |
| EX23 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001851/graph; UBERON_0001851-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001851", "target": "http://purl.obolibrary.org/obo/UBERON_0000064", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001851", "target": "http://purl.obolibrary.org/obo/UBERON_0000062", "uri": "http://purl.obolibrary.org/obo/RO_0002007", "label": "bounding layer of"}] |
| EX24 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001851; UBERON_0001851.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "UBERON:0001851", "label": "cortex", "is_obsolete": false, "description": ["Outermost layer of an organ[WP]."], "obo_synonym": [{"name": "cortex", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "FMA", "id": "61109", "description": null, "url": "http://purl.org/sig/ont/fma/61109"}]}]} |
| EAFTER | data/habitats/host_associated/cortex.yaml; Entire regenerated target YAML | supports | {"identifier": "UBERON:0001851", "label": "cortex", "definition": "Outermost layer of an organ[WP].", "definition_source": "UBERON", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "cortex of organ", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}], "parent_habitats": ["UBERON:0000064"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:8244", "source_label": "Cortex", "source_path": "Host-associated &gt; Plants &gt; Roots &gt; Cortex", "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: EXACT."}, {"timestamp": "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution PO:0009005 for habitatmech:GOLD.994d82c95b (Host-associated &gt; Plants &gt; Roots &gt; Cortex). Review https://github.com/CultureBotAI/HabitatMech/issues/2229 : Conjunctiva is not an entire visual system; cornea is not an entire eye; cortex is not an entire root; crop is not an entire digestive system, esophagus or foregut; crop contents are not an esophagus. Exclude only exact guarded source-path contributions, retaining independent genera and source observations. This does not settle generic cortex identity or equivalent avian crop sources. Exact target UBERON:0001851. Other identity and mapping findings remain separate."}]} |
| EPREV | reviews/structured/20261016T054408Z-cortex-record/review.yaml; Every immutable baseline finding | supports | Exact predecessor issue keys and findings are reconciled; original inspected source scope is preserved. |
| ETEST | tests/test_conjunctiva_crop_review_repairs.py; Complete full-corpus counterfactual | supports | Exactly ten records differ. The only scientific changes are guarded context-parent removal and two non-avian grounding/predicate/status corrections; source counts, taxa and other fields are invariant. |
| ERULE | docs/CURATION.md; Strict hierarchy, ITEM decisions and source units | supports | Generated artifacts are not edited by hand; native history/status follows exact maintained rows. |
| EH40 | history/mappings/conjunctiva_crop_review_nonavian/2026-10-16T054553Z-codex-gpt-5-64c4ba.yaml; Complete session event | supports | Authorized curation by codex-gpt-5; exact maintained owner and issue retained. |
| EH41 | history/mappings/conjunctiva_crop_review_parents/2026-10-16T054552Z-codex-gpt-5-b09465.yaml; Complete session event | supports | Authorized curation by codex-gpt-5; exact maintained owner and issue retained. |
| EPARENTS | curation/gold_parent_exclusions.tsv; Exact physical TSV rows | supports | [[6, "habitatmech:GOLD.994d82c95b\tHost-associated &gt; Plants &gt; Roots &gt; Cortex\tPO:0009005\tcodex-gpt-5\t2026-10-16\tReview https://github.com/CultureBotAI/HabitatMech/issues/2229 : Conjunctiva is not an entire visual system; cornea is not an entire eye; cortex is not an entire root; crop is not an entire digestive system, esophagus or foregut; crop contents are not an esophagus. Exclude only exact guarded source-path contributions, retaining independent genera and source observations. This does not settle generic cortex identity or equivalent avian crop sources. Exact target UBERON:0001851. Other identity and mapping findings remain separate."]] |

## Limits And Additional Notes

- Original specimen-level evidence and all pair-level citations were not exhaustively reconstructed. Native association counts, taxon ranks and scores do not establish prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs. Exact target TaxIds were separately resolved; frozen taxon labels are not universally current.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. No new causal mechanism is imported.
- This successor is a same-agent disposition, not independent human approval. Final-head and merge-queue checks are separate publication gates. Full-corpus scientific review and current kg-microbe export conformance remain incomplete.
- All immutable earlier bundles and session histories remain unchanged. Retain the exact off-main input base with an annotated provenance tag before squash merge and branch deletion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T062913Z-cortex-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: cortex'
started_at: '2026-10-16T05:59:21Z'
finished_at: '2026-10-16T06:29:13Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Parent agent integrates evidence and separate-agent source/hierarchy
    cross-checks; not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: Removed the guarded GOLD context-parent contribution. Identity and native
  status are unchanged. Source observations and independent genera are preserved.
  Remaining predecessor findings are explicitly open.
source:
  git_revision: ee3b5b9ecb9031a9a59dd7ed87da7c97c55a181f
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
    sha256: c4aeaa9bc04f3704e9e8f69e406990b6d08dd91b1c6afe39aec6a4727ff6612a
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 1f3af4cfd82b31d351ecdce846e5e2d626037d255db63ee869bab5259e12496e
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: bc7a13d922c179cd9bcd4d37b348bc90a39b08a4dafba7af4ed0039ad99621c3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: 747e6a5612dc0b7ed881b9fb323fd57ab3c75794d9ee5ebb9d59b2be57dbf8cd
    role: context
  - path: data/habitats/host_associated/cortex.yaml
    sha256: 7150f7f1f8728eea366f567490e811472c01b7fbf0545d7558b943823c6eaeb5
    role: target
  - path: data/habitats/host_associated/root__722ce44f.yaml
    sha256: eed2322864dbb77748a875551a9c8b42a7db2ffd35e246c9e4fa5f586ff736e5
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
  - path: history/README.md
    sha256: 819361a711697f96ff9c1aa0b27e94302547970b3b54777d67ec1449db5e543a
    role: context
  - path: history/mappings/conjunctiva_crop_review_nonavian/2026-10-16T054553Z-codex-gpt-5-64c4ba.yaml
    sha256: c2700ecc67a370a509f8b6aca48dc07c5bfb807c2a5c6b0e05c03dc2dbc76bd1
    role: context
  - path: history/mappings/conjunctiva_crop_review_parents/2026-10-16T054552Z-codex-gpt-5-b09465.yaml
    sha256: abe557d3e71cfb777cf2f135edbf0ae7d17c059f9717e1eed15543f58d579c59
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261016T054408Z-cortex-record/review.yaml
    sha256: 32219a91fd296e6d024abe87397ab5e1117032ad7df7da7a44ccb6b1bac98fb6
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
  - path: tests/test_conjunctiva_crop_review_repairs.py
    sha256: 182b7c46fdc4564730e0ca1612a776ae724833ec6ef49156077c5d9d0a95d78e
    role: context
targets:
- target_id: UBERON:0001851
  path: data/habitats/host_associated/cortex.yaml
  label: cortex
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
  description: Full current target assessment and explicit disposition of every baseline
    finding after bounded repair.
  selection: One of ten repaired targets from the column-through-crown-gall cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0001851
  exclusions:
  - target: Other corpus records and SSSOM/KGX conformance
    reason: Not whole-corpus scientific approval or shared export-contract certification.
checks:
- check_id: C4
  name: just validate data/habitats/host_associated/cortex.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/cortex.yaml
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:47:41Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cortex.yaml"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C10
  name: just validate-strict data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml
    data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml
    data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml
    data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml
    data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml
    data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml
    data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml
    data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml
    data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml
    data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml
    data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml
    data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml
    data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml
    data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml
    data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml
    data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml
    data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml
    data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml
    data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml
    data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml
    data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml
    data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml
    data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:47:56Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml\
    \ data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml\
    \ data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml\
    \ data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml\
    \ data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml\
    \ data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml\
    \ data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml\
    \ data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml\
    \ data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml\
    \ data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml\
    \ data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml\
    \ data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C11
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: 'Finished 2026-10-16T05:48:04Z. No issues found

    836 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C12
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:48:04Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C13
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:48:17Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C14
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:48:21Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C15
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:48:36Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C16
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:49:16Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C17
  name: uv run pytest -q tests/test_conjunctiva_crop_review_repairs.py --no-cov
  status: passed
  required: true
  command: uv run pytest -q tests/test_conjunctiva_crop_review_repairs.py --no-cov
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: 'Finished 2026-10-16T05:49:22Z. ..                                                                       [100%]

    2 passed in 4.92s'
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C18
  name: uv run ruff check .
  status: passed
  required: true
  command: uv run ruff check .
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: Finished 2026-10-16T05:49:22Z. All checks passed!
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C19
  name: git diff --check
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: 'Finished 2026-10-16T05:49:22Z. '
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C20
  name: just term-requests
  status: passed
  required: true
  command: just term-requests
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:55:54Z. wrote curation/term_requests/envo_robot_template.tsv:\
    \ 110 ENVO terms from 110 source records\n\n22 examined-ungrounded record(s) still\
    \ have no request written. Top by volume:\n      438  Medical-environment    \
    \            habitatmech:BACDIVE.5e52ea1bba\n      228  Fruit-Seed           \
    \              habitatmech:BACDIVE.ba016fe448\n       35  Egg                \
    \                habitatmech:BACDIVE.d48ce9485d\n        5  Caeca: Bacteriome\
    \                  habitatmech:GOLD.2d506b9526\n        3  Abdomen           \
    \                 habitatmech:GOLD.c6b0b54290\n        2  Crop               \
    \                habitatmech:GOLD.5446ce4c6d\n        1  Thalassic           \
    \               habitatmech:GOLD.3fece6dbf7\n        1  Crop                 \
    \              habitatmech:GOLD.57011086ca\n        0  Subtidal zone sediment\
    \             habitatmech:GOLD.785879d721\n        0  Subterranean lake      \
    \            habitatmech:GOLD.937bf682c4\n\ncovered 105842 upstream assertions;\
    \ 713 still unrequested across 22 record(s); 15 examined and deliberately not\
    \ asked for\n\n`created by` is empty: it wants pipe-delimited full ORCID IRIs\
    \ and this script cannot know them.\n uv run python scripts/build_term_requests.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C21
  name: just docs-stats
  status: passed
  required: true
  command: just docs-stats
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:56:12Z. updated README corpus statistics\n uv run\
    \ python scripts/check_docs.py --write"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C22
  name: just render
  status: passed
  required: true
  command: just render
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:56:38Z. rendered 3209 habitat pages, 259 redirect\
    \ stubs, 8 categories, 132 term requests -> /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages\n\
    \ uv run python scripts/render_pages.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C23
  name: just render-check
  status: passed
  required: true
  command: just render-check
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:57:05Z. rendered 3209 habitat pages, 259 redirect\
    \ stubs, 8 categories, 132 term requests -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpiryd8m6g/site\n\
    pages/ is in step with the corpus\n uv run python scripts/render_pages.py --check"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C24
  name: just redirects-check
  status: passed
  required: true
  command: just redirects-check
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: "Finished 2026-10-16T05:58:39Z. RETIRED.tsv is current (259 redirects)\n\
    \ uv run python scripts/build_redirects.py --check"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C25
  name: uv run ruff check .
  status: passed
  required: true
  command: uv run ruff check .
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: Finished 2026-10-16T05:58:39Z. All checks passed!
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C26
  name: git diff --check
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: 'Finished 2026-10-16T05:58:40Z. '
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: CCI
  name: Exact-revision hosted authoritative QC and archive contract
  status: passed
  required: true
  command: gh run view 38858656719 --repo CultureBotAI/HabitatMech --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - UBERON:0001851
  summary: Verified 2026-10-16T06:28:52Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38858656719
  scope_note: Repaired input/product commit before these new successor outputs; final-head
    and merge-queue checks remain separate.
evidence:
- evidence_id: EX9
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001/graph
  locator: ENVO_01001001-graph.json
  accessed_at: '2026-10-16T05:15:47Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001001",
    "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001001",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_33090", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 43b7f7cee8e27c64685cea0193012a2cc71851b91d19a2a7052fa1e6548a6a71
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001
  locator: ENVO_01001001.json
  accessed_at: '2026-10-16T05:15:46Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "ENVO:01001001", "label": "plant-associated environment", "is_obsolete": false,
    "description": ["An environmental system determined by a green plant."], "obo_synonym":
    null}'
  snapshot_sha256: b1623e2f33257c2fadc5bf06670bcc7e95384c210301e901f7faa8059c5ed815
- evidence_id: EX11
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0000258/graph
  locator: PO_0000258-graph.json
  accessed_at: '2026-10-16T05:21:56Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/PO_0000258",
    "target": "http://purl.obolibrary.org/obo/PO_0005708", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/PO_0000258",
    "target": "http://purl.obolibrary.org/obo/PO_0009005", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 49ce5b213aaa235ef3895b6c0785bd52e1fd1b01842ebdf5c534fafb5d015386
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0000258
  locator: PO_0000258.json
  accessed_at: '2026-10-16T05:21:56Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "PO:0000258", "label": "root cortex", "is_obsolete": false, "description": ["In
    dicots and gymnosperms, the cortex consists of mainly parenchyma cells. In monocots
    sclerenchyma develops in addition to parenchyma.", "A portion of cortex (PO:0005708)
    that is part of a root (PO:0009005)."], "obo_synonym": [{"name": "cortex de la
    ra&#237z (Spanish, exact)", "scope": "hasExactSynonym", "type": "Spanish synonym
    (exact)", "xrefs": [{"database": "POC", "id": "Maria_Alejandra_Gandolfo", "description":
    null, "url": null}]}, {"name": "\u6839\u76ae\u5c64 (Japanese, exact)", "scope":
    "hasExactSynonym", "type": "Japanese synonym (exact)", "xrefs": [{"database":
    "NIG", "id": "Yukiko_Yamazaki", "description": null, "url": null}]}]}'
  snapshot_sha256: b2f73e67a34f894f1e31a421bdabc609685788816be726f201c508125010576f
- evidence_id: EX13
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0005708/graph
  locator: PO_0005708-graph.json
  accessed_at: '2026-10-16T05:21:59Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/PO_0005708",
    "target": "http://purl.obolibrary.org/obo/PO_0025059", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: e771b5edc50bc0dec1298d9901aa04b15d7791490b16b8f1b162da4f1b0795a5
- evidence_id: EX14
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0005708
  locator: PO_0005708.json
  accessed_at: '2026-10-16T05:21:57Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "PO:0005708", "label": "cortex", "is_obsolete": false, "description": ["A maximal
    portion of ground tissue (PO:0025059) between the vascular system (PO:0000034)
    and the epidermis (PO:0005679) in a plant."], "obo_synonym": [{"name": "cortex
    (corteza) (Spanish, exact)", "scope": "hasExactSynonym", "type": "Spanish synonym
    (exact)", "xrefs": [{"database": "POC", "id": "Maria_Alejandra_Gandolfo", "description":
    null, "url": null}]}, {"name": "\u76ae\u5c64 (Japanese, exact)", "scope": "hasExactSynonym",
    "type": "Japanese synonym (exact)", "xrefs": [{"database": "NIG", "id": "Yukiko_Yamazaki",
    "description": null, "url": null}]}]}'
  snapshot_sha256: e5a8f5a8ad8233d20c285a4fcb79f7b36e23ceb2a5d358a615ff8055efe8d764
- evidence_id: EX15
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0009005/graph
  locator: PO_0009005-graph.json
  accessed_at: '2026-10-16T05:15:54Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/PO_0009005",
    "target": "http://purl.obolibrary.org/obo/PO_0025004", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/PO_0009005",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001062", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/PO_0009005",
    "target": "http://purl.obolibrary.org/obo/PO_0005029", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/PO_0009005",
    "target": "http://purl.obolibrary.org/obo/PO_0025025", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: eb432329da793b462e7a4304db0693a1eeddd1e7b0c6c147f83fb05d6c5e0c3e
- evidence_id: EX16
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0009005
  locator: PO_0009005.json
  accessed_at: '2026-10-16T05:15:53Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "PO:0009005", "label": "root", "is_obsolete": false, "description": ["Roots function
    in the absorption of water and inorganic nutrients, anchoring the plant body to
    the substrate and supporting it, storage of food and nutrients, and vegetative
    reproduction. The roots of most vascular plant species enter into symbiosis with
    soil-borne microorganisms. Roots are usually positively geotropic and found underground,
    although there are many exceptions such as the aerial roots of orchids. Roots
    often form secondary thickening from the root lateral meristem (PO:0006308). Commonly
    thought of as one of the three basic parts of the plant body, along with the shoot
    axis (PO:0025029) and leaves (PO:0025034).", "A plant axis (PO:0025004) that lacks
    shoot axis nodes (PO:0005004) and usually grows indeterminately."], "obo_synonym":
    [{"name": "ra&#237z (Spanish, exact)", "scope": "hasExactSynonym", "type": "Spanish
    synonym (exact)", "xrefs": [{"database": "POC", "id": "Maria_Alejandra_Gandolfo",
    "description": null, "url": null}]}, {"name": "radices (exact, plural)", "scope":
    "hasExactSynonym", "type": "plural form", "xrefs": [{"database": "FNA", "id":
    "3c46e84c-23e4-416b-91cd-2f7c42e4b13d", "description": null, "url": null}]}, {"name":
    "radix (exact)", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database":
    "FNA", "id": "e6315684-fc99-4976-b39d-b356c4b7e7fd", "description": null, "url":
    null}]}, {"name": "\u6839 (Japanese, exact)", "scope": "hasExactSynonym", "type":
    "Japanese synonym (exact)", "xrefs": [{"database": "NIG", "id": "Yukiko_Yamazaki",
    "description": null, "url": null}]}, {"name": "climbing root (narrow)", "scope":
    "hasNarrowSynonym", "type": null, "xrefs": [{"database": "FNA", "id": "bf0ce902-e91c-401a-92a8-26b20142ce5f",
    "description": null, "url": null}]}]}'
  snapshot_sha256: 60c8efb1f40858c6dbe6c028123a6df05954c7b8ed650ad132d94c01bc4716c5
- evidence_id: EX17
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0025004/graph
  locator: PO_0025004-graph.json
  accessed_at: '2026-10-16T05:15:56Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/PO_0025004",
    "target": "http://purl.obolibrary.org/obo/PO_0009008", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 4ce545704c28c431df21228b15bcd7ae99b1f53147c996f81dd0ae4318f0f343
- evidence_id: EX18
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0025004
  locator: PO_0025004.json
  accessed_at: '2026-10-16T05:15:55Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "PO:0025004", "label": "plant axis", "is_obsolete": false, "description": ["Includes
    roots and shoots.", "An axial plant organ (PO:0009008)."], "obo_synonym": [{"name":
    "eje de la planta (Spanish, exact)", "scope": "hasExactSynonym", "type": "Spanish
    synonym (exact)", "xrefs": [{"database": "POC", "id": "Maria_Alejandra_Gandolfo",
    "description": null, "url": null}]}, {"name": "plant axes (exact, plural)", "scope":
    "hasExactSynonym", "type": "plural form", "xrefs": [{"database": "FNA", "id":
    "2355281f-ab10-4ae2-a3d8-672cace068a8", "description": null, "url": null}]}, {"name":
    "\u690d\u7269\u8ef8\uff08\u8ef8\u67f1\uff09 (Japanese, exact)", "scope": "hasExactSynonym",
    "type": "Japanese synonym (exact)", "xrefs": [{"database": "NIG", "id": "Yukiko_Yamazaki",
    "description": null, "url": null}]}]}'
  snapshot_sha256: 3ad9ec0dbfc0bd3355b93e17b32032ab1fd4416ed2b480a9f81eee07f7f84867
- evidence_id: EX19
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000064/graph
  locator: UBERON_0000064-graph.json
  accessed_at: '2026-10-16T05:15:59Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000064",
    "target": "http://purl.obolibrary.org/obo/UBERON_0010000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 967402ffd0dddec5434cead4605a9d5c186b95ebca27e3058b3bf84a0125708a
- evidence_id: EX20
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000064
  locator: UBERON_0000064.json
  accessed_at: '2026-10-16T05:15:57Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "UBERON:0000064", "label": "organ part", "is_obsolete": false, "description":
    ["A multicellular structure that is a part of an organ."], "obo_synonym": [{"name":
    "cardinal organ part", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database":
    "FMA", "id": "82472", "description": null, "url": "http://purl.org/sig/ont/fma/82472"}]},
    {"name": "regional part of organ", "scope": "hasRelatedSynonym", "type": null,
    "xrefs": [{"database": "BIRNLEX", "id": "16", "description": null, "url": "http://uri.neuinfo.org/nif/nifstd/birnlex_16"}]}]}'
  snapshot_sha256: 09badc6401293dc9779182401df0aaf1db327829be2b99f024a083cd8118acf9
- evidence_id: EX21
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001062/graph
  locator: UBERON_0001062-graph.json
  accessed_at: '2026-10-16T05:16:11Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001062",
    "target": "http://purl.obolibrary.org/obo/BFO_0000004", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 5bf70afe3a2d4294afed655c9510e1e198dae2ff4c334cb77c32d1ec35eaf74f
- evidence_id: EX22
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001062
  locator: UBERON_0001062.json
  accessed_at: '2026-10-16T05:16:10Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "UBERON:0001062", "label": "anatomical entity", "is_obsolete": false, "description":
    ["Biological entity that is either an individual member of a biological species
    or constitutes the structural organization of an individual member of a biological
    species."], "obo_synonym": null}'
  snapshot_sha256: 5b4a4e4aa2a2dd579b9de26d95354871116cfb8a5b1f934ee05f791ce538bee6
- evidence_id: EX23
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001851/graph
  locator: UBERON_0001851-graph.json
  accessed_at: '2026-10-16T05:16:16Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001851",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000064", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001851",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000062", "uri": "http://purl.obolibrary.org/obo/RO_0002007",
    "label": "bounding layer of"}]'
  snapshot_sha256: fefe464e4db16ae4551b23e0cd8c0bde1bd3e306a56cf9e1d84659d7665d5cd9
- evidence_id: EX24
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001851
  locator: UBERON_0001851.json
  accessed_at: '2026-10-16T05:16:15Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "UBERON:0001851", "label": "cortex", "is_obsolete": false, "description": ["Outermost
    layer of an organ[WP]."], "obo_synonym": [{"name": "cortex", "scope": "hasExactSynonym",
    "type": null, "xrefs": [{"database": "FMA", "id": "61109", "description": null,
    "url": "http://purl.org/sig/ont/fma/61109"}]}]}'
  snapshot_sha256: ce613ba1b6b12c4f40237e0a5f27cb44fcaf72d8143792ca1fab840bac569760
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/cortex.yaml
  locator: Entire regenerated target YAML
  accessed_at: '2026-10-16T06:29:09Z'
  support: supports
  summary: '{"identifier": "UBERON:0001851", "label": "cortex", "definition": "Outermost
    layer of an organ[WP].", "definition_source": "UBERON", "habitat_category": "HOST_ASSOCIATED",
    "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text":
    "cortex of organ", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}], "parent_habitats":
    ["UBERON:0000064"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:8244",
    "source_label": "Cortex", "source_path": "Host-associated > Plants > Roots > Cortex",
    "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share
    this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: EXACT."}, {"timestamp": "2026-10-16T00:00:00Z", "curator":
    "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path
    parent contribution PO:0009005 for habitatmech:GOLD.994d82c95b (Host-associated
    > Plants > Roots > Cortex). Review https://github.com/CultureBotAI/HabitatMech/issues/2229
    : Conjunctiva is not an entire visual system; cornea is not an entire eye; cortex
    is not an entire root; crop is not an entire digestive system, esophagus or foregut;
    crop contents are not an esophagus. Exclude only exact guarded source-path contributions,
    retaining independent genera and source observations. This does not settle generic
    cortex identity or equivalent avian crop sources. Exact target UBERON:0001851.
    Other identity and mapping findings remain separate."}]}'
  snapshot_sha256: 7150f7f1f8728eea366f567490e811472c01b7fbf0545d7558b943823c6eaeb5
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261016T054408Z-cortex-record/review.yaml
  locator: Every immutable baseline finding
  accessed_at: '2026-10-16T06:29:09Z'
  support: supports
  summary: Exact predecessor issue keys and findings are reconciled; original inspected
    source scope is preserved.
  snapshot_sha256: 32219a91fd296e6d024abe87397ab5e1117032ad7df7da7a44ccb6b1bac98fb6
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_conjunctiva_crop_review_repairs.py
  locator: Complete full-corpus counterfactual
  accessed_at: '2026-10-16T06:29:09Z'
  support: supports
  summary: Exactly ten records differ. The only scientific changes are guarded context-parent
    removal and two non-avian grounding/predicate/status corrections; source counts,
    taxa and other fields are invariant.
  snapshot_sha256: 182b7c46fdc4564730e0ca1612a776ae724833ec6ef49156077c5d9d0a95d78e
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict hierarchy, ITEM decisions and source units
  accessed_at: '2026-10-16T06:29:09Z'
  support: supports
  summary: Generated artifacts are not edited by hand; native history/status follows
    exact maintained rows.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EH40
  kind: record_content
  reference: history/mappings/conjunctiva_crop_review_nonavian/2026-10-16T054553Z-codex-gpt-5-64c4ba.yaml
  locator: Complete session event
  accessed_at: '2026-10-16T06:29:09Z'
  support: supports
  summary: Authorized curation by codex-gpt-5; exact maintained owner and issue retained.
  snapshot_sha256: c2700ecc67a370a509f8b6aca48dc07c5bfb807c2a5c6b0e05c03dc2dbc76bd1
- evidence_id: EH41
  kind: record_content
  reference: history/mappings/conjunctiva_crop_review_parents/2026-10-16T054552Z-codex-gpt-5-b09465.yaml
  locator: Complete session event
  accessed_at: '2026-10-16T06:29:09Z'
  support: supports
  summary: Authorized curation by codex-gpt-5; exact maintained owner and issue retained.
  snapshot_sha256: abe557d3e71cfb777cf2f135edbf0ae7d17c059f9717e1eed15543f58d579c59
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact physical TSV rows
  accessed_at: '2026-10-16T06:29:11Z'
  support: supports
  summary: '[[6, "habitatmech:GOLD.994d82c95b\tHost-associated > Plants > Roots >
    Cortex\tPO:0009005\tcodex-gpt-5\t2026-10-16\tReview https://github.com/CultureBotAI/HabitatMech/issues/2229
    : Conjunctiva is not an entire visual system; cornea is not an entire eye; cortex
    is not an entire root; crop is not an entire digestive system, esophagus or foregut;
    crop contents are not an esophagus. Exclude only exact guarded source-path contributions,
    retaining independent genera and source observations. This does not settle generic
    cortex identity or equivalent avian crop sources. Exact target UBERON:0001851.
    Other identity and mapping findings remain separate."]]'
  snapshot_sha256: 1f3af4cfd82b31d351ecdce846e5e2d626037d255db63ee869bab5259e12496e
assessments:
- assessment_id: A1
  area: consistency
  topic: Bounded correction and exact preservation
  outcome: supported
  summary: Removed the guarded GOLD context-parent contribution. Identity and native
    status are unchanged. Source observations and independent genera are preserved.
    Remaining predecessor findings are explicitly open.
  target_ids:
  - UBERON:0001851
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
- assessment_id: A2
  area: identity
  topic: Current anatomical identity and hierarchy
  outcome: concern
  summary: 'UBERON:0001851: cortex; EXACT/SEEDED; parents ["UBERON:0000064"]. No replacement
    anatomical identity or definition is fabricated. Remaining exact-identity findings
    are not concealed.'
  target_ids:
  - UBERON:0001851
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
- assessment_id: A3
  area: quantity
  topic: Units, counts and observations
  outcome: supported
  summary: '[{"source": "GOLD", "source_id": "gold.ecosystem:8244", "source_label":
    "Cortex", "source_path": "Host-associated > Plants > Roots > Cortex", "mapping_predicate":
    "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first
    shown. See data/raw/gold_ecosystem_paths.tsv."}]. Original source counts/units,
    taxa, scores and parameters remain unchanged; these are not prevalence measurements.'
  target_ids:
  - UBERON:0001851
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
- assessment_id: A4
  area: representation
  topic: Predecessor reconciliation
  outcome: concern
  summary: 'Every previous finding keeps its stable issue key and exact lineage. Removing
    invalid non-avian matches does not solve global mapping contract #1398.'
  target_ids:
  - UBERON:0001851
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
- assessment_id: A5
  area: completeness
  topic: Evidence and lifecycle boundaries
  outcome: supported
  summary: Only the two explicit non-avian ITEM decisions change native status. Optional
    definitions, causal mechanisms and biological absence claims are not invented.
  target_ids:
  - UBERON:0001851
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
findings:
- finding_id: F1
  issue_key: cortex-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: GOLD context is not a strictly broader habitat class
  description: Removed only the guarded GOLD source-context contribution PO:0009005.
    Independent parents and every source observation are retained.
  target_ids:
  - UBERON:0001851
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2229
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T054408Z-cortex-record
    finding_id: F1
  disposition_reason: Removed only the guarded GOLD source-context contribution PO:0009005.
    Independent parents and every source observation are retained.
- finding_id: F2
  issue_key: cortex-generic-identity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Root-cortex source is not exact generic organ cortex
  description: The whole-root edge is removed, but exact generic cortex identity for
    the root-cortex source remains unresolved. An explicit identity migration and
    downstream redirect accounting remain required.
  target_ids:
  - UBERON:0001851
  field_paths:
  - identifier
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  - EX16
  - EX17
  - EX18
  - EX19
  - EX20
  - EX21
  - EX22
  - EX23
  - EX24
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2231
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T054408Z-cortex-record
    finding_id: F2
  disposition_reason: The whole-root edge is removed, but exact generic cortex identity
    for the root-cortex source remains unresolved. An explicit identity migration
    and downstream redirect accounting remain required.
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - UBERON:0001851
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  description: The sole source is Plants > Roots > Cortex, yet the record claims exact
    generic UBERON cortex identity and makes that generic organ layer a subtype of
    the whole plant root. Both the exact identity scope and whole-root parent need
    correction. Current PO root cortex is a verified candidate, not automatically
    adopted by this review. Preserve zero-count semantics and the independent organ-part
    genus pending explicit source-specific identity migration. Assess PO:0000258 against
    pinned sources and migrate identity through native path/redirect controls, not
    hand-edited YAML. Proposed work only; no repair or status promotion is performed
    by this review.
  generator: Controlled source/input correction, just seed, inspected just seed-canary,
    guarded just seed-apply, and dependent term-request/map/site/redirect regeneration
    where required.
  acceptance_checks:
  - Regress the exact target claim and preserve valid genera, identifiers, source
    counts/units and taxon associations. Recover original evidence before deleting
    a provisional pair; do not decrement frozen totals by hand.
  - Record authorized curation history; require schema, strict, provenance, history,
    label, corpus, site and full QC gates.
  - Save an immutable successor with the same issue key and exact predecessor finding
    identity.
limitations:
- Original specimen-level evidence and all pair-level citations were not exhaustively
  reconstructed. Native association counts, taxon ranks and scores do not establish
  prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs. Exact target TaxIds were
  separately resolved; frozen taxon labels are not universally current.
- 'iModulonDB is not applicable: no gene, regulator or expression-module claim is
  asserted. No new causal mechanism is imported.'
- This successor is a same-agent disposition, not independent human approval. Final-head
  and merge-queue checks are separate publication gates. Full-corpus scientific review
  and current kg-microbe export conformance remain incomplete.
notes:
- All immutable earlier bundles and session histories remain unchanged. Retain the
  exact off-main input base with an annotated provenance tag before squash merge and
  branch deletion.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261016T054408Z-cortex-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
