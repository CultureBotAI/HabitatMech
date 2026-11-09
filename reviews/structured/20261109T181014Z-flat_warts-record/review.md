# Record review: human flat wart (habitatmech:GOLD.79193f14f9)

- Review: 20261109T181014Z-flat_warts-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-09T18:08:00Z
- Finished UTC: 2026-11-09T18:10:14Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The curated GOLD record habitatmech:GOLD.79193f14f9 (human flat wart, 'Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Wart &gt; Flat warts', UNGROUNDED/REVIEWED, no assertion count/unit; total_assertions: 0 in GOLD row 2059) is coherently defined as a human cutaneous wart habitat under strictly broader parent BTO:0001859 (wart) via curation/term_requests.tsv row 592 (parent_mode ADD, combining with GOLD parent 'Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Wart' which resolves to BTO:0001859) with exact synonyms ('Flat warts', 'verruca plana') matching sibling filiform_warts.yaml and common_warts.yaml.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/flat_warts.yaml) at captured main revision 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (finger through free_living_state); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.79193f14f9 | data/habitats/host_associated/flat_warts.yaml | generated | human flat wart |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.79193f14f9 | Completed 2026-11-09T18:08:48Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.79193f14f9 | Completed 2026-11-09T18:08:54Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.79193f14f9 | Completed 2026-11-09T18:09:00Z. No issues found; 876 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.79193f14f9 | Completed 2026-11-09T18:09:01Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.79193f14f9 | Completed 2026-11-09T18:09:16Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.79193f14f9 | Completed 2026-11-09T18:09:22Z. validated 103 causal-graph curation file(s) with 103 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.79193f14f9 | Completed 2026-11-09T18:09:36Z. term-request table is current (674 terms). |
| validate-products | passed | True | habitatmech:GOLD.79193f14f9 | Completed 2026-11-09T18:10:17Z. OK_CANONICAL: 1213, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2094. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.79193f14f9.

Individual schema, strict 24-target validation, 876 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal overlays, and 674 term requests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:GOLD.79193f14f9.

The curated GOLD record habitatmech:GOLD.79193f14f9 (human flat wart, 'Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Wart &gt; Flat warts', UNGROUNDED/REVIEWED, no assertion count/unit; total_assertions: 0 in GOLD row 2059) is coherently defined as a human cutaneous wart habitat under strictly broader parent BTO:0001859 (wart) via curation/term_requests.tsv row 592 (parent_mode ADD, combining with GOLD parent 'Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Wart' which resolves to BTO:0001859) with exact synonyms ('Flat warts', 'verruca plana') matching sibling filiform_warts.yaml and common_warts.yaml.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.79193f14f9.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.79193f14f9.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/flat_warts.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.79193f14f9 (human flat wart) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and subcellular organelle terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.79193f14f9, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["BTO:0001859"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 2182 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Wart &gt; Flat warts", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype": "Wart", "ecosystem_type": "Benign tumor", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6667", "leaf_label": "Flat warts", "organism_count": "0", "specific_ecosystem": "Flat warts", "study_count": "0", "total_assertions": "0"}, "row": 2182}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 1859 | supports | [{"data": {"definition": "A horny projection on the skin usually of the extremities produced by proliferation of the skin papillae and caused by a papillomavirus.", "deprecated": "", "directly_referenced": "FALSE", "label": "wart", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001859"}, "row": 1859}] |
| EDEC | curation/decisions.tsv; TSV rows 739 | supports | [{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.79193f14f9", "notes": "Defined human flat wart under BTO:0001859 'wart'; supported by cutaneous papillomavirus lesion virome studies (PMID 25404569).", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 739}] |
| ETREQ | curation/term_requests.tsv; TSV rows 592 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "definition": "A wart presenting as a smooth, slightly elevated flat-topped papule on human facial, dorsal hand, or extremity skin induced by human papillomavirus (verruca plana).", "exact_synonym": "Flat warts&#124;verruca plana", "identifier": "habitatmech:GOLD.79193f14f9", "notes": "Defined human flat wart under BTO:0001859 'wart'; supported by cutaneous papillomavirus lesion virome studies (PMID 25404569).", "parent_class": "BTO:0001859", "parent_label": "wart", "parent_mode": "ADD", "requested_label": "human flat wart"}, "row": 592}] |
| EP1 | data/habitats/host_associated/wart.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "A horny projection on the skin usually of the extremities produced by proliferation of the skin papillae and caused by a papillomavirus.", "grounding_status": "EXACT", "identifier": "BTO:0001859", "label": "wart", "mapping_status": "SEEDED", "parent_habitats": ["habitatmech:GOLD.333c18201f"], "source_attestations": [{"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6226", "source_label": "Wart", "source_path": "Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Wart"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'flat_warts&#124;habitatmech:GOLD.79193f14f9' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

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
review_id: 20261109T181014Z-flat_warts-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: human flat wart (habitatmech:GOLD.79193f14f9)'
started_at: '2026-11-09T18:08:00Z'
finished_at: '2026-11-09T18:10:14Z'
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
summary: 'The curated GOLD record habitatmech:GOLD.79193f14f9 (human flat wart, ''Host-associated
  > Mammals: Human > Benign tumor > Wart > Flat warts'', UNGROUNDED/REVIEWED, no assertion
  count/unit; total_assertions: 0 in GOLD row 2059) is coherently defined as a human
  cutaneous wart habitat under strictly broader parent BTO:0001859 (wart) via curation/term_requests.tsv
  row 592 (parent_mode ADD, combining with GOLD parent ''Host-associated > Mammals:
  Human > Benign tumor > Wart'' which resolves to BTO:0001859) with exact synonyms
  (''Flat warts'', ''verruca plana'') matching sibling filiform_warts.yaml and common_warts.yaml.'
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
  - path: data/habitats/host_associated/flat_warts.yaml
    sha256: 13a97a0d2adc69ecdb313de39e957504e0badf89a9f6547a22b269cad69d53f3
    role: target
  - path: data/habitats/host_associated/wart.yaml
    sha256: 8dfbd965bef25cc428f75623bf410a7697050bbdb8609f8ec5e636eb45b1e559
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
- target_id: habitatmech:GOLD.79193f14f9
  path: data/habitats/host_associated/flat_warts.yaml
  label: human flat wart
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/flat_warts.yaml)
    at captured main revision 19d3ccb65e6b5128b9b0a5ae39cb509bf3f2bf39.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (finger through free_living_state); this bundle assesses its single
    resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.79193f14f9
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
    --target-class HabitatRecord data/habitats/host_associated/flat_warts.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.79193f14f9
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
  - habitatmech:GOLD.79193f14f9
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
  - habitatmech:GOLD.79193f14f9
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
  - habitatmech:GOLD.79193f14f9
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
  - habitatmech:GOLD.79193f14f9
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
  - habitatmech:GOLD.79193f14f9
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
  - habitatmech:GOLD.79193f14f9
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
  - habitatmech:GOLD.79193f14f9
  summary: 'Completed 2026-11-09T18:10:17Z. OK_CANONICAL: 1213, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2094. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/flat_warts.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T18:10:14Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.79193f14f9 (human flat wart) were read.
  snapshot_sha256: 13a97a0d2adc69ecdb313de39e957504e0badf89a9f6547a22b269cad69d53f3
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-09T18:10:14Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and subcellular organelle terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-09T18:10:14Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-09T18:10:14Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.79193f14f9, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["BTO:0001859"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2182
  accessed_at: '2026-11-09T18:10:14Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals: Human > Benign tumor > Wart > Flat warts", "depth": "5", "ecosystem":
    "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype":
    "Wart", "ecosystem_type": "Benign tumor", "gold_node_count": "1", "gold_node_ids":
    "gold.ecosystem:6667", "leaf_label": "Flat warts", "organism_count": "0", "specific_ecosystem":
    "Flat warts", "study_count": "0", "total_assertions": "0"}, "row": 2182}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 1859
  accessed_at: '2026-11-09T18:10:14Z'
  support: supports
  summary: '[{"data": {"definition": "A horny projection on the skin usually of the
    extremities produced by proliferation of the skin papillae and caused by a papillomavirus.",
    "deprecated": "", "directly_referenced": "FALSE", "label": "wart", "label_only":
    "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001859"}, "row":
    1859}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 739
  accessed_at: '2026-11-09T18:10:14Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17",
    "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.79193f14f9",
    "notes": "Defined human flat wart under BTO:0001859 ''wart''; supported by cutaneous
    papillomavirus lesion virome studies (PMID 25404569).", "object_id": "", "object_label":
    "", "relation": "", "review_depth": "ITEM"}, "row": 739}]'
  snapshot_sha256: d3bf0a3ca3570e8f318898db92f800a1e13220f64112fe5c1ce1edc9181c3ae2
- evidence_id: ETREQ
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV rows 592
  accessed_at: '2026-11-09T18:10:14Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "definition":
    "A wart presenting as a smooth, slightly elevated flat-topped papule on human
    facial, dorsal hand, or extremity skin induced by human papillomavirus (verruca
    plana).", "exact_synonym": "Flat warts|verruca plana", "identifier": "habitatmech:GOLD.79193f14f9",
    "notes": "Defined human flat wart under BTO:0001859 ''wart''; supported by cutaneous
    papillomavirus lesion virome studies (PMID 25404569).", "parent_class": "BTO:0001859",
    "parent_label": "wart", "parent_mode": "ADD", "requested_label": "human flat wart"},
    "row": 592}]'
  snapshot_sha256: ad853d6290dd72b2451d945a0545a5dc5272cc37c2296eaab78c99d2872d4b0c
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/wart.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-09T18:10:14Z'
  support: supports
  summary: '{"definition": "A horny projection on the skin usually of the extremities
    produced by proliferation of the skin papillae and caused by a papillomavirus.",
    "grounding_status": "EXACT", "identifier": "BTO:0001859", "label": "wart", "mapping_status":
    "SEEDED", "parent_habitats": ["habitatmech:GOLD.333c18201f"], "source_attestations":
    [{"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids
    share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source":
    "GOLD", "source_id": "gold.ecosystem:6226", "source_label": "Wart", "source_path":
    "Host-associated > Mammals: Human > Benign tumor > Wart"}]}'
  snapshot_sha256: 8dfbd965bef25cc428f75623bf410a7697050bbdb8609f8ec5e636eb45b1e559
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'flat_warts|habitatmech:GOLD.79193f14f9' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-09T18:10:14Z'
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
  - habitatmech:GOLD.79193f14f9
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'The curated GOLD record habitatmech:GOLD.79193f14f9 (human flat wart,
    ''Host-associated > Mammals: Human > Benign tumor > Wart > Flat warts'', UNGROUNDED/REVIEWED,
    no assertion count/unit; total_assertions: 0 in GOLD row 2059) is coherently defined
    as a human cutaneous wart habitat under strictly broader parent BTO:0001859 (wart)
    via curation/term_requests.tsv row 592 (parent_mode ADD, combining with GOLD parent
    ''Host-associated > Mammals: Human > Benign tumor > Wart'' which resolves to BTO:0001859)
    with exact synonyms (''Flat warts'', ''verruca plana'') matching sibling filiform_warts.yaml
    and common_warts.yaml.'
  target_ids:
  - habitatmech:GOLD.79193f14f9
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EDEC
  - ETREQ
  - EP1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted;
    unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.79193f14f9
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EDEC
  - ETREQ
  - EP1
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.79193f14f9
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings: []
actions: []
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
