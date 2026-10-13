# YAML Record Review: Anaerobic zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/anaerobic_zone.yaml`
- Started UTC: 2026-10-07T03:20:53Z
- Finished UTC: 2026-10-07T03:22:22Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the complete generated HabitatRecord and rendered page. Identifier
`habitatmech:GOLD.9f519b94cc`, ENGINEERED / UNGROUNDED / SEEDED. The exact
target is the anaerobic zone under the GOLD Partial-Nitrification/Anammox
(PNA) bioreactor path, not a general anaerobic quality or a marine anoxic
zone. One attestation, one parent and two history events. No count/unit,
mapping predicate, definition, synonym, xref, parameter, taxon, literature
evidence, causal graph, discussion or dataset is asserted.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/anaerobic_zone.yaml`: passed.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/anaerobic_zone.yaml`: passed, one file, zero errors.
- Read-only `build_corpus()` / `build_document()` comparison reproduces every
  field: one source concept, zero reviewed sources, zero taxa and two events.
  This target check supplements rather than replaces full-corpus verification.
- Full QC and OAK were not repeated. Scientific inputs and products remain
  unchanged from `ec95a7191a9b6c9ddaa404c2062f7be9932623a9`; reuse the
  successful [exact-baseline QC run](https://github.com/CultureBotAI/HabitatMech/actions/runs/37562477062)
  for reference, history, corpus and product gates. Its SHA and success were
  checked in the preceding continuation. Both immediate identities here are
  minted source concepts, not ontology labels OAK can independently certify.
- Original GOLD node/edge re-extraction and live numbered-node provenance
  were unavailable. The exact source-node claim is checked against the
  governed inventory, not inferred from a literature example.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:1203` records the exact depth-four path
`Engineered > Bioreactor > Partial-Nitrification/Anammox (PNA) > Anaerobic zone`,
with nodes `gold.ecosystem:8548|gold.ecosystem:8549` and all organism, study,
biosample and total assertion counts zero. The first-ID note is correct.
The generator intentionally omits count/unit when the organism count is
zero: this means no positive organism count in the inventory, not proof of
biological absence. No mapping predicate is needed for a minted source concept.

Actual GOLD resolution is `gold_unmatched`, preserved by the CLASS
CONFIRM_UNGROUNDED row at `curation/decisions.tsv:927`; the full-path mint
recomputes correctly and PATHS line 2481 pins the file. Its 2026-08-12 CLASS
event and original 2026-08-16 event are consistent with SEEDED, not ITEM review.
A zone can be a microbial habitat without being the biological process
named in its surrounding reactor context.

Read the entire immediate parent record
`data/habitats/engineered/partial_nitrification_anammox_pna.yaml`. It denotes
the PNA bioreactor setting, ID `habitatmech:GOLD.5f3cbd7563`, with bioreactor
ENVO:00002123 as its parent. Its mint, CLASS decision at line 586, prefix
path, inventory row 1200 and PATHS line 1989 agree. That identifies the
containing system, but supplies no evidence that its anaerobic zone is a
type of the whole PNA reactor.

## Evidence

Parsed exact-field/pipe-member searches of all 14 raw TSVs found the target
only in the ecosystem inventory. A second label hit at line 1204 is the
distinct Biomass descendant, node 8551, not an additional target attestation.
Lines 1201-1204 separately name aerobic and anaerobic zones and their biomass
descendants. This source structure supports keeping region, biomass and
whole-system identity distinct; it is not automatically an is-a hierarchy.

Fresh official PubMed XML for
[Vazquez-Padin et al. 2010](https://pubmed.ncbi.nlm.nih.gov/20646732/)
verified PMID 20646732, DOI 10.1016/j.watres.2010.05.041, authors, title,
journal/date and full abstract. Microelectrode and FISH measurements in
their CANON reactor distinguish external nitrification and internal anammox
zones within granules. This is experimental support for a region-versus-system
distinction, not identification of GOLD nodes 8548/8549 with that experiment.
No granule size, temperature, oxygen threshold, removal rate or studied taxon
is transferred to this target.

The specific publisher fetch failed; the official PubMed XML succeeded.
Another architecture paper was opened as a lead but is not needed to support
the verdict. The GOLD label alone does not settle whether this source zone
is a macroscopic compartment or a microbial-aggregate microzone. The finding
does not depend on choosing between those geometries.

## Completeness

Ignored-inclusive content searches used the ID, label, slug, full path and
parent ID across curation, history, configuration, documentation, tests,
research, the research manifest, PATHS and RETIRED; filename searches covered
curation/history/research. No target-owned definition, exclusion, causal
overlay or research report was found. Unrelated EBPR and host-associated
anaerobic-zone mentions do not describe this PNA target.

All raw inventories were searched, and a separate ignored-inclusive prefix
search of GOLD biosamples, triads and studies found no PNA-path contribution
there. No supported parameter, organism or dataset is being omitted from
those bounded inputs. A local ontology search found no exact PNA anaerobic
zone term; the marine anoxic-zone hit is the wrong context and is not a
grounding candidate. This is not a global ontology absence claim.

Optional sparse fields do not justify fabricated content. The same session's
ignored-inclusive search of `build` and configured kg-microbe data found no
GOLD node/edge dumps, preventing original re-extraction. iModulonDB is not
applicable to this uninstantiated habitat context: no named organism, gene,
regulator or expression dataset is supplied for a structured module match.

## Findings

1. **Major: a zone-to-containing-system link is modeled as a broader class.**
   `parent_habitats: [habitatmech:GOLD.5f3cbd7563]` says the zone is a type
   of the PNA system. Its full path and the inspected experimental evidence
   instead support spatial context. `docs/CURATION.md:26` requires is-a
   semantics; the immediate GOLD path loop in `src/habitatmech/seed.py:910`
   supplies this unsupported parent. Maintained owner:
   `curation/gold_parent_exclusions.tsv`.

No blocker or minor finding was established. Sparse provenance does not
establish that the zone is not a habitat or authorize a process identity.

## Recommended Edits

In separately authorized curation, add a source-parent exclusion keyed by
`habitatmech:GOLD.9f519b94cc`, exact full path ending in Anaerobic zone, and
expected parent `habitatmech:GOLD.5f3cbd7563`, with the region-versus-system
evidence. Preserve both source nodes, the first-ID note, path, identity,
category, count/unit/predicate omissions and UNGROUNDED/SEEDED provenance.
Add append-only session history and let regeneration add the exclusion event.

Do not invent a definition merely to suppress the edge, replace it with a
general anaerobic quality or marine-zone identity, merge it into Anammox or
Biomass, or promote its review status from this report. A supported region
genus, relation to the containing reactor and more precise spatial definition
are separate ITEM curation questions requiring additional source scope.

## Follow-up Checks

Add a focused regression in `tests/test_gold_parent_exclusions.py` proving
only this immediate parent disappears and the exclusion event is added,
with all unrelated scientific fields and SEEDED state unchanged. Run
`just seed`, inspect `just seed-canary habitatmech:GOLD.9f519b94cc --force`,
then authorized full regeneration, strict validation, `just verify-corpus`,
history/site checks and `just qc`. Any later ontology grounding requires
`just validate-products`. Do not alter the aerobic sibling, biomass descendants
or parent identity without their own scoped review.

## Additional Notes

Only this timestamped report was written. No scientific edits, generated
artifact changes, status promotion, paid research or GitHub mutation occurred.
The all-record objective remains active.
