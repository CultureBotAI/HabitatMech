# Record review: Bladder (habitatmech:GOLD.2c26547de4)

- Review: 20261015T125452Z-bladder__9a6dd80c-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T12:40:45Z
- Finished UTC: 2026-10-15T12:54:52Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The minted human bladder-polyp source context is retained, but neither a cnidarian polyp nor the whole urinary bladder is a strictly broader class for that lesion. The retained-mint narrow-match output also inherits the shared endpoint-contract problem.

## Scope And Provenance

Scientific review of one exact target at 68ceabb7039a537f65be44ac6aaa913116a154f5.

Selection: First seven records in the prepared next-twenty path-ordered cohort; this bundle assesses exactly one resolved identifier.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 68ceabb7039a537f65be44ac6aaa913116a154f5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.2c26547de4 | data/habitats/host_associated/bladder__9a6dd80c.yaml | generated | Bladder |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.2c26547de4 | Completed 2026-10-15T12:40:47Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bladder__9a6dd80c.yaml |
| validate-strict | passed | True | habitatmech:GOLD.2c26547de4 | Completed 2026-10-15T12:41:35Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml data/habitats/host_associated/blast_cell.yaml data/habitats/host_associated/blood.yaml data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.2c26547de4 | Completed 2026-10-15T12:41:43Z. No issues found<br>808 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.2c26547de4 | Completed 2026-10-15T12:41:44Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.2c26547de4 | Completed 2026-10-15T12:41:58Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.2c26547de4 | Completed 2026-10-15T12:42:02Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.2c26547de4 | Completed 2026-10-15T12:42:18Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.2c26547de4 | Completed 2026-10-15T12:42:59Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-revision baseline full QC | passed | True | habitatmech:GOLD.2c26547de4 | Verified 2026-10-15T12:40:46Z: https://github.com/CultureBotAI/HabitatMech/actions/runs/38733485444 |

## Scientific And Domain Assessments

### Native validation and reproduction

schema: supported. Targets: habitatmech:GOLD.2c26547de4.

Schema, strict, history, provenance, 3,208-record reproduction, causal overlays, term requests and configured labels passed. These establish deterministic fidelity, not scientific support.

### Identity, hierarchy and nomenclature

identity: concern. Targets: habitatmech:GOLD.2c26547de4.

The minted human bladder-polyp source context is retained, but neither a cnidarian polyp nor the whole urinary bladder is a strictly broader class for that lesion. The retained-mint narrow-match output also inherits the shared endpoint-contract problem.

### Source count, unit and ranking

quantity: supported. Targets: habitatmech:GOLD.2c26547de4.

Exact source projections retain [{"source": "GOLD", "source_id": "gold.ecosystem:6653", "source_label": "Bladder", "source_path": "Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Polyps &gt; Bladder", "mapping_predicate": "skos:narrowMatch"}]. All 0 displayed taxa were resolved against current NCBI IDs/labels. Ranks and candidate pools are source-specific; unlike units are never summed.

### Native status and optional fields

completeness: supported. Targets: habitatmech:GOLD.2c26547de4.

Executed source decisions reproduce NARROW/REVIEWED. No causal mechanism or is_characteristic assertion is present. Missing optional fields or SEEDED status are not automatic scientific defects.

## Findings

### F1: Human bladder-polyp context inherits a cnidarian parent

major / open / confirmed; issue key: bladder--9a6dd80c-cnidarian-context-parent.

Suppress only the exact GOLD parent contribution BTO:0006350 using gold_parent_exclusions.tsv. The independent parent identity defect remains #2171; do not silently relabel that other record or substitute a disease term.

### F2: A bladder polyp is not a kind of whole urinary bladder

major / open / confirmed; issue key: bladder--9a6dd80c-organ-as-genus.

Replace the exact source decision GROUND_AS_PARENT with supported retained-mint curation that keeps UBERON:0001255 only as contextual xref. Preserve the source path and zero-count omission; no unsupported lesion definition or organ identity should be invented.

### F3: Narrow mapping compares an undeclared ontology-parent endpoint

major / open / confirmed; issue key: bladder--9a6dd80c-mapping-endpoint-contract.

The executed GROUND_AS_PARENT route retains the source mint but emits narrowMatch relative to UBERON:0001255, unlike the schema source-to-record endpoint. Correct this target through its unsupported parent decision; shared producer/schema/consumer reconciliation remains #1398. This is not a claim that SKOS forbids self-links.

## Recommended Actions And Acceptance Checks

### ACT1

Suppress only the exact GOLD parent contribution BTO:0006350 using gold_parent_exclusions.tsv. The independent parent identity defect remains #2171; do not silently relabel that other record or substitute a disease term. No repair is performed by this review.

- Regress exact ancestry and endpoint claims while retaining the minted identity, source path, omitted zero counts and REVIEWED status. A justified NARROW-to-UNGROUNDED change and removal of its unsupported narrowMatch are expected; archive old decision evidence and append curation history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT2

Replace the exact source decision GROUND_AS_PARENT with supported retained-mint curation that keeps UBERON:0001255 only as contextual xref. Preserve the source path and zero-count omission; no unsupported lesion definition or organ identity should be invented. No repair is performed by this review.

- Regress exact ancestry and endpoint claims while retaining the minted identity, source path, omitted zero counts and REVIEWED status. A justified NARROW-to-UNGROUNDED change and removal of its unsupported narrowMatch are expected; archive old decision evidence and append curation history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

### ACT3

The executed GROUND_AS_PARENT route retains the source mint but emits narrowMatch relative to UBERON:0001255, unlike the schema source-to-record endpoint. Correct this target through its unsupported parent decision; shared producer/schema/consumer reconciliation remains #1398. This is not a claim that SKOS forbids self-links. No repair is performed by this review.

- Regress exact ancestry and endpoint claims while retaining the minted identity, source path, omitted zero counts and REVIEWED status. A justified NARROW-to-UNGROUNDED change and removal of its unsupported narrowMatch are expected; archive old decision evidence and append curation history.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bladder__9a6dd80c.yaml; Entire target YAML | supports | Read the full target including source paths, taxa, hierarchy and history. |
| ERULE | docs/CURATION.md; Identity, broader-parent and ownership rules | supports | Context, containment and whole-host identity differ from strictly broader habitat ancestry. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation and CharacteristicTaxon | supports | Mapping endpoints, assertion units and association versus characteristic-presence semantics. |
| ESEED | src/habitatmech/seed.py; Executed native source resolution | supports | Exact routes: [{"source": "GOLD", "mint": "habitatmech:GOLD.2c26547de4", "automatic": {"identifier": "BTO:0000123", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "habitatmech:GOLD.2c26547de4", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["UBERON:0001255"], "extra_xrefs": [], "route": "curated_ground_as_parent_from_gold_leaf_label", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.2c26547de4", "decision": "GROUND_AS_PARENT", "object_id": "UBERON:0001255", "object_label": "urinary bladder", "grounding_status": "NARROW", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "A bladder polyp, not the bladder. GOLD's path places it under Benign tumor. Path: Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Polyps &gt; Bladder", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; extract_prego | supports | Projection preserves distinct-taxon totals and score/channel ranking but not original pair citations. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 2170 | supports | [{"row": 2170, "data": {"canonical_path": "Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Polyps &gt; Bladder", "ecosystem": "Host-associated", "ecosystem_category": "Mammals: Human", "ecosystem_type": "Benign tumor", "ecosystem_subtype": "Polyps", "specific_ecosystem": "Bladder", "leaf_label": "Bladder", "depth": "5", "gold_node_count": "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions": "0", "gold_node_ids": "gold.ecosystem:6653"}}] |
| ET6 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 4438,11185,11186,11187 | supports | [{"row": 4438, "data": {"subject": "BTO:0006350", "predicate": "rdfs:subClassOf", "object": "BTO:0000284"}}, {"row": 11185, "data": {"subject": "UBERON:0001255", "predicate": "rdfs:subClassOf", "object": "UBERON:0002075"}}, {"row": 11186, "data": {"subject": "UBERON:0001255", "predicate": "rdfs:subClassOf", "object": "UBERON:0004120"}}, {"row": 11187, "data": {"subject": "UBERON:0001255", "predicate": "rdfs:subClassOf", "object": "UBERON:0018707"}}] |
| ET7 | data/raw/ontology_terms.tsv; Physical TSV rows 6349,13026 | supports | [{"row": 6349, "data": {"term_id": "BTO:0006350", "ontology": "BTO", "label": "polyp", "definition": "The sessile form of cnidarian (such as a coral or sea anemone) typically having a hollow cylindrical body closed and attached at one end and opening at the other by a central mouth surrounded by tentacles armed with nematocysts.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 13026, "data": {"term_id": "UBERON:0001255", "ontology": "UBERON", "label": "urinary bladder", "definition": "Distensible musculomembranous organ situated in the anterior part of the pelvic cavity in which urine collects before excretion[MP].", "synonyms": "bladder&#124;urocyst&#124;vesica&#124;vesica urinaria", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}] |
| ET8 | curation/decisions.tsv; Physical TSV rows 349 | supports | [{"row": 349, "data": {"identifier": "habitatmech:GOLD.2c26547de4", "decision": "GROUND_AS_PARENT", "object_id": "UBERON:0001255", "object_label": "urinary bladder", "grounding_status": "NARROW", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "A bladder polyp, not the bladder. GOLD's path places it under Benign tumor. Path: Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Polyps &gt; Bladder", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP9 | data/habitats/host_associated/polyp.yaml; Entire parent read for scope, not additional review coverage | supports | {"identifier": "BTO:0006350", "label": "polyp", "definition": "The sessile form of cnidarian (such as a coral or sea anemone) typically having a hollow cylindrical body closed and attached at one end and opening at the other by a central mouth surrounded by tentacles armed with nematocysts.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "REVIEWED", "synonyms": [{"synonym_text": "Polyps", "synonym_type": "EXACT_SYNONYM", "source": "GOLD"}], "parent_habitats": ["BTO:0000284", "habitatmech:GOLD.333c18201f"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6242", "source_label": "Polyps", "source_path": "Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Polyps", "mapping_predicate": "skos:exactMatch"}], "curation_history": [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND", "changes": "Grounded to BTO:0006350 'polyp' (EXACT). Leaf label equals the BTO label exactly and no other source concept claims it. Path: Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Polyps (source concept habitatmech:GOLD.bb1e8cd107)"}, {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: EXACT."}]} |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284/graph; BTO_0000284-graph.json | context_only | Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000284", "target": "http://purl.obolibrary.org/obo/BTO_0000000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284?lang=en; BTO_0000284.json | context_only | Inspected current identifier, label, active status and full definition for the scope assessment: {"obo_id": "BTO:0000284", "label": "organism form", "is_obsolete": false} |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0006350/graph; BTO_0006350-graph.json | context_only | Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0006350", "target": "http://purl.obolibrary.org/obo/BTO_0000284", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0006350?lang=en; BTO_0006350.json | context_only | Inspected current identifier, label, active status and full definition for the scope assessment: {"obo_id": "BTO:0006350", "label": "polyp", "is_obsolete": false} |
| EX14 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001255/graph; UBERON_0001255-graph.json | context_only | Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0002075", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0004120", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0018707", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0000164", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0001556", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0002323", "uri": "http://purl.obolibrary.org/obo/RO_0001025", "label": "located in"}] |
| EX15 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001255?lang=en; UBERON_0001255.json | context_only | Inspected current identifier, label, active status and full definition for the scope assessment: {"obo_id": "UBERON:0001255", "label": "urinary bladder", "is_obsolete": false} |
| ESEARCH | Local maintained inputs and structured archive; rg --no-ignore --hidden -l -F -e habitatmech:GOLD.2c26547de4 -e Bladder -e bladder__9a6dd80c -e habitatmech:GOLD.2c26547de4 curation history research reports data/raw build reviews | context_only | Ignored-inclusive search plus exact TSV parsing identified the stated source rows and no structured predecessor. |

## Limits And Additional Notes

- Every historical specimen and original PREGO pair has not been independently reidentified. Counts/scores/ranks are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 pairs without adapters; deterministic validity does not certify biological semantics.
- Full baseline QC is verified remote evidence at the captured revision, not a new local execution. Post-save archive and publication gates are subsequent.
- iModulonDB is not applicable: the target asserts no gene, regulator or expression module. No paid research was performed.
- All captured local input hashes were rechecked against both the working tree and exact Git revision. No input bytes were silently refreshed.
- Ignored-inclusive archive traversal found no structured predecessor for this target; legacy Markdown is context, not independent approval or successor lineage.
- This observation precedes separately authorized curation/publication and does not claim a repair.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T125452Z-bladder__9a6dd80c-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Bladder (habitatmech:GOLD.2c26547de4)'
started_at: '2026-10-15T12:40:45Z'
finished_at: '2026-10-15T12:54:52Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected the record and evidence; not independent
    human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The minted human bladder-polyp source context is retained, but neither a
  cnidarian polyp nor the whole urinary bladder is a strictly broader class for that
  lesion. The retained-mint narrow-match output also inherits the shared endpoint-contract
  problem.
source:
  git_revision: 68ceabb7039a537f65be44ac6aaa913116a154f5
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
    sha256: 6d5cbfd0f5ad911fbb074ee8ec253625d1fa13d94117759b1f25a1cd2e6576bc
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: a92f9003cc5f57c397ab5118474318f216077a8e9f90564d21dfa8089477a2eb
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
  - path: data/habitats/host_associated/bladder__9a6dd80c.yaml
    sha256: d38a8a7aa323675ca59765a868080c039505423e4ca01f01796ced9b45f979ed
    role: target
  - path: data/habitats/host_associated/polyp.yaml
    sha256: 5c6d8ce4d9028c2b4279ba300e7a567e20793d4a5e30c70b8de74c0119508767
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
- target_id: habitatmech:GOLD.2c26547de4
  path: data/habitats/host_associated/bladder__9a6dd80c.yaml
  label: Bladder
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
  description: Scientific review of one exact target at 68ceabb7039a537f65be44ac6aaa913116a154f5.
  selection: First seven records in the prepared next-twenty path-ordered cohort;
    this bundle assesses exactly one resolved identifier.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.2c26547de4
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parent context is not additional reviewed coverage. Export readiness is
      not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bladder__9a6dd80c.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Completed 2026-10-15T12:40:47Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bladder__9a6dd80c.yaml"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml
    data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml
    data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml
    data/habitats/host_associated/blast_cell.yaml data/habitats/host_associated/blood.yaml
    data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml
    data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml
    data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml
    data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml
    data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml
    data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Completed 2026-10-15T12:41:35Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml\
    \ data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml\
    \ data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml\
    \ data/habitats/host_associated/blast_cell.yaml data/habitats/host_associated/blood.yaml\
    \ data/habitats/host_associated/blood__070ce7aa.yaml data/habitats/host_associated/blood__5ca8064f.yaml\
    \ data/habitats/host_associated/blood__5ef3f2f4.yaml data/habitats/host_associated/blood__c1b484fe.yaml\
    \ data/habitats/host_associated/blood__d6f5ae05.yaml data/habitats/host_associated/blood_plasma.yaml\
    \ data/habitats/host_associated/blood_plasma__00b70c6a.yaml data/habitats/host_associated/blood_serum.yaml\
    \ data/habitats/host_associated/blood_vessel.yaml data/habitats/host_associated/bone.yaml\
    \ data/habitats/host_associated/bone__169c3d9e.yaml data/habitats/host_associated/bone__234001be.yaml\n\
    Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: 'Completed 2026-10-15T12:41:43Z. No issues found

    808 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Completed 2026-10-15T12:41:44Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Completed 2026-10-15T12:41:58Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Completed 2026-10-15T12:42:02Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Completed 2026-10-15T12:42:18Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Completed 2026-10-15T12:42:59Z. id↔label correspondence summary:\n   \
    \       OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict run includes all twenty prepared targets;
    other gates are full-corpus as documented.
- check_id: CCI
  name: Exact-revision baseline full QC
  status: passed
  required: true
  command: gh run view 38733485444 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: 'Verified 2026-10-15T12:40:46Z: https://github.com/CultureBotAI/HabitatMech/actions/runs/38733485444'
  scope_note: Remote full-QC execution at the exact unchanged scientific baseline;
    new review outputs are not yet covered.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bladder__9a6dd80c.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: Read the full target including source paths, taxa, hierarchy and history.
  snapshot_sha256: d38a8a7aa323675ca59765a868080c039505423e4ca01f01796ced9b45f979ed
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, broader-parent and ownership rules
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: Context, containment and whole-host identity differ from strictly broader
    habitat ancestry.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation and CharacteristicTaxon
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: Mapping endpoints, assertion units and association versus characteristic-presence
    semantics.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed native source resolution
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: 'Exact routes: [{"source": "GOLD", "mint": "habitatmech:GOLD.2c26547de4",
    "automatic": {"identifier": "BTO:0000123", "grounding_status": "EXACT", "mapping_predicate":
    "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs":
    [], "route": "gold_leaf_label", "category": null, "reviewed": false, "decision":
    null}, "final": {"identifier": "habitatmech:GOLD.2c26547de4", "grounding_status":
    "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true,
    "extra_parents": ["UBERON:0001255"], "extra_xrefs": [], "route": "curated_ground_as_parent_from_gold_leaf_label",
    "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.2c26547de4",
    "decision": "GROUND_AS_PARENT", "object_id": "UBERON:0001255", "object_label":
    "urinary bladder", "grounding_status": "NARROW", "curator": "claude-opus-5", "date":
    "2026-08-13", "notes": "A bladder polyp, not the bladder. GOLD''s path places
    it under Benign tumor. Path: Host-associated > Mammals: Human > Benign tumor >
    Polyps > Bladder", "review_depth": "ITEM", "category": "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: extract_prego
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: Projection preserves distinct-taxon totals and score/channel ranking but
    not original pair citations.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 2170
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: '[{"row": 2170, "data": {"canonical_path": "Host-associated > Mammals:
    Human > Benign tumor > Polyps > Bladder", "ecosystem": "Host-associated", "ecosystem_category":
    "Mammals: Human", "ecosystem_type": "Benign tumor", "ecosystem_subtype": "Polyps",
    "specific_ecosystem": "Bladder", "leaf_label": "Bladder", "depth": "5", "gold_node_count":
    "1", "organism_count": "0", "study_count": "0", "biosample_count": "0", "total_assertions":
    "0", "gold_node_ids": "gold.ecosystem:6653"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 4438,11185,11186,11187
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: '[{"row": 4438, "data": {"subject": "BTO:0006350", "predicate": "rdfs:subClassOf",
    "object": "BTO:0000284"}}, {"row": 11185, "data": {"subject": "UBERON:0001255",
    "predicate": "rdfs:subClassOf", "object": "UBERON:0002075"}}, {"row": 11186, "data":
    {"subject": "UBERON:0001255", "predicate": "rdfs:subClassOf", "object": "UBERON:0004120"}},
    {"row": 11187, "data": {"subject": "UBERON:0001255", "predicate": "rdfs:subClassOf",
    "object": "UBERON:0018707"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET7
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 6349,13026
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: '[{"row": 6349, "data": {"term_id": "BTO:0006350", "ontology": "BTO", "label":
    "polyp", "definition": "The sessile form of cnidarian (such as a coral or sea
    anemone) typically having a hollow cylindrical body closed and attached at one
    end and opening at the other by a central mouth surrounded by tentacles armed
    with nematocysts.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE",
    "label_only": "FALSE"}}, {"row": 13026, "data": {"term_id": "UBERON:0001255",
    "ontology": "UBERON", "label": "urinary bladder", "definition": "Distensible musculomembranous
    organ situated in the anterior part of the pelvic cavity in which urine collects
    before excretion[MP].", "synonyms": "bladder|urocyst|vesica|vesica urinaria",
    "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET8
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 349
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: '[{"row": 349, "data": {"identifier": "habitatmech:GOLD.2c26547de4", "decision":
    "GROUND_AS_PARENT", "object_id": "UBERON:0001255", "object_label": "urinary bladder",
    "grounding_status": "NARROW", "curator": "claude-opus-5", "date": "2026-08-13",
    "notes": "A bladder polyp, not the bladder. GOLD''s path places it under Benign
    tumor. Path: Host-associated > Mammals: Human > Benign tumor > Polyps > Bladder",
    "review_depth": "ITEM", "category": "", "relation": ""}}]'
  snapshot_sha256: ca42d86b6040df1c0c6e6ed36573bb51975a5e8daade262113bce547f1b6fd8b
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/polyp.yaml
  locator: Entire parent read for scope, not additional review coverage
  accessed_at: '2026-10-15T12:54:52Z'
  support: supports
  summary: '{"identifier": "BTO:0006350", "label": "polyp", "definition": "The sessile
    form of cnidarian (such as a coral or sea anemone) typically having a hollow cylindrical
    body closed and attached at one end and opening at the other by a central mouth
    surrounded by tentacles armed with nematocysts.", "definition_source": "BTO",
    "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status":
    "REVIEWED", "synonyms": [{"synonym_text": "Polyps", "synonym_type": "EXACT_SYNONYM",
    "source": "GOLD"}], "parent_habitats": ["BTO:0000284", "habitatmech:GOLD.333c18201f"],
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6242",
    "source_label": "Polyps", "source_path": "Host-associated > Mammals: Human > Benign
    tumor > Polyps", "mapping_predicate": "skos:exactMatch"}], "curation_history":
    [{"timestamp": "2026-08-12T00:00:00Z", "curator": "claude-opus-5", "action": "GROUND",
    "changes": "Grounded to BTO:0006350 ''polyp'' (EXACT). Leaf label equals the BTO
    label exactly and no other source concept claims it. Path: Host-associated > Mammals:
    Human > Benign tumor > Polyps (source concept habitatmech:GOLD.bb1e8cd107)"},
    {"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: EXACT."}]}'
  snapshot_sha256: 5c6d8ce4d9028c2b4279ba300e7a567e20793d4a5e30c70b8de74c0119508767
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284/graph
  locator: BTO_0000284-graph.json
  accessed_at: '2026-10-15T12:46:43Z'
  support: context_only
  summary: 'Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000284",
    "target": "http://purl.obolibrary.org/obo/BTO_0000000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: d8667ccebbf1ef06a4dfb8fc90b7e8fd16d9475a22121ec59f2cf35c6c7c5968
- evidence_id: EX11
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284?lang=en
  locator: BTO_0000284.json
  accessed_at: '2026-10-15T12:46:42Z'
  support: context_only
  summary: 'Inspected current identifier, label, active status and full definition
    for the scope assessment: {"obo_id": "BTO:0000284", "label": "organism form",
    "is_obsolete": false}'
  snapshot_sha256: 305fb4df3b8081b3645a0a98f1f5abe7014f5e0b0458732189ba37fdd5b961f8
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0006350/graph
  locator: BTO_0006350-graph.json
  accessed_at: '2026-10-15T12:46:51Z'
  support: context_only
  summary: 'Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0006350",
    "target": "http://purl.obolibrary.org/obo/BTO_0000284", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 1610c0d9304b069603a2ba93586a9c01a4d357afafbb46022fd84481a003867c
- evidence_id: EX13
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0006350?lang=en
  locator: BTO_0006350.json
  accessed_at: '2026-10-15T12:46:51Z'
  support: context_only
  summary: 'Inspected current identifier, label, active status and full definition
    for the scope assessment: {"obo_id": "BTO:0006350", "label": "polyp", "is_obsolete":
    false}'
  snapshot_sha256: acfaec2f3c9439f472dfaf0e51b349d13ab3c16f075e2944fc7493e89849b25c
- evidence_id: EX14
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001255/graph
  locator: UBERON_0001255-graph.json
  accessed_at: '2026-10-15T12:47:04Z'
  support: context_only
  summary: 'Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001255",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002075", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004120", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255",
    "target": "http://purl.obolibrary.org/obo/UBERON_0018707", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000164", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001556", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002323", "uri": "http://purl.obolibrary.org/obo/RO_0001025",
    "label": "located in"}]'
  snapshot_sha256: ff5e9d29907843cdcb80b8a7574112f3a344ef8c623d501b50ac0a43ae13d69f
- evidence_id: EX15
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001255?lang=en
  locator: UBERON_0001255.json
  accessed_at: '2026-10-15T12:47:04Z'
  support: context_only
  summary: 'Inspected current identifier, label, active status and full definition
    for the scope assessment: {"obo_id": "UBERON:0001255", "label": "urinary bladder",
    "is_obsolete": false}'
  snapshot_sha256: 8520adccd22e2c33e22f4bdab14e87519c4750c7759e1c0e55813299c4e0a16a
- evidence_id: ESEARCH
  kind: search
  reference: Local maintained inputs and structured archive
  locator: rg --no-ignore --hidden -l -F -e habitatmech:GOLD.2c26547de4 -e Bladder
    -e bladder__9a6dd80c -e habitatmech:GOLD.2c26547de4 curation history research
    reports data/raw build reviews
  accessed_at: '2026-10-15T12:45:44Z'
  support: context_only
  summary: Ignored-inclusive search plus exact TSV parsing identified the stated source
    rows and no structured predecessor.
  search_scope: curation, history, research, reports, data/raw, build and reviews,
    including ignored and hidden files; pathlib traversal of all structured review.yaml
    files.
assessments:
- assessment_id: A1
  area: schema
  topic: Native validation and reproduction
  outcome: supported
  summary: Schema, strict, history, provenance, 3,208-record reproduction, causal
    overlays, term requests and configured labels passed. These establish deterministic
    fidelity, not scientific support.
  target_ids:
  - habitatmech:GOLD.2c26547de4
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Identity, hierarchy and nomenclature
  outcome: concern
  summary: The minted human bladder-polyp source context is retained, but neither
    a cnidarian polyp nor the whole urinary bladder is a strictly broader class for
    that lesion. The retained-mint narrow-match output also inherits the shared endpoint-contract
    problem.
  target_ids:
  - habitatmech:GOLD.2c26547de4
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
- assessment_id: A3
  area: quantity
  topic: Source count, unit and ranking
  outcome: supported
  summary: 'Exact source projections retain [{"source": "GOLD", "source_id": "gold.ecosystem:6653",
    "source_label": "Bladder", "source_path": "Host-associated > Mammals: Human >
    Benign tumor > Polyps > Bladder", "mapping_predicate": "skos:narrowMatch"}]. All
    0 displayed taxa were resolved against current NCBI IDs/labels. Ranks and candidate
    pools are source-specific; unlike units are never summed.'
  target_ids:
  - habitatmech:GOLD.2c26547de4
  evidence_ids:
  - E1
  - ESEED
  - EEXTRACT
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
- assessment_id: A4
  area: completeness
  topic: Native status and optional fields
  outcome: supported
  summary: Executed source decisions reproduce NARROW/REVIEWED. No causal mechanism
    or is_characteristic assertion is present. Missing optional fields or SEEDED status
    are not automatic scientific defects.
  target_ids:
  - habitatmech:GOLD.2c26547de4
  evidence_ids:
  - E1
  - ESEED
  - ESCHEMA
findings:
- finding_id: F1
  issue_key: bladder--9a6dd80c-cnidarian-context-parent
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Human bladder-polyp context inherits a cnidarian parent
  description: 'Suppress only the exact GOLD parent contribution BTO:0006350 using
    gold_parent_exclusions.tsv. The independent parent identity defect remains #2171;
    do not silently relabel that other record or substitute a disease term.'
  target_ids:
  - habitatmech:GOLD.2c26547de4
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2171
- finding_id: F2
  issue_key: bladder--9a6dd80c-organ-as-genus
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: A bladder polyp is not a kind of whole urinary bladder
  description: Replace the exact source decision GROUND_AS_PARENT with supported retained-mint
    curation that keeps UBERON:0001255 only as contextual xref. Preserve the source
    path and zero-count omission; no unsupported lesion definition or organ identity
    should be invented.
  target_ids:
  - habitatmech:GOLD.2c26547de4
  field_paths:
  - parent_habitats
  - grounding_status
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues: []
- finding_id: F3
  issue_key: bladder--9a6dd80c-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping compares an undeclared ontology-parent endpoint
  description: 'The executed GROUND_AS_PARENT route retains the source mint but emits
    narrowMatch relative to UBERON:0001255, unlike the schema source-to-record endpoint.
    Correct this target through its unsupported parent decision; shared producer/schema/consumer
    reconciliation remains #1398. This is not a claim that SKOS forbids self-links.'
  target_ids:
  - habitatmech:GOLD.2c26547de4
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
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
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.2c26547de4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'Suppress only the exact GOLD parent contribution BTO:0006350 using
    gold_parent_exclusions.tsv. The independent parent identity defect remains #2171;
    do not silently relabel that other record or substitute a disease term. No repair
    is performed by this review.'
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress exact ancestry and endpoint claims while retaining the minted identity,
    source path, omitted zero counts and REVIEWED status. A justified NARROW-to-UNGROUNDED
    change and removal of its unsupported narrowMatch are expected; archive old decision
    evidence and append curation history.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.2c26547de4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Replace the exact source decision GROUND_AS_PARENT with supported retained-mint
    curation that keeps UBERON:0001255 only as contextual xref. Preserve the source
    path and zero-count omission; no unsupported lesion definition or organ identity
    should be invented. No repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress exact ancestry and endpoint claims while retaining the minted identity,
    source path, omitted zero counts and REVIEWED status. A justified NARROW-to-UNGROUNDED
    change and removal of its unsupported narrowMatch are expected; archive old decision
    evidence and append curation history.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
- action_id: ACT3
  finding_ids:
  - F3
  target_ids:
  - habitatmech:GOLD.2c26547de4
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'The executed GROUND_AS_PARENT route retains the source mint but emits
    narrowMatch relative to UBERON:0001255, unlike the schema source-to-record endpoint.
    Correct this target through its unsupported parent decision; shared producer/schema/consumer
    reconciliation remains #1398. This is not a claim that SKOS forbids self-links.
    No repair is performed by this review.'
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress exact ancestry and endpoint claims while retaining the minted identity,
    source path, omitted zero counts and REVIEWED status. A justified NARROW-to-UNGROUNDED
    change and removal of its unsupported narrowMatch are expected; archive old decision
    evidence and append curation history.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Every historical specimen and original PREGO pair has not been independently reidentified.
  Counts/scores/ranks are not prevalence, viability or characteristic presence.
- Configured label checks skip 2,061 pairs without adapters; deterministic validity
  does not certify biological semantics.
- Full baseline QC is verified remote evidence at the captured revision, not a new
  local execution. Post-save archive and publication gates are subsequent.
- 'iModulonDB is not applicable: the target asserts no gene, regulator or expression
  module. No paid research was performed.'
notes:
- All captured local input hashes were rechecked against both the working tree and
  exact Git revision. No input bytes were silently refreshed.
- Ignored-inclusive archive traversal found no structured predecessor for this target;
  legacy Markdown is context, not independent approval or successor lineage.
- This observation precedes separately authorized curation/publication and does not
  claim a repair.
tags:
- individual-scientific-review
- host-associated
```
