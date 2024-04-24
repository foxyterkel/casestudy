SELECT famsize, failures, COUNT(*) AS frequency
FROM student_performance
GROUP BY famsize, failures
ORDER BY famsize, frequency DESC;