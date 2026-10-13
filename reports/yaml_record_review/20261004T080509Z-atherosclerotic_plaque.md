# YAML Record Review: atherosclerotic plaque

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/atherosclerotic_plaque.yaml`
- Started UTC: 2026-10-04T07:53:49Z
- Finished UTC: 2026-10-04T08:05:09Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord BTO:0003120: HOST_ASSOCIATED,
EXACT, SEEDED. It contains a BTO definition, five PREGO related synonyms,
one PREGO attestation, 25 ranked taxon associations and one seed event.
No parent, environmental parameter, causal graph or dataset is emitted.
PATHS.tsv:358 pins the filename. The actual mint helper reproduces the
PREGO source key `habitatmech:PREGO.b240de33b7`.

## Validation

- `just validate data/habitats/host_associated/atherosclerotic_plaque.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/atherosclerotic_plaque.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
  This gate does not validate the NCBI taxon associations.
- Fresh batch `just qc`: terminal pass, exit zero. Lint, docs, provenance,
  457 tests (three skips, two dependency warnings), 90 history records,
  3,206 schema records, 32 causal overlays, curation floor, exact corpus,
  site, 231 redirects, 109 emitted term requests and final report passed.
  Test time was 464.25 seconds. Scientific inputs remained unchanged.
- Official OLS metadata and typed graph inspected. Official NCBI taxonomy
  EFetch resolved all 25 requested IDs; all 21 emitted names matched.
  Official PMC XML supplied primary methods/results where browser pages
  returned challenges. No original PREGO pair-level export was available
  in the configured upstream checkout.
- Read-only semantic comparisons used the actual adapter with full corpus
  context; results are distinguished from an actual source regeneration.

## Identity and Grounding

Current [BTO:0003120](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0003120)
is active and agrees with ontology_terms.tsv:3120 and the emitted definition.
This is a physical arterial deposit, not the disease atherosclerosis itself.
An excised plaque can be a microbial sampling material; disease association
alone is not grounds to mark the physical lesion NOT_APPLICABLE.

The typed BTO graph has narrower carotid and coronary plaque subclasses.
Its outgoing link to tunica intima vasorum BTO:0002012 is a disease-causes-
dysfunction relation, not subclass-of. A foam-cell part-of link also does
not supply a superclass. The complete vendored subclass-table scan found
no outgoing subclass edge from BTO:0003120. No missing is-a parent was
established. Current flat synonyms include arterial plaque and atheroma
cell; the emitted PREGO synonyms correctly remain RELATED_SYNONYM.

No ITEM decision was found. EXACT reflects the source ontology identifier,
not curator approval; SEEDED correctly preserves that distinction.

## Evidence

`data/raw/prego_habitats.tsv:241` records 39 unique source taxon IDs,
39 direct assertions, maximum score 1.42024 and environmental_samples.
The emitted count is TAXON, not patients, species, isolates or genomes.
`data/raw/prego_habitat_taxa.tsv:2734-2758` supplies the retained top 25.
Every emitted ID, name or name absence, score, rank, source and pool size
agrees with that inventory. All retained raw rows have direct_flag TRUE,
the environmental_samples channel and empty corroboration. The raw flags
are not per-taxon evidence fields in the emitted record.

`src/habitatmech/extract.py:extract_prego` aggregates unique habitat/taxon
pairs, takes maximum scores, combines channels, and ranks before retaining
25. `_load_taxon_labels` uses exact IDs without alias normalization.
`src/habitatmech/seed.py:ingest_prego` copies these associations. Neither
source scores nor a direct flag prove viable colonization, characteristic
status or causal effects. No entry claims `is_characteristic: true`.

All 25 taxon IDs resolved in current NCBI EFetch. The four unnamed rows
require particular care:

| Rank | Emitted ID | Current resolution |
| --- | --- | --- |
| 13 | NCBITaxon:335058 | Alias of NCBITaxon:93681, Roseateles; explicit AkaTaxIds entry |
| 14 | NCBITaxon:35493 | Streptophyta, a plant lineage |
| 16 | NCBITaxon:629395 | Bacteria Latreille et al. 1825, an insect genus |
| 19 | NCBITaxon:169215 | Bosea, a plant genus in Amaranthaceae |

The [insect ID](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=629395)
is not bacterial-domain NCBITaxon:2, already retained at rank 12 with the
same score. The [plant ID](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=169215)
is not [Allobosea, NCBITaxon:85413](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=85413),
the bacterial genus formerly named Bosea retained at rank 20 with the same
score. This pattern warrants source disambiguation. A name-collision cause
is an inference, not a reconstructed upstream error. Eukaryotic lineage
alone does not prove an environmental DNA association false, and the schema
does not prohibit all nonbacterial associations.

Inspected primary literature establishes bounded plaque sampling contexts:

- [PMC4056553](https://pmc.ncbi.nlm.nih.gov/articles/PMC4056553/),
  PMID:24917599, DOI:10.1128/mBio.01206-14, reports bacterial 16S detection
  in 15 carotid explants, with additional analyses on smaller subsets.
  Five microscopy specimens showed probe-labeled deposits. PCR controls
  and a laboratory-strain sequence comparison were reported, but do not
  establish that every possible contamination source was excluded. The
  separate in-vitro biofilm experiments do not prove in-vivo causation.
- [PMC13023004](https://pmc.ncbi.nlm.nih.gov/articles/PMC13023004/),
  PMID:41908294, DOI:10.1080/20002297.2026.2648325, examines 25 paired
  subgingival/carotid samples using 16S DNA analysis. Its small,
  cross-sectional cohort cannot establish causation; the authors also
  discuss contamination susceptibility of low-biomass samples.

These papers are not verified source documents for the individual PREGO
pairs. They do not validate all 25 associations or the suspected homonyms.

## Completeness

Ignored-inclusive searches covered identifier, source key, label and stem
in curation, history, research, PATHS, RETIRED and prior report metadata.
The pinned path was found, but no target decision, term request, overlay,
curation session, research report, redirect or prior target review.

Complete structured scans covered all 12 non-ontology inventories using
BTO:0003120, the source key, atherosclero and atheroma wording. Only the
PREGO rows matched: no hits in 2,562 GOLD paths, 1,040 bulk-biosample rows,
4,587 studies, 1,587 triads, 162 BacDive sources, 3,081 BacDive taxa,
770 parameters, 358 mappings, 58 Madin habitats or 1,378 Madin taxon rows.
This bounded search does not establish absence under every possible synonym.

The manifest-named PREGO nodes/edges were absent at their configured paths.
An ignored-inclusive filename search of the configured kg-microbe checkout
also found no PREGO-named files. This is not a whole-machine absence claim.
Recover versioned originals before auditing or rebuilding the full 39-ID
matrix; the retained 25 rows cannot reconstruct it.

Empty optional slots and four optional name omissions are not independent
schema defects. No gene, regulator, pathway or expression dataset is claimed;
iModulonDB is not applicable.

## Findings

1. **Major - HM-PLAQUE-001:** two unresolved cross-kingdom homonym
   associations lack inspectable pair-specific support. Taxon identities
   are verified, but occurrence interpretation and upstream cause remain
   unresolved. Maintained owners: versioned PREGO source identity mapping
   and `src/habitatmech/extract.py:extract_prego`, followed by ordinary
   seeding. Tracked in [#1359](https://github.com/CultureBotAI/HabitatMech/issues/1359).
2. **Minor - HM-PLAQUE-002:** NCBITaxon:335058 is a retired alias of
   [NCBITaxon:93681 Roseateles](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=93681).
   It resolves, so this is freshness debt, not a dangling reference or
   habitat-identity blocker. Maintained owners: versioned taxonomy/PREGO
   normalization and `_load_taxon_labels`. Tracked in
   [#1360](https://github.com/CultureBotAI/HabitatMech/issues/1360).

No blocker established. A missing optional citation by itself is not a
separate defect for every seeded association.

## Recommended Edits

Recover original pair evidence, then correct or explicitly qualify/quarantine
unsupported associations through a governed source/extraction contract.
Do not blindly replace nonmicrobial IDs with same-named bacterial IDs or
delete every eukaryote. Preserve distinctions among reported association,
contamination, viable colonization and characteristic membership.

Canonicalize the verified alias reproducibly, retaining original source-ID
provenance. Inspect the complete source matrix for canonical duplicates
before recalculating counts, ranks and the top 25. Never subtract from 39
by hand, patch generated YAML or rewrite checksums to conceal source drift.
An actual curation change needs append-only history.

The actual semantic adapter comparison found no text change for an ID-only
335058-to-93681 substitution, or removal of just the two unnamed homonyms.
Adding the canonical name introduces `observed taxon: Roseateles` and changes
text. These simulations do not prove a full corrected extraction is neutral:
backfilled ranked taxa or added labels may change it. Compare actual full
inputs and use the governed rebuild in
[#1217](https://github.com/CultureBotAI/HabitatMech/issues/1217) when required.
Do not classify every ID-only repair as blocked by that runtime limitation.

## Follow-up Checks

Add regressions for homonym disambiguation, retained supported controls,
alias resolution, canonical deduplication, provenance and ranked-pool counts.
Run extraction provenance checks, dry seed and guarded canary; inspect the
record and require ordinary/strict validation, OAK, history, exact corpus,
semantic-map/site freshness and full QC. Scientific evidence review remains
necessary even when structural gates pass.

## Additional Notes

Deduplication searched all 505 returned pre-existing issue titles, bodies
and returned comments, with a tighter check of the exact taxon IDs and
homonym names. Other habitat-specific evidence/alias issues did not cover
these witnesses. #1359 and #1360 keep source-evidence and canonical-ID
questions separate; both remain open.

No scientific input, generated record/page, status, event or history changed.
No paid research ran. Protected draft #1218 remains open, draft and unchanged
at `18c93452a789218f5c653d02723d11388d972055`. This is a record review, not
independent PR approval. Full-corpus review remains ongoing.
