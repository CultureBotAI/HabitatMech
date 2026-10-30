# Record review: echinoderm-associated environment (habitatmech:GOLD.e1f435d44b)

- Review: 20261026T083013Z-echinodermata-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-26T08:24:00Z
- Finished UTC: 2026-10-26T08:30:13Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The minted GOLD record habitatmech:GOLD.e1f435d44b (echinoderm-associated environment in Host-associated &gt; Invertebrates &gt; Echinodermata, UNGROUNDED/REVIEWED, 21 ORGANISM assertions) preserves echinoderm host-associated environment scope under ENVO:01001002 (animal-associated environment) and habitatmech:GOLD.4d792ac724 (invertebrate-associated environment) with contextual xref FOODON:03412115 (echinoderm), but asserts the bare host phylum label 'Echinodermata' as an EXACT_SYNONYM.

## Scope And Provenance

Scientific assessment of one exact generated target (data/habitats/host_associated/echinodermata.yaml) at captured main revision 1a40d0958114e6e3facd148ccec6197fa4dd679c.

Selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/ path order (ear_discharge through empyema); this bundle assesses its single resolved identifier and source path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 1a40d0958114e6e3facd148ccec6197fa4dd679c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.e1f435d44b | data/habitats/host_associated/echinodermata.yaml | generated | echinoderm-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.e1f435d44b | Completed 2026-10-26T08:25:36Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.e1f435d44b | Completed 2026-10-26T08:25:42Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.e1f435d44b | Completed 2026-10-26T08:25:48Z. No issues found; 852 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.e1f435d44b | Completed 2026-10-26T08:25:49Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.e1f435d44b | Completed 2026-10-26T08:26:03Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.e1f435d44b | Completed 2026-10-26T08:26:07Z. validated 53 causal-graph curation file(s) with 53 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.e1f435d44b | Completed 2026-10-26T08:26:21Z. term-request table is current (661 terms). |
| validate-products | passed | True | habitatmech:GOLD.e1f435d44b | Completed 2026-10-26T08:27:01Z. OK_CANONICAL: 1194, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2063. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.e1f435d44b.

Individual schema, strict 24-target validation, 852 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 53 causal overlays, and 661 term requests passed.

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.e1f435d44b.

The record is properly defined as 'An animal-associated environment which is determined by an echinoderm or by a part of an echinoderm.' under ENVO:01001002 and habitatmech:GOLD.4d792ac724 with contextual xref FOODON:03412115 (echinoderm), but synonyms includes EXACT_SYNONYM 'Echinodermata', which equates the host phylum with its associated environment.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.e1f435d44b.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": 21, "unit": "ORGANISM"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.e1f435d44b.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Host phylum label 'Echinodermata' is asserted as an exact environment synonym

major / open / confirmed; issue key: echinodermata-host-name-exact-synonym.

Remove the bare host phylum alias 'Echinodermata' from exact_synonym in curation/term_requests.tsv and add a guarded row in curation/definition_source_label_exclusions.tsv for habitatmech:GOLD.e1f435d44b so 'Echinodermata' is scoped as RELATED_SYNONYM from GOLD rather than EXACT_SYNONYM.

## Recommended Actions And Acceptance Checks

### ACT1

Remove the bare host phylum alias 'Echinodermata' from exact_synonym in curation/term_requests.tsv and add a guarded row in curation/definition_source_label_exclusions.tsv for habitatmech:GOLD.e1f435d44b so 'Echinodermata' is scoped as RELATED_SYNONYM from GOLD rather than EXACT_SYNONYM. No repair is performed by this read-only review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/echinodermata.yaml; Entire YAML | supports | All target fields, source attestations, synonyms, parent_habitats, and generated history for habitatmech:GOLD.e1f435d44b (echinoderm-associated environment) were read. |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.e1f435d44b, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001002", "habitatmech:GOLD.4d792ac724"]. |
| ERESEARCH | research/habitats/host_associated/echinodermata-habitatmech-gold-e1f435d44b-deep-research-claude_code.md; Entire markdown report | supports | Committed deep-research report for habitatmech:GOLD.e1f435d44b supporting an echinoderm-associated environment definition and keeping taxon FOODON:03412115 as a contextual xref. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 409 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Invertebrates &gt; Echinodermata", "depth": "3", "ecosystem": "Host-associated", "ecosystem_category": "Invertebrates", "ecosystem_subtype": "", "ecosystem_type": "Echinodermata", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:3565&#124;gold.ecosystem:4802&#124;gold.ecosystem:4803", "leaf_label": "Echinodermata", "organism_count": "21", "specific_ecosystem": "", "study_count": "0", "total_assertions": "21"}, "row": 409}] |
| EGROUND | data/raw/isolation_source_groundings.tsv; TSV rows 98 | supports | [{"data": {"confidence": "high", "curator": "ols4_auto", "mapping_justification": "semapv:LexicalMatching", "object_id": "NCBITaxon:7586", "object_label": "Echinodermata", "object_source": "NCBITaxon", "predicate_id": "skos:exactMatch", "source_dataset": "bacdive", "subject_label": "Echinodermata", "subject_label_normalized": "echinodermata", "verified_date": "2026-05-01"}, "row": 98}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 8491,10696 | supports | [{"data": {"definition": "An environmental system determined by an animal.", "deprecated": "", "directly_referenced": "TRUE", "label": "animal-associated environment", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "Metazoan-associated environment&#124;animal environment", "term_id": "ENVO:01001002"}, "row": 8491}, {"data": {"definition": "Echinoderm is the common name given to any member of the phylum *Echinodermata* of marine animals. The adults are recognizable by their (usually five-point) radial symmetry, and include such well-known animals as sea stars, sea urchins, sand dollars, and sea cucumbers, as well as the sea lilies or \"stone lilies\". [https://en.wikipedia.org/wiki/Echinoderm]", "deprecated": "", "directly_referenced": "TRUE", "label": "echinoderm", "label_only": "FALSE", "ontology": "FOODON", "synonyms": "Echinodermata&#124;Echinodermata Klein, 1734", "term_id": "FOODON:03412115"}, "row": 10696}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 6797,6992,6996,7704,8928,9020,9024,9025 | supports | [{"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001002"}, "row": 6797}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001176"}, "row": 6992}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001179"}, "row": 6996}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001829"}, "row": 7704}, {"data": {"object": "FOODON:03412115", "predicate": "rdfs:subClassOf", "subject": "FOODON:02022154"}, "row": 8928}, {"data": {"object": "FOODON:03412115", "predicate": "rdfs:subClassOf", "subject": "FOODON:03412107"}, "row": 9020}, {"data": {"object": "FOODON:00005703", "predicate": "rdfs:subClassOf", "subject": "FOODON:03412115"}, "row": 9024}, {"data": {"object": "FOODON:03411433", "predicate": "rdfs:subClassOf", "subject": "FOODON:03412115"}, "row": 9025}] |
| EDEC | curation/decisions.tsv; TSV rows 1581 | supports | [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-16", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.e1f435d44b", "notes": "Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it \u2014 the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an &lt;X&gt;-associated environment. Host-associated &gt; Porifera was NOT_APPLICABLE while its own child Porifera &gt; Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim.", "object_id": "FOODON:03412115", "object_label": "echinoderm", "relation": "xref", "review_depth": "ITEM"}, "row": 1581}] |
| ETR | curation/term_requests.tsv; TSV rows 59 | supports | [{"data": {"curator": "claude-opus-5", "date": "2026-09-02", "definition": "An animal-associated environment which is determined by an echinoderm or by a part of an echinoderm.", "exact_synonym": "Echinodermata", "identifier": "habitatmech:GOLD.e1f435d44b", "notes": "Definition authored from the record's committed deep-research report under research/habitats/, read in full; no new research was commissioned. Completes the invertebrate ladder (#222): invertebrate-, mollusc- and tunicate-associated environment were already authored at this rung on ENVO:01001002, and the echinoderm branch was the only one with neither a term nor an ontology parent - which is how it stayed unnoticed, since a record with no ontology parent is invisible to every ancestry-based screen. Worded exactly like the mollusc and tunicate siblings. FOODON:03412115 'echinoderm' and NCBITaxon:7586 stay xrefs: the phylum is a class of organisms, not a place (#99, #114). Genus is ENVO:01001002 and NOT the ENVO:01001176 this report recommends (#210, #222). The report is the fourth on this family to reach that recommendation and it makes the case against itself more clearly than any of the others: its own near-miss table rejects ENVO:01001055 'environment associated with an animal part or small animal' because 'the source concept is whole organisms across five classes spanning millimetre brittle stars to metre-long holothurians', and ENVO asserts ENVO:01001176 as a subclass of exactly that term - so the recommended genus imports the restriction the same paragraph refuses. The report also cites ENVO:01001179 'cnidarian-associated environment' as precedent for phylum-level granularity and notes it is asserted DIRECTLY under ENVO:01001002; that is the fact which decides against ENVO:01001176 rather than for it. Recorded rather than silently overridden, because a report is evidence for a curator and not an input. Dropped the exact synonym 'Echinodermata-associated environment' before merge (#229): it was coined at authoring time to mirror the requested label and is attested by no source and proposed by no report - the same construction #213 removed for 'Bivalvia-associated environment'. It passes the guard added there because it does not squash to the requested label, which is why that guard is not sufficient on its own. The GOLD source label is kept.", "parent_class": "ENVO:01001002", "parent_label": "animal-associated environment", "parent_mode": "ADD", "requested_label": "echinoderm-associated environment"}, "row": 59}] |
| EP1 | data/habitats/other/animal_associated_environment.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by an animal.", "grounding_status": "EXACT", "identifier": "ENVO:01001002", "label": "animal-associated environment", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"notes": "Physicochemical parameter bands from kg-microbe's environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal"}, {"assertion_count": 144, "assertion_unit": "TAXON", "source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated environment"}]} |
| EP2 | data/habitats/host_associated/invertebrates.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "An environmental system determined by an invertebrate.", "grounding_status": "UNGROUNDED", "identifier": "habitatmech:GOLD.4d792ac724", "label": "invertebrate-associated environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000", "ENVO:01001002"], "source_attestations": [{"assertion_count": 621, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3374", "source_label": "Invertebrates", "source_path": "Host-associated &gt; Invertebrates"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'echinodermata&#124;habitatmech:GOLD.e1f435d44b' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |

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
review_id: 20261026T083013Z-echinodermata-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: echinoderm-associated environment (habitatmech:GOLD.e1f435d44b)'
started_at: '2026-10-26T08:24:00Z'
finished_at: '2026-10-26T08:30:13Z'
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
summary: The minted GOLD record habitatmech:GOLD.e1f435d44b (echinoderm-associated
  environment in Host-associated > Invertebrates > Echinodermata, UNGROUNDED/REVIEWED,
  21 ORGANISM assertions) preserves echinoderm host-associated environment scope under
  ENVO:01001002 (animal-associated environment) and habitatmech:GOLD.4d792ac724 (invertebrate-associated
  environment) with contextual xref FOODON:03412115 (echinoderm), but asserts the
  bare host phylum label 'Echinodermata' as an EXACT_SYNONYM.
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
  - path: data/habitats/host_associated/echinodermata.yaml
    sha256: dfe4bcae51128e9e7f896ce5cf0f28578d628c8de01a8b9dd360744c71bffdb8
    role: target
  - path: data/habitats/host_associated/invertebrates.yaml
    sha256: c59c31e2f2e591167a1008f0fc67b6d8a4c7ca3cda46a22d79af28e6cf6358f8
    role: context
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
  - path: research/habitats/host_associated/echinodermata-habitatmech-gold-e1f435d44b-deep-research-claude_code.md
    sha256: 674c96ffd1fa0759e4a6329be1fe708e967d0862fc2a6a1d260af4287ab5e7f3
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: habitatmech:GOLD.e1f435d44b
  path: data/habitats/host_associated/echinodermata.yaml
  label: echinoderm-associated environment
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
  description: Scientific assessment of one exact generated target (data/habitats/host_associated/echinodermata.yaml)
    at captured main revision 1a40d0958114e6e3facd148ccec6197fa4dd679c.
  selection: Contiguous 24-record unreviewed cohort in data/habitats/host_associated/
    path order (ear_discharge through empyema); this bundle assesses its single resolved
    identifier and source path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.e1f435d44b
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
    --target-class HabitatRecord data/habitats/host_associated/echinodermata.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.e1f435d44b
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
  - habitatmech:GOLD.e1f435d44b
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
  - habitatmech:GOLD.e1f435d44b
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
  - habitatmech:GOLD.e1f435d44b
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
  - habitatmech:GOLD.e1f435d44b
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
  - habitatmech:GOLD.e1f435d44b
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
  - habitatmech:GOLD.e1f435d44b
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
  - habitatmech:GOLD.e1f435d44b
  summary: 'Completed 2026-10-26T08:27:01Z. OK_CANONICAL: 1194, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2063. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/echinodermata.yaml
  locator: Entire YAML
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: All target fields, source attestations, synonyms, parent_habitats, and
    generated history for habitatmech:GOLD.e1f435d44b (echinoderm-associated environment)
    were read.
  snapshot_sha256: dfe4bcae51128e9e7f896ce5cf0f28578d628c8de01a8b9dd360744c71bffdb8
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.e1f435d44b, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001002", "habitatmech:GOLD.4d792ac724"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ERESEARCH
  kind: primary_source
  reference: research/habitats/host_associated/echinodermata-habitatmech-gold-e1f435d44b-deep-research-claude_code.md
  locator: Entire markdown report
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: Committed deep-research report for habitatmech:GOLD.e1f435d44b supporting
    an echinoderm-associated environment definition and keeping taxon FOODON:03412115
    as a contextual xref.
  snapshot_sha256: 674c96ffd1fa0759e4a6329be1fe708e967d0862fc2a6a1d260af4287ab5e7f3
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 409
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Invertebrates > Echinodermata", "depth": "3", "ecosystem": "Host-associated",
    "ecosystem_category": "Invertebrates", "ecosystem_subtype": "", "ecosystem_type":
    "Echinodermata", "gold_node_count": "3", "gold_node_ids": "gold.ecosystem:3565|gold.ecosystem:4802|gold.ecosystem:4803",
    "leaf_label": "Echinodermata", "organism_count": "21", "specific_ecosystem": "",
    "study_count": "0", "total_assertions": "21"}, "row": 409}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EGROUND
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: TSV rows 98
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: '[{"data": {"confidence": "high", "curator": "ols4_auto", "mapping_justification":
    "semapv:LexicalMatching", "object_id": "NCBITaxon:7586", "object_label": "Echinodermata",
    "object_source": "NCBITaxon", "predicate_id": "skos:exactMatch", "source_dataset":
    "bacdive", "subject_label": "Echinodermata", "subject_label_normalized": "echinodermata",
    "verified_date": "2026-05-01"}, "row": 98}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 8491,10696
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: '[{"data": {"definition": "An environmental system determined by an animal.",
    "deprecated": "", "directly_referenced": "TRUE", "label": "animal-associated environment",
    "label_only": "FALSE", "ontology": "ENVO", "synonyms": "Metazoan-associated environment|animal
    environment", "term_id": "ENVO:01001002"}, "row": 8491}, {"data": {"definition":
    "Echinoderm is the common name given to any member of the phylum *Echinodermata*
    of marine animals. The adults are recognizable by their (usually five-point) radial
    symmetry, and include such well-known animals as sea stars, sea urchins, sand
    dollars, and sea cucumbers, as well as the sea lilies or \"stone lilies\". [https://en.wikipedia.org/wiki/Echinoderm]",
    "deprecated": "", "directly_referenced": "TRUE", "label": "echinoderm", "label_only":
    "FALSE", "ontology": "FOODON", "synonyms": "Echinodermata|Echinodermata Klein,
    1734", "term_id": "FOODON:03412115"}, "row": 10696}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 6797,6992,6996,7704,8928,9020,9024,9025
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: '[{"data": {"object": "ENVO:01001000", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001002"}, "row": 6797}, {"data": {"object": "ENVO:01001002",
    "predicate": "rdfs:subClassOf", "subject": "ENVO:01001176"}, "row": 6992}, {"data":
    {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf", "subject": "ENVO:01001179"},
    "row": 6996}, {"data": {"object": "ENVO:01001002", "predicate": "rdfs:subClassOf",
    "subject": "ENVO:01001829"}, "row": 7704}, {"data": {"object": "FOODON:03412115",
    "predicate": "rdfs:subClassOf", "subject": "FOODON:02022154"}, "row": 8928}, {"data":
    {"object": "FOODON:03412115", "predicate": "rdfs:subClassOf", "subject": "FOODON:03412107"},
    "row": 9020}, {"data": {"object": "FOODON:00005703", "predicate": "rdfs:subClassOf",
    "subject": "FOODON:03412115"}, "row": 9024}, {"data": {"object": "FOODON:03411433",
    "predicate": "rdfs:subClassOf", "subject": "FOODON:03412115"}, "row": 9025}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 1581
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-16",
    "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.e1f435d44b",
    "notes": "Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning
    that ''a host taxon is not a habitat''. That reasoning is wrong, and the corpus
    already contradicted it \u2014 the same kind of concept was treated as a habitat
    for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own
    identity and a term request for an <X>-associated environment. Host-associated
    > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term
    request.An organism acting as a host IS a habitat: it is where the microbe lives,
    and ENVO models exactly this at plant-associated, animal-associated and fungi-associated
    environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class
    of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept
    keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept
    is not a habitat, which is a stronger and false claim.", "object_id": "FOODON:03412115",
    "object_label": "echinoderm", "relation": "xref", "review_depth": "ITEM"}, "row":
    1581}]'
  snapshot_sha256: f7b5c0d1abf850eea20eb9ac3d76c3caec573f1d68dd0467cbf8d5f9ff9f50cb
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV rows 59
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: '[{"data": {"curator": "claude-opus-5", "date": "2026-09-02", "definition":
    "An animal-associated environment which is determined by an echinoderm or by a
    part of an echinoderm.", "exact_synonym": "Echinodermata", "identifier": "habitatmech:GOLD.e1f435d44b",
    "notes": "Definition authored from the record''s committed deep-research report
    under research/habitats/, read in full; no new research was commissioned. Completes
    the invertebrate ladder (#222): invertebrate-, mollusc- and tunicate-associated
    environment were already authored at this rung on ENVO:01001002, and the echinoderm
    branch was the only one with neither a term nor an ontology parent - which is
    how it stayed unnoticed, since a record with no ontology parent is invisible to
    every ancestry-based screen. Worded exactly like the mollusc and tunicate siblings.
    FOODON:03412115 ''echinoderm'' and NCBITaxon:7586 stay xrefs: the phylum is a
    class of organisms, not a place (#99, #114). Genus is ENVO:01001002 and NOT the
    ENVO:01001176 this report recommends (#210, #222). The report is the fourth on
    this family to reach that recommendation and it makes the case against itself
    more clearly than any of the others: its own near-miss table rejects ENVO:01001055
    ''environment associated with an animal part or small animal'' because ''the source
    concept is whole organisms across five classes spanning millimetre brittle stars
    to metre-long holothurians'', and ENVO asserts ENVO:01001176 as a subclass of
    exactly that term - so the recommended genus imports the restriction the same
    paragraph refuses. The report also cites ENVO:01001179 ''cnidarian-associated
    environment'' as precedent for phylum-level granularity and notes it is asserted
    DIRECTLY under ENVO:01001002; that is the fact which decides against ENVO:01001176
    rather than for it. Recorded rather than silently overridden, because a report
    is evidence for a curator and not an input. Dropped the exact synonym ''Echinodermata-associated
    environment'' before merge (#229): it was coined at authoring time to mirror the
    requested label and is attested by no source and proposed by no report - the same
    construction #213 removed for ''Bivalvia-associated environment''. It passes the
    guard added there because it does not squash to the requested label, which is
    why that guard is not sufficient on its own. The GOLD source label is kept.",
    "parent_class": "ENVO:01001002", "parent_label": "animal-associated environment",
    "parent_mode": "ADD", "requested_label": "echinoderm-associated environment"},
    "row": 59}]'
  snapshot_sha256: eae6c1d3d8ceafb8960c41a58cdd1fa1eb83fbefea57dc67bcd0ea6b7357d273
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/other/animal_associated_environment.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: '{"definition": "An environmental system determined by an animal.", "grounding_status":
    "EXACT", "identifier": "ENVO:01001002", "label": "animal-associated environment",
    "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001000"], "source_attestations":
    [{"notes": "Physicochemical parameter bands from kg-microbe''s environment table.",
    "source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal"},
    {"assertion_count": 144, "assertion_unit": "TAXON", "source": "MADIN", "source_id":
    "ENVO:01001002", "source_label": "animal-associated environment"}]}'
  snapshot_sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/invertebrates.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-10-26T08:30:13Z'
  support: supports
  summary: '{"definition": "An environmental system determined by an invertebrate.",
    "grounding_status": "UNGROUNDED", "identifier": "habitatmech:GOLD.4d792ac724",
    "label": "invertebrate-associated environment", "mapping_status": "REVIEWED",
    "parent_habitats": ["ENVO:01001000", "ENVO:01001002"], "source_attestations":
    [{"assertion_count": 621, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem
    node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3374", "source_label": "Invertebrates",
    "source_path": "Host-associated > Invertebrates"}]}'
  snapshot_sha256: c59c31e2f2e591167a1008f0fc67b6d8a4c7ca3cda46a22d79af28e6cf6358f8
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'echinodermata|habitatmech:GOLD.e1f435d44b' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-10-26T08:30:13Z'
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
  - habitatmech:GOLD.e1f435d44b
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: The record is properly defined as 'An animal-associated environment which
    is determined by an echinoderm or by a part of an echinoderm.' under ENVO:01001002
    and habitatmech:GOLD.4d792ac724 with contextual xref FOODON:03412115 (echinoderm),
    but synonyms includes EXACT_SYNONYM 'Echinodermata', which equates the host phylum
    with its associated environment.
  target_ids:
  - habitatmech:GOLD.e1f435d44b
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ERESEARCH
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
  - EP2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": 21, "unit": "ORGANISM"}]. Zero counts
    are omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.e1f435d44b
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ERESEARCH
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
  - EP2
- assessment_id: A4
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.e1f435d44b
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: echinodermata-host-name-exact-synonym
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: Host phylum label 'Echinodermata' is asserted as an exact environment synonym
  description: Remove the bare host phylum alias 'Echinodermata' from exact_synonym
    in curation/term_requests.tsv and add a guarded row in curation/definition_source_label_exclusions.tsv
    for habitatmech:GOLD.e1f435d44b so 'Echinodermata' is scoped as RELATED_SYNONYM
    from GOLD rather than EXACT_SYNONYM.
  target_ids:
  - habitatmech:GOLD.e1f435d44b
  field_paths:
  - synonyms
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ERESEARCH
  - EGOLD
  - EGROUND
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
  - EP2
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
  - habitatmech:GOLD.e1f435d44b
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Remove the bare host phylum alias 'Echinodermata' from exact_synonym
    in curation/term_requests.tsv and add a guarded row in curation/definition_source_label_exclusions.tsv
    for habitatmech:GOLD.e1f435d44b so 'Echinodermata' is scoped as RELATED_SYNONYM
    from GOLD rather than EXACT_SYNONYM. No repair is performed by this read-only
    review.
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
