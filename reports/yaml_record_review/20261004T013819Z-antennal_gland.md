# YAML Record Review: antennal gland

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/antennal_gland.yaml`
- Started UTC: 2026-10-04T01:33:59Z
- Finished UTC: 2026-10-04T01:38:19Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord for `UBERON:0009963`:
HOST_ASSOCIATED, EXACT, REVIEWED. It has an ontology definition, two synonyms,
two parents, one GOLD attestation without a positive count and two events.
The source is Crustaceans > Excretory system > Antennal/Green glands, not
an insect antennal reservoir or the external surface of an antenna.
The actual `mint` helper reproduces source key `GOLD.cb3fda7227`;
`PATHS.tsv:1122` pins the current slug and `RETIRED.tsv:17` preserves the
former minted-source URL.

## Validation

- `just validate data/habitats/host_associated/antennal_gland.yaml`: passed.
- `just validate-strict data/habitats/host_associated/antennal_gland.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh `just qc`: terminal PASS. Tests: 457 passed, three skipped, two
  dependency warnings. Also passed: 85 history records; 3,206 strict-valid
  records; 32 overlays; curation floor; exact corpus reproduction with zero
  missing, extra or differing records; current site; 231 redirects; 109
  term-request table entries; final corpus report.
- Current official OLS, NCBI taxonomy and PubMed EFetch responses were
  inspected successfully. Browser OLS requests failed; those failures are
  not treated as separate successful source inspection.

## Identity and Grounding

`curation/decisions.tsv:1645` is an ITEM GROUND to UBERON:0009963 with EXACT
scope. Current [antennal gland](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0009963)
is non-obsolete, retains green gland as a synonym, and describes the excretory
gland at the antennal peduncle. Vendored `ontology_terms.tsv:13391` agrees.
The slash/plural GOLD wording and crustacean path justify this anatomical
identity; it is not a whole-host taxon. The separate current BTO:0000075
term also describes this gland, but no duplicate record or new xref is needed.

The source's sole ITEM grounding explains REVIEWED, the exact mapping
predicate and August 16 events. The historical #12 backlog reference was
checked; its old counts and host interpretations are not current evidence.
The definition's spelling `rehulate` is faithfully inherited from both the
vendored and current UBERON text, not a new local transcription error.
No generated-definition patch is proposed for that cosmetic upstream wording.

Current [antennal-gland graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009963/graph)
asserts subclass UBERON:0009962, excretory gland, agreeing with vendored
subclass edge 11678 and term row 13390. This is the valid ontology parent.
The separately inspected [excretory-gland graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0009962/graph)
asserts subclass gland but `BFO:0000050` part_of UBERON:8450002, excretory
system. The typed part relation is on the superclass, not falsely reported
as a direct edge from the antennal-gland node.

The complete `excretory_system__22ee753c.yaml` identifies the second parent,
`habitatmech:GOLD.d0a97e09fe`, as a crustacean source NARROW beneath whole
[excretory system](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A8450002),
without an authored gland-environment definition. Current definition and
vendored row 13552 agree. The gland-to-system link is containment, not a
subtype claim. Positive ontology relations and definitions establish this
distinction; absence of an is-a edge alone is not the argument.

## Evidence

`gold_ecosystem_paths.tsv:1768` supplies the exact four-level source path,
two nodes 7330/7331 and zero organism/study/biosample assertions. The generated
first ID, full path, label and multiplicity note are faithful. Omitting a
positive count is correct; zero source assertions do not prove the organ
cannot contain microbes. Parent row 1767 contains different nodes
7329/7332/7333 and is not another target attestation.

Complete scans of 2,562 GOLD paths, 1,040 bulk-count rows, 4,587 studies
and 1,587 triads found only the target tree row for antennal/green-gland
wording. No sample, organism list or live-study metadata are fabricated.

The inspected primary-study abstract for
[De Gryse et al. 2020](https://pubmed.ncbi.nlm.nih.gov/33097672/)
verifies PMID:33097672 and DOI:10.1073/pnas.2013518117. Imaging and infection
experiments support a real crustacean excretory organ accessible to microbes.
They do not establish universal colonization, convert gland into a subtype
of a whole system, validate GOLD sample identities, or authorize importing
experimental pathogens/mechanisms into this record. Only the abstract was
inspected, not the full paper's detailed methods.

The extra source parent arises at `src/habitatmech/seed.py:898-907`.
The schema and `docs/CURATION.md` require every `parent_habitats`
contribution to be strictly broader/is-a; a preserved source breadcrumb
cannot justify publishing a different relation type.

## Completeness

Ignored-inclusive target/source/parent IDs, label, source label and stem
searches covered curation, history, research, prior reviews, PATHS, RETIRED
and raw inventories. They found the ITEM decision, ontology entries and
redirect, but no target term request, overlay, session record, target
research report or earlier exact-target review. Missing optional fields
and a later-style session file for older curation are not findings.

Full structured scans of 719 PREGO habitats, 8,807 PREGO taxa, 162 BacDive
sources, 3,081 BacDive taxa, 770 parameters, 358 mappings, 58 Madin habitats
and 1,378 Madin taxa found no antennal/green-gland or UBERON:0009963 /
BTO:0000075 match. Insect antennal symbionts mentioned in a neighboring
research report are different anatomy and were not imported. iModulonDB
is not applicable: the target makes no gene, regulator or expression claim.

## Findings

1. **Major - HM-ANTENNAL-001:** the valid gland identity also carries a
   whole-excretory-system superclass contributed by GOLD source nesting.
   Maintained owner: `src/habitatmech/seed.py:898-907` or a governed
   source-specific exclusion. Tracked in
   [#1328](https://github.com/CultureBotAI/HabitatMech/issues/1328).

No blocker or minor finding established. Exact anatomical identity, the
excretory-gland parent, ITEM status and source copying remain supported.

## Recommended Edits

Correct or exclude this particular GOLD parent contribution while retaining
UBERON:0009963, UBERON:0009962, source-node multiplicity, reviewed grounding
and the existing redirect. Do not hand-edit generated YAML, convert part-of
into an equivalence xref, globally delete GOLD ancestry or rename the record
after a proposed terminology change in one experimental paper.

Append required curation history, inspect a guarded canary and compare actual
semantic inputs before supported map/site regeneration. #1217 remains the
runtime limitation when inference is needed; draft #1218's mechanism is
not on main. No correction is claimed in this read-only report.

## Follow-up Checks

Regress this organ-to-system edge independently; retain the valid gland
superclass, exact mapping and source fields without inventing a count.
Check the entire ancestor chain, strict schema, OAK, history, corpus
reproduction, map/site/redirect freshness and full QC.

## Additional Notes

All 484 existing issues and returned comments were searched for antennal
wording, source/parent keys and UBERON:0009963; no matching repair was found.
#1328 was filed without closing the general #12 backlog. The ontology graph
also points to historical NCBITaxon:6657; current EFetch resolves that query
to Pancrustacea (197562), so it was not treated as proof of a present exact
Crustacea taxon identity or used to expand this source to insects.
No scientific input, generated record or history was changed; no paid
research ran. Parent and comparison reads do not add to target-review coverage.
