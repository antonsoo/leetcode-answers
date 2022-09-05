# 586. Customer Placing the Largest Number of Orders - Easy - 2022:Goog

SELECT customer_number FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC # yes you can ORDER BY a function...
LIMIT 1;  # take the top 1, aka highest/max number of orders


# my failed code: error for MySQL not supporting the subquery
# SELECT customer_number FROM Orders
# WHERE customer_number IN 
#     (SELECT customer_number, COUNT(DISTINCT order_number)
#         FROM Orders
#         ORDER BY customer_number DESC
#         LIMIT 1
#     );


# from LC user gavinguojia:
# Follow up: What if more than one customer have the largest number of orders, can you find all the customer_number in this case?
# SELECT customer_number
# FROM orders
# Group BY customer_number
# HAVING  count(order_number) = 
# (SELECT max(numOfOrder)
# FROM
#     (SELECT customer_number,count(order_number) as numOfOrder
#     FROM orders
#     Group By customer_number) as temp)
