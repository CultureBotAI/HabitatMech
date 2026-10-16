# Remediation review: crop__310374d9

- Review: 20261016T062916Z-crop__310374d9-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T05:59:21Z
- Finished UTC: 2026-10-16T06:29:16Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed the guarded GOLD context-parent contribution. The non-avian crop source retains its mint UNGROUNDED/REVIEWED without an avian genus or narrow mapping. Source observations and independent genera are preserved. No unresolved predecessor finding remains in this target scope.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding after bounded repair.

Selection: One of ten repaired targets from the column-through-crown-gall cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ee3b5b9ecb9031a9a59dd7ed87da7c97c55a181f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.5446ce4c6d | data/habitats/host_associated/crop__310374d9.yaml | generated | Crop |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/crop__310374d9.yaml | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:47:43Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/crop__310374d9.yaml |
| just validate-strict data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:47:56Z. uv run python scripts/validate_strict.py data/habitats/host_associated/column.yaml data/habitats/host_associated/common_warts.yaml data/habitats/host_associated/compact_bone.yaml data/habitats/host_associated/compact_bone__c00eaa73.yaml data/habitats/host_associated/conjunctiva.yaml data/habitats/host_associated/conjunctiva__482ca0a7.yaml data/habitats/host_associated/conjunctiva__6e913f9c.yaml data/habitats/host_associated/connective_tissue.yaml data/habitats/host_associated/connective_tissue__85a5a212.yaml data/habitats/host_associated/connective_tissue__b37fb9b6.yaml data/habitats/host_associated/coprolite.yaml data/habitats/host_associated/coral.yaml data/habitats/host_associated/corn_silk.yaml data/habitats/host_associated/cornea.yaml data/habitats/host_associated/cornea__2a9b9367.yaml data/habitats/host_associated/cornea__f146d32e.yaml data/habitats/host_associated/cortex.yaml data/habitats/host_associated/crop.yaml data/habitats/host_associated/crop__310374d9.yaml data/habitats/host_associated/crop__3de61c58.yaml data/habitats/host_associated/crop__a03dd0e3.yaml data/habitats/host_associated/crop__d566c329.yaml data/habitats/host_associated/crop_content.yaml data/habitats/host_associated/crown_gall.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:48:04Z. No issues found<br>836 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:48:04Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:48:17Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:48:21Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:48:36Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:49:16Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| uv run pytest -q tests/test_conjunctiva_crop_review_repairs.py --no-cov | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:49:22Z. ..                                                                       [100%]<br>2 passed in 4.92s |
| uv run ruff check . | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:49:22Z. All checks passed! |
| git diff --check | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:49:22Z.  |
| just term-requests | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:55:54Z. wrote curation/term_requests/envo_robot_template.tsv: 110 ENVO terms from 110 source records<br><br>22 examined-ungrounded record(s) still have no request written. Top by volume:<br>      438  Medical-environment                habitatmech:BACDIVE.5e52ea1bba<br>      228  Fruit-Seed                         habitatmech:BACDIVE.ba016fe448<br>       35  Egg                                habitatmech:BACDIVE.d48ce9485d<br>        5  Caeca: Bacteriome                  habitatmech:GOLD.2d506b9526<br>        3  Abdomen                            habitatmech:GOLD.c6b0b54290<br>        2  Crop                               habitatmech:GOLD.5446ce4c6d<br>        1  Thalassic                          habitatmech:GOLD.3fece6dbf7<br>        1  Crop                               habitatmech:GOLD.57011086ca<br>        0  Subtidal zone sediment             habitatmech:GOLD.785879d721<br>        0  Subterranean lake                  habitatmech:GOLD.937bf682c4<br><br>covered 105842 upstream assertions; 713 still unrequested across 22 record(s); 15 examined and deliberately not asked for<br><br>&#96;created by&#96; is empty: it wants pipe-delimited full ORCID IRIs and this script cannot know them.<br> uv run python scripts/build_term_requests.py |
| just docs-stats | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:56:12Z. updated README corpus statistics<br> uv run python scripts/check_docs.py --write |
| just render | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:56:38Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 132 term requests -&gt; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages<br> uv run python scripts/render_pages.py |
| just render-check | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:57:05Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 132 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpiryd8m6g/site<br>pages/ is in step with the corpus<br> uv run python scripts/render_pages.py --check |
| just redirects-check | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:58:39Z. RETIRED.tsv is current (259 redirects)<br> uv run python scripts/build_redirects.py --check |
| uv run ruff check . | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:58:39Z. All checks passed! |
| git diff --check | passed | True | habitatmech:GOLD.5446ce4c6d | Finished 2026-10-16T05:58:40Z.  |
| Exact-revision hosted authoritative QC and archive contract | passed | True | habitatmech:GOLD.5446ce4c6d | Verified 2026-10-16T06:28:52Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38858656719 |

## Scientific And Domain Assessments

### Bounded correction and exact preservation

consistency: supported. Targets: habitatmech:GOLD.5446ce4c6d.

Removed the guarded GOLD context-parent contribution. The non-avian crop source retains its mint UNGROUNDED/REVIEWED without an avian genus or narrow mapping. Source observations and independent genera are preserved. No unresolved predecessor finding remains in this target scope.

### Current anatomical identity and hierarchy

identity: supported. Targets: habitatmech:GOLD.5446ce4c6d.

habitatmech:GOLD.5446ce4c6d: Crop; UNGROUNDED/REVIEWED; parents []. No replacement anatomical identity or definition is fabricated. Remaining exact-identity findings are not concealed.

### Units, counts and observations

quantity: supported. Targets: habitatmech:GOLD.5446ce4c6d.

[{"source": "GOLD", "source_id": "gold.ecosystem:5069", "source_label": "Crop", "source_path": "Host-associated &gt; Annelida &gt; Digestive system &gt; Crop", "assertion_count": 2, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]. Original source counts/units, taxa, scores and parameters remain unchanged; these are not prevalence measurements.

### Predecessor reconciliation

representation: supported. Targets: habitatmech:GOLD.5446ce4c6d.

Every previous finding keeps its stable issue key and exact lineage. Removing invalid non-avian matches does not solve global mapping contract #1398.

### Evidence and lifecycle boundaries

completeness: supported. Targets: habitatmech:GOLD.5446ce4c6d.

Only the two explicit non-avian ITEM decisions change native status. Optional definitions, causal mechanisms and biological absence claims are not invented.

## Findings

### F1: GOLD context is not a strictly broader habitat class

major / resolved / confirmed; issue key: crop--310374d9-context-parent.

Removed only the guarded GOLD source-context contribution habitatmech:GOLD.d011f4b43c. Independent parents and every source observation are retained.

Disposition: Removed only the guarded GOLD source-context contribution habitatmech:GOLD.d011f4b43c. Independent parents and every source observation are retained.

### F2: Mapping uses an undeclared ontology-parent endpoint

major / resolved / confirmed; issue key: crop--310374d9-mapping-endpoint-contract.

An explicit ITEM decision preserves the non-avian source mint UNGROUNDED without the avian genus or narrow mapping. This resolves only the scoped witness; global #1398 is not fixed.

Disposition: An explicit ITEM decision preserves the non-avian source mint UNGROUNDED without the avian genus or narrow mapping. This resolves only the scoped witness; global #1398 is not fixed.

### F3: Avian crop is not a supported non-avian genus

major / resolved / confirmed; issue key: crop--310374d9-avian-genus.

An explicit ITEM decision preserves the non-avian source mint UNGROUNDED without the avian genus or narrow mapping. This resolves only the scoped witness; global #1398 is not fixed.

Disposition: An explicit ITEM decision preserves the non-avian source mint UNGROUNDED without the avian genus or narrow mapping. This resolves only the scoped witness; global #1398 is not fixed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001007/graph; UBERON_0001007-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001007", "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001007", "target": "http://purl.obolibrary.org/obo/GO_0022600", "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001007", "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"}] |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001007; UBERON_0001007.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "UBERON:0001007", "label": "digestive system", "is_obsolete": false, "description": ["Anatomical system that has as its parts the organs devoted to the ingestion, digestion, and assimilation of food and the discharge of residual wastes."], "obo_synonym": null} |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007356/graph; UBERON_0007356-graph.json | context_only | Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0007356", "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007356", "target": "http://purl.obolibrary.org/obo/NCBITaxon_8782", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007356", "target": "http://purl.obolibrary.org/obo/UBERON_0001043", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007356; UBERON_0007356.json | context_only | Current identity, definition, active status and typed synonyms: {"obo_id": "UBERON:0007356", "label": "crop", "is_obsolete": false, "description": ["A pouched enlargement of the gullet of many birds that serves as a receptacle for food and for its preliminary maceration."], "obo_synonym": null} |
| ECANDIDATE | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000301; BTO:0000301 identity and definition | context_only | Active crop concept with a definition spanning birds and other animals, explicitly including insects. This is a broader-genus candidate, not verified exact identity for either taxon-scoped GOLD mint. |
| EAFTER | data/habitats/host_associated/crop__310374d9.yaml; Entire regenerated target YAML | supports | {"identifier": "habitatmech:GOLD.5446ce4c6d", "label": "Crop", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:5069", "source_label": "Crop", "source_path": "Host-associated &gt; Annelida &gt; Digestive system &gt; Crop", "assertion_count": 2, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM reassessment https://github.com/CultureBotAI/HabitatMech/issues/2230 : Current UBERON:0007356 has in-taxon Aves scope (https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007356). This source is non-avian; no replacement genus or exact identity was verified. Retain its mint UNGROUNDED, source observations and native units. Whole-organ context is excluded separately. Path: Host-associated &gt; Annelida &gt; Digestive system &gt; Crop (source concept habitatmech:GOLD.5446ce4c6d)"}, {"timestamp": "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.d011f4b43c for habitatmech:GOLD.5446ce4c6d (Host-associated &gt; Annelida &gt; Digestive system &gt; Crop). Review https://github.com/CultureBotAI/HabitatMech/issues/2229 : Conjunctiva is not an entire visual system; cornea is not an entire eye; cortex is not an entire root; crop is not an entire digestive system, esophagus or foregut; crop contents are not an esophagus. Exclude only exact guarded source-path contributions, retaining independent genera and source observations. This does not settle generic cortex identity or equivalent avian crop sources. Exact target habitatmech:GOLD.5446ce4c6d. Other identity and mapping findings remain separate."}]} |
| EPREV | reviews/structured/20261016T054409Z-crop__310374d9-record/review.yaml; Every immutable baseline finding | supports | Exact predecessor issue keys and findings are reconciled; original inspected source scope is preserved. |
| ETEST | tests/test_conjunctiva_crop_review_repairs.py; Complete full-corpus counterfactual | supports | Exactly ten records differ. The only scientific changes are guarded context-parent removal and two non-avian grounding/predicate/status corrections; source counts, taxa and other fields are invariant. |
| ERULE | docs/CURATION.md; Strict hierarchy, ITEM decisions and source units | supports | Generated artifacts are not edited by hand; native history/status follows exact maintained rows. |
| EH40 | history/mappings/conjunctiva_crop_review_nonavian/2026-10-16T054553Z-codex-gpt-5-64c4ba.yaml; Complete session event | supports | Authorized curation by codex-gpt-5; exact maintained owner and issue retained. |
| EH41 | history/mappings/conjunctiva_crop_review_parents/2026-10-16T054552Z-codex-gpt-5-b09465.yaml; Complete session event | supports | Authorized curation by codex-gpt-5; exact maintained owner and issue retained. |
| EPARENTS | curation/gold_parent_exclusions.tsv; Exact physical TSV rows | supports | [[7, "habitatmech:GOLD.5446ce4c6d\tHost-associated &gt; Annelida &gt; Digestive system &gt; Crop\thabitatmech:GOLD.d011f4b43c\tcodex-gpt-5\t2026-10-16\tReview https://github.com/CultureBotAI/HabitatMech/issues/2229 : Conjunctiva is not an entire visual system; cornea is not an entire eye; cortex is not an entire root; crop is not an entire digestive system, esophagus or foregut; crop contents are not an esophagus. Exclude only exact guarded source-path contributions, retaining independent genera and source observations. This does not settle generic cortex identity or equivalent avian crop sources. Exact target habitatmech:GOLD.5446ce4c6d. Other identity and mapping findings remain separate."]] |
| EDECISION | curation/decisions.tsv; Exact physical TSV rows | supports | [[2, "habitatmech:GOLD.5446ce4c6d\tCONFIRM_UNGROUNDED\t\t\t\tcodex-gpt-5\t2026-10-16\tITEM reassessment https://github.com/CultureBotAI/HabitatMech/issues/2230 : Current UBERON:0007356 has in-taxon Aves scope (https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007356). This source is non-avian; no replacement genus or exact identity was verified. Retain its mint UNGROUNDED, source observations and native units. Whole-organ context is excluded separately. Path: Host-associated &gt; Annelida &gt; Digestive system &gt; Crop\tITEM\t\tparent"]] |

## Limits And Additional Notes

- Original specimen-level evidence and all pair-level citations were not exhaustively reconstructed. Native association counts, taxon ranks and scores do not establish prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs. Exact target TaxIds were separately resolved; frozen taxon labels are not universally current.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. No new causal mechanism is imported.
- UNGROUNDED here means this bounded repair has no verified replacement identity or genus; it is not proof that none exists. BTO:0000301 remains a broader-genus candidate for a separately scoped assessment. The generator boilerplate saying no ontology term fits must be read with this explicit limitation, not as an exhaustive absence claim.
- This successor is a same-agent disposition, not independent human approval. Final-head and merge-queue checks are separate publication gates. Full-corpus scientific review and current kg-microbe export conformance remain incomplete.
- All immutable earlier bundles and session histories remain unchanged. Retain the exact off-main input base with an annotated provenance tag before squash merge and branch deletion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T062916Z-crop__310374d9-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: crop__310374d9'
started_at: '2026-10-16T05:59:21Z'
finished_at: '2026-10-16T06:29:16Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Parent agent integrates evidence and separate-agent source/hierarchy
    cross-checks; not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Removed the guarded GOLD context-parent contribution. The non-avian crop
  source retains its mint UNGROUNDED/REVIEWED without an avian genus or narrow mapping.
  Source observations and independent genera are preserved. No unresolved predecessor
  finding remains in this target scope.
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
  - path: data/habitats/host_associated/crop__310374d9.yaml
    sha256: 0d54e5ec1e59baebfd7c75646c3af05d43f1fb17ec9a8f7a9ae279863bb04566
    role: target
  - path: data/habitats/host_associated/digestive_system__9ec9b5f9.yaml
    sha256: 6bb824d5c563d2698fad2e87bacc9d8cc80064830f821683ba15981c7c939e59
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
  - path: reviews/structured/20261016T054409Z-crop__310374d9-record/review.yaml
    sha256: cd992362cd843f9ddce61395a160bfa9aff6e654239b7929afae36d70c08c405
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
- target_id: habitatmech:GOLD.5446ce4c6d
  path: data/habitats/host_associated/crop__310374d9.yaml
  label: Crop
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
  - habitatmech:GOLD.5446ce4c6d
  exclusions:
  - target: Other corpus records and SSSOM/KGX conformance
    reason: Not whole-corpus scientific approval or shared export-contract certification.
checks:
- check_id: C5
  name: just validate data/habitats/host_associated/crop__310374d9.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/crop__310374d9.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5446ce4c6d
  summary: "Finished 2026-10-16T05:47:43Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/crop__310374d9.yaml"
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
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
  - habitatmech:GOLD.5446ce4c6d
  summary: Verified 2026-10-16T06:28:52Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38858656719
  scope_note: Repaired input/product commit before these new successor outputs; final-head
    and merge-queue checks remain separate.
evidence:
- evidence_id: EX9
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001007/graph
  locator: UBERON_0001007-graph.json
  accessed_at: '2026-10-16T05:16:05Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001007",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001007",
    "target": "http://purl.obolibrary.org/obo/GO_0022600", "uri": "http://purl.obolibrary.org/obo/RO_0002215",
    "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001007",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492",
    "label": "existence ends during"}]'
  snapshot_sha256: 6edb81365904fcd686c6cc14a898a5257038c30b7b71122d5934136a0b138d7b
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001007
  locator: UBERON_0001007.json
  accessed_at: '2026-10-16T05:16:04Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "UBERON:0001007", "label": "digestive system", "is_obsolete": false, "description":
    ["Anatomical system that has as its parts the organs devoted to the ingestion,
    digestion, and assimilation of food and the discharge of residual wastes."], "obo_synonym":
    null}'
  snapshot_sha256: aea4a663a4ca364533042f3049c36d82efbe62f67fc40cb202d7a839dc5d2c09
- evidence_id: EX11
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007356/graph
  locator: UBERON_0007356-graph.json
  accessed_at: '2026-10-16T05:16:20Z'
  support: context_only
  summary: 'Current typed outgoing edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0007356",
    "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007356",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_8782", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0007356",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001043", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 5bcde5a5491036c3f0ebaf2319e0865d1e1fde4cdcf1a0cd35dc47116294a4d1
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007356
  locator: UBERON_0007356.json
  accessed_at: '2026-10-16T05:16:20Z'
  support: context_only
  summary: 'Current identity, definition, active status and typed synonyms: {"obo_id":
    "UBERON:0007356", "label": "crop", "is_obsolete": false, "description": ["A pouched
    enlargement of the gullet of many birds that serves as a receptacle for food and
    for its preliminary maceration."], "obo_synonym": null}'
  snapshot_sha256: 3f1b8fe11c25b51a19f635adfa9ba0fef0bba666b26d77741e40643ebb78192e
- evidence_id: ECANDIDATE
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000301
  locator: BTO:0000301 identity and definition
  accessed_at: '2026-10-16T05:15:25Z'
  support: context_only
  summary: Active crop concept with a definition spanning birds and other animals,
    explicitly including insects. This is a broader-genus candidate, not verified
    exact identity for either taxon-scoped GOLD mint.
  snapshot_sha256: 384787d23df0f1005eb191b2e5fb0e92a44e38640d1d047ea23c85aa75ff2aab
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/crop__310374d9.yaml
  locator: Entire regenerated target YAML
  accessed_at: '2026-10-16T06:29:13Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.5446ce4c6d", "label": "Crop", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:5069",
    "source_label": "Crop", "source_path": "Host-associated > Annelida > Digestive
    system > Crop", "assertion_count": 2, "assertion_unit": "ORGANISM", "notes": "2
    GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-16T00:00:00Z",
    "curator": "codex-gpt-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed
    UNGROUNDED: no ontology term fits this concept. ITEM reassessment https://github.com/CultureBotAI/HabitatMech/issues/2230
    : Current UBERON:0007356 has in-taxon Aves scope (https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007356).
    This source is non-avian; no replacement genus or exact identity was verified.
    Retain its mint UNGROUNDED, source observations and native units. Whole-organ
    context is excluded separately. Path: Host-associated > Annelida > Digestive system
    > Crop (source concept habitatmech:GOLD.5446ce4c6d)"}, {"timestamp": "2026-10-16T00:00:00Z",
    "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded
    GOLD source-path parent contribution habitatmech:GOLD.d011f4b43c for habitatmech:GOLD.5446ce4c6d
    (Host-associated > Annelida > Digestive system > Crop). Review https://github.com/CultureBotAI/HabitatMech/issues/2229
    : Conjunctiva is not an entire visual system; cornea is not an entire eye; cortex
    is not an entire root; crop is not an entire digestive system, esophagus or foregut;
    crop contents are not an esophagus. Exclude only exact guarded source-path contributions,
    retaining independent genera and source observations. This does not settle generic
    cortex identity or equivalent avian crop sources. Exact target habitatmech:GOLD.5446ce4c6d.
    Other identity and mapping findings remain separate."}]}'
  snapshot_sha256: 0d54e5ec1e59baebfd7c75646c3af05d43f1fb17ec9a8f7a9ae279863bb04566
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261016T054409Z-crop__310374d9-record/review.yaml
  locator: Every immutable baseline finding
  accessed_at: '2026-10-16T06:29:13Z'
  support: supports
  summary: Exact predecessor issue keys and findings are reconciled; original inspected
    source scope is preserved.
  snapshot_sha256: cd992362cd843f9ddce61395a160bfa9aff6e654239b7929afae36d70c08c405
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_conjunctiva_crop_review_repairs.py
  locator: Complete full-corpus counterfactual
  accessed_at: '2026-10-16T06:29:13Z'
  support: supports
  summary: Exactly ten records differ. The only scientific changes are guarded context-parent
    removal and two non-avian grounding/predicate/status corrections; source counts,
    taxa and other fields are invariant.
  snapshot_sha256: 182b7c46fdc4564730e0ca1612a776ae724833ec6ef49156077c5d9d0a95d78e
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict hierarchy, ITEM decisions and source units
  accessed_at: '2026-10-16T06:29:13Z'
  support: supports
  summary: Generated artifacts are not edited by hand; native history/status follows
    exact maintained rows.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EH40
  kind: record_content
  reference: history/mappings/conjunctiva_crop_review_nonavian/2026-10-16T054553Z-codex-gpt-5-64c4ba.yaml
  locator: Complete session event
  accessed_at: '2026-10-16T06:29:13Z'
  support: supports
  summary: Authorized curation by codex-gpt-5; exact maintained owner and issue retained.
  snapshot_sha256: c2700ecc67a370a509f8b6aca48dc07c5bfb807c2a5c6b0e05c03dc2dbc76bd1
- evidence_id: EH41
  kind: record_content
  reference: history/mappings/conjunctiva_crop_review_parents/2026-10-16T054552Z-codex-gpt-5-b09465.yaml
  locator: Complete session event
  accessed_at: '2026-10-16T06:29:13Z'
  support: supports
  summary: Authorized curation by codex-gpt-5; exact maintained owner and issue retained.
  snapshot_sha256: abe557d3e71cfb777cf2f135edbf0ae7d17c059f9717e1eed15543f58d579c59
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact physical TSV rows
  accessed_at: '2026-10-16T06:29:14Z'
  support: supports
  summary: '[[7, "habitatmech:GOLD.5446ce4c6d\tHost-associated > Annelida > Digestive
    system > Crop\thabitatmech:GOLD.d011f4b43c\tcodex-gpt-5\t2026-10-16\tReview https://github.com/CultureBotAI/HabitatMech/issues/2229
    : Conjunctiva is not an entire visual system; cornea is not an entire eye; cortex
    is not an entire root; crop is not an entire digestive system, esophagus or foregut;
    crop contents are not an esophagus. Exclude only exact guarded source-path contributions,
    retaining independent genera and source observations. This does not settle generic
    cortex identity or equivalent avian crop sources. Exact target habitatmech:GOLD.5446ce4c6d.
    Other identity and mapping findings remain separate."]]'
  snapshot_sha256: 1f3af4cfd82b31d351ecdce846e5e2d626037d255db63ee869bab5259e12496e
- evidence_id: EDECISION
  kind: record_content
  reference: curation/decisions.tsv
  locator: Exact physical TSV rows
  accessed_at: '2026-10-16T06:29:15Z'
  support: supports
  summary: '[[2, "habitatmech:GOLD.5446ce4c6d\tCONFIRM_UNGROUNDED\t\t\t\tcodex-gpt-5\t2026-10-16\tITEM
    reassessment https://github.com/CultureBotAI/HabitatMech/issues/2230 : Current
    UBERON:0007356 has in-taxon Aves scope (https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0007356).
    This source is non-avian; no replacement genus or exact identity was verified.
    Retain its mint UNGROUNDED, source observations and native units. Whole-organ
    context is excluded separately. Path: Host-associated > Annelida > Digestive system
    > Crop\tITEM\t\tparent"]]'
  snapshot_sha256: c4aeaa9bc04f3704e9e8f69e406990b6d08dd91b1c6afe39aec6a4727ff6612a
assessments:
- assessment_id: A1
  area: consistency
  topic: Bounded correction and exact preservation
  outcome: supported
  summary: Removed the guarded GOLD context-parent contribution. The non-avian crop
    source retains its mint UNGROUNDED/REVIEWED without an avian genus or narrow mapping.
    Source observations and independent genera are preserved. No unresolved predecessor
    finding remains in this target scope.
  target_ids:
  - habitatmech:GOLD.5446ce4c6d
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - ECANDIDATE
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
  - EDECISION
- assessment_id: A2
  area: identity
  topic: Current anatomical identity and hierarchy
  outcome: supported
  summary: 'habitatmech:GOLD.5446ce4c6d: Crop; UNGROUNDED/REVIEWED; parents []. No
    replacement anatomical identity or definition is fabricated. Remaining exact-identity
    findings are not concealed.'
  target_ids:
  - habitatmech:GOLD.5446ce4c6d
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - ECANDIDATE
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
  - EDECISION
- assessment_id: A3
  area: quantity
  topic: Units, counts and observations
  outcome: supported
  summary: '[{"source": "GOLD", "source_id": "gold.ecosystem:5069", "source_label":
    "Crop", "source_path": "Host-associated > Annelida > Digestive system > Crop",
    "assertion_count": 2, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem
    node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}].
    Original source counts/units, taxa, scores and parameters remain unchanged; these
    are not prevalence measurements.'
  target_ids:
  - habitatmech:GOLD.5446ce4c6d
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - ECANDIDATE
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
  - EDECISION
- assessment_id: A4
  area: representation
  topic: Predecessor reconciliation
  outcome: supported
  summary: 'Every previous finding keeps its stable issue key and exact lineage. Removing
    invalid non-avian matches does not solve global mapping contract #1398.'
  target_ids:
  - habitatmech:GOLD.5446ce4c6d
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - ECANDIDATE
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
  - EDECISION
- assessment_id: A5
  area: completeness
  topic: Evidence and lifecycle boundaries
  outcome: supported
  summary: Only the two explicit non-avian ITEM decisions change native status. Optional
    definitions, causal mechanisms and biological absence claims are not invented.
  target_ids:
  - habitatmech:GOLD.5446ce4c6d
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - ECANDIDATE
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
  - EDECISION
findings:
- finding_id: F1
  issue_key: crop--310374d9-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: GOLD context is not a strictly broader habitat class
  description: Removed only the guarded GOLD source-context contribution habitatmech:GOLD.d011f4b43c.
    Independent parents and every source observation are retained.
  target_ids:
  - habitatmech:GOLD.5446ce4c6d
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - ECANDIDATE
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
  - EDECISION
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
    review_id: 20261016T054409Z-crop__310374d9-record
    finding_id: F1
  disposition_reason: Removed only the guarded GOLD source-context contribution habitatmech:GOLD.d011f4b43c.
    Independent parents and every source observation are retained.
- finding_id: F2
  issue_key: crop--310374d9-mapping-endpoint-contract
  category: representation
  severity: major
  status: resolved
  certainty: confirmed
  title: Mapping uses an undeclared ontology-parent endpoint
  description: 'An explicit ITEM decision preserves the non-avian source mint UNGROUNDED
    without the avian genus or narrow mapping. This resolves only the scoped witness;
    global #1398 is not fixed.'
  target_ids:
  - habitatmech:GOLD.5446ce4c6d
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - ECANDIDATE
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
  - EDECISION
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  - https://github.com/CultureBotAI/HabitatMech/issues/2230
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T054409Z-crop__310374d9-record
    finding_id: F2
  disposition_reason: 'An explicit ITEM decision preserves the non-avian source mint
    UNGROUNDED without the avian genus or narrow mapping. This resolves only the scoped
    witness; global #1398 is not fixed.'
- finding_id: F3
  issue_key: crop--310374d9-avian-genus
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Avian crop is not a supported non-avian genus
  description: 'An explicit ITEM decision preserves the non-avian source mint UNGROUNDED
    without the avian genus or narrow mapping. This resolves only the scoped witness;
    global #1398 is not fixed.'
  target_ids:
  - habitatmech:GOLD.5446ce4c6d
  field_paths:
  - parent_habitats
  - grounding_status
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - ECANDIDATE
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EPARENTS
  - EDECISION
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2230
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T054409Z-crop__310374d9-record
    finding_id: F3
  disposition_reason: 'An explicit ITEM decision preserves the non-avian source mint
    UNGROUNDED without the avian genus or narrow mapping. This resolves only the scoped
    witness; global #1398 is not fixed.'
actions: []
limitations:
- Original specimen-level evidence and all pair-level citations were not exhaustively
  reconstructed. Native association counts, taxon ranks and scores do not establish
  prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs. Exact target TaxIds were
  separately resolved; frozen taxon labels are not universally current.
- 'iModulonDB is not applicable: no gene, regulator or expression-module claim is
  asserted. No new causal mechanism is imported.'
- UNGROUNDED here means this bounded repair has no verified replacement identity or
  genus; it is not proof that none exists. BTO:0000301 remains a broader-genus candidate
  for a separately scoped assessment. The generator boilerplate saying no ontology
  term fits must be read with this explicit limitation, not as an exhaustive absence
  claim.
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
  review_id: 20261016T054409Z-crop__310374d9-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
