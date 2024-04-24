with base as (
SELECT pstatus, fjob, COUNT(*) AS frequency
FROM student_performance
GROUP BY pstatus, fjob),
ranked AS (
  SELECT
    pstatus,
    fjob,
    frequency,
    ROW_NUMBER() OVER (PARTITION BY pstatus ORDER BY frequency DESC) AS row_num
  FROM
    base
)
SELECT * FROM ranked WHERE row_num<=3;