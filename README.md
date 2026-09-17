# healthcare-readmission-analytics
End-to-end healthcare data analytics project analyzing hospital readmissions and patient outcomes using PostgreSQL, SQL, and Power BI.
# Hospital Readmission & Patient Outcomes Analytics

## Overview

An end-to-end healthcare data analytics project analyzing hospital encounters and 30-day readmissions to identify patterns in patient outcomes, healthcare utilization, and operational performance.

The project demonstrates practical data analyst skills including data profiling, data cleaning, SQL analysis, KPI development, data visualization, and business intelligence dashboarding.

## Business Problem

Hospital leadership wants to better understand patterns associated with 30-day hospital readmissions.

The goal of this analysis is to examine patient and encounter data, identify meaningful patterns, and communicate findings through an interactive Power BI dashboard.

## Business Objective

Analyze de-identified healthcare data to:

* Measure 30-day readmission rates
* Analyze readmissions across patient demographics
* Identify diagnoses associated with readmissions
* Examine length of stay and healthcare utilization
* Identify patient and encounter segments that may warrant further investigation
* Develop data-driven insights for healthcare operations and quality improvement

## Key Business Questions

1. How many hospital encounters are represented in the dataset?
2. How many unique patients are represented?
3. What is the overall 30-day readmission rate?
4. How does readmission rate vary by age group?
5. How does readmission rate vary by gender?
6. Which diagnoses are associated with the highest number of readmissions?
7. Which diagnosis groups have the highest observed readmission rates?
8. How does length of stay differ between readmitted and non-readmitted encounters?
9. Does admission type appear to be associated with readmission?
10. Which patient or encounter segments should hospital leadership investigate further?

## Key Performance Indicators

The analysis will evaluate metrics including:

* Total Encounters
* Unique Patients
* 30-Day Readmission Rate
* Total Readmissions
* Average Length of Stay
* Median Length of Stay
* Average Encounters per Patient
* Additional KPIs supported by the selected dataset

## Technology Stack

* PostgreSQL
* SQL
* Microsoft Power BI
* GitHub
* Markdown
* Python (if useful for data preparation or validation)

## Project Workflow

```text
Public Healthcare Dataset
        ↓
Data Profiling
        ↓
Data Cleaning
        ↓
PostgreSQL
        ↓
SQL Analysis
        ↓
KPI Development
        ↓
Power BI Dashboard
        ↓
Key Findings
        ↓
Business Recommendations
```

## Repository Structure

```text
healthcare-readmission-analytics/
│
├── README.md
├── data/
│   ├── raw/
│   └── cleaned/
├── sql/
├── powerbi/
├── screenshots/
└── docs/
```

## Healthcare Data & Privacy

This project will use publicly available, de-identified healthcare data for educational and portfolio purposes.

No private patient information will be used in this project.

The project will document relevant data privacy considerations and limitations associated with the selected dataset.

## Project Status

**Phase 1 — Project Definition**

* [x] Define business problem
* [x] Define business objective
* [x] Identify stakeholder
* [x] Define business questions
* [x] Define initial KPIs
* [x] Select technology stack
* [ ] Select healthcare dataset
* [ ] Profile raw data
* [ ] Clean data
* [ ] Load data into PostgreSQL
* [ ] Perform SQL analysis
* [ ] Build Power BI dashboard
* [ ] Document findings
* [ ] Develop recommendations
* [ ] Complete final portfolio documentation

