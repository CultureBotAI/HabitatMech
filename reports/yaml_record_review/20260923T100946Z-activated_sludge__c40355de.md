# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/activated_sludge__c40355de.yaml
- Started UTC: 2026-09-23T10:09:46Z
- Finished UTC: 2026-09-23T10:09:46Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.2edc84b874` |
| Label | `Activated sludge` |
| Path | `data/habitats/engineered/activated_sludge__c40355de.yaml` |
| Category | `ENGINEERED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Generated or maintained | Generated from `data/raw/gold_ecosystem_paths.tsv`, lexical ENVO grounding, and `data/habitats/PATHS.tsv`; not a maintained curation input |
| Source concept | GOLD `gold.ecosystem:8222` for `Engineered > Bioreactor > SBR-EBPR > Anaerobic-Aerobic > Activated sludge` |
| Locked slug | `data/habitats/PATHS.tsv:1631` maps `habitatmech:GOLD.2edc84b874` to `activated_sludge__c40355de` |

I read the full generated record. It contains generated identity, category,
grounding status, two parents, one GOLD source attestation, and the initial
`SEEDED_FROM_SOURCES` history event. It has no generated definition, synonyms,
environmental parameters, characteristic taxa, evidence items, causal graphs,
discussions, or dataset links.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/engineered/activated_sludge__c40355de.yaml` | Pass: `No issues found` |
| `just validate-strict data/habitats/engineered/activated_sludge__c40355de.yaml` | Pass: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass: 32 causal-graph curation files and 32 graphs validated |
| `just term-requests-check` | Pass: `term-request table is current (109 terms)` |
| `just validate-history` | Pass: `No issues found`; 77 history records valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass: expected 3,206 records, found 3,206 on disk, 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Pass: 0 ungrounded records still undecided; 1,810 decisions on file |
| `just report` | Pass: corpus report completed for 3,206 records |
| `git diff --check` | Pass |
| Reference validator | Not applicable: the target has no `evidence`, `causal_graphs`, or reference-bearing maintained overlay to validate |

## Identity and Grounding

The target is a minted GOLD-path record for `Engineered > Bioreactor >
SBR-EBPR > Anaerobic-Aerobic > Activated sludge`.
`data/raw/gold_ecosystem_paths.tsv:1208` contains exactly that path, gives it
the label `Activated sludge`, records depth `5`, records one GOLD ecosystem
node ID `gold.ecosystem:8222`, and supports the generated source attestation.
Its organism, study, biosample, and total assertion counts are all zero, so the
generated attestation correctly omits `assertion_count` and `assertion_unit`.

The GOLD MIxS triad inventory independently corroborates that the sampled
material for this path was activated sludge. `data/raw/gold_path_triads.tsv:53-55`
records 59 samples from one study with one distinct value in each slot:
`ENVO:01000313` `anthropogenic environment` for the broad slot,
`ENVO:00002123` `bioreactor` for the local slot, and `ENVO:00002046`
`activated sludge` for the medium slot.

The ontology parent is supported. `data/raw/ontology_terms.tsv:7191` gives
`ENVO:00002046` the canonical label `activated sludge`, and
`data/raw/ontology_subclass_edges.tsv:5293` places it under `ENVO:00002044`;
`data/raw/ontology_terms.tsv:7189` labels `ENVO:00002044` as `sludge`. That
supports keeping the GOLD path minted and carrying generic activated sludge as
a broader parent.

The source-path parent is not supported as an is-a parent.
`data/habitats/PATHS.tsv:2703` maps `habitatmech:GOLD.c07aaa941d` to
`anaerobic_aerobic__c424253c`, and
`data/habitats/engineered/anaerobic_aerobic__c424253c.yaml` is the seeded
record for `Engineered > Bioreactor > SBR-EBPR > Anaerobic-Aerobic`. Its GOLD
source row is `data/raw/gold_ecosystem_paths.tsv:1207`, which labels the
concept `Anaerobic-Aerobic` and collapses `gold.ecosystem:8219` and
`gold.ecosystem:8220`. The only maintained decision for
`habitatmech:GOLD.c07aaa941d` is a class-level `CONFIRM_UNGROUNDED` row at
`curation/decisions.tsv:1075`; that row explicitly says whether the concept is
a habitat at all was not assessed.

The sibling child corroborates the reading. GOLD also has `Engineered >
Bioreactor > SBR-EBPR > Anaerobic-Aerobic > Sludge` at
`data/raw/gold_ecosystem_paths.tsv:1209`, and the generated
`data/habitats/engineered/sludge__e608f05a.yaml` record keeps generic
`ENVO:00002044` `sludge` as the ontology parent. The shared GOLD path parent
therefore groups activated sludge and sludge materials under the same
anaerobic-aerobic SBR-EBPR context; it does not establish that either material
is a strict kind of that operational context.

No item-level curation decision currently reviews
`habitatmech:GOLD.2edc84b874`. An exact ignored/hidden-inclusive search for the
child identifier found only the generated record and `PATHS.tsv`; exact
ignored/hidden-inclusive searches for the child source node and full GOLD path
found only the generated record, raw GOLD path row, and raw GOLD triad rows
under the searched repository paths.

## Evidence

The generated record carries no literature evidence or mechanism evidence, and
none is required for the raw GOLD attestation itself.

| Claim | Checked evidence | Assessment |
|---|---|---|
| GOLD attests `Engineered > Bioreactor > SBR-EBPR > Anaerobic-Aerobic > Activated sludge`. | `data/raw/gold_ecosystem_paths.tsv:1208` | Supported. The path, label, depth, one-node identity, and zero direct assertion count agree with the generated `source_attestations` item. |
| The GOLD MIxS medium slot for this path is activated sludge. | `data/raw/gold_path_triads.tsv:55` | Supported. The row reports `ENVO:00002046` `activated sludge` as the unanimous medium term for 59 samples from one study. |
| The target path can use generic activated sludge as a broader parent. | `data/raw/ontology_terms.tsv:7191`; `data/raw/ontology_subclass_edges.tsv:5293` | Supported. `ENVO:00002046` is `activated sludge` and is a subclass of sludge. |
| The target path is a kind of `Engineered > Bioreactor > SBR-EBPR > Anaerobic-Aerobic`. | Generated from the GOLD parent path alone; the parent has only a class-level decision that did not assess habitat identity. | Unsupported. Anaerobic-aerobic is an operational SBR-EBPR context; activated sludge is a material in that context, not a subtype of the context itself. |
| The parent `Anaerobic-Aerobic` record is raw-source backed. | `data/raw/gold_ecosystem_paths.tsv:1207`; `data/habitats/engineered/anaerobic_aerobic__c424253c.yaml:9-15` | Supported as a source concept, not as a reviewed broader parent of this activated-sludge child. |

## Completeness

- No generated definition, curator-authored term request, environmental
  parameter, characteristic taxon, discussion, dataset, or causal graph is
  expected for a purely seeded GOLD record that has not yet received item-level
  review.
- Exact ignored/hidden-inclusive searches for
  `habitatmech:GOLD.2edc84b874`, `activated_sludge__c40355de`,
  `gold.ecosystem:8222`, `Engineered > Bioreactor > SBR-EBPR >
  Anaerobic-Aerobic > Activated sludge`, `habitatmech:GOLD.c07aaa941d`,
  `gold.ecosystem:8219`, `gold.ecosystem:8220`, `Engineered > Bioreactor >
  SBR-EBPR > Anaerobic-Aerobic`, `gold.ecosystem:8221`, `Engineered >
  Bioreactor > SBR-EBPR > Anaerobic-Aerobic > Sludge`, `ENVO:00002046`, and
  `ENVO:00002044` found the cited raw, triad, path-lock, maintained parent
  curation, ontology-slice, and generated-record rows outside `build/`,
  `pages/`, and `data/text_map/`.
- The target identifier had no hits in `curation/`, `research/`, `history/`, or
  pre-existing `reports/yaml_record_review/`, with ignored and hidden files
  included.
- The full target GOLD path had no hits in `data/raw/gold_studies.tsv` or
  `data/raw/gold_path_biosamples.tsv`; the absence search included ignored and
  hidden files outside `build/`, `pages/`, and `data/text_map/`.
- No exact prior report existed for `activated_sludge__c40355de` before this
  report was written: `find reports/yaml_record_review -maxdepth 1 -type f
  -name '*-activated_sludge__c40355de.md' -print` returned no paths.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-ACTSLUDGE-C40355DE-001 | major | `parent_habitats` asserts `habitatmech:GOLD.2edc84b874` is a kind of `habitatmech:GOLD.c07aaa941d` `Anaerobic-Aerobic`, but the child is `Activated sludge` and the supported ontology parent is `ENVO:00002046` `activated sludge` under `ENVO:00002044` `sludge`. `parent_habitats` is an is-a relation, and this path edge turns GOLD's anaerobic-aerobic SBR-EBPR context into the false claim that activated sludge is the operational context itself. | Add an item-level decision for `habitatmech:GOLD.2edc84b874` in `curation/decisions.tsv`; if the concept stays minted, add a `curation/term_requests.tsv` definition with `parent_mode=REPLACE` so the generated record keeps `ENVO:00002046` and drops the inherited `Anaerobic-Aerobic` parent. |

## Recommended Edits

1. Resolve `habitatmech:GOLD.2edc84b874` at item depth in
   `curation/decisions.tsv`.
2. If `Engineered > Bioreactor > SBR-EBPR > Anaerobic-Aerobic > Activated
   sludge` denotes generic activated sludge rather than an
   SBR-EBPR-specific subtype, ground it directly to `ENVO:00002046` so the
   GOLD attestation merges into the existing activated-sludge identity.
3. If the anaerobic-aerobic SBR-EBPR context is materially narrower than
   generic activated sludge, keep the source concept minted, use a
   `GROUND_AS_PARENT` decision to `ENVO:00002046`, and add a definition in
   `curation/term_requests.tsv` with `parent_mode=REPLACE` so the next seed no
   longer inherits the false `Anaerobic-Aerobic` source-path parent.
4. Regenerate through the seeder rather than editing
   `data/habitats/engineered/activated_sludge__c40355de.yaml` directly.

## Follow-up Checks

- `just seed`
- `just seed-canary habitatmech:GOLD.2edc84b874`
- Inspect `data/habitats/engineered/activated_sludge__c40355de.yaml` or
  confirm the record intentionally merged away after an exact `GROUND`.
- `just seed-apply --force`
- `just validate-strict data/habitats/engineered/activated_sludge__c40355de.yaml`
  if the record stays minted; otherwise validate the record that absorbed its
  source attestation.
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- The false parent is not caused by a hand edit: `just verify-corpus --max-diffs
  1` reproduced the generated YAML exactly from committed raw inputs.
- The parent decision at `curation/decisions.tsv:1075` explains only that no
  vendored term matched `Anaerobic-Aerobic` by the class-level search routes.
  It does not review the parent as a habitat, does not validate source-path
  child edges, and does not promote the child target to `REVIEWED`.
- A reference validator was recorded as not applicable because this record has
  no references or causal-graph overlay; the edge that needs curation is a
  generated hierarchy edge, not a reference-backed mechanism claim.
