# Record review: gastric epithelium (BTO:0000500)

- Review: 20261111T060532Z-gastric_epithelium-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-11T05:35:00Z
- Finished UTC: 2026-11-11T06:05:32Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The PREGO-attested record BTO:0000500 (gastric epithelium, EXACT/SEEDED, 2 TAXON assertions for Helicobacter pylori) is coherently grounded to BRENDA Tissue Ontology term BTO:0000500 ('Epithelium of the stomach.') under strictly broader BTO:0000416 (epithelium).

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/gastric_epithelium.yaml) at captured main revision 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (frontal_sinus through gastric_epithelium_cell_line); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000500 | data/habitats/host_associated/gastric_epithelium.yaml | generated | gastric epithelium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000500 | Completed 2026-11-11T05:58:54Z. No issues found. |
| validate-strict | passed | True | BTO:0000500 | Completed 2026-11-11T05:59:01Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | BTO:0000500 | Completed 2026-11-11T05:59:08Z. No issues found; 881 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | BTO:0000500 | Completed 2026-11-11T05:59:09Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | BTO:0000500 | Completed 2026-11-11T05:59:26Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | BTO:0000500 | Completed 2026-11-11T05:59:32Z. validated 113 causal-graph curation file(s) with 113 graph(s). |
| term-requests-check | passed | True | BTO:0000500 | Completed 2026-11-11T05:59:47Z. term-request table is current (676 terms). |
| validate-products | passed | True | BTO:0000500 | Completed 2026-11-11T06:00:30Z. OK_CANONICAL: 1211, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2106. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: BTO:0000500.

Individual schema, strict 24-target validation, 881 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 113 causal overlays, and 676 term requests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: BTO:0000500.

The PREGO-attested record BTO:0000500 (gastric epithelium, EXACT/SEEDED, 2 TAXON assertions for Helicobacter pylori) is coherently grounded to BRENDA Tissue Ontology term BTO:0000500 ('Epithelium of the stomach.') under strictly broader BTO:0000416 (epithelium).

### Source counts and retained ranking

quantity: supported. Targets: BTO:0000500.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 2, "source": "PREGO", "unit": "TAXON"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: BTO:0000500.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / EXACT; this read-only review does not mutate generated records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/gastric_epithelium.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for BTO:0000500 (gastric epithelium) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and disease-classification terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=BTO:0000500, grounding_status=EXACT, mapping_status=SEEDED, parent_habitats=["BTO:0000416"]. |
| EPREGO | data/raw/prego_habitats.tsv; TSV rows 474 | supports | [{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "2", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0000500", "prego_synonyms": "gastric epithelia&#124;gastric epithelial&#124;gastric epithelium&#124;gastric epitheliums&#124;stomach epithelia&#124;stomach epithelial&#124;stomach epithelium&#124;stomach epitheliums", "taxon_count": "2"}, "row": 474}] |
| EPREGOTAXA | data/raw/prego_habitat_taxa.tsv; TSV rows 690,691 | supports | 2 PREGO taxon-association rows for BTO:0000500. |
| EONT | data/raw/ontology_terms.tsv; TSV rows 418,501 | supports | [{"data": {"definition": "A membranous cellular tissue that covers a free surface or lines a tube or cavity of an animal body and serves especially to enclose and protect the other parts of the body, to produce secretions and excretions, and to function in assimilation.", "deprecated": "", "directly_referenced": "TRUE", "label": "epithelium", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000416"}, "row": 418}, {"data": {"definition": "Epithelium of the stomach.", "deprecated": "", "directly_referenced": "TRUE", "label": "gastric epithelium", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000500"}, "row": 501}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 50,165,212,258,263,272,274,275,328,515,639,668,796,807,980 | supports | [{"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000059"}, "row": 50}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000241"}, "row": 165}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000314"}, "row": 212}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000393"}, "row": 258}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000401"}, "row": 263}, {"data": {"object": "BTO:0000634", "predicate": "rdfs:subClassOf", "subject": "BTO:0000416"}, "row": 272}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000419"}, "row": 274}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000422"}, "row": 275}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000500"}, "row": 328}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000781"}, "row": 515}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000956"}, "row": 639}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000992"}, "row": 668}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0001177"}, "row": 796}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0001195"}, "row": 807}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0001428"}, "row": 980}] |
| EP1 | data/habitats/host_associated/epithelium.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "A membranous cellular tissue that covers a free surface or lines a tube or cavity of an animal body and serves especially to enclose and protect the other parts of the body, to produce secretions and excretions, and to function in assimilation.", "grounding_status": "EXACT", "identifier": "BTO:0000416", "label": "epithelium", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0000634"], "source_attestations": [{"assertion_count": 35, "assertion_unit": "TAXON", "evidence_channels": "annotated_genomes_isolates", "score": 3.0, "source": "PREGO", "source_id": "BTO:0000416", "source_label": "epithelium"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'gastric_epithelium&#124;BTO:0000500' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

## Limits And Additional Notes

- Only the cited repository inputs, ontology terms, and source inventories were inspected; original specimen-level support for every upstream source assertion was not exhaustively reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,106 no-adapter pairs; this is not whole-corpus identifier certification.
- Read-only review: no curation table, generated habitat YAML, status, or history record was modified.
- All target and context inputs were captured at clean git commit 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
- Structured-review archive traversal confirmed no prior target review bundle exists for this record.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261111T060532Z-gastric_epithelium-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: gastric epithelium (BTO:0000500)'
started_at: '2026-11-11T05:35:00Z'
finished_at: '2026-11-11T06:05:32Z'
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
summary: The PREGO-attested record BTO:0000500 (gastric epithelium, EXACT/SEEDED,
  2 TAXON assertions for Helicobacter pylori) is coherently grounded to BRENDA Tissue
  Ontology term BTO:0000500 ('Epithelium of the stomach.') under strictly broader
  BTO:0000416 (epithelium).
source:
  git_revision: 83aa5f212521389cb9c3507ded58d0bcd0a22ee0
  state: git_commit
  inputs:
  - path: curation/decisions.tsv
    sha256: 8e0c9ea50c453b9b0eb86e9a6cf246dbc188714ec7a8cc37b2918d5373e6d2ae
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 84e5214713a21033312eb9c512fe38f44865662f934a4e679d45e827b16ff780
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 21c90040f7616f5ecc103716597d65b899f433eee24e880ac3f2fd802ff624c6
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: 3703ae74d7565abdfb5a1fab47718b05c4fd02447b4ed60bbeb3bde65e1d8792
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: 779e0cf7e829e3ec74b5a898b6ed70d54d930b7da726c1611225902c00915388
    role: context
  - path: data/habitats/host_associated/epithelium.yaml
    sha256: 3842bb5461603ad2188db6eec103fd1bee09a08bb5ace94e45c4022434e2d68b
    role: context
  - path: data/habitats/host_associated/gastric_epithelium.yaml
    sha256: f15265925866e67517bc6ab20c308e4b75988683e58e910a0fc9f75ea224821c
    role: target
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/environment_parameters.tsv
    sha256: a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
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
- target_id: BTO:0000500
  path: data/habitats/host_associated/gastric_epithelium.yaml
  label: gastric epithelium
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/gastric_epithelium.yaml)
    at captured main revision 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (frontal_sinus through gastric_epithelium_cell_line); this bundle assesses
    its single resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000500
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
    --target-class HabitatRecord data/habitats/host_associated/gastric_epithelium.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000500
  summary: Completed 2026-11-11T05:58:54Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/frontal_sinus.yaml
    data/habitats/host_associated/frozen_remains.yaml data/habitats/host_associated/frozen_remains__584db35c.yaml
    data/habitats/host_associated/frozen_remains__aa25d597.yaml data/habitats/host_associated/fruit.yaml
    data/habitats/host_associated/fruit_juice.yaml data/habitats/host_associated/fruiting_body.yaml
    data/habitats/host_associated/fungi.yaml data/habitats/host_associated/fungi_associated_environment.yaml
    data/habitats/host_associated/g_cell.yaml data/habitats/host_associated/gall_bladder.yaml
    data/habitats/host_associated/gallbladder.yaml data/habitats/host_associated/gallbladder__d157697c.yaml
    data/habitats/host_associated/gallbladder_stones.yaml data/habitats/host_associated/gallbladder_stones__a31ee838.yaml
    data/habitats/host_associated/galls.yaml data/habitats/host_associated/gametophyte.yaml
    data/habitats/host_associated/ganglion.yaml data/habitats/host_associated/gaster.yaml
    data/habitats/host_associated/gastric_caeca.yaml data/habitats/host_associated/gastric_caeca__12108999.yaml
    data/habitats/host_associated/gastric_carcinoma.yaml data/habitats/host_associated/gastric_epithelium.yaml
    data/habitats/host_associated/gastric_epithelium_cell_line.yaml --out .temp/c9s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000500
  summary: 'Completed 2026-11-11T05:59:01Z. Validated 24 files; files with ERROR:
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
  - BTO:0000500
  summary: Completed 2026-11-11T05:59:08Z. No issues found; 881 history record(s)
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
  - BTO:0000500
  summary: 'Completed 2026-11-11T05:59:09Z. provenance current: 14 committed inventories,
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
  - BTO:0000500
  summary: 'Completed 2026-11-11T05:59:26Z. expected 3209 records, found 3209 on disk;
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
  - BTO:0000500
  summary: Completed 2026-11-11T05:59:32Z. validated 113 causal-graph curation file(s)
    with 113 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000500
  summary: Completed 2026-11-11T05:59:47Z. term-request table is current (676 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - BTO:0000500
  summary: 'Completed 2026-11-11T06:00:30Z. OK_CANONICAL: 1211, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2106. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/gastric_epithelium.yaml
  locator: Entire YAML
  accessed_at: '2026-11-11T06:05:32Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for BTO:0000500 (gastric epithelium) were read.
  snapshot_sha256: f15265925866e67517bc6ab20c308e4b75988683e58e910a0fc9f75ea224821c
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-11T06:05:32Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and disease-classification terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-11T06:05:32Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-11T06:05:32Z'
  support: supports
  summary: Seed generator produces identifier=BTO:0000500, grounding_status=EXACT,
    mapping_status=SEEDED, parent_habitats=["BTO:0000416"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EPREGO
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: TSV rows 474
  accessed_at: '2026-11-11T06:05:32Z'
  support: supports
  summary: '[{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels":
    "annotated_genomes_isolates", "direct_assertion_count": "2", "max_prego_score":
    "3", "ontology": "BTO", "prego_id": "BTO:0000500", "prego_synonyms": "gastric
    epithelia|gastric epithelial|gastric epithelium|gastric epitheliums|stomach epithelia|stomach
    epithelial|stomach epithelium|stomach epitheliums", "taxon_count": "2"}, "row":
    474}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: EPREGOTAXA
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV rows 690,691
  accessed_at: '2026-11-11T06:05:32Z'
  support: supports
  summary: 2 PREGO taxon-association rows for BTO:0000500.
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 418,501
  accessed_at: '2026-11-11T06:05:32Z'
  support: supports
  summary: '[{"data": {"definition": "A membranous cellular tissue that covers a free
    surface or lines a tube or cavity of an animal body and serves especially to enclose
    and protect the other parts of the body, to produce secretions and excretions,
    and to function in assimilation.", "deprecated": "", "directly_referenced": "TRUE",
    "label": "epithelium", "label_only": "FALSE", "ontology": "BTO", "synonyms": "",
    "term_id": "BTO:0000416"}, "row": 418}, {"data": {"definition": "Epithelium of
    the stomach.", "deprecated": "", "directly_referenced": "TRUE", "label": "gastric
    epithelium", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id":
    "BTO:0000500"}, "row": 501}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 50,165,212,258,263,272,274,275,328,515,639,668,796,807,980
  accessed_at: '2026-11-11T06:05:32Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000059"}, "row": 50}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000241"}, "row": 165}, {"data": {"object": "BTO:0000416", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0000314"}, "row": 212}, {"data": {"object":
    "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000393"}, "row":
    258}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000401"}, "row": 263}, {"data": {"object": "BTO:0000634", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000416"}, "row": 272}, {"data": {"object": "BTO:0000416", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0000419"}, "row": 274}, {"data": {"object":
    "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000422"}, "row":
    275}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000500"}, "row": 328}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000781"}, "row": 515}, {"data": {"object": "BTO:0000416", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0000956"}, "row": 639}, {"data": {"object":
    "BTO:0000416", "predicate": "rdfs:subClassOf", "subject": "BTO:0000992"}, "row":
    668}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0001177"}, "row": 796}, {"data": {"object": "BTO:0000416", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0001195"}, "row": 807}, {"data": {"object": "BTO:0000416", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0001428"}, "row": 980}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/epithelium.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-11T06:05:32Z'
  support: supports
  summary: '{"definition": "A membranous cellular tissue that covers a free surface
    or lines a tube or cavity of an animal body and serves especially to enclose and
    protect the other parts of the body, to produce secretions and excretions, and
    to function in assimilation.", "grounding_status": "EXACT", "identifier": "BTO:0000416",
    "label": "epithelium", "mapping_status": "SEEDED", "parent_habitats": ["BTO:0000634"],
    "source_attestations": [{"assertion_count": 35, "assertion_unit": "TAXON", "evidence_channels":
    "annotated_genomes_isolates", "score": 3.0, "source": "PREGO", "source_id": "BTO:0000416",
    "source_label": "epithelium"}]}'
  snapshot_sha256: 3842bb5461603ad2188db6eec103fd1bee09a08bb5ace94e45c4022434e2d68b
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'gastric_epithelium|BTO:0000500' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-11T06:05:32Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, strict 24-target validation, 881 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 113 causal
    overlays, and 676 term requests passed.
  target_ids:
  - BTO:0000500
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: The PREGO-attested record BTO:0000500 (gastric epithelium, EXACT/SEEDED,
    2 TAXON assertions for Helicobacter pylori) is coherently grounded to BRENDA Tissue
    Ontology term BTO:0000500 ('Epithelium of the stomach.') under strictly broader
    BTO:0000416 (epithelium).
  target_ids:
  - BTO:0000500
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
    and pools: [{"count": 2, "source": "PREGO", "unit": "TAXON"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - BTO:0000500
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
  - BTO:0000500
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
- Configured label correspondence skipped 2,106 no-adapter pairs; this is not whole-corpus
  identifier certification.
- 'Read-only review: no curation table, generated habitat YAML, status, or history
  record was modified.'
notes:
- All target and context inputs were captured at clean git commit 83aa5f212521389cb9c3507ded58d0bcd0a22ee0.
- Structured-review archive traversal confirmed no prior target review bundle exists
  for this record.
tags:
- individual-scientific-review
- host-associated
```
