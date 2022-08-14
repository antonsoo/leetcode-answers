# 1965. Employees With Missing Information - Easy - no companies
# Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:
#The employee's name is missing, or The employee's salary is missing.

SELECT employee_id FROM Employees 
    WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION 
SELECT employee_id FROM Salaries 
    WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id; # can also do ORDER BY 1 (orders by the first column)


# what I wanted to do with my solution:
# SELECT T.employee_id
# FROM  
#   (SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
#    UNION 
#    SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id))
# AS T
# WHERE T.salary IS NULL OR T.name IS NULL
# ORDER BY employee_id;





# my failed solution:
# SELECT * FROM Employees AS e
# JOIN Salaries AS s ON e.employee_id=s.employee_id
# WHERE name is NULL or salary is NULL;
