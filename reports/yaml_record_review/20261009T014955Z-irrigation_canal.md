# YAML Record Review: irrigation canal

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/irrigation_canal.yaml`
- Started UTC: 2026-10-09T01:47:14Z
- Finished UTC: 2026-10-09T01:49:55Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the entire generated HabitatRecord ENVO:00000036 at baseline
`49d86f3aa09e165a94c37af1f0a683f7be469eaf`: ENGINEERED / EXACT / SEEDED,
with one ENVO definition, one synonym, one parent, one GOLD attestation and
one seed event. This resumes preliminary work interrupted by publication,
with fresh current-state checks. The complete generic Canal parent was read
for context, not counted as another completed review. Neither its freshwater
namesake nor the Sediment descendant is this target.

## Validation

Fresh commands used `UV_CACHE_DIR=build/uv-cache`:

- `just validate data/habitats/engineered/irrigation_canal.yaml`: no issues.
- `just validate-strict data/habitats/engineered/irrigation_canal.yaml`:
  one file, zero errors.
- `just verify-corpus`: 3,208 expected/present, zero missing/extra/differing.
- `just validate-history`: 208 valid records.
- `just provenance-check`: 14 inventories and two GOLD sources current.

Full-index `build_corpus()` and `build_document()` reproduced every target
field: one source contributor, zero reviewed contributors, no authored
definition and no applied GOLD-parent exclusion. Full QC was not repeated
per read-only record: the immediately preceding local run and exact-baseline
[merge-queue QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37870446176)
passed all gates with 622 tests and three skips. Baseline
[label correspondence](https://github.com/CultureBotAI/HabitatMech/actions/runs/37870446171)
and [vendored sync](https://github.com/CultureBotAI/HabitatMech/actions/runs/37870446178)
also passed. These checks do not certify synonym scope. No scientific inputs
changed during this review. No SSSOM/KGX readiness audit was performed.

## Identity and Grounding

`PATHS.tsv:449` and the recomputed source mint
`habitatmech:GOLD.74ffec33ba` agree with the exact source path. Resolution with
complete mapping and claimant indexes is `gold_leaf_label` before and after
decision application: ENVO:00000036 / EXACT / skos:exactMatch, reviewed=False.
No ITEM decision is inferred from the spelling match or the parent's status.
Canonical identity and irrigation qualification agree with the inspected
ontology class; SEEDED correctly distinguishes automatic mapping from review.

Complete class elements from the [pinned primary ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
confirm the active label, definition and named superclass ENVO:00000014.
Primary ENVO explicitly marks `canal` as `hasBroadSynonym`, not exact.
The parent's comment also distinguishes the water contained in a canal from
the channel structure itself. Do not silently reinterpret this target as
dry lining or construction, or collapse irrigation-qualified identity into
generic canal because the emitted synonym misleadingly suggests equivalence.

ENVO:00000014 is independently supplied by the ontology subclass edge and
GOLD's immediate Canal path. That parent source mint is GOLD.258a8a071f:
default `gold_leaf_label`, then ITEM `curated_review_of_gold_leaf_label`.
The independent sources agree on the direct genus. The parent's own upper
hierarchy, PREGO aliases and taxa are not additional target assertions.

## Evidence

- `gold_ecosystem_paths.tsv:1247` contains the exact depth-four path and
  single node 5110, with zero organism/study/biosample/total assertions.
  Generated source ID, label/path, predicate and count/unit omissions agree.
  No multi-node collapse note is needed for a one-node source.
- `ontology_terms.tsv:6632` contains the untyped alias `canal`, while
  `ontology_subclass_edges.tsv:4665` supplies the true Canal genus.
  The edge at line 5168 is an underground-irrigation-canal child edge,
  not an additional parent of the target.
- The exact-field/pipe-member scan of all 14 raw TSVs found no direct target
  biosample, study, taxon or parameter row. It did find the target ID in a
  local-scale triad for the separate Sediment child. Context annotation is
  not a target sample assertion.
- That child's node 5111 has 66 bulk BIOSAMPLEs at
  `gold_path_biosamples.tsv:305` and one study Gs0145339 at
  `gold_studies.tsv:2965`. Its triads at lines 62-64 cover one sample and one
  study, with broad ENVO:01000219 anthropogenic terrestrial biome, local
  ENVO:00000036 irrigation canal, and medium ENVO:00002007 sediment.
  The three relevant class elements were inspected. These different units
  and coverages must not be summed or transferred to the parent watercourse.
- A fresh [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  read, with worksheet dimensions reset, finds `site data` row 175:
  node 5111 and the full Sediment-child path. It corroborates the branch,
  not a current direct node-5110 row, retirement of that node, or its counts.
  The 84,174-byte response SHA256 is
  `3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396`.
- The cached immutable ENVO source was reparsed and hash-checked:
  `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  An additional OLS API browser attempt was inaccessible; no OLS result was
  substituted for the successfully inspected primary OWL.

## Completeness

Xrefs, parameters, taxa, evidence objects, causal graphs, discussions and
datasets are empty. No such field should be filled from the Canal parent's
three ORGANISM and three TAXON assertions or the sediment child's samples.
iModulonDB is not applicable to the claims present. Original sample members
were not reconstructed; that is not needed to establish the typed-alias defect.

Ignored-inclusive ID, source mint, label/stem and path searches covered
curation, history, research, configuration, all raw inventories, PATHS/RETIRED
and individual reports. They found source rows and contextual mentions but
no target-owned decision, definition, parent exclusion, causal overlay,
session history, dossier or previous individual target review in those bounds.
The earlier freshwater Canal report is a different record, not completed
coverage or primary evidence for this one.

## Findings

1. **Major: a broader ontology alias is emitted as exact equivalence.**
   `synonyms[0]` makes generic canal an EXACT_SYNONYM of irrigation canal,
   contrary to primary ENVO's explicit `hasBroadSynonym`. This loses the
   irrigation restriction and is a witness of the existing open
   [issue #1249](https://github.com/CultureBotAI/HabitatMech/issues/1249),
   whose current state was read without modification. Maintained ownership
   is typed ontology acquisition/extraction (`src/habitatmech/extract.py`,
   `_load_tsv_ontology`), inventory representation and the unconditional
   EXACT_SYNONYM emission in `ConceptStore.get` at `seed.py:424`.

Zero blockers and zero minor findings. No parentage or count defect was
established. The inherited definition grammar is not a second identity error.

## Recommended Edits

In a separately authorized repair, preserve typed primary synonym relations
through the governed ontology input and seeder, emitting this alias as
BROAD_SYNONYM. The schema already supports that enum. A flat KGX synonym
string cannot recover its original scope by itself; acquire the typed source
and retain provenance rather than guessing from lexical overlap or changing
all aliases to a single fallback type. Coordinate with #1249 and audit lexical
grounding consumers as well as display emission.

Preserve ENVO:00000036, the canonical label/definition, independent Canal
genus, node 5110 and full source path. Do not manually patch generated YAML,
promote SEEDED status or add an unsupported ITEM identity endorsement. Any
upstream correction of the inherited definition grammar is separate from
the demonstrated synonym-scope repair.

## Follow-up Checks

Add a typed-synonym regression for this exact source class and compare the
full corpus for identity, mapping and alias consequences of the shared fix.
Regenerate governed inventories with provenance receipts, dry-seed, inspect
the target canary, append session history and run strict, history/provenance,
label, corpus/site and full QC. Check semantic-input hashes and perform a
real map rebuild if selected text changes. The genus and child-source
separation must survive the repair.

## Additional Notes

Only this new report was authored; no scientific inputs, products, history,
statuses or GitHub items changed. Workbook style warnings did not prevent
complete row inspection. The all-table scan handled surplus CSV cells rather
than failing on an unrelated biosample overflow row. Exact baseline technical
validation is reused only for unchanged files, not as scientific proof.
