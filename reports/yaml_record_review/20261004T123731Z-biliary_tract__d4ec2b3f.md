# YAML Record Review: Biliary tract

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml`
- Started UTC: 2026-10-04T12:35:17Z
- Finished UTC: 2026-10-04T12:37:31Z
- Verdict: needs curation

## Target

The complete generated `HabitatRecord` is `habitatmech:GOLD.de5efc0eb8`,
Biliary tract, HOST_ASSOCIATED, NARROW and SEEDED. It contains two parents,
one uncounted GOLD attestation and one deterministic seed event. No definition,
synonyms, xrefs, taxa, parameters, evidence, graph, discussions, datasets,
contributors or replacement links are emitted.

This is the Mammals source, `Host-associated > Mammals > Digestive system >
Biliary tract`, node `gold.ecosystem:6398`. It is distinct from the separately
reviewed human and Bird sources, despite the shared label.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/host_associated/biliary_tract__d4ec2b3f.yaml` | PASS, one file, zero errors. |
| `just validate-products` | PASS: 1,179 canonical pairs, one synonym, five exceptions, 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Running at report completion, no result yet. |
| `just qc` | Running tests at report completion; lint, documentation and raw provenance passed. Full-corpus history/schema/overlay, reproduction, site/redirect/term-request and final report gates are pending, not claimed successful. |
| Source and term checks | Complete target/parent reads, 14 raw TSVs scanned structurally including ignored files, actual mint calculation, current official UBERON terms and typed graph relations inspected. |

Whole-corpus-only validators were launched through the documented QC runner;
no invented per-record reference/history check substitutes for them. Later
terminal results should be recorded in the publication receipt.

## Identity and Grounding

The actual source-kind-prefixed `habitatmech.seed.mint` function reproduces
GOLD.de5efc0eb8. PATHS.tsv:2936 pins the filename. There is no maintained
decision for this source key in the ignored-inclusive search, matching SEEDED
and its single seed event. The six Biliary tract leaves in the GOLD tree all
have depth four; the tied-leaf route keeps them minted and emits NARROW with
`skos:narrowMatch`. Tree depth is an algorithmic explanation, not independent
scientific proof of the chosen anatomy.

Current [UBERON:0001173 biliary tree](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001173)
is active and denotes a bile-conducting network. Active
[UBERON:0002294 biliary system](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0002294)
denotes a wider organ-system subdivision. Both use the synonym biliary tract,
also present in the vendored slice. An ITEM review must resolve the intended
source scope before endorsing or replacing the automatic ontology mapping.
Shared synonyms do not make these terms equivalent.

The complete parent `digestive_system__efdbeca1.yaml` is
`habitatmech:GOLD.c8e85f3c84`, Mammals Digestive system, NARROW under
UBERON:0001007. It has no authored general associated-environment definition.
Current [UBERON digestive system](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON%3A0001007)
denotes the whole anatomical system. Neither a biliary network nor its system
subdivision is a kind of that whole system; anatomical membership is not is-a.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:2004` supplies the exact path, depth four,
node 6398 and zero organism, study and biosample assertions. The generated
omission of a positive count is correct. The complete structured scan of all
14 raw TSVs found no exact-path bulk-biosample, study, triad, taxon or parameter
row for this source. Absence here is bounded to committed inventories.

The digestive parent has 681 organism assertions. Separate children include
Liver with 77 and Gallbladder with 10, plus zero-count Bile, Bile ducts and
Gallbladder stones. These are not direct counts for Biliary tract. Child
placement provides classification context but does not establish ontology
subclassing, an exact biliary-system identity, a normal community or viability.

The current [biliary-tree graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001173/graph)
distinguishes subclass-of digestive system element (UBERON:0013765) from
part-of biliary system (UBERON:0002294). The
[biliary-system graph](https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0002294/graph)
distinguishes subclass-of organ system subdivision from part-of hepatobiliary
system. This typed evidence and the complete parent meaning support the
hierarchy finding, not merely a missing external edge.

Official GOLD-filtered OLS searches for GOLD:6398 and the complete mammal
path returned zero hits. Node/path provenance is verified in the committed
inventory; current original node/specimen details remain unrecovered. The
bounded search result does not establish retirement or biological absence.

## Completeness

Ignored-inclusive source/parent key, node, full path, label and filename searches
covered curation, history, research, review reports, PATHS and RETIRED. They
found no exact-target decision, authored definition, causal overlay, dedicated
research, separate session history, prior individual review or retirement entry
before this report. Older bile-child reviews mention this parent; those mentions
do not constitute a review of this target or validate containment as is-a.

Source-scoped definition and ITEM grounding review would resolve consequential
uncertainty. Optional taxa, parameters, citations, mechanisms and datasets need
not be filled without evidence. iModulonDB is not applicable: the record names
no gene, regulator or expression dataset, and module membership would not prove
an anatomical relationship.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | Mammal Biliary tract asserts the whole Mammals Digestive system (`habitatmech:GOLD.c8e85f3c84`) as a superclass. The GOLD source path has been converted from anatomical membership into is-a. | `src/habitatmech/seed.py:898-907`, or a governed source-specific correction input for that contribution. |

Counts: zero blockers, one major, zero minor. The shared-synonym ambiguity is
an unresolved grounding follow-up, not a second proven identity error. Honest
SEEDED status is not itself an additional defect.

## Recommended Edits

1. Correct this exact source-parent edge through maintained, regression-tested
   handling. Preserve source identity, path, node and zero-count semantics.
2. Resolve biliary-tree versus biliary-system scope at ITEM depth. Do not swap
   terms by synonym alone, merge host clades or use child placement as proof
   of exact identity. Retain valid ontology parents once verified.
3. Do not hand-edit generated YAML/pages, globally drop source parents or use
   `parent_mode=REPLACE` without proving every inherited parent false. Append
   required curation history and inspect guarded regeneration for an actual fix.

## Follow-up Checks

Regress the rejected whole-system edge and preserve exact source provenance.
Validate ontology scope, strict schema, label correspondence, provenance/history,
corpus reproduction and full QC; manually inspect the canary and rendered parent
list. No scientific edit is made by this review.

The actual `semantic_text` comparison with full corpus context removes
`broader habitat: Digestive system` and changes text. The current page renders
the same parent under Broader habitats. A real governed map/site rebuild is
required by open #1217. Protected draft #1218 remains OPEN/DRAFT at
`18c93452a789218f5c653d02723d11388d972055`, untouched; do not fake freshness
or assume its correction machinery is available on main.

## Additional Notes

Existing open [#1379](https://github.com/CultureBotAI/HabitatMech/issues/1379)
was read in full, including its empty comment list. It owns this exact
scientific defect family, initially demonstrated for the human and Bird
records. This independently reviewed mammal target should be added as a scoped
witness, not filed as a duplicate or marked fixed.

Browser OLS retrieval failed; direct access to the official structured API
succeeded. No paid research, scientific artifact/status change, curation event
or committed-history rewrite was performed.
