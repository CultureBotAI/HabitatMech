# YAML Record Review: Anaerobic digestor

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/anaerobic_digestor__8332e1c2.yaml`
- Started UTC: 2026-10-07T03:09:35Z
- Finished UTC: 2026-10-07T03:10:59Z
- Verdict: needs curation (0 blocker, 1 major, 0 minor)

## Target

Read the entire generated HabitatRecord and rendered minted-ID page.
The exact target is `habitatmech:GOLD.ed87e682a9`, Anaerobic digestor,
ENGINEERED / UNGROUNDED / SEEDED. It is the GOLD Wastewater-path concept,
not the same-label BacDive record or the GOLD WWTP-path Anaerobic digester.
One source attestation, one parent, one ORGANISM assertion and two events;
no definition, synonyms, xrefs, taxa, parameters, literature evidence, causal
graphs, discussions or datasets.

## Validation

- `UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/anaerobic_digestor__8332e1c2.yaml`: passed, no issues.
- `UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/anaerobic_digestor__8332e1c2.yaml`: passed, one file, zero errors.
- Read-only Python `build_corpus()` / `build_document()` comparison reproduces
  every field: one source, zero reviewed sources, no taxa and two history events.
  This supplemental check is distinct from the documented full-corpus gate.
- Full QC and OAK were not rerun for this report. Scientific inputs and
  products are unchanged from `ec95a7191a9b6c9ddaa404c2062f7be9932623a9`.
  A fresh session query verified [the exact-baseline QC run](https://github.com/CultureBotAI/HabitatMech/actions/runs/37562477062)
  completed successfully at that SHA. Its full-corpus, reference, history and
  generated-product checks are reused. Material ontology terms were freshly
  verified from official typed ENVO below.
- Original numbered GOLD nodes and the one organism edge could not be
  re-extracted from source dumps; no live source-node crosswalk is claimed.

## Identity and Grounding

`data/raw/gold_ecosystem_paths.tsv:914` contains the exact depth-three path
`Engineered > Wastewater > Anaerobic digestor`, with nodes
`gold.ecosystem:3510|gold.ecosystem:3840|gold.ecosystem:4271`. It records three
nodes, one organism, zero studies and zero biosamples in that inventory.
The recomputed full-path mint matches the record. The suffix in the filename
is a legacy disambiguator, not the current ID: `data/habitats/PATHS.tsv:3052`
explicitly pins it, so there is no filename-identity defect.

Actual resolution is `gold_unmatched`, preserved by the CLASS
CONFIRM_UNGROUNDED row at `curation/decisions.tsv:1309`. Zero ITEM-reviewed
sources correctly produce SEEDED. The emitted first source ID, three-node
note and one ORGANISM count match; a source-equals-minted-record attestation
needs no ontology mapping predicate. A reactor used for anaerobic digestion
is a physical microbial habitat, not the digestion process. Lack of an exact
term does not justify grounding it to sludge, wastewater or the whole plant.

The immediate `Engineered > Wastewater` path resolves through the mapping
table and an ITEM REVIEW to `ENVO:00002001`. That explains the emitted parent,
but it does not establish that the digestor is itself waste water.

## Evidence

Fresh official ENVO OWL at revision
`a2455d1a77e46bb8a664d65a157166b539269042` confirms active
`ENVO:00002001`, label waste water, defined as water adversely affected by
anthropogenic influence. Its two named parents are ENVO:00002186 and
ENVO:00002264. The local definition and edges agree at
`data/raw/ontology_terms.tsv:7166` and
`data/raw/ontology_subclass_edges.tsv:5263`. ENVO also distinguishes the
active bioreactor containment-unit class `ENVO:00002123` from this water
material and from `ENVO:00002043` wastewater treatment plant.

[EPA's archived industrial wastewater definitions](https://www3.epa.gov/ghgreporting/help/tool2014/userarchiveversion/definitions/industrial-wastewater.html)
were opened and read: the reactor and sludge digester are vessels, distinct
from the wastewater or sludge undergoing treatment. This source supports the
entity-type distinction, not a claim about current legal requirements, a
specific GOLD specimen, or equivalence of all digester designs.
[EPA's biological account](https://www.epa.gov/agstar/how-does-anaerobic-digestion-work),
also opened earlier in this session, describes microbial communities in the
reactor and separately identifies residual digestate.

An exact-field/pipe-member scan of all 14 raw TSVs found target evidence only
in the GOLD ecosystem, biosample and study inventories. The separate bulk
row `gold_path_biosamples.tsv:128` records 231 biosamples for path ID 4271;
18 rows in `gold_studies.tsv` contain this path. Two of those study rows also
contain other paths. `data/raw/GOLD_MANIFEST.yaml` identifies those bulk
outputs separately from the organism inventory. They must not be summed,
substituted for one ORGANISM, or treated as 231 independently verified samples
of a uniform operating regime. Study-page details and sample membership were
not individually verified; those accessions are not asserted in the record.
No exact-path triad or environmental-parameter row was found.

## Completeness

Ignored-inclusive ID, label, slug, source-ID and full-path searches covered
curation, history, configuration, documentation, tests, research, the research
manifest, PATHS and RETIRED. Ignored-inclusive filename searches additionally
covered curation/history/research. No target-owned definition, parent
exclusion, causal overlay or research report was found within those bounds.
The default resolver and the ontology inventory provide no exact digestor
identity; this is not a claim that no suitable term exists in any ontology.

The missing optional fields are not independent defects. Do not turn one
organism assertion into a guessed taxon, infer temperature or feedstock from
the word anaerobic, or create boilerplate discussions. iModulonDB is not
applicable because no gene, regulator or expression dataset is named.

The same session's ignored-inclusive filename search across `build` and the
configured kg-microbe data directory found no GOLD node/edge dumps. Source
re-extraction therefore remains unavailable. Spelling similarity with other
records is a future identity-comparison lead, not proof of a duplicate.

## Findings

1. **Major: the reactor is incorrectly modeled as a kind of waste water.**
   `parent_habitats: [ENVO:00002001]` promotes the immediate GOLD source
   context into an is-a relationship. A microbial containment unit is not the
   water material it treats. The edge originates in
   `src/habitatmech/seed.py:910`, not independent ontology or definition
   evidence. This violates `docs/CURATION.md:26`. Maintained owner:
   `curation/gold_parent_exclusions.tsv`.

No blocker or minor finding was established. The supported source identity,
count and workflow provenance can remain unchanged while this edge is fixed.

## Recommended Edits

In a separately authorized curation, add one evidence-backed exclusion for
`habitatmech:GOLD.ed87e682a9`, exact path
`Engineered > Wastewater > Anaerobic digestor`, expected parent
`ENVO:00002001`. Preserve all source nodes and counts, the full path, pinned
filename, minted identity, ENGINEERED category, UNGROUNDED/SEEDED status and
original decision history. Add append-only session history and regenerate;
let the seeder add the deterministic exclusion event.

Do not rename or merge this record based on the digestor/digester spelling,
replace its identity with a related material, invent a definition merely to
remove the edge, or patch generated YAML/pages. A supported bioreactor genus
and a comparison with the WWTP or BacDive source concepts would be separate
ITEM curation decisions, not prerequisites for removing this false parent.

## Follow-up Checks

Add a focused regression in `tests/test_gold_parent_exclusions.py` that
removes only this immediate GOLD parent and adds its event, preserving all
unrelated fields and the SEEDED status. Run `just seed`, inspect
`just seed-canary habitatmech:GOLD.ed87e682a9 --force`, then authorized full
regeneration, target strict validation, `just verify-corpus`, history/site
checks and `just qc`. Any later new grounding additionally requires
`just validate-products`. Recover governed source dumps before claiming
organism-edge or bulk sample-level verification.

## Additional Notes

Only this new review report was written. No scientific data, generated page,
mapping status, curation history or GitHub item was modified. No paid research
or SSSOM/KGX readiness assessment was performed. The complete-corpus review
goal remains unfinished.
