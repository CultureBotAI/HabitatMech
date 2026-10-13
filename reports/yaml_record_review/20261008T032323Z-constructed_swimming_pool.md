# YAML Record Review: constructed swimming pool

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/constructed_swimming_pool.yaml`
- Started UTC: 2026-10-08T03:19:58Z
- Finished UTC: 2026-10-08T03:23:23Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `ENVO:01000965` at
`6ef2563f667a7af527721a1a29ff6f0189e6d1da`. It is ENGINEERED / CLOSE /
REVIEWED, with an ENVO definition, six scoped synonym entries, two parents,
one GOLD attestation and three history events. The source path is
`Engineered > Built environment > Swimming pool`; its source-concept mint is
`habitatmech:GOLD.38dc52b40a`, not the record's ontology identity. Count/unit,
parameters, taxa, literature evidence, graphs, discussions and datasets are
absent. The record denotes the constructed container, not its water or filter.

## Validation

- Fresh `UV_CACHE_DIR=build/uv-cache just validate` passed on the target.
- Fresh strict validation: one file, zero errors.
- Actual full-index `resolve_gold` takes `gold_leaf_synonym`, adopts
  ENVO:01000965 and emits CLOSE/skos:closeMatch. Applying the real ITEM REVIEW
  gives `curated_review_of_gold_leaf_synonym`, reviewed=True.
- Full read-only `build_corpus` / `build_document` equality passed: one source,
  one reviewed source and the expected decision. The mint differs from the
  record identifier because ontology grounding occurred; this is not an error.
  `PATHS.tsv:868` agrees.
- Exact-field/pipe-member scans of all 14 raw TSVs found one target row.
- Fresh OLS confirmed the active identity/definition and synonym spellings.
  Typed RDF/XML from the current ENVO Git revision independently checked
  original synonym predicates and the named ontology superclass.

Full checks reuse current-head PR #1683 CI: offline QC passed (552 tests,
three skips, all 3,207 records reproduced); vendored sync passed. Required
label correspondence failed on unchanged beverage/pastry FOODON identities
(#1690), not this ENVO term. No all-green or merge-queue baseline is claimed.
Full history/reference/corpus gates were not rerun per target, and label
agreement alone cannot verify synonym scope.

## Identity and Grounding

[ENVO:01000965](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000965)
is a human-built construction intended to contain recreational water. The
engineered source path supports that sense over a natural pool. ITEM REVIEW
at `curation/decisions.tsv:1704` explains the positional constructed qualifier.
CLOSE is preserved rather than upgraded from a lexical match. The mapping
compares the source to an explicit, distinct ontology record; this is not the
retained-mint endpoint mismatch in #1398.

Read both full parent records. ENVO:00000070 human construction is the named
ontology superclass (`ontology_subclass_edges.tsv:6760`) and is supported by
the definition and inspected RDF. The independent GOLD path pass contributes
mesh:D000076624. The [official MeSH scope note](https://meshb.nlm.nih.gov/record/ui?ui=D000076624)
includes human-made physical environmental elements and infrastructure;
the pool construction fits that scope. This is not the same whole-location
versus-local-surface error found for Concrete surface. No parent defect was
established in this target.

The GOLD label is correctly retained as RELATED_SYNONYM by the CLOSE-source
rule and its SOURCE_SYNONYM_SCOPED event. Independently supplied ENVO scope
must still be checked; the source-label correction does not validate the
ontology's flattened synonym pipe.

## Evidence

`gold_ecosystem_paths.tsv:1284` has depth three, one node 5594 and zero tree
counters. Omitted count/unit and absence of a collapsed-node note are correct.
The full exact-key raw scan found no target biosample, study, triad, parameter
or taxon row. Zero inventory counters do not imply a biologically empty pool.

The Sand filter descendant at :1285 is a different source. The industrial-
wastewater local triad at `gold_path_triads.tsv:156` happens to use this ENVO
term but is not a swimming-pool source observation. Neither supplies target
water chemistry, treatment practices or counts. The human-construction
parent's PREGO taxa likewise are not inherited into this pool record.

Fresh [GOLD5594](https://gold.jgi.doe.gov/ecosystem/5594) retrieval failed.
Bounded exact-node/category and NCBI BioSample searches recovered no verified
source crosswalk. Numeric collisions and a separate BacDive water-isolate
lead were not adopted. No microbial species, disinfection regime, health
claim, ownership type or universal temperature is asserted from those leads.

OLS's response lists spellings but returns no typed `obo_synonym` objects.
Therefore it was not used to infer exactness. Fresh GitHub metadata resolved
ENVO to `a2455d1a77e46bb8a664d65a157166b539269042` (2026-06-29), and the
[versioned RDF/XML](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
was streamed and structurally parsed. The one matching class element asserts:

- `pool`: hasBroadSynonym.
- `paddling pool`, `swimming bath`, `swimming pool`, `wading pool`:
  hasExactSynonym.

The target emits all five ENVO entries as EXACT_SYNONYM. Only the first
contradiction is demonstrated here; narrower colloquial readings are not a
reason to downgrade the four verified exact annotations.

## Completeness

Ignored-inclusive ID, source mint/node/path, stem, label and spelling searches
covered curation, history, conf, tests, docs, research, prior reports, raw
inventories and registries. No target-owned term request, overlay, exclusion,
research entry, retirement or prior individual report was found. The ITEM
decision exists. A mention in cooling-tower research is not target evidence.
Ignored-inclusive filename searches in build/ and configured kg-microbe data/
found no local typed ENVO OWL/OBO/JSON candidate; the versioned public source
was used instead. These bounds do not cover all machine caches.

Optional empty biology is not a defect. iModulonDB is inapplicable because the
target asserts no named gene, organism, regulator, pathway or expression
dataset. [Shared issue #1249](https://github.com/CultureBotAI/HabitatMech/issues/1249)
was read and verified OPEN; this record is a specific broad-synonym witness.

## Findings

Zero blockers, one major finding, zero minor findings.

1. **Major: the broad ontology synonym pool is promoted to exact.**
   `data/raw/ontology_terms.tsv:8460` has an untyped pipe. The inspected
   `_load_tsv_ontology` in `src/habitatmech/extract.py:771` copies that untyped
   field, and `ConceptStore.get` in `src/habitatmech/seed.py:390` unconditionally
   emits each ontology synonym as exact. The current typed ontology explicitly
   uses hasBroadSynonym for this spelling. Owners are the governed typed-source
   extraction/provenance contract and seeder, under existing #1249; generated
   YAML is not the repair surface.

## Recommended Edits

Preserve original typed synonym assertions through reproducible ontology
inputs, then emit `pool` as BROAD_SYNONYM for this target. The schema already
supports that enum. Retain the four verified exact ENVO synonyms and the
independent RELATED GOLD spelling; do not globally downgrade every synonym
or change identity simply to remove a lexical collision.

Keep the definition, two supported parents, explicit source-to-record
closeMatch, genuine ITEM-derived REVIEWED state, source node/path, count
omissions and history. Unknown upstream scope elsewhere needs an explicit
conservative policy, not an assumed exact assertion or checksum-only patch.

## Follow-up Checks

Regress this exact broad spelling alongside its four exact companions, the
GOLD related spelling, unknown scope and multiple typed scopes. Append required
history; refresh typed provenance inputs, dry-seed, inspect a forced canary
and regenerate. Run provenance, schema, labels, full reproduction and QC.
Check actual semantic-map inputs before deciding whether a scope-only change
needs refreshed embeddings; no semantic-text comparison was run here.
Resolve #1690 before claiming all required gates pass. No SSSOM/KGX execution
or current kg-microbe modeling certification was performed.

## Additional Notes

Only this new report was written. No scientific input, generated record/page,
history, lifecycle status or GitHub item changed; no paid research or delegation
was used. Parent-context reads are not additional completed record reviews.
