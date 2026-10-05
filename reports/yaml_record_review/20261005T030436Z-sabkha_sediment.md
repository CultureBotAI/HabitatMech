# YAML Record Review: Sabkha Sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/sabkha_sediment.yaml`
- Started UTC: 2026-10-05T03:02:49Z
- Finished UTC: 2026-10-05T03:04:36Z
- Verdict: needs curation

## Target

Entire generated HabitatRecord habitatmech:GOLD.b3725fa211, Sabkha sediment,
AQUATIC/UNGROUNDED/SEEDED: one parent, one uncounted GOLD attestation and
two history events. Definition, synonyms, xrefs, parameters, taxa, evidence,
graphs, discussions and datasets are absent. PATHS.tsv:2603 pins the filename.

The exact source is Environmental > Aquatic > Marine > Supratidal zone >
Sabkha sediment, node 8050. It denotes source-qualified sediment material,
not the whole sabkha flat, its water, a marine zone or every use of the word
sabkha in inland salt-lake literature.

## Validation

| Check | Observed result |
| --- | --- |
| `just validate data/habitats/aquatic/sabkha_sediment.yaml` | PASS, no issues. |
| `just validate-strict data/habitats/aquatic/sabkha_sediment.yaml` | PASS, one file, zero errors. |
| `just validate-products` | Shared fresh PASS: 1,179 canonical, one synonym, five exceptions; 2,054 configured no-adapter skips. |
| `just worklist --status all --limit 5` | Shared PASS: 953 ungrounded records, 1,810 decisions. |
| `just qc` | Fresh authorized run active in tests; lint, documentation and raw provenance passed. No terminal whole-run result claimed at review finish. |
| Source/reference checks | Complete generated-document equality, executed source and parent routes, all 14 raw inventories, typed ENVO/current OLS, current GOLD attempt and complete rendered page. |

The full dictionary reproduces with one source concept and zero ITEM-reviewed
sources. The complete marine supra-littoral parent and current typed definition
were read during the preceding individual review and used here only as
context. Previous PR #1440 main-push QC 37256991482 is separately terminal
SUCCESS, not substituted for the fresh local run.

## Identity and Grounding

Minting reproduces the retained source identifier. The actual default
gold_unmatched resolution is retained by CLASS CONFIRM_UNGROUNDED at
curation/decisions.tsv:1014. Its 2026-08-12 event explicitly says habitat
identity was not assessed; the 2026-08-16 event records seeding. The honest
SEEDED status should not be promoted merely by this read-only review.

The sole parent is active
[ENVO:01000124 marine supra-littoral zone](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000124),
an above-high-tide marine area with specific splash/submergence conditions.
Its source key habitatmech:GOLD.600724f138 resolves through
gold_leaf_synonym/CLOSE, endorsed by ITEM REVIEW at decisions.tsv:1734.
seed.py:898-907 turns that immediate GOLD path context into strict
parent_habitats. A material situated in that zone is not a kind of zone.
The target has no actual material-genus parent to balance that type error.

Active [ENVO:00002007 sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002007),
also at ontology_terms.tsv:7170, is the existing generic material genus:
particles deposited following transport by flowing liquid. It is a broader
candidate, not an exact identity for this qualified source. An ITEM assessment
should retain that distinction and inspect deposition scope before authoring
a qualified definition.

Do not automatically choose
[ENVO:03000033 marine sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A03000033)
just because Marine appears in the path. Its textual definition describes
transport through the marine water column and settling on the seafloor;
the inspected OWL also contains adjacency/overlap restrictions and an
equivalent-class union. Those are not evidence that this unmeasured
supratidal source meets every intended scope condition. Keep the generic
sediment genus available while investigating any more specific choice.

The existing Sabkha record is a landform, not a material parent to substitute
blindly. Its PREGO strain association, synonym defect and review status do
not transfer here. This target has no synonym-scope or emitted-predicate
witness for #1249 or #1398. #1297 repairs a separate parent-zone edge and
would not repair sediment is-a zone.

## Evidence

Physical gold_ecosystem_paths.tsv:1556 gives one depth-five node and zeros for
organism, study and biosample counters. Count/unit omission is faithful; it
does not establish absence of microorganisms. All 14 raw inventories were
scanned for exact source path/node: only the tree row matched. No exact
bulk biosample, complete-triad, study, taxon, parameter, PREGO, BacDive or
Madin contribution was located. There is no mixed-path study to promote
into source-specific evidence.

Current official GOLD node 8050 returned 404. That is an access/resolution
limit, not proof of retirement. The label and provenance support a qualified
sediment concept, not a measured mineralogy, grain-size distribution, oxygen
state, salt concentration, temperature or microbial guild. Empty optional
fields are appropriate. In particular, a strain isolated from water at the
inland Ezzemoul site is not evidence for this marine sediment node.

The complete rendered page accurately shows UNGROUNDED/SEEDED, the CLASS
warning, source path and no positive count. It also displays the unsupported
marine-zone parent as a broader habitat. No gene, regulator or expression
claim makes iModulonDB applicable.

## Completeness

Ignored-inclusive exact-ID/node/path, label and filename searches covered
curation, conf, history, research, reports, all raw inventories, PATHS, RETIRED
and additional repository text. The CLASS decision, source row and text-map
copies were found. The preceding Sabkha report is sibling context, not an
earlier independent review of this material.

No target definition, external-xref row, causal overlay, dedicated research,
session-history file, retirement or prior individual report was located.
The missing material placement is part of the hierarchy finding below, not
an extra finding for every empty optional field. An authored definition needs
an ITEM identity assessment first; there is no reason to invent a duplicate
generic sediment term.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | Sabkha sediment is placed solely under its geographic marine-zone context as a strict superclass and lacks an appropriate sediment-material genus. | Exact-source parent control in src/habitatmech/seed.py:898-907; ITEM assessment at curation/decisions.tsv:1014 and, if justified, a qualified definition in curation/term_requests.tsv. |

Zero blockers, one major finding, zero minor. Suppressing the false zone edge
and supplying a defensible material genus are two parts of the same placement
repair; neither a generic exact merge nor replacing zone with whole sabkha
would solve it.

## Recommended Edits

1. ITEM-assess this exact qualified material and suppress its source-only
   supra-littoral parent. Preserve minted identity, full path, node, count
   omission and old history; do not globally remove valid zone subclasses.
2. Use the existing sediment genus with supported qualification. Keep an
   authored source-specific definition in `curation/term_requests.tsv` when
   justified. REPLACE is permissible only after establishing this sole
   inherited parent is false and documenting the replacement genus; a future
   valid inherited parent would require reconsidering that mode.
3. Do not attach the contextual Sabkha record's taxa, assign seafloor deposition
   from a marine label, or invent environmental parameters. Coordinate the
   parent's separate #1297 correction without treating it as this repair.

## Follow-up Checks

Dry seed and inspect `just seed-canary habitatmech:GOLD.b3725fa211 --force`.
Add exact-edge, sediment-genus, distinct-identity and genuine-zone controls;
verify count omission and ITEM-derived status/history. Append required
session history, use guarded regeneration, then ordinary/strict/products,
provenance/history, exact corpus reproduction, site and full QC.

Actual full-context parent removal changes semantic text; removing the
nonexistent predicate is neutral. The scientific hierarchy/definition repair
requires a genuine #1217 map/site refresh while preserving protected
#1218/runtime pins. SSSOM/KGX exports were not executed or certified here.

## Additional Notes

All-state exact-ID and Sabkha sediment issue searches returned no matching
repair. The inspected #1297 body concerns marine supra-littoral zone's own
whole-waterbody parent, not the present material assertion.
Typed official ENVO OWL SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
No scientific input, generated artifact, prior report/history, paid research
or GitHub item changed during this individual review.
