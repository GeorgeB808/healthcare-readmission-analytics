-- Hospital Readmission & Patient Outcomes Analytics
-- 04 - 30-Day Readmission by Primary Diagnosis

SELECT
    diag_1 AS primary_diagnosis,
    COUNT(*) AS total_encounters,
    SUM(readmitted_30_days) AS readmissions_30_days,
    ROUND(
        100.0 * SUM(readmitted_30_days) / COUNT(*),
        2
    ) AS readmission_rate_percent,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage_of_total_encounters
FROM encounters
WHERE diag_1 IS NOT NULL
GROUP BY diag_1
ORDER BY total_encounters