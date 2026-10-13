# YAML Record Review: chelicerate-associated environment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/host_associated/arthropoda_chelicerates.yaml`
- Started UTC: 2026-10-04T05:22:28Z
- Finished UTC: 2026-10-04T05:29:36Z
- Verdict: pass with minor issues

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.44a2cbbd60`:
HOST_ASSOCIATED, UNGROUNDED, REVIEWED. It has a curated definition, one
source-label synonym, two broader environment parents, one taxonomic xref,
one GOLD attestation with 169 ORGANISM assertions and three generated events.
The actual `mint` helper reproduces the key from Host-associated > Arthropoda:
Chelicerates; `data/habitats/PATHS.tsv:1805` pins its original source-label slug.

## Validation

- `just validate data/habitats/host_associated/arthropoda_chelicerates.yaml`:
  passed, no issues.
- `just validate-strict data/habitats/host_associated/arthropoda_chelicerates.yaml`:
  one file, zero errors.
- Fresh batch `just validate-products`: passed; 1,179 canonical pairs,
  one synonym, five configured exceptions and 2,054 no-adapter skips.
- Fresh batch `just qc` passed lint, documentation and raw provenance and
  remains in tests. No terminal local QC result is claimed here. Baseline
  [QC 37179294525](https://github.com/CultureBotAI/HabitatMech/actions/runs/37179294525)
  passed; the target has not changed from that baseline.
- Current official OLS term JSON and NCBI taxonomy content were inspected.
  Browser access to the OLS API failed; direct JSON retrieval succeeded.

## Identity and Grounding

`curation/decisions.tsv:1625` is ITEM CONFIRM_UNGROUNDED with relation xref.
`curation/term_requests.tsv:35` supplies the label, definition, source-label
synonym and ADD-mode animal-associated genus. REVIEWED reflects the single
source's ITEM depth. August 16 decision/seed and August 22 definition events
match those inputs. Minted environment identity is not the host taxon itself.

Vendored rows 8495/8497 and current non-obsolete
[ENVO:01001000](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001000)
and [ENVO:01001002](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001002)
agree on labels and definitions. The subclass inventory at row 6797 places
animal-associated environment beneath organism-determined environment.
Both are genuinely broader; retaining the inherited ancestor with ADD is
consistent with local rules. Complete parent-record reads confirm their
identities; their own counts, taxa and parameters are not inherited here.

Current [NCBI Chelicerata](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=6843)
places the clade within Arthropoda and includes arachnids, horseshoe crabs and
sea spiders. Current OLS verifies non-obsolete NCBITaxon:6656 Arthropoda and
NCBITaxon:6843 Chelicerata. The latter is not in the fully searched vendored
slice; the former is present at row 10760. The maintained definition notes
already state that Arthropoda is deliberately a broader taxonomic reference,
not this environment's identity. A more precise taxon reference is optional
future enrichment, not grounds for discarding the host habitat.

The current ENVO search for chelicerate associated environment returned zero
results; ignored-inclusive local searches found no matching class. This is a
bounded query/slice result, not proof that all possible ontology terminology
has been exhausted. The verified active cnidarian-associated term
[ENVO:01001179](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001179)
provides the organism-or-part definitional pattern, not a substitute identity.

## Evidence

`data/raw/gold_ecosystem_paths.tsv:136` supplies four nodes (7150, 7190,
7191, 7192), 169 organisms and zero study/biosample assertions. First-node
attestation, four-node note, full path, count and ORGANISM unit are faithful.
The 244-organism Whole body child and the environmental nest/web paths remain
separate records and are not added to the target count.

Complete structured scans covered 2,562 tree paths, 1,040 bulk-count rows,
4,587 studies and 1,587 triads. Chelicerate wording returned six tree paths,
two bulk rows, 15 studies and three triads. The side-table hits belong to
Whole body or ISE6, not the exact clade node. In particular, ISE6 now has one
bulk biosample despite zero tree assertions; the older research report's
zero-assertion statement must not be generalized across products. No child
sample, study or anatomical triad term is promoted to this target's identity.

The committed definition-research report was used as a lead, not independent
evidence for its wider numerical or mechanistic claims. Inspected primary
[Vanthournout and Hendrickx 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0117297)
publisher text verifies DOI:10.1371/journal.pone.0117297 and whole-individual
DNA sampling of Oedothorax gibbosus in a bacterial-community study. That is a
bounded example of a chelicerate hosting microbes, not evidence of a universal
community, a causal mechanism or the composition of GOLD's 169 assertions.
No paper taxa or prevalence numbers are copied into the record.

## Completeness

Ignored-inclusive key/label/stem searches covered curation, history, research,
prior reviews, raw inventories, PATHS and RETIRED. They found the maintained
decision/definition, generated ENVO template, research report and existing
label-change redirect, but no exact-target review, causal overlay or session
history. Older curation does not retroactively require a new session merely
for this read-only audit. The existing redirect at RETIRED row 26 preserves
the older source-label URL; no new rename is proposed.

Full structured scans of the other eight source tables (162 BacDive sources,
3,081 BacDive taxa, 770 parameters, 358 mappings, 58 Madin habitats, 1,378
Madin taxa, 719 PREGO habitats and 8,807 PREGO taxa) found no chelicerate-word
or target-key match. This does not rule out evidence under individual host
names. Optional taxa, parameters, graphs and datasets need not be populated.
iModulonDB is not applicable: the record makes no gene or expression claim.

## Findings

1. **Minor - HM-CHELICERATE-001:** `HabitatRecord.xrefs` is described in
   `src/habitatmech/schema/habitatmech.yaml:163-169` as equivalence-only,
   contradicting the implemented and documented non-identity xref policy.
   This target exposes the mismatch through its explicitly broader taxon
   reference. The scientific record follows the policy; the schema prose
   needs correction. Tracked in [#1351](https://github.com/CultureBotAI/HabitatMech/issues/1351).

No blocker or major finding established. No biological identity, definition,
source-count, hierarchy or evidence change is recommended for this target.

## Recommended Edits

Clarify the schema slot description: related context is allowed and an xref
alone asserts neither equivalence nor is-a. Preserve field type, constraints,
curation placement behavior and all scientific records. Append schema-edit
history. Do not replace this environment with Arthropoda, Chelicerata, a
single subgroup, whole body or an aquatic-only environment.

## Follow-up Checks

Run the existing xref-placement tests in `tests/test_decisions.py:625-672`,
schema/history validation and full QC. Verify unchanged scientific output,
corpus reproduction and map/site freshness. External ENVO submission remains
subject to explicit per-request approval; this review does not authorize one.

## Additional Notes

All 501 existing issue bodies and returned comments were searched. Closed
#99 introduced contextual xrefs; closed #169 corrected decision/seeder
comments, not this schema description, so #1351 is a distinct bounded repair.
No target record, decision, definition, status or history was changed by this
review. Parent/reference reads do not add review coverage. No paid research ran.
