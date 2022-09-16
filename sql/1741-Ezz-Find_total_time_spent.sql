# 1741. Find Total Time Spent by Each Employee - Ezz - 2020:Amzn
# Very good exercise for demonstrating GROUP BY and the orders of GROUP BY

SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id
