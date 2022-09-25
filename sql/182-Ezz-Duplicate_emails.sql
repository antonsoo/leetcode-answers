# 182. Duplicate Emails - Ezz - 2020:Msft/Uber

# Note, don't need to do "SELECT email AS Email" just do "SELECT Email"

# Sub-query:
SELECT Email FROM    
    (SELECT email, COUNT(email) AS counts FROM Person
        GROUP BY email
    ) AS Temp
WHERE counts > 1;

# Having:  Having is like "WHERE" but for aggregates. Use it after GROUP BY
# SELECT Email FROM Person
# GROUP BY Email
# HAVING COUNT(Email) > 1;

# Self-join
# SELECT DISTINCT p1.Email FROM Person p1, Person p2
# WHERE p1.Email = p2.Email and p1.id != p2.id;
