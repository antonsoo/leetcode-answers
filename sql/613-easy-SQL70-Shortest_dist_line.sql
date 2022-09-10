# 613. Shortest Distance in a Line - Easy - SQL70 - 2020:Amzn

# smartest solution from user ztrue:
SELECT MIN(A.x - B.x) AS shortest
FROM Point A JOIN Point B 
ON A.x > B.x;


# official sol:
# SELECT MIN(ABS(A.x - B.x)) AS shortest
# FROM Point A JOIN Point B 
# ON A.x != B.x; 


# my attempt (works)
# SELECT MIN(dist) AS shortest FROM
#  (
#     SELECT ABS(A.x - B.x) AS dist
#     FROM Point A JOIN Point B 
#     ON A.x != B.x
#  ) AS temp;
