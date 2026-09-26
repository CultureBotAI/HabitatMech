# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/pooled_tissues.yaml`
- Started UTC: 2026-09-26T18:13:54Z
- Finished UTC: 2026-09-26T18:13:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/pooled_tissues.yaml` |
| Identifier | `habitatmech:GOLD.56790b4070` |
| Label | `Pooled tissues` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `UNGROUNDED` |
| Mapping status | `SEEDED` |
| Generated status | Generated from committed inventories and `curation/decisions.tsv`; `data/habitats/PATHS.tsv` pins the identifier to `pooled_tissues` |
| Source concept | GOLD `Host-associated > Mammals > Multiple systems > Multiple organs > Pooled tissues` |

The record has one GOLD source attestation and one parent inherited from the
immediate GOLD parent path. It has no definition, synonyms, xrefs,
environmental parameters, characteristic taxa, evidence items, causal graphs,
discussions, or datasets.

## Validation

| Check | Result |
|---|---|
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Passed; wrote 953 ungrounded rows, with `Pooled tissues` immediately after aquatic `Mine water` |
| `just report` | Passed; current corpus has 3,206 records, 953 `UNGROUNDED` records, and 830 class-level sweeps |
| `just validate data/habitats/host_associated/pooled_tissues.yaml` | Passed |
| `just validate-strict data/habitats/host_associated/pooled_tissues.yaml` | Passed; 1 file scanned, 0 error rows |
| `just validate-causal-all` | Passed; 32 causal-graph curation files validated |
| `just term-requests-check` | Passed; the generated term-request table is current with 109 terms |
| `just validate-history` | Passed; 77 history records are valid |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 records found, no missing, extra, or differing records |
| `git diff --check` | Passed |

No separate reference validator is exposed in the HabitatMech `justfile`.
This generated record has no `EvidenceItem`, causal-graph edge, discussion, or
dataset references to validate.

## Identity and Grounding

The generated identity and source attestation match the maintained GOLD
inventory:

- `data/habitats/PATHS.tsv` maps `habitatmech:GOLD.56790b4070` to
  `pooled_tissues`.
- `data/raw/gold_ecosystem_paths.tsv` records the exact Multiple organs
  Pooled tissues source path with one GOLD ecosystem node,
  `gold.ecosystem:6423`, and `organism_count` 3.
- The YAML `source_attestations` entry preserves that node ID, label, source
  path, and three GOLD organism assertions with `assertion_unit: ORGANISM`.

The class-level curation decision is the only decision for this minted source
concept:

```tsv
habitatmech:GOLD.56790b4070	CONFIRM_UNGROUNDED				claude-opus-5	2026-08-12	Class-level sweep (see docs/HARMONIZATION.md#class-level-sweep): no term in the vendored slice matched this label by any search route. Whether the concept is a habitat at all was NOT assessed, so this is not yet a term-request candidate.	CLASS
```

That row explains why the generated record remains `UNGROUNDED` and `SEEDED`.
It does not decide whether GOLD's pooled-tissue leaf is a real host-associated
habitat, a mixture of several body sites, or a sampling artifact.

The maintained GOLD inventory has no MIxS triad row for the exact Multiple
organs target, but it has auxiliary context that constrains the review:

- `data/raw/gold_path_biosamples.tsv` counts 10 biosamples for the exact target
  path.
- `data/raw/gold_studies.tsv` records two GOLD studies that include the exact
  target path, `Gs0118454` and `Gs0159159`.
- `data/raw/gold_ecosystem_paths.tsv` also has a same-label GOLD sibling,
  `Host-associated > Mammals > Multiple systems > Soft tissue > Pooled tissues`
  with source node `gold.ecosystem:6882`.
- That Soft tissue sibling has one biosample and a single-study MIxS triad with
  `ENVO:01001000` `environmental system determined by an organism` as broad
  scale, `UBERON:0010000` `multicellular anatomical structure` as local scale,
  and `UBERON:0000479` `tissue` as medium.

The Soft tissue sibling's triad is not direct evidence for this Multiple organs
record, but it makes the same-label sibling and `UBERON:0000479` `tissue` a
near-neighbor pair to compare during item-level review.

The worklist candidates `UBERON:0000479` `tissue` and `UBERON:0002481`
`bone tissue` are lexical or synonym hits. `UBERON:0000479` is plausible as a
strict broader term only if item review decides that GOLD is naming mammalian
tissue material rather than a mere pooled-sample handling state. `UBERON:0002481`
is an over-specific bone term and is not supported by the source path.

An ignored/hidden-inclusive exact search of `data/raw/ontology_terms.tsv` for
`pooled tissue`, `pooled tissues`, `Pooled tissue`, and `Pooled tissues` found
no direct same-label ontology term in the vendored slice.

## Evidence

The record has no curator-authored definition, parameter band, causal edge, or
external citation claim.

| YAML claim | Maintained evidence | Review |
|---|---|---|
| `identifier: habitatmech:GOLD.56790b4070` | `data/raw/gold_ecosystem_paths.tsv` canonical path `Host-associated > Mammals > Multiple systems > Multiple organs > Pooled tissues` | Supported; this is the stable hash for the source path |
| `habitat_category: HOST_ASSOCIATED` | GOLD top-level path `Host-associated` and ecosystem category `Mammals` | Supported |
| `grounding_status: UNGROUNDED` | `curation/decisions.tsv` class-level `CONFIRM_UNGROUNDED` row | Reproducible but incomplete; see Findings |
| `parent_habitats: habitatmech:GOLD.4dbae6ecfe` | Immediate GOLD parent path `Host-associated > Mammals > Multiple systems > Multiple organs`; `data/habitats/PATHS.tsv` maps the parent source to `multiple_organs__a0ce3dd7` | Supported as a generated source-path parent |
| GOLD source attestation | `data/raw/gold_ecosystem_paths.tsv` row with node `gold.ecosystem:6423` and `organism_count` 3 | Supported |

The generated `Multiple organs` parent is itself a sparse minted GOLD source
record, `habitatmech:GOLD.4dbae6ecfe`, and is only class-reviewed. That is not a
defect in this child record's source-path reproduction, but any future
item-level review of `Pooled tissues` must check whether a pooled tissue sample
is truly narrower than a multiple-organs host habitat or should instead be
related to generic tissue, the Soft tissue sibling, or a non-habitat sample
aggregation.

## Completeness

Ignored and hidden files were included in exact searches for
`habitatmech:GOLD.56790b4070`, `GOLD.56790b4070`, `Pooled tissues`,
`pooled_tissues`, and the exact GOLD source path across `data/habitats`,
`data/raw`, `curation`, `history`, `research`, and
`reports/yaml_record_review`.

Those searches found the generated YAML, the `PATHS.tsv` row, the class-level
`curation/decisions.tsv` row, the exact GOLD ecosystem-path row, the
GOLD biosample row, the two GOLD study rows containing the exact path, and the
same-label Soft tissue sibling. They found no target-specific
`curation/term_requests.tsv` row, no target-specific `history/` entry, no
committed deep-research report, and no prior exact YAML review for
`habitatmech:GOLD.56790b4070`.

Ignored/hidden-inclusive searches for `habitatmech:GOLD.9b00d0ff9a` and
`Host-associated > Mammals > Multiple systems > Soft tissue > Pooled tissues`
found the same-label sibling's generated YAML, `PATHS.tsv` row, class-level
decision row, GOLD ecosystem-path row, GOLD biosample row, GOLD triad rows, and
GOLD study row. The sibling confirms that GOLD uses `Pooled tissues` in at
least two related Mammals > Multiple systems branches; it does not prove that
the two branches are exact duplicates.

`find curation/causal_graphs -maxdepth 1 -type f -iname '*pooled*tissue*' -print`
found no target or sibling causal overlay. That is acceptable for this
seed-only GOLD review because the generated record asserts no mechanism graph.

The generated record has no taxa because the committed GOLD source inventory
does not include per-taxon rows. It has no environmental parameter rows because
the kg-microbe environments table is keyed to ontology terms such as
`UBERON:0000479` `tissue`, not to this ungrounded minted GOLD source concept.

## Findings

### Blocker

None found.

### Major

1. `habitatmech:GOLD.56790b4070` is still only class-reviewed even though its
   same-label sibling and generic tissue near miss show that the pooled-tissue
   concept needs an item-level disposition.

   Owner: `curation/decisions.tsv`; likely `curation/term_requests.tsv` if the
   record remains a novel minted host-tissue concept

   The current decision row only records that no lexical route matched
   `Pooled tissues`; it explicitly did not inspect whether the concept is a
   habitat. GOLD's source path places this node under Mammals, Multiple systems,
   and Multiple organs, but the leaf names a pooled tissue source rather than a
   single anatomical site. The record therefore needs review against three
   possibilities that have different maintained fixes: keep it as a novel
   multiple-organ tissue habitat narrower than `UBERON:0000479` `tissue`,
   merge it with the same-label Soft tissue `Pooled tissues` source concept
   after proving that GOLD is using both paths for the same pooled host-tissue
   habitat, or mark it `NOT_APPLICABLE` if the leaf only denotes sample pooling
   rather than the environment from which the microbes were isolated. Leaving it
   as only `CLASS` depth prevents `mapping_status: REVIEWED`, leaves its
   relation to generic tissue undecided, and risks a duplicate term request if
   the Soft tissue sibling is reviewed separately.

### Minor

None found.

## Recommended Edits

Replace the class-level `curation/decisions.tsv` row for
`habitatmech:GOLD.56790b4070` with an item-level decision. Read the GOLD Multiple
organs path against the same-label Soft tissue sibling,
`habitatmech:GOLD.9b00d0ff9a`, before selecting a final relation.

If the two Pooled tissues paths denote the same pooled mammalian tissue habitat,
merge one minted source concept into the other with `SAME_AS` so HabitatMech
does not publish two term requests for one concept. If they are genuinely
distinct but both are habitat concepts, keep the Multiple organs record minted
and add an explicit broader relation such as `GROUND_AS_PARENT` to
`UBERON:0000479` `tissue` only after confirming that a pooled multi-tissue
source remains a kind of tissue-associated host habitat rather than a
sample-pooling artifact.

If item review determines that `Pooled tissues` only describes combining
material from several anatomical sources after sampling, change the source
concept to `NOT_APPLICABLE` instead of requesting a novel ontology term.

## Follow-up Checks

After the item-level decision:

- Run `just seed`.
- For a non-merge decision, regenerate the target with
  `just seed-apply --force --only habitatmech:GOLD.56790b4070`.
- If a sibling `SAME_AS` decision is added, run
  `just seed-apply --force --prune`, `just redirects`, and `just render`; then
  confirm the surviving Pooled tissues record has both GOLD source paths as
  separate `source_attestations` and the absorbed record URL appears in
  `data/habitats/RETIRED.tsv`.
- Inspect `data/habitats/host_associated/pooled_tissues.yaml` or the merged
  survivor to confirm it has the chosen item-level curation history and no
  duplicate same-label term request.
- Run `just verify-corpus --max-diffs 1`; after a sibling `SAME_AS` merge, also
  run `just redirects-check` and `just render-check`.
- If a term request is added, run `just term-requests-check` and confirm the
  generated request table includes only one Pooled tissues request.
- Run `just validate data/habitats/host_associated/pooled_tissues.yaml`, or the
  merged survivor's generated file if the identifier changes.
- Run `just validate-strict data/habitats/host_associated/pooled_tissues.yaml`,
  or the merged survivor's generated file if the identifier changes.
- Run `just validate-history`.
- Run `just verify-corpus --max-diffs 1`.
- Run `just report` and confirm the worklist no longer contains
  `habitatmech:GOLD.56790b4070` as a class-level ungrounded `Pooled tissues`
  item.

## Additional Notes

This review did not launch deep research, contact GOLD, or inspect a local
kg-microbe checkout. The committed GOLD path, biosample, study, and sibling
triad inventories are enough to audit the current YAML and to identify the
maintained item-review work this sparse generated record still needs.
