# Remediation review: dental_abscess

- Review: 20261016T090045Z-dental_abscess-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T08:41:20Z
- Finished UTC: 2026-10-16T09:00:45Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed the guarded GOLD context-parent contribution. Identity and native status are unchanged. Source observations and independent valid genera are preserved. Remaining predecessor findings are explicitly open.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding after bounded repair.

Selection: One of ten repaired targets from the crustacean-through-dental cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4b24d5599c8da75fb5203191d5859e0ba6af0c40.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.db17f52768 | data/habitats/host_associated/dental_abscess.yaml | generated | Dental abscess |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/dental_abscess.yaml | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:35:27Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/dental_abscess.yaml |
| just validate-strict data/habitats/host_associated/crustacean_maxillary_gland.yaml data/habitats/host_associated/crustacean_post_larval_stage.yaml data/habitats/host_associated/cryptomonads_cryptophytes.yaml data/habitats/host_associated/ctenophora.yaml data/habitats/host_associated/cud.yaml data/habitats/host_associated/cutaneous_leishmaniasis.yaml data/habitats/host_associated/cuticle.yaml data/habitats/host_associated/cuticle__11d6cb22.yaml data/habitats/host_associated/cuticle__6c2a3dac.yaml data/habitats/host_associated/cuticle__72f050c4.yaml data/habitats/host_associated/cuticle__9784f327.yaml data/habitats/host_associated/cuticle__a024212e.yaml data/habitats/host_associated/cv_1_cell.yaml data/habitats/host_associated/cyst.yaml data/habitats/host_associated/decayed_wood__afd3403c.yaml data/habitats/host_associated/decomposed_body.yaml data/habitats/host_associated/decomposed_body__7ba62861.yaml data/habitats/host_associated/decomposed_body__ee215354.yaml data/habitats/host_associated/dental_abscess.yaml data/habitats/host_associated/dental_calculus.yaml data/habitats/host_associated/dental_calculus__18e49dca.yaml data/habitats/host_associated/dental_calculus__8a0a99ac.yaml data/habitats/host_associated/dental_plaque.yaml data/habitats/host_associated/dental_plaque__384bd6e9.yaml | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:35:44Z. uv run python scripts/validate_strict.py data/habitats/host_associated/crustacean_maxillary_gland.yaml data/habitats/host_associated/crustacean_post_larval_stage.yaml data/habitats/host_associated/cryptomonads_cryptophytes.yaml data/habitats/host_associated/ctenophora.yaml data/habitats/host_associated/cud.yaml data/habitats/host_associated/cutaneous_leishmaniasis.yaml data/habitats/host_associated/cuticle.yaml data/habitats/host_associated/cuticle__11d6cb22.yaml data/habitats/host_associated/cuticle__6c2a3dac.yaml data/habitats/host_associated/cuticle__72f050c4.yaml data/habitats/host_associated/cuticle__9784f327.yaml data/habitats/host_associated/cuticle__a024212e.yaml data/habitats/host_associated/cv_1_cell.yaml data/habitats/host_associated/cyst.yaml data/habitats/host_associated/decayed_wood__afd3403c.yaml data/habitats/host_associated/decomposed_body.yaml data/habitats/host_associated/decomposed_body__7ba62861.yaml data/habitats/host_associated/decomposed_body__ee215354.yaml data/habitats/host_associated/dental_abscess.yaml data/habitats/host_associated/dental_calculus.yaml data/habitats/host_associated/dental_calculus__18e49dca.yaml data/habitats/host_associated/dental_calculus__8a0a99ac.yaml data/habitats/host_associated/dental_plaque.yaml data/habitats/host_associated/dental_plaque__384bd6e9.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:35:55Z. No issues found<br>839 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:35:56Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:36:18Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:36:23Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:36:46Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:37:48Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| uv run pytest -q tests/test_cuticle_dental_review_repairs.py --no-cov | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:37:58Z. ..                                                                       [100%]<br>2 passed in 7.86s |
| uv run ruff check . | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:37:58Z. All checks passed! |
| git diff --check | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:38:00Z.  |
| uv run pytest -q tests/test_decisions.py::test_curation_notes_do_not_cite_evidence_that_does_not_exist tests/test_cuticle_dental_review_repairs.py --no-cov | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:38:15Z. ...                                                                      [100%]<br>3 passed in 13.36s |
| just term-requests | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:35:45Z. wrote curation/term_requests/envo_robot_template.tsv: 110 ENVO terms from 110 source records<br><br>25 examined-ungrounded record(s) still have no request written. Top by volume:<br>      438  Medical-environment                habitatmech:BACDIVE.5e52ea1bba<br>      228  Fruit-Seed                         habitatmech:BACDIVE.ba016fe448<br>       35  Egg                                habitatmech:BACDIVE.d48ce9485d<br>        5  Caeca: Bacteriome                  habitatmech:GOLD.2d506b9526<br>        3  Abdomen                            habitatmech:GOLD.c6b0b54290<br>        2  Crop                               habitatmech:GOLD.5446ce4c6d<br>        1  Thalassic                          habitatmech:GOLD.3fece6dbf7<br>        1  Crop                               habitatmech:GOLD.57011086ca<br>        0  Subtidal zone sediment             habitatmech:GOLD.785879d721<br>        0  Subterranean lake                  habitatmech:GOLD.937bf682c4<br><br>covered 105842 upstream assertions; 713 still unrequested across 25 record(s); 15 examined and deliberately not asked for<br><br>&#96;created by&#96; is empty: it wants pipe-delimited full ORCID IRIs and this script cannot know them.<br> uv run python scripts/build_term_requests.py |
| just docs-stats | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:36:09Z. updated README corpus statistics<br> uv run python scripts/check_docs.py --write |
| just render | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:36:51Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 135 term requests -&gt; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages<br> uv run python scripts/render_pages.py |
| just render-check | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:37:36Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 135 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmp29xf44zp/site<br>pages/ is in step with the corpus<br> uv run python scripts/render_pages.py --check |
| just redirects-check | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:40:01Z. RETIRED.tsv is current (259 redirects)<br> uv run python scripts/build_redirects.py --check |
| uv run ruff check . | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:40:01Z. All checks passed! |
| git diff --check | passed | True | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:40:01Z.  |
| Exact-revision hosted authoritative QC and archive contract | passed | True | habitatmech:GOLD.db17f52768 | Verified 2026-10-16T09:00:10Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38875299816 |
| Citation correction preserves semantic-map input bytes | passed | False | habitatmech:GOLD.db17f52768 | Finished 2026-10-16T08:35:14Z. Full 3209-record semantic JSONL is byte-identical before and after replacing PMID strings with their publication URLs. |

## Scientific And Domain Assessments

### Bounded correction and exact preservation

consistency: supported. Targets: habitatmech:GOLD.db17f52768.

Removed the guarded GOLD context-parent contribution. Identity and native status are unchanged. Source observations and independent valid genera are preserved. Remaining predecessor findings are explicitly open.

### Current anatomical identity and hierarchy

identity: concern. Targets: habitatmech:GOLD.db17f52768.

habitatmech:GOLD.db17f52768: Dental abscess; NOT_APPLICABLE/REVIEWED; parents []. Source anatomy/material scope remains as assessed in the baseline; only the documented false parents are removed. No replacement identity, genus or definition is fabricated. Dental-abscess status remains provisional.

### Units, counts and observations

quantity: supported. Targets: habitatmech:GOLD.db17f52768.

[{"source": "GOLD", "source_id": "gold.ecosystem:6345", "source_label": "Dental abscess", "source_path": "Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Oral cavity &gt; Dental abscess", "assertion_count": 5, "assertion_unit": "ORGANISM"}]. Original counts/units, taxa, scores and parameters are preserved, not interpreted as prevalence or viability.

### Predecessor reconciliation

representation: concern. Targets: habitatmech:GOLD.db17f52768.

Every previous finding keeps its stable issue key and exact lineage. Removing three unsupported narrow matches does not resolve global mapping contract #1398.

### Evidence and lifecycle boundaries

completeness: supported. Targets: habitatmech:GOLD.db17f52768.

Only the three explicit arthropod ITEM decisions change native status. Optional definitions, causal mechanisms and biological absence claims are not invented. The complete target, remaining parents, history and original evidence were rechecked.

## Findings

### F1: Source context is not a strictly broader habitat class

major / resolved / confirmed; issue key: dental-abscess-context-parent.

Removed only the guarded GOLD source-context contribution habitatmech:GOLD.99880772e1. Independent valid parents and every source observation remain intact.

Disposition: Removed only the guarded GOLD source-context contribution habitatmech:GOLD.99880772e1. Independent valid parents and every source observation remain intact.

### F2: NOT_APPLICABLE rationale omits the localized abscess-material sense

major / open / provisional; issue key: dental-abscess-abscess-habitat-status.

The whole-cavity parent is removed, but the localized pus/material interpretation still requires original source assertions before changing NOT_APPLICABLE. Its provisional status is retained.

Disposition: The whole-cavity parent is removed, but the localized pus/material interpretation still requires original source assertions before changing NOT_APPLICABLE. Its provisional status is retained.

## Recommended Actions And Acceptance Checks

### ACT2

The ITEM decision categorically calls Dental abscess not a place, yet the inspected authority describes a localized pus collection caused by bacterial infection. This is a material/site sense that the generic disease/filler rationale does not address. Verify the five organism assertions and original source intent before revising NOT_APPLICABLE or defining an abscess-associated habitat. Independently, a localized collection is not a kind of whole oral cavity, so the inherited cavity parent is not strictly broader. No clinical treatment recommendation follows from this representation review. Inspect the original five source assertions and replace the blanket rationale with a source-intent decision; no new exact ontology identity is preselected. Proposed work only; no repair or status promotion is performed by this review.

- Regress the exact target claim and preserve valid genera, identifiers, source counts/units and taxon associations. Recover original evidence before deleting a provisional pair; do not decrement frozen totals by hand.
- Record authorized curation history; require schema, strict, provenance, history, label, corpus, site and full QC gates.
- Save an immutable successor with the same issue key and exact predecessor finding identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX8 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000167/graph; UBERON_0000167-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000167", "target": "http://purl.obolibrary.org/obo/UBERON_0002553", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000167", "target": "http://purl.obolibrary.org/obo/UBERON_0000165", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000167; UBERON_0000167.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:0000167", "label": "oral cavity", "is_obsolete": false, "description": ["Anatomical cavity at the start of the digestive tract that that is enclosed by the mouth. The boundaries and contents vary depending on the species. In vertebrates, the boundaries are the oral opening, the cheeks, the palate and (if present) the palatoglossal arch - if this is not present then the mouth and pharynx form the oropharyngeal cavity. The buccal cavity contains the teeth, tongue and palate (when present)."], "obo_synonym": [{"name": "buccal cavity", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "FMA", "id": "20292", "description": null, "url": "http://purl.org/sig/ont/fma/20292"}, {"database": "ISBN", "id": "0073040584", "description": null, "url": "https://www.worldcat.org/search?q=bn%3A0073040584"}]}], "annotation": {"database_cross_reference": ["AAO:0000053", "AAO:0000960", "BSA:0000107", "CALOHA:TS-1315", "EFO:0001975", "EHDAA2:0001324", "EHDAA:6970", "EMAPA:17411", "EMAPA:18399", "EV:0100057", "FMA:20292", "HAO:0000669", "NCIT:C12421", "SCTID:181220002", "TAO:0001027", "TGMA:0000102", "VHOG:0000188", "WBbt:0005255", "XAO:0000126", "ZFA:0001027", "MESH:D009055", "UMLS:C0226896"], "external_definition": ["Anatomical cavity bounded anteriorly by the mouth and posteriorly by the derivatives of the branchial arches.[AAO]", "The cavity of the mouth, bounded by the jaw bones and associated structures (muscles and mucosa). [TFD][VHOG]"], "homology_notes": ["Echinoderms, hemichordates, and chordates are called deuterostomes because the mouth arises not from the blastopore but from a second invagination at the anterior end of the larva that pushes in to connect with the archenteron.[well established][VHOG]"], "id": ["UBERON:0000167"]}} |
| EW10 | https://medlineplus.gov/ency/article/001060.htm; Definition and causes paragraphs | context_only | The authority describes a localized pus collection from bacterial infection in or around a tooth. This directly challenges a blanket not-a-place rationale without identifying the exact GOLD samples. Inspected through the web reader this session; no full-page byte snapshot claimed. |
| EAFTER | data/habitats/host_associated/dental_abscess.yaml; Entire regenerated target YAML | supports | {"identifier": "habitatmech:GOLD.db17f52768", "label": "Dental abscess", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NOT_APPLICABLE", "mapping_status": "REVIEWED", "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6345", "source_label": "Dental abscess", "source_path": "Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Oral cavity &gt; Dental abscess", "assertion_count": 5, "assertion_unit": "ORGANISM"}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "NOT_APPLICABLE", "changes": "Marked NOT_APPLICABLE: the source concept does not denote a habitat. 'Dental abscess' names a disease, an intervention, a sampling artefact or a no-value filler rather than a place. Pulled out of the class-level sweep and decided individually. (source concept habitatmech:GOLD.db17f52768)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NOT_APPLICABLE."}, {"timestamp": "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.99880772e1 for habitatmech:GOLD.db17f52768 (Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Oral cavity &gt; Dental abscess). Review https://github.com/CultureBotAI/HabitatMech/issues/2235 : Maxillary gland is not the entire excretory system; cud is not the stomach; cuticle is not the whole integument, integumentary system or skin; abscess, calculus and plaque are not the whole oral cavity. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.db17f52768. Other identity, status and mapping findings remain separate."}]} |
| EPREV | reviews/structured/20261016T073711Z-dental_abscess-record/review.yaml; Every immutable baseline finding | supports | Exact predecessor keys and findings reconciled; the original inspected source scope is preserved. |
| ETEST | tests/test_cuticle_dental_review_repairs.py; Complete full-corpus counterfactual | supports | Exactly ten records differ. Only guarded context-parent removal and three arthropod grounding/predicate/status corrections change scientific fields; all source observations and unrelated fields are invariant. |
| ERULE | docs/CURATION.md; Strict hierarchy, ITEM decisions and source units | supports | Native history/status follows maintained rows; generated artifacts are not hand-edited. |
| EH40 | history/mappings/cuticle_dental_review_citations/2026-10-16T083223Z-codex-gpt-5-c42651.yaml; Complete session event | supports | Authorized curation by codex-gpt-5; maintained owner and issue retained. |
| EH41 | history/mappings/cuticle_dental_review_mineral/2026-10-16T074759Z-codex-gpt-5-d2d9db.yaml; Complete session event | supports | Authorized curation by codex-gpt-5; maintained owner and issue retained. |
| EH42 | history/mappings/cuticle_dental_review_parents/2026-10-16T074758Z-codex-gpt-5-56d722.yaml; Complete session event | supports | Authorized curation by codex-gpt-5; maintained owner and issue retained. |
| EPARENTS | curation/gold_parent_exclusions.tsv; Exact physical TSV rows | supports | [[9, "habitatmech:GOLD.db17f52768\tHost-associated &gt; Mammals: Human &gt; Digestive system &gt; Oral cavity &gt; Dental abscess\thabitatmech:GOLD.99880772e1\tcodex-gpt-5\t2026-10-16\tReview https://github.com/CultureBotAI/HabitatMech/issues/2235 : Maxillary gland is not the entire excretory system; cud is not the stomach; cuticle is not the whole integument, integumentary system or skin; abscess, calculus and plaque are not the whole oral cavity. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.db17f52768. Other identity, status and mapping findings remain separate."]] |
| EDECISION | curation/decisions.tsv; Exact physical TSV rows | supports | [[1230, "habitatmech:GOLD.db17f52768\tNOT_APPLICABLE\t\t\t\tclaude-opus-5\t2026-08-12\t'Dental abscess' names a disease, an intervention, a sampling artefact or a no-value filler rather than a place. Pulled out of the class-level sweep and decided individually.\tITEM\t\t"]] |

## Limits And Additional Notes

- Original specimen-level evidence was not exhaustively reconstructed. Source counts, associations and scores do not establish prevalence, viability or characteristic presence.
- Configured id-label validation skips 2063 no-adapter pairs; the 18 displayed target TaxIds were separately checked against current NCBI.
- iModulonDB is not applicable: these records assert no genes, regulators, pathways or expression modules. Literature mechanisms were not imported as causal graphs.
- Same-agent disposition, not independent human approval. Final-head and merge-queue checks remain separate publication gates. Whole-corpus scientific review and current kg-microbe export conformance are incomplete.
- All earlier saved bundles and session histories remain unchanged. Preserve the exact off-main input base with an annotated provenance tag before squash merge and branch deletion.
- A preliminary unsaved capture at b3b87caf3d56b74891036c9d3c1c201f07388c63 was retained separately. CI #2240 required publication URLs instead of PMID CURIEs in three decision notes; after that formatting correction and regeneration, inputs were freshly captured and the complete targets reassessed. No prior saved review was refreshed or rewritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T090045Z-dental_abscess-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: dental_abscess'
started_at: '2026-10-16T08:41:20Z'
finished_at: '2026-10-16T09:00:45Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: The same agent read sources, assessed the target and authored
    this report; not independent reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: Removed the guarded GOLD context-parent contribution. Identity and native
  status are unchanged. Source observations and independent valid genera are preserved.
  Remaining predecessor findings are explicitly open.
source:
  git_revision: 4b24d5599c8da75fb5203191d5859e0ba6af0c40
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
    sha256: bd080045e44f1995788c20df1ea1e71e3fe8d2dc44a3730f8618c8f133e2341a
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 1675ec9acca1f4fe6b1101188aafbc10f3cf6d2fabfd149232ec0260262a311f
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
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
  - path: data/habitats/host_associated/dental_abscess.yaml
    sha256: 14df7e1859a2d23635276a8fe17a1a9381e59307060f16b06148220c5e0b3254
    role: target
  - path: data/habitats/host_associated/oral_cavity__7cca2853.yaml
    sha256: e0bba6d1097d505d9ef05b8da024d469df85fe6febd5dc0fd1a2ffbefb94d4c1
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
  - path: history/mappings/cuticle_dental_review_citations/2026-10-16T083223Z-codex-gpt-5-c42651.yaml
    sha256: f0a7f6577764a3dc69c894b8c6dffc7cac78a08a1d7f9f8a4c990bf6d9382a0e
    role: context
  - path: history/mappings/cuticle_dental_review_mineral/2026-10-16T074759Z-codex-gpt-5-d2d9db.yaml
    sha256: b2d4696ff2e86b972d0083c191362137f20c3c1c9e6a1b1d8f23c0051d03c3fa
    role: context
  - path: history/mappings/cuticle_dental_review_parents/2026-10-16T074758Z-codex-gpt-5-56d722.yaml
    sha256: 557e55252578fe0c8d3d92eb3054ae15a96973790ef9048f0b9cdbdd90af98cd
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261016T073711Z-dental_abscess-record/review.yaml
    sha256: 69567a9f5199b7883a75ad098d68cba413ea389e9dc02413349ce3b4e2fbe191
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
  - path: tests/test_cuticle_dental_review_repairs.py
    sha256: bfa65736cdf7252a34180b268b0e56e4ef25970cf3308b0f84658f3f731b6ed5
    role: context
targets:
- target_id: habitatmech:GOLD.db17f52768
  path: data/habitats/host_associated/dental_abscess.yaml
  label: Dental abscess
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
  description: Full current target assessment and explicit disposition of every baseline
    finding after bounded repair.
  selection: One of ten repaired targets from the crustacean-through-dental cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.db17f52768
  exclusions:
  - target: Other corpus records and SSSOM/KGX conformance
    reason: Not whole-corpus scientific approval or shared export-contract certification.
checks:
- check_id: C7
  name: just validate data/habitats/host_associated/dental_abscess.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/dental_abscess.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:35:27Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/dental_abscess.yaml"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C10
  name: just validate-strict data/habitats/host_associated/crustacean_maxillary_gland.yaml
    data/habitats/host_associated/crustacean_post_larval_stage.yaml data/habitats/host_associated/cryptomonads_cryptophytes.yaml
    data/habitats/host_associated/ctenophora.yaml data/habitats/host_associated/cud.yaml
    data/habitats/host_associated/cutaneous_leishmaniasis.yaml data/habitats/host_associated/cuticle.yaml
    data/habitats/host_associated/cuticle__11d6cb22.yaml data/habitats/host_associated/cuticle__6c2a3dac.yaml
    data/habitats/host_associated/cuticle__72f050c4.yaml data/habitats/host_associated/cuticle__9784f327.yaml
    data/habitats/host_associated/cuticle__a024212e.yaml data/habitats/host_associated/cv_1_cell.yaml
    data/habitats/host_associated/cyst.yaml data/habitats/host_associated/decayed_wood__afd3403c.yaml
    data/habitats/host_associated/decomposed_body.yaml data/habitats/host_associated/decomposed_body__7ba62861.yaml
    data/habitats/host_associated/decomposed_body__ee215354.yaml data/habitats/host_associated/dental_abscess.yaml
    data/habitats/host_associated/dental_calculus.yaml data/habitats/host_associated/dental_calculus__18e49dca.yaml
    data/habitats/host_associated/dental_calculus__8a0a99ac.yaml data/habitats/host_associated/dental_plaque.yaml
    data/habitats/host_associated/dental_plaque__384bd6e9.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/crustacean_maxillary_gland.yaml
    data/habitats/host_associated/crustacean_post_larval_stage.yaml data/habitats/host_associated/cryptomonads_cryptophytes.yaml
    data/habitats/host_associated/ctenophora.yaml data/habitats/host_associated/cud.yaml
    data/habitats/host_associated/cutaneous_leishmaniasis.yaml data/habitats/host_associated/cuticle.yaml
    data/habitats/host_associated/cuticle__11d6cb22.yaml data/habitats/host_associated/cuticle__6c2a3dac.yaml
    data/habitats/host_associated/cuticle__72f050c4.yaml data/habitats/host_associated/cuticle__9784f327.yaml
    data/habitats/host_associated/cuticle__a024212e.yaml data/habitats/host_associated/cv_1_cell.yaml
    data/habitats/host_associated/cyst.yaml data/habitats/host_associated/decayed_wood__afd3403c.yaml
    data/habitats/host_associated/decomposed_body.yaml data/habitats/host_associated/decomposed_body__7ba62861.yaml
    data/habitats/host_associated/decomposed_body__ee215354.yaml data/habitats/host_associated/dental_abscess.yaml
    data/habitats/host_associated/dental_calculus.yaml data/habitats/host_associated/dental_calculus__18e49dca.yaml
    data/habitats/host_associated/dental_calculus__8a0a99ac.yaml data/habitats/host_associated/dental_plaque.yaml
    data/habitats/host_associated/dental_plaque__384bd6e9.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:35:44Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/crustacean_maxillary_gland.yaml data/habitats/host_associated/crustacean_post_larval_stage.yaml\
    \ data/habitats/host_associated/cryptomonads_cryptophytes.yaml data/habitats/host_associated/ctenophora.yaml\
    \ data/habitats/host_associated/cud.yaml data/habitats/host_associated/cutaneous_leishmaniasis.yaml\
    \ data/habitats/host_associated/cuticle.yaml data/habitats/host_associated/cuticle__11d6cb22.yaml\
    \ data/habitats/host_associated/cuticle__6c2a3dac.yaml data/habitats/host_associated/cuticle__72f050c4.yaml\
    \ data/habitats/host_associated/cuticle__9784f327.yaml data/habitats/host_associated/cuticle__a024212e.yaml\
    \ data/habitats/host_associated/cv_1_cell.yaml data/habitats/host_associated/cyst.yaml\
    \ data/habitats/host_associated/decayed_wood__afd3403c.yaml data/habitats/host_associated/decomposed_body.yaml\
    \ data/habitats/host_associated/decomposed_body__7ba62861.yaml data/habitats/host_associated/decomposed_body__ee215354.yaml\
    \ data/habitats/host_associated/dental_abscess.yaml data/habitats/host_associated/dental_calculus.yaml\
    \ data/habitats/host_associated/dental_calculus__18e49dca.yaml data/habitats/host_associated/dental_calculus__8a0a99ac.yaml\
    \ data/habitats/host_associated/dental_plaque.yaml data/habitats/host_associated/dental_plaque__384bd6e9.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C11
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: 'Finished 2026-10-16T08:35:55Z. No issues found

    839 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C12
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:35:56Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C13
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:36:18Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C14
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:36:23Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C15
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:36:46Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C16
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:37:48Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C17
  name: uv run pytest -q tests/test_cuticle_dental_review_repairs.py --no-cov
  status: passed
  required: true
  command: uv run pytest -q tests/test_cuticle_dental_review_repairs.py --no-cov
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: 'Finished 2026-10-16T08:37:58Z. ..                                                                       [100%]

    2 passed in 7.86s'
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C18
  name: uv run ruff check .
  status: passed
  required: true
  command: uv run ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: Finished 2026-10-16T08:37:58Z. All checks passed!
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C19
  name: git diff --check
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: 'Finished 2026-10-16T08:38:00Z. '
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C20
  name: uv run pytest -q tests/test_decisions.py::test_curation_notes_do_not_cite_evidence_that_does_not_exist
    tests/test_cuticle_dental_review_repairs.py --no-cov
  status: passed
  required: true
  command: uv run pytest -q tests/test_decisions.py::test_curation_notes_do_not_cite_evidence_that_does_not_exist
    tests/test_cuticle_dental_review_repairs.py --no-cov
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: 'Finished 2026-10-16T08:38:15Z. ...                                                                      [100%]

    3 passed in 13.36s'
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C21
  name: just term-requests
  status: passed
  required: true
  command: just term-requests
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:35:45Z. wrote curation/term_requests/envo_robot_template.tsv:\
    \ 110 ENVO terms from 110 source records\n\n25 examined-ungrounded record(s) still\
    \ have no request written. Top by volume:\n      438  Medical-environment    \
    \            habitatmech:BACDIVE.5e52ea1bba\n      228  Fruit-Seed           \
    \              habitatmech:BACDIVE.ba016fe448\n       35  Egg                \
    \                habitatmech:BACDIVE.d48ce9485d\n        5  Caeca: Bacteriome\
    \                  habitatmech:GOLD.2d506b9526\n        3  Abdomen           \
    \                 habitatmech:GOLD.c6b0b54290\n        2  Crop               \
    \                habitatmech:GOLD.5446ce4c6d\n        1  Thalassic           \
    \               habitatmech:GOLD.3fece6dbf7\n        1  Crop                 \
    \              habitatmech:GOLD.57011086ca\n        0  Subtidal zone sediment\
    \             habitatmech:GOLD.785879d721\n        0  Subterranean lake      \
    \            habitatmech:GOLD.937bf682c4\n\ncovered 105842 upstream assertions;\
    \ 713 still unrequested across 25 record(s); 15 examined and deliberately not\
    \ asked for\n\n`created by` is empty: it wants pipe-delimited full ORCID IRIs\
    \ and this script cannot know them.\n uv run python scripts/build_term_requests.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C22
  name: just docs-stats
  status: passed
  required: true
  command: just docs-stats
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:36:09Z. updated README corpus statistics\n uv run\
    \ python scripts/check_docs.py --write"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C23
  name: just render
  status: passed
  required: true
  command: just render
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:36:51Z. rendered 3209 habitat pages, 259 redirect\
    \ stubs, 8 categories, 135 term requests -> /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages\n\
    \ uv run python scripts/render_pages.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C24
  name: just render-check
  status: passed
  required: true
  command: just render-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:37:36Z. rendered 3209 habitat pages, 259 redirect\
    \ stubs, 8 categories, 135 term requests -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmp29xf44zp/site\n\
    pages/ is in step with the corpus\n uv run python scripts/render_pages.py --check"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C25
  name: just redirects-check
  status: passed
  required: true
  command: just redirects-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: "Finished 2026-10-16T08:40:01Z. RETIRED.tsv is current (259 redirects)\n\
    \ uv run python scripts/build_redirects.py --check"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C26
  name: uv run ruff check .
  status: passed
  required: true
  command: uv run ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: Finished 2026-10-16T08:40:01Z. All checks passed!
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C27
  name: git diff --check
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: 'Finished 2026-10-16T08:40:01Z. '
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: CCI
  name: Exact-revision hosted authoritative QC and archive contract
  status: passed
  required: true
  command: gh run view 38875299816 --repo CultureBotAI/HabitatMech --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: Verified 2026-10-16T09:00:10Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38875299816
  scope_note: Repaired input/product commit before these successor outputs; final-head
    and merge-queue checks remain separate.
- check_id: CMAP
  name: Citation correction preserves semantic-map input bytes
  status: passed
  required: false
  command: cmp build/review-cs-map/current-inputs.jsonl build/review-cs-map/citation-inputs.jsonl
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.db17f52768
  summary: Finished 2026-10-16T08:35:14Z. Full 3209-record semantic JSONL is byte-identical
    before and after replacing PMID strings with their publication URLs.
  scope_note: This is a text-neutral citation correction, not a new embedding run
    or export-conformance audit.
evidence:
- evidence_id: EX8
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000167/graph
  locator: UBERON_0000167-graph.json
  accessed_at: '2026-10-16T07:15:14Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000167",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002553", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000167",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000165", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 02734b2eb6562f2f1529c0468349a071d21d004af7efdec99c99683567afeb41
- evidence_id: EX9
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000167
  locator: UBERON_0000167.json
  accessed_at: '2026-10-16T07:15:13Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:0000167", "label": "oral cavity", "is_obsolete": false, "description":
    ["Anatomical cavity at the start of the digestive tract that that is enclosed
    by the mouth. The boundaries and contents vary depending on the species. In vertebrates,
    the boundaries are the oral opening, the cheeks, the palate and (if present) the
    palatoglossal arch - if this is not present then the mouth and pharynx form the
    oropharyngeal cavity. The buccal cavity contains the teeth, tongue and palate
    (when present)."], "obo_synonym": [{"name": "buccal cavity", "scope": "hasExactSynonym",
    "type": null, "xrefs": [{"database": "FMA", "id": "20292", "description": null,
    "url": "http://purl.org/sig/ont/fma/20292"}, {"database": "ISBN", "id": "0073040584",
    "description": null, "url": "https://www.worldcat.org/search?q=bn%3A0073040584"}]}],
    "annotation": {"database_cross_reference": ["AAO:0000053", "AAO:0000960", "BSA:0000107",
    "CALOHA:TS-1315", "EFO:0001975", "EHDAA2:0001324", "EHDAA:6970", "EMAPA:17411",
    "EMAPA:18399", "EV:0100057", "FMA:20292", "HAO:0000669", "NCIT:C12421", "SCTID:181220002",
    "TAO:0001027", "TGMA:0000102", "VHOG:0000188", "WBbt:0005255", "XAO:0000126",
    "ZFA:0001027", "MESH:D009055", "UMLS:C0226896"], "external_definition": ["Anatomical
    cavity bounded anteriorly by the mouth and posteriorly by the derivatives of the
    branchial arches.[AAO]", "The cavity of the mouth, bounded by the jaw bones and
    associated structures (muscles and mucosa). [TFD][VHOG]"], "homology_notes": ["Echinoderms,
    hemichordates, and chordates are called deuterostomes because the mouth arises
    not from the blastopore but from a second invagination at the anterior end of
    the larva that pushes in to connect with the archenteron.[well established][VHOG]"],
    "id": ["UBERON:0000167"]}}'
  snapshot_sha256: 8d79e64c21ee4a6fad9f941f6740fd3817591fcbe4a2a787cc966f9100860500
- evidence_id: EW10
  kind: authority
  reference: https://medlineplus.gov/ency/article/001060.htm
  locator: Definition and causes paragraphs
  accessed_at: '2026-10-16T07:37:11Z'
  support: context_only
  summary: The authority describes a localized pus collection from bacterial infection
    in or around a tooth. This directly challenges a blanket not-a-place rationale
    without identifying the exact GOLD samples. Inspected through the web reader this
    session; no full-page byte snapshot claimed.
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/dental_abscess.yaml
  locator: Entire regenerated target YAML
  accessed_at: '2026-10-16T09:00:42Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.db17f52768", "label": "Dental abscess",
    "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NOT_APPLICABLE", "mapping_status":
    "REVIEWED", "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6345",
    "source_label": "Dental abscess", "source_path": "Host-associated > Mammals: Human
    > Digestive system > Oral cavity > Dental abscess", "assertion_count": 5, "assertion_unit":
    "ORGANISM"}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator":
    "claude-opus-5", "action": "NOT_APPLICABLE", "changes": "Marked NOT_APPLICABLE:
    the source concept does not denote a habitat. ''Dental abscess'' names a disease,
    an intervention, a sampling artefact or a no-value filler rather than a place.
    Pulled out of the class-level sweep and decided individually. (source concept
    habitatmech:GOLD.db17f52768)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator":
    "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from
    data/raw/ inventories; attested by GOLD. Grounding: NOT_APPLICABLE."}, {"timestamp":
    "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.99880772e1
    for habitatmech:GOLD.db17f52768 (Host-associated > Mammals: Human > Digestive
    system > Oral cavity > Dental abscess). Review https://github.com/CultureBotAI/HabitatMech/issues/2235
    : Maxillary gland is not the entire excretory system; cud is not the stomach;
    cuticle is not the whole integument, integumentary system or skin; abscess, calculus
    and plaque are not the whole oral cavity. Exclude only exact guarded GOLD source-path
    contributions, preserving independent genera and all source observations. Exact
    target habitatmech:GOLD.db17f52768. Other identity, status and mapping findings
    remain separate."}]}'
  snapshot_sha256: 14df7e1859a2d23635276a8fe17a1a9381e59307060f16b06148220c5e0b3254
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261016T073711Z-dental_abscess-record/review.yaml
  locator: Every immutable baseline finding
  accessed_at: '2026-10-16T09:00:42Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; the original inspected
    source scope is preserved.
  snapshot_sha256: 69567a9f5199b7883a75ad098d68cba413ea389e9dc02413349ce3b4e2fbe191
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_cuticle_dental_review_repairs.py
  locator: Complete full-corpus counterfactual
  accessed_at: '2026-10-16T09:00:42Z'
  support: supports
  summary: Exactly ten records differ. Only guarded context-parent removal and three
    arthropod grounding/predicate/status corrections change scientific fields; all
    source observations and unrelated fields are invariant.
  snapshot_sha256: bfa65736cdf7252a34180b268b0e56e4ef25970cf3308b0f84658f3f731b6ed5
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict hierarchy, ITEM decisions and source units
  accessed_at: '2026-10-16T09:00:42Z'
  support: supports
  summary: Native history/status follows maintained rows; generated artifacts are
    not hand-edited.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EH40
  kind: record_content
  reference: history/mappings/cuticle_dental_review_citations/2026-10-16T083223Z-codex-gpt-5-c42651.yaml
  locator: Complete session event
  accessed_at: '2026-10-16T09:00:42Z'
  support: supports
  summary: Authorized curation by codex-gpt-5; maintained owner and issue retained.
  snapshot_sha256: f0a7f6577764a3dc69c894b8c6dffc7cac78a08a1d7f9f8a4c990bf6d9382a0e
- evidence_id: EH41
  kind: record_content
  reference: history/mappings/cuticle_dental_review_mineral/2026-10-16T074759Z-codex-gpt-5-d2d9db.yaml
  locator: Complete session event
  accessed_at: '2026-10-16T09:00:42Z'
  support: supports
  summary: Authorized curation by codex-gpt-5; maintained owner and issue retained.
  snapshot_sha256: b2d4696ff2e86b972d0083c191362137f20c3c1c9e6a1b1d8f23c0051d03c3fa
- evidence_id: EH42
  kind: record_content
  reference: history/mappings/cuticle_dental_review_parents/2026-10-16T074758Z-codex-gpt-5-56d722.yaml
  locator: Complete session event
  accessed_at: '2026-10-16T09:00:42Z'
  support: supports
  summary: Authorized curation by codex-gpt-5; maintained owner and issue retained.
  snapshot_sha256: 557e55252578fe0c8d3d92eb3054ae15a96973790ef9048f0b9cdbdd90af98cd
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact physical TSV rows
  accessed_at: '2026-10-16T09:00:43Z'
  support: supports
  summary: '[[9, "habitatmech:GOLD.db17f52768\tHost-associated > Mammals: Human >
    Digestive system > Oral cavity > Dental abscess\thabitatmech:GOLD.99880772e1\tcodex-gpt-5\t2026-10-16\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2235 : Maxillary gland is not
    the entire excretory system; cud is not the stomach; cuticle is not the whole
    integument, integumentary system or skin; abscess, calculus and plaque are not
    the whole oral cavity. Exclude only exact guarded GOLD source-path contributions,
    preserving independent genera and all source observations. Exact target habitatmech:GOLD.db17f52768.
    Other identity, status and mapping findings remain separate."]]'
  snapshot_sha256: 1675ec9acca1f4fe6b1101188aafbc10f3cf6d2fabfd149232ec0260262a311f
- evidence_id: EDECISION
  kind: record_content
  reference: curation/decisions.tsv
  locator: Exact physical TSV rows
  accessed_at: '2026-10-16T09:00:44Z'
  support: supports
  summary: '[[1230, "habitatmech:GOLD.db17f52768\tNOT_APPLICABLE\t\t\t\tclaude-opus-5\t2026-08-12\t''Dental
    abscess'' names a disease, an intervention, a sampling artefact or a no-value
    filler rather than a place. Pulled out of the class-level sweep and decided individually.\tITEM\t\t"]]'
  snapshot_sha256: bd080045e44f1995788c20df1ea1e71e3fe8d2dc44a3730f8618c8f133e2341a
assessments:
- assessment_id: A1
  area: consistency
  topic: Bounded correction and exact preservation
  outcome: supported
  summary: Removed the guarded GOLD context-parent contribution. Identity and native
    status are unchanged. Source observations and independent valid genera are preserved.
    Remaining predecessor findings are explicitly open.
  target_ids:
  - habitatmech:GOLD.db17f52768
  evidence_ids:
  - EX8
  - EX9
  - EW10
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
- assessment_id: A2
  area: identity
  topic: Current anatomical identity and hierarchy
  outcome: concern
  summary: 'habitatmech:GOLD.db17f52768: Dental abscess; NOT_APPLICABLE/REVIEWED;
    parents []. Source anatomy/material scope remains as assessed in the baseline;
    only the documented false parents are removed. No replacement identity, genus
    or definition is fabricated. Dental-abscess status remains provisional.'
  target_ids:
  - habitatmech:GOLD.db17f52768
  evidence_ids:
  - EX8
  - EX9
  - EW10
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
- assessment_id: A3
  area: quantity
  topic: Units, counts and observations
  outcome: supported
  summary: '[{"source": "GOLD", "source_id": "gold.ecosystem:6345", "source_label":
    "Dental abscess", "source_path": "Host-associated > Mammals: Human > Digestive
    system > Oral cavity > Dental abscess", "assertion_count": 5, "assertion_unit":
    "ORGANISM"}]. Original counts/units, taxa, scores and parameters are preserved,
    not interpreted as prevalence or viability.'
  target_ids:
  - habitatmech:GOLD.db17f52768
  evidence_ids:
  - EX8
  - EX9
  - EW10
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
- assessment_id: A4
  area: representation
  topic: Predecessor reconciliation
  outcome: concern
  summary: 'Every previous finding keeps its stable issue key and exact lineage. Removing
    three unsupported narrow matches does not resolve global mapping contract #1398.'
  target_ids:
  - habitatmech:GOLD.db17f52768
  evidence_ids:
  - EX8
  - EX9
  - EW10
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
- assessment_id: A5
  area: completeness
  topic: Evidence and lifecycle boundaries
  outcome: supported
  summary: Only the three explicit arthropod ITEM decisions change native status.
    Optional definitions, causal mechanisms and biological absence claims are not
    invented. The complete target, remaining parents, history and original evidence
    were rechecked.
  target_ids:
  - habitatmech:GOLD.db17f52768
  evidence_ids:
  - EX8
  - EX9
  - EW10
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
findings:
- finding_id: F1
  issue_key: dental-abscess-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is not a strictly broader habitat class
  description: Removed only the guarded GOLD source-context contribution habitatmech:GOLD.99880772e1.
    Independent valid parents and every source observation remain intact.
  target_ids:
  - habitatmech:GOLD.db17f52768
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX8
  - EX9
  - EW10
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2235
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T073711Z-dental_abscess-record
    finding_id: F1
  disposition_reason: Removed only the guarded GOLD source-context contribution habitatmech:GOLD.99880772e1.
    Independent valid parents and every source observation remain intact.
- finding_id: F2
  issue_key: dental-abscess-abscess-habitat-status
  category: identity
  severity: major
  status: open
  certainty: provisional
  title: NOT_APPLICABLE rationale omits the localized abscess-material sense
  description: The whole-cavity parent is removed, but the localized pus/material
    interpretation still requires original source assertions before changing NOT_APPLICABLE.
    Its provisional status is retained.
  target_ids:
  - habitatmech:GOLD.db17f52768
  field_paths:
  - grounding_status
  - curation_history
  evidence_ids:
  - EX8
  - EX9
  - EW10
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2237
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T073711Z-dental_abscess-record
    finding_id: F2
  disposition_reason: The whole-cavity parent is removed, but the localized pus/material
    interpretation still requires original source assertions before changing NOT_APPLICABLE.
    Its provisional status is retained.
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.db17f52768
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  description: The ITEM decision categorically calls Dental abscess not a place, yet
    the inspected authority describes a localized pus collection caused by bacterial
    infection. This is a material/site sense that the generic disease/filler rationale
    does not address. Verify the five organism assertions and original source intent
    before revising NOT_APPLICABLE or defining an abscess-associated habitat. Independently,
    a localized collection is not a kind of whole oral cavity, so the inherited cavity
    parent is not strictly broader. No clinical treatment recommendation follows from
    this representation review. Inspect the original five source assertions and replace
    the blanket rationale with a source-intent decision; no new exact ontology identity
    is preselected. Proposed work only; no repair or status promotion is performed
    by this review.
  generator: Controlled source/input correction, just seed, inspected just seed-canary,
    guarded just seed-apply, and dependent term-request/map/site/redirect regeneration
    where required.
  acceptance_checks:
  - Regress the exact target claim and preserve valid genera, identifiers, source
    counts/units and taxon associations. Recover original evidence before deleting
    a provisional pair; do not decrement frozen totals by hand.
  - Record authorized curation history; require schema, strict, provenance, history,
    label, corpus, site and full QC gates.
  - Save an immutable successor with the same issue key and exact predecessor finding
    identity.
limitations:
- Original specimen-level evidence was not exhaustively reconstructed. Source counts,
  associations and scores do not establish prevalence, viability or characteristic
  presence.
- Configured id-label validation skips 2063 no-adapter pairs; the 18 displayed target
  TaxIds were separately checked against current NCBI.
- 'iModulonDB is not applicable: these records assert no genes, regulators, pathways
  or expression modules. Literature mechanisms were not imported as causal graphs.'
- Same-agent disposition, not independent human approval. Final-head and merge-queue
  checks remain separate publication gates. Whole-corpus scientific review and current
  kg-microbe export conformance are incomplete.
notes:
- All earlier saved bundles and session histories remain unchanged. Preserve the exact
  off-main input base with an annotated provenance tag before squash merge and branch
  deletion.
- 'A preliminary unsaved capture at b3b87caf3d56b74891036c9d3c1c201f07388c63 was retained
  separately. CI #2240 required publication URLs instead of PMID CURIEs in three decision
  notes; after that formatting correction and regeneration, inputs were freshly captured
  and the complete targets reassessed. No prior saved review was refreshed or rewritten.'
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261016T073711Z-dental_abscess-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
