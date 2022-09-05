# 184. Department Highest Salary - Medium - 2022Q3:Amzn

SELECT D.name AS Department, E.name AS Employee, Salary
FROM Employee E JOIN Department D 
ON E.departmentID = D.id  
WHERE (E.departmentID, Salary) IN 
    (SELECT departmentID, MAX(Salary) FROM Employee
    GROUP BY departmentID );
