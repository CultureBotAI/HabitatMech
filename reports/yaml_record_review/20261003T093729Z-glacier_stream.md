# YAML Record Review: Glacier stream

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/glacier_stream.yaml`
- Started UTC: 2026-10-03T09:37:29Z
- Finished UTC: 2026-10-03T09:38:50Z
- Verdict: needs curation

## Target

Read the complete generated `HabitatRecord`, `habitatmech:GOLD.cbad89b6dd`,
category `AQUATIC`, grounding `UNGROUNDED`, mapping `SEEDED`. Baseline:
`be5b91732f2f75e7135a9cba05b385a361798847`. The source is the Glacier stream
leaf under the direct Freshwater > Glacier path. It is not the parent
Glacier, a meltwater-material record, or a generic stream record.
Its slug is pinned at `data/habitats/PATHS.tsv:2785`.

## Validation

- `just validate data/habitats/aquatic/glacier_stream.yaml`: pass.
- `just validate-strict data/habitats/aquatic/glacier_stream.yaml`: pass,
  zero errors.
- Source row and exact-path inventory membership checks completed.
- Current OLS stream and englacial-stream definitions checked; glacier was
  also checked in this batch and the referenced parent record read in full.
- Shared full `just qc`: running at report completion; final outcome belongs
  to the PR. Full OAK validation was not repeated. The target has no asserted
  literature citation, taxon, or causal edge needing separate validation.

## Identity and Grounding

The path is
`Environmental > Aquatic > Freshwater > Glacier > Glacier stream`.
The minted identifier retains the compound source concept rather than
silently equating it with a generic or spatially narrower stream.
`curation/decisions.tsv:1126` is a `CLASS`-depth `CONFIRM_UNGROUNDED` row;
the generated `SEEDED` status and class-sweep warning accurately reflect it.

The sole parent, `habitatmech:GOLD.6faa98a0aa`, denotes the whole Glacier
source at the preceding path level. That parent record is glacier-grounded,
not a glacial-stream or glacier-associated-environment genus. Under the
ordinary watercourse reading, a stream fed by, on, or within a glacier is not
a subtype of that glacier. The record has no definition or item-level
decision resolving this distinction. The finding is an unsupported parent
assertion, not proof of a particular stream location or source membership.

## Evidence

Named-column parsing of `data/raw/gold_ecosystem_paths.tsv:1467` gives one
node (`gold.ecosystem:8062`), depth 5, and zero organism, study, biosample,
and total assertion counters. The record correctly retains the vocabulary
attestation without inventing a positive count or mapping predicate. There
is no genome-count column in this inventory.

Exact-path checks found no biosample or triad row and no pipe-delimited
membership in `gold_studies.tsv`. These bounded inventory misses do not prove
that the habitat lacks organisms or samples in the world. No authenticated
live GOLD query was made.

The [current ENVO stream definition](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000023)
describes a surface watercourse. The inspected primary study by
[Ezzat et al. (2025)](https://doi.org/10.1038/s41586-024-08313-z), especially
its Main and GFS environment sections, distinguishes glaciers from the
meltwater streams they feed. This supports the ordinary watercourse reading
and the source-versus-subclass distinction; its sampled communities and
physicochemical measurements are not evidence for GOLD node 8062 itself.

`ENVO:03000018` englacial stream is present in the vendored slice at
`ontology_terms.tsv:9580` and its
[live definition](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03000018)
specifies flow within a glacier or ice sheet. The GOLD label/path does not
establish that location, so it is not a justified exact grounding.
PREGO's generic stream row (`prego_habitats.tsv:52`) contains glacial-stream
label variants, but those do not become an independent attestation for this
minted GOLD target or prove full equivalence.

## Completeness

Ignored/hidden-inclusive searches covered `curation`, `history`, `research`,
`conf`, `reports/yaml_record_review`, `data/raw`, and the slug lock for the
identifier, node, exact path, slug, glacier/glacial-stream wording, and ice
stream. They found the class decision and the neighboring ontology/PREGO
terms, but no item-level decision, authored target definition, target research
report, causal overlay, or prior individual target review there.

No taxa, parameters, graphs, evidence, discussion, or datasets are asserted.
These optional fields should remain empty without scoped evidence. A useful
definition must distinguish a flowing-water habitat from an ice-flow feature;
neither that interpretation nor an englacial location should be invented to
make a parent fit.

## Findings

- **Major M1: the glacier parent is unsupported as a strict broader class.**
  The source hierarchy represents association or location under the ordinary
  stream interpretation, not is-a. Resolve the source meaning explicitly
  before retaining or replacing the edge; the present class sweep did not do
  that work. Owners: `curation/decisions.tsv`, a justified definition in
  `curation/term_requests.tsv`, and source-parent generation in
  `src/habitatmech/seed.py`.

Zero blockers and zero minor findings.

## Recommended Edits

1. Confirm from source documentation or scoped member evidence whether GOLD
   means a liquid-water stream, and define that scope. Do not reinterpret it
   as an ice-flow feature solely to preserve the existing parent.
2. For the watercourse reading, use an item-level broader stream grounding
   (`ENVO:00000023`) while retaining the minted glacier-specific identity,
   and suppress only the immediate GOLD parent `habitatmech:GOLD.6faa98a0aa`
   via the maintained exclusion mechanism proposed in draft PR #1218.
   Do not adopt englacial stream without evidence for its location constraint.

## Follow-up Checks

Run `just seed` and
`just seed-canary habitatmech:GOLD.cbad89b6dd --force`; inspect the complete
record, scope, retained source path, and independently supported genus.
Add curation history only for actual changes. Run schema/strict validation,
`just validate-products` for a grounding change, `just verify-corpus`, required
map refresh, `just render`, and `just qc`. Verify the parent Glacier record
and its other children are not merged or altered incidentally.

## Additional Notes

iModulonDB is not applicable: the target has no taxon, gene, regulator, or
expression dataset. The external paper is contextual evidence for this review,
not a newly attached record citation or a source of universal taxa or traits.
No paid research, corpus edit, or status promotion was performed.
