# Record review: Bone (habitatmech:GOLD.1e2686ea7e)

- Review: 20261015T145136Z-bone-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T14:33:37Z
- Finished UTC: 2026-10-15T14:51:36Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact human Fossilized remains path distinguishes this zero-tree-count Bone source from living-anatomy siblings. A fossil can host microbes, but the unreviewed BTO hard-connective-tissue genus needs a material-state assessment: fossilized material need not retain the organic tissue components in that definition. Fossilized remains may denote a material class, so its parent is not automatically rejected as a whole-body container. The narrow endpoint issue is independently confirmed.

## Scope And Provenance

Full scientific assessment of one exact target at b558fd561286d1fe3ba133784776f7be1f9f49fb.

Selection: One of the next 21 path-ordered unreviewed records, blood through bone marrow; this bundle assesses only this identifier.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base b558fd561286d1fe3ba133784776f7be1f9f49fb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.1e2686ea7e | data/habitats/host_associated/bone.yaml | generated | Bone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.1e2686ea7e | Completed 2026-10-15T14:35:14Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bone.yaml |
| validate-strict | passed | True | habitatmech:GOLD.1e2686ea7e | Completed 2026-10-15T14:36:08Z. uv run python scripts/validate_strict.py data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml data/habitats/host_associated/bone_marrow__c1fc5dec.yaml<br>Validating 21 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      21<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.1e2686ea7e | Completed 2026-10-15T14:36:40Z. No issues found<br>813 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.1e2686ea7e | Completed 2026-10-15T14:36:43Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.1e2686ea7e | Completed 2026-10-15T14:37:37Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.1e2686ea7e | Completed 2026-10-15T14:37:45Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.1e2686ea7e | Completed 2026-10-15T14:38:11Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.1e2686ea7e | Completed 2026-10-15T14:39:21Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | habitatmech:GOLD.1e2686ea7e | Verified 2026-10-15T14:33:14Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38748091185 |

## Scientific And Domain Assessments

### Identity and hierarchy

identity: concern. Targets: habitatmech:GOLD.1e2686ea7e.

The exact human Fossilized remains path distinguishes this zero-tree-count Bone source from living-anatomy siblings. A fossil can host microbes, but the unreviewed BTO hard-connective-tissue genus needs a material-state assessment: fossilized material need not retain the organic tissue components in that definition. Fossilized remains may denote a material class, so its parent is not automatically rejected as a whole-body container. The narrow endpoint issue is independently confirmed.

### Frozen source units, ranks and parameters

quantity: supported. Targets: habitatmech:GOLD.1e2686ea7e.

Count/unit, first GOLD node, channel, score and displayed taxon ranks/labels reproduce exact source rows. Verification: [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Zero counts are omitted, never interpreted as absence. Side-table biosamples/studies and MIxS slots are not added to tree ORGANISM counts.

### Scientific support and source limits

evidence: supported. Targets: habitatmech:GOLD.1e2686ea7e.

The exact human Fossilized remains path distinguishes this zero-tree-count Bone source from living-anatomy siblings. A fossil can host microbes, but the unreviewed BTO hard-connective-tissue genus needs a material-state assessment: fossilized material need not retain the organic tissue components in that definition. Fossilized remains may denote a material class, so its parent is not automatically rejected as a whole-body container. The narrow endpoint issue is independently confirmed.

### Native status and optional assertions

completeness: supported. Targets: habitatmech:GOLD.1e2686ea7e.

Executed routes reproduce NARROW/SEEDED. No causal edge or is_characteristic=true assertion is made. Optional absent fields and SEEDED status alone are not scientific defects; this review does not promote native status.

### Deterministic native gates

schema: supported. Targets: habitatmech:GOLD.1e2686ea7e.

Schema, strict, history, provenance, 3,208-record reproduction, causal, term-request, configured-label and exact-baseline full QC checks passed; these prove fidelity, not biological truth.

## Findings

### F1: Narrow predicate uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: bone-mapping-endpoint-contract.

The executed gold_narrower_than_leaf_match route retains the source mint yet emits narrowMatch relative to an ontology parent, while SourceAttestation describes a source-to-record mapping. Reconcile producer, schema and consumers under #1398; do not relabel an anatomically valid broader parent as an exact source identity, and do not claim SKOS formally forbids self-links.

### F2: Fossil material scope needs a source-specific genus assessment

major / open / provisional; issue key: bone-fossil-material-genus.

Assess the exact fossil-bone source before endorsing BTO:0000140 hard connective tissue as universally broader. Fossil mineral/organic preservation varies; primary dinosaur evidence is not proof about the human or mammal GOLD specimens. Preserve the mint and source provenance, distinguish bone tissue from whole bone element and fossilized material, and do not assume every fossil lacks original organic matter or that the remains-material parent is invalid.

## Recommended Actions And Acceptance Checks

### ACT1

The executed gold_narrower_than_leaf_match route retains the source mint yet emits narrowMatch relative to an ontology parent, while SourceAttestation describes a source-to-record mapping. Reconcile producer, schema and consumers under #1398; do not relabel an anatomically valid broader parent as an exact source identity, and do not claim SKOS formally forbids self-links. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Assess the exact fossil-bone source before endorsing BTO:0000140 hard connective tissue as universally broader. Fossil mineral/organic preservation varies; primary dinosaur evidence is not proof about the human or mammal GOLD specimens. Preserve the mint and source provenance, distinguish bone tissue from whole bone element and fossilized material, and do not assume every fossil lacks original organic matter or that the remains-material parent is invalid. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bone.yaml; Entire target YAML | supports | Full target read, including every source attestation, taxon, parent, parameter and history entry. |
| ERULE | docs/CURATION.md; Strict ancestry and maintained-input ownership | supports | Parent means strictly broader, not containing organ, body or system. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation, EnvironmentalParameter, CharacteristicTaxon | supports | Source-to-record mapping contract; qualified parameters and observed associations are not universal conditions or characteristic presence. |
| ESEED | src/habitatmech/seed.py; Executed build_corpus and apply_decision routes | supports | Whole generated document equality verified; source-specific resolutions: [{"mint": "habitatmech:GOLD.1e2686ea7e", "automatic": {"identifier": "habitatmech:GOLD.1e2686ea7e", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["BTO:0000140"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.1e2686ea7e", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["BTO:0000140"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source projection | supports | PREGO projects counts, scores, channels and ranked taxa without original pair citations. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 2374 | supports | [{"row": 2374, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Remains &gt; Fossilized remains &gt; Bone", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_type": "Remains", "ecosystem_subtype": "Fossilized remains", "specific_ecosystem": "Bone", "leaf_label": "Bone", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:6676"}}] |
| ET6 | data/raw/isolation_source_groundings.tsv; Physical TSV rows 46 | supports | [{"row": 46, "data": {"subject_label": "Bone", "subject_label_normalized": "bone", "object_id": "UBERON:0001474", "object_label": "bone element", "object_source": "UBERON", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification": "semapv:LexicalMatching", "curator": "ols4_auto", "source_dataset": "bacdive", "verified_date": "2026-05-01"}}] |
| ET7 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 101 | supports | [{"row": 101, "data": {"subject": "BTO:0000140", "predicate": "rdfs:subClassOf", "object": "BTO:0000421"}}] |
| ET8 | data/raw/ontology_terms.tsv; Physical TSV rows 142 | supports | [{"row": 142, "data": {"term_id": "BTO:0000140", "ontology": "BTO", "label": "bone", "definition": "The hard form of connective tissue that constitutes the majority of the skeleton of most vertebrates; it consists of an organic component (the cells and matrix) and an inorganic, or mineral, component; the matrix contains a framework of collagenous fibers and is impregnated with the mineral component, chiefly calcium phosphate (85 per cent) and calcium carbonate (10 per cent), which imparts the quality of rigidity to bone.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| EP9 | data/habitats/host_associated/fossilized_remains__8b01c49f.yaml; Full parent, scope context only | supports | {"identifier": "habitatmech:GOLD.f1a2eca320", "label": "Fossilized remains", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "SEEDED", "parent_habitats": ["habitatmech:GOLD.817e799cd5"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6138", "source_label": "Fossilized remains", "source_path": "Host-associated &gt; Mammals: Human &gt; Remains &gt; Fossilized remains", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. [CLASS-level] Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate. (source concept habitatmech:GOLD.f1a2eca320)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140/graph; BTO_0000140-graph.json | context_only | Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000140", "target": "http://purl.obolibrary.org/obo/BTO_0000421", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000140", "target": "http://purl.obolibrary.org/obo/BTO_0001486", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140; BTO_0000140.json | context_only | Inspected current ID, label, active status and definition for scope; {"obo_id": "BTO:0000140", "label": "bone", "is_obsolete": false} |
| EX3 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6581507/fullTextXML; PMC6581507.xml | context_only | Primary research abstract, DOI:10.7554/eLife.46205, PMID:31210129: aseptically excavated Centrosaurus bone had microbial communities distinct from surrounding sediment; proposed original soft-tissue preservation was not supported in those samples. This demonstrates fossil habitat plausibility and material-state uncertainty, not the identity or composition of the exact human/mammal GOLD specimens. |
| ESEARCH | Local inputs and review archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.1e2686ea7e -e Bone -e bone -e habitatmech:GOLD.1e2686ea7e curation history research reports data/raw build reviews | context_only | Exact TSV parsing and ignored-inclusive target/mint/label/slug search establish the bounded row inventory. Structured archive traversal found no predecessor; not every broad textual lead was inspected. |

## Limits And Additional Notes

- Every historical specimen and original source pair has not been independently reidentified. Source counts are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 no-adapter pairs and taxon labels; independent current NCBI lookup is recorded for displayed taxa.
- Full QC evidence is a verified remote run at the exact captured baseline, not a newly executed local QC. New review outputs require subsequent publication checks.
- iModulonDB is not applicable: no gene, regulator or expression-module assertion is made. No paid research was used.
- Captured hashes were rechecked against both working bytes and the exact Git base; no scientific inputs were silently refreshed.
- Ignored-inclusive searches and parsed structured archive found no prior structured observation of this exact target. Legacy Markdown is a lead, not structured lineage.
- This immutable observation precedes separately authorized curation and does not claim repairs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T145136Z-bone-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Bone (habitatmech:GOLD.1e2686ea7e)'
started_at: '2026-10-15T14:33:37Z'
finished_at: '2026-10-15T14:51:36Z'
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
summary: 'The exact human Fossilized remains path distinguishes this zero-tree-count
  Bone source from living-anatomy siblings. A fossil can host microbes, but the unreviewed
  BTO hard-connective-tissue genus needs a material-state assessment: fossilized material
  need not retain the organic tissue components in that definition. Fossilized remains
  may denote a material class, so its parent is not automatically rejected as a whole-body
  container. The narrow endpoint issue is independently confirmed.'
source:
  git_revision: b558fd561286d1fe3ba133784776f7be1f9f49fb
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
    sha256: 1e1c576daaee3c5055437ef42ba46363f5776210eef2e4182fe6fd3c87a7fe4d
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
  - path: data/habitats/host_associated/bone.yaml
    sha256: 973b7b5a298ca85413a552fc7769aa2b784640030ae3c1ad107fbdef6b238749
    role: target
  - path: data/habitats/host_associated/fossilized_remains__8b01c49f.yaml
    sha256: e6a4abcab64c4a8489b25f1106717859af8128269c9abdd50cd0b95b39ba35f6
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
  - path: reports/yaml_record_review/20260922T024852Z-bone.md
    sha256: 5c86490410f8af893143a3862a9305fa2371c8b6e6dbfb3a7b3953c8a4750178
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
- target_id: habitatmech:GOLD.1e2686ea7e
  path: data/habitats/host_associated/bone.yaml
  label: Bone
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
  description: Full scientific assessment of one exact target at b558fd561286d1fe3ba133784776f7be1f9f49fb.
  selection: One of the next 21 path-ordered unreviewed records, blood through bone
    marrow; this bundle assesses only this identifier.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.1e2686ea7e
  exclusions:
  - target: Other records and export products
    reason: Parent context is not additional coverage. SSSOM/KGX readiness is not
      certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bone.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  summary: "Completed 2026-10-15T14:35:14Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bone.yaml"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml
    data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml
    data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml
    data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml
    data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml
    data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml
    data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml
    data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml
    data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml
    data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml
    data/habitats/host_associated/bone_marrow__c1fc5dec.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  summary: "Completed 2026-10-15T14:36:08Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml\
    \ data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml\
    \ data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml\
    \ data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml\
    \ data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml\
    \ data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml\
    \ data/habitats/host_associated/bone__234001be.yaml data/habitats/host_associated/bone__71064238.yaml\
    \ data/habitats/host_associated/bone__8430e16e.yaml data/habitats/host_associated/bone__8d0df242.yaml\
    \ data/habitats/host_associated/bone__b47efce2.yaml data/habitats/host_associated/bone_element.yaml\
    \ data/habitats/host_associated/bone_marrow.yaml data/habitats/host_associated/bone_marrow__9387f1a6.yaml\
    \ data/habitats/host_associated/bone_marrow__c1fc5dec.yaml\nValidating 21 files\
    \ with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      21\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  summary: 'Completed 2026-10-15T14:36:40Z. No issues found

    813 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  summary: "Completed 2026-10-15T14:36:43Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  summary: "Completed 2026-10-15T14:37:37Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  summary: "Completed 2026-10-15T14:37:45Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  summary: "Completed 2026-10-15T14:38:11Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  summary: "Completed 2026-10-15T14:39:21Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual ordinary schema; strict for all 21 selected records; remaining
    gates full-corpus as documented.
- check_id: CCI
  name: Exact-baseline full QC
  status: passed
  required: true
  command: gh run view 38748091185 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  summary: Verified 2026-10-15T14:33:14Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38748091185
  scope_note: Exact unchanged scientific input baseline; these new review outputs
    require later checks.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bone.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T14:51:35Z'
  support: supports
  summary: Full target read, including every source attestation, taxon, parent, parameter
    and history entry.
  snapshot_sha256: 973b7b5a298ca85413a552fc7769aa2b784640030ae3c1ad107fbdef6b238749
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict ancestry and maintained-input ownership
  accessed_at: '2026-10-15T14:51:35Z'
  support: supports
  summary: Parent means strictly broader, not containing organ, body or system.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation, EnvironmentalParameter, CharacteristicTaxon
  accessed_at: '2026-10-15T14:51:35Z'
  support: supports
  summary: Source-to-record mapping contract; qualified parameters and observed associations
    are not universal conditions or characteristic presence.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed build_corpus and apply_decision routes
  accessed_at: '2026-10-15T14:51:35Z'
  support: supports
  summary: 'Whole generated document equality verified; source-specific resolutions:
    [{"mint": "habitatmech:GOLD.1e2686ea7e", "automatic": {"identifier": "habitatmech:GOLD.1e2686ea7e",
    "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding":
    true, "extra_parents": ["BTO:0000140"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match",
    "category": null, "reviewed": false, "decision": null}, "final": {"identifier":
    "habitatmech:GOLD.1e2686ea7e", "grounding_status": "NARROW", "mapping_predicate":
    "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["BTO:0000140"],
    "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null,
    "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source projection
  accessed_at: '2026-10-15T14:51:35Z'
  support: supports
  summary: PREGO projects counts, scores, channels and ranked taxa without original
    pair citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 2374
  accessed_at: '2026-10-15T14:51:35Z'
  support: supports
  summary: '[{"row": 2374, "data": {"canonical_path": "Host-associated > Mammals:
    Human > Remains > Fossilized remains > Bone", "ecosystem": "Host-associated",
    "ecosystem_category": "Mammals: Human", "ecosystem_type": "Remains", "ecosystem_subtype":
    "Fossilized remains", "specific_ecosystem": "Bone", "leaf_label": "Bone", "depth":
    "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count":
    "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:6676"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/isolation_source_groundings.tsv
  locator: Physical TSV rows 46
  accessed_at: '2026-10-15T14:51:35Z'
  support: supports
  summary: '[{"row": 46, "data": {"subject_label": "Bone", "subject_label_normalized":
    "bone", "object_id": "UBERON:0001474", "object_label": "bone element", "object_source":
    "UBERON", "predicate_id": "skos:closeMatch", "confidence": "medium", "mapping_justification":
    "semapv:LexicalMatching", "curator": "ols4_auto", "source_dataset": "bacdive",
    "verified_date": "2026-05-01"}}]'
  snapshot_sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 101
  accessed_at: '2026-10-15T14:51:35Z'
  support: supports
  summary: '[{"row": 101, "data": {"subject": "BTO:0000140", "predicate": "rdfs:subClassOf",
    "object": "BTO:0000421"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 142
  accessed_at: '2026-10-15T14:51:35Z'
  support: supports
  summary: '[{"row": 142, "data": {"term_id": "BTO:0000140", "ontology": "BTO", "label":
    "bone", "definition": "The hard form of connective tissue that constitutes the
    majority of the skeleton of most vertebrates; it consists of an organic component
    (the cells and matrix) and an inorganic, or mineral, component; the matrix contains
    a framework of collagenous fibers and is impregnated with the mineral component,
    chiefly calcium phosphate (85 per cent) and calcium carbonate (10 per cent), which
    imparts the quality of rigidity to bone.", "synonyms": "", "deprecated": "", "directly_referenced":
    "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/fossilized_remains__8b01c49f.yaml
  locator: Full parent, scope context only
  accessed_at: '2026-10-15T14:51:35Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.f1a2eca320", "label": "Fossilized remains",
    "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status":
    "SEEDED", "parent_habitats": ["habitatmech:GOLD.817e799cd5"], "source_attestations":
    [{"source": "GOLD", "source_id": "gold.ecosystem:6138", "source_label": "Fossilized
    remains", "source_path": "Host-associated > Mammals: Human > Remains > Fossilized
    remains", "notes": "2 GOLD ecosystem node ids share this path; first shown. See
    data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z",
    "curator": "claude-opus-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed
    UNGROUNDED: no ontology term fits this concept. [CLASS-level] Class-level sweep
    (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate. (source concept habitatmech:GOLD.f1a2eca320)"},
    {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: UNGROUNDED."}]}'
  snapshot_sha256: e6a4abcab64c4a8489b25f1106717859af8128269c9abdd50cd0b95b39ba35f6
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140/graph
  locator: BTO_0000140-graph.json
  accessed_at: '2026-10-15T14:36:17Z'
  support: context_only
  summary: 'Typed outgoing relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000140",
    "target": "http://purl.obolibrary.org/obo/BTO_0000421", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/BTO_0000140",
    "target": "http://purl.obolibrary.org/obo/BTO_0001486", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 14ec2b72ca358eed8ca91634929743f2dfff7491c094c0eeab5491e982c7ca35
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000140
  locator: BTO_0000140.json
  accessed_at: '2026-10-15T14:36:16Z'
  support: context_only
  summary: 'Inspected current ID, label, active status and definition for scope; {"obo_id":
    "BTO:0000140", "label": "bone", "is_obsolete": false}'
  snapshot_sha256: 75f23eb9636f74b74c10224f169aab677ce7cdba087ca4d5e51fba9a875cff6f
- evidence_id: EX3
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6581507/fullTextXML
  locator: PMC6581507.xml
  accessed_at: '2026-10-15T14:47:04Z'
  support: context_only
  summary: 'Primary research abstract, DOI:10.7554/eLife.46205, PMID:31210129: aseptically
    excavated Centrosaurus bone had microbial communities distinct from surrounding
    sediment; proposed original soft-tissue preservation was not supported in those
    samples. This demonstrates fossil habitat plausibility and material-state uncertainty,
    not the identity or composition of the exact human/mammal GOLD specimens.'
  snapshot_sha256: 86f96a4c0b6666aed012ca90d4959af65938cd0cba0ef7d34dea196d8a2edeb2
- evidence_id: ESEARCH
  kind: search
  reference: Local inputs and review archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.1e2686ea7e -e Bone -e
    bone -e habitatmech:GOLD.1e2686ea7e curation history research reports data/raw
    build reviews
  accessed_at: '2026-10-15T14:33:45Z'
  support: context_only
  summary: Exact TSV parsing and ignored-inclusive target/mint/label/slug search establish
    the bounded row inventory. Structured archive traversal found no predecessor;
    not every broad textual lead was inspected.
  search_scope: curation, history, research, reports, data/raw, build, reviews including
    ignored/hidden files; all structured review.yaml files parsed.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity and hierarchy
  outcome: concern
  summary: 'The exact human Fossilized remains path distinguishes this zero-tree-count
    Bone source from living-anatomy siblings. A fossil can host microbes, but the
    unreviewed BTO hard-connective-tissue genus needs a material-state assessment:
    fossilized material need not retain the organic tissue components in that definition.
    Fossilized remains may denote a material class, so its parent is not automatically
    rejected as a whole-body container. The narrow endpoint issue is independently
    confirmed.'
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EX1
  - EX2
  - EX3
- assessment_id: A2
  area: quantity
  topic: Frozen source units, ranks and parameters
  outcome: supported
  summary: 'Count/unit, first GOLD node, channel, score and displayed taxon ranks/labels
    reproduce exact source rows. Verification: [{"source": "GOLD", "count": 0, "unit":
    "ORGANISM"}]. Zero counts are omitted, never interpreted as absence. Side-table
    biosamples/studies and MIxS slots are not added to tree ORGANISM counts.'
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - EX1
  - EX2
  - EX3
- assessment_id: A3
  area: evidence
  topic: Scientific support and source limits
  outcome: supported
  summary: 'The exact human Fossilized remains path distinguishes this zero-tree-count
    Bone source from living-anatomy siblings. A fossil can host microbes, but the
    unreviewed BTO hard-connective-tissue genus needs a material-state assessment:
    fossilized material need not retain the organic tissue components in that definition.
    Fossilized remains may denote a material class, so its parent is not automatically
    rejected as a whole-body container. The narrow endpoint issue is independently
    confirmed.'
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EX1
  - EX2
  - EX3
- assessment_id: A4
  area: completeness
  topic: Native status and optional assertions
  outcome: supported
  summary: Executed routes reproduce NARROW/SEEDED. No causal edge or is_characteristic=true
    assertion is made. Optional absent fields and SEEDED status alone are not scientific
    defects; this review does not promote native status.
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  evidence_ids:
  - E1
  - ERULE
  - ESEED
- assessment_id: A5
  area: schema
  topic: Deterministic native gates
  outcome: supported
  summary: Schema, strict, history, provenance, 3,208-record reproduction, causal,
    term-request, configured-label and exact-baseline full QC checks passed; these
    prove fidelity, not biological truth.
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: bone-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow predicate uses an undeclared ontology-parent endpoint
  description: 'The executed gold_narrower_than_leaf_match route retains the source
    mint yet emits narrowMatch relative to an ontology parent, while SourceAttestation
    describes a source-to-record mapping. Reconcile producer, schema and consumers
    under #1398; do not relabel an anatomically valid broader parent as an exact source
    identity, and do not claim SKOS formally forbids self-links.'
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EX1
  - EX2
  - EX3
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
- finding_id: F2
  issue_key: bone-fossil-material-genus
  category: grounding
  severity: major
  status: open
  certainty: provisional
  title: Fossil material scope needs a source-specific genus assessment
  description: Assess the exact fossil-bone source before endorsing BTO:0000140 hard
    connective tissue as universally broader. Fossil mineral/organic preservation
    varies; primary dinosaur evidence is not proof about the human or mammal GOLD
    specimens. Preserve the mint and source provenance, distinguish bone tissue from
    whole bone element and fossilized material, and do not assume every fossil lacks
    original organic matter or that the remains-material parent is invalid.
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  field_paths:
  - parent_habitats
  - grounding_status
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EX1
  - EX2
  - EX3
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
  - habitatmech:GOLD.1e2686ea7e
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'The executed gold_narrower_than_leaf_match route retains the source
    mint yet emits narrowMatch relative to an ontology parent, while SourceAttestation
    describes a source-to-record mapping. Reconcile producer, schema and consumers
    under #1398; do not relabel an anatomically valid broader parent as an exact source
    identity, and do not claim SKOS formally forbids self-links. No repair is performed
    by this review.'
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history. Do not change
    source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.1e2686ea7e
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Assess the exact fossil-bone source before endorsing BTO:0000140 hard
    connective tissue as universally broader. Fossil mineral/organic preservation
    varies; primary dinosaur evidence is not proof about the human or mammal GOLD
    specimens. Preserve the mint and source provenance, distinguish bone tissue from
    whole bone element and fossilized material, and do not assume every fossil lacks
    original organic matter or that the remains-material parent is invalid. No repair
    is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independently valid identifiers,
    source counts/units, raw provenance, native status and history. Do not change
    source totals by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Every historical specimen and original source pair has not been independently reidentified.
  Source counts are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 no-adapter pairs and taxon labels; independent
  current NCBI lookup is recorded for displayed taxa.
- Full QC evidence is a verified remote run at the exact captured baseline, not a
  newly executed local QC. New review outputs require subsequent publication checks.
- 'iModulonDB is not applicable: no gene, regulator or expression-module assertion
  is made. No paid research was used.'
notes:
- Captured hashes were rechecked against both working bytes and the exact Git base;
  no scientific inputs were silently refreshed.
- Ignored-inclusive searches and parsed structured archive found no prior structured
  observation of this exact target. Legacy Markdown is a lead, not structured lineage.
- This immutable observation precedes separately authorized curation and does not
  claim repairs.
tags:
- individual-scientific-review
- host-associated
```
