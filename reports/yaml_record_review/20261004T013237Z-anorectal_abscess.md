# YAML Record Review: Anorectal abscess

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/anorectal_abscess.yaml`
- Started UTC: 2026-10-04T01:29:21Z
- Finished UTC: 2026-10-04T01:32:37Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord for `habitatmech:GOLD.aaf13396b6`:
HOST_ASSOCIATED, NOT_APPLICABLE, REVIEWED. It contains one parent, one GOLD
attestation with three ORGANISM assertions and two generated events. The
source is Human > Digestive system > Large intestine > Anorectal abscess,
not whole anal canal, mucosa, ordinary rectum or a generic abscess source.
The actual `mint` helper reproduces its ID; `PATHS.tsv:2546` pins the slug.

## Validation

- `just validate data/habitats/host_associated/anorectal_abscess.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/anorectal_abscess.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh QC remains running, with lint, documentation and raw provenance
  passed and tests progressing. No terminal batch QC result is claimed yet.
- Current primary PubMed abstract, official MeSH JSON and HPO term responses
  were inspected. MeSH's browser page exposed a JavaScript shell; its JSON
  succeeded. A separate PMC paper returned a browser challenge and was not
  treated as successfully inspected full text.

## Identity and Grounding

`curation/decisions.tsv:971` is ITEM NOT_APPLICABLE, but its rationale lists
disease, intervention, sampling artifact or filler without distinguishing
those alternatives for this source. REVIEWED and the August 12 decision /
August 16 seed events accurately reflect that maintained input. Correct
reproduction of the decision is not evidence that its interpretation is sound.

Current [HP:0033150](https://www.ebi.ac.uk/ols4/api/ontologies/hp/terms?obo_id=HP%3A0033150)
is a non-obsolete anorectal-abscess phenotype term describing a localized
abscess at the anal-canal/rectal junction. It is not adopted as habitat identity.
The exact-label OLS query also returns disease/phenotype and procedure entries;
lexical matches do not decide whether GOLD means diagnosis, lesion site or
sampled material. No verified exact habitat grounding is imposed.

The complete comparison `abscess.yaml` retains human Skin > Abscess as a
minted NARROW habitat beneath `mesh:D000038`, with 17 ORGANISM assertions.
Current official [MeSH descriptor](https://id.nlm.nih.gov/mesh/D000038.json)
is active and labeled Abscess, agreeing with vendored `ontology_terms.tsv:13554`.
Its [preferred concept](https://id.nlm.nih.gov/mesh/M0000059.json) describes
purulent material accumulated within tissue or a bounded space. This supports
examining the physical-site reading, not automatically grounding every named
abscess to the same identity. The comparison record is precedent, not proof
that all its own parents are valid.

The complete human `large_intestine__65b4f112.yaml` identifies the target's
parent, `habitatmech:GOLD.5b0aa7456c`, as NARROW beneath whole
[UBERON:0000059](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000059),
with no authored broader environmental definition. Its current OLS definition
and vendored row 12893 denote the digestive-tract subdivision. Neither an
excluded non-habitat nor a localized abscess site is a subtype of that whole
organ. The source-path contribution at `src/habitatmech/seed.py:898-907`
therefore violates the strict broader/is-a parent contract independently
of the final abscess disposition.

## Evidence

`gold_ecosystem_paths.tsv:753` supplies node 6341, the complete five-level
human path, one source node, three organisms and zero study/biosample
assertions. The generated attestation copies these faithfully. Three source
organism assertions do not establish three independent samples, particular
taxa or a sampling protocol; the source's pathological wording alone also
does not prove the category is only a disease diagnosis.

Complete scans of 2,562 GOLD paths, 1,040 bulk-count rows, 4,587 studies and
1,587 triads found only that tree row for anorectal wording. No live GOLD
study or specimen-level interpretation is claimed. The whole intestine's
20-organism count and the skin-abscess count are not assigned to this target.

The inspected [Alabbad et al. primary abstract](https://pubmed.ncbi.nlm.nih.gov/30234438/)
verifies PMID:30234438 and DOI:10.1089/sur.2018.144. It reports microbiological
data for 211 patients within a retrospective anorectal-abscess cohort. This
supports a real microbial site interpretation requiring examination, but
does not identify GOLD's organisms, distinguish its source metadata, or
license importing the study's taxa or frequencies into the record. No clinical
treatment advice or causal mechanism is inferred.

## Completeness

Ignored-inclusive searches of exact identifier, label and stem covered
curation, history, research, prior reports, raw inventories, PATHS and RETIRED.
They found the ITEM decision and source row but no target definition, overlay,
session record, target research report or prior exact-target review. Absence
of a later-style session file for this older decision is not a separate defect.

Full structured scans of 719 PREGO habitats, 8,807 PREGO taxa, 162 BacDive
sources, 3,081 BacDive taxa, 770 parameters, 358 mappings, 58 Madin habitats
and 1,378 Madin taxa found no anorectal match. Generic abscess data do not
become this path's attestations. Optional taxa, parameters and graphs need
not be filled. iModulonDB is not applicable: no gene, regulator or expression
claim is supplied.

Older abscess reviews are leads, not scientific authority. Their acceptance
of a parent merely because it reproduces GOLD, or a disposition merely because
an ITEM row exists, cannot establish the required semantic relation. This
review does not extend their conclusions to the current source.

## Findings

1. **Major - HM-ANORECTAL-001:** the generic ITEM exclusion lacks a source-
   specific distinction between disease classification and physical abscess
   habitat, despite retained abscess-site precedents and primary microbiology
   evidence. Reopen or justify that decision; do not claim a replacement
   identity is already proved. Owner: `curation/decisions.tsv:971` and any
   resulting maintained definition. Added to existing
   [#220](https://github.com/CultureBotAI/HabitatMech/issues/220).
2. **Major - HM-ANORECTAL-002:** the source still asserts a whole-large-
   intestine superclass. This is unsupported under either the current
   exclusion or the alternative physical-site reading. Owner:
   `src/habitatmech/seed.py:898-907` or a governed source-specific exclusion.
   Tracked in [#1327](https://github.com/CultureBotAI/HabitatMech/issues/1327).

No blocker or minor finding established. Source identity is not silently
reassigned while specimen-level interpretation remains unresolved.

## Recommended Edits

Remove or evidence-correct the unsupported source-parent contribution while
preserving source path, ID, three-ORGANISM count and audit rationale. Separately
review the exact source's disease-versus-site interpretation at ITEM depth.
If physical habitat scope is supported, use a compatible broader habitat or
an authored minted definition; if exclusion remains appropriate, write the
specific evidence and contrast with retained abscess sources. Generic MeSH
Abscess and an HPO phenotype are not automatic exact habitat matches.

Do not hand-edit generated YAML, substitute equivalence xrefs for containment,
merge anatomical sites by shared wording or globally remove GOLD parents.
Append required history, inspect a guarded canary, compare actual semantic
inputs and regenerate map/site through supported tooling where needed.
#1217 remains a runtime limitation and draft #1218 is not merged.

## Follow-up Checks

Regress the independent parent correction and any newly justified disposition.
Check retained provenance, count/unit, intended status, full ancestor chain,
strict schema, OAK, history, corpus reproduction, map/site freshness and full
QC. Preserve published URLs if identity changes. Do not close the broader
#220 family issue from this single target.

## Additional Notes

All 483 existing issue bodies and returned comments were searched for
anorectal, the target key and abscess wording. #220 owns the disposition
family; #531 is a closed report-format correction and #1314 addresses
unrelated alveolar evidence. No matching exact parent repair was found, so
#1327 was filed separately from the canal/mucosa witnesses in #1325.
No scientific input, generated record or history was changed; no paid
research ran. Comparison records were reference reads, not new target reviews.
