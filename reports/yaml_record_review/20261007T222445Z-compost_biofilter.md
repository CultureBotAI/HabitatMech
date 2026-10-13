# YAML Record Review: compost biofilter

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/compost_biofilter.yaml`
- Started UTC: 2026-10-07T22:22:18Z
- Finished UTC: 2026-10-07T22:24:45Z
- Verdict: pass

## Target

Read the complete generated HabitatRecord `ENVO:00002153`, compost biofilter,
ENGINEERED / EXACT / SEEDED, at baseline
`fd0276142f5c5a8a8a8982f985669ad853b013e4`. It has an ENVO definition, one
related plural synonym, one parent, one PREGO attestation, one taxon and the
seed event. There are no parameters, xrefs, literature-evidence objects,
causal graphs, discussions or dataset assertions.

## Validation

Commands used `UV_CACHE_DIR=build/uv-cache`.

- Fresh `just validate data/habitats/engineered/compost_biofilter.yaml`:
  no issues.
- Fresh `just validate-strict data/habitats/engineered/compost_biofilter.yaml`:
  one file, zero errors.
- Fresh read-only `build_corpus` / `build_document`: all-field equality,
  one source, zero reviewed sources and no applied decisions.
- Fresh structured ENVO responses verified both habitat IDs, labels,
  definitions and active status. NCBI EFetch verified the strain identifier.
- The source mint, all matching raw rows, PATHS entry and absence searches
  were checked independently of gitignore.

Full local QC is reused from the immediately preceding exact-head run:
533 passed, three skipped; 159 valid histories; 3,207 strict-valid and exactly
reproduced records; 32 valid overlays; provenance, curation floor, site,
redirect and term-request checks passed. It was not rerun for this target.
The older OAK result on the unchanged scientific corpus is also reused:
1,178 canonical, one synonym, five accepted exceptions, 2,056 no-adapter skips.
No claim is made that queued PR #1661 checks have passed.

## Identity and Grounding

Official [ENVO:00002153](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002153)
agrees with the compost-containing pollutant-removal biofilter identity and
definition. This is the filter system, not generic compost material or the
composting process. Its parent
[ENVO:00002152 biofilter](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002152)
is strictly broader; the local subclass edge at
`data/raw/ontology_subclass_edges.tsv:5357` has the correct direction.
Compost itself is not incorrectly asserted as a superclass of the device.

PREGO names the ontology CURIE directly, so EXACT identity is supported.
The source mint is `habitatmech:PREGO.ec3ae847eb`. No maintained ITEM decision
was found, consistent with SEEDED and the absence of a review event. This
read-only judgment does not change that curation status. The PREGO plural
`compost biofilters` is retained with related, not inflated exact, scope.

## Evidence

**Inventory fidelity.** All 14 raw TSVs were inspected with exact field and
pipe-member matching. `prego_habitats.tsv:702` has one taxon, one direct
assertion, maximum score 3, the annotated-genomes/isolate channel and the
canonical/plural spellings. `prego_habitat_taxa.tsv:6169` has the one direct
PM1 association, rank 1, score 3 and no corroborating source. These values
match the generated attestation and taxon entry, including candidate pool 1.
Another raw association for the same strain belongs to a different habitat;
it was not counted as a second observation for this target. TAXON is not a
sample, study or abundance unit, and no `is_characteristic` flag is asserted.

**Taxon identity.** Official
[NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=420662&retmode=xml)
returns NCBITaxon:420662, Methylibium petroleiphilum PM1, rank strain, with
species parent 105560. The generated name is current. The inspected
[BacDive strain record](https://bacdive.dsmz.de/strain/134120) links PM1 with
ATCC BAA-1232 and LMG 22953, explicitly reports compost-biofilter isolation,
and links its genome/sequence entries to taxon 420662. Its species-level
header ID 105560 is not a conflicting strain identifier. This external check
does not add a new BACDIVE attestation to the generated record.

**Primary association evidence.** Three original-study metadata/abstract
records were successfully read through the Europe PMC core API after browser
page failures:

- [Hanson et al. 1999, PMID:10543787](https://europepmc.org/article/MED/10543787),
  DOI 10.1128/aem.65.11.4788-4792.1999, explicitly reports PM1 isolated from
  a mixed consortium in a compost biofilter. This supports the habitat link,
  not ubiquitous presence in every such filter.
- [Bruns et al. 2001, PMID:11321538](https://europepmc.org/article/MED/11321538),
  DOI 10.1046/j.1462-2920.2001.00184.x, reports compost-biofilter-material
  enrichment and molecular profiling of PM1-like populations. Dominance is
  bounded to MTBE-grown enrichments; it is not a general habitat-abundance
  claim to add here.
- [Nakatsu et al. 2006, PMID:16627642](https://europepmc.org/article/MED/16627642),
  DOI 10.1099/ijs.0.63524-0, ties the species description to PM1 and the two
  type-strain collection identifiers. Culture traits and growth optima from
  that study were not imported as habitat parameters.

These checks corroborate the association but do not reconstruct PREGO's
particular score calculation or prove that the publications are independent
isolations. No gene, expression module or causal mechanism is asserted in
the target. iModulonDB is therefore not applicable to this record-level check;
papers discussing PM1 metabolism do not require adding those claims.

## Completeness

Ignored-inclusive searches covered the ID, source mint, label, slug and taxon
across curation, history, conf, tests, docs, research, its manifest, raw inputs,
PATHS, RETIRED and prior review reports. They found the ontology/PREGO inputs
and PATHS entry, not a target-owned decision, term request, exclusion, overlay,
retirement, session history or research-manifest item. A research comparison
and earlier generic-biofilter reviews mention this class contextually; neither
is a previous individual review of this record. An ignored-inclusive header
scan found no prior report for the exact target path.

The optional empty fields are not defects. A maintained source association
can be valid without an inline causal graph or a catalogue of all possible
filter organisms. No missing required representation was established.

## Findings

None found: zero blockers, zero major findings, zero minor findings.

## Recommended Edits

None required for the present scientific claims. In separately authorized
curation, an ITEM REVIEW decision for PREGO.ec3ae847eb could record this source
assessment in `curation/decisions.tsv`, with append-only session history.
Do not hand-edit mapping status or treat this report as that decision.

Any future evidence enrichment must keep the filter/device, compost medium,
laboratory enrichment, strain identity and generic association distinct. Do
not copy generic compost's parameter bands or thermophilic graph into this
record, or mark PM1 universally characteristic from enrichment dominance.

## Follow-up Checks

No correction is required. If an ITEM decision is later authorized, dry seed,
inspect `just seed-canary ENVO:00002153 --force`, validate the event/history,
reproduce the corpus and site, and run full QC and ontology-label checks.
Preserve the ontology definition and parent, the one TAXON count, PREGO score,
rank/pool, strain ID and existing seed event.

## Additional Notes

The Hanson PMC page presented a browser challenge and the Bruns PubMed page
returned HTTP 429. Their primary abstracts were instead inspected through
Europe PMC; full texts and quantitative figures were not verified. Search
results for a similarly titled Hydrogenophaga study were not treated as PM1
evidence. No scientific curation, generated product, history or status change,
paid research, delegation or GitHub mutation occurred. Only this new review
report was written for this target.
