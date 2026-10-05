# YAML Record Review: Runoff channel

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/runoff_channel.yaml`
- Started UTC: 2026-10-05T02:26:49Z
- Finished UTC: 2026-10-05T02:29:34Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.09350714a0, Runoff channel,
AQUATIC/UNGROUNDED/SEEDED: one parent, one GOLD attestation without count,
unit or mapping predicate, and two history events. Definition, synonyms,
xrefs, parameters, taxa, record-level evidence, graphs, discussions and
datasets are absent. PATHS.tsv:1339 pins runoff_channel.yaml.

Exact source: Environmental > Aquatic > Thermal springs > Runoff channel.
The attestation displays node 6350 and explicitly says that two GOLD node IDs
share this path. This review concerns the discharge channel, not runoff water,
its sediment, adjacent soil, microbial mats or the spring supplying the water.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/runoff_channel.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/runoff_channel.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared fresh PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | At review finish, authorized run active at retired-URL gate. Tests passed (457 passed, three skipped, two warnings); history, strict corpus, 32 overlays, curation floor, exact reproduction and generated site passed. No terminal whole-run result yet. Initial cache-access attempt terminated before gates. |
| Source/reference checks | Whole target and contextual hot-spring parent, executed source/parent routes, complete-document equality, all 14 raw inventories, typed ENVO/current OLS, GOLD/study attempts and full rendered page. |

The complete generated dictionary reproduces with one source concept and zero
ITEM-reviewed sources. History validation covered 90 files. Exact reproduction
covered 3,206 records with zero missing, extra or different records; generated
site covered 3,206 pages, 231 redirects, eight categories and 123 term requests.
Prior PR #1435 main-push QC 37254250614 is separately terminal SUCCESS, not a
substitute for this fresh run. These are review-time observations.

## Identity and Grounding

Actual source resolution is gold_unmatched, retained by CLASS-level
CONFIRM_UNGROUNDED at decisions.tsv:146. The 2026-08-12 event explicitly says
habitat identity was not assessed; the 2026-08-16 event records seeding.
UNGROUNDED/SEEDED is honest. No emitted predicate creates a #1398 endpoint
finding here.

The sole parent is current active
[ENVO:00000051 hot spring](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000051),
a spring carrying geothermally heated groundwater. Its named parent,
[ENVO:00000027 spring](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000027),
is a surface landform providing an outlet for groundwater or steam. A
downstream discharge channel is not thereby that groundwater outlet itself.

The source parent key habitatmech:GOLD.f0e9ce4655, Thermal springs, actually
resolves through ITEM GROUND at decisions.tsv:1333 to ENVO:00000051 with an
exact mapping. seed.py:898-907 promotes the immediate GOLD path parent into
the child's strict parent_habitats. That route explains the assertion but
does not establish a channel as a kind of spring. The full 623-line hot-spring
record was read as context only. Its four source attestations, taxa, nine
parameters, causal graph and REVIEWED status do not transfer to this child.

Existing active terms require a bounded structural assessment:
[ENVO:00000395 channel of a watercourse](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000395)
describes a depressed landform, with bed and banks, that confines a river,
slough or ocean strait; its definition is not simply every feature called a
channel. [ENVO:01000650 stream channel](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000650)
adds a stream constraint. Conversely,
[ENVO:00000029 watercourse](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000029)
denotes flowing water, not the confining structure. Typed official OWL and
current OLS were checked for all five terms. No exact identity or replacement
genus is asserted solely from lexical similarity. Uncertainty about the best
genus is not counted as another confirmed defect.

## Evidence

Physical gold_ecosystem_paths.tsv:1584 gives depth four, nodes 6350 and 6351,
and zero organism, study and biosample counters. Count/unit omission is
faithful, not evidence of biological sterility. Separate
gold_path_biosamples.tsv:400 records 36 biosamples using node 6351. This is
consistent with the two-node collapse note, not a source-ID mismatch and not
36 organism assertions.

The exact-path study row gold_studies.tsv:3999 is Gs0154480. It also names
adjacent soil beneath this channel, terrestrial endolithic habitat and
host-associated red algae. Its original GOLD page returned 403. Without an
inspected sample-level crosswalk, study-wide measurements or organisms cannot
be assigned to this channel. Raw child rows 1585-1587 separately denote
Adjacent soil, Microbial mats and Sediment; none establishes the parent
channel's own measured properties.

Current official GOLD OLS lookups for 6350 and 6351 both returned 404. This
does not establish retirement. All 14 raw inventories were searched for the
exact source path/node: no target complete-triad row, named taxon,
environmental parameter, BacDive, PREGO or Madin contribution was found.
The complete-triad aggregation's absence does not exclude partial sample
annotations. No inferred temperature, water chemistry, artificial-channel
construction or microbial mechanism should be filled from the source label.
iModulonDB is inapplicable without gene, regulator or expression assertions.

The complete rendered page correctly exposes the class-level warning, source
path, two-node note and missing count. It also presents hot spring as a broader
habitat, making the unsupported strict-parent assertion user-visible.

## Completeness

Ignored-inclusive searches covered the identifier, both nodes, full path,
label variants and filename across curation, conf, history, research, reports,
all raw inventories, PATHS, RETIRED and additional repository text, including
ignored build output. The CLASS decision and source rows were found. Prior
adjacent-soil and microbial-mat reports mention this channel as context; those
are not prior individual reviews of this target.

No target authored definition, xref row, causal overlay, dedicated research,
session-history file, retirement or prior individual report was located.
An ITEM identity assessment would resolve which channel structure and genus
the source supports. Missing optional data is not independently a finding
without target evidence; keep distinct child habitats distinct.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The thermal-spring runoff channel inherits hot spring as its sole strict superclass; the source establishes a supplying context, not that the channel is itself a groundwater outlet. | Exact-source parent controls and src/habitatmech/seed.py:898-907; ITEM assessment keyed by habitatmech:GOLD.09350714a0 at curation/decisions.tsv:146. |

Zero blockers, one major finding, zero minor. The optimal structural genus is
unresolved, not a separate confirmed missing-genus finding.

## Recommended Edits

1. Suppress this source-parent contribution without changing genuine spring
   identities globally. Preserve the minted source identity, qualified source
   path, two-node note, count omission and append-only history.
2. ITEM-assess the channel's structure and sampling scope in
   `curation/decisions.tsv`. Inspect candidate definitions before adopting an
   existing true genus. Do not equate channel structure with its water,
   sediment, mat or adjacent soil, and do not invent a duplicate generic term.
3. If an authored source-specific definition is justified, own it in
   `curation/term_requests.tsv` and keep its grounding compatible. REPLACE may
   be justified only after confirming that this sole inherited parent is
   unsupported and supplying the appropriate genus; it is not blanket
   permission to discard independently valid parents elsewhere.

## Follow-up Checks

Dry seed and inspect `just seed-canary habitatmech:GOLD.09350714a0 --force`.
Use regressions for this exact edge, genuine spring controls, the chosen
structural genus, two-node provenance, count omission and ITEM-derived status
and history. Append session history and use guarded regeneration, then
ordinary/strict/products, provenance/history, exact reproduction, site and
full QC.

Actual full-context parent removal changes semantic text; predicate-only
omission is a no-op because no predicate is emitted. A parent/genus correction
requires a genuine #1217 map/site refresh while preserving protected
#1218/runtime pins. Actual SSSOM/KGX exports were not executed or certified
compatible by this review.

## Additional Notes

All-state exact-ID and runoff-channel searches found #1397 and #1398, but no
matching repair of this channel-to-hot-spring assertion. The inspected #1397
comment, issuecomment-5982442429, covers the separate microbial-mat child
habitatmech:GOLD.bef53c8bcc inheriting this channel. Repairing that child's edge
does not repair this channel's own parent. #1398 concerns a predicate contract
not emitted here. Coordinate shared mechanisms without closing unrelated
scientific findings.

Typed official ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated artifact, old report/history, paid research or
GitHub item changed during this individual review.
