# YAML Record Review: Salt flat/Salt pan sediment

- Repository: CultureBotAI/HabitatMech
- Record: `data/habitats/aquatic/salt_flat_salt_pan_sediment.yaml`
- Started UTC: 2026-10-05T06:22:56Z
- Finished UTC: 2026-10-05T06:27:55Z
- Verdict: needs curation; 0 blocker, 3 major, 0 minor findings.

## Target

The complete generated HabitatRecord was read. Exact source-qualified
identifier habitatmech:GOLD.1bb701a40c denotes salt-flat/salt-pan sediment,
not the whole pan, its water or a generic sediment environment. It is
AQUATIC, NARROW and REVIEWED, with two parents, one GOLD attestation,
four ORGANISM assertions and two history events. Definition, synonyms,
xrefs, parameters, taxa, evidence, graphs, discussions and datasets are
absent. PATHS.tsv:1489 pins the stem. No scientific input or generated
artifact was edited.

## Validation

- `just validate data/habitats/aquatic/salt_flat_salt_pan_sediment.yaml`:
  pass, no issues.
- `just validate-strict data/habitats/aquatic/salt_flat_salt_pan_sediment.yaml`:
  pass, one file and zero errors.
- Complete build_corpus/build_document dictionary equality: pass; one
  contributing source, one ITEM-reviewed source, no taxa and two events.
- Fresh `just validate-products`: pass; 1179 canonical, one synonym,
  five exceptions and 2054 no-adapter skips. This is not a scientific
  hierarchy or mapping-endpoint check.
- `just worklist --status all --limit 5`: pass, 953 ungrounded records
  and 1810 decisions. Actual child and immediate-parent routes were
  independently executed.
- Initial QC/label launches stopped on uv cache sandbox access before
  validation; both were rerun with the required access. Fresh `just qc`
  is live during tests, after passing lint, documentation and provenance.
  Log: /private/tmp/habitatmech-salt-flat-marsh-qc-20261005.log.
  No terminal success or later gate completion is claimed at review close.
- The previous publication's separate main-push QC 37271740487 reached
  SUCCESS during this review; it is not the fresh local run.
- Isolated removal of either parent changes actual full-context semantic
  text. Predicate-only omission is text-neutral. No map/site or export
  was regenerated.

## Identity and Grounding

Actual minting reproduces GOLD.1bb701a40c. The default route is
gold_unmatched, UNGROUNDED with no mapping predicate. The ITEM
GROUND_AS_PARENT row at curation/decisions.tsv:254 changes it through
curated_ground_as_parent_from_gold_unmatched to the retained mint,
NARROW/skos:narrowMatch and extra parent ENVO:00000279 saline pan.
The rationale explicitly distinguishes sediment from the pan, but the
chosen genus contradicts that distinction. REVIEWED and the August 12
event faithfully describe the maintained decision, not scientific validity.

Current official [ENVO:00000279 saline pan](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00000279),
inventory row 6868, is a salt-covered ground expanse under ENVO:01000296
dry lake bed. Typed OWL marks salt pan exact and salt flat related, not
proof that every slash-bin member has identical scope. The whole pan is
not a strictly broader kind of its sediment. Neither the slash label nor
the parent's generated exact synonyms licenses exact identity.

The second parent comes from a different owner. The immediate GOLD path
Environmental > Aquatic > Non-marine Saline and Alkaline > Hypersaline
mints habitatmech:GOLD.4398c0543d. Its default is gold_unmatched; the ITEM
GROUND decision at decisions.tsv:459 resolves it CLOSE to ENVO:01001043
through curated_ground_from_gold_unmatched. The independent GOLD parent
pass at seed.py:898-907 then gives that identity to the sediment as a parent.
Fixing the child's curated saline-pan target alone cannot remove this edge.

Current official [ENVO:01001043 hypersaline water environment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001043),
inventory row 8538, denotes an environmental system determined by
hypersaline water. Typed OWL places it under saline water environment,
ENVO:01000307, with water-related restrictions. A source setting does not
make the sampled sediment material a subtype of that environmental system.
This is a material-versus-system distinction, not an assertion that the
sediment never occurs in a hypersaline setting.

Current official candidates and typed OWL were separately inspected:

| Term | Scope / consequence |
| --- | --- |
| ENVO:00002007 sediment | Particulate environmental material formed by transport/deposition by flowing liquid; defensible generic material-genus candidate, not exact identity for this qualified source. Inventory row 7170, subclass row 5268. |
| ENVO:01001036 sediment permeated by saline water | Pore space filled with saline water; an additional hydration condition needing source-wide support. Row 8531, subclass row 6834. |
| ENVO:01001050 saline sediment environment | An environmental system determined by saline-water-permeated sediment, not the sediment material itself. Row 8545. |

[Sediment](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002007)
is modeled under ENVO:01000060 particulate environmental material. The
[permeated-sediment term](https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A01001036)
does not prescribe a universal numeric salinity threshold. Bounded current
OLS queries returned no salt pan sediment or salt flat sediment result;
the saline sediment query returned environmental-system candidates.
Ignored-inclusive inventory searches likewise did not find an exact
salt-pan/flat sediment class. This is not an all-ontology absence claim.

## Evidence

Physical data/raw/gold_ecosystem_paths.tsv:672 contains the complete
depth-five path ending Hypersaline > Salt flat/Salt pan sediment, one node
7962, four organisms and zero tree study/biosample counts. The emitted
four ORGANISM assertions and full source path are faithful. The current
official GOLD node request returned 404, not a retirement determination.

All 14 raw inventories were scanned for exact path/node membership.
Only the tree row matched: no exact bulk sample, API triad, study,
parameter, PREGO, BacDive or Madin contribution was found. Individual
organism/sample accessions and original occurrence chains remain
unrecovered. Four assertions are not a measured microbial abundance.

The complete saline-pan and hypersaline-water-environment records were
read as context only. Their distinct source counts and other source
paths are not evidence for this sediment's four organisms. The immediate
parent's 219 organisms and the pan's separate six- and 19-organism
attestations must not be borrowed.

The primary [McGonigle et al. Bonneville Salt Flats study](https://doi.org/10.1128/msphere.00378-19)
was inspected in its abstract, stratigraphic results and sampling methods.
It collected distinct sediment layers from eight pits in a perennial
salt pan and characterized archaeal/bacterial communities with 16S
amplicons. This independently supports sediment as a microbial habitat
within the pan and shows why sampled layers are not the whole feature.
It is not demonstrated provenance for GOLD 7962. Site mineralogy, taxa,
hydration history and inferred metabolic functions are not universal
attributes for this record; no study accession or mechanism was imported.

NARROW/skos:narrowMatch also reproduces #1398's shared endpoint contract
defect. The schema at lines 317-322 describes source concept to record
identifier, omitting the predicate when the record is the source; the
grounding enum at 776-790 uses the source/record comparison. Actual
GROUND_AS_PARENT compares the retained source with an ontology parent,
and seed.py:890-891 emits that predicate without the parent endpoint.
A better material genus alone does not reconcile those comparisons.
No formal SKOS inconsistency or downstream export failure is claimed.

The full rendered page was inspected. Both false parents appear under
Broader habitats; the count/unit and decision history are faithfully
rendered. Agreement with generated YAML is not independent validation.

## Completeness

Ignored/hidden-inclusive searches covered exact ID, label, stem, node/path
and salt-flat/pan sediment wording across curation, conf, history,
research, prior reports, inventories, PATHS, RETIRED, docs, source and
tests. The decision and path lock exist. No target-authored definition,
causal overlay, dedicated research, separate history, retirement or
previous individual review was found. Broader inland-saline research
mentions four sediment assertions; it is not a target identity ruling.

Optional quantitative parameters, taxa, causal graphs and datasets should
remain empty without exact evidence. iModulonDB is not applicable because
no gene, regulator or expression claim occurs in the record. A future
definition may clarify the slash/source scope, but cannot simply be
attached to the current NARROW record: authored definitions require a
minted UNGROUNDED target.

## Findings

| Severity | Finding | Maintained owner / scope |
| --- | --- | --- |
| Major | The ITEM decision attaches a whole saline pan rather than a defensible sediment-material genus. | Exact GOLD.1bb701a40c row in `curation/decisions.tsv`; curated resolver in `src/habitatmech/seed.py`. |
| Major | The independent GOLD parent pass promotes the hypersaline water environment setting into a strict superclass of sediment material. | Exact child contribution in `src/habitatmech/seed.py:898`; separate from the child's curated genus. |
| Major | Retained-source NARROW/skos:narrowMatch compares with an implicit ontology parent rather than the declared source/record endpoints. | Shared resolver/schema/emitter/consumer contract under #1398. |

No blocker or minor finding was established. Identity, count unit,
source provenance and mechanical review/history derivation remain sound.

## Recommended Edits

1. Correct the exact ITEM decision to a justified sediment-material genus,
   retaining the source-qualified mint and full rationale. Assess the
   saline-water-permeated candidate's hydration restriction; do not
   exact-merge with generic sediment, a whole pan or a sediment environment.
2. Suppress the independent false water-environment source-parent edge
   through maintained source-specific machinery. Correcting only one
   parent owner leaves the other false edge.
3. Reconcile #1398 with explicit endpoint semantics and consumer tests,
   not a global broadMatch/narrowMatch swap.
4. If adding an authored source-specific definition, first choose a
   compatible UNGROUNDED decision and explicitly justify replacement of
   the false inherited parents. Do not combine a NARROW decision with a
   term-request definition or patch generated YAML.
5. Preserve exact node/path, four ORGANISM assertions, source category,
   stable stem and old events. Recover source membership before adding
   numerical chemistry/taxa; append required correction history.

## Follow-up Checks

Regress the exact curated genus, independent source-parent suppression,
retained identity/provenance/count, definition guard and mapping endpoints.
Dry-seed and inspect a forced GOLD.1bb701a40c canary before guarded wider
regeneration; never prune a partial run. Run ordinary/strict schema,
labels, provenance/history, mapping-consumer tests, exact reproduction,
site/redirect, term-request and full QC gates.

Either isolated parent removal changes real semantic text, so complete
genuine map/site refresh under #1217 while preserving protected #1218
and runtime pins. Audit actual SSSOM/KGX products and current kg-microbe
contracts separately; this report establishes no product-readiness claim.

## Additional Notes

All 577 open/closed issue titles and bodies were searched for exact
ID/node and salt-flat/pan sediment wording; no target-specific issue was
found. #1398 is the existing shared endpoint owner. Issue comments were
not exhaustively searched. No GitHub mutation occurred during this
individual review.

Typed ENVO snapshot SHA-256:
`a0b919065d33a9cf975b74cadd16c75f32f512d17f4f6d5999b74216701df54c`.
