# 1378. Replace Employee ID With The Unique Identifier - Ez - 2020:Point72
# return in any order.  
# using GROUP BY fails, and we don't need it

SELECT unique_id, name
FROM Employees E NATURAL LEFT JOIN EmployeeUNI I
