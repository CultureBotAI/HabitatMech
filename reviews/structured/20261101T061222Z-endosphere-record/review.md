# Record review: endosphere environment (habitatmech:BACDIVE.3e4680f074)

- Review: 20261101T061222Z-endosphere-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-01T06:05:00Z
- Finished UTC: 2026-11-01T06:12:22Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The minted BacDive record habitatmech:BACDIVE.3e4680f074 (endosphere environment, BacDive: Endosphere, UNGROUNDED/REVIEWED, 2 STRAIN assertions, 2 characteristic taxa) is coherently defined under ENVO:01001001 (plant-associated environment) with exact synonyms 'endosphere' and 'plant endosphere environment'.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/endosphere.yaml) at captured main revision ad20de05c38d4fadf667b5c579eef50496b31b02.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (empyema_drain through epibionts); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base ad20de05c38d4fadf667b5c579eef50496b31b02.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.3e4680f074 | data/habitats/host_associated/endosphere.yaml | generated | endosphere environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:BACDIVE.3e4680f074 | Completed 2026-11-01T06:08:08Z. No issues found. |
| validate-strict | passed | True | habitatmech:BACDIVE.3e4680f074 | Completed 2026-11-01T06:08:14Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:BACDIVE.3e4680f074 | Completed 2026-11-01T06:08:25Z. No issues found; 858 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:BACDIVE.3e4680f074 | Completed 2026-11-01T06:08:25Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:BACDIVE.3e4680f074 | Completed 2026-11-01T06:08:41Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:BACDIVE.3e4680f074 | Completed 2026-11-01T06:08:45Z. validated 63 causal-graph curation file(s) with 63 graph(s). |
| term-requests-check | passed | True | habitatmech:BACDIVE.3e4680f074 | Completed 2026-11-01T06:09:00Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:BACDIVE.3e4680f074 | Completed 2026-11-01T06:11:06Z. OK_CANONICAL: 1196, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2071. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:BACDIVE.3e4680f074.

Individual schema, strict 24-target validation, 858 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 63 causal overlays, and 671 term requests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:BACDIVE.3e4680f074.

The record defines the BacDive 'Endosphere' isolation category as an internal plant tissue environment under ENVO:01001001 (plant-associated environment) and retains the 2 upstream strain-backed characteristic taxa (Sphingobacterium haloxyli and Methylobacterium goesingense).

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:BACDIVE.3e4680f074.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "BACDIVE", "count": 2, "unit": "STRAIN"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:BACDIVE.3e4680f074.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/endosphere.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:BACDIVE.3e4680f074 (endosphere environment) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:BACDIVE.3e4680f074, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001001"]. |
| EBACDIVE | data/raw/bacdive_isolation_sources.tsv; TSV rows 155 | supports | [{"data": {"bacdive_id": "bacdive.isolation_source:endosphere", "label": "Endosphere", "source_slug": "endosphere", "strain_count": "2", "taxon_count": "2"}, "row": 155}] |
| EGROUND | data/raw/isolation_source_groundings.tsv; TSV rows 100 | supports | [{"data": {"confidence": "", "curator": "codex_review_fix", "mapping_justification": "", "object_id": "", "object_label": "", "object_source": "", "predicate_id": "", "source_dataset": "bacdive", "subject_label": "Endosphere", "subject_label_normalized": "endosphere", "verified_date": "2026-05-02"}, "row": 100}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 8490 | supports | [{"data": {"definition": "An environmental system determined by a green plant.", "deprecated": "", "directly_referenced": "TRUE", "label": "plant-associated environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "Viridiplantae-associated environment&#124;plant environment", "term_id": "ENVO:01001001"}, "row": 8490}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 6796 | supports | [{"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001001"}, "row": 6796}] |
| EDEC | curation/decisions.tsv; TSV rows 43 | supports | [{"data": {"category": "HOST_ASSOCIATED", "curator": "antigravity", "date": "2026-10-17", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:BACDIVE.3e4680f074", "notes": "ITEM curation: BacDive 'Endosphere' denotes the internal tissue habitat of plants colonized by endophytes. Define under ENVO:01001001 (plant-associated environment) (PMID 26213366; DOI:10.1016/j.tim.2015.07.004). Path: Endosphere", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 43}] |
| ETR | curation/term_requests.tsv; TSV rows 212 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "definition": "A plant-associated environment comprising the internal tissues, apoplastic spaces, and vascular elements within a plant body colonized by endophytic microorganisms.", "exact_synonym": "Endosphere", "identifier": "habitatmech:BACDIVE.3e4680f074", "notes": "ITEM curation: BacDive 'Endosphere' denotes the internal tissue habitat of plants colonized by endophytes. Define under ENVO:01001001 (plant-associated environment) (PMID 26213366; DOI:10.1016/j.tim.2015.07.004). Path: Endosphere", "parent_class": "ENVO:01001001", "parent_label": "plant-associated environment", "parent_mode": "ADD", "requested_label": "endosphere environment"}, "row": 212}] |
| EP1 | data/habitats/host_associated/plant_associated_environment.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by a green plant.", "grounding_status": "EXACT", "identifier": "ENVO:01001001", "label": "plant-associated environment", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"assertion_count": 2451, "assertion_unit": "STRAIN", "mapping_predicate": "skos:broadMatch", "notes": "kg-microbe's isolation-source mapping table has no ontology target for this source; the automatic route leaves it ungrounded. The explicit curator decision GROUND overrides that route; this source is emitted on ENVO:01001001.", "source": "BACDIVE", "source_id": "bacdive.isolation_source:herbaceous-plants-grass,crops", "source_label": "Herbaceous-plants-Grass,Crops"}, {"notes": "Physicochemical parameter bands from kg-microbe's environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "host_plant", "source_label": "host_plant"}, {"assertion_count": 12638, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3385", "source_label": "Plants", "source_path": "Host-associated &gt; Plants"}, {"assertion_count": 1206, "assertion_unit": "TAXON", "source": "MADIN", "source_id": "ENVO:01001001", "source_label": "plant-associated environment"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'endosphere&#124;habitatmech:BACDIVE.3e4680f074' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,071 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- All included input bytes match both the clean working tree and exact captured Git revision ad20de05c38d4fadf667b5c579eef50496b31b02.
- Structured archive traversal found no earlier structured review targeting this record. No existing bundle is superseded or closed.
- This read-only Stage-4 review proposes maintained-owner actions and preserves open findings for Stage 5 grouped remediation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T061222Z-endosphere-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: endosphere environment (habitatmech:BACDIVE.3e4680f074)'
started_at: '2026-11-01T06:05:00Z'
finished_at: '2026-11-01T06:12:22Z'
reviewer:
  identity: antigravity
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Same agent inspected the full target and source evidence; not
    independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'The minted BacDive record habitatmech:BACDIVE.3e4680f074 (endosphere environment,
  BacDive: Endosphere, UNGROUNDED/REVIEWED, 2 STRAIN assertions, 2 characteristic
  taxa) is coherently defined under ENVO:01001001 (plant-associated environment) with
  exact synonyms ''endosphere'' and ''plant endosphere environment''.'
source:
  git_revision: ad20de05c38d4fadf667b5c579eef50496b31b02
  state: git_commit
  inputs:
  - path: curation/decisions.tsv
    sha256: 663c2f4bb14541f465da997ea049f6a1b0d7845dd92b00c70a7a9c4acc6c2dbe
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: da9135a0fd5516dc2b47679731f64b8093806105bbaddcc2e3f4d5d7c49ce07f
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 12380d3ee22e773ff067d372204f74165cf5cfa77973ad9565162bbcd383a797
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: fdae9bb4dd49d8cdfbaca6ee898d9b7890dd1815d2b03145d1c0c58d12c12806
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/endosphere.yaml
    sha256: 9cc37e05aa4930c303e68e63698c17bd61646ae4693c5b42b6c183ebd6518d08
    role: target
  - path: data/habitats/host_associated/plant_associated_environment.yaml
    sha256: d2867ecbf58347f0022219d127df9153e4fbb933b532eeb76779998ee6ef6126
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/isolation_source_groundings.tsv
    sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
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
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: habitatmech:BACDIVE.3e4680f074
  path: data/habitats/host_associated/endosphere.yaml
  label: endosphere environment
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
    path: curation/term_requests_excluded.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
scope:
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/endosphere.yaml)
    at captured main revision ad20de05c38d4fadf667b5c579eef50496b31b02.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (empyema_drain through epibionts); this bundle assesses its single
    resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:BACDIVE.3e4680f074
  exclusions:
  - target: Other habitat records and SSSOM/KGX products
    reason: Direct parents and siblings inform hierarchy/synonym interpretation but
      are not additional completed reviews; exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: .venv/bin/python -m linkml.validator.cli -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/endosphere.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  summary: Completed 2026-11-01T06:08:08Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/empyema_drain.yaml
    data/habitats/host_associated/endocrine_gland.yaml data/habitats/host_associated/endocrine_gland__8c35903c.yaml
    data/habitats/host_associated/endocrine_system.yaml data/habitats/host_associated/endocrine_system__a22b6ca6.yaml
    data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml data/habitats/host_associated/endocrine_system__fc8977b8.yaml
    data/habitats/host_associated/endometrial_uterine.yaml data/habitats/host_associated/endometrium.yaml
    data/habitats/host_associated/endophytes.yaml data/habitats/host_associated/endophytes__ca9aaedf.yaml
    data/habitats/host_associated/endophytes__fae60ba7.yaml data/habitats/host_associated/endosphere.yaml
    data/habitats/host_associated/endosphere__005f8afe.yaml data/habitats/host_associated/endosphere__eb0d56da.yaml
    data/habitats/host_associated/endosphere__fd8c8a61.yaml data/habitats/host_associated/endosymbionts.yaml
    data/habitats/host_associated/endosymbionts__38198b44.yaml data/habitats/host_associated/endothelial_cell.yaml
    data/habitats/host_associated/endothelial_progenitor_cell.yaml data/habitats/host_associated/enterocyte.yaml
    data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    data/habitats/host_associated/eosinophil.yaml data/habitats/host_associated/epibionts.yaml
    --out /tmp/c4s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  summary: 'Completed 2026-11-01T06:08:14Z. Validated 24 files; files with ERROR:
    0; total ERROR rows: 0.'
  scope_note: Closed-schema strict validation across all 24 cohort target files (and
    3,209 full-corpus files).
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_history.py history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  summary: Completed 2026-11-01T06:08:25Z. No issues found; 858 history record(s)
    valid against src/habitatmech/schema/history.yaml.
  scope_note: Full-corpus curation history validation.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: .venv/bin/python scripts/check_provenance.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  summary: 'Completed 2026-11-01T06:08:25Z. provenance current: 14 committed inventories,
    2 GOLD sources.'
  scope_note: Full-corpus raw inventory provenance verification.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  summary: 'Completed 2026-11-01T06:08:41Z. expected 3209 records, found 3209 on disk;
    missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/.'
  scope_note: Full-corpus deterministic reproduction from raw inventories and curation
    tables.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_causal_graph_curations.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  summary: Completed 2026-11-01T06:08:45Z. validated 63 causal-graph curation file(s)
    with 63 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  summary: Completed 2026-11-01T06:09:00Z. term-request table is current (671 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  summary: 'Completed 2026-11-01T06:11:06Z. OK_CANONICAL: 1196, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2071. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/endosphere.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:BACDIVE.3e4680f074 (endosphere environment)
    were read.
  snapshot_sha256: 9cc37e05aa4930c303e68e63698c17bd61646ae4693c5b42b6c183ebd6518d08
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:BACDIVE.3e4680f074, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001001"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EBACDIVE
  kind: database
  reference: data/raw/bacdive_isolation_sources.tsv
  locator: TSV rows 155
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: '[{"data": {"bacdive_id": "bacdive.isolation_source:endosphere", "label":
    "Endosphere", "source_slug": "endosphere", "strain_count": "2", "taxon_count":
    "2"}, "row": 155}]'
  snapshot_sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
- evidence_id: EGROUND
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: TSV rows 100
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: '[{"data": {"confidence": "", "curator": "codex_review_fix", "mapping_justification":
    "", "object_id": "", "object_label": "", "object_source": "", "predicate_id":
    "", "source_dataset": "bacdive", "subject_label": "Endosphere", "subject_label_normalized":
    "endosphere", "verified_date": "2026-05-02"}, "row": 100}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 8490
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: '[{"data": {"definition": "An environmental system determined by a green
    plant.", "deprecated": "", "directly_referenced": "TRUE", "label": "plant-associated
    environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "Viridiplantae-associated
    environment|plant environment", "term_id": "ENVO:01001001"}, "row": 8490}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 6796
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: '[{"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001001"}, "row": 6796}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 43
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: '[{"data": {"category": "HOST_ASSOCIATED", "curator": "antigravity", "date":
    "2026-10-17", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier":
    "habitatmech:BACDIVE.3e4680f074", "notes": "ITEM curation: BacDive ''Endosphere''
    denotes the internal tissue habitat of plants colonized by endophytes. Define
    under ENVO:01001001 (plant-associated environment) (PMID 26213366; DOI:10.1016/j.tim.2015.07.004).
    Path: Endosphere", "object_id": "", "object_label": "", "relation": "", "review_depth":
    "ITEM"}, "row": 43}]'
  snapshot_sha256: 663c2f4bb14541f465da997ea049f6a1b0d7845dd92b00c70a7a9c4acc6c2dbe
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV rows 212
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "definition":
    "A plant-associated environment comprising the internal tissues, apoplastic spaces,
    and vascular elements within a plant body colonized by endophytic microorganisms.",
    "exact_synonym": "Endosphere", "identifier": "habitatmech:BACDIVE.3e4680f074",
    "notes": "ITEM curation: BacDive ''Endosphere'' denotes the internal tissue habitat
    of plants colonized by endophytes. Define under ENVO:01001001 (plant-associated
    environment) (PMID 26213366; DOI:10.1016/j.tim.2015.07.004). Path: Endosphere",
    "parent_class": "ENVO:01001001", "parent_label": "plant-associated environment",
    "parent_mode": "ADD", "requested_label": "endosphere environment"}, "row": 212}]'
  snapshot_sha256: fdae9bb4dd49d8cdfbaca6ee898d9b7890dd1815d2b03145d1c0c58d12c12806
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/plant_associated_environment.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-01T06:12:22Z'
  support: supports
  summary: '{"definition": "An environmental system determined by a green plant.",
    "grounding_status": "EXACT", "identifier": "ENVO:01001001", "label": "plant-associated
    environment", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001000"],
    "source_attestations": [{"assertion_count": 2451, "assertion_unit": "STRAIN",
    "mapping_predicate": "skos:broadMatch", "notes": "kg-microbe''s isolation-source
    mapping table has no ontology target for this source; the automatic route leaves
    it ungrounded. The explicit curator decision GROUND overrides that route; this
    source is emitted on ENVO:01001001.", "source": "BACDIVE", "source_id": "bacdive.isolation_source:herbaceous-plants-grass,crops",
    "source_label": "Herbaceous-plants-Grass,Crops"}, {"notes": "Physicochemical parameter
    bands from kg-microbe''s environment table.", "source": "ENVIRONMENTS_TABLE",
    "source_id": "host_plant", "source_label": "host_plant"}, {"assertion_count":
    12638, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "notes":
    "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3385", "source_label": "Plants",
    "source_path": "Host-associated > Plants"}, {"assertion_count": 1206, "assertion_unit":
    "TAXON", "source": "MADIN", "source_id": "ENVO:01001001", "source_label": "plant-associated
    environment"}]}'
  snapshot_sha256: d2867ecbf58347f0022219d127df9153e4fbb933b532eeb76779998ee6ef6126
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'endosphere|habitatmech:BACDIVE.3e4680f074' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-01T06:12:22Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit ad20de05c38d4fadf667b5c579eef50496b31b02.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, strict 24-target validation, 858 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 63 causal
    overlays, and 671 term requests passed.
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: The record defines the BacDive 'Endosphere' isolation category as an internal
    plant tissue environment under ENVO:01001001 (plant-associated environment) and
    retains the 2 upstream strain-backed characteristic taxa (Sphingobacterium haloxyli
    and Methylobacterium goesingense).
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EBACDIVE
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "BACDIVE", "count": 2, "unit": "STRAIN"}]. Zero counts
    are omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EBACDIVE
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:BACDIVE.3e4680f074
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings: []
actions: []
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,071 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- All included input bytes match both the clean working tree and exact captured Git
  revision ad20de05c38d4fadf667b5c579eef50496b31b02.
- Structured archive traversal found no earlier structured review targeting this record.
  No existing bundle is superseded or closed.
- This read-only Stage-4 review proposes maintained-owner actions and preserves open
  findings for Stage 5 grouped remediation.
tags:
- individual-scientific-review
- host-associated
```
