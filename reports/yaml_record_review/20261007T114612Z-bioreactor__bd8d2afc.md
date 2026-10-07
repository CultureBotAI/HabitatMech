# YAML Record Review: Bioreactor (grass composting)

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/bioreactor__bd8d2afc.yaml`
- Started UTC: 2026-10-07T11:45:06Z
- Finished UTC: 2026-10-07T11:46:12Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.00fe86978b`,
Bioreactor, ENGINEERED, NARROW/SEEDED. GOLD4873 attests
`Engineered > Solid waste > Grass > Composting > Bioreactor`.
`data/habitats/PATHS.tsv:1267` pins this record. It is distinct from the
wood/unknown-material composting reactors and the grass-fermentation reactor.

## Validation

- `just validate data/habitats/engineered/bioreactor__bd8d2afc.yaml`: pass.
- `just validate-strict data/habitats/engineered/bioreactor__bd8d2afc.yaml`:
  one file, zero errors.
- Parsed all-field reproduction using `build_corpus`/`build_document`: pass;
  one source concept, zero reviewed sources, zero taxa, one seeding event.
- Shared unchanged-tree checks in this review session: `just verify-corpus`
  reproduces all 3,207 records exactly; `just validate-history` validates 146.
- Current official ENVO compost definition, active status, synonym types and
  parent were inspected directly. The generic bioreactor check performed
  earlier in this session is reused explicitly, not presented as another fetch.
- Full QC/OAK/vendored checks are reused from the identical scientific tree
  merged as `c54d9263c97873f825caf023896571c256c1deb6`; they were not rerun
  for this report-only target. No target graph or taxon claim requires a
  graph/taxon-specific validator.

## Identity and Grounding

Actual seeder resolution is `gold_narrower_than_leaf_match` with no applied
ITEM decision. The exact full path reproduces the mint. The shallow generic
`Engineered > Bioreactor` path claims ENVO:00002123; this path keeps a qualified
mint with that broader device genus. ENGINEERED and NARROW/SEEDED agree with
the source and lack of ITEM review. No broader record's review status transfers.

Read the entire parent `data/habitats/engineered/composting.yaml`,
`habitatmech:GOLD.143ceb8669`. It is presently NARROW under ENVO:00002170,
compost. The actual parent route is `gold_narrower_than_mapping_match`, via
`data/raw/isolation_source_groundings.tsv:72`; its two collapsed nodes are
4872/4874, not additional child nodes. Current ENVO
`a2455d1a77e46bb8a664d65a157166b539269042` identifies compost as a manure
material derived from aerobic decomposition, with parent ENVO:03501300 and no
typed synonyms; the term is active. Thus this particular inherited parent
currently makes a vessel a subtype of material. The generic bioreactor genus
is independently sound and must remain.

## Evidence

- `data/raw/gold_ecosystem_paths.tsv:1362`: one node4873, complete path,
  zero organism/study/biosample/assertion counts in this inventory. Count/unit
  omissions in the YAML are faithful.
- `data/raw/gold_path_biosamples.tsv:467`: 25 biosamples in the separate
  GOLD bulk inventory. These are not organism assertions or a reason to
  populate the record's current GOLD count with 25.
- `data/raw/gold_studies.tsv`: six exact target-path memberships at rows31
  (Gs0045248),164 (Gs0050893),376 (Gs0063625),379 (Gs0063773),393 (Gs0069864),
  524 (Gs0099430). The first also lists tropical rainforest soil, which is
  study cross-context, not habitat equivalence. All six pages were attempted:
  three were inaccessible; Gs0063625/Gs0063773/Gs0099430 returned GOLD's request
  error. Exact-ID web searches yielded no results. Source identities and path
  membership are verified against the frozen inventory, not live study detail.
- Structured inspection covered all 14 raw TSVs with exact field/pipe-member
  matches and node keys taken from the real collapsed row. The other eleven
  inventories had no target hits; in particular there is no attached taxon,
  triad or parameter assertion to import.
- [Suzuki et al. 2004](https://pubmed.ncbi.nlm.nih.gov/15246435/),
  DOI:10.1016/j.biortech.2004.02.020: freshly inspected full abstract and
  article-level identifiers through NCBI efetch. The study separates an aerobic
  composting reactor from the organic materials processed in it and resulting
  compost. It supports only the device/material distinction here. It studies
  wood chips, not this grass source; do not import feedstock mixtures, duration,
  maturity thresholds, taxa or conditions. PubMed HTML separately rate-limited
  the request, but the structured abstract succeeded. Full text not inspected.
- [Official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
  and vendored `ontology_terms.tsv:7260`/`ontology_subclass_edges.tsv:5371`
  agree on the parent's compost genus.

## Completeness

Ignored-inclusive identifier/path/slug searches in curation, histories,
configuration, research/manifest, PATHS and RETIRED locate no target-owned
decision, definition, exclusion, overlay or research report. Broader Bioreactor
label searches expose generic research/overlays but do not establish target
ownership. Raw rows were scanned independently of ignore rules. Empty optional
definition, taxa, parameters, evidence, graphs, discussions and datasets are
not independently defects; no specific microbial or process claim is licensed
by the frozen source or inaccessible study pages. Do not inherit generic
bioreactor content or neighboring grass-fermentation conditions.

## Findings

1. **Major: reactor is made a kind of compost material.** Target line8 adds
   `habitatmech:GOLD.143ceb8669`, whose current broader class is ENVO:00002170.
   Source-path context does not make a containment device a kind of its
   material contents. Owner: `curation/gold_parent_exclusions.tsv` for this
   contribution. The parent source's own process/material interpretation
   belongs to a separate ITEM review in `curation/decisions.tsv`; if that
   interpretation later changes, deliberately reassess the guarded exclusion.

## Recommended Edits

1. Add a guarded exclusion for `habitatmech:GOLD.00fe86978b`, its exact grass
   composting bioreactor path and expected parent `habitatmech:GOLD.143ceb8669`.
   Preserve ENVO:00002123, mint, source4873, zero-count omissions, predicate
   and NARROW/SEEDED status. Do not change the parent interpretation implicitly.
2. Append curation history and regenerate only through supported tools in a
   later authorized curation session. Do not hand-edit this generated record.

## Follow-up Checks

Recover original study metadata before making any specific biological claim.
For the bounded hierarchy fix, add a full-corpus differential regression for
only this parent contribution and audit event; dry seed, inspect target canary,
validate strict/history and exact corpus reproduction, refresh affected map/site
products, and run full QC/OAK. Preserve independently supported parent routes.

## Additional Notes

Read-only individual review; only this new report was written. Scientific
inputs, generated artifacts, statuses and GitHub items were not changed.
iModulonDB is not applicable without a gene, regulator, named organism/dataset
or transcriptomic claim; absence from it is not negative habitat evidence.
