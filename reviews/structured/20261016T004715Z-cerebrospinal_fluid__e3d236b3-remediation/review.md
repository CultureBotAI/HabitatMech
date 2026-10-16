# Remediation review: cerebrospinal_fluid__e3d236b3

- Review: 20261016T004715Z-cerebrospinal_fluid__e3d236b3-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T00:25:12Z
- Finished UTC: 2026-10-16T00:47:15Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed only the reviewed GOLD parent contribution habitatmech:GOLD.54eda01cf1. All independent genera, source IDs/paths/counts/units, taxa, native identities and statuses are preserved. Remaining predecessor findings stay explicitly open.

## Scope And Provenance

Full current-record assessment and explicit disposition of every predecessor finding after the bounded parent correction.

Selection: One of twelve repaired targets in the 24-record cecal-through-cervical cohort; no additional sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5d98511b90fb848de1718404d2bf452ba2799e06.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.2777b651ed | data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml | generated | Cerebrospinal fluid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml | passed | True | habitatmech:GOLD.2777b651ed | Executed 2026-10-16T00:17:01Z through 2026-10-16T00:17:03Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml |
| just validate-strict data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml | passed | True | habitatmech:GOLD.2777b651ed | Executed 2026-10-16T00:14:39Z through 2026-10-16T00:14:46Z. uv run python scripts/validate_strict.py data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cecum__d677e5d7.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml data/habitats/host_associated/cecum_mucosa.yaml data/habitats/host_associated/cell_culture.yaml data/habitats/host_associated/cell_line.yaml data/habitats/host_associated/cell_line__59b8224e.yaml data/habitats/host_associated/cell_line__d7fc8c60.yaml data/habitats/host_associated/cellulitis.yaml data/habitats/host_associated/central_nervous_system.yaml data/habitats/host_associated/cephalochordata.yaml data/habitats/host_associated/cephalothorax.yaml data/habitats/host_associated/cerebellum.yaml data/habitats/host_associated/cerebrospinal_fluid.yaml data/habitats/host_associated/cerebrospinal_fluid__93998265.yaml data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml data/habitats/host_associated/cerebrospinal_fluid__f9e9497c.yaml data/habitats/host_associated/ceros.yaml data/habitats/host_associated/cerumen.yaml data/habitats/host_associated/cerumen_gland.yaml data/habitats/host_associated/cervical.yaml data/habitats/host_associated/cervical_adenocarcinoma_cell.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.2777b651ed | Executed 2026-10-16T00:14:46Z through 2026-10-16T00:14:56Z. No issues found<br>830 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.2777b651ed | Executed 2026-10-16T00:14:56Z through 2026-10-16T00:14:56Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.2777b651ed | Executed 2026-10-16T00:14:56Z through 2026-10-16T00:15:12Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.2777b651ed | Executed 2026-10-16T00:15:12Z through 2026-10-16T00:15:16Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.2777b651ed | Executed 2026-10-16T00:15:16Z through 2026-10-16T00:15:34Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.2777b651ed | Executed 2026-10-16T00:15:34Z through 2026-10-16T00:16:23Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_cecal_csf_cerumen_review_repairs.py | passed | True | habitatmech:GOLD.2777b651ed | Executed 2026-10-16T00:16:23Z through 2026-10-16T00:16:29Z. ..                                                                       [100%]<br>2 passed in 5.66s |
| git diff --check 0eb609a7ddb34925067116af806e26c165e10678 | passed | True | habitatmech:GOLD.2777b651ed | Executed 2026-10-16T00:16:29Z through 2026-10-16T00:16:30Z.  |
| Exact-revision full QC and archive contract | passed | True | habitatmech:GOLD.2777b651ed | Verified 2026-10-16T00:46:17Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38829324804 |
| Standalone evidence-reference validator applicability | not_applicable | False | habitatmech:GOLD.2777b651ed | No standalone citation/reference validator is documented for these evidence-free generated records. Target EvidenceItems and causal edges are absent. Stable source and ontology/taxon references were checked manually and with documented native gates; current-decision primary citations were separately verified where present. |

## Scientific And Domain Assessments

### Bounded repair and preservation

consistency: supported. Targets: habitatmech:GOLD.2777b651ed.

Removed only the reviewed GOLD parent contribution habitatmech:GOLD.54eda01cf1. All independent genera, source IDs/paths/counts/units, taxa, native identities and statuses are preserved. Remaining predecessor findings stay explicitly open.

### Current identity, definition, aliases and strict ancestry

identity: supported. Targets: habitatmech:GOLD.2777b651ed.

habitatmech:GOLD.2777b651ed: Cerebrospinal fluid, NARROW/SEEDED, parents ["UBERON:0001359"]. No unsupported replacement genus or optional definition is invented.

### Frozen nonadditive source evidence

quantity: supported. Targets: habitatmech:GOLD.2777b651ed.

[{"source": "GOLD", "source_id": "gold.ecosystem:6774", "source_label": "Cerebrospinal fluid", "source_path": "Host-associated &gt; Mammals &gt; Nervous system &gt; Subarachnoid space &gt; Cerebrospinal fluid", "mapping_predicate": "skos:narrowMatch", "assertion_count": 1, "assertion_unit": "ORGANISM"}]. Entire source attestations and taxon fields are unchanged by the counterfactual regression.

### Exact finding lineage and open scope

representation: concern. Targets: habitatmech:GOLD.2777b651ed.

Every predecessor finding retains its exact target and issue key. Parent correction does not resolve Ceros source meaning, the upstream Polyps identity or shared mapping endpoints. No export-conformance certification.

### Optional claims and current evidence limits

completeness: supported. Targets: habitatmech:GOLD.2777b651ed.

No parameters, causal edges or characteristic-presence claims were added. Inspected primary and taxonomy evidence remains bounded to its original claim; zero counts are not biological absence.

## Findings

### F1: Source context is not a supported broader habitat class

major / resolved / confirmed; issue key: cerebrospinal-fluid--e3d236b3-context-parent.

Corrected through maintained input and native regeneration. Excluded only exact guarded GOLD contribution habitatmech:GOLD.54eda01cf1; independently valid genera, original source observations and native identity/status remain unchanged.

Disposition: Excluded only exact guarded GOLD contribution habitatmech:GOLD.54eda01cf1; independently valid genera, original source observations and native identity/status remain unchanged.

### F2: Narrow predicate uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: cerebrospinal-fluid--e3d236b3-mapping-endpoint-contract.

Reassessed; remains unresolved. The source mint still emits narrowMatch relative to an undeclared ontology-parent endpoint. Removing a context parent does not resolve the shared schema/producer/consumer contract.

Disposition: The source mint still emits narrowMatch relative to an undeclared ontology-parent endpoint. Removing a context parent does not resolve the shared schema/producer/consumer contract.

## Recommended Actions And Acceptance Checks

### ACT2

The native route retains the GOLD source mint but emits narrowMatch with reference to its ontology parent, while SourceAttestation declares source-to-record endpoints. Reconcile schema, producer and consumers under #1398 without merging host scopes or blindly reversing predicates. This is not a formal SKOS self-link prohibition or export-conformance certification. No repair is performed by this review.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000315/graph; UBERON_0000315-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000315", "target": "http://purl.obolibrary.org/obo/UBERON_0000464", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000315", "target": "http://purl.obolibrary.org/obo/UBERON_0001359", "uri": "http://purl.obolibrary.org/obo/RO_0001015", "label": "location of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000315", "target": "http://purl.obolibrary.org/obo/UBERON_0001981", "uri": "http://purl.obolibrary.org/obo/RO_0001015", "label": "location of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000315", "target": "http://purl.obolibrary.org/obo/UBERON_0002361", "uri": "http://purl.obolibrary.org/obo/RO_0002220", "label": "adjacent to"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000315", "target": "http://purl.obolibrary.org/obo/UBERON_0002362", "uri": "http://purl.obolibrary.org/obo/RO_0002220", "label": "adjacent to"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000315", "target": "http://purl.obolibrary.org/obo/UBERON_0010743", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000315; UBERON_0000315.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0000315", "label": "subarachnoid space", "is_obsolete": false, "description": ["The space between the arachnoid and pia mater."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001359/graph; UBERON_0001359-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001359", "target": "http://purl.obolibrary.org/obo/UBERON_0007779", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001359", "target": "http://purl.obolibrary.org/obo/UBERON_0001886", "uri": "http://purl.obolibrary.org/obo/uberon/core#filtered_through", "label": "filtered through"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001359", "target": "http://purl.obolibrary.org/obo/UBERON_0002307", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001359", "target": "http://purl.obolibrary.org/obo/UBERON_0005281", "uri": "http://purl.obolibrary.org/obo/RO_0001025", "label": "located in"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001359; UBERON_0001359.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0001359", "label": "cerebrospinal fluid", "is_obsolete": false, "description": ["A clear, colorless, bodily fluid, that occupies the subarachnoid space and the ventricular system around and inside the brain and spinal cord."]} |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007779/graph; UBERON_0007779-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0007779", "target": "http://purl.obolibrary.org/obo/UBERON_0006314", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007779", "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007779", "target": "http://purl.obolibrary.org/obo/PATO_0001548", "uri": "http://purl.obolibrary.org/obo/RO_0000086", "label": "has quality"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007779", "target": "http://purl.obolibrary.org/obo/UBERON_0001969", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007779", "target": "http://purl.obolibrary.org/obo/UBERON_0001982", "uri": "http://purl.obolibrary.org/obo/uberon/core#filtered_through", "label": "filtered through"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007779; UBERON_0007779.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0007779", "label": "transudate", "is_obsolete": false, "description": ["Any bodily fluid that has passed through a membrane such as the capillary wall, as a result of unbalanced hydrostatic and osmotic forces."]} |
| EAFTER | data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml; Entire regenerated target | supports | {"identifier": "habitatmech:GOLD.2777b651ed", "label": "Cerebrospinal fluid", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001359"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6774", "source_label": "Cerebrospinal fluid", "source_path": "Host-associated &gt; Mammals &gt; Nervous system &gt; Subarachnoid space &gt; Cerebrospinal fluid", "mapping_predicate": "skos:narrowMatch", "assertion_count": 1, "assertion_unit": "ORGANISM"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.54eda01cf1 for habitatmech:GOLD.2777b651ed (Host-associated &gt; Mammals &gt; Nervous system &gt; Subarachnoid space &gt; Cerebrospinal fluid). Review https://github.com/CultureBotAI/HabitatMech/issues/2214 : Mammal cerebrospinal fluid retains a valid generic CSF genus and one ORGANISM assertion. The subarachnoid space is a containing site, not a broader fluid class. Preserve the host-specific mint and independent genus while addressing that parent and the separate narrowMatch endpoint contract. Exclude only this exact source contribution; preserve independent valid genera and source observations. Mapping endpoint #1398, Ceros source meaning #325 and upstream Polyps identity #2171 are not resolved by this hierarchy guard."}]} |
| EPREV | reviews/structured/20261015T235750Z-cerebrospinal_fluid__e3d236b3-record/review.yaml; Exact immutable predecessor and all findings | supports | Original observation remains byte-identical. Every finding retains its issue key, target and exact predecessor. |
| ETEST | tests/test_cecal_csf_cerumen_review_repairs.py; Full-corpus counterfactual and exact parent/source preservation | supports | The regression proves exactly twelve record documents change, only parent_habitats and one appended generated event change, and all identities and other fields/records remain identical. Public issue hrefs are checked with the template filter. |
| ERULE | docs/CURATION.md; Strict broader hierarchy and maintained ownership | supports | Context, anatomical containment and source-path proximity do not imply is-a. |
| EHISTORY | history/README.md; Immutable session audit versus generated projection | supports | Committed sessions and saved reviews remain append-only. |
| EI11 | curation/gold_parent_exclusions.tsv; Exact keyed rows 8 | supports | [[8, "habitatmech:GOLD.2777b651ed\tHost-associated &gt; Mammals &gt; Nervous system &gt; Subarachnoid space &gt; Cerebrospinal fluid\thabitatmech:GOLD.54eda01cf1\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2214 : Mammal cerebrospinal fluid retains a valid generic CSF genus and one ORGANISM assertion. The subarachnoid space is a containing site, not a broader fluid class. Preserve the host-specific mint and independent genus while addressing that parent and the separate narrowMatch endpoint contract. Exclude only this exact source contribution; preserve independent valid genera and source observations. Mapping endpoint #1398, Ceros source meaning #325 and upstream Polyps identity #2171 are not resolved by this hierarchy guard."]] |
| EI12 | curation/decisions.tsv; Exact keyed rows  | supports | [] |

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
review_id: 20261016T004715Z-cerebrospinal_fluid__e3d236b3-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: cerebrospinal_fluid__e3d236b3'
started_at: '2026-10-16T00:25:12Z'
finished_at: '2026-10-16T00:47:15Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected record and sources; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: Removed only the reviewed GOLD parent contribution habitatmech:GOLD.54eda01cf1.
  All independent genera, source IDs/paths/counts/units, taxa, native identities and
  statuses are preserved. Remaining predecessor findings stay explicitly open.
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
  - path: data/habitats/host_associated/cerebrospinal_fluid__b2fc1889.yaml
    sha256: d0450847e04f5e17b5cc3e330639a50a1d5d3ab94f0b72af1ce02cc693336190
    role: context
  - path: data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml
    sha256: d8108a9191dd4aa3c3d2961dbcd872580de813e76c882c861929b1cabdb95028
    role: target
  - path: data/habitats/host_associated/subarachnoid_space__3885f8ab.yaml
    sha256: ff5a82bc85b1fb6eef148e75f3d108850b7718c7eb09fb30c21d9b5c08f89e03
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
  - path: reviews/structured/20261015T235750Z-cerebrospinal_fluid__e3d236b3-record/review.yaml
    sha256: 50cafce49414d776f2ccaf4664be2bad3c347e41cb696b589b5c43504bb70cef
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
- target_id: habitatmech:GOLD.2777b651ed
  path: data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml
  label: Cerebrospinal fluid
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
  - habitatmech:GOLD.2777b651ed
  exclusions:
  - target: Other habitats and export conformance
    reason: No full-corpus scientific approval, upstream Polyps correction or current
      kg-microbe SSSOM/KGX certification.
checks:
- check_id: C6
  name: just validate data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2777b651ed
  summary: "Executed 2026-10-16T00:17:01Z through 2026-10-16T00:17:03Z. No issues\
    \ found\n uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class\
    \ HabitatRecord data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml"
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
  - habitatmech:GOLD.2777b651ed
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
  - habitatmech:GOLD.2777b651ed
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
  - habitatmech:GOLD.2777b651ed
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
  - habitatmech:GOLD.2777b651ed
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
  - habitatmech:GOLD.2777b651ed
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
  - habitatmech:GOLD.2777b651ed
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
  - habitatmech:GOLD.2777b651ed
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
  - habitatmech:GOLD.2777b651ed
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
  - habitatmech:GOLD.2777b651ed
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
  - habitatmech:GOLD.2777b651ed
  summary: Verified 2026-10-16T00:46:17Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38829324804
  scope_note: Exact repaired scientific-input revision; new successors still require
    post-save and final-head checks.
- check_id: CREF
  name: Standalone evidence-reference validator applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.2777b651ed
  summary: No standalone citation/reference validator is documented for these evidence-free
    generated records. Target EvidenceItems and causal edges are absent. Stable source
    and ontology/taxon references were checked manually and with documented native
    gates; current-decision primary citations were separately verified where present.
  scope_note: No command or exit code is invented for an unavailable/nonapplicable
    checker. Full-corpus causal validation ran separately.
evidence:
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000315/graph
  locator: UBERON_0000315-graph.json
  accessed_at: '2026-10-15T23:42:39Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000315",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000464", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000315",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001359", "uri": "http://purl.obolibrary.org/obo/RO_0001015",
    "label": "location of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000315",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001981", "uri": "http://purl.obolibrary.org/obo/RO_0001015",
    "label": "location of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000315",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002361", "uri": "http://purl.obolibrary.org/obo/RO_0002220",
    "label": "adjacent to"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000315",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002362", "uri": "http://purl.obolibrary.org/obo/RO_0002220",
    "label": "adjacent to"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000315",
    "target": "http://purl.obolibrary.org/obo/UBERON_0010743", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 5ef0d6e8470be276a1d16ac8ba1b348d6ad5b9914c6b25ad739ef492ce2df6cb
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000315
  locator: UBERON_0000315.json
  accessed_at: '2026-10-15T23:42:38Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0000315",
    "label": "subarachnoid space", "is_obsolete": false, "description": ["The space
    between the arachnoid and pia mater."]}'
  snapshot_sha256: 0d680a24620034d4f5224a54679ccd011d022b81197e9fe5b02a485f4247c093
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001359/graph
  locator: UBERON_0001359-graph.json
  accessed_at: '2026-10-15T23:42:45Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001359",
    "target": "http://purl.obolibrary.org/obo/UBERON_0007779", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001359",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001886", "uri": "http://purl.obolibrary.org/obo/uberon/core#filtered_through",
    "label": "filtered through"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001359",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002307", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001359",
    "target": "http://purl.obolibrary.org/obo/UBERON_0005281", "uri": "http://purl.obolibrary.org/obo/RO_0001025",
    "label": "located in"}]'
  snapshot_sha256: 160d352b22bd9e94522b8688b73da1da8ffee0ba32070fa3e081998116fbe1d1
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001359
  locator: UBERON_0001359.json
  accessed_at: '2026-10-15T23:42:44Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0001359",
    "label": "cerebrospinal fluid", "is_obsolete": false, "description": ["A clear,
    colorless, bodily fluid, that occupies the subarachnoid space and the ventricular
    system around and inside the brain and spinal cord."]}'
  snapshot_sha256: 17bb3b226b7217590f08876f188c4c99933f4fc98036a8c48ae4f031b257d3ac
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007779/graph
  locator: UBERON_0007779-graph.json
  accessed_at: '2026-10-15T23:42:51Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0007779",
    "target": "http://purl.obolibrary.org/obo/UBERON_0006314", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007779",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007779",
    "target": "http://purl.obolibrary.org/obo/PATO_0001548", "uri": "http://purl.obolibrary.org/obo/RO_0000086",
    "label": "has quality"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007779",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001969", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007779",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001982", "uri": "http://purl.obolibrary.org/obo/uberon/core#filtered_through",
    "label": "filtered through"}]'
  snapshot_sha256: 885904431a18885847ed9bef565008b872aaf9b19bccf3c7bc3598c6f74cf3a5
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007779
  locator: UBERON_0007779.json
  accessed_at: '2026-10-15T23:42:50Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0007779",
    "label": "transudate", "is_obsolete": false, "description": ["Any bodily fluid
    that has passed through a membrane such as the capillary wall, as a result of
    unbalanced hydrostatic and osmotic forces."]}'
  snapshot_sha256: 0fec7b87b4bd855853fc10409f75c0b9d6675bb8b442befc81c5b80c4c615930
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/cerebrospinal_fluid__e3d236b3.yaml
  locator: Entire regenerated target
  accessed_at: '2026-10-16T00:47:15Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.2777b651ed", "label": "Cerebrospinal
    fluid", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status":
    "SEEDED", "parent_habitats": ["UBERON:0001359"], "source_attestations": [{"source":
    "GOLD", "source_id": "gold.ecosystem:6774", "source_label": "Cerebrospinal fluid",
    "source_path": "Host-associated > Mammals > Nervous system > Subarachnoid space
    > Cerebrospinal fluid", "mapping_predicate": "skos:narrowMatch", "assertion_count":
    1, "assertion_unit": "ORGANISM"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp":
    "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.54eda01cf1
    for habitatmech:GOLD.2777b651ed (Host-associated > Mammals > Nervous system >
    Subarachnoid space > Cerebrospinal fluid). Review https://github.com/CultureBotAI/HabitatMech/issues/2214
    : Mammal cerebrospinal fluid retains a valid generic CSF genus and one ORGANISM
    assertion. The subarachnoid space is a containing site, not a broader fluid class.
    Preserve the host-specific mint and independent genus while addressing that parent
    and the separate narrowMatch endpoint contract. Exclude only this exact source
    contribution; preserve independent valid genera and source observations. Mapping
    endpoint #1398, Ceros source meaning #325 and upstream Polyps identity #2171 are
    not resolved by this hierarchy guard."}]}'
  snapshot_sha256: d8108a9191dd4aa3c3d2961dbcd872580de813e76c882c861929b1cabdb95028
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T235750Z-cerebrospinal_fluid__e3d236b3-record/review.yaml
  locator: Exact immutable predecessor and all findings
  accessed_at: '2026-10-16T00:47:15Z'
  support: supports
  summary: Original observation remains byte-identical. Every finding retains its
    issue key, target and exact predecessor.
  snapshot_sha256: 50cafce49414d776f2ccaf4664be2bad3c347e41cb696b589b5c43504bb70cef
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_cecal_csf_cerumen_review_repairs.py
  locator: Full-corpus counterfactual and exact parent/source preservation
  accessed_at: '2026-10-16T00:47:15Z'
  support: supports
  summary: The regression proves exactly twelve record documents change, only parent_habitats
    and one appended generated event change, and all identities and other fields/records
    remain identical. Public issue hrefs are checked with the template filter.
  snapshot_sha256: c0a9b3e0d1ef3957e3dbc67172c3066ffb687922a68e104d0eb5b64fac5b9851
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict broader hierarchy and maintained ownership
  accessed_at: '2026-10-16T00:47:15Z'
  support: supports
  summary: Context, anatomical containment and source-path proximity do not imply
    is-a.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EHISTORY
  kind: authority
  reference: history/README.md
  locator: Immutable session audit versus generated projection
  accessed_at: '2026-10-16T00:47:15Z'
  support: supports
  summary: Committed sessions and saved reviews remain append-only.
  snapshot_sha256: 819361a711697f96ff9c1aa0b27e94302547970b3b54777d67ec1449db5e543a
- evidence_id: EI11
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact keyed rows 8
  accessed_at: '2026-10-16T00:47:15Z'
  support: supports
  summary: '[[8, "habitatmech:GOLD.2777b651ed\tHost-associated > Mammals > Nervous
    system > Subarachnoid space > Cerebrospinal fluid\thabitatmech:GOLD.54eda01cf1\tcodex-gpt-5\t2026-10-15\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2214 : Mammal cerebrospinal
    fluid retains a valid generic CSF genus and one ORGANISM assertion. The subarachnoid
    space is a containing site, not a broader fluid class. Preserve the host-specific
    mint and independent genus while addressing that parent and the separate narrowMatch
    endpoint contract. Exclude only this exact source contribution; preserve independent
    valid genera and source observations. Mapping endpoint #1398, Ceros source meaning
    #325 and upstream Polyps identity #2171 are not resolved by this hierarchy guard."]]'
  snapshot_sha256: 7b7e21d2fa3350efb85fc3cf79725465c09adba8b4fe100b004813deb8a2eed7
- evidence_id: EI12
  kind: record_content
  reference: curation/decisions.tsv
  locator: 'Exact keyed rows '
  accessed_at: '2026-10-16T00:47:15Z'
  support: supports
  summary: '[]'
  snapshot_sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
assessments:
- assessment_id: A1
  area: consistency
  topic: Bounded repair and preservation
  outcome: supported
  summary: Removed only the reviewed GOLD parent contribution habitatmech:GOLD.54eda01cf1.
    All independent genera, source IDs/paths/counts/units, taxa, native identities
    and statuses are preserved. Remaining predecessor findings stay explicitly open.
  target_ids:
  - habitatmech:GOLD.2777b651ed
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI11
  - EI12
- assessment_id: A2
  area: identity
  topic: Current identity, definition, aliases and strict ancestry
  outcome: supported
  summary: 'habitatmech:GOLD.2777b651ed: Cerebrospinal fluid, NARROW/SEEDED, parents
    ["UBERON:0001359"]. No unsupported replacement genus or optional definition is
    invented.'
  target_ids:
  - habitatmech:GOLD.2777b651ed
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI11
  - EI12
- assessment_id: A3
  area: quantity
  topic: Frozen nonadditive source evidence
  outcome: supported
  summary: '[{"source": "GOLD", "source_id": "gold.ecosystem:6774", "source_label":
    "Cerebrospinal fluid", "source_path": "Host-associated > Mammals > Nervous system
    > Subarachnoid space > Cerebrospinal fluid", "mapping_predicate": "skos:narrowMatch",
    "assertion_count": 1, "assertion_unit": "ORGANISM"}]. Entire source attestations
    and taxon fields are unchanged by the counterfactual regression.'
  target_ids:
  - habitatmech:GOLD.2777b651ed
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI11
  - EI12
- assessment_id: A4
  area: representation
  topic: Exact finding lineage and open scope
  outcome: concern
  summary: Every predecessor finding retains its exact target and issue key. Parent
    correction does not resolve Ceros source meaning, the upstream Polyps identity
    or shared mapping endpoints. No export-conformance certification.
  target_ids:
  - habitatmech:GOLD.2777b651ed
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI11
  - EI12
- assessment_id: A5
  area: completeness
  topic: Optional claims and current evidence limits
  outcome: supported
  summary: No parameters, causal edges or characteristic-presence claims were added.
    Inspected primary and taxonomy evidence remains bounded to its original claim;
    zero counts are not biological absence.
  target_ids:
  - habitatmech:GOLD.2777b651ed
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI11
  - EI12
findings:
- finding_id: F1
  issue_key: cerebrospinal-fluid--e3d236b3-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is not a supported broader habitat class
  description: Corrected through maintained input and native regeneration. Excluded
    only exact guarded GOLD contribution habitatmech:GOLD.54eda01cf1; independently
    valid genera, original source observations and native identity/status remain unchanged.
  target_ids:
  - habitatmech:GOLD.2777b651ed
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI11
  - EI12
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
    review_id: 20261015T235750Z-cerebrospinal_fluid__e3d236b3-record
    finding_id: F1
  disposition_reason: Excluded only exact guarded GOLD contribution habitatmech:GOLD.54eda01cf1;
    independently valid genera, original source observations and native identity/status
    remain unchanged.
- finding_id: F2
  issue_key: cerebrospinal-fluid--e3d236b3-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow predicate uses an undeclared ontology-parent endpoint
  description: Reassessed; remains unresolved. The source mint still emits narrowMatch
    relative to an undeclared ontology-parent endpoint. Removing a context parent
    does not resolve the shared schema/producer/consumer contract.
  target_ids:
  - habitatmech:GOLD.2777b651ed
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EI11
  - EI12
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T235750Z-cerebrospinal_fluid__e3d236b3-record
    finding_id: F2
  disposition_reason: The source mint still emits narrowMatch relative to an undeclared
    ontology-parent endpoint. Removing a context parent does not resolve the shared
    schema/producer/consumer contract.
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.2777b651ed
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'The native route retains the GOLD source mint but emits narrowMatch
    with reference to its ontology parent, while SourceAttestation declares source-to-record
    endpoints. Reconcile schema, producer and consumers under #1398 without merging
    host scopes or blindly reversing predicates. This is not a formal SKOS self-link
    prohibition or export-conformance certification. No repair is performed by this
    review.'
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact claim, preserving independent valid genera, raw provenance and
    source counts/units. Change native status or mappings only when supported by the
    authorized ITEM assessment; never decrement source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
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
  review_id: 20261015T235750Z-cerebrospinal_fluid__e3d236b3-record
  relationship: Exact predecessor; every finding explicitly reconciled without changing
    earlier bundles.
```
