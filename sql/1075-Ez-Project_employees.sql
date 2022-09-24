# 1075. Project Employees I - Ez - 2020:FB
# Clarificiation questions: Can experience_years be NULL? Then use COALESCE
# Note: Return any order. Round to 2 dec digits

# Left JOIN will work if we also want to include projects where there are no employees yet. 
SELECT P.project_id, ROUND(AVG(E.experience_years), 2) AS average_years
FROM Project P NATURAL LEFT JOIN Employee E
GROUP BY P.project_id;

# Note: instead of saying "NATURAL .."  we can use USING(column_name) after the name of the second table , or use "ON P.col=E.col"  
