# YAML Record Review: Endotracheal Fluid

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/clinical/tracheal_aspirate.yaml`
- Started UTC: 2026-10-07T02:52:34Z
- Finished UTC: 2026-10-07T02:55:11Z
- Verdict: pass

## Target

Read the entire generated HabitatRecord and rendered page at
`ec95a7191a9b6c9ddaa404c2062f7be9932623a9`: NCIT:C171504 Endotracheal Fluid,
CLINICAL, CLOSE/REVIEWED. One BacDive attestation reports three STRAIN;
one genus-level association represents the complete one-taxon inventory pool.
It carries one source synonym, one ontology parent and two events. Definition,
xrefs, environmental parameters, literature evidence, graphs, discussion and
datasets are absent. This is collected respiratory fluid, not the aspiration
procedure or the trachea as an anatomical organ.

## Validation

- Fresh `UV_CACHE_DIR=build/uv-cache just validate data/habitats/clinical/tracheal_aspirate.yaml`:
  pass, no issues.
- Fresh `just validate-strict` with the same cache and target: one file,
  zero errors; only ignored diagnostic output refreshed.
- Fresh full `seed.build_corpus()` / `seed.build_document()` equality:
  all fields match; one source, one reviewed source, one taxon, two events.
- Fresh all-14-inventory scan, official NCI identity/parent/synonym checks
  and NCBI taxon verification completed successfully.
- Reuse the complete QC receipt on the current merged scientific baseline:
  all 13 local gates passed; 503 tests passed, three skipped, two dependency
  warnings; 119 histories, 3,206 strict records, 32 overlays, provenance,
  floor, reproduction, site, redirects and term requests passed. Exact-candidate
  [QC 37562477062](https://github.com/CultureBotAI/HabitatMech/actions/runs/37562477062)
  and [label correspondence 37562476998](https://github.com/CultureBotAI/HabitatMech/actions/runs/37562476998)
  passed. Full QC/OAK were not repeated for this report. Direct NCI/NCBI checks,
  not assumed OAK coverage, establish the external identifier correspondences.
- No browser visual QA or original BacDive dump re-extraction.

## Identity and Grounding

Official NCI EVS REST release 26.09d defines
[C171504 Endotracheal Fluid](https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C171504?include=full)
by fluid collected from the tracheal lumen. NCI includes Endotracheal Aspirate
Fluid and ETA Fluid; its CDISC synonyms include Tracheal Aspirate and Tracheal
Aspirate Fluid. Thus the source label and retained source-attributed synonym
are supported, not a misleading lexical substitution for an unrelated term.

Its direct parent is
[C204466 Body Fluid Specimen](https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C204466?include=full),
defined as a biospecimen consisting of body fluid and placed under Biospecimen.
That is a true broader material class. The specimen role does not by itself
make fluid incapable of carrying microorganisms or force NOT_APPLICABLE.
Unlike a site-unspecified collection-method category, this source names both
a material and its anatomical origin.

The medium-confidence upstream synonym mapping uses skos:closeMatch.
`curation/decisions.tsv:1550` supplies an ITEM-level REVIEW for
habitatmech:BACDIVE.b266a9b90c. Its note says cohort review, but the maintained
depth is ITEM; the one-source REVIEWED result follows the actual table.
CLOSE and its source predicate are faithfully retained, without upgrading
the source assertion to exact equivalence. CLINICAL is appropriate to the
recorded sampling context. `PATHS.tsv:988` pins the stem; `RETIRED.tsv:237`
preserves the former tracheal-aspirate URL.

## Evidence

Fresh exact-field/pipe-member scan found target contributions in five of
14 inventories; the other nine had no exact target key. The parent was also
checked explicitly.

| Input, physical line | Verified contribution |
| --- | --- |
| `bacdive_isolation_sources.tsv:152` | Exact source ID/label, three strains, one taxon |
| `bacdive_source_taxa.tsv:2862` | Acinetobacter, NCBITaxon:469, count 3, rank 1, no corroboration |
| `isolation_source_groundings.tsv:322` | C171504/Endotracheal Fluid, closeMatch, ols4_search_synonym, 2026-05-01 |
| `ontology_terms.tsv:10791` | Exact identity label, no local definition/synonyms |
| `ontology_subclass_edges.tsv:9078` | C171504 to C204466 |
| `ontology_terms.tsv:10800`; `ontology_subclass_edges.tsv:9085` | Body Fluid Specimen label and Biospecimen superclass |

Fresh [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=469&retmode=xml)
resolves 469 directly to Acinetobacter, rank genus, with no alias or label
mismatch. The sole row is not a claim that the genus is the entire airway
microbiome, that all species occur, or that the isolates caused infection.
No `is_characteristic` flag, independent corroboration or literature claim
is present. Three source-linked strains are not three patients or studies.

Live [BacDive 8100](https://bacdive.dsmz.de/strain/8100), DSM 9308 / Tr III-74,
records endotracheal aspirate as its sample and places it under Host Body
Product / Oral cavity and Airways / Tracheal aspirate. This directly supports
the material/site interpretation of the category. It is an illustrative
source record, not a verified match to each member of the original three-strain
extraction. Its culture media and temperature are not habitat measurements.

Inspected official PubMed metadata and the complete abstract for
[McGinniss et al. 2024](https://pubmed.ncbi.nlm.nih.gov/38211701/),
DOI:10.1016/j.chest.2024.01.007. The paired molecular-profiling study of 13
intubated patients compared standard aspirates with samples obtained through
newly placed tracheostomy tubes and found concordant bacterial profiles in
that cohort. It explicitly considers established tube/suction-catheter biofilms
as a possible sampling influence. This supports microbiological use of the
fluid, not universal interchangeability of sample types or independent proof
of these three BacDive isolates. No patient result, numerical parameter or
causal relation is transferred into the record.

## Completeness

Ignored-inclusive ID, mint, label, source ID and slug searches across curation,
history, conf, docs, tests, PATHS and RETIRED found the decision and path history.
Own-name filename searches across curation/history/research found no
target-owned term request, overlay, research report or session in those
locations. The original BacDive nodes/edges dumps were not found by the
ignored-inclusive build/configured-kg-microbe-data search in this clinical
review session. The original three-isolate crosswalk remains unverified.

The missing definition reflects the governed ontology slice and does not
prevent identification using the inspected authoritative definition. No new
term request is needed for this already named material. Optional parameters,
literature and mechanism fields should not be filled from general clinical
expectations. Neither this record nor the inspected 16S profiling example
supplies a named transcriptomic component requiring iModulonDB.

## Findings

None found: zero blockers, zero major, zero minor findings. Identity, source
synonym, broader parent, conservative mapping, status and bounded association
agree with the inspected evidence. Passing this record does not certify the
unreconstructed original isolate-level links or a universal airway community.

## Recommended Edits

No corrective edit is established. Preserve the fluid/material distinction,
source count/unit, genus-level observation, predicate, category and history.
An optional definition refresh belongs to versioned ontology inputs and the
extractor. A future species-level refinement requires actual source strain
identity evidence; do not infer a species from a single illustrative page.

## Follow-up Checks

For future enrichment, recover the original three-strain crosswalk and source
version, verify counts and taxonomy, canary/reproduce the target and compare
all records. Check provenance, history, closed schema, source-predicate
preservation, semantic-input impact, applicable map/site updates, redirects,
OAK and full QC. Do not merge this fluid with an anatomical trachea, a sampling
procedure, a catheter biofilm or bronchoalveolar lavage merely because a study
compared their microbial profiles.

## Additional Notes

The PubMed browser response had no useful article body; official XML supplied
the inspected abstract and stable PMID/DOI metadata. No scientific changes,
new curation events, generation, paid research, author contact or GitHub
mutation occurred. Only this new report was written for this target.
