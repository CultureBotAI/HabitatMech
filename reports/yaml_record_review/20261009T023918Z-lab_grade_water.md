# YAML Record Review: Lab-grade water

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/lab_grade_water.yaml`
- Started UTC: 2026-10-09T02:36:51Z
- Finished UTC: 2026-10-09T02:39:18Z
- Verdict: pass with minor issues (0 blocker, 0 major, 1 minor)

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.1b1ec698e7` at
`893f468d11748cef519a6f1191f294af37559d04`: ENGINEERED / UNGROUNDED /
SEEDED. It has one chemical-product parent, one two-node GOLD attestation
and two events. This resumes preliminary work interrupted by publication;
the current record and source routes were checked afresh. The complete
Chemical product parent and separate aquatic Sterile water record were read
as context, not counted as additional reviews.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/lab_grade_water.yaml`: no issues.
- `just validate-strict data/habitats/engineered/lab_grade_water.yaml`:
  one file, zero errors.
- `just verify-corpus`: 3,208 expected/present, zero differences.
- `just validate-history`: 208 valid records.
- `just provenance-check`: 14 inventories and two GOLD sources current.

Full-index `build_corpus()` / `build_document()` reproduced every target
field: one source, zero reviewed sources, no authored definition and no
applied parent exclusion. Full QC was not repeated per read-only record:
the immediately preceding local run and exact-baseline
[queue QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37874456969)
passed all gates with 622 tests and three skips. Baseline
[label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37874456975)
and [vendored sync](https://github.com/CultureBotAI/HabitatMech/actions/runs/37874456962)
also passed. Those gates do not establish sample roles or source equivalence.
No SSSOM/KGX readiness audit was performed.

## Identity and Grounding

The full source-path mint agrees with `PATHS.tsv:1486`. Complete mapping and
claimant indexes give `gold_unmatched`, followed by the CLASS decision at
`curation/decisions.tsv:252`: `curated_confirm_ungrounded_from_gold_unmatched`,
reviewed=False. Native identity, omitted predicate and UNGROUNDED/SEEDED
state faithfully preserve the unresolved source concept.

The parent source GOLD.413b4cb862 is also automatically unmatched, then an
ITEM GROUND decision selects ENVO:2000000 exactly. Primary ENVO defines this
parent as a manufactured chemical mixture produced through chemical
engineering. Laboratory purification supports a manufactured-water reading,
but the source label does not establish a formulation, purity specification
or control-system role. Nor does high purity prove absolute chemical
homogeneity and thereby establish a false mixture parent. Its precise fit
needs source scope; no definite false edge was established here. The
parent's independent Industrial production exclusion does not apply to this
child, and its review status does not transfer.

Primary ENVO distinguishes ENVO:00002006 liquid water, ENVO:00005791 sterile
water, and ENVO:01001042 sterile water environment. The last is a system;
its comment discusses a potentially contaminated negative control. None is
automatically an exact identity for laboratory-grade water. A liquid-water
genus may be useful after material scope is confirmed, but lack of that
optional refinement is not itself a major defect.

## Evidence

- `gold_ecosystem_paths.tsv:1311` contains the exact depth-four path,
  nodes 6221/6222 and zero tree assertion counts. The generated first ID,
  two-node note, full path and count/unit omissions agree.
- `gold_path_biosamples.tsv:107` separately reports 283 BIOSAMPLEs for
  node 6222. `gold_path_triads.tsv:104-106` covers 178 samples and one
  study, with one term per slot, top share 1.00 and one agreeing study:
  broad ENVO:01000249 urban biome, local ENVO:00000469 research facility,
  medium ENVO:00005791 sterile water. All three primary classes were
  inspected. These are different roles and coverage, not three identities
  or a sum of 283 and 178 organisms.
- Exact-field/pipe-member scanning of all 14 raw TSVs found nine study
  memberships. Physical `gold_studies.tsv` lines and path counts are:
  1994 Gs0133511 (10), 2188 Gs0136062 (3), 3321 Gs0150504 (3),
  3938 Gs0154244 (53), 4107 Gs0156789 (4), 4123 Gs0156805 (4),
  4124 Gs0156806 (8), 4240 Gs0159147 (8), and 4250 Gs0159158 (3).
  Every row spans other habitats. They do not identify which study supplies
  the one-study triad cohort or prove a negative-control role. Attempts to
  inspect [Gs0136062](https://gold.jgi.doe.gov/study?id=Gs0136062) and
  [Gs0159158](https://gold.jgi.doe.gov/study?id=Gs0159158) were inaccessible;
  the other seven study pages were not independently inspected. Original
  sample membership and role remain unresolved, not proven absent.
- The all-table scan found no direct target taxon or environmental-parameter
  contribution. The triads must not be promoted into habitat-wide chemical
  measurements, taxonomy or a sterile-state guarantee.
- The current [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths),
  read after resetting worksheet dimensions, confirms node 6222 and the
  exact path at `site data` row 309, with an Unclassified filler. This
  verifies classification, not the historical node 6221 or sample counts.
  The 84,174-byte response SHA256 is
  `3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396`.
- Inspected [ASTM D1193-24 public abstract/scope](https://store.astm.org/standards/d1193)
  distinguishes reagent-water types from additional microbiological grades.
  The inspected [MilliporeSigma laboratory-water overview](https://www.sigmaaldrich.com/US/en/technical-documents/technical-article/water-purification/understanding-lab-water/understanding-water-quality-grades-laboratory-applications)
  distinguishes multiple laboratory-water qualities and uses, including
  blanks and reagent preparation. These sources support separating purity,
  microbial state and use; they do not assign a standard, type, numerical
  limit or preparation method to GOLD's category. The full paid standard
  was not accessed, and no product recommendation is made.
- Complete class elements were reparsed from
  [pinned primary ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl),
  SHA256 `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  The previous Sterile water report was read as historical context, not
  primary evidence or a transfer of that separate record's findings.

## Completeness

Definition, synonyms, xrefs, parameters, taxa, evidence, graphs, discussions
and datasets are empty. No particular purity grade, sterility state,
microbial community or control role should be manufactured to fill them.
iModulonDB is not applicable to the record's assertions.

Ignored-inclusive ID, label/stem, node and exact-path searches covered
curation, history, research, configuration, raw inventories, PATHS/RETIRED
and individual reports. They found the CLASS decision and contextual source
mentions but no target-owned definition, exclusion, overlay, session history,
dossier or prior individual target report in those bounds. Large study rows
were checked structurally rather than omitted from the all-table conclusion.
The first guessed engineered path for Sterile water did not exist; an
ignored-inclusive identifier search located its actual aquatic file.

## Findings

1. **Minor: original-source material and experimental-role scope remains
   unresolved.** The label and classification do not specify a water grade,
   sterile material or control system, while the one-study medium annotation
   cannot define the whole category. This affects later identity and the
   literal mixture-parent assessment. Owners are the exact source decision
   in `curation/decisions.tsv`, an evidence-backed native definition in
   `curation/term_requests.tsv`, and original GOLD sample/source metadata.

Zero blockers and zero major findings. No count error or definite false
parent was established. The finding is not merely an empty optional slot or
the presence of CLASS/SEEDED status.

## Recommended Edits

Recover the category description and sample roles before ITEM curation.
Keep reagent quality, preparation state, environmental material and control
system separate. Retain the native identity if no exact term fits; do not
merge the separate Sterile water record or use a triad majority as an
identity decision. Assess the chemical-product genus against that scope;
use a guarded `curation/gold_parent_exclusions.tsv` row only if its exact
source contribution is shown to be contextual rather than broader.

## Follow-up Checks

Preserve both nodes, complete path, count omissions, separate 283/178 sample
coverages, all nine study memberships and the historical CLASS event. Any
later curation needs focused scope/count regressions, append-only history,
dry seed, inspected canary, strict, provenance/history, label, corpus/site
and full QC. Compare semantic inputs before a real map rebuild. This report
does not authorize status promotion or a scientific edit.

## Additional Notes

Only this report was written. Scientific inputs, generated records/pages,
history and GitHub state were unchanged. The workbook style warning did not
prevent complete reading. Baseline technical checks are reused only for
unchanged files and do not certify scientific interpretation.
