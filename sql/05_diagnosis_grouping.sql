-- Hospital Readmission & Patient Outcomes Analytics
-- 05 - Primary Diagnosis Grouping

SELECT
    CASE
        WHEN diag_1 ~ '^250' THEN 'Diabetes'
        WHEN diag_1 >= '390' AND diag_1 <= '459' THEN 'Circulatory'
        WHEN diag_1 >= '460' AND diag_1 <= '519' THEN 'Respiratory'
        WHEN diag_1 >= '520' AND diag_1 <= '579' THEN 'Digestive'
        WHEN diag_1 >= '580' AND diag_1 <= '629' THEN 'Genitourinary'
        WHEN diag_1 >= '680' AND diag_1 <= '709' THEN 'Skin'
        WHEN diag_1 >= '710' AND diag_1 <= '739' THEN 'Musculoskeletal'
        WHEN diag_1 >= '780' AND diag_1 <= '799' THEN 'Symptoms / Signs'
        WHEN diag_1 >= '800' AND diag_1 <= '999' THEN 'Injury / Complications'
        WHEN diag_1 ~ '^V' THEN 'Supplementary / Encounter'
        WHEN diag_1 ~ '^E' THEN 'External Causes'
        ELSE 'Other / Unclassified'
    END AS diagnosis_group,

    COUNT(*) AS total_encounters,

    SUM(readmitted_30_days) AS readmissions_30_days,

    ROUND(
        100.0 * SUM(readmitted_30_days) / COUNT(*),
        2
    ) AS readmission_rate_percent

FROM encounters

WHERE diag_1 IS NOT NULL

GROUP BY diagnosis_group

ORDER BY total_encounters DESC;
