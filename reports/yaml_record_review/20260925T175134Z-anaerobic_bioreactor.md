# YAML Record Review

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/engineered/anaerobic_bioreactor.yaml
- Started UTC: 2026-09-25T17:49:22Z
- Finished UTC: 2026-09-25T17:51:34Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00002124` |
| Label | `anaerobic bioreactor` |
| Category | `ENGINEERED` |
| Grounding status | `EXACT` |
| Mapping status | `REVIEWED` |
| Sources | `GOLD`, `PREGO` |
| Maintained owner | Generated from `data/raw/` plus reviewed source decisions in `curation/decisions.tsv`; future fixes belong in the contributing item-level `curation/decisions.tsv` rows, not in generated YAML. |

The target is the generated ENVO-grounded record for `anaerobic bioreactor`,
attested by five reviewed GOLD source concepts and one reviewed PREGO source
concept. The direct GOLD `Engineered > Bioreactor > Anaerobic` concept and the
PREGO `ENVO:00002124` association agree with the ontology identity. Four more
specific GOLD concepts under `Semi-continuous`, `SSF (Solid state
fermentation)`, `MBR (Membrane bioreactor)`, and `DHS reactor` have also been
exact-grounded into this generic ENVO record, which drops their reactor-specific
context.

| Source concept | Source row | Decision |
| --- | --- | --- |
| `habitatmech:GOLD.ec772ab975` / `Engineered > Bioreactor > Anaerobic` | `data/raw/gold_ecosystem_paths.tsv:163`, first GOLD node `gold.ecosystem:4440` | `GROUND ENVO:00002124` at `curation/decisions.tsv:1304` |
| `habitatmech:GOLD.15529e3307` / `Engineered > Bioreactor > Semi-continuous > Anaerobic` | `data/raw/gold_ecosystem_paths.tsv:1216`, first GOLD node `gold.ecosystem:7768` | `GROUND ENVO:00002124` at `curation/decisions.tsv:216` |
| `habitatmech:GOLD.b0d35001b6` / `Engineered > Bioreactor > SSF (Solid state fermentation) > Anaerobic` | `data/raw/gold_ecosystem_paths.tsv:1213`, first GOLD node `gold.ecosystem:8151` | `GROUND ENVO:00002124` at `curation/decisions.tsv:999` |
| `habitatmech:GOLD.9dac2d3db9` / `Engineered > Bioreactor > MBR (Membrane bioreactor) > Anaerobic` | `data/raw/gold_ecosystem_paths.tsv:1191`, first GOLD node `gold.ecosystem:8271` | `GROUND ENVO:00002124` at `curation/decisions.tsv:912` |
| `habitatmech:GOLD.7b1df1e18d` / `Engineered > Bioreactor > DHS reactor > Anaerobic` | `data/raw/gold_ecosystem_paths.tsv:1177`, first GOLD node `gold.ecosystem:8426` | `GROUND ENVO:00002124` at `curation/decisions.tsv:728` |
| `habitatmech:PREGO.3f92a7cfe1` / `ENVO:00002124` | `data/habitats/engineered/anaerobic_bioreactor.yaml` PREGO source attestation | `REVIEW` at `curation/decisions.tsv:1427` |

`data/habitats/PATHS.tsv:645` locks `ENVO:00002124` to the
`anaerobic_bioreactor` slug, and `data/raw/ontology_terms.tsv:7220` supplies
the ontology label and definition used in the generated record.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/habitats/engineered/anaerobic_bioreactor.yaml` | Pass: LinkML reported `No issues found`. |
| `just validate-strict data/habitats/engineered/anaerobic_bioreactor.yaml` | Pass: scanned 1 file with 0 files containing `ERROR` and 0 total `ERROR` rows. |
| `just validate-causal-all` | Pass: validated 32 causal-graph curation files with 32 graphs. |
| `just term-requests-check` | Pass: the term-request table is current with 109 terms. |
| `just validate-history` | Pass: 77 history records were valid against `src/habitatmech/schema/history.yaml`. |
| `just verify-corpus --max-diffs 1` | Pass: expected 3,206 records, found 3,206 on disk, and the corpus reproduces exactly from `data/raw/`. |
| `just worklist --limit 2000 --status all --out /tmp/habitatmech-anaerobic-bioreactor-worklist.tsv` | Pass: reported 953 ungrounded records, 1,810 decisions on file, and wrote 953 rows to `/tmp/habitatmech-anaerobic-bioreactor-worklist.tsv`. |
| `just report` | Pass: completed the corpus report for 3,206 records. |
| Reference validator | Not applicable: the record has PREGO source-owned characteristic taxa but no record-level `evidence`, `causal_graphs`, `discussions`, or `datasets` with citation-bearing `EvidenceItem` references. |
| `git diff --check` | Pass. |

## Identity and Grounding

The ENVO identity is supported for the direct GOLD `Engineered > Bioreactor >
Anaerobic` source concept. The vendored ontology defines `ENVO:00002124`
`anaerobic bioreactor` as a bioreactor whose contained material is not
oxygenated, and `data/raw/ontology_subclass_edges.tsv:5324` places it directly
under `ENVO:00002123` `bioreactor`. GOLD path row 163 composes the generic
`Bioreactor` parent with the oxygenation qualifier `Anaerobic`, and the row
carries 131 organism assertions from three duplicate GOLD ecosystem node IDs.

The exact grounding is too broad for the four deeper GOLD paths:

| Source concept | Raw row | Review |
| --- | --- | --- |
| `Engineered > Bioreactor > Semi-continuous > Anaerobic` | `data/raw/gold_ecosystem_paths.tsv:1216` has leaf `Anaerobic` under the `Semi-continuous` parent and two GOLD node IDs, `gold.ecosystem:7768\|gold.ecosystem:8425`. | This denotes an anaerobic semi-continuous bioreactor context, not all anaerobic bioreactors. It is narrower than `ENVO:00002124`. |
| `Engineered > Bioreactor > SSF (Solid state fermentation) > Anaerobic` | `data/raw/gold_ecosystem_paths.tsv:1213` has leaf `Anaerobic` under the SSF parent and two GOLD node IDs, `gold.ecosystem:8151\|gold.ecosystem:8152`. | This denotes an anaerobic solid-state-fermentation context, not all anaerobic bioreactors. It is narrower than `ENVO:00002124`. |
| `Engineered > Bioreactor > MBR (Membrane bioreactor) > Anaerobic` | `data/raw/gold_ecosystem_paths.tsv:1191` has leaf `Anaerobic` under the membrane-bioreactor parent and two GOLD node IDs, `gold.ecosystem:8271\|gold.ecosystem:8272`. | This denotes an anaerobic membrane bioreactor context, not all anaerobic bioreactors. It is narrower than `ENVO:00002124`. |
| `Engineered > Bioreactor > DHS reactor > Anaerobic` | `data/raw/gold_ecosystem_paths.tsv:1177` has leaf `Anaerobic` under the DHS parent and two GOLD node IDs, `gold.ecosystem:8426\|gold.ecosystem:8427`. | This denotes an anaerobic DHS reactor context, not all anaerobic bioreactors. It is narrower than `ENVO:00002124`. |

The generated `mapping_status: REVIEWED` is mechanically expected because every
contributing GOLD concept and the PREGO concept have item-level decisions, but
four of the five GOLD decisions use `GROUND` where a source-specific minted
identity plus `ENVO:00002124` as a parent would preserve the full GOLD meaning.

## Evidence

| Claim | Nearest support | Review |
| --- | --- | --- |
| `ENVO:00002124` is a subtype of `ENVO:00002123` `bioreactor`. | `data/raw/ontology_subclass_edges.tsv:5324`; `data/raw/ontology_terms.tsv:7220` | Supported. |
| The direct GOLD source concept `Engineered > Bioreactor > Anaerobic` is exact to `ENVO:00002124`. | `data/raw/gold_ecosystem_paths.tsv:163`; `curation/decisions.tsv:1304` | Supported. The GOLD leaf qualifies the generic `Bioreactor` path node. |
| The PREGO `ENVO:00002124` source concept is an association to `ENVO:00002124`. | `curation/decisions.tsv:1427`; generated PREGO source attestation in the target YAML | Supported. The PREGO label repeats the ENVO label, and the source-owned taxon associations are represented as PREGO-derived associations rather than curator-authored biological claims. |
| The generic GOLD source should carry `assertion_count: 131`. | `data/raw/gold_ecosystem_paths.tsv:163`; `src/habitatmech/seed.py` | Supported. The raw path has `organism_count=131`, and the seeder emits GOLD organism counts as source-attestation assertions. |
| The generic GOLD source should carry the duplicate-node note. | `data/raw/gold_ecosystem_paths.tsv:163`; `src/habitatmech/seed.py` | Supported. The raw row collapses three GOLD ecosystem node IDs; the seeder emits the first and notes the shared path. |
| `Engineered > Bioreactor > Semi-continuous > Anaerobic` is an exact source attestation for `ENVO:00002124`. | `curation/decisions.tsv:216` | Unsupported. The item-level note says GOLD qualifies the `Bioreactor` node, but the raw path qualifies the `Semi-continuous` node. |
| `Engineered > Bioreactor > SSF (Solid state fermentation) > Anaerobic` is an exact source attestation for `ENVO:00002124`. | `curation/decisions.tsv:999` | Unsupported. The item-level note says GOLD qualifies the `Bioreactor` node, but the raw path qualifies the `SSF (Solid state fermentation)` node. |
| `Engineered > Bioreactor > MBR (Membrane bioreactor) > Anaerobic` is an exact source attestation for `ENVO:00002124`. | `curation/decisions.tsv:912` | Unsupported. The item-level note says GOLD qualifies the `Bioreactor` node, but the raw path qualifies the `MBR (Membrane bioreactor)` node. |
| `Engineered > Bioreactor > DHS reactor > Anaerobic` is an exact source attestation for `ENVO:00002124`. | `curation/decisions.tsv:728` | Unsupported. The item-level note says GOLD qualifies the `Bioreactor` node, but the raw path qualifies the `DHS reactor` node. |
| The generic `ENVO:00002124` record is a child of `habitatmech:GOLD.32c2a98ae8` `Semi-continuous`, `habitatmech:GOLD.3af6ca6cc3` `SSF (Solid state fermentation)`, `ENVO:03600010` `membrane bioreactor`, and `habitatmech:GOLD.24cf427e7d` `DHS reactor`. | Generated by merging the four narrower source concepts into the generic ENVO record and retaining their immediate GOLD parents. | Unsupported. Semi-continuous, SSF, membrane, and DHS anaerobic bioreactors are narrower contexts within anaerobic bioreactors, not broader classes of all anaerobic bioreactors. |

## Completeness

No maintained definition, causal overlay, target-specific research report, or
history entry exists for `ENVO:00002124`, `anaerobic_bioreactor`, the five
contributing GOLD source concepts, or `habitatmech:PREGO.3f92a7cfe1`. Exact
gitignore-independent searches covered `curation`, `history`, `research`,
`reports/yaml_record_review`, `data/raw`, `data/habitats/PATHS.tsv`, and the
relevant generated engineered records while excluding broad generated `build`,
`data/text_map`, and `pages` outputs. Ignored files were included in those
absence checks.

`find reports/yaml_record_review -maxdepth 1 -type f -name
'*-anaerobic_bioreactor.md' -print` included ignored files and found no
pre-existing exact review report for this generated record before this file was
written.

The four over-merged deeper GOLD paths all carry zero organism, study,
biosample, and total assertions, so the generated source attestations correctly
omit `assertion_count` and `assertion_unit` for them. The unsupported claims are
the exact source identities and retained strict `parent_habitats`, not missing
direct GOLD count fields.

The generic record carries the top 25 PREGO taxon associations out of a source
candidate pool of 81, each with score `4.0`. Those `characteristic_taxa` are
source-owned PREGO associations, and this review did not find a maintained
curation row that endorses any one taxon as characteristic of all anaerobic
bioreactors.

## Findings

- **major**: Four narrower GOLD source concepts are exact-grounded into the
  generic `ENVO:00002124` `anaerobic bioreactor` record.
  `Engineered > Bioreactor > Semi-continuous > Anaerobic`,
  `Engineered > Bioreactor > SSF (Solid state fermentation) > Anaerobic`,
  `Engineered > Bioreactor > MBR (Membrane bioreactor) > Anaerobic`, and
  `Engineered > Bioreactor > DHS reactor > Anaerobic` are anaerobic variants
  of narrower reactor contexts; none is exact to all anaerobic bioreactors.
  The over-merges also make the generic ENVO record a generated child of
  `Semi-continuous`, `SSF (Solid state fermentation)`, `membrane bioreactor`,
  and `DHS reactor`, which reverses the true broader/narrower direction.

  **Owner**: Update the `habitatmech:GOLD.15529e3307`,
  `habitatmech:GOLD.b0d35001b6`, `habitatmech:GOLD.9dac2d3db9`, and
  `habitatmech:GOLD.7b1df1e18d` rows in `curation/decisions.tsv`; if any
  concept stays minted, add `curation/term_requests.tsv` definitions with true
  genera and rerun the seed.

No blockers found.

No minor findings.

## Recommended Edits

1. Replace the `GROUND ENVO:00002124` row for
   `habitatmech:GOLD.15529e3307` with a decision that preserves the
   semi-continuous anaerobic concept, most likely `GROUND_AS_PARENT
   ENVO:00002124 anaerobic bioreactor NARROW` plus an authored
   `curation/term_requests.tsv` definition under
   `habitatmech:GOLD.15529e3307`.

2. Replace the `GROUND ENVO:00002124` row for
   `habitatmech:GOLD.b0d35001b6` with a decision that preserves the
   SSF-specific anaerobic concept, most likely `GROUND_AS_PARENT
   ENVO:00002124 anaerobic bioreactor NARROW` plus an authored
   `curation/term_requests.tsv` definition under
   `habitatmech:GOLD.b0d35001b6`.

3. Replace the `GROUND ENVO:00002124` row for
   `habitatmech:GOLD.9dac2d3db9` with a decision that preserves the
   membrane-bioreactor-specific anaerobic concept, most likely
   `GROUND_AS_PARENT ENVO:00002124 anaerobic bioreactor NARROW` plus an
   authored `curation/term_requests.tsv` definition under
   `habitatmech:GOLD.9dac2d3db9`.

4. Replace the `GROUND ENVO:00002124` row for
   `habitatmech:GOLD.7b1df1e18d` with a decision that preserves the
   DHS-specific anaerobic concept, most likely `GROUND_AS_PARENT
   ENVO:00002124 anaerobic bioreactor NARROW` plus an authored
   `curation/term_requests.tsv` definition under
   `habitatmech:GOLD.7b1df1e18d`.

5. Keep the `habitatmech:GOLD.ec772ab975` exact grounding to
   `ENVO:00002124` and the `habitatmech:PREGO.3f92a7cfe1` review unless a
   future curator finds evidence that either source is narrower than the ENVO
   term.

6. Regenerate the corpus rather than editing
   `data/habitats/engineered/anaerobic_bioreactor.yaml` directly.

## Follow-up Checks

After curation, rerun:

- `just seed`
- `just seed-canary ENVO:00002124`
- `just seed-canary habitatmech:GOLD.15529e3307`
- `just seed-canary habitatmech:GOLD.b0d35001b6`
- `just seed-canary habitatmech:GOLD.9dac2d3db9`
- `just seed-canary habitatmech:GOLD.7b1df1e18d`
- Inspect `data/habitats/engineered/anaerobic_bioreactor.yaml` and confirm it
  keeps `ENVO:00002123` but no longer lists
  `habitatmech:GOLD.32c2a98ae8`, `habitatmech:GOLD.3af6ca6cc3`,
  `ENVO:03600010`, or `habitatmech:GOLD.24cf427e7d` under
  `parent_habitats`.
- Inspect the regenerated semi-continuous-, SSF-, MBR-, and DHS-specific
  anaerobic records and confirm `ENVO:00002124` is retained as their broader
  parent, not their exact identity.
- `just seed-apply --force`
- `just validate data/habitats/engineered/anaerobic_bioreactor.yaml`
- `just validate-strict data/habitats/engineered/anaerobic_bioreactor.yaml`
- `just validate-causal-all`
- `just term-requests-check`
- `just validate-history`
- `just verify-corpus --max-diffs 1`
- `just worklist --limit 2000 --status all --out /tmp/habitatmech-anaerobic-bioreactor-worklist.tsv`
- `just report`
- `git diff --check`

## Additional Notes

- The unsupported parents are not caused by a hand edit: `just verify-corpus
  --max-diffs 1` reproduced all 3,206 generated records exactly from
  maintained inputs.
- The source-owned PREGO characteristic-taxon list has 81 source associations
  and is not a curated assertion that every listed taxon is biologically
  characteristic of every anaerobic-bioreactor subtype.
- This is the anaerobic counterpart to the same exact-grounding error observed
  for `data/habitats/engineered/aerobic_bioreactor.yaml`, with two additional
  narrower reactor contexts: `Semi-continuous` and `MBR (Membrane bioreactor)`.
