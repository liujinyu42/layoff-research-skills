# Layoff Research Skills

Two reusable skills for building source-linked datasets on corporate layoffs and listed-company disclosures. They work in WorkBuddy, WorkBuddy AI, and Codex without an external output template or previous chat memory.

Current release: **v1.5.7-rc4 proposal-scope build** · Python **3.10+**

## What is included

| Skill | Purpose | Output grain |
|---|---|---|
| `layoff-announcement-tracker` | Finds distinct layoff announcements or plans, consolidates duplicate coverage, extracts company-stated reasons, event size and dates, company background, M&A and leadership context, and retains exact evidence. | One row per distinct event or plan |
| `listed-filing-extractor` | Extracts the proposal-scoped HR, AI/new-technology, and financial variables from annual reports, filings, incorporated proxy materials, and applicable official reports. | One row per company and fiscal year |

The skills accept listed, delisted, private, US, and non-US entities. A ticker or CIK helps but is not mandatory. The workflow verifies the legal entity and selects the applicable SEC, official-market, issuer-report, or imported-document route.

## Download

- [Installation package](two-skills-v1.5.7-rc4-proposal-scope.zip)
- [GitHub source package](layoff-research-skills-v1.5.7-rc4-github.zip)
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
2. A layoff-announcement date window.
3. The requested fiscal years.
4. A new absolute output-directory path.
5. A real SEC contact email when SEC sources apply.

Fiscal years are not assumed to be calendar years. Each entity and fiscal-year end must be verified. Start a fresh workspace for this proposal-scope build so an older schema or approval is not carried forward silently.

## Complete workflow

A completed run should continue through all of these stages:

1. Verify legal entities and filing identifiers.
2. Discover and collect applicable primary sources.
3. Parse documents and build evidence packets.
4. Extract all fixed proposal variables.
5. Preserve exact quotations and source metadata.
6. Complete source-based semantic self-review.
7. Check duplicate plans, fiscal-year alignment, comparative-period contamination, units, totals, and components.
8. Run measurement contracts and final delivery audits.
9. Export the workbooks and required sidecars.

Do not treat source collection, evidence packets, coding queues, or parser hits as a completed delivery. The host agent makes semantic judgments; deterministic scripts validate, retain, and audit them.

## Copy-ready example prompt

Paste the following prompt into WorkBuddy, WorkBuddy AI, or Codex:

```text
Use the installed v1.5.7-rc4 skills:

1. layoff-announcement-tracker
2. listed-filing-extractor

Companies:
- Amazon.com, Inc. (AMZN), United States, https://www.amazon.com.
- International Business Machines Corporation (IBM), United States, https://www.ibm.com.

Layoff announcement window: 2022-01-01 through 2024-12-31.
Fiscal years: FY2022, FY2023, and FY2024.
Output directory: /Users/liujinyu/Desktop/layoff-research-amazon-ibm-fy2022-2024.
SEC contact email: liujy_0514@163.com.

Verify both legal entities, tickers, exchanges, filing identifiers, official websites, and fiscal-year ends before collection. Preserve each company's actual fiscal-year dates; do not treat fiscal years as calendar years without verification.

Follow only the definitions, schemas, templates, measurement contracts, review procedures, and workflows bundled with the installed skills. Do not rely on previous chat history, remembered values, or external output templates.

Complete source discovery, document acquisition, extraction, exact-evidence preservation, semantic self-review, cross-source and cross-year checks, measurement review, final audit, and Excel export. Do not stop after preparing evidence packets, coding tasks, or review queues.

Deliver:

1. 1_layoff_announcements.xlsx
   Create one row per distinct layoff event or plan announced from 2022-01-01 through 2024-12-31. Keep genuinely separate plans separate. Consolidate repeated news coverage, implementation updates, revised estimates, and duplicate sources referring to the same plan.

2. 2_listed_company_filings.xlsx
   Create exactly six company-fiscal-year rows: two companies multiplied by three fiscal years. Preserve every row when a variable is unavailable and explain each missing, unresolved, inapplicable, or separately undisclosed value.

For annual disclosures, cover only the fixed proposal scope:
- HR and layoffs: workforce size; training and development costs; labor and talent risks; talent competition and hiring risks; MD&A human-capital discussion; restructuring and cost-saving narratives.
- AI and new technology: AI products and initiatives; internal AI integration; AI adoption; AI-related risk factors; AI investment; technology and infrastructure operating expense; R&D expense; capitalized software-development costs.
- Financial performance: revenue; operating income; restructuring charges; total compensation expense; AI-related executive compensation.

Distinguish company-stated reasons from third-party interpretations; generative AI from other AI, automation, cloud, and general digital transformation; plans and pilots from deployed technology; internal operations from customer-facing products; AI-specific amounts from mixed technology spending; current-year figures from comparative-year figures; and company-wide totals from components.

Use 1 only when qualifying evidence satisfies the bundled definition. Use 0 only after a completed, source-supported negative-disclosure review across all applicable sources. Keep unavailable, unresolved, inapplicable, and separately undisclosed amounts null with specific English reasons. Do not invent values or substitute proxies.

Prioritize company announcements, SEC filings, annual reports, proxy statements, financial-statement notes, MD&A, risk factors, and official investor-relations materials. Clearly label secondary evidence when primary evidence cannot establish an announcement fact.

Preserve original sources and exact evidence separately. Run all bundled semantic, measurement, consistency, and delivery audits. Check duplicate events, plan consolidation, fiscal-year alignment, comparative-period contamination, total-versus-component errors, amount and unit errors, false zeros, unsupported binary coding, missing proposal variables, and internal contradictions.

Each workbook must contain exactly one worksheet named Results, use only the bundled columns in the bundled order, and contain English-only displayed content, explanations, statuses, and review notes. Export genuine PARTIAL results when necessary and identify unfinished items precisely. Do not claim independent human reliability without independent human annotations.

Include all required evidence, measurement, review, and audit sidecars. Finish with a concise English summary listing events by company, coverage of all six company-years, missing or unresolved variables and reasons, audit results, remaining limitations, and absolute paths to both workbooks and supporting files.
```

For other companies or periods, use the [generic first-use prompt](FIRST_USE_PROMPT.md) and replace its bracketed inputs.

## Expected delivery

```text
<output-directory>/
├── 1_layoff_announcements.xlsx
├── 2_listed_company_filings.xlsx
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

See [OUTPUT_SCOPE.md](OUTPUT_SCOPE.md) for the exact fields. Unrelated balance-sheet, cash-flow, leverage, and ordinary CEO-pay extensions are intentionally excluded.

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

Advanced users may initialize a fresh workspace directly:

```bash
python "$S/scripts/research.py" init --work "$W" --company "Company name" --years 2022:2024
python "$S/scripts/research.py" source-plan --work "$W"
```

These commands only initialize the workspace and source plan. Continue through discovery, synchronization, decisions, semantic review, measurement, audit, and export.

## v1.5.7-rc4 highlights

- Accepts the published technology-evidence vocabulary while retaining legacy compatibility.
- Applies the same negative-review requirement to `not_separate` and `reviewed_absent`.
- Rejects one-sided numeric thresholds without explicit bounds and contradictory raw numeric claims.
- Adds configurable announcement-versus-plan granularity and reports row, relation, plan, and canonical-plan counts separately.
- Runs the delivery-grain audit during export and saves it in `qa/audit.json`.
- Creates actionable follow-up items for genuine contract gaps.

See [CHANGELOG.md](CHANGELOG.md) for the full release history.

## Limitations

- The skills use public evidence and cannot manufacture private or undisclosed information.
- Host browser or search access may be required outside the native SEC route.
- Availability and disclosure practices vary by company, market, language, and year.
- Same-model self-review improves consistency but does not replace blind independent human validation.
- A passing technical audit does not prove every source statement was interpreted correctly; high-risk measurements still warrant source reading.

## Reproducibility

When using generated data in research, retain the skill version, original source sidecars, measurement-contract hashes, semantic-review records, and audit outputs so the extraction can be reproduced and reviewed.
