# Remediation review: empyema

- Review: 20261031T082511Z-empyema-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-31T08:20:00Z
- Finished UTC: 2026-10-31T08:25:11Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Replaced parent_class UBERON:0002402 (pleural cavity) with UBERON:0000175 (pleural effusion, parent_mode=REPLACE) in curation/term_requests.tsv, excluded the guarded GOLD Pleural cavity parent UBERON:0002402 via curation/gold_parent_exclusions.tsv (#2276), and excluded the bare disease label 'Empyema' from exact_synonym via curation/definition_source_label_exclusions.tsv (#2277). Identity, native status, and source observations are preserved. Both predecessor findings (F1 and F2) are resolved.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/empyema.yaml after bounded Cycle 3 Stage 5 remediation.

Selection: One of eleven repaired targets from the ear_discharge-through-empyema cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 73f5de1ffa3a7ab7e7bfb0e60149aef034c51aa0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.818c9729e2 | data/habitats/host_associated/empyema.yaml | generated | mammalian pleural empyema exudate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:25:36Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:25:42Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-31T08:22:00Z. No issues found; 854 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:25:49Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-31T08:22:10Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:26:07Z. validated 53 causal-graph curation file(s) with 53 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-31T08:22:15Z. term-request table is current (663 terms). |
| validate-products | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-26T08:27:01Z. OK_CANONICAL: 1194, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2063. All id&lt;-&gt;label pairs correspond. |
| pytest counterfactual review repairs | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-31T08:23:00Z. 2 passed; exact 11-record counterfactual diff verified. |
| curation-floor | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-31T08:23:05Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | habitatmech:GOLD.818c9729e2 | Completed 2026-10-31T08:23:30Z. rendered 3209 habitat pages, 743 redirect stubs, 8 categories, 688 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: habitatmech:GOLD.818c9729e2.

Individual schema, strict 24-target validation, 854 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 53 causal overlays, 663 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: habitatmech:GOLD.818c9729e2.

habitatmech:GOLD.818c9729e2: mammalian pleural empyema exudate; UNGROUNDED/REVIEWED; parents ["UBERON:0000175"]. Replaced parent_class UBERON:0002402 (pleural cavity) with UBERON:0000175 (pleural effusion, parent_mode=REPLACE) in curation/term_requests.tsv, excluded the guarded GOLD Pleural cavity parent UBERON:0002402 via curation/gold_parent_exclusions.tsv (#2276), and excluded the bare disease label 'Empyema' from exact_synonym via curation/definition_source_label_exclusions.tsv (#2277). Identity, native status, and source observations are preserved. Both predecessor findings (F1 and F2) are resolved.

### Source counts and retained ranking

quantity: supported. Targets: habitatmech:GOLD.818c9729e2.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: habitatmech:GOLD.818c9729e2.

Every predecessor finding preserves its stable issue_key and exact lineage; all predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: habitatmech:GOLD.818c9729e2.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / UNGROUNDED; this read-only review does not mutate generated records.

## Findings

### F1: Mammalian pleural empyema exudate is placed as a subclass of anatomical pleural cavity

major / resolved / confirmed; issue key: empyema-cavity-parent-grounding.

Update curation/term_requests.tsv for habitatmech:GOLD.818c9729e2 so parent_class is UBERON:0000175 (pleural effusion, or UBERON:0006314 bodily fluid) with parent_mode REPLACE, excluding the anatomical cavity parent UBERON:0002402 (pleural cavity).

Disposition: Updated parent_class in curation/term_requests.tsv for habitatmech:GOLD.818c9729e2 from UBERON:0002402 (pleural cavity) to UBERON:0000175 (pleural effusion) with parent_mode=REPLACE and added a guarded exclusion row for UBERON:0002402 in curation/gold_parent_exclusions.tsv (#2276).

### F2: Bare clinical condition label 'Empyema' is asserted as an exact exudate synonym

major / resolved / confirmed; issue key: empyema-disease-name-exact-synonym.

Remove bare 'Empyema' from exact_synonym in curation/term_requests.tsv for habitatmech:GOLD.818c9729e2 (keeping 'pleural empyema fluid') and add a guarded row in curation/definition_source_label_exclusions.tsv so 'Empyema' is scoped as RELATED_SYNONYM from GOLD rather than EXACT_SYNONYM.

Disposition: Removed bare 'Empyema' from exact_synonym in curation/term_requests.tsv (retaining 'pleural empyema fluid') and added a guarded row in curation/definition_source_label_exclusions.tsv (#2277) so 'Empyema' is emitted as RELATED_SYNONYM from GOLD.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/empyema.yaml; Entire YAML | supports | {"identifier": "habitatmech:GOLD.818c9729e2", "label": "mammalian pleural empyema exudate", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "parent_habitats": ["UBERON:0000175"], "synonyms": [{"synonym_text": "pleural empyema fluid", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6844", "source_label": "Empyema", "source_path": "Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-31T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM reassessment https://github.com/CultureBotAI/HabitatMech/issues/2276 and https://github.com/CultureBotAI/HabitatMech/issues/2277 : Defined mammalian pleural empyema exudate under UBERON:0000175 'pleural effusion' with parent_mode REPLACE (excluding anatomical cavity parent UBERON:0002402 'pleural cavity') and excluded bare disease label 'Empyema' from exact_synonyms; supported by pleural empyema 16S and metagenomic studies (PMID 30915025; DOI:10.1093/cid/ciy579). Path: Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema (source concept habitatmech:GOLD.818c9729e2)"}, {"timestamp": "2026-10-31T00:00:00Z", "curator": "antigravity", "action": "DEFINED", "changes": "Defined as 'mammalian pleural empyema exudate' under UBERON:0000175 'pleural effusion'. Defined mammalian pleural empyema exudate under UBERON:0000175 'pleural effusion' (parent_mode REPLACE) for GOLD path 'Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema'; supported by pleural empyema 16S and metagenomic studies (PMID 30915025; DOI:10.1093/cid/ciy579)."}, {"timestamp": "2026-10-31T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution UBERON:0002402 for habitatmech:GOLD.818c9729e2 (Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema). Review https://github.com/CultureBotAI/HabitatMech/issues/2276 : Eccrine sweat gland is an exocrine skin appendage, not the entire human integumentary system; eczematous skin lesion is a cutaneous lesion, not the whole skin organ; middle ear effusion is a fluid accumulation, not the middle ear cavity/organ; egg capsule is a secreted reproductive capsule, not the entire annelid reproductive system; insect egg is a reproductive unit, not an entire ootheca/egg mass; elastic cartilage is a cartilage tissue type, not the entire skeletal cartilage assemblage; pleural empyema exudate is a purulent exudate, not the pleural cavity. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.818c9729e2. Shared mapping endpoints #1398 remain separate."}, {"timestamp": "2026-10-31T00:00:00Z", "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted automatic retention of displaced source label 'Empyema' when defining habitatmech:GOLD.818c9729e2 as 'mammalian pleural empyema exudate'. Verbatim source attestations are preserved. Review https://github.com/CultureBotAI/HabitatMech/issues/2277 : The displaced label Empyema names the clinical condition without host or anatomical restriction outside Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema. Remove only the bare condition exact alias and suppress exact-alias fallback; preserve verbatim source provenance, definition, pleural empyema fluid synonym, genera and native status."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=habitatmech:GOLD.818c9729e2, grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["UBERON:0000175"]. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 2111 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Pleural cavity", "ecosystem_type": "Respiratory system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6844", "leaf_label": "Empyema", "organism_count": "0", "specific_ecosystem": "Empyema", "study_count": "0", "total_assertions": "0"}, "row": 2111}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 13152 | supports | [{"data": {"definition": "The fluid-filled cavity that lies between the visceral and parietal pleurae.", "deprecated": "", "directly_referenced": "TRUE", "label": "pleural cavity", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "cavitas pleuralis&#124;cavitum pleuralae&#124;cavitum pleurale", "term_id": "UBERON:0002402"}, "row": 13152}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 11387 | supports | [{"data": {"object": "UBERON:0035809", "predicate": "rdfs:subClassOf", "subject": "UBERON:0002402"}, "row": 11387}] |
| EDEC | curation/decisions.tsv; TSV rows 784 | supports | [{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.818c9729e2", "notes": "Defined mammalian pleural empyema exudate under UBERON:0002402 'pleural cavity'; supported by pleural empyema 16S and metagenomic studies (PMID 30915025).", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "row": 784}] |
| ETR | curation/term_requests.tsv; TSV line 600 | supports | [[600, "habitatmech:GOLD.818c9729e2\tmammalian pleural empyema exudate\tUBERON:0000175\tpleural effusion\tA pleural effusion which consists of purulent exudate accumulated within the pleural cavity of a mammal as a result of bacterial or fungal pleural infection.\tpleural empyema fluid\tantigravity\t2026-10-31\tDefined mammalian pleural empyema exudate under UBERON:0000175 'pleural effusion' (parent_mode REPLACE) for GOLD path 'Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema'; supported by pleural empyema 16S and metagenomic studies (PMID 30915025; DOI:10.1093/cid/ciy579).\tREPLACE"]] |
| EP1 | data/habitats/host_associated/pleural_cavity.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": "The fluid-filled cavity that lies between the visceral and parietal pleurae.", "grounding_status": "EXACT", "identifier": "UBERON:0002402", "label": "pleural cavity", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0035809", "habitatmech:GOLD.e36ba981d1", "habitatmech:GOLD.fac4f63f3b"], "source_attestations": [{"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6302", "source_label": "Pleural space/cavity", "source_path": "Host-associated &gt; Mammals: Human &gt; Respiratory system &gt; Pleural space/cavity"}, {"mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:6840", "source_label": "Pleural cavity", "source_path": "Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'empyema&#124;habitatmech:GOLD.818c9729e2' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal verified no prior target review bundle exists for this record; curation and history tables were inspected for all matching rows. |
| EPREV | reviews/structured/20261026T083033Z-empyema-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_ear_discharge_to_empyema_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly eleven records differ from the counterfactual baseline across Issues #2276 and #2277. |
| EPARENTS | curation/gold_parent_exclusions.tsv; TSV line 9 | supports | [[9, "habitatmech:GOLD.818c9729e2\tHost-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema\tUBERON:0002402\tantigravity\t2026-10-31\tReview https://github.com/CultureBotAI/HabitatMech/issues/2276 : Eccrine sweat gland is an exocrine skin appendage, not the entire human integumentary system; eczematous skin lesion is a cutaneous lesion, not the whole skin organ; middle ear effusion is a fluid accumulation, not the middle ear cavity/organ; egg capsule is a secreted reproductive capsule, not the entire annelid reproductive system; insect egg is a reproductive unit, not an entire ootheca/egg mass; elastic cartilage is a cartilage tissue type, not the entire skeletal cartilage assemblage; pleural empyema exudate is a purulent exudate, not the pleural cavity. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.818c9729e2. Shared mapping endpoints #1398 remain separate."]] |
| EHIST_G1 | history/other/gold_parent_exclusions/2026-10-31T081500Z-antigravity-227601.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2276 recorded and validated. |
| ESYNS | curation/definition_source_label_exclusions.tsv; TSV line 8 | supports | [[8, "habitatmech:GOLD.818c9729e2\tEmpyema\tmammalian pleural empyema exudate\tantigravity\t2026-10-31\tReview https://github.com/CultureBotAI/HabitatMech/issues/2277 : The displaced label Empyema names the clinical condition without host or anatomical restriction outside Host-associated &gt; Mammals &gt; Respiratory system &gt; Pleural cavity &gt; Empyema. Remove only the bare condition exact alias and suppress exact-alias fallback; preserve verbatim source provenance, definition, pleural empyema fluid synonym, genera and native status."]] |
| EHIST_G2 | history/other/definition_source_label_exclusions/2026-10-31T081510Z-antigravity-227701.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2277 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,063 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 73f5de1ffa3a7ab7e7bfb0e60149aef034c51aa0; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261026T083033Z-empyema-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261031T082511Z-empyema-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: empyema'
started_at: '2026-10-31T08:20:00Z'
finished_at: '2026-10-31T08:25:11Z'
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
summary: Replaced parent_class UBERON:0002402 (pleural cavity) with UBERON:0000175
  (pleural effusion, parent_mode=REPLACE) in curation/term_requests.tsv, excluded
  the guarded GOLD Pleural cavity parent UBERON:0002402 via curation/gold_parent_exclusions.tsv
  (#2276), and excluded the bare disease label 'Empyema' from exact_synonym via curation/definition_source_label_exclusions.tsv
  (#2277). Identity, native status, and source observations are preserved. Both predecessor
  findings (F1 and F2) are resolved.
source:
  git_revision: 73f5de1ffa3a7ab7e7bfb0e60149aef034c51aa0
  state: working_tree
  inputs:
  - path: curation/decisions.tsv
    sha256: dea9f54c4f37043299ec911820c1ca9f552a913881bd8ceefef18b6140ed5031
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: f6d6e83963d272c057f795d8a5518e2d117b4a431c75c08b501eed13d170efa1
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 12380d3ee22e773ff067d372204f74165cf5cfa77973ad9565162bbcd383a797
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: 76e2e5b58191022cd20054836efccdbec3f4aee24903c73c68519908af4943d0
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/empyema.yaml
    sha256: e4ddd9f34e92f17a446559db259ed653509346da5f926d9ed988ddf4992182b3
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
  - path: history/other/definition_source_label_exclusions/2026-10-31T081510Z-antigravity-227701.yaml
    sha256: f25a4321c5b99cb3e6486d2be3e42cfc6a9762f7500163d90fd2957a3a6cda57
    role: context
  - path: history/other/gold_parent_exclusions/2026-10-31T081500Z-antigravity-227601.yaml
    sha256: 604c2de8bb4c0383bddd0bd8234b0153757b30db8ec49d35d02db80437caa136
    role: context
  - path: reviews/structured/20261026T083033Z-empyema-record/review.yaml
    sha256: b653ef7ce6adf416d3bbb80ad5b8500d06bfd86e99d88333b215bad3633d1ec7
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_ear_discharge_to_empyema_review_repairs.py
    sha256: e6ee4c56690b2018f4f02e84d445c93c30c79a319c93461ccb5674e1f51d26c8
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
  description: Full current target assessment and explicit disposition of every baseline
    finding on data/habitats/host_associated/empyema.yaml after bounded Cycle 3 Stage
    5 remediation.
  selection: One of eleven repaired targets from the ear_discharge-through-empyema
    cohort.
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
  summary: Completed 2026-10-31T08:22:00Z. No issues found; 854 history record(s)
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
  summary: 'Completed 2026-10-31T08:22:10Z. expected 3209 records, found 3209 on disk;
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
  summary: Completed 2026-10-31T08:22:15Z. term-request table is current (663 terms).
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
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_ear_discharge_to_empyema_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.818c9729e2
  summary: Completed 2026-10-31T08:23:00Z. 2 passed; exact 11-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2276 and #2277.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.818c9729e2
  summary: Completed 2026-10-31T08:23:05Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.818c9729e2
  summary: Completed 2026-10-31T08:23:30Z. rendered 3209 habitat pages, 743 redirect
    stubs, 8 categories, 688 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/empyema.yaml
  locator: Entire YAML
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.818c9729e2", "label": "mammalian pleural
    empyema exudate", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "parent_habitats": ["UBERON:0000175"], "synonyms": [{"synonym_text": "pleural
    empyema fluid", "synonym_type": "EXACT_SYNONYM", "source": "HabitatMech curation"}],
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6844",
    "source_label": "Empyema", "source_path": "Host-associated > Mammals > Respiratory
    system > Pleural cavity > Empyema"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp":
    "2026-10-31T00:00:00Z", "curator": "antigravity", "action": "CONFIRM_UNGROUNDED",
    "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM reassessment
    https://github.com/CultureBotAI/HabitatMech/issues/2276 and https://github.com/CultureBotAI/HabitatMech/issues/2277
    : Defined mammalian pleural empyema exudate under UBERON:0000175 ''pleural effusion''
    with parent_mode REPLACE (excluding anatomical cavity parent UBERON:0002402 ''pleural
    cavity'') and excluded bare disease label ''Empyema'' from exact_synonyms; supported
    by pleural empyema 16S and metagenomic studies (PMID 30915025; DOI:10.1093/cid/ciy579).
    Path: Host-associated > Mammals > Respiratory system > Pleural cavity > Empyema
    (source concept habitatmech:GOLD.818c9729e2)"}, {"timestamp": "2026-10-31T00:00:00Z",
    "curator": "antigravity", "action": "DEFINED", "changes": "Defined as ''mammalian
    pleural empyema exudate'' under UBERON:0000175 ''pleural effusion''. Defined mammalian
    pleural empyema exudate under UBERON:0000175 ''pleural effusion'' (parent_mode
    REPLACE) for GOLD path ''Host-associated > Mammals > Respiratory system > Pleural
    cavity > Empyema''; supported by pleural empyema 16S and metagenomic studies (PMID
    30915025; DOI:10.1093/cid/ciy579)."}, {"timestamp": "2026-10-31T00:00:00Z", "curator":
    "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path
    parent contribution UBERON:0002402 for habitatmech:GOLD.818c9729e2 (Host-associated
    > Mammals > Respiratory system > Pleural cavity > Empyema). Review https://github.com/CultureBotAI/HabitatMech/issues/2276
    : Eccrine sweat gland is an exocrine skin appendage, not the entire human integumentary
    system; eczematous skin lesion is a cutaneous lesion, not the whole skin organ;
    middle ear effusion is a fluid accumulation, not the middle ear cavity/organ;
    egg capsule is a secreted reproductive capsule, not the entire annelid reproductive
    system; insect egg is a reproductive unit, not an entire ootheca/egg mass; elastic
    cartilage is a cartilage tissue type, not the entire skeletal cartilage assemblage;
    pleural empyema exudate is a purulent exudate, not the pleural cavity. Exclude
    only exact guarded GOLD source-path contributions, preserving independent genera
    and all source observations. Exact target habitatmech:GOLD.818c9729e2. Shared
    mapping endpoints #1398 remain separate."}, {"timestamp": "2026-10-31T00:00:00Z",
    "curator": "antigravity", "action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted
    automatic retention of displaced source label ''Empyema'' when defining habitatmech:GOLD.818c9729e2
    as ''mammalian pleural empyema exudate''. Verbatim source attestations are preserved.
    Review https://github.com/CultureBotAI/HabitatMech/issues/2277 : The displaced
    label Empyema names the clinical condition without host or anatomical restriction
    outside Host-associated > Mammals > Respiratory system > Pleural cavity > Empyema.
    Remove only the bare condition exact alias and suppress exact-alias fallback;
    preserve verbatim source provenance, definition, pleural empyema fluid synonym,
    genera and native status."}]}'
  snapshot_sha256: e4ddd9f34e92f17a446559db259ed653509346da5f926d9ed988ddf4992182b3
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: Seed generator produces identifier=habitatmech:GOLD.818c9729e2, grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["UBERON:0000175"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 2111
  accessed_at: '2026-10-31T08:25:11Z'
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
  accessed_at: '2026-10-31T08:25:11Z'
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
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0035809", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0002402"}, "row": 11387}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV rows 784
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: '[{"data": {"category": "", "curator": "antigravity", "date": "2026-10-17",
    "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.818c9729e2",
    "notes": "Defined mammalian pleural empyema exudate under UBERON:0002402 ''pleural
    cavity''; supported by pleural empyema 16S and metagenomic studies (PMID 30915025).",
    "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"},
    "row": 784}]'
  snapshot_sha256: dea9f54c4f37043299ec911820c1ca9f552a913881bd8ceefef18b6140ed5031
- evidence_id: ETR
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV line 600
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: '[[600, "habitatmech:GOLD.818c9729e2\tmammalian pleural empyema exudate\tUBERON:0000175\tpleural
    effusion\tA pleural effusion which consists of purulent exudate accumulated within
    the pleural cavity of a mammal as a result of bacterial or fungal pleural infection.\tpleural
    empyema fluid\tantigravity\t2026-10-31\tDefined mammalian pleural empyema exudate
    under UBERON:0000175 ''pleural effusion'' (parent_mode REPLACE) for GOLD path
    ''Host-associated > Mammals > Respiratory system > Pleural cavity > Empyema'';
    supported by pleural empyema 16S and metagenomic studies (PMID 30915025; DOI:10.1093/cid/ciy579).\tREPLACE"]]'
  snapshot_sha256: 76e2e5b58191022cd20054836efccdbec3f4aee24903c73c68519908af4943d0
- evidence_id: EP1
  kind: record_content
  reference: data/habitats/host_associated/pleural_cavity.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-10-31T08:25:11Z'
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
  accessed_at: '2026-10-31T08:25:11Z'
  support: context_only
  summary: Structured-review traversal verified no prior target review bundle exists
    for this record; curation and history tables were inspected for all matching rows.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 1a40d0958114e6e3facd148ccec6197fa4dd679c.
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261026T083033Z-empyema-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: b653ef7ce6adf416d3bbb80ad5b8500d06bfd86e99d88333b215bad3633d1ec7
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_ear_discharge_to_empyema_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: 'Exactly eleven records differ from the counterfactual baseline across
    Issues #2276 and #2277.'
  snapshot_sha256: e6ee4c56690b2018f4f02e84d445c93c30c79a319c93461ccb5674e1f51d26c8
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: TSV line 9
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: '[[9, "habitatmech:GOLD.818c9729e2\tHost-associated > Mammals > Respiratory
    system > Pleural cavity > Empyema\tUBERON:0002402\tantigravity\t2026-10-31\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2276 : Eccrine sweat gland
    is an exocrine skin appendage, not the entire human integumentary system; eczematous
    skin lesion is a cutaneous lesion, not the whole skin organ; middle ear effusion
    is a fluid accumulation, not the middle ear cavity/organ; egg capsule is a secreted
    reproductive capsule, not the entire annelid reproductive system; insect egg is
    a reproductive unit, not an entire ootheca/egg mass; elastic cartilage is a cartilage
    tissue type, not the entire skeletal cartilage assemblage; pleural empyema exudate
    is a purulent exudate, not the pleural cavity. Exclude only exact guarded GOLD
    source-path contributions, preserving independent genera and all source observations.
    Exact target habitatmech:GOLD.818c9729e2. Shared mapping endpoints #1398 remain
    separate."]]'
  snapshot_sha256: 12380d3ee22e773ff067d372204f74165cf5cfa77973ad9565162bbcd383a797
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-10-31T081500Z-antigravity-227601.yaml
  locator: Complete curation session history event
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: 'Authorized curation event for Issue #2276 recorded and validated.'
  snapshot_sha256: 604c2de8bb4c0383bddd0bd8234b0153757b30db8ec49d35d02db80437caa136
- evidence_id: ESYNS
  kind: record_content
  reference: curation/definition_source_label_exclusions.tsv
  locator: TSV line 8
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: '[[8, "habitatmech:GOLD.818c9729e2\tEmpyema\tmammalian pleural empyema
    exudate\tantigravity\t2026-10-31\tReview https://github.com/CultureBotAI/HabitatMech/issues/2277
    : The displaced label Empyema names the clinical condition without host or anatomical
    restriction outside Host-associated > Mammals > Respiratory system > Pleural cavity
    > Empyema. Remove only the bare condition exact alias and suppress exact-alias
    fallback; preserve verbatim source provenance, definition, pleural empyema fluid
    synonym, genera and native status."]]'
  snapshot_sha256: f6d6e83963d272c057f795d8a5518e2d117b4a431c75c08b501eed13d170efa1
- evidence_id: EHIST_G2
  kind: record_content
  reference: history/other/definition_source_label_exclusions/2026-10-31T081510Z-antigravity-227701.yaml
  locator: Complete curation session history event
  accessed_at: '2026-10-31T08:25:11Z'
  support: supports
  summary: 'Authorized curation event for Issue #2277 recorded and validated.'
  snapshot_sha256: f25a4321c5b99cb3e6486d2be3e42cfc6a9762f7500163d90fd2957a3a6cda57
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 854 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 53 causal
    overlays, 663 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
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
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - ESYNS
  - EHIST_G2
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'habitatmech:GOLD.818c9729e2: mammalian pleural empyema exudate; UNGROUNDED/REVIEWED;
    parents ["UBERON:0000175"]. Replaced parent_class UBERON:0002402 (pleural cavity)
    with UBERON:0000175 (pleural effusion, parent_mode=REPLACE) in curation/term_requests.tsv,
    excluded the guarded GOLD Pleural cavity parent UBERON:0002402 via curation/gold_parent_exclusions.tsv
    (#2276), and excluded the bare disease label ''Empyema'' from exact_synonym via
    curation/definition_source_label_exclusions.tsv (#2277). Identity, native status,
    and source observations are preserved. Both predecessor findings (F1 and F2) are
    resolved.'
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
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - ESYNS
  - EHIST_G2
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
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - ESYNS
  - EHIST_G2
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: supported
  summary: Every predecessor finding preserves its stable issue_key and exact lineage;
    all predecessor findings in this target scope are resolved.
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
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - ESYNS
  - EHIST_G2
- assessment_id: A5
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
  - ERULE
  - ESCHEMA
  - ESEED
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - ETR
  - EP1
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - ESYNS
  - EHIST_G2
findings:
- finding_id: F1
  issue_key: empyema-cavity-parent-grounding
  category: grounding
  severity: major
  status: resolved
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
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - ESYNS
  - EHIST_G2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2276
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261026T083033Z-empyema-record
    finding_id: F1
  disposition_reason: Updated parent_class in curation/term_requests.tsv for habitatmech:GOLD.818c9729e2
    from UBERON:0002402 (pleural cavity) to UBERON:0000175 (pleural effusion) with
    parent_mode=REPLACE and added a guarded exclusion row for UBERON:0002402 in curation/gold_parent_exclusions.tsv
    (#2276).
- finding_id: F2
  issue_key: empyema-disease-name-exact-synonym
  category: nomenclature
  severity: major
  status: resolved
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
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - ESYNS
  - EHIST_G2
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
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2277
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261026T083033Z-empyema-record
    finding_id: F2
  disposition_reason: Removed bare 'Empyema' from exact_synonym in curation/term_requests.tsv
    (retaining 'pleural empyema fluid') and added a guarded row in curation/definition_source_label_exclusions.tsv
    (#2277) so 'Empyema' is emitted as RELATED_SYNONYM from GOLD.
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
- Saved against working-tree repairs atop main commit 73f5de1ffa3a7ab7e7bfb0e60149aef034c51aa0;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261026T083033Z-empyema-record with exact issue_key
  and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261026T083033Z-empyema-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
