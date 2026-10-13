# Engineered Record Publication Review

- PR: https://github.com/CultureBotAI/HabitatMech/pull/1634
- Baseline: `c54d9263c97873f825caf023896571c256c1deb6`
- Report commit: `342688b0ec2de0013b2c75908065bfd9094a22c6`
- Reviewed fix: `2e1a471fe6984cf419a412b43d38317dccb9467f`
- Snapshot UTC: 20261007T122345Z
- Status: curation and generated products ready for final checks; full local QC
  is running, final-head and merge-group CI have not yet passed.

## Scope and Method

Publish 24 immutable individual reports covering 23 engineered records. The
second biofilter report supersedes an inventory-filename citation only, not
another record. Earlier reports describe their review-time trees and validation
limits; they are not rewritten to imply that subsequent corrections existed.

This is a separate adversarial pass by Codex, not an independent human or agent
approval. Re-read all eleven correction targets and their report findings;
checked maintained source/path/expected-parent guards, independent genera,
primary abstracts, complete input/test/generated-record diffs and session actors.
The report-only commit is unchanged. Searches for existing exclusions/tests
included ignored and hidden files. The complete 259-open-issue title inventory
was screened for duplicate scope; related synonym issues were distinguished.

## Findings and Disposition

1. **Major, #1635:** eleven material/device/location context contributions were
   emitted as strict `parent_habitats`. Exact exclusions retain independent
   genera and all other record fields, except one appended audit event per
   record. All full source paths, original source IDs, count/unit values or
   omissions, collapsed-node notes, predicates, mints and statuses survive.
   Existing anaerobic-biomass ITEM review remains REVIEWED; the other ten
   targets remain SEEDED. The SSF Unclassified path uses its actual nonempty
   source levels for the expected parent. Parent identity is not silently
   reinterpreted.
2. **Minor, #1639:** semicolons following ten new PubMed URLs became part of
   rendered hrefs. Maintained notes now close parentheses immediately after the
   URL, with DOI in separate parentheses. The published-page regression grows
   from three to thirteen exact article links. The first history is preserved;
   a second append-only session records the citation-format repair.
3. **Unresolved, #1636:** eight source-scope findings require original GOLD
   interpretation before an ITEM identity or parent decision. Inaccessible
   study pages are not evidence for automatic NOT_APPLICABLE or a fabricated
   physical-habitat definition.
4. **Unresolved, #1637:** scrubber-biofilm definition restriction and automatic
   promotion of a broader old label to exact synonym need separately reviewed
   definition/alias changes, with broad impact testing.
5. **Unresolved, #1638:** generic bioreactor graph scope, community-as-TAXON
   typing, and hydrogen/carbon-substrate wording remain open. A deliberate
   semantic/schema review and outstanding claim-level sources are required.

The eleven targets, exact identifiers and their individual evidence reports
are listed in [#1635](https://github.com/CultureBotAI/HabitatMech/issues/1635).
Fresh inspected abstracts include Reguera PMID16936064, Gao PMID25514396,
Arora PMID29564535, Speth PMID27029554, Kleerebezem PMID15889396 and Suzuki
PMID15246435. ENVO's same-day inspected immutable revision is
`a2455d1a77e46bb8a664d65a157166b539269042`. These support bounded
material/device/location distinctions, not source-to-experiment crosswalks or
transfer of organisms, operating conditions or mechanisms.

## Completed Verification

- The new corpus-wide regression failed before the rows existed. All 35
  exclusion tests passed afterward, comparing all records and every field.
- Dry seed passed. The complete GOLD.080ba885f8 canary was inspected before
  bulk validated regeneration: 3,207 written, zero failures.
- Open canary validation and strict validation of all 3,207 records passed.
  Exact full reproduction: zero missing, extra or differing records.
- All 148 history records validate, with explicit Codex/gpt-5/codex attribution.
  No previous history was edited.
- OAK: 1,178 canonical, one synonym, five accepted exceptions and 2,056
  explicitly skipped no-adapter pairs. Minted identifiers are not adapter
  coverage.
- All 18 governed artifacts match canonical. Lint, curation floor and provenance
  pass; all 14 inventories and two GOLD sources remain current.
- The previous exclusion rows and the 24 original reports are byte-unchanged.
  No application, schema, raw inventory, grounding decision, term request,
  causal overlay, PATHS or RETIRED change is included.
- Full semantic input comparison changes exactly eleven target rows, with all
  3,207 identifiers retained. Input SHA256:
  `6c5c416740a0aeb7433f747a74d643fd5ad135f4cfca0acea50083300d7cce54`.
- [Supported-runtime map build 37619535451](https://github.com/CultureBotAI/HabitatMech/actions/runs/37619535451)
  succeeded at the reviewed fix. Canary: 11 encoded, repeat: 11 reused; full
  pass: 3,207 reused. The downloaded input matches local export byte-for-byte.
  Full bundle/cache validation passes with 3,207 unique finite-coordinate points,
  complete display coverage and no omissions.
- Selected map generation:
  `786ff52a3438b82184fc92693d7e90330ca7f308f86683b43a73f7e89a09e68c`.
  Preserve earlier immutable generations; stage only this new one and its pointer.
- Site regeneration completed: 3,207 habitat pages, 249 redirect stubs, eight
  categories and 126 term requests. The diff changes only the eleven target
  habitat pages and the generated full map products. Inspected rendered
  hierarchy/citation diffs and parsed all eleven new citation links.
- The temporary Linux build workflow is removed from the final working tree.
  The Intel local host cannot run the governed ARM-only macOS Torch wheel;
  the checked Linux artifact avoids changing or weakening the pinned runtime.

## Remaining Publication Gates

The interim fix-head CI run failed exactly two tests: stale map/site and missing
new citation links in pre-regeneration pages (522 passed, three skipped).
Those products are now regenerated; the failure is not represented as a pass.
Full local QC is currently running on the regenerated tree. Finish it and the
final-head required checks, then the native merge-group checks before merging.
No check or branch rule may be bypassed.

The user explicitly authorized merge and branch deletion. After actual merge,
verify the reconstructed merge tree, confirm #1635 and #1639 close, and delete
only this PR's local and remote branch. Keep #1636, #1637 and #1638 open.
Final completion evidence belongs in the PR receipt, not a rewrite of this
timestamped snapshot.

No all-record review completion or SSSOM/KGX readiness claim follows from this
publication. The broader active review goal remains incomplete.
