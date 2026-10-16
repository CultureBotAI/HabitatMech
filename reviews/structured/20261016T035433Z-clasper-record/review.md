# Record review: clasper (UBERON:0010516)

- Review: 20261016T035433Z-clasper-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T03:35:10Z
- Finished UTC: 2026-10-16T03:54:33Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The fish reproductive-system source denotes a clasper, consistent with active UBERON:0010516 and its intromittent-organ genus. A generic clasper is not automatically the narrower pelvic-fin subtype: the source does not specify that subtype. The inherited definition includes chimaera cephalic structures, so its detailed functional wording is ontology-sourced rather than a new universal biological claim. Correctly omitted zero counts and truthful SEEDED status do not imply an incomplete required field.

## Scope And Provenance

Full field-by-field assessment of this one resolved generated record.

Selection: One of the next 24 unreviewed records selected in deterministic path order from the ignored-inclusive 3209-record census. This bundle assesses exactly one target, not a proxy sample.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 67cde35918d7361de3a1164fb22756cba5d20e30.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0010516 | data/habitats/host_associated/clasper.yaml | generated | clasper |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | UBERON:0010516 | Finished 2026-10-16T03:35:42Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/clasper.yaml |
| validate-strict | passed | True | UBERON:0010516 | Finished 2026-10-16T03:36:32Z. uv run python scripts/validate_strict.py data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | UBERON:0010516 | Finished 2026-10-16T03:36:40Z. No issues found<br>831 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | UBERON:0010516 | Finished 2026-10-16T03:36:40Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | UBERON:0010516 | Finished 2026-10-16T03:37:54Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | UBERON:0010516 | Finished 2026-10-16T03:38:04Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | UBERON:0010516 | Finished 2026-10-16T03:38:23Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | UBERON:0010516 | Finished 2026-10-16T03:39:05Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted native QC | passed | True | UBERON:0010516 | Verified 2026-10-16T03:43:47Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38843593114 |
| Displayed candidate-pool correspondence | passed | False | UBERON:0010516 | Finished 2026-10-16T03:54:30Z. All 60 displayed candidate pools equal exact source taxon totals. |
| Standalone citation validation applicability | not_applicable | False | UBERON:0010516 | No standalone citation checker is documented for these evidence-free generated targets. Stable references were checked with native gates and current authorities; causal validation ran globally. |

## Scientific And Domain Assessments

### Identity, grounding, aliases and strictly broader hierarchy

identity: supported. Targets: UBERON:0010516.

The fish reproductive-system source denotes a clasper, consistent with active UBERON:0010516 and its intromittent-organ genus. A generic clasper is not automatically the narrower pelvic-fin subtype: the source does not specify that subtype. The inherited definition includes chimaera cephalic structures, so its detailed functional wording is ontology-sourced rather than a new universal biological claim. Correctly omitted zero counts and truthful SEEDED status do not imply an incomplete required field.

### Native source units, ranks, scores and candidate pools

quantity: supported. Targets: UBERON:0010516.

Exact source rows reproduce every emitted count/unit and displayed taxon rank/score/pool. Zero tree counts are omitted; supplemental biosamples, study memberships and triads are nonadditive. {"assertions": [{"source": "GOLD", "count": 0, "unit": "ORGANISM", "row": {"row": 1959, "data": {"canonical_path": "Host-associated &gt; Fish &gt; Reproductive system &gt; Intromittent organ &gt; Clasper", "ecosystem": "Host-associated", "ecosystem_category": "Fish", "ecosystem_type": "Reproductive system", "ecosystem_subtype": "Intromittent organ", "specific_ecosystem": "Clasper", "leaf_label": "Clasper", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7576"}}}], "taxa": []}

### Association evidence and claim scope

evidence: supported. Targets: UBERON:0010516.

Current ontology/TaxId identities and source attestations were verified. The fish reproductive-system source denotes a clasper, consistent with active UBERON:0010516 and its intromittent-organ genus. A generic clasper is not automatically the narrower pelvic-fin subtype: the source does not specify that subtype. The inherited definition includes chimaera cephalic structures, so its detailed functional wording is ontology-sourced rather than a new universal biological claim. Correctly omitted zero counts and truthful SEEDED status do not imply an incomplete required field. Individual papers support only the stated scope; original source pairs were not exhaustively reconstructed.

### Native lifecycle, optional content and mechanism limits

completeness: supported. Targets: UBERON:0010516.

Executed native routes reproduce EXACT/SEEDED. Required content is present. No optional environmental parameters, causal graph, discussion, dataset or characteristic-presence claim is fabricated. Missing ITEM status alone is not a defect; no status or history promotion is performed.

### Native validation and reproducibility

schema: supported. Targets: UBERON:0010516.

31 baseline commands passed: target schema, cohort strict, 831 histories, source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured labels. Exact-base hosted QC passed. Deterministic validity is not scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/clasper.yaml; Entire generated target YAML | supports | All fields, source attestations, displayed taxa, aliases and complete generated history read. |
| ERULE | docs/CURATION.md; Identity, evidence and strictly broader parents | supports | All parent contributions must be strictly broader; source context, anatomy, host and diagnosis are distinct. Optional absence is not a required-field defect. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and GroundingStatusEnum | supports | The mapping contract compares source concept to record identifier; source-is-record omits the predicate. Native status and association rules are preserved. |
| ESEED | src/habitatmech/seed.py; Executed source routes and entire document reproduction | supports | [{"mint": "habitatmech:GOLD.e9b71b9e9c", "automatic": {"identifier": "UBERON:0010516", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0010516", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category": null, "reviewed": false, "decision": null}}] |
| EEXTRACT | src/habitatmech/extract.py; Source counts, source-strain-taxon join and PREGO scoring/ranking | supports | Inspected native projections. Original BacDive source-strain join and PREGO pair citation evidence are not retained in the compact per-habitat taxon tables. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 1959 | supports | [{"row": 1959, "data": {"canonical_path": "Host-associated &gt; Fish &gt; Reproductive system &gt; Intromittent organ &gt; Clasper", "ecosystem": "Host-associated", "ecosystem_category": "Fish", "ecosystem_type": "Reproductive system", "ecosystem_subtype": "Intromittent organ", "specific_ecosystem": "Clasper", "leaf_label": "Clasper", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7576"}}] |
| ET6 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 11652,11704 | supports | [{"row": 11652, "data": {"subject": "UBERON:0008811", "predicate": "rdfs:subClassOf", "object": "UBERON:0003135"}}, {"row": 11704, "data": {"subject": "UBERON:0010516", "predicate": "rdfs:subClassOf", "object": "UBERON:0008811"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 13362,13405 | supports | [{"row": 13362, "data": {"term_id": "UBERON:0008811", "ontology": "UBERON", "label": "intromittent organ", "definition": "An external organ of a male organism that is specialized to deliver sperm during copulation. Intromittent organs are found most often in terrestrial species, as most aquatic species fertilize their eggs externally, although there are exceptions[WP].", "synonyms": "aedeagus&#124;copulatory organ&#124;penis", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row": 13405, "data": {"term_id": "UBERON:0010516", "ontology": "UBERON", "label": "clasper", "definition": "A male anatomical structure found some groups of animals, used in mating. Male cartilaginous fish have claspers formed from the posterior portion of their pelvic fin which serve as intromittent organs used to channel semen into the female's cloaca during mating. The act of mating in some fish including sharks usually includes one of the claspers raised to allow water into the siphon through a specific orifice. The clasper is then inserted into the vagina, where it opens like an umbrella to anchor its position. The siphon then begins to contract expelling water and sperm. Male chimaeras have cephalic claspers on their heads, which are thought to aid in holding the female during mating.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| EP8 | data/habitats/host_associated/intromittent_organ.yaml; Immediate parent record, context only | supports | {"identifier": "UBERON:0008811", "label": "intromittent organ", "definition": "An external organ of a male organism that is specialized to deliver sperm during copulation. Intromittent organs are found most often in terrestrial species, as most aquatic species fertilize their eggs externally, although there are exceptions[WP].", "definition_source": "UBERON", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "aedeagus", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text": "copulatory organ", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text": "penis", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}], "parent_habitats": ["UBERON:0003135", "habitatmech:GOLD.cad831cd73"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7574", "source_label": "Intromittent organ", "source_path": "Host-associated &gt; Fish &gt; Reproductive system &gt; Intromittent organ", "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: EXACT."}]} |
| EH9 | reports/yaml_record_review/20260930T221228Z-clasper.md; Historical findings and proposed edits | supports | Historical reproduction, hierarchy and status assessments were reconsidered. Current strict-parent semantics do not endorse containment-as-subclass or treating missing ITEM status alone as a major defect. No formal predecessor is closed. |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0003135/graph; UBERON_0003135-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0003135", "target": "http://purl.obolibrary.org/obo/UBERON_0003133", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003135", "target": "http://purl.obolibrary.org/obo/UBERON_0000079", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003135", "target": "http://purl.obolibrary.org/obo/UBERON_0003101", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0003135; UBERON_0003135.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:0003135", "label": "male reproductive organ", "is_obsolete": false, "description": ["A male organ involved in reproduction."], "obo_synonym": [{"name": "male organism reproductive organ", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description": null, "url": null}]}, {"name": "male organism reproductive structure", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description": null, "url": null}]}, {"name": "male organism reproductive system organ", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description": null, "url": null}]}, {"name": "male organism sex organ", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description": null, "url": null}]}, {"name": "male reproductive gland/organ", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "MA", "id": "0000545", "description": null, "url": "http://www.informatics.jax.org/searches/AMA.cgi?id=MA:0000545"}]}, {"name": "reproductive organ of male organism", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description": null, "url": null}]}, {"name": "reproductive structure of male organism", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description": null, "url": null}]}, {"name": "reproductive system organ of male organism", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description": null, "url": null}]}, {"name": "sex organ of male organism", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description": null, "url": null}]}, {"name": "male genital", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "WBbt", "id": "0008423", "description": null, "url": "http://www.wormbase.org/get?name=0008423"}]}], "annotation": {"database_cross_reference": ["MA:0000545", "WBbt:0008423"], "id": ["UBERON:0003135"]}} |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0008811/graph; UBERON_0008811-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0008811", "target": "http://purl.obolibrary.org/obo/UBERON_0003135", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0008811", "target": "http://purl.obolibrary.org/obo/GO_0007620", "uri": "http://purl.obolibrary.org/obo/RO_0002216", "label": "capable of part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0008811", "target": "http://purl.obolibrary.org/obo/NCBITaxon_6072", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0008811", "target": "http://purl.obolibrary.org/obo/UBERON_0000079", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0008811", "target": "http://purl.obolibrary.org/obo/UBERON_0000990", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0008811; UBERON_0008811.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:0008811", "label": "intromittent organ", "is_obsolete": false, "description": ["An external organ of a male organism that is specialized to deliver sperm during copulation. Intromittent organs are found most often in terrestrial species, as most aquatic species fertilize their eggs externally, although there are exceptions[WP]."], "obo_synonym": [{"name": "aedeagus", "scope": "hasNarrowSynonym", "type": "taxonomic disambiguation", "xrefs": [{"database": "FBbt", "id": "00004850", "description": null, "url": "http://flybase.org/cgi-bin/fbcvq.html?query=FBbt:00004850"}]}], "annotation": {"curator note": ["this is a broad grouping class connecting a number of different analagous organs by their function. We place the insect aedeagus here rather than penis, although this is somewhat arbitrary given the broadness of the current definition"], "database_cross_reference": ["AAO:0010255", "HAO:0000091", "TAO:0002036", "TGMA:0000585", "Wikipedia:Intromittent_organ", "FBbt:00004850"], "external_definition": ["Surface structure that is an external structure of a male organism through which sperm is transferred to a female organism during mating.[TAO]"], "id": ["UBERON:0008811"]}} |
| EX14 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010516/graph; UBERON_0010516-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0010516", "target": "http://purl.obolibrary.org/obo/UBERON_0008811", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0010516", "target": "http://purl.obolibrary.org/obo/NCBITaxon_7777", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}] |
| EX15 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010516; UBERON_0010516.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:0010516", "label": "clasper", "is_obsolete": false, "description": ["A male anatomical structure found some groups of animals, used in mating. Male cartilaginous fish have claspers formed from the posterior portion of their pelvic fin which serve as intromittent organs used to channel semen into the female's cloaca during mating. The act of mating in some fish including sharks usually includes one of the claspers raised to allow water into the siphon through a specific orifice. The clasper is then inserted into the vagina, where it opens like an umbrella to anchor its position. The siphon then begins to contract expelling water and sperm. Male chimaeras have cephalic claspers on their heads, which are thought to aid in holding the female during mating."], "obo_synonym": null, "annotation": {"database_cross_reference": ["Wikipedia:clasper"], "id": ["UBERON:0010516"], "taxon_notes": ["the term is also used for insect claspers, but we reserve it for the elasmobranchii structure"]}} |
| ESEARCH | Local source/curation/review corpus; rg --no-ignore --hidden -l -F -e UBERON:0010516 -e clasper -e clasper -e habitatmech:GOLD.e9b71b9e9c curation history research reports data/raw build reviews | context_only | Source rows were parsed by exact keys; broad name hits were leads, not all inspected. No formal structured target predecessor. |

## Limits And Additional Notes

- Original specimen-level evidence and every pair-level citation were not exhaustively reconstructed. Source associations, counts, ranks and scores are not prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs; target TaxIds were separately resolved with current NCBI.
- Exact-base hosted QC covers unchanged scientific inputs, not a new local full-QC execution or these new review files. Each new bundle requires native validation/save and the subsequent archive check.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. Cited experiments are used only for identity and context, not imported causal mechanisms.
- Captured working_tree provenance is retained. All local input hashes were additionally checked against exact base 67cde35918d7361de3a1164fb22756cba5d20e30.
- Read-only review: no source, curation, generated record, status or history edit; no GitHub mutation or paid research.
- Ignored-inclusive structured archive traversal found no previous structured target review. Legacy prose is contextual evidence, not formal predecessor lineage or issue closure.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T035433Z-clasper-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: clasper (UBERON:0010516)'
started_at: '2026-10-16T03:35:10Z'
finished_at: '2026-10-16T03:54:33Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assessed all evidence and target; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'The fish reproductive-system source denotes a clasper, consistent with active
  UBERON:0010516 and its intromittent-organ genus. A generic clasper is not automatically
  the narrower pelvic-fin subtype: the source does not specify that subtype. The inherited
  definition includes chimaera cephalic structures, so its detailed functional wording
  is ontology-sourced rather than a new universal biological claim. Correctly omitted
  zero counts and truthful SEEDED status do not imply an incomplete required field.'
source:
  git_revision: 67cde35918d7361de3a1164fb22756cba5d20e30
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
  - path: data/habitats/host_associated/clasper.yaml
    sha256: dda2e5bfc54590afaa85bf7fd5162defbb4752dacef0c62d62b3b56751072eb2
    role: target
  - path: data/habitats/host_associated/intromittent_organ.yaml
    sha256: 671d36e9595e438c27152c707e44d67013a736737b5bd49b4774c86c1c4cae0d
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
  - path: reports/yaml_record_review/20260930T221228Z-clasper.md
    sha256: 07ca323a448432498b0edfe86280acb3e4eac3237a673ddabb28de1d1e25c19b
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
targets:
- target_id: UBERON:0010516
  path: data/habitats/host_associated/clasper.yaml
  label: clasper
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
  description: Full field-by-field assessment of this one resolved generated record.
  selection: One of the next 24 unreviewed records selected in deterministic path
    order from the ignored-inclusive 3209-record census. This bundle assesses exactly
    one target, not a proxy sample.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0010516
  exclusions:
  - target: Other records, individual source specimens and SSSOM/KGX products
    reason: Parent context is not additional review coverage; original specimens and
      exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/clasper.yaml
  exit_code: 0
  target_ids:
  - UBERON:0010516
  summary: "Finished 2026-10-16T03:35:42Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/clasper.yaml"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml
    data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml
    data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml
    data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml
    data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml
    data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml
    data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml
    data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml
    data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml
    data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml
    data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml
    data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml
  exit_code: 0
  target_ids:
  - UBERON:0010516
  summary: "Finished 2026-10-16T03:36:32Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml\
    \ data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml\
    \ data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml\
    \ data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml\
    \ data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml\
    \ data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml\
    \ data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml\
    \ data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml\
    \ data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml\
    \ data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml\
    \ data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml\
    \ data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - UBERON:0010516
  summary: 'Finished 2026-10-16T03:36:40Z. No issues found

    831 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - UBERON:0010516
  summary: "Finished 2026-10-16T03:36:40Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - UBERON:0010516
  summary: "Finished 2026-10-16T03:37:54Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - UBERON:0010516
  summary: "Finished 2026-10-16T03:38:04Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - UBERON:0010516
  summary: "Finished 2026-10-16T03:38:23Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - UBERON:0010516
  summary: "Finished 2026-10-16T03:39:05Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict covers the 24-record cohort; history, provenance,
    reproduction, causal, term and configured label checks are full-corpus.
- check_id: CCI
  name: Exact-base hosted native QC
  status: passed
  required: true
  command: gh run view 38843593114 --repo CultureBotAI/HabitatMech --json headSha,conclusion,url,jobs
  exit_code: 0
  target_ids:
  - UBERON:0010516
  summary: Verified 2026-10-16T03:43:47Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38843593114
  scope_note: Unchanged scientific-input base only. Not a claim that the new output
    bundles were part of the earlier run.
- check_id: CPOOL
  name: Displayed candidate-pool correspondence
  status: passed
  required: false
  command: .venv/bin/python /private/tmp/habitatmech-review-cq-author.py pool_check
  exit_code: 0
  target_ids:
  - UBERON:0010516
  summary: Finished 2026-10-16T03:54:30Z. All 60 displayed candidate pools equal exact
    source taxon totals.
  scope_note: Supplemental mechanical cross-check of all 60 displayed taxon entries;
    not a replacement for native validators or scientific evidence.
- check_id: CREF
  name: Standalone citation validation applicability
  status: not_applicable
  required: false
  target_ids:
  - UBERON:0010516
  summary: No standalone citation checker is documented for these evidence-free generated
    targets. Stable references were checked with native gates and current authorities;
    causal validation ran globally.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/clasper.yaml
  locator: Entire generated target YAML
  accessed_at: '2026-10-16T03:54:33Z'
  support: supports
  summary: All fields, source attestations, displayed taxa, aliases and complete generated
    history read.
  snapshot_sha256: dda2e5bfc54590afaa85bf7fd5162defbb4752dacef0c62d62b3b56751072eb2
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, evidence and strictly broader parents
  accessed_at: '2026-10-16T03:54:33Z'
  support: supports
  summary: All parent contributions must be strictly broader; source context, anatomy,
    host and diagnosis are distinct. Optional absence is not a required-field defect.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and GroundingStatusEnum
  accessed_at: '2026-10-16T03:54:33Z'
  support: supports
  summary: The mapping contract compares source concept to record identifier; source-is-record
    omits the predicate. Native status and association rules are preserved.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source routes and entire document reproduction
  accessed_at: '2026-10-16T03:54:33Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.e9b71b9e9c", "automatic": {"identifier": "UBERON:0010516",
    "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category":
    null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0010516",
    "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category":
    null, "reviewed": false, "decision": null}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Source counts, source-strain-taxon join and PREGO scoring/ranking
  accessed_at: '2026-10-16T03:54:33Z'
  support: supports
  summary: Inspected native projections. Original BacDive source-strain join and PREGO
    pair citation evidence are not retained in the compact per-habitat taxon tables.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 1959
  accessed_at: '2026-10-16T03:54:33Z'
  support: supports
  summary: '[{"row": 1959, "data": {"canonical_path": "Host-associated > Fish > Reproductive
    system > Intromittent organ > Clasper", "ecosystem": "Host-associated", "ecosystem_category":
    "Fish", "ecosystem_type": "Reproductive system", "ecosystem_subtype": "Intromittent
    organ", "specific_ecosystem": "Clasper", "leaf_label": "Clasper", "depth": "5",
    "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count":
    "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7576"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 11652,11704
  accessed_at: '2026-10-16T03:54:33Z'
  support: supports
  summary: '[{"row": 11652, "data": {"subject": "UBERON:0008811", "predicate": "rdfs:subClassOf",
    "object": "UBERON:0003135"}}, {"row": 11704, "data": {"subject": "UBERON:0010516",
    "predicate": "rdfs:subClassOf", "object": "UBERON:0008811"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 13362,13405
  accessed_at: '2026-10-16T03:54:33Z'
  support: supports
  summary: '[{"row": 13362, "data": {"term_id": "UBERON:0008811", "ontology": "UBERON",
    "label": "intromittent organ", "definition": "An external organ of a male organism
    that is specialized to deliver sperm during copulation. Intromittent organs are
    found most often in terrestrial species, as most aquatic species fertilize their
    eggs externally, although there are exceptions[WP].", "synonyms": "aedeagus|copulatory
    organ|penis", "deprecated": "", "directly_referenced": "FALSE", "label_only":
    "FALSE"}}, {"row": 13405, "data": {"term_id": "UBERON:0010516", "ontology": "UBERON",
    "label": "clasper", "definition": "A male anatomical structure found some groups
    of animals, used in mating. Male cartilaginous fish have claspers formed from
    the posterior portion of their pelvic fin which serve as intromittent organs used
    to channel semen into the female''s cloaca during mating. The act of mating in
    some fish including sharks usually includes one of the claspers raised to allow
    water into the siphon through a specific orifice. The clasper is then inserted
    into the vagina, where it opens like an umbrella to anchor its position. The siphon
    then begins to contract expelling water and sperm. Male chimaeras have cephalic
    claspers on their heads, which are thought to aid in holding the female during
    mating.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only":
    "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: EP8
  kind: record_content
  reference: data/habitats/host_associated/intromittent_organ.yaml
  locator: Immediate parent record, context only
  accessed_at: '2026-10-16T03:54:33Z'
  support: supports
  summary: '{"identifier": "UBERON:0008811", "label": "intromittent organ", "definition":
    "An external organ of a male organism that is specialized to deliver sperm during
    copulation. Intromittent organs are found most often in terrestrial species, as
    most aquatic species fertilize their eggs externally, although there are exceptions[WP].",
    "definition_source": "UBERON", "habitat_category": "HOST_ASSOCIATED", "grounding_status":
    "EXACT", "mapping_status": "SEEDED", "synonyms": [{"synonym_text": "aedeagus",
    "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text": "copulatory
    organ", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}, {"synonym_text":
    "penis", "synonym_type": "EXACT_SYNONYM", "source": "UBERON"}], "parent_habitats":
    ["UBERON:0003135", "habitatmech:GOLD.cad831cd73"], "source_attestations": [{"source":
    "GOLD", "source_id": "gold.ecosystem:7574", "source_label": "Intromittent organ",
    "source_path": "Host-associated > Fish > Reproductive system > Intromittent organ",
    "mapping_predicate": "skos:exactMatch", "notes": "2 GOLD ecosystem node ids share
    this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: EXACT."}]}'
  snapshot_sha256: 671d36e9595e438c27152c707e44d67013a736737b5bd49b4774c86c1c4cae0d
- evidence_id: EH9
  kind: record_content
  reference: reports/yaml_record_review/20260930T221228Z-clasper.md
  locator: Historical findings and proposed edits
  accessed_at: '2026-10-16T03:54:33Z'
  support: supports
  summary: Historical reproduction, hierarchy and status assessments were reconsidered.
    Current strict-parent semantics do not endorse containment-as-subclass or treating
    missing ITEM status alone as a major defect. No formal predecessor is closed.
  snapshot_sha256: 07ca323a448432498b0edfe86280acb3e4eac3237a673ddabb28de1d1e25c19b
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0003135/graph
  locator: UBERON_0003135-graph.json
  accessed_at: '2026-10-16T03:37:26Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0003135",
    "target": "http://purl.obolibrary.org/obo/UBERON_0003133", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003135",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000079", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0003135",
    "target": "http://purl.obolibrary.org/obo/UBERON_0003101", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 99872550ad66a40dbcc52e3554402d550dab567ea4e44eb4bf0545b50a514c1d
- evidence_id: EX11
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0003135
  locator: UBERON_0003135.json
  accessed_at: '2026-10-16T03:37:25Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:0003135", "label": "male reproductive organ", "is_obsolete": false, "description":
    ["A male organ involved in reproduction."], "obo_synonym": [{"name": "male organism
    reproductive organ", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database":
    "OBOL", "id": "automatic", "description": null, "url": null}]}, {"name": "male
    organism reproductive structure", "scope": "hasExactSynonym", "type": null, "xrefs":
    [{"database": "OBOL", "id": "automatic", "description": null, "url": null}]},
    {"name": "male organism reproductive system organ", "scope": "hasExactSynonym",
    "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description":
    null, "url": null}]}, {"name": "male organism sex organ", "scope": "hasExactSynonym",
    "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description":
    null, "url": null}]}, {"name": "male reproductive gland/organ", "scope": "hasExactSynonym",
    "type": null, "xrefs": [{"database": "MA", "id": "0000545", "description": null,
    "url": "http://www.informatics.jax.org/searches/AMA.cgi?id=MA:0000545"}]}, {"name":
    "reproductive organ of male organism", "scope": "hasExactSynonym", "type": null,
    "xrefs": [{"database": "OBOL", "id": "automatic", "description": null, "url":
    null}]}, {"name": "reproductive structure of male organism", "scope": "hasExactSynonym",
    "type": null, "xrefs": [{"database": "OBOL", "id": "automatic", "description":
    null, "url": null}]}, {"name": "reproductive system organ of male organism", "scope":
    "hasExactSynonym", "type": null, "xrefs": [{"database": "OBOL", "id": "automatic",
    "description": null, "url": null}]}, {"name": "sex organ of male organism", "scope":
    "hasExactSynonym", "type": null, "xrefs": [{"database": "OBOL", "id": "automatic",
    "description": null, "url": null}]}, {"name": "male genital", "scope": "hasRelatedSynonym",
    "type": null, "xrefs": [{"database": "WBbt", "id": "0008423", "description": null,
    "url": "http://www.wormbase.org/get?name=0008423"}]}], "annotation": {"database_cross_reference":
    ["MA:0000545", "WBbt:0008423"], "id": ["UBERON:0003135"]}}'
  snapshot_sha256: dd9b1cc29b50c9e81315a02f47d71df7a8bf5271b9b30fa75e6aaa9ba01f9551
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0008811/graph
  locator: UBERON_0008811-graph.json
  accessed_at: '2026-10-16T03:37:31Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0008811",
    "target": "http://purl.obolibrary.org/obo/UBERON_0003135", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0008811",
    "target": "http://purl.obolibrary.org/obo/GO_0007620", "uri": "http://purl.obolibrary.org/obo/RO_0002216",
    "label": "capable of part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0008811",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_6072", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0008811",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000079", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0008811",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000990", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: f6bb137f7691e5c2ac306be8be397ef0a35aa0a5384a841f1c585c007aa2d5ab
- evidence_id: EX13
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0008811
  locator: UBERON_0008811.json
  accessed_at: '2026-10-16T03:37:30Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:0008811", "label": "intromittent organ", "is_obsolete": false, "description":
    ["An external organ of a male organism that is specialized to deliver sperm during
    copulation. Intromittent organs are found most often in terrestrial species, as
    most aquatic species fertilize their eggs externally, although there are exceptions[WP]."],
    "obo_synonym": [{"name": "aedeagus", "scope": "hasNarrowSynonym", "type": "taxonomic
    disambiguation", "xrefs": [{"database": "FBbt", "id": "00004850", "description":
    null, "url": "http://flybase.org/cgi-bin/fbcvq.html?query=FBbt:00004850"}]}],
    "annotation": {"curator note": ["this is a broad grouping class connecting a number
    of different analagous organs by their function. We place the insect aedeagus
    here rather than penis, although this is somewhat arbitrary given the broadness
    of the current definition"], "database_cross_reference": ["AAO:0010255", "HAO:0000091",
    "TAO:0002036", "TGMA:0000585", "Wikipedia:Intromittent_organ", "FBbt:00004850"],
    "external_definition": ["Surface structure that is an external structure of a
    male organism through which sperm is transferred to a female organism during mating.[TAO]"],
    "id": ["UBERON:0008811"]}}'
  snapshot_sha256: d70606db306d85ff98c2e90a7a14eaee86e25495b68f9a7bc7f939f5587625ee
- evidence_id: EX14
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010516/graph
  locator: UBERON_0010516-graph.json
  accessed_at: '2026-10-16T03:37:34Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0010516",
    "target": "http://purl.obolibrary.org/obo/UBERON_0008811", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0010516",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_7777", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}]'
  snapshot_sha256: 817cb77a458d24bb7ad3efab52a2076c572c2c71a1c8a9a90fafabd3d0316872
- evidence_id: EX15
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0010516
  locator: UBERON_0010516.json
  accessed_at: '2026-10-16T03:37:32Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:0010516", "label": "clasper", "is_obsolete": false, "description": ["A
    male anatomical structure found some groups of animals, used in mating. Male cartilaginous
    fish have claspers formed from the posterior portion of their pelvic fin which
    serve as intromittent organs used to channel semen into the female''s cloaca during
    mating. The act of mating in some fish including sharks usually includes one of
    the claspers raised to allow water into the siphon through a specific orifice.
    The clasper is then inserted into the vagina, where it opens like an umbrella
    to anchor its position. The siphon then begins to contract expelling water and
    sperm. Male chimaeras have cephalic claspers on their heads, which are thought
    to aid in holding the female during mating."], "obo_synonym": null, "annotation":
    {"database_cross_reference": ["Wikipedia:clasper"], "id": ["UBERON:0010516"],
    "taxon_notes": ["the term is also used for insect claspers, but we reserve it
    for the elasmobranchii structure"]}}'
  snapshot_sha256: a411bb812b5916d16de27afd4616c2870f4eac52f8b4cea0baa9c928bc2e54b3
- evidence_id: ESEARCH
  kind: search
  reference: Local source/curation/review corpus
  locator: rg --no-ignore --hidden -l -F -e UBERON:0010516 -e clasper -e clasper -e
    habitatmech:GOLD.e9b71b9e9c curation history research reports data/raw build reviews
  accessed_at: '2026-10-16T03:36:40Z'
  support: context_only
  summary: Source rows were parsed by exact keys; broad name hits were leads, not
    all inspected. No formal structured target predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews
    including hidden/ignored files; structured YAML archive parsed independently of
    gitignore.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, grounding, aliases and strictly broader hierarchy
  outcome: supported
  summary: 'The fish reproductive-system source denotes a clasper, consistent with
    active UBERON:0010516 and its intromittent-organ genus. A generic clasper is not
    automatically the narrower pelvic-fin subtype: the source does not specify that
    subtype. The inherited definition includes chimaera cephalic structures, so its
    detailed functional wording is ontology-sourced rather than a new universal biological
    claim. Correctly omitted zero counts and truthful SEEDED status do not imply an
    incomplete required field.'
  target_ids:
  - UBERON:0010516
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EP8
  - EH9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
- assessment_id: A2
  area: quantity
  topic: Native source units, ranks, scores and candidate pools
  outcome: supported
  summary: 'Exact source rows reproduce every emitted count/unit and displayed taxon
    rank/score/pool. Zero tree counts are omitted; supplemental biosamples, study
    memberships and triads are nonadditive. {"assertions": [{"source": "GOLD", "count":
    0, "unit": "ORGANISM", "row": {"row": 1959, "data": {"canonical_path": "Host-associated
    > Fish > Reproductive system > Intromittent organ > Clasper", "ecosystem": "Host-associated",
    "ecosystem_category": "Fish", "ecosystem_type": "Reproductive system", "ecosystem_subtype":
    "Intromittent organ", "specific_ecosystem": "Clasper", "leaf_label": "Clasper",
    "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0",
    "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7576"}}}],
    "taxa": []}'
  target_ids:
  - UBERON:0010516
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EP8
  - EH9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
- assessment_id: A3
  area: evidence
  topic: Association evidence and claim scope
  outcome: supported
  summary: 'Current ontology/TaxId identities and source attestations were verified.
    The fish reproductive-system source denotes a clasper, consistent with active
    UBERON:0010516 and its intromittent-organ genus. A generic clasper is not automatically
    the narrower pelvic-fin subtype: the source does not specify that subtype. The
    inherited definition includes chimaera cephalic structures, so its detailed functional
    wording is ontology-sourced rather than a new universal biological claim. Correctly
    omitted zero counts and truthful SEEDED status do not imply an incomplete required
    field. Individual papers support only the stated scope; original source pairs
    were not exhaustively reconstructed.'
  target_ids:
  - UBERON:0010516
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - EP8
  - EH9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
- assessment_id: A4
  area: completeness
  topic: Native lifecycle, optional content and mechanism limits
  outcome: supported
  summary: Executed native routes reproduce EXACT/SEEDED. Required content is present.
    No optional environmental parameters, causal graph, discussion, dataset or characteristic-presence
    claim is fabricated. Missing ITEM status alone is not a defect; no status or history
    promotion is performed.
  target_ids:
  - UBERON:0010516
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native validation and reproducibility
  outcome: supported
  summary: '31 baseline commands passed: target schema, cohort strict, 831 histories,
    source provenance, exact 3209-record reproduction, 32 causal overlays, 110 term
    requests and configured labels. Exact-base hosted QC passed. Deterministic validity
    is not scientific approval.'
  target_ids:
  - UBERON:0010516
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
findings: []
actions: []
limitations:
- Original specimen-level evidence and every pair-level citation were not exhaustively
  reconstructed. Source associations, counts, ranks and scores are not prevalence,
  viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs; target TaxIds were separately
  resolved with current NCBI.
- Exact-base hosted QC covers unchanged scientific inputs, not a new local full-QC
  execution or these new review files. Each new bundle requires native validation/save
  and the subsequent archive check.
- 'iModulonDB is not applicable: no gene, regulator or expression-module claim is
  asserted. Cited experiments are used only for identity and context, not imported
  causal mechanisms.'
notes:
- Captured working_tree provenance is retained. All local input hashes were additionally
  checked against exact base 67cde35918d7361de3a1164fb22756cba5d20e30.
- 'Read-only review: no source, curation, generated record, status or history edit;
  no GitHub mutation or paid research.'
- Ignored-inclusive structured archive traversal found no previous structured target
  review. Legacy prose is contextual evidence, not formal predecessor lineage or issue
  closure.
tags:
- individual-scientific-review
- host-associated
```
