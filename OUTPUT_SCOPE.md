# Output scope for v3.0.3

Each workbook has one English worksheet named `Results`. Supporting files retain audit records, source URLs and original-language evidence.

## Layoff announcements

`1_layoff_announcements.xlsx` has one row per verified event or distinct plan. The 13 columns contain four identifiers (plan ID, company ID, company name and announcement date) and nine research variables:

- Company-stated layoff reason
- M&A activity
- Leadership transition
- Company history
- Firm size
- Founding year
- Products or services
- Business model
- Known parties affected

## Listed-company filings

`2_listed_company_filings.xlsx` has one row per company and fiscal year. The default window is FY2019–FY2025. The 24 base columns include company ID, company name, fiscal year and 21 research fields:

| Category | Fields |
|---|---|
| HR | Workforce size, training and development cost amount, labor and talent risk, competition and hiring risk, MD&A HR discussion, restructuring and cost-saving narrative |
| AI and technology | AI products and initiatives, AI integration, AI adoption, AI risks, AI investment narrative, AI investment amount, technology and infrastructure operating expense, R&D expense, capitalized software development cost amount |
| Financial and compensation | Revenue, operating income, restructuring charges, total employee compensation expense, AI-linked compensation disclosure, AI-linked executive compensation amount |

The bundled schemas and templates define exact field names and order. See the [first-use prompts](FIRST_USE_PROMPT.md) and [installation package](two-skills-v3.0.3-install.zip).
