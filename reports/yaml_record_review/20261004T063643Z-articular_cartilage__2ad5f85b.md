# YAML Record Review: Articular cartilage (mammalian source)

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/articular_cartilage__2ad5f85b.yaml`
- Started UTC: 2026-10-04T06:34:16Z
- Finished UTC: 2026-10-04T06:36:43Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.ee0d0ceedd`:
HOST_ASSOCIATED, NARROW, SEEDED. It has two broader-parent assertions,
one GOLD attestation with skos:narrowMatch and one seed event. The source
is the mammalian articular-cartilage path, not the separately represented
human path. The actual `mint` helper reproduces its ID;
`data/habitats/PATHS.tsv:3056` pins the disambiguated filename.

## Validation

- `just validate data/habitats/host_associated/articular_cartilage__2ad5f85b.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/articular_cartilage__2ad5f85b.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch `just qc`: 457 tests passed, three skipped, two warnings;
  90 valid history records; 3,206 strict-valid records; 32 valid graph
  overlays; exact corpus reproduction; current site, redirects and
  term-request table. Its final corpus analysis is still running, so no
  terminal full-QC result is claimed at report completion.
- Current official BTO JSON and the primary PubMed abstract/identifier
  metadata were inspected during this batch. The source and parent record
  were separately read for this target.
- An in-memory candidate removal with the actual semantic adapter and full
  corpus context changes semantic text. No generated record was written.

## Identity and Grounding

The exact GOLD source denotes mammalian articular cartilage. The tied,
equally deep human/mammalian leaf paths explain the anti-conflation rule's
minted NARROW identities. Generic
[BTO:0001572 articular cartilage](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0001572)
is a valid broader class, matching vendored row 1572 and the source's
skos:narrowMatch. The source is not reviewed at ITEM depth; SEEDED does
not itself constitute a defect.

The complete `bone__8d0df242.yaml`, ID `habitatmech:GOLD.28cfbd7dee`,
denotes mammalian Bone under
[BTO:0000140 bone](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0000140),
not an authored broader bone-associated environmental class. Current BTO
definitions distinguish cartilage covering articular surfaces from hard
mineralized bone tissue. The vendored articular-cartilage subclass at row
1073 instead points to
[BTO:0000206 cartilage](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0000206).
All three current terms are non-obsolete and agree with the slice.

Articular cartilage is not a kind of Bone. The source-path pass at
`src/habitatmech/seed.py:898-907` promotes the GOLD anatomical context
to is-a, contrary to `docs/CURATION.md:26`. Preserve the valid BTO parent
while correcting this independent source-parent contribution.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:2117` records node 6797 on
Host-associated > Mammals > Skeletal system > Bone > Articular cartilage,
with zero organism, study and biosample counts. The emitted ID/path and
omitted count/unit follow that source and the seeder's nonzero count rule.
Parent bone's two-node provenance is separate from this one-node target.

Full exact-path comparisons covered 2,562 tree rows, 1,040 bulk rows,
4,587 study path lists and 1,587 triads. Only the tree row matches. The
earlier full articular-word scan of all 12 non-ontology source tables
found the two cartilage tree paths and one PREGO joint-synonym row:
`prego_habitats.tsv:254`, BTO:0001686. A joint is not articular cartilage,
so its taxa and counts are not this record's evidence.

The inspected primary [Voytek et al. 1988](https://pubmed.ncbi.nlm.nih.gov/3349117/)
abstract and identifier metadata verify DOI:10.1016/0142-9612(88)90080-4.
The authors report staphylococcal attachment to cartilage matrix on human
and rabbit articular surfaces. This is bounded support for an anatomical
microbial site, not a universal mammalian resident microbiome, a GOLD
specimen identity, or proof that cartilage is bone. No study-derived taxa,
numbers or causal claims are imported.

## Completeness

Ignored-inclusive searches of curation, history, research, prior reports,
PATHS and RETIRED used the target ID, parent ID, source node, label variants
and filename. They found the pinned path, older parent/bone-marrow reports
and this batch's human-cartilage report, but no maintained target decision,
term request, causal overlay, session, target research report, redirect or
prior exact-target review. Mentioning this record as a sibling is not a
completed review of it.

Optional definition, parameters, taxa, evidence, mechanisms, discussions and
datasets can remain absent. No source evidence justifies filling them for
coverage. iModulonDB is not applicable: the target makes no gene,
regulatory, expression or pathway assertion.

## Findings

1. **Major - HM-MAMMAL-ARTICULAR-001:** the target's mammalian Bone parent is
   not a strictly broader habitat. Its source-path context has been promoted
   to an incorrect superclass. Maintained owner: the GOLD source-parent
   rule in `src/habitatmech/seed.py` and an appropriately scoped maintained
   curation input. Added as a second independently checked target to
   [#1354](https://github.com/CultureBotAI/HabitatMech/issues/1354#issuecomment-5977365839).

No blocker or minor finding established. This is the same root cause as the
human case, not a reason to merge the two source identities.

## Recommended Edits

Correct or exclude only this source-parent contribution, retaining ID,
source node/path, generic BTO:0001572 parent, narrowMatch and intended
status. Do not hand-edit generated files or globally drop source parents.

The actual candidate comparison removes `broader habitat: Bone` from the
semantic input. A governed map/site rebuild is required; the unresolved
runtime dependency in [#1217](https://github.com/CultureBotAI/HabitatMech/issues/1217)
applies. Draft #1218 remains unmerged and unchanged. No scientific fix or
partial stale product update is claimed here.

## Follow-up Checks

Extend the scoped regression to both human and mammalian source keys,
assert retained BTO parent/mapping, append curation history, inspect a guarded
canary and pass strict validation, OAK, corpus reproduction and full QC.
Compare actual semantic inputs and rebuild map/site artifacts without
changing pins, fabricating coordinates or bypassing freshness checks.

## Additional Notes

All 503 current issue titles, bodies and returned comments were searched
for the exact second target/parent keys and articular-cartilage wording.
Only #1354 matched; its title was broadened and this second case was added
instead of creating a duplicate issue.

No generated record, curation input, status, event or history changed.
No paid research ran. This is not independent PR approval. Whole-corpus
review remains ongoing.
