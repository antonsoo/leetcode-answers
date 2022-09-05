# 1581. Customer Who Visited but Did Not Mk a Transa. - Easy - 2022Q1:Amzn

# works:
# SELECT customer_id, COUNT(V.visit_id) AS count_no_trans
# FROM Visits V LEFT JOIN Transactions T ON V.visit_id=T.visit_id
# WHERE T.visit_id IS NULL
# GROUP BY customer_id;

# Natural left join: finds the column to join on automatically
SELECT customer_id, COUNT(V.visit_id) AS count_no_trans
FROM Visits V NATURAL LEFT JOIN Transactions T # ON V.visit_id=T.visit_id
WHERE T.visit_id IS NULL
GROUP BY customer_id;   



# my worse try :
# two components: get the customers where they didn't make a transaction
# then have an internal selection to get the number of times those customers
#didn't make a transaction (just visited the store)...think in NULLs
# SELECT customer_id, COUNT(V.visit_id)
#     #(SELECT Count(T.visit_id) FROM Visit V LEFT JOIN Transactions T ON 
#     # V.visit_id=T.visit_id WHERE T.visit_id IS NULL
#     #)  <- commented this out
#     AS count_no_trans
# FROM Visits V LEFT JOIN Transactions T ON V.visit_id=T.visit_id
# WHERE T.visit_id IS NULL
# GROUP BY customer_id;
