#1141. User Activity for the Past 30 Days I - Easy - 2022Q3:FB

# note : activity_date > "2019-06-27" is not inclusive because June
#has 31 days, and they only wanted a 30 day gap.
# note #WHERE activity_type IS NOT NULL  # don't need this I think because
#there are no NULL values.

SELECT activity_date as day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date > "2019-06-27" AND activity_date <= "2019-07-27"
GROUP BY day;


# second way: add this after GROUP BY, and don't have a WHERE statement
# HAVING activity_date >= DATE_SUB('2019-07-27', INTERVAL 30 DAY)
