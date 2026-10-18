-- Hospital Readmission & Patient Outcomes Analytics
-- 07 - 30-Day Readmission by Admission Type

SELECT
    admission_type_description AS admission_type,

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

GROUP BY admission_type_description

ORDER BY total_encounters DESC;


-- Key finding:
-- Emergency admissions represented the largest admission category,
-- with 53,990 encounters and 6,221 observed 30-day readmissions.
-- The readmission rate was 11.52%, compared with 10.39% for elective
-- admissions and 11.18% for urgent admissions.
--
-- Interpretation:
-- Emergency encounters account for a large share of this dataset and
-- may warrant further quality-improvement investigation. These observed
-- differences do not establish causation.
