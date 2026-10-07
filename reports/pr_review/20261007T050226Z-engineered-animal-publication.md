# PR Review: Engineered and Animal-Related Habitats

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1611
- Scientific baseline: `43e6c5d0fb508bcbf7341b8ca5be0141a495f2ed`
- Report commit: `eeea313c4e2d8176afe5db7812133d191befd99f`
- Initial correction/build commit: `1368206b4bc2189a5aecf7b4f7e16f92643ed187`
- Reviewer: Codex, separate adversarial pass; no independent-agent approval claimed.

## Scope and Method

Publish the seven completed individual reports unchanged. The interrupted
Aquarium investigation is not presented as a completed report. Challenge the
reports and authoritative source decisions for component/system, ecosystem/
material, qualified/unqualified identity, source counts, taxonomy aliases,
synonym strength, review accounting and generated-product freshness.

Read the maintained curation guides, exact generated targets, relevant raw
and decision ownership, tests, full changed diffs and rendered claims. Recheck
primary ENVO at a2455d1a77e46bb8a664d65a157166b539269042, PubMed 12620842
and the USDA ARS McGarvey et al. 2004 publication 163878. These sources support
the distinctions, not attribution of every underlying source sample to those
experiments. Full open/closed issue searches returned 671 issues initially,
and 674 when checking the later link defect. Bounded local absence searches
included ignored files; source-export availability remains limited as reported
in the individual reviews.

The reports describe read-only work at their original baseline. Their historical
no-edit statements do not describe this subsequently authorized curation.
No paid research, subagent approval or outside-repository scientific edit occurred.

## Findings and Disposition

1. **Two major hierarchy findings, #1612, corrected.** Guarded exact-path
   exclusions remove Anode's component-to-whole-MFC edge and aquaculture farm's
   ecosystem-to-wastewater-material edge. Retain the farm's independently
   supported agricultural ecosystem parent, all source counts, taxa, predicates,
   provenance and existing review states. No replacement definition is invented.
2. **Major qualifier loss, #1613, corrected.** Replace only the BacDive
   Solid-animal-waste exact-identity decision with GROUND_AS_PARENT/NARROW to
   ENVO:00002276. The restored source mint is ENGINEERED/REVIEWED, retains its
   11 STRAIN attestation and all eight taxa with ranks/pool, and has no invented
   definition. Generic animal waste retains GOLD/PREGO and ten PREGO taxa.
   The source's alias1257027 stays intact, not silently canonicalized or dropped.
3. **Minor new publication defect, #1615, corrected.** Rendered-note inspection
   found `);` included in the USDA URL's query value. An exact-href regression
   failed before the correction. Reword only the maintained decision note to
   delimit the URL with whitespace, regenerate, and preserve the claim's scope.
   This is not a global rewrite of the template's linkification behavior (#1506).
   A fourth append-only session records this correction without altering the
   original split session. The exact-href regression now passes.
4. **Unresolved source evidence, #1614, open.** GOLD Anammox's process-only
   ITEM decision and habitat parent remain in tension. General process literature
   does not determine GOLD node4256's meaning. GOLD's aquaculture-farm path may
   denote a facility or its effluent; removal of the false global parent does
   not prove exact source identity. Target study pages were inaccessible in the
   reviews. Governed original-source metadata is needed before revising these
   interpretations; no process-name-only exclusion or guessed reactor definition
   is applied. Anammox is unchanged.
5. **Existing ingestion contracts remain open.** Added specific witnesses to
   #1249 (typed ontology synonyms), #1459 (close-mapped source aliases), and
   #1257 (PREGO/BacDive missing taxonomy names and explicit merged-ID aliases).
   Those require their own maintained input/rule repairs, not raw-cell/checksum
   or generated-YAML patches. Source-mapping endpoint semantics remain #1398.
   This publication does not certify SSSOM/KGX readiness against current
   kg-microbe modeling or claim all underlying scientific issues are closed.

No further blocking defect introduced by this scoped correction was established.
The existing unresolved findings above are not converted into passing science
merely because serialization and CI are green.

## Preservation and Regression

Two new fail-first full-corpus regressions establish the exact intervention
scope: two parent/event changes, one generic source split and one new record.
They reconstruct the prior inputs and compare every unaffected record and field.
The generic record's other parents and review decisions, each source's count
unit, and every taxon association remain unchanged. Seed events summarize the
current generated build; committed session histories and original reports are
not rewritten. The existing namespace and source-mapping conventions are not
silently altered.

The focused suite passed 69 tests. After the evidence-link correction, both
scope regressions and the new href regression passed again. Four new sessions
explicitly attribute Codex/model/tool. No raw inventory, embedding runtime,
profile pin, map enablement setting or prior immutable map bundle changes.

## Generated Products

- Before: 3,206 semantic rows, JSONL SHA-256
  `807f3d758321ff09838237f4bee221c133b4def5949a199bd7f8b9a7a9fa1dfa`.
- After: 3,207 semantic rows, JSONL SHA-256
  `9b09960700db33d361e73e617daa33c5a27f4628f1dc53c9253f7ddd42a0ea5a`.
- Exactly three existing semantic rows changed, and the BacDive solid-waste
  row was added. No row was removed. The note-link correction is text-neutral.
- New bundle:
  `1ccc4c291fd8853847a903c0c841d494b9c08886f88891717c2f544f8817a312`.

The unchanged locked Linux runtime passed
[map build 37573730170](https://github.com/CultureBotAI/HabitatMech/actions/runs/37573730170).
The canary encoded four vectors and reused all four on repeat. The 32-record
projection canary passed; full embedding reused all 3,207 vectors, and actual
PaCMAP generated the full projection with zero omitted records. Downloaded
inputs are byte-identical to the local export. Both downloaded and imported
bundles validate against the actual profile-bound vector cache. No checksum,
freshness receipt, runtime pin or stale-map guard was weakened.

The temporary branch-scoped read-only build workflow is removed from the final
diff. Rendering produced 3,207 pages, 249 redirects, eight categories and 126
displayed term requests. The original generic animal-waste URL remains live;
the split adds a new URL without deleting an old one. The generated href was
inspected and tested; browser visual QA was not performed.

## Validation and Remaining Gates

Completed before this audit: dry seed, inspected new-record canary, full seed,
exact 3,207-record reproduction, lint, 14-inventory/two-GOLD-source provenance,
curation floor, 249-redirect check, 109-authored-term request check, open/strict
validation of the new record, semantic/cache verification and site rendering.
OAK passed with 1,178 canonical pairs, one synonym, five accepted exceptions
and 2,056 no-adapter skips; it does not certify the missing taxon names or
scientific source equivalence. The first three sessions passed history validation;
the final fourth session is included in authoritative QC.

Pre-product CI failed only the expected stale-map/site test at 1368206b4,
before the rebuilt products were imported. Initial local attempts to inspect
the download ran before it finished and found no files; those were not used
as validation. The completed artifact was then read, compared and validated.
Full local QC is running at audit creation. Final-head CI and exact merge-queue
candidate checks remain mandatory; their terminal receipts will be posted on
the PR before completion, without admin bypass or fabricated approval.

Ignored-inclusive Path.rglob census: 1,093 reports cover 1,092 distinct current
records, with 2,115 of the now 3,207 records remaining and no unparsed reports.
The all-record review goal remains active and unfinished. This publishing
request does not constitute completion of the corpus-wide review.
