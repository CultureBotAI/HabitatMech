# YAML Record Review: xeric basin biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/xeric_basin_biome.yaml`
- Started UTC: 2026-10-07T02:05:04Z
- Finished UTC: 2026-10-07T02:08:42Z
- Verdict: pass with minor issues

## Target

Read the entire generated HabitatRecord and rendered page at
`1c066989c30b8bd885361fe836de49d8cc71a36c`: ENVO:00000893, xeric basin biome,
AQUATIC, EXACT/SEEDED. It contains an ENVO definition, one freshwater-biome
parent, two PREGO related synonyms, one PREGO attestation, 25 observational taxa
and one seed event. It asserts no xrefs, parameters, literature evidence,
mechanism graph, discussion or dataset. Dry climate does not itself make this
freshwater biogeographic class a terrestrial-soil habitat.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/aquatic/xeric_basin_biome.yaml`:
  pass, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/aquatic/xeric_basin_biome.yaml`:
  one file, zero errors; only ignored diagnostic output refreshed.
- Full `seed.build_corpus()`/`seed.build_document()` parsed equality: pass,
  one source concept, zero reviewed sources, 25 taxa, one event.
- Fresh actual PREGO resolution/category, all-14-inventory scan, official typed
  ENVO and all-25-ID NCBI Taxonomy checks completed.
- Reused the immediately preceding complete QC/OAK receipt on this merged
  scientific baseline: all 13 local gates passed; 503 tests passed, three
  skipped, two dependency warnings; 119 histories, 3,206 strict records,
  32 overlays, provenance, floor, corpus, site, redirects and term requests
  passed. OAK: 1,178 canonical, one synonym, five accepted exceptions,
  2,055 no-adapter skips, no failures. Exact merged-candidate
  [QC 37559411521](https://github.com/CultureBotAI/HabitatMech/actions/runs/37559411521)
  passed. Full QC/OAK were not repeated solely for this report; OAK does not
  validate these taxon names.
- Fresh git comparison verifies the guidance, generators, schema, raw inputs
  and this target were unchanged by the intervening wood-fall publication.
  No browser visual QA or original PREGO dump re-extraction.

## Identity and Grounding

Official typed ENVO revision
[`a2455d1a77e46bb8a664d65a157166b539269042`](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl),
106,817 triples, confirms active ENVO:00000893, the exact label/definition,
no typed synonyms and sole named parent ENVO:00000873 freshwater biome.
The latter is active and an aquatic-biome descendant. The two emitted synonyms
come from PREGO, not ontology exact-synonym axioms; their RELATED scope is honest.
The source's case-only label variant is correctly omitted as redundant.

Executed route for habitatmech:PREGO.f3891203f1: prego_self_grounded,
EXACT, no decision, reviewed False, no mapping predicate, category AQUATIC.
SEEDED is therefore correct. PREGO already uses the ontology identifier;
omitting a separate cross-vocabulary mapping predicate is not missing evidence.
`PATHS.tsv:605` pins the target filename.

## Evidence

Fresh exact-field/pipe-member scan of all 14 inventories found direct target
contributions in four files; the other ten had none.

| Input, physical line | Verified contribution |
| --- | --- |
| `ontology_terms.tsv:7159` | Logical row 7153, exact definition/label, active flag, directly referenced |
| `ontology_subclass_edges.tsv:5255` | Target to freshwater biome |
| `prego_habitats.tsv:247` | 36 taxa, 36 direct assertions, maximum score 4, environmental_samples, three source synonyms |
| `prego_habitat_taxa.tsv:5288` through line 5312 | All 25 emitted IDs/ranks/scores; TRUE direct flags; no corroboration |

The generator faithfully keeps 25 of 36 candidates. All scores are tied at 4;
`extract_prego` orders by score, direct flag and taxon CURIE, so different ranks
here do not establish different ecological strength. Counts are taxa, not
samples or independent studies; 4 is a source score, not a probability or
prevalence. No entry is marked characteristic or literature-confirmed.

Fresh [NCBI Taxonomy efetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=112248,1399,194373,196162,199684,231024,266940,28034,28115,29290,29346,29355,29539,330214,34073,36987,379066,39946,411485,428125,44576,45465,457427,469383,479432&retmode=xml)
resolves all 25 identifiers directly, without aliases: 17 species, seven strains
and one no-rank group. All 23 stored labels match. The two unlabeled entries
resolve to NCBITaxon:36987 Coptotermes formosanus and NCBITaxon:39946 Oryza sativa
Indica Group. Their valid identities do not independently validate ecological
associations, and their nonmicrobial nature is not itself a schema violation.

Primary [Olson and Dinerstein 2002, page 215](https://files.worldwildlife.org/wwfcmsprod/files/Publication/file/5xdxix5fsv_The_Global_200_Priority_Ecoregions_for_Global_Conservation.pdf)
places xeric basins in the freshwater realm and describes ephemeral watercourses
and lakes together with permanent springs. Inspected official FEOW accounts for
[Lake Eyre Basin](https://www.feow.org/ecoregions/details/806) and
[Inner Mongolia Endorheic Basins](https://www.feow.org/ecoregions/details/621)
independently support the dry-region freshwater classification. Their regional
examples, fauna and numeric tolerances cannot populate universal parameters or
validate the 36 PREGO associations.

The current ENVO definition still says low relative spring abundance. Its
annotation explicitly notes ambiguity and cites a WWF biome page. That page's
redirect could not be inspected reliably; direct retrieval returned HTTP 403.
The inspected primary paper establishes permanent springs, not their comparative
abundance. Thus the wording's comparison baseline remains unclear, but this
review does not establish a reversed quantifier or substitute a conjectural
definition. Ontology-owned definitions require upstream ENVO clarification and
governed refresh, not a local term-request override.

## Completeness

Ignored-inclusive ID/label/slug/mint searches across curation, history, research,
conf, docs, src, tests, PATHS, RETIRED and research manifest found only the path
pin. Own-name filename searches across curation/history/research found no
target-owned research, overlay or session. These searches included ignored files.

Ignored-inclusive filename searches across build and the configured kg-microbe
data directory found no PREGO nodes/edges dump in those layouts. The live PREGO
site timed out. The untruncated 36-taxon pool, original accessions and association
evidence therefore remain unverified beyond the governed inventory; this is a
bounded access limit, not proof that associations are false. Empty optional
literature, parameter and graph fields should not be filled for coverage.
No gene/regulator/pathway/transcriptomic claim makes iModulonDB applicable.

## Findings

1. **Minor: two resolvable taxon names are missing.** Ranks 16 and 18 lack
   names in both the generated record and raw inventory (`prego_habitat_taxa.tsv`
   lines 5303 and 5305), despite current canonical NCBI names. The maintained
   owner is governed PREGO/NCBI source data and `_load_taxon_labels` in
   `src/habitatmech/extract.py`, which reads the transformed NCBI node table.
   This is a non-blocking source-reference maintenance gap, not two broken
   CURIEs or proven false habitat associations.

Totals: zero blockers, zero major, one minor finding.

## Recommended Edits

In a separately authorized refresh, supply the two verified names through
versioned source inputs and the extractor, preserving IDs, source provenance,
25 retained rows, 36-candidate pool, tied scores and observational status.
Do not remove nonmicrobial taxa or substitute bacteria merely from their names.
Recover original association evidence before adjudicating ecological correctness.
Keep the ENVO spring-abundance wording as an explicit unresolved precision
question pending inspectable source clarification; do not hand-edit YAML or
checksums, infer a definition override or promote identity-review status.

## Follow-up Checks

Test optional-label and canonical-ID handling in the source refresh; compare
complete before/after inventories and corpus. Recheck taxonomy and original
association accessions, then provenance, canary, open/closed schema, append-only
session history, corpus, labels, semantic inputs, real map/site and full QC.
Any definition change must first satisfy the upstream ontology ownership path.

## Additional Notes

Read-only issue [#1257](https://github.com/CultureBotAI/HabitatMech/issues/1257)
is open for the same missing-label mechanism in generic lake, but concerns
different taxa and is not claimed to track this target. No GitHub mutation,
scientific curation, product regeneration, paid research or author contact
occurred. An optional BeautifulSoup import was unavailable; standard-library
retrieval then exposed the source HTTP 403 without installing dependencies.
Only this new report was written; the all-record goal remains incomplete.
