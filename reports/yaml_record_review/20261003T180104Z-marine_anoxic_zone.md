# YAML Record Review: marine anoxic zone

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/marine_anoxic_zone.yaml`
- Started UTC: 2026-10-03T17:59:41Z
- Finished UTC: 2026-10-03T18:01:04Z
- Verdict: needs curation

## Target

Read the full generated HabitatRecord, `ENVO:01000066`, marine anoxic zone,
AQUATIC, EXACT, SEEDED. PREGO is the only source, with computed decision key
`habitatmech:PREGO.2217ebab92`. `PATHS.tsv:772` pins the filename. The
deterministic seed event does not constitute item-level curation.

## Validation

- `just validate data/habitats/aquatic/marine_anoxic_zone.yaml`: pass.
- `just validate-strict data/habitats/aquatic/marine_anoxic_zone.yaml`: one
  file, zero errors.
- Fresh full `just qc` was still active at review finish; lint, documentation
  and raw provenance passed, tests were running. Later full-corpus gates are
  not implied by the focused validators.
- Inspected the current official ENVO OWL retrieved and byte-verified this
  batch, SHA-256
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
- All four NCBITaxon IDs and names resolved directly and exactly in fresh
  structured NCBI efetch, without alias redirects.
- Required CI will perform network OAK identity validation. The configured
  gate does not check taxon labels or synonym scopes. No DOI/PMID or causal
  reference is present.

## Identity and Grounding

Identifier, label and full definition match
[official ENVO](https://raw.githubusercontent.com/EnvironmentOntology/envo/master/envo.owl)
and `ontology_terms.tsv:7573`. The definition concerns an oxygen-depleted
marine region, retaining its qualified statements about water exchange,
stratification and oxygen consumption. It is not a claim about every freshwater
anoxic zone or an isolated volume of anoxic water material.

The sole named parent, `ENVO:01001201` marine environmental zone, is genuinely
broader and agrees with the current OWL and `ontology_subclass_edges.tsv:5705`.
The parent's definition was inspected in full; it is a region within a marine
environment. `ontology_terms.tsv:8695` supplies the valid term. An
ignored-inclusive exact-root search found no standalone generated parent
record, which is not a broken ontology reference.

Current ENVO explicitly declares `dead zone` with `hasRelatedSynonym`.
The generated ENVO entry incorrectly says EXACT_SYNONYM. PREGO independently
supplies a RELATED_SYNONYM entry with the same spelling; that separate
source assertion is already correctly scoped.

## Evidence

`prego_habitats.tsv:422` reports four distinct taxa, four direct assertions,
maximum score 3 and the annotated-genomes/isolates channel. YAML faithfully
uses TAXON, not an organism, sample or independent-study count.

All four retained rows at `prego_habitat_taxa.tsv:7600-7603` were checked with
structured CSV/YAML parsing: IDs, labels, scores, ranks 1-4, pool 4, TRUE
direct flags, channel and absent corroboration agree. Fresh
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy) responses matched
1089550 Salisaeta longa DSM 21114, 35743 Halorubrum sodomense,
43928 Halobaculum gomorrense and 748449 Halobacteroides halobius DSM 5150.
These checks verify displayed taxon identity and source projection, not
independent ecological evidence. None is marked `is_characteristic`.

PREGO's five-string alias pipe produces four noncanonical related synonyms,
including `dead` and `marine anoxics`. Those remain explicitly source-attributed
lexical assertions, not adopted exact biological identities. The source-label
lookup and association projection in `ingest_prego` were inspected.

## Completeness

Ignored-inclusive searches of the identifier, source key, label and stem
covered curation, inventories, PATHS, history, research and individual review
reports. The sampled `ok` judgment at `curation/samples/exact-20260814.tsv:24`
is not an ITEM decision. No target ITEM row, authored definition, overlay,
dedicated history or prior individual target review was found. The earlier
freshwater-anoxic-zone review mentions this term as a nonmatching candidate;
it does not review this marine record. SEEDED remains appropriate.

Optional measurements, graphs, discussions and datasets need specific evidence,
not generic completion text. iModulonDB is not applicable: the record makes
observational habitat associations and has no gene, regulator or expression
dataset claim requiring a module cross-check.

## Findings

- **Major M1: related ENVO synonym promoted to exact.** `dead zone` is
  explicitly related in current OWL but exact in this record. The maintained
  owners are the governed ontology extraction/inventory contract and
  `ConceptStore.get` in `src/habitatmech/seed.py:406-407`. This is another
  witness for existing #1249, not a separate root-cause issue.
- Blockers: 0. Major: 1. Minor: 0.

## Recommended Edits

Recover typed synonym assertions through the reproducible ontology input
contract and emit this ENVO entry as related. Preserve genuinely exact synonyms
elsewhere and the independently sourced PREGO entry; do not apply a blanket
downgrade or edit generated YAML. Keep identity, definition, true parent,
counts, four taxon associations and source provenance unchanged.

## Follow-up Checks

Add this witness to #1249's exact/related/unknown/mixed-source regressions.
Canary the record and run provenance, strict schema, label, history, corpus,
site and full QC checks. Compare semantic-map input hashes before deciding
whether a scope-only correction requires a map rebuild.

## Additional Notes

All 441 returned open and closed issues, including their returned comments,
were searched for this identifier and synonym failure; #1249 owns the defect.
No independent literature claim or global statement about all ontology
synonyms is inferred from this one witness. No scientific input, generated
record, page or curation history changed.
