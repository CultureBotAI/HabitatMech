# YAML Record Review: bituminous sand

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/bituminous_sand.yaml`
- Started UTC: 2026-10-07T11:57:38Z
- Finished UTC: 2026-10-07T13:35:34Z
- Verdict: needs curation (0 blocker, 2 major, 0 minor)

## Target

Read the entire generated HabitatRecord `ENVO:03600013`, bituminous sand,
ENGINEERED, CLOSE/REVIEWED. It denotes a naturally occurring environmental
material, with one GOLD source path, four synonym entries, two parents and
two history events. `data/habitats/PATHS.tsv:931` pins its filename. The review
was interrupted for PR publication and resumed against merged commit
`00a42547e41e3bb2380c97736976cc8dff9823ec`; the target remained unchanged.

## Validation

- `just validate data/habitats/engineered/bituminous_sand.yaml`: pass.
- `just validate-strict data/habitats/engineered/bituminous_sand.yaml`:
  one file, zero errors.
- Read-only `build_corpus`/`build_document` all-field comparison: pass;
  one contributing source, one reviewed source, no authored definition or
  parent exclusion applied.
- Fresh `just verify-corpus`: 3,207 expected and present, zero missing,
  extra or differing records. Fresh `just validate-history`: 148 valid records.
- Fresh full-corpus `just validate-products`: 1,178 canonical matches,
  one synonym match, five accepted exceptions, 2,056 no-adapter skips.
  The identity label is canonical; this gate does not check the semantic
  validity of `parent_habitats` or the target's synonym entries.
- Full QC was not rerun for this read-only report. The unchanged scientific
  tree passed the native merge-group QC before the baseline commit landed;
  the preceding local run had 524 passed and three skipped tests. These are
  explicitly reused results, not additional executions for this review.

## Identity and Grounding

`mint("GOLD", "Engineered > Built environment > Mine > Oil sands")`
reproduces `habitatmech:GOLD.6a5b013cc9`. Calling the maintained resolver with
the actual inventories gives `gold_leaf_synonym`, `ENVO:03600013`, CLOSE and
`skos:closeMatch`. The ITEM/REVIEW at `curation/decisions.tsv:1741` endorses
that resolution. Its generated REVIEW event and REVIEWED status are accurate;
this review does not promote or replace them.

The canonical label and material definition match the vendored ontology and
the current official ENVO OWL. Oil sands and tar sands are supported alternate
names for the mixture. CLOSE conservatively preserves the GOLD mining-path
framing rather than claiming exact source-to-ontology equivalence. ENGINEERED
is traceable to the source bucket, not a scientific assertion that all natural
bituminous sand is manufactured.

The two parents have different origins. The ontology contributes environmental
material (`ENVO:00010483`); GOLD's immediate path resolves to mine
(`ENVO:00000076`). The entire `data/habitats/engineered/mine.yaml` was read and
its source path checked. Mine is an excavation, not a broader material class.
The actual source-path contribution is therefore an unsupported is-a edge.

## Evidence

- `data/raw/gold_ecosystem_paths.tsv:1266` contains the exact path, nodes
  `gold.ecosystem:5840|gold.ecosystem:5841`, depth four and zero organism,
  study, biosample and total assertions. First-node display, the two-node note,
  and omission of count/unit reproduce the seeder's zero-count behavior. The
  omission is not evidence that microorganisms are absent from oil sands.
- `data/raw/ontology_terms.tsv:10062` contains the identity, definition and
  three ENVO aliases. This is a physical file line; the CSV record position
  differs because other records contain embedded newlines.
  `data/raw/ontology_subclass_edges.tsv:8458` supplies the material parent.
- [Official ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl):
  resolved the current upstream revision through the repository API and parsed
  the three exact classes from the immutable OWL. The target has only
  `ENVO:00010483` as a named direct superclass. Its editor note explicitly
  treats it as material and distinguishes a possible future deposit/location
  term. Importantly, `crude bitumen` is genuinely `hasExactSynonym` upstream;
  this particular error is not caused solely by flattening related synonyms.
- [Government of Alberta, Oil Sands glossary](https://history.alberta.ca/energyheritage/sands/glossary.aspx):
  inspected the Bitumen, Extraction and Oil sands entries. They distinguish
  viscous hydrocarbon from the sand/mineral mixture containing it and describe
  their separation. The same glossary supports tar sands/bituminous sands as
  mixture names. It does not support identifying the extracted constituent
  with the entire mixture.
- [Government of Alberta, What are the Oil Sands?](https://history.alberta.ca/energyheritage/bitumount/oil-sands/what-are-the-oil-sands.aspx):
  inspected the material-composition and separation discussion. It corroborates
  the mixture/constituent distinction, not an is-a relation to a mine.
- [Dinh et al., Microstructural characterization of a Canadian oil sand](https://arxiv.org/abs/1301.2658),
  author manuscript associated with DOI `10.1139/T2012-072`, Canadian
  Geotechnical Journal 49(10), 1212-1220: inspected the primary abstract and
  bibliographic metadata. The authors observe bitumen between sand grains in
  samples from one formation. This supports the distinction, not universal
  properties or taxa. Their lack of evidence for a thin interfacial water film
  differs from the general historical webpage description; neither microscopic
  arrangement is adopted as a universal record claim.

## Completeness

Structured exact-field and pipe-member searches covered all 14 raw TSVs using
the target ID, mint, both GOLD node IDs, full path, label and slug. Matches occur
only in the GOLD ecosystem inventory, ontology terms and ontology subclass
edges. No target-linked study, biosample, triad, parameter or taxon row was
found in those bounded inventories. Original GOLD individual records were not
independently recounted, and no location-specific microbiology was inferred.

Ignored-inclusive searches covered curation, histories, configuration,
research/manifest, PATHS, RETIRED and individual review reports. They locate
the ITEM decision and filename pin but no target-owned term request, causal
overlay, parent exclusion or research report in those surfaces. An oil-sands
pit-lake review mentions this material; it is not a review of this target.
Optional parameters, taxa, citations, graphs, discussions and datasets can
remain empty without record-specific evidence. iModulonDB is not applicable:
the target names no gene, regulator, organism/dataset or transcriptomic claim.

## Findings

1. **Major: mining context emitted as a strictly broader habitat.** A portion
   of bituminous sand is not a kind of excavation. The GOLD link is contextual;
   the independent environmental-material genus remains supported. Owner:
   `curation/gold_parent_exclusions.tsv`, keyed to the exact mint, source path
   and expected parent `ENVO:00000076`. Do not invent a term definition to
   suppress the edge or remove the true ontology parent.
2. **Major: constituent treated as an exact synonym of the mixture.**
   `crude bitumen` conflicts with the record's material definition and the
   inspected terminology and primary observation. ENVO currently makes the
   same assertion, so provenance is faithful but does not resolve the scientific
   conflict. Owners: the upstream ENVO assertion and its local import through
   `src/habitatmech/extract.py` and `src/habitatmech/seed.py`. A scope-preserving
   extractor alone will not repair an upstream exact synonym. A deliberate
   upstream correction or explicit maintained, target-specific override is
   needed; do not hand-edit generated YAML or silently change the habitat ID.

## Recommended Edits

1. In a later authorized curation session, add the exact guarded GOLD parent
   exclusion for `habitatmech:GOLD.6a5b013cc9` and retain all source context,
   the material genus, identity, CLOSE grounding and ITEM review status.
2. Resolve the upstream synonym conflict with claim-level evidence. Refresh
   ontology inputs through the extractor after an upstream correction, or
   design an explicit maintained synonym override if an interim local remedy
   is required. Do not globally rewrite all imported synonyms or use a
   decision row as if it already offered synonym-specific control.
3. Preserve the source's two collapsed node IDs and zero-count semantics;
   append honest curation history only when a scientific input actually changes.

## Follow-up Checks

Verify any revised ENVO assertion at an immutable revision and inspect its
synonym predicate, not just a lexical lookup. Add a differential regression
showing only the intended parent and/or synonym changes, with source path,
mint, counts, identity, other synonyms and true parent retained. Dry seed,
inspect the target canary, validate history and strict schema, reproduce the
full corpus, regenerate affected products and run full QC/OAK. OAK alone
cannot establish that the two semantic findings were fixed.

## Additional Notes

Only this new report was written; no record, maintained scientific input,
generated site, curation event or GitHub item changed. No paid research.
Initial source-file lookup used the nonexistent name `ontology_parents.tsv`;
the ignored-inclusive file inventory identified the actual
`ontology_subclass_edges.tsv`, which was then inspected. Current Alberta
overview access failed; only the successfully opened historical government
pages and primary abstract support the external claims above. Search snippets
and inaccessible source text were not used as evidence.
