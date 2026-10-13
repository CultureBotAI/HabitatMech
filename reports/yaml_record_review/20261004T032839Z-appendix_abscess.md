# YAML Record Review: Appendix abscess

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/appendix_abscess.yaml`
- Started UTC: 2026-10-04T03:26:14Z
- Finished UTC: 2026-10-04T03:28:39Z
- Verdict: needs curation

## Target

Read the full generated HabitatRecord `habitatmech:GOLD.0512cf397f`:
HOST_ASSOCIATED, NOT_APPLICABLE, REVIEWED. It has one whole-intestine parent,
one GOLD attestation with four ORGANISM assertions and two August 12/16
events. Source scope is Human > Digestive system > Large intestine >
Appendix abscess, not ordinary Appendix, anorectal abscess or skin Abscess.
Actual `mint` reproduces the key; `PATHS.tsv:1303` pins the filename.

## Validation

- `just validate data/habitats/host_associated/appendix_abscess.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/appendix_abscess.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch `just qc` remains in tests. Lint, documentation and raw
  provenance passed; no terminal success is claimed.
- Browser MeSH failed; direct official concept/descriptor JSON and primary
  PubMed EFetch succeeded. Failures do not supply source evidence.

## Identity and Grounding

`curation/decisions.tsv:125` explicitly makes an ITEM NOT_APPLICABLE decision.
The generated disposition, REVIEWED status and two events reproduce it
faithfully. Its disease/intervention/artifact/filler boilerplate does not
resolve the source's diagnosis-versus-physical-site ambiguity. Correct
generation is not independent support for that scientific judgment.

The inspected active [MeSH Abscess concept](https://id.nlm.nih.gov/mesh/M0000059.json)
describes purulent accumulation in tissues, organs or bounded spaces.
Active [D000038](https://id.nlm.nih.gov/mesh/D000038.json) resolves to that
preferred concept. These are scope comparisons, not a proposed exact
grounding of this anatomically restricted source to generic Abscess.

The complete comparison `abscess.yaml` retains a minted NARROW skin-source
habitat beneath mesh:D000038. The differing dispositions require a supported
source distinction, not automatic merging or automatic acceptance of either
record's answer.

The complete `large_intestine__65b4f112.yaml`, read in this batch, denotes
whole human Large intestine, `habitatmech:GOLD.5b0aa7456c`, NARROW beneath
[UBERON:0000059](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000059).
Its current official definition agrees with vendored row 12893 on the whole
tract subdivision; no authored broader-environment definition changes that
scope. Neither an excluded diagnosis nor a localized purulent collection
is a kind of whole large intestine. Source-path containment is not is-a.

## Evidence

`gold_ecosystem_paths.tsv:682` supplies node 6348, the exact five-level human
path and four organism assertions. Source label/path/ID and count/unit are
faithful. No patient, specimen, percentage or taxon count is implied.

Complete scans covered 2,562 tree paths, 1,040 bulk rows, 4,587 studies and
1,587 triads using the source key and appendix/appendiceal-abscess variants.
Only the tree row matched; the others do not resolve specimen identity.
Ordinary human Appendix, mammal Appendix and the parent's counts are not
substitutes for this source's four assertions.

The primary [Bennion et al. 1990 abstract](https://pubmed.ncbi.nlm.nih.gov/2405791/)
was read in full. It explicitly cultured abscess contents when present,
alongside peritoneal fluid and appendiceal tissue in a gangrenous/perforated-
appendicitis cohort. Primary ArticleIdList verifies PMID:2405791,
PMC1357960 and DOI:10.1097/00000658-199002000-00008. This establishes a
physical microbial-site interpretation worth assessing, not the identity
of this GOLD bin. Mixed-specimen counts and taxa are not abscess-only
observations and are not imported. Only the abstract is relied on here.

## Completeness

Ignored-inclusive searches for target ID, filename and appendix/appendiceal-
abscess wording covered curation, history, research, prior reviews, raw
inventories, PATHS and RETIRED. They found the ITEM row and source but no
target definition request, overlay, session, research report or earlier
exact-target review. Mentions in the two appendix reports are not reviews
of this distinct target. Old decisions do not retroactively require a
later-style session record merely to be reviewed now.

Full structured scans of 162 BacDive sources, 3,081 BacDive taxa, 770
parameters, 358 mappings, 58 Madin habitats, 1,378 Madin taxa, 719 PREGO
habitats and 8,807 PREGO taxa found no target-key or inspected abscess-variant
match. This is bounded inventory absence. Optional taxa, parameters and
graphs are not quotas. iModulonDB is not applicable: no gene, regulator
or expression-module claim is supplied.

## Findings

1. **Major - HM-APPENDIX-ABSCESS-001:** unsupported source-specific
   non-habitat judgment. Owner: `curation/decisions.tsv:125`; re-examine the
   site interpretation or document a specific exclusion rationale.
   Added to [#220](https://github.com/CultureBotAI/HabitatMech/issues/220).
2. **Major - HM-APPENDIX-ABSCESS-002:** unsupported whole-large-intestine
   superclass regardless of the eventual disposition. Owner:
   `src/habitatmech/seed.py:898-907` or a governed source-specific exclusion.
   Added to [#1327](https://github.com/CultureBotAI/HabitatMech/issues/1327).

No blocker or minor finding established. Source fields, count semantics
and status derivation are faithfully generated.

## Recommended Edits

Resolve this exact source as diagnosis, physical abscess site or sampled
material using source-specific evidence. Do not force a disease ontology
identity, transfer clinical-paper taxa, or merge with generic Abscess.
Correct the false whole-organ parent independently while preserving source
key, node 6348, path and four-ORGANISM provenance.

A read-only real-adapter comparison confirms parent removal drops Large
intestine and changes semantic input. Append required history, inspect a
guarded canary and regenerate map/site through supported tooling; #1217
remains relevant and draft #1218 remains separate. Do not hand-edit generated
YAML, globally remove source parents or encode containment as equivalence.

## Follow-up Checks

Test disposition and parent handling separately. Preserve intended status,
source count/unit and identity audit; verify strict schema, OAK, full
ancestry, history, corpus reproduction, map/site/redirect freshness and QC.
Obtain specimen-level provenance before importing biological observations.

## Additional Notes

All 493 existing issue bodies and returned comments were searched. #220
owns the exclusion family; #1327 now covers the two individually reviewed
abscess-source parent witnesses. #1325 concerns anatomical-part sources.
Comparison records were reference reads only. No scientific input,
generated artifact or history changed; no paid research ran.
