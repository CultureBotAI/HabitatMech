# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml`
- Started UTC: 2026-09-22T16:36:05Z
- Finished UTC: 2026-09-22T16:36:06Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:GOLD.4caaf1fb4f` |
| Label | `Buccal mucosa` |
| Class | `HabitatRecord` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `NARROW` |
| Mapping status | `SEEDED` |
| Maintained owner | Raw GOLD and ontology rows only; no item-level curation overlay is present |
| Locked slug | `data/habitats/PATHS.tsv:1854` maps `habitatmech:GOLD.4caaf1fb4f` to `buccal_mucosa__62ec5bff` |

This is the generated GOLD record for `Host-associated > Mammals > Digestive system > Oral cavity > Buccal mucosa`. The generated YAML faithfully preserves the GOLD leaf as a path-qualified source concept, attaches generic `UBERON:0006956` `buccal mucosa` as a broader parent with `skos:narrowMatch`, keeps the mammalian GOLD `Oral cavity` path as its source parent, and records GOLD's two organism assertions on this exact leaf.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `git diff --check` | Pass; no whitespace or patch errors after this report was written |

## Identity and Grounding

The generated identifier, label, category, grounding status, parents, source attestation, and seed status are supported by maintained inputs:

- `data/raw/gold_ecosystem_paths.tsv:846` is the raw GOLD row for `Host-associated > Mammals > Digestive system > Oral cavity > Buccal mucosa`. It has depth 5, one GOLD node id, two organism assertions, zero study assertions, zero biosample assertions, and total assertion count 2.
- `data/habitats/PATHS.tsv:1854` pins `habitatmech:GOLD.4caaf1fb4f` to `data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml`.
- `data/raw/ontology_terms.tsv:13316` imports `UBERON:0006956` with label `buccal mucosa` and definition `The inner lining of the cheeks and lips.`
- `data/raw/gold_ecosystem_paths.tsv:101` is the raw GOLD parent row for `Host-associated > Mammals > Digestive system > Oral cavity`; it has two GOLD node ids, 270 organism assertions, and generates the source parent `habitatmech:GOLD.92d1e65695`.

The generated record is correctly separate from the same-label generic and human Buccal mucosa records:

- `data/habitats/host_associated/buccal_mucosa.yaml` is the PREGO/BTO exact anatomical record for the generic term `BTO:0003833`, with its own PREGO source row and one PREGO taxon assertion.
- `data/raw/gold_ecosystem_paths.tsv:2218` is `Host-associated > Mammals: Human > Digestive system > Oral cavity > Buccal mucosa`, a human-qualified GOLD path that generates the separate `habitatmech:GOLD.1a8d5400cc` sibling.

## Evidence

Every generated claim is traceable to a raw row or maintained transform:

| Claim | Nearest source | Review |
|---|---|---|
| Minted identifier `habitatmech:GOLD.4caaf1fb4f` | GOLD path minting from `Host-associated > Mammals > Digestive system > Oral cavity > Buccal mucosa` | Supported exactly |
| Label `Buccal mucosa`, category `HOST_ASSOCIATED`, source label, source path, two organism assertions, and `ORGANISM` assertion unit | `data/raw/gold_ecosystem_paths.tsv:846` | Supported exactly |
| `source_id: gold.ecosystem:4110` | sole GOLD node id in `data/raw/gold_ecosystem_paths.tsv:846` | Supported exactly |
| `mapping_predicate: skos:narrowMatch` and parent `UBERON:0006956` | path-qualified GOLD leaf matched against imported `UBERON:0006956` | Supported exactly |
| Parent `habitatmech:GOLD.92d1e65695` | GOLD parent path from `data/raw/gold_ecosystem_paths.tsv:101` | Supported exactly |
| Absence of a definition, synonym, xref, environmental parameter, characteristic taxon, causal graph, record-level evidence, discussion, and dataset | No maintained input row or overlay found for these slots | Supported by bounded exact searches |

No GOLD biosample or study side-table rows exist on the exact `Host-associated > Mammals > Digestive system > Oral cavity > Buccal mucosa` path, so this record correctly has no `datasets` block. The 122-biosample and five-study side rows for `Host-associated > Mammals > Digestive system > Oral cavity` belong to the broader `Oral cavity` parent, not to this child leaf.

## Completeness

The generated fields are complete for the maintained inputs that currently feed this record:

- The single GOLD source attestation captures the path, GOLD node id, assertion count, assertion unit, and narrow ontology match.
- Both generated parents are present: the generic UBERON anatomical class and the source-inherited mammalian GOLD oral-cavity path.
- No item-level decision, authored term request, target-specific causal graph overlay, append-only history record, dedicated deep-research report, GOLD biosample or study side-table row on the exact target path, term-request exclusion row, BacDive row, PREGO row, Madin row, or previous exact YAML review report exists for `habitatmech:GOLD.4caaf1fb4f`.

Ignored/hidden-inclusive exact searches covered `curation`, `history`, `curation/causal_graphs`, `research`, `reports`, `data/raw`, `data/habitats/PATHS.tsv`, and the generated same-label buccal mucosa records, excluding generated `build`, `data/text_map`, and `pages` trees. They found the raw GOLD row, locked path row, exact generated record, imported UBERON parent, generated GOLD oral-cavity parent, generic PREGO/BTO Buccal mucosa sibling, human GOLD Buccal mucosa sibling, and the generic Buccal mucosa YAML review that mentioned this sibling; they found no target-specific maintained artifact beyond the raw, path-lock, generated, and related report rows cited above.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

No target-specific follow-up is required. If upstream GOLD or ontology inputs change for `gold.ecosystem:4110`, regenerate the target and re-run:

- `just validate data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml`
- `just validate-strict data/habitats/host_associated/buccal_mucosa__62ec5bff.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -name '*buccal_mucosa__62ec5bff*' -print` found no pre-existing exact review report for this record before this file was written.
- Exact ignored/hidden-inclusive content searches for `habitatmech:GOLD.4caaf1fb4f`, `gold.ecosystem:4110`, `buccal_mucosa__62ec5bff`, `Host-associated > Mammals > Digestive system > Oral cavity > Buccal mucosa`, `UBERON:0006956`, `habitatmech:GOLD.92d1e65695`, and the sibling identifiers `BTO:0003833` and `habitatmech:GOLD.1a8d5400cc` found no unsupported assertion, target-specific curation overlay, or prior exact review.
