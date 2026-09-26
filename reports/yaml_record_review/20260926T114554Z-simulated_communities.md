# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/other/simulated_communities.yaml
- Started UTC: 2026-09-26T11:45:55Z
- Finished UTC: 2026-09-26T11:46:00Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Identifier | `habitatmech:BACDIVE.5fa4710934` |
| Label | `Simulated-communities` |
| Class | `HabitatRecord` |
| Category | `OTHER` |
| Generated path | `data/habitats/other/simulated_communities.yaml` |
| Maintained path lock | `data/habitats/PATHS.tsv:1204` maps `habitatmech:BACDIVE.5fa4710934` to `simulated_communities` |
| Source concept | BACDIVE `bacdive.isolation_source:simulated-communities` |
| Source label | `Simulated-communities` |
| Grounding | `UNGROUNDED` |
| Mapping | `SEEDED` |

The reviewed file is generated from the BacDive source inventory, the local
copy of KG-Microbe's BacDive isolation-source grounding table, and one
class-level curation decision. It should not be patched directly.

## Validation

| Command | Result |
|---|---|
| `just worklist --limit 0 --status all --out /tmp/habitatmech-worklist.tsv` | Passed; wrote 953 rows. The target appeared as row 233 with four BacDive assertions and no candidate ontology term column. |
| `just validate data/habitats/other/simulated_communities.yaml` | Passed with `No issues found`. |
| `just validate-strict data/habitats/other/simulated_communities.yaml` | Passed; one file scanned, zero files with `ERROR`, zero total error rows. |
| `just validate-causal-all` | Passed; 32 causal-graph curation files with 32 graphs validated. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Passed; 3206 expected records, 3206 found, 0 missing, 0 extra, 0 differing. |
| `just report` | Passed. |
| `git diff --check` | Passed before this report was written. |

## Identity and Grounding

The generated identifier, BacDive source identity, strain count, and taxon list
agree with the raw BacDive inventory:

| Claim | Evidence | Assessment |
|---|---|---|
| The target is the BacDive `Simulated-communities` isolation source. | `data/raw/bacdive_isolation_sources.tsv:142` records `bacdive.isolation_source:simulated-communities`, label `Simulated-communities`, slug `simulated-communities`, four strains, and four taxa. | Supported exactly. |
| The KG-Microbe BacDive grounding row exists but does not carry an ontology target. | `data/raw/isolation_source_groundings.tsv:280` records `Simulated-communities` with normalized label `simulated communities`, blank `object_id`, blank `object_label`, and source dataset `bacdive`. | Supported exactly. `src/habitatmech/seed.py` treats this shape as `bacdive_declined_upstream`. |
| The `source_attestations` block preserves the raw source ID, source label, assertion count, and unit. | The generated YAML has `source: BACDIVE`, `source_id: bacdive.isolation_source:simulated-communities`, `source_label: Simulated-communities`, `assertion_count: 4`, and `assertion_unit: STRAIN`. | Supported exactly. |
| The four characteristic taxa preserve the BacDive isolation-source taxa ranking. | `data/raw/bacdive_source_taxa.tsv:2530-2533` lists `Haematobacter massiliensis`, `Roseicyclus marinus`, `Bifidobacterium animalis subsp. lactis`, and `Pusillimonas noertemannii`, each with one strain at ranks 1 through 4. | Supported exactly. |
| The record is still owned by a class-level sweep decision. | `curation/decisions.tsv:38` has `CONFIRM_UNGROUNDED` for `habitatmech:BACDIVE.5fa4710934` with `review_depth` `CLASS`. Its note says habitat status was not assessed. | Reproducible but incomplete. A class-level sweep is not enough to decide whether the label names a real engineered microbial habitat or an in-silico/model artifact. |

The BacDive label has no direct ontology candidate in the generated worklist.
It does have local modeled-community near-siblings in GOLD:

| Source path | Record | Local assessment |
|---|---|---|
| `Engineered > Modeled` | `habitatmech:GOLD.5df162af13` | The generated `Modeled` parent is also only class-depth reviewed. `curation/samples/class_swept_unscreened-20260814.tsv` sampled this row as a wrong class-sweep survivor because GOLD's modeled bin is in-silico rather than a place an organism was isolated from. |
| `Engineered > Modeled > Simulated communities (microbial mixture)` | `habitatmech:GOLD.0e7aeb7635` | The closest GOLD sibling to a real microbial mock community; still class-depth reviewed and narrower than BacDive's unqualified label. |
| `Engineered > Modeled > Simulated communities (DNA mixture)` | `habitatmech:GOLD.e96d7e84d0` | A modeled-community sibling that names a DNA mixture rather than a living community habitat. |
| `Engineered > Modeled > Simulated communities (contig mixture)` | `habitatmech:GOLD.4f2d583075` | A modeled-community sibling that names a sequence-assembly artifact rather than a living community habitat. |
| `Engineered > Modeled > Simulated communities (sequence read mixture)` | `habitatmech:GOLD.9203c1c268` | A modeled-community sibling that names a sequence-read mixture rather than a living community habitat. |

These GOLD records confirm that HabitatMech already has nearby source concepts,
but they do not prove the BacDive source's identity. An item review still has
to decide whether BacDive's flat label denotes a living synthetic microbial
mixture, a broader in-silico/modeling bin, or a non-habitat reference material.

## Evidence

| Record claim | Nearest source | Assessment |
|---|---|---|
| `source: BACDIVE`, `source_id: bacdive.isolation_source:simulated-communities`, and `source_label: Simulated-communities` | `data/raw/bacdive_isolation_sources.tsv:142` | Supported exactly. |
| `assertion_count: 4` and `assertion_unit: STRAIN` | `data/raw/bacdive_isolation_sources.tsv:142` | Supported exactly. This is a BacDive strain count and must not be combined with GOLD organism or biosample counts. |
| Note saying KG-Microbe has a blank isolation-source grounding for this source | `data/raw/isolation_source_groundings.tsv:280`; `src/habitatmech/seed.py` emits the note for `bacdive_declined_upstream` rows. | Supported exactly as generated behavior. The upstream blank should be item-reviewed rather than bypassed with a generated-YAML edit. |
| `NCBITaxon:195105` through `NCBITaxon:305977` characteristic taxa | `data/raw/bacdive_source_taxa.tsv:2530-2533` | Supported exactly. No rank, label, count, or candidate-pool mismatch was found. |
| Absence of a curated definition, source-derived parents, environmental parameters, evidence objects, and causal graphs | Exact hidden/ignored-inclusive searches for `habitatmech:BACDIVE.5fa4710934`, `bacdive.isolation_source:simulated-communities`, `Simulated-communities`, and `simulated_communities` across `data/raw/`, `curation/`, `history/`, `research/habitats/`, `reports/yaml_record_review/`, `data/habitats/`, and `pages/habitats/` found no target-specific maintained overlay, history row, research report, or prior review. | Supported. The current record is a generated BacDive leaf with no committed item-level curation. |

## Completeness

The generated record completely preserves the current BacDive source aggregate,
blank KG-Microbe grounding, class-level decision, and BacDive characteristic
taxa rows. It correctly avoids unsupported definitions, parents, environmental
parameters, evidence objects, and causal graph claims.

It is incomplete as a curation decision. The class-level sweep established only
that no vendored ontology term matched the label by any lexical route; it did
not inspect the BacDive source or decide whether the source is a place,
material, engineered community, in-silico bin, or sequence/mock-community
artifact.

The GOLD `Engineered > Modeled` branch makes that missing item review
consequential. GOLD has related simulated-community leaves for microbial, DNA,
contig, and sequence-read mixtures, and its `Modeled` parent was already
sampled as in-silico and therefore not a habitat. BacDive's unqualified
`Simulated-communities` source needs the same kind of per-item reading before
HabitatMech can safely keep it as a habitat, merge it with a real engineered
microbial-mixture source, set an `ENGINEERED` category, or mark it
`NOT_APPLICABLE`.

## Findings

| ID | Severity | Finding | Maintained owner |
|---|---|---|---|
| HM-SIMULATED-COMMUNITIES-001 | Major | `Simulated-communities` is still backed only by a blank BacDive grounding row and a `CLASS`-depth `CONFIRM_UNGROUNDED` decision. The generated BacDive strain/taxon content is reproducible, but the row has not been item-reviewed and its label is ambiguous between a living synthetic community habitat, GOLD-like modeled mixtures, and non-habitat sequence/mock-community artifacts. | `curation/decisions.tsv`; if the KG-Microbe BacDive mapping should resolve to a term or upstream synonym after item review, `data/raw/isolation_source_groundings.tsv` |

## Recommended Edits

1. Item-review `bacdive.isolation_source:simulated-communities` against the
   four BacDive strain sources and the local GOLD `Engineered > Modeled >
   Simulated communities (...)` family.
2. If the BacDive source is not a microbial habitat, replace the class-level
   `CONFIRM_UNGROUNDED` row in `curation/decisions.tsv` with an item-level
   `NOT_APPLICABLE` decision that records why the source names an in-silico
   artifact or reference mixture rather than an isolation site.
3. If the BacDive source is a living engineered mock or synthetic community,
   keep or merge it through an item-level decision, choose an `ENGINEERED`
   category deliberately, and add any required minted definition in
   `curation/term_requests.tsv`.
4. Regenerate from the maintained inputs and confirm the BacDive attestation,
   grounding status, mapping status, category, and generated history reflect
   the item-level decision.

Do not hand-edit `data/habitats/other/simulated_communities.yaml` or generated
HTML pages.

## Follow-up Checks

After item-level curation, rerun:

- `just seed`
- `just seed-canary habitatmech:BACDIVE.5fa4710934`
- inspect `data/habitats/other/simulated_communities.yaml` or the merged target
  that absorbs `bacdive.isolation_source:simulated-communities`
- `just validate-strict` on the regenerated target
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just report`

If the item review redirects the BacDive source to an existing GOLD
simulated-community record, also check `data/habitats/PATHS.tsv`, retired page
redirects, and generated pages before committing the curation change.

## Additional Notes

None.
