# Remediation review: Anterior chamber (habitatmech:GOLD.53e4290463)

- Review: 20261015T043316Z-anterior_chamber-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T04:31:09Z
- Finished UTC: 2026-10-15T04:33:16Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

3 predecessor finding(s) resolved; 0 remain open. The complete current record preserves its source identity and provenance. The corrected claims are supported within the documented source and evidence limits.

## Scope And Provenance

Full current record re-read with scoped remediation of the exact predecessor findings.

Selection: One exact record from the twelve-record authorized PR repair cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 2f52e94e2929ea1aa85ecf61f43d48afa1edb035.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.53e4290463 | data/habitats/host_associated/anterior_chamber.yaml | generated | Anterior chamber |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate-strict data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml | passed | True | habitatmech:GOLD.53e4290463 | Actual successful execution 2026-10-15T04:26:07Z through 2026-10-15T04:26:19Z. uv run python scripts/validate_strict.py data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml<br>Validating 12 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      12<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.53e4290463 | Actual successful execution 2026-10-15T04:26:19Z through 2026-10-15T04:26:35Z. No issues found<br>744 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.53e4290463 | Actual successful execution 2026-10-15T04:26:35Z through 2026-10-15T04:26:36Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.53e4290463 | Actual successful execution 2026-10-15T04:26:36Z through 2026-10-15T04:27:01Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.53e4290463 | Actual successful execution 2026-10-15T04:27:01Z through 2026-10-15T04:27:12Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.53e4290463 | Actual successful execution 2026-10-15T04:27:12Z through 2026-10-15T04:27:41Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.53e4290463 | Actual successful execution 2026-10-15T04:27:41Z through 2026-10-15T04:28:43Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_host_anatomy_review_repairs.py | passed | True | habitatmech:GOLD.53e4290463 | Actual successful execution 2026-10-15T04:28:43Z through 2026-10-15T04:28:52Z. .                                                                        [100%]<br>1 passed in 7.53s |
| git diff --check ea0bf6a2629ffcd2ed086310a5eee162d4f11cae | passed | True | habitatmech:GOLD.53e4290463 | Actual successful execution 2026-10-15T04:28:52Z through 2026-10-15T04:28:52Z.  |

## Scientific And Domain Assessments

### Scoped corrections and retained scientific identity

consistency: supported. Targets: habitatmech:GOLD.53e4290463.

Generated record and maintained owners agree. Exactly the expected field-level changes are present; valid ontology identity/genus, source path/node/count semantics and unrelated corpus records are preserved. The chamber remains a real regional habitat with no verified suitable grounding; its generated history reflects the new decision, while the old decision is preserved in the predecessor/Git and the append-only curation session.

### Primary-source scope and optional fields

evidence: supported. Targets: habitatmech:GOLD.53e4290463.

Retained anatomical or host-environment claims were rechecked against the predecessor primary evidence and current target. No new mechanism, characteristic taxon, prevalence, specimen identity or universal clade-level property is added. Source counts remain historical attestations.

## Findings

### F1: Source context is asserted as a broader habitat

major / resolved / confirmed; issue key: anterior-chamber-source-parent.

An anterior chamber of a crustacean hindgut is not a subtype of the whole hindgut. Exclude only the guarded immediate GOLD contribution habitatmech:GOLD.19840c718e in gold_parent_exclusions.tsv; preserve independent ontology parents and verbatim source provenance.

Disposition: The exact guarded GOLD context contribution is removed; independently supported ontology parents and original source fields remain.

### F2: Vertebrate embryonic term cannot subsume a crustacean compartment

major / resolved / confirmed; issue key: anterior-chamber-vertebrate-embryonic-parent.

Replace the unsupported GROUND_AS_PARENT decision with a verified regional-anatomy decision or explicit ITEM CONFIRM_UNGROUNDED. Do not restore eye chamber or substitute whole UBERON hindgut. Preserve minted identity, full path and node 7325.

Disposition: ITEM CONFIRM_UNGROUNDED removes the vertebrate embryonic target without restoring the eye homonym or substituting a whole-hindgut superclass.

### F3: Narrow predicate compares a different endpoint than the schema declares

major / resolved / confirmed; issue key: anterior-chamber-mapping-endpoint-contract.

Native execution retains the source minted ID but copies skos:narrowMatch into source-to-record attestation. The actual narrower comparison is to an ontology parent, not the retained record. Resolve shared schema/producer/consumer endpoints under #1398; a broad/narrow swap or an unsupported ontology merge is not a fix. No formal SKOS self-link prohibition or SSSOM/KGX conformance is claimed.

Disposition: This local witness no longer emits NARROW/skos:narrowMatch because the unsupported grounding was removed. The source mint remains the record and its mapping predicate is omitted. Shared issue #1398 remains open for other routes.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000510; Target term fields and typed relations, or primary abstract | supports | Inspected current authoritative term BTO:0000510 (hindgut), definition and obsolete flag False. Its scoped meaning is compared with the complete GOLD path in the scientific assessment. |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000510/graph; Target term fields and typed relations, or primary abstract | supports | Inspected typed outgoing edges: [{"label": "part of", "source": "http://purl.obolibrary.org/obo/BTO_0000510", "target": "http://purl.obolibrary.org/obo/BTO_0000545", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}]. Relation labels remain distinct; containment is not promoted to subclass. |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001766; Target term fields and typed relations, or primary abstract | supports | Inspected current authoritative term UBERON:0001766 (anterior chamber of eyeball), definition and obsolete flag False. Its scoped meaning is compared with the complete GOLD path in the scientific assessment. |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001046; Target term fields and typed relations, or primary abstract | supports | Inspected current authoritative term UBERON:0001046 (hindgut), definition and obsolete flag False. Its scoped meaning is compared with the complete GOLD path in the scientific assessment. |
| EX5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30564048%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Target term fields and typed relations, or primary abstract | supports | Primary abstract: ultrastructural comparison distinguishes anterior chamber and papillate region in Porcellio scaber hindgut. |
| EX6 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6288245/fullTextXML; Abstract and Introduction; inspected compartment description, not a complete full-text audit | supports | The inspected introduction describes an anterior chamber, papillate region and short rectum within the terrestrial-isopod hindgut. A regional component is distinct from the entire hindgut. |
| EX7 | https://www.ebi.ac.uk/ols4/api/search?q=anterior%20chamber%20hindgut&amp;ontology=envo,uberon,bto,foodon,aism&amp;rows=50; Target term fields and typed relations, or primary abstract | supports | Inspected bounded query response for a regional-anatomy candidate; no exhaustive ontology-absence conclusion is drawn. |
| EAFTER | data/habitats/host_associated/anterior_chamber.yaml; Entire current generated YAML | supports | Complete post-fix record re-read: {"curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM reassessment #1332: this source is the anterior chamber of a crustacean hindgut, not the eye chamber UBERON:0001766. BTO:0000510 explicitly denotes vertebrate embryonic hindgut and cannot subsume it. Bogataj et al. distinguish anterior chamber and papillate region in Porcellio scaber (PMID:30564048; DOI:10.3897/zookeys.801.22395). Retain the minted regional habitat UNGROUNDED because no fitting identity or strictly broader regional term was verified; whole UBERON:0001046 hindgut is not a compartment superclass. The independent GOLD whole-hindgut context parent is excluded under #1331. Preserve node 7325 and the full source path; no universal crustacean microbiome or sample identity is inferred. This supersedes the 2026-08-16 GROUND_AS_PARENT decision, retained in Git and append-only session history. (source concept habitatmech:GOLD.53e4290463)", "curator": "codex-gpt-5", "timestamp": "2026-10-15T00:00:00Z"}, {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.19840c718e for habitatmech:GOLD.53e4290463 (Host-associated &gt; Arthropoda: Crustaceans &gt; Digestive system &gt; Hindgut &gt; Anterior chamber). Scientific review #1331: a crustacean anterior hindgut chamber is a compartment, not a subtype of whole hindgut. Bogataj et al. distinguish this region from the papillate region in Porcellio scaber (PMID:30564048). Exclude only this exact GOLD contribution, preserving node 7325 and full source path. The independent vertebrate-embryonic BTO:0000510 decision is corrected under #1332; do not replace it with whole UBERON:0001046 or the eye-chamber homonym. https://pubmed.ncbi.nlm.nih.gov/30564048/", "curator": "codex-gpt-5", "timestamp": "2026-10-15T00:00:00Z"}], "grounding_status": "UNGROUNDED", "habitat_category": "HOST_ASSOCIATED", "identifier": "habitatmech:GOLD.53e4290463", "label": "Anterior chamber", "mapping_status": "REVIEWED", "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7325", "source_label": "Anterior chamber", "source_path": "Host-associated &gt; Arthropoda: Crustaceans &gt; Digestive system &gt; Hindgut &gt; Anterior chamber"}]} |
| EPREV | reviews/structured/20261015T041833Z-anterior_chamber-record/review.yaml; Complete immutable pre-fix scientific review | supports | Original scoped evidence and all normalized findings remain unchanged. |
| ETEST | tests/test_host_anatomy_review_repairs.py; Complete corpus counterfactual and repeated seeding test | supports | Test restores the old maintained semantics in memory and proves exactly twelve changed records, preserved identities and unrelated fields; it checks host fallback, source counts, valid parents and all fornix synonym scopes. |
| EI0 | curation/decisions.tsv; Exact identifier/source key habitatmech:GOLD.53e4290463; generated identifier habitatmech:GOLD.53e4290463 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |
| EI1 | curation/term_requests.tsv; Exact identifier/source key habitatmech:GOLD.53e4290463; generated identifier habitatmech:GOLD.53e4290463 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |
| EI2 | curation/gold_parent_exclusions.tsv; Exact identifier/source key habitatmech:GOLD.53e4290463; generated identifier habitatmech:GOLD.53e4290463 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |
| EI3 | curation/record_annotation_corrections.tsv; Exact identifier/source key habitatmech:GOLD.53e4290463; generated identifier habitatmech:GOLD.53e4290463 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |

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
review_id: 20261015T043316Z-anterior_chamber-remediation
kind: record
repository: CultureBotAI/HabitatMech
title: 'Remediation review: Anterior chamber (habitatmech:GOLD.53e4290463)'
started_at: '2026-10-15T04:31:09Z'
finished_at: '2026-10-15T04:33:16Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Continuing agent assessed complete records and primary evidence;
    this is not independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 3 predecessor finding(s) resolved; 0 remain open. The complete current record
  preserves its source identity and provenance. The corrected claims are supported
  within the documented source and evidence limits.
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
  - path: data/habitats/host_associated/anterior_chamber.yaml
    sha256: bf44a74ae4c2987b5baddcbea8f8433f97394a842268f3cb554b8376f1ed88ce
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
  - path: history/mappings/anterior_chamber/2026-10-15T042508Z-codex-gpt-5-ee6006.yaml
    sha256: 0f50b99196e965ca3670dc1d1c2ede3d217834edeaaea0dc7027db4ac04c1df0
    role: context
  - path: history/mappings/anterior_chamber/2026-10-15T042516Z-codex-gpt-5-aaba64.yaml
    sha256: dda27386f6698ef538b0557e63c226eca2e0a9dc9c6aa7660f14dbee7a091242
    role: context
  - path: reviews/structured/20261015T041833Z-anterior_chamber-record/review.yaml
    sha256: 0e8c88a5862ca378419c5db23170ca7691310d33ec14d825875c50ce6e6d500e
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
- target_id: habitatmech:GOLD.53e4290463
  path: data/habitats/host_associated/anterior_chamber.yaml
  label: Anterior chamber
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
  - habitatmech:GOLD.53e4290463
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
  - habitatmech:GOLD.53e4290463
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
  - habitatmech:GOLD.53e4290463
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
  - habitatmech:GOLD.53e4290463
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
  - habitatmech:GOLD.53e4290463
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
  - habitatmech:GOLD.53e4290463
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
  - habitatmech:GOLD.53e4290463
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
  - habitatmech:GOLD.53e4290463
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
  - habitatmech:GOLD.53e4290463
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
  - habitatmech:GOLD.53e4290463
  summary: 'Actual successful execution 2026-10-15T04:28:52Z through 2026-10-15T04:28:52Z. '
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
evidence:
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000510
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:04:35Z'
  support: supports
  summary: Inspected current authoritative term BTO:0000510 (hindgut), definition
    and obsolete flag False. Its scoped meaning is compared with the complete GOLD
    path in the scientific assessment.
  snapshot_sha256: 17f109dded1f0c3dae106e4b169fb9e575cd8d3bbd6c15f52e658d980e8589eb
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000510/graph
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:05:24Z'
  support: supports
  summary: 'Inspected typed outgoing edges: [{"label": "part of", "source": "http://purl.obolibrary.org/obo/BTO_0000510",
    "target": "http://purl.obolibrary.org/obo/BTO_0000545", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}].
    Relation labels remain distinct; containment is not promoted to subclass.'
  snapshot_sha256: ea81937a38b2b4e938043dd86a48507c7b9d5adcc2258f29e1a4859b5c5f9c4a
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001766
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:04:39Z'
  support: supports
  summary: Inspected current authoritative term UBERON:0001766 (anterior chamber of
    eyeball), definition and obsolete flag False. Its scoped meaning is compared with
    the complete GOLD path in the scientific assessment.
  snapshot_sha256: ff67bb5ae85df7fc909bfd976e80a8b36a13976b161228a219151f60f2dc945c
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001046
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:05:17Z'
  support: supports
  summary: Inspected current authoritative term UBERON:0001046 (hindgut), definition
    and obsolete flag False. Its scoped meaning is compared with the complete GOLD
    path in the scientific assessment.
  snapshot_sha256: f65ee5feea5c3a4fcfb07e6bc51713bd73c261363eaf039b32068d5a620d6fd9
- evidence_id: EX5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:30564048%20AND%20SRC:MED&format=json&resultType=core
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:05:28Z'
  support: supports
  summary: 'Primary abstract: ultrastructural comparison distinguishes anterior chamber
    and papillate region in Porcellio scaber hindgut.'
  snapshot_sha256: e29c925244701a30f231547df084cbf45c391c4ba47ca7eb3b24a3d557b65bf0
- evidence_id: EX6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6288245/fullTextXML
  locator: Abstract and Introduction; inspected compartment description, not a complete
    full-text audit
  accessed_at: '2026-10-15T04:05:30Z'
  support: supports
  summary: The inspected introduction describes an anterior chamber, papillate region
    and short rectum within the terrestrial-isopod hindgut. A regional component is
    distinct from the entire hindgut.
  snapshot_sha256: c0f2bc772d0b6ab69df573301e12cfc972d4de0309e026e64df8e514dccdc5f3
- evidence_id: EX7
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/search?q=anterior%20chamber%20hindgut&ontology=envo,uberon,bto,foodon,aism&rows=50
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:10:00Z'
  support: supports
  summary: Inspected bounded query response for a regional-anatomy candidate; no exhaustive
    ontology-absence conclusion is drawn.
  snapshot_sha256: bfeab5c36001e34f7cd9a93811dea58afaf3656e43ecfee6f8c7684e854c3873
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/anterior_chamber.yaml
  locator: Entire current generated YAML
  accessed_at: '2026-10-15T04:33:16Z'
  support: supports
  summary: 'Complete post-fix record re-read: {"curation_history": [{"action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED.",
    "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action":
    "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits
    this concept. ITEM reassessment #1332: this source is the anterior chamber of
    a crustacean hindgut, not the eye chamber UBERON:0001766. BTO:0000510 explicitly
    denotes vertebrate embryonic hindgut and cannot subsume it. Bogataj et al. distinguish
    anterior chamber and papillate region in Porcellio scaber (PMID:30564048; DOI:10.3897/zookeys.801.22395).
    Retain the minted regional habitat UNGROUNDED because no fitting identity or strictly
    broader regional term was verified; whole UBERON:0001046 hindgut is not a compartment
    superclass. The independent GOLD whole-hindgut context parent is excluded under
    #1331. Preserve node 7325 and the full source path; no universal crustacean microbiome
    or sample identity is inferred. This supersedes the 2026-08-16 GROUND_AS_PARENT
    decision, retained in Git and append-only session history. (source concept habitatmech:GOLD.53e4290463)",
    "curator": "codex-gpt-5", "timestamp": "2026-10-15T00:00:00Z"}, {"action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.19840c718e
    for habitatmech:GOLD.53e4290463 (Host-associated > Arthropoda: Crustaceans > Digestive
    system > Hindgut > Anterior chamber). Scientific review #1331: a crustacean anterior
    hindgut chamber is a compartment, not a subtype of whole hindgut. Bogataj et al.
    distinguish this region from the papillate region in Porcellio scaber (PMID:30564048).
    Exclude only this exact GOLD contribution, preserving node 7325 and full source
    path. The independent vertebrate-embryonic BTO:0000510 decision is corrected under
    #1332; do not replace it with whole UBERON:0001046 or the eye-chamber homonym.
    https://pubmed.ncbi.nlm.nih.gov/30564048/", "curator": "codex-gpt-5", "timestamp":
    "2026-10-15T00:00:00Z"}], "grounding_status": "UNGROUNDED", "habitat_category":
    "HOST_ASSOCIATED", "identifier": "habitatmech:GOLD.53e4290463", "label": "Anterior
    chamber", "mapping_status": "REVIEWED", "source_attestations": [{"source": "GOLD",
    "source_id": "gold.ecosystem:7325", "source_label": "Anterior chamber", "source_path":
    "Host-associated > Arthropoda: Crustaceans > Digestive system > Hindgut > Anterior
    chamber"}]}'
  snapshot_sha256: bf44a74ae4c2987b5baddcbea8f8433f97394a842268f3cb554b8376f1ed88ce
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T041833Z-anterior_chamber-record/review.yaml
  locator: Complete immutable pre-fix scientific review
  accessed_at: '2026-10-15T04:33:16Z'
  support: supports
  summary: Original scoped evidence and all normalized findings remain unchanged.
  snapshot_sha256: 0e8c88a5862ca378419c5db23170ca7691310d33ec14d825875c50ce6e6d500e
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_host_anatomy_review_repairs.py
  locator: Complete corpus counterfactual and repeated seeding test
  accessed_at: '2026-10-15T04:33:16Z'
  support: supports
  summary: Test restores the old maintained semantics in memory and proves exactly
    twelve changed records, preserved identities and unrelated fields; it checks host
    fallback, source counts, valid parents and all fornix synonym scopes.
  snapshot_sha256: 5c0a954d3373998c98dd57d219db062b9a2ad22a8cfea00ca399d91b0648f7d3
- evidence_id: EI0
  kind: record_content
  reference: curation/decisions.tsv
  locator: Exact identifier/source key habitatmech:GOLD.53e4290463; generated identifier
    habitatmech:GOLD.53e4290463
  accessed_at: '2026-10-15T04:33:16Z'
  support: supports
  summary: Maintained rows inspected and rechecked against the generated delta and
    predecessor. No raw inventories or generator implementation were edited.
  snapshot_sha256: 3f18e736384e6eece8e9c3c7e371714b8b3cef474de661e0e717705ee1341db7
- evidence_id: EI1
  kind: record_content
  reference: curation/term_requests.tsv
  locator: Exact identifier/source key habitatmech:GOLD.53e4290463; generated identifier
    habitatmech:GOLD.53e4290463
  accessed_at: '2026-10-15T04:33:16Z'
  support: supports
  summary: Maintained rows inspected and rechecked against the generated delta and
    predecessor. No raw inventories or generator implementation were edited.
  snapshot_sha256: 2144d43ab4e106ff820da87c348f673d16cb8ea30d5a565f12e156af598f85ad
- evidence_id: EI2
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact identifier/source key habitatmech:GOLD.53e4290463; generated identifier
    habitatmech:GOLD.53e4290463
  accessed_at: '2026-10-15T04:33:16Z'
  support: supports
  summary: Maintained rows inspected and rechecked against the generated delta and
    predecessor. No raw inventories or generator implementation were edited.
  snapshot_sha256: 761c1c1c60358c6c24e4d797637a12bdde6f8541e568914b404bffd1e0dd57ec
- evidence_id: EI3
  kind: record_content
  reference: curation/record_annotation_corrections.tsv
  locator: Exact identifier/source key habitatmech:GOLD.53e4290463; generated identifier
    habitatmech:GOLD.53e4290463
  accessed_at: '2026-10-15T04:33:16Z'
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
    and unrelated corpus records are preserved. The chamber remains a real regional
    habitat with no verified suitable grounding; its generated history reflects the
    new decision, while the old decision is preserved in the predecessor/Git and the
    append-only curation session.
  target_ids:
  - habitatmech:GOLD.53e4290463
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
  - habitatmech:GOLD.53e4290463
  evidence_ids:
  - EAFTER
  - EPREV
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
findings:
- finding_id: F1
  issue_key: anterior-chamber-source-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is asserted as a broader habitat
  description: An anterior chamber of a crustacean hindgut is not a subtype of the
    whole hindgut. Exclude only the guarded immediate GOLD contribution habitatmech:GOLD.19840c718e
    in gold_parent_exclusions.tsv; preserve independent ontology parents and verbatim
    source provenance.
  target_ids:
  - habitatmech:GOLD.53e4290463
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
  - EX4
  - EX5
  - EX6
  - EX7
  rule_id: docs/CURATION.md; SourceAttestation contract; native record-review checklist
  native_severity: major
  normalization_reason: Material semantic error; schema validity does not establish
    this claim.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated habitat files are read-only
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1331
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T041833Z-anterior_chamber-record
    finding_id: F1
  disposition_reason: The exact guarded GOLD context contribution is removed; independently
    supported ontology parents and original source fields remain.
- finding_id: F2
  issue_key: anterior-chamber-vertebrate-embryonic-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Vertebrate embryonic term cannot subsume a crustacean compartment
  description: Replace the unsupported GROUND_AS_PARENT decision with a verified regional-anatomy
    decision or explicit ITEM CONFIRM_UNGROUNDED. Do not restore eye chamber or substitute
    whole UBERON hindgut. Preserve minted identity, full path and node 7325.
  target_ids:
  - habitatmech:GOLD.53e4290463
  field_paths:
  - parent_habitats
  - grounding_status
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
  - EX4
  - EX5
  - EX6
  - EX7
  rule_id: docs/CURATION.md; SourceAttestation contract; native record-review checklist
  native_severity: major
  normalization_reason: Material semantic error; schema validity does not establish
    this claim.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; generated habitat files are read-only
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1332
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T041833Z-anterior_chamber-record
    finding_id: F2
  disposition_reason: ITEM CONFIRM_UNGROUNDED removes the vertebrate embryonic target
    without restoring the eye homonym or substituting a whole-hindgut superclass.
- finding_id: F3
  issue_key: anterior-chamber-mapping-endpoint-contract
  category: representation
  severity: major
  status: resolved
  certainty: confirmed
  title: Narrow predicate compares a different endpoint than the schema declares
  description: 'Native execution retains the source minted ID but copies skos:narrowMatch
    into source-to-record attestation. The actual narrower comparison is to an ontology
    parent, not the retained record. Resolve shared schema/producer/consumer endpoints
    under #1398; a broad/narrow swap or an unsupported ontology merge is not a fix.
    No formal SKOS self-link prohibition or SSSOM/KGX conformance is claimed.'
  target_ids:
  - habitatmech:GOLD.53e4290463
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
  - EX4
  - EX5
  - EX6
  - EX7
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
    review_id: 20261015T041833Z-anterior_chamber-record
    finding_id: F3
  disposition_reason: 'This local witness no longer emits NARROW/skos:narrowMatch
    because the unsupported grounding was removed. The source mint remains the record
    and its mapping predicate is omitted. Shared issue #1398 remains open for other
    routes.'
actions: []
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
  review_id: 20261015T041833Z-anterior_chamber-record
  relationship: Exact pre-fix predecessor; all finding identities retained.
tags:
- individual-scientific-review
- remediation
- host-associated
```
