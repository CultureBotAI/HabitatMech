# Record review: Anal canal (habitatmech:GOLD.a613af1611)

- Review: 20261015T041830Z-anal_canal__0e185227-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T04:04:34Z
- Finished UTC: 2026-10-15T04:18:30Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The mammal-qualified minted canal identity remains separate from the human record and mucosa. UBERON:0000159 is an appropriate anatomical genus, but the whole-organ source parent and mapping endpoint contract are not supported.

## Scope And Provenance

Full individual scientific assessment of this exact record at the captured main revision.

Selection: Exact source path, generated identifier and PATHS.tsv resolution in an unreviewed host-associated cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base ea0bf6a2629ffcd2ed086310a5eee162d4f11cae.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.a613af1611 | data/habitats/host_associated/anal_canal__0e185227.yaml | generated | Anal canal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | habitatmech:GOLD.a613af1611 | Actual exit 0 at 2026-10-15T04:05:21Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/anal_canal__0e185227.yaml |
| validate-strict | passed | True | habitatmech:GOLD.a613af1611 | Actual exit 0 at 2026-10-15T04:06:28Z. uv run python scripts/validate_strict.py data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml<br>Validating 12 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      12<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | habitatmech:GOLD.a613af1611 | Actual exit 0 at 2026-10-15T04:06:50Z. No issues found<br>730 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | habitatmech:GOLD.a613af1611 | Actual exit 0 at 2026-10-15T04:06:51Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | habitatmech:GOLD.a613af1611 | Actual exit 0 at 2026-10-15T04:07:17Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | habitatmech:GOLD.a613af1611 | Actual exit 0 at 2026-10-15T04:07:23Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | habitatmech:GOLD.a613af1611 | Actual exit 0 at 2026-10-15T04:07:48Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | habitatmech:GOLD.a613af1611 | Actual exit 0 at 2026-10-15T04:08:50Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |

## Scientific And Domain Assessments

### Native structural and reproduction gates

schema: supported. Targets: habitatmech:GOLD.a613af1611.

All recorded commands passed: target schema, twelve-record strict validation, 730 session histories, 3,208-record reproduction, 32 graphs and 110 term requests. These are not scientific proof.

### Source identity and anatomical or host scope

identity: concern. Targets: habitatmech:GOLD.a613af1611.

The mammal-qualified minted canal identity remains separate from the human record and mucosa. UBERON:0000159 is an appropriate anatomical genus, but the whole-organ source parent and mapping endpoint contract are not supported. Current Uberon positively types anal canal part_of large intestine and subClassOf anatomical conduit. No source-member identity is inferred from the single frozen organism assertion.

### Frozen counts, source nodes and later inventories

quantity: supported. Targets: habitatmech:GOLD.a613af1611.

All original node IDs and frozen counts/units match the exact tree row; zero counts are omitted. The later normalized-path biosample and study inventories are distinct datasets and are not summed with ORGANISM counts. Matched rows and bounded empty results are recorded above.

### Optional evidence, parameters, taxa and causal claims

completeness: not_applicable. Targets: habitatmech:GOLD.a613af1611.

No target environmental-parameter, characteristic-taxon, causal-edge, dataset or discussion claim requires evidence expansion. No optional slot is populated merely for coverage. Original source members were not recovered.

## Findings

### F1: Source context is asserted as a broader habitat

major / open / confirmed; issue key: anal-canal--0e185227-source-parent.

The mammal anal canal is a terminal part of the large intestine, not a subtype of the whole organ. Exclude only the guarded immediate GOLD contribution habitatmech:GOLD.6bda0871e2 in gold_parent_exclusions.tsv; preserve independent ontology parents and verbatim source provenance.

### F2: Narrow predicate compares a different endpoint than the schema declares

major / open / confirmed; issue key: anal-canal--0e185227-mapping-endpoint-contract.

Native execution retains the source minted ID but copies skos:narrowMatch into source-to-record attestation. The actual narrower comparison is to an ontology parent, not the retained record. Resolve shared schema/producer/consumer endpoints under #1398; a broad/narrow swap or an unsupported ontology merge is not a fix. No formal SKOS self-link prohibition or SSSOM/KGX conformance is claimed.

## Recommended Actions And Acceptance Checks

### ACT1

The mammal anal canal is a terminal part of the large intestine, not a subtype of the whole organ. Exclude only the guarded immediate GOLD contribution habitatmech:GOLD.6bda0871e2 in gold_parent_exclusions.tsv; preserve independent ontology parents and verbatim source provenance. Correct only through the named maintained owners; do not patch generated YAML.

- Regress this exact source/record and retained valid claims, with all-source identity, count/unit and status invariants.
- Append authorized session history; run strict schema, history, provenance, exact corpus reproduction, configured label validation and full just qc.
- Compare actual semantic input and rebuild map/site as needed; retain existing URLs and save an immutable successor with exact finding lineage.

### ACT2

Native execution retains the source minted ID but copies skos:narrowMatch into source-to-record attestation. The actual narrower comparison is to an ontology parent, not the retained record. Resolve shared schema/producer/consumer endpoints under #1398; a broad/narrow swap or an unsupported ontology merge is not a fix. No formal SKOS self-link prohibition or SSSOM/KGX conformance is claimed. Correct only through the named maintained owners; do not patch generated YAML.

- Regress this exact source/record and retained valid claims, with all-source identity, count/unit and status invariants.
- Append authorized session history; run strict schema, history, provenance, exact corpus reproduction, configured label validation and full just qc.
- Compare actual semantic input and rebuild map/site as needed; retain existing URLs and save an immutable successor with exact finding lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/anal_canal__0e185227.yaml; Entire YAML | supports | All target fields, generated history and source attestations read. |
| ERULE | docs/CURATION.md; Identity, host context, strictly broader parents and guarded corrections | supports | Every parent is strictly broader; host taxa are not habitat identities; source attestations preserve context. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; SourceAttestation.mapping_predicate and GroundingStatusEnum | supports | The declared mapping endpoint is the generated record, with omission when it is the source concept. |
| ESEED | src/habitatmech/seed.py; resolve_gold, apply_decision, ingest_gold, apply_curated_definitions | supports | Native routes executed with the complete normalized mapping and claimant sets. Final ID, status and predicate matched the target: {"automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["UBERON:0000159"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.a613af1611", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "final": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["UBERON:0000159"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.a613af1611", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "mint": "habitatmech:GOLD.a613af1611"} |
| ET4 | data/raw/gold_ecosystem_paths.tsv; Rows 1042 | supports | [{"data": {"biosample_count": "0", "canonical_path": "Host-associated &gt; Mammals &gt; Digestive system &gt; Large intestine &gt; Anal canal", "depth": "5", "ecosystem": "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Large intestine", "ecosystem_type": "Digestive system", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:6703", "leaf_label": "Anal canal", "organism_count": "1", "specific_ecosystem": "Anal canal", "study_count": "0", "total_assertions": "1"}, "row": 1042}] |
| ET5 | data/raw/ontology_subclass_edges.tsv; Rows 11022 | supports | [{"data": {"object": "UBERON:0004111", "predicate": "rdfs:subClassOf", "subject": "UBERON:0000159"}, "row": 11022}] |
| ET6 | data/raw/ontology_terms.tsv; Rows 12904 | supports | [{"data": {"definition": "The terminal part of the large intestine, continuous proximally with the rectum and distally terminates with the anus.", "deprecated": "", "directly_referenced": "FALSE", "label": "anal canal", "label_only": "FALSE", "ontology": "UBERON", "synonyms": "anal canal&#124;anal canal viewed anatomically&#124;anal pad&#124;anatomical anal canal&#124;anus&#124;canalis analis&#124;cloaca&#124;cloacal chamber&#124;mesenteron&#124;pars analis recti", "term_id": "UBERON:0000159"}, "row": 12904}] |
| ET7 | data/habitats/PATHS.tsv; Rows 2519 | supports | [{"data": {"identifier": "habitatmech:GOLD.a613af1611", "slug": "anal_canal__0e185227"}, "row": 2519}] |
| ESEARCH | Local source and review inventory; rg --no-ignore --hidden -l -F -e Anaerobic -e 'Anal canal' -e 'Anal canal mucosa' -e 'Anorectal abscess' -e Anterior -e 'Anterior chamber' -e UBERON:0009963 -e UBERON:0016487 -e amphibia -e 'amphibian-associated environment' -e anaerobic -e anal_canal -e anal_canal__0e185227 -e anal_canal_mucosa -e anal_canal_mucosa__9fc95cf9 -e 'annelid-associated environment' -e annelida -e anorectal_abscess -e 'antennal gland' -e antennal_gland -e anterior -e 'anterior fornix of vagina' -e anterior_chamber -e anterior_fornix_of_vagina -e habitatmech:GOLD.0cd585a031 -e habitatmech:GOLD.1d3e238d30 -e habitatmech:GOLD.53e4290463 -e habitatmech:GOLD.6e10201167 -e habitatmech:GOLD.9d219f6fdc -e habitatmech:GOLD.9e917ffe11 -e habitatmech:GOLD.a2d2eb3d96 -e habitatmech:GOLD.a613af1611 -e habitatmech:GOLD.aaf13396b6 -e habitatmech:GOLD.c3e9d3ce0b -e habitatmech:GOLD.cb3fda7227 -e habitatmech:GOLD.e45d906034 curation history research reports data/raw build reviews | context_only | Ignored-inclusive text search returned 7,154 files. Exact parsed table matches: {"curation/decisions.tsv": 0, "curation/definition_source_label_exclusions.tsv": 0, "curation/external_xrefs.tsv": 0, "curation/gold_parent_exclusions.tsv": 0, "curation/record_annotation_corrections.tsv": 0, "curation/redirects_retracted.tsv": 0, "curation/samples/narrow-20260814.tsv": 0, "curation/term_requests.tsv": 0, "curation/term_requests_excluded.tsv": 0, "data/habitats/PATHS.tsv": 1, "data/raw/bacdive_isolation_sources.tsv": 0, "data/raw/bacdive_source_taxa.tsv": 0, "data/raw/environment_parameters.tsv": 0, "data/raw/gold_ecosystem_paths.tsv": 1, "data/raw/gold_path_biosamples.tsv": 0, "data/raw/gold_path_triads.tsv": 0, "data/raw/gold_studies.tsv": 0, "data/raw/isolation_source_groundings.tsv": 0, "data/raw/madin_habitat_taxa.tsv": 0, "data/raw/madin_habitats.tsv": 0, "data/raw/ontology_subclass_edges.tsv": 1, "data/raw/ontology_terms.tsv": 1, "data/raw/prego_habitat_taxa.tsv": 0, "data/raw/prego_habitats.tsv": 0} |
| EP9 | data/habitats/host_associated/large_intestine__834e53c8.yaml; Complete direct-parent record | supports | Parent meaning inspected: {"grounding_status": "NARROW", "identifier": "habitatmech:GOLD.6bda0871e2", "label": "Large intestine", "parent_habitats": ["UBERON:0000059", "habitatmech:GOLD.c8e85f3c84"]} |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000159; Target term fields and typed relations, or primary abstract | supports | Inspected current authoritative term UBERON:0000159 (anal canal), definition and obsolete flag False. Its scoped meaning is compared with the complete GOLD path in the scientific assessment. |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000159/graph; Target term fields and typed relations, or primary abstract | supports | Inspected typed outgoing edges: [{"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0004111", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"}, {"label": "part of", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0000059", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}, {"label": "continuous with", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0001052", "uri": "http://purl.obolibrary.org/obo/RO_0002150"}, {"label": "continuous with", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0001245", "uri": "http://purl.obolibrary.org/obo/RO_0002150"}, {"label": "part of", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0001353", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"}, {"label": "channel for", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0001988", "uri": "http://purl.obolibrary.org/obo/uberon/core#channel_for"}, {"label": "develops from", "source": "http://purl.obolibrary.org/obo/UBERON_0000159", "target": "http://purl.obolibrary.org/obo/UBERON_0011272", "uri": "http://purl.obolibrary.org/obo/RO_0002202"}]. Relation labels remain distinct; containment is not promoted to subclass. |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059; Target term fields and typed relations, or primary abstract | supports | Inspected current authoritative term UBERON:0000059 (large intestine), definition and obsolete flag False. Its scoped meaning is compared with the complete GOLD path in the scientific assessment. |

## Limits And Additional Notes

- Frozen GOLD tree assertions are not inspected original organism/member records. No microbial prevalence or membership claim is inferred.
- Configured label checks skipped 2,061 no-adapter pairs; identity and relation semantics were assessed separately.
- Full just qc and immutable archive checking are publication gates, not executed as part of these pre-fix scientific observations.
- No paid research or iModulonDB query was used: the target has no gene, regulator or transcriptomic claim.
- Literature and ontology examples do not establish all members of the source bin. Bounded searches do not establish global absence.
- Historical generated history and research prose were treated as leads; not every historical citation or neighboring-record claim was independently re-reviewed.
- Input hashes captured before assessment, then rechecked unchanged against both the working tree and exact Git blobs.
- Historical ad hoc reports informed search leads but are not structured predecessors; current structured-target traversal found no predecessor for this target.
- This observation is pre-fix. Subsequent authorized curation must retain it unchanged and use successor observations.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T041830Z-anal_canal__0e185227-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: Anal canal (habitatmech:GOLD.a613af1611)'
started_at: '2026-10-15T04:04:34Z'
finished_at: '2026-10-15T04:18:30Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Continuing agent assessed complete records and primary evidence;
    this is not independent human or second-agent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: The mammal-qualified minted canal identity remains separate from the human
  record and mucosa. UBERON:0000159 is an appropriate anatomical genus, but the whole-organ
  source parent and mapping endpoint contract are not supported.
source:
  git_revision: ea0bf6a2629ffcd2ed086310a5eee162d4f11cae
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
    sha256: d9c76d275d61b7fef860179b6d0472e54e15b2b027022d7a125a19f03881fd8e
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: a3e2880134344406dd3239ee041076df64c76407d311b71a16f2382c4146a177
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: be17ead1dfa258599ee8c31af96143b6415c059a3f0a48ac92ba6afa5c590831
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: 144e48a101aa072a96cd08f88a9a66ecd14122d788c54b95ac8ad7d934f720bc
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/samples/narrow-20260814.tsv
    sha256: 4d91c76ad5e0a46442075c7b9f882637130bacdfaedb25fbe7922f169d35051c
    role: context
  - path: curation/term_requests.tsv
    sha256: 1a03f5fb7ade4232aadf5ad248c87da894a67e90ef3eab513849982429a9155e
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
  - path: data/habitats/host_associated/abscess.yaml
    sha256: a237a4e64bf42c192f74281e9f5b647178a9fe3f97fa4c6c569831c7590f51b7
    role: context
  - path: data/habitats/host_associated/amphibia.yaml
    sha256: bf894618e9ea5b5fae5ea686af23687a6c685b079216843d31c8f98333d91a4a
    role: context
  - path: data/habitats/host_associated/anaerobic.yaml
    sha256: 79890c2683cd13ecd659b6d27bfafdb752cfab3936c572ecb986244b2fb06f3d
    role: context
  - path: data/habitats/host_associated/anal_canal.yaml
    sha256: 80e4d83cbcf4907460647631424c80a2e311b88b0c5d93733dfcde49ef37a07e
    role: context
  - path: data/habitats/host_associated/anal_canal__0e185227.yaml
    sha256: 14499d7f46b38534b53c5ea33d01ee500827ac62218a313a09f1d290d55c24f6
    role: target
  - path: data/habitats/host_associated/anal_canal_mucosa.yaml
    sha256: 4113f3e47b5070f1464fa0239db8eaeddd8726fc16ef6a0623c18c8d0e8cb2c7
    role: context
  - path: data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml
    sha256: f898599a4c9d9d3ac7485928bd32e4928dfb0408c7de05f11d09cf78ea91b776
    role: context
  - path: data/habitats/host_associated/annelida.yaml
    sha256: 2efaae9fa0f7c82ab7e3f580b34082cab8782e52daeffc0273fde57fce6ae8dc
    role: context
  - path: data/habitats/host_associated/anorectal_abscess.yaml
    sha256: f87c1d1c3c0053b78f007f932109145749a589db23ed345c41633356e76de461
    role: context
  - path: data/habitats/host_associated/antennal_gland.yaml
    sha256: 480c54e4ca98344a288a3ab6e2d8a414e7345ff6b20e60a5a3682f3546f092fd
    role: context
  - path: data/habitats/host_associated/anterior.yaml
    sha256: 26e6d56132ab4e33e0bfe239e7e626a788d621f8ab5685a4fb0ad9a91ae9f4c6
    role: context
  - path: data/habitats/host_associated/anterior_chamber.yaml
    sha256: 9aad1daf1e8bb7baf4cd50537f3e838b7bb9b991abb7aef120cc0475d79fc5de
    role: context
  - path: data/habitats/host_associated/anterior_fornix_of_vagina.yaml
    sha256: c9cee40893df13a4e879119ffd4bd7d23cc1028385fb75b1c475bab70d2d1b76
    role: context
  - path: data/habitats/host_associated/environmental_system_determined_by_an_organism.yaml
    sha256: d3b79ef9436a87fbce8e6b204b0113e170fa758e4a66efb592543bf934c67270
    role: context
  - path: data/habitats/host_associated/excretory_system__22ee753c.yaml
    sha256: bbf5d8ad1733d9f22bcf1da9fab714a194cde611972cd776fa022657cd50342a
    role: context
  - path: data/habitats/host_associated/hindgut.yaml
    sha256: 57936445bbdc99946910654e5bfa962409db425dac08d2c6bc3541d7658d41df
    role: context
  - path: data/habitats/host_associated/hindgut__afd87e04.yaml
    sha256: 6c1c1bbaf2a47c41aa6563c0029fd95612f59e1e5ecc7a89a621fd91c3f79602
    role: context
  - path: data/habitats/host_associated/hindgut__f414b618.yaml
    sha256: d9e6476df58f7b510f568e8c374b1f6173570da79653f246e76f023b0cb5fd0e
    role: context
  - path: data/habitats/host_associated/large_intestine__65b4f112.yaml
    sha256: 2d44a35bc5550a8bc65a76972a8e1958f1abdc8b0be8fadff277d57a2948ab94
    role: context
  - path: data/habitats/host_associated/large_intestine__834e53c8.yaml
    sha256: 2c086c4115cc2a0b04df48cb9b989c051c96d6625a64dbe26cef1ac90e6d4d15
    role: context
  - path: data/habitats/host_associated/parabasalids.yaml
    sha256: 202f2624454d9e6df589d2a7c2beeebeb491bde198d6176c429512222ebdb4ca
    role: context
  - path: data/habitats/host_associated/vagina__a4a4e1ad.yaml
    sha256: c965a38efccaf952e2483c4e29628957acf22ee4f1552f50a219430478917129
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
  - path: reports/yaml_record_review/20261004T004445Z-amphibia.md
    sha256: c2b6b4f5f88321eca85160a0fd282bdec628d427f83851e1bba7199a68125cf0
    role: context
  - path: reports/yaml_record_review/20261004T004918Z-anaerobic.md
    sha256: 68cb6f56821fe2df52c6b66849ba1440f3eff9c38d362935eef86ebf524b05f1
    role: context
  - path: reports/yaml_record_review/20261004T005342Z-anal_canal.md
    sha256: 1fa6ddb9cff8ea3551f3488ba0f705af5b5a01e57a9797256e6d913cc718bb46
    role: context
  - path: reports/yaml_record_review/20261004T005612Z-anal_canal__0e185227.md
    sha256: 826b61920579ba9bb944660fc8cad5efe3813726e10c1562b87b92af5bcc9a89
    role: context
  - path: reports/yaml_record_review/20261004T012233Z-anal_canal_mucosa.md
    sha256: 6e20b1422cbd4358a6eb883a4865c895599e8bb6ba02a2a88f901e7ec6b1966a
    role: context
  - path: reports/yaml_record_review/20261004T012458Z-anal_canal_mucosa__9fc95cf9.md
    sha256: 7fc3c3fdbf3132387112a60991c32715611cf984673a3a2307089302a3c6f87e
    role: context
  - path: reports/yaml_record_review/20261004T012835Z-annelida.md
    sha256: 76d2be86613bc5300b64f440e9642be8f7ac3ad9b3759c44617f86f2a21b49f6
    role: context
  - path: reports/yaml_record_review/20261004T013237Z-anorectal_abscess.md
    sha256: 155bfaa1dd590f5398b33f60b83a4f334bd89df1811fe328b0557bc17928a27c
    role: context
  - path: reports/yaml_record_review/20261004T013819Z-antennal_gland.md
    sha256: b4e4fe065c18ac0e21cf1d9ff426d9d43e6f53f9b7244ec563ed957ac49647ed
    role: context
  - path: reports/yaml_record_review/20261004T020529Z-anterior.md
    sha256: afbc2ec6d10729417f8e0553d04d5aed1da6877f3d929500adcb35191ef9c139
    role: context
  - path: reports/yaml_record_review/20261004T020959Z-anterior_chamber.md
    sha256: 75710ee181f640e5ae2b968ea570d70130d892a1ca8a39969aa8467ad3b78936
    role: context
  - path: reports/yaml_record_review/20261004T021258Z-anterior_fornix_of_vagina.md
    sha256: 8a788dec1a129c3c61a438b9a44883ba49013dfd14b84db173ad7da5556e3499
    role: context
  - path: research/habitats/engineered/dissolved-organics-anaerobic-habitatmech-gold-bb0eb00ccb-deep-research-claude_code.md
    sha256: 8d01ee8d97912ffeaa49d2091766972b09c91b18e181a9c9f1d866572e5fe7c6
    role: context
  - path: research/habitats/host_associated/amphibia-habitatmech-gold-0cd585a031-deep-research-claude_code.md
    sha256: bd08c04f2c7ae568fa923dfa5ac68d471ebbbe4335fca0d1b6bc73ce27b468e8
    role: context
  - path: research/habitats/host_associated/annelida-habitatmech-gold-6e10201167-deep-research-claude_code.md
    sha256: 94e6b80c7c03fa791ed49b0b706e748ac8148e1d1a57464707f6f1656aafa851
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/aggregate_gold_triads.py
    sha256: 0e25179dbecd7c73cbedd99a0ae44e56e4992afb9e1ec02d2411439f643b8e54
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
  - path: src/habitatmech/curate/gold_parent_exclusions.py
    sha256: 044d8277509a9b1f6e4f2d7ea1fb82319b41e09ffef7788738a0f4ed0d0b63af
    role: context
  - path: src/habitatmech/curate/record_annotation_corrections.py
    sha256: 15bad3d40fd95e2acc72d3ff3c74289c15fb8a1775adc523b3575c3ea8487033
    role: context
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
    role: context
  - path: src/habitatmech/seed.py
    sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
    role: context
  - path: src/habitatmech/templates/habitat.html
    sha256: f46b320798ce077395ea2cd1891a4721b090100de5f98d3f7480884f628c8311
    role: context
targets:
- target_id: habitatmech:GOLD.a613af1611
  path: data/habitats/host_associated/anal_canal__0e185227.yaml
  label: Anal canal
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/definition_source_label_exclusions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/external_xrefs.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/record_annotation_corrections.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/redirects_retracted.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests_excluded.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_isolation_sources.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/bacdive_source_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/environment_parameters.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_biosamples.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_path_triads.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_studies.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/isolation_source_groundings.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitats.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained source, curation input, or generator; target YAML is read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained source, curation input, or generator; target YAML is read-only
scope:
  description: Full individual scientific assessment of this exact record at the captured
    main revision.
  selection: Exact source path, generated identifier and PATHS.tsv resolution in an
    unreviewed host-associated cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.a613af1611
  exclusions:
  - target: Other records and SSSOM/KGX products
    reason: Parents and siblings are context only; no fleet-wide or export compatibility
      certification.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/anal_canal__0e185227.yaml
  locator: Entire YAML
  accessed_at: '2026-10-15T04:18:30Z'
  support: supports
  summary: All target fields, generated history and source attestations read.
  snapshot_sha256: 14499d7f46b38534b53c5ea33d01ee500827ac62218a313a09f1d290d55c24f6
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, host context, strictly broader parents and guarded corrections
  accessed_at: '2026-10-15T04:18:30Z'
  support: supports
  summary: Every parent is strictly broader; host taxa are not habitat identities;
    source attestations preserve context.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: SourceAttestation.mapping_predicate and GroundingStatusEnum
  accessed_at: '2026-10-15T04:18:30Z'
  support: supports
  summary: The declared mapping endpoint is the generated record, with omission when
    it is the source concept.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: resolve_gold, apply_decision, ingest_gold, apply_curated_definitions
  accessed_at: '2026-10-15T04:18:30Z'
  support: supports
  summary: 'Native routes executed with the complete normalized mapping and claimant
    sets. Final ID, status and predicate matched the target: {"automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": ["UBERON:0000159"],
    "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.a613af1611",
    "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"},
    "final": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents":
    ["UBERON:0000159"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier":
    "habitatmech:GOLD.a613af1611", "mapping_predicate": "skos:narrowMatch", "reviewed":
    false, "route": "gold_narrower_than_leaf_match"}, "mint": "habitatmech:GOLD.a613af1611"}'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: ET4
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Rows 1042
  accessed_at: '2026-10-15T04:18:30Z'
  support: supports
  summary: '[{"data": {"biosample_count": "0", "canonical_path": "Host-associated
    > Mammals > Digestive system > Large intestine > Anal canal", "depth": "5", "ecosystem":
    "Host-associated", "ecosystem_category": "Mammals", "ecosystem_subtype": "Large
    intestine", "ecosystem_type": "Digestive system", "gold_node_count": "1", "gold_node_ids":
    "gold.ecosystem:6703", "leaf_label": "Anal canal", "organism_count": "1", "specific_ecosystem":
    "Anal canal", "study_count": "0", "total_assertions": "1"}, "row": 1042}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET5
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Rows 11022
  accessed_at: '2026-10-15T04:18:30Z'
  support: supports
  summary: '[{"data": {"object": "UBERON:0004111", "predicate": "rdfs:subClassOf",
    "subject": "UBERON:0000159"}, "row": 11022}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET6
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Rows 12904
  accessed_at: '2026-10-15T04:18:30Z'
  support: supports
  summary: '[{"data": {"definition": "The terminal part of the large intestine, continuous
    proximally with the rectum and distally terminates with the anus.", "deprecated":
    "", "directly_referenced": "FALSE", "label": "anal canal", "label_only": "FALSE",
    "ontology": "UBERON", "synonyms": "anal canal|anal canal viewed anatomically|anal
    pad|anatomical anal canal|anus|canalis analis|cloaca|cloacal chamber|mesenteron|pars
    analis recti", "term_id": "UBERON:0000159"}, "row": 12904}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET7
  kind: database
  reference: data/habitats/PATHS.tsv
  locator: Rows 2519
  accessed_at: '2026-10-15T04:18:30Z'
  support: supports
  summary: '[{"data": {"identifier": "habitatmech:GOLD.a613af1611", "slug": "anal_canal__0e185227"},
    "row": 2519}]'
  snapshot_sha256: b0135af0aa4deed0f3824a2f491d5a742c1b7de4775c533f283761d22e805821
- evidence_id: ESEARCH
  kind: search
  reference: Local source and review inventory
  locator: rg --no-ignore --hidden -l -F -e Anaerobic -e 'Anal canal' -e 'Anal canal
    mucosa' -e 'Anorectal abscess' -e Anterior -e 'Anterior chamber' -e UBERON:0009963
    -e UBERON:0016487 -e amphibia -e 'amphibian-associated environment' -e anaerobic
    -e anal_canal -e anal_canal__0e185227 -e anal_canal_mucosa -e anal_canal_mucosa__9fc95cf9
    -e 'annelid-associated environment' -e annelida -e anorectal_abscess -e 'antennal
    gland' -e antennal_gland -e anterior -e 'anterior fornix of vagina' -e anterior_chamber
    -e anterior_fornix_of_vagina -e habitatmech:GOLD.0cd585a031 -e habitatmech:GOLD.1d3e238d30
    -e habitatmech:GOLD.53e4290463 -e habitatmech:GOLD.6e10201167 -e habitatmech:GOLD.9d219f6fdc
    -e habitatmech:GOLD.9e917ffe11 -e habitatmech:GOLD.a2d2eb3d96 -e habitatmech:GOLD.a613af1611
    -e habitatmech:GOLD.aaf13396b6 -e habitatmech:GOLD.c3e9d3ce0b -e habitatmech:GOLD.cb3fda7227
    -e habitatmech:GOLD.e45d906034 curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-15T04:06:20Z'
  support: context_only
  summary: 'Ignored-inclusive text search returned 7,154 files. Exact parsed table
    matches: {"curation/decisions.tsv": 0, "curation/definition_source_label_exclusions.tsv":
    0, "curation/external_xrefs.tsv": 0, "curation/gold_parent_exclusions.tsv": 0,
    "curation/record_annotation_corrections.tsv": 0, "curation/redirects_retracted.tsv":
    0, "curation/samples/narrow-20260814.tsv": 0, "curation/term_requests.tsv": 0,
    "curation/term_requests_excluded.tsv": 0, "data/habitats/PATHS.tsv": 1, "data/raw/bacdive_isolation_sources.tsv":
    0, "data/raw/bacdive_source_taxa.tsv": 0, "data/raw/environment_parameters.tsv":
    0, "data/raw/gold_ecosystem_paths.tsv": 1, "data/raw/gold_path_biosamples.tsv":
    0, "data/raw/gold_path_triads.tsv": 0, "data/raw/gold_studies.tsv": 0, "data/raw/isolation_source_groundings.tsv":
    0, "data/raw/madin_habitat_taxa.tsv": 0, "data/raw/madin_habitats.tsv": 0, "data/raw/ontology_subclass_edges.tsv":
    1, "data/raw/ontology_terms.tsv": 1, "data/raw/prego_habitat_taxa.tsv": 0, "data/raw/prego_habitats.tsv":
    0}'
  search_scope: Hidden/ignored files included under curation, history, research, reports,
    data/raw, build and reviews. All TSV rows parsed for exact IDs/paths; study path-list
    membership tested exactly. Original remote members are not covered.
- evidence_id: EP9
  kind: record_content
  reference: data/habitats/host_associated/large_intestine__834e53c8.yaml
  locator: Complete direct-parent record
  accessed_at: '2026-10-15T04:18:30Z'
  support: supports
  summary: 'Parent meaning inspected: {"grounding_status": "NARROW", "identifier":
    "habitatmech:GOLD.6bda0871e2", "label": "Large intestine", "parent_habitats":
    ["UBERON:0000059", "habitatmech:GOLD.c8e85f3c84"]}'
  snapshot_sha256: 2c086c4115cc2a0b04df48cb9b989c051c96d6625a64dbe26cef1ac90e6d4d15
- evidence_id: EX1
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000159
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:04:38Z'
  support: supports
  summary: Inspected current authoritative term UBERON:0000159 (anal canal), definition
    and obsolete flag False. Its scoped meaning is compared with the complete GOLD
    path in the scientific assessment.
  snapshot_sha256: 7fc4ee47acc70030aebb13083fbc09ef38c1855e37b63d578100ac8a8c01cf8f
- evidence_id: EX2
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000159/graph
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:05:20Z'
  support: supports
  summary: 'Inspected typed outgoing edges: [{"label": "subClassOf", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004111", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf"},
    {"label": "part of", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000059", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"},
    {"label": "continuous with", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001052", "uri": "http://purl.obolibrary.org/obo/RO_0002150"},
    {"label": "continuous with", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001245", "uri": "http://purl.obolibrary.org/obo/RO_0002150"},
    {"label": "part of", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001353", "uri": "http://purl.obolibrary.org/obo/BFO_0000050"},
    {"label": "channel for", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001988", "uri": "http://purl.obolibrary.org/obo/uberon/core#channel_for"},
    {"label": "develops from", "source": "http://purl.obolibrary.org/obo/UBERON_0000159",
    "target": "http://purl.obolibrary.org/obo/UBERON_0011272", "uri": "http://purl.obolibrary.org/obo/RO_0002202"}].
    Relation labels remain distinct; containment is not promoted to subclass.'
  snapshot_sha256: f12805206dabe9442d32d9cbb027d9ae3246a2160074e23103f8a6c676fdec99
- evidence_id: EX3
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059
  locator: Target term fields and typed relations, or primary abstract
  accessed_at: '2026-10-15T04:05:15Z'
  support: supports
  summary: Inspected current authoritative term UBERON:0000059 (large intestine),
    definition and obsolete flag False. Its scoped meaning is compared with the complete
    GOLD path in the scientific assessment.
  snapshot_sha256: d43e203ec23dc43e60bf4f3eeef91235a695dc997d4784a65919688f223aaba8
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/anal_canal__0e185227.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a613af1611
  summary: "Actual exit 0 at 2026-10-15T04:05:21Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/anal_canal__0e185227.yaml"
  scope_note: Target schema; strict command covers twelve targets; history, corpus,
    provenance, causal, term-request and label checks have documented corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml
    data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml
    data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml
    data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml
    data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml
    data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a613af1611
  summary: "Actual exit 0 at 2026-10-15T04:06:28Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/amphibia.yaml data/habitats/host_associated/anaerobic.yaml\
    \ data/habitats/host_associated/anal_canal.yaml data/habitats/host_associated/anal_canal__0e185227.yaml\
    \ data/habitats/host_associated/anal_canal_mucosa.yaml data/habitats/host_associated/anal_canal_mucosa__9fc95cf9.yaml\
    \ data/habitats/host_associated/annelida.yaml data/habitats/host_associated/anorectal_abscess.yaml\
    \ data/habitats/host_associated/antennal_gland.yaml data/habitats/host_associated/anterior.yaml\
    \ data/habitats/host_associated/anterior_chamber.yaml data/habitats/host_associated/anterior_fornix_of_vagina.yaml\n\
    Validating 12 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      12\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Target schema; strict command covers twelve targets; history, corpus,
    provenance, causal, term-request and label checks have documented corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a613af1611
  summary: 'Actual exit 0 at 2026-10-15T04:06:50Z. No issues found

    730 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Target schema; strict command covers twelve targets; history, corpus,
    provenance, causal, term-request and label checks have documented corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a613af1611
  summary: "Actual exit 0 at 2026-10-15T04:06:51Z. provenance current: 14 committed\
    \ inventories, 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Target schema; strict command covers twelve targets; history, corpus,
    provenance, causal, term-request and label checks have documented corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a613af1611
  summary: "Actual exit 0 at 2026-10-15T04:07:17Z. expected 3208 records, found 3208\
    \ on disk\n  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces\
    \ exactly from data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Target schema; strict command covers twelve targets; history, corpus,
    provenance, causal, term-request and label checks have documented corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a613af1611
  summary: "Actual exit 0 at 2026-10-15T04:07:23Z. validated 32 causal-graph curation\
    \ file(s) with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Target schema; strict command covers twelve targets; history, corpus,
    provenance, causal, term-request and label checks have documented corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a613af1611
  summary: "Actual exit 0 at 2026-10-15T04:07:48Z. term-request table is current (110\
    \ terms)\n uv run python scripts/build_term_requests.py --check"
  scope_note: Target schema; strict command covers twelve targets; history, corpus,
    provenance, causal, term-request and label checks have documented corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - habitatmech:GOLD.a613af1611
  summary: "Actual exit 0 at 2026-10-15T04:08:50Z. id↔label correspondence summary:\n\
    \          OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Target schema; strict command covers twelve targets; history, corpus,
    provenance, causal, term-request and label checks have documented corpus scope.
assessments:
- assessment_id: A1
  area: schema
  topic: Native structural and reproduction gates
  outcome: supported
  summary: 'All recorded commands passed: target schema, twelve-record strict validation,
    730 session histories, 3,208-record reproduction, 32 graphs and 110 term requests.
    These are not scientific proof.'
  target_ids:
  - habitatmech:GOLD.a613af1611
  evidence_ids:
  - E1
  - ERULE
- assessment_id: A2
  area: identity
  topic: Source identity and anatomical or host scope
  outcome: concern
  summary: The mammal-qualified minted canal identity remains separate from the human
    record and mucosa. UBERON:0000159 is an appropriate anatomical genus, but the
    whole-organ source parent and mapping endpoint contract are not supported. Current
    Uberon positively types anal canal part_of large intestine and subClassOf anatomical
    conduit. No source-member identity is inferred from the single frozen organism
    assertion.
  target_ids:
  - habitatmech:GOLD.a613af1611
  evidence_ids:
  - E1
  - ESEED
  - EX1
  - EX2
  - EX3
- assessment_id: A3
  area: quantity
  topic: Frozen counts, source nodes and later inventories
  outcome: supported
  summary: All original node IDs and frozen counts/units match the exact tree row;
    zero counts are omitted. The later normalized-path biosample and study inventories
    are distinct datasets and are not summed with ORGANISM counts. Matched rows and
    bounded empty results are recorded above.
  target_ids:
  - habitatmech:GOLD.a613af1611
  evidence_ids:
  - E1
  - ESEARCH
  dimensions:
  - name: source-path
    value: Host-associated > Mammals > Digestive system > Large intestine > Anal canal
    definition: Exact GOLD context, not an automatic subclass axiom.
    evidence_ids:
    - E1
  - name: native-status
    value: NARROW/SEEDED
    definition: Deterministic grounding and all-source decision depth; not this scientific
      verdict.
    evidence_ids:
    - E1
    - ESEED
- assessment_id: A4
  area: completeness
  topic: Optional evidence, parameters, taxa and causal claims
  outcome: not_applicable
  summary: No target environmental-parameter, characteristic-taxon, causal-edge, dataset
    or discussion claim requires evidence expansion. No optional slot is populated
    merely for coverage. Original source members were not recovered.
  target_ids:
  - habitatmech:GOLD.a613af1611
  evidence_ids:
  - E1
  - ESEARCH
findings:
- finding_id: F1
  issue_key: anal-canal--0e185227-source-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Source context is asserted as a broader habitat
  description: The mammal anal canal is a terminal part of the large intestine, not
    a subtype of the whole organ. Exclude only the guarded immediate GOLD contribution
    habitatmech:GOLD.6bda0871e2 in gold_parent_exclusions.tsv; preserve independent
    ontology parents and verbatim source provenance.
  target_ids:
  - habitatmech:GOLD.a613af1611
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESEED
  - EX1
  - EX2
  - EX3
  rule_id: docs/CURATION.md; SourceAttestation contract; native record-review checklist
  native_severity: major
  normalization_reason: Material semantic error; schema validity does not establish
    this claim.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated habitat files are read-only
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1325
- finding_id: F2
  issue_key: anal-canal--0e185227-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Narrow predicate compares a different endpoint than the schema declares
  description: 'Native execution retains the source minted ID but copies skos:narrowMatch
    into source-to-record attestation. The actual narrower comparison is to an ontology
    parent, not the retained record. Resolve shared schema/producer/consumer endpoints
    under #1398; a broad/narrow swap or an unsupported ontology merge is not a fix.
    No formal SKOS self-link prohibition or SSSOM/KGX conformance is claimed.'
  target_ids:
  - habitatmech:GOLD.a613af1611
  field_paths:
  - grounding_status
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - E1
  - ESCHEMA
  - ESEED
  rule_id: docs/CURATION.md; SourceAttestation contract; native record-review checklist
  native_severity: major
  normalization_reason: Material semantic error; schema validity does not establish
    this claim.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; generated habitat files are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated habitat files are read-only
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.a613af1611
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; generated habitat files are read-only
  description: The mammal anal canal is a terminal part of the large intestine, not
    a subtype of the whole organ. Exclude only the guarded immediate GOLD contribution
    habitatmech:GOLD.6bda0871e2 in gold_parent_exclusions.tsv; preserve independent
    ontology parents and verbatim source provenance. Correct only through the named
    maintained owners; do not patch generated YAML.
  generator: just seed; inspect just seed-canary before seed-apply; regenerate affected
    term requests, map and pages through supported commands
  acceptance_checks:
  - Regress this exact source/record and retained valid claims, with all-source identity,
    count/unit and status invariants.
  - Append authorized session history; run strict schema, history, provenance, exact
    corpus reproduction, configured label validation and full just qc.
  - Compare actual semantic input and rebuild map/site as needed; retain existing
    URLs and save an immutable successor with exact finding lineage.
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.a613af1611
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; generated habitat files are read-only
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; generated habitat files are read-only
  description: 'Native execution retains the source minted ID but copies skos:narrowMatch
    into source-to-record attestation. The actual narrower comparison is to an ontology
    parent, not the retained record. Resolve shared schema/producer/consumer endpoints
    under #1398; a broad/narrow swap or an unsupported ontology merge is not a fix.
    No formal SKOS self-link prohibition or SSSOM/KGX conformance is claimed. Correct
    only through the named maintained owners; do not patch generated YAML.'
  generator: just seed; inspect just seed-canary before seed-apply; regenerate affected
    term requests, map and pages through supported commands
  acceptance_checks:
  - Regress this exact source/record and retained valid claims, with all-source identity,
    count/unit and status invariants.
  - Append authorized session history; run strict schema, history, provenance, exact
    corpus reproduction, configured label validation and full just qc.
  - Compare actual semantic input and rebuild map/site as needed; retain existing
    URLs and save an immutable successor with exact finding lineage.
limitations:
- Frozen GOLD tree assertions are not inspected original organism/member records.
  No microbial prevalence or membership claim is inferred.
- Configured label checks skipped 2,061 no-adapter pairs; identity and relation semantics
  were assessed separately.
- Full just qc and immutable archive checking are publication gates, not executed
  as part of these pre-fix scientific observations.
- 'No paid research or iModulonDB query was used: the target has no gene, regulator
  or transcriptomic claim.'
- Literature and ontology examples do not establish all members of the source bin.
  Bounded searches do not establish global absence.
- Historical generated history and research prose were treated as leads; not every
  historical citation or neighboring-record claim was independently re-reviewed.
notes:
- Input hashes captured before assessment, then rechecked unchanged against both the
  working tree and exact Git blobs.
- Historical ad hoc reports informed search leads but are not structured predecessors;
  current structured-target traversal found no predecessor for this target.
- This observation is pre-fix. Subsequent authorized curation must retain it unchanged
  and use successor observations.
tags:
- individual-scientific-review
- host-associated
```
