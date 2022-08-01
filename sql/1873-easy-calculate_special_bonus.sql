# 1873. Calculate Special Bonus - 'Easy' - no companies
# Problem: The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
# notice how the entire case statement is inside the SELECT
SELECT employee_id, 
 CASE # u dont need to tab it, it's just for clarity
    WHEN (name NOT LIKE 'M%' AND (employee_id % 2) = 1) THEN salary
    ELSE salary = 0 
 END AS bonus # name this entire case statement output as 'bonus' 
FROM Employees
ORDER BY employee_id; # DESC


# second way by using boolean evaluations: 
SELECT employee_id, 
    salary * (employee_id % 2) * (name NOT LIKE 'M%') as bonus 
FROM Employees
ORDER BY employee_id;


# my failed attempt
# LEFT(name, 1) means take 1 leftmost char from string in name col
#SELECT employee_id, bonus FROM Employee
#IF LEFT(name, 1)='M' AND employee_id%2!=0 THEN bonus=salary
#ELSE bonus=0
#ORDER BY employee_id DESC;
