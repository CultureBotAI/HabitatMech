# Scoped correction follow-up: Biofilm

- Review: 20261011T042443Z-biofilm__5327749c-followup
- Repository: culturebotai/HabitatMech
- Started UTC: 2026-10-11T04:22:55.773051Z
- Finished UTC: 2026-10-11T04:24:43.572455Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact source-parent exclusion resolves the container-as-genus edge while retaining the independent biofilm/biofilter genus, qualified identity, source provenance, counts and units, and NARROW/SEEDED state. The separate shared mapping-endpoint finding remains major and open in #1398. This correction does not certify original frozen member semantics or SSSOM/KGX compatibility.

## Scope And Provenance

Reassess every finding on one exact corrected habitat.

Selection: All findings of 20261011T041045Z-biofilm__5327749c on habitatmech:GOLD.905d58ea72
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5d35a305e4c40281520a41b7789777fafc164997.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.905d58ea72 | data/habitats/engineered/biofilm__5327749c.yaml | generated | Biofilm |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native validate | passed | True | habitatmech:GOLD.905d58ea72 | Started 2026-10-11T04:22:10.165340+00:00; finished 2026-10-11T04:22:12.724314+00:00. Command scope is exact; other records in a validation command were not scientifically reviewed by this observation. |
| Native validate-strict | passed | True | habitatmech:GOLD.905d58ea72 | Started 2026-10-11T04:22:26.449832+00:00; finished 2026-10-11T04:22:31.856777+00:00. Command scope is exact; other records in a validation command were not scientifically reviewed by this observation. |
| Native verify-corpus | passed | True | habitatmech:GOLD.905d58ea72 | Started 2026-10-11T04:22:31.857538+00:00; finished 2026-10-11T04:22:48.508430+00:00. Command scope is exact; other records in a validation command were not scientifically reviewed by this observation. |
| Native validate-products | passed | True | habitatmech:GOLD.905d58ea72 | Started 2026-10-11T04:22:48.509134+00:00; finished 2026-10-11T04:23:39.842540+00:00. Command scope is exact; other records in a validation command were not scientifically reviewed by this observation. |
| Native validate-history | passed | True | habitatmech:GOLD.905d58ea72 | Started 2026-10-11T04:23:39.843250+00:00; finished 2026-10-11T04:23:46.321702+00:00. Command scope is exact; other records in a validation command were not scientifically reviewed by this observation. |
| Native validate-causal-all | passed | True | habitatmech:GOLD.905d58ea72 | Started 2026-10-11T04:23:46.322405+00:00; finished 2026-10-11T04:23:51.130410+00:00. Command scope is exact; other records in a validation command were not scientifically reviewed by this observation. |
| Native term-requests-check | passed | True | habitatmech:GOLD.905d58ea72 | Started 2026-10-11T04:23:51.131181+00:00; finished 2026-10-11T04:24:06.664627+00:00. Command scope is exact; other records in a validation command were not scientifically reviewed by this observation. |
| Native lint | passed | True | habitatmech:GOLD.905d58ea72 | Started 2026-10-11T04:24:06.665499+00:00; finished 2026-10-11T04:24:06.876393+00:00. Command scope is exact; other records in a validation command were not scientifically reviewed by this observation. |
| Focused regressions | passed | True | habitatmech:GOLD.905d58ea72 | 53 passed. New regressions failed before the maintained corrections. |
| Full publication checks | skipped | False | habitatmech:GOLD.905d58ea72 | Final QC, rebuilt semantic map/site and protected CI are recorded separately on PR #1901 before merge; not claimed complete by this observation. |
| Mechanism-specific resources | not_applicable | False | habitatmech:GOLD.905d58ea72 | No gene, regulator, expression dataset or causal mechanism assertion was added; iModulonDB is not applicable. |

## Scientific And Domain Assessments

### Resolved context parent

grounding: supported. Targets: habitatmech:GOLD.905d58ea72.

The exact source-parent exclusion resolves the container-as-genus edge while retaining the independent biofilm/biofilter genus, qualified identity, source provenance, counts and units, and NARROW/SEEDED state. The separate shared mapping-endpoint finding remains major and open in #1398. This correction does not certify original frozen member semantics or SSSOM/KGX compatibility.

### Unchanged source and lifecycle claims

provenance: supported. Targets: habitatmech:GOLD.905d58ea72.

Exact source nodes, path, counts and units, qualified identifier and native status are unchanged. No source counts are summed, no association is promoted to characteristic occurrence, and no optional biology is fabricated.

### Original member evidence limitation

scope: unknown. Targets: habitatmech:GOLD.905d58ea72.

Later retained official GOLD workbooks and classification corroborate bounded context, not original frozen-node membership. Absence of later exact members does not disprove the habitat; this limitation prevents universal member-level certification.

### Remaining mapping endpoint

representation: concern. Targets: habitatmech:GOLD.905d58ea72.

The retained-source mint still emits narrowMatch against an implicit ontology-parent endpoint. This shared contract issue remains open, not a formal SKOS self-link prohibition.

## Findings

### F1: Source context is not an established is-a parent

major / resolved / confirmed; issue key: habitatmech-gold.905d58ea72-context-parent.

The exact source-parent exclusion resolves the container-as-genus edge while retaining the independent biofilm/biofilter genus, qualified identity, source provenance, counts and units, and NARROW/SEEDED state. The separate shared mapping-endpoint finding remains major and open in #1398. This correction does not certify original frozen member semantics or SSSOM/KGX compatibility.

Disposition: The maintained input removes the unsupported assertion; exact target and whole-corpus comparisons preserve unrelated fields. No guessed source-identity replacement was made.

### F2: Narrow mapping compares to an implicit ontology-parent endpoint

major / open / confirmed; issue key: habitatmech-gold.905d58ea72-mapping-endpoint-contract.

This record retains the deterministic source-path mint, but emits skos:narrowMatch from the source concept to the record. The seeder narrowing comparison is with an ontology parent. The schema instead describes source-to-record mapping and requires omission when the record is the source concept. This is a local endpoint-contract mismatch, not a formal SKOS self-link prohibition.

Disposition: The bounded hierarchy correction does not alter schema/emitter/consumer mapping endpoints; #1398 remains open.

## Recommended Actions And Acceptance Checks

### A2

Resolve the shared endpoint contract in #1398 across schema, emitters and actual consumers, preserving qualified identities. Do not globally swap broad/narrow or merge records.

- Explicit subject, predicate, object and status agree on every affected route. Audit actual SSSOM and KGX exports against current kg-microbe before any readiness claim.
- Preserve source keys, paths, counts/units and unrelated claims. Append required curation history; run focused tests, strict validation, corpus reproduction, relevant ontology/history/product checks and full QC. Save a linked successor review; do not rewrite this observation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| RAW | data/raw/gold_ecosystem_paths.tsv; Exact-field and pipe-member matches; logical TSV row numbers include header, not physical multiline lines | supports | {"data/raw/gold_ecosystem_paths.tsv": [{"logical_row": 1162, "row": {"biosample_count": "0", "canonical_path": "Engineered &gt; Artificial ecosystem &gt; Water channel system &gt; Indoor &gt; Biofilm", "depth": "5", "ecosystem": "Engineered", "ecosystem_category": "Artificial ecosystem", "ecosystem_subtype": "Indoor", "ecosystem_type": "Water channel system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:8494", "leaf_label": "Biofilm", "organism_count": "0", "specific_ecosystem": "Biofilm", "study_count": "0", "total_assertions": "0"}}]} |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md; .claude/skills/curate-yaml-record/references/review-checklist.md | supports | Parents must be strictly broader, not mere context. Preserve source-qualified identities and units. CLASS/SEEDED or missing optional biology is not automatically a defect. REVIEWED requires ITEM decisions for every contributing source. |
| CODE | src/habitatmech/seed.py; src/habitatmech/schema/habitatmech.yaml; resolve_gold:752-849; ingest_gold; SourceAttestation.mapping_predicate:317; apply_curated_definitions | supports | resolve_gold retains path mints and emits narrowMatch while comparing with an implicit ontology parent. ingest_gold emits source-to-record attestations. SourceAttestation.mapping_predicate specifies omission when the record is the source concept. Guarded exclusions remove only immediate GOLD parent contributions. |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.obo; Exact [Term] stanzas, definitions, typed synonyms and named parents | supports | Inspected exact ENVO stanzas and official OLS responses: [{"id": "ENVO:00002034", "label": "biofilm", "obsolete": false, "sha256": "165b76c7c01a18a5a6f9ec1a58fe7f30fbc210b2a890341bd6254c7762043396", "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002034"}]. Typed synonyms and direct is-a edges checked; parent-owned aliases are not target claims. |
| CLASS | https://gold.jgi.doe.gov/; site data sheet; exact five-level path | supports | Retained official classification workbook exact path: [{"path": "Engineered &gt; Artificial ecosystem &gt; Water channel system &gt; Indoor &gt; Biofilm", "row": 67, "slug": "biofilm__5327749c", "values": ["8494", "Engineered", "Artificial ecosystem", "Water channel system", "Indoor", "Biofilm"]}]. The original download endpoint is not retained; no fabricated endpoint or fresh-download claim. |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; All four sheets scanned: {"Biosample": 244951, "Organism": 532019, "SequencingProject": 636914, "Study": 63806} | supports | Complete exact-path census in a retained later export, not fresh live data or original frozen membership: {"Biosample": {"count": 35, "examples": [{"data": {"BIOSAMPLE GOLD ID": "Gb0411712", "BIOSAMPLE NAME": "Biofilm microbial communities from Eawag, Duebendorf, Switzerland - A01", "BIOSAMPLE NCBI TAX NAME": "biofilm metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "biofilm"}, "row": 230916}, {"data": {"BIOSAMPLE GOLD ID": "Gb0411713", "BIOSAMPLE NAME": "Biofilm microbial communities from Eawag, Duebendorf, Switzerland - A02", "BIOSAMPLE NCBI TAX NAME": "biofilm metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "biofilm"}, "row": 230917}, {"data": {"BIOSAMPLE GOLD ID": "Gb0411714", "BIOSAMPLE NAME": "Biofilm microbial communities from Eawag, Duebendorf, Switzerland - A03", "BIOSAMPLE NCBI TAX NAME": "biofilm metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "biofilm"}, "row": 230918}, {"data": {"BIOSAMPLE GOLD ID": "Gb0411715", "BIOSAMPLE NAME": "Biofilm microbial communities from Eawag, Duebendorf, Switzerland - A05", "BIOSAMPLE NCBI TAX NAME": "biofilm metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "biofilm"}, "row": 230919}, {"data": {"BIOSAMPLE GOLD ID": "Gb0411716", "BIOSAMPLE NAME": "Biofilm microbial communities from Eawag, Duebendorf, Switzerland - A06", "BIOSAMPLE NCBI TAX NAME": "biofilm metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "biofilm"}, "row": 230920}]}, "Organism": {"count": 0, "examples": []}}; sequencing projects=35; distinct joined studies=1. Zero matches mean only this exact later path, not biological absence. Frozen ORGANISM counts are not replaced by these BioSample totals. |
| CURRENT | data/habitats/engineered/biofilm__5327749c.yaml; Entire post-correction generated record | supports | The exact source-parent exclusion resolves the container-as-genus edge while retaining the independent biofilm/biofilter genus, qualified identity, source provenance, counts and units, and NARROW/SEEDED state. The separate shared mapping-endpoint finding remains major and open in #1398. This correction does not certify original frozen member semantics or SSSOM/KGX compatibility. |
| FIX | curation/gold_parent_exclusions.tsv; Exact source mint habitatmech:GOLD.905d58ea72 | supports | Maintained, reviewed input only; native dry seed, inspected canary and full apply regenerated the record. No raw inventory, identifier or status changes. |
| HISTORY | history/mappings/biofilm__5327749c/2026-10-11T042136Z-codex-gpt-5-9de1ba.yaml; Entire native append-only curation session | supports | Codex attribution and scoped hierarchy correction with preserved source identity. |
| PRIOR | reviews/structured/20261011T041045Z-biofilm__5327749c/review.yaml; All original findings | context_only | Immutable predecessor retained byte-for-byte. This observation reconciles every finding on the same exact target. |
| REGRESSION | tests/test_biofilm_biofilter_review_fixes.py; tests/test_gold_parent_exclusions.py; tests/test_doormat_dust_curation.py; 53 passing focused tests; two newly added tests first failed against the original inputs | supports | Whole-corpus with/without tests constrain parent exclusions to six exact records and the old-definition comparison to one. Explicit source, count, status and alias assertions pass. A separate comparison to the trusted main baseline permits only the reviewed parent/definition and corresponding generated audit event differences. |
| VALID | Documented native commands in checks | supports | All fourteen post-correction native commands passed. Full-corpus checks are deterministic and do not extend scientific review beyond this exact target. OAK retains 2,057 no-adapter skips. |

## Limits And Additional Notes

- Adversarial self-review, not independent scientific approval.
- Original frozen GOLD node membership was unavailable at the configured dump path; the later retained official export is not a reconstruction.
- Fresh OAK validation retains 2,057 no-adapter skips; schema, reproduction and label checks do not certify scientific scope.
- Final publication QC and map/site checks are reported separately on PR #1901.
- Shared mapping-endpoint issue #1398 remains open; no SSSOM/KGX readiness claim.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T042443Z-biofilm__5327749c-followup
kind: record
repository: culturebotai/HabitatMech
title: 'Scoped correction follow-up: Biofilm'
started_at: '2026-10-11T04:22:55.773051Z'
finished_at: '2026-10-11T04:24:43.572455Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Continuing agent involved in prior curation; not independent
    scientific approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'The exact source-parent exclusion resolves the container-as-genus edge while
  retaining the independent biofilm/biofilter genus, qualified identity, source provenance,
  counts and units, and NARROW/SEEDED state. The separate shared mapping-endpoint
  finding remains major and open in #1398. This correction does not certify original
  frozen member semantics or SSSOM/KGX compatibility.'
source:
  git_revision: 5d35a305e4c40281520a41b7789777fafc164997
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
  - path: data/habitats/aquatic/biofilm__cc6fe05a.yaml
    sha256: d74a10cf8b222933fe527e768b9a263392abbee9fc6498a90458fb5442121cda
    role: context
  - path: data/habitats/engineered/biofilm__5327749c.yaml
    sha256: 101f9f032af761e2c2632357439ae92e4951b6a611758f93f724b36cb9dc9b28
    role: target
  - path: data/habitats/engineered/indoor.yaml
    sha256: 8b50235a59549442cacf6f1345043b2eb8a62c4b68022eed6c14d66e867f9f8f
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
  - path: history/mappings/biofilm__5327749c/2026-10-11T042136Z-codex-gpt-5-9de1ba.yaml
    sha256: e9a5aa6ef8ef1b528ea22a0dacbb1115001ce0a71b050b6dd497ba1e4247424e
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260925T132617Z-biofilm__5327749c.md
    sha256: 2a1dda88998fbd607620bf5522fb9f42d72e097071ba7993d2cc44059e98b9fc
    role: context
  - path: reviews/structured/20261011T041045Z-biofilm__5327749c/review.yaml
    sha256: e3daaec5a30eab8828e05cc87201c6d0b096ec24974248583f58a8824cf00d0f
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
  - path: tests/test_biofilm_biofilter_review_fixes.py
    sha256: 891715ad112f3321186851d152230a1b3c6e05292b02d2cfc5c6133b698f69d8
    role: context
  - path: tests/test_doormat_dust_curation.py
    sha256: 9ad5e79415bcdfaaab77d2762fc05a3087107b6fa071325e6307783e75624365
    role: context
  - path: tests/test_gold_parent_exclusions.py
    sha256: 70102b4004bbe5d7f6a8fbd59bb47f2228832951f038b345e4ff94bcbaaf90e3
    role: context
targets:
- target_id: habitatmech:GOLD.905d58ea72
  path: data/habitats/engineered/biofilm__5327749c.yaml
  label: Biofilm
  kind: generated
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/decisions.tsv
    role: Source-concept identity and broader grounding
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded GOLD context-parent correction
  - repository: culturebotai/HabitatMech
    path: curation/term_requests.tsv
    role: Authored habitat definition and genus
  - repository: culturebotai/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD source concepts and unit-specific counts
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained generation and harmonization
scope:
  description: Reassess every finding on one exact corrected habitat.
  selection: All findings of 20261011T041045Z-biofilm__5327749c on habitatmech:GOLD.905d58ea72
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.905d58ea72
checks:
- check_id: C1
  name: Native validate
  command: just validate data/habitats/engineered/biofilm__5327749c.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - VALID
  summary: Started 2026-10-11T04:22:10.165340+00:00; finished 2026-10-11T04:22:12.724314+00:00.
    Command scope is exact; other records in a validation command were not scientifically
    reviewed by this observation.
- check_id: C2
  name: Native validate-strict
  command: just validate-strict data/habitats/engineered/biofilm__3952f25d.yaml data/habitats/engineered/biofilm__5327749c.yaml
    data/habitats/engineered/biofilm__a5211c59.yaml data/habitats/engineered/biofilm__b4a8654c.yaml
    data/habitats/engineered/biofilm__c8931a26.yaml data/habitats/engineered/biofilter__9cdb9879.yaml
    data/habitats/engineered/biofilter__c190958d.yaml
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - VALID
  summary: Started 2026-10-11T04:22:26.449832+00:00; finished 2026-10-11T04:22:31.856777+00:00.
    Command scope is exact; other records in a validation command were not scientifically
    reviewed by this observation.
- check_id: C3
  name: Native verify-corpus
  command: just verify-corpus
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - VALID
  summary: Started 2026-10-11T04:22:31.857538+00:00; finished 2026-10-11T04:22:48.508430+00:00.
    Command scope is exact; other records in a validation command were not scientifically
    reviewed by this observation.
- check_id: C4
  name: Native validate-products
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - VALID
  summary: Started 2026-10-11T04:22:48.509134+00:00; finished 2026-10-11T04:23:39.842540+00:00.
    Command scope is exact; other records in a validation command were not scientifically
    reviewed by this observation.
- check_id: C5
  name: Native validate-history
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - VALID
  summary: Started 2026-10-11T04:23:39.843250+00:00; finished 2026-10-11T04:23:46.321702+00:00.
    Command scope is exact; other records in a validation command were not scientifically
    reviewed by this observation.
- check_id: C6
  name: Native validate-causal-all
  command: just validate-causal-all
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - VALID
  summary: Started 2026-10-11T04:23:46.322405+00:00; finished 2026-10-11T04:23:51.130410+00:00.
    Command scope is exact; other records in a validation command were not scientifically
    reviewed by this observation.
- check_id: C7
  name: Native term-requests-check
  command: just term-requests-check
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - VALID
  summary: Started 2026-10-11T04:23:51.131181+00:00; finished 2026-10-11T04:24:06.664627+00:00.
    Command scope is exact; other records in a validation command were not scientifically
    reviewed by this observation.
- check_id: C8
  name: Native lint
  command: just lint
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - VALID
  summary: Started 2026-10-11T04:24:06.665499+00:00; finished 2026-10-11T04:24:06.876393+00:00.
    Command scope is exact; other records in a validation command were not scientifically
    reviewed by this observation.
- check_id: C9
  name: Focused regressions
  command: .venv/bin/python -m pytest -q tests/test_biofilm_biofilter_review_fixes.py
    tests/test_gold_parent_exclusions.py tests/test_doormat_dust_curation.py
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - REGRESSION
  summary: 53 passed. New regressions failed before the maintained corrections.
- check_id: C10
  name: Full publication checks
  status: skipped
  required: false
  target_ids:
  - habitatmech:GOLD.905d58ea72
  summary: 'Final QC, rebuilt semantic map/site and protected CI are recorded separately
    on PR #1901 before merge; not claimed complete by this observation.'
- check_id: C11
  name: Mechanism-specific resources
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.905d58ea72
  summary: No gene, regulator, expression dataset or causal mechanism assertion was
    added; iModulonDB is not applicable.
evidence:
- evidence_id: RAW
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  summary: '{"data/raw/gold_ecosystem_paths.tsv": [{"logical_row": 1162, "row": {"biosample_count":
    "0", "canonical_path": "Engineered > Artificial ecosystem > Water channel system
    > Indoor > Biofilm", "depth": "5", "ecosystem": "Engineered", "ecosystem_category":
    "Artificial ecosystem", "ecosystem_subtype": "Indoor", "ecosystem_type": "Water
    channel system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:8494",
    "leaf_label": "Biofilm", "organism_count": "0", "specific_ecosystem": "Biofilm",
    "study_count": "0", "total_assertions": "0"}}]}'
  support: supports
  accessed_at: '2026-10-11T04:10:45.000000Z'
  locator: Exact-field and pipe-member matches; logical TSV row numbers include header,
    not physical multiline lines
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/record-review-profile.md;
    .claude/skills/curate-yaml-record/references/review-checklist.md
  summary: Parents must be strictly broader, not mere context. Preserve source-qualified
    identities and units. CLASS/SEEDED or missing optional biology is not automatically
    a defect. REVIEWED requires ITEM decisions for every contributing source.
  support: supports
  accessed_at: '2026-10-11T04:10:45.000000Z'
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py; src/habitatmech/schema/habitatmech.yaml
  summary: resolve_gold retains path mints and emits narrowMatch while comparing with
    an implicit ontology parent. ingest_gold emits source-to-record attestations.
    SourceAttestation.mapping_predicate specifies omission when the record is the
    source concept. Guarded exclusions remove only immediate GOLD parent contributions.
  support: supports
  accessed_at: '2026-10-11T04:10:45.000000Z'
  locator: resolve_gold:752-849; ingest_gold; SourceAttestation.mapping_predicate:317;
    apply_curated_definitions
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.obo
  summary: 'Inspected exact ENVO stanzas and official OLS responses: [{"id": "ENVO:00002034",
    "label": "biofilm", "obsolete": false, "sha256": "165b76c7c01a18a5a6f9ec1a58fe7f30fbc210b2a890341bd6254c7762043396",
    "url": "https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002034"}].
    Typed synonyms and direct is-a edges checked; parent-owned aliases are not target
    claims.'
  support: supports
  accessed_at: '2026-10-11T04:02:52.528590Z'
  locator: Exact [Term] stanzas, definitions, typed synonyms and named parents
  snapshot_sha256: 7f5a6580d1b59166da07a54f9aa907a76f86079b7082e089192f04df91fd7d5b
- evidence_id: CLASS
  kind: database
  reference: https://gold.jgi.doe.gov/
  summary: 'Retained official classification workbook exact path: [{"path": "Engineered
    > Artificial ecosystem > Water channel system > Indoor > Biofilm", "row": 67,
    "slug": "biofilm__5327749c", "values": ["8494", "Engineered", "Artificial ecosystem",
    "Water channel system", "Indoor", "Biofilm"]}]. The original download endpoint
    is not retained; no fabricated endpoint or fresh-download claim.'
  support: supports
  accessed_at: '2026-10-11T04:10:01.304495Z'
  locator: site data sheet; exact five-level path
  snapshot_sha256: 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  summary: 'Complete exact-path census in a retained later export, not fresh live
    data or original frozen membership: {"Biosample": {"count": 35, "examples": [{"data":
    {"BIOSAMPLE GOLD ID": "Gb0411712", "BIOSAMPLE NAME": "Biofilm microbial communities
    from Eawag, Duebendorf, Switzerland - A01", "BIOSAMPLE NCBI TAX NAME": "biofilm
    metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "biofilm"}, "row": 230916}, {"data":
    {"BIOSAMPLE GOLD ID": "Gb0411713", "BIOSAMPLE NAME": "Biofilm microbial communities
    from Eawag, Duebendorf, Switzerland - A02", "BIOSAMPLE NCBI TAX NAME": "biofilm
    metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "biofilm"}, "row": 230917}, {"data":
    {"BIOSAMPLE GOLD ID": "Gb0411714", "BIOSAMPLE NAME": "Biofilm microbial communities
    from Eawag, Duebendorf, Switzerland - A03", "BIOSAMPLE NCBI TAX NAME": "biofilm
    metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "biofilm"}, "row": 230918}, {"data":
    {"BIOSAMPLE GOLD ID": "Gb0411715", "BIOSAMPLE NAME": "Biofilm microbial communities
    from Eawag, Duebendorf, Switzerland - A05", "BIOSAMPLE NCBI TAX NAME": "biofilm
    metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "biofilm"}, "row": 230919}, {"data":
    {"BIOSAMPLE GOLD ID": "Gb0411716", "BIOSAMPLE NAME": "Biofilm microbial communities
    from Eawag, Duebendorf, Switzerland - A06", "BIOSAMPLE NCBI TAX NAME": "biofilm
    metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "biofilm"}, "row": 230920}]},
    "Organism": {"count": 0, "examples": []}}; sequencing projects=35; distinct joined
    studies=1. Zero matches mean only this exact later path, not biological absence.
    Frozen ORGANISM counts are not replaced by these BioSample totals.'
  support: supports
  accessed_at: '2026-10-11T04:10:01.304495Z'
  locator: 'All four sheets scanned: {"Biosample": 244951, "Organism": 532019, "SequencingProject":
    636914, "Study": 63806}'
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: CURRENT
  kind: record_content
  reference: data/habitats/engineered/biofilm__5327749c.yaml
  locator: Entire post-correction generated record
  summary: 'The exact source-parent exclusion resolves the container-as-genus edge
    while retaining the independent biofilm/biofilter genus, qualified identity, source
    provenance, counts and units, and NARROW/SEEDED state. The separate shared mapping-endpoint
    finding remains major and open in #1398. This correction does not certify original
    frozen member semantics or SSSOM/KGX compatibility.'
  accessed_at: '2026-10-11T04:24:43.572455Z'
  support: supports
- evidence_id: FIX
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact source mint habitatmech:GOLD.905d58ea72
  summary: Maintained, reviewed input only; native dry seed, inspected canary and
    full apply regenerated the record. No raw inventory, identifier or status changes.
  accessed_at: '2026-10-11T04:24:43.572455Z'
  support: supports
- evidence_id: HISTORY
  kind: record_content
  reference: history/mappings/biofilm__5327749c/2026-10-11T042136Z-codex-gpt-5-9de1ba.yaml
  locator: Entire native append-only curation session
  summary: Codex attribution and scoped hierarchy correction with preserved source
    identity.
  accessed_at: '2026-10-11T04:24:43.572455Z'
  support: supports
- evidence_id: PRIOR
  kind: prior_review
  reference: reviews/structured/20261011T041045Z-biofilm__5327749c/review.yaml
  locator: All original findings
  summary: Immutable predecessor retained byte-for-byte. This observation reconciles
    every finding on the same exact target.
  accessed_at: '2026-10-11T04:24:43.572455Z'
  support: context_only
- evidence_id: REGRESSION
  kind: validation
  reference: tests/test_biofilm_biofilter_review_fixes.py; tests/test_gold_parent_exclusions.py;
    tests/test_doormat_dust_curation.py
  locator: 53 passing focused tests; two newly added tests first failed against the
    original inputs
  summary: Whole-corpus with/without tests constrain parent exclusions to six exact
    records and the old-definition comparison to one. Explicit source, count, status
    and alias assertions pass. A separate comparison to the trusted main baseline
    permits only the reviewed parent/definition and corresponding generated audit
    event differences.
  accessed_at: '2026-10-11T04:24:43.572455Z'
  support: supports
- evidence_id: VALID
  kind: validation
  reference: Documented native commands in checks
  summary: All fourteen post-correction native commands passed. Full-corpus checks
    are deterministic and do not extend scientific review beyond this exact target.
    OAK retains 2,057 no-adapter skips.
  accessed_at: '2026-10-11T04:24:43.572455Z'
  support: supports
assessments:
- assessment_id: D1
  area: grounding
  topic: Resolved context parent
  outcome: supported
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - CURRENT
  - FIX
  - PRIOR
  - REGRESSION
  - ONT
  summary: 'The exact source-parent exclusion resolves the container-as-genus edge
    while retaining the independent biofilm/biofilter genus, qualified identity, source
    provenance, counts and units, and NARROW/SEEDED state. The separate shared mapping-endpoint
    finding remains major and open in #1398. This correction does not certify original
    frozen member semantics or SSSOM/KGX compatibility.'
- assessment_id: D2
  area: provenance
  topic: Unchanged source and lifecycle claims
  outcome: supported
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - CURRENT
  - RAW
  - REGRESSION
  - HISTORY
  - VALID
  summary: Exact source nodes, path, counts and units, qualified identifier and native
    status are unchanged. No source counts are summed, no association is promoted
    to characteristic occurrence, and no optional biology is fabricated.
- assessment_id: D3
  area: scope
  topic: Original member evidence limitation
  outcome: unknown
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - BULK
  - CLASS
  - PRIOR
  summary: Later retained official GOLD workbooks and classification corroborate bounded
    context, not original frozen-node membership. Absence of later exact members does
    not disprove the habitat; this limitation prevents universal member-level certification.
- assessment_id: D4
  area: representation
  topic: Remaining mapping endpoint
  outcome: concern
  target_ids:
  - habitatmech:GOLD.905d58ea72
  evidence_ids:
  - CURRENT
  - CODE
  - RULES
  - PRIOR
  summary: The retained-source mint still emits narrowMatch against an implicit ontology-parent
    endpoint. This shared contract issue remains open, not a formal SKOS self-link
    prohibition.
findings:
- finding_id: F1
  issue_key: habitatmech-gold.905d58ea72-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is not an established is-a parent
  description: 'The exact source-parent exclusion resolves the container-as-genus
    edge while retaining the independent biofilm/biofilter genus, qualified identity,
    source provenance, counts and units, and NARROW/SEEDED state. The separate shared
    mapping-endpoint finding remains major and open in #1398. This correction does
    not certify original frozen member semantics or SSSOM/KGX compatibility.'
  target_ids:
  - habitatmech:GOLD.905d58ea72
  field_paths:
  - parent_habitats
  evidence_ids:
  - CURRENT
  - FIX
  - PRIOR
  - REGRESSION
  - VALID
  - RULES
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Materially unsupported identity, hierarchy, definition scope
    or shared representation contract affects scientific reuse.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained correction owner
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T041045Z-biofilm__5327749c
    finding_id: F1
  disposition_reason: The maintained input removes the unsupported assertion; exact
    target and whole-corpus comparisons preserve unrelated fields. No guessed source-identity
    replacement was made.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1902
- finding_id: F2
  issue_key: habitatmech-gold.905d58ea72-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping compares to an implicit ontology-parent endpoint
  description: This record retains the deterministic source-path mint, but emits skos:narrowMatch
    from the source concept to the record. The seeder narrowing comparison is with
    an ontology parent. The schema instead describes source-to-record mapping and
    requires omission when the record is the source concept. This is a local endpoint-contract
    mismatch, not a formal SKOS self-link prohibition.
  target_ids:
  - habitatmech:GOLD.905d58ea72
  field_paths:
  - source_attestations[0].mapping_predicate
  - grounding_status
  evidence_ids:
  - CURRENT
  - FIX
  - PRIOR
  - REGRESSION
  - VALID
  - RULES
  - CODE
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Materially unsupported identity, hierarchy, definition scope
    or shared representation contract affects scientific reuse.
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained correction owner
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained correction owner
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: culturebotai/HabitatMech
    review_id: 20261011T041045Z-biofilm__5327749c
    finding_id: F2
  disposition_reason: 'The bounded hierarchy correction does not alter schema/emitter/consumer
    mapping endpoints; #1398 remains open.'
actions:
- action_id: A2
  description: 'Resolve the shared endpoint contract in #1398 across schema, emitters
    and actual consumers, preserving qualified identities. Do not globally swap broad/narrow
    or merge records.'
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.905d58ea72
  owner_paths:
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained correction owner
  - repository: culturebotai/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained correction owner
  generator: 'In separately authorized curation: dry seed, inspect exact canary, regenerate
    affected corpus and products'
  acceptance_checks:
  - Explicit subject, predicate, object and status agree on every affected route.
    Audit actual SSSOM and KGX exports against current kg-microbe before any readiness
    claim.
  - Preserve source keys, paths, counts/units and unrelated claims. Append required
    curation history; run focused tests, strict validation, corpus reproduction, relevant
    ontology/history/product checks and full QC. Save a linked successor review; do
    not rewrite this observation.
limitations:
- Adversarial self-review, not independent scientific approval.
- Original frozen GOLD node membership was unavailable at the configured dump path;
  the later retained official export is not a reconstruction.
- Fresh OAK validation retains 2,057 no-adapter skips; schema, reproduction and label
  checks do not certify scientific scope.
- 'Final publication QC and map/site checks are reported separately on PR #1901.'
- 'Shared mapping-endpoint issue #1398 remains open; no SSSOM/KGX readiness claim.'
related_reviews:
- repository: culturebotai/HabitatMech
  review_id: 20261011T041045Z-biofilm__5327749c
  relationship: Reassesses every finding and resolves only the bounded correction
links:
- https://github.com/CultureBotAI/HabitatMech/pull/1901
tags:
- scientific-review
- record-review
- followup
- engineered
```
