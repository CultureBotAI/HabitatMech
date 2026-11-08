# Record review: Fetus (habitatmech:GOLD.f2a6418a5c)

- Review: 20261108T114924Z-fetus__250e9844-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-08T11:41:00Z
- Finished UTC: 2026-11-08T11:49:24Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The minted GOLD record habitatmech:GOLD.f2a6418a5c (Fetus in Host-associated &gt; Mammals: Human &gt; Fetus, NARROW/SEEDED, no assertion count/unit; total_assertions: 0 in GOLD) retains the life-stage organism term BTO:0000449 (fetus) in parent_habitats via the automatic ambiguous-leaf rule and exhibits the #1398 narrow-match mapping_predicate representation contract defect.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/fetus__250e9844.yaml) at captured main revision 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (fecal__0d8696a2 through fin); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.f2a6418a5c | data/habitats/host_associated/fetus__250e9844.yaml | generated | Fetus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.f2a6418a5c | Completed 2026-11-08T11:48:10Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.f2a6418a5c | Completed 2026-11-08T11:48:35Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.f2a6418a5c | Completed 2026-11-08T11:48:40Z. No issues found; 870 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.f2a6418a5c | Completed 2026-11-08T11:48:42Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.f2a6418a5c | Completed 2026-11-08T11:48:45Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.f2a6418a5c | Completed 2026-11-08T11:48:48Z. validated 93 causal-graph curation file(s) with 93 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.f2a6418a5c | Completed 2026-11-08T11:48:55Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:GOLD.f2a6418a5c | Completed 2026-11-08T11:57:10Z. OK_CANONICAL: 1209, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2088. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.f2a6418a5c.

Individual schema, strict 24-target validation, 870 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 93 causal overlays, and 671 term requests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.f2a6418a5c.

Per the host life-stage rule in docs/CURATION.md (#112/#114/#276), BTO:0000449 (fetus, 'An unborn or unhatched vertebrate...') denotes a whole organism at a developmental stage rather than a strictly broader habitat class for 'Host-associated &gt; Mammals: Human &gt; Fetus' (habitatmech:GOLD.f2a6418a5c), and the record carries mapping_predicate skos:narrowMatch on a minted source-path identifier (#1398).

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.f2a6418a5c.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": 4, "unit": "ORGANISM"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.f2a6418a5c.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / NARROW; this read-only review does not mutate generated records.

## Findings

### F1: Human Fetus asserts life-stage organism term BTO:0000449 (fetus) as a habitat superclass

major / open / confirmed; issue key: fetus--250e9844-life-stage-parent.

Add an ITEM-level CONFIRM_UNGROUNDED row in curation/decisions.tsv for habitatmech:GOLD.f2a6418a5c ('Host-associated &gt; Mammals: Human &gt; Fetus') with object_id=BTO:0000449, object_label=fetus, and relation=xref so the life-stage organism term BTO:0000449 is preserved as a contextual xref rather than a superclass in parent_habitats, retaining broader parent habitatmech:GOLD.cd0b0940e5 (human-associated environment).

### F2: Narrow mapping predicate points to a minted source-path record

major / open / confirmed; issue key: fetus--250e9844-mapping-endpoint-contract.

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.f2a6418a5c (Host-associated &gt; Mammals: Human &gt; Fetus); replacing the automatic ambiguous-leaf narrow match with CONFIRM_UNGROUNDED (relation=xref) on this target also removes its unsupported skos:narrowMatch emission.

## Recommended Actions And Acceptance Checks

### ACT1

Add an ITEM-level CONFIRM_UNGROUNDED row in curation/decisions.tsv for habitatmech:GOLD.f2a6418a5c ('Host-associated &gt; Mammals: Human &gt; Fetus') with object_id=BTO:0000449, object_label=fetus, and relation=xref so the life-stage organism term BTO:0000449 is preserved as a contextual xref rather than a superclass in parent_habitats, retaining broader parent habitatmech:GOLD.cd0b0940e5 (human-associated environment). No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.f2a6418a5c (Host-associated &gt; Mammals: Human &gt; Fetus); replacing the automatic ambiguous-leaf narrow match with CONFIRM_UNGROUNDED (relation=xref) on this target also removes its unsupported skos:narrowMatch emission. No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/fetus__250e9844.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.f2a6418a5c (Fetus) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon and life-stage organism terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.f2a6418a5c, grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["BTO:0000449", "habitatmech:GOLD.cd0b0940e5"]. |
| ESIB1 | data/habitats/host_associated/adult.yaml; Entire YAML | supports | Sibling life-stage host record habitatmech:GOLD.bb7fa12127 (Adult) where life-stage organism term UBERON:0007023 (adult organism) is kept as an xref via CONFIRM_UNGROUNDED (relation=xref) rather than a habitat superclass (#2135). |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 683 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals: Human &gt; Fetus", "depth": "3", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype": "", "ecosystem_type": "Fetus", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:6324&#124;gold.ecosystem:6571&#124;gold.ecosystem:6572", "leaf_label": "Fetus", "organism_count": "4", "specific_ecosystem": "", "study_count": "0", "total_assertions": "4"}, "row": 683}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 450 | supports | [{"data": {"definition": "An unborn or unhatched vertebrate especially after attaining the basic structural plan of its kind; specifically: a developing human from usually three months after conception to birth.", "deprecated": "", "directly_referenced": "FALSE", "label": "fetus", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000449"}, "row": 450}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 291 | supports | [{"data": {"object": "BTO:0000174", "predicate": "rdfs:subClassOf", "subject": "BTO:0000449"}, "row": 291}] |
| EP2 | data/habitats/host_associated/mammals_human.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by a human.", "grounding_status": "UNGROUNDED", "identifier": "habitatmech:GOLD.cd0b0940e5", "label": "human-associated environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000", "ENVO:01001002"], "source_attestations": [{"assertion_count": 11697, "assertion_unit": "STRAIN", "notes": "kg-microbe's isolation-source mapping table has no ontology target for this source; the automatic route leaves it ungrounded. The explicit curator decision SAME_AS overrides that route; this source is emitted on habitatmech:GOLD.cd0b0940e5.", "source": "BACDIVE", "source_id": "bacdive.isolation_source:human", "source_label": "Human"}, {"assertion_count": 40432, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3381", "source_label": "Mammals: Human", "source_path": "Host-associated &gt; Mammals: Human"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'fetus__250e9844&#124;habitatmech:GOLD.f2a6418a5c' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

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
review_id: 20261108T114924Z-fetus__250e9844-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Fetus (habitatmech:GOLD.f2a6418a5c)'
started_at: '2026-11-08T11:41:00Z'
finished_at: '2026-11-08T11:49:24Z'
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
summary: 'The minted GOLD record habitatmech:GOLD.f2a6418a5c (Fetus in Host-associated
  > Mammals: Human > Fetus, NARROW/SEEDED, no assertion count/unit; total_assertions:
  0 in GOLD) retains the life-stage organism term BTO:0000449 (fetus) in parent_habitats
  via the automatic ambiguous-leaf rule and exhibits the #1398 narrow-match mapping_predicate
  representation contract defect.'
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
  - path: data/habitats/host_associated/adult.yaml
    sha256: 91c41fc8a4d72c43682756d0e29562fbf92e27e198d386fc5847a6c8961e4e04
    role: context
  - path: data/habitats/host_associated/fetus__250e9844.yaml
    sha256: 1de36aaf5d6ba77a218d90b8733c18252b8935c2bf9a855c1bd24c8890d7a60d
    role: target
  - path: data/habitats/host_associated/mammals_human.yaml
    sha256: 6d3fba8ddf0a933b0e22f94b17e2df356eb2d297b1d96a7f960575e81d50d4d1
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
- target_id: habitatmech:GOLD.f2a6418a5c
  path: data/habitats/host_associated/fetus__250e9844.yaml
  label: Fetus
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/fetus__250e9844.yaml)
    at captured main revision 6a699ab5f6f775ca0c18be7a12d7af2e2645f31e.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (fecal__0d8696a2 through fin); this bundle assesses its single resolved
    identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.f2a6418a5c
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
    --target-class HabitatRecord data/habitats/host_associated/fetus__250e9844.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.f2a6418a5c
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
  - habitatmech:GOLD.f2a6418a5c
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
  - habitatmech:GOLD.f2a6418a5c
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
  - habitatmech:GOLD.f2a6418a5c
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
  - habitatmech:GOLD.f2a6418a5c
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
  - habitatmech:GOLD.f2a6418a5c
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
  - habitatmech:GOLD.f2a6418a5c
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
  - habitatmech:GOLD.f2a6418a5c
  summary: 'Completed 2026-11-08T11:57:10Z. OK_CANONICAL: 1209, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2088. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/fetus__250e9844.yaml
  locator: Entire YAML
  accessed_at: '2026-11-08T11:49:24Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.f2a6418a5c (Fetus) were read.
  snapshot_sha256: 1de36aaf5d6ba77a218d90b8733c18252b8935c2bf9a855c1bd24c8890d7a60d
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-08T11:49:24Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon and life-stage
    organism terms cannot substitute for associated environments; parent_habitats
    must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-08T11:49:24Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-08T11:49:24Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.f2a6418a5c, grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["BTO:0000449", "habitatmech:GOLD.cd0b0940e5"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/adult.yaml
  locator: Entire YAML
  accessed_at: '2026-11-08T11:49:24Z'
  support: supports
  summary: Sibling life-stage host record habitatmech:GOLD.bb7fa12127 (Adult) where
    life-stage organism term UBERON:0007023 (adult organism) is kept as an xref via
    CONFIRM_UNGROUNDED (relation=xref) rather than a habitat superclass (#2135).
  snapshot_sha256: 91c41fc8a4d72c43682756d0e29562fbf92e27e198d386fc5847a6c8961e4e04
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 683
  accessed_at: '2026-11-08T11:49:24Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals: Human > Fetus", "depth": "3", "ecosystem": "Host-associated", "ecosystem_category":
    "Mammals: Human", "ecosystem_subtype": "", "ecosystem_type": "Fetus", "gold_node_count":
    "3", "gold_node_ids": "gold.ecosystem:6324|gold.ecosystem:6571|gold.ecosystem:6572",
    "leaf_label": "Fetus", "organism_count": "4", "specific_ecosystem": "", "study_count":
    "0", "total_assertions": "4"}, "row": 683}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 450
  accessed_at: '2026-11-08T11:49:24Z'
  support: supports
  summary: '[{"data": {"definition": "An unborn or unhatched vertebrate especially
    after attaining the basic structural plan of its kind; specifically: a developing
    human from usually three months after conception to birth.", "deprecated": "",
    "directly_referenced": "FALSE", "label": "fetus", "label_only": "FALSE", "ontology":
    "BTO", "synonyms": "", "term_id": "BTO:0000449"}, "row": 450}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 291
  accessed_at: '2026-11-08T11:49:24Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0000174", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000449"}, "row": 291}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/mammals_human.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-08T11:49:24Z'
  support: supports
  summary: '{"definition": "An environmental system determined by a human.", "grounding_status":
    "UNGROUNDED", "identifier": "habitatmech:GOLD.cd0b0940e5", "label": "human-associated
    environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000",
    "ENVO:01001002"], "source_attestations": [{"assertion_count": 11697, "assertion_unit":
    "STRAIN", "notes": "kg-microbe''s isolation-source mapping table has no ontology
    target for this source; the automatic route leaves it ungrounded. The explicit
    curator decision SAME_AS overrides that route; this source is emitted on habitatmech:GOLD.cd0b0940e5.",
    "source": "BACDIVE", "source_id": "bacdive.isolation_source:human", "source_label":
    "Human"}, {"assertion_count": 40432, "assertion_unit": "ORGANISM", "notes": "4
    GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3381", "source_label": "Mammals:
    Human", "source_path": "Host-associated > Mammals: Human"}]}'
  snapshot_sha256: 6d3fba8ddf0a933b0e22f94b17e2df356eb2d297b1d96a7f960575e81d50d4d1
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'fetus__250e9844|habitatmech:GOLD.f2a6418a5c' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-08T11:49:24Z'
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
  - habitatmech:GOLD.f2a6418a5c
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: 'Per the host life-stage rule in docs/CURATION.md (#112/#114/#276), BTO:0000449
    (fetus, ''An unborn or unhatched vertebrate...'') denotes a whole organism at
    a developmental stage rather than a strictly broader habitat class for ''Host-associated
    > Mammals: Human > Fetus'' (habitatmech:GOLD.f2a6418a5c), and the record carries
    mapping_predicate skos:narrowMatch on a minted source-path identifier (#1398).'
  target_ids:
  - habitatmech:GOLD.f2a6418a5c
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": 4, "unit": "ORGANISM"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.f2a6418a5c
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce SEEDED / NARROW; this read-only review
    does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.f2a6418a5c
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: fetus--250e9844-life-stage-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Human Fetus asserts life-stage organism term BTO:0000449 (fetus) as a habitat
    superclass
  description: 'Add an ITEM-level CONFIRM_UNGROUNDED row in curation/decisions.tsv
    for habitatmech:GOLD.f2a6418a5c (''Host-associated > Mammals: Human > Fetus'')
    with object_id=BTO:0000449, object_label=fetus, and relation=xref so the life-stage
    organism term BTO:0000449 is preserved as a contextual xref rather than a superclass
    in parent_habitats, retaining broader parent habitatmech:GOLD.cd0b0940e5 (human-associated
    environment).'
  target_ids:
  - habitatmech:GOLD.f2a6418a5c
  field_paths:
  - grounding_status
  - mapping_status
  - parent_habitats
  - xrefs
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: fetus--250e9844-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping predicate points to a minted source-path record
  description: 'Reconcile narrow-match source-attestation output with the endpoint
    contract tracked in Issue #1398 for habitatmech:GOLD.f2a6418a5c (Host-associated
    > Mammals: Human > Fetus); replacing the automatic ambiguous-leaf narrow match
    with CONFIRM_UNGROUNDED (relation=xref) on this target also removes its unsupported
    skos:narrowMatch emission.'
  target_ids:
  - habitatmech:GOLD.f2a6418a5c
  field_paths:
  - identifier
  - grounding_status
  - parent_habitats
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: docs/CURATION.md
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.f2a6418a5c
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Add an ITEM-level CONFIRM_UNGROUNDED row in curation/decisions.tsv
    for habitatmech:GOLD.f2a6418a5c (''Host-associated > Mammals: Human > Fetus'')
    with object_id=BTO:0000449, object_label=fetus, and relation=xref so the life-stage
    organism term BTO:0000449 is preserved as a contextual xref rather than a superclass
    in parent_habitats, retaining broader parent habitatmech:GOLD.cd0b0940e5 (human-associated
    environment). No repair is performed by this read-only review.'
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
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.f2a6418a5c
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: docs/CURATION.md
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Reconcile narrow-match source-attestation output with the endpoint
    contract tracked in Issue #1398 for habitatmech:GOLD.f2a6418a5c (Host-associated
    > Mammals: Human > Fetus); replacing the automatic ambiguous-leaf narrow match
    with CONFIRM_UNGROUNDED (relation=xref) on this target also removes its unsupported
    skos:narrowMatch emission. No repair is performed by this read-only review.'
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
