# 1148. Article Views I - Easy - 2020:LinkedIn

# method 1: using DISTINCT and then sorting
SELECT DISTINCT author_id AS id FROM Views
WHERE author_id = viewer_id
ORDER BY id;

# method 2: using GROUP BY and then sorting
# SELECT author_id AS id FROM Views
# WHERE author_id = viewer_id
# GROUP BY id 
# ORDER BY id;

# method 3: "ORDER BY first. Use  another SELECT and an alias"
# SELECT id from (SELECT author_id AS id FROM Views 
# where author_id = viewer_id 
# ORDER BY id)a
# GROUP BY id 
# ORDER BY id;








# my failed query
# SELECT v1.author_id AS "id" FROM 
# Views v1 JOIN Views v2 ON v1.author_id = v2.viewer_id
# GROUP BY v1.author_id 
# ORDER BY v1.author_id
