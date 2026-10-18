SELECT
    CASE
        WHEN number_inpatient = 0 THEN '0 visits'
        WHEN number_inpatient = 1 THEN '1 visit'
        WHEN number_inpatient = 2 THEN '2 visits'
        WHEN number_inpatient BETWEEN 3 AND 4 THEN '3-4 visits'
        WHEN number_inpatient >= 5 THEN '5+ visits'
    END AS inpatient_utilization_group,

    COUNT(*) AS total_encounters,

    SUM(readmitted_30_days) AS readmissions_30_days,

    ROUND(
        100.0 * SUM(readmitted_30_days) / COUNT(*),
        2
    ) AS readmission_rate_percent

FROM encounters

GROUP BY
    CASE
        WHEN number_inpatient = 0 THEN '0 visits'
        WHEN number_inpatient = 1 THEN '1 visit'
        WHEN number_inpatient = 2 THEN '2 visits'
        WHEN number_inpatient BETWEEN 3 AND 4 THEN '3-4 visits'
        WHEN number_inpatient >= 5 THEN '5+ visits'
    END

ORDER BY
    MIN(number_inpatient);




-- Key finding:
-- Prior inpatient utilization showed an observed relationship with
-- 30-day readmission rates. Patients with no prior inpatient visits
-- had an 8.44% rate, compared with 12.92% for one prior visit and
-- 17.43% for two prior visits.
-- The rate increased to 21.36% for 3-4 prior visits and 36.41%
-- for five or more prior visits.
--
-- Interpretation:
-- Prior inpatient utilization may be useful for segmenting encounters
-- for further quality-improvement investigation. This association
-- does not establish causation. Interpret the highest-utilization
-- group's rate alongside its sample size.
