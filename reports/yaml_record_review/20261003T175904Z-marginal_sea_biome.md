# YAML Record Review: marginal sea biome

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marginal_sea_biome.yaml`
- Started UTC: 2026-10-03T17:57:25Z
- Finished UTC: 2026-10-03T17:59:04Z
- Verdict: pass

## Target

Read the entire generated HabitatRecord, `ENVO:01000046`, marginal sea biome,
AQUATIC, EXACT, SEEDED. PREGO is the sole attesting source; its source-decision
key is `habitatmech:PREGO.9dc267c401`, computed with the seeder's `mint`.
`PATHS.tsv:767` pins the stem. The single seed event is not ITEM review.

## Validation

- `just validate data/habitats/aquatic/marginal_sea_biome.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marginal_sea_biome.yaml`: one
  file, zero errors.
- Fresh full `just qc` was running at review finish: lint, documentation and
  raw provenance passed; tests were active. Later corpus, history and site
  gates are not claimed complete from focused validation.
- Fetched current official ENVO OWL and verified its bytes against the local
  parsed copy: SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- All nine displayed NCBITaxon IDs resolved directly through current NCBI
  efetch, with exact scientific-name matches and no alias redirects.
- OAK identity validation is deferred to required CI for this reports-only
  change. Its configuration excludes taxon labels and synonym scopes; those
  are not inferred correct merely from a green identity gate.

## Identity and Grounding

The identifier, label, full definition and sole named parent agree with
[current official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
and `ontology_terms.tsv:7555`. `ENVO:00000447` marine biome is genuinely
broader: the target specifies a marine biome associated with a partly enclosed
ocean region. The named edge is in `ontology_subclass_edges.tsv:5685`.
Read the full maintained marine-biome parent for context, not as another
completed review.

Keep this biome distinct from `ENVO:00000016` sea. Current ENVO treats
`marginal sea` as a narrow synonym of sea, whereas the target is a biome.
The separate GOLD Marginal Sea path occurs on `sea.yaml`; none of its
attestations or counts belongs to the present PREGO-only record merely because
the names overlap. This review does not adjudicate that other record's mapping.

## Evidence

`prego_habitats.tsv:346` supplies nine distinct taxa, nine direct assertions,
maximum score 4 and the annotated-genomes/isolates channel. The YAML faithfully
reports a TAXON count, not a sample or isolate count.

All nine retained rows at `prego_habitat_taxa.tsv:7491-7499` were compared to
the YAML using structured CSV/YAML parsing. IDs, labels, score 4, ranks 1-9,
pool 9, direct flags TRUE, channel and absent corroboration agree. The whole
candidate pool is represented; no omitted candidates need extrapolation.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy) verified the displayed
names for 1041152, 1121007, 1121912, 1122137, 1123053, 1123251, 1123270,
59919 and 693972. Matching names verifies identity, not an independent habitat
observation. No entry asserts `is_characteristic`.

PREGO's four-string pipe contains the canonical label plus `marginal sea`,
`marginal seal` and `marginal seas`. The three noncanonical strings are quoted
as source-attributed RELATED_SYNONYM entries, not exact ontology synonyms or
new biological claims. The suspicious lexical variant alone is not evidence
of a seeder transcription error. Source-label lookup and taxon projection were
inspected in `src/habitatmech/seed.py:1012-1114`.

## Completeness

Ignored-inclusive identifier, label, stem and minted-key searches covered
curation, raw inventories, PATHS, history, research and individual review
reports. No target ITEM decision, authored definition, causal overlay,
dedicated session history or previous individual review was found. References
to temperate marginal sea biome in unrelated indoor-habitat research are not
target evidence. SEEDED is appropriate.

The ontology definition and source attestation suffice for the present
descriptive record. Optional measurements, causal graphs, discussions and
datasets must not be filled from the separate GOLD source or generic marine
biology. iModulonDB is not applicable: there is no gene, regulator, expression
dataset or molecular mechanism claim.

## Findings

None found for the bounded current record. Blockers: 0. Major: 0. Minor: 0.
This is not a claim that every PREGO association has independent field-study
support, or that the parent record has received its own complete review.

## Recommended Edits

None required for the current claims. Any future endorsement belongs to an
ITEM row keyed to the PREGO source concept in `curation/decisions.tsv`; source
lexical cleanup belongs to a governed PREGO input/extraction policy, not a
manual edit of generated YAML. Do not merge the biome with sea by name alone.

## Follow-up Checks

Complete full QC and required network identity validation before merging the
report. A future scientific change needs a seed canary, source and taxon
comparison, strict schema, provenance, history, corpus and site reproduction.
Keep taxon associations observational unless inspected evidence supports a
stronger assertion.

## Additional Notes

The OLS web request was inaccessible; official OWL retrieval succeeded and
supplied the inspected ontology evidence. An initial diagnostic used the wrong
CSV column name (`direct`); after inspecting the header, the full structured
comparison and live taxon lookup completed. A separate optional GOLD mint
diagnostic hit the sandbox's uv-cache restriction; it is not used as evidence.
No scientific input, generated record, page or curation history changed.
