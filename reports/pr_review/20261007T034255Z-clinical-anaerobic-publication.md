# PR Review: Clinical and Anaerobic Habitats

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1607
- Scientific baseline: `ec95a7191a9b6c9ddaa404c2062f7be9932623a9`
- Report commit: `242fc4f0fd5c3fe8c6fc72cb2eb07407a6f3fbd7`
- Initial correction/build commit: `f94572078b317e4bfbfb62c252eac00e7efd67ee`
- Reviewer: Codex, separate adversarial pass; no independent-agent approval claimed.

## Scope and Method

Publish 11 completed individual reports unchanged. The unfinished Anammox
investigation is excluded. Review the report claims, authoritative decision
semantics, exact source paths, parent exclusions, synonym ingestion, current
records, new tests and histories, generated diffs and semantic inputs. Challenge
procedure versus specimen, reactor versus material or region, source counts,
synonym equivalence, status promotion and unsupported association repairs.

The reports describe their original baseline and limits; their read-only
statements are historical, not descriptions of this later authorized curation.
No paid research or outside-repository scientific edit was performed. Existing
all-state issue titles and relevant issue bodies/comments were checked before
filing new findings. Bounded ignored-inclusive searches include local source
availability checks; they do not establish global absence of evidence.

## Findings and Disposition

1. **Major, #1608: Biopsy habitat-status contradiction.** Change only its ITEM
   decision from CONFIRM_UNGROUNDED to NOT_APPLICABLE. The aggregate names a
   collection-method grouping, not a single anatomical habitat. Keep the mint,
   procedure xref, CLINICAL category, REVIEWED state, 95 STRAIN observations,
   25 retained taxa/pool 73, exclusion ledger and retired URL. Do not claim
   that BacDive never supplies sites or that specimens cannot host microbes.
2. **Five major parent findings, #1609.** Guarded exclusions remove only the
   reviewed GOLD contribution: digester to facility; digester sludge to vessel;
   digestor to waste-water material; anaerobic sludge to bioreactor; anaerobic
   zone to whole PNA setting. Keep independent sludge genera and all identities,
   counts, taxa and existing review states. Do not fabricate replacement
   definitions or equate a source node with a published reactor experiment.
3. **Two major Sludge synonym findings, partial #1459.** A canonical GOLD leaf
   resolving to a different strict ontology ancestor now remains RELATED,
   not EXACT. The same mechanical witness exists in exactly 12 current records,
   pinned by a corpus regression. Preserve spellings, attestations and
   independent ontology aliases. The original CLOSE/Saline cases and untyped
   ontology synonyms remain outside this repair; #1459 and #1249 stay open.
4. **New adversarial edge case, #1610.** Mutual reachability in a cyclic
   ontology is not strict ancestry. A synthetic two-node cycle failed before
   adding the reverse-ancestry guard; strict, unrelated and cyclic controls
   now pass. No current corpus witness was established and this refinement
   changes no generated scientific field.
5. **Minor, unresolved #1257.** Anaerobic sludge blanket reactor retains an
   unlabeled NCBITaxon:517543 association. The review verifies the direct current
   name Toxopoda sp. 2 RM-2008, not a replacement ID or false association.
   [Added target-specific evidence](https://github.com/CultureBotAI/HabitatMech/issues/1257#issuecomment-6030343066)
   to the existing governed PREGO/NCBI maintenance issue. Fresh case-insensitive,
   ignored-inclusive filename scans of build and configured kg-microbe/data
   found no PREGO node/edge or ncbitaxon_nodes.tsv inputs. Source recovery,
   versioned extraction, provenance and subsequent map regeneration remain
   necessary; no isolated raw/checksum or generated-YAML patch was made.

The primary sources inspected in the individual reviews distinguish the
entities, not universal experimental values or every underlying association.
Fresh publication reads rechecked the EPA reactor/material account, BacDive
154980 and PubMed 20646732. The clinical reports independently verify NCI
synonyms for catheter and tracheal aspirate: a CLOSE source mapping alone was
not their justification for lexical equivalence. No further blocking report
defect was established.

## Preservation and Regression

Full baseline-to-current comparison finds exactly 16 changed records. Allowed
changes are Biopsy status/history, five parent/history contributions and twelve
synonym-scope/history changes, with two overlapping sludge targets. All other
fields, source observations, identifiers and corpus membership are unchanged.
The eight new append-only sessions have explicit Codex actor/model/tool values.
Generated history summarizes current decisions; original reports and committed
session histories are not rewritten.

The new regression reconstructs the corpus without the six decision/exclusion
changes and proves exact scope, retained independent parents, preserved source
fields and status. Synonym tests pin all twelve affected IDs, preserve independent
aliases, prove deterministic events and show scope-only text neutrality.
Initial focused suite: 71 passed. After the adversarial refinement, all five
new regression cases pass. Two initial unit fixtures omitted their required
ontology column; this was corrected without weakening production validation.

## Generated Products

Both complete semantic exports have 3,206 records. Exactly five rows change,
each losing the unsupported parent line. Biopsy status and synonym scope are
text-neutral under the current adapter.

- Before JSONL SHA-256: `35fd75552af25c5b03e11d872b4bd6ad0df5582abe990021604da8aefd91a6a1`
- After JSONL SHA-256: `807f3d758321ff09838237f4bee221c133b4def5949a199bd7f8b9a7a9fa1dfa`
- New bundle: `dd78700eb081531c4047c9bef091d25b56e1c1a68fbac7d8a37bfdc3b0731b93`

The unchanged locked Linux runtime passed
[map build 37567589374](https://github.com/CultureBotAI/HabitatMech/actions/runs/37567589374).
The changed-record canary encoded five vectors, then reused all five; the
32-record projection canary passed. Full embedding reused all 3,206 vectors,
and genuine PaCMAP regenerated the full projection. Downloaded inputs are
byte-identical to the local export. Both downloaded and imported bundles
validate against the real vector cache. Older immutable bundles remain.
The temporary branch-scoped read-only workflow is removed from the final diff.

An initial artifact-copy command guessed a nonexistent bundles subdirectory;
the renderer correctly refused the incomplete import. The actual generated
directory was located, copied intact, validated and successfully rendered.
No stale-map guard, runtime pin or freshness receipt was weakened.

## Validation and Remaining Gates

Completed: dry seed, inspected sludge canary, full regeneration, exact 3,206-
record reproduction (also after the cycle fix), lint, inventory provenance,
term-request check (109 authored terms), OAK correspondence (1,178 canonical,
one synonym, five accepted exceptions, 2,055 no-adapter skips), semantic/cache
checks and site rendering (3,206 pages, 249 redirects, eight categories and
126 displayed term requests). The initial seven sessions validated; final
QC includes the eighth session. Historical report diff is empty.

Initial-head CI failed only the stale map/site test, as expected before the
rebuilt products were imported. A redundant pre-render standalone local test
run was stopped in favor of fresh authoritative QC on the final products.
Full local QC is running at audit creation; final-head and exact merge-candidate
checks remain mandatory. Final receipts will be posted on the PR before
completion, with no admin bypass or self-approval. Browser visual QA and original
source dump re-extraction were not performed.

Ignored-inclusive Path.rglob census: 1,086 reports cover 1,085 distinct current
records; 2,121 of 3,206 remain, with no unparsed reports. The all-record goal
remains unfinished. This PR does not certify SSSOM/KGX readiness against current
kg-microbe modeling.
