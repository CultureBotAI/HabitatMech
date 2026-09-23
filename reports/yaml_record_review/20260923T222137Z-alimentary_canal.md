# YAML Record Review

- Repository: `CultureBotAI/HabitatMech`
- Record: `data/habitats/host_associated/alimentary_canal.yaml`
- Started UTC: `2026-09-23T22:18:35Z`
- Finished UTC: `2026-09-23T22:21:37Z`
- Verdict: `pass with minor issues`

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/host_associated/alimentary_canal.yaml` |
| Class | `HabitatRecord` |
| Identifier | `BTO:0000058` |
| Label | `alimentary canal` |
| Definition source | `BTO` |
| Category | `HOST_ASSOCIATED` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |

This is a generated BTO/PREGO record owned by upstream inputs, not by hand edits
under `data/habitats/`. Its path is pinned by `data/habitats/PATHS.tsv`, which
maps `BTO:0000058` to `alimentary_canal`.

## Validation

| Check | Result |
|---|---|
| `find reports/yaml_record_review -maxdepth 1 -type f -name '*-alimentary_canal.md' -print` | Passed; no prior exact report was present. |
| `find curation/causal_graphs -maxdepth 1 -type f -name '*alimentary_canal*' -print` | Passed; no candidate causal overlay was present. |
| `rg --no-ignore --hidden -n --fixed-strings ... curation data/raw data/habitats reports research src tests conf history -g '!data/text_map/**' -g '!pages/**' -g '!build/**'` | Passed; bounded exact searches found the BTO ontology row, PREGO raw rows, the `PATHS.tsv` slug row, the generated target record, the BTO parent edge, and no maintained curation decision, term request, causal overlay, history record, research report, or auxiliary report for `BTO:0000058`. Ignored and hidden files were included. |
| `just validate data/habitats/host_associated/alimentary_canal.yaml` | Passed; `linkml-validate` reported no issues. |
| `just validate-strict data/habitats/host_associated/alimentary_canal.yaml` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| Focused causal-graph validation | Not applicable; the record has no maintained overlay under `curation/causal_graphs/`. |
| Reference validator | Not applicable; the record has no DOI, PMID, URL, causal-edge evidence, dataset, or discussion references to check. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; no issues found and 77 history records validated. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 on disk, 0 missing, 0 extra, and 0 differing. |
| `just worklist --limit 2000` | Passed; the command reported 0 ungrounded records still undecided and 1,810 decisions on file. |
| `just report` | Passed; the corpus report completed for 3,206 records. |
| `git diff --check` | Passed before report creation. |

## Identity and Grounding

The record denotes `BTO:0000058` `alimentary canal`, and the generated
identifier, label, definition, and `definition_source: BTO` exactly mirror
`data/raw/ontology_terms.tsv`.

The only source concept feeding the record is PREGO `BTO:0000058`. PREGO
concepts already use ontology CURIEs, so `src/habitatmech/seed.py` self-grounds
this source concept to `BTO:0000058` through the `prego_self_grounded` route.
No item-level `curation/decisions.tsv` row exists for the PREGO curator key
`habitatmech:PREGO.b22e169340`, so `mapping_status: SEEDED` is expected even
though the generated grounding is exact.

The single generated parent is an ontology parent. `data/raw/ontology_terms.tsv`
labels `BTO:0001491` as `viscus`, and `data/raw/ontology_subclass_edges.tsv`
asserts `BTO:0000058 rdfs:subClassOf BTO:0001491`.

## Evidence

The PREGO source attestation is faithful to `data/raw/prego_habitats.tsv`. The
raw row has `taxon_count` 114, `direct_assertion_count` 114, `max_prego_score`
4, `channels` `annotated_genomes_isolates|environmental_samples`, and 16 PREGO
synonym strings, 15 of which are non-label strings emitted as
`RELATED_SYNONYM`.

The 25 generated taxon associations match `data/raw/prego_habitat_taxa.tsv`
rows 8 through 32:

- each generated `taxon_id`, `score`, `rank`, and `candidate_pool` matches the
  PREGO row for the same rank;
- rows 14 and 15 omit `taxon_label` because the raw labels for
  `NCBITaxon:541000` and `NCBITaxon:629395` are blank;
- none of the generated rows carries `is_characteristic: true`, so the PREGO
  occurrence ranking is not upgraded to a curated characteristic claim.

The record has no `environmental_parameters`, causal graph, claim-level
evidence block, discussion item, or dataset usage. No maintained input
currently asserts those fields.

## Completeness

The record is complete enough as a generated PREGO/BTO seed. It preserves the
source-owned BTO definition, the BTO ontology parent, the PREGO source
attestation, the first 25 ranked PREGO taxon associations out of the 114-taxon
PREGO candidate pool, and the generated `SEEDED_FROM_SOURCES` history event.

The generated empty fields are expected for the current maintained inputs:

- no item-level curation decision is keyed by `habitatmech:PREGO.b22e169340`;
- no term request is keyed by `BTO:0000058`;
- no causal overlay file matches `alimentary_canal`;
- no record-specific history or research report exists for this exact source
  concept.

Bounded, ignored-inclusive exact searches for `BTO:0000058`,
`habitatmech:PREGO.b22e169340`, `alimentary canal`,
`alimentary_canal`, `BTO:0001491`, `NCBITaxon:541000`, and
`NCBITaxon:629395` across curation inputs, raw inputs, generated YAML, history,
reports, research, source, tests, and configuration found the expected ontology,
PREGO, path-lock, and generated-record rows. Generated `data/text_map/`,
`pages/`, and `build/` files were excluded; ignored and hidden files were
included.

## Findings

### Minor

| Finding | Evidence | Maintained owner |
|---|---|---|
| Some generated PREGO related synonyms are broad or mechanically inflected strings whose scope is not locally re-reviewed. | `data/raw/prego_habitats.tsv` preserves PREGO synonym strings such as `digestive system`, `digestive systems`, and `alimentary tractic`; `data/habitats/host_associated/alimentary_canal.yaml` copies them as `RELATED_SYNONYM` with `source: PREGO`. The record is faithful to the raw row, but downstream synonym lookups should not treat those strings as a HabitatMech-curated exact synonym audit. | `data/raw/prego_habitats.tsv`; `src/habitatmech/extract.py` |

No blocker or major findings found.

## Recommended Edits

1. Leave `data/habitats/host_associated/alimentary_canal.yaml` generated and do
   not add a `curation/decisions.tsv` row merely to restate that PREGO
   `BTO:0000058` is exactly BTO `alimentary canal`.
2. If broad or mechanically inflected PREGO related synonyms create false
   lookup behavior, add a maintained synonym-suppression mechanism for
   source-owned PREGO synonyms or fix the upstream PREGO vocabulary rows, then
   refresh the raw inventories.

## Follow-up Checks

- Run `just seed`.
- Run `just seed-canary BTO:0000058` and inspect
  `data/habitats/host_associated/alimentary_canal.yaml` if PREGO synonym
  handling changes.
- Run `just validate data/habitats/host_associated/alimentary_canal.yaml`.
- Run `just validate-strict data/habitats/host_associated/alimentary_canal.yaml`.
- Run `just verify-corpus --max-diffs 1`.
- Run `just validate-history` after any future curation session that changes a
  maintained input.

## Additional Notes

The vendored UBERON slice also contains `UBERON:0001555` `digestive tract`,
with `alimentary canal` as an ontology synonym, but that is a separate reviewed
record attested by GOLD `Digestive tube`. HabitatMech currently keeps these
vendored BTO and UBERON anatomy identifiers separate, and `SAME_AS` decisions
are restricted to minted HabitatMech identifiers rather than ontology-to-
ontology merges.
