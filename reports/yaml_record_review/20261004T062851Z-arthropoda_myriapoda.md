# YAML Record Review: myriapod-associated environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/arthropoda_myriapoda.yaml`
- Started UTC: 2026-10-04T06:26:26Z
- Finished UTC: 2026-10-04T06:28:51Z
- Verdict: pass

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.2333d6225a`:
HOST_ASSOCIATED, UNGROUNDED, REVIEWED. It has a curated definition, one
source-label synonym, two broader environment parents, one GOLD attestation
with 569 ORGANISM assertions and three generated events. The actual `mint`
helper reproduces its ID from Host-associated > Arthropoda: Myriapoda.
`data/habitats/PATHS.tsv:1549` pins its source-label filename.

## Validation

- `just validate data/habitats/host_associated/arthropoda_myriapoda.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/arthropoda_myriapoda.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch `just qc` passed lint, documentation and raw provenance and
  remains in tests. No terminal local result is claimed at report completion.
  It includes the full-corpus history, reference/invariant, schema,
  reproduction, site, redirect and term-request checks.
- Exact unchanged base `0ab7aeb487d2fa90a66695740c3f5d3451e0b779` passed
  [post-push QC 37182485949](https://github.com/CultureBotAI/HabitatMech/actions/runs/37182485949).
  Its earlier merge-group QC passed 457 tests, with three skips and two
  warnings, plus exact corpus reproduction. These are baseline results,
  not this report's final-head CI.
- Current official OLS JSON, primary publisher text and PubMed EFetch XML
  were inspected. Browser retrieval for PMID:27597263 hit a challenge;
  its complete abstract and identifiers were instead read through EFetch.

## Identity and Grounding

`curation/decisions.tsv:296` is ITEM CONFIRM_UNGROUNDED under the
animal-associated environment. `curation/term_requests.tsv:11` supplies
the authored label, definition, source-label synonym and ADD-mode genus.
August 12 decision and August 16 definition/seed events match those inputs.
The single contributing source's ITEM decision explains REVIEWED.

The fresh batch check of non-obsolete
[ENVO:01001000](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001000)
and [ENVO:01001002](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001002)
agrees with vendored rows 8495/8497. Both organism-determined and
animal-associated environment are genuinely broader. Subclass row 6797
places the latter under the former. ADD retains the true source ancestor
alongside the authored genus without equating the narrower host category
to all animal environments.

The same current batch check of
[ENVO:01001176](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001176)
confirms its aquatic requirement. The terrestrial millipede examples below
exclude using it as a universal superclass or exact identity here.
Current [NCBITaxon:61985](https://www.ebi.ac.uk/ols4/api/ontologies/ncbitaxon/terms?obo_id=NCBITaxon%3A61985)
is active Myriapoda but denotes the taxon, not this environment. The full
ignored-inclusive vendored-slice search found no such taxon row; adding an
optional xref is not required to make this record valid.

The current ENVO search for myriapod associated environment returned zero
results; a bounded ignored-inclusive slice search found no matching class.
These searches do not prove absence under every possible synonym. The
record is not a synonym of one millipede species, a hindgut alone, surrounding
litter or soil, or the other arthropod host categories.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:65` provides the exact depth-two source
path, nodes 3369, 3549, 3632 and 3901, 569 organisms and zero study/biosample
assertions. First-node ID, four-node note, count/unit and label/path are
faithful. The 569 is neither a microbial species count nor independently
verified specimen-level evidence.

Full structured scans of 2,562 tree paths, 1,040 bulk biosample rows,
4,587 studies and 1,587 triads found 21 tree, two bulk, four study and zero
triad matches for the target key or myriapod/millipede/centipede wording.
Exact-path membership checks found no target path in the three side tables.
The bulk matches are Gut and Whole body, each with three biosamples; all
four study matches also refer to those children. The whole-body tree row
has zero assertions, showing why zero tree counts must not be generalized
to absence from every source product. Child counts and units stay separate.

The complete committed myriapod research report was read as a lead.
Its proposed template-artifact interpretation of some child paths is not
a fact asserted by this clade-level target. Neither child anatomy nor the
research report's unverified individual-GOLD-isolate inference is adopted
as evidence for the target's 569 organisms.

Inspected primary [Nardi et al. 2016](https://pubmed.ncbi.nlm.nih.gov/27597263/)
abstract and identifier metadata verify DOI:10.1016/j.asd.2016.08.007.
The abstract describes microbial communities along the digestive tracts
of Cambala speobia and Cylindroiulus caeruleocinctus, including adherent
hindgut communities with regional differences. These are bounded examples
of colonized terrestrial myriapod hosts, not proof of the same anatomy,
taxa or community in every myriapod.

Inspected [Nweze et al. 2024](https://www.nature.com/articles/s42003-024-06821-2)
abstract/results and PubMed metadata verify DOI:10.1038/s42003-024-06821-2,
PMID:39342029 and PMC11438867. Experiments on juvenile Epibolus pulchripes
and Glomeris connexa reduced microbial load and faecal production without
major effects on survival or weight; the authors question an essential
nutritional role for gut fermentation under those conditions. This limits
functional generalizations without denying the habitat. No measured pH,
taxon, fermentation mechanism or mutualistic necessity is imposed on the
whole myriapod class, and no paper counts are added to GOLD counts.

## Completeness

Ignored-inclusive identifier/label/stem searches covered curation, history,
research, prior reports, raw inventories, PATHS and RETIRED. They found the
maintained rows, generated ENVO template at row 17, research report and
label-change redirect at RETIRED row 29, but no exact-target prior review,
causal overlay or session history. No new event or history entry is required
for this read-only review.

All eight non-GOLD source tables were scanned: 162 BacDive sources,
3,081 BacDive taxa, 770 parameters, 358 mappings, 58 Madin habitats,
1,378 Madin taxa, 719 PREGO habitats and 8,807 PREGO taxa. None matched the
target key or the searched myriapod/millipede/centipede wording. This does
not rule out evidence under individual host names. The definition rationale's
general BacDive statement does not create a target-specific attestation.

Optional xrefs, parameters, taxa, evidence, mechanisms, discussions and
datasets can remain absent. iModulonDB is not applicable: the record makes
no gene, regulatory or expression assertion. External paper methods do not
by themselves create a record-level transcriptomics claim.

## Findings

None found: zero blocker, major or minor findings established.

## Recommended Edits

None. Preserve the host-environment identity, definition, source count/unit
and both broader parents. Future decision changes belong in
`curation/decisions.tsv`; definition/genus changes belong in
`curation/term_requests.tsv`. Keep generated YAML and pages read-only.

## Follow-up Checks

Require terminal batch QC and final-head/merge-queue checks before publication.
Future scientific changes need a guarded canary, strict validation, OAK,
corpus reproduction and site/map freshness. Any proposed external ontology
submission needs explicit per-request approval.

## Additional Notes

Searched all 502 existing issue titles, bodies and returned comments for
the exact key, label and Myriapoda wording; none matched. This bounded search
does not certify all descendants or all differently worded issues as sound.
No new issue or scientific correction is recommended. This is not an
independent PR approval.

No generated record, maintained input, status or history changed. No paid
research ran; reference reads add no coverage. Whole-corpus review remains
ongoing.
