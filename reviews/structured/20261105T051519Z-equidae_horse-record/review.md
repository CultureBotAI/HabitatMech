# Record review: equid-associated environment (habitatmech:BACDIVE.09c3544e85)

- Review: 20261105T051519Z-equidae_horse-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-05T04:39:00Z
- Finished UTC: 2026-11-05T05:15:19Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The minted BacDive record habitatmech:BACDIVE.09c3544e85 (equid-associated environment, BacDive: Equidae-Horse, UNGROUNDED/REVIEWED, 269 STRAIN assertions, 25 characteristic taxa from candidate_pool: 124) is defined under ENVO:01001002 (animal-associated environment) with upstream NCBITaxon:9788 noted as a non-habitat mapping, but retains host-taxon label 'Equidae-Horse' as an EXACT_SYNONYM from HabitatMech curation.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/equidae_horse.yaml) at captured main revision 215b23c90244e634e64f88fa2c1a2a3bb011880a.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (epicuticular_wax through excretory_system); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 215b23c90244e634e64f88fa2c1a2a3bb011880a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.09c3544e85 | data/habitats/host_associated/equidae_horse.yaml | generated | equid-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:BACDIVE.09c3544e85 | Completed 2026-11-05T04:42:18Z. No issues found. |
| validate-strict | passed | True | habitatmech:BACDIVE.09c3544e85 | Completed 2026-11-05T04:55:15Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:BACDIVE.09c3544e85 | Completed 2026-11-05T04:40:17Z. No issues found; 862 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:BACDIVE.09c3544e85 | Completed 2026-11-05T04:40:25Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:BACDIVE.09c3544e85 | Completed 2026-11-05T04:41:11Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:BACDIVE.09c3544e85 | Completed 2026-11-05T04:40:29Z. validated 73 causal-graph curation file(s) with 73 graph(s). |
| term-requests-check | passed | True | habitatmech:BACDIVE.09c3544e85 | Completed 2026-11-05T04:41:21Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:BACDIVE.09c3544e85 | Completed 2026-11-05T04:43:01Z. OK_CANONICAL: 1200, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2077. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:BACDIVE.09c3544e85.

Individual schema, strict 24-target validation, 862 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 73 causal overlays, and 671 term requests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:BACDIVE.09c3544e85.

Under HabitatMech's host-identity rule, a host organism/taxon label ('Equidae-Horse') is not an exact synonym of an organism-associated environment ('equid-associated environment'); sibling BacDive host-bucket records (bovinae_cow_cattle, canidae_dog, caprinae_sheep_goat) cleared exact_synonym in curation/term_requests.tsv and added guard rows in curation/definition_source_label_exclusions.tsv so automatic retention of the displaced BacDive host label in synonyms is suppressed (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim source_attestations.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:BACDIVE.09c3544e85.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "BACDIVE", "count": 269, "unit": "STRAIN"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:BACDIVE.09c3544e85.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Equid-associated environment asserts host-taxon label 'Equidae-Horse' as an exact synonym

major / open / confirmed; issue key: equidae-horse-host-name-exact-synonym.

Clear 'Equidae-Horse' from exact_synonym in curation/term_requests.tsv for habitatmech:BACDIVE.09c3544e85 and add a guarded exclusion row in curation/definition_source_label_exclusions.tsv so automatic retention of the displaced BacDive host label 'Equidae-Horse' as an EXACT_SYNONYM is omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim source_attestations (source_label: Equidae-Horse), matching sibling BacDive host-bucket records (bovinae_cow_cattle, canidae_dog, caprinae_sheep_goat).

## Recommended Actions And Acceptance Checks

### ACT1

Clear 'Equidae-Horse' from exact_synonym in curation/term_requests.tsv for habitatmech:BACDIVE.09c3544e85 and add a guarded exclusion row in curation/definition_source_label_exclusions.tsv so automatic retention of the displaced BacDive host label 'Equidae-Horse' as an EXACT_SYNONYM is omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) while preserving verbatim source_attestations (source_label: Equidae-Horse), matching sibling BacDive host-bucket records (bovinae_cow_cattle, canidae_dog, caprinae_sheep_goat). No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/equidae_horse.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:BACDIVE.09c3544e85 (equid-associated environment) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:BACDIVE.09c3544e85, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001002"]. |
| ESIB1 | data/habitats/host_associated/bovinae_cow_cattle.yaml; Entire YAML | supports | Sibling BacDive host-bucket record habitatmech:BACDIVE.a4a67c4a7f (bovine-associated environment) where exact_synonym was cleared and displaced source label 'Bovinae-Cow,-Cattle' was omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) via curation/definition_source_label_exclusions.tsv. |
| ESIB2 | data/habitats/host_associated/canidae_dog.yaml; Entire YAML | supports | Sibling BacDive host-bucket record habitatmech:BACDIVE.33fde10528 (canid-associated environment) where exact_synonym was cleared and displaced source label 'Canidae-Dog' was omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) via curation/definition_source_label_exclusions.tsv. |
| ESIB3 | data/habitats/host_associated/caprinae_sheep_goat.yaml; Entire YAML | supports | Sibling BacDive host-bucket record habitatmech:BACDIVE.4d3086a839 (caprine-associated environment) where exact_synonym was cleared and displaced source label 'Caprinae-Sheep,-Goat' was omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) via curation/definition_source_label_exclusions.tsv. |
| EBACDIVE | data/raw/bacdive_isolation_sources.tsv; TSV rows 47 | supports | [{"data": {"bacdive_id": "bacdive.isolation_source:equidae-horse", "label": "Equidae-Horse", "source_slug": "equidae-horse", "strain_count": "269", "taxon_count": "124"}, "row": 47}] |
| EGROUND | data/raw/isolation_source_groundings.tsv; TSV rows 106 | supports | [{"data": {"confidence": "medium", "curator": "ols4_auto", "mapping_justification": "semapv:LexicalMatching", "object_id": "NCBITaxon:9788", "object_label": "Equidae", "object_source": "NCBITaxon", "predicate_id": "skos:closeMatch", "source_dataset": "bacdive", "subject_label": "Equidae-Horse", "subject_label_normalized": "equidae horse", "verified_date": "2026-05-01"}, "row": 106}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 8491 | supports | [{"data": {"definition": "An environmental system determined by an animal.", "deprecated": "", "directly_referenced": "TRUE", "label": "animal-associated environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "Metazoan-associated environment&#124;animal environment", "term_id": "ENVO:01001002"}, "row": 8491}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 6797,6992,6996,7704 | supports | [{"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001002"}, "row": 6797}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001176"}, "row": 6992}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001179"}, "row": 6996}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001829"}, "row": 7704}] |
| EDEC | curation/decisions.tsv; TSV rows 1612 | supports | [{"data": {"category": "HOST_ASSOCIATED", "curator": "claude-opus-5", "date": "2026-08-16", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:BACDIVE.09c3544e85", "notes": "Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it \u2014 the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an &lt;X&gt;-associated environment. Host-associated &gt; Porifera was NOT_APPLICABLE while its own child Porifera &gt; Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. Category set to HOST_ASSOCIATED (#200): the row already claims ENVO:01001002 'animal-associated environment' as the nearest broader term, which is the claim that a living animal host defines the habitat, and every other record carrying that parent is HOST_ASSOCIATED. The category column was left blank here, so the seeder's default stood and five domestic-mammal hosts stayed in OTHER while their siblings did not. The reasoning above is unchanged.", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 1612}] |
| ETR | curation/term_requests.tsv; TSV rows 22 | supports | [{"data": {"curator": "claude-opus-5", "date": "2026-08-17", "definition": "An animal-associated environment which is determined by a horse or other equid.", "exact_synonym": "Equidae-Horse", "identifier": "habitatmech:BACDIVE.09c3544e85", "notes": "Definition drafted from the record's deep-research report under research/habitats/ and read against it; the report's proposed wording, genus and near-miss table are the evidence. ", "parent_class": "ENVO:01001002", "parent_label": "animal-associated environment", "parent_mode": "ADD", "requested_label": "equid-associated environment"}, "row": 22}] |
| EP1 | data/habitats/other/animal_associated_environment.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by an animal.", "grounding_status": "EXACT", "identifier": "ENVO:01001002", "label": "animal-associated environment", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"notes": "Physicochemical parameter bands from kg-microbe's environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal"}, {"assertion_count": 144, "assertion_unit": "TAXON", "source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated environment"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'equidae_horse&#124;habitatmech:BACDIVE.09c3544e85' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,077 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- All included input bytes match both the clean working tree and exact captured Git revision 215b23c90244e634e64f88fa2c1a2a3bb011880a.
- Structured archive traversal found no earlier structured review targeting this record. No existing bundle is superseded or closed.
- This read-only Stage-4 review proposes maintained-owner actions and preserves open findings for Stage 5 grouped remediation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T051519Z-equidae_horse-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: equid-associated environment (habitatmech:BACDIVE.09c3544e85)'
started_at: '2026-11-05T04:39:00Z'
finished_at: '2026-11-05T05:15:19Z'
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
summary: 'The minted BacDive record habitatmech:BACDIVE.09c3544e85 (equid-associated
  environment, BacDive: Equidae-Horse, UNGROUNDED/REVIEWED, 269 STRAIN assertions,
  25 characteristic taxa from candidate_pool: 124) is defined under ENVO:01001002
  (animal-associated environment) with upstream NCBITaxon:9788 noted as a non-habitat
  mapping, but retains host-taxon label ''Equidae-Horse'' as an EXACT_SYNONYM from
  HabitatMech curation.'
source:
  git_revision: 215b23c90244e634e64f88fa2c1a2a3bb011880a
  state: git_commit
  inputs:
  - path: curation/decisions.tsv
    sha256: 7e55e782625f544f2d3e4e5c9e5ed5d82c04d477ee606c894bc26cb55f8a949e
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 454bc07fdc75b4abdced785be5334e75d2955ea691fedb1122bf474b68cd73de
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: ec8f7b5cf7b804e31663653e482be907b0333a8be807259eec024fcb7acfeb94
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: d2ca8bb2a88649eef54ff812b40641a02f2ab39145168d65617503309ea9127c
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/bovinae_cow_cattle.yaml
    sha256: 2f7e0000d47e33359ddf75fdd86e95f552162165bf23239d37e6579639948fbd
    role: context
  - path: data/habitats/host_associated/canidae_dog.yaml
    sha256: 87552b6a21a0c1b436ff9e38322f21fa5c657e3c23eb4b0aaf56e62b32c03172
    role: context
  - path: data/habitats/host_associated/caprinae_sheep_goat.yaml
    sha256: abc9056f4b86556c0e319fc6d3b4c2bf6245f9a90565a5b14fa5c94dc6c4d0e2
    role: context
  - path: data/habitats/host_associated/equidae_horse.yaml
    sha256: 7edf1d3ac806ab86781a2cac76d5b5635526996bf2e8add5bd8b6977c0d5a8fe
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
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: habitatmech:BACDIVE.09c3544e85
  path: data/habitats/host_associated/equidae_horse.yaml
  label: equid-associated environment
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/equidae_horse.yaml)
    at captured main revision 215b23c90244e634e64f88fa2c1a2a3bb011880a.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (epicuticular_wax through excretory_system); this bundle assesses its
    single resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:BACDIVE.09c3544e85
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
    --target-class HabitatRecord data/habitats/host_associated/equidae_horse.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.09c3544e85
  summary: Completed 2026-11-05T04:42:18Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/epicuticular_wax.yaml
    data/habitats/host_associated/epidermal_cell.yaml data/habitats/host_associated/epidermis.yaml
    data/habitats/host_associated/epidermoid.yaml data/habitats/host_associated/epiphytes.yaml
    data/habitats/host_associated/epiphytes__ec31dd8e.yaml data/habitats/host_associated/epithelial_cell.yaml
    data/habitats/host_associated/epithelial_lining_fluid.yaml data/habitats/host_associated/epithelium.yaml
    data/habitats/host_associated/equidae_horse.yaml data/habitats/host_associated/erythrocyte.yaml
    data/habitats/host_associated/erythroleukemia_cell_line.yaml data/habitats/host_associated/esophageal_ulcer.yaml
    data/habitats/host_associated/esophagus.yaml data/habitats/host_associated/esophagus__25614af3.yaml
    data/habitats/host_associated/esophagus__2ce9b1a3.yaml data/habitats/host_associated/esophagus__d8421c5e.yaml
    data/habitats/host_associated/esophagus__e0ae9e65.yaml data/habitats/host_associated/esophagus__e4629951.yaml
    data/habitats/host_associated/ethmoid_bone.yaml data/habitats/host_associated/eustachian_tube.yaml
    data/habitats/host_associated/eustachian_tube__a8583033.yaml data/habitats/host_associated/excavata.yaml
    data/habitats/host_associated/excretory_system.yaml --out /tmp/c5s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.09c3544e85
  summary: 'Completed 2026-11-05T04:55:15Z. Validated 24 files; files with ERROR:
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
  - habitatmech:BACDIVE.09c3544e85
  summary: Completed 2026-11-05T04:40:17Z. No issues found; 862 history record(s)
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
  - habitatmech:BACDIVE.09c3544e85
  summary: 'Completed 2026-11-05T04:40:25Z. provenance current: 14 committed inventories,
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
  - habitatmech:BACDIVE.09c3544e85
  summary: 'Completed 2026-11-05T04:41:11Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:BACDIVE.09c3544e85
  summary: Completed 2026-11-05T04:40:29Z. validated 73 causal-graph curation file(s)
    with 73 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.09c3544e85
  summary: Completed 2026-11-05T04:41:21Z. term-request table is current (671 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.09c3544e85
  summary: 'Completed 2026-11-05T04:43:01Z. OK_CANONICAL: 1200, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2077. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/equidae_horse.yaml
  locator: Entire YAML
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:BACDIVE.09c3544e85 (equid-associated environment)
    were read.
  snapshot_sha256: 7edf1d3ac806ab86781a2cac76d5b5635526996bf2e8add5bd8b6977c0d5a8fe
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:BACDIVE.09c3544e85, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001002"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/bovinae_cow_cattle.yaml
  locator: Entire YAML
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: Sibling BacDive host-bucket record habitatmech:BACDIVE.a4a67c4a7f (bovine-associated
    environment) where exact_synonym was cleared and displaced source label 'Bovinae-Cow,-Cattle'
    was omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) via curation/definition_source_label_exclusions.tsv.
  snapshot_sha256: 2f7e0000d47e33359ddf75fdd86e95f552162165bf23239d37e6579639948fbd
- evidence_id: ESIB2
  kind: record_content
  reference: data/habitats/host_associated/canidae_dog.yaml
  locator: Entire YAML
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: Sibling BacDive host-bucket record habitatmech:BACDIVE.33fde10528 (canid-associated
    environment) where exact_synonym was cleared and displaced source label 'Canidae-Dog'
    was omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) via curation/definition_source_label_exclusions.tsv.
  snapshot_sha256: 87552b6a21a0c1b436ff9e38322f21fa5c657e3c23eb4b0aaf56e62b32c03172
- evidence_id: ESIB3
  kind: record_content
  reference: data/habitats/host_associated/caprinae_sheep_goat.yaml
  locator: Entire YAML
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: Sibling BacDive host-bucket record habitatmech:BACDIVE.4d3086a839 (caprine-associated
    environment) where exact_synonym was cleared and displaced source label 'Caprinae-Sheep,-Goat'
    was omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) via curation/definition_source_label_exclusions.tsv.
  snapshot_sha256: abc9056f4b86556c0e319fc6d3b4c2bf6245f9a90565a5b14fa5c94dc6c4d0e2
- evidence_id: EBACDIVE
  kind: database
  reference: data/raw/bacdive_isolation_sources.tsv
  locator: TSV rows 47
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: '[{"data": {"bacdive_id": "bacdive.isolation_source:equidae-horse", "label":
    "Equidae-Horse", "source_slug": "equidae-horse", "strain_count": "269", "taxon_count":
    "124"}, "row": 47}]'
  snapshot_sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
- evidence_id: EGROUND
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: TSV rows 106
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: '[{"data": {"confidence": "medium", "curator": "ols4_auto", "mapping_justification":
    "semapv:LexicalMatching", "object_id": "NCBITaxon:9788", "object_label": "Equidae",
    "object_source": "NCBITaxon", "predicate_id": "skos:closeMatch", "source_dataset":
    "bacdive", "subject_label": "Equidae-Horse", "subject_label_normalized": "equidae
    horse", "verified_date": "2026-05-01"}, "row": 106}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 8491
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: '[{"data": {"definition": "An environmental system determined by an animal.",
    "deprecated": "", "directly_referenced": "TRUE", "label": "animal-associated environment",
    "label_only": "FALSE", "ontology": "ENVO", "synonyms": "Metazoan-associated environment|animal
    environment", "term_id": "ENVO:01001002"}, "row": 8491}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 6797,6992,6996,7704
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: '[{"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001002"}, "row": 6797}, {"data": {"object": "ENVO:01001002",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:01001176"}, "row": 6992}, {"data":
    {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001179"},
    "row": 6996}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001829"}, "row": 7704}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 1612
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: '[{"data": {"category": "HOST_ASSOCIATED", "curator": "claude-opus-5",
    "date": "2026-08-16", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "",
    "identifier": "habitatmech:BACDIVE.09c3544e85", "notes": "Host-taxon reversal
    (#114): this was NOT_APPLICABLE on the reasoning that ''a host taxon is not a
    habitat''. That reasoning is wrong, and the corpus already contradicted it \u2014
    the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia,
    Mammals, Birds and Fish, which keep their own identity and a term request for
    an <X>-associated environment. Host-associated > Porifera was NOT_APPLICABLE while
    its own child Porifera > Sponge was a term request.An organism acting as a host
    IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated,
    animal-associated and fungi-associated environment. What is not a habitat is the
    TAXON TERM \u2014 a phylum is a class of organisms, not a place \u2014 so the
    taxon stays an xref (#99) and the concept keeps its own identity as a term-request
    candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger
    and false claim. Category set to HOST_ASSOCIATED (#200): the row already claims
    ENVO:01001002 ''animal-associated environment'' as the nearest broader term, which
    is the claim that a living animal host defines the habitat, and every other record
    carrying that parent is HOST_ASSOCIATED. The category column was left blank here,
    so the seeder''s default stood and five domestic-mammal hosts stayed in OTHER
    while their siblings did not. The reasoning above is unchanged.", "object_id":
    "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 1612}]'
  snapshot_sha256: 7e55e782625f544f2d3e4e5c9e5ed5d82c04d477ee606c894bc26cb55f8a949e
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV rows 22
  accessed_at: '2026-11-05T05:15:19Z'
  support: supports
  summary: '[{"data": {"curator": "claude-opus-5", "date": "2026-08-17", "definition":
    "An animal-associated environment which is determined by a horse or other equid.",
    "exact_synonym": "Equidae-Horse", "identifier": "habitatmech:BACDIVE.09c3544e85",
    "notes": "Definition drafted from the record''s deep-research report under research/habitats/
    and read against it; the report''s proposed wording, genus and near-miss table
    are the evidence. ", "parent_class": "ENVO:01001002", "parent_label": "animal-associated
    environment", "parent_mode": "ADD", "requested_label": "equid-associated environment"},
    "row": 22}]'
  snapshot_sha256: d2ca8bb2a88649eef54ff812b40641a02f2ab39145168d65617503309ea9127c
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/other/animal_associated_environment.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-05T05:15:19Z'
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
  locator: grep -rn -E 'equidae_horse|habitatmech:BACDIVE.09c3544e85' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-05T05:15:19Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 215b23c90244e634e64f88fa2c1a2a3bb011880a.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, strict 24-target validation, 862 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 73 causal
    overlays, and 671 term requests passed.
  target_ids:
  - habitatmech:BACDIVE.09c3544e85
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: Under HabitatMech's host-identity rule, a host organism/taxon label ('Equidae-Horse')
    is not an exact synonym of an organism-associated environment ('equid-associated
    environment'); sibling BacDive host-bucket records (bovinae_cow_cattle, canidae_dog,
    caprinae_sheep_goat) cleared exact_synonym in curation/term_requests.tsv and added
    guard rows in curation/definition_source_label_exclusions.tsv so automatic retention
    of the displaced BacDive host label in synonyms is suppressed (SOURCE_SYNONYM_EXCLUDED)
    while preserving verbatim source_attestations.
  target_ids:
  - habitatmech:BACDIVE.09c3544e85
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - ESIB2
  - ESIB3
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
    and pools: [{"source": "BACDIVE", "count": 269, "unit": "STRAIN"}]. Zero counts
    are omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:BACDIVE.09c3544e85
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - ESIB2
  - ESIB3
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
  - habitatmech:BACDIVE.09c3544e85
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: equidae-horse-host-name-exact-synonym
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: Equid-associated environment asserts host-taxon label 'Equidae-Horse' as
    an exact synonym
  description: 'Clear ''Equidae-Horse'' from exact_synonym in curation/term_requests.tsv
    for habitatmech:BACDIVE.09c3544e85 and add a guarded exclusion row in curation/definition_source_label_exclusions.tsv
    so automatic retention of the displaced BacDive host label ''Equidae-Horse'' as
    an EXACT_SYNONYM is omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) while preserving
    verbatim source_attestations (source_label: Equidae-Horse), matching sibling BacDive
    host-bucket records (bovinae_cow_cattle, canidae_dog, caprinae_sheep_goat).'
  target_ids:
  - habitatmech:BACDIVE.09c3544e85
  field_paths:
  - synonyms
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - ESIB2
  - ESIB3
  - EBACDIVE
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
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
  - habitatmech:BACDIVE.09c3544e85
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Clear ''Equidae-Horse'' from exact_synonym in curation/term_requests.tsv
    for habitatmech:BACDIVE.09c3544e85 and add a guarded exclusion row in curation/definition_source_label_exclusions.tsv
    so automatic retention of the displaced BacDive host label ''Equidae-Horse'' as
    an EXACT_SYNONYM is omitted from synonyms (SOURCE_SYNONYM_EXCLUDED) while preserving
    verbatim source_attestations (source_label: Equidae-Horse), matching sibling BacDive
    host-bucket records (bovinae_cow_cattle, canidae_dog, caprinae_sheep_goat). No
    repair is performed by this read-only review.'
  generator: Controlled source/curation update in Stage 5, then just seed, guarded
    just seed-canary, just seed-apply, and dependent term-request/map/site/redirect
    regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,077 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- All included input bytes match both the clean working tree and exact captured Git
  revision 215b23c90244e634e64f88fa2c1a2a3bb011880a.
- Structured archive traversal found no earlier structured review targeting this record.
  No existing bundle is superseded or closed.
- This read-only Stage-4 review proposes maintained-owner actions and preserves open
  findings for Stage 5 grouped remediation.
tags:
- individual-scientific-review
- host-associated
```
