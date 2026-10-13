# YAML Record Review: Continuous Culture

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/continuous_culture.yaml`
- Started UTC: 2026-10-08T05:37:19Z
- Finished UTC: 2026-10-08T05:41:02Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.deb06c4e48` at
`8f8453fde62d9eacf305cb781c6104f9fc181936`. It denotes the exact GOLD path
`Engineered > Bioreactor > Continuous culture`, not its marine-sediment-inoculum
child. It is ENGINEERED / UNGROUNDED / SEEDED, with one parent, one attestation
and two history events. No definition, synonym, xref, parameter, taxon,
literature evidence, mechanism, discussion or dataset is asserted.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/continuous_culture.yaml`: no issues.
- `just validate-strict data/habitats/engineered/continuous_culture.yaml`:
  one file, zero errors.
- `just verify-corpus`: all 3,207 records reproduce; no missing, extra or
  differing files.
- `just validate-history`: all 171 session records valid.
- `just provenance-check`: 14 inventories and two GOLD sources current.
- `uv run pytest tests/test_corpus_integrity.py -q -k 'parent or
  reviewed_records or history or causal_edges_reference'`: six existing
  parent/status/reference tests passed, 33 deselected. This selection does
  not add a separate generated-history test.
- `just validate-products`, additionally setting
  `OAKLIB_HOME=$PWD/build/oak-current-20261008`: 1,177 canonical pairs, one
  synonym, five existing exceptions, and 2,057 explicit no-adapter skips.
  Label agreement does not validate the biological meaning of a parent edge.

Executed `resolve_gold` / `apply_decision` with complete ontology, normalized
mapping, leaf-claimant and composed-claimant indexes. Full read-only
`build_corpus` / `build_document` comparison reproduced every target field.
Full QC was not repeated for this report: the same baseline's native queue
[37732242717](https://github.com/CultureBotAI/HabitatMech/actions/runs/37732242717)
passed all offline gates, 578 tests with three skips; publication's local full
QC also passed before this review. No standalone literature-reference check
applies to this citation-free target. Original organism/sample re-extraction
was unavailable in the searched local source bounds.

## Identity and Grounding

Mint recomputation and `PATHS.tsv:2939` agree. Default resolution is
`gold_unmatched`, UNGROUNDED, without a predicate or extra parent. The CLASS
`CONFIRM_UNGROUNDED` decision at `curation/decisions.tsv:1231` preserves that
identity and produces `curated_confirm_ungrounded_from_gold_unmatched`.
One source concept and zero item-reviewed sources correctly yield SEEDED.
The absent mapping predicate agrees with retained source identity; the
narrow-match endpoint defect found in other records does not apply here.

The ENVO:00002123 parent comes from the independent GOLD parent-path pass,
not this decision. The complete `bioreactor.yaml` parent was read in sections.
Its organism/taxon observations, parameter bands and causal graph are not
assertions about this child and were not imported as child evidence.

Current [ENVO bioreactor metadata](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002123)
confirms an active containment-unit class, agreeing with the local definition
at `ontology_terms.tsv:7219`. A culture, its cultivation process and the
apparatus containing it are distinct possible referents. The bare label and
unassessed CLASS decision do not settle which referent this source bin means.
The source hierarchy establishes context, not on its own strict subsumption.

## Evidence

An exact-field/pipe-member scan of all 14 raw TSVs found:

- `gold_ecosystem_paths.tsv:882`: depth three; nodes 3517, 3850 and 4283;
  one ORGANISM assertion and zero other tree counters. The displayed first
  node, three-node note and count/unit reproduce this inventory.
- `gold_path_biosamples.tsv:441`: 28 BIOSAMPLE observations under node 4283.
  They are not another 28 organisms and do not replace the attestation unit.
- `gold_studies.tsv:566` and :2801: Gs0110122 and Gs0145062 respectively,
  each associated only with this exact path in that inventory.

Neither direct study page supplied usable metadata; exact-accession searches
found no usable primary result. Original sample identities remain unverified.
No exact target triad, named-taxon or environmental-parameter row was found.
The child inoculum path's five ORGANISM assertions, 33 BIOSAMPLE observations
and studies belong to that distinct path, not this record.

The current [GOLD classification workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
confirms node 4283 at row 90, with two trailing Unclassified fillers, and
separately places the inoculum child at row 89. It does not independently
verify historical nodes 3517/3850 or source counts. Download: 84,174 bytes,
SHA256 `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
This is classification evidence, not an ontology is-a axiom.

A bounded ignored-inclusive candidate search found active
[BTO:0001982 chemostat culture](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0001982),
whose definition concerns bacterial populations maintained in a controlled
steady state. Its local superclass is
[BTO:0000214 cell culture](https://www.ebi.ac.uk/ols4/api/ontologies/bto/terms?obo_id=BTO%3A0000214),
not a containment unit. These primary ontology definitions distinguish culture
from apparatus but do not establish that every observation in this GOLD bin
is a bacterial chemostat culture. No exact replacement is established.

The parent overlay's Hoskisson/Hobbs review, PMID:16207900, was inspected at
the abstract level as a contextual lead, not primary proof of this bin's
identity or a source for new mechanism claims. No full-text claim is made.

## Completeness

Ignored-inclusive searches for the exact ID, label, stem, path and node covered
curation, raw inventories, path/retirement registries, configuration, docs,
tests, history, research, its manifest and prior reports. They found the
decision and source rows, related parent-overlay prose and child references,
but no target-owned definition, exclusion, causal overlay, research entry,
retirement or previous individual review. Contextual mentions are not reviews.

An ignored-inclusive filename search of `build`, `data/raw` and the configured
kg-microbe `data` tree found no original GOLD node/edge dumps, goldData.xlsx
or biosample-sweep intermediate. The current OAK BTO cache exists. The public
path workbook is not the missing bulk source. No gene, strain, regulator,
pathway or expression assertion makes iModulonDB applicable. Empty optional
biology is not a defect or permission to copy the parent's graph.

## Findings

Zero blockers, one major finding, zero minor findings.

1. **Major: unsubstantiated containment-unit parent.** The generated
   `parent_habitats: ENVO:00002123` asserts strict is-a, but available source
   evidence only places an undefined continuous-culture category in a
   bioreactor context. The class-screened decision has not assessed the
   culture/material/process/apparatus boundary. This is an unsupported
   hierarchy assertion, not a conclusive claim that GOLD can only mean a
   process or that the record must be NOT_APPLICABLE. Owners:
   `curation/decisions.tsv`, a supported definition in
   `curation/term_requests.tsv`, and the source-edge control in
   `curation/gold_parent_exclusions.tsv` if the parent proves contextual.

## Recommended Edits

Perform an item-level assessment of the exact source bin and original sample
metadata. State explicitly whether the maintained concept is a continuous-
culture apparatus/environment or cultured material; retain a true microbial
habitat even when a technique is involved. Do not equate the whole bin to the
narrower chemostat-culture candidate merely by association.

If the concept is material in a reactor, suppress only the context parent
through the exact-source exclusion table and choose a supported material
genus, with an evidence-backed definition where needed. If source evidence
supports a kind of apparatus, document that meaning before endorsing the
strict parent. Preserve the minted identity, all three historical nodes,
source units and honest lifecycle. Do not hand-edit generated YAML.

## Follow-up Checks

Regress default/curated resolution, the independent parent-path contribution,
source-count units, node collapse, lifecycle and separation from the inoculum
child. Authorized curation requires session history, dry seed, inspected
canary, strict/provenance/history/corpus checks and full QC. A schema or label
pass alone cannot prove the repaired scope. This review does not certify
SSSOM/KGX readiness or current kg-microbe model compatibility.

## Additional Notes

Only this new report was written for this target. No scientific input,
generated record/page, curation history/status or GitHub item changed. No
paid research or delegation was used. The contextual parent read is not a
new completed review of that parent. The workbook was parsed in memory after
resetting its incorrectly declared A1-only worksheet dimensions.
