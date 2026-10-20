---
name: curate-causal-graphs
description: Review and curate evidence-backed HabitatMech mechanism overlays, then
  regenerate and verify habitat records without hand-editing generated YAML.
---

# HabitatMech causal mechanism overlays

Read [curation](../../../docs/CURATION.md),
[the schema](../../../src/habitatmech/schema/habitatmech.yaml), and
[add-yaml-record](../add-yaml-record/SKILL.md).
Generated `data/habitats/**/*.yaml` is not the writing surface. Mechanisms are
maintained in `curation/causal_graphs/<slug>.yaml` as `HabitatCausalGraphCuration`
with `causal_graphs`; resolve the exact owner identifier/slug before changing it.

Preserve stable graph/node/edge IDs. Check direction, habitat versus host/taxon
identity, condition and organism scope, and source support for each edge. Source
attestations that a habitat exists do not prove the mechanism. A plausible
pathway or taxon association must not become a causal claim.

Validate edited overlays with `just validate-causal <overlay-path>` and
`just validate-causal-all`. Use `just seed` preview and
`just seed-canary <IDENTIFIER> --force`; verify the regenerated target contains
the intended overlay changes. A skipped existing target is not a successful
canary. Then run the authorized `just seed-apply --force`, inspecting the complete
generated diff and never pruning on partial runs. Record actual history through
`just new-history`. Run `just validate-strict <record-path>`, `just verify-corpus`,
`just render`, `just qc` and `git diff --check`; derived status/history must follow
inputs, not be directly assigned on the generated record.
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
