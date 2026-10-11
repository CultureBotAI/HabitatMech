# Scientific record review: waste_water

- Review: 20261011T195959Z-waste_water
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-11T19:36:43.237024Z
- Finished UTC: 2026-10-11T19:59:59.611996Z
- Reviewer: OpenAI Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ENVO:00002001 denotes anthropogenically affected water, with contaminated-water and waste-material genera, not the treatment facility. Four current contributors reproduce: GOLD1140 ORGANISM, PREGO623 TAXON, MADIN524 TAXON and the qualitative environment table. Only two have ITEM decisions, correctly leaving SEEDED status. The16-edge organic-nitrogen biotreatment overlay has a bounded treatment scope, but several attached citations do not establish the precise causal claim in the inspected text.

## Scope And Provenance

Entire exact generated record and every contributing source, with scientific claim and parent-context assessment.

Selection: All forty remaining ENGINEERED records in stable slug order; individual full-record observations, not a sampled category verdict. Starting distinct completed-observation coverage448/3208 is not clean-verdict or current-input coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 30167db0bf254f16bf774573bad9ebfcbe78d2d6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| ENVO:00002001 | data/habitats/engineered/waste_water.yaml | generated | waste water |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native check on captured scientific inputs | passed | True | ENVO:00002001 | Actual successful check from 2026-10-11T19:39:14.068484Z to 2026-10-11T19:39:16.503966Z. Per-record applicability retained; full-corpus gates do not expand scientific coverage. |
| Native check on captured scientific inputs | passed | True | ENVO:00002001 | Actual successful check from 2026-10-11T19:40:22.830722Z to 2026-10-11T19:40:32.094218Z. Per-record applicability retained; full-corpus gates do not expand scientific coverage. |
| Native check on captured scientific inputs | passed | True | ENVO:00002001 | Actual successful check from 2026-10-11T19:40:32.095315Z to 2026-10-11T19:40:52.911157Z. Per-record applicability retained; full-corpus gates do not expand scientific coverage. |
| Native check on captured scientific inputs | passed | True | ENVO:00002001 | Actual successful check from 2026-10-11T19:40:52.912319Z to 2026-10-11T19:41:56.664292Z. Per-record applicability retained; full-corpus gates do not expand scientific coverage. |
| Native check on captured scientific inputs | passed | True | ENVO:00002001 | Actual successful check from 2026-10-11T19:41:56.665596Z to 2026-10-11T19:42:06.494516Z. Per-record applicability retained; full-corpus gates do not expand scientific coverage. |
| Native check on captured scientific inputs | passed | True | ENVO:00002001 | Actual successful check from 2026-10-11T19:42:06.495610Z to 2026-10-11T19:42:12.023268Z. Per-record applicability retained; full-corpus gates do not expand scientific coverage. |
| Native check on captured scientific inputs | passed | True | ENVO:00002001 | Actual successful check from 2026-10-11T19:42:12.024508Z to 2026-10-11T19:42:39.328480Z. Per-record applicability retained; full-corpus gates do not expand scientific coverage. |
| Native check on captured scientific inputs | passed | True | ENVO:00002001 | Actual successful check from 2026-10-11T19:39:18.548604Z to 2026-10-11T19:39:21.517288Z. Authoritative CI executed the full QC runner on exact clean baseline 30167db0bf254f16bf774573bad9ebfcbe78d2d6; ['776 passed, 3 skipped']. https://github.com/CultureBotAI/HabitatMech/actions/runs/38167383091 This is verified CI on the exact scientific-input baseline, not a claim that local just qc was executed or new review files were already checked by CI. |
| Resolver and whole-document reconstruction | passed | False | ENVO:00002001 | All40 complete generated documents matched, and captured input hashes were reverified unchanged. |
| Original assertion-level membership reconstruction | unavailable | False | ENVO:00002001 | Manifest-named original inputs were unavailable at the configured paths; bounded ignored-inclusive searches did not reconstruct complete original membership. Frozen inventories remain reproducible. |
| iModulonDB applicability | not_applicable | False | ENVO:00002001 | No gene/regulator/expression-module claim in this exact record. Expression-module membership would not itself prove a habitat assertion. |

## Scientific And Domain Assessments

### Causal edge: waste_water_receives_anthropogenic_load

evidence: supported. Targets: ENVO:00002001.

The ENVO definition directly establishes human-affected water; PMID12180096 supplies sewage-treatment context, not a measured loading experiment.

### Causal edge: anthropogenic_load_supplies_organic_matter

evidence: supported. Targets: ENVO:00002001.

PMID27453679 full text, introduction and wastewater-characterization sections, discusses incoming wastewater organic substrates; this applies to the organic-treatment graph, not every wastewater composition.

### Causal edge: anthropogenic_load_supplies_ammonium

evidence: concern. Targets: ENVO:00002001.

PMID15276744 tests DO-dependent AOB communities. Its abstract and the attached title fragment do not establish the asserted origin of ammonium. Full text was not retrieved; claim support needs a precise source passage or a better citation.

### Causal edge: organic_matter_creates_oxygen_demand

evidence: supported. Targets: ENVO:00002001.

PMID27453679 introduction and biodegradability paragraphs explicitly connect organic pollution, oxygen consumption and oxygen-depletion potential.

### Causal edge: organic_matter_supports_heterotrophs

evidence: unknown. Targets: ENVO:00002001.

PMID12180096 abstract addresses microbial functional guilds but does not state this exact substrate-to-heterotroph edge. The claim is biologically plausible; that is not a replacement for uninspected full-text support.

### Causal edge: heterotrophs_perform_organic_oxidation

evidence: supported. Targets: ENVO:00002001.

PMID27453679 describes microbial oxidation of wastewater organics to carbon dioxide and water and coupled growth. Nonoxidative removal routes also exist and are not excluded by this bounded graph.

### Causal edge: organic_oxidation_consumes_oxygen

evidence: supported. Targets: ENVO:00002001.

PMID27453679 introduction, oxygen-uptake characterization and aeration discussion support oxygen consumption during the specified aerobic oxidation process.

### Causal edge: oxygen_demand_creates_anoxic_zones

evidence: unknown. Targets: ENVO:00002001.

The description qualifies this as a contribution rather than inevitable anoxia, but the PMID12180096 abstract/title snippet does not establish the local oxygen-demand-to-anoxic-zone claim.

### Causal edge: dissolved_oxygen_enables_nitrification

evidence: supported. Targets: ENVO:00002001.

PMID15276744 directly varies DO and measures AOB enrichment/kinetics. Support is direct for the ammonia-oxidizing portion; the broader nitrite-oxidizer clause was not separately tested in the inspected abstract.

### Causal edge: ammonium_selects_ammonia_oxidizers

evidence: concern. Targets: ENVO:00002001.

PMID19515200 is a one-year observational community study, with reported correlations strongest for temperature, oxygen, influent nitrite and chromium. It does not demonstrate ammonium-driven selection in the inspected abstract; attached title text cannot supply that causal inference.

### Causal edge: ammonia_oxidizers_perform_nitrification

evidence: supported. Targets: ENVO:00002001.

PMID15276744 studies enrichment and growth kinetics of ammonia oxidizers; the description correctly specifies only the first nitrification step, not complete nitrification by AOB alone.

### Causal edge: nitrite_oxidizers_complete_nitrification

evidence: unknown. Targets: ENVO:00002001.

This conventional NOB role is plausible, but PMID12180096 abstract does not explicitly establish the conversion; full-text verification remains outstanding.

### Causal edge: nitrification_produces_nitrate

evidence: unknown. Targets: ENVO:00002001.

The graph correctly links the composite nitrification process, not AOB alone, to nitrate. The attached PMID12180096 title fragment and inspected abstract do not document the particular conversion.

### Causal edge: anoxic_zones_select_denitrifiers

evidence: supported. Targets: ENVO:00002001.

PMID17391331 compares17 nitrogen-removal plants with four lacking denitrification and tests nitrate/nitrite electron acceptors. This supports operating-context enrichment and functional capability, not obligate anaerobiosis or a universal abundance claim.

### Causal edge: denitrifiers_perform_denitrification

evidence: supported. Targets: ENVO:00002001.

PMID18811652 measures substrate-dependent nitrate/nitrite consumption and uses MAR-FISH to identify active groups in two plants. It supports denitrifying activity under the reported conditions.

### Causal edge: denitrification_removes_nitrogen

evidence: unknown. Targets: ENVO:00002001.

PMID18811652 abstract reports nitrate/nitrite consumption, not direct gaseous-nitrogen measurements. A measured gaseous endpoint or a precise mechanistic source passage is needed for this wording; no contradiction of denitrification chemistry is claimed.

### Habitat identity, definition and source boundary

identity: supported. Targets: ENVO:00002001.

ENVO:00002001 denotes anthropogenically affected water, with contaminated-water and waste-material genera, not the treatment facility. Four current contributors reproduce: GOLD1140 ORGANISM, PREGO623 TAXON, MADIN524 TAXON and the qualitative environment table. Only two have ITEM decisions, correctly leaving SEEDED status. The16-edge organic-nitrogen biotreatment overlay has a bounded treatment scope, but several attached citations do not establish the precise causal claim in the inspected text.

### All direct and inherited genus contributions, synonym scopes and mapping endpoints

grounding: concern. Targets: ENVO:00002001.

ENVO:00002001 denotes anthropogenically affected water, with contaminated-water and waste-material genera, not the treatment facility. Four current contributors reproduce: GOLD1140 ORGANISM, PREGO623 TAXON, MADIN524 TAXON and the qualitative environment table. Only two have ITEM decisions, correctly leaving SEEDED status. The16-edge organic-nitrogen biotreatment overlay has a bounded treatment scope, but several attached citations do not establish the precise causal claim in the inspected text. Independent ontology, GOLD, ambiguous-leaf and authored-definition contributions were considered separately.

### Contributors, frozen counts and native status/history

provenance: supported. Targets: ENVO:00002001.

Full-document reproduction preserves 4 source concepts and 2 ITEM-reviewed contributors. Actual attestations=[{"source": "ENVIRONMENTS_TABLE", "source_id": "wastewater", "source_label": "wastewater", "notes": "Physicochemical parameter bands from kg-microbe's environment table."}, {"source": "GOLD", "source_id": "gold.ecosystem:2886", "source_label": "Wastewater", "source_path": "Engineered &gt; Wastewater", "mapping_predicate": "skos:exactMatch", "assertion_count": 1140, "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path; first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "MADIN", "source_id": "ENVO:00002001", "source_label": "waste water", "assertion_count": 524, "assertion_unit": "TAXON"}, {"source": "PREGO", "source_id": "ENVO:00002001", "source_label": "waste water", "assertion_count": 623, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels": "annotated_genomes_isolates&#124;environmental_samples"}]. Source counts/units are not summed; omitted zero counts are not biological absence. The generated native status/history is consistent with maintained inputs, not promoted by this scientific review.

### Source association versus characteristic presence

evidence: supported. Targets: ENVO:00002001.

All retained associations were read and reproduce: {"PREGO": 25, "MADIN": 23}. All taxon IDs resolve. Source-specific ranks, candidate pools, counts, scores and corroborations retain their original meaning; none asserts is_characteristic. A source ranking is neither abundance nor a cross-source confidence probability. PREGO retains25 tied score4 entries from623; MADIN retains23 associations from524 without invented score/rank. Five frozen labels differ from current NCBI naming, with the same IDs/strain designations; no taxonomy refresh was applied.

### Environmental parameters, optional evidence and applicability

completeness: supported. Targets: ENVO:00002001.

The five wastewater qualitative bands reproduce exactly: [{"parameter": "NUTRIENTS", "qualitative_value": "high", "source": "kg-microbe environments.csv (wastewater)"}, {"parameter": "PRESSURE", "qualitative_value": "low", "source": "kg-microbe environments.csv (wastewater)"}, {"parameter": "TEMPERATURE", "qualitative_value": "medium", "source": "kg-microbe environments.csv (wastewater)"}, {"parameter": "WATER_AVAILABILITY", "qualitative_value": "high", "source": "kg-microbe environments.csv (wastewater)"}, {"parameter": "WATER_VARIABILITY", "qualitative_value": "permanently wet", "source": "kg-microbe environments.csv (wastewater)"}]. They are coarse source annotations, not measured universal thresholds. The sole graph is assessed edge by edge above. No gene, regulator or expression-module claim calls for iModulonDB. Optional discussions, datasets and organism detail are not required merely to fill fields; parent/child evidence is not silently imported.

## Findings

### F1: Several causal edges lack verified claim-specific support in their attached evidence

major / open / provisional; issue key: envo-00002001-causal-citation-specificity.

The16-edge pathway is plausible and several edges are supported. However, the ammonium-loading edge cites a DO/AOB study, the ammonium-selection edge cites an observational community study, and the gas-removal endpoint exceeds the inspected nitrate/nitrite-consumption abstract. Four additional Wagner/Loy edges remain unverified at the exact claim level. Attached title fragments do not supply those missing causal passages. This is a bounded evidence-placement gap, not proof that the biological mechanisms are false; full-text access limits are explicit.

## Recommended Actions And Acceptance Checks

### A1

For each concerned/unknown edge, inspect the actual full-text passage or add an appropriate primary/mechanistic citation. Distinguish observation, intervention, substrate capability and gaseous endpoint; keep conditional treatment scope. Preserve supported organic-oxidation edges and document every edge-level disposition.

- Use maintained source/curation owners, exact source keys and inspected claim-level evidence. Do not hand-edit generated records or rewrite immutable reviews.
- Preserve frozen source IDs, paths, count units, valid independent parents and native lifecycle rules; later exports do not replace original membership.
- For an authorized fix, append required native history, add focused regressions, inspect a seed canary, regenerate affected products and pass schema, strict, labels, reproduction and full QC.
- Save a linked successor observation for any disposition; report persistence alone does not resolve this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| R | data/habitats/engineered/waste_water.yaml; Entire captured YAML read, including every source, taxon, parameter, graph and generated event | supports | ENVO:00002001 denotes anthropogenically affected water, with contaminated-water and waste-material genera, not the treatment facility. Four current contributors reproduce: GOLD1140 ORGANISM, PREGO623 TAXON, MADIN524 TAXON and the qualitative environment table. Only two have ITEM decisions, correctly leaving SEEDED status. The16-edge organic-nitrogen biotreatment overlay has a bounded treatment scope, but several attached citations do not establish the precise causal claim in the inspected text. |
| RULES | docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml; Native field checklist; SourceAttestation and CharacteristicTaxon contracts | supports | Applied strict-genus and identity boundaries, source-specific count/score semantics, ITEM lifecycle, environmental-triad roles and edge-level evidence rules. Optional data are not invented for coverage. |
| RAW | data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv; Exact logical TSV rows (header is row1), not nearby-path or descendant membership | supports | {"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:GOLD.1a43260310", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row": 245}, {"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:PREGO.963b96a257", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row": 1480}], "data/raw/environment_parameters.tsv": [{"data": {"cobo_simon_habitat": "NA", "env_type": "wastewater", "main_group": "Other", "parameter": "Nutrients", "term_ids": "ENVO:00002001", "term_labels": "waste water", "value": "high"}, "logical_row": 597}, {"data": {"cobo_simon_habitat": "NA", "env_type": "wastewater", "main_group": "Other", "parameter": "Pressure", "term_ids": "ENVO:00002001", "term_labels": "waste water", "value": "low"}, "logical_row": 598}, {"data": {"cobo_simon_habitat": "NA", "env_type": "wastewater", "main_group": "Other", "parameter": "Temperature", "term_ids": "ENVO:00002001", "term_labels": "waste water", "value": "medium"}, "logical_row": 599}, {"data": {"cobo_simon_habitat": "NA", "env_type": "wastewater", "main_group": "Other", "parameter": "Water", "term_ids": "ENVO:00002001", "term_labels": "waste water", "value": "high"}, "logical_row": 600}, {"data": {"cobo_simon_habitat": "NA", "env_type": "wastewater", "main_group": "Other", "parameter": "water variability", "term_ids": "ENVO:00002001", "term_labels": "waste water", "value": "permanently wet"}, "logical_row": 601}], "data/raw/gold_ecosystem_paths.tsv": [{"data": {"biosample_count": "0", "canonical_path": "Engineered &gt; Wastewater", "depth": "2", "ecosystem": "Engineered", "ecosystem_category": "Wastewater", "ecosystem_subtype": "", "ecosystem_type": "", "gold_node_count": "4", "gold_node_ids": "gold.ecosystem:2886&#124;gold.ecosystem:3508&#124;gold.ecosystem:3833&#124;gold.ecosystem:4264", "leaf_label": "Wastewater", "organism_count": "1140", "specific_ecosystem": "", "study_count": "0", "total_assertions": "1140"}, "logical_row": 38}], "data/raw/gold_path_biosamples.tsv": [{"data": {"biosample_count": "23", "canonical_path": "Engineered &gt; Wastewater", "ecosystem_path_id": "4264"}, "logical_row": 492}], "data/raw/isolation_source_groundings.tsv": [{"data": {"confidence": "high", "curator": "codex_review_fix", "mapping_justification": "semapv:ManualMappingCuration", "object_id": "ENVO:00002001", "object_label": "waste water", "object_source": "ENVO", "predicate_id": "skos:exactMatch", "source_dataset": "bacdive", "subject_label": "Wastewater", "subject_label_normalized": "wastewater", "verified_date": "2026-05-02"}, "logical_row": 343}], "data/raw/madin_habitat_taxa.tsv": [{"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1058", "taxon_label": "thiocapsa_roseopersicina"}, "logical_row": 236}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1089553", "taxon_label": "Thermacetogenium phaeum DSM 12270"}, "logical_row": 237}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1120924", "taxon_label": "Acinetobacter baylyi DSM 14961"}, "logical_row": 238}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1120925", "taxon_label": "Acinetobacter bouvetii DSM 14964"}, "logical_row": 239}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1120927", "taxon_label": "Acinetobacter tandoii DSM 14970"}, "logical_row": 240}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1120928", "taxon_label": "Acinetobacter tjernbergiae DSM 14971"}, "logical_row": 241}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1120929", "taxon_label": "Acinetobacter towneri DSM 14962"}, "logical_row": 242}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1120962", "taxon_label": "Alcaligenes faecalis phenolicus DSM 16503"}, "logical_row": 243}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121109", "taxon_label": "Bifidobacterium minimum DSM 20102"}, "logical_row": 244}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121110", "taxon_label": "Bifidobacterium subtile DSM 20096"}, "logical_row": 245}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121111", "taxon_label": "Bifidobacterium thermacidophilum thermacidophilum DSM 15837"}, "logical_row": 246}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121123", "taxon_label": "Brevundimonas aveniformis DSM 17977"}, "logical_row": 247}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121255", "taxon_label": "Caenimonas koreensis DSM 17982"}, "logical_row": 248}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121262", "taxon_label": "Caloramator proteoclasticus DSM 10124"}, "logical_row": 249}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121271", "taxon_label": "Gemmobacter nectariphilus DSM 15620"}, "logical_row": 250}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121285", "taxon_label": "Chryseobacterium caeni DSM 17710"}, "logical_row": 251}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121286", "taxon_label": "Chryseobacterium daeguense DSM 19388"}, "logical_row": 252}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121344", "taxon_label": "Clostridium viride DSM 6836"}, "logical_row": 253}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121348", "taxon_label": "Comamonas badia DSM 17552"}, "logical_row": 254}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121378", "taxon_label": "Deinococcus aquatilis DSM 23025"}, "logical_row": 255}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121393", "taxon_label": "Desulfatibacillum alkenivorans DSM 16219"}, "logical_row": 256}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121405", "taxon_label": "Desulfococcus multivorans DSM 2059"}, "logical_row": 257}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121433", "taxon_label": "Desulfovermiculus halophilus DSM 18834"}, "logical_row": 258}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121438", "taxon_label": "Desulfovibrio alcoholivorans DSM 5433"}, "logical_row": 259}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121440", "taxon_label": "Desulfovibrio aminophilus DSM 12254"}, "logical_row": 260}], "data/raw/madin_habitats.tsv": [{"data": {"label": "waste water", "madin_id": "ENVO:00002001", "taxon_count": "524", "vocabulary": "ENVO"}, "logical_row": 14}], "data/raw/ontology_subclass_edges.tsv": [{"data": {"object": "ENVO:00002186", "predicate": "rdfs:subClassOf", "subject": "ENVO:00002001"}, "logical_row": 5263}, {"data": {"object": "ENVO:00002264", "predicate": "rdfs:subClassOf", "subject": "ENVO:00002001"}, "logical_row": 5264}], "data/raw/ontology_terms.tsv": [{"data": {"definition": "Water that has been adversely affected in quality by anthropogenic influence.", "deprecated": "", "directly_referenced": "TRUE", "label": "waste water", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id": "ENVO:00002001"}, "logical_row": 7160}], "data/raw/prego_habitat_taxa.tsv": [{"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "1", "taxon_id": "NCBITaxon:1046983", "taxon_label": "Hydrogenedentes bacterium JGI 0000059-N10"}, "logical_row": 5416}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "2", "taxon_id": "NCBITaxon:1047009", "taxon_label": "Fidelibacterota bacterium SCGC AAA011-A05"}, "logical_row": 5417}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "3", "taxon_id": "NCBITaxon:1047012", "taxon_label": "Caldiserica bacterium JGI 0000059-M03"}, "logical_row": 5418}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "4", "taxon_id": "NCBITaxon:1047053", "taxon_label": "Atribacteria bacterium JGI 0000059-I14"}, "logical_row": 5419}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "5", "taxon_id": "NCBITaxon:1047055", "taxon_label": "Fidelibacterota bacterium JGI 0000039-D08"}, "logical_row": 5420}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "6", "taxon_id": "NCBITaxon:1047056", "taxon_label": "Fidelibacterota bacterium JGI 0000039-E15"}, "logical_row": 5421}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "7", "taxon_id": "NCBITaxon:1047058", "taxon_label": "Fidelibacterota bacterium JGI 0000039-O11"}, "logical_row": 5422}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "8", "taxon_id": "NCBITaxon:1047059", "taxon_label": "Fidelibacterota bacterium JGI 0000059-D20"}, "logical_row": 5423}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "9", "taxon_id": "NCBITaxon:1047060", "taxon_label": "Fidelibacterota bacterium JGI 0000059-E23"}, "logical_row": 5424}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "10", "taxon_id": "NCBITaxon:1047061", "taxon_label": "Fidelibacterota bacterium JGI 0000059-L03"}, "logical_row": 5425}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "11", "taxon_id": "NCBITaxon:1047063", "taxon_label": "WS1 bacterium JGI 0000059-K21"}, "logical_row": 5426}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "12", "taxon_id": "NCBITaxon:1047073", "taxon_label": "Cloacimonetes bacterium JGI 0000039-I17"}, "logical_row": 5427}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "13", "taxon_id": "NCBITaxon:1047076", "taxon_label": "Cloacimonetes bacterium JGI 0000039-M09"}, "logical_row": 5428}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "14", "taxon_id": "NCBITaxon:1047077", "taxon_label": "Cloacimonetes bacterium JGI 0000039-P09"}, "logical_row": 5429}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "15", "taxon_id": "NCBITaxon:1047078", "taxon_label": "Cloacimonetes bacterium JGI 0000059-F17"}, "logical_row": 5430}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "16", "taxon_id": "NCBITaxon:1047079", "taxon_label": "Cloacimonetes bacterium JGI 0000059-L07"}, "logical_row": 5431}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "17", "taxon_id": "NCBITaxon:1047080", "taxon_label": "Cloacimonetes bacterium JGI 0000059-P03"}, "logical_row": 5432}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "18", "taxon_id": "NCBITaxon:1047081", "taxon_label": "Cloacimonetes bacterium JGI 0000059-P11"}, "logical_row": 5433}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "19", "taxon_id": "NCBITaxon:1058", "taxon_label": "Thiocapsa roseopersicina"}, "logical_row": 5434}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "20", "taxon_id": "NCBITaxon:1089553", "taxon_label": "Thermacetogenium phaeum DSM 12270"}, "logical_row": 5435}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "21", "taxon_id": "NCBITaxon:1104568", "taxon_label": "Synergistetes bacterium JGI 0000079-D21"}, "logical_row": 5436}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "22", "taxon_id": "NCBITaxon:1104603", "taxon_label": "Atribacteria bacterium JGI 0000079-L04"}, "logical_row": 5437}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "23", "taxon_id": "NCBITaxon:1104604", "taxon_label": "Atribacteria bacterium JGI 0000079-F20"}, "logical_row": 5438}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "24", "taxon_id": "NCBITaxon:1104605", "taxon_label": "Armatimonadetes bacterium JGI 0000077-K19"}, "logical_row": 5439}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "25", "taxon_id": "NCBITaxon:1104619", "taxon_label": "Hydrogenedentes bacterium JGI 0000077-D07"}, "logical_row": 5440}], "data/raw/prego_habitats.tsv": [{"data": {"biolink_category": "biolink:OntologyClass", "channels": "annotated_genomes_isolates&#124;environmental_samples", "direct_assertion_count": "719", "max_prego_score": "4", "ontology": "ENVO", "prego_id": "ENVO:00002001", "prego_synonyms": "waste water&#124;waste waters", "taxon_count": "623"}, "logical_row": 93}]} |
| CODE | src/habitatmech/seed.py; Executed resolver, item/class decisions and full-document reproduction; all40 documents match | supports | {"reviewed_sources": 2, "routes": [{"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": null, "reviewed": false, "route": "environments_table_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": null, "reviewed": false, "route": "environments_table_self_grounded"}, "minted": "habitatmech:ENVIRONMENTS_TABLE.5bb62a0436", "source": "ENVIRONMENTS_TABLE", "source_id": "wastewater"}, {"actual": {"category": null, "contributes_grounding": true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:GOLD.1a43260310", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": "skos:exactMatch", "reviewed": true, "route": "curated_review_of_gold_mapping_table"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": "skos:exactMatch", "reviewed": false, "route": "gold_mapping_table"}, "minted": "habitatmech:GOLD.1a43260310", "source": "GOLD", "source_id": "gold.ecosystem:2886"}, {"actual": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": null, "reviewed": false, "route": "madin_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": null, "reviewed": false, "route": "madin_self_grounded"}, "minted": "habitatmech:MADIN.da9572e4ca", "source": "MADIN", "source_id": "ENVO:00002001"}, {"actual": {"category": null, "contributes_grounding": true, "decision": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:PREGO.963b96a257", "notes": "Multi-source review pass: this record is attested by more than one independent vocabulary, and this source's label or path was read against the record's ontology term to check the merge is right. It agrees. Source concepts in the same pass whose labels did not agree were re-decided rather than endorsed; see the pass's other decisions of the same date.", "object_id": "", "object_label": "", "relation": "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": null, "reviewed": true, "route": "curated_review_of_prego_self_grounded"}, "automatic": {"category": null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": null, "reviewed": false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.963b96a257", "source": "PREGO", "source_id": "ENVO:00002001"}], "source_concepts": 4} |
| ONT | https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl; Named current OWL target/parent/candidate classes; direct axioms distinguished from related properties; no automatic remapping | supports | {"ENVO:00002001": {"definitions": ["Water that has been adversely affected in quality by anthropogenic influence."], "deprecated": [], "equivalents": [], "labels": ["waste water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002186", "http://purl.obolibrary.org/obo/ENVO_00002264"], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002186": {"definitions": [], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002006"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/ENVO_02000200"], "http://www.w3.org/2002/07/owl#someValuesFrom": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"nested": true}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["contaminated water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/ENVO_02000200"], "http://www.w3.org/2002/07/owl#someValuesFrom": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/CHEBI_24431"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000087"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_78298"]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["polluted water"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002264": {"definitions": ["A material which is not the desired output of a process and which is typically the input of a process which removes it from its producer (e.g. a disposal process)."], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00010483"], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000087"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000665"]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}], "labels": ["waste material"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00010483", {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"], "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000087"], "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000665"]}], "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}} Same-day cached source; original access time retained, SHA256 reverified 2026-10-11T19:38:15.215491+00:00. |
| PARENT | data/habitats/engineered/engineered__900b76ad.yaml; data/habitats/other/waste_material.yaml; data/habitats/other/environmental_material.yaml; Available generated ancestor identity/context; external-only parents are assessed in ONT. Context reads do not count as full-record coverage of ancestors. | supports | {"ENVO:00002264": {"definition": "A material which is not the desired output of a process and which is typically the input of a process which removes it from its producer (e.g. a disposal process).", "grounding_status": "EXACT", "label": "waste material", "parent_habitats": ["ENVO:00010483"]}, "ENVO:00010483": {"definition": "A material entity which other material entities in an environmental system are primarily or partially composed of.", "grounding_status": "EXACT", "label": "environmental material", "parent_habitats": null}, "habitatmech:GOLD.2acb39dd08": {"definition": null, "grounding_status": "UNGROUNDED", "label": "Engineered", "parent_habitats": null}} |
| BULK | https://gold.jgi.doe.gov/download?mode=site_excel; Exact five-position tuples; blank/Unclassified normalization preserves internal positions; 245071/532036/637051/63807 sheet rows including headers | supports | Full positional census counts={"Biosample": 0, "Organism": 1002, "SequencingProject": 878}; inspected first three descriptions per sample/organism sheet={"Biosample": [], "Organism": [{"data": {"ORGANISM GOLD ID": "Go0000015", "ORGANISM HABITAT": "Soil&#124;Host&#124;Fresh water&#124;Sludge&#124;Wastewater&#124;Oil fields", "ORGANISM ISOLATION HOST NAME": "", "ORGANISM NAME": "Delftia acidovorans SPH-1", "ORGANISM SAMPLE COLLECTION SITE": "Sludge from communal sewage treatment plant; Germany"}, "row": 14}, {"data": {"ORGANISM GOLD ID": "Go0000051", "ORGANISM HABITAT": "Fresh water", "ORGANISM ISOLATION HOST NAME": "", "ORGANISM NAME": "Pseudothermotoga lettingae TMO", "ORGANISM SAMPLE COLLECTION SITE": "Thermophilic sulfate-reducing bioreactor; The Netherlands, Wageningen"}, "row": 47}, {"data": {"ORGANISM GOLD ID": "Go0000071", "ORGANISM HABITAT": "Host&#124;Sludge", "ORGANISM ISOLATION HOST NAME": "", "ORGANISM NAME": "Parvibaculum lavamentivorans DS-1", "ORGANISM SAMPLE COLLECTION SITE": "Sewage treatment plant in Germany"}, "row": 66}]}. Zero exact matches is bounded to this export, not biological absence. Other member rows and study joins were indexed, not individually assessed. Frozen counts are unchanged. Same-day cached source; original access time retained, SHA256 reverified 2026-10-11T19:38:16.257007+00:00. |
| CLASS | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Later official five-position classification rows, not original membership reconstruction | supports | [{"row": 466, "slug": "waste_water", "path": "Engineered &gt; Wastewater", "values": ["4264", "Engineered", "Wastewater", "Unclassified", "Unclassified", "Unclassified"]}] Same-day cached source; original access time retained, SHA256 reverified 2026-10-11T19:38:16.258000+00:00. |
| TAX | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1046983%2C1047009%2C1047012%2C1047053%2C1047055%2C1047056%2C1047058%2C1047059%2C1047060%2C1047061%2C1047063%2C1047073%2C1047076%2C1047077%2C1047078%2C1047079%2C1047080%2C1047081%2C1058%2C1089553%2C1104568%2C1104603%2C1104604%2C1104605%2C1104619%2C1120924%2C1120925%2C1120927%2C1120928%2C1120929%2C1120962%2C1121109%2C1121110%2C1121111%2C1121123%2C1121255%2C1121262%2C1121271%2C1121285%2C1121286%2C1121344%2C1121348%2C1121378%2C1121393%2C1121405%2C1121433%2C1121438%2C1121440%2C1121889%2C1121933%2C1122132%2C1123024%2C1123399%2C1123400%2C1223541%2C1259795%2C1304875%2C1399774%2C1469607%2C1667%2C1720%2C1871044%2C1871047%2C1871616%2C1872122%2C214688%2C2164%2C264023%2C265072%2C28892%2C306%2C310396%2C317577%2C338966%2C340%2C361%2C370973%2C424718%2C469547%2C469551%2C53408%2C53463%2C558173%2C572547%2C584708%2C622617%2C65735%2C680375%2C76114%2C866499%2C916&amp;retmode=xml; NCBI Taxonomy EFetch XML: each target-associated TaxId, ScientificName and Rank; OtherNames inspected for five label differences | supports | [{"current_name": "Thiocapsa roseopersicina", "frozen_label": "Thiocapsa roseopersicina", "id": "1058", "rank": "species"}, {"current_name": "Thermacetogenium phaeum DSM 12270", "frozen_label": "Thermacetogenium phaeum DSM 12270", "id": "1089553", "rank": "strain"}, {"current_name": "Acinetobacter baylyi DSM 14961 = CIP 107474", "frozen_label": "Acinetobacter baylyi DSM 14961", "id": "1120924", "rank": "strain"}, {"current_name": "Acinetobacter bouvetii DSM 14964 = CIP 107468", "frozen_label": "Acinetobacter bouvetii DSM 14964", "id": "1120925", "rank": "strain"}, {"current_name": "Acinetobacter tandoii DSM 14970 = CIP 107469", "frozen_label": "Acinetobacter tandoii DSM 14970", "id": "1120927", "rank": "strain"}, {"current_name": "Acinetobacter tjernbergiae DSM 14971 = CIP 107465", "frozen_label": "Acinetobacter tjernbergiae DSM 14971", "id": "1120928", "rank": "strain"}, {"current_name": "Acinetobacter towneri DSM 14962 = CIP 107472", "frozen_label": "Acinetobacter towneri DSM 14962", "id": "1120929", "rank": "strain"}, {"current_name": "Alcaligenes phenolicus DSM 16503", "frozen_label": "Alcaligenes faecalis phenolicus DSM 16503", "id": "1120962", "rank": "strain"}, {"current_name": "Bifidobacterium minimum DSM 20102", "frozen_label": "Bifidobacterium minimum DSM 20102", "id": "1121109", "rank": "strain"}, {"current_name": "Bifidobacterium subtile DSM 20096", "frozen_label": "Bifidobacterium subtile DSM 20096", "id": "1121110", "rank": "strain"}, {"current_name": "Bifidobacterium thermacidophilum subsp. thermacidophilum DSM 15837", "frozen_label": "Bifidobacterium thermacidophilum thermacidophilum DSM 15837", "id": "1121111", "rank": "strain"}, {"current_name": "Brevundimonas aveniformis DSM 17977", "frozen_label": "Brevundimonas aveniformis DSM 17977", "id": "1121123", "rank": "strain"}, {"current_name": "Caenimonas koreensis DSM 17982", "frozen_label": "Caenimonas koreensis DSM 17982", "id": "1121255", "rank": "strain"}, {"current_name": "Caloramator proteoclasticus DSM 10124", "frozen_label": "Caloramator proteoclasticus DSM 10124", "id": "1121262", "rank": "strain"}, {"current_name": "Gemmobacter nectariphilus DSM 15620", "frozen_label": "Gemmobacter nectariphilus DSM 15620", "id": "1121271", "rank": "strain"}, {"current_name": "Epilithonimonas caeni DSM 17710", "frozen_label": "Chryseobacterium caeni DSM 17710", "id": "1121285", "rank": "strain"}, {"current_name": "Chryseobacterium daeguense DSM 19388", "frozen_label": "Chryseobacterium daeguense DSM 19388", "id": "1121286", "rank": "strain"}, {"current_name": "[Clostridium] viride DSM 6836", "frozen_label": "Clostridium viride DSM 6836", "id": "1121344", "rank": "strain"}, {"current_name": "Comamonas badia DSM 17552", "frozen_label": "Comamonas badia DSM 17552", "id": "1121348", "rank": "strain"}, {"current_name": "Deinococcus aquatilis DSM 23025", "frozen_label": "Deinococcus aquatilis DSM 23025", "id": "1121378", "rank": "strain"}, {"current_name": "Desulfatibacillum alkenivorans DSM 16219", "frozen_label": "Desulfatibacillum alkenivorans DSM 16219", "id": "1121393", "rank": "strain"}, {"current_name": "Desulfococcus multivorans DSM 2059", "frozen_label": "Desulfococcus multivorans DSM 2059", "id": "1121405", "rank": "strain"}, {"current_name": "Desulfovermiculus halophilus DSM 18834", "frozen_label": "Desulfovermiculus halophilus DSM 18834", "id": "1121433", "rank": "strain"}, {"current_name": "Solidesulfovibrio alcoholivorans DSM 5433", "frozen_label": "Desulfovibrio alcoholivorans DSM 5433", "id": "1121438", "rank": "strain"}, {"current_name": "Desulfovibrio aminophilus DSM 12254", "frozen_label": "Desulfovibrio aminophilus DSM 12254", "id": "1121440", "rank": "strain"}, {"current_name": "Hydrogenedentes bacterium JGI 0000059-N10", "frozen_label": "Hydrogenedentes bacterium JGI 0000059-N10", "id": "1046983", "rank": "species"}, {"current_name": "Fidelibacterota bacterium SCGC AAA011-A05", "frozen_label": "Fidelibacterota bacterium SCGC AAA011-A05", "id": "1047009", "rank": "species"}, {"current_name": "Caldiserica bacterium JGI 0000059-M03", "frozen_label": "Caldiserica bacterium JGI 0000059-M03", "id": "1047012", "rank": "species"}, {"current_name": "Atribacteria bacterium JGI 0000059-I14", "frozen_label": "Atribacteria bacterium JGI 0000059-I14", "id": "1047053", "rank": "species"}, {"current_name": "Fidelibacterota bacterium JGI 0000039-D08", "frozen_label": "Fidelibacterota bacterium JGI 0000039-D08", "id": "1047055", "rank": "species"}, {"current_name": "Fidelibacterota bacterium JGI 0000039-E15", "frozen_label": "Fidelibacterota bacterium JGI 0000039-E15", "id": "1047056", "rank": "species"}, {"current_name": "Fidelibacterota bacterium JGI 0000039-O11", "frozen_label": "Fidelibacterota bacterium JGI 0000039-O11", "id": "1047058", "rank": "species"}, {"current_name": "Fidelibacterota bacterium JGI 0000059-D20", "frozen_label": "Fidelibacterota bacterium JGI 0000059-D20", "id": "1047059", "rank": "species"}, {"current_name": "Fidelibacterota bacterium JGI 0000059-E23", "frozen_label": "Fidelibacterota bacterium JGI 0000059-E23", "id": "1047060", "rank": "species"}, {"current_name": "Fidelibacterota bacterium JGI 0000059-L03", "frozen_label": "Fidelibacterota bacterium JGI 0000059-L03", "id": "1047061", "rank": "species"}, {"current_name": "WS1 bacterium JGI 0000059-K21", "frozen_label": "WS1 bacterium JGI 0000059-K21", "id": "1047063", "rank": "species"}, {"current_name": "Cloacimonetes bacterium JGI 0000039-I17", "frozen_label": "Cloacimonetes bacterium JGI 0000039-I17", "id": "1047073", "rank": "species"}, {"current_name": "Cloacimonetes bacterium JGI 0000039-M09", "frozen_label": "Cloacimonetes bacterium JGI 0000039-M09", "id": "1047076", "rank": "species"}, {"current_name": "Cloacimonetes bacterium JGI 0000039-P09", "frozen_label": "Cloacimonetes bacterium JGI 0000039-P09", "id": "1047077", "rank": "species"}, {"current_name": "Cloacimonetes bacterium JGI 0000059-F17", "frozen_label": "Cloacimonetes bacterium JGI 0000059-F17", "id": "1047078", "rank": "species"}, {"current_name": "Cloacimonetes bacterium JGI 0000059-L07", "frozen_label": "Cloacimonetes bacterium JGI 0000059-L07", "id": "1047079", "rank": "species"}, {"current_name": "Cloacimonetes bacterium JGI 0000059-P03", "frozen_label": "Cloacimonetes bacterium JGI 0000059-P03", "id": "1047080", "rank": "species"}, {"current_name": "Cloacimonetes bacterium JGI 0000059-P11", "frozen_label": "Cloacimonetes bacterium JGI 0000059-P11", "id": "1047081", "rank": "species"}, {"current_name": "Synergistetes bacterium JGI 0000079-D21", "frozen_label": "Synergistetes bacterium JGI 0000079-D21", "id": "1104568", "rank": "species"}, {"current_name": "Atribacteria bacterium JGI 0000079-L04", "frozen_label": "Atribacteria bacterium JGI 0000079-L04", "id": "1104603", "rank": "species"}, {"current_name": "Atribacteria bacterium JGI 0000079-F20", "frozen_label": "Atribacteria bacterium JGI 0000079-F20", "id": "1104604", "rank": "species"}, {"current_name": "Armatimonadetes bacterium JGI 0000077-K19", "frozen_label": "Armatimonadetes bacterium JGI 0000077-K19", "id": "1104605", "rank": "species"}, {"current_name": "Hydrogenedentes bacterium JGI 0000077-D07", "frozen_label": "Hydrogenedentes bacterium JGI 0000077-D07", "id": "1104619", "rank": "species"}]. All named IDs resolve directly. Current labels do not silently replace frozen source labels. Taxonomy resolution does not validate the habitat association. |
| SEARCH | curation; history; research; reports; reviews; data/raw; data/habitats; conf; Bounded ignored-independent searches | supports | Identifier/label/slug/source-path search included hidden and ignored files in these roots. Structured coverage used Path.rglob. Original manifest paths and bounded upstream data/build traversal={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe", "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv", "exists": false, "expected_sha256": "c13c21bdd04619c75ce16e63b05e51577b0cefec5b61765d383313f654ab3fae"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_edges.tsv", "exists": false, "expected_sha256": "54982c25de9d2c820eeebc1452aeac0b034595921d04d55b810bf1d2b1e127e0"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/nodes.tsv", "exists": false, "expected_sha256": "a2a2f9acae230636dd866347d173a32c9f025c04a377060087a4be65781628f3"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/bacdive/edges.tsv", "exists": false, "expected_sha256": "ab6208bff4854db7c1a736d53d0aa04269a682ab15a1ce6f37c6d731000281d7"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/nodes.tsv", "exists": false, "expected_sha256": "020de3afc71495571ddb05000c83a58d009272f53735b5f7c9326c1293e0415c"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/prego/edges.tsv", "exists": false, "expected_sha256": "8863ee3197a36915865fa4833df39d10c3f8f69b64bafbb746b9cd731308a0aa"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/nodes.tsv", "exists": false, "expected_sha256": "cc5941cd677831e8e207da018dca763cd009bb1f9310b21cb4d45892316e006d"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/madin_etal/edges.tsv", "exists": false, "expected_sha256": "fd333634eaaa3cfe57a35cdca2f4c5b8cf0662851c1df58914d3e999d62a650e"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/environments.csv", "exists": false, "expected_sha256": "99299fe635159712f95568783ad3b484230fb31781262f1f6f8bd84db4bc3048"}, {"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/isolation_source_to_ontology.tsv", "exists": false, "expected_sha256": "2dea3d1bb20c72a04b6f64a67e2bb2bdc4f3649b809c5935390239be2791ef1f"}], "traversal": [{"command": ["rg", "--files", "--no-ignore", "--hidden", "data"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "build"], "exit_code": 0, "matches": [], "stderr": ""}, {"command": ["rg", "--files", "--no-ignore", "--hidden", "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data"], "exit_code": 0, "matches": [], "stderr": ""}]}. This is not a global filesystem absence claim, and older ad hoc reports are not automatically completed structured coverage. |
| GRAPH | curation/causal_graphs/waste_water.yaml; All nodes/edges; history and generated attachment | supports | Entire overlay and generated16-edge graph read. Node identities, typed directions, edge descriptions, citations, snippets and history match. Scope is organic-nitrogen biotreatment, not a universal process claim for all wastewater. |
| PMID-12180096 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12180096+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID12180096; DOI10.1016/s0958-1669(02)00315-4; title, full abstract and bibliographic metadata | supports | The review abstract establishes nutrient-removal guilds in sewage treatment; it does not expose the specific substrate, oxygen-gradient or nitrate-conversion passages needed by several graph edges. |
| PMID-27453679 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27453679+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID27453679; DOI10.1080/10643389.2016.1149903; title, full abstract and bibliographic metadata | supports | Abstract and inspected full-text introduction/characterization paragraphs support aerobic organic oxidation, coupled growth and oxygen demand; the article also emphasizes nonoxidative removal routes. |
| PMID-15276744 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15276744+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID15276744; DOI10.1016/j.watres.2004.04.047; title, full abstract and bibliographic metadata | supports | Controlled chemostat and full-scale DO comparisons directly support oxygen-dependent AOB ecology/kinetics, not the asserted source of anthropogenic ammonium loading. |
| PMID-19515200 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19515200+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID19515200; DOI10.1111/j.1462-2920.2009.01958.x; title, full abstract and bibliographic metadata | supports | A one-year observational AOB/AOA study reports multivariate environmental correlations; it is not an ammonium-manipulation experiment. |
| PMID-17391331 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17391331+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID17391331; DOI10.1111/j.1574-6941.2007.00309.x; title, full abstract and bibliographic metadata | supports | FISH and microautoradiography compare denitrifier populations and electron acceptors across nutrient-removal and non-denitrifying plants, supporting bounded denitrifying ecophysiology. |
| PMID-18811652 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18811652+AND+SRC%3AMED&amp;format=json&amp;resultType=core; PMID18811652; DOI10.1111/j.1574-6941.2008.00571.x; title, full abstract and bibliographic metadata | supports | Two-plant substrate-addition experiments measure nitrate/nitrite consumption and active probe-defined groups, not direct gaseous-nitrogen flux in the inspected abstract. |
| MODIN-FULL | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4940897/fullTextXML; PMID27453679; Introduction, Wastewater characteristics and identified operational paragraphs; other full-text passages not claimed inspected | supports | Inspected body paragraphs0,2,4,6,7,8,10,14,15,38,57,59,60,63 and80 support organic-matter/oxygen context and show alternative removal pathways. No one operating regime is generalized to all wastewater. |

## Limits And Additional Notes

- Complete assessment means the full record and applicable claims were reviewed, not that every claim is supported or that original source membership was recovered.
- Only the first three exact current BioSample/Organism descriptions per sheet were individually interpreted; remaining rows and study joins are an inventory, not per-member scientific review.
- Current official ontology/GOLD downloads were hash-verified and retain actual retrieval times. No pinned ontology, taxonomy or inventory refresh was performed.
- Undefined source groupings and CLASS/SEEDED interpretations remain unpromoted. Positive apparatus/material boundaries do not settle every ancestor source interpretation.
- This is a same-agent review, not independent approval. Earlier ad hoc reports and issue discussions do not replace this exact captured-input assessment.
- SSSOM/KGX product conformance with current kg-microbe modeling was not audited. Shared endpoint1398 remains separate.
- Full-corpus review is incomplete. This individual report does not establish a category-wide or all-corpus pass.
- All six cited abstracts and bibliographic identities were inspected. Selected relevant full-text sections of PMID27453679 were inspected. Publisher full-text retrieval failed for12180096,15276744,19515200 and18811652;17391331 was assessed from its abstract only. No full-text absence claim is made.
- Concerned and unknown causal-edge support remains open; a valid graph schema and resolving PMID are not evidence of the precise causal claim.
- Only a new immutable review bundle is written. No habitat, curation, generated-site or scientific-status changes are made by this review.
- No prior structured review names this exact target as reviewed or affected; older issue links are related scope, not silent resolution of other records.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T195959Z-waste_water
kind: record
repository: CultureBotAI/HabitatMech
title: 'Scientific record review: waste_water'
started_at: '2026-10-11T19:36:43.237024Z'
finished_at: '2026-10-11T19:59:59.611996Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Continuing agent has participated in HabitatMech curation and
    earlier reviews; this is not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'ENVO:00002001 denotes anthropogenically affected water, with contaminated-water
  and waste-material genera, not the treatment facility. Four current contributors
  reproduce: GOLD1140 ORGANISM, PREGO623 TAXON, MADIN524 TAXON and the qualitative
  environment table. Only two have ITEM decisions, correctly leaving SEEDED status.
  The16-edge organic-nitrogen biotreatment overlay has a bounded treatment scope,
  but several attached citations do not establish the precise causal claim in the
  inspected text.'
source:
  git_revision: 30167db0bf254f16bf774573bad9ebfcbe78d2d6
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
  - path: curation/causal_graphs/waste_water.yaml
    sha256: 299b5128af6cf5f7a61ce53304f1084e6eb045414b47cbcfd8832de095142aef
    role: context
  - path: curation/decisions.tsv
    sha256: 7cbec6d310b1aac248defdbe657e68c0cc1e848981230d2279e63f474c6f4c96
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: 2d41fc93db4939122b3909f2a412b84b679703948b10d9f02e12021442f71407
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 1c75d78798266f625984ddfbc493c0ea9eaacb654925f8d29c8aa337365b1f59
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
  - path: data/habitats/engineered/engineered__900b76ad.yaml
    sha256: 85154c9542e8e033e17cf631b06a462612229f3bcfdc1cdca0fc6cf73b9b9364
    role: context
  - path: data/habitats/engineered/waste_water.yaml
    sha256: 774c88de3169fb8ae95ea05deb748f21e036a35d0b21734c81c228493ec96056
    role: target
  - path: data/habitats/other/environmental_material.yaml
    sha256: f3916c9c17060dbb92c026d8e340be9478c37409361279bbb639642cdae29fe7
    role: context
  - path: data/habitats/other/waste_material.yaml
    sha256: fe8e42f2fe582f7984c8a12d7015ba28a3c417267590b545980d27811a13b757
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
  - path: history/mappings/activated_sludge__f91e662c/2026-10-10T214438Z-codex-gpt-5-5fbacd.yaml
    sha256: e5439df0e7e14c4afdb44d4b294ca042369090c2598e957b781981139e471bb1
    role: context
  - path: history/mappings/anaerobic_digestor__8332e1c2/2026-10-07T033543Z-codex-gpt-5-726504.yaml
    sha256: c9028918572bf82d26608229ffbf7cf3201c097ce8fa1885b72d7e68b73f7bf6
    role: context
  - path: history/mappings/river/2026-10-10T052811Z-codex-gpt-5-f5d017.yaml
    sha256: c32b9ce8e4a3752c6c832101ff30013cfe633febeb1a90ef623a28759585a58b
    role: context
  - path: history/mappings/wastewater__7fd6e093/2026-10-11T172128Z-codex-gpt-5-4d7f4d.yaml
    sha256: d2559f2942ac932c6c3319b2b39dad327429477e5bb5d27de14bcea9201afb59
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: reports/yaml_record_review/20260923T090833Z-activated_sludge__a6d16f1c.md
    sha256: 168f959d59a6611b1395062071bb243ca7351ad8552e390381a78f5b2f48c703
    role: context
  - path: reports/yaml_record_review/20260923T092905Z-activated_sludge__afe6b159.md
    sha256: 1b9c6ef0e81e3629775118084b0abdeab83bf3f7d7775995158cf705ac0a8180
    role: context
  - path: reports/yaml_record_review/20260923T112138Z-activated_sludge__ebcebab5.md
    sha256: baf6253b4eb08212a442ebc3ae771eeb8c834a063500d62403ab1aa7a6556ead
    role: context
  - path: reports/yaml_record_review/20260923T120225Z-activated_sludge__f91e662c.md
    sha256: fb715555e4d98d82a4366daec9a32b799d1d2491fc9e1eccacf0590f96c7d4b1
    role: context
  - path: reports/yaml_record_review/20260925T164936Z-wastewater__49e4fa74.md
    sha256: 2ce2551ade3ab9ddaf14dd3e35d168957e3a86b3eab5b5a62967bb136ba70d03
    role: context
  - path: reports/yaml_record_review/20260925T185226Z-wastewater__b5b1cb15.md
    sha256: 1b210be01ba566e5b2458d9a3bc4e520c59be68bd7eb22ce18246fb85258f1b8
    role: context
  - path: reports/yaml_record_review/20260925T222448Z-pulp_and_paper_wastewater.md
    sha256: b41d4828928d6daad732bcf20d68a64c0eb2c03eb9fcba5d94ee4d78dde87cfc
    role: context
  - path: reports/yaml_record_review/20261007T031059Z-anaerobic_digestor__8332e1c2.md
    sha256: e409f40fb795c1c16f599910af066efb5e24937db5164fdc8c21dceb4fd7818b
    role: context
  - path: reports/yaml_record_review/20261007T111633Z-bioreactor__12a40e2f.md
    sha256: 9730235016490d4722cc461e9e17905cfd089480c3648d52f001503618566686
    role: context
  - path: reports/yaml_record_review/20261008T085203Z-dissolved_organics_aerobic.md
    sha256: 4def9ac56d1fad6d0c057bb30ca7ec231a6c5c46a645ae0052ba9d145e69b534
    role: context
  - path: reports/yaml_record_review/20261008T121001Z-effluent.md
    sha256: 3b9c50eda0d1c955f47cb089985fd0f3978e67bb48d47084d40e72d4dc6ff71a
    role: context
  - path: reports/yaml_record_review/20261008T121219Z-effluent__7ff89bae.md
    sha256: 0c2b2c8a7f666413b112b28c96a809c978f0af22585daaf84864c958b284cc06
    role: context
  - path: reports/yaml_record_review/20261008T184140Z-hospital_wastewater.md
    sha256: 038e182c1bf164f5b9c45765aa9bc0a7359317f93b84b010269d07fc15d99c56
    role: context
  - path: reports/yaml_record_review/20261009T000732Z-industrial_wastewater.md
    sha256: 7f60987a5614e46907d709c299fdd7fc71d22000b5662b5108174c978a7bfa09
    role: context
  - path: research/habitats/engineered/dissolved-organics-anaerobic-habitatmech-gold-bb0eb00ccb-deep-research-claude_code.md
    sha256: 8d01ee8d97912ffeaa49d2091766972b09c91b18e181a9c9f1d866572e5fe7c6
    role: context
  - path: research/habitats/other/waste-gas-habitatmech-bacdive-3eec8fcfc4-deep-research-claude_code.md
    sha256: 7cb0023d6b84d6907fd8ace8dff73969415ce3d0b7cfbfbddaa17130ae4f3690
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
- target_id: ENVO:00002001
  path: data/habitats/engineered/waste_water.yaml
  label: waste water
  kind: generated
  record_class: HabitatRecord
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: Per-source grounding and native review-depth decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/gold_parent_exclusions.tsv
    role: Exact GOLD context-parent contribution decisions
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Curated definition, genus and lexical scope
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_terms.tsv
    role: Pinned ontology identity, labels, synonyms and definitions
  - repository: CultureBotAI/HabitatMech
    path: data/raw/ontology_subclass_edges.tsv
    role: Pinned ontology hierarchy
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Source harmonization and generated output
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitats.tsv
    role: Frozen Madin source habitat
  - repository: CultureBotAI/HabitatMech
    path: data/raw/madin_habitat_taxa.tsv
    role: Frozen Madin taxa
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitats.tsv
    role: Frozen PREGO habitat identity and count
  - repository: CultureBotAI/HabitatMech
    path: data/raw/prego_habitat_taxa.tsv
    role: Frozen top-ranked taxon associations
  - repository: CultureBotAI/HabitatMech
    path: data/raw/environment_parameters.tsv
    role: Frozen source-specific qualitative environmental parameter bands
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen source paths, nodes and ORGANISM counts
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/waste_water.yaml
    role: Authored causal graph nodes, directed edges and claim-level evidence
scope:
  description: Entire exact generated record and every contributing source, with scientific
    claim and parent-context assessment.
  selection: All forty remaining ENGINEERED records in stable slug order; individual
    full-record observations, not a sampled category verdict. Starting distinct completed-observation
    coverage448/3208 is not clean-verdict or current-input coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - ENVO:00002001
  exclusions:
  - target: Other3207 current records
    reason: Context/ancestor reads do not count as their completed full-record reviews.
checks:
- check_id: C0
  name: Native check on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002001
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=30167db0bf254f16bf774573bad9ebfcbe78d2d6
    just validate data/habitats/engineered/waste_water.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual successful check from 2026-10-11T19:39:14.068484Z to 2026-10-11T19:39:16.503966Z.
    Per-record applicability retained; full-corpus gates do not expand scientific
    coverage.
  evidence_ids:
  - R
  - RULES
- check_id: C1
  name: Native check on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002001
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=30167db0bf254f16bf774573bad9ebfcbe78d2d6
    just validate-strict data/habitats/engineered/terephthalate.yaml data/habitats/engineered/terrarium.yaml
    data/habitats/engineered/tetrachloroethylene.yaml data/habitats/engineered/tetrachloroethylene_and_derivatives.yaml
    data/habitats/engineered/textile.yaml data/habitats/engineered/thermophilic_digester.yaml
    data/habitats/engineered/thiocyanate.yaml data/habitats/engineered/thiocyanate_remediating.yaml
    data/habitats/engineered/tobacco_product.yaml data/habitats/engineered/tobacco_production.yaml
    data/habitats/engineered/town_canal.yaml data/habitats/engineered/track.yaml data/habitats/engineered/train_car.yaml
    data/habitats/engineered/uasb_upflow_anaerobic_sludge_blanket.yaml data/habitats/engineered/undefined_media.yaml
    data/habitats/engineered/unknown_material.yaml data/habitats/engineered/urban_waste.yaml
    data/habitats/engineered/urban_wastewater.yaml data/habitats/engineered/vaccine.yaml
    data/habitats/engineered/vegetable.yaml data/habitats/engineered/vermicompost.yaml
    data/habitats/engineered/vivarium.yaml data/habitats/engineered/waste_gas.yaml
    data/habitats/engineered/waste_treatment_plant.yaml data/habitats/engineered/waste_water.yaml
    data/habitats/engineered/wastewater_treatment_plant.yaml data/habitats/engineered/water.yaml
    data/habitats/engineered/water_channel_system.yaml data/habitats/engineered/water_microcosm.yaml
    data/habitats/engineered/water_treatment_plant__3df322b3.yaml data/habitats/engineered/wetland_sediment.yaml
    data/habitats/engineered/wetsalted_hide.yaml data/habitats/engineered/wheat_straw.yaml
    data/habitats/engineered/wood__d82aae22.yaml data/habitats/engineered/wood_chips.yaml
    data/habitats/engineered/woodchip_biofilm.yaml data/habitats/engineered/woodchip_bioreactor_wbr.yaml
    data/habitats/engineered/wooden_surface.yaml data/habitats/engineered/xylene.yaml
    data/habitats/engineered/zoo_waste.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual successful check from 2026-10-11T19:40:22.830722Z to 2026-10-11T19:40:32.094218Z.
    Per-record applicability retained; full-corpus gates do not expand scientific
    coverage.
  evidence_ids:
  - R
  - RULES
- check_id: C2
  name: Native check on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002001
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=30167db0bf254f16bf774573bad9ebfcbe78d2d6
    just verify-corpus
  exit_code: 0
  expected_exit_code: 0
  summary: Actual successful check from 2026-10-11T19:40:32.095315Z to 2026-10-11T19:40:52.911157Z.
    Per-record applicability retained; full-corpus gates do not expand scientific
    coverage.
  evidence_ids:
  - R
  - RULES
- check_id: C3
  name: Native check on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002001
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=30167db0bf254f16bf774573bad9ebfcbe78d2d6
    just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: Actual successful check from 2026-10-11T19:40:52.912319Z to 2026-10-11T19:41:56.664292Z.
    Per-record applicability retained; full-corpus gates do not expand scientific
    coverage.
  evidence_ids:
  - R
  - RULES
- check_id: C4
  name: Native check on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002001
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=30167db0bf254f16bf774573bad9ebfcbe78d2d6
    just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: Actual successful check from 2026-10-11T19:41:56.665596Z to 2026-10-11T19:42:06.494516Z.
    Per-record applicability retained; full-corpus gates do not expand scientific
    coverage.
  evidence_ids:
  - R
  - RULES
- check_id: C5
  name: Native check on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002001
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=30167db0bf254f16bf774573bad9ebfcbe78d2d6
    just validate-causal-all
  exit_code: 0
  expected_exit_code: 0
  summary: Actual successful check from 2026-10-11T19:42:06.495610Z to 2026-10-11T19:42:12.023268Z.
    Per-record applicability retained; full-corpus gates do not expand scientific
    coverage.
  evidence_ids:
  - R
  - RULES
- check_id: C6
  name: Native check on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002001
  command: env UV_CACHE_DIR=/private/tmp/habitatmech-review-ap-uv-cache RECORD_REVIEW_BASE=30167db0bf254f16bf774573bad9ebfcbe78d2d6
    just term-requests-check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual successful check from 2026-10-11T19:42:12.024508Z to 2026-10-11T19:42:39.328480Z.
    Per-record applicability retained; full-corpus gates do not expand scientific
    coverage.
  evidence_ids:
  - R
  - RULES
- check_id: C7
  name: Native check on captured scientific inputs
  required: true
  status: passed
  target_ids:
  - ENVO:00002001
  command: gh run view 38167383091 --json headSha,conclusion,status,jobs,url
  exit_code: 0
  expected_exit_code: 0
  summary: Actual successful check from 2026-10-11T19:39:18.548604Z to 2026-10-11T19:39:21.517288Z.
    Authoritative CI executed the full QC runner on exact clean baseline 30167db0bf254f16bf774573bad9ebfcbe78d2d6;
    ['776 passed, 3 skipped']. https://github.com/CultureBotAI/HabitatMech/actions/runs/38167383091
    This is verified CI on the exact scientific-input baseline, not a claim that local
    just qc was executed or new review files were already checked by CI.
  evidence_ids:
  - R
  - RULES
- check_id: REPRO
  name: Resolver and whole-document reconstruction
  required: false
  status: passed
  target_ids:
  - ENVO:00002001
  command: .venv/bin/python /private/tmp/habitatmech-review-aw-evidence.py
  exit_code: 0
  summary: All40 complete generated documents matched, and captured input hashes were
    reverified unchanged.
  evidence_ids:
  - RAW
  - CODE
- check_id: ORIGINAL
  name: Original assertion-level membership reconstruction
  required: false
  status: unavailable
  target_ids:
  - ENVO:00002001
  summary: Manifest-named original inputs were unavailable at the configured paths;
    bounded ignored-inclusive searches did not reconstruct complete original membership.
    Frozen inventories remain reproducible.
  evidence_ids:
  - SEARCH
- check_id: IMODULON
  name: iModulonDB applicability
  required: false
  status: not_applicable
  target_ids:
  - ENVO:00002001
  summary: No gene/regulator/expression-module claim in this exact record. Expression-module
    membership would not itself prove a habitat assertion.
  evidence_ids:
  - R
  - RULES
evidence:
- evidence_id: R
  kind: record_content
  reference: data/habitats/engineered/waste_water.yaml
  summary: 'ENVO:00002001 denotes anthropogenically affected water, with contaminated-water
    and waste-material genera, not the treatment facility. Four current contributors
    reproduce: GOLD1140 ORGANISM, PREGO623 TAXON, MADIN524 TAXON and the qualitative
    environment table. Only two have ITEM decisions, correctly leaving SEEDED status.
    The16-edge organic-nitrogen biotreatment overlay has a bounded treatment scope,
    but several attached citations do not establish the precise causal claim in the
    inspected text.'
  accessed_at: '2026-10-11T19:59:59.611996Z'
  support: supports
  locator: Entire captured YAML read, including every source, taxon, parameter, graph
    and generated event
- evidence_id: RULES
  kind: record_content
  reference: docs/CURATION.md; docs/HARMONIZATION.md; docs/RESEARCH.md; src/habitatmech/schema/habitatmech.yaml
  summary: Applied strict-genus and identity boundaries, source-specific count/score
    semantics, ITEM lifecycle, environmental-triad roles and edge-level evidence rules.
    Optional data are not invented for coverage.
  accessed_at: '2026-10-11T19:59:59.611996Z'
  support: supports
  locator: Native field checklist; SourceAttestation and CharacteristicTaxon contracts
- evidence_id: RAW
  kind: database
  reference: data/raw; curation/decisions.tsv; curation/term_requests.tsv; curation/gold_parent_exclusions.tsv
  summary: '{"curation/decisions.tsv": [{"data": {"category": "", "curator": "claude-opus-5",
    "date": "2026-08-13", "decision": "REVIEW", "grounding_status": "", "identifier":
    "habitatmech:GOLD.1a43260310", "notes": "Multi-source review pass: this record
    is attested by more than one independent vocabulary, and this source''s label
    or path was read against the record''s ontology term to check the merge is right.
    It agrees. Source concepts in the same pass whose labels did not agree were re-decided
    rather than endorsed; see the pass''s other decisions of the same date.", "object_id":
    "", "object_label": "", "relation": "", "review_depth": "ITEM"}, "logical_row":
    245}, {"data": {"category": "", "curator": "claude-opus-5", "date": "2026-08-13",
    "decision": "REVIEW", "grounding_status": "", "identifier": "habitatmech:PREGO.963b96a257",
    "notes": "Multi-source review pass: this record is attested by more than one independent
    vocabulary, and this source''s label or path was read against the record''s ontology
    term to check the merge is right. It agrees. Source concepts in the same pass
    whose labels did not agree were re-decided rather than endorsed; see the pass''s
    other decisions of the same date.", "object_id": "", "object_label": "", "relation":
    "", "review_depth": "ITEM"}, "logical_row": 1480}], "data/raw/environment_parameters.tsv":
    [{"data": {"cobo_simon_habitat": "NA", "env_type": "wastewater", "main_group":
    "Other", "parameter": "Nutrients", "term_ids": "ENVO:00002001", "term_labels":
    "waste water", "value": "high"}, "logical_row": 597}, {"data": {"cobo_simon_habitat":
    "NA", "env_type": "wastewater", "main_group": "Other", "parameter": "Pressure",
    "term_ids": "ENVO:00002001", "term_labels": "waste water", "value": "low"}, "logical_row":
    598}, {"data": {"cobo_simon_habitat": "NA", "env_type": "wastewater", "main_group":
    "Other", "parameter": "Temperature", "term_ids": "ENVO:00002001", "term_labels":
    "waste water", "value": "medium"}, "logical_row": 599}, {"data": {"cobo_simon_habitat":
    "NA", "env_type": "wastewater", "main_group": "Other", "parameter": "Water", "term_ids":
    "ENVO:00002001", "term_labels": "waste water", "value": "high"}, "logical_row":
    600}, {"data": {"cobo_simon_habitat": "NA", "env_type": "wastewater", "main_group":
    "Other", "parameter": "water variability", "term_ids": "ENVO:00002001", "term_labels":
    "waste water", "value": "permanently wet"}, "logical_row": 601}], "data/raw/gold_ecosystem_paths.tsv":
    [{"data": {"biosample_count": "0", "canonical_path": "Engineered > Wastewater",
    "depth": "2", "ecosystem": "Engineered", "ecosystem_category": "Wastewater", "ecosystem_subtype":
    "", "ecosystem_type": "", "gold_node_count": "4", "gold_node_ids": "gold.ecosystem:2886|gold.ecosystem:3508|gold.ecosystem:3833|gold.ecosystem:4264",
    "leaf_label": "Wastewater", "organism_count": "1140", "specific_ecosystem": "",
    "study_count": "0", "total_assertions": "1140"}, "logical_row": 38}], "data/raw/gold_path_biosamples.tsv":
    [{"data": {"biosample_count": "23", "canonical_path": "Engineered > Wastewater",
    "ecosystem_path_id": "4264"}, "logical_row": 492}], "data/raw/isolation_source_groundings.tsv":
    [{"data": {"confidence": "high", "curator": "codex_review_fix", "mapping_justification":
    "semapv:ManualMappingCuration", "object_id": "ENVO:00002001", "object_label":
    "waste water", "object_source": "ENVO", "predicate_id": "skos:exactMatch", "source_dataset":
    "bacdive", "subject_label": "Wastewater", "subject_label_normalized": "wastewater",
    "verified_date": "2026-05-02"}, "logical_row": 343}], "data/raw/madin_habitat_taxa.tsv":
    [{"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id":
    "NCBITaxon:1058", "taxon_label": "thiocapsa_roseopersicina"}, "logical_row": 236},
    {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id":
    "NCBITaxon:1089553", "taxon_label": "Thermacetogenium phaeum DSM 12270"}, "logical_row":
    237}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id":
    "NCBITaxon:1120924", "taxon_label": "Acinetobacter baylyi DSM 14961"}, "logical_row":
    238}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id":
    "NCBITaxon:1120925", "taxon_label": "Acinetobacter bouvetii DSM 14964"}, "logical_row":
    239}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id":
    "NCBITaxon:1120927", "taxon_label": "Acinetobacter tandoii DSM 14970"}, "logical_row":
    240}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id":
    "NCBITaxon:1120928", "taxon_label": "Acinetobacter tjernbergiae DSM 14971"}, "logical_row":
    241}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id":
    "NCBITaxon:1120929", "taxon_label": "Acinetobacter towneri DSM 14962"}, "logical_row":
    242}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001", "taxon_id":
    "NCBITaxon:1120962", "taxon_label": "Alcaligenes faecalis phenolicus DSM 16503"},
    "logical_row": 243}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001",
    "taxon_id": "NCBITaxon:1121109", "taxon_label": "Bifidobacterium minimum DSM 20102"},
    "logical_row": 244}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001",
    "taxon_id": "NCBITaxon:1121110", "taxon_label": "Bifidobacterium subtile DSM 20096"},
    "logical_row": 245}, {"data": {"corroborated_by": "PREGO", "madin_id": "ENVO:00002001",
    "taxon_id": "NCBITaxon:1121111", "taxon_label": "Bifidobacterium thermacidophilum
    thermacidophilum DSM 15837"}, "logical_row": 246}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121123", "taxon_label":
    "Brevundimonas aveniformis DSM 17977"}, "logical_row": 247}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121255", "taxon_label":
    "Caenimonas koreensis DSM 17982"}, "logical_row": 248}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121262", "taxon_label":
    "Caloramator proteoclasticus DSM 10124"}, "logical_row": 249}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121271", "taxon_label":
    "Gemmobacter nectariphilus DSM 15620"}, "logical_row": 250}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121285", "taxon_label":
    "Chryseobacterium caeni DSM 17710"}, "logical_row": 251}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121286", "taxon_label":
    "Chryseobacterium daeguense DSM 19388"}, "logical_row": 252}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121344", "taxon_label":
    "Clostridium viride DSM 6836"}, "logical_row": 253}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121348", "taxon_label":
    "Comamonas badia DSM 17552"}, "logical_row": 254}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121378", "taxon_label":
    "Deinococcus aquatilis DSM 23025"}, "logical_row": 255}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121393", "taxon_label":
    "Desulfatibacillum alkenivorans DSM 16219"}, "logical_row": 256}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121405", "taxon_label":
    "Desulfococcus multivorans DSM 2059"}, "logical_row": 257}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121433", "taxon_label":
    "Desulfovermiculus halophilus DSM 18834"}, "logical_row": 258}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121438", "taxon_label":
    "Desulfovibrio alcoholivorans DSM 5433"}, "logical_row": 259}, {"data": {"corroborated_by":
    "PREGO", "madin_id": "ENVO:00002001", "taxon_id": "NCBITaxon:1121440", "taxon_label":
    "Desulfovibrio aminophilus DSM 12254"}, "logical_row": 260}], "data/raw/madin_habitats.tsv":
    [{"data": {"label": "waste water", "madin_id": "ENVO:00002001", "taxon_count":
    "524", "vocabulary": "ENVO"}, "logical_row": 14}], "data/raw/ontology_subclass_edges.tsv":
    [{"data": {"object": "ENVO:00002186", "predicate": "rdfs:subClassOf", "subject":
    "ENVO:00002001"}, "logical_row": 5263}, {"data": {"object": "ENVO:00002264", "predicate":
    "rdfs:subClassOf", "subject": "ENVO:00002001"}, "logical_row": 5264}], "data/raw/ontology_terms.tsv":
    [{"data": {"definition": "Water that has been adversely affected in quality by
    anthropogenic influence.", "deprecated": "", "directly_referenced": "TRUE", "label":
    "waste water", "label_only": "FALSE", "ontology": "ENVO", "synonyms": "", "term_id":
    "ENVO:00002001"}, "logical_row": 7160}], "data/raw/prego_habitat_taxa.tsv": [{"data":
    {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "1", "taxon_id":
    "NCBITaxon:1046983", "taxon_label": "Hydrogenedentes bacterium JGI 0000059-N10"},
    "logical_row": 5416}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank":
    "2", "taxon_id": "NCBITaxon:1047009", "taxon_label": "Fidelibacterota bacterium
    SCGC AAA011-A05"}, "logical_row": 5417}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "3", "taxon_id": "NCBITaxon:1047012", "taxon_label": "Caldiserica
    bacterium JGI 0000059-M03"}, "logical_row": 5418}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "4", "taxon_id": "NCBITaxon:1047053", "taxon_label": "Atribacteria
    bacterium JGI 0000059-I14"}, "logical_row": 5419}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "5", "taxon_id": "NCBITaxon:1047055", "taxon_label": "Fidelibacterota
    bacterium JGI 0000039-D08"}, "logical_row": 5420}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "6", "taxon_id": "NCBITaxon:1047056", "taxon_label": "Fidelibacterota
    bacterium JGI 0000039-E15"}, "logical_row": 5421}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "7", "taxon_id": "NCBITaxon:1047058", "taxon_label": "Fidelibacterota
    bacterium JGI 0000039-O11"}, "logical_row": 5422}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "8", "taxon_id": "NCBITaxon:1047059", "taxon_label": "Fidelibacterota
    bacterium JGI 0000059-D20"}, "logical_row": 5423}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "9", "taxon_id": "NCBITaxon:1047060", "taxon_label": "Fidelibacterota
    bacterium JGI 0000059-E23"}, "logical_row": 5424}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "10", "taxon_id": "NCBITaxon:1047061", "taxon_label": "Fidelibacterota
    bacterium JGI 0000059-L03"}, "logical_row": 5425}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "11", "taxon_id": "NCBITaxon:1047063", "taxon_label": "WS1 bacterium
    JGI 0000059-K21"}, "logical_row": 5426}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "12", "taxon_id": "NCBITaxon:1047073", "taxon_label": "Cloacimonetes
    bacterium JGI 0000039-I17"}, "logical_row": 5427}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "13", "taxon_id": "NCBITaxon:1047076", "taxon_label": "Cloacimonetes
    bacterium JGI 0000039-M09"}, "logical_row": 5428}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "14", "taxon_id": "NCBITaxon:1047077", "taxon_label": "Cloacimonetes
    bacterium JGI 0000039-P09"}, "logical_row": 5429}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "15", "taxon_id": "NCBITaxon:1047078", "taxon_label": "Cloacimonetes
    bacterium JGI 0000059-F17"}, "logical_row": 5430}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "16", "taxon_id": "NCBITaxon:1047079", "taxon_label": "Cloacimonetes
    bacterium JGI 0000059-L07"}, "logical_row": 5431}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "17", "taxon_id": "NCBITaxon:1047080", "taxon_label": "Cloacimonetes
    bacterium JGI 0000059-P03"}, "logical_row": 5432}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "18", "taxon_id": "NCBITaxon:1047081", "taxon_label": "Cloacimonetes
    bacterium JGI 0000059-P11"}, "logical_row": 5433}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002001",
    "prego_score": "4", "rank": "19", "taxon_id": "NCBITaxon:1058", "taxon_label":
    "Thiocapsa roseopersicina"}, "logical_row": 5434}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "MADIN", "direct_flag": "TRUE", "prego_id": "ENVO:00002001",
    "prego_score": "4", "rank": "20", "taxon_id": "NCBITaxon:1089553", "taxon_label":
    "Thermacetogenium phaeum DSM 12270"}, "logical_row": 5435}, {"data": {"channels":
    "annotated_genomes_isolates", "corroborated_by": "", "direct_flag": "TRUE", "prego_id":
    "ENVO:00002001", "prego_score": "4", "rank": "21", "taxon_id": "NCBITaxon:1104568",
    "taxon_label": "Synergistetes bacterium JGI 0000079-D21"}, "logical_row": 5436},
    {"data": {"channels": "annotated_genomes_isolates", "corroborated_by": "", "direct_flag":
    "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank": "22", "taxon_id":
    "NCBITaxon:1104603", "taxon_label": "Atribacteria bacterium JGI 0000079-L04"},
    "logical_row": 5437}, {"data": {"channels": "annotated_genomes_isolates", "corroborated_by":
    "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score": "4", "rank":
    "23", "taxon_id": "NCBITaxon:1104604", "taxon_label": "Atribacteria bacterium
    JGI 0000079-F20"}, "logical_row": 5438}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "24", "taxon_id": "NCBITaxon:1104605", "taxon_label": "Armatimonadetes
    bacterium JGI 0000077-K19"}, "logical_row": 5439}, {"data": {"channels": "annotated_genomes_isolates",
    "corroborated_by": "", "direct_flag": "TRUE", "prego_id": "ENVO:00002001", "prego_score":
    "4", "rank": "25", "taxon_id": "NCBITaxon:1104619", "taxon_label": "Hydrogenedentes
    bacterium JGI 0000077-D07"}, "logical_row": 5440}], "data/raw/prego_habitats.tsv":
    [{"data": {"biolink_category": "biolink:OntologyClass", "channels": "annotated_genomes_isolates|environmental_samples",
    "direct_assertion_count": "719", "max_prego_score": "4", "ontology": "ENVO", "prego_id":
    "ENVO:00002001", "prego_synonyms": "waste water|waste waters", "taxon_count":
    "623"}, "logical_row": 93}]}'
  accessed_at: '2026-10-11T19:59:59.611996Z'
  support: supports
  locator: Exact logical TSV rows (header is row1), not nearby-path or descendant
    membership
- evidence_id: CODE
  kind: record_content
  reference: src/habitatmech/seed.py
  summary: '{"reviewed_sources": 2, "routes": [{"actual": {"category": null, "contributes_grounding":
    true, "decision": null, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": null, "reviewed":
    false, "route": "environments_table_self_grounded"}, "automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "EXACT", "identifier": "ENVO:00002001", "mapping_predicate":
    null, "reviewed": false, "route": "environments_table_self_grounded"}, "minted":
    "habitatmech:ENVIRONMENTS_TABLE.5bb62a0436", "source": "ENVIRONMENTS_TABLE", "source_id":
    "wastewater"}, {"actual": {"category": null, "contributes_grounding": true, "decision":
    {"category": "", "curator": "claude-opus-5", "date": "2026-08-13", "decision":
    "REVIEW", "grounding_status": "", "identifier": "habitatmech:GOLD.1a43260310",
    "notes": "Multi-source review pass: this record is attested by more than one independent
    vocabulary, and this source''s label or path was read against the record''s ontology
    term to check the merge is right. It agrees. Source concepts in the same pass
    whose labels did not agree were re-decided rather than endorsed; see the pass''s
    other decisions of the same date.", "object_id": "", "object_label": "", "relation":
    "parent", "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": "skos:exactMatch",
    "reviewed": true, "route": "curated_review_of_gold_mapping_table"}, "automatic":
    {"category": null, "contributes_grounding": true, "decision": null, "extra_parents":
    [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier": "ENVO:00002001",
    "mapping_predicate": "skos:exactMatch", "reviewed": false, "route": "gold_mapping_table"},
    "minted": "habitatmech:GOLD.1a43260310", "source": "GOLD", "source_id": "gold.ecosystem:2886"},
    {"actual": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier":
    "ENVO:00002001", "mapping_predicate": null, "reviewed": false, "route": "madin_self_grounded"},
    "automatic": {"category": null, "contributes_grounding": true, "decision": null,
    "extra_parents": [], "extra_xrefs": [], "grounding_status": "EXACT", "identifier":
    "ENVO:00002001", "mapping_predicate": null, "reviewed": false, "route": "madin_self_grounded"},
    "minted": "habitatmech:MADIN.da9572e4ca", "source": "MADIN", "source_id": "ENVO:00002001"},
    {"actual": {"category": null, "contributes_grounding": true, "decision": {"category":
    "", "curator": "claude-opus-5", "date": "2026-08-13", "decision": "REVIEW", "grounding_status":
    "", "identifier": "habitatmech:PREGO.963b96a257", "notes": "Multi-source review
    pass: this record is attested by more than one independent vocabulary, and this
    source''s label or path was read against the record''s ontology term to check
    the merge is right. It agrees. Source concepts in the same pass whose labels did
    not agree were re-decided rather than endorsed; see the pass''s other decisions
    of the same date.", "object_id": "", "object_label": "", "relation": "parent",
    "review_depth": "ITEM"}, "extra_parents": [], "extra_xrefs": [], "grounding_status":
    "EXACT", "identifier": "ENVO:00002001", "mapping_predicate": null, "reviewed":
    true, "route": "curated_review_of_prego_self_grounded"}, "automatic": {"category":
    null, "contributes_grounding": true, "decision": null, "extra_parents": [], "extra_xrefs":
    [], "grounding_status": "EXACT", "identifier": "ENVO:00002001", "mapping_predicate":
    null, "reviewed": false, "route": "prego_self_grounded"}, "minted": "habitatmech:PREGO.963b96a257",
    "source": "PREGO", "source_id": "ENVO:00002001"}], "source_concepts": 4}'
  accessed_at: '2026-10-11T19:59:59.611996Z'
  support: supports
  locator: Executed resolver, item/class decisions and full-document reproduction;
    all40 documents match
- evidence_id: ONT
  kind: authority
  reference: https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl
  summary: '{"ENVO:00002001": {"definitions": ["Water that has been adversely affected
    in quality by anthropogenic influence."], "deprecated": [], "equivalents": [],
    "labels": ["waste water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002186",
    "http://purl.obolibrary.org/obo/ENVO_00002264"], "replacements": [], "synonyms":
    {"hasBroadSynonym": [], "hasExactSynonym": [], "hasNarrowSynonym": [], "hasRelatedSynonym":
    []}}, "ENVO:00002186": {"definitions": [], "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00002006"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/ENVO_02000200"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"nested": true}]}]}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}],
    "labels": ["contaminated water"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00002006",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/ENVO_02000200"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/CHEBI_24431"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000087"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/CHEBI_78298"]}],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": ["polluted
    water"], "hasNarrowSynonym": [], "hasRelatedSynonym": []}}, "ENVO:00002264": {"definitions":
    ["A material which is not the desired output of a process and which is typically
    the input of a process which removes it from its producer (e.g. a disposal process)."],
    "deprecated": [], "equivalents": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type":
    ["http://www.w3.org/2002/07/owl#Class"], "http://www.w3.org/2002/07/owl#intersectionOf":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first": ["http://purl.obolibrary.org/obo/ENVO_00010483"],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#first":
    [{"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000087"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000665"]}],
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest": ["http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"]}]}]}],
    "labels": ["waste material"], "parents": ["http://purl.obolibrary.org/obo/ENVO_00010483",
    {"http://www.w3.org/1999/02/22-rdf-syntax-ns#type": ["http://www.w3.org/2002/07/owl#Restriction"],
    "http://www.w3.org/2002/07/owl#onProperty": ["http://purl.obolibrary.org/obo/RO_0000087"],
    "http://www.w3.org/2002/07/owl#someValuesFrom": ["http://purl.obolibrary.org/obo/ENVO_01000665"]}],
    "replacements": [], "synonyms": {"hasBroadSynonym": [], "hasExactSynonym": [],
    "hasNarrowSynonym": [], "hasRelatedSynonym": []}}} Same-day cached source; original
    access time retained, SHA256 reverified 2026-10-11T19:38:15.215491+00:00.'
  accessed_at: '2026-10-11T13:21:47.927208Z'
  support: supports
  locator: Named current OWL target/parent/candidate classes; direct axioms distinguished
    from related properties; no automatic remapping
  snapshot_sha256: a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c
- evidence_id: PARENT
  kind: record_content
  reference: data/habitats/engineered/engineered__900b76ad.yaml; data/habitats/other/waste_material.yaml;
    data/habitats/other/environmental_material.yaml
  summary: '{"ENVO:00002264": {"definition": "A material which is not the desired
    output of a process and which is typically the input of a process which removes
    it from its producer (e.g. a disposal process).", "grounding_status": "EXACT",
    "label": "waste material", "parent_habitats": ["ENVO:00010483"]}, "ENVO:00010483":
    {"definition": "A material entity which other material entities in an environmental
    system are primarily or partially composed of.", "grounding_status": "EXACT",
    "label": "environmental material", "parent_habitats": null}, "habitatmech:GOLD.2acb39dd08":
    {"definition": null, "grounding_status": "UNGROUNDED", "label": "Engineered",
    "parent_habitats": null}}'
  accessed_at: '2026-10-11T19:59:59.611996Z'
  support: supports
  locator: Available generated ancestor identity/context; external-only parents are
    assessed in ONT. Context reads do not count as full-record coverage of ancestors.
- evidence_id: BULK
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=site_excel
  summary: 'Full positional census counts={"Biosample": 0, "Organism": 1002, "SequencingProject":
    878}; inspected first three descriptions per sample/organism sheet={"Biosample":
    [], "Organism": [{"data": {"ORGANISM GOLD ID": "Go0000015", "ORGANISM HABITAT":
    "Soil|Host|Fresh water|Sludge|Wastewater|Oil fields", "ORGANISM ISOLATION HOST
    NAME": "", "ORGANISM NAME": "Delftia acidovorans SPH-1", "ORGANISM SAMPLE COLLECTION
    SITE": "Sludge from communal sewage treatment plant; Germany"}, "row": 14}, {"data":
    {"ORGANISM GOLD ID": "Go0000051", "ORGANISM HABITAT": "Fresh water", "ORGANISM
    ISOLATION HOST NAME": "", "ORGANISM NAME": "Pseudothermotoga lettingae TMO", "ORGANISM
    SAMPLE COLLECTION SITE": "Thermophilic sulfate-reducing bioreactor; The Netherlands,
    Wageningen"}, "row": 47}, {"data": {"ORGANISM GOLD ID": "Go0000071", "ORGANISM
    HABITAT": "Host|Sludge", "ORGANISM ISOLATION HOST NAME": "", "ORGANISM NAME":
    "Parvibaculum lavamentivorans DS-1", "ORGANISM SAMPLE COLLECTION SITE": "Sewage
    treatment plant in Germany"}, "row": 66}]}. Zero exact matches is bounded to this
    export, not biological absence. Other member rows and study joins were indexed,
    not individually assessed. Frozen counts are unchanged. Same-day cached source;
    original access time retained, SHA256 reverified 2026-10-11T19:38:16.257007+00:00.'
  accessed_at: '2026-10-11T13:21:51.155056Z'
  support: supports
  locator: Exact five-position tuples; blank/Unclassified normalization preserves
    internal positions; 245071/532036/637051/63807 sheet rows including headers
  snapshot_sha256: b222fa9df89ffbd1a30897a1e7302da363c57b463d9948ecc9bfcb9304b4a96f
- evidence_id: CLASS
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  summary: '[{"row": 466, "slug": "waste_water", "path": "Engineered > Wastewater",
    "values": ["4264", "Engineered", "Wastewater", "Unclassified", "Unclassified",
    "Unclassified"]}] Same-day cached source; original access time retained, SHA256
    reverified 2026-10-11T19:38:16.258000+00:00.'
  accessed_at: '2026-10-11T13:21:50.982232Z'
  support: supports
  locator: Later official five-position classification rows, not original membership
    reconstruction
  snapshot_sha256: 78ed6ce1c3799a2d6ef2d17e4a9eeee5da48eef78df0b71079c0f942555e5e7d
- evidence_id: TAX
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1046983%2C1047009%2C1047012%2C1047053%2C1047055%2C1047056%2C1047058%2C1047059%2C1047060%2C1047061%2C1047063%2C1047073%2C1047076%2C1047077%2C1047078%2C1047079%2C1047080%2C1047081%2C1058%2C1089553%2C1104568%2C1104603%2C1104604%2C1104605%2C1104619%2C1120924%2C1120925%2C1120927%2C1120928%2C1120929%2C1120962%2C1121109%2C1121110%2C1121111%2C1121123%2C1121255%2C1121262%2C1121271%2C1121285%2C1121286%2C1121344%2C1121348%2C1121378%2C1121393%2C1121405%2C1121433%2C1121438%2C1121440%2C1121889%2C1121933%2C1122132%2C1123024%2C1123399%2C1123400%2C1223541%2C1259795%2C1304875%2C1399774%2C1469607%2C1667%2C1720%2C1871044%2C1871047%2C1871616%2C1872122%2C214688%2C2164%2C264023%2C265072%2C28892%2C306%2C310396%2C317577%2C338966%2C340%2C361%2C370973%2C424718%2C469547%2C469551%2C53408%2C53463%2C558173%2C572547%2C584708%2C622617%2C65735%2C680375%2C76114%2C866499%2C916&retmode=xml
  summary: '[{"current_name": "Thiocapsa roseopersicina", "frozen_label": "Thiocapsa
    roseopersicina", "id": "1058", "rank": "species"}, {"current_name": "Thermacetogenium
    phaeum DSM 12270", "frozen_label": "Thermacetogenium phaeum DSM 12270", "id":
    "1089553", "rank": "strain"}, {"current_name": "Acinetobacter baylyi DSM 14961
    = CIP 107474", "frozen_label": "Acinetobacter baylyi DSM 14961", "id": "1120924",
    "rank": "strain"}, {"current_name": "Acinetobacter bouvetii DSM 14964 = CIP 107468",
    "frozen_label": "Acinetobacter bouvetii DSM 14964", "id": "1120925", "rank": "strain"},
    {"current_name": "Acinetobacter tandoii DSM 14970 = CIP 107469", "frozen_label":
    "Acinetobacter tandoii DSM 14970", "id": "1120927", "rank": "strain"}, {"current_name":
    "Acinetobacter tjernbergiae DSM 14971 = CIP 107465", "frozen_label": "Acinetobacter
    tjernbergiae DSM 14971", "id": "1120928", "rank": "strain"}, {"current_name":
    "Acinetobacter towneri DSM 14962 = CIP 107472", "frozen_label": "Acinetobacter
    towneri DSM 14962", "id": "1120929", "rank": "strain"}, {"current_name": "Alcaligenes
    phenolicus DSM 16503", "frozen_label": "Alcaligenes faecalis phenolicus DSM 16503",
    "id": "1120962", "rank": "strain"}, {"current_name": "Bifidobacterium minimum
    DSM 20102", "frozen_label": "Bifidobacterium minimum DSM 20102", "id": "1121109",
    "rank": "strain"}, {"current_name": "Bifidobacterium subtile DSM 20096", "frozen_label":
    "Bifidobacterium subtile DSM 20096", "id": "1121110", "rank": "strain"}, {"current_name":
    "Bifidobacterium thermacidophilum subsp. thermacidophilum DSM 15837", "frozen_label":
    "Bifidobacterium thermacidophilum thermacidophilum DSM 15837", "id": "1121111",
    "rank": "strain"}, {"current_name": "Brevundimonas aveniformis DSM 17977", "frozen_label":
    "Brevundimonas aveniformis DSM 17977", "id": "1121123", "rank": "strain"}, {"current_name":
    "Caenimonas koreensis DSM 17982", "frozen_label": "Caenimonas koreensis DSM 17982",
    "id": "1121255", "rank": "strain"}, {"current_name": "Caloramator proteoclasticus
    DSM 10124", "frozen_label": "Caloramator proteoclasticus DSM 10124", "id": "1121262",
    "rank": "strain"}, {"current_name": "Gemmobacter nectariphilus DSM 15620", "frozen_label":
    "Gemmobacter nectariphilus DSM 15620", "id": "1121271", "rank": "strain"}, {"current_name":
    "Epilithonimonas caeni DSM 17710", "frozen_label": "Chryseobacterium caeni DSM
    17710", "id": "1121285", "rank": "strain"}, {"current_name": "Chryseobacterium
    daeguense DSM 19388", "frozen_label": "Chryseobacterium daeguense DSM 19388",
    "id": "1121286", "rank": "strain"}, {"current_name": "[Clostridium] viride DSM
    6836", "frozen_label": "Clostridium viride DSM 6836", "id": "1121344", "rank":
    "strain"}, {"current_name": "Comamonas badia DSM 17552", "frozen_label": "Comamonas
    badia DSM 17552", "id": "1121348", "rank": "strain"}, {"current_name": "Deinococcus
    aquatilis DSM 23025", "frozen_label": "Deinococcus aquatilis DSM 23025", "id":
    "1121378", "rank": "strain"}, {"current_name": "Desulfatibacillum alkenivorans
    DSM 16219", "frozen_label": "Desulfatibacillum alkenivorans DSM 16219", "id":
    "1121393", "rank": "strain"}, {"current_name": "Desulfococcus multivorans DSM
    2059", "frozen_label": "Desulfococcus multivorans DSM 2059", "id": "1121405",
    "rank": "strain"}, {"current_name": "Desulfovermiculus halophilus DSM 18834",
    "frozen_label": "Desulfovermiculus halophilus DSM 18834", "id": "1121433", "rank":
    "strain"}, {"current_name": "Solidesulfovibrio alcoholivorans DSM 5433", "frozen_label":
    "Desulfovibrio alcoholivorans DSM 5433", "id": "1121438", "rank": "strain"}, {"current_name":
    "Desulfovibrio aminophilus DSM 12254", "frozen_label": "Desulfovibrio aminophilus
    DSM 12254", "id": "1121440", "rank": "strain"}, {"current_name": "Hydrogenedentes
    bacterium JGI 0000059-N10", "frozen_label": "Hydrogenedentes bacterium JGI 0000059-N10",
    "id": "1046983", "rank": "species"}, {"current_name": "Fidelibacterota bacterium
    SCGC AAA011-A05", "frozen_label": "Fidelibacterota bacterium SCGC AAA011-A05",
    "id": "1047009", "rank": "species"}, {"current_name": "Caldiserica bacterium JGI
    0000059-M03", "frozen_label": "Caldiserica bacterium JGI 0000059-M03", "id": "1047012",
    "rank": "species"}, {"current_name": "Atribacteria bacterium JGI 0000059-I14",
    "frozen_label": "Atribacteria bacterium JGI 0000059-I14", "id": "1047053", "rank":
    "species"}, {"current_name": "Fidelibacterota bacterium JGI 0000039-D08", "frozen_label":
    "Fidelibacterota bacterium JGI 0000039-D08", "id": "1047055", "rank": "species"},
    {"current_name": "Fidelibacterota bacterium JGI 0000039-E15", "frozen_label":
    "Fidelibacterota bacterium JGI 0000039-E15", "id": "1047056", "rank": "species"},
    {"current_name": "Fidelibacterota bacterium JGI 0000039-O11", "frozen_label":
    "Fidelibacterota bacterium JGI 0000039-O11", "id": "1047058", "rank": "species"},
    {"current_name": "Fidelibacterota bacterium JGI 0000059-D20", "frozen_label":
    "Fidelibacterota bacterium JGI 0000059-D20", "id": "1047059", "rank": "species"},
    {"current_name": "Fidelibacterota bacterium JGI 0000059-E23", "frozen_label":
    "Fidelibacterota bacterium JGI 0000059-E23", "id": "1047060", "rank": "species"},
    {"current_name": "Fidelibacterota bacterium JGI 0000059-L03", "frozen_label":
    "Fidelibacterota bacterium JGI 0000059-L03", "id": "1047061", "rank": "species"},
    {"current_name": "WS1 bacterium JGI 0000059-K21", "frozen_label": "WS1 bacterium
    JGI 0000059-K21", "id": "1047063", "rank": "species"}, {"current_name": "Cloacimonetes
    bacterium JGI 0000039-I17", "frozen_label": "Cloacimonetes bacterium JGI 0000039-I17",
    "id": "1047073", "rank": "species"}, {"current_name": "Cloacimonetes bacterium
    JGI 0000039-M09", "frozen_label": "Cloacimonetes bacterium JGI 0000039-M09", "id":
    "1047076", "rank": "species"}, {"current_name": "Cloacimonetes bacterium JGI 0000039-P09",
    "frozen_label": "Cloacimonetes bacterium JGI 0000039-P09", "id": "1047077", "rank":
    "species"}, {"current_name": "Cloacimonetes bacterium JGI 0000059-F17", "frozen_label":
    "Cloacimonetes bacterium JGI 0000059-F17", "id": "1047078", "rank": "species"},
    {"current_name": "Cloacimonetes bacterium JGI 0000059-L07", "frozen_label": "Cloacimonetes
    bacterium JGI 0000059-L07", "id": "1047079", "rank": "species"}, {"current_name":
    "Cloacimonetes bacterium JGI 0000059-P03", "frozen_label": "Cloacimonetes bacterium
    JGI 0000059-P03", "id": "1047080", "rank": "species"}, {"current_name": "Cloacimonetes
    bacterium JGI 0000059-P11", "frozen_label": "Cloacimonetes bacterium JGI 0000059-P11",
    "id": "1047081", "rank": "species"}, {"current_name": "Synergistetes bacterium
    JGI 0000079-D21", "frozen_label": "Synergistetes bacterium JGI 0000079-D21", "id":
    "1104568", "rank": "species"}, {"current_name": "Atribacteria bacterium JGI 0000079-L04",
    "frozen_label": "Atribacteria bacterium JGI 0000079-L04", "id": "1104603", "rank":
    "species"}, {"current_name": "Atribacteria bacterium JGI 0000079-F20", "frozen_label":
    "Atribacteria bacterium JGI 0000079-F20", "id": "1104604", "rank": "species"},
    {"current_name": "Armatimonadetes bacterium JGI 0000077-K19", "frozen_label":
    "Armatimonadetes bacterium JGI 0000077-K19", "id": "1104605", "rank": "species"},
    {"current_name": "Hydrogenedentes bacterium JGI 0000077-D07", "frozen_label":
    "Hydrogenedentes bacterium JGI 0000077-D07", "id": "1104619", "rank": "species"}].
    All named IDs resolve directly. Current labels do not silently replace frozen
    source labels. Taxonomy resolution does not validate the habitat association.'
  accessed_at: '2026-10-11T19:39:23.103151Z'
  support: supports
  locator: 'NCBI Taxonomy EFetch XML: each target-associated TaxId, ScientificName
    and Rank; OtherNames inspected for five label differences'
  snapshot_sha256: 1ff1e1289581b7167b07731ea046b062dfb57870bb29d7426a356bdd27be271e
- evidence_id: SEARCH
  kind: search
  reference: curation; history; research; reports; reviews; data/raw; data/habitats;
    conf
  summary: 'Identifier/label/slug/source-path search included hidden and ignored files
    in these roots. Structured coverage used Path.rglob. Original manifest paths and
    bounded upstream data/build traversal={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe",
    "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv",
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
    "exit_code": 0, "matches": [], "stderr": ""}]}. This is not a global filesystem
    absence claim, and older ad hoc reports are not automatically completed structured
    coverage.'
  accessed_at: '2026-10-11T19:59:59.611996Z'
  support: supports
  locator: Bounded ignored-independent searches
  search_scope: 'Identifier/label/slug/source-path search included hidden and ignored
    files in these roots. Structured coverage used Path.rglob. Original manifest paths
    and bounded upstream data/build traversal={"configured_root": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe",
    "root_exists": true, "exact_paths": [{"path": "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/raw/gold/GOLD_nodes.tsv",
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
    "exit_code": 0, "matches": [], "stderr": ""}]}. This is not a global filesystem
    absence claim, and older ad hoc reports are not automatically completed structured
    coverage.'
- evidence_id: GRAPH
  kind: record_content
  reference: curation/causal_graphs/waste_water.yaml
  summary: Entire overlay and generated16-edge graph read. Node identities, typed
    directions, edge descriptions, citations, snippets and history match. Scope is
    organic-nitrogen biotreatment, not a universal process claim for all wastewater.
  accessed_at: '2026-10-11T19:59:59.611996Z'
  support: supports
  locator: All nodes/edges; history and generated attachment
- evidence_id: PMID-12180096
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12180096+AND+SRC%3AMED&format=json&resultType=core
  summary: The review abstract establishes nutrient-removal guilds in sewage treatment;
    it does not expose the specific substrate, oxygen-gradient or nitrate-conversion
    passages needed by several graph edges.
  accessed_at: '2026-10-11T19:39:24.491640Z'
  support: supports
  locator: PMID12180096; DOI10.1016/s0958-1669(02)00315-4; title, full abstract and
    bibliographic metadata
  snapshot_sha256: 58f5549c329e437a7e8baa85e97aeda2d9a1be43902e1978d6d66d0284b6d590
- evidence_id: PMID-27453679
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27453679+AND+SRC%3AMED&format=json&resultType=core
  summary: Abstract and inspected full-text introduction/characterization paragraphs
    support aerobic organic oxidation, coupled growth and oxygen demand; the article
    also emphasizes nonoxidative removal routes.
  accessed_at: '2026-10-11T19:39:25.695985Z'
  support: supports
  locator: PMID27453679; DOI10.1080/10643389.2016.1149903; title, full abstract and
    bibliographic metadata
  snapshot_sha256: 1a768566918e6b0bd324c6dc3ee8dcf4fdbc8b933ca1e630358788e7b78ef554
- evidence_id: PMID-15276744
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15276744+AND+SRC%3AMED&format=json&resultType=core
  summary: Controlled chemostat and full-scale DO comparisons directly support oxygen-dependent
    AOB ecology/kinetics, not the asserted source of anthropogenic ammonium loading.
  accessed_at: '2026-10-11T19:39:26.908978Z'
  support: supports
  locator: PMID15276744; DOI10.1016/j.watres.2004.04.047; title, full abstract and
    bibliographic metadata
  snapshot_sha256: 19231c11373e68bbc9d2c0aaf79534e2a1e51bd89bc279f30acdeb0d05cfa9ed
- evidence_id: PMID-19515200
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19515200+AND+SRC%3AMED&format=json&resultType=core
  summary: A one-year observational AOB/AOA study reports multivariate environmental
    correlations; it is not an ammonium-manipulation experiment.
  accessed_at: '2026-10-11T19:39:27.952524Z'
  support: supports
  locator: PMID19515200; DOI10.1111/j.1462-2920.2009.01958.x; title, full abstract
    and bibliographic metadata
  snapshot_sha256: f051de2246c4bd74338ebaf2499242233d0aa869ac585a7326ebbad3b24a44b0
- evidence_id: PMID-17391331
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17391331+AND+SRC%3AMED&format=json&resultType=core
  summary: FISH and microautoradiography compare denitrifier populations and electron
    acceptors across nutrient-removal and non-denitrifying plants, supporting bounded
    denitrifying ecophysiology.
  accessed_at: '2026-10-11T19:39:29.006223Z'
  support: supports
  locator: PMID17391331; DOI10.1111/j.1574-6941.2007.00309.x; title, full abstract
    and bibliographic metadata
  snapshot_sha256: 8e92f6a56fb9cdd3f1ee6edc68d365165632dfb9bd270ccd256527536bf05de8
- evidence_id: PMID-18811652
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18811652+AND+SRC%3AMED&format=json&resultType=core
  summary: Two-plant substrate-addition experiments measure nitrate/nitrite consumption
    and active probe-defined groups, not direct gaseous-nitrogen flux in the inspected
    abstract.
  accessed_at: '2026-10-11T19:39:30.041497Z'
  support: supports
  locator: PMID18811652; DOI10.1111/j.1574-6941.2008.00571.x; title, full abstract
    and bibliographic metadata
  snapshot_sha256: b8d50f4e6e3c16e8d552170cdcd50fd3a77a4e5e796e201075f9b38f795a3030
- evidence_id: MODIN-FULL
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4940897/fullTextXML
  summary: Inspected body paragraphs0,2,4,6,7,8,10,14,15,38,57,59,60,63 and80 support
    organic-matter/oxygen context and show alternative removal pathways. No one operating
    regime is generalized to all wastewater.
  accessed_at: '2026-10-11T19:48:19.522649Z'
  support: supports
  locator: PMID27453679; Introduction, Wastewater characteristics and identified operational
    paragraphs; other full-text passages not claimed inspected
  snapshot_sha256: 1236f91a826eb61f31117b87ea857c26caab7b4e9cffaba26928e1bef1ea610e
assessments:
- assessment_id: EDGE-waste_water_receives_anthropogenic_load
  area: evidence
  topic: 'Causal edge: waste_water_receives_anthropogenic_load'
  outcome: supported
  summary: The ENVO definition directly establishes human-affected water; PMID12180096
    supplies sewage-treatment context, not a measured loading experiment.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-12180096
  - ONT
- assessment_id: EDGE-anthropogenic_load_supplies_organic_matter
  area: evidence
  topic: 'Causal edge: anthropogenic_load_supplies_organic_matter'
  outcome: supported
  summary: PMID27453679 full text, introduction and wastewater-characterization sections,
    discusses incoming wastewater organic substrates; this applies to the organic-treatment
    graph, not every wastewater composition.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-27453679
  - MODIN-FULL
- assessment_id: EDGE-anthropogenic_load_supplies_ammonium
  area: evidence
  topic: 'Causal edge: anthropogenic_load_supplies_ammonium'
  outcome: concern
  summary: PMID15276744 tests DO-dependent AOB communities. Its abstract and the attached
    title fragment do not establish the asserted origin of ammonium. Full text was
    not retrieved; claim support needs a precise source passage or a better citation.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-15276744
- assessment_id: EDGE-organic_matter_creates_oxygen_demand
  area: evidence
  topic: 'Causal edge: organic_matter_creates_oxygen_demand'
  outcome: supported
  summary: PMID27453679 introduction and biodegradability paragraphs explicitly connect
    organic pollution, oxygen consumption and oxygen-depletion potential.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-27453679
  - MODIN-FULL
- assessment_id: EDGE-organic_matter_supports_heterotrophs
  area: evidence
  topic: 'Causal edge: organic_matter_supports_heterotrophs'
  outcome: unknown
  summary: PMID12180096 abstract addresses microbial functional guilds but does not
    state this exact substrate-to-heterotroph edge. The claim is biologically plausible;
    that is not a replacement for uninspected full-text support.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-12180096
- assessment_id: EDGE-heterotrophs_perform_organic_oxidation
  area: evidence
  topic: 'Causal edge: heterotrophs_perform_organic_oxidation'
  outcome: supported
  summary: PMID27453679 describes microbial oxidation of wastewater organics to carbon
    dioxide and water and coupled growth. Nonoxidative removal routes also exist and
    are not excluded by this bounded graph.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-27453679
  - MODIN-FULL
- assessment_id: EDGE-organic_oxidation_consumes_oxygen
  area: evidence
  topic: 'Causal edge: organic_oxidation_consumes_oxygen'
  outcome: supported
  summary: PMID27453679 introduction, oxygen-uptake characterization and aeration
    discussion support oxygen consumption during the specified aerobic oxidation process.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-27453679
  - MODIN-FULL
- assessment_id: EDGE-oxygen_demand_creates_anoxic_zones
  area: evidence
  topic: 'Causal edge: oxygen_demand_creates_anoxic_zones'
  outcome: unknown
  summary: The description qualifies this as a contribution rather than inevitable
    anoxia, but the PMID12180096 abstract/title snippet does not establish the local
    oxygen-demand-to-anoxic-zone claim.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-12180096
- assessment_id: EDGE-dissolved_oxygen_enables_nitrification
  area: evidence
  topic: 'Causal edge: dissolved_oxygen_enables_nitrification'
  outcome: supported
  summary: PMID15276744 directly varies DO and measures AOB enrichment/kinetics. Support
    is direct for the ammonia-oxidizing portion; the broader nitrite-oxidizer clause
    was not separately tested in the inspected abstract.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-15276744
- assessment_id: EDGE-ammonium_selects_ammonia_oxidizers
  area: evidence
  topic: 'Causal edge: ammonium_selects_ammonia_oxidizers'
  outcome: concern
  summary: PMID19515200 is a one-year observational community study, with reported
    correlations strongest for temperature, oxygen, influent nitrite and chromium.
    It does not demonstrate ammonium-driven selection in the inspected abstract; attached
    title text cannot supply that causal inference.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-19515200
- assessment_id: EDGE-ammonia_oxidizers_perform_nitrification
  area: evidence
  topic: 'Causal edge: ammonia_oxidizers_perform_nitrification'
  outcome: supported
  summary: PMID15276744 studies enrichment and growth kinetics of ammonia oxidizers;
    the description correctly specifies only the first nitrification step, not complete
    nitrification by AOB alone.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-15276744
- assessment_id: EDGE-nitrite_oxidizers_complete_nitrification
  area: evidence
  topic: 'Causal edge: nitrite_oxidizers_complete_nitrification'
  outcome: unknown
  summary: This conventional NOB role is plausible, but PMID12180096 abstract does
    not explicitly establish the conversion; full-text verification remains outstanding.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-12180096
- assessment_id: EDGE-nitrification_produces_nitrate
  area: evidence
  topic: 'Causal edge: nitrification_produces_nitrate'
  outcome: unknown
  summary: The graph correctly links the composite nitrification process, not AOB
    alone, to nitrate. The attached PMID12180096 title fragment and inspected abstract
    do not document the particular conversion.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-12180096
- assessment_id: EDGE-anoxic_zones_select_denitrifiers
  area: evidence
  topic: 'Causal edge: anoxic_zones_select_denitrifiers'
  outcome: supported
  summary: PMID17391331 compares17 nitrogen-removal plants with four lacking denitrification
    and tests nitrate/nitrite electron acceptors. This supports operating-context
    enrichment and functional capability, not obligate anaerobiosis or a universal
    abundance claim.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-17391331
- assessment_id: EDGE-denitrifiers_perform_denitrification
  area: evidence
  topic: 'Causal edge: denitrifiers_perform_denitrification'
  outcome: supported
  summary: PMID18811652 measures substrate-dependent nitrate/nitrite consumption and
    uses MAR-FISH to identify active groups in two plants. It supports denitrifying
    activity under the reported conditions.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-18811652
- assessment_id: EDGE-denitrification_removes_nitrogen
  area: evidence
  topic: 'Causal edge: denitrification_removes_nitrogen'
  outcome: unknown
  summary: PMID18811652 abstract reports nitrate/nitrite consumption, not direct gaseous-nitrogen
    measurements. A measured gaseous endpoint or a precise mechanistic source passage
    is needed for this wording; no contradiction of denitrification chemistry is claimed.
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - GRAPH
  - PMID-18811652
- assessment_id: IDENTITY
  area: identity
  topic: Habitat identity, definition and source boundary
  outcome: supported
  summary: 'ENVO:00002001 denotes anthropogenically affected water, with contaminated-water
    and waste-material genera, not the treatment facility. Four current contributors
    reproduce: GOLD1140 ORGANISM, PREGO623 TAXON, MADIN524 TAXON and the qualitative
    environment table. Only two have ITEM decisions, correctly leaving SEEDED status.
    The16-edge organic-nitrogen biotreatment overlay has a bounded treatment scope,
    but several attached citations do not establish the precise causal claim in the
    inspected text.'
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - R
  - RAW
  - ONT
  - PARENT
- assessment_id: HIERARCHY
  area: grounding
  topic: All direct and inherited genus contributions, synonym scopes and mapping
    endpoints
  outcome: concern
  summary: 'ENVO:00002001 denotes anthropogenically affected water, with contaminated-water
    and waste-material genera, not the treatment facility. Four current contributors
    reproduce: GOLD1140 ORGANISM, PREGO623 TAXON, MADIN524 TAXON and the qualitative
    environment table. Only two have ITEM decisions, correctly leaving SEEDED status.
    The16-edge organic-nitrogen biotreatment overlay has a bounded treatment scope,
    but several attached citations do not establish the precise causal claim in the
    inspected text. Independent ontology, GOLD, ambiguous-leaf and authored-definition
    contributions were considered separately.'
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - R
  - RAW
  - CODE
  - PARENT
  - ONT
- assessment_id: PROVENANCE
  area: provenance
  topic: Contributors, frozen counts and native status/history
  outcome: supported
  summary: 'Full-document reproduction preserves 4 source concepts and 2 ITEM-reviewed
    contributors. Actual attestations=[{"source": "ENVIRONMENTS_TABLE", "source_id":
    "wastewater", "source_label": "wastewater", "notes": "Physicochemical parameter
    bands from kg-microbe''s environment table."}, {"source": "GOLD", "source_id":
    "gold.ecosystem:2886", "source_label": "Wastewater", "source_path": "Engineered
    > Wastewater", "mapping_predicate": "skos:exactMatch", "assertion_count": 1140,
    "assertion_unit": "ORGANISM", "notes": "4 GOLD ecosystem node ids share this path;
    first shown. See data/raw/gold_ecosystem_paths.tsv."}, {"source": "MADIN", "source_id":
    "ENVO:00002001", "source_label": "waste water", "assertion_count": 524, "assertion_unit":
    "TAXON"}, {"source": "PREGO", "source_id": "ENVO:00002001", "source_label": "waste
    water", "assertion_count": 623, "assertion_unit": "TAXON", "score": 4.0, "evidence_channels":
    "annotated_genomes_isolates|environmental_samples"}]. Source counts/units are
    not summed; omitted zero counts are not biological absence. The generated native
    status/history is consistent with maintained inputs, not promoted by this scientific
    review.'
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - R
  - RAW
  - CODE
  - RULES
- assessment_id: TAXA
  area: evidence
  topic: Source association versus characteristic presence
  outcome: supported
  summary: 'All retained associations were read and reproduce: {"PREGO": 25, "MADIN":
    23}. All taxon IDs resolve. Source-specific ranks, candidate pools, counts, scores
    and corroborations retain their original meaning; none asserts is_characteristic.
    A source ranking is neither abundance nor a cross-source confidence probability.
    PREGO retains25 tied score4 entries from623; MADIN retains23 associations from524
    without invented score/rank. Five frozen labels differ from current NCBI naming,
    with the same IDs/strain designations; no taxonomy refresh was applied.'
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - R
  - RAW
  - TAX
  - RULES
- assessment_id: COMPLETENESS
  area: completeness
  topic: Environmental parameters, optional evidence and applicability
  outcome: supported
  summary: 'The five wastewater qualitative bands reproduce exactly: [{"parameter":
    "NUTRIENTS", "qualitative_value": "high", "source": "kg-microbe environments.csv
    (wastewater)"}, {"parameter": "PRESSURE", "qualitative_value": "low", "source":
    "kg-microbe environments.csv (wastewater)"}, {"parameter": "TEMPERATURE", "qualitative_value":
    "medium", "source": "kg-microbe environments.csv (wastewater)"}, {"parameter":
    "WATER_AVAILABILITY", "qualitative_value": "high", "source": "kg-microbe environments.csv
    (wastewater)"}, {"parameter": "WATER_VARIABILITY", "qualitative_value": "permanently
    wet", "source": "kg-microbe environments.csv (wastewater)"}]. They are coarse
    source annotations, not measured universal thresholds. The sole graph is assessed
    edge by edge above. No gene, regulator or expression-module claim calls for iModulonDB.
    Optional discussions, datasets and organism detail are not required merely to
    fill fields; parent/child evidence is not silently imported.'
  target_ids:
  - ENVO:00002001
  evidence_ids:
  - R
  - RAW
  - RULES
  - SEARCH
findings:
- finding_id: F1
  issue_key: envo-00002001-causal-citation-specificity
  category: scope
  severity: major
  status: open
  certainty: provisional
  title: Several causal edges lack verified claim-specific support in their attached
    evidence
  description: The16-edge pathway is plausible and several edges are supported. However,
    the ammonium-loading edge cites a DO/AOB study, the ammonium-selection edge cites
    an observational community study, and the gas-removal endpoint exceeds the inspected
    nitrate/nitrite-consumption abstract. Four additional Wagner/Loy edges remain
    unverified at the exact claim level. Attached title fragments do not supply those
    missing causal passages. This is a bounded evidence-placement gap, not proof that
    the biological mechanisms are false; full-text access limits are explicit.
  target_ids:
  - ENVO:00002001
  field_paths:
  - causal_graphs[0].edges
  evidence_ids:
  - GRAPH
  - PMID-12180096
  - PMID-15276744
  - PMID-19515200
  - PMID-18811652
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/waste_water.yaml
    role: Claim-level citations, passages and conditional edge wording
  rule_id: docs/CURATION.md; .claude/skills/curate-yaml-record/references/review-checklist.md
  native_severity: major
  normalization_reason: An asserted identity, strict relation, source-evidence scope
    or mapping endpoint is materially unsupported.
actions:
- action_id: A1
  description: For each concerned/unknown edge, inspect the actual full-text passage
    or add an appropriate primary/mechanistic citation. Distinguish observation, intervention,
    substrate capability and gaseous endpoint; keep conditional treatment scope. Preserve
    supported organic-oxidation edges and document every edge-level disposition.
  finding_ids:
  - F1
  target_ids:
  - ENVO:00002001
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/causal_graphs/waste_water.yaml
    role: Claim-level citations, passages and conditional edge wording
  generator: src/habitatmech/seed.py
  acceptance_checks:
  - Use maintained source/curation owners, exact source keys and inspected claim-level
    evidence. Do not hand-edit generated records or rewrite immutable reviews.
  - Preserve frozen source IDs, paths, count units, valid independent parents and
    native lifecycle rules; later exports do not replace original membership.
  - For an authorized fix, append required native history, add focused regressions,
    inspect a seed canary, regenerate affected products and pass schema, strict, labels,
    reproduction and full QC.
  - Save a linked successor observation for any disposition; report persistence alone
    does not resolve this finding.
limitations:
- Complete assessment means the full record and applicable claims were reviewed, not
  that every claim is supported or that original source membership was recovered.
- Only the first three exact current BioSample/Organism descriptions per sheet were
  individually interpreted; remaining rows and study joins are an inventory, not per-member
  scientific review.
- Current official ontology/GOLD downloads were hash-verified and retain actual retrieval
  times. No pinned ontology, taxonomy or inventory refresh was performed.
- Undefined source groupings and CLASS/SEEDED interpretations remain unpromoted. Positive
  apparatus/material boundaries do not settle every ancestor source interpretation.
- This is a same-agent review, not independent approval. Earlier ad hoc reports and
  issue discussions do not replace this exact captured-input assessment.
- SSSOM/KGX product conformance with current kg-microbe modeling was not audited.
  Shared endpoint1398 remains separate.
- Full-corpus review is incomplete. This individual report does not establish a category-wide
  or all-corpus pass.
- All six cited abstracts and bibliographic identities were inspected. Selected relevant
  full-text sections of PMID27453679 were inspected. Publisher full-text retrieval
  failed for12180096,15276744,19515200 and18811652;17391331 was assessed from its
  abstract only. No full-text absence claim is made.
- Concerned and unknown causal-edge support remains open; a valid graph schema and
  resolving PMID are not evidence of the precise causal claim.
notes:
- Only a new immutable review bundle is written. No habitat, curation, generated-site
  or scientific-status changes are made by this review.
- No prior structured review names this exact target as reviewed or affected; older
  issue links are related scope, not silent resolution of other records.
tags:
- habitatmech
- engineered
- record-review
- scientific-review
```
