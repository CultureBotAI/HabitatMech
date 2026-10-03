# YAML Record Review: Mangrove sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/mangrove_sediment.yaml`
- Started UTC: 2026-10-03T17:23:59Z
- Finished UTC: 2026-10-03T17:24:52Z
- Verdict: needs curation

## Target

Read the entire generated `HabitatRecord`, `habitatmech:GOLD.376c23f892`,
Mangrove sediment, AQUATIC, UNGROUNDED, SEEDED. GOLD node 5364 is the sole
source, at Environmental > Aquatic > Marine > Intertidal zone > Mangrove
sediment. `PATHS.tsv:1699` pins the stem. The CLASS decision at
`curation/decisions.tsv:399` is a lexical-screen outcome, not ITEM curation;
its generated history and the seed event preserve that distinction.

## Validation

- `just validate data/habitats/aquatic/mangrove_sediment.yaml`: pass.
- `just validate-strict data/habitats/aquatic/mangrove_sediment.yaml`: one
  file, zero errors.
- Fresh full `just qc` was still running tests at review finish. Lint,
  documentation and provenance passed; remaining full-corpus gates are not
  claimed complete here.
- Read the complete maintained Intertidal zone parent in this batch. Current
  official ENVO OWL definitions, named parents and candidate labels were
  inspected, using the byte-verified current file with SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- No target DOI/PMID, taxon, mechanism or dataset references are attached.
  GOLD study memberships below were verified in the committed inventory,
  not on live study pages. Minted identity is outside OAK's configured scope.

## Identity and Grounding

The minted source preserves mangrove and intertidal qualifiers and does not
incorrectly equate the material with all sediment. Its sole parent,
`habitatmech:GOLD.115edc36f8` Intertidal zone, is nevertheless a geographic
context rather than a strictly broader material class. This differs from the
separate Mangrove area source: material located in a zone is not itself a
kind of zone.

Current [ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
defines `ENVO:00002007` sediment as particulate environmental material formed
through transport and deposition by flowing liquid. It is a supported broader
candidate, not exact identity for all mangrove sediment. The inspected
[NOAA mangrove account](https://oceanservice.noaa.gov/facts/mangroves.html)
distinguishes the mangrove setting from particles settling and accumulating
within it, independently supporting the material/context distinction.

Do not adopt `ENVO:00002113` from older "marine sediment" wording: current
ENVO calls it deep marine sediment and defines a deep-ocean setting. The
current marine-sediment class is `ENVO:03000033`; its water-column/seafloor
scope still needs comparison with this source. `ENVO:02000138` mangrove biome
soil is not automatically equivalent to sediment. A current-OWL label/synonym
search for mangrove terms found no exact sediment class; that bounded search
does not establish absence from every ontology.

## Evidence

`gold_ecosystem_paths.tsv:181` has one depth-five node and 114 ORGANISM
assertions, matching the record. `gold_path_biosamples.tsv:302` independently
records 68 samples. These units are not interchangeable or additive.

API rows 542-544 describe 30 samples and six studies. Broad mangrove biome
(`ENVO:01000181`) has one term, share 1.00 and six agreeing studies. Local
estuary (`ENVO:00000045`) has three terms, share 0.50 and two agreeing studies.
Medium sediment (`ENVO:00002007`) has two terms, share 0.97 and five agreeing
studies. Current definitions of all three IDs were inspected. The local mode
does not establish an estuary-only identity, and the rounded medium majority
is not unanimity or an exact-identity mapping.

Exact membership scans across all 4,587 study rows found nine accessions:
Gs0110103, Gs0110116, Gs0110188, Gs0111368, Gs0118783, Gs0142052,
Gs0159291, Gs0160785 and Gs0161532. Some span other sediment or habitat paths;
those shared memberships do not merge source concepts. The study table and
API summary are separate snapshots, not discrepant counts to reconcile by
adding or deleting studies.

## Completeness

Ignored-inclusive identifier, node, label, path and stem searches covered
curation, raw inputs, PATHS, history, research and prior reports. They found the
CLASS row and generic research mentions, but no target ITEM decision, authored
definition, overlay, dedicated history or completed individual report.

The 2026-08-16 ontology-process research note uses this label as a definition
example; it is not a verified habitat-specific definition or authority for
the now differently labelled marine-sediment ID. It was treated as a lead,
not primary evidence. Missing optional taxa and mechanisms are not defects.
iModulonDB is not applicable without a molecular or transcriptomic assertion.

## Findings

- **Major M1: sediment material is-a Intertidal zone.** The sole inherited
  source-parent edge is unsupported subsumption. Owner: target-specific
  maintained controls consumed by `src/habitatmech/seed.py:898`, or an
  evidence-backed definition in `curation/term_requests.tsv` with an ITEM
  decision in `curation/decisions.tsv`. Adding a sediment parent while leaving
  the zone edge does not repair the error.
- Blockers: 0. Major: 1. Minor: 0.

## Recommended Edits

Retain the minted source and its mangrove/intertidal context, establish a
verified sediment genus, and remove the false zone parent. Definition
`REPLACE` is justified only after recording that this sole inherited parent
is false; otherwise exclude exactly the source edge. Keep sediment distinct
from soil, swamp, biome and mangrove plant taxa. Preserve node, path and 114
ORGANISM assertions. Append history only with actual curation.

## Follow-up Checks

Dry seed and exact-source canary; inspect all generated parent contributions,
then strict validation, OAK labels for any added term, append-only history,
corpus reproduction, supported map/site generation and full QC. Check that
no same-label or neighboring mangrove source was merged. #1217/#1218 remain
regeneration dependencies, not permission to bypass checks.

## Additional Notes

The all-state search of 437 issues/comments found no target-specific issue;
the subsequently filed Lotic issue is distinct. Earlier estuary-sediment
reports concern a different source and do not complete this review. No
scientific input, generated record, page or history was changed.
