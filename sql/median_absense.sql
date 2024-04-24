with base as (SELECT sex,
                     absences
              FROM student_performance
              WHERE famrel IN (2, 3))
SELECT sex,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY absences) AS median_absences
FROM
    student_performance
GROUP BY
    sex;