# YAML Record Review: Subtidal zone sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/subtidal_zone_sediment.yaml`
- Started UTC: 2026-10-06T15:17:25Z
- Finished UTC: 2026-10-06T15:19:09Z
- Verdict: needs curation; 0 blocker, 1 major, 0 minor findings.

## Target

The whole generated HabitatRecord was read. habitatmech:GOLD.785879d721 is
AQUATIC/UNGROUNDED/SEEDED, with one parent, one uncounted GOLD attestation
and two events. Its exact source is Environmental > Aquatic > Marine >
Neritic zone/Coastal water > Subtidal zone sediment. PATHS.tsv:2175 pins the
stem. This is not GOLD4647 Sediment below the generic marine Subtidal zone;
that distinct source's reef triad and counts must not be transferred here.
Baseline: 4157ac2b3935aa8a5ab6d018df5acc15fd5214b6.

## Validation

- `just validate data/habitats/aquatic/subtidal_zone_sediment.yaml`: pass.
- `just validate-strict data/habitats/aquatic/subtidal_zone_sediment.yaml`:
  pass, one file, zero errors.
- Actual full build_corpus/build_document equality: pass, one source, zero
  reviewed sources, zero taxa and two events. Actual child/parent routes and
  full-context semantic-text comparison were executed.
- Shared checks freshly run on the unchanged scientific baseline: exact
  `just verify-corpus --max-diffs 1` for 3,206 records; `just validate-history`
  for 95 records; `just validate-causal-all` for 32 graphs;
  `just term-requests-check` for 109 terms; `just provenance-check` for 14
  inventories/two GOLD sources; `just worklist --limit 3`; and `just report`:
  all pass. The corpus report completed after the preceding zone report
  closed, with 688 REVIEWED and 2,518 SEEDED records.
- Shared `just validate-products`: pass, 1,179 canonical, one synonym, five
  exceptions and 2,054 configured no-adapter skips. This does not assess is-a.
- `git diff --quiet -- curation data/raw src scripts data/habitats pages history README.md`:
  pass, proving baseline reuse covers unchanged scientific inputs/products.
- Full tests/QC and browser visual QA were not rerun for report-only work.
  No standalone reference validator is documented for this citation-free
  record. No reference-bearing optional slot is populated.

## Identity and Grounding

Actual minting gives GOLD.785879d721. The automatic route is gold_unmatched;
CLASS CONFIRM_UNGROUNDED at curation/decisions.tsv:715 retains the mint with
no mapping predicate or extra placement. SEEDED and both dated events agree.
Neither a class sweep nor this report is ITEM curation sign-off.

The immediate Neritic zone/Coastal water source, GOLD.89754b31f3, is also
automatically unmatched, but its maintained ITEM GROUND/CLOSE decision resolves
it to ENVO:00002150. The independent GOLD path-parent pass then attaches that
term to the sediment. The complete coastal_sea_water.yaml was read for context;
its taxa, counts and REVIEWED status are not child evidence.

Vendored rows 7246, 9589 and 7170 and the current typed official
[ENVO ontology](https://raw.githubusercontent.com/EnvironmentOntology/envo/a2455d1a77e46bb8a664d65a157166b539269042/envo.owl)
distinguish coastal sea water, marine sediment and sediment. All three are
active OWL classes. Sediment deposited in a marine setting is not a kind of
seawater. Marine sediment is a defensible material-genus candidate; it is
not an exact identity for this subtidal/coastal-qualified source class.

Fresh exact=true ENVO searches for subtidal zone sediment, subtidal sediment
and marine subtidal sediment each returned zero. Ignored-inclusive compound
searches found no such exact term in the vendored slice. These are bounded
searches, not proof that no ontology could represent the concept.

## Evidence

Structured exact full-path, minted-ID and node searches covered all 14 raw
TSVs. gold_ecosystem_paths.tsv:1541 gives depth five, node gold.ecosystem:7948,
one node and zero organism/study/biosample/total KGX counters. The attestation
faithfully retains node, label and path; omission of count/unit follows the
zero-organism emission rule and does not assert biological absence.

The separate bulk inventory gold_path_biosamples.tsv:287 gives 74 biosamples
for exact path ID 7948. gold_studies.tsv has the following exact memberships:

| Physical row | Study | Distinct paths |
| --- | --- | --- |
| 4339 | Gs0159326 | 1 |
| 4377 | Gs0160772 | 1 |
| 4463 | Gs0161499 | 1 |

No exact target membership was found in gold_path_triads.tsv or the other
source inventories. The three live GOLD study URLs were inaccessible through
the web tool, so study contents, current samples and taxon crosswalks remain
unverified. Seventy-four biosamples must not be emitted as 74 organisms or
treated as the sum of those three study rows. The manifests/checks establish
the committed snapshots, not complete current GOLD coverage.

[Probandt et al., Microbial life on a sand grain](https://www.nature.com/articles/ismej2017197),
DOI:10.1038/ismej.2017.197, PMID:29192905, was inspected in publisher metadata,
abstract, sampling and amplification methods; PubMed metadata was also opened.
The study sampled subtidal Helgoland Roads sediment and examined bulk material
and individual grains with sequencing and microscopy. It supports a bounded
microbial sediment habitat, not universal sand composition, a fixed depth,
photic conditions, taxa or mechanisms across this source bin. No link to any
of the three GOLD studies was established. The initial PMC retrieval returned
a browser challenge; the publisher supplied the inspected text instead.

The complete generated HTML accurately presents the path and uncounted
attestation, but calls coastal sea water a broader habitat. Actual semantic
text repeats that parent. An in-memory replacement with the verified marine
sediment genus changes semantic text; no generated product was changed.

## Completeness

Ignored/hidden-inclusive ID, label and stem searches covered curation,
history, research, reports, conf, docs, tests, src, PATHS and RETIRED; compound
searches additionally covered ontology terms, definitions, causal overlays
and the research manifest. No target-owned ITEM decision, definition, causal
overlay or guarded exclusion was found. Related sediment reports and seaweed
research are not source-owned support.

Optional parameters, taxa, evidence, datasets and mechanisms are correctly
unasserted. A missing authored definition alone is not a defect. iModulonDB
is not applicable because no organism, gene, regulator or expression dataset
is asserted. Access-limited study detail is a follow-up limitation, not evidence
against the habitat or a new finding.

## Findings

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| Major | Subtidal zone sediment is placed beneath coastal sea water, encoding material-in-context as material-is-a-water and omitting a supported sediment genus. | Exact source exclusion in curation/gold_parent_exclusions.tsv; ITEM broader placement in curation/decisions.tsv, or a justified definition in curation/term_requests.tsv. |

No blocker or minor finding was established. The wrong parent and missing
material placement form one coherent hierarchy correction. No source mapping
predicate is emitted, so retained-source predicate defects are not a present
finding for this record.

## Recommended Edits

1. Exclude only the exact GOLD.785879d721/path/ENVO:00002150 source-parent
   contribution with the maintained guarded table. Preserve the qualified
   mint, source node/path, stem/category and zero-count omission.
2. ITEM-assess marine sediment as a strictly broader genus. The existing
   CONFIRM_UNGROUNDED parent-placement route can retain unresolved exact
   identity while adding a verified genus without a source mapping predicate.
   Do not merge every subtidal sediment source or use a zone as a material
   superclass. Do not add a definition merely to suppress the wrong parent.
3. Preserve source snapshot/unit distinctions and obtain study-level evidence
   before adding any taxa, measurement, dataset assertion or causal graph.

## Follow-up Checks

Test the exact guarded exclusion, verified material placement, unchanged
source identity/count omissions and honest review/mapping status. Dry-seed,
inspect the exact forced canary, append required session provenance, then
run schema/strict, labels, provenance, curation-floor, history, reproduction,
site and full QC. A changed genus requires a genuine semantic-map rebuild
and rendered-site refresh. Do not hand-edit generated YAML or map checksums.

## Additional Notes

The same-day typed ontology check parsed 106,817 triples at the pinned commit
above; it was reused for this record's explicitly named terms. The literature
check is independent habitat evidence, not a GOLD identity crosswalk or a
full systematic review. No scientific inputs, audit history, mapping status,
GitHub objects or paid research were modified. SSSOM/KGX compatibility is not
certified by these checks.
