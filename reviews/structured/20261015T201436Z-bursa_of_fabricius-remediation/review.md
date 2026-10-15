# Remediation review: bursa of Fabricius (UBERON:0003903)

- Review: 20261015T201436Z-bursa_of_fabricius-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T19:57:52Z
- Finished UTC: 2026-10-15T20:14:36Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed only the exact GOLD context-parent contribution habitatmech:GOLD.f65007e88e. All source identifiers, paths, counts/units and taxa remain intact. No unresolved finding remains in this exact target scope; specimen-level limits still apply.

## Scope And Provenance

Full regenerated target re-read and explicit disposition of every exact predecessor finding.

Selection: One of sixteen repaired targets in the twenty-four-record brown-algal through carcass cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 094ed0793c629eb7a9c279dc8ce9d26b642e11d8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0003903 | data/habitats/host_associated/bursa_of_fabricius.yaml | generated | bursa of Fabricius |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/bursa_of_fabricius.yaml | passed | True | UBERON:0003903 | Executed 2026-10-15T19:50:02Z through 2026-10-15T19:50:06Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bursa_of_fabricius.yaml |
| just validate-strict data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml | passed | True | UBERON:0003903 | Executed 2026-10-15T19:50:41Z through 2026-10-15T19:50:52Z. uv run python scripts/validate_strict.py data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | UBERON:0003903 | Executed 2026-10-15T19:50:52Z through 2026-10-15T19:51:06Z. No issues found<br>824 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | UBERON:0003903 | Executed 2026-10-15T19:51:06Z through 2026-10-15T19:51:07Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | UBERON:0003903 | Executed 2026-10-15T19:51:07Z through 2026-10-15T19:51:31Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | UBERON:0003903 | Executed 2026-10-15T19:51:31Z through 2026-10-15T19:51:37Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | UBERON:0003903 | Executed 2026-10-15T19:51:37Z through 2026-10-15T19:52:00Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | UBERON:0003903 | Executed 2026-10-15T19:52:00Z through 2026-10-15T19:52:58Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_buccal_camelid_caeca_review_repairs.py | passed | True | UBERON:0003903 | Executed 2026-10-15T19:52:58Z through 2026-10-15T19:53:05Z. ..                                                                       [100%]<br>2 passed in 6.03s |
| git diff --check a073f8e821a7c095f35501982930cc5a156835c0 | passed | True | UBERON:0003903 | Executed 2026-10-15T19:53:05Z through 2026-10-15T19:53:05Z.  |
| Exact-revision full QC and structured archive contract | passed | True | UBERON:0003903 | Verified 2026-10-15T20:14:20Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38798112068 |

## Scientific And Domain Assessments

### Correction and preservation

consistency: supported. Targets: UBERON:0003903.

Removed only the exact GOLD context-parent contribution habitatmech:GOLD.f65007e88e. All source identifiers, paths, counts/units and taxa remain intact. No unresolved finding remains in this exact target scope; specimen-level limits still apply.

### Current identity, definition and ancestry

identity: supported. Targets: UBERON:0003903.

Current target: bursa of Fabricius (UBERON:0003903), EXACT/SEEDED. Parents: ["UBERON:0004177", "UBERON:0011510", "UBERON:0013765"]. The unchanged source identity remains distinct; no replacement genus or merge is inferred.

### Frozen source assertions and taxa

quantity: supported. Targets: UBERON:0003903.

All source IDs, paths, counts/units, taxon IDs, labels, ranks and scores are unchanged. Current attestations: [{"source": "GOLD", "source_id": "gold.ecosystem:7474", "source_label": "Bursa of Fabricius", "source_path": "Host-associated &gt; Birds &gt; Lymphatic system &gt; Bursa of Fabricius", "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]. Three caecal targets alone lose unsupported mapping_predicate after explicit ITEM reassessment; zero omissions and independent source units remain distinct.

### Remaining scoped findings

representation: supported. Targets: UBERON:0003903.

Every predecessor issue key and exact target scope is preserved. A resolved local caecum mapping witness does not close the shared #1398 contract; unresolved original PREGO evidence and category-policy questions are not decided by this repair.

## Findings

### F1: GOLD context is not a broader habitat class

major / resolved / confirmed; issue key: bursa-of-fabricius-context-parent.

Corrected through the maintained input and native regeneration. Removed only the exact GOLD context-parent contribution habitatmech:GOLD.f65007e88e.

Disposition: Removed only the exact GOLD context-parent contribution habitatmech:GOLD.f65007e88e.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002465/graph; UBERON_0002465-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0002465", "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002465", "target": "http://purl.obolibrary.org/obo/NCBITaxon_7711", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002465", "target": "http://purl.obolibrary.org/obo/UBERON_0002193", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002465", "target": "http://purl.obolibrary.org/obo/UBERON_0002405", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002465; UBERON_0002465.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "UBERON:0002465", "label": "lymphoid system", "is_obsolete": false, "description": ["The lymphatic system in vertebrates is a network of conduits that carry a clear fluid called lymph. It also includes the lymphoid tissue through which the lymph travels. Lymphoid tissue is found in many organs, particularly the lymph nodes, and in the lymphoid follicles associated with the digestive system such as the tonsils. The system also includes all the structures dedicated to the circulation and production of lymphocytes, which includes the spleen, thymus, bone marrow and the lymphoid tissue associated with the digestive system[WP]."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0003903/graph; UBERON_0003903-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0003903", "target": "http://purl.obolibrary.org/obo/UBERON_0004177", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003903", "target": "http://purl.obolibrary.org/obo/UBERON_0011510", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003903", "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003903", "target": "http://purl.obolibrary.org/obo/GO_0030097", "uri": "http://purl.obolibrary.org/obo/BFO_0000067", "label": "contains process"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003903", "target": "http://purl.obolibrary.org/obo/GO_0030183", "uri": "http://purl.obolibrary.org/obo/BFO_0000067", "label": "contains process"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003903", "target": "http://purl.obolibrary.org/obo/NCBITaxon_8457", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0003903; UBERON_0003903.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "UBERON:0003903", "label": "bursa of Fabricius", "is_obsolete": false, "description": ["An epithelial and lymphoid organ that develops as a dorsal diverticulum of the proctodeal region of the cloaca in birds. The luminal (interior) surface of the bursa is plicated with as many as 15 primary and 7 secondary plicae or folds. These plicae have hundreds of bursal follicles containing follicle-associated epithelial cells, lymphocytes, macrophages, and plasma cells. Lymphoid stem cells migrate from the fetal liver to the bursa during ontogeny. In the bursa, these stem cells acquire the characteristics of mature, immunocompetent B cells[WP]. The bursa is an organ found in birds involved in B cell differentiation[GO]."]} |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0004177/graph; UBERON_0004177-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0004177", "target": "http://purl.obolibrary.org/obo/UBERON_0000062", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0004177", "target": "http://purl.obolibrary.org/obo/UBERON_0002390", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0004177; UBERON_0004177.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "UBERON:0004177", "label": "hemopoietic organ", "is_obsolete": false, "description": ["Organ that is part of the hematopoietic system."]} |
| EX7 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0011510/graph; UBERON_0011510-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0011510", "target": "http://purl.obolibrary.org/obo/UBERON_0000063", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0011510", "target": "http://purl.obolibrary.org/obo/UBERON_0000162", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX8 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0011510; UBERON_0011510.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "UBERON:0011510", "label": "cloacal bursa", "is_obsolete": false, "description": ["Taxon notes: in cryptodires, bursae apparently function primarily in buoyancy control and secondarily in ion transport and nesting, but several pleurodires have been shown recently to use them in aquatic respiration.[PMID:11479904]", "An evagination of the cloaca. In Testudines these are hypothesized to function in different physiological roles, primarily in respiration."]} |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0013765/graph; UBERON_0013765-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0013765", "target": "http://purl.obolibrary.org/obo/UBERON_0000062", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0013765", "target": "http://purl.obolibrary.org/obo/UBERON_0001007", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0013765; UBERON_0013765.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "UBERON:0013765", "label": "digestive system element", "is_obsolete": false, "description": ["Any of the organs or elements that are part of the digestive system. Examples: tongue, esophagus, spleen, crop, lunge feeding organ, tooth elements."]} |
| EAFTER | data/habitats/host_associated/bursa_of_fabricius.yaml; Entire regenerated target | supports | {"identifier": "UBERON:0003903", "label": "bursa of Fabricius", "definition": "An epithelial and lymphoid organ that develops as a dorsal diverticulum of the proctodeal region of the cloaca in birds. The luminal (interior) surface of the bursa is plicated with as many as 15 primary and 7 secondary plicae or folds. These plicae have hundreds of bursal follicles containing follicle-associated epithelial cells, lymphocytes, macrophages, and plasma cells. Lymphoid stem cells migrate from the fetal liver to the bursa during ontogeny. In the bursa, these stem cells acquire the characteristics of mature, immunocompetent B cells[WP]. The bursa is an organ found in birds involved in B cell differentiation[GO].", "definition_source": "UBERON", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0004177", "UBERON:0011510", "UBERON:0013765"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7474", "source_label": "Bursa of Fabricius", "source_path": "Host-associated &gt; Birds &gt; Lymphatic system &gt; Bursa of Fabricius", "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: EXACT."}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.f65007e88e for habitatmech:GOLD.dfef770cb8 (Host-associated &gt; Birds &gt; Lymphatic system &gt; Bursa of Fabricius). Review https://github.com/CultureBotAI/HabitatMech/issues/2198 : A component, derived sample fraction or distinct anatomical structure is not a subtype of this containing or neighboring source context. Exclude only this exact GOLD contribution; retain independent valid genera and source observations. This does not resolve C1 source scope or shared mapping endpoint #1398."}]} |
| EPREV | reviews/structured/20261015T193023Z-bursa_of_fabricius-record/review.yaml; Exact predecessor, all evidence and findings | supports | Baseline observation retained byte-identically; every finding is reconciled with identical target and issue-key scope. |
| ETEST | tests/test_buccal_camelid_caeca_review_repairs.py; Full-corpus counterfactual and public URL rendering | supports | Exactly sixteen targets change. All source IDs, paths, counts, units and taxa are preserved; only three rejected caecum predicates are removed. No unrelated records change. |
| EFIXTURE | tests/data/buccal_camelid_caeca_prior_decisions.json; Two loader-normalized earlier decisions | supports | Preserves earlier brown-algae and bacteriome effective fields, including explicit loader defaults, for the counterfactual; original row bytes remain in the baseline Git revision. |
| ERULE | docs/CURATION.md; Strict hierarchy, host identity, item decisions and provenance | supports | Context is not is-a; whole host labels are not exact environment aliases; unsupported ontology terms must not be substituted for source identity. |
| EHISTORY | history/README.md; Session history versus generated record audit trail | supports | Committed session files and reviews are append-only. Generated history is a separate projection; superseding current decisions does not overwrite the saved historical session. |
| EI16 | curation/gold_parent_exclusions.tsv; Exact keyed rows 6 | supports | [[6, "habitatmech:GOLD.dfef770cb8\tHost-associated &gt; Birds &gt; Lymphatic system &gt; Bursa of Fabricius\thabitatmech:GOLD.f65007e88e\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2198 : A component, derived sample fraction or distinct anatomical structure is not a subtype of this containing or neighboring source context. Exclude only this exact GOLD contribution; retain independent valid genera and source observations. This does not resolve C1 source scope or shared mapping endpoint #1398."]] |

## Limits And Additional Notes

- Original specimens and every pair-level source citation have not been independently reidentified. Source counts and ranks are not prevalence, viability, or characteristic presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities were separately checked against current NCBI Taxonomy, not certified by that label gate.
- iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic module or causal mechanism is asserted. No paid research was used.
- Same-agent adversarial review, not independent approval. Predecessor primary-source and specimen-level limits remain; no new prevalence, characteristic presence or causal mechanism is asserted.
- Shared mapping contract #1398 and current kg-microbe SSSOM/KGX compatibility remain outside this correction.
- Final-head checks must validate this new immutable successor; recorded full QC covers the exact repaired scientific input revision.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T201436Z-bursa_of_fabricius-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: bursa of Fabricius (UBERON:0003903)'
started_at: '2026-10-15T19:57:52Z'
finished_at: '2026-10-15T20:14:36Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the record and sources; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Removed only the exact GOLD context-parent contribution habitatmech:GOLD.f65007e88e.
  All source identifiers, paths, counts/units and taxa remain intact. No unresolved
  finding remains in this exact target scope; specimen-level limits still apply.
source:
  git_revision: 094ed0793c629eb7a9c279dc8ce9d26b642e11d8
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
    sha256: 490d3478aadc1dc3c4f04770d06db02fead4964d2e40ff339bfa389d46a5918a
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 12be4a7eccfcc6a9b9ef89fc1cb009e8f5e9ab87005bd6eb7ba93c910abf8f6d
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
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: a2a0496837ea75e487d7fc5d35317a890262a941d8fffe9babcd39f2f332c6db
    role: context
  - path: data/habitats/host_associated/bursa_of_fabricius.yaml
    sha256: cdf0f378251821be51ed50bc398eceb33e1f88f82b6eee9b9ab6fb980245547c
    role: target
  - path: data/habitats/host_associated/lymphatic_system__b7b64dca.yaml
    sha256: f193d3cdcebd83694a0c24f3c022441c1167dba11c876e84c7c78df5f723fa77
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
  - path: history/mappings/brown_algae/2026-10-15T194814Z-codex-gpt-5-1c7e43.yaml
    sha256: e58650e3a37c7cce2cf6aec0ef5ec91abf8355c6f0a3bde937aaa2910adf42d8
    role: context
  - path: history/mappings/brown_algae/2026-10-15T194825Z-codex-gpt-5-43fcaa.yaml
    sha256: 266340dbc008749095f682a10d3ce7fae0d147ab6c94046736d3de14c0841ef6
    role: context
  - path: history/mappings/buccal_camelid_caeca_review/2026-10-15T194811Z-codex-gpt-5-a1906b.yaml
    sha256: 8b45cceb2942bbd5a55549c4e30fcf7153348ad4366a47577883c8572769100b
    role: context
  - path: history/mappings/caeca/2026-10-15T194820Z-codex-gpt-5-79516a.yaml
    sha256: e838de6bc6e9ebbb214e83e710f4fd4d015460c99777639213c4aa966a847366
    role: context
  - path: history/mappings/caeca__67ed138d/2026-10-15T194822Z-codex-gpt-5-86d6f8.yaml
    sha256: 0043b78304be474ab023b01a15d898c8e268cb50a007185939773db820137452
    role: context
  - path: history/mappings/caeca_bacteriome/2026-10-15T194824Z-codex-gpt-5-563361.yaml
    sha256: 5b713fe134d059ccbf7696c2e2650f4d99b1b14a3ed88c1f23c07adace1fb72c
    role: context
  - path: history/mappings/canidae_dog/2026-10-15T194816Z-codex-gpt-5-753be4.yaml
    sha256: 3b5a0e886ce427adc35b009c813ddd69da1eeb36a89e6571efdf243756b7be62
    role: context
  - path: history/mappings/caprinae_sheep_goat/2026-10-15T194818Z-codex-gpt-5-349edb.yaml
    sha256: 5c822ec5df15502ccb006e0a752cf0f7431b633c56785a3a702cb166300ef878
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260929T214704Z-bursa_of_fabricius.md
    sha256: c8bdc8bc6142f33f0d096c908c0fe1a0983b1046c82b900392957414327ce4a2
    role: context
  - path: reviews/structured/20261015T193023Z-bursa_of_fabricius-record/review.yaml
    sha256: a79aa7ee398a9543f322b981e4d2f3a771b463b8054ed08687505ae7b95bb1e0
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
  - path: tests/data/buccal_camelid_caeca_prior_decisions.json
    sha256: d63a19ea91e38b91be200ae0a8aa32db911b60db0b5ae36c94c86b63414d8f16
    role: context
  - path: tests/test_buccal_camelid_caeca_review_repairs.py
    sha256: 53d33c91a46d655e426f1010454d52f40d3b4df132c1d35b59c65967b5d6ee78
    role: context
targets:
- target_id: UBERON:0003903
  path: data/habitats/host_associated/bursa_of_fabricius.yaml
  label: bursa of Fabricius
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
  description: Full regenerated target re-read and explicit disposition of every exact
    predecessor finding.
  selection: One of sixteen repaired targets in the twenty-four-record brown-algal
    through carcass cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0003903
  exclusions:
  - target: Other habitats and export compatibility
    reason: No whole-corpus scientific sign-off or SSSOM/KGX certification; source-evidence
      gaps remain separately scoped.
checks:
- check_id: C5
  name: just validate data/habitats/host_associated/bursa_of_fabricius.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/bursa_of_fabricius.yaml
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: "Executed 2026-10-15T19:50:02Z through 2026-10-15T19:50:06Z. No issues\
    \ found\n uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class\
    \ HabitatRecord data/habitats/host_associated/bursa_of_fabricius.yaml"
  scope_note: Ordinary schema for sixteen corrected targets; strict for all 24; other
    checks retain documented full-corpus scope.
- check_id: C16
  name: just validate-strict data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml
    data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml
    data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml
    data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml
    data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml
    data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml
    data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml
    data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml
    data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml
    data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml
    data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml
    data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml
    data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml
    data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml
    data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml
    data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml
    data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml
    data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml
    data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml
    data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml
    data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml
    data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml
    data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: "Executed 2026-10-15T19:50:41Z through 2026-10-15T19:50:52Z. uv run python\
    \ scripts/validate_strict.py data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml\
    \ data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml\
    \ data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml\
    \ data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml\
    \ data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml\
    \ data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml\
    \ data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml\
    \ data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml\
    \ data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml\
    \ data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml\
    \ data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml\
    \ data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for sixteen corrected targets; strict for all 24; other
    checks retain documented full-corpus scope.
- check_id: C17
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: 'Executed 2026-10-15T19:50:52Z through 2026-10-15T19:51:06Z. No issues
    found

    824 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for sixteen corrected targets; strict for all 24; other
    checks retain documented full-corpus scope.
- check_id: C18
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: "Executed 2026-10-15T19:51:06Z through 2026-10-15T19:51:07Z. provenance\
    \ current: 14 committed inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for sixteen corrected targets; strict for all 24; other
    checks retain documented full-corpus scope.
- check_id: C19
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: "Executed 2026-10-15T19:51:07Z through 2026-10-15T19:51:31Z. expected 3208\
    \ records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\
    \ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for sixteen corrected targets; strict for all 24; other
    checks retain documented full-corpus scope.
- check_id: C20
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: "Executed 2026-10-15T19:51:31Z through 2026-10-15T19:51:37Z. validated\
    \ 32 causal-graph curation file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for sixteen corrected targets; strict for all 24; other
    checks retain documented full-corpus scope.
- check_id: C21
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: "Executed 2026-10-15T19:51:37Z through 2026-10-15T19:52:00Z. term-request\
    \ table is current (110 terms)\n uv run python scripts/build_term_requests.py\
    \ --check"
  scope_note: Ordinary schema for sixteen corrected targets; strict for all 24; other
    checks retain documented full-corpus scope.
- check_id: C22
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: "Executed 2026-10-15T19:52:00Z through 2026-10-15T19:52:58Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n\
    \ uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for sixteen corrected targets; strict for all 24; other
    checks retain documented full-corpus scope.
- check_id: C23
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_buccal_camelid_caeca_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_buccal_camelid_caeca_review_repairs.py
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: 'Executed 2026-10-15T19:52:58Z through 2026-10-15T19:53:05Z. ..                                                                       [100%]

    2 passed in 6.03s'
  scope_note: Ordinary schema for sixteen corrected targets; strict for all 24; other
    checks retain documented full-corpus scope.
- check_id: C24
  name: git diff --check a073f8e821a7c095f35501982930cc5a156835c0
  status: passed
  required: true
  command: git diff --check a073f8e821a7c095f35501982930cc5a156835c0
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: 'Executed 2026-10-15T19:53:05Z through 2026-10-15T19:53:05Z. '
  scope_note: Ordinary schema for sixteen corrected targets; strict for all 24; other
    checks retain documented full-corpus scope.
- check_id: CCI
  name: Exact-revision full QC and structured archive contract
  status: passed
  required: true
  command: gh run view 38798112068 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - UBERON:0003903
  summary: Verified 2026-10-15T20:14:20Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38798112068
  scope_note: Exact repaired scientific input revision. Final-head checks remain mandatory
    for this new successor.
evidence:
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002465/graph
  locator: UBERON_0002465-graph.json
  accessed_at: '2026-10-15T19:06:31Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0002465",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002465",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_7711", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002465",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002193", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002465",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002405", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 2967b1474b746746ad9d7e14bb70599e4383b5222585f25f060e06d95862762e
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002465
  locator: UBERON_0002465.json
  accessed_at: '2026-10-15T19:06:30Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "UBERON:0002465", "label": "lymphoid system", "is_obsolete": false, "description":
    ["The lymphatic system in vertebrates is a network of conduits that carry a clear
    fluid called lymph. It also includes the lymphoid tissue through which the lymph
    travels. Lymphoid tissue is found in many organs, particularly the lymph nodes,
    and in the lymphoid follicles associated with the digestive system such as the
    tonsils. The system also includes all the structures dedicated to the circulation
    and production of lymphocytes, which includes the spleen, thymus, bone marrow
    and the lymphoid tissue associated with the digestive system[WP]."]}'
  snapshot_sha256: 630064766c5a885ad2000996260b0773ba24ed1e00503468ce48f8088f145093
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0003903/graph
  locator: UBERON_0003903-graph.json
  accessed_at: '2026-10-15T19:06:33Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0003903",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004177", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003903",
    "target": "http://purl.obolibrary.org/obo/UBERON_0011510", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003903",
    "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003903",
    "target": "http://purl.obolibrary.org/obo/GO_0030097", "uri": "http://purl.obolibrary.org/obo/BFO_0000067",
    "label": "contains process"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003903",
    "target": "http://purl.obolibrary.org/obo/GO_0030183", "uri": "http://purl.obolibrary.org/obo/BFO_0000067",
    "label": "contains process"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003903",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_8457", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}]'
  snapshot_sha256: 47f68e10222b029a7889e4a488cf44a080e501e20b4484dd45f94c18c2f70997
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0003903
  locator: UBERON_0003903.json
  accessed_at: '2026-10-15T19:06:32Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "UBERON:0003903", "label": "bursa of Fabricius", "is_obsolete": false, "description":
    ["An epithelial and lymphoid organ that develops as a dorsal diverticulum of the
    proctodeal region of the cloaca in birds. The luminal (interior) surface of the
    bursa is plicated with as many as 15 primary and 7 secondary plicae or folds.
    These plicae have hundreds of bursal follicles containing follicle-associated
    epithelial cells, lymphocytes, macrophages, and plasma cells. Lymphoid stem cells
    migrate from the fetal liver to the bursa during ontogeny. In the bursa, these
    stem cells acquire the characteristics of mature, immunocompetent B cells[WP].
    The bursa is an organ found in birds involved in B cell differentiation[GO]."]}'
  snapshot_sha256: 2b41b9b122880bfee0b6bbe28de3ef1760ea708ef554b677c53374688a5ee089
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0004177/graph
  locator: UBERON_0004177-graph.json
  accessed_at: '2026-10-15T19:06:34Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0004177",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000062", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0004177",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002390", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: c99bd2bb8820d6c222135a59267170638c6bb58f943d0248cb27b8335532de4d
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0004177
  locator: UBERON_0004177.json
  accessed_at: '2026-10-15T19:06:33Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "UBERON:0004177", "label": "hemopoietic organ", "is_obsolete": false, "description":
    ["Organ that is part of the hematopoietic system."]}'
  snapshot_sha256: ab8de78589f433728c9c7a5ee5ae328b71bbfaeb1477d9df673b583a3831bd54
- evidence_id: EX7
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0011510/graph
  locator: UBERON_0011510-graph.json
  accessed_at: '2026-10-15T19:06:40Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0011510",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000063", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0011510",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000162", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: d0a796998ae64b83bfeb7316a15d9bfd0b5a10d51c7ea582489f3e2fe26320bd
- evidence_id: EX8
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0011510
  locator: UBERON_0011510.json
  accessed_at: '2026-10-15T19:06:39Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "UBERON:0011510", "label": "cloacal bursa", "is_obsolete": false, "description":
    ["Taxon notes: in cryptodires, bursae apparently function primarily in buoyancy
    control and secondarily in ion transport and nesting, but several pleurodires
    have been shown recently to use them in aquatic respiration.[PMID:11479904]",
    "An evagination of the cloaca. In Testudines these are hypothesized to function
    in different physiological roles, primarily in respiration."]}'
  snapshot_sha256: 8f8ddca92b6c67674eff431caf90713e32f1588526e75f78bf1181c322113ac0
- evidence_id: EX9
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0013765/graph
  locator: UBERON_0013765-graph.json
  accessed_at: '2026-10-15T19:06:41Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0013765",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000062", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0013765",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001007", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 323f973710161da936919e1298481f5c543072d9b76d9b2b34d70cbd48c46493
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0013765
  locator: UBERON_0013765.json
  accessed_at: '2026-10-15T19:06:40Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "UBERON:0013765", "label": "digestive system element", "is_obsolete": false, "description":
    ["Any of the organs or elements that are part of the digestive system. Examples:
    tongue, esophagus, spleen, crop, lunge feeding organ, tooth elements."]}'
  snapshot_sha256: 551bea3988ac4ce59b0f1e27373c0788895265f63fa9c6e6fd95a17bc435c219
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/bursa_of_fabricius.yaml
  locator: Entire regenerated target
  accessed_at: '2026-10-15T20:14:36Z'
  support: supports
  summary: '{"identifier": "UBERON:0003903", "label": "bursa of Fabricius", "definition":
    "An epithelial and lymphoid organ that develops as a dorsal diverticulum of the
    proctodeal region of the cloaca in birds. The luminal (interior) surface of the
    bursa is plicated with as many as 15 primary and 7 secondary plicae or folds.
    These plicae have hundreds of bursal follicles containing follicle-associated
    epithelial cells, lymphocytes, macrophages, and plasma cells. Lymphoid stem cells
    migrate from the fetal liver to the bursa during ontogeny. In the bursa, these
    stem cells acquire the characteristics of mature, immunocompetent B cells[WP].
    The bursa is an organ found in birds involved in B cell differentiation[GO].",
    "definition_source": "UBERON", "habitat_category": "HOST_ASSOCIATED", "grounding_status":
    "EXACT", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0004177", "UBERON:0011510",
    "UBERON:0013765"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7474",
    "source_label": "Bursa of Fabricius", "source_path": "Host-associated > Birds
    > Lymphatic system > Bursa of Fabricius", "mapping_predicate": "skos:exactMatch",
    "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by GOLD. Grounding: EXACT."}, {"timestamp": "2026-10-15T00:00:00Z", "curator":
    "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path
    parent contribution habitatmech:GOLD.f65007e88e for habitatmech:GOLD.dfef770cb8
    (Host-associated > Birds > Lymphatic system > Bursa of Fabricius). Review https://github.com/CultureBotAI/HabitatMech/issues/2198
    : A component, derived sample fraction or distinct anatomical structure is not
    a subtype of this containing or neighboring source context. Exclude only this
    exact GOLD contribution; retain independent valid genera and source observations.
    This does not resolve C1 source scope or shared mapping endpoint #1398."}]}'
  snapshot_sha256: cdf0f378251821be51ed50bc398eceb33e1f88f82b6eee9b9ab6fb980245547c
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T193023Z-bursa_of_fabricius-record/review.yaml
  locator: Exact predecessor, all evidence and findings
  accessed_at: '2026-10-15T20:14:36Z'
  support: supports
  summary: Baseline observation retained byte-identically; every finding is reconciled
    with identical target and issue-key scope.
  snapshot_sha256: a79aa7ee398a9543f322b981e4d2f3a771b463b8054ed08687505ae7b95bb1e0
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_buccal_camelid_caeca_review_repairs.py
  locator: Full-corpus counterfactual and public URL rendering
  accessed_at: '2026-10-15T20:14:36Z'
  support: supports
  summary: Exactly sixteen targets change. All source IDs, paths, counts, units and
    taxa are preserved; only three rejected caecum predicates are removed. No unrelated
    records change.
  snapshot_sha256: 53d33c91a46d655e426f1010454d52f40d3b4df132c1d35b59c65967b5d6ee78
- evidence_id: EFIXTURE
  kind: record_content
  reference: tests/data/buccal_camelid_caeca_prior_decisions.json
  locator: Two loader-normalized earlier decisions
  accessed_at: '2026-10-15T20:14:36Z'
  support: supports
  summary: Preserves earlier brown-algae and bacteriome effective fields, including
    explicit loader defaults, for the counterfactual; original row bytes remain in
    the baseline Git revision.
  snapshot_sha256: d63a19ea91e38b91be200ae0a8aa32db911b60db0b5ae36c94c86b63414d8f16
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict hierarchy, host identity, item decisions and provenance
  accessed_at: '2026-10-15T20:14:36Z'
  support: supports
  summary: Context is not is-a; whole host labels are not exact environment aliases;
    unsupported ontology terms must not be substituted for source identity.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EHISTORY
  kind: authority
  reference: history/README.md
  locator: Session history versus generated record audit trail
  accessed_at: '2026-10-15T20:14:36Z'
  support: supports
  summary: Committed session files and reviews are append-only. Generated history
    is a separate projection; superseding current decisions does not overwrite the
    saved historical session.
  snapshot_sha256: 819361a711697f96ff9c1aa0b27e94302547970b3b54777d67ec1449db5e543a
- evidence_id: EI16
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact keyed rows 6
  accessed_at: '2026-10-15T20:14:36Z'
  support: supports
  summary: '[[6, "habitatmech:GOLD.dfef770cb8\tHost-associated > Birds > Lymphatic
    system > Bursa of Fabricius\thabitatmech:GOLD.f65007e88e\tcodex-gpt-5\t2026-10-15\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2198 : A component, derived
    sample fraction or distinct anatomical structure is not a subtype of this containing
    or neighboring source context. Exclude only this exact GOLD contribution; retain
    independent valid genera and source observations. This does not resolve C1 source
    scope or shared mapping endpoint #1398."]]'
  snapshot_sha256: 12be4a7eccfcc6a9b9ef89fc1cb009e8f5e9ab87005bd6eb7ba93c910abf8f6d
assessments:
- assessment_id: A1
  area: consistency
  topic: Correction and preservation
  outcome: supported
  summary: Removed only the exact GOLD context-parent contribution habitatmech:GOLD.f65007e88e.
    All source identifiers, paths, counts/units and taxa remain intact. No unresolved
    finding remains in this exact target scope; specimen-level limits still apply.
  target_ids:
  - UBERON:0003903
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EAFTER
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI16
- assessment_id: A2
  area: identity
  topic: Current identity, definition and ancestry
  outcome: supported
  summary: 'Current target: bursa of Fabricius (UBERON:0003903), EXACT/SEEDED. Parents:
    ["UBERON:0004177", "UBERON:0011510", "UBERON:0013765"]. The unchanged source identity
    remains distinct; no replacement genus or merge is inferred.'
  target_ids:
  - UBERON:0003903
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EAFTER
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI16
  dimensions:
  - name: native_status
    value: EXACT/SEEDED
    definition: Native generated grounding and curation state, distinct from this
      scientific verdict.
    evidence_ids:
    - EAFTER
    - ERULE
- assessment_id: A3
  area: quantity
  topic: Frozen source assertions and taxa
  outcome: supported
  summary: 'All source IDs, paths, counts/units, taxon IDs, labels, ranks and scores
    are unchanged. Current attestations: [{"source": "GOLD", "source_id": "gold.ecosystem:7474",
    "source_label": "Bursa of Fabricius", "source_path": "Host-associated > Birds
    > Lymphatic system > Bursa of Fabricius", "mapping_predicate": "skos:exactMatch",
    "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}].
    Three caecal targets alone lose unsupported mapping_predicate after explicit ITEM
    reassessment; zero omissions and independent source units remain distinct.'
  target_ids:
  - UBERON:0003903
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EAFTER
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI16
  dimensions:
  - name: source_assertion_units
    value: '[{"source": "GOLD", "assertion_count": null, "assertion_unit": null}]'
    definition: Source-specific noninterchangeable assertion units; omitted zero counts
      retain their baseline source verification.
    evidence_ids:
    - EAFTER
    - EPREV
    - ETEST
- assessment_id: A4
  area: representation
  topic: Remaining scoped findings
  outcome: supported
  summary: 'Every predecessor issue key and exact target scope is preserved. A resolved
    local caecum mapping witness does not close the shared #1398 contract; unresolved
    original PREGO evidence and category-policy questions are not decided by this
    repair.'
  target_ids:
  - UBERON:0003903
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EAFTER
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI16
findings:
- finding_id: F1
  issue_key: bursa-of-fabricius-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: GOLD context is not a broader habitat class
  description: Corrected through the maintained input and native regeneration. Removed
    only the exact GOLD context-parent contribution habitatmech:GOLD.f65007e88e.
  target_ids:
  - UBERON:0003903
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EAFTER
  - EPREV
  - ETEST
  - EFIXTURE
  - ERULE
  - EHISTORY
  - EI16
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2198
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T193023Z-bursa_of_fabricius-record
    finding_id: F1
  disposition_reason: Removed only the exact GOLD context-parent contribution habitatmech:GOLD.f65007e88e.
actions: []
limitations:
- Original specimens and every pair-level source citation have not been independently
  reidentified. Source counts and ranks are not prevalence, viability, or characteristic
  presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities
  were separately checked against current NCBI Taxonomy, not certified by that label
  gate.
- 'iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic
  module or causal mechanism is asserted. No paid research was used.'
- Same-agent adversarial review, not independent approval. Predecessor primary-source
  and specimen-level limits remain; no new prevalence, characteristic presence or
  causal mechanism is asserted.
- 'Shared mapping contract #1398 and current kg-microbe SSSOM/KGX compatibility remain
  outside this correction.'
- Final-head checks must validate this new immutable successor; recorded full QC covers
  the exact repaired scientific input revision.
notes: []
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T193023Z-bursa_of_fabricius-record
  relationship: Exact predecessor; every finding is explicitly reconciled.
```
