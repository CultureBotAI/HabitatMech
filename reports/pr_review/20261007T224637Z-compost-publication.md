# Compost Publication Adversarial Review

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1663
- Baseline: `fd0276142f5c5a8a8a8982f985669ad853b013e4`
- Report commit: `385152ea8e11e7ee66122a668b998a7ae66642a1`
- Correction head: `f4080bc704dc7482af9b8c0e115b4bac94a7506b`
- Snapshot UTC: 2026-10-07T22:46:37Z
- Disposition: corrections implemented; publication blocked on generated map/site
  and required checks. This is not merge approval or a full-QC pass.

## Scope and Method

Separate adversarial self-review by Codex, not an independent reviewer. Read
both complete individual reports, maintained inputs, relevant seeder routes,
schema semantics, tests and generated changes. Preserve immutable review-time
reports; they do not describe the corrected tree. Rechecked primary EPA/NLM
scope evidence and the cited graph evidence against the reports' access bounds.
The Finore article is a review, while Richard's primary abstract was inspected;
neither supports transferring graph functions to every associated taxon.

Gitignore-independent local searches and the complete 707-item GitHub issue
response were used to deduplicate findings. The two existing implementation
issues were read in full. Contextual record reads are not additional completed
individual reviews.

## Findings and Disposition

1. **Major, #1459:** CLOSE-mapped GOLD and BacDive labels were promoted to exact
   synonyms. Corrected from each source's resolution, not aggregate grounding.
   Related scope and deterministic audit now preserve spelling, original source
   attestations and independently supplied ontology synonyms. EXACT routes and
   the pre-existing canonical-ancestor guard remain tested. Untyped ontology
   synonym interpretation remains the separate #1249 contract.
2. **Major, #1664:** generic compost acquired an unsupported Solid Waste genus
   from GOLD input context. One exact source/path/expected-parent exclusion now
   removes that contribution while preserving ENVO:03501300 manure. No qualified
   Composting identity, legal classification or original-source scope is guessed.
3. **Major, #1665:** graph node types conflated material, a compost phase and a
   functional grouping with an axis, cellular state and taxon. The overlay now
   models environmental material, temperature and community succession, with
   compatible edge endpoints/predicates. Citations, exact snippets and earlier
   graph history are retained; thermophilic-stage scope remains explicit.
4. **Minor, #1264:** environment co-attestor review accounting occurred only for
   new concepts. Registration now occurs once per habitat/source mint, preserving
   distinct env_type sources on a shared record. Current compost counts five
   reviewed sources and emits the existing environment ITEM event; water is also
   covered. Multi-band input is not miscounted as multiple sources.
5. **Minor, #1666, unresolved:** two tokenized MADIN taxon names require governed
   source extraction. Ignored-inclusive searches of the configured kg-microbe
   data tree found no Madin/NCBITaxon source paths; local retained inventories
   cannot reconstruct the pinned original dump. No raw manifest, generated
   label or association was manually patched. The issue remains open.
6. **Publication blocker:** the compost parent change makes the map/site stale.
   The renderer rejects it before publication. The locked Torch runtime has no
   Intel macOS wheel; no dependency/pin was changed. A branch-scoped, read-only
   Linux build is queued, not successful. The PR is draft until products and
   checks are complete. No additional blocking code defect was established.

## Verification

- 62 focused tests passed, covering both alias routes, CLOSE/EXACT, independent
  exact aliases, shared spellings, new/existing environment concepts, ITEM/CLASS/
  unreviewed sources, multiple bands and sources, real compost/water audits,
  graph connectivity/evidence and full-corpus parent-exclusion impact.
- Full 3,207-record pre/post comparison: 144 changed records; 133 synonym lists;
  only compost's parent list and graph change. No identity, status, attestation,
  parameter or taxon change; every earlier generated history event remains.
- Alias comparison: 140 source exact entries removed and 144 related entries
  added, with no lost spelling or ontology-source entry. Existing de-duplication
  changes the related `Creek` display source from PREGO to GOLD in stream; the
  independent ENVO exact entry, raw PREGO synonym and both attestations remain.
  This is the existing first-source policy, not new exact equivalence.
- Dry seed and inspected compost canary preceded full guarded regeneration:
  3,207 records written, zero failures. Fresh full reproduction has zero missing,
  extra or differing records. All 32 graph overlays and 164 histories validate.
- Four session scaffolds inherited the wrong actor.name default. The append-only
  `pr1663_actor_correction` record explicitly identifies Codex as the actor;
  original timestamps/actions and correctly supplied model/tool fields remain.
- OAK passed: 1,178 canonical, one synonym, five accepted exceptions, 2,056
  no-adapter skips. Minted IDs and source taxon labels are not adapter coverage.
- Full semantic-input export retains 3,207 identifiers and changes only compost
  text/hash. SHA256: `e653ef57ae7e63fa660039319a3f55c6ae0b3390e1f6429f0252ad15f9190351`.
  Comparing semantic_text without resolved parent labels is not sufficient for
  map freshness; the full adapter export, not that preliminary projection, was
  used to establish the product change.
- Full local QC is running at this snapshot. A restricted-network vendored
  check failed fetching the canonical manifest; the approved network retry is
  pending. Neither is reported as a pass here.

## Remaining Gates

[Linux build 37697834420](https://github.com/CultureBotAI/HabitatMech/actions/runs/37697834420)
must produce a verified full bundle at the correction head. Check artifact input
bytes against the local full export, canary encoding/reuse, complete cache and
finite coordinates. Install the actual new generation and pointer, regenerate
site, and remove the temporary build workflow. Never update only a receipt/hash
to hide stale vectors or bypass the renderer.

Then rerun local full QC and required final-head checks, mark the PR ready, and
enter the native merge queue at the exact reviewed head. Verify combined queue
checks, actual MERGED state and reconstructed merge tree before deleting local
or remote branches. Keep #1666 open; close corrected issues only on merged fixes.

PR #1661 remains a separate pending report-only ancestor with its own queued
checks and enabled auto-merge. It was not changed or treated as merged. Its
Commercial compost source-scope issue #1662 remains unresolved. Final receipts
belong in the PR after the gates complete, not in a rewritten snapshot.

The broader record-review goal is still incomplete: 1,150 distinct records
reviewed, 2,057 remaining, from an ignored-inclusive census of 1,152 reports.
No SSSOM/KGX readiness or full-corpus scientific approval follows from this PR.
