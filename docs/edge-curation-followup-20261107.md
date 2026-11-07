# Extend exact native evidence and projection coverage for EdgeMech

The initial native adapter for CLAW #767 exports the complete pinned
`curation/decisions.tsv` surface, with explicit manifest exclusions.

Exact organism/taxon source observations, aggregate-to-row evidence bindings and reviewed SKOS projections are not supplied by the native decision table. A complete eligible-overlap result must report this scope limitation; zero matched native predicates is not evidence of no biological overlap.

Follow-up work must establish source-row identities, evidence ancestry,
reviewed payload scope and safe projection rules before admitting additional
assertions to eligible reuse. Keep counts/units, taxonomy/strain versions,
conditions and polarity where present. Never promote a record-level status
or native cohort review into approval of every exported assertion.

The current PR preserves these limitations and native statuses rather than
fabricating scientific RecordReview objects. This issue remains open for the
additional native evidence and projection work.
