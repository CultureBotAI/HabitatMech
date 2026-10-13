# YAML Record Review: Built Environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/built_environment.yaml`
- Started UTC: 2026-10-07T15:38:58Z
- Finished UTC: 2026-10-07T15:41:04Z
- Verdict: needs curation

## Target

Generated `HabitatRecord` `mesh:D000076624`, label `Built Environment`, category
`ENGINEERED`, grounding `EXACT`, mapping `SEEDED`. Baseline:
`884218cc445dce07a946e14cd42e41f6d2df5764`. The entire 22-line record was read
as this review's target, separately from the preceding building review.

It contains two parents, one GOLD attestation and one seed event. Definition,
synonyms, xrefs, environmental parameters, taxa, causal graphs, discussions and
dataset references are absent. No generated content or maintained scientific
input was changed by this review.

## Validation

Commands use `UV_CACHE_DIR=build/uv-cache`:

| Check | Result and scope |
|---|---|
| `just validate data/habitats/engineered/built_environment.yaml` | No issues found. |
| `just validate-strict data/habitats/engineered/built_environment.yaml` | One file, zero errors. |
| Read-only `build_corpus` / `build_document` equality | All fields reproduce exactly; one counted source, zero reviewed sources. |
| `just verify-corpus` | Shared run earlier in this session: 3,207 expected/present, zero missing, extra or different records. Scientific inputs have not changed. |
| `just validate-history` | Shared session run: 149 histories valid. |
| `just validate-causal-all` | Shared session run: all 32 overlays/graphs valid; no overlay targets this record. |
| Identifier/relation inspection | Both MeSH descriptors verified through NLM browser text and current structured JSON; source mint and all four GOLD node IDs verified against the committed inventory. |

Previous full QC at the unchanged baseline passed 525 tests with three skips,
plus corpus/site/redirect/term-request gates. Previous full OAK results were
1,178 canonical, one synonym, five accepted exceptions and 2,056 no-adapter
skips. Neither full gate was rerun for this report. MeSH is not certified by
that OAK adapter coverage; its semantics were independently inspected here.
No focused taxon or citation validator applies to this record's empty slots.

## Identity and Grounding

[NLM Built Environment, D000076624](https://meshb.nlm.nih.gov/record/ui?ui=D000076624)
is an active descriptor covering manufactured physical environmental elements,
including buildings and infrastructure. Its preferred concept is M000622402
and its tree placement is N06.230.145.500. The label and broad GOLD grouping
are compatible. It is not synonymous with indoor air, one building, or the
activity of designing an environment.

The exact GOLD source mint is `habitatmech:GOLD.d601823ae4`, computed from
`Engineered > Built environment`. There is no matching decision row in
`curation/decisions.tsv`; generation confirms zero ITEM-reviewed sources.
`SEEDED` accurately signals that this automated exact-label resolution is not
an ITEM endorsement. This read-only review does not promote the status.

The first parent, `habitatmech:GOLD.2acb39dd08`, resolves to the generated
Engineered root at `data/habitats/engineered/engineered__900b76ad.yaml`. Its
source is GOLD's top-level Engineered grouping; its existing CLASS decision
does not claim an ITEM-level habitat assessment. Built physical environments
fit that engineered grouping, so no specific false-parent finding is established
for this edge. Its broader root definition remains provisional, not independently
certified by this child review.

The second parent, `mesh:D004779`, is **Environment Design**, not Environment.
[NLM defines that descriptor as the activity of structuring environments to
influence behavior](https://meshb.nlm.nih.gov/record/ui?ui=D004779).
Physical built elements are not kinds of that activity. This violates the local
strictly-broader meaning of `parent_habitats` even though it accurately reflects
a link in the source thesaurus.

## Evidence

**Attestation.** The exact committed `gold_ecosystem_paths.tsv` row records:

- Path `Engineered > Built environment`, depth 2, leaf `Built environment`.
- Four node IDs: `gold.ecosystem:2888`, `3515`, `3847`, and `4279`.
- 282 organism assertions; zero study and biosample assertions.

The record correctly shows the first node, the collapse note, `skos:exactMatch`
and 282 ORGANISM assertions. The count is a source summary, not 282 taxa, a
species prevalence estimate or a summation of descendants. For example, the
inventory separately has 25 direct child paths, including Building, Canal,
House, Hospital, Pipeline, and International Space Station. Their assertions
must not be folded into this record's count without a separately defined
aggregation contract. The four source IDs were not independently re-fetched
from authenticated live GOLD records.

**The false strict-parent edge has a traceable importer cause.** The current
[NLM structured descriptor](https://id.nlm.nih.gov/mesh/D000076624.json)
uses `http://id.nlm.nih.gov/mesh/vocab#broaderDescriptor` for its link to
D004779. Its object is confirmed by the [parent descriptor JSON](https://id.nlm.nih.gov/mesh/D004779.json).
This is not an NLM-authored `rdfs:subClassOf` assertion.

In `src/habitatmech/extract.py`, `_reference_ancestry` reads MeSH
`broaderDescriptor` into an untyped child/parent pair. Later, `extract_ontology_terms`
emits every such ancestry pair with predicate `rdfs:subClassOf`. The resulting
row in `data/raw/ontology_subclass_edges.tsv` is exactly:

```text
mesh:D000076624  rdfs:subClassOf  mesh:D004779
```

The seeder then uses that row as a habitat parent. Therefore corpus reproduction
proves propagation of the input, not correctness of its strengthened relation.
The demonstrated bug is this physical-entity-to-activity edge; this review does
not assume that every MeSH broader relation is unsuitable, or that other
ontology subclass imports should be removed.

**Definition and empty evidence fields.** The local ontology slice supplies the
canonical label but leaves the definition blank, so the generated omission is
faithful. The NLM scope note would be useful to retain through a governed
definition-import policy, but absence of an optional definition is not itself
an additional finding. No record-authored microbial, parameter, taxon or causal
claim requires literature support here. Evidence from the narrower building
graph must not be inherited as a universal mechanism for this broad class.

## Completeness

Ignored-inclusive searches covered identifier, source mint, label and slug in
`curation/`, `history/`, `conf/`, `PATHS.tsv`, `RETIRED.tsv`, committed raw
inventories and the research manifest. Exact table parsing additionally confirmed
no target decision, term-request or GOLD-parent-exclusion row. All maintained
graph YAMLs were searched, including ignored files; none targets this ID.
There is no target-specific session history in the searched history tree.
References to other records beneath Built environment are not target evidence.

A full ignored-inclusive parse of `data/habitats/**/*.yaml` found no separate
HabitatRecord for D004779. This is not a broken reference: it is present and
labelled in the ontology slice, which supplies external parent identities.
The problem is semantic relation type, not missing node existence.

No optional taxa, parameters or graph should be invented to make this broad
grouping denser. A future ITEM decision should explicitly compare GOLD scope
with the NLM descriptor, not infer approval from label equality or this report.
iModulonDB is not applicable: no gene, regulator, strain, pathway or expression
dataset is asserted. Absence from such a database is not ecological evidence.

## Findings

No blocker; one major finding; no minor findings.

1. **Major: a MeSH thesaurus relation is promoted to false habitat subsumption.**
   Built Environment is placed under Environment Design as though a physical
   environment were a kind of designing activity. The primary scope notes and
   structured relation, committed edge and importer implementation jointly
   establish the defect. Maintained owner: the MeSH branch of
   `_reference_ancestry` and ontology-edge emission in `src/habitatmech/extract.py`,
   with a governed source-relation representation or explicit reviewed policy
   if related links are retained. Generated owners affected are
   `data/raw/ontology_subclass_edges.tsv`, this habitat record and downstream
   products. `curation/gold_parent_exclusions.tsv` is not the correct fix surface:
   this contribution is an ontology import, not a GOLD path parent.

## Recommended Edits

1. Preserve MeSH relation semantics in the maintained import path. Do not cast
   all broader descriptors to strict subclass edges. Remove this unsupported
   strict-parent contribution through a documented, provenance-preserving rule;
   retain the source association under an appropriate relation if supported.
2. Preserve Built Environment identity, category, GOLD source IDs/counts/path
   and the independently sourced Engineered parent. Do not replace the record
   with Environment Design or invent a definition solely to override ancestry.
3. Add regression coverage using this exact MeSH pair, and assess the full
   affected MeSH ancestry slice before a shared importer change. Scope-note
   import and an ITEM review can be separate deliberate enhancements.
4. Append a truthful history record for the later import/curation session.
   Do not hand-edit the raw inventory, checksum, generated YAML or old audit.

## Follow-up Checks

- Re-extraction requires the pinned source snapshots. Inspect drift before
  changing the manifest; do not silently substitute a different ontology release.
- Verify the preserved source relation and absence of the false strict edge in
  regenerated inputs. Test that valid independently supported parents survive.
- Dry-seed, inspect `just seed-canary mesh:D000076624`, and compare all fields
  with this baseline before wider generation.
- Run strict validation, corpus reproduction, curation-history validation and
  `just qc`; inspect the whole-corpus semantic differential of the shared
  importer. Rebuild governed map/site artifacts when inputs change.
- Repeat the NLM descriptor and relation checks explicitly. A passing ontology
  label check or corpus reproducer alone cannot prove hierarchy semantics.

## Additional Notes

The browser tool could not open descriptor JSON, but direct structured retrieval
succeeded for both IDs. A speculative upstream module path was absent; the
defect was subsequently traced in the actual local HabitatMech extractor, so no
finding relies on that failed path lookup.

This report is read-only. It does not count its parent or any of the 25 GOLD
children as separately reviewed, create GitHub issues, certify export readiness,
or complete the all-record review objective.
