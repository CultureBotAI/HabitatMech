# Methane bioremediation material: defensible material genus with an incorrect anaerobic-reactor rationale

- Review: 20261009T112815Z-methane
- Repository: CultureBotAI/HabitatMech
- Started UTC: 2026-10-09T11:19:04Z
- Finished UTC: 2026-10-09T11:28:15Z
- Reviewer: codex-gpt-5 (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Reviewed the whole methane record and its source/definition owners. The material genus, chemical-only xref, suppressed chemical synonym, native ITEM status and separate source-count snapshots are coherent. One confirmed minor finding concerns the rationale equating an anaerobic bioreactor with methane production. Original GOLD members and the authored gas-exposure restriction remain unverified; no replacement identity or mechanism is inferred.

## Scope And Provenance

Whole generated methane.yaml and its sole GOLD contribution. Environmental material and the excluded Hydrocarbon parent were read as context, not additional completed target reviews.

Selection: PATHS.tsv:2867, habitatmech:GOLD.d510166905, exact Engineered &gt; Bioremediation &gt; Hydrocarbon &gt; Methane path.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4ad2058873bd936baa7cba619e5fed8233cf92bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| habitatmech:GOLD.d510166905 | data/habitats/engineered/methane.yaml | generated | methane bioremediation material |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Pre-assessment input capture | passed | True | habitatmech:GOLD.d510166905 | 42 inputs captured at 4ad205887 after reading the complete target. |
| Source-adapter context capture | passed | True | habitatmech:GOLD.d510166905 | Added the three inspected GOLD helper files: 45 inputs; verified the original revision and all 42 prior hashes remain identical. |
| Target LinkML validation | passed | True | habitatmech:GOLD.d510166905 | No issues found. |
| Target closed-schema validation | passed | True | habitatmech:GOLD.d510166905 | One file, zero errors. |
| All-fourteen-inventory exact-field scan | passed | True | habitatmech:GOLD.d510166905 | Exact aggregate path has two ORGANISM assertions and two source nodes. A separate August-20 inventory reports one biosample and study Gs0121605; no complete target triad or target taxon/parameter row. Units and snapshots are not combined. |
| Full source resolution and document reproduction | passed | True | habitatmech:GOLD.d510166905 | Gold-unmatched mint becomes ITEM CONFIRM_UNGROUNDED with chemical xref; one source and one reviewed source. Whole generated document equals disk. The curated REPLACE genus removes the non-habitat chemical parent; chemical source-label synonym is intentionally suppressed. |
| Ignored-inclusive ownership and prior-review search | passed | True | habitatmech:GOLD.d510166905 | Decision, definition, path lock and native history identified. No earlier individual review or target causal overlay found in these bounded roots. |
| Current GOLD classification and exact ontology terms | passed | True | habitatmech:GOLD.d510166905 | Workbook row147 confirms terminal4452. All five exact ENVO/ChEBI terms remain active with matching labels. Public study and node page requests returned HTTP errors, reported separately from successful term/classification access. |
| Full corpus reproduction | passed | True | habitatmech:GOLD.d510166905 | 3208 expected and found; zero missing, extra or differing records. |
| Native curation history | passed | True | habitatmech:GOLD.d510166905 | 219 native histories valid. |
| Raw inventory provenance | passed | True | habitatmech:GOLD.d510166905 | 14 committed inventories and two GOLD source snapshots current. |
| Parent, status and reference regressions | passed | True | habitatmech:GOLD.d510166905 | 6 passed, 33 deselected. Deterministic integrity is not scientific proof. |
| Exact-baseline full QC receipt | passed | True | habitatmech:GOLD.d510166905 | Freshly queried SUCCESS at 4ad205887. The log read in the preceding publication turn records 645 passed, 3 skipped and all native gates. No new local full-QC run in this review. |
| Exact-baseline ontology-label receipt | passed | True | habitatmech:GOLD.d510166905 | Freshly queried SUCCESS at 4ad205887. Configured ontology coverage and accepted exceptions do not establish source meaning. |
| Scientific-input equivalence | passed | True | habitatmech:GOLD.d510166905 | Scientific inputs and generated records unchanged from the exact verified base. |
| Original GOLD member detail | failed | False | habitatmech:GOLD.d510166905 | OFFLINE_TOKEN was not supplied to the process; no credential search performed. Public study/node page reads also failed. Original member crosswalk, matrix and exposure phase are not established. |
| Untracked source cache discovery | failed | False | habitatmech:GOLD.d510166905 | Ignored-inclusive filenames under local data/build found no goldData.xlsx, gold_biosample_triads.tsv or GOLD cache JSON. A broader ../../ filename scan returned exit2 with permission-denied subtrees; that partial search cannot establish global absence. |
| Causal and expression adapters | not_applicable | False | habitatmech:GOLD.d510166905 | Target has no gene, protein, regulator, strain, expression dataset or causal overlay. Generic methane oxidation wording is not an iModulonDB organism/dataset key; the background paper's molecular results are not imported. |

## Scientific And Domain Assessments

### Material rather than methane molecule

identity: supported. Targets: habitatmech:GOLD.d510166905.

The authored material interpretation is coherent and deliberately separates the chemical xref; it is not independently established for original GOLD members.

### Environmental-material genus and excluded chemical/device parents

graph: supported. Targets: habitatmech:GOLD.d510166905.

Environmental material is broader than the declared matrix. A chemical class and a containing reactor are not broader material classes. The existing genus need not change to correct the rationale.

### Anaerobic-reactor reasoning

evidence: concern. Targets: habitatmech:GOLD.d510166905.

The term definition is oxygen-condition based, and inspected primary evidence demonstrates methane oxidation in an anoxic reactor. Production-only wording is incorrect.

### Original source matrix and methane phase

scope: unknown. Targets: habitatmech:GOLD.d510166905.

The original organisms and the later biosample were not recovered. Generic reactor literature and a four-path study inventory do not prove gas-only exposure or a sample-level source crosswalk.

### Snapshot and unit preservation

quantity: supported. Targets: habitatmech:GOLD.d510166905.

Two ORGANISM assertions are retained. One later biosample and a multi-path study are distinct evidence units, not additions to that count.

### ITEM lifecycle and synonym safety

consistency: supported. Targets: habitatmech:GOLD.d510166905.

One source with one ITEM decision correctly yields REVIEWED. The displaced chemical label is not retained as an exact habitat synonym.

### No imported taxa, parameters or molecular claims

completeness: supported. Targets: habitatmech:GOLD.d510166905.

No direct target rows justify optional additions. Environmental-material parent's taxa and paper-specific genes/rates cannot be transferred to this source class.

### Complete generation and owned future changes

schema: supported. Targets: habitatmech:GOLD.d510166905.

Whole record reproduces. Future rationale correction belongs in term_requests.tsv with append-only native session history and normal generation, not direct YAML editing.

## Findings

### anaerobic_rationale: Anaerobic bioreactor is incorrectly equated with methane production

minor / open / confirmed; issue key: methane-anaerobic-reactor-rationale.

The authored notes reject ENVO:00002124 as overspecifying anaerobic methane production rather than aerobic oxidation. Neither the ontology definition nor primary experimental evidence supports that process restriction. The device-versus-matrix distinction independently supports the retained material genus, so this is a bounded rationale defect, not proof of wrong identity or parent.

## Recommended Actions And Acceptance Checks

### correct_rationale

Correct the maintained definition notes to distinguish material from device without equating anoxia with methanogenesis; attach a precise inspected citation. Preserve historical session files and record any authorized correction in a new session.

- Notes no longer claim anaerobic bioreactor implies methane production or that methane oxidation is necessarily aerobic.
- Keep current identity, chemical-only xref, two ORGANISM assertions, source nodes and genus unless separate source evidence warrants changing them.
- just validate data/habitats/engineered/methane.yaml; just validate-strict data/habitats/engineered/methane.yaml; just verify-corpus; just validate-history; just render; just qc.
- Save a linked successor review for disposition; do not rewrite this observation.

### recover_source

Before broadening or further narrowing the definition, recover the original GOLD organism memberships and the Gs0121605 biosample on path4452; establish matrix and methane exposure phase from original metadata.

- Record exact original member accessions and a reproducible source crosswalk.
- Retain scope as unresolved if member-level evidence remains unavailable; do not import other study paths or paper-specific biology.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/habitats/engineered/methane.yaml; Entire YAML and all three generated history events | supports | Minted ENGINEERED material, UNGROUNDED/REVIEWED, ENVO:00010483 parent, CHEBI:16183 xref, sole GOLD attestation with two ORGANISM assertions. |
| decision | curation/decisions.tsv; Row1178, exact mint | supports | ITEM CONFIRM_UNGROUNDED retains CHEBI methane solely as xref; it does not ground the habitat to the molecule. |
| definition | curation/term_requests.tsv; Row83, full definition and notes | partial | REPLACE environmental-material genus, methane-gas exposure and microbial oxidation are authored claims. Notes cite unspecified biofiltration literature and incorrectly associate anaerobic bioreactor with methane production. |
| source | data/raw/gold_ecosystem_paths.tsv; Row773; manifest August16 snapshot | supports | Two source nodes4451&#124;4452; two ORGANISM assertions. Other aggregate counters are zero at this snapshot, not ecological absence. |
| later_source | data/raw/gold_path_biosamples.tsv; Row943; gold_studies.tsv row1366; GOLD_MANIFEST.yaml August20 | context_only | Later bulk snapshot has one biosample on path4452. Study Gs0121605 spans four paths including this one, anaerobic reactor, anaerobic sludge and tailings pond; these are not all members of this target or evidence that it shares their biology. |
| xref | curation/external_xrefs.tsv; Row4 and source-label suppression at seed.py:473-484 | supports | Allow-listed active unvendored methane xref does not become habitat identity, parent, or exact source-label synonym. Native infrastructure history documents this intended behavior. |
| ontology | https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002124; Current ENVO:00002124 plus 00010483,00002123,00002152 and CHEBI:16183 exact lookups; committed terms read | refutes | Anaerobic bioreactor denotes a reactor with nonoxygenated contained material, not specifically methane production. Material versus containing device remains a sound distinction; ChEBI confirms methane chemical identity. |
| anaerobic_study | https://link.springer.com/article/10.1007/s00253-020-10748-z; Stultiens et al.2020; abstract, methods Biomass/Establishment, results Enrichment, Fig3; PMID32607646 | refutes | The authors operated an anoxic sludge-inoculated reactor and measured methane consumption. This directly counters the production-only rationale, without proving that its culture belongs to the GOLD target. Gas-supplied culture is an example, not universal source scope. |
| gold | https://gold.jgi.doe.gov/download?mode=ecosystempaths; Current site data row147 | supports | Terminal4452 retains Engineered/Bioremediation/Hydrocarbon/Methane/Unclassified. This establishes classification, not original organism identity or a gas-only matrix. |
| history | history/mappings/methane/2026-09-10T131350Z-claude-code-7d9a98.yaml; Whole native record | context_only | Records the authored matrix interpretation and xref/REPLACE choice but identifies no methane-biofiltration article or source specimen. |
| search | curation; ID/label/slug/node plus methane-biofiltration/oxidation queries across curation,history,research,reports,reviews,docs,conf and PATHS | context_only | The maintained notes and history supplied no traceable article for the original gas-exposure scope. No target research report, target causal overlay or earlier individual review was recovered in the bounded roots. |
| unavailable | https://gold.jgi.doe.gov/study?id=Gs0121605; Public study and ecosystem4451 requests; bounded API helper attempt | unknown | Public requests failed; API attempt lacked an exported token. No original member reconstruction. Cached search snippets and inaccessible PMC/PubMed pages were not scientific evidence; the publisher's inspected full text was used. |
| gates | https://github.com/CultureBotAI/HabitatMech/actions/runs/37922005631; Exact4ad205887 baseline; label run37922005635; fresh native target/corpus checks | supports | Native gates pass on unchanged scientific inputs; deterministic success does not repair unsupported rationale. |

## Limits And Additional Notes

- One record of the 3208-record corpus reviewed here; full-corpus completion remains unproven.
- Source-member reconstruction was unavailable; a current GOLD class path is not specimen evidence or proof of the authored gas restriction.
- Parent records are context only, not completed parent reviews or endorsements of their taxa.
- No article-level evidence for the original curator's unspecified biofiltration literature was recovered in the bounded ignored-inclusive roots. Newly inspected primary evidence does not retroactively establish what that curator read.
- Exact-baseline fullQC and ontology-label receipts are reused with unchanged-input verification; no fresh global ontology refresh, and three baseline native tests remain skipped.
- Only a new immutable review pair is written. No scientific curation, native status/history change, GitHub mutation, publication, or SSSOM/KGX readiness assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T112815Z-methane
kind: record
repository: CultureBotAI/HabitatMech
title: 'Methane bioremediation material: defensible material genus with an incorrect
  anaerobic-reactor rationale'
started_at: '2026-10-09T11:19:04Z'
finished_at: '2026-10-09T11:28:15Z'
reviewer:
  identity: codex-gpt-5
  kind: agent
  model: gpt-5
  independence: self_review
  independence_basis: Same agent continuing individual corpus review; this is not
    independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md@2.0.0
completion: completed
verdict: needs_curation
scientific_review: true
summary: Reviewed the whole methane record and its source/definition owners. The material
  genus, chemical-only xref, suppressed chemical synonym, native ITEM status and separate
  source-count snapshots are coherent. One confirmed minor finding concerns the rationale
  equating an anaerobic bioreactor with methane production. Original GOLD members
  and the authored gas-exposure restriction remain unverified; no replacement identity
  or mechanism is inferred.
source:
  git_revision: 4ad2058873bd936baa7cba619e5fed8233cf92bb
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 4544b5d2c11fbbb3a46cd8a65f7e664363df78c1000c590aab533219f9eec59b
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: d429c8bb74f521df9a77a90b216a44fc6959ee28efb1fa17a93582536caa8bce
    role: context
  - path: CLAUDE.md
    sha256: 98d95f910ff5160bc5b2ff572766785519dacdba487700bebaa6dbf96d071fd9
    role: context
  - path: conf/id_label_targets.yaml
    sha256: e100d84aabccaeb00c1a60246142b3cafcec009dbfba58f5cc319c35adddb633
    role: context
  - path: curation/decisions.tsv
    sha256: 0602cca13e6495da256a6f1cfd5897462f73f9739a729447862017d93c148efd
    role: context
  - path: curation/definition_source_label_exclusions.tsv
    sha256: cc4da2e7e5e8750e6c023683014aa37a909230280f231eec5be7c71795340312
    role: context
  - path: curation/external_xrefs.tsv
    sha256: cf8394a6ab22e35efd9e252aef422018226280830bf816a39bf4f2256ff75ad5
    role: context
  - path: curation/gold_parent_exclusions.tsv
    sha256: 9d2324647d0a0ddeccc2f7836811872e112af208bb1b8f7decb332c00f17d12b
    role: context
  - path: curation/term_requests.tsv
    sha256: 3efdac153ccd40f518458a9dc5360e09dd660c3a42fbd06bfc57f3b2f707ece7
    role: context
  - path: curation/term_requests_excluded.tsv
    sha256: 36bc332b2b699c23df6de1006c591a822f8571d130173e84454a35dafd18fde0
    role: context
  - path: data/habitats/PATHS.tsv
    sha256: b59b9e800a918135e3915145d4d8098bb48dcea36a312b3004c594a57d221ae9
    role: context
  - path: data/habitats/RETIRED.tsv
    sha256: 41beffc45aabdf304de633c21200b375d7f01d1cb2e036d4a026961d545a35e5
    role: context
  - path: data/habitats/engineered/hydrocarbon__e596377f.yaml
    sha256: 28b8c37c070c8a3cff0bd88f4afeb5d0e938e8486f030f67718c5322fab25f3b
    role: context
  - path: data/habitats/engineered/methane.yaml
    sha256: 4bafd057fe4a37b648a69ed2dc7aa39ae235e3ea8562e4a3e9e46e88b987e57f
    role: target
  - path: data/habitats/other/environmental_material.yaml
    sha256: f3916c9c17060dbb92c026d8e340be9478c37409361279bbb639642cdae29fe7
    role: context
  - path: data/raw/GOLD_MANIFEST.yaml
    sha256: 99ec487ae02d512cfb75440685f927abe907effe52cb755feb095631e8841489
    role: context
  - path: data/raw/MANIFEST.yaml
    sha256: 4657672d429be35e551ceef4a1204ab0a8120558ce63e2a2b74188eee94b8480
    role: context
  - path: data/raw/bacdive_isolation_sources.tsv
    sha256: fb1645dd899a43130be9cf38b0e8b27ffbaa0175306917bff20e20ee225875fc
    role: context
  - path: data/raw/bacdive_source_taxa.tsv
    sha256: 08471c12f887882e2a6af8f078166b1f59ed7e2b24eb7edbe43a7fc77dfbad44
    role: context
  - path: data/raw/environment_parameters.tsv
    sha256: a75d0f565d8ee2498188ff98b17d0ab325ae4f782601bf4414eff6e86c13e0f9
    role: context
  - path: data/raw/gold_ecosystem_paths.tsv
    sha256: 5e4ede39caec9598dc6e1b8f34a292cc758c9837a963d825af1f58d295163b5d
    role: context
  - path: data/raw/gold_path_biosamples.tsv
    sha256: 97cd7c8d0e731d07a85db6986dbcf9e49096a3c7988bd90a855599f492fe619e
    role: context
  - path: data/raw/gold_path_triads.tsv
    sha256: b1717bd8fc4fdcd6a1a132f4eb32df3638b01ddf7d78f9a5797f110ee2b1e8d6
    role: context
  - path: data/raw/gold_studies.tsv
    sha256: fa7aaa46f288d10c453bb723e6cf486cde646a003559414b5523cc3883a84c8c
    role: context
  - path: data/raw/isolation_source_groundings.tsv
    sha256: ab6a997359aab961c40928f9b13e06adb6dc43124fa3de821819570dd87f43b8
    role: context
  - path: data/raw/madin_habitat_taxa.tsv
    sha256: d30854cfcffca0405914d04071ac47053938d354d5df250125843131b7c91fd7
    role: context
  - path: data/raw/madin_habitats.tsv
    sha256: 2ae1756f40242600365c49bfbdada4bce5fc8b86630426bb34892f055e5a5c93
    role: context
  - path: data/raw/ontology_subclass_edges.tsv
    sha256: b06a709f4e47abf0417e5a8907b671dc057dd4b5ca10518d3f60c043911d65a3
    role: context
  - path: data/raw/ontology_terms.tsv
    sha256: 7508afaa249de34fd877f6d168391cfce36030f067f169752562db987fb5d348
    role: context
  - path: data/raw/prego_habitat_taxa.tsv
    sha256: 26c121b5ec8ac25a637b33f988d15a4db5165cc6fd17c14a2b69003b614d8ce6
    role: context
  - path: data/raw/prego_habitats.tsv
    sha256: 07dd724817bec360d8971509c68ec14c39925fc5eb9db32f99fcfaa2c052dd06
    role: context
  - path: docs/CURATION.md
    sha256: 36df8306394c06c352b73e0bf7b47a2858784cedac7389a24d0b78f593ece646
    role: context
  - path: docs/HARMONIZATION.md
    sha256: ee39d3cd29115ee14f5e7386169c76c47d471ebdc2502c008c49d30fb44918f1
    role: context
  - path: docs/RESEARCH.md
    sha256: 82c5471890d310bf8fd33141d5596f847bfc1eb6091c2db6f485388435e067af
    role: context
  - path: docs/record-review-profile.md
    sha256: f7aa39ee762d94f1902d9f08f328cb897bc543e4e226057eb4770d24bfcc6eb5
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/infrastructure/source_label_xref_synonyms/2026-09-10T131413Z-claude-code-4d76ef.yaml
    sha256: 06c8bffc1617c17fcd092dd5f64f8d115ebaefd86903619c8f0b8a78daf01015
    role: context
  - path: history/mappings/methane/2026-09-10T131350Z-claude-code-7d9a98.yaml
    sha256: b648f20a297dfbaaccfa7e8237cb9de748d20fd67d313974e7b7099e76da134b
    role: context
  - path: justfile
    sha256: e9b0ba6704eab8f68570a9b7d592d4b82fc719792b0fec04240ae1b52f862b14
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/extract_gold_biosamples.py
    sha256: b6a2773c86fe718e1ca0b1d7b32709f0eee491ac813655e310aa0817c0fec31b
    role: context
  - path: scripts/gold_api.py
    sha256: 29ffed8b78a179a53a2801efe4fd568b3c836d6524c783c6f1284712a8792dc2
    role: context
  - path: scripts/gold_enumerate.py
    sha256: 53df07afa52e2236f6ec03f3da79001d32f1e1ab2d1bb74a3a6a5a6b05ce84be
    role: context
  - path: src/habitatmech/schema/habitatmech.yaml
    sha256: 52d2a22309a1f4a10728a663560bb4d918346c292221fd34139b99b4159d3fe5
    role: context
  - path: src/habitatmech/seed.py
    sha256: 92adf631fa099120a497ff7001473e659347d23ac9b418f04cd341ddad5d2a89
    role: context
targets:
- target_id: habitatmech:GOLD.d510166905
  path: data/habitats/engineered/methane.yaml
  label: methane bioremediation material
  kind: generated
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: ITEM source identity and contaminant xref
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definition, rationale and REPLACE genus
  - repository: CultureBotAI/HabitatMech
    path: curation/external_xrefs.tsv
    role: Unvendored ChEBI xref allow-list
  - repository: CultureBotAI/HabitatMech
    path: data/raw/gold_ecosystem_paths.tsv
    role: Frozen GOLD path and ORGANISM counts
  - repository: CultureBotAI/HabitatMech
    path: src/habitatmech/seed.py
    role: Generated representation and source-label suppression
scope:
  description: Whole generated methane.yaml and its sole GOLD contribution. Environmental
    material and the excluded Hydrocarbon parent were read as context, not additional
    completed target reviews.
  selection: PATHS.tsv:2867, habitatmech:GOLD.d510166905, exact Engineered > Bioremediation
    > Hydrocarbon > Methane path.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - habitatmech:GOLD.d510166905
checks:
- check_id: capture
  name: Pre-assessment input capture
  command: env UV_CACHE_DIR=build/uv-cache uv run python scripts/record_review.py
    inspect --targets /private/tmp/habitatmech-methane-targets-20261009T111904Z.json
    --input CLAUDE.md --input justfile --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/RESEARCH.md --input docs/record-review-profile.md --input docs/record-reviews.md
    --input .claude/skills/review-yaml-record/SKILL.md --input .claude/skills/curate-yaml-record/references/review-checklist.md
    --input schema/record_review.yaml --input src/habitatmech/schema/habitatmech.yaml
    --input src/habitatmech/seed.py --input curation/decisions.tsv --input curation/gold_parent_exclusions.tsv
    --input curation/term_requests.tsv --input curation/term_requests_excluded.tsv
    --input data/habitats/PATHS.tsv --input data/habitats/RETIRED.tsv --input data/raw/ontology_terms.tsv
    --input data/raw/ontology_subclass_edges.tsv --input data/raw/isolation_source_groundings.tsv
    --input data/raw/gold_ecosystem_paths.tsv --input data/raw/gold_path_biosamples.tsv
    --input data/raw/gold_path_triads.tsv --input data/raw/gold_studies.tsv --input
    data/raw/prego_habitats.tsv --input data/raw/prego_habitat_taxa.tsv --input data/raw/bacdive_isolation_sources.tsv
    --input data/raw/bacdive_source_taxa.tsv --input data/raw/madin_habitats.tsv --input
    data/raw/madin_habitat_taxa.tsv --input data/raw/environment_parameters.tsv --input
    data/raw/MANIFEST.yaml --input data/raw/GOLD_MANIFEST.yaml --input curation/external_xrefs.tsv
    --input curation/definition_source_label_exclusions.tsv --input history/mappings/methane/2026-09-10T131350Z-claude-code-7d9a98.yaml
    --input history/infrastructure/source_label_xref_synonyms/2026-09-10T131413Z-claude-code-4d76ef.yaml
    --input data/habitats/other/environmental_material.yaml --input data/habitats/engineered/hydrocarbon__e596377f.yaml
    --input conf/id_label_targets.yaml
  summary: 42 inputs captured at 4ad205887 after reading the complete target.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: capture_extension
  name: Source-adapter context capture
  command: env UV_CACHE_DIR=build/uv-cache uv run python scripts/record_review.py
    inspect --targets /private/tmp/habitatmech-methane-targets-20261009T111904Z.json
    --input CLAUDE.md --input justfile --input docs/CURATION.md --input docs/HARMONIZATION.md
    --input docs/RESEARCH.md --input docs/record-review-profile.md --input docs/record-reviews.md
    --input .claude/skills/review-yaml-record/SKILL.md --input .claude/skills/curate-yaml-record/references/review-checklist.md
    --input schema/record_review.yaml --input src/habitatmech/schema/habitatmech.yaml
    --input src/habitatmech/seed.py --input curation/decisions.tsv --input curation/gold_parent_exclusions.tsv
    --input curation/term_requests.tsv --input curation/term_requests_excluded.tsv
    --input data/habitats/PATHS.tsv --input data/habitats/RETIRED.tsv --input data/raw/ontology_terms.tsv
    --input data/raw/ontology_subclass_edges.tsv --input data/raw/isolation_source_groundings.tsv
    --input data/raw/gold_ecosystem_paths.tsv --input data/raw/gold_path_biosamples.tsv
    --input data/raw/gold_path_triads.tsv --input data/raw/gold_studies.tsv --input
    data/raw/prego_habitats.tsv --input data/raw/prego_habitat_taxa.tsv --input data/raw/bacdive_isolation_sources.tsv
    --input data/raw/bacdive_source_taxa.tsv --input data/raw/madin_habitats.tsv --input
    data/raw/madin_habitat_taxa.tsv --input data/raw/environment_parameters.tsv --input
    data/raw/MANIFEST.yaml --input data/raw/GOLD_MANIFEST.yaml --input curation/external_xrefs.tsv
    --input curation/definition_source_label_exclusions.tsv --input history/mappings/methane/2026-09-10T131350Z-claude-code-7d9a98.yaml
    --input history/infrastructure/source_label_xref_synonyms/2026-09-10T131413Z-claude-code-4d76ef.yaml
    --input data/habitats/other/environmental_material.yaml --input data/habitats/engineered/hydrocarbon__e596377f.yaml
    --input conf/id_label_targets.yaml --input scripts/gold_api.py --input scripts/gold_enumerate.py
    --input scripts/extract_gold_biosamples.py
  summary: 'Added the three inspected GOLD helper files: 45 inputs; verified the original
    revision and all 42 prior hashes remain identical.'
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: schema
  name: Target LinkML validation
  command: env UV_CACHE_DIR=build/uv-cache just validate data/habitats/engineered/methane.yaml
  summary: No issues found.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: strict
  name: Target closed-schema validation
  command: env UV_CACHE_DIR=build/uv-cache just validate-strict data/habitats/engineered/methane.yaml
  summary: One file, zero errors.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: raw
  name: All-fourteen-inventory exact-field scan
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nfrom pathlib import\
    \ Path\nimport csv,json\nneedles={'habitatmech:GOLD.d510166905','Engineered >\
    \ Bioremediation > Hydrocarbon > Methane','gold.ecosystem:4451','gold.ecosystem:4452'}\n\
    for path in sorted(Path('data/raw').glob('*.tsv')):\n    hits=[]\n    with path.open()\
    \ as h:\n        for n,row in enumerate(csv.DictReader(h,delimiter='\\t'),2):\n\
    \            values=[v for x in row.values() for v in (x if isinstance(x,list)\
    \ else [x]) if v]\n            if any(v in needles or needles.intersection(v.split('|'))\
    \ for v in values):hits.append({'line':n,'row':row})\n    print(path.name,json.dumps(hits))\n\
    PY"
  summary: Exact aggregate path has two ORGANISM assertions and two source nodes.
    A separate August-20 inventory reports one biosample and study Gs0121605; no complete
    target triad or target taxon/parameter row. Units and snapshots are not combined.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: route
  name: Full source resolution and document reproduction
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nfrom habitatmech\
    \ import seed as s\nfrom dataclasses import asdict\nfrom pathlib import Path\n\
    import json,yaml\nrows=s.read_tsv('gold_ecosystem_paths.tsv')\nont=s.OntologyIndex(s.read_tsv('ontology_terms.tsv'),s.read_tsv('ontology_subclass_edges.tsv'))\n\
    d=s.load_decisions(s.DECISIONS_PATH)\nmapping={}\nfor row in s.read_tsv('isolation_source_groundings.tsv'):\n\
    \    for key in (s.norm_label(row['subject_label']),s.norm_label(row['subject_label_normalized'])):\n\
    \        if key:mapping.setdefault(key,row)\nfor path in ['Engineered > Bioremediation\
    \ > Hydrocarbon > Methane','Engineered > Bioremediation > Hydrocarbon']:\n   \
    \ row=next(r for r in rows if r['canonical_path']==path)\n    ident=s.mint('GOLD',path)\n\
    \    auto=s.resolve_gold(row,ont,mapping,s.leaf_claimants(rows),s.composed_claimants(rows))\n\
    \    print(json.dumps({'path':path,'mint':ident,'automatic':asdict(auto),'final':asdict(s.apply_decision(auto,ident,d))}))\n\
    c=next(c for c in s.build_corpus().concepts if c.identifier=='habitatmech:GOLD.d510166905')\n\
    assert s.build_document(c)==yaml.safe_load(Path('data/habitats/engineered/methane.yaml').read_text())\n\
    print('Whole document equal; sources',c.source_concepts,'reviewed',c.reviewed_sources)\n\
    for ident in ['ENVO:00010483','ENVO:00002152','ENVO:00002123','ENVO:00002124','CHEBI:16183']:\n\
    \    print('ONTOLOGY',ident,ont.terms.get(ident))\nPY"
  summary: Gold-unmatched mint becomes ITEM CONFIRM_UNGROUNDED with chemical xref;
    one source and one reviewed source. Whole generated document equals disk. The
    curated REPLACE genus removes the non-habitat chemical parent; chemical source-label
    synonym is intentionally suppressed.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: search
  name: Ignored-inclusive ownership and prior-review search
  command: rg --no-ignore --hidden -n 'GOLD\.d510166905|methane bioremediation material|methane\.yaml|gold.ecosystem:445[12]'
    curation history research reports reviews data/habitats/PATHS.tsv
  summary: Decision, definition, path lock and native history identified. No earlier
    individual review or target causal overlay found in these bounded roots.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: external
  name: Current GOLD classification and exact ontology terms
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nimport urllib.request,urllib.parse,io,hashlib,json\n\
    from openpyxl import load_workbook\nfrom html.parser import HTMLParser\nu='https://gold.jgi.doe.gov/download?mode=ecosystempaths'\n\
    b=urllib.request.urlopen(u,timeout=60).read()\ns=load_workbook(io.BytesIO(b),read_only=True,data_only=True)['site\
    \ data'];s.reset_dimensions()\nprint('GOLD_WORKBOOK',len(b),hashlib.sha256(b).hexdigest())\n\
    for n,row in enumerate(s.iter_rows(values_only=True),1):\n    if 'Methane' in\
    \ row:print('GOLD_ROW',n,row)\nfor ident in ['ENVO:00010483','ENVO:00002152','ENVO:00002123','ENVO:00002124','CHEBI:16183']:\n\
    \    ontology=ident.split(':')[0].lower()\n    u='https://www.ebi.ac.uk/ols4/api/ontologies/'+ontology+'/terms?'+urllib.parse.urlencode({'obo_id':ident})\n\
    \    b=urllib.request.urlopen(u,timeout=60).read();d=json.loads(b)\n    print('TERM',ident,len(b),hashlib.sha256(b).hexdigest())\n\
    \    for t in d.get('_embedded',{}).get('terms',[]):print(json.dumps({k:t.get(k)\
    \ for k in ('obo_id','label','description','is_obsolete','synonyms')}))\nclass\
    \ Text(HTMLParser):\n    def __init__(self):super().__init__();self.parts=[];self.skip=0\n\
    \    def handle_starttag(self,tag,attrs):\n        if tag in ('script','style'):self.skip+=1\n\
    \    def handle_endtag(self,tag):\n        if tag in ('script','style'):self.skip=max(0,self.skip-1)\n\
    \    def handle_data(self,data):\n        if not self.skip and data.strip():self.parts.append(data.strip())\n\
    for u in ['https://gold.jgi.doe.gov/study?id=Gs0121605','https://gold.jgi.doe.gov/ecosystem/4451']:\n\
    \    try:\n        b=urllib.request.urlopen(u,timeout=30).read();p=Text();p.feed(b.decode('utf-8','replace'))\n\
    \        print('GOLD_PAGE',u,len(b),hashlib.sha256(b).hexdigest(),'\\n'.join(p.parts)[:18000])\n\
    \    except Exception as e:print('GOLD_PAGE_UNAVAILABLE',u,type(e).__name__)\n\
    PY"
  summary: Workbook row147 confirms terminal4452. All five exact ENVO/ChEBI terms
    remain active with matching labels. Public study and node page requests returned
    HTTP errors, reported separately from successful term/classification access.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: corpus
  name: Full corpus reproduction
  command: env UV_CACHE_DIR=build/uv-cache just verify-corpus
  summary: 3208 expected and found; zero missing, extra or differing records.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: history
  name: Native curation history
  command: env UV_CACHE_DIR=build/uv-cache just validate-history
  summary: 219 native histories valid.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: provenance
  name: Raw inventory provenance
  command: env UV_CACHE_DIR=build/uv-cache just provenance-check
  summary: 14 committed inventories and two GOLD source snapshots current.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: references
  name: Parent, status and reference regressions
  command: env UV_CACHE_DIR=build/uv-cache uv run pytest -q tests/test_corpus_integrity.py
    -k 'parent or reviewed_records or history or causal_edges_reference'
  summary: 6 passed, 33 deselected. Deterministic integrity is not scientific proof.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: qc_receipt
  name: Exact-baseline full QC receipt
  command: gh run view 37922005631 --json status,conclusion,headSha,url
  summary: Freshly queried SUCCESS at 4ad205887. The log read in the preceding publication
    turn records 645 passed, 3 skipped and all native gates. No new local full-QC
    run in this review.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: label_receipt
  name: Exact-baseline ontology-label receipt
  command: gh run view 37922005635 --json status,conclusion,headSha,url
  summary: Freshly queried SUCCESS at 4ad205887. Configured ontology coverage and
    accepted exceptions do not establish source meaning.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: unchanged
  name: Scientific-input equivalence
  command: git diff --exit-code 4ad2058873bd936baa7cba619e5fed8233cf92bb -- data curation
    src scripts tests docs conf schema CLAUDE.md justfile
  summary: Scientific inputs and generated records unchanged from the exact verified
    base.
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - habitatmech:GOLD.d510166905
- check_id: original_source
  name: Original GOLD member detail
  status: failed
  required: false
  command: "env UV_CACHE_DIR=build/uv-cache uv run python - <<'PY'\nimport os,sys,json\n\
    sys.path.insert(0,'scripts')\nfrom gold_api import access_token,biosamples,gold_path\n\
    if not os.environ.get('OFFLINE_TOKEN'):\n    print('GOLD API unavailable: OFFLINE_TOKEN\
    \ not supplied to this process; no credential search performed.')\n    raise SystemExit(2)\n\
    try:\n    token=access_token()\n    rows=biosamples(token,studyGoldId='Gs0121605')\n\
    except BaseException as exc:\n    print('GOLD API unavailable:',type(exc).__name__,';\
    \ credentials and exception payload omitted.')\n    raise SystemExit(2)\nprint('Study\
    \ biosample count',len(rows))\nfor row in rows:\n    if gold_path(row)=='Engineered\
    \ > Bioremediation > Hydrocarbon > Methane':\n        print(json.dumps(row,sort_keys=True))\n\
    PY"
  exit_code: 2
  target_ids:
  - habitatmech:GOLD.d510166905
  summary: OFFLINE_TOKEN was not supplied to the process; no credential search performed.
    Public study/node page reads also failed. Original member crosswalk, matrix and
    exposure phase are not established.
- check_id: cache_search
  name: Untracked source cache discovery
  status: failed
  required: false
  target_ids:
  - habitatmech:GOLD.d510166905
  summary: Ignored-inclusive filenames under local data/build found no goldData.xlsx,
    gold_biosample_triads.tsv or GOLD cache JSON. A broader ../../ filename scan returned
    exit2 with permission-denied subtrees; that partial search cannot establish global
    absence.
  command: rg --no-ignore --hidden --files ../.. -g GOLD_nodes.tsv -g GOLD_edges.tsv
    -g goldData.xlsx -g gold_biosample_triads.tsv -g '!**/.git/objects/**'
  exit_code: 2
- check_id: molecular
  name: Causal and expression adapters
  status: not_applicable
  required: false
  target_ids:
  - habitatmech:GOLD.d510166905
  summary: Target has no gene, protein, regulator, strain, expression dataset or causal
    overlay. Generic methane oxidation wording is not an iModulonDB organism/dataset
    key; the background paper's molecular results are not imported.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/habitats/engineered/methane.yaml
  locator: Entire YAML and all three generated history events
  support: supports
  summary: Minted ENGINEERED material, UNGROUNDED/REVIEWED, ENVO:00010483 parent,
    CHEBI:16183 xref, sole GOLD attestation with two ORGANISM assertions.
  accessed_at: '2026-10-09T11:25:01Z'
- evidence_id: decision
  kind: record_content
  reference: curation/decisions.tsv
  locator: Row1178, exact mint
  support: supports
  summary: ITEM CONFIRM_UNGROUNDED retains CHEBI methane solely as xref; it does not
    ground the habitat to the molecule.
  accessed_at: '2026-10-09T11:25:01Z'
- evidence_id: definition
  kind: record_content
  reference: curation/term_requests.tsv
  locator: Row83, full definition and notes
  support: partial
  summary: REPLACE environmental-material genus, methane-gas exposure and microbial
    oxidation are authored claims. Notes cite unspecified biofiltration literature
    and incorrectly associate anaerobic bioreactor with methane production.
  accessed_at: '2026-10-09T11:25:01Z'
- evidence_id: source
  kind: record_content
  reference: data/raw/gold_ecosystem_paths.tsv
  locator: Row773; manifest August16 snapshot
  support: supports
  summary: Two source nodes4451|4452; two ORGANISM assertions. Other aggregate counters
    are zero at this snapshot, not ecological absence.
  accessed_at: '2026-10-09T11:25:01Z'
- evidence_id: later_source
  kind: record_content
  reference: data/raw/gold_path_biosamples.tsv
  locator: Row943; gold_studies.tsv row1366; GOLD_MANIFEST.yaml August20
  support: context_only
  summary: Later bulk snapshot has one biosample on path4452. Study Gs0121605 spans
    four paths including this one, anaerobic reactor, anaerobic sludge and tailings
    pond; these are not all members of this target or evidence that it shares their
    biology.
  accessed_at: '2026-10-09T11:25:01Z'
- evidence_id: xref
  kind: record_content
  reference: curation/external_xrefs.tsv
  locator: Row4 and source-label suppression at seed.py:473-484
  support: supports
  summary: Allow-listed active unvendored methane xref does not become habitat identity,
    parent, or exact source-label synonym. Native infrastructure history documents
    this intended behavior.
  accessed_at: '2026-10-09T11:25:01Z'
- evidence_id: ontology
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/envo/terms?obo_id=ENVO%3A00002124
  locator: Current ENVO:00002124 plus 00010483,00002123,00002152 and CHEBI:16183 exact
    lookups; committed terms read
  support: refutes
  summary: Anaerobic bioreactor denotes a reactor with nonoxygenated contained material,
    not specifically methane production. Material versus containing device remains
    a sound distinction; ChEBI confirms methane chemical identity.
  accessed_at: '2026-10-09T11:25:01Z'
  snapshot_sha256: 100dc16e36bbc3c0c495513c57c8ec0219cb408f5c82dc2a97975f1d03c80bd9
- evidence_id: anaerobic_study
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/s00253-020-10748-z
  locator: Stultiens et al.2020; abstract, methods Biomass/Establishment, results
    Enrichment, Fig3; PMID32607646
  support: refutes
  summary: The authors operated an anoxic sludge-inoculated reactor and measured methane
    consumption. This directly counters the production-only rationale, without proving
    that its culture belongs to the GOLD target. Gas-supplied culture is an example,
    not universal source scope.
  accessed_at: '2026-10-09T11:25:01Z'
- evidence_id: gold
  kind: database
  reference: https://gold.jgi.doe.gov/download?mode=ecosystempaths
  locator: Current site data row147
  support: supports
  summary: Terminal4452 retains Engineered/Bioremediation/Hydrocarbon/Methane/Unclassified.
    This establishes classification, not original organism identity or a gas-only
    matrix.
  accessed_at: '2026-10-09T11:25:01Z'
  snapshot_sha256: 3933e5f0664915c1bbfa00212e17d013da360fb33dd52e509254050813135396
- evidence_id: history
  kind: record_content
  reference: history/mappings/methane/2026-09-10T131350Z-claude-code-7d9a98.yaml
  locator: Whole native record
  support: context_only
  summary: Records the authored matrix interpretation and xref/REPLACE choice but
    identifies no methane-biofiltration article or source specimen.
  accessed_at: '2026-10-09T11:25:01Z'
- evidence_id: search
  kind: search
  reference: curation
  locator: ID/label/slug/node plus methane-biofiltration/oxidation queries across
    curation,history,research,reports,reviews,docs,conf and PATHS
  support: context_only
  summary: The maintained notes and history supplied no traceable article for the
    original gas-exposure scope. No target research report, target causal overlay
    or earlier individual review was recovered in the bounded roots.
  accessed_at: '2026-10-09T11:25:01Z'
  search_scope: rg --no-ignore --hidden included ignored files. Exact ID/label/slug/node
    and methane biofiltration/methane oxidation/methane-containing queries; unrelated
    records were not treated as evidence. Broader parent-directory filename search
    was incomplete because of permission-denied subtrees.
- evidence_id: unavailable
  kind: database
  reference: https://gold.jgi.doe.gov/study?id=Gs0121605
  locator: Public study and ecosystem4451 requests; bounded API helper attempt
  support: unknown
  summary: Public requests failed; API attempt lacked an exported token. No original
    member reconstruction. Cached search snippets and inaccessible PMC/PubMed pages
    were not scientific evidence; the publisher's inspected full text was used.
  accessed_at: '2026-10-09T11:25:01Z'
- evidence_id: gates
  kind: validation
  reference: https://github.com/CultureBotAI/HabitatMech/actions/runs/37922005631
  locator: Exact4ad205887 baseline; label run37922005635; fresh native target/corpus
    checks
  support: supports
  summary: Native gates pass on unchanged scientific inputs; deterministic success
    does not repair unsupported rationale.
  accessed_at: '2026-10-09T11:25:01Z'
assessments:
- assessment_id: identity
  area: identity
  topic: Material rather than methane molecule
  outcome: supported
  summary: The authored material interpretation is coherent and deliberately separates
    the chemical xref; it is not independently established for original GOLD members.
  evidence_ids:
  - record
  - decision
  - xref
  target_ids:
  - habitatmech:GOLD.d510166905
- assessment_id: genus
  area: graph
  topic: Environmental-material genus and excluded chemical/device parents
  outcome: supported
  summary: Environmental material is broader than the declared matrix. A chemical
    class and a containing reactor are not broader material classes. The existing
    genus need not change to correct the rationale.
  evidence_ids:
  - record
  - definition
  - ontology
  target_ids:
  - habitatmech:GOLD.d510166905
- assessment_id: rationale
  area: evidence
  topic: Anaerobic-reactor reasoning
  outcome: concern
  summary: The term definition is oxygen-condition based, and inspected primary evidence
    demonstrates methane oxidation in an anoxic reactor. Production-only wording is
    incorrect.
  evidence_ids:
  - definition
  - ontology
  - anaerobic_study
  target_ids:
  - habitatmech:GOLD.d510166905
- assessment_id: scope
  area: scope
  topic: Original source matrix and methane phase
  outcome: unknown
  summary: The original organisms and the later biosample were not recovered. Generic
    reactor literature and a four-path study inventory do not prove gas-only exposure
    or a sample-level source crosswalk.
  evidence_ids:
  - source
  - later_source
  - gold
  - unavailable
  - search
  target_ids:
  - habitatmech:GOLD.d510166905
- assessment_id: counts
  area: quantity
  topic: Snapshot and unit preservation
  outcome: supported
  summary: Two ORGANISM assertions are retained. One later biosample and a multi-path
    study are distinct evidence units, not additions to that count.
  evidence_ids:
  - source
  - later_source
  - record
  target_ids:
  - habitatmech:GOLD.d510166905
- assessment_id: lifecycle
  area: consistency
  topic: ITEM lifecycle and synonym safety
  outcome: supported
  summary: One source with one ITEM decision correctly yields REVIEWED. The displaced
    chemical label is not retained as an exact habitat synonym.
  evidence_ids:
  - decision
  - xref
  - record
  target_ids:
  - habitatmech:GOLD.d510166905
- assessment_id: optional
  area: completeness
  topic: No imported taxa, parameters or molecular claims
  outcome: supported
  summary: No direct target rows justify optional additions. Environmental-material
    parent's taxa and paper-specific genes/rates cannot be transferred to this source
    class.
  evidence_ids:
  - source
  - later_source
  - record
  target_ids:
  - habitatmech:GOLD.d510166905
- assessment_id: reproduction
  area: schema
  topic: Complete generation and owned future changes
  outcome: supported
  summary: Whole record reproduces. Future rationale correction belongs in term_requests.tsv
    with append-only native session history and normal generation, not direct YAML
    editing.
  evidence_ids:
  - definition
  - gates
  target_ids:
  - habitatmech:GOLD.d510166905
findings:
- finding_id: anaerobic_rationale
  issue_key: methane-anaerobic-reactor-rationale
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Anaerobic bioreactor is incorrectly equated with methane production
  description: The authored notes reject ENVO:00002124 as overspecifying anaerobic
    methane production rather than aerobic oxidation. Neither the ontology definition
    nor primary experimental evidence supports that process restriction. The device-versus-matrix
    distinction independently supports the retained material genus, so this is a bounded
    rationale defect, not proof of wrong identity or parent.
  target_ids:
  - habitatmech:GOLD.d510166905
  field_paths:
  - curation_history[2].changes
  evidence_ids:
  - definition
  - ontology
  - anaerobic_study
  rule_id: docs/CURATION.md#curated-definitions-and-hierarchy
  native_severity: minor
  normalization_reason: Incorrect bounded explanatory text; no demonstrated identity,
    parent, count or status regression.
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definition, rationale and REPLACE genus
actions:
- action_id: correct_rationale
  description: Correct the maintained definition notes to distinguish material from
    device without equating anoxia with methanogenesis; attach a precise inspected
    citation. Preserve historical session files and record any authorized correction
    in a new session.
  finding_ids:
  - anaerobic_rationale
  target_ids:
  - habitatmech:GOLD.d510166905
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definition, rationale and REPLACE genus
  generator: just seed; just seed-canary habitatmech:GOLD.d510166905 --force; authorized
    normal generation
  acceptance_checks:
  - Notes no longer claim anaerobic bioreactor implies methane production or that
    methane oxidation is necessarily aerobic.
  - Keep current identity, chemical-only xref, two ORGANISM assertions, source nodes
    and genus unless separate source evidence warrants changing them.
  - just validate data/habitats/engineered/methane.yaml; just validate-strict data/habitats/engineered/methane.yaml;
    just verify-corpus; just validate-history; just render; just qc.
  - Save a linked successor review for disposition; do not rewrite this observation.
- action_id: recover_source
  description: Before broadening or further narrowing the definition, recover the
    original GOLD organism memberships and the Gs0121605 biosample on path4452; establish
    matrix and methane exposure phase from original metadata.
  finding_ids: []
  target_ids:
  - habitatmech:GOLD.d510166905
  owner_paths:
  - repository: CultureBotAI/HabitatMech
    path: curation/decisions.tsv
    role: ITEM source identity and contaminant xref
  - repository: CultureBotAI/HabitatMech
    path: curation/term_requests.tsv
    role: Authored definition, rationale and REPLACE genus
  acceptance_checks:
  - Record exact original member accessions and a reproducible source crosswalk.
  - Retain scope as unresolved if member-level evidence remains unavailable; do not
    import other study paths or paper-specific biology.
limitations:
- One record of the 3208-record corpus reviewed here; full-corpus completion remains
  unproven.
- Source-member reconstruction was unavailable; a current GOLD class path is not specimen
  evidence or proof of the authored gas restriction.
- Parent records are context only, not completed parent reviews or endorsements of
  their taxa.
- No article-level evidence for the original curator's unspecified biofiltration literature
  was recovered in the bounded ignored-inclusive roots. Newly inspected primary evidence
  does not retroactively establish what that curator read.
- Exact-baseline fullQC and ontology-label receipts are reused with unchanged-input
  verification; no fresh global ontology refresh, and three baseline native tests
  remain skipped.
- Only a new immutable review pair is written. No scientific curation, native status/history
  change, GitHub mutation, publication, or SSSOM/KGX readiness assessment.
```
