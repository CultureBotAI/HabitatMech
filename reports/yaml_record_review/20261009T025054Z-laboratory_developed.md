# YAML Record Review: Laboratory developed

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/laboratory_developed.yaml`
- Started UTC: 2026-10-09T02:40:37Z
- Finished UTC: 2026-10-09T02:50:54Z
- Verdict: pass with minor issues (0 blocker, 0 major, 1 minor)

## Target

Read the complete generated HabitatRecord `habitatmech:GOLD.77c5518fff` at
`893f468d11748cef519a6f1191f294af37559d04`: ENGINEERED / UNGROUNDED /
SEEDED. It has one native Engineered parent, one four-node GOLD attestation,
56 ORGANISM assertions and two events. The complete Engineered parent and
Genetically modified child were read as context, not counted as additional
reviews. This target is not Lab culture, a laboratory facility or the
separate Lab synthesis branch.

## Validation

- Fresh `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/laboratory_developed.yaml`:
  no issues.
- Fresh strict validation with the same cache setting: one file, zero errors.
- Full-index `build_corpus()` / `build_document()` reproduced every target
  field: one contributor, zero reviewed contributors, no authored definition
  and no applied GOLD-parent exclusion.
- Fresh shared session gates passed: 3,208 records reproduce with zero
  differences; 208 histories valid; 14 inventories and two GOLD sources current.
- Full QC was not repeated per read-only record. The unchanged baseline's
  local run and [exact-baseline queue QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37874456969)
  passed all gates with 622 tests and three skips. Baseline
  [label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37874456975)
  and vendored sync passed too. These checks do not prove native habitathood
  or recover original organism membership.

No SSSOM/KGX audit was performed. No target ontology identity, taxon,
literature evidence or graph claim requires a separate identifier check.

## Identity and Grounding

The exact source-path mint agrees with `PATHS.tsv:2171`. Actual resolution
with complete mapping and claimant indexes is `gold_unmatched`, then the
CLASS row at `curation/decisions.tsv:713` produces
`curated_confirm_ungrounded_from_gold_unmatched`, reviewed=False. Native
identity, absent predicate and UNGROUNDED/SEEDED status are faithfully emitted.
The CLASS caveat explicitly does not endorse habitathood.

The immediate Engineered source, GOLD.2acb39dd08, also resolves unmatched
and CLASS-confirmed through `decisions.tsv:332`. It has no authored genus
definition. Laboratory development is compatible with engineered provenance,
but provenance alone does not establish a strictly broader habitat. Conversely,
the undefined wording alone does not prove a particular false habitat edge.

The neighboring Genetically modified source GOLD.2eecc8ad2c is explicitly
ITEM NOT_APPLICABLE: an organism qualification, not its surroundings. Its
former Laboratory developed parent contribution was already excluded by
`curation/gold_parent_exclusions.tsv:9`; the complete current child has no
parent and retains NOT_APPLICABLE/REVIEWED. That bounded child correction
does not classify all 56 direct parent assertions or authorize a blanket
non-habitat decision for this target. The older child report was read as
historical context; its pre-fix parent finding is not a current target defect.

## Evidence

- `gold_ecosystem_paths.tsv:292` contains the exact depth-two path, nodes
  4385/4727/4728/4729 and 56 ORGANISM assertions. The generated first ID,
  four-node note, source label/path and count/unit agree. These are neither
  distinct species nor 56 development procedures.
- Exact-field/pipe-member scanning of all 14 raw TSVs found only that
  ecosystem row for this target. No direct target study, biosample, triad,
  taxon or environmental-parameter contribution was found in those inputs.
  The child's 1,704 ORGANISM assertions and root's 68 are separate scopes.
- Fresh [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  parsing with worksheet dimensions reset confirms node 4729 at `site data`
  row 352, with three Unclassified fillers. Row 351 instead represents
  the Genetically modified child, node 4726. The 84,174-byte response SHA256
  is `3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396`.
  It confirms current branch structure, not historical nodes or counts.
- The fresh [GOLD organism-tree JSON](https://gold.jgi.doe.gov/download?mode=organismEcosystemsJson)
  has 1,738 organisms across this branch: 1,686 in Genetically modified and
  52 in Unclassified. The latter continues through Unclassified fillers.
  These live aggregate/subgroup counts must not replace the pinned direct
  56-assertion inventory or be described as the same population. Response:
  1,450,415 bytes, SHA256
  `49ef0a3e654a79f6b7e7140d2cdb2ac0ce0bb1df2ccb8decae68d129eeb7ca11`.
  Both the linked full-branch and Unclassified-member search pages were
  inaccessible through the browser tool. Member-level scope remains unresolved.
- The inspected [GOLD classification guide](https://gold.jgi.doe.gov/ecosystem_classification)
  describes a sample-driven, revisable five-level grouping of collection
  surroundings. Its broad purpose is not a guarantee that each grouping
  is formal habitat subsumption or a definition of Laboratory developed.
- The inspected [NHGRI GMO glossary](https://www.genome.gov/genetics-glossary/Genetically-Modified-Organism-GMO)
  distinguishes genome modification of an organism from its surroundings.
  This supports caution about the child branch, not a claim about a specific
  gene, species, modification or physical environment among the direct
  parent members. No experimental procedure was imported.

## Completeness

Definition, synonyms, xrefs, parameters, taxa, evidence, graphs, discussions
and datasets are empty. No development method, genotype, organism, medium,
room or mechanism is justified by this category label. iModulonDB is not
applicable without a specific gene, regulator or expression assertion.

Ignored-inclusive ID, label/stem, source-path and node searches covered
curation, history, research, configuration, raw inventories, PATHS/RETIRED
and individual reports. They found the CLASS row, child-owned exclusion and
contextual report/research mentions, but no target-owned definition,
exclusion, overlay, session history, dossier or previous individual report
within those bounds. A separate ignored-inclusive slice/term-request search
found no literal Laboratory developed term. That is not a universal claim
about all ontologies. An initial wrong-category guess for the child was
corrected using an ignored-inclusive identifier search.

## Findings

1. **Minor: the source category's entity is not established independently
   of laboratory-development provenance.** It could classify the origin or
   manipulation of organisms rather than a physical microbial environment.
   The child assessment and current tree warrant scrutiny, but the original
   direct members were not recovered and do not justify automatically
   assigning the child's meaning to the whole parent. Maintained owners are
   GOLD.77c5518fff in `curation/decisions.tsv`, any supported native definition
   in `curation/term_requests.tsv`, and original source/member metadata.

Zero blockers and zero major findings. The historical count is reproduced,
not contradicted by a differently scoped live aggregate. CLASS status and
an empty definition alone are not the finding.

## Recommended Edits

Recover the intended object and original direct members before ITEM review.
If it is solely an organism-development qualifier, record that explicitly
rather than inventing a habitat definition; if it denotes a physical
engineered environment, define that supported scope. Do not force a mapping
to laboratory environment or transfer the child NOT_APPLICABLE status.
Assess the target's Engineered parent only after scope is established;
guarded `gold_parent_exclusions.tsv` is the owner of any proven context-only
source contribution. Preserve the already-corrected child exclusion.

## Follow-up Checks

Preserve the four nodes, complete path, 56 ORGANISM count and historical
CLASS event. Audit incoming references before an identity/status change.
Add scope/count/full-corpus regressions, append history, dry-seed, inspect
a canary and run strict, provenance/history, label, corpus/site and full QC
for future authorized curation. Any count refresh requires governed source
provenance, not copying the live JSON number. Compare semantic inputs before
a genuine map rebuild. No lifecycle promotion follows from this report.

## Additional Notes

Only this new report was written. No scientific inputs, generated records,
history or GitHub state changed. The workbook style warning did not prevent
reading. Current source availability corroborates classification but does
not recover the original organism roster or settle the scope gap.
