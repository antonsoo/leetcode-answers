# 1587. Bank Account Summary II - Ez - 2022Q3:Uber

# return in any order
# left join in case there are users with no transactions, by default they have all have at least 0 balance
# actually just the normal inner JOIN works here

SELECT U.name, SUM(T.amount) AS balance
FROM Users U NATURAL LEFT JOIN Transactions T
GROUP BY T.account
HAVING balance > 10000;
