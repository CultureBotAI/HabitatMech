# Record review: compartment 3 of camelid stomach (habitatmech:GOLD.5f6ed7c41e)

- Review: 20261015T193029Z-c3-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T19:05:37Z
- Finished UTC: 2026-10-15T19:30:29Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The native C3 definition describes the terminal camelid gastric compartment with tubular proximal and differentiated distal regions. Primary dromedary anatomy supports continuity within C3, while regional studies distinguish glandular areas; three-versus-four-compartment nomenclature is not silently universalized. No fixed percentage is imported. The stomach-zone genus is appropriate, but the containing whole mammalian Stomach is not its superclass.

## Scope And Provenance

Full field-by-field scientific assessment of this exact target at a073f8e821a7c095f35501982930cc5a156835c0.

Selection: One of the next 24 path-ordered unreviewed identifiers in an ignored-inclusive 3208-record census. This bundle reviews one identifier, not a sample standing for other targets.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base a073f8e821a7c095f35501982930cc5a156835c0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.5f6ed7c41e | data/habitats/host_associated/c3.yaml | generated | compartment 3 of camelid stomach |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.5f6ed7c41e | Finished 2026-10-15T19:09:26Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/c3.yaml |
| validate-strict | passed | True | habitatmech:GOLD.5f6ed7c41e | Finished 2026-10-15T19:10:07Z. uv run python scripts/validate_strict.py data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.5f6ed7c41e | Finished 2026-10-15T19:10:18Z. No issues found<br>816 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.5f6ed7c41e | Finished 2026-10-15T19:10:19Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.5f6ed7c41e | Finished 2026-10-15T19:10:38Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.5f6ed7c41e | Finished 2026-10-15T19:10:44Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.5f6ed7c41e | Finished 2026-10-15T19:11:04Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.5f6ed7c41e | Finished 2026-10-15T19:12:07Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | habitatmech:GOLD.5f6ed7c41e | Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592 |

## Scientific And Domain Assessments

### Identity, definition, category and broader ancestry

identity: concern. Targets: habitatmech:GOLD.5f6ed7c41e.

The native C3 definition describes the terminal camelid gastric compartment with tubular proximal and differentiated distal regions. Primary dromedary anatomy supports continuity within C3, while regional studies distinguish glandular areas; three-versus-four-compartment nomenclature is not silently universalized. No fixed percentage is imported. The stomach-zone genus is appropriate, but the containing whole mammalian Stomach is not its superclass.

### Source counts, units, ranks, pools and channels

quantity: supported. Targets: habitatmech:GOLD.5f6ed7c41e.

Every attestation and displayed taxon was compared with its exact frozen source row. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Side-table biosamples and study memberships are separate from tree ORGANISM counts; zero-count omission is not biological absence.

### Biological support and limits

evidence: supported. Targets: habitatmech:GOLD.5f6ed7c41e.

The native C3 definition describes the terminal camelid gastric compartment with tubular proximal and differentiated distal regions. Primary dromedary anatomy supports continuity within C3, while regional studies distinguish glandular areas; three-versus-four-compartment nomenclature is not silently universalized. No fixed percentage is imported. The stomach-zone genus is appropriate, but the containing whole mammalian Stomach is not its superclass.

### Curation status, parameters, mechanisms and optional content

completeness: supported. Targets: habitatmech:GOLD.5f6ed7c41e.

Executed routes reproduce UNGROUNDED/REVIEWED. No target environmental parameters, causal edges, discussions/datasets or is_characteristic=true assertions are present. Parent-record mechanisms are not inherited. Optional absence and SEEDED status alone are not defects.

### Native deterministic gates

schema: supported. Targets: habitatmech:GOLD.5f6ed7c41e.

Ordinary and strict schema, 816 curation histories, provenance, exact 3208-record reproduction, 32 causal overlays, term requests, configured labels and exact-base QC passed. Deterministic fidelity does not establish biological correctness.

## Findings

### F1: GOLD context is not a broader habitat class

major / open / confirmed; issue key: c3-context-parent.

Exclude only the exact source-path/expected-parent contribution habitatmech:GOLD.d3869ad37f. The native C3 definition describes the terminal camelid gastric compartment with tubular proximal and differentiated distal regions. Primary dromedary anatomy supports continuity within C3, while regional studies distinguish glandular areas; three-versus-four-compartment nomenclature is not silently universalized. No fixed percentage is imported. The stomach-zone genus is appropriate, but the containing whole mammalian Stomach is not its superclass. Preserve independent valid ontology genera and raw provenance.

## Recommended Actions And Acceptance Checks

### ACT1

Exclude only the exact source-path/expected-parent contribution habitatmech:GOLD.d3869ad37f. The native C3 definition describes the terminal camelid gastric compartment with tubular proximal and differentiated distal regions. Primary dromedary anatomy supports continuity within C3, while regional studies distinguish glandular areas; three-versus-four-compartment nomenclature is not silently universalized. No fixed percentage is imported. The stomach-zone genus is appropriate, but the containing whole mammalian Stomach is not its superclass. Preserve independent valid ontology genera and raw provenance. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identities, source totals/units and raw provenance. Change mapping or native status only when separately supported by the item assessment; never alter source counts by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/c3.yaml; Entire target YAML | supports | All fields, displayed taxa and complete curation history read. |
| ERULE | docs/CURATION.md; Identity, hierarchy and source-evidence rules | supports | All parent contributions must be strictly broader; host identity is not environment identity. Source occurrences are not automatically characteristic. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation and category enums | supports | Source-to-record mapping endpoints; reported associations versus characteristic assertions; category scope and optional fields. |
| ESEED | src/habitatmech/seed.py; Executed resolution routes, parent accumulation, prefix category and overrides | supports | Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:GOLD.5f6ed7c41e", "automatic": {"identifier": "UBERON:0002960", "grounding_status": "CLOSE", "mapping_predicate": "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_synonym", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.5f6ed7c41e", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_leaf_synonym", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.5f6ed7c41e", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-14", "notes": "Disjoint-grounding review (#62): was UBERON:0002960 'central oculomotor nucleus', a brainstem structure. Same as C2 \u2014 the path is Digestive system &gt; Stomach &gt; C3, a camelid stomach compartment. Path: Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; C3", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Inventory projection | supports | Counts/units and taxon ranks/scores preserve source meanings. PREGO projections omit original pair-level citation links. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 2028 | supports | [{"row": 2028, "data": {"canonical_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; C3", "ecosystem": "Host-associated", "ecosystem_category": "Mammals", "ecosystem_type": "Digestive system", "ecosystem_subtype": "Stomach", "specific_ecosystem": "C3", "leaf_label": "C3", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:6701"}}] |
| ET6 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 11674,11675 | supports | [{"row": 11674, "data": {"subject": "UBERON:0009870", "predicate": "rdfs:subClassOf", "object": "UBERON:0004921"}}, {"row": 11675, "data": {"subject": "UBERON:0009870", "predicate": "rdfs:subClassOf", "object": "UBERON:0034944"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 13382 | supports | [{"row": 13382, "data": {"term_id": "UBERON:0009870", "ontology": "UBERON", "label": "zone of stomach", "definition": "A division of the stomach. The stomach can be divided based on mucosal histology (glandular epithelium and gastric glands) and the relative position and type of gastric gland.", "synonyms": "gastric zone&#124;region of stomach&#124;section of stomach", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| ET8 | curation/term_requests.tsv; Physical TSV rows 91 | supports | [{"row": 91, "data": {"identifier": "habitatmech:GOLD.5f6ed7c41e", "requested_label": "compartment 3 of camelid stomach", "parent_class": "UBERON:0009870", "parent_label": "zone of stomach", "definition": "A zone of stomach which is the third and terminal compartment of the camelid stomach and comprises a tubiform proximal region followed by a short distal acid-secreting region.", "exact_synonym": "", "curator": "codex-gpt-5", "date": "2026-09-10", "notes": "Definition authored from the record's committed deep-research report under research/habitats/, read in full; no new paid research was commissioned. GOLD's Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; C3 source denotes compartment 3 of the camelid stomach rather than central oculomotor nucleus, complement component C3, C3 photosynthesis or C3 plants, the ruminant abomasum or omasum, or a separate C4 compartment. The definition says short distal acid-secreting region without assigning a fraction because the report found disagreement on the exact proximal-distal split. UBERON:0009870 'zone of stomach' is the tightest vendored genus because UBERON lacks a generic stomach-compartment class and all candidate ruminant stomach compartments assert the wrong Ruminantia clade. ADD preserves GOLD's source-derived Stomach parent while adding the neutral stomach-division genus.", "parent_mode": "ADD"}}] |
| ET9 | curation/decisions.tsv; Physical TSV rows 1595 | supports | [{"row": 1595, "data": {"identifier": "habitatmech:GOLD.5f6ed7c41e", "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-14", "notes": "Disjoint-grounding review (#62): was UBERON:0002960 'central oculomotor nucleus', a brainstem structure. Same as C2 \u2014 the path is Digestive system &gt; Stomach &gt; C3, a camelid stomach compartment. Path: Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach &gt; C3", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP10 | data/habitats/host_associated/stomach__0260a3a9.yaml; Entire immediate parent record; context only | supports | {"identifier": "habitatmech:GOLD.d3869ad37f", "label": "Stomach", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000945", "habitatmech:GOLD.c8e85f3c84"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:3664", "source_label": "Stomach", "source_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Stomach", "mapping_predicate": "skos:narrowMatch", "assertion_count": 20, "assertion_unit": "ORGANISM", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}]} |
| ERESEARCH | research/habitats/host_associated/c3-habitatmech-gold-5f6ed7c41e-deep-research-claude_code.md; Entire research report; leads checked against adopted claims | supports | Whole report inspected. Competing three/four-compartment conventions and different distal proportions are retained as uncertainty; the native definition does not assert a numeric fraction. The report itself recognizes whole-Stomach part-of versus is-a. |
| EX1 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11139325/fullTextXML; PMC11139325.xml | context_only | Primary sample-collection methods, PMID:38814894, DOI:10.1371/journal.pone.0300316. Mucus from six distinct glandular regions in five Bactrian camels was sampled after slaughter. Supports regional sampling and noninterchangeability of sites; questionable taxonomic wording in the discussion and mechanistic claims are not adopted. |
| EX2 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13417070/fullTextXML; PMC13417070.xml | context_only | Primary abstract, gross-anatomy results and discussion, PMID:42514640, DOI:10.3390/vetsci13070630. Dromedary C2 is smallest, chambered, partly continuous with C1 and communicating with C3; C3 tubular/distal regions remain continuous. The paper discusses competing compartment interpretations. No numerical gland fraction or universal homology is imported. |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000945/graph; UBERON_0000945-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000945", "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945", "target": "http://purl.obolibrary.org/obo/UBERON_0010039", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945", "target": "http://purl.obolibrary.org/obo/GO_0001696", "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945", "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945", "target": "http://purl.obolibrary.org/obo/NCBITaxon_7776", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945", "target": "http://purl.obolibrary.org/obo/UBERON_0001007", "uri": "http://purl.obolibrary.org/obo/RO_0002433", "label": "contributes to morphology of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945", "target": "http://purl.obolibrary.org/obo/UBERON_0001041", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000945; UBERON_0000945.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "UBERON:0000945", "label": "stomach", "is_obsolete": false, "description": ["An expanded region of the vertebrate alimentary tract that serves as a food storage compartment and digestive organ. A stomach is lined, in whole or in part by a glandular epithelium."]} |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009870/graph; UBERON_0009870-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0009870", "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0009870", "target": "http://purl.obolibrary.org/obo/UBERON_0034944", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0009870", "target": "http://purl.obolibrary.org/obo/UBERON_0000945", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009870; UBERON_0009870.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "UBERON:0009870", "label": "zone of stomach", "is_obsolete": false, "description": ["A division of the stomach. The stomach can be divided based on mucosal histology (glandular epithelium and gastric glands) and the relative position and type of gastric gland."]} |
| EX7 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1002/ar.24588&amp;format=json&amp;resultType=core&amp;pageSize=10; paper-camel.json | context_only | Primary abstract PMID:33480155, DOI:10.1002/ar.24588. Alpaca dissections distinguish three compartments from regional saccules. The structured endpoint supplies only the abstract. |
| EWEB | https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.24588; Introduction 1.1-1.2; Results 3.1-3.2 | supports | Full-text publisher page inspected through web. Direct dissection describes tubular C3 with differentiated distal mucosa; the introduction summarizes distal acid secretion from earlier physiology. This is not a new acid-secretion experiment. |
| ESEARCH | Maintained inputs and local structured archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.5f6ed7c41e -e 'compartment 3 of camelid stomach' -e c3 -e habitatmech:GOLD.5f6ed7c41e curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately. No formal target predecessor was found; not every broad label match was inspected. |

## Limits And Additional Notes

- Original specimens and every pair-level source citation have not been independently reidentified. Source counts and ranks are not prevalence, viability, or characteristic presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities were separately checked against current NCBI Taxonomy, not certified by that label gate.
- Full QC evidence is a successful remote run at the exact unchanged scientific input base, not a new local full-QC execution. New review files require a post-save native archive check.
- iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic module or causal mechanism is asserted. No paid research was used.
- Current input hashes were checked against both working bytes and exact tracked base blobs; source.state git_commit explicitly describes that revision.
- Ignored-inclusive searches and the parsed structured archive found no previous structured observation targeting this identifier. Broad label matches are leads, not formal lineage or automatic scientific findings.
- Read-only scientific review: no habitat curation, generation, history/status promotion or GitHub mutation is performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T193029Z-c3-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: compartment 3 of camelid stomach (habitatmech:GOLD.5f6ed7c41e)'
started_at: '2026-10-15T19:05:37Z'
finished_at: '2026-10-15T19:30:29Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the record and sources; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The native C3 definition describes the terminal camelid gastric compartment
  with tubular proximal and differentiated distal regions. Primary dromedary anatomy
  supports continuity within C3, while regional studies distinguish glandular areas;
  three-versus-four-compartment nomenclature is not silently universalized. No fixed
  percentage is imported. The stomach-zone genus is appropriate, but the containing
  whole mammalian Stomach is not its superclass.
source:
  git_revision: a073f8e821a7c095f35501982930cc5a156835c0
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
    sha256: 196d393819145d33f30f7706fd9c5369ed05847d2ccbd9b977a759556ca293fd
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 9344f0bbbad1423ff0e47204ad49bc27ffaf4b5e63841e77e09cc01877b91f54
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: da5dcc7d49a3441bd9ff25d95ff204ba4e8716cf062271338ee2795ca16a5ce4
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
  - path: data/habitats/host_associated/c3.yaml
    sha256: 2f42a2495dda67cba632021b458cbc1d49973615e6312c633a377bdc4c248424
    role: target
  - path: data/habitats/host_associated/stomach__0260a3a9.yaml
    sha256: 112f083fc13038eb46b4cefe6b7a668ec9ef29b6023d17d77b07a8eb97911bf4
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
  - path: history/mappings/c3/2026-09-11T054749Z-codex-gpt-5-f1d7de.yaml
    sha256: 8441f6cb4fba792b896c9d8e388abea2d7d53c60c7faf347e405948f67ffbf9e
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: research/habitats/host_associated/c3-habitatmech-gold-5f6ed7c41e-deep-research-claude_code.md
    sha256: dbb07b5ea68d728c2ec1ea9b04a58acd0ca88502b701ff40371c90fb4c762f55
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
- target_id: habitatmech:GOLD.5f6ed7c41e
  path: data/habitats/host_associated/c3.yaml
  label: compartment 3 of camelid stomach
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
  description: Full field-by-field scientific assessment of this exact target at a073f8e821a7c095f35501982930cc5a156835c0.
  selection: One of the next 24 path-ordered unreviewed identifiers in an ignored-inclusive
    3208-record census. This bundle reviews one identifier, not a sample standing
    for other targets.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  exclusions:
  - target: Other habitats and SSSOM/KGX products
    reason: Parent context is not additional record coverage. Export conformance and
      original individual specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/c3.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  summary: "Finished 2026-10-15T19:09:26Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/c3.yaml"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml
    data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml
    data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml
    data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml
    data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml
    data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml
    data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml
    data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml
    data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml
    data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml
    data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml
    data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  summary: "Finished 2026-10-15T19:10:07Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml\
    \ data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml\
    \ data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml\
    \ data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml\
    \ data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml\
    \ data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml\
    \ data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml\
    \ data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml\
    \ data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml\
    \ data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml\
    \ data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml\
    \ data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  summary: 'Finished 2026-10-15T19:10:18Z. No issues found

    816 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  summary: "Finished 2026-10-15T19:10:19Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  summary: "Finished 2026-10-15T19:10:38Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  summary: "Finished 2026-10-15T19:10:44Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  summary: "Finished 2026-10-15T19:11:04Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  summary: "Finished 2026-10-15T19:12:07Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: CCI
  name: Exact-baseline full QC
  status: passed
  required: true
  command: gh run view 38786529592 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  summary: Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592
  scope_note: Unchanged scientific input baseline; these new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/c3.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: All fields, displayed taxa and complete curation history read.
  snapshot_sha256: 2f42a2495dda67cba632021b458cbc1d49973615e6312c633a377bdc4c248424
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, hierarchy and source-evidence rules
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: All parent contributions must be strictly broader; host identity is not
    environment identity. Source occurrences are not automatically characteristic.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation and category enums
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: Source-to-record mapping endpoints; reported associations versus characteristic
    assertions; category scope and optional fields.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed resolution routes, parent accumulation, prefix category and overrides
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: 'Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:GOLD.5f6ed7c41e",
    "automatic": {"identifier": "UBERON:0002960", "grounding_status": "CLOSE", "mapping_predicate":
    "skos:closeMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs":
    [], "route": "gold_leaf_synonym", "category": null, "reviewed": false, "decision":
    null}, "final": {"identifier": "habitatmech:GOLD.5f6ed7c41e", "grounding_status":
    "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_leaf_synonym",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.5f6ed7c41e",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-14", "notes": "Disjoint-grounding
    review (#62): was UBERON:0002960 ''central oculomotor nucleus'', a brainstem structure.
    Same as C2 \u2014 the path is Digestive system > Stomach > C3, a camelid stomach
    compartment. Path: Host-associated > Mammals > Digestive system > Stomach > C3",
    "review_depth": "ITEM", "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Inventory projection
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: Counts/units and taxon ranks/scores preserve source meanings. PREGO projections
    omit original pair-level citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 2028
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: '[{"row": 2028, "data": {"canonical_path": "Host-associated > Mammals >
    Digestive system > Stomach > C3", "ecosystem": "Host-associated", "ecosystem_category":
    "Mammals", "ecosystem_type": "Digestive system", "ecosystem_subtype": "Stomach",
    "specific_ecosystem": "C3", "leaf_label": "C3", "depth": "5", "gold_node_count":
    "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions":
    "0", "gold_node_ids": "gold.ecosystem:6701"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 11674,11675
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: '[{"row": 11674, "data": {"subject": "UBERON:0009870", "predicate": "rdfs:subClassOf",
    "object": "UBERON:0004921"}}, {"row": 11675, "data": {"subject": "UBERON:0009870",
    "predicate": "rdfs:subClassOf", "object": "UBERON:0034944"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 13382
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: '[{"row": 13382, "data": {"term_id": "UBERON:0009870", "ontology": "UBERON",
    "label": "zone of stomach", "definition": "A division of the stomach. The stomach
    can be divided based on mucosal histology (glandular epithelium and gastric glands)
    and the relative position and type of gastric gland.", "synonyms": "gastric zone|region
    of stomach|section of stomach", "deprecated": "", "directly_referenced": "FALSE",
    "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET8
  kind: database
  reference: curation/term_requests.tsv
  locator: Physical TSV rows 91
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: '[{"row": 91, "data": {"identifier": "habitatmech:GOLD.5f6ed7c41e", "requested_label":
    "compartment 3 of camelid stomach", "parent_class": "UBERON:0009870", "parent_label":
    "zone of stomach", "definition": "A zone of stomach which is the third and terminal
    compartment of the camelid stomach and comprises a tubiform proximal region followed
    by a short distal acid-secreting region.", "exact_synonym": "", "curator": "codex-gpt-5",
    "date": "2026-09-10", "notes": "Definition authored from the record''s committed
    deep-research report under research/habitats/, read in full; no new paid research
    was commissioned. GOLD''s Host-associated > Mammals > Digestive system > Stomach
    > C3 source denotes compartment 3 of the camelid stomach rather than central oculomotor
    nucleus, complement component C3, C3 photosynthesis or C3 plants, the ruminant
    abomasum or omasum, or a separate C4 compartment. The definition says short distal
    acid-secreting region without assigning a fraction because the report found disagreement
    on the exact proximal-distal split. UBERON:0009870 ''zone of stomach'' is the
    tightest vendored genus because UBERON lacks a generic stomach-compartment class
    and all candidate ruminant stomach compartments assert the wrong Ruminantia clade.
    ADD preserves GOLD''s source-derived Stomach parent while adding the neutral stomach-division
    genus.", "parent_mode": "ADD"}}]'
  snapshot_sha256: da5dcc7d49a3441bd9ff25d95ff204ba4e8716cf062271338ee2795ca16a5ce4
- evidence_id: ET9
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 1595
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: '[{"row": 1595, "data": {"identifier": "habitatmech:GOLD.5f6ed7c41e", "decision":
    "CONFIRM_UNGROUNDED", "object_id": "", "object_label": "", "grounding_status":
    "", "curator": "claude-opus-5", "date": "2026-08-14", "notes": "Disjoint-grounding
    review (#62): was UBERON:0002960 ''central oculomotor nucleus'', a brainstem structure.
    Same as C2 \u2014 the path is Digestive system > Stomach > C3, a camelid stomach
    compartment. Path: Host-associated > Mammals > Digestive system > Stomach > C3",
    "review_depth": "ITEM", "category": "", "relation": ""}}]'
  snapshot_sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
- evidence_id: EP10
  kind: record_content
  reference: data/habitats/host_associated/stomach__0260a3a9.yaml
  locator: Entire immediate parent record; context only
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.d3869ad37f", "label": "Stomach", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats":
    ["UBERON:0000945", "habitatmech:GOLD.c8e85f3c84"], "source_attestations": [{"source":
    "GOLD", "source_id": "gold.ecosystem:3664", "source_label": "Stomach", "source_path":
    "Host-associated > Mammals > Digestive system > Stomach", "mapping_predicate":
    "skos:narrowMatch", "assertion_count": 20, "assertion_unit": "ORGANISM", "notes":
    "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by GOLD. Grounding: NARROW."}]}'
  snapshot_sha256: 112f083fc13038eb46b4cefe6b7a668ec9ef29b6023d17d77b07a8eb97911bf4
- evidence_id: ERESEARCH
  kind: record_content
  reference: research/habitats/host_associated/c3-habitatmech-gold-5f6ed7c41e-deep-research-claude_code.md
  locator: Entire research report; leads checked against adopted claims
  accessed_at: '2026-10-15T19:30:28Z'
  support: supports
  summary: Whole report inspected. Competing three/four-compartment conventions and
    different distal proportions are retained as uncertainty; the native definition
    does not assert a numeric fraction. The report itself recognizes whole-Stomach
    part-of versus is-a.
  snapshot_sha256: dbb07b5ea68d728c2ec1ea9b04a58acd0ca88502b701ff40371c90fb4c762f55
- evidence_id: EX1
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11139325/fullTextXML
  locator: PMC11139325.xml
  accessed_at: '2026-10-15T19:19:53Z'
  support: context_only
  summary: Primary sample-collection methods, PMID:38814894, DOI:10.1371/journal.pone.0300316.
    Mucus from six distinct glandular regions in five Bactrian camels was sampled
    after slaughter. Supports regional sampling and noninterchangeability of sites;
    questionable taxonomic wording in the discussion and mechanistic claims are not
    adopted.
  snapshot_sha256: cc8fa4f55e064cb83602aa2c954fa86b6c31af87a4728cd918a9d397fef12012
- evidence_id: EX2
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13417070/fullTextXML
  locator: PMC13417070.xml
  accessed_at: '2026-10-15T19:19:04Z'
  support: context_only
  summary: Primary abstract, gross-anatomy results and discussion, PMID:42514640,
    DOI:10.3390/vetsci13070630. Dromedary C2 is smallest, chambered, partly continuous
    with C1 and communicating with C3; C3 tubular/distal regions remain continuous.
    The paper discusses competing compartment interpretations. No numerical gland
    fraction or universal homology is imported.
  snapshot_sha256: 54f6a776d1718da6aab3e7d878d7355d2d30eb2c8054e8884eea8942d0a70787
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000945/graph
  locator: UBERON_0000945-graph.json
  accessed_at: '2026-10-15T19:06:24Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000945",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945",
    "target": "http://purl.obolibrary.org/obo/UBERON_0010039", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945",
    "target": "http://purl.obolibrary.org/obo/GO_0001696", "uri": "http://purl.obolibrary.org/obo/RO_0002215",
    "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_7776", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001007", "uri": "http://purl.obolibrary.org/obo/RO_0002433",
    "label": "contributes to morphology of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000945",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001041", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 49334cf579a69dbcf02328fd1ea2b6bae7a15280345490be2655748c794f46fb
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000945
  locator: UBERON_0000945.json
  accessed_at: '2026-10-15T19:06:24Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "UBERON:0000945", "label": "stomach", "is_obsolete": false, "description": ["An
    expanded region of the vertebrate alimentary tract that serves as a food storage
    compartment and digestive organ. A stomach is lined, in whole or in part by a
    glandular epithelium."]}'
  snapshot_sha256: 201440780f903004f89b8f2fe0dc4a31d3d69e8b2d68f43e8c2677bd442ee041
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009870/graph
  locator: UBERON_0009870-graph.json
  accessed_at: '2026-10-15T19:06:38Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0009870",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0009870",
    "target": "http://purl.obolibrary.org/obo/UBERON_0034944", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0009870",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000945", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 6da2509d311de1819a649752d8b0c5f16eaf18510fbe4e0454b16b68240cd27b
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009870
  locator: UBERON_0009870.json
  accessed_at: '2026-10-15T19:06:37Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "UBERON:0009870", "label": "zone of stomach", "is_obsolete": false, "description":
    ["A division of the stomach. The stomach can be divided based on mucosal histology
    (glandular epithelium and gastric glands) and the relative position and type of
    gastric gland."]}'
  snapshot_sha256: 1a4c6629ca4bd302614fe0200bab34621d638605bdef5780c52e56d7d0b205cb
- evidence_id: EX7
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1002/ar.24588&format=json&resultType=core&pageSize=10
  locator: paper-camel.json
  accessed_at: '2026-10-15T19:19:12Z'
  support: context_only
  summary: Primary abstract PMID:33480155, DOI:10.1002/ar.24588. Alpaca dissections
    distinguish three compartments from regional saccules. The structured endpoint
    supplies only the abstract.
  snapshot_sha256: 1849c42f1433d959a88a705077e21a277207e2bec1c001eca0d37088350570a4
- evidence_id: EWEB
  kind: primary_source
  reference: https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.24588
  locator: Introduction 1.1-1.2; Results 3.1-3.2
  accessed_at: '2026-10-15T19:25:11Z'
  support: supports
  summary: Full-text publisher page inspected through web. Direct dissection describes
    tubular C3 with differentiated distal mucosa; the introduction summarizes distal
    acid secretion from earlier physiology. This is not a new acid-secretion experiment.
- evidence_id: ESEARCH
  kind: search
  reference: Maintained inputs and local structured archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.5f6ed7c41e -e 'compartment
    3 of camelid stomach' -e c3 -e habitatmech:GOLD.5f6ed7c41e curation history research
    reports data/raw build reviews
  accessed_at: '2026-10-15T19:05:55Z'
  support: context_only
  summary: Exact source/curation rows were parsed separately. No formal target predecessor
    was found; not every broad label match was inspected.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    ignored and hidden files included; every structured review.yaml was parsed.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, category and broader ancestry
  outcome: concern
  summary: The native C3 definition describes the terminal camelid gastric compartment
    with tubular proximal and differentiated distal regions. Primary dromedary anatomy
    supports continuity within C3, while regional studies distinguish glandular areas;
    three-versus-four-compartment nomenclature is not silently universalized. No fixed
    percentage is imported. The stomach-zone genus is appropriate, but the containing
    whole mammalian Stomach is not its superclass.
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EWEB
  dimensions:
  - name: native_status
    value: UNGROUNDED/REVIEWED
    definition: Generated grounding and curation status; distinct from this scientific
      review verdict.
    evidence_ids:
    - E1
    - ESEED
- assessment_id: A2
  area: quantity
  topic: Source counts, units, ranks, pools and channels
  outcome: supported
  summary: 'Every attestation and displayed taxon was compared with its exact frozen
    source row. [{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]. Side-table biosamples
    and study memberships are separate from tree ORGANISM counts; zero-count omission
    is not biological absence.'
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EWEB
  dimensions:
  - name: source_assertion_units
    value: '[{"source": "GOLD", "count": 0, "unit": "ORGANISM"}]'
    definition: Frozen source counts with their noninterchangeable units; omitted
      zero GOLD counts are verified in the raw row.
    evidence_ids:
    - E1
    - EEXTRACT
    - ESEED
- assessment_id: A3
  area: evidence
  topic: Biological support and limits
  outcome: supported
  summary: The native C3 definition describes the terminal camelid gastric compartment
    with tubular proximal and differentiated distal regions. Primary dromedary anatomy
    supports continuity within C3, while regional studies distinguish glandular areas;
    three-versus-four-compartment nomenclature is not silently universalized. No fixed
    percentage is imported. The stomach-zone genus is appropriate, but the containing
    whole mammalian Stomach is not its superclass.
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EWEB
  - ERESEARCH
- assessment_id: A4
  area: completeness
  topic: Curation status, parameters, mechanisms and optional content
  outcome: supported
  summary: Executed routes reproduce UNGROUNDED/REVIEWED. No target environmental
    parameters, causal edges, discussions/datasets or is_characteristic=true assertions
    are present. Parent-record mechanisms are not inherited. Optional absence and
    SEEDED status alone are not defects.
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  evidence_ids:
  - E1
  - ERULE
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native deterministic gates
  outcome: supported
  summary: Ordinary and strict schema, 816 curation histories, provenance, exact 3208-record
    reproduction, 32 causal overlays, term requests, configured labels and exact-base
    QC passed. Deterministic fidelity does not establish biological correctness.
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: c3-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: GOLD context is not a broader habitat class
  description: Exclude only the exact source-path/expected-parent contribution habitatmech:GOLD.d3869ad37f.
    The native C3 definition describes the terminal camelid gastric compartment with
    tubular proximal and differentiated distal regions. Primary dromedary anatomy
    supports continuity within C3, while regional studies distinguish glandular areas;
    three-versus-four-compartment nomenclature is not silently universalized. No fixed
    percentage is imported. The stomach-zone genus is appropriate, but the containing
    whole mammalian Stomach is not its superclass. Preserve independent valid ontology
    genera and raw provenance.
  target_ids:
  - habitatmech:GOLD.5f6ed7c41e
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
  - ET9
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EWEB
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
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
  - habitatmech:GOLD.5f6ed7c41e
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Exclude only the exact source-path/expected-parent contribution habitatmech:GOLD.d3869ad37f.
    The native C3 definition describes the terminal camelid gastric compartment with
    tubular proximal and differentiated distal regions. Primary dromedary anatomy
    supports continuity within C3, while regional studies distinguish glandular areas;
    three-versus-four-compartment nomenclature is not silently universalized. No fixed
    percentage is imported. The stomach-zone genus is appropriate, but the containing
    whole mammalian Stomach is not its superclass. Preserve independent valid ontology
    genera and raw provenance. No repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independent identities, source totals/units
    and raw provenance. Change mapping or native status only when separately supported
    by the item assessment; never alter source counts by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Original specimens and every pair-level source citation have not been independently
  reidentified. Source counts and ranks are not prevalence, viability, or characteristic
  presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities
  were separately checked against current NCBI Taxonomy, not certified by that label
  gate.
- Full QC evidence is a successful remote run at the exact unchanged scientific input
  base, not a new local full-QC execution. New review files require a post-save native
  archive check.
- 'iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic
  module or causal mechanism is asserted. No paid research was used.'
notes:
- Current input hashes were checked against both working bytes and exact tracked base
  blobs; source.state git_commit explicitly describes that revision.
- Ignored-inclusive searches and the parsed structured archive found no previous structured
  observation targeting this identifier. Broad label matches are leads, not formal
  lineage or automatic scientific findings.
- 'Read-only scientific review: no habitat curation, generation, history/status promotion
  or GitHub mutation is performed.'
tags:
- individual-scientific-review
- host-associated
```
