# Remediation review: cibarium_preoral_cavity

- Review: 20261016T024243Z-cibarium_preoral_cavity-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T02:31:08Z
- Finished UTC: 2026-10-16T02:42:43Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed only the reviewed GOLD context-parent contribution habitatmech:GOLD.bd1664969c. Preserved source identity, observations, counts/units, native status and all independent genera. No unresolved predecessor finding remains in this target scope.

## Scope And Provenance

Full current-record assessment and explicit disposition of every predecessor finding after guarded parent repair.

Selection: One of six corrected targets from the 24-record cervical-through-circulatory cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2f083c50037e54913a1b131dec213c5084002dcd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.5a9d059298 | data/habitats/host_associated/cibarium_preoral_cavity.yaml | generated | Cibarium/Preoral cavity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/cibarium_preoral_cavity.yaml | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:17:53Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cibarium_preoral_cavity.yaml |
| just validate-strict data/habitats/host_associated/cervical_cancer.yaml data/habitats/host_associated/cervical_neck_nodes.yaml data/habitats/host_associated/cervix.yaml data/habitats/host_associated/cervix__0de03fa8.yaml data/habitats/host_associated/chago_k_1_cell.yaml data/habitats/host_associated/cho.yaml data/habitats/host_associated/choanomastigote.yaml data/habitats/host_associated/cholesteatoma_tissue.yaml data/habitats/host_associated/chorionic_villi.yaml data/habitats/host_associated/chorionic_villi__9af464db.yaml data/habitats/host_associated/chyme.yaml data/habitats/host_associated/chyme__0bfd2730.yaml data/habitats/host_associated/cibarium_preoral_cavity.yaml data/habitats/host_associated/ciliates.yaml data/habitats/host_associated/ciliates__df51eda4.yaml data/habitats/host_associated/ciliophora.yaml data/habitats/host_associated/circulatory_system.yaml data/habitats/host_associated/circulatory_system__241de4de.yaml data/habitats/host_associated/circulatory_system__5b3debaf.yaml data/habitats/host_associated/circulatory_system__745592ee.yaml data/habitats/host_associated/circulatory_system__7e4ecb0e.yaml data/habitats/host_associated/circulatory_system__90d88932.yaml data/habitats/host_associated/circulatory_system__e49da8a0.yaml data/habitats/host_associated/circulatory_system__f5b69d9c.yaml | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:18:03Z. uv run python scripts/validate_strict.py data/habitats/host_associated/cervical_cancer.yaml data/habitats/host_associated/cervical_neck_nodes.yaml data/habitats/host_associated/cervix.yaml data/habitats/host_associated/cervix__0de03fa8.yaml data/habitats/host_associated/chago_k_1_cell.yaml data/habitats/host_associated/cho.yaml data/habitats/host_associated/choanomastigote.yaml data/habitats/host_associated/cholesteatoma_tissue.yaml data/habitats/host_associated/chorionic_villi.yaml data/habitats/host_associated/chorionic_villi__9af464db.yaml data/habitats/host_associated/chyme.yaml data/habitats/host_associated/chyme__0bfd2730.yaml data/habitats/host_associated/cibarium_preoral_cavity.yaml data/habitats/host_associated/ciliates.yaml data/habitats/host_associated/ciliates__df51eda4.yaml data/habitats/host_associated/ciliophora.yaml data/habitats/host_associated/circulatory_system.yaml data/habitats/host_associated/circulatory_system__241de4de.yaml data/habitats/host_associated/circulatory_system__5b3debaf.yaml data/habitats/host_associated/circulatory_system__745592ee.yaml data/habitats/host_associated/circulatory_system__7e4ecb0e.yaml data/habitats/host_associated/circulatory_system__90d88932.yaml data/habitats/host_associated/circulatory_system__e49da8a0.yaml data/habitats/host_associated/circulatory_system__f5b69d9c.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:18:15Z. No issues found<br>831 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:18:16Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:18:38Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:18:44Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:19:07Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:20:10Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_cervix_chyme_review_repairs.py | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:20:21Z. ..                                                                       [100%]<br>2 passed in 9.14s |
| git diff --check 5fef9bb871a510550a3f70c45118805ac7c8d9a8 | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:20:21Z.  |
| Exact-revision hosted archive contract | passed | True | habitatmech:GOLD.5a9d059298 | Verified successful Validate structured review contract step at 2026-10-16T02:42:35Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38840830342 |
| just redirects | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:25:14Z. wrote data/habitats/RETIRED.tsv: 259 redirect(s)<br>  label_changed              107<br>  source_concepts_merged     148<br>  source_concepts_split      4<br> uv run python scripts/build_redirects.py |
| just render | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:26:01Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 129 term requests -&gt; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages<br> uv run python scripts/render_pages.py |
| just docs-stats | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:26:23Z. updated README corpus statistics<br> uv run python scripts/check_docs.py --write |
| just redirects-check | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:29:11Z. RETIRED.tsv is current (259 redirects)<br> uv run python scripts/build_redirects.py --check |
| just render-check | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:30:06Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 129 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpasmttfoz/site<br>pages/ is in step with the corpus<br> uv run python scripts/render_pages.py --check |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m ruff check . | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:30:07Z. All checks passed! |
| git diff --check 5fef9bb871a510550a3f70c45118805ac7c8d9a8 | passed | True | habitatmech:GOLD.5a9d059298 | Finished 2026-10-16T02:30:08Z.  |
| Standalone citation validator applicability | not_applicable | False | habitatmech:GOLD.5a9d059298 | No standalone citation checker documented for evidence-free generated targets. Stable references checked with native gates/current authorities; causal validation ran globally. |

## Scientific And Domain Assessments

### Bounded repair and field preservation

consistency: supported. Targets: habitatmech:GOLD.5a9d059298.

Removed only the reviewed GOLD context-parent contribution habitatmech:GOLD.bd1664969c. Preserved source identity, observations, counts/units, native status and all independent genera. No unresolved predecessor finding remains in this target scope.

### Current identity and strict ancestry

identity: supported. Targets: habitatmech:GOLD.5a9d059298.

habitatmech:GOLD.5a9d059298: Cibarium/Preoral cavity; UNGROUNDED/SEEDED; parents []. No replacement genus or optional definition invented. Original primary-source assessments remain bounded to the claims in EPREV.

### Nonadditive frozen evidence

quantity: supported. Targets: habitatmech:GOLD.5a9d059298.

[{"source": "GOLD", "source_id": "gold.ecosystem:7386", "source_label": "Cibarium/Preoral cavity", "source_path": "Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Foregut &gt; Cibarium/Preoral cavity"}]. Counterfactual comparison preserves entire source and taxon fields.

### Every predecessor finding reconciled

representation: supported. Targets: habitatmech:GOLD.5a9d059298.

All issue keys, targets and exact predecessors retained. Parent repair does not certify mapping endpoints or SSSOM/KGX.

### Optional claims and remaining uncertainty

completeness: supported. Targets: habitatmech:GOLD.5a9d059298.

No parameters, mechanisms or characteristic-presence claims added. Counts are not prevalence or biological absence.

## Findings

### F1: Source context is not a broader habitat class

major / resolved / confirmed; issue key: cibarium-preoral-cavity-context-parent.

Excluded only exact guarded GOLD contribution habitatmech:GOLD.bd1664969c. Independent genera and every other scientific field remain unchanged.

Disposition: Excluded only exact guarded GOLD contribution habitatmech:GOLD.bd1664969c. Independent genera and every other scientific field remain unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4153580/fullTextXML; PMC4153580.xml | context_only | PMID:25184624; DOI:10.1371/journal.pone.0106215. Anatomy, dissection methods and discussion inspected. Cibarium and precibarium are components of the functional foregut; dissections from 96 insects were sequenced. Authors caution that some detections may reflect contamination and do not prove attached residence. Used only for compartment identity and bounded habitat context. |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001041/graph; UBERON_0001041-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001041", "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001041; UBERON_0001041.json | context_only | Current term identity, active status and definition: {"obo_id": "UBERON:0001041", "label": "foregut", "is_obsolete": false, "description": ["Anterior subdivision of a digestive tract."]} |
| EAFTER | data/habitats/host_associated/cibarium_preoral_cavity.yaml; Full regenerated YAML | supports | {"identifier": "habitatmech:GOLD.5a9d059298", "label": "Cibarium/Preoral cavity", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "SEEDED", "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7386", "source_label": "Cibarium/Preoral cavity", "source_path": "Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Foregut &gt; Cibarium/Preoral cavity"}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. [CLASS-level] Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate. (source concept habitatmech:GOLD.5a9d059298)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.bd1664969c for habitatmech:GOLD.5a9d059298 (Host-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Foregut &gt; Cibarium/Preoral cavity). Review https://github.com/CultureBotAI/HabitatMech/issues/2217 : The insect cibarium/preoral-cavity source names a compartment, not a type of complete foregut. Primary sharpshooter dissection separates cibarium and precibarium within the functional anterior foregut and studies their microbial context. This supports physical habitat meaning and a part/whole distinction, not the identity of any GOLD specimen or universal residence of all sequenced taxa. Remove only the whole-foregut source parent. Exclude only this exact GOLD contribution; preserve all independent genera, source observations and native status. Shared mapping endpoints #1398 remain unresolved."}]} |
| EPREV | reviews/structured/20261016T021308Z-cibarium_preoral_cavity-record/review.yaml; Exact immutable predecessor and every finding | supports | Original observation unchanged; exact issue keys and lineage retained. |
| ETEST | tests/test_cervix_chyme_review_repairs.py; Whole-corpus counterfactual regression | supports | Exactly six documents change, only parent_habitats and appended audit event; all identities, counts, units, source paths, aliases, taxa, statuses and other records are identical. |
| ERULE | docs/CURATION.md; Strict broader hierarchy | supports | Containment and source grouping do not imply is-a. |
| EHISTORY | history/mappings/cervix_chyme_review/2026-10-16T021625Z-codex-gpt-5-9b4900.yaml; Complete immutable session event | supports | Actor codex-gpt-5, model gpt-5, tool codex; six guarded parent repairs under #2217. |
| EINPUT | curation/gold_parent_exclusions.tsv; Exact guarded source row | supports | [[7, "habitatmech:GOLD.5a9d059298\tHost-associated &gt; Arthropoda: Insects &gt; Digestive system &gt; Foregut &gt; Cibarium/Preoral cavity\thabitatmech:GOLD.bd1664969c\tcodex-gpt-5\t2026-10-16\tReview https://github.com/CultureBotAI/HabitatMech/issues/2217 : The insect cibarium/preoral-cavity source names a compartment, not a type of complete foregut. Primary sharpshooter dissection separates cibarium and precibarium within the functional anterior foregut and studies their microbial context. This supports physical habitat meaning and a part/whole distinction, not the identity of any GOLD specimen or universal residence of all sequenced taxa. Remove only the whole-foregut source parent. Exclude only this exact GOLD contribution; preserve all independent genera, source observations and native status. Shared mapping endpoints #1398 remain unresolved."]] |

## Limits And Additional Notes

- Source counts, score channels and ranks do not establish prevalence, viability or characteristic presence. Original specimen-level and pair-level evidence has not been reconstructed exhaustively.
- Configured label validation skipped 2063 no-adapter pairs; displayed target TaxIds were resolved separately with current NCBI.
- iModulonDB is not applicable: target claims do not assert genes, regulators or expression modules. No paid research or native status promotion.
- Same-agent assessment, not independent approval. The exact-base hosted archive contract passed, but its full quality gate was still running at capture. Native scientific and product gates passed. Final-head and merge-queue quality checks remain required before merge.
- Native working-tree capture retained; the off-main base will be preserved by an annotated provenance tag before branch deletion.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T024243Z-cibarium_preoral_cavity-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: cibarium_preoral_cavity'
started_at: '2026-10-16T02:31:08Z'
finished_at: '2026-10-16T02:42:43Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assessed sources and target; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Removed only the reviewed GOLD context-parent contribution habitatmech:GOLD.bd1664969c.
  Preserved source identity, observations, counts/units, native status and all independent
  genera. No unresolved predecessor finding remains in this target scope.
source:
  git_revision: 2f083c50037e54913a1b131dec213c5084002dcd
  state: working_tree
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
    sha256: 04ba048af6f93b69c127bc3d47e2403dbe153452c75f9e26939188fc5daa52d7
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
  - path: data/habitats/host_associated/cibarium_preoral_cavity.yaml
    sha256: 815a5e0f796892a16e0d48f1438f72fd6d858716e4fca0fe0f6ddba713a331f3
    role: target
  - path: data/habitats/host_associated/foregut__ce63e8ab.yaml
    sha256: c2e259b437506873d31f861f1ab6b3172a320578aab5a3dfeebc16f9c710860c
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
  - path: history/mappings/cervix_chyme_review/2026-10-16T021625Z-codex-gpt-5-9b4900.yaml
    sha256: 5c5e778a351aa79a87968b5b305a660ea3b49cc5de8cbc7e0ab8232dffc14483
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261016T021308Z-cibarium_preoral_cavity-record/review.yaml
    sha256: dc3d159417c54abd481ec0e0ba3fc68b4a5bc04df64b245b3333a0e73b7c4ab7
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
  - path: tests/test_cervix_chyme_review_repairs.py
    sha256: 6c5278c50f78c6abebdc9bc78e777be71a83b42e559cd1f55c201e1c881aaabd
    role: context
targets:
- target_id: habitatmech:GOLD.5a9d059298
  path: data/habitats/host_associated/cibarium_preoral_cavity.yaml
  label: Cibarium/Preoral cavity
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
  description: Full current-record assessment and explicit disposition of every predecessor
    finding after guarded parent repair.
  selection: One of six corrected targets from the 24-record cervical-through-circulatory
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.5a9d059298
  exclusions:
  - target: Other records and SSSOM/KGX conformance
    reason: No whole-corpus scientific approval or mapping-contract certification.
checks:
- check_id: C5
  name: just validate data/habitats/host_associated/cibarium_preoral_cavity.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/cibarium_preoral_cavity.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:17:53Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cibarium_preoral_cavity.yaml"
  scope_note: Target schema; cohort strict; other gates retain documented full-corpus
    scope.
- check_id: C6
  name: just validate-strict data/habitats/host_associated/cervical_cancer.yaml data/habitats/host_associated/cervical_neck_nodes.yaml
    data/habitats/host_associated/cervix.yaml data/habitats/host_associated/cervix__0de03fa8.yaml
    data/habitats/host_associated/chago_k_1_cell.yaml data/habitats/host_associated/cho.yaml
    data/habitats/host_associated/choanomastigote.yaml data/habitats/host_associated/cholesteatoma_tissue.yaml
    data/habitats/host_associated/chorionic_villi.yaml data/habitats/host_associated/chorionic_villi__9af464db.yaml
    data/habitats/host_associated/chyme.yaml data/habitats/host_associated/chyme__0bfd2730.yaml
    data/habitats/host_associated/cibarium_preoral_cavity.yaml data/habitats/host_associated/ciliates.yaml
    data/habitats/host_associated/ciliates__df51eda4.yaml data/habitats/host_associated/ciliophora.yaml
    data/habitats/host_associated/circulatory_system.yaml data/habitats/host_associated/circulatory_system__241de4de.yaml
    data/habitats/host_associated/circulatory_system__5b3debaf.yaml data/habitats/host_associated/circulatory_system__745592ee.yaml
    data/habitats/host_associated/circulatory_system__7e4ecb0e.yaml data/habitats/host_associated/circulatory_system__90d88932.yaml
    data/habitats/host_associated/circulatory_system__e49da8a0.yaml data/habitats/host_associated/circulatory_system__f5b69d9c.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/cervical_cancer.yaml
    data/habitats/host_associated/cervical_neck_nodes.yaml data/habitats/host_associated/cervix.yaml
    data/habitats/host_associated/cervix__0de03fa8.yaml data/habitats/host_associated/chago_k_1_cell.yaml
    data/habitats/host_associated/cho.yaml data/habitats/host_associated/choanomastigote.yaml
    data/habitats/host_associated/cholesteatoma_tissue.yaml data/habitats/host_associated/chorionic_villi.yaml
    data/habitats/host_associated/chorionic_villi__9af464db.yaml data/habitats/host_associated/chyme.yaml
    data/habitats/host_associated/chyme__0bfd2730.yaml data/habitats/host_associated/cibarium_preoral_cavity.yaml
    data/habitats/host_associated/ciliates.yaml data/habitats/host_associated/ciliates__df51eda4.yaml
    data/habitats/host_associated/ciliophora.yaml data/habitats/host_associated/circulatory_system.yaml
    data/habitats/host_associated/circulatory_system__241de4de.yaml data/habitats/host_associated/circulatory_system__5b3debaf.yaml
    data/habitats/host_associated/circulatory_system__745592ee.yaml data/habitats/host_associated/circulatory_system__7e4ecb0e.yaml
    data/habitats/host_associated/circulatory_system__90d88932.yaml data/habitats/host_associated/circulatory_system__e49da8a0.yaml
    data/habitats/host_associated/circulatory_system__f5b69d9c.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:18:03Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/cervical_cancer.yaml data/habitats/host_associated/cervical_neck_nodes.yaml\
    \ data/habitats/host_associated/cervix.yaml data/habitats/host_associated/cervix__0de03fa8.yaml\
    \ data/habitats/host_associated/chago_k_1_cell.yaml data/habitats/host_associated/cho.yaml\
    \ data/habitats/host_associated/choanomastigote.yaml data/habitats/host_associated/cholesteatoma_tissue.yaml\
    \ data/habitats/host_associated/chorionic_villi.yaml data/habitats/host_associated/chorionic_villi__9af464db.yaml\
    \ data/habitats/host_associated/chyme.yaml data/habitats/host_associated/chyme__0bfd2730.yaml\
    \ data/habitats/host_associated/cibarium_preoral_cavity.yaml data/habitats/host_associated/ciliates.yaml\
    \ data/habitats/host_associated/ciliates__df51eda4.yaml data/habitats/host_associated/ciliophora.yaml\
    \ data/habitats/host_associated/circulatory_system.yaml data/habitats/host_associated/circulatory_system__241de4de.yaml\
    \ data/habitats/host_associated/circulatory_system__5b3debaf.yaml data/habitats/host_associated/circulatory_system__745592ee.yaml\
    \ data/habitats/host_associated/circulatory_system__7e4ecb0e.yaml data/habitats/host_associated/circulatory_system__90d88932.yaml\
    \ data/habitats/host_associated/circulatory_system__e49da8a0.yaml data/habitats/host_associated/circulatory_system__f5b69d9c.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Target schema; cohort strict; other gates retain documented full-corpus
    scope.
- check_id: C7
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: 'Finished 2026-10-16T02:18:15Z. No issues found

    831 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Target schema; cohort strict; other gates retain documented full-corpus
    scope.
- check_id: C8
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:18:16Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Target schema; cohort strict; other gates retain documented full-corpus
    scope.
- check_id: C9
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:18:38Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Target schema; cohort strict; other gates retain documented full-corpus
    scope.
- check_id: C10
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:18:44Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Target schema; cohort strict; other gates retain documented full-corpus
    scope.
- check_id: C11
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:19:07Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Target schema; cohort strict; other gates retain documented full-corpus
    scope.
- check_id: C12
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:20:10Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Target schema; cohort strict; other gates retain documented full-corpus
    scope.
- check_id: C13
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_cervix_chyme_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_cervix_chyme_review_repairs.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: 'Finished 2026-10-16T02:20:21Z. ..                                                                       [100%]

    2 passed in 9.14s'
  scope_note: Target schema; cohort strict; other gates retain documented full-corpus
    scope.
- check_id: C14
  name: git diff --check 5fef9bb871a510550a3f70c45118805ac7c8d9a8
  status: passed
  required: true
  command: git diff --check 5fef9bb871a510550a3f70c45118805ac7c8d9a8
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: 'Finished 2026-10-16T02:20:21Z. '
  scope_note: Target schema; cohort strict; other gates retain documented full-corpus
    scope.
- check_id: CCI
  name: Exact-revision hosted archive contract
  status: passed
  required: true
  command: gh run view 38840830342 --repo CultureBotAI/HabitatMech --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: Verified successful Validate structured review contract step at 2026-10-16T02:42:35Z
    https://github.com/CultureBotAI/HabitatMech/actions/runs/38840830342
  scope_note: Only the completed archive-contract step is claimed. The full hosted
    quality gate was still running at capture; final-head and merge-queue validation
    remain required.
- check_id: CPRODUCT0
  name: just redirects
  status: passed
  required: true
  command: just redirects
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:25:14Z. wrote data/habitats/RETIRED.tsv: 259 redirect(s)\n\
    \  label_changed              107\n  source_concepts_merged     148\n  source_concepts_split\
    \      4\n uv run python scripts/build_redirects.py"
  scope_note: Native product generation, reproducibility and lint for the repaired
    corpus.
- check_id: CPRODUCT1
  name: just render
  status: passed
  required: true
  command: just render
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:26:01Z. rendered 3209 habitat pages, 259 redirect\
    \ stubs, 8 categories, 129 term requests -> /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages\n\
    \ uv run python scripts/render_pages.py"
  scope_note: Native product generation, reproducibility and lint for the repaired
    corpus.
- check_id: CPRODUCT2
  name: just docs-stats
  status: passed
  required: true
  command: just docs-stats
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:26:23Z. updated README corpus statistics\n uv run\
    \ python scripts/check_docs.py --write"
  scope_note: Native product generation, reproducibility and lint for the repaired
    corpus.
- check_id: CPRODUCT3
  name: just redirects-check
  status: passed
  required: true
  command: just redirects-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:29:11Z. RETIRED.tsv is current (259 redirects)\n\
    \ uv run python scripts/build_redirects.py --check"
  scope_note: Native product generation, reproducibility and lint for the repaired
    corpus.
- check_id: CPRODUCT4
  name: just render-check
  status: passed
  required: true
  command: just render-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: "Finished 2026-10-16T02:30:06Z. rendered 3209 habitat pages, 259 redirect\
    \ stubs, 8 categories, 129 term requests -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpasmttfoz/site\n\
    pages/ is in step with the corpus\n uv run python scripts/render_pages.py --check"
  scope_note: Native product generation, reproducibility and lint for the repaired
    corpus.
- check_id: CPRODUCT5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff check .
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: Finished 2026-10-16T02:30:07Z. All checks passed!
  scope_note: Native product generation, reproducibility and lint for the repaired
    corpus.
- check_id: CPRODUCT6
  name: git diff --check 5fef9bb871a510550a3f70c45118805ac7c8d9a8
  status: passed
  required: true
  command: git diff --check 5fef9bb871a510550a3f70c45118805ac7c8d9a8
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: 'Finished 2026-10-16T02:30:08Z. '
  scope_note: Native product generation, reproducibility and lint for the repaired
    corpus.
- check_id: CREF
  name: Standalone citation validator applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.5a9d059298
  summary: No standalone citation checker documented for evidence-free generated targets.
    Stable references checked with native gates/current authorities; causal validation
    ran globally.
  scope_note: No invented command or exit code.
evidence:
- evidence_id: EX1
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4153580/fullTextXML
  locator: PMC4153580.xml
  accessed_at: '2026-10-16T02:10:54Z'
  support: context_only
  summary: PMID:25184624; DOI:10.1371/journal.pone.0106215. Anatomy, dissection methods
    and discussion inspected. Cibarium and precibarium are components of the functional
    foregut; dissections from 96 insects were sequenced. Authors caution that some
    detections may reflect contamination and do not prove attached residence. Used
    only for compartment identity and bounded habitat context.
  snapshot_sha256: ba2e2e4ba3a919e3e1f6a53e2eef6d6cde950a3ed83c9bf0937c0a93fb6d74d0
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001041/graph
  locator: UBERON_0001041-graph.json
  accessed_at: '2026-10-16T02:02:03Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001041",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 5e654070fd8134ce4b1dee14096d6256fb83d429090126f841d858a9aa70c8e2
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001041
  locator: UBERON_0001041.json
  accessed_at: '2026-10-16T02:02:02Z'
  support: context_only
  summary: 'Current term identity, active status and definition: {"obo_id": "UBERON:0001041",
    "label": "foregut", "is_obsolete": false, "description": ["Anterior subdivision
    of a digestive tract."]}'
  snapshot_sha256: 38f8052b71c655d4ab8e41f860cdd2f11fbbd87fc2247a5e64dcd9f2129bba28
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/cibarium_preoral_cavity.yaml
  locator: Full regenerated YAML
  accessed_at: '2026-10-16T02:42:43Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.5a9d059298", "label": "Cibarium/Preoral
    cavity", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED",
    "mapping_status": "SEEDED", "source_attestations": [{"source": "GOLD", "source_id":
    "gold.ecosystem:7386", "source_label": "Cibarium/Preoral cavity", "source_path":
    "Host-associated > Arthropoda: Insects > Digestive system > Foregut > Cibarium/Preoral
    cavity"}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator":
    "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED:
    no ontology term fits this concept. [CLASS-level] Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep):
    no term in the vendored slice matched this label by any search route. Whether
    the concept is a habitat at all was NOT assessed, so this is not yet a term-request
    candidate. (source concept habitatmech:GOLD.5a9d059298)"}, {"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp":
    "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.bd1664969c
    for habitatmech:GOLD.5a9d059298 (Host-associated > Arthropoda: Insects > Digestive
    system > Foregut > Cibarium/Preoral cavity). Review https://github.com/CultureBotAI/HabitatMech/issues/2217
    : The insect cibarium/preoral-cavity source names a compartment, not a type of
    complete foregut. Primary sharpshooter dissection separates cibarium and precibarium
    within the functional anterior foregut and studies their microbial context. This
    supports physical habitat meaning and a part/whole distinction, not the identity
    of any GOLD specimen or universal residence of all sequenced taxa. Remove only
    the whole-foregut source parent. Exclude only this exact GOLD contribution; preserve
    all independent genera, source observations and native status. Shared mapping
    endpoints #1398 remain unresolved."}]}'
  snapshot_sha256: 815a5e0f796892a16e0d48f1438f72fd6d858716e4fca0fe0f6ddba713a331f3
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261016T021308Z-cibarium_preoral_cavity-record/review.yaml
  locator: Exact immutable predecessor and every finding
  accessed_at: '2026-10-16T02:42:43Z'
  support: supports
  summary: Original observation unchanged; exact issue keys and lineage retained.
  snapshot_sha256: dc3d159417c54abd481ec0e0ba3fc68b4a5bc04df64b245b3333a0e73b7c4ab7
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_cervix_chyme_review_repairs.py
  locator: Whole-corpus counterfactual regression
  accessed_at: '2026-10-16T02:42:43Z'
  support: supports
  summary: Exactly six documents change, only parent_habitats and appended audit event;
    all identities, counts, units, source paths, aliases, taxa, statuses and other
    records are identical.
  snapshot_sha256: 6c5278c50f78c6abebdc9bc78e777be71a83b42e559cd1f55c201e1c881aaabd
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict broader hierarchy
  accessed_at: '2026-10-16T02:42:43Z'
  support: supports
  summary: Containment and source grouping do not imply is-a.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EHISTORY
  kind: record_content
  reference: history/mappings/cervix_chyme_review/2026-10-16T021625Z-codex-gpt-5-9b4900.yaml
  locator: Complete immutable session event
  accessed_at: '2026-10-16T02:42:43Z'
  support: supports
  summary: 'Actor codex-gpt-5, model gpt-5, tool codex; six guarded parent repairs
    under #2217.'
  snapshot_sha256: 5c5e778a351aa79a87968b5b305a660ea3b49cc5de8cbc7e0ab8232dffc14483
- evidence_id: EINPUT
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact guarded source row
  accessed_at: '2026-10-16T02:42:43Z'
  support: supports
  summary: '[[7, "habitatmech:GOLD.5a9d059298\tHost-associated > Arthropoda: Insects
    > Digestive system > Foregut > Cibarium/Preoral cavity\thabitatmech:GOLD.bd1664969c\tcodex-gpt-5\t2026-10-16\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2217 : The insect cibarium/preoral-cavity
    source names a compartment, not a type of complete foregut. Primary sharpshooter
    dissection separates cibarium and precibarium within the functional anterior foregut
    and studies their microbial context. This supports physical habitat meaning and
    a part/whole distinction, not the identity of any GOLD specimen or universal residence
    of all sequenced taxa. Remove only the whole-foregut source parent. Exclude only
    this exact GOLD contribution; preserve all independent genera, source observations
    and native status. Shared mapping endpoints #1398 remain unresolved."]]'
  snapshot_sha256: 04ba048af6f93b69c127bc3d47e2403dbe153452c75f9e26939188fc5daa52d7
assessments:
- assessment_id: A1
  area: consistency
  topic: Bounded repair and field preservation
  outcome: supported
  summary: Removed only the reviewed GOLD context-parent contribution habitatmech:GOLD.bd1664969c.
    Preserved source identity, observations, counts/units, native status and all independent
    genera. No unresolved predecessor finding remains in this target scope.
  target_ids:
  - habitatmech:GOLD.5a9d059298
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EINPUT
- assessment_id: A2
  area: identity
  topic: Current identity and strict ancestry
  outcome: supported
  summary: 'habitatmech:GOLD.5a9d059298: Cibarium/Preoral cavity; UNGROUNDED/SEEDED;
    parents []. No replacement genus or optional definition invented. Original primary-source
    assessments remain bounded to the claims in EPREV.'
  target_ids:
  - habitatmech:GOLD.5a9d059298
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EINPUT
- assessment_id: A3
  area: quantity
  topic: Nonadditive frozen evidence
  outcome: supported
  summary: '[{"source": "GOLD", "source_id": "gold.ecosystem:7386", "source_label":
    "Cibarium/Preoral cavity", "source_path": "Host-associated > Arthropoda: Insects
    > Digestive system > Foregut > Cibarium/Preoral cavity"}]. Counterfactual comparison
    preserves entire source and taxon fields.'
  target_ids:
  - habitatmech:GOLD.5a9d059298
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EINPUT
- assessment_id: A4
  area: representation
  topic: Every predecessor finding reconciled
  outcome: supported
  summary: All issue keys, targets and exact predecessors retained. Parent repair
    does not certify mapping endpoints or SSSOM/KGX.
  target_ids:
  - habitatmech:GOLD.5a9d059298
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EINPUT
- assessment_id: A5
  area: completeness
  topic: Optional claims and remaining uncertainty
  outcome: supported
  summary: No parameters, mechanisms or characteristic-presence claims added. Counts
    are not prevalence or biological absence.
  target_ids:
  - habitatmech:GOLD.5a9d059298
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EINPUT
findings:
- finding_id: F1
  issue_key: cibarium-preoral-cavity-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is not a broader habitat class
  description: Excluded only exact guarded GOLD contribution habitatmech:GOLD.bd1664969c.
    Independent genera and every other scientific field remain unchanged.
  target_ids:
  - habitatmech:GOLD.5a9d059298
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX1
  - EX2
  - EX3
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EHISTORY
  - EINPUT
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported hierarchy, mapping or source-evidence
    semantics; correct deterministic reproduction does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2217
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T021308Z-cibarium_preoral_cavity-record
    finding_id: F1
  disposition_reason: Excluded only exact guarded GOLD contribution habitatmech:GOLD.bd1664969c.
    Independent genera and every other scientific field remain unchanged.
actions: []
limitations:
- Source counts, score channels and ranks do not establish prevalence, viability or
  characteristic presence. Original specimen-level and pair-level evidence has not
  been reconstructed exhaustively.
- Configured label validation skipped 2063 no-adapter pairs; displayed target TaxIds
  were resolved separately with current NCBI.
- 'iModulonDB is not applicable: target claims do not assert genes, regulators or
  expression modules. No paid research or native status promotion.'
- Same-agent assessment, not independent approval. The exact-base hosted archive contract
  passed, but its full quality gate was still running at capture. Native scientific
  and product gates passed. Final-head and merge-queue quality checks remain required
  before merge.
notes:
- Native working-tree capture retained; the off-main base will be preserved by an
  annotated provenance tag before branch deletion.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261016T021308Z-cibarium_preoral_cavity-record
  relationship: Exact predecessor; every finding reconciled without rewriting history.
```
