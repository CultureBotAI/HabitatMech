# YAML Record Review: geothermal power plant

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/geothermal_power_plant.yaml`
- Started UTC: 2026-10-08T16:48:44Z
- Finished UTC: 2026-10-08T16:51:30Z
- Verdict: pass

## Target

Generated HabitatRecord ENVO:00002215, geothermal power plant, ENGINEERED /
EXACT / SEEDED. The entire target was read. It has one PREGO attestation, one
strain-level taxon, two PREGO related aliases and one ontology parent.
Baseline: d3576b026.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/geothermal_power_plant.yaml`:
  passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/geothermal_power_plant.yaml`:
  passed, one file, zero errors.
- Fresh full corpus construction exactly reproduces the complete parsed target:
  one source, zero ITEM-reviewed contributors. Recomputed PREGO source mint
  `habitatmech:PREGO.a71a7effb2` has no decision; actual application preserves
  `prego_self_grounded`, ENVO:00002215, EXACT and no mapping predicate.
- Full QC was reused, not rerun for report-only work. Fresh same-turn tree
  comparison proves baseline d3576b026 equals validated cafc537cd. The completed
  local run passed 594 tests with three skips and all other gates: 191 histories,
  3,207 strict-valid/reproduced records, 32 overlays, provenance, floor, site,
  redirects, terms and report. Final-head/queue QC, labels and vendored checks
  passed; [PR #1735 receipt](https://github.com/CultureBotAI/HabitatMech/pull/1735#issuecomment-6064561377).
- Original PREGO edge/source reconstruction and SSSOM/KGX compatibility were
  not independently verified. No target literature or causal reference requires
  an additional focused reference validator.

## Identity and Grounding

`PATHS.tsv:682` agrees with the ontology identity and filename. PREGO's source
identifier is already ENVO:00002215, so self-grounding and omission of a
source-to-record mapping predicate are coherent. SEEDED correctly does not
claim an ITEM review merely because the source uses a valid ontology term.
The sole generated event matches source seeding; this review does not promote it.

The definition is faithfully inherited from ENVO and denotes a power plant
using geothermal heat, not the heat itself, a natural thermal spring or a
particular Icelandic installation. ENGINEERED is appropriate. ENVO:00002214
power plant is its direct ontology superclass and a strictly broader facility
class. No GOLD-path, ambiguous-leaf or authored-definition parent contributes.

A guessed `power_plant.yaml` read failed. Ignored-inclusive identifier/PATHS
searches found no generated parent record, but the complete vendored parent row
and primary OWL class were inspected. `parent_habitats` permits ontology CURIEs;
an external, valid ontology parent need not have its own source-attested YAML.
This is not a broken reference.

The PREGO aliases `geothermal power plantic` and `geothermal power plants`
match the inventory and are explicitly RELATED_SYNONYM, not exact lexical
identities. The awkward first form is a source-supplied search alias, not an
ENVO canonical name or an authored scientific definition. No identity defect
is established by preserving it with its current scope and source attribution.

## Evidence

- `prego_habitats.tsv:708` records one taxon, one direct taxon, score 3 and
  channel `annotated_genomes_isolates`. `prego_habitat_taxa.tsv:6305` records
  NCBITaxon:384616, Pyrobaculum islandicum DSM 4184, rank 1, score 3 and
  direct_flag TRUE. The YAML's TAXON unit, score, channel, rank and candidate
  pool of one reproduce correctly. The score is retained as PREGO evidence
  strength, not a probability, prevalence, growth optimum or assertion count.
- Fresh [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  confirms the active target and parent, canonical labels, definitions and
  direct subclass edge. SHA256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`;
  9,614,229 bytes. Local target: `ontology_terms.tsv` physical line 7297 /
  CSV logical row 7291; edge: `ontology_subclass_edges.tsv:5410`.
- Inspected [DSMZ catalogue DSM 4184](https://www.dsmz.de/collection/catalogue/details/culture/DSM-4184)
  identifies strain GEO3 and isolation from water at a geothermal power plant
  in Krafla, Iceland. This independently supports the narrow reported-from
  association. Its cultivation instructions are not measurements of every
  geothermal-power-plant habitat and were not copied into the record.
- Inspected [NCBI BioProject PRJNA16743](https://www.ncbi.nlm.nih.gov/bioproject/16743)
  explicitly binds Pyrobaculum islandicum DSM 4184 to taxonomy ID 384616 and
  describes a monoisolate genome project. The [taxonomy page](https://www.ncbi.nlm.nih.gov/taxonomy/384616)
  resolves to the same strain title; the BioProject supplies the inspectable
  ID/name correspondence rather than relying on a title or search snippet alone.

The taxon is not marked `is_characteristic`. A single isolate at one plant does
not establish a characteristic community, abundance, universal distribution,
or a facility-wide metabolic capability. No independent replicate count is
inferred from the DSMZ and NCBI descriptions of the same strain.

## Completeness

No xrefs, environmental parameters, literature EvidenceItems, causal graphs,
discussions or datasets are asserted. Their optional absence is not a defect.
Do not generalize the strain's cultivation temperature, oxygen requirements,
medium, proteins or metal-reduction experiments to the whole habitat class.
iModulonDB is not applicable: a taxon association is present, but no target
gene, regulator, expression module or transcriptomics claim is made.

Ignored-inclusive ontology ID, PREGO mint, label, stem and strain searches
covered curation, raw inventories, PATHS/RETIRED, configuration, docs, tests,
history, research, individual reports and the research manifest. Filename
traversal covered curation/history/research. No target decision, authored
definition, exclusion, overlay, separate session history, research file or prior
individual report was found in those bounds.

Exact-field/pipe-member scanning of every raw TSV found the target ontology
term/edge and PREGO habitat/taxon rows above, not target GOLD/triad/parameter
rows. Ignored-inclusive find under build, data/raw and configured kg-microbe
data, including paths under prego directories, found only the two committed
PREGO inventories, not the original PREGO source node/edge dumps. The original
score and synonym derivations were therefore not reconstructed from upstream
raw files; their faithful inventory-to-record representation was checked.

## Findings

None found: zero blockers, zero major findings, zero minor findings.
This bounded pass supports the facility identity and explicitly attributed
strain association, not every original PREGO processing step or a characteristic
microbial community.

## Recommended Edits

No scientific edit is established. Preserve ontology identity, the true power-
plant genus, PREGO count/unit/score provenance, related alias scope and the
strain-level reported-from interpretation. Do not mark the taxon characteristic
or promote the record's review status from this report alone. Any source-alias
cleanup belongs in a governed PREGO normalization decision, not hand-edited YAML.

## Follow-up Checks

For future changes, verify source score/alias provenance and taxon identity,
keep isolation evidence separate from cultivation conditions, and test that
the one-taxon candidate pool is not inflated. Authorized curation needs maintained
inputs, dry seed, inspected canary, history where required, provenance, labels,
schema, exact reproduction, generated artifacts and full QC.

## Additional Notes

Only this new report was written. No scientific/generated artifact, earlier
report, curation history, review state or GitHub item changed. Primary articles
returned by search were leads; their mechanistic findings were not adopted.
