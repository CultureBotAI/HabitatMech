# YAML Record Review: drinking water

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/drinking_water.yaml
- Started UTC: 2026-10-01T20:52:00Z
- Finished UTC: 2026-10-01T21:00:30Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/drinking_water.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00003064` |
| Label | `drinking water` |
| Category | `AQUATIC` |
| Generated or maintained | Generated from committed raw inventories, the vendored ontology slice, and `data/habitats/PATHS.tsv`; `data/habitats/` remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:714` maps `ENVO:00003064` to `drinking_water` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source concept reviewed | `habitatmech:PREGO.47ebd70614`, minted from `PREGO:ENVO:00003064` |

The generated record harmonizes the PREGO ontology-class habitat
`ENVO:00003064` directly onto the same ENVO identity. It carries the ENVO
definition, the ENVO `fresh water` parent, PREGO's plural lexical variant as a
related synonym, ENVO's `potable water` exact synonym, one PREGO source
attestation, and the 14 top PREGO taxon associations for this term. No curated
definition, xrefs, environmental parameters, record-level evidence,
causal-graph overlays, discussions, or dataset links are present.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -name '*-drinking_water.md' -print` | Passed; no prior exact `drinking_water` report was present before this report was written. `find` included ignored files under `reports/yaml_record_review`. |
| `just validate data/habitats/aquatic/drinking_water.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/drinking_water.yaml` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just validate-all data/habitats/aquatic/drinking_water.yaml` | Passed; this delegates to the strict validator and again scanned 1 file with 0 errors. |
| Reference validator | Not applicable; this record has no record-level `evidence`, no causal graph, and no DOI, PMID, or URL `EvidenceItem` references. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just term-requests-check` | Passed; the generated ENVO term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 records were expected, 3,206 were found on disk, and there were 0 missing, extra, or differing records. |
| `just render-check` | Passed; rendered 3,206 habitat pages, 231 redirect stubs, 8 categories, and 123 term requests into a temporary tree; `pages/` is in step with the corpus. |
| `just worklist --out /tmp/habitatmech-record-review-worklist.tsv --limit 20` | Passed; 0 ungrounded records are still undecided and 1,810 decisions are on file. |
| `just report --out /tmp/habitatmech-record-review-report.tsv --ungrounded-top 0 --slug-drift-top 0` | Passed; wrote the complete 3,206-record report. Line 714 reports `ENVO:00003064` as `AQUATIC`, `EXACT`, `SEEDED`, PREGO-only, with 1 parent, 14 source assertions, 14 taxa, and no parameters or causal graphs. |
| `git diff --check` | Passed before report creation. |

## Identity and Grounding

The record's identifier, label, definition, definition source, exact synonym,
and exact grounding all come from the vendored ENVO slice. The
`data/raw/ontology_terms.tsv:7376` row for `ENVO:00003064` has ontology `ENVO`,
label `drinking water`, the same definition copied into the YAML, the synonym
`potable water`, `directly_referenced` set to `TRUE`, and `label_only` set to
`FALSE`.

The broader-parent edge is also an ontology edge, not a source-path inference.
`data/raw/ontology_subclass_edges.tsv:5495` asserts
`ENVO:00003064 rdfs:subClassOf ENVO:00002011`, and
`data/raw/ontology_terms.tsv:7173` labels `ENVO:00002011` as `fresh water`.
The `AQUATIC` category is consistent with the seeder's ENVO category inference:
`ENVO:00003064` is a descendant of the `ENVO:00002006` `liquid water` anchor
used for aquatic ENVO terms.

PREGO concepts are already ontology CURIEs and are seeded as exact
self-groundings. `src/habitatmech/seed.py` applies a default
`Resolution(row["prego_id"], "EXACT", route="prego_self_grounded")`, while still
minting a curator-addressable source key. For this row, the source key is
`habitatmech:PREGO.47ebd70614`.

That PREGO self-grounding has not been promoted by a curator decision.
An ignored/hidden-inclusive exact search over `curation`, `history`, `research`,
`reports/yaml_record_review`, `data/habitats`, and `pages/habitats` found no
`habitatmech:PREGO.47ebd70614` reference, so the generated
`mapping_status: SEEDED` is appropriate. It means the identity is mechanically
plausible and traceable, not yet endorsed by an item-level review row.

## Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| The generated record denotes the ENVO class `ENVO:00003064` `drinking water`. | `data/habitats/aquatic/drinking_water.yaml:1` uses `ENVO:00003064`, and `data/raw/ontology_terms.tsv:7376` gives the same CURIE and label. | Supported exactly. |
| `ENVO:00003064` is current and directly represented in the vendored slice. | `data/raw/ontology_terms.tsv:7376` leaves the `deprecated` column empty, sets `directly_referenced` to `TRUE`, and sets `label_only` to `FALSE`. | Supported exactly. |
| The ENVO definition in the YAML is source-derived. | The YAML's `definition` and `definition_source: ENVO` match the definition column of `data/raw/ontology_terms.tsv:7376`. | Supported exactly. |
| The only generated parent, `ENVO:00002011`, is a broader ENVO term for fresh water. | `data/raw/ontology_subclass_edges.tsv:5495` asserts the direct subclass edge, and `data/raw/ontology_terms.tsv:7173` labels the object `fresh water`. | Supported exactly. |
| PREGO attests 14 taxa for the `ENVO:00003064` habitat with max score 4 and the `annotated_genomes_isolates` channel. | `data/raw/prego_habitats.tsv:316` has `prego_id=ENVO:00003064`, `taxon_count=14`, `direct_assertion_count=14`, `max_prego_score=4`, `channels=annotated_genomes_isolates`, and `prego_synonyms=drinking water\|drinking waters`. | Supported exactly. |
| The generated source attestation reports PREGO's own assertion count and score without changing the unit. | `src/habitatmech/seed.py` stores PREGO `taxon_count` as `assertion_count`, assigns `assertion_unit: TAXON`, stores `max_prego_score` as `score`, and copies the PREGO `channels` string into `evidence_channels`. | Supported exactly. |
| The 14 YAML `characteristic_taxa` entries are the top PREGO rows for this exact habitat. | `data/raw/prego_habitat_taxa.tsv:6741-6754` has the same 14 rank-ordered `ENVO:00003064` rows, NCBITaxon CURIEs, labels, and scores that appear in the generated YAML. | Supported exactly. |
| The generated taxa are reported-from associations, not curator claims that these taxa typify drinking water. | The YAML omits `is_characteristic` from each taxon, and `docs/HARMONIZATION.md` states that the seeder does not set `is_characteristic` because PREGO attests that a taxon was reported from a habitat, which is weaker than typifying it. | Supported; no overclaim found. |
| No causal overlay is attached to this record. | Ignored/hidden-inclusive exact searches found no `ENVO:00003064` reference in `curation/causal_graphs`, and `find curation/causal_graphs -maxdepth 1 -type f -name '*drinking*' -print` found no candidate drinking-water overlay. | Supported exactly. |

No claim-level literature evidence is attached to the record, and no causal
edges or evidence snippets need source-text review. The structured iModulonDB
cross-check is not applicable: this habitat record names no gene, locus tag,
UniProt accession, regulator, pathway, stress response, trait, or
transcriptomics dataset.

## Completeness

The generated record is complete for the current raw PREGO row and vendored
ENVO rows. It has the ENVO identity, label, definition, exact synonym, direct
ENVO parent, PREGO habitat attestation, PREGO related synonym, and every
committed top-taxon row for `ENVO:00003064`.

Empty curator-owned slots are also appropriate. Ignored/hidden-inclusive exact
searches covered `curation`, `history`, `research`, `reports/yaml_record_review`,
`data/raw`, `data/habitats/PATHS.tsv`, `data/habitats`, `pages/habitats`,
`conf/id_label_targets.yaml`, `data/habitats/RETIRED.tsv`, and
`curation/redirects_retracted.tsv` for `ENVO:00003064`, `drinking_water`,
`drinking water`, and `habitatmech:PREGO.47ebd70614`. They found the target ENVO
term, locked path, PREGO habitat row, PREGO taxa, generated YAML, rendered page,
and adjacent GOLD drinking-water records; they found no prior exact YAML review,
no decision row for the target PREGO source concept, no term request, no causal
overlay, no history record, no id-label residual, no retired URL row, and no
redirect retraction.

The separate GOLD drinking-water records are expected siblings, not duplicates.
`data/habitats/aquatic/drinking_water__6d6ef579.yaml` represents the GOLD path
`Environmental > Aquatic > Freshwater > Drinking water` as a narrower source
concept under the ENVO `drinking water` class; `data/habitats/engineered/drinking_water__0a661d20.yaml`
represents the GOLD path
`Engineered > Built environment > Drinking water treatment plant > Drinking water`.
Keeping both minted GOLD leaves separate avoids conflating source-path context
with the general ENVO class.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If a future curation pass reviews this PREGO source concept at
item depth, the maintained input would be `curation/decisions.tsv` keyed by
`habitatmech:PREGO.47ebd70614`, and the narrowest proof would be:

- `just seed-canary ENVO:00003064`
- `just validate data/habitats/aquatic/drinking_water.yaml`
- `just validate-strict data/habitats/aquatic/drinking_water.yaml`
- `just verify-corpus --max-diffs 1`

## Additional Notes

The rendered page `pages/habitats/drinking-water-envo-00003064.html` mirrors
the YAML: it displays `SEEDED`, includes the machine-generated warning, renders
the PREGO source attestation, links the sole `fresh water` parent, lists all 14
PREGO taxa as reported-from associations with no corroboration markers, and
lists `drinking waters` and `potable water` under "Also called".
