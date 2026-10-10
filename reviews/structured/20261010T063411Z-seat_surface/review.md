# Scientific record review: Seat surface [seat_surface]

- Review: 20261010T063411Z-seat_surface
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-10T06:23:04Z
- Finished UTC: 2026-10-10T06:34:11Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The stadium seat-surface source is distinct from both the stadium and the train-car seat-surface source. A contact surface is not a subtype of its enclosing stadium; the context-only parent needs exclusion without inventing a replacement identity or merging the two seat records.

## Scope And Provenance

Read the entire resolved generated record and assess every emitted claim type against maintained inputs and bounded external evidence.

Selection: Next individual target in the ongoing3208-record goal. Before this set,111 native bundles cover87 distinct current targets. Context records are not counted as reviewed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 486d97f799fe3df7d8933b6c9a5dab69e48f7f59.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.2934cf4eee | data/habitats/engineered/seat_surface.yaml | generated | Seat surface |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate | passed | True | habitatmech:GOLD.2934cf4eee | No issues found<br>uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/engineered/seat_surface.yaml |
| just validate-strict | passed | True | habitatmech:GOLD.2934cf4eee | uv run python scripts/validate_strict.py data/habitats/engineered/sand_filter.yaml data/habitats/engineered/sand_microcosm.yaml data/habitats/engineered/sandstone.yaml data/habitats/engineered/sanger.yaml data/habitats/engineered/sbr_ebpr.yaml data/habitats/engineered/seat_surface.yaml data/habitats/engineered/seat_surface__a1cb78f8.yaml<br>Validating 7 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      7<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just verify-corpus | passed | True | habitatmech:GOLD.2934cf4eee | expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br>uv run python scripts/verify_corpus.py |
| just validate-products | passed | True | habitatmech:GOLD.2934cf4eee | id↔label correspondence summary:<br>          OK_CANONICAL: 1178<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2057<br><br>✅ All id↔label pairs correspond.<br>uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| just validate-history | passed | True | habitatmech:GOLD.2934cf4eee | No issues found<br>236 history record(s) valid against src/habitatmech/schema/history.yaml |
| just validate-causal-all | passed | True | habitatmech:GOLD.2934cf4eee | validated 32 causal-graph curation file(s) with 32 graph(s)<br>uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.2934cf4eee | term-request table is current (109 terms)<br>uv run python scripts/build_term_requests.py --check |
| Authoritative QC on exact unchanged reviewed base | passed | True | habitatmech:GOLD.2934cf4eee | 658 passed,3 skipped; all HabitatMech quality gates passed on exact reviewed base.4 structured-review contract tests also passed. No local full-QC execution is claimed. |
| Structured iModulonDB applicability | not_applicable | False | habitatmech:GOLD.2934cf4eee | No target gene, locus, regulator or transcript-module claim requires an adapter lookup. SBR paper is used only for reactor context; no expression/mechanism claim is curated. |

## Scientific And Domain Assessments

### Resolved identity, grounding and source scope

identity: supported. Targets: habitatmech:GOLD.2934cf4eee.

The full path resolves a stadium-associated Seat surface, identifier habitatmech:GOLD.2934cf4eee, node8306. The train-car record has a different mint and context, despite sharing the display label. Neither the word seat nor the source path makes the surface identical to the whole seat, building, or stadium. Preserve both mints unless source equivalence is separately established.

### Strict parents versus source context

grounding: concern. Targets: habitatmech:GOLD.2934cf4eee.

The sole parent habitatmech:GOLD.2d40c87aeb is the Stadium source grouping. A surface on seating is located in or part of a venue but is not a kind of venue. This is a supported hierarchy defect even though original sample membership is unavailable.

### Primary evidence, taxon and mechanism scope

evidence: supported. Targets: habitatmech:GOLD.2934cf4eee.

Buttner et al. inspect plastic arena-seat surfaces and distinguish their sampled material from the overall test setting. This controlled, inoculated study supports the surface/material distinction only; it is neither a field stadium survey nor evidence for exact GOLD node8306 membership or natural characteristic taxa. Generic seat-surface evidence cannot supply the missing source cohort.

### Source extent, units, decisions and historical limitations

provenance: unknown. Targets: habitatmech:GOLD.2934cf4eee.

Frozen GOLD data row1251 has node8306 and zero organism/study/biosample counts. No assertion count or unit is emitted. Later classification row182 retains the exact stadium-seat path; the full later bulk Biosample/Organism census has no exact-path members or joined projects. This is a bounded source availability limitation, not proof of an empty stadium microbiome. Decision data row322 is CLASS, so SEEDED remains correct.

Current exact-field source-row details (data rows exclude headers/comments):
[
  {
    "file": "data/raw/gold_ecosystem_paths.tsv",
    "matches": [
      {
        "data_row": 1251,
        "row": {
          "canonical_path": "Engineered &gt; Built environment &gt; City &gt; Stadium &gt; Seat surface",
          "ecosystem": "Engineered",
          "ecosystem_category": "Built environment",
          "ecosystem_type": "City",
          "ecosystem_subtype": "Stadium",
          "specific_ecosystem": "Seat surface",
          "leaf_label": "Seat surface",
          "depth": "5",
          "gold_node_count": "1",
          "organism_count": "0",
          "study_count": "0",
          "biosample_count": "0",
          "total_assertions": "0",
          "gold_node_ids": "gold.ecosystem:8306"
        }
      }
    ]
  },
  {
    "file": "curation/decisions.tsv",
    "matches": [
      {
        "data_row": 322,
        "row": {
          "identifier": "habitatmech:GOLD.2934cf4eee",
          "decision": "CONFIRM_UNGROUNDED",
          "object_id": "",
          "object_label": "",
          "grounding_status": "",
          "curator": "claude-opus-5",
          "date": "2026-08-12",
          "notes": "Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.",
          "review_depth": "CLASS",
          "category": "",
          "relation": ""
        }
      }
    ]
  },
  {
    "file": "data/habitats/PATHS.tsv",
    "matches": [
      {
        "data_row": 1589,
        "row": {
          "identifier": "habitatmech:GOLD.2934cf4eee",
          "slug": "seat_surface"
        }
      }
    ]
  }
]

### Optional content and status are not automatically enriched

completeness: supported. Targets: habitatmech:GOLD.2934cf4eee.

No target causal graph, environmental parameter, discussion or dataset claim is emitted. Optional emptiness is not itself a defect. 1 source concept(s), 0 ITEM-reviewed: status and history reproduce. Parent/child taxa, parameters and observations are not inherited. No definitions, curation events or status promotions are made by this review.

### Validation scope versus scientific judgement

schema: supported. Targets: habitatmech:GOLD.2934cf4eee.

Fresh native validators passed; exact-base CI QC passed with3 skipped tests. ID-label checks report1178 canonical,1 synonym,5 accepted exceptions and2057 entries without an adapter. These are deterministic checks, not ecological certification or a general SSSOM/KGX readiness finding.

## Findings

### F1: Exclude the stadium context parent from its seat surface

major / open / confirmed; issue key: gold-2934cf4eee-seat-surface-stadium-context-parent.

The generated source hierarchy asserts that a seat surface is a kind of Stadium. A contacted seating surface and its surrounding venue are different entity types; retain the source location in the attestation rather than as an is-a parent.

## Recommended Actions And Acceptance Checks

### ACT1

Add a guarded exclusion for habitatmech:GOLD.2934cf4eee, exact path Engineered &gt; Built environment &gt; City &gt; Stadium &gt; Seat surface, expected parent habitatmech:GOLD.2d40c87aeb. Preserve mint, node8306, path, zero-count omission and CLASS/SEEDED state. Do not merge with train-car seating or invent a whole-seat/venue genus.

- Change only the named maintained input in a separately authorized curation session; never hand-edit generated habitats.
- Run just seed, then inspect just seed-canary habitatmech:GOLD.2934cf4eee --force before any broader write.
- Preserve unaffected identity, source units, node provenance and prior history; allow only intended generator-derived status/history changes.
- Append native session history for actual curation, regenerate semantic-map/site products if changed, and pass just qc plus just validate-products.
- Save a new native follow-up with this exact finding identity; do not rewrite this review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/seat_surface.yaml; Complete generated YAML; every emitted field read | supports | Identity, all parents, source attestations, optional-slot presence, status and full generated history inspected. |
| E2 | data/raw/ and curation/; Exact rows in the source-extent assessment; structured parse of every raw and top-level curation TSV | supports | Mint/path, source nodes, counts/units, decisions, definitions, ontology parents and seeder output traced. Exact full-document reproduction was asserted. |
| R0 | docs/CURATION.md; Decision model, MIxS triads, status gates and GOLD context-parent exclusions; native checklist and HARMONIZATION also read | supports | Parents must be strictly broader. Source occurrence, triad roles and taxonomic associations do not establish identity, characteristic presence or mechanism. |
| W1 | https://gold.jgi.doe.gov/download?mode=site_excel; Reused dated complete-sheet census: Biosample 244951, Organism 532019, SequencingProject636914, Study63806 rows including headers; classification workbook2422 rows | supports | Reused prior preparation census, inspected exact-path members/joins, and rechecked bulk SHA256 and classification SHA256. Bulk 238974789 bytes; classification https://gold.jgi.doe.gov/download?mode=ecosystempaths is 84174 bytes, SHA2563933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396. This later snapshot does not replace either frozen manifest. |
| P1 | https://journals.asm.org/doi/10.1128/AEM.01825-06; DOI:10.1128/AEM.01825-06; primary full text, Test materials and Surface sampling and sample processing | supports | Plastic arena seats are explicitly treated as sampled surface materials. This is controlled inoculation evidence for the surface distinction, not exact GOLD provenance or natural colonization. |
| V1 | https://github.com/CultureBotAI/HabitatMech/actions/runs/38030062780; Exact-base merge-group QC metadata/log and fresh local checks | supports | CI at exact base486d97f799fe3df7d8933b6c9a5dab69e48f7f59 passed authoritative QC: 658 tests passed,3 skipped;4 structured-review contract tests passed. Fresh local target/schema, corpus, label, history, causal and term-request gates also passed. CI is not claimed as a newly run local full QC. |
| S1 | data/raw/, curation/, research/, reports/, reviews/; Ignored-inclusive rg by target IDs, labels and slugs, plus full pathlib traversal/structured parsing | context_only | No target causal overlay among32 scanned files and no prior native scientific review of this exact target among111 bundles. Legacy sand-microcosm review and contextual parent reviews remain historical evidence. Bounded ontology-label searches found no exact proposed sand-filter, sand-microcosm, seat-surface or SBR-EBPR match; an incidental passangers substring is not Sanger evidence. |

## Limits And Additional Notes

- The exact stadium, seat material, sample type and source members are not established by the frozen zero-count row.
- The primary arena-seat experiment is controlled inoculation, not a natural stadium community survey. No observational taxa or health implications are inferred.
- Frozen and later source snapshots have different scope and units. Bounded missing entries are not evidence of ecological absence.
- No paid research, habitat/curation mutation, GitHub mutation, or publication was performed. Existing bundles remain immutable.
- Scientific coverage is not inferred from schema checks. Adapter-free label rows and three skipped baseline tests remain explicitly unverified by those gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T063411Z-seat_surface
kind: record
repository: culturebotai/HabitatMech
title: 'Scientific record review: Seat surface [seat_surface]'
started_at: '2026-10-10T06:23:04Z'
finished_at: '2026-10-10T06:34:11Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same continuing agent independently checks source claims within
    this session; no separate reviewer or human approval is claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The stadium seat-surface source is distinct from both the stadium and the
  train-car seat-surface source. A contact surface is not a subtype of its enclosing
  stadium; the context-only parent needs exclusion without inventing a replacement
  identity or merging the two seat records.
source:
  git_revision: 486d97f799fe3df7d8933b6c9a5dab69e48f7f59
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
    sha256: 200a0185b77586aaea6bffd2b1e837fb671eb26e8f7f4d2cb05db658f9036972
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 09f728b498eb096296a2f50c8eb4af55b0af24c224740273b8a9c0202bdbb33c
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: 9977e384b79128d6e89c85f28e35c77d29644d503dea6d53c12628599e33f7f3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/engineered/artificial_ecosystem.yaml
    sha256: 721350810f5b9c5c33a03ce8133bdfee22605458fef414c87390469695964317
    role: context
  - path: data/habitats/engineered/bioreactor.yaml
    sha256: c0a5f4d06130d949810c29b15f5874b4e9673b23dc188161d699412c2bea0c02
    role: context
  - path: data/habitats/engineered/constructed_swimming_pool.yaml
    sha256: 4e3cc2756947fc794f0e36159147bf1d6d474f5fcf6e56138a3079f85a76333b
    role: context
  - path: data/habitats/engineered/sand_filter.yaml
    sha256: 0e8421f00c3e4ce0e582c787808321ede3d08cb35de0d167e2d8cc51cefb6d85
    role: context
  - path: data/habitats/engineered/sand_microcosm.yaml
    sha256: 1f52fa1987052118fe10e6ebe73150d7c5b818b30a469942ae36469004d2429e
    role: context
  - path: data/habitats/engineered/sandstone.yaml
    sha256: 728a8d34ece8bd7bc1a5d2f2a5cb64ed03e4251d6119a180da62bac31dd57f5a
    role: context
  - path: data/habitats/engineered/sanger.yaml
    sha256: f266151bc7cb43bcb015754b3194288c4b84619645b27eb7889ef661c12cfa54
    role: context
  - path: data/habitats/engineered/sbr_ebpr.yaml
    sha256: 28f53957563fdd126544845f58edfbd208f386d64172e0b924e8ad7133488650
    role: context
  - path: data/habitats/engineered/seat_surface.yaml
    sha256: 007419cde64cb77d512708d786adaa4fceb49047dfa5d6376e8df58be2fe2363
    role: target
  - path: data/habitats/engineered/seat_surface__a1cb78f8.yaml
    sha256: c7202231ac26aab07f1100eb2bde2add703e32b39c60f4cef961c723641d516b
    role: context
  - path: data/habitats/engineered/simulated_communities_sequence_read_mixture.yaml
    sha256: 1148b9a248c8d388e337b259fdbdde3093674a7261a453321f35b5c69c62df32
    role: context
  - path: data/habitats/engineered/stadium.yaml
    sha256: e964c2e922899f227ba875d8c74a1f80d96c2a96597a027ab7be1daf3d63733b
    role: context
  - path: data/habitats/engineered/stone.yaml
    sha256: 416b23ae32970801cb998c4d2705a08d98d77c88a57ad0c2b86d30db94a78337
    role: context
  - path: data/habitats/engineered/train_car.yaml
    sha256: 1077e48e9cc6cbc472f7b3f9572716469b89de9f3540b62d44cc18a2ed4beb05
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
  - path: reports/yaml_record_review/20260925T072816Z-sand_microcosm.md
    sha256: 15be1461842bb1197c95462d26a423a9919e385cc5c81af924b6ab3402437ccc
    role: context
  - path: reports/yaml_record_review/20261008T032323Z-constructed_swimming_pool.md
    sha256: 6343daecaee202ff400ae5304d2bca3f4532572d8d090414e1d9e1600c28ac10
    role: context
  - path: reviews/structured/20261009T164402Z-modeled/review.md
    sha256: c339f741bb2e3c43d5266ac5d4e5312617781d6642a017e1cae2148a06faabed
    role: context
  - path: reviews/structured/20261009T164402Z-modeled/review.yaml
    sha256: 2dcf49f4df3b5fee58578ef50d52e20a8ecc61e03aa02e260dff2cdf3bfff44b
    role: context
  - path: reviews/structured/20261010T045310Z-room_surface/review.md
    sha256: 5075ceb7e5b7c5089ef6919e86b4d5f7eb37d722b75be5fd5d17da0435cc744c
    role: context
  - path: reviews/structured/20261010T045310Z-room_surface/review.yaml
    sha256: f362436c0872c4b058fe76b5cea81e98765afda6de531e2c6010760ee1ac8919
    role: context
  - path: reviews/structured/20261010T054259Z-room_surface-followup/review.md
    sha256: 37c76612d4093673b3d77be223ac8dd1df081aa9cc555409db14aa1665f0d316
    role: context
  - path: reviews/structured/20261010T054259Z-room_surface-followup/review.yaml
    sha256: 5bf518d52afaa8a3db9f05ce221ee802f0843d74d8fa29bb875e5d54f5ab152e
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5
    role: context
  - path: src/habitatmech/seed.py
    sha256: 92adf631fa099120a497ff7001473e659347d23ac9b418f04cd341ddad5d2a89
    role: context
scope:
  description: Read the entire resolved generated record and assess every emitted
    claim type against maintained inputs and bounded external evidence.
  selection: Next individual target in the ongoing3208-record goal. Before this set,111
    native bundles cover87 distinct current targets. Context records are not counted
    as reviewed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.2934cf4eee
  exclusions:
  - target: Other habitat records, full external database membership and universal
      mechanism claims
    reason: Related records and primary studies provide bounded context only; this
      is one-record coverage, not a corpus pass.
targets:
- target_id: habitatmech:GOLD.2934cf4eee
  path: data/habitats/engineered/seat_surface.yaml
  label: Seat surface
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: source identity and item-level review decisions
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: authored label/definition and genus
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: guarded GOLD context-parent exclusions
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: frozen GOLD source paths and organism counts
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: later source-classified BIOSAMPLE counts
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_studies.tsv
    role: study/path relationships
  - repository: culturebotai/HabitatMech
    path: scripts/extract_gold_biosamples.py
    role: source sample/study extraction
  - repository: culturebotai/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: PREGO habitat and taxon count summary
  - repository: culturebotai/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: ranked taxon association scores and channels
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: generated records
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/extract.py
    role: source inventory extraction
  - repository: culturebotai/HabitatMech
    path: data/habitats/PATHS.tsv
    role: stable identifier-to-slug mapping
checks:
- check_id: C1
  name: just validate
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  command: just validate data/habitats/engineered/seat_surface.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - V1
  summary: 'No issues found

    uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class
    HabitatRecord data/habitats/engineered/seat_surface.yaml'
  scope_note: Actually executed 2026-10-10T06:25:44.720891+00:00 to 2026-10-10T06:25:46.708258+00:00;
    shared gates cover the corpus or the explicitly listed seven targets.
- check_id: C2
  name: just validate-strict
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  command: just validate-strict data/habitats/engineered/sand_filter.yaml data/habitats/engineered/sand_microcosm.yaml
    data/habitats/engineered/sandstone.yaml data/habitats/engineered/sanger.yaml data/habitats/engineered/sbr_ebpr.yaml
    data/habitats/engineered/seat_surface.yaml data/habitats/engineered/seat_surface__a1cb78f8.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - V1
  summary: "uv run python scripts/validate_strict.py data/habitats/engineered/sand_filter.yaml\
    \ data/habitats/engineered/sand_microcosm.yaml data/habitats/engineered/sandstone.yaml\
    \ data/habitats/engineered/sanger.yaml data/habitats/engineered/sbr_ebpr.yaml\
    \ data/habitats/engineered/seat_surface.yaml data/habitats/engineered/seat_surface__a1cb78f8.yaml\n\
    Validating 7 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      7\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Actually executed 2026-10-10T06:25:48.693729+00:00 to 2026-10-10T06:25:53.005123+00:00;
    shared gates cover the corpus or the explicitly listed seven targets.
- check_id: C3
  name: just verify-corpus
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - V1
  summary: "expected 3208 records, found 3208 on disk\n  missing:   0\n  extra:  \
    \   0\n  differing: 0\n\ncorpus reproduces exactly from data/raw/\nuv run python\
    \ scripts/verify_corpus.py"
  scope_note: Actually executed 2026-10-10T06:25:53.005694+00:00 to 2026-10-10T06:26:06.159027+00:00;
    shared gates cover the corpus or the explicitly listed seven targets.
- check_id: C4
  name: just validate-products
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - V1
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 1178\n     \
    \       OK_SYNONYM: 1\n          OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2057\n\
    \n✅ All id↔label pairs correspond.\nuv run python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml"
  scope_note: Actually executed 2026-10-10T06:26:06.159626+00:00 to 2026-10-10T06:26:46.073150+00:00;
    shared gates cover the corpus or the explicitly listed seven targets.
- check_id: C5
  name: just validate-history
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - V1
  summary: 'No issues found

    236 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Actually executed 2026-10-10T06:26:46.073742+00:00 to 2026-10-10T06:26:51.196420+00:00;
    shared gates cover the corpus or the explicitly listed seven targets.
- check_id: C6
  name: just validate-causal-all
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  command: just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - V1
  summary: 'validated 32 causal-graph curation file(s) with 32 graph(s)

    uv run python scripts/validate_causal_graph_curations.py'
  scope_note: Actually executed 2026-10-10T06:26:51.197037+00:00 to 2026-10-10T06:26:55.149194+00:00;
    shared gates cover the corpus or the explicitly listed seven targets.
- check_id: C7
  name: just term-requests-check
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  command: just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - V1
  summary: 'term-request table is current (109 terms)

    uv run python scripts/build_term_requests.py --check'
  scope_note: Actually executed 2026-10-10T06:26:55.150096+00:00 to 2026-10-10T06:27:10.492214+00:00;
    shared gates cover the corpus or the explicitly listed seven targets.
- check_id: CI
  name: Authoritative QC on exact unchanged reviewed base
  status: passed
  required: true
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  command: just qc (GitHub merge-group run38030062780; inspected metadata and log)
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - V1
  summary: 658 passed,3 skipped; all HabitatMech quality gates passed on exact reviewed
    base.4 structured-review contract tests also passed. No local full-QC execution
    is claimed.
- check_id: IM
  name: Structured iModulonDB applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  summary: No target gene, locus, regulator or transcript-module claim requires an
    adapter lookup. SBR paper is used only for reactor context; no expression/mechanism
    claim is curated.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/seat_surface.yaml
  locator: Complete generated YAML; every emitted field read
  accessed_at: '2026-10-10T06:34:11Z'
  support: supports
  summary: Identity, all parents, source attestations, optional-slot presence, status
    and full generated history inspected.
- evidence_id: E2
  kind: record_content
  reference: data/raw/ and curation/
  locator: Exact rows in the source-extent assessment; structured parse of every raw
    and top-level curation TSV
  accessed_at: '2026-10-10T06:34:11Z'
  support: supports
  summary: Mint/path, source nodes, counts/units, decisions, definitions, ontology
    parents and seeder output traced. Exact full-document reproduction was asserted.
- evidence_id: R0
  kind: authority
  reference: docs/CURATION.md
  locator: Decision model, MIxS triads, status gates and GOLD context-parent exclusions;
    native checklist and HARMONIZATION also read
  accessed_at: '2026-10-10T06:34:11Z'
  support: supports
  summary: Parents must be strictly broader. Source occurrence, triad roles and taxonomic
    associations do not establish identity, characteristic presence or mechanism.
- evidence_id: W1
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: 'Reused dated complete-sheet census: Biosample 244951, Organism 532019,
    SequencingProject636914, Study63806 rows including headers; classification workbook2422
    rows'
  accessed_at: '2026-10-10T06:34:11Z'
  support: supports
  summary: Reused prior preparation census, inspected exact-path members/joins, and
    rechecked bulk SHA256 and classification SHA256. Bulk 238974789 bytes; classification
    https://gold.jgi.doe.gov/download?mode=ecosystempaths is 84174 bytes, SHA2563933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396.
    This later snapshot does not replace either frozen manifest.
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: P1
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/AEM.01825-06
  locator: DOI:10.1128/AEM.01825-06; primary full text, Test materials and Surface
    sampling and sample processing
  accessed_at: '2026-10-10T06:34:11Z'
  support: supports
  summary: Plastic arena seats are explicitly treated as sampled surface materials.
    This is controlled inoculation evidence for the surface distinction, not exact
    GOLD provenance or natural colonization.
- evidence_id: V1
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/38030062780
  locator: Exact-base merge-group QC metadata/log and fresh local checks
  accessed_at: '2026-10-10T06:34:11Z'
  support: supports
  summary: 'CI at exact base486d97f799fe3df7d8933b6c9a5dab69e48f7f59 passed authoritative
    QC: 658 tests passed,3 skipped;4 structured-review contract tests passed. Fresh
    local target/schema, corpus, label, history, causal and term-request gates also
    passed. CI is not claimed as a newly run local full QC.'
- evidence_id: S1
  kind: search
  reference: data/raw/, curation/, research/, reports/, reviews/
  locator: Ignored-inclusive rg by target IDs, labels and slugs, plus full pathlib
    traversal/structured parsing
  accessed_at: '2026-10-10T06:34:11Z'
  support: context_only
  summary: No target causal overlay among32 scanned files and no prior native scientific
    review of this exact target among111 bundles. Legacy sand-microcosm review and
    contextual parent reviews remain historical evidence. Bounded ontology-label searches
    found no exact proposed sand-filter, sand-microcosm, seat-surface or SBR-EBPR
    match; an incidental passangers substring is not Sanger evidence.
  search_scope: rg --no-ignore --hidden and pathlib/CSV/YAML parsing include gitignored
    content within the listed repository surfaces. All14 raw TSVs and top-level curation
    TSVs were parsed; target overlay identifiers were checked in32 files. Searches
    are not an assertion of universal external absence.
assessments:
- assessment_id: A1
  area: identity
  topic: Resolved identity, grounding and source scope
  outcome: supported
  summary: The full path resolves a stadium-associated Seat surface, identifier habitatmech:GOLD.2934cf4eee,
    node8306. The train-car record has a different mint and context, despite sharing
    the display label. Neither the word seat nor the source path makes the surface
    identical to the whole seat, building, or stadium. Preserve both mints unless
    source equivalence is separately established.
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  evidence_ids:
  - E1
  - E2
  - R0
  - W1
  - P1
- assessment_id: A2
  area: grounding
  topic: Strict parents versus source context
  outcome: concern
  summary: The sole parent habitatmech:GOLD.2d40c87aeb is the Stadium source grouping.
    A surface on seating is located in or part of a venue but is not a kind of venue.
    This is a supported hierarchy defect even though original sample membership is
    unavailable.
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  evidence_ids:
  - E1
  - E2
  - R0
  - P1
- assessment_id: A3
  area: evidence
  topic: Primary evidence, taxon and mechanism scope
  outcome: supported
  summary: Buttner et al. inspect plastic arena-seat surfaces and distinguish their
    sampled material from the overall test setting. This controlled, inoculated study
    supports the surface/material distinction only; it is neither a field stadium
    survey nor evidence for exact GOLD node8306 membership or natural characteristic
    taxa. Generic seat-surface evidence cannot supply the missing source cohort.
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  evidence_ids:
  - E1
  - E2
  - R0
  - W1
  - P1
- assessment_id: A4
  area: provenance
  topic: Source extent, units, decisions and historical limitations
  outcome: unknown
  summary: Frozen GOLD data row1251 has node8306 and zero organism/study/biosample
    counts. No assertion count or unit is emitted. Later classification row182 retains
    the exact stadium-seat path; the full later bulk Biosample/Organism census has
    no exact-path members or joined projects. This is a bounded source availability
    limitation, not proof of an empty stadium microbiome. Decision data row322 is
    CLASS, so SEEDED remains correct.
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  evidence_ids:
  - E1
  - E2
  - W1
  - R0
  details: "Current exact-field source-row details (data rows exclude headers/comments):\n\
    [\n  {\n    \"file\": \"data/raw/gold_ecosystem_paths.tsv\",\n    \"matches\"\
    : [\n      {\n        \"data_row\": 1251,\n        \"row\": {\n          \"canonical_path\"\
    : \"Engineered > Built environment > City > Stadium > Seat surface\",\n      \
    \    \"ecosystem\": \"Engineered\",\n          \"ecosystem_category\": \"Built\
    \ environment\",\n          \"ecosystem_type\": \"City\",\n          \"ecosystem_subtype\"\
    : \"Stadium\",\n          \"specific_ecosystem\": \"Seat surface\",\n        \
    \  \"leaf_label\": \"Seat surface\",\n          \"depth\": \"5\",\n          \"\
    gold_node_count\": \"1\",\n          \"organism_count\": \"0\",\n          \"\
    study_count\": \"0\",\n          \"biosample_count\": \"0\",\n          \"total_assertions\"\
    : \"0\",\n          \"gold_node_ids\": \"gold.ecosystem:8306\"\n        }\n  \
    \    }\n    ]\n  },\n  {\n    \"file\": \"curation/decisions.tsv\",\n    \"matches\"\
    : [\n      {\n        \"data_row\": 322,\n        \"row\": {\n          \"identifier\"\
    : \"habitatmech:GOLD.2934cf4eee\",\n          \"decision\": \"CONFIRM_UNGROUNDED\"\
    ,\n          \"object_id\": \"\",\n          \"object_label\": \"\",\n       \
    \   \"grounding_status\": \"\",\n          \"curator\": \"claude-opus-5\",\n \
    \         \"date\": \"2026-08-12\",\n          \"notes\": \"Class-level sweep\
    \ (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice\
    \ matched this label by any search route. Whether the concept is a habitat at\
    \ all was NOT assessed, so this is not yet a term-request candidate.\",\n    \
    \      \"review_depth\": \"CLASS\",\n          \"category\": \"\",\n         \
    \ \"relation\": \"\"\n        }\n      }\n    ]\n  },\n  {\n    \"file\": \"data/habitats/PATHS.tsv\"\
    ,\n    \"matches\": [\n      {\n        \"data_row\": 1589,\n        \"row\":\
    \ {\n          \"identifier\": \"habitatmech:GOLD.2934cf4eee\",\n          \"\
    slug\": \"seat_surface\"\n        }\n      }\n    ]\n  }\n]"
  dimensions:
  - name: native_state
    value: UNGROUNDED/SEEDED
    definition: Current generated grounding and curation state, not this review verdict
    evidence_ids:
    - E1
    - E2
  - name: frozen_source_unit
    value: zero-organism count intentionally omitted
    definition: Frozen GOLD count semantics; later BIOSAMPLE/project counts are not
      substitutes
    evidence_ids:
    - E1
    - E2
- assessment_id: A5
  area: completeness
  topic: Optional content and status are not automatically enriched
  outcome: supported
  summary: 'No target causal graph, environmental parameter, discussion or dataset
    claim is emitted. Optional emptiness is not itself a defect. 1 source concept(s),
    0 ITEM-reviewed: status and history reproduce. Parent/child taxa, parameters and
    observations are not inherited. No definitions, curation events or status promotions
    are made by this review.'
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  evidence_ids:
  - E1
  - E2
  - R0
  - S1
- assessment_id: A6
  area: schema
  topic: Validation scope versus scientific judgement
  outcome: supported
  summary: Fresh native validators passed; exact-base CI QC passed with3 skipped tests.
    ID-label checks report1178 canonical,1 synonym,5 accepted exceptions and2057 entries
    without an adapter. These are deterministic checks, not ecological certification
    or a general SSSOM/KGX readiness finding.
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  evidence_ids:
  - V1
findings:
- finding_id: F1
  issue_key: gold-2934cf4eee-seat-surface-stadium-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Exclude the stadium context parent from its seat surface
  description: The generated source hierarchy asserts that a seat surface is a kind
    of Stadium. A contacted seating surface and its surrounding venue are different
    entity types; retain the source location in the attestation rather than as an
    is-a parent.
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - E2
  - R0
  - W1
  - P1
  rule_id: HabitatMech:strictly-broader-parents
  native_severity: major
  normalization_reason: Material entity-type or hierarchy error, or missing supported
    ontology relationship; target and source record are resolved, so not classified
    as an ambiguous-target blocker.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated habitat YAML is read-only
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated habitat YAML is read-only
actions:
- action_id: ACT1
  description: Add a guarded exclusion for habitatmech:GOLD.2934cf4eee, exact path
    Engineered > Built environment > City > Stadium > Seat surface, expected parent
    habitatmech:GOLD.2d40c87aeb. Preserve mint, node8306, path, zero-count omission
    and CLASS/SEEDED state. Do not merge with train-car seating or invent a whole-seat/venue
    genus.
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.2934cf4eee
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated habitat YAML is read-only
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated habitat YAML is read-only
  generator: scripts/seed_from_sources.py; normal validated canary workflow
  acceptance_checks:
  - Change only the named maintained input in a separately authorized curation session;
    never hand-edit generated habitats.
  - Run just seed, then inspect just seed-canary habitatmech:GOLD.2934cf4eee --force
    before any broader write.
  - Preserve unaffected identity, source units, node provenance and prior history;
    allow only intended generator-derived status/history changes.
  - Append native session history for actual curation, regenerate semantic-map/site
    products if changed, and pass just qc plus just validate-products.
  - Save a new native follow-up with this exact finding identity; do not rewrite this
    review.
limitations:
- The exact stadium, seat material, sample type and source members are not established
  by the frozen zero-count row.
- The primary arena-seat experiment is controlled inoculation, not a natural stadium
  community survey. No observational taxa or health implications are inferred.
- Frozen and later source snapshots have different scope and units. Bounded missing
  entries are not evidence of ecological absence.
- No paid research, habitat/curation mutation, GitHub mutation, or publication was
  performed. Existing bundles remain immutable.
- Scientific coverage is not inferred from schema checks. Adapter-free label rows
  and three skipped baseline tests remain explicitly unverified by those gates.
tags:
- scientific-review
- engineered
- individual-record
- read-only
```
