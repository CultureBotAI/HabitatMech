# Remediation review: external_genitalia

- Review: 20261107T050003Z-external_genitalia-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-07T04:55:00Z
- Finished UTC: 2026-11-07T05:00:03Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed the guarded GOLD whole-system context-parent contributions habitatmech:GOLD.29feb6867b and habitatmech:GOLD.abc827a582 (Reproductive system) for source concepts habitatmech:GOLD.2ab65bac9e and habitatmech:GOLD.97989ecf5e via curation/gold_parent_exclusions.tsv (#2304), preserving broader ontology parent UBERON:0003133 (reproductive organ); updated curation/decisions.tsv for habitatmech:GOLD.97989ecf5e from EXACT to CLOSE so 'External genitalia/Vulva' is emitted as RELATED_SYNONYM (skos:closeMatch) and added an item-level REVIEW row for habitatmech:GOLD.2ab65bac9e so UBERON:0004176 achieves mapping_status REVIEWED (#2305). Both predecessor findings (F1 and F2) are resolved.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding on data/habitats/host_associated/external_genitalia.yaml after bounded Cycle 6 Stage 5 remediation.

Selection: One of twenty-two repaired targets from the excretory_system__22ee753c-through-fecal cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 30fbe25f4c539ad6266dae7680d21e451caf6e40.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0004176 | data/habitats/host_associated/external_genitalia.yaml | generated | external genitalia |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | UBERON:0004176 | Completed 2026-11-07T04:58:12Z. No issues found. |
| validate-strict | passed | True | UBERON:0004176 | Completed 2026-11-07T04:58:18Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | UBERON:0004176 | Completed 2026-11-07T04:59:00Z. No issues found; 868 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | UBERON:0004176 | Completed 2026-11-07T04:59:05Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | UBERON:0004176 | Completed 2026-11-07T04:59:10Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | UBERON:0004176 | Completed 2026-11-07T04:59:12Z. validated 83 causal-graph curation file(s) with 83 graph(s). |
| term-requests-check | passed | True | UBERON:0004176 | Completed 2026-11-07T04:59:15Z. term-request table is current (671 terms). |
| validate-products | passed | True | UBERON:0004176 | Completed 2026-11-07T04:59:20Z. OK_CANONICAL: 1203, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2084. All id&lt;-&gt;label pairs correspond. |
| pytest counterfactual review repairs | passed | True | UBERON:0004176 | Completed 2026-11-07T04:59:30Z. 2 passed; exact 22-record counterfactual diff verified. |
| curation-floor | passed | True | UBERON:0004176 | Completed 2026-11-07T04:59:35Z. Floor satisfied across all 13 metrics. |
| render-check | passed | True | UBERON:0004176 | Completed 2026-11-07T04:59:50Z. rendered 3209 habitat pages, 750 redirect stubs, 8 categories, 696 term requests; pages/ is in step with the corpus. |

## Scientific And Domain Assessments

### Native validity and reproduction after bounded remediation

schema: supported. Targets: UBERON:0004176.

Individual schema, strict 24-target validation, 868 history records, 14 inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 83 causal overlays, 671 term requests, curation floor, site parity, and counterfactual regression tests passed.

### Identity, definition, hierarchy and aliases

identity: supported. Targets: UBERON:0004176.

UBERON:0004176: external genitalia; EXACT/REVIEWED; parents ["UBERON:0003133"]. Removed the guarded GOLD whole-system context-parent contributions habitatmech:GOLD.29feb6867b and habitatmech:GOLD.abc827a582 (Reproductive system) for source concepts habitatmech:GOLD.2ab65bac9e and habitatmech:GOLD.97989ecf5e via curation/gold_parent_exclusions.tsv (#2304), preserving broader ontology parent UBERON:0003133 (reproductive organ); updated curation/decisions.tsv for habitatmech:GOLD.97989ecf5e from EXACT to CLOSE so 'External genitalia/Vulva' is emitted as RELATED_SYNONYM (skos:closeMatch) and added an item-level REVIEW row for habitatmech:GOLD.2ab65bac9e so UBERON:0004176 achieves mapping_status REVIEWED (#2305). Both predecessor findings (F1 and F2) are resolved.

### Source counts and retained ranking

quantity: supported. Targets: UBERON:0004176.

Exact raw rows reproduce emitted counts/units, labels, scores, ranks, and pools: [{"source": "GOLD", "count": 10, "unit": "ORGANISM"}, {"source": "GOLD", "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts are not combined.

### Predecessor finding reconciliation

representation: supported. Targets: UBERON:0004176.

Every predecessor finding preserves its stable issue_key and exact lineage. All predecessor findings in this target scope are resolved.

### Parameters, mechanisms and native status

completeness: supported. Targets: UBERON:0004176.

Missing optional parameters/graphs are not evidence deficits. Full source decisions and executed routes reproduce REVIEWED / EXACT; this read-only review does not mutate generated records.

## Findings

### F1: External genitalia retains mammalian and human Reproductive system GOLD parents as superclasses

major / resolved / confirmed; issue key: external-genitalia-context-parent.

Add exclusion rows in curation/gold_parent_exclusions.tsv for source identifier habitatmech:GOLD.2ab65bac9e ('Host-associated &gt; Mammals &gt; Reproductive system &gt; External genitalia', excluding parent_id habitatmech:GOLD.29feb6867b) and source identifier habitatmech:GOLD.97989ecf5e ('Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; External genitalia/Vulva', excluding parent_id habitatmech:GOLD.abc827a582) on exact target UBERON:0004176, preserving ontology parent UBERON:0003133 (reproductive organ).

Disposition: Excluded only the guarded GOLD whole-system context-parent contributions habitatmech:GOLD.29feb6867b and habitatmech:GOLD.abc827a582 (Reproductive system) for source concepts habitatmech:GOLD.2ab65bac9e and habitatmech:GOLD.97989ecf5e in curation/gold_parent_exclusions.tsv (#2304), preserving broader ontology parent UBERON:0003133 (reproductive organ).

### F2: External genitalia promotes slash-disjunction 'External genitalia/Vulva' as an exact synonym and lacks item-level review on its second GOLD path

major / resolved / confirmed; issue key: external-genitalia-vulva-exact-synonym.

Update curation/decisions.tsv row 901 for habitatmech:GOLD.97989ecf5e ('Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; External genitalia/Vulva', object_id UBERON:0004176) from grounding_status EXACT to CLOSE so the slash-disjunction label 'External genitalia/Vulva' is emitted with scope RELATED_SYNONYM (skos:closeMatch) rather than EXACT_SYNONYM, and add an item-level REVIEW decision row (EXACT -&gt; UBERON:0004176) for habitatmech:GOLD.2ab65bac9e ('Host-associated &gt; Mammals &gt; Reproductive system &gt; External genitalia') so both feeding source concepts are reviewed.

Disposition: Updated curation/decisions.tsv for habitatmech:GOLD.97989ecf5e (External genitalia/Vulva) from EXACT to CLOSE and added an item-level REVIEW row for habitatmech:GOLD.2ab65bac9e (External genitalia) (#2305) so 'External genitalia/Vulva' is emitted with synonym_type RELATED_SYNONYM (skos:closeMatch) and external_genitalia.yaml achieves mapping_status REVIEWED.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/external_genitalia.yaml; Entire YAML | supports | {"identifier": "UBERON:0004176", "label": "external genitalia", "grounding_status": "EXACT", "mapping_status": "REVIEWED", "parent_habitats": ["UBERON:0003133"], "synonyms": [{"synonym_text": "External genitalia/Vulva", "synonym_type": "RELATED_SYNONYM", "source": "GOLD"}, {"synonym_text": "external reproductive organ", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text": "external sex organ", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6245", "source_label": "External genitalia/Vulva", "source_path": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; External genitalia/Vulva", "mapping_predicate": "skos:closeMatch", "assertion_count": 10, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "GOLD", "source_id": "gold.ecosystem:7634", "source_label": "External genitalia", "source_path": "Host-associated &gt; Mammals &gt; Reproductive system &gt; External genitalia", "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: EXACT."}, {"timestamp": "2026-10-07T00:00:00Z", "curator": "seed_from_sources", "action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained GOLD label 'External genitalia/Vulva' as RELATED_SYNONYM: a CLOSE source mapping does not establish exact lexical equivalence. Independent ontology synonyms and verbatim attestations are preserved (#1459)."}, {"timestamp": "2026-11-06T00:00:00Z", "curator": "antigravity", "action": "REVIEW", "changes": "Reviewed and endorsed the seeder's own resolution. Multi-source review pass (https://github.com/CultureBotAI/HabitatMech/issues/2305): GOLD 'Host-associated &gt; Mammals &gt; Reproductive system &gt; External genitalia' matches UBERON:0004176 'external genitalia' directly; reviewed at ITEM depth so both source concepts feeding UBERON:0004176 are reviewed. (source concept habitatmech:GOLD.2ab65bac9e)"}, {"timestamp": "2026-11-06T00:00:00Z", "curator": "antigravity", "action": "GROUND", "changes": "Grounded to UBERON:0004176 'external genitalia' (CLOSE). Slash-disjunction label 'External genitalia/Vulva' combines sex-neutral external genitalia (UBERON:0004176) with female vulva; CLOSE preserves the merged grounding while emitting 'External genitalia/Vulva' as RELATED_SYNONYM (https://github.com/CultureBotAI/HabitatMech/issues/2305). Path: Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; External genitalia/Vulva (source concept habitatmech:GOLD.97989ecf5e)"}, {"timestamp": "2026-11-06T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.29feb6867b for habitatmech:GOLD.2ab65bac9e (Host-associated &gt; Mammals &gt; Reproductive system &gt; External genitalia). Review https://github.com/CultureBotAI/HabitatMech/issues/2304 : Crustacean and annelid excretory system are organ systems, not subtypes of the whole crustacean- or annelid-associated host environment; external genitalia is an anatomical reproductive organ structure, not a subtype of the entire mammalian or human reproductive system; external soft tissue zone is a soft-tissue anatomical region, not a subtype of the mammalian Multiple systems GOLD classification bucket; mammalian, piscine, and human eye are sense organs and ciliary body and vitreous chamber are intraocular structures/compartments, not subtypes of the entire visual system; human and mammalian fallopian tube are oviductal reproductive organs, not subtypes of the entire reproductive system; mammalian and human fascia are connective tissue sheets, not subtypes of the host-scoped connective tissue assemblage; insect fat body is an adipose organ/tissue, not a subtype of the whole insect-associated environment; feather is an avian epidermal appendage, not a subtype of the whole avian skin organ. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target UBERON:0004176. Shared mapping endpoints #1398 remain separate."}, {"timestamp": "2026-11-06T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.abc827a582 for habitatmech:GOLD.97989ecf5e (Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; External genitalia/Vulva). Review https://github.com/CultureBotAI/HabitatMech/issues/2304 : Crustacean and annelid excretory system are organ systems, not subtypes of the whole crustacean- or annelid-associated host environment; external genitalia is an anatomical reproductive organ structure, not a subtype of the entire mammalian or human reproductive system; external soft tissue zone is a soft-tissue anatomical region, not a subtype of the mammalian Multiple systems GOLD classification bucket; mammalian, piscine, and human eye are sense organs and ciliary body and vitreous chamber are intraocular structures/compartments, not subtypes of the entire visual system; human and mammalian fallopian tube are oviductal reproductive organs, not subtypes of the entire reproductive system; mammalian and human fascia are connective tissue sheets, not subtypes of the host-scoped connective tissue assemblage; insect fat body is an adipose organ/tissue, not a subtype of the whole insect-associated environment; feather is an avian epidermal appendage, not a subtype of the whole avian skin organ. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target UBERON:0004176. Shared mapping endpoints #1398 remain separate."}]} |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator produces identifier=UBERON:0004176, grounding_status=EXACT, mapping_status=REVIEWED, parent_habitats=["UBERON:0003133"]. |
| ESIB1 | data/habitats/host_associated/ethmoid_bone.yaml; Entire YAML | supports | Sibling GOLD-attested anatomical record UBERON:0001679 where grounding_status was updated from EXACT to CLOSE in curation/decisions.tsv (#2296) so a non-equivalent GOLD source label is retained as RELATED_SYNONYM (skos:closeMatch) rather than EXACT_SYNONYM. |
| EGOLD | data/raw/gold_ecosystem_paths.tsv; TSV rows 528,2094 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; External genitalia/Vulva", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype": "External genitalia/Vulva", "ecosystem_type": "Reproductive system", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:6245&#124;gold.ecosystem:6246", "leaf_label": "External genitalia/Vulva", "organism_count": "10", "specific_ecosystem": "", "study_count": "0", "total_assertions": "10"}, "row": 528}, {"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals &gt; Reproductive system &gt; External genitalia", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "External genitalia", "ecosystem_type": "Reproductive system", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:7634&#124;gold.ecosystem:7635", "leaf_label": "External genitalia", "organism_count": "0", "specific_ecosystem": "", "study_count": "0", "total_assertions": "0"}, "row": 2094}] |
| EONT | data/raw/ontology_terms.tsv; TSV rows 13183,13229 | supports | [{"data": {"definition": "An organ involved in reproduction.", "deprecated": "", "directly_referenced": "FALSE", "label": "reproductive organ", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "genital organ&#124;genitalia&#124;reproductive system organ&#124;sex organ", "term_id": "UBERON:0003133"}, "row": 13183}, {"data": {"definition": "The external genitalia are the outer sex organs, such as the penis or vulva in mammals.", "deprecated": "", "directly_referenced": "TRUE", "label": "external genitalia", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "external genitalia&#124;external reproductive organ&#124;external sex organ", "term_id": "UBERON:0004176"}, "row": 13229}] |
| EONTEDGE | data/raw/ontology_subclass_edges.tsv; TSV rows 11113,11426,11427,11428,11429,11483 | supports | [{"data": {"object": "UBERON:0003133", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000991"}, "row": 11113}, {"data": {"object": "UBERON:0000062", "predicate": "rdfs:subClassOf", "subject": "UBERON:0003133"}, "row": 11426}, {"data": {"object": "UBERON:0005156", "predicate": "rdfs:subClassOf", "subject": "UBERON:0003133"}, "row": 11427}, {"data": {"object": "UBERON:0003133", "predicate": "rdfs:subClassOf", "subject": "UBERON:0003134"}, "row": 11428}, {"data": {"object": "UBERON:0003133", "predicate": "rdfs:subClassOf", "subject": "UBERON:0003135"}, "row": 11429}, {"data": {"object": "UBERON:0003133", "predicate": "rdfs:subClassOf", "subject": "UBERON:0004176"}, "row": 11483}] |
| EDEC | curation/decisions.tsv; TSV line 349, 902 | supports | [[349, "habitatmech:GOLD.2ab65bac9e\tREVIEW\t\t\t\tantigravity\t2026-11-06\tMulti-source review pass (https://github.com/CultureBotAI/HabitatMech/issues/2305): GOLD 'Host-associated &gt; Mammals &gt; Reproductive system &gt; External genitalia' matches UBERON:0004176 'external genitalia' directly; reviewed at ITEM depth so both source concepts feeding UBERON:0004176 are reviewed.\tITEM\t\t"], [902, "habitatmech:GOLD.97989ecf5e\tGROUND\tUBERON:0004176\texternal genitalia\tCLOSE\tantigravity\t2026-11-06\tSlash-disjunction label 'External genitalia/Vulva' combines sex-neutral external genitalia (UBERON:0004176) with female vulva; CLOSE preserves the merged grounding while emitting 'External genitalia/Vulva' as RELATED_SYNONYM (https://github.com/CultureBotAI/HabitatMech/issues/2305). Path: Host-associated &gt; Mammals: Human &gt; Reproductive system &gt; External genitalia/Vulva\tITEM\t\t"]] |
| EP2 | data/habitats/host_associated/reproductive_system__637f205f.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.29feb6867b", "label": "Reproductive system", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000990", "habitatmech:GOLD.e889967f4f"], "source_attestations": [{"assertion_count": 58, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3580", "source_label": "Reproductive system", "source_path": "Host-associated &gt; Mammals &gt; Reproductive system"}]} |
| EP3 | data/habitats/host_associated/reproductive_system__74cf1790.yaml; Direct-parent identity, definition, hierarchy and source scope | supports | {"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.abc827a582", "label": "Reproductive system", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000990", "habitatmech:GOLD.cd0b0940e5"], "source_attestations": [{"assertion_count": 60, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3594", "source_label": "Reproductive system", "source_path": "Host-associated &gt; Mammals: Human &gt; Reproductive system"}]} |
| ESEARCH | Local input and review traversal; grep -rn -E 'external_genitalia&#124;UBERON:0004176' reviews/structured/*/review.yaml curation/ history/ | context_only | Structured-review traversal located Stage 4 predecessor bundle 20261106T194813Z-external_genitalia-record (linked via EPREV and related_reviews) and checked related cohort and ancestor reviews for reconciliation. |
| EPREV | reviews/structured/20261106T194813Z-external_genitalia-record/review.yaml; Every immutable Stage 4 baseline finding | supports | Exact predecessor keys and findings reconciled; original inspected source scope preserved. |
| ETEST | tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py; Complete full-corpus counterfactual regression suite | supports | Exactly twenty-two records differ from the counterfactual baseline across Issues #2304 and #2305. |
| EPARENTS | curation/gold_parent_exclusions.tsv; TSV line 4, 5 | supports | [[4, "habitatmech:GOLD.2ab65bac9e\tHost-associated &gt; Mammals &gt; Reproductive system &gt; External genitalia\thabitatmech:GOLD.29feb6867b\tantigravity\t2026-11-06\tReview https://github.com/CultureBotAI/HabitatMech/issues/2304 : Crustacean and annelid excretory system are organ systems, not subtypes of the whole crustacean- or annelid-associated host environment; external genitalia is an anatomical reproductive organ structure, not a subtype of the entire mammalian or human reproductive system; external soft tissue zone is a soft-tissue anatomical region, not a subtype of the mammalian Multiple systems GOLD classification bucket; mammalian, piscine, and human eye are sense organs and ciliary body and vitreous chamber are intraocular structures/compartments, not subtypes of the entire visual system; human and mammalian fallopian tube are oviductal reproductive organs, not subtypes of the entire reproductive system; mammalian and human fascia are connective tissue sheets, not subtypes of the host-scoped connective tissue assemblage; insect fat body is an adipose organ/tissue, not a subtype of the whole insect-associated environment; feather is an avian epidermal appendage, not a subtype of the whole avian skin organ. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target UBERON:0004176. Shared mapping endpoints #1398 remain separate."], [5, "habitatmech:GOLD.97989ecf5e\tHost-associated &gt; Mammals: Human &gt; Reproductive system &gt; External genitalia/Vulva\thabitatmech:GOLD.abc827a582\tantigravity\t2026-11-06\tReview https://github.com/CultureBotAI/HabitatMech/issues/2304 : Crustacean and annelid excretory system are organ systems, not subtypes of the whole crustacean- or annelid-associated host environment; external genitalia is an anatomical reproductive organ structure, not a subtype of the entire mammalian or human reproductive system; external soft tissue zone is a soft-tissue anatomical region, not a subtype of the mammalian Multiple systems GOLD classification bucket; mammalian, piscine, and human eye are sense organs and ciliary body and vitreous chamber are intraocular structures/compartments, not subtypes of the entire visual system; human and mammalian fallopian tube are oviductal reproductive organs, not subtypes of the entire reproductive system; mammalian and human fascia are connective tissue sheets, not subtypes of the host-scoped connective tissue assemblage; insect fat body is an adipose organ/tissue, not a subtype of the whole insect-associated environment; feather is an avian epidermal appendage, not a subtype of the whole avian skin organ. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target UBERON:0004176. Shared mapping endpoints #1398 remain separate."]] |
| EHIST_G1 | history/other/gold_parent_exclusions/2026-11-07T045500Z-antigravity-230401.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2304 recorded and validated. |
| EHIST_G2 | history/other/definition_source_label_exclusions/2026-11-07T045510Z-antigravity-230501.yaml; Complete curation session history event | supports | Authorized curation event for Issue #2305 recorded and validated. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,084 no-adapter pairs; this is not whole-corpus identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in this pre-save observation.
- iModulonDB is not applicable: the target has no gene, regulator or expression-module assertion. No paid research or scientific-status promotion was performed.
- Saved against working-tree repairs atop main commit 30fbe25f4c539ad6266dae7680d21e451caf6e40; all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261106T194813Z-external_genitalia-record with exact issue_key and previous_occurrences lineage.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T050003Z-external_genitalia-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: external_genitalia'
started_at: '2026-11-07T04:55:00Z'
finished_at: '2026-11-07T05:00:03Z'
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
summary: Removed the guarded GOLD whole-system context-parent contributions habitatmech:GOLD.29feb6867b
  and habitatmech:GOLD.abc827a582 (Reproductive system) for source concepts habitatmech:GOLD.2ab65bac9e
  and habitatmech:GOLD.97989ecf5e via curation/gold_parent_exclusions.tsv (#2304),
  preserving broader ontology parent UBERON:0003133 (reproductive organ); updated
  curation/decisions.tsv for habitatmech:GOLD.97989ecf5e from EXACT to CLOSE so 'External
  genitalia/Vulva' is emitted as RELATED_SYNONYM (skos:closeMatch) and added an item-level
  REVIEW row for habitatmech:GOLD.2ab65bac9e so UBERON:0004176 achieves mapping_status
  REVIEWED (#2305). Both predecessor findings (F1 and F2) are resolved.
source:
  git_revision: 30fbe25f4c539ad6266dae7680d21e451caf6e40
  state: working_tree
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
  - path: data/habitats/host_associated/ethmoid_bone.yaml
    sha256: e406e59cf9e099828db610c838af4d413af1da9f57d9d2723b518d236188db8a
    role: context
  - path: data/habitats/host_associated/external_genitalia.yaml
    sha256: 28ce53715103e76864ca7322c1fb9743606d3468101b02cdddda033c4357e362
    role: target
  - path: data/habitats/host_associated/reproductive_system__637f205f.yaml
    sha256: 5e42989b4be93c75426bd107c5447c109a80823ede279076a57bb09d05c4d028
    role: context
  - path: data/habitats/host_associated/reproductive_system__74cf1790.yaml
    sha256: 6d45bc8c65e395c8becf2e8d97a076d494fede86f6586dabcb2c15d53b3ba2bb
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
  - path: history/other/definition_source_label_exclusions/2026-11-07T045510Z-antigravity-230501.yaml
    sha256: 16115355944b03d6e09142bca848ee5d52d3ab9332e2367433aebb6177da314c
    role: context
  - path: history/other/gold_parent_exclusions/2026-11-07T045500Z-antigravity-230401.yaml
    sha256: d55f782e57e1c75b9485ba0c5e39260dfcbaed7532af9a7fc30c3316874efac9
    role: context
  - path: reviews/structured/20261106T194813Z-external_genitalia-record/review.yaml
    sha256: 873a9c7f2930c607e09fdf82cfc9fa60dfcc0ef9b2fc6ac7739dba791a0cd8f4
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py
    sha256: 90bb097e6a2311fbaf0a2afadc4ca7642581bab11e5dd3d582ea5cd149c066f6
    role: context
targets:
- target_id: UBERON:0004176
  path: data/habitats/host_associated/external_genitalia.yaml
  label: external genitalia
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
    finding on data/habitats/host_associated/external_genitalia.yaml after bounded
    Cycle 6 Stage 5 remediation.
  selection: One of twenty-two repaired targets from the excretory_system__22ee753c-through-fecal
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0004176
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
    --target-class HabitatRecord data/habitats/host_associated/external_genitalia.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0004176
  summary: Completed 2026-11-07T04:58:12Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/excretory_system__22ee753c.yaml
    data/habitats/host_associated/excretory_system__37f93bb9.yaml data/habitats/host_associated/exoskeleton.yaml
    data/habitats/host_associated/external_genitalia.yaml data/habitats/host_associated/external_organs.yaml
    data/habitats/host_associated/external_organs__aed6edb3.yaml data/habitats/host_associated/external_soft_tissue_zone.yaml
    data/habitats/host_associated/extracellular.yaml data/habitats/host_associated/extracellular__3f7afaf4.yaml
    data/habitats/host_associated/extracellular_symbionts.yaml data/habitats/host_associated/eye.yaml
    data/habitats/host_associated/eye__59a4c665.yaml data/habitats/host_associated/eye__810dedbb.yaml
    data/habitats/host_associated/eye_ciliary_body.yaml data/habitats/host_associated/eye_ciliary_body__832768c5.yaml
    data/habitats/host_associated/eye_vitreous_chamber.yaml data/habitats/host_associated/eye_vitreous_chamber__b4eddfc1.yaml
    data/habitats/host_associated/fallopian_tubes.yaml data/habitats/host_associated/fallopian_tubes__c41e0038.yaml
    data/habitats/host_associated/fascia.yaml data/habitats/host_associated/fascia__1f6c9c1a.yaml
    data/habitats/host_associated/fat_body.yaml data/habitats/host_associated/feather.yaml
    data/habitats/host_associated/fecal.yaml --out /tmp/c6s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0004176
  summary: 'Completed 2026-11-07T04:58:18Z. Validated 24 files; files with ERROR:
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
  - UBERON:0004176
  summary: Completed 2026-11-07T04:59:00Z. No issues found; 868 history record(s)
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
  - UBERON:0004176
  summary: 'Completed 2026-11-07T04:59:05Z. provenance current: 14 committed inventories,
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
  - UBERON:0004176
  summary: 'Completed 2026-11-07T04:59:10Z. expected 3209 records, found 3209 on disk;
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
  - UBERON:0004176
  summary: Completed 2026-11-07T04:59:12Z. validated 83 causal-graph curation file(s)
    with 83 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0004176
  summary: Completed 2026-11-07T04:59:15Z. term-request table is current (671 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0004176
  summary: 'Completed 2026-11-07T04:59:20Z. OK_CANONICAL: 1203, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2084. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
- check_id: C9
  name: pytest counterfactual review repairs
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0004176
  summary: Completed 2026-11-07T04:59:30Z. 2 passed; exact 22-record counterfactual
    diff verified.
  scope_note: 'Full-corpus counterfactual regression test for Issues #2304 and #2305.'
- check_id: C10
  name: curation-floor
  status: passed
  required: true
  command: .venv/bin/python scripts/check_curation_floor.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0004176
  summary: Completed 2026-11-07T04:59:35Z. Floor satisfied across all 13 metrics.
  scope_note: Full-corpus curation floor ratchets.
- check_id: C11
  name: render-check
  status: passed
  required: true
  command: .venv/bin/python scripts/render_pages.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0004176
  summary: Completed 2026-11-07T04:59:50Z. rendered 3209 habitat pages, 750 redirect
    stubs, 8 categories, 696 term requests; pages/ is in step with the corpus.
  scope_note: Full-corpus static site parity check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/external_genitalia.yaml
  locator: Entire YAML
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: '{"identifier": "UBERON:0004176", "label": "external genitalia", "grounding_status":
    "EXACT", "mapping_status": "REVIEWED", "parent_habitats": ["UBERON:0003133"],
    "synonyms": [{"synonym_text": "External genitalia/Vulva", "synonym_type": "RELATED_SYNONYM",
    "source": "GOLD"}, {"synonym_text": "external reproductive organ", "synonym_type":
    "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text": "external sex organ", "synonym_type":
    "EXACT_SYNONYM", "source": "UBERON"}], "source_attestations": [{"source": "GOLD",
    "source_id": "gold.ecosystem:6245", "source_label": "External genitalia/Vulva",
    "source_path": "Host-associated > Mammals: Human > Reproductive system > External
    genitalia/Vulva", "mapping_predicate": "skos:closeMatch", "assertion_count": 10,
    "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path;
    first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "GOLD", "source_id":
    "gold.ecosystem:7634", "source_label": "External genitalia", "source_path": "Host-associated
    > Mammals > Reproductive system > External genitalia", "mapping_predicate": "skos:exactMatch",
    "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by GOLD. Grounding: EXACT."}, {"timestamp": "2026-10-07T00:00:00Z", "curator":
    "seed_from_sources", "action": "SOURCE_SYNONYM_SCOPED", "changes": "Retained GOLD
    label ''External genitalia/Vulva'' as RELATED_SYNONYM: a CLOSE source mapping
    does not establish exact lexical equivalence. Independent ontology synonyms and
    verbatim attestations are preserved (#1459)."}, {"timestamp": "2026-11-06T00:00:00Z",
    "curator": "antigravity", "action": "REVIEW", "changes": "Reviewed and endorsed
    the seeder''s own resolution. Multi-source review pass (https://github.com/CultureBotAI/HabitatMech/issues/2305):
    GOLD ''Host-associated > Mammals > Reproductive system > External genitalia''
    matches UBERON:0004176 ''external genitalia'' directly; reviewed at ITEM depth
    so both source concepts feeding UBERON:0004176 are reviewed. (source concept habitatmech:GOLD.2ab65bac9e)"},
    {"timestamp": "2026-11-06T00:00:00Z", "curator": "antigravity", "action": "GROUND",
    "changes": "Grounded to UBERON:0004176 ''external genitalia'' (CLOSE). Slash-disjunction
    label ''External genitalia/Vulva'' combines sex-neutral external genitalia (UBERON:0004176)
    with female vulva; CLOSE preserves the merged grounding while emitting ''External
    genitalia/Vulva'' as RELATED_SYNONYM (https://github.com/CultureBotAI/HabitatMech/issues/2305).
    Path: Host-associated > Mammals: Human > Reproductive system > External genitalia/Vulva
    (source concept habitatmech:GOLD.97989ecf5e)"}, {"timestamp": "2026-11-06T00:00:00Z",
    "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded
    GOLD source-path parent contribution habitatmech:GOLD.29feb6867b for habitatmech:GOLD.2ab65bac9e
    (Host-associated > Mammals > Reproductive system > External genitalia). Review
    https://github.com/CultureBotAI/HabitatMech/issues/2304 : Crustacean and annelid
    excretory system are organ systems, not subtypes of the whole crustacean- or annelid-associated
    host environment; external genitalia is an anatomical reproductive organ structure,
    not a subtype of the entire mammalian or human reproductive system; external soft
    tissue zone is a soft-tissue anatomical region, not a subtype of the mammalian
    Multiple systems GOLD classification bucket; mammalian, piscine, and human eye
    are sense organs and ciliary body and vitreous chamber are intraocular structures/compartments,
    not subtypes of the entire visual system; human and mammalian fallopian tube are
    oviductal reproductive organs, not subtypes of the entire reproductive system;
    mammalian and human fascia are connective tissue sheets, not subtypes of the host-scoped
    connective tissue assemblage; insect fat body is an adipose organ/tissue, not
    a subtype of the whole insect-associated environment; feather is an avian epidermal
    appendage, not a subtype of the whole avian skin organ. Exclude only exact guarded
    GOLD source-path contributions, preserving independent genera and all source observations.
    Exact target UBERON:0004176. Shared mapping endpoints #1398 remain separate."},
    {"timestamp": "2026-11-06T00:00:00Z", "curator": "antigravity", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.abc827a582
    for habitatmech:GOLD.97989ecf5e (Host-associated > Mammals: Human > Reproductive
    system > External genitalia/Vulva). Review https://github.com/CultureBotAI/HabitatMech/issues/2304
    : Crustacean and annelid excretory system are organ systems, not subtypes of the
    whole crustacean- or annelid-associated host environment; external genitalia is
    an anatomical reproductive organ structure, not a subtype of the entire mammalian
    or human reproductive system; external soft tissue zone is a soft-tissue anatomical
    region, not a subtype of the mammalian Multiple systems GOLD classification bucket;
    mammalian, piscine, and human eye are sense organs and ciliary body and vitreous
    chamber are intraocular structures/compartments, not subtypes of the entire visual
    system; human and mammalian fallopian tube are oviductal reproductive organs,
    not subtypes of the entire reproductive system; mammalian and human fascia are
    connective tissue sheets, not subtypes of the host-scoped connective tissue assemblage;
    insect fat body is an adipose organ/tissue, not a subtype of the whole insect-associated
    environment; feather is an avian epidermal appendage, not a subtype of the whole
    avian skin organ. Exclude only exact guarded GOLD source-path contributions, preserving
    independent genera and all source observations. Exact target UBERON:0004176. Shared
    mapping endpoints #1398 remain separate."}]}'
  snapshot_sha256: 28ce53715103e76864ca7322c1fb9743606d3468101b02cdddda033c4357e362
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: Seed generator produces identifier=UBERON:0004176, grounding_status=EXACT,
    mapping_status=REVIEWED, parent_habitats=["UBERON:0003133"].
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ESIB1
  kind: record_content
  reference: data/habitats/host_associated/ethmoid_bone.yaml
  locator: Entire YAML
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: Sibling GOLD-attested anatomical record UBERON:0001679 where grounding_status
    was updated from EXACT to CLOSE in curation/decisions.tsv (#2296) so a non-equivalent
    GOLD source label is retained as RELATED_SYNONYM (skos:closeMatch) rather than
    EXACT_SYNONYM.
  snapshot_sha256: e406e59cf9e099828db610c838af4d413af1da9f57d9d2723b518d236188db8a
- evidence_id: EGOLD
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV rows 528,2094
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals: Human > Reproductive system > External genitalia/Vulva", "depth": "4",
    "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_subtype":
    "External genitalia/Vulva", "ecosystem_type": "Reproductive system", "gold_node_count":
    "2", "gold_node_ids": "gold.ecosystem:6245|gold.ecosystem:6246", "leaf_label":
    "External genitalia/Vulva", "organism_count": "10", "specific_ecosystem": "",
    "study_count": "0", "total_assertions": "10"}, "row": 528}, {"data": {"biosample_count":
    "0", "canonical_path": "Host-associated > Mammals > Reproductive system > External
    genitalia", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category":
    "Mammals", "ecosystem_subtype": "External genitalia", "ecosystem_type": "Reproductive
    system", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:7634|gold.ecosystem:7635",
    "leaf_label": "External genitalia", "organism_count": "0", "specific_ecosystem":
    "", "study_count": "0", "total_assertions": "0"}, "row": 2094}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: EONT
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV rows 13183,13229
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: '[{"data": {"definition": "An organ involved in reproduction.", "deprecated":
    "", "directly_referenced": "FALSE", "label": "reproductive organ", "label_only":
    "FALSE", "ontology": "UBERON", "synonyms": "genital organ|genitalia|reproductive
    system organ|sex organ", "term_id": "UBERON:0003133"}, "row": 13183}, {"data":
    {"definition": "The external genitalia are the outer sex organs, such as the penis
    or vulva in mammals.", "deprecated": "", "directly_referenced": "TRUE", "label":
    "external genitalia", "label_only": "FALSE", "ontology": "UBERON", "synonyms":
    "external genitalia|external reproductive organ|external sex organ", "term_id":
    "UBERON:0004176"}, "row": 13229}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EONTEDGE
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV rows 11113,11426,11427,11428,11429,11483
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0003133", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0000991"}, "row": 11113}, {"data": {"object": "UBERON:0000062",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0003133"}, "row": 11426}, {"data":
    {"object": "UBERON:0005156", "predicate": "rdfs:subClassOf", "subject": "UBERON:0003133"},
    "row": 11427}, {"data": {"object": "UBERON:0003133", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0003134"}, "row": 11428}, {"data": {"object": "UBERON:0003133",
    "predicate": "rdfs:subClassOf", "subject": "UBERON:0003135"}, "row": 11429}, {"data":
    {"object": "UBERON:0003133", "predicate": "rdfs:subClassOf", "subject": "UBERON:0004176"},
    "row": 11483}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: EDEC
  kind: database
  reference: curation/decisions.tsv
  locator: TSV line 349, 902
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: '[[349, "habitatmech:GOLD.2ab65bac9e\tREVIEW\t\t\t\tantigravity\t2026-11-06\tMulti-source
    review pass (https://github.com/CultureBotAI/HabitatMech/issues/2305): GOLD ''Host-associated
    > Mammals > Reproductive system > External genitalia'' matches UBERON:0004176
    ''external genitalia'' directly; reviewed at ITEM depth so both source concepts
    feeding UBERON:0004176 are reviewed.\tITEM\t\t"], [902, "habitatmech:GOLD.97989ecf5e\tGROUND\tUBERON:0004176\texternal
    genitalia\tCLOSE\tantigravity\t2026-11-06\tSlash-disjunction label ''External
    genitalia/Vulva'' combines sex-neutral external genitalia (UBERON:0004176) with
    female vulva; CLOSE preserves the merged grounding while emitting ''External genitalia/Vulva''
    as RELATED_SYNONYM (https://github.com/CultureBotAI/HabitatMech/issues/2305).
    Path: Host-associated > Mammals: Human > Reproductive system > External genitalia/Vulva\tITEM\t\t"]]'
  snapshot_sha256: 7e0e28eeca775e7795d3f72384794f392fcf287f7f972fa57042234a64d3ce40
- evidence_id: EP2
  kind: record_content
  reference: data/habitats/host_associated/reproductive_system__637f205f.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: '{"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.29feb6867b",
    "label": "Reproductive system", "mapping_status": "SEEDED", "parent_habitats":
    ["UBERON:0000990", "habitatmech:GOLD.e889967f4f"], "source_attestations": [{"assertion_count":
    58, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes":
    "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3580", "source_label": "Reproductive
    system", "source_path": "Host-associated > Mammals > Reproductive system"}]}'
  snapshot_sha256: 5e42989b4be93c75426bd107c5447c109a80823ede279076a57bb09d05c4d028
- evidence_id: EP3
  kind: record_content
  reference: data/habitats/host_associated/reproductive_system__74cf1790.yaml
  locator: Direct-parent identity, definition, hierarchy and source scope
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: '{"definition": null, "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.abc827a582",
    "label": "Reproductive system", "mapping_status": "SEEDED", "parent_habitats":
    ["UBERON:0000990", "habitatmech:GOLD.cd0b0940e5"], "source_attestations": [{"assertion_count":
    60, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "notes":
    "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:3594", "source_label": "Reproductive
    system", "source_path": "Host-associated > Mammals: Human > Reproductive system"}]}'
  snapshot_sha256: 6d45bc8c65e395c8becf2e8d97a076d494fede86f6586dabcb2c15d53b3ba2bb
- evidence_id: ESEARCH
  kind: search
  reference: Local input and review traversal
  locator: grep -rn -E 'external_genitalia|UBERON:0004176' reviews/structured/*/review.yaml
    curation/ history/
  accessed_at: '2026-11-07T05:00:03Z'
  support: context_only
  summary: Structured-review traversal located Stage 4 predecessor bundle 20261106T194813Z-external_genitalia-record
    (linked via EPREV and related_reviews) and checked related cohort and ancestor
    reviews for reconciliation.
  search_scope: curation, history, data/raw, and reviews/structured/*/review.yaml
    traversal at commit 30fbe25f4c539ad6266dae7680d21e451caf6e40.
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261106T194813Z-external_genitalia-record/review.yaml
  locator: Every immutable Stage 4 baseline finding
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; original inspected source
    scope preserved.
  snapshot_sha256: 873a9c7f2930c607e09fdf82cfc9fa60dfcc0ef9b2fc6ac7739dba791a0cd8f4
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_excretory_system_22ee753c_to_fecal_review_repairs.py
  locator: Complete full-corpus counterfactual regression suite
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: 'Exactly twenty-two records differ from the counterfactual baseline across
    Issues #2304 and #2305.'
  snapshot_sha256: 90bb097e6a2311fbaf0a2afadc4ca7642581bab11e5dd3d582ea5cd149c066f6
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: TSV line 4, 5
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: '[[4, "habitatmech:GOLD.2ab65bac9e\tHost-associated > Mammals > Reproductive
    system > External genitalia\thabitatmech:GOLD.29feb6867b\tantigravity\t2026-11-06\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2304 : Crustacean and annelid
    excretory system are organ systems, not subtypes of the whole crustacean- or annelid-associated
    host environment; external genitalia is an anatomical reproductive organ structure,
    not a subtype of the entire mammalian or human reproductive system; external soft
    tissue zone is a soft-tissue anatomical region, not a subtype of the mammalian
    Multiple systems GOLD classification bucket; mammalian, piscine, and human eye
    are sense organs and ciliary body and vitreous chamber are intraocular structures/compartments,
    not subtypes of the entire visual system; human and mammalian fallopian tube are
    oviductal reproductive organs, not subtypes of the entire reproductive system;
    mammalian and human fascia are connective tissue sheets, not subtypes of the host-scoped
    connective tissue assemblage; insect fat body is an adipose organ/tissue, not
    a subtype of the whole insect-associated environment; feather is an avian epidermal
    appendage, not a subtype of the whole avian skin organ. Exclude only exact guarded
    GOLD source-path contributions, preserving independent genera and all source observations.
    Exact target UBERON:0004176. Shared mapping endpoints #1398 remain separate."],
    [5, "habitatmech:GOLD.97989ecf5e\tHost-associated > Mammals: Human > Reproductive
    system > External genitalia/Vulva\thabitatmech:GOLD.abc827a582\tantigravity\t2026-11-06\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2304 : Crustacean and annelid
    excretory system are organ systems, not subtypes of the whole crustacean- or annelid-associated
    host environment; external genitalia is an anatomical reproductive organ structure,
    not a subtype of the entire mammalian or human reproductive system; external soft
    tissue zone is a soft-tissue anatomical region, not a subtype of the mammalian
    Multiple systems GOLD classification bucket; mammalian, piscine, and human eye
    are sense organs and ciliary body and vitreous chamber are intraocular structures/compartments,
    not subtypes of the entire visual system; human and mammalian fallopian tube are
    oviductal reproductive organs, not subtypes of the entire reproductive system;
    mammalian and human fascia are connective tissue sheets, not subtypes of the host-scoped
    connective tissue assemblage; insect fat body is an adipose organ/tissue, not
    a subtype of the whole insect-associated environment; feather is an avian epidermal
    appendage, not a subtype of the whole avian skin organ. Exclude only exact guarded
    GOLD source-path contributions, preserving independent genera and all source observations.
    Exact target UBERON:0004176. Shared mapping endpoints #1398 remain separate."]]'
  snapshot_sha256: 913f1ece5224bbed33b736f78cc8e1244155e91f390fe8e790d6f91a24b3b796
- evidence_id: EHIST_G1
  kind: record_content
  reference: history/other/gold_parent_exclusions/2026-11-07T045500Z-antigravity-230401.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: 'Authorized curation event for Issue #2304 recorded and validated.'
  snapshot_sha256: d55f782e57e1c75b9485ba0c5e39260dfcbaed7532af9a7fc30c3316874efac9
- evidence_id: EHIST_G2
  kind: record_content
  reference: history/other/definition_source_label_exclusions/2026-11-07T045510Z-antigravity-230501.yaml
  locator: Complete curation session history event
  accessed_at: '2026-11-07T05:00:03Z'
  support: supports
  summary: 'Authorized curation event for Issue #2305 recorded and validated.'
  snapshot_sha256: 16115355944b03d6e09142bca848ee5d52d3ab9332e2367433aebb6177da314c
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction after bounded remediation
  outcome: supported
  summary: Individual schema, strict 24-target validation, 868 history records, 14
    inventory/2 GOLD provenance sources, exact 3,209-record reproduction, 83 causal
    overlays, 671 term requests, curation floor, site parity, and counterfactual regression
    tests passed.
  target_ids:
  - UBERON:0004176
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP2
  - EP3
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - EHIST_G2
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: supported
  summary: 'UBERON:0004176: external genitalia; EXACT/REVIEWED; parents ["UBERON:0003133"].
    Removed the guarded GOLD whole-system context-parent contributions habitatmech:GOLD.29feb6867b
    and habitatmech:GOLD.abc827a582 (Reproductive system) for source concepts habitatmech:GOLD.2ab65bac9e
    and habitatmech:GOLD.97989ecf5e via curation/gold_parent_exclusions.tsv (#2304),
    preserving broader ontology parent UBERON:0003133 (reproductive organ); updated
    curation/decisions.tsv for habitatmech:GOLD.97989ecf5e from EXACT to CLOSE so
    ''External genitalia/Vulva'' is emitted as RELATED_SYNONYM (skos:closeMatch) and
    added an item-level REVIEW row for habitatmech:GOLD.2ab65bac9e so UBERON:0004176
    achieves mapping_status REVIEWED (#2305). Both predecessor findings (F1 and F2)
    are resolved.'
  target_ids:
  - UBERON:0004176
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP2
  - EP3
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - EHIST_G2
- assessment_id: A3
  area: quantity
  topic: Source counts and retained ranking
  outcome: supported
  summary: 'Exact raw rows reproduce emitted counts/units, labels, scores, ranks,
    and pools: [{"source": "GOLD", "count": 10, "unit": "ORGANISM"}, {"source": "GOLD",
    "count": null, "unit": null}]. Zero counts are omitted; unrelated parent counts
    are not combined.'
  target_ids:
  - UBERON:0004176
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP2
  - EP3
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - EHIST_G2
- assessment_id: A4
  area: representation
  topic: Predecessor finding reconciliation
  outcome: supported
  summary: Every predecessor finding preserves its stable issue_key and exact lineage.
    All predecessor findings in this target scope are resolved.
  target_ids:
  - UBERON:0004176
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP2
  - EP3
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - EHIST_G2
- assessment_id: A5
  area: completeness
  topic: Parameters, mechanisms and native status
  outcome: supported
  summary: Missing optional parameters/graphs are not evidence deficits. Full source
    decisions and executed routes reproduce REVIEWED / EXACT; this read-only review
    does not mutate generated records.
  target_ids:
  - UBERON:0004176
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP2
  - EP3
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - EHIST_G2
findings:
- finding_id: F1
  issue_key: external-genitalia-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: External genitalia retains mammalian and human Reproductive system GOLD parents
    as superclasses
  description: 'Add exclusion rows in curation/gold_parent_exclusions.tsv for source
    identifier habitatmech:GOLD.2ab65bac9e (''Host-associated > Mammals > Reproductive
    system > External genitalia'', excluding parent_id habitatmech:GOLD.29feb6867b)
    and source identifier habitatmech:GOLD.97989ecf5e (''Host-associated > Mammals:
    Human > Reproductive system > External genitalia/Vulva'', excluding parent_id
    habitatmech:GOLD.abc827a582) on exact target UBERON:0004176, preserving ontology
    parent UBERON:0003133 (reproductive organ).'
  target_ids:
  - UBERON:0004176
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
  - EDEC
  - EP2
  - EP3
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - EHIST_G2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2304
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261106T194813Z-external_genitalia-record
    finding_id: F1
  disposition_reason: Excluded only the guarded GOLD whole-system context-parent contributions
    habitatmech:GOLD.29feb6867b and habitatmech:GOLD.abc827a582 (Reproductive system)
    for source concepts habitatmech:GOLD.2ab65bac9e and habitatmech:GOLD.97989ecf5e
    in curation/gold_parent_exclusions.tsv (#2304), preserving broader ontology parent
    UBERON:0003133 (reproductive organ).
- finding_id: F2
  issue_key: external-genitalia-vulva-exact-synonym
  category: nomenclature
  severity: major
  status: resolved
  certainty: confirmed
  title: External genitalia promotes slash-disjunction 'External genitalia/Vulva'
    as an exact synonym and lacks item-level review on its second GOLD path
  description: 'Update curation/decisions.tsv row 901 for habitatmech:GOLD.97989ecf5e
    (''Host-associated > Mammals: Human > Reproductive system > External genitalia/Vulva'',
    object_id UBERON:0004176) from grounding_status EXACT to CLOSE so the slash-disjunction
    label ''External genitalia/Vulva'' is emitted with scope RELATED_SYNONYM (skos:closeMatch)
    rather than EXACT_SYNONYM, and add an item-level REVIEW decision row (EXACT ->
    UBERON:0004176) for habitatmech:GOLD.2ab65bac9e (''Host-associated > Mammals >
    Reproductive system > External genitalia'') so both feeding source concepts are
    reviewed.'
  target_ids:
  - UBERON:0004176
  field_paths:
  - mapping_status
  - source_attestations[0].mapping_predicate
  - synonyms
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ESIB1
  - EGOLD
  - EONT
  - EONTEDGE
  - EDEC
  - EP2
  - EP3
  - ESEARCH
  - EPREV
  - ETEST
  - EPARENTS
  - EHIST_G1
  - EHIST_G2
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or representation claim; deterministic
    validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2305
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261106T194813Z-external_genitalia-record
    finding_id: F2
  disposition_reason: Updated curation/decisions.tsv for habitatmech:GOLD.97989ecf5e
    (External genitalia/Vulva) from EXACT to CLOSE and added an item-level REVIEW
    row for habitatmech:GOLD.2ab65bac9e (External genitalia) (#2305) so 'External
    genitalia/Vulva' is emitted with synonym_type RELATED_SYNONYM (skos:closeMatch)
    and external_genitalia.yaml achieves mapping_status REVIEWED.
actions: []
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence. Parent observations are not inherited by children.
- Configured label correspondence skipped 2,084 no-adapter pairs; this is not whole-corpus
  identifier certification.
- The post-save archive check is a subsequent output gate, not a result claimed in
  this pre-save observation.
- 'iModulonDB is not applicable: the target has no gene, regulator or expression-module
  assertion. No paid research or scientific-status promotion was performed.'
notes:
- Saved against working-tree repairs atop main commit 30fbe25f4c539ad6266dae7680d21e451caf6e40;
  all earlier saved bundles in reviews/structured/ remain byte-identical.
- Reconciles predecessor bundle 20261106T194813Z-external_genitalia-record with exact
  issue_key and previous_occurrences lineage.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261106T194813Z-external_genitalia-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
