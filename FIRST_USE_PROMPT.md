# First-use prompts for v3.0.3

## Layoff announcement tracker v3.0.3

Use the installed layoff-announcement-tracker for [ROSTER], [DATE_WINDOW] and [OUTPUT_DIRECTORY]. Use only the nine event research variables in assets/event_schema.json: employer-stated layoff reason, M&A activity, leadership transition, company history, firm size, founding year, products or services, business model, and known parties affected. Retain plan ID, company ID, company name and announcement date as row identifiers. Do not request, code or enrich any other analytical variable. Preserve original tracker receipts as source documents. Seek the original employer announcement, including SEC 8-K, 6-K or 10-Q where applicable, and record its URL and exact evidence separately. Use credible attributed reporting if the original is unavailable. For company context use dated issuer profiles available at the event. Firm size means employer workforce size; affected parties identifies roles, units or groups. Attribute reasons to the employer and leave unsupported fields null. An acquisition or leadership change alone does not establish a layoff motive. Use the existing discovery audit and batch export workflow. Export one English Results sheet per event workbook.

## Listed-company filing extractor v3.0.2

Use listed-filing-extractor v3.0.2 for listed issuers in [ROSTER], FY2019 through FY2025. Use [CONTACT_EMAIL] for SEC and [OUTPUT_DIR] for delivery. Verify listing, route official filings, review only assets/filing_schema.json fields, and export the bundled Results workbook and evidence sidecars. Keep missing amounts null.
