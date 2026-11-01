# Layoff Research Skills

**v1.4.0 — English output, proposal-focused variables, source-linked self-review.**

Two reusable skills collect layoff announcements and company annual disclosures for research. Supply your own company names and periods. No original author's dataset, prior chat memory or external output template is required. Listed, private, delisted and non-US companies can be inputs; actual coverage depends on accessible public disclosures.

| Skill | What it collects | Output |
|---|---|---|
| `layoff-announcement-tracker` | Layoff announcements, stated reasons, affected parties, M&A and leadership context, company history, founding year, workforce size, products/services and business model | One event/plan per row; 43 business fields |
| `listed-filing-extractor` | HR practices and layoff disclosures, AI/new-technology adoption and investment, and specified financial metrics | One company/fiscal year per row; 42 business fields |

The annual skill's historical name is retained for compatibility. A US listing, ticker or CIK is not mandatory. SEC discovery is supported when applicable; other companies use verified issuer/local official sources discovered by the host agent and imported as HTML, text or PDF.

## Install with one command

Requires Python 3.10+ and a host that supports local skills. The installer downloads the checksum-verified v1.4.0 source, creates an isolated Python runtime, installs dependencies and installs both skills. It starts no collection or scheduled task.

**WorkBuddy (macOS/Linux)**

```bash
curl -fsSL https://raw.githubusercontent.com/liujinyu42/layoff-research-skills/main/quick_install.py -o quick_install.py && python3 quick_install.py --target workbuddy
```

**WorkBuddy AI (macOS/Linux)**

```bash
curl -fsSL https://raw.githubusercontent.com/liujinyu42/layoff-research-skills/main/quick_install.py -o quick_install.py && python3 quick_install.py --target workbuddy-ai
```

**Codex (macOS/Linux)**

```bash
curl -fsSL https://raw.githubusercontent.com/liujinyu42/layoff-research-skills/main/quick_install.py -o quick_install.py && python3 quick_install.py --target codex
```

**Windows PowerShell**

```powershell
Invoke-WebRequest 'https://raw.githubusercontent.com/liujinyu42/layoff-research-skills/main/quick_install.py' -OutFile quick_install.py
py -3 quick_install.py --target workbuddy
```

For upgrades, stop tasks using the old skills, then add `--force`. Existing skill folders are backed up. `--dry-run` previews the installation. Refresh the host's skills or reopen the host after installation. Use a new v1.4 workspace because definitions and presentation rules changed; reconcile reusable source snapshots explicitly.

### Download and manual installation

- [Self-contained installation ZIP](two-skills-v1.4.0-install.zip): extract it, open a terminal at its root, then run the command below. Its two skill folders may also be copied manually into your host's skills directory.
- [Complete source ZIP](layoff-research-skills-v1.4.0-github.zip): runtime, source code, tests, schemas, definitions and templates. Extract it to inspect or develop the project.
- [Checksums](SHA256.json), [changelog](CHANGELOG.md), [validation scope](VALIDATION.json).

```bash
python3 -m pip install -r requirements.txt
python3 install.py --target workbuddy
```

Run these commands inside an extracted package, not the repository's download-only root. Supported targets are `workbuddy`, `workbuddy-ai` and `codex`.

## First run

Paste this into your host after installation. Replace the brackets with your inputs; no original workbook is needed.

```text
Use layoff-announcement-tracker and listed-filing-extractor.
Companies: [legal names and countries/websites if ambiguous].
Announcement window: [start date to end date].
Fiscal years: [2019 through 2025, or my selected years].
Output folder: [absolute output folder].
SEC contact when applicable: [my real name/email, or configured SEC_USER_AGENT].

Use the skills' built-in definitions and templates. Verify company identities and
sources. Collect the fixed proposal variables, complete source-based decisions
and substantive self-review, and export both Excel files entirely in English.
Each file must contain exactly one Results worksheet, with one event/plan or
company/fiscal-year per row. Preserve genuine missing values and explicit reasons.
Label unfinished dependencies PARTIAL. Keep original-language evidence unchanged
in the canonical archive and use reviewed English translations in the workbook.
Summarize coverage, corrections and remaining gaps in English.
```

The [full first-use prompt](FIRST_USE_PROMPT.md) is also embedded in each skill. Users request companies and periods; the host agent performs discovery, reading and coding. The Python runtime validates and stores judgments. It does not contain an autonomous paid LLM service, and installation alone does not start scraping.

## Annual disclosure coverage

| Category | Measures |
|---|---|
| HR practices and layoffs | Workforce size; training/development cost text and amount; layoff disclosure; labor/talent risk; competition/hiring risk; MD&A HR discussion; restructuring/cost-saving narrative |
| AI and new technology | AI products/initiatives; internal AI integration; actual AI adoption; new-technology use; all distinct AI-related risks; AI investment text/amount; AI operating expense; technology/infrastructure operating-cost text/amount; R&D expense; capitalized software text/current-year additions |
| Financial performance | Revenue; operating income; restructuring expense; company-wide total compensation expense; explicitly AI-linked compensation, including executive awards |

The fixed annual scope contains 15 text constructs, 15 nullable disclosure flags and 12 numeric fields. It excludes unrelated balance-sheet, cash-flow, leverage and ordinary CEO-pay extensions. [Complete output dictionary](OUTPUT_SCOPE.md).

## Output and evidence

- `1_layoff_announcements.xlsx`: one verified event/plan per row, 49 base columns including identifiers/status/evidence.
- `2_listed_company_filings.xlsx`: one company/fiscal-year per row, 48 base columns including identifiers/status/evidence.
- Each workbook contains one `Results` sheet. All displayed narratives, reasons and JSON metadata are English. Long evidence continues horizontally in `__partN` columns without truncation or extra observations.
- Original-language evidence is preserved in the canonical `.source_evidence.json` archive. Reviewed translations are labeled translations; offsets and source hashes still identify original text.
- `1` means qualifying disclosure. `0` requires completed review of all applicable sources. Null distinguishes unavailable, unquantified, inapplicable or unresolved data through recorded status. A missing monetary amount never becomes zero automatically.

## What changed in v1.4.0

English presentation is now enforced. Broad MD&A HR discussion uses `mdna_hr_discussion`, separate from labor risk. Established operational cloud use can qualify as new-technology use without an invented first-adoption date; cloud alone does not prove AI adoption. Explicit R&D expense is distinguished from mixed Technology and development costs. All distinct AI risks are retained in the existing broad risk field. Event checks reject point-valued censored thresholds and bounds invented from approximate counts. M&A/leadership context requires updates through the event date.

Small hash-cached source leads assist review without automatically assigning values. Actual source rereading and counterevidence checks remain necessary. Hash/offset success verifies provenance, not every interpretation. Same-model self-review is not independent human coding reliability. True blockers remain PARTIAL, and inaccessible private-company information cannot be manufactured.

## Validation and development

The v1.4.0 source package passed 82 offline behavior tests, including English presentation, native-evidence preservation, company-neutral inputs, numerical bounds, source binding and installation. Run `python -m pytest -q tests` inside the extracted source package. See VALIDATION.json for the limited primary-source verification and remaining limits. These tests do not establish complete live extraction or semantic perfection for every company.

Historical project corpus counts describe prior research, not required inputs or sample-size quotas. Older archives remain historical versions; use the v1.4.0 links above for current installation.
