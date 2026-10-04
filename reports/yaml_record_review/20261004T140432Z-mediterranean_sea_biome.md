# YAML Record Review: mediterranean sea biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/mediterranean_sea_biome.yaml`
- Started UTC: 2026-10-04T13:57:42Z
- Finished UTC: 2026-10-04T14:04:32Z
- Verdict: needs curation

## Target

Complete generated `HabitatRecord`: ENVO:01000047, mediterranean sea biome,
AQUATIC, EXACT and SEEDED. It contains an ENVO definition, three PREGO
related synonyms, two ontology parents, one source attestation, 25 associated
taxa and one seed event. Parameters, citations, graphs, discussions, datasets,
xrefs, contributors and replacement links are not emitted.

The actual mint function reproduces decision key
`habitatmech:PREGO.803957665c`; PATHS.tsv:768 pins the filename. This is an
oceanographic biome type, not simply a named geographical sea or a climate.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/mediterranean_sea_biome.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/mediterranean_sea_biome.yaml` | PASS, one file, zero errors. |
| `just validate-products` | PASS: 1,179 canonical pairs, one synonym, five exceptions, 2,054 configured no-adapter skips. This does not check NCBITaxon names or biological occurrence. |
| `just worklist --status all --limit 5` | PASS: 953 ungrounded records and 1,810 decisions. Not an ITEM endorsement of this EXACT target. |
| `just qc` | Still running tests at report completion. Lint, documentation and raw provenance passed; no terminal result yet for tests or subsequent full-corpus history/schema, reproduction, site, redirects and term-request gates. |
| Source/reference checks | Full record, structured scan of all 14 raw TSVs, all 25 retained taxon rows, current OLS terms/typed graph and all NCBI taxon resolutions checked. Primary oceanographic article introduction, AMS definition and PREGO methods inspected. |

Whole-corpus-only checks use the documented runner. Later terminal results
belong in a publication receipt, not a rewrite of these timing observations.

## Identity and Grounding

Current [ENVO:01000047](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000047)
is active, with the same label and definition as the record and physical
`data/raw/ontology_terms.tsv:7556`. Its defining conditions concern enclosure,
restricted ocean exchange and density-driven circulation. AQUATIC and its
PREGO self-grounded identity are appropriate; SEEDED is not curated approval.

Both parents are genuine current ENVO subclass assertions, matching
`ontology_subclass_edges.tsv:5686-5687`, not accidental GOLD path edges.
[ENVO:00000447 marine biome](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000447)
is a defensible broader class. However,
[ENVO:01001833 mediterranean biome](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001833)
is defined by Mediterranean climatic conditions. Enclosed-sea circulation
does not establish that climatic restriction.

The inspected [AMS oceanographic definition](https://glossary.ametsoc.org/wiki/mediterranean-sea/)
distinguishes arid and humid types and includes Baltic and Indonesian examples.
The primary [Osterhus et al. 2019 article](https://os.copernicus.org/articles/15/379/2019/),
DOI:10.5194/os-15-379-2019, describes the Arctic Mediterranean's restricted
gateways and water-mass exchange in its introduction. These establish the
general oceanographic usage, not the sampled location of every PREGO pair.
The climatic parent conflates two meanings of mediterranean and over-restricts
the target's stated scope. Its presence in ENVO is provenance, not evidence
that the two definitions are logically compatible.

## Evidence

`data/raw/prego_habitats.tsv:49` gives 1,625 taxa, 1,629 direct assertions,
maximum score 4 and the two emitted channels. The record correctly uses
1,625 TAXON, not 1,629 specimens or studies. The source supplies the canonical
label plus the three related lexical variants. Current ENVO lists no synonym
for this term; the displayed variants are PREGO-owned, not ENVO synonyms.

All 25 rows at `prego_habitat_taxa.tsv:7500-7524` match emitted IDs, labels,
scores, ranks and pool size. The first 13 have score 4 and environmental_samples;
the remaining 12 have score 3 and annotated_genomes_isolates, with rank 23
also carrying environmental_samples. None has independent corroboration.
The record-level channel union must not be assigned to every pair.

Official [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=163503,168759,184592,216773,29805,40464,463619,55518,595452,60480,6334,69773,76775,1104565,1104566,1121404,1121937,1121948,1122607,2183988,2738566,419481,472759,491952,59919&retmode=xml)
resolves all 25 requested identifiers after accounting for one merge. All 21
nonempty record labels match current scientific names. Four unlabeled rows
resolve as follows:

| Retained ID | Current resolution |
| --- | --- |
| NCBITaxon:168759 | Nanomia bijuga. |
| NCBITaxon:184592 | NCBITaxon:240364, Chaetoceros neogracilis; the response explicitly lists 184592 in AkaTaxIds. |
| NCBITaxon:29805 | Pinus luchuensis. |
| NCBITaxon:6334 | Trichinella spiralis. |

A separate single-ID query confirmed the merged Chaetoceros mapping. The
legacy ID is resolvable, not a dead reference. Missing labels faithfully
reflect blank source-table cells; canonicalization/label recovery belongs
upstream, not in generated YAML. These taxonomy resolutions do not prove
habitat occurrence or justify deleting non-microbial environmental detections.

[PREGO methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC8879827/),
PMID:35208748, DOI:10.3390/microorganisms10020293, were inspected through
official Europe PMC full-text XML, sections 2.3, 2.4 and C.3. Environmental
associations can derive from taxonomic detections co-occurring with sample
metadata; scores are not abundance, viability or phenotype measurements.
No original pair-level sample evidence was inspected. The 25/1,625 truncation
is explicit, and no `is_characteristic` flag is asserted.

## Completeness

Ignored-inclusive ID, actual source-key, label and filename searches covered
curation, history, research, reports, PATHS and RETIRED. Only the pinned path
matched exact target searches: no target decision, authored term request,
causal overlay, dedicated research, session history or prior individual report
was found in those locations. A broader mediterranean search found nine
research files discussing other habitats, not target-owned evidence.

An ITEM scope/hierarchy review is consequential. Empty optional mechanisms,
parameters and citations should not be filled from unrelated regional studies.
No gene, regulator or expression dataset is asserted, so iModulonDB is not
applicable; transcriptomic membership would not resolve these findings.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | The general circulation-defined sea biome inherits from Mediterranean-climate biome ENVO:01001833, imposing an unsupported climatic restriction. | Upstream ENVO subclass assertion; governed ontology extraction feeding `data/raw/ontology_subclass_edges.tsv:5687`, consumed by `ConceptStore.get` at `src/habitatmech/seed.py:408`. |
| Minor | PREGO's apparently corrupted lexical variant mediterranean seal is emitted as a habitat synonym without inspected support. Its RELATED scope is preserved, but that does not establish a valid spelling. | PREGO source vocabulary/extraction and `seed.py:1064-1065`; a scoped maintained lexical correction, not a blanket synonym-scope downgrade. |
| Minor | One retained taxon uses merged ID 184592 and four rows have recoverable missing names. This is a non-blocking taxonomy/provenance refresh, not four invalid taxa or a broken link. | Versioned upstream taxonomy and PREGO pair inventory; `_load_taxon_labels` at `src/habitatmech/extract.py:650-665` only performs exact-ID label lookup. |

Counts: zero blockers, one major, two minor. No unsupported characteristic
phenotype or erroneous source-count claim was found.

## Recommended Edits

1. Correct the climatic superclass upstream and refresh the governed ontology
   inventory, or introduce an explicitly reviewed, scoped ontology-edge
   qualification contract. Preserve the valid marine-biome parent and generic
   oceanographic definition; do not silently narrow identity to one named sea.
2. Recover the original lexical provenance and correct/qualify the apparent
   seal typo while retaining the source observation and valid sea/seas forms.
3. Reconcile the merged taxon and recover labels through versioned taxonomy
   machinery. Preserve original IDs as provenance and recompute full-source
   deduplication/count/ranking if canonicalization collapses pairs; a top-25
   patch cannot establish the 1,625-taxon aggregate.
4. Add scoped regressions, append required curation history, and inspect guarded
   regeneration. Do not edit generated records/pages or frozen checksums.

## Follow-up Checks

Require current typed ontology/taxonomy verification, original lexical evidence,
schema, label correspondence, provenance/history, exact corpus reproduction and
full QC. The rendered page currently displays the climatic parent, seal variant
and four bare taxon IDs; inspected output is not independent source evidence.

Actual semantic-adapter comparisons with full corpus context show changed text
after removing the climatic parent, removing the typo, or filling the four
names. Those corrections require the real map/site rebuild tracked in #1217.
Changing only the unlabeled legacy taxon ID is text-neutral, so that narrow
operation must not automatically be described as blocked by #1217. Recheck
actual regenerated inputs and preserve protected draft #1218.

## Additional Notes

GitHub title/body/comment searches for mediterranean and 184592 returned no
issue. The full body of open #1249 was inspected: it concerns ontology synonym
scope inflation, not PREGO lexical spelling, and does not own this typo.
A taxon/label title search also found no issue; that is a bounded search,
not proof of absence throughout every issue body/comment.

Browser OLS access failed and PMC returned a browser challenge. Direct official
OLS/NCBI and Europe PMC XML succeeded. Physical ontology-term line 7556 differs
from logical TSV row 7550 because earlier quoted cells contain newlines; the
locator above was separately verified. No paid research, scientific edit,
status promotion, curation event or committed-history rewrite was performed.
