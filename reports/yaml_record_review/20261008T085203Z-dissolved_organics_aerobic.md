# YAML Record Review: Dissolved organics (aerobic)

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/dissolved_organics_aerobic.yaml`
- Started UTC: 2026-10-08T08:47:59Z
- Finished UTC: 2026-10-08T08:52:03Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.17461837d0`
at `9260067e6d32d02b582eebe9861e7c2fcfc76f1f`. Its exact source path is
`Engineered > Wastewater > Nutrient removal > Dissolved organics (aerobic)`.
It is ENGINEERED / UNGROUNDED / SEEDED, with one parent, one GOLD
attestation and two generated history events. There is no definition,
synonym, xref, parameter, named taxon, literature item, graph, discussion
or dataset. The anaerobic sibling and the Activated sludge child are
distinct records, not alternative targets for this review.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/dissolved_organics_aerobic.yaml`:
  no issues.
- `just validate-strict` on the same target: one file, zero errors.

Read-only `build_corpus` / `build_document` reproduces every target field,
with one source concept and zero ITEM-reviewed sources. Actual default and
curated resolutions for target and immediate source parent were executed
with complete ontology, normalized mapping and both claimant indexes.

Fresh session-wide gates reused here passed: `just verify-corpus` reproduced
all 3,207 records; `just validate-history` validated 176 histories;
`just provenance-check` passed 14 inventories and two GOLD sources. Full QC
was not repeated for report-only changes. The exact baseline passed
native-queue [QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37748712190)
and [label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37748711526),
plus preceding full local QC: 581 passed, three skipped, all gates passed.
Those gates do not resolve habitat denotation or convert source-path context
into a strictly broader class. Original GOLD re-extraction and independent
study/sample verification were unavailable within the bounds below. No
standalone literature-reference validator applies to this citation-free record.

## Identity and Grounding

The full-path mint and `PATHS.tsv:1446` agree. Default resolution is
`gold_unmatched`, retained by the CLASS CONFIRM_UNGROUNDED row at
`curation/decisions.tsv:227`. No ontology mapping predicate is asserted.
The CLASS and seeding events correctly preserve SEEDED rather than claiming
ITEM review.

The source label does not say which physical entity is being represented.
It can be read as dissolved organic material under an oxygen condition, a
treatment function, or an aerobic treatment environment containing wastewater
and biomass. These readings have different identities and parents. The
classification path and its Activated sludge child make a treatment-context
reading plausible, but do not establish that the target is a reactor vessel,
its liquid contents, or another treatment setting.

Read the entire immediate parent `nutrient_removal.yaml`,
`habitatmech:GOLD.a18a70ae30`. Its default is also unmatched, retained by
its CLASS row at line 938; it has no definition and is parented to waste
water. The target's link to it is generated solely by the GOLD source-path
pass. The parent label denotes a treatment function in ordinary engineering
usage, while its intended HabitatMech entity remains unstated. Source-tree
membership therefore does not settle the required strict habitat-parent
meaning.

Fresh [official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
inspection checked these nearby classes and found no deprecation assertion:

- ENVO:00002126 aerobic bioreactor: a bioreactor with well-oxygenated contents.
  It could be a broader genus only after a reactor reading is established;
  it does not itself specify wastewater or dissolved-organic removal.
- ENVO:00002001 waste water: anthropogenically degraded water, a possible
  material context rather than an automatic exact identity for a treatment unit.
- ENVO:00002046 activated sludge and ENVO:00002043 wastewater treatment
  plant: current labels verified, but no definition text was returned from
  their inspected IAO definition slots. Neither label alone resolves this
  target, which is above a sludge child and below a treatment classification.
- ENVO:06105300 wastewater treatment process: explicitly a recycling
  process, not a habitat identity.

No exact target has been established by this candidate inspection; no global
absence of an appropriate ontology term is claimed. An oxygen adjective is
not itself a habitat, and an available reactor genus must not decide the
system-versus-material question merely because it is convenient.

## Evidence

An exact-field/pipe-member scan of all 14 raw TSVs found:

- `gold_ecosystem_paths.tsv:1411`: depth four, nodes 3829 and 4258, and
  zero organism/study/biosample/total tree counters. The first-node display
  and two-node note reproduce correctly.
- `gold_path_biosamples.tsv:448`: 27 BIOSAMPLE observations for node 4258.
- `gold_studies.tsv:615`: Gs0111359, with this exact path, its separate
  Activated sludge child, and river sediment as three path memberships.

The seeder emits organism count/unit only when that counter is nonzero.
Their omission is correct, not an assertion of sterile material or no samples.
Separate biosample inventory counts do not repair an ORGANISM counter by
substitution. The child path's fifteen biosamples are not automatically added
to this target's twenty-seven. A study spanning river sediment and treatment
categories does not equate those environments. No exact target taxon,
physicochemical-parameter or MIxS-triad row was found.

The current [GOLD classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
confirms node 4258 at `site data` row 457 with this path and an Unclassified
filler. Row 456 contains node 4257 for the Activated sludge child. This
establishes current source classification, not historical node 3829 or
sample-level treatment conditions. The live
[Gs0111359 page](https://gold.jgi.doe.gov/study?id=Gs0111359) was inaccessible,
and an exact-accession search yielded no usable primary study text. The
study and sample context therefore remain inventory-backed.

The primary [EPA Municipal Nutrient Removal Technologies Reference Document](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P100GE8B.TXT),
EPA 832-R-08-006, Chapter 1.1, distinguishes conventional secondary
biological treatment from additional nitrogen/phosphorus removal. This
supports caution about treating a carbon/organic-removal duty as proof of
a nutrient-removal habitat genus. It does not prove how GOLD intended its
broader bucket, and it does not establish the performance or design of these
samples. No regulatory, cost or quantitative treatment claim is taken from it.

The entire generated anaerobic sibling was read. Its ITEM decision and
authored reactor definition are local curation, not independent evidence
for the aerobic target. The sibling's committed research report was inspected
as a lead: its denotation/boundary sections acknowledge that choosing a
reactor rather than its contents is an inference from the path structure.
That uncertainty must not disappear when reusing the report. Its proposed
anaerobic physiology and operating constraints were not copied into this
aerobic record.

## Completeness

Ignored-inclusive searches covered target ID, full path, label/slug, both
source nodes and parent ID across curation, raw inventories, path/retirement
registries, configuration, docs, tests, history, research, its manifest and
prior reports. They found the CLASS row and source context, but no
target-owned definition, parent exclusion, overlay, research report, session
history, retirement or previous individual review within those bounds.
Research and curation for the anaerobic sibling mention this target; they
do not constitute its own completed curation. Prior child review is likewise
not an individual assessment of this parent record.

The session's ignored-inclusive filename traversal of `build`, `data/raw`
and configured kg-microbe `data` found no original GOLD node/edge dumps,
goldData.xlsx or searched biosample JSONL intermediate. The public
classification workbook does not replace the missing biological inputs.
No named organism, gene, regulator or expression dataset makes iModulonDB
applicable. Optional taxa and mechanisms should remain empty; the consequential
gap is the entity boundary and resulting hierarchy, not empty optional biology.

## Findings

Zero blockers, one major finding, zero minor findings.

1. **Major: material, treatment-function and treatment-environment readings
   remain unresolved while a strict habitat-parent relation is published.**
   The bare process-condition label, undefined Nutrient removal parent and
   heterogeneous source context do not identify a defensible physical genus.
   This is not a finding merely because the record is SEEDED, nor proof that
   its source ID is wrong. It is a consequential identity/hierarchy ambiguity
   requiring source-specific assessment. Owners: the exact target and parent
   rows in `curation/decisions.tsv`, evidence-backed habitat definitions in
   `curation/term_requests.tsv`, and a guarded source-parent exclusion in
   `curation/gold_parent_exclusions.tsv` if the edge proves contextual.

## Recommended Edits

Recover source/sample descriptions and decide whether this bin denotes an
aerobic wastewater treatment environment, a sampled material, or only a
process/analytical category. Keep the source mint while assessing that choice.
If a habitat is supported, define its physical boundary with an appropriate
current material or environment genus and only supported differentia. If
the source is purely a non-habitat process category, use a justified
NOT_APPLICABLE decision rather than manufacturing a reactor.

Review Nutrient removal independently as the claimed broader habitat. If
it is only treatment context, the existing guarded exclusion can remove this
source-path contribution while retaining the full attestation. Do not infer
a false edge solely from EPA's terminology, copy the anaerobic definition,
replace oxygen words mechanically, import a sludge-only design, or merge
source bins without evidence. Preserve nodes, sample-unit distinctions and
honest lifecycle until the ITEM work is actually done.

## Follow-up Checks

Regress exact source-path resolution, both source nodes, omitted organism
count/unit, separate 27-sample context, Gs0111359's three memberships and
distinction from the Activated sludge child and anaerobic sibling. Check any
chosen genus against current ontology definition and ancestry, not just its
label. A guarded exclusion must name the exact path and expected resolved
parent `habitatmech:GOLD.a18a70ae30` and reject stale resolution.

If curation is authorized, append truthful history, dry-seed, inspect a
canary, regenerate affected outputs and run strict/provenance/history/label/
corpus/full QC. Label or identity changes require the documented post-commit
redirect workflow; semantic changes require complete map-input comparison.
This review does not certify SSSOM/KGX readiness.

## Additional Notes

Only this new target report was written. Scientific inputs, generated
records/pages, statuses, session history and GitHub were unchanged. No paid
research or delegation. The EPA text endpoint was readable when its PDF
endpoint failed; only the relevant inspected sections inform this review.
Fresh workbook: 84,174 bytes, SHA256
`f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
Fresh ENVO OWL: 9,614,229 bytes, SHA256
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
