# Layoff Research Skills

Two reusable skills for building source-linked datasets on corporate layoffs and listed-company disclosures. They work in WorkBuddy, WorkBuddy AI, and Codex without an external output template or previous chat memory.

Current release: **v2.3.1** · Runtime 2.3.1 (`layoff-announcement-tracker`) and 2.2.2 (`listed-filing-extractor`) · Python **3.10+**

## What is included

| Skill | Purpose | Output grain |
|---|---|---|
| `layoff-announcement-tracker` | Discovers and verifies layoff events from public trackers, Google-discoverable pages, regulatory notices, and original reporting. Reconciles every candidate in a disposition ledger, deduplicates plans, extracts company-stated reasons, event size and dates, company background, M&A and leadership context, and retains exact evidence with a cited verification URL. | One row per distinct event or plan |
| `listed-filing-extractor` | Extracts the proposal-scoped HR, AI/new-technology, and financial variables from annual reports, filings, incorporated proxy materials, and applicable official reports. Adds a targeted amount follow-up ledger when core amounts are blank. | One row per company and fiscal year |

The skills accept listed, delisted, private, US, and non-US entities. A ticker or CIK helps but is not mandatory. The workflow verifies the legal entity and selects the applicable SEC, official-market, issuer-report, or imported-document route.

## Download

- [Installation package](two-skills-v2.3.1-install.zip)
- [GitHub source package](layoff-research-skills-v2.3.1-github.zip)
- [Generic first-use prompt](FIRST_USE_PROMPT.md)
- [Exact output scope](OUTPUT_SCOPE.md)
- [Changelog](CHANGELOG.md)

## Quick installation

Download and extract the installation package, open a terminal in the extracted folder, and run:

```bash
python3 -m pip install -r requirements.txt
python3 install.py --target workbuddy
```

Other supported targets:

```bash
python3 install.py --target workbuddy-ai
python3 install.py --target codex
```

Preview or replace an older installation:

```bash
python3 install.py --target codex --dry-run
python3 install.py --target codex --force
```

The installer backs up an existing same-name skill. Installation does not start collection or create a scheduled task.

## Information required for a run

Prepare:

1. Legal company names, plus tickers, countries, and official websites when available.
2. Verified historical or common-name aliases for discovery, separated by semicolons.
3. A layoff-announcement date window.
4. The requested fiscal years.
5. A new absolute output-directory path.
6. A real SEC contact email when SEC sources apply.

Fiscal years are not assumed to be calendar years. Each entity and fiscal-year end must be verified. Start a fresh workspace for this release so an older schema or approval is not carried forward silently.

## Complete workflow

A completed run should continue through all of these stages:

1. Verify legal entities, aliases, and filing identifiers.
2. Build the discovery plan and execute its per-company, per-year queries.
3. Preserve actual search captures and import them into the discovery inbox.
4. Reconcile every supplied lead and discovered candidate in the candidate ledger.
5. Collect and register applicable primary sources.
6. Parse documents and build evidence packets.
7. Extract all fixed proposal variables.
8. Preserve exact quotations and source metadata.
9. Complete source-based semantic self-review.
10. Check duplicate plans, fiscal-year alignment, comparative-period contamination, units, totals, and components.
11. Run measurement contracts and final delivery audits.
12. Export the workbooks and required sidecars.

Discovery is not optional. A known-event lookup does not establish annual coverage, and a search hit is a candidate rather than a finding. Do not treat source collection, evidence packets, coding queues, or parser hits as a completed delivery. The host agent makes semantic judgments; deterministic scripts validate, retain, and audit them.

## Copy-ready example prompt

Paste the following prompt into WorkBuddy, WorkBuddy AI, or Codex:

```text
Use the installed v2.3.1 skills:

1. layoff-announcement-tracker (runtime 2.3.1)
2. listed-filing-extractor (runtime 2.2.2)

Companies:
- Amazon.com, Inc. (AMZN), United States, https://www.amazon.com.
- International Business Machines Corporation (IBM), United States, https://www.ibm.com.

Aliases: [verified historical or common names, separated by semicolons, or "none"].

Layoff announcement window: 2022-01-01 through 2024-12-31.
Fiscal years: FY2022, FY2023, and FY2024.
Output directory: /Users/liujinyu/Desktop/layoff-research-amazon-ibm-fy2022-2024.
SEC contact email: liujy_0514@163.com.

Verify both legal entities, tickers, exchanges, filing identifiers, official websites, and fiscal-year ends before collection. Preserve each company's actual fiscal-year dates; do not treat fiscal years as calendar years without verification.

Follow only the definitions, schemas, templates, measurement contracts, review procedures, and workflows bundled with the installed skills. Do not rely on previous chat history, remembered values, or external output templates.

Run discovery-plan, execute its broad company-and-year queries with the available search tools, save the actual result captures, and import them with discovery-import. Reconcile every relevant hit and every supplied lead in event_candidate_review.csv with a disposition of included, merged, excluded, or unresolved. Resolve blocked pages through alternate public reporting before enriching company profiles. Run candidate-review-prepare and complete source-bound disposition reviews. A regulator notice or credible attributed report can establish an event without a separate issuer announcement.

Complete source discovery, document acquisition, extraction, exact-evidence preservation, semantic self-review, cross-source and cross-year checks, measurement review, final audit, and Excel export. Do not stop after preparing evidence packets, coding tasks, or review queues.

Deliver:

1. 1_layoff_announcements.xlsx
   Create one row per distinct layoff event or plan announced from 2022-01-01 through 2024-12-31. Keep genuinely separate plans separate. Consolidate repeated news coverage, implementation updates, revised estimates, and duplicate sources referring to the same plan. Supply a cited verification_source_url for every included event.

2. 2_listed_company_filings.xlsx
   Create exactly six company-fiscal-year rows: two companies multiplied by three fiscal years. Preserve every row when a variable is unavailable and explain each missing, unresolved, inapplicable, or separately undisclosed value.

For annual disclosures, cover only the fixed proposal scope:
- HR and layoffs: workforce size; training and development costs; labor and talent risks; talent competition and hiring risks; MD&A human-capital discussion; restructuring and cost-saving narratives.
- AI and new technology: AI products and initiatives; internal AI integration; AI adoption; AI-related risk factors; AI investment; technology and infrastructure operating expense; R&D expense; capitalized software-development costs.
- Financial performance: revenue; operating income; restructuring charges; total compensation expense; AI-related executive compensation.

Write filing_amount_followup.csv in the workspace root. For every issuer whose core amount is blank across all requested years, record the source, section or table, fiscal period, and result of a targeted supplementary check. Use a header-only ledger when no check triggers.

Distinguish company-stated reasons from third-party interpretations; generative AI from other AI, automation, cloud, and general digital transformation; plans and pilots from deployed technology; internal operations from customer-facing products; AI-specific amounts from mixed technology spending; current-year figures from comparative-year figures; and company-wide totals from components.

Use 1 only when qualifying evidence satisfies the bundled definition. Use 0 only after a completed, source-supported negative-disclosure review across all applicable sources. Keep unavailable, unresolved, inapplicable, and separately undisclosed amounts null with specific English reasons. Do not invent values or substitute proxies.

Prioritize company announcements, SEC filings, annual reports, proxy statements, financial-statement notes, MD&A, risk factors, and official investor-relations materials. Clearly label secondary evidence when primary evidence cannot establish an announcement fact.

Preserve original sources and exact evidence separately. Run all bundled semantic, measurement, consistency, and delivery audits. Check duplicate events, plan consolidation, fiscal-year alignment, comparative-period contamination, total-versus-component errors, amount and unit errors, false zeros, unsupported binary coding, missing proposal variables, and internal contradictions.

Each workbook must contain exactly one worksheet named Results, use only the bundled columns in the bundled order, and contain English-only displayed content, explanations, statuses, and review notes. Export genuine PARTIAL results when necessary and identify unfinished items precisely. Do not claim independent human reliability without independent human annotations.

Include all required discovery, candidate, evidence, measurement, review, and audit sidecars. Finish with a concise English summary listing events by company, coverage of all six company-years, missing or unresolved variables and reasons, audit results, remaining limitations, and absolute paths to both workbooks and supporting files.
```

For other companies or periods, use the [generic first-use prompt](FIRST_USE_PROMPT.md) and replace its bracketed inputs.

## Expected delivery

```text
<output-directory>/
├── 1_layoff_announcements.xlsx
├── 2_listed_company_filings.xlsx
├── event_candidate_review.csv
├── filing_amount_followup.csv
├── discovery/      planned queries, search captures, and candidate inbox
├── evidence/       original and exact source evidence
├── measurement/    contract receipts and measurement sidecars
├── review/         semantic-review records and follow-up queues
└── qa/             audit and readiness outputs
```

Each workbook contains exactly one worksheet named `Results`:

- Announcement workbook: one distinct event or plan per row.
- Filing workbook: one company and fiscal year per row.
- Displayed values, explanations, statuses, and review notes are English.
- Native evidence remains unchanged in the canonical evidence archive; reviewed English translations are labeled.
- Lossless `__partN` continuation fields appear only when Excel cell limits require them.

The announcement workbook keeps 43 business fields in 50 base columns; the filing workbook keeps 41 business fields in 47 base columns. Both counts include stable identifiers, status fields, and exact evidence — not additional business variables.

See [OUTPUT_SCOPE.md](OUTPUT_SCOPE.md) for the exact fields. Unrelated balance-sheet, cash-flow, leverage, and ordinary CEO-pay extensions are intentionally excluded.

## Candidate reconciliation

Every supplied reference lead and every discovered candidate receives an English disposition in `event_candidate_review.csv`:

| Column | Meaning |
|---|---|
| `candidate_id` | Stable ID from the discovery inbox or supplied lead |
| `company` | Verified company or operating unit |
| `reported_date` | Reported or announcement date |
| `source_url` | Candidate URL |
| `affected_scope` | Reported entity and population scope |
| `disposition` | `included`, `merged`, `excluded`, or `unresolved` |
| `plan_id` | Surviving plan ID for included or merged records |
| `evidence_url` | Cited verification source |
| `reason` | English justification and linkage evidence |

Merges require positive linkage evidence, not equal dates or equal counts. A dead link requires alternate-source discovery or an unresolved disposition. Hiring pauses, automation forecasts, generic restructuring, and stand-alone voluntary offers remain in the sidecar rather than the layoff workbook. An unresolved material candidate requires `PARTIAL`.

## Understanding 1, 0, null, and PARTIAL

- `1`: qualifying evidence satisfies the bundled definition.
- `0`: all required applicable sources were reviewed and support a negative-disclosure conclusion.
- Blank/null: unavailable, unresolved, inapplicable, separately undisclosed, or not defensibly measurable; the status and reason remain explicit.
- `PARTIAL`: genuine results were exported, but a required search, review, measurement, or dependency remains incomplete.

Missing values must not be replaced with components, comparative-year amounts, future plans, general technology spending, ordinary executive pay, or invented proxies.

## Measurement contracts and self-review

| Contract | Purpose |
|---|---|
| `reason_codebook` | Attributes company-stated reasons using located evidence and a fixed nine-category codebook. |
| `search_coverage` | Separates searches executed from events discovered and records uncovered intervals. |
| `tech_evidence` | Distinguishes technology classes, plans, pilots, and operational deployments. |
| `missingness` | Separates non-disclosure from incomplete review and reports distinct coverage denominators. |
| `linkage` | Uses publication date and information period, not the fiscal-year label alone. |
| `human_validation` | Records whether blind independent human annotation was actually performed. |
| `market_routes` | Validates the document route and legal entity for each market and company-year. |

Useful status commands, with `S` as the installed skill folder and `W` as the workspace:

```bash
python "$S/scripts/research.py" contracts-status --work "$W"
python "$S/scripts/research.py" contracts-scorecard --work "$W"
python "$S/scripts/research.py" readiness --work "$W"
python "$S/scripts/research.py" next-actions --work "$W"
```

The audit separates evidence integrity, measurement-contract status, research readiness, comparison readiness, and the weakest unresolved link. A parser match, hash check, or same-model review is not independent human reliability.

## Direct command-line entry point

Advanced users may initialize a fresh workspace and build the discovery plan directly:

```bash
python "$S/scripts/research.py" init --work "$W" --company "Company name" --years 2022:2024
python "$S/scripts/research.py" source-plan --work "$W"
python "$S/scripts/research.py" discovery-plan --work "$W"
python "$S/scripts/research.py" discovery-import --work "$W" --file "$W/discovery/batch.json"
python "$S/scripts/research.py" candidate-review-prepare --work "$W"
```

These commands initialize the workspace, register planned searches, and prepare review tasks. Continue through discovery, synchronization, decisions, semantic review, measurement, audit, and export.

## v2.3.1 highlights

- Adds a snapshot-backed discovery plan with broad per-company, per-year query families built from verified aliases.
- Adds `discovery-import`, `discovery-status`, and `candidate-review-prepare` commands with a preserved search-result inbox.
- Requires an English candidate ledger (`event_candidate_review.csv`) covering every supplied lead and discovered candidate.
- Accepts regulatory notices and credible attributed reporting as event evidence, while keeping inaccessible leads visible as coverage gaps.
- Adds the `verification_source_url` provenance field so every included event carries a cited verification URL.
- Keeps the announcement scope at 43 business fields and the filing scope at 41 business fields; no new business columns were added.
- Requires a targeted `filing_amount_followup.csv` check when an issuer's core amount is blank across all requested years.
- Requires a source-bound second-review record for positive AI compensation, internal integration, and adoption decisions.
- Bundles the shared research core and vendor engine inside each skill, so installation no longer needs separate `shared/` or `engine/` folders.

See [CHANGELOG.md](CHANGELOG.md) for the full release history.

## Limitations

- The skills use public evidence and cannot manufacture private or undisclosed information.
- Host browser or search access may be required outside the native SEC route.
- Search receipts document the observed search process; they do not establish exhaustive worldwide event recall.
- Availability and disclosure practices vary by company, market, language, and year.
- Same-model self-review improves consistency but does not replace blind independent human validation.
- A passing technical audit does not prove every source statement was interpreted correctly; high-risk measurements still warrant source reading.

## Reproducibility

When using generated data in research, retain the skill version, original source sidecars, measurement-contract hashes, semantic-review records, and audit outputs so the extraction can be reproduced and reviewed.
