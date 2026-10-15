# Record review: autopod pad (UBERON:0012348)

- Review: 20261015T093736Z-autopod_pad-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T09:23:13Z
- Finished UTC: 2026-10-15T09:37:36Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The source paw-pad site and autopod-skin superclass are supported. CLOSE is reproduced from the reviewed synonym route. The separate UBERON paw pad alias is typed related in the official OWL but emitted exact; the GOLD alias already correctly remains related.

## Scope And Provenance

Scientific review of one exact target at bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.

Selection: Next twenty unreviewed records in corpus path order; this bundle assesses exactly one of their resolved identifiers.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0012348 | data/habitats/host_associated/autopod_pad.yaml | generated | autopod pad |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | UBERON:0012348 | Completed 2026-10-15T09:23:42Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/autopod_pad.yaml |
| validate-strict | passed | True | UBERON:0012348 | Completed 2026-10-15T09:25:01Z. uv run python scripts/validate_strict.py data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | UBERON:0012348 | Completed 2026-10-15T09:25:13Z. No issues found<br>777 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | UBERON:0012348 | Completed 2026-10-15T09:25:14Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | UBERON:0012348 | Completed 2026-10-15T09:25:35Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | UBERON:0012348 | Completed 2026-10-15T09:25:40Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | UBERON:0012348 | Completed 2026-10-15T09:26:00Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | UBERON:0012348 | Completed 2026-10-15T09:26:58Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-revision baseline full QC | passed | True | UBERON:0012348 | Required full native QC and structured-review contract succeeded at the exact captured revision; status checked 2026-10-15T09:25:51Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38709434919 |

## Scientific And Domain Assessments

### Native validators and reproduction

schema: supported. Targets: UBERON:0012348.

Individual schema, twenty-target strict validation, 777 history records, 14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110 term requests passed. This establishes deterministic fidelity, not scientific validity.

### Identity, definition, hierarchy and synonym scope

identity: concern. Targets: UBERON:0012348.

The source paw-pad site and autopod-skin superclass are supported. CLOSE is reproduced from the reviewed synonym route. The separate UBERON paw pad alias is typed related in the official OWL but emitted exact; the GOLD alias already correctly remains related.

### Counts, units and ranking provenance

quantity: supported. Targets: UBERON:0012348.

Exact source rows reproduce [{"source": "GOLD", "count": 2, "unit": "ORGANISM"}]. Every displayed taxon ID/name resolves in NCBI; ranks and pools reproduce the exact habitat-keyed rows. Tied PREGO score/direct flags are ordered by taxon ID, not abundance. Zero tree counts do not imply microbial absence or erase different bulk counts.

### Source status and optional claims

completeness: supported. Targets: UBERON:0012348.

Full routes reproduce CLOSE/REVIEWED. Optional parameter, mechanism and characteristic-presence claims are not asserted and are not required quotas. Source parent counts, triad annotations and adjacent records are not inherited observations.

## Findings

### F1: Related ontology aliases are emitted as exact

major / open / confirmed; issue key: autopod-pad-ontology-synonym-scope.

Use guarded record_annotation_corrections.tsv rows to change only the UBERON paw pad annotations from EXACT_SYNONYM to RELATED_SYNONYM. Preserve independent exact aliases, canonical identity and source labels. The shared extractor/seeder scope loss remains #1249; a bounded correction does not repair every ontology synonym.

## Recommended Actions And Acceptance Checks

### ACT1

Use guarded record_annotation_corrections.tsv rows to change only the UBERON paw pad annotations from EXACT_SYNONYM to RELATED_SYNONYM. Preserve independent exact aliases, canonical identity and source labels. The shared extractor/seeder scope loss remains #1249; a bounded correction does not repair every ontology synonym. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/autopod_pad.yaml; Entire YAML | supports | Read the complete target including source path, fields, taxonomy and generated history. |
| ERULE | docs/CURATION.md; Host identity, broader parents and maintained ownership | supports | Whole organisms cannot identify associated environments; parent_habitats requires strictly broader habitat meaning. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon | supports | Source-to-record mapping endpoints, broader habitat relations and observed versus characteristic presence are distinct. |
| ESEED | src/habitatmech/seed.py; Native executed resolution route | supports | Executed native route and final decision: [{"source": "GOLD", "mint": "habitatmech:GOLD.48acde6f2d", "automatic": {"identifier": "UBERON:0012348", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_synonym", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0012348", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_gold_leaf_synonym", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.48acde6f2d", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "CLOSE-grounding review (#12): read against the full source path and the term's own definition. The grounding is right and CLOSE is the honest status \u2014 the term is the concept with a difference of framing or specificity that EXACT would overstate.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; extract_prego | supports | Projection deduplicates pairs, preserves best score/channel, uses score/directness/taxon-ID order and retains a full distinct-taxon pool. Original pair citations are not emitted into this committed projection. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; TSV physical rows 848 | supports | [{"row": 848, "data": {"canonical_path": "Host-associated &gt; Mammals &gt; Integumentary system &gt; Skin &gt; Paw pad", "ecosystem": "Host-associated", "ecosystem_category": "Mammals", "ecosystem_type": "Integumentary system", "ecosystem_subtype": "Skin", "specific_ecosystem": "Paw pad", "leaf_label": "Paw pad", "depth": "5", "gold_node_count": "1", "organism_count": "2", "study_count": "0", "biosample_count": "0", "total_assertions": "2", "gold_node_ids": "gold.ecosystem:6394"}}] |
| ET6 | data/raw/gold_path_biosamples.tsv; TSV physical rows 633 | supports | [{"row": 633, "data": {"canonical_path": "Host-associated &gt; Mammals &gt; Integumentary system &gt; Skin &gt; Paw pad", "ecosystem_path_id": "6394", "biosample_count": "10"}}] |
| ET7 | data/raw/gold_studies.tsv; TSV physical rows 1101 | supports | Exact membership in 1 study path lists. These are not additive with tree-organism or bulk-biosample counts. |
| ET8 | data/raw/ontology_subclass_edges.tsv; TSV physical rows 11752,11794 | supports | [{"row": 11752, "data": {"subject": "UBERON:0012348", "predicate": "rdfs:subClassOf", "object": "UBERON:0015790"}}, {"row": 11794, "data": {"subject": "UBERON:0015790", "predicate": "rdfs:subClassOf", "object": "UBERON:0001419"}}] |
| ET9 | data/raw/ontology_terms.tsv; TSV physical rows 13442,13476 | supports | [{"row": 13442, "data": {"term_id": "UBERON:0012348", "ontology": "UBERON", "label": "autopod pad", "definition": "Pigmented, keratinised, hairless epidermis covering subcutaneous, collagenous, and adipose tissue.", "synonyms": "paw pad", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row": 13476, "data": {"term_id": "UBERON:0015790", "ontology": "UBERON", "label": "autopod skin", "definition": "A zone of skin that is part of a autopod region.", "synonyms": "paw skin", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| ET10 | curation/decisions.tsv; TSV physical rows 1761 | supports | [{"row": 1761, "data": {"identifier": "habitatmech:GOLD.48acde6f2d", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "CLOSE-grounding review (#12): read against the full source path and the term's own definition. The grounding is right and CLOSE is the honest status \u2014 the term is the concept with a difference of framing or specificity that EXACT would overstate.", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP11 | data/habitats/host_associated/skin__120842b3.yaml; Direct parent scope, not an additional target review | supports | {"identifier": "habitatmech:GOLD.c896f9520f", "label": "Skin", "grounding_status": "NARROW", "parent_habitats": ["BTO:0001253", "habitatmech:GOLD.56e0776270"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6383", "source_label": "Skin", "source_path": "Host-associated &gt; Mammals &gt; Integumentary system &gt; Skin", "mapping_predicate": "skos:narrowMatch", "assertion_count": 121, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001253/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0001253", "target": "http://purl.obolibrary.org/obo/BTO_0000634", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001253; Canonical term identity, definition and explicit relation types | supports | BTO:0001253 skin; inspected definition and typed scope. ["The integument of an animal (as a fur-bearing mammal or a bird) separated from the body usually with its hair or feathers."] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0012348/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0012348", "target": "http://purl.obolibrary.org/obo/UBERON_0015790", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0012348", "target": "http://purl.obolibrary.org/obo/UBERON_0001003", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0012348", "target": "http://purl.obolibrary.org/obo/UBERON_0002470", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0012348; Canonical term identity, definition and explicit relation types | supports | UBERON:0012348 autopod pad; inspected definition and typed scope. ["Pigmented, keratinised, hairless epidermis covering subcutaneous, collagenous, and adipose tissue."] |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0015790/graph; Canonical term identity, definition and explicit relation types | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0015790", "target": "http://purl.obolibrary.org/obo/UBERON_0001419", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0015790", "target": "http://purl.obolibrary.org/obo/UBERON_0002470", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0015790; Canonical term identity, definition and explicit relation types | supports | UBERON:0015790 autopod skin; inspected definition and typed scope. ["A zone of skin that is part of a autopod region."] |
| EX7 | https://purl.obolibrary.org/obo/uberon/uberon-base.owl; Direct OWL class annotations for UBERON:0012348 | supports | Official OWL explicitly hasRelatedSynonym paw pad for UBERON:0012348; lack of a scoped OLS synonym entry is not evidence of exactness. |
| ESEARCH | Local records and maintained inputs; rg --no-ignore --hidden -l -F -e UBERON:0012348 -e 'autopod pad' -e autopod_pad -e habitatmech:GOLD.48acde6f2d curation history research reports data/raw build reviews | context_only | Identifier, label, slug and minted-source search includes hidden and ignored files; parsed structured archive traversal found no target predecessor. Broad text hits are not treated as exact source associations. |
| ELEGACY | reports/yaml_record_review/20261004T090653Z-autopod_pad.md; Historical target review, especially findings and evidence leads | supports | Historical assessment was consulted for source and issue leads; current findings are independently reassessed against the captured inputs and stated authorities. It is not structured predecessor lineage. |

## Limits And Additional Notes

- Source counts, PREGO scores and rank are not prevalence, viability, mechanism or characteristic presence. Every historical specimen has not been independently reidentified.
- Configured label correspondence skipped 2,061 pairs without adapters; it is not full identifier or semantic certification.
- Baseline full QC is exact-revision CI evidence, not a new local full-QC execution. The post-save archive gate is subsequent and is not claimed passed inside this observation.
- Only stated source passages were assessed. Historical reports provide leads, not independent approval; optional empty fields do not create automatic deficiencies.
- iModulonDB is not applicable because the target asserts no gene, regulator or expression module. No paid research, curation, native-status promotion or GitHub mutation was performed.
- No positive nonmammalian witness was established for this exact ontology class; generic anatomical naming alone was not used to declare the mammal Skin edge false. This does not certify every possible taxonomic application of autopod pad.
- Fresh captures were made at current main after the previous publication; earlier scratch captures were not refreshed or reused as provenance.
- All captured bytes match both current files and the exact Git revision. The extractor has a separate native supplemental capture.
- Ignored-inclusive traversal found no structured predecessor targeting this identifier. Legacy Markdown observations are contextual; no earlier structured finding is silently closed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T093736Z-autopod_pad-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: autopod pad (UBERON:0012348)'
started_at: '2026-10-15T09:23:13Z'
finished_at: '2026-10-15T09:37:36Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent performed evidence inspection; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The source paw-pad site and autopod-skin superclass are supported. CLOSE
  is reproduced from the reviewed synonym route. The separate UBERON paw pad alias
  is typed related in the official OWL but emitted exact; the GOLD alias already correctly
  remains related.
source:
  git_revision: bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d
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
    sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: ee710783b625e34dcfa822afab0008e4bfe6b2daf3224b5f804fe569dccb26fb
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 5a794902f1338c3206cb43900e310ef7d573fcbff61da4a01d77bb43b6677c48
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 6af1d1e372e4400f3caf58808eeb508d3436c2ee1ae7a897c4a23e434093d455
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 70656ba3c46b4d72fd44cb0ef83322c2c4591edbc3501a9fb7d1497aaeab67a6
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
  - path: data/habitats/host_associated/autopod_pad.yaml
    sha256: acd5cd99c7e6e49557aad77a4a45d71398aff07ed8f3437b153736c093957005
    role: target
  - path: data/habitats/host_associated/skin__120842b3.yaml
    sha256: d289ced090fe833fd08c77a79df5c013044dfada3603d6eb839c8da7cb9216ff
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
  - path: reports/yaml_record_review/20261004T090653Z-autopod_pad.md
    sha256: 885f068c878ead31f2716d8eccf09d5e79fdc8ff9390c1d471e17710dd2211fd
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
- target_id: UBERON:0012348
  path: data/habitats/host_associated/autopod_pad.yaml
  label: autopod pad
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
  description: Scientific review of one exact target at bcf6c369a27a5bf1dd9a0156f12f0a61352ff78d.
  selection: Next twenty unreviewed records in corpus path order; this bundle assesses
    exactly one of their resolved identifiers.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0012348
  exclusions:
  - target: Other records, exports and parent-record reviews
    reason: Parent context informs this review but is not counted as additional reviewed
      coverage; SSSOM/KGX readiness is not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/autopod_pad.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0012348
  summary: "Completed 2026-10-15T09:23:42Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/autopod_pad.yaml"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml
    data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml
    data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml
    data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml
    data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml
    data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml
    data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml
    data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml
    data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml
    data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0012348
  summary: "Completed 2026-10-15T09:25:01Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/attached_keratinized_gingiva.yaml data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml\
    \ data/habitats/host_associated/auditory_hearing_system.yaml data/habitats/host_associated/auditory_hearing_system__8fefc879.yaml\
    \ data/habitats/host_associated/aural.yaml data/habitats/host_associated/autopod_pad.yaml\
    \ data/habitats/host_associated/autotrophic_anf.yaml data/habitats/host_associated/axilla.yaml\
    \ data/habitats/host_associated/b_lymphocyte.yaml data/habitats/host_associated/b_lymphocyte_cell_line.yaml\
    \ data/habitats/host_associated/bacteria.yaml data/habitats/host_associated/bacteria__7bc807fd.yaml\
    \ data/habitats/host_associated/bacteroid.yaml data/habitats/host_associated/bark.yaml\
    \ data/habitats/host_associated/bark__5b1d3b9d.yaml data/habitats/host_associated/bartholin_abscess.yaml\
    \ data/habitats/host_associated/basal_cell_carcinoma.yaml data/habitats/host_associated/bcp_1_cell.yaml\
    \ data/habitats/host_associated/beaker_s_popliteal_cyst.yaml data/habitats/host_associated/benign_tumor.yaml\n\
    Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0012348
  summary: 'Completed 2026-10-15T09:25:13Z. No issues found

    777 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0012348
  summary: "Completed 2026-10-15T09:25:14Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0012348
  summary: "Completed 2026-10-15T09:25:35Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0012348
  summary: "Completed 2026-10-15T09:25:40Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0012348
  summary: "Completed 2026-10-15T09:26:00Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0012348
  summary: "Completed 2026-10-15T09:26:58Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict validation names all twenty targets; other
    native gates have documented full-corpus scope.
- check_id: CCI
  name: Exact-revision baseline full QC
  status: passed
  required: true
  command: gh run view 38709434919 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - UBERON:0012348
  summary: Required full native QC and structured-review contract succeeded at the
    exact captured revision; status checked 2026-10-15T09:25:51Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38709434919
  scope_note: Remote baseline execution; newly saved review outputs require their
    own archive check.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/autopod_pad.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: Read the complete target including source path, fields, taxonomy and generated
    history.
  snapshot_sha256: acd5cd99c7e6e49557aad77a4a45d71398aff07ed8f3437b153736c093957005
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, broader parents and maintained ownership
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: Whole organisms cannot identify associated environments; parent_habitats
    requires strictly broader habitat meaning.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: Source-to-record mapping endpoints, broader habitat relations and observed
    versus characteristic presence are distinct.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Native executed resolution route
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: 'Executed native route and final decision: [{"source": "GOLD", "mint":
    "habitatmech:GOLD.48acde6f2d", "automatic": {"identifier": "UBERON:0012348", "grounding_status":
    "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true,
    "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_synonym", "category":
    null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0012348",
    "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_gold_leaf_synonym",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.48acde6f2d",
    "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "CLOSE-grounding
    review (#12): read against the full source path and the term''s own definition.
    The grounding is right and CLOSE is the honest status \u2014 the term is the concept
    with a difference of framing or specificity that EXACT would overstate.", "review_depth":
    "ITEM", "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: Projection deduplicates pairs, preserves best score/channel, uses score/directness/taxon-ID
    order and retains a full distinct-taxon pool. Original pair citations are not
    emitted into this committed projection.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV physical rows 848
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: '[{"row": 848, "data": {"canonical_path": "Host-associated > Mammals >
    Integumentary system > Skin > Paw pad", "ecosystem": "Host-associated", "ecosystem_category":
    "Mammals", "ecosystem_type": "Integumentary system", "ecosystem_subtype": "Skin",
    "specific_ecosystem": "Paw pad", "leaf_label": "Paw pad", "depth": "5", "gold_node_count":
    "1", "organism_count": "2", "study_count": "0", "biosample_count": "0", "total_assertions":
    "2", "gold_node_ids": "gold.ecosystem:6394"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/gold_path_biosamples.tsv
  locator: TSV physical rows 633
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: '[{"row": 633, "data": {"canonical_path": "Host-associated > Mammals >
    Integumentary system > Skin > Paw pad", "ecosystem_path_id": "6394", "biosample_count":
    "10"}}]'
  snapshot_sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
- evidence_id: ET7
  kind: database
  reference: data/raw/gold_studies.tsv
  locator: TSV physical rows 1101
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: Exact membership in 1 study path lists. These are not additive with tree-organism
    or bulk-biosample counts.
  snapshot_sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
- evidence_id: ET8
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV physical rows 11752,11794
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: '[{"row": 11752, "data": {"subject": "UBERON:0012348", "predicate": "rdfs:subClassOf",
    "object": "UBERON:0015790"}}, {"row": 11794, "data": {"subject": "UBERON:0015790",
    "predicate": "rdfs:subClassOf", "object": "UBERON:0001419"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET9
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV physical rows 13442,13476
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: '[{"row": 13442, "data": {"term_id": "UBERON:0012348", "ontology": "UBERON",
    "label": "autopod pad", "definition": "Pigmented, keratinised, hairless epidermis
    covering subcutaneous, collagenous, and adipose tissue.", "synonyms": "paw pad",
    "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row":
    13476, "data": {"term_id": "UBERON:0015790", "ontology": "UBERON", "label": "autopod
    skin", "definition": "A zone of skin that is part of a autopod region.", "synonyms":
    "paw skin", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET10
  kind: database
  reference: curation/decisions.tsv
  locator: TSV physical rows 1761
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: '[{"row": 1761, "data": {"identifier": "habitatmech:GOLD.48acde6f2d", "decision":
    "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator":
    "claude-opus-5", "date": "2026-08-16", "notes": "CLOSE-grounding review (#12):
    read against the full source path and the term''s own definition. The grounding
    is right and CLOSE is the honest status \u2014 the term is the concept with a
    difference of framing or specificity that EXACT would overstate.", "review_depth":
    "ITEM", "category": "", "relation": ""}}]'
  snapshot_sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
- evidence_id: EP11
  kind: record_content
  reference: data/habitats/host_associated/skin__120842b3.yaml
  locator: Direct parent scope, not an additional target review
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.c896f9520f", "label": "Skin", "grounding_status":
    "NARROW", "parent_habitats": ["BTO:0001253", "habitatmech:GOLD.56e0776270"], "source_attestations":
    [{"source": "GOLD", "source_id": "gold.ecosystem:6383", "source_label": "Skin",
    "source_path": "Host-associated > Mammals > Integumentary system > Skin", "mapping_predicate":
    "skos:narrowMatch", "assertion_count": 121, "assertion_unit": "ORGANISM", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]}'
  snapshot_sha256: d289ced090fe833fd08c77a79df5c013044dfada3603d6eb839c8da7cb9216ff
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001253/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:26Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0001253",
    "target": "http://purl.obolibrary.org/obo/BTO_0000634", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: e21351e06776a6d6529b169ab35fcbe1459c546169c5c7f44d68388a102a9204
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001253
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:26Z'
  support: supports
  summary: BTO:0001253 skin; inspected definition and typed scope. ["The integument
    of an animal (as a fur-bearing mammal or a bird) separated from the body usually
    with its hair or feathers."]
  snapshot_sha256: 4cc1bdfc54665947a911db22bbcc8fe146c3f1d7d939f2239f978be28ba13886
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0012348/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:56Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0012348",
    "target": "http://purl.obolibrary.org/obo/UBERON_0015790", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0012348",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001003", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0012348",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002470", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 3050a6da4f63a06a0350cc5d204be2599d071aa714f98ee5b848c67c7b7e30f5
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0012348
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:56Z'
  support: supports
  summary: UBERON:0012348 autopod pad; inspected definition and typed scope. ["Pigmented,
    keratinised, hairless epidermis covering subcutaneous, collagenous, and adipose
    tissue."]
  snapshot_sha256: 61fe60b6d8b824fccab009ed52a37fcb60acaff25babd18f04ad531d13cc11f5
- evidence_id: EX5
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0015790/graph
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:58Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0015790",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001419", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0015790",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002470", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 23f7f90647c226cd3bd42b047fb6ab194bcc485a11e93ffa043dee6e16358e36
- evidence_id: EX6
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0015790
  locator: Canonical term identity, definition and explicit relation types
  accessed_at: '2026-10-15T09:25:57Z'
  support: supports
  summary: UBERON:0015790 autopod skin; inspected definition and typed scope. ["A
    zone of skin that is part of a autopod region."]
  snapshot_sha256: 2202a29fe9157ea5680f03aa495db11398f6bff3a515bcbda9256b185a02d29d
- evidence_id: EX7
  kind: authority
  reference: https://purl.obolibrary.org/obo/uberon/uberon-base.owl
  locator: Direct OWL class annotations for UBERON:0012348
  accessed_at: '2026-10-15T09:28:35Z'
  support: supports
  summary: Official OWL explicitly hasRelatedSynonym paw pad for UBERON:0012348; lack
    of a scoped OLS synonym entry is not evidence of exactness.
  snapshot_sha256: e69b77112e073da633d60b20aeec48dfc70eca98d7500707bbb3b43bcef2971c
- evidence_id: ESEARCH
  kind: search
  reference: Local records and maintained inputs
  locator: rg --no-ignore --hidden -l -F -e UBERON:0012348 -e 'autopod pad' -e autopod_pad
    -e habitatmech:GOLD.48acde6f2d curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-15T09:24:07Z'
  support: context_only
  summary: Identifier, label, slug and minted-source search includes hidden and ignored
    files; parsed structured archive traversal found no target predecessor. Broad
    text hits are not treated as exact source associations.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    filesystem traversal of every structured review.yaml independent of gitignore.
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20261004T090653Z-autopod_pad.md
  locator: Historical target review, especially findings and evidence leads
  accessed_at: '2026-10-15T09:37:36Z'
  support: supports
  summary: Historical assessment was consulted for source and issue leads; current
    findings are independently reassessed against the captured inputs and stated authorities.
    It is not structured predecessor lineage.
  snapshot_sha256: 885f068c878ead31f2716d8eccf09d5e79fdc8ff9390c1d471e17710dd2211fd
assessments:
- assessment_id: A1
  area: schema
  topic: Native validators and reproduction
  outcome: supported
  summary: Individual schema, twenty-target strict validation, 777 history records,
    14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110
    term requests passed. This establishes deterministic fidelity, not scientific
    validity.
  target_ids:
  - UBERON:0012348
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, definition, hierarchy and synonym scope
  outcome: concern
  summary: The source paw-pad site and autopod-skin superclass are supported. CLOSE
    is reproduced from the reviewed synonym route. The separate UBERON paw pad alias
    is typed related in the official OWL but emitted exact; the GOLD alias already
    correctly remains related.
  target_ids:
  - UBERON:0012348
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
- assessment_id: A3
  area: quantity
  topic: Counts, units and ranking provenance
  outcome: supported
  summary: 'Exact source rows reproduce [{"source": "GOLD", "count": 2, "unit": "ORGANISM"}].
    Every displayed taxon ID/name resolves in NCBI; ranks and pools reproduce the
    exact habitat-keyed rows. Tied PREGO score/direct flags are ordered by taxon ID,
    not abundance. Zero tree counts do not imply microbial absence or erase different
    bulk counts.'
  target_ids:
  - UBERON:0012348
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
- assessment_id: A4
  area: completeness
  topic: Source status and optional claims
  outcome: supported
  summary: Full routes reproduce CLOSE/REVIEWED. Optional parameter, mechanism and
    characteristic-presence claims are not asserted and are not required quotas. Source
    parent counts, triad annotations and adjacent records are not inherited observations.
  target_ids:
  - UBERON:0012348
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: autopod-pad-ontology-synonym-scope
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: Related ontology aliases are emitted as exact
  description: 'Use guarded record_annotation_corrections.tsv rows to change only
    the UBERON paw pad annotations from EXACT_SYNONYM to RELATED_SYNONYM. Preserve
    independent exact aliases, canonical identity and source labels. The shared extractor/seeder
    scope loss remains #1249; a bounded correction does not repair every ontology
    synonym.'
  target_ids:
  - UBERON:0012348
  field_paths:
  - synonyms
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1249
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - UBERON:0012348
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Use guarded record_annotation_corrections.tsv rows to change only
    the UBERON paw pad annotations from EXACT_SYNONYM to RELATED_SYNONYM. Preserve
    independent exact aliases, canonical identity and source labels. The shared extractor/seeder
    scope loss remains #1249; a bounded correction does not repair every ontology
    synonym. No repair is performed by this review.'
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
- Source counts, PREGO scores and rank are not prevalence, viability, mechanism or
  characteristic presence. Every historical specimen has not been independently reidentified.
- Configured label correspondence skipped 2,061 pairs without adapters; it is not
  full identifier or semantic certification.
- Baseline full QC is exact-revision CI evidence, not a new local full-QC execution.
  The post-save archive gate is subsequent and is not claimed passed inside this observation.
- Only stated source passages were assessed. Historical reports provide leads, not
  independent approval; optional empty fields do not create automatic deficiencies.
- iModulonDB is not applicable because the target asserts no gene, regulator or expression
  module. No paid research, curation, native-status promotion or GitHub mutation was
  performed.
- No positive nonmammalian witness was established for this exact ontology class;
  generic anatomical naming alone was not used to declare the mammal Skin edge false.
  This does not certify every possible taxonomic application of autopod pad.
notes:
- Fresh captures were made at current main after the previous publication; earlier
  scratch captures were not refreshed or reused as provenance.
- All captured bytes match both current files and the exact Git revision. The extractor
  has a separate native supplemental capture.
- Ignored-inclusive traversal found no structured predecessor targeting this identifier.
  Legacy Markdown observations are contextual; no earlier structured finding is silently
  closed.
tags:
- individual-scientific-review
- host-associated
```
