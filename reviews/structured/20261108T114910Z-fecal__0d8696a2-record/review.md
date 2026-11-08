# Record review: mollusc feces (habitatmech:GOLD.e60074d642)

- Review: 20261108T114910Z-fecal__0d8696a2-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-08T11:41:00Z
- Finished UTC: 2026-11-08T11:49:10Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The minted GOLD record habitatmech:GOLD.e60074d642 (mollusc feces in Host-associated &gt; Mollusca &gt; Digestive system &gt; Intestine &gt; Fecal, UNGROUNDED/REVIEWED, no assertion count/unit; total_assertions: 0 in GOLD) is coherently defined under UBERON:0001988 (feces) with parent_mode REPLACE to exclude anatomical Intestine and displaced source label 'Fecal' omitted from synonyms (SOURCE_SYNONYM_EXCLUDED).

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/fecal__0d8696a2.yaml) at captured main revision 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (fecal__0d8696a2 through fin); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.e60074d642 | data/habitats/host_associated/fecal__0d8696a2.yaml | generated | mollusc feces |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.e60074d642 | Completed 2026-11-08T11:48:10Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.e60074d642 | Completed 2026-11-08T11:48:35Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.e60074d642 | Completed 2026-11-08T11:48:40Z. No issues found; 870 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.e60074d642 | Completed 2026-11-08T11:48:42Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.e60074d642 | Completed 2026-11-08T11:48:45Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.e60074d642 | Completed 2026-11-08T11:48:48Z. validated 93 causal-graph curation file(s) with 93 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.e60074d642 | Completed 2026-11-08T11:48:55Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:GOLD.e60074d642 | Completed 2026-11-08T11:57:10Z. OK_CANONICAL: 1209, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2088. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.e60074d642.

Individual schema, strict 24-target validation, 870 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 93 causal overlays, and 671 term requests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:GOLD.e60074d642.

The record defines mollusc feces under UBERON:0001988 (feces) with parent_mode REPLACE to exclude anatomical molluscan Intestine (habitatmech:GOLD.3474d6c4ab), retains curated exact synonyms ('molluscan fecal pellet', 'molluscan feces'), and omits displaced GOLD source label 'Fecal' from synonyms (SOURCE_SYNONYM_EXCLUDED) via curation/definition_source_label_exclusions.tsv.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.e60074d642.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.e60074d642.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/fecal__0d8696a2.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.e60074d642 (mollusc feces) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon and life-stage organism terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.e60074d642, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["UBERON:0001988"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 2480 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Fecal", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mollusca", "ecosystem_subtype": "Hindgut", "ecosystem_type": "Digestive system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:7838", "leaf_label": "Fecal", "organism_count": "0", "specific_ecosystem": "Fecal", "study_count": "0", "total_assertions": "0"}, "row": 2480}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 13092 | supports | [{"data": {"definition": "Portion of semisolid bodily waste discharged through the anus[MW,modified].", "deprecated": "", "directly_referenced": "TRUE", "label": "feces", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "cow dung&#124;cow pat&#124;droppings&#124;dung&#124;excrement&#124;excreta&#124;faeces&#124;fecal material&#124;fecal matter&#124;fewmet&#124;frass&#124;guano&#124;ordure&#124;piece of shit&#124;portion of dung&#124;portion of excrement&#124;portion of faeces&#124;portion of fecal material&#124;portion of fecal matter&#124;portion of feces&#124;portion of guano&#124;portion of scat&#124;portionem cacas&#124;scat&#124;spoor&#124;spraint&#124;stool", "term_id": "UBERON:0001988"}, "row": 13092}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 11287,11594 | supports | [{"data": {"object": "UBERON:0000174", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001988"}, "row": 11287}, {"data": {"object": "UBERON:0001988", "predicate": "rdfs:subClassOf", "subject": "UBERON:0007109"}, "row": 11594}] |
| EDEC | curation/decisions.tsv; TSV rows 1290 | supports | [{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.e60074d642", "notes": "ITEM curation: GOLD 'Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Fecal' denotes molluscan fecal biodeposits rather than the hindgut organ. Define under UBERON:0001988 (feces) with parent_mode REPLACE and exclude bare 'Fecal' (PMID 29487366; DOI:10.3389/fmicb.2018.00286). Path: Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Fecal", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 1290}] |
| ETR | curation/term_requests.tsv; TSV rows 374 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "definition": "A feces (biodeposit) excreted from the hindgut of a mollusc.", "exact_synonym": "molluscan feces&#124;mollusc biodeposit", "identifier": "habitatmech:GOLD.e60074d642", "notes": "ITEM curation: GOLD 'Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Fecal' denotes molluscan fecal biodeposits rather than the hindgut organ. Define under UBERON:0001988 (feces) with parent_mode REPLACE and exclude bare 'Fecal' (PMID 29487366; DOI:10.3389/fmicb.2018.00286). Path: Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Fecal", "parent_class": "UBERON:0001988", "parent_label": "feces", "parent_mode": "REPLACE", "requested_label": "mollusc feces"}, "row": 374}] |
| ELE | curation/definition_source_label_exclusions.tsv; TSV rows 160 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "identifier": "habitatmech:GOLD.e60074d642", "notes": "Displaced GOLD source label 'Fecal' in path 'Host-associated &gt; Mollusca &gt; Digestive system &gt; Hindgut &gt; Fecal' is context-dependent, ambiguous, or names a host/disease/process rather than the defined habitat 'mollusc feces'; suppress automatic exact-synonym retention while preserving verbatim source provenance.", "requested_label": "mollusc feces", "source_label": "Fecal"}, "row": 160}] |
| EP1 | data/habitats/host_associated/feces.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "Portion of semisolid bodily waste discharged through the anus[MW,modified].", "grounding_status": "EXACT", "identifier": "UBERON:0001988", "label": "feces", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:00002276", "UBERON:0000174", "UBERON:0001555", "habitatmech:GOLD.5b0aa7456c", "habitatmech:GOLD.6bda0871e2", "habitatmech:GOLD.b091b80314"], "source_attestations": [{"assertion_count": 2421, "assertion_unit": "STRAIN", "mapping_predicate": "skos:exactMatch", "source": "BACDIVE", "source_id": "bacdive.isolation_source:feces-stool", "source_label": "Feces-Stool"}, {"assertion_count": 13744, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "source": "GOLD", "source_id": "gold.ecosystem:3920", "source_label": "Fecal", "source_path": "Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Large intestine &gt; Fecal"}, {"assertion_count": 4785, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "source": "GOLD", "source_id": "gold.ecosystem:4104", "source_label": "Fecal", "source_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Fecal"}, {"assertion_count": 1229, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:exactMatch", "source": "GOLD", "source_id": "gold.ecosystem:4957", "source_label": "Fecal", "source_path": "Host-associated &gt; Birds &gt; Digestive system &gt; Large intestine &gt; Fecal"}, {"assertion_count": 2, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:broadMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6471", "source_label": "Guano", "source_path": "Engineered &gt; Solid waste &gt; Animal waste &gt; Guano"}, {"assertion_count": 3, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:closeMatch", "source": "GOLD", "source_id": "gold.ecosystem:8175", "source_label": "Cast", "source_path": "Host-associated &gt; Annelida &gt; Digestive system &gt; Digestive tube &gt; Cast"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'fecal__0d8696a2&#124;habitatmech:GOLD.e60074d642' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,088 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- All included input bytes match both the clean working tree and exact captured Git revision 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.
- Structured archive traversal found no earlier structured review targeting this record. No existing bundle is superseded or closed.
- This read-only Stage-4 review proposes maintained-owner actions and preserves open findings for Stage 5 grouped remediation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261108T114910Z-fecal__0d8696a2-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: mollusc feces (habitatmech:GOLD.e60074d642)'
started_at: '2026-11-08T11:41:00Z'
finished_at: '2026-11-08T11:49:10Z'
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
summary: 'The minted GOLD record habitatmech:GOLD.e60074d642 (mollusc feces in Host-associated
  > Mollusca > Digestive system > Intestine > Fecal, UNGROUNDED/REVIEWED, no assertion
  count/unit; total_assertions: 0 in GOLD) is coherently defined under UBERON:0001988
  (feces) with parent_mode REPLACE to exclude anatomical Intestine and displaced source
  label ''Fecal'' omitted from synonyms (SOURCE_SYNONYM_EXCLUDED).'
source:
  git_revision: 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e
  state: git_commit
  inputs:
  - path: curation/decisions.tsv
    sha256: 7e0e28eeca775e7795d3f72384794f392fcf287f7f972fa57042234a64d3ce40
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 596d59ab03fafa4c1fcdcb6446c87b7c72c04305e9d516047e661060710e86d4
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 913f1ece5224bbed33b736f78cc8e1244155e91f390fe8e790d6f91a24b3b796
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: f86df360f54cb00d3062ae27a9196828113219c06cfd9cfc9830a0e08603d069
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/fecal__0d8696a2.yaml
    sha256: 67f1694100c5caec45e311155198921fe59680be2242e7671a45f679b5396bd9
    role: target
  - path: data/habitats/host_associated/feces.yaml
    sha256: 8fc3ef983646fb278130da29b370d5448ac99af2762f66746aad06d187d3fddb
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
- target_id: habitatmech:GOLD.e60074d642
  path: data/habitats/host_associated/fecal__0d8696a2.yaml
  label: mollusc feces
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/fecal__0d8696a2.yaml)
    at captured main revision 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (fecal__0d8696a2 through fin); this bundle assesses its single resolved
    identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.e60074d642
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
    --target-class HabitatRecord data/habitats/host_associated/fecal__0d8696a2.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.e60074d642
  summary: Completed 2026-11-08T11:48:10Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/fecal__0d8696a2.yaml
    data/habitats/host_associated/fecal__0e10427f.yaml data/habitats/host_associated/fecal__69dad039.yaml
    data/habitats/host_associated/fecal__89494a72.yaml data/habitats/host_associated/fecal__c047ee1e.yaml
    data/habitats/host_associated/fecal__ceae17b6.yaml data/habitats/host_associated/fecal__d12909cd.yaml
    data/habitats/host_associated/fecal__e9f04eec.yaml data/habitats/host_associated/feces.yaml
    data/habitats/host_associated/felidae_cat.yaml data/habitats/host_associated/female_reproductive_system.yaml
    data/habitats/host_associated/fetal_tissue.yaml data/habitats/host_associated/fetal_tissue__610eb0c8.yaml
    data/habitats/host_associated/fetus.yaml data/habitats/host_associated/fetus__250e9844.yaml
    data/habitats/host_associated/fiber.yaml data/habitats/host_associated/fibroblast.yaml
    data/habitats/host_associated/fibrocartilage.yaml data/habitats/host_associated/fibrocartilage__9cc92423.yaml
    data/habitats/host_associated/fibroma.yaml data/habitats/host_associated/filament.yaml
    data/habitats/host_associated/filiform_warts.yaml data/habitats/host_associated/filter_chamber.yaml
    data/habitats/host_associated/fin.yaml --out .temp/c7s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.e60074d642
  summary: 'Completed 2026-11-08T11:48:35Z. Validated 24 files; files with ERROR:
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
  - habitatmech:GOLD.e60074d642
  summary: Completed 2026-11-08T11:48:40Z. No issues found; 870 history record(s)
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
  - habitatmech:GOLD.e60074d642
  summary: 'Completed 2026-11-08T11:48:42Z. provenance current: 14 committed inventories,
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
  - habitatmech:GOLD.e60074d642
  summary: 'Completed 2026-11-08T11:48:45Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:GOLD.e60074d642
  summary: Completed 2026-11-08T11:48:48Z. validated 93 causal-graph curation file(s)
    with 93 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.e60074d642
  summary: Completed 2026-11-08T11:48:55Z. term-request table is current (671 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.e60074d642
  summary: 'Completed 2026-11-08T11:57:10Z. OK_CANONICAL: 1209, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2088. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/fecal__0d8696a2.yaml
  locator: Entire YAML
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.e60074d642 (mollusc feces) were read.
  snapshot_sha256: 67f1694100c5caec45e311155198921fe59680be2242e7671a45f679b5396bd9
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon and life-stage
    organism terms cannot substitute for associated environments; parent_habitats
    must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.e60074d642, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["UBERON:0001988"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2480
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mollusca > Digestive system > Hindgut > Fecal", "depth": "5", "ecosystem": "Host-associated",
    "ecosystem_category": "Mollusca", "ecosystem_subtype": "Hindgut", "ecosystem_type":
    "Digestive system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:7838",
    "leaf_label": "Fecal", "organism_count": "0", "specific_ecosystem": "Fecal", "study_count":
    "0", "total_assertions": "0"}, "row": 2480}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 13092
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: '[{"data": {"definition": "Portion of semisolid bodily waste discharged
    through the anus[MW,modified].", "deprecated": "", "directly_referenced": "TRUE",
    "label": "feces", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "cow
    dung|cow pat|droppings|dung|excrement|excreta|faeces|fecal material|fecal matter|fewmet|frass|guano|ordure|piece
    of shit|portion of dung|portion of excrement|portion of faeces|portion of fecal
    material|portion of fecal matter|portion of feces|portion of guano|portion of
    scat|portionem cacas|scat|spoor|spraint|stool", "term_id": "UBERON:0001988"},
    "row": 13092}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 11287,11594
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0000174", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0001988"}, "row": 11287}, {"data": {"object": "UBERON:0001988",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0007109"}, "row": 11594}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 1290
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17",
    "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.e60074d642",
    "notes": "ITEM curation: GOLD ''Host-associated > Mollusca > Digestive system
    > Hindgut > Fecal'' denotes molluscan fecal biodeposits rather than the hindgut
    organ. Define under UBERON:0001988 (feces) with parent_mode REPLACE and exclude
    bare ''Fecal'' (PMID 29487366; DOI:10.3389/fmicb.2018.00286). Path: Host-associated
    > Mollusca > Digestive system > Hindgut > Fecal", "object_id": "", "object_label":
    "", "relation": "", "review_depth": "ITEM"}, "row": 1290}]'
  snapshot_sha256: 7e0e28eeca775e7795d3f72384794f392fcf287f7f972fa57042234a64d3ce40
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV rows 374
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "definition":
    "A feces (biodeposit) excreted from the hindgut of a mollusc.", "exact_synonym":
    "molluscan feces|mollusc biodeposit", "identifier": "habitatmech:GOLD.e60074d642",
    "notes": "ITEM curation: GOLD ''Host-associated > Mollusca > Digestive system
    > Hindgut > Fecal'' denotes molluscan fecal biodeposits rather than the hindgut
    organ. Define under UBERON:0001988 (feces) with parent_mode REPLACE and exclude
    bare ''Fecal'' (PMID 29487366; DOI:10.3389/fmicb.2018.00286). Path: Host-associated
    > Mollusca > Digestive system > Hindgut > Fecal", "parent_class": "UBERON:0001988",
    "parent_label": "feces", "parent_mode": "REPLACE", "requested_label": "mollusc
    feces"}, "row": 374}]'
  snapshot_sha256: f86df360f54cb00d3062ae27a9196828113219c06cfd9cfc9830a0e08603d069
- evidence_id: ELE
  kind: database
  reference: curation/definition_source_label_exclusions.tsv
  locator: TSV rows 160
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "identifier":
    "habitatmech:GOLD.e60074d642", "notes": "Displaced GOLD source label ''Fecal''
    in path ''Host-associated > Mollusca > Digestive system > Hindgut > Fecal'' is
    context-dependent, ambiguous, or names a host/disease/process rather than the
    defined habitat ''mollusc feces''; suppress automatic exact-synonym retention
    while preserving verbatim source provenance.", "requested_label": "mollusc feces",
    "source_label": "Fecal"}, "row": 160}]'
  snapshot_sha256: 596d59ab03fafa4c1fcdcb6446c87b7c72c04305e9d516047e661060710e86d4
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/feces.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-08T11:49:10Z'
  support: supports
  summary: '{"definition": "Portion of semisolid bodily waste discharged through the
    anus[MW,modified].", "grounding_status": "EXACT", "identifier": "UBERON:0001988",
    "label": "feces", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:00002276",
    "UBERON:0000174", "UBERON:0001555", "habitatmech:GOLD.5b0aa7456c", "habitatmech:GOLD.6bda0871e2",
    "habitatmech:GOLD.b091b80314"], "source_attestations": [{"assertion_count": 2421,
    "assertion_unit": "STRAIN", "mapping_predicate": "skos:exactMatch", "source":
    "BACDIVE", "source_id": "bacdive.isolation_source:feces-stool", "source_label":
    "Feces-Stool"}, {"assertion_count": 13744, "assertion_unit": "ORGANISM", "mapping_predicate":
    "skos:exactMatch", "source": "GOLD", "source_id": "gold.ecosystem:3920", "source_label":
    "Fecal", "source_path": "Host-associated > Mammals: Human > Digestive system >
    Large intestine > Fecal"}, {"assertion_count": 4785, "assertion_unit": "ORGANISM",
    "mapping_predicate": "skos:exactMatch", "source": "GOLD", "source_id": "gold.ecosystem:4104",
    "source_label": "Fecal", "source_path": "Host-associated > Mammals > Digestive
    system > Large intestine > Fecal"}, {"assertion_count": 1229, "assertion_unit":
    "ORGANISM", "mapping_predicate": "skos:exactMatch", "source": "GOLD", "source_id":
    "gold.ecosystem:4957", "source_label": "Fecal", "source_path": "Host-associated
    > Birds > Digestive system > Large intestine > Fecal"}, {"assertion_count": 2,
    "assertion_unit": "ORGANISM", "mapping_predicate": "skos:broadMatch", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:6471", "source_label": "Guano",
    "source_path": "Engineered > Solid waste > Animal waste > Guano"}, {"assertion_count":
    3, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:closeMatch", "source":
    "GOLD", "source_id": "gold.ecosystem:8175", "source_label": "Cast", "source_path":
    "Host-associated > Annelida > Digestive system > Digestive tube > Cast"}]}'
  snapshot_sha256: 8fc3ef983646fb278130da29b370d5448ac99af2762f66746aad06d187d3fddb
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'fecal__0d8696a2|habitatmech:GOLD.e60074d642' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-08T11:49:10Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, strict 24-target validation, 870 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 93 causal
    overlays, and 671 term requests passed.
  target_ids:
  - habitatmech:GOLD.e60074d642
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: The record defines mollusc feces under UBERON:0001988 (feces) with parent_mode
    REPLACE to exclude anatomical molluscan Intestine (habitatmech:GOLD.3474d6c4ab),
    retains curated exact synonyms ('molluscan fecal pellet', 'molluscan feces'),
    and omits displaced GOLD source label 'Fecal' from synonyms (SOURCE_SYNONYM_EXCLUDED)
    via curation/definition_source_label_exclusions.tsv.
  target_ids:
  - habitatmech:GOLD.e60074d642
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ELE
  - EP1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.e60074d642
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - ELE
  - EP1
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.e60074d642
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
- Configured label correspondence skipped 2,088 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- All included input bytes match both the clean working tree and exact captured Git
  revision 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.
- Structured archive traversal found no earlier structured review targeting this record.
  No existing bundle is superseded or closed.
- This read-only Stage-4 review proposes maintained-owner actions and preserves open
  findings for Stage 5 grouped remediation.
tags:
- individual-scientific-review
- host-associated
```
