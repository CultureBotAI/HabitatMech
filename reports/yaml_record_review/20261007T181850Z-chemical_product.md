# YAML Record Review: chemical product

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/chemical_product.yaml`
- Started UTC: 2026-10-07T18:12:16Z
- Finished UTC: 2026-10-07T18:18:50Z
- Verdict: needs curation

## Target

Generated `HabitatRecord` `ENVO:2000000`, label `chemical product`, category
`ENGINEERED`, grounding `EXACT`, mapping `REVIEWED`. Baseline:
`2697504b4d6185ab702988cd13f8e2233a9ac109`.

The complete target was read. It contains an ENVO definition and definition
source, one GOLD synonym, two parents, one source attestation and two history
events. It has no xrefs, environmental parameters, taxa, graph, discussion or
dataset reference. This report changes no scientific input or generated record.

## Validation

Commands use `UV_CACHE_DIR=build/uv-cache`:

| Check | Result and scope |
|---|---|
| `just validate data/habitats/engineered/chemical_product.yaml` | No issues found. |
| `just validate-strict data/habitats/engineered/chemical_product.yaml` | One file, zero errors. |
| Read-only `build_corpus` / `build_document` comparison | Every target field reproduced exactly; one source concept and one ITEM-reviewed source. |
| Source mint | Exact GOLD path mints `habitatmech:GOLD.413b4cb862`, the maintained decision key. |
| Current ontology cross-check | Official ENVO master resolved to `a2455d1a77e46bb8a664d65a157166b539269042`; structured OWL was inspected for the target, manufactured-product genus, manufacturing process and output relation. |

The preceding publication session's full `just qc` passed on the identical
file tree: 530 tests passed, three skipped; 153 valid histories; all 3,207
records strict-valid and exactly reproduced; 32 overlays, curation floor,
map/site freshness, 249 redirects and term-request gates passed. Its separate
OAK check found 1,178 canonical labels, one synonym, five accepted exceptions
and 2,056 no-adapter skips. All 18 governed artifacts matched. These are reused
full-gate results, not fresh full runs for this target. Fresh focused checks
are listed above. Shape, reproduction and label checks cannot certify strict
parent semantics.

## Identity and Grounding

The source concept is `Engineered > Industrial production > Chemical products`.
Its 2026-08-12 ITEM `GROUND` decision resolves the mint to `ENVO:2000000` with
the verified canonical label and `EXACT` status. The one source has an ITEM
decision, so `REVIEWED` is correctly derived. That status does not certify
parents added independently by the source hierarchy.

The label, definition and `ENVO` definition source agree with the local slice
and current official OWL. The GOLD plural `Chemical products` is preserved as
an exact lexical synonym and as the verbatim source label. The singular/plural
variation does not by itself establish an identity defect. The historical
decision's exact-label wording should not be mistaken for a documented survey
of every product formulation or sample in the source bin.

This is a manufactured material/product class, not a molecular identity, a
chemical role, the production activity, or a claim that all chemicals are
habitats. Its definition does not justify importing every chemical substance
or blank-control role into a common biological environment. No contrary
source-specific evidence establishes that this retained identity must be
changed as part of the bounded parent correction.

## Evidence

**Valid ontology genus.** The current [official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
explicitly gives `ENVO:00003074`, manufactured product, as the named superclass
of `ENVO:2000000`. The latter concerns chemically engineered mixtures; the
former concerns material entities processed by humans or their technology.
This typed parent agrees with `data/raw/ontology_subclass_edges.tsv` and must
be retained. The genus is available in the ontology slice even though an
ignored-inclusive identifier search found no separately attested HabitatRecord
for it; a valid ontology reference need not have its own habitat page.

**Product versus production.** The same OWL relates manufactured product to
`ENVO:01000993`, manufacturing process, through `RO:0002353`, output of. The
process has an output relation back to manufactured products and is typed as
a process, not as the product's material genus. This supports the distinction
between a material result and its production context; it does not equate the
minted GOLD parent with that ENVO process class.

The other generated parent, `habitatmech:GOLD.a744ade0d8`, is the separate
Industrial production record at
`data/habitats/engineered/industrial_production__f961ebd0.yaml`. It remains
UNGROUNDED/SEEDED with only CLASS screening and no authored material definition.
`ingest_gold` adds it from the immediate GOLD path level. The source gives
production context, not evidence that chemical products are a subtype of
the production activity or its setting. Nor can that one source path establish
a universal industrial-production subtype restriction on the adopted ENVO class.
This is the unsupported hierarchy contribution requiring correction.

**Direct attestation.** The exact depth-three GOLD row collapses nodes
`gold.ecosystem:5579`, `gold.ecosystem:5787` and `gold.ecosystem:5788`.
It records ten organism assertions, zero study/biosample counts in that older
inventory, and total assertions ten. The generated first-node display,
three-node note, ten ORGANISM count and source path agree. The source mint
resolves to a different ontology identity through the ITEM decision, so the
`skos:exactMatch` mapping predicate has the expected direction and owner.

The later GOLD enrichment inventory has 74 biosamples at path ID 5788. Exact
pipe-member comparison in the study inventory finds 11 study IDs containing
the direct path, not counts inherited from its children:

`Gs0144948`, `Gs0151580`, `Gs0151852`, `Gs0153947`, `Gs0154228`, `Gs0156829`,
`Gs0156830`, `Gs0156849`, `Gs0159258`, `Gs0159292`, `Gs0164331`.

These inventories use different units/releases; 74 biosamples must not replace
or be added to ten organism assertions. The study rows have other habitat paths,
so they do not establish characteristic organisms or a uniform composition.
No exact direct-path row occurs in `gold_path_triads.tsv`. Triads on reagent
blank, lab-grade water, sheath fluid and input-fracking-water descendants are
not this record's environmental parameters.

The first listed [live GOLD study](https://gold.jgi.doe.gov/study?id=Gs0144948)
could not be accessed. The 11 study identifiers were checked as committed
inventory references, not independently verified live studies or publication
crosswalks. No biological mechanism is inferred from them.

## Completeness

Ignored-inclusive ID, source-mint, label and slug searches covered curation,
history, configuration, raw inventories, PATHS/RETIRED maps, research reports
and the research manifest. They found the ITEM decision but no target-owned
term request, external-xref row, causal overlay, parent exclusion, retirement,
or target-specific session history on those surfaces. References in the buffer
solution definition/history concern that child, not a missing authored
definition for this already ontology-defined parent.

The absence of taxa, parameters and causal graphs is appropriate for this broad
product class without source-specific support. Ten organism assertions are not
ten characterized taxa, and the parent's 125 organism assertions are not the
child's evidence. Distilled water, buffer solution, artificial seawater and
blank-control descendants do not establish class-wide chemistry or microbial
mechanisms. Their individual boundaries need their own reviews.

iModulonDB is not applicable: the target makes no gene, regulator, pathway,
strain-specific stress-response or transcriptomic-module assertion. No DOI,
PMID, experimental figure or quantitative mechanism claim requires literature
validation in this record.

## Findings

No blocker; one major finding; no minor finding established.

1. **Major: Industrial production is imported as a strict parent of a product.**
   The valid manufactured-product genus is independent. The additional GOLD
   edge turns production context into universal subtype semantics, unsupported
   by the source or the adopted ontology definition. The maintained fix owner
   is `curation/gold_parent_exclusions.tsv`, keyed to
   `habitatmech:GOLD.413b4cb862`, the exact Chemical products path, and expected
   resolved parent `habitatmech:GOLD.a744ade0d8`. The guarded implementation
   already exists in `src/habitatmech/seed.py::ingest_gold`.

## Recommended Edits

1. In a separately authorized curation session, exclude only that immediate
   GOLD parent contribution. Retain `ENVO:00003074`, the existing ENVO identity,
   definition, synonym, source path, three-node provenance, ten ORGANISM count,
   exact mapping predicate and ITEM-derived status.
2. Do not use a broad `REPLACE` definition or alter ontology edges to suppress
   this context contribution. Do not change the parent record's own identity
   merely to repair a claim made by the child.
3. Append a truthful curation-session history when the exclusion is actually
   applied. This review neither adds history nor changes status.
4. Keep potential source-bin heterogeneity and descendant blank-control roles
   as separate identity assessments. Do not use them to invent uniform
   composition, taxa, pH, growth conditions or a chemical-process graph here.

## Follow-up Checks

- Regression-test the actual source exclusion against an otherwise identical
  corpus: only this target's parent/audit fields should change; the ontology
  genus and all provenance must remain unchanged.
- Retain tests for stale source-path/resolved-parent guards and independent
  ontology/curator parent preservation.
- Dry-seed, then inspect `just seed-canary ENVO:2000000 --force` before any
  wider generation. Run strict validation, history validation, full corpus
  reproduction and `just qc` after authorized curation.
- Refresh the semantic map before rendering because parent labels affect its
  selected inputs. Recheck actual source descriptions before revising the
  exact identity or making formulation- or organism-specific assertions.

## Additional Notes

Browser calls to the OLS term endpoints failed. The official GitHub API and
commit-pinned ENVO OWL succeeded through structured retrieval, and the relevant
class/relation elements were inspected directly. No unavailable OLS text was
treated as evidence.

All searches establishing absence included ignored files in the named local
surfaces. Contextual reads of Industrial production and references to buffer
solution are not additional completed record reviews. Only this new report was
written; no generated record, maintained scientific input or GitHub item changed.
