# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/other/activated_sludge.yaml`
- Started UTC: 2026-09-23T07:10:30Z
- Finished UTC: 2026-09-23T07:17:55Z
- Verdict: pass

## Target

| Field | Value |
|---|---|
| Class | `HabitatRecord` |
| Identifier | `ENVO:00002046` |
| Label | `activated sludge` |
| Category | `OTHER` |
| Grounding status | `EXACT` |
| Mapping status | `SEEDED` |
| Source concept | PREGO `ENVO:00002046` |
| Maintained owner | Generated from the PREGO inventory, vendored ENVO slice, and `data/habitats/PATHS.tsv`; generated YAML remains read-only |
| Locked slug | `data/habitats/PATHS.tsv:631` maps `ENVO:00002046` to `activated_sludge` |

This is the generated PREGO record for the ENVO class `ENVO:00002046`
`activated sludge`. PREGO already keys the habitat as an ENVO ontology class,
so the source concept and record identifier are the same CURIE.

## Validation

| Command | Result |
|---|---|
| `just validate data/habitats/other/activated_sludge.yaml` | Pass; `linkml-validate` reported `No issues found` |
| `just validate-strict data/habitats/other/activated_sludge.yaml` | Pass; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows |
| `just validate-causal-all` | Pass; 32 causal-graph curation files with 32 graphs validated |
| `just term-requests-check` | Pass; term-request table is current with 109 terms |
| `just validate-history` | Pass; 77 history records are valid against `src/habitatmech/schema/history.yaml` |
| `just verify-corpus --max-diffs 1` | Pass; expected 3206 records, found 3206, with 0 missing, 0 extra, 0 differing |
| `just worklist --limit 2000` | Pass; 0 ungrounded records are still undecided and 1810 decisions are on file |
| `just report` | Pass; the report completed and kept the corpus at 3206 records |
| `git diff --check` | Pass; no whitespace errors |

## Identity and Grounding

The record's identity is internally consistent:

- `data/raw/prego_habitats.tsv:83` attests PREGO habitat `ENVO:00002046` with ontology `ENVO`, Biolink category `biolink:OntologyClass`, `taxon_count: 914`, `direct_assertion_count: 932`, `max_prego_score: 4`, evidence channels `annotated_genomes_isolates|environmental_samples`, and synonyms `activated sludge|activated sludges`.
- `data/raw/ontology_terms.tsv:7191` gives `ENVO:00002046` the canonical label `activated sludge` and marks the class as directly referenced.
- `data/raw/ontology_subclass_edges.tsv:5293` states that `ENVO:00002046` is an `rdfs:subClassOf` `ENVO:00002044`, and `data/raw/ontology_terms.tsv:7189` labels `ENVO:00002044` as `sludge`.
- `data/habitats/PATHS.tsv:631` pins `ENVO:00002046` to the generated `activated_sludge` slug.

`grounding_status: EXACT` is appropriate because PREGO directly names the same
ENVO class used as the record identifier. `mapping_status: SEEDED` is also
expected: ignored/hidden-inclusive exact searches for `ENVO:00002046` and
`activated_sludge` under maintained `curation/` and `history/` inputs found no
item-level `curation/decisions.tsv` row, target-specific term request,
target-specific causal-graph overlay, or history entry that would promote this
seeded exact mapping to `REVIEWED`.

The generated `habitat_category: OTHER` is a PREGO-only placement, not a curated
identity claim. The record has no GOLD source attestation; committed GOLD triad
rows mention `ENVO:00002046` only as environmental-medium context for narrower
GOLD concepts, which remain separate minted records with `ENVO:00002046` as a
broader parent.

## Evidence

| Claim | Nearest source | Review |
|---|---|---|
| PREGO contains an ENVO habitat concept for `activated sludge`. | `data/raw/prego_habitats.tsv:83`; `data/raw/ontology_terms.tsv:7191` | Supported exactly |
| The PREGO concept has 914 associated taxa and two evidence channels, `annotated_genomes_isolates` and `environmental_samples`. | `data/raw/prego_habitats.tsv:83` | Supported exactly; the record uses `taxon_count` as `assertion_count` because PREGO assertion units are distinct taxa |
| `activated sludges` is a PREGO synonym of `activated sludge`. | `data/raw/prego_habitats.tsv:83` | Supported exactly by the pipe-delimited `prego_synonyms` cell |
| `activated sludge` is a subclass of `sludge`. | `data/raw/ontology_subclass_edges.tsv:5293`; `data/raw/ontology_terms.tsv:7189`, `7191` | Supported exactly |
| The 25 generated taxon associations are PREGO's first 25 ranked taxa for `ENVO:00002046`. | `data/raw/prego_habitat_taxa.tsv:5895-5919` | Supported exactly in rank, taxon id, taxon label, score, and source channel |

The generated taxon entries are PREGO-reported associations, not curator claims
that those taxa typify activated sludge. The entries correctly omit
`is_characteristic` and `reference`, and the record carries `candidate_pool:
914` so each rank is read against the full source pool.

The record has no definition, xrefs, environmental parameters, record-level
evidence, causal graphs, discussion links, datasets, or quality flags. Those
absences match the inspected maintained inputs: the ENVO slice has no definition
for `ENVO:00002046`, and HabitatMech has no activated-sludge-specific causal
overlay or term request.

Unsupported or over-scoped claims: None found.

## Completeness

The PREGO source attestation is complete for `data/raw/prego_habitats.tsv:83`:
the generated record carries the ENVO source id, source label, 914-taxon count,
`TAXON` assertion unit, maximum score `4.0`, and both source evidence channels.
It deliberately does not serialize PREGO's `direct_assertion_count: 932`
because `SourceAttestation.assertion_count` is distinct taxa for PREGO.

The synonym list is complete for the PREGO row: the only source label that
differs from the record label, `activated sludges`, appears as a
`RELATED_SYNONYM`.

The ranked taxon list is complete for HabitatMech's inline representation:
PREGO supplies 914 candidate taxa and `data/raw/prego_habitat_taxa.tsv:5895-5919`
are exactly the top 25 emitted into the generated record.

No BacDive or GOLD attestation is missing from this exact record. An
ignored/hidden-inclusive exact search of the BacDive committed inputs for
`Activated-sludge`, `activated sludge`, and `ENVO:00002046` found only a lexical
candidate row in `data/raw/isolation_source_groundings.tsv` and no committed
`data/raw/bacdive_isolation_sources.tsv` or `data/raw/bacdive_source_taxa.tsv`
source row. GOLD references to `activated sludge` in the committed raw inventory
are either MIxS medium triad context for GOLD paths or narrower source paths
that already generate their own minted child records.

Ignored/hidden-inclusive exact searches covered the target id, the record stem,
the PREGO label and plural synonym, GOLD's `Activated sludge` and `Activated
Sludge` spellings, the ENVO parent `ENVO:00002044`, the PREGO source rows, the
`PATHS.tsv` lock row, and maintained `curation/` and `history/` inputs,
excluding generated `build`, `data/text_map`, and `pages` trees for broad
content searches. They found the cited PREGO, ENVO, path-lock,
BacDive-lexical-candidate, GOLD-path, GOLD-triad, generated child-record, and
broader `sludge` causal-graph rows, and no maintained target row that should
already have changed this record.

## Findings

None found.

No blocker findings.

No major findings.

No minor findings.

## Recommended Edits

None required.

If a future curator wants to promote this seeded PREGO record to reviewed
status, add an item-level `REVIEW` row for `ENVO:00002046` in
`curation/decisions.tsv` and rerun a canary for `ENVO:00002046`. That should be
a status-only change: keep `ENVO:00002046` as the exact identifier, keep
`ENVO:00002044` as the broader ontology parent, and keep the PREGO taxon
associations non-characteristic unless independent evidence supports stronger
taxon claims.

## Follow-up Checks

None required beyond the validators already run for this report.

For any future status-only review row, run:

- `just seed`
- `just seed-canary ENVO:00002046`
- `just validate data/habitats/other/activated_sludge.yaml`
- `just validate-strict data/habitats/other/activated_sludge.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000`
- `just report`
- `git diff --check`

## Additional Notes

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*-activated_sludge.md' -print` found no pre-existing exact review report for this record before this file was written, and `find` included ignored files under the searched directory.
- Exact ignored/hidden-inclusive content searches for `ENVO:00002046`, `activated_sludge`, `activated sludge`, `activated sludges`, `Activated sludge`, `Activated Sludge`, `ENVO:00002044`, `^identifier: ENVO:00002046$`, and BacDive's `Activated-sludge` spelling found the cited raw, path-lock, curation, and generated-record rows, and no target-specific curated input rows.
