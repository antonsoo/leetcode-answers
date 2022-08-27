# 607. Sales Person - "Easy" - 2020:Amzn

# in the subquery, you're finding all the people with the sales_id
#that have sold with the company called "RED"
# then outside, you're choosing the names corresponding to the sales_id
#which did not use that company, so everyone who's not in the subquery outp.
SELECT name FROM SalesPerson
WHERE sales_id NOT IN
    (SELECT O.sales_id FROM Orders O 
     NATURAL JOIN Company C #ON C.com_id = O.com_id
    WHERE C.name = 'RED');
