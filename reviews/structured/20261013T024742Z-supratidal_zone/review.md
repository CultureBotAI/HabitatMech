# Scientific record review: Supratidal zone

- Review: 20261013T024742Z-supratidal_zone
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-13T02:18:30.687830Z
- Finished UTC: 2026-10-13T02:47:42.901031Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

GOLD node7910 preserves its marine supratidal source identity and the previously corrected whole-region parent exclusion. The retained NARROW mapping still has an implicit ontology comparison target under the shared attestation contract (#1398). The exact versus narrower scope of this automatically placed source remains unestablished.

## Scope And Provenance

One entire generated habitat and every contributing source concept.

Selection: Next four aquatic paths without completed individual structured scientific reviews, in stable path order; this bundle assesses only this target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 348085582b0090404a73c122376b8045e6050c41.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.2ef6207bd1 | data/habitats/aquatic/supratidal_zone.yaml | generated | Supratidal zone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validation | passed | True | habitatmech:GOLD.2ef6207bd1 | Actual success 2026-10-13T02:18:39.239931+00:00 to 2026-10-13T02:18:44.735906+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | habitatmech:GOLD.2ef6207bd1 | Actual success 2026-10-13T02:18:44.737837+00:00 to 2026-10-13T02:18:51.021851+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | habitatmech:GOLD.2ef6207bd1 | Actual success 2026-10-13T02:08:10.569120+00:00 to 2026-10-13T02:09:49.514758+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | habitatmech:GOLD.2ef6207bd1 | Actual success 2026-10-13T02:09:49.516177+00:00 to 2026-10-13T02:10:00.046475+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | habitatmech:GOLD.2ef6207bd1 | Actual success 2026-10-13T02:10:00.047246+00:00 to 2026-10-13T02:10:00.898990+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | habitatmech:GOLD.2ef6207bd1 | Actual success 2026-10-13T02:10:00.899837+00:00 to 2026-10-13T02:10:22.775641+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | habitatmech:GOLD.2ef6207bd1 | Actual success 2026-10-13T02:10:22.776432+00:00 to 2026-10-13T02:10:29.162380+00:00. The command retains its record-specific or corpus-wide scope. |
| Native validation | passed | True | habitatmech:GOLD.2ef6207bd1 | Actual success 2026-10-13T02:10:29.163275+00:00 to 2026-10-13T02:10:58.864928+00:00. The command retains its record-specific or corpus-wide scope. |
| Exact-input hosted authoritative QC | passed | True | habitatmech:GOLD.2ef6207bd1 | Exact-head authoritative hosted QC passed: 1060 tests, 3 skipped, and all native quality gates. New review files are not covered by this pre-save run. |
| Claim-specific expression module | not_applicable | False | habitatmech:GOLD.2ef6207bd1 | No gene, regulator or strain-specific transcriptomic claim occurs in this habitat record; iModulonDB is not applicable and non-use is not negative evidence. |

## Scientific And Domain Assessments

### Exact identity and strictly broader hierarchy

identity: concern. Targets: habitatmech:GOLD.2ef6207bd1.

The record is a supratidal environmental zone, not permanently submerged water and not a kind of the whole marine littoral region. Active ENVO:01000124 describes the marine supra-littoral zone and has marine environmental zone as its named parent. Its supratidal-zone spelling is a related synonym. Neither that synonym nor an extra level in the GOLD path proves a strict subclass relation. Preserve the mint and candidate placement while undertaking source-level ITEM assessment; do not silently upgrade to exact identity.

### Source counters, triad roles and review lifecycle

provenance: supported. Targets: habitatmech:GOLD.2ef6207bd1.

gold_ecosystem_paths row1534 preserves the exact five-level path and sole node7910. All direct occurrence counters are zero, so omitted display count/unit is appropriate, not proof of ecological absence. The exact source guard row153 excludes ENVO:01000125 only. A structured scan of all top-level data/raw and curation TSVs found no source ITEM decision or exact-path bulk, triad or study row; ignored files were included in that bounded scan. SEEDED therefore remains distinct from an ITEM-reviewed source.

### Bounded taxon evidence and optional scientific content

evidence: supported. Targets: habitatmech:GOLD.2ef6207bd1.

No taxa, measured parameters, mechanism edges, citations or authored definition are asserted. NOAA describes occasional very-high/storm-tide flooding; this supports the shoreline context but does not determine a GOLD-to-ENVO mapping endpoint or strict narrower scope. A whole-region part-of relation must not be substituted for is-a.

### NARROW mapping does not expose its ontology comparison endpoint

grounding: concern. Targets: habitatmech:GOLD.2ef6207bd1.

The source mint is retained while skos:narrowMatch is emitted for its implicit comparison with ENVO:01000124. SourceAttestation.mapping_predicate instead declares source_id to the record identifier, omitting it when the record is the source concept. The comparison object is therefore ambiguous. This is an application representation mismatch, not a claim that SKOS forbids self-links.

## Findings

### F1: NARROW mapping does not expose its ontology comparison endpoint

major / open / confirmed; issue key: habitatmech-gold.2ef6207bd1-mapping-endpoint-contract.

The source mint is retained while skos:narrowMatch is emitted for its implicit comparison with ENVO:01000124. SourceAttestation.mapping_predicate instead declares source_id to the record identifier, omitting it when the record is the source concept. The comparison object is therefore ambiguous. This is an application representation mismatch, not a claim that SKOS forbids self-links.

## Recommended Actions And Acceptance Checks

### A1

Resolve source-to-record identity versus retained-record-to-ontology comparisons in the shared schema, seeder and consumers. Separately assess this exact source scope before deciding its mapping strength.

- Represent and test actual subject, predicate and object across exact, retained-mint and parent routes; a global broad/narrow predicate swap is insufficient.
- Preserve node7910, the complete source path, omitted counts and the guarded whole-littoral-region exclusion.
- Check actual downstream SSSOM/KGX triples against current kg-microbe modeling before claiming compatibility.
- Append required curation history, regenerate through native writers, and pass schema, labels, provenance, exact reproduction, site and full QC. Preserve prior immutable reviews and use a linked successor to change this disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/aquatic/supratidal_zone.yaml | supports | Entire YAML inspected, including each source, taxon and historical event. GOLD node7910 preserves its marine supratidal source identity and the previously corrected whole-region parent exclusion. The retained NARROW mapping still has an implicit ontology comparison target under the shared attestation contract (#1398). The exact versus narrower scope of this automatically placed source remains unestablished. |
| RAW | data/raw/gold_ecosystem_paths.tsv:1534; curation/gold_parent_exclusions.tsv:153 | supports | gold_ecosystem_paths row1534 preserves the exact five-level path and sole node7910. All direct occurrence counters are zero, so omitted display count/unit is appropriate, not proof of ecological absence. The exact source guard row153 excludes ENVO:01000125 only. A structured scan of all top-level data/raw and curation TSVs found no source ITEM decision or exact-path bulk, triad or study row; ignored files were included in that bounded scan. SEEDED therefore remains distinct from an ITEM-reviewed source. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; docs/record-review-profile.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied strict-genus, source-comparison, typed-synonym, MIxS-role, source-unit, association-versus-characteristic and ITEM lifecycle rules. Native optional fields are not mandatory scientific inventions. |
| CODE | src/habitatmech/seed.py:427; src/habitatmech/seed.py:804; src/habitatmech/schema/habitatmech.yaml:317; src/habitatmech/extract.py:338; src/habitatmech/extract.py:835 | supports | Inspected source and synonym routes plus PREGO ranking semantics. Exact full-document reconstruction from build_corpus/build_document matched this record, with captured input hashes rechecked unchanged. Reproduction establishes implementation provenance, not scientific correctness. |
| SEARCH | curation; history; research; conf; reviews/structured; reports/yaml_record_review; data/raw | supports | Bounded ignored/hidden-inclusive searches used target ID, source mint, label and slug. Existing legacy report and later maintained fixes were inspected; legacy prose is not a new structured disposition. No earlier completed individual structured review of this exact target was present in the coverage inventory. Original source membership was not independently rebuilt; no global absence claim is made. |
| QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38335796983 | supports | Exact-head authoritative hosted QC passed: 1060 tests, 3 skipped, and all native quality gates. This exact captured scientific-input head was checked; these new immutable reviews require separate integrity and final-head CI. |
| ONT0 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000124 | supports | Active ENVO:01000124 marine supra-littoral zone. Description inspected against the stored definition and the identity assessment above. Named parents from the official linked response: [["ENVO:01001201", "marine environmental zone"]]. Relevant typed synonym assertions: [["splash zone", "hasRelatedSynonym"], ["spray zone", "hasRelatedSynonym"], ["supralittoral zone", "hasBroadSynonym"], ["supratidal zone", "hasRelatedSynonym"]]. |
| ONT1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000125 | supports | Active ENVO:01000125 marine littoral zone. Description inspected against the stored definition and the identity assessment above. Named parents from the official linked response: [["ENVO:01000407", "littoral zone"]]. Relevant typed synonym assertions: []. |
| NOAA | https://coast.noaa.gov/estuaries/estuary-resources/glossary.html; S / Supratidal | context_only | The official glossary describes occasional flooding during unusually high or storm tides. This supports the exposure distinction, not an exact or strictly narrower ontology mapping. |

## Limits And Additional Notes

- Same-agent review, not independent approval or whole-corpus certification.
- Source occurrence and association membership was not independently rebuilt from original upstream matrices; frozen counters reproduce but do not establish characteristic presence. Live ontology and taxonomy resolution do not validate habitat occurrence.
- Ontology-label validation retains configured no-adapter skips and accepted exceptions; those skips are not scientific approval.
- Legacy reports are historical leads, not structured finding lineage; earlier corrections are not newly performed or silently reopened by this review.
- The assessment changes no habitat, decision, scientific status, history, generated site or map. Optional parameters, definitions and mechanisms are not invented.
- SSSOM/KGX compatibility was not audited. Shared endpoint issue #1398 and typed synonym issue #1249 remain open where applicable.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T024742Z-supratidal_zone
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: Supratidal zone'
started_at: '2026-10-13T02:18:30.687830Z'
finished_at: '2026-10-13T02:47:42.901031Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Agent participated in repository work; this is not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: needs_curation
summary: GOLD node7910 preserves its marine supratidal source identity and the previously
  corrected whole-region parent exclusion. The retained NARROW mapping still has an
  implicit ontology comparison target under the shared attestation contract (#1398).
  The exact versus narrower scope of this automatically placed source remains unestablished.
source:
  git_revision: 348085582b0090404a73c122376b8045e6050c41
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
  - path: conf/sources.yaml
    sha256: a8e069f9278068b57fa234f43e03c8d893f857827b83fd10cfa92d6815aed642
    role: context
  - path: curation/decisions.tsv
    sha256: eb82cec48508912622b452ae78bb1ad199c93cb0591ce534bb8f25273da4e220
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: c7017ce7889ebfce889eb6f2c6a6c12510428be4b8a4370e2e4e165231e1af25
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 331a7d9eb8a8909fc37402c0a776838979a8065644504d5c4f2a1c39bce5c24d
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/aquatic/supratidal_zone.yaml
    sha256: 511c780668817dc8a7adbbbfb9a173c845bbe0bffe801ddeb9c5aab4ea2adba9
    role: target
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
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
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
  - path: history/mappings/supratidal_zone/2026-10-06T155006Z-codex-gpt-5-86e7c7.yaml
    sha256: 093406011ce45689c944d97132bbbe4af36ec4a56492e640978de7ee18ca403a
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261006T152226Z-supratidal_zone.md
    sha256: d3edefd0b531299da59cfd324ca1d4faa1cbc1a0db72edd6fcdce9e9e3c7f886
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
targets:
- target_id: habitatmech:GOLD.2ef6207bd1
  path: data/habitats/aquatic/supratidal_zone.yaml
  label: Supratidal zone
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source identity and ITEM review decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact source context-parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Definitions and genus
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology definitions and synonyms
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Source harmonization and generated record construction
scope:
  description: One entire generated habitat and every contributing source concept.
  selection: Next four aquatic paths without completed individual structured scientific
    reviews, in stable path order; this bundle assesses only this target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.2ef6207bd1
checks:
- check_id: C0
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  command: just validate data/habitats/aquatic/supratidal_zone.yaml
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:18:39.239931+00:00 to 2026-10-13T02:18:44.735906+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C1
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  command: just validate-strict data/habitats/aquatic/supratidal_zone.yaml
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:18:44.737837+00:00 to 2026-10-13T02:18:51.021851+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C2
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  command: just validate-products
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:08:10.569120+00:00 to 2026-10-13T02:09:49.514758+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C3
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  command: just validate-history
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:09:49.516177+00:00 to 2026-10-13T02:10:00.046475+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C4
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  command: just provenance-check
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:10:00.047246+00:00 to 2026-10-13T02:10:00.898990+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C5
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  command: just verify-corpus
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:10:00.899837+00:00 to 2026-10-13T02:10:22.775641+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C6
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  command: just validate-causal-all
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:10:22.776432+00:00 to 2026-10-13T02:10:29.162380+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: C7
  name: Native validation
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  command: just term-requests-check
  exit_code: 0
  evidence_ids:
  - QC
  summary: Actual success 2026-10-13T02:10:29.163275+00:00 to 2026-10-13T02:10:58.864928+00:00.
    The command retains its record-specific or corpus-wide scope.
- check_id: CI
  name: Exact-input hosted authoritative QC
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  command: gh run view 38335796983 --log
  exit_code: 0
  evidence_ids:
  - QC
  summary: 'Exact-head authoritative hosted QC passed: 1060 tests, 3 skipped, and
    all native quality gates. New review files are not covered by this pre-save run.'
- check_id: IMOD
  name: Claim-specific expression module
  required: false
  status: not_applicable
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  summary: No gene, regulator or strain-specific transcriptomic claim occurs in this
    habitat record; iModulonDB is not applicable and non-use is not negative evidence.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/aquatic/supratidal_zone.yaml
  accessed_at: '2026-10-13T02:47:42.900792Z'
  support: supports
  summary: Entire YAML inspected, including each source, taxon and historical event.
    GOLD node7910 preserves its marine supratidal source identity and the previously
    corrected whole-region parent exclusion. The retained NARROW mapping still has
    an implicit ontology comparison target under the shared attestation contract (#1398).
    The exact versus narrower scope of this automatically placed source remains unestablished.
- evidence_id: RAW
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv:1534; curation/gold_parent_exclusions.tsv:153
  accessed_at: '2026-10-13T02:47:42.900792Z'
  support: supports
  summary: gold_ecosystem_paths row1534 preserves the exact five-level path and sole
    node7910. All direct occurrence counters are zero, so omitted display count/unit
    is appropriate, not proof of ecological absence. The exact source guard row153
    excludes ENVO:01000125 only. A structured scan of all top-level data/raw and curation
    TSVs found no source ITEM decision or exact-path bulk, triad or study row; ignored
    files were included in that bounded scan. SEEDED therefore remains distinct from
    an ITEM-reviewed source.
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; docs/record-review-profile.md;
    src/habitatmech/schema/habitatmech.yaml
  accessed_at: '2026-10-13T02:47:42.900792Z'
  support: supports
  summary: Applied strict-genus, source-comparison, typed-synonym, MIxS-role, source-unit,
    association-versus-characteristic and ITEM lifecycle rules. Native optional fields
    are not mandatory scientific inventions.
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py:427; src/habitatmech/seed.py:804; src/habitatmech/schema/habitatmech.yaml:317;
    src/habitatmech/extract.py:338; src/habitatmech/extract.py:835
  accessed_at: '2026-10-13T02:47:42.900792Z'
  support: supports
  summary: Inspected source and synonym routes plus PREGO ranking semantics. Exact
    full-document reconstruction from build_corpus/build_document matched this record,
    with captured input hashes rechecked unchanged. Reproduction establishes implementation
    provenance, not scientific correctness.
- evidence_id: SEARCH
  kind: record_content
  reference: curation; history; research; conf; reviews/structured; reports/yaml_record_review;
    data/raw
  accessed_at: '2026-10-13T02:47:42.900792Z'
  support: supports
  summary: Bounded ignored/hidden-inclusive searches used target ID, source mint,
    label and slug. Existing legacy report and later maintained fixes were inspected;
    legacy prose is not a new structured disposition. No earlier completed individual
    structured review of this exact target was present in the coverage inventory.
    Original source membership was not independently rebuilt; no global absence claim
    is made.
- evidence_id: QC
  kind: record_content
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38335796983
  accessed_at: '2026-10-13T02:47:42.900792Z'
  support: supports
  summary: 'Exact-head authoritative hosted QC passed: 1060 tests, 3 skipped, and
    all native quality gates. This exact captured scientific-input head was checked;
    these new immutable reviews require separate integrity and final-head CI.'
- evidence_id: ONT0
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000124
  accessed_at: '2026-10-13T02:20:18.811670Z'
  support: supports
  summary: 'Active ENVO:01000124 marine supra-littoral zone. Description inspected
    against the stored definition and the identity assessment above. Named parents
    from the official linked response: [["ENVO:01001201", "marine environmental zone"]].
    Relevant typed synonym assertions: [["splash zone", "hasRelatedSynonym"], ["spray
    zone", "hasRelatedSynonym"], ["supralittoral zone", "hasBroadSynonym"], ["supratidal
    zone", "hasRelatedSynonym"]].'
- evidence_id: ONT1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000125
  accessed_at: '2026-10-13T02:20:27.588163Z'
  support: supports
  summary: 'Active ENVO:01000125 marine littoral zone. Description inspected against
    the stored definition and the identity assessment above. Named parents from the
    official linked response: [["ENVO:01000407", "littoral zone"]]. Relevant typed
    synonym assertions: [].'
- evidence_id: NOAA
  kind: database
  reference: https://coast.noaa.gov/estuaries/estuary-resources/glossary.html
  locator: S / Supratidal
  accessed_at: '2026-10-13T02:31:36Z'
  support: context_only
  summary: The official glossary describes occasional flooding during unusually high
    or storm tides. This supports the exposure distinction, not an exact or strictly
    narrower ontology mapping.
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Exact identity and strictly broader hierarchy
  outcome: concern
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  evidence_ids:
  - RECORD
  - RAW
  - RULES
  - ONT0
  - ONT1
  summary: The record is a supratidal environmental zone, not permanently submerged
    water and not a kind of the whole marine littoral region. Active ENVO:01000124
    describes the marine supra-littoral zone and has marine environmental zone as
    its named parent. Its supratidal-zone spelling is a related synonym. Neither that
    synonym nor an extra level in the GOLD path proves a strict subclass relation.
    Preserve the mint and candidate placement while undertaking source-level ITEM
    assessment; do not silently upgrade to exact identity.
- assessment_id: PROVENANCE
  area: provenance
  topic: Source counters, triad roles and review lifecycle
  outcome: supported
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  evidence_ids:
  - RECORD
  - RAW
  - CODE
  summary: gold_ecosystem_paths row1534 preserves the exact five-level path and sole
    node7910. All direct occurrence counters are zero, so omitted display count/unit
    is appropriate, not proof of ecological absence. The exact source guard row153
    excludes ENVO:01000125 only. A structured scan of all top-level data/raw and curation
    TSVs found no source ITEM decision or exact-path bulk, triad or study row; ignored
    files were included in that bounded scan. SEEDED therefore remains distinct from
    an ITEM-reviewed source.
- assessment_id: ASSOCIATIONS
  area: evidence
  topic: Bounded taxon evidence and optional scientific content
  outcome: supported
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  evidence_ids:
  - RECORD
  - RAW
  - CODE
  - NOAA
  summary: No taxa, measured parameters, mechanism edges, citations or authored definition
    are asserted. NOAA describes occasional very-high/storm-tide flooding; this supports
    the shoreline context but does not determine a GOLD-to-ENVO mapping endpoint or
    strict narrower scope. A whole-region part-of relation must not be substituted
    for is-a.
- assessment_id: CONTRACT
  area: grounding
  topic: NARROW mapping does not expose its ontology comparison endpoint
  outcome: concern
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  evidence_ids:
  - RECORD
  - RAW
  - CODE
  - ONT0
  summary: The source mint is retained while skos:narrowMatch is emitted for its implicit
    comparison with ENVO:01000124. SourceAttestation.mapping_predicate instead declares
    source_id to the record identifier, omitting it when the record is the source
    concept. The comparison object is therefore ambiguous. This is an application
    representation mismatch, not a claim that SKOS forbids self-links.
findings:
- finding_id: F1
  issue_key: habitatmech-gold.2ef6207bd1-mapping-endpoint-contract
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: NARROW mapping does not expose its ontology comparison endpoint
  description: The source mint is retained while skos:narrowMatch is emitted for its
    implicit comparison with ENVO:01000124. SourceAttestation.mapping_predicate instead
    declares source_id to the record identifier, omitting it when the record is the
    source concept. The comparison object is therefore ambiguous. This is an application
    representation mismatch, not a claim that SKOS forbids self-links.
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  field_paths:
  - source_attestations.mapping_predicate
  evidence_ids:
  - RECORD
  - RAW
  - RULES
  - CODE
  - ONT0
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained representation owner; generated YAML remains read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained representation owner; generated YAML remains read-only
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material representation or semantic-scope mismatch, not stylistic
    wording.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: A1
  description: Resolve source-to-record identity versus retained-record-to-ontology
    comparisons in the shared schema, seeder and consumers. Separately assess this
    exact source scope before deciding its mapping strength.
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.2ef6207bd1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained representation owner; generated YAML remains read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained representation owner; generated YAML remains read-only
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Represent and test actual subject, predicate and object across exact, retained-mint
    and parent routes; a global broad/narrow predicate swap is insufficient.
  - Preserve node7910, the complete source path, omitted counts and the guarded whole-littoral-region
    exclusion.
  - Check actual downstream SSSOM/KGX triples against current kg-microbe modeling
    before claiming compatibility.
  - Append required curation history, regenerate through native writers, and pass
    schema, labels, provenance, exact reproduction, site and full QC. Preserve prior
    immutable reviews and use a linked successor to change this disposition.
limitations:
- Same-agent review, not independent approval or whole-corpus certification.
- Source occurrence and association membership was not independently rebuilt from
  original upstream matrices; frozen counters reproduce but do not establish characteristic
  presence. Live ontology and taxonomy resolution do not validate habitat occurrence.
- Ontology-label validation retains configured no-adapter skips and accepted exceptions;
  those skips are not scientific approval.
- Legacy reports are historical leads, not structured finding lineage; earlier corrections
  are not newly performed or silently reopened by this review.
- The assessment changes no habitat, decision, scientific status, history, generated
  site or map. Optional parameters, definitions and mechanisms are not invented.
- 'SSSOM/KGX compatibility was not audited. Shared endpoint issue #1398 and typed
  synonym issue #1249 remain open where applicable.'
tags:
- habitatmech
- record-review
- aquatic
```
