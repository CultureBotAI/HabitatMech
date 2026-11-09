# Record review: fish-associated environment (habitatmech:GOLD.3d529a667e)

- Review: 20261109T181011Z-fish-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-09T18:08:00Z
- Finished UTC: 2026-11-09T18:10:11Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The curated GOLD host-environment record habitatmech:GOLD.3d529a667e (fish-associated environment, UNGROUNDED/REVIEWED, 1,350 ORGANISM assertions) has a sound definition and parent_habitats (ENVO:01001000, ENVO:01001002), but curation/term_requests.tsv row 9 retains the bare host clade name 'Fish' in exact_synonym, emitting 'Fish' as an EXACT_SYNONYM on the environment record.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/fish.yaml) at captured main revision 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (finger through free_living_state); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.3d529a667e | data/habitats/host_associated/fish.yaml | generated | fish-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.3d529a667e | Completed 2026-11-09T18:08:48Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.3d529a667e | Completed 2026-11-09T18:08:54Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.3d529a667e | Completed 2026-11-09T18:09:00Z. No issues found; 876 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.3d529a667e | Completed 2026-11-09T18:09:01Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.3d529a667e | Completed 2026-11-09T18:09:16Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.3d529a667e | Completed 2026-11-09T18:09:22Z. validated 103 causal-graph curation file(s) with 103 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.3d529a667e | Completed 2026-11-09T18:09:36Z. term-request table is current (674 terms). |
| validate-products | passed | True | habitatmech:GOLD.3d529a667e | Completed 2026-11-09T18:10:17Z. OK_CANONICAL: 1213, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2094. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.3d529a667e.

Individual schema, strict 24-target validation, 876 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal overlays, and 674 term requests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.3d529a667e.

The curated GOLD host-environment record habitatmech:GOLD.3d529a667e (fish-associated environment, UNGROUNDED/REVIEWED, 1,350 ORGANISM assertions) has a sound definition and parent_habitats (ENVO:01001000, ENVO:01001002), but curation/term_requests.tsv row 9 retains the bare host clade name 'Fish' in exact_synonym, emitting 'Fish' as an EXACT_SYNONYM on the environment record.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.3d529a667e.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 1350, "source": "GOLD", "unit": "ORGANISM"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.3d529a667e.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Bare host clade name 'Fish' is asserted as an exact synonym of fish-associated environment

major / open / confirmed; issue key: fish-host-name-exact-synonym.

Remove bare host clade label 'Fish' from exact_synonym in curation/term_requests.tsv row 9 for habitatmech:GOLD.3d529a667e (retaining 'fish host environment') and add a guarded row in curation/definition_source_label_exclusions.tsv so the displaced GOLD source label 'Fish' is not retained as an EXACT_SYNONYM on fish-associated environment.

## Recommended Actions And Acceptance Checks

### ACT1

Remove bare host clade label 'Fish' from exact_synonym in curation/term_requests.tsv row 9 for habitatmech:GOLD.3d529a667e (retaining 'fish host environment') and add a guarded row in curation/definition_source_label_exclusions.tsv so the displaced GOLD source label 'Fish' is not retained as an EXACT_SYNONYM on fish-associated environment.

- Verify exact_synonyms on data/habitats/host_associated/fish.yaml retains only 'fish host environment' and omits bare 'Fish'.
- Run just qc and just validate-products.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/fish.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.3d529a667e (fish-associated environment) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and subcellular organelle terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.3d529a667e, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001000", "ENVO:01001002"]. |
| ESIB1 | data/habitats/host_associated/birds.yaml; Entire YAML | supports | Sibling vertebrate host-environment record habitatmech:GOLD.0628ec0ca9 (bird-associated environment) where bare host clade name 'Birds' was excluded from exact_synonyms (#2183). |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 33 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Fish", "depth": "2", "ecosystem": "Host-associated", "ecosystem_category": "Fish", "ecosystem_subtype": "", "ecosystem_type": "", "gold_node_count": "4", "gold_node_ids": "gold.ecosystem:3375&#124;gold.ecosystem:3569&#124;gold.ecosystem:3651&#124;gold.ecosystem:4095", "leaf_label": "Fish", "organism_count": "1350", "specific_ecosystem": "", "study_count": "0", "total_assertions": "1350"}, "row": 33}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 8489,8491 | supports | [{"data": {"definition": "An environmental system which is determined by a living organism.", "deprecated": "", "directly_referenced": "FALSE", "label": "environmental system determined by an organism", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "host-associated environment", "term_id": "ENVO:01001000"}, "row": 8489}, {"data": {"definition": "An environmental system determined by an animal.", "deprecated": "", "directly_referenced": "TRUE", "label": "animal-associated environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "Metazoan-associated environment&#124;animal environment", "term_id": "ENVO:01001002"}, "row": 8491}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 6795,6796,6797,6840,6992,6996,7704 | supports | [{"data": {"object": "ENVO:01000254", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001000"}, "row": 6795}, {"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001001"}, "row": 6796}, {"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001002"}, "row": 6797}, {"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001041"}, "row": 6840}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001176"}, "row": 6992}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001179"}, "row": 6996}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001829"}, "row": 7704}] |
| EDEC | curation/decisions.tsv; TSV rows 449 | supports | [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.3d529a667e", "notes": "Fish as host. Parented to animal-associated environment; not grounded there because every host clade would merge onto one record. ENVO term request.", "object_id": "ENVO:01001002", "object_label": "animal-associated environment", "relation": "", "review_depth": "ITEM"}, "row": 449}] |
| ETREQ | curation/term_requests.tsv; TSV rows 9 | supports | [{"data": {"curator": "claude-opus-5", "date": "2026-08-16", "definition": "An environmental system determined by a fish.", "exact_synonym": "Fish", "identifier": "habitatmech:GOLD.3d529a667e", "notes": "The habitat is the host clade, and it is the entire content of the concept: GOLD and BacDive both organise host-associated isolates by host, and every downstream anatomical path hangs off it. HabitatMech deliberately does not ground these to animal-associated environment, because every clade would then merge onto one record and the distinction the sources are making would be lost. ENVO already has this shape at plant-, animal- and fungi-associated environment; this asks for the same pattern one level down. ", "parent_class": "ENVO:01001002", "parent_label": "animal-associated environment", "parent_mode": "ADD", "requested_label": "fish-associated environment"}, "row": 9}] |
| EP1 | data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system which is determined by a living organism.", "grounding_status": "EXACT", "identifier": "ENVO:01001000", "label": "environmental system determined by an organism", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01000254"], "source_attestations": [{"assertion_count": 25581, "assertion_unit": "STRAIN", "mapping_predicate": "skos:exactMatch", "notes": "kg-microbe's isolation-source mapping table has no ontology target for this source; the automatic route leaves it ungrounded. The explicit curator decision GROUND overrides that route; this source is emitted on ENVO:01001000.", "source": "BACDIVE", "source_id": "bacdive.isolation_source:host", "source_label": "Host"}, {"assertion_count": 3307, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "notes": "5 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3373", "source_label": "Host-associated", "source_path": "Host-associated"}]} |
| EP2 | data/habitats/other/animal_associated_environment.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by an animal.", "grounding_status": "EXACT", "identifier": "ENVO:01001002", "label": "animal-associated environment", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"notes": "Physicochemical parameter bands from kg-microbe's environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal"}, {"assertion_count": 144, "assertion_unit": "TAXON", "source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated environment"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'fish&#124;habitatmech:GOLD.3d529a667e' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

## Limits And Additional Notes

- Only the cited repository inputs, ontology terms, and source inventories were inspected; original specimen-level support for every upstream source assertion was not exhaustively reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus identifier certification.
- Read-only review: no curation table, generated habitat YAML, status, or history record was modified.
- All target and context inputs were captured at clean git commit 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
- Structured-review archive traversal confirmed no prior target review bundle exists for this record.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T181011Z-fish-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: fish-associated environment (habitatmech:GOLD.3d529a667e)'
started_at: '2026-11-09T18:08:00Z'
finished_at: '2026-11-09T18:10:11Z'
reviewer:
  identity: antigravity
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Same agent inspected the full target and source evidence; not
    independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The curated GOLD host-environment record habitatmech:GOLD.3d529a667e (fish-associated
  environment, UNGROUNDED/REVIEWED, 1,350 ORGANISM assertions) has a sound definition
  and parent_habitats (ENVO:01001000, ENVO:01001002), but curation/term_requests.tsv
  row 9 retains the bare host clade name 'Fish' in exact_synonym, emitting 'Fish'
  as an EXACT_SYNONYM on the environment record.
source:
  git_revision: 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39
  state: git_commit
  inputs:
  - path: curation/decisions.tsv
    sha256: d3bf0a3ca3570e8f318898db92f800a1e13220f64112fe5c1ce1edc9181c3ae2
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: f53415b9d57f351620a1722c7c83414983899dd9a4559d42e9a094a3e8f501e8
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: f004c15e7d206d673bdd9e6d051f6fce93c8a06ebe4db6026149d4d00c49cc9e
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: ad853d6290dd72b2451d945a0545a5dc5272cc37c2296eaab78c99d2872d4b0c
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/host_associated/birds.yaml
    sha256: 2de4c694d7ca103897d519fd7fbef6d955a9c2502f6045aa8c56d4af09204aae
    role: context
  - path: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
    role: context
  - path: data/habitats/host_associated/fish.yaml
    sha256: 511e15b9761796b18df95ffb1befb025a6e4e8f6c68a8b85fb5ffa2710cd0308
    role: target
  - path: data/habitats/other/animal_associated_environment.yaml
    sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: habitatmech:GOLD.3d529a667e
  path: data/habitats/host_associated/fish.yaml
  label: fish-associated environment
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
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
scope:
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/fish.yaml)
    at captured main revision 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (finger through free_living_state); this bundle assesses its single
    resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.3d529a667e
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
    --target-class HabitatRecord data/habitats/host_associated/fish.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3d529a667e
  summary: Completed 2026-11-09T18:08:48Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/finger.yaml
    data/habitats/host_associated/fish.yaml data/habitats/host_associated/flagellate.yaml
    data/habitats/host_associated/flagellum.yaml data/habitats/host_associated/flat_warts.yaml
    data/habitats/host_associated/flower.yaml data/habitats/host_associated/foot.yaml
    data/habitats/host_associated/foraminifera.yaml data/habitats/host_associated/forearm.yaml
    data/habitats/host_associated/foregut.yaml data/habitats/host_associated/foregut__6bc8c43a.yaml
    data/habitats/host_associated/foregut__c14450a8.yaml data/habitats/host_associated/foregut__ce63e8ab.yaml
    data/habitats/host_associated/foregut__d14a54ae.yaml data/habitats/host_associated/foregut__ee6a8f74.yaml
    data/habitats/host_associated/foreleg.yaml data/habitats/host_associated/forestomach.yaml
    data/habitats/host_associated/fossilized_remains.yaml data/habitats/host_associated/fossilized_remains__19772eb4.yaml
    data/habitats/host_associated/fossilized_remains__8b01c49f.yaml data/habitats/host_associated/fossilized_remains__eec3c6e8.yaml
    data/habitats/host_associated/frass.yaml data/habitats/host_associated/frass__c029dd2b.yaml
    data/habitats/host_associated/free_living_state.yaml --out .temp/c8s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3d529a667e
  summary: 'Completed 2026-11-09T18:08:54Z. Validated 24 files; files with ERROR:
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
  - habitatmech:GOLD.3d529a667e
  summary: Completed 2026-11-09T18:09:00Z. No issues found; 876 history record(s)
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
  - habitatmech:GOLD.3d529a667e
  summary: 'Completed 2026-11-09T18:09:01Z. provenance current: 14 committed inventories,
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
  - habitatmech:GOLD.3d529a667e
  summary: 'Completed 2026-11-09T18:09:16Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:GOLD.3d529a667e
  summary: Completed 2026-11-09T18:09:22Z. validated 103 causal-graph curation file(s)
    with 103 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3d529a667e
  summary: Completed 2026-11-09T18:09:36Z. term-request table is current (674 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.3d529a667e
  summary: 'Completed 2026-11-09T18:10:17Z. OK_CANONICAL: 1213, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2094. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/fish.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.3d529a667e (fish-associated environment)
    were read.
  snapshot_sha256: 511e15b9761796b18df95ffb1befb025a6e4e8f6c68a8b85fb5ffa2710cd0308
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and subcellular organelle terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.3d529a667e, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001000", "ENVO:01001002"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/birds.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: Sibling vertebrate host-environment record habitatmech:GOLD.0628ec0ca9
    (bird-associated environment) where bare host clade name 'Birds' was excluded
    from exact_synonyms (#2183).
  snapshot_sha256: 2de4c694d7ca103897d519fd7fbef6d955a9c2502f6045aa8c56d4af09204aae
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 33
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Fish", "depth": "2", "ecosystem": "Host-associated", "ecosystem_category": "Fish",
    "ecosystem_subtype": "", "ecosystem_type": "", "gold_node_count": "4", "gold_node_ids":
    "gold.ecosystem:3375|gold.ecosystem:3569|gold.ecosystem:3651|gold.ecosystem:4095",
    "leaf_label": "Fish", "organism_count": "1350", "specific_ecosystem": "", "study_count":
    "0", "total_assertions": "1350"}, "row": 33}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 8489,8491
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: '[{"data": {"definition": "An environmental system which is determined
    by a living organism.", "deprecated": "", "directly_referenced": "FALSE", "label":
    "environmental system determined by an organism", "label_only": "FALSE", "ontology":
    "ENVO", "synonyms": "host-associated environment", "term_id": "ENVO:01001000"},
    "row": 8489}, {"data": {"definition": "An environmental system determined by an
    animal.", "deprecated": "", "directly_referenced": "TRUE", "label": "animal-associated
    environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "Metazoan-associated
    environment|animal environment", "term_id": "ENVO:01001002"}, "row": 8491}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 6795,6796,6797,6840,6992,6996,7704
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: '[{"data": {"object": "ENVO:01000254", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001000"}, "row": 6795}, {"data": {"object": "ENVO:01001000",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:01001001"}, "row": 6796}, {"data":
    {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001002"},
    "row": 6797}, {"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001041"}, "row": 6840}, {"data": {"object": "ENVO:01001002",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:01001176"}, "row": 6992}, {"data":
    {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001179"},
    "row": 6996}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001829"}, "row": 7704}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 449
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12",
    "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.3d529a667e",
    "notes": "Fish as host. Parented to animal-associated environment; not grounded
    there because every host clade would merge onto one record. ENVO term request.",
    "object_id": "ENVO:01001002", "object_label": "animal-associated environment",
    "relation": "", "review_depth": "ITEM"}, "row": 449}]'
  snapshot_sha256: d3bf0a3ca3570e8f318898db92f800a1e13220f64112fe5c1ce1edc9181c3ae2
- evidence_id: ETREQ
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV rows 9
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: '[{"data": {"curator": "claude-opus-5", "date": "2026-08-16", "definition":
    "An environmental system determined by a fish.", "exact_synonym": "Fish", "identifier":
    "habitatmech:GOLD.3d529a667e", "notes": "The habitat is the host clade, and it
    is the entire content of the concept: GOLD and BacDive both organise host-associated
    isolates by host, and every downstream anatomical path hangs off it. HabitatMech
    deliberately does not ground these to animal-associated environment, because every
    clade would then merge onto one record and the distinction the sources are making
    would be lost. ENVO already has this shape at plant-, animal- and fungi-associated
    environment; this asks for the same pattern one level down. ", "parent_class":
    "ENVO:01001002", "parent_label": "animal-associated environment", "parent_mode":
    "ADD", "requested_label": "fish-associated environment"}, "row": 9}]'
  snapshot_sha256: ad853d6290dd72b2451d945a0545a5dc5272cc37c2296eaab78c99d2872d4b0c
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: '{"definition": "An environmental system which is determined by a living
    organism.", "grounding_status": "EXACT", "identifier": "ENVO:01001000", "label":
    "environmental system determined by an organism", "mapping_status": "REVIEWED",
    "parent_habitats": ["ENVO:01000254"], "source_attestations": [{"assertion_count":
    25581, "assertion_unit": "STRAIN", "mapping_predicate": "skos:exactMatch", "notes":
    "kg-microbe''s isolation-source mapping table has no ontology target for this
    source; the automatic route leaves it ungrounded. The explicit curator decision
    GROUND overrides that route; this source is emitted on ENVO:01001000.", "source":
    "BACDIVE", "source_id": "bacdive.isolation_source:host", "source_label": "Host"},
    {"assertion_count": 3307, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch",
    "notes": "5 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3373", "source_label": "Host-associated",
    "source_path": "Host-associated"}]}'
  snapshot_sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/other/animal_associated_environment.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-09T18:10:11Z'
  support: supports
  summary: '{"definition": "An environmental system determined by an animal.", "grounding_status":
    "EXACT", "identifier": "ENVO:01001002", "label": "animal-associated environment",
    "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001000"], "source_attestations":
    [{"notes": "Physicochemical parameter bands from kg-microbe''s environment table.",
    "source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal"},
    {"assertion_count": 144, "assertion_unit": "TAXON", "source": "MADIN", "source_id":
    "ENVO:01001002", "source_label": "animal-associated environment"}]}'
  snapshot_sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'fish|habitatmech:GOLD.3d529a667e' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-09T18:10:11Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, strict 24-target validation, 876 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal
    overlays, and 674 term requests passed.
  target_ids:
  - habitatmech:GOLD.3d529a667e
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: The curated GOLD host-environment record habitatmech:GOLD.3d529a667e (fish-associated
    environment, UNGROUNDED/REVIEWED, 1,350 ORGANISM assertions) has a sound definition
    and parent_habitats (ENVO:01001000, ENVO:01001002), but curation/term_requests.tsv
    row 9 retains the bare host clade name 'Fish' in exact_synonym, emitting 'Fish'
    as an EXACT_SYNONYM on the environment record.
  target_ids:
  - habitatmech:GOLD.3d529a667e
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETREQ
  - EP1
  - EP2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"count": 1350, "source": "GOLD", "unit": "ORGANISM"}]. Zero counts
    are omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.3d529a667e
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETREQ
  - EP1
  - EP2
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.3d529a667e
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: fish-host-name-exact-synonym
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: Bare host clade name 'Fish' is asserted as an exact synonym of fish-associated
    environment
  description: Remove bare host clade label 'Fish' from exact_synonym in curation/term_requests.tsv
    row 9 for habitatmech:GOLD.3d529a667e (retaining 'fish host environment') and
    add a guarded row in curation/definition_source_label_exclusions.tsv so the displaced
    GOLD source label 'Fish' is not retained as an EXACT_SYNONYM on fish-associated
    environment.
  target_ids:
  - habitatmech:GOLD.3d529a667e
  field_paths:
  - exact_synonyms
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETREQ
  - EP1
  - EP2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.3d529a667e
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Remove bare host clade label 'Fish' from exact_synonym in curation/term_requests.tsv
    row 9 for habitatmech:GOLD.3d529a667e (retaining 'fish host environment') and
    add a guarded row in curation/definition_source_label_exclusions.tsv so the displaced
    GOLD source label 'Fish' is not retained as an EXACT_SYNONYM on fish-associated
    environment.
  generator: Update curation/term_requests.tsv and curation/definition_source_label_exclusions.tsv,
    then run just seed, just seed-canary, just seed-apply, just term-requests, and
    just render.
  acceptance_checks:
  - Verify exact_synonyms on data/habitats/host_associated/fish.yaml retains only
    'fish host environment' and omits bare 'Fish'.
  - Run just qc and just validate-products.
limitations:
- Only the cited repository inputs, ontology terms, and source inventories were inspected;
  original specimen-level support for every upstream source assertion was not exhaustively
  reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism,
  or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus
  identifier certification.
- 'Read-only review: no curation table, generated habitat YAML, status, or history
  record was modified.'
notes:
- All target and context inputs were captured at clean git commit 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
- Structured-review archive traversal confirmed no prior target review bundle exists
  for this record.
tags:
- individual-scientific-review
- host-associated
```
