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
