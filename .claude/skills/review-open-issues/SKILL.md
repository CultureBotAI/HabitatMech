---
name: review-open-issues
description: Sweep and prioritize HabitatMech's complete open GitHub issue queue using current corpus, curation-decision, grounding, generated-artifact, and code evidence. Use for full backlog triage or deciding which issues are genuinely urgent; do not use as permission to close issues, re-seed the corpus, launch a paid research batch, or implement fixes.
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Review and prioritize open issues

Produce a complete, dependency-aware triage of HabitatMech's open issues. The
issue queue, the curation backlog index (#12), and the generated worklists are
different surfaces: sweep the queue itself, then test every claim against the
current repository and the authoritative project contracts.

This is a read-only review by default. It does not implement fixes, re-seed the
corpus, run a paid research batch, close or edit issues, change labels, or
maintain a tracker unless the user separately authorizes that exact mutation.

**When to use**: the user asks to review, triage, or prioritize issues or the
backlog; asks what is genuinely urgent; or a review pass has just filed a batch
of issues that need sorting.

**When NOT to use**: picking the next unit of work to implement, or acting on a
single known issue. This skill produces a ranking, not a fix. It is expensive
enough that it should not run on every "what's next" question.

## Sources of truth

Use these before relying on an issue title or an old planning comment:

- `CLAUDE.md` for the generated-file boundaries, the safe corpus workflow, and
  the semantic invariants — the shortest statement of what counts as a defect;
- `docs/HARMONIZATION.md` for identity, merging, the anti-conflation rule, and
  what the seeder deliberately does not do;
- `docs/CURATION.md` for decision semantics across all three curation inputs
  (`decisions.tsv`, `term_requests.tsv`, `redirects_retracted.tsv`);
- `docs/RESEARCH.md` for what a deep-research report is and is not;
- the module docstring in `src/habitatmech/seed.py` for the grounding routes in
  the order tried — read it before judging any grounding issue;
- `src/habitatmech/schema/habitatmech.yaml` for what an enum value actually
  asserts (`NOT_APPLICABLE` means "the source concept is not a habitat", which
  is a stronger claim than most issue prose assumes);
- `data/raw/MANIFEST.yaml` and `data/raw/GOLD_MANIFEST.yaml` for upstream bytes;
- current source, tests, CI, and the committed corpus and site for behavior.

Treat issue bodies and titles as claims, not current status. Read comments:
corrections, narrowed residuals, and reversals of earlier reasoning are recorded
there. A merged PR is evidence only after its code and acceptance criteria are
checked.

Generated artifacts are evidence about the corpus, never an independent source:
`data/habitats/`, `pages/`, `data/habitats/RETIRED.tsv`, the README statistics
block, and `curation/term_requests/envo_robot_template.tsv` are all outputs. An
issue that proposes editing one of them directly is mis-stated, not merely
wrong; the fix belongs in the extractor, the seeder, or a curation decision.

## Workflow

### 1. Fetch the entire queue

Confirm the repository, current count, labels, and full queue. Never silently
accept `gh`'s default 30-item limit.

```bash
gh repo view --json nameWithOwner,url,defaultBranchRef
gh issue list --state open --limit 5000 --json number | jq length
gh issue list --state open --limit 5000 \
  --json number,title,body,comments,labels,createdAt,updatedAt,author
gh label list --limit 200
```

State the exact number reviewed and whether coverage was complete. Read every
issue body and its comments; for a long queue, inspect related groups in
parallel but preserve one disposition per issue.

The repository already carries `priority: P0` / `P1` / `P2` labels. Report the
tier you assign even when it disagrees with the label, and say which it is.

### 2. Build the dependency graph before assigning rank

Place each issue at the earliest stage it affects:

```text
upstream source release (GOLD / BacDive / PREGO / Madin) + vendored ontology slice
  -> committed inventories in data/raw/ and their manifests
  -> extractor and source-concept identity
  -> grounding route, minted identifier, and the merge
  -> curation inputs: decisions.tsv, term_requests.tsv, redirects_retracted.tsv
  -> generated records under data/habitats/ (+ PATHS.tsv slugs)
  -> generated site under pages/, RETIRED.tsv redirects, term-request template
  -> outward-facing claims: README statistics, the published site, term requests
```

An upstream identity or grounding problem invalidates every curation decision
keyed to it and every record that merged into it. Recommend fixing or auditing
that root problem before curating downstream or regenerating artifacts. Group
issues that share a root cause, but do not hide the individual issue numbers.

For each issue, record when applicable:

- pipeline stage, and whether the fix belongs in the extractor, the seeder, a
  curation decision, or a template;
- affected source concepts and minted identifiers, and how many records and
  assertions ride on them;
- which of the four parent contributors is implicated — ontology subclass
  parents, the GOLD parent-path link, the ambiguous-leaf rule, or a curated
  definition's genus — since `decisions.tsv` is not the whole audit trail;
- `grounding_status` and `mapping_status` separately; they answer different
  questions and an issue often conflates them;
- assertion counts *with their `assertion_unit`*, never summed across units;
- whether any published URL moves, and therefore whether a redirect is owed;
- prerequisites, blockers, duplicates, and superseding issues;
- cheapest decisive evidence and acceptance test;
- execution class: read-only audit, local edit + `just qc`, bulk re-seed,
  upstream re-extraction, or a billed model-assisted research run.

### 3. Check current reality and staleness

For each issue or group representative:

- Search exact issue references in history:

  ```bash
  git log --all --oneline --perl-regexp --grep '#<N>\b'
  gh pr list --state merged --search '<N>' --limit 100
  ```

  The word boundary is required: `#12` must not match `#127`. GitHub PR search
  is only a lead; open each candidate and verify it actually resolves the issue.

- Use `rg` to confirm that named paths, functions, `just` recipes, columns, and
  claims still exist and behave as described. Inspect tests as well as
  implementation.
- Query the corpus rather than trusting a count in an issue title. Backlog
  numbers in titles go stale every time a slice merges:

  ```bash
  just report
  just worklist
  just research-worklist
  ```

- Compare acceptance criteria with the merged change. If only part is fixed,
  retain the issue with a narrowed residual; do not recommend closure merely
  because a related PR merged.
- Distinguish an observation from its action issue. Prefer closing a fully
  recorded observation as superseded when a separate open issue owns the only
  remaining work.
- **A decision row is evidence only for the question its note discusses.** This
  is where a triage pass goes to answer "was this examined?", and the answer is
  narrower than it looks. `REVIEW` means the curator endorsed *the seeder's own
  answer* — whatever it was, on whatever question they were actually asking —
  and it carries `review_depth: ITEM`, so the record reads as curated. On the
  current corpus, 350 of 356 `REVIEW` notes never mention habitat-hood at all.
  `Muridae-Mouse/Rat` sat at `NOT_APPLICABLE` — "the source concept is not a
  habitat" — over 325 strains behind a `REVIEW` whose note discussed only
  whether its xref was over-narrow (#43, repaired by #194). Read the note before
  crediting the row.
- Verify a record by reading it, not by its filename or its label. Filenames are
  pinned in `PATHS.tsv` and deliberately do not track labels, so a mismatch is
  expected and is not by itself a defect.

### 4. Apply corpus and curation stop-the-line checks

Treat these as P0 when live or outward-facing:

- a published record URL that 404s, or a redirect regression in `RETIRED.tsv` —
  the map is the only thing standing between curation and dead citable URLs;
- a non-habitat adopted as a record identity: a quality, chemical, disease,
  process, procedure, or a whole-organism taxon term;
- a `parent_habitats` edge that is not strictly broader, from any of the four
  contributors — a related-but-not-broader term belongs in an xref;
- corpus drift: `data/habitats/` no longer reproducing from its inputs, or a
  record written outside `write_validated_habitat`, or hand-edited;
- extractor drift against the manifests waved through with `--allow-drift` — a
  different upstream checkout reproduces a wrong corpus just as faithfully;
- `assertion_count` summed or compared across differing `assertion_unit`;
- a generated artifact contradicting the corpus it claims to describe: stale
  README statistics, `pages/` out of step, an orphaned or missing stub;
- a record whose provenance claim misdescribes its source — an attestation
  note, `assertion_unit`, `source_label` or xref rationale asserting something
  the upstream data does not say. Every consistency gate is structurally blind
  to this: a wrong provenance claim reproduces as faithfully as a right one, so
  `verify-corpus` and `render --check` pass while the record misleads. It needs
  reading, not running. Five records published `targets a non-habitat ontology
  (); kept as an xref` with curation having dropped the mapping (#186);
- an outward-facing claim that presents unreviewed `SEEDED` output as curated,
  or a lexical match as an item-level judgment;
- a defect that would make an imminent billed research batch or bulk re-seed
  unusable while appearing to succeed.

Each of these has a cheap read-only probe; run the probe rather than asserting
the condition from an issue's prose. `just redirects-check` and
`just render-check` confirm the published site and the redirect map are in step
with the corpus, `just verify-corpus` proves the corpus reproduces from its
inputs, and `just validate-all` checks every record against the closed schema.
`just qc` runs all four, so a defect it would catch is either already fixed or
names a gap in the gate — say which.

For grounding and parent questions, prefer the routes in
`src/habitatmech/seed.py` and the invariants in `CLAUDE.md` over an issue's
prose. An empty upstream BacDive mapping is a curator's deliberate refusal and
stays `UNGROUNDED`; do not treat "no mapping" as an invitation to guess. A host
organism is a habitat even though its taxon term is not the identity — an issue
arguing the opposite is repeating reasoning this repository has already
reversed, and that reversal is recorded in `decisions.tsv` notes.

A count is not evidence of coverage. A curation claim needs the decision rows,
the review depth, and the records they actually reach.

### 5. Assign priority and execution order

Use priority for consequence and a separate readiness/cost annotation for
ordering.

- **P0 — stop the line.** Published-URL loss, corpus corruption or
  irreproducibility, a wrong identity or parent claim already published, or a
  blocker that must be resolved before an already-planned bulk or billed step.
- **P1 — important and schedulable.** Grounding correctness, curation
  reproducibility, provenance, generated-artifact reliability, and invariants
  with no machine check; defects that would waste a research budget; missing
  guards for a likely curator workflow.
- **P2 — low-risk or historical.** Documentation drift, refactors, theoretical
  edge cases, optional audits, and cosmetic corpus issues without published
  consequence.
- **CLOSE/UPDATE.** Fixed, superseded, duplicate, no-longer-applicable, or a
  title materially broader than the remaining work — including a stale count in
  the title. Cite the exact commit/PR/code/record that supports the disposition.

Calibrate P0 sparingly. Then order work within and across tiers using:

1. upstream identity and grounding before downstream curation;
2. anything that touches a published URL before anything that only touches
   uncommitted or internal state;
3. recover already-paid-for evidence — committed research reports under
   `research/habitats/` — before commissioning new runs;
4. read-only audits and `just qc` falsifiers before bulk writes;
5. a canary before any fan-out, and a re-canary after any fix to the canary;
6. combine issues only when one patch or one seed run genuinely satisfies each
   issue's acceptance criteria.

Do not prioritize by age, by assertion count alone, or by a `P0` label on a
stale title. A large backlog slice is not urgent merely because it is large.

### 6. Report

Return a compact report with:

1. coverage: repository, timestamp, number reviewed, and completeness;
2. top 2–3 next actions, including why they unblock later work;
3. a dependency-ordered P0/P1/P2 table with issue number, current status,
   evidence, blockers, execution class, and next acceptance test;
4. CLOSE/UPDATE candidates with specific evidence;
5. unresolved evidence gaps and cross-repository ownership — TraitMech,
   CultureMech, MediaIngredientMech, CommunityMech and the upstream
   `monarch-initiative/dismech` pattern share conventions, and
   `src/habitatmech/schema/mech_shared.yaml` is vendored byte-identically, so
   some findings are not this repository's to fix;
6. a short sequence showing which costly work must wait.

Call out old issues explicitly rather than silently dropping them. Separate
measured findings, code inspection, inference, and proposed/untested work.

## Conventions this skill enforces

- **Full-queue coverage, not first-page sampling.** State exactly how many
  issues were reviewed and whether coverage was complete.
- **Evidence over vibes.** Every CLOSE/UPDATE/duplicate recommendation cites a
  specific commit, PR, record, or code location — never "this looks done."
- **P0 is rare.** If more than ~10% of the queue lands P0, the calibration is
  wrong; recheck. A `priority: P0` label on a stale title is not evidence.
- **Titles are claims and they drift.** Backlog issues here carry counts in
  their titles that go stale on every merge. Re-read titles at report time
  rather than trusting the ones fetched at the start of the sweep.
- **The queue moves during the sweep.** Concurrent sessions work this repository
  in separate git worktrees and can merge PRs mid-triage. Re-check the open set
  immediately before reporting, and say so if it changed.

## Measurement discipline

The recurring failure in this repository is not misreading evidence, it is
mismeasuring it. Before citing any of the following, confirm how it was
obtained:

- **Generated output as a proxy for state.** Grepping `pages/` to learn which
  redirects are live coupled the answer to a template's wording; rewording the
  template silently dropped a published URL. Read the map, not the page.
- **A tool that returns nothing on failure.** `git ...` wrapped to return `""`
  on non-zero exit makes a broken call and an absent file the same answer — that
  produced 34 redirect rows instead of 138, silently. Confirm a helper
  distinguishes "absent" from "failed" before trusting a count it produced.
- **Exit codes through pipes.** `cmd | tail -3; echo $?` reports `tail`'s status,
  not `cmd`'s, so a fail-closed gate looks like it passed. Use
  `cmd >/tmp/o 2>/tmp/e; echo $?`, or `${PIPESTATUS[0]}`.
- **`gh pr diff --name-only` vs. a rename.** It can present a moved file as an
  addition with no matching deletion, hiding a category or path change. Use
  `git diff --name-status -M <base>...<head>`.
- **CI green on a branch is not green on the merge.** A PR can be MERGEABLE with
  no textual conflict while CI has never run on the combination. Merge the base
  in and re-run `just qc` before citing CI as evidence for a stale-based PR.
- **Vacuous assertions.** A test can pass because its subject never reaches the
  check. Before citing a test as coverage, mutate the thing it guards and
  confirm the test fails.
- **Truncated tool output.** Long TSV rows and long notes are elided by several
  tools. Re-read the cited file at the cited line before acting on it.
- **Backticks in a double-quoted `-m`.** `git commit -m "...`cmd`..."` executes
  the backticked text. Write reports, issue bodies, and commit messages
  containing shell examples via `-F <file>` or a quoted heredoc (`<<'EOF'`),
  then read the result back before pushing.

## Notes and limitations

- `gh issue list --json` omits `comments` unless explicitly requested. This
  repository records corrections, reversals, and narrowed residual scope in
  comments, so a body-only fetch will systematically overstate what is open.
- `gh pr list --search "<N>"` matches the number anywhere in indexed text, so it
  returns unrelated PRs. Treat every hit as a lead and open it before citing it.
  Likewise `git log --grep '#<N>'` needs the `\b` anchor, or `#12` matches
  `#127`.
- An issue may be fully addressed in code while its acceptance criteria are not.
  Partial fixes keep the issue open with a narrowed residual; say which part is
  done and which is not.
- A backlog issue whose title carries a count is never closed by a single slice.
  Recompute the count and recommend a retitle rather than a closure.
- Deep-research reports under `research/habitats/` are evidence for a curator,
  never automatic record input. A report's recommendation is not a decision, and
  citing one as if it were is a category error the reports themselves warn about.
- No @-mentions in issue comments or reports without explicit per-mention
  authorization (standing rule).

## Related

- `just report` — corpus, grounding and curation statistics; the authoritative
  answer to "how many" questions that issue titles get wrong.
- `just worklist` — the curation worklist keyed by minted identifier, which is
  how a decision row is addressed.
- `just research-worklist` — what a billed research batch would cover.
- `just qc` — the authoritative gate; CI runs the same runner. An issue claiming
  a defect that `just qc` would catch is either already fixed or names a gap in
  the gate, and which one it is belongs in the report.

## Mutation boundary

Do not close, comment on, relabel, retitle, or create issues or trackers during
the review. If the user later asks to act, present the exact issue numbers and
proposed mutation first. Apply closures one issue at a time with cited evidence;
never treat general approval as authorization for an unattended bulk-close.

Do not run `just seed-apply`, `just extract-inventory`, `just redirects`,
`just render`, or `just research <ID>` as part of triage. A recommended command
is a proposal, not permission to write the corpus, rewrite generated artifacts,
or spend a research budget. Do not pass `--allow-drift` to investigate drift;
investigating it is the work an issue should describe.

Each has a free counterpart that answers the same question, and the standing
rule is to exhaust those first — reach for these instead:

| Instead of | Run |
|---|---|
| `just seed-apply` | `just seed` (dry-run report), `just seed-canary <ID>` |
| `just redirects` | `just redirects-check` |
| `just render` | `just render-check` |
| `just research <ID>` | `just research-dry <ID>` — prints the provider command without calling it |
| `just extract-inventory` | `just extract-inventory-dry` |

A prohibition without its counterpart leaves a reviewer stalled or reaching for
the mutating command, which is how the costly ones get run by accident.

Do not merge a PR, delete a branch, or open a cross-repository issue without
explicit authorization.
