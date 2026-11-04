# Cycle 4 Stage 5 Issue Map & Grouped Finding Dispositions (`empyema_drain` to `epibionts`)

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `4`
- **Stage:** `5` (`resolve_review_findings`)
- **Revision:** `1`
- **Frozen Review Source:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml` (`83d298ceded5970e01661838c3a195e5149a8c8ade68097cfa0220480991d0f1`)
- **Source Revision:** `95a1eb1b6a5b18b8a5c3b135222b1118f7506ef0`
- **Scope Frozen At:** `2026-11-04T03:45:00Z`

## 1. Issue Group Summary

| Group ID | Status | GitHub Issue | Findings Count | Repair Ownership / Cause |
| --- | --- | --- | ---: | --- |
| `G-empyema-drain-to-epibionts-parent-grounding-repairs` | `resolved` | [#2285](https://github.com/CultureBotAI/HabitatMech/issues/2285) | 6 | GOLD context-only parent leakage (`endocrine_gland`, `endocrine_gland__8c35903c`, `endometrium`, `endophytes`, `endophytes__fae60ba7`) and `UBERON:0013764` (`cnidarian polyp`) vs `UBERON:0036226` (`Lesion`) genus/parent defect on `endometrial_uterine`; fixed via `curation/decisions.tsv`, `curation/term_requests.tsv`, `curation/gold_parent_exclusions.tsv`, `scripts/build_term_requests.py`, and `scripts/seed_from_sources.py` |
| `G-empyema-drain-to-epibionts-exact-synonym-repairs` | `resolved` | [#2286](https://github.com/CultureBotAI/HabitatMech/issues/2286) | 4 | Bare GOLD source leaf labels (`Empyema drain`, `Endosphere`) promoted to `exact_synonyms` on `empyema_drain` and `endosphere__fd8c8a61`, plus cross-record `plant endosphere` exact-synonym collision between `endophytes__ca9aaedf` and `endophytes__fae60ba7`; fixed via `curation/term_requests.tsv`, guarded rows in `curation/definition_source_label_exclusions.tsv`, and `scripts/seed_from_sources.py` |
| `G-source-attestation-mapping-endpoint-contract` | `deferred` | [#1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) | 30 | Systemic `source_attestations[].mapping_predicate` endpoint contract where `skos:narrowMatch` from `curation/decisions.tsv` (`NARROW` to a broader ontology parent) is emitted on `SourceAttestation` against a minted `habitatmech:GOLD.*` record identifier; deferred under open repository architecture Issue #1398 |

## 2. Finding-to-Issue-to-Fix Traceability

### Group 1: `G-empyema-drain-to-epibionts-parent-grounding-repairs` ([Issue #2285](https://github.com/CultureBotAI/HabitatMech/issues/2285)) — `resolved`

| Finding ID | Record Path | Record ID | Excluded GOLD Context Parent / Repaired Grounding | Preserved Superclass(es) | Predecessor Bundle | Fresh Remediation Bundle |
| --- | --- | --- | --- | --- | --- | --- |
| `endocrine-gland-context-parent` | `data/habitats/host_associated/endocrine_gland.yaml` | `habitatmech:GOLD.4e865e4d23` | `UBERON:0000949` (`endocrine system` in `Host-associated > Mammals: Human > Endocrine system > Endocrine gland`) | `UBERON:0002530` (`gland`) | `20261101T061211Z-endocrine_gland-record` | `20261104T035802Z-endocrine_gland-remediation` |
| `endocrine-gland--8c35903c-context-parent` | `data/habitats/host_associated/endocrine_gland__8c35903c.yaml` | `habitatmech:GOLD.b6bfeb7df5` | `UBERON:0000949` (`endocrine system` in `Host-associated > Mammals > Endocrine system > Endocrine gland`) | `UBERON:0002530` (`gland`) | `20261101T061212Z-endocrine_gland__8c35903c-record` | `20261104T035803Z-endocrine_gland__8c35903c-remediation` |
| `endometrial-uterine-cnidarian-polyp-parent` | `data/habitats/host_associated/endometrial_uterine.yaml` | `habitatmech:GOLD.1488865daa` | Replaced `UBERON:0013764` (`polyp`, cnidarian life-cycle form) with `UBERON:0036226` (`Lesion`, `parent_mode=REPLACE`) in `curation/term_requests.tsv`, updated `curation/decisions.tsv`, and excluded `UBERON:0000995` (`uterus` in `Host-associated > Mammals: Human > Reproductive system > Uterus > Polyp > Endometrial/Uterine`) | `UBERON:0036226` (`Lesion`) | `20261101T061217Z-endometrial_uterine-record` | `20261104T035808Z-endometrial_uterine-remediation` |
| `endometrium-context-parent` | `data/habitats/host_associated/endometrium.yaml` | `UBERON:0001295` | `UBERON:0000995` (`uterus` in `Host-associated > Mammals: Human > Reproductive system > Uterus > Endometrium`) | `UBERON:0000344` (`mucosa`) | `20261101T061218Z-endometrium-record` | `20261104T035809Z-endometrium-remediation` |
| `endophytes-context-parent` | `data/habitats/host_associated/endophytes.yaml` | `habitatmech:GOLD.f4469db65f` | `habitatmech:GOLD.cd4f2f2186` (`macroalgal host environment` in `Host-associated > Algae > Macroalgae > Endophytes`, `parent_mode=REPLACE`) | `PO:0009007` (`portion of plant tissue`) | `20261101T061219Z-endophytes-record` | `20261104T035811Z-endophytes-remediation` |
| `endophytes--fae60ba7-context-parent` | `data/habitats/host_associated/endophytes__fae60ba7.yaml` | `habitatmech:GOLD.796a8ab6ba` | `habitatmech:GOLD.db7faef3a8` (`plant host environment` in `Host-associated > Plants > Endophytes`, `parent_mode=REPLACE`) | `PO:0009007` (`portion of plant tissue`) | `20261101T061221Z-endophytes__fae60ba7-record` | `20261104T035813Z-endophytes__fae60ba7-remediation` |

### Group 2: `G-empyema-drain-to-epibionts-exact-synonym-repairs` ([Issue #2286](https://github.com/CultureBotAI/HabitatMech/issues/2286)) — `resolved`

| Finding ID | Record Path | Record ID | Resolution Summary | Predecessor Bundle | Fresh Remediation Bundle |
| --- | --- | --- | --- | --- | --- |
| `empyema-drain-device-name-exact-synonym` | `data/habitats/host_associated/empyema_drain.yaml` | `habitatmech:GOLD.ab7c8a2936` | Removed bare medical-device label `'Empyema drain'` from `exact_synonym` in `curation/term_requests.tsv` and added guarded row in `curation/definition_source_label_exclusions.tsv`; retained as `RELATED_SYNONYM` (`source: GOLD`) | `20261101T061210Z-empyema_drain-record` | `20261104T035801Z-empyema_drain-remediation` |
| `endophytes--ca9aaedf-synonym-collision` | `data/habitats/host_associated/endophytes__ca9aaedf.yaml` | `habitatmech:GOLD.ca6b46b22d` | Replaced colliding `exact_synonym` `'plant endosphere'` in `curation/term_requests.tsv` with `'fungal-dominated plant endosphere'` | `20261101T061220Z-endophytes__ca9aaedf-record` | `20261104T035812Z-endophytes__ca9aaedf-remediation` |
| `endophytes--fae60ba7-synonym-collision` | `data/habitats/host_associated/endophytes__fae60ba7.yaml` | `habitatmech:GOLD.796a8ab6ba` | Replaced colliding `exact_synonym` `'plant endosphere'` in `curation/term_requests.tsv` with `'plant tissue endosphere'` | `20261101T061221Z-endophytes__fae60ba7-record` | `20261104T035813Z-endophytes__fae60ba7-remediation` |
| `endosphere--fd8c8a61-bare-source-label-exact-synonym` | `data/habitats/host_associated/endosphere__fd8c8a61.yaml` | `habitatmech:GOLD.cf60c050d7` | Removed bare cross-kingdom label `'Endosphere'` from `exact_synonym` in `curation/term_requests.tsv` and added guarded row in `curation/definition_source_label_exclusions.tsv`; retained as `RELATED_SYNONYM` (`source: GOLD`) | `20261101T061225Z-endosphere__fd8c8a61-record` | `20261104T035815Z-endosphere__fd8c8a61-remediation` |

### Group 3: `G-source-attestation-mapping-endpoint-contract` ([Issue #1398](https://github.com/CultureBotAI/HabitatMech/issues/1398)) — `deferred`

All 30 `mapping-endpoint-contract` findings (24 carried forward from Cycles 1–3 plus 6 new findings from Cycle 4 Stage 4: `endocrine-gland-mapping-endpoint-contract`, `endocrine-gland--8c35903c-mapping-endpoint-contract`, `endocarp-mapping-endpoint-contract`, `endolymph-mapping-endpoint-contract`, `endolithic-microbiome-mapping-endpoint-contract`, and `epibionts-mapping-endpoint-contract`) share the repository-wide schema/writer representation question tracked in open [Issue #1398](https://github.com/CultureBotAI/HabitatMech/issues/1398) (*"Reconcile GOLD narrow-match output with source-attestation endpoint contract"*), where `curation/decisions.tsv` records `mapping_type: NARROW` against a broader ontology parent and `src/habitatmech/seed.py` emits `mapping_predicate: skos:narrowMatch` on `SourceAttestation` of the minted `habitatmech:GOLD.*` record. Because resolving #1398 requires a corpus-wide `SourceAttestation` schema/generator change rather than per-record curation edits, all 30 findings are explicitly deferred and carried forward in `carry_forward_ids`.
