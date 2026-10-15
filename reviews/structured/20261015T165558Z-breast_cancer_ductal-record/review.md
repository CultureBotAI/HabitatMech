# Record review: Breast cancer: Ductal (habitatmech:GOLD.1064d1667e)

- Review: 20261015T165558Z-breast_cancer_ductal-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T16:30:16Z
- Finished UTC: 2026-10-15T16:55:58Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The ductal breast-cancer leaf is a distinct GOLD source, not a child of the generic breast-cancer record. NCI describes ductal carcinoma arising in duct lining, with in-situ and invasive forms; neither implies a whole duct habitat identity. Ten biosamples and one sixteen-path study membership do not settle disease versus sampled tumor material. Resolve that ITEM-level distinction and remove disease taxonomy from habitat ancestry.

## Scope And Provenance

Full field-by-field scientific review of this one exact target at 50dbf8b388bf32ca58708f7993e83120310f7cea.

Selection: One of the next 24 path-ordered unreviewed targets in an ignored-inclusive 3208-record census. This bundle assesses only this identifier, not a cohort sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 50dbf8b388bf32ca58708f7993e83120310f7cea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.1064d1667e | data/habitats/host_associated/breast_cancer_ductal.yaml | generated | Breast cancer: Ductal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.1064d1667e | Completed 2026-10-15T16:34:33Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/breast_cancer_ductal.yaml |
| validate-strict | passed | True | habitatmech:GOLD.1064d1667e | Completed 2026-10-15T16:35:27Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.1064d1667e | Completed 2026-10-15T16:35:39Z. No issues found<br>814 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.1064d1667e | Completed 2026-10-15T16:35:39Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.1064d1667e | Completed 2026-10-15T16:36:01Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.1064d1667e | Completed 2026-10-15T16:36:06Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.1064d1667e | Completed 2026-10-15T16:36:35Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.1064d1667e | Completed 2026-10-15T16:37:38Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | habitatmech:GOLD.1064d1667e | Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320 |

## Scientific And Domain Assessments

### Identity, definition, hierarchy and aliases

identity: concern. Targets: habitatmech:GOLD.1064d1667e.

The ductal breast-cancer leaf is a distinct GOLD source, not a child of the generic breast-cancer record. NCI describes ductal carcinoma arising in duct lining, with in-situ and invasive forms; neither implies a whole duct habitat identity. Ten biosamples and one sixteen-path study membership do not settle disease versus sampled tumor material. Resolve that ITEM-level distinction and remove disease taxonomy from habitat ancestry.

### Frozen counts, units, ranks, channels and scores

quantity: supported. Targets: habitatmech:GOLD.1064d1667e.

Every source assertion and displayed taxon was checked against its exact raw row. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Side-table biosample/study counts are not added to tree ORGANISM counts. Zero-count omission is not biological absence.

### Scientific support and scope limits

evidence: concern. Targets: habitatmech:GOLD.1064d1667e.

The ductal breast-cancer leaf is a distinct GOLD source, not a child of the generic breast-cancer record. NCI describes ductal carcinoma arising in duct lining, with in-situ and invasive forms; neither implies a whole duct habitat identity. Ten biosamples and one sixteen-path study membership do not settle disease versus sampled tumor material. Resolve that ITEM-level distinction and remove disease taxonomy from habitat ancestry.

### Status, optional content, triads and mechanisms

completeness: supported. Targets: habitatmech:GOLD.1064d1667e.

Actual routes reproduce UNGROUNDED/SEEDED. No environmental-parameter, causal-edge, discussion/dataset or is_characteristic=true assertion is present in this target. Optional absence and SEEDED status alone are not defects. Scientific review does not promote native status.

### Native deterministic validation

schema: supported. Targets: habitatmech:GOLD.1064d1667e.

Ordinary and strict schemas, 814 history records, provenance, 3208-record reproduction, 32 causal overlays, term-request checks, configured labels and exact-base full QC passed. These establish fidelity, not biological truth.

## Findings

### F1: Cancer classification is published as broader habitat ancestry

major / open / confirmed; issue key: breast-cancer-ductal-disease-taxonomy-parent.

The retained Carcinoma parent habitatmech:GOLD.9bb307824f is ITEM NOT_APPLICABLE. Clinical subclass membership does not make it a broader habitat. Suppress this exact GOLD parent contribution while retaining the full disease source path; any future structured clinical hierarchy needs a distinct typed relation. This does not by itself change the child disposition.

### F2: Resolve diagnosis versus sampled tumor habitat at item level

major / open / provisional; issue key: breast-cancer-ductal-disease-versus-tumor-scope.

The ductal breast-cancer leaf is a distinct GOLD source, not a child of the generic breast-cancer record. NCI describes ductal carcinoma arising in duct lining, with in-situ and invasive forms; neither implies a whole duct habitat identity. Ten biosamples and one sixteen-path study membership do not settle disease versus sampled tumor material. Resolve that ITEM-level distinction and remove disease taxonomy from habitat ancestry. Inspect exact source specimens before selecting NOT_APPLICABLE for a diagnostic bucket or defining a tumor-material habitat. Do not treat cancer, a normal mammary gland, its duct, or lobule as interchangeable identities.

## Recommended Actions And Acceptance Checks

### ACT1

The retained Carcinoma parent habitatmech:GOLD.9bb307824f is ITEM NOT_APPLICABLE. Clinical subclass membership does not make it a broader habitat. Suppress this exact GOLD parent contribution while retaining the full disease source path; any future structured clinical hierarchy needs a distinct typed relation. This does not by itself change the child disposition. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identifiers, counts/units and raw provenance. Change identity, native status or mapping only when separately supported by the scoped item assessment; never change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

The ductal breast-cancer leaf is a distinct GOLD source, not a child of the generic breast-cancer record. NCI describes ductal carcinoma arising in duct lining, with in-situ and invasive forms; neither implies a whole duct habitat identity. Ten biosamples and one sixteen-path study membership do not settle disease versus sampled tumor material. Resolve that ITEM-level distinction and remove disease taxonomy from habitat ancestry. Inspect exact source specimens before selecting NOT_APPLICABLE for a diagnostic bucket or defining a tumor-material habitat. Do not treat cancer, a normal mammary gland, its duct, or lobule as interchangeable identities. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identifiers, counts/units and raw provenance. Change identity, native status or mapping only when separately supported by the scoped item assessment; never change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/breast_cancer_ductal.yaml; Entire target YAML | supports | Entire record read: identity, definition, parents, source attestations, every displayed taxon and complete history. |
| ERULE | docs/CURATION.md; Host, anatomy, hierarchy, disposition and evidence rules | supports | Parent_habitats means strictly broader; source occurrence does not establish characteristic presence. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord and SourceAttestation slots | supports | Typed identity, broader habitat and source-to-record mapping semantics; optional fields are not mandatory. |
| ESEED | src/habitatmech/seed.py; Executed build_corpus/apply_decision routes and parent accumulation | supports | Full target equality was verified against actual generated document. Exact source routes: [{"mint": "habitatmech:GOLD.1064d1667e", "automatic": {"identifier": "habitatmech:GOLD.1064d1667e", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.1064d1667e", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_unmatched", "category": null, "reviewed": false, "decision": {"identifier": "habitatmech:GOLD.1064d1667e", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Frozen inventory projection | supports | Source counts and taxon ranks/scores preserve source units; PREGO projections do not retain original pair-level citations. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 2328 | supports | [{"row": 2328, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Breast cancer: Ductal", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_type": "Malignant tumor", "ecosystem_subtype": "Carcinoma", "specific_ecosystem": "Breast cancer: Ductal", "leaf_label": "Breast cancer: Ductal", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:6174"}}] |
| ET6 | data/raw/gold_path_biosamples.tsv; Physical TSV rows 639 | supports | [{"row": 639, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Breast cancer: Ductal", "ecosystem_path_id": "6174", "biosample_count": "10"}}] |
| ET7 | data/raw/gold_studies.tsv; Physical TSV rows 3099 | supports | [{"row": 3099, "data": {"study_gold_id": "Gs0150275", "path_count": "16", "paths": "Host-associated &gt; Mammals: Human &gt; Abdominal/Peritoneal cavity &gt; Ascites &gt; Malignant ascites&#124;Host-associated &gt; Mammals: Human &gt; Circulatory system &gt; Blood&#124;Host-associated &gt; Mammals: Human &gt; Digestive system &gt; Large intestine &gt; Colon mucosa&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Basal cell carcinoma&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Breast cancer: Ductal&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Breast cancer: Lobular&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Colon cancer&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Oral cavity cancer&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma &gt; Ovarian cancer&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Germ cell tumor &gt; Testicular non-seminoma&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Germ cell tumor &gt; Testicular seminoma&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Lymphoma &gt; Diffuse large B-cell lymphoma&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Lymphoma &gt; Lymphoblastic lymphoma&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Lymphoma &gt; Mycosis fungoides/Cutaneous T-cell lymphoma&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Melanoma&#124;Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Myeloma &gt; Multiple myeloma"}}] |
| ET8 | curation/decisions.tsv; Physical TSV rows 196 | supports | [{"row": 196, "data": {"identifier": "habitatmech:GOLD.1064d1667e", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS", "category": "", "relation": ""}}] |
| EP9 | data/habitats/host_associated/carcinoma.yaml; Full parent record, context only | supports | {"identifier": "habitatmech:GOLD.9bb307824f", "label": "Carcinoma", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NOT_APPLICABLE", "mapping_status": "REVIEWED", "parent_habitats": ["habitatmech:GOLD.31d7fab4fa"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6172", "source_label": "Carcinoma", "source_path": "Host-associated &gt; Mammals: Human &gt; Malignant tumor &gt; Carcinoma", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "NOT_APPLICABLE", "changes": "Marked NOT_APPLICABLE: the source concept does not denote a habitat. 'Carcinoma' names a disease, an intervention, a sampling artefact or a no-value filler rather than a place. Pulled out of the class-level sweep and decided individually. (source concept habitatmech:GOLD.9bb307824f)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NOT_APPLICABLE."}]} |
| ELEGACY | reports/yaml_record_review/20260922T111550Z-breast_cancer_ductal.md; Findings and recommended edits; historical lead | supports | Legacy conclusions were compared with current target and primary evidence. No formal predecessor or automatic native-status requirement is inferred. |
| ENCI | https://www.cancer.gov/publications/dictionaries/cancer-terms/def/ductal-carcinoma; Rendered NCI dictionary entry, definition paragraphs | context_only | Official NCI definition distinguishes ductal carcinoma, duct-lining origin, in-situ disease and invasion outside the duct. Inspected rendered text via web tool. Raw HTTP returned a JavaScript shell and the attempted API route returned 404; neither was used as definition evidence. |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.1064d1667e -e 'Breast cancer: Ductal' -e breast_cancer_ductal -e habitatmech:GOLD.1064d1667e curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately from broad textual matches. No previous structured target observation was found; not every broad label match was inspected. |

## Limits And Additional Notes

- Historical specimens and every original association have not been independently reidentified. Counts, scores and ranked rows are not prevalence, viability, characteristic presence or mechanism.
- The label gate skips 2061 no-adapter pairs and does not certify taxon labels. Every displayed taxon ID was separately resolved through current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged input baseline, not a new local full-QC execution. These new review bundles require their native post-save archive check.
- iModulonDB is not applicable: no gene, regulator, transcriptomic module or causal mechanism is asserted. No paid research was used.
- Input hashes match both current working bytes and exact tracked base blobs; source.state git_commit describes that historical revision without silently refreshing inputs.
- Ignored-inclusive searches and parsed structured archive found no previous structured observation targeting this exact identifier. Legacy findings were inspected as leads, not adopted automatically or assigned false structured lineage.
- Review-only: no habitat curation, regeneration, status promotion, history mutation or GitHub mutation is performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T165558Z-breast_cancer_ductal-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Breast cancer: Ductal (habitatmech:GOLD.1064d1667e)'
started_at: '2026-10-15T16:30:16Z'
finished_at: '2026-10-15T16:55:58Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the target and evidence; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The ductal breast-cancer leaf is a distinct GOLD source, not a child of the
  generic breast-cancer record. NCI describes ductal carcinoma arising in duct lining,
  with in-situ and invasive forms; neither implies a whole duct habitat identity.
  Ten biosamples and one sixteen-path study membership do not settle disease versus
  sampled tumor material. Resolve that ITEM-level distinction and remove disease taxonomy
  from habitat ancestry.
source:
  git_revision: 50dbf8b388bf32ca58708f7993e83120310f7cea
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
    sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 6d5cbfd0f5ad911fbb074ee8ec253625d1fa13d94117759b1f25a1cd2e6576bc
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 903fc125adcd84df9fa99a4fae71b30d4a3541efc48eeff3cd49b94e866a5056
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: dfde49f64273cb94b4162170a5542c94880fa36015ccaac6edfa248820492a23
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
  - path: data/habitats/host_associated/breast_cancer_ductal.yaml
    sha256: bbb79704a0d871073d9774f7b6d8d4d4303060b818b0f0a451838a569addd92e
    role: target
  - path: data/habitats/host_associated/carcinoma.yaml
    sha256: 7eae8fe197c614d3c985fd20ee22c71f561c209433bf33c544a774ddb37b8fe8
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
  - path: reports/yaml_record_review/20260922T111550Z-breast_cancer_ductal.md
    sha256: 7e043e5bf4a33c71cedbf71569d7bf923dbb751eb88ff046d15c93ebfec660d3
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
targets:
- target_id: habitatmech:GOLD.1064d1667e
  path: data/habitats/host_associated/breast_cancer_ductal.yaml
  label: 'Breast cancer: Ductal'
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
  description: Full field-by-field scientific review of this one exact target at 50dbf8b388bf32ca58708f7993e83120310f7cea.
  selection: One of the next 24 path-ordered unreviewed targets in an ignored-inclusive
    3208-record census. This bundle assesses only this identifier, not a cohort sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.1064d1667e
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context is not additional coverage. Export compatibility and original
      individual source specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/breast_cancer_ductal.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1064d1667e
  summary: "Completed 2026-10-15T16:34:33Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/breast_cancer_ductal.yaml"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml
    data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml
    data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml
    data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml
    data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml
    data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml
    data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml
    data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml
    data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml
    data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml
    data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml
    data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1064d1667e
  summary: "Completed 2026-10-15T16:35:27Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/bovinae_cow_cattle.yaml data/habitats/host_associated/bowens_disease_squamous_cell_carcinoma_in_situ.yaml\
    \ data/habitats/host_associated/brain.yaml data/habitats/host_associated/brain__7bf4166c.yaml\
    \ data/habitats/host_associated/brain__803f6884.yaml data/habitats/host_associated/brain__b2bb2ba8.yaml\
    \ data/habitats/host_associated/brain__e9ca95b7.yaml data/habitats/host_associated/brain__f0593337.yaml\
    \ data/habitats/host_associated/brain_cell_line.yaml data/habitats/host_associated/brain_stem.yaml\
    \ data/habitats/host_associated/breast.yaml data/habitats/host_associated/breast_abscess.yaml\
    \ data/habitats/host_associated/breast_cancer.yaml data/habitats/host_associated/breast_cancer_ductal.yaml\
    \ data/habitats/host_associated/breast_cancer_lobular.yaml data/habitats/host_associated/breast_cyst.yaml\
    \ data/habitats/host_associated/breviatea.yaml data/habitats/host_associated/bronchi.yaml\
    \ data/habitats/host_associated/bronchi__3fb23b44.yaml data/habitats/host_associated/bronchi__c8c64428.yaml\
    \ data/habitats/host_associated/bronchial_epithelial_cell.yaml data/habitats/host_associated/bronchiole.yaml\
    \ data/habitats/host_associated/bronchoalveolar_lavage_fluid.yaml data/habitats/host_associated/bronchus.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1064d1667e
  summary: 'Completed 2026-10-15T16:35:39Z. No issues found

    814 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1064d1667e
  summary: "Completed 2026-10-15T16:35:39Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1064d1667e
  summary: "Completed 2026-10-15T16:36:01Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1064d1667e
  summary: "Completed 2026-10-15T16:36:06Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1064d1667e
  summary: "Completed 2026-10-15T16:36:35Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1064d1667e
  summary: "Completed 2026-10-15T16:37:38Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for this target; strict for all 24 selected targets;
    remaining checks use documented full-corpus scope.
- check_id: CCI
  name: Exact-baseline full QC
  status: passed
  required: true
  command: gh run view 38764995320 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1064d1667e
  summary: Verified 2026-10-15T16:29:56Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38764995320
  scope_note: Exact unchanged scientific input baseline; new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/breast_cancer_ductal.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: 'Entire record read: identity, definition, parents, source attestations,
    every displayed taxon and complete history.'
  snapshot_sha256: bbb79704a0d871073d9774f7b6d8d4d4303060b818b0f0a451838a569addd92e
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host, anatomy, hierarchy, disposition and evidence rules
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: Parent_habitats means strictly broader; source occurrence does not establish
    characteristic presence.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord and SourceAttestation slots
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: Typed identity, broader habitat and source-to-record mapping semantics;
    optional fields are not mandatory.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed build_corpus/apply_decision routes and parent accumulation
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: 'Full target equality was verified against actual generated document. Exact
    source routes: [{"mint": "habitatmech:GOLD.1064d1667e", "automatic": {"identifier":
    "habitatmech:GOLD.1064d1667e", "grounding_status": "UNGROUNDED", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "gold_unmatched", "category": null, "reviewed": false, "decision": null}, "final":
    {"identifier": "habitatmech:GOLD.1064d1667e", "grounding_status": "UNGROUNDED",
    "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [],
    "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_unmatched",
    "category": null, "reviewed": false, "decision": {"identifier": "habitatmech:GOLD.1064d1667e",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep
    (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS",
    "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Frozen inventory projection
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: Source counts and taxon ranks/scores preserve source units; PREGO projections
    do not retain original pair-level citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 2328
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: '[{"row": 2328, "data": {"canonical_path": "Host-associated > Mammals:
    Human > Malignant tumor > Carcinoma > Breast cancer: Ductal", "ecosystem": "Host-associated",
    "ecosystem_category": "Mammals: Human", "ecosystem_type": "Malignant tumor", "ecosystem_subtype":
    "Carcinoma", "specific_ecosystem": "Breast cancer: Ductal", "leaf_label": "Breast
    cancer: Ductal", "depth": "5", "gold_node_count": "1", "organism_count": "0",
    "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids":
    "gold.ecosystem:6174"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/gold_path_biosamples.tsv
  locator: Physical TSV rows 639
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: '[{"row": 639, "data": {"canonical_path": "Host-associated > Mammals: Human
    > Malignant tumor > Carcinoma > Breast cancer: Ductal", "ecosystem_path_id": "6174",
    "biosample_count": "10"}}]'
  snapshot_sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
- evidence_id: ET7
  kind: database
  reference: data/raw/gold_studies.tsv
  locator: Physical TSV rows 3099
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: '[{"row": 3099, "data": {"study_gold_id": "Gs0150275", "path_count": "16",
    "paths": "Host-associated > Mammals: Human > Abdominal/Peritoneal cavity > Ascites
    > Malignant ascites|Host-associated > Mammals: Human > Circulatory system > Blood|Host-associated
    > Mammals: Human > Digestive system > Large intestine > Colon mucosa|Host-associated
    > Mammals: Human > Malignant tumor > Carcinoma > Basal cell carcinoma|Host-associated
    > Mammals: Human > Malignant tumor > Carcinoma > Breast cancer: Ductal|Host-associated
    > Mammals: Human > Malignant tumor > Carcinoma > Breast cancer: Lobular|Host-associated
    > Mammals: Human > Malignant tumor > Carcinoma > Colon cancer|Host-associated
    > Mammals: Human > Malignant tumor > Carcinoma > Oral cavity cancer|Host-associated
    > Mammals: Human > Malignant tumor > Carcinoma > Ovarian cancer|Host-associated
    > Mammals: Human > Malignant tumor > Germ cell tumor > Testicular non-seminoma|Host-associated
    > Mammals: Human > Malignant tumor > Germ cell tumor > Testicular seminoma|Host-associated
    > Mammals: Human > Malignant tumor > Lymphoma > Diffuse large B-cell lymphoma|Host-associated
    > Mammals: Human > Malignant tumor > Lymphoma > Lymphoblastic lymphoma|Host-associated
    > Mammals: Human > Malignant tumor > Lymphoma > Mycosis fungoides/Cutaneous T-cell
    lymphoma|Host-associated > Mammals: Human > Malignant tumor > Melanoma|Host-associated
    > Mammals: Human > Malignant tumor > Myeloma > Multiple myeloma"}}]'
  snapshot_sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
- evidence_id: ET8
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 196
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: '[{"row": 196, "data": {"identifier": "habitatmech:GOLD.1064d1667e", "decision":
    "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Class-level sweep
    (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate.", "review_depth": "CLASS",
    "category": "", "relation": ""}}]'
  snapshot_sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/carcinoma.yaml
  locator: Full parent record, context only
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.9bb307824f", "label": "Carcinoma", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "NOT_APPLICABLE", "mapping_status": "REVIEWED",
    "parent_habitats": ["habitatmech:GOLD.31d7fab4fa"], "source_attestations": [{"source":
    "GOLD", "source_id": "gold.ecosystem:6172", "source_label": "Carcinoma", "source_path":
    "Host-associated > Mammals: Human > Malignant tumor > Carcinoma", "notes": "2
    GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5",
    "action": "NOT_APPLICABLE", "changes": "Marked NOT_APPLICABLE: the source concept
    does not denote a habitat. ''Carcinoma'' names a disease, an intervention, a sampling
    artefact or a no-value filler rather than a place. Pulled out of the class-level
    sweep and decided individually. (source concept habitatmech:GOLD.9bb307824f)"},
    {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: NOT_APPLICABLE."}]}'
  snapshot_sha256: 7eae8fe197c614d3c985fd20ee22c71f561c209433bf33c544a774ddb37b8fe8
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20260922T111550Z-breast_cancer_ductal.md
  locator: Findings and recommended edits; historical lead
  accessed_at: '2026-10-15T16:55:58Z'
  support: supports
  summary: Legacy conclusions were compared with current target and primary evidence.
    No formal predecessor or automatic native-status requirement is inferred.
  snapshot_sha256: 7e043e5bf4a33c71cedbf71569d7bf923dbb751eb88ff046d15c93ebfec660d3
- evidence_id: ENCI
  kind: authority
  reference: https://www.cancer.gov/publications/dictionaries/cancer-terms/def/ductal-carcinoma
  locator: Rendered NCI dictionary entry, definition paragraphs
  accessed_at: '2026-10-15T16:48:58Z'
  support: context_only
  summary: Official NCI definition distinguishes ductal carcinoma, duct-lining origin,
    in-situ disease and invasion outside the duct. Inspected rendered text via web
    tool. Raw HTTP returned a JavaScript shell and the attempted API route returned
    404; neither was used as definition evidence.
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: 'rg --no-ignore --hidden -l -F -e habitatmech:GOLD.1064d1667e -e ''Breast
    cancer: Ductal'' -e breast_cancer_ductal -e habitatmech:GOLD.1064d1667e curation
    history research reports data/raw build reviews'
  accessed_at: '2026-10-15T16:33:57Z'
  support: context_only
  summary: Exact source/curation rows were parsed separately from broad textual matches.
    No previous structured target observation was found; not every broad label match
    was inspected.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    ignored and hidden files included, with all structured review.yaml files parsed.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, hierarchy and aliases
  outcome: concern
  summary: The ductal breast-cancer leaf is a distinct GOLD source, not a child of
    the generic breast-cancer record. NCI describes ductal carcinoma arising in duct
    lining, with in-situ and invasive forms; neither implies a whole duct habitat
    identity. Ten biosamples and one sixteen-path study membership do not settle disease
    versus sampled tumor material. Resolve that ITEM-level distinction and remove
    disease taxonomy from habitat ancestry.
  target_ids:
  - habitatmech:GOLD.1064d1667e
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ENCI
- assessment_id: A2
  area: quantity
  topic: Frozen counts, units, ranks, channels and scores
  outcome: supported
  summary: 'Every source assertion and displayed taxon was checked against its exact
    raw row. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Side-table biosample/study
    counts are not added to tree ORGANISM counts. Zero-count omission is not biological
    absence.'
  target_ids:
  - habitatmech:GOLD.1064d1667e
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - ENCI
- assessment_id: A3
  area: evidence
  topic: Scientific support and scope limits
  outcome: concern
  summary: The ductal breast-cancer leaf is a distinct GOLD source, not a child of
    the generic breast-cancer record. NCI describes ductal carcinoma arising in duct
    lining, with in-situ and invasive forms; neither implies a whole duct habitat
    identity. Ten biosamples and one sixteen-path study membership do not settle disease
    versus sampled tumor material. Resolve that ITEM-level distinction and remove
    disease taxonomy from habitat ancestry.
  target_ids:
  - habitatmech:GOLD.1064d1667e
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ENCI
- assessment_id: A4
  area: completeness
  topic: Status, optional content, triads and mechanisms
  outcome: supported
  summary: Actual routes reproduce UNGROUNDED/SEEDED. No environmental-parameter,
    causal-edge, discussion/dataset or is_characteristic=true assertion is present
    in this target. Optional absence and SEEDED status alone are not defects. Scientific
    review does not promote native status.
  target_ids:
  - habitatmech:GOLD.1064d1667e
  evidence_ids:
  - E1
  - ERULE
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native deterministic validation
  outcome: supported
  summary: Ordinary and strict schemas, 814 history records, provenance, 3208-record
    reproduction, 32 causal overlays, term-request checks, configured labels and exact-base
    full QC passed. These establish fidelity, not biological truth.
  target_ids:
  - habitatmech:GOLD.1064d1667e
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: breast-cancer-ductal-disease-taxonomy-parent
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Cancer classification is published as broader habitat ancestry
  description: The retained Carcinoma parent habitatmech:GOLD.9bb307824f is ITEM NOT_APPLICABLE.
    Clinical subclass membership does not make it a broader habitat. Suppress this
    exact GOLD parent contribution while retaining the full disease source path; any
    future structured clinical hierarchy needs a distinct typed relation. This does
    not by itself change the child disposition.
  target_ids:
  - habitatmech:GOLD.1064d1667e
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ENCI
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues: []
- finding_id: F2
  issue_key: breast-cancer-ductal-disease-versus-tumor-scope
  category: identity
  severity: major
  status: open
  certainty: provisional
  title: Resolve diagnosis versus sampled tumor habitat at item level
  description: The ductal breast-cancer leaf is a distinct GOLD source, not a child
    of the generic breast-cancer record. NCI describes ductal carcinoma arising in
    duct lining, with in-situ and invasive forms; neither implies a whole duct habitat
    identity. Ten biosamples and one sixteen-path study membership do not settle disease
    versus sampled tumor material. Resolve that ITEM-level distinction and remove
    disease taxonomy from habitat ancestry. Inspect exact source specimens before
    selecting NOT_APPLICABLE for a diagnostic bucket or defining a tumor-material
    habitat. Do not treat cancer, a normal mammary gland, its duct, or lobule as interchangeable
    identities.
  target_ids:
  - habitatmech:GOLD.1064d1667e
  field_paths:
  - grounding_status
  - mapping_status
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ENCI
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.1064d1667e
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: The retained Carcinoma parent habitatmech:GOLD.9bb307824f is ITEM NOT_APPLICABLE.
    Clinical subclass membership does not make it a broader habitat. Suppress this
    exact GOLD parent contribution while retaining the full disease source path; any
    future structured clinical hierarchy needs a distinct typed relation. This does
    not by itself change the child disposition. No repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independent identifiers, counts/units
    and raw provenance. Change identity, native status or mapping only when separately
    supported by the scoped item assessment; never change source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.1064d1667e
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: The ductal breast-cancer leaf is a distinct GOLD source, not a child
    of the generic breast-cancer record. NCI describes ductal carcinoma arising in
    duct lining, with in-situ and invasive forms; neither implies a whole duct habitat
    identity. Ten biosamples and one sixteen-path study membership do not settle disease
    versus sampled tumor material. Resolve that ITEM-level distinction and remove
    disease taxonomy from habitat ancestry. Inspect exact source specimens before
    selecting NOT_APPLICABLE for a diagnostic bucket or defining a tumor-material
    habitat. Do not treat cancer, a normal mammary gland, its duct, or lobule as interchangeable
    identities. No repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independent identifiers, counts/units
    and raw provenance. Change identity, native status or mapping only when separately
    supported by the scoped item assessment; never change source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Historical specimens and every original association have not been independently
  reidentified. Counts, scores and ranked rows are not prevalence, viability, characteristic
  presence or mechanism.
- The label gate skips 2061 no-adapter pairs and does not certify taxon labels. Every
  displayed taxon ID was separately resolved through current NCBI Taxonomy.
- Full QC evidence is a successful remote run at the exact unchanged input baseline,
  not a new local full-QC execution. These new review bundles require their native
  post-save archive check.
- 'iModulonDB is not applicable: no gene, regulator, transcriptomic module or causal
  mechanism is asserted. No paid research was used.'
notes:
- Input hashes match both current working bytes and exact tracked base blobs; source.state
  git_commit describes that historical revision without silently refreshing inputs.
- Ignored-inclusive searches and parsed structured archive found no previous structured
  observation targeting this exact identifier. Legacy findings were inspected as leads,
  not adopted automatically or assigned false structured lineage.
- 'Review-only: no habitat curation, regeneration, status promotion, history mutation
  or GitHub mutation is performed.'
tags:
- individual-scientific-review
- host-associated
```
