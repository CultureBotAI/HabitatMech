# YAML Record Review: Articular cartilage (human source)

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/articular_cartilage.yaml`
- Started UTC: 2026-10-04T06:29:36Z
- Finished UTC: 2026-10-04T06:33:35Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.c36ec4b6b6`:
HOST_ASSOCIATED, NARROW, SEEDED. It has two parents, one GOLD attestation
with skos:narrowMatch, and one seed event; no definition or count is emitted.
The full path specifies human skeletal-system articular cartilage, distinct
from the mammalian sibling source. The actual `mint` helper reproduces its
key, and `data/habitats/PATHS.tsv:2722` pins its filename.

## Validation

- `just validate data/habitats/host_associated/articular_cartilage.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/articular_cartilage.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch `just qc` passed lint, documentation and raw provenance;
  tests remain running. No terminal local result is claimed at completion.
  History, strict schema, reference/invariant, reproduction, site, redirect
  and term-request checks are included in that command.
- Exact unchanged base `0ab7aeb487d2fa90a66695740c3f5d3451e0b779` passed
  [QC 37182485949](https://github.com/CultureBotAI/HabitatMech/actions/runs/37182485949).
  Its merge-group QC passed 457 tests with three skips and two warnings.
  Green validation does not establish scientific correctness of a source edge.
- Fresh official OLS term JSON and the primary PubMed abstract/identifier
  metadata described below were inspected.
- An in-memory candidate removal using the actual `semantic_text` function
  with `build_context` over the complete corpus changes semantic input.
  No corpus or generated product was written by that comparison.

## Identity and Grounding

The GOLD human source identity is supported. The anti-conflation rule in
`docs/HARMONIZATION.md` keeps the two equally deep human/mammalian source
paths minted and NARROW beneath generic BTO:0001572. The target has no
maintained item decision, so SEEDED is honest; adding a review-status event
alone would not fix its hierarchy.

Current non-obsolete
[BTO:0001572 articular cartilage](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0001572)
agrees with vendored term row 1572: cartilage covering articular surfaces in
synovial joints. It is a defensible broader class for the human-specific
source. Vendored edge 1073 places it under BTO:0000206 cartilage. Preserve
that BTO parent and the source's narrower mapping rather than equating a
human-specific habitat with the generic ontology term.

The other parent, `habitatmech:GOLD.67f49f8b15`, is invalid as is-a.
The complete `bone__234001be.yaml` denotes human Bone, NARROW under
[BTO:0000140 bone](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0000140).
It has no authored environment definition changing that anatomical meaning.
Current bone and [cartilage](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0000206)
definitions agree with vendored rows 142/208 and distinguish these tissues.
Cartilage on a bone is not a kind of bone. The second GOLD pass at
`src/habitatmech/seed.py:898-907` promotes the source-path containment to
a superclass, contrary to `docs/CURATION.md:26`.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:2439` supplies node 6578 and the exact
human path, with zero organism, study and biosample assertions. Omitting
count/unit is consistent with the seeder's nonzero-organism rule. The source
node is classification provenance, not a demonstrated healthy-cartilage
microbiome. Parent bone's 29 organisms are not inherited.

Full structured scans covered all 12 non-ontology source TSVs. The only
articular-cartilage tree rows are this human source and the mammalian
sibling at row 2117, node 6797. None of the 1,040 bulk, 4,587 study or
1,587 triad rows matches the target path or articular wording. The only
non-GOLD word hit is PREGO `BTO:0001686` at row 254, with joint synonyms.
That broader joint row and its counts are not cartilage evidence and must
not be transferred to this target.

Inspected primary [Voytek et al. 1988](https://pubmed.ncbi.nlm.nih.gov/3349117/)
abstract and identifier metadata verify DOI:10.1016/0142-9612(88)90080-4.
Ultrastructural observations of human and rabbit articular surfaces show
staphylococcal attachment to cartilage matrix. This supports a bounded
microbial-site interpretation, not a normal resident microbiome, universal
characteristic taxon or specimen-level identity for GOLD node 6578.
No mechanism, taxon or experimental number is imported into this record.

## Completeness

Ignored-inclusive searches for the identifier, label variants, filename and
source node covered curation, history, research, prior reports, PATHS and
RETIRED. They found the pinned path and sibling path, but no target decision,
term request, overlay, session, research report, prior exact-target review
or redirect. Parent and bone-marrow review reports are not reviews of this
target and cannot establish that its source edge is is-a.

Full source-table scans found no target-specific BacDive, Madin, PREGO or
parameter input beyond the unrelated joint hit described above. Optional
definition, taxa, parameters, mechanisms, discussions and datasets are not
required merely for coverage. iModulonDB is not applicable: there is no gene,
regulator, expression or pathway claim in the target.

## Findings

1. **Major - HM-HUMAN-ARTICULAR-001:** human articular cartilage is made a
   subclass of human Bone by the GOLD source-parent pass. Anatomical
   location/containment is not is-a. Maintained owner: the source-parent
   contribution rule in `src/habitatmech/seed.py` and an appropriately
   scoped maintained curation input. Tracked in
   [#1354](https://github.com/CultureBotAI/HabitatMech/issues/1354).

No blocker or minor finding established. The generic articular-cartilage
ontology parent is supported independently of the false Bone edge.

## Recommended Edits

Correct or exclude only this source-parent contribution through maintained
inputs/rules, preserving minted identity, source node/path, generic BTO
parent/mapping and intended review depth. Do not globally remove GOLD parents,
redefine the Bone record to conceal the mismatch, or hand-edit generated YAML.

The actual adapter comparison removes `broader habitat: Bone` from the
semantic text. This is not a metadata-only fix: governed map/site regeneration
is needed. [#1217](https://github.com/CultureBotAI/HabitatMech/issues/1217)
remains open with a documented unsupported local runtime. Draft #1218 is
still open at `18c93452a789218f5c653d02723d11388d972055`; its exclusion
mechanism is not assumed to be available on main. No scientific fix is
claimed or partially published here.

## Follow-up Checks

Add a regression for removal of this false source edge and retention of
BTO:0001572. Append required curation history, inspect a guarded canary,
run ordinary/strict validation and OAK, prove corpus reproduction, compare
actual semantic inputs, rebuild governed map/site artifacts and pass full
QC. Do not bypass freshness or manufacture coordinates while the runtime
dependency remains unresolved.

## Additional Notes

All 502 existing issue titles, bodies and returned comments were searched
for the exact target/parent IDs, articular-cartilage wording and cartilage/bone
combinations; none matched, so #1354 was filed as a new bounded finding.
The generic mammalian sibling is a separate review, not extra coverage from
this source comparison.

This report does not change records, curation inputs, status, events or
history. No paid research ran. It is not independent PR approval, and the
whole-corpus review remains ongoing.
