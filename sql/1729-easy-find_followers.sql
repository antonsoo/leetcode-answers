# 1729. Find Followers Count - Easy - 2020:Tesla

SELECT user_id, COUNT(DISTINCT follower_id) AS followers_count
FROM Followers
GROUP BY user_id;
