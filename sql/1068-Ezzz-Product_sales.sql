# 1068. Product Sales Analysis I - SQL70 - Ezzzzz - 2020:Amzn
# Not a good question, too easy and too little fail cases, like maybe no duplicates or null values.

SELECT product_name, year, price
FROM Sales S NATURAL JOIN Product P;
 
 
 
 
 
 # some guy's solution who claims it runs faster, but it doesnt
# SELECT DISTINCT 
#     P.product_name, S.year, S.price 
# FROM 
#     (SELECT DISTINCT product_id, year, price FROM Sales) S
# INNER JOIN
#     Product AS P
# USING (product_id);
