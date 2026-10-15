# Remediation review: catarrh

- Review: 20261015T224442Z-catarrh-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T22:24:59Z
- Finished UTC: 2026-10-15T22:44:42Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Excluded only the exact GOLD containing-anatomy contribution UBERON:0000341; independent valid genera and source paths remain. Original source observations, counts, units and taxa are preserved. Unresolved predecessor findings remain explicit.

## Scope And Provenance

Full regenerated target assessment and explicit disposition of every predecessor finding; identity replacement or source split includes all affected current identities and the retired predecessor.

Selection: One of fifteen repaired baseline targets in the 24-record carcinoid-through-cecum cohort; no new cohort sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base b5659e0d8bed801c41745839d9a2b69095aa9f4e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.62dfa9436e | data/habitats/host_associated/catarrh.yaml | generated | Catarrh |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/catarrh.yaml | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:45:12Z through 2026-10-15T21:45:14Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/catarrh.yaml |
| just validate-strict data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:45:33Z through 2026-10-15T21:45:42Z. uv run python scripts/validate_strict.py data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml<br>Validating 25 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      25<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:45:43Z through 2026-10-15T21:45:53Z. No issues found<br>828 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:45:53Z through 2026-10-15T21:45:54Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:45:54Z through 2026-10-15T21:46:11Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:46:11Z through 2026-10-15T21:46:15Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:46:15Z through 2026-10-15T21:46:38Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:46:38Z through 2026-10-15T21:47:36Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_cardiac_cartilage_cecum_review_repairs.py | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:47:36Z through 2026-10-15T21:47:44Z. ..                                                                       [100%]<br>2 passed in 6.45s |
| git diff --check 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:47:44Z through 2026-10-15T21:47:44Z.  |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_cardiac_cartilage_cecum_review_repairs.py | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T21:58:55Z through 2026-10-15T21:59:03Z. ..                                                                       [100%]<br>2 passed in 6.82s |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_decisions.py tests/test_cardiac_cartilage_cecum_review_repairs.py | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T22:16:03Z through 2026-10-15T22:19:46Z. ........................................................................ [100%]<br>72 passed in 221.76s (0:03:41) |
| just lint | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T22:19:50Z through 2026-10-15T22:19:51Z. All checks passed!<br> uv run ruff check  . |
| just validate-strict data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/ceca__2f9665ca.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T22:19:51Z through 2026-10-15T22:19:58Z. uv run python scripts/validate_strict.py data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/ceca__2f9665ca.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml<br>Validating 3 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      3<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T22:19:58Z through 2026-10-15T22:20:11Z. No issues found<br>829 history record(s) valid against src/habitatmech/schema/history.yaml |
| just verify-corpus | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T22:20:11Z through 2026-10-15T22:20:40Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python scripts/embedding_pipeline.py check --output data/text_map --input /private/tmp/habitatmech-review-cn-20261015-citation-map-inputs.jsonl --cache build/review-cn-map/download/build/text-map/vectors.sqlite | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T22:20:40Z through 2026-10-15T22:20:43Z. {<br>  "coverage": {<br>    "displayed": 3209,<br>    "eligible": 3209,<br>    "maximum": 50000,<br>    "omitted": 0,<br>    "selection": "bottom-k-sha256(seed,identifier)",<br>    "total": 3209<br>  },<br>  "encoder": {<br>    "dimension": 1024,<br>    "dtype": "float32-le",<br>    "format_version": 1,<br>    "inference_device": "cpu",<br>    "library_versions": {<br>      "numpy": "2.3.5",<br>      "sentence-transformers": "6.0.0",<br>      "tokenizers": "0.23.2",<br>      "torch": "2.14.0",<br>      "transformers": "5.17.0"<br>    },<br>    "max_seq_length": 512,<br>    "model": "BAAI/bge-large-en-v1.5",<br>    "normalized": true,<br>    "pooling": "sentence-transformers-model",<br>    "query_instruction": null,<br>    "revision": "d4aa6901d3a41ba39fb536a557fa166f842b0e09",<br>    "truncation": "tail",<br>    "weight_dtype": "torch.float32"<br>  },<br>  "encoder_profile_sha256": "15d9788b0f2912b22721f35398583eddad76f135f66de223319930f9d6013c6f",<br>  "files": {<br>    "index.html": "9af3cd50170b152332bde16c94f94e2d461b947dc07f03701dd288e9e66e0176",<br>    "points.json": "5f7c46b8701863a95b2021e4745ceaed5819e24c19dc522e052228d27ee7f22e"<br>  },<br>  "format_version": 1,<br>  "generated_at_utc": "2026-10-15T21:47:31.472391+00:00",<br>  "inputs": {<br>    "adapter_version": "habitatmech-semantic-v1",<br>    "categories": {<br>      "AIR": 7,<br>      "AQUATIC": 468,<br>      "CLINICAL": 4,<br>      "ENGINEERED": 488,<br>      "FOOD": 59,<br>      "HOST_ASSOCIATED": 1651,<br>      "OTHER": 179,<br>      "TERRESTRIAL": 353<br>    },<br>    "corpus_sha256": "9d77fbd6ae91b5b9403004cc4d0320a245ff4bb563c35547436ccb1a7ef431c8",<br>    "count": 3209,<br>    "input_sha256": "2e8d2ce36bbfede1123feb802a5653ae86926c2c83d924ef70ce3245c9018d5f",<br>    "records_sha256": "6f1e9d175eeb857b0fc52ea2ea3e98a617b9995baf321b0ffbeb77978eb0f024"<br>  },<br>  "projection": {<br>    "FP_ratio": 2.0,<br>    "MN_ratio": 0.5,<br>    "apply_pca": true,<br>    "dimensions": 2,<br>    "distance": "euclidean",<br>    "effective_pairs": {<br>      "further": 30,<br>      "mid_near": 8,<br>      "neighbors": 15<br>    },<br>    "implementation": "pacmap.PaCMAP",<br>    "initialization": "pca",<br>    "iterations": [<br>      100,<br>      100,<br>      250<br>    ],<br>    "knn_backend": "faiss",<br>    "learning_rate": 1.0,<br>    "library_versions": {<br>      "faiss-cpu": "1.15.0",<br>      "numba": "0.63.1",<br>      "numpy": "2.3.5",<br>      "pacmap": "0.9.1",<br>      "scikit-learn": "1.8.0"<br>    },<br>    "method": "pacmap",<br>    "neighbors": 15,<br>    "requested_neighbors": 15,<br>    "seed": 42<br>  },<br>  "representation": "semantic-text",<br>  "source_vectors": {<br>    "dtype": "float32-le",<br>    "order": "points.json",<br>    "sha256": "2fcf746746be1500ba74869a480d83a616377bc2ddff79fc354d4af39f8fefd5",<br>    "shape": [<br>      3209,<br>      1024<br>    ],<br>    "storage": "local-profile-bound-cache"<br>  }<br>} |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python scripts/render_pages.py --check | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T22:20:43Z through 2026-10-15T22:21:37Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 129 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpf4m4_epj/site<br>pages/ is in step with the corpus |
| git diff --check 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b | passed | True | habitatmech:GOLD.62dfa9436e | Executed 2026-10-15T22:21:37Z through 2026-10-15T22:21:38Z.  |
| Exact-revision full QC and structured archive contract | passed | True | habitatmech:GOLD.62dfa9436e | Verified 2026-10-15T22:43:10Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38816416003 |

## Scientific And Domain Assessments

### Correction and preservation

consistency: supported. Targets: habitatmech:GOLD.62dfa9436e.

Excluded only the exact GOLD containing-anatomy contribution UBERON:0000341; independent valid genera and source paths remain. Original source observations, counts, units and taxa are preserved. Unresolved predecessor findings remain explicit.

### Current identities, definition scope and strict ancestry

identity: concern. Targets: habitatmech:GOLD.62dfa9436e.

habitatmech:GOLD.62dfa9436e: Catarrh, UNGROUNDED/SEEDED, parents []. The bounded source identity is retained without inventing a missing genus or optional definition. Catarrh condition/material scope is not settled by a hierarchy edit.

### Frozen source counts, units, scores and taxa

quantity: supported. Targets: habitatmech:GOLD.62dfa9436e.

Source-specific nonadditive observations are retained. [[{"source": "GOLD", "source_id": "gold.ecosystem:6831", "source_label": "Catarrh", "source_path": "Host-associated &gt; Mammals &gt; Respiratory system &gt; Pharynx/Throat &gt; Catarrh"}]]

### Exact predecessor lineage and remaining findings

representation: concern. Targets: habitatmech:GOLD.62dfa9436e.

Every predecessor finding and affected target identity is retained. This scoped review does not certify exports.

## Findings

### F1: Containing anatomy is emitted as a broader habitat class

major / resolved / confirmed; issue key: catarrh-context-parent.

Corrected through maintained inputs and native regeneration. Excluded only the exact GOLD containing-anatomy contribution UBERON:0000341; independent valid genera and source paths remain.

Disposition: Excluded only the exact GOLD containing-anatomy contribution UBERON:0000341; independent valid genera and source paths remain.

### F2: Catarrh source meaning is unresolved between condition and material

major / open / provisional; issue key: catarrh-condition-material-scope.

Reassessed after scoped repair; remains unresolved. Condition versus accumulated mucus remains unresolved for this exact source. Neither interpretation warrants the removed whole-organ superclass. No unsupported NOT_APPLICABLE decision or material definition was added.

Disposition: Condition versus accumulated mucus remains unresolved for this exact source. Neither interpretation warrants the removed whole-organ superclass. No unsupported NOT_APPLICABLE decision or material definition was added.

## Recommended Actions And Acceptance Checks

### ACT2

Condition versus accumulated mucus remains unresolved for this exact source. Neither interpretation warrants the removed whole-organ superclass. No unsupported NOT_APPLICABLE decision or material definition was added. Recover exact source/specimen evidence and make an ITEM scope decision before defining or excluding this concept.

- Regress the exact claim, preserving independent valid genera, raw provenance and source counts/units. Change native status or mappings only when supported by the authorized ITEM assessment; never decrement source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000341/graph; UBERON_0000341-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000341", "target": "http://purl.obolibrary.org/obo/UBERON_0034929", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000341", "target": "http://purl.obolibrary.org/obo/UBERON_0000974", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000341; UBERON_0000341.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0000341", "label": "throat", "is_obsolete": false, "description": ["In anatomy, the throat is the anterior part of the neck, in front of the vertebral column. It consists of the pharynx and larynx. An important feature of the throat is the epiglottis, a flap which separates the esophagus from the trachea and prevents inhalation of food or drink. The throat contains various blood vessels, various pharyngeal muscles, the trachea (windpipe) and the esophagus. The hyoid bone and the clavicle are the only bones located in the throat of mammals. It is sometimes considered a synonym for fauces. [WP,unvetted]."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0034929/graph; UBERON_0034929-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0010000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0010314", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0000014", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0000475", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0001015", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0001021", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929", "target": "http://purl.obolibrary.org/obo/UBERON_0002049", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0034929; UBERON_0034929.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0034929", "label": "external soft tissue zone", "is_obsolete": false, "description": ["A region or zone on the surface of an organism that encompasses skin and any adnexa, down through muscles and bounded by underlying skeletal support structures."]} |
| EX5 | https://www.nhs.uk/conditions/catarrh/; nhs-catarrh.html | context_only | NHS terminology inspected: catarrh concerns mucus/phlegm accumulation in nose, sinuses and throat and associated symptoms. This supports a condition/material distinction from the containing anatomy, without resolving the exact two GOLD source meanings. |
| EAFTER0 | data/habitats/host_associated/catarrh.yaml; Entire regenerated target | supports | {"identifier": "habitatmech:GOLD.62dfa9436e", "label": "Catarrh", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "SEEDED", "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6831", "source_label": "Catarrh", "source_path": "Host-associated &gt; Mammals &gt; Respiratory system &gt; Pharynx/Throat &gt; Catarrh"}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. [CLASS-level] Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate. (source concept habitatmech:GOLD.62dfa9436e)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution UBERON:0000341 for habitatmech:GOLD.62dfa9436e (Host-associated &gt; Mammals &gt; Respiratory system &gt; Pharynx/Throat &gt; Catarrh). Review https://github.com/CultureBotAI/HabitatMech/issues/2206 : Neither the condition nor accumulated mucus is a subtype of the whole source anatomical region. Exclude only this exact GOLD contribution without deciding which meaning the source intended. Preserve source observations; condition/material scope remains open under #2210."}]} |
| EPREV | reviews/structured/20261015T212550Z-catarrh-record/review.yaml; Exact predecessor, all findings and source evidence | supports | Baseline observation retained byte-identically. Every finding retains its exact predecessor identity and issue key. |
| ETEST | tests/test_cardiac_cartilage_cecum_review_repairs.py; Full-corpus counterfactual, exact source partition, taxonomy preservation and public URL rendering | supports | Exactly fourteen shared record identities change, one incompatible ontology identity is removed and two minted source identities become records. Entire source-attestation multiset excluding only mapping predicates and all taxon-bearing records remain identical. Other identities remain byte-equivalent as generated documents. |
| EFIXTURE | tests/data/cardiac_cartilage_cecum_prior_decisions.json; Loader-normalized prior molluscan cecum decision | supports | Earlier effective decision content retained with loader defaults; original bytes remain in the baseline Git revision. |
| ERULE | docs/CURATION.md; Strict hierarchy, source identity and evidence rules | supports | Containment is not is-a; lexical homonyms do not establish cross-host anatomical equivalence. |
| EHISTORY | history/README.md; Generated audit trail versus immutable sessions | supports | Superseding a maintained decision regenerates its projection while saved session history and reviews remain append-only. |
| EI11 | curation/gold_parent_exclusions.tsv; Exact keyed rows 9 | supports | [[9, "habitatmech:GOLD.62dfa9436e\tHost-associated &gt; Mammals &gt; Respiratory system &gt; Pharynx/Throat &gt; Catarrh\tUBERON:0000341\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2206 : Neither the condition nor accumulated mucus is a subtype of the whole source anatomical region. Exclude only this exact GOLD contribution without deciding which meaning the source intended. Preserve source observations; condition/material scope remains open under #2210."]] |
| EI12 | curation/decisions.tsv; Exact keyed rows 616 | supports | [[616, "habitatmech:GOLD.62dfa9436e\tCONFIRM_UNGROUNDED\t\t\t\tclaude-opus-5\t2026-08-12\tClass-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.\tCLASS\t\t"]] |

## Limits And Additional Notes

- Individual source specimens and all original pair-level citations have not been independently reconstructed. Counts, ranks and source scores are not prevalence or characteristic presence.
- iModulonDB is not applicable to target claims: no gene, regulator, expression module or causal mechanism is asserted. Papers mentioning genes are used only for source context. No paid research was used.
- Same-agent adversarial review, not independent approval. Original inspected primary-source and specimen-level limits remain; no prevalence, characteristic presence or mechanism is inferred.
- Configured label validation has no-adapter skips, reported in the actual check result. No all-prefix identity or SSSOM/KGX conformance certification is made.
- Final-head checks must validate this new immutable successor. Recorded full QC covers the exact repaired scientific-input revision.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T224442Z-catarrh-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: catarrh'
started_at: '2026-10-15T22:24:59Z'
finished_at: '2026-10-15T22:44:42Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses target and evidence; not independent reviewer
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: Excluded only the exact GOLD containing-anatomy contribution UBERON:0000341;
  independent valid genera and source paths remain. Original source observations,
  counts, units and taxa are preserved. Unresolved predecessor findings remain explicit.
source:
  git_revision: b5659e0d8bed801c41745839d9a2b69095aa9f4e
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
    sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 7158cb696b7e2ac84a8d594a03015711424ff56e21c07a4648ffc6fb2e84a107
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: bc7a13d922c179cd9bcd4d37b348bc90a39b08a4dafba7af4ed0039ad99621c3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: 747e6a5612dc0b7ed881b9fb323fd57ab3c75794d9ee5ebb9d59b2be57dbf8cd
    role: context
  - path: data/habitats/host_associated/catarrh.yaml
    sha256: eb1d71e31efa2cebe7a8885cf804ab6ebfa45ef06e003b849f006fcc85058438
    role: target
  - path: data/habitats/host_associated/throat__4f7984ed.yaml
    sha256: f9efde64f7142c1477d2357f8c0ee6aa2ded232cf25d87816e637f67ee66ef2a
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
  - path: history/README.md
    sha256: 819361a711697f96ff9c1aa0b27e94302547970b3b54777d67ec1449db5e543a
    role: context
  - path: history/mappings/cardiac_cartilage_cecum_review/2026-10-15T214400Z-codex-gpt-5-909775.yaml
    sha256: 98f4d839aa9a9361d5167448a3425842998d8b1d3de14f11af61df5ce0657b52
    role: context
  - path: history/mappings/cardiac_molluscan_citation_format/2026-10-15T221623Z-codex-gpt-5-cea5ff.yaml
    sha256: 66ff55b4feec04542c81ca5b3ba004d2966dd915c1331a0e1901478d2e25b967
    role: context
  - path: history/mappings/cardiac_stomach/2026-10-15T214401Z-codex-gpt-5-ac65b1.yaml
    sha256: ca808e9e8293f2a2794605c6bb0459ced388b0b8f5e21cab7f8a4c6450aad762
    role: context
  - path: history/mappings/ceca__2f9665ca/2026-10-15T214402Z-codex-gpt-5-f5ef14.yaml
    sha256: 83f828ff3a626f06ada6e1f1cd260ff10046bd6f9abd06155ceaa8aeb7301c41
    role: context
  - path: history/mappings/cecum/2026-10-15T214403Z-codex-gpt-5-cf5c53.yaml
    sha256: 58234fcca34d0117048ee812c4319ed63453aa6add6d158ba89a41baefee9104
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261015T212550Z-catarrh-record/review.yaml
    sha256: 5aa491dab3126a0afcaef35a9f203194206716111846258a781d6ed08b890ef2
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
  - path: tests/data/cardiac_cartilage_cecum_prior_decisions.json
    sha256: 7266598936ff8418d36a26c8e0086c570dbf7706813d92981642c5e33dc8d256
    role: context
  - path: tests/test_cardiac_cartilage_cecum_review_repairs.py
    sha256: 1ca96d2b8fcf3d5016f8831dd3f3a1c51358e4ad752aa9237358259eb5583528
    role: context
targets:
- target_id: habitatmech:GOLD.62dfa9436e
  path: data/habitats/host_associated/catarrh.yaml
  label: Catarrh
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
scope:
  description: Full regenerated target assessment and explicit disposition of every
    predecessor finding; identity replacement or source split includes all affected
    current identities and the retired predecessor.
  selection: One of fifteen repaired baseline targets in the 24-record carcinoid-through-cecum
    cohort; no new cohort sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.62dfa9436e
  exclusions:
  - target: Other habitats and export compatibility
    reason: No full-corpus scientific sign-off or SSSOM/KGX certification. Original
      PREGO pair evidence remains bounded.
checks:
- check_id: C7
  name: just validate data/habitats/host_associated/catarrh.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/catarrh.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T21:45:12Z through 2026-10-15T21:45:14Z. No issues\
    \ found\n uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class\
    \ HabitatRecord data/habitats/host_associated/catarrh.yaml"
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C16
  name: just validate-strict data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml
    data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml
    data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml
    data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml
    data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml
    data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml
    data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml
    data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml
    data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml
    data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml
    data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml
    data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml
    data/habitats/host_associated/cecum_intestinal_cecum.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml
    data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml
    data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml
    data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml
    data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml
    data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml
    data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml
    data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml
    data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml
    data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml
    data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml
    data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml
    data/habitats/host_associated/cecum_intestinal_cecum.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T21:45:33Z through 2026-10-15T21:45:42Z. uv run python\
    \ scripts/validate_strict.py data/habitats/host_associated/carcinoid.yaml data/habitats/host_associated/carcinoma.yaml\
    \ data/habitats/host_associated/carcinoma_cell.yaml data/habitats/host_associated/carcinosarcoma.yaml\
    \ data/habitats/host_associated/cardiac_atrium.yaml data/habitats/host_associated/cardiac_septum.yaml\
    \ data/habitats/host_associated/cardiac_skeleton.yaml data/habitats/host_associated/cardiac_stomach.yaml\
    \ data/habitats/host_associated/cardiovascular_system.yaml data/habitats/host_associated/carposphere.yaml\
    \ data/habitats/host_associated/cartilage.yaml data/habitats/host_associated/cartilage__bd8c407c.yaml\
    \ data/habitats/host_associated/cartilage__c54322c6.yaml data/habitats/host_associated/caryopsis.yaml\
    \ data/habitats/host_associated/caski.yaml data/habitats/host_associated/catarrh.yaml\
    \ data/habitats/host_associated/catarrh__1e78e51c.yaml data/habitats/host_associated/caulosphere.yaml\
    \ data/habitats/host_associated/ceca.yaml data/habitats/host_associated/ceca__2f9665ca.yaml\
    \ data/habitats/host_associated/ceca__d15faa5d.yaml data/habitats/host_associated/cecotropes_night_fecs.yaml\
    \ data/habitats/host_associated/cecum.yaml data/habitats/host_associated/cecum__79e270ae.yaml\
    \ data/habitats/host_associated/cecum_intestinal_cecum.yaml\nValidating 25 files\
    \ with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      25\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C17
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: 'Executed 2026-10-15T21:45:43Z through 2026-10-15T21:45:53Z. No issues
    found

    828 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C18
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T21:45:53Z through 2026-10-15T21:45:54Z. provenance\
    \ current: 14 committed inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C19
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T21:45:54Z through 2026-10-15T21:46:11Z. expected 3209\
    \ records, found 3209 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\
    \ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C20
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T21:46:11Z through 2026-10-15T21:46:15Z. validated\
    \ 32 causal-graph curation file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C21
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T21:46:15Z through 2026-10-15T21:46:38Z. term-request\
    \ table is current (110 terms)\n uv run python scripts/build_term_requests.py\
    \ --check"
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C22
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T21:46:38Z through 2026-10-15T21:47:36Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n\
    \ uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C23
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_cardiac_cartilage_cecum_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_cardiac_cartilage_cecum_review_repairs.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: 'Executed 2026-10-15T21:47:36Z through 2026-10-15T21:47:44Z. ..                                                                       [100%]

    2 passed in 6.45s'
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C24
  name: git diff --check 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b
  status: passed
  required: true
  command: git diff --check 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: 'Executed 2026-10-15T21:47:44Z through 2026-10-15T21:47:44Z. '
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C25
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_cardiac_cartilage_cecum_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_cardiac_cartilage_cecum_review_repairs.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: 'Executed 2026-10-15T21:58:55Z through 2026-10-15T21:59:03Z. ..                                                                       [100%]

    2 passed in 6.82s'
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat. Historical intermediate-repair execution, before
    the later lint/citation corrections; retained as executed evidence, not asserted
    to have been rerun at the current revision. Later focused checks and exact-revision
    CI cover the corrected inputs.
- check_id: C26
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_decisions.py tests/test_cardiac_cartilage_cecum_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_decisions.py tests/test_cardiac_cartilage_cecum_review_repairs.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: 'Executed 2026-10-15T22:16:03Z through 2026-10-15T22:19:46Z. ........................................................................
    [100%]

    72 passed in 221.76s (0:03:41)'
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat.
- check_id: C27
  name: just lint
  status: passed
  required: true
  command: just lint
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T22:19:50Z through 2026-10-15T22:19:51Z. All checks\
    \ passed!\n uv run ruff check  ."
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat.
- check_id: C28
  name: just validate-strict data/habitats/host_associated/cardiac_stomach.yaml data/habitats/host_associated/ceca__2f9665ca.yaml
    data/habitats/host_associated/cecum_intestinal_cecum.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/cardiac_stomach.yaml
    data/habitats/host_associated/ceca__2f9665ca.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T22:19:51Z through 2026-10-15T22:19:58Z. uv run python\
    \ scripts/validate_strict.py data/habitats/host_associated/cardiac_stomach.yaml\
    \ data/habitats/host_associated/ceca__2f9665ca.yaml data/habitats/host_associated/cecum_intestinal_cecum.yaml\n\
    Validating 3 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      3\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat.
- check_id: C29
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: 'Executed 2026-10-15T22:19:58Z through 2026-10-15T22:20:11Z. No issues
    found

    829 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat.
- check_id: C30
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T22:20:11Z through 2026-10-15T22:20:40Z. expected 3209\
    \ records, found 3209 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\
    \ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat.
- check_id: C31
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/embedding_pipeline.py check --output data/text_map --input /private/tmp/habitatmech-review-cn-20261015-citation-map-inputs.jsonl
    --cache build/review-cn-map/download/build/text-map/vectors.sqlite
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/embedding_pipeline.py check --output data/text_map --input /private/tmp/habitatmech-review-cn-20261015-citation-map-inputs.jsonl
    --cache build/review-cn-map/download/build/text-map/vectors.sqlite
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: "Executed 2026-10-15T22:20:40Z through 2026-10-15T22:20:43Z. {\n  \"coverage\"\
    : {\n    \"displayed\": 3209,\n    \"eligible\": 3209,\n    \"maximum\": 50000,\n\
    \    \"omitted\": 0,\n    \"selection\": \"bottom-k-sha256(seed,identifier)\"\
    ,\n    \"total\": 3209\n  },\n  \"encoder\": {\n    \"dimension\": 1024,\n   \
    \ \"dtype\": \"float32-le\",\n    \"format_version\": 1,\n    \"inference_device\"\
    : \"cpu\",\n    \"library_versions\": {\n      \"numpy\": \"2.3.5\",\n      \"\
    sentence-transformers\": \"6.0.0\",\n      \"tokenizers\": \"0.23.2\",\n     \
    \ \"torch\": \"2.14.0\",\n      \"transformers\": \"5.17.0\"\n    },\n    \"max_seq_length\"\
    : 512,\n    \"model\": \"BAAI/bge-large-en-v1.5\",\n    \"normalized\": true,\n\
    \    \"pooling\": \"sentence-transformers-model\",\n    \"query_instruction\"\
    : null,\n    \"revision\": \"d4aa6901d3a41ba39fb536a557fa166f842b0e09\",\n   \
    \ \"truncation\": \"tail\",\n    \"weight_dtype\": \"torch.float32\"\n  },\n \
    \ \"encoder_profile_sha256\": \"15d9788b0f2912b22721f35398583eddad76f135f66de223319930f9d6013c6f\"\
    ,\n  \"files\": {\n    \"index.html\": \"9af3cd50170b152332bde16c94f94e2d461b947dc07f03701dd288e9e66e0176\"\
    ,\n    \"points.json\": \"5f7c46b8701863a95b2021e4745ceaed5819e24c19dc522e052228d27ee7f22e\"\
    \n  },\n  \"format_version\": 1,\n  \"generated_at_utc\": \"2026-10-15T21:47:31.472391+00:00\"\
    ,\n  \"inputs\": {\n    \"adapter_version\": \"habitatmech-semantic-v1\",\n  \
    \  \"categories\": {\n      \"AIR\": 7,\n      \"AQUATIC\": 468,\n      \"CLINICAL\"\
    : 4,\n      \"ENGINEERED\": 488,\n      \"FOOD\": 59,\n      \"HOST_ASSOCIATED\"\
    : 1651,\n      \"OTHER\": 179,\n      \"TERRESTRIAL\": 353\n    },\n    \"corpus_sha256\"\
    : \"9d77fbd6ae91b5b9403004cc4d0320a245ff4bb563c35547436ccb1a7ef431c8\",\n    \"\
    count\": 3209,\n    \"input_sha256\": \"2e8d2ce36bbfede1123feb802a5653ae86926c2c83d924ef70ce3245c9018d5f\"\
    ,\n    \"records_sha256\": \"6f1e9d175eeb857b0fc52ea2ea3e98a617b9995baf321b0ffbeb77978eb0f024\"\
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
    \    \"order\": \"points.json\",\n    \"sha256\": \"2fcf746746be1500ba74869a480d83a616377bc2ddff79fc354d4af39f8fefd5\"\
    ,\n    \"shape\": [\n      3209,\n      1024\n    ],\n    \"storage\": \"local-profile-bound-cache\"\
    \n  }\n}"
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat.
- check_id: C32
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/render_pages.py --check
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/render_pages.py --check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: 'Executed 2026-10-15T22:20:43Z through 2026-10-15T22:21:37Z. rendered 3209
    habitat pages, 259 redirect stubs, 8 categories, 129 term requests -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpf4m4_epj/site

    pages/ is in step with the corpus'
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat.
- check_id: C33
  name: git diff --check 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b
  status: passed
  required: true
  command: git diff --check 62952fb7cdf223af9d1ffbf1cc2f556b22f7ee6b
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: 'Executed 2026-10-15T22:21:37Z through 2026-10-15T22:21:38Z. '
  scope_note: Ordinary schema for the sixteen changed current records; strict for
    all 25 current cohort records; other checks retain documented full-corpus scope.
    Historical identity disposition is checked through the source-partition regression,
    not validation as a live habitat.
- check_id: CCI
  name: Exact-revision full QC and structured archive contract
  status: passed
  required: true
  command: gh run view 38816416003 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  summary: Verified 2026-10-15T22:43:10Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38816416003
  scope_note: Exact repaired scientific-input revision, before this successor is saved.
    Final-head checks remain mandatory.
evidence:
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000341/graph
  locator: UBERON_0000341-graph.json
  accessed_at: '2026-10-15T21:14:04Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000341",
    "target": "http://purl.obolibrary.org/obo/UBERON_0034929", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000341",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000974", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: fb0a10679ac3bb18e2e78af98903cdd8f1d973a83ff690ff5709d4545450e37a
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000341
  locator: UBERON_0000341.json
  accessed_at: '2026-10-15T21:14:03Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0000341",
    "label": "throat", "is_obsolete": false, "description": ["In anatomy, the throat
    is the anterior part of the neck, in front of the vertebral column. It consists
    of the pharynx and larynx. An important feature of the throat is the epiglottis,
    a flap which separates the esophagus from the trachea and prevents inhalation
    of food or drink. The throat contains various blood vessels, various pharyngeal
    muscles, the trachea (windpipe) and the esophagus. The hyoid bone and the clavicle
    are the only bones located in the throat of mammals. It is sometimes considered
    a synonym for fauces. [WP,unvetted]."]}'
  snapshot_sha256: 9309b245c1b628164cfbb141a78638cfdd5c8875b8113e5f8006708e8c164395
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0034929/graph
  locator: UBERON_0034929-graph.json
  accessed_at: '2026-10-15T21:14:27Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0010000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0010314", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000014", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000475", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001015", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001021", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0034929",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002049", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}]'
  snapshot_sha256: b29546fda916e47b82ba2cde0fc537bba943c7fa7fabacc3024d14e0398afa64
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0034929
  locator: UBERON_0034929.json
  accessed_at: '2026-10-15T21:14:26Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0034929",
    "label": "external soft tissue zone", "is_obsolete": false, "description": ["A
    region or zone on the surface of an organism that encompasses skin and any adnexa,
    down through muscles and bounded by underlying skeletal support structures."]}'
  snapshot_sha256: b14ff3638a856ff89ab4a75e976e0c396b738a6a568159f4f43beea3aac7b4f9
- evidence_id: EX5
  kind: database
  reference: https://www.nhs.uk/conditions/catarrh/
  locator: nhs-catarrh.html
  accessed_at: '2026-10-15T21:21:15Z'
  support: context_only
  summary: 'NHS terminology inspected: catarrh concerns mucus/phlegm accumulation
    in nose, sinuses and throat and associated symptoms. This supports a condition/material
    distinction from the containing anatomy, without resolving the exact two GOLD
    source meanings.'
  snapshot_sha256: d4e1f1c6bc1195a06ec158b06cb60298ba882aef4c2e01120028a7733a84aea6
- evidence_id: EAFTER0
  kind: record_content
  reference: data/habitats/host_associated/catarrh.yaml
  locator: Entire regenerated target
  accessed_at: '2026-10-15T22:44:42Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.62dfa9436e", "label": "Catarrh", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "SEEDED",
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6831",
    "source_label": "Catarrh", "source_path": "Host-associated > Mammals > Respiratory
    system > Pharynx/Throat > Catarrh"}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z",
    "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed
    UNGROUNDED: no ontology term fits this concept. [CLASS-level] Class-level sweep
    (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate. (source concept habitatmech:GOLD.62dfa9436e)"},
    {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-15T00:00:00Z", "curator":
    "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path
    parent contribution UBERON:0000341 for habitatmech:GOLD.62dfa9436e (Host-associated
    > Mammals > Respiratory system > Pharynx/Throat > Catarrh). Review https://github.com/CultureBotAI/HabitatMech/issues/2206
    : Neither the condition nor accumulated mucus is a subtype of the whole source
    anatomical region. Exclude only this exact GOLD contribution without deciding
    which meaning the source intended. Preserve source observations; condition/material
    scope remains open under #2210."}]}'
  snapshot_sha256: eb1d71e31efa2cebe7a8885cf804ab6ebfa45ef06e003b849f006fcc85058438
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T212550Z-catarrh-record/review.yaml
  locator: Exact predecessor, all findings and source evidence
  accessed_at: '2026-10-15T22:44:42Z'
  support: supports
  summary: Baseline observation retained byte-identically. Every finding retains its
    exact predecessor identity and issue key.
  snapshot_sha256: 5aa491dab3126a0afcaef35a9f203194206716111846258a781d6ed08b890ef2
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_cardiac_cartilage_cecum_review_repairs.py
  locator: Full-corpus counterfactual, exact source partition, taxonomy preservation
    and public URL rendering
  accessed_at: '2026-10-15T22:44:42Z'
  support: supports
  summary: Exactly fourteen shared record identities change, one incompatible ontology
    identity is removed and two minted source identities become records. Entire source-attestation
    multiset excluding only mapping predicates and all taxon-bearing records remain
    identical. Other identities remain byte-equivalent as generated documents.
  snapshot_sha256: 1ca96d2b8fcf3d5016f8831dd3f3a1c51358e4ad752aa9237358259eb5583528
- evidence_id: EFIXTURE
  kind: record_content
  reference: tests/data/cardiac_cartilage_cecum_prior_decisions.json
  locator: Loader-normalized prior molluscan cecum decision
  accessed_at: '2026-10-15T22:44:42Z'
  support: supports
  summary: Earlier effective decision content retained with loader defaults; original
    bytes remain in the baseline Git revision.
  snapshot_sha256: 7266598936ff8418d36a26c8e0086c570dbf7706813d92981642c5e33dc8d256
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict hierarchy, source identity and evidence rules
  accessed_at: '2026-10-15T22:44:42Z'
  support: supports
  summary: Containment is not is-a; lexical homonyms do not establish cross-host anatomical
    equivalence.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EHISTORY
  kind: authority
  reference: history/README.md
  locator: Generated audit trail versus immutable sessions
  accessed_at: '2026-10-15T22:44:42Z'
  support: supports
  summary: Superseding a maintained decision regenerates its projection while saved
    session history and reviews remain append-only.
  snapshot_sha256: 819361a711697f96ff9c1aa0b27e94302547970b3b54777d67ec1449db5e543a
- evidence_id: EI11
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact keyed rows 9
  accessed_at: '2026-10-15T22:44:42Z'
  support: supports
  summary: '[[9, "habitatmech:GOLD.62dfa9436e\tHost-associated > Mammals > Respiratory
    system > Pharynx/Throat > Catarrh\tUBERON:0000341\tcodex-gpt-5\t2026-10-15\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2206 : Neither the condition
    nor accumulated mucus is a subtype of the whole source anatomical region. Exclude
    only this exact GOLD contribution without deciding which meaning the source intended.
    Preserve source observations; condition/material scope remains open under #2210."]]'
  snapshot_sha256: 7158cb696b7e2ac84a8d594a03015711424ff56e21c07a4648ffc6fb2e84a107
- evidence_id: EI12
  kind: record_content
  reference: curation/decisions.tsv
  locator: Exact keyed rows 616
  accessed_at: '2026-10-15T22:44:42Z'
  support: supports
  summary: '[[616, "habitatmech:GOLD.62dfa9436e\tCONFIRM_UNGROUNDED\t\t\t\tclaude-opus-5\t2026-08-12\tClass-level
    sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice
    matched this label by any search route. Whether the concept is a habitat at all
    was NOT assessed, so this is not yet a term-request candidate.\tCLASS\t\t"]]'
  snapshot_sha256: e5cb2e09f72dd4b18e069c0e2576e25e13e56c9991f4eb5ae47416345e247578
assessments:
- assessment_id: A0
  area: consistency
  topic: Correction and preservation
  outcome: supported
  summary: Excluded only the exact GOLD containing-anatomy contribution UBERON:0000341;
    independent valid genera and source paths remain. Original source observations,
    counts, units and taxa are preserved. Unresolved predecessor findings remain explicit.
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EAFTER0
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI11
  - EI12
- assessment_id: A1
  area: identity
  topic: Current identities, definition scope and strict ancestry
  outcome: concern
  summary: 'habitatmech:GOLD.62dfa9436e: Catarrh, UNGROUNDED/SEEDED, parents []. The
    bounded source identity is retained without inventing a missing genus or optional
    definition. Catarrh condition/material scope is not settled by a hierarchy edit.'
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EAFTER0
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI11
  - EI12
  dimensions:
  - name: native_status
    value: '{"habitatmech:GOLD.62dfa9436e": "UNGROUNDED/SEEDED"}'
    definition: Native current states, distinct from scientific review verdict; a
      retired identity has no current native status.
    evidence_ids:
    - EX1
    - EX2
    - EX3
    - EX4
    - EX5
    - EAFTER0
    - EPREV
    - ETEST
    - EFIXTURE
    - ERULE
    - EHISTORY
    - EI11
    - EI12
- assessment_id: A2
  area: quantity
  topic: Frozen source counts, units, scores and taxa
  outcome: supported
  summary: 'Source-specific nonadditive observations are retained. [[{"source": "GOLD",
    "source_id": "gold.ecosystem:6831", "source_label": "Catarrh", "source_path":
    "Host-associated > Mammals > Respiratory system > Pharynx/Throat > Catarrh"}]]'
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EAFTER0
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI11
  - EI12
- assessment_id: A3
  area: representation
  topic: Exact predecessor lineage and remaining findings
  outcome: concern
  summary: Every predecessor finding and affected target identity is retained. This
    scoped review does not certify exports.
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EAFTER0
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI11
  - EI12
findings:
- finding_id: F1
  issue_key: catarrh-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Containing anatomy is emitted as a broader habitat class
  description: Corrected through maintained inputs and native regeneration. Excluded
    only the exact GOLD containing-anatomy contribution UBERON:0000341; independent
    valid genera and source paths remain.
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EAFTER0
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI11
  - EI12
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2206
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T212550Z-catarrh-record
    finding_id: F1
  disposition_reason: Excluded only the exact GOLD containing-anatomy contribution
    UBERON:0000341; independent valid genera and source paths remain.
- finding_id: F2
  issue_key: catarrh-condition-material-scope
  category: identity
  severity: major
  status: open
  certainty: provisional
  title: Catarrh source meaning is unresolved between condition and material
  description: Reassessed after scoped repair; remains unresolved. Condition versus
    accumulated mucus remains unresolved for this exact source. Neither interpretation
    warrants the removed whole-organ superclass. No unsupported NOT_APPLICABLE decision
    or material definition was added.
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  field_paths:
  - grounding_status
  - parent_habitats
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EAFTER0
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI11
  - EI12
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2210
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T212550Z-catarrh-record
    finding_id: F2
  disposition_reason: Condition versus accumulated mucus remains unresolved for this
    exact source. Neither interpretation warrants the removed whole-organ superclass.
    No unsupported NOT_APPLICABLE decision or material definition was added.
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.62dfa9436e
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Condition versus accumulated mucus remains unresolved for this exact
    source. Neither interpretation warrants the removed whole-organ superclass. No
    unsupported NOT_APPLICABLE decision or material definition was added. Recover
    exact source/specimen evidence and make an ITEM scope decision before defining
    or excluding this concept.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact claim, preserving independent valid genera, raw provenance and
    source counts/units. Change native status or mappings only when supported by the
    authorized ITEM assessment; never decrement source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Individual source specimens and all original pair-level citations have not been
  independently reconstructed. Counts, ranks and source scores are not prevalence
  or characteristic presence.
- 'iModulonDB is not applicable to target claims: no gene, regulator, expression module
  or causal mechanism is asserted. Papers mentioning genes are used only for source
  context. No paid research was used.'
- Same-agent adversarial review, not independent approval. Original inspected primary-source
  and specimen-level limits remain; no prevalence, characteristic presence or mechanism
  is inferred.
- Configured label validation has no-adapter skips, reported in the actual check result.
  No all-prefix identity or SSSOM/KGX conformance certification is made.
- Final-head checks must validate this new immutable successor. Recorded full QC covers
  the exact repaired scientific-input revision.
notes: []
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T212550Z-catarrh-record
  relationship: Exact predecessor; every finding and affected target is explicitly
    reconciled.
```
