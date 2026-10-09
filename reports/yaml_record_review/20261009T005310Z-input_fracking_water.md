# YAML Record Review: Input fracking water

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/input_fracking_water.yaml`
- Started UTC: 2026-10-09T00:50:40Z
- Finished UTC: 2026-10-09T00:53:10Z
- Verdict: pass with minor issues (0 blocker, 0 major, 1 minor)

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.333af3f6ef`
at `b8a0a7bd659e3bb8e4aa9c9ce08d56ced830f66d`: ENGINEERED / UNGROUNDED /
SEEDED, one chemical-product parent, one collapsed GOLD attestation and two
events. This review resumes earlier preliminary work but rechecks the current
record, source routes and evidence against the merged baseline. The separate
aquatic and terrestrial Fracking water records and returned/produced-water
records are not this target. The complete chemical-product parent was read
for context, not counted as another completed review.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/input_fracking_water.yaml`: no issues.
- `just validate-strict data/habitats/engineered/input_fracking_water.yaml`:
  one file, zero errors.
- `just verify-corpus`: 3,208 expected/present, zero missing/extra/differing.
- `just validate-history`: 207 valid records.
- `just provenance-check`: 14 inventories and two GOLD sources current.

Full-index in-memory `build_corpus()` and `build_document()` matched the
entire parsed target: one contributor, zero ITEM-reviewed contributors, no
authored definition and no target-owned GOLD-parent exclusion. Full QC was
not rerun per record: the immediately preceding publication passed 621 tests,
three skips and all local gates; native queue [QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37865912182)
and [label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37865912102)
passed on this exact baseline. No tracked input or implementation changed
during this review. Labels/schema/reproduction do not validate original
sample composition or certify a native concept's material-stage boundary.
No SSSOM/KGX audit or original sample-member reconstruction was performed.

## Identity and Grounding

The source-path mint agrees with `PATHS.tsv:1663`. Complete mapping and
claimant indexes give `gold_unmatched`, followed by the CLASS decision at
`curation/decisions.tsv:380`: `curated_confirm_ungrounded_from_gold_unmatched`,
reviewed=False. Keeping the native ID, UNGROUNDED/SEEDED status and absent
mapping predicate is consistent. CLASS status alone is not a defect, and the
generated caveat correctly says habitat identity was not item-assessed.

The sole parent is contributed by GOLD's immediate Chemical products path,
source mint `habitatmech:GOLD.413b4cb862`. Its default is also unmatched;
its ITEM GROUND selects ENVO:2000000. Inspected [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
defines that parent as a manufactured chemical mixture. Formulated input
fluid can fit that material scope; unmixed source water need not. The parent's
separate exclusion of its Industrial production context does not exclude
this child's chemical-product edge or transfer the parent's review status.

ENVO:01001869, fracking liquid, is a relevant material candidate already in
`ontology_terms.tsv:9360`. Primary ENVO describes water-based liquid amended
with thickening agents and proppants; its `fracking water` alias is narrow,
not exact. The target emits no such alias, so there is no demonstrated synonym
scope defect in this record. ENVO:01001868 hydraulic fracturing is a process,
not an alternative material identity. Neither candidate establishes exact
equivalence for the input-stage GOLD category merely through spelling.

## Evidence

- `gold_ecosystem_paths.tsv:1310` has the exact depth-four path, nodes
  5877/5878 and zero direct organism/study/biosample/total assertions. The
  first source ID, two-node note, path and count/unit omissions are faithful.
  The parent record's ten ORGANISM assertions are not target observations.
- `gold_path_biosamples.tsv:874` independently records two BIOSAMPLEs for
  node 5878. These must not be converted into two organisms or treated as a
  contradiction of the separate extraction's zero direct counts.
- `gold_path_triads.tsv:101-103` covers two samples and one study, with one
  distinct term per slot and top share 1.00: broad ENVO:01000219 anthropogenic
  terrestrial biome; local ENVO:02500027 anthropogenic environmental process;
  medium ENVO:01001869 fracking liquid. Complete primary class elements were
  parsed and their labels/roles verified. The medium supports a formulated-
  fluid candidate for these samples, not automatic whole-category identity.
- Primary [ENVO/MIxS guidance](https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS)
  separates environmental system, local surrounding entity and sample material.
  The local process annotation does not fit the recommended countable-entity
  role and warrants sample-level checking. It is not imported as target
  identity or an ecological assertion, so it is not a second record defect.
- `gold_studies.tsv:859` links Gs0114675 to this path and five other paths,
  including produced/flowback water, lake, tank, wetlands and rumen fluid.
  Study membership is not evidence that those contexts or their organisms
  belong to the target. Opening the [GOLD study](https://gold.jgi.doe.gov/study?id=Gs0114675)
  returned a request-processing error. Indexed study metadata supplied leads,
  but was not substituted for inspected sample records or used to assign taxa.
- The current [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths),
  parsed with worksheet dimensions reset, confirms the exact path at `site
  data` row 308, node 5878, with a final Unclassified filler. It confirms
  current classification, not historical node 5877, sample contents or counts.
  Its 84,174 bytes have SHA256
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
- The inspected [EPA water-cycle description](https://www.epa.gov/hfstudy/hydraulic-fracturing-water-cycle)
  distinguishes acquiring source water, mixing formulated fluid, injection,
  returned-water handling and disposal/reuse. This supports keeping stages
  distinct; it does not identify the stage or composition of GOLD's two samples.
  The parsed ENVO source SHA256 is
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.

## Completeness

Definition, synonyms, xrefs, parameters, taxa, literature evidence, graphs,
discussions and datasets are empty. None should be invented from two anonymous
sample annotations or other paths in the same study. iModulonDB is not
applicable to this record's claims. No count, process, recipe or environmental
condition is justified by the generic word fracking.

Ignored-inclusive ID, stem/label and study searches covered curation, history,
research, configuration, all raw inventories, PATHS/RETIRED and individual
reports. They found the CLASS row and contextual sibling/study discussions,
but no target-owned authored definition, exclusion, causal overlay, session
history, dossier or earlier individual target review in those bounds. An
exact-field/pipe-member scan of all 14 raw TSVs recovered the rows above and
no direct target taxon or physicochemical-parameter row. These are bounded
inventory findings, not a claim that original sample records do not exist.

## Findings

1. **Minor: the input-stage material scope lacks item-level provenance.**
   Chemical-product parentage is plausible for formulated fluid, while the
   unqualified input-water reading could include source water before mixing.
   Two medium annotations support a candidate but do not settle the complete
   source category. The unavailable study detail leaves that distinction
   unresolved. This is a non-blocking provenance/scope gap, not proof that
   the parent is false, not a demand to fill every optional field, and not
   a finding based solely on CLASS/SEEDED status.

Zero blockers and zero major findings. No forced exact mapping, parent
deletion, returned-water merge or NOT_APPLICABLE judgement is established.

## Recommended Edits

Recover the two original sample descriptions and the GOLD category's intended
scope before item-level curation. A justified identity decision belongs under
GOLD.333af3f6ef in `curation/decisions.tsv`; a retained native term's supported
definition belongs in `curation/term_requests.tsv`. Preserve the input-stage
modifier and separate material from process, source water and returned water.
Only if evidence disproves the chemical-product subsumption should a guarded
row in `curation/gold_parent_exclusions.tsv` suppress that source contribution.
Source triad corrections belong in the governed GOLD extraction inputs.

## Follow-up Checks

Check original sample IDs, stage, additives/proppant context and the anomalous
local-process annotation without transferring study-wide taxa or counts.
Re-evaluate candidate relation direction against typed ENVO. After separately
authorized curation, append history, dry-seed, inspect a target canary and run
strict, history/provenance/label, corpus/site and full QC. Compare full semantic
inputs before any necessary real map rebuild. Do not hand-edit generated YAML.

## Additional Notes

Only this new report was authored; no scientific input, generated product,
history, lifecycle or GitHub state changed. Workbook loading emitted a default-
style warning, but all rows were read. The all-table scan handled surplus CSV
cells rather than failing on the unrelated existing biosample overflow row.
The separate earlier Fracking water review is context, not primary evidence
and not a review of this exact source concept.
