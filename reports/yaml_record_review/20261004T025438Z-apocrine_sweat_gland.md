# YAML Record Review: apocrine sweat gland

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/apocrine_sweat_gland.yaml`
- Started UTC: 2026-10-04T02:51:37Z
- Finished UTC: 2026-10-04T02:54:38Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `BTO:0001458`: HOST_ASSOCIATED,
EXACT, REVIEWED. It has a BTO definition, one GOLD plural synonym, three
parents, one uncounted GOLD attestation and two generated events. Its source
is Human > Integumentary system > Apocrine sweat glands, not its Sweat child,
an apoeccrine gland or a generic gland secretion. The actual `mint` helper
reproduces source key `habitatmech:GOLD.f3c6dc4883`; `PATHS.tsv:271` pins it.

## Validation

- `just validate data/habitats/host_associated/apocrine_sweat_gland.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/apocrine_sweat_gland.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch QC remains running. Lint, documentation, raw provenance,
  457 tests (three skipped, two dependency warnings) and 85 history records
  passed; strict corpus validation and later gates are not yet terminal.
- Direct official OLS and primary PubMed EFetch requests succeeded; browser
  OLS failed. Only successful inspected sources support the conclusions.

## Identity and Grounding

Current [BTO:0001458](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0001458)
is non-obsolete and matches vendored row 1458 on label and definition.
The human source fits this gland identity. `curation/decisions.tsv:1346`
grounds it at ITEM depth; the exact mapping, plural synonym, REVIEWED status
and August 12/16 events are faithfully generated.

The current [BTO graph](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FBTO_0001458/graph)
asserts subClassOf BTO:0001162 apocrine gland and BTO:0001331 sweat gland,
matching vendored edges 1002/1003. Both parent terms were separately checked
as non-obsolete, with definitions agreeing with rows 1163/1332. These are
gland classifications, not claims that the gland is a whole organ system.

Current [UBERON:0000382](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000382)
independently describes the coiled gland and hair-follicle duct, matching
vendored row 12934. Its graph supplies sweat-gland and skin-apocrine-gland
superclasses, consistent with local edges 11049/11050. A second ontology's
matching concept does not by itself require changing the valid BTO identity.

The complete `integumentary_system__2442c03e.yaml` identifies the extra
parent, `habitatmech:GOLD.dc86c8917c`, as whole human Integumentary system,
NARROW beneath UBERON:0002416. That term was independently checked in this
batch as a non-obsolete connected anatomical system, not a gland class.
The local parent has no authored gland-associated-environment definition.
A gland belonging to a system is not a subtype of the whole system.

## Evidence

`gold_ecosystem_paths.tsv:2254` provides the exact four-level human path,
nodes 6863/6867 and zero organism, study and biosample assertions. The
generated first ID, two-node note, path, label and absent positive count
are faithful. Row 2255 is the distinct Sweat child, node 6864; its location
does not make a secretion and a gland equivalent.

Complete scans of 2,562 tree paths, 1,040 bulk rows, 4,587 studies and
1,587 triads found only those two tree rows for apocrine wording and the
target identifiers. There is no target bulk, study or triad attestation in
those complete tables. Source-node multiplicity does not count specimens.

Three inspected primary abstracts put the inherited description in context:

- [Schaumburg-Lever and Lever 1975](https://pubmed.ncbi.nlm.nih.gov/1110304/),
  DOI:10.1111/1523-1747.ep12540893, observed multiple secretion modes,
  including apocrine, in human apocrine glands.
- [Stoeckelhuber et al. 2011](https://pubmed.ncbi.nlm.nih.gov/21154231/),
  DOI:10.14670/HH-26.177, studied the apical-release process in human axillary
  glands. This does not imply that every secretion uses only one mechanism.
- [Natsch et al. 2003](https://pubmed.ncbi.nlm.nih.gov/12468539/),
  DOI:10.1074/jbc.M210142200, experimentally linked axillary bacterial
  activity to odorant release. It does not make the tested organisms universal
  gland residents or prove a causal edge for every anatomical location.

Primary ArticleIdList entries verified those PMIDs/DOIs. Only abstracts
were inspected; no taxa, genes or new mechanism edges are imported.

## Completeness

Ignored-inclusive target/source/parent keys, label and filename searches
covered curation, history, research, prior reviews, raw inventories, PATHS
and RETIRED. They found the ITEM row but no target definition request,
overlay, session file or earlier exact-target review. Cerumen research and
other integumentary-target reviews are different subjects, not new reviews
of this gland. Missing later-style history for an old decision is not a defect.

Full scans of 162 BacDive sources, 3,081 BacDive taxa, 770 parameters,
358 mappings, 58 Madin habitats, 1,378 Madin taxa, 719 PREGO habitats and
8,807 PREGO taxa found no apocrine wording or target-key match. This is a
bounded inventory result. Optional parameters, taxa and graphs are not
quotas; iModulonDB is not applicable because no microbial gene or expression
claim is being assessed or adopted from the separate literature leads.

## Findings

1. **Major - HM-APOCRINE-001:** the gland inherits a whole human
   integumentary-system superclass from source nesting. Owner:
   `src/habitatmech/seed.py:898-907` or a governed source-specific exclusion.
   Added as a second witness to
   [#1337](https://github.com/CultureBotAI/HabitatMech/issues/1337).

No blocker or minor finding established. The two BTO gland parents,
anatomical identity and faithful source/status representation are supported.

## Recommended Edits

Correct or exclude only the false whole-system source-parent contribution.
Retain BTO:0001458, BTO:0001162 and BTO:0001331, both source nodes,
definition provenance and intended review status. Do not globally remove
GOLD parents, encode part-of as an equivalence xref or hand-edit generated YAML.

A read-only copy through the real semantic adapter confirms that removing
the GOLD parent drops Integumentary system and changes the input. Append
required history, inspect a guarded canary and use supported map/site
regeneration. #1217 remains relevant and draft #1218 remains separate.

## Follow-up Checks

Regress the exact GOLD edge independently from the two valid ontology
parents. Preserve source fields, absent positive counts and intended
EXACT/REVIEWED states. Check complete ancestry, strict schema, OAK, history,
corpus reproduction, semantic/site/redirect freshness and full QC.

## Additional Notes

All 492 existing issue bodies and returned comments were searched for the
target/source-parent keys, apocrine wording and whole-system-superclass
mechanism. #1337 already owns the maintained rule defect; the separate
human-gland witness was added without a duplicate issue. The parent was
read as a reference only. No scientific input, generated record or history
changed; no paid research ran.
