# PR Review: Whale Fall and White Smoker

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1599
- Scientific baseline: `c271b83aa1f3bce93f4e3cb171e6d3e66767fa09`
- Review-report commit: `9a9d16e0a1849428a86a8914cf56007b3719c24b`
- Correction/build commit: `e4a8077e1b311bc7229ff5bc2e7abfea3e13a906`
- Reviewer: Codex, separate adversarial pass; no independent-agent approval claimed.

## Scope and Method

Publish the two completed individual reviews unchanged and correct their bounded
local findings. The unfinished wood-fall review is excluded. Read both complete
records and reports, maintained curation contracts, source-parent loader and
application, deterministic history emission, definition ownership guard,
mechanism tests, new full-corpus regression, session histories and generated
diffs. Challenge source-bin versus ontology scope, independent-parent retention,
status and count preservation, lexical versus conceptual equivalence, provenance
attribution and generated-product freshness.

Ignored-inclusive searches across curation, history, tests, docs and workflows
found the existing white-smoker decision but no target-owned exclusions or
sessions. GitHub all-state phrase/identifier searches found no duplicate for
these specific corrections. Existing #1215 concerns the Fossil record's own
parent, not whale fall's edge; #1340 concerns host-associated strains and is not
resolved here. The searches were bounded, not a claim of universal absence.

## Findings and Disposition

1. **Major, #1600: unsupported Fossil superclass.** Added exactly one guarded
   exclusion for habitatmech:GOLD.6de51dbee8, full path
   `Environmental > Aquatic > Marine > Fossil > Whale fall`, expected resolved
   parent habitatmech:GOLD.88e2b29307. Modern carcasses belong to the general
   whale-fall class; the unresolved legacy source bin supplies no reviewed
   broader-than semantics. Retain ENVO:01000139 animal carcass fall. Do not
   equate the parent mint to fossil material or claim sample-bin equivalence.
2. **Minor, #1601: inaccurate exact-label rationale.** Corrected only the note
   on habitatmech:GOLD.d28b62ff00. White smokers is curator-recognized as plural-
   equivalent to white smoker, not equal under the actual normalization. A fresh
   executed route starts at gold_unmatched and applies ITEM GROUND. Retain the
   original decision's actor/date; a new session attributes this repair to Codex.
   The generated GROUND event renders the current note deterministically; no
   committed session history was rewritten.
3. **Major, #1602: upstream definition overclaim remains unresolved.** The
   white-smoker definition generalizes alkalinity and continuous thioester
   production. Submitted the scoped correction to
   [EnvironmentOntology/envo#1674](https://github.com/EnvironmentOntology/envo/issues/1674)
   and linked it to the local tracking issue. No upstream acceptance, corrected
   ontology release or governed downstream refresh is claimed. This issue stays
   open; it is not silently closed with the two local corrections.

Fresh official typed ENVO at revision
`a2455d1a77e46bb8a664d65a157166b539269042`, 106,817 triples, confirms both
active identities, the true carcass-fall genus and the marine hydrothermal-vent
hierarchy. The problematic definition is upstream text, not a local copy error.
Freshly read the [Treude et al. primary abstract](https://www.researchgate.net/publication/240642986_Biogeochemistry_of_a_deep-sea_whale_fall_sulfate_reduction_sulfide_efflux_and_methanogenesis)
about a modern carcass deployment; the individual report also records inspected
site methods. Fresh NCBI XML for [Nakagawa et al.](https://pubmed.ncbi.nlm.nih.gov/16343320/)
confirms acidic TOTO white-smoker fluids. The [Huber and Wachtershauser abstract](https://pubmed.ncbi.nlm.nih.gov/9092471/)
describes a laboratory model, not universal continuous field production. No
universal numerical parameter or taxon assertion is derived from these studies.

`validate_curated_definitions` rejects ontology-owned grounded terms. A local
term request cannot override ENVO here. Retain that ownership guard: fix ENVO,
then refresh actual governed sources rather than patching YAML or raw checksums.
No additional defect in the bounded local fixes was established.

## Preservation and Regression

`test_whale_fall_parent_and_white_smoker_note_have_exact_scope` builds all 3,206
records with and without only these changes. Membership is identical and only
ENVO:01000140 and ENVO:01000257 differ. Whale fall loses one parent contribution
and gains one SOURCE_PARENT_EXCLUDED event. Its prior event, true genus,
GOLD4000 path/predicate, count omission and EXACT/SEEDED state remain equal.
White smoker changes only the deterministic note text of its original event;
the other event, source GOLD8303, synonym, both true parents, omitted count/unit
and EXACT/REVIEWED state remain equal. All other records, including the Fossil
parent and related host records, are unchanged. Existing tests verify stale
mint/path/parent rejection and independent ontology, curator and other-source
parent retention. All 33 focused tests passed in 37.29 seconds.

Structured before/after TSV comparison proves exactly one decision's notes
changed; all other columns and 1,810 rows are identical. The standard whitespace
check flags that row's retained trailing tabs, which encode two empty optional
TSV columns. All 11 fields are present and values have no surrounding whitespace;
the whitespace check excluding this structured TSV passes. No format or metadata
churn was introduced to hide valid empty columns.

## Generated Products

Full semantic exports each contain 3,206 records. Only whale fall changes,
losing the unsupported Fossil parent line. The white-smoker note is correctly
excluded from embedding text.

- Before JSONL SHA-256: `9662ba781a3f97222814ea346fb191ddec51f09e842bfc05e1a3e58434be4e4e`
- After JSONL SHA-256: `5aa8d821cd1b8cea97df876a72e449375afd6906f71144e77391f4186632aa5b`

The unchanged locked Linux runtime passed
[build 37554099106](https://github.com/CultureBotAI/HabitatMech/actions/runs/37554099106).
The changed-record canary encoded one vector and reused it on repeat. The
32-record projection canary passed; the full embed reused all 3,206 vectors and
actual PaCMAP rebuilt the complete projection. Downloaded input bytes equal the
local export. Both downloaded and imported bundles passed local validation
against the downloaded real vector cache. New immutable generation:
`2b1ab9ea4e03a5746576bee02ff9da2079e7d0e602f0b115129f3c3366af70de`.
Older generations remain; no coordinate or freshness receipt was fabricated.
The temporary read-only branch-scoped workflow is removed from the final diff.

## Validation and Remaining Gates

Completed before this audit: dry seed; forced target canaries and complete
generated-record inspection; 33 focused tests; exact 3,206-record reproduction;
target open/closed schema; both new histories; lint; provenance for all 14
inventories and two GOLD sources; curation floor; and OAK correspondence
(1,178 canonical, one synonym, five accepted exceptions, 2,055 no-adapter skips,
no failing pairs). Reports are byte-identical to the report commit. The default
history-helper path was unavailable; setting CLAW_SRC to the actual checkout
produced validated sessions without modifying the shared tooling.

Site regeneration and full local QC are running at audit creation. Final-head
CI, exact-tree merge-queue checks and post-merge integrity remain required.
Final receipts will be posted on the PR; no admin bypass or self-approval is
used. Browser visual QA was not performed.

Ignored-inclusive Path.rglob census: 1,073 reports cover 1,072 distinct current
records; 2,134 of 3,206 remain, with no unparsed reports. The all-record goal is
unfinished. #1398 was freshly verified open; this publication does not certify
SSSOM/KGX modeling readiness or current kg-microbe endpoint compatibility.
