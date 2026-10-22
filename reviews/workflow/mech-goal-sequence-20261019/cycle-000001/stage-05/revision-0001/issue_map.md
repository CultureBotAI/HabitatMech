# Stage 5 Issue Map & Grouped Finding Dispositions (`dental_plaque__8396e8ec` to `digestive_system__780e5b67`)

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `1`
- **Stage:** `5` (`resolve_review_findings`)
- **Revision:** `1`
- **Frozen Review Source:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (`0b8231a897d2228981ae4a43a4ed60ea08bb109736dbf772a5a533c24ee5ecea`)
- **Source Revision:** `2ec3d103f44a563f8cc4562f33e82d364039fa81`
- **Scope Frozen At:** `2026-10-22T06:21:22.673036Z`

## 1. Issue Group Summary

| Group ID | Status | GitHub Issue | Findings Count | Repair Ownership / Cause |
| --- | --- | --- | ---: | --- |
| `G-gold-context-parent-exclusions` | `resolved` | [#2255](https://github.com/CultureBotAI/HabitatMech/issues/2255) | 11 | GOLD source-path context/partonomy/disease parent leakage into `parents`; fixed via guarded rows in `curation/gold_parent_exclusions.tsv`, synchronized `curation/term_requests.tsv` + `curation/term_requests/envo_robot_template.tsv`, and native `scripts/generate_habitats.py` rebuild |
| `G-diatoms-host-name-exact-synonym` | `resolved` | [#2256](https://github.com/CultureBotAI/HabitatMech/issues/2256) | 1 | Bare host-clade label `'Diatoms'` asserted as `EXACT_SYNONYM` on `data/habitats/host_associated/diatoms.yaml`; fixed via `curation/term_requests.tsv`, `curation/definition_source_label_exclusions.tsv`, and native `scripts/generate_habitats.py` rebuild |
| `G-source-attestation-mapping-endpoint-contract` | `deferred` | [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) | 10 | Systemic `source_attestations[].mapping_predicate` endpoint contract where `skos:narrowMatch` from `curation/decisions.tsv` (`NARROW` to a broader ontology parent) is emitted on `SourceAttestation` against a minted `habitatmech:GOLD.*` record identifier; deferred under existing open architecture issue #1398 |

## 2. Finding-to-Issue-to-Fix Traceability

### Group 1: `G-gold-context-parent-exclusions` ([Issue #2255](https://github.com/CultureBotAI/HabitatMech/issues/2255)) — `resolved`

| Finding ID | Record Path | Record ID | Excluded GOLD Context Parent | Preserved Superclass(es) | Predecessor Bundle | Fresh Remediation Bundle |
| --- | --- | --- | --- | --- | --- | --- |
| `dental-plaque--8396e8ec-context-parent` | `data/habitats/host_associated/dental_plaque__8396e8ec.yaml` | `habitatmech:GOLD.26b1d1137f` | `habitatmech:GOLD.92d1e65695` (`Oral cavity` in `Host-associated > Mammals > Digestive system > Oral cavity > Dental plaque`) | `UBERON:0016482` (`dental plaque`) | `20261022T014510Z-dental_plaque__8396e8ec-record` | `20261022T065801Z-dental_plaque__8396e8ec-remediation` |
| `dentin--be69daef-context-parent` | `data/habitats/host_associated/dentin__be69daef.yaml` | `habitatmech:GOLD.7ec36a9a02` | `habitatmech:GOLD.2f62ba7993` (`human skeletonized remains`, bone tissue assemblage) | `BTO:0003453` (`dentin`) | `20261022T014514Z-dentin__be69daef-record` | `20261022T065802Z-dentin__be69daef-remediation` |
| `dentition-context-parent` | `data/habitats/host_associated/dentition.yaml` | `UBERON:0003672` | `UBERON:0000167` (`oral cavity` in `Host-associated > Fish > Digestive system > Oral/Buccal cavity > Teeth`) | `UBERON:0034925` (`anatomical collection`) | `20261022T014515Z-dentition-record` | `20261022T065803Z-dentition-remediation` |
| `dermal-papilla-context-parent` | `data/habitats/host_associated/dermal_papilla.yaml` | `UBERON:0000412` | `habitatmech:GOLD.4b37ab4b76` (`Skin` in `Host-associated > Mammals: Human > Integumentary system > Skin > Dermal papilla`) | `UBERON:0000479` (`tissue`) | `20261022T014516Z-dermal_papilla-record` | `20261022T065804Z-dermal_papilla-remediation` |
| `dermatitis-context-parent` | `data/habitats/host_associated/dermatitis.yaml` | `habitatmech:GOLD.25fd1f31a1` | `habitatmech:GOLD.c896f9520f` (`Skin` in `Host-associated > Mammals > Integumentary system > Skin > Dermatitis`) | `ENVO:2100003` (`skin environment`) | `20261022T014517Z-dermatitis-record` | `20261022T065805Z-dermatitis-remediation` |
| `dermatitis--d991f62d-context-parent` | `data/habitats/host_associated/dermatitis__d991f62d.yaml` | `habitatmech:GOLD.fdd6965162` | `habitatmech:GOLD.4b37ab4b76` (`Skin` in `Host-associated > Mammals: Human > Integumentary system > Skin > Dermatitis`) | `[]` (`NOT_APPLICABLE` disease concept) | `20261022T014518Z-dermatitis__d991f62d-record` | `20261022T065806Z-dermatitis__d991f62d-remediation` |
| `dermis-context-parent` | `data/habitats/host_associated/dermis.yaml` | `UBERON:0002067` | `habitatmech:GOLD.4b37ab4b76` (`Skin` in `Host-associated > Mammals: Human > Integumentary system > Skin > Dermis`) | `UBERON:0000479` (`tissue`), `UBERON:0004121` (`ectoderm-derived structure`), `UBERON:0013754` (`integumentary system layer`) | `20261022T014519Z-dermis-record` | `20261022T065807Z-dermis-remediation` |
| `descending-colon-context-parent` | `data/habitats/host_associated/descending_colon.yaml` | `UBERON:0001158` | `habitatmech:GOLD.5b0aa7456c` (`Large intestine` in `Host-associated > Mammals: Human > Digestive system > Large intestine > Descending colon`) | `UBERON:0000168` (`proximal-distal subdivision of colon`) | `20261022T014521Z-descending_colon-record` | `20261022T065808Z-descending_colon-remediation` |
| `diabetic-foot-ulcer-dfu-context-parent` | `data/habitats/host_associated/diabetic_foot_ulcer_dfu.yaml` | `habitatmech:GOLD.1219b1a720` | `habitatmech:GOLD.4b37ab4b76` (`Skin` in `Host-associated > Mammals: Human > Integumentary system > Skin > Diabetic foot ulcer (DFU)`) | `[]` (`NOT_APPLICABLE` disease concept) | `20261022T014522Z-diabetic_foot_ulcer_dfu-record` | `20261022T065809Z-diabetic_foot_ulcer_dfu-remediation` |
| `diaphragm--3c058609-context-parent` | `data/habitats/host_associated/diaphragm__3c058609.yaml` | `habitatmech:GOLD.a287a77880` | `habitatmech:GOLD.e36ba981d1` (`Respiratory system` in `Host-associated > Mammals: Human > Respiratory system > Diaphragm`) | `UBERON:0001103` (`diaphragm`) | `20261022T014525Z-diaphragm__3c058609-record` | `20261022T065810Z-diaphragm__3c058609-remediation` |
| `diaphragm--fbd202d9-context-parent` | `data/habitats/host_associated/diaphragm__fbd202d9.yaml` | `habitatmech:GOLD.c84e967b80` | `habitatmech:GOLD.fac4f63f3b` (`Respiratory system` in `Host-associated > Mammals > Respiratory system > Diaphragm`) | `UBERON:0001103` (`diaphragm`) | `20261022T014526Z-diaphragm__fbd202d9-record` | `20261022T065811Z-diaphragm__fbd202d9-remediation` |

### Group 2: `G-diatoms-host-name-exact-synonym` ([Issue #2256](https://github.com/CultureBotAI/HabitatMech/issues/2256)) — `resolved`

| Finding ID | Record Path | Record ID | Resolution Summary | Predecessor Bundle | Fresh Remediation Bundle |
| --- | --- | --- | --- | --- | --- |
| `diatoms-host-name-exact-synonym` | `data/habitats/host_associated/diatoms.yaml` | `habitatmech:GOLD.1276bea544` | Removed bare host-clade label `'Diatoms'` from `exact_synonym` in `curation/term_requests.tsv` (retaining `'diatom host environment'`) and added a guarded row in `curation/definition_source_label_exclusions.tsv` so `'Diatoms'` is preserved only as `RELATED_SYNONYM` (`source: GOLD`) | `20261022T014527Z-diatoms-record` | `20261022T065812Z-diatoms-remediation` |

### Group 3: `G-source-attestation-mapping-endpoint-contract` ([Issue #1398](https://github.com/CultureBotAI/HabitatMech/issues/1398)) — `deferred`

All 10 `mapping-endpoint-contract` findings in this cohort share the repository-wide schema/writer representation question tracked in open [Issue #1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) (*"Reconcile GOLD narrow-match output with source-attestation endpoint contract"*), where `curation/decisions.tsv` records `mapping_type: NARROW` against a broader ontology parent (`UBERON:0016482`, `BTO:0003453`, `UBERON:0001103`, `UBERON:0001007`), and `scripts/generate_habitats.py` emits `mapping_predicate: skos:narrowMatch` on `SourceAttestation` of the minted `habitatmech:GOLD.*` record. Because resolving #1398 requires a corpus-wide `SourceAttestation` schema/generator change rather than per-record curation edits, all 10 findings are explicitly deferred and carried forward in `carry_forward_ids`:

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
