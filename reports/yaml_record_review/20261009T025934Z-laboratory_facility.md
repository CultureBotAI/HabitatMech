# YAML Record Review: laboratory facility

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/laboratory_facility.yaml`
- Started UTC: 2026-10-09T02:56:55Z
- Finished UTC: 2026-10-09T02:59:34Z
- Verdict: pass (0 blocker, 0 major, 0 minor)

## Target

Read the complete generated HabitatRecord ENVO:01001406 at baseline
`893f468d11748cef519a6f1191f294af37559d04`: ENGINEERED / CLOSE / REVIEWED.
It contains an ENVO definition, two differently scoped synonyms, one parent,
one BacDive attestation, 363 STRAIN assertions, 25 retained taxa from a
310-taxon candidate pool, and three events. The complete Research facility
parent was read as context, not counted as another completed review. This
facility is not automatically a culture medium, laboratory-developed
organism, synthesis process or the whole meaning of the neighboring GOLD
Lab synthesis source.

## Validation

- Fresh `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/laboratory_facility.yaml`:
  no issues.
- Fresh strict validation with the same cache setting: one file, zero errors.
- Full-index `build_corpus()` / `build_document()` reproduced all fields:
  one source, one ITEM-reviewed source, no authored definition or parent
  exclusion. All 25 retained taxon IDs, labels, counts, ranks and pools
  were separately compared with their raw input rows.
- Fresh shared session gates passed: exact reproduction of 3,208 records,
  208 valid histories, and current provenance for 14 inventories/two GOLD
  sources.
- Full QC was not repeated per read-only record. Local and
  [exact-baseline queue QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37874456969)
  passed all gates with 622 tests and three skips; baseline
  [label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37874456975)
  and vendored sync passed too. These checks do not independently reconstruct
  the original strain cohort. No SSSOM/KGX audit was performed.

## Identity and Grounding

`PATHS.tsv:892` agrees with the canonical ID/stem. Recomputed source mint
`habitatmech:BACDIVE.3582899e36` uses the full BacDive source ID. Complete
mapping indexes give `bacdive_mapping_table`, ENVO:01001406, CLOSE and
skos:closeMatch. The ITEM REVIEW row at `curation/decisions.tsv:1746`
produces `curated_review_of_bacdive_mapping_table`, reviewed=True. It
endorses the close correspondence without asserting exact source equivalence;
REVIEWED and all three generated events agree with the maintained inputs.

Primary ENVO:01001406 defines a research facility with manufactured systems
controlling internal conditions and supporting research/measurement. Its
label, definition, ENVO:00000469 research-facility superclass and explicit
`hasExactSynonym` research laboratory match the record and
`ontology_terms.tsv:8899`. The primary class also has a has-part restriction
to laboratory environment, not an is-a assertion equating facility and
environment. The generated parent correctly retains only the named genus.

BacDive Laboratory is RELATED_SYNONYM, consistent with its CLOSE mapping.
The distinct primary ENVO research laboratory synonym is genuinely exact;
it must not be downgraded merely because the source mapping is close. The
SOURCE_SYNONYM_SCOPED event accurately records the implemented #1459 behavior.
The BROAD-source fallback finding in the preceding laboratory-environment
review is not reproduced in this CLOSE source route.

## Evidence

- `bacdive_isolation_sources.tsv:41` supplies source ID
  `bacdive.isolation_source:laboratory`, label Laboratory, 363 strains and
  310 taxa. This is an aggregate source key, not an individual strain
  accession. `isolation_source_groundings.tsv:173` supplies the closeMatch
  to laboratory facility, medium confidence, LexicalMatching provenance
  and 2026-05-01 verification date. The later ITEM review is separate from
  that automatic upstream mapping; neither warrants an EXACT upgrade.
- `bacdive_source_taxa.tsv:1599-1623` contains the 25 retained rows. Every
  label, distinct-strain association count and rank matches; every emitted
  candidate_pool is 310. There are no corroboration strings, characteristic
  flags or abundance scores on these entries. Their counts sum to 67,
  not 363: the retained list is not the complete strain or taxon roster.
  The complete 310-taxon pool and original 363 strain records were not
  independently reconstructed in this review.
- A fresh [NCBI Taxonomy efetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=83428,144185,153233,286730,1211807,1270,1280,1506,28214,294,562,67263,1393,1402,1465,1486246,1747,1869227,1906,2024826,2041036,2094151,2426,28095,293&retmode=xml)
  returned all 25 requested IDs directly with exactly matching scientific
  names. No missing/merged identifier or name mismatch was observed.
  Response: 148,772 bytes, SHA256
  `63510d14ffffd45dad174b7340d903e22ba6b77d79461e38c3edc0c58d5fb24c`.
  This verifies names, not biological occurrence in every laboratory.

| Rank | NCBITaxon ID | Retained strain count |
|---|---|---|
| 1 | 83428 | 5 |
| 2 | 144185 | 4 |
| 3 | 153233 | 4 |
| 4 | 286730 | 4 |
| 5 | 1211807 | 3 |
| 6 | 1270 | 3 |
| 7 | 1280 | 3 |
| 8 | 1506 | 3 |
| 9 | 28214 | 3 |
| 10 | 294 | 3 |
| 11 | 562 | 3 |
| 12 | 67263 | 3 |
| 13 | 1393 | 2 |
| 14 | 1402 | 2 |
| 15 | 1465 | 2 |
| 16 | 1486246 | 2 |
| 17 | 1747 | 2 |
| 18 | 1869227 | 2 |
| 19 | 1906 | 2 |
| 20 | 2024826 | 2 |
| 21 | 2041036 | 2 |
| 22 | 2094151 | 2 |
| 23 | 2426 | 2 |
| 24 | 28095 | 2 |
| 25 | 293 | 2 |

- Exact-field/pipe-member scanning of all 14 inventories found no direct
  target GOLD path/biosample/study, PREGO/Madin or environmental-parameter
  contribution. The CURIE appears in two other paths' triads: Reagent blank
  broad scale at `gold_path_triads.tsv:107`, and Multiple myeloma local
  scale at line 1470, each one sample/study. Those uses are contextual,
  not co-attestations or target samples, and are not endorsed as correct
  triad-slot assignments by this review.
- Complete target and parent class elements were parsed from
  [pinned primary ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl).
  The session-verified OWL SHA256 is
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  The Research facility parent's 339-TAXON PREGO aggregate, scores and
  25 displayed associations do not transfer; that contextual file read
  does not independently validate its taxa or complete its review.

## Completeness

Xrefs, environmental parameters, claim evidence objects, graphs, discussions
and datasets are empty. No universal community, laboratory surface, medium,
physiological mechanism or particular experimental practice is implied by
the observational associations. iModulonDB is not applicable: the listed
taxa are not gene/regulator/transcriptomic claims.

Ignored-inclusive ontology/source IDs, label/stem and source-key searches
covered curation, history, research, configuration, raw inventories,
PATHS/RETIRED and individual reports. They found the ITEM row and contextual
mentions, but no target-owned authored definition, parent exclusion, causal
overlay, dedicated dossier, target-specific session history or earlier
individual target report within those bounds. The shared synonym fix is
represented by its generated audit event; absence of a target-specific
history file does not mean that shared fix had no session history.

## Findings

None found: zero blockers, zero major and zero minor findings in the
assertions present. The broad facility-level source label is not a defect
merely because original strain collection surfaces are not reconstructed.
CLOSE remains appropriately qualified, and no exactness or characteristic-
presence promotion is recommended.

## Recommended Edits

None required by this review. Preserve the true research-facility genus,
primary exact synonym, weaker BacDive synonym, genuine ITEM-derived status,
363 STRAIN aggregate, 310-taxon pool and 25 observational associations.
If future strain-level evidence distinguishes collection environment from
laboratory handling, curate only the supported source scope through its
maintained mapping/decision input; do not infer it from taxon names alone.

## Follow-up Checks

Future authorized source refreshes should validate all retained taxon
identifiers/names, ranks and counts against the governed original join and
audit the full pool before changing its aggregate. Run provenance, strict,
history, labels, full-index reproduction, site and full QC for any change.
Regression controls should keep CLOSE source aliases distinct from genuine
ontology exact synonyms. Compare semantic inputs before any required real
map rebuild; do not merge the neighboring source concepts by label.

## Additional Notes

Only this report was written. Scientific inputs, generated products, status,
history and GitHub state are unchanged. Technical baseline reuse and live
NCBI name agreement do not independently certify all original BacDive
strain records or make the displayed taxa characteristic of laboratories.
