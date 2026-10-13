# YAML Record Review: marine bathypelagic zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_bathypelagic_zone.yaml`
- Started UTC: 2026-10-03T18:09:09Z
- Finished UTC: 2026-10-03T18:10:16Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord, `ENVO:00000211`, marine
bathypelagic zone, AQUATIC, EXACT, REVIEWED. GOLD is the sole source, keyed
by `habitatmech:GOLD.e02911103f`. `PATHS.tsv:523` fixes the stem.

## Validation

- `just validate data/habitats/aquatic/marine_bathypelagic_zone.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_bathypelagic_zone.yaml`:
  one file, zero errors.
- Fresh full `just qc` was still active at review finish: 455 tests passed,
  3 skipped, 2 warnings; 83 history records, 3,206 strict records, 32 overlays,
  curation floor, exact corpus/site reproduction and 231 redirects passed.
  Term-request and final-report gates were not yet confirmed complete.
- Inspected current official ENVO OWL, fetched and byte-verified this batch:
  SHA-256 `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- Required network OAK identity validation is deferred to CI. No displayed
  taxa, DOI/PMID or causal references require separate resolution.

## Identity and Grounding

Identifier, label and definition reproduce
[current official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
and `ontology_terms.tsv:6801`. `decisions.tsv:1242` is an ITEM GROUND of the
exact Marine > Bathypelagic path; REVIEWED follows from that source decision.
The generated exact GOLD synonym preserves the source label. This water-column
zone is not the similarly named bathyal benthic biome or the separate slashed
GOLD Bathypelagic/Bathyal zone source.

`ENVO:00000210` marine aphotic zone is the direct ontology parent, preserved
in `ontology_subclass_edges.tsv:4844`; its full current class and maintained
record were read in this batch. Retain this true layer parent.

The second parent, `ENVO:00001999` marine water body, comes from GOLD's
Marine path. Its inspected definition denotes a whole water body, not a
depth/temperature layer within one. The zone-to-water-body relationship is
contextual or part-of, not the strict is-a relation required by
`parent_habitats`. The source path cannot justify this extra superclass.

The definition literally begins `The one of an ocean`. That malformed phrase
is present in current ENVO as well as the vendored TSV, so it is an upstream
wording defect, not a local transcription error. Do not silently repair an
ontology-sourced quote in generated YAML.

ENVO characterizes the zone by thermal limits; its distinct biome class,
`ENVO:01000037`, uses an approximate 1,000 to 2,500-2,700 m range.
[NOAA's light-zone account](https://oceanservice.noaa.gov/facts/light_travel.html)
uses 1,000-4,000 m for bathypelagic. These are inspected differing conventions,
not interchangeable numerical definitions. This review does not infer a new
exact depth bound, replace the zone with the biome, or count the convention
difference as another demonstrated source-mapping defect.

## Evidence

`gold_ecosystem_paths.tsv:255` has the depth-four path, nodes 5337 and 5338,
and 68 ORGANISM assertions. The record shows first node 5337 with the two-node
note; it does not lose the second node's provenance. The separate bulk row at
`gold_path_biosamples.tsv:431` names path ID 5338 and 30 biosamples, not
5,338 samples or 68 independently assayed depth profiles.

API triads at `gold_path_triads.tsv:440-442` cover 30 samples and five studies:

- Broad: `ENVO:01000037` oceanic bathypelagic zone biome, one term, share
  1.00, five agreeing studies.
- Local: `ENVO:00000211` marine bathypelagic zone, two terms, share 0.97,
  four agreeing studies.
- Medium: `ENVO:00002149` sea water, one term, share 1.00, five agreeing
  studies.

The current meanings of all three top terms were inspected. These are role-
specific annotations supporting context, not three independent sample sets
or a basis for making a zone identical to water material.

Structured exact-path membership over all 4,587 study rows found Gs0121483,
Gs0133511, Gs0141831, Gs0145237 and Gs0150723. Several studies include other
depth layers or unrelated source paths; co-occurrence does not imply habitat
equivalence. These are committed snapshot memberships, not independent
reviews of live study pages. No taxon is displayed or inferred.

## Completeness

Ignored-inclusive identifier, source-key, label, stem and path searches covered
curation, inventories, PATHS, history, research and individual reports. The
ITEM row was found; no target authored definition, causal overlay, dedicated
session history or prior individual target review was found. Earlier mentions
concern a separate slashed GOLD label, not this completed review.

Optional measurements, taxa, evidence, graphs, discussions and datasets should
remain empty without claim-specific input. iModulonDB is not applicable: there
is no taxon/gene/regulator/expression or molecular mechanism claim.

## Findings

- **Major M1: layer asserted to be a whole marine water body.** Remove the
  source-derived `ENVO:00001999` parent while retaining `ENVO:00000210`.
  Owner: GOLD parent-link generation in `src/habitatmech/seed.py:898-909`
  and a scoped maintained source-parent policy, not generated YAML.
- **Minor m1: malformed ontology definition opening.** `The one of an ocean`
  is faithfully copied from current ENVO. Owner: the upstream definition and
  governed ontology inventory refresh in `src/habitatmech/extract.py`, not a
  local string substitution or hand-edited provenance checksum.
- Blockers: 0. Major: 1. Minor: 1.

## Recommended Edits

First suppress only the false GOLD Marine parent through a governed scoped
rule, with a regression retaining the true aphotic parent. Do not use blanket
REPLACE or merge the separate bathyal/bathypelagic source from its label alone.
Keep the current zone identity and source evidence unless further source
review establishes a different scope.

Separately obtain an approved definition correction through the ontology's
maintenance process, then reproducibly refresh the pinned input and regenerate.
Do not guess that repairing one word settles the depth/temperature convention
or silently change numerical limits while fixing grammar.

## Follow-up Checks

Canary the record; preserve nodes, 68-ORGANISM count, two-node note, exact
source label and retained true parent. Append actual curation history and run
provenance, schema, OAK, corpus and full QC. Parent and definition text changes
affect semantic-map inputs, so rebuild the real map/site with the governed
runtime. Keep blocked #1217/draft #1218 separate and do not weaken freshness.

## Additional Notes

All 443 returned open/closed issues and comments were searched for the target,
source key and malformed definition; no matching correction was found. The
hierarchy and grammar findings have different owners and should be tracked
separately. No scientific input, generated artifact or history changed.
