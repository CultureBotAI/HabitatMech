# Remediation review: amphibian-associated environment (habitatmech:GOLD.0cd585a031)

- Review: 20261015T043308Z-amphibia-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T04:30:17Z
- Finished UTC: 2026-10-15T04:33:08Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

1 predecessor finding(s) resolved; 0 remain open. The complete current record preserves its source identity and provenance. The corrected claims are supported within the documented source and evidence limits.

## Scope And Provenance

Full current record re-read with scoped remediation of the exact predecessor findings.

Selection: One exact record from the twelve-record authorized PR repair cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 2f52e94e2929ea1aa85ecf61f43d48afa1edb035.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.0cd585a031 | data/habitats/host_associated/amphibia.yaml | generated | amphibian-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate-strict data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml | passed | True | habitatmech:GOLD.0cd585a031 | Actual successful execution 2026-10-15T04:26:07Z through 2026-10-15T04:26:19Z. uv run python scripts/validate_strict.py data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml<br>Validating 12 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      12<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.0cd585a031 | Actual successful execution 2026-10-15T04:26:19Z through 2026-10-15T04:26:35Z. No issues found<br>744 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.0cd585a031 | Actual successful execution 2026-10-15T04:26:35Z through 2026-10-15T04:26:36Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.0cd585a031 | Actual successful execution 2026-10-15T04:26:36Z through 2026-10-15T04:27:01Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.0cd585a031 | Actual successful execution 2026-10-15T04:27:01Z through 2026-10-15T04:27:12Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.0cd585a031 | Actual successful execution 2026-10-15T04:27:12Z through 2026-10-15T04:27:41Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.0cd585a031 | Actual successful execution 2026-10-15T04:27:41Z through 2026-10-15T04:28:43Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_host_anatomy_review_repairs.py | passed | True | habitatmech:GOLD.0cd585a031 | Actual successful execution 2026-10-15T04:28:43Z through 2026-10-15T04:28:52Z. .                                                                        [100%]<br>1 passed in 7.53s |
| git diff --check ea0bf6a2629ffcd2ed086310a5eee162d4f11cae | passed | True | habitatmech:GOLD.0cd585a031 | Actual successful execution 2026-10-15T04:28:52Z through 2026-10-15T04:28:52Z.  |

## Scientific And Domain Assessments

### Scoped corrections and retained scientific identity

consistency: supported. Targets: habitatmech:GOLD.0cd585a031.

Generated record and maintained owners agree. Exactly the expected field-level changes are present; valid ontology identity/genus, source path/node/count semantics and unrelated corpus records are preserved. The previous generated history is retained; any new exclusion/correction events are appended.

### Primary-source scope and optional fields

evidence: supported. Targets: habitatmech:GOLD.0cd585a031.

Retained anatomical or host-environment claims were rechecked against the predecessor primary evidence and current target. No new mechanism, characteristic taxon, prevalence, specimen identity or universal clade-level property is added. Source counts remain historical attestations.

## Findings

### F1: Host taxon is an exact habitat synonym

major / resolved / confirmed; issue key: amphibia-host-name-exact-synonym.

Remove only the authored host-clade exact alias in term_requests.tsv. Keep the definition, genus, xref and source label. The existing matching organism xref suppresses automatic old-label fallback; verify that behavior instead of adding an unnecessary exclusion.

Disposition: Only the authored host-taxon alias is removed; the existing matching taxon xref suppresses fallback. Definition, genus, source labels/counts and original DEFINED event remain unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002; Target term fields and typed relations, or primary abstract | supports | Inspected current authoritative term ENVO:01001002 (animal-associated environment), definition and obsolete flag False. Its scoped meaning is compared with the complete GOLD path in the scientific assessment. |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph; Target term fields and typed relations, or primary abstract | supports | Inspected typed outgoing edges: [{"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}, {"label": "part of", "source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}]. Relation labels remain distinct; containment is not promoted to subclass. |
| EX3 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=6340,8292; Top-level Taxon 8292 Amphibia class and 6340 Annelida phylum; lineages | supports | NCBI confirms taxid8292 Amphibia, rank class, and taxid6340 Annelida, rank phylum. These are organism taxa, not environmental classes. |
| EX4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:19322245%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Target term fields and typed relations, or primary abstract | supports | Primary abstract: a frog-skin bacterial intervention supports a specific amphibian-associated microbial environment, not a universal clade-level microbiome. |
| EAFTER | data/habitats/host_associated/amphibia.yaml; Entire current generated YAML | supports | Complete post-fix record re-read: {"curation_history": [{"action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. NCBITaxon:8292 'Amphibia' kept as an xref. Host-taxon reversal (#114): this was NOT_APPLICABLE on the reasoning that 'a host taxon is not a habitat'. That reasoning is wrong, and the corpus already contradicted it \u2014 the same kind of concept was treated as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep their own identity and a term request for an &lt;X&gt;-associated environment. Host-associated &gt; Porifera was NOT_APPLICABLE while its own child Porifera &gt; Sponge was a term request.An organism acting as a host IS a habitat: it is where the microbe lives, and ENVO models exactly this at plant-associated, animal-associated and fungi-associated environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.0cd585a031)", "curator": "claude-opus-5", "timestamp": "2026-08-16T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "DEFINED", "changes": "Defined as 'amphibian-associated environment' under ENVO:01001002 'animal-associated environment'. Definition drafted from the record's deep-research report under research/habitats/ and read against it; the report's proposed wording, genus and near-miss table are the evidence.", "curator": "claude-opus-5", "timestamp": "2026-08-17T00:00:00Z"}], "definition": "An animal-associated environment which is determined by an amphibian.", "definition_source": "HabitatMech", "grounding_status": "UNGROUNDED", "habitat_category": "HOST_ASSOCIATED", "identifier": "habitatmech:GOLD.0cd585a031", "label": "amphibian-associated environment", "mapping_status": "REVIEWED", "parent_habitats": ["ENVO:01001000", "ENVO:01001002"], "source_attestations": [{"assertion_count": 41, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3372", "source_label": "Amphibia", "source_path": "Host-associated &gt; Amphibia"}], "xrefs": ["NCBITaxon:8292"]} |
| EPREV | reviews/structured/20261015T041828Z-amphibia-record/review.yaml; Complete immutable pre-fix scientific review | supports | Original scoped evidence and all normalized findings remain unchanged. |
| ETEST | tests/test_host_anatomy_review_repairs.py; Complete corpus counterfactual and repeated seeding test | supports | Test restores the old maintained semantics in memory and proves exactly twelve changed records, preserved identities and unrelated fields; it checks host fallback, source counts, valid parents and all fornix synonym scopes. |
| EI0 | curation/decisions.tsv; Exact identifier/source key habitatmech:GOLD.0cd585a031; generated identifier habitatmech:GOLD.0cd585a031 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |
| EI1 | curation/term_requests.tsv; Exact identifier/source key habitatmech:GOLD.0cd585a031; generated identifier habitatmech:GOLD.0cd585a031 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |
| EI2 | curation/gold_parent_exclusions.tsv; Exact identifier/source key habitatmech:GOLD.0cd585a031; generated identifier habitatmech:GOLD.0cd585a031 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |
| EI3 | curation/record_annotation_corrections.tsv; Exact identifier/source key habitatmech:GOLD.0cd585a031; generated identifier habitatmech:GOLD.0cd585a031 | supports | Maintained rows inspected and rechecked against the generated delta and predecessor. No raw inventories or generator implementation were edited. |

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
review_id: 20261015T043308Z-amphibia-remediation
kind: record
repository: CultureBotAI/HabitatMech
title: 'Remediation review: amphibian-associated environment (habitatmech:GOLD.0cd585a031)'
started_at: '2026-10-15T04:30:17Z'
finished_at: '2026-10-15T04:33:08Z'
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
summary: 1 predecessor finding(s) resolved; 0 remain open. The complete current record
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
  - path: data/habitats/host_associated/amphibia.yaml
    sha256: 720ed0986037a6963fe034d53668fbeeb5e3766a9e52a8894539630722203d4b
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
  - path: history/mappings/amphibia/2026-10-15T042512Z-codex-gpt-5-b95e4a.yaml
    sha256: 114be8d90608119ad41277221fd8435becb9f1c94313fd0780c3f97bbf4d2220
    role: context
  - path: reviews/structured/20261015T041828Z-amphibia-record/review.yaml
    sha256: a6fa6ac590b3de3dd91ad24f1973ea081ab2b08b6eaa03c1f5798386e2c4c70c
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
- target_id: habitatmech:GOLD.0cd585a031
  path: data/habitats/host_associated/amphibia.yaml
  label: amphibian-associated environment
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
  - habitatmech:GOLD.0cd585a031
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
  - habitatmech:GOLD.0cd585a031
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
  - habitatmech:GOLD.0cd585a031
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
  - habitatmech:GOLD.0cd585a031
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
  - habitatmech:GOLD.0cd585a031
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
  - habitatmech:GOLD.0cd585a031
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
  - habitatmech:GOLD.0cd585a031
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
  - habitatmech:GOLD.0cd585a031
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
  - habitatmech:GOLD.0cd585a031
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
  - habitatmech:GOLD.0cd585a031
  summary: 'Actual successful execution 2026-10-15T04:28:52Z through 2026-10-15T04:28:52Z. '
  scope_note: Strict validation covers twelve repaired records; other commands have
    their recorded full-corpus or focused-test scope.
evidence:
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:04:37Z'
  support: supports
  summary: Inspected current authoritative term ENVO:01001002 (animal-associated environment),
    definition and obsolete flag False. Its scoped meaning is compared with the complete
    GOLD path in the scientific assessment.
  snapshot_sha256: c3c90d5e91cc85727658222c907f7747f34861ad80bf1ceac5ce209f7e170907
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:05:25Z'
  support: supports
  summary: 'Inspected typed outgoing edges: [{"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"},
    {"label": "part of", "source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}].
    Relation labels remain distinct; containment is not promoted to subclass.'
  snapshot_sha256: 882375d994d0dea7166097328c56e0e22362848e68aba0125d1b128a24ebf1b0
- evidence_id: EX3
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=6340,8292
  locator: Top-level Taxon 8292 Amphibia class and 6340 Annelida phylum; lineages
  accessed_at: '2026-10-15T04:04:42Z'
  support: supports
  summary: NCBI confirms taxid8292 Amphibia, rank class, and taxid6340 Annelida, rank
    phylum. These are organism taxa, not environmental classes.
  snapshot_sha256: 8f136820809391753f284fb21c1cb03bc2b51d6203187baecc868c611398ccdd
- evidence_id: EX4
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:19322245%20AND%20SRC:MED&format=json&resultType=core
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:05:25Z'
  support: supports
  summary: 'Primary abstract: a frog-skin bacterial intervention supports a specific
    amphibian-associated microbial environment, not a universal clade-level microbiome.'
  snapshot_sha256: b1d7595a9be1363703a1a492b4a3998731e0f9c1b090f5c5135e2aa6b3400157
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/amphibia.yaml
  locator: Entire current generated YAML
  accessed_at: '2026-10-15T04:33:08Z'
  support: supports
  summary: 'Complete post-fix record re-read: {"curation_history": [{"action": "CONFIRM_UNGROUNDED",
    "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. NCBITaxon:8292
    ''Amphibia'' kept as an xref. Host-taxon reversal (#114): this was NOT_APPLICABLE
    on the reasoning that ''a host taxon is not a habitat''. That reasoning is wrong,
    and the corpus already contradicted it \u2014 the same kind of concept was treated
    as a habitat for Sponge, Nematoda, Reptilia, Mammals, Birds and Fish, which keep
    their own identity and a term request for an <X>-associated environment. Host-associated
    > Porifera was NOT_APPLICABLE while its own child Porifera > Sponge was a term
    request.An organism acting as a host IS a habitat: it is where the microbe lives,
    and ENVO models exactly this at plant-associated, animal-associated and fungi-associated
    environment. What is not a habitat is the TAXON TERM \u2014 a phylum is a class
    of organisms, not a place \u2014 so the taxon stays an xref (#99) and the concept
    keeps its own identity as a term-request candidate. NOT_APPLICABLE said the concept
    is not a habitat, which is a stronger and false claim. (source concept habitatmech:GOLD.0cd585a031)",
    "curator": "claude-opus-5", "timestamp": "2026-08-16T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED.",
    "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action":
    "DEFINED", "changes": "Defined as ''amphibian-associated environment'' under ENVO:01001002
    ''animal-associated environment''. Definition drafted from the record''s deep-research
    report under research/habitats/ and read against it; the report''s proposed wording,
    genus and near-miss table are the evidence.", "curator": "claude-opus-5", "timestamp":
    "2026-08-17T00:00:00Z"}], "definition": "An animal-associated environment which
    is determined by an amphibian.", "definition_source": "HabitatMech", "grounding_status":
    "UNGROUNDED", "habitat_category": "HOST_ASSOCIATED", "identifier": "habitatmech:GOLD.0cd585a031",
    "label": "amphibian-associated environment", "mapping_status": "REVIEWED", "parent_habitats":
    ["ENVO:01001000", "ENVO:01001002"], "source_attestations": [{"assertion_count":
    41, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this
    path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD",
    "source_id": "gold.ecosystem:3372", "source_label": "Amphibia", "source_path":
    "Host-associated > Amphibia"}], "xrefs": ["NCBITaxon:8292"]}'
  snapshot_sha256: 720ed0986037a6963fe034d53668fbeeb5e3766a9e52a8894539630722203d4b
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T041828Z-amphibia-record/review.yaml
  locator: Complete immutable pre-fix scientific review
  accessed_at: '2026-10-15T04:33:08Z'
  support: supports
  summary: Original scoped evidence and all normalized findings remain unchanged.
  snapshot_sha256: a6fa6ac590b3de3dd91ad24f1973ea081ab2b08b6eaa03c1f5798386e2c4c70c
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_host_anatomy_review_repairs.py
  locator: Complete corpus counterfactual and repeated seeding test
  accessed_at: '2026-10-15T04:33:08Z'
  support: supports
  summary: Test restores the old maintained semantics in memory and proves exactly
    twelve changed records, preserved identities and unrelated fields; it checks host
    fallback, source counts, valid parents and all fornix synonym scopes.
  snapshot_sha256: 5c0a954d3373998c98dd57d219db062b9a2ad22a8cfea00ca399d91b0648f7d3
- evidence_id: EI0
  kind: record_content
  reference: curation/decisions.tsv
  locator: Exact identifier/source key habitatmech:GOLD.0cd585a031; generated identifier
    habitatmech:GOLD.0cd585a031
  accessed_at: '2026-10-15T04:33:08Z'
  support: supports
  summary: Maintained rows inspected and rechecked against the generated delta and
    predecessor. No raw inventories or generator implementation were edited.
  snapshot_sha256: 3f18e736384e6eece8e9c3c7e371714b8b3cef474de661e0e717705ee1341db7
- evidence_id: EI1
  kind: record_content
  reference: curation/term_requests.tsv
  locator: Exact identifier/source key habitatmech:GOLD.0cd585a031; generated identifier
    habitatmech:GOLD.0cd585a031
  accessed_at: '2026-10-15T04:33:08Z'
  support: supports
  summary: Maintained rows inspected and rechecked against the generated delta and
    predecessor. No raw inventories or generator implementation were edited.
  snapshot_sha256: 2144d43ab4e106ff820da87c348f673d16cb8ea30d5a565f12e156af598f85ad
- evidence_id: EI2
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact identifier/source key habitatmech:GOLD.0cd585a031; generated identifier
    habitatmech:GOLD.0cd585a031
  accessed_at: '2026-10-15T04:33:08Z'
  support: supports
  summary: Maintained rows inspected and rechecked against the generated delta and
    predecessor. No raw inventories or generator implementation were edited.
  snapshot_sha256: 761c1c1c60358c6c24e4d797637a12bdde6f8541e568914b404bffd1e0dd57ec
- evidence_id: EI3
  kind: record_content
  reference: curation/record_annotation_corrections.tsv
  locator: Exact identifier/source key habitatmech:GOLD.0cd585a031; generated identifier
    habitatmech:GOLD.0cd585a031
  accessed_at: '2026-10-15T04:33:08Z'
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
  - habitatmech:GOLD.0cd585a031
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
  - habitatmech:GOLD.0cd585a031
  evidence_ids:
  - EAFTER
  - EPREV
  - EX1
  - EX2
  - EX3
  - EX4
findings:
- finding_id: F1
  issue_key: amphibia-host-name-exact-synonym
  category: nomenclature
  severity: major
  status: resolved
  certainty: confirmed
  title: Host taxon is an exact habitat synonym
  description: Remove only the authored host-clade exact alias in term_requests.tsv.
    Keep the definition, genus, xref and source label. The existing matching organism
    xref suppresses automatic old-label fallback; verify that behavior instead of
    adding an unnecessary exclusion.
  target_ids:
  - habitatmech:GOLD.0cd585a031
  field_paths:
  - synonyms
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
  rule_id: docs/CURATION.md; SourceAttestation contract; native record-review checklist
  native_severity: major
  normalization_reason: Material semantic error; schema validity does not establish
    this claim.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; generated habitat files are read-only
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2157
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T041828Z-amphibia-record
    finding_id: F1
  disposition_reason: Only the authored host-taxon alias is removed; the existing
    matching taxon xref suppresses fallback. Definition, genus, source labels/counts
    and original DEFINED event remain unchanged.
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
  review_id: 20261015T041828Z-amphibia-record
  relationship: Exact pre-fix predecessor; all finding identities retained.
tags:
- individual-scientific-review
- remediation
- host-associated
```
