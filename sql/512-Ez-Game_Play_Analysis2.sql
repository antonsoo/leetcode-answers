# 512. Game Play Analysis II  - Ez/Med? - SQL70 - 2020:GSNGames


# report the device that is first logged in **for each player.**
# Return the result table in any order.

# window function approach:  
# I don't understand why the alias here needs to be same as one of the columns
SELECT DISTINCT player_id, FIRST_VALUE(device_id)
    OVER (PARTITION BY player_id ORDER BY event_date) AS device_id
FROM Activity;


# need a subquery here because the subquery uses an event_date but we don't want to return that.
# SELECT player_id, device_id
# FROM Activity
# WHERE (player_id, event_date) IN 
#     (
#     SELECT player_id, MIN(event_date)
#     FROM Activity
#     GROUP BY player_id
#     )
