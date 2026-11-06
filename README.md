# Layoff Research Skills

**Current release: v1.5.7-rc4 proposal-scope build**

Two reusable skills collect public layoff announcements and annual company disclosures for research. Supply company names and periods. The skills include definitions, templates, evidence checks, and English Excel exports.

- [Download the installation package](two-skills-v1.5.7-rc4-proposal-scope.zip)
- [Download the complete source package](layoff-research-skills-v1.5.7-rc4-github.zip)
- [First-use prompt](FIRST_USE_PROMPT.md)
- [Fixed output scope](OUTPUT_SCOPE.md)
- [Changelog](CHANGELOG.md)

| Skill | Coverage | Output grain |
| --- | --- | --- |
| layoff-announcement-tracker | Layoff reasons, dates, workforce impact, affected parties, and company context | Announcement by default, with optional canonical plan grouping |
| listed-filing-extractor | Proposal variables for HR, AI and new technology, and financial disclosures | One company and fiscal year per row |

## Install

Extract the installation package and open a terminal in the extracted directory. Python 3.10 or newer is required.

```bash
python3 -m pip install -r requirements.txt
python3 install.py --target workbuddy
```

Other supported targets are `workbuddy-ai` and `codex`. Add `--force` to replace an existing installation. Start a fresh filing workspace to bind the updated proposal-scope schema, then use the first-use prompt linked above.

## Output and review

Each workbook uses an English `Results` sheet. Keep the source archive, audit, and review queue with the workbook. The event audit distinguishes announcement rows from canonical plan counts. One-sided numerical thresholds retain their bounds, and the filing workflow records section-level review for negative findings and amounts that are not separately disclosed.

The complete source package contains the runtime, templates, and validation materials. Use its bundled validation reports to review tested behavior and coverage limits. Source hashes verify provenance. Review the underlying evidence before drawing research conclusions.
