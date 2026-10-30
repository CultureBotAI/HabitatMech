# Record review: Egg (habitatmech:BACDIVE.d48ce9485d)

- Review: 20261026T083019Z-egg-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-26T08:24:00Z
- Finished UTC: 2026-10-26T08:30:19Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The minted BacDive record habitatmech:BACDIVE.d48ce9485d (Egg, UNGROUNDED/REVIEWED, 35 STRAIN assertions, 25 displayed characteristic taxa from a 30-taxon pool) is confirmed ungrounded as a host-body-product isolation category (#2051), rejecting FOODON:00001274 (egg food product) and reproducing exact raw strain-count provenance.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/egg.yaml) at captured main revision 1a40d0958114e6e3facd148ccec6197fa4dd679c.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (ear_discharge through empyema); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 1a40d0958114e6e3facd148ccec6197fa4dd679c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:BACDIVE.d48ce9485d | data/habitats/host_associated/egg.yaml | generated | Egg |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:BACDIVE.d48ce9485d | Completed 2026-10-26T08:25:36Z. No issues found. |
| validate-strict | passed | True | habitatmech:BACDIVE.d48ce9485d | Completed 2026-10-26T08:25:42Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:BACDIVE.d48ce9485d | Completed 2026-10-26T08:25:48Z. No issues found; 852 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:BACDIVE.d48ce9485d | Completed 2026-10-26T08:25:49Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:BACDIVE.d48ce9485d | Completed 2026-10-26T08:26:03Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:BACDIVE.d48ce9485d | Completed 2026-10-26T08:26:07Z. validated 53 causal-graph curation file(s) with 53 graph(s). |
| term-requests-check | passed | True | habitatmech:BACDIVE.d48ce9485d | Completed 2026-10-26T08:26:21Z. term-request table is current (661 terms). |
| validate-products | passed | True | habitatmech:BACDIVE.d48ce9485d | Completed 2026-10-26T08:27:01Z. OK_CANONICAL: 1194, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2063. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:BACDIVE.d48ce9485d.

Individual schema, strict 24-target validation, 852 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 53 causal overlays, and 661 term requests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:BACDIVE.d48ce9485d.

BacDive isolation source 'Egg' (bacdive.isolation_source:egg) is confirmed ungrounded via CONFIRM_UNGROUNDED (#2051) because the source category is &#96;#Host Body-Product &gt; #Egg&#96; rather than a food product (&#96;FOODON:00001274 'egg food product'&#96;).

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:BACDIVE.d48ce9485d.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "BACDIVE", "count": 35, "unit": "STRAIN"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:BACDIVE.d48ce9485d.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/egg.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:BACDIVE.d48ce9485d (Egg) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:BACDIVE.d48ce9485d, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=[]. |
| EBACDIVE | data/raw/bacdive_isolation_sources.tsv; TSV rows 105 | supports | [{"data": {"bacdive_id": "bacdive.isolation_source:egg", "label": "Egg", "source_slug": "egg", "strain_count": "35", "taxon_count": "30"}, "row": 105}] |
| EGROUND | data/raw/isolation_source_groundings.tsv; TSV rows 99 | supports | [{"data": {"confidence": "medium", "curator": "ols4_auto", "mapping_justification": "semapv:LexicalMatching", "object_id": "FOODON:00001274", "object_label": "egg food product", "object_source": "FOODON", "predicate_id": "skos:closeMatch", "source_dataset": "bacdive", "subject_label": "Egg", "subject_label_normalized": "egg", "verified_date": ""}, "row": 99}] |
| EDEC | curation/decisions.tsv; TSV rows 1734 | supports | [{"data": {"category": "HOST_ASSOCIATED", "curator": "codex-gpt-5", "date": "2026-10-14", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:BACDIVE.d48ce9485d", "notes": "Source-identity correction (#2051): BacDive Egg is a host-body-product isolation category, not a food-only vocabulary branch. Exact stored strain DSM 19883 (BacDive https://bacdive.dsmz.de/strain/7355) was isolated from a chironomid egg mass in a waste-stabilization pond; DSM 18103 (https://bacdive.dsmz.de/strain/5652) from halibut egg epiflora. Both explicitly carry Host Body Product &gt; Urogenital tract &gt; Egg. Reject FOODON:00001274 'egg food product' and its vertebrate-food restriction; retain the native source habitat with HOST_ASSOCIATED coarse placement, not whole-organism ontology identity or NOT_APPLICABLE. No verified exact identity for this source scope is established in the committed slice; this is not global ontology absence. Preserve all 35 STRAIN-unit source assertions and all 25 displayed taxon observations/ranks from the 30-taxon pool. Two exact-strain witnesses do not reconstruct every original member or justify a source split, characteristic-presence claim or merger with GOLD Egg products.", "object_id": "", "object_label": "", "relation": "parent", "review_depth": "ITEM"}, "row": 1734}] |
| ESEARCH | Local input and review traversal; grep -rn -E 'egg&#124;habitatmech:BACDIVE.d48ce9485d' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,063 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- All included input bytes match both the clean working tree and exact captured Git revision 1a40d0958114e6e3facd148ccec6197fa4dd679c.
- Structured archive traversal found no earlier structured review targeting this record. No existing bundle is superseded or closed.
- This read-only Stage-4 review proposes maintained-owner actions and preserves open findings for Stage 5 grouped remediation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261026T083019Z-egg-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Egg (habitatmech:BACDIVE.d48ce9485d)'
started_at: '2026-10-26T08:24:00Z'
finished_at: '2026-10-26T08:30:19Z'
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
summary: The minted BacDive record habitatmech:BACDIVE.d48ce9485d (Egg, UNGROUNDED/REVIEWED,
  35 STRAIN assertions, 25 displayed characteristic taxa from a 30-taxon pool) is
  confirmed ungrounded as a host-body-product isolation category (#2051), rejecting
  FOODON:00001274 (egg food product) and reproducing exact raw strain-count provenance.
source:
  git_revision: 1a40d0958114e6e3facd148ccec6197fa4dd679c
  state: git_commit
  inputs:
  - path: curation/decisions.tsv
    sha256: f7b5c0d1abf850eea20eb9ac3d76c3caec573f1d68dd0467cbf8d5f9ff9f50cb
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: cae6e8f2391c5cd4b5b97d2f07849fcdd0bb100cba72ad27d97b90f417532da0
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: d3608f94d77d1709c6fa01e93800e326853b9c027b080692128e80a6039f5c28
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: eae6c1d3d8ceafb8960c41a58cdd1fa1eb83fbefea57dc67bcd0ea6b7357d273
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/egg.yaml
    sha256: 4442ae82f9df6071c9c46f1f0ce6db9210ed6b836e497ccfbb22525c11ee2781
    role: target
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
- target_id: habitatmech:BACDIVE.d48ce9485d
  path: data/habitats/host_associated/egg.yaml
  label: Egg
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/egg.yaml)
    at captured main revision 1a40d0958114e6e3facd148ccec6197fa4dd679c.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (ear_discharge through empyema); this bundle assesses its single resolved
    identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  exclusions:
  - target: Other habitat records and SSSOM/KGX products
    reason: Direct parents inform hierarchy interpretation but are not additional
      completed reviews; exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: .venv/bin/python -m linkml.validator.cli -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/egg.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  summary: Completed 2026-10-26T08:25:36Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/ear_discharge.yaml
    data/habitats/host_associated/ear_discharge__c59c71e2.yaml data/habitats/host_associated/eccrine_sweat_gland.yaml
    data/habitats/host_associated/echinodermata.yaml data/habitats/host_associated/ectosymbionts.yaml
    data/habitats/host_associated/ectosymbionts__7a42a232.yaml data/habitats/host_associated/eczema.yaml
    data/habitats/host_associated/effusion.yaml data/habitats/host_associated/effusion__ef80da5d.yaml
    data/habitats/host_associated/egg.yaml data/habitats/host_associated/egg_capsule.yaml
    data/habitats/host_associated/eggs.yaml data/habitats/host_associated/eggs__79d5874d.yaml
    data/habitats/host_associated/elastic__846c7f5c.yaml data/habitats/host_associated/elastic_cartilage_tissue.yaml
    data/habitats/host_associated/electric_organ.yaml data/habitats/host_associated/elementary_body.yaml
    data/habitats/host_associated/embryo.yaml data/habitats/host_associated/embryo__3df16fcc.yaml
    data/habitats/host_associated/embryo__74685e7d.yaml data/habitats/host_associated/embryo__e76df6f3.yaml
    data/habitats/host_associated/embryonic_cell_line.yaml data/habitats/host_associated/embryonic_stem_cell.yaml
    data/habitats/host_associated/empyema.yaml --out /tmp/c3s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  summary: 'Completed 2026-10-26T08:25:42Z. Validated 24 files; files with ERROR:
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
  - habitatmech:BACDIVE.d48ce9485d
  summary: Completed 2026-10-26T08:25:48Z. No issues found; 852 history record(s)
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
  - habitatmech:BACDIVE.d48ce9485d
  summary: 'Completed 2026-10-26T08:25:49Z. provenance current: 14 committed inventories,
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
  - habitatmech:BACDIVE.d48ce9485d
  summary: 'Completed 2026-10-26T08:26:03Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:BACDIVE.d48ce9485d
  summary: Completed 2026-10-26T08:26:07Z. validated 53 causal-graph curation file(s)
    with 53 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  summary: Completed 2026-10-26T08:26:21Z. term-request table is current (661 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  summary: 'Completed 2026-10-26T08:27:01Z. OK_CANONICAL: 1194, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2063. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/egg.yaml
  locator: Entire YAML
  accessed_at: '2026-10-26T08:30:19Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:BACDIVE.d48ce9485d (Egg) were read.
  snapshot_sha256: 4442ae82f9df6071c9c46f1f0ce6db9210ed6b836e497ccfbb22525c11ee2781
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-10-26T08:30:19Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-10-26T08:30:19Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-10-26T08:30:19Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:BACDIVE.d48ce9485d, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=[].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EBACDIVE
  kind: database
  reference: data/raw/bacdive_isolation_sources.tsv
  locator: TSV rows 105
  accessed_at: '2026-10-26T08:30:19Z'
  support: supports
  summary: '[{"data": {"bacdive_id": "bacdive.isolation_source:egg", "label": "Egg",
    "source_slug": "egg", "strain_count": "35", "taxon_count": "30"}, "row": 105}]'
  snapshot_sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
- evidence_id: EGROUND
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: TSV rows 99
  accessed_at: '2026-10-26T08:30:19Z'
  support: supports
  summary: '[{"data": {"confidence": "medium", "curator": "ols4_auto", "mapping_justification":
    "semapv:LexicalMatching", "object_id": "FOODON:00001274", "object_label": "egg
    food product", "object_source": "FOODON", "predicate_id": "skos:closeMatch", "source_dataset":
    "bacdive", "subject_label": "Egg", "subject_label_normalized": "egg", "verified_date":
    ""}, "row": 99}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 1734
  accessed_at: '2026-10-26T08:30:19Z'
  support: supports
  summary: '[{"data": {"category": "HOST_ASSOCIATED", "curator": "codex-gpt-5", "date":
    "2026-10-14", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier":
    "habitatmech:BACDIVE.d48ce9485d", "notes": "Source-identity correction (#2051):
    BacDive Egg is a host-body-product isolation category, not a food-only vocabulary
    branch. Exact stored strain DSM 19883 (BacDive https://bacdive.dsmz.de/strain/7355)
    was isolated from a chironomid egg mass in a waste-stabilization pond; DSM 18103
    (https://bacdive.dsmz.de/strain/5652) from halibut egg epiflora. Both explicitly
    carry Host Body Product > Urogenital tract > Egg. Reject FOODON:00001274 ''egg
    food product'' and its vertebrate-food restriction; retain the native source habitat
    with HOST_ASSOCIATED coarse placement, not whole-organism ontology identity or
    NOT_APPLICABLE. No verified exact identity for this source scope is established
    in the committed slice; this is not global ontology absence. Preserve all 35 STRAIN-unit
    source assertions and all 25 displayed taxon observations/ranks from the 30-taxon
    pool. Two exact-strain witnesses do not reconstruct every original member or justify
    a source split, characteristic-presence claim or merger with GOLD Egg products.",
    "object_id": "", "object_label": "", "relation": "parent", "review_depth": "ITEM"},
    "row": 1734}]'
  snapshot_sha256: f7b5c0d1abf850eea20eb9ac3d76c3caec573f1d68dd0467cbf8d5f9ff9f50cb
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'egg|habitatmech:BACDIVE.d48ce9485d' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-10-26T08:30:19Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 1a40d0958114e6e3facd148ccec6197fa4dd679c.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, strict 24-target validation, 852 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 53 causal
    overlays, and 661 term requests passed.
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'BacDive isolation source ''Egg'' (bacdive.isolation_source:egg) is confirmed
    ungrounded via CONFIRM_UNGROUNDED (#2051) because the source category is `#Host
    Body-Product > #Egg` rather than a food product (`FOODON:00001274 ''egg food product''`).'
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EBACDIVE
  - EGROUND
  - EDEC
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "BACDIVE", "count": 35, "unit": "STRAIN"}]. Zero counts
    are omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EBACDIVE
  - EGROUND
  - EDEC
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:BACDIVE.d48ce9485d
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
- Configured label correspondence skipped 2,063 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- All included input bytes match both the clean working tree and exact captured Git
  revision 1a40d0958114e6e3facd148ccec6197fa4dd679c.
- Structured archive traversal found no earlier structured review targeting this record.
  No existing bundle is superseded or closed.
- This read-only Stage-4 review proposes maintained-owner actions and preserves open
  findings for Stage 5 grouped remediation.
tags:
- individual-scientific-review
- host-associated
```
