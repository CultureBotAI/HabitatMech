# organic waste material: source, identity and hierarchy review

- Review: 20261009T201157Z-organic_waste_material
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-09T19:45:46Z
- Finished UTC: 2026-10-09T20:11:57Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

PREGO self-identity, GOLD close mapping, counts and 25 source-ranked associations are reproduced. A confirmed ontology-synonym scope inflation and a provisional Solid Waste parent-scope concern remain. The native REVIEWED status is mechanically correct, not independent scientific approval.

## Scope And Provenance

Entire generated record and every contributing source concept.

Selection: Exact path and identifier selected as one of the next six engineered review leads, not a claim of full corpus completion.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24829e1d73449a2bd2815b1140099926f8b16ea0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00002873 | data/habitats/engineered/organic_waste_material.yaml | generated | organic waste material |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Schema | passed | True | ENVO:00002873 | No issues found. |
| Closed schema | passed | True | ENVO:00002873 | One file,zero errors. |
| Full native QC | passed | True | ENVO:00002873 | 649 passed,3 skipped; all native quality gates passed at captured baseline. |
| Ontology labels | passed | True | ENVO:00002873 | 1178 canonical,1 synonym,5 exceptions,2057 no-adapter skips; labels do not certify semantics. |
| Existing structured reviews | passed | True | ENVO:00002873 | 49 existing bundles valid before saving this batch. |
| Input stability and full-document reproduction | passed | True | ENVO:00002873 | Original55 hashes unchanged before expanded61-input native capture; full in-memory build_document equality confirmed for this target. |
| Target causal and expression-module checks | not_applicable | False | ENVO:00002873 | No target causal overlay or gene/expression claim. Full QC still validates all32 repository causal overlays. |
| Original upstream re-extraction and per-association evidence | unavailable | False | ENVO:00002873 | Original GOLD node/edge and August workbook not recovered in bounded ignored-inclusive searches; original PREGO evidence unavailable. Frozen inventory is reproducible, but membership-level ecological support remains limited. |

## Scientific And Domain Assessments

### Physical habitat and source identity

identity: supported. Targets: ENVO:00002873.

The PREGO concept is explicitly ENVO:00002873, a waste-material class, not a disposal process. GOLD retains close rather than exact source equivalence. The absent definition reflects the inspected ENVO term, which has no definition and an editorial suggestion to consider a merge; the suggestion is not an enacted obsoletion or curator authorization.

### Exact identity, source mapping and broader scope

grounding: concern. Targets: ENVO:00002873.

The ENVO ID and label are active and match the frozen slice. Aggregate EXACT comes from PREGO, not a promotion of GOLD's CLOSE mapping. The ENVO-sourced organic waste synonym is broad in the pinned ontology but emitted as exact; GOLD/PREGO related aliases are separate assertions and should survive a typed-synonym fix.

### All parent contribution routes

graph: concern. Targets: ENVO:00002873.

The independent biological-waste parent is supported. The other parent, NLM Solid Waste, excludes dissolved materials in sewage or industrial discharges. The generic ENVO identity has no explicit solid-only restriction in the inspected source. GOLD's qualified branch alone does not establish that restriction for every PREGO-associated member; the universal parent remains provisional rather than proven false from missing axioms.

### Frozen counts, source versions and MIxS roles

quantity: supported. Targets: ENVO:00002873.

gold_ecosystem_paths data row 1375: nodes 8411&#124;8412&#124;8413, all counts zero. PREGO habitat data row 251: 34 distinct taxa, 34 direct assertions, max score4, annotated_genomes_isolates&#124;environmental_samples. Taxa data rows 6529-6553 contain the 25 emitted entries, all score4/direct TRUE/environmental_samples/no corroboration. Decisions rows676 and1443 are ITEM REVIEW for GOLD.71a8554be0 and PREGO.4bb6ce49fc; PATHS row701; ontology term row7351 and named subclass row5475. No target term request or GOLD-parent exclusion. Current member counts are not substituted for frozen counts or summed across units. No contextual triad is adopted as target identity.

### Native status, history and reproduction

provenance: supported. Targets: ENVO:00002873.

Actual GOLD gold_leaf_synonym -&gt; curated_review_of_gold_leaf_synonym, CLOSE/skos:closeMatch to ENVO:00002873; PREGO self-grounding supplies EXACT. Both of two source concepts are ITEM-reviewed, hence REVIEWED. ENVO:01000373 is an independent ontology parent; mesh:D062611 is only the GOLD Solid waste path contribution. The prior source-synonym correction preserves GOLD as RELATED but does not repair flattened ontology synonym scopes. Whole-document reproduction passed. Saving this observation does not endorse prior scientific decisions or promote status.

### Optional parameters, literature, graphs and datasets

completeness: supported. Targets: ENVO:00002873.

The whole target and contributing inventories were inspected. Empty optional slots are not negative biological evidence. No parameter, causal edge, definition or characteristic-organism claim is inferred from external study examples or unrelated parent/child records.

### Structured expression-module applicability

evidence: not_applicable. Targets: ENVO:00002873.

No gene, regulator, protein or transcriptomic claim triggers iModulonDB. Not invoking that adapter is not evidence against habitat eligibility.

### Native checks and scientific limits

schema: supported. Targets: ENVO:00002873.

Required native checks passed. Mechanical validity does not adjudicate identity, parent scope or ecological support. Original upstream re-extraction is unavailable and label skips are explicit.

### Every emitted taxon and source confidence semantics

evidence: supported. Targets: ENVO:00002873.

All 25 emitted taxon IDs and names resolve identically in current NCBI Taxonomy; 24 are species-rank entries and Alkaliphilus oremlandii OhILAs (350688) is strain rank. Rank1-25 is a deterministic selection from a 34-taxon pool, not abundance or prevalence. All retained rows tie at score4 and direct TRUE, so the extractor's CURIE-string tie-break determines their order; the 9 omitted candidates and original PREGO documents were not recovered. The two aggregate evidence channels must not be attributed to every listed taxon: these 25 frozen rows say environmental_samples only. No is_characteristic/reference claim is present.

## Findings

### F1: ENVO broad synonym is emitted as an exact synonym

major / open / confirmed; issue key: envo-00002873-organic-waste-synonym-scope.

The organic waste synonym attributed to ENVO is EXACT_SYNONYM in this record. The inspected official ENVO OWL asserts hasBroadSynonym, while the frozen slice stores only the spelling and ConceptStore.get unconditionally emits EXACT_SYNONYM. The corrected GOLD related synonym and PREGO related synonyms do not repair this independent ontology-sourced assertion. OLS's flat synonyms list has no typed obo_synonym here, so the primary OWL was used for scope.

### F2: A solid-waste source context constrains a generic merged waste class

major / open / provisional; issue key: envo-00002873-solid-waste-parent-scope.

mesh:D062611 is introduced only by the GOLD Solid waste branch, then published as a strict parent of the generic PREGO-grounded ENVO00002873 record. The inspected ENVO class has no solid-only scope and NLM excludes dissolved waste material. No original GOLD or PREGO member set was recovered to demonstrate that all material in this merged identity satisfies NLM's scope. This is unsupported universal scope, not a claim that all organic waste is liquid or a proved formal disjointness.

## Recommended Actions And Acceptance Checks

### ACT1

Resolve through the shared typed-ontology-synonym contract in #1249. Recover and preserve source scopes reproducibly; emit broad scope for this ENVO assertion while retaining independent GOLD/PREGO related aliases and verified exact synonyms elsewhere.

- Add a regression for ENVO00002873 organic waste broad scope plus exact and unknown-scope controls.
- Re-extract or curate through governed inputs with provenance; do not patch generated YAML or merely change a checksum.
- Run focused schema/strict validation, corpus reproduction, native history and full QC; run label validation for grounding changes.

### ACT2

Adjudicate generic organic-waste versus solid-waste-qualified source scope. Preserve PREGO's generic ENVO identity. If the parent is rejected, exclude only the GOLD.71a8554be0 exact path/mesh:D062611 contribution; do not remove the independent ENVO01000373 parent or conflate close mapping with exact equivalence.

- Document evidence resolving NLM's dissolved-material exclusion for the source and generic target; retain uncertainty until then.
- Any later exclusion must preserve all 25 taxon rows, pool34/count unit/score/channels, scoped aliases and native source decisions.
- Run focused schema/strict validation, corpus reproduction, native history and full QC; run label validation for grounding changes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/engineered/organic_waste_material.yaml; Entire generated file; immediate parents read as context | supports | ENGINEERED / EXACT / REVIEWED. No definition; four scoped synonyms, parents ENVO:01000373 and mesh:D062611; GOLD and PREGO attestations; 25 PREGO taxa; four history events including the 2026-10-07 GOLD alias-scope correction. No parameters, xrefs, cited characteristic claims, causal graphs, discussions or datasets. |
| E2 | data/raw/gold_ecosystem_paths.tsv; Exact source keys; all row numbers are 1-based data rows excluding comments/header | supports | gold_ecosystem_paths data row 1375: nodes 8411&#124;8412&#124;8413, all counts zero. PREGO habitat data row 251: 34 distinct taxa, 34 direct assertions, max score4, annotated_genomes_isolates&#124;environmental_samples. Taxa data rows 6529-6553 contain the 25 emitted entries, all score4/direct TRUE/environmental_samples/no corroboration. Decisions rows676 and1443 are ITEM REVIEW for GOLD.71a8554be0 and PREGO.4bb6ce49fc; PATHS row701; ontology term row7351 and named subclass row5475. No target term request or GOLD-parent exclusion. |
| E3 | src/habitatmech/seed.py; resolve_gold, apply_decision, ingest_gold, ontology and GOLD parent contribution, build_document | supports | Actual GOLD gold_leaf_synonym -&gt; curated_review_of_gold_leaf_synonym, CLOSE/skos:closeMatch to ENVO:00002873; PREGO self-grounding supplies EXACT. Both of two source concepts are ITEM-reviewed, hence REVIEWED. ENVO:01000373 is an independent ontology parent; mesh:D062611 is only the GOLD Solid waste path contribution. The prior source-synonym correction preserves GOLD as RELATED but does not repair flattened ontology synonym scopes. |
| E4 | https://gold.jgi.doe.gov/download?mode=site_excel; Complete Biosample, Organism, SequencingProject and Study sheets | partial | No exact-path BioSample or Organism member in the complete later workbook. Classification row413 retains path8413; row412 is the distinct Biochar descendant, not a target sample. Do not transfer descendants or parent taxon/parameter tables to this record. Complete census: 244951/532019/636914/63806 rows including headers. This Oct9 snapshot is later than frozen provenance. |
| E5 | https://gold.jgi.doe.gov/download?mode=ecosystempaths; site data, 2422 rows after reset_dimensions; terminal row stated in E4 | context_only | The exact terminal classification persists; prefix descendants were separately distinguished and never counted as exact target members. |
| E6 | curation/; history/; research/; reports/; reviews/; data/raw/; Ignored-inclusive identifier/label/slug/mint traversal and exact structured keys | context_only | Scanned 43 curation,225 history,121 research,1274 report and98 structured-review files. Parsed all14 raw TSVs,7 top-level maintained curation tables and PATHS. No earlier native bundle targets this exact path. No target causal overlay, term request or parameter contribution was found. Original upstream membership and original PREGO association documents were not recovered. |
| E7 | build/review-20261009o-resumed-qc.log; Fresh baseline full QC, focused schema/strict, label check and native review check | supports | QC exited0:649 passed,3 skipped;224 history records,3208 strict-valid and exactly reproduced habitats,32 causal overlays,curation floor,site,252 redirects and term-request gates pass. Each target separately passed schema and strict checks. Fresh labels:1178 canonical,1 synonym,5 exceptions,2057 no-adapter skips. Existing49 bundles valid. |
| E8 | CLAUDE.md; Semantic invariants; docs/CURATION.md; HabitatRecord, SourceAttestation, GroundingStatusEnum and CharacteristicTaxon schema | supports | Parents must be strictly broader. Source mapping endpoints are source concept -&gt; record ID. Counts require their units; PREGO score/rank is not abundance or characteristic status. REVIEWED requires ITEM decisions for all merged sources. A review bundle does not itself promote status. |
| S1 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:00002873; Active terms and their official parent endpoints: ENVO:00002873, ENVO:01000373 | supports | The ENVO ID and label are active and match the frozen slice. Aggregate EXACT comes from PREGO, not a promotion of GOLD's CLOSE mapping. The ENVO-sourced organic waste synonym is broad in the pinned ontology but emitted as exact; GOLD/PREGO related aliases are separate assertions and should survive a typed-synonym fix. The independent biological-waste parent is supported. The other parent, NLM Solid Waste, excludes dissolved materials in sewage or industrial discharges. The generic ENVO identity has no explicit solid-only restriction in the inspected source. GOLD's qualified branch alone does not establish that restriction for every PREGO-associated member; the universal parent remains provisional rather than proven false from missing axioms. |
| S2 | https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl; ENVO_00002873, ENVO_01000373, ENVO_00002276 XML class blocks | supports | Official current commit verified through GitHub. ENVO00002873 has hasBroadSynonym organic waste, named parent ENVO01000373, no definition and an editorial merge suggestion. Neither it nor its inspected waste parent establishes a solid-only restriction. |
| S3 | https://id.nlm.nih.gov/mesh/M0568791.json; Solid Waste preferred concept scopeNote for mesh:D062611 | supports | NLM describes discarded solid, semi-solid or contained materials and explicitly excludes dissolved materials in domestic sewage, irrigation returns and industrial discharges. A physical-state label alone is not enough to settle this scope. |
| S6 | https://github.com/CultureBotAI/HabitatMech/issues/1249; Issue body and OPEN state inspected | context_only | Existing shared typed-synonym issue identifies the untyped ontology pipe and unconditional EXACT_SYNONYM emission. This target supplies a new specific broad-to-exact witness, not a claim that every synonym is wrong. |
| S4 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1270,136093,1393,1396,1397,1402,1404,1408,1409,1455,1482,148604,1580,1587,1601,1624,1667,180295,28031,28042,292806,338044,33936,350688,36808; Bulk XML:33 requested IDs across two records,33 returned Taxon entries,zero XML errors | supports | All 25 emitted taxon IDs and names resolve identically in current NCBI Taxonomy; 24 are species-rank entries and Alkaliphilus oremlandii OhILAs (350688) is strain rank. Rank1-25 is a deterministic selection from a 34-taxon pool, not abundance or prevalence. All retained rows tie at score4 and direct TRUE, so the extractor's CURIE-string tie-break determines their order; the 9 omitted candidates and original PREGO documents were not recovered. The two aggregate evidence channels must not be attributed to every listed taxon: these 25 frozen rows say environmental_samples only. No is_characteristic/reference claim is present. |
| S5 | https://doi.org/10.3390/microorganisms10020293; PMID35208748 / PMC8879827 fullTextXML, methods2.1/2.3 and AppendixC | supports | PREGO combines heterogeneous evidence channels with channel-specific confidence formulas bounded(0,5]. Fixed resource confidence for genome/isolate evidence differs from environmental-sample co-occurrence. These scores are not abundance, prevalence, occupancy or a claim of characteristic biology. |

## Limits And Additional Notes

- Original GOLD node/edge and frozen August membership were not recovered in bounded searches. The later public workbook is not a replacement for frozen provenance.
- All source and ontology searches are bounded. Missing examples or optional values do not establish biological absence or justify invented identities.
- QC skips3 tests; label validation skips2057 no-adapter terms. These deterministic checks do not establish scientific correctness.
- All emitted taxonomy labels/IDs were checked, but original PREGO per-association evidence was unavailable. Confidence scores do not prove characteristic biology; not every association was independently verified against primary ecological evidence.
- Read-only observation saved before separately authorized corrections/publication. Actions are proposed work, not completed fixes.
- No paid research, source refresh, scientific status promotion or automatic resolution of historical findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T201157Z-organic_waste_material
kind: record
repository: CultureBotAI/HabitatMech
title: 'organic waste material: source, identity and hierarchy review'
started_at: '2026-10-09T19:45:46Z'
finished_at: '2026-10-09T20:11:57Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent continuing scientific review and separately authorized
    publication; no independent scientific approval claimed.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: PREGO self-identity, GOLD close mapping, counts and 25 source-ranked associations
  are reproduced. A confirmed ontology-synonym scope inflation and a provisional Solid
  Waste parent-scope concern remain. The native REVIEWED status is mechanically correct,
  not independent scientific approval.
source:
  git_revision: 24829e1d73449a2bd2815b1140099926f8b16ea0
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
    sha256: 0602cca13e6495da256a6f1cfd5897462f73f9739a729447862017d93c148efd
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: cc4da2e7e5e8750e6c023683014aa37a909230280f231eec5be7c71795340312
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 34c70a2b13b5051130d0fc15952aeea74aafc49c3ad88a96ce67f6da41a52d12
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/samples/class_swept_unscreened-20260814.tsv
    sha256: 27fce2849781b21f8fdb434aaaffac0f55e51bef84f1c1ea7d7feecd11d8471e
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
  - path: data/habitats/engineered/bioreactor.yaml
    sha256: c0a5f4d06130d949810c29b15f5874b4e9673b23dc188161d699412c2bea0c02
    role: context
  - path: data/habitats/engineered/chemical_product.yaml
    sha256: d5039d8e0f3f8c77680371d162d7934f5ada70d63130e5a1b4bcab154bb77b1f
    role: context
  - path: data/habitats/engineered/city.yaml
    sha256: 3a52eece16e4be7b9a7d1d19a57cfaac92dcb6e97c7a0bd3ef08dddad0814c7a
    role: context
  - path: data/habitats/engineered/industrial_wastewater.yaml
    sha256: 07698df721a169cd55c2d1ce80027df8c8a3140536ba99eee312272887ce8768
    role: context
  - path: data/habitats/engineered/material.yaml
    sha256: 01b2767b0983a3ed85de20b759119f14102b6c1333dad051466e7b94667ffa02
    role: context
  - path: data/habitats/engineered/organic_dairy_farm.yaml
    sha256: c8c647d25e2d4731f1ee7bd714952d1ca00a15ccca48b0710a2f26ce955feb0c
    role: context
  - path: data/habitats/engineered/organic_waste_material.yaml
    sha256: 8f0f59b82c69cc6ba5fab56d4bf40c3cf33ac8eb9ab58dd32a4b8b93875cc9c6
    role: target
  - path: data/habitats/engineered/paper.yaml
    sha256: 183ff1a853f7783cb29f0404c05ac67ca018cd93a8ad34cf9e1c101223bc8793
    role: context
  - path: data/habitats/engineered/park.yaml
    sha256: e3cc6bf0d136339d98fc205220b5acb12c57544e17cdd8d18b60a5b762c6163d
    role: context
  - path: data/habitats/engineered/partial_nitrification_anammox_pna.yaml
    sha256: bca83d5e1f1c72ea951ec088eaf23ada93822960252f70c081b2a14b8515c957
    role: context
  - path: data/habitats/engineered/pcr_blank_control.yaml
    sha256: 46f5385ddb5c38656a87918cb6a5076d1a9e1abb32a9fb739e8b71988ca3578b
    role: context
  - path: data/habitats/engineered/sheet_of_paper.yaml
    sha256: 6499a0ee1a610df73a6a8b8eb32193ea88e2b45b40850c6b5cbdc627054fad6b
    role: context
  - path: data/habitats/engineered/solid_waste.yaml
    sha256: 4cd78657634aca99d98863d643419c7deb56b8835d9f47d144d08247457736d4
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
  - path: history/mappings/anaerobic_zone/2026-10-07T033547Z-codex-gpt-5-d36e47.yaml
    sha256: f7027c603782fbc30e9e55bdf57d8649607b1ac94275c72fd49df2c8ad17998d
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260923T183929Z-aerobic_zone.md
    sha256: 15372ba808c0ef233930195600d9fecff599f58b8379918f765f489554754ed9
    role: context
  - path: reports/yaml_record_review/20260924T104251Z-sheet_of_paper.md
    sha256: cc4f1ac519d0e5d7d73e3f38ef6cc034385b7e565e506f2909d81cf538118edb
    role: context
  - path: reports/yaml_record_review/20261007T032222Z-anaerobic_zone.md
    sha256: 0d18ff1020121cf559347efe6f1fe8a54e6ff0b134a23cafafb60e04ab7b5e3a
    role: context
  - path: reports/yaml_record_review/20261007T082502Z-biochar__4f716948.md
    sha256: 996004cbce7c05357e71efb67b9618b6e113c95808203a7a63ae0fc4027051e5
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
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 92adf631fa099120a497ff7001473e659347d23ac9b418f04cd341ddad5d2a89
    role: context
scope:
  description: Entire generated record and every contributing source concept.
  selection: Exact path and identifier selected as one of the next six engineered
    review leads, not a claim of full corpus completion.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00002873
  exclusions:
  - target: All other HabitatMech records
    reason: Parents, children, same-label concepts and source examples inform this
      target only.
targets:
- target_id: ENVO:00002873
  path: data/habitats/engineered/organic_waste_material.yaml
  label: organic waste material
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input, source transform or generator owner
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input, source transform or generator owner
checks:
- check_id: C1
  name: Schema
  status: passed
  required: true
  target_ids:
  - ENVO:00002873
  command: env UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/organic_waste_material.yaml
  exit_code: 0
  summary: No issues found.
- check_id: C2
  name: Closed schema
  status: passed
  required: true
  target_ids:
  - ENVO:00002873
  command: env UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/organic_waste_material.yaml
  exit_code: 0
  summary: One file,zero errors.
- check_id: C3
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - ENVO:00002873
  command: env UV_CACHE_DIR=build/uv-cache just qc > build/review-20261009o-resumed-qc.log
    2>&1
  exit_code: 0
  summary: 649 passed,3 skipped; all native quality gates passed at captured baseline.
- check_id: C4
  name: Ontology labels
  status: passed
  required: true
  target_ids:
  - ENVO:00002873
  command: env UV_CACHE_DIR=build/uv-cache just validate-products
  exit_code: 0
  summary: 1178 canonical,1 synonym,5 exceptions,2057 no-adapter skips; labels do
    not certify semantics.
- check_id: C5
  name: Existing structured reviews
  status: passed
  required: true
  target_ids:
  - ENVO:00002873
  command: env UV_CACHE_DIR=build/uv-cache uv run python scripts/record_review.py
    check
  exit_code: 0
  summary: 49 existing bundles valid before saving this batch.
- check_id: C6
  name: Input stability and full-document reproduction
  status: passed
  required: true
  target_ids:
  - ENVO:00002873
  exit_code: 0
  summary: Original55 hashes unchanged before expanded61-input native capture; full
    in-memory build_document equality confirmed for this target.
- check_id: C7
  name: Target causal and expression-module checks
  status: not_applicable
  required: false
  target_ids:
  - ENVO:00002873
  summary: No target causal overlay or gene/expression claim. Full QC still validates
    all32 repository causal overlays.
- check_id: C8
  name: Original upstream re-extraction and per-association evidence
  status: unavailable
  required: false
  target_ids:
  - ENVO:00002873
  summary: Original GOLD node/edge and August workbook not recovered in bounded ignored-inclusive
    searches; original PREGO evidence unavailable. Frozen inventory is reproducible,
    but membership-level ecological support remains limited.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/engineered/organic_waste_material.yaml
  locator: Entire generated file; immediate parents read as context
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: ENGINEERED / EXACT / REVIEWED. No definition; four scoped synonyms, parents
    ENVO:01000373 and mesh:D062611; GOLD and PREGO attestations; 25 PREGO taxa; four
    history events including the 2026-10-07 GOLD alias-scope correction. No parameters,
    xrefs, cited characteristic claims, causal graphs, discussions or datasets.
- evidence_id: E2
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Exact source keys; all row numbers are 1-based data rows excluding comments/header
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: 'gold_ecosystem_paths data row 1375: nodes 8411|8412|8413, all counts zero.
    PREGO habitat data row 251: 34 distinct taxa, 34 direct assertions, max score4,
    annotated_genomes_isolates|environmental_samples. Taxa data rows 6529-6553 contain
    the 25 emitted entries, all score4/direct TRUE/environmental_samples/no corroboration.
    Decisions rows676 and1443 are ITEM REVIEW for GOLD.71a8554be0 and PREGO.4bb6ce49fc;
    PATHS row701; ontology term row7351 and named subclass row5475. No target term
    request or GOLD-parent exclusion.'
- evidence_id: E3
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: resolve_gold, apply_decision, ingest_gold, ontology and GOLD parent contribution,
    build_document
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: Actual GOLD gold_leaf_synonym -> curated_review_of_gold_leaf_synonym, CLOSE/skos:closeMatch
    to ENVO:00002873; PREGO self-grounding supplies EXACT. Both of two source concepts
    are ITEM-reviewed, hence REVIEWED. ENVO:01000373 is an independent ontology parent;
    mesh:D062611 is only the GOLD Solid waste path contribution. The prior source-synonym
    correction preserves GOLD as RELATED but does not repair flattened ontology synonym
    scopes.
- evidence_id: E4
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  locator: Complete Biosample, Organism, SequencingProject and Study sheets
  accessed_at: '2026-10-09T20:11:57Z'
  support: partial
  summary: 'No exact-path BioSample or Organism member in the complete later workbook.
    Classification row413 retains path8413; row412 is the distinct Biochar descendant,
    not a target sample. Do not transfer descendants or parent taxon/parameter tables
    to this record. Complete census: 244951/532019/636914/63806 rows including headers.
    This Oct9 snapshot is later than frozen provenance.'
  snapshot_sha256: 5f48b2f50fb2a9257754960a0f0e12dc6e8fa121e97c3e9f4497249e5fe6e439
- evidence_id: E5
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  locator: site data, 2422 rows after reset_dimensions; terminal row stated in E4
  accessed_at: '2026-10-09T20:11:57Z'
  support: context_only
  summary: The exact terminal classification persists; prefix descendants were separately
    distinguished and never counted as exact target members.
  snapshot_sha256: 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
- evidence_id: E6
  kind: search
  reference: curation/; history/; research/; reports/; reviews/; data/raw/
  locator: Ignored-inclusive identifier/label/slug/mint traversal and exact structured
    keys
  accessed_at: '2026-10-09T20:11:57Z'
  support: context_only
  summary: Scanned 43 curation,225 history,121 research,1274 report and98 structured-review
    files. Parsed all14 raw TSVs,7 top-level maintained curation tables and PATHS.
    No earlier native bundle targets this exact path. No target causal overlay, term
    request or parameter contribution was found. Original upstream membership and
    original PREGO association documents were not recovered.
  search_scope: 'No gitignore filtering: Path.rglob and rg --no-ignore --hidden. Expected
    GOLD_nodes.tsv, GOLD_edges.tsv and goldData.xlsx also searched under build, data/raw
    and configured kg-microbe/data. Configured transformed/prego is missing. These
    are bounded local-source misses, not global absence claims.'
- evidence_id: E7
  kind: validation
  reference: build/review-20261009o-resumed-qc.log
  locator: Fresh baseline full QC, focused schema/strict, label check and native review
    check
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: QC exited0:649 passed,3 skipped;224 history records,3208 strict-valid and
    exactly reproduced habitats,32 causal overlays,curation floor,site,252 redirects
    and term-request gates pass. Each target separately passed schema and strict checks.
    Fresh labels:1178 canonical,1 synonym,5 exceptions,2057 no-adapter skips. Existing49
    bundles valid.
- evidence_id: E8
  kind: record_content
  reference: CLAUDE.md
  locator: Semantic invariants; docs/CURATION.md; HabitatRecord, SourceAttestation,
    GroundingStatusEnum and CharacteristicTaxon schema
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: Parents must be strictly broader. Source mapping endpoints are source concept
    -> record ID. Counts require their units; PREGO score/rank is not abundance or
    characteristic status. REVIEWED requires ITEM decisions for all merged sources.
    A review bundle does not itself promote status.
- evidence_id: S1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO:00002873
  locator: 'Active terms and their official parent endpoints: ENVO:00002873, ENVO:01000373'
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: The ENVO ID and label are active and match the frozen slice. Aggregate
    EXACT comes from PREGO, not a promotion of GOLD's CLOSE mapping. The ENVO-sourced
    organic waste synonym is broad in the pinned ontology but emitted as exact; GOLD/PREGO
    related aliases are separate assertions and should survive a typed-synonym fix.
    The independent biological-waste parent is supported. The other parent, NLM Solid
    Waste, excludes dissolved materials in sewage or industrial discharges. The generic
    ENVO identity has no explicit solid-only restriction in the inspected source.
    GOLD's qualified branch alone does not establish that restriction for every PREGO-associated
    member; the universal parent remains provisional rather than proven false from
    missing axioms.
- evidence_id: S2
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl
  locator: ENVO_00002873, ENVO_01000373, ENVO_00002276 XML class blocks
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: Official current commit verified through GitHub. ENVO00002873 has hasBroadSynonym
    organic waste, named parent ENVO01000373, no definition and an editorial merge
    suggestion. Neither it nor its inspected waste parent establishes a solid-only
    restriction.
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: S3
  kind: authority
  reference: https://id.nlm.nih.gov/mesh/M0568791.json
  locator: Solid Waste preferred concept scopeNote for mesh:D062611
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: NLM describes discarded solid, semi-solid or contained materials and explicitly
    excludes dissolved materials in domestic sewage, irrigation returns and industrial
    discharges. A physical-state label alone is not enough to settle this scope.
- evidence_id: S6
  kind: prior_review
  reference: https://github.com/CultureBotAI/HabitatMech/issues/1249
  locator: Issue body and OPEN state inspected
  accessed_at: '2026-10-09T20:11:57Z'
  support: context_only
  summary: Existing shared typed-synonym issue identifies the untyped ontology pipe
    and unconditional EXACT_SYNONYM emission. This target supplies a new specific
    broad-to-exact witness, not a claim that every synonym is wrong.
- evidence_id: S4
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1270,136093,1393,1396,1397,1402,1404,1408,1409,1455,1482,148604,1580,1587,1601,1624,1667,180295,28031,28042,292806,338044,33936,350688,36808
  locator: Bulk XML:33 requested IDs across two records,33 returned Taxon entries,zero
    XML errors
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: 'All 25 emitted taxon IDs and names resolve identically in current NCBI
    Taxonomy; 24 are species-rank entries and Alkaliphilus oremlandii OhILAs (350688)
    is strain rank. Rank1-25 is a deterministic selection from a 34-taxon pool, not
    abundance or prevalence. All retained rows tie at score4 and direct TRUE, so the
    extractor''s CURIE-string tie-break determines their order; the 9 omitted candidates
    and original PREGO documents were not recovered. The two aggregate evidence channels
    must not be attributed to every listed taxon: these 25 frozen rows say environmental_samples
    only. No is_characteristic/reference claim is present.'
- evidence_id: S5
  kind: primary_source
  reference: https://doi.org/10.3390/microorganisms10020293
  locator: PMID35208748 / PMC8879827 fullTextXML, methods2.1/2.3 and AppendixC
  accessed_at: '2026-10-09T20:11:57Z'
  support: supports
  summary: PREGO combines heterogeneous evidence channels with channel-specific confidence
    formulas bounded(0,5]. Fixed resource confidence for genome/isolate evidence differs
    from environmental-sample co-occurrence. These scores are not abundance, prevalence,
    occupancy or a claim of characteristic biology.
assessments:
- assessment_id: A1
  area: identity
  topic: Physical habitat and source identity
  outcome: supported
  summary: The PREGO concept is explicitly ENVO:00002873, a waste-material class,
    not a disposal process. GOLD retains close rather than exact source equivalence.
    The absent definition reflects the inspected ENVO term, which has no definition
    and an editorial suggestion to consider a merge; the suggestion is not an enacted
    obsoletion or curator authorization.
  target_ids:
  - ENVO:00002873
  evidence_ids:
  - E1
  - E2
  - E4
  - S1
  - S2
- assessment_id: A2
  area: grounding
  topic: Exact identity, source mapping and broader scope
  outcome: concern
  summary: The ENVO ID and label are active and match the frozen slice. Aggregate
    EXACT comes from PREGO, not a promotion of GOLD's CLOSE mapping. The ENVO-sourced
    organic waste synonym is broad in the pinned ontology but emitted as exact; GOLD/PREGO
    related aliases are separate assertions and should survive a typed-synonym fix.
  target_ids:
  - ENVO:00002873
  evidence_ids:
  - E1
  - E2
  - E3
  - E8
  - S1
- assessment_id: A3
  area: graph
  topic: All parent contribution routes
  outcome: concern
  summary: The independent biological-waste parent is supported. The other parent,
    NLM Solid Waste, excludes dissolved materials in sewage or industrial discharges.
    The generic ENVO identity has no explicit solid-only restriction in the inspected
    source. GOLD's qualified branch alone does not establish that restriction for
    every PREGO-associated member; the universal parent remains provisional rather
    than proven false from missing axioms.
  target_ids:
  - ENVO:00002873
  evidence_ids:
  - E1
  - E2
  - E3
  - S1
- assessment_id: A4
  area: quantity
  topic: Frozen counts, source versions and MIxS roles
  outcome: supported
  summary: 'gold_ecosystem_paths data row 1375: nodes 8411|8412|8413, all counts zero.
    PREGO habitat data row 251: 34 distinct taxa, 34 direct assertions, max score4,
    annotated_genomes_isolates|environmental_samples. Taxa data rows 6529-6553 contain
    the 25 emitted entries, all score4/direct TRUE/environmental_samples/no corroboration.
    Decisions rows676 and1443 are ITEM REVIEW for GOLD.71a8554be0 and PREGO.4bb6ce49fc;
    PATHS row701; ontology term row7351 and named subclass row5475. No target term
    request or GOLD-parent exclusion. Current member counts are not substituted for
    frozen counts or summed across units. No contextual triad is adopted as target
    identity.'
  target_ids:
  - ENVO:00002873
  evidence_ids:
  - E1
  - E2
  - E4
  - E5
  - E8
- assessment_id: A5
  area: provenance
  topic: Native status, history and reproduction
  outcome: supported
  summary: Actual GOLD gold_leaf_synonym -> curated_review_of_gold_leaf_synonym, CLOSE/skos:closeMatch
    to ENVO:00002873; PREGO self-grounding supplies EXACT. Both of two source concepts
    are ITEM-reviewed, hence REVIEWED. ENVO:01000373 is an independent ontology parent;
    mesh:D062611 is only the GOLD Solid waste path contribution. The prior source-synonym
    correction preserves GOLD as RELATED but does not repair flattened ontology synonym
    scopes. Whole-document reproduction passed. Saving this observation does not endorse
    prior scientific decisions or promote status.
  target_ids:
  - ENVO:00002873
  evidence_ids:
  - E1
  - E2
  - E3
  - E7
- assessment_id: A6
  area: completeness
  topic: Optional parameters, literature, graphs and datasets
  outcome: supported
  summary: The whole target and contributing inventories were inspected. Empty optional
    slots are not negative biological evidence. No parameter, causal edge, definition
    or characteristic-organism claim is inferred from external study examples or unrelated
    parent/child records.
  target_ids:
  - ENVO:00002873
  evidence_ids:
  - E1
  - E2
  - E6
  - E8
- assessment_id: A7
  area: evidence
  topic: Structured expression-module applicability
  outcome: not_applicable
  summary: No gene, regulator, protein or transcriptomic claim triggers iModulonDB.
    Not invoking that adapter is not evidence against habitat eligibility.
  target_ids:
  - ENVO:00002873
  evidence_ids:
  - E1
- assessment_id: A8
  area: schema
  topic: Native checks and scientific limits
  outcome: supported
  summary: Required native checks passed. Mechanical validity does not adjudicate
    identity, parent scope or ecological support. Original upstream re-extraction
    is unavailable and label skips are explicit.
  target_ids:
  - ENVO:00002873
  evidence_ids:
  - E7
- assessment_id: A9
  area: evidence
  topic: Every emitted taxon and source confidence semantics
  outcome: supported
  summary: 'All 25 emitted taxon IDs and names resolve identically in current NCBI
    Taxonomy; 24 are species-rank entries and Alkaliphilus oremlandii OhILAs (350688)
    is strain rank. Rank1-25 is a deterministic selection from a 34-taxon pool, not
    abundance or prevalence. All retained rows tie at score4 and direct TRUE, so the
    extractor''s CURIE-string tie-break determines their order; the 9 omitted candidates
    and original PREGO documents were not recovered. The two aggregate evidence channels
    must not be attributed to every listed taxon: these 25 frozen rows say environmental_samples
    only. No is_characteristic/reference claim is present.'
  target_ids:
  - ENVO:00002873
  evidence_ids:
  - E1
  - E2
  - E3
  - S4
  - S5
findings:
- finding_id: F1
  issue_key: envo-00002873-organic-waste-synonym-scope
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: ENVO broad synonym is emitted as an exact synonym
  description: The organic waste synonym attributed to ENVO is EXACT_SYNONYM in this
    record. The inspected official ENVO OWL asserts hasBroadSynonym, while the frozen
    slice stores only the spelling and ConceptStore.get unconditionally emits EXACT_SYNONYM.
    The corrected GOLD related synonym and PREGO related synonyms do not repair this
    independent ontology-sourced assertion. OLS's flat synonyms list has no typed
    obo_synonym here, so the primary OWL was used for scope.
  target_ids:
  - ENVO:00002873
  field_paths:
  - synonyms[1].synonym_type
  evidence_ids:
  - E1
  - E2
  - E3
  - S2
  - S6
  rule_id: HabitatMech native identity, strictly-broader parent, evidence-scope and
    provenance rules
  native_severity: major
  normalization_reason: Material identity, hierarchy or source-representation concern.
    Provisional findings retain uncertainty and do not authorize guessed corrections.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator for proposed correction
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator for proposed correction
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained input or generator for proposed correction
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1249
- finding_id: F2
  issue_key: envo-00002873-solid-waste-parent-scope
  category: graph
  severity: major
  status: open
  certainty: provisional
  title: A solid-waste source context constrains a generic merged waste class
  description: mesh:D062611 is introduced only by the GOLD Solid waste branch, then
    published as a strict parent of the generic PREGO-grounded ENVO00002873 record.
    The inspected ENVO class has no solid-only scope and NLM excludes dissolved waste
    material. No original GOLD or PREGO member set was recovered to demonstrate that
    all material in this merged identity satisfies NLM's scope. This is unsupported
    universal scope, not a claim that all organic waste is liquid or a proved formal
    disjointness.
  target_ids:
  - ENVO:00002873
  field_paths:
  - parent_habitats
  - source_attestations
  evidence_ids:
  - E1
  - E2
  - E3
  - S1
  - S2
  - S3
  rule_id: HabitatMech native identity, strictly-broader parent, evidence-scope and
    provenance rules
  native_severity: major
  normalization_reason: Material identity, hierarchy or source-representation concern.
    Provisional findings retain uncertainty and do not authorize guessed corrections.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator for proposed correction
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator for proposed correction
actions:
- action_id: ACT1
  description: 'Resolve through the shared typed-ontology-synonym contract in #1249.
    Recover and preserve source scopes reproducibly; emit broad scope for this ENVO
    assertion while retaining independent GOLD/PREGO related aliases and verified
    exact synonyms elsewhere.'
  finding_ids:
  - F1
  target_ids:
  - ENVO:00002873
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator for proposed correction
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator for proposed correction
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained input or generator for proposed correction
  acceptance_checks:
  - Add a regression for ENVO00002873 organic waste broad scope plus exact and unknown-scope
    controls.
  - Re-extract or curate through governed inputs with provenance; do not patch generated
    YAML or merely change a checksum.
  - Run focused schema/strict validation, corpus reproduction, native history and
    full QC; run label validation for grounding changes.
  generator: Native maintained-input curation -> just seed -> just seed-canary ENVO:00002873
    -> just seed-apply --force -> just render; no hand-edited generated records.
- action_id: ACT2
  description: Adjudicate generic organic-waste versus solid-waste-qualified source
    scope. Preserve PREGO's generic ENVO identity. If the parent is rejected, exclude
    only the GOLD.71a8554be0 exact path/mesh:D062611 contribution; do not remove the
    independent ENVO01000373 parent or conflate close mapping with exact equivalence.
  finding_ids:
  - F2
  target_ids:
  - ENVO:00002873
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator for proposed correction
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator for proposed correction
  acceptance_checks:
  - Document evidence resolving NLM's dissolved-material exclusion for the source
    and generic target; retain uncertainty until then.
  - Any later exclusion must preserve all 25 taxon rows, pool34/count unit/score/channels,
    scoped aliases and native source decisions.
  - Run focused schema/strict validation, corpus reproduction, native history and
    full QC; run label validation for grounding changes.
  generator: Native maintained-input curation -> just seed -> just seed-canary ENVO:00002873
    -> just seed-apply --force -> just render; no hand-edited generated records.
limitations:
- Original GOLD node/edge and frozen August membership were not recovered in bounded
  searches. The later public workbook is not a replacement for frozen provenance.
- All source and ontology searches are bounded. Missing examples or optional values
  do not establish biological absence or justify invented identities.
- QC skips3 tests; label validation skips2057 no-adapter terms. These deterministic
  checks do not establish scientific correctness.
- All emitted taxonomy labels/IDs were checked, but original PREGO per-association
  evidence was unavailable. Confidence scores do not prove characteristic biology;
  not every association was independently verified against primary ecological evidence.
notes:
- Read-only observation saved before separately authorized corrections/publication.
  Actions are proposed work, not completed fixes.
- No paid research, source refresh, scientific status promotion or automatic resolution
  of historical findings.
tags:
- habitat
- engineered
- gold
- record-review
```
