# YAML Record Review: area of moss-dominated vegetation

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/area_of_moss_dominated_vegetation.yaml`
- Started UTC: 2026-10-04T04:16:11Z
- Finished UTC: 2026-10-04T04:23:21Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord `ENVO:01000890`, HOST_ASSOCIATED,
CLOSE, REVIEWED: definition, one synonym, two parents, two attestations,
25 taxa and three history events. `PATHS.tsv:861` pins the slug. Actual
`mint` reproduces `habitatmech:BACDIVE.6946e653a5` from the BacDive source
ID, not its display label, and `habitatmech:GOLD.82644ed4d2` from the GOLD
path. The two ITEM REVIEW decisions are at `curation/decisions.tsv:43,769`.

## Validation

- `just validate data/habitats/host_associated/area_of_moss_dominated_vegetation.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/area_of_moss_dominated_vegetation.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Reused the immediately preceding full local `just qc` on identical tree
  `5454cf514ce031807b6647dc393b1974c7aee257`: 457 passed, three skipped,
  two dependency warnings, 87 history records, 3,206 strict records,
  32 overlays and corpus/site/redirect checks passed. No scientific files
  changed. Post-merge QC run 37176047075 also completed successfully.
  This is not a claim of another fresh full local run for this record.
- Current official OLS JSON, NCBI taxonomy and primary EFetch retrievals
  succeeded. A later browser OLS request failed; direct official JSON
  reconfirmed the definition. Publisher abstract and BacDive sources opened.

## Identity and Grounding

Current non-obsolete [ENVO:01000890](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000890)
matches vendored row 8385: a planetary area with moss ground cover and its
atmospheric column. Its NLCD annotation explicitly does not strictly assert
the coverage threshold; neither an Alaska-only restriction nor an 80-percent
threshold is needed for this finding. The current typed graph and local
subclass row 6676 identify [ENVO:01001305](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001305),
vegetated area, as a superclass; vendored row 8799 agrees.

This landscape identity is not the host-associated source concept. CLOSE
does not prevent merging by the ontology identifier. The exact Moss synonym,
HOST_ASSOCIATED category and host-source parent are manifestations of that
one identity mismatch, not three separately counted defects. The complete
`bryophytes.yaml` reference record, `habitatmech:GOLD.35beb98884`, is a
CLASS-swept, UNGROUNDED/SEEDED host context, not an authored landscape genus.

Both source resolutions can consume upstream mapping row 206 through
`resolve_bacdive` and `resolve_gold` in `src/habitatmech/seed.py`. Thus two
attestations do not independently confirm this lexical closeMatch. ITEM
REVIEW at rows 43 and 769 endorses the result; generated REVIEWED and the
two August 13 events faithfully reflect those decisions, but do not make
the identity scientifically valid.

## Evidence

`bacdive_isolation_sources.tsv:89` preserves Moss, 59 STRAIN assertions and
39 candidate taxa. GOLD tree row 2508 preserves nodes 8110/8111, collapsed
to `Host-associated > Plants > Bryophytes > Moss`, with zero organism,
study, biosample and total assertions. Omitted GOLD count/unit is expected.
Seven subsequent GOLD rows distinguish plant structures or life stages.

Full structured scans covered 162 BacDive sources, 3,081 BacDive taxon rows,
358 mappings, 2,562 GOLD tree paths, 1,040 bulk rows, 4,587 study rows and
1,587 triads. No exact target bulk/study/triad support was found. Separate
Peat moss entries include 11 tree organism assertions, 732 bulk biosamples
and five study rows; these are not this source or comparable count units.

All 25 emitted taxa match raw rows 1913-1937 in identifier, label,
association count, rank, source and pool size. Current NCBI checks verified
all 25 names/IDs, including the two strain-level IDs and generic species
labels. No corroboration or `is_characteristic` assertion is made. A
source-bin association does not prove occurrence throughout a landscape.

[BacDive 1979](https://bacdive.dsmz.de/strain/1979) identifies A3 / DSM 23488 /
LMG 23650 / CCUG 53006 from Aulacomnium palustre. The inspected
[primary abstract, PMID:17911288](https://pubmed.ncbi.nlm.nih.gov/17911288/),
DOI:10.1099/ijs.0.65142-0, supports moss gametophyte isolation and the type
strain aliases. Its former Burkholderia names are not evidence that current
Paraburkholderia identifiers are wrong; the abstract also mentions soil
isolates, so exclusivity to moss is not asserted.

Two retained taxa expose why a narrow moss-host replacement cannot absorb
the whole bin. [BacDive 131388](https://bacdive.dsmz.de/strain/131388) records
NCBITaxon:1619309, R33 / DSM 29849 / CGMCC 1.15042, Moss-tagged but isolated
from Herbertus sendtneri. [PMID:26155771](https://pubmed.ncbi.nlm.nih.gov/26155771/),
DOI:10.1007/s10482-015-0514-3, verifies that host and those aliases.
[BacDive 132390](https://bacdive.dsmz.de/strain/132390) records
NCBITaxon:1619310, R55 / DSM 29850 / CGMCC 1.15043, also Moss-tagged but
explicitly from surface-disinfected liverwort Herbertus sendtneri. The
inspected [primary abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.000789),
PMID:26597860, confirms the liverwort and strain aliases. Primary
PubmedData ArticleIdList entries verified all three PMID/DOI pairs.
These exact-strain witnesses do not prove species-wide host exclusivity.
Only abstracts and relevant BacDive source fields are relied on, not
uninspected full-paper methods or unrelated physiological measurements.

## Completeness

Ignored-inclusive searches for both source keys, ontology ID, label, slug
and moss-associated variants covered curation, history, research, prior
reviews, raw inputs, PATHS and RETIRED. No target definition request,
overlay, session, research report or earlier target review was found.
Peat-moss decision/definition and research passages are a separate near
miss, not an exact target or an excuse to merge general moss with Sphagnum.
Only relevant passages of that research report were inspected.

Full scans of 770 parameter rows, 58 Madin habitats and 1,378 Madin taxa,
719 PREGO habitats and 8,807 PREGO taxa found no target-key or whole-word
moss match. These are bounded inventory negatives, not biological absence.
Optional parameters, evidence graphs and datasets are not quotas.
iModulonDB is not applicable: no gene, regulator or expression-module claim.
A fitting replacement ontology identity is not established by this review.

## Findings

1. **Blocker - HM-MOSS-IDENTITY-001:** host-source concepts are represented
   by a landscape-area identity. Maintained owners: the two ITEM decisions
   in `curation/decisions.tsv`, with any supported minted definitions in
   `curation/term_requests.tsv`. Filed as
   [#1346](https://github.com/CultureBotAI/HabitatMech/issues/1346).

No separate major or minor finding established. The liverwort witnesses
constrain the identity repair; they are not counted as another finding.

## Recommended Edits

Re-decide both keys independently. Reject the landscape identity without
calling real host habitats NOT_APPLICABLE. Resolve the GOLD moss-host scope
separately from the broader/noisy BacDive bin, preserving raw evidence;
do not transfer all 59 strains into a moss-only definition. Verify suitable
associated-environment terms or author supported minted definitions, not
whole-host taxonomy identities. Audit descendants, source parents, exact
synonyms and URL continuity before splitting or merging anything.

A real semantic-adapter comparison shows that removing even the landscape
parent changes the input. Parent removal alone does not fix the identity.
Append required history, inspect canaries and regenerate all affected
corpus/map/site/redirect products through supported tools; #1217 remains a
dependency. No generated file, freshness hash or runtime pin should be patched.

## Follow-up Checks

Regress source-specific identity, host scope, all source IDs/counts and
retained taxa. Run strict validation, OAK, full ancestry and corpus checks,
history, provenance, term-request/redirect/site freshness and full QC.
Inspect actual regenerated source allocation, not just a new label.

## Additional Notes

All 498 existing issue bodies and returned comments were searched before
filing; no duplicate identity issue matched. No science inputs, generated
records/pages or history changed, and no paid research ran. Parent and
strain reference reads are not additional completed record reviews.
