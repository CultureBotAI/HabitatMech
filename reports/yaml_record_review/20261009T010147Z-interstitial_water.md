# YAML Record Review: interstitial water

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/interstitial_water.yaml`
- Started UTC: 2026-10-09T00:58:39Z
- Finished UTC: 2026-10-09T01:01:47Z
- Verdict: needs curation (0 blocker, 1 major, 1 minor)

## Target

Read the entire generated HabitatRecord ENVO:03600009 at baseline
`b8a0a7bd659e3bb8e4aa9c9ce08d56ced830f66d`: ENGINEERED / EXACT / SEEDED,
with an ENVO definition, two parents, one collapsed GOLD attestation and one
seed event. The source is specifically `Engineered > Bioreactor > Sulphur
Autotrophic Denitrification > Interstitial water`, not the distinct groundwater-
qualified Porewater record. The entire native Sulphur Autotrophic
Denitrification parent was read for context, not counted as another review.

## Validation

- Fresh `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/interstitial_water.yaml`:
  no issues.
- Fresh strict validation with the same cache setting: one file, zero errors.
- Full-index in-memory construction and `build_document()` matched all target
  fields: one contributor, zero reviewed contributors, no applied decision,
  authored definition or GOLD-parent exclusion.
- Shared checks freshly completed during this unchanged report-only session
  passed: `just verify-corpus` (3,208 expected/present, zero differences),
  `just validate-history` (207 valid), and `just provenance-check`
  (14 inventories and two GOLD sources current).
- Full QC was not rerun per record. The immediately preceding baseline run
  passed all gates with 621 tests and three skips. Its native queue
  [QC](https://github.com/CultureBotAI/HabitatMech/actions/runs/37865912182)
  and [label check](https://github.com/CultureBotAI/HabitatMech/actions/runs/37865912102)
  passed on this exact commit. Canonical-label agreement does not prove that
  the qualified source has the ontology definition's scope or that a
  source-context parent is a valid strict superclass.

No SSSOM/KGX compatibility audit or original sample-member reconstruction was
performed. The record has no taxon, literature, causal or external-xref
assertion needing a separate claim-level reference validator.

## Identity and Grounding

`PATHS.tsv:929` pins ENVO:03600009 to this file. The actual GOLD source mint
is `habitatmech:GOLD.b099e463e2`. Complete mapping and claimant indexes give
`gold_leaf_label`, ENVO:03600009 / EXACT / skos:exactMatch, reviewed=False,
before and after decision application. SEEDED faithfully represents an
automatic label match, not an ITEM-approved source identity.

The inspected [pinned ENVO OWL](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
confirms the active label and definition: naturally occurring liquid water
in rock and sediment pores. Its direct named superclass is ENVO:00002006,
liquid water. Vendored `ontology_terms.tsv:10058` and
`ontology_subclass_edges.tsv:8453` agree. The record has no synonym whose
scope needs correction; the liquid-water parent's broad alias is not emitted
as an alias of this target.

The independent liquid-water parent is sound. The other parent,
`habitatmech:GOLD.f07ee97491`, comes solely from GOLD's immediate Sulphur
Autotrophic Denitrification path. That source defaults to `gold_unmatched`;
its CLASS CONFIRM_UNGROUNDED at `curation/decisions.tsv:1333` preserves native
identity and SEEDED status. Its own parent is ENVO:00002123 bioreactor, which
primary ENVO defines as a containment unit supporting organisms' activities.
Neither a denitrification process nor a reactor configuration is a strictly
broader kind of the generic natural pore-water material. This conclusion
does not require deciding the parent's unresolved identity or changing its
status to NOT_APPLICABLE.

## Evidence

- `gold_ecosystem_paths.tsv:1219` records the exact depth-four path, nodes
  5661/5662 and zero direct organism/study/biosample/total assertions. The
  generated first ID, two-node note, full path and count/unit omissions agree.
- `gold_path_biosamples.tsv:870` separately records two BIOSAMPLEs for node
  5662. The parent has its own two-sample row at line 869; these are not
  four target samples and must not be treated as organism assertions.
- `gold_studies.tsv:2607` links Gs0144746 to three paths: Bioreactor, Sulphur
  Autotrophic Denitrification, and this exact child. They are one study's
  memberships, not independent evidence or transferable taxa. Opening the
  [GOLD study](https://gold.jgi.doe.gov/study?id=Gs0144746) failed; a direct
  retrieval returned HTTP 403. No original sample IDs or descriptions were
  recovered from that page.
- Exact-field/pipe-member scanning of all 14 raw TSVs found the source,
  biosample, study, ontology-term and subclass rows above, but no direct
  target triad, taxon or physicochemical-parameter row. No medium annotation
  resolves the rock/sediment-versus-reactor-packing question.
- The current [GOLD workbook](https://gold.jgi.doe.gov/download?mode=ecosystempaths)
  confirms node 5662 at `site data` row 135 with a final Unclassified filler.
  Worksheet dimensions were reset before parsing. It corroborates the source
  classification, not historical node 5661 or the two samples' composition.
  The 84,174-byte workbook SHA256 is
  `f8e4cb5cf89ecc88d3cf28170cfc3a1cf47daed8218408a52914c53667dfd3d4`.
- The primary article [Burns et al. 2018, AEM.01250-18](https://journals.asm.org/doi/10.1128/aem.01250-18)
  was opened on the publisher site after the PMC endpoint returned a browser
  challenge. Its introduction and results distinguish water within sulfur-
  denitrification towers from sulfur/aragonite packing and from the equipment.
  The study uses recirculated artificial seawater and calls water inside the
  system interstitial. This is a real engineered usage that does not by
  itself establish natural occurrence within rock/sediment pores.
  The accessible article did not provide the queried GOLD ID; no crosswalk
  to Gs0144746 was established. It is terminology/scope evidence, not proof
  that these are GOLD's two samples. No article taxa, gene functions, aquarium
  location, salinity or operating measurements were imported into this record.
- Complete relevant ENVO class elements were parsed from the primary OWL,
  SHA256 `a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
  The older individual Porewater review was read as context only; its separate
  groundwater source and recommended genus do not establish this reactor
  source's exact identity.

## Completeness

Synonyms, xrefs, parameters, taxa, evidence objects, graphs, discussions and
datasets are empty. None should be filled from a plausible but unjoined
reactor paper, another path in the study, or the generic liquid-water record.
iModulonDB is not applicable to the assertions present in the target; the
adjacent paper's expression analyses do not create a target dataset claim.

Ignored-inclusive ontology/source IDs, label/stem, full source path and node
searches covered curation, history, research, configuration, raw inventories,
PATHS/RETIRED and individual reports. They found the parent CLASS decision and
contextual Porewater review but no target-owned decision, definition, parent
exclusion, overlay, history, dossier or earlier individual target review within
those bounds. Original sample metadata remain unrecovered, not proven absent.

## Findings

1. **Major: a reactor/process source context becomes a strict parent of
   generic interstitial-water material.** The GOLD prefix contributes
   `habitatmech:GOLD.f07ee97491` to `parent_habitats`. Primary ENVO identifies
   the target as liquid material, not a denitrification operation or its
   containment unit. The generic natural pore-water class is not universally
   a type of this engineered source context. The maintained owner is
   `curation/gold_parent_exclusions.tsv`, guarded by source mint
   GOLD.b099e463e2, exact path and expected parent GOLD.f07ee97491. Preserve
   the independently supported ENVO:00002006 parent.
2. **Minor: exact source-to-ontology scope lacks original-sample support.**
   The automatic spelling match does not establish that this reactor source
   satisfies the ontology's natural rock/sediment-pore restriction. The
   inspected engineered usage gives a concrete reason to investigate, but
   the unavailable original sample join prevents declaring that example the
   source's actual composition. This is not a second proven wrong identity
   or a reason to downgrade every seeded mapping mechanically.

Zero blockers. Missing optional fields and SEEDED status are not additional
findings. The major hierarchy defect stands independently of the minor
identity-scope uncertainty.

## Recommended Edits

Exclude only the false GOLD source-parent contribution using the guarded
table. Preserve the genuine liquid-water genus, nodes 5661/5662, source path,
count omissions and existing lifecycle; record the deterministic exclusion
event and append session history through maintained tools. Do not hand-edit
generated YAML or rewrite ENVO's definition to accommodate the source.

Separately recover the original samples and ITEM-review GOLD.b099e463e2 in
`curation/decisions.tsv`. If the source denotes engineered interstitial fluid
outside ENVO:03600009's scope, preserve its qualified native identity and
choose only an evidence-backed material genus; do not automatically use the
natural-pore-water term as a broader class. Any new definition belongs in
`curation/term_requests.tsv`. Check all references and redirects before a
split or retirement. This review does not establish a final replacement
identity, formulation, habitat-wide mechanism or source-member taxonomy.

## Follow-up Checks

Add an exact-source exclusion regression and a complete-corpus comparison
showing only target parent/audit changes for that bounded fix. Dry-seed,
inspect `just seed-canary ENVO:03600009`, and run strict, history/provenance,
corpus/site and full QC. An identity change additionally needs ontology-label,
source-equivalence, reference/redirect and downstream mapping checks. Compare
full semantic inputs and genuinely rebuild the map when they change. Preserve
all older review/history records and distinguish technical reproduction from
scientific support.

## Additional Notes

Only this new report was authored; scientific inputs, generated artifacts,
mapping status, history and GitHub state are unchanged. The direct GOLD probe
also found that BeautifulSoup is not installed; its upstream HTTP 403 already
prevented inspection, and no dependency was installed. A Europe PMC XML attempt
failed, but the publisher supplied the relevant primary text. Failed retrievals
are not evidence of sample absence, retirement or a completed accession join.
