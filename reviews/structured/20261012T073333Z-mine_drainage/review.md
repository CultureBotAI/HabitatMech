# Scientific record review: mine_drainage

- Review: 20261012T073333Z-mine_drainage
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-12T07:21:36.362312Z
- Finished UTC: 2026-10-12T07:33:33.789461Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Groundwater/Mine drainage: ENVO treats drainage as an outflow/watercourse feature, while the other parent denotes groundwater material. USGS permits drainage from groundwater or surface water; that does not settle this exact source intent. Later ARMAN samples are contextual, not universal acidity evidence.

## Scope And Provenance

Entire exact generated record, all source contributors and asserted fields, with bounded source-context assessment.

Selection: Next forty records without a completed individual scientific review in stable repository-relative path order: microbial_mats__2265bbbd through ocean_trench. Full individual observations, not a category-wide pass. Prior coverage counts distinct observations, not a clean current-input corpus. Starting distinct-review coverage 728/3208 is not clean current-input coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f7727c58b4e3d4883ecaab0dc81441e4a85b716b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.342d26e2ac | data/habitats/aquatic/mine_drainage.yaml | generated | Mine drainage |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native gate on captured inputs | passed | True | habitatmech:GOLD.342d26e2ac | Actual success 2026-10-12T07:23:55.438802Z to 2026-10-12T07:23:58.165721Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | habitatmech:GOLD.342d26e2ac | Actual success 2026-10-12T07:24:43.138183Z to 2026-10-12T07:24:53.380336Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | habitatmech:GOLD.342d26e2ac | Actual success 2026-10-12T07:24:53.381554Z to 2026-10-12T07:25:17.592324Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | habitatmech:GOLD.342d26e2ac | Actual success 2026-10-12T07:25:17.593658Z to 2026-10-12T07:26:19.939303Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | habitatmech:GOLD.342d26e2ac | Actual success 2026-10-12T07:26:19.940781Z to 2026-10-12T07:26:29.078055Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | habitatmech:GOLD.342d26e2ac | Actual success 2026-10-12T07:26:29.079194Z to 2026-10-12T07:26:34.354132Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | habitatmech:GOLD.342d26e2ac | Actual success 2026-10-12T07:26:34.355124Z to 2026-10-12T07:26:54.824749Z. Native command scope retained. |
| Native gate on captured inputs | passed | True | habitatmech:GOLD.342d26e2ac | Actual success 2026-10-12T07:26:54.826025Z to 2026-10-12T07:26:55.497046Z. Native command scope retained. |
| Exact-base CI authoritative QC | passed | True | habitatmech:GOLD.342d26e2ac | Actual success 2026-10-12T07:23:23.595254Z to 2026-10-12T07:23:25.901988Z. All three required merge-group workflows passed at the exact captured base; authoritative QC passed 946 tests with 3 skipped. Newly saved review bundles require their own integrity check. These newly saved review bundles were not part of that earlier exact-base CI run. |
| Full target reconstruction | passed | False | habitatmech:GOLD.342d26e2ac | All forty complete documents matched; captured input hashes rechecked before authoring. |
| Original occurrence inputs | unavailable | False | habitatmech:GOLD.342d26e2ac | Bounded ignored-inclusive searches did not recover complete original inputs. Later GOLD context is not original assertion membership. |
| Expression-adapter applicability | not_applicable | False | habitatmech:GOLD.342d26e2ac | No claim-specific gene, regulator or expression-module assertion warrants an adapter query. |

## Scientific And Domain Assessments

### Exact identity and source scope

identity: concern. Targets: habitatmech:GOLD.342d26e2ac.

Groundwater/Mine drainage: ENVO treats drainage as an outflow/watercourse feature, while the other parent denotes groundwater material. USGS permits drainage from groundwater or surface water; that does not settle this exact source intent. Later ARMAN samples are contextual, not universal acidity evidence.

### All strict-parent contributors and mapping endpoints

grounding: concern. Targets: habitatmech:GOLD.342d26e2ac.

Groundwater/Mine drainage: ENVO treats drainage as an outflow/watercourse feature, while the other parent denotes groundwater material. USGS permits drainage from groundwater or surface water; that does not settle this exact source intent. Later ARMAN samples are contextual, not universal acidity evidence. Actual ontology, GOLD context, automatic leaf and curated-genus contributions were distinguished.

### Source units and ITEM lifecycle

provenance: supported. Targets: habitatmech:GOLD.342d26e2ac.

Complete reconstruction preserves 1 source concepts and 0 ITEM-reviewed contributors. Counts with distinct units are not added; seeded and reviewed statuses describe native provenance, not automatic scientific correctness.

### Optional fields and mechanism applicability

completeness: supported. Targets: habitatmech:GOLD.342d26e2ac.

No causal graph, gene/regulator or expression-module claim is asserted in the complete target. Optional empty slots alone are not defects. Bounded supporting-file search included ignored files; no expression-adapter query was applicable.

## Findings

### F1: Narrow mapping uses an undeclared ontology comparison endpoint

major / open / confirmed; issue key: habitatmech-gold.342d26e2ac-mapping-endpoint.

A source-specific mint is retained and the generic ontology class is a parent. narrowMatch compares to that parent, but SourceAttestation describes comparison to the generated record. This is an endpoint contract ambiguity, not proof of formal SKOS self-inconsistency.

### F2: Resolve excavation or drainage feature versus sampled-water identity

major / open / provisional; issue key: habitatmech-gold.342d26e2ac-source-entity-scope.

Groundwater/Mine drainage: ENVO treats drainage as an outflow/watercourse feature, while the other parent denotes groundwater material. USGS permits drainage from groundwater or surface water; that does not settle this exact source intent. Later ARMAN samples are contextual, not universal acidity evidence.

## Recommended Actions And Acceptance Checks

### A1

Resolve shared issue #1398 with explicit subject/predicate/object semantics and SSSOM/KGX consumer tests; retain source-specific identities. Reversing the predicate alone cannot supply a missing endpoint.

- Change only maintained owners after source-level assessment; retain independent true parents, source identity/count/unit provenance and lifecycle unless a separately justified change requires otherwise.
- Append required current history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, label, provenance, corpus reproduction, causal/history and full QC gates; save a linked successor for any finding disposition.

### A2

Assess original membership and source intent before choosing feature versus sampled-water genera. Do not simply delete one parent or equate all mine waters with acid mine drainage.

- Change only maintained owners after source-level assessment; retain independent true parents, source identity/count/unit provenance and lifecycle unless a separately justified change requires otherwise.
- Append required current history, add focused regressions, inspect a seed canary and regenerate affected products without hand-editing records or pages.
- Pass schema, strict, label, provenance, corpus reproduction, causal/history and full QC gates; save a linked successor for any finding disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/aquatic/mine_drainage.yaml; Entire captured YAML read, including all taxa, parameters, graphs and generated history | supports | Groundwater/Mine drainage: ENVO treats drainage as an outflow/watercourse feature, while the other parent denotes groundwater material. USGS permits drainage from groundwater or surface water; that does not settle this exact source intent. Later ARMAN samples are contextual, not universal acidity evidence. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml | supports | Applied exact identity, strict-genus, MIxS roles, source-unit/score and ITEM lifecycle contracts; graph node types retain their biological definitions. |
| RAW | data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; Exact logical TSV rows, header=row1; filtered by current source IDs and exact paths, not legacy issue line numbers | supports | {"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Environmental &gt; Aquatic &gt; Freshwater &gt; Groundwater &gt; Mine drainage", "depth": "5", "ecosystem": "Environmental", "ecosystem_category": "Aquatic", "ecosystem_subtype": "Groundwater", "ecosystem_type": "Freshwater", "gold_node_count": "1", "gold_node_ids": "gold.ecosystem:4170", "leaf_label": "Mine drainage", "organism_count": "0", "specific_ecosystem": "Mine drainage", "study_count": "0", "total_assertions": "0"}, "logical_row": 1469}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "9", "canonical_path": "Environmental &gt; Aquatic &gt; Freshwater &gt; Groundwater &gt; Mine drainage", "ecosystem_path_id": "4170"}, "logical_row": 647}], "data/raw/gold_path_triads.tsv": [{"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Freshwater &gt; Groundwater &gt; Mine drainage", "distinct_terms": "1", "samples": "9", "slot": "broad", "studies": "3", "studies_agreeing": "3", "top_label": "aquatic biome", "top_share": "1.00", "top_term": "ENVO:00002030"}, "logical_row": 287}, {"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Freshwater &gt; Groundwater &gt; Mine drainage", "distinct_terms": "2", "samples": "9", "slot": "local", "studies": "3", "studies_agreeing": "2", "top_label": "acid mine drainage", "top_share": "0.78", "top_term": "ENVO:00001997"}, "logical_row": 288}, {"data": {"canonical_path": "Environmental &gt; Aquatic &gt; Freshwater &gt; Groundwater &gt; Mine drainage", "distinct_terms": "2", "samples": "9", "slot": "medium", "studies": "3", "studies_agreeing": "2", "top_label": "acidic water", "top_share": "0.78", "top_term": "ENVO:01000358"}, "logical_row": 289}]} |
| CODE | src/habitatmech/seed.py; Executed complete-document reconstruction; all 40 matched; routes distinguish source mints and generated identity | supports | {"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:00001996"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.342d26e2ac", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": ["ENVO:00001996"], "extra_xrefs": [], "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.342d26e2ac", "mapping_predicate": "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "minted": "habitatmech:GOLD.342d26e2ac", "source": "GOLD", "source_id": "gold.ecosystem:4170"}], "source_concepts": 1} |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Official OWL retrieved 12-Oct; labels, definitions, typed synonyms, named parents and restrictions; no snapshot refresh | supports | {"ENVO:00001996": {"definitions": ["The outflow of water from a mine."], "deprecated": [], "equivalents": [], "labels": ["mine drainage"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000029", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00000076"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["acid and metalliferous drainage", "acid rock drainage"]}}, "ENVO:00002006": {"definitions": ["An environmental material primarily composed of dihydrogen oxide in its liquid form."], "deprecated": [], "equivalents": [], "labels": ["liquid water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000815", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_15377"]}], "replacements": [], "synonyms": {"hasBroadSynonym": ["water"], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002011": {"definitions": ["Water which has a low concentration of dissolved solutes, particularly that of sodium chloride."], "deprecated": [], "equivalents": [], "labels": ["fresh water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["freshwater"], "hasNarrowSynonym": [], "hasRelatedSynonym": ["sweet water"]}}, "ENVO:00005792": {"definitions": ["Water which has physicochemical properties determined by processes which occur beneath the planetary crust."], "deprecated": [], "equivalents": [], "labels": ["underground water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0001025"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000941"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": ["subterranean water"]}}, "ENVO:01001004": {"definitions": ["Underground water which is located in pore spaces found in rock or unconsolidated deposits such as soil, clay, or gravel."], "deprecated": [], "equivalents": [], "labels": ["groundwater"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00005792", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0001025"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00012408"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["ground water"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}} |
| PARENT | data/habitats/aquatic/groundwater__25377149.yaml; data/habitats/aquatic/groundwater__585f08d9.yaml; data/habitats/aquatic/underground_water.yaml; data/habitats/aquatic/liquid_water.yaml; data/habitats/aquatic/fresh_water.yaml; Ancestor context adds no full-record coverage | supports | {"ENVO:00002006": {"definition": "An environmental material primarily composed of dihydrogen oxide in its liquid form.", "grounding_status": "EXACT", "label": "liquid water", "parent_habitats": ["ENVO:01000815"]}, "ENVO:00002011": {"definition": "Water which has a low concentration of dissolved solutes, particularly that of sodium chloride.", "grounding_status": "EXACT", "label": "fresh water", "parent_habitats": ["ENVO:00002006"]}, "ENVO:00005792": {"definition": "Water which has physicochemical properties determined by processes which occur beneath the planetary crust.", "grounding_status": "EXACT", "label": "underground water", "parent_habitats": ["ENVO:00002006"]}, "ENVO:01001004": {"definition": "Underground water which is located in pore spaces found in rock or unconsolidated deposits such as soil, clay, or gravel.", "grounding_status": "EXACT", "label": "groundwater", "parent_habitats": ["ENVO:00005792"]}, "habitatmech:GOLD.7f8e268653": {"definition": null, "grounding_status": "NARROW", "label": "Groundwater", "parent_habitats": ["ENVO:00002011", "ENVO:01001004"]}} |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; Five-position ecosystem paths preserved; contacts excluded; first 3 BioSample and Organism descriptions per target | supports | Exact positional census counts={"Biosample": 9, "Organism": 0, "SequencingProject": 10}; individually inspected descriptions={"Biosample": [{"data": {"BIOSAMPLE GOLD ID": "Gb0051935", "BIOSAMPLE NAME": "Acid Mine Drainage (ARMAN) microbial communities from Richmond mine, Iron Mountain, CA, USA - Site 1", "BIOSAMPLE NCBI TAX NAME": "mine drainage metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Richmond mine, Iron Mountain, California, USA"}, "row": 757}, {"data": {"BIOSAMPLE GOLD ID": "Gb0051936", "BIOSAMPLE NAME": "Acid Mine Drainage (ARMAN) microbial communities from Richmond mine, Iron Mountain, CA, USA -UBA Waterfall", "BIOSAMPLE NCBI TAX NAME": "mine drainage metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Richmond mine, Iron Mountain, California, USA"}, "row": 758}, {"data": {"BIOSAMPLE GOLD ID": "Gb0051937", "BIOSAMPLE NAME": "Acid Mine Drainage (ARMAN) microbial communities from Richmond mine, Iron Mountain, CA, USA", "BIOSAMPLE NCBI TAX NAME": "mine drainage metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Richmond mine, Iron Mountain, California, USA"}, "row": 759}], "Organism": []}. These later examples may include mixed sample/host/enrichment contexts; they do not reconstruct original assertion membership. Remaining members and study joins were indexed, not individually assessed. |
| CLASS | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Later official classification; Exact later classification tuples compared; missing tuples do not establish nonexistence | supports | [{"row": 583, "slug": "mine_drainage", "path": "Environmental &gt; Aquatic &gt; Freshwater &gt; Groundwater &gt; Mine drainage", "values": ["4170", "Environmental", "Aquatic", "Freshwater", "Groundwater", "Mine drainage"]}] |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf; Search boundaries are explicit; no global absence claim | supports | Identifier, label, slug and exact-path searches included hidden/ignored files in these roots. No earlier structured target observation was found. Legacy reports exist and are not silently retired. Bounded original-source search={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv", "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv", "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv", "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv", "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv", "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv", "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv", "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv", "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv", "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv", "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}], "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "exit_code": 0, "matches": [], "stderr": ""}]} |
| ISSUES | https://github.com/CultureBotAI/HabitatMech/issues; GitHub CLI inventory retrieved 12-Oct | supports | All-state971-issue title/body inventory and relevant bodies inspected. Issues are historical leads, not primary support. Comments were not exhaustively crawled; issue #1397 witness comments were additionally checked. |
| DRAIN | https://www.usgs.gov/mission-areas/water-resources/science/mine-drainage; Background and How does mine drainage occur | supports | USGS distinguishes waters draining active or abandoned mines, including surface and groundwater. Generic mine water is not necessarily flowing out; drainage need not universally be acidic. |

## Limits And Additional Notes

- This completed bounded review is not a clean-record verdict or exhaustive validation of original source occurrences.
- Only the first three exact-path BioSample and Organism descriptions per target/sheet were individually interpreted; remaining members and study joins were indexed only.
- Later GOLD export/classification does not reconstruct original August membership; no source snapshot was refreshed.
- Same-agent assessment, not independent approval. Initial review capture precedes separately authorized curation.
- SSSOM/KGX conformance to current kg-microbe modeling was not audited; issue #1398 remains unresolved.
- Current label validation has no-adapter skips and accepted exceptions; broad gates do not expand scientific coverage.
- Initial observation captured before separately authorized curation/publication; no paid research.
- No earlier structured target observation found; legacy reports are historical and are not automatically superseded.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T073333Z-mine_drainage
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: mine_drainage'
started_at: '2026-10-12T07:21:36.362312Z'
finished_at: '2026-10-12T07:33:33.789461Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Agent has participated in repository curation; this is not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Groundwater/Mine drainage: ENVO treats drainage as an outflow/watercourse
  feature, while the other parent denotes groundwater material. USGS permits drainage
  from groundwater or surface water; that does not settle this exact source intent.
  Later ARMAN samples are contextual, not universal acidity evidence.'
source:
  git_revision: f7727c58b4e3d4883ecaab0dc81441e4a85b716b
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
  - path: curation/causal_graphs/fresh_water.yaml
    sha256: 25e76fb54dd972041827ce7fb2367cf26a91cc275bca3709c3836e61945a7fb7
    role: context
  - path: curation/causal_graphs/liquid_water.yaml
    sha256: 1e6033c72342a74125774b6fc3f7c2438a32046efed57a6e05f90a93fe39c33d
    role: context
  - path: curation/decisions.tsv
    sha256: 2fd5aec7ac1710ede2405849e78dd0423c253d72b43676230f72b9905bae99dd
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 5f7905046872ae48b4b5007b82f3b0b750e695d4f01014875a0474b04403d489
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
    sha256: 99bd93c6173c2ccf7b59645a131ae41c88c45246b45265034a8275053b3745b7
    role: context
  - path: data/habitats/aquatic/groundwater__25377149.yaml
    sha256: 544ade94828e3661804e081b6349061463ec793deaed3776eda4eceb5afa08a8
    role: context
  - path: data/habitats/aquatic/groundwater__585f08d9.yaml
    sha256: c312e4f180875d56e34afecdb41cde835eff185770b508626e81e00b9dabfcb8
    role: context
  - path: data/habitats/aquatic/liquid_water.yaml
    sha256: b91ec338644558b9184fbbb52ace39758ffacaf10f76eb8c52bd854a389c9fd2
    role: context
  - path: data/habitats/aquatic/mine_drainage.yaml
    sha256: e823f6b3886057260d53e2236852b5872ef27e6ec4068dd0eb08d9507901a42a
    role: target
  - path: data/habitats/aquatic/underground_water.yaml
    sha256: ffb74eebd8196044ed52d9866f6e778a87b4fce2bfac5194713d8551150ae3d7
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
    sha256: 105b3c8e10f43ce689b05d3089d3a8be1d713a98dd6806e11be37ebd85b10590
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260926T173701Z-mine_water__20810f85.md
    sha256: 27d5a4bd2403e9d7780d97a382d93441af29afa94d6e27d7c2566aafd648e9b6
    role: context
  - path: reports/yaml_record_review/20261004T190905Z-mine_drainage.md
    sha256: 32e7b1465f38157fa32f7212754eed9c52e310acdd768c938b7e5a0322345633
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
  - path: src/habitatmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/habitatmech/seed.py
    sha256: 4adf105e23d75c3563a516a0c160623d1065df7fcb2f31b7a0a0a8303d0401be
    role: context
targets:
- target_id: habitatmech:GOLD.342d26e2ac
  path: data/habitats/aquatic/mine_drainage.yaml
  label: Mine drainage
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Source-specific identity and lifecycle decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definitions and genus
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Guarded source context-parent exclusions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology labels, definitions and synonyms
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Harmonization and generated record construction
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD source inventory
scope:
  description: Entire exact generated record, all source contributors and asserted
    fields, with bounded source-context assessment.
  selection: 'Next forty records without a completed individual scientific review
    in stable repository-relative path order: microbial_mats__2265bbbd through ocean_trench.
    Full individual observations, not a category-wide pass. Prior coverage counts
    distinct observations, not a clean current-input corpus. Starting distinct-review
    coverage 728/3208 is not clean current-input coverage.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.342d26e2ac
  exclusions:
  - target: Other 3207 current records
    reason: Context reads are not their full scientific review.
checks:
- check_id: C0
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=f7727c58b4e3d4883ecaab0dc81441e4a85b716b
    just validate data/habitats/aquatic/mine_drainage.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T07:23:55.438802Z to 2026-10-12T07:23:58.165721Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C1
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=f7727c58b4e3d4883ecaab0dc81441e4a85b716b
    just validate-strict data/habitats/aquatic/microbial_mats__2265bbbd.yaml data/habitats/aquatic/microbial_mats__42c901d2.yaml
    data/habitats/aquatic/microbial_mats__522cc2c0.yaml data/habitats/aquatic/microbial_mats__54849ba0.yaml
    data/habitats/aquatic/microbial_mats__59ad9a00.yaml data/habitats/aquatic/microbial_mats__66f27e00.yaml
    data/habitats/aquatic/microbial_mats__74823fe8.yaml data/habitats/aquatic/microbial_mats__7a576572.yaml
    data/habitats/aquatic/microbial_mats__884c9c12.yaml data/habitats/aquatic/microbial_mats__8cd68d16.yaml
    data/habitats/aquatic/microbial_mats__91e1bc3c.yaml data/habitats/aquatic/microbial_mats__a2a31086.yaml
    data/habitats/aquatic/microbial_mats__a56a2e1b.yaml data/habitats/aquatic/microbial_mats__aaf3c430.yaml
    data/habitats/aquatic/microbial_mats__aba42aab.yaml data/habitats/aquatic/microbial_mats__c3f0268a.yaml
    data/habitats/aquatic/microbial_mats__cfca43d0.yaml data/habitats/aquatic/microbial_mats__d16dafc1.yaml
    data/habitats/aquatic/microbialites.yaml data/habitats/aquatic/microbialites__2dd0659e.yaml
    data/habitats/aquatic/microbialites__82d49810.yaml data/habitats/aquatic/microbialites__a38bc21d.yaml
    data/habitats/aquatic/microbialites__b8560cfd.yaml data/habitats/aquatic/mine__d2db7642.yaml
    data/habitats/aquatic/mine_drainage.yaml data/habitats/aquatic/mine_pit_lake.yaml
    data/habitats/aquatic/mine_pit_pond.yaml data/habitats/aquatic/mine_water__20810f85.yaml
    data/habitats/aquatic/mixolimnion_top_layer.yaml data/habitats/aquatic/monimolimnion_bottom_layer.yaml
    data/habitats/aquatic/mud_volcano__980e0b1f.yaml data/habitats/aquatic/near_boiling_90c.yaml
    data/habitats/aquatic/near_boiling_90c__f7b76591.yaml data/habitats/aquatic/neritic_epipelagic_zone_biome.yaml
    data/habitats/aquatic/neutral.yaml data/habitats/aquatic/neutral__819b9d53.yaml
    data/habitats/aquatic/non_marine_saline_and_alkaline__0e812745.yaml data/habitats/aquatic/ocean.yaml
    data/habitats/aquatic/ocean_biome.yaml data/habitats/aquatic/ocean_trench.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T07:24:43.138183Z to 2026-10-12T07:24:53.380336Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C2
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=f7727c58b4e3d4883ecaab0dc81441e4a85b716b
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T07:24:53.381554Z to 2026-10-12T07:25:17.592324Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C3
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=f7727c58b4e3d4883ecaab0dc81441e4a85b716b
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T07:25:17.593658Z to 2026-10-12T07:26:19.939303Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C4
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=f7727c58b4e3d4883ecaab0dc81441e4a85b716b
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T07:26:19.940781Z to 2026-10-12T07:26:29.078055Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C5
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=f7727c58b4e3d4883ecaab0dc81441e4a85b716b
    just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T07:26:29.079194Z to 2026-10-12T07:26:34.354132Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C6
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=f7727c58b4e3d4883ecaab0dc81441e4a85b716b
    just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T07:26:34.355124Z to 2026-10-12T07:26:54.824749Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C7
  name: Native gate on captured inputs
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=f7727c58b4e3d4883ecaab0dc81441e4a85b716b
    just provenance-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T07:26:54.826025Z to 2026-10-12T07:26:55.497046Z.
    Native command scope retained.
  evidence_ids:
  - R
  - RULES
- check_id: C8
  name: Exact-base CI authoritative QC
  required: true
  status: passed
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  command: gh run view 38215367859 --repo CultureBotAI/HabitatMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Actual success 2026-10-12T07:23:23.595254Z to 2026-10-12T07:23:25.901988Z.
    All three required merge-group workflows passed at the exact captured base; authoritative
    QC passed 946 tests with 3 skipped. Newly saved review bundles require their own
    integrity check. These newly saved review bundles were not part of that earlier
    exact-base CI run.
  evidence_ids:
  - R
  - RULES
- check_id: REPRO
  name: Full target reconstruction
  required: false
  status: passed
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  command: uv run python /private/tmp/habitatmech-review-bd-evidence.py
  exit_code: 0
  summary: All forty complete documents matched; captured input hashes rechecked before
    authoring.
  evidence_ids:
  - RAW
  - CODE
- check_id: ORIGINAL
  name: Original occurrence inputs
  required: false
  status: unavailable
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  summary: Bounded ignored-inclusive searches did not recover complete original inputs.
    Later GOLD context is not original assertion membership.
  evidence_ids:
  - SEARCH
- check_id: IMODULON
  name: Expression-adapter applicability
  required: false
  status: not_applicable
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  summary: No claim-specific gene, regulator or expression-module assertion warrants
    an adapter query.
  evidence_ids:
  - R
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/aquatic/mine_drainage.yaml
  summary: 'Groundwater/Mine drainage: ENVO treats drainage as an outflow/watercourse
    feature, while the other parent denotes groundwater material. USGS permits drainage
    from groundwater or surface water; that does not settle this exact source intent.
    Later ARMAN samples are contextual, not universal acidity evidence.'
  accessed_at: '2026-10-12T07:33:33.789461Z'
  support: supports
  locator: Entire captured YAML read, including all taxa, parameters, graphs and generated
    history
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml
  summary: Applied exact identity, strict-genus, MIxS roles, source-unit/score and
    ITEM lifecycle contracts; graph node types retain their biological definitions.
  accessed_at: '2026-10-12T07:33:33.789461Z'
  support: supports
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0",
    "canonical_path": "Environmental > Aquatic > Freshwater > Groundwater > Mine drainage",
    "depth": "5", "ecosystem": "Environmental", "ecosystem_category": "Aquatic", "ecosystem_subtype":
    "Groundwater", "ecosystem_type": "Freshwater", "gold_node_count": "1", "gold_node_ids":
    "gold.ecosystem:4170", "leaf_label": "Mine drainage", "organism_count": "0", "specific_ecosystem":
    "Mine drainage", "study_count": "0", "total_assertions": "0"}, "logical_row":
    1469}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "9",
    "canonical_path": "Environmental > Aquatic > Freshwater > Groundwater > Mine drainage",
    "ecosystem_path_id": "4170"}, "logical_row": 647}], "data/raw/gold_path_triads.tsv":
    [{"data": {"canonical_path": "Environmental > Aquatic > Freshwater > Groundwater
    > Mine drainage", "distinct_terms": "1", "samples": "9", "slot": "broad", "studies":
    "3", "studies_agreeing": "3", "top_label": "aquatic biome", "top_share": "1.00",
    "top_term": "ENVO:00002030"}, "logical_row": 287}, {"data": {"canonical_path":
    "Environmental > Aquatic > Freshwater > Groundwater > Mine drainage", "distinct_terms":
    "2", "samples": "9", "slot": "local", "studies": "3", "studies_agreeing": "2",
    "top_label": "acid mine drainage", "top_share": "0.78", "top_term": "ENVO:00001997"},
    "logical_row": 288}, {"data": {"canonical_path": "Environmental > Aquatic > Freshwater
    > Groundwater > Mine drainage", "distinct_terms": "2", "samples": "9", "slot":
    "medium", "studies": "3", "studies_agreeing": "2", "top_label": "acidic water",
    "top_share": "0.78", "top_term": "ENVO:01000358"}, "logical_row": 289}]}'
  accessed_at: '2026-10-12T07:33:33.789461Z'
  support: supports
  locator: Exact logical TSV rows, header=row1; filtered by current source IDs and
    exact paths, not legacy issue line numbers
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 0, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": ["ENVO:00001996"], "extra_xrefs": [],
    "grounding_status": "NARROW", "identifier": "habitatmech:GOLD.342d26e2ac", "mapping_predicate":
    "skos:narrowMatch", "reviewed": false, "route": "gold_narrower_than_leaf_match"},
    "automatic": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": ["ENVO:00001996"], "extra_xrefs": [], "grounding_status": "NARROW",
    "identifier": "habitatmech:GOLD.342d26e2ac", "mapping_predicate": "skos:narrowMatch",
    "reviewed": false, "route": "gold_narrower_than_leaf_match"}, "minted": "habitatmech:GOLD.342d26e2ac",
    "source": "GOLD", "source_id": "gold.ecosystem:4170"}], "source_concepts": 1}'
  accessed_at: '2026-10-12T07:33:33.789461Z'
  support: supports
  locator: Executed complete-document reconstruction; all 40 matched; routes distinguish
    source mints and generated identity
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl
  summary: '{"ENVO:00001996": {"definitions": ["The outflow of water from a mine."],
    "deprecated": [], "equivalents": [], "labels": ["mine drainage"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00000029",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/BFO_0000050"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_00000076"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [],
    "hasNarrowSynonym": [], "hasRelatedSynonym": ["acid and metalliferous drainage",
    "acid rock drainage"]}}, "ENVO:00002006": {"definitions": ["An environmental material
    primarily composed of dihydrogen oxide in its liquid form."], "deprecated": [],
    "equivalents": [], "labels": ["liquid water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_01000815",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0002473"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_15377"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": ["water"], "hasExactSynonym":
    [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002011": {"definitions":
    ["Water which has a low concentration of dissolved solutes, particularly that
    of sodium chloride."], "deprecated": [], "equivalents": [], "labels": ["fresh
    water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006"], "replacements":
    [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["freshwater"], "hasNarrowSynonym":
    [], "hasRelatedSynonym": ["sweet water"]}}, "ENVO:00005792": {"definitions": ["Water
    which has physicochemical properties determined by processes which occur beneath
    the planetary crust."], "deprecated": [], "equivalents": [], "labels": ["underground
    water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0001025"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_01000941"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym":
    ["subterranean water"]}}, "ENVO:01001004": {"definitions": ["Underground water
    which is located in pore spaces found in rock or unconsolidated deposits such
    as soil, clay, or gravel."], "deprecated": [], "equivalents": [], "labels": ["groundwater"],
    "parents": ["http://purl.obolibrary.org/obo/ENVO_00005792", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty":
    ["http://purl.obolibrary.org/obo/RO_0001025"], "http://www.w3.org/2002/07/owl#someValuesFrom":
    ["http://purl.obolibrary.org/obo/ENVO_00012408"]}], "replacements": [], "synonyms":
    {"hasBroadSynonym": [], "hasExactSynonym": ["ground water"], "hasNarrowSynonym":
    [], "hasRelatedSynonym": []}}}'
  accessed_at: '2026-10-12T07:20:50.397857Z'
  support: supports
  locator: Official OWL retrieved 12-Oct; labels, definitions, typed synonyms, named
    parents and restrictions; no snapshot refresh
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats/aquatic/groundwater__25377149.yaml; data/habitats/aquatic/groundwater__585f08d9.yaml;
    data/habitats/aquatic/underground_water.yaml; data/habitats/aquatic/liquid_water.yaml;
    data/habitats/aquatic/fresh_water.yaml
  summary: '{"ENVO:00002006": {"definition": "An environmental material primarily
    composed of dihydrogen oxide in its liquid form.", "grounding_status": "EXACT",
    "label": "liquid water", "parent_habitats": ["ENVO:01000815"]}, "ENVO:00002011":
    {"definition": "Water which has a low concentration of dissolved solutes, particularly
    that of sodium chloride.", "grounding_status": "EXACT", "label": "fresh water",
    "parent_habitats": ["ENVO:00002006"]}, "ENVO:00005792": {"definition": "Water
    which has physicochemical properties determined by processes which occur beneath
    the planetary crust.", "grounding_status": "EXACT", "label": "underground water",
    "parent_habitats": ["ENVO:00002006"]}, "ENVO:01001004": {"definition": "Underground
    water which is located in pore spaces found in rock or unconsolidated deposits
    such as soil, clay, or gravel.", "grounding_status": "EXACT", "label": "groundwater",
    "parent_habitats": ["ENVO:00005792"]}, "habitatmech:GOLD.7f8e268653": {"definition":
    null, "grounding_status": "NARROW", "label": "Groundwater", "parent_habitats":
    ["ENVO:00002011", "ENVO:01001004"]}}'
  accessed_at: '2026-10-12T07:33:33.789461Z'
  support: supports
  locator: Ancestor context adds no full-record coverage
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  summary: 'Exact positional census counts={"Biosample": 9, "Organism": 0, "SequencingProject":
    10}; individually inspected descriptions={"Biosample": [{"data": {"BIOSAMPLE GOLD
    ID": "Gb0051935", "BIOSAMPLE NAME": "Acid Mine Drainage (ARMAN) microbial communities
    from Richmond mine, Iron Mountain, CA, USA - Site 1", "BIOSAMPLE NCBI TAX NAME":
    "mine drainage metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Richmond mine,
    Iron Mountain, California, USA"}, "row": 757}, {"data": {"BIOSAMPLE GOLD ID":
    "Gb0051936", "BIOSAMPLE NAME": "Acid Mine Drainage (ARMAN) microbial communities
    from Richmond mine, Iron Mountain, CA, USA -UBA Waterfall", "BIOSAMPLE NCBI TAX
    NAME": "mine drainage metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Richmond
    mine, Iron Mountain, California, USA"}, "row": 758}, {"data": {"BIOSAMPLE GOLD
    ID": "Gb0051937", "BIOSAMPLE NAME": "Acid Mine Drainage (ARMAN) microbial communities
    from Richmond mine, Iron Mountain, CA, USA", "BIOSAMPLE NCBI TAX NAME": "mine
    drainage metagenome", "BIOSAMPLE SAMPLE COLLECTION SITE": "Richmond mine, Iron
    Mountain, California, USA"}, "row": 759}], "Organism": []}. These later examples
    may include mixed sample/host/enrichment contexts; they do not reconstruct original
    assertion membership. Remaining members and study joins were indexed, not individually
    assessed.'
  accessed_at: '2026-10-11T13:21:51.155056Z'
  support: supports
  locator: Five-position ecosystem paths preserved; contacts excluded; first 3 BioSample
    and Organism descriptions per target
  snapshot_sha256: b222fa9df89ffbd1a30897a1e7302da363c57b463d9948ecc9bfcb9304b4a96f
- evidence_id: CLASS
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  summary: '[{"row": 583, "slug": "mine_drainage", "path": "Environmental > Aquatic
    > Freshwater > Groundwater > Mine drainage", "values": ["4170", "Environmental",
    "Aquatic", "Freshwater", "Groundwater", "Mine drainage"]}]'
  accessed_at: '2026-10-12T07:20:53.124942Z'
  support: supports
  locator: Later official classification; Exact later classification tuples compared;
    missing tuples do not establish nonexistence
  snapshot_sha256: 78ed6ce1c3799a2d6ef2d17e4a9eeee5da48eef78df0b71079c0f942555e5e7d
- evidence_id: SEARCH
  kind: search
  reference: curation; history; research; reports; reviews; data/raw; data/habitats;
    conf
  summary: 'Identifier, label, slug and exact-path searches included hidden/ignored
    files in these roots. No earlier structured target observation was found. Legacy
    reports exist and are not silently retired. Bounded original-source search={"configured_root":
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists":
    true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv",
    "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv",
    "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv",
    "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv",
    "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv",
    "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv",
    "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv",
    "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv",
    "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv",
    "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv",
    "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}],
    "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"],
    "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command":
    ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "exit_code": 0, "matches": [], "stderr": ""}]}'
  accessed_at: '2026-10-12T07:33:33.789461Z'
  support: supports
  locator: Search boundaries are explicit; no global absence claim
  search_scope: 'Identifier, label, slug and exact-path searches included hidden/ignored
    files in these roots. No earlier structured target observation was found. Legacy
    reports exist and are not silently retired. Bounded original-source search={"configured_root":
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists":
    true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv",
    "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv",
    "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv",
    "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv",
    "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv",
    "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv",
    "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv",
    "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv",
    "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv",
    "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"},
    {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv",
    "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}],
    "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"],
    "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore",
    "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command":
    ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"],
    "exit_code": 0, "matches": [], "stderr": ""}]}'
- evidence_id: ISSUES
  kind: database
  reference: https://github.com/CultureBotAI/HabitatMech/issues
  summary: 'All-state971-issue title/body inventory and relevant bodies inspected.
    Issues are historical leads, not primary support. Comments were not exhaustively
    crawled; issue #1397 witness comments were additionally checked.'
  accessed_at: '2026-10-12T07:33:33.789461Z'
  support: supports
  locator: GitHub CLI inventory retrieved 12-Oct
- evidence_id: DRAIN
  kind: authority
  reference: https://www.usgs.gov/mission-areas/water-resources/science/mine-drainage
  summary: USGS distinguishes waters draining active or abandoned mines, including
    surface and groundwater. Generic mine water is not necessarily flowing out; drainage
    need not universally be acidic.
  accessed_at: '2026-10-12T07:29:12.994826Z'
  support: supports
  locator: Background and How does mine drainage occur
  snapshot_sha256: 8ff6fc0da73c6dac0e16644a8a46ad2df1e8d22d458ffe111d2393b0c5cb45aa
assessments:
- assessment_id: IDENTITY
  area: identity
  topic: Exact identity and source scope
  outcome: concern
  summary: 'Groundwater/Mine drainage: ENVO treats drainage as an outflow/watercourse
    feature, while the other parent denotes groundwater material. USGS permits drainage
    from groundwater or surface water; that does not settle this exact source intent.
    Later ARMAN samples are contextual, not universal acidity evidence.'
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
- assessment_id: HIERARCHY
  area: grounding
  topic: All strict-parent contributors and mapping endpoints
  outcome: concern
  summary: 'Groundwater/Mine drainage: ENVO treats drainage as an outflow/watercourse
    feature, while the other parent denotes groundwater material. USGS permits drainage
    from groundwater or surface water; that does not settle this exact source intent.
    Later ARMAN samples are contextual, not universal acidity evidence. Actual ontology,
    GOLD context, automatic leaf and curated-genus contributions were distinguished.'
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  evidence_ids:
  - R
  - RAW
  - CODE
  - ONT
  - PARENT
- assessment_id: PROVENANCE
  area: provenance
  topic: Source units and ITEM lifecycle
  outcome: supported
  summary: Complete reconstruction preserves 1 source concepts and 0 ITEM-reviewed
    contributors. Counts with distinct units are not added; seeded and reviewed statuses
    describe native provenance, not automatic scientific correctness.
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  evidence_ids:
  - R
  - RAW
  - CODE
  - RULES
- assessment_id: COMPLETENESS
  area: completeness
  topic: Optional fields and mechanism applicability
  outcome: supported
  summary: No causal graph, gene/regulator or expression-module claim is asserted
    in the complete target. Optional empty slots alone are not defects. Bounded supporting-file
    search included ignored files; no expression-adapter query was applicable.
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  evidence_ids:
  - R
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: habitatmech-gold.342d26e2ac-mapping-endpoint
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Narrow mapping uses an undeclared ontology comparison endpoint
  description: A source-specific mint is retained and the generic ontology class is
    a parent. narrowMatch compares to that parent, but SourceAttestation describes
    comparison to the generated record. This is an endpoint contract ambiguity, not
    proof of formal SKOS self-inconsistency.
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  field_paths:
  - source_attestations
  - grounding_status
  evidence_ids:
  - R
  - RAW
  - CODE
  - RULES
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Resolver endpoints
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Attestation comparison contract
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material identity, strict-hierarchy, evidence or representation
    defect.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
- finding_id: F2
  issue_key: habitatmech-gold.342d26e2ac-source-entity-scope
  category: scope
  severity: major
  status: open
  certainty: provisional
  title: Resolve excavation or drainage feature versus sampled-water identity
  description: 'Groundwater/Mine drainage: ENVO treats drainage as an outflow/watercourse
    feature, while the other parent denotes groundwater material. USGS permits drainage
    from groundwater or surface water; that does not settle this exact source intent.
    Later ARMAN samples are contextual, not universal acidity evidence.'
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  field_paths:
  - parent_habitats
  - grounding_status
  evidence_ids:
  - R
  - RAW
  - PARENT
  - BULK
  - DRAIN
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Exact-source entity assessment
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: Material identity, strict-hierarchy, evidence or representation
    defect.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1408
actions:
- action_id: A1
  description: 'Resolve shared issue #1398 with explicit subject/predicate/object
    semantics and SSSOM/KGX consumer tests; retain source-specific identities. Reversing
    the predicate alone cannot supply a missing endpoint.'
  finding_ids:
  - F1
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Resolver endpoints
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Attestation comparison contract
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained owners after source-level assessment; retain independent
    true parents, source identity/count/unit provenance and lifecycle unless a separately
    justified change requires otherwise.
  - Append required current history, add focused regressions, inspect a seed canary
    and regenerate affected products without hand-editing records or pages.
  - Pass schema, strict, label, provenance, corpus reproduction, causal/history and
    full QC gates; save a linked successor for any finding disposition.
- action_id: A2
  description: Assess original membership and source intent before choosing feature
    versus sampled-water genera. Do not simply delete one parent or equate all mine
    waters with acid mine drainage.
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.342d26e2ac
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Exact-source entity assessment
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Change only maintained owners after source-level assessment; retain independent
    true parents, source identity/count/unit provenance and lifecycle unless a separately
    justified change requires otherwise.
  - Append required current history, add focused regressions, inspect a seed canary
    and regenerate affected products without hand-editing records or pages.
  - Pass schema, strict, label, provenance, corpus reproduction, causal/history and
    full QC gates; save a linked successor for any finding disposition.
limitations:
- This completed bounded review is not a clean-record verdict or exhaustive validation
  of original source occurrences.
- Only the first three exact-path BioSample and Organism descriptions per target/sheet
  were individually interpreted; remaining members and study joins were indexed only.
- Later GOLD export/classification does not reconstruct original August membership;
  no source snapshot was refreshed.
- Same-agent assessment, not independent approval. Initial review capture precedes
  separately authorized curation.
- 'SSSOM/KGX conformance to current kg-microbe modeling was not audited; issue #1398
  remains unresolved.'
- Current label validation has no-adapter skips and accepted exceptions; broad gates
  do not expand scientific coverage.
notes:
- Initial observation captured before separately authorized curation/publication;
  no paid research.
- No earlier structured target observation found; legacy reports are historical and
  are not automatically superseded.
tags:
- habitatmech
- aquatic
- record-review
- scientific-review
```
