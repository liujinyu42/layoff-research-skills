# First-use prompt

Copy the text below and replace the bracketed inputs.

```text
Use the installed v2.3.1 event tracker and the v2.2.2 annual-disclosure extractor.

Companies: [legal company names, country or website if ambiguous].
Aliases: [verified historical or common names, separated by semicolons, or "none"].
Event window: [start date to end date].
Fiscal years: [years].
Output folder: [absolute folder path].
SEC contact, when applicable: [contact name and email].

Follow the bundled schemas, definitions, and blank templates. Verify legal entities, aliases, and official sources. Accept public, private, and non-US inputs without inventing identifiers or unavailable disclosures.

Run discovery-plan, execute its broad company-and-year queries with the available search tools, save the actual result captures, and run discovery-import. Reconcile every relevant result in event_candidate_review.csv using one of included, merged, excluded, or unresolved. Resolve blocked pages through alternate public reporting. Complete source-bound disposition reviews. Include discovery, candidate, and fallback sidecars in the delivery.

Deliver the two Excel workbooks named by the installed templates. Each workbook must contain exactly one Results worksheet, use only the bundled fields in the bundled order, and keep all displayed text in English.

For every issuer whose core amount is blank across all requested years, run and record a targeted supplementary check in the amount follow-up ledger. For every positive AI compensation, internal integration, and adoption decision, re-read the exact supporting excerpt and document the entity, action, period, and scope in the second-review record.

Complete source discovery, extraction, exact-evidence preservation, semantic self-review, consistency checks, measurement review, final audit, and export. Do not stop after preparing evidence packets or review queues. Report audit results, remaining limitations, and absolute file paths in English.
```
