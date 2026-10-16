# Remediation review: cloaca

- Review: 20261016T042219Z-cloaca-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T04:15:16Z
- Finished UTC: 2026-10-16T04:22:19Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Removed the reviewed GOLD context-parent contribution(s). Native identity and status are unchanged. Source observations and independent valid genera are preserved. Unresolved predecessor findings remain explicitly open.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding after bounded input repair.

Selection: One of ten repaired records from the 24-record clasper-through-colostrum cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ce5a5b09e405e16ac1870472f424bbcdb4866c33.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.037d4112ea | data/habitats/host_associated/cloaca.yaml | generated | Cloaca |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/cloaca.yaml | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:04:31Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cloaca.yaml |
| just validate-strict data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:04:50Z. uv run python scripts/validate_strict.py data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:04:57Z. No issues found<br>834 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:04:57Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:05:10Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:05:13Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:05:27Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:06:09Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| uv run pytest -q tests/test_claw_colon_review_repairs.py tests/test_record_annotation_corrections.py --no-cov | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:06:15Z. ..............................                                           [100%]<br>30 passed in 5.29s |
| uv run ruff check . | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:06:16Z. All checks passed! |
| git diff --check | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:06:16Z.  |
| just term-requests | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:11:19Z. wrote curation/term_requests/envo_robot_template.tsv: 110 ENVO terms from 110 source records<br><br>20 examined-ungrounded record(s) still have no request written. Top by volume:<br>      438  Medical-environment                habitatmech:BACDIVE.5e52ea1bba<br>      228  Fruit-Seed                         habitatmech:BACDIVE.ba016fe448<br>       35  Egg                                habitatmech:BACDIVE.d48ce9485d<br>        5  Caeca: Bacteriome                  habitatmech:GOLD.2d506b9526<br>        3  Abdomen                            habitatmech:GOLD.c6b0b54290<br>        1  Thalassic                          habitatmech:GOLD.3fece6dbf7<br>        0  Subtidal zone sediment             habitatmech:GOLD.785879d721<br>        0  Subterranean lake                  habitatmech:GOLD.937bf682c4<br>        0  Subterranean lake                  habitatmech:GOLD.51eb0120ab<br>        0  Colon                              habitatmech:GOLD.c484d9a195<br><br>covered 105842 upstream assertions; 710 still unrequested across 20 record(s); 15 examined and deliberately not asked for<br><br>&#96;created by&#96; is empty: it wants pipe-delimited full ORCID IRIs and this script cannot know them.<br> uv run python scripts/build_term_requests.py |
| just docs-stats | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:11:36Z. updated README corpus statistics<br> uv run python scripts/check_docs.py --write |
| just render | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:12:22Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 130 term requests -&gt; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages<br> uv run python scripts/render_pages.py |
| just render-check | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:12:53Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 130 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpv8mv60qy/site<br>pages/ is in step with the corpus<br> uv run python scripts/render_pages.py --check |
| just redirects-check | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:14:33Z. RETIRED.tsv is current (259 redirects)<br> uv run python scripts/build_redirects.py --check |
| uv run ruff check . | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:14:34Z. All checks passed! |
| git diff --check | passed | True | habitatmech:GOLD.037d4112ea | Finished 2026-10-16T04:14:34Z.  |
| Exact-revision hosted review contract | passed | True | habitatmech:GOLD.037d4112ea | Successful archive-contract step verified 2026-10-16T04:21:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38849674101 |
| Standalone citation validation applicability | not_applicable | False | habitatmech:GOLD.037d4112ea | No standalone citation checker is documented for these evidence-free generated targets. Stable references were checked with native gates and current authorities; causal validation ran globally. |

## Scientific And Domain Assessments

### Bounded repair and exact preservation

consistency: supported. Targets: habitatmech:GOLD.037d4112ea.

Removed the reviewed GOLD context-parent contribution(s). Native identity and status are unchanged. Source observations and independent valid genera are preserved. Unresolved predecessor findings remain explicitly open.

### Current habitat identity and hierarchy

identity: supported. Targets: habitatmech:GOLD.037d4112ea.

habitatmech:GOLD.037d4112ea: Cloaca; NARROW/SEEDED; parents ["UBERON:0000162"]. No replacement identity or optional definition fabricated.

### Source units and observation preservation

quantity: supported. Targets: habitatmech:GOLD.037d4112ea.

[{"source": "GOLD", "source_id": "gold.ecosystem:6895", "source_label": "Cloaca", "source_path": "Host-associated &gt; Birds &gt; Digestive system &gt; Large intestine &gt; Cloaca", "mapping_predicate": "skos:narrowMatch", "assertion_count": 309, "assertion_unit": "ORGANISM"}]. Source counts/units, taxa, ranks, scores and parameters are unchanged; they are not prevalence.

### Every predecessor finding reconciled

representation: concern. Targets: habitatmech:GOLD.037d4112ea.

Exact issue keys and predecessor references retained; scoped synonym correction and removal of one invalid insect match do not solve global #1249 or #1398.

### Lifecycle and evidence boundaries

completeness: supported. Targets: habitatmech:GOLD.037d4112ea.

No optional mechanism, parameter, characteristic-presence or biological-absence claim added. Native status changes only for the explicit insect ITEM decision. Other reviewed targets retain their prior status.

## Findings

### F1: Source context is not a strictly broader class

major / resolved / confirmed; issue key: cloaca-context-parent.

Removed only the exact guarded GOLD context-parent contributions habitatmech:GOLD.b091b80314. Source paths and observations remain; independent valid genera are preserved.

Disposition: Removed only the exact guarded GOLD context-parent contributions habitatmech:GOLD.b091b80314. Source paths and observations remain; independent valid genera are preserved.

### F2: Mapping uses an undeclared ontology-parent endpoint

major / open / confirmed; issue key: cloaca-mapping-endpoint-contract.

Retained NARROW mapping still compares the source mint with an undeclared ontology-parent endpoint. Removing a context-only parent does not reconcile that shared contract.

Disposition: Retained NARROW mapping still compares the source mint with an undeclared ontology-parent endpoint. Removing a context-only parent does not reconcile that shared contract.

## Recommended Actions And Acceptance Checks

### ACT2

Retained NARROW mapping still compares the source mint with an undeclared ontology-parent endpoint. Removing a context-only parent does not reconcile that shared contract. Proposed remaining work only; this successor does not perform further curation.

- Regress the exact target claim and preserve valid genera, identifiers, source counts/units and taxon associations. Recover original evidence before deleting a provisional pair; do not decrement frozen totals by hand.
- Record authorized curation history; require schema, strict, provenance, history, label, corpus, site and full QC gates.
- Save an immutable successor with the same issue key and exact predecessor finding identity.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX13 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059/graph; UBERON_0000059-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000059", "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059", "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059", "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059", "target": "http://purl.obolibrary.org/obo/UBERON_0000160", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059", "target": "http://purl.obolibrary.org/obo/UBERON_0004907", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX14 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059; UBERON_0000059.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:0000059", "label": "large intestine", "is_obsolete": false, "description": ["A subdivision of the digestive tract that connects the small intestine to the cloaca or anus. Lacks or has few villi[Kardong]."], "obo_synonym": [{"name": "intestinum crassum", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "BTO", "id": "0000706", "description": null, "url": "http://purl.obolibrary.org/obo/BTO_0000706"}]}], "annotation": {"database_cross_reference": ["AAO:0010396", "BTO:0000706", "CALOHA:TS-1306", "EFO:0000840", "EMAPA:19252", "EV:0100077", "FMA:7201", "GAID:306", "MA:0000333", "MESH:D007420", "MIAA:0000046", "NCIT:C12379", "SCTID:181254001", "VHOG:0000054", "Wikipedia:Large_intestine_(anatomy)", "XAO:0000131", "galen:LargeIntestine", "UMLS:C0021851"], "depiction": ["https://cdn.humanatlas.io/digital-objects/ref-organ/large-intestine-female/v1.3/assets/3d-sbu-f-large-intestine.glb", "https://cdn.humanatlas.io/digital-objects/ref-organ/large-intestine-male/v1.3/assets/3d-sbu-m-large-intestine.glb"], "homology_notes": ["Intestinal surface area also is increased in amphibians and reptiles by internal folds and occasionally by a few villi. The intestine can be divided into a small intestine and a slightly wider large intestine.[well established][VHOG]"], "id": ["UBERON:0000059"]}} |
| EX15 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000162/graph; UBERON_0000162-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000162", "target": "http://purl.obolibrary.org/obo/UBERON_0013522", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000162", "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000162", "target": "http://purl.obolibrary.org/obo/UBERON_0001555", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000162", "target": "http://purl.obolibrary.org/obo/UBERON_0004122", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX16 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000162; UBERON_0000162.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:0000162", "label": "cloaca", "is_obsolete": false, "description": ["Common chamber into which the intestines and excretory system opens. Arises during development in all vertebrates, but in many it becomes subdivided, lost or incorporated into other structures."], "obo_synonym": [{"name": "cloacal chamber", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "AAO", "id": "0000095", "description": null, "url": "http://purl.obolibrary.org/obo/AAO_0000095"}]}, {"name": "vent", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "XAO", "id": "0000244", "description": null, "url": "http://purl.obolibrary.org/obo/XAO_0000244"}]}], "annotation": {"database_cross_reference": ["AAO:0000095", "GAID:1206", "MESH:D002988", "NCIT:C34127", "SCTID:362857006", "SCTID:370631000", "VHOG:0001186", "Wikipedia:Cloaca", "XAO:0000244", "ZFA:0005781", "UMLS:C0008987"], "development_notes": ["hindgut endoderm and proctodeal ectoderm."], "editor note": ["adding df link to embryonic cloaca leads to a cycle in uberon-simple, as cloaca is a suberclass of embryonic cloaca"], "external_definition": ["A common passage for fecal, urinary, and reproductive discharge in most lower vertebrates as well as the terminal end of the hindgut before division into rectum, bladder, and genital primordia in mammalian embryos. [TFD][VHOG]", "Anatomical structure which is the common receptacle for the alimentary canal, Wolffian ducts, oviducts, and the bladder.[AAO]"], "has_relational_adjective": ["cloacal"], "homology_notes": ["A cloaca is apparently a primitive vertebrate feature because it occurs in most primitive gnathostomes and persists in the embryos of almost all vertebrates.[well established][VHOG]"], "id": ["UBERON:0000162"], "present in taxon": ["http://purl.obolibrary.org/obo/NCBITaxon_9369"], "taxon_notes": ["Human beings only have an embryonic cloaca, which is split up into separate tracts during the development of the urinary and reproductive organs"]}} |
| EAFTER | data/habitats/host_associated/cloaca.yaml; Entire regenerated target YAML | supports | {"identifier": "habitatmech:GOLD.037d4112ea", "label": "Cloaca", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats": ["UBERON:0000162"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6895", "source_label": "Cloaca", "source_path": "Host-associated &gt; Birds &gt; Digestive system &gt; Large intestine &gt; Cloaca", "mapping_predicate": "skos:narrowMatch", "assertion_count": 309, "assertion_unit": "ORGANISM"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp": "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.b091b80314 for habitatmech:GOLD.037d4112ea (Host-associated &gt; Birds &gt; Digestive system &gt; Large intestine &gt; Cloaca). Review https://github.com/CultureBotAI/HabitatMech/issues/2221 : The avian cloacal chamber is not a type of whole large intestine. Retain the generic cloaca genus, distinct source mint, all counts and native status. Exclude only the exact source-context parent; shared mapping endpoints remain unresolved."}]} |
| EPREV | reviews/structured/20261016T035435Z-cloaca-record/review.yaml; Immutable baseline, all fields and findings | supports | Every finding is reconciled with its exact issue key and predecessor identity. Earlier scientific evidence remains bounded to its original claim scope. |
| ETEST | tests/test_claw_colon_review_repairs.py; Full-corpus before/after counterfactual | supports | Exactly ten documents change. Eleven guarded parent contributions, two coelom synonym scopes and the insect grounding/status/predicate/history are the only allowed changes. All other records and scientific observations remain identical. |
| ERULE | docs/CURATION.md; Native curation rules | supports | Strictly broader parents, guarded annotation correction, ITEM decisions, source units, host/anatomy and generated ownership. |
| EH40 | history/mappings/claw_colon_review_insect/2026-10-16T040312Z-codex-gpt-5-7927d3.yaml; Complete append-only session event | supports | Authorized curation: agent codex-gpt-5, model gpt-5, tool codex; exact owner and issue recorded. |
| EH41 | history/mappings/claw_colon_review_parents/2026-10-16T040310Z-codex-gpt-5-5f2ade.yaml; Complete append-only session event | supports | Authorized curation: agent codex-gpt-5, model gpt-5, tool codex; exact owner and issue recorded. |
| EH42 | history/mappings/claw_colon_review_synonym/2026-10-16T040311Z-codex-gpt-5-00c6ad.yaml; Complete append-only session event | supports | Authorized curation: agent codex-gpt-5, model gpt-5, tool codex; exact owner and issue recorded. |
| EPARENTS | curation/gold_parent_exclusions.tsv; Exact physical TSV rows | supports | [[4, "habitatmech:GOLD.037d4112ea\tHost-associated &gt; Birds &gt; Digestive system &gt; Large intestine &gt; Cloaca\thabitatmech:GOLD.b091b80314\tcodex-gpt-5\t2026-10-16\tReview https://github.com/CultureBotAI/HabitatMech/issues/2221 : The avian cloacal chamber is not a type of whole large intestine. Retain the generic cloaca genus, distinct source mint, all counts and native status. Exclude only the exact source-context parent; shared mapping endpoints remain unresolved."]] |

## Limits And Additional Notes

- Original specimen-level evidence and every pair-level citation were not exhaustively reconstructed. Source associations, counts, ranks and scores are not prevalence, viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs; target TaxIds were separately resolved with current NCBI.
- iModulonDB is not applicable: no gene, regulator or expression-module claim is asserted. Cited experiments are used only for identity and context, not imported causal mechanisms.
- Same-agent assessment, not independent approval. Final-head and merge-queue checks remain required before publication. The interrupted local archive command is not a passed check; hosted native archive verification is cited instead.
- Full hosted QC was not complete at capture; only its successful archive-contract step is claimed. Native scientific and product checks passed separately.
- Native working_tree capture retained. The off-main input base is preserved by an annotated provenance tag before merge and branch deletion. Generated seeding history is deterministic current-state output; all immutable saved review bundles and history/ session files remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T042219Z-cloaca-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: cloaca'
started_at: '2026-10-16T04:15:16Z'
finished_at: '2026-10-16T04:22:19Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assessed all evidence and target; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: Removed the reviewed GOLD context-parent contribution(s). Native identity
  and status are unchanged. Source observations and independent valid genera are preserved.
  Unresolved predecessor findings remain explicitly open.
source:
  git_revision: ce5a5b09e405e16ac1870472f424bbcdb4866c33
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
    sha256: 5d3af0a0505a61cda5e088e2c4b7922b740b7423fbca957d49aa8261b5584b37
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 29671974bab045cad2620da3ad89d176f8a2f5ca2612ad3c8761d82fd3f1ea81
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: c1207270bb0ae2031e42de6cb8220b20f98886f65e40d48793bfd7e9d757d83a
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: bc7a13d922c179cd9bcd4d37b348bc90a39b08a4dafba7af4ed0039ad99621c3
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: ee559f7b45b4af2d72a078c45d1a3b676785d34305f286e9738f95771dbaccfd
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: 747e6a5612dc0b7ed881b9fb323fd57ab3c75794d9ee5ebb9d59b2be57dbf8cd
    role: context
  - path: data/habitats/host_associated/cloaca.yaml
    sha256: 9e0ddeec08bb05c7432c5d202758cf963e9badf871c6560366b59fc3cf714f25
    role: target
  - path: data/habitats/host_associated/large_intestine__deeaad00.yaml
    sha256: 851eb7ca7fc4cf40d64b53ffd33908b892db4ba5314293e12c33993d071a11c7
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
  - path: history/README.md
    sha256: 819361a711697f96ff9c1aa0b27e94302547970b3b54777d67ec1449db5e543a
    role: context
  - path: history/mappings/claw_colon_review_insect/2026-10-16T040312Z-codex-gpt-5-7927d3.yaml
    sha256: 301fa9177811519acd7a15e95aa3a3157ef17ede6938957966f5c37c7fd01edc
    role: context
  - path: history/mappings/claw_colon_review_parents/2026-10-16T040310Z-codex-gpt-5-5f2ade.yaml
    sha256: 4d5d1c5dc93e58c8505ec4b711d90876e3573c9836fe50d72391546411d0966d
    role: context
  - path: history/mappings/claw_colon_review_synonym/2026-10-16T040311Z-codex-gpt-5-00c6ad.yaml
    sha256: 12401ab3d3fbd750f977169f186d144444e43f9853c6246114e6f7d13aa538e0
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260929T091516Z-cloaca.md
    sha256: bcc6b7bc3eb9963e56a83d9b9173a49b029fc51b81940094c570e75d3d7be6c2
    role: context
  - path: reviews/structured/20261016T035435Z-cloaca-record/review.yaml
    sha256: eafc9d2fb0fec697c2c60adaa526504a46dc4e139d76da5e8abee8b46f5b0864
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
  - path: tests/test_claw_colon_review_repairs.py
    sha256: f4ecc8e694dce8dce5c640654c2ef92d922a2431d1b5f5f1cce82905951931ec
    role: context
targets:
- target_id: habitatmech:GOLD.037d4112ea
  path: data/habitats/host_associated/cloaca.yaml
  label: Cloaca
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
  description: Full current target assessment and explicit disposition of every baseline
    finding after bounded input repair.
  selection: One of ten repaired records from the 24-record clasper-through-colostrum
    cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.037d4112ea
  exclusions:
  - target: Other records and SSSOM/KGX conformance
    reason: Not whole-corpus scientific approval or a shared mapping-contract repair.
checks:
- check_id: C1
  name: just validate data/habitats/host_associated/cloaca.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/cloaca.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:04:31Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cloaca.yaml"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C10
  name: just validate-strict data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml
    data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml
    data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml
    data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml
    data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml
    data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml
    data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml
    data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml
    data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml
    data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml
    data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml
    data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml
    data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml
    data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml
    data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml
    data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml
    data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml
    data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml
    data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml
    data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml
    data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml
    data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml
    data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:04:50Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/clasper.yaml data/habitats/host_associated/claw.yaml\
    \ data/habitats/host_associated/cloaca.yaml data/habitats/host_associated/cloaca__f527d4ff.yaml\
    \ data/habitats/host_associated/cnidarian_associated_environment.yaml data/habitats/host_associated/cob.yaml\
    \ data/habitats/host_associated/cocoon.yaml data/habitats/host_associated/coelom.yaml\
    \ data/habitats/host_associated/coelom__d65ea80b.yaml data/habitats/host_associated/colon.yaml\
    \ data/habitats/host_associated/colon__a0dd5461.yaml data/habitats/host_associated/colon__ff534087.yaml\
    \ data/habitats/host_associated/colon_cancer.yaml data/habitats/host_associated/colon_mucosa.yaml\
    \ data/habitats/host_associated/colon_mucosa__7a8e4588.yaml data/habitats/host_associated/colon_mucosa__b687aead.yaml\
    \ data/habitats/host_associated/colon_mucosa__de31f03f.yaml data/habitats/host_associated/colonic.yaml\
    \ data/habitats/host_associated/colonic_cancer_cell.yaml data/habitats/host_associated/colonic_epithelium.yaml\
    \ data/habitats/host_associated/colonic_mucosa.yaml data/habitats/host_associated/colorectal_polyps.yaml\
    \ data/habitats/host_associated/colorectum.yaml data/habitats/host_associated/colostrum.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C11
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: 'Finished 2026-10-16T04:04:57Z. No issues found

    834 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C12
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:04:57Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C13
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:05:10Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C14
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:05:13Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C15
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:05:27Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C16
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:06:09Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C17
  name: uv run pytest -q tests/test_claw_colon_review_repairs.py tests/test_record_annotation_corrections.py
    --no-cov
  status: passed
  required: true
  command: uv run pytest -q tests/test_claw_colon_review_repairs.py tests/test_record_annotation_corrections.py
    --no-cov
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: 'Finished 2026-10-16T04:06:15Z. ..............................                                           [100%]

    30 passed in 5.29s'
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C18
  name: uv run ruff check .
  status: passed
  required: true
  command: uv run ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: Finished 2026-10-16T04:06:16Z. All checks passed!
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C19
  name: git diff --check
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: 'Finished 2026-10-16T04:06:16Z. '
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C20
  name: just term-requests
  status: passed
  required: true
  command: just term-requests
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:11:19Z. wrote curation/term_requests/envo_robot_template.tsv:\
    \ 110 ENVO terms from 110 source records\n\n20 examined-ungrounded record(s) still\
    \ have no request written. Top by volume:\n      438  Medical-environment    \
    \            habitatmech:BACDIVE.5e52ea1bba\n      228  Fruit-Seed           \
    \              habitatmech:BACDIVE.ba016fe448\n       35  Egg                \
    \                habitatmech:BACDIVE.d48ce9485d\n        5  Caeca: Bacteriome\
    \                  habitatmech:GOLD.2d506b9526\n        3  Abdomen           \
    \                 habitatmech:GOLD.c6b0b54290\n        1  Thalassic          \
    \                habitatmech:GOLD.3fece6dbf7\n        0  Subtidal zone sediment\
    \             habitatmech:GOLD.785879d721\n        0  Subterranean lake      \
    \            habitatmech:GOLD.937bf682c4\n        0  Subterranean lake       \
    \           habitatmech:GOLD.51eb0120ab\n        0  Colon                    \
    \          habitatmech:GOLD.c484d9a195\n\ncovered 105842 upstream assertions;\
    \ 710 still unrequested across 20 record(s); 15 examined and deliberately not\
    \ asked for\n\n`created by` is empty: it wants pipe-delimited full ORCID IRIs\
    \ and this script cannot know them.\n uv run python scripts/build_term_requests.py"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C21
  name: just docs-stats
  status: passed
  required: true
  command: just docs-stats
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:11:36Z. updated README corpus statistics\n uv run\
    \ python scripts/check_docs.py --write"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C22
  name: just render
  status: passed
  required: true
  command: just render
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:12:22Z. rendered 3209 habitat pages, 259 redirect\
    \ stubs, 8 categories, 130 term requests -> /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages\n\
    \ uv run python scripts/render_pages.py"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C23
  name: just render-check
  status: passed
  required: true
  command: just render-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:12:53Z. rendered 3209 habitat pages, 259 redirect\
    \ stubs, 8 categories, 130 term requests -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmpv8mv60qy/site\n\
    pages/ is in step with the corpus\n uv run python scripts/render_pages.py --check"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C24
  name: just redirects-check
  status: passed
  required: true
  command: just redirects-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: "Finished 2026-10-16T04:14:33Z. RETIRED.tsv is current (259 redirects)\n\
    \ uv run python scripts/build_redirects.py --check"
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C25
  name: uv run ruff check .
  status: passed
  required: true
  command: uv run ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: Finished 2026-10-16T04:14:34Z. All checks passed!
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: C26
  name: git diff --check
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: 'Finished 2026-10-16T04:14:34Z. '
  scope_note: Individual schema; strict covers 24 targets; other native corpus/product
    gates retain their documented scope.
- check_id: CCI
  name: Exact-revision hosted review contract
  status: passed
  required: true
  command: gh run view 38849674101 --repo CultureBotAI/HabitatMech --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: Successful archive-contract step verified 2026-10-16T04:21:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38849674101
  scope_note: Only the completed archive step is asserted by this check; final-head
    and merge-queue QC remain separate publication gates.
- check_id: CREF
  name: Standalone citation validation applicability
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.037d4112ea
  summary: No standalone citation checker is documented for these evidence-free generated
    targets. Stable references were checked with native gates and current authorities;
    causal validation ran globally.
evidence:
- evidence_id: EX13
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059/graph
  locator: UBERON_0000059-graph.json
  accessed_at: '2026-10-16T03:37:11Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000059",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004921", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059",
    "target": "http://purl.obolibrary.org/obo/UBERON_0013765", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000160", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000059",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004907", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 8e11a36702591e8fdbb38beb59c7ca21416d18f4a524ccdd7fb246e8d82d799c
- evidence_id: EX14
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000059
  locator: UBERON_0000059.json
  accessed_at: '2026-10-16T03:37:10Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:0000059", "label": "large intestine", "is_obsolete": false, "description":
    ["A subdivision of the digestive tract that connects the small intestine to the
    cloaca or anus. Lacks or has few villi[Kardong]."], "obo_synonym": [{"name": "intestinum
    crassum", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "BTO",
    "id": "0000706", "description": null, "url": "http://purl.obolibrary.org/obo/BTO_0000706"}]}],
    "annotation": {"database_cross_reference": ["AAO:0010396", "BTO:0000706", "CALOHA:TS-1306",
    "EFO:0000840", "EMAPA:19252", "EV:0100077", "FMA:7201", "GAID:306", "MA:0000333",
    "MESH:D007420", "MIAA:0000046", "NCIT:C12379", "SCTID:181254001", "VHOG:0000054",
    "Wikipedia:Large_intestine_(anatomy)", "XAO:0000131", "galen:LargeIntestine",
    "UMLS:C0021851"], "depiction": ["https://cdn.humanatlas.io/digital-objects/ref-organ/large-intestine-female/v1.3/assets/3d-sbu-f-large-intestine.glb",
    "https://cdn.humanatlas.io/digital-objects/ref-organ/large-intestine-male/v1.3/assets/3d-sbu-m-large-intestine.glb"],
    "homology_notes": ["Intestinal surface area also is increased in amphibians and
    reptiles by internal folds and occasionally by a few villi. The intestine can
    be divided into a small intestine and a slightly wider large intestine.[well established][VHOG]"],
    "id": ["UBERON:0000059"]}}'
  snapshot_sha256: d43e203ec23dc43e60bf4f3eeef91235a695dc997d4784a65919688f223aaba8
- evidence_id: EX15
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000162/graph
  locator: UBERON_0000162-graph.json
  accessed_at: '2026-10-16T03:37:12Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0000162",
    "target": "http://purl.obolibrary.org/obo/UBERON_0013522", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000162",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_7742", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000162",
    "target": "http://purl.obolibrary.org/obo/UBERON_0001555", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0000162",
    "target": "http://purl.obolibrary.org/obo/UBERON_0004122", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: c86624ff309763486ab50e348af0799da5b310b8ee7fd6d85d883452fd9abc91
- evidence_id: EX16
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0000162
  locator: UBERON_0000162.json
  accessed_at: '2026-10-16T03:37:11Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:0000162", "label": "cloaca", "is_obsolete": false, "description": ["Common
    chamber into which the intestines and excretory system opens. Arises during development
    in all vertebrates, but in many it becomes subdivided, lost or incorporated into
    other structures."], "obo_synonym": [{"name": "cloacal chamber", "scope": "hasRelatedSynonym",
    "type": null, "xrefs": [{"database": "AAO", "id": "0000095", "description": null,
    "url": "http://purl.obolibrary.org/obo/AAO_0000095"}]}, {"name": "vent", "scope":
    "hasRelatedSynonym", "type": null, "xrefs": [{"database": "XAO", "id": "0000244",
    "description": null, "url": "http://purl.obolibrary.org/obo/XAO_0000244"}]}],
    "annotation": {"database_cross_reference": ["AAO:0000095", "GAID:1206", "MESH:D002988",
    "NCIT:C34127", "SCTID:362857006", "SCTID:370631000", "VHOG:0001186", "Wikipedia:Cloaca",
    "XAO:0000244", "ZFA:0005781", "UMLS:C0008987"], "development_notes": ["hindgut
    endoderm and proctodeal ectoderm."], "editor note": ["adding df link to embryonic
    cloaca leads to a cycle in uberon-simple, as cloaca is a suberclass of embryonic
    cloaca"], "external_definition": ["A common passage for fecal, urinary, and reproductive
    discharge in most lower vertebrates as well as the terminal end of the hindgut
    before division into rectum, bladder, and genital primordia in mammalian embryos.
    [TFD][VHOG]", "Anatomical structure which is the common receptacle for the alimentary
    canal, Wolffian ducts, oviducts, and the bladder.[AAO]"], "has_relational_adjective":
    ["cloacal"], "homology_notes": ["A cloaca is apparently a primitive vertebrate
    feature because it occurs in most primitive gnathostomes and persists in the embryos
    of almost all vertebrates.[well established][VHOG]"], "id": ["UBERON:0000162"],
    "present in taxon": ["http://purl.obolibrary.org/obo/NCBITaxon_9369"], "taxon_notes":
    ["Human beings only have an embryonic cloaca, which is split up into separate
    tracts during the development of the urinary and reproductive organs"]}}'
  snapshot_sha256: bd5758ca6ec1b0ee490cceaadc9ee0b78f4eeda43fda03c60776f4d614b06d74
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/cloaca.yaml
  locator: Entire regenerated target YAML
  accessed_at: '2026-10-16T04:22:17Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.037d4112ea", "label": "Cloaca", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "NARROW", "mapping_status": "SEEDED", "parent_habitats":
    ["UBERON:0000162"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:6895",
    "source_label": "Cloaca", "source_path": "Host-associated > Birds > Digestive
    system > Large intestine > Cloaca", "mapping_predicate": "skos:narrowMatch", "assertion_count":
    309, "assertion_unit": "ORGANISM"}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z",
    "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded
    from data/raw/ inventories; attested by GOLD. Grounding: NARROW."}, {"timestamp":
    "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.b091b80314
    for habitatmech:GOLD.037d4112ea (Host-associated > Birds > Digestive system >
    Large intestine > Cloaca). Review https://github.com/CultureBotAI/HabitatMech/issues/2221
    : The avian cloacal chamber is not a type of whole large intestine. Retain the
    generic cloaca genus, distinct source mint, all counts and native status. Exclude
    only the exact source-context parent; shared mapping endpoints remain unresolved."}]}'
  snapshot_sha256: 9e0ddeec08bb05c7432c5d202758cf963e9badf871c6560366b59fc3cf714f25
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261016T035435Z-cloaca-record/review.yaml
  locator: Immutable baseline, all fields and findings
  accessed_at: '2026-10-16T04:22:17Z'
  support: supports
  summary: Every finding is reconciled with its exact issue key and predecessor identity.
    Earlier scientific evidence remains bounded to its original claim scope.
  snapshot_sha256: eafc9d2fb0fec697c2c60adaa526504a46dc4e139d76da5e8abee8b46f5b0864
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_claw_colon_review_repairs.py
  locator: Full-corpus before/after counterfactual
  accessed_at: '2026-10-16T04:22:17Z'
  support: supports
  summary: Exactly ten documents change. Eleven guarded parent contributions, two
    coelom synonym scopes and the insect grounding/status/predicate/history are the
    only allowed changes. All other records and scientific observations remain identical.
  snapshot_sha256: f4ecc8e694dce8dce5c640654c2ef92d922a2431d1b5f5f1cce82905951931ec
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Native curation rules
  accessed_at: '2026-10-16T04:22:17Z'
  support: supports
  summary: Strictly broader parents, guarded annotation correction, ITEM decisions,
    source units, host/anatomy and generated ownership.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EH40
  kind: record_content
  reference: history/mappings/claw_colon_review_insect/2026-10-16T040312Z-codex-gpt-5-7927d3.yaml
  locator: Complete append-only session event
  accessed_at: '2026-10-16T04:22:17Z'
  support: supports
  summary: 'Authorized curation: agent codex-gpt-5, model gpt-5, tool codex; exact
    owner and issue recorded.'
  snapshot_sha256: 301fa9177811519acd7a15e95aa3a3157ef17ede6938957966f5c37c7fd01edc
- evidence_id: EH41
  kind: record_content
  reference: history/mappings/claw_colon_review_parents/2026-10-16T040310Z-codex-gpt-5-5f2ade.yaml
  locator: Complete append-only session event
  accessed_at: '2026-10-16T04:22:17Z'
  support: supports
  summary: 'Authorized curation: agent codex-gpt-5, model gpt-5, tool codex; exact
    owner and issue recorded.'
  snapshot_sha256: 4d5d1c5dc93e58c8505ec4b711d90876e3573c9836fe50d72391546411d0966d
- evidence_id: EH42
  kind: record_content
  reference: history/mappings/claw_colon_review_synonym/2026-10-16T040311Z-codex-gpt-5-00c6ad.yaml
  locator: Complete append-only session event
  accessed_at: '2026-10-16T04:22:17Z'
  support: supports
  summary: 'Authorized curation: agent codex-gpt-5, model gpt-5, tool codex; exact
    owner and issue recorded.'
  snapshot_sha256: 12401ab3d3fbd750f977169f186d144444e43f9853c6246114e6f7d13aa538e0
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact physical TSV rows
  accessed_at: '2026-10-16T04:22:19Z'
  support: supports
  summary: '[[4, "habitatmech:GOLD.037d4112ea\tHost-associated > Birds > Digestive
    system > Large intestine > Cloaca\thabitatmech:GOLD.b091b80314\tcodex-gpt-5\t2026-10-16\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2221 : The avian cloacal chamber
    is not a type of whole large intestine. Retain the generic cloaca genus, distinct
    source mint, all counts and native status. Exclude only the exact source-context
    parent; shared mapping endpoints remain unresolved."]]'
  snapshot_sha256: 29671974bab045cad2620da3ad89d176f8a2f5ca2612ad3c8761d82fd3f1ea81
assessments:
- assessment_id: A1
  area: consistency
  topic: Bounded repair and exact preservation
  outcome: supported
  summary: Removed the reviewed GOLD context-parent contribution(s). Native identity
    and status are unchanged. Source observations and independent valid genera are
    preserved. Unresolved predecessor findings remain explicitly open.
  target_ids:
  - habitatmech:GOLD.037d4112ea
  evidence_ids:
  - EX13
  - EX14
  - EX15
  - EX16
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
- assessment_id: A2
  area: identity
  topic: Current habitat identity and hierarchy
  outcome: supported
  summary: 'habitatmech:GOLD.037d4112ea: Cloaca; NARROW/SEEDED; parents ["UBERON:0000162"].
    No replacement identity or optional definition fabricated.'
  target_ids:
  - habitatmech:GOLD.037d4112ea
  evidence_ids:
  - EX13
  - EX14
  - EX15
  - EX16
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
- assessment_id: A3
  area: quantity
  topic: Source units and observation preservation
  outcome: supported
  summary: '[{"source": "GOLD", "source_id": "gold.ecosystem:6895", "source_label":
    "Cloaca", "source_path": "Host-associated > Birds > Digestive system > Large intestine
    > Cloaca", "mapping_predicate": "skos:narrowMatch", "assertion_count": 309, "assertion_unit":
    "ORGANISM"}]. Source counts/units, taxa, ranks, scores and parameters are unchanged;
    they are not prevalence.'
  target_ids:
  - habitatmech:GOLD.037d4112ea
  evidence_ids:
  - EX13
  - EX14
  - EX15
  - EX16
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
- assessment_id: A4
  area: representation
  topic: Every predecessor finding reconciled
  outcome: concern
  summary: 'Exact issue keys and predecessor references retained; scoped synonym correction
    and removal of one invalid insect match do not solve global #1249 or #1398.'
  target_ids:
  - habitatmech:GOLD.037d4112ea
  evidence_ids:
  - EX13
  - EX14
  - EX15
  - EX16
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
- assessment_id: A5
  area: completeness
  topic: Lifecycle and evidence boundaries
  outcome: supported
  summary: No optional mechanism, parameter, characteristic-presence or biological-absence
    claim added. Native status changes only for the explicit insect ITEM decision.
    Other reviewed targets retain their prior status.
  target_ids:
  - habitatmech:GOLD.037d4112ea
  evidence_ids:
  - EX13
  - EX14
  - EX15
  - EX16
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
findings:
- finding_id: F1
  issue_key: cloaca-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is not a strictly broader class
  description: Removed only the exact guarded GOLD context-parent contributions habitatmech:GOLD.b091b80314.
    Source paths and observations remain; independent valid genera are preserved.
  target_ids:
  - habitatmech:GOLD.037d4112ea
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX13
  - EX14
  - EX15
  - EX16
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2221
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T035435Z-cloaca-record
    finding_id: F1
  disposition_reason: Removed only the exact guarded GOLD context-parent contributions
    habitatmech:GOLD.b091b80314. Source paths and observations remain; independent
    valid genera are preserved.
- finding_id: F2
  issue_key: cloaca-mapping-endpoint-contract
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Mapping uses an undeclared ontology-parent endpoint
  description: Retained NARROW mapping still compares the source mint with an undeclared
    ontology-parent endpoint. Removing a context-only parent does not reconcile that
    shared contract.
  target_ids:
  - habitatmech:GOLD.037d4112ea
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - EX13
  - EX14
  - EX15
  - EX16
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/1398
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T035435Z-cloaca-record
    finding_id: F2
  disposition_reason: Retained NARROW mapping still compares the source mint with
    an undeclared ontology-parent endpoint. Removing a context-only parent does not
    reconcile that shared contract.
actions:
- action_id: ACT2
  finding_ids:
  - F2
  target_ids:
  - habitatmech:GOLD.037d4112ea
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/schema/habitatmech.yaml
    role: Maintained input or generator; never hand-edit generated habitat YAML
  description: Retained NARROW mapping still compares the source mint with an undeclared
    ontology-parent endpoint. Removing a context-only parent does not reconcile that
    shared contract. Proposed remaining work only; this successor does not perform
    further curation.
  generator: Controlled source/input correction, just seed, inspected just seed-canary,
    guarded just seed-apply, and dependent term-request/map/site/redirect regeneration
    where required.
  acceptance_checks:
  - Regress the exact target claim and preserve valid genera, identifiers, source
    counts/units and taxon associations. Recover original evidence before deleting
    a provisional pair; do not decrement frozen totals by hand.
  - Record authorized curation history; require schema, strict, provenance, history,
    label, corpus, site and full QC gates.
  - Save an immutable successor with the same issue key and exact predecessor finding
    identity.
limitations:
- Original specimen-level evidence and every pair-level citation were not exhaustively
  reconstructed. Source associations, counts, ranks and scores are not prevalence,
  viability or characteristic presence.
- Configured label validation skips 2063 no-adapter pairs; target TaxIds were separately
  resolved with current NCBI.
- 'iModulonDB is not applicable: no gene, regulator or expression-module claim is
  asserted. Cited experiments are used only for identity and context, not imported
  causal mechanisms.'
- Same-agent assessment, not independent approval. Final-head and merge-queue checks
  remain required before publication. The interrupted local archive command is not
  a passed check; hosted native archive verification is cited instead.
- Full hosted QC was not complete at capture; only its successful archive-contract
  step is claimed. Native scientific and product checks passed separately.
notes:
- Native working_tree capture retained. The off-main input base is preserved by an
  annotated provenance tag before merge and branch deletion. Generated seeding history
  is deterministic current-state output; all immutable saved review bundles and history/
  session files remain unchanged.
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261016T035435Z-cloaca-record
  relationship: Exact predecessor; every finding reconciled without rewriting history.
```
