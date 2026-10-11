# Scientific record review: biomass__9d8a5aca

- Review: 20261011T051114Z-biomass__9d8a5aca
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T04:58:06.232106Z
- Finished UTC: 2026-10-11T05:11:14.128642Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

PNA anaerobic-zone Biomass denotes organic material, not the spatial zone it occupies. ENVO:01000155 remains a defensible broader material. The separate Anaerobic zone record describes location and has already had its own container parent excluded; that does not repair this child edge. The biomass-to-zone is-a and retained-mint mapping endpoint need correction. No uniform oxygenation, granule geometry or source-to-experiment crosswalk is established.

## Scope And Provenance

Every field of one exact generated HabitatRecord, its contributing source concepts, relevant parent meaning, and applicable causal evidence.

Selection: Next alphabetically ordered unreviewed engineered record in an explicit 16-record work sequence; independent report per exact identifier. Global starting coverage200/3208, not a cohort-wide verdict.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c287909e97d2953317a72ec85ec77dc5a43b7ea3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.497ed1acca | data/habitats/engineered/biomass__9d8a5aca.yaml | generated | Biomass |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:GOLD.497ed1acca | Exit0; started 2026-10-11T04:58:55.771337Z, finished 2026-10-11T04:58:58.151352Z. Target LinkML validation reported no issues. |
| Native validate-strict | passed | True | habitatmech:GOLD.497ed1acca | Exit0; started 2026-10-11T04:59:34.232262Z, finished 2026-10-11T04:59:45.248215Z. 16 selected files, zero errors. |
| Native verify-corpus | passed | True | habitatmech:GOLD.497ed1acca | Exit0; started 2026-10-11T04:59:45.249317Z, finished 2026-10-11T05:00:05.120376Z. 3,208 records reproduce exactly. |
| Native validate-products | passed | True | habitatmech:GOLD.497ed1acca | Exit0; started 2026-10-11T05:00:05.121701Z, finished 2026-10-11T05:00:50.713443Z. Label gate passed with 2,057 no-adapter skips; not a scientific or deprecation gate. |
| Native validate-history | passed | True | habitatmech:GOLD.497ed1acca | Exit0; started 2026-10-11T05:00:50.714268Z, finished 2026-10-11T05:00:56.739106Z. 302 history records valid. |
| Native validate-causal-all | passed | True | habitatmech:GOLD.497ed1acca | Exit0; started 2026-10-11T05:00:56.739825Z, finished 2026-10-11T05:01:01.766304Z. All 32 causal overlays valid. |
| Native term-requests-check | passed | True | habitatmech:GOLD.497ed1acca | Exit0; started 2026-10-11T05:01:01.767272Z, finished 2026-10-11T05:01:17.149018Z. 109 term requests current. |
| All-field target reproduction and actual source routes | passed | False | habitatmech:GOLD.497ed1acca | All 16 selected generated documents equal seed.build_document results, including every taxon, edge and history field. |
| Full publication QC | skipped | False | habitatmech:GOLD.497ed1acca | No maintained science or generated product changes in this read-only review. Full publication QC at the unchanged base was completed in the preceding publication; not rerun or presented as a fresh scientific check. Native gates above and review-check are used for this review-only output. |
| Original frozen source-member reconstruction | unavailable | False | habitatmech:GOLD.497ed1acca | Ignored-inclusive rg --files of the configured kg-microbe data/raw/gold path returned ENOENT (search exit2); source reconstruction could not run. This is bounded to that configured path, not a global absence claim. Frozen inventories and the separately hashed later export are available. |

## Scientific And Domain Assessments

### Exact source-qualified habitat meaning

identity: supported. Targets: habitatmech:GOLD.497ed1acca.

PNA anaerobic-zone Biomass denotes organic material, not the spatial zone it occupies. ENVO:01000155 remains a defensible broader material. The separate Anaerobic zone record describes location and has already had its own container parent excluded; that does not repair this child edge. The biomass-to-zone is-a and retained-mint mapping endpoint need correction. No uniform oxygenation, granule geometry or source-to-experiment crosswalk is established.

### Current source accounting and native mapping status

consistency: supported. Targets: habitatmech:GOLD.497ed1acca.

All fields reproduce from maintained inputs. Contributing concepts=1, ITEM-reviewed=0; generated mapping_status=SEEDED. The review neither endorses every inherited claim nor changes native status.

### Attestations, counts, units and later-member scope

provenance: supported. Targets: habitatmech:GOLD.497ed1acca.

Frozen source IDs, labels, paths, collapsed-node notes and organism counts match. Zero-count omission is not biological absence. Later BioSample/Organism records and joined studies are kept separate from frozen ORGANISM assertions and from any taxon pool. No MIxS triad, study observation or parent biology is automatically promoted to identity.

### Strictly broader genera versus contextual source parents

grounding: concern. Targets: habitatmech:GOLD.497ed1acca.

PNA anaerobic-zone Biomass denotes organic material, not the spatial zone it occupies. ENVO:01000155 remains a defensible broader material. The separate Anaerobic zone record describes location and has already had its own container parent excluded; that does not repair this child edge. The biomass-to-zone is-a and retained-mint mapping endpoint need correction. No uniform oxygenation, granule geometry or source-to-experiment crosswalk is established.

### Optional biology and structured-source applicability

completeness: not_applicable. Targets: habitatmech:GOLD.497ed1acca.

The target makes no taxon, parameter, causal-graph, gene, regulator, protein or organism/dataset expression-module claim. Optional biological fields need not be filled from neighboring records or studies. iModulonDB is not applicable to this declared claim set; no database coverage absence is inferred.

## Findings

### F1: Retained source identity carries a narrow mapping to an implicit endpoint

major / open / confirmed; issue key: habitatmech-gold.497ed1acca-mapping-endpoint-contract.

The GOLD path mints habitatmech:GOLD.497ed1acca, which is also the generated record identifier. Its narrowMatch compares implicitly with the broader ontology term, but SourceAttestation.mapping_predicate declares source concept to record identifier and omission when they coincide. This is a local endpoint-contract mismatch, not a claim that SKOS formally prohibits reflexive mappings. Preserve qualified identity and genuine genus; do not merely invert broad/narrow or exact-merge the record.

### F2: Source context is not an established habitat genus: Anaerobic zone

major / open / confirmed; issue key: habitatmech-gold.497ed1acca-context-parent.

Organic biomass is not a kind of the Anaerobic zone location. The named source parent supplies location, not a broader material genus. Retain ENVO genus and exact source provenance; do not infer a replacement identity from a neighboring record.

## Recommended Actions And Acceptance Checks

### A1

Reconcile schema, emitter and consumers so each relation has explicit intended endpoints. Keep source-qualified mints, genuine parents, source counts and native status. Audit actual SSSOM/KGX products before any compatibility claim.

- Regression for this exact GOLD path asserts source and object endpoint semantics.
- Run just seed, inspect the exact seed-canary, then authorized seed-apply and just verify-corpus.
- Run focused schema/strict tests, just validate-products, just validate-history and just qc; inspect downstream mapping products.

### A2

Adjudicate only the immediate GOLD contribution habitatmech:GOLD.9f519b94cc for this source. Add an evidence-backed guarded exclusion. Preserve independent ontology genus, source identifiers, paths, count units and native status.

- Full-corpus before/after regression proves only the reviewed contribution and audit event change.
- Append authorized curation history, dry seed, inspect exact canary, run schema/strict, history, products and corpus reproduction gates.
- Regenerate downstream site/map only after authorized curation; inspect parent display and run full QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/engineered/biomass__9d8a5aca.yaml; Entire target YAML, all fields and generated history | supports | PNA anaerobic-zone Biomass denotes organic material, not the spatial zone it occupies. ENVO:01000155 remains a defensible broader material. The separate Anaerobic zone record describes location and has already had its own container parent excluded; that does not repair this child edge. The biomass-to-zone is-a and retained-mint mapping endpoint need correction. No uniform oxygenation, granule geometry or source-to-experiment crosswalk is established. |
| RAW | data/raw/gold_ecosystem_paths.tsv; Exact target source fields and pipe-delimited path membership | supports | {"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Engineered &gt; Bioreactor &gt; Partial-Nitrification/Anammox (PNA) &gt; Anaerobic zone &gt; Biomass", "depth": "5", "ecosystem": "Engineered", "ecosystem_category": "Bioreactor", "ecosystem_subtype": "Anaerobic zone", "ecosystem_type": "Partial-Nitrification/Anammox (PNA)", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:8551", "leaf_label": "Biomass", "organism_count": "0", "specific_ecosystem": "Biomass", "study_count": "0", "total_assertions": "0"}, "logical_row": 1204}]}. Logical CSV/TSV row ordinals include the header; they are not physical multiline line numbers. GOLD organism counts, auxiliary BioSample totals and TAXON pools are not additive. |
| OWN | curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv; Exact identifiers across all maintained TSV rows | supports | {}. Only exact source-mint/target-owned rows are represented; rows merely pointing to this target are not its decisions. |
| CODE | src/habitatmech/seed.py; src/habitatmech/schema/habitatmech.yaml; Resolution/_decided/resolve_gold/ingest_gold/ingest_parameters/build_document; SourceAttestation.mapping_predicate | supports | Actual source counts and GOLD routes: {"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:01000155"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.497ed1acca", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:01000155"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.497ed1acca", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "path": "Engineered &gt; Bioreactor &gt; Partial-Nitrification/Anammox (PNA) &gt; Anaerobic zone &gt; Biomass"}], "source_concepts": 1}. The mapping_predicate schema describes source concept to record identifier and omission when they are the same concept. Retained-mint NARROW routes compare to an implicit parent while emitting the predicate on the source-to-record attestation. Guarded exclusions affect only the immediate GOLD parent contribution. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md; .claude/skills/curate-yaml-record/references/review-checklist.md; Native identity, hierarchy, units, evidence and status rubric | supports | Parents mean strictly broader is-a, not containment or treatment context. Source occurrences are weaker than characteristic presence. CLASS/SEEDED and optional-field sparsity alone do not establish a defect. Scientific review does not promote native status. |
| PARENT | data/habitats/engineered/anaerobic_zone.yaml; Exact direct source-parent records | supports | {"habitatmech:GOLD.9f519b94cc": {"path": "data/habitats/engineered/anaerobic_zone.yaml", "record": {"curation_history": [{"action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. [CLASS-level] Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate. (source concept habitatmech:GOLD.9f519b94cc)", "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED.", "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.5f3cbd7563 for habitatmech:GOLD.9f519b94cc (Engineered &gt; Bioreactor &gt; Partial-Nitrification/Anammox (PNA) &gt; Anaerobic zone). ITEM hierarchy assessment (#1609): The anaerobic region is not a type of the containing PNA system. PMID:20646732 (DOI:10.1016/j.watres.2010.05.041) experimentally distinguishes reaction zones from the reactor; this does not identify GOLD nodes with that experiment or settle compartment versus microzone geometry. Exclude only the immediate GOLD context contribution; preserve identity, source counts and existing review status.", "curator": "codex-gpt-5", "timestamp": "2026-10-07T00:00:00Z"}], "grounding_status": "UNGROUNDED", "habitat_category": "ENGINEERED", "identifier": "habitatmech:GOLD.9f519b94cc", "label": "Anaerobic zone", "mapping_status": "SEEDED", "source_attestations": [{"notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.", "source": "GOLD", "source_id": "gold.ecosystem:8548", "source_label": "Anaerobic zone", "source_path": "Engineered &gt; Bioreactor &gt; Partial-Nitrification/Anammox (PNA) &gt; Anaerobic zone"}]}}}. Only parent identity, definition, hierarchy and decision coverage are assessed here; parent taxa or mechanisms are not inherited. |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl; Exact ENVO classes, definitions, named parents and typed synonyms | supports | [{"id": "ENVO:01000155", "label": "organic material", "obsolete": false, "sha256": "e76fb55555d983c3b51558dcbee6ffef0fa8384e20866092699c2b67c967c060", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000155"}]. Pinned OWL definitions distinguish organism-derived material from containment equipment. Named parents and typed synonyms were parsed as RDF/XML: organic material has exact synonym biomass; bioreactor has biomaterial containment unit as named parent and no exact synonym. OLS independently verifies current activity and labels. |
| CLASS | https://gold.jgi.doe.gov/; site data sheet exact tuple and row | supports | [{"row": 119, "slug": "biomass__9d8a5aca", "values": ["8551", "Engineered", "Bioreactor", "Partial-Nitrification/Anammox (PNA)", "Anaerobic zone", "Biomass"]}]. Retained official classification workbook; original endpoint was not retained. All five positions are matched, normalizing empty/Unclassified without dropping fields. |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; Five-position tuples; complete sheet row counts (including headers): {"Biosample": 244951, "Organism": 532019, "SequencingProject": 636914, "Study": 63806} | supports | {"Biosample": {"count": 0, "examples": []}, "Organism": {"count": 0, "examples": []}}; exact member-linked sequencing projects=0. Complete census of the retained later export, not a fresh download or original frozen-membership reconstruction. A zero applies only to this exact tuple in this snapshot. Do not replace frozen counts or treat metadata as universal habitat biology. |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf; Selection/support-search/local/audit scratch logs; all existing structured review targets | supports | Ignored/hidden-inclusive rg searches used exact target IDs, source IDs, paths, labels and slugs. Structured scans read all raw/curation TSV rows and all 32 overlay identifiers; Path.rglob read all existing structured reviews. No previous completed scientific structured review targets this exact identifier. No target overlay exists except for generic bioreactor. Searches do not establish absence outside these roots. |
| P27029554 | https://pubmed.ncbi.nlm.nih.gov/27029554/; PubMed ArticleTitle, Abstract and article-level ArticleIdList; full-text limits stated explicitly | partial | Speth 2016; DOI:10.1038/ncomms11172. Abstract and full-text model-system/sampling passages distinguish flocculent and granular material from aerobic/anaerobic niches. The study is not identified with GOLD8550 or GOLD8551; no taxa, genes or numerical oxygen conditions transfer. |
| PNA-TEXT | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4821891/fullTextXML; Model system and Sampling; PMID27029554/DOI10.1038/ncomms11172 | context_only | Inspected full-text model-system description and sampling section: physical biomass fractions and spatial niches are distinguished. This is context evidence only, not a mapping between the experiment and either GOLD leaf. |

## Limits And Additional Notes

- One exact generated record is scientifically assessed; siblings, parent-owned biology and the full corpus are not certified by this report.
- Original frozen GOLD member identities were not reconstructed. The later official export is explicitly a separate snapshot and must not replace frozen counts or prove original equivalence.
- Ontology label validation contains no-adapter skips; focused ontology identities were independently inspected where this target relies on them.
- No curation, native status promotion, paid research, GitHub mutation, product generation or SSSOM/KGX readiness certification is performed.
- All 32 overlays and existing structured review targets were scanned including hidden/ignored files; absence claims remain bounded to the declared local roots.
- The full objective remains review of all 3208 records. Completing this record does not complete that objective.
- No prior structured finding for this exact target was found in the ignored-inclusive parsed inventory. Historical Markdown does not provide an immutable finding identity and is not silently closed.
- Missing optional fields and unpromoted native status alone are not defects. Proposed actions require separately authorized curation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T051114Z-biomass__9d8a5aca
kind: record
repository: culturebotai/HabitatMech
title: 'Scientific record review: biomass__9d8a5aca'
started_at: '2026-10-11T04:58:06.232106Z'
finished_at: '2026-10-11T05:11:14.128642Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Continuing agent participated in prior curation and review workflow;
    this is an adversarial self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: PNA anaerobic-zone Biomass denotes organic material, not the spatial zone
  it occupies. ENVO:01000155 remains a defensible broader material. The separate Anaerobic
  zone record describes location and has already had its own container parent excluded;
  that does not repair this child edge. The biomass-to-zone is-a and retained-mint
  mapping endpoint need correction. No uniform oxygenation, granule geometry or source-to-experiment
  crosswalk is established.
source:
  git_revision: c287909e97d2953317a72ec85ec77dc5a43b7ea3
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
    sha256: 14eb020a26287751c86d1d6eab5c91cf606e0e8ea076832fce82e0646fb85cdd
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
    sha256: a7701bac9916ddd1c471c66edc4d7709d7336801fbc2f6e5082467170278dd4d
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
  - path: data/habitats/engineered/anaerobic_zone.yaml
    sha256: fec30a8db152d08be21eaf94ed65c3cb6d5274c00c25d7b02b3efe797bff3868
    role: context
  - path: data/habitats/engineered/biomass__9d8a5aca.yaml
    sha256: 329c2ed92c31c8fabf53ba091810d2d46460ec85d6c812c4c7497339c16e5b74
    role: target
  - path: data/habitats/other/organic_material.yaml
    sha256: b93ec7554d0bee53cb88474d1d2506e75b693fb68d44b56a4e2e6205d6097694
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
  - path: reports/yaml_record_review/20260928T013131Z-biomass__9d8a5aca.md
    sha256: ab1cf2f284b010f843b2cf0a50f24f45819a05cf21b4491ac04a9d8c530a3bec
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
    sha256: 52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5
    role: context
  - path: src/habitatmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
scope:
  description: Every field of one exact generated HabitatRecord, its contributing
    source concepts, relevant parent meaning, and applicable causal evidence.
  selection: Next alphabetically ordered unreviewed engineered record in an explicit
    16-record work sequence; independent report per exact identifier. Global starting
    coverage200/3208, not a cohort-wide verdict.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.497ed1acca
  exclusions:
  - target: Other 3207 current habitat records
    reason: No record-level verdict in this single-target report; relevant parents
      and sources are context only.
targets:
- target_id: habitatmech:GOLD.497ed1acca
  path: data/habitats/engineered/biomass__9d8a5aca.yaml
  label: Biomass
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Exact source-concept identity and grounding decisions
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded immediate GOLD context-parent exclusions
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: Authored habitat definitions and genus
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained harmonization and generation
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD concepts and ORGANISM counts
checks:
- check_id: C3
  name: Native validate
  status: passed
  required: true
  summary: Exit0; started 2026-10-11T04:58:55.771337Z, finished 2026-10-11T04:58:58.151352Z.
    Target LinkML validation reported no issues.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  command: just validate data/habitats/engineered/biomass__9d8a5aca.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
  scope_note: Actual command scope is retained; a shared full-corpus gate is not an
    individual scientific verdict.
- check_id: C16
  name: Native validate-strict
  status: passed
  required: true
  summary: Exit0; started 2026-10-11T04:59:34.232262Z, finished 2026-10-11T04:59:45.248215Z.
    16 selected files, zero errors.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  command: just validate-strict data/habitats/engineered/biomass.yaml data/habitats/engineered/biomass__545e678f.yaml
    data/habitats/engineered/biomass__6131cc6d.yaml data/habitats/engineered/biomass__9d8a5aca.yaml
    data/habitats/engineered/biomass__e0c132c1.yaml data/habitats/engineered/bioreactor.yaml
    data/habitats/engineered/bioreactor__12a40e2f.yaml data/habitats/engineered/bioreactor__1ac05569.yaml
    data/habitats/engineered/bioreactor__4c20e811.yaml data/habitats/engineered/bioreactor__4c39516f.yaml
    data/habitats/engineered/bioreactor__9b3c0a8b.yaml data/habitats/engineered/bioreactor__afec28a4.yaml
    data/habitats/engineered/bioreactor__bd8d2afc.yaml data/habitats/engineered/bioreactor__e86e1c04.yaml
    data/habitats/engineered/bioreactor__f3a45a9d.yaml data/habitats/engineered/bioremediation__2261f921.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
  scope_note: Actual command scope is retained; a shared full-corpus gate is not an
    individual scientific verdict.
- check_id: C17
  name: Native verify-corpus
  status: passed
  required: true
  summary: Exit0; started 2026-10-11T04:59:45.249317Z, finished 2026-10-11T05:00:05.120376Z.
    3,208 records reproduce exactly.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
  scope_note: Actual command scope is retained; a shared full-corpus gate is not an
    individual scientific verdict.
- check_id: C18
  name: Native validate-products
  status: passed
  required: true
  summary: Exit0; started 2026-10-11T05:00:05.121701Z, finished 2026-10-11T05:00:50.713443Z.
    Label gate passed with 2,057 no-adapter skips; not a scientific or deprecation
    gate.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
  scope_note: Actual command scope is retained; a shared full-corpus gate is not an
    individual scientific verdict.
- check_id: C19
  name: Native validate-history
  status: passed
  required: true
  summary: Exit0; started 2026-10-11T05:00:50.714268Z, finished 2026-10-11T05:00:56.739106Z.
    302 history records valid.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
  scope_note: Actual command scope is retained; a shared full-corpus gate is not an
    individual scientific verdict.
- check_id: C20
  name: Native validate-causal-all
  status: passed
  required: true
  summary: Exit0; started 2026-10-11T05:00:56.739825Z, finished 2026-10-11T05:01:01.766304Z.
    All 32 causal overlays valid.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  command: just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
  scope_note: Actual command scope is retained; a shared full-corpus gate is not an
    individual scientific verdict.
- check_id: C21
  name: Native term-requests-check
  status: passed
  required: true
  summary: Exit0; started 2026-10-11T05:01:01.767272Z, finished 2026-10-11T05:01:17.149018Z.
    109 term requests current.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  command: just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - R
  - RULES
  scope_note: Actual command scope is retained; a shared full-corpus gate is not an
    individual scientific verdict.
- check_id: REPRO
  name: All-field target reproduction and actual source routes
  status: passed
  required: false
  summary: All 16 selected generated documents equal seed.build_document results,
    including every taxon, edge and history field.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  command: .venv/bin/python /private/tmp/habitatmech-review-ak-reproduce.py
  exit_code: 0
  evidence_ids:
  - CODE
- check_id: QC
  name: Full publication QC
  status: skipped
  required: false
  summary: No maintained science or generated product changes in this read-only review.
    Full publication QC at the unchanged base was completed in the preceding publication;
    not rerun or presented as a fresh scientific check. Native gates above and review-check
    are used for this review-only output.
  target_ids:
  - habitatmech:GOLD.497ed1acca
- check_id: ORIGINAL-GOLD
  name: Original frozen source-member reconstruction
  status: unavailable
  required: false
  summary: Ignored-inclusive rg --files of the configured kg-microbe data/raw/gold
    path returned ENOENT (search exit2); source reconstruction could not run. This
    is bounded to that configured path, not a global absence claim. Frozen inventories
    and the separately hashed later export are available.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  command: rg --files --no-ignore --hidden /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold
  evidence_ids:
  - RAW
  - BULK
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/engineered/biomass__9d8a5aca.yaml
  summary: PNA anaerobic-zone Biomass denotes organic material, not the spatial zone
    it occupies. ENVO:01000155 remains a defensible broader material. The separate
    Anaerobic zone record describes location and has already had its own container
    parent excluded; that does not repair this child edge. The biomass-to-zone is-a
    and retained-mint mapping endpoint need correction. No uniform oxygenation, granule
    geometry or source-to-experiment crosswalk is established.
  locator: Entire target YAML, all fields and generated history
  accessed_at: '2026-10-11T05:11:14.128642Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  summary: '{"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0",
    "canonical_path": "Engineered > Bioreactor > Partial-Nitrification/Anammox (PNA)
    > Anaerobic zone > Biomass", "depth": "5", "ecosystem": "Engineered", "ecosystem_category":
    "Bioreactor", "ecosystem_subtype": "Anaerobic zone", "ecosystem_type": "Partial-Nitrification/Anammox
    (PNA)", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:8551", "leaf_label":
    "Biomass", "organism_count": "0", "specific_ecosystem": "Biomass", "study_count":
    "0", "total_assertions": "0"}, "logical_row": 1204}]}. Logical CSV/TSV row ordinals
    include the header; they are not physical multiline line numbers. GOLD organism
    counts, auxiliary BioSample totals and TAXON pools are not additive.'
  locator: Exact target source fields and pipe-delimited path membership
  accessed_at: '2026-10-11T05:03:44.909197Z'
  support: supports
- evidence_id: OWN
  kind: record_content
  reference: curation/decisions.tsv; curation/gold_parent_exclusions.tsv; curation/term_requests.tsv
  summary: '{}. Only exact source-mint/target-owned rows are represented; rows merely
    pointing to this target are not its decisions.'
  locator: Exact identifiers across all maintained TSV rows
  accessed_at: '2026-10-11T05:03:44.909197Z'
  support: supports
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/schema/habitatmech.yaml
  summary: 'Actual source counts and GOLD routes: {"reviewed_sources": 0, "routes":
    [{"actual": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": ["ENVO:01000155"], "extra_xrefs": [], "grounding_status": "NARROW",
    "identifier": "habitatmech:GOLD.497ed1acca", "mapping_predicate": "skos:narrowMatch",
    "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:01000155"],
    "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.497ed1acca",
    "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"},
    "path": "Engineered > Bioreactor > Partial-Nitrification/Anammox (PNA) > Anaerobic
    zone > Biomass"}], "source_concepts": 1}. The mapping_predicate schema describes
    source concept to record identifier and omission when they are the same concept.
    Retained-mint NARROW routes compare to an implicit parent while emitting the predicate
    on the source-to-record attestation. Guarded exclusions affect only the immediate
    GOLD parent contribution.'
  locator: Resolution/_decided/resolve_gold/ingest_gold/ingest_parameters/build_document;
    SourceAttestation.mapping_predicate
  accessed_at: '2026-10-11T05:05:18.797672Z'
  support: supports
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md;
    .claude/skills/curate-yaml-record/references/review-checklist.md
  summary: Parents mean strictly broader is-a, not containment or treatment context.
    Source occurrences are weaker than characteristic presence. CLASS/SEEDED and optional-field
    sparsity alone do not establish a defect. Scientific review does not promote native
    status.
  locator: Native identity, hierarchy, units, evidence and status rubric
  accessed_at: '2026-10-11T05:11:14.128642Z'
  support: supports
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats/engineered/anaerobic_zone.yaml
  summary: '{"habitatmech:GOLD.9f519b94cc": {"path": "data/habitats/engineered/anaerobic_zone.yaml",
    "record": {"curation_history": [{"action": "CONFIRM_UNGROUNDED", "changes": "Confirmed
    UNGROUNDED: no ontology term fits this concept. [CLASS-level] Class-level sweep
    (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched
    this label by any search route. Whether the concept is a habitat at all was NOT
    assessed, so this is not yet a term-request candidate. (source concept habitatmech:GOLD.9f519b94cc)",
    "curator": "claude-opus-5", "timestamp": "2026-08-12T00:00:00Z"}, {"action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED.",
    "curator": "seed_from_sources", "timestamp": "2026-08-16T05:58:02Z"}, {"action":
    "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution
    habitatmech:GOLD.5f3cbd7563 for habitatmech:GOLD.9f519b94cc (Engineered > Bioreactor
    > Partial-Nitrification/Anammox (PNA) > Anaerobic zone). ITEM hierarchy assessment
    (#1609): The anaerobic region is not a type of the containing PNA system. PMID:20646732
    (DOI:10.1016/j.watres.2010.05.041) experimentally distinguishes reaction zones
    from the reactor; this does not identify GOLD nodes with that experiment or settle
    compartment versus microzone geometry. Exclude only the immediate GOLD context
    contribution; preserve identity, source counts and existing review status.", "curator":
    "codex-gpt-5", "timestamp": "2026-10-07T00:00:00Z"}], "grounding_status": "UNGROUNDED",
    "habitat_category": "ENGINEERED", "identifier": "habitatmech:GOLD.9f519b94cc",
    "label": "Anaerobic zone", "mapping_status": "SEEDED", "source_attestations":
    [{"notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv.",
    "source": "GOLD", "source_id": "gold.ecosystem:8548", "source_label": "Anaerobic
    zone", "source_path": "Engineered > Bioreactor > Partial-Nitrification/Anammox
    (PNA) > Anaerobic zone"}]}}}. Only parent identity, definition, hierarchy and
    decision coverage are assessed here; parent taxa or mechanisms are not inherited.'
  locator: Exact direct source-parent records
  accessed_at: '2026-10-11T05:11:14.128642Z'
  support: supports
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl
  summary: '[{"id": "ENVO:01000155", "label": "organic material", "obsolete": false,
    "sha256": "e76fb55555d983c3b51558dcbee6ffef0fa8384e20866092699c2b67c967c060",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000155"}].
    Pinned OWL definitions distinguish organism-derived material from containment
    equipment. Named parents and typed synonyms were parsed as RDF/XML: organic material
    has exact synonym biomass; bioreactor has biomaterial containment unit as named
    parent and no exact synonym. OLS independently verifies current activity and labels.'
  locator: Exact ENVO classes, definitions, named parents and typed synonyms
  accessed_at: '2026-10-11T05:02:40.178399Z'
  support: supports
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: CLASS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: '[{"row": 119, "slug": "biomass__9d8a5aca", "values": ["8551", "Engineered",
    "Bioreactor", "Partial-Nitrification/Anammox (PNA)", "Anaerobic zone", "Biomass"]}].
    Retained official classification workbook; original endpoint was not retained.
    All five positions are matched, normalizing empty/Unclassified without dropping
    fields.'
  locator: site data sheet exact tuple and row
  accessed_at: '2026-10-11T05:07:53.566565Z'
  support: supports
  snapshot_sha256: 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  summary: '{"Biosample": {"count": 0, "examples": []}, "Organism": {"count": 0, "examples":
    []}}; exact member-linked sequencing projects=0. Complete census of the retained
    later export, not a fresh download or original frozen-membership reconstruction.
    A zero applies only to this exact tuple in this snapshot. Do not replace frozen
    counts or treat metadata as universal habitat biology.'
  locator: 'Five-position tuples; complete sheet row counts (including headers): {"Biosample":
    244951, "Organism": 532019, "SequencingProject": 636914, "Study": 63806}'
  accessed_at: '2026-10-11T05:07:53.566565Z'
  support: supports
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: SEARCH
  kind: search
  reference: curation; history; research; reports; reviews; data/raw; data/habitats;
    conf
  summary: Ignored/hidden-inclusive rg searches used exact target IDs, source IDs,
    paths, labels and slugs. Structured scans read all raw/curation TSV rows and all
    32 overlay identifiers; Path.rglob read all existing structured reviews. No previous
    completed scientific structured review targets this exact identifier. No target
    overlay exists except for generic bioreactor. Searches do not establish absence
    outside these roots.
  locator: Selection/support-search/local/audit scratch logs; all existing structured
    review targets
  accessed_at: '2026-10-11T04:58:06.232106Z'
  support: supports
  search_scope: Ignored/hidden-inclusive rg searches used exact target IDs, source
    IDs, paths, labels and slugs. Structured scans read all raw/curation TSV rows
    and all 32 overlay identifiers; Path.rglob read all existing structured reviews.
    No previous completed scientific structured review targets this exact identifier.
    No target overlay exists except for generic bioreactor. Searches do not establish
    absence outside these roots.
- evidence_id: P27029554
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/27029554/
  summary: Speth 2016; DOI:10.1038/ncomms11172. Abstract and full-text model-system/sampling
    passages distinguish flocculent and granular material from aerobic/anaerobic niches.
    The study is not identified with GOLD8550 or GOLD8551; no taxa, genes or numerical
    oxygen conditions transfer.
  locator: PubMed ArticleTitle, Abstract and article-level ArticleIdList; full-text
    limits stated explicitly
  accessed_at: '2026-10-11T05:02:41.690844Z'
  support: partial
  snapshot_sha256: 97caf61fa3b1b55bd2c7ca941e891834675681436786bcca5cf3d0e04180bf22
- evidence_id: PNA-TEXT
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4821891/fullTextXML
  summary: 'Inspected full-text model-system description and sampling section: physical
    biomass fractions and spatial niches are distinguished. This is context evidence
    only, not a mapping between the experiment and either GOLD leaf.'
  locator: Model system and Sampling; PMID27029554/DOI10.1038/ncomms11172
  accessed_at: '2026-10-11T05:03:43.446162Z'
  support: context_only
  snapshot_sha256: ea24615fa9eead6f2936a927809766df5d0edb76dfe7f6f8b833d54059187dbb
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Exact source-qualified habitat meaning
  outcome: supported
  summary: PNA anaerobic-zone Biomass denotes organic material, not the spatial zone
    it occupies. ENVO:01000155 remains a defensible broader material. The separate
    Anaerobic zone record describes location and has already had its own container
    parent excluded; that does not repair this child edge. The biomass-to-zone is-a
    and retained-mint mapping endpoint need correction. No uniform oxygenation, granule
    geometry or source-to-experiment crosswalk is established.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  evidence_ids:
  - R
  - RAW
  - PARENT
  - BULK
  - ONT
- assessment_id: STATUS
  area: consistency
  topic: Current source accounting and native mapping status
  outcome: supported
  summary: All fields reproduce from maintained inputs. Contributing concepts=1, ITEM-reviewed=0;
    generated mapping_status=SEEDED. The review neither endorses every inherited claim
    nor changes native status.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  evidence_ids:
  - OWN
  - CODE
  - R
- assessment_id: SOURCE
  area: provenance
  topic: Attestations, counts, units and later-member scope
  outcome: supported
  summary: Frozen source IDs, labels, paths, collapsed-node notes and organism counts
    match. Zero-count omission is not biological absence. Later BioSample/Organism
    records and joined studies are kept separate from frozen ORGANISM assertions and
    from any taxon pool. No MIxS triad, study observation or parent biology is automatically
    promoted to identity.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  evidence_ids:
  - RAW
  - CLASS
  - BULK
- assessment_id: HIERARCHY
  area: grounding
  topic: Strictly broader genera versus contextual source parents
  outcome: concern
  summary: PNA anaerobic-zone Biomass denotes organic material, not the spatial zone
    it occupies. ENVO:01000155 remains a defensible broader material. The separate
    Anaerobic zone record describes location and has already had its own container
    parent excluded; that does not repair this child edge. The biomass-to-zone is-a
    and retained-mint mapping endpoint need correction. No uniform oxygenation, granule
    geometry or source-to-experiment crosswalk is established.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  evidence_ids:
  - OWN
  - PARENT
  - RULES
  - ONT
  - P27029554
- assessment_id: SPARSE
  area: completeness
  topic: Optional biology and structured-source applicability
  outcome: not_applicable
  summary: The target makes no taxon, parameter, causal-graph, gene, regulator, protein
    or organism/dataset expression-module claim. Optional biological fields need not
    be filled from neighboring records or studies. iModulonDB is not applicable to
    this declared claim set; no database coverage absence is inferred.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  evidence_ids:
  - R
  - SEARCH
findings:
- finding_id: F1
  issue_key: habitatmech-gold.497ed1acca-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Retained source identity carries a narrow mapping to an implicit endpoint
  description: The GOLD path mints habitatmech:GOLD.497ed1acca, which is also the
    generated record identifier. Its narrowMatch compares implicitly with the broader
    ontology term, but SourceAttestation.mapping_predicate declares source concept
    to record identifier and omission when they coincide. This is a local endpoint-contract
    mismatch, not a claim that SKOS formally prohibits reflexive mappings. Preserve
    qualified identity and genuine genus; do not merely invert broad/narrow or exact-merge
    the record.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - R
  - CODE
  - OWN
  - RULES
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material semantic or evidence defect requiring maintained-input
    correction.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Mapping emission and source resolution
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Declared mapping endpoints
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
- finding_id: F2
  issue_key: habitatmech-gold.497ed1acca-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: 'Source context is not an established habitat genus: Anaerobic zone'
  description: Organic biomass is not a kind of the Anaerobic zone location. The named
    source parent supplies location, not a broader material genus. Retain ENVO genus
    and exact source provenance; do not infer a replacement identity from a neighboring
    record.
  target_ids:
  - habitatmech:GOLD.497ed1acca
  field_paths:
  - parent_habitats[habitatmech:GOLD.9f519b94cc]
  evidence_ids:
  - R
  - RAW
  - PARENT
  - OWN
  - BULK
  - RULES
  rule_id: docs/CURATION.md; docs/record-review-profile.md
  native_severity: major
  normalization_reason: Material semantic or evidence defect requiring maintained-input
    correction.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact path and expected-parent guard
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Source-scope adjudication
actions:
- action_id: A1
  description: Reconcile schema, emitter and consumers so each relation has explicit
    intended endpoints. Keep source-qualified mints, genuine parents, source counts
    and native status. Audit actual SSSOM/KGX products before any compatibility claim.
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.497ed1acca
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Mapping emission and source resolution
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Declared mapping endpoints
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Regression for this exact GOLD path asserts source and object endpoint semantics.
  - Run just seed, inspect the exact seed-canary, then authorized seed-apply and just
    verify-corpus.
  - Run focused schema/strict tests, just validate-products, just validate-history
    and just qc; inspect downstream mapping products.
- action_id: A2
  description: Adjudicate only the immediate GOLD contribution habitatmech:GOLD.9f519b94cc
    for this source. Add an evidence-backed guarded exclusion. Preserve independent
    ontology genus, source identifiers, paths, count units and native status.
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.497ed1acca
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact path and expected-parent guard
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Source-scope adjudication
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Full-corpus before/after regression proves only the reviewed contribution and
    audit event change.
  - Append authorized curation history, dry seed, inspect exact canary, run schema/strict,
    history, products and corpus reproduction gates.
  - Regenerate downstream site/map only after authorized curation; inspect parent
    display and run full QC.
limitations:
- One exact generated record is scientifically assessed; siblings, parent-owned biology
  and the full corpus are not certified by this report.
- Original frozen GOLD member identities were not reconstructed. The later official
  export is explicitly a separate snapshot and must not replace frozen counts or prove
  original equivalence.
- Ontology label validation contains no-adapter skips; focused ontology identities
  were independently inspected where this target relies on them.
- No curation, native status promotion, paid research, GitHub mutation, product generation
  or SSSOM/KGX readiness certification is performed.
- All 32 overlays and existing structured review targets were scanned including hidden/ignored
  files; absence claims remain bounded to the declared local roots.
notes:
- The full objective remains review of all 3208 records. Completing this record does
  not complete that objective.
- No prior structured finding for this exact target was found in the ignored-inclusive
  parsed inventory. Historical Markdown does not provide an immutable finding identity
  and is not silently closed.
- Missing optional fields and unpromoted native status alone are not defects. Proposed
  actions require separately authorized curation.
tags:
- habitatmech
- record-review
- engineered
- scientific-review
```
