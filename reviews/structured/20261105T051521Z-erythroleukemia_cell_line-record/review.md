# Record review: erythroleukemia cell line (BTO:0000846)

- Review: 20261105T051521Z-erythroleukemia_cell_line-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-05T04:39:00Z
- Finished UTC: 2026-11-05T05:15:21Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The PREGO-attested record BTO:0000846 (erythroleukemia cell line, EXACT/SEEDED, 1 TAXON assertion) is coherently grounded to BRENDA Tissue Ontology term BTO:0000846 under BTO:0000737 (leukemia cell line) with 5 PREGO RELATED_SYNONYMs and 1 literature-mined taxon association (no vendored BTO definition in ontology_terms.tsv).

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/erythroleukemia_cell_line.yaml) at captured main revision 215b23c90244e634e64f88fa2c1a2a3bb011880a.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (epicuticular_wax through excretory_system); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 215b23c90244e634e64f88fa2c1a2a3bb011880a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000846 | data/habitats/host_associated/erythroleukemia_cell_line.yaml | generated | erythroleukemia cell line |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000846 | Completed 2026-11-05T04:42:18Z. No issues found. |
| validate-strict | passed | True | BTO:0000846 | Completed 2026-11-05T04:55:15Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | BTO:0000846 | Completed 2026-11-05T04:40:17Z. No issues found; 862 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | BTO:0000846 | Completed 2026-11-05T04:40:25Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | BTO:0000846 | Completed 2026-11-05T04:41:11Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | BTO:0000846 | Completed 2026-11-05T04:40:29Z. validated 73 causal-graph curation file(s) with 73 graph(s). |
| term-requests-check | passed | True | BTO:0000846 | Completed 2026-11-05T04:41:21Z. term-request table is current (671 terms). |
| validate-products | passed | True | BTO:0000846 | Completed 2026-11-05T04:43:01Z. OK_CANONICAL: 1200, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2077. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: BTO:0000846.

Individual schema, strict 24-target validation, 862 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 73 causal overlays, and 671 term requests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: BTO:0000846.

BTO:0000846 (erythroleukemia cell line) is an exact cell-line habitat identity under strictly broader ontology parent BTO:0000737 (leukemia cell line) with 1 retained PREGO taxon association (noting as source limitations the absence of a vendored BTO definition and PREGO stemming variants 'erythroleukemia cell linous'/'erythroleukemic cell linous' in RELATED_SYNONYM).

### Source counts and retained ranking

quantity: supported. Targets: BTO:0000846.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "PREGO", "count": 1, "unit": "TAXON"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: BTO:0000846.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / EXACT; this read-only review does not mutate generated records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/erythroleukemia_cell_line.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for BTO:0000846 (erythroleukemia cell line) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=BTO:0000846, grounding_status=EXACT, mapping_status=SEEDED, parent_habitats=["BTO:0000737"]. |
| EPREGO | data/raw/prego_habitats.tsv; TSV rows 565 | supports | [{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "1", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0000846", "prego_synonyms": "erythroleukemia cell line&#124;erythroleukemia cell lines&#124;erythroleukemia cell linous&#124;erythroleukemic cell line&#124;erythroleukemic cell lines&#124;erythroleukemic cell linous", "taxon_count": "1"}, "row": 565}] |
| EPREGOTAXA | data/raw/prego_habitat_taxa.tsv; TSV rows 1437 | supports | 1 PREGO taxon-association rows for BTO:0000846. |
| EONT | data/raw/ontology_terms.tsv; TSV rows 738,847 | supports | [{"data": {"definition": "", "deprecated": "", "directly_referenced": "TRUE", "label": "leukemia cell line", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000737"}, "row": 738}, {"data": {"definition": "", "deprecated": "", "directly_referenced": "TRUE", "label": "erythroleukemia cell line", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000846"}, "row": 847}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 364,478,482,483,571,674,689,866,1617,1673,1728,2019 | supports | [{"data": {"object": "BTO:0000846", "predicate": "rdfs:subClassOf", "subject": "BTO:0000565"}, "row": 364}, {"data": {"object": "BTO:0001035", "predicate": "rdfs:subClassOf", "subject": "BTO:0000737"}, "row": 478}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf", "subject": "BTO:0000740"}, "row": 482}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf", "subject": "BTO:0000741"}, "row": 483}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf", "subject": "BTO:0000846"}, "row": 571}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf", "subject": "BTO:0001000"}, "row": 674}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf", "subject": "BTO:0001018"}, "row": 689}, {"data": {"object": "BTO:0000846", "predicate": "rdfs:subClassOf", "subject": "BTO:0001263"}, "row": 866}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf", "subject": "BTO:0002332"}, "row": 1617}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf", "subject": "BTO:0002406"}, "row": 1673}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf", "subject": "BTO:0002489"}, "row": 1728}, {"data": {"object": "BTO:0000846", "predicate": "rdfs:subClassOf", "subject": "BTO:0002885"}, "row": 2019}] |
| EP1 | data/habitats/host_associated/leukemia_cell_line.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": null, "grounding_status": "EXACT", "identifier": "BTO:0000737", "label": "leukemia cell line", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0001035"], "source_attestations": [{"assertion_count": 1, "assertion_unit": "TAXON", "evidence_channels": "annotated_genomes_isolates", "score": 3.0, "source": "PREGO", "source_id": "BTO:0000737", "source_label": "leukemia cell line"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'erythroleukemia_cell_line&#124;BTO:0000846' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

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
review_id: 20261105T051521Z-erythroleukemia_cell_line-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: erythroleukemia cell line (BTO:0000846)'
started_at: '2026-11-05T04:39:00Z'
finished_at: '2026-11-05T05:15:21Z'
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
summary: The PREGO-attested record BTO:0000846 (erythroleukemia cell line, EXACT/SEEDED,
  1 TAXON assertion) is coherently grounded to BRENDA Tissue Ontology term BTO:0000846
  under BTO:0000737 (leukemia cell line) with 5 PREGO RELATED_SYNONYMs and 1 literature-mined
  taxon association (no vendored BTO definition in ontology_terms.tsv).
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
  - path: data/habitats/host_associated/erythroleukemia_cell_line.yaml
    sha256: 00c5e6772aaea2b26f87b3f274578fa10de94c64f9565de5335bfa05502fbaac
    role: target
  - path: data/habitats/host_associated/leukemia_cell_line.yaml
    sha256: 057fba4dea9b812ad80e6731dd80511d0d407081d8ca36b2cf7d11fe70837b9d
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
- target_id: BTO:0000846
  path: data/habitats/host_associated/erythroleukemia_cell_line.yaml
  label: erythroleukemia cell line
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/erythroleukemia_cell_line.yaml)
    at captured main revision 215b23c90244e634e64f88fa2c1a2a3bb011880a.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (epicuticular_wax through excretory_system); this bundle assesses its
    single resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000846
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
    --target-class HabitatRecord data/habitats/host_associated/erythroleukemia_cell_line.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000846
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
  - BTO:0000846
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
  - BTO:0000846
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
  - BTO:0000846
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
  - BTO:0000846
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
  - BTO:0000846
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
  - BTO:0000846
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
  - BTO:0000846
  summary: 'Completed 2026-11-05T04:43:01Z. OK_CANONICAL: 1200, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2077. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/erythroleukemia_cell_line.yaml
  locator: Entire YAML
  accessed_at: '2026-11-05T05:15:21Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for BTO:0000846 (erythroleukemia cell line) were read.
  snapshot_sha256: 00c5e6772aaea2b26f87b3f274578fa10de94c64f9565de5335bfa05502fbaac
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-05T05:15:21Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-05T05:15:21Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-05T05:15:21Z'
  support: supports
  summary: Seed generator produces identifier=BTO:0000846, grounding_status=EXACT,
    mapping_status=SEEDED, parent_habitats=["BTO:0000737"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EPREGO
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: TSV rows 565
  accessed_at: '2026-11-05T05:15:21Z'
  support: supports
  summary: '[{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels":
    "annotated_genomes_isolates", "direct_assertion_count": "1", "max_prego_score":
    "3", "ontology": "BTO", "prego_id": "BTO:0000846", "prego_synonyms": "erythroleukemia
    cell line|erythroleukemia cell lines|erythroleukemia cell linous|erythroleukemic
    cell line|erythroleukemic cell lines|erythroleukemic cell linous", "taxon_count":
    "1"}, "row": 565}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: EPREGOTAXA
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV rows 1437
  accessed_at: '2026-11-05T05:15:21Z'
  support: supports
  summary: 1 PREGO taxon-association rows for BTO:0000846.
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 738,847
  accessed_at: '2026-11-05T05:15:21Z'
  support: supports
  summary: '[{"data": {"definition": "", "deprecated": "", "directly_referenced":
    "TRUE", "label": "leukemia cell line", "label_only": "FALSE", "ontology": "BTO",
    "synonyms": "", "term_id": "BTO:0000737"}, "row": 738}, {"data": {"definition":
    "", "deprecated": "", "directly_referenced": "TRUE", "label": "erythroleukemia
    cell line", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id":
    "BTO:0000846"}, "row": 847}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 364,478,482,483,571,674,689,866,1617,1673,1728,2019
  accessed_at: '2026-11-05T05:15:21Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0000846", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000565"}, "row": 364}, {"data": {"object": "BTO:0001035", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000737"}, "row": 478}, {"data": {"object": "BTO:0000737", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0000740"}, "row": 482}, {"data": {"object":
    "BTO:0000737", "predicate": "rdfs:subClassOf", "subject": "BTO:0000741"}, "row":
    483}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000846"}, "row": 571}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0001000"}, "row": 674}, {"data": {"object": "BTO:0000737", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0001018"}, "row": 689}, {"data": {"object":
    "BTO:0000846", "predicate": "rdfs:subClassOf", "subject": "BTO:0001263"}, "row":
    866}, {"data": {"object": "BTO:0000737", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0002332"}, "row": 1617}, {"data": {"object": "BTO:0000737", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0002406"}, "row": 1673}, {"data": {"object":
    "BTO:0000737", "predicate": "rdfs:subClassOf", "subject": "BTO:0002489"}, "row":
    1728}, {"data": {"object": "BTO:0000846", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0002885"}, "row": 2019}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/leukemia_cell_line.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-05T05:15:21Z'
  support: supports
  summary: '{"definition": null, "grounding_status": "EXACT", "identifier": "BTO:0000737",
    "label": "leukemia cell line", "mapping_status": "SEEDED", "parent_habitats":
    ["BTO:0001035"], "source_attestations": [{"assertion_count": 1, "assertion_unit":
    "TAXON", "evidence_channels": "annotated_genomes_isolates", "score": 3.0, "source":
    "PREGO", "source_id": "BTO:0000737", "source_label": "leukemia cell line"}]}'
  snapshot_sha256: 057fba4dea9b812ad80e6731dd80511d0d407081d8ca36b2cf7d11fe70837b9d
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'erythroleukemia_cell_line|BTO:0000846' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-05T05:15:21Z'
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
  - BTO:0000846
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: BTO:0000846 (erythroleukemia cell line) is an exact cell-line habitat identity
    under strictly broader ontology parent BTO:0000737 (leukemia cell line) with 1
    retained PREGO taxon association (noting as source limitations the absence of
    a vendored BTO definition and PREGO stemming variants 'erythroleukemia cell linous'/'erythroleukemic
    cell linous' in RELATED_SYNONYM).
  target_ids:
  - BTO:0000846
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - EP1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "PREGO", "count": 1, "unit": "TAXON"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - BTO:0000846
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - EP1
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce SEEDED / EXACT; this read-only review
    does not mutate generated records.
  target_ids:
  - BTO:0000846
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
