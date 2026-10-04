# YAML Record Review: Anterior chamber

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/anterior_chamber.yaml`
- Started UTC: 2026-10-04T02:06:08Z
- Finished UTC: 2026-10-04T02:09:59Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.53e4290463`:
HOST_ASSOCIATED, NARROW, REVIEWED. It has two parents, one uncounted GOLD
attestation and two events. The source is Crustaceans > Digestive system >
Hindgut > Anterior chamber, not an eye space or an insect anterior region.
The actual `mint` helper reproduces its identifier; `PATHS.tsv:1901` pins
the current filename. `RETIRED.tsv:18` retains the former erroneous
eye-term URL for the same source concept, not a new anatomical equivalence.

## Validation

- `just validate data/habitats/host_associated/anterior_chamber.yaml`: passed.
- `just validate-strict data/habitats/host_associated/anterior_chamber.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch QC remains running; lint, documentation and raw provenance
  passed and tests are progressing. No terminal QC success is claimed yet.
- Current official OLS terms and PubMed EFetch abstract were inspected
  successfully. OLS browser access failed earlier in the batch; successful
  direct responses, not those failures, support the ontology checks.

## Identity and Grounding

`curation/decisions.tsv:1682` supplies ITEM GROUND_AS_PARENT to BTO:0000510.
The seeder correctly reproduces NARROW, REVIEWED, skos:narrowMatch and both
August 16 events. That faithful status/history does not validate the decision.

The decision correctly rejected
[UBERON:0001766, anterior chamber of eyeball](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001766).
Its current non-obsolete definition and vendored `ontology_terms.tsv:13070`
describe an eye space, not the GOLD hindgut compartment. Do not restore this
older lexical misgrounding merely because the leaf label matches.

The replacement [BTO:0000510](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0000510)
is also unsupported: current OLS and vendored line 511 explicitly restrict
it to vertebrate embryonic hindgut. A crustacean compartment cannot be a
subtype of that taxonomically and developmentally restricted structure.
The term is non-obsolete; this is a scope error, not an obsolete-ID error.

The complete referenced `hindgut__afd87e04.yaml` identifies the second
parent, `habitatmech:GOLD.19840c718e`, as whole crustacean Hindgut, NARROW
beneath [UBERON:0001046](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001046).
Current OLS and vendored line 13003 describe the caudalmost digestive-tract
subdivision. This source has no authored compartment-environment definition.
Removing BTO alone would leave a separate whole-organ is-a claim in place.

A scoped current OLS query for anterior chamber hindgut across BTO, UBERON,
ENVO and AISM returned zero candidates. This does not prove universal absence
or justify adopting an adjacent term. Historical #12 remains an open general
backlog; its old counts and claims of screen coverage are not current
scientific evidence for either parent.

## Evidence

`gold_ecosystem_paths.tsv:1760` supplies the exact five-level source path,
node 7325, one source node and zero organism/study/biosample assertions.
The generated label, full path and source ID are faithful; no positive count
should be invented. The whole-hindgut parent's one ORGANISM assertion is
not an assertion about this compartment.

Complete scans of 2,562 tree paths, 1,040 bulk rows, 4,587 studies and 1,587
triads find only that tree row for anterior-chamber wording. No exact target
path has a bulk, study or triad attestation. This is bounded source absence,
not proof that the anatomical compartment cannot contain microorganisms.

The primary abstract of [Bogataj et al. 2018](https://pubmed.ncbi.nlm.nih.gov/30564048/)
directly distinguishes the anterior chamber and papillate region of an isopod
hindgut and compares their ultrastructure. PubMed's primary ArticleIdList
verifies PMID:30564048 and DOI:10.3897/zookeys.801.22395. It positively
supports the compartment-versus-whole distinction; no universal crustacean
scope, microbial mechanism or GOLD sample identity is inferred from it.
Only the abstract was inspected, not the full experimental methods.

The source-parent edge arises separately at `src/habitatmech/seed.py:898-907`.
The strict broader/is-a contract applies to that contribution as well as the
curated ontology parent. A GOLD breadcrumb cannot substitute for subsumption.

## Completeness

Ignored-inclusive source/parent IDs, label and filename searches covered
curation, history, research, prior reviews, PATHS, RETIRED and raw inventories.
They located the ITEM row and retired URL but no target definition, overlay,
session record or earlier exact-target review. The matching passage in the
neighboring crustacean research report lists the source path; that passage
is a lead, not independent anatomy evidence. Missing later-style history for
an older decision is not a defect.

Full scans of 162 BacDive sources, 3,081 BacDive taxa, 770 parameters,
358 mappings, 58 Madin habitats, 1,378 Madin taxa, 719 PREGO habitats and
8,807 PREGO taxa found no anterior-chamber wording. Generic hindgut or eye
data are not imported into this record. Empty optional taxa, parameters and
graphs are not findings. iModulonDB is not applicable because no gene,
regulator or expression-module claim is supplied.

## Findings

1. **Major - HM-ANTERIOR-CHAMBER-001:** the ITEM decision assigns a vertebrate
   embryonic hindgut parent to a crustacean compartment. Owner:
   `curation/decisions.tsv:1682`. Filed as
   [#1332](https://github.com/CultureBotAI/HabitatMech/issues/1332).
2. **Major - HM-ANTERIOR-CHAMBER-002:** the independent GOLD source parent
   makes this compartment a subtype of a whole hindgut. Owner:
   `src/habitatmech/seed.py:898-907` or a governed source-specific exclusion.
   Added as a second witness to
   [#1331](https://github.com/CultureBotAI/HabitatMech/issues/1331).

No blocker or minor finding established. The minted source identity and
rejection of the former eye-space grounding remain sound.

## Recommended Edits

Re-decide the BTO grounding at ITEM depth, using a verified anatomical-region
genus or retaining an ungrounded minted habitat if none fits. Independently
correct or exclude the whole-hindgut source parent. Do not substitute
UBERON:0001046 as a quick broader match: removing the vertebrate restriction
does not resolve the compartment/whole distinction.

Preserve source path/node, intended status and the historical URL. Do not
hand-edit generated YAML or use an equivalence xref for containment. Read-only
copies through the actual semantic adapter confirm that removing either
parent, or both, changes the input despite their similar displayed names.
Append required history, inspect a guarded canary and use supported map/site
regeneration; #1217 remains relevant and draft #1218 is not on main.

## Follow-up Checks

Regress both parent contributors independently and verify that neither wrong
edge survives the other correction. Check source identity, absent positive
count, intended status, full ancestry, strict schema, OAK, history, corpus
reproduction, map/site/redirect freshness and full QC.

## Additional Notes

All 487 existing issue bodies and returned comments were searched for the
target/source-parent keys, BTO:0000510 and anterior-chamber wording. #1331
covered the adjacent source-parent mechanism but not this maintained ITEM
decision. The BTO repair was filed separately and the source-parent witness
was deduplicated into #1331. No scientific input, generated record or history
changed; no paid research ran. Parent reads do not add to review coverage.
