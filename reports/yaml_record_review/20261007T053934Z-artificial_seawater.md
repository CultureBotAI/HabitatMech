# YAML Record Review: Artificial seawater

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/artificial_seawater.yaml`
- Started UTC: 2026-10-07T05:38:24Z
- Finished UTC: 2026-10-07T05:39:34Z
- Verdict: pass (0 blocker, 0 major, 0 minor)

## Target

Read the entire generated HabitatRecord and rendered page. Identifier
`habitatmech:GOLD.a00fd807eb`, ENGINEERED / UNGROUNDED / SEEDED, source path
`Engineered > Industrial production > Chemical products > Artificial seawater`.
This is a manufactured seawater-like material, not natural sea water, a
specific enriched culture recipe or an aquarium. One parent, one attestation
and two history events are present. No definition, synonym, xref, count/unit,
parameter, taxon, literature evidence, graph, discussion or dataset is asserted.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/artificial_seawater.yaml`: passed.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/artificial_seawater.yaml`: passed, one file and zero errors.
- Read-only `build_corpus()` / `build_document()` comparison reproduced the
  full parsed record: one source concept, zero reviewed sources, zero taxa
  and two events. Actual target and parent GOLD resolution routes were read.
- Primary ENVO OWL at `a2455d1a77e46bb8a664d65a157166b539269042`
  confirms the parent is active, with the exact stored label and definition;
  the nearby sea-water class was checked for scope, not adopted as identity.
- Full QC and OAK were not repeated per record. Scientific inputs remain
  at `ca366555ec4e19694bec1154e1d892c4242bc6c0`. Reuse
  [exact-baseline QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37575268135)
  and [label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37575268092),
  whose SHA and terminal success were checked this continuation, for corpus,
  reference, history and generated-product gates. A minted identity is not
  an ontology identity validated by OAK.
- Original GOLD source re-extraction remains unavailable: the continuation's
  ignored-inclusive search of `build` and configured kg-microbe `data` found
  no original node/edge dumps. Source-node details below are checked against
  the committed inventory rather than a fresh source export.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:1308` contains the exact path, nodes
`gold.ecosystem:8501|gold.ecosystem:8502` and zero organism/study/biosample
counts. The first-node note and omitted assertion count/unit are correct;
zero counted organisms does not imply that the material cannot host microbes.
PATHS line 2487 and the full-path mint agree.

The automatic route is `gold_unmatched`, retained by CLASS
CONFIRM_UNGROUNDED at `curation/decisions.tsv:931`. The source parent's mint
`habitatmech:GOLD.413b4cb862` resolves through ITEM decision line 451 to
`ENVO:2000000` chemical product. The target therefore inherits that parent
without having its own ITEM decision. Both history events and SEEDED
status match this distinction.

The complete chemical-product parent record was inspected. Its label and
definition agree with `data/raw/ontology_terms.tsv:10334` and current
[ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl).
Artificially prepared salt solutions fit that manufactured chemical-mixture
genus. Current `ENVO:00002149` sea water instead depends on physicochemical
properties determined by sea/ocean processes, so a similar composition is
not enough to assert exact identity with natural sea water.

## Evidence

Structured exact-field/pipe-member scanning covered all 14 raw TSVs. Only
the ecosystem-path inventory contains a target-key contribution; no target
bulk biosample, study, triad, taxon or environmental-parameter row was found.

The inspected official [DSMZ SP2 medium recipe](https://mediadive.dsmz.de/medium/405)
distinguishes artificial from natural sea water and gives a prepared
salt-and-water solution used in a larger culture medium. This supports the
manufactured material interpretation and possible cultivation context,
not identity with SP2 or transfer of its pH, ingredients, strain or growth
conditions to every artificial seawater product.

The public [ASTM D1141 scope](https://store.astm.org/standards/d1141)
also describes prepared inorganic-salt solutions that simulate ocean
water and cautions against treating their behavior as natural ocean water.
Only the public scope was inspected; the paid standard was not acquired.
Neither source identifies the particular formulations represented by GOLD
nodes 8501/8502, and neither is an additional imported source attestation.

## Completeness

Ignored-inclusive identifier, label, slug and parent-ID searches covered
curation, history, configuration, docs, tests, research, research manifest,
PATHS and RETIRED, plus filename searches of curation/history/research.
No target-owned definition, parent exclusion, causal overlay, session
history or research report was found within those bounds. A research note
about an adjacent materials category is only a lead.

An ignored-inclusive search for artificial/synthetic sea-water variants in
`data/raw/ontology_terms.tsv` and `isolation_source_groundings.tsv` found
no exact candidate. This is a bounded local result, not a global ontology
absence claim. The historical CLASS no-match statement is not proof that
no current exact term can exist.

No optional measurement, characteristic organism or mechanism is being
omitted from the examined target inputs. iModulonDB is not applicable
without a named gene, regulator, organism or expression dataset; its
non-use is not negative evidence. A future supported definition would be
useful enrichment, but a guessed universal recipe would be incorrect.

## Findings

None found: zero blocker, major and minor findings. The minted identity,
manufactured category, direct chemical-product parent, source provenance
and limited workflow status are defensible. This verdict does not promote
the source bin to an ITEM-reviewed ontology definition.

## Recommended Edits

No corrective edit is established. Preserve the minted source identity,
chemical-product parent, node note and count omissions. Future ITEM
assessment belongs in `curation/decisions.tsv`; a supported definition
belongs in `curation/term_requests.tsv`, not generated YAML or HTML.
Do not collapse this record into natural sea water or a named DSMZ recipe.

## Follow-up Checks

No immediate regeneration is needed. For later authorized enrichment,
verify the particular source scope, inspect a seed dry run and target
canary, and run strict, corpus, history, site and full QC checks after
regeneration. Any ontology grounding also requires primary scope checks
and `just validate-products`. Retain the distinction between a generic
artificial seawater material and enriched formulations made from it.

## Additional Notes

Only this timestamped report was authored. No curation decision, history
event, review-status change, generated product, paid research or GitHub
item was changed.
