# v2.8.6 — 2026-11-18

Tracker-only release: `layoff-announcement-tracker` moves to the v2.8.x line (schema 1.6.0); `listed-filing-extractor` is unchanged at runtime 2.2.2. The 50-column announcement output contract (43 business fields) is unchanged. Per-release engineering notes are bundled with the skill (`CHANGELOG-v2.8.*.md`).

- Rebuilds publisher-address resolution: aggregator redirect links and publisher sitemaps are parsed year-month pairwise, including robots-declared indexes, so articles resolve from Google News-style pointers instead of nearly always failing.
- Incremental ingest no longer deactivates the registered source corpus when a partial manifest is written; sources outside the manifest keep their active status.
- Clause-scoped multi-employer sentences: counts and shares are read from the clause carrying each employer's own action, with approximation qualifiers preserved on counts and shares alike.
- Announcement date and publication date are separate facts with `announcement_date_precision` (`day` / `month` / `relative` / `unknown`); no day is manufactured from page metadata.
- The second review re-reads bound evidence, recomputes values under current scope rules, verifies dates at recorded precision, and returns `confirm` / `revise` / `abstain` in risk order.
- Headcounts keep information versions (initial report, confirmed figure, implementation update) with as-of anchors; HTML inline tags stay inline so evidence offsets map to readable sentences.
- Real-estate reductions are separate events, mixed layoff/furlough populations record their basis, and retrospective sources are itemised with `source_timing=retrospective`.
- Adds regional closure, consultation and earnings-reduction discovery query families (16 to 22 queries per alias/year) and grouped missing-date/count/share follow-ups generated from existing plans and decisions.
- On resume, `candidate-review-prepare` reopens legacy automated exclusions caused by a missing plan or an inconclusive text rule; back up the workspace before the first migration.
- Existing pre-2.8 workspaces are not migrated silently. Create a fresh workspace and re-read original sources; old code 0 is never imported as absence.

Verified: the bundled tracker regression suite passes; the v2.8.4 validation reports 299 tests run, 298 passed, one skipped. No live semantic rerun or new complete collection is claimed.

# v2.3.1 — 2026-11-07

- Adds the runtime 2.3.1 discovery workflow: `discovery-plan`, `discovery-status`, `discovery-import`, and `candidate-review-prepare`, with preserved search captures and a deduplicated discovery inbox.
- Requires an English candidate ledger (`event_candidate_review.csv`) with included, merged, excluded, or unresolved dispositions and cited evidence.
- Adds `verification_source_url`; the event scope keeps 43 business fields and moves from 49 to 50 base columns.
- Accepts regulatory notices and credible attributed reporting as event evidence; inaccessible leads remain visible as coverage gaps.
- Adds targeted amount follow-up checks for issuers with blank core amounts across all requested years.
- Adds source-bound second review for positive AI compensation, internal integration, and adoption decisions.
- Bundles the shared research core and vendor engine inside each skill; installation no longer needs separate shared or engine folders.
- Existing 1.5.7-rc4 workspaces are not migrated silently. Start a fresh workspace and re-audit previous exports.

Verified: both skills compile; bundled discovery and event-review tests pass; init and discovery-plan smoke tests complete.
