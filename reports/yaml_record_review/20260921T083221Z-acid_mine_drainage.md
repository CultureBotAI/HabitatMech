# YAML Record Review: acid mine drainage

- Repository: CultureBotAI/HabitatMech
- Record: data/habitats/aquatic/acid_mine_drainage.yaml
- Started UTC: 2026-09-21T08:30:12Z
- Finished UTC: 2026-09-21T08:32:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/habitats/aquatic/acid_mine_drainage.yaml` |
| Class | `HabitatRecord` |
| Identifier | `ENVO:00001997` |
| Label | `acid mine drainage` |
| Category | `AQUATIC` |
| Grounding status | `EXACT` |
| Mapping status | `REVIEWED` |
| Maintained/generated status | Generated from `data/raw/` inventories and curator inputs; `just verify-corpus --max-diffs 1` reproduces it byte-for-byte. |

The record is a reviewed exact merge of three upstream concepts:

- GOLD `Environmental > Aquatic > Freshwater > Groundwater > Acid Mine Drainage`
  contributes `gold.ecosystem:4164`, 18 organism assertions, and source concept
  `habitatmech:GOLD.d727388954`.
- GOLD `Engineered > Wastewater > Industrial wastewater > Acid mine drainage`
  contributes `gold.ecosystem:6075`, 16 organism assertions across two GOLD
  ecosystem node IDs, and source concept `habitatmech:GOLD.4d88cc502b`.
- PREGO contributes `ENVO:00001997`, three directly asserted taxa, source
  synonyms, and source concept `habitatmech:PREGO.03c5325bcc`.

## Validation

| Check | Result |
|---|---|
| `just validate data/habitats/aquatic/acid_mine_drainage.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/habitats/aquatic/acid_mine_drainage.yaml --quiet` | Passed; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| `just term-requests-check` | Passed; the term-request table is current with 109 terms. |
| `just verify-corpus --max-diffs 1` | Passed; 3,206 expected records, 3,206 records on disk, 0 missing, 0 extra, 0 differing. |
| `just validate-history` | Passed; 77 history records are valid against `src/habitatmech/schema/history.yaml`. |
| Reference validator | Not checked: this record has no DOI/PMID/URL `EvidenceItem`, no causal-edge evidence, and no dedicated `research/habitats/` report for `ENVO:00001997`. |

## Identity and Grounding

| Claim | Evidence | Assessment |
|---|---|---|
| `ENVO:00001997` is the exact ontology identity for the merged record. | `data/raw/ontology_terms.tsv` lists `ENVO:00001997` with canonical label `acid mine drainage`, definition `A mine drainage with an acidic pH.`, exact synonym `acid rock drainage`, and an active ENVO status. | Supported exactly. |
| ENVO places acid mine drainage under mine drainage. | `data/raw/ontology_subclass_edges.tsv` has `ENVO:00001997 rdfs:subClassOf ENVO:00001996`; `data/raw/ontology_terms.tsv` verifies `ENVO:00001996` as `mine drainage`. | Supported exactly. |
| The environmental GOLD attestation is an acid-mine-drainage source concept. | `data/raw/gold_ecosystem_paths.tsv` has canonical path `Environmental > Aquatic > Freshwater > Groundwater > Acid Mine Drainage`, leaf `Acid Mine Drainage`, depth `5`, `gold_node_count=1`, `organism_count=18`, and node ID `gold.ecosystem:4164`. | Supported exactly for the source path and assertion count. |
| The engineered GOLD attestation is an acid-mine-drainage source concept. | `data/raw/gold_ecosystem_paths.tsv` has canonical path `Engineered > Wastewater > Industrial wastewater > Acid mine drainage`, leaf `Acid mine drainage`, depth `4`, `gold_node_count=2`, `organism_count=16`, and node IDs `gold.ecosystem:6075\|gold.ecosystem:8141`. | Supported exactly for the source path and collapsed-node note. |
| PREGO attests the same ENVO habitat. | `data/raw/prego_habitats.tsv` row `ENVO:00001997` lists ontology `ENVO`, `taxon_count=3`, `direct_assertion_count=3`, `max_prego_score=4`, evidence channel `annotated_genomes_isolates`, and source synonyms `acid mine drainage\|acid mine drainages\|acid rock drainage\|acid rock drainages`. | Supported exactly. |
| All three source concepts have item-level review. | `curation/decisions.tsv` has `ITEM` rows for `habitatmech:GOLD.4d88cc502b`, `habitatmech:PREGO.03c5325bcc`, and `habitatmech:GOLD.d727388954`; the first two `REVIEW` the seeder's exact merge and the last explicitly `GROUND`s the shallower-guarded GOLD branch to `ENVO:00001997`. | Supported exactly; `mapping_status: REVIEWED` follows from all contributing sources having item-level decisions. |
| `ENVO:01000964` `industrial wastewater` and `habitatmech:GOLD.7f8e268653` `Groundwater` are broader habitats for the merged ENVO record. | They are generated mechanically from the two GOLD source path parents: `Engineered > Wastewater > Industrial wastewater` and `Environmental > Aquatic > Freshwater > Groundwater`. `src/habitatmech/seed.py` links every GOLD child to the resolved identifier of its parent path after identity merging. | Needs curation. These are context parents for the two GOLD branches, not proven universal parents of generic ENVO acid mine drainage. |

## Evidence

The generated record has no record-level `evidence` entries and no
`causal_graphs`.

| Claim | Evidence | Assessment |
|---|---|---|
| `acid rock drainage` is an exact ENVO synonym. | `data/raw/ontology_terms.tsv` lists `acid rock drainage` in the synonym field for active term `ENVO:00001997`. | Supported exactly. |
| PREGO contributes related source synonyms. | `data/raw/prego_habitats.tsv` lists `acid mine drainage`, `acid mine drainages`, `acid rock drainage`, and `acid rock drainages` for `ENVO:00001997`. | Supported exactly. |
| The PREGO taxon rows are source-observed associations, not curator claims that the taxa typify acid mine drainage. | `data/raw/prego_habitat_taxa.tsv` ranks `NCBITaxon:768535` `Acidipila rosea`, `NCBITaxon:1121877` `Ferrimicrobium acidiphilum DSM 19497`, and `NCBITaxon:349163` `Acidiphilium cryptum JF-5` for `ENVO:00001997` with scores `4`, `3`, and `3`; the generated YAML omits `is_characteristic` and `reference`, matching the schema description that seeded PREGO entries are observational. | Supported exactly. |
| The August 20 GOLD merge note uses MIxS triad evidence correctly for the environmental GOLD path. | `data/raw/gold_path_triads.tsv` records 60 samples across 14 studies for `Environmental > Aquatic > Freshwater > Groundwater > Acid Mine Drainage`, all with `local = ENVO:00001997 acid mine drainage`, matching the curation note's quoted study count and CURIE. | Supported exactly for the local-scale triad claim. |

## Completeness

- The record is complete enough for a reviewed exact ENVO/PREGO/GOLD
  harmonization of the acid-mine-drainage identity.
- The only consequential gap found is in the inherited hierarchy: the record
  currently publishes two branch-specific GOLD path parents as universal
  `parent_habitats` of `ENVO:00001997`.
- Ignored/hidden-inclusive exact searches across `data/habitats`,
  `data/raw`, `curation`, `research/habitats`,
  `reports/habitat_research_manifest.tsv`, and
  `reports/yaml_record_review` for `ENVO:00001997`,
  `gold.ecosystem:4164`, `gold.ecosystem:6075`,
  `habitatmech:GOLD.4d88cc502b`, `habitatmech:GOLD.d727388954`,
  `habitatmech:PREGO.03c5325bcc`, and both exact GOLD paths found the target
  record, source rows, ontology rows, and decision rows above.
- Ignored/hidden-inclusive exact searches under `curation/causal_graphs`,
  `research/habitats`, and `reports/yaml_record_review` for
  `Acid Mine Drainage`, `Acid mine drainage`, and `acid_mine_drainage`, plus
  `find` checks for `*acid*` and `*mine*`, found no curated causal overlay, no
  dedicated research report, and no prior acid-mine-drainage YAML review
  report.

## Findings

| ID | Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|---|
| `HM-ACID-MINE-DRAINAGE-001` | Major | The exact ENVO record inherits two false or unproven source-path parents after merging branch-specific GOLD concepts. `parent_habitats` asserts that generic `ENVO:00001997` acid mine drainage is a kind of both `ENVO:01000964` industrial wastewater and `habitatmech:GOLD.7f8e268653` Groundwater. Those edges come from the engineered and environmental GOLD filing paths, while the record identity is the broader ENVO class whose own direct parent is only `ENVO:00001996` mine drainage in the vendored ENVO slice. | `data/habitats/aquatic/acid_mine_drainage.yaml` lists all three parents. `data/raw/ontology_subclass_edges.tsv` lists only `ENVO:00001996` as the direct ENVO parent of `ENVO:00001997`. `data/habitats/engineered/industrial_wastewater.yaml` and `data/habitats/aquatic/groundwater__25377149.yaml` are the generated records for the two source-path parents. `src/habitatmech/seed.py` adds a GOLD parent-path edge after exact identity merging, so the exact merge makes branch-local context look like a global is-a edge on `ENVO:00001997`. | No existing row-level owner can express this suppression for an ontology-grounded exact record. The fix belongs in the GOLD parent-edge curation path: either revise the source decisions in `curation/decisions.tsv` if the two GOLD branch concepts are narrower than `ENVO:00001997`, or add an explicit curated parent-edge suppression consumed by `src/habitatmech/seed.py`. |

No blocker or minor findings found.

## Recommended Edits

1. Re-review the two GOLD concepts feeding `ENVO:00001997` in
   `curation/decisions.tsv`: `habitatmech:GOLD.4d88cc502b` for the
   engineered branch and `habitatmech:GOLD.d727388954` for the groundwater
   branch.
2. If their acid-mine-drainage leaves are exact to `ENVO:00001997` and the
   parent path is only GOLD filing context, add a curator-owned parent-edge
   override that lets `src/habitatmech/seed.py` drop
   `ENVO:00001997 -> ENVO:01000964` and
   `ENVO:00001997 -> habitatmech:GOLD.7f8e268653` without hand-editing
   `data/habitats/aquatic/acid_mine_drainage.yaml`.
3. If either GOLD branch concept is specifically industrial-wastewater AMD or
   groundwater AMD rather than generic AMD, change that source concept's
   decision so it mints a narrower HabitatMech record with `ENVO:00001997` as
   a parent instead of merging into the generic ENVO record.
4. Regenerate `ENVO:00001997` with a canary and inspect the parent list before
   any wider seed run.

## Follow-up Checks

| Edit | Narrowest proving check |
|---|---|
| Revise the two GOLD source decisions or add parent-edge suppressions. | Re-read the maintained input row(s), then run `just seed` to confirm the planned concept counts and mapping decisions. |
| Regenerate the acid-mine-drainage record. | `just seed-canary ENVO:00001997`, then inspect `data/habitats/aquatic/acid_mine_drainage.yaml` and confirm `parent_habitats` no longer contains `ENVO:01000964` or `habitatmech:GOLD.7f8e268653` unless a curator has explicitly proven those as strict parents. |
| Validate the regenerated record and corpus. | `just validate data/habitats/aquatic/acid_mine_drainage.yaml`, `just validate-strict data/habitats/aquatic/acid_mine_drainage.yaml --quiet`, `just term-requests-check`, `just validate-history`, and `just verify-corpus --max-diffs 1`. |

## Additional Notes

- `data/habitats/engineered/sediment__64234dd6.yaml`, the GOLD child
  `Engineered > Wastewater > Industrial wastewater > Acid mine drainage >
  Sediment`, correctly keeps `ENVO:00001997` as a parent because acid mine
  drainage is broader than acid-mine-drainage sediment.
- The Engineered GOLD acid-mine-drainage path has only one unanimous MIxS local
  triad study in `data/raw/gold_path_triads.tsv`; the environmental GOLD path
  is the one supported by 14 unanimous local-scale studies in the August 20
  decision note.
- `data/habitats/RETIRED.tsv` has a redirect from the former
  `habitatmech:GOLD.d727388954` page to `ENVO:00001997`, which matches the
  intentional merge of the guarded Environmental GOLD source concept.
