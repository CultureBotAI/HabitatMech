# Remediation review: free_living_state

- Review: 20261109T215013Z-free_living_state-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-09T21:40:00Z
- Finished UTC: 2026-11-09T21:50:13Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reclassified PREGO source concept habitatmech:PREGO.6c4660c2ae (BTO:0001551 'free-living state') via an ITEM-level NOT_APPLICABLE decision (target_id=BTO:0001551 'free-living state', relation=xref) in curation/decisions.tsv (#2334). This replaces organism-form state identity BTO:0001551 with minted identifier habitatmech:PREGO.6c4660c2ae (REVIEWED/NOT_APPLICABLE), removes organism-form parent BTO:0000284 (organism form) from parent_habitats, preserves BTO:0001551 as a contextual xref, and retains all 3 PREGO TAXON assertions (3 characteristic_taxa rows). Both predecessor findings (F1 and F2) are resolved.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/free_living_state.yaml after bounded Cycle 8 Stage 5 remediation.

Selection: One of thirteen repaired targets from the finger-through-free_living_state cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c82566b001f676eb0d3c9cc6c905f85a99b8bde.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:PREGO.6c4660c2ae | data/habitats/host_associated/free_living_state.yaml | generated | free-living state |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:48:00Z. No issues found against src/habitatmech/schema/habitatmech.yaml. |
| validate-strict | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:48:05Z. 24 checked, 0 failed; target passed closed-schema validation. |
| validate-history | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:48:10Z. No issues found; 879 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:48:15Z. 14 inventory files and 2 GOLD export files verified. |
| verify-corpus | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:48:25Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:48:30Z. 103 causal-graph curations and target records validated. |
| term-requests-check | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:48:35Z. term-request table is current (676 terms). |
| validate-products | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:48:45Z. 24 records, 0 label drift findings. |
| pytest counterfactual review repairs | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:49:00Z. 2 passed; exact 13-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:49:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:PREGO.6c4660c2ae | Completed 2026-11-09T21:49:30Z. rendered 3209 habitat pages, 757 redirect stubs, 8 categories, 701 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:PREGO.6c4660c2ae.

Individual schema, strict 24-target validation, 879 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal overlays, 676 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:PREGO.6c4660c2ae.

habitatmech:PREGO.6c4660c2ae: free-living state; NOT_APPLICABLE/REVIEWED; parents []. Reclassified PREGO source concept habitatmech:PREGO.6c4660c2ae (BTO:0001551 'free-living state') via an ITEM-level NOT_APPLICABLE decision (target_id=BTO:0001551 'free-living state', relation=xref) in curation/decisions.tsv (#2334). This replaces organism-form state identity BTO:0001551 with minted identifier habitatmech:PREGO.6c4660c2ae (REVIEWED/NOT_APPLICABLE), removes organism-form parent BTO:0000284 (organism form) from parent_habitats, preserves BTO:0001551 as a contextual xref, and retains all 3 PREGO TAXON assertions (3 characteristic_taxa rows). Both predecessor findings (F1 and F2) are resolved.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:PREGO.6c4660c2ae.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 3, "source": "PREGO", "unit": "TAXON"}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: habitatmech:PREGO.6c4660c2ae.

Every predecessor finding preserves its stable issue_key and exact lineage. All predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:PREGO.6c4660c2ae.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / NOT_APPLICABLE; this read-only review does not mutate generated records.

## Findings

### F1: Microbial physiological/lifestyle state BTO:0001551 (free-living state) is used as a habitat identity

blocker / resolved / confirmed; issue key: free-living-state-organism-form-identity.

BTO:0001551 (free-living state, definition: null, child of BTO:0000284 organism form, attested by 3 PREGO TAXON rows for Bradyrhizobium sp. DOA9, Escherichia coli str. K-12 substr. W3110, and Azorhizobium caulinodans ORS 571) describes a physiological/lifestyle state of the microbe itself (contrasted with the symbiotic/bacteroid state in nitrogen-fixing rhizobia), not a microbial habitat or anatomical host site. Under docs/CURATION.md, add an ITEM-level NOT_APPLICABLE row in curation/decisions.tsv for habitatmech:PREGO.6c4660c2ae (object_id=BTO:0001551, object_label=free-living state, category=HOST_ASSOCIATED), preserving BTO:0001551 as an xref and retaining all 3 PREGO taxon rows on the minted concept, and update data/habitats/PATHS.tsv.

Disposition: Added ITEM-level NOT_APPLICABLE decision for habitatmech:PREGO.6c4660c2ae (target_id=BTO:0001551 'free-living state', relation=xref) in curation/decisions.tsv (#2334), reclassifying the organismal ecological-mode bin as REVIEWED/NOT_APPLICABLE with BTO:0001551 preserved as a contextual xref.

### F2: Organism-form class BTO:0000284 (organism form) is asserted in parent_habitats

major / resolved / confirmed; issue key: free-living-state-organism-form-parent.

BTO:0000284 (organism form) is an organism-form classification imported from BTO:0001551 rather than a strictly broader microbial habitat superclass. Resolving F1 in curation/decisions.tsv (NOT_APPLICABLE on habitatmech:PREGO.6c4660c2ae) removes BTO:0000284 from parent_habitats.

Disposition: Resolved by reclassifying habitatmech:PREGO.6c4660c2ae as NOT_APPLICABLE in curation/decisions.tsv (#2334), removing the BTO:0001551 -&gt; BTO:0000284 (organism form) subclass edge from parent_habitats.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/free_living_state.yaml; Entire YAML | supports | {"identifier": "habitatmech:PREGO.6c4660c2ae", "label": "free-living state", "grounding_status": "NOT_APPLICABLE", "mapping_status": "REVIEWED", "xrefs": ["BTO:0001551"], "synonyms": [{"synonym_text": "free-living states", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}], "source_attestations": [{"source": "PREGO", "source_id": "BTO:0001551", "source_label": "free-living state", "assertion_count": 3, "assertion_unit": "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by PREGO. Grounding: NOT_APPLICABLE."}, {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "NOT_APPLICABLE", "changes": "Marked NOT_APPLICABLE: the source concept does not denote a habitat. BTO:0001551 kept as an xref. ITEM organism-state review #2334: PREGO BTO:0001551 ('free-living state', child of BTO:0000284 'organism form', attested by 3 PREGO taxon rows for Bradyrhizobium sp. DOA9, Escherichia coli str. K-12 substr. W3110, and Azorhizobium caulinodans ORS 571) describes a physiological/lifestyle state of the microbe itself (contrasted with the symbiotic/bacteroid state in nitrogen-fixing rhizobia) rather than an external microbial habitat or anatomical host site. Mark NOT_APPLICABLE on the minted concept habitatmech:PREGO.6c4660c2ae in HOST_ASSOCIATED while preserving BTO:0001551 as an xref and retaining all 3 PREGO taxon rows. https://purl.obolibrary.org/obo/BTO_0001551 (source concept habitatmech:PREGO.6c4660c2ae)"}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and subcellular organelle terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:PREGO.6c4660c2ae, grounding_status=NOT_APPLICABLE, mapping_status=REVIEWED, parent_habitats=[], xrefs=["BTO:0001551"]. |
| ESIB1 | data/habitats/host_associated/adult.yaml; Entire YAML | supports | {"identifier": "habitatmech:PREGO.57e0a5faae", "label": "adult-associated environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "definition": "An environmental system determined by a living organism that has reached its adult stage.", "parent_habitats": ["ENVO:01001000"], "xrefs": ["BTO:0001043"], "synonyms": [{"synonym_text": "adult stage", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "adult stages", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}, {"synonym_text": "adults", "synonym_type": "RELATED_SYNONYM", "source": "PREGO"}]} |
| EPREGO | data/raw/prego_habitats.tsv; TSV rows 446 | supports | [{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "3", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0001551", "prego_synonyms": "free-living state&#124;free-living states", "taxon_count": "3"}, "row": 446}] |
| EPREGOTAXA | data/raw/prego_habitat_taxa.tsv; TSV rows 2394,2395,2396 | supports | 3 PREGO taxon-association rows for BTO:0001551. |
| EONT | data/raw/ontology_terms.tsv; TSV rows 286,1551 | supports | [{"data": {"definition": "", "deprecated": "", "directly_referenced": "FALSE", "label": "organism form", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000284"}, "row": 286}, {"data": {"definition": "", "deprecated": "", "directly_referenced": "TRUE", "label": "free-living state", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001551"}, "row": 1551}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 68,82,122,194,218,246,278,366,701,791,793,1027,1056,1184,1368 | supports | [{"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0000090"}, "row": 68}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0000109"}, "row": 82}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0000174"}, "row": 122}, {"data": {"object": "BTO:0000000", "predicate": "rdfs:subClassOf", "subject": "BTO:0000284"}, "row": 194}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0000320"}, "row": 218}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0000377"}, "row": 246}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0000425"}, "row": 278}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0000569"}, "row": 366}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0001043"}, "row": 701}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0001171"}, "row": 791}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0001172"}, "row": 793}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0001512"}, "row": 1027}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0001551"}, "row": 1056}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0001762"}, "row": 1184}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0002007"}, "row": 1368}] |
| ESEARCH | Local input and review traversal; grep -rn -E 'free_living_state&#124;BTO:0001551' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal located Stage 4 predecessor bundle 20261109T181033Z-free_living_state-record (linked via EPREV and related_reviews) and checked related cohort and ancestor reviews for reconciliation. |
| EDEC | curation/decisions.tsv; TSV line 1845 | supports | [[1845, "habitatmech:PREGO.6c4660c2ae\tNOT_APPLICABLE\tBTO:0001551\tfree-living state\t\tantigravity\t2026-11-09\tITEM organism-state review #2334: PREGO BTO:0001551 ('free-living state', child of BTO:0000284 'organism form', attested by 3 PREGO taxon rows for Bradyrhizobium sp. DOA9, Escherichia coli str. K-12 substr. W3110, and Azorhizobium caulinodans ORS 571) describes a physiological/lifestyle state of the microbe itself (contrasted with the symbiotic/bacteroid state in nitrogen-fixing rhizobia) rather than an external microbial habitat or anatomical host site. Mark NOT_APPLICABLE on the minted concept habitatmech:PREGO.6c4660c2ae in HOST_ASSOCIATED while preserving BTO:0001551 as an xref and retaining all 3 PREGO taxon rows. https://purl.obolibrary.org/obo/BTO_0001551\tITEM\tHOST_ASSOCIATED\txref"]] |
| EPREV | reviews/structured/20261109T181033Z-free_living_state-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_finger_to_free_living_state_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly thirteen records differ from the counterfactual baseline across Issues #2334, #2335, and #2336. |
| EHIST_G1 | history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2334 recorded and validated. |

## Limits And Additional Notes

- Only the cited repository inputs, ontology terms, and source inventories were inspected; original specimen-level support for every upstream source assertion was not exhaustively reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus identifier certification.
- Read-only review: no curation table, generated habitat YAML, status, or history record was modified.
- Saved against working-tree repairs atop main commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261109T181033Z-free_living_state-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T215013Z-free_living_state-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: free_living_state'
started_at: '2026-11-09T21:40:00Z'
finished_at: '2026-11-09T21:50:13Z'
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
summary: Reclassified PREGO source concept habitatmech:PREGO.6c4660c2ae (BTO:0001551
  'free-living state') via an ITEM-level NOT_APPLICABLE decision (target_id=BTO:0001551
  'free-living state', relation=xref) in curation/decisions.tsv (#2334). This replaces
  organism-form state identity BTO:0001551 with minted identifier habitatmech:PREGO.6c4660c2ae
  (REVIEWED/NOT_APPLICABLE), removes organism-form parent BTO:0000284 (organism form)
  from parent_habitats, preserves BTO:0001551 as a contextual xref, and retains all
  3 PREGO TAXON assertions (3 characteristic_taxa rows). Both predecessor findings
  (F1 and F2) are resolved.
source:
  git_revision: 7c82566b001f676eb0d3c9cc6c905f85a99b8bde
  state: working_tree
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
  - path: data/habitats/host_associated/adult.yaml
    sha256: 91c41fc8a4d72c43682756d0e29562fbf92e27e198d386fc5847a6c8961e4e04
    role: context
  - path: data/habitats/host_associated/free_living_state.yaml
    sha256: 136893501eba32ff41eacb0c0eeb35e411da91d8571077b6d6185aec64dfad2f
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
  - path: history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml
    sha256: b6347253e029b5d760e3e10bc1c927efc02c51fd69114bd920a11681c35f7ff2
    role: context
  - path: reviews/structured/20261109T181033Z-free_living_state-record/review.yaml
    sha256: c1db1765656c6124cf551a16e44f117ae27c6e9b2e742ae2bbd59303f247ab76
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
  - path: tests/test_finger_to_free_living_state_review_repairs.py
    sha256: 495a506d77d0f3c2484e16b510c233a7c8b108ae96cba6b6346252c3a9d01bdb
    role: context
targets:
- target_id: habitatmech:PREGO.6c4660c2ae
  path: data/habitats/host_associated/free_living_state.yaml
  label: free-living state
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
  description: Full current target assessment and explicit disposition of every baseline
    finding on data/habitats/host_associated/free_living_state.yaml after bounded
    Cycle 8 Stage 5 remediation.
  selection: One of thirteen repaired targets from the finger-through-free_living_state
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:PREGO.6c4660c2ae
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
    --target-class HabitatRecord data/habitats/host_associated/free_living_state.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  summary: Completed 2026-11-09T21:48:00Z. No issues found against src/habitatmech/schema/habitatmech.yaml.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/finger.yaml
    data/habitats/host_associated/fingernail.yaml data/habitats/host_associated/fish.yaml
    data/habitats/host_associated/fistula.yaml data/habitats/host_associated/flagellate.yaml
    data/habitats/host_associated/flagellum.yaml data/habitats/host_associated/flea.yaml
    data/habitats/host_associated/flesh.yaml data/habitats/host_associated/floc.yaml
    data/habitats/host_associated/flower.yaml data/habitats/host_associated/Flower_head.yaml
    data/habitats/host_associated/fluid.yaml data/habitats/host_associated/fluid__8fb24b60.yaml
    data/habitats/host_associated/fly.yaml data/habitats/host_associated/fomite.yaml
    data/habitats/host_associated/foot.yaml data/habitats/host_associated/foregut.yaml
    data/habitats/host_associated/foregut__6bc8c43a.yaml data/habitats/host_associated/foregut__c14450a8.yaml
    data/habitats/host_associated/foregut__ce63e8ab.yaml data/habitats/host_associated/foregut__d14a54ae.yaml
    data/habitats/host_associated/foregut__ee6a8f74.yaml data/habitats/host_associated/foreleg.yaml
    data/habitats/host_associated/forestomach.yaml --out .temp/c8s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  summary: Completed 2026-11-09T21:48:05Z. 24 checked, 0 failed; target passed closed-schema
    validation.
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
  - habitatmech:PREGO.6c4660c2ae
  summary: Completed 2026-11-09T21:48:10Z. No issues found; 879 history record(s)
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
  - habitatmech:PREGO.6c4660c2ae
  summary: Completed 2026-11-09T21:48:15Z. 14 inventory files and 2 GOLD export files
    verified.
  scope_note: Full-corpus raw inventory provenance verification.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: .venv/bin/python scripts/verify_corpus.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  summary: 'Completed 2026-11-09T21:48:25Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:PREGO.6c4660c2ae
  summary: Completed 2026-11-09T21:48:30Z. 103 causal-graph curations and target records
    validated.
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  summary: Completed 2026-11-09T21:48:35Z. term-request table is current (676 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  summary: Completed 2026-11-09T21:48:45Z. 24 records, 0 label drift findings.
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_finger_to_free_living_state_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  summary: Completed 2026-11-09T21:49:00Z. 2 passed; exact 13-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2334, #2335,
    and #2336.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  summary: Completed 2026-11-09T21:49:05Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  summary: Completed 2026-11-09T21:49:30Z. rendered 3209 habitat pages, 757 redirect
    stubs, 8 categories, 701 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/free_living_state.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: '{"identifier": "habitatmech:PREGO.6c4660c2ae", "label": "free-living state",
    "grounding_status": "NOT_APPLICABLE", "mapping_status": "REVIEWED", "xrefs": ["BTO:0001551"],
    "synonyms": [{"synonym_text": "free-living states", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}], "source_attestations": [{"source": "PREGO", "source_id":
    "BTO:0001551", "source_label": "free-living state", "assertion_count": 3, "assertion_unit":
    "TAXON", "score": 3.0, "evidence_channels": "annotated_genomes_isolates"}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by PREGO. Grounding: NOT_APPLICABLE."}, {"timestamp": "2026-11-09T00:00:00Z",
    "curator": "antigravity", "action": "NOT_APPLICABLE", "changes": "Marked NOT_APPLICABLE:
    the source concept does not denote a habitat. BTO:0001551 kept as an xref. ITEM
    organism-state review #2334: PREGO BTO:0001551 (''free-living state'', child of
    BTO:0000284 ''organism form'', attested by 3 PREGO taxon rows for Bradyrhizobium
    sp. DOA9, Escherichia coli str. K-12 substr. W3110, and Azorhizobium caulinodans
    ORS 571) describes a physiological/lifestyle state of the microbe itself (contrasted
    with the symbiotic/bacteroid state in nitrogen-fixing rhizobia) rather than an
    external microbial habitat or anatomical host site. Mark NOT_APPLICABLE on the
    minted concept habitatmech:PREGO.6c4660c2ae in HOST_ASSOCIATED while preserving
    BTO:0001551 as an xref and retaining all 3 PREGO taxon rows. https://purl.obolibrary.org/obo/BTO_0001551
    (source concept habitatmech:PREGO.6c4660c2ae)"}]}'
  snapshot_sha256: 136893501eba32ff41eacb0c0eeb35e411da91d8571077b6d6185aec64dfad2f
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and subcellular organelle terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:PREGO.6c4660c2ae, grounding_status=NOT_APPLICABLE,
    mapping_status=REVIEWED, parent_habitats=[], xrefs=["BTO:0001551"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/adult.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: '{"identifier": "habitatmech:PREGO.57e0a5faae", "label": "adult-associated
    environment", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "definition": "An environmental system determined by a living organism that has
    reached its adult stage.", "parent_habitats": ["ENVO:01001000"], "xrefs": ["BTO:0001043"],
    "synonyms": [{"synonym_text": "adult stage", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "adult stages", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}, {"synonym_text": "adults", "synonym_type": "RELATED_SYNONYM",
    "source": "PREGO"}]}'
  snapshot_sha256: 91c41fc8a4d72c43682756d0e29562fbf92e27e198d386fc5847a6c8961e4e04
- evidence_id: EPREGO
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: TSV rows 446
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: '[{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels":
    "annotated_genomes_isolates", "direct_assertion_count": "3", "max_prego_score":
    "3", "ontology": "BTO", "prego_id": "BTO:0001551", "prego_synonyms": "free-living
    state|free-living states", "taxon_count": "3"}, "row": 446}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: EPREGOTAXA
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: TSV rows 2394,2395,2396
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: 3 PREGO taxon-association rows for BTO:0001551.
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 286,1551
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: '[{"data": {"definition": "", "deprecated": "", "directly_referenced":
    "FALSE", "label": "organism form", "label_only": "FALSE", "ontology": "BTO", "synonyms":
    "", "term_id": "BTO:0000284"}, "row": 286}, {"data": {"definition": "", "deprecated":
    "", "directly_referenced": "TRUE", "label": "free-living state", "label_only":
    "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0001551"}, "row":
    1551}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 68,82,122,194,218,246,278,366,701,791,793,1027,1056,1184,1368
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000090"}, "row": 68}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000109"}, "row": 82}, {"data": {"object": "BTO:0000284", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0000174"}, "row": 122}, {"data": {"object":
    "BTO:0000000", "predicate": "rdfs:subClassOf", "subject": "BTO:0000284"}, "row":
    194}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000320"}, "row": 218}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000377"}, "row": 246}, {"data": {"object": "BTO:0000284", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0000425"}, "row": 278}, {"data": {"object":
    "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0000569"}, "row":
    366}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0001043"}, "row": 701}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0001171"}, "row": 791}, {"data": {"object": "BTO:0000284", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0001172"}, "row": 793}, {"data": {"object":
    "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0001512"}, "row":
    1027}, {"data": {"object": "BTO:0000284", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0001551"}, "row": 1056}, {"data": {"object": "BTO:0000284", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0001762"}, "row": 1184}, {"data": {"object":
    "BTO:0000284", "predicate": "rdfs:subClassOf", "subject": "BTO:0002007"}, "row":
    1368}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'free_living_state|BTO:0001551' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-09T21:50:13Z'
  support: context_only
  summary: Structured-review traversal located Stage 4 predecessor bundle 20261109T181033Z-free_living_state-record
    (linked via EPREV and related_reviews) and checked related cohort and ancestor
    reviews for reconciliation.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde.
- evidence_id: EDEC
  kind: record_content
  reference: curation/decisions.tsv
  locator: TSV line 1845
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: '[[1845, "habitatmech:PREGO.6c4660c2ae\tNOT_APPLICABLE\tBTO:0001551\tfree-living
    state\t\tantigravity\t2026-11-09\tITEM organism-state review #2334: PREGO BTO:0001551
    (''free-living state'', child of BTO:0000284 ''organism form'', attested by 3
    PREGO taxon rows for Bradyrhizobium sp. DOA9, Escherichia coli str. K-12 substr.
    W3110, and Azorhizobium caulinodans ORS 571) describes a physiological/lifestyle
    state of the microbe itself (contrasted with the symbiotic/bacteroid state in
    nitrogen-fixing rhizobia) rather than an external microbial habitat or anatomical
    host site. Mark NOT_APPLICABLE on the minted concept habitatmech:PREGO.6c4660c2ae
    in HOST_ASSOCIATED while preserving BTO:0001551 as an xref and retaining all 3
    PREGO taxon rows. https://purl.obolibrary.org/obo/BTO_0001551\tITEM\tHOST_ASSOCIATED\txref"]]'
  snapshot_sha256: 8e0c9ea50c453b9b0eb86e9a6cf246dbc188714ec7a8cc37b2918d5373e6d2ae
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261109T181033Z-free_living_state-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: c1db1765656c6124cf551a16e44f117ae27c6e9b2e742ae2bbd59303f247ab76
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_finger_to_free_living_state_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: 'Exactly thirteen records differ from the counterfactual baseline across
    Issues #2334, #2335, and #2336.'
  snapshot_sha256: 495a506d77d0f3c2484e16b510c233a7c8b108ae96cba6b6346252c3a9d01bdb
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-09T21:50:13Z'
  support: supports
  summary: 'Authorized curation event for Issue #2334 recorded and validated.'
  snapshot_sha256: b6347253e029b5d760e3e10bc1c927efc02c51fd69114bd920a11681c35f7ff2
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 879 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal
    overlays, 676 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'habitatmech:PREGO.6c4660c2ae: free-living state; NOT_APPLICABLE/REVIEWED;
    parents []. Reclassified PREGO source concept habitatmech:PREGO.6c4660c2ae (BTO:0001551
    ''free-living state'') via an ITEM-level NOT_APPLICABLE decision (target_id=BTO:0001551
    ''free-living state'', relation=xref) in curation/decisions.tsv (#2334). This
    replaces organism-form state identity BTO:0001551 with minted identifier habitatmech:PREGO.6c4660c2ae
    (REVIEWED/NOT_APPLICABLE), removes organism-form parent BTO:0000284 (organism
    form) from parent_habitats, preserves BTO:0001551 as a contextual xref, and retains
    all 3 PREGO TAXON assertions (3 characteristic_taxa rows). Both predecessor findings
    (F1 and F2) are resolved.'
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"count": 3, "source": "PREGO", "unit": "TAXON"}]. Zero counts are
    omitted; unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: supported
  summary: Every predecessor finding preserves its stable issue_key and exact lineage.
    All predecessor findings in this target scope are resolved.
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / NOT_APPLICABLE; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
findings:
- finding_id: F1
  issue_key: free-living-state-organism-form-identity
  category: identity
  severity: blocker
  status: resolved
  certainty: confirmed
  title: Microbial physiological/lifestyle state BTO:0001551 (free-living state) is
    used as a habitat identity
  description: 'BTO:0001551 (free-living state, definition: null, child of BTO:0000284
    organism form, attested by 3 PREGO TAXON rows for Bradyrhizobium sp. DOA9, Escherichia
    coli str. K-12 substr. W3110, and Azorhizobium caulinodans ORS 571) describes
    a physiological/lifestyle state of the microbe itself (contrasted with the symbiotic/bacteroid
    state in nitrogen-fixing rhizobia), not a microbial habitat or anatomical host
    site. Under docs/CURATION.md, add an ITEM-level NOT_APPLICABLE row in curation/decisions.tsv
    for habitatmech:PREGO.6c4660c2ae (object_id=BTO:0001551, object_label=free-living
    state, category=HOST_ASSOCIATED), preserving BTO:0001551 as an xref and retaining
    all 3 PREGO taxon rows on the minted concept, and update data/habitats/PATHS.tsv.'
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  field_paths:
  - identifier
  - grounding_status
  - mapping_status
  - parent_habitats
  - xrefs
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: blocker
  normalization_reason: Microbial lifestyle/organism-form state is adopted as a habitat
    identity, contradicting docs/CURATION.md.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2334
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261109T181033Z-free_living_state-record
    finding_id: F1
  disposition_reason: Added ITEM-level NOT_APPLICABLE decision for habitatmech:PREGO.6c4660c2ae
    (target_id=BTO:0001551 'free-living state', relation=xref) in curation/decisions.tsv
    (#2334), reclassifying the organismal ecological-mode bin as REVIEWED/NOT_APPLICABLE
    with BTO:0001551 preserved as a contextual xref.
- finding_id: F2
  issue_key: free-living-state-organism-form-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Organism-form class BTO:0000284 (organism form) is asserted in parent_habitats
  description: BTO:0000284 (organism form) is an organism-form classification imported
    from BTO:0001551 rather than a strictly broader microbial habitat superclass.
    Resolving F1 in curation/decisions.tsv (NOT_APPLICABLE on habitatmech:PREGO.6c4660c2ae)
    removes BTO:0000284 from parent_habitats.
  target_ids:
  - habitatmech:PREGO.6c4660c2ae
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EPREGO
  - EPREGOTAXA
  - EONT
  - EONTEDGE
  - ESEARCH
  - EDEC
  - EPREV
  - ETEST
  - EHIST_G1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2334
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261109T181033Z-free_living_state-record
    finding_id: F2
  disposition_reason: Resolved by reclassifying habitatmech:PREGO.6c4660c2ae as NOT_APPLICABLE
    in curation/decisions.tsv (#2334), removing the BTO:0001551 -> BTO:0000284 (organism
    form) subclass edge from parent_habitats.
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
- Saved against working-tree repairs atop main commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261109T181033Z-free_living_state-record with exact
  issue_key and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181033Z-free_living_state-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
