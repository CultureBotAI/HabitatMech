# Record review: mammalian pleural empyema exudate (habitatmech:GOLD.818c9729e2)

- Review: 20261026T083033Z-empyema-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-26T08:24:00Z
- Finished UTC: 2026-10-26T08:30:33Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The minted GOLD record habitatmech:GOLD.818c9729e2 (mammalian pleural empyema exudate in Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema, UNGROUNDED/REVIEWED, no assertion count/unit; total_assertions: 0 in GOLD) defines a purulent pleural exudate, but places it as a subclass (is_a) of the anatomical cavity UBERON:0002402 (pleural cavity), and asserts the bare clinical condition name 'Empyema' as an EXACT_SYNONYM.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/empyema.yaml) at captured main revision 1a40d0958114e6e3facd148ccec6197fa4dd679c.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (ear_discharge through empyema); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 1a40d0958114e6e3facd148ccec6197fa4dd679c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.818c9729e2 | data/habitats/host_associated/empyema.yaml | generated | mammalian pleural empyema exudate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:25:36Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:25:42Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:25:48Z. No issues found; 852 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:25:49Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:26:03Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:26:07Z. validated 53 causal-graph curation file(s) with 53 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:26:21Z. term-request table is current (661 terms). |
| validate-products | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:27:01Z. OK_CANONICAL: 1194, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2063. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.818c9729e2.

Individual schema, strict 24-target validation, 852 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 53 causal overlays, and 661 term requests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.818c9729e2.

A purulent pleural exudate (mammalian pleural empyema exudate) is an infected bodily fluid / pleural effusion accumulated within the pleural space rather than a subtype (is_a) of the anatomical pleural cavity (UBERON:0002402), and bare 'Empyema' is a clinical condition name rather than an exact synonym of mammalian pleural empyema exudate.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.818c9729e2.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.818c9729e2.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Mammalian pleural empyema exudate is placed as a subclass of anatomical pleural cavity

major / open / confirmed; issue key: empyema-cavity-parent-grounding.

Update curation/term_requests.tsv for habitatmech:GOLD.818c9729e2 so parent_class is UBERON:0000175 (pleural effusion, or UBERON:0006314 bodily fluid) with parent_mode REPLACE, excluding the anatomical cavity parent UBERON:0002402 (pleural cavity).

### F2: Bare clinical condition label 'Empyema' is asserted as an exact exudate synonym

major / open / confirmed; issue key: empyema-disease-name-exact-synonym.

Remove bare 'Empyema' from exact_synonym in curation/term_requests.tsv for habitatmech:GOLD.818c9729e2 (keeping 'pleural empyema fluid') and add a guarded row in curation/definition_source_label_exclusions.tsv so 'Empyema' is scoped as RELATED_SYNONYM from GOLD rather than EXACT_SYNONYM.

## Recommended Actions And Acceptance Checks

### ACT1

Update curation/term_requests.tsv for habitatmech:GOLD.818c9729e2 so parent_class is UBERON:0000175 (pleural effusion, or UBERON:0006314 bodily fluid) with parent_mode REPLACE, excluding the anatomical cavity parent UBERON:0002402 (pleural cavity). No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Remove bare 'Empyema' from exact_synonym in curation/term_requests.tsv for habitatmech:GOLD.818c9729e2 (keeping 'pleural empyema fluid') and add a guarded row in curation/definition_source_label_exclusions.tsv so 'Empyema' is scoped as RELATED_SYNONYM from GOLD rather than EXACT_SYNONYM. No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/empyema.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.818c9729e2 (mammalian pleural empyema exudate) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.818c9729e2, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["UBERON:0002402"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 2111 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Pleural cavity", "ecosystem_type": "Respiratory system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6844", "leaf_label": "Empyema", "organism_count": "0", "specific_ecosystem": "Empyema", "study_count": "0", "total_assertions": "0"}, "row": 2111}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 13152 | supports | [{"data": {"definition": "The fluid-filled cavity that lies between the visceral and parietal pleurae.", "deprecated": "", "directly_referenced": "TRUE", "label": "pleural cavity", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "cavitas pleuralis&#124;cavitum pleuralae&#124;cavitum pleurale", "term_id": "UBERON:0002402"}, "row": 13152}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 11387 | supports | [{"data": {"object": "UBERON:0035809", "predicate": "rdfs:subClassOf", "subject": "UBERON:0002402"}, "row": 11387}] |
| EDEC | curation/decisions.tsv; TSV rows 784 | supports | [{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.818c9729e2", "notes": "Defined mammalian pleural empyema exudate under UBERON:0002402 'pleural cavity'; supported by pleural empyema 16S and metagenomic studies (PMID 30915025).", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 784}] |
| ETR | curation/term_requests.tsv; TSV rows 600 | supports | [{"data": {"curator": "antigravity", "date": "2026-10-17", "definition": "A pleural cavity purulent exudate accumulated within the mammalian pleural space during bacterial pleuropneumonia or thoracic infection (pleural empyema).", "exact_synonym": "Empyema&#124;pleural empyema fluid", "identifier": "habitatmech:GOLD.818c9729e2", "notes": "Defined mammalian pleural empyema exudate under UBERON:0002402 'pleural cavity'; supported by pleural empyema 16S and metagenomic studies (PMID 30915025).", "parent_class": "UBERON:0002402", "parent_label": "pleural cavity", "parent_mode": "ADD", "requested_label": "mammalian pleural empyema exudate"}, "row": 600}] |
| EP1 | data/habitats/host_associated/pleural_cavity.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "The fluid-filled cavity that lies between the visceral and parietal pleurae.", "grounding_status": "EXACT", "identifier": "UBERON:0002402", "label": "pleural cavity", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0035809", "habitatmech:GOLD.e36ba981d1", "habitatmech:GOLD.fac4f63f3b"], "source_attestations": [{"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6302", "source_label": "Pleural space/cavity", "source_path": "Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity"}, {"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6840", "source_label": "Pleural cavity", "source_path": "Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'empyema&#124;habitatmech:GOLD.818c9729e2' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

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
review_id: 20261026T083033Z-empyema-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: mammalian pleural empyema exudate (habitatmech:GOLD.818c9729e2)'
started_at: '2026-10-26T08:24:00Z'
finished_at: '2026-10-26T08:30:33Z'
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
summary: 'The minted GOLD record habitatmech:GOLD.818c9729e2 (mammalian pleural empyema
  exudate in Host-associated > Mammals > Respiratory system > Pleural cavity > Empyema,
  UNGROUNDED/REVIEWED, no assertion count/unit; total_assertions: 0 in GOLD) defines
  a purulent pleural exudate, but places it as a subclass (is_a) of the anatomical
  cavity UBERON:0002402 (pleural cavity), and asserts the bare clinical condition
  name ''Empyema'' as an EXACT_SYNONYM.'
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
  - path: data/habitats/host_associated/empyema.yaml
    sha256: 67f9f62f0125e7f470b2dfc8fb1731b0fd366a5eb9fb43da866359d5e7eb2479
    role: target
  - path: data/habitats/host_associated/pleural_cavity.yaml
    sha256: dd0018f7e4f9c5bb131b097fc097039abd890e55d10b8b01a689f47c91870dc1
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
- target_id: habitatmech:GOLD.818c9729e2
  path: data/habitats/host_associated/empyema.yaml
  label: mammalian pleural empyema exudate
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/empyema.yaml)
    at captured main revision 1a40d0958114e6e3facd148ccec6197fa4dd679c.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (ear_discharge through empyema); this bundle assesses its single resolved
    identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.818c9729e2
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
    --target-class HabitatRecord data/habitats/host_associated/empyema.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.818c9729e2
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
  - habitatmech:GOLD.818c9729e2
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
  - habitatmech:GOLD.818c9729e2
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
  - habitatmech:GOLD.818c9729e2
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
  - habitatmech:GOLD.818c9729e2
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
  - habitatmech:GOLD.818c9729e2
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
  - habitatmech:GOLD.818c9729e2
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
  - habitatmech:GOLD.818c9729e2
  summary: 'Completed 2026-10-26T08:27:01Z. OK_CANONICAL: 1194, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2063. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/empyema.yaml
  locator: Entire YAML
  accessed_at: '2026-10-26T08:30:33Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.818c9729e2 (mammalian pleural empyema exudate)
    were read.
  snapshot_sha256: 67f9f62f0125e7f470b2dfc8fb1731b0fd366a5eb9fb43da866359d5e7eb2479
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-10-26T08:30:33Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-10-26T08:30:33Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-10-26T08:30:33Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.818c9729e2, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["UBERON:0002402"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2111
  accessed_at: '2026-10-26T08:30:33Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals > Respiratory system > Pleural cavity > Empyema", "depth": "5", "ecosystem":
    "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Pleural
    cavity", "ecosystem_type": "Respiratory system", "gold_node_count": "1", "gold_node_ids":
    "gold.ecosystem:6844", "leaf_label": "Empyema", "organism_count": "0", "specific_ecosystem":
    "Empyema", "study_count": "0", "total_assertions": "0"}, "row": 2111}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 13152
  accessed_at: '2026-10-26T08:30:33Z'
  support: supports
  summary: '[{"data": {"definition": "The fluid-filled cavity that lies between the
    visceral and parietal pleurae.", "deprecated": "", "directly_referenced": "TRUE",
    "label": "pleural cavity", "label_only": "FALSE", "ontology": "UBERON", "synonyms":
    "cavitas pleuralis|cavitum pleuralae|cavitum pleurale", "term_id": "UBERON:0002402"},
    "row": 13152}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 11387
  accessed_at: '2026-10-26T08:30:33Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0035809", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0002402"}, "row": 11387}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 784
  accessed_at: '2026-10-26T08:30:33Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17",
    "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.818c9729e2",
    "notes": "Defined mammalian pleural empyema exudate under UBERON:0002402 ''pleural
    cavity''; supported by pleural empyema 16S and metagenomic studies (PMID 30915025).",
    "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"},
    "row": 784}]'
  snapshot_sha256: f7b5c0d1abf850eea20eb9ac3d76c3caec573f1d68dd0467cbf8d5f9ff9f50cb
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV rows 600
  accessed_at: '2026-10-26T08:30:33Z'
  support: supports
  summary: '[{"data": {"curator": "antigravity", "date": "2026-10-17", "definition":
    "A pleural cavity purulent exudate accumulated within the mammalian pleural space
    during bacterial pleuropneumonia or thoracic infection (pleural empyema).", "exact_synonym":
    "Empyema|pleural empyema fluid", "identifier": "habitatmech:GOLD.818c9729e2",
    "notes": "Defined mammalian pleural empyema exudate under UBERON:0002402 ''pleural
    cavity''; supported by pleural empyema 16S and metagenomic studies (PMID 30915025).",
    "parent_class": "UBERON:0002402", "parent_label": "pleural cavity", "parent_mode":
    "ADD", "requested_label": "mammalian pleural empyema exudate"}, "row": 600}]'
  snapshot_sha256: eae6c1d3d8ceafb8960c41a58cdd1fa1eb83fbefea57dc67bcd0ea6b7357d273
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/pleural_cavity.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-10-26T08:30:33Z'
  support: supports
  summary: '{"definition": "The fluid-filled cavity that lies between the visceral
    and parietal pleurae.", "grounding_status": "EXACT", "identifier": "UBERON:0002402",
    "label": "pleural cavity", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0035809",
    "habitatmech:GOLD.e36ba981d1", "habitatmech:GOLD.fac4f63f3b"], "source_attestations":
    [{"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids
    share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source":
    "GOLD", "source_id": "gold.ecosystem:6302", "source_label": "Pleural space/cavity",
    "source_path": "Host-associated > Mammals: Human > Respiratory system > Pleural
    space/cavity"}, {"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem
    node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:6840", "source_label": "Pleural
    cavity", "source_path": "Host-associated > Mammals > Respiratory system > Pleural
    cavity"}]}'
  snapshot_sha256: dd0018f7e4f9c5bb131b097fc097039abd890e55d10b8b01a689f47c91870dc1
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'empyema|habitatmech:GOLD.818c9729e2' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-10-26T08:30:33Z'
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
  - habitatmech:GOLD.818c9729e2
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: A purulent pleural exudate (mammalian pleural empyema exudate) is an infected
    bodily fluid / pleural effusion accumulated within the pleural space rather than
    a subtype (is_a) of the anatomical pleural cavity (UBERON:0002402), and bare 'Empyema'
    is a clinical condition name rather than an exact synonym of mammalian pleural
    empyema exudate.
  target_ids:
  - habitatmech:GOLD.818c9729e2
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
  - EP1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.818c9729e2
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
  - EP1
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.818c9729e2
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: empyema-cavity-parent-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Mammalian pleural empyema exudate is placed as a subclass of anatomical pleural
    cavity
  description: Update curation/term_requests.tsv for habitatmech:GOLD.818c9729e2 so
    parent_class is UBERON:0000175 (pleural effusion, or UBERON:0006314 bodily fluid)
    with parent_mode REPLACE, excluding the anatomical cavity parent UBERON:0002402
    (pleural cavity).
  target_ids:
  - habitatmech:GOLD.818c9729e2
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
  - EDEC
  - ETR
  - EP1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: empyema-disease-name-exact-synonym
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: Bare clinical condition label 'Empyema' is asserted as an exact exudate synonym
  description: Remove bare 'Empyema' from exact_synonym in curation/term_requests.tsv
    for habitatmech:GOLD.818c9729e2 (keeping 'pleural empyema fluid') and add a guarded
    row in curation/definition_source_label_exclusions.tsv so 'Empyema' is scoped
    as RELATED_SYNONYM from GOLD rather than EXACT_SYNONYM.
  target_ids:
  - habitatmech:GOLD.818c9729e2
  field_paths:
  - synonyms
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
  - habitatmech:GOLD.818c9729e2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Update curation/term_requests.tsv for habitatmech:GOLD.818c9729e2 so
    parent_class is UBERON:0000175 (pleural effusion, or UBERON:0006314 bodily fluid)
    with parent_mode REPLACE, excluding the anatomical cavity parent UBERON:0002402
    (pleural cavity). No repair is performed by this read-only review.
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
  - habitatmech:GOLD.818c9729e2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Remove bare 'Empyema' from exact_synonym in curation/term_requests.tsv
    for habitatmech:GOLD.818c9729e2 (keeping 'pleural empyema fluid') and add a guarded
    row in curation/definition_source_label_exclusions.tsv so 'Empyema' is scoped
    as RELATED_SYNONYM from GOLD rather than EXACT_SYNONYM. No repair is performed
    by this read-only review.
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
