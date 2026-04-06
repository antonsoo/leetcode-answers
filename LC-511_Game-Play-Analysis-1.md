#511. Game Play Analysis I
#Solution link:https://leetcode.com/problems/game-play-analysis-i/solutions/7771997/game-play-analysis-i-sql-aggregation-win-hkso/
# Write your MySQL query statement below
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
