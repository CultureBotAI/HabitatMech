# Remediation review: Anal canal (habitatmech:GOLD.a2d2eb3d96)

- Review: 20261015T043311Z-anal_canal-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T04:30:26Z
- Finished UTC: 2026-10-15T04:33:11Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

1 predecessor finding(s) resolved; 1 remain open. The complete current record preserves its source identity and provenance. The remaining issue is not hidden by the scoped repair.

## Scope And Provenance

Full current record re-read with scoped remediation of the exact predecessor findings.

Selection: One exact record from the twelve-record authorized PR repair cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 2f52e94e2929ea1aa85ecf61f43d48afa1edb035.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.a2d2eb3d96 | data/habitats/host_associated/anal_canal.yaml | generated | Anal canal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate-strict data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml | passed | True | habitatmech:GOLD.a2d2eb3d96 | Actual successful execution 2026-10-15T04:26:07Z through 2026-10-15T04:26:19Z. uv run python scripts/validate_strict.py data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml<br>Validating 12 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      12<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.a2d2eb3d96 | Actual successful execution 2026-10-15T04:26:19Z through 2026-10-15T04:26:35Z. No issues found<br>744 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.a2d2eb3d96 | Actual successful execution 2026-10-15T04:26:35Z through 2026-10-15T04:26:36Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.a2d2eb3d96 | Actual successful execution 2026-10-15T04:26:36Z through 2026-10-15T04:27:01Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.a2d2eb3d96 | Actual successful execution 2026-10-15T04:27:01Z through 2026-10-15T04:27:12Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.a2d2eb3d96 | Actual successful execution 2026-10-15T04:27:12Z through 2026-10-15T04:27:41Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.a2d2eb3d96 | Actual successful execution 2026-10-15T04:27:41Z through 2026-10-15T04:28:43Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_host_anatomy_review_repairs.py | passed | True | habitatmech:GOLD.a2d2eb3d96 | Actual successful execution 2026-10-15T04:28:43Z through 2026-10-15T04:28:52Z. .                                                                        [100%]<br>1 passed in 7.53s |
| git diff --check ea0bf6a2629ffcd2ed086310a5eee162d4f11cae | passed | True | habitatmech:GOLD.a2d2eb3d96 | Actual successful execution 2026-10-15T04:28:52Z through 2026-10-15T04:28:52Z.  |

## Scientific And Domain Assessments

### Scoped corrections and retained scientific identity

consistency: supported. Targets: habitatmech:GOLD.a2d2eb3d96.

Generated record and maintained owners agree. Exactly the expected field-level changes are present; valid ontology identity/genus, source path/node/count semantics and unrelated corpus records are preserved. The previous generated history is retained; any new exclusion/correction events are appended.

### Primary-source scope and optional fields

evidence: supported. Targets: habitatmech:GOLD.a2d2eb3d96.

Retained anatomical or host-environment claims were rechecked against the predecessor primary evidence and current target. No new mechanism, characteristic taxon, prevalence, specimen identity or universal clade-level property is added. Source counts remain historical attestations.

### Unresolved scoped findings

representation: concern. Targets: habitatmech:GOLD.a2d2eb3d96.

Narrow predicate compares a different endpoint than the schema declares

## Findings

### F1: Source context is asserted as a broader habitat

major / resolved / confirmed; issue key: anal-canal-source-parent.

The human anal canal is a terminal part of the large intestine, not a subtype of the whole organ. Exclude only the guarded immediate GOLD contribution habitatmech:GOLD.5b0aa7456c in gold_parent_exclusions.tsv; preserve independent ontology parents and verbatim source provenance.

Disposition: The exact guarded GOLD context contribution is removed; independently supported ontology parents and original source fields remain.

### F2: Narrow predicate compares a different endpoint than the schema declares

major / open / confirmed; issue key: anal-canal-mapping-endpoint-contract.

Native execution retains the source minted ID but copies skos:narrowMatch into source-to-record attestation. The actual narrower comparison is to an ontology parent, not the retained record. Resolve shared schema/producer/consumer endpoints under #1398; a broad/narrow swap or an unsupported ontology merge is not a fix. No formal SKOS self-link prohibition or SSSOM/KGX conformance is claimed.

Disposition: Rechecked and still present. The bounded parent/synonym corrections do not establish the missing source interpretation or reconcile the shared endpoint contract.

## Recommended Actions And Acceptance Checks

### ACT2

Native execution retains the source minted ID but copies skos:narrowMatch into source-to-record attestation. The actual narrower comparison is to an ontology parent, not the retained record. Resolve shared schema/producer/consumer endpoints under #1398; a broad/narrow swap or an unsupported ontology merge is not a fix. No formal SKOS self-link prohibition or SSSOM/KGX conformance is claimed. Correct only through the named maintained owners; do not patch generated YAML.

- Regress this exact source/record and retained valid claims, with all-source identity, count/unit and status invariants.
- Append authorized session history; run strict schema, history, provenance, exact corpus reproduction, configured label validation and full just qc.
- Compare actual semantic input and rebuild map/site as needed; retain existing URLs and save an immutable successor with exact finding lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000159; Target term fields and typed relations, or primary abstract | supports | Inspected current authoritative term UBERON:0000159 (anal canal), definition and obsolete flag False. Its scoped meaning is compared with the complete GOLD path in the scientific assessment. |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000159/graph; Target term fields and typed relations, or primary abstract | supports | Inspected typed outgoing edges: [{"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0004111", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}, {"label": "part of", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0000059", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}, {"label": "continuous with", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0001052", "uri": "http://purl.obolibrary.org/obo/RO_0002150"}, {"label": "continuous with", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0001245", "uri": "http://purl.obolibrary.org/obo/RO_0002150"}, {"label": "part of", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0001353", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}, {"label": "channel for", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0001988", "uri": "http://purl.obolibrary.org/obo/uberon/core#channel_for"}, {"label": "develops from", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0011272", "uri": "http://purl.obolibrary.org/obo/RO_0002202"}]. Relation labels remain distinct; containment is not promoted to subclass. |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059; Target term fields and typed relations, or primary abstract | supports | Inspected current authoritative term UBERON:0000059 (large intestine), definition and obsolete flag False. Its scoped meaning is compared with the complete GOLD path in the scientific assessment. |
| EAFTER | data/habitats/host_associated/anal_canal.yaml; Entire current generated YAML | supports | Complete post-fix record re-read: {"curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.5b0aa7456c for habitatmech:GOLD.a2d2eb3d96 (Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Large intestine &gt; Anal canal). Scientific review #1325: the human anal canal is part of the large intestine, not a kind of whole large intestine. Current UBERON:0000159 positively distinguishes part_of from subClassOf anatomical conduit. Exclude only this source-parent contribution; retain independent UBERON:0000159, node 6285, one ORGANISM assertion, full path and NARROW/SEEDED state. Shared mapping-endpoint issue #1398 remains open. https://purl.obolibrary.org/obo/UBERON_0000159", "curator": "codex-gpt-5", "timestamp": "2026-10-15T00:00:00Z"}], "grounding_status": "NARROW", "habitat_category": "HOST_ASSOCIATED", "identifier": "habitatmech:GOLD.a2d2eb3d96", "label": "Anal canal", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000159"], "source_attestations": [{"assertion_count": 1, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:narrowMatch", "source": "GOLD", "source_id": "gold.ecosystem:6285", "source_label": "Anal canal", "source_path": "Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Large intestine &gt; Anal canal"}]} |
| EPREV | reviews/structured/20261015T041830Z-anal_canal-record/review.yaml; Complete immutable pre-fix scientific review | supports | Original scoped evidence and all normalized findings remain unchanged. |
| ETEST | tests/test_host_anatomy_review_repairs.py; Complete corpus counterfactual and repeated seeding test | supports | Test restores the old maintained semantics in memory and proves exactly twelve changed records, preserved identities and unrelated fields; it checks host fallback, source counts, valid parents and all fornix synonym scopes. |
| EI0 | curation/decisions.tsv; Exact identifier/source key habitatmech:GOLD.a2d2eb3d96; generated identifier habitatmech:GOLD.a2d2eb3d96 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |
| EI1 | curation/term_requests.tsv; Exact identifier/source key habitatmech:GOLD.a2d2eb3d96; generated identifier habitatmech:GOLD.a2d2eb3d96 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |
| EI2 | curation/gold_parent_exclusions.tsv; Exact identifier/source key habitatmech:GOLD.a2d2eb3d96; generated identifier habitatmech:GOLD.a2d2eb3d96 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |
| EI3 | curation/record_annotation_corrections.tsv; Exact identifier/source key habitatmech:GOLD.a2d2eb3d96; generated identifier habitatmech:GOLD.a2d2eb3d96 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |

## Limits And Additional Notes

- Continuing-agent self-review, not independent approval. Native status is not promoted by this observation.
- Original GOLD organism/member identities remain unverified. Ontology and paper evidence retains the narrow scope and access limitations of the predecessor.
- Full map/site, immutable archive and full QC are separate publication gates and are not claimed as already passed here.
- The shared endpoint problem #1398 and typed-synonym extraction #1249 remain open outside any repaired local witness.
- No paid research or transcriptomic inference was performed. iModulonDB is not applicable.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T043311Z-anal_canal-remediation
kind: record
repository: CultureBotAI/HabitatMech
title: 'Remediation review: Anal canal (habitatmech:GOLD.a2d2eb3d96)'
started_at: '2026-10-15T04:30:26Z'
finished_at: '2026-10-15T04:33:11Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Continuing agent assessed complete records and primary evidence;
    this is not independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 1 predecessor finding(s) resolved; 1 remain open. The complete current record
  preserves its source identity and provenance. The remaining issue is not hidden
  by the scoped repair.
source:
  git_revision: 2f52e94e2929ea1aa85ecf61f43d48afa1edb035
  state: git_commit
  inputs:
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: curation/decisions.tsv
    sha256: 3f18e736384e6eece8e9c3c7e371714b8b3cef474de661e0e717705ee1341db7
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 761c1c1c60358c6c24e4d797637a12bdde6f8541e568914b404bffd1e0dd57ec
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: ea37676f1a16dd05fbfbb6c394b3f14b42ea93b763fb257043b817a4f10d3612
    role: context
  - path: curation/term_requests.tsv
    sha256: 2144d43ab4e106ff820da87c348f673d16cb8ea30d5a565f12e156af598f85ad
    role: context
  - path: data/habitats/host_associated/anal_canal.yaml
    sha256: 6ee7e60acc8023a2c9326737a1a6a06ed1b7566e8341014e61428614823d0a01
    role: target
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/ontology_subclass_edges.tsv
    sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
    role: context
  - path: data/raw/ontology_terms.tsv
    sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
    role: context
  - path: docs/CURATION.md
    sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/record-review-profile.md
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/mappings/anal_canal/2026-10-15T042453Z-codex-gpt-5-5b2adf.yaml
    sha256: ce6449bfbf2c699756bdd886f0d0f68798781cda58ed593ea1ee6affa4a696e1
    role: context
  - path: reviews/structured/20261015T041830Z-anal_canal-record/review.yaml
    sha256: 2fa3cfc986b02173b3fda32a87f14a52744193502a5c06d93a92127788bcb41e
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_host_anatomy_review_repairs.py
    sha256: 5c0a954d3373998c98dd57d219db062b9a2ad22a8cfea00ca399d91b0648f7d3
    role: context
targets:
- target_id: habitatmech:GOLD.a2d2eb3d96
  path: data/habitats/host_associated/anal_canal.yaml
  label: Anal canal
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; generated habitat files are read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; generated habitat files are read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated habitat files are read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; generated habitat files are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated habitat files are read-only
scope:
  description: Full current record re-read with scoped remediation of the exact predecessor
    findings.
  selection: One exact record from the twelve-record authorized PR repair cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  exclusions:
  - target: Global source modeling, other records and SSSOM/KGX conformance
    reason: No global endpoint, synonym-extraction or source-member certification.
checks:
- check_id: C1
  name: just validate-strict data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml
    data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml
    data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml
    data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml
    data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml
    data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml
    data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml
    data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml
    data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml
    data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml
    data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  summary: "Actual successful execution 2026-10-15T04:26:07Z through 2026-10-15T04:26:19Z.\
    \ uv run python scripts/validate_strict.py data/habitats/host_associated/amphibia.yaml\
    \ data/habitats/host_associated/anaerobic.yaml data/habitats/host_associated/anal_canal.yaml\
    \ data/habitats/host_associated/anal_canal__0e185227.yaml data/habitats/host_associated/anal_canal_mucosa.yaml\
    \ data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml data/habitats/host_associated/annelida.yaml\
    \ data/habitats/host_associated/anorectal_abscess.yaml data/habitats/host_associated/antennal_gland.yaml\
    \ data/habitats/host_associated/anterior.yaml data/habitats/host_associated/anterior_chamber.yaml\
    \ data/habitats/host_associated/anterior_fornix_of_vagina.yaml\nValidating 12\
    \ files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      12\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
- check_id: C2
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  summary: 'Actual successful execution 2026-10-15T04:26:19Z through 2026-10-15T04:26:35Z.
    No issues found

    744 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
- check_id: C3
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  summary: "Actual successful execution 2026-10-15T04:26:35Z through 2026-10-15T04:26:36Z.\
    \ provenance current: 14 committed inventories, 2 GOLD sources\n uv run python\
    \ scripts/check_provenance.py"
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
- check_id: C4
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  summary: "Actual successful execution 2026-10-15T04:26:36Z through 2026-10-15T04:27:01Z.\
    \ expected 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n\
    \  differing: 0\n\ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
- check_id: C5
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  summary: "Actual successful execution 2026-10-15T04:27:01Z through 2026-10-15T04:27:12Z.\
    \ validated 32 causal-graph curation file(s) with 32 graph(s)\n uv run python\
    \ scripts/validate_causal_graph_curations.py"
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
- check_id: C6
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  summary: "Actual successful execution 2026-10-15T04:27:12Z through 2026-10-15T04:27:41Z.\
    \ term-request table is current (110 terms)\n uv run python scripts/build_term_requests.py\
    \ --check"
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
- check_id: C7
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  summary: "Actual successful execution 2026-10-15T04:27:41Z through 2026-10-15T04:28:43Z.\
    \ id↔label correspondence summary:\n          OK_CANONICAL: 1174\n           \
    \ OK_SYNONYM: 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅\
    \ All id↔label pairs correspond.\n uv run python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml"
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
- check_id: C8
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_host_anatomy_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_host_anatomy_review_repairs.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  summary: 'Actual successful execution 2026-10-15T04:28:43Z through 2026-10-15T04:28:52Z.
    .                                                                        [100%]

    1 passed in 7.53s'
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
- check_id: C9
  name: git diff --check ea0bf6a2629ffcd2ed086310a5eee162d4f11cae
  status: passed
  required: true
  command: git diff --check ea0bf6a2629ffcd2ed086310a5eee162d4f11cae
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  summary: 'Actual successful execution 2026-10-15T04:28:52Z through 2026-10-15T04:28:52Z. '
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
evidence:
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000159
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:04:38Z'
  support: supports
  summary: Inspected current authoritative term UBERON:0000159 (anal canal), definition
    and obsolete flag False. Its scoped meaning is compared with the complete GOLD
    path in the scientific assessment.
  snapshot_sha256: 7fc4ee47acc70030aebb13083fbc09ef38c1855e37b63d578100ac8a8c01cf8f
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000159/graph
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:05:20Z'
  support: supports
  summary: 'Inspected typed outgoing edges: [{"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004111", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"},
    {"label": "part of", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000059", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"},
    {"label": "continuous with", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001052", "uri": "http://purl.obolibrary.org/obo/RO_0002150"},
    {"label": "continuous with", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001245", "uri": "http://purl.obolibrary.org/obo/RO_0002150"},
    {"label": "part of", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001353", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"},
    {"label": "channel for", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001988", "uri": "http://purl.obolibrary.org/obo/uberon/core#channel_for"},
    {"label": "develops from", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0011272", "uri": "http://purl.obolibrary.org/obo/RO_0002202"}].
    Relation labels remain distinct; containment is not promoted to subclass.'
  snapshot_sha256: f12805206dabe9442d32d9cbb027d9ae3246a2160074e23103f8a6c676fdec99
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:05:15Z'
  support: supports
  summary: Inspected current authoritative term UBERON:0000059 (large intestine),
    definition and obsolete flag False. Its scoped meaning is compared with the complete
    GOLD path in the scientific assessment.
  snapshot_sha256: d43e203ec23dc43e60bf4f3eeef91235a695dc997d4784a65919688f223aaba8
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/anal_canal.yaml
  locator: Entire current generated YAML
  accessed_at: '2026-10-15T04:33:11Z'
  support: supports
  summary: 'Complete post-fix record re-read: {"curation_history": [{"action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW.",
    "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action":
    "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution
    habitatmech:GOLD.5b0aa7456c for habitatmech:GOLD.a2d2eb3d96 (Host-associated >
    Mammals: Human > Digestive system > Large intestine > Anal canal). Scientific
    review #1325: the human anal canal is part of the large intestine, not a kind
    of whole large intestine. Current UBERON:0000159 positively distinguishes part_of
    from subClassOf anatomical conduit. Exclude only this source-parent contribution;
    retain independent UBERON:0000159, node 6285, one ORGANISM assertion, full path
    and NARROW/SEEDED state. Shared mapping-endpoint issue #1398 remains open. https://purl.obolibrary.org/obo/UBERON_0000159",
    "curator": "codex-gpt-5", "timestamp": "2026-10-15T00:00:00Z"}], "grounding_status":
    "NARROW", "habitat_category": "HOST_ASSOCIATED", "identifier": "habitatmech:GOLD.a2d2eb3d96",
    "label": "Anal canal", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000159"],
    "source_attestations": [{"assertion_count": 1, "assertion_unit": "ORGANISM", "mapping_predicate":
    "skos:narrowMatch", "source": "GOLD", "source_id": "gold.ecosystem:6285", "source_label":
    "Anal canal", "source_path": "Host-associated > Mammals: Human > Digestive system
    > Large intestine > Anal canal"}]}'
  snapshot_sha256: 6ee7e60acc8023a2c9326737a1a6a06ed1b7566e8341014e61428614823d0a01
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T041830Z-anal_canal-record/review.yaml
  locator: Complete immutable pre-fix scientific review
  accessed_at: '2026-10-15T04:33:11Z'
  support: supports
  summary: Original scoped evidence and all normalized findings remain unchanged.
  snapshot_sha256: 2fa3cfc986b02173b3fda32a87f14a52744193502a5c06d93a92127788bcb41e
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_host_anatomy_review_repairs.py
  locator: Complete corpus counterfactual and repeated seeding test
  accessed_at: '2026-10-15T04:33:11Z'
  support: supports
  summary: Test restores the old maintained semantics in memory and proves exactly
    twelve changed records, preserved identities and unrelated fields; it checks host
    fallback, source counts, valid parents and all fornix synonym scopes.
  snapshot_sha256: 5c0a954d3373998c98dd57d219db062b9a2ad22a8cfea00ca399d91b0648f7d3
- evidence_id: EI0
  kind: record_content
  reference: curation/decisions.tsv
  locator: Exact identifier/source key habitatmech:GOLD.a2d2eb3d96; generated identifier
    habitatmech:GOLD.a2d2eb3d96
  accessed_at: '2026-10-15T04:33:11Z'
  support: supports
  summary: Maintained rows inspected and rechecked against the generated delta and
    predecessor. No raw inventories or generator implementation were edited.
  snapshot_sha256: 3f18e736384e6eece8e9c3c7e371714b8b3cef474de661e0e717705ee1341db7
- evidence_id: EI1
  kind: record_content
  reference: curation/term_requests.tsv
  locator: Exact identifier/source key habitatmech:GOLD.a2d2eb3d96; generated identifier
    habitatmech:GOLD.a2d2eb3d96
  accessed_at: '2026-10-15T04:33:11Z'
  support: supports
  summary: Maintained rows inspected and rechecked against the generated delta and
    predecessor. No raw inventories or generator implementation were edited.
  snapshot_sha256: 2144d43ab4e106ff820da87c348f673d16cb8ea30d5a565f12e156af598f85ad
- evidence_id: EI2
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact identifier/source key habitatmech:GOLD.a2d2eb3d96; generated identifier
    habitatmech:GOLD.a2d2eb3d96
  accessed_at: '2026-10-15T04:33:11Z'
  support: supports
  summary: Maintained rows inspected and rechecked against the generated delta and
    predecessor. No raw inventories or generator implementation were edited.
  snapshot_sha256: 761c1c1c60358c6c24e4d797637a12bdde6f8541e568914b404bffd1e0dd57ec
- evidence_id: EI3
  kind: record_content
  reference: curation/record_annotation_corrections.tsv
  locator: Exact identifier/source key habitatmech:GOLD.a2d2eb3d96; generated identifier
    habitatmech:GOLD.a2d2eb3d96
  accessed_at: '2026-10-15T04:33:11Z'
  support: supports
  summary: Maintained rows inspected and rechecked against the generated delta and
    predecessor. No raw inventories or generator implementation were edited.
  snapshot_sha256: ea37676f1a16dd05fbfbb6c394b3f14b42ea93b763fb257043b817a4f10d3612
assessments:
- assessment_id: A1
  area: consistency
  topic: Scoped corrections and retained scientific identity
  outcome: supported
  summary: Generated record and maintained owners agree. Exactly the expected field-level
    changes are present; valid ontology identity/genus, source path/node/count semantics
    and unrelated corpus records are preserved. The previous generated history is
    retained; any new exclusion/correction events are appended.
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI0
  - EI1
  - EI2
  - EI3
- assessment_id: A2
  area: evidence
  topic: Primary-source scope and optional fields
  outcome: supported
  summary: Retained anatomical or host-environment claims were rechecked against the
    predecessor primary evidence and current target. No new mechanism, characteristic
    taxon, prevalence, specimen identity or universal clade-level property is added.
    Source counts remain historical attestations.
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  evidence_ids:
  - EAFTER
  - EPREV
  - EX1
  - EX2
  - EX3
- assessment_id: A3
  area: representation
  topic: Unresolved scoped findings
  outcome: concern
  summary: Narrow predicate compares a different endpoint than the schema declares
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  evidence_ids:
  - EAFTER
  - EPREV
findings:
- finding_id: F1
  issue_key: anal-canal-source-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is asserted as a broader habitat
  description: The human anal canal is a terminal part of the large intestine, not
    a subtype of the whole organ. Exclude only the guarded immediate GOLD contribution
    habitatmech:GOLD.5b0aa7456c in gold_parent_exclusions.tsv; preserve independent
    ontology parents and verbatim source provenance.
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  field_paths:
  - parent_habitats
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI0
  - EI1
  - EI2
  - EI3
  - EX1
  - EX2
  - EX3
  rule_id: docs/CURATION.md; SourceAttestation contract; native record-review checklist
  native_severity: major
  normalization_reason: Material semantic error; schema validity does not establish
    this claim.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated habitat files are read-only
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1325
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T041830Z-anal_canal-record
    finding_id: F1
  disposition_reason: The exact guarded GOLD context contribution is removed; independently
    supported ontology parents and original source fields remain.
- finding_id: F2
  issue_key: anal-canal-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow predicate compares a different endpoint than the schema declares
  description: 'Native execution retains the source minted ID but copies skos:narrowMatch
    into source-to-record attestation. The actual narrower comparison is to an ontology
    parent, not the retained record. Resolve shared schema/producer/consumer endpoints
    under #1398; a broad/narrow swap or an unsupported ontology merge is not a fix.
    No formal SKOS self-link prohibition or SSSOM/KGX conformance is claimed.'
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  field_paths:
  - grounding_status
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI0
  - EI1
  - EI2
  - EI3
  - EX1
  - EX2
  - EX3
  rule_id: docs/CURATION.md; SourceAttestation contract; native record-review checklist
  native_severity: major
  normalization_reason: Material semantic error; schema validity does not establish
    this claim.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; generated habitat files are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated habitat files are read-only
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T041830Z-anal_canal-record
    finding_id: F2
  disposition_reason: Rechecked and still present. The bounded parent/synonym corrections
    do not establish the missing source interpretation or reconcile the shared endpoint
    contract.
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.a2d2eb3d96
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; generated habitat files are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated habitat files are read-only
  description: 'Native execution retains the source minted ID but copies skos:narrowMatch
    into source-to-record attestation. The actual narrower comparison is to an ontology
    parent, not the retained record. Resolve shared schema/producer/consumer endpoints
    under #1398; a broad/narrow swap or an unsupported ontology merge is not a fix.
    No formal SKOS self-link prohibition or SSSOM/KGX conformance is claimed. Correct
    only through the named maintained owners; do not patch generated YAML.'
  generator: just seed; inspect just seed-canary before seed-apply; regenerate affected
    term requests, map and pages through supported commands
  acceptance_checks:
  - Regress this exact source/record and retained valid claims, with all-source identity,
    count/unit and status invariants.
  - Append authorized session history; run strict schema, history, provenance, exact
    corpus reproduction, configured label validation and full just qc.
  - Compare actual semantic input and rebuild map/site as needed; retain existing
    URLs and save an immutable successor with exact finding lineage.
limitations:
- Continuing-agent self-review, not independent approval. Native status is not promoted
  by this observation.
- Original GOLD organism/member identities remain unverified. Ontology and paper evidence
  retains the narrow scope and access limitations of the predecessor.
- Full map/site, immutable archive and full QC are separate publication gates and
  are not claimed as already passed here.
- 'The shared endpoint problem #1398 and typed-synonym extraction #1249 remain open
  outside any repaired local witness.'
- No paid research or transcriptomic inference was performed. iModulonDB is not applicable.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T041830Z-anal_canal-record
  relationship: Exact pre-fix predecessor; all finding identities retained.
tags:
- individual-scientific-review
- remediation
- host-associated
```
