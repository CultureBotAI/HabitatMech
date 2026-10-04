# YAML Record Review: Attached/Keratinized gingiva

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml`
- Started UTC: 2026-10-04T08:36:27Z
- Finished UTC: 2026-10-04T08:38:58Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.d672a250b4`:
HOST_ASSOCIATED, UNGROUNDED, SEEDED. This is GOLD's general-Mammals path,
not the separately reviewed human path. General Mammals is not assumed
to mean exclusively nonhuman mammals. The record has one Oral cavity
parent, one GOLD attestation, a CLASS-level decision event and a seed
event. No definition, synonyms, positive count, taxa, parameters, graphs
or datasets is emitted. PATHS.tsv:2874 pins the stem. The actual mint
helper reproduces the identifier from the full source path.

## Validation

- `just validate data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/attached_keratinized_gingiva__a8c3d27a.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch `just qc`: lint, docs, provenance, 457 tests, 90 history
  records, 3,206 strict-schema records, 32 overlays, curation floor,
  exact corpus and generated site passed. Tests had three skips and two
  dependency warnings, taking 621.73 seconds. Redirect and final checks
  are still running at report completion; no terminal full-QC result
  is claimed here.
- The unchanged scientific baseline `a7acd01cd4958003420b697f1c2ef859a9b369f9`
  also passed [post-push QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37188660479).
  This is not final-head CI for the new report.
- Current official OLS terms and typed graph were inspected in this batch;
  primary pig-jaw histology was inspected through official PMC XML.
  A separate full-context semantic comparison for this target confirms
  its parent removal changes text.

## Identity and Grounding

`curation/decisions.tsv:1184` is CLASS-level CONFIRM_UNGROUNDED. It records
lexical nonmatching and explicitly does not assess habitat eligibility.
It neither warrants a novel-term submission nor falsely claims ITEM
review; SEEDED preserves the limited review depth.

Attached gingiva denotes a physical tissue/site. Current active
[UBERON:0001828 gingiva](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001828)
describes fibrous tissue investing teeth, matching ontology_terms.tsv:13075.
Its typed graph subclasses it to current
[UBERON:0003729 mouth mucosa](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0003729),
as does vendored subclass row 11262. Part-of and adjacency edges are
separate relation types, not additional superclasses.

Bounded current BTO/UBERON/ENVO searches found related anatomical terms
but no exact match to the full compound label. Attached-gingiva query
hits included adjacent alveolar mucosa and an attachment-zone complex;
keratinized-gingiva hits included gingiva and gingival epithelium.
These candidates do not license an exact merge with generic gingiva,
the groove, an epithelium or an adjacent structure. Nor does a human
protocol's operational naming settle all anatomical usages of the slash.

The complete parent `oral_cavity__2e0f1569.yaml`,
`habitatmech:GOLD.92d1e65695`, is general-mammal Oral cavity, NARROW
under [UBERON:0000167](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000167).
The current active term agrees with vendored row 12911 on an anatomical
cavity. The parent has no authored oral-surface-environment definition.
Gingival tissue is not a subtype of that cavity. The source-parent pass
at `src/habitatmech/seed.py:898-907` introduces the link from GOLD nesting,
contrary to the strict broader/is-a contract.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:2017` gives the exact mammal path,
one node (gold.ecosystem:6714) and zero organism, study, biosample and
total assertions. The emitted absence of a positive count/unit is correct
for this tree snapshot. The parent's 270 organisms are not observations
from this leaf and must not be transferred.

Complete scans found no exact general-mammal path in 1,040 bulk-biosample
rows, 4,587 studies or 1,587 triads. The shared-label hits are only for
the human path: seven biosamples, two study memberships and a one-sample
triad with gingiva local and saliva medium. None belongs to this target
by virtue of the identical leaf label. No sample-level provenance or
named mammal species is invented for node 6714.

The primary [pig-jaw study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7048786/),
PMID:32111855, DOI:10.1038/s41598-020-60291-0, distinguishes attached
gingival tissue from adjacent mucosa histologically in a five-jaw model.
Its attached region includes epithelium and underlying connective tissue;
the measured keratinized-tissue width extends to the free gingival margin.
This supports a tissue interpretation and cautions against treating all
keratinized tissue as identical to the attached region. It is not a
microbiome experiment, evidence about every mammal, or a GOLD occurrence.

The inspected [historical HMP sampling protocol, section 7.3.1.6](https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/document.cgi?phd=2235&study_id=phs000228.v3.p1)
provides a human example of attached-gingiva soft-tissue sampling separate
from saliva and plaque. That example is not extrapolated to all mammal
species or imported as a target dataset. No taxa, abundances, clinical
measurements or causal mechanisms are added.

## Completeness

Ignored-inclusive searches covered the target and parent keys, node,
label and stem across curation, history, research, PATHS, RETIRED and
reports. They found the CLASS row and pinned paths but no target ITEM
decision, authored definition, overlay, curation session, research report,
redirect or prior exact target review. A neighboring gingival-crevice
research report only mentions the parent; it is not target evidence.

All 12 non-ontology inventories were scanned fully with exact path and
target/source/attached-gingiva wording. Only the target tree row and
human-side matches described above were found. No matching BacDive,
Madin, PREGO, mapping or environmental-parameter row was found across
their 162/3,081/770/358/58/1,378/719/8,807 rows. This bounded search is
not absence under every synonym or specimen label.

No optional field needs filling merely for coverage. The record claims
no gene, regulator, pathway or expression dataset; iModulonDB is not
applicable, and its absence is not negative habitat evidence.

## Findings

1. **Major - HM-GINGIVA-D672A250B4-001:** the whole mammal Oral cavity
   is emitted as an is-a superclass of gingival tissue. The contribution
   originates in `src/habitatmech/seed.py`; a supported definition in
   `curation/term_requests.tsv` can own replacement, with scoped
   source-parent handling as an alternative. Added as a separate witness to
   [#1363](https://github.com/CultureBotAI/HabitatMech/issues/1363#issuecomment-5978179567).

No blocker or minor finding established. Lack of an exact term does not
justify NOT_APPLICABLE for this physical site.

## Recommended Edits

Correct or exclude the exact cavity contribution through maintained
rules/inputs, preserving source identity, path/node and count semantics.
Use ITEM curation to define the intended attached/keratinized site and
justify any tissue/surface genus. The existing definition-owned
`curation/term_requests.tsv` `parent_mode=REPLACE` route can replace the
current parent set once the supported definition notes establish that
every inherited parent is false. This record currently has only the
false cavity parent. The route is documented in `docs/CURATION.md:152-164`
and implemented in `src/habitatmech/seed.py:423-447`; new exclusion
machinery is not required. Without a supported definition/genus, use
scoped source-parent handling instead. Never invent a definition just
to use REPLACE or remove an otherwise valid inherited parent.

Do not equate related anatomical terms,
merge the human bin on its label, or encode containment as an equivalence
xref. Append history for actual curation; do not patch generated files.

The actual adapter comparison removes `broader habitat: Oral cavity`
and changes semantic text. Use the real governed map/site rebuild in
[#1217](https://github.com/CultureBotAI/HabitatMech/issues/1217), not a
checksum or freshness bypass. Protected draft #1218 remains unmerged
and untouched; its proposed mechanism is not treated as present on main
or required for the existing definition-owned REPLACE route.

## Follow-up Checks

Regress the exact false parent and retained source facts. Run dry seed,
guarded canary and visual record inspection; require ordinary/strict
schema, OAK, provenance/history, exact corpus reproduction, map/site
freshness and full QC. Revisit sample-level evidence before assigning
taxa or merging host-specific sources. Preserve pinned URL behavior.

## Additional Notes

The prior full scan of 508 issue titles, bodies and returned comments
included this exact source key and compound label. No repair owner was
found then; newly created #1363 was re-read before adding this witness.
The existing buccal-mucosa count issue #503 is not this parent correction.

No scientific input, generated artifact, status, event or history changed.
No paid research ran. Full-corpus review remains ongoing.
