# Scientific record review: aerial root

- Review: 20261014T214824Z-aerial_root
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-14T21:34:34Z
- Finished UTC: 2026-10-14T21:48:24Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

An aerial root is both a root and an aerial plant part. Its GOLD source path and one ORGANISM assertion agree with the frozen source. Counts for the separate mucilage child or generic Roots triads are not evidence for this source member.

## Scope And Provenance

One fully read HabitatRecord, all contributing source concepts and maintained owners, and claim-specific current source checks.

Selection: Next lexical unreviewed host-associated record after a census of 1,053 reviewed of 3,208 current IDs; one of 12 separately assessed targets, not a sample estimate.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 22120cf5ce86a96fbd23524bfcd7a00ed08b3106.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0001659 | data/habitats/host_associated/aerial_root.yaml | generated | aerial root |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native just validate | passed | True | BTO:0001659 | Actual execution 2026-10-14T21:34:44Z to 2026-10-14T21:34:46Z. No issues found |
| Native just validate-strict | passed | True | BTO:0001659 | Actual execution 2026-10-14T21:34:46Z to 2026-10-14T21:34:53Z. files scanned:      12<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| Native just validate-history | passed | True | BTO:0001659 | Actual execution 2026-10-14T21:34:53Z to 2026-10-14T21:35:03Z. No issues found<br>708 history record(s) valid against src/habitatmech/schema/history.yaml |
| Native just provenance-check | passed | True | BTO:0001659 | Actual execution 2026-10-14T21:35:03Z to 2026-10-14T21:35:04Z. provenance current: 14 committed inventories, 2 GOLD sources |
| Native just verify-corpus | passed | True | BTO:0001659 | Actual execution 2026-10-14T21:35:04Z to 2026-10-14T21:35:21Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/ |
| Native just validate-causal-all | passed | True | BTO:0001659 | Actual execution 2026-10-14T21:35:21Z to 2026-10-14T21:35:25Z. validated 32 causal-graph curation file(s) with 32 graph(s) |
| Native just term-requests-check | passed | True | BTO:0001659 | Actual execution 2026-10-14T21:35:25Z to 2026-10-14T21:35:45Z. term-request table is current (109 terms) |
| Native just validate-products | passed | True | BTO:0001659 | Actual execution 2026-10-14T21:35:45Z to 2026-10-14T21:36:46Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1175<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2060<br><br>✅ All id↔label pairs correspond. |
| Authoritative exact-base QC | passed | True | BTO:0001659 | Hosted native QC succeeded at the exact assessed base. New bundles require a separate archive check after saving. |
| Expression adapter applicability | not_applicable | False | BTO:0001659 | No gene, regulator or expression-dataset claim is present; module membership would not establish habitat anatomy or occurrence. |
| Original source-pair recovery | unavailable | False | BTO:0001659 | Frozen aggregate rows reproduce. Original GOLD specimens and PREGO pair-level references were not recovered; a backup search was permission-limited. This is not evidence of biological absence. |

## Scientific And Domain Assessments

### Exact anatomy, host and source meaning

identity: supported. Targets: BTO:0001659.

An aerial root is both a root and an aerial plant part. Its GOLD source path and one ORGANISM assertion agree with the frozen source. Counts for the separate mucilage child or generic Roots triads are not evidence for this source member.

### Frozen source counts and source-level decisions

provenance: supported. Targets: BTO:0001659.

Every contributing source and maintained decision was traced. GOLD zero counts omit count/unit; nonzero counts retain ORGANISM. PREGO TAXON counts are distinct taxa, not direct-assertion rows or prevalence. The source status is reproduced, not scientifically certified by reproduction.

### Strict genus versus source context

consistency: supported. Targets: BTO:0001659.

The false context parents are identified individually in findings; independent anatomical genera are retained. For adenoma, being a benign tumor is biologically valid: the parent record NOT_APPLICABLE flag alone does not refute that relation, so legacy HM-ADENOMA-002 is not adopted as a confirmed false-is-a finding. For aerial root, root and aerial part remain valid genera.

### Association versus characteristic presence and source-member evidence

evidence: not_applicable. Targets: BTO:0001659.

No retained taxon, environmental-parameter or causal-graph assertion needs filling merely for coverage. Source-path context is not mechanistic evidence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RECORD | data/habitats/host_associated/aerial_root.yaml | supports | An aerial root is both a root and an aerial plant part. Its GOLD source path and one ORGANISM assertion agree with the frozen source. Counts for the separate mucilage child or generic Roots triads are not evidence for this source member. Entire target YAML was read, including synonyms, source attestations, taxa and audit events. This observation assesses exact commit 22120cf5ce86a96fbd23524bfcd7a00ed08b3106. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md | supports | Parents are strictly broader, not contextual locations or whole systems. Host stage and organism classes are not habitat identity. ITEM review is distinct from lexical/CLASS seeding and scientific review does not itself promote mapping status. |
| SOURCE | data/raw/gold_ecosystem_paths.tsv; data/raw/prego_habitat_taxa.tsv; data/raw/prego_habitats.tsv; 1-based physical TSV row numbers in the attached row data | supports | Exact matching source rows, including source-parent/sibling context where matched: {"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Plants &gt; Roots &gt; Aerial root &gt; Mucilage", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Plants", "ecosystem_subtype": "Aerial root", "ecosystem_type": "Roots", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:7971", "leaf_label": "Mucilage", "organism_count": "31", "specific_ecosystem": "Mucilage", "study_count": "0", "total_assertions": "31"}, "row": 349}, {"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Plants &gt; Roots &gt; Aerial root", "depth": "4", "ecosystem": "Host-associated", "ecosystem_category": "Plants", "ecosystem_subtype": "Aerial root", "ecosystem_type": "Roots", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:7969&#124;gold.ecosystem:7970", "leaf_label": "Aerial root", "organism_count": "1", "specific_ecosystem": "", "study_count": "0", "total_assertions": "1"}, "row": 1108}], "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "1", "taxon_id": "NCBITaxon:10", "taxon_label": "Cellvibrio"}, "row": 1690}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "2", "taxon_id": "NCBITaxon:1004301", "taxon_label": "Flavihumibacter"}, "row": 1691}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "3", "taxon_id": "NCBITaxon:1005038", "taxon_label": "Fimbriimonas"}, "row": 1692}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "4", "taxon_id": "NCBITaxon:1011", "taxon_label": "Sporocytophaga"}, "row": 1693}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "5", "taxon_id": "NCBITaxon:102234", "taxon_label": "Cyanobacterium"}, "row": 1694}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "6", "taxon_id": "NCBITaxon:1032526", "taxon_label": "Pedosphaera"}, "row": 1695}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "7", "taxon_id": "NCBITaxon:1033", "taxon_label": "Afipia"}, "row": 1696}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "8", "taxon_id": "NCBITaxon:103728", "taxon_label": "Actinokineospora diospyrosa"}, "row": 1697}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "9", "taxon_id": "NCBITaxon:1042312", "taxon_label": "Armatimonadia"}, "row": 1698}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "10", "taxon_id": "NCBITaxon:1042314", "taxon_label": "Armatimonadaceae"}, "row": 1699}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "11", "taxon_id": "NCBITaxon:1060", "taxon_label": "Rhodobacter"}, "row": 1700}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "12", "taxon_id": "NCBITaxon:106589", "taxon_label": "Cupriavidus"}, "row": 1701}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "13", "taxon_id": "NCBITaxon:1071", "taxon_label": "Rhodopila globiformis"}, "row": 1702}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "14", "taxon_id": "NCBITaxon:1077257", "taxon_label": "Chthonomonadia"}, "row": 1703}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "15", "taxon_id": "NCBITaxon:1077264", "taxon_label": "Chthonomonadaceae"}, "row": 1704}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "16", "taxon_id": "NCBITaxon:1077265", "taxon_label": "Chthonomonas"}, "row": 1705}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "17", "taxon_id": "NCBITaxon:1090", "taxon_label": "Chlorobiota"}, "row": 1706}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "18", "taxon_id": "NCBITaxon:1107", "taxon_label": "Chloroflexus"}, "row": 1707}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "19", "taxon_id": "NCBITaxon:1117", "taxon_label": "Cyanobacteriota"}, "row": 1708}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "20", "taxon_id": "NCBITaxon:114248", "taxon_label": "Tepidimonas"}, "row": 1709}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "21", "taxon_id": "NCBITaxon:1147159", "taxon_label": "Ornithinibacillus scapharcae"}, "row": 1710}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "22", "taxon_id": "NCBITaxon:115336", "taxon_label": "Actinomadura vinacea"}, "row": 1711}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "23", "taxon_id": "NCBITaxon:1154584", "taxon_label": "Gaiellales"}, "row": 1712}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "24", "taxon_id": "NCBITaxon:1154585", "taxon_label": "Gaiellaceae"}, "row": 1713}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "25", "taxon_id": "NCBITaxon:1162", "taxon_label": "Nostocaceae"}, "row": 1714}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001658", "prego_score": "3", "rank": "1", "taxon_id": "NCBITaxon:693986", "taxon_label": "Methylobacterium oryzae CBMB20"}, "row": 2414}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "environmental_samples", "direct_assertion_count": "794", "max_prego_score": "4", "ontology": "BTO", "prego_id": "BTO:0001188", "prego_synonyms": "root", "taxon_count": "794"}, "row": 89}, {"data": {"biolink_category": "biolink:GrossAnatomicalStructure", "channels": "annotated_genomes_isolates", "direct_assertion_count": "1", "max_prego_score": "3", "ontology": "BTO", "prego_id": "BTO:0001658", "prego_synonyms": "aerial bodies&#124;aerial body&#124;aerial part&#124;aerial partic&#124;aerial parts&#124;aerial tissue&#124;aerial tissues", "taxon_count": "1"}, "row": 606}]}. Native source mints: habitatmech:GOLD.4c130cb0f9. Counts are source assertions with source-specific units, not prevalence. Original specimen-level joins were not recovered. |
| CURATION | curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv | supports | Matching maintained rows and parent context: {"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12", "decision": "GROUND", "grounding_status": "EXACT", "identifier": "habitatmech:GOLD.7c6b8ca314", "notes": "Plant roots as habitat. Grounded to PO, the authoritative plant anatomy ontology, now that it is vendored (#10). Re-grounded from BTO:0001188 to PO:0009005 now that PO is vendored (#10).", "object_id": "PO:0009005", "object_label": "root", "relation": "", "review_depth": "ITEM"}, "row": 744}, {"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-15", "decision": "GROUND", "grounding_status": "EXACT", "identifier": "habitatmech:ENVIRONMENTS_TABLE.58c6c839f8", "notes": "Co-attestor review (#12): kg-microbe's environments.csv maps 'host_plant_root-associated' to NCBITaxon:1, whose label is 'root' \u2014 the root of the TAXONOMY, not a plant root. The seeder's non-habitat-prefix guard drops the row, so the parameter bands for a real habitat were being lost silently rather than misattributed. PO:0009005 'root' is the term meant. Reported upstream.", "object_id": "PO:0009005", "object_label": "root", "relation": "", "review_depth": "ITEM"}, "row": 1634}]}. No habitat curation has been performed for this observation. |
| TRANSFORM | src/habitatmech/seed.py; src/habitatmech/extract.py; src/habitatmech/schema/habitatmech.yaml; extract_prego; ingest_prego; CharacteristicTaxon; GOLD parent generation | supports | PREGO preserves original source-term attestations/taxa when its emitted identity is redirected. Extraction keeps top 25 distinct taxa by maximum score; direct_assertion_count counts evidence rows, not distinct taxa. CharacteristicTaxon entries are observational unless is_characteristic is explicitly asserted. GOLD immediate source parents are separate from ontology and decision parents. |
| SEARCH | curation/; history/; research/; reports/; data/raw/; build/; reviews/ | supports | Bounded ignored-inclusive search at 2026-10-14T21:34:59Z. All structured findings were scanned for these exact target IDs and none supplied a structured predecessor. Original PREGO transformed nodes/edges were not recovered at the manifest path; one backup directory was inaccessible, so no global absence is claimed. |
| LEGACY | reports/yaml_record_review/20260923T172735Z-aerial_root.md | context_only | Historical Findings section and verdict reassessed. This is an ad hoc report without structured occurrence IDs, not an independent scientific authority. Stable legacy issue keys are retained where present; no previous_occurrences are invented. |
| BASE_QC | https://github.com/CultureBotAI/HabitatMech/actions/runs/38638089409 | context_only | Authoritative Build and test succeeded on exact base 22120cf5ce86a96fbd23524bfcd7a00ed08b3106. This predates the newly saved bundles and does not substitute for their archive check. |
| TERM0 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001188; obo_id, label, description, obo_synonym | supports | Current BTO:0001188 resolves to root; obsolete=False. Definition and synonym metadata inspected; ontology hierarchy alone is not proof that a contextual parent is a biological genus. Retrieval: {"accessed_at": "2026-10-14T21:35:06Z", "final_url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001188", "sha256": "bad0d042b0bf734173f028a9a68be56234a3192e799004966dd5283a9e421dc3", "status": 200, "url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001188"}. |
| TERM1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001658; obo_id, label, description, obo_synonym | supports | Current BTO:0001658 resolves to aerial part; obsolete=False. Definition and synonym metadata inspected; ontology hierarchy alone is not proof that a contextual parent is a biological genus. Retrieval: {"accessed_at": "2026-10-14T21:35:09Z", "final_url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001658", "sha256": "3d3d6c1e9fd72ac990cdbf87c6d2a04efc55b07550175ae1f9e62f918d273641", "status": 200, "url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001658"}. |
| TERM2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001659; obo_id, label, description, obo_synonym | supports | Current BTO:0001659 resolves to aerial root; obsolete=False. Definition and synonym metadata inspected; ontology hierarchy alone is not proof that a contextual parent is a biological genus. Retrieval: {"accessed_at": "2026-10-14T21:35:10Z", "final_url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001659", "sha256": "59afd23010d20c67bbc106c243e44bf7ac1929e01c72901d2e86301aeeab7b87", "status": 200, "url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001659"}. |
| TERM3 | https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0009005; obo_id, label, description, obo_synonym | supports | Current PO:0009005 resolves to root; obsolete=False. Definition and synonym metadata inspected; ontology hierarchy alone is not proof that a contextual parent is a biological genus. Retrieval: {"accessed_at": "2026-10-14T21:35:11Z", "final_url": "https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0009005", "sha256": "60c8efb1f40858c6dbe6c028123a6df05954c7b8ed650ad132d94c01bc4716c5", "status": 200, "url": "https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0009005"}. |

## Limits And Additional Notes

- This observation assesses exact commit 22120cf5ce86a96fbd23524bfcd7a00ed08b3106 before any curation in the authorized publication workflow; proposed actions are not completed fixes.
- Original specimen-level and PREGO pair-level references were not recovered; source association is not independently certified as isolation, residence or characteristic presence.
- Current ontology checks do not refresh the frozen slice. Product-label and deterministic gates do not establish scientific truth or SSSOM/KGX readiness.
- The review covers one complete target, not the whole corpus. Optional empty fields are not treated as missing required evidence.
- Legacy ad hoc findings have no structured occurrence IDs. They are evidence, not invented previous_occurrences.
- The requested publication workflow is separate from this immutable pre-curation observation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T214824Z-aerial_root
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: aerial root'
started_at: '2026-10-14T21:34:34Z'
finished_at: '2026-10-14T21:48:24Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same-agent scientific assessment and later adversarial pass,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
scientific_review: true
verdict: pass_with_limitations
summary: An aerial root is both a root and an aerial plant part. Its GOLD source path
  and one ORGANISM assertion agree with the frozen source. Counts for the separate
  mucilage child or generic Roots triads are not evidence for this source member.
source:
  git_revision: 22120cf5ce86a96fbd23524bfcd7a00ed08b3106
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
  - path: curation/decisions.tsv
    sha256: 82b51cd6ebc6f22aa5e6f67fb1202c7fdb574013aafb692779466ca2f7108a62
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 717cdadc8ac4f7ae0c67c228278b6081cdf141082e62d9903fe4a3b17ab88b1f
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 11f153cc7f19333dc89a9019ef59c33b210bbebb44dd4e84b11166be3dd3927f
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: ac7bfb1d309f66d89b9180e77b5c7ae6ec4c96568edea9b72da1db88e9dac310
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: 1a9576ea20f669a599b2b5ce64138b221df03c5eb051b8499ce35c33be825008
    role: context
  - path: data/habitats/host_associated/acute_lymphoblastic_leukemia_cell.yaml
    sha256: 00aa44197c12be59d28acd8d9006d0c468f36e8b7dec42595326d2dabf017d81
    role: context
  - path: data/habitats/host_associated/adenoid.yaml
    sha256: a17452b36824f55c4e28e7ab9134d8b6095504a06d36e96203cf62f6115dd89e
    role: context
  - path: data/habitats/host_associated/adenoma.yaml
    sha256: 3cf9c9c96c98f6a5db085bd3a9e265900e81c0d1f7dafd7e19af8e90c9f5cda1
    role: context
  - path: data/habitats/host_associated/adipose_tissue.yaml
    sha256: 864bdf2a2f2a5a1e99716a7ea9c354a0d2cec4833c183458f526f54ed313329e
    role: context
  - path: data/habitats/host_associated/adipose_tissue__28f7c202.yaml
    sha256: 35607065d54cd166863b5ab92eef44a1a9515bbfb6e61a12232e9d7f9636a744
    role: context
  - path: data/habitats/host_associated/adipose_tissue__2f4c0234.yaml
    sha256: 31030269f5f22d4ce59b5089cf9169e358c6470b6f2c9b3ed4107d6822f3758d
    role: context
  - path: data/habitats/host_associated/adipose_tissue__3dd3b646.yaml
    sha256: 9e6af80852c8bec3236a0631fa61864b76f6e967ecf0f9ad28139d95fe5eb6b0
    role: context
  - path: data/habitats/host_associated/adipose_tissue__9969df64.yaml
    sha256: decb0a4d628d548ac21a2a6faf4a0f932a275a3609398392c0ad70efd3014d21
    role: context
  - path: data/habitats/host_associated/adrenal_gland.yaml
    sha256: 55f7ccfe65649f98791eb5fe776d3e0838024a18f0fad3ffe60618cd6c4ca055
    role: context
  - path: data/habitats/host_associated/adult.yaml
    sha256: c7f6dcb657d475f674d7ce99efcc40d3e30db9e2df4e899a21cfcbbe6123f39d
    role: context
  - path: data/habitats/host_associated/aerial_part.yaml
    sha256: eb7b4c5a03c7b5c5c5f0af47e97a50cf4f0a185affb57f30aee21c6432c3c71a
    role: context
  - path: data/habitats/host_associated/aerial_root.yaml
    sha256: 6a5f29f9b0077c138c2021f72060b6b1cf8e7462c4071c36cdf697b9dca86978
    role: target
  - path: data/habitats/host_associated/benign_tumor.yaml
    sha256: 3e0b774986a5090329828796dfdc55d7405135ecbc27ff8c9c638cf47863d63e
    role: context
  - path: data/habitats/host_associated/connective_tissue.yaml
    sha256: a9bdb03f9861db9efde176fa4d7eaa4daedce57096e99bf6064de8ce62b556e9
    role: context
  - path: data/habitats/host_associated/endocrine_gland.yaml
    sha256: 7bad2c064b51f831c15818a6c641d7db5984605f2d54d6553ce737a824081dcc
    role: context
  - path: data/habitats/host_associated/endocrine_gland__8c35903c.yaml
    sha256: 514315aea57ac6555d13e02dac2548b4f829f1b060d347f65f372fde8a7eb9f5
    role: context
  - path: data/habitats/host_associated/integumentary_system__2442c03e.yaml
    sha256: 6b9641cba433804d7f4535dda313f84aefd1805f7f36a79c71e0e93dabd78afc
    role: context
  - path: data/habitats/host_associated/integumentary_system__489a751e.yaml
    sha256: ca8dd250782441d72f1bc981dd1e9402553363456897b21c7cbbd2133b50ed8a
    role: context
  - path: data/habitats/host_associated/integumentary_system__bd82bc93.yaml
    sha256: 4e26a3fb52d1b0aab9ddecc1c357935e2394b6a2af1764f67afc244ddd824be5
    role: context
  - path: data/habitats/host_associated/integumentary_system__e212bc7d.yaml
    sha256: 17169f5334109254c2d5f87a04cadfe86f0a74ded9dceac8d608e0cdf2abf93e
    role: context
  - path: data/habitats/host_associated/lymphoid_tissue.yaml
    sha256: 4fe04531289bdcca53a59810a84bfbc3308297b75b1cc1a2eb87aedac523dd64
    role: context
  - path: data/habitats/host_associated/root.yaml
    sha256: bff8dbd6b887c04f59cf573e8a201cd30f49bc2c51e6e92d5fb72747cc55df25
    role: context
  - path: data/habitats/host_associated/root__722ce44f.yaml
    sha256: eed2322864dbb77748a875551a9c8b42a7db2ffd35e246c9e4fa5f586ff736e5
    role: context
  - path: data/habitats/host_associated/tonsil.yaml
    sha256: a7b94d7d9e01995eb25e5e17f05d89516e2637ce750da05bf58e39232e2d6b8e
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
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260923T051638Z-acute_lymphoblastic_leukemia_cell.md
    sha256: 8a9e0d858e0d17a6bd0b0f4f4de9c6252683bf6391d8556960136cead84fa5e0
    role: context
  - path: reports/yaml_record_review/20260923T053455Z-adenoid.md
    sha256: 792e800776371c11f981e4f5d33342c542413ba86d6bdf3bdff72d2c68dac8a4
    role: context
  - path: reports/yaml_record_review/20260923T055611Z-adenoma.md
    sha256: 6b2d1f1081e5b790771803b6495c608eccce79a899c2a9a29bc1153e1c17c6a9
    role: context
  - path: reports/yaml_record_review/20260923T061621Z-adipose_tissue.md
    sha256: cb87ecd387e6d053e5fca96e902cdf2cdb9c457d82fd438dfcbdac75361521a3
    role: context
  - path: reports/yaml_record_review/20260923T063701Z-adipose_tissue__28f7c202.md
    sha256: 9dc2e8e0a07eeb052eacb37502451fa14cf80b72ec58270e8bf21c4a374836c0
    role: context
  - path: reports/yaml_record_review/20260923T065349Z-adipose_tissue__2f4c0234.md
    sha256: 0da01abaa79b7812f2acfdcaa4150561a3174b70e8fc35d228b7198d490ca7e1
    role: context
  - path: reports/yaml_record_review/20260923T154927Z-adipose_tissue__3dd3b646.md
    sha256: b83483ed390e3e1f87f7bdb76388e516d99cb0f1a235eb58462eb43bd036c51a
    role: context
  - path: reports/yaml_record_review/20260923T161138Z-adipose_tissue__9969df64.md
    sha256: 482bb8e1957f09645964a094b3751692c630ecfb7c4f50919cd943841020d51b
    role: context
  - path: reports/yaml_record_review/20260923T163309Z-adrenal_gland.md
    sha256: be09f641d0cd6d2787e50fc93ff9f628df60e10ba960b892b4d8fbd63b52e69d
    role: context
  - path: reports/yaml_record_review/20260923T165051Z-adult.md
    sha256: 73ec6bd6dbea8969afce52b8ad941dced86297d4698340af6c7f3ceac45a5033
    role: context
  - path: reports/yaml_record_review/20260923T170759Z-aerial_part.md
    sha256: eab52834eb277777c15176f2b65ed71cb919167054bbc624c0a0df2f422e24b8
    role: context
  - path: reports/yaml_record_review/20260923T172735Z-aerial_root.md
    sha256: 9eb877777b9cfd926036011d637b1b857a83ed98196f97819d575215ef317324
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
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
targets:
- target_id: BTO:0001659
  path: data/habitats/host_associated/aerial_root.yaml
  label: aerial root
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/external_xrefs.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/redirects_retracted.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests_excluded.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_isolation_sources.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/environment_parameters.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_triads.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_studies.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/isolation_source_groundings.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitats.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
scope:
  description: One fully read HabitatRecord, all contributing source concepts and
    maintained owners, and claim-specific current source checks.
  selection: Next lexical unreviewed host-associated record after a census of 1,053
    reviewed of 3,208 current IDs; one of 12 separately assessed targets, not a sample
    estimate.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0001659
checks:
- check_id: C11
  name: Native just validate
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/aerial_root.yaml
  exit_code: 0
  target_ids:
  - BTO:0001659
  summary: Actual execution 2026-10-14T21:34:44Z to 2026-10-14T21:34:46Z. No issues
    found
  scope_note: Schema exact target; strict selected 12; history/provenance/corpus/causal/term-request/product
    checks full native scope. Product labels do not prove biological hierarchy or
    validate all minted prefixes.
- check_id: C12
  name: Native just validate-strict
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/acute_lymphoblastic_leukemia_cell.yaml data/habitats/host_associated/adenoid.yaml
    data/habitats/host_associated/adenoma.yaml data/habitats/host_associated/adipose_tissue.yaml
    data/habitats/host_associated/adipose_tissue__28f7c202.yaml data/habitats/host_associated/adipose_tissue__2f4c0234.yaml
    data/habitats/host_associated/adipose_tissue__3dd3b646.yaml data/habitats/host_associated/adipose_tissue__9969df64.yaml
    data/habitats/host_associated/adrenal_gland.yaml data/habitats/host_associated/adult.yaml
    data/habitats/host_associated/aerial_part.yaml data/habitats/host_associated/aerial_root.yaml
  exit_code: 0
  target_ids:
  - BTO:0001659
  summary: "Actual execution 2026-10-14T21:34:46Z to 2026-10-14T21:34:53Z. files scanned:\
    \      12\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:          \
    \      reports/instance_validation_failures.tsv"
  scope_note: Schema exact target; strict selected 12; history/provenance/corpus/causal/term-request/product
    checks full native scope. Product labels do not prove biological hierarchy or
    validate all minted prefixes.
- check_id: C13
  name: Native just validate-history
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0001659
  summary: 'Actual execution 2026-10-14T21:34:53Z to 2026-10-14T21:35:03Z. No issues
    found

    708 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Schema exact target; strict selected 12; history/provenance/corpus/causal/term-request/product
    checks full native scope. Product labels do not prove biological hierarchy or
    validate all minted prefixes.
- check_id: C14
  name: Native just provenance-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0001659
  summary: 'Actual execution 2026-10-14T21:35:03Z to 2026-10-14T21:35:04Z. provenance
    current: 14 committed inventories, 2 GOLD sources'
  scope_note: Schema exact target; strict selected 12; history/provenance/corpus/causal/term-request/product
    checks full native scope. Product labels do not prove biological hierarchy or
    validate all minted prefixes.
- check_id: C15
  name: Native just verify-corpus
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0001659
  summary: "Actual execution 2026-10-14T21:35:04Z to 2026-10-14T21:35:21Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/"
  scope_note: Schema exact target; strict selected 12; history/provenance/corpus/causal/term-request/product
    checks full native scope. Product labels do not prove biological hierarchy or
    validate all minted prefixes.
- check_id: C16
  name: Native just validate-causal-all
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0001659
  summary: Actual execution 2026-10-14T21:35:21Z to 2026-10-14T21:35:25Z. validated
    32 causal-graph curation file(s) with 32 graph(s)
  scope_note: Schema exact target; strict selected 12; history/provenance/corpus/causal/term-request/product
    checks full native scope. Product labels do not prove biological hierarchy or
    validate all minted prefixes.
- check_id: C17
  name: Native just term-requests-check
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0001659
  summary: Actual execution 2026-10-14T21:35:25Z to 2026-10-14T21:35:45Z. term-request
    table is current (109 terms)
  scope_note: Schema exact target; strict selected 12; history/provenance/corpus/causal/term-request/product
    checks full native scope. Product labels do not prove biological hierarchy or
    validate all minted prefixes.
- check_id: C18
  name: Native just validate-products
  required: true
  status: passed
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0001659
  summary: "Actual execution 2026-10-14T21:35:45Z to 2026-10-14T21:36:46Z. id↔label\
    \ correspondence summary:\n          OK_CANONICAL: 1175\n            OK_SYNONYM:\
    \ 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2060\n\n✅ All id↔label\
    \ pairs correspond."
  scope_note: Schema exact target; strict selected 12; history/provenance/corpus/causal/term-request/product
    checks full native scope. Product labels do not prove biological hierarchy or
    validate all minted prefixes.
- check_id: QC
  name: Authoritative exact-base QC
  required: true
  status: passed
  command: gh run view 38638089409 --repo CultureBotAI/HabitatMech --json name,status,conclusion,headSha,url
  exit_code: 0
  target_ids:
  - BTO:0001659
  evidence_ids:
  - BASE_QC
  summary: Hosted native QC succeeded at the exact assessed base. New bundles require
    a separate archive check after saving.
- check_id: IMODULON
  name: Expression adapter applicability
  required: false
  status: not_applicable
  target_ids:
  - BTO:0001659
  summary: No gene, regulator or expression-dataset claim is present; module membership
    would not establish habitat anatomy or occurrence.
- check_id: MEMBERS
  name: Original source-pair recovery
  required: false
  status: unavailable
  target_ids:
  - BTO:0001659
  summary: Frozen aggregate rows reproduce. Original GOLD specimens and PREGO pair-level
    references were not recovered; a backup search was permission-limited. This is
    not evidence of biological absence.
evidence:
- evidence_id: RECORD
  kind: record_content
  reference: data/habitats/host_associated/aerial_root.yaml
  accessed_at: '2026-10-14T21:47:23Z'
  support: supports
  summary: An aerial root is both a root and an aerial plant part. Its GOLD source
    path and one ORGANISM assertion agree with the frozen source. Counts for the separate
    mucilage child or generic Roots triads are not evidence for this source member.
    Entire target YAML was read, including synonyms, source attestations, taxa and
    audit events. This observation assesses exact commit 22120cf5ce86a96fbd23524bfcd7a00ed08b3106.
- evidence_id: RULES
  kind: authority
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md
  accessed_at: '2026-10-14T21:47:23Z'
  support: supports
  summary: Parents are strictly broader, not contextual locations or whole systems.
    Host stage and organism classes are not habitat identity. ITEM review is distinct
    from lexical/CLASS seeding and scientific review does not itself promote mapping
    status.
- evidence_id: SOURCE
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv; data/raw/prego_habitat_taxa.tsv; data/raw/prego_habitats.tsv
  accessed_at: '2026-10-14T21:47:23Z'
  support: supports
  summary: 'Exact matching source rows, including source-parent/sibling context where
    matched: {"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0",
    "canonical_path": "Host-associated > Plants > Roots > Aerial root > Mucilage",
    "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Plants",
    "ecosystem_subtype": "Aerial root", "ecosystem_type": "Roots", "gold_node_count":
    "1", "gold_node_ids": "gold.ecosystem:7971", "leaf_label": "Mucilage", "organism_count":
    "31", "specific_ecosystem": "Mucilage", "study_count": "0", "total_assertions":
    "31"}, "row": 349}, {"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Plants > Roots > Aerial root", "depth": "4", "ecosystem": "Host-associated",
    "ecosystem_category": "Plants", "ecosystem_subtype": "Aerial root", "ecosystem_type":
    "Roots", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:7969|gold.ecosystem:7970",
    "leaf_label": "Aerial root", "organism_count": "1", "specific_ecosystem": "",
    "study_count": "0", "total_assertions": "1"}, "row": 1108}], "data/raw/prego_habitat_taxa.tsv":
    [{"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "1", "taxon_id":
    "NCBITaxon:10", "taxon_label": "Cellvibrio"}, "row": 1690}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "BTO:0001188", "prego_score": "4", "rank": "2", "taxon_id": "NCBITaxon:1004301",
    "taxon_label": "Flavihumibacter"}, "row": 1691}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score":
    "4", "rank": "3", "taxon_id": "NCBITaxon:1005038", "taxon_label": "Fimbriimonas"},
    "row": 1692}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank":
    "4", "taxon_id": "NCBITaxon:1011", "taxon_label": "Sporocytophaga"}, "row": 1693},
    {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "5", "taxon_id":
    "NCBITaxon:102234", "taxon_label": "Cyanobacterium"}, "row": 1694}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "BTO:0001188", "prego_score": "4", "rank": "6", "taxon_id": "NCBITaxon:1032526",
    "taxon_label": "Pedosphaera"}, "row": 1695}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score":
    "4", "rank": "7", "taxon_id": "NCBITaxon:1033", "taxon_label": "Afipia"}, "row":
    1696}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "8", "taxon_id":
    "NCBITaxon:103728", "taxon_label": "Actinokineospora diospyrosa"}, "row": 1697},
    {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "9", "taxon_id":
    "NCBITaxon:1042312", "taxon_label": "Armatimonadia"}, "row": 1698}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "BTO:0001188", "prego_score": "4", "rank": "10", "taxon_id": "NCBITaxon:1042314",
    "taxon_label": "Armatimonadaceae"}, "row": 1699}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score":
    "4", "rank": "11", "taxon_id": "NCBITaxon:1060", "taxon_label": "Rhodobacter"},
    "row": 1700}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank":
    "12", "taxon_id": "NCBITaxon:106589", "taxon_label": "Cupriavidus"}, "row": 1701},
    {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "13", "taxon_id":
    "NCBITaxon:1071", "taxon_label": "Rhodopila globiformis"}, "row": 1702}, {"data":
    {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE",
    "prego_id": "BTO:0001188", "prego_score": "4", "rank": "14", "taxon_id": "NCBITaxon:1077257",
    "taxon_label": "Chthonomonadia"}, "row": 1703}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score":
    "4", "rank": "15", "taxon_id": "NCBITaxon:1077264", "taxon_label": "Chthonomonadaceae"},
    "row": 1704}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank":
    "16", "taxon_id": "NCBITaxon:1077265", "taxon_label": "Chthonomonas"}, "row":
    1705}, {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "17", "taxon_id":
    "NCBITaxon:1090", "taxon_label": "Chlorobiota"}, "row": 1706}, {"data": {"channels":
    "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "BTO:0001188", "prego_score": "4", "rank": "18", "taxon_id": "NCBITaxon:1107",
    "taxon_label": "Chloroflexus"}, "row": 1707}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score":
    "4", "rank": "19", "taxon_id": "NCBITaxon:1117", "taxon_label": "Cyanobacteriota"},
    "row": 1708}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank":
    "20", "taxon_id": "NCBITaxon:114248", "taxon_label": "Tepidimonas"}, "row": 1709},
    {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "21", "taxon_id":
    "NCBITaxon:1147159", "taxon_label": "Ornithinibacillus scapharcae"}, "row": 1710},
    {"data": {"channels": "environmental_samples", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank": "22", "taxon_id":
    "NCBITaxon:115336", "taxon_label": "Actinomadura vinacea"}, "row": 1711}, {"data":
    {"channels": "environmental_samples", "corroborated_by": "", "direct_flag": "TRUE",
    "prego_id": "BTO:0001188", "prego_score": "4", "rank": "23", "taxon_id": "NCBITaxon:1154584",
    "taxon_label": "Gaiellales"}, "row": 1712}, {"data": {"channels": "environmental_samples",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score":
    "4", "rank": "24", "taxon_id": "NCBITaxon:1154585", "taxon_label": "Gaiellaceae"},
    "row": 1713}, {"data": {"channels": "environmental_samples", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "BTO:0001188", "prego_score": "4", "rank":
    "25", "taxon_id": "NCBITaxon:1162", "taxon_label": "Nostocaceae"}, "row": 1714},
    {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "BTO:0001658", "prego_score": "3", "rank": "1", "taxon_id":
    "NCBITaxon:693986", "taxon_label": "Methylobacterium oryzae CBMB20"}, "row": 2414}],
    "data/raw/prego_habitats.tsv": [{"data": {"biolink_category": "biolink:GrossAnatomicalStructure",
    "channels": "environmental_samples", "direct_assertion_count": "794", "max_prego_score":
    "4", "ontology": "BTO", "prego_id": "BTO:0001188", "prego_synonyms": "root", "taxon_count":
    "794"}, "row": 89}, {"data": {"biolink_category": "biolink:GrossAnatomicalStructure",
    "channels": "annotated_genomes_isolates", "direct_assertion_count": "1", "max_prego_score":
    "3", "ontology": "BTO", "prego_id": "BTO:0001658", "prego_synonyms": "aerial bodies|aerial
    body|aerial part|aerial partic|aerial parts|aerial tissue|aerial tissues", "taxon_count":
    "1"}, "row": 606}]}. Native source mints: habitatmech:GOLD.4c130cb0f9. Counts
    are source assertions with source-specific units, not prevalence. Original specimen-level
    joins were not recovered.'
  locator: 1-based physical TSV row numbers in the attached row data
- evidence_id: CURATION
  kind: record_content
  reference: curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  accessed_at: '2026-10-14T21:47:23Z'
  support: supports
  summary: 'Matching maintained rows and parent context: {"curation/decisions.tsv":
    [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-12", "decision":
    "GROUND", "grounding_status": "EXACT", "identifier": "habitatmech:GOLD.7c6b8ca314",
    "notes": "Plant roots as habitat. Grounded to PO, the authoritative plant anatomy
    ontology, now that it is vendored (#10). Re-grounded from BTO:0001188 to PO:0009005
    now that PO is vendored (#10).", "object_id": "PO:0009005", "object_label": "root",
    "relation": "", "review_depth": "ITEM"}, "row": 744}, {"data": {"category": "",
    "curator": "claude-opus-5", "date": "2026-08-15", "decision": "GROUND", "grounding_status":
    "EXACT", "identifier": "habitatmech:ENVIRONMENTS_TABLE.58c6c839f8", "notes": "Co-attestor
    review (#12): kg-microbe''s environments.csv maps ''host_plant_root-associated''
    to NCBITaxon:1, whose label is ''root'' \u2014 the root of the TAXONOMY, not a
    plant root. The seeder''s non-habitat-prefix guard drops the row, so the parameter
    bands for a real habitat were being lost silently rather than misattributed. PO:0009005
    ''root'' is the term meant. Reported upstream.", "object_id": "PO:0009005", "object_label":
    "root", "relation": "", "review_depth": "ITEM"}, "row": 1634}]}. No habitat curation
    has been performed for this observation.'
- evidence_id: TRANSFORM
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/extract.py; src/habitatmech/schema/habitatmech.yaml
  accessed_at: '2026-10-14T21:47:23Z'
  support: supports
  summary: PREGO preserves original source-term attestations/taxa when its emitted
    identity is redirected. Extraction keeps top 25 distinct taxa by maximum score;
    direct_assertion_count counts evidence rows, not distinct taxa. CharacteristicTaxon
    entries are observational unless is_characteristic is explicitly asserted. GOLD
    immediate source parents are separate from ontology and decision parents.
  locator: extract_prego; ingest_prego; CharacteristicTaxon; GOLD parent generation
- evidence_id: SEARCH
  kind: search
  reference: curation/; history/; research/; reports/; data/raw/; build/; reviews/
  accessed_at: '2026-10-14T21:47:23Z'
  support: supports
  summary: Bounded ignored-inclusive search at 2026-10-14T21:34:59Z. All structured
    findings were scanned for these exact target IDs and none supplied a structured
    predecessor. Original PREGO transformed nodes/edges were not recovered at the
    manifest path; one backup directory was inaccessible, so no global absence is
    claimed.
  search_scope: rg --no-ignore --hidden across curation, history, research, reports,
    data/raw, build and reviews using target IDs, labels, slugs and native source
    mints; ignored and hidden files included. Structured finding scan used every reviews/structured/**/review.yaml.
    External backup directories were not exhaustively accessible.
- evidence_id: LEGACY
  kind: prior_review
  reference: reports/yaml_record_review/20260923T172735Z-aerial_root.md
  accessed_at: '2026-10-14T21:47:23Z'
  support: context_only
  summary: Historical Findings section and verdict reassessed. This is an ad hoc report
    without structured occurrence IDs, not an independent scientific authority. Stable
    legacy issue keys are retained where present; no previous_occurrences are invented.
- evidence_id: BASE_QC
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38638089409
  accessed_at: '2026-10-14T21:47:23Z'
  support: context_only
  summary: Authoritative Build and test succeeded on exact base 22120cf5ce86a96fbd23524bfcd7a00ed08b3106.
    This predates the newly saved bundles and does not substitute for their archive
    check.
- evidence_id: TERM0
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001188
  accessed_at: '2026-10-14T21:35:06Z'
  support: supports
  summary: 'Current BTO:0001188 resolves to root; obsolete=False. Definition and synonym
    metadata inspected; ontology hierarchy alone is not proof that a contextual parent
    is a biological genus. Retrieval: {"accessed_at": "2026-10-14T21:35:06Z", "final_url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001188",
    "sha256": "bad0d042b0bf734173f028a9a68be56234a3192e799004966dd5283a9e421dc3",
    "status": 200, "url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001188"}.'
  locator: obo_id, label, description, obo_synonym
- evidence_id: TERM1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001658
  accessed_at: '2026-10-14T21:35:09Z'
  support: supports
  summary: 'Current BTO:0001658 resolves to aerial part; obsolete=False. Definition
    and synonym metadata inspected; ontology hierarchy alone is not proof that a contextual
    parent is a biological genus. Retrieval: {"accessed_at": "2026-10-14T21:35:09Z",
    "final_url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001658",
    "sha256": "3d3d6c1e9fd72ac990cdbf87c6d2a04efc55b07550175ae1f9e62f918d273641",
    "status": 200, "url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001658"}.'
  locator: obo_id, label, description, obo_synonym
- evidence_id: TERM2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001659
  accessed_at: '2026-10-14T21:35:10Z'
  support: supports
  summary: 'Current BTO:0001659 resolves to aerial root; obsolete=False. Definition
    and synonym metadata inspected; ontology hierarchy alone is not proof that a contextual
    parent is a biological genus. Retrieval: {"accessed_at": "2026-10-14T21:35:10Z",
    "final_url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001659",
    "sha256": "59afd23010d20c67bbc106c243e44bf7ac1929e01c72901d2e86301aeeab7b87",
    "status": 200, "url": "https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001659"}.'
  locator: obo_id, label, description, obo_synonym
- evidence_id: TERM3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0009005
  accessed_at: '2026-10-14T21:35:11Z'
  support: supports
  summary: 'Current PO:0009005 resolves to root; obsolete=False. Definition and synonym
    metadata inspected; ontology hierarchy alone is not proof that a contextual parent
    is a biological genus. Retrieval: {"accessed_at": "2026-10-14T21:35:11Z", "final_url":
    "https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0009005",
    "sha256": "60c8efb1f40858c6dbe6c028123a6df05954c7b8ed650ad132d94c01bc4716c5",
    "status": 200, "url": "https://www.ebi.ac.uk/ols4/api/ontologies/po/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FPO_0009005"}.'
  locator: obo_id, label, description, obo_synonym
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Exact anatomy, host and source meaning
  outcome: supported
  target_ids:
  - BTO:0001659
  evidence_ids:
  - RECORD
  - RULES
  - TERM0
  - TERM1
  - TERM2
  - TERM3
  summary: An aerial root is both a root and an aerial plant part. Its GOLD source
    path and one ORGANISM assertion agree with the frozen source. Counts for the separate
    mucilage child or generic Roots triads are not evidence for this source member.
- assessment_id: SOURCE
  area: provenance
  topic: Frozen source counts and source-level decisions
  outcome: supported
  target_ids:
  - BTO:0001659
  evidence_ids:
  - SOURCE
  - CURATION
  - TRANSFORM
  summary: Every contributing source and maintained decision was traced. GOLD zero
    counts omit count/unit; nonzero counts retain ORGANISM. PREGO TAXON counts are
    distinct taxa, not direct-assertion rows or prevalence. The source status is reproduced,
    not scientifically certified by reproduction.
  dimensions:
  - name: mapping_status
    value: SEEDED
    definition: Native generated decision coverage, not review verdict
    evidence_ids:
    - RECORD
    - CURATION
  - name: grounding_status
    value: EXACT
    definition: Native mapping relation independently assessed for correctness
    evidence_ids:
    - RECORD
    - SOURCE
- assessment_id: HIERARCHY
  area: consistency
  topic: Strict genus versus source context
  outcome: supported
  target_ids:
  - BTO:0001659
  evidence_ids:
  - RECORD
  - RULES
  - CURATION
  - TERM0
  - TERM1
  - TERM2
  - TERM3
  summary: 'The false context parents are identified individually in findings; independent
    anatomical genera are retained. For adenoma, being a benign tumor is biologically
    valid: the parent record NOT_APPLICABLE flag alone does not refute that relation,
    so legacy HM-ADENOMA-002 is not adopted as a confirmed false-is-a finding. For
    aerial root, root and aerial part remain valid genera.'
- assessment_id: BIOLOGY
  area: evidence
  topic: Association versus characteristic presence and source-member evidence
  outcome: not_applicable
  target_ids:
  - BTO:0001659
  evidence_ids:
  - RECORD
  - SOURCE
  summary: No retained taxon, environmental-parameter or causal-graph assertion needs
    filling merely for coverage. Source-path context is not mechanistic evidence.
findings: []
actions: []
limitations:
- This observation assesses exact commit 22120cf5ce86a96fbd23524bfcd7a00ed08b3106
  before any curation in the authorized publication workflow; proposed actions are
  not completed fixes.
- Original specimen-level and PREGO pair-level references were not recovered; source
  association is not independently certified as isolation, residence or characteristic
  presence.
- Current ontology checks do not refresh the frozen slice. Product-label and deterministic
  gates do not establish scientific truth or SSSOM/KGX readiness.
- The review covers one complete target, not the whole corpus. Optional empty fields
  are not treated as missing required evidence.
notes:
- Legacy ad hoc findings have no structured occurrence IDs. They are evidence, not
  invented previous_occurrences.
- The requested publication workflow is separate from this immutable pre-curation
  observation.
tags:
- habitatmech
- record-review
- host-associated
```
