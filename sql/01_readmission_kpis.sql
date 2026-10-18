
-- Hospital Readmission & Patient Outcomes Analytics
-- 01 - Key Performance Indicators (KPIs)

-- KPI 1: Total encounters
SELECT
    COUNT(*) AS total_encounters
FROM encounters;

-- KPI 2: Unique patients
SELECT
    COUNT(DISTINCT patient_nbr) AS unique_patients
FROM encounters;

-- KPI 3: Total 30-day readmissions
SELECT
    SUM(readmitted_30_days) AS readmissions_30_days
FROM encounters;

-- KPI 4: Overall 30-day readmission rate
SELECT
    COUNT(*) AS total_encounters,
    SUM(readmitted_30_days) AS readmissions_30_days,
    ROUND(
        100.0 * SUM(readmitted_30_days) / NULLIF(COUNT(*), 0),
        2
    ) AS readmission_rate_percent
FROM encounters;

-- KPI 5: Readmission status distribution
SELECT
    readmitted,
    COUNT(*) AS total_encounters,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage_of_encounters
FROM encounters
GROUP BY readmitted
ORDER BY total_encounters DESC;