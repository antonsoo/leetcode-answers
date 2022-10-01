# 1303. Find the Team Size - Ez - SQL70 - 2020: Amzn
# return in any order
# assuming each employee is only on one team


# window function:   # can put any column in the COUNT() and it will work
# the window function works similar to map() in Python, applies the func to each elem
SELECT employee_id, COUNT(*) OVER(PARTITION BY team_id) AS team_size 
FROM Employee


# no window function: the idea is to left join to make sure every employee_id
#gets to have its own team_size attached to it, because there will be duplicates;
#duplicates that come from the team_id being the same for multiple employee_id
# SELECT employee_id, team_size
# FROM Employee AS A NATURAL LEFT JOIN (
#       SELECT team_id, COUNT(employee_id) AS team_size
#       FROM Employee
#       GROUP BY team_id
#     ) AS B
# ##ON A.team_id = B.team_id









# failed attempt 1
# SELECT employee_id, COUNT(employee_id) AS team_size  
# FROM Employee
# GROUP BY team_id
# - 
# failed attempt 2
#     FROM ( 
#         SELECT employee_id, COUNT(employee_id) FROM Employee
    
    
#     ) AS Temp
    
 


