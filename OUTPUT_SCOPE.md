# Fixed output scope v1.4.0

Each Excel has exactly one Results worksheet. All presentation is English, with native evidence preserved in a separate canonical archive. No original dataset or chat memory is required. Historical sample counts are background, not run quotas. All company types may be inputs; actual available public disclosures determine coverage.

## listed-filing-extractor

42 business fields and 48 base columns.

| Field | Meaning | Type |
|---|---|---|
| headcount | Year-end workforce size | number |
| training_costs | Training and development cost disclosure | text |
| training_costs_disclosed | Training and development cost disclosure disclosed (0/1/null) | binary |
| training_costs_amount | Training and development expense amount | number |
| layoff_statement | Layoff or workforce-reduction disclosure | text |
| layoff_statement_disclosed | Layoff or workforce-reduction disclosure disclosed (0/1/null) | binary |
| mdna_hr_discussion | MD&A discussion of HR topics | text |
| mdna_hr_discussion_disclosed | MD&A discussion of HR topics disclosed (0/1/null) | binary |
| restructuring_narrative | Restructuring and cost-saving narrative | text |
| restructuring_narrative_disclosed | Restructuring and cost-saving narrative disclosed (0/1/null) | binary |
| labor_talent_risk | Labor and talent risk disclosure | text |
| labor_talent_risk_disclosed | Labor and talent risk disclosure disclosed (0/1/null) | binary |
| talent_competition_risk | Talent competition and hiring risk | text |
| talent_competition_risk_disclosed | Talent competition and hiring risk disclosed (0/1/null) | binary |
| ai_products | AI products and initiatives | text |
| ai_products_disclosed | AI products and initiatives disclosed (0/1/null) | binary |
| ai_integration | AI integration into operations | text |
| ai_integration_disclosed | AI integration into operations disclosed (0/1/null) | binary |
| ai_adoption | Actual AI technology adoption | text |
| ai_adoption_disclosed | Actual AI technology adoption disclosed (0/1/null) | binary |
| new_tech_adoption | Actual new-technology use or adoption | text |
| new_tech_adoption_disclosed | Actual new-technology use or adoption disclosed (0/1/null) | binary |
| ai_risk_disclosure | AI-related risk factors | text |
| ai_risk_disclosure_disclosed | AI-related risk factors disclosed (0/1/null) | binary |
| ai_investment_disclosure | AI investment disclosure | text |
| ai_investment_disclosure_disclosed | AI investment disclosure disclosed (0/1/null) | binary |
| ai_investment_amount | Explicit AI investment amount | number |
| ai_opex_amount | Explicit AI operating expense | number |
| tech_opex_amount | Reported technology operating expense | number |
| rd_expense | Explicit research and development expense | number |
| capitalized_software | Capitalized software development disclosure | text |
| capitalized_software_disclosed | Capitalized software development disclosure disclosed (0/1/null) | binary |
| capitalized_software_amount | Current-year capitalized software development additions | number |
| revenue | Revenue | number |
| operating_income | Operating income or loss | number |
| restructuring_charges | Recognized restructuring expense | number |
| total_comp_expense | Company-wide employee compensation expense | number |
| ai_exec_comp | AI-linked compensation including executive awards | text |
| ai_exec_comp_disclosed | AI-linked compensation including executive awards disclosed (0/1/null) | binary |
| ai_executive_comp_amount | Explicit AI-linked compensation amount | number |
| tech_opex_disclosure | Technology and infrastructure operating-cost narrative | text |
| tech_opex_disclosure_disclosed | Technology and infrastructure operating-cost narrative disclosed (0/1/null) | binary |

## layoff-announcement-tracker

43 business fields and 49 base columns.

| Field | Meaning | Type |
|---|---|---|
| company_name_at_event | Legal company and operating unit at the event | text |
| announcement_date | Announcement date | date |
| announcement_date_raw | Original date wording | text |
| announcement_date_precision | Date precision | text |
| effective_date_start | Implementation start date | date |
| effective_date_end | Implementation end date | date |
| announcement_status | Announcement or implementation status | text |
| original_announcement_url | Original issuer announcement URL | text |
| original_announcement_status | Original announcement search status | text |
| announcement_source_kind | Evidence source kind | text |
| source_publication_date | Source publication date | date |
| layoff_count | Reported point count of affected people or roles | number |
| layoff_count_lower | Explicit lower threshold for affected people or roles | number |
| layoff_count_upper | Explicit upper threshold for affected people or roles | number |
| layoff_count_qualifier | Count qualifier and boundary direction | text |
| layoff_count_basis | Count population and measurement basis | text |
| layoff_percentage | Reported point percentage | number |
| layoff_percentage_lower | Explicit lower percentage threshold | number |
| layoff_percentage_upper | Explicit upper percentage threshold | number |
| layoff_percentage_qualifier | Percentage qualifier and boundary direction | text |
| layoff_percentage_denominator | Percentage denominator population | text |
| numerical_claim_raw | Original numerical claim | text |
| stated_reason_text | Stated layoff reason and attribution | text |
| reason_attribution | Speaker or reporter attribution | text |
| ma_activity | Event-time M&A activity | text |
| leadership_transition | Event-time leadership changes | text |
| firm_size | Event-time company workforce size | number |
| firm_size_basis | Workforce-size population basis | text |
| firm_size_as_of | Workforce-size information date | date |
| affected_parties | Known affected teams, roles or groups | text |
| listed_at_event | Listed status at the event | binary |
| exchange_at_event | Exchange at the event | text |
| ticker_at_event | Ticker at the event | text |
| cik | SEC company identifier if applicable | text |
| country | Country or jurisdiction | text |
| plan_identity_verified | Plan identity verification | binary |
| event_type | Workforce-action type | text |
| related_plan_id | Related plan identifier | text |
| plan_relationship | Relationship to the other plan | text |
| company_history | Company history known at the event | text |
| founding_year | Founding or incorporation year with entity basis | integer |
| products_services | Products and services at the event | text |
| business_model | Business model at the event | text |
