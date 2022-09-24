# 1407. Top Travellers - Ez - 2020:Point72

# COALESCENE(col, 0) will simply replace the NULL values with 0's

SELECT U.name, SUM(COALESCE(R.distance, 0)) AS travelled_distance
FROM Users U LEFT JOIN Rides R ON U.id = R.user_id
GROUP BY R.user_id
ORDER BY travelled_distance DESC, U.name ASC;

