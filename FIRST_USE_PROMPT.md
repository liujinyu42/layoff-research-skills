# First-use prompt

Copy the text below and replace the bracketed inputs. No original research dataset or output template is needed.

```text
Use layoff-announcement-tracker v2.3.1. Use listed-filing-extractor v2.2.2 if annual extraction is requested.
Companies: [legal company names, country/website if ambiguous].
Aliases: [verified historical or common names, separated by semicolons, or "none"].
Announcement window: [2020-01-01 to 2026-09-30, or my chosen dates].
Fiscal years: [2019 through 2025, or my chosen years].
Output folder: [absolute folder path].
SEC contact, when applicable: [my real contact name/email; use my existing SEC_USER_AGENT if configured].

Follow the skills' bundled schemas, definitions and blank templates. Verify the legal entities, aliases and official sources; accept private, delisted and non-US inputs without inventing a CIK or unavailable disclosures. The proposal's historical sample sizes are background, not this run's quota.

Execute discovery-plan, use the host search tools for its broad company/year queries, preserve actual result captures, and run discovery-import. Reconcile each relevant result in event_candidate_review.csv using its generated ID and one of included, merged, excluded or unresolved. Resolve blocked pages through alternate public reports before profile enrichment. Run candidate-review-prepare and complete source-bound disposition reviews. A verified local notice can establish an event even if its relationship to a wider plan remains unknown. Include discovery, candidate and fallback sidecars in the delivery.

Deliver 1_layoff_announcements.xlsx and 2_listed_company_filings.xlsx. Each must contain exactly one Results worksheet, one event/plan or company/fiscal-year per row, and only the fixed proposal fields plus basic identity/status/evidence. Make every displayed cell, narrative, reason, missing explanation and review note English. Keep native source evidence unchanged in the separate canonical archive, with reviewed English translations and original-source provenance in the workbook.

For every issuer whose core amount is blank across all requested years, run and record a targeted supplementary check in filing_amount_followup.csv. For every positive AI compensation, internal integration and adoption decision, re-read the exact supporting excerpt and document entity, action, period and scope in the second-review record.

Read the applicable sources and complete the extraction and substantive self-review loops. Check operational technology use even without a first-adoption date; distinguish explicit R&D from mixed technology expenses; do not turn ordinary MD&A personnel costs into labor risk. Preserve event count/percentage qualifiers and event-time context. Never substitute components, prior years, future plans, ordinary CEO pay or missing values for the requested totals/AI measures. Treat parser/search hits as candidates, not findings. Preserve genuine missing amounts and unresolved dependencies, and state PARTIAL when blocked. Summarize coverage, actual corrections and remaining gaps in English. Do not ask me to fill intermediate coding JSON.

Keep the measurement contracts on their default `strict` level and report what they say. Code stated reasons with the shipped nine-category book and never overwrite the stated_reason_text cell; record executed searches separately from discovered events so an empty window is not read as "no layoffs"; tag technology evidence with a class and an adoption stage so a plan is not reported as a capability; classify paired annual observations by publication date and information period rather than fiscal-year label; report review coverage and value availability as two separate ratios; and state the human-validation status as it is, including `not_executed`. Report `audit`, `readiness` and any contract gap in the final summary instead of working around it.
```
