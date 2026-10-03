# YAML Record Review: lotic water body

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/lotic_water_body.yaml`
- Started UTC: 2026-10-03T17:14:38Z
- Finished UTC: 2026-10-03T17:17:03Z
- Verdict: needs curation

## Target

Read the complete generated `HabitatRecord`, `ENVO:01000618`, lotic water body,
AQUATIC, EXACT, REVIEWED. Its sole attestation is GOLD's Environmental >
Aquatic > Freshwater > Lotic, source concept `habitatmech:GOLD.283c698731`.
`PATHS.tsv:850` pins the stem. The ITEM GROUND decision at
`curation/decisions.tsv:316` owns the exact identity; the embedded decision
and seed history accurately describe the generator, not scientific validation.

## Validation

- `just validate data/habitats/aquatic/lotic_water_body.yaml`: pass.
- `just validate-strict data/habitats/aquatic/lotic_water_body.yaml`: one file,
  zero errors.
- Fresh `just qc` was active at review finish: lint, documentation and raw
  provenance passed; tests were running. Full history, corpus reproduction,
  site, redirects and term requests are later full-corpus gates, not inferred
  passed from this focused validation.
- Current official ENVO OWL was fetched and parsed in full. SHA-256:
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  It byte-matched the earlier local OWL. OLS web fetches failed; the official
  OWL supplied the inspected definitions, synonym predicates and hierarchy.
- No DOI/PMID, taxon, graph or dataset claim is attached to this target.
  Study accessions below were verified in the committed source table, not
  claimed to have been checked on live GOLD study pages. OAK's full network
  gate is deferred to CI for this reports-only change.

## Identity and Grounding

The identifier, canonical label, definition and AQUATIC category agree with
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
However, the term denotes an entire flowing water body without a freshwater
restriction. GOLD's complete path is narrower. The ITEM decision's claim of
exact equivalence and the resulting exact attestation do not preserve that
scope. Keeping the path as provenance does not repair the identity assertion.

`ENVO:00000063` water body is the true direct ontology parent. The extra
`ENVO:00002011` fresh water denotes material and enters through GOLD's second
parent pass (`seed.py:898-907`). Current ENVO instead models
`ENVO:01001320` fresh water body through composition with fresh water, not
subsumption under the material. The complete maintained water-body and
fresh-water records were read for context, not counted as additional reviews.

Preserve a freshwater-qualified identity with justified broader grounding to
the lotic class, unless a genuinely exact freshwater-lotic term is established.
No globally exhaustive claim about absence of such a term is made. The current
OWL label search found only the generic lotic class. Do not substitute stream,
river, freshwater biome, or sampled mat material as exact identity.

## Evidence

`gold_ecosystem_paths.tsv:206` has two nodes, 4342 and 4645, at depth four,
with 95 ORGANISM assertions. The displayed first node, count and note match.
`gold_path_biosamples.tsv:329` independently has 58 samples at path ID 4645.
These are different source units, not missing or additive organism counts.

API rows 359-361 describe 56 samples and 14 studies. Broad context is modal
`ENVO:00000873` freshwater biome (five terms, share 0.61, nine agreeing
studies); local is `ENVO:00000023` stream (14 terms, share 0.32, three studies);
medium is `ENVO:01000157` microbial mat material (eight terms, share 0.27,
two studies). All three meanings were inspected in current OWL. The weak
local/medium modes neither narrow the entire source to streams nor turn it
into mat-derived material. The other terms are not exposed by this summary.

Exact membership checks across all 4,587 committed study rows find 14 studies:
Gs0045858, Gs0054941, Gs0063570, Gs0067861, Gs0084963, Gs0087377,
Gs0096913, Gs0111418, Gs0111472, Gs0113835, Gs0114738, Gs0121696,
Gs0121722 and Gs0131204. Some also name River, Lake, or other source paths;
shared study membership does not equate those habitats. Bulk and API sample
counts remain separate. An initial broad CSV value scan encountered a list
in an unrelated row; the corrected string-field membership scan completed.

## Completeness

Ignored-inclusive ID, label, stem and full-path searches covered curation,
raw inventories, PATHS, history, research and prior individual reports. They
found the ITEM decision but no target definition, causal overlay, dedicated
session-history file or completed individual report. The earlier waterfall
review mentions this parent; that is not a review of this target.

Optional mechanisms, organisms and parameter bands should not be borrowed
from the parent records. iModulonDB is not applicable to this target without
a molecular, organism-specific or transcriptomic assertion. Its absence is
not negative ecological evidence.

## Findings

1. **Major M1: freshwater source exactly grounded to an unrestricted class.**
   Owner: the ITEM decision at `curation/decisions.tsv:316`, with scoped
   definition inputs if a minted identity is retained. Preserve the source
   qualifier, update mapping/synonym semantics and append actual curation
   history rather than hand-editing the generated status or old event.
2. **Major M2: whole water body is-a fresh-water material.** Owner: maintained
   exact-source parent controls consumed by `src/habitatmech/seed.py:898`.
   Remove only this contribution; retain the true water-body ancestry.

Blockers: 0. Major: 2. Minor: 0.

## Recommended Edits

Correct the source-specific grounding and material-parent contribution through
maintained inputs. Do not blanket-REPLACE all parents: the ontology parent is
true. Keep node IDs, full path, 95 ORGANISM assertions and all independent raw
inventory evidence. Do not globally redirect `ENVO:01000618` to a freshwater
source: current watercourse and waterfall records legitimately reference the
generic ontology parent. Their identity/hierarchy must survive a source split.

## Follow-up Checks

Dry seed, canary the exact source, inspect the generated record and both parent
contributions, then test that generic watercourse/waterfall ancestry is not
made freshwater-only. Run strict and OAK checks, history validation, exact
corpus reproduction, supported map/site/redirect generation and full QC.
Regeneration dependencies #1217/#1218 must not be bypassed.

## Additional Notes

All 437 returned open/closed issues and their comments were searched. #1220
owns other fresh-water material-parent cases; #1260 concerns Lentic, not this
independently reviewed Lotic source. This review changes no decision, generated
record, page or history entry. Only this target adds to completed coverage.
