# YAML Record Review: aqueous humor of eyeball

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/aqueous_humor_of_eyeball.yaml`
- Started UTC: 2026-10-04T04:09:37Z
- Finished UTC: 2026-10-04T04:15:18Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord `UBERON:0001796`, HOST_ASSOCIATED,
EXACT, REVIEWED: ontology definition, four synonyms, three parents, one GOLD
attestation and two August 16 events. This is the Mammals path, not the
separate Mammals: Human source. Actual `mint` reproduces its former key
`habitatmech:GOLD.2a1b56ffda`; `PATHS.tsv:1043` pins the current filename
and `RETIRED.tsv:122` preserves the former source URL.

## Validation

- `just validate data/habitats/host_associated/aqueous_humor_of_eyeball.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/aqueous_humor_of_eyeball.yaml`:
  one file, zero errors.
- Fresh `just validate-products`: passed; 1,179 canonical pairs, one synonym,
  five configured exceptions and 2,054 configured no-adapter skips.
- Full local `just qc` passed immediately before this batch on the identical
  tree `5454cf514ce031807b6647dc393b1974c7aee257`: 457 tests passed, three
  skipped, two dependency warnings; 87 history records, 3,206 strict records,
  32 overlays, corpus and generated products passed. No scientific files
  changed since then. Post-merge QC run 37176047075 also completed successfully
  during this review; no redundant new full local run is claimed.
- Current official OLS term/typed-graph retrievals succeeded. Browser PubMed
  returned HTTP 429; direct primary EFetch supplied the abstract and IDs.

## Identity and Grounding

ITEM GROUND at `curation/decisions.tsv:1650` resolves this source to
[UBERON:0001796](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001796).
The current non-obsolete label, definition and three ontology synonyms
match vendored row 13073 and the generated record. The full slash-form
source label names aqueous humor in its ciliary-body context; the isolated
words intraocular fluid are not used to merge all ocular fluids.
EXACT/REVIEWED and the GROUND/SEEDED events faithfully follow the ITEM row.

Current non-obsolete [UBERON:0006312](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0006312)
ocular refractive media and [UBERON:0006314](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0006314)
bodily fluid match vendored rows 13293/13294. Both are true broader classes;
local subclass rows 11249/11250 agree with the current typed graph.

The complete parent `eye_ciliary_body__832768c5.yaml` denotes the ciliary-
body structure, `habitatmech:GOLD.aceda5f881`, not an authored regional
environment. Current [UBERON:0001775](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001775)
positively defines that structure as vascular-tunic tissue with muscle and
processes. It is not a fluid class. Its local whole-eye parent
[UBERON:0000970](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0000970)
denotes a light-detecting organ and does not make this false edge valid.

The current [aqueous-humor graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001796/graph)
distinguishes subclass, part_of anterior chamber and production by ciliary
epithelium. These positive typed relations and definitions support the
fluid/structure distinction; the finding is not inferred solely from a
missing subclass edge. Production and containment are not is-a.

## Evidence

`gold_ecosystem_paths.tsv:2144` is node 6876, exact five-level Mammals path,
with zero organism/study/biosample/total assertions in that tree inventory.
The generated source ID, path, label and exactMatch predicate agree. The
seeder emits count/unit only for nonzero organism counts, so their omission
is expected; it does not prove the environment cannot contain microbes.

Complete structured scans covered 2,562 tree paths, 1,040 bulk biosample
rows, 4,587 studies and 1,587 triads. The human sibling, node 6184, has
seven biosamples in the separate bulk inventory, one matching study row
`Gs0132964` spanning two paths and three triad rows. Those are not the
target mammal path, not seven organism assertions and not independent
studies. Its local ciliary-body triad and aqueous medium have distinct
roles and do not justify this target's source-parent is-a edge.

The complete human sibling YAML and its decision at row 1669 retain a
separate NARROW source beneath aqueous humor. It was a reference read,
not another completed target review or evidence to transfer here.

The inspected [primary abstract, PMID:28706959](https://pubmed.ncbi.nlm.nih.gov/28706959/)
reports positive aqueous cultures in a retrospective bacterial-
endophthalmitis cohort. The primary PubmedData ArticleIdList, distinguished
from cited-reference IDs, verifies DOI:10.1186/s40662-017-0083-9 and
PMC5506679. This supports a bounded microbial-site interpretation, not a
normal healthy-eye microbiome, a universal diagnostic claim or membership
in either GOLD source. No clinical quantities or taxa are imported; only
the abstract is relied on, not uninspected full methods.

## Completeness

Ignored-inclusive target ID, former key, label variants and filename
searches covered curation, history, research, prior reviews, raw inputs,
PATHS and RETIRED. They found the decision, source and redirect but no
target definition request, overlay, session, research report or earlier
target review. Unrelated soil/liquid aqueous-phase mentions were not
treated as ocular evidence. Old decisions do not retroactively require a
later-style session record merely to be reviewed now.

Full scans of 162 BacDive sources, 3,081 BacDive taxa, 358 mapping rows,
770 parameters, 58 Madin habitats, 1,378 Madin taxa, 719 PREGO habitats
and 8,807 PREGO taxa found no target-key or aqueous/intraocular match.
This is bounded inventory coverage, not biological absence. Optional
taxa, parameters and graphs are not quotas. iModulonDB is not applicable:
the target supplies no gene, regulator or expression-module claim.

## Findings

1. **Major - HM-AQUEOUS-HUMOR-001:** the ciliary-body source parent is not
   a strictly broader class of aqueous humor. Maintained owner:
   `src/habitatmech/seed.py:898-907` or a governed source-specific exclusion.
   Filed as [#1345](https://github.com/CultureBotAI/HabitatMech/issues/1345).

No blocker or minor finding established. Identity, ontology ancestry,
source fields and zero-count handling are supported.

## Recommended Edits

Remove only the false source-parent contribution, preserving the exact
identity, both valid ontology parents, source key/node/path, status and
retired URL. Do not encode production/partonomy as an equivalence xref,
globally delete GOLD parents or silently merge human/mammal evidence.
The ciliary-body parent's own grounding needs separate review.

A read-only real-adapter comparison confirms parent removal changes input
by dropping the ciliary-body superclass line. Append required history,
inspect a guarded canary and regenerate map/site through supported tools;
#1217 remains relevant. Do not hand-edit generated YAML or freshness hashes.

## Follow-up Checks

Regress this exact edge while preserving both ontology parents and every
source field. Verify strict schema, OAK, full ancestry, history, corpus
reproduction, semantic/site/redirect freshness and full QC. Recheck raw
path identity before adding any human study or triad evidence.

## Additional Notes

All 497 existing issue bodies and returned comments were searched before
filing. #926 concerns old review lookup wording, not the new edge finding.
The earlier human-ciliary review treats anatomical containment as broader
ancestry; that reasoning is not adopted here and its reference reads are
not counted as new coverage. No scientific inputs, generated artifacts or
history changed; no paid research ran.
