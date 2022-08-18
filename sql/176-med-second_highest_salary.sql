# 176. Second Highest Salary - Med/Easy - 2022:Amzn/Goog

# LIMIT 1 means it will return only 1 row from the selection
# OFFSET 1 means it will skip the first row from your query
# this solution: Orders/finds the distinct salaries from high to low, 
#then it selects the second item in that query
#  If you just use one select it will fail in the case there is no second highest salary
SELECT
    (SELECT DISTINCT Salary FROM Employee
        ORDER BY Salary DESC LIMIT 1 OFFSET 1) AS SecondHighestSalary;
        
        
# second way: 
SELECT
    IFNULL((SELECT DISTINCT Salary FROM Employee
       ORDER BY Salary DESC LIMIT 1 OFFSET 1),
      NULL) AS SecondHighestSalary;
