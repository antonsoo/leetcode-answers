# 183. Customers Who Never Order - Easyy - Bloom/Amzn/etc
# Problem: report customers that haven't made orders.
# i.e., return id's from table1 that are not used in the table2.
# note: LEFT JOIN ... WHERE .. IS NULL is like exclusive left join.
# note: Orders.id are the order id's, they don't correspond to customer names unlike
# note: can also do Customers.name but there's only one 'name' anyway
SELECT name AS "Customers" FROM Customers
LEFT JOIN Orders ON Customers.id = Orders.CustomerId
WHERE Orders.CustomerId IS NULL;

# second way, using a subquery:
#SELECT name as "Customers" FROM Customers
#WHERE Customers.id NOT IN (SELECT CustomerId FROM Orders);
