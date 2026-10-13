# YAML Record Review: animal waste material

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/animal_waste_material.yaml`
- Started UTC: 2026-10-07T04:30:15Z
- Finished UTC: 2026-10-07T04:34:11Z
- Verdict: needs curation (0 blocker, 2 major, 1 minor)

## Target

Read the entire generated HabitatRecord and rendered page. Identifier
`ENVO:00002276`, ENGINEERED / EXACT / REVIEWED. Three contributing concepts
are BacDive Solid-animal-waste, GOLD's Animal waste below Solid waste, and
PREGO's unqualified ontology class. Five source-attributed synonym entries,
two parents, three attestations, 18 associated taxa and four history events
are present. No definition, parameter, xref, literature-evidence object,
causal graph, discussion or dataset is asserted.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/animal_waste_material.yaml`: passed.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/animal_waste_material.yaml`: passed, one file, zero errors.
- Read-only `build_corpus()` / `build_document()` comparison reproduced every
  parsed field: three source concepts, three reviewed sources, 18 taxa and
  four events. Actual automatic/curated routes were inspected for all three
  sources and the immediate GOLD parent.
- Full QC/OAK were not repeated per record. Scientific inputs/products
  remain at `43e6c5d0fb508bcbf7341b8ca5be0141a495f2ed`; reuse successful
  [exact-baseline QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37569153392),
  freshly checked at that SHA earlier in this continuation, for corpus,
  reference, history and product gates. Fresh ENVO, MeSH and NCBI checks
  below supplement these; OAK does not certify ecological associations or
  synonym scope.
- Ignored-inclusive filename searches of `build` and configured kg-microbe
  `data` found no original GOLD, BacDive or PREGO node/edge dumps, nor the
  NCBI label/merge files. Original associations were not re-extracted; their
  committed aggregate and retained taxon rows were fully compared instead.

## Identity and Grounding

The ontology class, label and organic-waste parent reproduce from
`data/raw/ontology_terms.tsv:7351` and `ontology_subclass_edges.tsv:5467`.
PATHS line 697 agrees. Fresh primary
[ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
at current master SHA `a2455d1a77e46bb8a664d65a157166b539269042` confirms
active ENVO:00002276, no textual definition, a BROAD synonym `animal waste`,
and named parent ENVO:00002873, organic waste material. The record's missing
definition reflects its source, not a dropped authored definition.

The source keys and maintained decisions are:

| Source key | Maintained row | Actual result |
| --- | --- | --- |
| habitatmech:BACDIVE.a862e7c17e | decisions.tsv:66, ITEM GROUND | ENVO:00002276 / EXACT / exactMatch |
| habitatmech:GOLD.e8c535ac1c | decisions.tsv:1288, ITEM REVIEW | ENVO:00002276 / CLOSE / closeMatch |
| habitatmech:PREGO.d47fcbddfc | decisions.tsv:1506, ITEM REVIEW | ENVO:00002276 / EXACT, self-grounded |

BacDive's automatic route instead points CLOSE to generic waste material
ENVO:00002264 through `isolation_source_groundings.tsv:284`; the explicit
curation override moves it to animal waste and declares exact equivalence.
The GOLD route is `gold_leaf_synonym`, not a verified exact label match.
The PREGO identity is already its source ontology ID. Aggregate EXACT is
the strongest contributing status, not proof that every source is exact.
REVIEWED correctly follows three ITEM decisions, but does not validate
the scientific scope of those decisions.

## Evidence

Structured exact-field/pipe-member searches covered all 14 raw TSVs:

- `bacdive_isolation_sources.tsv:125` records 11 strains and eight taxa.
  All eight rows at `bacdive_source_taxa.tsv:2559-2566` are retained, with
  association counts 3, 2 and six 1s, totaling 11; each pool is eight.
- `gold_ecosystem_paths.tsv:227` records the full path
  `Engineered > Solid waste > Animal waste`, 79 organisms and nodes
  `gold.ecosystem:3514|gold.ecosystem:3846|gold.ecosystem:4278`. The first-ID
  note is correct. Descendant hits, including Manure slurry and Liquid
  manure, are not additional target attestations or counts.
- `gold_path_biosamples.tsv:576` separately records 13 bulk biosamples.
  `gold_studies.tsv:953`, `:1834` and `:1856` link Gs0117456, Gs0133114
  and Gs0133136; the latter two also cover other paths. These counts and
  contexts must not be added to the 79-organism assertion. Public page
  retrieval returned an application error for the first study and inaccessible
  results for the other two. Live study identities/content remain unverified;
  no accession is declared nonexistent and no study properties are transferred.
- `prego_habitats.tsv:338` records ten taxa, ten direct assertions, maximum
  score 4 and annotated_genomes_isolates. All ten rows at
  `prego_habitat_taxa.tsv:6495-6504` are retained with that score/channel and
  no corroboration. BacDive ranks/counts and PREGO ranks/scores are separate
  source measures, not 18 ranked members of one measured community.

Fresh NCBI Taxonomy efetch resolved all 18 IDs: ten species and eight
strains. All 17 populated labels agree with current NCBI. The one missing
name, BacDive ID NCBITaxon:1257027 at rank three, resolves through explicit
AkaTaxIds to [NCBITaxon:713595, Streptomyces fenghuangensis](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1257027&retmode=xml).
It is a resolvable source alias, not a broken or invented taxon. No retained
row is marked characteristic; the rendered page explicitly uses reported
association wording. Original source sampling evidence was not reconstructed.

Inspected the [USDA ARS authors' account of McGarvey et al. 2004](https://www.ars.usda.gov/research/publications/publication/?seqNo115=163878),
including citation, interpretive summary and full technical abstract. Their
dairy-waste study distinguishes solid and liquid waste fractions and examines
manure and treatment waters. This supports the narrower meaning of solid
animal waste; it does not identify these 11 BacDive strains or prove an
ontology mapping from a specific sample. No study taxon, abundance, pathogen
result or operational parameter is copied into this record.

Read both full local parents. ENVO directly supplies organic waste material.
Primary [MeSH descriptor](https://id.nlm.nih.gov/mesh/D062611.json) and
[concept scope](https://id.nlm.nih.gov/mesh/M0568791.json) confirm active
Solid Waste and a definition covering refuse/sludge and specified solid,
semisolid or contained waste, with exclusions for some dissolved wastes.
Thus the GOLD liquid-manure descendants alone do NOT prove this MeSH parent
false: MeSH is not merely the physical solid phase. However, the inherited
GOLD edge does not independently prove that every unqualified animal-waste
material meets that waste-management scope. Reassess it with source identity;
no additional definitive hierarchy finding is counted here.

## Completeness

Ignored-inclusive ID, label, slug and all three source-key searches covered
curation, history, configuration, docs, tests, research, the research
manifest, PATHS and RETIRED; filename searches covered curation/history/
research. No target-owned definition, causal overlay, parent exclusion or
separate history session was found in those bounds. The three maintained
decisions are present. A dust/ash research mention of vocabulary siblings is
only a lead and supplies no independent equivalence evidence.

No parameter or triad contribution appears for the target in the inspected
inventories. A missing ontology definition is not authority to invent one
locally. iModulonDB is not applicable to these source habitat associations:
the record supplies no gene, regulator, expression dataset or mechanistic
claim for which module evidence would resolve its mapping or label issues.

## Findings

1. **Major: the BacDive exact-identity decision loses the solid qualifier.**
   The maintained rationale declares Solid-animal-waste exactly equivalent
   to unqualified ENVO animal waste material without evidence that the latter
   excludes other physical forms. The inspected primary waste study supports
   a real solid/liquid distinction. Replacing a generic waste mapping with a
   more specific animal-waste term improves placement, but does not itself
   establish exact identity. The derived exact BacDive synonym repeats this
   unsupported equivalence. Owner: `curation/decisions.tsv`, source key
   `habitatmech:BACDIVE.a862e7c17e`.
2. **Major: ENVO and GOLD synonyms are asserted more strongly than their
   evidence permits.** ENVO explicitly types `animal waste` broad, while the
   record emits it exact. GOLD's close-mapped `Animal waste` is also emitted
   exact without separate lexical-equivalence evidence. PREGO's two related
   entries are correctly weaker. Owners: governed typed ontology extraction
   and `src/habitatmech/seed.py` source-synonym handling, represented by
   [#1249](https://github.com/CultureBotAI/HabitatMech/issues/1249) and
   [#1459](https://github.com/CultureBotAI/HabitatMech/issues/1459), both
   freshly verified open in this continuation. Counted together as one
   record-level synonym-scope finding, with two ingestion mechanisms.
3. **Minor: the BacDive taxon alias lacks a resolvable name.** Raw taxon row
   2561 already omits the label for 1257027; NCBI provides its canonical
   identity/name through 713595. Owner: governed BacDive/taxonomy inputs and
   `_load_taxon_labels` in `src/habitatmech/extract.py`, not the YAML. The
   same alias-aware label-resolution limitation affects other reviewed taxa,
   but this is a distinct source row from the PREGO examples in #1257.

No blocker was established: the retained ENVO class denotes the requested
animal-waste material, and all referenced taxon IDs resolve. The mapping
findings concern unsupported source equivalence and lexical scope.

## Recommended Edits

In separately authorized curation, replace the unsupported exact BacDive
identity with a justified broader-parent placement on a minted solid-animal-
waste concept, unless target-specific evidence establishes true equivalence.
`GROUND_AS_PARENT` to ENVO:00002276 is the conservative candidate to validate.
Preserve its 11-strain attestation and all eight taxon associations on the
source concept; do not discard observations while separating identities.

Review GOLD's full-path meaning independently. Its source tree includes
slurry/liquid descendants, so do not assume it is identical to the explicitly
solid BacDive bin or strengthen closeMatch by decree. Preserve PREGO's
generic ontology identity. If the source-derived MeSH parent is subsequently
shown to over-scope the retained generic record, its guarded removal belongs
in `curation/gold_parent_exclusions.tsv`, keyed by the GOLD source, exact
path and expected parent; do not remove the supported ENVO parent.

Recover typed ontology synonyms and preserve ENVO's broad scope. Give GOLD's
close-mapped label justified weaker scope or source-only provenance. Do not
globally downgrade genuinely exact synonyms, and do not assume the recently
added GOLD strict-ancestor guard fixes these different cases.

Refresh the missing taxon label and merged-ID handling from versioned inputs,
retaining the original source ID and checking collisions before canonical
deduplication. Use append-only curation history for later authorized changes;
never patch generated records/pages or raw checksums to simulate a source
refresh. No definition or causal graph is needed merely to fix these issues.

## Follow-up Checks

Regress the BacDive qualifier boundary, provenance-preserving association
movement, generic PREGO identity, each source's count/unit and review state,
ENVO broad versus GOLD close-derived synonym scope, and the taxon alias/name.
Canary the retained generic record and any newly minted source record after
`just seed`; inspect both before full application. After authorized changes
run provenance, strict schema, `just verify-corpus`, `just validate-products`,
history/site checks and `just qc`. Compare semantic-map inputs and genuinely
rebuild if splitting records or adding the missing taxon name changes them.
Reassess redirects only from committed identity changes, not by hand.

## Additional Notes

The published class remains REVIEWED because its inputs have ITEM decisions;
this report does not revoke that status or certify those judgments. Only this
new report was authored for the target. No scientific edits, history changes,
paid research or GitHub mutation occurred. The all-record goal remains active.
