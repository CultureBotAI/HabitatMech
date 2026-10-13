# YAML Record Review: Transient pool

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/transient_pool.yaml`
- Started UTC: 2026-10-06T18:10:51Z
- Finished UTC: 2026-10-06T18:12:59Z
- Verdict: needs curation

## Target

Complete-file review of the generated `HabitatRecord`
`habitatmech:GOLD.d39a2ed099`, label Transient pool, category AQUATIC,
UNGROUNDED/SEEDED, at baseline `7507858f867f57eb3a552f032dc84a16ed2a21f2`.
It has one parent, one GOLD attestation, and two generated history events.
No definition, synonyms, taxa, parameters, literature evidence or mechanism
graph is asserted. The target is the freshwater GOLD path, not a generic
temporary pool, a vernal-pool sibling, or its Microbial mat child.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/aquatic/transient_pool.yaml`:
  pass, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/aquatic/transient_pool.yaml`:
  one file, zero errors; only the validator's ignored diagnostic TSV refreshed.
- Actual `seed.build_corpus()` / `seed.build_document()` and entire parsed-YAML
  comparison: pass; one source concept, zero ITEM-reviewed sources, zero taxa,
  two history events.
- This review shares the same unchanged inputs as the immediately preceding
  tidal-mudflat review. In this session, `just verify-corpus` found all 3,206
  records with zero missing/extra/differing files; `just validate-history`
  validated all 104 histories; `just term-requests-check` found 109 terms current.
  No scientific input, source, record, history or generated page changed between
  those checks and this review.
- [Full QC 37507480894](https://github.com/CultureBotAI/HabitatMech/actions/runs/37507480894)
  and [label gate 37507480900](https://github.com/CultureBotAI/HabitatMech/actions/runs/37507480900)
  succeeded on the exact baseline. Full QC/OAK, provenance, causal and site
  gates were not separately rerun for this individual report.
- Official current ENVO RDF/XML was parsed for all six parent/candidate terms
  discussed below; all resolve to nondeprecated classes. There are no taxon,
  DOI, PMID, gene or causal-edge identifiers in the target to validate.
- Rendered page text was inspected. It correctly distinguishes the CLASS
  sweep from individual judgment and displays no numerical source assertion.
  It also exposes the erroneous parent. No browser visual QA is claimed.

## Identity and Grounding

`seed.mint("GOLD", "Environmental > Aquatic > Freshwater > Transient pool")`
reproduces the identifier; `data/habitats/PATHS.tsv:2852` pins its stem.
The source path and AQUATIC placement describe a freshwater pool environment,
not a quality, process, taxon or sample identifier.

The actual default route is `gold_unmatched`, retaining the minted identity.
The maintained CLASS-level CONFIRM_UNGROUNDED row at
`curation/decisions.tsv:1168` yields
`curated_confirm_ungrounded_from_gold_unmatched`, still UNGROUNDED with
`reviewed=False`. Thus SEEDED is correct. This automated non-match is not an
item-level judgment that no appropriate ontology concept can ever be found.
The attestation has no mapping predicate because the retained source concept
is the record itself; no endpoint mismatch is demonstrated for this target.

The immediate GOLD Freshwater parent resolves through `gold_leaf_synonym` to
`ENVO:00002011`, CLOSE, endorsed by an ITEM REVIEW of
`habitatmech:GOLD.ad12f0169a`. The second GOLD parent-path pass in
`src/habitatmech/seed.py:907-934` then adds that resolved identifier as the
Transient pool superclass. This is the source of the finding, not an ontology
subclass assertion or an authored definition.

[ENVO at a2455d1a77e46bb8a664d65a157166b539269042](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
distinguishes the relevant alternatives:

| Term | Inspected meaning and limitation |
| --- | --- |
| ENVO:00002011, fresh water | Low-solute water material; not the pool/basin that contains it |
| ENVO:00000063, water body | Accumulation of water; candidate broader class if the source denotes the water body |
| ENVO:00000033, pond | Small water body; does not encode transient duration |
| ENVO:00000504, container of an intermittent pond | A basin/container, with illumination/mixing/size conditions; not automatically exact identity for an unspecified transient pool |
| ENVO:00000549, container of an intermittent water body | Periodically water-filled depression; container scope must be established |
| ENVO:01000871, puddle of water | Small surface accumulation; source size and formation constraints are not supplied |

The broad candidate search included pool, temporary, ephemeral and transient
terms in the complete committed ontology table. Nearby terms are leads, not
grounds for silently equating the source with a container, puddle, tidal pool,
or season-specific vernal pool.

## Evidence

All 14 raw TSV inventories were scanned using structured field/pipe-list
membership for the exact path, minted ID, both GOLD IDs and source label.
`data/raw/gold_ecosystem_paths.tsv:1498` has the exact four-level path,
depth 4, nodes `gold.ecosystem:8268|gold.ecosystem:8269`, and zero organism,
study, biosample and total assertion counts. The YAML faithfully shows the
first node and a two-node collapse note. No count/unit is emitted because
`ingest_gold` emits those slots only for positive organism counts; the omitted
count is not missing evidence of a known positive population.

The [current GOLD ecosystem workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
verifies the path at row 656, node 8269, with the fifth level Unclassified;
the adjacent row 655 is node 8270, the Microbial mat child. Downloaded bytes
had SHA-256 `01c8c8500c86297101fbe3ecc42ff63c058096977cba5238524b8a83770ec2e0`.
All rows were iterated after resetting incorrect A1:A1 worksheet dimensions.
The public terminal-path workbook does not independently verify historical
internal node 8268; that node is verified against the committed inventory,
not claimed as a separately fetched current node record. The child is a
distinct canonical path, not another assertion for its parent.

[EPA's seasonal-pool manual, EPA/903/B-05/001](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1002R0O.TXT)
describes ephemeral pools as temporary water bodies and distinguishes their
hydroperiod from annually drying pools. This supports the water-body/material
distinction, not a numerical duration threshold for every GOLD Transient pool.
[EPA's vernal-pool account](https://www.epa.gov/wetlands/vernal-pools) also
describes periodically flooded and dry depressional habitats. Its regional,
seasonal and substrate details cannot be generalized to this unspecified
GOLD class. No organism, microbial mechanism, salinity value or characteristic
community was imported from those examples.

## Completeness

Ignored-inclusive `rg --no-ignore --hidden` searches covered identifiers,
source IDs, label, slug and transient/intermittent/temporary pool variants in
`curation/`, `history/`, `research/`, `conf/`, `docs/`, `src/`, `tests/`,
PATHS and RETIRED, with focused checks of term requests, causal overlays,
GOLD parent exclusions and the research manifest. No target-owned authored
definition, exclusion, causal overlay or research report was found in those
surfaces. Bytecode/dependency environments were not scientific evidence scope.

The structured scan found no exact target rows in the GOLD biosample, triad
or study tables, parameter inventory, BacDive, PREGO or Madin inventories.
The GOLD path table alone contains the target and its separately identified
Microbial mat child. This is a bounded committed-inventory finding, not a
claim that no environmental samples or relevant studies exist globally.

A definition clarifying whether the source denotes the temporary water body,
its persistent basin or the intermittently wet ecosystem would improve future
grounding. Its current absence is an honest sparse SEEDED record, not an
independent major failure. Empty taxa, datasets, parameters, discussions and
causal graphs are appropriate until evidence is scoped to this source.
The fresh-water parent's permanently-wet parameter and osmotic-response graph
must not be copied into the transient-pool record. iModulonDB is not applicable:
no gene, regulator, protein or expression dataset is asserted here.

## Findings

1. **Major: the GOLD classification context becomes a false material is-a.**
   `parent_habitats: ENVO:00002011` asserts that the transient pool is a type
   of fresh-water material. The executed path resolution, inspected parent
   definition and primary pool descriptions support containment/composition,
   not that subclass assertion. Both a temporary water body and its persistent
   basin are distinct from the material. Owner:
   `curation/gold_parent_exclusions.tsv` for the exact
   `habitatmech:GOLD.d39a2ed099` source path and expected ENVO:00002011
   contribution; `curation/term_requests.tsv` if a subsequently justified
   definition and replacement genus are added. Do not patch the generated YAML.

Totals: zero blockers, one major finding, zero minor findings. No unsupported
exact match is recommended. Sparse counts and CLASS/SEEDED status are not
additional findings.

## Recommended Edits

1. Exclude only the exact source-path contribution to ENVO:00002011 through
   the guarded GOLD parent-exclusion table. Preserve both source node IDs,
   the canonical path, collapse note, and zero-count omission.
2. In a separate ITEM-level decision, establish the intended water-body versus
   basin scope. Keep the minted identity if exact equivalence remains
   unsupported. A verified broader water-body or basin genus can be represented
   through the maintained definition/decision surfaces, but must not be chosen
   solely to replace the rejected material edge.
3. Add append-only history and a regression proving that the exclusion leaves
   other-source/ontology parents and the separate Microbial mat child intact.
   Do not change raw snapshots or promote status merely because a review
   report now exists.

## Follow-up Checks

Run dry seed, an inspected forced canary for GOLD.d39a2ed099, closed/open
validation, history validation and full corpus reproduction. Verify the
source/expected-parent guard, preserved counts and node collapse, and any
new genus against current primary ontology definitions. Re-run labels,
provenance, term requests, generated site and full QC after curation. Compare
semantic inputs and perform the genuine map rebuild required by a changed
parent/definition. Confirm that any later definition does not over-specify
regional seasons, hydroperiod, substrate, taxonomy or microbial mechanisms.

## Additional Notes

Only this new timestamped report was authored for this target. No scientific
record, curation table, source, history, page or GitHub item was changed.
The two generated history events reproduce the CLASS sweep and original seed;
this review adds no curation event. No paid research or SSSOM/KGX audit was run.
The full-corpus review goal remains incomplete.
