# YAML Record Review: meromictic lake

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/meromictic_lake.yaml`
- Started UTC: 2026-10-04T14:14:08Z
- Finished UTC: 2026-10-04T14:21:43Z
- Verdict: needs curation

## Target

Complete generated `HabitatRecord`: ENVO:00000199, meromictic lake, AQUATIC,
EXACT and REVIEWED. It contains an ENVO definition, one RELATED PREGO synonym,
two parents, GOLD and PREGO attestations, one associated taxon and three
history events. Parameters, citations, graphs, datasets, discussions, xrefs
and replacement links are not emitted.

Source mints are `habitatmech:GOLD.4f1a9febbf` and
`habitatmech:PREGO.e0a4978251`; PATHS.tsv:517 pins meromictic_lake. The GOLD
source is `Environmental > Aquatic > Freshwater > Meromictic lake`, with
gold.ecosystem:8537 displayed and node 8538 sharing the same collapsed path.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/meromictic_lake.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/meromictic_lake.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared unchanged-corpus run PASS: 1,179 canonical pairs, one synonym, five exceptions, 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared run PASS, 953 ungrounded records and 1,810 decisions. |
| `just qc` | Shared run finished: all quality gates passed. Tests: 457 passed, three skipped, two warnings in 649.28 seconds. Includes history, all 3,206 strict-schema records, 32 overlays, curation floor, corpus reproduction, generated site and redirect checks. |
| Source/reference checks | Entire target, relevant decisions, structured rows across 14 raw TSVs, official ENVO OWL/OLS, current NCBI taxonomy, and DSMZ/JGI strain pages inspected. |

The QC session had closed when polled after context recovery; its final log
explicitly reports all gates passed. It was not restarted or represented as
a new focused validator. Full-corpus-only checks remain full-corpus checks.

## Identity and Grounding

Current [official ENVO OWL](https://purl.obolibrary.org/obo/envo.owl) has the
record's definition under IAO:0000115 and lake (ENVO:00000020) as its sole
direct named subclass parent. The OLS term response exposed explanatory
commentary in its description field instead of this concise definition;
the typed OWL predicates resolve that presentation discrepancy. The
commentary's generalization about organisms in bottom sediments is not
adopted as a scientific claim of this record.

Current [ENVO:00002011](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002011)
denotes fresh water, a liquid-water material. A lake as a whole is not a
subclass of its liquid contents. The extra fresh-water parent comes from
the GOLD path, not ENVO's lake hierarchy. Retain the supported lake parent.

`curation/decisions.tsv:506` and `:1511` contain ITEM-level REVIEW decisions
for the two source mints, dated 2026-08-13. The generated REVIEWED status
and two corresponding review events therefore follow the maintained inputs.
The broad multisource-review rationale did not prevent the false parent;
that is a curation defect, not evidence of a fabricated status or reason to
erase either existing audit event. The seed event is dated 2026-08-16.

The source names agree with the lake identity. The plural PREGO synonym is
conservatively RELATED, and AQUATIC is appropriate. No separate identity
change is justified by the demonstrated parent error.

## Evidence

Physical CSV line locators below account for multiline cells.
`data/raw/gold_ecosystem_paths.tsv:1479` contains the exact depth-four path,
nodes 8537|8538, and zero organism/study/biosample counts. The absence of an
emitted GOLD assertion count is consistent with this snapshot. Child rows
1480-1483 describe chemocline, microbial mats, mixolimnion and monimolimnion;
they are not extra attestations or defining parts supplied by this target.
The full structured raw scan found no exact-target bulk biosample, study,
triad or parameter row. OLS GOLD lookups for both current path IRIs returned
404; these bounded retrieval failures do not prove retirement or invalidity
of the committed source nodes.

`prego_habitats.tsv:673` records one taxon, one direct assertion and maximum
score 3 in annotated_genomes_isolates, with the canonical label and plural.
`prego_habitat_taxa.tsv:4208` agrees with the emitted taxon, label, score,
and rank 1. Candidate pool 1 is separately derived from taxon_count in
`prego_habitats.tsv:673` by `seed.py:1101`; the pair table has no pool field.
Score is a PREGO evidence-channel score, not
abundance, prevalence or an experimentally measured lake preference.

Current [NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=319225)
and the inspected EFetch response retain NCBITaxon:319225 as Pelodictyon
luteolum DSM 273, with Chlorobium luteolum DSM 273 as an alternative name.
The [DSMZ DSM 273 catalogue](https://www.dsmz.de/collection/catalogue/details/culture/DSM-273)
identifies a meromictic-lake isolate from Norway under the Chlorobium name.
The [JGI DSM 273 genome project](https://genome.jgi.doe.gov/portal/pellu/pellu.home.html)
explicitly bridges the names and identifies Lake Polden, Norway, as its
meromictic-lake isolation site. These primary resources independently support
the exact strain's association; the alternative name does not make the
record's current NCBI label wrong.

The original PREGO pair-level provenance was not recovered. Independent
strain evidence does not recover that original link, establish characteristic
presence in every meromictic lake, or authorize importing the strain's
genomic traits and culture requirements into universal habitat parameters.
No is_characteristic assertion or unsupported mechanism is emitted.

`ontology_terms.tsv:6789` preserves the same lake definition;
`ontology_subclass_edges.tsv:4832` supplies only ENVO:00000020. The second
parent is introduced by the GOLD second pass at `src/habitatmech/seed.py:898-907`.

## Completeness

Ignored-inclusive ID, source-key, label and filename searches covered
curation, history, research, individual reports, PATHS and RETIRED. They
found the two decisions, path lock and contextual mentions in earlier
chemocline/aquatic-biome reports, but no target authored definition, causal
overlay, dedicated research, separate session-history entry, retirement
entry or earlier individual review of this lake. The chemocline report's
different child-to-whole error is not counted against this record.

Empty optional scientific fields are not defects without target-specific
support. No gene, regulator, pathway or transcriptomics dataset is asserted;
iModulonDB is not applicable. External strain support found during this
review does not retroactively supply a frozen-pipeline corroborated_by value.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The whole meromictic lake has liquid fresh water as a superclass. GOLD contextual placement has been promoted into a false whole-to-material is-a relation. | Source-parent pass at `src/habitatmech/seed.py:898-907`, or a governed exclusion keyed to GOLD.4f1a9febbf and expected parent ENVO:00002011. |

Counts: zero blockers, one major, zero minor. The definition, supported lake
parent, provenance, taxon identity/association and derived review status
remain supported within the evidence scopes above.

## Recommended Edits

1. Exclude only the exact GOLD fresh-water parent contribution. Preserve the
   ENVO lake parent, both source concepts, node-collapse note, PREGO score,
   count/unit, taxon and all existing review provenance.
2. Record a new audited correction through maintained inputs and the guarded
   generator. Do not manually downgrade REVIEWED, rewrite old events, or
   rename the NCBI taxon solely to match another database's preferred name.
3. Add a regression for the exact target/source pair and independent-parent
   preservation, then regenerate the corpus and dependent products.

## Follow-up Checks

Require source-key/expected-parent checks, ordinary and strict schema,
identifier-label correspondence, history/provenance, corpus reproduction,
generated-site validation and full QC. Inspect the complete output, not
only a matching parent-list assertion.

The rendered page currently presents both lake and fresh water as Broader
habitats. An actual full-context semantic-adapter comparison removing only
ENVO:00002011 drops `broader habitat: fresh water`. A scientific correction
therefore needs the governed map/site rebuild tracked in #1217. Preserve
runtime pins and unrelated protected draft #1218.

## Additional Notes

GitHub searches for the exact source key and meromictic label returned no
existing target-specific issue. A broader search found open #1220; its full
body and comments were inspected. It covers the same GOLD whole/material
parent mechanism for other freshwater records. Add this target as a new,
separately identified witness, not as one of its three already implemented
draft-PR exclusions. Its scientific acceptance remains unresolved.

Official ENVO OWL bytes inspected have SHA-256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No paid research, scientific edit, status promotion, curation event or
committed-history rewrite was performed.
