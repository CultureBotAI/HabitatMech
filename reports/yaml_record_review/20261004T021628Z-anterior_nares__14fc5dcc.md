# YAML Record Review: Anterior nares

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/anterior_nares__14fc5dcc.yaml`
- Started UTC: 2026-10-04T02:13:41Z
- Finished UTC: 2026-10-04T02:16:28Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.cdc9731b44`:
HOST_ASSOCIATED, NARROW, SEEDED. It has two parents, one GOLD attestation
with three ORGANISM assertions and one seed event. The exact source is
Human > Respiratory system > Nasal cavity > Anterior nares, not the separate
mammal source reviewed earlier. The actual `mint` helper reproduces its
identifier; `PATHS.tsv:2802` pins the collision-resolved filename.

## Validation

- `just validate data/habitats/host_associated/anterior_nares__14fc5dcc.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/anterior_nares__14fc5dcc.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed, 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch `just qc`: terminal PASS, including 457 tests, three skipped,
  two dependency warnings; 85 history records; 3,206 strict-valid records;
  32 overlays; curation floor; exact corpus reproduction with zero missing,
  extra or differing records; current site; 231 redirects; 109 term-request
  table entries; final corpus report.
- Current official OLS term and typed-graph requests succeeded. Both live
  GOLD study requests returned 403, so their specimen metadata remain
  unverified. No failed access is treated as inspected evidence.

## Identity and Grounding

Current [UBERON:0005928, external naris](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0005928)
is non-obsolete and includes anterior nares as a synonym, matching vendored
`ontology_terms.tsv:13289`. Its external-opening meaning is compatible
with this human source. The human and mammal leaves tie at depth five,
explaining the seeder's conservative separate minted NARROW records.
That fallback and SEEDED status are not independently defects.

The current [external-naris graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0005928/graph)
asserts subclass naris and surface structure, BFO:0000050 part_of nose, and
RO:0002176 connects nasal cavity. It does not label the connection as part_of
nasal cavity. Vendored subclass edges 11552/11553 agree with the two
subclass parents. The current naris definition describes an orifice; the
nasal-cavity definition describes the space bounded anteriorly by the nares.
Both referenced terms were checked as non-obsolete and agree with vendored
rows 12876/13057. This is positive opening-versus-cavity evidence, not merely
an absent subclass edge.

The complete `nasal_cavity__ae9d5dba.yaml` identifies the other parent,
`habitatmech:GOLD.bcb2f8b7f3`, as whole human Nasal cavity, NARROW beneath
[UBERON:0001707](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001707),
without an authored opening-associated-environment definition. An opening
connecting to the cavity is not a kind of that cavity.

## Evidence

`gold_ecosystem_paths.tsv:763` supplies node 6091, the exact five-level human
path, one source node, three organism assertions and zero study/biosample
assertions. Generated source ID, full path, label, predicate, count and unit
are faithful. The parent's 251 ORGANISM assertions do not belong to this
opening, and three source assertions do not identify three specimens.

Complete scans of 2,562 tree paths, 1,040 bulk rows, 4,587 study rows and
1,587 triads distinguish the two nares tree paths. Only the human path has
bulk row 194, with 129 biosamples, and study rows 378/2209, with
Gs0063646/Gs0136083. The former study lists fifteen paths, the latter six.
The normalized-path counting and first-seen ID behavior in
`scripts/extract_gold_biosamples.py:96-111` were inspected. Later bulk
biosamples are not summed with older tree organism assertions.

Both live study pages returned 403. The committed study-path links are
verified, but individual hosts, specimens and microbial taxa are not. No
nares triad occurs in the full table. The mammal source's zero assertions
do not acquire the human bulk data, and overlapping host scopes do not
justify adding counts or assuming disjoint samples.

The extra source parent is added at `src/habitatmech/seed.py:898-907`.
`docs/CURATION.md` requires strict broader/is-a semantics for this route,
not preservation of arbitrary source-path topology as a superclass.

## Completeness

Ignored-inclusive target/source-parent identifiers, label and filenames were
searched through curation, history, research, prior reviews, raw inventories,
PATHS and RETIRED. No target ITEM decision, definition request, overlay,
session file or earlier exact human-target review was found. The earlier
`20260928T002315Z-anterior_nares.md` is explicitly about the mammal sibling;
its reference to this human path is not a completed human review.

That earlier report was read in full, as were the current mammal sibling and
its nasal-cavity parent. Its M1 already identifies the analogous mammal
source-parent defect. These reference checks are not counted as a new
mammal target review or used to import its counts into the human source.

Full scans of 162 BacDive sources, 3,081 BacDive taxa, 770 parameters,
358 mappings, 58 Madin habitats, 1,378 Madin taxa, 719 PREGO habitats and
8,807 PREGO taxa found no anterior-nares wording or identifier-number
0005928 match. That is a bounded inventory result, not a literature-wide
absence claim. Optional taxa, parameters and graphs are not quotas.
iModulonDB is not applicable: no gene, regulator or expression claim occurs.

## Findings

1. **Major - HM-ANTERIOR-NARES-HUMAN-001:** the human external-naris source
   inherits whole Nasal cavity as an is-a parent, although the supported
   relation is connectivity between an opening and a cavity. Owner:
   `src/habitatmech/seed.py:898-907` or a governed source-specific exclusion.
   Filed with the earlier mammal witness in
   [#1334](https://github.com/CultureBotAI/HabitatMech/issues/1334).

No blocker or minor finding established. The valid external-naris parent,
human source scope, conservative grounding and count semantics are supported.

## Recommended Edits

Correct or exclude the exact human source-parent edge and separately regress
the mammal witness already identified by its earlier report. Preserve
UBERON:0005928, source paths/nodes and their distinct count semantics.
Compare both source concepts at ITEM depth before any exact merge, and do
not move the false cavity edge onto a merged ontology record.

Do not equate opening with cavity, encode connectivity as an equivalence
xref, globally delete GOLD parents or hand-edit generated YAML. A read-only
copy through the actual semantic adapter confirms that removing the human
source parent changes the input by dropping Nasal cavity. Append required
history, inspect guarded canaries and use supported map/site regeneration.
#1217 remains relevant; draft #1218 is not on main.

## Follow-up Checks

Regress both exact source-parent contributions while retaining correct naris
ancestry, source provenance, the human three-ORGANISM assertion and the
mammal absence of a positive count. Check intended statuses, full ancestry,
strict schema, OAK, history, corpus reproduction, map/site/redirect freshness
and QC. Recover live GOLD metadata before making specimen-level assertions.

## Additional Notes

All 489 existing issue bodies and returned comments were searched for exact
keys, UBERON:0005928, nares/naris and nasal-parent wording. Closed #897 is
a report-wording correction; closed #343 repaired nasal-discharge material.
Neither owns these anatomical opening edges, so #1334 was filed. No
scientific input, generated record or history changed; no paid research ran.
