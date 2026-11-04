# Category cohort review: host_associated slice empyema_drain through epibionts (24 records)

- Review: 20261101T061300Z-empyema_drain_to_epibionts-category
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-11-01T06:05:00Z
- Finished UTC: 2026-11-01T06:13:00Z
- Reviewer: antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full 24-record category boundary and cohort review of the contiguous unreviewed host_associated slice (empyema_drain.yaml through epibionts.yaml) at commit ad20de05c38d4fadf667b5c579eef50496b31b02. All 24 records represent distinct host-clade, anatomical, clinical-fluid, lesion, plant-compartment, symbiotic, or cell-type concepts (retain decisions). Record-level open findings (16 total across 13 records) are recorded in the 24 linked kind: record bundles for Stage 5 remediation.

## Scope And Provenance

Contiguous 24-record cohort boundary review of previously unreviewed records in data/habitats/host_associated/ (indices 434-457 in path order).

Selection: Next 24 unreviewed records in data/habitats/host_associated/ immediately following 20261026T083033Z-empyema-record.
Coverage: full; 24 reviewed / 24 in the declared population.
Source: git_commit at Git base ad20de05c38d4fadf667b5c579eef50496b31b02.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.1ce5b3ff1a | data/habitats/host_associated/empyema_drain.yaml | generated | pleural empyema drainage fluid |
| habitatmech:GOLD.2f5a0b5455 | data/habitats/host_associated/endocrine_gland.yaml | generated | Endocrine gland |
| habitatmech:GOLD.c26b92ece6 | data/habitats/host_associated/endocrine_gland__8c35903c.yaml | generated | Endocrine gland |
| habitatmech:GOLD.016d1f9e29 | data/habitats/host_associated/endocrine_system.yaml | generated | Endocrine system |
| habitatmech:GOLD.f386e4764b | data/habitats/host_associated/endocrine_system__a22b6ca6.yaml | generated | Endocrine system |
| habitatmech:GOLD.d275fc9ccd | data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml | generated | Endocrine system |
| habitatmech:GOLD.d63e165267 | data/habitats/host_associated/endocrine_system__fc8977b8.yaml | generated | Endocrine system |
| habitatmech:GOLD.1488865daa | data/habitats/host_associated/endometrial_uterine.yaml | generated | human endometrial polyp |
| UBERON:0001295 | data/habitats/host_associated/endometrium.yaml | generated | endometrium |
| habitatmech:GOLD.89d01f437a | data/habitats/host_associated/endophytes.yaml | generated | fruit endophyte environment |
| habitatmech:GOLD.b8e99e08e5 | data/habitats/host_associated/endophytes__ca9aaedf.yaml | generated | leaf endophyte environment |
| habitatmech:GOLD.9731c6bb13 | data/habitats/host_associated/endophytes__fae60ba7.yaml | generated | root endophyte environment |
| habitatmech:BACDIVE.3e4680f074 | data/habitats/host_associated/endosphere.yaml | generated | endosphere environment |
| habitatmech:GOLD.af0c4ac629 | data/habitats/host_associated/endosphere__005f8afe.yaml | generated | root endosphere |
| habitatmech:GOLD.356adc0d4d | data/habitats/host_associated/endosphere__eb0d56da.yaml | generated | leaf endosphere |
| habitatmech:GOLD.bfe3e11951 | data/habitats/host_associated/endosphere__fd8c8a61.yaml | generated | plant endosphere |
| habitatmech:GOLD.895a2372e5 | data/habitats/host_associated/endosymbionts.yaml | generated | host endosymbiont microhabitat |
| habitatmech:GOLD.90791d494c | data/habitats/host_associated/endosymbionts__38198b44.yaml | generated | dinoflagellate intracellular endosymbiont environment |
| BTO:0001176 | data/habitats/host_associated/endothelial_cell.yaml | generated | endothelial cell |
| BTO:0004093 | data/habitats/host_associated/endothelial_progenitor_cell.yaml | generated | endothelial progenitor cell |
| BTO:0000398 | data/habitats/host_associated/enterocyte.yaml | generated | enterocyte |
| ENVO:01001000 | data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml | generated | environmental system determined by an organism |
| BTO:0000399 | data/habitats/host_associated/eosinophil.yaml | generated | eosinophil |
| habitatmech:GOLD.d0cebee7db | data/habitats/host_associated/epibionts.yaml | generated | annelid cuticle epibiont environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db | Completed 2026-11-01T06:08:08Z. No issues found. |
| validate-strict | passed | True | habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db | Completed 2026-11-01T06:08:14Z. Validated 24 files; files with ERROR: 0; total ERROR rows: 0. |
| validate-history | passed | True | habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db | Completed 2026-11-01T06:08:25Z. No issues found; 858 history record(s) valid against src/habitatmech/schema/history.yaml. |
| provenance-check | passed | True | habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db | Completed 2026-11-01T06:08:25Z. provenance current: 14 committed inventories, 2 GOLD sources. |
| verify-corpus | passed | True | habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db | Completed 2026-11-01T06:08:41Z. expected 3209 records, found 3209 on disk; missing: 0, extra: 0, differing: 0; corpus reproduces exactly from data/raw/. |
| validate-causal-all | passed | True | habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db | Completed 2026-11-01T06:08:45Z. validated 63 causal-graph curation file(s) with 63 graph(s). |
| term-requests-check | passed | True | habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db | Completed 2026-11-01T06:09:00Z. term-request table is current (671 terms). |
| validate-products | passed | True | habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db | Completed 2026-11-01T06:11:06Z. OK_CANONICAL: 1196, OK_SYNONYM: 1, OK_EXCEPTION: 5, SKIPPED_NO_ADAPTER: 2071. All id&lt;-&gt;label pairs correspond. |

## Scientific And Domain Assessments

### Cohort native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db.

All 24 cohort target records pass LinkML validation and closed-schema strict validation; full-corpus history (858), provenance (14+2), reproduction (3,209), causal graphs (63), term requests (671), and OAK label correspondence pass.

### Cohort boundary and lumping/splitting evaluation

scope: supported. Targets: habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db.

All 24 records represent distinct host-clade, anatomical, clinical-fluid, lesion, plant-compartment, symbiotic, or cell-type bins; no lumping or splitting is warranted across the cohort.

### Cohort hierarchy, synonym, and mapping-endpoint summary

grounding: supported. Targets: habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267, habitatmech:GOLD.1488865daa, UBERON:0001295, habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951, habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, BTO:0001176, BTO:0004093, BTO:0000398, ENVO:01001000, BTO:0000399, habitatmech:GOLD.d0cebee7db.

11 records pass with limitations; 13 records have 16 open major findings recorded in their respective kind: record bundles (linked in related_reviews) and carried forward to Stage 5 grouped remediation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: habitatmech:GOLD.1ce5b3ff1a, habitatmech:GOLD.1488865daa, UBERON:0001295. Retain pleural empyema drainage fluid (habitatmech:GOLD.1ce5b3ff1a, purulent pleural drainage fluid collected via chest tube), human endometrial polyp (habitatmech:GOLD.1488865daa, benign endometrial mucosal overgrowth), and human-attested endometrium (UBERON:0001295, uterine mucosal lining) as distinct clinical-fluid, benign-lesion, and anatomical-mucosa concepts.
- retain: habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6, habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267. Retain mammalian and human Endocrine gland records (habitatmech:GOLD.2f5a0b5455, habitatmech:GOLD.c26b92ece6) and mammalian, avian, piscine, and human Endocrine system records (habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd, habitatmech:GOLD.d63e165267) as distinct host-scoped organ vs organ-system GOLD bins.
- retain: habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13, habitatmech:BACDIVE.3e4680f074, habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951. Retain fruit, leaf, and root endophyte environment GOLD paths (habitatmech:GOLD.89d01f437a, habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13) alongside BacDive Endosphere (habitatmech:BACDIVE.3e4680f074) and GOLD root, leaf, and general plant Endosphere paths (habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951) as distinct upstream source-path bins pending synonym/parent remediation in Stage 5.
- retain: habitatmech:GOLD.895a2372e5, habitatmech:GOLD.90791d494c, ENVO:01001000, habitatmech:GOLD.d0cebee7db. Retain general host endosymbiont microhabitat (habitatmech:GOLD.895a2372e5), dinoflagellate intracellular endosymbiont environment (habitatmech:GOLD.90791d494c), root host-associated class ENVO:01001000 (environmental system determined by an organism), and annelid cuticle epibiont environment (habitatmech:GOLD.d0cebee7db) as distinct symbiotic and host-associated environmental system levels.
- retain: BTO:0001176, BTO:0004093, BTO:0000398, BTO:0000399. Retain PREGO-attested endothelial cell (BTO:0001176), endothelial progenitor cell (BTO:0004093), enterocyte (BTO:0000398), and eosinophil (BTO:0000399) as distinct differentiated and progenitor host cell-type habitats.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ERULE | docs/CURATION.md; Host identity, strict broader hierarchy, bodily fluids, and source ownership | supports | Anatomical sites may identify habitats; whole-host taxon terms cannot substitute for associated environments; parent_habitats must be strictly broader across all contributing routes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon | supports | The declared mapping endpoint is the emitted record; contextual xrefs are not equivalence; parent_habitats requires strictly broader habitat classes. |
| ESEED | src/habitatmech/seed.py; Executed native resolution routes and generated source fields | supports | Seed generator resolution routes and parent/synonym assembly verified across all 24 cohort records. |
| EREC1 | data/habitats/host_associated/empyema_drain.yaml; Entire YAML | supports | habitatmech:GOLD.1ce5b3ff1a (pleural empyema drainage fluid): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["UBERON:0006314"]. |
| EREC2 | data/habitats/host_associated/endocrine_gland.yaml; Entire YAML | supports | habitatmech:GOLD.2f5a0b5455 (Endocrine gland): grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:0002368", "habitatmech:GOLD.016d1f9e29"]. |
| EREC3 | data/habitats/host_associated/endocrine_gland__8c35903c.yaml; Entire YAML | supports | habitatmech:GOLD.c26b92ece6 (Endocrine gland): grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:0002368", "habitatmech:GOLD.d63e165267"]. |
| EREC4 | data/habitats/host_associated/endocrine_system.yaml; Entire YAML | supports | habitatmech:GOLD.016d1f9e29 (Endocrine system): grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:0000949", "habitatmech:GOLD.e889967f4f"]. |
| EREC5 | data/habitats/host_associated/endocrine_system__a22b6ca6.yaml; Entire YAML | supports | habitatmech:GOLD.f386e4764b (Endocrine system): grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:0000949", "habitatmech:GOLD.47e603cf4f"]. |
| EREC6 | data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml; Entire YAML | supports | habitatmech:GOLD.d275fc9ccd (Endocrine system): grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:0000949", "habitatmech:GOLD.3d529a667e"]. |
| EREC7 | data/habitats/host_associated/endocrine_system__fc8977b8.yaml; Entire YAML | supports | habitatmech:GOLD.d63e165267 (Endocrine system): grounding_status=NARROW, mapping_status=SEEDED, parent_habitats=["UBERON:0000949", "habitatmech:GOLD.cd0b0940e5"]. |
| EREC8 | data/habitats/host_associated/endometrial_uterine.yaml; Entire YAML | supports | habitatmech:GOLD.1488865daa (human endometrial polyp): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["BTO:0006350"]. |
| EREC9 | data/habitats/host_associated/endometrium.yaml; Entire YAML | supports | UBERON:0001295 (endometrium): grounding_status=EXACT, mapping_status=SEEDED, parent_habitats=["UBERON:0019042", "habitatmech:GOLD.f736cbfbc5"]. |
| EREC10 | data/habitats/host_associated/endophytes.yaml; Entire YAML | supports | habitatmech:GOLD.89d01f437a (fruit endophyte environment): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001057", "habitatmech:GOLD.e898437067"]. |
| EREC11 | data/habitats/host_associated/endophytes__ca9aaedf.yaml; Entire YAML | supports | habitatmech:GOLD.b8e99e08e5 (leaf endophyte environment): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001057"]. |
| EREC12 | data/habitats/host_associated/endophytes__fae60ba7.yaml; Entire YAML | supports | habitatmech:GOLD.9731c6bb13 (root endophyte environment): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001057", "ENVO:01001181"]. |
| EREC13 | data/habitats/host_associated/endosphere.yaml; Entire YAML | supports | habitatmech:BACDIVE.3e4680f074 (endosphere environment): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001001"]. |
| EREC14 | data/habitats/host_associated/endosphere__005f8afe.yaml; Entire YAML | supports | habitatmech:GOLD.af0c4ac629 (root endosphere): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001057"]. |
| EREC15 | data/habitats/host_associated/endosphere__eb0d56da.yaml; Entire YAML | supports | habitatmech:GOLD.356adc0d4d (leaf endosphere): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001057"]. |
| EREC16 | data/habitats/host_associated/endosphere__fd8c8a61.yaml; Entire YAML | supports | habitatmech:GOLD.bfe3e11951 (plant endosphere): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001001"]. |
| EREC17 | data/habitats/host_associated/endosymbionts.yaml; Entire YAML | supports | habitatmech:GOLD.895a2372e5 (host endosymbiont microhabitat): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001000"]. |
| EREC18 | data/habitats/host_associated/endosymbionts__38198b44.yaml; Entire YAML | supports | habitatmech:GOLD.90791d494c (dinoflagellate intracellular endosymbiont environment): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001000", "habitatmech:GOLD.94019ddb33"]. |
| EREC19 | data/habitats/host_associated/endothelial_cell.yaml; Entire YAML | supports | BTO:0001176 (endothelial cell): grounding_status=EXACT, mapping_status=SEEDED, parent_habitats=[]. |
| EREC20 | data/habitats/host_associated/endothelial_progenitor_cell.yaml; Entire YAML | supports | BTO:0004093 (endothelial progenitor cell): grounding_status=EXACT, mapping_status=SEEDED, parent_habitats=["BTO:0004092"]. |
| EREC21 | data/habitats/host_associated/enterocyte.yaml; Entire YAML | supports | BTO:0000398 (enterocyte): grounding_status=EXACT, mapping_status=SEEDED, parent_habitats=[]. |
| EREC22 | data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml; Entire YAML | supports | ENVO:01001000 (environmental system determined by an organism): grounding_status=EXACT, mapping_status=REVIEWED, parent_habitats=["ENVO:01000254"]. |
| EREC23 | data/habitats/host_associated/eosinophil.yaml; Entire YAML | supports | BTO:0000399 (eosinophil): grounding_status=EXACT, mapping_status=SEEDED, parent_habitats=["BTO:0000539"]. |
| EREC24 | data/habitats/host_associated/epibionts.yaml; Entire YAML | supports | habitatmech:GOLD.d0cebee7db (annelid cuticle epibiont environment): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001055"]. |

## Limits And Additional Notes

- Only the stated primary evidence and current ontology/taxonomy authorities were independently inspected; original specimen-level support for every source-bin member is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism or characteristic presence.
- Configured label correspondence skipped 2,071 no-adapter pairs; this is not whole-corpus identifier certification.
- Record-specific open findings (16 across 13 records: 6 grounding/hierarchy defects, 4 nomenclature exact_synonyms defects, and 6 #1398 mapping-endpoint contract defects) are recorded on their respective kind: record bundles in related_reviews so each issue_key has a single authoritative open owner for Stage 5 remediation.
- All 24 cohort target files and context inputs were captured at clean git commit ad20de05c38d4fadf667b5c579eef50496b31b02.
- Each of the 24 targets has a dedicated kind: record bundle in reviews/structured/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T061300Z-empyema_drain_to_epibionts-category
repository: CultureBotAI/HabitatMech
kind: category
title: 'Category cohort review: host_associated slice empyema_drain through epibionts
  (24 records)'
started_at: '2026-11-01T06:05:00Z'
finished_at: '2026-11-01T06:13:00Z'
reviewer:
  identity: antigravity
  kind: agent
  model: claude-opus-4-6
  independence: self_review
  independence_basis: Same agent inspected all 24 cohort target records and source
    evidence; not independent human or second-agent approval.
skill: .claude/skills/review-yaml-category/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Full 24-record category boundary and cohort review of the contiguous unreviewed
  host_associated slice (empyema_drain.yaml through epibionts.yaml) at commit ad20de05c38d4fadf667b5c579eef50496b31b02.
  All 24 records represent distinct host-clade, anatomical, clinical-fluid, lesion,
  plant-compartment, symbiotic, or cell-type concepts (retain decisions). Record-level
  open findings (16 total across 13 records) are recorded in the 24 linked kind: record
  bundles for Stage 5 remediation.'
source:
  git_revision: ad20de05c38d4fadf667b5c579eef50496b31b02
  state: git_commit
  inputs:
  - path: curation/decisions.tsv
    sha256: 663c2f4bb14541f465da997ea049f6a1b0d7845dd92b00c70a7a9c4acc6c2dbe
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: da9135a0fd5516dc2b47679731f64b8093806105bbaddcc2e3f4d5d7c49ce07f
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 12380d3ee22e773ff067d372204f74165cf5cfa77973ad9565162bbcd383a797
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/term_requests.tsv
    sha256: fdae9bb4dd49d8cdfbaca6ee898d9b7890dd1815d2b03145d1c0c58d12c12806
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/host_associated/birds.yaml
    sha256: 2de4c694d7ca103897d519fd7fbef6d955a9c2502f6045aa8c56d4af09204aae
    role: context
  - path: data/habitats/host_associated/carposphere.yaml
    sha256: 8e29fc34bda6032f5f442106c65d27aeaac1fa84b9eccb4aead52e05eed43017
    role: context
  - path: data/habitats/host_associated/colonic.yaml
    sha256: 0017623e75dfe094c67d12bd5968d836e520038474b10e39cacfce8410028472
    role: context
  - path: data/habitats/host_associated/colorectal_polyps.yaml
    sha256: b73c9ca075c5f0b0d9c39f3d18ee1811676eb3fc940ab02357500e6d057e404b
    role: context
  - path: data/habitats/host_associated/dinoflagellates__887680eb.yaml
    sha256: 7b952bdcb6ef69dc0ff78732871356832ac9e28ab7dab8dbb224083793ba89d0
    role: context
  - path: data/habitats/host_associated/empyema_drain.yaml
    sha256: b9022361e3b09f4f1a74b0e811cf46fedcf07a152697c3956d04b9da8cd36446
    role: target
  - path: data/habitats/host_associated/endocrine_gland.yaml
    sha256: 7bad2c064b51f831c15818a6c641d7db5984605f2d54d6553ce737a824081dcc
    role: target
  - path: data/habitats/host_associated/endocrine_gland__8c35903c.yaml
    sha256: 514315aea57ac6555d13e02dac2548b4f829f1b060d347f65f372fde8a7eb9f5
    role: target
  - path: data/habitats/host_associated/endocrine_system.yaml
    sha256: d40185902cc96f17a5ae3b3c264754c84a97777f838c487b5730904c86d644dd
    role: target
  - path: data/habitats/host_associated/endocrine_system__a22b6ca6.yaml
    sha256: 839f0269b2120d9e9a486b3cfc4cde33d0579147dca6f7ca66375de3de2c0c72
    role: target
  - path: data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml
    sha256: bdc9be0d773d568cfb93f3e6d0913e3e660096c5f722771e666a4d729423dfbe
    role: target
  - path: data/habitats/host_associated/endocrine_system__fc8977b8.yaml
    sha256: d6b61f33e6a697e1b706ee63c485500da4a152c568c728eddc5817cb5edb010c
    role: target
  - path: data/habitats/host_associated/endometrial_uterine.yaml
    sha256: 3aaa152a6b20b4425400f89cbbfdebe21d56b3cfc7b51a8b63725be9a9b966ea
    role: target
  - path: data/habitats/host_associated/endometrium.yaml
    sha256: fe2a37d1b4021b65f36fc82f1758f7ea972176c71c2fc2c14cc38ee60a7a7aea
    role: target
  - path: data/habitats/host_associated/endophytes.yaml
    sha256: de96b024fc52f0d0fa3726caf5224bb0b34d195b01893ba0fd0595f7f4de7e14
    role: target
  - path: data/habitats/host_associated/endophytes__ca9aaedf.yaml
    sha256: 091600b436f4fca00fe702ae79c2902dafc9e4dede0c2437ae414c0f18ca794d
    role: target
  - path: data/habitats/host_associated/endophytes__fae60ba7.yaml
    sha256: 63b02749e6c4397e27d3284b36f221a58036b9e41a8800a619a1b865b3b619c2
    role: target
  - path: data/habitats/host_associated/endosphere.yaml
    sha256: 9cc37e05aa4930c303e68e63698c17bd61646ae4693c5b42b6c183ebd6518d08
    role: target
  - path: data/habitats/host_associated/endosphere__005f8afe.yaml
    sha256: 49ee2c7234a46c873582ba42d0f548911b1cb53eb6a535c167ffaf8316c81d2f
    role: target
  - path: data/habitats/host_associated/endosphere__eb0d56da.yaml
    sha256: cdda8f515c326357284600aae75002d9f14f5d112d49e8d28f646da8aa857112
    role: target
  - path: data/habitats/host_associated/endosphere__fd8c8a61.yaml
    sha256: 2a7297554cd29370e5fe0c1e60c80fd6f02c9cb5937117dafe316ab9d89b13a2
    role: target
  - path: data/habitats/host_associated/endosymbionts.yaml
    sha256: 552e6941a0f96665c0486e9bf8fba0351fdd4165cc09497aaeb0770875eac2a0
    role: target
  - path: data/habitats/host_associated/endosymbionts__38198b44.yaml
    sha256: 12f437a7efca3674ef998e478c382d4aabb34d9fa8374e180f03e50a45b98449
    role: target
  - path: data/habitats/host_associated/endothelial_cell.yaml
    sha256: 3539dd3c465819e55c8d9582780f412e9f3c182cc90da78e1a99a4bc7e7f7cb8
    role: target
  - path: data/habitats/host_associated/endothelial_progenitor_cell.yaml
    sha256: 48d26f5ecea077b00eb4db6f513a288e4a491646fe92b6b3ce255c5fd0a4988a
    role: target
  - path: data/habitats/host_associated/enterocyte.yaml
    sha256: 48cedbff114e272f4a9a7715a580197f65bac4395673a1a4472c9764d5f544e8
    role: target
  - path: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
    role: target
  - path: data/habitats/host_associated/eosinophil.yaml
    sha256: b6217be5b23c8f7358ad60b5349f3a33832b45cb0b8b2ff279d76766d5b843d5
    role: target
  - path: data/habitats/host_associated/epibionts.yaml
    sha256: db529ba843e2544f2002d86800370d0e65f330102739973daf60abb789b2f62f
    role: target
  - path: data/habitats/host_associated/fish.yaml
    sha256: 511e15b9761796b18df95ffb1befb025a6e4e8f6c68a8b85fb5ffa2710cd0308
    role: context
  - path: data/habitats/host_associated/hyperplastic_inflammatory_polyps.yaml
    sha256: bbf2d72875f46e5856c92d7b8d89d3cb77f93b66b384b92e1bbad147d4605ff2
    role: context
  - path: data/habitats/host_associated/mammals.yaml
    sha256: e070a7aa0a880df14e2cbee12da0375cf135cef30266fc1a3c81f41af4dd4943
    role: context
  - path: data/habitats/host_associated/mammals_human.yaml
    sha256: 6d3fba8ddf0a933b0e22f94b17e2df356eb2d297b1d96a7f960575e81d50d4d1
    role: context
  - path: data/habitats/host_associated/plant_associated_environment.yaml
    sha256: d2867ecbf58347f0022219d127df9153e4fbb933b532eeb76779998ee6ef6126
    role: context
  - path: data/habitats/host_associated/polyp.yaml
    sha256: 5c6d8ce4d9028c2b4279ba300e7a567e20793d4a5e30c70b8de74c0119508767
    role: context
  - path: data/habitats/host_associated/rhizoplane.yaml
    sha256: 20179dc7befc16a012b43aca9f12a51c54673153f950014a488687580f3b4936
    role: context
  - path: data/habitats/host_associated/uterus__a0e26d9f.yaml
    sha256: 6053e7077e3b8d1aab73f8a13ad5eb37571bf5467ddf0d24df9a20345f4a246a
    role: context
  - path: data/habitats/other/environmental_system.yaml
    sha256: 2c227791ce7b92c16ae9b76ad8295be95efee73cb65ec7050d1de2b00c8eecbc
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
- target_id: habitatmech:GOLD.1ce5b3ff1a
  path: data/habitats/host_associated/empyema_drain.yaml
  label: pleural empyema drainage fluid
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
- target_id: habitatmech:GOLD.2f5a0b5455
  path: data/habitats/host_associated/endocrine_gland.yaml
  label: Endocrine gland
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
- target_id: habitatmech:GOLD.c26b92ece6
  path: data/habitats/host_associated/endocrine_gland__8c35903c.yaml
  label: Endocrine gland
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
- target_id: habitatmech:GOLD.016d1f9e29
  path: data/habitats/host_associated/endocrine_system.yaml
  label: Endocrine system
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
- target_id: habitatmech:GOLD.f386e4764b
  path: data/habitats/host_associated/endocrine_system__a22b6ca6.yaml
  label: Endocrine system
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
- target_id: habitatmech:GOLD.d275fc9ccd
  path: data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml
  label: Endocrine system
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
- target_id: habitatmech:GOLD.d63e165267
  path: data/habitats/host_associated/endocrine_system__fc8977b8.yaml
  label: Endocrine system
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
- target_id: habitatmech:GOLD.1488865daa
  path: data/habitats/host_associated/endometrial_uterine.yaml
  label: human endometrial polyp
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
- target_id: UBERON:0001295
  path: data/habitats/host_associated/endometrium.yaml
  label: endometrium
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
- target_id: habitatmech:GOLD.89d01f437a
  path: data/habitats/host_associated/endophytes.yaml
  label: fruit endophyte environment
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
- target_id: habitatmech:GOLD.b8e99e08e5
  path: data/habitats/host_associated/endophytes__ca9aaedf.yaml
  label: leaf endophyte environment
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
- target_id: habitatmech:GOLD.9731c6bb13
  path: data/habitats/host_associated/endophytes__fae60ba7.yaml
  label: root endophyte environment
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
- target_id: habitatmech:BACDIVE.3e4680f074
  path: data/habitats/host_associated/endosphere.yaml
  label: endosphere environment
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
- target_id: habitatmech:GOLD.af0c4ac629
  path: data/habitats/host_associated/endosphere__005f8afe.yaml
  label: root endosphere
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
- target_id: habitatmech:GOLD.356adc0d4d
  path: data/habitats/host_associated/endosphere__eb0d56da.yaml
  label: leaf endosphere
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
- target_id: habitatmech:GOLD.bfe3e11951
  path: data/habitats/host_associated/endosphere__fd8c8a61.yaml
  label: plant endosphere
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
- target_id: habitatmech:GOLD.895a2372e5
  path: data/habitats/host_associated/endosymbionts.yaml
  label: host endosymbiont microhabitat
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
- target_id: habitatmech:GOLD.90791d494c
  path: data/habitats/host_associated/endosymbionts__38198b44.yaml
  label: dinoflagellate intracellular endosymbiont environment
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
- target_id: BTO:0001176
  path: data/habitats/host_associated/endothelial_cell.yaml
  label: endothelial cell
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
- target_id: BTO:0004093
  path: data/habitats/host_associated/endothelial_progenitor_cell.yaml
  label: endothelial progenitor cell
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
- target_id: BTO:0000398
  path: data/habitats/host_associated/enterocyte.yaml
  label: enterocyte
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
- target_id: ENVO:01001000
  path: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
  label: environmental system determined by an organism
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
- target_id: BTO:0000399
  path: data/habitats/host_associated/eosinophil.yaml
  label: eosinophil
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
- target_id: habitatmech:GOLD.d0cebee7db
  path: data/habitats/host_associated/epibionts.yaml
  label: annelid cuticle epibiont environment
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
  description: Contiguous 24-record cohort boundary review of previously unreviewed
    records in data/habitats/host_associated/ (indices 434-457 in path order).
  selection: Next 24 unreviewed records in data/habitats/host_associated/ immediately
    following 20261026T083033Z-empyema-record.
  coverage: full
  population_size: 24
  reviewed_target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  exclusions:
  - target: Other habitat records outside indices 434-457 of data/habitats/host_associated/
    reason: Bounded 24-record cohort slice for Cycle 4 Stage 4 record/category review;
      direct parents and relevant siblings are inspected as context.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: .venv/bin/python -m linkml.validator.cli -s src/habitatmech/schema/habitatmech.yaml
    --target-class HabitatRecord data/habitats/host_associated/empyema_drain.yaml
    data/habitats/host_associated/endocrine_gland.yaml data/habitats/host_associated/endocrine_gland__8c35903c.yaml
    data/habitats/host_associated/endocrine_system.yaml data/habitats/host_associated/endocrine_system__a22b6ca6.yaml
    data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml data/habitats/host_associated/endocrine_system__fc8977b8.yaml
    data/habitats/host_associated/endometrial_uterine.yaml data/habitats/host_associated/endometrium.yaml
    data/habitats/host_associated/endophytes.yaml data/habitats/host_associated/endophytes__ca9aaedf.yaml
    data/habitats/host_associated/endophytes__fae60ba7.yaml data/habitats/host_associated/endosphere.yaml
    data/habitats/host_associated/endosphere__005f8afe.yaml data/habitats/host_associated/endosphere__eb0d56da.yaml
    data/habitats/host_associated/endosphere__fd8c8a61.yaml data/habitats/host_associated/endosymbionts.yaml
    data/habitats/host_associated/endosymbionts__38198b44.yaml data/habitats/host_associated/endothelial_cell.yaml
    data/habitats/host_associated/endothelial_progenitor_cell.yaml data/habitats/host_associated/enterocyte.yaml
    data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    data/habitats/host_associated/eosinophil.yaml data/habitats/host_associated/epibionts.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  summary: Completed 2026-11-01T06:08:08Z. No issues found.
  scope_note: Individual schema; strict command covers the 24 named cohort targets;
    other documented gates have full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_strict.py data/habitats/host_associated/empyema_drain.yaml
    data/habitats/host_associated/endocrine_gland.yaml data/habitats/host_associated/endocrine_gland__8c35903c.yaml
    data/habitats/host_associated/endocrine_system.yaml data/habitats/host_associated/endocrine_system__a22b6ca6.yaml
    data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml data/habitats/host_associated/endocrine_system__fc8977b8.yaml
    data/habitats/host_associated/endometrial_uterine.yaml data/habitats/host_associated/endometrium.yaml
    data/habitats/host_associated/endophytes.yaml data/habitats/host_associated/endophytes__ca9aaedf.yaml
    data/habitats/host_associated/endophytes__fae60ba7.yaml data/habitats/host_associated/endosphere.yaml
    data/habitats/host_associated/endosphere__005f8afe.yaml data/habitats/host_associated/endosphere__eb0d56da.yaml
    data/habitats/host_associated/endosphere__fd8c8a61.yaml data/habitats/host_associated/endosymbionts.yaml
    data/habitats/host_associated/endosymbionts__38198b44.yaml data/habitats/host_associated/endothelial_cell.yaml
    data/habitats/host_associated/endothelial_progenitor_cell.yaml data/habitats/host_associated/enterocyte.yaml
    data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    data/habitats/host_associated/eosinophil.yaml data/habitats/host_associated/epibionts.yaml
    --out /tmp/c4s4_24_strict.tsv
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  summary: 'Completed 2026-11-01T06:08:14Z. Validated 24 files; files with ERROR:
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
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  summary: Completed 2026-11-01T06:08:25Z. No issues found; 858 history record(s)
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
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  summary: 'Completed 2026-11-01T06:08:25Z. provenance current: 14 committed inventories,
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
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  summary: 'Completed 2026-11-01T06:08:41Z. expected 3209 records, found 3209 on disk;
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
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  summary: Completed 2026-11-01T06:08:45Z. validated 63 causal-graph curation file(s)
    with 63 graph(s).
  scope_note: Full-corpus causal-graph overlay validation.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: .venv/bin/python scripts/build_term_requests.py --check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  summary: Completed 2026-11-01T06:09:00Z. term-request table is current (671 terms).
  scope_note: Full-corpus term-request table currency check.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  summary: 'Completed 2026-11-01T06:11:06Z. OK_CANONICAL: 1196, OK_SYNONYM: 1, OK_EXCEPTION:
    5, SKIPPED_NO_ADAPTER: 2071. All id<->label pairs correspond.'
  scope_note: Configured OAK identifier-label correspondence check across corpus and
    products.
evidence:
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, strict broader hierarchy, bodily fluids, and source ownership
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: Anatomical sites may identify habitats; whole-host taxon terms cannot substitute
    for associated environments; parent_habitats must be strictly broader across all
    contributing routes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate, parent_habitats, xrefs, CharacteristicTaxon
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: The declared mapping endpoint is the emitted record; contextual xrefs are
    not equivalence; parent_habitats requires strictly broader habitat classes.
  snapshot_sha256: 2ff26d07ea5a311fbe3b517c63b33e09443cb8d19947ff9e3b7627d453de1a60
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native resolution routes and generated source fields
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: Seed generator resolution routes and parent/synonym assembly verified across
    all 24 cohort records.
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EREC1
  kind: record_content
  reference: data/habitats/host_associated/empyema_drain.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.1ce5b3ff1a (pleural empyema drainage fluid): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["UBERON:0006314"].'
  snapshot_sha256: b9022361e3b09f4f1a74b0e811cf46fedcf07a152697c3956d04b9da8cd36446
- evidence_id: EREC2
  kind: record_content
  reference: data/habitats/host_associated/endocrine_gland.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.2f5a0b5455 (Endocrine gland): grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:0002368", "habitatmech:GOLD.016d1f9e29"].'
  snapshot_sha256: 7bad2c064b51f831c15818a6c641d7db5984605f2d54d6553ce737a824081dcc
- evidence_id: EREC3
  kind: record_content
  reference: data/habitats/host_associated/endocrine_gland__8c35903c.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.c26b92ece6 (Endocrine gland): grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:0002368", "habitatmech:GOLD.d63e165267"].'
  snapshot_sha256: 514315aea57ac6555d13e02dac2548b4f829f1b060d347f65f372fde8a7eb9f5
- evidence_id: EREC4
  kind: record_content
  reference: data/habitats/host_associated/endocrine_system.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.016d1f9e29 (Endocrine system): grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:0000949", "habitatmech:GOLD.e889967f4f"].'
  snapshot_sha256: d40185902cc96f17a5ae3b3c264754c84a97777f838c487b5730904c86d644dd
- evidence_id: EREC5
  kind: record_content
  reference: data/habitats/host_associated/endocrine_system__a22b6ca6.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.f386e4764b (Endocrine system): grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:0000949", "habitatmech:GOLD.47e603cf4f"].'
  snapshot_sha256: 839f0269b2120d9e9a486b3cfc4cde33d0579147dca6f7ca66375de3de2c0c72
- evidence_id: EREC6
  kind: record_content
  reference: data/habitats/host_associated/endocrine_system__e2d3d7a6.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.d275fc9ccd (Endocrine system): grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:0000949", "habitatmech:GOLD.3d529a667e"].'
  snapshot_sha256: bdc9be0d773d568cfb93f3e6d0913e3e660096c5f722771e666a4d729423dfbe
- evidence_id: EREC7
  kind: record_content
  reference: data/habitats/host_associated/endocrine_system__fc8977b8.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.d63e165267 (Endocrine system): grounding_status=NARROW,
    mapping_status=SEEDED, parent_habitats=["UBERON:0000949", "habitatmech:GOLD.cd0b0940e5"].'
  snapshot_sha256: d6b61f33e6a697e1b706ee63c485500da4a152c568c728eddc5817cb5edb010c
- evidence_id: EREC8
  kind: record_content
  reference: data/habitats/host_associated/endometrial_uterine.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.1488865daa (human endometrial polyp): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["BTO:0006350"].'
  snapshot_sha256: 3aaa152a6b20b4425400f89cbbfdebe21d56b3cfc7b51a8b63725be9a9b966ea
- evidence_id: EREC9
  kind: record_content
  reference: data/habitats/host_associated/endometrium.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'UBERON:0001295 (endometrium): grounding_status=EXACT, mapping_status=SEEDED,
    parent_habitats=["UBERON:0019042", "habitatmech:GOLD.f736cbfbc5"].'
  snapshot_sha256: fe2a37d1b4021b65f36fc82f1758f7ea972176c71c2fc2c14cc38ee60a7a7aea
- evidence_id: EREC10
  kind: record_content
  reference: data/habitats/host_associated/endophytes.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.89d01f437a (fruit endophyte environment): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001057", "habitatmech:GOLD.e898437067"].'
  snapshot_sha256: de96b024fc52f0d0fa3726caf5224bb0b34d195b01893ba0fd0595f7f4de7e14
- evidence_id: EREC11
  kind: record_content
  reference: data/habitats/host_associated/endophytes__ca9aaedf.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.b8e99e08e5 (leaf endophyte environment): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001057"].'
  snapshot_sha256: 091600b436f4fca00fe702ae79c2902dafc9e4dede0c2437ae414c0f18ca794d
- evidence_id: EREC12
  kind: record_content
  reference: data/habitats/host_associated/endophytes__fae60ba7.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.9731c6bb13 (root endophyte environment): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001057", "ENVO:01001181"].'
  snapshot_sha256: 63b02749e6c4397e27d3284b36f221a58036b9e41a8800a619a1b865b3b619c2
- evidence_id: EREC13
  kind: record_content
  reference: data/habitats/host_associated/endosphere.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:BACDIVE.3e4680f074 (endosphere environment): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001001"].'
  snapshot_sha256: 9cc37e05aa4930c303e68e63698c17bd61646ae4693c5b42b6c183ebd6518d08
- evidence_id: EREC14
  kind: record_content
  reference: data/habitats/host_associated/endosphere__005f8afe.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.af0c4ac629 (root endosphere): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001057"].'
  snapshot_sha256: 49ee2c7234a46c873582ba42d0f548911b1cb53eb6a535c167ffaf8316c81d2f
- evidence_id: EREC15
  kind: record_content
  reference: data/habitats/host_associated/endosphere__eb0d56da.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.356adc0d4d (leaf endosphere): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001057"].'
  snapshot_sha256: cdda8f515c326357284600aae75002d9f14f5d112d49e8d28f646da8aa857112
- evidence_id: EREC16
  kind: record_content
  reference: data/habitats/host_associated/endosphere__fd8c8a61.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.bfe3e11951 (plant endosphere): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001001"].'
  snapshot_sha256: 2a7297554cd29370e5fe0c1e60c80fd6f02c9cb5937117dafe316ab9d89b13a2
- evidence_id: EREC17
  kind: record_content
  reference: data/habitats/host_associated/endosymbionts.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.895a2372e5 (host endosymbiont microhabitat): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001000"].'
  snapshot_sha256: 552e6941a0f96665c0486e9bf8fba0351fdd4165cc09497aaeb0770875eac2a0
- evidence_id: EREC18
  kind: record_content
  reference: data/habitats/host_associated/endosymbionts__38198b44.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.90791d494c (dinoflagellate intracellular endosymbiont
    environment): grounding_status=UNGROUNDED, mapping_status=REVIEWED, parent_habitats=["ENVO:01001000",
    "habitatmech:GOLD.94019ddb33"].'
  snapshot_sha256: 12f437a7efca3674ef998e478c382d4aabb34d9fa8374e180f03e50a45b98449
- evidence_id: EREC19
  kind: record_content
  reference: data/habitats/host_associated/endothelial_cell.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'BTO:0001176 (endothelial cell): grounding_status=EXACT, mapping_status=SEEDED,
    parent_habitats=[].'
  snapshot_sha256: 3539dd3c465819e55c8d9582780f412e9f3c182cc90da78e1a99a4bc7e7f7cb8
- evidence_id: EREC20
  kind: record_content
  reference: data/habitats/host_associated/endothelial_progenitor_cell.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'BTO:0004093 (endothelial progenitor cell): grounding_status=EXACT, mapping_status=SEEDED,
    parent_habitats=["BTO:0004092"].'
  snapshot_sha256: 48d26f5ecea077b00eb4db6f513a288e4a491646fe92b6b3ce255c5fd0a4988a
- evidence_id: EREC21
  kind: record_content
  reference: data/habitats/host_associated/enterocyte.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'BTO:0000398 (enterocyte): grounding_status=EXACT, mapping_status=SEEDED,
    parent_habitats=[].'
  snapshot_sha256: 48cedbff114e272f4a9a7715a580197f65bac4395673a1a4472c9764d5f544e8
- evidence_id: EREC22
  kind: record_content
  reference: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'ENVO:01001000 (environmental system determined by an organism): grounding_status=EXACT,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01000254"].'
  snapshot_sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
- evidence_id: EREC23
  kind: record_content
  reference: data/habitats/host_associated/eosinophil.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'BTO:0000399 (eosinophil): grounding_status=EXACT, mapping_status=SEEDED,
    parent_habitats=["BTO:0000539"].'
  snapshot_sha256: b6217be5b23c8f7358ad60b5349f3a33832b45cb0b8b2ff279d76766d5b843d5
- evidence_id: EREC24
  kind: record_content
  reference: data/habitats/host_associated/epibionts.yaml
  locator: Entire YAML
  accessed_at: '2026-11-01T06:13:00Z'
  support: supports
  summary: 'habitatmech:GOLD.d0cebee7db (annelid cuticle epibiont environment): grounding_status=UNGROUNDED,
    mapping_status=REVIEWED, parent_habitats=["ENVO:01001055"].'
  snapshot_sha256: db529ba843e2544f2002d86800370d0e65f330102739973daf60abb789b2f62f
assessments:
- assessment_id: A1
  area: schema
  topic: Cohort native validity and reproduction
  outcome: supported
  summary: All 24 cohort target records pass LinkML validation and closed-schema strict
    validation; full-corpus history (858), provenance (14+2), reproduction (3,209),
    causal graphs (63), term requests (671), and OAK label correspondence pass.
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  evidence_ids:
  - ERULE
  - ESCHEMA
  - ESEED
- assessment_id: A2
  area: scope
  topic: Cohort boundary and lumping/splitting evaluation
  outcome: supported
  summary: All 24 records represent distinct host-clade, anatomical, clinical-fluid,
    lesion, plant-compartment, symbiotic, or cell-type bins; no lumping or splitting
    is warranted across the cohort.
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  evidence_ids:
  - EREC1
  - EREC2
  - EREC3
  - EREC4
  - EREC5
  - EREC6
  - EREC7
  - EREC8
  - EREC9
  - EREC10
  - EREC11
  - EREC12
  - EREC13
  - EREC14
  - EREC15
  - EREC16
  - EREC17
  - EREC18
  - EREC19
  - EREC20
  - EREC21
  - EREC22
  - EREC23
  - EREC24
  - ERULE
- assessment_id: A3
  area: grounding
  topic: Cohort hierarchy, synonym, and mapping-endpoint summary
  outcome: supported
  summary: '11 records pass with limitations; 13 records have 16 open major findings
    recorded in their respective kind: record bundles (linked in related_reviews)
    and carried forward to Stage 5 grouped remediation.'
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - ENVO:01001000
  - BTO:0000399
  - habitatmech:GOLD.d0cebee7db
  evidence_ids:
  - EREC1
  - EREC2
  - EREC3
  - EREC4
  - EREC5
  - EREC6
  - EREC7
  - EREC8
  - EREC9
  - EREC10
  - EREC11
  - EREC12
  - EREC13
  - EREC14
  - EREC15
  - EREC16
  - EREC17
  - EREC18
  - EREC19
  - EREC20
  - EREC21
  - EREC22
  - EREC23
  - EREC24
  - ERULE
  - ESCHEMA
  - ESEED
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - habitatmech:GOLD.1ce5b3ff1a
  - habitatmech:GOLD.1488865daa
  - UBERON:0001295
  rationale: Retain pleural empyema drainage fluid (habitatmech:GOLD.1ce5b3ff1a, purulent
    pleural drainage fluid collected via chest tube), human endometrial polyp (habitatmech:GOLD.1488865daa,
    benign endometrial mucosal overgrowth), and human-attested endometrium (UBERON:0001295,
    uterine mucosal lining) as distinct clinical-fluid, benign-lesion, and anatomical-mucosa
    concepts.
  evidence_ids:
  - EREC1
  - EREC8
  - EREC9
  - ERULE
- action: retain
  target_ids:
  - habitatmech:GOLD.2f5a0b5455
  - habitatmech:GOLD.c26b92ece6
  - habitatmech:GOLD.016d1f9e29
  - habitatmech:GOLD.f386e4764b
  - habitatmech:GOLD.d275fc9ccd
  - habitatmech:GOLD.d63e165267
  rationale: Retain mammalian and human Endocrine gland records (habitatmech:GOLD.2f5a0b5455,
    habitatmech:GOLD.c26b92ece6) and mammalian, avian, piscine, and human Endocrine
    system records (habitatmech:GOLD.016d1f9e29, habitatmech:GOLD.f386e4764b, habitatmech:GOLD.d275fc9ccd,
    habitatmech:GOLD.d63e165267) as distinct host-scoped organ vs organ-system GOLD
    bins.
  evidence_ids:
  - EREC2
  - EREC3
  - EREC4
  - EREC5
  - EREC6
  - EREC7
  - ERULE
- action: retain
  target_ids:
  - habitatmech:GOLD.89d01f437a
  - habitatmech:GOLD.b8e99e08e5
  - habitatmech:GOLD.9731c6bb13
  - habitatmech:BACDIVE.3e4680f074
  - habitatmech:GOLD.af0c4ac629
  - habitatmech:GOLD.356adc0d4d
  - habitatmech:GOLD.bfe3e11951
  rationale: Retain fruit, leaf, and root endophyte environment GOLD paths (habitatmech:GOLD.89d01f437a,
    habitatmech:GOLD.b8e99e08e5, habitatmech:GOLD.9731c6bb13) alongside BacDive Endosphere
    (habitatmech:BACDIVE.3e4680f074) and GOLD root, leaf, and general plant Endosphere
    paths (habitatmech:GOLD.af0c4ac629, habitatmech:GOLD.356adc0d4d, habitatmech:GOLD.bfe3e11951)
    as distinct upstream source-path bins pending synonym/parent remediation in Stage
    5.
  evidence_ids:
  - EREC10
  - EREC11
  - EREC12
  - EREC13
  - EREC14
  - EREC15
  - EREC16
  - ERULE
- action: retain
  target_ids:
  - habitatmech:GOLD.895a2372e5
  - habitatmech:GOLD.90791d494c
  - ENVO:01001000
  - habitatmech:GOLD.d0cebee7db
  rationale: Retain general host endosymbiont microhabitat (habitatmech:GOLD.895a2372e5),
    dinoflagellate intracellular endosymbiont environment (habitatmech:GOLD.90791d494c),
    root host-associated class ENVO:01001000 (environmental system determined by an
    organism), and annelid cuticle epibiont environment (habitatmech:GOLD.d0cebee7db)
    as distinct symbiotic and host-associated environmental system levels.
  evidence_ids:
  - EREC17
  - EREC18
  - EREC22
  - EREC24
  - ERULE
- action: retain
  target_ids:
  - BTO:0001176
  - BTO:0004093
  - BTO:0000398
  - BTO:0000399
  rationale: Retain PREGO-attested endothelial cell (BTO:0001176), endothelial progenitor
    cell (BTO:0004093), enterocyte (BTO:0000398), and eosinophil (BTO:0000399) as
    distinct differentiated and progenitor host cell-type habitats.
  evidence_ids:
  - EREC19
  - EREC20
  - EREC21
  - EREC23
  - ERULE
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061210Z-empyema_drain-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061211Z-endocrine_gland-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061212Z-endocrine_gland__8c35903c-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061213Z-endocrine_system-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061214Z-endocrine_system__a22b6ca6-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061215Z-endocrine_system__e2d3d7a6-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061216Z-endocrine_system__fc8977b8-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061217Z-endometrial_uterine-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061218Z-endometrium-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061219Z-endophytes-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061220Z-endophytes__ca9aaedf-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061221Z-endophytes__fae60ba7-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061222Z-endosphere-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061223Z-endosphere__005f8afe-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061224Z-endosphere__eb0d56da-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061225Z-endosphere__fd8c8a61-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061226Z-endosymbionts-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061227Z-endosymbionts__38198b44-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061228Z-endothelial_cell-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061229Z-endothelial_progenitor_cell-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061230Z-enterocyte-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061231Z-environmental_system_determined_by_an_organism-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061232Z-eosinophil-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
- repository: CultureBotAI/HabitatMech
  review_id: 20261101T061233Z-epibionts-record
  relationship: Component individual record review in this 24-record Cycle-4 Stage-4
    cohort.
limitations:
- Only the stated primary evidence and current ontology/taxonomy authorities were
  independently inspected; original specimen-level support for every source-bin member
  is not established.
- Association counts and PREGO scores do not establish prevalence, viability, mechanism
  or characteristic presence.
- Configured label correspondence skipped 2,071 no-adapter pairs; this is not whole-corpus
  identifier certification.
- 'Record-specific open findings (16 across 13 records: 6 grounding/hierarchy defects,
  4 nomenclature exact_synonyms defects, and 6 #1398 mapping-endpoint contract defects)
  are recorded on their respective kind: record bundles in related_reviews so each
  issue_key has a single authoritative open owner for Stage 5 remediation.'
notes:
- All 24 cohort target files and context inputs were captured at clean git commit
  ad20de05c38d4fadf667b5c579eef50496b31b02.
- 'Each of the 24 targets has a dedicated kind: record bundle in reviews/structured/.'
tags:
- category-cohort-review
- host-associated
```
