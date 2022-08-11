# 1667. Fix Names in a Table - Easy - No companies
# Problem: Fix names so they all start with an uppercase letter and the rest of the letters are lowercase
# Funcs: CONCAT(strA, strB), UPPER(str), SUBSTR(str, index, length)
SELECT user_id, CONCAT( UPPER(SUBSTR(name,1,1)), 
                       LOWER(SUBSTR(name,2)) ) AS name 
FROM Users
ORDER BY user_id;
