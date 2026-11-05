# Record review: Esophagus (habitatmech:GOLD.974cd3759a)

- Review: 20261105T051527Z-esophagus__e0ae9e65-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-05T04:39:00Z
- Finished UTC: 2026-11-05T05:15:27Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The minted GOLD record habitatmech:GOLD.974cd3759a (Esophagus in Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Esophagus, NARROW/SEEDED, no assertion count/unit; total_assertions: 0 in GOLD) retains whole-organ-system human Digestive system parent habitatmech:GOLD.f6720bccf0 as a superclass and exhibits the #1398 narrow-match mapping_predicate representation contract defect.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/esophagus__e0ae9e65.yaml) at captured main revision 215b23c90244e634e64f88fa2c1a2a3bb011880a.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (epicuticular_wax through excretory_system); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 215b23c90244e634e64f88fa2c1a2a3bb011880a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.974cd3759a | data/habitats/host_associated/esophagus__e0ae9e65.yaml | generated | Esophagus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.974cd3759a | Completed 2026-11-05T04:42:18Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.974cd3759a | Completed 2026-11-05T04:55:15Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.974cd3759a | Completed 2026-11-05T04:40:17Z. No issues found; 862 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.974cd3759a | Completed 2026-11-05T04:40:25Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.974cd3759a | Completed 2026-11-05T04:41:11Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.974cd3759a | Completed 2026-11-05T04:40:29Z. validated 73 causal-graph curation file(s) with 73 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.974cd3759a | Completed 2026-11-05T04:41:21Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:GOLD.974cd3759a | Completed 2026-11-05T04:43:01Z. OK_CANONICAL: 1200, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2077. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.974cd3759a.

Individual schema, strict 24-target validation, 862 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 73 causal overlays, and 671 term requests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.974cd3759a.

The esophagus (UBERON:0001043) is an anatomical organ (part_of) of the digestive system rather than a subtype (is_a) of the human Digestive system (habitatmech:GOLD.f6720bccf0), and the record carries mapping_predicate skos:narrowMatch while its emitted identifier is the minted source concept (#1398).

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.974cd3759a.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.974cd3759a.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce SEEDED / NARROW; this read-only review does not mutate generated records.

## Findings

### F1: Human Esophagus retains human Digestive system GOLD parent as a superclass

major / open / confirmed; issue key: esophagus--e0ae9e65-context-parent.

Add an exclusion row in curation/gold_parent_exclusions.tsv for source identifier habitatmech:GOLD.974cd3759a on GOLD path 'Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Esophagus' (exact target habitatmech:GOLD.974cd3759a) excluding parent_id habitatmech:GOLD.f6720bccf0 (Digestive system), preserving broader ontology parent UBERON:0001043 (esophagus).

### F2: Narrow mapping predicate points to a minted source-path record

major / open / confirmed; issue key: esophagus--e0ae9e65-mapping-endpoint-contract.

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.974cd3759a (Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Esophagus) and its broader ontology parent UBERON:0001043 (esophagus).

## Recommended Actions And Acceptance Checks

### ACT1

Add an exclusion row in curation/gold_parent_exclusions.tsv for source identifier habitatmech:GOLD.974cd3759a on GOLD path 'Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Esophagus' (exact target habitatmech:GOLD.974cd3759a) excluding parent_id habitatmech:GOLD.f6720bccf0 (Digestive system), preserving broader ontology parent UBERON:0001043 (esophagus). No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Reconcile narrow-match source-attestation output with the endpoint contract tracked in Issue #1398 for habitatmech:GOLD.974cd3759a (Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Esophagus) and its broader ontology parent UBERON:0001043 (esophagus). No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/esophagus__e0ae9e65.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.974cd3759a (Esophagus) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.974cd3759a, grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:0001043", "habitatmech:GOLD.f6720bccf0"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 2210 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Esophagus", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype": "Esophagus", "ecosystem_type": "Digestive system", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:6430&#124;gold.ecosystem:6431", "leaf_label": "Esophagus", "organism_count": "0", "specific_ecosystem": "", "study_count": "0", "total_assertions": "0"}, "row": 2210}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 12994 | supports | [{"data": {"definition": "Tube that connects the pharynx to the stomach. In mammals, the oesophagus connects the buccal cavity with the stomach. The stratified squamous non-keratinised epithelium lining the buccal cavity is continued through the pharynx down into the oesophagus. The lowest part of the oesophagus (ca. 2 cm) is lined with gastric mucosa and covered by peritoneum. The main body of the oesophagus is lined with small, simple mucous glands. Each gland opens into the lumen by a long duct which pierces the muscularis mucosae (Wilson and Washington, 1989). A sphincter is situated at the point where the oesophagus enters the stomach to prevent gastro-oesophageal reflux, i.e. to prevent acidic gastric contents from reaching stratified epithelia of the oesophagus, where they can cause inflammation and irritation (Wilson and Washington, 1989; Brown et al., 1993).", "deprecated": "", "directly_referenced": "FALSE", "label": "esophagus", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "gullet&#124;oesophagus", "term_id": "UBERON:0001043"}, "row": 12994}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 11145,11146,11147 | supports | [{"data": {"object": "UBERON:0000062", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001043"}, "row": 11145}, {"data": {"object": "UBERON:0004921", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001043"}, "row": 11146}, {"data": {"object": "UBERON:0013765", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001043"}, "row": 11147}] |
| EP2 | data/habitats/host_associated/digestive_system__87922027.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.f6720bccf0", "label": "Digestive system", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001007", "habitatmech:GOLD.cd0b0940e5"], "source_attestations": [{"assertion_count": 1443, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3587", "source_label": "Digestive system", "source_path": "Host-associated &gt; Mammals: Human &gt; Digestive system"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'esophagus__e0ae9e65&#124;habitatmech:GOLD.974cd3759a' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

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
review_id: 20261105T051527Z-esophagus__e0ae9e65-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Esophagus (habitatmech:GOLD.974cd3759a)'
started_at: '2026-11-05T04:39:00Z'
finished_at: '2026-11-05T05:15:27Z'
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
summary: 'The minted GOLD record habitatmech:GOLD.974cd3759a (Esophagus in Host-associated
  > Mammals: Human > Digestive system > Esophagus, NARROW/SEEDED, no assertion count/unit;
  total_assertions: 0 in GOLD) retains whole-organ-system human Digestive system parent
  habitatmech:GOLD.f6720bccf0 as a superclass and exhibits the #1398 narrow-match
  mapping_predicate representation contract defect.'
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
  - path: data/habitats/host_associated/digestive_system__87922027.yaml
    sha256: 3a11b162810bbb236e30ec4b17e5058dabf38c48ac3ba6336e922a6f9cd43335
    role: context
  - path: data/habitats/host_associated/esophagus__e0ae9e65.yaml
    sha256: 24c500b5e56d3fd95daed34ddbc6edc578b130d36f0f076776e0b64e4d626118
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
- target_id: habitatmech:GOLD.974cd3759a
  path: data/habitats/host_associated/esophagus__e0ae9e65.yaml
  label: Esophagus
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/esophagus__e0ae9e65.yaml)
    at captured main revision 215b23c90244e634e64f88fa2c1a2a3bb011880a.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (epicuticular_wax through excretory_system); this bundle assesses its
    single resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.974cd3759a
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
    --target-class HabitatRecord data/habitats/host_associated/esophagus__e0ae9e65.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.974cd3759a
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
  - habitatmech:GOLD.974cd3759a
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
  - habitatmech:GOLD.974cd3759a
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
  - habitatmech:GOLD.974cd3759a
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
  - habitatmech:GOLD.974cd3759a
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
  - habitatmech:GOLD.974cd3759a
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
  - habitatmech:GOLD.974cd3759a
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
  - habitatmech:GOLD.974cd3759a
  summary: 'Completed 2026-11-05T04:43:01Z. OK_CANONICAL: 1200, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2077. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/esophagus__e0ae9e65.yaml
  locator: Entire YAML
  accessed_at: '2026-11-05T05:15:27Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.974cd3759a (Esophagus) were read.
  snapshot_sha256: 24c500b5e56d3fd95daed34ddbc6edc578b130d36f0f076776e0b64e4d626118
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-05T05:15:27Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-05T05:15:27Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-05T05:15:27Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.974cd3759a, grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:0001043", "habitatmech:GOLD.f6720bccf0"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2210
  accessed_at: '2026-11-05T05:15:27Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals: Human > Digestive system > Esophagus", "depth": "4", "ecosystem": "Host-associated",
    "ecosystem_category": "Mammals: Human", "ecosystem_subtype": "Esophagus", "ecosystem_type":
    "Digestive system", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:6430|gold.ecosystem:6431",
    "leaf_label": "Esophagus", "organism_count": "0", "specific_ecosystem": "", "study_count":
    "0", "total_assertions": "0"}, "row": 2210}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 12994
  accessed_at: '2026-11-05T05:15:27Z'
  support: supports
  summary: '[{"data": {"definition": "Tube that connects the pharynx to the stomach.
    In mammals, the oesophagus connects the buccal cavity with the stomach. The stratified
    squamous non-keratinised epithelium lining the buccal cavity is continued through
    the pharynx down into the oesophagus. The lowest part of the oesophagus (ca. 2
    cm) is lined with gastric mucosa and covered by peritoneum. The main body of the
    oesophagus is lined with small, simple mucous glands. Each gland opens into the
    lumen by a long duct which pierces the muscularis mucosae (Wilson and Washington,
    1989). A sphincter is situated at the point where the oesophagus enters the stomach
    to prevent gastro-oesophageal reflux, i.e. to prevent acidic gastric contents
    from reaching stratified epithelia of the oesophagus, where they can cause inflammation
    and irritation (Wilson and Washington, 1989; Brown et al., 1993).", "deprecated":
    "", "directly_referenced": "FALSE", "label": "esophagus", "label_only": "FALSE",
    "ontology": "UBERON", "synonyms": "gullet|oesophagus", "term_id": "UBERON:0001043"},
    "row": 12994}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 11145,11146,11147
  accessed_at: '2026-11-05T05:15:27Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0000062", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0001043"}, "row": 11145}, {"data": {"object": "UBERON:0004921",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0001043"}, "row": 11146}, {"data":
    {"object": "UBERON:0013765", "predicate": "rdfs:subClassOf", "subject": "UBERON:0001043"},
    "row": 11147}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/digestive_system__87922027.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-05T05:15:27Z'
  support: supports
  summary: '{"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.f6720bccf0",
    "label": "Digestive system", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001007",
    "habitatmech:GOLD.cd0b0940e5"], "source_attestations": [{"assertion_count": 1443,
    "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes":
    "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3587", "source_label": "Digestive
    system", "source_path": "Host-associated > Mammals: Human > Digestive system"}]}'
  snapshot_sha256: 3a11b162810bbb236e30ec4b17e5058dabf38c48ac3ba6336e922a6f9cd43335
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'esophagus__e0ae9e65|habitatmech:GOLD.974cd3759a' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-05T05:15:27Z'
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
  - habitatmech:GOLD.974cd3759a
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: The esophagus (UBERON:0001043) is an anatomical organ (part_of) of the
    digestive system rather than a subtype (is_a) of the human Digestive system (habitatmech:GOLD.f6720bccf0),
    and the record carries mapping_predicate skos:narrowMatch while its emitted identifier
    is the minted source concept (#1398).
  target_ids:
  - habitatmech:GOLD.974cd3759a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.974cd3759a
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
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
  - habitatmech:GOLD.974cd3759a
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: esophagus--e0ae9e65-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Human Esophagus retains human Digestive system GOLD parent as a superclass
  description: 'Add an exclusion row in curation/gold_parent_exclusions.tsv for source
    identifier habitatmech:GOLD.974cd3759a on GOLD path ''Host-associated > Mammals:
    Human > Digestive system > Esophagus'' (exact target habitatmech:GOLD.974cd3759a)
    excluding parent_id habitatmech:GOLD.f6720bccf0 (Digestive system), preserving
    broader ontology parent UBERON:0001043 (esophagus).'
  target_ids:
  - habitatmech:GOLD.974cd3759a
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: esophagus--e0ae9e65-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping predicate points to a minted source-path record
  description: 'Reconcile narrow-match source-attestation output with the endpoint
    contract tracked in Issue #1398 for habitatmech:GOLD.974cd3759a (Host-associated
    > Mammals: Human > Digestive system > Esophagus) and its broader ontology parent
    UBERON:0001043 (esophagus).'
  target_ids:
  - habitatmech:GOLD.974cd3759a
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
  - EGOLD
  - EONT
  - EONTEDGE
  - EP2
  owner_paths:
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
  - habitatmech:GOLD.974cd3759a
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Add an exclusion row in curation/gold_parent_exclusions.tsv for source
    identifier habitatmech:GOLD.974cd3759a on GOLD path ''Host-associated > Mammals:
    Human > Digestive system > Esophagus'' (exact target habitatmech:GOLD.974cd3759a)
    excluding parent_id habitatmech:GOLD.f6720bccf0 (Digestive system), preserving
    broader ontology parent UBERON:0001043 (esophagus). No repair is performed by
    this read-only review.'
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
  - habitatmech:GOLD.974cd3759a
  owner_paths:
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
    contract tracked in Issue #1398 for habitatmech:GOLD.974cd3759a (Host-associated
    > Mammals: Human > Digestive system > Esophagus) and its broader ontology parent
    UBERON:0001043 (esophagus). No repair is performed by this read-only review.'
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
