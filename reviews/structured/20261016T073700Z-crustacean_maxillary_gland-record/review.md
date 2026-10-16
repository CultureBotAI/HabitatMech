# Record review: crustacean maxillary gland (UBERON:0009964)

- Review: 20261016T073700Z-crustacean_maxillary_gland-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T07:13:05Z
- Finished UTC: 2026-10-16T07:37:00Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The ITEM grounding correctly identifies a crustacean excretory organ, not the mammalian salivary gland reached by the default lexical route. Active UBERON:0009964 and its excretory-gland genus support the definition. The whole crustacean Excretory system is a location/system context, not a strictly broader gland class. Preserve the correct identity, gland genus, contextual source alias and two collapsed GOLD node IDs; zero organism assertions do not mean the organ cannot host microbes.

## Scope And Provenance

Full field-by-field assessment of this exact generated record.

Selection: One of the next 24 unreviewed records in deterministic path order from an ignored-inclusive 3209-record census. This individual report is not proxy coverage for other records.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 34f65fac61907aa03cf13705201f30da8b963b0a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| UBERON:0009964 | data/habitats/host_associated/crustacean_maxillary_gland.yaml | generated | crustacean maxillary gland |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | UBERON:0009964 | Finished 2026-10-16T07:13:30Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/crustacean_maxillary_gland.yaml |
| validate-strict | passed | True | UBERON:0009964 | Finished 2026-10-16T07:16:52Z. uv run python scripts/validate_strict.py data/habitats/host_associated/crustacean_maxillary_gland.yaml data/habitats/host_associated/crustacean_post_larval_stage.yaml data/habitats/host_associated/cryptomonads_cryptophytes.yaml data/habitats/host_associated/ctenophora.yaml data/habitats/host_associated/cud.yaml data/habitats/host_associated/cutaneous_leishmaniasis.yaml data/habitats/host_associated/cuticle.yaml data/habitats/host_associated/cuticle__11d6cb22.yaml data/habitats/host_associated/cuticle__6c2a3dac.yaml data/habitats/host_associated/cuticle__72f050c4.yaml data/habitats/host_associated/cuticle__9784f327.yaml data/habitats/host_associated/cuticle__a024212e.yaml data/habitats/host_associated/cv_1_cell.yaml data/habitats/host_associated/cyst.yaml data/habitats/host_associated/decayed_wood__afd3403c.yaml data/habitats/host_associated/decomposed_body.yaml data/habitats/host_associated/decomposed_body__7ba62861.yaml data/habitats/host_associated/decomposed_body__ee215354.yaml data/habitats/host_associated/dental_abscess.yaml data/habitats/host_associated/dental_calculus.yaml data/habitats/host_associated/dental_calculus__18e49dca.yaml data/habitats/host_associated/dental_calculus__8a0a99ac.yaml data/habitats/host_associated/dental_plaque.yaml data/habitats/host_associated/dental_plaque__384bd6e9.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | UBERON:0009964 | Finished 2026-10-16T07:17:04Z. No issues found<br>836 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | UBERON:0009964 | Finished 2026-10-16T07:17:05Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | UBERON:0009964 | Finished 2026-10-16T07:17:30Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | UBERON:0009964 | Finished 2026-10-16T07:17:36Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | UBERON:0009964 | Finished 2026-10-16T07:18:01Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | UBERON:0009964 | Finished 2026-10-16T07:19:10Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-base hosted QC | passed | True | UBERON:0009964 | Verified 2026-10-16T07:18:44Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38863397429 |
| Candidate-pool and displayed-entry correspondence | passed | False | UBERON:0009964 | All 18 displayed candidate pools equal exact source taxon totals. |
| Standalone record citation-validator applicability | not_applicable | False | UBERON:0009964 | No standalone citation validator is documented for these generated targets without record-level citation blocks. Stable identifiers and source references were checked directly; causal validation ran globally. |

## Scientific And Domain Assessments

### Identity, definition, source scope, aliases and parent meanings

identity: concern. Targets: UBERON:0009964.

The ITEM grounding correctly identifies a crustacean excretory organ, not the mammalian salivary gland reached by the default lexical route. Active UBERON:0009964 and its excretory-gland genus support the definition. The whole crustacean Excretory system is a location/system context, not a strictly broader gland class. Preserve the correct identity, gland genus, contextual source alias and two collapsed GOLD node IDs; zero organism assertions do not mean the organ cannot host microbes.

### Source counts, units, scores, ranks and pool denominators

quantity: supported. Targets: UBERON:0009964.

Exact raw rows reproduce every emitted count, unit, rank, score and candidate pool. GOLD zero counts are omitted; side-table biosamples, study memberships and triads are not added to organism totals. {"assertions": [{"source": "GOLD", "count": 0, "unit": "ORGANISM", "row": {"row": 1769, "data": {"canonical_path": "Host-associated &gt; Arthropoda: Crustaceans &gt; Excretory system &gt; Maxillary glands", "ecosystem": "Host-associated", "ecosystem_category": "Arthropoda: Crustaceans", "ecosystem_type": "Excretory system", "ecosystem_subtype": "Maxillary glands", "specific_ecosystem": "", "leaf_label": "Maxillary glands", "depth": "4", "gold_node_count": "2", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7334&#124;gold.ecosystem:7335"}}}], "taxa": []}

### Source association versus biological localization

evidence: supported. Targets: UBERON:0009964.

The ITEM grounding correctly identifies a crustacean excretory organ, not the mammalian salivary gland reached by the default lexical route. Active UBERON:0009964 and its excretory-gland genus support the definition. The whole crustacean Excretory system is a location/system context, not a strictly broader gland class. Preserve the correct identity, gland genus, contextual source alias and two collapsed GOLD node IDs; zero organism assertions do not mean the organ cannot host microbes. The supporting authorities and primary studies have only the scopes stated in their evidence entries. Original specimen evidence is not fully reconstructed.

### Native status, source history and optional scientific content

completeness: supported. Targets: UBERON:0009964.

Executed generation reproduces EXACT/REVIEWED. Status truthfully records decision depth, not the outcome of this review. No absent optional graph, parameter, discussion, dataset or characteristic-presence flag is fabricated. Known scientific contradictions are retained above; missing ITEM status alone is not an issue.

### Native structural validation and reproduction

schema: supported. Targets: UBERON:0009964.

All 31 baseline commands passed: 24 individual schemas, cohort strict, 836 histories, provenance, exact 3209-record reproduction, 32 causal overlays, 110 term requests and configured labels. Exact-base hosted QC passed; none of these gates proves scientific support.

## Findings

### F1: Source context is not a strictly broader habitat class

major / open / confirmed; issue key: crustacean-maxillary-gland-context-parent.

The ITEM grounding correctly identifies a crustacean excretory organ, not the mammalian salivary gland reached by the default lexical route. Active UBERON:0009964 and its excretory-gland genus support the definition. The whole crustacean Excretory system is a location/system context, not a strictly broader gland class. Preserve the correct identity, gland genus, contextual source alias and two collapsed GOLD node IDs; zero organism assertions do not mean the organ cannot host microbes. Exact context contribution: habitatmech:GOLD.d0a97e09fe. Use the guarded GOLD-parent exclusion after source-scope review, retaining independent true parents.

## Recommended Actions And Acceptance Checks

### ACT1

The ITEM grounding correctly identifies a crustacean excretory organ, not the mammalian salivary gland reached by the default lexical route. Active UBERON:0009964 and its excretory-gland genus support the definition. The whole crustacean Excretory system is a location/system context, not a strictly broader gland class. Preserve the correct identity, gland genus, contextual source alias and two collapsed GOLD node IDs; zero organism assertions do not mean the organ cannot host microbes. Exact context contribution: habitatmech:GOLD.d0a97e09fe. Use the guarded GOLD-parent exclusion after source-scope review, retaining independent true parents. Proposed work only; no repair or status promotion is performed by this review.

- Regress the exact target claim and preserve valid genera, identifiers, source counts/units and taxon associations. Recover original evidence before deleting a provisional pair; do not decrement frozen totals by hand.
- Record authorized curation history; require schema, strict, provenance, history, label, corpus, site and full QC gates.
- Save an immutable successor with the same issue key and exact predecessor finding identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/crustacean_maxillary_gland.yaml; Entire generated YAML, including complete history | supports | Every field read; exact source identity, aliases, parents, assertions and taxa assessed. |
| ERULE | docs/CURATION.md; Host identity, source evidence and strict broader-parent rules | supports | Host environment, anatomy, whole system, life stage and disease are distinct; every parent contribution must be strictly broader. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation, TaxonAssociation and grounding/status semantics | supports | Source mapping endpoint is the record identifier; source-is-record omits a mapping predicate. Counts retain their units and reported association does not imply characteristic presence. |
| ESEED | src/habitatmech/seed.py; Executed source resolution and exact document regeneration | supports | [{"mint": "habitatmech:GOLD.82cc79ac14", "automatic": {"identifier": "habitatmech:GOLD.82cc79ac14", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0009964", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_ground_from_gold_unmatched", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.82cc79ac14", "decision": "GROUND", "object_id": "UBERON:0009964", "object_label": "crustacean maxillary gland", "grounding_status": "EXACT", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Variant-match review (#12): the variant route reaches UBERON:0001736 'submandibular gland', a mammalian SALIVARY gland. The path is Crustaceans &gt; Excretory system, and UBERON has a distinct crustacean maxillary gland. Same word, different phylum and different organ system. Path: Host-associated &gt; Arthropoda: Crustaceans &gt; Excretory system &gt; Maxillary glands", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; extract_prego and source projections | supports | Per-pair maximum score, direct flag and deterministic rank reproduce source associations. The compact taxon tables do not retain original pair citations. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 1769 | supports | [{"row": 1769, "data": {"canonical_path": "Host-associated &gt; Arthropoda: Crustaceans &gt; Excretory system &gt; Maxillary glands", "ecosystem": "Host-associated", "ecosystem_category": "Arthropoda: Crustaceans", "ecosystem_type": "Excretory system", "ecosystem_subtype": "Maxillary glands", "specific_ecosystem": "", "leaf_label": "Maxillary glands", "depth": "4", "gold_node_count": "2", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:7334&#124;gold.ecosystem:7335"}}] |
| ET6 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 11677,11679 | supports | [{"row": 11677, "data": {"subject": "UBERON:0009962", "predicate": "rdfs:subClassOf", "object": "UBERON:0002530"}}, {"row": 11679, "data": {"subject": "UBERON:0009964", "predicate": "rdfs:subClassOf", "object": "UBERON:0009962"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 13384,13386 | supports | [{"row": 13384, "data": {"term_id": "UBERON:0009962", "ontology": "UBERON", "label": "excretory gland", "definition": "A gland that discharges its secretion through a duct opening on an internal or external surface of the body, as a lacrimal gland.", "synonyms": "renal gland", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row": 13386, "data": {"term_id": "UBERON:0009964", "ontology": "UBERON", "label": "crustacean maxillary gland", "definition": "Excretory organ in maxillary segment with duct opening on maxilla.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET8 | curation/decisions.tsv; Physical TSV rows 1677 | supports | [{"row": 1677, "data": {"identifier": "habitatmech:GOLD.82cc79ac14", "decision": "GROUND", "object_id": "UBERON:0009964", "object_label": "crustacean maxillary gland", "grounding_status": "EXACT", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "Variant-match review (#12): the variant route reaches UBERON:0001736 'submandibular gland', a mammalian SALIVARY gland. The path is Crustaceans &gt; Excretory system, and UBERON has a distinct crustacean maxillary gland. Same word, different phylum and different organ system. Path: Host-associated &gt; Arthropoda: Crustaceans &gt; Excretory system &gt; Maxillary glands", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP9 | data/habitats/host_associated/excretory_system__22ee753c.yaml; Complete immediate parent, context only | supports | {"identifier": "habitatmech:GOLD.d0a97e09fe", "label": "Excretory system", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:8450002", "habitatmech:GOLD.2959225799"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7329", "source_label": "Excretory system", "source_path": "Host-associated &gt; Arthropoda: Crustaceans &gt; Excretory system", "mapping_predicate": "skos:narrowMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]} |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009962/graph; UBERON_0009962-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0009962", "target": "http://purl.obolibrary.org/obo/UBERON_0002530", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0009962", "target": "http://purl.obolibrary.org/obo/UBERON_8450002", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009962; UBERON_0009962.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:0009962", "label": "excretory gland", "is_obsolete": false, "description": ["A gland that discharges its secretion through a duct opening on an internal or external surface of the body, as a lacrimal gland."], "obo_synonym": [{"name": "renal gland", "scope": "hasNarrowSynonym", "type": null, "xrefs": [{"database": null, "id": "https://github.com/obophenotype/uberon/issues/1450", "description": null, "url": "https://github.com/obophenotype/uberon/issues/1450"}]}], "annotation": {"database_cross_reference": ["BTO:0000431"], "editor note": ["TODO - child terms"], "id": ["UBERON:0009962"]}} |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009964/graph; UBERON_0009964-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0009964", "target": "http://purl.obolibrary.org/obo/UBERON_0009962", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0009964", "target": "http://purl.obolibrary.org/obo/NCBITaxon_197562", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}] |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009964; UBERON_0009964.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:0009964", "label": "crustacean maxillary gland", "is_obsolete": false, "description": ["Excretory organ in maxillary segment with duct opening on maxilla."], "obo_synonym": null, "annotation": {"editor note": ["cede this term to Arthropod AO"], "id": ["UBERON:0009964"], "never in taxon": ["http://purl.obolibrary.org/obo/NCBITaxon_6960"], "taxon_notes": ["consider generalizing to include millipedes, centipedes. Function: Two different excretory organs are found among crustaceans: the antennal gland and the maxillary gland. Both have the same basic structure: an end sac and a convoluted duct that may expand into a bladder before opening to the outside. In most adult crustaceans only one or the other gland functions. The functional gland may change during the life cycle. Terminology note: http://crustacea.nhm.org/glossary/define.html?termID=327 suggests green gland as the generic term and antennal as the decapoda term"]}} |
| EX14 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_8450002/graph; UBERON_8450002-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_8450002", "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_8450002", "target": "http://purl.obolibrary.org/obo/GO_0046903", "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}] |
| EX15 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_8450002; UBERON_8450002.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:8450002", "label": "excretory system", "is_obsolete": false, "description": ["An anatomical system that eliminates waste products that arise as a result of metabolic activity."], "obo_synonym": null, "annotation": {"created by": ["http://orcid.org/0000-0002-6095-8718"], "creation date": ["2022-05-25T18:21:29Z"], "database_cross_reference": ["BTO:0006338"], "id": ["UBERON:8450002"]}} |
| ESEARCH | Local raw, maintained-input and review corpus; rg --no-ignore --hidden -l -F -e UBERON:0009964 -e 'crustacean maxillary gland' -e crustacean_maxillary_gland -e habitatmech:GOLD.82cc79ac14 curation history research reports data/raw build reviews | context_only | Exact source rows parsed. Broad matching files are leads, not a claim that every match was inspected. No formal structured target predecessor found. |

## Limits And Additional Notes

- Original specimen-level evidence was not exhaustively reconstructed. Source counts, associations and scores do not establish prevalence, viability or characteristic presence.
- Configured id-label validation skips 2063 no-adapter pairs; the 18 displayed target TaxIds were separately checked against current NCBI.
- Exact-base hosted QC covers unchanged scientific inputs, not a newly executed local full QC or these new output bundles. Native output validation/save and the subsequent archive check are separate.
- iModulonDB is not applicable: these records assert no genes, regulators, pathways or expression modules. Literature mechanisms were not imported as causal graphs.
- Captured working-tree provenance and original assessment start were preserved. Every input hash was rechecked against current bytes and exact Git base 34f65fac61907aa03cf13705201f30da8b963b0a.
- Read-only review: no habitat/source/curation/history/status edits, paid research or GitHub mutation.
- Ignored-inclusive structured archive traversal found no prior structured review for this target; legacy prose is context and no formal finding is closed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T073700Z-crustacean_maxillary_gland-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: crustacean maxillary gland (UBERON:0009964)'
started_at: '2026-10-16T07:13:05Z'
finished_at: '2026-10-16T07:37:00Z'
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
summary: The ITEM grounding correctly identifies a crustacean excretory organ, not
  the mammalian salivary gland reached by the default lexical route. Active UBERON:0009964
  and its excretory-gland genus support the definition. The whole crustacean Excretory
  system is a location/system context, not a strictly broader gland class. Preserve
  the correct identity, gland genus, contextual source alias and two collapsed GOLD
  node IDs; zero organism assertions do not mean the organ cannot host microbes.
source:
  git_revision: 34f65fac61907aa03cf13705201f30da8b963b0a
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
    sha256: c4aeaa9bc04f3704e9e8f69e406990b6d08dd91b1c6afe39aec6a4727ff6612a
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 1f3af4cfd82b31d351ecdce846e5e2d626037d255db63ee869bab5259e12496e
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
  - path: data/habitats/host_associated/crustacean_maxillary_gland.yaml
    sha256: 149aba9521a6302a2f99e96c4264de188909efb12fe9221ed16ce4d250db805a
    role: target
  - path: data/habitats/host_associated/excretory_system__22ee753c.yaml
    sha256: bbf5d8ad1733d9f22bcf1da9fab714a194cde611972cd776fa022657cd50342a
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
- target_id: UBERON:0009964
  path: data/habitats/host_associated/crustacean_maxillary_gland.yaml
  label: crustacean maxillary gland
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
  description: Full field-by-field assessment of this exact generated record.
  selection: One of the next 24 unreviewed records in deterministic path order from
    an ignored-inclusive 3209-record census. This individual report is not proxy coverage
    for other records.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - UBERON:0009964
  exclusions:
  - target: Other records, original individual source specimens, SSSOM/KGX products
    reason: Parents are context only; no extra coverage or export certification is
      claimed.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/crustacean_maxillary_gland.yaml
  exit_code: 0
  target_ids:
  - UBERON:0009964
  summary: "Finished 2026-10-16T07:13:30Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/crustacean_maxillary_gland.yaml"
  scope_note: Individual schema; strict covers the selected 24; history, provenance,
    corpus, causal, term-request and configured label checks are full-corpus. Inputs
    remain unchanged.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/crustacean_maxillary_gland.yaml data/habitats/host_associated/crustacean_post_larval_stage.yaml
    data/habitats/host_associated/cryptomonads_cryptophytes.yaml data/habitats/host_associated/ctenophora.yaml
    data/habitats/host_associated/cud.yaml data/habitats/host_associated/cutaneous_leishmaniasis.yaml
    data/habitats/host_associated/cuticle.yaml data/habitats/host_associated/cuticle__11d6cb22.yaml
    data/habitats/host_associated/cuticle__6c2a3dac.yaml data/habitats/host_associated/cuticle__72f050c4.yaml
    data/habitats/host_associated/cuticle__9784f327.yaml data/habitats/host_associated/cuticle__a024212e.yaml
    data/habitats/host_associated/cv_1_cell.yaml data/habitats/host_associated/cyst.yaml
    data/habitats/host_associated/decayed_wood__afd3403c.yaml data/habitats/host_associated/decomposed_body.yaml
    data/habitats/host_associated/decomposed_body__7ba62861.yaml data/habitats/host_associated/decomposed_body__ee215354.yaml
    data/habitats/host_associated/dental_abscess.yaml data/habitats/host_associated/dental_calculus.yaml
    data/habitats/host_associated/dental_calculus__18e49dca.yaml data/habitats/host_associated/dental_calculus__8a0a99ac.yaml
    data/habitats/host_associated/dental_plaque.yaml data/habitats/host_associated/dental_plaque__384bd6e9.yaml
  exit_code: 0
  target_ids:
  - UBERON:0009964
  summary: "Finished 2026-10-16T07:16:52Z. uv run python scripts/validate_strict.py\
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
  scope_note: Individual schema; strict covers the selected 24; history, provenance,
    corpus, causal, term-request and configured label checks are full-corpus. Inputs
    remain unchanged.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - UBERON:0009964
  summary: 'Finished 2026-10-16T07:17:04Z. No issues found

    836 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict covers the selected 24; history, provenance,
    corpus, causal, term-request and configured label checks are full-corpus. Inputs
    remain unchanged.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - UBERON:0009964
  summary: "Finished 2026-10-16T07:17:05Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict covers the selected 24; history, provenance,
    corpus, causal, term-request and configured label checks are full-corpus. Inputs
    remain unchanged.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - UBERON:0009964
  summary: "Finished 2026-10-16T07:17:30Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict covers the selected 24; history, provenance,
    corpus, causal, term-request and configured label checks are full-corpus. Inputs
    remain unchanged.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - UBERON:0009964
  summary: "Finished 2026-10-16T07:17:36Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict covers the selected 24; history, provenance,
    corpus, causal, term-request and configured label checks are full-corpus. Inputs
    remain unchanged.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - UBERON:0009964
  summary: "Finished 2026-10-16T07:18:01Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict covers the selected 24; history, provenance,
    corpus, causal, term-request and configured label checks are full-corpus. Inputs
    remain unchanged.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - UBERON:0009964
  summary: "Finished 2026-10-16T07:19:10Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict covers the selected 24; history, provenance,
    corpus, causal, term-request and configured label checks are full-corpus. Inputs
    remain unchanged.
- check_id: CCI
  name: Exact-base hosted QC
  status: passed
  required: true
  command: gh run view 38863397429 --repo CultureBotAI/HabitatMech --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - UBERON:0009964
  summary: Verified 2026-10-16T07:18:44Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38863397429
  scope_note: Scientific input base only; these new review bundles were not part of
    that earlier run.
- check_id: CPOOL
  name: Candidate-pool and displayed-entry correspondence
  status: passed
  required: false
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    /private/tmp/habitatmech-review-cs-author.py pool_check
  exit_code: 0
  target_ids:
  - UBERON:0009964
  summary: All 18 displayed candidate pools equal exact source taxon totals.
  scope_note: Supplemental exact source check for all 18 displayed taxon entries;
    not scientific approval of the pair.
- check_id: CREF
  name: Standalone record citation-validator applicability
  status: not_applicable
  required: false
  target_ids:
  - UBERON:0009964
  summary: No standalone citation validator is documented for these generated targets
    without record-level citation blocks. Stable identifiers and source references
    were checked directly; causal validation ran globally.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/crustacean_maxillary_gland.yaml
  locator: Entire generated YAML, including complete history
  accessed_at: '2026-10-16T07:37:00Z'
  support: supports
  summary: Every field read; exact source identity, aliases, parents, assertions and
    taxa assessed.
  snapshot_sha256: 149aba9521a6302a2f99e96c4264de188909efb12fe9221ed16ce4d250db805a
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Host identity, source evidence and strict broader-parent rules
  accessed_at: '2026-10-16T07:37:00Z'
  support: supports
  summary: Host environment, anatomy, whole system, life stage and disease are distinct;
    every parent contribution must be strictly broader.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation, TaxonAssociation and grounding/status semantics
  accessed_at: '2026-10-16T07:37:00Z'
  support: supports
  summary: Source mapping endpoint is the record identifier; source-is-record omits
    a mapping predicate. Counts retain their units and reported association does not
    imply characteristic presence.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed source resolution and exact document regeneration
  accessed_at: '2026-10-16T07:37:00Z'
  support: supports
  summary: '[{"mint": "habitatmech:GOLD.82cc79ac14", "automatic": {"identifier": "habitatmech:GOLD.82cc79ac14",
    "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category":
    null, "reviewed": false, "decision": null}, "final": {"identifier": "UBERON:0009964",
    "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding":
    true, "extra_parents": [], "extra_xrefs": [], "route": "curated_ground_from_gold_unmatched",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.82cc79ac14",
    "decision": "GROUND", "object_id": "UBERON:0009964", "object_label": "crustacean
    maxillary gland", "grounding_status": "EXACT", "curator": "claude-opus-5", "date":
    "2026-08-16", "notes": "Variant-match review (#12): the variant route reaches
    UBERON:0001736 ''submandibular gland'', a mammalian SALIVARY gland. The path is
    Crustaceans > Excretory system, and UBERON has a distinct crustacean maxillary
    gland. Same word, different phylum and different organ system. Path: Host-associated
    > Arthropoda: Crustaceans > Excretory system > Maxillary glands", "review_depth":
    "ITEM", "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego and source projections
  accessed_at: '2026-10-16T07:37:00Z'
  support: supports
  summary: Per-pair maximum score, direct flag and deterministic rank reproduce source
    associations. The compact taxon tables do not retain original pair citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 1769
  accessed_at: '2026-10-16T07:37:00Z'
  support: supports
  summary: '[{"row": 1769, "data": {"canonical_path": "Host-associated > Arthropoda:
    Crustaceans > Excretory system > Maxillary glands", "ecosystem": "Host-associated",
    "ecosystem_category": "Arthropoda: Crustaceans", "ecosystem_type": "Excretory
    system", "ecosystem_subtype": "Maxillary glands", "specific_ecosystem": "", "leaf_label":
    "Maxillary glands", "depth": "4", "gold_node_count": "2", "organism_count": "0",
    "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids":
    "gold.ecosystem:7334|gold.ecosystem:7335"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 11677,11679
  accessed_at: '2026-10-16T07:37:00Z'
  support: supports
  summary: '[{"row": 11677, "data": {"subject": "UBERON:0009962", "predicate": "rdfs:subClassOf",
    "object": "UBERON:0002530"}}, {"row": 11679, "data": {"subject": "UBERON:0009964",
    "predicate": "rdfs:subClassOf", "object": "UBERON:0009962"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 13384,13386
  accessed_at: '2026-10-16T07:37:00Z'
  support: supports
  summary: '[{"row": 13384, "data": {"term_id": "UBERON:0009962", "ontology": "UBERON",
    "label": "excretory gland", "definition": "A gland that discharges its secretion
    through a duct opening on an internal or external surface of the body, as a lacrimal
    gland.", "synonyms": "renal gland", "deprecated": "", "directly_referenced": "FALSE",
    "label_only": "FALSE"}}, {"row": 13386, "data": {"term_id": "UBERON:0009964",
    "ontology": "UBERON", "label": "crustacean maxillary gland", "definition": "Excretory
    organ in maxillary segment with duct opening on maxilla.", "synonyms": "", "deprecated":
    "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET8
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 1677
  accessed_at: '2026-10-16T07:37:00Z'
  support: supports
  summary: '[{"row": 1677, "data": {"identifier": "habitatmech:GOLD.82cc79ac14", "decision":
    "GROUND", "object_id": "UBERON:0009964", "object_label": "crustacean maxillary
    gland", "grounding_status": "EXACT", "curator": "claude-opus-5", "date": "2026-08-16",
    "notes": "Variant-match review (#12): the variant route reaches UBERON:0001736
    ''submandibular gland'', a mammalian SALIVARY gland. The path is Crustaceans >
    Excretory system, and UBERON has a distinct crustacean maxillary gland. Same word,
    different phylum and different organ system. Path: Host-associated > Arthropoda:
    Crustaceans > Excretory system > Maxillary glands", "review_depth": "ITEM", "category":
    "", "relation": ""}}]'
  snapshot_sha256: c4aeaa9bc04f3704e9e8f69e406990b6d08dd91b1c6afe39aec6a4727ff6612a
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/excretory_system__22ee753c.yaml
  locator: Complete immediate parent, context only
  accessed_at: '2026-10-16T07:37:00Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.d0a97e09fe", "label": "Excretory system",
    "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status":
    "SEEDED", "parent_habitats": ["UBERON:8450002", "habitatmech:GOLD.2959225799"],
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:7329",
    "source_label": "Excretory system", "source_path": "Host-associated > Arthropoda:
    Crustaceans > Excretory system", "mapping_predicate": "skos:narrowMatch", "notes":
    "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by GOLD. Grounding: NARROW."}]}'
  snapshot_sha256: bbf5d8ad1733d9f22bcf1da9fab714a194cde611972cd776fa022657cd50342a
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009962/graph
  locator: UBERON_0009962-graph.json
  accessed_at: '2026-10-16T07:15:24Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0009962",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002530", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0009962",
    "target": "http://purl.obolibrary.org/obo/UBERON_8450002", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: c6c0efd94e7888ac556dbac63e70b3297b4a63447feeec0a6ab47e0d0a456bb5
- evidence_id: EX11
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009962
  locator: UBERON_0009962.json
  accessed_at: '2026-10-16T07:15:23Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:0009962", "label": "excretory gland", "is_obsolete": false, "description":
    ["A gland that discharges its secretion through a duct opening on an internal
    or external surface of the body, as a lacrimal gland."], "obo_synonym": [{"name":
    "renal gland", "scope": "hasNarrowSynonym", "type": null, "xrefs": [{"database":
    null, "id": "https://github.com/obophenotype/uberon/issues/1450", "description":
    null, "url": "https://github.com/obophenotype/uberon/issues/1450"}]}], "annotation":
    {"database_cross_reference": ["BTO:0000431"], "editor note": ["TODO - child terms"],
    "id": ["UBERON:0009962"]}}'
  snapshot_sha256: 4ae39de9639ed75821852aac16227fe4bdc13dfd3d191384931755930e73df62
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009964/graph
  locator: UBERON_0009964-graph.json
  accessed_at: '2026-10-16T07:15:26Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0009964",
    "target": "http://purl.obolibrary.org/obo/UBERON_0009962", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0009964",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_197562", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}]'
  snapshot_sha256: 377aa314619966631fb89b839c5957617dd15d3b87e43b0b16ede1eaac0c0196
- evidence_id: EX13
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009964
  locator: UBERON_0009964.json
  accessed_at: '2026-10-16T07:15:25Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:0009964", "label": "crustacean maxillary gland", "is_obsolete": false,
    "description": ["Excretory organ in maxillary segment with duct opening on maxilla."],
    "obo_synonym": null, "annotation": {"editor note": ["cede this term to Arthropod
    AO"], "id": ["UBERON:0009964"], "never in taxon": ["http://purl.obolibrary.org/obo/NCBITaxon_6960"],
    "taxon_notes": ["consider generalizing to include millipedes, centipedes. Function:
    Two different excretory organs are found among crustaceans: the antennal gland
    and the maxillary gland. Both have the same basic structure: an end sac and a
    convoluted duct that may expand into a bladder before opening to the outside.
    In most adult crustaceans only one or the other gland functions. The functional
    gland may change during the life cycle. Terminology note: http://crustacea.nhm.org/glossary/define.html?termID=327
    suggests green gland as the generic term and antennal as the decapoda term"]}}'
  snapshot_sha256: 0c84491a2fae97d92d9b12feb6520ff809ca5f4225701ebce78e8de172a408b7
- evidence_id: EX14
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_8450002/graph
  locator: UBERON_8450002-graph.json
  accessed_at: '2026-10-16T07:15:33Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_8450002",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_8450002",
    "target": "http://purl.obolibrary.org/obo/GO_0046903", "uri": "http://purl.obolibrary.org/obo/RO_0002215",
    "label": "capable of"}]'
  snapshot_sha256: 3d391b91bb62664d77f52107953b5810baa9fd11b3d1233fe3fb6f857234aa42
- evidence_id: EX15
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_8450002
  locator: UBERON_8450002.json
  accessed_at: '2026-10-16T07:15:33Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:8450002", "label": "excretory system", "is_obsolete": false, "description":
    ["An anatomical system that eliminates waste products that arise as a result of
    metabolic activity."], "obo_synonym": null, "annotation": {"created by": ["http://orcid.org/0000-0002-6095-8718"],
    "creation date": ["2022-05-25T18:21:29Z"], "database_cross_reference": ["BTO:0006338"],
    "id": ["UBERON:8450002"]}}'
  snapshot_sha256: a31104b71eb28dd765b8856990eae30a839232f33ca3a79c0b0ab9efff73adfe
- evidence_id: ESEARCH
  kind: search
  reference: Local raw, maintained-input and review corpus
  locator: rg --no-ignore --hidden -l -F -e UBERON:0009964 -e 'crustacean maxillary
    gland' -e crustacean_maxillary_gland -e habitatmech:GOLD.82cc79ac14 curation history
    research reports data/raw build reviews
  accessed_at: '2026-10-16T07:14:45Z'
  support: context_only
  summary: Exact source rows parsed. Broad matching files are leads, not a claim that
    every match was inspected. No formal structured target predecessor found.
  search_scope: curation, history, research, reports, data/raw, build and reviews,
    including hidden and ignored files; structured YAML archive parsed independently
    of gitignore.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, source scope, aliases and parent meanings
  outcome: concern
  summary: The ITEM grounding correctly identifies a crustacean excretory organ, not
    the mammalian salivary gland reached by the default lexical route. Active UBERON:0009964
    and its excretory-gland genus support the definition. The whole crustacean Excretory
    system is a location/system context, not a strictly broader gland class. Preserve
    the correct identity, gland genus, contextual source alias and two collapsed GOLD
    node IDs; zero organism assertions do not mean the organ cannot host microbes.
  target_ids:
  - UBERON:0009964
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - EP9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
- assessment_id: A2
  area: quantity
  topic: Source counts, units, scores, ranks and pool denominators
  outcome: supported
  summary: 'Exact raw rows reproduce every emitted count, unit, rank, score and candidate
    pool. GOLD zero counts are omitted; side-table biosamples, study memberships and
    triads are not added to organism totals. {"assertions": [{"source": "GOLD", "count":
    0, "unit": "ORGANISM", "row": {"row": 1769, "data": {"canonical_path": "Host-associated
    > Arthropoda: Crustaceans > Excretory system > Maxillary glands", "ecosystem":
    "Host-associated", "ecosystem_category": "Arthropoda: Crustaceans", "ecosystem_type":
    "Excretory system", "ecosystem_subtype": "Maxillary glands", "specific_ecosystem":
    "", "leaf_label": "Maxillary glands", "depth": "4", "gold_node_count": "2", "organism_count":
    "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids":
    "gold.ecosystem:7334|gold.ecosystem:7335"}}}], "taxa": []}'
  target_ids:
  - UBERON:0009964
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - EP9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
- assessment_id: A3
  area: evidence
  topic: Source association versus biological localization
  outcome: supported
  summary: The ITEM grounding correctly identifies a crustacean excretory organ, not
    the mammalian salivary gland reached by the default lexical route. Active UBERON:0009964
    and its excretory-gland genus support the definition. The whole crustacean Excretory
    system is a location/system context, not a strictly broader gland class. Preserve
    the correct identity, gland genus, contextual source alias and two collapsed GOLD
    node IDs; zero organism assertions do not mean the organ cannot host microbes.
    The supporting authorities and primary studies have only the scopes stated in
    their evidence entries. Original specimen evidence is not fully reconstructed.
  target_ids:
  - UBERON:0009964
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - EP9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
- assessment_id: A4
  area: completeness
  topic: Native status, source history and optional scientific content
  outcome: supported
  summary: Executed generation reproduces EXACT/REVIEWED. Status truthfully records
    decision depth, not the outcome of this review. No absent optional graph, parameter,
    discussion, dataset or characteristic-presence flag is fabricated. Known scientific
    contradictions are retained above; missing ITEM status alone is not an issue.
  target_ids:
  - UBERON:0009964
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native structural validation and reproduction
  outcome: supported
  summary: 'All 31 baseline commands passed: 24 individual schemas, cohort strict,
    836 histories, provenance, exact 3209-record reproduction, 32 causal overlays,
    110 term requests and configured labels. Exact-base hosted QC passed; none of
    these gates proves scientific support.'
  target_ids:
  - UBERON:0009964
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: crustacean-maxillary-gland-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Source context is not a strictly broader habitat class
  description: 'The ITEM grounding correctly identifies a crustacean excretory organ,
    not the mammalian salivary gland reached by the default lexical route. Active
    UBERON:0009964 and its excretory-gland genus support the definition. The whole
    crustacean Excretory system is a location/system context, not a strictly broader
    gland class. Preserve the correct identity, gland genus, contextual source alias
    and two collapsed GOLD node IDs; zero organism assertions do not mean the organ
    cannot host microbes. Exact context contribution: habitatmech:GOLD.d0a97e09fe.
    Use the guarded GOLD-parent exclusion after source-scope review, retaining independent
    true parents.'
  target_ids:
  - UBERON:0009964
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - EEXTRACT
  - ET5
  - ET6
  - ET7
  - ET8
  - EP9
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
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
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - UBERON:0009964
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  description: 'The ITEM grounding correctly identifies a crustacean excretory organ,
    not the mammalian salivary gland reached by the default lexical route. Active
    UBERON:0009964 and its excretory-gland genus support the definition. The whole
    crustacean Excretory system is a location/system context, not a strictly broader
    gland class. Preserve the correct identity, gland genus, contextual source alias
    and two collapsed GOLD node IDs; zero organism assertions do not mean the organ
    cannot host microbes. Exact context contribution: habitatmech:GOLD.d0a97e09fe.
    Use the guarded GOLD-parent exclusion after source-scope review, retaining independent
    true parents. Proposed work only; no repair or status promotion is performed by
    this review.'
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
- Exact-base hosted QC covers unchanged scientific inputs, not a newly executed local
  full QC or these new output bundles. Native output validation/save and the subsequent
  archive check are separate.
- 'iModulonDB is not applicable: these records assert no genes, regulators, pathways
  or expression modules. Literature mechanisms were not imported as causal graphs.'
notes:
- Captured working-tree provenance and original assessment start were preserved. Every
  input hash was rechecked against current bytes and exact Git base 34f65fac61907aa03cf13705201f30da8b963b0a.
- 'Read-only review: no habitat/source/curation/history/status edits, paid research
  or GitHub mutation.'
- Ignored-inclusive structured archive traversal found no prior structured review
  for this target; legacy prose is context and no formal finding is closed.
tags:
- individual-scientific-review
- host-associated
```
