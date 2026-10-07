# YAML Record Review: Animal feed production

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/animal_feed_production.yaml`
- Started UTC: 2026-10-07T04:24:41Z
- Finished UTC: 2026-10-07T04:25:50Z
- Verdict: pass (0 blocker, 0 major, 0 minor)

## Target

Read the complete generated HabitatRecord and rendered page. Identifier
`habitatmech:GOLD.68f7051d62`, ENGINEERED / UNGROUNDED / SEEDED. The target
is the depth-two GOLD category `Engineered > Animal feed production`, not
animal feed material, a specific mill, a storage space or its Fermentation
descendant. One parent, one attestation and two history events are present.
No definition, synonym, xref, mapping predicate, count/unit, parameter,
taxon, literature evidence, graph, discussion or dataset is asserted.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/animal_feed_production.yaml`: passed.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/animal_feed_production.yaml`: passed, one file, zero errors.
- Read-only `build_corpus()` / `build_document()` comparison reproduced the
  whole parsed record: one source concept, zero reviewed sources, zero taxa
  and two events. This is not a replacement for full-corpus verification.
- Full QC and OAK were not repeated per target. Scientific inputs/products
  remain at `43e6c5d0fb508bcbf7341b8ca5be0141a495f2ed`; reuse successful
  [exact-baseline QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37569153392),
  whose SHA and terminal success were checked in this continuation, for
  corpus, reference, history and product gates. Both immediate identities
  are minted source concepts rather than ontology IDs OAK can certify.
- Original GOLD node/edge re-extraction remains unavailable: the
  continuation's ignored-inclusive search of `build` and configured
  kg-microbe `data` found no such dumps. Exact numbered-node provenance
  below is verified against the committed inventory, not a new export.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:1111` records the full path, four nodes
`gold.ecosystem:6478|gold.ecosystem:8378|gold.ecosystem:8379|gold.ecosystem:8380`,
and zero organism/study/biosample counts. The first-node note and omitted
count/unit are correct; zero counted source organisms is not biological
absence. The full-path mint matches the record and PATHS line 2053.

The actual seeder route is `gold_unmatched`, retained by the CLASS
CONFIRM_UNGROUNDED row at `curation/decisions.tsv:624`. Its explicit caveat
that habitat-hood was not individually assessed is preserved in the record
and page. The CLASS and seed events justify SEEDED, not REVIEWED. The
historical no-match note is not a claim that no suitable term can ever exist.

Read the full actual parent, `engineered__900b76ad.yaml`, identifier
`habitatmech:GOLD.2acb39dd08`. Its source path, first of five nodes,
68-organism count and CLASS status agree with inventory row 253 and decision
line 331. The initially guessed `engineered.yaml` filename did not exist;
PATHS was used to select the correct suffixed record. Actual child and
parent automatic/curated resolution routes were both inspected.

## Evidence

Freshly inspected primary
[GOLD classification guidance](https://gold.jgi.doe.gov/ecosystem_classification)
describes paths as sample surroundings, with Engineered representing
engineered environments and its ecosystem categories representing divisions
of those environments. Inference: this high-level feed-production bin can
denote engineered production surroundings, so its relationship to the
Engineered umbrella is defensible. The activity-like label alone does not
prove a process-only identity. The guidance does not identify a particular
facility, feed material, recipe or production technology for these nodes.

Structured exact-field/pipe-member searches covered all 14 raw TSVs. The
ecosystem inventory is the only target-key-bearing input. Two additional
hits are descendants: Fermentation at line 693 (three organisms) and Swine
waste with corn at line 626 (five organisms). These distinguish the category
from a named activity and a feed-associated material; their counts and
properties are not inherited by the target. They do not establish that all
source-tree edges are is-a.

An ignored-inclusive search of bulk biosamples, triads and studies for the
full category label found no matching contribution. There is no target
dataset or accession to verify beyond the governed GOLD node IDs.

## Completeness

Ignored-inclusive content searches covered identifier, label, slug and
parent ID across curation, history, configuration, docs, tests, research,
the research manifest, PATHS and RETIRED; filename searches covered
curation/history/research. No target-owned definition, parent exclusion,
causal overlay, history session or research report was found in those
bounds. A broad Environmental research report only lists this GOLD category
and is not independent scientific evidence. The child's process exclusion
is a separate decision, not evidence that this entire category is a process.

A bounded ignored-inclusive ontology/mapping search found animal-feed
material and feed-storage terms, but no exact feed-production category
match. This is not a global ontology absence claim. None of those nearby
terms can be adopted merely to replace an UNGROUNDED status.

The missing optional definition leaves the production-setting boundary
coarse; it does not make the honest SEEDED record a reviewed definition.
No observed parameter, characteristic organism or mechanism is being
discarded from the examined inputs. iModulonDB is not applicable without a
named organism, gene, regulator or expression dataset; this is not negative
evidence about biological activity.

## Findings

None found: zero blocker, major and minor findings. Identity and broad
parentage are defensible at the source-category level, and unassessed
ITEM status is disclosed. This verdict is not a claim of completed ontology
curation or a license to collapse activity, factory, storage and material
identities into one exact term.

## Recommended Edits

No corrective edit is established by the inspected evidence. Preserve the
minted identity, source path and first-node note, Engineered parent,
count/unit omissions, and UNGROUNDED/SEEDED state.

For future separately authorized enrichment, inspect target-specific source
metadata before defining the production environment. An ITEM assessment
belongs in `curation/decisions.tsv`; a supported novel habitat definition
belongs in `curation/term_requests.tsv`, with attributed session history.
Do not add a NOT_APPLICABLE decision just because the label contains
production, or replace the bin with an animal-feed material term. Those
would be stronger claims than the present evidence supports.

## Follow-up Checks

No immediate fix requires regeneration. If later curation changes identity
or definition, review the exact category boundary against its descendants,
run `just seed`, inspect
`just seed-canary habitatmech:GOLD.68f7051d62 --force`, and perform strict,
corpus, history, site and full QC checks after authorized regeneration.
Any ontology grounding additionally requires primary identifier/label
verification and `just validate-products`. Do not promote descendants or
sum their counts as part of a target-only change.

## Additional Notes

Search-engine results unrelated to the GOLD category were not used as
evidence. Only this new report was authored for the target; no scientific
edits, review-status promotion, history changes, paid research or GitHub
mutation occurred. The all-record objective remains active.
