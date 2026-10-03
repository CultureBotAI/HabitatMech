# YAML Record Review: marine sponge reef

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_sponge_reef.yaml`
- Started UTC: 2026-10-03T20:15:45Z
- Finished UTC: 2026-10-03T20:18:40Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord for `ENVO:01000161`, marine sponge
reef: AQUATIC, EXACT, SEEDED, sole PREGO attestation, four observational taxon
entries and one seeding event. `data/habitats/PATHS.tsv:789` pins its stem.

## Validation

- `just validate data/habitats/aquatic/marine_sponge_reef.yaml`: passed.
- `just validate-strict data/habitats/aquatic/marine_sponge_reef.yaml`: one
  file, zero errors.
- All four raw-to-record taxon comparisons passed; all four current NCBI IDs
  resolve directly, with no alias substitutions.
- Fresh `just qc`: 455 tests passed, three skipped, two warnings; 83 valid
  history records; 3,206 strict-valid corpus records; 32 overlays; curation
  floor and exact corpus reproduction passed. Site freshness passed. The
  retired-URL and later gates have not completed at report finish.
- OAK does not check these taxon labels or ecological associations. Required
  CI identity checks do not replace the scientific review below.

## Identity and Grounding

`ontology_terms.tsv:7666` and freshly fetched current ENVO agree on identity
and definition. `ontology_subclass_edges.tsv:5812` and current OWL assert
`ENVO:01000143` marine reef as the named parent. A reef built by sponges is a
seafloor structure, not a sponge host body or the entire associated biome.
The PREGO plural is separately RELATED_SYNONYM, not an invented ENVO synonym.

[DFO's Pacific reef description](https://www.pac.dfo-mpo.gc.ca/fm-gp/sustain-soutien/gsr-res/about-gsr-au-sujet-res-eng.html)
supports the reef-building interpretation and describes new sponges settling
on older rigid skeletons. The inspected
[Conway et al. 2001 abstract](https://journals.lib.unb.ca/index.php/GC/article/view/4076)
supports the described Canadian shelf setting and glacially scoured substrate.
Those sources do not establish a current universal distribution rule for all
sponge reefs or a modern taxonomic revision of the definition's Hexactinosa
wording. These remain limits on the definition audit, not a verified new
ontology error or a reason to conflate a reef with its builders.

The source key is `habitatmech:PREGO.6045a95e9c`. Ignored-inclusive searches
found the historical exact-grounding sample at `curation/samples/exact-20260814.tsv:26`,
but no ITEM decision for this source. A sample marked ok is not an ITEM
decision; SEEDED and the sole generated seeding event are consistent.

## Evidence

`prego_habitats.tsv:423` gives four taxa, four direct assertions, maximum score
1.3019, and environmental-samples evidence. All attestation fields match.
The complete displayed pool matches `prego_habitat_taxa.tsv:7872-7875`:

| Rank | Taxon ID | Current NCBI identity | Score |
|---:|---|---|---:|
| 1 | NCBITaxon:6047 | Geodia cydonium, species | 1.3019 |
| 2 | NCBITaxon:31330 | Ephydatia fluviatilis, species | 1.29935 |
| 3 | NCBITaxon:75883 | Lubomirskia, genus | 1.20849 |
| 4 | NCBITaxon:55567 | Suberites domuncula, species | 1.19316 |

All four source labels are blank and optional. All raw rows are direct
environmental-samples assertions without corroboration; the generated entries
preserve ranks, scores and pool 4 without `is_characteristic` or invented
association counts. NCBI taxonomy establishes identity and rank, not ecological
truth. Demospongiae membership alone does not prove that a marine species
cannot be associated with a glass-sponge reef; the record does not call these
taxa reef builders.

Two entries nevertheless have a substantive habitat-scope conflict:

- [Keller-Costa et al. 2014](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0088429),
  Abstract and Sampling, identifies E. fluviatilis as a freshwater sponge and
  explicitly samples it in a Dutch lake. This is inspected ecological evidence,
  not an inference from its scientific name.
- [PMID:17959393](https://pubmed.ncbi.nlm.nih.gov/17959393/), verified by NCBI
  EFetch, treats freshwater sponges and the Lake Baikal Lubomirskiidae,
  including Lubomirskia. NCBI confirms that the record's ID denotes the genus,
  not a similarly named marine organism.

These sources do not prove which original PREGO mention caused each mapping,
nor justify automatic deletion. They require reconciliation of the freshwater
context with the unqualified marine-reef association. The other two marine
taxon associations remain unverified at original study level as well.

## Completeness

All four members of the retained source pool were checked; no top-25
truncation applies. Empty optional parameter, graph, evidence, discussion and
dataset fields are not automatic defects. No mechanism is claimed.

Ignored-inclusive searches by identifier, label, stem and source key covered
curation, history, research, prior reports and PATHS. They found the sample
screen and related sponge-host research, but no target ITEM decision, term
request, overlay, authored session history or prior exact-target report.
Related research was used only as a lead. The complete parameter table was
scanned without a target-term match.

The configured upstream kg-microbe checkout lacks PREGO files in an
ignored-inclusive file search. A wider KG-Microbe-root search returned
permission-denied directories and is not exhaustive. The original transformed
PREGO rows and ecological evidence therefore remain uninspected; no claim is
made that they do not exist elsewhere.

## Findings

1. **Major - HM-SPONGE-REEF-001:** the unqualified marine-reef associations
   for freshwater E. fluviatilis and Lubomirskia require source-evidence
   reconciliation. Faithful projection and `direct_flag` do not resolve this
   conflict. Owner: maintained PREGO evidence/annotation inputs and
   `src/habitatmech/extract.py`, not generated YAML. Tracked in
   [#1296](https://github.com/CultureBotAI/HabitatMech/issues/1296).

No blocker or minor finding was independently established. The optional blank
names and correctly resolved identifiers are not broken references.

## Recommended Edits

Inspect the original PREGO evidence for the two freshwater taxa. Distinguish
generic sponge-host mentions or lexical conflation from a demonstrated reef
association, then retain with appropriate evidence/scope or correct the source
assertion with provenance. Do not broaden the habitat identity to all sponge
hosts or guess replacement taxa. Preserve original IDs, scores and ranks until
an evidence-backed source correction warrants recomputation.

## Follow-up Checks

Re-query taxonomy and inspect the original ecological assertions. If source
inputs change, update manifests and recompute counts/pools consistently;
canary and verify exact corpus reproduction, regenerate affected map/site in
the supported runtime tracked by #1217, and run strict/OAK checks and full QC.
No scientific fix or issue closure is claimed by this report.

## Additional Notes

Current [ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
SHA256: `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
All 460 existing open/closed issues and returned comments were searched before
filing #1296. An initial taxon-output formatter stopped on a missing optional
OtherNames element; the query was rerun and all four IDs/ranks were inspected.
iModulonDB was not applicable to any claim in this record. The external
ecological paper's gene discussion was not imported as a new mechanism.
No paid research, record mutation, history mutation or product generation was
performed for this review.
