SELECT traveltime, COUNT(*) AS frequency
FROM student_performance
WHERE address='R'
GROUP BY traveltime
ORDER BY 2 DESC;