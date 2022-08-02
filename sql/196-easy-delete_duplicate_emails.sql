# 196. Delete Duplicate Emails - Easy - 2020/21:Amzn/FB/Uber

# subquery method. GROUP BY will automatically get rid of the dupl's
#only the unique emails will remain, and then you're selecting the 
#smallest id's from those. So that whole subquery is what will *NOT*  
#be deleted. Hence "NOT IN," every other Id will be deleted! 
/*
DELETE FROM Person WHERE Id NOT IN
(SELECT * FROM (SELECT MIN(Id) FROM Person GROUP BY Email) as p);
*/

# official solution method using a self-join done with a WHERE:
#so you see, it will find the emails that are the same, and then
#it will delete the emails with the IDs that are bigger, so only the
#smallest IDs will be kept.
/*
DELETE table1 FROM Person table1, Person table2 # this is like a JOIN
WHERE table1.Email = table2.email AND table1.ID > table2.ID;
*/

# Using JOIN. Solution from user mcello0318:
# He is doing the same thing as above but flipping the names
DELETE table2 
FROM Person table1 JOIN Person table2 ON 
table1.Email = table2.Email WHERE table1.Id < table2.Id;



/*
# EX: Select all distinct emails only once and when there *is* a dupl.
#then select the duplicate with the lower id num.
# Algo: Join the table on itself (u dont need JOIN, use FROM & WHERE)
SELECT p1.* # select everything from table1 given the condition below
FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id
;
*/
