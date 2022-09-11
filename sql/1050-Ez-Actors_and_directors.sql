# 1050. Actors and Directors Who Cooperated At Least Three Times - Ez -  2022:Amzn

# dont forget: Cooperated at least three times! meaning three or more pairs in the data
SELECT actor_id, director_id FROM ActorDirector
GROUP BY director_id, actor_id  # need to GROUP BY both
HAVING COUNT(director_id) >= 3  # this will only GROUP BY this condition


# SELECT A.actor_id, A.director_id
# FROM ActorDirector A JOIN ActorDirector B 
# ON A.timestamp != B.timestamp 
#     AND A.actor_id = B.director_id;
