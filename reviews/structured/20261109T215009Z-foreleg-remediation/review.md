# Remediation review: foreleg

- Review: 20261109T215009Z-foreleg-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-09T21:40:00Z
- Finished UTC: 2026-11-09T21:50:09Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Replaced whole-limb BTO:0006514 ('foreleg') exact grounding on habitatmech:GOLD.80220dc4d4 ('Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs') with ITEM-level CONFIRM_UNGROUNDED (target_id=UBERON:0000029 'lymph node', relation=parent) in curation/decisions.tsv, defined 'mammalian forelimb lymph node' under UBERON:0000029 (parent_mode REPLACE) in curation/term_requests.tsv, and excluded automatic retention of displaced source label 'Forelegs' in curation/definition_source_label_exclusions.tsv (#2334). This resolves both the whole-limb identity mismatch and the limb parent collision (BTO:0000721 'leg'), placing the record cleanly under UBERON:0000029 (lymph node) alongside sibling Lymph nodes &gt; Hind legs (habitatmech:GOLD.ca4882ca81). Both predecessor findings (F1 and F2) are resolved.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/foreleg.yaml after bounded Cycle 8 Stage 5 remediation.

Selection: One of thirteen repaired targets from the finger-through-free_living_state cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c82566b001f676eb0d3c9cc6c905f85a99b8bde.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.80220dc4d4 | data/habitats/host_associated/foreleg.yaml | generated | mammalian forelimb lymph node |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:48:00Z. No issues found against src/habitatmech/schema/habitatmech.yaml. |
| validate-strict | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:48:05Z. 24 checked, 0 failed; target passed closed-schema validation. |
| validate-history | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:48:10Z. No issues found; 879 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:48:15Z. 14 inventory files and 2 GOLD export files verified. |
| verify-corpus | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:48:25Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:48:30Z. 103 causal-graph curations and target records validated. |
| term-requests-check | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:48:35Z. term-request table is current (676 terms). |
| validate-products | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:48:45Z. 24 records, 0 label drift findings. |
| pytest counterfactual review repairs | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:49:00Z. 2 passed; exact 13-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:49:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:GOLD.80220dc4d4 | Completed 2026-11-09T21:49:30Z. rendered 3209 habitat pages, 757 redirect stubs, 8 categories, 701 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:GOLD.80220dc4d4.

Individual schema, strict 24-target validation, 879 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 103 causal overlays, 676 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:GOLD.80220dc4d4.

habitatmech:GOLD.80220dc4d4: mammalian forelimb lymph node; UNGROUNDED/REVIEWED; parents ["UBERON:0000029"]. Replaced whole-limb BTO:0006514 ('foreleg') exact grounding on habitatmech:GOLD.80220dc4d4 ('Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs') with ITEM-level CONFIRM_UNGROUNDED (target_id=UBERON:0000029 'lymph node', relation=parent) in curation/decisions.tsv, defined 'mammalian forelimb lymph node' under UBERON:0000029 (parent_mode REPLACE) in curation/term_requests.tsv, and excluded automatic retention of displaced source label 'Forelegs' in curation/definition_source_label_exclusions.tsv (#2334). This resolves both the whole-limb identity mismatch and the limb parent collision (BTO:0000721 'leg'), placing the record cleanly under UBERON:0000029 (lymph node) alongside sibling Lymph nodes &gt; Hind legs (habitatmech:GOLD.ca4882ca81). Both predecessor findings (F1 and F2) are resolved.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.80220dc4d4.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: habitatmech:GOLD.80220dc4d4.

Every predecessor finding preserves its stable issue_key and exact lineage. All predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.80220dc4d4.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Mammalian forelimb lymph node path is grounded to whole limb BTO:0006514 (foreleg)

blocker / resolved / confirmed; issue key: foreleg-lymph-node-identity.

GOLD path 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' (habitatmech:GOLD.80220dc4d4) denotes a lymph node of the mammalian forelimb (such as the axillary or superficial cervical lymph node, parallel to already-curated sibling hind_legs.yaml habitatmech:GOLD.ca4882ca81 'mammalian hindlimb lymph node'), not the entire front leg (BTO:0006514 foreleg, 'A front leg.'). Replace the GROUND decision on habitatmech:GOLD.80220dc4d4 in curation/decisions.tsv with CONFIRM_UNGROUNDED (object_id=UBERON:0000029, object_label=lymph node, relation=parent), author a curated definition for 'mammalian forelimb lymph node' under UBERON:0000029 in curation/term_requests.tsv, exclude displaced source label 'Forelegs' in curation/definition_source_label_exclusions.tsv, and update data/habitats/PATHS.tsv.

Disposition: Updated habitatmech:GOLD.80220dc4d4 in curation/decisions.tsv from BTO:0006514 ('foreleg') to ITEM-level CONFIRM_UNGROUNDED (target_id=UBERON:0000029 'lymph node', relation=parent), defined 'mammalian forelimb lymph node' under UBERON:0000029 (parent_mode REPLACE) in curation/term_requests.tsv, and added a guarded source-label exclusion for 'Forelegs' in curation/definition_source_label_exclusions.tsv (#2334).

### F2: Grounding forelimb lymph node to BTO:0006514 (foreleg) asserts UBERON:0000029 (lymph node) as a parent of foreleg

major / resolved / confirmed; issue key: foreleg-lymph-node-parent-collision.

Because habitatmech:GOLD.80220dc4d4 ('Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs') is grounded to BTO:0006514 (foreleg), the generated record combines BTO subclass parent BTO:0000721 (leg) with GOLD path parent UBERON:0000029 (lymph node), falsely asserting that a foreleg is a subtype of lymph node. Resolving F1 by ungrounding habitatmech:GOLD.80220dc4d4 to 'mammalian forelimb lymph node' under UBERON:0000029 eliminates this parent collision.

Disposition: Resolved by un-grounding habitatmech:GOLD.80220dc4d4 from BTO:0006514 and defining it under UBERON:0000029 (parent_mode REPLACE) in curation/term_requests.tsv (#2334), removing the whole-limb BTO subclass parent BTO:0000721 (leg) and aligning the record with sibling habitatmech:GOLD.ca4882ca81 ('mammalian hindlimb lymph node').

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/foreleg.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.80220dc4d4", "label": "mammalian forelimb lymph node", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "definition": "A lymph node located in the forelimb of a non-human mammal (such as the axillary or superficial cervical lymph node).", "parent_habitats": ["UBERON:0000029"], "synonyms": [{"synonym_text": "mammalian foreleg lymph node", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6764", "source_label": "Forelegs", "source_path": "Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. Nearest broader term UBERON:0000029 'lymph node' attached as a parent. ITEM curation #2334: GOLD 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' denotes lymph nodes of the mammalian forelimb (such as the axillary or superficial cervical/prescapular lymph node; PMID 29643885; DOI:10.3389/fimmu.2018.00682), parallel to sibling hind_legs.yaml (habitatmech:GOLD.ca4882ca81 'mammalian hindlimb lymph node'), not the entire front leg (BTO:0006514 'foreleg'). Keep the source concept minted under UBERON:0000029 ('lymph node'). Path: Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs (source concept habitatmech:GOLD.80220dc4d4)"}, {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "DEFINED", "changes": "Defined as 'mammalian forelimb lymph node' under UBERON:0000029 'lymph node'. ITEM curation #2334: GOLD 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' denotes lymph nodes of the mammalian forelimb (PMID 29643885; DOI:10.3389/fimmu.2018.00682), parallel to sibling habitatmech:GOLD.ca4882ca81 ('mammalian hindlimb lymph node'). Path: Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs"}, {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted automatic retention of displaced source label 'Forelegs' when defining habitatmech:GOLD.80220dc4d4 as 'mammalian forelimb lymph node'. Verbatim source attestations are preserved. Review #2334: Displaced GOLD source label 'Forelegs' in path 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' names the whole forelimb rather than the defined habitat 'mammalian forelimb lymph node'; suppress automatic exact-synonym retention while preserving verbatim source provenance."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon, organism-form, and subcellular organelle terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.80220dc4d4, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["UBERON:0000029"], xrefs=[]. |
| ESIB1 | data/habitats/host_associated/hind_legs.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.ca4882ca81", "label": "mammalian hindlimb lymph node", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "definition": "A lymph node located in the hindlimb of a non-human mammal (such as the popliteal or subiliac lymph node).", "parent_habitats": ["UBERON:0000029"]} |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 2076 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Lymph nodes", "ecosystem_type": "Lymphatic system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6764", "leaf_label": "Forelegs", "organism_count": "0", "specific_ecosystem": "Forelegs", "study_count": "0", "total_assertions": "0"}, "row": 2076}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 722,6513,12878 | supports | [{"data": {"definition": "A limb of an animal used especially for supporting the body and for walking.", "deprecated": "", "directly_referenced": "FALSE", "label": "leg", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0000721"}, "row": 722}, {"data": {"definition": "A front leg.", "deprecated": "", "directly_referenced": "TRUE", "label": "foreleg", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id": "BTO:0006514"}, "row": 6513}, {"data": {"definition": "Any of the rounded masses of lymphoid tissue that are surrounded by a capsule of connective tissue, are distributed along the lymphatic vessels, and contain numerous lymphocytes which filter the flow of lymph.", "deprecated": "", "directly_referenced": "TRUE", "label": "lymph node", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "lymph gland&#124;nodus lymphaticus", "term_id": "UBERON:0000029"}, "row": 12878}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 463,464,4556,4557,10990 | supports | [{"data": {"object": "BTO:0001729", "predicate": "rdfs:subClassOf", "subject": "BTO:0000721"}, "row": 463}, {"data": {"object": "BTO:0002345", "predicate": "rdfs:subClassOf", "subject": "BTO:0000721"}, "row": 464}, {"data": {"object": "BTO:0000721", "predicate": "rdfs:subClassOf", "subject": "BTO:0006514"}, "row": 4556}, {"data": {"object": "BTO:0000721", "predicate": "rdfs:subClassOf", "subject": "BTO:0006515"}, "row": 4557}, {"data": {"object": "UBERON:0005057", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000029"}, "row": 10990}] |
| EP2 | data/habitats/host_associated/lymph_node__7af26c8b.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"identifier": "UBERON:0000029", "label": "lymph node", "grounding_status": "EXACT", "mapping_status": "REVIEWED", "definition": "Any of the rounded masses of lymphoid tissue that are surrounded by a capsule of connective tissue, are distributed along the lymphatic vessels, and contain numerous lymphocytes which filter the flow of lymph.", "parent_habitats": ["UBERON:0005057", "habitatmech:GOLD.a792be9b27", "habitatmech:GOLD.be39fe9a0e"], "synonyms": [{"synonym_text": "Lymph nodes", "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "lymph gland", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text": "nodus lymphaticus", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'foreleg&#124;BTO:0006514' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal located Stage 4 predecessor bundle 20261109T181025Z-foreleg-record (linked via EPREV and related_reviews) and checked related cohort and ancestor reviews for reconciliation. |
| ETR | curation/term_requests.tsv; TSV line 678 | supports | [[678, "habitatmech:GOLD.80220dc4d4\tmammalian forelimb lymph node\tUBERON:0000029\tlymph node\tA lymph node located in the forelimb of a non-human mammal (such as the axillary or superficial cervical lymph node).\tmammalian foreleg lymph node\tantigravity\t2026-11-09\tITEM curation #2334: GOLD 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' denotes lymph nodes of the mammalian forelimb (PMID 29643885; DOI:10.3389/fimmu.2018.00682), parallel to sibling habitatmech:GOLD.ca4882ca81 ('mammalian hindlimb lymph node'). Path: Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs\tREPLACE"]] |
| EDEC | curation/decisions.tsv; TSV line 776 | supports | [[776, "habitatmech:GOLD.80220dc4d4\tCONFIRM_UNGROUNDED\tUBERON:0000029\tlymph node\t\tantigravity\t2026-11-09\tITEM curation #2334: GOLD 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' denotes lymph nodes of the mammalian forelimb (such as the axillary or superficial cervical/prescapular lymph node; PMID 29643885; DOI:10.3389/fimmu.2018.00682), parallel to sibling hind_legs.yaml (habitatmech:GOLD.ca4882ca81 'mammalian hindlimb lymph node'), not the entire front leg (BTO:0006514 'foreleg'). Keep the source concept minted under UBERON:0000029 ('lymph node'). Path: Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs\tITEM\tHOST_ASSOCIATED\tparent"]] |
| ESYNS | curation/definition_source_label_exclusions.tsv; TSV line 4 | supports | [[4, "habitatmech:GOLD.80220dc4d4\tForelegs\tmammalian forelimb lymph node\tantigravity\t2026-11-09\tReview #2334: Displaced GOLD source label 'Forelegs' in path 'Host-associated &gt; Mammals &gt; Lymphatic system &gt; Lymph nodes &gt; Forelegs' names the whole forelimb rather than the defined habitat 'mammalian forelimb lymph node'; suppress automatic exact-synonym retention while preserving verbatim source provenance."]] |
| EPREV | reviews/structured/20261109T181025Z-foreleg-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_finger_to_free_living_state_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly thirteen records differ from the counterfactual baseline across Issues #2334, #2335, and #2336. |
| EHIST_G1 | history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2334 recorded and validated. |

## Limits And Additional Notes

- Only the cited repository inputs, ontology terms, and source inventories were inspected; original specimen-level support for every upstream source assertion was not exhaustively reconstructed.
- Source counts, PREGO scores, and ranks are not prevalence, viability, mechanism, or characteristic presence.
- Configured label correspondence skipped 2,094 no-adapter pairs; this is not whole-corpus identifier certification.
- Read-only review: no curation table, generated habitat YAML, status, or history record was modified.
- Saved against working-tree repairs atop main commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261109T181025Z-foreleg-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261109T215009Z-foreleg-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: foreleg'
started_at: '2026-11-09T21:40:00Z'
finished_at: '2026-11-09T21:50:09Z'
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
summary: Replaced whole-limb BTO:0006514 ('foreleg') exact grounding on habitatmech:GOLD.80220dc4d4
  ('Host-associated > Mammals > Lymphatic system > Lymph nodes > Forelegs') with ITEM-level
  CONFIRM_UNGROUNDED (target_id=UBERON:0000029 'lymph node', relation=parent) in curation/decisions.tsv,
  defined 'mammalian forelimb lymph node' under UBERON:0000029 (parent_mode REPLACE)
  in curation/term_requests.tsv, and excluded automatic retention of displaced source
  label 'Forelegs' in curation/definition_source_label_exclusions.tsv (#2334). This
  resolves both the whole-limb identity mismatch and the limb parent collision (BTO:0000721
  'leg'), placing the record cleanly under UBERON:0000029 (lymph node) alongside sibling
  Lymph nodes > Hind legs (habitatmech:GOLD.ca4882ca81). Both predecessor findings
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
  - path: data/habitats/host_associated/foreleg.yaml
    sha256: 7057177ca95014cd6805eb7173f846b81c7f711396963887e500dee201be4bb5
    role: target
  - path: data/habitats/host_associated/hind_legs.yaml
    sha256: 92f64b32540428e126f0d371ed83553b36e4f1429458c855dfde6753ccc7d088
    role: context
  - path: data/habitats/host_associated/lymph_node__7af26c8b.yaml
    sha256: 2ad5c08889ffa33811bb6d9e2cf48891e13376d441f51fdacac76aa2456288b7
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
  - path: history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml
    sha256: b6347253e029b5d760e3e10bc1c927efc02c51fd69114bd920a11681c35f7ff2
    role: context
  - path: reviews/structured/20261109T181025Z-foreleg-record/review.yaml
    sha256: 1ff0d6b3fc34ac12a6f33203daa47c856f7672938fcd99bc761423f7e0e1f590
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
- target_id: habitatmech:GOLD.80220dc4d4
  path: data/habitats/host_associated/foreleg.yaml
  label: mammalian forelimb lymph node
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
    finding on data/habitats/host_associated/foreleg.yaml after bounded Cycle 8 Stage
    5 remediation.
  selection: One of thirteen repaired targets from the finger-through-free_living_state
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.80220dc4d4
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
    --target-class HabitatRecord data/habitats/host_associated/foreleg.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.80220dc4d4
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
  - habitatmech:GOLD.80220dc4d4
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
  - habitatmech:GOLD.80220dc4d4
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
  - habitatmech:GOLD.80220dc4d4
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
  - habitatmech:GOLD.80220dc4d4
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
  - habitatmech:GOLD.80220dc4d4
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
  - habitatmech:GOLD.80220dc4d4
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
  - habitatmech:GOLD.80220dc4d4
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
  - habitatmech:GOLD.80220dc4d4
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
  - habitatmech:GOLD.80220dc4d4
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
  - habitatmech:GOLD.80220dc4d4
  summary: Completed 2026-11-09T21:49:30Z. rendered 3209 habitat pages, 757 redirect
    stubs, 8 categories, 701 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/foreleg.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.80220dc4d4", "label": "mammalian forelimb
    lymph node", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "definition":
    "A lymph node located in the forelimb of a non-human mammal (such as the axillary
    or superficial cervical lymph node).", "parent_habitats": ["UBERON:0000029"],
    "synonyms": [{"synonym_text": "mammalian foreleg lymph node", "synonym_type":
    "EXACT_SYNONYM", "source": "HabitatMech curation"}], "source_attestations": [{"source":
    "GOLD", "source_id": "gold.ecosystem:6764", "source_label": "Forelegs", "source_path":
    "Host-associated > Mammals > Lymphatic system > Lymph nodes > Forelegs"}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-11-09T00:00:00Z", "curator":
    "antigravity", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED:
    no ontology term fits this concept. Nearest broader term UBERON:0000029 ''lymph
    node'' attached as a parent. ITEM curation #2334: GOLD ''Host-associated > Mammals
    > Lymphatic system > Lymph nodes > Forelegs'' denotes lymph nodes of the mammalian
    forelimb (such as the axillary or superficial cervical/prescapular lymph node;
    PMID 29643885; DOI:10.3389/fimmu.2018.00682), parallel to sibling hind_legs.yaml
    (habitatmech:GOLD.ca4882ca81 ''mammalian hindlimb lymph node''), not the entire
    front leg (BTO:0006514 ''foreleg''). Keep the source concept minted under UBERON:0000029
    (''lymph node''). Path: Host-associated > Mammals > Lymphatic system > Lymph nodes
    > Forelegs (source concept habitatmech:GOLD.80220dc4d4)"}, {"timestamp": "2026-11-09T00:00:00Z",
    "curator": "antigravity", "action": "DEFINED", "changes": "Defined as ''mammalian
    forelimb lymph node'' under UBERON:0000029 ''lymph node''. ITEM curation #2334:
    GOLD ''Host-associated > Mammals > Lymphatic system > Lymph nodes > Forelegs''
    denotes lymph nodes of the mammalian forelimb (PMID 29643885; DOI:10.3389/fimmu.2018.00682),
    parallel to sibling habitatmech:GOLD.ca4882ca81 (''mammalian hindlimb lymph node'').
    Path: Host-associated > Mammals > Lymphatic system > Lymph nodes > Forelegs"},
    {"timestamp": "2026-11-09T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED",
    "changes": "Omitted automatic retention of displaced source label ''Forelegs''
    when defining habitatmech:GOLD.80220dc4d4 as ''mammalian forelimb lymph node''.
    Verbatim source attestations are preserved. Review #2334: Displaced GOLD source
    label ''Forelegs'' in path ''Host-associated > Mammals > Lymphatic system > Lymph
    nodes > Forelegs'' names the whole forelimb rather than the defined habitat ''mammalian
    forelimb lymph node''; suppress automatic exact-synonym retention while preserving
    verbatim source provenance."}]}'
  snapshot_sha256: 7057177ca95014cd6805eb7173f846b81c7f711396963887e500dee201be4bb5
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon, organism-form,
    and subcellular organelle terms cannot substitute for associated environments;
    parent_habitats must be strictly broader across all contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.80220dc4d4, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["UBERON:0000029"], xrefs=[].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/hind_legs.yaml
  locator: Entire YAML
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.ca4882ca81", "label": "mammalian hindlimb
    lymph node", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "definition":
    "A lymph node located in the hindlimb of a non-human mammal (such as the popliteal
    or subiliac lymph node).", "parent_habitats": ["UBERON:0000029"]}'
  snapshot_sha256: 92f64b32540428e126f0d371ed83553b36e4f1429458c855dfde6753ccc7d088
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2076
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals > Lymphatic system > Lymph nodes > Forelegs", "depth": "5", "ecosystem":
    "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Lymph
    nodes", "ecosystem_type": "Lymphatic system", "gold_node_count": "1", "gold_node_ids":
    "gold.ecosystem:6764", "leaf_label": "Forelegs", "organism_count": "0", "specific_ecosystem":
    "Forelegs", "study_count": "0", "total_assertions": "0"}, "row": 2076}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 722,6513,12878
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: '[{"data": {"definition": "A limb of an animal used especially for supporting
    the body and for walking.", "deprecated": "", "directly_referenced": "FALSE",
    "label": "leg", "label_only": "FALSE", "ontology": "BTO", "synonyms": "", "term_id":
    "BTO:0000721"}, "row": 722}, {"data": {"definition": "A front leg.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "foreleg", "label_only": "FALSE",
    "ontology": "BTO", "synonyms": "", "term_id": "BTO:0006514"}, "row": 6513}, {"data":
    {"definition": "Any of the rounded masses of lymphoid tissue that are surrounded
    by a capsule of connective tissue, are distributed along the lymphatic vessels,
    and contain numerous lymphocytes which filter the flow of lymph.", "deprecated":
    "", "directly_referenced": "TRUE", "label": "lymph node", "label_only": "FALSE",
    "ontology": "UBERON", "synonyms": "lymph gland|nodus lymphaticus", "term_id":
    "UBERON:0000029"}, "row": 12878}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 463,464,4556,4557,10990
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: '[{"data": {"object": "BTO:0001729", "predicate": "rdfs:subClassOf", "subject":
    "BTO:0000721"}, "row": 463}, {"data": {"object": "BTO:0002345", "predicate": "rdfs:subClassOf",
    "subject": "BTO:0000721"}, "row": 464}, {"data": {"object": "BTO:0000721", "predicate":
    "rdfs:subClassOf", "subject": "BTO:0006514"}, "row": 4556}, {"data": {"object":
    "BTO:0000721", "predicate": "rdfs:subClassOf", "subject": "BTO:0006515"}, "row":
    4557}, {"data": {"object": "UBERON:0005057", "predicate": "rdfs:subClassOf", "subject":
    "UBERON:0000029"}, "row": 10990}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/lymph_node__7af26c8b.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: '{"identifier": "UBERON:0000029", "label": "lymph node", "grounding_status":
    "EXACT", "mapping_status": "REVIEWED", "definition": "Any of the rounded masses
    of lymphoid tissue that are surrounded by a capsule of connective tissue, are
    distributed along the lymphatic vessels, and contain numerous lymphocytes which
    filter the flow of lymph.", "parent_habitats": ["UBERON:0005057", "habitatmech:GOLD.a792be9b27",
    "habitatmech:GOLD.be39fe9a0e"], "synonyms": [{"synonym_text": "Lymph nodes", "synonym_type":
    "EXACT_SYNONYM", "source": "GOLD"}, {"synonym_text": "lymph gland", "synonym_type":
    "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text": "nodus lymphaticus", "synonym_type":
    "EXACT_SYNONYM", "source": "UBERON"}]}'
  snapshot_sha256: 2ad5c08889ffa33811bb6d9e2cf48891e13376d441f51fdacac76aa2456288b7
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'foreleg|BTO:0006514' reviews/structured/*/review.yaml curation/
    history/
  accessed_at: '2026-11-09T21:50:09Z'
  support: context_only
  summary: Structured-review traversal located Stage 4 predecessor bundle 20261109T181025Z-foreleg-record
    (linked via EPREV and related_reviews) and checked related cohort and ancestor
    reviews for reconciliation.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 7c82566b001f676eb0d3c9cc6c905f85a99b8bde.
- evidence_id: ETR
  kind: record_content
  reference: curation/term_requests.tsv
  locator: TSV line 678
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: '[[678, "habitatmech:GOLD.80220dc4d4\tmammalian forelimb lymph node\tUBERON:0000029\tlymph
    node\tA lymph node located in the forelimb of a non-human mammal (such as the
    axillary or superficial cervical lymph node).\tmammalian foreleg lymph node\tantigravity\t2026-11-09\tITEM
    curation #2334: GOLD ''Host-associated > Mammals > Lymphatic system > Lymph nodes
    > Forelegs'' denotes lymph nodes of the mammalian forelimb (PMID 29643885; DOI:10.3389/fimmu.2018.00682),
    parallel to sibling habitatmech:GOLD.ca4882ca81 (''mammalian hindlimb lymph node'').
    Path: Host-associated > Mammals > Lymphatic system > Lymph nodes > Forelegs\tREPLACE"]]'
  snapshot_sha256: 3703ae74d7565abdfb5a1fab47718b05c4fd02447b4ed60bbeb3bde65e1d8792
- evidence_id: EDEC
  kind: record_content
  reference: curation/decisions.tsv
  locator: TSV line 776
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: '[[776, "habitatmech:GOLD.80220dc4d4\tCONFIRM_UNGROUNDED\tUBERON:0000029\tlymph
    node\t\tantigravity\t2026-11-09\tITEM curation #2334: GOLD ''Host-associated >
    Mammals > Lymphatic system > Lymph nodes > Forelegs'' denotes lymph nodes of the
    mammalian forelimb (such as the axillary or superficial cervical/prescapular lymph
    node; PMID 29643885; DOI:10.3389/fimmu.2018.00682), parallel to sibling hind_legs.yaml
    (habitatmech:GOLD.ca4882ca81 ''mammalian hindlimb lymph node''), not the entire
    front leg (BTO:0006514 ''foreleg''). Keep the source concept minted under UBERON:0000029
    (''lymph node''). Path: Host-associated > Mammals > Lymphatic system > Lymph nodes
    > Forelegs\tITEM\tHOST_ASSOCIATED\tparent"]]'
  snapshot_sha256: 8e0c9ea50c453b9b0eb86e9a6cf246dbc188714ec7a8cc37b2918d5373e6d2ae
- evidence_id: ESYNS
  kind: record_content
  reference: curation/definition_source_label_exclusions.tsv
  locator: TSV line 4
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: '[[4, "habitatmech:GOLD.80220dc4d4\tForelegs\tmammalian forelimb lymph
    node\tantigravity\t2026-11-09\tReview #2334: Displaced GOLD source label ''Forelegs''
    in path ''Host-associated > Mammals > Lymphatic system > Lymph nodes > Forelegs''
    names the whole forelimb rather than the defined habitat ''mammalian forelimb
    lymph node''; suppress automatic exact-synonym retention while preserving verbatim
    source provenance."]]'
  snapshot_sha256: 84e5214713a21033312eb9c512fe38f44865662f934a4e679d45e827b16ff780
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261109T181025Z-foreleg-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: 1ff0d6b3fc34ac12a6f33203daa47c856f7672938fcd99bc761423f7e0e1f590
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_finger_to_free_living_state_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-09T21:50:09Z'
  support: supports
  summary: 'Exactly thirteen records differ from the counterfactual baseline across
    Issues #2334, #2335, and #2336.'
  snapshot_sha256: 495a506d77d0f3c2484e16b510c233a7c8b108ae96cba6b6346252c3a9d01bdb
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/decisions/2026-11-09T214500Z-antigravity-233401.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-09T21:50:09Z'
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
  - habitatmech:GOLD.80220dc4d4
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'habitatmech:GOLD.80220dc4d4: mammalian forelimb lymph node; UNGROUNDED/REVIEWED;
    parents ["UBERON:0000029"]. Replaced whole-limb BTO:0006514 (''foreleg'') exact
    grounding on habitatmech:GOLD.80220dc4d4 (''Host-associated > Mammals > Lymphatic
    system > Lymph nodes > Forelegs'') with ITEM-level CONFIRM_UNGROUNDED (target_id=UBERON:0000029
    ''lymph node'', relation=parent) in curation/decisions.tsv, defined ''mammalian
    forelimb lymph node'' under UBERON:0000029 (parent_mode REPLACE) in curation/term_requests.tsv,
    and excluded automatic retention of displaced source label ''Forelegs'' in curation/definition_source_label_exclusions.tsv
    (#2334). This resolves both the whole-limb identity mismatch and the limb parent
    collision (BTO:0000721 ''leg''), placing the record cleanly under UBERON:0000029
    (lymph node) alongside sibling Lymph nodes > Hind legs (habitatmech:GOLD.ca4882ca81).
    Both predecessor findings (F1 and F2) are resolved.'
  target_ids:
  - habitatmech:GOLD.80220dc4d4
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"count": 0, "source": "GOLD", "unit": null}]. Zero counts are omitted;
    unrelated parent counts are not combined.'
  target_ids:
  - habitatmech:GOLD.80220dc4d4
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
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
  - habitatmech:GOLD.80220dc4d4
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only
    review does not mutate generated records.
  target_ids:
  - habitatmech:GOLD.80220dc4d4
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
findings:
- finding_id: F1
  issue_key: foreleg-lymph-node-identity
  category: identity
  severity: blocker
  status: resolved
  certainty: confirmed
  title: Mammalian forelimb lymph node path is grounded to whole limb BTO:0006514
    (foreleg)
  description: GOLD path 'Host-associated > Mammals > Lymphatic system > Lymph nodes
    > Forelegs' (habitatmech:GOLD.80220dc4d4) denotes a lymph node of the mammalian
    forelimb (such as the axillary or superficial cervical lymph node, parallel to
    already-curated sibling hind_legs.yaml habitatmech:GOLD.ca4882ca81 'mammalian
    hindlimb lymph node'), not the entire front leg (BTO:0006514 foreleg, 'A front
    leg.'). Replace the GROUND decision on habitatmech:GOLD.80220dc4d4 in curation/decisions.tsv
    with CONFIRM_UNGROUNDED (object_id=UBERON:0000029, object_label=lymph node, relation=parent),
    author a curated definition for 'mammalian forelimb lymph node' under UBERON:0000029
    in curation/term_requests.tsv, exclude displaced source label 'Forelegs' in curation/definition_source_label_exclusions.tsv,
    and update data/habitats/PATHS.tsv.
  target_ids:
  - habitatmech:GOLD.80220dc4d4
  field_paths:
  - identifier
  - label
  - definition
  - grounding_status
  - parent_habitats
  - source_attestations
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: data/habitats/PATHS.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: blocker
  normalization_reason: Source path denoting a forelimb lymph node is grounded to
    the whole forelimb anatomical class BTO:0006514.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2334
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261109T181025Z-foreleg-record
    finding_id: F1
  disposition_reason: Updated habitatmech:GOLD.80220dc4d4 in curation/decisions.tsv
    from BTO:0006514 ('foreleg') to ITEM-level CONFIRM_UNGROUNDED (target_id=UBERON:0000029
    'lymph node', relation=parent), defined 'mammalian forelimb lymph node' under
    UBERON:0000029 (parent_mode REPLACE) in curation/term_requests.tsv, and added
    a guarded source-label exclusion for 'Forelegs' in curation/definition_source_label_exclusions.tsv
    (#2334).
- finding_id: F2
  issue_key: foreleg-lymph-node-parent-collision
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Grounding forelimb lymph node to BTO:0006514 (foreleg) asserts UBERON:0000029
    (lymph node) as a parent of foreleg
  description: Because habitatmech:GOLD.80220dc4d4 ('Host-associated > Mammals > Lymphatic
    system > Lymph nodes > Forelegs') is grounded to BTO:0006514 (foreleg), the generated
    record combines BTO subclass parent BTO:0000721 (leg) with GOLD path parent UBERON:0000029
    (lymph node), falsely asserting that a foreleg is a subtype of lymph node. Resolving
    F1 by ungrounding habitatmech:GOLD.80220dc4d4 to 'mammalian forelimb lymph node'
    under UBERON:0000029 eliminates this parent collision.
  target_ids:
  - habitatmech:GOLD.80220dc4d4
  field_paths:
  - parent_habitats
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
  - ESEARCH
  - ETR
  - EDEC
  - ESYNS
  - EPREV
  - ETEST
  - EHIST_G1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2334
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261109T181025Z-foreleg-record
    finding_id: F2
  disposition_reason: Resolved by un-grounding habitatmech:GOLD.80220dc4d4 from BTO:0006514
    and defining it under UBERON:0000029 (parent_mode REPLACE) in curation/term_requests.tsv
    (#2334), removing the whole-limb BTO subclass parent BTO:0000721 (leg) and aligning
    the record with sibling habitatmech:GOLD.ca4882ca81 ('mammalian hindlimb lymph
    node').
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
- Reconciles predecessor bundle 20261109T181025Z-foreleg-record with exact issue_key
  and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261109T181025Z-foreleg-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
