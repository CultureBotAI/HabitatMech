# Cycle 2 Stage 5 Issue Map & Grouped Finding Dispositions (`digestive_system__87922027` to `ear_canal__7b012d70`)

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `2`
- **Stage:** `5` (`resolve_review_findings`)
- **Revision:** `1`
- **Frozen Review Source:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml` (`9c59a5659e8fc97d0519ef40faa2f091e8c412e33887f4e422be548845c733c1`)
- **Source Revision:** `6a4778d4cff07ec783dd596044d9b00921e3925f`
- **Scope Frozen At:** `2026-10-25T14:55:00Z`

## 1. Issue Group Summary

| Group ID | Status | GitHub Issue | Findings Count | Repair Ownership / Cause |
| --- | --- | --- | ---: | --- |
| `G-gold-context-parent-exclusions` | `resolved` | [#2265](https://github.com/CultureBotAI/HabitatMech/issues/2265) | 8 | GOLD source-path context/partonomy/disease parent leakage into `parent_habitats`; fixed via guarded rows in `curation/gold_parent_exclusions.tsv` and native `scripts/seed_from_sources.py` rebuild |
| `G-dinoflagellates-host-name-exact-synonym` | `resolved` | [#2266](https://github.com/CultureBotAI/HabitatMech/issues/2266) | 1 | Bare host-clade label `'Dinoflagellates'` asserted as `EXACT_SYNONYM` on `data/habitats/host_associated/dinoflagellates__887680eb.yaml`; fixed via `curation/term_requests.tsv`, `curation/definition_source_label_exclusions.tsv`, and native `scripts/seed_from_sources.py` rebuild |
| `G-source-attestation-mapping-endpoint-contract` | `deferred` | [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) | 23 | Systemic `source_attestations[].mapping_predicate` endpoint contract where `skos:narrowMatch` from `curation/decisions.tsv` (`NARROW` to a broader ontology parent) is emitted on `SourceAttestation` against a minted `habitatmech:GOLD.*` record identifier (10 carried forward from Cycle 1 Stage 5 + 13 from Cycle 2 Stage 4); deferred under existing open architecture issue #1398 |

## 2. Finding-to-Issue-to-Fix Traceability

### Group 1: `G-gold-context-parent-exclusions` ([Issue #2265](https://github.com/CultureBotAI/HabitatMech/issues/2265)) — `resolved`

| Finding ID | Record Path | Record ID | Excluded GOLD Context Parent | Preserved Superclass(es) | Predecessor Bundle | Fresh Remediation Bundle |
| --- | --- | --- | --- | --- | --- | --- |
| `digestive-tract-context-parent` | `data/habitats/host_associated/digestive_tract.yaml` | `UBERON:0001555` | `habitatmech:GOLD.d011f4b43c` (`Digestive system` in `Host-associated > Annelida > Digestive system > Digestive tube`) | `UBERON:0000025` (`tube`) | `20261025T104019Z-digestive_tract-record` | `20261025T151001Z-digestive_tract-remediation` |
| `duodenal-ulcer-context-parent` | `data/habitats/host_associated/duodenal_ulcer.yaml` | `habitatmech:GOLD.9bfaa32c03` | `habitatmech:GOLD.f131dcac3d` (`Small intestine` in `Host-associated > Mammals: Human > Digestive system > Small intestine > Duodenal ulcer`) | `[]` (`NOT_APPLICABLE` disease concept) | `20261025T104026Z-duodenal_ulcer-record` | `20261025T151003Z-duodenal_ulcer-remediation` |
| `duodenum--00ca3b2c-context-parent` | `data/habitats/host_associated/duodenum__00ca3b2c.yaml` | `habitatmech:GOLD.d1ffda8340` | `habitatmech:GOLD.f131dcac3d` (`Small intestine` in `Host-associated > Mammals: Human > Digestive system > Small intestine > Duodenum`) | `UBERON:0002114` (`duodenum`) | `20261025T104028Z-duodenum__00ca3b2c-record` | `20261025T151004Z-duodenum__00ca3b2c-remediation` |
| `duodenum--5b2d8f0e-context-parent` | `data/habitats/host_associated/duodenum__5b2d8f0e.yaml` | `habitatmech:GOLD.4e3f079a4d` | `habitatmech:GOLD.d3160a0c40` (`Small intestine` in `Host-associated > Mammals > Digestive system > Small intestine > Duodenum`) | `UBERON:0002114` (`duodenum`) | `20261025T104029Z-duodenum__5b2d8f0e-record` | `20261025T151005Z-duodenum__5b2d8f0e-remediation` |
| `duodenum--e751f297-context-parent` | `data/habitats/host_associated/duodenum__e751f297.yaml` | `habitatmech:GOLD.87d8aea294` | `habitatmech:GOLD.333c28fb9f` (`Small intestine` in `Host-associated > Birds > Digestive system > Small intestine > Duodenum`) | `UBERON:0002114` (`duodenum`) | `20261025T104030Z-duodenum__e751f297-record` | `20261025T151006Z-duodenum__e751f297-remediation` |
| `ear-context-parent` | `data/habitats/host_associated/ear.yaml` | `UBERON:0001690` | `habitatmech:GOLD.b842078e17` (`human auditory system environment` in `Host-associated > Mammals: Human > Auditory/Hearing system > Ear`) | `UBERON:0000020` (`sense organ`), `UBERON:0010314` (`structure with developmental contribution from neural crest`) | `20261025T104031Z-ear-record` | `20261025T151007Z-ear-remediation` |
| `ear-canal-context-parent` | `data/habitats/host_associated/ear_canal.yaml` | `habitatmech:GOLD.57fa2ba2ad` | `habitatmech:GOLD.1930d3bfbc` (`Outer ear` in `Host-associated > Mammals > Auditory/Hearing system > Outer ear > Ear canal`) | `UBERON:0001352` (`external acoustic meatus`) | `20261025T104032Z-ear_canal-record` | `20261025T151008Z-ear_canal-remediation` |
| `ear-canal--7b012d70-context-parent` | `data/habitats/host_associated/ear_canal__7b012d70.yaml` | `habitatmech:GOLD.8b135afbf6` | `habitatmech:GOLD.1821934761` (`Outer ear` in `Host-associated > Mammals: Human > Auditory/Hearing system > Outer ear > Ear canal`) | `UBERON:0001352` (`external acoustic meatus`) | `20261025T104033Z-ear_canal__7b012d70-record` | `20261025T151009Z-ear_canal__7b012d70-remediation` |

### Group 2: `G-dinoflagellates-host-name-exact-synonym` ([Issue #2266](https://github.com/CultureBotAI/HabitatMech/issues/2266)) — `resolved`

| Finding ID | Record Path | Record ID | Resolution Summary | Predecessor Bundle | Fresh Remediation Bundle |
| --- | --- | --- | --- | --- | --- |
| `dinoflagellates--887680eb-host-name-exact-synonym` | `data/habitats/host_associated/dinoflagellates__887680eb.yaml` | `habitatmech:GOLD.94019ddb33` | Replaced bare host-clade label `'Dinoflagellates'` in `exact_synonym` in `curation/term_requests.tsv` with `'dinoflagellate host environment'` and added a guarded row in `curation/definition_source_label_exclusions.tsv` so `'Dinoflagellates'` is preserved only as `RELATED_SYNONYM` (`source: GOLD`) | `20261025T104021Z-dinoflagellates__887680eb-record` | `20261025T151002Z-dinoflagellates__887680eb-remediation` |

### Group 3: `G-source-attestation-mapping-endpoint-contract` ([Issue #1398](https://github.com/CultureBotAI/HabitatMech/issues/1398)) — `deferred`

All 23 `mapping-endpoint-contract` findings (10 carried forward from Cycle 1 Stage 5 plus 13 from Cycle 2 Stage 4) share the repository-wide schema/writer representation question tracked in open [Issue #1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) (*"Reconcile GOLD narrow-match output with source-attestation endpoint contract"*), where `curation/decisions.tsv` records `mapping_type: NARROW` against a broader ontology parent (`UBERON:0016482`, `BTO:0003453`, `UBERON:0001103`, `UBERON:0001007`, `UBERON:0002114`, `UBERON:0001352`), and `src/habitatmech/seed.py` emits `mapping_predicate: skos:narrowMatch` on `SourceAttestation` of the minted `habitatmech:GOLD.*` record. Because resolving #1398 requires a corpus-wide `SourceAttestation` schema/generator change rather than per-record curation edits, all 23 findings are explicitly deferred and carried forward in `carry_forward_ids`:

1. `dental-plaque--8396e8ec-mapping-endpoint-contract` (`data/habitats/host_associated/dental_plaque__8396e8ec.yaml`)
2. `dentin-mapping-endpoint-contract` (`data/habitats/host_associated/dentin.yaml`)
3. `dentin--be69daef-mapping-endpoint-contract` (`data/habitats/host_associated/dentin__be69daef.yaml`)
4. `diaphragm--3c058609-mapping-endpoint-contract` (`data/habitats/host_associated/diaphragm__3c058609.yaml`)
5. `diaphragm--fbd202d9-mapping-endpoint-contract` (`data/habitats/host_associated/diaphragm__fbd202d9.yaml`)
6. `digestive-system-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system.yaml`)
7. `digestive-system--2589c8ce-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__2589c8ce.yaml`)
8. `digestive-system--46d403bb-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__46d403bb.yaml`)
9. `digestive-system--4f205b4d-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__4f205b4d.yaml`)
10. `digestive-system--780e5b67-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__780e5b67.yaml`)
11. `digestive-system--87922027-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__87922027.yaml`)
12. `digestive-system--9ec9b5f9-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__9ec9b5f9.yaml`)
13. `digestive-system--ae8329bf-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__ae8329bf.yaml`)
14. `digestive-system--c5da4fa6-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__c5da4fa6.yaml`)
15. `digestive-system--d7057103-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__d7057103.yaml`)
16. `digestive-system--e41cfc7b-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__e41cfc7b.yaml`)
17. `digestive-system--efdbeca1-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__efdbeca1.yaml`)
18. `digestive-system--f6665a67-mapping-endpoint-contract` (`data/habitats/host_associated/digestive_system__f6665a67.yaml`)
19. `duodenum--00ca3b2c-mapping-endpoint-contract` (`data/habitats/host_associated/duodenum__00ca3b2c.yaml`)
20. `duodenum--5b2d8f0e-mapping-endpoint-contract` (`data/habitats/host_associated/duodenum__5b2d8f0e.yaml`)
21. `duodenum--e751f297-mapping-endpoint-contract` (`data/habitats/host_associated/duodenum__e751f297.yaml`)
22. `ear-canal-mapping-endpoint-contract` (`data/habitats/host_associated/ear_canal.yaml`)
23. `ear-canal--7b012d70-mapping-endpoint-contract` (`data/habitats/host_associated/ear_canal__7b012d70.yaml`)
