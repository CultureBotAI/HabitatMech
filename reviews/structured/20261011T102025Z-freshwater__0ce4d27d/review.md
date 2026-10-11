# Scientific record review: freshwater__0ce4d27d

- Review: 20261011T102025Z-freshwater__0ce4d27d
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T10:09:21.217672Z
- Finished UTC: 2026-10-11T10:20:25.911866Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The microcosm-qualified freshwater mint has a supported freshwater-material genus, but experimental microcosm ENVO01000621 denotes a vivarium rather than a kind of water. Later exact BioSamples describe pond water incubated in microcosm media. Remove only the context parent; the separate emitted narrowMatch endpoint-contract mismatch remains unresolved.

## Scope And Provenance

Entire exact HabitatRecord, contributor provenance, direct-parent meaning and applicable biological evidence.

Selection: Next 24 alphabetically ordered unreviewed ENGINEERED records, from engineered__900b76ad through fruit_processing; separate exact-target record reviews, not a sample or category verdict. Starting current coverage303/3208.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 435a217c6d378e013e2ee11f22147e5b09737183.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.d482ddbf80 | data/habitats/engineered/freshwater__0ce4d27d.yaml | generated | Freshwater |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:GOLD.d482ddbf80 | Actual exit0; start 2026-10-11T10:10:30.161151Z; finish 2026-10-11T10:10:32.871557Z. Full-corpus procedural checks are not additional scientific coverage. |
| Native validate-strict | passed | True | habitatmech:GOLD.d482ddbf80 | Actual exit0; start 2026-10-11T10:10:43.887582Z; finish 2026-10-11T10:10:52.258696Z. Full-corpus procedural checks are not additional scientific coverage. |
| Native verify-corpus | passed | True | habitatmech:GOLD.d482ddbf80 | Actual exit0; start 2026-10-11T10:10:52.259836Z; finish 2026-10-11T10:11:06.554044Z. Full-corpus procedural checks are not additional scientific coverage. |
| Native validate-products | passed | True | habitatmech:GOLD.d482ddbf80 | Actual exit0; start 2026-10-11T10:11:06.554814Z; finish 2026-10-11T10:11:55.255958Z. Full-corpus procedural checks are not additional scientific coverage. |
| Native validate-history | passed | True | habitatmech:GOLD.d482ddbf80 | Actual exit0; start 2026-10-11T10:11:55.256933Z; finish 2026-10-11T10:12:06.655006Z. Full-corpus procedural checks are not additional scientific coverage. |
| Native validate-causal-all | passed | True | habitatmech:GOLD.d482ddbf80 | Actual exit0; start 2026-10-11T10:12:06.656051Z; finish 2026-10-11T10:12:15.551857Z. Full-corpus procedural checks are not additional scientific coverage. |
| Native term-requests-check | passed | True | habitatmech:GOLD.d482ddbf80 | Actual exit0; start 2026-10-11T10:12:15.553494Z; finish 2026-10-11T10:12:44.715204Z. Full-corpus procedural checks are not additional scientific coverage. |
| Complete target reproduction | passed | False | habitatmech:GOLD.d482ddbf80 | All24 selected native build_document results equal every current target field. |
| Original source membership reconstruction | unavailable | False | habitatmech:GOLD.d482ddbf80 | Configured original input paths unavailable within ignored-inclusive bounds. Later official exports are separate evidence. |
| Publication QC | skipped | False | habitatmech:GOLD.d482ddbf80 | Full QC is still running when authoring this observation. No future success is asserted; required focused/native gates above have completed. |

## Scientific And Domain Assessments

### Identity, grounding, genus and synonym scope

identity: concern. Targets: habitatmech:GOLD.d482ddbf80.

The microcosm-qualified freshwater mint has a supported freshwater-material genus, but experimental microcosm ENVO01000621 denotes a vivarium rather than a kind of water. Later exact BioSamples describe pond water incubated in microcosm media. Remove only the context parent; the separate emitted narrowMatch endpoint-contract mismatch remains unresolved.

### Frozen source counts, roles and lifecycle

provenance: supported. Targets: habitatmech:GOLD.d482ddbf80.

Every emitted field reproduces from the maintained inputs. Frozen counts and nodes trace to exact inventory rows; zero-count omission is not evidence of biological absence. Actual source/reviewed-source counts and routes={"source_concepts": 1, "reviewed_sources": 0, "routes": [{"path": "Engineered &gt; Artificial ecosystem &gt; Microcosm &gt; Freshwater", "automatic": {"identifier": "habitatmech:GOLD.d482ddbf80", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["ENVO:00002011"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}, "actual": {"identifier": "habitatmech:GOLD.d482ddbf80", "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["ENVO:00002011"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null, "reviewed": false, "decision": null}}]}. Later sample/organism counts remain separate. Native status is not promoted by this scientific review.

### Evidence proportional to actual claims

completeness: supported. Targets: habitatmech:GOLD.d482ddbf80.

No target has causal-edge, gene/regulator or transcriptomic claims; iModulonDB is not applicable. No optional definition, parameter, mechanism, discussion or dataset is invented for coverage. Triad roles remain broad/local/medium context rather than automatic identity evidence.

## Findings

### F1: Containing room or experimental enclosure is emitted as a strict parent

major / open / confirmed; issue key: habitatmech-gold.d482ddbf80-context-parent.

The microcosm-qualified freshwater mint has a supported freshwater-material genus, but experimental microcosm ENVO01000621 denotes a vivarium rather than a kind of water. Later exact BioSamples describe pond water incubated in microcosm media. Remove only the context parent; the separate emitted narrowMatch endpoint-contract mismatch remains unresolved. Unsupported contribution: ENVO:01000621.

### F2: Narrow-match route compares a parent rather than the declared attestation endpoint

major / open / confirmed; issue key: habitatmech-gold.d482ddbf80-mapping-endpoint-contract.

The executed gold_narrower_than_leaf_match route retains the source mint as the record identifier, adds ENVO:00002011 as parent, and emits NARROW/skos:narrowMatch. The schema defines mapping_predicate as source-to-record and omits it when the record is the source. The ontology parent is not that declared endpoint. This is an application-contract mismatch, not a claim that SKOS forbids hierarchical self-links.

## Recommended Actions And Acceptance Checks

### A1

Exclude only this GOLD context-parent contribution with the exact source path and expected resolved parent. Preserve identity, independent freshwater genus where present, source counts/units, statuses and prior history. Do not invent a replacement definition.

- Adjudicate the exact source with primary evidence; do not invent a replacement or infer ecological absence.
- Preserve source counts/units and immutable review/history records; append native curation history for supported changes.
- Add focused regression coverage, dry seed and inspect a canary, regenerate only affected products, and pass provenance, labels, strict validation, reproduction, history and full QC.

### A2

Resolve shared #1398 across producer, schema and actual consumers with explicit endpoints and export regression tests. Preserve source identity and genuine water parent; a predicate swap or context-parent exclusion alone does not fix it.

- Adjudicate the exact source with primary evidence; do not invent a replacement or infer ecological absence.
- Preserve source counts/units and immutable review/history records; append native curation history for supported changes.
- Add focused regression coverage, dry seed and inspect a canary, regenerate only affected products, and pass provenance, labels, strict validation, reproduction, history and full QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/engineered/freshwater__0ce4d27d.yaml; Entire generated YAML, including all history, synonym and taxon entries | supports | The microcosm-qualified freshwater mint has a supported freshwater-material genus, but experimental microcosm ENVO01000621 denotes a vivarium rather than a kind of water. Later exact BioSamples describe pond water incubated in microcosm media. Remove only the context parent; the separate emitted narrowMatch endpoint-contract mismatch remains unresolved. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md; Native field-by-field checklist and maintained-input ownership | supports | Applied identity, strictly broader parent, ITEM status, observational taxon, source-unit, triad-role and causal-evidence rules. Optional absent fields do not require invented content. |
| RAW | data/raw; curation/decisions.tsv; curation/gold_parent_exclusions.tsv; Exact source inventory, ontology and decision rows | supports | {"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Engineered &gt; Artificial ecosystem &gt; Microcosm &gt; Freshwater", "depth": "4", "ecosystem": "Engineered", "ecosystem_category": "Artificial ecosystem", "ecosystem_subtype": "Freshwater", "ecosystem_type": "Microcosm", "gold_node_count": "2", "gold_node_ids": "gold.ecosystem:8263&#124;gold.ecosystem:8264", "leaf_label": "Freshwater", "organism_count": "0", "specific_ecosystem": "", "study_count": "0", "total_assertions": "0"}, "logical_row": 1137}]}. Logical TSV row ordinals include the header; these are exact target/mint/path rows, not wholesale assessment of neighboring records. |
| CODE | src/habitatmech/seed.py; Complete target reconstruction and actual resolve_gold/apply_decision results | supports | {"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:00002011"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.d482ddbf80", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:00002011"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.d482ddbf80", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "path": "Engineered &gt; Artificial ecosystem &gt; Microcosm &gt; Freshwater"}], "source_concepts": 1}. Native build_document reproduces the whole target. Mapping predicates retain the actual executed route. |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Typed synonyms, labels, definitions, deprecation, named parents and restrictions | supports | {"ENVO:00002011": {"definition": ["Water which has a low concentration of dissolved solutes, particularly that of sodium chloride."], "deprecated": [], "label": ["fresh water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006"], "restrictions": [], "synonyms": {"Broad": [], "Exact": ["freshwater"], "Narrow": [], "Related": ["sweet water"]}}, "ENVO:01000621": {"definition": ["A microcosm is a vivarium within which a simple ecosystem is artificially established and used to simulate and predict the behaviour of natural ecosystems under controlled conditions."], "deprecated": [], "label": ["microcosm"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00010622"], "restrictions": [], "synonyms": {"Broad": [], "Exact": [], "Narrow": [], "Related": []}}}. Current primary RDF confirms these exact terms; ontology meaning is not an independently proven GOLD crosswalk. |
| PARENT | data/habitats; data/raw/ontology_subclass_edges.tsv; Direct-parent identity projection | supports | {"ENVO:00002011": {"definition": "Water which has a low concentration of dissolved solutes, particularly that of sodium chloride.", "identifier": "ENVO:00002011", "label": "fresh water", "parent_habitats": ["ENVO:00002006", "ENVO:00002030"], "source_attestations": [{"notes": "Physicochemical parameter bands from kg-microbe's environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "water_fresh", "source_label": "water_fresh"}, {"assertion_count": 2055, "assertion_unit": "ORGANISM", "mapping_predicate": "skos:closeMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:3488", "source_label": "Freshwater", "source_path": "Environmental &gt; Aquatic &gt; Freshwater"}, {"assertion_count": 645, "assertion_unit": "TAXON", "source": "MADIN", "source_id": "ENVO:00002011", "source_label": "fresh water"}, {"assertion_count": 4936, "assertion_unit": "TAXON", "evidence_channels": "annotated_genomes_isolates&#124;environmental_samples", "score": 4.0, "source": "PREGO", "source_id": "ENVO:00002011", "source_label": "fresh water"}]}, "ENVO:01000621": {"definition": "A microcosm is a vivarium within which a simple ecosystem is artificially established and used to simulate and predict the behaviour of natural ecosystems under controlled conditions.", "identifier": "ENVO:01000621", "label": "microcosm", "parent_habitats": ["ENVO:00010622", "habitatmech:GOLD.0acae9a1a4"], "source_attestations": [{"mapping_predicate": "skos:exactMatch", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:8179", "source_label": "Microcosm", "source_path": "Engineered &gt; Artificial ecosystem &gt; Microcosm"}]}}. Direct-parent identity and source context only, not additional full-record scientific coverage. |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; Exact five-position ecosystem tuples; first three BioSample/Organism descriptions per target | supports | Retained official 09-Oct export, not a new download or original frozen-membership reconstruction. Complete sheet census including headers={"Biosample": 244951, "Organism": 532019, "SequencingProject": 636914, "Study": 63806}; target exact tuple match counts={"Biosample": 94, "Organism": 0, "SequencingProject": 94}; inspected first three member descriptions per sheet={"Biosample": [{"data": {"BIOSAMPLE GOLD ID": "Gb0389614", "BIOSAMPLE NAME": "Freshwater pond microcosm microbial communities from Marine Biological Laboratory, The University of Chicago, Falmouth, MA, USA - MC1-C12-TB2", "BIOSAMPLE NCBI TAX NAME": "pond metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "pond water incubated in a microcosm media"}, "row": 215164}, {"data": {"BIOSAMPLE GOLD ID": "Gb0389615", "BIOSAMPLE NAME": "Freshwater pond microcosm microbial communities from Marine Biological Laboratory, The University of Chicago, Falmouth, MA, USA - MC1-C12-TB3", "BIOSAMPLE NCBI TAX NAME": "pond metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "pond water incubated in a microcosm media"}, "row": 215165}, {"data": {"BIOSAMPLE GOLD ID": "Gb0389616", "BIOSAMPLE NAME": "Freshwater pond microcosm microbial communities from Marine Biological Laboratory, The University of Chicago, Falmouth, MA, USA - MC1-C12-TB5", "BIOSAMPLE NCBI TAX NAME": "pond metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "pond water incubated in a microcosm media"}, "row": 215166}], "Organism": []}. Further rows and joined projects/studies are inventoried, not all scientifically assessed. |
| CLASS | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Five-position tuple with Unclassified retained as an empty position | supports | Fresh current classification, 2422 rows including header; exact target rows=[{"row": 41, "slug": "freshwater__0ce4d27d", "values": ["8264", "Engineered", "Artificial ecosystem", "Microcosm", "Freshwater", "Unclassified"]}]. A miss is bounded to this snapshot and does not establish habitat absence. |
| SEARCH | curation; data/raw; data/habitats; history; research; reports; reviews; conf; Captured support-search ledger and exact maintained-row search | supports | Ignored/hidden-inclusive rg searched target IDs, labels, slugs, source IDs and paths. Root raw/curation TSVs were structurally scanned and causal-overlay identifiers checked. No prior structured review targeted this exact ID at capture. Original configured source search={"/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold": {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold: IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold: No such file or directory (os error 2)\n"}, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive": {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive: IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive: No such file or directory (os error 2)\n"}, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego": {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego: IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego: No such file or directory (os error 2)\n"}, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/ontologies": {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/ontologies: IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/ontologies: No such file or directory (os error 2)\n"}}. Configured-path ENOENT is not global absence. |

## Limits And Additional Notes

- Original assertion-level inputs were not recovered. Later GOLD counts do not replace frozen counts or prove original membership.
- Only explicitly identified passages and member fields were scientifically inspected; the complete workbook census is not complete member-level verification.
- Sparse source bins remain qualified source representations. No optional content or native REVIEWED status is created by a qualified pass.
- No required focused/native gate was unavailable. Full publication QC is pending in this immutable observation.
- This review does not certify SSSOM/KGX readiness, resolve shared #1398, or close prior GitHub findings.
- The corpus-wide review goal remains incomplete.
- Legacy reports inform search leads, not automatically converted verdicts. Publication and supported remediation are separately authorized by the current user request.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T102025Z-freshwater__0ce4d27d
kind: record
repository: culturebotai/HabitatMech
title: 'Scientific record review: freshwater__0ce4d27d'
started_at: '2026-10-11T10:09:21.217672Z'
finished_at: '2026-10-11T10:20:25.911866Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Continuing agent participated in prior reviews and curation;
    adversarial self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The microcosm-qualified freshwater mint has a supported freshwater-material
  genus, but experimental microcosm ENVO01000621 denotes a vivarium rather than a
  kind of water. Later exact BioSamples describe pond water incubated in microcosm
  media. Remove only the context parent; the separate emitted narrowMatch endpoint-contract
  mismatch remains unresolved.
source:
  git_revision: 435a217c6d378e013e2ee11f22147e5b09737183
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
  - path: curation/causal_graphs/agricultural_soil.yaml
    sha256: 2f9c73b186d6b79df1d64098f929d8364a1768f732101edaf144dee7723c60f4
    role: context
  - path: curation/causal_graphs/aquatic_biome.yaml
    sha256: 03ba09d10f9a9d8d32060fc0208b511ef0d59e731fd7c63ca6c02296e70da5f5
    role: context
  - path: curation/causal_graphs/biofilm.yaml
    sha256: 37fae9d123c2edfb68376b6b4fe5441f72092d48d81dba6f60510087217c8680
    role: context
  - path: curation/causal_graphs/bioreactor.yaml
    sha256: 170d1134c3de38348844e45dbf6d87663dd4a0d1f33fd9e441a4352b6e277583
    role: context
  - path: curation/causal_graphs/brackish_water.yaml
    sha256: b9d58082a53bef1143a3868918cfed7f6d74ba7e2330648069733d9ea2c76508
    role: context
  - path: curation/causal_graphs/building.yaml
    sha256: 9e9360775fdda554b285d7ecfb9b1729bf389b8241376a410eca60bd672eb235
    role: context
  - path: curation/causal_graphs/compost.yaml
    sha256: e0fd3ae54311115939f07ba1f3f158c5c44353bd0fab1dcdc1a9292ff0ad1de5
    role: context
  - path: curation/causal_graphs/deep_marine_sediment.yaml
    sha256: eb6a68290a58ec157a4c9895e082cbba760c47b5fbe35523d3bb163af3091d0c
    role: context
  - path: curation/causal_graphs/forest_soil.yaml
    sha256: faef7b6c26c25ba33110d362dc7e4351440bc08c1106f270e1e6f2decfb1e3f4
    role: context
  - path: curation/causal_graphs/forested_area.yaml
    sha256: eb96b992e1ee8fef7df2550c765a30f0d446082ce16592b6c1da44a54b34e427
    role: context
  - path: curation/causal_graphs/fresh_water.yaml
    sha256: e95ea96aa1912066d4c98cbff91e34528668d4c453d93dc4203c67e7769c691a
    role: context
  - path: curation/causal_graphs/fungi_associated_environment.yaml
    sha256: 45736893315a37e327c25d401ff8794fee47b1056347e52f4980bc3a58e8e0d8
    role: context
  - path: curation/causal_graphs/grassland_soil.yaml
    sha256: 81b2a9ea6255dfbd4b393102b9903dd3c9e8af12f7d3a9adc7c4649650542ae8
    role: context
  - path: curation/causal_graphs/hot_spring.yaml
    sha256: ee0f6d7f7eff179b44e1e934c1c801524062a7e71f3199e16e9ef35e7bad81ed
    role: context
  - path: curation/causal_graphs/hydrothermal_vent.yaml
    sha256: b5c101a93e724531cb7e50e8031203138230c09599855fe8a03bec945469efb0
    role: context
  - path: curation/causal_graphs/hypersaline_water.yaml
    sha256: e974d5e9cc241ac9daf3542ba11156915cfb7786e683ad5ad212af5b35006158
    role: context
  - path: curation/causal_graphs/intestine_environment.yaml
    sha256: 2ef766692eff55471a3322c0cd1cf82188decf37fd5ecd3535cb0ef612e2b725
    role: context
  - path: curation/causal_graphs/leaf.yaml
    sha256: fadc8027b39884bc16cf98f774804a84fd1b1d805876310a47a095f6019435cc
    role: context
  - path: curation/causal_graphs/liquid_water.yaml
    sha256: 12aac1021b9b51c6becc4ef8509bd63557b306e42c01d9b4443d69252ce29a81
    role: context
  - path: curation/causal_graphs/marine_sediment.yaml
    sha256: 8b230eb079171ab8134b648caa29878dc5015fb36362559a6a8c67fb2b433741
    role: context
  - path: curation/causal_graphs/marine_water_body.yaml
    sha256: b2f81102970e9541bf61978fabdd68b7db8f9459f1ef11b467fecfc2956f238b
    role: context
  - path: curation/causal_graphs/milk.yaml
    sha256: 049daa5b499096c61cb625b7bb9ac0f02ea216c96d6b5f7b77126c8709b2378d
    role: context
  - path: curation/causal_graphs/peat_soil.yaml
    sha256: 0f23fa02718b08e3607478ceaa2294320b320ae841a79e144e48ed3497db09e2
    role: context
  - path: curation/causal_graphs/plant_associated_environment.yaml
    sha256: 300044040f76234e7ed3bf373137ba224e55f48e3f3d6d505086b3830877cfcb
    role: context
  - path: curation/causal_graphs/plant_litter.yaml
    sha256: 25e10d6640992be2aa506490f763d8f9642fde125f599207dae7852b6a13b369
    role: context
  - path: curation/causal_graphs/root_nodule.yaml
    sha256: b363e5d418df93d6e44c9d3f3256c8b0ede7c4518125359ffb880020fc00721c
    role: context
  - path: curation/causal_graphs/sea_water.yaml
    sha256: 240ffc8ad2c0abf6f4cce41e01018679aca726816006c90ce329b8d1910d9cd7
    role: context
  - path: curation/causal_graphs/sediment.yaml
    sha256: 62b97afba9466dc64f8b5b1b3fd5d92f8b4b6bf96fe1c761af579ff7deca0e47
    role: context
  - path: curation/causal_graphs/sludge.yaml
    sha256: 55b9c9a27fd00c7b84a8780f2cedc83eeb31ebdda9a2e1029678d96a7fa4a06c
    role: context
  - path: curation/causal_graphs/soil.yaml
    sha256: 2a2bf4b1099b3bc69015f9530cf6e926c05c33667132234b3c52f06aacc957c2
    role: context
  - path: curation/causal_graphs/terrestrial_biome.yaml
    sha256: 239e6a2b711564ed12084cddd1295547d23858dd329c33c538251d5f53c88834
    role: context
  - path: curation/causal_graphs/waste_water.yaml
    sha256: 299b5128af6cf5f7a61ce53304f1084e6eb045414b47cbcfd8832de095142aef
    role: context
  - path: curation/decisions.tsv
    sha256: c2482c7441b08f593baa8bd59546ac68c6e5c7e4e1cb36c24c12a74592b9ff3c
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 45e4ff459e76b9c8eee63dcd86c153ab139491a828e03d5f9652da4c6a930589
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 3f2ce04805defe5ff65dc20988cc72bc94d4636b3140eb1311017866bdc0ea0a
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/aquatic/fresh_water.yaml
    sha256: fc60c1fc64ceea8fdf8d2d294dc96c855aa3793962f818e9cdd1b9b3cb87d1be
    role: context
  - path: data/habitats/engineered/freshwater__0ce4d27d.yaml
    sha256: 2ab06038fb90de9c3e8fa7cd594a7a6f163c9076f2ec49cb81a8259dbd8c16ff
    role: target
  - path: data/habitats/engineered/microcosm.yaml
    sha256: c7d419660d9b429df2150353515da454216144805cbf7004787cdc4735ba0952
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
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260925T050203Z-freshwater__0ce4d27d.md
    sha256: 89b1f43cf7255880b025f487c68b02d6b51a0cfe1dda7a10b315e6ab7c029eda
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/extract_source_inventory.py
    sha256: 4bf5391d25ff48a2d81eb3821af6582de063fd0391440973d309dfd93016490c
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
scope:
  description: Entire exact HabitatRecord, contributor provenance, direct-parent meaning
    and applicable biological evidence.
  selection: Next 24 alphabetically ordered unreviewed ENGINEERED records, from engineered__900b76ad
    through fruit_processing; separate exact-target record reviews, not a sample or
    category verdict. Starting current coverage303/3208.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.d482ddbf80
  exclusions:
  - target: Other3207 current HabitatRecords
    reason: Context is not additional full-record scientific review.
targets:
- target_id: habitatmech:GOLD.d482ddbf80
  path: data/habitats/engineered/freshwater__0ce4d27d.yaml
  label: Freshwater
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Exact source-concept grounding and identity decisions
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded GOLD context-parent contributions
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: Authored habitat definition and genus
  - repository: culturebotai/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology identities, labels, definitions and parent axioms
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained harmonization and deterministic generation
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD paths, node IDs and ORGANISM counts
checks:
- check_id: C19
  name: Native validate
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T10:10:30.161151Z; finish 2026-10-11T10:10:32.871557Z.
    Full-corpus procedural checks are not additional scientific coverage.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate
    data/habitats/engineered/freshwater__0ce4d27d.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C24
  name: Native validate-strict
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T10:10:43.887582Z; finish 2026-10-11T10:10:52.258696Z.
    Full-corpus procedural checks are not additional scientific coverage.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-strict
    data/habitats/engineered/engineered__900b76ad.yaml data/habitats/engineered/engineered_product__d2d22ac0.yaml
    data/habitats/engineered/external_surfaces.yaml data/habitats/engineered/factory.yaml
    data/habitats/engineered/feedlot.yaml data/habitats/engineered/feedstock.yaml
    data/habitats/engineered/fermentation.yaml data/habitats/engineered/fermentation__cbf94220.yaml
    data/habitats/engineered/fermentation_pit.yaml data/habitats/engineered/filter.yaml
    data/habitats/engineered/fish_pen.yaml data/habitats/engineered/fish_pond.yaml
    data/habitats/engineered/fish_tank.yaml data/habitats/engineered/floor.yaml data/habitats/engineered/floor__86528402.yaml
    data/habitats/engineered/floor__bcd0ae16.yaml data/habitats/engineered/food_waste.yaml
    data/habitats/engineered/fresh_manure.yaml data/habitats/engineered/fresh_water_aquarium.yaml
    data/habitats/engineered/freshwater__0ce4d27d.yaml data/habitats/engineered/freshwater__fec74bd2.yaml
    data/habitats/engineered/freshwater_debries.yaml data/habitats/engineered/freshwater_ras.yaml
    data/habitats/engineered/fruit_processing.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C25
  name: Native verify-corpus
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T10:10:52.259836Z; finish 2026-10-11T10:11:06.554044Z.
    Full-corpus procedural checks are not additional scientific coverage.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C26
  name: Native validate-products
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T10:11:06.554814Z; finish 2026-10-11T10:11:55.255958Z.
    Full-corpus procedural checks are not additional scientific coverage.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C27
  name: Native validate-history
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T10:11:55.256933Z; finish 2026-10-11T10:12:06.655006Z.
    Full-corpus procedural checks are not additional scientific coverage.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C28
  name: Native validate-causal-all
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T10:12:06.656051Z; finish 2026-10-11T10:12:15.551857Z.
    Full-corpus procedural checks are not additional scientific coverage.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: C29
  name: Native term-requests-check
  status: passed
  required: true
  summary: Actual exit0; start 2026-10-11T10:12:15.553494Z; finish 2026-10-11T10:12:44.715204Z.
    Full-corpus procedural checks are not additional scientific coverage.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
- check_id: REPRO
  name: Complete target reproduction
  status: passed
  required: false
  summary: All24 selected native build_document results equal every current target
    field.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  command: .venv/bin/python /private/tmp/habitatmech-review-ap-local.py
  exit_code: 0
  evidence_ids:
  - CODE
- check_id: ORIGINAL
  name: Original source membership reconstruction
  status: unavailable
  required: false
  summary: Configured original input paths unavailable within ignored-inclusive bounds.
    Later official exports are separate evidence.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  evidence_ids:
  - SEARCH
- check_id: QC
  name: Publication QC
  status: skipped
  required: false
  summary: Full QC is still running when authoring this observation. No future success
    is asserted; required focused/native gates above have completed.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/engineered/freshwater__0ce4d27d.yaml
  summary: The microcosm-qualified freshwater mint has a supported freshwater-material
    genus, but experimental microcosm ENVO01000621 denotes a vivarium rather than
    a kind of water. Later exact BioSamples describe pond water incubated in microcosm
    media. Remove only the context parent; the separate emitted narrowMatch endpoint-contract
    mismatch remains unresolved.
  locator: Entire generated YAML, including all history, synonym and taxon entries
  accessed_at: '2026-10-11T10:20:25.911866Z'
  support: supports
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md
  summary: Applied identity, strictly broader parent, ITEM status, observational taxon,
    source-unit, triad-role and causal-evidence rules. Optional absent fields do not
    require invented content.
  locator: Native field-by-field checklist and maintained-input ownership
  accessed_at: '2026-10-11T10:20:25.911866Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0",
    "canonical_path": "Engineered > Artificial ecosystem > Microcosm > Freshwater",
    "depth": "4", "ecosystem": "Engineered", "ecosystem_category": "Artificial ecosystem",
    "ecosystem_subtype": "Freshwater", "ecosystem_type": "Microcosm", "gold_node_count":
    "2", "gold_node_ids": "gold.ecosystem:8263|gold.ecosystem:8264", "leaf_label":
    "Freshwater", "organism_count": "0", "specific_ecosystem": "", "study_count":
    "0", "total_assertions": "0"}, "logical_row": 1137}]}. Logical TSV row ordinals
    include the header; these are exact target/mint/path rows, not wholesale assessment
    of neighboring records.'
  locator: Exact source inventory, ontology and decision rows
  accessed_at: '2026-10-11T10:20:25.911866Z'
  support: supports
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": ["ENVO:00002011"], "extra_xrefs": [],
    "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.d482ddbf80", "mapping_predicate":
    "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"},
    "automatic": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": ["ENVO:00002011"], "extra_xrefs": [], "grounding_status": "NARROW",
    "identifier": "habitatmech:GOLD.d482ddbf80", "mapping_predicate": "skos:narrowMatch",
    "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "path": "Engineered
    > Artificial ecosystem > Microcosm > Freshwater"}], "source_concepts": 1}. Native
    build_document reproduces the whole target. Mapping predicates retain the actual
    executed route.'
  locator: Complete target reconstruction and actual resolve_gold/apply_decision results
  accessed_at: '2026-10-11T10:20:25.911866Z'
  support: supports
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl
  summary: '{"ENVO:00002011": {"definition": ["Water which has a low concentration
    of dissolved solutes, particularly that of sodium chloride."], "deprecated": [],
    "label": ["fresh water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006"],
    "restrictions": [], "synonyms": {"Broad": [], "Exact": ["freshwater"], "Narrow":
    [], "Related": ["sweet water"]}}, "ENVO:01000621": {"definition": ["A microcosm
    is a vivarium within which a simple ecosystem is artificially established and
    used to simulate and predict the behaviour of natural ecosystems under controlled
    conditions."], "deprecated": [], "label": ["microcosm"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00010622"],
    "restrictions": [], "synonyms": {"Broad": [], "Exact": [], "Narrow": [], "Related":
    []}}}. Current primary RDF confirms these exact terms; ontology meaning is not
    an independently proven GOLD crosswalk.'
  locator: Typed synonyms, labels, definitions, deprecation, named parents and restrictions
  accessed_at: '2026-10-11T10:10:30.391898Z'
  support: supports
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats; data/raw/ontology_subclass_edges.tsv
  summary: '{"ENVO:00002011": {"definition": "Water which has a low concentration
    of dissolved solutes, particularly that of sodium chloride.", "identifier": "ENVO:00002011",
    "label": "fresh water", "parent_habitats": ["ENVO:00002006", "ENVO:00002030"],
    "source_attestations": [{"notes": "Physicochemical parameter bands from kg-microbe''s
    environment table.", "source": "ENVIRONMENTS_TABLE", "source_id": "water_fresh",
    "source_label": "water_fresh"}, {"assertion_count": 2055, "assertion_unit": "ORGANISM",
    "mapping_predicate": "skos:closeMatch", "notes": "3 GOLD ecosystem node ids share
    this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD",
    "source_id": "gold.ecosystem:3488", "source_label": "Freshwater", "source_path":
    "Environmental > Aquatic > Freshwater"}, {"assertion_count": 645, "assertion_unit":
    "TAXON", "source": "MADIN", "source_id": "ENVO:00002011", "source_label": "fresh
    water"}, {"assertion_count": 4936, "assertion_unit": "TAXON", "evidence_channels":
    "annotated_genomes_isolates|environmental_samples", "score": 4.0, "source": "PREGO",
    "source_id": "ENVO:00002011", "source_label": "fresh water"}]}, "ENVO:01000621":
    {"definition": "A microcosm is a vivarium within which a simple ecosystem is artificially
    established and used to simulate and predict the behaviour of natural ecosystems
    under controlled conditions.", "identifier": "ENVO:01000621", "label": "microcosm",
    "parent_habitats": ["ENVO:00010622", "habitatmech:GOLD.0acae9a1a4"], "source_attestations":
    [{"mapping_predicate": "skos:exactMatch", "notes": "3 GOLD ecosystem node ids
    share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source":
    "GOLD", "source_id": "gold.ecosystem:8179", "source_label": "Microcosm", "source_path":
    "Engineered > Artificial ecosystem > Microcosm"}]}}. Direct-parent identity and
    source context only, not additional full-record scientific coverage.'
  locator: Direct-parent identity projection
  accessed_at: '2026-10-11T10:20:25.911866Z'
  support: supports
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  summary: 'Retained official 09-Oct export, not a new download or original frozen-membership
    reconstruction. Complete sheet census including headers={"Biosample": 244951,
    "Organism": 532019, "SequencingProject": 636914, "Study": 63806}; target exact
    tuple match counts={"Biosample": 94, "Organism": 0, "SequencingProject": 94};
    inspected first three member descriptions per sheet={"Biosample": [{"data": {"BIOSAMPLE
    GOLD ID": "Gb0389614", "BIOSAMPLE NAME": "Freshwater pond microcosm microbial
    communities from Marine Biological Laboratory, The University of Chicago, Falmouth,
    MA, USA - MC1-C12-TB2", "BIOSAMPLE NCBI TAX NAME": "pond metagenome", "BIOSAMPLE
    SAMPLE COLLECTION SITE": "pond water incubated in a microcosm media"}, "row":
    215164}, {"data": {"BIOSAMPLE GOLD ID": "Gb0389615", "BIOSAMPLE NAME": "Freshwater
    pond microcosm microbial communities from Marine Biological Laboratory, The University
    of Chicago, Falmouth, MA, USA - MC1-C12-TB3", "BIOSAMPLE NCBI TAX NAME": "pond
    metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "pond water incubated in a microcosm
    media"}, "row": 215165}, {"data": {"BIOSAMPLE GOLD ID": "Gb0389616", "BIOSAMPLE
    NAME": "Freshwater pond microcosm microbial communities from Marine Biological
    Laboratory, The University of Chicago, Falmouth, MA, USA - MC1-C12-TB5", "BIOSAMPLE
    NCBI TAX NAME": "pond metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "pond water
    incubated in a microcosm media"}, "row": 215166}], "Organism": []}. Further rows
    and joined projects/studies are inventoried, not all scientifically assessed.'
  locator: Exact five-position ecosystem tuples; first three BioSample/Organism descriptions
    per target
  accessed_at: '2026-10-11T10:20:25.911866Z'
  support: supports
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: CLASS
  kind: authority
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  summary: 'Fresh current classification, 2422 rows including header; exact target
    rows=[{"row": 41, "slug": "freshwater__0ce4d27d", "values": ["8264", "Engineered",
    "Artificial ecosystem", "Microcosm", "Freshwater", "Unclassified"]}]. A miss is
    bounded to this snapshot and does not establish habitat absence.'
  locator: Five-position tuple with Unclassified retained as an empty position
  accessed_at: '2026-10-11T10:10:41.220214Z'
  support: supports
  snapshot_sha256: 78ed6ce1c3799a2d6ef2d17e4a9eeee5da48eef78df0b71079c0f942555e5e7d
- evidence_id: SEARCH
  kind: search
  reference: curation; data/raw; data/habitats; history; research; reports; reviews;
    conf
  summary: 'Ignored/hidden-inclusive rg searched target IDs, labels, slugs, source
    IDs and paths. Root raw/curation TSVs were structurally scanned and causal-overlay
    identifiers checked. No prior structured review targeted this exact ID at capture.
    Original configured source search={"/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold":
    {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold:
    No such file or directory (os error 2)\n"}, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive":
    {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive:
    No such file or directory (os error 2)\n"}, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego":
    {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego:
    No such file or directory (os error 2)\n"}, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/ontologies":
    {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/ontologies:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/ontologies:
    No such file or directory (os error 2)\n"}}. Configured-path ENOENT is not global
    absence.'
  locator: Captured support-search ledger and exact maintained-row search
  accessed_at: '2026-10-11T10:20:25.911866Z'
  support: supports
  search_scope: 'Ignored/hidden-inclusive rg searched target IDs, labels, slugs, source
    IDs and paths. Root raw/curation TSVs were structurally scanned and causal-overlay
    identifiers checked. No prior structured review targeted this exact ID at capture.
    Original configured source search={"/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold":
    {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold:
    No such file or directory (os error 2)\n"}, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive":
    {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive:
    No such file or directory (os error 2)\n"}, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego":
    {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego:
    No such file or directory (os error 2)\n"}, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/ontologies":
    {"exit_code": 2, "stdout": "", "stderr": "rg: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/ontologies:
    IO error for operation on /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/ontologies:
    No such file or directory (os error 2)\n"}}. Configured-path ENOENT is not global
    absence.'
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Identity, grounding, genus and synonym scope
  outcome: concern
  summary: The microcosm-qualified freshwater mint has a supported freshwater-material
    genus, but experimental microcosm ENVO01000621 denotes a vivarium rather than
    a kind of water. Later exact BioSamples describe pond water incubated in microcosm
    media. Remove only the context parent; the separate emitted narrowMatch endpoint-contract
    mismatch remains unresolved.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  evidence_ids:
  - R
  - RAW
  - CODE
  - ONT
  - PARENT
- assessment_id: PROVENANCE
  area: provenance
  topic: Frozen source counts, roles and lifecycle
  outcome: supported
  summary: 'Every emitted field reproduces from the maintained inputs. Frozen counts
    and nodes trace to exact inventory rows; zero-count omission is not evidence of
    biological absence. Actual source/reviewed-source counts and routes={"source_concepts":
    1, "reviewed_sources": 0, "routes": [{"path": "Engineered > Artificial ecosystem
    > Microcosm > Freshwater", "automatic": {"identifier": "habitatmech:GOLD.d482ddbf80",
    "grounding_status": "NARROW", "mapping_predicate": "skos:narrowMatch", "contributes_grounding":
    true, "extra_parents": ["ENVO:00002011"], "extra_xrefs": [], "route": "gold_narrower_than_leaf_match",
    "category": null, "reviewed": false, "decision": null}, "actual": {"identifier":
    "habitatmech:GOLD.d482ddbf80", "grounding_status": "NARROW", "mapping_predicate":
    "skos:narrowMatch", "contributes_grounding": true, "extra_parents": ["ENVO:00002011"],
    "extra_xrefs": [], "route": "gold_narrower_than_leaf_match", "category": null,
    "reviewed": false, "decision": null}}]}. Later sample/organism counts remain separate.
    Native status is not promoted by this scientific review.'
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  evidence_ids:
  - R
  - RAW
  - CODE
- assessment_id: COMPLETENESS
  area: completeness
  topic: Evidence proportional to actual claims
  outcome: supported
  summary: No target has causal-edge, gene/regulator or transcriptomic claims; iModulonDB
    is not applicable. No optional definition, parameter, mechanism, discussion or
    dataset is invented for coverage. Triad roles remain broad/local/medium context
    rather than automatic identity evidence.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  evidence_ids:
  - R
  - RAW
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: habitatmech-gold.d482ddbf80-context-parent
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Containing room or experimental enclosure is emitted as a strict parent
  description: 'The microcosm-qualified freshwater mint has a supported freshwater-material
    genus, but experimental microcosm ENVO01000621 denotes a vivarium rather than
    a kind of water. Later exact BioSamples describe pond water incubated in microcosm
    media. Remove only the context parent; the separate emitted narrowMatch endpoint-contract
    mismatch remains unresolved. Unsupported contribution: ENVO:01000621.'
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  field_paths:
  - parent_habitats
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
  - BULK
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material identity, hierarchy, grounding scope or application
    contract requires maintained-input adjudication.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact-source guarded context-parent exclusion
- finding_id: F2
  issue_key: habitatmech-gold.d482ddbf80-mapping-endpoint-contract
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Narrow-match route compares a parent rather than the declared attestation
    endpoint
  description: The executed gold_narrower_than_leaf_match route retains the source
    mint as the record identifier, adds ENVO:00002011 as parent, and emits NARROW/skos:narrowMatch.
    The schema defines mapping_predicate as source-to-record and omits it when the
    record is the source. The ontology parent is not that declared endpoint. This
    is an application-contract mismatch, not a claim that SKOS forbids hierarchical
    self-links.
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  field_paths:
  - grounding_status
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - R
  - CODE
  - RULES
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material identity, hierarchy, grounding scope or application
    contract requires maintained-input adjudication.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Mapping producer and route
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Source-attestation endpoint contract
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: A1
  description: Exclude only this GOLD context-parent contribution with the exact source
    path and expected resolved parent. Preserve identity, independent freshwater genus
    where present, source counts/units, statuses and prior history. Do not invent
    a replacement definition.
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact-source guarded context-parent exclusion
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Adjudicate the exact source with primary evidence; do not invent a replacement
    or infer ecological absence.
  - Preserve source counts/units and immutable review/history records; append native
    curation history for supported changes.
  - Add focused regression coverage, dry seed and inspect a canary, regenerate only
    affected products, and pass provenance, labels, strict validation, reproduction,
    history and full QC.
- action_id: A2
  description: 'Resolve shared #1398 across producer, schema and actual consumers
    with explicit endpoints and export regression tests. Preserve source identity
    and genuine water parent; a predicate swap or context-parent exclusion alone does
    not fix it.'
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.d482ddbf80
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Mapping producer and route
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Source-attestation endpoint contract
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Adjudicate the exact source with primary evidence; do not invent a replacement
    or infer ecological absence.
  - Preserve source counts/units and immutable review/history records; append native
    curation history for supported changes.
  - Add focused regression coverage, dry seed and inspect a canary, regenerate only
    affected products, and pass provenance, labels, strict validation, reproduction,
    history and full QC.
limitations:
- Original assertion-level inputs were not recovered. Later GOLD counts do not replace
  frozen counts or prove original membership.
- Only explicitly identified passages and member fields were scientifically inspected;
  the complete workbook census is not complete member-level verification.
- Sparse source bins remain qualified source representations. No optional content
  or native REVIEWED status is created by a qualified pass.
- No required focused/native gate was unavailable. Full publication QC is pending
  in this immutable observation.
- 'This review does not certify SSSOM/KGX readiness, resolve shared #1398, or close
  prior GitHub findings.'
notes:
- The corpus-wide review goal remains incomplete.
- Legacy reports inform search leads, not automatically converted verdicts. Publication
  and supported remediation are separately authorized by the current user request.
tags:
- habitatmech
- engineered
- record-review
- scientific-review
```
