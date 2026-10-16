# Remediation review: cerumen

- Review: 20261016T004717Z-cerumen-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T00:25:14Z
- Finished UTC: 2026-10-16T00:47:17Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed only the reviewed GOLD parent contribution UBERON:0013211. All independent genera, source IDs/paths/counts/units, taxa, native identities and statuses are preserved. No unresolved predecessor finding remains in this exact target scope.

## Scope And Provenance

Full current-record assessment and explicit disposition of every predecessor finding after the bounded parent correction.

Selection: One of twelve repaired targets in the 24-record cecal-through-cervical cohort; no additional sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5d98511b90fb848de1718404d2bf452ba2799e06.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0002297 | data/habitats/host_associated/cerumen.yaml | generated | cerumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/cerumen.yaml | passed | True | UBERON:0002297 | Executed 2026-10-16T00:17:08Z through 2026-10-16T00:17:10Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cerumen.yaml |
| just validate-strict data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml | passed | True | UBERON:0002297 | Executed 2026-10-16T00:14:39Z through 2026-10-16T00:14:46Z. uv run python scripts/validate_strict.py data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | UBERON:0002297 | Executed 2026-10-16T00:14:46Z through 2026-10-16T00:14:56Z. No issues found<br>830 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | UBERON:0002297 | Executed 2026-10-16T00:14:56Z through 2026-10-16T00:14:56Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | UBERON:0002297 | Executed 2026-10-16T00:14:56Z through 2026-10-16T00:15:12Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | UBERON:0002297 | Executed 2026-10-16T00:15:12Z through 2026-10-16T00:15:16Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | UBERON:0002297 | Executed 2026-10-16T00:15:16Z through 2026-10-16T00:15:34Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | UBERON:0002297 | Executed 2026-10-16T00:15:34Z through 2026-10-16T00:16:23Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_cecal_csf_cerumen_review_repairs.py | passed | True | UBERON:0002297 | Executed 2026-10-16T00:16:23Z through 2026-10-16T00:16:29Z. ..                                                                       [100%]<br>2 passed in 5.66s |
| git diff --check 0eb609a7ddb34925067116af806e26c165e10678 | passed | True | UBERON:0002297 | Executed 2026-10-16T00:16:29Z through 2026-10-16T00:16:30Z.  |
| Exact-revision full QC and archive contract | passed | True | UBERON:0002297 | Verified 2026-10-16T00:46:17Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38829324804 |
| Standalone evidence-reference validator applicability | not_applicable | False | UBERON:0002297 | No standalone citation/reference validator is documented for these evidence-free generated records. Target EvidenceItems and causal edges are absent. Stable source and ontology/taxon references were checked manually and with documented native gates; current-decision primary citations were separately verified where present. |

## Scientific And Domain Assessments

### Bounded repair and preservation

consistency: supported. Targets: UBERON:0002297.

Removed only the reviewed GOLD parent contribution UBERON:0013211. All independent genera, source IDs/paths/counts/units, taxa, native identities and statuses are preserved. No unresolved predecessor finding remains in this exact target scope.

### Current identity, definition, aliases and strict ancestry

identity: supported. Targets: UBERON:0002297.

UBERON:0002297: cerumen, EXACT/REVIEWED, parents ["UBERON:0001089"]. No unsupported replacement genus or optional definition is invented.

### Frozen nonadditive source evidence

quantity: supported. Targets: UBERON:0002297.

[{"source": "GOLD", "source_id": "gold.ecosystem:7025", "source_label": "Cerumen/Earwax", "source_path": "Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Ceruminous glands &gt; Cerumen/Earwax", "mapping_predicate": "skos:exactMatch"}]. Entire source attestations and taxon fields are unchanged by the counterfactual regression.

### Exact finding lineage and open scope

representation: supported. Targets: UBERON:0002297.

Every predecessor finding retains its exact target and issue key. Parent correction does not resolve Ceros source meaning, the upstream Polyps identity or shared mapping endpoints. No export-conformance certification.

### Optional claims and current evidence limits

completeness: supported. Targets: UBERON:0002297.

No parameters, causal edges or characteristic-presence claims were added. Inspected primary and taxonomy evidence remains bounded to its original claim; zero counts are not biological absence.

## Findings

### F1: Source context is not a supported broader habitat class

major / resolved / confirmed; issue key: cerumen-context-parent.

Corrected through maintained input and native regeneration. Excluded only exact guarded GOLD contribution UBERON:0013211; independently valid genera, original source observations and native identity/status remain unchanged.

Disposition: Excluded only exact guarded GOLD contribution UBERON:0013211; independently valid genera, original source observations and native identity/status remain unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000382/graph; UBERON_0000382-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000382", "target": "http://purl.obolibrary.org/obo/UBERON_0001820", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000382", "target": "http://purl.obolibrary.org/obo/UBERON_0012177", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000382", "target": "http://purl.obolibrary.org/obo/UBERON_0001003", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000382; UBERON_0000382.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0000382", "label": "apocrine sweat gland", "is_obsolete": false, "description": ["Apocrine sweat glands are sweat glands composed of a coiled secretory portion located at the junction of the dermis and subcutaneous fat, from which a straight portion inserts and secretes into the infundibular portion of the hair follicle. The ducts of apocrine glands open into the canals of hair follicles. The stimulus for the secretion of apocrine sweat glands is adrenaline, which is a hormone carried in the blood[WP]."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001089/graph; UBERON_0001089-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001089", "target": "http://purl.obolibrary.org/obo/UBERON_0000456", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001089", "target": "http://purl.obolibrary.org/obo/UBERON_0006314", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001089", "target": "http://purl.obolibrary.org/obo/PATO_0001548", "uri": "http://purl.obolibrary.org/obo/RO_0000086", "label": "has quality"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001089", "target": "http://purl.obolibrary.org/obo/UBERON_0001820", "uri": "http://purl.obolibrary.org/obo/RO_0003001", "label": "produced by"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001089; UBERON_0001089.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0001089", "label": "sweat", "is_obsolete": false, "description": ["Secretion produced by a sweat gland."]} |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002297/graph; UBERON_0002297-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0002297", "target": "http://purl.obolibrary.org/obo/UBERON_0001089", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002297", "target": "http://purl.obolibrary.org/obo/UBERON_0000382", "uri": "http://purl.obolibrary.org/obo/RO_0003001", "label": "produced by"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002297", "target": "http://purl.obolibrary.org/obo/UBERON_0001352", "uri": "http://purl.obolibrary.org/obo/RO_0001025", "label": "located in"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002297; UBERON_0002297.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0002297", "label": "cerumen", "is_obsolete": false, "description": ["The yellow or brown waxy secretions produced by vestigial apocrine sweat glands in the external ear canal[MESH]."]} |
| EX7 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0013211/graph; UBERON_0013211-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0013211", "target": "http://purl.obolibrary.org/obo/UBERON_0000382", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0013211", "target": "http://purl.obolibrary.org/obo/UBERON_0001352", "uri": "http://purl.obolibrary.org/obo/RO_0001025", "label": "located in"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0013211", "target": "http://purl.obolibrary.org/obo/UBERON_0001691", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0013211", "target": "http://purl.obolibrary.org/obo/UBERON_0002297", "uri": "http://purl.obolibrary.org/obo/RO_0003000", "label": "produces"}] |
| EX8 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0013211; UBERON_0013211.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0013211", "label": "cerumen gland", "is_obsolete": false, "description": ["A specialized sudoriferous gland (sweat glands) located subcutaneously in the external auditory canal."]} |
| EAFTER | data/habitats/host_associated/cerumen.yaml; Entire regenerated target | supports | {"identifier": "UBERON:0002297", "label": "cerumen", "definition": "The yellow or brown waxy secretions produced by vestigial apocrine sweat glands in the external ear canal[MESH].", "definition_source": "UBERON", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Cerumen/Earwax", "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "ear wax", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text": "earwax", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}], "parent_habitats": ["UBERON:0001089"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7025", "source_label": "Cerumen/Earwax", "source_path": "Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Ceruminous glands &gt; Cerumen/Earwax", "mapping_predicate": "skos:exactMatch"}], "curation_history": [{"timestamp": "2026-08-16T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to UBERON:0002297 'cerumen' (EXACT). Variant-match review (#12): the seeder grounds on exact labels only, so GOLD's slash and plural conventions hid a term that says exactly this. Cerumen is earwax, defined by UBERON as the waxy secretion of the external auditory canal. Path: Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Ceruminous glands &gt; Cerumen/Earwax (source concept habitatmech:GOLD.aea4a5fe91)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: EXACT."}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution UBERON:0013211 for habitatmech:GOLD.aea4a5fe91 (Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Ceruminous glands &gt; Cerumen/Earwax). Review https://github.com/CultureBotAI/HabitatMech/issues/2214 : UBERON cerumen denotes earwax with supported sweat genus. It is a product of glands, not a subtype of the cerumen gland. Keep the reviewed ITEM identity, aliases and independent genus; exclude only the GOLD gland context contribution. No source observations or universal chemical measurements should be invented. Exclude only this exact source contribution; preserve independent valid genera and source observations. Mapping endpoint #1398, Ceros source meaning #325 and upstream Polyps identity #2171 are not resolved by this hierarchy guard."}]} |
| EPREV | reviews/structured/20261015T235751Z-cerumen-record/review.yaml; Exact immutable predecessor and all findings | supports | Original observation remains byte-identical. Every finding retains its issue key, target and exact predecessor. |
| ETEST | tests/test_cecal_csf_cerumen_review_repairs.py; Full-corpus counterfactual and exact parent/source preservation | supports | The regression proves exactly twelve record documents change, only parent_habitats and one appended generated event change, and all identities and other fields/records remain identical. Public issue hrefs are checked with the template filter. |
| ERULE | docs/CURATION.md; Strict broader hierarchy and maintained ownership | supports | Context, anatomical containment and source-path proximity do not imply is-a. |
| EHISTORY | history/README.md; Immutable session audit versus generated projection | supports | Committed sessions and saved reviews remain append-only. |
| EI13 | curation/gold_parent_exclusions.tsv; Exact keyed rows 11 | supports | [[11, "habitatmech:GOLD.aea4a5fe91\tHost-associated &gt; Mammals: Human &gt; Integumentary system &gt; Ceruminous glands &gt; Cerumen/Earwax\tUBERON:0013211\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2214 : UBERON cerumen denotes earwax with supported sweat genus. It is a product of glands, not a subtype of the cerumen gland. Keep the reviewed ITEM identity, aliases and independent genus; exclude only the GOLD gland context contribution. No source observations or universal chemical measurements should be invented. Exclude only this exact source contribution; preserve independent valid genera and source observations. Mapping endpoint #1398, Ceros source meaning #325 and upstream Polyps identity #2171 are not resolved by this hierarchy guard."]] |
| EI14 | curation/decisions.tsv; Exact keyed rows 1661 | supports | [[1661, "habitatmech:GOLD.aea4a5fe91\tGROUND\tUBERON:0002297\tcerumen\tEXACT\tclaude-opus-5\t2026-08-16\tVariant-match review (#12): the seeder grounds on exact labels only, so GOLD's slash and plural conventions hid a term that says exactly this. Cerumen is earwax, defined by UBERON as the waxy secretion of the external auditory canal. Path: Host-associated &gt; Mammals: Human &gt; Integumentary system &gt; Ceruminous glands &gt; Cerumen/Earwax\tITEM\t\t"]] |

## Limits And Additional Notes

- Source counts, ranks and scores do not establish prevalence, viability or characteristic presence. Original specimen-level evidence for every source member has not been reconstructed.
- Configured label validation skipped 2063 no-adapter pairs; displayed TaxIds were separately resolved against current NCBI including aliases.
- iModulonDB is not applicable: target assertions contain no gene, regulator or expression-module claim. No paid research or native status promotion was performed.
- Same-agent adversarial assessment, not independent approval. Recorded full QC covers exact repaired inputs before this new successor; final-head and queue checks remain publication gates.
- Native working-tree source capture is preserved. Every input was additionally compared against its committed base blob, and save verifies base and current bytes. The off-main base is retained by annotated provenance tag for fresh clones.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T004717Z-cerumen-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: cerumen'
started_at: '2026-10-16T00:25:14Z'
finished_at: '2026-10-16T00:47:17Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected record and sources; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Removed only the reviewed GOLD parent contribution UBERON:0013211. All independent
  genera, source IDs/paths/counts/units, taxa, native identities and statuses are
  preserved. No unresolved predecessor finding remains in this exact target scope.
source:
  git_revision: 5d98511b90fb848de1718404d2bf452ba2799e06
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
    sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 7b7e21d2fa3350efb85fc3cf79725465c09adba8b4fe100b004813deb8a2eed7
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
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
  - path: data/habitats/host_associated/cerumen.yaml
    sha256: 1fcecff38df7f30fe43f4bcbdb015afc6059c14a3e6bdf4d7ae533af1cb7c303
    role: target
  - path: data/habitats/host_associated/cerumen_gland.yaml
    sha256: 8eee2c3b59c3559b06409cabcc87609a7fc6bd932d3f36cb91f69ad19a133916
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
  - path: history/mappings/cecal_csf_cerumen_review/2026-10-16T001333Z-codex-gpt-5-76d2d7.yaml
    sha256: b83832e70b4b73620eeaad1de47539ba3508fa8a3b968196e9b53275b3e21bd8
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261015T235751Z-cerumen-record/review.yaml
    sha256: 48eb4a8817e9c8f544d95ca6a20ceef654af4269ed793eaadf4f9ecc34de40fb
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
  - path: tests/test_cecal_csf_cerumen_review_repairs.py
    sha256: c0a9b3e0d1ef3957e3dbc67172c3066ffb687922a68e104d0eb5b64fac5b9851
    role: context
targets:
- target_id: UBERON:0002297
  path: data/habitats/host_associated/cerumen.yaml
  label: cerumen
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
  description: Full current-record assessment and explicit disposition of every predecessor
    finding after the bounded parent correction.
  selection: One of twelve repaired targets in the 24-record cecal-through-cervical
    cohort; no additional sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0002297
  exclusions:
  - target: Other habitats and export conformance
    reason: No full-corpus scientific approval, upstream Polyps correction or current
      kg-microbe SSSOM/KGX certification.
checks:
- check_id: C9
  name: just validate data/habitats/host_associated/cerumen.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/cerumen.yaml
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: "Executed 2026-10-16T00:17:08Z through 2026-10-16T00:17:10Z. No issues\
    \ found\n uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class\
    \ HabitatRecord data/habitats/host_associated/cerumen.yaml"
  scope_note: Schema for this target; strict for all 24 cohort records; other checks
    retain full-corpus scope.
- check_id: C12
  name: just validate-strict data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml
    data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml
    data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml
    data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml
    data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml
    data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml
    data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml
    data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml
    data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml
    data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml
    data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml
    data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml
    data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml
    data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml
    data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml
    data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml
    data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml
    data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml
    data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml
    data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml
    data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml
    data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml
    data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: "Executed 2026-10-16T00:14:39Z through 2026-10-16T00:14:46Z. uv run python\
    \ scripts/validate_strict.py data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml\
    \ data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml\
    \ data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml\
    \ data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml\
    \ data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml\
    \ data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml\
    \ data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml\
    \ data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml\
    \ data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml\
    \ data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml\
    \ data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml\
    \ data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Schema for this target; strict for all 24 cohort records; other checks
    retain full-corpus scope.
- check_id: C13
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: 'Executed 2026-10-16T00:14:46Z through 2026-10-16T00:14:56Z. No issues
    found

    830 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Schema for this target; strict for all 24 cohort records; other checks
    retain full-corpus scope.
- check_id: C14
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: "Executed 2026-10-16T00:14:56Z through 2026-10-16T00:14:56Z. provenance\
    \ current: 14 committed inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Schema for this target; strict for all 24 cohort records; other checks
    retain full-corpus scope.
- check_id: C15
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: "Executed 2026-10-16T00:14:56Z through 2026-10-16T00:15:12Z. expected 3209\
    \ records, found 3209 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\
    \ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Schema for this target; strict for all 24 cohort records; other checks
    retain full-corpus scope.
- check_id: C16
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: "Executed 2026-10-16T00:15:12Z through 2026-10-16T00:15:16Z. validated\
    \ 32 causal-graph curation file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Schema for this target; strict for all 24 cohort records; other checks
    retain full-corpus scope.
- check_id: C17
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: "Executed 2026-10-16T00:15:16Z through 2026-10-16T00:15:34Z. term-request\
    \ table is current (110 terms)\n uv run python scripts/build_term_requests.py\
    \ --check"
  scope_note: Schema for this target; strict for all 24 cohort records; other checks
    retain full-corpus scope.
- check_id: C18
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: "Executed 2026-10-16T00:15:34Z through 2026-10-16T00:16:23Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n\
    \ uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Schema for this target; strict for all 24 cohort records; other checks
    retain full-corpus scope.
- check_id: C19
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_cecal_csf_cerumen_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_cecal_csf_cerumen_review_repairs.py
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: 'Executed 2026-10-16T00:16:23Z through 2026-10-16T00:16:29Z. ..                                                                       [100%]

    2 passed in 5.66s'
  scope_note: Schema for this target; strict for all 24 cohort records; other checks
    retain full-corpus scope.
- check_id: C20
  name: git diff --check 0eb609a7ddb34925067116af806e26c165e10678
  status: passed
  required: true
  command: git diff --check 0eb609a7ddb34925067116af806e26c165e10678
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: 'Executed 2026-10-16T00:16:29Z through 2026-10-16T00:16:30Z. '
  scope_note: Schema for this target; strict for all 24 cohort records; other checks
    retain full-corpus scope.
- check_id: CCI
  name: Exact-revision full QC and archive contract
  status: passed
  required: true
  command: gh run view 38829324804 --repo CultureBotAI/HabitatMech --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - UBERON:0002297
  summary: Verified 2026-10-16T00:46:17Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38829324804
  scope_note: Exact repaired scientific-input revision; new successors still require
    post-save and final-head checks.
- check_id: CREF
  name: Standalone evidence-reference validator applicability
  status: not_applicable
  required: false
  target_ids:
  - UBERON:0002297
  summary: No standalone citation/reference validator is documented for these evidence-free
    generated records. Target EvidenceItems and causal edges are absent. Stable source
    and ontology/taxon references were checked manually and with documented native
    gates; current-decision primary citations were separately verified where present.
  scope_note: No command or exit code is invented for an unavailable/nonapplicable
    checker. Full-corpus causal validation ran separately.
evidence:
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000382/graph
  locator: UBERON_0000382-graph.json
  accessed_at: '2026-10-15T23:42:41Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000382",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001820", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000382",
    "target": "http://purl.obolibrary.org/obo/UBERON_0012177", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000382",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001003", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 6501c9c637530f1ac47913f3eaac8ceccc14ee7d9f8b5beff0fe7aeff6799c91
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000382
  locator: UBERON_0000382.json
  accessed_at: '2026-10-15T23:42:40Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0000382",
    "label": "apocrine sweat gland", "is_obsolete": false, "description": ["Apocrine
    sweat glands are sweat glands composed of a coiled secretory portion located at
    the junction of the dermis and subcutaneous fat, from which a straight portion
    inserts and secretes into the infundibular portion of the hair follicle. The ducts
    of apocrine glands open into the canals of hair follicles. The stimulus for the
    secretion of apocrine sweat glands is adrenaline, which is a hormone carried in
    the blood[WP]."]}'
  snapshot_sha256: 5534f7b704937a134a716b7b3bb9c8047e0eab51ed4a61048b3a9495cf292994
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001089/graph
  locator: UBERON_0001089-graph.json
  accessed_at: '2026-10-15T23:42:44Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001089",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000456", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001089",
    "target": "http://purl.obolibrary.org/obo/UBERON_0006314", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001089",
    "target": "http://purl.obolibrary.org/obo/PATO_0001548", "uri": "http://purl.obolibrary.org/obo/RO_0000086",
    "label": "has quality"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001089",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001820", "uri": "http://purl.obolibrary.org/obo/RO_0003001",
    "label": "produced by"}]'
  snapshot_sha256: c265337f350ec0311974c6fe3e86b5aaf60882acc2a47bde18ea5eb4c7e752e4
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001089
  locator: UBERON_0001089.json
  accessed_at: '2026-10-15T23:42:43Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0001089",
    "label": "sweat", "is_obsolete": false, "description": ["Secretion produced by
    a sweat gland."]}'
  snapshot_sha256: f0214b8fd8d055824ccc30dfae1cd808f81b234b8150a681c5ac3fcd2e4a52ba
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002297/graph
  locator: UBERON_0002297-graph.json
  accessed_at: '2026-10-15T23:42:46Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0002297",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001089", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002297",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000382", "uri": "http://purl.obolibrary.org/obo/RO_0003001",
    "label": "produced by"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002297",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001352", "uri": "http://purl.obolibrary.org/obo/RO_0001025",
    "label": "located in"}]'
  snapshot_sha256: c9487837e2c4f2307ed84d4298451e719a32eb755c8e7f6642b42473b96d5fa7
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002297
  locator: UBERON_0002297.json
  accessed_at: '2026-10-15T23:42:46Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0002297",
    "label": "cerumen", "is_obsolete": false, "description": ["The yellow or brown
    waxy secretions produced by vestigial apocrine sweat glands in the external ear
    canal[MESH]."]}'
  snapshot_sha256: c24528e9b596c265ae0b242dcd53c9174f3f4a870043c5a0b68a293849cfd38e
- evidence_id: EX7
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0013211/graph
  locator: UBERON_0013211-graph.json
  accessed_at: '2026-10-15T23:42:52Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0013211",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000382", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0013211",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001352", "uri": "http://purl.obolibrary.org/obo/RO_0001025",
    "label": "located in"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0013211",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001691", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0013211",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002297", "uri": "http://purl.obolibrary.org/obo/RO_0003000",
    "label": "produces"}]'
  snapshot_sha256: 8a358cb6305e9a4fc52d9cf22d586c28881ff128300c6aeb5a05252ce42c6752
- evidence_id: EX8
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0013211
  locator: UBERON_0013211.json
  accessed_at: '2026-10-15T23:42:51Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0013211",
    "label": "cerumen gland", "is_obsolete": false, "description": ["A specialized
    sudoriferous gland (sweat glands) located subcutaneously in the external auditory
    canal."]}'
  snapshot_sha256: 541c94024c5e40f7a157f691df64df4368229195b9fed1ee2e7cb8c2b680ca0e
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/cerumen.yaml
  locator: Entire regenerated target
  accessed_at: '2026-10-16T00:47:17Z'
  support: supports
  summary: '{"identifier": "UBERON:0002297", "label": "cerumen", "definition": "The
    yellow or brown waxy secretions produced by vestigial apocrine sweat glands in
    the external ear canal[MESH].", "definition_source": "UBERON", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "REVIEWED",
    "synonyms": [{"synonym_text": "Cerumen/Earwax", "synonym_type": "EXACT_SYNONYM",
    "source": "GOLD"}, {"synonym_text": "ear wax", "synonym_type": "EXACT_SYNONYM",
    "source": "UBERON"}, {"synonym_text": "earwax", "synonym_type": "EXACT_SYNONYM",
    "source": "UBERON"}], "parent_habitats": ["UBERON:0001089"], "source_attestations":
    [{"source": "GOLD", "source_id": "gold.ecosystem:7025", "source_label": "Cerumen/Earwax",
    "source_path": "Host-associated > Mammals: Human > Integumentary system > Ceruminous
    glands > Cerumen/Earwax", "mapping_predicate": "skos:exactMatch"}], "curation_history":
    [{"timestamp": "2026-08-16T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND",
    "changes": "Grounded to UBERON:0002297 ''cerumen'' (EXACT). Variant-match review
    (#12): the seeder grounds on exact labels only, so GOLD''s slash and plural conventions
    hid a term that says exactly this. Cerumen is earwax, defined by UBERON as the
    waxy secretion of the external auditory canal. Path: Host-associated > Mammals:
    Human > Integumentary system > Ceruminous glands > Cerumen/Earwax (source concept
    habitatmech:GOLD.aea4a5fe91)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator":
    "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from
    data/raw/ inventories; attested by GOLD. Grounding: EXACT."}, {"timestamp": "2026-10-15T00:00:00Z",
    "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded
    GOLD source-path parent contribution UBERON:0013211 for habitatmech:GOLD.aea4a5fe91
    (Host-associated > Mammals: Human > Integumentary system > Ceruminous glands >
    Cerumen/Earwax). Review https://github.com/CultureBotAI/HabitatMech/issues/2214
    : UBERON cerumen denotes earwax with supported sweat genus. It is a product of
    glands, not a subtype of the cerumen gland. Keep the reviewed ITEM identity, aliases
    and independent genus; exclude only the GOLD gland context contribution. No source
    observations or universal chemical measurements should be invented. Exclude only
    this exact source contribution; preserve independent valid genera and source observations.
    Mapping endpoint #1398, Ceros source meaning #325 and upstream Polyps identity
    #2171 are not resolved by this hierarchy guard."}]}'
  snapshot_sha256: 1fcecff38df7f30fe43f4bcbdb015afc6059c14a3e6bdf4d7ae533af1cb7c303
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T235751Z-cerumen-record/review.yaml
  locator: Exact immutable predecessor and all findings
  accessed_at: '2026-10-16T00:47:17Z'
  support: supports
  summary: Original observation remains byte-identical. Every finding retains its
    issue key, target and exact predecessor.
  snapshot_sha256: 48eb4a8817e9c8f544d95ca6a20ceef654af4269ed793eaadf4f9ecc34de40fb
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_cecal_csf_cerumen_review_repairs.py
  locator: Full-corpus counterfactual and exact parent/source preservation
  accessed_at: '2026-10-16T00:47:17Z'
  support: supports
  summary: The regression proves exactly twelve record documents change, only parent_habitats
    and one appended generated event change, and all identities and other fields/records
    remain identical. Public issue hrefs are checked with the template filter.
  snapshot_sha256: c0a9b3e0d1ef3957e3dbc67172c3066ffb687922a68e104d0eb5b64fac5b9851
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict broader hierarchy and maintained ownership
  accessed_at: '2026-10-16T00:47:17Z'
  support: supports
  summary: Context, anatomical containment and source-path proximity do not imply
    is-a.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EHISTORY
  kind: authority
  reference: history/README.md
  locator: Immutable session audit versus generated projection
  accessed_at: '2026-10-16T00:47:17Z'
  support: supports
  summary: Committed sessions and saved reviews remain append-only.
  snapshot_sha256: 819361a711697f96ff9c1aa0b27e94302547970b3b54777d67ec1449db5e543a
- evidence_id: EI13
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact keyed rows 11
  accessed_at: '2026-10-16T00:47:17Z'
  support: supports
  summary: '[[11, "habitatmech:GOLD.aea4a5fe91\tHost-associated > Mammals: Human >
    Integumentary system > Ceruminous glands > Cerumen/Earwax\tUBERON:0013211\tcodex-gpt-5\t2026-10-15\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2214 : UBERON cerumen denotes
    earwax with supported sweat genus. It is a product of glands, not a subtype of
    the cerumen gland. Keep the reviewed ITEM identity, aliases and independent genus;
    exclude only the GOLD gland context contribution. No source observations or universal
    chemical measurements should be invented. Exclude only this exact source contribution;
    preserve independent valid genera and source observations. Mapping endpoint #1398,
    Ceros source meaning #325 and upstream Polyps identity #2171 are not resolved
    by this hierarchy guard."]]'
  snapshot_sha256: 7b7e21d2fa3350efb85fc3cf79725465c09adba8b4fe100b004813deb8a2eed7
- evidence_id: EI14
  kind: record_content
  reference: curation/decisions.tsv
  locator: Exact keyed rows 1661
  accessed_at: '2026-10-16T00:47:17Z'
  support: supports
  summary: '[[1661, "habitatmech:GOLD.aea4a5fe91\tGROUND\tUBERON:0002297\tcerumen\tEXACT\tclaude-opus-5\t2026-08-16\tVariant-match
    review (#12): the seeder grounds on exact labels only, so GOLD''s slash and plural
    conventions hid a term that says exactly this. Cerumen is earwax, defined by UBERON
    as the waxy secretion of the external auditory canal. Path: Host-associated >
    Mammals: Human > Integumentary system > Ceruminous glands > Cerumen/Earwax\tITEM\t\t"]]'
  snapshot_sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
assessments:
- assessment_id: A1
  area: consistency
  topic: Bounded repair and preservation
  outcome: supported
  summary: Removed only the reviewed GOLD parent contribution UBERON:0013211. All
    independent genera, source IDs/paths/counts/units, taxa, native identities and
    statuses are preserved. No unresolved predecessor finding remains in this exact
    target scope.
  target_ids:
  - UBERON:0002297
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI13
  - EI14
- assessment_id: A2
  area: identity
  topic: Current identity, definition, aliases and strict ancestry
  outcome: supported
  summary: 'UBERON:0002297: cerumen, EXACT/REVIEWED, parents ["UBERON:0001089"]. No
    unsupported replacement genus or optional definition is invented.'
  target_ids:
  - UBERON:0002297
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI13
  - EI14
- assessment_id: A3
  area: quantity
  topic: Frozen nonadditive source evidence
  outcome: supported
  summary: '[{"source": "GOLD", "source_id": "gold.ecosystem:7025", "source_label":
    "Cerumen/Earwax", "source_path": "Host-associated > Mammals: Human > Integumentary
    system > Ceruminous glands > Cerumen/Earwax", "mapping_predicate": "skos:exactMatch"}].
    Entire source attestations and taxon fields are unchanged by the counterfactual
    regression.'
  target_ids:
  - UBERON:0002297
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI13
  - EI14
- assessment_id: A4
  area: representation
  topic: Exact finding lineage and open scope
  outcome: supported
  summary: Every predecessor finding retains its exact target and issue key. Parent
    correction does not resolve Ceros source meaning, the upstream Polyps identity
    or shared mapping endpoints. No export-conformance certification.
  target_ids:
  - UBERON:0002297
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI13
  - EI14
- assessment_id: A5
  area: completeness
  topic: Optional claims and current evidence limits
  outcome: supported
  summary: No parameters, causal edges or characteristic-presence claims were added.
    Inspected primary and taxonomy evidence remains bounded to its original claim;
    zero counts are not biological absence.
  target_ids:
  - UBERON:0002297
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI13
  - EI14
findings:
- finding_id: F1
  issue_key: cerumen-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is not a supported broader habitat class
  description: Corrected through maintained input and native regeneration. Excluded
    only exact guarded GOLD contribution UBERON:0013211; independently valid genera,
    original source observations and native identity/status remain unchanged.
  target_ids:
  - UBERON:0002297
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI13
  - EI14
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2214
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T235751Z-cerumen-record
    finding_id: F1
  disposition_reason: Excluded only exact guarded GOLD contribution UBERON:0013211;
    independently valid genera, original source observations and native identity/status
    remain unchanged.
actions: []
limitations:
- Source counts, ranks and scores do not establish prevalence, viability or characteristic
  presence. Original specimen-level evidence for every source member has not been
  reconstructed.
- Configured label validation skipped 2063 no-adapter pairs; displayed TaxIds were
  separately resolved against current NCBI including aliases.
- 'iModulonDB is not applicable: target assertions contain no gene, regulator or expression-module
  claim. No paid research or native status promotion was performed.'
- Same-agent adversarial assessment, not independent approval. Recorded full QC covers
  exact repaired inputs before this new successor; final-head and queue checks remain
  publication gates.
notes:
- Native working-tree source capture is preserved. Every input was additionally compared
  against its committed base blob, and save verifies base and current bytes. The off-main
  base is retained by annotated provenance tag for fresh clones.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T235751Z-cerumen-record
  relationship: Exact predecessor; every finding explicitly reconciled without changing
    earlier bundles.
```
