# 1158. Market Analysis I - Med/ez - 2020: Poshmark

# COUNT() ignores NULL values so don't need COALESCE().

SELECT U.user_id AS buyer_id, U.join_date, 
    COUNT(O.order_id) AS orders_in_2019
FROM Users U LEFT JOIN Orders O ON U.user_id=O.buyer_id
    AND YEAR(order_date)='2019' # or: order_date LIKE '2019%'
GROUP BY U.user_id;








