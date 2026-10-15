# Remediation review: alga-associated environment

- Review: 20261015T013718Z-algae-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T01:32:36Z
- Finished UTC: 2026-10-15T01:37:18Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The authored Algae exact synonym is removed from the maintained term request. The existing organism xref guard prevents automatic reintroduction. Definition, genus, original definition-event provenance, FOODON xref, both verbatim source attestations, counts/units and all 25 taxon entries are unchanged. The confirmed mixed Madin source-equivalence finding remains open under #1307; synonym repair does not establish a living-host interpretation for every source member.

## Scope And Provenance

Focused scientific reassessment of the complete current record and exact prior findings after maintained-input remediation.

Selection: Exact successor to 20261015T005332Z-algae-record
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 81f9c9ead99cc14954df0c59bf752ed7284dd4b3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.02383c20a7 | data/habitats/host_associated/algae.yaml | generated | alga-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:16:28Z to 2026-10-15T01:16:33Z. No issues found |
| Native validate-strict | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:16:49Z to 2026-10-15T01:17:00Z. files scanned:      6<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native validate-history | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:17:00Z to 2026-10-15T01:17:19Z. No issues found<br>725 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native provenance-check | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:17:19Z to 2026-10-15T01:17:20Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native verify-corpus | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:17:20Z to 2026-10-15T01:18:03Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native validate-causal-all | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:18:03Z to 2026-10-15T01:18:11Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native term-requests-check | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:18:11Z to 2026-10-15T01:18:46Z. term-request table is current (110 terms) |
| Native validate-products | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:18:46Z to 2026-10-15T01:20:48Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond. |
| Focused regressions | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:20:48Z to 2026-10-15T01:28:37Z. ........................................................................ [ 74%]<br>.........................                                                [100%]<br>97 passed in 467.28s (0:07:47) |
| Repository lint | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:28:37Z to 2026-10-15T01:28:37Z. All checks passed! |
| Whitespace | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:28:37Z to 2026-10-15T01:28:40Z. |
| Native render | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:29:55Z to 2026-10-15T01:31:02Z. rendered 3208 habitat pages, 258 redirect stubs, 8 categories, 121 term requests -&gt; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages |
| Native validate-history | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:31:18Z to 2026-10-15T01:31:36Z. No issues found<br>726 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native verify-corpus | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:31:36Z to 2026-10-15T01:32:14Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Focused regressions | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:32:14Z to 2026-10-15T01:32:24Z. ..                                                                       [100%]<br>2 passed in 7.95s |
| Repository lint | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:32:24Z to 2026-10-15T01:32:24Z. All checks passed! |
| Semantic input export | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:32:24Z to 2026-10-15T01:32:39Z. {"adapter_version": "habitatmech-semantic-v1", "jsonl_sha256": "0558587d4f64acbaf076ce3c3b3031db377da3cc4900486a1ee4c271692d88f8", "mode": "export", "output": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/build/pr2145-linkfix-text-map-inputs.jsonl", "records": 3208, "scope": "full"} |
| Semantic input preservation | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:32:39Z to 2026-10-15T01:32:39Z. All 3208 semantic input rows byte-identical after punctuation-only correction |
| Whitespace | passed | True | habitatmech:GOLD.02383c20a7 | Executed 2026-10-15T01:32:39Z to 2026-10-15T01:32:39Z. |
| Original source-member recovery | unavailable | False | habitatmech:GOLD.02383c20a7 | Original GOLD member joins and PREGO pair-level citations remain unavailable. Anatomy and synonym corrections are not occurrence certification. |
| Final publication gates | unavailable | False | habitatmech:GOLD.02383c20a7 | Final retained-archive verification and protected final-head QC remain required before merge. Local map verification and site regeneration passed; final publication freshness is reported separately. No final merge-gate success is predeclared. |

## Scientific And Domain Assessments

### Exact maintained-input repairs and remaining findings

grounding: concern. Targets: habitatmech:GOLD.02383c20a7.

The authored Algae exact synonym is removed from the maintained term request. The existing organism xref guard prevents automatic reintroduction. Definition, genus, original definition-event provenance, FOODON xref, both verbatim source attestations, counts/units and all 25 taxon entries are unchanged. The confirmed mixed Madin source-equivalence finding remains open under #1307; synonym repair does not establish a living-host interpretation for every source member.

### Identity, source evidence and native status preservation

consistency: supported. Targets: habitatmech:GOLD.02383c20a7.

All original fields outside the explicit tested corrections are preserved. The entire current target was re-read. Native status is REVIEWED/UNGROUNDED; a saved review does not promote status or certify species occurrence.

## Findings

### F1: Mixed Madin category is merged as one living-host environment

major / open / confirmed; issue key: HM-ALGAE-001.

Pre-fix observation: The pinned Madin release contains 100 host_algae observations for 88 distinct IDs, including every displayed ID. Its conversion table maps 38 source strings, including decomposing scum, algal mats, algae-bearing sediment and lichen-colonized rock. This mixed scope is not unconditionally the living-host environment.

Disposition: This distinct confirmed finding remains unresolved; the scoped anatomy or synonym correction does not establish the missing source-equivalence or explicit mapping-endpoint contract.

### F2: Organism-group name is an exact synonym of its environment

major / resolved / confirmed; issue key: gold-02383c20a7-host-name-exact-synonym.

Pre-fix observation: Algae denotes the organism group and should not be an exact synonym of its associated environment.

Disposition: The authored Algae exact synonym is removed from the maintained term request. The existing organism xref guard prevents automatic reintroduction. Definition, genus, original definition-event provenance, FOODON xref, both verbatim source attestations, counts/units and all 25 taxon entries are unchanged. The confirmed mixed Madin source-equivalence finding remains open under #1307; synonym repair does not establish a living-host interpretation for every source member.

## Recommended Actions And Acceptance Checks

### A1

Reassess the Madin SAME_AS decision using original observation contexts. Preserve supported thallus/coculture associations, separate material/community contexts, and remove the host-name exact synonym from the authored term request while preserving the source label in provenance. The existing annotation-correction table only handles ontology synonyms, so do not misuse it for this curated synonym; a new typed authored-synonym capability would need its own design. Review the eight unrouted parameter rows only after source scope is resolved; do not attach them by lexical match.

- Resolve source scope and relation endpoints with inspected primary or original source evidence; retain explicit uncertainty until then.
- Make any separately authorized correction in maintained inputs, append native history, run just seed and inspect affected just seed-canary output before regeneration.
- Add focused regressions for the supported and rejected scopes; run strict/schema, provenance, history, corpus reproduction, causal, term-request and configured label gates, followed by just qc.
- Inspect actual downstream mappings and generated pages/redirects after any identity or relation change; deterministic record checks do not certify SSSOM/KGX compatibility.
- Save an immutable successor with these exact finding identities; do not rewrite this observation or promote scientific status by review alone.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| PREVIOUS | reviews/structured/20261015T005332Z-algae-record/review.yaml | supports | Exact same-agent predecessor retains inspected primary ontology/literature evidence, hashes, source rows and bounded access limitations. Not independent approval. |
| PATCH | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/record_annotation_corrections.tsv; curation/term_requests.tsv; data/habitats/host_associated/algae.yaml | supports | The authored Algae exact synonym is removed from the maintained term request. The existing organism xref guard prevents automatic reintroduction. Definition, genus, original definition-event provenance, FOODON xref, both verbatim source attestations, counts/units and all 25 taxon entries are unchanged. The confirmed mixed Madin source-equivalence finding remains open under #1307; synonym repair does not establish a living-host interpretation for every source member. |
| REGRESSION | tests/test_airway_and_alga_repairs.py | supports | A full-corpus counterfactual reconstructs the former input rows and proves exactly five changed records, no identity changes, preserved counts/taxa/attestations and prior events, exact remaining parents and unchanged child insect-air-sac bytes. Only the insect Trachea parent gains ITEM-derived REVIEWED status. |

## Limits And Additional Notes

- Same-agent scientific reassessment, not independent approval.
- Original source-member evidence remains unavailable; no full-corpus, species-occurrence or SSSOM/KGX readiness certification.
- Configured label correspondence retains unsupported-prefix skips. Final retained-archive and protected publication gates are pending at this immutable observation.
- Unresolved confirmed major finding(s): HM-ALGAE-001.
- Source inputs were freshly captured with the native inspector and checked against exact committed blobs and current disk bytes. Retain this off-main input commit with an annotated provenance tag before squash and branch deletion.
- The original definition date, author and generated definition history of Algae were deliberately preserved; the new session history records the synonym-only correction. No historic review/history file was rewritten.
- Adversarial rendered-page inspection found a semicolon incorrectly included in the new issue 2148 href. The new publication regression reproduced the defect (one expected failure). Issue 2152 corrects the maintained note and regenerates the record/page, followed by fresh passing checks. Earlier temporary captures were superseded by a fresh native inspection and reassessment, not silently rehashed. Scientific fields and all 3208 semantic input rows remain unchanged by this punctuation-only follow-up.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T013718Z-algae-remediation
kind: record
repository: CultureBotAI/HabitatMech
title: 'Remediation review: alga-associated environment'
started_at: '2026-10-15T01:32:36Z'
finished_at: '2026-10-15T01:37:18Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Continuing review agent; current claims and historical leads
    were reassessed against primary evidence. No independent approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'The authored Algae exact synonym is removed from the maintained term request.
  The existing organism xref guard prevents automatic reintroduction. Definition,
  genus, original definition-event provenance, FOODON xref, both verbatim source attestations,
  counts/units and all 25 taxon entries are unchanged. The confirmed mixed Madin source-equivalence
  finding remains open under #1307; synonym repair does not establish a living-host
  interpretation for every source member.'
source:
  git_revision: 81f9c9ead99cc14954df0c59bf752ed7284dd4b3
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
    sha256: d9c76d275d61b7fef860179b6d0472e54e15b2b027022d7a125a19f03881fd8e
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 505e6efc536392c9f6ce77fd4a70284392166269713189ff53e40367256d2899
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 41d223485ac848fcb5a724dc308caba88e922ae89c972ca9f92565ff3b753f32
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 144e48a101aa072a96cd08f88a9a66ecd14122d788c54b95ac8ad7d934f720bc
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 034aee0bcf71e9c813d20450bc93d7f3f6070cab0ddebfe6f3f39911e7c6b0e1
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
    role: context
  - path: data/habitats/host_associated/algae.yaml
    sha256: d188ea80a8e2702b52255dcc82378cb14be502fdaba853827d6138ba86a9f0b6
    role: target
  - path: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
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
  - path: history/mappings/algae/2026-10-15T011337Z-codex-gpt-5-0745f0.yaml
    sha256: 43617f393e55f4ae3c0a057db3bed3910ad95814c29c0004527e8e456e43b55c
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261003T221216Z-algae.md
    sha256: a04e507bd94034dbccead13ec666fb60fa97f0852e68b820d2da7817724f210d
    role: context
  - path: reviews/structured/20261015T005332Z-algae-record/review.md
    sha256: 4ac2f6db8dae4429b05f4e4c8e1f502730130099447e57bb3fa934f4c43fbccd
    role: context
  - path: reviews/structured/20261015T005332Z-algae-record/review.yaml
    sha256: 13b269e6754a46e4ac4c063982567e1570ebc4a7bc7a5d48a17077018c38510b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/curate/decisions.py
    sha256: f33d3e9dc95bb428e63e640d48d4074cf15e90ea666603fb16fb651d591e3f02
    role: context
  - path: src/habitatmech/curate/definitions.py
    sha256: decd02eea029e884ab1a8bbb51dd870edb5544906b3ddd39598147b27ce572c9
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
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: tests/test_airway_and_alga_repairs.py
    sha256: 8593a60916200c099b6ec7d30cfc542a71acf55dafe09c22deadece1e0080f6e
    role: context
  - path: tests/test_airway_publication.py
    sha256: 0cc3a47fdabc09abdc12c5758b7fa4f05931720c3a01c33353bdfe1c8c3039ef
    role: context
targets:
- target_id: habitatmech:GOLD.02383c20a7
  path: data/habitats/host_associated/algae.yaml
  label: alga-associated environment
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/curate/definitions.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained source, curation input, or generator; target YAML is read-only
scope:
  description: Focused scientific reassessment of the complete current record and
    exact prior findings after maintained-input remediation.
  selection: Exact successor to 20261015T005332Z-algae-record
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.02383c20a7
checks:
- check_id: FIX2
  name: Native validate
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/algae.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Executed 2026-10-15T01:16:28Z to 2026-10-15T01:16:33Z. No issues found
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX6
  name: Native validate-strict
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/air_sac.yaml data/habitats/host_associated/air_sacs__d20658f1.yaml
    data/habitats/host_associated/algae.yaml data/habitats/host_associated/alveoli.yaml
    data/habitats/host_associated/alveoli__5d35ddee.yaml data/habitats/host_associated/trachea__4ac9ebc1.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: "Executed 2026-10-15T01:16:49Z to 2026-10-15T01:17:00Z. files scanned:\
    \      6\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:           \
    \     reports/instance_validation_failures.tsv"
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX7
  name: Native validate-history
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: 'Executed 2026-10-15T01:17:00Z to 2026-10-15T01:17:19Z. No issues found

    725 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX8
  name: Native provenance-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: 'Executed 2026-10-15T01:17:19Z to 2026-10-15T01:17:20Z. provenance current:
    14 committed inventories, 2 GOLD sources'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX9
  name: Native verify-corpus
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: "Executed 2026-10-15T01:17:20Z to 2026-10-15T01:18:03Z. expected 3208 records,\
    \ found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus\
    \ reproduces exactly from data/raw/"
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX10
  name: Native validate-causal-all
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Executed 2026-10-15T01:18:03Z to 2026-10-15T01:18:11Z. validated 32 causal-graph
    curation file(s) with 32 graph(s)
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX11
  name: Native term-requests-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Executed 2026-10-15T01:18:11Z to 2026-10-15T01:18:46Z. term-request table
    is current (110 terms)
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX12
  name: Native validate-products
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: "Executed 2026-10-15T01:18:46Z to 2026-10-15T01:20:48Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond."
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX13
  name: Focused regressions
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_airway_and_alga_repairs.py tests/test_gold_parent_exclusions.py
    tests/test_record_annotation_corrections.py tests/test_curated_definitions.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: 'Executed 2026-10-15T01:20:48Z to 2026-10-15T01:28:37Z. ........................................................................
    [ 74%]

    .........................                                                [100%]

    97 passed in 467.28s (0:07:47)'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX14
  name: Repository lint
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Executed 2026-10-15T01:28:37Z to 2026-10-15T01:28:37Z. All checks passed!
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX15
  name: Whitespace
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache git diff --check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Executed 2026-10-15T01:28:37Z to 2026-10-15T01:28:40Z.
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX16
  name: Native render
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just render
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Executed 2026-10-15T01:29:55Z to 2026-10-15T01:31:02Z. rendered 3208 habitat
    pages, 258 redirect stubs, 8 categories, 121 term requests -> /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX19
  name: Native validate-history
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: 'Executed 2026-10-15T01:31:18Z to 2026-10-15T01:31:36Z. No issues found

    726 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX20
  name: Native verify-corpus
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: "Executed 2026-10-15T01:31:36Z to 2026-10-15T01:32:14Z. expected 3208 records,\
    \ found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus\
    \ reproduces exactly from data/raw/"
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX21
  name: Focused regressions
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_airway_and_alga_repairs.py tests/test_airway_publication.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: 'Executed 2026-10-15T01:32:14Z to 2026-10-15T01:32:24Z. ..                                                                       [100%]

    2 passed in 7.95s'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX22
  name: Repository lint
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Executed 2026-10-15T01:32:24Z to 2026-10-15T01:32:24Z. All checks passed!
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX23
  name: Semantic input export
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    scripts/text_map_inputs.py --output build/pr2145-linkfix-text-map-inputs.jsonl
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: 'Executed 2026-10-15T01:32:24Z to 2026-10-15T01:32:39Z. {"adapter_version":
    "habitatmech-semantic-v1", "jsonl_sha256": "0558587d4f64acbaf076ce3c3b3031db377da3cc4900486a1ee4c271692d88f8",
    "mode": "export", "output": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/build/pr2145-linkfix-text-map-inputs.jsonl",
    "records": 3208, "scope": "full"}'
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX24
  name: Semantic input preservation
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -c from pathlib import Path; assert Path("build/pr2145-linkfix-text-map-inputs.jsonl").read_bytes()
    == Path("build/pr2145-text-map-inputs.jsonl").read_bytes(); print("All 3208 semantic
    input rows byte-identical after punctuation-only correction")
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Executed 2026-10-15T01:32:39Z to 2026-10-15T01:32:39Z. All 3208 semantic
    input rows byte-identical after punctuation-only correction
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: FIX25
  name: Whitespace
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache git diff --check b09f0b8718528ce9b5853f3a809d2e1846499f99
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Executed 2026-10-15T01:32:39Z to 2026-10-15T01:32:39Z.
  scope_note: Original scientific gates ran on curation commit 6106bc33751a3d37ddf03471df0122213c833d1a.
    A later punctuation-only provenance-link fix preserves all scientific fields and
    every semantic input byte; fresh changed-record validation, history/corpus gates
    and both new regressions are also recorded. Final archive and protected QC are
    separate.
- check_id: MEMBERS
  name: Original source-member recovery
  required: false
  status: unavailable
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Original GOLD member joins and PREGO pair-level citations remain unavailable.
    Anatomy and synonym corrections are not occurrence certification.
- check_id: PUBLICATION
  name: Final publication gates
  required: false
  status: unavailable
  target_ids:
  - habitatmech:GOLD.02383c20a7
  summary: Final retained-archive verification and protected final-head QC remain
    required before merge. Local map verification and site regeneration passed; final
    publication freshness is reported separately. No final merge-gate success is predeclared.
evidence:
- evidence_id: PREVIOUS
  kind: prior_review
  reference: reviews/structured/20261015T005332Z-algae-record/review.yaml
  accessed_at: '2026-10-15T01:37:18Z'
  support: supports
  summary: Exact same-agent predecessor retains inspected primary ontology/literature
    evidence, hashes, source rows and bounded access limitations. Not independent
    approval.
- evidence_id: PATCH
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/record_annotation_corrections.tsv;
    curation/term_requests.tsv; data/habitats/host_associated/algae.yaml
  accessed_at: '2026-10-15T01:37:18Z'
  support: supports
  summary: 'The authored Algae exact synonym is removed from the maintained term request.
    The existing organism xref guard prevents automatic reintroduction. Definition,
    genus, original definition-event provenance, FOODON xref, both verbatim source
    attestations, counts/units and all 25 taxon entries are unchanged. The confirmed
    mixed Madin source-equivalence finding remains open under #1307; synonym repair
    does not establish a living-host interpretation for every source member.'
- evidence_id: REGRESSION
  kind: validation
  reference: tests/test_airway_and_alga_repairs.py
  accessed_at: '2026-10-15T01:37:18Z'
  support: supports
  summary: A full-corpus counterfactual reconstructs the former input rows and proves
    exactly five changed records, no identity changes, preserved counts/taxa/attestations
    and prior events, exact remaining parents and unchanged child insect-air-sac bytes.
    Only the insect Trachea parent gains ITEM-derived REVIEWED status.
assessments:
- assessment_id: REPAIR
  area: grounding
  topic: Exact maintained-input repairs and remaining findings
  outcome: concern
  target_ids:
  - habitatmech:GOLD.02383c20a7
  evidence_ids:
  - PREVIOUS
  - PATCH
  - REGRESSION
  summary: 'The authored Algae exact synonym is removed from the maintained term request.
    The existing organism xref guard prevents automatic reintroduction. Definition,
    genus, original definition-event provenance, FOODON xref, both verbatim source
    attestations, counts/units and all 25 taxon entries are unchanged. The confirmed
    mixed Madin source-equivalence finding remains open under #1307; synonym repair
    does not establish a living-host interpretation for every source member.'
- assessment_id: PRESERVATION
  area: consistency
  topic: Identity, source evidence and native status preservation
  outcome: supported
  target_ids:
  - habitatmech:GOLD.02383c20a7
  evidence_ids:
  - PREVIOUS
  - REGRESSION
  summary: All original fields outside the explicit tested corrections are preserved.
    The entire current target was re-read. Native status is REVIEWED/UNGROUNDED; a
    saved review does not promote status or certify species occurrence.
  dimensions:
  - name: mapping_status
    value: REVIEWED
    definition: Native generated status, separate from scientific-review verdict
    evidence_ids:
    - PATCH
  - name: grounding_status
    value: UNGROUNDED
    definition: Native generated status, separate from scientific-review verdict
    evidence_ids:
    - PATCH
findings:
- issue_key: HM-ALGAE-001
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Mixed Madin category is merged as one living-host environment
  description: 'Pre-fix observation: The pinned Madin release contains 100 host_algae
    observations for 88 distinct IDs, including every displayed ID. Its conversion
    table maps 38 source strings, including decomposing scum, algal mats, algae-bearing
    sediment and lichen-colonized rock. This mixed scope is not unconditionally the
    living-host environment.'
  field_paths:
  - source_attestations
  - characteristic_taxa
  - curation_history
  evidence_ids:
  - PREVIOUS
  - PATCH
  - REGRESSION
  rule_id: HabitatMech:claim-scope-and-strict-broader-identity
  native_severity: major
  normalization_reason: The finding changes the scientific interpretation of an anatomical
    relation, identity or occurrence claim, rather than style. Provisional findings
    require original source evidence before correction.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1307
  finding_id: F1
  target_ids:
  - habitatmech:GOLD.02383c20a7
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T005332Z-algae-record
    finding_id: F1
  disposition_reason: This distinct confirmed finding remains unresolved; the scoped
    anatomy or synonym correction does not establish the missing source-equivalence
    or explicit mapping-endpoint contract.
- issue_key: gold-02383c20a7-host-name-exact-synonym
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Organism-group name is an exact synonym of its environment
  description: 'Pre-fix observation: Algae denotes the organism group and should not
    be an exact synonym of its associated environment.'
  field_paths:
  - synonyms
  evidence_ids:
  - PREVIOUS
  - PATCH
  - REGRESSION
  rule_id: HabitatMech:claim-scope-and-strict-broader-identity
  native_severity: major
  normalization_reason: The finding changes the scientific interpretation of an anatomical
    relation, identity or occurrence claim, rather than style. Provisional findings
    require original source evidence before correction.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/curate/definitions.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  finding_id: F2
  target_ids:
  - habitatmech:GOLD.02383c20a7
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T005332Z-algae-record
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2149
  disposition_reason: 'The authored Algae exact synonym is removed from the maintained
    term request. The existing organism xref guard prevents automatic reintroduction.
    Definition, genus, original definition-event provenance, FOODON xref, both verbatim
    source attestations, counts/units and all 25 taxon entries are unchanged. The
    confirmed mixed Madin source-equivalence finding remains open under #1307; synonym
    repair does not establish a living-host interpretation for every source member.'
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.02383c20a7
  description: Reassess the Madin SAME_AS decision using original observation contexts.
    Preserve supported thallus/coculture associations, separate material/community
    contexts, and remove the host-name exact synonym from the authored term request
    while preserving the source label in provenance. The existing annotation-correction
    table only handles ontology synonyms, so do not misuse it for this curated synonym;
    a new typed authored-synonym capability would need its own design. Review the
    eight unrouted parameter rows only after source scope is resolved; do not attach
    them by lexical match.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/curate/definitions.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Resolve source scope and relation endpoints with inspected primary or original
    source evidence; retain explicit uncertainty until then.
  - Make any separately authorized correction in maintained inputs, append native
    history, run just seed and inspect affected just seed-canary output before regeneration.
  - Add focused regressions for the supported and rejected scopes; run strict/schema,
    provenance, history, corpus reproduction, causal, term-request and configured
    label gates, followed by just qc.
  - Inspect actual downstream mappings and generated pages/redirects after any identity
    or relation change; deterministic record checks do not certify SSSOM/KGX compatibility.
  - Save an immutable successor with these exact finding identities; do not rewrite
    this observation or promote scientific status by review alone.
limitations:
- Same-agent scientific reassessment, not independent approval.
- Original source-member evidence remains unavailable; no full-corpus, species-occurrence
  or SSSOM/KGX readiness certification.
- Configured label correspondence retains unsupported-prefix skips. Final retained-archive
  and protected publication gates are pending at this immutable observation.
- 'Unresolved confirmed major finding(s): HM-ALGAE-001.'
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T005332Z-algae-record
  relationship: Exact finding remediation successor retaining every affected predecessor
    target
notes:
- Source inputs were freshly captured with the native inspector and checked against
  exact committed blobs and current disk bytes. Retain this off-main input commit
  with an annotated provenance tag before squash and branch deletion.
- The original definition date, author and generated definition history of Algae were
  deliberately preserved; the new session history records the synonym-only correction.
  No historic review/history file was rewritten.
- Adversarial rendered-page inspection found a semicolon incorrectly included in the
  new issue 2148 href. The new publication regression reproduced the defect (one expected
  failure). Issue 2152 corrects the maintained note and regenerates the record/page,
  followed by fresh passing checks. Earlier temporary captures were superseded by
  a fresh native inspection and reassessment, not silently rehashed. Scientific fields
  and all 3208 semantic input rows remain unchanged by this punctuation-only follow-up.
```
