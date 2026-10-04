# YAML Record Review: oceanic mesopelagic zone biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/oceanic_mesopelagic_zone_biome.yaml`
- Started UTC: 2026-10-04T21:22:14Z
- Finished UTC: 2026-10-04T21:25:32Z
- Verdict: pass

## Target

Entire generated HabitatRecord ENVO:01000036 oceanic mesopelagic zone biome,
AQUATIC/EXACT/SEEDED. It has an ENVO definition, one ontology parent, three
PREGO related synonyms, one 26-TAXON attestation, 25 retained associations
and one seed event. One retained taxon lacks a label. Parameters, xrefs,
evidence, graphs, discussions and datasets are absent.

`PATHS.tsv:764` pins the stem. Actual PREGO source minting gives
habitatmech:PREGO.cff0ebcd4d. The biome is not the separate marine
mesopelagic-zone record or GOLD Mesopelagic/Twilight zone source. Their
parent findings, study counts and decisions are not inherited here.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/oceanic_mesopelagic_zone_biome.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/oceanic_mesopelagic_zone_biome.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared batch PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records and 1,810 decisions. |
| `just qc` | Active at retired-URL gate. Tests: 457 passed, three skipped, two dependency warnings in 873.11 seconds. History, strict corpus, causal overlays, curation floor, exact reproduction and generated site passed. No terminal whole-run result claimed. |
| Source/reference checks | Full record, actual PREGO ingestion and complete taxon/attestation dictionaries, all 14 raw tables, current typed ENVO/OLS, all 25 current NCBI IDs, optional-field schema and label loader, whole page and actual semantic comparison. |

The batch's first QC invocation stopped before running on a uv cache
permission error; the authorized retry above is the live run. Faithful
projection does not independently verify ecology. No SSSOM/KGX compatibility
audit is claimed; terminal QC belongs in the later publication receipt.

## Identity and Grounding

Current [ENVO:01000036](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000036)
is active and matches physical ontology_terms.tsv line 7546. Its offshore
water-column biome has an approximate 200-1,000 m extent; the definition's
depth and organism-composition statements are ontology prose, not measured
properties of the 26 source taxa. The inspected
[NOAA layer account](https://www.noaa.gov/jetstream/ocean/layers-of-ocean)
uses the same mesopelagic depth interval, but that general agreement is
not independent evidence for the individual PREGO associations.

The sole named superclass ENVO:01000033 oceanic pelagic zone biome matches
physical subclass row 5676 and current typed OWL. The parent's current prose
contains the anomalous word epipelagic despite its generic label/hierarchy;
retain this as an upstream clarification question rather than silently
rewriting the parent or importing a whole-waterbody edge.

Actual ingestion is prego_self_grounded, one source concept and zero
reviewed sources. PREGO's own identifier is the record's ontology identifier.
EXACT without a mapping predicate, SEEDED and the single event are faithful.
This is not a #1398 endpoint-direction witness or an ITEM ecological review.

There are no current ENVO synonym assertions. The three PREGO variants,
including oceanic mesopelagic zonous, remain explicitly RELATED_SYNONYM.
Awkward source morphology is not a canonical label or an exact zone/biome
equivalence. No #1249 ontology-scope inflation is demonstrated here.

## Evidence

`prego_habitats.tsv:277` supplies 26 distinct taxa, 26 direct assertions,
maximum score four and environmental_samples only. The generated TAXON
count is not a count of samples, isolates or studies.

Every retained raw row at `prego_habitat_taxa.tsv:7459-7483` was inspected;
all 25 generated dictionaries match actual ingestion. Each has score four,
direct TRUE, environmental_samples only and no cross-source corroboration.
All are unmarked for is_characteristic. Score/direct/taxon-ID ordering
explains the tied ranks. One of 26 candidates is outside the retained list;
that omission is not biological absence or proof the displayed 25 are
representative of mesopelagic communities.

[Current NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=134561,1394,266940,28122,34085,36987,379066,411477,411485,428125,435805,445336,457427,498761,537937,562,56780,57043,583355,585501,595452,595453,641112,655815,70993&retmode=xml)
resolved all 25 IDs directly with no alias redirects. All 24 supplied names
match current names. Fourteen entries are strain-ranked; the remainder are
species-ranked, including unresolved sp. labels whose specificity must not
be invented.

The unlabelled NCBITaxon:36987 at raw row 7464 is Coptotermes formosanus,
with an inspected Metazoa/Insecta lineage. It is neither a retired ID nor an
unidentified microbial species. The blank raw label is faithfully omitted by
seed.py:1093-1095; `_load_taxon_labels` in extract.py only supplies names
present in the upstream taxonomy table. The schema at lines 389-447 makes
labels optional and records observational taxa, not an exclusively microbial
filter. A guessed microbial replacement or silent deletion would be unsupported.

Its ecological basis remains unverified. Source score/direct flags do not
prove that this insect inhabits the mesopelagic biome. This report neither
endorses that interpretation nor declares the source assertion false without
the original sample context. The same caution applies to the other names:
taxonomy identity is not ecological evidence. The full page displays a CURIE
fallback for 36987 and labels the whole list source-associated, not characteristic.

The all-14-table exact-ID/key scan found ontology/PREGO inputs and one GOLD
broad-scale context mention: gold_path_triads.tsv:581, Marine > Mesopelagic,
104 samples/eight studies with share 1.00. That belongs to a separate GOLD
source. It does not supply a GOLD attestation or independently corroborate
these 26 PREGO taxa. No BacDive, MADIN or parameter contribution feeds this target.

The batch's fresh ignored-inclusive search found no original PREGO files in
the configured kg-microbe checkout. Its network-authorized portal request
failed verified TLS because the certificate had expired, without bypass.
Thus original sample-level ecology and the 26th association are not recovered.

## Completeness

Ignored-inclusive ontology-ID, minted-key, label/stem and filename searches
covered curation, history, research, reports, conf, PATHS and RETIRED. They
found the path lock and contextual neighboring reviews, but no target-owned
decision, definition, overlay, session history, retirement or prior individual
review. Broader searches for 36987/Coptotermes found other source occurrences
and prior caveated reviews, not original evidence for this association.

No novel term or required missing field is established. Keep optional
parameters, mechanisms and expression fields empty without exact evidence.
iModulonDB is inapplicable without gene/regulator/expression assertions;
an unrelated module cannot validate an environmental association.

## Findings

None verified for the current identity and explicitly source-attributed
projection: zero blockers, zero major, zero minor. This is a bounded pass,
not ecological certification of Coptotermes formosanus or the other taxa.
The optional blank name is not alone a schema or provenance defect.

## Recommended Edits

No immediate record correction is justified by the inspected evidence.
Prioritize recovering original PREGO evidence for 36987 before stronger
ecological use. Any supported name enrichment belongs in governed upstream
taxonomy/extraction inputs; any association correction needs an auditable
source policy. Never patch the generated YAML or filter unusual organisms
solely from plausibility.

## Follow-up Checks

A future source refresh must preserve or deliberately reconcile the
count/pool, taxon IDs, channel, score/rank semantics and observational state.
Dry seed, inspect the ENVO:01000036 canary, then validate provenance, ordinary/
strict/product checks, new history, exact reproduction, site and full QC.

Actual in-memory enrichment of the missing name changes full semantic text;
that future change would need genuine map/site refresh under #1217. No such
edit was made here. Preserve protected #1218/runtime pins and inspect actual
SSSOM/KGX products before claiming downstream compatibility.

## Additional Notes

All-state target-ID/key, 36987 and Coptotermes searches found no dedicated
new issue. The full #1285 body concerns the distinct marine mesopelagic-zone
record's GOLD parent, not this PREGO biome. The prior marine-bathyal review
was read for context, while all current taxon identities were independently
rechecked here. No new deletion/alias issue is invented for a valid ID.

Official ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated artifact, old report/history, paid research
or GitHub item was changed by this individual review.
