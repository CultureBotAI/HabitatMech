# YAML Record Review: Insect burrows

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/insect_burrows.yaml`
- Started UTC: 2026-10-03T14:40:33Z
- Finished UTC: 2026-10-03T14:42:16Z
- Verdict: needs curation

## Target

Read the entire generated `HabitatRecord`, `habitatmech:GOLD.40bfbe291f`,
Insect burrows, `AQUATIC`, `UNGROUNDED`, `SEEDED`. It has one source-qualified
sediment parent, one GOLD attestation, a CLASS confirmation and a seed event.
No definition, taxa, parameters, citation or mechanism graph is present.
`PATHS.tsv:1781` identifies this exact aquatic source, not a generic terrestrial
burrow or an insect body habitat.

## Validation

- `just validate data/habitats/aquatic/insect_burrows.yaml`: pass.
- `just validate-strict data/habitats/aquatic/insect_burrows.yaml`: pass,
  zero errors.
- Minting the complete source path reproduces the ID; decision row 446
  explains the CLASS-level confirmation and seeded status.
- Current OLS verifies burrow and sediment. The complete minted sediment
  parent was read, rather than inferring its meaning from its label alone.
- Fresh local QC has passed 455 tests (three skipped), 83 history records,
  all 3,206 closed-schema records, 32 graph overlays, curation floor and exact
  corpus reproduction. Site and later gates are still running at this timestamp.
  Exact baseline full QC and network labels also passed at `7f1e021db`,
  runs [37128839209](https://github.com/CultureBotAI/HabitatMech/actions/runs/37128839209)
  and 37128839287.

## Identity and Grounding

The full source path is
`Environmental > Aquatic > Freshwater > Sediment > Insect burrows`.
It describes a sediment-associated biogenic feature, not the insect taxon
or a process alone. The generic burrow class `ENVO:01000429` denotes an
excavated hole or tunnel and is a plausible strictly broader parent, not
an exact replacement for this insect/freshwater-qualified source.
[Burrow](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000429).

The sole actual parent `habitatmech:GOLD.e4e91038b5` is the minted freshwater
Sediment material, independently parented to `ENVO:00002007`. Sediment is
deposited particulate material. A burrow within it, including its space and
interfaces, is not a subtype of that material. The immediate GOLD source
hierarchy is contextual and does not justify an is-a claim. If future source
metadata specifically describes burrow-wall sediment, that would require an
explicit material-scope decision, not an assumption made to retain this edge.
[Sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002007).

## Evidence

`gold_ecosystem_paths.tsv:1489` supplies node `gold.ecosystem:8392`, depth
five and zero assertion counters. The generated record correctly emits no
positive count. Its enclosing sediment parent has 190 organism assertions,
which must not be borrowed for the burrow source.

Complete exact-path scans found no sample, API-triad or study membership in
`gold_path_biosamples.tsv`, `gold_path_triads.tsv` or `gold_studies.tsv`.
These snapshot misses do not prove biological absence.

The inspected primary abstract for PMID:24218828,
DOI:10.1016/S1001-0742(12)60116-8, describes a specific Lake Taihu experiment
with larval burrows as microenvironments within sediment. It supports the
reality of a freshwater burrow habitat and its distinction from bulk sediment.
It does not identify this GOLD node or license universal species, oxygen,
nitrogen-flux or mechanism claims for all insect burrows.
[Primary study](https://doi.org/10.1016/S1001-0742(12)60116-8).

## Completeness

Ignored-inclusive searches of the exact IDs, source path, label/stem and
freshwater-burrow wording covered curation, history, research, configuration,
raw inventories and prior reports. No target ITEM decision, definition,
causal overlay, session history or prior exact-target report was found. The
CLASS decision is not an individual habitat assessment. Empty optional taxa
and mechanisms are appropriate until source-specific support exists.
iModulonDB is not applicable: the record makes no organism-specific molecular
claim, and an example paper's larvae do not provide a matching bacterial dataset.

## Findings

1. **Major: a burrow feature inherits its surrounding sediment material as
   an is-a parent.** The edge is
   `habitatmech:GOLD.40bfbe291f -> habitatmech:GOLD.e4e91038b5`.
   Owner: maintained GOLD source-parent controls in `src/habitatmech/seed.py`;
   an ITEM identity/broader-parent decision belongs in `curation/decisions.tsv`.

Zero blockers, one major finding, zero minor findings.

## Recommended Edits

Confirm the feature-versus-wall-material scope, exclude the unjustified
sediment contribution, and add a verified broader burrow relation if the
ordinary feature reading holds. Retain the minted insect/freshwater-qualified
identity. Do not map to a whole insect or make the enclosing sediment's
organism count part of this record. Append history and regenerate through
maintained inputs and the validated writer.

## Follow-up Checks

Add an exact-source parent regression, dry-run/canary, preserve zero-count
semantics and qualified source provenance, and inspect true broader parents.
Regenerate the semantic map/site using the governed runtime and run label,
schema, history, corpus and full QC. Coordinate the source-parent mechanism
in draft #1218 and map-runtime dependency #1217 without bypassing their gates.

## Additional Notes

No target input or product was changed. The primary study's abstract was
verified through Europe PMC, not treated as a source-member lookup. All
returned open/closed issues were searched for the target and parent IDs and
burrow wording; no matching issue was returned.
