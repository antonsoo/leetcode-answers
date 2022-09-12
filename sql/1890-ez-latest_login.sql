# 1890. The Latest Login in 2020 - Ez - 2022Q3: Nothing
# Problem: max/last login, but only in the year 2020.

# using LIKE
SELECT user_id, MAX(time_stamp) AS last_stamp FROM Logins
WHERE time_stamp LIKE '2020%'
GROUP BY user_id

# second way, faster? By using the YEAR() function
# SELECT user_id, MAX(time_stamp) AS last_stamp FROM Logins
# WHERE YEAR(time_stamp) = 2020
# GROUP BY user_id
