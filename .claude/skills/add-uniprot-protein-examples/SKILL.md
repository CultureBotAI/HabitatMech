---
name: add-uniprot-protein-examples
description: Audit HabitatMech gene/protein mechanism nodes and add exact verified
  protein references where the native overlay schema preserves their identity and
  evidence.
---

# HabitatMech protein references in mechanisms

Read [the schema](../../../src/habitatmech/schema/habitatmech.yaml) and
[causal overlay workflow](../curate-causal-graphs/SKILL.md). Inventory generated
habitat records and their maintained `curation/causal_graphs/*.yaml` owners.
`CausalNode` supports `GENE_OR_PROTEIN`, `grounding`, `xrefs` and `description`;
it does **not** currently define a typed `protein_examples` field. Never insert a
sibling's unsupported fields or represent a family/complex by one member.

For a node explicitly denoting one exact protein, use a verified UniProtKB
reference only if it accurately denotes that node. For an abstract family or
complex, keep its semantic grounding; use a native reference only when the
source context and description unambiguously preserve example/subunit scope.
Do not use an untyped xref to smuggle in a related ortholog as equivalence. If the
native model cannot preserve required example/taxon/role distinctions, retain a
candidate and propose the missing representation; do not label it enriched.
Attach inspected role evidence to the supported edge, preserving organism and
experimental context in the native graph/description/evidence fields.

All changes belong to overlays and use the causal skill's validate-causal,
canary, regeneration, history and verify-corpus gates. No generated-record edit
or automatic status promotion is permitted.
## Protein identity and evidence

Inspect live UniProt entry metadata or a release-pinned, provenance-verifiable
native snapshot. Check primary accession and active/merged/deleted state,
organism and strain, sequence/isoform, gene/locus mapping and source identity.
Prefer an exact assayed protein over a convenient ortholog. A named gene alone
is not a unique protein match. Keep family, whole complex, individual subunit,
native protein and experimental construct distinct. UniProt identity metadata
supports identity; primary role evidence supports participation in the record's
mechanism. Retain the original accession and an explicit mapping rationale when
resolving a changed identifier. Do not silently substitute species or isoforms.
## Scope and completion

For one target, read the whole maintained record and its generated projection or
components. For a corpus goal, first freeze an inventory of record IDs, paths,
input hashes and applicable graph/protein elements; resume that ledger after an
interruption. Include hidden and ignored inputs when establishing absence.
Classify each target as checked, changed, evidence-limited, excluded, not
applicable or blocked, with reasons and inspected sources. A sample, a provider
report and a validator pass do not establish whole-corpus scientific completion.

Use [curate-yaml-record](../curate-yaml-record/SKILL.md) for the local evidence,
write, history and status contract; this adapter does not replace its managed
method. Record actual agent identity. Preserve scientific status rules and
unrelated edits. Use inspected primary evidence for mechanistic claims and exact
active identifiers for instances; never infer causality from association or
coverage from an empty query. A quotation is source text; interpretation belongs
in the native notes/explanation field.

Save final scientific assessments through
[review-yaml-record](../review-yaml-record/SKILL.md),
[record reviews](../../../docs/record-reviews.md), and the
[local profile](../../../docs/record-review-profile.md), including their native
persistence exceptions. Keep coverage/checkpoint accounting even when a clean
review should not produce a bundle. Unavailable prerequisites remain blocked;
a skipped target is not a completed enrichment. This skill authorizes no paid
provider call by itself.

After a completed goal, follow the user's authorized commit, push/PR,
adversarial review, issue/fix, merge and branch-cleanup sequence under the current
repository guidance. Carry forward existing authorization without asking again.
Use fresh required checks and native merge-queue rules. Verify actual merge and
landed content before deleting that feature branch or starting the next goal.
Only genuine review findings become issues; a no-diff goal needs a documented
no-op receipt rather than an artificial commit.
