# Scientific follow-up: Beef chop

- Review: 20261014T085720Z-beef_chop-followup
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T08:31:55.525048Z
- Finished UTC: 2026-10-14T08:57:20.006874Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The raw-qualified GOLD source now retains its native identity with generic beef chop as a broader parent, not exact identity. Raw meat remains a supported source genus, node 6425 and omitted organism counts are preserved, and the ITEM decision derives NARROW/REVIEWED. The shared source-attestation endpoint contract mismatch remains actionable under #1398; this record is not a scientific pass or SSSOM/KGX certification.

## Scope And Provenance

Full corrected record and exact predecessor disposition; original source-membership reconstruction remains outside established evidence.

Selection: Explicit correction follow-up, not a random sample or corpus-wide pass. Two linked surfaces: current native record and former generic identity mapping row, retained for exact finding lineage.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base ad47456f8bcac0d01f37b45beb3c34a3de0cc61f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.413b64dcc1 | data/habitats/food/beef_chop.yaml | generated | Beef chop (raw-qualified GOLD source) |
| FOODON:02020979 | curation/decisions.tsv # identifier=habitatmech:GOLD.413b64dcc1; object_id=FOODON:02020979; former exact mapping now GROUND_AS_PARENT | snapshot_row | Former generic-beef-chop identity claim, now only a broader mapping |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Executed 2026-10-14T08:31:56.654821Z to 2026-10-14T08:31:58.713930Z. No issues found |
| just validate-strict | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Executed 2026-10-14T08:31:58.714470Z to 2026-10-14T08:32:02.834609Z. uv run python scripts/validate_strict.py data/habitats/food/baby_formula.yaml data/habitats/food/bean.yaml data/habitats/food/beverage.yaml data/habitats/food/bread_food_product.yaml data/habitats/food/cereal_grain_food_product.yaml data/habitats/food/beef_chop.yaml<br>Validating 6 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      6<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Executed 2026-10-14T08:32:02.835092Z to 2026-10-14T08:32:09.194384Z. No issues found<br>654 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Executed 2026-10-14T08:32:09.194898Z to 2026-10-14T08:32:09.690662Z. provenance current: 14 committed inventories, 2 GOLD sources |
| just verify-corpus | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Executed 2026-10-14T08:32:09.691186Z to 2026-10-14T08:32:26.552550Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| just validate-causal-all | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Executed 2026-10-14T08:32:26.553540Z to 2026-10-14T08:32:33.245942Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| just term-requests-check | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Executed 2026-10-14T08:32:33.246762Z to 2026-10-14T08:32:52.942934Z. term-request table is current (109 terms) |
| just validate-products | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Executed 2026-10-14T08:32:52.943563Z to 2026-10-14T08:33:41.661935Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1177<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2058<br><br>✅ All id↔label pairs correspond. |
| uv run | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Executed 2026-10-14T08:33:41.662615Z to 2026-10-14T08:35:02.440376Z. ........................................................................ [ 86%]<br>...........                                                              [100%]<br>83 passed in 79.73s (0:01:19) |
| Exact corrected-base authoritative hosted QC | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Success on the exact captured corrected base; post-save archive and final PR gates remain required. |
| Historical pre-formatting CI failure | failed | False | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | The inspected preliminary hosted QC run failed at lint on 2026-10-14T08:33:19Z. Five fixture lines exceeded 110 characters. This is an explicit superseded baseline failure, not a current required gate. The five lines were wrapped, ruff check passed locally, 83 focused tests passed again, and the later required full QC passed. |
| Corrected local lint | passed | True | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | All checks passed after the five fixture-line wraps; the exact test-hash reassessment is retained in notes. |
| Original source-member reconstruction | unavailable | False | habitatmech:GOLD.413b64dcc1, FOODON:02020979 | Original dumps and member crosswalks remain unavailable; six GOLD study pages returned HTTP 403 during the predecessor evidence pass. No new access or absence claim is inferred. |

## Scientific And Domain Assessments

### Exact finding correction and source preservation

grounding: supported. Targets: habitatmech:GOLD.413b64dcc1, FOODON:02020979.

The raw-qualified GOLD source now retains its native identity with generic beef chop as a broader parent, not exact identity. Raw meat remains a supported source genus, node 6425 and omitted organism counts are preserved, and the ITEM decision derives NARROW/REVIEWED. The shared source-attestation endpoint contract mismatch remains actionable under #1398; this record is not a scientific pass or SSSOM/KGX certification.

### Claim scope and optional biological fields

evidence: supported. Targets: habitatmech:GOLD.413b64dcc1, FOODON:02020979.

Re-read the entire current record, every attestation and event. Frozen occurrence-edge counts remain distinct from later biosamples and complete-triad samples. No taxon, parameter, causal, citation, discussion or dataset claim is introduced. Generic class definition and exact synonyms are not copied as defining assertions of a newly minted source. The raw qualification is carried by the source path and Raw meat genus; FoodOn explicitly distinguishes raw and generic chops. The regenerated seed event describes the new identity; the previous generic seed remains documented in Git and the immutable predecessor, not claimed byte-identical.

### Unresolved shared mapping endpoint contract

representation: concern. Targets: habitatmech:GOLD.413b64dcc1.

The raw source and record identifier are the same mint, but the emitted predicate is skos:narrowMatch and the enum description compares record versus source. The implemented narrow relationship instead concerns generic beef chop as parent. This is another concrete witness of shared #1398, not a new unrelated predicate-direction issue.

## Findings

### F1: Raw-qualified source is exactly mapped to generic beef chop

major / resolved / confirmed; issue key: foodon-02020979-raw-source-generic-identity.

The source path explicitly qualifies Beef chop with Raw meat. FOODON:02020979 is generic, while the inspected ontology explicitly distinguishes FOODON:02020980 beef chop (raw) as its subclass. Lexical leaf identity loses the raw qualification and incorrectly makes the generic chop a kind of Raw meat. Exact ontology synonyms beef meat chop and cow chop are independently supported.

Disposition: The raw-qualified GOLD source now retains its native identity with generic beef chop as a broader parent, not exact identity. Raw meat remains a supported source genus, node 6425 and omitted organism counts are preserved, and the ITEM decision derives NARROW/REVIEWED. The shared source-attestation endpoint contract mismatch remains actionable under #1398; this record is not a scientific pass or SSSOM/KGX certification.

### F2: Native NARROW output compares against an implicit ontology-parent endpoint

major / open / confirmed; issue key: gold-413b64dcc1-source-attestation-endpoints.

The raw source and record identifier are the same mint, but the emitted predicate is skos:narrowMatch and the enum description compares record versus source. The implemented narrow relationship instead concerns generic beef chop as parent. This is another concrete witness of shared #1398, not a new unrelated predicate-direction issue.

## Recommended Actions And Acceptance Checks

### A2

Resolve shared #1398 with explicit source-to-record and record-to-ontology-parent endpoints; preserve the raw source identity and genuine genera. Do not patch this generated record or swap all broad/narrow predicates.

- Reconcile schema descriptions, all narrow routes and actual consumers with endpoint-specific regressions.
- Audit emitted SSSOM/KGX triples against current kg-microbe modeling; native QC alone is not conformance proof.
- Save a successor retaining this exact issue key and occurrence after source-preserving regeneration and full gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| CURRENT | data/habitats/food/beef_chop.yaml; Entire corrected YAML and source attestation | supports | The raw-qualified GOLD source now retains its native identity with generic beef chop as a broader parent, not exact identity. Raw meat remains a supported source genus, node 6425 and omitted organism counts are preserved, and the ITEM decision derives NARROW/REVIEWED. The shared source-attestation endpoint contract mismatch remains actionable under #1398; this record is not a scientific pass or SSSOM/KGX certification. |
| OWNERS | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; tests/test_food_review_fixes.py; curation/decisions.tsv:2 identifier=habitatmech:GOLD.413b64dcc1 | supports | Inspected complete maintained rows, six append-only histories and full before/after corpus regression. Only five shared identities change parent/history, and only generic beef chop is replaced by its source mint. Independent source-count and status assertions are pinned. |
| PREVIOUS | reviews/structured/20261014T082137Z-beef_chop/review.yaml | context_only | Read immutable predecessor and its exact findings, source receipts and limitations. Retain every predecessor target on successor dispositions; the old beef identity is represented by its maintained mapping claim, not falsely presented as a live record. |
| QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38536352907 | supports | Verified authoritative hosted QC succeeded on exact current commit ad47456f8bcac0d01f37b45beb3c34a3de0cc61f. Scientific inputs were hashed before assessment and proved unchanged after map/site publication. This run predates the new successor bundles. |
| RAW | reviews/structured/20261014T082137Z-beef_chop/review.yaml; evidence_id=RAW; historical source and decision-row snapshot | supports | Historical baseline row snapshot, not current decision-table line numbers. Frozen raw tables are unchanged; current curation rows are located in OWNERS. Inspected exact-key structured rows, distinguishing parent and child matches from the own source path. {"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12", "decision": "CONFIRM_UNGROUNDED", "grounding_status": "", "identifier": "habitatmech:GOLD.43005e4de2", "notes": "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.", "object_id": "", "object_label": "", "relation": "", "review_depth": "CLASS"}, "row": 456}], "data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Engineered &gt; Food production &gt; Meat products &gt; Raw meat &gt; Beef chop", "depth": "5", "ecosystem": "Engineered", "ecosystem_category": "Food production", "ecosystem_subtype": "Raw meat", "ecosystem_type": "Meat products", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6425", "leaf_label": "Beef chop", "organism_count": "0", "specific_ecosystem": "Beef chop", "study_count": "0", "total_assertions": "0"}, "row": 1300}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "17", "canonical_path": "Engineered &gt; Food production &gt; Meat products &gt; Raw meat &gt; Beef chop", "ecosystem_path_id": "6425"}, "row": 534}], "data/raw/gold_path_triads.tsv": [{"data": {"canonical_path": "Engineered &gt; Food production &gt; Meat products &gt; Raw meat &gt; Beef chop", "distinct_terms": "2", "samples": "2", "slot": "broad", "studies": "1", "studies_agreeing": "1", "top_label": "hygienic food production area", "top_share": "0.50", "top_term": "ENVO:03501318"}, "row": 98}, {"data": {"canonical_path": "Engineered &gt; Food production &gt; Meat products &gt; Raw meat &gt; Beef chop", "distinct_terms": "2", "samples": "2", "slot": "local", "studies": "1", "studies_agreeing": "1", "top_label": "abattoir", "top_share": "0.50", "top_term": "ENVO:01000925"}, "row": 99}, {"data": {"canonical_path": "Engineered &gt; Food production &gt; Meat products &gt; Raw meat &gt; Beef chop", "distinct_terms": "2", "samples": "2", "slot": "medium", "studies": "1", "studies_agreeing": "1", "top_label": "meat processing plant", "top_share": "0.50", "top_term": "ENVO:03501297"}, "row": 100}], "data/raw/gold_studies.tsv": [{"data": {"path_count": "1", "paths": "Engineered &gt; Food production &gt; Meat products &gt; Raw meat &gt; Beef chop", "study_gold_id": "Gs0142293"}, "row": 2379}]} |
| RULES | docs/CURATION.md | supports | Applied identity, strict-superclass, MIxS roles, source units, optional-field and ITEM status rules with the local checklist. |
| TRANSFORM | src/habitatmech/seed.py; extract.py:extract_gold; seed.py:ingest_gold; scripts/extract_gold_biosamples.py:extract; scripts/aggregate_gold_triads.py:aggregate | supports | extract_gold counts occurs_in edges by subject prefix and collapses path nodes, not proven unique organisms. ingest_gold emits a positive ORGANISM count only and resolves immediate source-path parents separately. Bulk biosample rows and study path unions use a separate export; triads aggregate complete annotations only. |
| FOODON | https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl; FOODON:02020979 and all FoodOn parents; raw-chop, formula and grain candidate context | supports | Inspected typed synonyms, definitions and named parents in pinned official RDF/XML; SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf. This is a pinned ontology check, not an unbounded latest-release refresh. The source path explicitly qualifies Beef chop with Raw meat. FOODON:02020979 is generic, while the inspected ontology explicitly distinguishes FOODON:02020980 beef chop (raw) as its subclass. Lexical leaf identity loses the raw qualification and incorrectly makes the generic chop a kind of Raw meat. Exact ontology synonyms beef meat chop and cow chop are independently supported. |
| GOLD_ACCESS | https://gold.jgi.doe.gov/ | context_only | Direct retrieval of the six relevant study pages returned HTTP 403; no study contents were inferred. Receipts: {"Gs0142293": {"accessed_at": "2026-10-14T08:11:39.570835Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0142293"}, "Gs0150300": {"accessed_at": "2026-10-14T08:11:39.785085Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150300"}, "Gs0150660": {"accessed_at": "2026-10-14T08:11:39.830086Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150660"}, "Gs0153740": {"accessed_at": "2026-10-14T08:11:39.869363Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153740"}, "Gs0153816": {"accessed_at": "2026-10-14T08:11:39.925031Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153816"}, "Gs0154282": {"accessed_at": "2026-10-14T08:11:39.962586Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}} |
| ENDPOINTS | src/habitatmech/schema/habitatmech.yaml; src/habitatmech/seed.py; SourceAttestation.mapping_predicate; GroundingStatusEnum; seed._decided GROUND_AS_PARENT | refutes | The schema defines source concept -&gt; record identifier and omission when they are identical. GROUND_AS_PARENT retains the exact source mint but emits skos:narrowMatch from NARROW, comparing the source to its ontology genus instead. The generic parent is supported; the implicit endpoint and status description are inconsistent. Inspected existing open GitHub #1398, whose acceptance requires coordinated schema/generator/consumer reconciliation; no formal SKOS inconsistency or universal predicate swap is asserted. |

## Limits And Additional Notes

- Same-agent reassessment and adversarial review, not independent approval.
- Original source membership remains unavailable; no new member-level habitat occurrence or latest ontology refresh is certified.
- Only the exact predecessor findings receive the explicit dispositions shown. Bread production identity (#2044) remains open; broader Food production and Meat products identities are outside this fix.
- No SSSOM/KGX conformance certification; shared modeling issues remain outside this review.
- Native label correspondence retains configured exceptions and unsupported-prefix skips. Hosted QC predates these successor files; post-save archive and PR checks remain required.
- Initial corrected capture at d6e8268d931100ec3bc6db9bb0571754c7c43599; after map/site publication, reinspection at 2026-10-14T08:57:19.993469Z proved every inspected input hash unchanged before using the current base.
- Inspected the five fixture-line wraps required by the E501 lint failure; no test behavior or scientific input changed. Focused tests and lint were rerun. Test hash 569dbc4358da73df57f87a2404ee3a6a17136ad166bcc39dde6063f9c8242c1d -&gt; bc798ddc7027b09b4300ef507ae62eea8037d25ce0b7a623ef605ec86ef1e94f.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T085720Z-beef_chop-followup
kind: batch
repository: CultureBotAI/HabitatMech
title: 'Scientific follow-up: Beef chop'
started_at: '2026-10-14T08:31:55.525048Z'
finished_at: '2026-10-14T08:57:20.006874Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same agent participated in repository work; not independent
    approval.
skill: .claude/skills/curate-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: needs_curation
summary: 'The raw-qualified GOLD source now retains its native identity with generic
  beef chop as a broader parent, not exact identity. Raw meat remains a supported
  source genus, node 6425 and omitted organism counts are preserved, and the ITEM
  decision derives NARROW/REVIEWED. The shared source-attestation endpoint contract
  mismatch remains actionable under #1398; this record is not a scientific pass or
  SSSOM/KGX certification.'
source:
  git_revision: ad47456f8bcac0d01f37b45beb3c34a3de0cc61f
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
    sha256: 45321d0e994aa54fa4b80a943c9ce28e174d9334e59a5bde2a8a02826055106f
    role: target
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: e31f574d4a1e65f5ff97a7a1b675c4d1179b3e2fe048dc0de9c3e34b9388cf0f
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
    sha256: a28af6ce3b1406cf8fe7d05c66c0a2e1378ea21910c742a281cc9bf81e9ccd86
    role: context
  - path: data/habitats/food/baby_formula.yaml
    sha256: 59226704fcb17da0144f9915f54e54d78161ecdbdc720f6497b72d4830677bba
    role: context
  - path: data/habitats/food/bean.yaml
    sha256: 1211b504ca7c076ca73de9b25032ba6dc2618dd3f756530f75eace34d23e9f99
    role: context
  - path: data/habitats/food/beef_chop.yaml
    sha256: b8254ef3a766d2260f2d65da11284b5ad089c7d7b72d0bf5635b2708abc19e92
    role: target
  - path: data/habitats/food/beverage.yaml
    sha256: b5d70ad5849c891fd01efe9f27abe3e6df8a74abc70fc212482dcdc61c842003
    role: context
  - path: data/habitats/food/bread.yaml
    sha256: 109e90fe77a77741c93ff5c4fc9c753dcd16c987c3cc527c36f544944ce719bf
    role: context
  - path: data/habitats/food/bread_food_product.yaml
    sha256: 1e9faea17ec694e01ed21c618fda4056a05499d9070586dde3b37f5f9aa384d1
    role: context
  - path: data/habitats/food/butchery_cut_of_beef.yaml
    sha256: 837d45cc3f7fb377199b254fffe21a366d1312b13e5fd2232b987c136ffc33bb
    role: context
  - path: data/habitats/food/cereal_grain_food_product.yaml
    sha256: 61850a597755f4c086491d128832e504cd4fbb76373f078cb5342c28e8ccba6c
    role: context
  - path: data/habitats/food/food_production.yaml
    sha256: b0fce7af2cc321a0979ce4d3bfec5e2d4383410ae8e62172b006073afb783ab7
    role: context
  - path: data/habitats/food/mammalian_meat_food_product.yaml
    sha256: fab8fbd8e3352bfe93aefac2761dded407774e918244be3e6b8a87ae45ec27b5
    role: context
  - path: data/habitats/food/raw_meat.yaml
    sha256: e45e1d71102c32bc410ff08a2175fcd645de883da0d4682f8acfaf0b04b0564d
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
  - path: history/mappings/baby_formula/2026-10-14T082837Z-codex-gpt-5-52d2c4.yaml
    sha256: 7dbea5a334ec4e80713021c68cf725f6f86b6e2b23710b0177b6524210c743bd
    role: context
  - path: history/mappings/bean/2026-10-14T082839Z-codex-gpt-5-ce631c.yaml
    sha256: e17929f33b7c9e0b956ae320cf5c8aa3e3796044001ba8d8f0becc6ce392e02c
    role: context
  - path: history/mappings/beef_chop/2026-10-14T082844Z-codex-gpt-5-c9f0de.yaml
    sha256: fa38dbafcbed8f45a52cc239f00a54330a106905d816bd5c29eeea130deac763
    role: context
  - path: history/mappings/beverage/2026-10-14T082840Z-codex-gpt-5-094a2c.yaml
    sha256: 8f5a850a500d2431469c3581ac93d324ccd6f3e2b795fc94affa060ffc272a5d
    role: context
  - path: history/mappings/bread_food_product/2026-10-14T082842Z-codex-gpt-5-4bf705.yaml
    sha256: f27bcbcea5697d473a91528af6131f197c15a2076bf8fe9b60f3d1565787b9c8
    role: context
  - path: history/mappings/cereal_grain_food_product/2026-10-14T082843Z-codex-gpt-5-f8fcc5.yaml
    sha256: 5823cb106d663f25d9110ceb741b28d5963204b1089c01cfda082cc36734f7a0
    role: context
  - path: history/mappings/foodon_beverage_pastry_scope/2026-10-08T034738Z-codex-4bb239.yaml
    sha256: 3b55dd188863916f4fda7a1813547e08473f124cbb0188aba284e700a1d48ae9
    role: context
  - path: history/mappings/grains_grain_products/2026-09-09T030500Z-claude-code-1b8d5a.yaml
    sha256: fd799709156f489929dfdb3d7cc3cc4dc779a51aa91665b7e85432941391b2c5
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260929T030651Z-food_production.md
    sha256: 8e8b30e0bfe4849c96aec02bec10e0ef0970da582375e62f1068e9446a1cae4a
    role: context
  - path: reviews/structured/20261014T082137Z-beef_chop/review.yaml
    sha256: 9f2c5818757b529cb0c6b1d8d41172935ee6e77c57727c7c05f93a61f8e5666a
    role: context
  - path: scripts/aggregate_gold_triads.py
    sha256: 0e25179dbecd7c73cbedd99a0ae44e56e4992afb9e1ec02d2411439f643b8e54
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
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
  - path: tests/test_food_review_fixes.py
    sha256: bc798ddc7027b09b4300ef507ae62eea8037d25ce0b7a623ef605ec86ef1e94f
    role: context
  - path: tests/test_ontology_labels.py
    sha256: 53b6a1abb31be450184e330432600703dbcff1e270e66b876f8c4851599762f3
    role: context
targets:
- target_id: habitatmech:GOLD.413b64dcc1
  path: data/habitats/food/beef_chop.yaml
  label: Beef chop (raw-qualified GOLD source)
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_triads.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_studies.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained curation or source owner; never hand-edit generated YAML
  record_class: HabitatRecord
- target_id: FOODON:02020979
  path: curation/decisions.tsv
  selector: identifier=habitatmech:GOLD.413b64dcc1; object_id=FOODON:02020979; former
    exact mapping now GROUND_AS_PARENT
  label: Former generic-beef-chop identity claim, now only a broader mapping
  kind: snapshot_row
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_triads.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_studies.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained curation or source owner; never hand-edit generated YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained curation or source owner; never hand-edit generated YAML
scope:
  description: Full corrected record and exact predecessor disposition; original source-membership
    reconstruction remains outside established evidence.
  selection: 'Explicit correction follow-up, not a random sample or corpus-wide pass.
    Two linked surfaces: current native record and former generic identity mapping
    row, retained for exact finding lineage.'
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
checks:
- check_id: C5
  name: just validate
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/food/beef_chop.yaml
  exit_code: 0
  summary: Executed 2026-10-14T08:31:56.654821Z to 2026-10-14T08:31:58.713930Z. No
    issues found
- check_id: C6
  name: just validate-strict
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/food/baby_formula.yaml data/habitats/food/bean.yaml data/habitats/food/beverage.yaml
    data/habitats/food/bread_food_product.yaml data/habitats/food/cereal_grain_food_product.yaml
    data/habitats/food/beef_chop.yaml
  exit_code: 0
  summary: "Executed 2026-10-14T08:31:58.714470Z to 2026-10-14T08:32:02.834609Z. uv\
    \ run python scripts/validate_strict.py data/habitats/food/baby_formula.yaml data/habitats/food/bean.yaml\
    \ data/habitats/food/beverage.yaml data/habitats/food/bread_food_product.yaml\
    \ data/habitats/food/cereal_grain_food_product.yaml data/habitats/food/beef_chop.yaml\n\
    Validating 6 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      6\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
- check_id: C7
  name: just validate-history
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  summary: 'Executed 2026-10-14T08:32:02.835092Z to 2026-10-14T08:32:09.194384Z. No
    issues found

    654 history record(s) valid against src/habitatmech/schema/history.yaml'
- check_id: C8
  name: just provenance-check
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  summary: 'Executed 2026-10-14T08:32:09.194898Z to 2026-10-14T08:32:09.690662Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
- check_id: C9
  name: just verify-corpus
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  summary: "Executed 2026-10-14T08:32:09.691186Z to 2026-10-14T08:32:26.552550Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
- check_id: C10
  name: just validate-causal-all
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  summary: Executed 2026-10-14T08:32:26.553540Z to 2026-10-14T08:32:33.245942Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
- check_id: C11
  name: just term-requests-check
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  summary: Executed 2026-10-14T08:32:33.246762Z to 2026-10-14T08:32:52.942934Z. term-request
    table is current (109 terms)
- check_id: C12
  name: just validate-products
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  summary: "Executed 2026-10-14T08:32:52.943563Z to 2026-10-14T08:33:41.661935Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1177\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2058\n\n✅ All id↔label\
    \ pairs correspond."
- check_id: C13
  name: uv run
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run pytest -q tests/test_food_review_fixes.py
    tests/test_ontology_labels.py tests/test_gold_parent_exclusions.py
  exit_code: 0
  summary: 'Executed 2026-10-14T08:33:41.662615Z to 2026-10-14T08:35:02.440376Z. ........................................................................
    [ 86%]

    ...........                                                              [100%]

    83 passed in 79.73s (0:01:19)'
- check_id: QC
  name: Exact corrected-base authoritative hosted QC
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: gh run view 38536352907 --json headSha,status,conclusion,url
  exit_code: 0
  summary: Success on the exact captured corrected base; post-save archive and final
    PR gates remain required.
  evidence_ids:
  - QC
- check_id: PRELIMINARY_QC
  name: Historical pre-formatting CI failure
  status: failed
  required: false
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: uv run python scripts/run_qc.py
  exit_code: 1
  scope_note: Hosted run https://github.com/CultureBotAI/HabitatMech/actions/runs/38535542576
    at d6e8268d931100ec3bc6db9bb0571754c7c43599, not the final corrected base.
  summary: The inspected preliminary hosted QC run failed at lint on 2026-10-14T08:33:19Z.
    Five fixture lines exceeded 110 characters. This is an explicit superseded baseline
    failure, not a current required gate. The five lines were wrapped, ruff check
    passed locally, 83 focused tests passed again, and the later required full QC
    passed.
- check_id: LINT
  name: Corrected local lint
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache uv run ruff check .
  exit_code: 0
  summary: All checks passed after the five fixture-line wraps; the exact test-hash
    reassessment is retained in notes.
- check_id: MEMBERS
  name: Original source-member reconstruction
  status: unavailable
  required: false
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  summary: Original dumps and member crosswalks remain unavailable; six GOLD study
    pages returned HTTP 403 during the predecessor evidence pass. No new access or
    absence claim is inferred.
  evidence_ids:
  - GOLD_ACCESS
evidence:
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/food/beef_chop.yaml
  accessed_at: '2026-10-14T08:57:19.993469Z'
  locator: Entire corrected YAML and source attestation
  support: supports
  summary: 'The raw-qualified GOLD source now retains its native identity with generic
    beef chop as a broader parent, not exact identity. Raw meat remains a supported
    source genus, node 6425 and omitted organism counts are preserved, and the ITEM
    decision derives NARROW/REVIEWED. The shared source-attestation endpoint contract
    mismatch remains actionable under #1398; this record is not a scientific pass
    or SSSOM/KGX certification.'
- evidence_id: OWNERS
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; tests/test_food_review_fixes.py
  accessed_at: '2026-10-14T08:57:19.993469Z'
  support: supports
  summary: Inspected complete maintained rows, six append-only histories and full
    before/after corpus regression. Only five shared identities change parent/history,
    and only generic beef chop is replaced by its source mint. Independent source-count
    and status assertions are pinned.
  locator: curation/decisions.tsv:2 identifier=habitatmech:GOLD.413b64dcc1
- evidence_id: PREVIOUS
  kind: prior_review
  reference: reviews/structured/20261014T082137Z-beef_chop/review.yaml
  accessed_at: '2026-10-14T08:57:19.993469Z'
  support: context_only
  summary: Read immutable predecessor and its exact findings, source receipts and
    limitations. Retain every predecessor target on successor dispositions; the old
    beef identity is represented by its maintained mapping claim, not falsely presented
    as a live record.
- evidence_id: QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38536352907
  accessed_at: '2026-10-14T08:57:19.993469Z'
  support: supports
  summary: Verified authoritative hosted QC succeeded on exact current commit ad47456f8bcac0d01f37b45beb3c34a3de0cc61f.
    Scientific inputs were hashed before assessment and proved unchanged after map/site
    publication. This run predates the new successor bundles.
- evidence_id: RAW
  kind: prior_review
  reference: reviews/structured/20261014T082137Z-beef_chop/review.yaml
  summary: 'Historical baseline row snapshot, not current decision-table line numbers.
    Frozen raw tables are unchanged; current curation rows are located in OWNERS.
    Inspected exact-key structured rows, distinguishing parent and child matches from
    the own source path. {"curation/decisions.tsv": [{"data": {"category": "", "curator":
    "claude-opus-5", "date": "2026-08-12", "decision": "CONFIRM_UNGROUNDED", "grounding_status":
    "", "identifier": "habitatmech:GOLD.43005e4de2", "notes": "Class-level sweep (see
    docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate.", "object_id": "", "object_label":
    "", "relation": "", "review_depth": "CLASS"}, "row": 456}], "data/raw/gold_ecosystem_paths.tsv":
    [{"data": {"biosample_count": "0", "canonical_path": "Engineered > Food production
    > Meat products > Raw meat > Beef chop", "depth": "5", "ecosystem": "Engineered",
    "ecosystem_category": "Food production", "ecosystem_subtype": "Raw meat", "ecosystem_type":
    "Meat products", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6425",
    "leaf_label": "Beef chop", "organism_count": "0", "specific_ecosystem": "Beef
    chop", "study_count": "0", "total_assertions": "0"}, "row": 1300}], "data/raw/gold_path_biosamples.tsv":
    [{"data": {"biosample_count": "17", "canonical_path": "Engineered > Food production
    > Meat products > Raw meat > Beef chop", "ecosystem_path_id": "6425"}, "row":
    534}], "data/raw/gold_path_triads.tsv": [{"data": {"canonical_path": "Engineered
    > Food production > Meat products > Raw meat > Beef chop", "distinct_terms": "2",
    "samples": "2", "slot": "broad", "studies": "1", "studies_agreeing": "1", "top_label":
    "hygienic food production area", "top_share": "0.50", "top_term": "ENVO:03501318"},
    "row": 98}, {"data": {"canonical_path": "Engineered > Food production > Meat products
    > Raw meat > Beef chop", "distinct_terms": "2", "samples": "2", "slot": "local",
    "studies": "1", "studies_agreeing": "1", "top_label": "abattoir", "top_share":
    "0.50", "top_term": "ENVO:01000925"}, "row": 99}, {"data": {"canonical_path":
    "Engineered > Food production > Meat products > Raw meat > Beef chop", "distinct_terms":
    "2", "samples": "2", "slot": "medium", "studies": "1", "studies_agreeing": "1",
    "top_label": "meat processing plant", "top_share": "0.50", "top_term": "ENVO:03501297"},
    "row": 100}], "data/raw/gold_studies.tsv": [{"data": {"path_count": "1", "paths":
    "Engineered > Food production > Meat products > Raw meat > Beef chop", "study_gold_id":
    "Gs0142293"}, "row": 2379}]}'
  accessed_at: '2026-10-14T08:21:37.137628Z'
  support: supports
  locator: evidence_id=RAW; historical source and decision-row snapshot
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md
  summary: Applied identity, strict-superclass, MIxS roles, source units, optional-field
    and ITEM status rules with the local checklist.
  accessed_at: '2026-10-14T08:21:37.137628Z'
  support: supports
- evidence_id: TRANSFORM
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: extract_gold counts occurs_in edges by subject prefix and collapses path
    nodes, not proven unique organisms. ingest_gold emits a positive ORGANISM count
    only and resolves immediate source-path parents separately. Bulk biosample rows
    and study path unions use a separate export; triads aggregate complete annotations
    only.
  accessed_at: '2026-10-14T08:21:37.137628Z'
  support: supports
  locator: extract.py:extract_gold; seed.py:ingest_gold; scripts/extract_gold_biosamples.py:extract;
    scripts/aggregate_gold_triads.py:aggregate
- evidence_id: FOODON
  kind: database
  reference: https://raw.githubusercontent.com/FoodOntology/foodon/cd73540243a84bcd511a500d9a497d12d7dc02f6/foodon.owl
  summary: Inspected typed synonyms, definitions and named parents in pinned official
    RDF/XML; SHA256 b897bf64c1b265c422db9ee01e1235c10c0b809e7f02326ef810a52068347edf.
    This is a pinned ontology check, not an unbounded latest-release refresh. The
    source path explicitly qualifies Beef chop with Raw meat. FOODON:02020979 is generic,
    while the inspected ontology explicitly distinguishes FOODON:02020980 beef chop
    (raw) as its subclass. Lexical leaf identity loses the raw qualification and incorrectly
    makes the generic chop a kind of Raw meat. Exact ontology synonyms beef meat chop
    and cow chop are independently supported.
  accessed_at: '2026-10-14T08:11:36.247630Z'
  support: supports
  locator: FOODON:02020979 and all FoodOn parents; raw-chop, formula and grain candidate
    context
- evidence_id: GOLD_ACCESS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'Direct retrieval of the six relevant study pages returned HTTP 403; no
    study contents were inferred. Receipts: {"Gs0142293": {"accessed_at": "2026-10-14T08:11:39.570835Z",
    "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0142293"},
    "Gs0150300": {"accessed_at": "2026-10-14T08:11:39.785085Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0150300"}, "Gs0150660":
    {"accessed_at": "2026-10-14T08:11:39.830086Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0150660"}, "Gs0153740": {"accessed_at":
    "2026-10-14T08:11:39.869363Z", "error": "HTTP Error 403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153740"},
    "Gs0153816": {"accessed_at": "2026-10-14T08:11:39.925031Z", "error": "HTTP Error
    403: Forbidden", "url": "https://gold.jgi.doe.gov/study?id=Gs0153816"}, "Gs0154282":
    {"accessed_at": "2026-10-14T08:11:39.962586Z", "error": "HTTP Error 403: Forbidden",
    "url": "https://gold.jgi.doe.gov/study?id=Gs0154282"}}'
  accessed_at: '2026-10-14T08:21:37.137628Z'
  support: context_only
- evidence_id: ENDPOINTS
  kind: record_content
  reference: src/habitatmech/schema/habitatmech.yaml; src/habitatmech/seed.py
  locator: SourceAttestation.mapping_predicate; GroundingStatusEnum; seed._decided
    GROUND_AS_PARENT
  accessed_at: '2026-10-14T08:57:19.993469Z'
  support: refutes
  summary: 'The schema defines source concept -> record identifier and omission when
    they are identical. GROUND_AS_PARENT retains the exact source mint but emits skos:narrowMatch
    from NARROW, comparing the source to its ontology genus instead. The generic parent
    is supported; the implicit endpoint and status description are inconsistent. Inspected
    existing open GitHub #1398, whose acceptance requires coordinated schema/generator/consumer
    reconciliation; no formal SKOS inconsistency or universal predicate swap is asserted.'
assessments:
- assessment_id: FIX
  area: grounding
  topic: Exact finding correction and source preservation
  outcome: supported
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - FOODON
  - RULES
  - QC
  summary: 'The raw-qualified GOLD source now retains its native identity with generic
    beef chop as a broader parent, not exact identity. Raw meat remains a supported
    source genus, node 6425 and omitted organism counts are preserved, and the ITEM
    decision derives NARROW/REVIEWED. The shared source-attestation endpoint contract
    mismatch remains actionable under #1398; this record is not a scientific pass
    or SSSOM/KGX certification.'
- assessment_id: SCIENCE
  area: evidence
  topic: Claim scope and optional biological fields
  outcome: supported
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  evidence_ids:
  - CURRENT
  - RAW
  - TRANSFORM
  - FOODON
  summary: Re-read the entire current record, every attestation and event. Frozen
    occurrence-edge counts remain distinct from later biosamples and complete-triad
    samples. No taxon, parameter, causal, citation, discussion or dataset claim is
    introduced. Generic class definition and exact synonyms are not copied as defining
    assertions of a newly minted source. The raw qualification is carried by the source
    path and Raw meat genus; FoodOn explicitly distinguishes raw and generic chops.
    The regenerated seed event describes the new identity; the previous generic seed
    remains documented in Git and the immutable predecessor, not claimed byte-identical.
- assessment_id: ENDPOINTS
  area: representation
  topic: Unresolved shared mapping endpoint contract
  outcome: concern
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  evidence_ids:
  - CURRENT
  - ENDPOINTS
  - RULES
  summary: 'The raw source and record identifier are the same mint, but the emitted
    predicate is skos:narrowMatch and the enum description compares record versus
    source. The implemented narrow relationship instead concerns generic beef chop
    as parent. This is another concrete witness of shared #1398, not a new unrelated
    predicate-direction issue.'
findings:
- finding_id: F1
  issue_key: foodon-02020979-raw-source-generic-identity
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Raw-qualified source is exactly mapped to generic beef chop
  description: The source path explicitly qualifies Beef chop with Raw meat. FOODON:02020979
    is generic, while the inspected ontology explicitly distinguishes FOODON:02020980
    beef chop (raw) as its subclass. Lexical leaf identity loses the raw qualification
    and incorrectly makes the generic chop a kind of Raw meat. Exact ontology synonyms
    beef meat chop and cow chop are independently supported.
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  - FOODON:02020979
  field_paths:
  - identifier
  - grounding_status
  - parent_habitats
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained curation or source owner; never hand-edit generated YAML
  evidence_ids:
  - CURRENT
  - OWNERS
  - PREVIOUS
  - QC
  - FOODON
  - RULES
  rule_id: docs/CURATION.md; local record checklist
  native_severity: major
  normalization_reason: Unsupported identity scope or false strict superclass is a
    material semantic defect, not style; no original member-level population is asserted.
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261014T082137Z-beef_chop
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2043
  disposition_reason: 'The raw-qualified GOLD source now retains its native identity
    with generic beef chop as a broader parent, not exact identity. Raw meat remains
    a supported source genus, node 6425 and omitted organism counts are preserved,
    and the ITEM decision derives NARROW/REVIEWED. The shared source-attestation endpoint
    contract mismatch remains actionable under #1398; this record is not a scientific
    pass or SSSOM/KGX certification.'
- finding_id: F2
  issue_key: gold-413b64dcc1-source-attestation-endpoints
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Native NARROW output compares against an implicit ontology-parent endpoint
  description: 'The raw source and record identifier are the same mint, but the emitted
    predicate is skos:narrowMatch and the enum description compares record versus
    source. The implemented narrow relationship instead concerns generic beef chop
    as parent. This is another concrete witness of shared #1398, not a new unrelated
    predicate-direction issue.'
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  field_paths:
  - grounding_status
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - CURRENT
  - ENDPOINTS
  - RULES
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Shared source-to-record versus ontology-parent mapping contract owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Shared source-to-record versus ontology-parent mapping contract owner
  rule_id: SourceAttestation.mapping_predicate; GroundingStatusEnum
  native_severity: major
  normalization_reason: Material mapping endpoint ambiguity affects consumer interpretation,
    not style.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: A2
  description: 'Resolve shared #1398 with explicit source-to-record and record-to-ontology-parent
    endpoints; preserve the raw source identity and genuine genera. Do not patch this
    generated record or swap all broad/narrow predicates.'
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.413b64dcc1
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Shared source-to-record versus ontology-parent mapping contract owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Shared source-to-record versus ontology-parent mapping contract owner
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Reconcile schema descriptions, all narrow routes and actual consumers with endpoint-specific
    regressions.
  - Audit emitted SSSOM/KGX triples against current kg-microbe modeling; native QC
    alone is not conformance proof.
  - Save a successor retaining this exact issue key and occurrence after source-preserving
    regeneration and full gates.
limitations:
- Same-agent reassessment and adversarial review, not independent approval.
- Original source membership remains unavailable; no new member-level habitat occurrence
  or latest ontology refresh is certified.
- Only the exact predecessor findings receive the explicit dispositions shown. Bread
  production identity (#2044) remains open; broader Food production and Meat products
  identities are outside this fix.
- No SSSOM/KGX conformance certification; shared modeling issues remain outside this
  review.
- Native label correspondence retains configured exceptions and unsupported-prefix
  skips. Hosted QC predates these successor files; post-save archive and PR checks
  remain required.
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261014T082137Z-beef_chop
  relationship: Reassesses exact predecessor findings without rewriting the immutable
    original.
notes:
- Initial corrected capture at d6e8268d931100ec3bc6db9bb0571754c7c43599; after map/site
  publication, reinspection at 2026-10-14T08:57:19.993469Z proved every inspected
  input hash unchanged before using the current base.
- Inspected the five fixture-line wraps required by the E501 lint failure; no test
  behavior or scientific input changed. Focused tests and lint were rerun. Test hash
  569dbc4358da73df57f87a2404ee3a6a17136ad166bcc39dde6063f9c8242c1d -> bc798ddc7027b09b4300ef507ae62eea8037d25ce0b7a623ef605ec86ef1e94f.
tags:
- habitatmech
- record-review
- food
- followup
```
