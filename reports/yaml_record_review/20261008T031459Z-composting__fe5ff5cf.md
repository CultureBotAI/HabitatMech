# YAML Record Review: Composting (Agricultural waste)

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/engineered/composting__fe5ff5cf.yaml`
- Started UTC: 2026-10-08T03:13:13Z
- Finished UTC: 2026-10-08T03:14:59Z
- Verdict: needs curation

## Target

Read the entire generated HabitatRecord `habitatmech:GOLD.e979bbb99c` at
`6ef2563f667a7af527721a1a29ff6f0189e6d1da`. Its exact source is
`Engineered > Solid waste > Agricultural waste > Composting`, not the
Sugarcane filter cake descendant or Agricultural wastewater path. It is
ENGINEERED / NARROW / SEEDED, with two ontology parents, one attestation,
17 ORGANISM assertions and one seed event. Definition, synonyms, xrefs,
parameters, named taxa, literature evidence, graphs, discussions and datasets
are absent from this record.

## Validation

- Fresh `UV_CACHE_DIR=build/uv-cache just validate` on the target passed.
- Fresh strict validation with the same cache: one file, zero errors.
- Actual default/applied resolution used full ontology, normalized mapping,
  leaf-claimant and composed-claimant indexes.
- Full read-only `build_corpus` / `build_document` equality passed: one source,
  zero reviewed sources, no applied decision and a matching source mint.
  `PATHS.tsv:3030` agrees.
- Exact-field/pipe-member scans of all 14 raw TSVs recovered four target rows.
- Fresh official OLS confirms active ENVO:01000371 agricultural waste material.
  The same-turn fresh ENVO:00002170 compost verification is reused.

Current-head PR #1683 supplies the reused full checks: offline QC passed
(552 tests, three skips, all 3,207 records reproduced); vendored sync passed.
The required label-correspondence job failed on unchanged beverage/pastry
FOODON identities, tracked in #1690. Therefore the full validation baseline is
not all green, although this target's ENVO terms were separately verified.
No merge-queue check is claimed. Full history/reference/corpus gates were not
rerun per target, and structural success does not establish scientific scope.

## Identity and Grounding

Mint, source label/path and engineered category reproduce faithfully. Both
`resolve_gold` and `apply_decision` take `gold_narrower_than_mapping_match`,
retain GOLD.e979bbb99c, emit NARROW/skos:narrowMatch, add ENVO:00002170 and
return reviewed=False/decision=None. The fallback mapping is
`data/raw/isolation_source_groundings.tsv:72`. The independent GOLD parent-
path pass adds ENVO:01000371.

Read the complete `agricultural_waste_material.yaml` parent and its historical
review, `reports/yaml_record_review/20260923T190909Z-agricultural_waste_material.md`.
The parent is a CLOSE / REVIEWED GOLD/PREGO merge, with its own two-organism
and five-taxon provenance. Its GOLD ITEM REVIEW at decisions.tsv:1740 and
PREGO BROAD replacement at :1817 do not review this child. Its pre-existing
Solid Waste parent finding is not a new completed parent review here.
The old report's recommendation to inspect this child is not evidence that
the child-to-parent relationship has been assessed.

[Current ENVO agricultural waste material](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01000371)
covers waste from agricultural operations, including more than plant residues
or solids; its returned description also cautions about waste-role modeling.
It remains active. [ENVO compost](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002170)
is aerobically derived material. Inference: agricultural origin alone does
not decide whether every sampled processing environment or transformed product
has both asserted material genera. The caveat is not an automatic deletion
rule, legal waste-status determination or NOT_APPLICABLE verdict.

## Evidence

`gold_ecosystem_paths.tsv:439` has depth four, nodes 4909/4910, 17 ORGANISM
assertions and zero other tree counters. Displaying the first node with the
two-node note is faithful. `gold_path_biosamples.tsv:878` separately has two
BIOSAMPLE observations at path 4910; unlike denominators must not be summed.

`gold_studies.tsv:1730` associates Gs0132952 with this path alone. At :2080,
Gs0135086 spans this path plus Defined media, two whole-body host categories
and fungal Mycelium. Study membership does not identify a universal organism,
host, substrate, condition or experimental replicate count for the target.
No exact target triad was found in the complete raw scan.

The Sugarcane filter cake descendant separately has two biosamples at :879,
studies Gs0114039/Gs0114467 at :772/:820, and broad/local/medium triads at
`gold_path_triads.tsv:140-142`. Those include a composting-toilet local term;
none is target evidence. No toilet setting, sugarcane feedstock or descendant
count is inherited by this parent review.

Fresh [node 4909](https://gold.jgi.doe.gov/ecosystem/4909),
[node 4910](https://gold.jgi.doe.gov/ecosystem/4910),
[Gs0132952](https://gold.jgi.doe.gov/study?id=Gs0132952) and
[Gs0135086](https://gold.jgi.doe.gov/study?id=Gs0135086) retrievals failed.
Exact study searches returned no results. Category searches produced generic
studies, not verified original node/sample crosswalks. Failure is not evidence
of source absence or retirement.

The inspected [PRJNA1426577 submission](https://www.ncbi.nlm.nih.gov/bioproject/1426577)
describes a particular agricultural-waste composting experiment sampled over
time with a commercial decomposer. It establishes that experiment's context,
not its equivalence to either GOLD study or this category's two biosamples.
No inoculant organism, stage, sequencing count or thermophilic condition was
imported into the record. A matched broad subject is not an accession crosswalk.

## Completeness

Ignored-inclusive target/parent IDs, stem, full path, Agricultural waste and
Composting labels, nodes and study accessions were searched across curation,
history, conf, tests, docs, research, prior reports, inventories and registries.
No target-owned ITEM decision, definition, exclusion, overlay, research entry,
retirement or earlier individual report was found within those bounds.
The parent report's child reference is not a completed target review.
Generic Composting decisions do not assess this exact source.

Optional empty biology is not a defect. iModulonDB is inapplicable: this target
has no named gene, strain, regulator, pathway or expression assertion.

## Findings

Zero blockers, two major findings, zero minor findings.

1. **Major: source scope and both strict parent claims remain unresolved.**
   The source's input, processing environment and product boundaries need
   assessment independently of the parent review and unrelated experiments.
   This is one combined scope/hierarchy gap, not proof of two false edges.
   Owners: maintained decisions, justified definitions and exact source-parent
   controls under `curation/`.
2. **Major: emitted mapping/status use endpoints different from their
   contract.** Schema lines 317-322 define source-to-record mapping, omitted
   for retained identity; GroundingStatusEnum at 776 onward is source-relative.
   The executed route compares the retained mint with an ontology parent.
   Owners: `src/habitatmech/seed.py`, `src/habitatmech/schema/habitatmech.yaml`
   and actual consumers; shared #1398. No formal SKOS self-link prohibition
   or blanket predicate reversal is claimed.

## Recommended Edits

Recover original category/node and organism/sample context before ITEM
curation in `curation/decisions.tsv`. Assess both parent contributions and add
an evidence-backed definition in `curation/term_requests.tsv` only if justified.
If agricultural waste is merely input context, guard any exclusion in
`curation/gold_parent_exclusions.tsv` by GOLD.e979bbb99c, the exact source path
and resolved parent ENVO:01000371. Do not assume a minted parent, repair the
parent's separate Solid Waste claim implicitly, or infer a universal recipe.

Resolve #1398 with explicit source/record/ontology endpoints and coherent
status semantics. Preserve the target mint, nodes/path, 17-ORGANISM provenance,
separate biosample denominator and historical events. Derive lifecycle status
from actual source decisions rather than parent review or publication.

## Follow-up Checks

For future authorized curation, regress exact route, parents, mapping endpoints,
count units and separation from descendant triads and multi-path study contexts.
Append history, dry-seed, inspect a forced canary and regenerate from maintained
inputs. Run labels, strict schema, provenance, full reproduction and QC; #1690
must be resolved before claiming all required gates pass. Refresh genuinely
changed semantic map/site inputs. No SSSOM/KGX execution or current kg-microbe
modeling certification was performed here.

## Additional Notes

Only this new report was written. No scientific input, generated record/page,
history, lifecycle status or GitHub item changed; no paid research or delegation
was used. Contextual parent and project reads are not additional record reviews.
