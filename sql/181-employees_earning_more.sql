/* 181 -  Easy - Employees Earning More Than Their Managers - 2022Q1: Amzn>FB
Manager-id is the id of their manager!
*/

SELECT 
    a.name AS 'Employee'
FROM                   -- make a copy (cartesian product) of the two tables
    Employee AS a, 
    Employee AS b
WHERE                   -- select employees managed by a particular manager, who have salaries larger than their manager
    a.managerID = b.id  -- in SQL you don't use ==
        AND a.salary > b.salary  -- employee's salary is greater than their manager's 
;


# second way:
# SELECT
#      a.NAME AS Employee
# FROM Employee AS a JOIN Employee AS b
#      ON a.ManagerId = b.Id
#      AND a.Salary > b.Salary
# ;


# my failed attempt:
# go through the list, if the current person is a manager, go to the person he is managing
#and check if he is earning more than his manager's money
# Write your MySQL query statement below
# SELECT name 
# CASE 
# WHEN managerId != Null 
#     THEN
#         curr_managers_salary = salary
#         GOTO id of managerId
#         CASE
#             WHEN salary > curr_managers_salary THEN name
                
#         END 
        
#     END

# END AS Employee
# FROM Employee
