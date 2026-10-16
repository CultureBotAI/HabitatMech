# Remediation review: cuticle__9784f327

- Review: 20261016T090038Z-cuticle__9784f327-remediation
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-16T08:41:19Z
- Finished UTC: 2026-10-16T09:00:38Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Removed the guarded GOLD context-parent contribution. The unrestricted arthropod cuticle source retains its mint UNGROUNDED/REVIEWED without a non-mineral genus or narrow mapping. Source observations and independent valid genera are preserved. No unresolved predecessor finding remains in this target scope.

## Scope And Provenance

Full current target assessment and explicit disposition of every baseline finding after bounded repair.

Selection: One of ten repaired targets from the crustacean-through-dental cohort.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4b24d5599c8da75fb5203191d5859e0ba6af0c40.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.c859639497 | data/habitats/host_associated/cuticle__9784f327.yaml | generated | Cuticle |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/habitats/host_associated/cuticle__9784f327.yaml | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:35:21Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cuticle__9784f327.yaml |
| just validate-strict data/habitats/host_associated/crustacean_maxillary_gland.yaml data/habitats/host_associated/crustacean_post_larval_stage.yaml data/habitats/host_associated/cryptomonads_cryptophytes.yaml data/habitats/host_associated/ctenophora.yaml data/habitats/host_associated/cud.yaml data/habitats/host_associated/cutaneous_leishmaniasis.yaml data/habitats/host_associated/cuticle.yaml data/habitats/host_associated/cuticle__11d6cb22.yaml data/habitats/host_associated/cuticle__6c2a3dac.yaml data/habitats/host_associated/cuticle__72f050c4.yaml data/habitats/host_associated/cuticle__9784f327.yaml data/habitats/host_associated/cuticle__a024212e.yaml data/habitats/host_associated/cv_1_cell.yaml data/habitats/host_associated/cyst.yaml data/habitats/host_associated/decayed_wood__afd3403c.yaml data/habitats/host_associated/decomposed_body.yaml data/habitats/host_associated/decomposed_body__7ba62861.yaml data/habitats/host_associated/decomposed_body__ee215354.yaml data/habitats/host_associated/dental_abscess.yaml data/habitats/host_associated/dental_calculus.yaml data/habitats/host_associated/dental_calculus__18e49dca.yaml data/habitats/host_associated/dental_calculus__8a0a99ac.yaml data/habitats/host_associated/dental_plaque.yaml data/habitats/host_associated/dental_plaque__384bd6e9.yaml | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:35:44Z. uv run python scripts/validate_strict.py data/habitats/host_associated/crustacean_maxillary_gland.yaml data/habitats/host_associated/crustacean_post_larval_stage.yaml data/habitats/host_associated/cryptomonads_cryptophytes.yaml data/habitats/host_associated/ctenophora.yaml data/habitats/host_associated/cud.yaml data/habitats/host_associated/cutaneous_leishmaniasis.yaml data/habitats/host_associated/cuticle.yaml data/habitats/host_associated/cuticle__11d6cb22.yaml data/habitats/host_associated/cuticle__6c2a3dac.yaml data/habitats/host_associated/cuticle__72f050c4.yaml data/habitats/host_associated/cuticle__9784f327.yaml data/habitats/host_associated/cuticle__a024212e.yaml data/habitats/host_associated/cv_1_cell.yaml data/habitats/host_associated/cyst.yaml data/habitats/host_associated/decayed_wood__afd3403c.yaml data/habitats/host_associated/decomposed_body.yaml data/habitats/host_associated/decomposed_body__7ba62861.yaml data/habitats/host_associated/decomposed_body__ee215354.yaml data/habitats/host_associated/dental_abscess.yaml data/habitats/host_associated/dental_calculus.yaml data/habitats/host_associated/dental_calculus__18e49dca.yaml data/habitats/host_associated/dental_calculus__8a0a99ac.yaml data/habitats/host_associated/dental_plaque.yaml data/habitats/host_associated/dental_plaque__384bd6e9.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| just validate-history | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:35:55Z. No issues found<br>839 history record(s) valid against src/habitatmech/schema/history.yaml |
| just provenance-check | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:35:56Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| just verify-corpus | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:36:18Z. expected 3209 records, found 3209 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| just validate-causal-all | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:36:23Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| just term-requests-check | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:36:46Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| just validate-products | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:37:48Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1173<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2063<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| uv run pytest -q tests/test_cuticle_dental_review_repairs.py --no-cov | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:37:58Z. ..                                                                       [100%]<br>2 passed in 7.86s |
| uv run ruff check . | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:37:58Z. All checks passed! |
| git diff --check | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:38:00Z.  |
| uv run pytest -q tests/test_decisions.py::test_curation_notes_do_not_cite_evidence_that_does_not_exist tests/test_cuticle_dental_review_repairs.py --no-cov | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:38:15Z. ...                                                                      [100%]<br>3 passed in 13.36s |
| just term-requests | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:35:45Z. wrote curation/term_requests/envo_robot_template.tsv: 110 ENVO terms from 110 source records<br><br>25 examined-ungrounded record(s) still have no request written. Top by volume:<br>      438  Medical-environment                habitatmech:BACDIVE.5e52ea1bba<br>      228  Fruit-Seed                         habitatmech:BACDIVE.ba016fe448<br>       35  Egg                                habitatmech:BACDIVE.d48ce9485d<br>        5  Caeca: Bacteriome                  habitatmech:GOLD.2d506b9526<br>        3  Abdomen                            habitatmech:GOLD.c6b0b54290<br>        2  Crop                               habitatmech:GOLD.5446ce4c6d<br>        1  Thalassic                          habitatmech:GOLD.3fece6dbf7<br>        1  Crop                               habitatmech:GOLD.57011086ca<br>        0  Subtidal zone sediment             habitatmech:GOLD.785879d721<br>        0  Subterranean lake                  habitatmech:GOLD.937bf682c4<br><br>covered 105842 upstream assertions; 713 still unrequested across 25 record(s); 15 examined and deliberately not asked for<br><br>&#96;created by&#96; is empty: it wants pipe-delimited full ORCID IRIs and this script cannot know them.<br> uv run python scripts/build_term_requests.py |
| just docs-stats | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:36:09Z. updated README corpus statistics<br> uv run python scripts/check_docs.py --write |
| just render | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:36:51Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 135 term requests -&gt; /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages<br> uv run python scripts/render_pages.py |
| just render-check | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:37:36Z. rendered 3209 habitat pages, 259 redirect stubs, 8 categories, 135 term requests -&gt; /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmp29xf44zp/site<br>pages/ is in step with the corpus<br> uv run python scripts/render_pages.py --check |
| just redirects-check | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:40:01Z. RETIRED.tsv is current (259 redirects)<br> uv run python scripts/build_redirects.py --check |
| uv run ruff check . | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:40:01Z. All checks passed! |
| git diff --check | passed | True | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:40:01Z.  |
| Exact-revision hosted authoritative QC and archive contract | passed | True | habitatmech:GOLD.c859639497 | Verified 2026-10-16T09:00:10Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38875299816 |
| Citation correction preserves semantic-map input bytes | passed | False | habitatmech:GOLD.c859639497 | Finished 2026-10-16T08:35:14Z. Full 3209-record semantic JSONL is byte-identical before and after replacing PMID strings with their publication URLs. |

## Scientific And Domain Assessments

### Bounded correction and exact preservation

consistency: supported. Targets: habitatmech:GOLD.c859639497.

Removed the guarded GOLD context-parent contribution. The unrestricted arthropod cuticle source retains its mint UNGROUNDED/REVIEWED without a non-mineral genus or narrow mapping. Source observations and independent valid genera are preserved. No unresolved predecessor finding remains in this target scope.

### Current anatomical identity and hierarchy

identity: supported. Targets: habitatmech:GOLD.c859639497.

habitatmech:GOLD.c859639497: Cuticle; UNGROUNDED/REVIEWED; parents []. Source anatomy/material scope remains as assessed in the baseline; only the documented false parents are removed. No replacement identity, genus or definition is fabricated.

### Units, counts and observations

quantity: supported. Targets: habitatmech:GOLD.c859639497.

[{"source": "GOLD", "source_id": "gold.ecosystem:8187", "source_label": "Cuticle", "source_path": "Host-associated &gt; Arthropoda: Crustaceans &gt; Integumentary system &gt; Cuticle", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}]. Original counts/units, taxa, scores and parameters are preserved, not interpreted as prevalence or viability.

### Predecessor reconciliation

representation: supported. Targets: habitatmech:GOLD.c859639497.

Every previous finding keeps its stable issue key and exact lineage. Removing three unsupported narrow matches does not resolve global mapping contract #1398.

### Evidence and lifecycle boundaries

completeness: supported. Targets: habitatmech:GOLD.c859639497.

Only the three explicit arthropod ITEM decisions change native status. Optional definitions, causal mechanisms and biological absence claims are not invented. The complete target, remaining parents, history and original evidence were rechecked.

## Findings

### F1: Source context is not a strictly broader habitat class

major / resolved / confirmed; issue key: cuticle--9784f327-context-parent.

Removed only the guarded GOLD source-context contribution habitatmech:GOLD.dd76069e56. Independent valid parents and every source observation remain intact.

Disposition: Removed only the guarded GOLD source-context contribution habitatmech:GOLD.dd76069e56. Independent valid parents and every source observation remain intact.

### F2: Mapping comparison uses an undeclared ontology-parent endpoint

major / resolved / confirmed; issue key: cuticle--9784f327-mapping-endpoint-contract.

An explicit ITEM decision preserves this unrestricted arthropod source mint UNGROUNDED without the non-mineral genus or narrow mapping. This resolves only this scoped witness, not global #1398 or the upstream cuticle definition.

Disposition: An explicit ITEM decision preserves this unrestricted arthropod source mint UNGROUNDED without the non-mineral genus or narrow mapping. This resolves only this scoped witness, not global #1398 or the upstream cuticle definition.

### F3: Non-mineral cuticle definition is not broader than the unrestricted source

major / resolved / confirmed; issue key: cuticle--9784f327-nonmineral-genus-scope.

An explicit ITEM decision preserves this unrestricted arthropod source mint UNGROUNDED without the non-mineral genus or narrow mapping. This resolves only this scoped witness, not global #1398 or the upstream cuticle definition.

Disposition: An explicit ITEM decision preserves this unrestricted arthropod source mint UNGROUNDED without the non-mineral genus or narrow mapping. This resolves only this scoped witness, not global #1398 or the upstream cuticle definition.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| EX9 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001002/graph; UBERON_0001002-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001002", "target": "http://purl.obolibrary.org/obo/UBERON_0000476", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001002", "target": "http://purl.obolibrary.org/obo/NCBITaxon_6072", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}] |
| EX10 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001002; UBERON_0001002.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:0001002", "label": "cuticle", "is_obsolete": false, "description": ["EDITOR_NOTE TODO - check cuticle vs exoskeleton. Note that GO has a very generic definition of cuticle. See also arthropod-anatomy ontology. Note in ncit Cuticle is a plant part", "Tough but flexible, non-mineral outer coverings of an organism, or parts of an organism, that provide protection. Cuticles are non-homologous, differing in their origin, structure and chemical composition[WP]."], "obo_synonym": [{"name": "cuticula", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "BTO", "id": "0001600", "description": null, "url": "http://purl.obolibrary.org/obo/BTO_0001600"}]}], "annotation": {"database_cross_reference": ["BTO:0001600", "Wikipedia:Cuticle"], "has_relational_adjective": ["cuticular"], "id": ["UBERON:0001002"]}} |
| EX11 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002416/graph; UBERON_0002416-graph.json | context_only | Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0002416", "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002416", "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492", "label": "existence ends during"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002416", "target": "http://purl.obolibrary.org/obo/UBERON_0000468", "uri": "http://purl.obolibrary.org/obo/RO_0002007", "label": "bounding layer of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002416", "target": "http://purl.obolibrary.org/obo/UBERON_0007376", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002416", "target": "http://purl.obolibrary.org/obo/UBERON_0013514", "uri": "http://purl.obolibrary.org/obo/RO_0002219", "label": "surrounded by"}] |
| EX12 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002416; UBERON_0002416.json | context_only | Current identity, active status, definition and typed synonyms: {"obo_id": "UBERON:0002416", "label": "integumental system", "is_obsolete": false, "description": ["Connected anatomical system that forms a barrier between an animal and its environment. In vertebrates, the integumental system consists of the epidermis, dermis plus associated glands and adnexa such as hair and scales. In invertebrates, the integumental system may include cuticle."], "obo_synonym": [{"name": "integumentary system", "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "FMA", "id": "72979", "description": null, "url": "http://purl.org/sig/ont/fma/72979"}]}, {"name": "dermal system", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "MIAA", "id": "0000033", "description": null, "url": null}]}, {"name": "integumentum commune", "scope": "hasRelatedSynonym", "type": "latin term", "xrefs": [{"database": "Wikipedia", "id": "Integumentary_system", "description": null, "url": "http://en.wikipedia.org/wiki/Integumentary_system"}]}, {"name": "organism surface", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "EHDAA2", "id": "0003154", "description": null, "url": "http://purl.obolibrary.org/obo/EHDAA2_0003154"}]}, {"name": "surface", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database": "BILA", "id": "0000118", "description": null, "url": "http://purl.obolibrary.org/obo/BILA_0000118"}]}], "annotation": {"Contributor": ["https://orcid.org/0000-0002-0956-8634", "https://orcid.org/0000-0002-6601-2165"], "database_cross_reference": ["AEO:0000154", "BILA:0000118", "CALOHA:TS-1299", "CARO:0002001", "EFO:0000807", "EHDAA2:0000836", "EHDAA2_RETIRED:0003154", "EHDAA:6520", "EMAPA:17524", "EV:0100151", "FMA:72979", "HAO:0000421", "MA:0000014", "MAT:0000033", "MESH:D034582", "MIAA:0000033", "NCIT:C12907", "SCTID:361692004", "TADS:0000108", "VHOG:0000403", "Wikipedia:Integumentary_system", "XAO:0000176", "galen:Surface", "FBbt:00004969", "UMLS:C0037267"], "has_alternative_id": ["UBERON:0007029"], "homology_notes": ["(...) the integument of many tetrapods is reinforced by a morphologically and structurally diverse assemblage of skeletal elements. These elements are widely understood to be derivatives of the once all-encompassing dermal skeleton of stem-gnathostomes (...).[well established][VHOG]"], "id": ["UBERON:0002416"]}} |
| EX13 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18550385%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; paper-isopod-cuticle.json | context_only | Primary abstract PMID:18550385; DOI:10.1016/j.jsb.2008.04.010 inspected: microscopy and Raman analysis document calcium-carbonate phases in Armadillidium and Porcellio cuticle. Supports a mineralized crustacean counterexample, not universal mineralization of all cuticle regions. |
| EAFTER | data/habitats/host_associated/cuticle__9784f327.yaml; Entire regenerated target YAML | supports | {"identifier": "habitatmech:GOLD.c859639497", "label": "Cuticle", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED", "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:8187", "source_label": "Cuticle", "source_path": "Host-associated &gt; Arthropoda: Crustaceans &gt; Integumentary system &gt; Cuticle", "notes": "2 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED: no ontology term fits this concept. ITEM reassessment https://github.com/CultureBotAI/HabitatMech/issues/2236 : UBERON:0001002 explicitly restricts cuticle to non-mineral coverings, whereas this unrestricted host-group source includes mineralized examples (https://pubmed.ncbi.nlm.nih.gov/15670859/ for millipedes; https://pubmed.ncbi.nlm.nih.gov/18550385/ for isopods). Retain the source mint UNGROUNDED pending a verified genus or upstream definition repair; this is not proof that no suitable ontology term exists. Preserve all source observations. Whole-organ context is excluded separately. Path: Host-associated &gt; Arthropoda: Crustaceans &gt; Integumentary system &gt; Cuticle (source concept habitatmech:GOLD.c859639497)"}, {"timestamp": "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED", "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.dd76069e56 for habitatmech:GOLD.c859639497 (Host-associated &gt; Arthropoda: Crustaceans &gt; Integumentary system &gt; Cuticle). Review https://github.com/CultureBotAI/HabitatMech/issues/2235 : Maxillary gland is not the entire excretory system; cud is not the stomach; cuticle is not the whole integument, integumentary system or skin; abscess, calculus and plaque are not the whole oral cavity. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.c859639497. Other identity, status and mapping findings remain separate."}]} |
| EPREV | reviews/structured/20261016T073707Z-cuticle__9784f327-record/review.yaml; Every immutable baseline finding | supports | Exact predecessor keys and findings reconciled; the original inspected source scope is preserved. |
| ETEST | tests/test_cuticle_dental_review_repairs.py; Complete full-corpus counterfactual | supports | Exactly ten records differ. Only guarded context-parent removal and three arthropod grounding/predicate/status corrections change scientific fields; all source observations and unrelated fields are invariant. |
| ERULE | docs/CURATION.md; Strict hierarchy, ITEM decisions and source units | supports | Native history/status follows maintained rows; generated artifacts are not hand-edited. |
| EH40 | history/mappings/cuticle_dental_review_citations/2026-10-16T083223Z-codex-gpt-5-c42651.yaml; Complete session event | supports | Authorized curation by codex-gpt-5; maintained owner and issue retained. |
| EH41 | history/mappings/cuticle_dental_review_mineral/2026-10-16T074759Z-codex-gpt-5-d2d9db.yaml; Complete session event | supports | Authorized curation by codex-gpt-5; maintained owner and issue retained. |
| EH42 | history/mappings/cuticle_dental_review_parents/2026-10-16T074758Z-codex-gpt-5-56d722.yaml; Complete session event | supports | Authorized curation by codex-gpt-5; maintained owner and issue retained. |
| EPARENTS | curation/gold_parent_exclusions.tsv; Exact physical TSV rows | supports | [[7, "habitatmech:GOLD.c859639497\tHost-associated &gt; Arthropoda: Crustaceans &gt; Integumentary system &gt; Cuticle\thabitatmech:GOLD.dd76069e56\tcodex-gpt-5\t2026-10-16\tReview https://github.com/CultureBotAI/HabitatMech/issues/2235 : Maxillary gland is not the entire excretory system; cud is not the stomach; cuticle is not the whole integument, integumentary system or skin; abscess, calculus and plaque are not the whole oral cavity. Exclude only exact guarded GOLD source-path contributions, preserving independent genera and all source observations. Exact target habitatmech:GOLD.c859639497. Other identity, status and mapping findings remain separate."]] |
| EDECISION | curation/decisions.tsv; Exact physical TSV rows | supports | [[4, "habitatmech:GOLD.c859639497\tCONFIRM_UNGROUNDED\t\t\t\tcodex-gpt-5\t2026-10-16\tITEM reassessment https://github.com/CultureBotAI/HabitatMech/issues/2236 : UBERON:0001002 explicitly restricts cuticle to non-mineral coverings, whereas this unrestricted host-group source includes mineralized examples (https://pubmed.ncbi.nlm.nih.gov/15670859/ for millipedes; https://pubmed.ncbi.nlm.nih.gov/18550385/ for isopods). Retain the source mint UNGROUNDED pending a verified genus or upstream definition repair; this is not proof that no suitable ontology term exists. Preserve all source observations. Whole-organ context is excluded separately. Path: Host-associated &gt; Arthropoda: Crustaceans &gt; Integumentary system &gt; Cuticle\tITEM\t\tparent"]] |

## Limits And Additional Notes

- Original specimen-level evidence was not exhaustively reconstructed. Source counts, associations and scores do not establish prevalence, viability or characteristic presence.
- Configured id-label validation skips 2063 no-adapter pairs; the 18 displayed target TaxIds were separately checked against current NCBI.
- iModulonDB is not applicable: these records assert no genes, regulators, pathways or expression modules. Literature mechanisms were not imported as causal graphs.
- UNGROUNDED means no replacement identity or genus was verified in this bounded repair, not proof that no suitable term exists. The generator boilerplate claiming no ontology term fits must be read with the explicit qualification in the ITEM notes. Upstream cuticle definition refinement and alternative genera remain future work.
- Same-agent disposition, not independent human approval. Final-head and merge-queue checks remain separate publication gates. Whole-corpus scientific review and current kg-microbe export conformance are incomplete.
- All earlier saved bundles and session histories remain unchanged. Preserve the exact off-main input base with an annotated provenance tag before squash merge and branch deletion.
- A preliminary unsaved capture at b3b87caf3d56b74891036c9d3c1c201f07388c63 was retained separately. CI #2240 required publication URLs instead of PMID CURIEs in three decision notes; after that formatting correction and regeneration, inputs were freshly captured and the complete targets reassessed. No prior saved review was refreshed or rewritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T090038Z-cuticle__9784f327-remediation
repository: CultureBotAI/HabitatMech
kind: record
title: 'Remediation review: cuticle__9784f327'
started_at: '2026-10-16T08:41:19Z'
finished_at: '2026-10-16T09:00:38Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: The same agent read sources, assessed the target and authored
    this report; not independent reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Removed the guarded GOLD context-parent contribution. The unrestricted arthropod
  cuticle source retains its mint UNGROUNDED/REVIEWED without a non-mineral genus
  or narrow mapping. Source observations and independent valid genera are preserved.
  No unresolved predecessor finding remains in this target scope.
source:
  git_revision: 4b24d5599c8da75fb5203191d5859e0ba6af0c40
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
    sha256: bd080045e44f1995788c20df1ea1e71e3fe8d2dc44a3730f8618c8f133e2341a
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 37dc4b40642d19e7b5c3262f368d12daa82e03115e7731a2326ae88785ceff5b
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 1675ec9acca1f4fe6b1101188aafbc10f3cf6d2fabfd149232ec0260262a311f
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
  - path: data/habitats/host_associated/cuticle__9784f327.yaml
    sha256: 3b09220a9e491b0625867635e0a66a56d337b5c9db8f4b98acfd614a8c953873
    role: target
  - path: data/habitats/host_associated/integumentary_system__8b2b03cc.yaml
    sha256: 028b290899f73db527266d7cafbfc679a46dc610cd11c61dd4d8c52efe3f12fc
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
  - path: history/mappings/cuticle_dental_review_citations/2026-10-16T083223Z-codex-gpt-5-c42651.yaml
    sha256: f0a7f6577764a3dc69c894b8c6dffc7cac78a08a1d7f9f8a4c990bf6d9382a0e
    role: context
  - path: history/mappings/cuticle_dental_review_mineral/2026-10-16T074759Z-codex-gpt-5-d2d9db.yaml
    sha256: b2d4696ff2e86b972d0083c191362137f20c3c1c9e6a1b1d8f23c0051d03c3fa
    role: context
  - path: history/mappings/cuticle_dental_review_parents/2026-10-16T074758Z-codex-gpt-5-56d722.yaml
    sha256: 557e55252578fe0c8d3d92eb3054ae15a96973790ef9048f0b9cdbdd90af98cd
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reviews/structured/20261016T073707Z-cuticle__9784f327-record/review.yaml
    sha256: acc2dbccac24b7bb83bb77fdd684e46cf086522ffcdea3fe802e5180af4f86c7
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
  - path: tests/test_cuticle_dental_review_repairs.py
    sha256: bfa65736cdf7252a34180b268b0e56e4ef25970cf3308b0f84658f3f731b6ed5
    role: context
targets:
- target_id: habitatmech:GOLD.c859639497
  path: data/habitats/host_associated/cuticle__9784f327.yaml
  label: Cuticle
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
    finding after bounded repair.
  selection: One of ten repaired targets from the crustacean-through-dental cohort.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.c859639497
  exclusions:
  - target: Other corpus records and SSSOM/KGX conformance
    reason: Not whole-corpus scientific approval or shared export-contract certification.
checks:
- check_id: C5
  name: just validate data/habitats/host_associated/cuticle__9784f327.yaml
  status: passed
  required: true
  command: just validate data/habitats/host_associated/cuticle__9784f327.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:35:21Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/cuticle__9784f327.yaml"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C10
  name: just validate-strict data/habitats/host_associated/crustacean_maxillary_gland.yaml
    data/habitats/host_associated/crustacean_post_larval_stage.yaml data/habitats/host_associated/cryptomonads_cryptophytes.yaml
    data/habitats/host_associated/ctenophora.yaml data/habitats/host_associated/cud.yaml
    data/habitats/host_associated/cutaneous_leishmaniasis.yaml data/habitats/host_associated/cuticle.yaml
    data/habitats/host_associated/cuticle__11d6cb22.yaml data/habitats/host_associated/cuticle__6c2a3dac.yaml
    data/habitats/host_associated/cuticle__72f050c4.yaml data/habitats/host_associated/cuticle__9784f327.yaml
    data/habitats/host_associated/cuticle__a024212e.yaml data/habitats/host_associated/cv_1_cell.yaml
    data/habitats/host_associated/cyst.yaml data/habitats/host_associated/decayed_wood__afd3403c.yaml
    data/habitats/host_associated/decomposed_body.yaml data/habitats/host_associated/decomposed_body__7ba62861.yaml
    data/habitats/host_associated/decomposed_body__ee215354.yaml data/habitats/host_associated/dental_abscess.yaml
    data/habitats/host_associated/dental_calculus.yaml data/habitats/host_associated/dental_calculus__18e49dca.yaml
    data/habitats/host_associated/dental_calculus__8a0a99ac.yaml data/habitats/host_associated/dental_plaque.yaml
    data/habitats/host_associated/dental_plaque__384bd6e9.yaml
  status: passed
  required: true
  command: just validate-strict data/habitats/host_associated/crustacean_maxillary_gland.yaml
    data/habitats/host_associated/crustacean_post_larval_stage.yaml data/habitats/host_associated/cryptomonads_cryptophytes.yaml
    data/habitats/host_associated/ctenophora.yaml data/habitats/host_associated/cud.yaml
    data/habitats/host_associated/cutaneous_leishmaniasis.yaml data/habitats/host_associated/cuticle.yaml
    data/habitats/host_associated/cuticle__11d6cb22.yaml data/habitats/host_associated/cuticle__6c2a3dac.yaml
    data/habitats/host_associated/cuticle__72f050c4.yaml data/habitats/host_associated/cuticle__9784f327.yaml
    data/habitats/host_associated/cuticle__a024212e.yaml data/habitats/host_associated/cv_1_cell.yaml
    data/habitats/host_associated/cyst.yaml data/habitats/host_associated/decayed_wood__afd3403c.yaml
    data/habitats/host_associated/decomposed_body.yaml data/habitats/host_associated/decomposed_body__7ba62861.yaml
    data/habitats/host_associated/decomposed_body__ee215354.yaml data/habitats/host_associated/dental_abscess.yaml
    data/habitats/host_associated/dental_calculus.yaml data/habitats/host_associated/dental_calculus__18e49dca.yaml
    data/habitats/host_associated/dental_calculus__8a0a99ac.yaml data/habitats/host_associated/dental_plaque.yaml
    data/habitats/host_associated/dental_plaque__384bd6e9.yaml
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:35:44Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/crustacean_maxillary_gland.yaml data/habitats/host_associated/crustacean_post_larval_stage.yaml\
    \ data/habitats/host_associated/cryptomonads_cryptophytes.yaml data/habitats/host_associated/ctenophora.yaml\
    \ data/habitats/host_associated/cud.yaml data/habitats/host_associated/cutaneous_leishmaniasis.yaml\
    \ data/habitats/host_associated/cuticle.yaml data/habitats/host_associated/cuticle__11d6cb22.yaml\
    \ data/habitats/host_associated/cuticle__6c2a3dac.yaml data/habitats/host_associated/cuticle__72f050c4.yaml\
    \ data/habitats/host_associated/cuticle__9784f327.yaml data/habitats/host_associated/cuticle__a024212e.yaml\
    \ data/habitats/host_associated/cv_1_cell.yaml data/habitats/host_associated/cyst.yaml\
    \ data/habitats/host_associated/decayed_wood__afd3403c.yaml data/habitats/host_associated/decomposed_body.yaml\
    \ data/habitats/host_associated/decomposed_body__7ba62861.yaml data/habitats/host_associated/decomposed_body__ee215354.yaml\
    \ data/habitats/host_associated/dental_abscess.yaml data/habitats/host_associated/dental_calculus.yaml\
    \ data/habitats/host_associated/dental_calculus__18e49dca.yaml data/habitats/host_associated/dental_calculus__8a0a99ac.yaml\
    \ data/habitats/host_associated/dental_plaque.yaml data/habitats/host_associated/dental_plaque__384bd6e9.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C11
  name: just validate-history
  status: passed
  required: true
  command: just validate-history
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: 'Finished 2026-10-16T08:35:55Z. No issues found

    839 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C12
  name: just provenance-check
  status: passed
  required: true
  command: just provenance-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:35:56Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C13
  name: just verify-corpus
  status: passed
  required: true
  command: just verify-corpus
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:36:18Z. expected 3209 records, found 3209 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C14
  name: just validate-causal-all
  status: passed
  required: true
  command: just validate-causal-all
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:36:23Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C15
  name: just term-requests-check
  status: passed
  required: true
  command: just term-requests-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:36:46Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C16
  name: just validate-products
  status: passed
  required: true
  command: just validate-products
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:37:48Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1173\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2063\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C17
  name: uv run pytest -q tests/test_cuticle_dental_review_repairs.py --no-cov
  status: passed
  required: true
  command: uv run pytest -q tests/test_cuticle_dental_review_repairs.py --no-cov
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: 'Finished 2026-10-16T08:37:58Z. ..                                                                       [100%]

    2 passed in 7.86s'
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C18
  name: uv run ruff check .
  status: passed
  required: true
  command: uv run ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: Finished 2026-10-16T08:37:58Z. All checks passed!
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C19
  name: git diff --check
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: 'Finished 2026-10-16T08:38:00Z. '
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C20
  name: uv run pytest -q tests/test_decisions.py::test_curation_notes_do_not_cite_evidence_that_does_not_exist
    tests/test_cuticle_dental_review_repairs.py --no-cov
  status: passed
  required: true
  command: uv run pytest -q tests/test_decisions.py::test_curation_notes_do_not_cite_evidence_that_does_not_exist
    tests/test_cuticle_dental_review_repairs.py --no-cov
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: 'Finished 2026-10-16T08:38:15Z. ...                                                                      [100%]

    3 passed in 13.36s'
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C21
  name: just term-requests
  status: passed
  required: true
  command: just term-requests
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:35:45Z. wrote curation/term_requests/envo_robot_template.tsv:\
    \ 110 ENVO terms from 110 source records\n\n25 examined-ungrounded record(s) still\
    \ have no request written. Top by volume:\n      438  Medical-environment    \
    \            habitatmech:BACDIVE.5e52ea1bba\n      228  Fruit-Seed           \
    \              habitatmech:BACDIVE.ba016fe448\n       35  Egg                \
    \                habitatmech:BACDIVE.d48ce9485d\n        5  Caeca: Bacteriome\
    \                  habitatmech:GOLD.2d506b9526\n        3  Abdomen           \
    \                 habitatmech:GOLD.c6b0b54290\n        2  Crop               \
    \                habitatmech:GOLD.5446ce4c6d\n        1  Thalassic           \
    \               habitatmech:GOLD.3fece6dbf7\n        1  Crop                 \
    \              habitatmech:GOLD.57011086ca\n        0  Subtidal zone sediment\
    \             habitatmech:GOLD.785879d721\n        0  Subterranean lake      \
    \            habitatmech:GOLD.937bf682c4\n\ncovered 105842 upstream assertions;\
    \ 713 still unrequested across 25 record(s); 15 examined and deliberately not\
    \ asked for\n\n`created by` is empty: it wants pipe-delimited full ORCID IRIs\
    \ and this script cannot know them.\n uv run python scripts/build_term_requests.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C22
  name: just docs-stats
  status: passed
  required: true
  command: just docs-stats
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:36:09Z. updated README corpus statistics\n uv run\
    \ python scripts/check_docs.py --write"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C23
  name: just render
  status: passed
  required: true
  command: just render
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:36:51Z. rendered 3209 habitat pages, 259 redirect\
    \ stubs, 8 categories, 135 term requests -> /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/pages\n\
    \ uv run python scripts/render_pages.py"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C24
  name: just render-check
  status: passed
  required: true
  command: just render-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:37:36Z. rendered 3209 habitat pages, 259 redirect\
    \ stubs, 8 categories, 135 term requests -> /var/folders/lm/hg0p5znd1hd5yc5lml35j6lh0000gn/T/tmp29xf44zp/site\n\
    pages/ is in step with the corpus\n uv run python scripts/render_pages.py --check"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C25
  name: just redirects-check
  status: passed
  required: true
  command: just redirects-check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: "Finished 2026-10-16T08:40:01Z. RETIRED.tsv is current (259 redirects)\n\
    \ uv run python scripts/build_redirects.py --check"
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C26
  name: uv run ruff check .
  status: passed
  required: true
  command: uv run ruff check .
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: Finished 2026-10-16T08:40:01Z. All checks passed!
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: C27
  name: git diff --check
  status: passed
  required: true
  command: git diff --check
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: 'Finished 2026-10-16T08:40:01Z. '
  scope_note: Individual schema, 24-target strict validation and otherwise the documented
    full-corpus/product scope.
- check_id: CCI
  name: Exact-revision hosted authoritative QC and archive contract
  status: passed
  required: true
  command: gh run view 38875299816 --repo CultureBotAI/HabitatMech --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: Verified 2026-10-16T09:00:10Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38875299816
  scope_note: Repaired input/product commit before these successor outputs; final-head
    and merge-queue checks remain separate.
- check_id: CMAP
  name: Citation correction preserves semantic-map input bytes
  status: passed
  required: false
  command: cmp build/review-cs-map/current-inputs.jsonl build/review-cs-map/citation-inputs.jsonl
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.c859639497
  summary: Finished 2026-10-16T08:35:14Z. Full 3209-record semantic JSONL is byte-identical
    before and after replacing PMID strings with their publication URLs.
  scope_note: This is a text-neutral citation correction, not a new embedding run
    or export-conformance audit.
evidence:
- evidence_id: EX9
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001002/graph
  locator: UBERON_0001002-graph.json
  accessed_at: '2026-10-16T07:15:18Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0001002",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000476", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0001002",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_6072", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}]'
  snapshot_sha256: 7020267ba914b2276edf62b2d149038f87c66aea11164cc014a37b2de4c45a85
- evidence_id: EX10
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001002
  locator: UBERON_0001002.json
  accessed_at: '2026-10-16T07:15:18Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:0001002", "label": "cuticle", "is_obsolete": false, "description": ["EDITOR_NOTE
    TODO - check cuticle vs exoskeleton. Note that GO has a very generic definition
    of cuticle. See also arthropod-anatomy ontology. Note in ncit Cuticle is a plant
    part", "Tough but flexible, non-mineral outer coverings of an organism, or parts
    of an organism, that provide protection. Cuticles are non-homologous, differing
    in their origin, structure and chemical composition[WP]."], "obo_synonym": [{"name":
    "cuticula", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database":
    "BTO", "id": "0001600", "description": null, "url": "http://purl.obolibrary.org/obo/BTO_0001600"}]}],
    "annotation": {"database_cross_reference": ["BTO:0001600", "Wikipedia:Cuticle"],
    "has_relational_adjective": ["cuticular"], "id": ["UBERON:0001002"]}}'
  snapshot_sha256: 7b268729dfadbf4122dccd00b9abaf3007d8dc2988e7ce77144efb3d58579240
- evidence_id: EX11
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002416/graph
  locator: UBERON_0002416-graph.json
  accessed_at: '2026-10-16T07:15:22Z'
  support: context_only
  summary: 'Current typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/UBERON_0002416",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000467", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002416",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000066", "uri": "http://purl.obolibrary.org/obo/RO_0002492",
    "label": "existence ends during"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002416",
    "target": "http://purl.obolibrary.org/obo/UBERON_0000468", "uri": "http://purl.obolibrary.org/obo/RO_0002007",
    "label": "bounding layer of"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002416",
    "target": "http://purl.obolibrary.org/obo/UBERON_0007376", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/UBERON_0002416",
    "target": "http://purl.obolibrary.org/obo/UBERON_0013514", "uri": "http://purl.obolibrary.org/obo/RO_0002219",
    "label": "surrounded by"}]'
  snapshot_sha256: a06731988b4839b8c7d6fb25637f9f988fb5b3294222d3fa38847f5c06c9b76a
- evidence_id: EX12
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002416
  locator: UBERON_0002416.json
  accessed_at: '2026-10-16T07:15:21Z'
  support: context_only
  summary: 'Current identity, active status, definition and typed synonyms: {"obo_id":
    "UBERON:0002416", "label": "integumental system", "is_obsolete": false, "description":
    ["Connected anatomical system that forms a barrier between an animal and its environment.
    In vertebrates, the integumental system consists of the epidermis, dermis plus
    associated glands and adnexa such as hair and scales. In invertebrates, the integumental
    system may include cuticle."], "obo_synonym": [{"name": "integumentary system",
    "scope": "hasExactSynonym", "type": null, "xrefs": [{"database": "FMA", "id":
    "72979", "description": null, "url": "http://purl.org/sig/ont/fma/72979"}]}, {"name":
    "dermal system", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database":
    "MIAA", "id": "0000033", "description": null, "url": null}]}, {"name": "integumentum
    commune", "scope": "hasRelatedSynonym", "type": "latin term", "xrefs": [{"database":
    "Wikipedia", "id": "Integumentary_system", "description": null, "url": "http://en.wikipedia.org/wiki/Integumentary_system"}]},
    {"name": "organism surface", "scope": "hasRelatedSynonym", "type": null, "xrefs":
    [{"database": "EHDAA2", "id": "0003154", "description": null, "url": "http://purl.obolibrary.org/obo/EHDAA2_0003154"}]},
    {"name": "surface", "scope": "hasRelatedSynonym", "type": null, "xrefs": [{"database":
    "BILA", "id": "0000118", "description": null, "url": "http://purl.obolibrary.org/obo/BILA_0000118"}]}],
    "annotation": {"Contributor": ["https://orcid.org/0000-0002-0956-8634", "https://orcid.org/0000-0002-6601-2165"],
    "database_cross_reference": ["AEO:0000154", "BILA:0000118", "CALOHA:TS-1299",
    "CARO:0002001", "EFO:0000807", "EHDAA2:0000836", "EHDAA2_RETIRED:0003154", "EHDAA:6520",
    "EMAPA:17524", "EV:0100151", "FMA:72979", "HAO:0000421", "MA:0000014", "MAT:0000033",
    "MESH:D034582", "MIAA:0000033", "NCIT:C12907", "SCTID:361692004", "TADS:0000108",
    "VHOG:0000403", "Wikipedia:Integumentary_system", "XAO:0000176", "galen:Surface",
    "FBbt:00004969", "UMLS:C0037267"], "has_alternative_id": ["UBERON:0007029"], "homology_notes":
    ["(...) the integument of many tetrapods is reinforced by a morphologically and
    structurally diverse assemblage of skeletal elements. These elements are widely
    understood to be derivatives of the once all-encompassing dermal skeleton of stem-gnathostomes
    (...).[well established][VHOG]"], "id": ["UBERON:0002416"]}}'
  snapshot_sha256: b99dd38824896b19176431aaa2cc09f4b344a5fa22c303ec9193f3c9f1694d8a
- evidence_id: EX13
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18550385%20AND%20SRC%3AMED&format=json&resultType=core
  locator: paper-isopod-cuticle.json
  accessed_at: '2026-10-16T07:30:05Z'
  support: context_only
  summary: 'Primary abstract PMID:18550385; DOI:10.1016/j.jsb.2008.04.010 inspected:
    microscopy and Raman analysis document calcium-carbonate phases in Armadillidium
    and Porcellio cuticle. Supports a mineralized crustacean counterexample, not universal
    mineralization of all cuticle regions.'
  snapshot_sha256: 0f332aa75517dc100f0b593522f1f0347a136ab43324d1b880240278310beb05
- evidence_id: EAFTER
  kind: record_content
  reference: data/habitats/host_associated/cuticle__9784f327.yaml
  locator: Entire regenerated target YAML
  accessed_at: '2026-10-16T09:00:35Z'
  support: supports
  summary: '{"identifier": "habitatmech:GOLD.c859639497", "label": "Cuticle", "habitat_category":
    "HOST_ASSOCIATED", "grounding_status": "UNGROUNDED", "mapping_status": "REVIEWED",
    "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:8187",
    "source_label": "Cuticle", "source_path": "Host-associated > Arthropoda: Crustaceans
    > Integumentary system > Cuticle", "notes": "2 GOLD ecosystem node ids share this
    path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history":
    [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action":
    "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested
    by GOLD. Grounding: UNGROUNDED."}, {"timestamp": "2026-10-16T00:00:00Z", "curator":
    "codex-gpt-5", "action": "CONFIRM_UNGROUNDED", "changes": "Confirmed UNGROUNDED:
    no ontology term fits this concept. ITEM reassessment https://github.com/CultureBotAI/HabitatMech/issues/2236
    : UBERON:0001002 explicitly restricts cuticle to non-mineral coverings, whereas
    this unrestricted host-group source includes mineralized examples (https://pubmed.ncbi.nlm.nih.gov/15670859/
    for millipedes; https://pubmed.ncbi.nlm.nih.gov/18550385/ for isopods). Retain
    the source mint UNGROUNDED pending a verified genus or upstream definition repair;
    this is not proof that no suitable ontology term exists. Preserve all source observations.
    Whole-organ context is excluded separately. Path: Host-associated > Arthropoda:
    Crustaceans > Integumentary system > Cuticle (source concept habitatmech:GOLD.c859639497)"},
    {"timestamp": "2026-10-16T00:00:00Z", "curator": "codex-gpt-5", "action": "SOURCE_PARENT_EXCLUDED",
    "changes": "Excluded GOLD source-path parent contribution habitatmech:GOLD.dd76069e56
    for habitatmech:GOLD.c859639497 (Host-associated > Arthropoda: Crustaceans > Integumentary
    system > Cuticle). Review https://github.com/CultureBotAI/HabitatMech/issues/2235
    : Maxillary gland is not the entire excretory system; cud is not the stomach;
    cuticle is not the whole integument, integumentary system or skin; abscess, calculus
    and plaque are not the whole oral cavity. Exclude only exact guarded GOLD source-path
    contributions, preserving independent genera and all source observations. Exact
    target habitatmech:GOLD.c859639497. Other identity, status and mapping findings
    remain separate."}]}'
  snapshot_sha256: 3b09220a9e491b0625867635e0a66a56d337b5c9db8f4b98acfd614a8c953873
- evidence_id: EPREV
  kind: prior_review
  reference: reviews/structured/20261016T073707Z-cuticle__9784f327-record/review.yaml
  locator: Every immutable baseline finding
  accessed_at: '2026-10-16T09:00:35Z'
  support: supports
  summary: Exact predecessor keys and findings reconciled; the original inspected
    source scope is preserved.
  snapshot_sha256: acc2dbccac24b7bb83bb77fdd684e46cf086522ffcdea3fe802e5180af4f86c7
- evidence_id: ETEST
  kind: record_content
  reference: tests/test_cuticle_dental_review_repairs.py
  locator: Complete full-corpus counterfactual
  accessed_at: '2026-10-16T09:00:35Z'
  support: supports
  summary: Exactly ten records differ. Only guarded context-parent removal and three
    arthropod grounding/predicate/status corrections change scientific fields; all
    source observations and unrelated fields are invariant.
  snapshot_sha256: bfa65736cdf7252a34180b268b0e56e4ef25970cf3308b0f84658f3f731b6ed5
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Strict hierarchy, ITEM decisions and source units
  accessed_at: '2026-10-16T09:00:35Z'
  support: supports
  summary: Native history/status follows maintained rows; generated artifacts are
    not hand-edited.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: EH40
  kind: record_content
  reference: history/mappings/cuticle_dental_review_citations/2026-10-16T083223Z-codex-gpt-5-c42651.yaml
  locator: Complete session event
  accessed_at: '2026-10-16T09:00:35Z'
  support: supports
  summary: Authorized curation by codex-gpt-5; maintained owner and issue retained.
  snapshot_sha256: f0a7f6577764a3dc69c894b8c6dffc7cac78a08a1d7f9f8a4c990bf6d9382a0e
- evidence_id: EH41
  kind: record_content
  reference: history/mappings/cuticle_dental_review_mineral/2026-10-16T074759Z-codex-gpt-5-d2d9db.yaml
  locator: Complete session event
  accessed_at: '2026-10-16T09:00:35Z'
  support: supports
  summary: Authorized curation by codex-gpt-5; maintained owner and issue retained.
  snapshot_sha256: b2d4696ff2e86b972d0083c191362137f20c3c1c9e6a1b1d8f23c0051d03c3fa
- evidence_id: EH42
  kind: record_content
  reference: history/mappings/cuticle_dental_review_parents/2026-10-16T074758Z-codex-gpt-5-56d722.yaml
  locator: Complete session event
  accessed_at: '2026-10-16T09:00:35Z'
  support: supports
  summary: Authorized curation by codex-gpt-5; maintained owner and issue retained.
  snapshot_sha256: 557e55252578fe0c8d3d92eb3054ae15a96973790ef9048f0b9cdbdd90af98cd
- evidence_id: EPARENTS
  kind: record_content
  reference: curation/gold_parent_exclusions.tsv
  locator: Exact physical TSV rows
  accessed_at: '2026-10-16T09:00:36Z'
  support: supports
  summary: '[[7, "habitatmech:GOLD.c859639497\tHost-associated > Arthropoda: Crustaceans
    > Integumentary system > Cuticle\thabitatmech:GOLD.dd76069e56\tcodex-gpt-5\t2026-10-16\tReview
    https://github.com/CultureBotAI/HabitatMech/issues/2235 : Maxillary gland is not
    the entire excretory system; cud is not the stomach; cuticle is not the whole
    integument, integumentary system or skin; abscess, calculus and plaque are not
    the whole oral cavity. Exclude only exact guarded GOLD source-path contributions,
    preserving independent genera and all source observations. Exact target habitatmech:GOLD.c859639497.
    Other identity, status and mapping findings remain separate."]]'
  snapshot_sha256: 1675ec9acca1f4fe6b1101188aafbc10f3cf6d2fabfd149232ec0260262a311f
- evidence_id: EDECISION
  kind: record_content
  reference: curation/decisions.tsv
  locator: Exact physical TSV rows
  accessed_at: '2026-10-16T09:00:37Z'
  support: supports
  summary: '[[4, "habitatmech:GOLD.c859639497\tCONFIRM_UNGROUNDED\t\t\t\tcodex-gpt-5\t2026-10-16\tITEM
    reassessment https://github.com/CultureBotAI/HabitatMech/issues/2236 : UBERON:0001002
    explicitly restricts cuticle to non-mineral coverings, whereas this unrestricted
    host-group source includes mineralized examples (https://pubmed.ncbi.nlm.nih.gov/15670859/
    for millipedes; https://pubmed.ncbi.nlm.nih.gov/18550385/ for isopods). Retain
    the source mint UNGROUNDED pending a verified genus or upstream definition repair;
    this is not proof that no suitable ontology term exists. Preserve all source observations.
    Whole-organ context is excluded separately. Path: Host-associated > Arthropoda:
    Crustaceans > Integumentary system > Cuticle\tITEM\t\tparent"]]'
  snapshot_sha256: bd080045e44f1995788c20df1ea1e71e3fe8d2dc44a3730f8618c8f133e2341a
assessments:
- assessment_id: A1
  area: consistency
  topic: Bounded correction and exact preservation
  outcome: supported
  summary: Removed the guarded GOLD context-parent contribution. The unrestricted
    arthropod cuticle source retains its mint UNGROUNDED/REVIEWED without a non-mineral
    genus or narrow mapping. Source observations and independent valid genera are
    preserved. No unresolved predecessor finding remains in this target scope.
  target_ids:
  - habitatmech:GOLD.c859639497
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
- assessment_id: A2
  area: identity
  topic: Current anatomical identity and hierarchy
  outcome: supported
  summary: 'habitatmech:GOLD.c859639497: Cuticle; UNGROUNDED/REVIEWED; parents [].
    Source anatomy/material scope remains as assessed in the baseline; only the documented
    false parents are removed. No replacement identity, genus or definition is fabricated.'
  target_ids:
  - habitatmech:GOLD.c859639497
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
- assessment_id: A3
  area: quantity
  topic: Units, counts and observations
  outcome: supported
  summary: '[{"source": "GOLD", "source_id": "gold.ecosystem:8187", "source_label":
    "Cuticle", "source_path": "Host-associated > Arthropoda: Crustaceans > Integumentary
    system > Cuticle", "notes": "2 GOLD ecosystem node ids share this path; first
    shown. See data/raw/gold_ecosystem_paths.tsv."}]. Original counts/units, taxa,
    scores and parameters are preserved, not interpreted as prevalence or viability.'
  target_ids:
  - habitatmech:GOLD.c859639497
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
- assessment_id: A4
  area: representation
  topic: Predecessor reconciliation
  outcome: supported
  summary: 'Every previous finding keeps its stable issue key and exact lineage. Removing
    three unsupported narrow matches does not resolve global mapping contract #1398.'
  target_ids:
  - habitatmech:GOLD.c859639497
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
- assessment_id: A5
  area: completeness
  topic: Evidence and lifecycle boundaries
  outcome: supported
  summary: Only the three explicit arthropod ITEM decisions change native status.
    Optional definitions, causal mechanisms and biological absence claims are not
    invented. The complete target, remaining parents, history and original evidence
    were rechecked.
  target_ids:
  - habitatmech:GOLD.c859639497
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
findings:
- finding_id: F1
  issue_key: cuticle--9784f327-context-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Source context is not a strictly broader habitat class
  description: Removed only the guarded GOLD source-context contribution habitatmech:GOLD.dd76069e56.
    Independent valid parents and every source observation remain intact.
  target_ids:
  - habitatmech:GOLD.c859639497
  field_paths:
  - parent_habitats
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
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
  - https://github.com/CultureBotAI/HabitatMech/issues/2235
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T073707Z-cuticle__9784f327-record
    finding_id: F1
  disposition_reason: Removed only the guarded GOLD source-context contribution habitatmech:GOLD.dd76069e56.
    Independent valid parents and every source observation remain intact.
- finding_id: F2
  issue_key: cuticle--9784f327-mapping-endpoint-contract
  category: representation
  severity: major
  status: resolved
  certainty: confirmed
  title: Mapping comparison uses an undeclared ontology-parent endpoint
  description: 'An explicit ITEM decision preserves this unrestricted arthropod source
    mint UNGROUNDED without the non-mineral genus or narrow mapping. This resolves
    only this scoped witness, not global #1398 or the upstream cuticle definition.'
  target_ids:
  - habitatmech:GOLD.c859639497
  field_paths:
  - source_attestations[0].mapping_predicate
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
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
  - https://github.com/CultureBotAI/HabitatMech/issues/2236
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T073707Z-cuticle__9784f327-record
    finding_id: F2
  disposition_reason: 'An explicit ITEM decision preserves this unrestricted arthropod
    source mint UNGROUNDED without the non-mineral genus or narrow mapping. This resolves
    only this scoped witness, not global #1398 or the upstream cuticle definition.'
- finding_id: F3
  issue_key: cuticle--9784f327-nonmineral-genus-scope
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Non-mineral cuticle definition is not broader than the unrestricted source
  description: 'An explicit ITEM decision preserves this unrestricted arthropod source
    mint UNGROUNDED without the non-mineral genus or narrow mapping. This resolves
    only this scoped witness, not global #1398 or the upstream cuticle definition.'
  target_ids:
  - habitatmech:GOLD.c859639497
  field_paths:
  - parent_habitats
  - grounding_status
  evidence_ids:
  - EX9
  - EX10
  - EX11
  - EX12
  - EX13
  - EAFTER
  - EPREV
  - ETEST
  - ERULE
  - EH40
  - EH41
  - EH42
  - EPARENTS
  - EDECISION
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Maintained input or generator; never hand-edit generated habitat YAML
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/extract.py
    role: Maintained input or generator; never hand-edit generated habitat YAML
  rule_id: docs/CURATION.md and native field-by-field review checklist
  native_severity: major
  normalization_reason: Material hierarchy, grounding, representation or pair-evidence
    mismatch. Source reproduction alone does not establish scientific support.
  external_issues:
  - https://github.com/CultureBotAI/HabitatMech/issues/2236
  previous_occurrences:
  - repository: CultureBotAI/HabitatMech
    review_id: 20261016T073707Z-cuticle__9784f327-record
    finding_id: F3
  disposition_reason: 'An explicit ITEM decision preserves this unrestricted arthropod
    source mint UNGROUNDED without the non-mineral genus or narrow mapping. This resolves
    only this scoped witness, not global #1398 or the upstream cuticle definition.'
actions: []
limitations:
- Original specimen-level evidence was not exhaustively reconstructed. Source counts,
  associations and scores do not establish prevalence, viability or characteristic
  presence.
- Configured id-label validation skips 2063 no-adapter pairs; the 18 displayed target
  TaxIds were separately checked against current NCBI.
- 'iModulonDB is not applicable: these records assert no genes, regulators, pathways
  or expression modules. Literature mechanisms were not imported as causal graphs.'
- UNGROUNDED means no replacement identity or genus was verified in this bounded repair,
  not proof that no suitable term exists. The generator boilerplate claiming no ontology
  term fits must be read with the explicit qualification in the ITEM notes. Upstream
  cuticle definition refinement and alternative genera remain future work.
- Same-agent disposition, not independent human approval. Final-head and merge-queue
  checks remain separate publication gates. Whole-corpus scientific review and current
  kg-microbe export conformance are incomplete.
notes:
- All earlier saved bundles and session histories remain unchanged. Preserve the exact
  off-main input base with an annotated provenance tag before squash merge and branch
  deletion.
- 'A preliminary unsaved capture at b3b87caf3d56b74891036c9d3c1c201f07388c63 was retained
  separately. CI #2240 required publication URLs instead of PMID CURIEs in three decision
  notes; after that formatting correction and regeneration, inputs were freshly captured
  and the complete targets reassessed. No prior saved review was refreshed or rewritten.'
tags:
- individual-scientific-review
- host-associated
related_reviews:
- repository: CultureBotAI/HabitatMech
  review_id: 20261016T073707Z-cuticle__9784f327-record
  relationship: Exact predecessor; every finding explicitly reconciled.
```
