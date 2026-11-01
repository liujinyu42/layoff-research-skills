# Changelog

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
