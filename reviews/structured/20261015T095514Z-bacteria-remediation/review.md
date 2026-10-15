# Remediation review: bacterium-associated environment (habitatmech:GOLD.029baaef9e)

- Review: 20261015T095514Z-bacteria-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T09:53:03Z
- Finished UTC: 2026-10-15T09:55:14Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

1 predecessor finding(s) resolved; 0 remain open. The complete current record and maintained inputs agree; only scoped parent/synonym claims and appended deterministic history change.

## Scope And Provenance

Complete current record re-read and exact predecessor disposition.

Selection: One of ten repaired targets from the twenty-record PR cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 423f501bdb507d335cb198fa27d653ae68949c93.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.029baaef9e | data/habitats/host_associated/bacteria.yaml | generated | bacterium-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate-strict data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml | passed | True | habitatmech:GOLD.029baaef9e | Executed 2026-10-15T09:52:04Z through 2026-10-15T09:52:13Z. uv run python scripts/validate_strict.py data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.029baaef9e | Executed 2026-10-15T09:52:13Z through 2026-10-15T09:52:24Z. No issues found<br>789 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.029baaef9e | Executed 2026-10-15T09:52:24Z through 2026-10-15T09:52:25Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.029baaef9e | Executed 2026-10-15T09:52:25Z through 2026-10-15T09:52:47Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.029baaef9e | Executed 2026-10-15T09:52:47Z through 2026-10-15T09:52:53Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.029baaef9e | Executed 2026-10-15T09:52:53Z through 2026-10-15T09:53:21Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.029baaef9e | Executed 2026-10-15T09:53:21Z through 2026-10-15T09:54:36Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python3 -m pytest -q tests/test_gingiva_benign_review_repairs.py | passed | True | habitatmech:GOLD.029baaef9e | Executed 2026-10-15T09:54:36Z through 2026-10-15T09:54:43Z. .                                                                        [100%]<br>1 passed in 6.15s |
| git diff --check bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d | passed | True | habitatmech:GOLD.029baaef9e | Executed 2026-10-15T09:54:43Z through 2026-10-15T09:54:43Z.  |

## Scientific And Domain Assessments

### Scoped repairs and complete-record preservation

consistency: supported. Targets: habitatmech:GOLD.029baaef9e.

Counterfactual and complete-record checks establish exactly the intended bounded changes and preserve identities, definitions, source observations, statuses, valid parents and prior history.

### Retained scientific support

evidence: supported. Targets: habitatmech:GOLD.029baaef9e.

Rechecked complete target against the inspected typed ontology and bounded primary evidence retained from its predecessor. No new prevalence, mechanism or characteristic-presence claim is added.

## Findings

### F1: Whole-host name is an exact environmental synonym

major / resolved / confirmed; issue key: bacteria-host-name-exact-synonym.

Remove only Bacteria from the exact_synonym cell for habitatmech:GOLD.029baaef9e and add a guarded definition_source_label_exclusions.tsv row preventing automatic old-label fallback. Preserve the environmental definition, genus, minted identity, source label/path and counts.

Disposition: Removed the authored whole-host exact alias and explicitly blocked old-label fallback. The environmental definition, genera, verbatim source label/path/count and native status are unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000254/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_01000254", "target": "http://purl.obolibrary.org/obo/RO_0002577", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000254; Canonical term identity, definition and explicit relation types | supports | ENVO:01000254 environmental system; inspected definition and typed scope. ["In ENVO's alignment with the Basic Formal Ontology, this class is being considered as a subclass of a proposed BFO class \"system\". The relation \"environed_by\" is also under development. Roughly, a system which includes a material entity (at least partially) within its site and causally influences that entity may be considered to environ it. Following the completion of this alignment, this class' definition and the definitions of its subclasses will be revised.", "A system which has the disposition to environ one or more material entities."] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000; Canonical term identity, definition and explicit relation types | supports | ENVO:01001000 environmental system determined by an organism; inspected definition and typed scope. ["An environmental system which is determined by a living organism."] |
| EAFTER | data/habitats/host_associated/bacteria.yaml; Entire regenerated YAML | supports | Complete current record inspected: {"curation_history": [{"action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. GOLD's Host-associated &gt; Microbial &gt; Bacteria: bacteria acting as host for another microbe. No environment term exists for a microbial host; ENVO's organism-associated terms cover plants and animals only. ENVO term request. (source concept habitatmech:GOLD.029baaef9e)", "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "DEFINED", "changes": "Defined as 'bacterium-associated environment' under ENVO:01001000 'environmental system determined by an organism'. The habitat is the host clade, and it is the entire content of the concept: GOLD organises host-associated isolates by host and every anatomical path hangs off it. Not grounded to the parent, because every clade would then merge onto one record. Same pattern ENVO already has at plant-, animal- and fungi-associated environment. GOLD's child of Microbial. Parented to the organism root here because its natural parent, microbe-associated environment, is requested in this same batch and does not exist yet \u2014 editors should re-parent it if both are minted.", "curator": "claude-opus-5", "timestamp": "2026-08-16T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "SOURCE_SYNONYM_EXCLUDED", "changes": "Omitted automatic retention of displaced source label 'Bacteria' when defining habitatmech:GOLD.029baaef9e as 'bacterium-associated environment'. Verbatim source attestations are preserved. Review #2167: Bacteria denotes the host organisms, not their associated environment. Remove only this authored exact alias and suppress old-label fallback; retain the environmental definition, genera, verbatim source label/path/count/unit, native status and prior history.", "curator": "codex-gpt-5", "timestamp": "2026-10-15T00:00:00Z"}], "definition": "An environmental system determined by a bacterium.", "definition_source": "HabitatMech", "grounding_status": "UNGROUNDED", "habitat_category": "HOST_ASSOCIATED", "identifier": "habitatmech:GOLD.029baaef9e", "label": "bacterium-associated environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000", "habitatmech:GOLD.184623c963"], "source_attestations": [{"assertion_count": 3017, "assertion_unit": "ORGANISM", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3540", "source_label": "Bacteria", "source_path": "Host-associated &gt; Microbial &gt; Bacteria"}]} |
| EPREV | reviews/structured/20261015T093738Z-bacteria-record/review.yaml; Exact immutable predecessor and all findings | supports | Original evidence, limitations and finding identities remain preserved. |
| ETEST | tests/test_gingiva_benign_review_repairs.py; Whole-corpus counterfactual regression | supports | Restores only the prior rules in memory: exactly ten records change. Identity, definition, source observations/counts/units, taxa, statuses and prior history are preserved; regeneration repeats identically. |
| EI1 | curation/term_requests.tsv; Exact maintained TSV rows 17 | supports | [[17, {"curator": "claude-opus-5", "date": "2026-08-16", "definition": "An environmental system determined by a bacterium.", "exact_synonym": "", "identifier": "habitatmech:GOLD.029baaef9e", "notes": "The habitat is the host clade, and it is the entire content of the concept: GOLD organises host-associated isolates by host and every anatomical path hangs off it. Not grounded to the parent, because every clade would then merge onto one record. Same pattern ENVO already has at plant-, animal- and fungi-associated environment. GOLD's child of Microbial. Parented to the organism root here because its natural parent, microbe-associated environment, is requested in this same batch and does not exist yet \u2014 editors should re-parent it if both are minted.", "parent_class": "ENVO:01001000", "parent_label": "environmental system determined by an organism", "parent_mode": "ADD", "requested_label": "bacterium-associated environment"}]] |
| EI2 | curation/definition_source_label_exclusions.tsv; Exact maintained TSV rows 2 | supports | [[2, {"curator": "codex-gpt-5", "date": "2026-10-15", "identifier": "habitatmech:GOLD.029baaef9e", "notes": "Review #2167: Bacteria denotes the host organisms, not their associated environment. Remove only this authored exact alias and suppress old-label fallback; retain the environmental definition, genera, verbatim source label/path/count/unit, native status and prior history.", "requested_label": "bacterium-associated environment", "source_label": "Bacteria"}]] |

## Limits And Additional Notes

- Same-agent review is not independent approval. Native scientific status is not promoted by review.
- Predecessor source-member limitations remain; preserving source assertions is not independent confirmation of every sample.
- Full QC, archive integrity and semantic-map/site publication are subsequent gates, not claimed as already passed in this observation.
- Configured ontology checks retain their documented no-adapter skips; they are not global semantic certification.
- Global typed-synonym extraction #1249 and mapping endpoints #1398 remain open. iModulonDB is not applicable; no gene/expression claim is assessed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T095514Z-bacteria-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: bacterium-associated environment (habitatmech:GOLD.029baaef9e)'
started_at: '2026-10-15T09:53:03Z'
finished_at: '2026-10-15T09:55:14Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent performed evidence inspection; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 1 predecessor finding(s) resolved; 0 remain open. The complete current record
  and maintained inputs agree; only scoped parent/synonym claims and appended deterministic
  history change.
source:
  git_revision: 423f501bdb507d335cb198fa27d653ae68949c93
  state: git_commit
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 4544b5d2c11fbbb3a46cd8a65f7e664363df78c1000c590aab533219f9eec59b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce
    role: context
  - path: CLAUDE.md
    sha256: 98d95f910ff5160bc5b2ff572766785519dacdba487700bebaa6dbf96d071fd9
    role: context
  - path: conf/id_label_targets.yaml
    sha256: e100d84aabccaeb00c1a60246142b3cafcec009dbfba58f5cc319c35adddb633
    role: context
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: e54999803277611372ffbad02a795423dc527822d7e900515f27f8824e6b7367
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 6dc8428e469ce29d5d091ec282d39445d07f11eb090e874de1efbe587a080782
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 5c9bd23cb0f681e2880ff13d606b0bf4d47d12fbcf73154260da1d795b801cbe
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: b303b863e16eb805932c8e8fe831cdb82b17518d63a8b3ab0f62fef675cd24cc
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: a2a0496837ea75e487d7fc5d35317a890262a941d8fffe9babcd39f2f332c6db
    role: context
  - path: data/habitats/host_associated/bacteria.yaml
    sha256: b57e45a9dbd0f66ff970ad75e7c512d609bd55a4fe49bcf27b49ee62531f05a1
    role: target
  - path: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
    role: context
  - path: data/habitats/host_associated/microbial__50f690f2.yaml
    sha256: 0a61c7a8e834ed6be95c75fb2162102602fe1fdbec71e83aeecb0eeb720e5143
    role: context
  - path: data/raw/GOLD_MANIFEST.yaml
    sha256: 99ec487ae02d512cfb75440685f927abe907effe52cb755feb095631e8841489
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 4657672d429be35e551ceef4a1204ab0a8120558ce63e2a2b74188eee94b8480
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/bacdive_source_taxa.tsv
    sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
    role: context
  - path: data/raw/environment_parameters.tsv
    sha256: a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/gold_path_biosamples.tsv
    sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
    role: context
  - path: data/raw/gold_path_triads.tsv
    sha256: b1717bd8fc4fdcd6a1a132f4eb32df3638b01ddf7d78f9a5797f110ee2b1e8d6
    role: context
  - path: data/raw/gold_studies.tsv
    sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
    role: context
  - path: data/raw/isolation_source_groundings.tsv
    sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
    role: context
  - path: data/raw/madin_habitat_taxa.tsv
    sha256: d30854cfcffca0405914d04071ac47053938d354d5df250125843131b7c91fd7
    role: context
  - path: data/raw/madin_habitats.tsv
    sha256: 2ae1756f40242600365c49bfbdada4bce5fc8b86630426bb34892f055e5a5c93
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
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/mappings/bacteria/2026-10-15T095055Z-codex-gpt-5-266fd5.yaml
    sha256: bf809a4e863cd377c62ec30efb70f2100d7588eec49886b6c40c2b077ac5554e
    role: context
  - path: history/mappings/bacteria/2026-10-15T095056Z-codex-gpt-5-51ab75.yaml
    sha256: 39486829f67d8c6e3748febd3e5ca590998ae83a31133a410a1274523f959fe5
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261004T095554Z-bacteria.md
    sha256: b7544fcf4a880859dca89993882a70d7ccc360dd9b2ee374a5fdf12b0e4a0bbc
    role: context
  - path: reviews/structured/20261015T093738Z-bacteria-record/review.yaml
    sha256: da44fbe3575fed82d4ec67c3a238ba9ec5804581839c47d7e15b1db4e5cb1e54
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/curate/__init__.py
    sha256: d9837c29dc61d8c9245fdb471a68a109cea31b131cdbc0c4d51d23a8d013ce12
    role: context
  - path: src/habitatmech/curate/causal_graphs.py
    sha256: d1884374263ed7926292c52a58742c614e75628d78ff50fe688e6abc0ddf9c1c
    role: context
  - path: src/habitatmech/curate/curation_event.py
    sha256: 08c774d309fe988c468097518d346f07a653b283cb9b9b51c7fe79fa0af785a9
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
    role: context
  - path: src/habitatmech/curate/definition_source_label_exclusions.py
    sha256: 0c13e83fe17613e8b9f5b346d1259104172f8c1de42f911625579b903707625d
    role: context
  - path: src/habitatmech/curate/definitions.py
    sha256: decd02eea029e884ab1a8bbb51dd870edb5544906b3ddd39598147b27ce572c9
    role: context
  - path: src/habitatmech/curate/external_xrefs.py
    sha256: 8b90ec049887d3aa67e31cce7f7a04d7300421c6fedb833cc66e5d5f5f181694
    role: context
  - path: src/habitatmech/curate/gold_parent_exclusions.py
    sha256: 044d8277509a9b1f6e4f2d7ea1fb82319b41e09ffef7788738a0f4ed0d0b63af
    role: context
  - path: src/habitatmech/curate/record_annotation_corrections.py
    sha256: 15bad3d40fd95e2acc72d3ff3c74289c15fb8a1775adc523b3575c3ea8487033
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/labels.py
    sha256: eb6986c3a9c7d5a3e4651b639351f1f2d3e12d74c4bfaa92899205a1f9df0977
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_gingiva_benign_review_repairs.py
    sha256: d02671704e36a06c58e1a874ae8053517e046b94484fa1a08658b515d50774c3
    role: context
targets:
- target_id: habitatmech:GOLD.029baaef9e
  path: data/habitats/host_associated/bacteria.yaml
  label: bacterium-associated environment
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
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated YAML is not an edit owner
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
scope:
  description: Complete current record re-read and exact predecessor disposition.
  selection: One of ten repaired targets from the twenty-record PR cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.029baaef9e
  exclusions:
  - target: Other records and shared source/export contracts
    reason: The exact parent and synonym witnesses are repaired, not the complete
      corpus or SSSOM/KGX products.
checks:
- check_id: C1
  name: just validate-strict data/habitats/host_associated/attached_keratinized_gingiva.yaml
    data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml data/habitats/host_associated/auditory_hearing_system.yaml
    data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml data/habitats/host_associated/aural.yaml
    data/habitats/host_associated/autopod_pad.yaml data/habitats/host_associated/autotrophic_anf.yaml
    data/habitats/host_associated/axilla.yaml data/habitats/host_associated/b_lymphocyte.yaml
    data/habitats/host_associated/b_lymphocyte_cell_line.yaml data/habitats/host_associated/bacteria.yaml
    data/habitats/host_associated/bacteria__7bc807fd.yaml data/habitats/host_associated/bacteroid.yaml
    data/habitats/host_associated/bark.yaml data/habitats/host_associated/bark__5b1d3b9d.yaml
    data/habitats/host_associated/bartholin_abscess.yaml data/habitats/host_associated/basal_cell_carcinoma.yaml
    data/habitats/host_associated/bcp_1_cell.yaml data/habitats/host_associated/beaker_s_popliteal_cyst.yaml
    data/habitats/host_associated/benign_tumor.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/attached_keratinized_gingiva.yaml
    data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml data/habitats/host_associated/auditory_hearing_system.yaml
    data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml data/habitats/host_associated/aural.yaml
    data/habitats/host_associated/autopod_pad.yaml data/habitats/host_associated/autotrophic_anf.yaml
    data/habitats/host_associated/axilla.yaml data/habitats/host_associated/b_lymphocyte.yaml
    data/habitats/host_associated/b_lymphocyte_cell_line.yaml data/habitats/host_associated/bacteria.yaml
    data/habitats/host_associated/bacteria__7bc807fd.yaml data/habitats/host_associated/bacteroid.yaml
    data/habitats/host_associated/bark.yaml data/habitats/host_associated/bark__5b1d3b9d.yaml
    data/habitats/host_associated/bartholin_abscess.yaml data/habitats/host_associated/basal_cell_carcinoma.yaml
    data/habitats/host_associated/bcp_1_cell.yaml data/habitats/host_associated/beaker_s_popliteal_cyst.yaml
    data/habitats/host_associated/benign_tumor.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.029baaef9e
  summary: "Executed 2026-10-15T09:52:04Z through 2026-10-15T09:52:13Z. uv run python\
    \ scripts/validate_strict.py data/habitats/host_associated/attached_keratinized_gingiva.yaml\
    \ data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml data/habitats/host_associated/auditory_hearing_system.yaml\
    \ data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml data/habitats/host_associated/aural.yaml\
    \ data/habitats/host_associated/autopod_pad.yaml data/habitats/host_associated/autotrophic_anf.yaml\
    \ data/habitats/host_associated/axilla.yaml data/habitats/host_associated/b_lymphocyte.yaml\
    \ data/habitats/host_associated/b_lymphocyte_cell_line.yaml data/habitats/host_associated/bacteria.yaml\
    \ data/habitats/host_associated/bacteria__7bc807fd.yaml data/habitats/host_associated/bacteroid.yaml\
    \ data/habitats/host_associated/bark.yaml data/habitats/host_associated/bark__5b1d3b9d.yaml\
    \ data/habitats/host_associated/bartholin_abscess.yaml data/habitats/host_associated/basal_cell_carcinoma.yaml\
    \ data/habitats/host_associated/bcp_1_cell.yaml data/habitats/host_associated/beaker_s_popliteal_cyst.yaml\
    \ data/habitats/host_associated/benign_tumor.yaml\nValidating 20 files with 15\
    \ workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Strict validation covers twenty targets; history, provenance, corpus,
    causal, term and configured label gates use full native scope; pytest is focused.
- check_id: C2
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.029baaef9e
  summary: 'Executed 2026-10-15T09:52:13Z through 2026-10-15T09:52:24Z. No issues
    found

    789 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Strict validation covers twenty targets; history, provenance, corpus,
    causal, term and configured label gates use full native scope; pytest is focused.
- check_id: C3
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.029baaef9e
  summary: "Executed 2026-10-15T09:52:24Z through 2026-10-15T09:52:25Z. provenance\
    \ current: 14 committed inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Strict validation covers twenty targets; history, provenance, corpus,
    causal, term and configured label gates use full native scope; pytest is focused.
- check_id: C4
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.029baaef9e
  summary: "Executed 2026-10-15T09:52:25Z through 2026-10-15T09:52:47Z. expected 3208\
    \ records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\
    \ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Strict validation covers twenty targets; history, provenance, corpus,
    causal, term and configured label gates use full native scope; pytest is focused.
- check_id: C5
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.029baaef9e
  summary: "Executed 2026-10-15T09:52:47Z through 2026-10-15T09:52:53Z. validated\
    \ 32 causal-graph curation file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Strict validation covers twenty targets; history, provenance, corpus,
    causal, term and configured label gates use full native scope; pytest is focused.
- check_id: C6
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.029baaef9e
  summary: "Executed 2026-10-15T09:52:53Z through 2026-10-15T09:53:21Z. term-request\
    \ table is current (110 terms)\n uv run python scripts/build_term_requests.py\
    \ --check"
  scope_note: Strict validation covers twenty targets; history, provenance, corpus,
    causal, term and configured label gates use full native scope; pytest is focused.
- check_id: C7
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.029baaef9e
  summary: "Executed 2026-10-15T09:53:21Z through 2026-10-15T09:54:36Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n\
    \ uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Strict validation covers twenty targets; history, provenance, corpus,
    causal, term and configured label gates use full native scope; pytest is focused.
- check_id: C8
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python3
    -m pytest -q tests/test_gingiva_benign_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python3
    -m pytest -q tests/test_gingiva_benign_review_repairs.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.029baaef9e
  summary: 'Executed 2026-10-15T09:54:36Z through 2026-10-15T09:54:43Z. .                                                                        [100%]

    1 passed in 6.15s'
  scope_note: Strict validation covers twenty targets; history, provenance, corpus,
    causal, term and configured label gates use full native scope; pytest is focused.
- check_id: C9
  name: git diff --check bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d
  status: passed
  required: true
  command: git diff --check bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.029baaef9e
  summary: 'Executed 2026-10-15T09:54:43Z through 2026-10-15T09:54:43Z. '
  scope_note: Strict validation covers twenty targets; history, provenance, corpus,
    causal, term and configured label gates use full native scope; pytest is focused.
evidence:
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000254/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:35Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_01000254",
    "target": "http://purl.obolibrary.org/obo/RO_0002577", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 743ecf3c761bfce55781906b57a31602e2f4366b29232406d53b40aaf75fcb78
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000254
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:34Z'
  support: supports
  summary: ENVO:01000254 environmental system; inspected definition and typed scope.
    ["In ENVO's alignment with the Basic Formal Ontology, this class is being considered
    as a subclass of a proposed BFO class \"system\". The relation \"environed_by\"
    is also under development. Roughly, a system which includes a material entity
    (at least partially) within its site and causally influences that entity may be
    considered to environ it. Following the completion of this alignment, this class'
    definition and the definitions of its subclasses will be revised.", "A system
    which has the disposition to environ one or more material entities."]
  snapshot_sha256: 6400120603ffe93953d6ea567a86900fc6692a8538ed015eb299135e2a98dd8b
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:36Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: e11b34dbd0a626083d5d0bbbb364469ef95831fb61cb81da5377d59715b272ca
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:35Z'
  support: supports
  summary: ENVO:01001000 environmental system determined by an organism; inspected
    definition and typed scope. ["An environmental system which is determined by a
    living organism."]
  snapshot_sha256: 8bd797929d18bf28171af7fd10f358db9b093f752d20b99f665779bb2e6b504e
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/bacteria.yaml
  locator: Entire regenerated YAML
  accessed_at: '2026-10-15T09:55:14Z'
  support: supports
  summary: 'Complete current record inspected: {"curation_history": [{"action": "CONFIRM_UNGROUNDED",
    "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. GOLD''s
    Host-associated > Microbial > Bacteria: bacteria acting as host for another microbe.
    No environment term exists for a microbial host; ENVO''s organism-associated terms
    cover plants and animals only. ENVO term request. (source concept habitatmech:GOLD.029baaef9e)",
    "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "DEFINED",
    "changes": "Defined as ''bacterium-associated environment'' under ENVO:01001000
    ''environmental system determined by an organism''. The habitat is the host clade,
    and it is the entire content of the concept: GOLD organises host-associated isolates
    by host and every anatomical path hangs off it. Not grounded to the parent, because
    every clade would then merge onto one record. Same pattern ENVO already has at
    plant-, animal- and fungi-associated environment. GOLD''s child of Microbial.
    Parented to the organism root here because its natural parent, microbe-associated
    environment, is requested in this same batch and does not exist yet \u2014 editors
    should re-parent it if both are minted.", "curator": "claude-opus-5", "timestamp":
    "2026-08-16T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED.", "curator":
    "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "SOURCE_SYNONYM_EXCLUDED",
    "changes": "Omitted automatic retention of displaced source label ''Bacteria''
    when defining habitatmech:GOLD.029baaef9e as ''bacterium-associated environment''.
    Verbatim source attestations are preserved. Review #2167: Bacteria denotes the
    host organisms, not their associated environment. Remove only this authored exact
    alias and suppress old-label fallback; retain the environmental definition, genera,
    verbatim source label/path/count/unit, native status and prior history.", "curator":
    "codex-gpt-5", "timestamp": "2026-10-15T00:00:00Z"}], "definition": "An environmental
    system determined by a bacterium.", "definition_source": "HabitatMech", "grounding_status":
    "UNGROUNDED", "habitat_category": "HOST_ASSOCIATED", "identifier": "habitatmech:GOLD.029baaef9e",
    "label": "bacterium-associated environment", "mapping_status": "REVIEWED", "parent_habitats":
    ["ENVO:01001000", "habitatmech:GOLD.184623c963"], "source_attestations": [{"assertion_count":
    3017, "assertion_unit": "ORGANISM", "notes": "3 GOLD ecosystem node ids share
    this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD",
    "source_id": "gold.ecosystem:3540", "source_label": "Bacteria", "source_path":
    "Host-associated > Microbial > Bacteria"}]}'
  snapshot_sha256: b57e45a9dbd0f66ff970ad75e7c512d609bd55a4fe49bcf27b49ee62531f05a1
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T093738Z-bacteria-record/review.yaml
  locator: Exact immutable predecessor and all findings
  accessed_at: '2026-10-15T09:55:14Z'
  support: supports
  summary: Original evidence, limitations and finding identities remain preserved.
  snapshot_sha256: da44fbe3575fed82d4ec67c3a238ba9ec5804581839c47d7e15b1db4e5cb1e54
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_gingiva_benign_review_repairs.py
  locator: Whole-corpus counterfactual regression
  accessed_at: '2026-10-15T09:55:14Z'
  support: supports
  summary: 'Restores only the prior rules in memory: exactly ten records change. Identity,
    definition, source observations/counts/units, taxa, statuses and prior history
    are preserved; regeneration repeats identically.'
  snapshot_sha256: d02671704e36a06c58e1a874ae8053517e046b94484fa1a08658b515d50774c3
- evidence_id: EI1
  kind: record_content
  reference: curation/term_requests.tsv
  locator: Exact maintained TSV rows 17
  accessed_at: '2026-10-15T09:55:14Z'
  support: supports
  summary: '[[17, {"curator": "claude-opus-5", "date": "2026-08-16", "definition":
    "An environmental system determined by a bacterium.", "exact_synonym": "", "identifier":
    "habitatmech:GOLD.029baaef9e", "notes": "The habitat is the host clade, and it
    is the entire content of the concept: GOLD organises host-associated isolates
    by host and every anatomical path hangs off it. Not grounded to the parent, because
    every clade would then merge onto one record. Same pattern ENVO already has at
    plant-, animal- and fungi-associated environment. GOLD''s child of Microbial.
    Parented to the organism root here because its natural parent, microbe-associated
    environment, is requested in this same batch and does not exist yet \u2014 editors
    should re-parent it if both are minted.", "parent_class": "ENVO:01001000", "parent_label":
    "environmental system determined by an organism", "parent_mode": "ADD", "requested_label":
    "bacterium-associated environment"}]]'
  snapshot_sha256: b303b863e16eb805932c8e8fe831cdb82b17518d63a8b3ab0f62fef675cd24cc
- evidence_id: EI2
  kind: record_content
  reference: curation/definition_source_label_exclusions.tsv
  locator: Exact maintained TSV rows 2
  accessed_at: '2026-10-15T09:55:14Z'
  support: supports
  summary: '[[2, {"curator": "codex-gpt-5", "date": "2026-10-15", "identifier": "habitatmech:GOLD.029baaef9e",
    "notes": "Review #2167: Bacteria denotes the host organisms, not their associated
    environment. Remove only this authored exact alias and suppress old-label fallback;
    retain the environmental definition, genera, verbatim source label/path/count/unit,
    native status and prior history.", "requested_label": "bacterium-associated environment",
    "source_label": "Bacteria"}]]'
  snapshot_sha256: e54999803277611372ffbad02a795423dc527822d7e900515f27f8824e6b7367
assessments:
- assessment_id: A1
  area: consistency
  topic: Scoped repairs and complete-record preservation
  outcome: supported
  summary: Counterfactual and complete-record checks establish exactly the intended
    bounded changes and preserve identities, definitions, source observations, statuses,
    valid parents and prior history.
  target_ids:
  - habitatmech:GOLD.029baaef9e
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI1
  - EI2
- assessment_id: A2
  area: evidence
  topic: Retained scientific support
  outcome: supported
  summary: Rechecked complete target against the inspected typed ontology and bounded
    primary evidence retained from its predecessor. No new prevalence, mechanism or
    characteristic-presence claim is added.
  target_ids:
  - habitatmech:GOLD.029baaef9e
  evidence_ids:
  - EAFTER
  - EPREV
  - EX1
  - EX2
  - EX3
  - EX4
findings:
- finding_id: F1
  issue_key: bacteria-host-name-exact-synonym
  category: nomenclature
  severity: major
  status: resolved
  certainty: confirmed
  title: Whole-host name is an exact environmental synonym
  description: Remove only Bacteria from the exact_synonym cell for habitatmech:GOLD.029baaef9e
    and add a guarded definition_source_label_exclusions.tsv row preventing automatic
    old-label fallback. Preserve the environmental definition, genus, minted identity,
    source label/path and counts.
  target_ids:
  - habitatmech:GOLD.029baaef9e
  field_paths:
  - synonyms
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI1
  - EI2
  - EX1
  - EX2
  - EX3
  - EX4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2167
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T093738Z-bacteria-record
    finding_id: F1
  disposition_reason: Removed the authored whole-host exact alias and explicitly blocked
    old-label fallback. The environmental definition, genera, verbatim source label/path/count
    and native status are unchanged.
actions: []
limitations:
- Same-agent review is not independent approval. Native scientific status is not promoted
  by review.
- Predecessor source-member limitations remain; preserving source assertions is not
  independent confirmation of every sample.
- Full QC, archive integrity and semantic-map/site publication are subsequent gates,
  not claimed as already passed in this observation.
- Configured ontology checks retain their documented no-adapter skips; they are not
  global semantic certification.
- 'Global typed-synonym extraction #1249 and mapping endpoints #1398 remain open.
  iModulonDB is not applicable; no gene/expression claim is assessed.'
notes: []
tags:
- individual-scientific-review
- remediation
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T093738Z-bacteria-record
  relationship: Exact predecessor; every finding identity and disposition lineage
    retained.
```
