# Data Profiling Report

## Dataset

**Dataset:** Diabetes 130-US Hospitals for Years 1999–2008

**Source:** UCI Machine Learning Repository

**Purpose:** Analyze hospital encounters involving patients with diabetes and identify patterns associated with 30-day readmissions.

## Dataset Overview

Initial profiling identified:

* **101,766 hospital encounters**
* **71,518 unique patients**
* **50 columns**
* **101,766 unique encounter IDs**
* **0 duplicate encounter IDs**

The dataset is analyzed primarily at the **hospital encounter level**. Because individual patients may have multiple encounters, patient-level and encounter-level metrics will be distinguished throughout the analysis.

## Readmission Distribution

| Readmission Outcome       |  Encounters |  Percentage |
| ------------------------- | ----------: | ----------: |
| No readmission            |      54,864 |      53.91% |
| Readmitted after 30 days  |      35,545 |      34.93% |
| Readmitted within 30 days |      11,357 |      11.16% |
| **Total**                 | **101,766** | **100.00%** |

### Primary Outcome Definition

For this project, a **30-day readmission** is defined as an encounter where:

`readmitted = '<30'`

The initial descriptive baseline is **11.16% of encounters** classified as 30-day readmissions.

This percentage is descriptive and does not establish that any particular patient characteristic, diagnosis, or operational factor caused readmission.

## Missing Data

Two fields contain substantial missing values:

| Field           | Missing Values | Missing Percentage |
| --------------- | -------------: | -----------------: |
| `max_glu_serum` |         96,420 |             94.75% |
| `A1Cresult`     |         84,748 |             83.28% |

These fields will be evaluated during the data-cleaning and feature-selection stages rather than automatically removing records containing missing values.

## Data Quality Observations

The initial profiling identified:

* No duplicate encounter IDs.
* Multiple encounters can belong to the same patient.
* The dataset contains a mixture of numeric and categorical fields.
* The `readmitted` field provides the primary outcome used for this project.
* Several clinical measurement fields have substantial missingness.
* Additional categorical fields require interpretation and potentially mapping before analysis.

## Initial Analytical Considerations

The analysis will distinguish between:

* **Encounter-level metrics**, such as total encounters and readmission rate.
* **Patient-level metrics**, such as unique patients.
* **Utilization measures**, including previous outpatient, emergency, and inpatient encounters.
* **Clinical and operational characteristics**, including diagnoses, admission type, length of stay, and number of procedures or medications.

Further data cleaning and validation will be performed before the dataset is loaded into PostgreSQL.

## Next Step

The next stage is to identify fields required for the business questions, evaluate categorical values and missing-value patterns, and create a cleaned analytical dataset for SQL analysis.
