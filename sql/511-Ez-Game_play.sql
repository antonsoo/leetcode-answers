# 511. Game Play Analysis I - Easy - 2022Q3:Amzn

SELECT player_id, MIN(event_date) AS first_login FROM Activity
GROUP BY player_id
