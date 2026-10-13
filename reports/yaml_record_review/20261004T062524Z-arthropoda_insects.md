# YAML Record Review: insect-associated environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/arthropoda_insects.yaml`
- Started UTC: 2026-10-04T06:22:45Z
- Finished UTC: 2026-10-04T06:25:24Z
- Verdict: pass

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.dba2a83b95`:
HOST_ASSOCIATED, UNGROUNDED, REVIEWED. It has a curated definition, one exact
source-label synonym, two broader environment parents, one GOLD attestation
with 1,833 ORGANISM assertions, and three generated events. The actual
`mint` helper reproduces its key from Host-associated > Arthropoda: Insects.
`data/habitats/PATHS.tsv:2919` pins the source-label filename.

## Validation

- `just validate data/habitats/host_associated/arthropoda_insects.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/arthropoda_insects.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch `just qc` passed lint, documentation and raw provenance and
  remains in tests. No terminal result is claimed at report completion.
  It includes history, strict schema, reference/invariant tests, corpus
  reproduction, site, redirect and term-request validation.
- Exact unchanged base `0ab7aeb487d2fa90a66695740c3f5d3451e0b779` passed
  [merge-group QC 37182189628](https://github.com/CultureBotAI/HabitatMech/actions/runs/37182189628):
  457 passed, three skipped, two warnings, with exact corpus reproduction.
  The duplicate post-push QC is still running; neither run is this report's
  final-head CI.
- Official OLS JSON and the primary literature passages described below
  were inspected. PubMed browser retrieval was inconsistent for the
  caterpillar paper; its EFetch XML abstract and identifiers were read.

## Identity and Grounding

`curation/decisions.tsv:1215` is ITEM CONFIRM_UNGROUNDED under
ENVO:01001002. `curation/term_requests.tsv:7` supplies the authored label,
definition, source-label synonym and ADD-mode genus. The August 12 decision
and August 16 definition/seed events match those inputs. REVIEWED follows
the sole source concept's ITEM decision, not a claim of complete ecology.

Vendored rows 8495/8497 and current non-obsolete
[ENVO:01001000](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001000)
and [ENVO:01001002](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001002)
support organism-determined and animal-associated environment parentage.
Subclass row 6797 confirms their relationship. Both the inherited GOLD
Host-associated ancestor and the curated animal genus are genuinely broader;
ADD need not remove a true ancestor merely because it is implied.

Current [ENVO:01001176](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001176)
requires an aquatic context and cross-cuts insect hosts, including terrestrial
ones. It is not a replacement identity or a universal superclass here.
Current [NCBITaxon:50557](https://www.ebi.ac.uk/ols4/api/ontologies/ncbitaxon/terms?obo_id=NCBITaxon%3A50557)
is active Insecta, also present at vendored row 10755; it denotes the taxon,
not this host environment. A contextual xref is optional.

The current ENVO query for insect associated environment returned zero
results, and ignored-inclusive matching searches of the vendored slice
found no such class. These are bounded results, not exhaustive proof across
all possible terminology. The source bin remains distinct from the insect
gut alone, other arthropod categories, nests, hive products and insect food.
The research report's proposed Hexapoda expansion is not asserted by this
record and is not adopted without source evidence.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:26` records nodes 7073, 7181, 7182 and
7183, 1,833 organisms and zero study/biosample assertions on the exact
depth-two path. First-node ID, four-node note, label/path, count and unit
are faithful. The count is not richness, prevalence or a census of all
insect-associated microbes.

Full structured scans covered 2,562 tree paths, 1,040 bulk biosample rows,
4,587 studies and 1,587 triads. Insect wording matched 97 tree paths,
41 bulk rows, 153 studies and 42 triads. The host subtree contains 87 paths.
Exact-path comparisons, including membership in study path lists, found no
target path in the three side tables. The 742 gut, 94 larval and 60 whole-body
organism assertions are separate tree rows, not additions to the target count.

The complete committed insect definition-research report was read as a lead.
Its species counts, mechanisms, physicochemical generalizations and universal
colonization language are not independently adopted as record assertions.
Inspected primary [Yun et al. 2014](https://journals.asm.org/doi/10.1128/AEM.01226-14)
abstract and methods verify the DOI and describe 305 specimens from 218
species in 21 orders. Sampling included aquatic and terrestrial host
categories. Most DNA came from dissected guts; very small insects instead
used washed whole bodies. This supports a real insect-host context, not
uniform microbiota or equivalence of every body site.

Inspected primary [Hammer et al. 2017](https://pubmed.ncbi.nlm.nih.gov/28830993/)
abstract and identifier metadata verify DOI:10.1073/pnas.1707186114 and
PMC5594680. The study reports low-density, variable gut microbes in sampled
leaf-feeding caterpillars, largely lacking host-specific resident symbionts;
antibiotic suppression in Manduca sexta did not significantly affect the
tested growth/development/survival outcomes. This limits resident-microbiome
generalizations, but does not make an insect host cease to be an environment.
Neither paper's counts, taxa or mechanistic results are imported into GOLD's
1,833 assertions or this record.

## Completeness

Ignored-inclusive identifier/label/stem searches covered curation, history,
research, prior reports, raw inventories, PATHS and RETIRED. They found the
maintained inputs, generated ENVO template at row 9, research report and
label-change redirect at RETIRED row 28. Other reports discuss this parent,
but exact target-metadata coverage confirms no prior review of this record.
No target-specific causal overlay or session history was found in those
searched areas. A read-only review does not require a new curation event.

All eight non-GOLD source tables were scanned structurally. Target-key
matching and insect-word matching found no target attestation. The
mapping-only Insecta row at `isolation_source_groundings.tsv:163` names a taxon
but lacks a matching BacDive source occurrence in the 162-source inventory.
One Madin taxon-name hit belongs to ectothermic hosts; three PREGO taxon-name
hits belong to other habitat IDs. Their insecticola epithets are not
evidence for this target. Parameters and the other habitat/source tables
supply no matching row under these bounded searches.

Optional xrefs, parameters, taxa, evidence, mechanisms, discussions and
datasets need not be filled. iModulonDB is not applicable: this record makes
no gene, regulatory or expression claim.

## Findings

None found: zero blocker, major or minor findings established.

## Recommended Edits

None. Preserve the minted identity, both broader parents, definition and
source count/unit. Future grounding fixes belong in `curation/decisions.tsv`;
definition/genus changes belong in `curation/term_requests.tsv`. Do not
hand-edit generated records or infer a new source attestation from a
taxon-mapping table.

## Follow-up Checks

Require terminal batch QC and final-head/merge-queue checks before publication.
Any future scientific change needs a guarded canary, strict validation, OAK,
corpus reproduction and site/map freshness. An external ENVO submission
requires its own explicit approval.

## Additional Notes

All 502 existing issue titles, bodies and returned comments were searched
for the target key, filename and label. Open #280 concerns Metasoma/Gaster;
closed #276 concerns insect life-stage treatment. Both bodies were inspected
and neither establishes a defect in this clade-level record. No new issue
or scientific correction is recommended. This is a record review, not
independent PR approval.

No generated record, maintained curation input, status or history changed.
No paid research ran; reference reads add no coverage. Whole-corpus review
remains ongoing.
