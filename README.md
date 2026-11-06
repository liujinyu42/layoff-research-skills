> Proposal-scope build based on 1.5.7-rc4. See the changelog for the filing scope change.

# Layoff Research Skills

This proposal-scope build derives from 1.5.7-rc4 and requires Python 3.10+. The filing schema and output contract are version 1.5.1. Start a fresh filing workspace to bind the updated schema.

## What 1.5.7-rc4 changes

- Semantic receipts accept the published `tech_evidence_contract.json` vocabulary (`use_context`: internal_operations | customer_product | both | unspecified; `adoption_stage`: planned | pilot | deployed_internal | deployed_customer | deployed_both | retired | unknown); legacy `internal` / `deployed` / `established_use` values are still read. Contract-compliant records are no longer judged as gaps.
- `not_separate` counts as a negative finding everywhere: it owes the same section-level `negative_review` receipt as `reviewed_absent`, in both the main validator and the receipt gate (one shared status set).
- A one-sided threshold (`more_than`, `at_least`, `less_than`, `at_most`, `up_to`) must carry its bound (`_lower` / `_upper`) with `explicit_bound_basis`; a qualifier with no bound at all is a hard error, not a silent blank.
- A preserved `numerical_claim_raw` cannot coexist with `reviewed_absent` on every numeric quantity field, and `reviewed_absent` cannot carry a raw-claim value; both are hard errors.
- New `plan_granularity` init option (`announcement` default, `plan` folds `implementation_of` / `extension_of` links into the canonical group); audit reports `plan_count_by_relation`, `plan_rows` and `canonical_plan_count` so row count is never read as plan count.
- The delivery grain check (`audit_deliverables.py`) is wired into `export` and its result is stored in `qa/audit.json`; new contract gaps get real follow-up actions in the review queue.

Reusable collection skills for any identified company. They obtain and refresh the requested information when invoked; they do not require the researcher's existing dataset or recreate its historical sample size.

| Skill | Fixed research output | Grain |
|---|---|---|
| layoff-announcement-tracker | Proposal Part 1's nine substantive variables plus essential event identity, size, dates and provenance (43 business fields) | Event/plan |
| listed-filing-extractor | Only the requested HR, AI/new-technology and financial categories (41 business fields) | Company/fiscal year |

The second identifier is retained for installation compatibility, and supports nonlisted, delisted and non-US companies too. Supply names directly or a roster; CIK/ticker are optional. Resolve legal entity, country and official identity. `source-plan` provides the SEC/official-local/issuer route; generic HTML/TXT/PDF imports cover actual authorized reports. Host search/browser discovery is required outside the native SEC route. Private or otherwise undisclosed data cannot be manufactured; preserve unavailable company-years and specific null reasons.

## Install

Extract either release archive and run from its root:

```bash
python3 -m pip install -r requirements.txt && python3 install.py --target workbuddy
```

Use --target workbuddy-ai or --target codex as needed. Existing same-name skills require --force after active tasks finish; they are backed up. --dry-run previews only. Manual copying must use the self-contained folders in the installation archive. Installation starts no collection/schedule. The source archive is ready for a GitHub repository; this release does not modify a live remote repository.

## Use

With S set to the desired skill folder and W a new workspace:

```bash
python "$S/scripts/research.py" init --work "$W" --company "Company name" --years 2019:2025
python "$S/scripts/research.py" source-plan --work "$W"
```

Follow each skill's workflow through real discovery, sync, finite reading/decision batches, supplementary sources, semantic self-review and export. The host agent performs judgments; scripts validate and retain them. Copy the [first-use prompt](prompts/first-run.en.md). Each installed skill contains its own prompt, codebook, blank input/output templates and runtime. No original author's files or chat memory are needed.

Both profiles select the same fixed set. Annual output: 15 texts + 15 disclosure flags + 11 numeric fields; no unrelated balance-sheet, cash-flow, leverage or ordinary CEO-pay extensions. Announcement output retains history/founding/products/business model as explicitly confirmed, but removes fixed eight reason codes and other unrequested extensions. Every workbook has exactly one Results sheet, 47 annual or 49 announcement base columns including identity/status/evidence, with lossless __partN continuations only when needed.

Disclosure codes, text and money are distinct. Zero disclosure needs complete applicable-source review; missing numbers never become zero. Keep original units, currency, fiscal periods, signs, locale separators, totals/components and event-time context. AI-linked compensation needs an explicit AI relation and recipient scope, not ordinary executive pay. A hash/offset pass is not semantic accuracy or human reliability. Incomplete/failed/conflicted work stays explicit PARTIAL. The complete actual variable list is in [OUTPUT_SCOPE.md](docs/OUTPUT_SCOPE.md); validation scope is in docs/validation.json.


## Measurement contracts (v1.5)

The columns did not change. What changed is what the same cells are allowed to support. Seven versioned contracts ship as assets, are enforced at `strict` (default) or `baseline`, and write content-addressed sidecars under `work/measurement/`:

| Contract | Question it settles | Where |
|---|---|---|
| reason_codebook | What did the company say, in which category, with whose attribution — nine categories, four levels, one span per label | announcement table |
| search_coverage | Was the company's window actually searched, or only an event found — eight channels, five outcomes, named uncovered intervals | announcement table |
| tech_evidence | Which technology, and is it a plan, a pilot or an operating deployment — six classes, seven stages | annual table |
| missingness | Not disclosed, or not yet reviewed — seven statuses and two denominators | annual table |
| linkage | Was the evidence public before the event — publication date and information period, never the fiscal-year label | both tables |
| human_validation | Has a blind human annotated a held-out split — freeze, annotate, score once | both tables |
| market_routes | Which documents does this market publish, and which legal entity is this row | both tables |

```bash
python "$S/scripts/research.py" contracts-status    --work "$W"
python "$S/scripts/research.py" contracts-scorecard --work "$W"
python "$S/scripts/research.py" readiness           --work "$W"
python "$S/scripts/research.py" next-actions        --work "$W"
```

`audit` separates evidence integrity from `measurement_contracts_pass`, `contract_gaps`, `research_readiness` (RQ1–RQ3), `comparisons` and `weakest_link`, and COMPLETE requires no contract gap. Editing a contract invalidates existing codes through the hash rather than leaving a stale claim; existing workspaces run unchanged at `--contract-level baseline`.

`readiness` reports five named comparisons instead of one composite score — `reason_description`, `financial_contrast`, `pre_event_capability`, `longitudinal_performance`, `job_skill_pairing` — each with its own sample size and blockers. `next-actions` turns the open gaps into an ordered list: deterministic repairs first, semantic comparisons last.

## What 1.5.6 fixes

Each item below was a reproducible defect in 1.5.0, demonstrated with a counter-example, and now has a regression test in `regression_test.py`:

| defect in 1.5.0 | what 1.5.6 does |
|---|---|
| A late AI exhibit borrowed an early annual report's publication date, because matching aggregated a company-year before filtering | Classification runs per `(variable, cited source)` unit (`evidence-level-v2`); the row carries `contaminated_variables`, and capability joins on `entity_id + source_id` |
| The row-level `enters_primary_measure` flag was always false | The flag reads the contract's own boolean, and JSON, CSV and readiness use the same function |
| A sidecar stayed valid after the decisions it described changed | Records carry an upstream dependency fingerprint; a changed `config`/`decisions`/`entities`/`sources` file raises `stale_record` and names it |
| A "frozen" prediction could be edited as long as the keys stayed | The freeze stores a canonical payload digest, contract hash, split digest and source fingerprint; changing a value is `prediction_freeze_mismatch` |
| κ crashed on a single record; metrics pooled splits; F1 divided by zero | κ aligns coders across records, metrics are held-out only, model-only labels enter the confusion table, F1 of an undefined class is 0 |
| A cue list acted as a hard classifier: pilots were upgraded, Chinese spans rejected, AI fields accepted pure automation | Three declared paths (`cue`, reviewed `semantic_review`, reviewed `translation`); AI fields refuse non-AI classes; a same-sentence qualifier keeps a pilot a pilot |
| Capability counts depended on input order and double-counted wording | One unit per `project_id`, order-independent, with `stage_conflicts` reported rather than smoothed |
| An empty label set passed silently, and a "primary" reason needed no textual basis | Empty sets need a declared status and notes; a primary needs ordering language plus a located quote; new categories wait for human review |
| readiness treated "module present" as a valid sample | Five comparisons with per-company/per-year intersections; no comparable year is `not_measurable`, and job–skill pairing is `not_available` at this scope |
| Market and search coverage were checked per company | Market requirements are checked per company × fiscal year; searches per declared channel plan |


## English output and v1.4 measurement fixes

All presented cells, including JSON explanations, use English. Native source evidence remains unchanged in a separate canonical archive; only reviewed translations appear in the English workbook and they are labeled translations. A verified English company display name can be supplied via `company_en`. Output validation rejects non-Latin authored text and checks every displayed cell; the reader still verifies English meaning. The worksheet name is Results.

The annual field pair labor_risk_discussion / labor_risk_discussion_disclosed is replaced by mdna_hr_discussion / mdna_hr_discussion_disclosed, at that release. MD&A personnel-cost narratives qualify without being recoded as labor risk. Established operational cloud/automation use may qualify as new-tech adoption without an invented first-use year. Explicit R&D notes and mixed technology functional costs remain distinct measures. The queues supply small cached source-linked leads for missed R&D/new-tech evidence; they never auto-code a finding. Event audits reject point-valued censored thresholds and bounds invented from approximate counts. Event-time M&A and leadership context can use reliable attributed reporting and requires checking intervening updates.

Create a new v1.5 workspace, or open a 1.4 workspace at `--contract-level baseline`; the contracts appear as gaps until their sidecars exist. Do not silently carry old definitions or self-review approvals forward. See [CHANGELOG](CHANGELOG.md), the [fixed output scope](docs/OUTPUT_SCOPE.md) and [validation scope](docs/validation.json). Same-model self-review does not guarantee that all semantic errors are absent, and no test here replaces reading the source. This release does not publish to GitHub or change installed skills automatically.
