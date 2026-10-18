SELECT
    CASE
        WHEN number_emergency = 0 THEN '0 visits'
        WHEN number_emergency = 1 THEN '1 visit'
        WHEN number_emergency = 2 THEN '2 visits'
        WHEN number_emergency BETWEEN 3 AND 4 THEN '3-4 visits'
        WHEN number_emergency >= 5 THEN '5+ visits'
    END AS emergency_utilization_group,

    COUNT(*) AS total_encounters,

    SUM(readmitted_30_days) AS readmissions_30_days,

    ROUND(
        100.0 * SUM(readmitted_30_days) / COUNT(*),
        2
    ) AS readmission_rate_percent

FROM encounters

GROUP BY
    CASE
        WHEN number_emergency = 0 THEN '0 visits'
        WHEN number_emergency = 1 THEN '1 visit'
        WHEN number_emergency = 2 THEN '2 visits'
        WHEN number_emergency BETWEEN 3 AND 4 THEN '3-4 visits'
        WHEN number_emergency >= 5 THEN '5+ visits'
    END

ORDER BY
    MIN(number_emergency);


-- Interpretation:
-- This query groups encounters by the number of prior emergency-department
-- visits recorded in number_emergency.
-- Compare readmission rates across groups to identify patterns that may
-- warrant further investigation. These associations do not establish causation.