# Record review: epicuticular wax (PO:0025388)

- Review: 20261105T051510Z-epicuticular_wax-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-05T04:39:00Z
- Finished UTC: 2026-11-05T05:15:10Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The GOLD-attested record PO:0025388 (epicuticular wax, EXACT/REVIEWED, no assertion count/unit; total_assertions: 0 in GOLD) maps GOLD 'Host-associated &gt; Plants &gt; Phyllosphere &gt; Phylloplane/Leaf &gt; Epicuticular wax' (source concept habitatmech:GOLD.284cf93966) to PO:0025388 under PO:0025386 (cuticular wax), but retains the whole-organ leaf parent PO:0025034 (leaf) as a superclass.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/epicuticular_wax.yaml) at captured main revision 215b23c90244e634e64f88fa2c1a2a3bb011880a.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (epicuticular_wax through excretory_system); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 215b23c90244e634e64f88fa2c1a2a3bb011880a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| PO:0025388 | data/habitats/host_associated/epicuticular_wax.yaml | generated | epicuticular wax |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | PO:0025388 | Completed 2026-11-05T04:42:18Z. No issues found. |
| validate-strict | passed | True | PO:0025388 | Completed 2026-11-05T04:55:15Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | PO:0025388 | Completed 2026-11-05T04:40:17Z. No issues found; 862 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | PO:0025388 | Completed 2026-11-05T04:40:25Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | PO:0025388 | Completed 2026-11-05T04:41:11Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | PO:0025388 | Completed 2026-11-05T04:40:29Z. validated 73 causal-graph curation file(s) with 73 graph(s). |
| term-requests-check | passed | True | PO:0025388 | Completed 2026-11-05T04:41:21Z. term-request table is current (671 terms). |
| validate-products | passed | True | PO:0025388 | Completed 2026-11-05T04:43:01Z. OK_CANONICAL: 1200, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2077. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: PO:0025388.

Individual schema, strict 24-target validation, 862 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 73 causal overlays, and 671 term requests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: PO:0025388.

Epicuticular wax (PO:0025388) is a lipid film coating (part_of) the outer surface of the plant cuticle under PO:0025386 (cuticular wax), not a subtype (is_a) of the whole organ PO:0025034 (leaf).

### Source counts and retained ranking

quantity: supported. Targets: PO:0025388.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: PO:0025388.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / EXACT; this read-only review does not mutate generated records.

## Findings

### F1: Epicuticular wax retains whole-organ PO:0025034 (leaf) GOLD parent as a superclass

major / open / confirmed; issue key: epicuticular-wax-context-parent.

Add an exclusion row in curation/gold_parent_exclusions.tsv for source identifier habitatmech:GOLD.284cf93966 on GOLD path 'Host-associated &gt; Plants &gt; Phyllosphere &gt; Phylloplane/Leaf &gt; Epicuticular wax' (exact target PO:0025388) excluding parent_id PO:0025034 (leaf), preserving ontology parent PO:0025386 (cuticular wax).

## Recommended Actions And Acceptance Checks

### ACT1

Add an exclusion row in curation/gold_parent_exclusions.tsv for source identifier habitatmech:GOLD.284cf93966 on GOLD path 'Host-associated &gt; Plants &gt; Phyllosphere &gt; Phylloplane/Leaf &gt; Epicuticular wax' (exact target PO:0025388) excluding parent_id PO:0025034 (leaf), preserving ontology parent PO:0025386 (cuticular wax). No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/epicuticular_wax.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for PO:0025388 (epicuticular wax) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=PO:0025388, grounding_status=EXACT, mapping_status=REVIEWED, parent_habitats=["PO:0025034", "PO:0025386"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 2520 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Plants &gt; Phyllosphere &gt; Phylloplane/Leaf &gt; Epicuticular wax", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Plants", "ecosystem_subtype": "Phylloplane/Leaf", "ecosystem_type": "Phyllosphere", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:8139", "leaf_label": "Epicuticular wax", "organism_count": "0", "specific_ecosystem": "Epicuticular wax", "study_count": "0", "total_assertions": "0"}, "row": 2520}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 12132,12484,12486 | supports | [{"data": {"definition": "A phyllome (PO:0006001) that is not associated with a reproductive structure.", "deprecated": "", "directly_referenced": "TRUE", "label": "leaf", "label_only": "FALSE", "ontology": "PO", "synonyms": "hoja (Spanish, exact)&#124;\u8449 (Japanese, exact)", "term_id": "PO:0025034"}, "row": 12132}, {"data": {"definition": "A portion of plant substance (PO:0025161) comprised predominantly of very long chain aliphatic lipids and is part of a plant cuticle (PO:0000022).", "deprecated": "", "directly_referenced": "FALSE", "label": "cuticular wax", "label_only": "FALSE", "ontology": "PO", "synonyms": "cera cuticular (Spanish, exact)&#124;\u30af\u30c1\u30af\u30e9\u30ef\u30c3\u30af\u30b9 (Japanese, exact)", "term_id": "PO:0025386"}, "row": 12484}, {"data": {"definition": "A portion of cuticular wax (PO:0025386) that forms crystalloids or a smooth film on the exterior of a plant cuticle (PO:0000022).", "deprecated": "", "directly_referenced": "TRUE", "label": "epicuticular wax", "label_only": "FALSE", "ontology": "PO", "synonyms": "cera epicuticular (Spanish, exact)&#124;\u30a8\u30d4\u30af\u30c1\u30af\u30e9\u30ef\u30c3\u30af\u30b9 (Japanese, exact)", "term_id": "PO:0025388"}, "row": 12486}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 9960,10183,10184,10227,10563,10565,10566 | supports | [{"data": {"object": "PO:0025034", "predicate": "rdfs:subClassOf", "subject": "PO:0009025"}, "row": 9960}, {"data": {"object": "FOODON:03420144", "predicate": "rdfs:subClassOf", "subject": "PO:0025034"}, "row": 10183}, {"data": {"object": "PO:0006001", "predicate": "rdfs:subClassOf", "subject": "PO:0025034"}, "row": 10184}, {"data": {"object": "PO:0025034", "predicate": "rdfs:subClassOf", "subject": "PO:0025075"}, "row": 10227}, {"data": {"object": "PO:0025161", "predicate": "rdfs:subClassOf", "subject": "PO:0025386"}, "row": 10563}, {"data": {"object": "PO:0025386", "predicate": "rdfs:subClassOf", "subject": "PO:0025388"}, "row": 10565}, {"data": {"object": "PO:0025386", "predicate": "rdfs:subClassOf", "subject": "PO:0025389"}, "row": 10566}] |
| EDEC | curation/decisions.tsv; TSV rows 1621 | supports | [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-14", "decision": "GROUND", "grounding_status": "EXACT", "identifier": "habitatmech:GOLD.284cf93966", "notes": "Stale-sweep review (#12): the class sweep said no term matched, and that was true when it ran \u2014 PO was vendored later, under #10. PO:0025388 'epicuticular wax' matches the leaf exactly and the path is Plants &gt; Phyllosphere &gt; Phylloplane/Leaf &gt; Epicuticular wax, so it is the same thing. Path: Host-associated &gt; Plants &gt; Phyllosphere &gt; Phylloplane/Leaf &gt; Epicuticular wax", "object_id": "PO:0025388", "object_label": "epicuticular wax", "relation": "", "review_depth": "ITEM"}, "row": 1621}] |
| EP1 | data/habitats/host_associated/leaf__36ca5f79.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "A phyllome (PO:0006001) that is not associated with a reproductive structure.", "grounding_status": "EXACT", "identifier": "PO:0025034", "label": "leaf", "mapping_status": "SEEDED", "parent_habitats": ["FOODON:03420144", "PO:0006001", "habitatmech:GOLD.7406232b7e"], "source_attestations": [{"assertion_count": 500, "assertion_unit": "STRAIN", "mapping_predicate": "skos:broadMatch", "notes": "kg-microbe's isolation-source mapping table has no ontology target for this source; the automatic route leaves it ungrounded. The explicit curator decision GROUND overrides that route; this source is emitted on PO:0025034.", "source": "BACDIVE", "source_id": "bacdive.isolation_source:leaf-phyllosphere", "source_label": "Leaf-Phyllosphere"}, {"notes": "Physicochemical parameter bands from kg-microbe's environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "host_plant_leaf-associated", "source_label": "host_plant_leaf-associated"}, {"assertion_count": 843, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:broadMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:5260", "source_label": "Phylloplane/Leaf surface", "source_path": "Host-associated &gt; Plants &gt; Phyllosphere &gt; Phylloplane/Leaf surface"}, {"assertion_count": 1448, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:broadMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:5267", "source_label": "Phylloplane/Leaf", "source_path": "Host-associated &gt; Plants &gt; Phyllosphere &gt; Phylloplane/Leaf"}, {"assertion_count": 77, "assertion_unit": "TAXON", "source": "MADIN", "source_id": "PO:0025034", "source_label": "leaf"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'epicuticular_wax&#124;PO:0025388' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

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
review_id: 20261105T051510Z-epicuticular_wax-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: epicuticular wax (PO:0025388)'
started_at: '2026-11-05T04:39:00Z'
finished_at: '2026-11-05T05:15:10Z'
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
summary: 'The GOLD-attested record PO:0025388 (epicuticular wax, EXACT/REVIEWED, no
  assertion count/unit; total_assertions: 0 in GOLD) maps GOLD ''Host-associated >
  Plants > Phyllosphere > Phylloplane/Leaf > Epicuticular wax'' (source concept habitatmech:GOLD.284cf93966)
  to PO:0025388 under PO:0025386 (cuticular wax), but retains the whole-organ leaf
  parent PO:0025034 (leaf) as a superclass.'
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
  - path: data/habitats/host_associated/epicuticular_wax.yaml
    sha256: d8201ff70f2f356f76afefe5879d56afe4dded116a76fdb993def2c529ca7488
    role: target
  - path: data/habitats/host_associated/leaf__36ca5f79.yaml
    sha256: 9f2fcc88db5b8910201e7acc220fd1fc88baa9532a203e544ed6558d65f2eda9
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
- target_id: PO:0025388
  path: data/habitats/host_associated/epicuticular_wax.yaml
  label: epicuticular wax
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/epicuticular_wax.yaml)
    at captured main revision 215b23c90244e634e64f88fa2c1a2a3bb011880a.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (epicuticular_wax through excretory_system); this bundle assesses its
    single resolved identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - PO:0025388
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
    --target-class HabitatRecord data/habitats/host_associated/epicuticular_wax.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - PO:0025388
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
  - PO:0025388
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
  - PO:0025388
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
  - PO:0025388
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
  - PO:0025388
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
  - PO:0025388
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
  - PO:0025388
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
  - PO:0025388
  summary: 'Completed 2026-11-05T04:43:01Z. OK_CANONICAL: 1200, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2077. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/epicuticular_wax.yaml
  locator: Entire YAML
  accessed_at: '2026-11-05T05:15:10Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for PO:0025388 (epicuticular wax) were read.
  snapshot_sha256: d8201ff70f2f356f76afefe5879d56afe4dded116a76fdb993def2c529ca7488
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-05T05:15:10Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-05T05:15:10Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-05T05:15:10Z'
  support: supports
  summary: Seed generator produces identifier=PO:0025388, grounding_status=EXACT,
    mapping_status=REVIEWED, parent_habitats=["PO:0025034", "PO:0025386"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2520
  accessed_at: '2026-11-05T05:15:10Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Plants > Phyllosphere > Phylloplane/Leaf > Epicuticular wax", "depth": "5",
    "ecosystem": "Host-associated", "ecosystem_category": "Plants", "ecosystem_subtype":
    "Phylloplane/Leaf", "ecosystem_type": "Phyllosphere", "gold_node_count": "1",
    "gold_node_ids": "gold.ecosystem:8139", "leaf_label": "Epicuticular wax", "organism_count":
    "0", "specific_ecosystem": "Epicuticular wax", "study_count": "0", "total_assertions":
    "0"}, "row": 2520}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 12132,12484,12486
  accessed_at: '2026-11-05T05:15:10Z'
  support: supports
  summary: '[{"data": {"definition": "A phyllome (PO:0006001) that is not associated
    with a reproductive structure.", "deprecated": "", "directly_referenced": "TRUE",
    "label": "leaf", "label_only": "FALSE", "ontology": "PO", "synonyms": "hoja (Spanish,
    exact)|\u8449 (Japanese, exact)", "term_id": "PO:0025034"}, "row": 12132}, {"data":
    {"definition": "A portion of plant substance (PO:0025161) comprised predominantly
    of very long chain aliphatic lipids and is part of a plant cuticle (PO:0000022).",
    "deprecated": "", "directly_referenced": "FALSE", "label": "cuticular wax", "label_only":
    "FALSE", "ontology": "PO", "synonyms": "cera cuticular (Spanish, exact)|\u30af\u30c1\u30af\u30e9\u30ef\u30c3\u30af\u30b9
    (Japanese, exact)", "term_id": "PO:0025386"}, "row": 12484}, {"data": {"definition":
    "A portion of cuticular wax (PO:0025386) that forms crystalloids or a smooth film
    on the exterior of a plant cuticle (PO:0000022).", "deprecated": "", "directly_referenced":
    "TRUE", "label": "epicuticular wax", "label_only": "FALSE", "ontology": "PO",
    "synonyms": "cera epicuticular (Spanish, exact)|\u30a8\u30d4\u30af\u30c1\u30af\u30e9\u30ef\u30c3\u30af\u30b9
    (Japanese, exact)", "term_id": "PO:0025388"}, "row": 12486}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 9960,10183,10184,10227,10563,10565,10566
  accessed_at: '2026-11-05T05:15:10Z'
  support: supports
  summary: '[{"data": {"object": "PO:0025034", "predicate": "rdfs:subClassOf", "subject":
    "PO:0009025"}, "row": 9960}, {"data": {"object": "FOODON:03420144", "predicate":
    "rdfs:subClassOf", "subject": "PO:0025034"}, "row": 10183}, {"data": {"object":
    "PO:0006001", "predicate": "rdfs:subClassOf", "subject": "PO:0025034"}, "row":
    10184}, {"data": {"object": "PO:0025034", "predicate": "rdfs:subClassOf", "subject":
    "PO:0025075"}, "row": 10227}, {"data": {"object": "PO:0025161", "predicate": "rdfs:subClassOf",
    "subject": "PO:0025386"}, "row": 10563}, {"data": {"object": "PO:0025386", "predicate":
    "rdfs:subClassOf", "subject": "PO:0025388"}, "row": 10565}, {"data": {"object":
    "PO:0025386", "predicate": "rdfs:subClassOf", "subject": "PO:0025389"}, "row":
    10566}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 1621
  accessed_at: '2026-11-05T05:15:10Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-14",
    "decision": "GROUND", "grounding_status": "EXACT", "identifier": "habitatmech:GOLD.284cf93966",
    "notes": "Stale-sweep review (#12): the class sweep said no term matched, and
    that was true when it ran \u2014 PO was vendored later, under #10. PO:0025388
    ''epicuticular wax'' matches the leaf exactly and the path is Plants > Phyllosphere
    > Phylloplane/Leaf > Epicuticular wax, so it is the same thing. Path: Host-associated
    > Plants > Phyllosphere > Phylloplane/Leaf > Epicuticular wax", "object_id": "PO:0025388",
    "object_label": "epicuticular wax", "relation": "", "review_depth": "ITEM"}, "row":
    1621}]'
  snapshot_sha256: 7e55e782625f544f2d3e4e5c9e5ed5d82c04d477ee606c894bc26cb55f8a949e
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/leaf__36ca5f79.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-05T05:15:10Z'
  support: supports
  summary: '{"definition": "A phyllome (PO:0006001) that is not associated with a
    reproductive structure.", "grounding_status": "EXACT", "identifier": "PO:0025034",
    "label": "leaf", "mapping_status": "SEEDED", "parent_habitats": ["FOODON:03420144",
    "PO:0006001", "habitatmech:GOLD.7406232b7e"], "source_attestations": [{"assertion_count":
    500, "assertion_unit": "STRAIN", "mapping_predicate": "skos:broadMatch", "notes":
    "kg-microbe''s isolation-source mapping table has no ontology target for this
    source; the automatic route leaves it ungrounded. The explicit curator decision
    GROUND overrides that route; this source is emitted on PO:0025034.", "source":
    "BACDIVE", "source_id": "bacdive.isolation_source:leaf-phyllosphere", "source_label":
    "Leaf-Phyllosphere"}, {"notes": "Physicochemical parameter bands from kg-microbe''s
    environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "host_plant_leaf-associated",
    "source_label": "host_plant_leaf-associated"}, {"assertion_count": 843, "assertion_unit":
    "ORGANISM", "mapping_predicate": "skos:broadMatch", "notes": "2 GOLD ecosystem
    node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:5260", "source_label": "Phylloplane/Leaf
    surface", "source_path": "Host-associated > Plants > Phyllosphere > Phylloplane/Leaf
    surface"}, {"assertion_count": 1448, "assertion_unit": "ORGANISM", "mapping_predicate":
    "skos:broadMatch", "notes": "2 GOLD ecosystem node ids share this path; first
    shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id":
    "gold.ecosystem:5267", "source_label": "Phylloplane/Leaf", "source_path": "Host-associated
    > Plants > Phyllosphere > Phylloplane/Leaf"}, {"assertion_count": 77, "assertion_unit":
    "TAXON", "source": "MADIN", "source_id": "PO:0025034", "source_label": "leaf"}]}'
  snapshot_sha256: 9f2fcc88db5b8910201e7acc220fd1fc88baa9532a203e544ed6558d65f2eda9
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'epicuticular_wax|PO:0025388' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-05T05:15:10Z'
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
  - PO:0025388
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: Epicuticular wax (PO:0025388) is a lipid film coating (part_of) the outer
    surface of the plant cuticle under PO:0025386 (cuticular wax), not a subtype (is_a)
    of the whole organ PO:0025034 (leaf).
  target_ids:
  - PO:0025388
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - PO:0025388
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP1
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / EXACT; this read-only review
    does not mutate generated records.
  target_ids:
  - PO:0025388
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: epicuticular-wax-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Epicuticular wax retains whole-organ PO:0025034 (leaf) GOLD parent as a superclass
  description: Add an exclusion row in curation/gold_parent_exclusions.tsv for source
    identifier habitatmech:GOLD.284cf93966 on GOLD path 'Host-associated > Plants
    > Phyllosphere > Phylloplane/Leaf > Epicuticular wax' (exact target PO:0025388)
    excluding parent_id PO:0025034 (leaf), preserving ontology parent PO:0025386 (cuticular
    wax).
  target_ids:
  - PO:0025388
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
  - EP1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
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
  - PO:0025388
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Add an exclusion row in curation/gold_parent_exclusions.tsv for source
    identifier habitatmech:GOLD.284cf93966 on GOLD path 'Host-associated > Plants
    > Phyllosphere > Phylloplane/Leaf > Epicuticular wax' (exact target PO:0025388)
    excluding parent_id PO:0025034 (leaf), preserving ontology parent PO:0025386 (cuticular
    wax). No repair is performed by this read-only review.
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
