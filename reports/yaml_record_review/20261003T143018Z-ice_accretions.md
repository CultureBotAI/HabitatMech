# YAML Record Review: Ice accretions

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/ice_accretions.yaml`
- Started UTC: 2026-10-03T14:27:57Z
- Finished UTC: 2026-10-03T14:30:18Z
- Verdict: pass

## Target

Read the complete generated `HabitatRecord`, `habitatmech:GOLD.c4f57235c7`,
Ice accretions, `AQUATIC`, `UNGROUNDED`, `SEEDED`. It contains a freshwater-ice
parent, one GOLD attestation, a CLASS confirmation and a seed event. There
are no authored definitions, taxa, parameters, evidence objects or graphs.
`PATHS.tsv:2733` locks this exact target.

## Validation

- `just validate data/habitats/aquatic/ice_accretions.yaml`: pass.
- `just validate-strict data/habitats/aquatic/ice_accretions.yaml`: pass,
  one record, zero errors.
- `mint('GOLD', source_path)` reproduces the ID; the full source row and
  `curation/decisions.tsv:1095` agree with the emitted statuses/history.
- Current OLS responses verify freshwater ice, polar biome and glacial lake;
  ice was verified during the immediately preceding ice review.
- Full baseline QC passed at `7f1e021db7a9578ff090e55713f7ebd0080ab3dc`,
  [run 37128839209](https://github.com/CultureBotAI/HabitatMech/actions/runs/37128839209),
  with network label correspondence passing run 37128839287. Fresh local
  full QC is still running. No target or maintained input changed.
- The live GOLD study page returned a retrieval error; `Gs0060824` membership
  was verified only in the committed source snapshot, not its live metadata.

## Identity and Grounding

The path `Environmental > Aquatic > Freshwater > Ice > Ice accretions`
supports deposited ice material, not an accretion process as habitat identity.
`ENVO:01001511` freshwater ice is defined in current ENVO as water ice made
by freezing fresh water, so it is an appropriate broader material parent.
The local slice lacks its definition, but retains its correct active label.
[Freshwater ice](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001511).

The CLASS-depth decision records a lexical nonmatch, not a completed
individual habitat assessment. `UNGROUNDED` and `SEEDED` preserve that
limitation honestly. The inspected slice contains no accretion-ice identity;
this bounded observation is not a claim that no ontology anywhere can name it.
NSIDC's meteorological accretion entry describes a formation process and
must not be substituted for the resulting ice material in this GOLD path.
[NSIDC accretion](https://nsidc.org/learn/cryosphere-glossary/accretion).

## Evidence

`gold_ecosystem_paths.tsv:934` supplies the exact node `gold.ecosystem:4062`,
depth five and one organism assertion. Its label, path, count and `ORGANISM`
unit match the record. `gold_path_biosamples.tsv:966` separately gives one
bulk-export sample; `gold_studies.tsv:308` supplies study `Gs0060824`.

`gold_path_triads.tsv:308-310` contains one complete API triad from one study:
polar biome (`ENVO:01000339`), glacial lake (`ENVO:00000488`), and ice
(`ENVO:01001125`). Each modal share is 1.00 because the denominator is one,
not because independent studies establish universal class meaning. The
biome/local-feature/material roles were not collapsed into identity. Bulk,
API and organism counts were neither summed nor assumed to represent an
identical underlying object solely because each happens to be one.

Primary abstracts describe ice accreted from Lake Vostok water and microbes
in sampled accretion ice. They support a real environmental-material usage,
not a universal community, viability claim or equation of the GOLD source
with that named lake. No connection to `Gs0060824` was established.
PMID:10591642, DOI:10.1126/science.286.5447.2141, and PMID:18552196,
DOI:10.1128/AEM.02501-07 were verified through Europe PMC structured records.
[Geomicrobiology study](https://doi.org/10.1126/science.286.5447.2141),
[isolation study](https://doi.org/10.1128/AEM.02501-07).

## Completeness

Ignored-inclusive searches for the exact ID, label, stem and accretion-ice
wording covered curation, history, research, configuration, raw inventories
and prior reports. No target ITEM decision, authored definition, graph,
session history or exact-target review was found. Empty optional traits and
taxa are appropriate; a broad literature example does not fill them.
iModulonDB is not applicable because no organism-specific molecular claim
is present. No specific freezing mechanism, age, depth or temperature was
imported from the example papers.

## Findings

None found: zero blockers, zero major findings, zero minor findings.
Pass applies to the current conservative seeded representation, not to a
claim that an ITEM-level definition or source study has already been curated.

## Recommended Edits

No corrective edit is required by this review. Optional future ITEM curation
could clarify formation and source scope in `curation/decisions.tsv` and,
if a novel term is warranted, `curation/term_requests.tsv`. Do not force a
match to glacial lake, the meteorological process or generic ice merely to
eliminate `UNGROUNDED`.

## Follow-up Checks

Read the actual source study/sample metadata before naming a lake or adding
a definition, organism or mechanism. If future inputs change, canary this ID,
preserve source count units, regenerate affected products, and pass schema,
corpus, applicable label, history, map/site and full QC gates.

## Additional Notes

PMC's browser endpoint returned a challenge and Europe PMC full-text XML
returned HTTP 500. The two structured abstracts were successfully inspected;
full-text methods were not claimed as checked. This report is the only write.
