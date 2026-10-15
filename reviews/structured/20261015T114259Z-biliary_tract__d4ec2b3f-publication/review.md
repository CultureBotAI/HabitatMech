# Publication follow-up: Biliary tract (habitatmech:GOLD.de5efc0eb8)

- Review: 20261015T114259Z-biliary_tract__d4ec2b3f-publication
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T11:42:02Z
- Finished UTC: 2026-10-15T11:42:59Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Issue URL punctuation is corrected under #2179. The full current target retains every scientific field and every prior scientific finding disposition; only the new curation-note URL boundaries differ. No new biological conclusion or resolved scientific finding is claimed.

## Scope And Provenance

Full current target re-read after an issue-URL punctuation-only correction; every scientific disposition reassessed.

Selection: One of fifteen repaired records or the unchanged biofilm target receiving a report-locator correction in this twenty-record PR cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 6e7f4baa9e2c8a5acc71e1af0b070cd82c84b798.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.de5efc0eb8 | data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml | generated | Biliary tract |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate-strict data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml | passed | True | habitatmech:GOLD.de5efc0eb8 | Actual execution 2026-10-15T11:40:21Z through 2026-10-15T11:40:29Z. uv run python scripts/validate_strict.py data/habitats/host_associated/benign_tumor_tissue.yaml data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml data/habitats/host_associated/bivalves.yaml<br>Validating 20 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      20<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.de5efc0eb8 | Actual execution 2026-10-15T11:40:29Z through 2026-10-15T11:40:39Z. No issues found<br>808 history record(s) valid against src/habitatmech/schema/history.yaml |
| just verify-corpus | passed | True | habitatmech:GOLD.de5efc0eb8 | Actual execution 2026-10-15T11:40:39Z through 2026-10-15T11:40:56Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_biliary_review_links.py tests/test_biliary_bivalve_review_repairs.py | passed | True | habitatmech:GOLD.de5efc0eb8 | Actual execution 2026-10-15T11:40:56Z through 2026-10-15T11:41:03Z. ..                                                                       [100%]<br>2 passed in 6.38s |
| just render-check | passed | True | habitatmech:GOLD.de5efc0eb8 | Actual execution 2026-10-15T11:41:03Z through 2026-10-15T11:41:33Z. rendered 3208 habitat pages, 258 redirect stubs, 8 categories, 122 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmp7e571f_3/site<br>pages/ is in step with the corpus<br> uv run python scripts/render_pages.py --check |
| git diff --check 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87 | passed | True | habitatmech:GOLD.de5efc0eb8 | Actual execution 2026-10-15T11:41:33Z through 2026-10-15T11:41:35Z.  |

## Scientific And Domain Assessments

### Exact correction and whole-record preservation

consistency: supported. Targets: habitatmech:GOLD.de5efc0eb8.

The whole-corpus counterfactual and complete current YAML demonstrate bounded hierarchy/synonym changes, preserved source metadata and status, and repeatable generation.

### Retained scientific support

evidence: supported. Targets: habitatmech:GOLD.de5efc0eb8.

The target was rechecked against retained typed ontology and bounded primary evidence. No new characteristic-presence, prevalence or mechanism claim is added.

### Unresolved findings

representation: concern. Targets: habitatmech:GOLD.de5efc0eb8.

Narrow predicate describes a different endpoint from the schema

### Publication correction preserves scientific content

consistency: supported. Targets: habitatmech:GOLD.de5efc0eb8.

Complete target comparison permits only URL-boundary spacing in the new deterministic curation history. All scientific claims and unresolved limitations remain unchanged.

## Findings

### F1: Source context is asserted as a strictly broader habitat

major / resolved / confirmed; issue key: biliary-tract--d4ec2b3f-source-parent.

A biliary subsystem is not the whole digestive system. Exclude only the exact GOLD contribution habitatmech:GOLD.c8e85f3c84 using source-path and expected-parent guards. Preserve independent ontology genera, counts, identities and native status. The linked issue is related context; additional host witnesses expand its original examples.

Disposition: Exact source-path and expected-parent guards suppress only the reviewed GOLD context edge. Independent ontology parents, source attestations/counts/units, identity and status remain.

### F2: Narrow predicate describes a different endpoint from the schema

major / open / confirmed; issue key: biliary-tract--d4ec2b3f-mapping-endpoint-contract.

The mint is retained while narrowMatch compares it to an ontology parent, not the declared source-to-generated-record endpoint. Reconcile producer/schema/consumer contracts under #1398 without collapsing host-specific identities or blindly flipping a predicate. This is not a claim that SKOS forbids self-links.

Disposition: The shared mapping endpoint mismatch is unchanged. Edge-only correction does not reconcile producer/schema/consumer contracts or certify source precision.

## Recommended Actions And Acceptance Checks

### ACT1

The mint is retained while narrowMatch compares it to an ontology parent, not the declared source-to-generated-record endpoint. Reconcile producer/schema/consumer contracts under #1398 without collapsing host-specific identities or blindly flipping a predicate. This is not a claim that SKOS forbids self-links. No repair is performed by this review.

- Regress the exact reported claim and preserve independently valid identifiers, source counts/units, raw provenance, native status and history. Do not change source totals by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001007/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001007", "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001007", "target": "http://purl.obolibrary.org/obo/GO_0022600", "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001007", "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001007; Current identity, definition and typed relations | supports | UBERON:0001007 digestive system; inspected definition: ["Anatomical system that has as its parts the organs devoted to the ingestion, digestion, and assimilation of food and the discharge of residual wastes."] |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001173/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0004119", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0001246", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0001282", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0002294", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0002394", "uri": "http://purl.obolibrary.org/obo/RO_0002473", "label": "composed primarily of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0002423", "uri": "http://purl.obolibrary.org/obo/RO_0002433", "label": "contributes to morphology of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0003703", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173", "target": "http://purl.obolibrary.org/obo/UBERON_0004912", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001173; Current identity, definition and typed relations | supports | UBERON:0001173 biliary tree; inspected definition: ["The path in many species is as follows: Bile canaliculi -&gt; Canals of Hering (intralobar bile duct) -&gt; interlobular bile ducts -&gt; intrahepatic bile ducts -&gt; left and right hepatic ducts merge to form -&gt; common hepatic duct *exits liver* and joins -&gt; cystic duct (from gall bladder) forming -&gt; common bile duct -&gt; joins with pancreatic duct -&gt; forming ampulla of Vater -&gt; enters duodenum [WP]", "A complex network of conduits that begins with the canals of Hering (intralobar bile duct) and progressively merges into a system of interlobular, septal, and major ducts which then coalesce to form the extrahepatic bile ducts, which finally deliver bile to the intestine, and in some species to the gallbladder."] Typed synonyms: [{"name": "biliary tract", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "MA", "id": "0001273", "description": null, "url": "http://www.informatics.jax.org/searches/AMA.cgi?id=MA:0001273"}]}] |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002294/graph; Current identity, definition and typed relations | supports | Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0002294", "target": "http://purl.obolibrary.org/obo/UBERON_0011216", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002294", "target": "http://purl.obolibrary.org/obo/GO_0006699", "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002294", "target": "http://purl.obolibrary.org/obo/GO_0015721", "uri": "http://purl.obolibrary.org/obo/RO_0002215", "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002294", "target": "http://purl.obolibrary.org/obo/UBERON_0001173", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002294", "target": "http://purl.obolibrary.org/obo/UBERON_0002423", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002294; Current identity, definition and typed relations | supports | UBERON:0002294 biliary system; inspected definition: ["Organ system subdivision that consists of the organs and ducts that are involved in the production and transportation of bile. In most species this is the gallbladder and the bile ducts (biliary tree)."] Typed synonyms: [{"name": "biliary apparatus", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "FMA", "id": "79646", "description": null, "url": "http://purl.org/sig/ont/fma/79646"}]}, {"name": "biliary tract", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "FMA", "id": "79646", "description": null, "url": "http://purl.org/sig/ont/fma/79646"}, {"database": "MA", "id": "0001273", "description": null, "url": "http://www.informatics.jax.org/searches/AMA.cgi?id=MA:0001273"}]}] |
| EAFTER | data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml; Entire current YAML | supports | Complete current target: {"identifier": "habitatmech:GOLD.de5efc0eb8", "label": "Biliary tract", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001173"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6398", "source_label": "Biliary tract", "source_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Biliary tract", "mapping_predicate": "skos:narrowMatch"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.c8e85f3c84 for habitatmech:GOLD.de5efc0eb8 (Host-associated &gt; Mammals &gt; Digestive system &gt; Biliary tract). Review https://github.com/CultureBotAI/HabitatMech/issues/2177 : A biliary subsystem is not the whole digestive system. Suppress only the exact GOLD context contribution. Preserve independent parents, identity, source path/node/count/unit, taxa, native status and prior history. No source-scope or mapping-endpoint certification is implied."}]} |
| EPREV | reviews/structured/20261015T112629Z-biliary_tract__d4ec2b3f-remediation/review.yaml; Immediate immutable predecessor | supports | Scientific findings and dispositions remain unchanged. |
| ETEST | tests/test_biliary_bivalve_review_repairs.py; Whole-corpus counterfactual | supports | Restoring only prior rules changes exactly fifteen records. Identity, definitions, source observations/counts/units, taxa, native statuses, valid parents and prior history are preserved; regeneration is repeatable. |
| EI0 | curation/gold_parent_exclusions.tsv; Current maintained rows | supports | [[11, {"identifier": "habitatmech:GOLD.de5efc0eb8", "source_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Biliary tract", "parent_id": "habitatmech:GOLD.c8e85f3c84", "curator": "codex-gpt-5", "date": "2026-10-15", "notes": "Review https://github.com/CultureBotAI/HabitatMech/issues/2177 : A biliary subsystem is not the whole digestive system. Suppress only the exact GOLD context contribution. Preserve independent parents, identity, source path/node/count/unit, taxa, native status and prior history. No source-scope or mapping-endpoint certification is implied."}]] |
| ELINK | tests/test_biliary_review_links.py; Issue URL boundary regression | supports | The regression failed before correction and passed afterward for all 18 new notes. Parsed generated HTML verifies 18 exact hrefs on 15 pages. Whole-record comparison permits only the expected whitespace before colon; all semantic JSONL bytes are identical. |

## Limits And Additional Notes

- Same-agent review is not independent approval. Review does not promote native scientific status.
- Original source-member and source-precision limitations from the predecessor remain; preserved assertions are not independently confirmed specimens.
- Final full QC, archive integrity and real semantic-map/site publication are subsequent gates, not claimed completed in this observation.
- Configured label correspondence retains documented no-adapter skips; this is not global identifier or semantic certification.
- Shared mapping endpoints #1398 and typed ontology extraction #1249 remain open. iModulonDB is not applicable; no gene/expression assertion is made.
- Biliary-tree versus biliary-system source precision remains unresolved under #1379. Removing the whole-digestive-system superclass does not justify an ontology swap.
- Publication repair https://github.com/CultureBotAI/HabitatMech/issues/2179; broader renderer issue #2046 remains open. Native seeding/site regeneration and whole-record comparison preserve all scientific fields and unchanged semantic-map input bytes. All earlier review bundles and session history remain immutable.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T114259Z-biliary_tract__d4ec2b3f-publication
repository: CultureBotAI/HabitatMech
kind: record
title: 'Publication follow-up: Biliary tract (habitatmech:GOLD.de5efc0eb8)'
started_at: '2026-10-15T11:42:02Z'
finished_at: '2026-10-15T11:42:59Z'
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
summary: 'Issue URL punctuation is corrected under #2179. The full current target
  retains every scientific field and every prior scientific finding disposition; only
  the new curation-note URL boundaries differ. No new biological conclusion or resolved
  scientific finding is claimed.'
source:
  git_revision: 6e7f4baa9e2c8a5acc71e1af0b070cd82c84b798
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
  - path: data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
    sha256: 100e3d311062851be06598d3c6d25df5cbfef28ef2bfd9033bad61d05159dc88
    role: target
  - path: data/habitats/host_associated/digestive_system__efdbeca1.yaml
    sha256: 68f12a08d60a0a350f532b270582ae5e3b8c4419b6c95b1da4a9efdeb085d7a6
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
  - path: history/mappings/biliary_tract__d4ec2b3f/2026-10-15T112029Z-codex-gpt-5-243cb1.yaml
    sha256: e459db86bdad7c60b3ac8197545d6d9a3021d6ec72519cc332883594d09616f2
    role: context
  - path: history/mappings/review-link-boundaries/2026-10-15T113917Z-codex-gpt-5-a9297b.yaml
    sha256: 3447b314e8c5b51bf844ad09a69a176a7cc11c363af8ba06ab5e8121e3b94791
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20261004T123731Z-biliary_tract__d4ec2b3f.md
    sha256: 35d394a4ad5cc7ad94934ec3c811961b708a6a09f13334ea15c6e2e3c765bde3
    role: context
  - path: reviews/structured/20261015T110630Z-biliary_tract__d4ec2b3f-record/review.yaml
    sha256: 9f0dac82e2117e0bdc9cf47f8504a4c35fc29b0cc8bcac4d6626a4bfa0b75a8b
    role: context
  - path: reviews/structured/20261015T112629Z-biliary_tract__d4ec2b3f-remediation/review.yaml
    sha256: 8d946d6342e02e4710f066b0eb857fa1095a9b2293f20a91edcc32124e4cd617
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
  - path: tests/test_biliary_bivalve_review_repairs.py
    sha256: 1412766b81259472012db4a0b75b171a12d854357f7c6d2d79289dcbcb1882d0
    role: context
  - path: tests/test_biliary_review_links.py
    sha256: c93aef11ddc15313ad428e63e6123483e9a78ba12149d734a2440dc25de439f8
    role: context
targets:
- target_id: habitatmech:GOLD.de5efc0eb8
  path: data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
  label: Biliary tract
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
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
scope:
  description: Full current target re-read after an issue-URL punctuation-only correction;
    every scientific disposition reassessed.
  selection: One of fifteen repaired records or the unchanged biofilm target receiving
    a report-locator correction in this twenty-record PR cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.de5efc0eb8
  exclusions:
  - target: Global mapping, source contracts and other records
    reason: Only exact hierarchy/synonym witnesses are repaired; SSSOM/KGX readiness
      is not certified.
checks:
- check_id: C1
  name: just validate-strict data/habitats/host_associated/benign_tumor_tissue.yaml
    data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml
    data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml
    data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml
    data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml
    data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml
    data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
    data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml
    data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml
    data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml
    data/habitats/host_associated/bivalves.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/benign_tumor_tissue.yaml
    data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml
    data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml
    data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml
    data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml
    data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml
    data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
    data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml
    data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml
    data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml
    data/habitats/host_associated/bivalves.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  summary: "Actual execution 2026-10-15T11:40:21Z through 2026-10-15T11:40:29Z. uv\
    \ run python scripts/validate_strict.py data/habitats/host_associated/benign_tumor_tissue.yaml\
    \ data/habitats/host_associated/bhk.yaml data/habitats/host_associated/bhk_21_cell.yaml\
    \ data/habitats/host_associated/bile.yaml data/habitats/host_associated/bile__22fc0a7b.yaml\
    \ data/habitats/host_associated/bile__57dd7796.yaml data/habitats/host_associated/bile__612af0df.yaml\
    \ data/habitats/host_associated/bile__deca6de5.yaml data/habitats/host_associated/bile_duct.yaml\
    \ data/habitats/host_associated/biliary_tract.yaml data/habitats/host_associated/biliary_tract__076692f7.yaml\
    \ data/habitats/host_associated/biliary_tract__7bf9e820.yaml data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml\
    \ data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml data/habitats/host_associated/biliary_tract__e6019127.yaml\
    \ data/habitats/host_associated/biocrust.yaml data/habitats/host_associated/biofilm.yaml\
    \ data/habitats/host_associated/biofilm__465616a5.yaml data/habitats/host_associated/birds.yaml\
    \ data/habitats/host_associated/bivalves.yaml\nValidating 20 files with 15 workers;\
    \ schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      20\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
- check_id: C2
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  summary: 'Actual execution 2026-10-15T11:40:29Z through 2026-10-15T11:40:39Z. No
    issues found

    808 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
- check_id: C3
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  summary: "Actual execution 2026-10-15T11:40:39Z through 2026-10-15T11:40:56Z. expected\
    \ 3208 records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing:\
    \ 0\n\ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
- check_id: C4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_biliary_review_links.py tests/test_biliary_bivalve_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_biliary_review_links.py tests/test_biliary_bivalve_review_repairs.py
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  summary: 'Actual execution 2026-10-15T11:40:56Z through 2026-10-15T11:41:03Z. ..                                                                       [100%]

    2 passed in 6.38s'
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
- check_id: C5
  name: just render-check
  status: passed
  required: true
  command: just render-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  summary: "Actual execution 2026-10-15T11:41:03Z through 2026-10-15T11:41:33Z. rendered\
    \ 3208 habitat pages, 258 redirect stubs, 8 categories, 122 term requests -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmp7e571f_3/site\n\
    pages/ is in step with the corpus\n uv run python scripts/render_pages.py --check"
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
- check_id: C6
  name: git diff --check 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87
  status: passed
  required: true
  command: git diff --check 405ef4c51cf7aa4d0d2203aaf392ed5d773a7e87
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  summary: 'Actual execution 2026-10-15T11:41:33Z through 2026-10-15T11:41:35Z. '
  scope_note: Strict check covers twenty targets; remaining documented native gates
    cover the corpus; pytest is the focused preservation/publication regression.
evidence:
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001007/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:52Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001007",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001007",
    "target": "http://purl.obolibrary.org/obo/GO_0022600", "uri": "http://purl.obolibrary.org/obo/RO_0002215",
    "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001007",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492",
    "label": "existence ends during"}]'
  snapshot_sha256: 6edb81365904fcd686c6cc14a898a5257038c30b7b71122d5934136a0b138d7b
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001007
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:51Z'
  support: supports
  summary: 'UBERON:0001007 digestive system; inspected definition: ["Anatomical system
    that has as its parts the organs devoted to the ingestion, digestion, and assimilation
    of food and the discharge of residual wastes."]'
  snapshot_sha256: aea4a663a4ca364533042f3049c36d82efbe62f67fc40cb202d7a839dc5d2c09
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001173/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:54Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004119", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001246", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001282", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002294", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002394", "uri": "http://purl.obolibrary.org/obo/RO_0002473",
    "label": "composed primarily of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002423", "uri": "http://purl.obolibrary.org/obo/RO_0002433",
    "label": "contributes to morphology of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0003703", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001173",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004912", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}]'
  snapshot_sha256: c3f1f945a7973cdf4b8971cb0a7c773dfdfe5580aa6ca63ef0eaca5d34423cce
- evidence_id: EX4
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001173
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:52:53Z'
  support: supports
  summary: 'UBERON:0001173 biliary tree; inspected definition: ["The path in many
    species is as follows: Bile canaliculi -> Canals of Hering (intralobar bile duct)
    -> interlobular bile ducts -> intrahepatic bile ducts -> left and right hepatic
    ducts merge to form -> common hepatic duct *exits liver* and joins -> cystic duct
    (from gall bladder) forming -> common bile duct -> joins with pancreatic duct
    -> forming ampulla of Vater -> enters duodenum [WP]", "A complex network of conduits
    that begins with the canals of Hering (intralobar bile duct) and progressively
    merges into a system of interlobular, septal, and major ducts which then coalesce
    to form the extrahepatic bile ducts, which finally deliver bile to the intestine,
    and in some species to the gallbladder."] Typed synonyms: [{"name": "biliary tract",
    "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "MA", "id":
    "0001273", "description": null, "url": "http://www.informatics.jax.org/searches/AMA.cgi?id=MA:0001273"}]}]'
  snapshot_sha256: 37320ff91102de4a8c23a02276a955e085041a65dba3cb570e5d8a8c22dcb9f9
- evidence_id: EX5
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002294/graph
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:56:42Z'
  support: supports
  summary: 'Outgoing typed relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0002294",
    "target": "http://purl.obolibrary.org/obo/UBERON_0011216", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002294",
    "target": "http://purl.obolibrary.org/obo/GO_0006699", "uri": "http://purl.obolibrary.org/obo/RO_0002215",
    "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002294",
    "target": "http://purl.obolibrary.org/obo/GO_0015721", "uri": "http://purl.obolibrary.org/obo/RO_0002215",
    "label": "capable of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002294",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001173", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002294",
    "target": "http://purl.obolibrary.org/obo/UBERON_0002423", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 152e0bff2d29993ac46edf3e6ef573d2740c18b86d8ab15a2bf31e9484deabdb
- evidence_id: EX6
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002294
  locator: Current identity, definition and typed relations
  accessed_at: '2026-10-15T10:56:42Z'
  support: supports
  summary: 'UBERON:0002294 biliary system; inspected definition: ["Organ system subdivision
    that consists of the organs and ducts that are involved in the production and
    transportation of bile. In most species this is the gallbladder and the bile ducts
    (biliary tree)."] Typed synonyms: [{"name": "biliary apparatus", "scope": "hasExactSynonym",
    "type": null, "xrefs": [{"database": "FMA", "id": "79646", "description": null,
    "url": "http://purl.org/sig/ont/fma/79646"}]}, {"name": "biliary tract", "scope":
    "hasRelatedSynonym", "type": null, "xrefs": [{"database": "FMA", "id": "79646",
    "description": null, "url": "http://purl.org/sig/ont/fma/79646"}, {"database":
    "MA", "id": "0001273", "description": null, "url": "http://www.informatics.jax.org/searches/AMA.cgi?id=MA:0001273"}]}]'
  snapshot_sha256: 8d48f630f35726265be5e9c4636f0a773929e09f8e3606b5eab5ff0307ad041b
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml
  locator: Entire current YAML
  accessed_at: '2026-10-15T11:42:59Z'
  support: supports
  summary: 'Complete current target: {"identifier": "habitatmech:GOLD.de5efc0eb8",
    "label": "Biliary tract", "habitat_category": "HOST_ASSOCIATED", "grounding_status":
    "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0001173"], "source_attestations":
    [{"source": "GOLD", "source_id": "gold.ecosystem:6398", "source_label": "Biliary
    tract", "source_path": "Host-associated > Mammals > Digestive system > Biliary
    tract", "mapping_predicate": "skos:narrowMatch"}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."},
    {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.c8e85f3c84
    for habitatmech:GOLD.de5efc0eb8 (Host-associated > Mammals > Digestive system
    > Biliary tract). Review https://github.com/CultureBotAI/HabitatMech/issues/2177
    : A biliary subsystem is not the whole digestive system. Suppress only the exact
    GOLD context contribution. Preserve independent parents, identity, source path/node/count/unit,
    taxa, native status and prior history. No source-scope or mapping-endpoint certification
    is implied."}]}'
  snapshot_sha256: 100e3d311062851be06598d3c6d25df5cbfef28ef2bfd9033bad61d05159dc88
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T112629Z-biliary_tract__d4ec2b3f-remediation/review.yaml
  locator: Immediate immutable predecessor
  accessed_at: '2026-10-15T11:42:59Z'
  support: supports
  summary: Scientific findings and dispositions remain unchanged.
  snapshot_sha256: 8d946d6342e02e4710f066b0eb857fa1095a9b2293f20a91edcc32124e4cd617
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_biliary_bivalve_review_repairs.py
  locator: Whole-corpus counterfactual
  accessed_at: '2026-10-15T11:26:29Z'
  support: supports
  summary: Restoring only prior rules changes exactly fifteen records. Identity, definitions,
    source observations/counts/units, taxa, native statuses, valid parents and prior
    history are preserved; regeneration is repeatable.
  snapshot_sha256: 1412766b81259472012db4a0b75b171a12d854357f7c6d2d79289dcbcb1882d0
- evidence_id: EI0
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Current maintained rows
  accessed_at: '2026-10-15T11:42:59Z'
  support: supports
  summary: '[[11, {"identifier": "habitatmech:GOLD.de5efc0eb8", "source_path": "Host-associated
    > Mammals > Digestive system > Biliary tract", "parent_id": "habitatmech:GOLD.c8e85f3c84",
    "curator": "codex-gpt-5", "date": "2026-10-15", "notes": "Review https://github.com/CultureBotAI/HabitatMech/issues/2177
    : A biliary subsystem is not the whole digestive system. Suppress only the exact
    GOLD context contribution. Preserve independent parents, identity, source path/node/count/unit,
    taxa, native status and prior history. No source-scope or mapping-endpoint certification
    is implied."}]]'
  snapshot_sha256: a92f9003cc5f57c397ab5118474318f216077a8e9f90564d21dfa8089477a2eb
- evidence_id: ELINK
  kind: record_content
  reference: tests/test_biliary_review_links.py
  locator: Issue URL boundary regression
  accessed_at: '2026-10-15T11:42:59Z'
  support: supports
  summary: The regression failed before correction and passed afterward for all 18
    new notes. Parsed generated HTML verifies 18 exact hrefs on 15 pages. Whole-record
    comparison permits only the expected whitespace before colon; all semantic JSONL
    bytes are identical.
  snapshot_sha256: c93aef11ddc15313ad428e63e6123483e9a78ba12149d734a2440dc25de439f8
assessments:
- assessment_id: A1
  area: consistency
  topic: Exact correction and whole-record preservation
  outcome: supported
  summary: The whole-corpus counterfactual and complete current YAML demonstrate bounded
    hierarchy/synonym changes, preserved source metadata and status, and repeatable
    generation.
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI0
- assessment_id: A2
  area: evidence
  topic: Retained scientific support
  outcome: supported
  summary: The target was rechecked against retained typed ontology and bounded primary
    evidence. No new characteristic-presence, prevalence or mechanism claim is added.
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  evidence_ids:
  - EAFTER
  - EPREV
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
- assessment_id: A3
  area: representation
  topic: Unresolved findings
  outcome: concern
  summary: Narrow predicate describes a different endpoint from the schema
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  evidence_ids:
  - EAFTER
  - EPREV
- assessment_id: A4
  area: consistency
  topic: Publication correction preserves scientific content
  outcome: supported
  summary: Complete target comparison permits only URL-boundary spacing in the new
    deterministic curation history. All scientific claims and unresolved limitations
    remain unchanged.
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  evidence_ids:
  - EAFTER
  - EPREV
  - ELINK
findings:
- finding_id: F1
  issue_key: biliary-tract--d4ec2b3f-source-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is asserted as a strictly broader habitat
  description: A biliary subsystem is not the whole digestive system. Exclude only
    the exact GOLD contribution habitatmech:GOLD.c8e85f3c84 using source-path and
    expected-parent guards. Preserve independent ontology genera, counts, identities
    and native status. The linked issue is related context; additional host witnesses
    expand its original examples.
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  field_paths:
  - parent_habitats
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI0
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1379
  - https://github.com/CultureBotAI/HabitatMech/issues/2177
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T112629Z-biliary_tract__d4ec2b3f-remediation
    finding_id: F1
  disposition_reason: Exact source-path and expected-parent guards suppress only the
    reviewed GOLD context edge. Independent ontology parents, source attestations/counts/units,
    identity and status remain.
- finding_id: F2
  issue_key: biliary-tract--d4ec2b3f-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow predicate describes a different endpoint from the schema
  description: 'The mint is retained while narrowMatch compares it to an ontology
    parent, not the declared source-to-generated-record endpoint. Reconcile producer/schema/consumer
    contracts under #1398 without collapsing host-specific identities or blindly flipping
    a predicate. This is not a claim that SKOS forbids self-links.'
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI0
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T112629Z-biliary_tract__d4ec2b3f-remediation
    finding_id: F2
  disposition_reason: The shared mapping endpoint mismatch is unchanged. Edge-only
    correction does not reconcile producer/schema/consumer contracts or certify source
    precision.
actions:
- action_id: ACT1
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.de5efc0eb8
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never patch generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never patch generated habitat YAML
  description: 'The mint is retained while narrowMatch compares it to an ontology
    parent, not the declared source-to-generated-record endpoint. Reconcile producer/schema/consumer
    contracts under #1398 without collapsing host-specific identities or blindly flipping
    a predicate. This is not a claim that SKOS forbids self-links. No repair is performed
    by this review.'
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
- Same-agent review is not independent approval. Review does not promote native scientific
  status.
- Original source-member and source-precision limitations from the predecessor remain;
  preserved assertions are not independently confirmed specimens.
- Final full QC, archive integrity and real semantic-map/site publication are subsequent
  gates, not claimed completed in this observation.
- Configured label correspondence retains documented no-adapter skips; this is not
  global identifier or semantic certification.
- 'Shared mapping endpoints #1398 and typed ontology extraction #1249 remain open.
  iModulonDB is not applicable; no gene/expression assertion is made.'
- 'Biliary-tree versus biliary-system source precision remains unresolved under #1379.
  Removing the whole-digestive-system superclass does not justify an ontology swap.'
notes:
- 'Publication repair https://github.com/CultureBotAI/HabitatMech/issues/2179; broader
  renderer issue #2046 remains open. Native seeding/site regeneration and whole-record
  comparison preserve all scientific fields and unchanged semantic-map input bytes.
  All earlier review bundles and session history remain immutable.'
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T110630Z-biliary_tract__d4ec2b3f-record
  relationship: Exact predecessor; every original finding identity and lineage retained.
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T112629Z-biliary_tract__d4ec2b3f-remediation
  relationship: Immediate predecessor; all finding identities and dispositions preserved
    after publication-only correction.
```
