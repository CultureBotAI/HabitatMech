# YAML Record Review: marine benthic biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_benthic_biome.yaml`
- Started UTC: 2026-10-03T18:33:39Z
- Finished UTC: 2026-10-03T18:39:00Z
- Verdict: needs curation

## Target

Read the complete generated HabitatRecord, `ENVO:01000024`, marine benthic
biome, AQUATIC, EXACT, REVIEWED. `data/habitats/PATHS.tsv:760` pins its stem.
Three GOLD source concepts and one PREGO concept feed this record. The full
Desert springs record was read only as parent context, not counted as another
completed target review.

## Validation

- `just validate data/habitats/aquatic/marine_benthic_biome.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_benthic_biome.yaml`:
  one file, zero errors.
- Fresh full `just qc` was still running its tests at review finish. Lint,
  documentation consistency and raw provenance had passed. The remaining
  full-corpus, history, reference and generated-product gates were not yet
  confirmed complete; this is not a full QC pass.
- Current official ENVO OWL was fetched and byte-verified in this review
  batch: SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  Inspected the target, its ontology/source parents and all three triad terms.
- Current NCBI taxonomy efetch resolved all 25 displayed IDs directly, with
  no alias redirects. Structured CSV/YAML comparison verified all retained
  raw scores, ranks, blank labels, candidate pools and provenance flags.
- OAK correspondence is deferred to required CI. Schema validation and
  identity-label correspondence do not prove source equivalence or ecology.

## Identity and Grounding

The ID, canonical label, definition and `ENVO:00000447` marine-biome parent
agree with `data/raw/ontology_terms.tsv:7535`,
`data/raw/ontology_subclass_edges.tsv:5665` and
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl).
Its scope includes coastal and deep seafloor settings. Oceanic zone
(`ENVO:00000207`) is an off-shelf water mass; marine water body
(`ENVO:00001999`) is a whole water body. Neither is a strictly broader class
of this generic biome. The additional Desert springs parent comes from the
freshwater source conflation described below.

The four decision keys and source paths were checked individually:

| Source concept | Maintained decision | Assessment |
|---|---|---|
| `habitatmech:GOLD.01adfdcfa4`, node 4040, Marine > Oceanic > Benthic | `curation/decisions.tsv:109`, GROUND/CLOSE, ITEM | Notes distinguish zone from biome; exact identity needs reassessment, and its oceanic parent must not constrain the generic biome. |
| `habitatmech:GOLD.8911f04011`, node 5402, Freshwater > Desert springs > Benthic | `curation/decisions.tsv:805`, GROUND/CLOSE, ITEM | Explicit freshwater context contradicts the adopted marine identity. |
| `habitatmech:GOLD.d0bf6f6843`, node 5711, Marine > Benthic | `curation/decisions.tsv:1151`, GROUND/CLOSE, ITEM | Notes distinguish zone from biome; close similarity alone does not establish identity. |
| `habitatmech:PREGO.41a65dc075`, ENVO:01000024 | `curation/decisions.tsv:1433`, REVIEW, ITEM | Stable ontology identity and source projection agree. The old multi-source endorsement does not resolve the other decisions' conflicts. |

All four ITEM decisions explain the mechanically derived REVIEWED status.
The three CLOSE mappings do not override the stronger EXACT PREGO grounding.
Neither computed status establishes that the merge is scientifically valid.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:467`, `:1457` and `:1507` reproduce all
three GOLD paths and node IDs. Only the oceanic path has a nonzero organism
count, 15. The other two paths have zero source counts; omission of an
assertion count in their YAML attestations is faithful, not missing evidence.

For the exact oceanic path, `data/raw/gold_path_biosamples.tsv:702` gives
seven bulk samples. `data/raw/gold_path_triads.tsv:611-613` describes seven
API samples across four studies. Its leading broad/local/medium terms are
ocean biome, marine benthic feature and microbial mat material, each with
share 0.43. Their distinct-term counts are 3/3/4 and studies agreeing are
2/2/1. These are contextual slots, not three equivalent habitat identities.
The current local term `ENVO:01000105` is obsolete with several consider
targets, not a unique replacement; do not adopt it as a new grounding.

`data/raw/gold_studies.tsv` contains five exact-path bulk study memberships:
Gs0095614 (line 508), Gs0110098 (555), Gs0110099 (556), Gs0130311 (1604),
and Gs0135746 (2140). The last also has a crustal-fluids path. Four API
studies versus five bulk memberships is a snapshot/provenance distinction,
not evidence that either count should overwrite the other. These committed
memberships were inspected; live study contents were not independently read.

Structured exact-path checks scanned all 1,040 bulk-count rows, 1,587 triad
rows and 4,587 study rows. Neither the freshwater benthic path nor the
generic Marine > Benthic path has a matching row in those three tables.
Child Wood fall and the separate Benthic zone > Sediment rows do not supply
their parent's missing evidence. No assertion counts from unlike units were
summed.

`data/raw/prego_habitats.tsv:35` gives 2,067 taxa/direct assertions, maximum
score 2.20432 and environmental_samples. All 25 displayed rows at
`data/raw/prego_habitat_taxa.tsv:7403-7427` match their IDs, scores, ranks
1-25 and pool 2,067. Raw names are blank, direct flags TRUE, and corroboration
is absent. No retained row sets `is_characteristic`; 2,042 other candidates
were not individually reviewed.

The primary
[NCBI efetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=406538,406540,29158,6613,106299,80836,69293,8090,7425,104421,29159,6182,9258,483417,7029,6334,13686,6238,7070,483407,7159,9031,121224,6945,7209)
resolved every displayed ID. Examples include 406538 Loripes lacteus,
29159 Magallana gigas, 9031 Gallus gallus and 7209 Loa loa. A valid stable
taxon identifier is not proof of benthic ecology. The original PREGO sample
evidence was not inspected, so the supported claim is faithful source
projection, not independently verified habitat membership. Do not infer a
microbial name or delete an unusual association solely from plausibility.

PREGO's two alternate strings are related synonyms. GOLD's ambiguous
Benthic label is emitted as an exact synonym by `ingest_gold`; its meaning
must be reconsidered with the source-identity decisions, not treated as
independent support for the conflation.

## Completeness

Ignored-inclusive identifier, source-key, label and stem searches covered
curation, history, raw inventories, PATHS, research and individual review
reports. No target-specific authored definition, causal overlay or separate
curation-history file was found. Earlier reports mention this term as
context or a candidate; they do not constitute a completed review of this
target. The maintained decisions and generated history were inspected.

No optional environmental parameters, causal graphs, evidence objects,
discussions or datasets are present in the target. Generic seafloor biology
does not justify filling those fields. Optional blank taxon names are not
alone a schema failure. iModulonDB is not applicable: this record makes no
gene, regulator, expression-dataset or mechanism claim.

## Findings

Blockers: 1. Major: 1. Minor: 0.

1. **Blocker B1: freshwater source merged into a marine identity.** The
   desert-spring Benthic decision ignores its explicit freshwater path and
   introduces a false Desert springs parent. These are one underlying
   conflation, not two findings. Owner: `curation/decisions.tsv:805` and
   governed regeneration. Tracked in
   [#1279](https://github.com/CultureBotAI/HabitatMech/issues/1279).
2. **Major M1: contextual GOLD parents become false generic is-a claims.**
   The oceanic-zone and whole-marine-waterbody parents are not broader
   classes of the target. `src/habitatmech/seed.py`'s second `ingest_gold`
   pass links resolved parent paths without checking semantic scope.
   Owners: the marine source decisions at rows 109/1151 and narrowly
   governed source-parent handling, coordinated with draft #1218. Retain
   the genuine marine-biome parent and all source provenance. Tracked in
   [#1280](https://github.com/CultureBotAI/HabitatMech/issues/1280).

## Recommended Edits

Detach the freshwater concept into its minted identity unless a verified
exact freshwater term is established. Do not transfer the marine PREGO
taxa. Reassess both marine GROUND/CLOSE decisions using full paths and
zone-versus-biome semantics; do not assume that a close mapping permits
identity merging, or automatically merge the separate Benthic zone record.

After identity decisions, retain only strictly broader parents. If a marine
GOLD source legitimately remains merged, exclude its contextual ancestry
through the governed source-specific input/rule, not by deleting generated
YAML parents or all GOLD hierarchy. Preserve the ontology parent.

These scientific fixes remain open. Their changed semantic inputs require
map/site regeneration; the supported-runtime blocker is tracked in
[#1217](https://github.com/CultureBotAI/HabitatMech/issues/1217). No runtime
pins, map freshness checks or generated checksums should be bypassed.

## Follow-up Checks

Add source-specific regression tests for freshwater/marine separation,
retained PREGO ownership and genuine ontology ancestry. Append curation
history for the input changes, dry seed, inspect affected canaries, then
regenerate through the normal guarded writer. Check descendant/redirect
effects if identities split; do not prune a partial run.

Run normal/strict validation, history and provenance checks, exact corpus
reproduction and OAK correspondence. Rebuild affected semantic map/site
products in the supported governed runtime, then run full QC. For this
report-only PR, complete local QC and all required CI before merge.

## Additional Notes

All 446 returned open/closed GitHub issues and their comments were searched
for the target ID, freshwater source key and benthic terms before filing.
#262 addresses obsolete ontology identities elsewhere; it does not resolve
the present marine/freshwater merge or justify adopting the obsolete triad
term. Existing reports and research prose were treated as leads only.

This report changes no scientific input, generated record, page, review
status or curation history. Its publication does not close #1279 or #1280.
