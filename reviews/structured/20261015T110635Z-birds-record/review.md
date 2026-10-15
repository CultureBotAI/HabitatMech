# Record review: bird-associated environment (habitatmech:GOLD.47e603cf4f)

- Review: 20261015T110635Z-birds-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T10:50:51Z
- Finished UTC: 2026-10-15T11:06:35Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The bird-associated environmental definition and organism/animal-associated genera are coherent. The authored exact alias Birds names the whole host category rather than its environment. Preserve the 1,848 source ORGANISM assertions and verbatim source label.

## Scope And Provenance

Scientific assessment of one exact target at captured revision 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87.

Selection: Next twenty unreviewed records in corpus path order; this document assesses one resolved identifier.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.47e603cf4f | data/habitats/host_associated/birds.yaml | generated | bird-associated environment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.47e603cf4f | Completed 2026-10-15T10:51:36Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/birds.yaml |
| validate-strict | passed | True | habitatmech:GOLD.47e603cf4f | Completed 2026-10-15T10:52:03Z. uv run python scripts/validate_strict.py data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.47e603cf4f | Completed 2026-10-15T10:52:45Z. No issues found<br>789 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.47e603cf4f | Completed 2026-10-15T10:52:46Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.47e603cf4f | Completed 2026-10-15T10:53:13Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.47e603cf4f | Completed 2026-10-15T10:53:20Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.47e603cf4f | Completed 2026-10-15T10:53:50Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.47e603cf4f | Completed 2026-10-15T10:55:12Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Baseline full native QC | passed | True | habitatmech:GOLD.47e603cf4f | Exact-revision full QC and structured review contract succeeded; verified 2026-10-15T11:05:49Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38722329263 |

## Scientific And Domain Assessments

### Native validity and reproduction

schema: supported. Targets: habitatmech:GOLD.47e603cf4f.

Individual schema, twenty-target strict validation, 789 history records, 14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110 term requests passed. These are deterministic rather than scientific certification.

### Identity, hierarchy and alias scope

identity: concern. Targets: habitatmech:GOLD.47e603cf4f.

The bird-associated environmental definition and organism/animal-associated genera are coherent. The authored exact alias Birds names the whole host category rather than its environment. Preserve the 1,848 source ORGANISM assertions and verbatim source label.

### Counts, units and ranking

quantity: supported. Targets: habitatmech:GOLD.47e603cf4f.

Exact source rows reproduce [{"source": "GOLD", "count": 1848, "unit": "ORGANISM"}]. All 0 retained taxon IDs were resolved against current NCBI identities, including the explicit alias noted for bile. Zero-count omissions are not biological absence; unlike counts are not summed.

### Native status and optional assertions

completeness: supported. Targets: habitatmech:GOLD.47e603cf4f.

Executed routes reproduce UNGROUNDED/REVIEWED. No causal or characteristic-presence claim is asserted; missing optional fields are not automatic deficiencies.

## Findings

### F1: Whole-host name is asserted as an exact environment synonym

major / open / confirmed; issue key: birds-host-name-exact-synonym.

Remove the authored exact host alias 'Birds' from its term_requests.tsv row and guard automatic old-label fallback in definition_source_label_exclusions.tsv. Keep the verbatim attestation, minted identity, environmental definition, genuine genera and source counts.

## Recommended Actions And Acceptance Checks

### ACT1

Remove the authored exact host alias 'Birds' from its term_requests.tsv row and guard automatic old-label fallback in definition_source_label_exclusions.tsv. Keep the verbatim attestation, minted identity, environmental definition, genuine genera and source counts. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/birds.yaml; Entire YAML | supports | Complete target read, including source paths, fields, taxa and history. |
| ERULE | docs/CURATION.md; Habitat identity, strictly broader parents and owner boundaries | supports | Whole hosts differ from associated environments; context and part-of links must not be asserted as broader habitat classes. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon | supports | Mapping endpoints, broader parents and reported versus characteristic presence are distinct. |
| ESEED | src/habitatmech/seed.py; Executed native routes | supports | Resolution results: [{"source": "GOLD", "mint": "habitatmech:GOLD.47e603cf4f", "automatic": {"identifier": "habitatmech:GOLD.47e603cf4f", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_unmatched", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.47e603cf4f", "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": ["ENVO:01001002"], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_unmatched", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.47e603cf4f", "decision": "CONFIRM_UNGROUNDED", "object_id": "ENVO:01001002", "object_label": "animal-associated environment", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Birds as host. Parented to animal-associated environment; not grounded there because every host clade would merge onto one record. ENVO term request.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; extract_prego | supports | Distinct pairs, maximum scores/channels, score/directness/ID ordering and full taxon pool are retained; original pair citations are not emitted. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; TSV physical rows 25 | supports | [{"row": 25, "data": {"canonical_path": "Host-associated &gt; Birds", "ecosystem": "Host-associated", "ecosystem_category": "Birds", "ecosystem_type": "", "ecosystem_subtype": "", "specific_ecosystem": "", "leaf_label": "Birds", "depth": "2", "gold_node_count": "4", "organism_count": "1848", "study_count": "0", "biosample_count": "0", "total_assertions": "1848", "gold_node_ids": "gold.ecosystem:3382&#124;gold.ecosystem:3599&#124;gold.ecosystem:3714&#124;gold.ecosystem:4154"}}] |
| ET6 | data/raw/ontology_subclass_edges.tsv; TSV physical rows 6795,6797 | supports | [{"row": 6795, "data": {"subject": "ENVO:01001000", "predicate": "rdfs:subClassOf", "object": "ENVO:01000254"}}, {"row": 6797, "data": {"subject": "ENVO:01001002", "predicate": "rdfs:subClassOf", "object": "ENVO:01001000"}}] |
| ET7 | data/raw/ontology_terms.tsv; TSV physical rows 8489,8491 | supports | [{"row": 8489, "data": {"term_id": "ENVO:01001000", "ontology": "ENVO", "label": "environmental system determined by an organism", "definition": "An environmental system which is determined by a living organism.", "synonyms": "host-associated environment", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row": 8491, "data": {"term_id": "ENVO:01001002", "ontology": "ENVO", "label": "animal-associated environment", "definition": "An environmental system determined by an animal.", "synonyms": "Metazoan-associated environment&#124;animal environment", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET8 | curation/term_requests.tsv; TSV physical rows 7 | supports | [{"row": 7, "data": {"identifier": "habitatmech:GOLD.47e603cf4f", "requested_label": "bird-associated environment", "parent_class": "ENVO:01001002", "parent_label": "animal-associated environment", "definition": "An environmental system determined by a bird.", "exact_synonym": "Birds", "curator": "claude-opus-5", "date": "2026-08-16", "notes": "The habitat is the host clade, and it is the entire content of the concept: GOLD and BacDive both organise host-associated isolates by host, and every downstream anatomical path hangs off it. HabitatMech deliberately does not ground these to animal-associated environment, because every clade would then merge onto one record and the distinction the sources are making would be lost. ENVO already has this shape at plant-, animal- and fungi-associated environment; this asks for the same pattern one level down. ", "parent_mode": "ADD"}}] |
| ET9 | curation/decisions.tsv; TSV physical rows 488 | supports | [{"row": 488, "data": {"identifier": "habitatmech:GOLD.47e603cf4f", "decision": "CONFIRM_UNGROUNDED", "object_id": "ENVO:01001002", "object_label": "animal-associated environment", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-12", "notes": "Birds as host. Parented to animal-associated environment; not grounded there because every host clade would merge onto one record. ENVO term request.", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP10 | data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml; Direct-parent scope | supports | {"identifier": "ENVO:01001000", "label": "environmental system determined by an organism", "definition": "An environmental system which is determined by a living organism.", "grounding_status": "EXACT", "parent_habitats": ["ENVO:01000254"], "source_attestations": [{"source": "BACDIVE", "source_id": "bacdive.isolation_source:host", "source_label": "Host", "mapping_predicate": "skos:exactMatch", "assertion_count": 25581, "assertion_unit": "STRAIN", "notes": "kg-microbe's isolation-source mapping table has no ontology target for this source; the automatic route leaves it ungrounded. The explicit curator decision GROUND overrides that route; this source is emitted on ENVO:01001000."}, {"source": "GOLD", "source_id": "gold.ecosystem:3373", "source_label": "Host-associated", "source_path": "Host-associated", "mapping_predicate": "skos:exactMatch", "assertion_count": 3307, "assertion_unit": "ORGANISM", "notes": "5 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]} |
| EP11 | data/habitats/other/animal_associated_environment.yaml; Direct-parent scope | supports | {"identifier": "ENVO:01001002", "label": "animal-associated environment", "definition": "An environmental system determined by an animal.", "grounding_status": "EXACT", "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"source": "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal", "notes": "Physicochemical parameter bands from kg-microbe's environment table."}, {"source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated environment", "assertion_count": 144, "assertion_unit": "TAXON"}]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000254/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_01000254", "target": "http://purl.obolibrary.org/obo/RO_0002577", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000254; Current identity, definition and typed relations | supports | ENVO:01000254 environmental system; inspected definition: ["In ENVO's alignment with the Basic Formal Ontology, this class is being considered as a subclass of a proposed BFO class \"system\". The relation \"environed_by\" is also under development. Roughly, a system which includes a material entity (at least partially) within its site and causally influences that entity may be considered to environ it. Following the completion of this alignment, this class' definition and the definitions of its subclasses will be revised.", "A system which has the disposition to environ one or more material entities."] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000", "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000; Current identity, definition and typed relations | supports | ENVO:01001000 environmental system determined by an organism; inspected definition: ["An environmental system which is determined by a living organism."] |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001002", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002; Current identity, definition and typed relations | supports | ENVO:01001002 animal-associated environment; inspected definition: ["An environmental system determined by an animal."] |
| ESEARCH | Local maintained inputs and archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.47e603cf4f -e 'bird-associated environment' -e birds -e habitatmech:GOLD.47e603cf4f curation history research reports data/raw build reviews | context_only | Ignored-inclusive identifier/label/slug traversal plus exact TSV parsing found the stated source rows and no structured predecessor. |

## Limits And Additional Notes

- Only the identified source passages were assessed; every historical specimen or PREGO pair has not been independently verified.
- Counts, score and rank are not prevalence, viability, mechanism or characteristic presence. Parent observations are not inherited.
- Configured label correspondence skipped 2,061 pairs without adapters; this is not whole-corpus semantic certification.
- Exact-revision baseline full QC is remote evidence, not a new local QC execution. Post-save archive validation is a subsequent gate.
- iModulonDB is not applicable because no gene, regulator or expression module is asserted. No paid research or scientific-status promotion was performed.
- All captured local bytes were rechecked against the working tree and the captured Git tree before saving.
- Ignored-inclusive archive traversal found no structured predecessor. Legacy observations are contextual leads, not independent approval or structured lineage.
- This observation precedes any separately authorized curation/publication and does not claim a repair.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T110635Z-birds-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: bird-associated environment (habitatmech:GOLD.47e603cf4f)'
started_at: '2026-10-15T10:50:51Z'
finished_at: '2026-10-15T11:06:35Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected target and evidence; not independent human
    or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The bird-associated environmental definition and organism/animal-associated
  genera are coherent. The authored exact alias Birds names the whole host category
  rather than its environment. Preserve the 1,848 source ORGANISM assertions and verbatim
  source label.
source:
  git_revision: 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87
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
    sha256: e54999803277611372ffbad02a795423dc527822d7e900515f27f8824e6b7367
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 6dc8428e469ce29d5d091ec282d39445d07f11eb090e874de1efbe587a080782
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 5c9bd23cb0f681e2880ff13d606b0bf4d47d12fbcf73154260da1d795b801cbe
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: b303b863e16eb805932c8e8fe831cdb82b17518d63a8b3ab0f62fef675cd24cc
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
  - path: data/habitats/host_associated/birds.yaml
    sha256: 1a0a3370dd9dca70a569f866c0195f6edc6fbead2b583e1a9ebd3ffb1425ffd3
    role: target
  - path: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
    role: context
  - path: data/habitats/other/animal_associated_environment.yaml
    sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
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
  - path: reports/yaml_record_review/20260927T223225Z-birds.md
    sha256: 6ef332217a995f793d98c0a76b547bf658d9d44770813ede71eee16479b9425d
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
- target_id: habitatmech:GOLD.47e603cf4f
  path: data/habitats/host_associated/birds.yaml
  label: bird-associated environment
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
  description: Scientific assessment of one exact target at captured revision 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87.
  selection: Next twenty unreviewed records in corpus path order; this document assesses
    one resolved identifier.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.47e603cf4f
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context informs hierarchy but is not an additional completed review;
      exports are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/birds.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  summary: "Completed 2026-10-15T10:51:36Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/birds.yaml"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml
    data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml
    data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml
    data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml
    data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml
    data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml
    data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml
    data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml
    data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml
    data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  summary: "Completed 2026-10-15T10:52:03Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml\
    \ data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml\
    \ data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml\
    \ data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml\
    \ data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml\
    \ data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml\
    \ data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml\
    \ data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml\
    \ data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml\
    \ data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml\n\
    Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  summary: 'Completed 2026-10-15T10:52:45Z. No issues found

    789 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  summary: "Completed 2026-10-15T10:52:46Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  summary: "Completed 2026-10-15T10:53:13Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  summary: "Completed 2026-10-15T10:53:20Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  summary: "Completed 2026-10-15T10:53:50Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  summary: "Completed 2026-10-15T10:55:12Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema, strict validation of twenty targets, other gates
    full-corpus as documented.
- check_id: CCI
  name: Baseline full native QC
  status: passed
  required: true
  command: gh run view 38722329263 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  summary: Exact-revision full QC and structured review contract succeeded; verified
    2026-10-15T11:05:49Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38722329263
  scope_note: Remote baseline, not a new local QC execution.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/birds.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: Complete target read, including source paths, fields, taxa and history.
  snapshot_sha256: 1a0a3370dd9dca70a569f866c0195f6edc6fbead2b583e1a9ebd3ffb1425ffd3
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Habitat identity, strictly broader parents and owner boundaries
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: Whole hosts differ from associated environments; context and part-of links
    must not be asserted as broader habitat classes.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation, parent_habitats, xrefs and CharacteristicTaxon
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: Mapping endpoints, broader parents and reported versus characteristic presence
    are distinct.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native routes
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: 'Resolution results: [{"source": "GOLD", "mint": "habitatmech:GOLD.47e603cf4f",
    "automatic": {"identifier": "habitatmech:GOLD.47e603cf4f", "grounding_status":
    "UNGROUNDED", "mapping_predicate": null, "contributes_grounding": true, "extra_parents":
    [], "extra_xrefs": [], "route": "gold_unmatched", "category": null, "reviewed":
    false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.47e603cf4f",
    "grounding_status": "UNGROUNDED", "mapping_predicate": null, "contributes_grounding":
    true, "extra_parents": ["ENVO:01001002"], "extra_xrefs": [], "route": "curated_confirm_ungrounded_from_gold_unmatched",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.47e603cf4f",
    "decision": "CONFIRM_UNGROUNDED", "object_id": "ENVO:01001002", "object_label":
    "animal-associated environment", "grounding_status": "", "curator": "claude-opus-5",
    "date": "2026-08-12", "notes": "Birds as host. Parented to animal-associated environment;
    not grounded there because every host clade would merge onto one record. ENVO
    term request.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: Distinct pairs, maximum scores/channels, score/directness/ID ordering and
    full taxon pool are retained; original pair citations are not emitted.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: TSV physical rows 25
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: '[{"row": 25, "data": {"canonical_path": "Host-associated > Birds", "ecosystem":
    "Host-associated", "ecosystem_category": "Birds", "ecosystem_type": "", "ecosystem_subtype":
    "", "specific_ecosystem": "", "leaf_label": "Birds", "depth": "2", "gold_node_count":
    "4", "organism_count": "1848", "study_count": "0", "biosample_count": "0", "total_assertions":
    "1848", "gold_node_ids": "gold.ecosystem:3382|gold.ecosystem:3599|gold.ecosystem:3714|gold.ecosystem:4154"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: TSV physical rows 6795,6797
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: '[{"row": 6795, "data": {"subject": "ENVO:01001000", "predicate": "rdfs:subClassOf",
    "object": "ENVO:01000254"}}, {"row": 6797, "data": {"subject": "ENVO:01001002",
    "predicate": "rdfs:subClassOf", "object": "ENVO:01001000"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: TSV physical rows 8489,8491
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: '[{"row": 8489, "data": {"term_id": "ENVO:01001000", "ontology": "ENVO",
    "label": "environmental system determined by an organism", "definition": "An environmental
    system which is determined by a living organism.", "synonyms": "host-associated
    environment", "deprecated": "", "directly_referenced": "FALSE", "label_only":
    "FALSE"}}, {"row": 8491, "data": {"term_id": "ENVO:01001002", "ontology": "ENVO",
    "label": "animal-associated environment", "definition": "An environmental system
    determined by an animal.", "synonyms": "Metazoan-associated environment|animal
    environment", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET8
  kind: database
  reference: curation/term_requests.tsv
  locator: TSV physical rows 7
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: '[{"row": 7, "data": {"identifier": "habitatmech:GOLD.47e603cf4f", "requested_label":
    "bird-associated environment", "parent_class": "ENVO:01001002", "parent_label":
    "animal-associated environment", "definition": "An environmental system determined
    by a bird.", "exact_synonym": "Birds", "curator": "claude-opus-5", "date": "2026-08-16",
    "notes": "The habitat is the host clade, and it is the entire content of the concept:
    GOLD and BacDive both organise host-associated isolates by host, and every downstream
    anatomical path hangs off it. HabitatMech deliberately does not ground these to
    animal-associated environment, because every clade would then merge onto one record
    and the distinction the sources are making would be lost. ENVO already has this
    shape at plant-, animal- and fungi-associated environment; this asks for the same
    pattern one level down. ", "parent_mode": "ADD"}}]'
  snapshot_sha256: b303b863e16eb805932c8e8fe831cdb82b17518d63a8b3ab0f62fef675cd24cc
- evidence_id: ET9
  kind: database
  reference: curation/decisions.tsv
  locator: TSV physical rows 488
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: '[{"row": 488, "data": {"identifier": "habitatmech:GOLD.47e603cf4f", "decision":
    "CONFIRM_UNGROUNDED", "object_id": "ENVO:01001002", "object_label": "animal-associated
    environment", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-12",
    "notes": "Birds as host. Parented to animal-associated environment; not grounded
    there because every host clade would merge onto one record. ENVO term request.",
    "review_depth": "ITEM", "category": "", "relation": ""}}]'
  snapshot_sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
- evidence_id: EP10
  kind: record_content
  reference: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
  locator: Direct-parent scope
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: '{"identifier": "ENVO:01001000", "label": "environmental system determined
    by an organism", "definition": "An environmental system which is determined by
    a living organism.", "grounding_status": "EXACT", "parent_habitats": ["ENVO:01000254"],
    "source_attestations": [{"source": "BACDIVE", "source_id": "bacdive.isolation_source:host",
    "source_label": "Host", "mapping_predicate": "skos:exactMatch", "assertion_count":
    25581, "assertion_unit": "STRAIN", "notes": "kg-microbe''s isolation-source mapping
    table has no ontology target for this source; the automatic route leaves it ungrounded.
    The explicit curator decision GROUND overrides that route; this source is emitted
    on ENVO:01001000."}, {"source": "GOLD", "source_id": "gold.ecosystem:3373", "source_label":
    "Host-associated", "source_path": "Host-associated", "mapping_predicate": "skos:exactMatch",
    "assertion_count": 3307, "assertion_unit": "ORGANISM", "notes": "5 GOLD ecosystem
    node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]}'
  snapshot_sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
- evidence_id: EP11
  kind: record_content
  reference: data/habitats/other/animal_associated_environment.yaml
  locator: Direct-parent scope
  accessed_at: '2026-10-15T11:06:35Z'
  support: supports
  summary: '{"identifier": "ENVO:01001002", "label": "animal-associated environment",
    "definition": "An environmental system determined by an animal.", "grounding_status":
    "EXACT", "parent_habitats": ["ENVO:01001000"], "source_attestations": [{"source":
    "ENVIRONMENTS_TABLE", "source_id": "host_animal", "source_label": "host_animal",
    "notes": "Physicochemical parameter bands from kg-microbe''s environment table."},
    {"source": "MADIN", "source_id": "ENVO:01001002", "source_label": "animal-associated
    environment", "assertion_count": 144, "assertion_unit": "TAXON"}]}'
  snapshot_sha256: a1cf41f43f9bece44dfb3e5d6ab0ca86858df67b88ee25d6ada260cccac69e16
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000254/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:30Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_01000254",
    "target": "http://purl.obolibrary.org/obo/RO_0002577", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 743ecf3c761bfce55781906b57a31602e2f4366b29232406d53b40aaf75fcb78
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01000254
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:29Z'
  support: supports
  summary: 'ENVO:01000254 environmental system; inspected definition: ["In ENVO''s
    alignment with the Basic Formal Ontology, this class is being considered as a
    subclass of a proposed BFO class \"system\". The relation \"environed_by\" is
    also under development. Roughly, a system which includes a material entity (at
    least partially) within its site and causally influences that entity may be considered
    to environ it. Following the completion of this alignment, this class'' definition
    and the definitions of its subclasses will be revised.", "A system which has the
    disposition to environ one or more material entities."]'
  snapshot_sha256: 6400120603ffe93953d6ea567a86900fc6692a8538ed015eb299135e2a98dd8b
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:35Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "target": "http://purl.obolibrary.org/obo/ENVO_01000254", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001000",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_131567", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: e11b34dbd0a626083d5d0bbbb364469ef95831fb61cb81da5377d59715b272ca
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001000
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:34Z'
  support: supports
  summary: 'ENVO:01001000 environmental system determined by an organism; inspected
    definition: ["An environmental system which is determined by a living organism."]'
  snapshot_sha256: 8bd797929d18bf28171af7fd10f358db9b093f752d20b99f665779bb2e6b504e
- evidence_id: EX5
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:36Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001002",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_33208", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 882375d994d0dea7166097328c56e0e22362848e68aba0125d1b128a24ebf1b0
- evidence_id: EX6
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001002
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:36Z'
  support: supports
  summary: 'ENVO:01001002 animal-associated environment; inspected definition: ["An
    environmental system determined by an animal."]'
  snapshot_sha256: c3c90d5e91cc85727658222c907f7747f34861ad80bf1ceac5ce209f7e170907
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.47e603cf4f -e 'bird-associated
    environment' -e birds -e habitatmech:GOLD.47e603cf4f curation history research
    reports data/raw build reviews
  accessed_at: '2026-10-15T10:51:11Z'
  support: context_only
  summary: Ignored-inclusive identifier/label/slug traversal plus exact TSV parsing
    found the stated source rows and no structured predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    all structured review.yaml files traversed independently of gitignore.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validity and reproduction
  outcome: supported
  summary: Individual schema, twenty-target strict validation, 789 history records,
    14 inventories/two GOLD sources, 3,208-record reproduction, 32 overlays and 110
    term requests passed. These are deterministic rather than scientific certification.
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, hierarchy and alias scope
  outcome: concern
  summary: The bird-associated environmental definition and organism/animal-associated
    genera are coherent. The authored exact alias Birds names the whole host category
    rather than its environment. Preserve the 1,848 source ORGANISM assertions and
    verbatim source label.
  target_ids:
  - habitatmech:GOLD.47e603cf4f
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
- assessment_id: A3
  area: quantity
  topic: Counts, units and ranking
  outcome: supported
  summary: 'Exact source rows reproduce [{"source": "GOLD", "count": 1848, "unit":
    "ORGANISM"}]. All 0 retained taxon IDs were resolved against current NCBI identities,
    including the explicit alias noted for bile. Zero-count omissions are not biological
    absence; unlike counts are not summed.'
  target_ids:
  - habitatmech:GOLD.47e603cf4f
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
- assessment_id: A4
  area: completeness
  topic: Native status and optional assertions
  outcome: supported
  summary: Executed routes reproduce UNGROUNDED/REVIEWED. No causal or characteristic-presence
    claim is asserted; missing optional fields are not automatic deficiencies.
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: birds-host-name-exact-synonym
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: Whole-host name is asserted as an exact environment synonym
  description: Remove the authored exact host alias 'Birds' from its term_requests.tsv
    row and guard automatic old-label fallback in definition_source_label_exclusions.tsv.
    Keep the verbatim attestation, minted identity, environmental definition, genuine
    genera and source counts.
  target_ids:
  - habitatmech:GOLD.47e603cf4f
  field_paths:
  - synonyms
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - ESCHEMA
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
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
  - habitatmech:GOLD.47e603cf4f
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Remove the authored exact host alias 'Birds' from its term_requests.tsv
    row and guard automatic old-label fallback in definition_source_label_exclusions.tsv.
    Keep the verbatim attestation, minted identity, environmental definition, genuine
    genera and source counts. No repair is performed by this review.
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
- Only the identified source passages were assessed; every historical specimen or
  PREGO pair has not been independently verified.
- Counts, score and rank are not prevalence, viability, mechanism or characteristic
  presence. Parent observations are not inherited.
- Configured label correspondence skipped 2,061 pairs without adapters; this is not
  whole-corpus semantic certification.
- Exact-revision baseline full QC is remote evidence, not a new local QC execution.
  Post-save archive validation is a subsequent gate.
- iModulonDB is not applicable because no gene, regulator or expression module is
  asserted. No paid research or scientific-status promotion was performed.
notes:
- All captured local bytes were rechecked against the working tree and the captured
  Git tree before saving.
- Ignored-inclusive archive traversal found no structured predecessor. Legacy observations
  are contextual leads, not independent approval or structured lineage.
- This observation precedes any separately authorized curation/publication and does
  not claim a repair.
tags:
- individual-scientific-review
- host-associated
```
