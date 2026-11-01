# First-use prompt

Copy the text below and replace the bracketed inputs. No original research dataset or output template is needed.

```text
Use layoff-announcement-tracker and listed-filing-extractor.
Companies: [legal company names, country/website if ambiguous].
Announcement window: [2020-01-01 to 2026-09-30, or my chosen dates].
Fiscal years: [2019 through 2025, or my chosen years].
Output folder: [absolute folder path].
SEC contact, when applicable: [my real contact name/email; use my existing SEC_USER_AGENT if configured].

Follow the skills' bundled schemas, definitions and blank templates. Verify the legal entities and official sources; accept private, delisted and non-US inputs without inventing a CIK or unavailable disclosures. The proposal's historical sample sizes are background, not this run's quota.

Deliver 1_layoff_announcements.xlsx and 2_listed_company_filings.xlsx. Each must contain exactly one Results worksheet, one event/plan or company/fiscal-year per row, and only the fixed proposal fields plus basic identity/status/evidence. Make every displayed cell, narrative, reason, missing explanation and review note English. Keep native source evidence unchanged in the separate canonical archive, with reviewed English translations and original-source provenance in the workbook.

Read the applicable sources and complete the extraction and substantive self-review loops. Check operational technology use even without a first-adoption date; distinguish explicit R&D from mixed technology expenses; do not turn ordinary MD&A personnel costs into labor risk. Preserve event count/percentage qualifiers and event-time context. Never substitute components, prior years, future plans, ordinary CEO pay or missing values for the requested totals/AI measures. Treat parser/search hits as candidates, not findings. Preserve genuine missing amounts and unresolved dependencies, and state PARTIAL when blocked. Summarize coverage, actual corrections and remaining gaps in English. Do not ask me to fill intermediate coding JSON.
```
