# Publication follow-up: Anterior chamber (habitatmech:GOLD.53e4290463)

- Review: 20261015T050816Z-anterior_chamber-publication
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T05:07:55Z
- Finished UTC: 2026-10-15T05:08:16Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All three scientific predecessor findings remain resolved after a citation-format-only correction. Complete current record re-read confirms unchanged identity, source scope, ungrounded disposition and absent unsupported parents. Issue #2159 changes the verified paper identifier to its equivalent PubMed URL; it does not alter scientific evidence or certify shared export modeling.

## Scope And Provenance

Full current anterior-chamber record re-read after the maintained decision-note publication citation was reformatted.

Selection: One exact record from the twelve-record authorized PR repair cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 9000e3916da0f27a48a2a2f4ec9460bab67f7850.
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
| .venv/bin/python -m pytest -q tests/test_decisions.py tests/test_host_anatomy_review_repairs.py | passed | True | habitatmech:GOLD.53e4290463 | Actual execution 2026-10-15T05:01:01Z through 2026-10-15T05:05:46Z. .......................................................................  [100%]<br>71 passed in 283.52s (0:04:43) |
| .venv/bin/python -m pytest -q tests/test_decisions.py::test_curation_notes_do_not_cite_evidence_that_does_not_exist | passed | True | habitatmech:GOLD.53e4290463 | Actual execution 2026-10-15T05:06:18Z through 2026-10-15T05:06:25Z. .                                                                        [100%]<br>1 passed in 4.70s |
| just validate-strict data/habitats/host_associated/anterior_chamber.yaml | passed | True | habitatmech:GOLD.53e4290463 | Actual execution 2026-10-15T05:06:17Z through 2026-10-15T05:06:28Z. uv run python scripts/validate_strict.py data/habitats/host_associated/anterior_chamber.yaml<br>Validating 1 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.53e4290463 | Actual execution 2026-10-15T05:06:28Z through 2026-10-15T05:06:48Z. No issues found<br>746 history record(s) valid against src/habitatmech/schema/history.yaml |
| just verify-corpus | passed | True | habitatmech:GOLD.53e4290463 | Actual execution 2026-10-15T05:06:48Z through 2026-10-15T05:07:24Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just text-map-inputs --output build/review-ce-map/citation-final-inputs.jsonl | passed | True | habitatmech:GOLD.53e4290463 | Actual execution 2026-10-15T05:07:24Z through 2026-10-15T05:07:38Z. {"adapter_version": "habitatmech-semantic-v1", "jsonl_sha256": "49b0762b6a0e67362795e8881c2dc95174fa39b07431311de0025351c5c7b76d", "mode": "export", "output": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/build/review-ce-map/citation-final-inputs.jsonl", "records": 3208, "scope": "full"}<br> uv run python scripts/text_map_inputs.py "$@" |
| cmp build/review-ce-map/current-inputs.jsonl build/review-ce-map/citation-final-inputs.jsonl | passed | True | habitatmech:GOLD.53e4290463 | Actual execution 2026-10-15T05:07:38Z through 2026-10-15T05:07:38Z.  |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python scripts/embedding_pipeline.py check --output data/text_map --input build/review-ce-map/citation-final-inputs.jsonl --cache build/review-ce-map/download/build/text-map/vectors.sqlite | passed | True | habitatmech:GOLD.53e4290463 | Actual execution 2026-10-15T05:07:38Z through 2026-10-15T05:07:42Z. {<br>  "coverage": {<br>    "displayed": 3208,<br>    "eligible": 3208,<br>    "maximum": 50000,<br>    "omitted": 0,<br>    "selection": "bottom-k-sha256(seed,identifier)",<br>    "total": 3208<br>  },<br>  "encoder": {<br>    "dimension": 1024,<br>    "dtype": "float32-le",<br>    "format_version": 1,<br>    "inference_device": "cpu",<br>    "library_versions": {<br>      "numpy": "2.3.5",<br>      "sentence-transformers": "6.0.0",<br>      "tokenizers": "0.23.2",<br>      "torch": "2.14.0",<br>      "transformers": "5.17.0"<br>    },<br>    "max_seq_length": 512,<br>    "model": "BAAI/bge-large-en-v1.5",<br>    "normalized": true,<br>    "pooling": "sentence-transformers-model",<br>    "query_instruction": null,<br>    "revision": "d4aa6901d3a41ba39fb536a557fa166f842b0e09",<br>    "truncation": "tail",<br>    "weight_dtype": "torch.float32"<br>  },<br>  "encoder_profile_sha256": "15d9788b0f2912b22721f35398583eddad76f135f66de223319930f9d6013c6f",<br>  "files": {<br>    "index.html": "5a7ab0318561613ed86a6ab638ab26eb9e4be7718bf4ce3ad3c30e0de07e1b83",<br>    "points.json": "d73b5d66586b74c5b3d45768de788cc6705f42fcd8b7a50e688b376a8d9853ac"<br>  },<br>  "format_version": 1,<br>  "generated_at_utc": "2026-10-15T04:29:21.998399+00:00",<br>  "inputs": {<br>    "adapter_version": "habitatmech-semantic-v1",<br>    "categories": {<br>      "AIR": 7,<br>      "AQUATIC": 468,<br>      "CLINICAL": 4,<br>      "ENGINEERED": 488,<br>      "FOOD": 59,<br>      "HOST_ASSOCIATED": 1650,<br>      "OTHER": 179,<br>      "TERRESTRIAL": 353<br>    },<br>    "corpus_sha256": "5dc497c389e4216e2759ed6fb693f16fe0623367d992ec6c4d37491ae2f940b6",<br>    "count": 3208,<br>    "input_sha256": "49b0762b6a0e67362795e8881c2dc95174fa39b07431311de0025351c5c7b76d",<br>    "records_sha256": "22c06c18716b8124525ea28ef57267a9afda735a4ef152b83227e7a94b61d86a"<br>  },<br>  "projection": {<br>    "FP_ratio": 2.0,<br>    "MN_ratio": 0.5,<br>    "apply_pca": true,<br>    "dimensions": 2,<br>    "distance": "euclidean",<br>    "effective_pairs": {<br>      "further": 30,<br>      "mid_near": 8,<br>      "neighbors": 15<br>    },<br>    "implementation": "pacmap.PaCMAP",<br>    "initialization": "pca",<br>    "iterations": [<br>      100,<br>      100,<br>      250<br>    ],<br>    "knn_backend": "faiss",<br>    "learning_rate": 1.0,<br>    "library_versions": {<br>      "faiss-cpu": "1.15.0",<br>      "numba": "0.63.1",<br>      "numpy": "2.3.5",<br>      "pacmap": "0.9.1",<br>      "scikit-learn": "1.8.0"<br>    },<br>    "method": "pacmap",<br>    "neighbors": 15,<br>    "requested_neighbors": 15,<br>    "seed": 42<br>  },<br>  "representation": "semantic-text",<br>  "source_vectors": {<br>    "dtype": "float32-le",<br>    "order": "points.json",<br>    "sha256": "59153ecd462faeb1865f8da19b6d5d305809f89e93e667d7647ebcdf9085751a",<br>    "shape": [<br>      3208,<br>      1024<br>    ],<br>    "storage": "local-profile-bound-cache"<br>  }<br>} |

## Scientific And Domain Assessments

### Scoped corrections and retained scientific identity

consistency: supported. Targets: habitatmech:GOLD.53e4290463.

Generated record and maintained owners agree. Exactly the expected field-level changes are present; valid ontology identity/genus, source path/node/count semantics and unrelated corpus records are preserved. The chamber remains a real regional habitat with no verified suitable grounding; its generated history reflects the new decision, while the old decision is preserved in the predecessor/Git and the append-only curation session.

### Primary-source scope and optional fields

evidence: supported. Targets: habitatmech:GOLD.53e4290463.

Retained anatomical or host-environment claims were rechecked against the predecessor primary evidence and current target. No new mechanism, characteristic taxon, prevalence, specimen identity or universal clade-level property is added. Source counts remain historical attestations.

### Publication citation format

provenance: supported. Targets: habitatmech:GOLD.53e4290463.

The same inspected paper and DOI are retained. Exact structured record comparison differs only in the citation spelling and adjacent delimiter; full semantic input bytes remain identical.

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
| EAFTER | data/habitats/host_associated/anterior_chamber.yaml; Entire current generated YAML | supports | Complete record re-read: {"curation_history": [{"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM reassessment #1332: this source is the anterior chamber of a crustacean hindgut, not the eye chamber UBERON:0001766. BTO:0000510 explicitly denotes vertebrate embryonic hindgut and cannot subsume it. Bogataj et al. distinguish anterior chamber and papillate region in Porcellio scaber (https://pubmed.ncbi.nlm.nih.gov/30564048/ DOI:10.3897/zookeys.801.22395). Retain the minted regional habitat UNGROUNDED because no fitting identity or strictly broader regional term was verified; whole UBERON:0001046 hindgut is not a compartment superclass. The independent GOLD whole-hindgut context parent is excluded under #1331. Preserve node 7325 and the full source path; no universal crustacean microbiome or sample identity is inferred. This supersedes the 2026-08-16 GROUND_AS_PARENT decision, retained in Git and append-only session history. (source concept habitatmech:GOLD.53e4290463)", "curator": "codex-gpt-5", "timestamp": "2026-10-15T00:00:00Z"}, {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.19840c718e for habitatmech:GOLD.53e4290463 (Host-associated &gt; Arthropoda: Crustaceans &gt; Digestive system &gt; Hindgut &gt; Anterior chamber). Scientific review #1331: a crustacean anterior hindgut chamber is a compartment, not a subtype of whole hindgut. Bogataj et al. distinguish this region from the papillate region in Porcellio scaber (PMID:30564048). Exclude only this exact GOLD contribution, preserving node 7325 and full source path. The independent vertebrate-embryonic BTO:0000510 decision is corrected under #1332; do not replace it with whole UBERON:0001046 or the eye-chamber homonym. https://pubmed.ncbi.nlm.nih.gov/30564048/", "curator": "codex-gpt-5", "timestamp": "2026-10-15T00:00:00Z"}], "grounding_status": "UNGROUNDED", "habitat_category": "HOST_ASSOCIATED", "identifier": "habitatmech:GOLD.53e4290463", "label": "Anterior chamber", "mapping_status": "REVIEWED", "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7325", "source_label": "Anterior chamber", "source_path": "Host-associated &gt; Arthropoda: Crustaceans &gt; Digestive system &gt; Hindgut &gt; Anterior chamber"}]} |
| EPREV | reviews/structured/20261015T043316Z-anterior_chamber-remediation/review.yaml; Complete previous remediation review | supports | All three scientific findings and their resolved dispositions remain unchanged. |
| EFORMAT | history/mappings/anterior_chamber/2026-10-15T050035Z-codex-gpt-5-06460b.yaml; Complete append-only citation correction history | supports | Only PMID:30564048 in the decision note became its verified PubMed URL; no ontology validator, inventory, scientific decision or original saved review changed. |
| EDELIMITER | history/mappings/anterior_chamber/2026-10-15T050513Z-codex-gpt-5-56cab7.yaml; Complete append-only citation delimiter history | supports | The adjacent semicolon was removed so the rendered href equals the actual PubMed URL. |
| EGATE | tests/test_decisions.py; Decision-note evidence gate | supports | Existing ontology CURIE and label validation is unchanged. The original complete notes gate now passes with the established publication-URL convention. |

## Limits And Additional Notes

- Continuing-agent self-review, not independent approval. Native status is not promoted by this observation.
- Original GOLD organism/member identities remain unverified. Ontology and paper evidence retains the narrow scope and access limitations of the predecessor.
- The shared endpoint problem #1398 and typed-synonym extraction #1249 remain open outside any repaired local witness.
- No paid research or transcriptomic inference was performed. iModulonDB is not applicable.
- The first full CI run failed the decision-note citation spelling (#2159): 1,124 passed, one failed, three skipped. The focused decision suite now passes; final site/archive, full revised-head CI and protected queue validation remain separate publication gates. Map input equality and native map validation passed in the recorded follow-up checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T050816Z-anterior_chamber-publication
kind: record
repository: CultureBotAI/HabitatMech
title: 'Publication follow-up: Anterior chamber (habitatmech:GOLD.53e4290463)'
started_at: '2026-10-15T05:07:55Z'
finished_at: '2026-10-15T05:08:16Z'
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
summary: 'All three scientific predecessor findings remain resolved after a citation-format-only
  correction. Complete current record re-read confirms unchanged identity, source
  scope, ungrounded disposition and absent unsupported parents. Issue #2159 changes
  the verified paper identifier to its equivalent PubMed URL; it does not alter scientific
  evidence or certify shared export modeling.'
source:
  git_revision: 9000e3916da0f27a48a2a2f4ec9460bab67f7850
  state: git_commit
  inputs:
  - path: conf/record_review.yaml
    sha256: c2f5d0eb4c5744f5fe354c92184ddab144dc2688dba952b032b4f3d597bc08d6
    role: context
  - path: curation/decisions.tsv
    sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
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
    sha256: f00480e29971f1fa70408a9687e0a6546d0c5651f2c5c5b394bf271168394670
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
  - path: history/mappings/anterior_chamber/2026-10-15T050035Z-codex-gpt-5-06460b.yaml
    sha256: b774b4f9fd1d4514435d44c809d55e783056ca6d4516db594fa339faf533d9f6
    role: context
  - path: history/mappings/anterior_chamber/2026-10-15T050513Z-codex-gpt-5-56cab7.yaml
    sha256: 7bcd1fcd42982f1ec6fbf21bbdb28f9ea6c7fd0c7db3dbd7a24f4a7cdaf3ec00
    role: context
  - path: reviews/structured/20261015T041833Z-anterior_chamber-record/review.yaml
    sha256: 0e8c88a5862ca378419c5db23170ca7691310d33ec14d825875c50ce6e6d500e
    role: context
  - path: reviews/structured/20261015T043316Z-anterior_chamber-remediation/review.yaml
    sha256: 96213e3f93389734c3efb855468ea429921ea144f95f65c3cd58f6c45819c397
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_decisions.py
    sha256: ffc4ddc715739ff3d75920c496caeb67a27a7bb9de9720d9413db7fb322c6f91
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
  description: Full current anterior-chamber record re-read after the maintained decision-note
    publication citation was reformatted.
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
- check_id: CP0
  name: .venv/bin/python -m pytest -q tests/test_decisions.py tests/test_host_anatomy_review_repairs.py
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_decisions.py tests/test_host_anatomy_review_repairs.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.53e4290463
  summary: 'Actual execution 2026-10-15T05:01:01Z through 2026-10-15T05:05:46Z. .......................................................................  [100%]

    71 passed in 283.52s (0:04:43)'
  scope_note: Citation-format follow-up; exact scope is recorded in the command and
    output. Earlier retained checks have their original execution times.
- check_id: CP1
  name: .venv/bin/python -m pytest -q tests/test_decisions.py::test_curation_notes_do_not_cite_evidence_that_does_not_exist
  status: passed
  required: true
  command: .venv/bin/python -m pytest -q tests/test_decisions.py::test_curation_notes_do_not_cite_evidence_that_does_not_exist
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.53e4290463
  summary: 'Actual execution 2026-10-15T05:06:18Z through 2026-10-15T05:06:25Z. .                                                                        [100%]

    1 passed in 4.70s'
  scope_note: Citation-format follow-up; exact scope is recorded in the command and
    output. Earlier retained checks have their original execution times.
- check_id: CP2
  name: just validate-strict data/habitats/host_associated/anterior_chamber.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/anterior_chamber.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.53e4290463
  summary: "Actual execution 2026-10-15T05:06:17Z through 2026-10-15T05:06:28Z. uv\
    \ run python scripts/validate_strict.py data/habitats/host_associated/anterior_chamber.yaml\n\
    Validating 1 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Citation-format follow-up; exact scope is recorded in the command and
    output. Earlier retained checks have their original execution times.
- check_id: CP3
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.53e4290463
  summary: 'Actual execution 2026-10-15T05:06:28Z through 2026-10-15T05:06:48Z. No
    issues found

    746 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Citation-format follow-up; exact scope is recorded in the command and
    output. Earlier retained checks have their original execution times.
- check_id: CP4
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.53e4290463
  summary: "Actual execution 2026-10-15T05:06:48Z through 2026-10-15T05:07:24Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Citation-format follow-up; exact scope is recorded in the command and
    output. Earlier retained checks have their original execution times.
- check_id: CP5
  name: just text-map-inputs --output build/review-ce-map/citation-final-inputs.jsonl
  status: passed
  required: true
  command: just text-map-inputs --output build/review-ce-map/citation-final-inputs.jsonl
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.53e4290463
  summary: "Actual execution 2026-10-15T05:07:24Z through 2026-10-15T05:07:38Z. {\"\
    adapter_version\": \"habitatmech-semantic-v1\", \"jsonl_sha256\": \"49b0762b6a0e67362795e8881c2dc95174fa39b07431311de0025351c5c7b76d\"\
    , \"mode\": \"export\", \"output\": \"/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/build/review-ce-map/citation-final-inputs.jsonl\"\
    , \"records\": 3208, \"scope\": \"full\"}\n uv run python scripts/text_map_inputs.py\
    \ \"$@\""
  scope_note: Citation-format follow-up; exact scope is recorded in the command and
    output. Earlier retained checks have their original execution times.
- check_id: CP6
  name: cmp build/review-ce-map/current-inputs.jsonl build/review-ce-map/citation-final-inputs.jsonl
  status: passed
  required: true
  command: cmp build/review-ce-map/current-inputs.jsonl build/review-ce-map/citation-final-inputs.jsonl
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.53e4290463
  summary: 'Actual execution 2026-10-15T05:07:38Z through 2026-10-15T05:07:38Z. '
  scope_note: Citation-format follow-up; exact scope is recorded in the command and
    output. Earlier retained checks have their original execution times.
- check_id: CP7
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/embedding_pipeline.py check --output data/text_map --input build/review-ce-map/citation-final-inputs.jsonl
    --cache build/review-ce-map/download/build/text-map/vectors.sqlite
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/embedding_pipeline.py check --output data/text_map --input build/review-ce-map/citation-final-inputs.jsonl
    --cache build/review-ce-map/download/build/text-map/vectors.sqlite
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.53e4290463
  summary: "Actual execution 2026-10-15T05:07:38Z through 2026-10-15T05:07:42Z. {\n\
    \  \"coverage\": {\n    \"displayed\": 3208,\n    \"eligible\": 3208,\n    \"\
    maximum\": 50000,\n    \"omitted\": 0,\n    \"selection\": \"bottom-k-sha256(seed,identifier)\"\
    ,\n    \"total\": 3208\n  },\n  \"encoder\": {\n    \"dimension\": 1024,\n   \
    \ \"dtype\": \"float32-le\",\n    \"format_version\": 1,\n    \"inference_device\"\
    : \"cpu\",\n    \"library_versions\": {\n      \"numpy\": \"2.3.5\",\n      \"\
    sentence-transformers\": \"6.0.0\",\n      \"tokenizers\": \"0.23.2\",\n     \
    \ \"torch\": \"2.14.0\",\n      \"transformers\": \"5.17.0\"\n    },\n    \"max_seq_length\"\
    : 512,\n    \"model\": \"BAAI/bge-large-en-v1.5\",\n    \"normalized\": true,\n\
    \    \"pooling\": \"sentence-transformers-model\",\n    \"query_instruction\"\
    : null,\n    \"revision\": \"d4aa6901d3a41ba39fb536a557fa166f842b0e09\",\n   \
    \ \"truncation\": \"tail\",\n    \"weight_dtype\": \"torch.float32\"\n  },\n \
    \ \"encoder_profile_sha256\": \"15d9788b0f2912b22721f35398583eddad76f135f66de223319930f9d6013c6f\"\
    ,\n  \"files\": {\n    \"index.html\": \"5a7ab0318561613ed86a6ab638ab26eb9e4be7718bf4ce3ad3c30e0de07e1b83\"\
    ,\n    \"points.json\": \"d73b5d66586b74c5b3d45768de788cc6705f42fcd8b7a50e688b376a8d9853ac\"\
    \n  },\n  \"format_version\": 1,\n  \"generated_at_utc\": \"2026-10-15T04:29:21.998399+00:00\"\
    ,\n  \"inputs\": {\n    \"adapter_version\": \"habitatmech-semantic-v1\",\n  \
    \  \"categories\": {\n      \"AIR\": 7,\n      \"AQUATIC\": 468,\n      \"CLINICAL\"\
    : 4,\n      \"ENGINEERED\": 488,\n      \"FOOD\": 59,\n      \"HOST_ASSOCIATED\"\
    : 1650,\n      \"OTHER\": 179,\n      \"TERRESTRIAL\": 353\n    },\n    \"corpus_sha256\"\
    : \"5dc497c389e4216e2759ed6fb693f16fe0623367d992ec6c4d37491ae2f940b6\",\n    \"\
    count\": 3208,\n    \"input_sha256\": \"49b0762b6a0e67362795e8881c2dc95174fa39b07431311de0025351c5c7b76d\"\
    ,\n    \"records_sha256\": \"22c06c18716b8124525ea28ef57267a9afda735a4ef152b83227e7a94b61d86a\"\
    \n  },\n  \"projection\": {\n    \"FP_ratio\": 2.0,\n    \"MN_ratio\": 0.5,\n\
    \    \"apply_pca\": true,\n    \"dimensions\": 2,\n    \"distance\": \"euclidean\"\
    ,\n    \"effective_pairs\": {\n      \"further\": 30,\n      \"mid_near\": 8,\n\
    \      \"neighbors\": 15\n    },\n    \"implementation\": \"pacmap.PaCMAP\",\n\
    \    \"initialization\": \"pca\",\n    \"iterations\": [\n      100,\n      100,\n\
    \      250\n    ],\n    \"knn_backend\": \"faiss\",\n    \"learning_rate\": 1.0,\n\
    \    \"library_versions\": {\n      \"faiss-cpu\": \"1.15.0\",\n      \"numba\"\
    : \"0.63.1\",\n      \"numpy\": \"2.3.5\",\n      \"pacmap\": \"0.9.1\",\n   \
    \   \"scikit-learn\": \"1.8.0\"\n    },\n    \"method\": \"pacmap\",\n    \"neighbors\"\
    : 15,\n    \"requested_neighbors\": 15,\n    \"seed\": 42\n  },\n  \"representation\"\
    : \"semantic-text\",\n  \"source_vectors\": {\n    \"dtype\": \"float32-le\",\n\
    \    \"order\": \"points.json\",\n    \"sha256\": \"59153ecd462faeb1865f8da19b6d5d305809f89e93e667d7647ebcdf9085751a\"\
    ,\n    \"shape\": [\n      3208,\n      1024\n    ],\n    \"storage\": \"local-profile-bound-cache\"\
    \n  }\n}"
  scope_note: Citation-format follow-up; exact scope is recorded in the command and
    output. Earlier retained checks have their original execution times.
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
  accessed_at: '2026-10-15T05:08:16Z'
  support: supports
  summary: 'Complete record re-read: {"curation_history": [{"action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED.",
    "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action":
    "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits
    this concept. ITEM reassessment #1332: this source is the anterior chamber of
    a crustacean hindgut, not the eye chamber UBERON:0001766. BTO:0000510 explicitly
    denotes vertebrate embryonic hindgut and cannot subsume it. Bogataj et al. distinguish
    anterior chamber and papillate region in Porcellio scaber (https://pubmed.ncbi.nlm.nih.gov/30564048/
    DOI:10.3897/zookeys.801.22395). Retain the minted regional habitat UNGROUNDED
    because no fitting identity or strictly broader regional term was verified; whole
    UBERON:0001046 hindgut is not a compartment superclass. The independent GOLD whole-hindgut
    context parent is excluded under #1331. Preserve node 7325 and the full source
    path; no universal crustacean microbiome or sample identity is inferred. This
    supersedes the 2026-08-16 GROUND_AS_PARENT decision, retained in Git and append-only
    session history. (source concept habitatmech:GOLD.53e4290463)", "curator": "codex-gpt-5",
    "timestamp": "2026-10-15T00:00:00Z"}, {"action": "SOURCE_PARENT_EXCLUDED", "changes":
    "Excluded GOLD source-path parent contribution habitatmech:GOLD.19840c718e for
    habitatmech:GOLD.53e4290463 (Host-associated > Arthropoda: Crustaceans > Digestive
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
  snapshot_sha256: f00480e29971f1fa70408a9687e0a6546d0c5651f2c5c5b394bf271168394670
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T043316Z-anterior_chamber-remediation/review.yaml
  locator: Complete previous remediation review
  accessed_at: '2026-10-15T05:08:16Z'
  support: supports
  summary: All three scientific findings and their resolved dispositions remain unchanged.
  snapshot_sha256: 96213e3f93389734c3efb855468ea429921ea144f95f65c3cd58f6c45819c397
- evidence_id: EFORMAT
  kind: record_content
  reference: history/mappings/anterior_chamber/2026-10-15T050035Z-codex-gpt-5-06460b.yaml
  locator: Complete append-only citation correction history
  accessed_at: '2026-10-15T05:08:16Z'
  support: supports
  summary: Only PMID:30564048 in the decision note became its verified PubMed URL;
    no ontology validator, inventory, scientific decision or original saved review
    changed.
  snapshot_sha256: b774b4f9fd1d4514435d44c809d55e783056ca6d4516db594fa339faf533d9f6
- evidence_id: EDELIMITER
  kind: record_content
  reference: history/mappings/anterior_chamber/2026-10-15T050513Z-codex-gpt-5-56cab7.yaml
  locator: Complete append-only citation delimiter history
  accessed_at: '2026-10-15T05:08:16Z'
  support: supports
  summary: The adjacent semicolon was removed so the rendered href equals the actual
    PubMed URL.
  snapshot_sha256: 7bcd1fcd42982f1ec6fbf21bbdb28f9ea6c7fd0c7db3dbd7a24f4a7cdaf3ec00
- evidence_id: EGATE
  kind: record_content
  reference: tests/test_decisions.py
  locator: Decision-note evidence gate
  accessed_at: '2026-10-15T05:08:16Z'
  support: supports
  summary: Existing ontology CURIE and label validation is unchanged. The original
    complete notes gate now passes with the established publication-URL convention.
  snapshot_sha256: ffc4ddc715739ff3d75920c496caeb67a27a7bb9de9720d9413db7fb322c6f91
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
- assessment_id: A3
  area: provenance
  topic: Publication citation format
  outcome: supported
  summary: The same inspected paper and DOI are retained. Exact structured record
    comparison differs only in the citation spelling and adjacent delimiter; full
    semantic input bytes remain identical.
  target_ids:
  - habitatmech:GOLD.53e4290463
  evidence_ids:
  - EAFTER
  - EPREV
  - EFORMAT
  - EDELIMITER
  - EGATE
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
  - EFORMAT
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
    review_id: 20261015T043316Z-anterior_chamber-remediation
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
  - EFORMAT
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
    review_id: 20261015T043316Z-anterior_chamber-remediation
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
  - EFORMAT
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
    review_id: 20261015T043316Z-anterior_chamber-remediation
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
- 'The shared endpoint problem #1398 and typed-synonym extraction #1249 remain open
  outside any repaired local witness.'
- No paid research or transcriptomic inference was performed. iModulonDB is not applicable.
- 'The first full CI run failed the decision-note citation spelling (#2159): 1,124
  passed, one failed, three skipped. The focused decision suite now passes; final
  site/archive, full revised-head CI and protected queue validation remain separate
  publication gates. Map input equality and native map validation passed in the recorded
  follow-up checks.'
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T041833Z-anterior_chamber-record
  relationship: Exact pre-fix predecessor; all finding identities retained.
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T043316Z-anterior_chamber-remediation
  relationship: Exact predecessor before the publication citation format correction.
tags:
- individual-scientific-review
- remediation
- host-associated
```
