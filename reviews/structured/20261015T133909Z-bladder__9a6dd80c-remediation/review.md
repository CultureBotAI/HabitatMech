# Remediation review: Bladder (habitatmech:GOLD.2c26547de4)

- Review: 20261015T133909Z-bladder__9a6dd80c-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T13:12:34Z
- Finished UTC: 2026-10-15T13:39:09Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All 3 scoped predecessor findings are resolved. The human source mint and REVIEWED status remain; false organism/organ parents and unsupported narrowMatch are removed, and urinary bladder is retained only as contextual xref. Grounding changes from NARROW to UNGROUNDED without adding a lesion definition or changing zero-count omission.

## Scope And Provenance

Full current target re-read and disposition of every exact predecessor finding.

Selection: One of two repaired bladder records in the seven-record publication cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 85c62cf2147431e261e8a7c0147040d1355e75a8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.2c26547de4 | data/habitats/host_associated/bladder__9a6dd80c.yaml | generated | Bladder |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/bladder__9a6dd80c.yaml | passed | True | habitatmech:GOLD.2c26547de4 | Executed 2026-10-15T13:05:19Z through 2026-10-15T13:05:24Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bladder__9a6dd80c.yaml |
| just validate-strict data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml data/habitats/host_associated/blast_cell.yaml | passed | True | habitatmech:GOLD.2c26547de4 | Executed 2026-10-15T13:05:28Z through 2026-10-15T13:05:34Z. uv run python scripts/validate_strict.py data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml data/habitats/host_associated/blast_cell.yaml<br>Validating 7 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      7<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.2c26547de4 | Executed 2026-10-15T13:05:34Z through 2026-10-15T13:05:43Z. No issues found<br>813 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.2c26547de4 | Executed 2026-10-15T13:05:43Z through 2026-10-15T13:05:44Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.2c26547de4 | Executed 2026-10-15T13:05:44Z through 2026-10-15T13:06:01Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.2c26547de4 | Executed 2026-10-15T13:06:01Z through 2026-10-15T13:06:05Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.2c26547de4 | Executed 2026-10-15T13:06:05Z through 2026-10-15T13:06:24Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.2c26547de4 | Executed 2026-10-15T13:06:24Z through 2026-10-15T13:07:06Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python -m pytest -q tests/test_bladder_review_repairs.py | passed | True | habitatmech:GOLD.2c26547de4 | Executed 2026-10-15T13:07:06Z through 2026-10-15T13:07:11Z. ..                                                                       [100%]<br>2 passed in 4.84s |
| git diff --check 68ceabb7039a537f65be44ac6aaa913116a154f5 | passed | True | habitatmech:GOLD.2c26547de4 | Executed 2026-10-15T13:07:11Z through 2026-10-15T13:07:12Z.  |
| Exact-revision full QC and archive contract | passed | True | habitatmech:GOLD.2c26547de4 | Authoritative quality gate succeeded at captured revision 85c62cf2147431e261e8a7c0147040d1355e75a8; verified 2026-10-15T13:38:30Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38740765213 |

## Scientific And Domain Assessments

### Scoped correction and preservation

consistency: supported. Targets: habitatmech:GOLD.2c26547de4.

All 3 scoped predecessor findings are resolved. The human source mint and REVIEWED status remain; false organism/organ parents and unsupported narrowMatch are removed, and urinary bladder is retained only as contextual xref. Grounding changes from NARROW to UNGROUNDED without adding a lesion definition or changing zero-count omission.

### Retained scientific support

evidence: supported. Targets: habitatmech:GOLD.2c26547de4.

Current record was re-read against retained typed ontology and bounded primary-source evidence. No new prevalence, viability, characteristic-presence or causal claim is added.

## Findings

### F1: Human bladder-polyp context inherits a cnidarian parent

major / resolved / confirmed; issue key: bladder--9a6dd80c-cnidarian-context-parent.

Suppress only the exact GOLD parent contribution BTO:0006350 using gold_parent_exclusions.tsv. The independent parent identity defect remains #2171; do not silently relabel that other record or substitute a disease term.

Disposition: An exact source-path/expected-parent exclusion removes only the reviewed GOLD context contribution. Independent valid ancestry, source identifiers, counts/units and taxa are preserved. The separate parent record is unchanged.

### F2: A bladder polyp is not a kind of whole urinary bladder

major / resolved / confirmed; issue key: bladder--9a6dd80c-organ-as-genus.

Replace the exact source decision GROUND_AS_PARENT with supported retained-mint curation that keeps UBERON:0001255 only as contextual xref. Preserve the source path and zero-count omission; no unsupported lesion definition or organ identity should be invented.

Disposition: The ITEM decision now retains the source mint UNGROUNDED with UBERON:0001255 as xref, not superclass or identity. Source observations and REVIEWED status remain; no exact lesion grounding is invented.

### F3: Narrow mapping compares an undeclared ontology-parent endpoint

major / resolved / confirmed; issue key: bladder--9a6dd80c-mapping-endpoint-contract.

The executed GROUND_AS_PARENT route retains the source mint but emits narrowMatch relative to UBERON:0001255, unlike the schema source-to-record endpoint. Correct this target through its unsupported parent decision; shared producer/schema/consumer reconciliation remains #1398. This is not a claim that SKOS forbids self-links.

Disposition: This exact retained-mint witness no longer emits narrowMatch after removing the unsupported organ-parent decision. The global producer/schema/consumer contract remains unresolved under #1398; this disposition covers only the target finding.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284/graph; BTO_0000284-graph.json | context_only | Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0000284", "target": "http://purl.obolibrary.org/obo/BTO_0000000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000284?lang=en; BTO_0000284.json | context_only | Inspected current identifier, label, active status and full definition for the scope assessment: {"obo_id": "BTO:0000284", "label": "organism form", "is_obsolete": false} |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0006350/graph; BTO_0006350-graph.json | context_only | Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/BTO_0006350", "target": "http://purl.obolibrary.org/obo/BTO_0000284", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0006350?lang=en; BTO_0006350.json | context_only | Inspected current identifier, label, active status and full definition for the scope assessment: {"obo_id": "BTO:0006350", "label": "polyp", "is_obsolete": false} |
| EX14 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001255/graph; UBERON_0001255-graph.json | context_only | Inspected outgoing typed ontology relations: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0002075", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0004120", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0018707", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0000164", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0001556", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001255", "target": "http://purl.obolibrary.org/obo/UBERON_0002323", "uri": "http://purl.obolibrary.org/obo/RO_0001025", "label": "located in"}] |
| EX15 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001255?lang=en; UBERON_0001255.json | context_only | Inspected current identifier, label, active status and full definition for the scope assessment: {"obo_id": "UBERON:0001255", "label": "urinary bladder", "is_obsolete": false} |
| EAFTER | data/habitats/host_associated/bladder__9a6dd80c.yaml; Entire generated post-fix YAML | supports | {"identifier": "habitatmech:GOLD.2c26547de4", "label": "Bladder", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "xrefs": ["UBERON:0001255"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6653", "source_label": "Bladder", "source_path": "Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Polyps &gt; Bladder"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. UBERON:0001255 'urinary bladder' kept as an xref. Review https://github.com/CultureBotAI/HabitatMech/issues/2181 : Retain this human bladder-polyp source context as minted. A polyp is not a kind of whole urinary bladder; preserve UBERON:0001255 only as contextual xref, not identity or superclass. The human path cannot inherit BTO:0006350 cnidarian polyp. No exact lesion ontology identity or unsupported definition is asserted; original decision evidence remains in immutable review/history. Shared mapping contract #1398 and parent identity #2171 remain separate. (source concept habitatmech:GOLD.2c26547de4)"}, {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution BTO:0006350 for habitatmech:GOLD.2c26547de4 (Host-associated &gt; Mammals: Human &gt; Benign tumor &gt; Polyps &gt; Bladder). Review https://github.com/CultureBotAI/HabitatMech/issues/2181 : Human bladder-polyp context is not a cnidarian body form; parent identity remains tracked separately in #2171. Exclude only this exact source-path/expected-parent contribution. Preserve independent parents and source observations."}]} |
| EPREV | reviews/structured/20261015T125452Z-bladder__9a6dd80c-record/review.yaml; Exact predecessor with all findings | supports | Original scientific observation remains immutable. |
| ETEST | tests/test_bladder_review_repairs.py; Whole-corpus counterfactual and actual Jinja urlize regression | supports | Exactly the two intended records change across all 3,208 generated identities. Source observations are preserved. The polyp grounding and generated seed summary change explicitly; old evidence remains in the predecessor and append-only history. All three new issue hrefs exclude trailing colons. |
| EI0 | curation/decisions.tsv; Exact keyed TSV rows 349 | supports | [[349, "habitatmech:GOLD.2c26547de4\tCONFIRM_UNGROUNDED\tUBERON:0001255\turinary bladder\t\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2181 : Retain this human bladder-polyp source context as minted. A polyp is not a kind of whole urinary bladder; preserve UBERON:0001255 only as contextual xref, not identity or superclass. The human path cannot inherit BTO:0006350 cnidarian polyp. No exact lesion ontology identity or unsupported definition is asserted; original decision evidence remains in immutable review/history. Shared mapping contract #1398 and parent identity #2171 remain separate.\tITEM\t\txref"]] |
| EI1 | curation/gold_parent_exclusions.tsv; Exact keyed TSV rows 2 | supports | [[2, "habitatmech:GOLD.2c26547de4\tHost-associated &gt; Mammals: Human &gt; Benign tumor &gt; Polyps &gt; Bladder\tBTO:0006350\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2181 : Human bladder-polyp context is not a cnidarian body form; parent identity remains tracked separately in #2171. Exclude only this exact source-path/expected-parent contribution. Preserve independent parents and source observations."]] |

## Limits And Additional Notes

- Same-agent review, not independent approval. Original specimen/pair-evidence limitations remain; only scoped hierarchy and mapping witnesses are repaired.
- The polyp retains its source-context identity without an authored exact lesion definition. This is not an ontology-completeness claim or correction of the separate parent-polyp record.
- Global source-to-record mapping contract #1398 and parent identity #2171 remain open; export compatibility is not certified.
- Configured label correspondence includes 2,061 no-adapter skips. iModulonDB is not applicable; no gene or expression claim is present.
- Final-head archive validation of this newly added observation is a subsequent release gate; exact captured-input full QC and real map/site publication have already passed.
- Issue #2184 additionally corrects three new rendered issue links; actual Jinja urlize regression is included. Immutable original reviews and existing committed history are untouched.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T133909Z-bladder__9a6dd80c-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: Bladder (habitatmech:GOLD.2c26547de4)'
started_at: '2026-10-15T13:12:34Z'
finished_at: '2026-10-15T13:39:09Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent inspected the record and evidence; not independent
    human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All 3 scoped predecessor findings are resolved. The human source mint and
  REVIEWED status remain; false organism/organ parents and unsupported narrowMatch
  are removed, and urinary bladder is retained only as contextual xref. Grounding
  changes from NARROW to UNGROUNDED without adding a lesion definition or changing
  zero-count omission.
source:
  git_revision: 85c62cf2147431e261e8a7c0147040d1355e75a8
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
    sha256: 6d5cbfd0f5ad911fbb074ee8ec253625d1fa13d94117759b1f25a1cd2e6576bc
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 1e1c576daaee3c5055437ef42ba46363f5776210eef2e4182fe6fd3c87a7fe4d
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
    sha256: 40b66aa000b2d0490e82421b40b96a0f18915f190898d8134a0e79358abc5374
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
  - path: history/mappings/bladder__9a6dd80c/2026-10-15T130108Z-codex-gpt-5-99b0d8.yaml
    sha256: 77af8c0c8dc4a7de167750bad41c1b12c57b9b8568fd9291486d3bac743ab123
    role: context
  - path: history/mappings/bladder__9a6dd80c/2026-10-15T130109Z-codex-gpt-5-7fac17.yaml
    sha256: 6edb81e03e58c7de7c4aa0e2f7386d1c019f73194f2685afdb6c400c562ca5a8
    role: context
  - path: history/mappings/bladder__9a6dd80c/2026-10-15T130350Z-codex-gpt-5-1af42e.yaml
    sha256: 428898ad4a96480319e3ed837dc042d66c2adc0246d0fdefba4fca730df9c9cb
    role: context
  - path: history/mappings/bladder_review_links/2026-10-15T130351Z-codex-gpt-5-e878c5.yaml
    sha256: cab4c5a304942389614b0880303c1efa3bf640ebf4f41cfcddbbf514f3a4fd93
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261015T125452Z-bladder__9a6dd80c-record/review.yaml
    sha256: 726cea6544759a743fc08691c5aaacdde6cb289b400766e87dfa06a5374fbc2e
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
  - path: tests/test_bladder_review_repairs.py
    sha256: a5dc8ac0450f286fa38bb087a8a44513794db586fa18bfeb7baeacb1afeed4be
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
  description: Full current target re-read and disposition of every exact predecessor
    finding.
  selection: One of two repaired bladder records in the seven-record publication cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.2c26547de4
  exclusions:
  - target: Shared mapping contract and parent-polyp identity
    reason: '#1398 and #2171 are not resolved by this target repair; SSSOM/KGX conformance
      is not certified.'
checks:
- check_id: C0
  name: just validate data/habitats/host_associated/bladder__9a6dd80c.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/bladder__9a6dd80c.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Executed 2026-10-15T13:05:19Z through 2026-10-15T13:05:24Z. No issues\
    \ found\n uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class\
    \ HabitatRecord data/habitats/host_associated/bladder__9a6dd80c.yaml"
  scope_note: Ordinary schema for both changed records, strict for seven records,
    focused pytest, other native gates full-corpus.
- check_id: C2
  name: just validate-strict data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml
    data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml
    data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml
    data/habitats/host_associated/blast_cell.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml
    data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml
    data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml
    data/habitats/host_associated/blast_cell.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Executed 2026-10-15T13:05:28Z through 2026-10-15T13:05:34Z. uv run python\
    \ scripts/validate_strict.py data/habitats/host_associated/bl_3_cell.yaml data/habitats/host_associated/bladder.yaml\
    \ data/habitats/host_associated/bladder__9a6dd80c.yaml data/habitats/host_associated/bladder_stone.yaml\
    \ data/habitats/host_associated/blade.yaml data/habitats/host_associated/blade__f83a64ca.yaml\
    \ data/habitats/host_associated/blast_cell.yaml\nValidating 7 files with 15 workers;\
    \ schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      7\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for both changed records, strict for seven records,
    focused pytest, other native gates full-corpus.
- check_id: C3
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: 'Executed 2026-10-15T13:05:34Z through 2026-10-15T13:05:43Z. No issues
    found

    813 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for both changed records, strict for seven records,
    focused pytest, other native gates full-corpus.
- check_id: C4
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Executed 2026-10-15T13:05:43Z through 2026-10-15T13:05:44Z. provenance\
    \ current: 14 committed inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for both changed records, strict for seven records,
    focused pytest, other native gates full-corpus.
- check_id: C5
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Executed 2026-10-15T13:05:44Z through 2026-10-15T13:06:01Z. expected 3208\
    \ records, found 3208 on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\
    \ncorpus reproduces exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for both changed records, strict for seven records,
    focused pytest, other native gates full-corpus.
- check_id: C6
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Executed 2026-10-15T13:06:01Z through 2026-10-15T13:06:05Z. validated\
    \ 32 causal-graph curation file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for both changed records, strict for seven records,
    focused pytest, other native gates full-corpus.
- check_id: C7
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Executed 2026-10-15T13:06:05Z through 2026-10-15T13:06:24Z. term-request\
    \ table is current (110 terms)\n uv run python scripts/build_term_requests.py\
    \ --check"
  scope_note: Ordinary schema for both changed records, strict for seven records,
    focused pytest, other native gates full-corpus.
- check_id: C8
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: "Executed 2026-10-15T13:06:24Z through 2026-10-15T13:07:06Z. id↔label correspondence\
    \ summary:\n          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n        \
    \  OK_EXCEPTION: 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n\
    \ uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for both changed records, strict for seven records,
    focused pytest, other native gates full-corpus.
- check_id: C9
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_bladder_review_repairs.py
  status: passed
  required: true
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/.venv/bin/python
    -m pytest -q tests/test_bladder_review_repairs.py
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: 'Executed 2026-10-15T13:07:06Z through 2026-10-15T13:07:11Z. ..                                                                       [100%]

    2 passed in 4.84s'
  scope_note: Ordinary schema for both changed records, strict for seven records,
    focused pytest, other native gates full-corpus.
- check_id: C10
  name: git diff --check 68ceabb7039a537f65be44ac6aaa913116a154f5
  status: passed
  required: true
  command: git diff --check 68ceabb7039a537f65be44ac6aaa913116a154f5
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: 'Executed 2026-10-15T13:07:11Z through 2026-10-15T13:07:12Z. '
  scope_note: Ordinary schema for both changed records, strict for seven records,
    focused pytest, other native gates full-corpus.
- check_id: CCI
  name: Exact-revision full QC and archive contract
  status: passed
  required: true
  command: gh run view 38740765213 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.2c26547de4
  summary: Authoritative quality gate succeeded at captured revision 85c62cf2147431e261e8a7c0147040d1355e75a8;
    verified 2026-10-15T13:38:30Z. https://github.com/CultureBotAI/HabitatMech/actions/runs/38740765213
  scope_note: Remote full native QC at the exact input revision; this new immutable
    observation will also require final-head archive validation.
evidence:
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
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/bladder__9a6dd80c.yaml
  locator: Entire generated post-fix YAML
  accessed_at: '2026-10-15T13:39:09Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.2c26547de4", "label": "Bladder", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "xrefs": ["UBERON:0001255"], "source_attestations": [{"source": "GOLD", "source_id":
    "gold.ecosystem:6653", "source_label": "Bladder", "source_path": "Host-associated
    > Mammals: Human > Benign tumor > Polyps > Bladder"}], "curation_history": [{"timestamp":
    "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES",
    "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."},
    {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "CONFIRM_UNGROUNDED",
    "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. UBERON:0001255
    ''urinary bladder'' kept as an xref. Review https://github.com/CultureBotAI/HabitatMech/issues/2181
    : Retain this human bladder-polyp source context as minted. A polyp is not a kind
    of whole urinary bladder; preserve UBERON:0001255 only as contextual xref, not
    identity or superclass. The human path cannot inherit BTO:0006350 cnidarian polyp.
    No exact lesion ontology identity or unsupported definition is asserted; original
    decision evidence remains in immutable review/history. Shared mapping contract
    #1398 and parent identity #2171 remain separate. (source concept habitatmech:GOLD.2c26547de4)"},
    {"timestamp": "2026-10-15T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution BTO:0006350 for habitatmech:GOLD.2c26547de4
    (Host-associated > Mammals: Human > Benign tumor > Polyps > Bladder). Review https://github.com/CultureBotAI/HabitatMech/issues/2181
    : Human bladder-polyp context is not a cnidarian body form; parent identity remains
    tracked separately in #2171. Exclude only this exact source-path/expected-parent
    contribution. Preserve independent parents and source observations."}]}'
  snapshot_sha256: 40b66aa000b2d0490e82421b40b96a0f18915f190898d8134a0e79358abc5374
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261015T125452Z-bladder__9a6dd80c-record/review.yaml
  locator: Exact predecessor with all findings
  accessed_at: '2026-10-15T13:39:09Z'
  support: supports
  summary: Original scientific observation remains immutable.
  snapshot_sha256: 726cea6544759a743fc08691c5aaacdde6cb289b400766e87dfa06a5374fbc2e
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_bladder_review_repairs.py
  locator: Whole-corpus counterfactual and actual Jinja urlize regression
  accessed_at: '2026-10-15T13:39:09Z'
  support: supports
  summary: Exactly the two intended records change across all 3,208 generated identities.
    Source observations are preserved. The polyp grounding and generated seed summary
    change explicitly; old evidence remains in the predecessor and append-only history.
    All three new issue hrefs exclude trailing colons.
  snapshot_sha256: a5dc8ac0450f286fa38bb087a8a44513794db586fa18bfeb7baeacb1afeed4be
- evidence_id: EI0
  kind: record_content
  reference: curation/decisions.tsv
  locator: Exact keyed TSV rows 349
  accessed_at: '2026-10-15T13:39:09Z'
  support: supports
  summary: '[[349, "habitatmech:GOLD.2c26547de4\tCONFIRM_UNGROUNDED\tUBERON:0001255\turinary
    bladder\t\tcodex-gpt-5\t2026-10-15\tReview https://github.com/CultureBotAI/HabitatMech/issues/2181
    : Retain this human bladder-polyp source context as minted. A polyp is not a kind
    of whole urinary bladder; preserve UBERON:0001255 only as contextual xref, not
    identity or superclass. The human path cannot inherit BTO:0006350 cnidarian polyp.
    No exact lesion ontology identity or unsupported definition is asserted; original
    decision evidence remains in immutable review/history. Shared mapping contract
    #1398 and parent identity #2171 remain separate.\tITEM\t\txref"]]'
  snapshot_sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
- evidence_id: EI1
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact keyed TSV rows 2
  accessed_at: '2026-10-15T13:39:09Z'
  support: supports
  summary: '[[2, "habitatmech:GOLD.2c26547de4\tHost-associated > Mammals: Human >
    Benign tumor > Polyps > Bladder\tBTO:0006350\tcodex-gpt-5\t2026-10-15\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2181 : Human bladder-polyp
    context is not a cnidarian body form; parent identity remains tracked separately
    in #2171. Exclude only this exact source-path/expected-parent contribution. Preserve
    independent parents and source observations."]]'
  snapshot_sha256: 1e1c576daaee3c5055437ef42ba46363f5776210eef2e4182fe6fd3c87a7fe4d
assessments:
- assessment_id: A1
  area: consistency
  topic: Scoped correction and preservation
  outcome: supported
  summary: All 3 scoped predecessor findings are resolved. The human source mint and
    REVIEWED status remain; false organism/organ parents and unsupported narrowMatch
    are removed, and urinary bladder is retained only as contextual xref. Grounding
    changes from NARROW to UNGROUNDED without adding a lesion definition or changing
    zero-count omission.
  target_ids:
  - habitatmech:GOLD.2c26547de4
  evidence_ids:
  - EAFTER
  - EPREV
  - ETEST
  - EI0
  - EI1
- assessment_id: A2
  area: evidence
  topic: Retained scientific support
  outcome: supported
  summary: Current record was re-read against retained typed ontology and bounded
    primary-source evidence. No new prevalence, viability, characteristic-presence
    or causal claim is added.
  target_ids:
  - habitatmech:GOLD.2c26547de4
  evidence_ids:
  - EAFTER
  - EPREV
  - EX10
  - EX11
  - EX12
  - EX13
  - EX14
  - EX15
findings:
- finding_id: F1
  issue_key: bladder--9a6dd80c-cnidarian-context-parent
  category: representation
  severity: major
  status: resolved
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
  - EAFTER
  - EPREV
  - ETEST
  - EI0
  - EI1
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
  - https://github.com/CultureBotAI/HabitatMech/issues/2181
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T125452Z-bladder__9a6dd80c-record
    finding_id: F1
  disposition_reason: An exact source-path/expected-parent exclusion removes only
    the reviewed GOLD context contribution. Independent valid ancestry, source identifiers,
    counts/units and taxa are preserved. The separate parent record is unchanged.
- finding_id: F2
  issue_key: bladder--9a6dd80c-organ-as-genus
  category: representation
  severity: major
  status: resolved
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
  - EAFTER
  - EPREV
  - ETEST
  - EI0
  - EI1
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
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2181
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T125452Z-bladder__9a6dd80c-record
    finding_id: F2
  disposition_reason: The ITEM decision now retains the source mint UNGROUNDED with
    UBERON:0001255 as xref, not superclass or identity. Source observations and REVIEWED
    status remain; no exact lesion grounding is invented.
- finding_id: F3
  issue_key: bladder--9a6dd80c-mapping-endpoint-contract
  category: representation
  severity: major
  status: resolved
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
  - EAFTER
  - EPREV
  - ETEST
  - EI0
  - EI1
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
  - https://github.com/CultureBotAI/HabitatMech/issues/2181
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261015T125452Z-bladder__9a6dd80c-record
    finding_id: F3
  disposition_reason: 'This exact retained-mint witness no longer emits narrowMatch
    after removing the unsupported organ-parent decision. The global producer/schema/consumer
    contract remains unresolved under #1398; this disposition covers only the target
    finding.'
actions: []
limitations:
- Same-agent review, not independent approval. Original specimen/pair-evidence limitations
  remain; only scoped hierarchy and mapping witnesses are repaired.
- The polyp retains its source-context identity without an authored exact lesion definition.
  This is not an ontology-completeness claim or correction of the separate parent-polyp
  record.
- 'Global source-to-record mapping contract #1398 and parent identity #2171 remain
  open; export compatibility is not certified.'
- Configured label correspondence includes 2,061 no-adapter skips. iModulonDB is not
  applicable; no gene or expression claim is present.
- Final-head archive validation of this newly added observation is a subsequent release
  gate; exact captured-input full QC and real map/site publication have already passed.
notes:
- 'Issue #2184 additionally corrects three new rendered issue links; actual Jinja
  urlize regression is included. Immutable original reviews and existing committed
  history are untouched.'
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261015T125452Z-bladder__9a6dd80c-record
  relationship: Exact predecessor; all original finding identities and target scope
    retained.
```
