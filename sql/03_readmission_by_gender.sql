-- Hospital Readmission & Patient Outcomes Analytics
-- 03 - 30-Day Readmission by Gender

SELECT
    gender,
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
GROUP BY gender
ORDER BY total_encounters DESC;



-- Key finding:
-- Gender differences in observed 30-day readmission rates were minimal.
-- Female patients had an 11.25% rate compared with 11.06% among male
-- patients. Gender alone may not strongly distinguish readmission patterns
-- in this dataset; this observation does not establish causation.