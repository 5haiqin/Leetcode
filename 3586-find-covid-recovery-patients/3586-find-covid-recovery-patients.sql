SELECT
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(
        MIN(ct2.test_date),
        MIN(ct1.test_date)
    ) AS recovery_time
FROM patients p
JOIN covid_tests ct1
    ON p.patient_id = ct1.patient_id
   AND ct1.result = 'Positive'
JOIN covid_tests ct2
    ON p.patient_id = ct2.patient_id
   AND ct2.result = 'Negative'
   AND ct2.test_date > ct1.test_date
GROUP BY
    p.patient_id,
    p.patient_name,
    p.age
HAVING
    COUNT(*) > 0
ORDER BY
    recovery_time ASC,
    p.patient_name ASC;