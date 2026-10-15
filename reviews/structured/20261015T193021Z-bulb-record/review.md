# Record review: bulb (BTO:0000159)

- Review: 20261015T193021Z-bulb-record
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-15T19:05:24Z
- Finished UTC: 2026-10-15T19:30:21Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

BTO bulb denotes a short underground stem with overlapping leaves, not an elongated rhizome. The merged GOLD and PREGO source meanings are coherent at the bulb identity, and the primary Wigar10 paper explicitly reports isolation from a surface-sterilized garlic bulb. Preserve three GOLD ORGANISM assertions separately from one PREGO TAXON association. The inherited Rhizome superclass is unsupported; BTO plant-structure parentage is not removed by that correction.

## Scope And Provenance

Full field-by-field scientific assessment of this exact target at a073f8e821a7c095f35501982930cc5a156835c0.

Selection: One of the next 24 path-ordered unreviewed identifiers in an ignored-inclusive 3208-record census. This bundle reviews one identifier, not a sample standing for other targets.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base a073f8e821a7c095f35501982930cc5a156835c0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| BTO:0000159 | data/habitats/host_associated/bulb.yaml | generated | bulb |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | BTO:0000159 | Finished 2026-10-15T19:09:15Z. No issues found<br> uv run linkml-validate -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bulb.yaml |
| validate-strict | passed | True | BTO:0000159 | Finished 2026-10-15T19:10:07Z. uv run python scripts/validate_strict.py data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml<br>Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      24<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                reports/instance_validation_failures.tsv |
| validate-history | passed | True | BTO:0000159 | Finished 2026-10-15T19:10:18Z. No issues found<br>816 history record(s) valid against src/habitatmech/schema/history.yaml |
| provenance-check | passed | True | BTO:0000159 | Finished 2026-10-15T19:10:19Z. provenance current: 14 committed inventories, 2 GOLD sources<br> uv run python scripts/check_provenance.py |
| verify-corpus | passed | True | BTO:0000159 | Finished 2026-10-15T19:10:38Z. expected 3208 records, found 3208 on disk<br>  missing:   0<br>  extra:     0<br>  differing: 0<br><br>corpus reproduces exactly from data/raw/<br> uv run python scripts/verify_corpus.py |
| validate-causal-all | passed | True | BTO:0000159 | Finished 2026-10-15T19:10:44Z. validated 32 causal-graph curation file(s) with 32 graph(s)<br> uv run python scripts/validate_causal_graph_curations.py |
| term-requests-check | passed | True | BTO:0000159 | Finished 2026-10-15T19:11:04Z. term-request table is current (110 terms)<br> uv run python scripts/build_term_requests.py --check |
| validate-products | passed | True | BTO:0000159 | Finished 2026-10-15T19:12:07Z. id↔label correspondence summary:<br>          OK_CANONICAL: 1174<br>            OK_SYNONYM: 1<br>          OK_EXCEPTION: 5<br>    SKIPPED_NO_ADAPTER: 2061<br><br>✅ All id↔label pairs correspond.<br> uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml |
| Exact-baseline full QC | passed | True | BTO:0000159 | Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592 |

## Scientific And Domain Assessments

### Identity, definition, category and broader ancestry

identity: concern. Targets: BTO:0000159.

BTO bulb denotes a short underground stem with overlapping leaves, not an elongated rhizome. The merged GOLD and PREGO source meanings are coherent at the bulb identity, and the primary Wigar10 paper explicitly reports isolation from a surface-sterilized garlic bulb. Preserve three GOLD ORGANISM assertions separately from one PREGO TAXON association. The inherited Rhizome superclass is unsupported; BTO plant-structure parentage is not removed by that correction.

### Source counts, units, ranks, pools and channels

quantity: supported. Targets: BTO:0000159.

Every attestation and displayed taxon was compared with its exact frozen source row. [{"source": "GOLD", "count": 3, "unit": "ORGANISM"}, {"source": "PREGO", "count": 1, "unit": "TAXON"}]. Side-table biosamples and study memberships are separate from tree ORGANISM counts; zero-count omission is not biological absence.

### Biological support and limits

evidence: supported. Targets: BTO:0000159.

BTO bulb denotes a short underground stem with overlapping leaves, not an elongated rhizome. The merged GOLD and PREGO source meanings are coherent at the bulb identity, and the primary Wigar10 paper explicitly reports isolation from a surface-sterilized garlic bulb. Preserve three GOLD ORGANISM assertions separately from one PREGO TAXON association. The inherited Rhizome superclass is unsupported; BTO plant-structure parentage is not removed by that correction.

### Curation status, parameters, mechanisms and optional content

completeness: supported. Targets: BTO:0000159.

Executed routes reproduce EXACT/REVIEWED. No target environmental parameters, causal edges, discussions/datasets or is_characteristic=true assertions are present. Parent-record mechanisms are not inherited. Optional absence and SEEDED status alone are not defects.

### Native deterministic gates

schema: supported. Targets: BTO:0000159.

Ordinary and strict schema, 816 curation histories, provenance, exact 3208-record reproduction, 32 causal overlays, term requests, configured labels and exact-base QC passed. Deterministic fidelity does not establish biological correctness.

## Findings

### F1: GOLD context is not a broader habitat class

major / open / confirmed; issue key: bulb-context-parent.

Exclude only the exact source-path/expected-parent contribution BTO:0001181. BTO bulb denotes a short underground stem with overlapping leaves, not an elongated rhizome. The merged GOLD and PREGO source meanings are coherent at the bulb identity, and the primary Wigar10 paper explicitly reports isolation from a surface-sterilized garlic bulb. Preserve three GOLD ORGANISM assertions separately from one PREGO TAXON association. The inherited Rhizome superclass is unsupported; BTO plant-structure parentage is not removed by that correction. Preserve independent valid ontology genera and raw provenance.

## Recommended Actions And Acceptance Checks

### ACT1

Exclude only the exact source-path/expected-parent contribution BTO:0001181. BTO bulb denotes a short underground stem with overlapping leaves, not an elongated rhizome. The merged GOLD and PREGO source meanings are coherent at the bulb identity, and the primary Wigar10 paper explicitly reports isolation from a surface-sterilized garlic bulb. Preserve three GOLD ORGANISM assertions separately from one PREGO TAXON association. The inherited Rhizome superclass is unsupported; BTO plant-structure parentage is not removed by that correction. Preserve independent valid ontology genera and raw provenance. No repair is performed by this review.

- Regress the exact reported claim and preserve independent identities, source totals/units and raw provenance. Change mapping or native status only when separately supported by the item assessment; never alter source counts by hand.
- Append the authorized curation history and require schema, strict, provenance, history, corpus, label, site and full QC gates.
- Reassess the changed record in an immutable successor retaining this issue key and exact predecessor lineage.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E1 | data/habitats/host_associated/bulb.yaml; Entire target YAML | supports | All fields, displayed taxa and complete curation history read. |
| ERULE | docs/CURATION.md; Identity, hierarchy and source-evidence rules | supports | All parent contributions must be strictly broader; host identity is not environment identity. Source occurrences are not automatically characteristic. |
| ESCHEMA | src/habitatmech/schema/habitatmech.yaml; HabitatRecord, SourceAttestation, TaxonAssociation and category enums | supports | Source-to-record mapping endpoints; reported associations versus characteristic assertions; category scope and optional fields. |
| ESEED | src/habitatmech/seed.py; Executed resolution routes, parent accumulation, prefix category and overrides | supports | Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:GOLD.9def37c9a4", "automatic": {"identifier": "BTO:0000159", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "gold_leaf_label", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000159", "grounding_status": "EXACT", "mapping_predicate": "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_gold_leaf_label", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:GOLD.9def37c9a4", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}, {"mint": "habitatmech:PREGO.3c0b2b9d8e", "automatic": {"identifier": "BTO:0000159", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "prego_self_grounded", "category": null, "reviewed": false, "decision": null}, "final": {"identifier": "BTO:0000159", "grounding_status": "EXACT", "mapping_predicate": null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route": "curated_review_of_prego_self_grounded", "category": null, "reviewed": true, "decision": {"identifier": "habitatmech:PREGO.3c0b2b9d8e", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": "parent"}}}] |
| EEXTRACT | src/habitatmech/extract.py; Inventory projection | supports | Counts/units and taxon ranks/scores preserve source meanings. PREGO projections omit original pair-level citation links. |
| ET5 | data/raw/gold_ecosystem_paths.tsv; Physical TSV rows 768 | supports | [{"row": 768, "data": {"canonical_path": "Host-associated &gt; Plants &gt; Rhizome &gt; Bulb", "ecosystem": "Host-associated", "ecosystem_category": "Plants", "ecosystem_type": "Rhizome", "ecosystem_subtype": "Bulb", "specific_ecosystem": "", "leaf_label": "Bulb", "depth": "4", "gold_node_count": "2", "organism_count": "3", "study_count": "0", "biosample_count": "0", "total_assertions": "3", "gold_node_ids": "gold.ecosystem:5415&#124;gold.ecosystem:5416"}}] |
| ET6 | data/raw/prego_habitat_taxa.tsv; Physical TSV rows 213 | supports | [{"row": 213, "data": {"prego_id": "BTO:0000159", "rank": "1", "taxon_id": "NCBITaxon:1085628", "taxon_label": "Streptomyces sp. Wigar10", "prego_score": "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by": ""}}] |
| ET7 | data/raw/prego_habitats.tsv; Physical TSV rows 537 | supports | [{"row": 537, "data": {"prego_id": "BTO:0000159", "ontology": "BTO", "biolink_category": "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count": "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms": "bulb"}}] |
| ET8 | data/raw/gold_path_biosamples.tsv; Physical TSV rows 864 | supports | [{"row": 864, "data": {"canonical_path": "Host-associated &gt; Plants &gt; Rhizome &gt; Bulb", "ecosystem_path_id": "5416", "biosample_count": "3"}}] |
| ET9 | data/raw/gold_studies.tsv; Physical TSV rows 3207 | supports | [{"row": 3207, "data": {"study_gold_id": "Gs0150386", "path_count": "2", "paths": "Host-associated &gt; Plants &gt; Rhizome &gt; Bulb&#124;Host-associated &gt; Plants &gt; Rhizome &gt; Stem tuber"}}] |
| ET10 | data/raw/ontology_subclass_edges.tsv; Physical TSV rows 112,462 | supports | [{"row": 112, "data": {"subject": "BTO:0000159", "predicate": "rdfs:subClassOf", "object": "BTO:0000720"}}, {"row": 462, "data": {"subject": "BTO:0000720", "predicate": "rdfs:subClassOf", "object": "BTO:0001461"}}] |
| ET11 | data/raw/ontology_terms.tsv; Physical TSV rows 161,721,1182 | supports | [{"row": 161, "data": {"term_id": "BTO:0000159", "ontology": "BTO", "label": "bulb", "definition": "A resting stage of a plant (as the lily, onion, hyacinth, or tulip) that is usually formed underground and consists of a short stem base bearing one or more buds enclosed in overlapping membranous or fleshy leaves.", "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only": "FALSE"}}, {"row": 721, "data": {"term_id": "BTO:0000720", "ontology": "BTO", "label": "plant form", "definition": "", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}, {"row": 1182, "data": {"term_id": "BTO:0001181", "ontology": "BTO", "label": "rhizome", "definition": "A somewhat elongate usually horizontal subterranean plant stem that is often thickened by deposits of reserve food material, produces shoots above and roots below, and is distinguished from a true root in possessing buds, nodes, and usually scalelike leaves.", "synonyms": "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}] |
| ET12 | curation/decisions.tsv; Physical TSV rows 926,1433 | supports | [{"row": 926, "data": {"identifier": "habitatmech:GOLD.9def37c9a4", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": ""}}, {"row": 1433, "data": {"identifier": "habitatmech:PREGO.3c0b2b9d8e", "decision": "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "review_depth": "ITEM", "category": "", "relation": ""}}] |
| EP13 | data/habitats/host_associated/rhizome.yaml; Entire immediate parent record; context only | supports | {"identifier": "BTO:0001181", "label": "rhizome", "definition": "A somewhat elongate usually horizontal subterranean plant stem that is often thickened by deposits of reserve food material, produces shoots above and roots below, and is distinguished from a true root in possessing buds, nodes, and usually scalelike leaves.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status": "EXACT", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001001"], "source_attestations": [{"source": "GOLD", "source_id": "gold.ecosystem:3607", "source_label": "Rhizome", "source_path": "Host-associated &gt; Plants &gt; Rhizome", "mapping_predicate": "skos:exactMatch", "assertion_count": 130, "assertion_unit": "ORGANISM", "notes": "3 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}], "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources", "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories; attested by GOLD. Grounding: EXACT."}]} |
| ELEGACY | reports/yaml_record_review/20261002T210446Z-bulb.md; Findings and recommended edits; historical review lead | supports | The earlier no-edit recommendation is not adopted for the inherited Rhizome parent. Valid merged bulb identity and primary Wigar10 support are retained. |
| EX1 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000159/graph; BTO_0000159-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000159", "target": "http://purl.obolibrary.org/obo/BTO_0000720", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX2 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000159; BTO_0000159.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "BTO:0000159", "label": "bulb", "is_obsolete": false, "description": ["A resting stage of a plant (as the lily, onion, hyacinth, or tulip) that is usually formed underground and consists of a short stem base bearing one or more buds enclosed in overlapping membranous or fleshy leaves."]} |
| EX3 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000720/graph; BTO_0000720-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000720", "target": "http://purl.obolibrary.org/obo/BTO_0001461", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}] |
| EX4 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000720; BTO_0000720.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "BTO:0000720", "label": "plant form", "is_obsolete": false, "description": []} |
| EX5 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001181/graph; BTO_0001181-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001181", "target": "http://purl.obolibrary.org/obo/BTO_0001300", "uri": "http://purl.obolibrary.org/obo/RO_0002202", "label": "develops from"}] |
| EX6 | https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001181; BTO_0001181.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "BTO:0001181", "label": "rhizome", "is_obsolete": false, "description": ["A somewhat elongate usually horizontal subterranean plant stem that is often thickened by deposits of reserve food material, produces shoots above and roots below, and is distinguished from a true root in possessing buds, nodes, and usually scalelike leaves."]} |
| EX7 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001/graph; ENVO_01001001-graph.json | context_only | Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001001", "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001001", "target": "http://purl.obolibrary.org/obo/NCBITaxon_33090", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}] |
| EX8 | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001; ENVO_01001001.json | context_only | Current authoritative identity, active status and definition: {"obo_id": "ENVO:01001001", "label": "plant-associated environment", "is_obsolete": false, "description": ["An environmental system determined by a green plant."]} |
| EX9 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=3232846; PMC3232846-ncbi.xml | context_only | Primary abstract PMID:22123757, DOI:10.1128/JB.06257-11. Wigar10 was isolated from a surface-sterilized garlic bulb, Allium sativum var. Purple Stripe. Supports bulb association, not rhizome identity. NCBI XML is metadata/abstract only. |
| EX10 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML; PMC8879827.xml | context_only | Primary methods section 2.3, PMID:35208748, DOI:10.3390/microorganisms10020293. BioProject-assigned taxa are associated with entities mined from linked abstracts at score three. This source channel does not certify natural isolation, viability, prevalence or characteristic presence. |
| EX11 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=100469,1015,108028,1085628,1159213,1163745,1205679,131109,131112,1329,1330043,1334,1392869,1417985,155085,1580,1661,170187,1719,184914,1872627,1962667,197,2,206,243265,243273,28080,28091,28121,28188,283734,28450,28898,29419,317010,326522,33,34,35,38,388919,398527,52770,54,554290,557433,56,562,590061,694433,71864,722,731,753,754,759,75985,760,82806,83456,83462,85336,85401,90240,99807&amp;retmode=xml; taxonomy.xml | context_only | Current NCBI TaxIds, names and source-label comparison: [{"id": "NCBITaxon:1085628", "source": "PREGO", "label": "Streptomyces sp. Wigar10", "current_id": "1085628", "current_name": "Streptomyces sp. Wigar10", "rank": "species", "direct_match": true, "recognized_alias": true}] |
| ESEARCH | Maintained inputs and local structured archive; rg --no-ignore --hidden -l -F -e BTO:0000159 -e bulb -e bulb -e habitatmech:GOLD.9def37c9a4 -e habitatmech:PREGO.3c0b2b9d8e curation history research reports data/raw build reviews | context_only | Exact source/curation rows were parsed separately. No formal target predecessor was found; not every broad label match was inspected. |
| EAVAIL | Configured kg-microbe checkout; find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe -type f -path '*/prego/*' -name '*.tsv' | context_only | No prego-directory TSV files were found in this checkout. Original pair-level citation exports remain unavailable; this is not a global absence claim. |

## Limits And Additional Notes

- Original specimens and every pair-level source citation have not been independently reidentified. Source counts and ranks are not prevalence, viability, or characteristic presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities were separately checked against current NCBI Taxonomy, not certified by that label gate.
- Full QC evidence is a successful remote run at the exact unchanged scientific input base, not a new local full-QC execution. New review files require a post-save native archive check.
- iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic module or causal mechanism is asserted. No paid research was used.
- Original PREGO pair exports are unavailable in the configured checkout. Primary examples do not prove the provenance or truth of every retained pair. Score three remains the source score, not measured localization confidence.
- Current input hashes were checked against both working bytes and exact tracked base blobs; source.state git_commit explicitly describes that revision.
- Ignored-inclusive searches and the parsed structured archive found no previous structured observation targeting this identifier. Broad label matches are leads, not formal lineage or automatic scientific findings.
- Read-only scientific review: no habitat curation, generation, history/status promotion or GitHub mutation is performed.
- The earlier no-edit recommendation is not adopted for the inherited Rhizome parent. Valid merged bulb identity and primary Wigar10 support are retained.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T193021Z-bulb-record
repository: CultureBotAI/HabitatMech
kind: record
title: 'Record review: bulb (BTO:0000159)'
started_at: '2026-10-15T19:05:24Z'
finished_at: '2026-10-15T19:30:21Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent assesses the record and sources; not independent
    reviewer approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: BTO bulb denotes a short underground stem with overlapping leaves, not an
  elongated rhizome. The merged GOLD and PREGO source meanings are coherent at the
  bulb identity, and the primary Wigar10 paper explicitly reports isolation from a
  surface-sterilized garlic bulb. Preserve three GOLD ORGANISM assertions separately
  from one PREGO TAXON association. The inherited Rhizome superclass is unsupported;
  BTO plant-structure parentage is not removed by that correction.
source:
  git_revision: a073f8e821a7c095f35501982930cc5a156835c0
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
    sha256: 196d393819145d33f30f7706fd9c5369ed05847d2ccbd9b977a759556ca293fd
    role: context
  - path: curation/external_xrefs.tsv
    sha256: f289c938b0c70d6f2bfb231bf137edf1c862bbda9143d9b6eae9e3fdd587703c
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 9344f0bbbad1423ff0e47204ad49bc27ffaf4b5e63841e77e09cc01877b91f54
    role: context
  - path: curation/record_annotation_corrections.tsv
    sha256: a56f07a45fb743fb7b0e61f83ef70fa5ed61a3c892cfaf36e3428967c548dc5e
    role: context
  - path: curation/redirects_retracted.tsv
    sha256: 0f1e9af8881f5a5db19f87de06b3b3d1800cfac8101699b380388c0a1a1e9a19
    role: context
  - path: curation/term_requests.tsv
    sha256: da5dcc7d49a3441bd9ff25d95ff204ba4e8716cf062271338ee2795ca16a5ce4
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
  - path: data/habitats/host_associated/bulb.yaml
    sha256: f2a51f7e17c68a1f01d5415be2aed6f9c98e99feb31cd0229c45532a9f6448a3
    role: target
  - path: data/habitats/host_associated/rhizome.yaml
    sha256: 0a3f2a7dbf58125380cdb120632f3756c5afd3518c925ca587f4317948a4e476
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
  - path: reports/yaml_record_review/20261002T210446Z-bulb.md
    sha256: bfb34ed6e0176b2db1bf0a49410a2320d141231ebeec29f9f9dc98a8aaf9f0f0
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
  - path: src/habitatmech/extract.py
    sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
    role: context
targets:
- target_id: BTO:0000159
  path: data/habitats/host_associated/bulb.yaml
  label: bulb
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
  description: Full field-by-field scientific assessment of this exact target at a073f8e821a7c095f35501982930cc5a156835c0.
  selection: One of the next 24 path-ordered unreviewed identifiers in an ignored-inclusive
    3208-record census. This bundle reviews one identifier, not a sample standing
    for other targets.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - BTO:0000159
  exclusions:
  - target: Other habitats and SSSOM/KGX products
    reason: Parent context is not additional record coverage. Export conformance and
      original individual specimens are not certified.
checks:
- check_id: C1
  name: validate
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate data/habitats/host_associated/bulb.yaml
  exit_code: 0
  target_ids:
  - BTO:0000159
  summary: "Finished 2026-10-15T19:09:15Z. No issues found\n uv run linkml-validate\
    \ -s src/habitatmech/schema/habitatmech.yaml --target-class HabitatRecord data/habitats/host_associated/bulb.yaml"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C2
  name: validate-strict
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-strict
    data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml
    data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml
    data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml
    data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml
    data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml
    data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml
    data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml
    data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml
    data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml
    data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml
    data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml
    data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml
  exit_code: 0
  target_ids:
  - BTO:0000159
  summary: "Finished 2026-10-15T19:10:07Z. uv run python scripts/validate_strict.py\
    \ data/habitats/host_associated/brown_algae.yaml data/habitats/host_associated/bryophytes.yaml\
    \ data/habitats/host_associated/bryozoa.yaml data/habitats/host_associated/bryozoans.yaml\
    \ data/habitats/host_associated/buccal_mucosa.yaml data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml\
    \ data/habitats/host_associated/buccal_mucosa__a90386db.yaml data/habitats/host_associated/buffy_coat.yaml\
    \ data/habitats/host_associated/bulb.yaml data/habitats/host_associated/bursa_of_fabricius.yaml\
    \ data/habitats/host_associated/c1_glandular_saccules.yaml data/habitats/host_associated/c2.yaml\
    \ data/habitats/host_associated/c3.yaml data/habitats/host_associated/caco_2_cell.yaml\
    \ data/habitats/host_associated/caeca.yaml data/habitats/host_associated/caeca__67ed138d.yaml\
    \ data/habitats/host_associated/caeca_bacteriome.yaml data/habitats/host_associated/canidae_dog.yaml\
    \ data/habitats/host_associated/canthus.yaml data/habitats/host_associated/canthus__f4c2e1df.yaml\
    \ data/habitats/host_associated/capillary.yaml data/habitats/host_associated/caprinae_sheep_goat.yaml\
    \ data/habitats/host_associated/carapace.yaml data/habitats/host_associated/carcass.yaml\n\
    Validating 24 files with 15 workers; schema=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/HabitatMech/src/habitatmech/schema/habitatmech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      24\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                reports/instance_validation_failures.tsv"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C3
  name: validate-history
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-history
  exit_code: 0
  target_ids:
  - BTO:0000159
  summary: 'Finished 2026-10-15T19:10:18Z. No issues found

    816 history record(s) valid against src/habitatmech/schema/history.yaml'
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C4
  name: provenance-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just provenance-check
  exit_code: 0
  target_ids:
  - BTO:0000159
  summary: "Finished 2026-10-15T19:10:19Z. provenance current: 14 committed inventories,\
    \ 2 GOLD sources\n uv run python scripts/check_provenance.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C5
  name: verify-corpus
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just verify-corpus
  exit_code: 0
  target_ids:
  - BTO:0000159
  summary: "Finished 2026-10-15T19:10:38Z. expected 3208 records, found 3208 on disk\n\
    \  missing:   0\n  extra:     0\n  differing: 0\n\ncorpus reproduces exactly from\
    \ data/raw/\n uv run python scripts/verify_corpus.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C6
  name: validate-causal-all
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-causal-all
  exit_code: 0
  target_ids:
  - BTO:0000159
  summary: "Finished 2026-10-15T19:10:44Z. validated 32 causal-graph curation file(s)\
    \ with 32 graph(s)\n uv run python scripts/validate_causal_graph_curations.py"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C7
  name: term-requests-check
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just term-requests-check
  exit_code: 0
  target_ids:
  - BTO:0000159
  summary: "Finished 2026-10-15T19:11:04Z. term-request table is current (110 terms)\n\
    \ uv run python scripts/build_term_requests.py --check"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: C8
  name: validate-products
  status: passed
  required: true
  command: UV_CACHE_DIR=/private/tmp/habitatmech-bk-uv-cache just validate-products
  exit_code: 0
  target_ids:
  - BTO:0000159
  summary: "Finished 2026-10-15T19:12:07Z. id↔label correspondence summary:\n    \
    \      OK_CANONICAL: 1174\n            OK_SYNONYM: 1\n          OK_EXCEPTION:\
    \ 5\n    SKIPPED_NO_ADAPTER: 2061\n\n✅ All id↔label pairs correspond.\n uv run\
    \ python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml"
  scope_note: Ordinary schema for this target; strict validation for all 24; other
    commands use documented full-corpus scope.
- check_id: CCI
  name: Exact-baseline full QC
  status: passed
  required: true
  command: gh run view 38786529592 --json status,conclusion,headSha,url,jobs
  exit_code: 0
  target_ids:
  - BTO:0000159
  summary: Verified 2026-10-15T19:04:33Z https://github.com/CultureBotAI/HabitatMech/actions/runs/38786529592
  scope_note: Unchanged scientific input baseline; these new review files are outside
    that remote run.
evidence:
- evidence_id: E1
  kind: record_content
  reference: data/habitats/host_associated/bulb.yaml
  locator: Entire target YAML
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: All fields, displayed taxa and complete curation history read.
  snapshot_sha256: f2a51f7e17c68a1f01d5415be2aed6f9c98e99feb31cd0229c45532a9f6448a3
- evidence_id: ERULE
  kind: authority
  reference: docs/CURATION.md
  locator: Identity, hierarchy and source-evidence rules
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: All parent contributions must be strictly broader; host identity is not
    environment identity. Source occurrences are not automatically characteristic.
  snapshot_sha256: f3f5d3d033fa7e7c1d78571959fc2e62e0b0a625f47dba1413657e8cf944b322
- evidence_id: ESCHEMA
  kind: authority
  reference: src/habitatmech/schema/habitatmech.yaml
  locator: HabitatRecord, SourceAttestation, TaxonAssociation and category enums
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: Source-to-record mapping endpoints; reported associations versus characteristic
    assertions; category scope and optional fields.
  snapshot_sha256: 7e3cda3dadb9c7462498e5014bf38ef730068212f8f9cb131e3fce383c21d10e
- evidence_id: ESEED
  kind: record_content
  reference: src/habitatmech/seed.py
  locator: Executed resolution routes, parent accumulation, prefix category and overrides
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: 'Exact emitted target reproduction established. Routes: [{"mint": "habitatmech:GOLD.9def37c9a4",
    "automatic": {"identifier": "BTO:0000159", "grounding_status": "EXACT", "mapping_predicate":
    "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs":
    [], "route": "gold_leaf_label", "category": null, "reviewed": false, "decision":
    null}, "final": {"identifier": "BTO:0000159", "grounding_status": "EXACT", "mapping_predicate":
    "skos:exactMatch", "contributes_grounding": true, "extra_parents": [], "extra_xrefs":
    [], "route": "curated_review_of_gold_leaf_label", "category": null, "reviewed":
    true, "decision": {"identifier": "habitatmech:GOLD.9def37c9a4", "decision": "REVIEW",
    "object_id": "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5",
    "date": "2026-08-13", "notes": "Multi-source review pass: this record is attested
    by more than one independent vocabulary, and this source''s label or path was
    read against the record''s ontology term to check the merge is right. It agrees.
    Source concepts in the same pass whose labels did not agree were re-decided rather
    than endorsed; see the pass''s other decisions of the same date.", "review_depth":
    "ITEM", "category": "", "relation": "parent"}}}, {"mint": "habitatmech:PREGO.3c0b2b9d8e",
    "automatic": {"identifier": "BTO:0000159", "grounding_status": "EXACT", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "prego_self_grounded", "category": null, "reviewed": false, "decision": null},
    "final": {"identifier": "BTO:0000159", "grounding_status": "EXACT", "mapping_predicate":
    null, "contributes_grounding": true, "extra_parents": [], "extra_xrefs": [], "route":
    "curated_review_of_prego_self_grounded", "category": null, "reviewed": true, "decision":
    {"identifier": "habitatmech:PREGO.3c0b2b9d8e", "decision": "REVIEW", "object_id":
    "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date":
    "2026-08-13", "notes": "Multi-source review pass: this record is attested by more
    than one independent vocabulary, and this source''s label or path was read against
    the record''s ontology term to check the merge is right. It agrees. Source concepts
    in the same pass whose labels did not agree were re-decided rather than endorsed;
    see the pass''s other decisions of the same date.", "review_depth": "ITEM", "category":
    "", "relation": "parent"}}}]'
  snapshot_sha256: 35ab365591562452b7ce268a3cc8e9b3b0b4461362f2f872c674838dcdb6f021
- evidence_id: EEXTRACT
  kind: record_content
  reference: src/habitatmech/extract.py
  locator: Inventory projection
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: Counts/units and taxon ranks/scores preserve source meanings. PREGO projections
    omit original pair-level citation links.
  snapshot_sha256: 4d9397bda649381a5daf81937369531c6dc8b4518d6c7047e6f3f14e605bf860
- evidence_id: ET5
  kind: database
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Physical TSV rows 768
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: '[{"row": 768, "data": {"canonical_path": "Host-associated > Plants > Rhizome
    > Bulb", "ecosystem": "Host-associated", "ecosystem_category": "Plants", "ecosystem_type":
    "Rhizome", "ecosystem_subtype": "Bulb", "specific_ecosystem": "", "leaf_label":
    "Bulb", "depth": "4", "gold_node_count": "2", "organism_count": "3", "study_count":
    "0", "biosample_count": "0", "total_assertions": "3", "gold_node_ids": "gold.ecosystem:5415|gold.ecosystem:5416"}}]'
  snapshot_sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
- evidence_id: ET6
  kind: database
  reference: data/raw/prego_habitat_taxa.tsv
  locator: Physical TSV rows 213
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: '[{"row": 213, "data": {"prego_id": "BTO:0000159", "rank": "1", "taxon_id":
    "NCBITaxon:1085628", "taxon_label": "Streptomyces sp. Wigar10", "prego_score":
    "3", "direct_flag": "TRUE", "channels": "annotated_genomes_isolates", "corroborated_by":
    ""}}]'
  snapshot_sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
- evidence_id: ET7
  kind: database
  reference: data/raw/prego_habitats.tsv
  locator: Physical TSV rows 537
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: '[{"row": 537, "data": {"prego_id": "BTO:0000159", "ontology": "BTO", "biolink_category":
    "biolink:GrossAnatomicalStructure", "taxon_count": "1", "direct_assertion_count":
    "1", "max_prego_score": "3", "channels": "annotated_genomes_isolates", "prego_synonyms":
    "bulb"}}]'
  snapshot_sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
- evidence_id: ET8
  kind: database
  reference: data/raw/gold_path_biosamples.tsv
  locator: Physical TSV rows 864
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: '[{"row": 864, "data": {"canonical_path": "Host-associated > Plants > Rhizome
    > Bulb", "ecosystem_path_id": "5416", "biosample_count": "3"}}]'
  snapshot_sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
- evidence_id: ET9
  kind: database
  reference: data/raw/gold_studies.tsv
  locator: Physical TSV rows 3207
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: '[{"row": 3207, "data": {"study_gold_id": "Gs0150386", "path_count": "2",
    "paths": "Host-associated > Plants > Rhizome > Bulb|Host-associated > Plants >
    Rhizome > Stem tuber"}}]'
  snapshot_sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
- evidence_id: ET10
  kind: database
  reference: data/raw/ontology_subclass_edges.tsv
  locator: Physical TSV rows 112,462
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: '[{"row": 112, "data": {"subject": "BTO:0000159", "predicate": "rdfs:subClassOf",
    "object": "BTO:0000720"}}, {"row": 462, "data": {"subject": "BTO:0000720", "predicate":
    "rdfs:subClassOf", "object": "BTO:0001461"}}]'
  snapshot_sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
- evidence_id: ET11
  kind: database
  reference: data/raw/ontology_terms.tsv
  locator: Physical TSV rows 161,721,1182
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: '[{"row": 161, "data": {"term_id": "BTO:0000159", "ontology": "BTO", "label":
    "bulb", "definition": "A resting stage of a plant (as the lily, onion, hyacinth,
    or tulip) that is usually formed underground and consists of a short stem base
    bearing one or more buds enclosed in overlapping membranous or fleshy leaves.",
    "synonyms": "", "deprecated": "", "directly_referenced": "TRUE", "label_only":
    "FALSE"}}, {"row": 721, "data": {"term_id": "BTO:0000720", "ontology": "BTO",
    "label": "plant form", "definition": "", "synonyms": "", "deprecated": "", "directly_referenced":
    "FALSE", "label_only": "FALSE"}}, {"row": 1182, "data": {"term_id": "BTO:0001181",
    "ontology": "BTO", "label": "rhizome", "definition": "A somewhat elongate usually
    horizontal subterranean plant stem that is often thickened by deposits of reserve
    food material, produces shoots above and roots below, and is distinguished from
    a true root in possessing buds, nodes, and usually scalelike leaves.", "synonyms":
    "", "deprecated": "", "directly_referenced": "FALSE", "label_only": "FALSE"}}]'
  snapshot_sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
- evidence_id: ET12
  kind: database
  reference: curation/decisions.tsv
  locator: Physical TSV rows 926,1433
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: '[{"row": 926, "data": {"identifier": "habitatmech:GOLD.9def37c9a4", "decision":
    "REVIEW", "object_id": "", "object_label": "", "grounding_status": "", "curator":
    "claude-opus-5", "date": "2026-08-13", "notes": "Multi-source review pass: this
    record is attested by more than one independent vocabulary, and this source''s
    label or path was read against the record''s ontology term to check the merge
    is right. It agrees. Source concepts in the same pass whose labels did not agree
    were re-decided rather than endorsed; see the pass''s other decisions of the same
    date.", "review_depth": "ITEM", "category": "", "relation": ""}}, {"row": 1433,
    "data": {"identifier": "habitatmech:PREGO.3c0b2b9d8e", "decision": "REVIEW", "object_id":
    "", "object_label": "", "grounding_status": "", "curator": "claude-opus-5", "date":
    "2026-08-13", "notes": "Multi-source review pass: this record is attested by more
    than one independent vocabulary, and this source''s label or path was read against
    the record''s ontology term to check the merge is right. It agrees. Source concepts
    in the same pass whose labels did not agree were re-decided rather than endorsed;
    see the pass''s other decisions of the same date.", "review_depth": "ITEM", "category":
    "", "relation": ""}}]'
  snapshot_sha256: b01c55614780f2eba62e1dc7b47f30d40fb783fe388e75761ca2639769b9c5de
- evidence_id: EP13
  kind: record_content
  reference: data/habitats/host_associated/rhizome.yaml
  locator: Entire immediate parent record; context only
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: '{"identifier": "BTO:0001181", "label": "rhizome", "definition": "A somewhat
    elongate usually horizontal subterranean plant stem that is often thickened by
    deposits of reserve food material, produces shoots above and roots below, and
    is distinguished from a true root in possessing buds, nodes, and usually scalelike
    leaves.", "definition_source": "BTO", "habitat_category": "HOST_ASSOCIATED", "grounding_status":
    "EXACT", "mapping_status": "SEEDED", "parent_habitats": ["ENVO:01001001"], "source_attestations":
    [{"source": "GOLD", "source_id": "gold.ecosystem:3607", "source_label": "Rhizome",
    "source_path": "Host-associated > Plants > Rhizome", "mapping_predicate": "skos:exactMatch",
    "assertion_count": 130, "assertion_unit": "ORGANISM", "notes": "3 GOLD ecosystem
    node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}],
    "curation_history": [{"timestamp": "2026-08-16T05:58:02Z", "curator": "seed_from_sources",
    "action": "SEEDED_FROM_SOURCES", "changes": "Seeded from data/raw/ inventories;
    attested by GOLD. Grounding: EXACT."}]}'
  snapshot_sha256: 0a3f2a7dbf58125380cdb120632f3756c5afd3518c925ca587f4317948a4e476
- evidence_id: ELEGACY
  kind: record_content
  reference: reports/yaml_record_review/20261002T210446Z-bulb.md
  locator: Findings and recommended edits; historical review lead
  accessed_at: '2026-10-15T19:30:21Z'
  support: supports
  summary: The earlier no-edit recommendation is not adopted for the inherited Rhizome
    parent. Valid merged bulb identity and primary Wigar10 support are retained.
  snapshot_sha256: bfb34ed6e0176b2db1bf0a49410a2320d141231ebeec29f9f9dc98a8aaf9f0f0
- evidence_id: EX1
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000159/graph
  locator: BTO_0000159-graph.json
  accessed_at: '2026-10-15T19:05:49Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000159",
    "target": "http://purl.obolibrary.org/obo/BTO_0000720", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: 094e2ef021262447e81788b8f33e45262fbcf7b3db6686b555f6bb020162c215
- evidence_id: EX2
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000159
  locator: BTO_0000159.json
  accessed_at: '2026-10-15T19:05:48Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "BTO:0000159", "label": "bulb", "is_obsolete": false, "description": ["A resting
    stage of a plant (as the lily, onion, hyacinth, or tulip) that is usually formed
    underground and consists of a short stem base bearing one or more buds enclosed
    in overlapping membranous or fleshy leaves."]}'
  snapshot_sha256: e95ea84c7abeb329b22c0843c8890bd9406b4c7cf73875a0a7c77934c0a95d12
- evidence_id: EX3
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000720/graph
  locator: BTO_0000720-graph.json
  accessed_at: '2026-10-15T19:05:55Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0000720",
    "target": "http://purl.obolibrary.org/obo/BTO_0001461", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}]'
  snapshot_sha256: d889ce20493ec130704d493e2770784f93c44635ad0a41acdee59f0de6f09810
- evidence_id: EX4
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0000720
  locator: BTO_0000720.json
  accessed_at: '2026-10-15T19:05:54Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "BTO:0000720", "label": "plant form", "is_obsolete": false, "description": []}'
  snapshot_sha256: 1a368f9628632f52dbe5b17817809c10b1cf5e89c45ce13e54faa0b1b636dc5a
- evidence_id: EX5
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001181/graph
  locator: BTO_0001181-graph.json
  accessed_at: '2026-10-15T19:05:58Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/BTO_0001181",
    "target": "http://purl.obolibrary.org/obo/BTO_0001300", "uri": "http://purl.obolibrary.org/obo/RO_0002202",
    "label": "develops from"}]'
  snapshot_sha256: 0531c4eb1311151235412aae1b45add875019eeaafa534d222cbac1780658463
- evidence_id: EX6
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001181
  locator: BTO_0001181.json
  accessed_at: '2026-10-15T19:05:57Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "BTO:0001181", "label": "rhizome", "is_obsolete": false, "description": ["A somewhat
    elongate usually horizontal subterranean plant stem that is often thickened by
    deposits of reserve food material, produces shoots above and roots below, and
    is distinguished from a true root in possessing buds, nodes, and usually scalelike
    leaves."]}'
  snapshot_sha256: 04142f984a47d9a8a04f401793999b36417d080f40c00168b502086a4d406803
- evidence_id: EX7
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001/graph
  locator: ENVO_01001001-graph.json
  accessed_at: '2026-10-15T19:06:13Z'
  support: context_only
  summary: 'Typed outgoing ontology edges: [{"source": "http://purl.obolibrary.org/obo/ENVO_01001001",
    "target": "http://purl.obolibrary.org/obo/ENVO_01001000", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/ENVO_01001001",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_33090", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}]'
  snapshot_sha256: 43b7f7cee8e27c64685cea0193012a2cc71851b91d19a2a7052fa1e6548a6a71
- evidence_id: EX8
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FENVO_01001001
  locator: ENVO_01001001.json
  accessed_at: '2026-10-15T19:06:12Z'
  support: context_only
  summary: 'Current authoritative identity, active status and definition: {"obo_id":
    "ENVO:01001001", "label": "plant-associated environment", "is_obsolete": false,
    "description": ["An environmental system determined by a green plant."]}'
  snapshot_sha256: b1623e2f33257c2fadc5bf06670bcc7e95384c210301e901f7faa8059c5ed815
- evidence_id: EX9
  kind: primary_source
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3232846
  locator: PMC3232846-ncbi.xml
  accessed_at: '2026-10-15T19:19:51Z'
  support: context_only
  summary: Primary abstract PMID:22123757, DOI:10.1128/JB.06257-11. Wigar10 was isolated
    from a surface-sterilized garlic bulb, Allium sativum var. Purple Stripe. Supports
    bulb association, not rhizome identity. NCBI XML is metadata/abstract only.
  snapshot_sha256: 1a21e455bec39c6d3c84c2f96d80030527e37ce803cd2adb5fb147a622a8dbd8
- evidence_id: EX10
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8879827/fullTextXML
  locator: PMC8879827.xml
  accessed_at: '2026-10-15T19:19:06Z'
  support: context_only
  summary: Primary methods section 2.3, PMID:35208748, DOI:10.3390/microorganisms10020293.
    BioProject-assigned taxa are associated with entities mined from linked abstracts
    at score three. This source channel does not certify natural isolation, viability,
    prevalence or characteristic presence.
  snapshot_sha256: 375f0fde4d07bb823cb9106aa4567bc0ef03c2866af0b2a7740b543f50687c25
- evidence_id: EX11
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=100469,1015,108028,1085628,1159213,1163745,1205679,131109,131112,1329,1330043,1334,1392869,1417985,155085,1580,1661,170187,1719,184914,1872627,1962667,197,2,206,243265,243273,28080,28091,28121,28188,283734,28450,28898,29419,317010,326522,33,34,35,38,388919,398527,52770,54,554290,557433,56,562,590061,694433,71864,722,731,753,754,759,75985,760,82806,83456,83462,85336,85401,90240,99807&retmode=xml
  locator: taxonomy.xml
  accessed_at: '2026-10-15T19:06:42Z'
  support: context_only
  summary: 'Current NCBI TaxIds, names and source-label comparison: [{"id": "NCBITaxon:1085628",
    "source": "PREGO", "label": "Streptomyces sp. Wigar10", "current_id": "1085628",
    "current_name": "Streptomyces sp. Wigar10", "rank": "species", "direct_match":
    true, "recognized_alias": true}]'
  snapshot_sha256: ea5036b7cc5c9bf152840fae0a470b8f6cb17f89633967069648541712ecf8b2
- evidence_id: ESEARCH
  kind: search
  reference: Maintained inputs and local structured archive
  locator: rg --no-ignore --hidden -l -F -e BTO:0000159 -e bulb -e bulb -e habitatmech:GOLD.9def37c9a4
    -e habitatmech:PREGO.3c0b2b9d8e curation history research reports data/raw build
    reviews
  accessed_at: '2026-10-15T19:05:55Z'
  support: context_only
  summary: Exact source/curation rows were parsed separately. No formal target predecessor
    was found; not every broad label match was inspected.
  search_scope: curation, history, research, reports, data/raw, build and reviews;
    ignored and hidden files included; every structured review.yaml was parsed.
- evidence_id: EAVAIL
  kind: search
  reference: Configured kg-microbe checkout
  locator: find /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe
    -type f -path '*/prego/*' -name '*.tsv'
  accessed_at: '2026-10-15T19:19:24Z'
  support: context_only
  summary: No prego-directory TSV files were found in this checkout. Original pair-level
    citation exports remain unavailable; this is not a global absence claim.
  search_scope: find across the configured checkout, including ignored and hidden
    files.
assessments:
- assessment_id: A1
  area: identity
  topic: Identity, definition, category and broader ancestry
  outcome: concern
  summary: BTO bulb denotes a short underground stem with overlapping leaves, not
    an elongated rhizome. The merged GOLD and PREGO source meanings are coherent at
    the bulb identity, and the primary Wigar10 paper explicitly reports isolation
    from a surface-sterilized garlic bulb. Preserve three GOLD ORGANISM assertions
    separately from one PREGO TAXON association. The inherited Rhizome superclass
    is unsupported; BTO plant-structure parentage is not removed by that correction.
  target_ids:
  - BTO:0000159
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - ET12
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EX11
  dimensions:
  - name: native_status
    value: EXACT/REVIEWED
    definition: Generated grounding and curation status; distinct from this scientific
      review verdict.
    evidence_ids:
    - E1
    - ESEED
- assessment_id: A2
  area: quantity
  topic: Source counts, units, ranks, pools and channels
  outcome: supported
  summary: 'Every attestation and displayed taxon was compared with its exact frozen
    source row. [{"source": "GOLD", "count": 3, "unit": "ORGANISM"}, {"source": "PREGO",
    "count": 1, "unit": "TAXON"}]. Side-table biosamples and study memberships are
    separate from tree ORGANISM counts; zero-count omission is not biological absence.'
  target_ids:
  - BTO:0000159
  evidence_ids:
  - E1
  - EEXTRACT
  - ESEED
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EX11
  dimensions:
  - name: source_assertion_units
    value: '[{"source": "GOLD", "count": 3, "unit": "ORGANISM"}, {"source": "PREGO",
      "count": 1, "unit": "TAXON"}]'
    definition: Frozen source counts with their noninterchangeable units; omitted
      zero GOLD counts are verified in the raw row.
    evidence_ids:
    - E1
    - EEXTRACT
    - ESEED
- assessment_id: A3
  area: evidence
  topic: Biological support and limits
  outcome: supported
  summary: BTO bulb denotes a short underground stem with overlapping leaves, not
    an elongated rhizome. The merged GOLD and PREGO source meanings are coherent at
    the bulb identity, and the primary Wigar10 paper explicitly reports isolation
    from a surface-sterilized garlic bulb. Preserve three GOLD ORGANISM assertions
    separately from one PREGO TAXON association. The inherited Rhizome superclass
    is unsupported; BTO plant-structure parentage is not removed by that correction.
  target_ids:
  - BTO:0000159
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - ET12
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EX11
- assessment_id: A4
  area: completeness
  topic: Curation status, parameters, mechanisms and optional content
  outcome: supported
  summary: Executed routes reproduce EXACT/REVIEWED. No target environmental parameters,
    causal edges, discussions/datasets or is_characteristic=true assertions are present.
    Parent-record mechanisms are not inherited. Optional absence and SEEDED status
    alone are not defects.
  target_ids:
  - BTO:0000159
  evidence_ids:
  - E1
  - ERULE
  - ESEED
- assessment_id: A5
  area: schema
  topic: Native deterministic gates
  outcome: supported
  summary: Ordinary and strict schema, 816 curation histories, provenance, exact 3208-record
    reproduction, 32 causal overlays, term requests, configured labels and exact-base
    QC passed. Deterministic fidelity does not establish biological correctness.
  target_ids:
  - BTO:0000159
  evidence_ids:
  - E1
  - ERULE
findings:
- finding_id: F1
  issue_key: bulb-context-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: GOLD context is not a broader habitat class
  description: Exclude only the exact source-path/expected-parent contribution BTO:0001181.
    BTO bulb denotes a short underground stem with overlapping leaves, not an elongated
    rhizome. The merged GOLD and PREGO source meanings are coherent at the bulb identity,
    and the primary Wigar10 paper explicitly reports isolation from a surface-sterilized
    garlic bulb. Preserve three GOLD ORGANISM assertions separately from one PREGO
    TAXON association. The inherited Rhizome superclass is unsupported; BTO plant-structure
    parentage is not removed by that correction. Preserve independent valid ontology
    genera and raw provenance.
  target_ids:
  - BTO:0000159
  field_paths:
  - parent_habitats
  evidence_ids:
  - E1
  - ERULE
  - ESCHEMA
  - ESEED
  - ET5
  - ET6
  - ET7
  - ET8
  - ET9
  - ET10
  - ET11
  - ET12
  - EX1
  - EX2
  - EX3
  - EX4
  - EX5
  - EX6
  - EX7
  - EX8
  - EX9
  - EX10
  - EX11
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  rule_id: docs/CURATION.md and native record-review checklist
  native_severity: major
  normalization_reason: Materially unsupported semantic or source-evidence claim;
    deterministic validity does not establish scientific support.
  external_issues: []
actions:
- action_id: ACT1
  finding_ids:
  - F1
  target_ids:
  - BTO:0000159
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Maintained input or generator; never patch generated habitat YAML
  description: Exclude only the exact source-path/expected-parent contribution BTO:0001181.
    BTO bulb denotes a short underground stem with overlapping leaves, not an elongated
    rhizome. The merged GOLD and PREGO source meanings are coherent at the bulb identity,
    and the primary Wigar10 paper explicitly reports isolation from a surface-sterilized
    garlic bulb. Preserve three GOLD ORGANISM assertions separately from one PREGO
    TAXON association. The inherited Rhizome superclass is unsupported; BTO plant-structure
    parentage is not removed by that correction. Preserve independent valid ontology
    genera and raw provenance. No repair is performed by this review.
  generator: Controlled source refresh when required, then just seed, guarded just
    seed-canary, just seed-apply, and dependent term-request/map/site/redirect regeneration.
  acceptance_checks:
  - Regress the exact reported claim and preserve independent identities, source totals/units
    and raw provenance. Change mapping or native status only when separately supported
    by the item assessment; never alter source counts by hand.
  - Append the authorized curation history and require schema, strict, provenance,
    history, corpus, label, site and full QC gates.
  - Reassess the changed record in an immutable successor retaining this issue key
    and exact predecessor lineage.
limitations:
- Original specimens and every pair-level source citation have not been independently
  reidentified. Source counts and ranks are not prevalence, viability, or characteristic
  presence.
- The configured label gate skips 2061 no-adapter pairs. Displayed taxon identities
  were separately checked against current NCBI Taxonomy, not certified by that label
  gate.
- Full QC evidence is a successful remote run at the exact unchanged scientific input
  base, not a new local full-QC execution. New review files require a post-save native
  archive check.
- 'iModulonDB is not applicable to these target claims: no gene, regulator, transcriptomic
  module or causal mechanism is asserted. No paid research was used.'
- Original PREGO pair exports are unavailable in the configured checkout. Primary
  examples do not prove the provenance or truth of every retained pair. Score three
  remains the source score, not measured localization confidence.
notes:
- Current input hashes were checked against both working bytes and exact tracked base
  blobs; source.state git_commit explicitly describes that revision.
- Ignored-inclusive searches and the parsed structured archive found no previous structured
  observation targeting this identifier. Broad label matches are leads, not formal
  lineage or automatic scientific findings.
- 'Read-only scientific review: no habitat curation, generation, history/status promotion
  or GitHub mutation is performed.'
- The earlier no-edit recommendation is not adopted for the inherited Rhizome parent.
  Valid merged bulb identity and primary Wigar10 support are retained.
tags:
- individual-scientific-review
- host-associated
```
