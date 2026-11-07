# v2.3.1 — 2026-11-07

Discovery and candidate reconciliation release.

- Adds the runtime 2.3.1 discovery workflow: `discovery-plan`, `discovery-status`, `discovery-import`, and `candidate-review-prepare`. The planner builds broad per-company, per-year query families from verified roster aliases; actual search captures are preserved in the workspace and deduplicated into `discovery/inbox.csv`.
- Requires an English `event_candidate_review.csv` ledger covering every supplied lead and discovered candidate, with dispositions `included`, `merged`, `excluded`, or `unresolved`, a surviving plan ID, positive linkage evidence for merges, and a cited `evidence_url`. A header-only ledger is required when no candidates exist.
- Adds `verification_source_url` to the announcement output. The 43 business fields are unchanged; base columns move from 49 to 50.
- Accepts regulatory notices and credible attributed original reporting as event evidence when no issuer announcement exists. Blocked candidates require alternate public reporting or an unresolved disposition; inaccessible leads remain visible as coverage gaps.
- Requires evidence of an announced or implemented involuntary workforce reduction for workbook admission. Hiring pauses, automation forecasts, generic restructuring, and stand-alone voluntary offers remain in the candidate sidecar.
- Runs tracker seeding first. Search-log imports take `search_scope=event_lookup` or `window_sweep`; a known-event lookup no longer certifies annual coverage.
- Adds discovery and candidate audit outputs (`qa/candidate-review.json`, `review/fallback-tasks.json`). Content changes invalidate source-bound review receipts.
- Replaces `delivery_quality.py` and `semantic_receipts.py` with `delivery_review.py`; adds `discovery.py`, `candidate_review.py`, and `event_sources.py`; removes the bundled `reproducible-extraction.md` guidance in favour of the contract references.
- Filing extractor runtime 2.2.2 adds `filing_amount_followup.csv` targeted supplementary checks for issuers whose core amount is blank across the requested years, requires a source-bound second review for positive AI compensation, internal integration, and adoption decisions, and bundles the shared `layoffcore` and `layoff-hcm-tracker` vendor engine inside the skill.
- Existing 1.5.7-rc4 workspaces are not migrated silently. Start a fresh workspace and re-audit previous exports instead of relabelling them.

Verified: both skills compile; the 6 bundled discovery tests and 10 event-review tests pass; `init` and `discovery-plan` smoke tests complete. No live semantic rerun or new complete collection is claimed.

# Proposal-scope build

The filing extractor uses schema and output contract 1.5.1. Technology and infrastructure operating expenses remain in scope. This build removes the separate AI operating expense amount and keeps the existing AI investment fields. Start a fresh filing workspace.

# v1.5.7-rc4
Fixed an event audit import-order error. Internal technology measures require internal use. New event workspaces default to plan grain and fold implementation waves into their parent plans. Extensions require separate evidence review. Missing or invalid contracts produce explicit errors.

The rc3 contract path was correct. This release retains it and adds a test that loads the bundled asset.

Historical rc4 validation passed 37 regression tests, including corrected expectations for two internal adoption tests. An existing Kimi event workspace audited as PARTIAL with its original blockers. The historical run used existing sources and retained the rc3 schemas and contracts.

Historical release notes
# 1.5.7-rc4 comparative-audit candidate

- Semantic receipts accept the published `tech_evidence_contract.json` vocabulary (`use_context`: internal_operations | customer_product | both | unspecified; `adoption_stage`: planned | pilot | deployed_internal | deployed_customer | deployed_both | retired | unknown); legacy `internal` / `deployed` / `established_use` values are still read. Contract-compliant records no longer fail the receipt gate.
- Unify the negative finding: `not_separate` owes the same section-level `negative_review` receipt as `reviewed_absent`, in both the main validator and the receipt gate (one shared status set).
- One-sided thresholds (`more_than`, `at_least`, `less_than`, `at_most`, `up_to`) must store their bound (`_lower` / `_upper`) with `explicit_bound_basis`; a qualifier with no bound at all is a hard error, not a silent blank.
- A preserved `numerical_claim_raw` cannot coexist with `reviewed_absent` on every numeric quantity field, and `reviewed_absent` cannot carry a raw-claim value; both directions are hard errors.
- New `plan_granularity` init option (`announcement` default; `plan` folds `implementation_of` / `extension_of` links into the canonical group); audit reports `plan_count_by_relation`, `plan_rows` and `canonical_plan_count` so row count is never read as plan count.
- The delivery grain check (`audit_deliverables.py`) is wired into `export` and recorded in `qa/audit.json`; the review queue maps `semantic_receipts_v1` and `evidence_scope` gaps to real follow-up actions.
- Version drift fixed (README, review-closure titles, sources User-Agent, install.py, docs/validation.json marked historical). No schema, template or contract asset bytes changed; per-file measurement contract versions are listed in REVIEW_RELEASE.md.

Verified: 34 regressions; import/compile of both mirrored cores; init+audit smoke for both skills. See VALIDATION_RC3.json. No live semantic rerun is claimed; a fresh second-pass audit on real event data remains the acceptance test.

---

Historical entries below:

# 1.5.7-rc2 comparative-audit candidate

- Reject same-plan cycles and roots dated later than their known updates during audit/export.
- Validate linked targets for same_plan_update/extension_of and prohibit up_to bounds as point counts.
- Reject gzip transport bytes passed as source text rather than decoded HTML.
- Require textual no-candidate explanations; apply restructuring perimeter validation to zero as well as positive amounts.
- Add a read-only validator for actual saved Results workbooks and expected row grain.
- Focus guidance on event-time ownership, dates, internal cybersecurity/infrastructure, mixed AI incentive factors, accounting perimeters and genuine review completion.
- Schema/template/contract assets unchanged. No company answer is hard-coded. Not installed globally.

Verified: 20 regressions; two frontmatter checks; ten actual input workbook checks (eight expected passes, two Kimi expected rejections). Assets match rc1; mirrored cores match. No live semantic rerun is claimed.

---
Historical entries below:

# v1.5.6

- Transfer explicitly reviewed quantity bundles from updates to canonical rows.
- Bind selection to member decision hashes and invalidate changed groups.
- Rewrite exported related-plan references to canonical IDs and flag invalid targets.
- Flag observed relationships containing unresolved or unknown values.

# v1.5.5

- Export valid same-plan updates under their canonical plan and preserve update records in the evidence sidecar.
- Flag invalid plan links, unreconciled update quantities and oversized evidence before complete delivery.
- Add review instructions for restructuring scope, negative findings and WARN provenance.

# v1.5.4

- Export first and second review tasks, contract actions, coverage gaps and source failures in one resume queue.
- Keep strict event deliveries partial when asserted plan identities lack a resolved relationship review.
- Add operational rules for evidence reuse, missingness, amount adjudication, technology coding and merged review validation.

# v1.5.3 — Review closure and honest readiness

- Keep fixed English Results templates and all existing variables.
- Export workbook SHA-256, explicit runtime/schema versions, pending review queue, disclosure bounds and sidecar index.
- Event news no longer needs invented fiscal years to satisfy annual market-role checks; event search and identity checks remain separate.
- RQ2 local capability evidence is a partial descriptive prerequisite, not a certified reason-group contrast.
- Add source-review closure rules for null/zero, original-announcement search, plan identity, directional bounds, event-time denominators and fiscal/publication timing.
- Preserve multi-construct evidence while requiring project-level capability deduplication. Explain existing reason and typed-technology sidecars.
- Invalidate previous derived algorithm records (layered-v4); preserve source archives and decisions for revalidation.

Offline regression tests validate implementation, not universal semantic accuracy or complete public-source coverage. No existing research workbook is automatically corrected.

# Changelog

## 1.5.2 — 2026-11-03

- Preserve plan identity in company-year linkage summaries.
- Aggregate all source states conservatively, independent of input order. Mixed timing remains flagged; source units are retained.
- Join typed capability by entity, source and variable, deduplicating projects within each unit. Counts across exported rows must not be summed.
- Restrict human-human kappa and alpha to common held-out records.
- Business fields and workbook templates are unchanged. Workspace format compatibility does not imply measurement compatibility: rebuild linkage and human validation outputs before reuse.
- Real-world extraction accuracy, independent human validation and token savings have not been measured in this release.



## 1.5.1 — 2026-11-03

Correctness release. 1.5.0 shipped the measurement contracts but several of them could return a well-formed wrong answer; each item below was reproduced with a counter-example before it was fixed, and each now has a regression test in `regression_test.py`. No column, contract sidecar format or workspace version changes: the business fields stay 43/49 and 42/48, the contract versions stay where 1.5.0 put them, and an existing 1.5.0 workspace opens unchanged.

- Evidence-level linkage (`evidence-level-v2`). Classification now runs per `(variable, cited source)` instead of aggregating a company-year first, so a late AI exhibit can no longer borrow the publication date of an early annual report. Rows expose `pre_event_variables` and `contaminated_variables`; the capability join is `entity_id + source_id`. Same-day publication is `undetermined` unless the contract declares a convention.
- Qualification flag. `enters_primary_measure` reads the contract's own boolean instead of comparing a state name with `True`, so the flag is no longer always false and JSON, CSV and readiness agree.
- Upstream binding. Records carry a dependency fingerprint over `config.json`, `decisions.json`, `entities.json` and `sources.json` of both workspaces. Editing any of them and re-reading without rebuilding raises `stale_record`, names the changed file, and `audit` reports it as a gap. Applies to `reason_codebook`, `tech_evidence` and `linkage`.
- Prediction freeze. The freeze stores the canonical payload digest, the human-validation contract hash, the split digest and a source fingerprint. Editing a frozen value now fails with `prediction_freeze_mismatch` even when every key is unchanged; row order does not matter, and changing the design or the split assignment needs a new experiment id.
- Human validation metrics. κ and α compare two annotators across the records both coded (`coders_compared`), a single annotator returns `null` instead of crashing, splits are assigned by company or plan so one document cannot straddle development and held-out, every scored metric is held-out only, model-only statuses appear in the confusion matrix, an undefined class reports F1 = 0, and a second held-out claim for the same experiment is refused.
- Technology evidence. Cues became reading aids with three declared paths: `cue`, reviewed `semantic_review` (30+ character basis and a second reviewer) and reviewed `translation` (translated quote and a translation reviewer). AI fields refuse pure automation and cloud classes; a same-sentence qualifier keeps "we use AI in a limited pilot" a pilot instead of forcing a deployment; the stage vocabulary is checked for consistency rather than override.
- Capability summary. One unit per `project_id` (or one span when no project is declared), independent of input order, with `stage_conflicts`, `unknown_stage_units` and `retired_units` kept separate from `planned`/`pilot` rather than merged.
- Reason coding. An observed plan with neither a label nor a status is `labels_incomplete`; an empty set needs one of four `no_label_status` values plus notes. A primary reason needs ordering language in `primary_basis` and a `primary_basis_quote` located in a cited source. Labels may carry their own attribution, never stronger than the plan's. Unmatched categories go to `proposed_categories` with `pending_human_review` instead of becoming labels. `reason-apply` merges by plan instead of replacing the batch.
- Search coverage. The channel plan is declared (contract default, or `search_channel_plan` in the workspace). Coverage is reported per planned channel, with `missing_planned_channels` and a `planned_channel_not_searched` gate, so one searched channel cannot stand for four.
- Market routes. Required document roles are checked per company × fiscal year; `missing_years`, `sources_without_fiscal_year` and `company_years_satisfied` replace the company-level "has an annual report" answer.
- Readiness and orchestration. Five comparisons replace the single readiness verdict — `reason_description`, `financial_contrast`, `pre_event_capability`, `longitudinal_performance`, `job_skill_pairing` — each with its own sample and blockers; a present module with no comparable units is no longer `measurable`, and job–skill pairing is `not_available` at this scope. New `next-actions` command orders repairs deterministic-first. `audit` exposes `comparisons`.
- Tests: 298 offline tests pass (258 in 1.5.0), including 35 new regressions covering every reproduced defect.

Upgrade in place. Existing 1.5.0 workspaces open unchanged; sidecars built before this release will report `stale_record` until the affected command is rerun, which is the intended behaviour rather than a silent reuse.

## 1.5.0 — 2026-11-02

Measurement layer. The business columns are unchanged from 1.4.0 (43/49 and 42/48) and no contract adds a field; what changes is what the same cells are allowed to support. Contract assets are shipped in `assets/`, sidecars are written to `work/measurement/`, and each sidecar binds the contract hash, the schema version and its own payload hash.

- Add a seven-contract registry with `strict` (default) and `baseline` enforcement levels. `audit` now reports `measurement_contracts_pass`, `contract_gaps`, `research_readiness`, `weakest_link`, `human_validation` and `capability_inventory`, and COMPLETE requires no contract gap.
- Reason coding: nine fixed categories, four attribution levels derived from the event's `reason_attribution` decision, multi-label, one verbatim span per label. Cue, primary, exclusivity and null gates; `other_stated_reason` is exclusive. The `stated_reason_text` cell is never overwritten and no reason-code column is added.
- Technology evidence: six technology classes and seven adoption stages with per-field rules and six consistency rules. Generative AI needs a generative cue, cloud is not AI, and only `deployed_*` stages enter the capability table.
- Pre-event linkage: paired annual observations are classified `pre_event_public` / `retrospective` / `undetermined` by the carrying document's publication date and information period, never by the fiscal-year label. Excluded pairs are counted, not deleted.
- Human validation: freeze model predictions, annotate blind, evaluate once on a held-out split. Cohen's κ and nominal Krippendorff's α, class metrics with support and a minimum flag, and four status levels that decide what may be claimed. Without annotation the status is `not_executed` and no reliability is claimed.
- Search coverage: an executed-search registry separate from discovered events. Eight channels, five outcomes, window coverage with named uncovered intervals, and three gate reasons. A `none_found` search creates no pseudo-event and no zero row.
- Missingness: seven statuses and two denominators — review coverage and value availability — reported by variable, year and source type and never merged into one percentage. No zero filling.
- Entity registry and comparability: verified names with validity windows, parent links and cycle/overlap checks; period length, currency, consolidation scope and restatement version decide whether two years may be divided.
- Market document contracts for ten markets, checked per roster company and reported as document gaps only.
- Research readiness: RQ1–RQ3 report `measurable`, `partially_measurable` or `not_measurable` with explicit blockers, so an unanswerable question fails loudly instead of producing a number.
- Add reference documentation for every contract, blank input templates, and 176 new offline tests (258 total, from 82).

Upgrade in a new workspace. Existing 1.4 workspaces run unchanged at `--contract-level baseline`; `strict` will report the new contracts as gaps until the sidecars exist. Old decisions bind old definitions and must be reviewed rather than migrated.

## 1.4.0 — 2026-11-01

- Enforce English presentation across Results worksheet names, business values, company display names, reasons, criteria, missing-data explanations and evidence/review JSON. Add non-Latin leakage checks and an English roster display alias.
- Preserve canonical native-language evidence unchanged in a separate source-evidence sidecar. Require reviewed English quote translations with original-source hashes/offset semantics; never present translated text as verbatim original evidence.
- Replace labor_risk_discussion and its flag with mdna_hr_discussion and its flag. Cover the proposal's broad MD&A HR narrative while keeping labor-risk qualification separate. Annual scope remains 42 business fields; announcement scope remains 43.
- Clarify that actual established new-technology use qualifies without a first-adoption date. Cloud use alone is not AI adoption. Add bounded, hash-cached R&D and operational-technology review leads and a negative-counterevidence self-review check; leads never decide values automatically.
- Aggregate every distinct material AI risk in the existing broad risk field, with separate evidence passages. Do not stop at the first competitive-risk match or add unrequested subtype columns.
- Distinguish explicitly labeled R&D expense from mixed Technology and development expense, tax credits and tax-capitalized research balances. Preserve literal labels, years, units and scope.
- Reject one-sided censored thresholds stored as point estimates, and approximate counts with unsupported lower/upper bounds. Keep denominators and raw qualifiers.
- Allow event-time M&A and leadership context from reliable attributed event reporting; require a check of intervening updates rather than carrying stale annual-report context forward.
- Refresh English codebooks, templates, output contracts, first-use prompts and documentation. Retain company-neutral input, fixed output fields, nullable disclosure coding, source binding, genuine PARTIAL exports and independent-reliability boundaries.

Upgrade in a new workspace. Original source snapshots may be reconciled and reused, but old decisions require review against the changed definitions. The validation record identifies offline tests and the limited live primary-source checks; it does not claim a new complete collection across every company.

## 1.3.0

Fixed proposal-only output scope and company-neutral source routing based on the supplied v1.2.0 installation package. Historical project corpus counts are background rather than input requirements or run quotas.
