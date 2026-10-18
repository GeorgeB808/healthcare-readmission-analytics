-- Hospital Readmission & Patient Outcomes Analytics
-- 06 - 30-Day Readmission by Length of Stay

SELECT
    time_in_hospital AS length_of_stay_days,

    COUNT(*) AS total_encounters,

    SUM(readmitted_30_days) AS readmissions_30_days,

    ROUND(
        100.0 * SUM(readmitted_30_days) / COUNT(*),
        2
    ) AS readmission_rate_percent

FROM encounters

WHERE time_in_hospital IS NOT NULL

GROUP BY time_in_hospital

ORDER BY time_in_hospital;




-- Key finding:
-- Observed 30-day readmission rates generally increased with length of stay
-- through approximately 10 days, rising from 8.18% for one-day encounters
-- to 14.35% for ten-day encounters.
--
-- Interpretation:
-- Length of stay may be useful for segmenting readmission patterns.
-- This is an observational association, not evidence of causation, because
-- length of stay may reflect patient complexity and clinical severity.