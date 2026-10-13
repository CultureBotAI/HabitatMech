# YAML Record Review: Biliary tract

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml`
- Started UTC: 2026-10-04T12:38:37Z
- Finished UTC: 2026-10-04T12:39:49Z
- Verdict: needs curation

## Target

The complete generated `HabitatRecord` is `habitatmech:GOLD.134eb9e767`,
Biliary tract, HOST_ASSOCIATED, NARROW, SEEDED. It has two parents, one
uncounted GOLD attestation and one deterministic seed event. Definition,
synonyms, xrefs, taxa, parameters, citations, graphs, discussions, datasets,
contributors and replacement links are not emitted.

The exact target is `Host-associated > Reptilia > Digestive system > Biliary
tract`, node `gold.ecosystem:6938`. It is not a human, mammal, Bird, fish or
amphibian record merely sharing that label.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/host_associated/biliary_tract__d5e0bd1d.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Same unchanged-corpus invocation PASS: 1,179 canonical pairs, one synonym, five exceptions, 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | PASS, 953 ungrounded records and 1,810 decisions. This NARROW record is not one of the five displayed ungrounded rows. |
| `just qc` | Running tests at report completion; lint, documentation and provenance passed. No terminal test/full-QC result yet; history/schema/overlays, reproduction, site, redirects, term requests and final report remain unclaimed. |
| Structured references | Complete target and parent read; 14 raw TSVs scanned for exact key/path/node including ignored files. Current UBERON definitions and typed relations were inspected in this session; bounded current GOLD searches completed. |

Whole-corpus-only checks remain full-corpus checks. Subsequent terminal results
belong in the PR receipt rather than rewriting these observation-time results.

## Identity and Grounding

`habitatmech.seed.mint` reproduces GOLD.134eb9e767 using the source-kind-prefixed
complete path. PATHS.tsv:1421 pins its filename. No decision exists for this
source in the ignored-inclusive input search. SEEDED, NARROW/skos:narrowMatch
and the sole seed event accurately describe automatic tied-leaf grounding,
not an ITEM-reviewed equivalence claim. Six Biliary tract leaves tie at depth
four in the committed GOLD tree.

Active [UBERON:0001173 biliary tree](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001173)
defines the duct network. Active
[UBERON:0002294 biliary system](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0002294)
defines a wider organ-system subdivision. Both have biliary tract as a synonym
in current OLS and the vendored slice. The common wording does not resolve
GOLD's intended scope; an ITEM review should precede endorsement or replacement
of the automatic ontology parent. No universal reptile organ configuration is
inferred from these generic terms.

The complete source-parent record `digestive_system.yaml`,
`habitatmech:GOLD.26a84185d3`, is Reptilia Digestive system, NARROW under
UBERON:0001007. It has no authored general environment definition. Current
[UBERON digestive system](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001007)
denotes the whole anatomical system. A biliary network or subdivision is not
a subtype of that whole system, even though it contributes to digestion.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:2551` supplies the exact Reptilia path,
depth four, node 6938 and zero organism, study and biosample assertions. The
generated omission of a positive count is faithful to that row. The complete
structured scan of all 14 raw inventories found no exact-path bulk-biosample,
study, triad, taxon or parameter row for this target.

The whole digestive parent has 15 organism assertions; the separate Liver
child has one, at node 6939. Neither count belongs to this Biliary tract node.
The child's placement is classification context, not proof that liver is a
kind of biliary tree or that the parent source exactly equals biliary system.
No particular reptile species, normal microbiota, viability or disease-state
claim is supported or emitted.

The inspected current [biliary-tree graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001173/graph)
distinguishes subclass-of digestive system element from part-of biliary system.
The [biliary-system graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002294/graph)
distinguishes organ system subdivision from its part-of hepatobiliary system
relation. These typed distinctions and the complete digestive-system meaning
support the finding; mere absence of an external edge is not the argument.

Official OLS searches restricted to GOLD for GOLD:6938 and the complete path
returned zero hits. The committed node/path is verified, while current original
node/specimen details were not recovered. No retirement, absence of microbial
occupancy or contradiction of the source is inferred from these limited misses.

## Completeness

Ignored-inclusive searches of curation, history, research, reports, PATHS and
RETIRED used the source/parent keys, node, full path and filename. The session's
biliary-label search also covered maintained inputs, history and host research.
No exact-target decision, authored definition, overlay, dedicated research,
separate session history, previous individual review or retirement entry was
found before this new report.

A source-scoped definition and ITEM review are useful for the ontology
ambiguity. Optional taxa, parameters, literature, graphs and datasets need not
be filled from unrelated host evidence. iModulonDB is not applicable: the target
has no gene, regulator or expression dataset, and transcriptomic membership
would not establish anatomy or microbial habitat occupancy.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | Reptilia Biliary tract lists the whole Reptilia Digestive system (`habitatmech:GOLD.26a84185d3`) as a superclass, converting anatomical membership into is-a. | GOLD source-parent second pass at `src/habitatmech/seed.py:898-907`, or a governed source-specific correction input. |

Counts: zero blockers, one major, zero minor. The tree/system scope ambiguity
is a bounded follow-up, not a second proven identity error. Honest SEEDED status
is not separately scored as a defect.

## Recommended Edits

1. Correct this exact source-parent edge through maintained handling and regress
   its removal while preserving source identity/path/node and count semantics.
2. Resolve the shared-synonym scope at ITEM depth before changing the ontology
   parent or identity. Do not automatically merge host sources or swap terms
   because of child placement. Preserve valid parents once verified.
3. Do not hand-edit generated YAML/pages, erase source provenance, globally
   remove GOLD parents or apply `REPLACE` without assessing every inherited
   parent. Append required history and inspect guarded canary regeneration.

## Follow-up Checks

Require strict schema, current ontology semantics/labels, provenance/history,
exact corpus reproduction and full QC; inspect the emitted record and page.
An in-memory real-adapter comparison with full corpus context removes
`broader habitat: Digestive system` and changes semantic text. The current page
also displays the false source edge under Broader habitats.

A scientific repair therefore requires the real governed map/site rebuild
described in #1217. Keep protected draft #1218 untouched, preserve runtime pins
and freshness checks, and do not fabricate coordinates or checksums.

## Additional Notes

Open [#1379](https://github.com/CultureBotAI/HabitatMech/issues/1379) was inspected
and owns this hierarchy-defect family. An exact-source title/body/comment search
returned no separate issue. Add this independently verified reptile witness to
the existing issue, without treating the report as an implemented correction.

No paid research, scientific input/output mutation, status promotion, curation
event or committed-history rewrite was performed.
