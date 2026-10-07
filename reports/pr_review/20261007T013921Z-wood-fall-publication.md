# PR Review: Wood Fall

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1603
- Scientific baseline: `c74adeca82fc8a28cb2863d96100741ef46eff38`
- Review-report commit: `53844715f2341015090506eafee315278d759e02`
- Correction/build commit: `83c79e5026dd0ebf93f92c099d679a0b67ebf93f`
- Reviewer: Codex, separate adversarial pass; no independent-agent approval claimed.

## Scope and Method

Publish the completed individual wood-fall review unchanged and correct its
bounded hierarchy finding. The unfinished xeric-basin investigation is excluded.
Read the complete record and report, maintained curation contracts, source-parent
loader/application, deterministic history emission, mechanism tests, new
full-corpus regression, both session histories and generated diffs. Challenge
context versus subsumption, independent-parent retention, source/count/status
preservation, attribution and product freshness.

Ignored-inclusive searches across curation, history, tests and docs found no
target-owned exclusion or session before editing. All-state GitHub phrase/mint
searches found no duplicate issue for this correction. These are bounded searches,
not assertions that no other evidence exists anywhere.

## Findings and Disposition

1. **Major, #1604: benthic context emitted as a superclass.** Added one guarded
   exclusion for habitatmech:GOLD.615f1a92a4, exact path
   `Environmental > Aquatic > Marine > Benthic > Wood fall`, expected resolved
   parent ENVO:01000024. A woody accumulation is not the surrounding biome.
   Retain ENVO:01000138 plant matter fall. Benthic's own CLOSE mapping is not
   re-adjudicated. This does not assert a replacement relation.
2. **Minor, #1605: incorrect scaffolder-default actor name.** The first new
   session accidentally defaulted its actor name to claude-code; model/tool were
   already codex-gpt-5/codex. Added a second append-only AUDIT with explicit actor
   codex-gpt-5, referencing the earlier filename and superseding only its actor
   attribution. No second scientific edit is claimed. Both histories validate;
   neither the earlier session nor the historical individual report was rewritten.

Fresh official typed ENVO revision
`a2455d1a77e46bb8a664d65a157166b539269042`, 106,817 triples, confirms active
wood fall, its definition, absence of typed synonyms and the sole named plant-
matter-fall parent. The marine benthic biome is a separate ecosystem-scale class.
The [primary study](https://www.nature.com/articles/s41598-017-17463-2),
DOI:10.1038/s41598-017-17463-2, PMID:29343757, was freshly checked through
[Europe PMC full-text XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5772046/fullTextXML)
after web fetch failed. Its abstract and complete Methods describe two experimental
wood deployments above sediment, not universal habitat measurements or a verified
GOLD study-to-BioSample crosswalk. No additional numerical, taxon or causal claim
is introduced. No additional defect in the bounded scientific fix was established.

## Preservation and Regression

`test_wood_fall_context_exclusion_has_exact_scope` builds the full corpus with
and without only the new exclusion. Membership is identical and only
ENVO:01000142 changes: remove the one parent contribution and append one
SOURCE_PARENT_EXCLUDED event. Retain the prior event, ontology genus, definition,
identity, GOLD5712/path/exact predicate, omitted count/unit and EXACT/SEEDED state.
All other fields and all other records, including Benthic, remain equal.
Existing tests reject stale mint/path/parent guards and preserve independent
ontology, curator and other-source contributions. All 34 focused tests passed
in 28.25 seconds. No generated record was hand-edited.

## Generated Products

Complete before/after semantic exports each have 3,206 records. Only wood fall
changes, losing the unsupported marine-benthic-biome parent line.

- Before JSONL SHA-256: `5aa8d821cd1b8cea97df876a72e449375afd6906f71144e77391f4186632aa5b`
- After JSONL SHA-256: `35fd75552af25c5b03e11d872b4bd6ad0df5582abe990021604da8aefd91a6a1`

The unchanged locked Linux runtime passed
[build 37557921016](https://github.com/CultureBotAI/HabitatMech/actions/runs/37557921016).
The changed-record canary encoded one vector and reused it on repeat; the
32-record projection canary passed. The full embed reused all 3,206 cached
vectors and actual PaCMAP rebuilt the complete projection. Downloaded inputs
are byte-identical to the local export. Downloaded and imported bundles passed
local validation against the downloaded real vector cache. New immutable bundle:
`1a912ce8fdce19dc14a29c6cc68e71ce97d2e4da228565f239e838b31f0052ff`.
Older generations remain; no coordinates or freshness receipts were fabricated.
The temporary read-only branch-scoped workflow is removed from the final diff.

## Validation and Remaining Gates

Completed before this audit: dry seed; forced canary and complete-record
inspection; 34 focused tests; exact 3,206-record reproduction; target open/closed
schema; both new histories; lint; all-source provenance; curation floor;
whitespace check; and OAK correspondence (1,178 canonical, one synonym, five
accepted exceptions, 2,055 no-adapter skips, no failing pairs). The individual
report is byte-identical to its original commit.

Site regeneration is running at audit creation. Full local QC, final-head CI,
exact-tree merge-queue checks and post-merge integrity remain required. Final
receipts will be posted on the PR; no admin bypass or self-approval is used.
Browser visual QA was not performed.

Ignored-inclusive Path.rglob census: 1,074 reports cover 1,073 distinct current
records; 2,133 of 3,206 remain, with no unparsed reports. The all-record goal is
unfinished. #1398 was freshly verified open; this publication does not certify
SSSOM/KGX modeling readiness or current kg-microbe endpoint compatibility.
